from __future__ import annotations

from pathlib import Path
from typing import Any
import shutil

from pypdf import PdfReader

from kb_core.config import SETTINGS
from kb_core.utils import list_files_recursive, read_json, save_markdown_file, slugify, utc_now_iso, write_json


REQUIRED_DIRS = [
    SETTINGS.raw_dir,
    SETTINGS.by_course_dir,
    SETTINGS.by_concept_dir,
    SETTINGS.by_author_dir,
    SETTINGS.syntheses_dir,
    SETTINGS.answered_questions_dir,
    SETTINGS.open_questions_dir,
]


def ensure_project_dirs() -> None:
    for path in REQUIRED_DIRS:
        path.mkdir(parents=True, exist_ok=True)


def sidecar_path_for(raw_path: Path) -> Path:
    return raw_path.with_suffix(raw_path.suffix + ".meta.json")


def save_uploaded_bytes(
    *,
    filename: str,
    content: bytes,
    semester: str,
    course: str,
    extra_metadata: dict[str, Any] | None = None,
) -> Path:
    ensure_project_dirs()
    semester_slug = slugify(semester)
    course_slug = slugify(course)
    target_dir = SETTINGS.raw_dir / semester_slug / course_slug
    target_dir.mkdir(parents=True, exist_ok=True)
    target_path = target_dir / filename
    target_path.write_bytes(content)

    metadata = {
        "semester": semester,
        "course": course,
        "filename": filename,
        "raw_path": str(target_path),
        "uploaded_at": utc_now_iso(),
        "status": "raw",
    }
    if extra_metadata:
        metadata.update(extra_metadata)

    write_json(sidecar_path_for(target_path), metadata)
    return target_path


def register_existing_file(source_path: Path, semester: str, course: str, extra_metadata: dict[str, Any] | None = None) -> Path:
    target_dir = SETTINGS.raw_dir / slugify(semester) / slugify(course)
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / source_path.name
    shutil.copy2(source_path, target)
    metadata = {
        "semester": semester,
        "course": course,
        "filename": source_path.name,
        "raw_path": str(target),
        "uploaded_at": utc_now_iso(),
        "status": "raw",
    }
    if extra_metadata:
        metadata.update(extra_metadata)
    write_json(sidecar_path_for(target), metadata)
    return target


def list_raw_documents() -> list[dict[str, Any]]:
    ensure_project_dirs()
    files = [p for p in list_files_recursive(SETTINGS.raw_dir) if not p.name.endswith(".meta.json")]
    docs: list[dict[str, Any]] = []
    for path in files:
        meta_path = sidecar_path_for(path)
        metadata = read_json(meta_path) if meta_path.exists() else {}
        docs.append({
            "path": path,
            "metadata": metadata,
        })
    docs.sort(key=lambda item: str(item["path"]).lower())
    return docs


def extract_text_from_raw(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix in {".md", ".txt"}:
        return path.read_text(encoding="utf-8", errors="ignore")
    if suffix == ".pdf":
        reader = PdfReader(str(path))
        chunks: list[str] = []
        for idx, page in enumerate(reader.pages, start=1):
            page_text = page.extract_text() or ""
            chunks.append(f"\n\n[Page {idx}]\n{page_text}")
        return "\n".join(chunks).strip()
    return ""


def write_note(note_path: Path, frontmatter: dict[str, Any], body: str) -> None:
    save_markdown_file(note_path, frontmatter, body)
