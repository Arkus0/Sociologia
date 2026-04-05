from __future__ import annotations

import streamlit as st

from kb_core.search_engine import HybridSearchEngine
from kb_core.storage import ensure_project_dirs
from kb_core.wiki_renderer import (
    WIKI_CSS,
    get_recent_articles,
    get_wiki_counts,
    list_articles_by_type,
    load_article,
    render_article_view_html,
    render_category_view_html,
    render_home_html,
    render_not_found_html,
    render_page_html,
    render_search_results_html,
    render_sidebar_html,
)


st.set_page_config(page_title="Jotapedia", layout="wide")
ensure_project_dirs()


@st.cache_resource(show_spinner=False)
def _search_engine() -> HybridSearchEngine:
    return HybridSearchEngine()


@st.cache_data(show_spinner=False)
def _counts() -> dict[str, int]:
    return get_wiki_counts()


@st.cache_data(show_spinner=False)
def _recent(limit: int = 8) -> list[dict]:
    return get_recent_articles(limit=limit)


@st.cache_data(show_spinner=False)
def _articles_by_type(note_type: str) -> list[dict]:
    return list_articles_by_type(note_type)


@st.cache_data(show_spinner=False)
def _search(query: str) -> list[dict]:
    return _search_engine().search(query, top_k=15)


def _active_section(view: str, article: dict | None, note_type: str) -> str:
    if article:
        resolved_type = str(article.get("note_type", "home"))
        return resolved_type if resolved_type in {"concept", "author", "source", "course"} else "home"
    if view == "search":
        return "search"
    if view == "category":
        return note_type
    return "home"


st.markdown(WIKI_CSS, unsafe_allow_html=True)

params = st.query_params.to_dict()
view = str(params.get("view", "home") or "home")
article_slug = str(params.get("article", "") or "")
article_type = str(params.get("type", "concept") or "concept")
search_query = str(params.get("q", "") or "")
category_filter = str(params.get("filter", "") or "")

counts = _counts()
recent_articles = _recent(limit=10)

article = load_article(article_slug, article_type) if article_slug else None

if article_slug:
    main_html = render_article_view_html(article) if article else render_not_found_html(article_slug)
elif view == "search":
    results = _search(search_query) if search_query.strip() else []
    main_html = render_search_results_html(search_query, results)
elif view == "category":
    category_type = article_type if article_type else "concept"
    articles = _articles_by_type(category_type)
    main_html = render_category_view_html(category_type, articles, filter_query=category_filter)
else:
    main_html = render_home_html(counts, recent_articles[:8])

active_section = _active_section(view, article, article_type)
sidebar_html = render_sidebar_html(counts, recent_articles[:6], active_section)
page_html = render_page_html(main_html=main_html, sidebar_html=sidebar_html, search_query=search_query)

st.markdown(page_html, unsafe_allow_html=True)
