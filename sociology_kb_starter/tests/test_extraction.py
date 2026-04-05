from __future__ import annotations

from pathlib import Path

import pymupdf

from kb_core.extraction import extract_text
from kb_core.models import ExtractionStatus


def _make_blank_pdf(path: Path) -> None:
    doc = pymupdf.open()
    doc.new_page(width=200, height=200)
    doc.save(str(path))
    doc.close()


def test_pdf_extraction_failure_empty_pdf(kb_tmp) -> None:
    pdf_path = kb_tmp / "raw" / "2026-s1" / "general" / "blank.pdf"
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    _make_blank_pdf(pdf_path)

    result = extract_text(pdf_path)
    assert result.status in {ExtractionStatus.EMPTY, ExtractionStatus.SUCCESS}


def test_pdf_extraction_encrypted(kb_tmp) -> None:
    pdf_path = kb_tmp / "raw" / "2026-s1" / "general" / "enc.pdf"
    pdf_path.parent.mkdir(parents=True, exist_ok=True)

    doc = pymupdf.open()
    doc.new_page(width=200, height=200)
    perm = pymupdf.PDF_PERM_ACCESSIBILITY
    encrypt_meth = pymupdf.PDF_ENCRYPT_AES_256
    doc.save(str(pdf_path), encryption=encrypt_meth, owner_pw="owner", user_pw="secret", permissions=perm)
    doc.close()

    result = extract_text(pdf_path)
    assert result.status == ExtractionStatus.ENCRYPTED


def test_pdf_extraction_parse_error(kb_tmp) -> None:
    pdf_path = kb_tmp / "raw" / "2026-s1" / "general" / "bad.pdf"
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    pdf_path.write_bytes(b"not-a-real-pdf")

    result = extract_text(pdf_path)
    assert result.status == ExtractionStatus.PARSE_ERROR
