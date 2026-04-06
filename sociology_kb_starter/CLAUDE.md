# Canvas Workflow — Agent Instructions

## Pipeline Architecture (updated 2026-04-05)

### PDF Extraction (`kb_core/extraction.py`)
- **OCR**: Real Tesseract OCR via `page.get_textpage_ocr(language="spa+eng", dpi=300)` for scanned pages (<100 chars). Falls back gracefully to text-only if Tesseract is not installed.
- **Text cleaning**: `clean_extracted_text()` removes repeated headers/footers (3+ occurrences), rejoins end-of-line hyphens, strips bare page numbers, collapses excessive blank lines.

### LLM Calls (`kb_core/llm.py`)
- **JSON mode**: Groq and OpenAI use `response_format={"type": "json_object"}`. Anthropic uses string parsing.
- **Retries**: 3 attempts with exponential backoff (2s → 4s → 8s) for rate limits (429), connection errors, and timeouts.
- **Providers**: Groq (primary/cheapest), OpenAI (`gpt-4.1-mini`), Anthropic (`claude-3-7-sonnet-latest`).

### Compilation (`kb_core/compiler.py`)
- **Smart chunking**: Page-aware excerpt up to 32k chars (head + tail on `[Page N]` markers) instead of arbitrary `text[:12000]`.
- **LLM max_tokens**: 4000 (up from 2000) for richer compilation output.
- **Post-compile**: Rebuilds graph index, search index, AND embedding index (if OpenAI key is available).

### Search & RAG (`kb_core/search_engine.py`, `kb_core/embeddings.py`)
- **Hybrid search**: Combines TF-IDF lexical search with OpenAI embedding vectors via Reciprocal Rank Fusion (RRF, k=60).
- **EmbeddingIndex**: `text-embedding-3-small` (1536 dims), numpy-based cosine similarity, persisted as `.npy` + JSON in `data/graph/`.
- **HybridSearchEngine**: Drop-in replacement for `SearchEngine`. Falls back to lexical-only when embeddings are unavailable.
- **CLI**: `python -m kb_core.search_engine "query"` uses hybrid by default, `--lexical-only` for pure TF-IDF.

### Wiki Renderer (`kb_core/wiki_renderer.py`)
- Resolves `[[wikilinks]]` to clickable HTML links for Streamlit Wikipedia-style browsing.
- Extracts table of contents from H2/H3 headings.
- Renders Wikipedia-style infoboxes, breadcrumbs, and category listings.

### Streamlit App (`app.py`)
- **Three layers**: Atlas (graph exploration), Wiki (Wikipedia-style article browser), Studio (ingestion/maintenance).
- **Wiki tab**: Search bar (hybrid search), category index (Conceptos, Autores, Fuentes, Cursos), article pages with TOC, infobox, breadcrumbs, resolved wikilinks.
- **Routing**: `st.query_params` — `?article=slug&type=concept`, `?view=category&type=author`, `?view=home`.

---

## Wiki Enrichment Status (updated 2025-04)

### Concepts — COMPLETE
- **225 concept entries** in `data/wiki/concepts/`, **0 stubs remaining**.
- All enriched with 8 mandatory sections per WIKI_RULES.md (Definición, Contexto histórico, Desarrollo teórico, Aplicaciones, Debates, Véase también, Fuentes, Notas de origen).
- REVIEW_LOG entries 1–206.

### Authors — COMPLETE
- **103 author files** in `data/wiki/authors/`:
  - **89 fully enriched articles** (8 sections per WIKI_RULES.md: Biografía intelectual, Contribuciones principales, Método y enfoque, Obras fundamentales, Influencia y legado, Críticas, Véase también, Fuentes).
  - **6 redirect pages** (abbreviated slugs → canonical: g-king→gary-king, i-lago→ignacio-lago, r-keohane→robert-keohane, s-verba→sidney-verba, peter-l-berger→peter-berger, roger-martinez→roger-martinez-sanmarti).
  - **8 short-name aliases** (pre-existing redirects: durkheim, marx, kant, etc.).
- **0 stubs remaining.**
- REVIEW_LOG entries 207–295.

### Sources, Courses, Research — pending
- Source notes exist from PDF ingestion pipeline.
- Course and research wiki pages not yet enriched.

---

## CRITICAL RULE

**NEVER edit `.canvas` files directly.** All canvas modifications MUST go through the CLI tool:

```bash
python canvas-tool.py "<file>.canvas" <command> [args]
```

Direct JSON editing of `.canvas` files is **forbidden**. The CLI tool enforces workflow rules (valid transitions, cycle detection, blocked states) so you don't have to remember them.

## Session Protocol

### 1. Start of session — read the board

```bash
python canvas-tool.py "Project.canvas" status
```

Review the board state. Run `normalize` if needed. Report ready tasks, blocked tasks, and any anomalies to the user.

### 2. Pick a task

```bash
python canvas-tool.py "Project.canvas" ready            # see what's available
python canvas-tool.py "Project.canvas" show <TASK-ID>    # read task details
python canvas-tool.py "Project.canvas" start <TASK-ID>   # begin work (red → orange)
```

If multiple tasks are ready, ask the user which to prioritize.

### 3. Work on the task

Execute the task. If you discover subtasks, propose them:

```bash
python canvas-tool.py "Project.canvas" propose Development "Subtask title" "Description" --depends-on DV-01
```

Update notes on your in-progress task:

```bash
python canvas-tool.py "Project.canvas" edit <TASK-ID> "Updated description with findings."
```

### 4. Finish the task

```bash
python canvas-tool.py "Project.canvas" finish <TASK-ID>   # orange → cyan
```

Tell the user what was done. Do NOT attempt to set the card green — only the human does that.

### 5. Repeat

After the human marks your task green, check for newly unblocked tasks:

```bash
python canvas-tool.py "Project.canvas" normalize
python canvas-tool.py "Project.canvas" ready
```

## What you CAN do

- **Read** the board: `status`, `show`, `list`, `blocked`, `blocking`, `ready`, `dump`
- **Normalize** the board: `normalize`
- **Propose** tasks: `propose` or `batch` (creates purple cards)
- **Propose** groups: `propose-group` or `batch`
- **Start** a task: `start <ID>` (red → orange)
- **Finish** a task: `finish <ID>` (orange → cyan)
- **Pause** a task: `pause <ID>` (orange → red)
- **Edit** task text: `edit <ID> "<text>"` (only orange tasks)
- **Add dependencies**: `add-dep <FROM> <TO>`

## What you CANNOT do

- Edit `.canvas` files directly
- Mark any card green (done) — human only
- Work on purple cards (proposals awaiting approval)
- Work on gray cards (blocked)
- Work on cyan cards (awaiting human review)
- Remove cards or edges
- Change green cards

## Color meanings

| Color | Meaning | Value |
|-------|---------|-------|
| Purple | Proposed by agent | `"6"` |
| Red | To Do (ready) | `"1"` |
| Orange | Doing | `"2"` |
| Cyan | Ready to review | `"5"` |
| Green | Done | `"4"` |
| Gray | Blocked | `"0"` |
