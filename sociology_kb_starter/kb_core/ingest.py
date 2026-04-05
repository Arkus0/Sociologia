from __future__ import annotations

import argparse
import sys
from pathlib import Path

from kb_core.compiler import compile_raw_document, rebuild_indexes
from kb_core.config import SETTINGS
from kb_core.models import CompilationResult, DocumentStatus
from kb_core.storage import ensure_project_dirs, list_raw_documents, register_existing_file


def scan_pending() -> list[Path]:
    """Find all raw files with status saved_raw or compile_pending."""
    pending: list[Path] = []
    for doc in list_raw_documents():
        status = doc["metadata"].get("status", "")
        if status in {DocumentStatus.SAVED_RAW.value, DocumentStatus.COMPILE_PENDING.value}:
            pending.append(doc["path"])
    return pending


def compile_batch(paths: list[Path]) -> list[CompilationResult]:
    """Compile a list of raw document paths sequentially."""
    results: list[CompilationResult] = []
    for path in paths:
        result = compile_raw_document(path)
        results.append(result)
    if results:
        rebuild_indexes()
    return results


def ingest_directory(dir_path: Path, semester: str, course: str) -> list[Path]:
    """Register all supported files in a directory as raw documents."""
    ensure_project_dirs()
    supported = (".pdf", ".txt", ".md")
    registered: list[Path] = []
    if not dir_path.is_dir():
        raise FileNotFoundError(f"Directory not found: {dir_path}")
    for file_path in sorted(dir_path.iterdir()):
        if file_path.is_file() and file_path.suffix.lower() in supported:
            target = register_existing_file(file_path, semester=semester, course=course)
            registered.append(target)
    return registered


def ingest_and_compile(dir_path: Path, semester: str, course: str) -> list[CompilationResult]:
    """Register files from a directory and compile them all."""
    registered = ingest_directory(dir_path, semester, course)
    return compile_batch(registered)


def main() -> None:
    parser = argparse.ArgumentParser(description="Bulk ingest and compile raw documents")
    parser.add_argument("directory", nargs="?", help="Directory of files to ingest")
    parser.add_argument("--semester", default="2026-S1", help="Semester ID (e.g. 2026-S1)")
    parser.add_argument("--course", default="general", help="Course slug")
    parser.add_argument("--compile-pending", action="store_true", help="Compile all pending documents")
    args = parser.parse_args()

    if args.compile_pending:
        pending = scan_pending()
        if not pending:
            print("No pending documents found.")
            return
        print(f"Compiling {len(pending)} pending documents...")
        results = compile_batch(pending)
        ok = sum(1 for r in results if r.ok)
        print(f"Done: {ok}/{len(results)} compiled successfully.")
        return

    if not args.directory:
        parser.print_help()
        sys.exit(1)

    dir_path = Path(args.directory).resolve()
    print(f"Ingesting from {dir_path} (semester={args.semester}, course={args.course})...")
    results = ingest_and_compile(dir_path, args.semester, args.course)
    ok = sum(1 for r in results if r.ok)
    print(f"Done: {ok}/{len(results)} compiled successfully.")


if __name__ == "__main__":
    main()
