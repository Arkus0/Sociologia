from __future__ import annotations

from pathlib import Path

from kb_core.search_engine import SearchEngine
from kb_core.storage import ensure_project_dirs, write_note


def test_search_returns_results(kb_tmp: Path):
    """SearchEngine finds notes matching a query."""
    ensure_project_dirs()
    from kb_core.config import SETTINGS

    note_dir = SETTINGS.sources_dir / "2026-s1" / "teoria"
    note_dir.mkdir(parents=True, exist_ok=True)
    write_note(
        note_dir / "durkheim-solidarity.md",
        {
            "id": "durkheim-solidarity",
            "title": "Durkheim on Solidarity",
            "note_type": "source",
            "semester": "2026-S1",
            "course": "teoria",
            "concepts": ["solidarity", "anomie"],
            "authors": ["Durkheim"],
        },
        "# Durkheim on Solidarity\n\n## Summary\nA study of social solidarity and its forms.",
    )

    engine = SearchEngine()
    results = engine.search("durkheim solidarity")
    assert len(results) >= 1
    assert results[0]["title"] == "Durkheim on Solidarity"
    assert results[0]["score"] > 0


def test_search_filters_by_course(kb_tmp: Path):
    """SearchEngine filters by course."""
    ensure_project_dirs()
    from kb_core.config import SETTINGS

    for course_slug, title in [("teoria", "Teoria Note"), ("metodos", "Metodos Note")]:
        note_dir = SETTINGS.sources_dir / "2026-s1" / course_slug
        note_dir.mkdir(parents=True, exist_ok=True)
        write_note(
            note_dir / f"{course_slug}-note.md",
            {"id": f"{course_slug}-note", "title": title, "note_type": "source", "course": course_slug, "concepts": ["sociology"]},
            f"# {title}\n\n## Summary\nSociology content.",
        )

    engine = SearchEngine()
    results = engine.search("sociology", course="teoria")
    assert all(r["course"] == "teoria" for r in results)


def test_build_index(kb_tmp: Path):
    """build_index creates search_index.json."""
    ensure_project_dirs()
    from kb_core.config import SETTINGS

    engine = SearchEngine()
    path = engine.build_index()
    assert path.exists()
    assert path.name == "search_index.json"
