from __future__ import annotations

from datetime import date, datetime, timezone
import html
from pathlib import Path
import re
from urllib.parse import urlencode

import markdown

from kb_core.config import SETTINGS
from kb_core.utils import WIKILINK_RE, list_files_recursive, load_markdown_file, slugify


TYPE_LABELS = {
    "concept": "Conceptos",
    "author": "Autores",
    "source": "Fuentes",
    "course": "Cursos",
    "research": "Investigacion",
    "slide": "Diapositivas",
}

TYPE_DESCRIPTIONS = {
    "concept": "Definiciones, debates y relaciones teoricas.",
    "author": "Autores y tradiciones sociologicas.",
    "source": "Apuntes compilados a partir de materiales del curso.",
    "course": "Paginas indice por asignatura.",
}

_SEARCHABLE_TYPES = ("concept", "author", "source", "course")
_HEADING_RE = re.compile(r"^(#{2,3})\s+(.+)$", re.MULTILINE)
_TOP_H1_RE = re.compile(r"^\s*#\s+.+?(?:\n+|$)")
_ATTR_RE = re.compile(r"\s*\{#([^}]+)\}\s*$")
_MARKDOWN_EXTENSIONS = ("tables", "fenced_code", "sane_lists", "attr_list")


def _type_dirs() -> dict[str, Path]:
    return {
        "concept": SETTINGS.concepts_dir,
        "author": SETTINGS.authors_dir,
        "course": SETTINGS.courses_dir,
        "research": SETTINGS.research_dir,
        "slide": SETTINGS.slides_dir,
    }


def build_url(**params: str | None) -> str:
    query = urlencode({key: value for key, value in params.items() if value not in (None, "")})
    return f"?{query}" if query else "?"


def _escape(value: str | None) -> str:
    return html.escape(str(value or ""), quote=True)


def _strip_heading_markup(title: str) -> str:
    clean = _ATTR_RE.sub("", title).strip()
    return re.sub(r"[*_`~\[\]]", "", clean).strip()


def _strip_top_h1(body: str) -> str:
    return _TOP_H1_RE.sub("", body, count=1).lstrip()


def _guess_note_type(slug: str) -> str:
    canonical = slugify(slug)
    for note_type, base_dir in _type_dirs().items():
        if (base_dir / f"{canonical}.md").exists():
            return note_type
    for path in SETTINGS.sources_dir.rglob(f"{canonical}.md"):
        if path.is_file():
            return "source"
    return "concept"


def resolve_wikilinks_markdown(body: str) -> str:
    def _replace(match: re.Match[str]) -> str:
        slug = slugify(match.group(1).strip())
        display = (match.group(2) or match.group(1)).strip()
        note_type = _guess_note_type(slug)
        return f"[{display}]({build_url(article=slug, type=note_type)})"

    return WIKILINK_RE.sub(_replace, body)


def resolve_wikilinks_html(body: str) -> str:
    def _replace(match: re.Match[str]) -> str:
        slug = slugify(match.group(1).strip())
        display = (match.group(2) or match.group(1)).strip()
        note_type = _guess_note_type(slug)
        return f'<a href="{_escape(build_url(article=slug, type=note_type))}">{_escape(display)}</a>'

    return WIKILINK_RE.sub(_replace, body)


def _inject_heading_anchors(body: str) -> str:
    def _replace(match: re.Match[str]) -> str:
        marks = match.group(1)
        title = _strip_heading_markup(match.group(2))
        anchor = slugify(title)
        return f"{marks} {title} {{#{anchor}}}"

    return _HEADING_RE.sub(_replace, body)


def extract_toc(body: str) -> list[dict]:
    toc = []
    clean_body = _strip_top_h1(body)
    for match in _HEADING_RE.finditer(clean_body):
        level = len(match.group(1))
        title = _strip_heading_markup(match.group(2))
        toc.append({"level": level, "title": title, "anchor": slugify(title)})
    return toc


def render_markdown_html(body: str) -> str:
    prepared = _strip_top_h1(body)
    prepared = resolve_wikilinks_markdown(prepared)
    prepared = _inject_heading_anchors(prepared)
    return markdown.markdown(prepared, extensions=list(_MARKDOWN_EXTENSIONS))


def render_toc_html(toc: list[dict]) -> str:
    if not toc:
        return ""

    items = []
    for item in toc:
        level_class = "wiki-toc__item--sub" if item["level"] == 3 else ""
        items.append(
            f'<li class="wiki-toc__item {level_class}">'
            f'<a href="#{_escape(item["anchor"])}">{_escape(item["title"])}</a>'
            f"</li>"
        )

    return (
        '<div class="wiki-toc">'
        '<div class="wiki-toc__title">Contenido</div>'
        f'<ol class="wiki-toc__list">{"".join(items)}</ol>'
        "</div>"
    )


def render_breadcrumbs(note_type: str, title: str) -> str:
    category = TYPE_LABELS.get(note_type, note_type.title())
    return (
        '<nav class="wiki-breadcrumbs">'
        f'<a href="{_escape(build_url(view="home"))}">Jotapedia</a>'
        '<span class="wiki-breadcrumbs__sep">&rsaquo;</span>'
        f'<a href="{_escape(build_url(view="category", type=note_type))}">{_escape(category)}</a>'
        '<span class="wiki-breadcrumbs__sep">&rsaquo;</span>'
        f"<span>{_escape(title)}</span>"
        "</nav>"
    )


def render_infobox(frontmatter: dict) -> str:
    title = frontmatter.get("title", "")
    note_type = str(frontmatter.get("note_type", "") or "")
    type_label = TYPE_LABELS.get(note_type, note_type.title() or "Articulo")

    rows = [
        '<tr><th colspan="2" class="wiki-infobox__header">'
        f"{_escape(title)}</th></tr>",
        "<tr>"
        '<th class="wiki-infobox__label">Tipo</th>'
        f'<td class="wiki-infobox__value"><span class="wiki-pill wiki-pill--{_escape(note_type)}">{_escape(type_label)}</span></td>'
        "</tr>",
    ]

    for key, label in (
        ("semester", "Semestre"),
        ("course", "Curso"),
        ("compiled_at", "Compilado"),
        ("updated_at", "Actualizado"),
    ):
        value = frontmatter.get(key)
        if value:
            rows.append(
                "<tr>"
                f'<th class="wiki-infobox__label">{_escape(label)}</th>'
                f'<td class="wiki-infobox__value">{_escape(value)}</td>'
                "</tr>"
            )

    related = frontmatter.get("related_concepts", [])
    if related:
        related_html = ", ".join(
            f'<a href="{_escape(build_url(article=slugify(concept), type="concept"))}">{_escape(concept)}</a>'
            for concept in related[:8]
        )
        rows.append(
            "<tr>"
            '<th class="wiki-infobox__label">Relacionados</th>'
            f'<td class="wiki-infobox__value">{related_html}</td>'
            "</tr>"
        )

    if note_type == "source":
        for key, label, type_name in (
            ("concepts", "Conceptos", "concept"),
            ("authors", "Autores", "author"),
        ):
            values = frontmatter.get(key, [])
            if values:
                links = ", ".join(
                    f'<a href="{_escape(build_url(article=slugify(value), type=type_name))}">{_escape(value)}</a>'
                    for value in values[:10]
                )
                rows.append(
                    "<tr>"
                    f'<th class="wiki-infobox__label">{_escape(label)}</th>'
                    f'<td class="wiki-infobox__value">{links}</td>'
                    "</tr>"
                )

    return f'<table class="wiki-infobox">{"".join(rows)}</table>'


def _extract_preview(body: str) -> str:
    clean_body = _strip_top_h1(body)
    for line in clean_body.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith(("#", "|", "-", ">")):
            continue
        return stripped[:220]
    return ""


def _normalize_timestamp(value: object) -> datetime | None:
    if isinstance(value, datetime):
        dt = value
    elif isinstance(value, date):
        dt = datetime(value.year, value.month, value.day)
    else:
        text = str(value or "").strip()
        if not text:
            return None
        text = text.replace("Z", "+00:00")
        try:
            dt = datetime.fromisoformat(text)
        except ValueError:
            dt = None
            for fmt in ("%Y-%m-%d", "%Y/%m/%d"):
                try:
                    dt = datetime.strptime(text, fmt)
                    break
                except ValueError:
                    continue
            if dt is None:
                return None

    if dt.tzinfo is None:
        return dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def _article_timestamp(path: Path, frontmatter: dict) -> datetime:
    for key in ("updated_at", "compiled_at"):
        value = frontmatter.get(key)
        if not value:
            continue
        normalized = _normalize_timestamp(value)
        if normalized is not None:
            return normalized
    return datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)


def list_articles_by_type(note_type: str) -> list[dict]:
    dirs = _type_dirs()
    base_dir = dirs.get(note_type)
    if note_type == "source":
        base_dir = SETTINGS.sources_dir
    if base_dir is None:
        return []

    articles = []
    for path in list_files_recursive(base_dir, suffixes=(".md",)):
        frontmatter, body = load_markdown_file(path)
        articles.append(
            {
                "id": frontmatter.get("id", path.stem),
                "title": frontmatter.get("title", path.stem),
                "note_type": frontmatter.get("note_type", note_type),
                "path": str(path.relative_to(SETTINGS.kb_root)),
                "preview": _extract_preview(body),
                "course": frontmatter.get("course", ""),
                "semester": frontmatter.get("semester", ""),
                "updated_at": frontmatter.get("updated_at", ""),
                "compiled_at": frontmatter.get("compiled_at", ""),
            }
        )
    articles.sort(key=lambda item: item["title"].lower())
    return articles


def get_wiki_counts() -> dict[str, int]:
    return {note_type: len(list_articles_by_type(note_type)) for note_type in _SEARCHABLE_TYPES}


def get_recent_articles(limit: int = 8) -> list[dict]:
    articles = []
    for note_type in _SEARCHABLE_TYPES:
        for article in list_articles_by_type(note_type):
            path = SETTINGS.kb_root / article["path"]
            frontmatter, _ = load_markdown_file(path)
            article["timestamp"] = _article_timestamp(path, frontmatter)
            articles.append(article)
    articles.sort(key=lambda item: item["timestamp"], reverse=True)
    return articles[:limit]


def load_article(article_slug: str, article_type: str) -> dict | None:
    canonical = slugify(article_slug)
    type_dirs = _type_dirs()

    article_path = None
    if article_type == "source":
        for path in sorted(SETTINGS.sources_dir.rglob(f"{canonical}.md")):
            article_path = path
            break
    else:
        base_dir = type_dirs.get(article_type)
        if base_dir:
            candidate = base_dir / f"{canonical}.md"
            if candidate.exists():
                article_path = candidate

    if article_path is None:
        for base_dir in [SETTINGS.concepts_dir, SETTINGS.authors_dir, SETTINGS.courses_dir, SETTINGS.sources_dir]:
            candidate = base_dir / f"{canonical}.md"
            if candidate.exists():
                article_path = candidate
                break
        if article_path is None:
            for path in sorted(SETTINGS.wiki_dir.rglob(f"{canonical}.md")):
                article_path = path
                break

    if article_path is None:
        return None

    frontmatter, body = load_markdown_file(article_path)
    resolved_type = frontmatter.get("note_type", article_type or _guess_note_type(canonical))
    return {
        "id": frontmatter.get("id", article_path.stem),
        "title": frontmatter.get("title", article_path.stem),
        "note_type": resolved_type,
        "path": article_path,
        "frontmatter": frontmatter,
        "body": body,
    }


def _resolve_source_reference(reference: str) -> tuple[str, str] | None:
    path_text = str(reference).replace("\\", "/")
    path = SETTINGS.kb_root / path_text
    if not path.exists():
        candidate = SETTINGS.wiki_dir / path_text.replace("wiki/", "", 1)
        path = candidate if candidate.exists() else path
    if not path.exists():
        return None
    frontmatter, _ = load_markdown_file(path)
    title = frontmatter.get("title", path.stem)
    return title, build_url(article=frontmatter.get("id", path.stem), type="source")


def render_article_view_html(article: dict) -> str:
    title = article["title"]
    note_type = article["note_type"]
    frontmatter = article["frontmatter"]
    body_html = render_markdown_html(article["body"])
    toc_html = render_toc_html(extract_toc(article["body"]))
    infobox_html = render_infobox(frontmatter)

    related_links = []
    for concept in frontmatter.get("related_concepts", []):
        related_links.append(
            f'<a href="{_escape(build_url(article=slugify(concept), type="concept"))}">{_escape(concept)}</a>'
        )
    for source_reference in frontmatter.get("source_notes", []):
        resolved = _resolve_source_reference(source_reference)
        if resolved is None:
            continue
        source_title, source_url = resolved
        related_links.append(f'<a href="{_escape(source_url)}">{_escape(source_title)}</a>')

    related_html = ""
    if related_links:
        related_html = (
            '<section class="wiki-related">'
            '<h2>Articulos relacionados</h2>'
            f'<div class="wiki-related__links">{"".join(f"<span>{link}</span>" for link in related_links[:12])}</div>'
            "</section>"
        )

    return (
        f"{render_breadcrumbs(note_type, title)}"
        '<div class="wiki-article-page">'
        '<div class="wiki-article-page__main">'
        f'<h1 class="wiki-page-title">{_escape(title)}</h1>'
        f'<div class="wiki-article">{body_html}</div>'
        f"{related_html}"
        "</div>"
        '<aside class="wiki-article-page__rail">'
        f"{toc_html}"
        f"{infobox_html}"
        "</aside>"
        "</div>"
    )


def render_not_found_html(article_slug: str) -> str:
    return (
        '<section class="wiki-message">'
        '<h1 class="wiki-page-title">Articulo no encontrado</h1>'
        f"<p>No existe una pagina con el slug <code>{_escape(article_slug)}</code>.</p>"
        f'<p><a href="{_escape(build_url(view="home"))}">Volver a la portada de Jotapedia</a></p>'
        "</section>"
    )


def render_search_results_html(query: str, results: list[dict]) -> str:
    query_html = _escape(query)
    if not query.strip():
        return (
            '<section class="wiki-message">'
            '<h1 class="wiki-page-title">Buscar en Jotapedia</h1>'
            "<p>Escribe un termino sociologico para recorrer conceptos, autores, fuentes y cursos.</p>"
            "</section>"
        )

    rendered = []
    for item in results:
        note_type = item.get("note_type", "concept")
        label = TYPE_LABELS.get(note_type, note_type.title())
        meta_bits = [label]
        if item.get("course"):
            meta_bits.append(str(item["course"]))
        if item.get("semester"):
            meta_bits.append(str(item["semester"]))
        rendered.append(
            '<article class="wiki-search-result">'
            f'<h2><a href="{_escape(build_url(article=item["id"], type=note_type))}">{_escape(item["title"])}</a></h2>'
            f'<div class="wiki-search-result__meta">{_escape(" | ".join(meta_bits))}</div>'
            f'<p>{_escape(item.get("snippet", ""))}</p>'
            "</article>"
        )

    if not rendered:
        rendered.append('<p class="wiki-muted">No hay resultados para esta consulta.</p>')

    return (
        '<section class="wiki-search-page">'
        f'<h1 class="wiki-page-title">Resultados para "{query_html}"</h1>'
        f'<p class="wiki-muted">{len(results)} resultados</p>'
        f'{"".join(rendered)}'
        "</section>"
    )


def render_category_view_html(note_type: str, articles: list[dict], filter_query: str = "") -> str:
    label = TYPE_LABELS.get(note_type, note_type.title())
    description = TYPE_DESCRIPTIONS.get(note_type, "")
    filtered_articles = articles
    if filter_query:
        needle = filter_query.lower()
        filtered_articles = [item for item in articles if needle in item["title"].lower()]

    items = []
    for article in filtered_articles:
        meta_bits = []
        if article.get("course"):
            meta_bits.append(str(article["course"]))
        if article.get("semester"):
            meta_bits.append(str(article["semester"]))
        meta = f'<div class="wiki-index__meta">{_escape(" | ".join(meta_bits))}</div>' if meta_bits else ""
        preview = f'<p>{_escape(article["preview"])}</p>' if article.get("preview") else ""
        items.append(
            '<article class="wiki-index__item">'
            f'<h2><a href="{_escape(build_url(article=article["id"], type=note_type))}">{_escape(article["title"])}</a></h2>'
            f"{meta}"
            f"{preview}"
            "</article>"
        )

    if not items:
        items.append('<p class="wiki-muted">No hay articulos que coincidan con ese filtro.</p>')

    filter_form = (
        '<form action="" method="get" class="jp-search-form jp-search-form--inline">'
        '<input type="hidden" name="view" value="category" />'
        f'<input type="hidden" name="type" value="{_escape(note_type)}" />'
        f'<input type="search" name="filter" value="{_escape(filter_query)}" placeholder="Filtrar articulos" />'
        '<button type="submit">Filtrar</button>'
        "</form>"
    )

    return (
        '<section class="wiki-index">'
        f'<h1 class="wiki-page-title">{_escape(label)}</h1>'
        f'<p class="wiki-subtitle">{_escape(description)}</p>'
        f'<div class="wiki-index__toolbar"><span class="wiki-muted">{len(filtered_articles)} articulos</span>{filter_form}</div>'
        f'{"".join(items)}'
        "</section>"
    )


def render_home_html(counts: dict[str, int], recent_articles: list[dict]) -> str:
    category_cards = []
    for note_type in _SEARCHABLE_TYPES:
        label = TYPE_LABELS[note_type]
        category_cards.append(
            '<article class="wiki-category-card">'
            f'<h2><a href="{_escape(build_url(view="category", type=note_type))}">{_escape(label)}</a></h2>'
            f'<p>{_escape(TYPE_DESCRIPTIONS.get(note_type, ""))}</p>'
            f'<div class="wiki-category-card__count">{counts.get(note_type, 0)} articulos</div>'
            "</article>"
        )

    recent_items = []
    for item in recent_articles:
        label = TYPE_LABELS.get(item["note_type"], item["note_type"].title())
        recent_items.append(
            '<li>'
            f'<a href="{_escape(build_url(article=item["id"], type=item["note_type"]))}">{_escape(item["title"])}</a>'
            f' <span class="wiki-muted">({_escape(label)})</span>'
            "</li>"
        )

    recent_html = "".join(recent_items) or '<li class="wiki-muted">Todavia no hay articulos recientes.</li>'

    return (
        '<section class="wiki-home">'
        '<div class="wiki-home__hero">'
        '<div>'
        '<h1 class="wiki-page-title">Jotapedia</h1>'
        '<p class="wiki-subtitle">Una enciclopedia sociologica privada, construida sobre tu propia wiki de conocimiento.</p>'
        "</div>"
        '<form action="" method="get" class="jp-search-form jp-search-form--hero">'
        '<input type="hidden" name="view" value="search" />'
        '<input type="search" name="q" placeholder="Buscar conceptos, autores o fuentes" />'
        '<button type="submit">Buscar</button>'
        "</form>"
        "</div>"
        '<div class="wiki-home__grid">'
        '<section class="wiki-home__panel">'
        '<h2>Explorar por categoria</h2>'
        f'<div class="wiki-home__categories">{"".join(category_cards)}</div>'
        "</section>"
        '<section class="wiki-home__panel">'
        '<h2>Adiciones recientes</h2>'
        f'<ul class="wiki-home__recent">{recent_html}</ul>'
        "</section>"
        "</div>"
        "</section>"
    )


def render_sidebar_html(counts: dict[str, int], recent_articles: list[dict], active_section: str) -> str:
    nav_items = [
        ("home", "Portada", build_url(view="home")),
        ("concept", TYPE_LABELS["concept"], build_url(view="category", type="concept")),
        ("author", TYPE_LABELS["author"], build_url(view="category", type="author")),
        ("source", TYPE_LABELS["source"], build_url(view="category", type="source")),
        ("course", TYPE_LABELS["course"], build_url(view="category", type="course")),
        ("search", "Busqueda", build_url(view="search")),
    ]

    nav_html = []
    for key, label, url in nav_items:
        cls = "is-active" if active_section == key else ""
        count = f'<span class="jp-nav__count">{counts.get(key, "")}</span>' if key in counts else ""
        nav_html.append(f'<li class="{cls}"><a href="{_escape(url)}">{_escape(label)}</a>{count}</li>')

    recent_html = []
    for item in recent_articles[:6]:
        recent_html.append(
            "<li>"
            f'<a href="{_escape(build_url(article=item["id"], type=item["note_type"]))}">{_escape(item["title"])}</a>'
            "</li>"
        )

    recent_links_html = "".join(recent_html) or '<li class="wiki-muted">Sin cambios recientes.</li>'

    return (
        '<aside class="jp-sidebar">'
        '<section class="jp-portlet">'
        '<h2>Navegacion</h2>'
        f'<ul class="jp-nav">{"".join(nav_html)}</ul>'
        "</section>"
        '<section class="jp-portlet">'
        '<h2>Jotapedia</h2>'
        '<p class="wiki-muted">La app publica de Streamlit ahora es una wiki propia, centrada en lectura y navegacion.</p>'
        "</section>"
        '<section class="jp-portlet">'
        '<h2>Reciente</h2>'
        f'<ul class="jp-recent-links">{recent_links_html}</ul>'
        "</section>"
        "</aside>"
    )


def render_page_html(main_html: str, sidebar_html: str, search_query: str = "") -> str:
    return (
        '<div class="jp-shell">'
        '<header class="jp-header">'
        '<div class="jp-header__brand">'
        f'<a href="{_escape(build_url(view="home"))}" class="jp-wordmark">Jotapedia</a>'
        '<div class="jp-wordmark__tagline">La enciclopedia sociologica de Jota</div>'
        "</div>"
        '<nav class="jp-header__nav">'
        f'<a href="{_escape(build_url(view="home"))}">Portada</a>'
        f'<a href="{_escape(build_url(view="category", type="concept"))}">Conceptos</a>'
        f'<a href="{_escape(build_url(view="category", type="author"))}">Autores</a>'
        f'<a href="{_escape(build_url(view="category", type="source"))}">Fuentes</a>'
        "</nav>"
        '<form action="" method="get" class="jp-search-form jp-search-form--header">'
        '<input type="hidden" name="view" value="search" />'
        f'<input type="search" name="q" value="{_escape(search_query)}" placeholder="Buscar en Jotapedia" />'
        '<button type="submit">Buscar</button>'
        "</form>"
        "</header>"
        '<div class="jp-layout">'
        f"{sidebar_html}"
        f'<main class="jp-main">{main_html}</main>'
        "</div>"
        "</div>"
    )


WIKI_CSS = """
<style>
:root {
    --wiki-bg: #f6f6f6;
    --wiki-surface: #ffffff;
    --wiki-border: #a2a9b1;
    --wiki-soft-border: #c8ccd1;
    --wiki-muted: #54595d;
    --wiki-text: #202122;
    --wiki-link: #0645ad;
    --wiki-hover: #0b0080;
    --wiki-panel: #f8f9fa;
}

html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
    background: var(--wiki-bg);
    color: var(--wiki-text);
}

[data-testid="stHeader"],
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"],
#MainMenu,
footer {
    display: none;
}

.block-container {
    max-width: 1440px;
    padding-top: 0 !important;
    padding-bottom: 2rem !important;
}

.jp-shell {
    font-family: Arial, Helvetica, sans-serif;
    color: var(--wiki-text);
}

.jp-header {
    display: grid;
    grid-template-columns: minmax(220px, 300px) minmax(280px, 1fr) minmax(260px, 360px);
    align-items: end;
    gap: 16px;
    background: var(--wiki-surface);
    border-bottom: 1px solid var(--wiki-border);
    border-top: 2px solid #000;
    padding: 18px 24px 16px;
}

.jp-wordmark {
    color: #000;
    text-decoration: none;
    font-family: Georgia, "Times New Roman", serif;
    font-size: 2rem;
}

.jp-wordmark__tagline {
    color: var(--wiki-muted);
    font-size: 0.9rem;
    margin-top: 2px;
}

.jp-header__nav {
    display: flex;
    gap: 14px;
    flex-wrap: wrap;
    padding-bottom: 4px;
}

.jp-header__nav a,
.jp-nav a,
.jp-recent-links a,
.wiki-article a,
.wiki-search-result a,
.wiki-category-card a,
.wiki-home a,
.wiki-index a,
.wiki-breadcrumbs a,
.wiki-infobox a {
    color: var(--wiki-link);
    text-decoration: none;
}

.jp-header__nav a:hover,
.jp-nav a:hover,
.jp-recent-links a:hover,
.wiki-article a:hover,
.wiki-search-result a:hover,
.wiki-category-card a:hover,
.wiki-home a:hover,
.wiki-index a:hover,
.wiki-breadcrumbs a:hover,
.wiki-infobox a:hover {
    color: var(--wiki-hover);
    text-decoration: underline;
}

.jp-search-form {
    display: flex;
    gap: 8px;
    align-items: center;
}

.jp-search-form input[type="search"] {
    width: 100%;
    border: 1px solid var(--wiki-border);
    background: var(--wiki-surface);
    color: var(--wiki-text);
    padding: 0.45rem 0.6rem;
    font-size: 0.95rem;
}

.jp-search-form button {
    border: 1px solid var(--wiki-border);
    background: linear-gradient(#f8f9fa, #eaecf0);
    color: var(--wiki-text);
    padding: 0.45rem 0.8rem;
    cursor: pointer;
}

.jp-layout {
    display: grid;
    grid-template-columns: 250px minmax(0, 1fr);
    gap: 18px;
    align-items: start;
    padding: 20px 24px 0;
}

.jp-sidebar {
    display: grid;
    gap: 14px;
}

.jp-portlet {
    background: var(--wiki-panel);
    border: 1px solid var(--wiki-soft-border);
    padding: 12px 14px;
}

.jp-portlet h2 {
    font-size: 0.95rem;
    margin: 0 0 10px;
    padding-bottom: 6px;
    border-bottom: 1px solid var(--wiki-soft-border);
    font-weight: bold;
}

.jp-nav,
.jp-recent-links,
.wiki-home__recent,
.wiki-toc__list {
    list-style: none;
    margin: 0;
    padding: 0;
}

.jp-nav li,
.jp-recent-links li {
    display: flex;
    justify-content: space-between;
    gap: 12px;
    padding: 4px 0;
}

.jp-nav li.is-active a {
    font-weight: bold;
    color: #000;
}

.jp-nav__count {
    color: var(--wiki-muted);
    font-size: 0.85rem;
}

.jp-main {
    background: var(--wiki-surface);
    border: 1px solid var(--wiki-soft-border);
    padding: 20px 24px 28px;
    min-height: 70vh;
}

.wiki-page-title {
    font-family: Georgia, "Times New Roman", serif;
    font-size: 2rem;
    font-weight: normal;
    margin: 0 0 10px;
    padding-bottom: 8px;
    border-bottom: 1px solid var(--wiki-border);
}

.wiki-subtitle,
.wiki-muted,
.wiki-search-result__meta,
.wiki-index__meta,
.wiki-breadcrumbs {
    color: var(--wiki-muted);
}

.wiki-breadcrumbs {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 0.9rem;
    margin-bottom: 18px;
}

.wiki-home__hero {
    display: grid;
    grid-template-columns: minmax(0, 1fr) minmax(280px, 420px);
    gap: 24px;
    align-items: center;
    padding-bottom: 18px;
    border-bottom: 1px solid var(--wiki-soft-border);
}

.wiki-home__grid {
    display: grid;
    grid-template-columns: minmax(0, 1.25fr) minmax(280px, 0.75fr);
    gap: 20px;
    margin-top: 20px;
}

.wiki-home__panel h2,
.wiki-search-result h2,
.wiki-index__item h2,
.wiki-related h2 {
    font-family: Georgia, "Times New Roman", serif;
    font-size: 1.35rem;
    font-weight: normal;
    margin: 0 0 8px;
}

.wiki-home__categories {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 14px;
}

.wiki-category-card {
    border: 1px solid var(--wiki-soft-border);
    background: var(--wiki-panel);
    padding: 14px;
}

.wiki-category-card__count {
    color: var(--wiki-muted);
    font-size: 0.9rem;
}

.wiki-home__recent li {
    padding: 8px 0;
    border-bottom: 1px solid var(--wiki-soft-border);
}

.wiki-search-result,
.wiki-index__item {
    padding: 12px 0 16px;
    border-bottom: 1px solid var(--wiki-soft-border);
}

.wiki-index__toolbar {
    display: flex;
    justify-content: space-between;
    gap: 16px;
    align-items: center;
    margin-bottom: 8px;
    padding-bottom: 12px;
    border-bottom: 1px solid var(--wiki-soft-border);
}

.wiki-article-page {
    display: grid;
    grid-template-columns: minmax(0, 1fr) 320px;
    gap: 22px;
    align-items: start;
}

.wiki-article-page__rail {
    display: grid;
    gap: 16px;
    position: sticky;
    top: 18px;
}

.wiki-article {
    font-family: Georgia, "Times New Roman", serif;
    font-size: 1.05rem;
    line-height: 1.72;
}

.wiki-article h2 {
    font-family: Georgia, "Times New Roman", serif;
    font-weight: normal;
    font-size: 1.6rem;
    margin: 1.6rem 0 0.7rem;
    padding-bottom: 6px;
    border-bottom: 1px solid #eaecf0;
}

.wiki-article h3 {
    font-family: Georgia, "Times New Roman", serif;
    font-weight: bold;
    font-size: 1.15rem;
    margin: 1.2rem 0 0.4rem;
}

.wiki-article p,
.wiki-article ul,
.wiki-article ol,
.wiki-article blockquote,
.wiki-article table {
    margin: 0 0 1rem;
}

.wiki-article ul,
.wiki-article ol {
    padding-left: 1.4rem;
}

.wiki-article blockquote {
    border-left: 3px solid var(--wiki-soft-border);
    background: var(--wiki-panel);
    padding: 0.7rem 1rem;
}

.wiki-article table,
.wiki-infobox {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.95rem;
}

.wiki-article th,
.wiki-article td,
.wiki-infobox th,
.wiki-infobox td {
    border: 1px solid var(--wiki-soft-border);
    padding: 0.45rem 0.55rem;
    vertical-align: top;
}

.wiki-article th,
.wiki-infobox th {
    background: #eaecf0;
}

.wiki-toc,
.wiki-infobox {
    border: 1px solid var(--wiki-soft-border);
    background: var(--wiki-panel);
}

.wiki-toc {
    padding: 12px 14px;
}

.wiki-toc__title {
    font-weight: bold;
    margin-bottom: 8px;
}

.wiki-toc__item {
    padding: 3px 0;
}

.wiki-toc__item--sub {
    padding-left: 16px;
}

.wiki-infobox__header {
    text-align: center;
    font-family: Georgia, "Times New Roman", serif;
    font-size: 1.05rem;
}

.wiki-pill {
    display: inline-block;
    padding: 0.2rem 0.45rem;
    color: #fff;
    font-size: 0.8rem;
}

.wiki-pill--concept { background: #2a4b8d; }
.wiki-pill--author { background: #8b5a2b; }
.wiki-pill--source { background: #1f6a8a; }
.wiki-pill--course { background: #6a3f8b; }

.wiki-related {
    margin-top: 26px;
    padding-top: 10px;
    border-top: 1px solid var(--wiki-soft-border);
}

.wiki-related__links {
    display: flex;
    flex-wrap: wrap;
    gap: 12px 18px;
}

.wiki-message code {
    background: var(--wiki-panel);
    padding: 0.15rem 0.35rem;
    border: 1px solid var(--wiki-soft-border);
}

@media (max-width: 1100px) {
    .jp-header,
    .jp-layout,
    .wiki-home__hero,
    .wiki-home__grid,
    .wiki-home__categories,
    .wiki-article-page {
        grid-template-columns: 1fr;
    }

    .wiki-article-page__rail {
        position: static;
        order: -1;
    }
}

@media (max-width: 720px) {
    .block-container {
        padding-left: 0.6rem !important;
        padding-right: 0.6rem !important;
    }

    .jp-header,
    .jp-layout {
        padding-left: 12px;
        padding-right: 12px;
    }

    .jp-main {
        padding: 16px 14px 22px;
    }

    .wiki-page-title {
        font-size: 1.7rem;
    }
}
</style>
"""
