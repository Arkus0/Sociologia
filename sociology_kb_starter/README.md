# Sociology Knowledge Base Starter

A practical starter project for building an incremental sociology wiki by semester using:

- **Streamlit** as the operating console
- **Markdown** as the long-term source of truth
- **Optional LLM providers** (OpenAI or Anthropic) for source compilation, concept synthesis, and Q&A
- **Optional Notion sync** as a dashboard/export layer, not the core database

## What this project already includes

- A working Streamlit app with tabs for Dashboard, Ingest, Compile, Explore, Ask, Lint, and Notion
- A file-based wiki structure with course notes, concept notes, author notes, syntheses, and open questions
- Raw document ingestion for `.md`, `.txt`, and `.pdf`
- Sidecar metadata files so each source keeps semester/course provenance
- A compiler that turns raw sources into structured markdown notes with YAML frontmatter
- Incremental concept and author indexes
- Basic local retrieval + optional LLM-grounded answers with note citations
- Health checks for missing metadata, missing source anchors, orphan concepts, and duplicate titles
- A sample bootstrap script with sociology content

## Why this structure

The design treats **Markdown as the durable knowledge layer**. Notion is optional and useful for coordination, but the wiki itself is stored in versionable plain text so you can audit, diff, and evolve it across the full degree.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
python scripts/bootstrap_sample.py
streamlit run app.py
```

## Environment variables

See `.env.example`.

You can run the project with **no API keys**. In that case it will still ingest files, compile fallback notes, build indexes, run lint checks, and produce retrieval packs. If you add an API key, the app becomes much more useful.

Supported providers:

- `OPENAI_API_KEY` + `LLM_PROVIDER=openai`
- `ANTHROPIC_API_KEY` + `LLM_PROVIDER=anthropic`

## Recommended usage during a semester

1. Upload raw files into `data/raw/<semester>/<course>/`
2. Add or review metadata during upload in the Streamlit UI
3. Compile raw sources into source notes
4. Rebuild concept and author notes incrementally
5. Ask questions against the wiki
6. Review lint issues every week
7. Export selected notes to Notion if useful

## Important design rule

This system is only worth using if **traceability stays mandatory**.

Each note should preserve:

- source path
- semester
- course
- concepts and authors involved
- whether the note is reviewed or not
- source anchors or citations whenever possible

Without that, the wiki becomes polished nonsense.

## Suggested next steps after this starter

- Add Git version control and commit after each lecture pack
- Add image extraction and OCR only if you truly need it
- Add better semantic search later, not first
- Add a proper graph view once your concept coverage is stable
- Add assignment-specific output templates for PECs, essays, oral exams, and flashcards

## Notion position

Use Notion as a planning and dashboard layer, not as the final knowledge store. This repo is the knowledge store.

See `docs/notion_schema.md` for a recommended database design.
