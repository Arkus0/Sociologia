from __future__ import annotations

from collections import defaultdict
from pathlib import Path

from kb_core.config import SETTINGS
from kb_core.storage import ensure_project_dirs
from kb_core.utils import list_files_recursive, load_markdown_file, slugify, utc_now_iso, wikilink, write_text


def init_semester(semester_id: str, courses: list[str]) -> dict[str, list[Path]]:
    """Create directory scaffolding for a new semester."""
    ensure_project_dirs()
    created: dict[str, list[Path]] = {"raw": [], "wiki": []}

    for course in courses:
        course_slug = slugify(course)
        semester_slug = slugify(semester_id)

        raw_dir = SETTINGS.raw_dir / semester_slug / course_slug
        raw_dir.mkdir(parents=True, exist_ok=True)
        created["raw"].append(raw_dir)

        wiki_dir = SETTINGS.sources_dir / semester_slug / course_slug
        wiki_dir.mkdir(parents=True, exist_ok=True)
        created["wiki"].append(wiki_dir)

    return created


def semester_stats(semester_id: str) -> dict:
    """Compute statistics for a specific semester."""
    semester_slug = slugify(semester_id)
    raw_dir = SETTINGS.raw_dir / semester_slug
    sources_dir = SETTINGS.sources_dir / semester_slug

    raw_files = list_files_recursive(raw_dir) if raw_dir.exists() else []
    raw_files = [f for f in raw_files if not f.name.endswith(".meta.json")]

    source_notes = list_files_recursive(sources_dir, suffixes=(".md",)) if sources_dir.exists() else []

    courses: set[str] = set()
    concepts: set[str] = set()
    authors: set[str] = set()
    for note_path in source_notes:
        front, _ = load_markdown_file(note_path)
        if front.get("course"):
            courses.add(str(front["course"]))
        for c in front.get("concepts", []):
            concepts.add(str(c))
        for a in front.get("authors", []):
            authors.add(str(a))

    return {
        "semester": semester_id,
        "raw_files": len(raw_files),
        "compiled_notes": len(source_notes),
        "courses": sorted(courses),
        "unique_concepts": len(concepts),
        "unique_authors": len(authors),
    }


def cross_semester_index() -> str:
    """Generate a master INDEX.md linking concepts across all semesters."""
    semester_dirs = sorted(
        [d for d in SETTINGS.sources_dir.iterdir() if d.is_dir()]
    ) if SETTINGS.sources_dir.exists() else []

    semester_data: dict[str, dict] = {}
    all_concepts: defaultdict[str, set[str]] = defaultdict(set)
    all_authors: defaultdict[str, set[str]] = defaultdict(set)

    for sem_dir in semester_dirs:
        semester_id = sem_dir.name
        courses: set[str] = set()
        notes_count = 0

        for note_path in list_files_recursive(sem_dir, suffixes=(".md",)):
            front, _ = load_markdown_file(note_path)
            notes_count += 1
            course = str(front.get("course", "general"))
            courses.add(course)
            for c in front.get("concepts", []):
                all_concepts[str(c)].add(semester_id)
            for a in front.get("authors", []):
                all_authors[str(a)].add(semester_id)

        semester_data[semester_id] = {
            "courses": sorted(courses),
            "notes_count": notes_count,
        }

    cross_semester_concepts = {
        c: sorted(semesters) for c, semesters in all_concepts.items() if len(semesters) > 1
    }

    lines = [
        "# Sociology Knowledge Base — Master Index",
        "",
        f"*Auto-generated: {utc_now_iso()}*",
        "",
        "## Semesters",
        "",
    ]
    for sem_id, data in sorted(semester_data.items()):
        lines.append(f"### {sem_id}")
        lines.append(f"- **Notes**: {data['notes_count']}")
        lines.append(f"- **Courses**: {', '.join(wikilink(c, c) for c in data['courses'])}")
        lines.append("")

    lines.extend([
        "## Cross-Semester Concepts",
        "",
        "Concepts that appear across multiple semesters:",
        "",
    ])
    if cross_semester_concepts:
        for concept, semesters in sorted(cross_semester_concepts.items()):
            lines.append(f"- {wikilink(concept, concept)} — semesters: {', '.join(semesters)}")
    else:
        lines.append("- None yet (need more semesters)")
    lines.append("")

    top_authors = sorted(all_authors.items(), key=lambda x: len(x[1]), reverse=True)[:20]
    lines.extend([
        "## Top Authors",
        "",
    ])
    for author, semesters in top_authors:
        lines.append(f"- {wikilink(author, author)} ({len(semesters)} semesters)")
    lines.append("")

    content = "\n".join(lines)
    index_path = SETTINGS.wiki_dir / "INDEX.md"
    index_path.parent.mkdir(parents=True, exist_ok=True)
    write_text(index_path, content)
    return content
