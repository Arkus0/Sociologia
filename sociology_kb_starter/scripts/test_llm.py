"""Quick LLM connectivity test."""
from kb_core.llm import LLMClient

c = LLMClient()
print(f"Provider: {c.provider}")
print(f"Available: {c.available()}")
r = c.complete('Respond with JSON: {"ok": true}', "Test", max_tokens=50)
print(f"Result: {r}")
