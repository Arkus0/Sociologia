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
    openai_model: str = os.getenv("OPENAI_MODEL", "gpt-4.1-mini").strip()
    anthropic_api_key: str = os.getenv("ANTHROPIC_API_KEY", "").strip()
    anthropic_model: str = os.getenv("ANTHROPIC_MODEL", "claude-3-7-sonnet-latest").strip()
    groq_api_key: str = os.getenv("GROQ_API_KEY", "").strip()
    groq_model: str = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile").strip()
    notion_token: str = os.getenv("NOTION_TOKEN", "").strip()
    notion_database_id: str = os.getenv("NOTION_DATABASE_ID", "").strip()
    embedding_model: str = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small").strip()
    embedding_dimensions: int = int(os.getenv("EMBEDDING_DIMENSIONS", "1536"))

    @property
    def raw_dir(self) -> Path:
        return self.kb_root / "raw"

    @property
    def wiki_dir(self) -> Path:
        return self.kb_root / "wiki"

    @property
    def sources_dir(self) -> Path:
        return self.wiki_dir / "sources"

    @property
    def concepts_dir(self) -> Path:
        return self.wiki_dir / "concepts"

    @property
    def authors_dir(self) -> Path:
        return self.wiki_dir / "authors"

    @property
    def courses_dir(self) -> Path:
        return self.wiki_dir / "courses"

    @property
    def syntheses_dir(self) -> Path:
        return self.kb_root / "syntheses"

    @property
    def research_dir(self) -> Path:
        return self.wiki_dir / "research"

    @property
    def slides_dir(self) -> Path:
        return self.wiki_dir / "slides"

    @property
    def assets_dir(self) -> Path:
        return self.wiki_dir / "assets"

    @property
    def viz_dir(self) -> Path:
        return self.wiki_dir / "assets" / "viz"

    @property
    def graph_dir(self) -> Path:
        return self.kb_root / "graph"

    @property
    def inbox_dir(self) -> Path:
        return self.kb_root / "inbox"

    @property
    def inbox_processed_dir(self) -> Path:
        return self.kb_root / "inbox" / "processed"

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
