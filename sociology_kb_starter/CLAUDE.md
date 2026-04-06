# Canvas Workflow — Agent Instructions

## PDF Processing Workflow (updated 2026-04-06)

### CRITICAL: No Automated Processing

- **Watcher DISABLED**: `kb_core/watcher.py` raises `RuntimeError` — NEVER re-enable it.
- **NO LLM API for wiki generation**: Groq/OpenAI/Anthropic are NOT used to generate wiki content from PDFs. The `.env` keys exist for search/embeddings only.
- **Claude processes PDFs manually**: the user drops PDFs in `data/inbox/2026-S1/`, tells Claude, and Claude reads, analyzes, and creates all wiki entries by hand.

### Manual Processing Steps

1. **Extract text**: Use `kb_core/extraction.py` (`extract_pdf()`) to get raw text from the PDF
2. **Read and analyze**: Claude reads the full extracted text, identifies concepts, authors, arguments, structure
3. **Create source note**: One per PDF module in `data/wiki/sources/{semester}/{course}/`
4. **Create/update course entry**: In `data/wiki/courses/`
5. **Create concept entries**: One per major concept in `data/wiki/concepts/`
6. **Create author entries**: One per significant author in `data/wiki/authors/`
7. **Enrich with academic sources**: Add inline citations and full bibliographic references (see WIKI_RULES.md §9)
8. **Move PDF**: From `data/inbox/` to `data/inbox/processed/`
9. **Git commit**: Stage and commit all new entries

### Why Not Automated?

The automated pipeline (compiler.py + watcher.py + Groq) produced garbage when the API failed (fallback mode) and its `rebuild_indexes()` **overwrote 310 enriched files** in April 2026. The fix:
- `rebuild_indexes()` now uses a merge strategy (preserves existing frontmatter, only updates `source_notes` and `updated_at`)
- Watcher is permanently disabled
- Claude provides richer analysis than any LLM API pipeline (concepts, relationships, debates, exam questions, full academic references)

---

## Existing Infrastructure (still used)

### PDF Extraction (`kb_core/extraction.py`)
- **OCR**: Tesseract OCR via `page.get_textpage_ocr(language="spa+eng", dpi=300)` for scanned pages.
- **Text cleaning**: `clean_extracted_text()` removes repeated headers/footers, rejoins hyphens, strips page numbers.
- Used by Claude for step 1 of manual processing.

### Search & RAG (`kb_core/search_engine.py`, `kb_core/embeddings.py`)
- **Hybrid search**: TF-IDF + OpenAI embedding vectors via RRF (k=60).
- **CLI**: `python -m kb_core.search_engine "query"`

### Wiki Renderer (`kb_core/wiki_renderer.py`)
- Resolves `[[wikilinks]]` to HTML links for Streamlit browsing.

### Streamlit App (`app.py`)
- Atlas (graph), Wiki (articles), Studio (maintenance).
- Routing: `st.query_params` — `?article=slug&type=concept`.

---

## Wiki Enrichment Status (updated 2026-04-06)

### Concepts
- **242+ concept entries** in `data/wiki/concepts/`.
- Original 225 from Intro Sociología + Metodología (enriched, REVIEW_LOG 1–206).
- **17 new** from Estructura Económica (2026-04-06): mundialización, fordismo, taylorismo, toyotismo, acumulación de capital, ciclo económico, bretton-woods, plan-marshall, deuda-externa, gran-recesión, estanflación, titulización, modelo-isi, modelo-ise, petróleo, opep, transición-demográfica, sector-tic, economía-del-conocimiento.
- All new entries enriched with inline academic citations + full bibliographic references.

### Authors
- **109+ author files** in `data/wiki/authors/`.
- Original 103 (89 enriched + 6 redirects + 8 aliases).
- **6 new** from Estructura Económica: Vidal Villa, Kondrátiev, Keynes, Lipietz, Malthus, Vilaseca Requena.

### Courses
- `introduccion-a-la-sociologia.md` — existing
- `metodologia-de-las-ciencias-sociales.md` — existing
- `estructura-economica.md` — **NEW** (2026-04-06), links 26 concepts + 8 authors

### Sources
- Estructura Económica: `la-evolucion-del-capitalismo-y-la-mundializacion.md`, `base-material-del-sistema.md`
- Plus existing source notes from Intro Sociología and Metodología.

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
