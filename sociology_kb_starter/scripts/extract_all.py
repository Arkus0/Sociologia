"""Extract text from all metodologia PDFs and save to temp files for review."""
import sys
from pathlib import Path

from kb_core.extraction import extract_text
from kb_core.config import SETTINGS

raw_dir = SETTINGS.raw_dir / "2026-s1" / "metodologia-de-las-ciencias-sociales"
out_dir = Path("scripts/_extracted")
out_dir.mkdir(parents=True, exist_ok=True)

pdfs = sorted(raw_dir.glob("*.pdf"))
for pdf in pdfs:
    print(f"Extracting: {pdf.name}")
    result = extract_text(pdf)
    print(f"  Status: {result.status}, Pages: {result.page_count}, Text chars: {len(result.text or '')}")
    if result.text:
        out_path = out_dir / f"{pdf.stem}.txt"
        out_path.write_text(result.text, encoding="utf-8")
        print(f"  Saved to: {out_path}")
    else:
        print(f"  ERROR: {result.message}")
