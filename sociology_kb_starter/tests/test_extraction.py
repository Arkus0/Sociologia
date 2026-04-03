from __future__ import annotations

from pathlib import Path

from pypdf import PdfWriter

from kb_core.extraction import extract_text
from kb_core.models import ExtractionStatus


def _make_blank_pdf(path: Path) -> None:
    writer = PdfWriter()
    writer.add_blank_page(width=200, height=200)
    with path.open("wb") as fh:
        writer.write(fh)


def test_pdf_extraction_failure_empty_pdf(kb_tmp) -> None:
    pdf_path = kb_tmp / "raw" / "2026-s1" / "general" / "blank.pdf"
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    _make_blank_pdf(pdf_path)

    result = extract_text(pdf_path)
    assert result.status in {ExtractionStatus.EMPTY, ExtractionStatus.SUCCESS}


def test_pdf_extraction_encrypted(kb_tmp) -> None:
    pdf_path = kb_tmp / "raw" / "2026-s1" / "general" / "enc.pdf"
    pdf_path.parent.mkdir(parents=True, exist_ok=True)

    writer = PdfWriter()
    writer.add_blank_page(width=200, height=200)
    writer.encrypt("secret")
    with pdf_path.open("wb") as fh:
        writer.write(fh)

    result = extract_text(pdf_path)
    assert result.status == ExtractionStatus.ENCRYPTED


def test_pdf_extraction_parse_error(kb_tmp) -> None:
    pdf_path = kb_tmp / "raw" / "2026-s1" / "general" / "bad.pdf"
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    pdf_path.write_bytes(b"not-a-real-pdf")

    result = extract_text(pdf_path)
    assert result.status == ExtractionStatus.PARSE_ERROR
