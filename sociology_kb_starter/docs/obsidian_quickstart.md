# Guía Rápida: Tu Knowledge Base de Sociología en Obsidian

Esta guía te explica paso a paso cómo usar tu base de conocimiento de sociología.
Está pensada para alguien que acaba de instalar Obsidian.

---

## 1. Abrir el vault por primera vez

1. Abre **Obsidian**
2. Clic en **"Open folder as vault"** (Abrir carpeta como vault)
3. Navega hasta `sociology_kb_starter/` y selecciónala
4. Obsidian cargará la carpeta completa como tu vault

> **¿Qué es un vault?** Es simplemente una carpeta que Obsidian trata como tu proyecto. Todo lo que hay dentro (notas, PDFs, configuración) es accesible desde la app.

---

## 2. Estructura de carpetas — qué es cada cosa

```
sociology_kb_starter/          ← Tu vault (raíz)
├── data/
│   ├── raw/                   ← PDFs y archivos originales (no tocar)
│   │   └── {semestre}/{curso}/
│   ├── wiki/                  ← TUS NOTAS (las compiladas por el LLM)
│   │   ├── sources/           ← Notas de cada documento original
│   │   ├── concepts/          ← Páginas de conceptos (ej: [[funcionalismo]])
│   │   ├── authors/           ← Páginas de autores (ej: [[durkheim]])
│   │   ├── courses/           ← Índice por asignatura
│   │   ├── research/          ← Respuestas Q&A archivadas
│   │   └── slides/            ← Presentaciones generadas (Marp)
│   ├── inbox/                 ← ZONA DE ENTREGA: deja aquí tus PDFs nuevos
│   │   └── processed/         ← PDFs ya procesados (se mueven aquí solos)
│   ├── qa/                    ← Preguntas abiertas y respondidas
│   └── graph/                 ← Datos del grafo de conocimiento
├── docs/                      ← Documentación del proyecto
├── kb_core/                   ← Código Python (no necesitas tocarlo)
├── Project.canvas             ← Tablero Kanvas (gestión de tareas)
└── RULES.md                   ← Reglas del flujo de trabajo Kanvas
```

**Lo que más te interesa:** `data/wiki/` para leer tus notas, `data/inbox/` para subir PDFs nuevos.

---

## 3. Navegación básica en Obsidian

### Panel izquierdo: Explorador de archivos
- Navega por carpetas como en un explorador de Windows
- Haz clic en cualquier `.md` para abrirlo
- Empieza por `data/wiki/sources/` para ver tus notas compiladas

### Atajos imprescindibles

| Atajo | Qué hace |
|-------|----------|
| `Ctrl + O` | **Quick Switcher** — busca cualquier nota por nombre (el más útil) |
| `Ctrl + Shift + F` | Búsqueda global en todo el vault |
| `Ctrl + G` | **Graph view** — grafo visual de tus notas y conexiones |
| `Ctrl + P` | Paleta de comandos (como VS Code) |
| `Ctrl + E` | Alternar entre modo edición y lectura |
| `Ctrl + Click` | Seguir un enlace (wikilink) |

### Paneles útiles

- **Backlinks** (panel derecho): muestra qué otras notas enlazan a la nota actual
- **Outline** (panel derecho): tabla de contenidos de la nota actual
- Para activarlos: `Ctrl + P` → busca "Backlinks" o "Outline" → "Toggle"

---

## 4. Wikilinks: cómo funcionan las conexiones

Tus notas están llenas de enlaces como `[[funcionalismo]]` o `[[durkheim]]`. Esto es un **wikilink** — un enlace interno entre notas.

- **Clic** en un wikilink → te lleva a esa nota
- **Hover** sobre un wikilink → vista previa rápida
- **Backlinks** → ves desde qué notas se referencia un concepto o autor

Esto es lo que hace que el grafo funcione: cada wikilink es una conexión.

### Ejemplo de flujo de lectura:
1. Abres una nota fuente en `sources/`
2. Ves el concepto `[[capital-social]]` mencionado
3. Haces clic → te lleva a la página del concepto
4. Ahí ves TODAS las fuentes que mencionan capital social
5. Descubres conexiones entre asignaturas que no habías visto

---

## 5. Graph view: el grafo de conocimiento

Pulsa `Ctrl + G` para abrir el grafo. Verás tus notas como nodos y los wikilinks como líneas.

- **Nodos grandes** = notas con muchas conexiones (conceptos clave)
- **Clusters** = grupos de notas muy interrelacionadas (suelen ser de la misma asignatura)
- **Nodos aislados** = notas sin conexiones (posibles huecos en el KB)

### Filtros del grafo:
- En la barra lateral del grafo puedes filtrar por tipo (`source`, `concept`, `author`)
- Puedes buscar nodos específicos con la barra de búsqueda

---

## 6. Frontmatter: metadatos de cada nota

Al abrir una nota, verás un bloque YAML al inicio entre `---`:

```yaml
---
id: durkheim-division-trabajo
title: "La División del Trabajo Social"
note_type: source
semester: 2026-S1
course: teoria-sociologica
concepts:
  - solidaridad-mecanica
  - solidaridad-organica
authors:
  - durkheim
compiled_at: "2026-04-01T10:30:00Z"
reviewed: false
---
```

**No edites el frontmatter manualmente.** Es generado automáticamente por el sistema. Si necesitas cambiar algo, usa las herramientas MCP o el Streamlit.

---

## 7. Flujo diario de trabajo

### Subir PDFs nuevos (automático)

1. **Crea subcarpetas** en `data/inbox/` con la estructura `{semestre}/{curso}/`:
   ```
   data/inbox/2026-S1/teoria-sociologica/
   data/inbox/2026-S1/metodologia/
   ```
2. **Arrastra o copia** tus PDFs a la carpeta correspondiente
3. **Arranca el watcher** (si no está corriendo):
   ```bash
   cd sociology_kb_starter
   python -m kb_core.watcher
   ```
4. El watcher detectará los PDFs, los procesará automáticamente y los moverá a `inbox/processed/`
5. Las notas compiladas aparecerán en `data/wiki/sources/{semestre}/{curso}/`

> **Opción rápida** (sin watcher): `python -m kb_core.watcher --once` procesa todo lo que haya en inbox y sale.

### Explorar tu conocimiento

1. Abre Obsidian → `Ctrl + G` para el grafo
2. O `Ctrl + O` → escribe el nombre de un concepto o autor
3. Lee notas fuente → sigue wikilinks → descubre conexiones
4. Usa el panel de backlinks para ver qué más referencia un tema

### Hacer preguntas

Via el servidor MCP (Claude Desktop, ChatGPT, etc.):
- Buscar notas: *"busca notas sobre funcionalismo"*
- Leer una nota: *"lee la nota de Durkheim"*
- Archivar respuestas: *"archiva esta respuesta sobre capital social"*
- Generar slides: *"genera presentación sobre teorías clásicas"*

---

## 8. Kanvas: gestión visual de tareas

Tu proyecto incluye **Kanvas**, un sistema de gestión de tareas visual.

### Abrir el tablero
1. En Obsidian, busca `Project.canvas` en el explorador de archivos
2. Haz doble clic para abrirlo

### Colores de las tarjetas

| Color | Estado | Quién |
|-------|--------|-------|
| 🟣 Morado | Propuesta | Agente IA |
| 🔴 Rojo | Por hacer | Tú |
| 🟠 Naranja | En progreso | Tú o agente |
| 🔵 Cian | En revisión | Agente IA |
| 🟢 Verde | Hecho | Tú |
| ⬜ Gris | Bloqueada | Automático |

### Flujo de uso
1. Abre el tablero → revisa tareas propuestas (moradas)
2. Aprueba las que quieras hacer (cambia a rojo)
3. Empieza una tarea (cambia a naranja)
4. Al terminar marca para revisión (cian) o directamente hecho (verde)
5. Las flechas entre tarjetas indican dependencias

### CLI de Kanvas (para agentes IA)
```bash
python canvas-tool.py "Project.canvas" status    # Ver estado del tablero
python canvas-tool.py "Project.canvas" ready      # Tareas listas para empezar
python canvas-tool.py "Project.canvas" list       # Listar todas las tareas
```

---

## 9. Plugins recomendados

Estos ya están preconfigurados en tu vault:

| Plugin | Para qué |
|--------|----------|
| **Canvas** | Tablero visual de Kanvas (core plugin, ya activo) |
| **Graph view** | Visualizar el grafo de conocimiento (ya activo) |
| **Backlinks** | Ver qué notas referencian la actual (ya activo) |
| **Marp Slides** | Ver presentaciones generadas directamente en Obsidian |
| **Dataview** | Consultas dinámicas sobre tus notas |
| **Canvas Watcher** | Sincroniza estados de Kanvas automáticamente |

Para activar/desactivar: `Settings → Community plugins`

---

## 10. Comandos útiles del proyecto

```bash
# Arrancar el watcher de inbox (deja corriendo en segundo plano)
python -m kb_core.watcher

# Procesar inbox una vez y salir
python -m kb_core.watcher --once

# Ingestar un directorio manualmente
python -m kb_core.ingest ./mis-pdfs/ --semester 2026-S1 --course teoria

# Compilar documentos pendientes
python -m kb_core.ingest --compile-pending

# Buscar en la KB
python -m kb_core.search_engine "funcionalismo"

# Arrancar el dashboard web
streamlit run app.py

# Arrancar servidor MCP — modo HTTP (browser, Streamlit)
python mcp_server.py

# Arrancar servidor MCP — modo stdio (ChatGPT Desktop, Claude Desktop)
python mcp_server.py --stdio

# Correr tests
python -m pytest tests/ -v
```

---

## 11. Configuración inicial (.env)

Antes de compilar PDFs, necesitas configurar tu proveedor LLM. Copia `.env.example` a `.env`:

```bash
copy .env.example .env
```

Edita `.env` y configura al menos UN proveedor:

```env
# Recomendado: Groq (gratis, muy rápido)
LLM_PROVIDER=groq
GROQ_API_KEY=tu-api-key-aqui

# Alternativa: OpenAI
# LLM_PROVIDER=openai
# OPENAI_API_KEY=tu-api-key

# Alternativa: Anthropic (Claude)
# LLM_PROVIDER=anthropic
# ANTHROPIC_API_KEY=tu-api-key
```

**¿Dónde conseguir un API key de Groq?** → [console.groq.com](https://console.groq.com) — es gratis con límite de ~30 peticiones/minuto.

---

## 12. Conectar ChatGPT Desktop al servidor MCP

ChatGPT Desktop puede usar las herramientas de tu KB de sociología directamente via MCP.

### Paso 1: Instalar ChatGPT Desktop
Descárgalo desde [chatgpt.com/desktop](https://chatgpt.com/desktop) si aún no lo tienes.

### Paso 2: Configurar el servidor MCP
1. Abre **ChatGPT Desktop**
2. Ve a **Settings** (⚙️) → **MCP Servers** → **Add Server**
3. Configura con estos datos:
   - **Name:** `sociology-kb`
   - **Command:** `C:\Python314\python.exe`
   - **Arguments:** `mcp_server.py --stdio`
   - **Working Directory:** `C:\Users\Usuario\Sociologia\sociology_kb_starter`

> **Alternativa manual:** Copia el contenido de `chatgpt_mcp_config.json` (incluido en el proyecto) al archivo de configuración de ChatGPT Desktop:
> `%APPDATA%\com.openai.chat\mcp.json`

### Paso 3: Verificar
Una vez configurado, en ChatGPT verás un icono de herramientas (🔧) en el chat. Las herramientas disponibles son:

| Herramienta | Qué hace |
|-------------|----------|
| `kb_search_notes` | Busca notas por texto |
| `kb_read_note` | Lee una nota completa |
| `kb_list_courses` | Lista todos los cursos |
| `kb_list_authors` | Lista todos los autores |
| `kb_list_concepts` | Lista todos los conceptos |
| `kb_get_graph_neighbors` | Explora conexiones en el grafo |
| `kb_file_answer` | Archiva una respuesta Q&A |
| `kb_generate_slides` | Genera presentaciones Marp |
| `kb_ingest_from_inbox` | Procesa PDFs del inbox |

### Ejemplo de uso en ChatGPT
> "Busca todas las notas sobre Durkheim y hazme un resumen de su concepto de solidaridad mecánica"

ChatGPT usará `kb_search_notes` y `kb_read_note` automáticamente para responderte con información de tu KB.

---

## Resumen: tu primer día

1. ✅ Abre `sociology_kb_starter/` como vault en Obsidian
2. ✅ Edita `.env` y pon tu API key de Groq (obtén una en [console.groq.com](https://console.groq.com))
3. ✅ Crea carpetas en `data/inbox/` (ej: `2026-S1/teoria/`)
4. ✅ Copia tus PDFs ahí
5. ✅ Ejecuta `python -m kb_core.watcher --once`
6. ✅ Vuelve a Obsidian → `Ctrl + G` → explora tu grafo de conocimiento
7. ✅ Abre `Project.canvas` para ver y gestionar las tareas del proyecto
8. ✅ Conecta ChatGPT Desktop al MCP (ver sección 12)
