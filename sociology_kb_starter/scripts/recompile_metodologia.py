"""Recompile all Metodologia PDFs with the real LLM provider."""
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

from kb_core.compiler import compile_raw_document, rebuild_indexes
from kb_core.config import SETTINGS

raw_dir = SETTINGS.raw_dir / "2026-s1" / "metodologia-de-las-ciencias-sociales"
pdfs = sorted(raw_dir.glob("*.pdf"))

print(f"Found {len(pdfs)} PDFs to recompile:")
for p in pdfs:
    print(f"  - {p.name}")

results = []
for pdf in pdfs:
    print(f"\n{'='*60}")
    print(f"Compiling: {pdf.name}")
    print(f"{'='*60}")
    result = compile_raw_document(pdf)
    results.append(result)
    print(f"  OK: {result.ok}")
    print(f"  Provider: {result.llm_provider or 'N/A'}")
    print(f"  Model: {result.llm_model or 'N/A'}")
    print(f"  Note: {result.note_path or 'N/A'}")
    if not result.ok:
        print(f"  Error: {result.message}")

print(f"\n{'='*60}")
print("Rebuilding indexes...")
rebuild_indexes()
print("Done!")

ok_count = sum(1 for r in results if r.ok)
print(f"\nResults: {ok_count}/{len(results)} compiled successfully")
