"""Debug: test what Groq actually returns for one document."""
import json
from kb_core.extraction import extract_text
from kb_core.llm import LLMClient
from kb_core.config import SETTINGS
from pathlib import Path

raw_path = SETTINGS.raw_dir / "2026-s1" / "introduccion-a-la-sociologia" / "Modulo fundadores.pdf"
print(f"Extracting text from: {raw_path.name}")

extraction = extract_text(raw_path)
print(f"Extraction status: {extraction.status}")
print(f"Text length: {len(extraction.text)}")
print(f"First 500 chars:\n---\n{extraction.text[:500]}\n---\n")

SOURCE_PROMPT = """You are compiling a sociology knowledge base.
Return strict JSON with keys: title, summary, core_ideas, concepts, authors, methods, exam_questions, open_questions, source_anchors.
Rules:
- Be conservative and grounded in the source text.
- Do not invent references or page numbers.
- Keep unknown fields short.
"""

payload = {
    "source_path": str(raw_path.relative_to(SETTINGS.kb_root)),
    "semester": "2026-S1",
    "course": "Introduccion a la sociologia",
    "filename": raw_path.name,
    "text_excerpt": extraction.text[:12000],
}

llm = LLMClient()
print(f"\nLLM available: {llm.available()}")
print(f"Sending to LLM (payload text_excerpt length: {len(payload['text_excerpt'])} chars)...")

result = llm.complete(SOURCE_PROMPT, json.dumps(payload, ensure_ascii=False, indent=2), max_tokens=2000)
print(f"\nLLM response (provider={result.provider}, model={result.model}):")
print(f"Content length: {len(result.content)}")
print(f"Content:\n---\n{result.content[:2000]}\n---")

# Try to parse
try:
    parsed = json.loads(result.content)
    print("\nJSON parse: SUCCESS")
    print(f"Keys: {list(parsed.keys())}")
except json.JSONDecodeError as e:
    print(f"\nJSON parse: FAILED - {e}")
