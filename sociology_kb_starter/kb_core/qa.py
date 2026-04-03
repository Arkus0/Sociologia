from __future__ import annotations

from collections import Counter
import re

from kb_core.config import SETTINGS
from kb_core.llm import LLMClient
from kb_core.utils import list_files_recursive, load_markdown_file, slugify, utc_now_iso, write_text


TOKEN_RE = re.compile(r"[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ0-9]{3,}")


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
    query_tokens = Counter(_tokenize(query))
    scored: list[tuple[int, dict]] = []
    for path in list_files_recursive(SETTINGS.wiki_dir, suffixes=(".md",)):
        frontmatter, body = load_markdown_file(path)
        haystack = " ".join([
            frontmatter.get("title", ""),
            frontmatter.get("course", ""),
            frontmatter.get("semester", ""),
            " ".join(frontmatter.get("concepts", [])),
            " ".join(frontmatter.get("authors", [])),
            body,
        ])
        score = _score(query_tokens, _tokenize(haystack))
        if score > 0:
            scored.append((score, {
                "path": path,
                "frontmatter": frontmatter,
                "body": body,
                "score": score,
            }))
    scored.sort(key=lambda item: item[0], reverse=True)
    return [item[1] for item in scored[:top_k]]


def _tokenize(text: str) -> list[str]:
    return [token.lower() for token in TOKEN_RE.findall(text)]


def _score(query_tokens: Counter, haystack_tokens: list[str]) -> int:
    haystack_counter = Counter(haystack_tokens)
    score = 0
    for token, count in query_tokens.items():
        score += min(count, haystack_counter.get(token, 0))
    return score


def _build_context(retrieved: list[dict]) -> str:
    chunks: list[str] = []
    for item in retrieved:
        rel_path = item["path"].relative_to(SETTINGS.kb_root)
        summary = item["body"][:1600]
        chunks.append(f"PATH: {rel_path}\nTITLE: {item['frontmatter'].get('title', item['path'].stem)}\nCONTENT:\n{summary}")
    return "\n\n---\n\n".join(chunks)


def _fallback_answer(query: str, retrieved: list[dict]) -> str:
    if not retrieved:
        return "No relevant notes were retrieved yet. Ingest and compile more sources first."
    lines = [f"Question: {query}", "", "Best matching notes:"]
    for item in retrieved:
        rel_path = item["path"].relative_to(SETTINGS.kb_root)
        title = item["frontmatter"].get("title", item["path"].stem)
        course = item["frontmatter"].get("course", "unknown course")
        lines.append(f"- {title} [{rel_path}] ({course})")
    lines.append("")
    lines.append("This is a retrieval pack, not a final synthesis, because no LLM provider is configured.")
    return "\n".join(lines)


def _save_answer(query: str, answer: str, retrieved: list[dict], provider: str, model: str) -> None:
    slug = slugify(query)[:80]
    path = SETTINGS.answered_questions_dir / f"{slug}.md"
    citations = "\n".join(f"- {item['path'].relative_to(SETTINGS.kb_root)}" for item in retrieved)
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
