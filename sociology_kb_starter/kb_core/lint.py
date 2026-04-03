from __future__ import annotations

from collections import defaultdict
from pathlib import Path

from kb_core.config import SETTINGS
from kb_core.models import DocumentStatus
from kb_core.storage import list_raw_documents
from kb_core.utils import list_files_recursive, load_markdown_file


REQUIRED_FRONTMATTER_KEYS = {"id", "title", "note_type"}


def run_lint_checks() -> list[dict]:
    issues: list[dict] = []
    titles: dict[str, list[Path]] = defaultdict(list)
    concept_references: set[str] = set()

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

    all_notes = list_files_recursive(SETTINGS.wiki_dir, suffixes=(".md",))
    for path in all_notes:
        frontmatter, body = load_markdown_file(path)
        title = str(frontmatter.get("title", "")).strip().lower()
        if title:
            titles[title].append(path)

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
                concept_references.add(concept.strip().lower())

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
        frontmatter, _ = load_markdown_file(concept_note)
        title = str(frontmatter.get("title", "")).strip().lower()
        if title and title not in concept_references:
            issues.append(
                {
                    "severity": "warning",
                    "type": "orphan_concept",
                    "path": str(concept_note.relative_to(SETTINGS.kb_root)),
                    "message": "Concept note exists but no source note currently references it.",
                }
            )

    return sorted(issues, key=lambda item: (item["severity"], item["type"], item["path"]))
