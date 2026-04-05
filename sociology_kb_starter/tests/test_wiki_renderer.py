from __future__ import annotations

from pathlib import Path

from kb_core.config import SETTINGS
from kb_core.storage import ensure_project_dirs, write_note
from kb_core.wiki_renderer import (
    extract_toc,
    list_articles_by_type,
    load_article,
    render_breadcrumbs,
    render_infobox,
    render_markdown_html,
    render_toc_html,
    resolve_wikilinks_html,
)


def test_resolve_wikilinks_html():
    body = "This links to [[anomia]] and [[max-weber|Max Weber]] concepts."
    result = resolve_wikilinks_html(body)
    assert "anomia" in result
    assert "Max Weber" in result
    assert "[[" not in result
    assert 'href="?article=' in result


def test_extract_toc():
    body = "# Title\n\n## Introduction\n\nSome text\n\n### Details\n\nMore text\n\n## Conclusion\n"
    toc = extract_toc(body)
    assert len(toc) == 3
    assert toc[0]["level"] == 2
    assert toc[0]["title"] == "Introduction"
    assert toc[1]["level"] == 3
    assert toc[1]["title"] == "Details"
    assert toc[2]["level"] == 2
    assert toc[2]["title"] == "Conclusion"


def test_render_markdown_html_supports_article_elements():
    body = (
        "# Title\n\n"
        "## Intro\n\n"
        "Paragraph with [[anomia]] inside.\n\n"
        "- one\n- two\n\n"
        "> quoted text\n\n"
        "| Col | Val |\n| --- | --- |\n| A | 1 |\n"
    )
    html = render_markdown_html(body)
    assert '<h2 id="intro">Intro</h2>' in html
    assert "<ul>" in html
    assert "<blockquote>" in html
    assert "<table>" in html
    assert 'href="?article=anomia&amp;type=concept"' in html


def test_render_toc_html():
    toc = [
        {"level": 2, "title": "Intro", "anchor": "intro"},
        {"level": 3, "title": "Sub", "anchor": "sub"},
    ]
    html = render_toc_html(toc)
    assert "Contenido" in html
    assert 'href="#intro"' in html
    assert 'href="#sub"' in html


def test_render_toc_html_empty():
    assert render_toc_html([]) == ""


def test_render_breadcrumbs():
    html = render_breadcrumbs("concept", "Anomia")
    assert "Jotapedia" in html
    assert "Conceptos" in html
    assert "Anomia" in html


def test_render_infobox():
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
    ensure_project_dirs()

    for name in ["zeta-concept", "alpha-concept"]:
        write_note(
            SETTINGS.concepts_dir / f"{name}.md",
            {"id": name, "title": name.replace("-", " ").title(), "note_type": "concept"},
            f"# {name}\n\nDefinition text.",
        )

    articles = list_articles_by_type("concept")
    assert len(articles) >= 2
    titles = [article["title"] for article in articles]
    assert titles == sorted(titles, key=str.lower)


def test_load_article_resolves_nested_source(kb_tmp: Path):
    ensure_project_dirs()

    note_dir = SETTINGS.sources_dir / "2026-s1" / "teoria"
    note_dir.mkdir(parents=True, exist_ok=True)
    write_note(
        note_dir / "durkheim-solidarity.md",
        {
            "id": "durkheim-solidarity",
            "title": "Durkheim on Solidarity",
            "note_type": "source",
        },
        "# Durkheim\n\n## Summary\nBody",
    )

    article = load_article("durkheim-solidarity", "source")
    assert article is not None
    assert article["title"] == "Durkheim on Solidarity"
    assert article["note_type"] == "source"


def test_renderer_does_not_modify_wiki_content(kb_tmp: Path):
    ensure_project_dirs()

    target = SETTINGS.concepts_dir / "institution.md"
    write_note(
        target,
        {"id": "institution", "title": "Institution", "note_type": "concept"},
        "# Institution\n\n## Definition\nA body with [[anomia]].",
    )
    before = target.read_text(encoding="utf-8")

    article = load_article("institution", "concept")
    assert article is not None
    render_markdown_html(article["body"])
    list_articles_by_type("concept")

    after = target.read_text(encoding="utf-8")
    assert after == before
