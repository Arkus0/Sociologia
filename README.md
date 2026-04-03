# Sociología Knowledge Base

This repository is now **single-purpose**: a sociology-focused knowledge-base product for ingesting class material, compiling structured notes, and answering questions over the generated wiki.

Legacy coursework and unrelated artifacts were removed to keep the repository intentional and domain-focused.

## Project layout

- `sociology_kb_starter/` — core sociology KB application and pipeline
  - `app.py` — Streamlit app
  - `kb_core/` — ingestion, extraction, compilation, retrieval, lint, storage
  - `tests/` — automated tests
  - `docs/` — architecture and Notion schema docs

## Quick start

```bash
cd sociology_kb_starter
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Testing

```bash
cd sociology_kb_starter
pytest
```

## Notes on repository name

I cannot rename the remote GitHub repository from this local workspace.
If you want the repo name changed to `sociologia`/`sociología`, rename it in GitHub repository settings.
