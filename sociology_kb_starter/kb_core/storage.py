from __future__ import annotations

from pathlib import Path
from typing import Any
import shutil

from pydantic import ValidationError

from kb_core.config import SETTINGS
from kb_core.models import DocumentStatus, RawDocumentMetadata
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


DEFAULT_SEMESTER = "2026-S1"
DEFAULT_COURSE = "general"


def ensure_project_dirs() -> None:
    for path in REQUIRED_DIRS:
        path.mkdir(parents=True, exist_ok=True)


def sidecar_path_for(raw_path: Path) -> Path:
    return raw_path.with_suffix(raw_path.suffix + ".meta.json")


def _target_path(filename: str, semester: str | None, course: str | None) -> Path:
    semester_slug = slugify(semester or DEFAULT_SEMESTER)
    course_slug = slugify(course or DEFAULT_COURSE)
    return SETTINGS.raw_dir / semester_slug / course_slug / filename


def _build_metadata(raw_path: Path, *, semester: str | None, course: str | None, extra_metadata: dict[str, Any] | None) -> RawDocumentMetadata:
    now = utc_now_iso()
    incoming = extra_metadata or {}
    return RawDocumentMetadata(
        semester=semester or DEFAULT_SEMESTER,
        course=course or DEFAULT_COURSE,
        filename=raw_path.name,
        raw_path=str(raw_path),
        uploaded_at=incoming.get("uploaded_at", now),
        updated_at=now,
        status=DocumentStatus.SAVED_RAW,
        manual_concepts=incoming.get("manual_concepts", []),
        manual_authors=incoming.get("manual_authors", []),
    )


def save_uploaded_bytes(
    *,
    filename: str,
    content: bytes,
    semester: str | None = None,
    course: str | None = None,
    extra_metadata: dict[str, Any] | None = None,
) -> Path:
    ensure_project_dirs()
    target_path = _target_path(filename, semester, course)
    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_bytes(content)
    metadata = _build_metadata(target_path, semester=semester, course=course, extra_metadata=extra_metadata)
    write_json(sidecar_path_for(target_path), metadata.model_dump(mode="json"))
    return target_path


def register_existing_file(source_path: Path, semester: str | None = None, course: str | None = None, extra_metadata: dict[str, Any] | None = None) -> Path:
    target = _target_path(source_path.name, semester, course)
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source_path, target)
    metadata = _build_metadata(target, semester=semester, course=course, extra_metadata=extra_metadata)
    write_json(sidecar_path_for(target), metadata.model_dump(mode="json"))
    return target


def read_metadata(raw_path: Path) -> RawDocumentMetadata:
    sidecar = sidecar_path_for(raw_path)
    if not sidecar.exists():
        meta = _build_metadata(raw_path, semester=None, course=None, extra_metadata=None)
        write_json(sidecar, meta.model_dump(mode="json"))
        return meta

    try:
        data = read_json(sidecar)
        return RawDocumentMetadata.model_validate(data)
    except (ValidationError, ValueError, TypeError):
        fallback = _build_metadata(raw_path, semester=None, course=None, extra_metadata=None)
        fallback.last_error_category = "invalid_metadata"
        fallback.last_error_message = "Metadata sidecar was invalid; regenerated with safe defaults."
        write_json(sidecar, fallback.model_dump(mode="json"))
        return fallback


def update_metadata_status(raw_path: Path, *, status: DocumentStatus, error_category: str | None = None, error_message: str | None = None, compiled_note_path: str | None = None) -> RawDocumentMetadata:
    metadata = read_metadata(raw_path)
    metadata.status = status
    metadata.updated_at = utc_now_iso()
    if status in {DocumentStatus.COMPILING, DocumentStatus.COMPILE_FAILED, DocumentStatus.PARSE_FAILED, DocumentStatus.COMPILED}:
        metadata.compile_attempts += 1 if status == DocumentStatus.COMPILING else 0
    metadata.last_error_category = error_category
    metadata.last_error_message = error_message
    if compiled_note_path:
        metadata.compiled_note_path = compiled_note_path
    write_json(sidecar_path_for(raw_path), metadata.model_dump(mode="json"))
    return metadata


def mark_compile_pending(raw_path: Path) -> RawDocumentMetadata:
    return update_metadata_status(raw_path, status=DocumentStatus.COMPILE_PENDING)


def list_raw_documents() -> list[dict[str, Any]]:
    ensure_project_dirs()
    files = [p for p in list_files_recursive(SETTINGS.raw_dir) if not p.name.endswith(".meta.json")]
    docs: list[dict[str, Any]] = []
    for path in files:
        metadata = read_metadata(path)
        docs.append({"path": path, "metadata": metadata.model_dump(mode="json")})
    docs.sort(key=lambda item: str(item["path"]).lower())
    return docs


def write_note(note_path: Path, frontmatter: dict[str, Any], body: str) -> None:
    save_markdown_file(note_path, frontmatter, body)
