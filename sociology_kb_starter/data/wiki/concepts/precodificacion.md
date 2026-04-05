---
id: precodificacion
title: Precodificación
note_type: concept
semester: 2026-S1
course: "Metodologia de las ciencias sociales"
related_concepts:
  - codificacion
  - cuestionario
  - preguntas-abiertas-y-cerradas
  - encuesta
  - niveles-de-medicion
  - trabajo-de-campo
  - analisis-estadistico
tags:
  - metodología
  - cuestionario
  - codificación
  - investigación cuantitativa
  - técnicas de investigación
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\cuaderno-metodologico-cuestionarios.md
updated_at: '2025-07-13'
---

## Definición

La **precodificación** es el procedimiento metodológico consistente en asignar códigos numéricos a las categorías de respuesta de un [[cuestionario]] *antes* de que comience el [[trabajo-de-campo]]. A diferencia de la [[codificacion]] posterior —que se aplica una vez recogidos los datos, especialmente en [[preguntas-abiertas-y-cerradas|preguntas abiertas]]—, la precodificación integra el sistema de códigos directamente en el diseño del instrumento de recogida. Cada opción de respuesta cerrada lleva impreso un valor numérico que el entrevistador o el propio encuestado pueden registrar de forma inmediata, garantizando así la correspondencia unívoca entre la respuesta verbal y su representación cuantitativa.

En términos operativos, precodificar supone decidir, durante la fase de planificación del cuestionario, qué número representará cada categoría, qué valores se reservarán para las respuestas especiales (no sabe, no contesta, no procede) y cómo se organizará el **libro de códigos** (*codebook*) que documenta estas decisiones para todo el equipo de investigación.

## Origen y contexto histórico

La práctica de precodificar cuestionarios se consolida a mediados del siglo XX, cuando la expansión de la [[encuesta]] muestral como técnica estandarizada de investigación social exigió procedimientos eficientes para procesar grandes volúmenes de datos. Los primeros centros de investigación por encuesta —el *Survey Research Center* de la Universidad de Michigan, el *National Opinion Research Center* (NORC) de Chicago y, en España, el Centro de Investigaciones Sociológicas (CIS)— fueron los principales impulsores de la estandarización del proceso. La introducción de tarjetas perforadas y, más tarde, de terminales de grabación de datos hizo imprescindible que cada respuesta tuviese un código numérico fijo antes de llegar a la fase de tratamiento informático.

María José Azofra, en el *Cuaderno Metodológico* n.º 26 del CIS, señala que la **planificación del cuestionario** incluye explícitamente la precodificación como paso previo al trabajo de campo, junto con la definición del orden de preguntas, la longitud del instrumento, los filtros y las instrucciones al entrevistador. De este modo, la precodificación dejó de ser un detalle técnico para convertirse en un componente integral del diseño de investigación.

## Desarrollo teórico

### Precodificación frente a codificación posterior

La distinción fundamental reside en el momento en que se asignan los códigos:

- **Precodificación**: los códigos se determinan durante el diseño del cuestionario y quedan impresos junto a cada categoría de respuesta cerrada. Es aplicable cuando las opciones de respuesta son conocidas de antemano y pueden enumerarse de forma exhaustiva y mutuamente excluyente.
- **Codificación posterior** (*post-coding*): se realiza una vez finalizado el campo. Se reserva para las [[preguntas-abiertas-y-cerradas|preguntas abiertas]], cuyas respuestas no pueden anticiparse en su totalidad. Requiere extraer una muestra de cuestionarios, agrupar las respuestas semejantes y elaborar un libro de claves *a posteriori*.

### Convenciones de codificación

Según la práctica del CIS, el código **1** se reserva convencionalmente para la postura positiva o favorable en escalas de actitud, descendiendo hacia valores más altos a medida que la posición es menos favorable. Las respuestas especiales reciben códigos reservados fuera del rango sustantivo: típicamente **8** para «No sabe», **9** para «No contesta» y **0** o **99** para «No procede». Estos **códigos de valores perdidos** (*missing value codes*) son esenciales para que el software estadístico distinga entre datos sustantivos y ausencias de información durante el [[analisis-estadistico]].

### El libro de códigos

El libro de códigos (*codebook*) es el documento que registra, para cada variable del cuestionario, su nombre, etiqueta, [[niveles-de-medicion|nivel de medición]], rango de valores válidos, códigos de valores perdidos y la correspondencia exacta entre cada categoría de respuesta y su código numérico. Sin un libro de códigos riguroso, la precodificación pierde su función estandarizadora, pues distintos miembros del equipo podrían interpretar los datos de forma incompatible.

### Precodificación y tipos de preguntas

La precodificación se aplica de forma natural a:

- **Preguntas cerradas dicotómicas**: Sí (1) / No (2).
- **Preguntas categorizadas u ordinales**: escalas de acuerdo-desacuerdo con valores sucesivos.
- **Preguntas de escala numérica**: autoubicación ideológica de 1 a 10.
- **Variables sociodemográficas**: sexo, nivel de estudios, situación laboral, cuyas categorías son estandarizadas.

Las **preguntas abiertas**, por definición, no pueden precodificarse plenamente, aunque es frecuente incorporar una precodificación parcial cuando se prevé que un porcentaje elevado de respuestas se agrupará en categorías conocidas (práctica denominada *semi-precodificación* o **pregunta semicerrada**).

## Relación con otros conceptos

La precodificación se sitúa en la intersección de varias operaciones del proceso de investigación:

- Con la [[codificacion]], constituye las dos modalidades temporales de asignación de códigos; juntas cubren la totalidad del cuestionario.
- Con el [[cuestionario]], forma parte de su fase de planificación y condiciona su maquetación física o digital.
- Con las [[preguntas-abiertas-y-cerradas]], delimita el alcance de su aplicabilidad: solo las cerradas admiten precodificación completa.
- Con la [[encuesta]], facilita la eficiencia del campo y la calidad de la grabación de datos.
- Con los [[niveles-de-medicion]], determina si los códigos representan categorías nominales, ordinales o de intervalo, lo que condiciona las operaciones estadísticas admisibles.

## Debates y críticas

Un primer debate concierne al **riesgo de rigidez**: al fijar las categorías antes del campo, la precodificación puede excluir respuestas no previstas por el investigador, empobreciendo la información recogida. Este problema se mitiga parcialmente con la inclusión de categorías residuales («Otra respuesta, ¿cuál?»), pero la experiencia muestra que los entrevistadores tienden a infrautilizar estas opciones para no ralentizar la entrevista.

Un segundo problema es la **asignación convencional de valores**. Cuando el código 1 se reserva para la postura «favorable», el investigador introduce implícitamente un juicio valorativo sobre qué extremo de la escala es positivo; en temas políticamente controvertidos, esta decisión puede no ser neutral. Algunos metodólogos recomiendan rotar el sentido de las escalas o emplear codificaciones arbitrarias que se recodifican después.

Asimismo, la precodificación puede generar una **ilusión de precisión**: el hecho de que cada respuesta tenga un número asociado no garantiza que el encuestado distinga realmente entre las categorías ofrecidas, especialmente en escalas largas donde la diferencia entre posiciones adyacentes es subjetiva.

## Vigencia contemporánea

La precodificación mantiene plena vigencia en la investigación social contemporánea y, de hecho, su importancia ha aumentado con la generalización de las encuestas asistidas por ordenador (CAPI, CATI, CAWI). En estos formatos, la precodificación se implementa directamente en el software de recogida de datos, de modo que la respuesta seleccionada por el encuestado se almacena automáticamente como valor numérico, eliminando la fase manual de grabación y reduciendo drásticamente los errores de transcripción.

Las plataformas contemporáneas de encuestas en línea (Qualtrics, SurveyMonkey, LimeSurvey) incorporan la precodificación como funcionalidad nativa: cada opción de respuesta lleva asociado un valor numérico configurable que se exporta directamente a formatos compatibles con SPSS, R o Python. Este avance técnico no ha eliminado, sin embargo, la necesidad de decisiones metodológicas humanas sobre la estructura de los códigos, los valores perdidos y la documentación en el libro de códigos.

## Ejemplo empírico

En una encuesta del CIS sobre hábitos culturales, la pregunta «¿Con qué frecuencia lee usted libros?» se precodifica con las siguientes categorías: (1) Todos o casi todos los días, (2) Una o dos veces por semana, (3) Alguna vez al mes, (4) Alguna vez al trimestre, (5) Casi nunca, (6) Nunca, (8) N.S., (9) N.C. El entrevistador marca el código correspondiente y este se registra directamente en la base de datos. Si la misma encuesta incluyera una pregunta abierta —«¿Qué libro está leyendo actualmente?»—, los títulos obtenidos no podrían precodificarse y requerirían [[codificacion]] posterior: agrupación por géneros, elaboración de un libro de claves y asignación de códigos por un equipo de codificadores.

## Véase también

- [[codificacion]]
- [[cuestionario]]
- [[preguntas-abiertas-y-cerradas]]
- [[encuesta]]
- [[niveles-de-medicion]]
- [[trabajo-de-campo]]
- [[variables-sociodemograficas]]
- [[operacionalizacion]]

## Fuentes

- [[cuadernos-metodologicos-cis-26-diseno-de-cuestionarios]] — Azofra, M. J. (1999). *Cuadernos Metodológicos CIS 26: Diseño de cuestionarios*. Madrid: Centro de Investigaciones Sociológicas.
