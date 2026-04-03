# Project Memory

## Core objective
Build a **wiki for the full Sociology degree** based on:
- **PDFs** as primary source material
- **Markdown files** in an **Obsidian-style** structure
- A design that can be **connected to mobile AI assistants/models**

This project is **not** just a note app and **not** just a second brain. Its purpose is to become a durable, queryable academic knowledge base for the Sociology degree.

## Canonical scope
The canonical scope of this repository is:
1. Ingest course material from PDFs.
2. Convert or reorganize knowledge into clean Markdown.
3. Preserve links, concepts, summaries, and topic pages in an Obsidian-like wiki structure.
4. Make the resulting knowledge base easy to consume by AI systems, especially on mobile workflows.
5. Cover the **entire Sociology degree**, not just isolated assignments.

## Design constraints
- Markdown should remain **portable**, readable, and repository-friendly.
- The structure should work well with **Obsidian-style navigation**.
- PDFs are source-of-truth inputs, but Markdown should be the main working format.
- The system should be designed with **future AI integrations** in mind.
- Mobile usability matters. The architecture should not assume a desktop-only workflow.

## Practical interpretation
This repo should evolve toward something like:
- `/raw/` or equivalent for source PDFs
- `/wiki/` or equivalent for normalized concept/topic notes
- `/courses/` or equivalent for subject-level organization
- `/scripts/` for ingestion, parsing, cleaning, indexing, and export helpers
- `/prompts/` or equivalent if AI-facing instructions become part of the pipeline

Exact folder names can change, but the functional separation should remain.

## Non-goals
- Not merely storing random notes without structure.
- Not optimizing only for one model or one vendor.
- Not building a generic personal productivity system unrelated to Sociology.

## Continuity note
Future work in this repository should assume:
- The user wants continuity across sessions.
- The project identity is stable: **Sociology degree wiki + PDFs + Obsidian-style Markdown + mobile AI connectivity**.
- New features should be judged by whether they strengthen that core direction.

## Current state
There is already **some implementation in this repository**. Before major restructuring, inspect existing files and align changes with what is already built.

## Working rule
When discussing this repo in future sessions, treat this document as the compact project brief unless the user explicitly changes direction.
