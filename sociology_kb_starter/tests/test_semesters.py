from __future__ import annotations

from pathlib import Path

from kb_core.semesters import cross_semester_index, init_semester, semester_stats
from kb_core.storage import ensure_project_dirs, save_uploaded_bytes, write_note
from kb_core.utils import slugify, utc_now_iso


def test_init_semester(kb_tmp: Path):
    """init_semester creates directory scaffolding."""
    ensure_project_dirs()
    created = init_semester("2026-S1", ["teoria-sociologica", "metodologia"])
    assert len(created["raw"]) == 2
    assert len(created["wiki"]) == 2
    for d in created["raw"] + created["wiki"]:
        assert d.is_dir()


def test_semester_stats(kb_tmp: Path):
    """semester_stats returns correct counts."""
    ensure_project_dirs()
    from kb_core.config import SETTINGS

    note_dir = SETTINGS.sources_dir / "2026-s1" / "teoria"
    note_dir.mkdir(parents=True, exist_ok=True)
    write_note(
        note_dir / "test-note.md",
        {"id": "test-note", "title": "Test Note", "note_type": "source", "semester": "2026-S1", "course": "teoria", "concepts": ["anomie"], "authors": ["Durkheim"]},
        "# Test Note\n\n## Summary\nTest",
    )

    stats = semester_stats("2026-S1")
    assert stats["compiled_notes"] == 1
    assert stats["unique_concepts"] == 1


def test_cross_semester_index(kb_tmp: Path):
    """cross_semester_index generates INDEX.md."""
    ensure_project_dirs()
    from kb_core.config import SETTINGS

    for sem, course in [("2026-s1", "teoria"), ("2026-s2", "metodos")]:
        note_dir = SETTINGS.sources_dir / sem / course
        note_dir.mkdir(parents=True, exist_ok=True)
        write_note(
            note_dir / "note.md",
            {"id": f"note-{sem}", "title": f"Note {sem}", "note_type": "source", "semester": sem, "course": course, "concepts": ["anomie"], "authors": []},
            "# Note\n\n## Summary\nTest",
        )

    content = cross_semester_index()
    assert "Master Index" in content
    assert "anomie" in content
    assert (SETTINGS.wiki_dir / "INDEX.md").exists()
