# Sociology Atlas Starter

Graph-first, markdown-first sociology knowledge system.

## Core architecture

- `app.py` — Streamlit atlas UI (exploration first, operations second)
- `kb_core/config.py` — settings and canonical folder structure
- `kb_core/storage.py` — raw save + sidecar metadata lifecycle
- `kb_core/extraction.py` — robust PDF/text extraction with diagnostics
- `kb_core/compiler.py` — explicit compilation stages and note writing
- `kb_core/graph_index.py` — derived graph artifact generation
- `kb_core/qa.py` — deterministic retrieval + QA persistence
- `kb_core/lint.py` — health checks for note quality and pipeline failures
- `tests/` — pipeline and indexing tests

## Canonical data model

- `data/raw/` — raw evidence (PDF/TXT/MD) + sidecar metadata
- `data/wiki/sources/` — compiled source notes
- `data/wiki/concepts/` — concept pages
- `data/wiki/authors/` — author pages
- `data/wiki/courses/` — course pages
- `data/qa/` — answered/open question artifacts
- `data/graph/` — generated graph indexes (`atlas_graph.json`)

Markdown is the source of truth for retrieval and graph connections.

## Ingestion flow

1. Upload one or more files.
2. Optionally set semester/course defaults.
3. Save raw files immediately (`saved_raw` + `compile_pending`).
4. Compile now or compile later.

Raw saving never depends on parse success.

## Compilation flow

Stages in `compile_raw_document`:
1. mark metadata as `compiling`
2. extract text with structured diagnostics
3. parse failure path -> `parse_failed`
4. LLM compile or deterministic fallback
5. validate output schema
6. write source markdown note
7. store open questions
8. finalize metadata status

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
