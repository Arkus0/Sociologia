from __future__ import annotations

import json
import logging
from pathlib import Path

import numpy as np

from kb_core.config import SETTINGS
from kb_core.utils import list_files_recursive, load_markdown_file

logger = logging.getLogger(__name__)

_EMBEDDINGS_FILE = "embeddings.npy"
_IDS_FILE = "embedding_ids.json"
_BATCH_SIZE = 64


def _get_openai_client():
    """Return an OpenAI client if the key is configured, else None."""
    if not SETTINGS.openai_api_key:
        return None
    from openai import OpenAI

    return OpenAI(api_key=SETTINGS.openai_api_key)


def _embed_texts(client, texts: list[str]) -> np.ndarray:
    """Call OpenAI embeddings API in batches. Returns (N, dim) array."""
    all_vecs: list[list[float]] = []
    for start in range(0, len(texts), _BATCH_SIZE):
        batch = texts[start : start + _BATCH_SIZE]
        resp = client.embeddings.create(
            input=batch,
            model=SETTINGS.embedding_model,
            dimensions=SETTINGS.embedding_dimensions,
        )
        all_vecs.extend([item.embedding for item in resp.data])
    return np.array(all_vecs, dtype=np.float32)


def _prepare_text(frontmatter: dict, body: str) -> str:
    """Build a single text string from a wiki note for embedding."""
    title = frontmatter.get("title", "")
    concepts = " ".join(str(c) for c in frontmatter.get("concepts", []))
    authors = " ".join(str(a) for a in frontmatter.get("authors", []))
    # Extract summary section if present
    summary = ""
    for marker in ("## Summary", "## Resumen", "## Definición"):
        if marker in body:
            fragment = body.split(marker, 1)[1]
            if "## " in fragment:
                fragment = fragment.split("## ", 1)[0]
            summary = fragment.strip()
            break

    parts = [p for p in [title, concepts, authors, summary, body[:2000]] if p]
    return "\n".join(parts)


class EmbeddingIndex:
    """Lightweight numpy-based embedding index for wiki articles."""

    def __init__(self) -> None:
        self._matrix: np.ndarray | None = None
        self._ids: list[dict] | None = None

    @property
    def _emb_path(self) -> Path:
        return SETTINGS.graph_dir / _EMBEDDINGS_FILE

    @property
    def _ids_path(self) -> Path:
        return SETTINGS.graph_dir / _IDS_FILE

    @property
    def available(self) -> bool:
        return self._matrix is not None and self._ids is not None and len(self._ids) > 0

    def load(self) -> bool:
        """Load persisted embeddings from disk. Returns True if loaded successfully."""
        if self._emb_path.exists() and self._ids_path.exists():
            try:
                self._matrix = np.load(str(self._emb_path))
                self._ids = json.loads(self._ids_path.read_text(encoding="utf-8"))
                if len(self._ids) != self._matrix.shape[0]:
                    logger.warning("Embedding index size mismatch; clearing.")
                    self._matrix = None
                    self._ids = None
                    return False
                return True
            except Exception as exc:
                logger.warning("Failed to load embedding index: %s", exc)
                self._matrix = None
                self._ids = None
        return False

    def build(self) -> int:
        """Build embedding index from all wiki notes. Returns number of docs embedded."""
        client = _get_openai_client()
        if client is None:
            logger.warning("No OpenAI API key configured; skipping embedding build.")
            return 0

        wiki_dirs = [
            SETTINGS.sources_dir,
            SETTINGS.concepts_dir,
            SETTINGS.authors_dir,
            SETTINGS.courses_dir,
        ]
        for extra in [SETTINGS.research_dir, SETTINGS.slides_dir]:
            if extra.exists():
                wiki_dirs.append(extra)

        docs: list[dict] = []
        texts: list[str] = []
        for base_dir in wiki_dirs:
            for path in list_files_recursive(base_dir, suffixes=(".md",)):
                frontmatter, body = load_markdown_file(path)
                text = _prepare_text(frontmatter, body)
                if not text.strip():
                    continue
                docs.append({
                    "path": str(path.relative_to(SETTINGS.kb_root)),
                    "id": frontmatter.get("id", path.stem),
                    "title": frontmatter.get("title", path.stem),
                    "note_type": frontmatter.get("note_type", "unknown"),
                    "course": frontmatter.get("course", ""),
                    "semester": frontmatter.get("semester", ""),
                })
                texts.append(text)

        if not texts:
            logger.warning("No wiki notes found for embedding.")
            return 0

        logger.info("Embedding %d wiki notes with %s...", len(texts), SETTINGS.embedding_model)
        matrix = _embed_texts(client, texts)

        # Normalize for cosine similarity (dot product on unit vectors = cosine)
        norms = np.linalg.norm(matrix, axis=1, keepdims=True)
        norms[norms == 0] = 1.0
        matrix = matrix / norms

        self._matrix = matrix
        self._ids = docs

        # Persist
        SETTINGS.graph_dir.mkdir(parents=True, exist_ok=True)
        np.save(str(self._emb_path), matrix)
        self._ids_path.write_text(
            json.dumps(docs, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        logger.info("Embedding index saved: %d docs, %d dims.", len(docs), matrix.shape[1])
        return len(docs)

    def query(
        self,
        text: str,
        top_k: int = 10,
        note_type: str | None = None,
        semester: str | None = None,
        course: str | None = None,
    ) -> list[dict]:
        """Semantic search by cosine similarity. Returns scored results."""
        if not self.available:
            return []

        client = _get_openai_client()
        if client is None:
            return []

        resp = client.embeddings.create(
            input=[text],
            model=SETTINGS.embedding_model,
            dimensions=SETTINGS.embedding_dimensions,
        )
        query_vec = np.array(resp.data[0].embedding, dtype=np.float32)
        query_vec = query_vec / (np.linalg.norm(query_vec) or 1.0)

        scores = self._matrix @ query_vec  # cosine similarity

        # Apply metadata filters
        mask = np.ones(len(self._ids), dtype=bool)
        for i, doc in enumerate(self._ids):
            if note_type and doc.get("note_type") != note_type:
                mask[i] = False
            if semester and doc.get("semester") != semester:
                mask[i] = False
            if course and str(doc.get("course", "")).lower() != course.lower():
                mask[i] = False

        scores = np.where(mask, scores, -1.0)
        top_indices = np.argsort(scores)[::-1][:top_k]

        results = []
        for idx in top_indices:
            if scores[idx] <= 0:
                break
            doc = self._ids[idx]
            results.append({
                "path": doc["path"],
                "id": doc["id"],
                "title": doc["title"],
                "note_type": doc["note_type"],
                "course": doc.get("course", ""),
                "semester": doc.get("semester", ""),
                "score": float(scores[idx]),
            })
        return results
