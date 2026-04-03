from __future__ import annotations

from collections import defaultdict
from typing import Any

from kb_core.config import SETTINGS
from kb_core.utils import list_files_recursive, load_markdown_file, slugify, write_json


def build_graph_index() -> dict[str, Any]:
    nodes: dict[str, dict[str, Any]] = {}
    edges: set[tuple[str, str, str]] = set()

    def ensure_node(node_id: str, title: str, node_type: str, path: str | None = None) -> None:
        nodes.setdefault(node_id, {"id": node_id, "title": title, "type": node_type, "path": path})

    concept_course_map: defaultdict[str, set[str]] = defaultdict(set)
    course_author_map: defaultdict[str, set[str]] = defaultdict(set)

    for source_path in list_files_recursive(SETTINGS.sources_dir, suffixes=(".md",)):
        front, _body = load_markdown_file(source_path)
        title = str(front.get("title", source_path.stem))
        course = str(front.get("course", "general"))
        concepts = [str(x).strip() for x in front.get("concepts", []) if str(x).strip()]
        authors = [str(x).strip() for x in front.get("authors", []) if str(x).strip()]

        sid = f"source::{slugify(title)}"
        cid = f"course::{slugify(course)}"

        ensure_node(sid, title, "source", str(source_path.relative_to(SETTINGS.kb_root)))
        ensure_node(cid, course, "course")
        edges.add((sid, cid, "source_to_course"))

        for concept in concepts:
            nid = f"concept::{slugify(concept)}"
            ensure_node(nid, concept, "concept")
            edges.add((sid, nid, "source_to_concept"))
            edges.add((cid, nid, "course_to_concept"))
            concept_course_map[concept].add(course)

        for author in authors:
            nid = f"author::{slugify(author)}"
            ensure_node(nid, author, "author")
            edges.add((sid, nid, "source_to_author"))
            edges.add((cid, nid, "course_to_author"))
            course_author_map[course].add(author)

    for concept, courses in concept_course_map.items():
        if len(courses) > 1:
            ordered = sorted(courses)
            for idx, left in enumerate(ordered):
                for right in ordered[idx + 1 :]:
                    edges.add((f"course::{slugify(left)}", f"course::{slugify(right)}", "course_crosses_concept"))

    graph = {
        "nodes": sorted(nodes.values(), key=lambda n: (n["type"], n["title"].lower())),
        "edges": [
            {"source": s, "target": t, "type": r}
            for s, t, r in sorted(edges)
        ],
        "stats": {
            "node_count": len(nodes),
            "edge_count": len(edges),
        },
    }
    write_json(SETTINGS.graph_dir / "atlas_graph.json", graph)
    return graph
