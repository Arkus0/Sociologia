from __future__ import annotations

from enum import Enum
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator


class DocumentStatus(str, Enum):
    SAVED_RAW = "saved_raw"
    COMPILE_PENDING = "compile_pending"
    COMPILING = "compiling"
    COMPILED = "compiled"
    PARSE_FAILED = "parse_failed"
    COMPILE_FAILED = "compile_failed"


class ExtractionStatus(str, Enum):
    SUCCESS = "success"
    EMPTY = "empty"
    UNSUPPORTED = "unsupported"
    ENCRYPTED = "encrypted"
    PARSE_ERROR = "parse_error"


class ExtractionPageDiagnostic(BaseModel):
    page_number: int
    status: Literal["ok", "error", "empty"]
    message: str = ""
    chars_extracted: int = 0


class ExtractionResult(BaseModel):
    status: ExtractionStatus
    text: str = ""
    mime_hint: str = ""
    page_count: int = 0
    pages_with_text: int = 0
    diagnostics: list[ExtractionPageDiagnostic] = Field(default_factory=list)
    error_category: str | None = None
    message: str


class RawDocumentMetadata(BaseModel):
    model_config = ConfigDict(extra="forbid")

    semester: str = "unknown"
    course: str = "general"
    filename: str
    raw_path: str
    uploaded_at: str
    updated_at: str
    status: DocumentStatus = DocumentStatus.SAVED_RAW
    compile_attempts: int = 0
    last_error_category: str | None = None
    last_error_message: str | None = None
    compiled_note_path: str | None = None
    manual_concepts: list[str] = Field(default_factory=list)
    manual_authors: list[str] = Field(default_factory=list)

    @field_validator("manual_concepts", "manual_authors")
    @classmethod
    def _dedupe_trim(cls, values: list[str]) -> list[str]:
        deduped: list[str] = []
        seen: set[str] = set()
        for value in values:
            clean = str(value).strip()
            if not clean:
                continue
            key = clean.lower()
            if key in seen:
                continue
            deduped.append(clean)
            seen.add(key)
        return deduped


class CompiledSourcePayload(BaseModel):
    title: str
    summary: str = ""
    core_ideas: list[str] = Field(default_factory=list)
    concepts: list[str] = Field(default_factory=list)
    authors: list[str] = Field(default_factory=list)
    methods: list[str] = Field(default_factory=list)
    exam_questions: list[str] = Field(default_factory=list)
    open_questions: list[str] = Field(default_factory=list)
    source_anchors: list[str] = Field(default_factory=list)
    source_url: str | None = None

    @field_validator(
        "core_ideas",
        "concepts",
        "authors",
        "methods",
        "exam_questions",
        "open_questions",
        "source_anchors",
    )
    @classmethod
    def _clean_lists(cls, values: list[str]) -> list[str]:
        out: list[str] = []
        seen: set[str] = set()
        for value in values:
            clean = str(value).strip()
            if not clean:
                continue
            key = clean.lower()
            if key in seen:
                continue
            seen.add(key)
            out.append(clean)
        return out


class CompilationResult(BaseModel):
    ok: bool
    raw_path: str
    note_path: str | None = None
    status: DocumentStatus
    message: str
    error_category: str | None = None
    extraction: ExtractionResult | None = None
    llm_provider: str = "fallback"
    llm_model: str = "fallback"
    details: dict[str, Any] = Field(default_factory=dict)
