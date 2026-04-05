from __future__ import annotations

from kb_core.wiki_renderer import (
    extract_toc,
    list_articles_by_type,
    render_breadcrumbs,
    render_infobox,
    render_toc_html,
    resolve_wikilinks_html,
)
from kb_core.storage import ensure_project_dirs, write_note
from pathlib import Path


def test_resolve_wikilinks_html():
    """Wikilinks are converted to HTML anchor tags."""
    body = "This links to [[anomia]] and [[max-weber|Max Weber]] concepts."
    result = resolve_wikilinks_html(body)
    assert "anomia" in result
    assert "Max Weber" in result
    assert "[[" not in result
    assert 'href="?article=' in result


def test_extract_toc():
    """TOC extraction picks up H2 and H3 headings."""
    body = "# Title\n\n## Introduction\n\nSome text\n\n### Details\n\nMore text\n\n## Conclusion\n"
    toc = extract_toc(body)
    assert len(toc) == 3
    assert toc[0]["level"] == 2
    assert toc[0]["title"] == "Introduction"
    assert toc[1]["level"] == 3
    assert toc[1]["title"] == "Details"
    assert toc[2]["level"] == 2
    assert toc[2]["title"] == "Conclusion"


def test_render_toc_html():
    """TOC renders as HTML with anchors."""
    toc = [
        {"level": 2, "title": "Intro", "anchor": "intro"},
        {"level": 3, "title": "Sub", "anchor": "sub"},
    ]
    html = render_toc_html(toc)
    assert "Contenido" in html
    assert 'href="#intro"' in html
    assert 'href="#sub"' in html


def test_render_toc_html_empty():
    """Empty TOC returns empty string."""
    assert render_toc_html([]) == ""


def test_render_breadcrumbs():
    """Breadcrumbs show Wiki > Category > Title."""
    html = render_breadcrumbs("concept", "Anomia")
    assert "Wiki" in html
    assert "Conceptos" in html
    assert "Anomia" in html


def test_render_infobox():
    """Infobox renders table with frontmatter data."""
    front = {
        "title": "Anomia",
        "note_type": "concept",
        "semester": "2026-S1",
        "course": "teoria",
    }
    html = render_infobox(front)
    assert "Anomia" in html
    assert "Conceptos" in html
    assert "2026-S1" in html


def test_list_articles_by_type(kb_tmp: Path):
    """list_articles_by_type returns sorted articles."""
    ensure_project_dirs()
    from kb_core.config import SETTINGS

    for name in ["zeta-concept", "alpha-concept"]:
        write_note(
            SETTINGS.concepts_dir / f"{name}.md",
            {"id": name, "title": name.replace("-", " ").title(), "note_type": "concept"},
            f"# {name}\n\nDefinition text.",
        )

    articles = list_articles_by_type("concept")
    assert len(articles) >= 2
    titles = [a["title"] for a in articles]
    assert titles == sorted(titles, key=str.lower)
