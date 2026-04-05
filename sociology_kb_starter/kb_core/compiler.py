from __future__ import annotations

from collections import defaultdict
from pathlib import Path
import json

from pydantic import ValidationError

from kb_core.config import SETTINGS
from kb_core.extraction import extract_text
from kb_core.graph_index import build_graph_index
from kb_core.llm import LLMClient
from kb_core.models import CompilationResult, CompiledSourcePayload, DocumentStatus, ExtractionStatus
from kb_core.storage import list_raw_documents, read_metadata, update_metadata_status, write_note
from kb_core.utils import list_files_recursive, load_markdown_file, slugify, utc_now_iso, wikilink, write_text

SOURCE_PROMPT = """You are compiling a sociology knowledge base.
Return strict JSON with keys: title, summary, core_ideas, concepts, authors, methods, exam_questions, open_questions, source_anchors.
Rules:
- Be conservative and grounded in the source text.
- Do not invent references or page numbers.
- Keep unknown fields short.
"""

FALLBACK_SUMMARY_LIMIT = 1200

# Text length thresholds for smart chunking
_MAX_EXCERPT_CHARS = 32000  # ~8k tokens, well within Groq's 128k context
_HEAD_CHARS = 24000
_TAIL_CHARS = 8000


def compile_all_raw_documents() -> list[CompilationResult]:
    results = [compile_raw_document(item["path"]) for item in list_raw_documents()]
    rebuild_indexes()
    return results


def compile_raw_document(raw_path: Path) -> CompilationResult:
    metadata = read_metadata(raw_path)
    update_metadata_status(raw_path, status=DocumentStatus.COMPILING)

    extraction = extract_text(raw_path)
    if extraction.status in {ExtractionStatus.UNSUPPORTED, ExtractionStatus.ENCRYPTED, ExtractionStatus.PARSE_ERROR, ExtractionStatus.EMPTY}:
        update_metadata_status(
            raw_path,
            status=DocumentStatus.PARSE_FAILED,
            error_category=extraction.error_category,
            error_message=extraction.message,
        )
        return CompilationResult(
            ok=False,
            raw_path=str(raw_path),
            status=DocumentStatus.PARSE_FAILED,
            message=extraction.message,
            error_category=extraction.error_category,
            extraction=extraction,
        )

    payload = _build_compilation_payload(raw_path, extraction.text, metadata.semester, metadata.course)
    compiled = _compile_payload(raw_path, extraction.text, payload)

    try:
        note_path = _write_source_note(raw_path, metadata.semester, metadata.course, metadata.manual_concepts, metadata.manual_authors, compiled["payload"], compiled["provider"], compiled["model"])
        _store_open_questions(slugify(compiled["payload"].title), compiled["payload"].open_questions, metadata.semester, metadata.course)
        update_metadata_status(raw_path, status=DocumentStatus.COMPILED, compiled_note_path=str(note_path.relative_to(SETTINGS.kb_root)))
        return CompilationResult(
            ok=True,
            raw_path=str(raw_path),
            note_path=str(note_path),
            status=DocumentStatus.COMPILED,
            message="Compilation finished successfully.",
            extraction=extraction,
            llm_provider=compiled["provider"],
            llm_model=compiled["model"],
        )
    except Exception as exc:
        update_metadata_status(
            raw_path,
            status=DocumentStatus.COMPILE_FAILED,
            error_category="note_write_failure",
            error_message=str(exc),
        )
        return CompilationResult(
            ok=False,
            raw_path=str(raw_path),
            status=DocumentStatus.COMPILE_FAILED,
            message="Compilation failed while writing note artifacts.",
            error_category="note_write_failure",
            extraction=extraction,
            details={"error": str(exc)},
        )


def _build_compilation_payload(raw_path: Path, text: str, semester: str, course: str) -> dict:
    return {
        "source_path": str(raw_path.relative_to(SETTINGS.kb_root)),
        "semester": semester,
        "course": course,
        "filename": raw_path.name,
        "text_excerpt": _smart_excerpt(text),
    }


def _smart_excerpt(text: str) -> str:
    """Page-aware text excerpt: send full text if short, head+tail otherwise."""
    if len(text) <= _MAX_EXCERPT_CHARS:
        return text
    # Find the last [Page N] marker within the head budget
    head = text[:_HEAD_CHARS]
    last_marker = head.rfind("\n\n[Page ")
    if last_marker > _HEAD_CHARS // 2:
        head = text[:last_marker]
    # Find the first [Page N] marker within the tail budget
    tail_start = len(text) - _TAIL_CHARS
    tail = text[tail_start:]
    first_marker = tail.find("\n\n[Page ")
    if first_marker != -1:
        tail = tail[first_marker:]
    return head + "\n\n[...content truncated...]\n" + tail


def _compile_payload(raw_path: Path, text: str, payload: dict) -> dict:
    llm = LLMClient()
    llm_result = llm.complete(SOURCE_PROMPT, json.dumps(payload, ensure_ascii=False, indent=2), max_tokens=4000) if llm.available() else None
    if llm_result and llm_result.content:
        parsed = _parse_compiled_payload(llm_result.content, raw_path, text)
        return {"payload": parsed, "provider": llm_result.provider, "model": llm_result.model}
    return {"payload": _fallback_payload(raw_path, text), "provider": "fallback", "model": "fallback"}


def rebuild_indexes() -> None:
    source_notes = _load_source_notes()
    concept_map: dict[str, list[dict]] = defaultdict(list)
    author_map: dict[str, list[dict]] = defaultdict(list)
    course_map: dict[str, list[dict]] = defaultdict(list)

    for note in source_notes:
        front = note["frontmatter"]
        course_map[str(front.get("course", "general"))].append(note)
        for concept in front.get("concepts", []):
            concept_map[str(concept)].append(note)
        for author in front.get("authors", []):
            author_map[str(author)].append(note)

    for concept, notes in concept_map.items():
        write_note(
            SETTINGS.concepts_dir / f"{slugify(concept)}.md",
            {
                "id": slugify(concept),
                "title": concept,
                "note_type": "concept",
                "updated_at": utc_now_iso(),
                "source_notes": [str(item["path"].relative_to(SETTINGS.kb_root)) for item in notes],
            },
            _build_entity_body(concept, notes, "concept"),
        )

    for author, notes in author_map.items():
        write_note(
            SETTINGS.authors_dir / f"{slugify(author)}.md",
            {
                "id": slugify(author),
                "title": author,
                "note_type": "author",
                "updated_at": utc_now_iso(),
                "source_notes": [str(item["path"].relative_to(SETTINGS.kb_root)) for item in notes],
            },
            _build_entity_body(author, notes, "author"),
        )

    for course, notes in course_map.items():
        all_concepts = sorted({c for n in notes for c in n["frontmatter"].get("concepts", [])})
        all_authors = sorted({a for n in notes for a in n["frontmatter"].get("authors", [])})
        body = "\n".join(
            [
                "## Scope",
                f"Sociology course node for **{course}**.",
                "",
                "## Core concepts",
                "\n".join(f"- {wikilink(c, c)}" for c in all_concepts) or "- None yet",
                "",
                "## Authors",
                "\n".join(f"- {wikilink(a, a)}" for a in all_authors) or "- None yet",
                "",
                "## Source notes",
                "\n".join(f"- {wikilink(n['frontmatter'].get('title', n['path'].stem), n['frontmatter'].get('title', n['path'].stem))}" for n in notes),
            ]
        )
        write_note(
            SETTINGS.courses_dir / f"{slugify(course)}.md",
            {
                "id": slugify(course),
                "title": course,
                "note_type": "course",
                "updated_at": utc_now_iso(),
            },
            body,
        )

    build_graph_index()

    # Rebuild embedding index if OpenAI key is available
    try:
        from kb_core.embeddings import EmbeddingIndex
        idx = EmbeddingIndex()
        idx.build()
    except Exception:
        pass  # Embeddings are optional; lexical search still works


def _parse_compiled_payload(raw_content: str, raw_path: Path, extracted_text: str) -> CompiledSourcePayload:
    try:
        cleaned = raw_content.strip()
        if cleaned.startswith("```"):
            first_newline = cleaned.index("\n")
            cleaned = cleaned[first_newline + 1:]
        if cleaned.endswith("```"):
            cleaned = cleaned[:-3].rstrip()
        return CompiledSourcePayload.model_validate(json.loads(cleaned))
    except (json.JSONDecodeError, ValidationError, TypeError, ValueError):
        return _fallback_payload(raw_path, extracted_text)


def _fallback_payload(raw_path: Path, text: str) -> CompiledSourcePayload:
    excerpt = text.strip()[:FALLBACK_SUMMARY_LIMIT]
    lines = [line.strip() for line in excerpt.splitlines() if line.strip()]
    return CompiledSourcePayload(
        title=raw_path.stem.replace("_", " ").replace("-", " ").title(),
        summary=lines[0] if lines else f"Fallback summary for {raw_path.stem}.",
        core_ideas=lines[1:4],
        source_anchors=lines[:3],
    )


def _write_source_note(raw_path: Path, semester: str, course: str, manual_concepts: list[str], manual_authors: list[str], payload: CompiledSourcePayload, llm_provider: str, llm_model: str) -> Path:
    concepts = _unique_strings(manual_concepts + payload.concepts)
    authors = _unique_strings(manual_authors + payload.authors)
    title = payload.title or raw_path.stem.replace("_", " ").replace("-", " ").title()
    note_slug = slugify(title)
    note_path = SETTINGS.sources_dir / slugify(semester) / slugify(course) / f"{note_slug}.md"

    frontmatter = {
        "id": note_slug,
        "title": title,
        "note_type": "source",
        "semester": semester,
        "course": course,
        "source_path": str(raw_path.relative_to(SETTINGS.kb_root)),
        "compiled_at": utc_now_iso(),
        "reviewed": False,
        "concepts": concepts,
        "authors": authors,
        "methods": payload.methods,
        "tags": _unique_strings([course] + concepts + authors),
        "llm_provider": llm_provider,
        "llm_model": llm_model,
    }

    body = _format_source_note(title, payload.summary, payload.core_ideas, concepts, authors, payload.methods, payload.exam_questions, payload.open_questions, payload.source_anchors)
    write_note(note_path, frontmatter, body)
    return note_path


def _format_source_note(title: str, summary: str, core_ideas: list[str], concepts: list[str], authors: list[str], methods: list[str], exam_questions: list[str], open_questions: list[str], source_anchors: list[str]) -> str:
    def bullets(items: list[str]) -> str:
        return "\n".join(f"- {item}" for item in items) if items else "- None yet"

    def wikilink_bullets(items: list[str]) -> str:
        return "\n".join(f"- {wikilink(item, item)}" for item in items) if items else "- None yet"

    return f"""# {title}

## Summary
{summary or 'No summary generated yet.'}

## Core ideas
{bullets(core_ideas)}

## Concepts
{wikilink_bullets(concepts)}

## Authors
{wikilink_bullets(authors)}

## Methods
{bullets(methods)}

## Possible exam questions
{bullets(exam_questions)}

## Open questions
{bullets(open_questions)}

## Source anchors
{bullets(source_anchors)}
"""


def _build_entity_body(entity: str, notes: list[dict], mode: str) -> str:
    header = "Definition" if mode == "concept" else "Core ideas"
    references = "\n".join(
        f"- {wikilink(item['frontmatter'].get('title', item['path'].stem), item['frontmatter'].get('title', item['path'].stem))} ({item['frontmatter'].get('course', 'general')})"
        for item in notes
    )
    return f"""## {header}
This page aggregates references to **{entity}** across the sociology wiki.

## Source notes
{references}
"""


def _store_open_questions(source_slug: str, questions: list[str], semester: str, course: str) -> None:
    if not questions:
        return
    path = SETTINGS.open_questions_dir / f"{slugify(semester)}-{slugify(course)}-{source_slug}.md"
    lines = [f"# Open questions from {source_slug}", ""]
    lines.extend(f"- {question}" for question in questions)
    write_text(path, "\n".join(lines) + "\n")


def _load_source_notes() -> list[dict]:
    notes = []
    for path in list_files_recursive(SETTINGS.sources_dir, suffixes=(".md",)):
        frontmatter, body = load_markdown_file(path)
        notes.append({"path": path, "frontmatter": frontmatter, "body": body})
    return notes


def _unique_strings(items: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        clean = str(item).strip()
        if not clean:
            continue
        key = clean.lower()
        if key in seen:
            continue
        seen.add(key)
        result.append(clean)
    return result
