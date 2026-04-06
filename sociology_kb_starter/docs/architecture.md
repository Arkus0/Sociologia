# Sociology Atlas Architecture

## Purpose

Sociology-only knowledge base where raw documents are evidence and markdown notes are the canonical working layer.

## Directory model

- `data/raw/<semester>/<course>/...` raw files and sidecars (`*.meta.json`)
- `data/wiki/sources/...` compiled source notes (canonical)
- `data/wiki/concepts/...` derived concept notes — **225 enriched, 0 stubs** (REVIEW_LOG 1–206)
- `data/wiki/authors/...` derived author notes — **89 enriched + 6 redirects + 8 aliases = 103 files, 0 stubs** (REVIEW_LOG 207–295)
- `data/wiki/courses/...` derived course notes from canonical source notes
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
- `kb_core/services.py`
  - reusable knowledge operations consumed by Streamlit and MCP
  - deterministic read APIs
  - safe PR-oriented write APIs
- `kb_core/mcp_tools.py`
  - MCP-facing tool handlers with stable names and simple schemas
- `mcp_server.py`
  - remote MCP app, read tools first, write tool for PR workflows

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

## Safe write strategy

- Do not expose destructive direct filesystem edits as primary tool path.
- Preferred write flow:
  1. Propose note update (`propose_note_edit`)
  2. Build a reviewable patch (`build_patch_for_note`)
  3. Create branch + commit for PR review (`create_branch_and_pr_for_changes`)
- GitHub PR is the operational write boundary.

## External agent readiness

- Stable markdown paths + explicit frontmatter schema.
- Deterministic retrieval and graph generation.
- MCP tool names are explicit (`kb_*`) and use concise, typed inputs.

## Notion export

Notion is optional and downstream only. Markdown remains source of truth.
