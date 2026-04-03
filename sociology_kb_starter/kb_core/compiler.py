from __future__ import annotations

from collections import defaultdict
from pathlib import Path
import json

from pydantic import ValidationError

from kb_core.config import SETTINGS
from kb_core.extraction import extract_text
from kb_core.llm import LLMClient
from kb_core.models import CompilationResult, CompiledSourcePayload, DocumentStatus, ExtractionStatus
from kb_core.storage import (
    list_raw_documents,
    read_metadata,
    update_metadata_status,
    write_note,
)
from kb_core.utils import list_files_recursive, load_markdown_file, slugify, utc_now_iso, write_text


SOURCE_PROMPT = """You are compiling a sociology knowledge base.
Return strict JSON with these keys:
- title: string
- summary: string
- core_ideas: list[string]
- concepts: list[string]
- authors: list[string]
- methods: list[string]
- exam_questions: list[string]
- open_questions: list[string]
- source_anchors: list[string]
Rules:
- Be conservative.
- Do not invent citations or page numbers.
- If uncertain, leave a list short rather than hallucinating.
- Prefer sociological terminology when supported by the source.
"""

CONCEPT_PROMPT = """You are synthesizing a concept page for a sociology wiki.
Write concise markdown with these sections:
## Definition
## Why it matters
## Cross-course links
## Source notes
Use only the supplied evidence.
"""

AUTHOR_PROMPT = """You are synthesizing an author page for a sociology wiki.
Write concise markdown with these sections:
## Core ideas
## Related concepts
## Cross-course relevance
## Source notes
Use only the supplied evidence.
"""

FALLBACK_SUMMARY_LIMIT = 1200


def compile_all_raw_documents() -> list[CompilationResult]:
    results: list[CompilationResult] = []
    for item in list_raw_documents():
        results.append(compile_raw_document(item["path"]))
    rebuild_indexes()
    return results


def compile_raw_document(raw_path: Path) -> CompilationResult:
    metadata = read_metadata(raw_path)
    update_metadata_status(raw_path, status=DocumentStatus.COMPILING)

    extraction = extract_text(raw_path)
    if extraction.status in {ExtractionStatus.UNSUPPORTED, ExtractionStatus.ENCRYPTED, ExtractionStatus.PARSE_ERROR, ExtractionStatus.EMPTY}:
        status = DocumentStatus.PARSE_FAILED
        update_metadata_status(
            raw_path,
            status=status,
            error_category=extraction.error_category,
            error_message=extraction.message,
        )
        return CompilationResult(
            ok=False,
            raw_path=str(raw_path),
            status=status,
            message=extraction.message,
            error_category=extraction.error_category,
            extraction=extraction,
        )

    llm = LLMClient()
    payload = {
        "source_path": str(raw_path.relative_to(SETTINGS.kb_root)),
        "semester": metadata.semester,
        "course": metadata.course,
        "filename": raw_path.name,
        "text_excerpt": extraction.text[:12000],
    }

    llm_result = llm.complete(SOURCE_PROMPT, json.dumps(payload, ensure_ascii=False, indent=2), max_tokens=2000) if llm.available() else None

    compiled_payload: CompiledSourcePayload
    if llm_result and llm_result.content:
        compiled_payload = _parse_compiled_payload(llm_result.content, raw_path, extraction.text)
    else:
        compiled_payload = _fallback_payload(raw_path, extraction.text)

    try:
        note_path = _write_source_note(raw_path, metadata.semester, metadata.course, metadata.manual_concepts, metadata.manual_authors, compiled_payload, llm_result.provider if llm_result else "fallback", llm_result.model if llm_result else "fallback")
        _store_open_questions(slugify(compiled_payload.title), compiled_payload.open_questions, metadata.semester, metadata.course)
        update_metadata_status(
            raw_path,
            status=DocumentStatus.COMPILED,
            compiled_note_path=str(note_path.relative_to(SETTINGS.kb_root)),
        )
        return CompilationResult(
            ok=True,
            raw_path=str(raw_path),
            note_path=str(note_path),
            status=DocumentStatus.COMPILED,
            message="Compilation finished successfully.",
            extraction=extraction,
            llm_provider=llm_result.provider if llm_result else "fallback",
            llm_model=llm_result.model if llm_result else "fallback",
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


def rebuild_indexes() -> None:
    source_notes = _load_source_notes()
    concept_map: dict[str, list[dict]] = defaultdict(list)
    author_map: dict[str, list[dict]] = defaultdict(list)

    for note in source_notes:
        front = note["frontmatter"]
        for concept in front.get("concepts", []):
            concept_map[concept].append(note)
        for author in front.get("authors", []):
            author_map[author].append(note)

    llm = LLMClient()

    for concept, notes in concept_map.items():
        slug = slugify(concept)
        path = SETTINGS.by_concept_dir / f"{slug}.md"
        body = _build_concept_or_author_body(concept, notes, mode="concept", llm=llm)
        frontmatter = {
            "id": slug,
            "title": concept,
            "note_type": "concept",
            "updated_at": utc_now_iso(),
            "source_notes": [str(item["path"].relative_to(SETTINGS.kb_root)) for item in notes],
        }
        write_note(path, frontmatter, body)

    for author, notes in author_map.items():
        slug = slugify(author)
        path = SETTINGS.by_author_dir / f"{slug}.md"
        body = _build_concept_or_author_body(author, notes, mode="author", llm=llm)
        frontmatter = {
            "id": slug,
            "title": author,
            "note_type": "author",
            "updated_at": utc_now_iso(),
            "source_notes": [str(item["path"].relative_to(SETTINGS.kb_root)) for item in notes],
        }
        write_note(path, frontmatter, body)


def _parse_compiled_payload(raw_content: str, raw_path: Path, extracted_text: str) -> CompiledSourcePayload:
    try:
        parsed = json.loads(raw_content)
        return CompiledSourcePayload.model_validate(parsed)
    except (json.JSONDecodeError, ValidationError, TypeError):
        return _fallback_payload(raw_path, extracted_text)


def _fallback_payload(raw_path: Path, text: str) -> CompiledSourcePayload:
    excerpt = text.strip()[:FALLBACK_SUMMARY_LIMIT]
    lines = [line.strip() for line in excerpt.splitlines() if line.strip()]
    summary = lines[0] if lines else f"Fallback summary for {raw_path.stem}."
    return CompiledSourcePayload(
        title=raw_path.stem.replace("_", " ").replace("-", " ").title(),
        summary=summary,
        core_ideas=lines[1:4],
        source_anchors=lines[:3],
    )


def _write_source_note(
    raw_path: Path,
    semester: str,
    course: str,
    manual_concepts: list[str],
    manual_authors: list[str],
    payload: CompiledSourcePayload,
    llm_provider: str,
    llm_model: str,
) -> Path:
    concepts = _unique_strings(manual_concepts + payload.concepts)
    authors = _unique_strings(manual_authors + payload.authors)

    title = payload.title or raw_path.stem.replace("_", " ").replace("-", " ").title()
    note_slug = slugify(title)
    course_slug = slugify(course)
    note_path = SETTINGS.by_course_dir / course_slug / f"{note_slug}.md"

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

    body = _format_source_note(
        title=title,
        summary=payload.summary,
        core_ideas=payload.core_ideas,
        concepts=concepts,
        authors=authors,
        methods=payload.methods,
        exam_questions=payload.exam_questions,
        open_questions=payload.open_questions,
        source_anchors=payload.source_anchors,
    )
    write_note(note_path, frontmatter, body)
    return note_path


def _format_source_note(
    *,
    title: str,
    summary: str,
    core_ideas: list[str],
    concepts: list[str],
    authors: list[str],
    methods: list[str],
    exam_questions: list[str],
    open_questions: list[str],
    source_anchors: list[str],
) -> str:
    def bullet_block(items: list[str]) -> str:
        return "\n".join(f"- {item}" for item in items) if items else "- None yet"

    return f"""# {title}

## Summary
{summary or 'No summary generated yet.'}

## Core ideas
{bullet_block(core_ideas)}

## Concepts
{bullet_block(concepts)}

## Authors
{bullet_block(authors)}

## Methods
{bullet_block(methods)}

## Possible exam questions
{bullet_block(exam_questions)}

## Open questions
{bullet_block(open_questions)}

## Source anchors
{bullet_block(source_anchors)}
"""


def _build_concept_or_author_body(entity: str, notes: list[dict], mode: str, llm: LLMClient) -> str:
    references = "\n".join(
        f"- {item['frontmatter'].get('title', item['path'].stem)} ({item['frontmatter'].get('course', 'unknown course')}) -> {item['path'].relative_to(SETTINGS.kb_root)}"
        for item in notes
    )
    payload = {
        "entity": entity,
        "mode": mode,
        "evidence": [
            {
                "title": item["frontmatter"].get("title"),
                "course": item["frontmatter"].get("course"),
                "summary": _extract_section(item["body"], "## Summary", "## Core ideas"),
                "core_ideas": _extract_section(item["body"], "## Core ideas", "## Concepts"),
                "path": str(item["path"].relative_to(SETTINGS.kb_root)),
            }
            for item in notes
        ],
    }

    prompt = CONCEPT_PROMPT if mode == "concept" else AUTHOR_PROMPT
    llm_result = llm.complete(prompt, json.dumps(payload, ensure_ascii=False, indent=2), max_tokens=1400) if llm.available() else None
    if llm_result and llm_result.content:
        body = llm_result.content.strip()
    else:
        heading = "Definition" if mode == "concept" else "Core ideas"
        body = f"## {heading}\nThis page aggregates references to **{entity}** across the current wiki.\n\n## Source notes\n{references}\n"
    if "## Source notes" not in body:
        body = f"{body.rstrip()}\n\n## Source notes\n{references}\n"
    return body


def _extract_section(body: str, start_marker: str, end_marker: str) -> str:
    if start_marker not in body:
        return ""
    section = body.split(start_marker, 1)[1]
    if end_marker in section:
        section = section.split(end_marker, 1)[0]
    return section.strip()


def _load_source_notes() -> list[dict]:
    notes: list[dict] = []
    for path in list_files_recursive(SETTINGS.by_course_dir, suffixes=(".md",)):
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


def _store_open_questions(source_id: str, questions: list[str], semester: str, course: str) -> None:
    if not questions:
        return
    lines = [f"# Open questions from {source_id}", "", f"- semester: {semester}", f"- course: {course}", ""]
    for question in questions:
        lines.append(f"- [ ] {question}")
    body = "\n".join(lines) + "\n"
    path = SETTINGS.open_questions_dir / f"{source_id}.md"
    write_text(path, body)
