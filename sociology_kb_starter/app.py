from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
import textwrap

import pandas as pd
import streamlit as st

from kb_core.compiler import compile_all_raw_documents, compile_raw_document, rebuild_indexes
from kb_core.config import SETTINGS
from kb_core.lint import run_lint_checks
from kb_core.notion_sync import notion_is_configured, push_note_to_notion
from kb_core.qa import answer_question
from kb_core.storage import ensure_project_dirs, list_raw_documents, mark_compile_pending, save_uploaded_bytes
from kb_core.utils import list_files_recursive, load_markdown_file, slugify


try:
    from streamlit_agraph import Config as AGraphConfig
    from streamlit_agraph import Edge, Node, agraph

    AGRAPH_AVAILABLE = True
except Exception:
    AGRAPH_AVAILABLE = False


st.set_page_config(page_title="Sociology Atlas", layout="wide")
ensure_project_dirs()


TYPE_COLORS = {
    "source": "#4E79A7",
    "concept": "#59A14F",
    "author": "#F28E2B",
    "course": "#E15759",
    "question": "#B07AA1",
    "synthesis": "#76B7B2",
    "method": "#EDC949",
}


@dataclass
class AtlasNode:
    node_id: str
    title: str
    node_type: str
    summary: str
    linked: dict[str, list[str]]
    source_backlinks: list[str]
    related_notes: list[str]


@st.cache_data(show_spinner=False)
def _stats() -> dict[str, int]:
    raw_docs = list_raw_documents()
    course_notes = list_files_recursive(SETTINGS.by_course_dir, suffixes=(".md",))
    concept_notes = list_files_recursive(SETTINGS.by_concept_dir, suffixes=(".md",))
    author_notes = list_files_recursive(SETTINGS.by_author_dir, suffixes=(".md",))
    answered = list_files_recursive(SETTINGS.answered_questions_dir, suffixes=(".md",))
    return {
        "raw_docs": len(raw_docs),
        "course_notes": len(course_notes),
        "concept_notes": len(concept_notes),
        "author_notes": len(author_notes),
        "answered": len(answered),
    }


@st.cache_data(show_spinner=False)
def _raw_docs_table() -> pd.DataFrame:
    rows = []
    for item in list_raw_documents():
        meta = item["metadata"]
        rows.append(
            {
                "path": str(item["path"].relative_to(SETTINGS.kb_root)),
                "semester": meta.get("semester", ""),
                "course": meta.get("course", ""),
                "status": meta.get("status", ""),
                "attempts": meta.get("compile_attempts", 0),
                "error": meta.get("last_error_message", "") or "",
            }
        )
    return pd.DataFrame(rows)


def _extract_section(body: str, start_marker: str, end_marker: str) -> str:
    if start_marker not in body:
        return ""
    section = body.split(start_marker, 1)[1]
    if end_marker in section:
        section = section.split(end_marker, 1)[0]
    return section.strip()


@st.cache_data(show_spinner=False)
def _load_source_notes() -> list[dict]:
    notes: list[dict] = []
    for path in list_files_recursive(SETTINGS.by_course_dir, suffixes=(".md",)):
        frontmatter, body = load_markdown_file(path)
        notes.append({"path": path, "frontmatter": frontmatter, "body": body})
    return notes


@st.cache_data(show_spinner=False)
def _load_entity_notes(base_dir) -> list[dict]:
    notes: list[dict] = []
    for path in list_files_recursive(base_dir, suffixes=(".md",)):
        frontmatter, body = load_markdown_file(path)
        notes.append({"path": path, "frontmatter": frontmatter, "body": body})
    return notes


@st.cache_data(show_spinner=False)
def _build_graph_payload() -> dict:
    source_notes = _load_source_notes()
    concept_notes = _load_entity_notes(SETTINGS.by_concept_dir)
    author_notes = _load_entity_notes(SETTINGS.by_author_dir)

    nodes: dict[str, AtlasNode] = {}
    edges: set[tuple[str, str, str]] = set()
    concept_to_courses: defaultdict[str, set[str]] = defaultdict(set)
    course_counts: Counter[str] = Counter()

    def add_node(node_id: str, title: str, node_type: str, summary: str = "") -> None:
        if node_id in nodes:
            return
        nodes[node_id] = AtlasNode(
            node_id=node_id,
            title=title,
            node_type=node_type,
            summary=summary,
            linked=defaultdict(list),
            source_backlinks=[],
            related_notes=[],
        )

    def add_edge(src: str, dst: str, relation: str) -> None:
        if src == dst:
            return
        edges.add((src, dst, relation))

    for note in source_notes:
        front = note["frontmatter"]
        body = note["body"]
        title = front.get("title", note["path"].stem)
        summary = _extract_section(body, "## Summary", "## Core ideas") or "Source note in the sociology atlas."
        course = str(front.get("course", "general")).strip() or "general"
        concepts = [str(value).strip() for value in front.get("concepts", []) if str(value).strip()]
        authors = [str(value).strip() for value in front.get("authors", []) if str(value).strip()]

        source_id = f"source::{slugify(title)}"
        course_id = f"course::{slugify(course)}"

        add_node(source_id, title, "source", summary)
        add_node(course_id, course, "course", f"Course node connected to {title} and related sociology concepts.")

        nodes[source_id].linked["course"].append(course)
        nodes[source_id].related_notes.append(str(note["path"].relative_to(SETTINGS.kb_root)))

        nodes[course_id].source_backlinks.append(title)
        course_counts[course] += 1

        add_edge(source_id, course_id, "source_to_course")

        concept_ids: list[tuple[str, str]] = []
        author_ids: list[tuple[str, str]] = []

        for concept in concepts:
            concept_id = f"concept::{slugify(concept)}"
            concept_ids.append((concept_id, concept))
            add_node(concept_id, concept, "concept", f"Sociology concept referenced in {course} materials.")
            nodes[source_id].linked["concept"].append(concept)
            nodes[concept_id].source_backlinks.append(title)
            nodes[course_id].linked["concept"].append(concept)
            concept_to_courses[concept].add(course)
            add_edge(source_id, concept_id, "source_to_concept")
            add_edge(course_id, concept_id, "course_to_concept")

        for author in authors:
            author_id = f"author::{slugify(author)}"
            author_ids.append((author_id, author))
            add_node(author_id, author, "author", f"Sociological author connected across multiple notes.")
            nodes[source_id].linked["author"].append(author)
            nodes[author_id].source_backlinks.append(title)
            nodes[course_id].linked["author"].append(author)
            add_edge(source_id, author_id, "source_to_author")
            add_edge(course_id, author_id, "course_to_author")

        for concept_id, _ in concept_ids:
            for other_id, _ in concept_ids:
                if concept_id != other_id:
                    add_edge(concept_id, other_id, "concept_to_concept")

        for author_id, _ in author_ids:
            for concept_id, _ in concept_ids:
                add_edge(author_id, concept_id, "author_to_concept")

    for note in concept_notes:
        front = note["frontmatter"]
        title = front.get("title", note["path"].stem)
        node_id = f"concept::{slugify(title)}"
        add_node(node_id, title, "concept", _extract_section(note["body"], "## Definition", "## Why it matters") or nodes.get(node_id, AtlasNode("", "", "", "", defaultdict(list), [], [])).summary)
        for src in front.get("source_notes", []):
            nodes[node_id].related_notes.append(str(src))

    for note in author_notes:
        front = note["frontmatter"]
        title = front.get("title", note["path"].stem)
        node_id = f"author::{slugify(title)}"
        add_node(node_id, title, "author", _extract_section(note["body"], "## Core ideas", "## Related concepts") or nodes.get(node_id, AtlasNode("", "", "", "", defaultdict(list), [], [])).summary)
        for src in front.get("source_notes", []):
            nodes[node_id].related_notes.append(str(src))

    cross_course_rows = []
    for concept, courses in sorted(concept_to_courses.items()):
        if len(courses) > 1:
            cross_course_rows.append({"concept": concept, "courses": ", ".join(sorted(courses)), "course_count": len(courses)})

    recent_rows = []
    for note in source_notes:
        front = note["frontmatter"]
        recent_rows.append(
            {
                "title": front.get("title", note["path"].stem),
                "course": front.get("course", "general"),
                "compiled_at": front.get("compiled_at", ""),
                "path": str(note["path"].relative_to(SETTINGS.kb_root)),
            }
        )
    recent_rows = sorted(recent_rows, key=lambda row: row["compiled_at"], reverse=True)

    return {
        "nodes": nodes,
        "edges": sorted(edges),
        "cross_course": cross_course_rows,
        "recent": recent_rows,
        "course_counts": dict(course_counts),
    }


def _render_graph(payload: dict, allowed_types: list[str], allowed_courses: list[str], search: str) -> str | None:
    nodes: dict[str, AtlasNode] = payload["nodes"]
    edges: list[tuple[str, str, str]] = payload["edges"]

    lowered_search = search.strip().lower()
    filtered_ids: set[str] = set()
    for node_id, node in nodes.items():
        if node.node_type not in allowed_types:
            continue
        if lowered_search and lowered_search not in node.title.lower():
            continue
        if node.node_type == "course" and allowed_courses and node.title not in allowed_courses:
            continue
        filtered_ids.add(node_id)

    if allowed_courses:
        for src, dst, relation in edges:
            if relation == "source_to_course" and dst in nodes and nodes[dst].title in allowed_courses:
                filtered_ids.add(src)

    graph_edges: list[Edge] = []
    for src, dst, relation in edges:
        if src in filtered_ids and dst in filtered_ids:
            graph_edges.append(Edge(source=src, target=dst, label=relation.replace("_", " "), color="#9AA0A6"))

    graph_nodes: list[Node] = []
    for node_id in filtered_ids:
        node = nodes[node_id]
        graph_nodes.append(
            Node(
                id=node_id,
                label=node.title,
                title=f"{node.node_type.title()} • {node.title}",
                color=TYPE_COLORS.get(node.node_type, "#777777"),
                size=30 if node.node_type in {"concept", "course"} else 20,
            )
        )

    if not graph_nodes:
        st.info("No nodes for the current filters.")
        return None

    if AGRAPH_AVAILABLE:
        config = AGraphConfig(width="100%", height=650, directed=True, physics=True, hierarchical=False, nodeHighlightBehavior=True)
        return agraph(nodes=graph_nodes, edges=graph_edges, config=config)

    st.warning("Install `streamlit-agraph` for clickable graph interactions. Showing fallback network table.")
    st.dataframe(
        pd.DataFrame(
            {
                "node": [node.title for node in (nodes[node_id] for node_id in filtered_ids)],
                "type": [node.node_type for node in (nodes[node_id] for node_id in filtered_ids)],
            }
        ),
        use_container_width=True,
    )
    return None


def _render_node_details(payload: dict, selected_node_id: str | None) -> None:
    nodes: dict[str, AtlasNode] = payload["nodes"]
    if not selected_node_id or selected_node_id not in nodes:
        st.info("Select or click a node to inspect links, backlinks, and context.")
        return

    node = nodes[selected_node_id]
    st.markdown(f"### {node.title}")
    st.caption(f"Type: `{node.node_type}`")
    st.write(node.summary or "No summary available yet.")

    linked = {key: sorted(set(values)) for key, values in node.linked.items() if values}
    if linked:
        st.markdown("**Linked concepts/authors/courses**")
        for key, values in linked.items():
            st.markdown(f"- **{key.title()}**: {', '.join(values)}")

    backlinks = sorted(set(node.source_backlinks))
    if backlinks:
        st.markdown("**Source backlinks**")
        for value in backlinks[:15]:
            st.markdown(f"- {value}")

    related_notes = sorted(set(node.related_notes))
    if related_notes:
        st.markdown("**Related notes**")
        for note in related_notes[:15]:
            st.code(note)


def _clear_caches() -> None:
    _stats.clear()
    _raw_docs_table.clear()
    _load_source_notes.clear()
    _load_entity_notes.clear()
    _build_graph_payload.clear()


st.title("Sociology Atlas")
st.caption("A graph-first knowledge map for connecting sources, concepts, authors, and courses.")

with st.sidebar:
    st.subheader("Navigation")
    layer = st.radio("Workspace", ["Atlas", "Studio"], index=0)
    st.caption("Atlas is for study and synthesis. Studio keeps ingestion and maintenance tools out of the way.")

    st.divider()
    st.subheader("System")
    st.write(f"KB root: `{SETTINGS.kb_root}`")
    st.write(f"LLM provider: `{SETTINGS.llm_provider or 'none'}`")
    st.write(f"Notion configured: `{notion_is_configured()}`")

stats = _stats()

if layer == "Atlas":
    payload = _build_graph_payload()
    nodes: dict[str, AtlasNode] = payload["nodes"]
    all_courses = sorted([node.title for node in nodes.values() if node.node_type == "course"])

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Knowledge nodes", len(nodes))
    c2.metric("Connections", len(payload["edges"]))
    c3.metric("Cross-course concepts", len(payload["cross_course"]))
    c4.metric("Source notes", stats["course_notes"])

    st.markdown("#### Knowledge map")
    f1, f2, f3 = st.columns([2, 2, 3])
    with f1:
        allowed_types = st.multiselect("Node types", ["source", "concept", "author", "course"], default=["source", "concept", "author", "course"])
    with f2:
        allowed_courses = st.multiselect("Courses", all_courses, default=all_courses[:6]) if all_courses else []
    with f3:
        search = st.text_input("Search nodes", placeholder="e.g., Durkheim, social integration, methodology")

    graph_col, detail_col = st.columns([2.1, 1.1])
    with graph_col:
        selected_node_id = _render_graph(payload, allowed_types, allowed_courses, search)
    with detail_col:
        options = {node.title: node.node_id for node in nodes.values() if node.node_type in allowed_types}
        fallback_title = st.selectbox("Node detail", ["(none)"] + sorted(options.keys()))
        if fallback_title != "(none)" and not selected_node_id:
            selected_node_id = options[fallback_title]
        _render_node_details(payload, selected_node_id)

    bottom_left, bottom_right = st.columns(2)
    with bottom_left:
        st.markdown("#### Cross-course synthesis")
        if payload["cross_course"]:
            st.dataframe(pd.DataFrame(payload["cross_course"]), use_container_width=True)
        else:
            st.info("Cross-course links will appear as you compile more material from multiple subjects.")
    with bottom_right:
        st.markdown("#### Recent additions")
        if payload["recent"]:
            st.dataframe(pd.DataFrame(payload["recent"][:12]), use_container_width=True)
        else:
            st.info("No compiled source notes yet.")

    with st.expander("Why this layout changed"):
        st.markdown(
            textwrap.dedent(
                """
                - The previous UI centered on operational tabs (ingest, compile, lint, export) and made the app feel like an admin console.
                - This atlas starts with the sociology graph so exploration is the default behavior.
                - Operations still exist, but live in the **Studio** layer as supporting tools.
                - Node details and synthesis surfaces make cross-course understanding visible, not hidden in folders.
                """
            )
        )

else:
    st.markdown("### Studio (secondary operations)")
    st.caption("Ingestion, compilation, quality checks, and export are still available here, but they no longer define the product identity.")

    studio_mode = st.segmented_control("Studio section", ["Ingest", "Compile", "Quality", "Ask", "Notion"], default="Ingest")

    if studio_mode == "Ingest":
        st.subheader("Ingest raw sources")
        with st.form("upload_form"):
            semester = st.text_input("Semester (optional)", value="2026-S1")
            course = st.text_input("Course (optional)", value="general")
            compile_now = st.checkbox("Compile immediately after save", value=False)

            with st.expander("Optional enrichments"):
                manual_concepts = st.text_input("Manual concepts (comma separated)")
                manual_authors = st.text_input("Manual authors (comma separated)")

            uploaded_files = st.file_uploader("Files", type=["pdf", "md", "txt"], accept_multiple_files=True)
            submitted = st.form_submit_button("Save files")

        if submitted:
            if not uploaded_files:
                st.warning("Upload at least one file.")
            else:
                concepts = [item.strip() for item in manual_concepts.split(",") if item.strip()]
                authors = [item.strip() for item in manual_authors.split(",") if item.strip()]
                saved_paths = []
                for uploaded in uploaded_files:
                    saved = save_uploaded_bytes(
                        filename=uploaded.name,
                        content=uploaded.read(),
                        semester=semester.strip() or None,
                        course=course.strip() or None,
                        extra_metadata={"manual_concepts": concepts, "manual_authors": authors},
                    )
                    mark_compile_pending(saved)
                    saved_paths.append(saved)

                compile_results = []
                if compile_now:
                    for path in saved_paths:
                        compile_results.append(compile_raw_document(path))
                    rebuild_indexes()

                _clear_caches()
                st.success(f"Saved {len(saved_paths)} file(s).")
                if compile_results:
                    ok_count = sum(1 for result in compile_results if result.ok)
                    st.info(f"Compiled {ok_count}/{len(compile_results)} files.")

    elif studio_mode == "Compile":
        st.subheader("Compile and index")
        raw_docs = list_raw_documents()
        if not raw_docs:
            st.info("Nothing to compile yet.")
        else:
            options = {str(item["path"].relative_to(SETTINGS.kb_root)): item for item in raw_docs}
            selected = st.multiselect("Select raw files", list(options.keys()), default=list(options.keys())[:10])
            col_a, col_b, col_c = st.columns([1, 1, 1])
            with col_a:
                if st.button("Compile selected"):
                    results = [compile_raw_document(options[key]["path"]) for key in selected]
                    rebuild_indexes()
                    _clear_caches()
                    ok_count = sum(1 for result in results if result.ok)
                    st.success(f"Compiled {ok_count}/{len(results)} selected file(s).")
            with col_b:
                if st.button("Compile everything"):
                    results = compile_all_raw_documents()
                    _clear_caches()
                    ok_count = sum(1 for result in results if result.ok)
                    st.success(f"Compiled {ok_count}/{len(results)} files.")
            with col_c:
                if st.button("Rebuild indexes"):
                    rebuild_indexes()
                    _clear_caches()
                    st.success("Concept and author indexes rebuilt.")

            st.markdown("#### Raw status overview")
            st.dataframe(_raw_docs_table(), use_container_width=True)

    elif studio_mode == "Quality":
        st.subheader("Processing and lint health")
        issues = run_lint_checks()
        if issues:
            st.dataframe(pd.DataFrame(issues), use_container_width=True)
        else:
            st.success("No issues detected.")

    elif studio_mode == "Ask":
        st.subheader("Ask the knowledge base")
        query = st.text_area("Question", value="How is Durkheim related to anomie and social integration?")
        if st.button("Answer question"):
            result = answer_question(query)
            st.markdown(result["answer"])
            retrieved_rows = []
            for item in result["retrieved"]:
                retrieved_rows.append(
                    {
                        "path": str(item["path"].relative_to(SETTINGS.kb_root)),
                        "title": item["frontmatter"].get("title", item["path"].stem),
                        "score": item["score"],
                        "course": item["frontmatter"].get("course", ""),
                    }
                )
            if retrieved_rows:
                st.dataframe(pd.DataFrame(retrieved_rows), use_container_width=True)
            st.caption(f"Provider: {result['provider']} | Model: {result['model']}")

    elif studio_mode == "Notion":
        st.subheader("Optional Notion export")
        if not notion_is_configured():
            st.info("Notion is not configured yet. Fill NOTION_TOKEN and NOTION_DATABASE_ID in your .env file.")
        note_paths = list_files_recursive(SETTINGS.wiki_dir, suffixes=(".md",))
        labels = [str(path.relative_to(SETTINGS.kb_root)) for path in note_paths]
        if labels:
            selected = st.selectbox("Choose a note to export", labels, key="notion_note")
            if st.button("Export selected note to Notion"):
                result = push_note_to_notion(SETTINGS.kb_root / selected)
                if result.get("ok"):
                    st.success(result["message"])
                else:
                    st.error(result["message"])
