# Programacionscidat — Sociology Atlas v1

A focused, markdown-first sociology knowledge-base system.

This repository is intentionally single-purpose: ingest sociology source material, compile canonical markdown notes, generate a knowledge graph, and support inspectable retrieval/Q&A.

## Product identity

- **Domain:** sociology only
- **Canonical layer:** markdown (`data/wiki/...`)
- **Raw evidence layer:** uploaded source files (`data/raw/...`)
- **Derived layer:** graph/index artifacts (`data/graph/...`)

## Quick start

```bash
cd sociology_kb_starter
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Tests

```bash
cd sociology_kb_starter
pytest
```

For architecture and flow details, see `sociology_kb_starter/docs/architecture.md`.
