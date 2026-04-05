# Reglas de Calidad para Entradas de la Wiki de Sociología

Estándar obligatorio para todas las entradas del wiki. Diseñado para maximizar la utilidad
académica, la interconexión entre artículos y la eficacia del sistema RAG (Retrieval-Augmented
Generation) conectado a Claude.

---

## 1. Estructura de Frontmatter

### Conceptos (`note_type: concept`)

```yaml
---
id: slug-del-concepto          # kebab-case, sin acentos
title: Nombre con Acentos      # Nombre canónico con acentos y mayúsculas
note_type: concept
semester: 2026-S1               # Semestre donde se introduce
course: Nombre del curso        # Curso principal
related_concepts:               # 3-8 conceptos estrechamente relacionados
  - concepto-uno
  - concepto-dos
tags:                           # Etiquetas para búsqueda y clasificación
  - nombre-del-curso
  - paradigma-o-tradicion
source_notes:                   # Auto-gestionado por el compiler
  - ruta/a/source-note.md
updated_at: ISO-8601            # Auto-gestionado
---
```

### Autores (`note_type: author`)

```yaml
---
id: nombre-apellido
title: Nombre Completo
note_type: author
birth_year: AAAA                # Opcional
death_year: AAAA                # Opcional, omitir si vive
nationality: país
tradition: tradición sociológica principal
related_concepts:
  - concepto-central-uno
  - concepto-central-dos
tags:
  - sociologia-clasica          # o contemporanea, metodologia, etc.
source_notes: []                # Auto-gestionado
updated_at: ISO-8601            # Auto-gestionado
---
```

---

## 2. Estructura del Cuerpo — Conceptos

Toda entrada de concepto DEBE contener estas secciones, en este orden:

### Secciones obligatorias

```markdown
## Definición
Párrafo denso (80-150 palabras) que defina el concepto con precisión académica.
Debe ser autosuficiente: un lector que solo lea esta sección debe entender qué es.

## Origen y contexto histórico
Quién lo formuló, cuándo, en respuesta a qué problema intelectual/social.
Mínimo 2 autores con [[wikilinks]]. Citar obra específica cuando sea posible.

## Desarrollo teórico
Explicación del concepto, sus dimensiones, tipologías internas.
Usar ### subsecciones si hay variantes o subtipos.
Mínimo 150 palabras.

## Relación con otros conceptos
Lista de conexiones explícitas con [[wikilinks]] — NO una lista seca,
sino frases que expliquen la relación:
- La [[anomia]] es la contraparte durkheimiana de la [[alienacion]] marxista
- Se operacionaliza mediante [[indicadores]] en la [[investigacion-cuantitativa]]

## Debates y críticas
Al menos 1 crítica o debate importante sobre el concepto.

## Vigencia contemporánea
Cómo se usa o se reinterpreta el concepto hoy (post-2010).
Referencias a fenómenos actuales: digitalización, plataformas, crisis climática, etc.

## Ejemplo empírico
Un caso concreto de investigación o situación real que ilustre el concepto.
Puede venir de las source notes o ser referencia bibliográfica.

## Véase también
- [[concepto-relacionado-1]]
- [[concepto-relacionado-2]]

## Fuentes
- [[source-note-1]] (curso donde aparece)
- Referencia bibliográfica si procede
```

### Longitud mínima
- **Conceptos fundamentales** (alienación, anomia, burocracia, etc.): 600-1000 palabras
- **Conceptos metodológicos**: 400-700 palabras
- **Conceptos menores**: 300-500 palabras

---

## 3. Estructura del Cuerpo — Autores

```markdown
## Biografía intelectual
Párrafo biográfico centrado en su trayectoria intelectual, NO en datos personales
irrelevantes. Contexto histórico-social en que trabajó. (80-150 palabras)

## Contribuciones principales
### Concepto/Obra 1
Explicación de la contribución con [[wikilinks]] a los conceptos.

### Concepto/Obra 2
...

## Método y enfoque
Cómo investigaba, qué métodos usó, qué enfoque epistemológico defendía.

## Obras fundamentales
- *Título de la obra* (año): breve descripción de su contenido e impacto

## Influencia y legado
Quién se inspiró en este autor, qué corrientes derivan de su trabajo.
Usar [[wikilinks]] a otros autores y conceptos.

## Críticas
Al menos una crítica relevante a su obra.

## Véase también
- [[concepto-1]]
- [[autor-relacionado]]

## Fuentes
- [[source-note-1]]
```

### Longitud mínima
- **Autores "indiscutibles"** (Marx, Durkheim, Weber, Comte): 700-1200 palabras
- **Autores relevantes** (Simmel, Parsons, Bourdieu, etc.): 500-800 palabras
- **Autores menores/profesorado**: 200-400 palabras

---

## 4. Reglas de Wikilinks

### Formato canónico
```
[[slug-en-kebab-case]]                    → enlace simple
[[slug-en-kebab-case|Texto visible]]      → enlace con alias
```

### Reglas estrictas
1. **SIEMPRE slug en minúsculas sin acentos**: `[[alienacion]]`, NO `[[Alienación]]`
2. **NUNCA mayúsculas** en el slug: `[[karl-marx]]`, NO `[[Karl Marx]]`
3. **NUNCA acentos** en el slug: `[[anomia]]`, NO `[[anomía]]`
4. **NUNCA backslashes**: `[[web-du-bois|W.E.B. Du Bois]]`, NO `[[web-du-bois\|...]]`
5. **Usar alias** cuando el slug no sea legible: `[[emile-durkheim|Émile Durkheim]]`
6. **Mínimo 5 wikilinks** por entrada de concepto, **3** por entrada de autor
7. **Bidireccional implícito**: si A enlaza a B, B debe enlazar a A (preferiblemente)

### Slugificación
- Espacios → guiones: `Karl Marx` → `karl-marx`
- Acentos eliminados: `Émile` → `emile`, `Anomía` → `anomia`
- Artículos y preposiciones mantenidos: `ley-de-los-tres-estadios`
- Eñes: `diseño` → `diseno`

---

## 5. Reglas para Optimización RAG

Estas reglas maximizan la utilidad de las entradas cuando Claude las recupera vía RAG:

### Densidad semántica
- Cada párrafo debe contener **información sustantiva**. Evitar frases de relleno.
- La **primera oración** de cada sección debe resumir su contenido (patrón pirámide invertida).
- Incluir **sinónimos y términos alternativos** entre paréntesis: "anomia (anomie, normlessness)".

### Contexto autosuficiente
- Cada entrada debe ser comprensible **sin leer otras entradas**. No asumir que Claude
  ha leído el artículo del que se enlaza.
- Cuando se mencione un concepto de otra entrada, dar una micro-definición en línea:
  "la [[anomia]] (ausencia de normas reguladoras según Durkheim)".

### Relaciones explícitas
- Nombrar las relaciones: "X es una **causa** de Y", "X es un **tipo** de Y",
  "X **se opone** a Y", "X **complementa** a Y".
- El grafo de conocimiento se construye a partir de estas relaciones.

### Anclajes temporales y espaciales
- Siempre situar conceptos en tiempo y espacio: "formulado por Weber en *Economía y
  Sociedad* (1922)", NO "formulado por Weber".
- Esto permite a Claude contextualizar cronológicamente las respuestas.

### Terminología consistente
- Usar siempre el mismo término para el mismo concepto en toda la wiki.
- Si hay variantes, declarar el término canónico y los alias en la definición:
  "**Racionalización** (también: racionalidad instrumental, Zweckrationalität)".

---

## 6. Reglas de Idioma y Estilo

- **Idioma**: español académico, registro formal pero accesible.
- **Persona**: tercera persona impersonal ("se define como", "Durkheim propone").
- **Citas**: estilo APA simplificado: "Weber (1905)" o "(Weber, 1905)".
- **Cursivas**: títulos de obras (*El Capital*, *Las reglas del método sociológico*).
- **Negritas**: solo para términos que se definen por primera vez en la entrada.
- **NO incluir** opiniones personales, valoraciones subjetivas, ni contenido no verificable.

---

## 7. Checklist de Calidad (pre-publicación)

Toda entrada debe pasar este checklist antes de considerarse completa:

- [ ] Frontmatter completo con todos los campos requeridos
- [ ] `id` en kebab-case sin acentos
- [ ] `related_concepts` con mínimo 3 entradas
- [ ] Todas las secciones obligatorias presentes
- [ ] Mínimo de palabras cumplido según categoría
- [ ] Mínimo 5 wikilinks (conceptos) o 3 wikilinks (autores)
- [ ] Todos los wikilinks en formato `[[slug-minusculas]]`
- [ ] Primera oración de cada sección funciona como resumen
- [ ] Al menos 1 referencia bibliográfica o source note
- [ ] Sin frases de relleno ni secciones vacías
- [ ] Revisión de ortografía y coherencia terminológica

---

## 8. Proceso de Enriquecimiento

### Desde stub auto-generado a entrada completa:

1. **Recopilar**: leer todas las source notes que referencian el concepto/autor
2. **Sintetizar**: combinar la información de múltiples fuentes en una narrativa coherente
3. **Contextualizar**: añadir contexto histórico, debates y vigencia contemporánea
4. **Conectar**: crear wikilinks bidireccionales con entradas relacionadas
5. **Verificar**: pasar el checklist de calidad
6. **Proteger**: el compiler preserva automáticamente el contenido enriquecido

### Señal de contenido enriquecido
El compiler detecta automáticamente si una entrada ha sido enriquecida. Las entradas que
contienen el texto "This page aggregates references to" se consideran stubs y serán
regeneradas. Las que no lo contienen se preservan y solo se actualiza su frontmatter.
