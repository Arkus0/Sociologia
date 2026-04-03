from __future__ import annotations

from kb_core.models import DocumentStatus, RawDocumentMetadata
from kb_core.storage import list_raw_documents, save_uploaded_bytes, sidecar_path_for
from kb_core.utils import read_json


def test_metadata_validation_dedupes_lists() -> None:
    metadata = RawDocumentMetadata(
        semester="2026-S1",
        course="theory",
        filename="doc.txt",
        raw_path="/tmp/doc.txt",
        uploaded_at="2026-01-01T00:00:00+00:00",
        updated_at="2026-01-01T00:00:00+00:00",
        manual_concepts=["anomie", " Anomie ", ""],
        manual_authors=["Durkheim", "durkheim"],
    )
    assert metadata.manual_concepts == ["anomie"]
    assert metadata.manual_authors == ["Durkheim"]


def test_save_uploaded_bytes_generates_sidecar(kb_tmp) -> None:
    raw_path = save_uploaded_bytes(filename="lecture.txt", content=b"hello", semester="2026-S1", course="theory")
    sidecar = read_json(sidecar_path_for(raw_path))
    assert sidecar["filename"] == "lecture.txt"
    assert sidecar["status"] == DocumentStatus.SAVED_RAW.value


def test_list_raw_documents_returns_metadata(kb_tmp) -> None:
    save_uploaded_bytes(filename="notes.md", content=b"# Notes", semester="2026-S1", course="theory")
    docs = list_raw_documents()
    assert len(docs) == 1
    assert docs[0]["metadata"]["course"] == "theory"
