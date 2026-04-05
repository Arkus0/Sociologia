from __future__ import annotations

from collections import Counter
import math
import re
import unicodedata

from kb_core.config import SETTINGS
from kb_core.llm import LLMClient
from kb_core.utils import list_files_recursive, load_markdown_file, save_markdown_file, slugify, utc_now_iso, wikilink, write_text


TOKEN_RE = re.compile(r"[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ0-9]{2,}")
FIELD_WEIGHTS = {
    "title": 4.0,
    "concepts": 3.0,
    "authors": 3.0,
    "summary": 2.0,
    "body": 1.0,
}


def answer_question(query: str, top_k: int = 5) -> dict:
    retrieved = retrieve_notes(query, top_k=top_k)
    llm = LLMClient()
    context = _build_context(retrieved)

    if llm.available() and retrieved:
        system_prompt = (
            "You answer questions against a sociology markdown wiki. "
            "Use only the supplied context. Cite note paths inline in square brackets. "
            "Be explicit when the context is incomplete."
        )
        user_prompt = f"Question:\n{query}\n\nContext:\n{context}"
        result = llm.complete(system_prompt, user_prompt, max_tokens=1200)
        answer = result.content if result else "No answer generated."
        provider = result.provider if result else "none"
        model = result.model if result else "none"
    else:
        answer = _fallback_answer(query, retrieved)
        provider = "fallback"
        model = "fallback"

    _save_answer(query, answer, retrieved, provider, model)
    return {
        "answer": answer,
        "retrieved": retrieved,
        "provider": provider,
        "model": model,
    }


def retrieve_notes(query: str, top_k: int = 5) -> list[dict]:
    query_tokens = _tokenize(query)
    if not query_tokens:
        return []
    all_docs = []
    for path in list_files_recursive(SETTINGS.wiki_dir, suffixes=(".md",)):
        frontmatter, body = load_markdown_file(path)
        fields = {
            "title": frontmatter.get("title", ""),
            "concepts": " ".join(frontmatter.get("concepts", [])),
            "authors": " ".join(frontmatter.get("authors", [])),
            "summary": _extract_summary(body),
            "body": body,
        }
        all_docs.append({"path": path, "frontmatter": frontmatter, "body": body, "fields": fields})

    doc_freq = Counter()
    tokenized_docs: list[tuple[dict, dict[str, Counter]]] = []
    for doc in all_docs:
        field_tokens = {name: Counter(_tokenize(text)) for name, text in doc["fields"].items()}
        merged = set().union(*(counter.keys() for counter in field_tokens.values()))
        for token in merged:
            doc_freq[token] += 1
        tokenized_docs.append((doc, field_tokens))

    total_docs = max(len(tokenized_docs), 1)
    scored: list[dict] = []
    for doc, field_tokens in tokenized_docs:
        score = 0.0
        for token in query_tokens:
            idf = math.log((1 + total_docs) / (1 + doc_freq[token])) + 1.0
            for field_name, counter in field_tokens.items():
                tf = counter.get(token, 0)
                if tf:
                    score += FIELD_WEIGHTS[field_name] * (1 + math.log(tf)) * idf
        if score > 0:
            scored.append(
                {
                    "path": doc["path"],
                    "frontmatter": doc["frontmatter"],
                    "body": doc["body"],
                    "score": round(score, 3),
                }
            )

    scored.sort(key=lambda item: item["score"], reverse=True)
    return scored[:top_k]


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


def _build_context(retrieved: list[dict]) -> str:
    chunks: list[str] = []
    for item in retrieved:
        rel_path = item["path"].relative_to(SETTINGS.kb_root)
        summary = item["body"][:1600]
        chunks.append(f"PATH: {rel_path}\nTITLE: {item['frontmatter'].get('title', item['path'].stem)}\nSCORE: {item['score']}\nCONTENT:\n{summary}")
    return "\n\n---\n\n".join(chunks)


def _fallback_answer(query: str, retrieved: list[dict]) -> str:
    if not retrieved:
        return "No relevant notes were retrieved yet. Ingest and compile more sources first."
    lines = [f"Question: {query}", "", "Best matching notes:"]
    for item in retrieved:
        rel_path = item["path"].relative_to(SETTINGS.kb_root)
        title = item["frontmatter"].get("title", item["path"].stem)
        course = item["frontmatter"].get("course", "unknown course")
        lines.append(f"- {title} [{rel_path}] ({course}) score={item['score']}")
    lines.append("")
    lines.append("This is a retrieval pack, not a final synthesis, because no LLM provider is configured.")
    return "\n".join(lines)


def _save_answer(query: str, answer: str, retrieved: list[dict], provider: str, model: str) -> None:
    slug = slugify(query)[:80]
    path = SETTINGS.answered_questions_dir / f"{slug}.md"
    citations = "\n".join(
        f"- {item['path'].relative_to(SETTINGS.kb_root)} (score={item['score']})" for item in retrieved
    )
    content = f"""# {query}

- answered_at: {utc_now_iso()}
- provider: {provider}
- model: {model}

## Answer
{answer}

## Retrieved notes
{citations or '- None'}
"""
    write_text(path, content)


def file_answer_to_wiki(
    query: str,
    answer: str,
    concepts: list[str] | None = None,
    authors: list[str] | None = None,
    retrieved: list[dict] | None = None,
) -> Path:
    """File a Q&A answer back into the wiki as a research note."""
    slug = slugify(query)[:80]
    note_path = SETTINGS.research_dir / f"{slug}.md"
    note_path.parent.mkdir(parents=True, exist_ok=True)

    concept_list = concepts or []
    author_list = authors or []

    cited_sources = []
    if retrieved:
        for item in retrieved:
            title = item.get("frontmatter", {}).get("title", "")
            if title:
                cited_sources.append(title)

    frontmatter = {
        "id": slug,
        "title": query,
        "note_type": "research",
        "created_at": utc_now_iso(),
        "concepts": concept_list,
        "authors": author_list,
        "tags": list(set(concept_list + author_list)),
        "reviewed": False,
    }

    concept_links = "\n".join(f"- {wikilink(c, c)}" for c in concept_list) if concept_list else "- None"
    author_links = "\n".join(f"- {wikilink(a, a)}" for a in author_list) if author_list else "- None"
    source_links = "\n".join(f"- {wikilink(s, s)}" for s in cited_sources) if cited_sources else "- None"

    body = f"""# {query}

## Answer
{answer}

## Related concepts
{concept_links}

## Related authors
{author_links}

## Cited sources
{source_links}
"""

    save_markdown_file(note_path, frontmatter, body)
    return note_path
