from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import json
import re
import unicodedata
from typing import Any

import yaml


FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?(.*)$", re.DOTALL)
WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def slugify(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9\s_-]", "", value)
    value = re.sub(r"\s+", "-", value)
    value = re.sub(r"-+", "-", value)
    return value.strip("-") or "untitled"


def normalize_text(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value or "")
    return "".join(char for char in normalized if not unicodedata.combining(char)).strip().lower()


def wikilink(slug_or_name: str, display: str | None = None) -> str:
    slug = slugify(slug_or_name)
    if display and slugify(display) != slug:
        return f"[[{slug}|{display}]]"
    return f"[[{slug}]]"


def wikilinks_list(items: list[str]) -> str:
    return ", ".join(wikilink(item, item) for item in items) if items else ""


def extract_wikilinks(text: str) -> list[str]:
    return [m.group(1) for m in WIKILINK_RE.finditer(text)]


def _first_meaningful_block(body: str) -> str:
    for block in re.split(r"\n\s*\n", body):
        lines = [line for line in block.strip().splitlines() if line.strip()]
        while lines and lines[0].lstrip().startswith("#"):
            lines.pop(0)
        stripped = "\n".join(lines).strip()
        if not stripped:
            continue
        return stripped
    return ""


def extract_alias_target(body: str) -> str | None:
    canonical_section_match = re.search(
        r"^##\s+(Canonical note|Nota can[oó]nica)\s*$\n?([\s\S]*?)(?=^##\s+|(?![\s\S]))",
        body,
        re.IGNORECASE | re.MULTILINE,
    )
    if canonical_section_match:
        scoped_links = extract_wikilinks(canonical_section_match.group(2))
        if scoped_links:
            return scoped_links[0].split("|", 1)[0].strip()

    first_block = _first_meaningful_block(body)
    if not first_block:
        return None

    scoped_links = extract_wikilinks(first_block)
    if not scoped_links:
        return None

    normalized_block = normalize_text(first_block)
    is_alias_block = normalized_block.startswith("vease [[") or "entrada canonica es [[" in normalized_block
    if not is_alias_block and not re.search(r"canonical note[\s\S]{0,120}\bis\s+\[\[", normalized_block):
        return None

    return scoped_links[0].split("|", 1)[0].strip() or None


def normalize_markdown_text(content: str) -> str:
    return content.replace("\ufeff", "", 1).replace("\r\n", "\n").replace("\r", "\n")


def read_text(path: Path) -> str:
    return normalize_markdown_text(path.read_text(encoding="utf-8-sig"))


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def to_markdown(frontmatter: dict[str, Any], body: str) -> str:
    front = yaml.safe_dump(frontmatter, allow_unicode=True, sort_keys=False).strip()
    return f"---\n{front}\n---\n\n{body.strip()}\n"


def from_markdown(content: str) -> tuple[dict[str, Any], str]:
    match = FRONTMATTER_RE.match(normalize_markdown_text(content))
    if not match:
        return {}, content
    frontmatter = yaml.safe_load(match.group(1)) or {}
    body = match.group(2).strip()
    return frontmatter, body


def load_markdown_file(path: Path) -> tuple[dict[str, Any], str]:
    return from_markdown(read_text(path))


def save_markdown_file(path: Path, frontmatter: dict[str, Any], body: str) -> None:
    write_text(path, to_markdown(frontmatter, body))


def list_files_recursive(path: Path, suffixes: tuple[str, ...] | None = None) -> list[Path]:
    if not path.exists():
        return []
    files = [p for p in path.rglob("*") if p.is_file()]
    if suffixes:
        return [p for p in files if p.suffix.lower() in suffixes]
    return files
