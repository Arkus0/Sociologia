from __future__ import annotations

from pathlib import Path
from unittest.mock import MagicMock, patch

import numpy as np
import pytest

from kb_core.storage import ensure_project_dirs, write_note


def _seed_wiki(kb_tmp: Path):
    """Create a few notes for embedding tests."""
    from kb_core.config import SETTINGS

    ensure_project_dirs()
    note_dir = SETTINGS.sources_dir / "2026-s1" / "teoria"
    note_dir.mkdir(parents=True, exist_ok=True)
    for i, (title, body) in enumerate([
        ("Durkheim on Solidarity", "## Summary\nSocial solidarity mechanical and organic forms."),
        ("Weber and Bureaucracy", "## Summary\nBureaucracy as rational-legal authority."),
        ("Marx on Alienation", "## Summary\nAlienation of labour under capitalism."),
    ]):
        slug = title.lower().replace(" ", "-")
        write_note(
            note_dir / f"{slug}.md",
            {"id": slug, "title": title, "note_type": "source", "semester": "2026-S1",
             "course": "teoria", "concepts": [title.split()[-1].lower()], "authors": [title.split()[0]]},
            f"# {title}\n\n{body}",
        )


def test_embedding_index_build_and_query(kb_tmp: Path):
    """EmbeddingIndex builds and queries with a mocked OpenAI client."""
    _seed_wiki(kb_tmp)

    from kb_core.embeddings import EmbeddingIndex

    dim = 8
    fake_embeddings = [
        np.random.randn(dim).astype(np.float32).tolist(),
        np.random.randn(dim).astype(np.float32).tolist(),
        np.random.randn(dim).astype(np.float32).tolist(),
    ]

    def mock_create(**kwargs):
        texts = kwargs.get("input", [])
        items = []
        for i, _ in enumerate(texts):
            item = MagicMock()
            item.embedding = fake_embeddings[i] if i < len(fake_embeddings) else np.random.randn(dim).tolist()
            items.append(item)
        resp = MagicMock()
        resp.data = items
        return resp

    mock_client = MagicMock()
    mock_client.embeddings.create = mock_create

    with patch("kb_core.embeddings._get_openai_client", return_value=mock_client), \
         patch("kb_core.embeddings.SETTINGS") as mock_settings:
        mock_settings.openai_api_key = "test-key"
        mock_settings.embedding_model = "text-embedding-3-small"
        mock_settings.embedding_dimensions = dim
        mock_settings.graph_dir = kb_tmp / "graph"
        mock_settings.sources_dir = kb_tmp / "wiki" / "sources"
        mock_settings.concepts_dir = kb_tmp / "wiki" / "concepts"
        mock_settings.authors_dir = kb_tmp / "wiki" / "authors"
        mock_settings.courses_dir = kb_tmp / "wiki" / "courses"
        mock_settings.research_dir = kb_tmp / "wiki" / "research"
        mock_settings.slides_dir = kb_tmp / "wiki" / "slides"
        mock_settings.kb_root = kb_tmp

        idx = EmbeddingIndex()
        count = idx.build()
        assert count == 3
        assert idx.available

        # Query
        results = idx.query("solidarity social", top_k=2)
        assert len(results) <= 2
        assert all("score" in r for r in results)


def test_embedding_index_graceful_no_key(kb_tmp: Path):
    """EmbeddingIndex returns 0 if no OpenAI key is set."""
    from kb_core.embeddings import EmbeddingIndex

    with patch("kb_core.embeddings._get_openai_client", return_value=None):
        idx = EmbeddingIndex()
        assert idx.build() == 0
        assert not idx.available
        assert idx.query("test") == []


def test_embedding_index_load_missing(kb_tmp: Path):
    """EmbeddingIndex.load returns False when files don't exist."""
    from kb_core.embeddings import EmbeddingIndex

    idx = EmbeddingIndex()
    assert idx.load() is False
    assert not idx.available
