# Remote MCP Server for Sociology KB

The project includes `mcp_server.py`, a remote MCP app exposing reusable knowledge services.

## Run

```bash
cd sociology_kb_starter
python mcp_server.py
```

This launches a streamable HTTP MCP server.

## Tooling principles

- Read tools are primary and marked read-only.
- Write operations are PR-oriented (`kb_create_pr_for_note_changes`) and reviewable.
- No destructive direct-write MCP tool is exposed as the default edit workflow.

## Tool list

### Read-only tools

- `kb_search_notes(query, filters=None, limit=10)`
  - Use this when you need ranked retrieval over canonical notes.
- `kb_read_note(path_or_id)`
  - Use this when you need full note content + frontmatter.
- `kb_list_courses()`
  - Use this when you need all course notes.
- `kb_list_authors()`
  - Use this when you need all author notes.
- `kb_list_concepts()`
  - Use this when you need all concept notes.
- `kb_get_graph_neighbors(node_id, node_type, depth=1)`
  - Use this when you need nearest nodes from the derived graph.
- `kb_get_recent_sources(limit=10)`
  - Use this when you need latest compiled/updated source notes.
- `kb_get_source_provenance(note_id)`
  - Use this when you need raw evidence + sidecar provenance.
- `kb_propose_note_edit(note_id, instruction)`
  - Use this when you need a safe edit proposal before PR creation.

### Write tool (safe path)

- `kb_create_pr_for_note_changes(changes, branch_name=None, commit_message=None)`
  - Use this when you want branch + commit output suitable for GitHub PR review.

## Connect from ChatGPT custom MCP app

1. Host this service on a reachable URL (for example behind a reverse proxy).
2. Ensure dependencies are installed (`pip install -r requirements.txt`).
3. Configure ChatGPT custom app MCP endpoint to the hosted URL.
4. Verify tool discovery includes all `kb_*` tools.
5. Start with read tools; enable write tool only for trusted review workflows.

## Safety notes

- Markdown remains source of truth.
- Raw files remain immutable evidence.
- Graph JSON is regenerate-only.
- Write flow should always be branch + PR, never silent mutation on main.
