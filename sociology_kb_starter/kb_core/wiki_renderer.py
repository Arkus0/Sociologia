from __future__ import annotations

import re
from pathlib import Path

from kb_core.config import SETTINGS
from kb_core.utils import WIKILINK_RE, slugify


# ── Wikilink resolution ─────────────────────────────────────────────

def resolve_wikilinks_html(body: str) -> str:
    """Replace [[slug]] and [[slug|display]] with clickable HTML links for Streamlit."""

    def _replace(match: re.Match) -> str:
        slug = match.group(1).strip()
        display = (match.group(2) or slug).strip()
        # Determine note_type by checking which directory the slug belongs to
        note_type = _guess_note_type(slug)
        return (
            f'<a href="?article={slug}&type={note_type}" '
            f'style="color:#3366CC;text-decoration:none;border-bottom:1px dotted #3366CC">'
            f'{display}</a>'
        )

    return WIKILINK_RE.sub(_replace, body)


def _guess_note_type(slug: str) -> str:
    """Guess the note_type for a slug by checking which wiki directory contains it."""
    canonical = slugify(slug)
    if (SETTINGS.concepts_dir / f"{canonical}.md").exists():
        return "concept"
    if (SETTINGS.authors_dir / f"{canonical}.md").exists():
        return "author"
    if (SETTINGS.courses_dir / f"{canonical}.md").exists():
        return "course"
    for path in SETTINGS.sources_dir.rglob(f"{canonical}.md"):
        return "source"
    return "concept"  # default fallback


# ── Table of Contents ────────────────────────────────────────────────

_HEADING_RE = re.compile(r"^(#{2,3})\s+(.+)$", re.MULTILINE)


def extract_toc(body: str) -> list[dict]:
    """Extract H2/H3 headings as a table of contents."""
    toc = []
    for match in _HEADING_RE.finditer(body):
        level = len(match.group(1))
        title = match.group(2).strip()
        anchor = slugify(title)
        toc.append({"level": level, "title": title, "anchor": anchor})
    return toc


def render_toc_html(toc: list[dict]) -> str:
    """Render TOC as an HTML sidebar-ready list."""
    if not toc:
        return ""
    lines = ['<div style="font-size:0.85em;line-height:1.9">']
    lines.append('<strong>Contenido</strong>')
    for item in toc:
        indent = "0" if item["level"] == 2 else "16px"
        lines.append(
            f'<div style="margin-left:{indent}">'
            f'<a href="#{item["anchor"]}" style="color:#3366CC;text-decoration:none">'
            f'{item["title"]}</a></div>'
        )
    lines.append("</div>")
    return "\n".join(lines)


# ── Breadcrumbs ──────────────────────────────────────────────────────

_TYPE_LABELS = {
    "concept": "Conceptos",
    "author": "Autores",
    "source": "Fuentes",
    "course": "Cursos",
    "research": "Investigación",
}


def render_breadcrumbs(note_type: str, title: str) -> str:
    """Render Wikipedia-style breadcrumbs as HTML."""
    category = _TYPE_LABELS.get(note_type, note_type.title())
    return (
        f'<nav style="font-size:0.85em;color:#666;margin-bottom:8px">'
        f'<a href="?view=home" style="color:#3366CC;text-decoration:none">Wiki</a>'
        f' › '
        f'<a href="?view=category&type={note_type}" style="color:#3366CC;text-decoration:none">{category}</a>'
        f' › {title}'
        f'</nav>'
    )


# ── Infobox ──────────────────────────────────────────────────────────

def render_infobox(frontmatter: dict) -> str:
    """Render a Wikipedia-style infobox card from frontmatter."""
    note_type = frontmatter.get("note_type", "")
    title = frontmatter.get("title", "")

    rows = []
    rows.append(f'<tr><td colspan="2" style="background:#E8E8E8;text-align:center;'
                f'font-weight:bold;padding:8px;font-size:1.1em">{title}</td></tr>')

    type_colors = {
        "concept": "#59A14F",
        "author": "#F28E2B",
        "source": "#4E79A7",
        "course": "#E15759",
    }
    color = type_colors.get(note_type, "#777")
    type_label = _TYPE_LABELS.get(note_type, note_type)
    rows.append(f'<tr><td style="padding:4px 8px;font-weight:bold">Tipo</td>'
                f'<td style="padding:4px 8px"><span style="display:inline-block;'
                f'background:{color};color:white;padding:2px 8px;border-radius:3px;'
                f'font-size:0.85em">{type_label}</span></td></tr>')

    field_labels = {
        "semester": "Semestre",
        "course": "Curso",
        "compiled_at": "Compilado",
        "updated_at": "Actualizado",
    }
    for key, label in field_labels.items():
        value = frontmatter.get(key)
        if value:
            rows.append(f'<tr><td style="padding:4px 8px;font-weight:bold">{label}</td>'
                        f'<td style="padding:4px 8px">{value}</td></tr>')

    # Related concepts
    related = frontmatter.get("related_concepts", [])
    if related:
        links = ", ".join(
            f'<a href="?article={slugify(c)}&type=concept" style="color:#3366CC">{c}</a>'
            for c in related[:8]
        )
        rows.append(f'<tr><td style="padding:4px 8px;font-weight:bold">Relacionados</td>'
                    f'<td style="padding:4px 8px">{links}</td></tr>')

    # Concepts for source notes
    concepts = frontmatter.get("concepts", [])
    if concepts and note_type == "source":
        links = ", ".join(
            f'<a href="?article={slugify(c)}&type=concept" style="color:#3366CC">{c}</a>'
            for c in concepts[:10]
        )
        rows.append(f'<tr><td style="padding:4px 8px;font-weight:bold">Conceptos</td>'
                    f'<td style="padding:4px 8px">{links}</td></tr>')

    # Authors for source notes
    authors = frontmatter.get("authors", [])
    if authors and note_type == "source":
        links = ", ".join(
            f'<a href="?article={slugify(a)}&type=author" style="color:#3366CC">{a}</a>'
            for a in authors[:10]
        )
        rows.append(f'<tr><td style="padding:4px 8px;font-weight:bold">Autores</td>'
                    f'<td style="padding:4px 8px">{links}</td></tr>')

    table_rows = "\n".join(rows)
    return (
        f'<table style="float:right;margin:0 0 12px 16px;border:1px solid #CCC;'
        f'border-collapse:collapse;width:280px;background:#FAFAFA;font-size:0.9em">'
        f'{table_rows}</table>'
    )


# ── Category listing ─────────────────────────────────────────────────

def list_articles_by_type(note_type: str) -> list[dict]:
    """List all articles of a given type, sorted alphabetically."""
    dirs = {
        "concept": SETTINGS.concepts_dir,
        "author": SETTINGS.authors_dir,
        "course": SETTINGS.courses_dir,
    }
    base_dir = dirs.get(note_type)
    if base_dir is None and note_type == "source":
        base_dir = SETTINGS.sources_dir
    if base_dir is None:
        return []

    from kb_core.utils import list_files_recursive, load_markdown_file

    articles = []
    for path in list_files_recursive(base_dir, suffixes=(".md",)):
        frontmatter, body = load_markdown_file(path)
        # Extract first paragraph as preview
        preview = ""
        for line in body.split("\n"):
            stripped = line.strip()
            if stripped and not stripped.startswith("#") and not stripped.startswith("---"):
                preview = stripped[:150]
                break
        articles.append({
            "id": frontmatter.get("id", path.stem),
            "title": frontmatter.get("title", path.stem),
            "note_type": frontmatter.get("note_type", note_type),
            "path": str(path.relative_to(SETTINGS.kb_root)),
            "preview": preview,
            "course": frontmatter.get("course", ""),
            "semester": frontmatter.get("semester", ""),
        })
    articles.sort(key=lambda a: a["title"].lower())
    return articles


# ── CSS ──────────────────────────────────────────────────────────────

WIKI_CSS = """
<style>
.wiki-article {
    max-width: 900px;
    margin: 0 auto;
    font-family: 'Linux Libertine', 'Georgia', 'Times', serif;
    line-height: 1.65;
    color: #222;
}
.wiki-article h1 {
    font-size: 1.8em;
    border-bottom: 1px solid #A2A9B1;
    padding-bottom: 4px;
    margin-bottom: 8px;
    font-weight: normal;
}
.wiki-article h2 {
    font-size: 1.35em;
    border-bottom: 1px solid #EAECF0;
    padding-bottom: 2px;
    margin-top: 24px;
    font-weight: normal;
}
.wiki-article h3 {
    font-size: 1.1em;
    margin-top: 16px;
    font-weight: bold;
}
.wiki-article a {
    color: #3366CC;
    text-decoration: none;
}
.wiki-article a:hover {
    text-decoration: underline;
}
.wiki-article blockquote {
    border-left: 3px solid #C8CCD1;
    margin: 12px 0;
    padding: 4px 16px;
    color: #555;
    background: #F8F9FA;
}
.wiki-article table {
    border-collapse: collapse;
    margin: 12px 0;
}
.wiki-article th, .wiki-article td {
    border: 1px solid #C8CCD1;
    padding: 6px 10px;
    text-align: left;
}
.wiki-article th {
    background: #EAECF0;
}
.wiki-search-result {
    padding: 8px 0;
    border-bottom: 1px solid #EEE;
}
.wiki-search-result a {
    font-size: 1.1em;
    color: #3366CC;
    text-decoration: none;
}
.wiki-search-result .meta {
    font-size: 0.85em;
    color: #666;
}
.wiki-category-card {
    background: #F8F9FA;
    border: 1px solid #EAECF0;
    border-radius: 4px;
    padding: 16px;
    margin-bottom: 8px;
}
</style>
"""
