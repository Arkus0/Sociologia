from __future__ import annotations

import textwrap

import pandas as pd
import streamlit as st

from kb_core.compiler import compile_all_raw_documents, compile_raw_document, rebuild_indexes
from kb_core.config import SETTINGS
from kb_core.lint import run_lint_checks
from kb_core.notion_sync import notion_is_configured, push_note_to_notion
from kb_core.qa import answer_question
from kb_core.storage import ensure_project_dirs, list_raw_documents, mark_compile_pending, save_uploaded_bytes
from kb_core.utils import list_files_recursive, load_markdown_file


st.set_page_config(page_title="Sociology KB", layout="wide")
ensure_project_dirs()


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


st.title("Sociology Knowledge Base")
st.caption("Markdown-first sociology study console with resilient ingestion and compilation.")

with st.sidebar:
    st.subheader("Configuration")
    st.write(f"KB root: `{SETTINGS.kb_root}`")
    st.write(f"LLM provider: `{SETTINGS.llm_provider or 'none'}`")
    st.write(f"Notion configured: `{notion_is_configured()}`")
    if st.button("Rebuild concept and author indexes"):
        rebuild_indexes()
        _stats.clear()
        st.success("Indexes rebuilt.")

stats = _stats()
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Raw docs", stats["raw_docs"])
col2.metric("Course notes", stats["course_notes"])
col3.metric("Concept notes", stats["concept_notes"])
col4.metric("Author notes", stats["author_notes"])
col5.metric("Answered Q&A", stats["answered"])


tab_dashboard, tab_ingest, tab_compile, tab_explore, tab_ask, tab_lint, tab_notion = st.tabs(
    ["Dashboard", "Ingest", "Compile", "Explore", "Ask", "Lint", "Notion"]
)

with tab_dashboard:
    st.subheader("Workflow")
    st.markdown(
        textwrap.dedent(
            """
            1. Upload files (PDF/MD/TXT) with optional course and semester.
            2. Files are always stored first (`saved_raw`) regardless of parse quality.
            3. Compile now or later from the Compile tab.
            4. Review statuses, extraction failures, and lint issues.
            """
        )
    )
    frame = _raw_docs_table()
    if frame.empty:
        st.info("No raw documents yet.")
    else:
        st.dataframe(frame, use_container_width=True)

with tab_ingest:
    st.subheader("Upload raw sources")
    st.caption("Low-friction upload: only files required. Course and semester are optional defaults.")

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

            _stats.clear()
            st.success(f"Saved {len(saved_paths)} file(s).")
            if compile_results:
                ok_count = sum(1 for result in compile_results if result.ok)
                st.info(f"Compiled {ok_count}/{len(compile_results)} files. Check Compile tab for failures.")

with tab_compile:
    st.subheader("Compile raw sources")
    raw_docs = list_raw_documents()
    if not raw_docs:
        st.info("Nothing to compile yet.")
    else:
        options = {str(item["path"].relative_to(SETTINGS.kb_root)): item for item in raw_docs}
        selected = st.multiselect("Select raw files", list(options.keys()), default=list(options.keys())[:10])
        col_a, col_b = st.columns([1, 1])
        with col_a:
            if st.button("Compile selected"):
                results = [compile_raw_document(options[key]["path"]) for key in selected]
                rebuild_indexes()
                _stats.clear()
                ok_count = sum(1 for result in results if result.ok)
                st.success(f"Compiled {ok_count}/{len(results)} selected file(s).")
        with col_b:
            if st.button("Compile everything"):
                results = compile_all_raw_documents()
                _stats.clear()
                ok_count = sum(1 for result in results if result.ok)
                st.success(f"Compiled {ok_count}/{len(results)} files.")

        st.markdown("#### Raw status overview")
        st.dataframe(_raw_docs_table(), use_container_width=True)

with tab_explore:
    st.subheader("Explore notes")
    note_type = st.selectbox("Directory", ["by_course", "by_concept", "by_author"])
    base_dir = {
        "by_course": SETTINGS.by_course_dir,
        "by_concept": SETTINGS.by_concept_dir,
        "by_author": SETTINGS.by_author_dir,
    }[note_type]
    note_paths = list_files_recursive(base_dir, suffixes=(".md",))
    labels = [str(path.relative_to(SETTINGS.kb_root)) for path in note_paths]
    if labels:
        selected_label = st.selectbox("Note", labels)
        selected_path = SETTINGS.kb_root / selected_label
        frontmatter, body = load_markdown_file(selected_path)
        st.json(frontmatter)
        st.markdown(body)
    else:
        st.info("No notes in this section yet.")

with tab_ask:
    st.subheader("Ask the wiki")
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

with tab_lint:
    st.subheader("Health checks")
    issues = run_lint_checks()
    if issues:
        st.dataframe(pd.DataFrame(issues), use_container_width=True)
    else:
        st.success("No issues detected.")

with tab_notion:
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
