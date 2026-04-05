from __future__ import annotations

from pathlib import Path

from kb_core.config import SETTINGS
from kb_core.llm import LLMClient
from kb_core.qa import retrieve_notes
from kb_core.utils import slugify, utc_now_iso, write_text


SLIDES_SYSTEM_PROMPT = """You generate Marp-format slide decks from sociology wiki content.
Output valid Marp markdown. Start with the marp frontmatter block.
Use clear headings, bullet points, and keep each slide focused on one idea.
Cite source notes when referencing specific claims.
"""


def generate_slides(topic_or_query: str, output_name: str | None = None) -> Path:
    """Generate a Marp slide deck from wiki content matching the query."""
    retrieved = retrieve_notes(topic_or_query, top_k=8)
    context = _build_slides_context(retrieved)

    llm = LLMClient()
    if llm.available() and retrieved:
        user_prompt = (
            f"Create a Marp slide deck about: {topic_or_query}\n\n"
            f"Use these wiki sources:\n{context}"
        )
        result = llm.complete(SLIDES_SYSTEM_PROMPT, user_prompt, max_tokens=3000)
        content = result.content if result else _fallback_slides(topic_or_query, retrieved)
    else:
        content = _fallback_slides(topic_or_query, retrieved)

    slug = output_name or slugify(topic_or_query)
    output_path = SETTINGS.slides_dir / f"{slug}.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    write_text(output_path, content)
    return output_path


def slides_from_note(note_path: Path) -> Path:
    """Convert a single wiki article into a Marp slide deck."""
    from kb_core.utils import load_markdown_file

    frontmatter, body = load_markdown_file(note_path)
    title = frontmatter.get("title", note_path.stem)

    llm = LLMClient()
    if llm.available():
        user_prompt = (
            f"Convert this wiki article into a Marp slide deck.\n\n"
            f"Title: {title}\n\n{body}"
        )
        result = llm.complete(SLIDES_SYSTEM_PROMPT, user_prompt, max_tokens=3000)
        content = result.content if result else _fallback_slides_from_body(title, body)
    else:
        content = _fallback_slides_from_body(title, body)

    slug = slugify(title)
    output_path = SETTINGS.slides_dir / f"{slug}.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    write_text(output_path, content)
    return output_path


def _build_slides_context(retrieved: list[dict]) -> str:
    chunks: list[str] = []
    for item in retrieved:
        rel_path = item["path"].relative_to(SETTINGS.kb_root)
        title = item["frontmatter"].get("title", item["path"].stem)
        summary = item["body"][:1200]
        chunks.append(f"### {title} ({rel_path})\n{summary}")
    return "\n\n---\n\n".join(chunks)


def _fallback_slides(topic: str, retrieved: list[dict]) -> str:
    lines = [
        "---",
        "marp: true",
        "theme: default",
        "paginate: true",
        "---",
        "",
        f"# {topic}",
        "",
        f"Generated: {utc_now_iso()}",
        "",
        "---",
        "",
    ]
    for item in retrieved[:6]:
        title = item["frontmatter"].get("title", item["path"].stem)
        summary = item["body"][:400].split("\n")[0]
        lines.extend([
            f"## {title}",
            "",
            summary,
            "",
            "---",
            "",
        ])
    return "\n".join(lines)


def _fallback_slides_from_body(title: str, body: str) -> str:
    lines = [
        "---",
        "marp: true",
        "theme: default",
        "paginate: true",
        "---",
        "",
        f"# {title}",
        "",
        f"Generated: {utc_now_iso()}",
        "",
        "---",
        "",
    ]
    for section in body.split("## ")[1:]:
        heading_line = section.split("\n", 1)
        heading = heading_line[0].strip()
        content = heading_line[1].strip()[:500] if len(heading_line) > 1 else ""
        lines.extend([
            f"## {heading}",
            "",
            content,
            "",
            "---",
            "",
        ])
    return "\n".join(lines)
