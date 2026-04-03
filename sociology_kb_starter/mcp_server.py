from __future__ import annotations

from kb_core import mcp_tools

try:
    from mcp.server.fastmcp import FastMCP
except Exception as exc:  # pragma: no cover
    raise RuntimeError(
        "The 'mcp' package is required to run the MCP server. Install dependencies first."
    ) from exc


mcp = FastMCP("sociology-kb")


@mcp.tool(name="kb_search_notes", read_only=True)
def tool_search_notes(query: str, filters: dict | None = None, limit: int = 10) -> list[dict]:
    """Use this when you need ranked retrieval over sociology markdown notes."""
    return mcp_tools.kb_search_notes(query=query, filters=filters, limit=limit)


@mcp.tool(name="kb_read_note", read_only=True)
def tool_read_note(path_or_id: str) -> dict:
    """Use this when you need full note content and frontmatter."""
    return mcp_tools.kb_read_note(path_or_id=path_or_id)


@mcp.tool(name="kb_list_courses", read_only=True)
def tool_list_courses() -> list[dict]:
    """Use this when you need all course notes."""
    return mcp_tools.kb_list_courses()


@mcp.tool(name="kb_list_authors", read_only=True)
def tool_list_authors() -> list[dict]:
    """Use this when you need all author notes."""
    return mcp_tools.kb_list_authors()


@mcp.tool(name="kb_list_concepts", read_only=True)
def tool_list_concepts() -> list[dict]:
    """Use this when you need all concept notes."""
    return mcp_tools.kb_list_concepts()


@mcp.tool(name="kb_get_graph_neighbors", read_only=True)
def tool_get_graph_neighbors(node_id: str, node_type: str, depth: int = 1) -> dict:
    """Use this when you need graph neighbors for an entity."""
    return mcp_tools.kb_get_graph_neighbors(node_id=node_id, node_type=node_type, depth=depth)


@mcp.tool(name="kb_get_recent_sources", read_only=True)
def tool_get_recent_sources(limit: int = 10) -> list[dict]:
    """Use this when you need newest source notes by compiled/updated timestamp."""
    return mcp_tools.kb_get_recent_sources(limit=limit)


@mcp.tool(name="kb_get_source_provenance", read_only=True)
def tool_get_source_provenance(note_id: str) -> dict:
    """Use this when you need raw evidence provenance for a source note."""
    return mcp_tools.kb_get_source_provenance(note_id=note_id)


@mcp.tool(name="kb_propose_note_edit", read_only=True)
def tool_propose_note_edit(note_id: str, instruction: str) -> dict:
    """Use this when you want a safe edit proposal before changing files."""
    return mcp_tools.kb_propose_note_edit(note_id=note_id, instruction=instruction)


@mcp.tool(name="kb_create_pr_for_note_changes", read_only=False)
def tool_create_pr_for_note_changes(changes: list[dict], branch_name: str | None = None, commit_message: str | None = None) -> dict:
    """Use this when you want PR-oriented note edits through a dedicated branch commit."""
    return mcp_tools.kb_create_pr_for_note_changes(
        changes=changes,
        branch_name=branch_name,
        commit_message=commit_message,
    )


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
