# Session Handout — Sociology LLM Knowledge Base

> Resumen completo de la sesión de implementación del **Karpathy-style LLM Knowledge Base** para la carrera de Sociología.

---

## Qué se construyó

Se transformó el repositorio base `sociology_kb_starter` en un sistema completo de gestión de conocimiento incremental. El concepto central: cada semestre alimenta un **wiki acumulativo** que el LLM compila, indexa, consulta y enriquece automáticamente.

### Ciclo del conocimiento

```
PDF/TXT/MD  →  Ingestión  →  Compilación LLM  →  Wiki (Obsidian)
                                                      ↓
                                              Query / Q&A
                                                      ↓
                                            Respuesta archivada
                                              como nota research
                                                      ↓
                                              Wiki enriquecido ←─┘
```

---

## Módulos nuevos (8)

| Módulo | Qué hace | Uso |
|--------|----------|-----|
| `kb_core/images.py` | Descarga imágenes remotas de artículos markdown, reescribe rutas a locales | `download_article_images(md_path)` |
| `kb_core/ingest.py` | Ingestión masiva de documentos + CLI | `python -m kb_core.ingest ./docs/ --semester 2026-S1 --course teoria` |
| `kb_core/slides.py` | Genera presentaciones Marp desde el wiki | `generate_slides("anomia social")` |
| `kb_core/viz.py` | Genera visualizaciones con matplotlib (mapas conceptuales, timelines, estadísticas) | `generate_concept_map(concepts)` |
| `kb_core/search_engine.py` | Motor de búsqueda híbrido TF-IDF + embeddings (RRF) con filtros y snippets + CLI | `python -m kb_core.search_engine "durkheim" --top-k 5` |
| `kb_core/semesters.py` | Gestión de semestres: inicialización, estadísticas, índice cruzado | `init_semester("2026-S1", ["teoria", "metodos"])` |
| `kb_core/embeddings.py` | Índice de embeddings OpenAI (`text-embedding-3-small`) con numpy, persistido como `.npy` | `EmbeddingIndex().build()` |
| `kb_core/wiki_renderer.py` | Renderizado Wikipedia: resolución de wikilinks, TOC, infobox, breadcrumbs, categorías | `resolve_wikilinks_html(body)` |

---

## Módulos modificados (11)

| Módulo | Cambios principales |
|--------|-------------------|
| `compiler.py` | Genera `[[wikilinks]]` en notas fuente, conceptos y autores. Smart chunking (32k chars head+tail vs antiguo 12k truncation). max_tokens subido a 4000 |
| `extraction.py` | OCR real con Tesseract (`get_textpage_ocr`, spa+eng). Post-procesamiento: limpieza de headers repetidos, unión de guiones, eliminación de números de página sueltos |
| `llm.py` | JSON mode (`response_format`) para Groq y OpenAI. Retry con backoff exponencial (3 intentos, 2s→4s→8s) para rate limits y errores de red |
| `config.py` | Fix modelo OpenAI: `gpt-4.1-mini` (era `gpt-5-mini` que no existe). Properties: `research_dir`, `slides_dir`, `assets_dir`, `viz_dir`. Nuevos settings: `embedding_model`, `embedding_dimensions` |
| `utils.py` | Funciones `wikilink()`, `wikilinks_list()`, `extract_wikilinks()`, regex `WIKILINK_RE` |
| `qa.py` | `file_answer_to_wiki()` — archiva respuestas como notas `research` con wikilinks |
| `lint.py` | Detecta wikilinks rotos, conceptos mencionados sin enlazar, `suggest_new_articles()` |
| `graph_index.py` | Nodos de semestre, aristas cross-semester, notas research, genera `GRAPH.md` (mermaid) |
| `models.py` | Campo `source_url` en `CompiledSourcePayload` |
| `storage.py` | 4 directorios requeridos nuevos |
| `services.py` | 6 funciones nuevas: `file_answer()`, `generate_slides_service()`, `generate_viz_service()`, `get_semester_stats()`, `suggest_articles()`, `rebuild_embeddings()`. Búsqueda usa `HybridSearchEngine` (TF-IDF + embeddings) |
| `mcp_tools.py` | 7 wrappers MCP nuevos con modelos Pydantic |
| `mcp_server.py` | 7 herramientas MCP registradas (17 total) |
| `compiler.py` | Post-compile ahora también reconstruye embedding index (si hay API key OpenAI) |
| `lint.py` | Nuevas reglas RAG-quality: detecta notas sin sección resumen/definición, cursos sin semestre |
| `app.py` | Nueva pestaña **Wiki** (Wikipedia-style browser) junto a Atlas y Studio |

---

## Configuración Obsidian

Se creó `data/.obsidian/` con:

- **`app.json`** — Habilita wikilinks y Marp live preview
- **`community-plugins.json`** — Marp Slides, Dataview, Graph Analysis
- **`graph.json`** — Colores por tipo de nota: source (morado), concept (verde), author (azul), course (naranja), research (rojo)

Para activar: abrir `data/` como vault en Obsidian, instalar los plugins listados desde Community Plugins.

---

## Herramientas MCP (17 total)

### Lectura (10)
1. `kb_search_notes` — Búsqueda híbrida (TF-IDF + embeddings con RRF)
2. `kb_read_note` — Leer nota completa
3. `kb_list_courses` — Listar cursos
4. `kb_list_authors` — Listar autores
5. `kb_list_concepts` — Listar conceptos
6. `kb_get_graph_neighbors` — BFS desde cualquier nodo
7. `kb_get_recent_sources` — Notas más recientes
8. `kb_get_source_provenance` — Cadena raw → compilado
9. `kb_get_semester_stats` — Estadísticas por semestre
10. `kb_suggest_articles` — Sugerir artículos cross-curso

### Escritura (5)
11. `kb_create_pr_for_note_changes` — Ediciones via branch/PR
12. `kb_file_answer` — Archivar respuesta Q&A al wiki
13. `kb_generate_slides` — Generar slide deck Marp
14. `kb_generate_viz` — Generar visualización matplotlib
15. `kb_propose_note_edit` — Proponer edición de nota

### Mantenimiento (2)
16. `kb_ingest_from_inbox` — Escanear inbox e ingestar documentos nuevos
17. `kb_rebuild_embeddings` — Reconstruir índice de embeddings semánticos

---

## Comandos de uso diario

```bash
# Desde sociology_kb_starter/

# 1. Ingestar documentos de un semestre nuevo
python -m kb_core.ingest ./ruta/a/pdfs/ --semester 2026-S1 --course teoria-sociologica

# 2. Compilar todo lo pendiente
python -m kb_core.ingest --compile-pending

# 3. Buscar en el wiki
python -m kb_core.search_engine "solidaridad mecánica" --top-k 10

# 4. Correr tests
python -m pytest tests/ -v

# 5. Iniciar MCP server
python mcp_server.py

# 6. Dashboard Streamlit (Atlas + Wiki + Studio)
streamlit run app.py

# 7. Reconstruir embeddings
python -c "from kb_core.embeddings import EmbeddingIndex; print(EmbeddingIndex().build(), 'docs embedded')"
```

---

## Testing

**41 tests — todos pasando** (`python -m pytest tests/ -v`)

| Archivo | Tests | Cobertura |
|---------|-------|-----------|
| `test_compile_and_qa.py` | 3 | Compilación, Q&A, rebuild indexes |
| `test_extraction.py` | 3 | Extracción PDF/TXT/MD |
| `test_graph_index.py` | 1 | Derivación de grafos |
| `test_metadata_and_storage.py` | 3 | Persistencia y metadatos |
| `test_services_and_mcp_tools.py` | 4 | Integración servicios + MCP |
| `test_ingest.py` | 3 | Scan pending, batch compile, ingest directory |
| `test_semesters.py` | 3 | Init, stats, cross-semester index |
| `test_search_engine.py` | 3 | Build index, search, filters |
| `test_file_answer.py` | 2 | Filing answers, wikilink generation |
| `test_lint_enhanced.py` | 2 | Broken wikilinks, suggestions |
| `test_slides.py` | 1 | Marp slide generation |
| `test_viz.py` | 3 | Concept map, timeline, statistics |
| `test_embeddings.py` | 3 | Build, query, graceful fallback sin API key |
| `test_wiki_renderer.py` | 7 | Wikilinks, TOC, breadcrumbs, infobox, categorías |

---

## Estructura de datos de nota

Cada nota wiki tiene frontmatter YAML:

```yaml
---
id: durkheim-division-trabajo
title: "La División del Trabajo Social"
note_type: source          # source | concept | author | course | research
semester: "2026-S1"
course: teoria-sociologica
source_path: raw/2026-S1/teoria-sociologica/durkheim-division.pdf
compiled_at: "2025-01-15T10:30:00"
concepts:
  - solidaridad-mecanica
  - solidaridad-organica
  - anomia
authors:
  - emile-durkheim
---

## Resumen

Contenido compilado por el LLM con [[solidaridad-mecanica|Solidaridad Mecánica]] y
referencias a [[emile-durkheim|Émile Durkheim]]...
```

---

## Mejoras del pipeline (2026-04-04)

### Problemas corregidos
1. **OCR falso** → OCR real con Tesseract (`get_textpage_ocr`, `language="spa+eng"`, `dpi=300`). Fallback graceful si Tesseract no está instalado.
2. **Texto truncado a 12k chars** → Smart chunking: hasta 32k chars con corte en `[Page N]` markers (head + tail para documentos grandes).
3. **Sin JSON mode** → `response_format={"type": "json_object"}` para Groq y OpenAI. Elimina el parsing frágil de markdown fences.
4. **Sin reintentos** → 3 intentos con backoff exponencial (2s → 4s → 8s) para 429, errores de red y timeouts.
5. **Modelo inexistente** → `gpt-5-mini` corregido a `gpt-4.1-mini` en config.py.
6. **Texto sucio del PDF** → Post-procesamiento: elimina headers/footers repetidos, une guiones de fin de línea, elimina números de página sueltos.

### Notas recompiladas manualmente
Las 5 notas fuente del semestre 2026-S1 fueron recompiladas manualmente (provider: `claude-opus-4-20250514`) porque el pipeline original con `text[:12000]` perdía entre el 81-92% del contenido de los PDFs grandes. Las nuevas notas incluyen todos los conceptos, autores y argumentos del texto completo.

---

## Próximos pasos sugeridos

1. **API key Groq**: Configurar `GROQ_API_KEY` en `.env` (gratis en console.groq.com, ~30 req/min). Es el provider recomendado.
2. **Tesseract OCR** (opcional): Instalar Tesseract si tienes PDFs escaneados. Sin él, la extracción funciona pero sin OCR.
3. **Obsidian**: Abrir `sociology_kb_starter/` como vault e instalar Marp Slides, Dataview, Canvas Watcher.
4. **MCP en ChatGPT Desktop**: Ver sección 12 de `docs/obsidian_quickstart.md`.
5. **Construir embeddings**: Ejecutar `python -c "from kb_core.embeddings import EmbeddingIndex; EmbeddingIndex().build()"` para activar búsqueda semántica (requiere `OPENAI_API_KEY`).
6. **Wiki Streamlit**: Abrir `streamlit run app.py` → pestaña Wiki para navegar artículos estilo Wikipedia.
7. **Workflow reviewed** (futuro): Conectar el campo `reviewed: false` con filtros de búsqueda y herramienta MCP `kb_mark_reviewed`.

---

## Stack técnico

| Componente | Tecnología |
|-----------|-----------|
| Runtime | Python 3.14 |
| Validación | Pydantic v2 |
| LLM | Groq (primary) / OpenAI / Anthropic — JSON mode, retry con backoff |
| PDF Extraction | PyMuPDF + Tesseract OCR (opcional) con post-procesamiento de texto |
| Búsqueda | Híbrida: TF-IDF + embeddings OpenAI (`text-embedding-3-small`) con Reciprocal Rank Fusion |
| Visualización | matplotlib (headless Agg) |
| Presentaciones | Marp (Markdown Presentation) |
| Wiki / IDE | Obsidian |
| Dashboard | Streamlit |
| Integración | MCP (Model Context Protocol) via FastMCP |
| Tests | pytest (41 tests) |
| Notion | API push unidireccional (opcional) |

---

*Generado al cierre de la sesión de implementación.*
