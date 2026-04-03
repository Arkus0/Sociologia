# Sociology Atlas Architecture

## Purpose

Sociology-only knowledge base where raw documents are evidence and markdown notes are the canonical working layer.

## Directory model

- `data/raw/<semester>/<course>/...` raw files and sidecars (`*.meta.json`)
- `data/wiki/sources/...` compiled source notes
- `data/wiki/concepts/...` concept notes
- `data/wiki/authors/...` author notes
- `data/wiki/courses/...` course notes
- `data/qa/answered_questions/...` answered QA artifacts with evidence
- `data/qa/open_questions/...` unresolved questions extracted from source notes
- `data/graph/atlas_graph.json` generated graph nodes/edges

## Module responsibilities

- `kb_core/models.py`
  - status enums
  - extraction result schema
  - metadata schema validation
  - compilation payload schema
- `kb_core/storage.py`
  - create required directories
  - save raw files
  - create and read metadata sidecars
  - maintain status transitions
- `kb_core/extraction.py`
  - extract text from `.pdf`, `.txt`, `.md`
  - return structured diagnostics
  - classify failures: unsupported, encrypted, parse_error, empty
- `kb_core/compiler.py`
  - explicit compilation stages
  - fallback behavior when LLM is unavailable/invalid
  - write canonical source markdown
  - rebuild concept/author/course pages
- `kb_core/graph_index.py`
  - derive graph nodes/edges from markdown notes
  - write `atlas_graph.json`
- `kb_core/qa.py`
  - deterministic weighted retrieval
  - optional LLM answer generation
  - persist answers with provenance
- `kb_core/lint.py`
  - detect missing frontmatter, failed raw docs, orphan concepts, duplicates

## Ingestion lifecycle

Document statuses:
- `saved_raw`
- `compile_pending`
- `compiling`
- `compiled`
- `parse_failed`
- `compile_failed`

Raw file save and parse/compile are independent. A parse failure cannot block raw persistence.

## Retrieval design

Field-weighted lexical ranking (title, concepts, authors, summary, body), with accent/case normalization and TF-IDF-like weighting for deterministic behavior.

## Notion export

Notion is optional and downstream only. Markdown remains source of truth.

## Known limitations

- No OCR yet for scanned PDFs.
- LLM JSON output is schema-validated, but low-context sources still produce shallow notes.
- Graph rendering depends on `streamlit-agraph` for interactive selection.

## Future extension points

- OCR plugin on `ExtractionStatus.EMPTY`
- richer course/synthesis notes
- optional embeddings layer alongside deterministic retrieval
- MCP server over markdown + graph artifacts
