"""Watched-folder daemon: monitors data/inbox/ for new PDFs and auto-ingests them."""
from __future__ import annotations

import argparse
import logging
import shutil
import time
from pathlib import Path

from watchdog.events import FileSystemEventHandler, FileCreatedEvent
from watchdog.observers import Observer

from kb_core.compiler import compile_raw_document, rebuild_indexes
from kb_core.config import SETTINGS
from kb_core.models import DocumentStatus
from kb_core.storage import ensure_project_dirs, register_existing_file

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

SUPPORTED_EXTENSIONS = {".pdf", ".txt", ".md"}
# Seconds to wait after detecting a file (ensures write is complete)
SETTLE_DELAY = 2.0


def _infer_semester_course(file_path: Path, inbox_root: Path) -> tuple[str, str]:
    """Infer semester/course from subfolder structure under inbox/.

    Expected: inbox/{semester}/{course}/file.pdf
    Fallback: semester=inbox, course=general
    """
    try:
        rel = file_path.parent.relative_to(inbox_root)
        parts = rel.parts
    except ValueError:
        parts = ()

    semester = parts[0] if len(parts) >= 1 else "inbox"
    course = parts[1] if len(parts) >= 2 else "general"
    return semester, course


def process_file(file_path: Path) -> bool:
    """Ingest and compile a single file from the inbox. Returns True on success."""
    inbox_root = SETTINGS.inbox_dir

    if file_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
        logger.debug("Skipping unsupported file: %s", file_path.name)
        return False

    # Skip files in the processed/ subfolder
    try:
        file_path.relative_to(SETTINGS.inbox_processed_dir)
        return False
    except ValueError:
        pass  # Not inside processed/, continue

    semester, course = _infer_semester_course(file_path, inbox_root)
    logger.info("Processing: %s (semester=%s, course=%s)", file_path.name, semester, course)

    try:
        ensure_project_dirs()
        raw_path = register_existing_file(file_path, semester=semester, course=course)
        result = compile_raw_document(raw_path)

        if result.ok:
            logger.info("Compiled successfully: %s → %s", file_path.name, result.note_path or "wiki")
            rebuild_indexes()
        else:
            logger.warning("Compilation issue for %s: %s", file_path.name, result.message)

        # Move original to processed/
        dest = SETTINGS.inbox_processed_dir / file_path.name
        dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.exists():
            # Avoid overwrite: append timestamp
            stem = dest.stem
            dest = dest.with_name(f"{stem}_{int(time.time())}{dest.suffix}")
        shutil.move(str(file_path), str(dest))
        logger.info("Moved to processed: %s", dest.name)
        return result.ok

    except Exception:
        logger.exception("Failed to process %s", file_path.name)
        return False


def process_inbox_once() -> int:
    """Scan inbox/ and process all pending files. Returns count of files processed."""
    inbox = SETTINGS.inbox_dir
    if not inbox.is_dir():
        logger.info("Inbox directory does not exist: %s", inbox)
        return 0

    count = 0
    for file_path in sorted(inbox.rglob("*")):
        if not file_path.is_file():
            continue
        if file_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue
        # Skip processed/
        try:
            file_path.relative_to(SETTINGS.inbox_processed_dir)
            continue
        except ValueError:
            pass
        if process_file(file_path):
            count += 1
    return count


class InboxHandler(FileSystemEventHandler):
    """Watchdog handler that processes new files dropped into inbox/."""

    def on_created(self, event: FileCreatedEvent) -> None:  # type: ignore[override]
        if event.is_directory:
            return
        file_path = Path(event.src_path)
        if file_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            return
        # Skip processed/
        try:
            file_path.relative_to(SETTINGS.inbox_processed_dir)
            return
        except ValueError:
            pass

        # Wait for file write to settle
        logger.info("Detected new file: %s — waiting %.0fs for write to complete...", file_path.name, SETTLE_DELAY)
        time.sleep(SETTLE_DELAY)
        process_file(file_path)


def watch(inbox_path: Path | None = None) -> None:
    """Start the continuous watcher on the inbox directory."""
    inbox = inbox_path or SETTINGS.inbox_dir
    inbox.mkdir(parents=True, exist_ok=True)
    SETTINGS.inbox_processed_dir.mkdir(parents=True, exist_ok=True)

    logger.info("Watching %s for new files...", inbox)
    logger.info("Drop PDFs, TXT, or MD files here. Subfolder convention: inbox/{semester}/{course}/")
    logger.info("Press Ctrl+C to stop.")

    # Process any files already in inbox
    existing = process_inbox_once()
    if existing:
        logger.info("Processed %d existing file(s) from inbox.", existing)

    handler = InboxHandler()
    observer = Observer()
    observer.schedule(handler, str(inbox), recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logger.info("Stopping watcher...")
        observer.stop()
    observer.join()


def main() -> None:
    parser = argparse.ArgumentParser(description="Watch inbox/ for new documents and auto-ingest them")
    parser.add_argument("--once", action="store_true", help="Process current inbox contents and exit (no watching)")
    parser.add_argument("--inbox", type=str, default=None, help="Override inbox directory path")
    args = parser.parse_args()

    inbox = Path(args.inbox) if args.inbox else None

    if args.once:
        target = inbox or SETTINGS.inbox_dir
        target.mkdir(parents=True, exist_ok=True)
        count = process_inbox_once()
        print(f"Processed {count} file(s).")
    else:
        watch(inbox)


if __name__ == "__main__":
    main()
