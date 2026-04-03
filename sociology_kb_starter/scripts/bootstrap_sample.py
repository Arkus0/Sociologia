from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from kb_core.compiler import compile_all_raw_documents
from kb_core.storage import ensure_project_dirs, save_uploaded_bytes


SAMPLE_TEXT = """# Durkheim, anomie and social integration

Émile Durkheim develops a sociological explanation of social order by focusing on the strength of norms, institutions and forms of solidarity.

Anomie refers to a state of normlessness or weakened regulation. It becomes especially relevant when rapid social change disrupts the moral framework that orients individuals.

Social integration refers to the degree to which individuals are connected to groups, collective beliefs and social life. In Durkheim's work, low integration and low regulation can both become pathological under certain conditions.

These ideas matter not only for classical theory but also for contemporary sociology of crisis, precarity and fragmentation.
"""


if __name__ == "__main__":
    ensure_project_dirs()
    save_uploaded_bytes(
        filename="durkheim-anomie.md",
        content=SAMPLE_TEXT.encode("utf-8"),
        semester="2026-S1",
        course="teoria-sociologica",
        extra_metadata={
            "manual_concepts": ["anomie", "social integration", "solidarity"],
            "manual_authors": ["Émile Durkheim"],
        },
    )
    compile_all_raw_documents()
    print("Sample content bootstrapped.")
