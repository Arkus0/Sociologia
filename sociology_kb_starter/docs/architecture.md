# Sociology KB Architecture (Refactor 2026-04-03)

## Layered modules

- **UI (Streamlit)**: `app.py`
- **Configuration**: `kb_core/config.py`
- **Storage & metadata**: `kb_core/storage.py`, `kb_core/models.py`
- **Extraction**: `kb_core/extraction.py`
- **Compilation pipeline**: `kb_core/compiler.py`
- **Retrieval and QA**: `kb_core/qa.py`
- **Notion export**: `kb_core/notion_sync.py`
- **Health/lint checks**: `kb_core/lint.py`

## Ingestion flow

1. User uploads file(s) in Streamlit.
2. `save_uploaded_bytes()` writes raw file to `data/raw/<semester>/<course>/`.
3. Sidecar metadata (`*.meta.json`) is validated with Pydantic and persisted.
4. File status moves to `compile_pending`.

Important: **raw save is independent from parse or compile**.

## Compilation flow

`compile_raw_document()` stages:

1. Set status to `compiling`.
2. Run extraction with `extract_text()`.
3. If extraction fails (`encrypted`, `parse_error`, `empty`, `unsupported`) set `parse_failed` and stop gracefully.
4. Build source payload for LLM or fallback.
5. Validate LLM JSON into `CompiledSourcePayload`.
6. Write source note markdown.
7. Persist open questions.
8. Update metadata status to `compiled` (or `compile_failed` if note write crashes).

## Status model

`DocumentStatus` values:

- `saved_raw`
- `compile_pending`
- `compiling`
- `compiled`
- `parse_failed`
- `compile_failed`

## Retrieval model

`retrieve_notes()` uses deterministic weighted lexical ranking:

- normalized (case + accents)
- weighted fields (`title`, `concepts`, `authors`, `summary`, `body`)
- TF-IDF-like scoring

This keeps retrieval local and inspectable while improving over plain token overlap.

## Extension points

- OCR plugin can be added after `ExtractionStatus.EMPTY` for scanned PDFs.
- Metadata schema can be extended in `RawDocumentMetadata`.
- Additional exporters can follow `notion_sync.py` pattern.
