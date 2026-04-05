from __future__ import annotations

import argparse
import json
import math
import sys
from collections import Counter
from pathlib import Path

from kb_core.config import SETTINGS
from kb_core.utils import list_files_recursive, load_markdown_file, slugify, write_json

TOKEN_RE_PATTERN = r"[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ0-9]{2,}"
import re
TOKEN_RE = re.compile(TOKEN_RE_PATTERN)
import unicodedata

FIELD_WEIGHTS = {
    "title": 4.0,
    "concepts": 3.0,
    "authors": 3.0,
    "summary": 2.0,
    "body": 1.0,
}


class SearchEngine:
    """Full-text search over all wiki notes with filtering and snippet extraction."""

    def __init__(self) -> None:
        self.docs: list[dict] = []
        self.doc_freq: Counter = Counter()
        self.tokenized_docs: list[tuple[dict, dict[str, Counter]]] = []
        self._loaded = False

    def load(self) -> None:
        """Load and tokenize all wiki notes."""
        self.docs = []
        self.doc_freq = Counter()
        self.tokenized_docs = []

        wiki_dirs = [
            SETTINGS.sources_dir,
            SETTINGS.concepts_dir,
            SETTINGS.authors_dir,
            SETTINGS.courses_dir,
        ]
        for extra in [SETTINGS.research_dir, SETTINGS.slides_dir]:
            if extra.exists():
                wiki_dirs.append(extra)

        for base_dir in wiki_dirs:
            for path in list_files_recursive(base_dir, suffixes=(".md",)):
                frontmatter, body = load_markdown_file(path)
                fields = {
                    "title": frontmatter.get("title", ""),
                    "concepts": " ".join(str(c) for c in frontmatter.get("concepts", [])),
                    "authors": " ".join(str(a) for a in frontmatter.get("authors", [])),
                    "summary": _extract_summary(body),
                    "body": body,
                }
                self.docs.append({
                    "path": path,
                    "frontmatter": frontmatter,
                    "body": body,
                    "fields": fields,
                })

        for doc in self.docs:
            field_tokens = {name: Counter(_tokenize(text)) for name, text in doc["fields"].items()}
            merged = set().union(*(counter.keys() for counter in field_tokens.values()))
            for token in merged:
                self.doc_freq[token] += 1
            self.tokenized_docs.append((doc, field_tokens))

        self._loaded = True

    def search(
        self,
        query: str,
        top_k: int = 10,
        note_type: str | None = None,
        semester: str | None = None,
        course: str | None = None,
        author: str | None = None,
        concept: str | None = None,
    ) -> list[dict]:
        """Search with optional filters. Returns scored results with snippets."""
        if not self._loaded:
            self.load()

        query_tokens = _tokenize(query)
        if not query_tokens:
            return []

        total_docs = max(len(self.tokenized_docs), 1)
        scored: list[dict] = []

        for doc, field_tokens in self.tokenized_docs:
            front = doc["frontmatter"]

            if note_type and front.get("note_type") != note_type:
                continue
            if semester and front.get("semester") != semester:
                continue
            if course and str(front.get("course", "")).lower() != course.lower():
                continue
            if author:
                doc_authors = {str(a).lower() for a in front.get("authors", [])}
                if author.lower() not in doc_authors:
                    continue
            if concept:
                doc_concepts = {str(c).lower() for c in front.get("concepts", [])}
                if concept.lower() not in doc_concepts:
                    continue

            score = 0.0
            for token in query_tokens:
                idf = math.log((1 + total_docs) / (1 + self.doc_freq[token])) + 1.0
                for field_name, counter in field_tokens.items():
                    tf = counter.get(token, 0)
                    if tf:
                        score += FIELD_WEIGHTS[field_name] * (1 + math.log(tf)) * idf

            if score > 0:
                snippet = _extract_snippet(doc["body"], query_tokens)
                scored.append({
                    "path": str(doc["path"].relative_to(SETTINGS.kb_root)),
                    "id": front.get("id", doc["path"].stem),
                    "title": front.get("title", doc["path"].stem),
                    "note_type": front.get("note_type", "unknown"),
                    "course": front.get("course", ""),
                    "semester": front.get("semester", ""),
                    "score": round(score, 3),
                    "snippet": snippet,
                })

        scored.sort(key=lambda item: item["score"], reverse=True)
        return scored[:top_k]

    def build_index(self) -> Path:
        """Precompute and save search index for faster queries."""
        if not self._loaded:
            self.load()

        index_data = {
            "doc_count": len(self.docs),
            "doc_freq": dict(self.doc_freq.most_common(500)),
            "docs": [
                {
                    "path": str(doc["path"].relative_to(SETTINGS.kb_root)),
                    "id": doc["frontmatter"].get("id", doc["path"].stem),
                    "title": doc["frontmatter"].get("title", doc["path"].stem),
                    "note_type": doc["frontmatter"].get("note_type", "unknown"),
                }
                for doc in self.docs
            ],
        }
        index_path = SETTINGS.graph_dir / "search_index.json"
        index_path.parent.mkdir(parents=True, exist_ok=True)
        write_json(index_path, index_data)
        return index_path


def _normalize(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text or "")
    return "".join(char for char in normalized if not unicodedata.combining(char)).lower()


def _tokenize(text: str) -> list[str]:
    return TOKEN_RE.findall(_normalize(text))


def _extract_summary(body: str) -> str:
    if "## Summary" not in body:
        return ""
    fragment = body.split("## Summary", 1)[1]
    if "## " in fragment:
        fragment = fragment.split("## ", 1)[0]
    return fragment


def _extract_snippet(body: str, query_tokens: list[str], max_len: int = 200) -> str:
    """Extract best matching snippet from body text."""
    normalized = _normalize(body)
    best_pos = 0
    best_score = 0
    words = normalized.split()
    for i, word in enumerate(words):
        window = " ".join(words[max(0, i - 10):i + 10])
        score = sum(1 for t in query_tokens if t in window)
        if score > best_score:
            best_score = score
            best_pos = max(0, i - 10)

    snippet_words = body.split()[best_pos:best_pos + 30]
    snippet = " ".join(snippet_words)[:max_len]
    return snippet.strip() + ("..." if len(snippet) >= max_len else "")


class HybridSearchEngine(SearchEngine):
    """Combines lexical TF-IDF search with semantic embedding search via Reciprocal Rank Fusion."""

    RRF_K = 60  # standard RRF constant

    def __init__(self) -> None:
        super().__init__()
        self._embedding_index = None

    def _ensure_embeddings(self):
        if self._embedding_index is not None:
            return
        from kb_core.embeddings import EmbeddingIndex

        self._embedding_index = EmbeddingIndex()
        self._embedding_index.load()

    def search(
        self,
        query: str,
        top_k: int = 10,
        note_type: str | None = None,
        semester: str | None = None,
        course: str | None = None,
        author: str | None = None,
        concept: str | None = None,
    ) -> list[dict]:
        # Lexical results from the parent class
        lexical_results = super().search(
            query, top_k=top_k * 3, note_type=note_type, semester=semester,
            course=course, author=author, concept=concept,
        )

        # Try semantic results
        self._ensure_embeddings()
        if self._embedding_index is None or not self._embedding_index.available:
            return lexical_results[:top_k]

        semantic_results = self._embedding_index.query(
            query, top_k=top_k * 3,
            note_type=note_type, semester=semester, course=course,
        )

        # Reciprocal Rank Fusion
        rrf_scores: dict[str, float] = {}
        result_map: dict[str, dict] = {}

        for rank, item in enumerate(lexical_results):
            key = item["path"]
            rrf_scores[key] = rrf_scores.get(key, 0.0) + 1.0 / (self.RRF_K + rank + 1)
            result_map[key] = item

        for rank, item in enumerate(semantic_results):
            key = item["path"]
            rrf_scores[key] = rrf_scores.get(key, 0.0) + 1.0 / (self.RRF_K + rank + 1)
            if key not in result_map:
                # Semantic-only result — needs a snippet
                result_map[key] = item
                result_map[key].setdefault("snippet", "")

        # Sort by fused score and apply author/concept filters for semantic-only results
        fused = sorted(rrf_scores.items(), key=lambda kv: kv[1], reverse=True)
        final: list[dict] = []
        for path, score in fused:
            item = result_map[path]
            item["score"] = round(score, 6)
            final.append(item)
            if len(final) >= top_k:
                break

        return final

    def build_index(self) -> Path:
        """Build both lexical and embedding indexes."""
        path = super().build_index()
        try:
            self._ensure_embeddings()
            if self._embedding_index is not None:
                self._embedding_index.build()
        except Exception as exc:
            import logging
            logging.getLogger(__name__).warning("Embedding build failed (lexical index still OK): %s", exc)
        return path


def main() -> None:
    parser = argparse.ArgumentParser(description="Search the sociology knowledge base")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--top-k", type=int, default=10, help="Number of results")
    parser.add_argument("--note-type", help="Filter by note type")
    parser.add_argument("--semester", help="Filter by semester")
    parser.add_argument("--course", help="Filter by course")
    parser.add_argument("--author", help="Filter by author")
    parser.add_argument("--concept", help="Filter by concept")
    parser.add_argument("--format", choices=["json", "text"], default="text", help="Output format")
    parser.add_argument("--build-index", action="store_true", help="Build search index and exit")
    parser.add_argument("--lexical-only", action="store_true", help="Skip embeddings, use lexical search only")
    args = parser.parse_args()

    if args.lexical_only:
        engine = SearchEngine()
    else:
        engine = HybridSearchEngine()

    if args.build_index:
        path = engine.build_index()
        print(f"Search index written to {path}")
        return

    results = engine.search(
        args.query,
        top_k=args.top_k,
        note_type=args.note_type,
        semester=args.semester,
        course=args.course,
        author=args.author,
        concept=args.concept,
    )

    if args.format == "json":
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        if not results:
            print("No results found.")
            return
        for r in results:
            print(f"[{r['score']:.1f}] {r['title']} ({r['note_type']}) — {r['path']}")
            if r.get("snippet"):
                print(f"  {r['snippet']}")
            print()


if __name__ == "__main__":
    main()
