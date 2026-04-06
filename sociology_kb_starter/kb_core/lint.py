from __future__ import annotations

from collections import defaultdict
from pathlib import Path
import re

from kb_core.config import SETTINGS
from kb_core.models import DocumentStatus
from kb_core.storage import list_raw_documents
from kb_core.utils import (
    extract_alias_target,
    extract_wikilinks,
    list_files_recursive,
    load_markdown_file,
    normalize_text,
    slugify,
)


REQUIRED_FRONTMATTER_KEYS = {"id", "title", "note_type"}
SUMMARY_HEADING_PREFIXES = ("definicion", "resumen", "summary")
AUTHOR_SUMMARY_HEADING_PREFIXES = (
    "datos biograficos",
    "biografia",
    "biografia intelectual",
    "biografia y trayectoria",
    "trayectoria",
)


def _canonical_note_paths() -> list[Path]:
    return (
        list_files_recursive(SETTINGS.concepts_dir, suffixes=(".md",))
        + list_files_recursive(SETTINGS.authors_dir, suffixes=(".md",))
        + list_files_recursive(SETTINGS.courses_dir, suffixes=(".md",))
        + list_files_recursive(SETTINGS.sources_dir, suffixes=(".md",))
    )


def _extract_h2_headings(body: str) -> list[str]:
    return [normalize_text(match.group(1)) for match in re.finditer(r"^##\s+(.+?)\s*$", body, re.MULTILINE)]


def _first_meaningful_paragraph(body: str) -> str:
    for block in re.split(r"\n\s*\n", body):
        stripped = block.strip()
        if not stripped or stripped.startswith("#"):
            continue
        return stripped
    return ""


def _has_summary_content(body: str, note_type: str) -> bool:
    headings = _extract_h2_headings(body)
    prefixes = SUMMARY_HEADING_PREFIXES
    if note_type == "author":
        prefixes = SUMMARY_HEADING_PREFIXES + AUTHOR_SUMMARY_HEADING_PREFIXES

    if any(any(heading.startswith(prefix) for prefix in prefixes) for heading in headings):
        return True

    return bool(_first_meaningful_paragraph(body))


def run_lint_checks() -> list[dict]:
    issues: list[dict] = []
    titles: dict[str, list[Path]] = defaultdict(list)
    concept_references: set[str] = set()
    all_note_slugs: set[str] = set()
    all_wikilinks: list[tuple[Path, str]] = []

    for raw_doc in list_raw_documents():
        path = raw_doc["path"]
        metadata = raw_doc["metadata"]
        if metadata.get("status") in {DocumentStatus.PARSE_FAILED.value, DocumentStatus.COMPILE_FAILED.value}:
            issues.append(
                {
                    "severity": "warning",
                    "type": "raw_document_failed",
                    "path": str(path.relative_to(SETTINGS.kb_root)),
                    "message": metadata.get("last_error_message") or "Raw document failed in previous compile attempt.",
                }
            )

    for path in _canonical_note_paths():
        frontmatter, body = load_markdown_file(path)
        title = normalize_text(str(frontmatter.get("title", "")))
        note_id = frontmatter.get("id", path.stem)
        is_alias = extract_alias_target(body) is not None

        all_note_slugs.add(slugify(str(note_id)))
        if title:
            if not is_alias:
                titles[title].append(path)
            all_note_slugs.add(slugify(title))

        missing_keys = REQUIRED_FRONTMATTER_KEYS - set(frontmatter.keys())
        if missing_keys:
            issues.append(
                {
                    "severity": "error",
                    "type": "missing_frontmatter",
                    "path": str(path.relative_to(SETTINGS.kb_root)),
                    "message": f"Missing frontmatter keys: {', '.join(sorted(missing_keys))}",
                }
            )

        if frontmatter.get("note_type") == "source":
            if "## Source anchors" not in body:
                issues.append(
                    {
                        "severity": "warning",
                        "type": "missing_source_anchors_section",
                        "path": str(path.relative_to(SETTINGS.kb_root)),
                        "message": "Source note has no explicit source anchors section.",
                    }
                )
            if not frontmatter.get("concepts"):
                issues.append(
                    {
                        "severity": "warning",
                        "type": "missing_concepts",
                        "path": str(path.relative_to(SETTINGS.kb_root)),
                        "message": "Source note has no concepts yet.",
                    }
                )
            for concept in frontmatter.get("concepts", []):
                concept_references.add(normalize_text(concept))

            body_text_lower = body.lower()
            for concept in frontmatter.get("concepts", []):
                if concept.lower() in body_text_lower and f"[[{slugify(concept)}" not in body:
                    issues.append(
                        {
                            "severity": "info",
                            "type": "concept_mentioned_but_not_linked",
                            "path": str(path.relative_to(SETTINGS.kb_root)),
                            "message": f"Concept '{concept}' appears in body text but is not wikilinked.",
                        }
                    )

        wikilinks = [extract_alias_target(body)] if is_alias else extract_wikilinks(body)
        for link in wikilinks:
            if link:
                all_wikilinks.append((path, link))

    for path, link_target in all_wikilinks:
        link_slug = slugify(link_target)
        if link_slug not in all_note_slugs:
            issues.append(
                {
                    "severity": "warning",
                    "type": "broken_wikilink",
                    "path": str(path.relative_to(SETTINGS.kb_root)),
                    "message": f"Broken wikilink: [[{link_target}]] - no note with slug '{link_slug}' found.",
                }
            )

    for title, paths in titles.items():
        if len(paths) > 1:
            issues.append(
                {
                    "severity": "warning",
                    "type": "duplicate_title",
                    "path": ", ".join(str(p.relative_to(SETTINGS.kb_root)) for p in paths),
                    "message": f"Duplicate title detected: {title}",
                }
            )

    for concept_note in list_files_recursive(SETTINGS.concepts_dir, suffixes=(".md",)):
        frontmatter, body = load_markdown_file(concept_note)
        if extract_alias_target(body):
            continue

        title = normalize_text(str(frontmatter.get("title", "")))
        if title and title not in concept_references:
            issues.append(
                {
                    "severity": "warning",
                    "type": "orphan_concept",
                    "path": str(concept_note.relative_to(SETTINGS.kb_root)),
                    "message": "Concept note exists but no source note currently references it.",
                }
            )
        if not _has_summary_content(body, "concept"):
            issues.append(
                {
                    "severity": "info",
                    "type": "missing_summary_section",
                    "path": str(concept_note.relative_to(SETTINGS.kb_root)),
                    "message": "Note lacks a summary/definition section - degrades RAG retrieval quality.",
                }
            )

    for author_note in list_files_recursive(SETTINGS.authors_dir, suffixes=(".md",)):
        _frontmatter, body = load_markdown_file(author_note)
        if extract_alias_target(body):
            continue

        if not _has_summary_content(body, "author"):
            issues.append(
                {
                    "severity": "info",
                    "type": "missing_summary_section",
                    "path": str(author_note.relative_to(SETTINGS.kb_root)),
                    "message": "Author note lacks a biographical/summary section - degrades RAG retrieval quality.",
                }
            )

    for course_note in list_files_recursive(SETTINGS.courses_dir, suffixes=(".md",)):
        frontmatter, _ = load_markdown_file(course_note)
        if not frontmatter.get("semester"):
            issues.append(
                {
                    "severity": "warning",
                    "type": "missing_semester",
                    "path": str(course_note.relative_to(SETTINGS.kb_root)),
                    "message": "Course note is missing 'semester' in frontmatter.",
                }
            )

    return sorted(issues, key=lambda item: (item["severity"], item["type"], item["path"]))


def suggest_new_articles(top_k: int = 5) -> list[dict]:
    """Identify cross-course concept connections that could become new wiki articles."""
    concept_courses: defaultdict[str, set[str]] = defaultdict(set)
    concept_notes: defaultdict[str, list[str]] = defaultdict(list)

    for path in list_files_recursive(SETTINGS.sources_dir, suffixes=(".md",)):
        front, _ = load_markdown_file(path)
        course = str(front.get("course", "general"))
        title = front.get("title", path.stem)
        for concept in front.get("concepts", []):
            concept_courses[concept].add(course)
            concept_notes[concept].append(title)

    suggestions: list[dict] = []
    for concept, courses in concept_courses.items():
        if len(courses) > 1:
            suggestions.append({
                "concept": concept,
                "courses": sorted(courses),
                "source_notes": concept_notes[concept],
                "reason": f"'{concept}' appears across {len(courses)} courses - potential for a comparative analysis article.",
            })

    suggestions.sort(key=lambda s: len(s["courses"]), reverse=True)
    return suggestions[:top_k]
