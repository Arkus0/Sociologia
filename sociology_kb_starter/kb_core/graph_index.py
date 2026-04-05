from __future__ import annotations

from collections import defaultdict
from typing import Any

from kb_core.config import SETTINGS
from kb_core.utils import list_files_recursive, load_markdown_file, slugify, utc_now_iso, wikilink, write_json, write_text


def build_graph_index() -> dict[str, Any]:
    nodes: dict[str, dict[str, Any]] = {}
    edges: set[tuple[str, str, str]] = set()

    def ensure_node(node_id: str, title: str, node_type: str, path: str | None = None) -> None:
        nodes.setdefault(node_id, {"id": node_id, "title": title, "type": node_type, "path": path})

    concept_course_map: defaultdict[str, set[str]] = defaultdict(set)
    course_author_map: defaultdict[str, set[str]] = defaultdict(set)
    concept_semester_map: defaultdict[str, set[str]] = defaultdict(set)

    for source_path in list_files_recursive(SETTINGS.sources_dir, suffixes=(".md",)):
        front, _body = load_markdown_file(source_path)
        title = str(front.get("title", source_path.stem))
        course = str(front.get("course", "general"))
        semester = str(front.get("semester", "unknown"))
        concepts = [str(x).strip() for x in front.get("concepts", []) if str(x).strip()]
        authors = [str(x).strip() for x in front.get("authors", []) if str(x).strip()]

        sid = f"source::{slugify(title)}"
        cid = f"course::{slugify(course)}"
        semid = f"semester::{slugify(semester)}"

        ensure_node(sid, title, "source", str(source_path.relative_to(SETTINGS.kb_root)))
        ensure_node(cid, course, "course")
        ensure_node(semid, semester, "semester")
        edges.add((sid, cid, "source_to_course"))
        edges.add((cid, semid, "course_to_semester"))

        for concept in concepts:
            nid = f"concept::{slugify(concept)}"
            ensure_node(nid, concept, "concept")
            edges.add((sid, nid, "source_to_concept"))
            edges.add((cid, nid, "course_to_concept"))
            concept_course_map[concept].add(course)
            concept_semester_map[concept].add(semester)

        for author in authors:
            nid = f"author::{slugify(author)}"
            ensure_node(nid, author, "author")
            edges.add((sid, nid, "source_to_author"))
            edges.add((cid, nid, "course_to_author"))
            course_author_map[course].add(author)

    # Also index research notes if they exist
    if SETTINGS.research_dir.exists():
        for research_path in list_files_recursive(SETTINGS.research_dir, suffixes=(".md",)):
            front, _body = load_markdown_file(research_path)
            title = str(front.get("title", research_path.stem))
            rid = f"research::{slugify(title)}"
            ensure_node(rid, title, "research", str(research_path.relative_to(SETTINGS.kb_root)))
            for concept in front.get("concepts", []):
                nid = f"concept::{slugify(str(concept))}"
                if nid in nodes:
                    edges.add((rid, nid, "research_to_concept"))
            for author in front.get("authors", []):
                nid = f"author::{slugify(str(author))}"
                if nid in nodes:
                    edges.add((rid, nid, "research_to_author"))

    for concept, courses in concept_course_map.items():
        if len(courses) > 1:
            ordered = sorted(courses)
            for idx, left in enumerate(ordered):
                for right in ordered[idx + 1 :]:
                    edges.add((f"course::{slugify(left)}", f"course::{slugify(right)}", "course_crosses_concept"))

    # Cross-semester concept edges
    for concept, semesters in concept_semester_map.items():
        if len(semesters) > 1:
            ordered = sorted(semesters)
            for idx, left in enumerate(ordered):
                for right in ordered[idx + 1 :]:
                    edges.add((f"semester::{slugify(left)}", f"semester::{slugify(right)}", "semester_shares_concept"))

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
    _write_mermaid_graph(nodes, edges)
    return graph


def _write_mermaid_graph(nodes: dict[str, dict], edges: set[tuple[str, str, str]]) -> None:
    """Generate a mermaid diagram viewable in Obsidian."""
    lines = [
        "# Knowledge Graph",
        "",
        f"*Auto-generated: {utc_now_iso()}*",
        "",
        "```mermaid",
        "graph LR",
    ]

    # Add semester and course nodes for a readable top-level view
    semester_nodes = {nid: n for nid, n in nodes.items() if n["type"] == "semester"}
    course_nodes = {nid: n for nid, n in nodes.items() if n["type"] == "course"}
    concept_nodes = {nid: n for nid, n in nodes.items() if n["type"] == "concept"}

    for nid, n in semester_nodes.items():
        safe_id = nid.replace("::", "_")
        lines.append(f"    {safe_id}[{n['title']}]")

    for nid, n in course_nodes.items():
        safe_id = nid.replace("::", "_")
        lines.append(f"    {safe_id}({n['title']})")

    # Only show concepts that cross courses (to keep diagram readable)
    cross_concepts = set()
    concept_courses: defaultdict[str, set[str]] = defaultdict(set)
    for s, t, r in edges:
        if r == "course_to_concept":
            concept_courses[t].add(s)
    for cid, courses in concept_courses.items():
        if len(courses) > 1 and cid in concept_nodes:
            cross_concepts.add(cid)
            safe_id = cid.replace("::", "_")
            lines.append(f"    {safe_id}{{{{{concept_nodes[cid]['title']}}}}}")

    for s, t, r in sorted(edges):
        safe_s = s.replace("::", "_")
        safe_t = t.replace("::", "_")
        if r == "course_to_semester" and s in course_nodes and t in semester_nodes:
            lines.append(f"    {safe_t} --> {safe_s}")
        elif r == "course_to_concept" and t in cross_concepts:
            lines.append(f"    {safe_s} -.-> {safe_t}")

    lines.append("```")
    content = "\n".join(lines)
    graph_md_path = SETTINGS.wiki_dir / "GRAPH.md"
    graph_md_path.parent.mkdir(parents=True, exist_ok=True)
    write_text(graph_md_path, content)
