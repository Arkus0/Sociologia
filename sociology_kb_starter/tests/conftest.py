from __future__ import annotations

from pathlib import Path
import sys

import pytest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from kb_core.config import SETTINGS
from kb_core.storage import ensure_project_dirs


@pytest.fixture()
def kb_tmp(tmp_path: Path):
    original = SETTINGS.kb_root
    SETTINGS.kb_root = tmp_path / "data"
    ensure_project_dirs()
    # Reset cached hybrid search engine so it doesn't retain docs from prior tests
    import kb_core.services as _svc
    _svc._hybrid_engine = None
    try:
        yield SETTINGS.kb_root
    finally:
        _svc._hybrid_engine = None
        SETTINGS.kb_root = original
