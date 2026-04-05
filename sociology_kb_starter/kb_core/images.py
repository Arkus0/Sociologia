from __future__ import annotations

from pathlib import Path
import re
import urllib.parse
import urllib.request

from kb_core.config import SETTINGS
from kb_core.utils import read_text, slugify, write_text

IMAGE_URL_RE = re.compile(r"!\[([^\]]*)\]\((https?://[^)]+)\)")


def download_article_images(md_path: Path) -> list[Path]:
    """Parse a markdown file for remote image URLs, download them locally,
    and rewrite the markdown to reference local paths."""
    content = read_text(md_path)
    downloaded: list[Path] = []

    def _replace(match: re.Match) -> str:
        alt = match.group(1)
        url = match.group(2)
        try:
            local_path = _download_image(url, md_path.stem)
            downloaded.append(local_path)
            rel = _obsidian_relative(local_path)
            return f"![{alt}]({rel})"
        except Exception:
            return match.group(0)

    new_content = IMAGE_URL_RE.sub(_replace, content)
    if downloaded:
        write_text(md_path, new_content)
    return downloaded


def _download_image(url: str, context_slug: str) -> Path:
    """Download a single image URL to the wiki assets directory."""
    SETTINGS.assets_dir.mkdir(parents=True, exist_ok=True)
    parsed = urllib.parse.urlparse(url)
    filename = Path(parsed.path).name or "image.png"
    safe_name = f"{slugify(context_slug)}-{slugify(Path(filename).stem)}{Path(filename).suffix}"
    target = SETTINGS.assets_dir / safe_name

    if not target.exists():
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            target.write_bytes(resp.read())
    return target


def _obsidian_relative(image_path: Path) -> str:
    """Return an Obsidian-friendly relative path from wiki root."""
    try:
        return str(image_path.relative_to(SETTINGS.wiki_dir)).replace("\\", "/")
    except ValueError:
        return str(image_path.relative_to(SETTINGS.kb_root)).replace("\\", "/")
