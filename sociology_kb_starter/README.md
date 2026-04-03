# Sociology Atlas Starter

Graph-first, markdown-first sociology knowledge system.

## Core architecture

- `app.py` — Streamlit atlas UI (one interface, not core logic)
- `kb_core/services.py` — reusable knowledge operations for UI and MCP
- `kb_core/mcp_tools.py` — MCP tool handlers mapped to services
- `mcp_server.py` — remote MCP server entrypoint
- `kb_core/config.py` — settings and canonical folder structure
- `kb_core/storage.py` — raw save + sidecar metadata lifecycle
- `kb_core/extraction.py` — robust PDF/text extraction with diagnostics
- `kb_core/compiler.py` — explicit compilation stages and note writing
- `kb_core/graph_index.py` — derived graph artifact generation
- `kb_core/qa.py` — deterministic retrieval + QA persistence
- `kb_core/lint.py` — health checks for note quality and pipeline failures
- `tests/` — pipeline, indexing, services, and MCP handler tests

## Canonical data model

- `data/raw/` — raw evidence (PDF/TXT/MD) + sidecar metadata
- `data/wiki/sources/` — compiled source notes (canonical layer)
- `data/wiki/concepts/` — derived concept pages
- `data/wiki/authors/` — derived author pages
- `data/wiki/courses/` — derived course pages
- `data/qa/` — answered/open question artifacts
- `data/graph/` — generated graph indexes (`atlas_graph.json`)

Markdown is the source of truth for retrieval and graph connections.

## Reusable service operations

`kb_core.services` exposes:

- `search_notes(query, filters)`
- `read_note(path_or_id)`
- `list_notes(note_type, filters)`
- `list_courses()`
- `list_authors()`
- `list_concepts()`
- `get_graph_neighbors(node_id, node_type, depth=1)`
- `get_recent_sources(limit)`
- `get_source_provenance(note_id)`
- `propose_note_edit(note_id, instruction)`
- `build_patch_for_note(note_id, new_content)`
- `create_branch_and_pr_for_changes(changes)`

## MCP server

```bash
python mcp_server.py
```

Read tools are exposed first (`kb_search_notes`, `kb_read_note`, etc.).
Write is PR-oriented (`kb_create_pr_for_note_changes`).

See:
- `docs/architecture.md`
- `docs/markdown_knowledge_model.md`
- `docs/mcp_server.md`

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Test

```bash
pytest
```
