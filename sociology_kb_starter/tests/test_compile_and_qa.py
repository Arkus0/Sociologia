from __future__ import annotations

from kb_core.compiler import compile_raw_document
from kb_core.models import DocumentStatus
from kb_core.qa import retrieve_notes
from kb_core.storage import read_metadata, save_uploaded_bytes
from kb_core.utils import list_files_recursive, load_markdown_file
from kb_core.config import SETTINGS


def test_compile_fallback_and_note_written(kb_tmp) -> None:
    raw_path = save_uploaded_bytes(
        filename="durkheim.txt",
        content=b"Durkheim writes about anomie and social integration.",
        semester="2026-S1",
        course="teoria",
    )

    result = compile_raw_document(raw_path)
    assert result.ok is True
    assert result.status == DocumentStatus.COMPILED

    metadata = read_metadata(raw_path)
    assert metadata.status == DocumentStatus.COMPILED

    notes = list_files_recursive(SETTINGS.by_course_dir, suffixes=(".md",))
    assert notes, "expected at least one compiled note"
    frontmatter, body = load_markdown_file(notes[0])
    assert frontmatter["note_type"] == "source"
    assert "## Summary" in body


def test_compile_marks_parse_failed_for_unreadable_pdf(kb_tmp) -> None:
    raw_path = save_uploaded_bytes(
        filename="broken.pdf",
        content=b"broken-pdf",
        semester="2026-S1",
        course="teoria",
    )
    result = compile_raw_document(raw_path)
    assert result.ok is False
    assert result.status == DocumentStatus.PARSE_FAILED


def test_retrieval_ranking_prefers_weighted_fields(kb_tmp) -> None:
    doc1 = save_uploaded_bytes(
        filename="doc1.txt",
        content=b"Durkheim and anomie in industrial society",
        semester="2026-S1",
        course="theory",
        extra_metadata={"manual_concepts": ["anomie"], "manual_authors": ["Durkheim"]},
    )
    doc2 = save_uploaded_bytes(
        filename="doc2.txt",
        content=b"Generic class logistics and dates",
        semester="2026-S1",
        course="theory",
    )
    compile_raw_document(doc1)
    compile_raw_document(doc2)

    retrieved = retrieve_notes("anomie durkheim", top_k=2)
    assert retrieved
    top_title = retrieved[0]["frontmatter"].get("title", "").lower()
    assert "doc1" in top_title or "durkheim" in retrieved[0]["body"].lower()
