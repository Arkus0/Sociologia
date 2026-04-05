---
id: preguntas-filtro
title: Preguntas filtro
note_type: concept
semester: 2026-S1
course: "Metodologia de las ciencias sociales"
related_concepts:
  - cuestionario
  - encuesta
  - preguntas-abiertas-y-cerradas
  - diseno-de-investigacion
  - investigacion-cuantitativa
  - error-muestral
  - variable-dependiente
tags:
  - metodología
  - cuestionario
  - diseño-de-encuesta
  - técnicas-de-investigación
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\cuaderno-metodologico-cuestionarios.md
updated_at: '2025-07-13'
---

## Definición

Las **preguntas filtro** son un tipo especial de pregunta dentro de un [[cuestionario]] cuya función es dirigir al entrevistado hacia las preguntas que resultan pertinentes según su situación particular, evitando que responda a aquellas que no le corresponden. En la terminología anglosajona se conocen como *screening questions* o *filter questions*, y el mecanismo lógico que generan se denomina *skip logic* o *branching logic*. Según el *Cuaderno Metodológico* del Centro de Investigaciones Sociológicas (CIS), «las preguntas filtro tienen la función de evitar que contesten aquellas personas a quienes no va destinada la pregunta» (Cuadernos Metodológicos CIS, n.º 26). Se realizan previamente a otra pregunta o bloque de preguntas para excluir a quienes el tema no les afecta, canalizando así el flujo del cuestionario de manera lógica y eficiente.

## Origen y contexto histórico

El desarrollo de las preguntas filtro está ligado a la profesionalización de la [[encuesta]] como técnica de investigación social durante el siglo XX. A medida que los cuestionarios crecieron en extensión y complejidad — particularmente a partir de los grandes estudios de opinión pública de mediados de siglo, como los realizados por George Gallup y Paul Lazarsfeld —, se hizo evidente la necesidad de mecanismos que evitaran formular preguntas irrelevantes a determinados segmentos de la [[muestra-estadistica|muestra]]. La formalización del diseño de cuestionarios en manuales metodológicos, como los publicados por el CIS en España o por instituciones como NORC en Estados Unidos, consolidó el uso de preguntas filtro como una herramienta estándar del [[diseno-de-investigacion]]. Con la llegada de la encuesta asistida por ordenador (CAPI, CATI) y, más recientemente, de las plataformas de encuestas en línea, la lógica de saltos condicionales se automatizó, permitiendo ramificaciones más complejas sin riesgo de error del entrevistador.

## Desarrollo teórico

Desde un punto de vista metodológico, las preguntas filtro cumplen varias funciones simultáneas dentro de la [[investigacion-cuantitativa]]:

1. **Pertinencia temática**: garantizan que cada entrevistado solo responda a las preguntas que le son aplicables. Por ejemplo, si se desea conocer a qué tipo de colegio — público o privado — llevan los padres a sus hijos, es necesario formular primero una pregunta filtro: «¿Tiene Ud. hijos en edad escolar?». Solo quienes responden afirmativamente deben continuar con la pregunta filtrada.

2. **Reducción de la carga del encuestado**: al eliminar preguntas inaplicables se acorta la duración efectiva de la entrevista, lo que disminuye la fatiga y mejora la calidad de las respuestas.

3. **Coherencia interna del cuestionario**: evitan situaciones en las que un entrevistado se vea obligado a responder sobre algo que contradice una respuesta anterior, lo que podría generar confusión o datos inconsistentes.

4. **Orientación del entrevistador**: en cuestionarios administrados cara a cara, las preguntas filtro deben ir claramente señalizadas — mediante flechas, recuadros o notas — para que el entrevistador navegue el instrumento sin vacilaciones.

El mecanismo operativo es sencillo: la respuesta a la pregunta filtro determina si el encuestado debe responder la pregunta o serie de preguntas siguientes (*preguntas filtradas*) o si debe saltar a otro punto del cuestionario. Esta lógica de ramificación puede encadenarse en varios niveles, creando árboles de decisión que adaptan el recorrido del cuestionario al perfil de cada entrevistado.

## Relación con otros conceptos

Las preguntas filtro se sitúan en la intersección de varios elementos del diseño de encuestas:

- **[[cuestionario]]**: constituyen uno de los tipos funcionales de pregunta dentro de la estructura del cuestionario, junto con las preguntas en batería, las de control y las sociodemográficas.
- **[[preguntas-abiertas-y-cerradas]]**: las preguntas filtro suelen adoptar un formato cerrado — frecuentemente dicotómico (sí/no) — para facilitar la lógica de ramificación.
- **[[error-muestral]]**: un riesgo asociado al uso excesivo de preguntas filtro es la reducción de la submuestra efectiva que responde a las preguntas filtradas, lo que incrementa el error muestral para esas variables.
- **[[encuesta]]**: la lógica de filtrado es un componente esencial del diseño de cualquier encuesta de cierta complejidad, tanto presencial como en línea.
- **[[diseno-de-investigacion]]**: la decisión sobre qué preguntas filtro incluir forma parte de la planificación general de la investigación y debe contemplarse desde la operacionalización de las hipótesis.

## Debates y críticas

El principal debate metodológico en torno a las preguntas filtro gira sobre el equilibrio entre especificidad y pérdida de muestra. Como advierte el CIS: «No conviene abusar de las preguntas filtro: reducen la muestra sensiblemente, llegando, en algunos casos, hasta el extremo de hacer imposible el análisis estadístico de la información que recogen». Un cuestionario está diseñado para aplicarse a un determinado [[tamano-de-la-muestra]], vinculado al error muestral aceptable. Cada pregunta filtro subdivide la muestra, y si las sucesivas ramificaciones son muchas, las submuestras resultantes pueden ser demasiado pequeñas para un análisis estadístico fiable.

Otras críticas señalan que: (a) un exceso de saltos condicionales puede dificultar la labor del entrevistador en cuestionarios en papel, aumentando los errores de administración; (b) en encuestas en línea, una ramificación excesiva puede generar experiencias desiguales entre encuestados, complicando la comparabilidad; y (c) cuando las preguntas filtro no están correctamente señalizadas, el entrevistado puede verse desconcertado al recibir preguntas aparentemente incongruentes con sus respuestas previas.

## Vigencia contemporánea

En la era de las encuestas digitales, las preguntas filtro han cobrado nueva relevancia gracias a la automatización. Plataformas como Qualtrics, SurveyMonkey o LimeSurvey implementan la lógica de saltos (*skip logic*) y la lógica de visualización (*display logic*) de forma nativa, permitiendo diseños de ramificación complejos sin riesgo de error humano. Esto ha ampliado las posibilidades del [[diseno-de-investigacion]], habilitando cuestionarios adaptativos que se ajustan en tiempo real al perfil del respondiente.

Asimismo, en el contexto de los macrodatos y la investigación a gran escala, el filtrado inteligente de preguntas contribuye a reducir la fatiga del encuestado — un problema creciente dada la proliferación de encuestas en línea — y a mejorar las tasas de respuesta completa. La investigación metodológica contemporánea explora también el uso de algoritmos de *adaptive questioning* que van más allá del filtro binario clásico, seleccionando dinámicamente las preguntas en función de las respuestas acumuladas.

## Ejemplo empírico

En una encuesta del CIS sobre hábitos de consumo de tabaco, se incluye la siguiente pregunta filtro:

> **P.5** ¿Podría decirme si ha fumado regularmente alguna vez?
> 1. Sí, ha fumado y fuma actualmente → *Pasar a P.5a*
> 2. Sí, ha fumado, pero ya lo ha dejado → *Pasar a P.5a*
> 3. Solo de forma esporádica → *Pasar a P.6*
> 4. No ha fumado nunca → *Pasar a P.6*

En este caso, la pregunta P.5a — que indaga sobre la cantidad de cigarrillos consumidos diariamente — solo se formula a quienes han respondido las opciones 1 o 2. Quienes nunca han fumado o solo lo han hecho esporádicamente saltan directamente a la siguiente sección. El diseño con flechas y recuadros permite al entrevistador seguir el flujo sin ambigüedad.

## Véase también

- [[cuestionario]]
- [[encuesta]]
- [[preguntas-abiertas-y-cerradas]]
- [[diseno-de-investigacion]]
- [[investigacion-cuantitativa]]
- [[error-muestral]]
- [[tamano-de-la-muestra]]
- [[variables-sociodemograficas]]

## Fuentes

- [[cuadernos-metodologicos-cis-26-diseno-de-cuestionarios]] — *Cuadernos Metodológicos* n.º 26, Centro de Investigaciones Sociológicas (CIS).
- Cea D'Ancona, M. Á. (2004). *Métodos de encuesta: teoría y práctica, errores y mejora*. Madrid: Síntesis.
- Fowler, F. J. (2014). *Survey Research Methods* (5.ª ed.). Thousand Oaks: SAGE.
- Saris, W. E. & Gallhofer, I. N. (2014). *Design, Evaluation and Analysis of Questionnaires for Survey Research* (2.ª ed.). Hoboken: Wiley.
- «Cuestionario». *Wikipedia en español*. Consultado el 13 de julio de 2025.
