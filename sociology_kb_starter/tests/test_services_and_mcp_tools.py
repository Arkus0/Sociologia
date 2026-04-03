from __future__ import annotations

from kb_core.compiler import compile_raw_document, rebuild_indexes
from kb_core.storage import save_uploaded_bytes
from kb_core import services
from kb_core import mcp_tools


def _seed_source_note() -> str:
    raw_path = save_uploaded_bytes(
        filename="durkheim.txt",
        content=b"Durkheim discusses social facts, solidarity, and division of labor.",
        semester="2026-S1",
        course="sociological-theory",
        extra_metadata={"manual_concepts": ["social facts"], "manual_authors": ["Emile Durkheim"]},
    )
    result = compile_raw_document(raw_path)
    assert result.ok
    rebuild_indexes()
    note = services.get_recent_sources(limit=1)[0]
    return note["id"]


def test_services_read_search_and_lists(kb_tmp) -> None:
    note_id = _seed_source_note()

    hits = services.search_notes("solidarity")
    assert hits

    note = services.read_note(note_id)
    assert note["frontmatter"]["note_type"] == "source"

    assert services.list_courses()
    assert services.list_authors()
    assert services.list_concepts()


def test_services_graph_and_provenance(kb_tmp) -> None:
    note_id = _seed_source_note()

    graph = services.get_graph_neighbors(node_id="sociological-theory", node_type="course", depth=1)
    assert graph["neighbors"]

    provenance = services.get_source_provenance(note_id)
    assert provenance["raw_source_path"].endswith("durkheim.txt")


def test_services_edit_patch_flow(kb_tmp) -> None:
    note_id = _seed_source_note()
    proposal = services.propose_note_edit(note_id, "Add one sentence about methodological individualism.")
    assert "Agent edit proposal" in proposal["proposed_content"]

    patch = services.build_patch_for_note(note_id, proposal["proposed_content"])
    assert "@@" in patch["patch"]


def test_mcp_tools_read_handlers(kb_tmp) -> None:
    note_id = _seed_source_note()

    assert mcp_tools.kb_search_notes("Durkheim")
    assert mcp_tools.kb_read_note(note_id)["id"] == note_id
    assert mcp_tools.kb_list_courses()
    assert mcp_tools.kb_list_authors()
    assert mcp_tools.kb_list_concepts()
    assert mcp_tools.kb_get_graph_neighbors("sociological-theory", "course", 1)["neighbors"]
    assert mcp_tools.kb_get_recent_sources(1)
    assert mcp_tools.kb_get_source_provenance(note_id)["note_id"] == note_id
    assert mcp_tools.kb_propose_note_edit(note_id, "clarify summary")["note_id"] == note_id
