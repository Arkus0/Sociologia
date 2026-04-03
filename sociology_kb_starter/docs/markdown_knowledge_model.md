# Markdown Knowledge Model (Canonical Layer)

This repository is **markdown-first**:

- PDFs/TXT/MD uploads in `data/raw/` are raw evidence only.
- Canonical knowledge lives in markdown notes under `data/wiki/`.
- Graph artifacts in `data/graph/` are derived from markdown, never edited directly.

## Stable note structure

```
data/wiki/
  sources/<semester>/<course>/*.md
  concepts/*.md
  authors/*.md
  courses/*.md
```

## Frontmatter schema (explicit)

### Source note

Required keys:
- `id` (string)
- `title` (string)
- `note_type: source`
- `semester` (string)
- `course` (string)
- `source_path` (string, path under `data/raw`)
- `compiled_at` (ISO timestamp)
- `concepts` (string list)
- `authors` (string list)

Optional keys:
- `methods` (string list)
- `tags` (string list)
- `reviewed` (bool)
- `llm_provider` (string)
- `llm_model` (string)

### Entity notes (`concept`, `author`, `course`)

Required keys:
- `id`
- `title`
- `note_type`
- `updated_at`

Optional keys:
- `source_notes` (for concept/author)

## Deterministic retrieval contract

`kb_core.services.search_notes` and QA retrieval use deterministic lexical ranking (weighted fields + normalization) so external agents get repeatable results without requiring embeddings.
