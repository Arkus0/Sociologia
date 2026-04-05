# Auditoría de la Wiki de Sociología — 5 de abril de 2026

Estado actual de la wiki: **168 archivos .md** distribuidos en authors/, concepts/, courses/, sources/.
Cursos cubiertos: Introducción a la Sociología, Metodología de las Ciencias Sociales (2026-S1).

---

## LISTA 1 — Entradas existentes que necesitan mejora (45 entradas)

Cada entrada incluye el problema principal detectado y una orientación de mejora.

### A. Duplicados y stubs de redirección (5)

| # | Archivo | Problema | Mejora sugerida |
|---|---------|----------|-----------------|
| 1 | `authors/marx.md` | Stub de redirección (~55 palabras), duplica `karl-marx.md` | Consolidar en una sola entrada; eliminar el stub y redirigir wikilinks |
| 2 | `authors/kant.md` | Stub de redirección (~59 palabras), duplica `immanuel-kant.md` | Idem |
| 3 | `authors/durkheim.md` | Stub de redirección (~61 palabras), duplica `emile-durkheim.md` | Idem |
| 4 | `authors/toni-estrade-i-salto.md` | Stub (~62 palabras), duplica `antoni-estrade-i-salto.md` | Idem |
| 5 | `GRAPH.md` | Solo 414 bytes, mapa Mermaid vacío o mínimo | Regenerar el grafo completo del wiki con todas las conexiones actuales |

### B. Autores con calidad baja o sin referencias académicas (10)

| # | Archivo | Palabras | Problema | Mejora sugerida |
|---|---------|----------|----------|-----------------|
| 6 | `authors/rosa-borge-bravo.md` | ~95 | Sin referencias académicas, sin wikilinks internos | Añadir obra principal, contexto en ciencia política, enlazar a conceptos de metodología |
| 7 | `authors/albert-padro-solanet.md` | ~125 | Sin referencias académicas | Añadir publicaciones, enlazar a conceptos de metodología que enseña |
| 8 | `authors/roger-martinez-sanmarti.md` | ~130 | Sin referencias académicas | Añadir publicaciones sobre sociología clásica |
| 9 | `authors/grace-abbott.md` | ~130 | Solo 1 referencia, entrada corta | Expandir con obra legislativa, relación con políticas de inmigración |
| 10 | `authors/edith-abbott.md` | ~135 | Solo 1 referencia, entrada corta | Expandir con contribución metodológica a la Escuela de Chicago |
| 11 | `authors/sophonisba-breckinridge.md` | ~135 | Solo 1 referencia | Expandir con trabajo jurídico-social y reforma legislativa |
| 12 | `authors/julia-lathrop.md` | ~125 | Solo 1 referencia | Expandir con contribución al Children's Bureau |
| 13 | `authors/leslie-kish.md` | ~155 | Funcional pero escueto para un metodólogo clave | Expandir con impacto del muestreo probabilístico, aplicaciones internacionales |
| 14 | `authors/robert-merton.md` | ~165 | Entrada funcional pero delgada vs. su importancia | Expandir con funciones manifiestas/latentes, profecía autocumplida, serendipity |
| 15 | `authors/marianne-weber.md` | ~650 | Decente pero reconoce ser reducida a "esposa de" sin expandir su obra propia | Profundizar su trabajo sobre derecho y género, su sociología autónoma |

### C. Conceptos metodológicos delgados (15)

Estos conceptos tienen entre 220-280 palabras, formato heterogéneo (muchos usan `updated_at` en vez de `semester/course`), y leen más como fichas de referencia que como artículos de síntesis. Compararlos con entradas como `alienacion.md` o `burocracia.md` (~800 palabras, historización, debates, vigencia) muestra la brecha.

| # | Archivo | Palabras | Problemas específicos |
|---|---------|----------|-----------------------|
| 16 | `concepts/variable-dependiente.md` | ~237 | Wikilinks rotos (mayúsculas), sin contexto histórico, sin ejemplo empírico desarrollado |
| 17 | `concepts/variable-independiente.md` | ~227 | Idem; casi idéntica en estructura a la anterior |
| 18 | `concepts/variable-interviniente.md` | ~268 | Wikilink roto a "problema de la caja negra" (no existe) |
| 19 | `concepts/variable-de-control.md` | ~244 | Correcta pero muy breve; falta ejemplo de investigación real |
| 20 | `concepts/validez-interna.md` | ~229 | Sin referencia académica explícita; necesita amenazas a la validez (Campbell & Stanley) |
| 21 | `concepts/validez-externa.md` | ~273 | Wikilink roto a "trilema de la encuesta"; necesita discusión de generalización |
| 22 | `concepts/grupo-experimental.md` | ~264 | Falta referencia a diseños cuasi-experimentales |
| 23 | `concepts/estadistica-descriptiva.md` | ~243 | Muy corta; sin medidas concretas (media, mediana, moda, desviación), sin ejemplo |
| 24 | `concepts/estadistica-inferencial.md` | ~241 | Muy corta; falta p-valor, contraste de hipótesis, intervalos de confianza |
| 25 | `concepts/covarianza.md` | ~278 | Falta distinción clara covarianza/correlación, coeficiente de Pearson |
| 26 | `concepts/indicador.md` | ~268 | Breve; necesita ejemplo completo de operacionalización→indicadores |
| 27 | `concepts/diseno-empirico.md` | ~268 | Falta tipología de diseños (experimental, cuasi, observacional, longitudinal) |
| 28 | `concepts/investigacion-cualitativa.md` | ~256 | Muy escueta para un paradigma entero; faltan métodos concretos (etnografía, análisis del discurso) |
| 29 | `concepts/investigacion-cuantitativa.md` | ~280 | Wikilinks todos rotos (mayúsculas); falta proceso detallado |
| 30 | `concepts/niveles-de-medicion.md` | ~302 | Aceptable pero necesita tabla comparativa clara (nominal, ordinal, intervalo, razón) |

### D. Conceptos teóricos que necesitan actualización o expansión (10)

| # | Archivo | Problema principal |
|---|---------|-------------------|
| 31 | `concepts/estado-de-bienestar.md` | ~600 palabras; falta crisis contemporánea (austeridad, neoliberalismo post-2008), cuarto mundo de bienestar |
| 32 | `concepts/androcentrismo.md` | ~650 palabras; importante concepto epistemológico tratado brevemente; necesita más sobre cómo sesga métodos y teorías |
| 33 | `concepts/trabajo-domestico.md` | ~700 palabras; falta trabajo de cuidados contemporáneo, economía reproductiva, cadenas globales de cuidado |
| 34 | `concepts/infraestructura-y-superestructura.md` | ~650 palabras; falta discusión de la reificación del modelo en el marxismo vulgar, matización gramsciana más profunda |
| 35 | `concepts/encuesta.md` | Formato diferente al resto; falta discusión de la crisis contemporánea de la encuesta (tasas de respuesta decrecientes, encuestas online) |
| 36 | `concepts/muestreo.md` | Muestreo no probabilístico muy poco desarrollado (solo cuotas); faltan bola de nieve, conveniencia, teórico |
| 37 | `concepts/operacionalizacion.md` | Falta un ejemplo negativo de mala operacionalización; discusión de validez de constructo |
| 38 | `concepts/hipotesis.md` | Falta distinción clara entre hipótesis y pregunta de investigación |
| 39 | `concepts/causalidad.md` | Frontmatter inconsistente; falta discusión del "problema de la caja negra" de Goldthorpe mencionada en otras entradas |
| 40 | `concepts/anomalias-sociales.md` | Entrada huérfana (nadie enlaza a ella); necesita integración en la red de wikilinks |

### E. Problemas estructurales transversales (5)

| # | Problema | Archivos afectados |
|---|----------|--------------------|
| 41 | **89 wikilinks rotos masivos**: los enlaces `[[El proceso de formulación teórica]]`, `[[El proceso de investigación...]]`, `[[La investigación cuantitativa]]` usan mayúsculas/acentos en vez del slug | ~30 archivos de metodología cada uno |
| 42 | **47 wikilinks con mayúsculas**: `[[Deducción]]`, `[[Hipótesis]]`, `[[Operacionalización]]` en vez de `[[deduccion]]`, `[[hipotesis]]`, etc. | Dispersos en concepts/ de metodología |
| 43 | **Wikilink con backslash**: `[[web-du-bois\|W.E.B. Du Bois]]` en `relaciones-raciales.md` | 1 archivo |
| 44 | **Frontmatter heterogéneo**: entradas de metodología usan `updated_at` + `source_notes` mientras que las de teoría usan `semester` + `course` + `related_concepts` + `tags` | ~15 archivos de metodología |
| 45 | **Secciones "vigencia contemporánea" desactualizadas**: las referencias más recientes son de los 2000s; faltan perspectivas post-2015 (plataformas, algoritmos, crisis climática) | burocracia, racionalizacion, modernidad, estado-de-bienestar, entre otros |

---

## LISTA 2 — Entradas que faltan y deberían crearse (48 entradas)

### A. Autores referenciados pero sin entrada (8)

| # | Autor | Justificación |
|---|-------|---------------|
| 1 | **W.E.B. Du Bois** | Referenciado en `ana-julia-cooper.md`, `sociologia-clasica.md`, `relaciones-raciales.md`; fundador de la sociología empírica de la raza |
| 2 | **Herbert Spencer** | Referenciado en `darwinismo-social-de-reforma.md`, `sociologia-clasica.md`; figura necesaria para entender el evolucionismo social |
| 3 | **Alexis de Tocqueville** | Referenciado en `sociologia-clasica.md`; clave para democracia, asociacionismo, igualdad de condiciones |
| 4 | **Karl Popper** | Referenciado en `david-hume.md`; esencial para racionalismo crítico y falsabilidad (ya hay entrada de `racionalismo-critico`) |
| 5 | **Pierre Bourdieu** | Mencionado en varias entradas (lucha de clases, etc.); su teoría del capital cultural/habitus/campo es imprescindible |
| 6 | **Georg Simmel** | Ausente; fundador junto a Weber de la sociología comprensiva alemana; conceptos de interacción social, el extranjero, las formas sociales |
| 7 | **Talcott Parsons** | Ausente; dominó la sociología americana del siglo XX; sistema social, AGIL, funcionalismo estructural |
| 8 | **Erving Goffman** | Ausente; dramaturgia social, estigma, interaccionismo simbólico |

### B. Conceptos teóricos fundamentales ausentes (20)

| # | Concepto | Justificación |
|---|----------|---------------|
| 9 | **Funcionalismo** | Paradigma central de la sociología; conecta con Durkheim, Parsons, Merton |
| 10 | **Interaccionismo simbólico** | Tercer gran paradigma; conecta con Escuela de Chicago, Mead, Blumer, Goffman |
| 11 | **Teoría del conflicto** | Paradigma que agrupa Marx, Dahrendorf, Collins; contrapunto al funcionalismo |
| 12 | **Estratificación social** | Concepto central; conecta con clases sociales, movilidad, desigualdad |
| 13 | **Movilidad social** | Complemento de estratificación; enlaza con Goldthorpe (ya tiene entrada) |
| 14 | **Capital social** | Referenciado en `robert-putnam.md`; concepto clave de Bourdieu, Coleman y Putnam |
| 15 | **Capital cultural** | Bourdieu; esencial para entender reproducción social y educación |
| 16 | **Habitus** | Bourdieu; puente entre estructura y agencia |
| 17 | **Socialización** | Proceso fundamental; conecta con Durkheim, Berger, Parsons |
| 18 | **Desviación social** | Conecta con anomia (ya existe), Merton, Becker, labeling theory |
| 19 | **Institución social** | Concepto básico; familia, educación, religión, Estado |
| 20 | **Rol social** | Concepto básico; enlaza con Parsons, Goffman, Merton (role-set) |
| 21 | **Contrato social** | Conecta con Rousseau (ya tiene entrada), Hobbes, Locke; fundamento de la teoría política moderna |
| 22 | **Legitimidad y dominación** | Weber; conecta con burocracia, tipos ideales; tres tipos de dominación |
| 23 | **Verstehen (comprensión)** | Método weberiano central; mencionado pero sin entrada propia |
| 24 | **Solidaridad social** (general) | Entrada marco que conecte mecánica + orgánica + nuevas formas de solidaridad |
| 25 | **Clase social** | Concepto propio diferenciado de "lucha de clases"; definiciones de Marx, Weber, Bourdieu, Wright |
| 26 | **Ideología** | Marx, Mannheim, Althusser; conecta con infraestructura-superestructura |
| 27 | **Hegemonía** | Gramsci; mencionada en infraestructura-y-superestructura pero sin desarrollo |
| 28 | **Globalización** | Tema central de sociología contemporánea; conecta con Giddens, Bauman, Beck |

### C. Conceptos metodológicos referenciados pero inexistentes (12)

| # | Concepto | Justificación |
|---|----------|---------------|
| 29 | **Codificación** | Referenciada 4 veces en wikilinks rotos; proceso clave en análisis de datos |
| 30 | **Censo** | Referenciado en wikilinks; técnica de recolección fundamental |
| 31 | **Contrastabilidad / Falsabilidad** | Referenciada en wikilink roto; conecta con Popper y racionalismo crítico |
| 32 | **Grupo de control** | Referenciado en wikilinks rotos; complemento de grupo-experimental |
| 33 | **Instrumento de medición** | Referenciado en wikilinks; concepto clave de operacionalización |
| 34 | **Preguntas abiertas y cerradas** | Referenciado en `cuestionario.md`; fundamental para diseño de cuestionarios |
| 35 | **Análisis de contenido** | Técnica cualitativa importante no cubierta |
| 36 | **Etnografía** | Método cualitativo central; conecta con Escuela de Chicago, Geertz |
| 37 | **Entrevista en profundidad** | Técnica cualitativa fundamental; complementa encuesta y cuestionario |
| 38 | **Fiabilidad** | Complemento de validez (interna y externa ya existen); concepto medular |
| 39 | **Paradigma** | Kuhn; referencia conceptual para entender los debates metodológicos |
| 40 | **Triangulación** | Método que conecta lo cualitativo y lo cuantitativo |

### D. Entradas de perspectivas críticas y contemporáneas (8)

| # | Entrada | Justificación |
|---|---------|---------------|
| 41 | **Sociología postcolonial** | Perspectiva ausente; toda la wiki es occidental; necesario para un grado completo |
| 42 | **Interseccionalidad** | Crenshaw; conecta con Du Bois, Wells-Barnett, perspectiva de género |
| 43 | **Sociología urbana** | Conecta con Escuela de Chicago ya existente; Park, Burgess, Wirth |
| 44 | **Sociología del conocimiento** | Mannheim, Berger & Luckmann; conecta con Peter Berger (ya tiene entrada) |
| 45 | **Construcción social de la realidad** | Berger & Luckmann; complementa la entrada de Peter Berger |
| 46 | **Racismo estructural** | Complementa relaciones-raciales; conecta con Du Bois, Wells-Barnett |
| 47 | **Teoría crítica / Escuela de Frankfurt** | Mencionada en varias entradas (alienación, fetichismo, jaula de hierro) pero sin entrada propia |
| 48 | **Sociedad del riesgo** | Beck; complementa globalización y modernidad reflexiva de Giddens |

---

## Resumen cuantitativo

| Categoría | Entradas |
|-----------|----------|
| **A mejorar** | 45 |
| **A crear** | 48 |
| **Total acciones** | 93 |

### Prioridades recomendadas

**Urgente** (impacto inmediato en integridad): corregir los 89 wikilinks rotos masivos (#41), normalizar mayúsculas (#42), consolidar duplicados (#1-4).

**Alta** (completitud conceptual): crear las 8 entradas de autores ausentes y los 12 conceptos metodológicos referenciados — son deuda técnica directa del wiki (links que apuntan a la nada).

**Media** (profundidad): expandir los 15 conceptos metodológicos delgados (#16-30) al nivel de calidad de los conceptos teóricos; actualizar las secciones de vigencia contemporánea.

**Planificable** (crecimiento del wiki): crear los 20 conceptos teóricos y las 8 perspectivas contemporáneas a medida que se avance en el grado.
