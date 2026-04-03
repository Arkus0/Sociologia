from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import os

from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parents[1]
load_dotenv(PROJECT_ROOT / ".env")


@dataclass(slots=True)
class Settings:
    kb_root: Path = Path(os.getenv("KB_ROOT", str(PROJECT_ROOT / "data")))
    llm_provider: str = os.getenv("LLM_PROVIDER", "").strip().lower()
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "").strip()
    openai_model: str = os.getenv("OPENAI_MODEL", "gpt-5-mini").strip()
    anthropic_api_key: str = os.getenv("ANTHROPIC_API_KEY", "").strip()
    anthropic_model: str = os.getenv("ANTHROPIC_MODEL", "claude-3-7-sonnet-latest").strip()
    notion_token: str = os.getenv("NOTION_TOKEN", "").strip()
    notion_database_id: str = os.getenv("NOTION_DATABASE_ID", "").strip()

    @property
    def raw_dir(self) -> Path:
        return self.kb_root / "raw"

    @property
    def wiki_dir(self) -> Path:
        return self.kb_root / "wiki"

    @property
    def notes_dir(self) -> Path:
        return self.wiki_dir / "notes"

    @property
    def by_course_dir(self) -> Path:
        return self.notes_dir / "by_course"

    @property
    def by_concept_dir(self) -> Path:
        return self.notes_dir / "by_concept"

    @property
    def by_author_dir(self) -> Path:
        return self.notes_dir / "by_author"

    @property
    def syntheses_dir(self) -> Path:
        return self.kb_root / "syntheses"

    @property
    def qa_dir(self) -> Path:
        return self.kb_root / "qa"

    @property
    def answered_questions_dir(self) -> Path:
        return self.qa_dir / "answered_questions"

    @property
    def open_questions_dir(self) -> Path:
        return self.qa_dir / "open_questions"


SETTINGS = Settings()
