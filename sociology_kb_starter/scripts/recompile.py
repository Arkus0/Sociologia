"""Reset all documents to compile_pending and recompile with Groq."""
from kb_core.storage import mark_compile_pending, list_raw_documents
from kb_core.ingest import compile_batch

docs = list_raw_documents()
paths = []
for doc in docs:
    name = doc["path"].name
    status = doc["metadata"].get("status", "?")
    print(f"  {name}: {status} -> compile_pending")
    mark_compile_pending(doc["path"])
    paths.append(doc["path"])

print(f"\nRecompiling {len(paths)} documents with Groq...\n")
results = compile_batch(paths)
for r in results:
    status = "OK" if r.ok else "FAIL"
    provider = getattr(r, "llm_provider", "?")
    print(f"  [{status}] {r.raw_path} (provider={provider})")

ok = sum(1 for r in results if r.ok)
print(f"\nDone: {ok}/{len(results)} compiled successfully.")
