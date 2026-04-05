from __future__ import annotations

from collections import deque
from pathlib import Path
import difflib
import subprocess

from kb_core.config import SETTINGS
from kb_core.graph_index import build_graph_index
from kb_core.qa import file_answer_to_wiki, retrieve_notes
from kb_core.search_engine import HybridSearchEngine
from kb_core.storage import read_metadata, sidecar_path_for
from kb_core.utils import load_markdown_file, read_json, read_text, slugify, to_markdown, write_text

_hybrid_engine: HybridSearchEngine | None = None


def _get_hybrid_engine() -> HybridSearchEngine:
    global _hybrid_engine
    if _hybrid_engine is None:
        _hybrid_engine = HybridSearchEngine()
    return _hybrid_engine


def _note_type_dirs() -> dict[str, Path]:
    return {
        "source": SETTINGS.sources_dir,
        "concept": SETTINGS.concepts_dir,
        "author": SETTINGS.authors_dir,
        "course": SETTINGS.courses_dir,
        "research": SETTINGS.research_dir,
    }


def _resolve_note_path(path_or_id: str) -> Path:
    raw = Path(path_or_id)
    if raw.exists() and raw.suffix == ".md":
        return raw

    candidate = SETTINGS.kb_root / path_or_id
    if candidate.exists() and candidate.suffix == ".md":
        return candidate

    for path in SETTINGS.wiki_dir.rglob("*.md"):
        frontmatter, _body = load_markdown_file(path)
        if frontmatter.get("id") == path_or_id:
            return path
    raise FileNotFoundError(f"Note not found: {path_or_id}")


def _matches_filters(frontmatter: dict, body: str, filters: dict | None) -> bool:
    if not filters:
        return True
    for key, expected in filters.items():
        if key == "contains":
            needle = str(expected).strip().lower()
            haystack = f"{frontmatter.get('title', '')}\n{body}".lower()
            if needle and needle not in haystack:
                return False
            continue

        value = frontmatter.get(key)
        if isinstance(value, list):
            normalized = {str(item).lower() for item in value}
            if str(expected).lower() not in normalized:
                return False
        else:
            if str(value).lower() != str(expected).lower():
                return False
    return True


def search_notes(query: str, filters: dict | None = None, limit: int = 10) -> list[dict]:
    engine = _get_hybrid_engine()

    # Map filter keys to search engine params
    note_type = filters.pop("note_type", None) if filters else None
    semester = filters.pop("semester", None) if filters else None
    course = filters.pop("course", None) if filters else None
    author = filters.pop("author", None) if filters else None
    concept = filters.pop("concept", None) if filters else None

    results = engine.search(
        query,
        top_k=max(limit * 3, 10),
        note_type=note_type,
        semester=semester,
        course=course,
        author=author,
        concept=concept,
    )

    # Apply any remaining filters (e.g. "contains")
    final: list[dict] = []
    for item in results:
        if filters:
            # Load full note for remaining filters
            try:
                note_path = SETTINGS.kb_root / item["path"]
                frontmatter, body = load_markdown_file(note_path)
                if not _matches_filters(frontmatter, body, filters):
                    continue
            except Exception:
                continue
        final.append({
            "id": item.get("id", ""),
            "title": item.get("title", ""),
            "note_type": item.get("note_type", "unknown"),
            "course": item.get("course", "general"),
            "path": item["path"],
            "score": item.get("score", 0),
        })
        if len(final) >= limit:
            break
    return final


def read_note(path_or_id: str) -> dict:
    path = _resolve_note_path(path_or_id)
    frontmatter, body = load_markdown_file(path)
    return {
        "id": frontmatter.get("id", path.stem),
        "path": str(path.relative_to(SETTINGS.kb_root)),
        "frontmatter": frontmatter,
        "body": body,
    }


def list_notes(note_type: str, filters: dict | None = None) -> list[dict]:
    note_dirs = _note_type_dirs()
    if note_type not in note_dirs:
        raise ValueError(f"Unsupported note_type '{note_type}'. Use one of: {', '.join(sorted(note_dirs))}")

    notes: list[dict] = []
    for path in note_dirs[note_type].rglob("*.md"):
        frontmatter, body = load_markdown_file(path)
        if not _matches_filters(frontmatter, body, filters):
            continue
        notes.append(
            {
                "id": frontmatter.get("id", path.stem),
                "title": frontmatter.get("title", path.stem),
                "note_type": frontmatter.get("note_type", note_type),
                "path": str(path.relative_to(SETTINGS.kb_root)),
                "updated_at": frontmatter.get("updated_at") or frontmatter.get("compiled_at", ""),
            }
        )
    notes.sort(key=lambda item: (item["title"].lower(), item["path"]))
    return notes


def list_courses() -> list[dict]:
    return list_notes("course")


def list_authors() -> list[dict]:
    return list_notes("author")


def list_concepts() -> list[dict]:
    return list_notes("concept")


def get_graph_neighbors(node_id: str, node_type: str, depth: int = 1) -> dict:
    graph_path = SETTINGS.graph_dir / "atlas_graph.json"
    graph = read_json(graph_path) if graph_path.exists() else build_graph_index()

    canonical_id = node_id if "::" in node_id else f"{node_type}::{slugify(node_id)}"
    nodes = {node["id"]: node for node in graph.get("nodes", [])}
    if canonical_id not in nodes:
        raise ValueError(f"Node not found: {canonical_id}")

    adjacency: dict[str, set[str]] = {}
    for edge in graph.get("edges", []):
        adjacency.setdefault(edge["source"], set()).add(edge["target"])
        adjacency.setdefault(edge["target"], set()).add(edge["source"])

    visited = {canonical_id}
    queue = deque([(canonical_id, 0)])
    neighbor_ids: set[str] = set()

    while queue:
        current, current_depth = queue.popleft()
        if current_depth >= depth:
            continue
        for nxt in adjacency.get(current, set()):
            if nxt in visited:
                continue
            visited.add(nxt)
            neighbor_ids.add(nxt)
            queue.append((nxt, current_depth + 1))

    return {
        "node": nodes[canonical_id],
        "depth": depth,
        "neighbors": [nodes[nid] for nid in sorted(neighbor_ids)],
    }


def get_recent_sources(limit: int = 10) -> list[dict]:
    notes = list_notes("source")
    notes.sort(key=lambda item: item.get("updated_at", ""), reverse=True)
    return notes[:limit]


def get_source_provenance(note_id: str) -> dict:
    note = read_note(note_id)
    source_path = note["frontmatter"].get("source_path")
    if not source_path:
        raise ValueError("Note has no source_path in frontmatter; provenance unavailable.")

    raw_path = SETTINGS.kb_root / source_path
    metadata = read_metadata(raw_path)
    sidecar = sidecar_path_for(raw_path)

    return {
        "note_id": note["id"],
        "note_path": note["path"],
        "raw_source_path": source_path,
        "metadata_path": str(sidecar.relative_to(SETTINGS.kb_root)),
        "metadata": metadata.model_dump(mode="json"),
    }


def propose_note_edit(note_id: str, instruction: str) -> dict:
    note = read_note(note_id)
    body = note["body"]
    heading = "## Agent edit proposal"
    proposal = (
        f"{body.rstrip()}\n\n{heading}\n"
        f"- instruction: {instruction.strip()}\n"
        "- proposed_change: Review and apply manually or through a PR patch.\n"
    )
    return {
        "note_id": note["id"],
        "path": note["path"],
        "instruction": instruction,
        "proposed_content": proposal,
    }


def build_patch_for_note(note_id: str, new_content: str) -> dict:
    note = read_note(note_id)
    note_path = SETTINGS.kb_root / note["path"]
    current_markdown = to_markdown(note["frontmatter"], note["body"]) 
    desired_markdown = to_markdown(note["frontmatter"], new_content)
    diff_lines = list(
        difflib.unified_diff(
            current_markdown.splitlines(),
            desired_markdown.splitlines(),
            fromfile=str(note_path),
            tofile=str(note_path),
            lineterm="",
        )
    )
    return {
        "note_id": note["id"],
        "path": note["path"],
        "patch": "\n".join(diff_lines) + ("\n" if diff_lines else ""),
        "new_content": new_content,
    }


def create_branch_and_pr_for_changes(changes: list[dict], branch_name: str | None = None, commit_message: str | None = None) -> dict:
    if not changes:
        raise ValueError("No changes provided.")

    branch = branch_name or f"kb-edit-{slugify(changes[0].get('note_id', 'change'))}"
    commit_msg = commit_message or f"kb: update {changes[0].get('note_id', 'note')}"

    subprocess.run(["git", "checkout", "-b", branch], check=True)
    updated_paths: list[str] = []

    for change in changes:
        note = read_note(change["note_id"])
        target = SETTINGS.kb_root / note["path"]
        write_text(target, to_markdown(note["frontmatter"], change["new_content"]))
        updated_paths.append(str(target))

    subprocess.run(["git", "add", *updated_paths], check=True)
    subprocess.run(["git", "commit", "-m", commit_msg], check=True)

    return {
        "branch": branch,
        "commit_message": commit_msg,
        "updated_files": [str(Path(path).relative_to(Path.cwd())) for path in updated_paths],
        "pr_hint": "Push the branch and open a GitHub PR for review.",
    }


def file_answer(
    query: str,
    answer: str,
    concepts: list[str] | None = None,
    authors: list[str] | None = None,
    retrieved: list[dict] | None = None,
) -> dict:
    """File a Q&A answer back into the wiki as a research note."""
    note_path = file_answer_to_wiki(query, answer, concepts=concepts, authors=authors, retrieved=retrieved)
    return {
        "path": str(note_path.relative_to(SETTINGS.kb_root)),
        "message": f"Research note filed at {note_path.name}",
    }


def generate_slides_service(topic_or_query: str, output_name: str | None = None) -> dict:
    """Generate a Marp slide deck from wiki content."""
    from kb_core.slides import generate_slides
    output_path = generate_slides(topic_or_query, output_name=output_name)
    return {
        "path": str(output_path.relative_to(SETTINGS.kb_root)),
        "message": f"Slide deck generated at {output_path.name}",
    }


def generate_viz_service(viz_type: str, data: dict) -> dict:
    """Generate a visualization from wiki data."""
    from kb_core.viz import generate_concept_map, generate_statistics, generate_timeline

    if viz_type == "concept_map":
        concepts = data.get("concepts", [])
        output_path = generate_concept_map(concepts, output_name=data.get("output_name"))
    elif viz_type == "timeline":
        events = data.get("events", [])
        output_path = generate_timeline(events, output_name=data.get("output_name"))
    elif viz_type == "statistics":
        output_path = generate_statistics(data, output_name=data.get("output_name"))
    else:
        raise ValueError(f"Unknown viz_type: {viz_type}. Use concept_map, timeline, or statistics.")

    return {
        "path": str(output_path.relative_to(SETTINGS.kb_root)),
        "message": f"Visualization generated: {output_path.name}",
    }


def get_semester_stats(semester_id: str) -> dict:
    """Get statistics for a specific semester."""
    from kb_core.semesters import semester_stats
    return semester_stats(semester_id)


def suggest_articles() -> list[dict]:
    """Get suggestions for new cross-course articles."""
    from kb_core.lint import suggest_new_articles
    return suggest_new_articles()


def rebuild_embeddings() -> dict:
    """Rebuild the embedding index for semantic search."""
    from kb_core.embeddings import EmbeddingIndex

    idx = EmbeddingIndex()
    count = idx.build()
    # Reset cached hybrid engine so it picks up new embeddings
    global _hybrid_engine
    _hybrid_engine = None
    return {"embedded_docs": count, "message": f"Embedded {count} wiki notes."}
