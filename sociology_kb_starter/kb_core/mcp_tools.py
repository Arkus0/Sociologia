from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field

from kb_core import services


class SearchNotesInput(BaseModel):
    query: str = Field(description="Free text query for sociology markdown notes.")
    filters: dict[str, Any] | None = Field(default=None, description="Optional frontmatter/body filters.")
    limit: int = Field(default=10, ge=1, le=50)


class ReadNoteInput(BaseModel):
    path_or_id: str = Field(description="Relative markdown path or note id.")


class ListNotesInput(BaseModel):
    note_type: str = Field(description="One of source, concept, author, course.")
    filters: dict[str, Any] | None = None


class GraphNeighborsInput(BaseModel):
    node_id: str
    node_type: str = Field(description="source, concept, author, or course")
    depth: int = Field(default=1, ge=1, le=3)


class RecentSourcesInput(BaseModel):
    limit: int = Field(default=10, ge=1, le=50)


class SourceProvenanceInput(BaseModel):
    note_id: str


class ProposeNoteEditInput(BaseModel):
    note_id: str
    instruction: str


class BuildPatchInput(BaseModel):
    note_id: str
    new_content: str


def kb_search_notes(query: str, filters: dict[str, Any] | None = None, limit: int = 10) -> list[dict]:
    """Use this when you need ranked retrieval over canonical markdown notes."""
    return services.search_notes(query, filters=filters, limit=limit)


def kb_read_note(path_or_id: str) -> dict:
    """Use this when you need the full content and frontmatter of a specific note."""
    return services.read_note(path_or_id)


def kb_list_courses() -> list[dict]:
    """Use this when you need the available course nodes."""
    return services.list_courses()


def kb_list_authors() -> list[dict]:
    """Use this when you need the available author nodes."""
    return services.list_authors()


def kb_list_concepts() -> list[dict]:
    """Use this when you need the available concept nodes."""
    return services.list_concepts()


def kb_get_graph_neighbors(node_id: str, node_type: str, depth: int = 1) -> dict:
    """Use this when you need neighborhood traversal from the derived graph artifact."""
    return services.get_graph_neighbors(node_id=node_id, node_type=node_type, depth=depth)


def kb_get_recent_sources(limit: int = 10) -> list[dict]:
    """Use this when you need the most recently compiled source notes."""
    return services.get_recent_sources(limit=limit)


def kb_get_source_provenance(note_id: str) -> dict:
    """Use this when you need evidence provenance from source note to raw document metadata."""
    return services.get_source_provenance(note_id)


def kb_propose_note_edit(note_id: str, instruction: str) -> dict:
    """Use this when you want an editable proposal before creating a PR patch."""
    return services.propose_note_edit(note_id, instruction)


def kb_create_pr_for_note_changes(changes: list[dict], branch_name: str | None = None, commit_message: str | None = None) -> dict:
    """Use this when you need to commit note edits on a branch for GitHub PR review."""
    return services.create_branch_and_pr_for_changes(changes, branch_name=branch_name, commit_message=commit_message)
