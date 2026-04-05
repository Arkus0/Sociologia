from __future__ import annotations

from pathlib import Path

import pytest

from kb_core.storage import ensure_project_dirs


def test_generate_concept_map(kb_tmp: Path):
    """Concept map generates a PNG file."""
    ensure_project_dirs()
    pytest.importorskip("matplotlib")
    from kb_core.viz import generate_concept_map
    output = generate_concept_map(["anomie", "solidarity"])
    assert output.exists()
    assert output.suffix == ".png"


def test_generate_timeline(kb_tmp: Path):
    """Timeline generates a PNG file."""
    ensure_project_dirs()
    pytest.importorskip("matplotlib")
    from kb_core.viz import generate_timeline
    events = [
        {"year": "1893", "label": "Division of Labour"},
        {"year": "1897", "label": "Suicide"},
    ]
    output = generate_timeline(events, output_name="durkheim")
    assert output.exists()
    assert output.suffix == ".png"


def test_generate_statistics(kb_tmp: Path):
    """Statistics chart generates a PNG file."""
    ensure_project_dirs()
    pytest.importorskip("matplotlib")
    from kb_core.viz import generate_statistics
    data = {
        "title": "Notes per Course",
        "values": {"teoria": 5, "metodos": 3, "estadistica": 2},
        "xlabel": "Count",
    }
    output = generate_statistics(data, output_name="course-stats")
    assert output.exists()
    assert output.suffix == ".png"
