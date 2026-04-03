from __future__ import annotations

from pathlib import Path
from typing import Any

import requests

from kb_core.config import SETTINGS
from kb_core.utils import load_markdown_file


NOTION_VERSION = "2022-06-28"


def notion_is_configured() -> bool:
    return bool(SETTINGS.notion_token and SETTINGS.notion_database_id)


def push_note_to_notion(note_path: Path) -> dict[str, Any]:
    if not notion_is_configured():
        return {"ok": False, "message": "Notion is not configured. Fill NOTION_TOKEN and NOTION_DATABASE_ID first."}

    frontmatter, body = load_markdown_file(note_path)
    headers = {
        "Authorization": f"Bearer {SETTINGS.notion_token}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }

    payload = {
        "parent": {"database_id": SETTINGS.notion_database_id},
        "properties": {
            "Name": {"title": [{"text": {"content": frontmatter.get("title", note_path.stem)}}]},
            "Type": {"select": {"name": frontmatter.get("note_type", "unknown")}},
            "Course": {"rich_text": [{"text": {"content": str(frontmatter.get("course", ""))}}]},
            "Semester": {"rich_text": [{"text": {"content": str(frontmatter.get("semester", ""))}}]},
            "SourcePath": {"url": None},
            "Concepts": {"multi_select": [{"name": value[:100]} for value in frontmatter.get("concepts", [])[:20]]},
            "Authors": {"multi_select": [{"name": value[:100]} for value in frontmatter.get("authors", [])[:20]]},
        },
        "children": _markdown_to_notion_blocks(body[:18000]),
    }

    response = requests.post("https://api.notion.com/v1/pages", headers=headers, json=payload, timeout=30)
    if response.ok:
        return {"ok": True, "message": "Note exported to Notion.", "response": response.json()}
    return {"ok": False, "message": response.text}


def _markdown_to_notion_blocks(markdown_text: str) -> list[dict[str, Any]]:
    blocks: list[dict[str, Any]] = []
    for raw_line in markdown_text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith("# "):
            blocks.append(_heading_block("heading_1", line[2:]))
        elif line.startswith("## "):
            blocks.append(_heading_block("heading_2", line[3:]))
        elif line.startswith("- "):
            blocks.append(_bulleted_block(line[2:]))
        else:
            blocks.append(_paragraph_block(line))
        if len(blocks) >= 100:
            break
    return blocks


def _rich_text(content: str) -> list[dict[str, Any]]:
    return [{"type": "text", "text": {"content": content[:2000]}}]


def _heading_block(kind: str, text: str) -> dict[str, Any]:
    return {"object": "block", "type": kind, kind: {"rich_text": _rich_text(text)}}


def _paragraph_block(text: str) -> dict[str, Any]:
    return {"object": "block", "type": "paragraph", "paragraph": {"rich_text": _rich_text(text)}}


def _bulleted_block(text: str) -> dict[str, Any]:
    return {"object": "block", "type": "bulleted_list_item", "bulleted_list_item": {"rich_text": _rich_text(text)}}
