# Jotapedia

Markdown-first sociology knowledge system with a Streamlit frontend that now opens directly as a private Wikipedia-style wiki.

## Core architecture

- `app.py` - Streamlit entrypoint for the public Jotapedia wiki.
- `kb_core/wiki_renderer.py` - article rendering, wiki shell HTML, navigation, infoboxes, and Wikipedia-style CSS.
- `kb_core/search_engine.py` - lexical and hybrid wiki search.
- `kb_core/services.py` - reusable knowledge operations for UI and MCP.
- `kb_core/mcp_tools.py` - MCP tool handlers mapped to services.
- `mcp_server.py` - remote MCP server entrypoint.
- `kb_core/config.py` - settings and canonical folder structure.
- `kb_core/storage.py` - raw save + sidecar metadata lifecycle.
- `kb_core/compiler.py` - compilation stages and note writing.
- `kb_core/graph_index.py` - derived graph artifact generation.
- `kb_core/qa.py` - deterministic retrieval + QA persistence.
- `kb_core/lint.py` - health checks for note quality and pipeline failures.
- `tests/` - pipeline, indexing, renderer, and MCP handler tests.

## Canonical data model

- `data/raw/` - raw evidence (PDF/TXT/MD) + sidecar metadata.
- `data/wiki/sources/` - compiled source notes.
- `data/wiki/concepts/` - concept pages.
- `data/wiki/authors/` - author pages.
- `data/wiki/courses/` - course index pages.
- `data/qa/` - answered/open question artifacts.
- `data/graph/` - generated graph indexes.

Markdown remains the source of truth for retrieval and graph connections. The Jotapedia redesign does not modify wiki content.

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Opening `streamlit run app.py` launches directly into Jotapedia with `home`, `category`, `search`, and `article` views.

## MCP server

```bash
python mcp_server.py
```

## Test

```bash
pytest
```
