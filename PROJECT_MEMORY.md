# Project Memory

## Core objective
Build a **Karpathy-style LLM Knowledge Base** for the full **Sociology degree**.

The LLM owns the wiki. The cycle is: **raw data → LLM compile → wiki → query/Q&A → file answers back → enhance wiki**. Queries and explorations always "add up" into the knowledge base. The wiki grows incrementally each semester until it covers the entire degree.

This project is **not** just a note app, **not** just a second brain, and **not** just a chatbot. It is a durable, self-enhancing academic knowledge base where the LLM is the primary author and Obsidian is the primary viewer.

## Canonical scope
1. **Data ingest**: Index source documents (PDFs, articles, web clips, repos) into `data/raw/`, with Obsidian Web Clipper for web articles.
2. **LLM compile**: Incrementally compile a wiki (`data/wiki/`) — structured `.md` files with summaries, backlinks, concept articles, `[[wikilinks]]`, all authored by the LLM.
3. **Obsidian as IDE**: View raw data, compiled wiki, slides, and visualizations in Obsidian. The `data/` directory is the vault. Graph View shows the knowledge structure.
4. **Q&A over the wiki**: Ask complex questions, the LLM researches answers across the wiki (~100+ articles, ~400K+ words at scale).
5. **Filing back**: Q&A answers and explorations are filed back into the wiki as `research` articles, enriching it for further queries.
6. **Output formats**: Markdown articles, Marp slide decks, matplotlib visualizations — all viewable in Obsidian.
7. **Linting & health checks**: LLM-driven consistency checks, missing data imputation, cross-course connection discovery.
8. **Search engine**: CLI + web UI search over the wiki, usable by humans and handed off to the LLM as a tool.
9. **Semester growth**: Each semester adds courses. Concepts and authors accumulate across semesters. The goal: a complete sociology degree wiki.

## Design constraints
- **Markdown-first**: Portable, readable, repository-friendly. Obsidian `[[wikilinks]]` for internal links.
- **LLM-authored**: The wiki is the domain of the LLM. Humans rarely edit it directly.
- **No vendor lock-in**: LLM provider is configurable (OpenAI, Anthropic, or fallback).
- **Obsidian-native**: `data/` is an Obsidian vault with Graph View, Marp Slides, Dataview support.
- **Deterministic retrieval**: TF-IDF with field weights — no embeddings required at this scale.
- **Safe writes**: PR-oriented workflow for destructive edits. Branch + commit, never direct mutation.
- **Mobile-ready**: MCP server for remote AI assistant access.

## Directory model
```
data/                          ← Obsidian vault root
  raw/<semester>/<course>/     ← immutable source files
  wiki/
    sources/<semester>/<course>/*.md
    concepts/*.md
    authors/*.md
    courses/*.md
    research/*.md              ← filed Q&A answers
    slides/*.md                ← Marp slide decks
    assets/                    ← local images
    assets/viz/                ← generated charts
    INDEX.md                   ← auto-maintained master index
    GRAPH.md                   ← mermaid degree map
  qa/
    answered_questions/*.md
    open_questions/*.md
  graph/
    atlas_graph.json
    search_index.json
```

## Non-goals
- Not a generic personal productivity system unrelated to Sociology.
- Not optimizing for one model or one vendor.
- Not a Notion-first system (Notion is optional, downstream only).
- Not embedding-based RAG (yet — TF-IDF is sufficient at current scale).

## Continuity note
- The user wants continuity across sessions.
- The project identity is stable: **Sociology degree LLM wiki + Obsidian + incremental semester growth**.
- New features should strengthen the core cycle: ingest → compile → query → file back → enhance.

## Working rule
When discussing this repo in future sessions, treat this document as the compact project brief unless the user explicitly changes direction.
