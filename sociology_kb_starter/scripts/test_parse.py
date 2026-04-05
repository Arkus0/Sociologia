"""Quick test of the JSON parsing fix."""
import json
from kb_core.compiler import _parse_compiled_payload
from pathlib import Path

raw = '```json\n{"title": "El pensamiento sociologico", "summary": "Un resumen", "core_ideas": ["idea1"], "concepts": ["positivismo"], "authors": ["Comte"], "methods": [], "exam_questions": [], "open_questions": [], "source_anchors": []}\n```'

result = _parse_compiled_payload(raw, Path("test.pdf"), "fallback text here")
print("title:", result.title)
print("summary:", result.summary)
print("concepts:", result.concepts)
print("authors:", result.authors)
print("Is fallback?", result.title == "Test")
