from __future__ import annotations

from pathlib import Path

from kb_core.qa import file_answer_to_wiki
from kb_core.storage import ensure_project_dirs, write_note
from kb_core.utils import load_markdown_file


def test_file_answer_creates_research_note(kb_tmp: Path):
    """file_answer_to_wiki creates a research note in the wiki."""
    ensure_project_dirs()
    note_path = file_answer_to_wiki(
        query="What is anomie?",
        answer="Anomie is a breakdown of social norms.",
        concepts=["anomie"],
        authors=["Durkheim"],
    )
    assert note_path.exists()
    front, body = load_markdown_file(note_path)
    assert front["note_type"] == "research"
    assert "anomie" in front["concepts"]
    assert "[[durkheim|Durkheim]]" in body or "[[durkheim]]" in body


def test_file_answer_with_retrieved_sources(kb_tmp: Path):
    """Filed answer references cited sources via wikilinks."""
    ensure_project_dirs()
    from kb_core.config import SETTINGS

    note_path = file_answer_to_wiki(
        query="Explain solidarity",
        answer="Solidarity binds society together.",
        concepts=["solidarity"],
        retrieved=[
            {"frontmatter": {"title": "Durkheim on Solidarity"}, "path": SETTINGS.sources_dir / "test.md", "score": 5.0},
        ],
    )
    _, body = load_markdown_file(note_path)
    assert "durkheim-on-solidarity" in body or "Durkheim on Solidarity" in body
