from __future__ import annotations

from pathlib import Path

from kb_core.ingest import compile_batch, ingest_directory, scan_pending
from kb_core.storage import ensure_project_dirs, save_uploaded_bytes


def test_ingest_directory(kb_tmp: Path):
    """Ingesting a directory registers all supported files."""
    ensure_project_dirs()
    src_dir = kb_tmp / "import_test"
    src_dir.mkdir(parents=True, exist_ok=True)
    (src_dir / "doc1.txt").write_text("Hello sociology", encoding="utf-8")
    (src_dir / "doc2.txt").write_text("Social facts", encoding="utf-8")
    (src_dir / "ignore.jpg").write_bytes(b"\xff\xd8")  # unsupported

    registered = ingest_directory(src_dir, semester="2026-S1", course="intro")
    assert len(registered) == 2
    assert all(p.exists() for p in registered)


def test_scan_pending_finds_saved_raw(kb_tmp: Path):
    """scan_pending returns files with saved_raw status."""
    ensure_project_dirs()
    save_uploaded_bytes(filename="test.txt", content=b"content", semester="2026-S1", course="intro")
    pending = scan_pending()
    assert len(pending) >= 1


def test_compile_batch_fallback(kb_tmp: Path):
    """compile_batch compiles files using fallback when no LLM."""
    ensure_project_dirs()
    path = save_uploaded_bytes(filename="batch.txt", content=b"Durkheim on solidarity", semester="2026-S1", course="teoria")
    results = compile_batch([path])
    assert len(results) == 1
    assert results[0].ok
