from __future__ import annotations

from pathlib import Path

from kb_core.lint import run_lint_checks, suggest_new_articles
from kb_core.storage import ensure_project_dirs, write_note


def test_broken_wikilink_detected(kb_tmp: Path):
    """Lint detects broken wikilinks."""
    ensure_project_dirs()
    from kb_core.config import SETTINGS

    note_dir = SETTINGS.sources_dir / "2026-s1" / "teoria"
    note_dir.mkdir(parents=True, exist_ok=True)
    write_note(
        note_dir / "test.md",
        {"id": "test", "title": "Test", "note_type": "source", "concepts": ["anomie"]},
        "# Test\n\nSee [[nonexistent-concept]] for details.\n\n## Source anchors\n- p.1",
    )

    issues = run_lint_checks()
    broken = [i for i in issues if i["type"] == "broken_wikilink"]
    assert len(broken) >= 1
    assert "nonexistent-concept" in broken[0]["message"]


def test_suggest_new_articles(kb_tmp: Path):
    """suggest_new_articles finds cross-course concepts."""
    ensure_project_dirs()
    from kb_core.config import SETTINGS

    for course in ["teoria", "metodos"]:
        note_dir = SETTINGS.sources_dir / "2026-s1" / course
        note_dir.mkdir(parents=True, exist_ok=True)
        write_note(
            note_dir / f"{course}-note.md",
            {"id": f"{course}-note", "title": f"{course} Note", "note_type": "source", "course": course, "concepts": ["stratification"]},
            f"# {course} Note\n\n## Summary\nContent.",
        )

    suggestions = suggest_new_articles()
    assert len(suggestions) >= 1
    assert suggestions[0]["concept"] == "stratification"
    assert len(suggestions[0]["courses"]) == 2
