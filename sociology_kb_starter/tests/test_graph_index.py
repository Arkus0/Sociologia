from __future__ import annotations

from kb_core.compiler import compile_raw_document, rebuild_indexes
from kb_core.graph_index import build_graph_index
from kb_core.storage import save_uploaded_bytes


def test_graph_index_generation_basics(kb_tmp) -> None:
    raw_path = save_uploaded_bytes(
        filename="weber.txt",
        content=b"Max Weber discusses authority, legitimacy and bureaucracy.",
        semester="2026-S1",
        course="sociological-theory",
        extra_metadata={"manual_concepts": ["authority"], "manual_authors": ["Max Weber"]},
    )
    compile_raw_document(raw_path)
    rebuild_indexes()

    graph = build_graph_index()
    assert graph["stats"]["node_count"] > 0
    assert graph["stats"]["edge_count"] > 0
    assert any(node["type"] == "source" for node in graph["nodes"])
    assert any(edge["type"] == "source_to_concept" for edge in graph["edges"])
