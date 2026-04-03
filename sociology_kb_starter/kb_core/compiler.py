from __future__ import annotations

from collections import defaultdict
from pathlib import Path
import json

from kb_core.config import SETTINGS
from kb_core.llm import LLMClient
from kb_core.storage import extract_text_from_raw, list_raw_documents, write_note
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


def compile_all_raw_documents() -> list[Path]:
    compiled: list[Path] = []
    for item in list_raw_documents():
        note_path = compile_raw_document(item["path"], item.get("metadata", {}))
        compiled.append(note_path)
    rebuild_indexes()
    return compiled


def compile_raw_document(raw_path: Path, metadata: dict) -> Path:
    llm = LLMClient()
    text = extract_text_from_raw(raw_path)
    relative_raw = raw_path.relative_to(SETTINGS.kb_root)
    semester = metadata.get("semester", "unknown")
    course = metadata.get("course", "unknown")
    manual_concepts = metadata.get("manual_concepts", [])
    manual_authors = metadata.get("manual_authors", [])

    payload = {
        "source_path": str(relative_raw),
        "semester": semester,
        "course": course,
        "filename": raw_path.name,
        "text_excerpt": text[:12000],
    }

    llm_result = llm.complete(SOURCE_PROMPT, json.dumps(payload, ensure_ascii=False, indent=2), max_tokens=2000) if llm.available() else None

    if llm_result:
        try:
            data = json.loads(llm_result.content)
        except json.JSONDecodeError:
            data = _fallback_data(raw_path, text)
    else:
        data = _fallback_data(raw_path, text)

    concepts = _unique_strings(manual_concepts + data.get("concepts", []))
    authors = _unique_strings(manual_authors + data.get("authors", []))
    methods = _unique_strings(data.get("methods", []))
    exam_questions = _unique_strings(data.get("exam_questions", []))
    open_questions = _unique_strings(data.get("open_questions", []))
    source_anchors = _unique_strings(data.get("source_anchors", []))
    title = data.get("title") or raw_path.stem.replace("_", " ").replace("-", " ").title()
    course_slug = slugify(course)
    note_slug = slugify(title)

    note_path = SETTINGS.by_course_dir / course_slug / f"{note_slug}.md"
    frontmatter = {
        "id": note_slug,
        "title": title,
        "note_type": "source",
        "semester": semester,
        "course": course,
        "source_path": str(relative_raw),
        "compiled_at": utc_now_iso(),
        "reviewed": False,
        "concepts": concepts,
        "authors": authors,
        "methods": methods,
        "tags": _unique_strings([course] + concepts + authors),
        "llm_provider": llm_result.provider if llm_result else "fallback",
        "llm_model": llm_result.model if llm_result else "fallback",
    }

    body = _format_source_note(
        title=title,
        summary=data.get("summary", ""),
        core_ideas=data.get("core_ideas", []),
        concepts=concepts,
        authors=authors,
        methods=methods,
        exam_questions=exam_questions,
        open_questions=open_questions,
        source_anchors=source_anchors,
    )
    write_note(note_path, frontmatter, body)
    _store_open_questions(note_slug, open_questions, semester, course)
    return note_path


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


def _fallback_data(raw_path: Path, text: str) -> dict:
    excerpt = text.strip()[:FALLBACK_SUMMARY_LIMIT]
    lines = [line.strip() for line in excerpt.splitlines() if line.strip()]
    summary = lines[0] if lines else f"Fallback summary for {raw_path.stem}."
    anchors = lines[:3]
    return {
        "title": raw_path.stem.replace("_", " ").replace("-", " ").title(),
        "summary": summary,
        "core_ideas": lines[1:4],
        "concepts": [],
        "authors": [],
        "methods": [],
        "exam_questions": [],
        "open_questions": [],
        "source_anchors": anchors,
    }


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
    lines = [f"# Open questions from {source_id}", ""]
    for question in questions:
        lines.append(f"- [ ] {question}")
    body = "\n".join(lines) + "\n"
    path = SETTINGS.open_questions_dir / f"{source_id}.md"
    write_text(path, body)
