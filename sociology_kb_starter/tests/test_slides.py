from __future__ import annotations

from pathlib import Path

from kb_core.slides import generate_slides
from kb_core.storage import ensure_project_dirs, write_note


def test_generate_slides_fallback(kb_tmp: Path):
    """Slide generation works with fallback when no LLM is available."""
    ensure_project_dirs()
    from kb_core.config import SETTINGS

    note_dir = SETTINGS.sources_dir / "2026-s1" / "teoria"
    note_dir.mkdir(parents=True, exist_ok=True)
    write_note(
        note_dir / "solidarity.md",
        {"id": "solidarity", "title": "Solidarity", "note_type": "source", "concepts": ["solidarity"]},
        "# Solidarity\n\n## Summary\nMechanical and organic solidarity forms.",
    )

    output = generate_slides("solidarity")
    assert output.exists()
    content = output.read_text(encoding="utf-8")
    assert "marp: true" in content or "Solidarity" in content
