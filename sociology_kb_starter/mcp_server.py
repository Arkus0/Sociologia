from __future__ import annotations

from kb_core import mcp_tools

try:
    from mcp.server.fastmcp import FastMCP
except Exception as exc:  # pragma: no cover
    raise RuntimeError(
        "The 'mcp' package is required to run the MCP server. Install dependencies first."
    ) from exc


mcp = FastMCP("sociology-kb")


@mcp.tool(name="kb_search_notes")
def tool_search_notes(query: str, filters: dict | None = None, limit: int = 10) -> list[dict]:
    """Use this when you need ranked retrieval over sociology markdown notes."""
    return mcp_tools.kb_search_notes(query=query, filters=filters, limit=limit)


@mcp.tool(name="kb_read_note")
def tool_read_note(path_or_id: str) -> dict:
    """Use this when you need full note content and frontmatter."""
    return mcp_tools.kb_read_note(path_or_id=path_or_id)


@mcp.tool(name="kb_list_courses")
def tool_list_courses() -> list[dict]:
    """Use this when you need all course notes."""
    return mcp_tools.kb_list_courses()


@mcp.tool(name="kb_list_authors")
def tool_list_authors() -> list[dict]:
    """Use this when you need all author notes."""
    return mcp_tools.kb_list_authors()


@mcp.tool(name="kb_list_concepts")
def tool_list_concepts() -> list[dict]:
    """Use this when you need all concept notes."""
    return mcp_tools.kb_list_concepts()


@mcp.tool(name="kb_get_graph_neighbors")
def tool_get_graph_neighbors(node_id: str, node_type: str, depth: int = 1) -> dict:
    """Use this when you need graph neighbors for an entity."""
    return mcp_tools.kb_get_graph_neighbors(node_id=node_id, node_type=node_type, depth=depth)


@mcp.tool(name="kb_get_recent_sources")
def tool_get_recent_sources(limit: int = 10) -> list[dict]:
    """Use this when you need newest source notes by compiled/updated timestamp."""
    return mcp_tools.kb_get_recent_sources(limit=limit)


@mcp.tool(name="kb_get_source_provenance")
def tool_get_source_provenance(note_id: str) -> dict:
    """Use this when you need raw evidence provenance for a source note."""
    return mcp_tools.kb_get_source_provenance(note_id=note_id)


@mcp.tool(name="kb_propose_note_edit")
def tool_propose_note_edit(note_id: str, instruction: str) -> dict:
    """Use this when you want a safe edit proposal before changing files."""
    return mcp_tools.kb_propose_note_edit(note_id=note_id, instruction=instruction)


@mcp.tool(name="kb_create_pr_for_note_changes")
def tool_create_pr_for_note_changes(changes: list[dict], branch_name: str | None = None, commit_message: str | None = None) -> dict:
    """Use this when you want PR-oriented note edits through a dedicated branch commit."""
    return mcp_tools.kb_create_pr_for_note_changes(
        changes=changes,
        branch_name=branch_name,
        commit_message=commit_message,
    )


@mcp.tool(name="kb_file_answer")
def tool_file_answer(query: str, answer: str, concepts: list[str] | None = None, authors: list[str] | None = None) -> dict:
    """Use this when you want to file a Q&A answer back into the wiki as a research note."""
    return mcp_tools.kb_file_answer(query=query, answer=answer, concepts=concepts, authors=authors)


@mcp.tool(name="kb_generate_slides")
def tool_generate_slides(topic_or_query: str, output_name: str | None = None) -> dict:
    """Use this when you want to generate a Marp slide deck from wiki content."""
    return mcp_tools.kb_generate_slides(topic_or_query=topic_or_query, output_name=output_name)


@mcp.tool(name="kb_generate_viz")
def tool_generate_viz(viz_type: str, data: dict) -> dict:
    """Use this when you want to generate a visualization (concept_map, timeline, or statistics)."""
    return mcp_tools.kb_generate_viz(viz_type=viz_type, data=data)


@mcp.tool(name="kb_get_semester_stats")
def tool_get_semester_stats(semester_id: str) -> dict:
    """Use this when you need statistics for a specific semester."""
    return mcp_tools.kb_get_semester_stats(semester_id=semester_id)


@mcp.tool(name="kb_suggest_articles")
def tool_suggest_articles() -> list[dict]:
    """Use this when you want cross-course topic suggestions for new wiki articles."""
    return mcp_tools.kb_suggest_articles()


@mcp.tool(name="kb_ingest_from_inbox")
def tool_ingest_from_inbox() -> dict:
    """Use this when you want to scan the inbox folder and ingest any new documents found there."""
    return mcp_tools.kb_ingest_from_inbox()


@mcp.tool(name="kb_rebuild_embeddings")
def tool_rebuild_embeddings() -> dict:
    """Use this when you want to rebuild the semantic embedding index for improved search quality."""
    return mcp_tools.kb_rebuild_embeddings()


if __name__ == "__main__":
    import sys

    if "--stdio" in sys.argv:
        mcp.run(transport="stdio")
    else:
        mcp.run(transport="streamable-http")
