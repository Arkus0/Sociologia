from __future__ import annotations

from pathlib import Path
from typing import Any

from kb_core.config import SETTINGS
from kb_core.utils import list_files_recursive, load_markdown_file, slugify


def generate_concept_map(concepts: list[str], output_name: str | None = None) -> Path:
    """Generate a matplotlib concept relationship diagram and save as PNG."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    SETTINGS.viz_dir.mkdir(parents=True, exist_ok=True)
    slug = output_name or slugify("-".join(concepts[:5]))
    output_path = SETTINGS.viz_dir / f"concept-map-{slug}.png"

    concept_sources: dict[str, list[str]] = {}
    for path in list_files_recursive(SETTINGS.sources_dir, suffixes=(".md",)):
        front, _ = load_markdown_file(path)
        note_concepts = [str(c).lower() for c in front.get("concepts", [])]
        title = front.get("title", path.stem)
        for c in concepts:
            if c.lower() in note_concepts:
                concept_sources.setdefault(c, []).append(title)

    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_title("Concept Map", fontsize=16, fontweight="bold")

    if not concept_sources:
        ax.text(0.5, 0.5, "No connections found", ha="center", va="center", fontsize=14)
    else:
        y_positions = {}
        for i, concept in enumerate(concepts):
            y = 1.0 - (i / max(len(concepts) - 1, 1)) if len(concepts) > 1 else 0.5
            y_positions[concept] = y
            ax.annotate(
                concept, (0.15, y), fontsize=12, fontweight="bold",
                ha="center", va="center",
                bbox=dict(boxstyle="round,pad=0.3", facecolor="#59A14F", alpha=0.7),
            )

        all_sources = sorted({s for sources in concept_sources.values() for s in sources})
        for i, source in enumerate(all_sources[:15]):
            y = 1.0 - (i / max(len(all_sources[:15]) - 1, 1)) if len(all_sources) > 1 else 0.5
            ax.annotate(
                source[:30], (0.85, y), fontsize=9,
                ha="center", va="center",
                bbox=dict(boxstyle="round,pad=0.2", facecolor="#4E79A7", alpha=0.5),
            )
            for concept, sources in concept_sources.items():
                if source in sources and concept in y_positions:
                    ax.annotate(
                        "", xy=(0.7, y), xytext=(0.3, y_positions[concept]),
                        arrowprops=dict(arrowstyle="->", color="gray", alpha=0.5),
                    )

    ax.set_xlim(0, 1)
    ax.set_ylim(-0.1, 1.1)
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return output_path


def generate_timeline(events: list[dict[str, str]], output_name: str | None = None) -> Path:
    """Generate a chronological timeline visualization.
    events: list of {year: str, label: str}"""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    SETTINGS.viz_dir.mkdir(parents=True, exist_ok=True)
    slug = output_name or "timeline"
    output_path = SETTINGS.viz_dir / f"timeline-{slug}.png"

    fig, ax = plt.subplots(figsize=(14, 6))
    ax.set_title("Timeline", fontsize=16, fontweight="bold")

    if not events:
        ax.text(0.5, 0.5, "No events provided", ha="center", va="center", fontsize=14)
    else:
        years = []
        labels = []
        for e in events:
            try:
                years.append(float(e.get("year", 0)))
                labels.append(e.get("label", ""))
            except (ValueError, TypeError):
                continue

        if years:
            ax.scatter(years, [0] * len(years), s=80, c="#E15759", zorder=5)
            for i, (year, label) in enumerate(zip(years, labels)):
                offset = 0.15 if i % 2 == 0 else -0.15
                ax.annotate(
                    f"{label}\n({int(year)})", (year, 0),
                    xytext=(0, 40 if offset > 0 else -40),
                    textcoords="offset points", ha="center", fontsize=8,
                    arrowprops=dict(arrowstyle="-", color="gray"),
                )
            ax.axhline(0, color="gray", linewidth=0.5)
            ax.set_ylim(-1, 1)

    ax.axis("off")
    fig.tight_layout()
    fig.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return output_path


def generate_statistics(data: dict[str, Any], output_name: str | None = None) -> Path:
    """Generate a bar chart from key-value data."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    SETTINGS.viz_dir.mkdir(parents=True, exist_ok=True)
    slug = output_name or "stats"
    output_path = SETTINGS.viz_dir / f"stats-{slug}.png"

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_title(data.get("title", "Statistics"), fontsize=14, fontweight="bold")

    labels = list(data.get("values", {}).keys())
    values = list(data.get("values", {}).values())

    if labels:
        colors = ["#4E79A7", "#59A14F", "#F28E2B", "#E15759", "#76B7B2", "#EDC948"]
        bar_colors = [colors[i % len(colors)] for i in range(len(labels))]
        ax.barh(labels, values, color=bar_colors)
        ax.set_xlabel(data.get("xlabel", "Count"))
    else:
        ax.text(0.5, 0.5, "No data provided", ha="center", va="center", fontsize=14)

    fig.tight_layout()
    fig.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return output_path
