from __future__ import annotations

from pathlib import Path
from textwrap import dedent

from kb_core.lint import run_lint_checks, suggest_new_articles
from kb_core.storage import ensure_project_dirs, write_note
from kb_core.utils import extract_alias_target


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


def test_extract_alias_target_ignores_vease_tambien_sections():
    body = dedent(
        """\
        # TLCAN

        ## Definicion

        Nota completa con desarrollo propio.

        ## Vease tambien

        - [[integracion-economica]]
        - [[mercado-comun]]
        """
    )

    assert extract_alias_target(body) is None


def test_lint_ignores_auxiliary_files_and_bom_aliases(kb_tmp: Path):
    """Lint ignores auxiliary wiki files and recognizes BOM redirects as aliases."""
    ensure_project_dirs()
    from kb_core.config import SETTINGS

    write_note(
        SETTINGS.authors_dir / "gary-king.md",
        {"id": "gary-king", "title": "Gary King", "note_type": "author", "updated_at": "2026-04-05"},
        "## Biografía intelectual\n\nAutor de referencia.",
    )

    (SETTINGS.authors_dir / "g-king.md").write_text(
        "\ufeff" + dedent(
            """\
            ---
            id: g-king
            title: G. King
            note_type: author
            updated_at: "2026-04-05"
            ---

            Véase [[gary-king|Gary King]].
            """
        ),
        encoding="utf-8",
    )

    (SETTINGS.wiki_dir / "GRAPH.md").write_text(
        "# Graph\n\nAuxiliary artifact.",
        encoding="utf-8",
    )
    source_dir = SETTINGS.sources_dir / "2026-s1" / "metodologia"
    source_dir.mkdir(parents=True, exist_ok=True)
    write_note(
        source_dir / "cuadernos.md",
        {
            "id": "cuadernos",
            "title": "Cuadernos",
            "note_type": "source",
            "semester": "2026-S1",
            "course": "Metodologia",
        },
        "## Canonical note\nEsta ficha se mantiene por compatibilidad historica. La entrada canonica es [[cuaderno-canonico]].",
    )

    issues = run_lint_checks()

    alias_issues = [issue for issue in issues if issue["path"].endswith(r"authors\g-king.md")]
    assert not any(issue["type"] == "missing_frontmatter" for issue in alias_issues)
    assert not any(issue["type"] == "missing_summary_section" for issue in alias_issues)
    source_alias_issues = [issue for issue in issues if issue["path"].endswith(r"sources\2026-s1\metodologia\cuadernos.md")]
    assert not any(issue["type"] == "missing_source_anchors_section" for issue in source_alias_issues)
    assert not any(issue["type"] == "missing_concepts" for issue in source_alias_issues)
    assert not any(issue["path"] == r"wiki\GRAPH.md" for issue in issues)


def test_lint_accepts_extended_author_summary_headings(kb_tmp: Path):
    """Lint accepts author summary headings already used in the wiki."""
    ensure_project_dirs()
    from kb_core.config import SETTINGS

    write_note(
        SETTINGS.authors_dir / "esther-fernandez-mostaza.md",
        {
            "id": "esther-fernandez-mostaza",
            "title": "Esther Fernandez Mostaza",
            "note_type": "author",
            "updated_at": "2026-04-05",
        },
        "# Esther Fernandez Mostaza\n\n## Biographical sketch\n\nAutora de referencia.",
    )
    write_note(
        SETTINGS.authors_dir / "san-agustin.md",
        {
            "id": "san-agustin",
            "title": "San Agustin",
            "note_type": "author",
            "updated_at": "2026-04-05",
        },
        "# San Agustin\n\n## Panorama biografico\n\nAutor de referencia.",
    )

    issues = run_lint_checks()

    summary_issues = [
        issue
        for issue in issues
        if issue["type"] == "missing_summary_section"
        and issue["path"] in {
            r"wiki\authors\esther-fernandez-mostaza.md",
            r"wiki\authors\san-agustin.md",
        }
    ]
    assert not summary_issues


def test_lint_duplicate_titles_are_scoped_by_note_type(kb_tmp: Path):
    """Lint should not flag a course and a source that legitimately share a title."""
    ensure_project_dirs()
    from kb_core.config import SETTINGS

    write_note(
        SETTINGS.courses_dir / "metodologia.md",
        {
            "id": "metodologia",
            "title": "Metodologia de las ciencias sociales",
            "note_type": "course",
            "semester": "2026-S1",
        },
        "# Metodologia\n\n## Scope\nCurso.",
    )

    note_dir = SETTINGS.sources_dir / "2026-s1" / "metodologia"
    note_dir.mkdir(parents=True, exist_ok=True)
    write_note(
        note_dir / "metodologia-de-las-ciencias-sociales.md",
        {
            "id": "metodologia-de-las-ciencias-sociales",
            "title": "Metodologia de las ciencias sociales",
            "note_type": "source",
            "semester": "2026-S1",
            "course": "Metodologia",
            "concepts": ["diseno de investigacion"],
        },
        "# Metodologia\n\n## Summary\nFuente.\n\n## Source anchors\n- p.1",
    )

    issues = run_lint_checks()

    duplicate_title_issues = [issue for issue in issues if issue["type"] == "duplicate_title"]
    assert not duplicate_title_issues
