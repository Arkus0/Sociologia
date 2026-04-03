from __future__ import annotations

from pathlib import Path

from pypdf import PdfReader
from pypdf.errors import PdfReadError

from kb_core.models import ExtractionPageDiagnostic, ExtractionResult, ExtractionStatus


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
        reader = PdfReader(str(path))
    except PdfReadError as exc:
        return ExtractionResult(
            status=ExtractionStatus.PARSE_ERROR,
            message="PDF parsing failed at file load stage.",
            error_category="pdf_read_error",
            diagnostics=[ExtractionPageDiagnostic(page_number=0, status="error", message=str(exc)[:240])],
        )
    except Exception as exc:  # pragma: no cover - defensive fallback for library edge cases
        return ExtractionResult(
            status=ExtractionStatus.PARSE_ERROR,
            message="PDF parsing failed with unexpected loader error.",
            error_category="pdf_unexpected_error",
            diagnostics=[ExtractionPageDiagnostic(page_number=0, status="error", message=str(exc)[:240])],
        )

    if reader.is_encrypted:
        return ExtractionResult(
            status=ExtractionStatus.ENCRYPTED,
            message="PDF is encrypted and cannot be extracted without a password.",
            error_category="encrypted_pdf",
            page_count=0,
        )

    all_chunks: list[str] = []
    diagnostics: list[ExtractionPageDiagnostic] = []
    pages_with_text = 0

    for page_num, page in enumerate(reader.pages, start=1):
        try:
            page_text = (page.extract_text() or "").strip()
            if not page_text:
                diagnostics.append(
                    ExtractionPageDiagnostic(
                        page_number=page_num,
                        status="empty",
                        message="No text detected on page.",
                        chars_extracted=0,
                    )
                )
                continue
            pages_with_text += 1
            diagnostics.append(
                ExtractionPageDiagnostic(
                    page_number=page_num,
                    status="ok",
                    chars_extracted=len(page_text),
                )
            )
            all_chunks.append(f"\n\n[Page {page_num}]\n{page_text}")
        except Exception as exc:  # pragma: no cover - rare per-page parser failures
            diagnostics.append(
                ExtractionPageDiagnostic(
                    page_number=page_num,
                    status="error",
                    message=f"Page extraction failed: {exc}",
                    chars_extracted=0,
                )
            )

    text = "\n".join(all_chunks).strip()
    if not text:
        return ExtractionResult(
            status=ExtractionStatus.EMPTY,
            text="",
            mime_hint=suffix,
            page_count=0,
            pages_with_text=0,
            diagnostics=diagnostics,
            message="No extractable text found. PDF may be scanned/image-based.",
            error_category="no_extractable_text",
        )

    return ExtractionResult(
        status=ExtractionStatus.SUCCESS,
        text=text,
        mime_hint=suffix,
        page_count=len(reader.pages),
        pages_with_text=pages_with_text,
        diagnostics=diagnostics,
        message="PDF text extracted successfully.",
    )
