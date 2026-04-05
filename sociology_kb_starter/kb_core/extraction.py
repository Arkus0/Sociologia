from __future__ import annotations

import logging
import re
from collections import Counter
from pathlib import Path

import pymupdf

from kb_core.models import ExtractionPageDiagnostic, ExtractionResult, ExtractionStatus

logger = logging.getLogger(__name__)

# --- Tesseract availability check (done once at import time) ---
_TESSERACT_AVAILABLE: bool | None = None


def _check_tesseract() -> bool:
    global _TESSERACT_AVAILABLE
    if _TESSERACT_AVAILABLE is not None:
        return _TESSERACT_AVAILABLE
    try:
        test_doc = pymupdf.open()
        test_page = test_doc.new_page(width=100, height=100)
        test_page.get_textpage_ocr(flags=0, dpi=72, full=True, language="eng")
        test_doc.close()
        _TESSERACT_AVAILABLE = True
    except Exception:
        _TESSERACT_AVAILABLE = False
        logger.info("Tesseract OCR not available — scanned PDFs will use text-only extraction")
    return _TESSERACT_AVAILABLE


# --- Text cleaning helpers ---
_HYPHEN_EOL_RE = re.compile(r"(\w)-\n(\w)")
_BARE_PAGE_NUM_RE = re.compile(r"^\s*\d{1,4}\s*$")


def clean_extracted_text(text: str) -> str:
    """Post-process raw PDF text: remove repeated headers, rejoin hyphens, strip noise."""
    lines = text.split("\n")

    # 1. Detect repeated header/footer lines (appear on 3+ pages identically)
    line_counts: Counter[str] = Counter()
    for line in lines:
        stripped = line.strip()
        if 3 <= len(stripped) <= 120:
            line_counts[stripped] += 1
    repeated = {ln for ln, count in line_counts.items() if count >= 3}
    if repeated:
        logger.debug("Removing %d repeated header/footer patterns", len(repeated))
        lines = [ln for ln in lines if ln.strip() not in repeated]

    text = "\n".join(lines)

    # 2. Rejoin end-of-line hyphens (socie-\ndad → sociedad)
    text = _HYPHEN_EOL_RE.sub(r"\1\2", text)

    # 3. Remove bare page-number lines
    lines = text.split("\n")
    lines = [ln for ln in lines if not _BARE_PAGE_NUM_RE.match(ln)]

    # 4. Collapse runs of 3+ blank lines to 2
    cleaned: list[str] = []
    blank_run = 0
    for ln in lines:
        if ln.strip() == "":
            blank_run += 1
            if blank_run <= 2:
                cleaned.append(ln)
        else:
            blank_run = 0
            cleaned.append(ln)

    return "\n".join(cleaned).strip()


def extract_text(path: Path) -> ExtractionResult:
    suffix = path.suffix.lower()
    if suffix in {".md", ".txt"}:
        text = path.read_text(encoding="utf-8", errors="ignore").strip()
        if not text:
            return ExtractionResult(
                status=ExtractionStatus.EMPTY,
                text="",
                mime_hint=suffix,
                message="Text file is empty after decoding.",
                error_category="empty_text",
            )
        return ExtractionResult(status=ExtractionStatus.SUCCESS, text=text, mime_hint=suffix, message="Text extracted successfully.")

    if suffix != ".pdf":
        return ExtractionResult(
            status=ExtractionStatus.UNSUPPORTED,
            message=f"Unsupported file type: {suffix or 'unknown'}",
            error_category="unsupported_type",
        )

    try:
        doc = pymupdf.open(str(path))
    except Exception as exc:
        return ExtractionResult(
            status=ExtractionStatus.PARSE_ERROR,
            message="PDF parsing failed at file load stage.",
            error_category="pdf_read_error",
            diagnostics=[ExtractionPageDiagnostic(page_number=0, status="error", message=str(exc)[:240])],
        )

    if doc.is_encrypted:
        doc.close()
        return ExtractionResult(
            status=ExtractionStatus.ENCRYPTED,
            message="PDF is encrypted and cannot be extracted without a password.",
            error_category="encrypted_pdf",
            page_count=0,
        )

    all_chunks: list[str] = []
    diagnostics: list[ExtractionPageDiagnostic] = []
    pages_with_text = 0
    ocr_used = False

    for page_num in range(len(doc)):
        page = doc[page_num]
        display_num = page_num + 1
        try:
            page_text = (page.get_text("text") or "").strip()

            # OCR fallback for scanned / image-heavy pages
            if len(page_text) < 100:
                try:
                    if _check_tesseract():
                        tp = page.get_textpage_ocr(flags=0, dpi=300, full=True, language="spa+eng")
                        ocr_text = (page.get_text("text", textpage=tp) or "").strip()
                    else:
                        ocr_text = (page.get_text("text", flags=pymupdf.TEXT_DEHYPHENATE) or "").strip()
                    if len(ocr_text) > len(page_text):
                        page_text = ocr_text
                        ocr_used = True
                except Exception:
                    pass  # OCR not available, continue with what we have

            if not page_text:
                diagnostics.append(
                    ExtractionPageDiagnostic(
                        page_number=display_num,
                        status="empty",
                        message="No text detected on page.",
                        chars_extracted=0,
                    )
                )
                continue
            pages_with_text += 1
            diagnostics.append(
                ExtractionPageDiagnostic(
                    page_number=display_num,
                    status="ok",
                    chars_extracted=len(page_text),
                )
            )
            all_chunks.append(f"\n\n[Page {display_num}]\n{page_text}")
        except Exception as exc:  # pragma: no cover
            diagnostics.append(
                ExtractionPageDiagnostic(
                    page_number=display_num,
                    status="error",
                    message=f"Page extraction failed: {exc}",
                    chars_extracted=0,
                )
            )

    total_pages = len(doc)
    doc.close()

    text = "\n".join(all_chunks).strip()
    text = clean_extracted_text(text)
    if not text:
        return ExtractionResult(
            status=ExtractionStatus.EMPTY,
            text="",
            mime_hint=suffix,
            page_count=total_pages,
            pages_with_text=0,
            diagnostics=diagnostics,
            message="No extractable text found. PDF may be scanned/image-based.",
            error_category="no_extractable_text",
        )

    msg = "PDF text extracted successfully."
    if ocr_used:
        msg += " (OCR fallback used on some pages)"

    return ExtractionResult(
        status=ExtractionStatus.SUCCESS,
        text=text,
        mime_hint=suffix,
        page_count=total_pages,
        pages_with_text=pages_with_text,
        diagnostics=diagnostics,
        message=msg,
    )
