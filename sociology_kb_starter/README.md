# Sociology Knowledge Base Starter

Production-minded, markdown-first sociology knowledge base with Streamlit console.

## What this now prioritizes

- Low-friction ingestion (upload now, compile now or later)
- Strict separation between **raw storage** and **compilation/parsing**
- Defensive PDF extraction with structured diagnostics
- Explicit metadata schema validation
- Deterministic retrieval with weighted ranking
- Testable compilation pipeline and status tracking

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Environment variables

- `KB_ROOT` (optional, defaults to `sociology_kb_starter/data`)
- `LLM_PROVIDER` (`openai` or `anthropic`)
- `OPENAI_API_KEY`, `OPENAI_MODEL`
- `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`
- `NOTION_TOKEN`, `NOTION_DATABASE_ID`

The app works without API keys using fallback compilation and fallback Q&A.

## Ingestion and metadata

Primary flow:

1. Upload files (`pdf`, `md`, `txt`)
2. Optionally set semester/course
3. Save raw sources
4. Compile immediately or defer to Compile tab

Each raw file gets a sidecar `*.meta.json` with validated metadata and status.

## Compilation model

Pipeline stages:

1. Load metadata and set status `compiling`
2. Extract text (resilient extraction result object)
3. Build compilation payload
4. LLM compile or fallback compile
5. Validate output schema
6. Write markdown source note
7. Persist open questions
8. Set final status (`compiled`, `parse_failed`, or `compile_failed`)

## QA and retrieval

- Local retrieval across wiki markdown
- Normalized tokenization (case + accent normalization)
- Weighted ranking by fields (`title`, `concepts`, `authors`, `summary`, `body`)
- Saved Q&A outputs with evidence paths and scores

## Notion export

Notion remains optional and one-way from markdown notes.
See `docs/notion_schema.md`.

## Lint and health checks

Lint checks include:

- missing required frontmatter
- missing source anchor section
- duplicate titles
- orphan concepts
- raw files that previously failed parse/compile

## Tests

```bash
pytest
```

Test suite covers metadata/schema, sidecar generation, extraction failure handling, compile fallback, note writing, and retrieval ranking.

## Architecture

See `docs/architecture.md` for module responsibilities and extension points.
