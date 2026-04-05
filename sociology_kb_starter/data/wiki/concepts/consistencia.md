---
id: consistencia
title: Consistencia
note_type: concept
semester: 2026-S1
course: "Metodología de las ciencias sociales"
related_concepts:
  - fiabilidad
  - validez
  - completitud
  - indicador
  - operacionalizacion
  - contrastabilidad
  - cuestionario
  - escala-likert
  - definicion-operacional
tags:
  - metodología
  - medición
  - lógica
  - diseño-de-investigación
  - filosofía-de-la-ciencia
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\modulo-2.md
updated_at: '2026-04-05'
---

## Definición

La **consistencia** es la propiedad que exige que las proposiciones de una teoría, las hipótesis derivadas de ella y los [[indicador|indicadores]] empleados para medir las variables no se contradigan entre sí. En metodología de las ciencias sociales el término opera en al menos dos planos complementarios. En el plano *lógico-teórico*, una teoría es consistente cuando de sus axiomas y supuestos no es posible deducir simultáneamente una proposición y su negación; esta acepción conecta con la noción formal de consistencia procedente de la metalógica, donde un conjunto de fórmulas es consistente si y solo si no permite derivar una contradicción. En el plano *empírico-operacional*, la consistencia designa el grado en que un instrumento de medición —un [[cuestionario]], una [[escala-likert]], un índice compuesto— produce resultados homogéneos al medir el mismo fenómeno, lo que en la tradición psicométrica se denomina *consistencia interna* y se estima habitualmente mediante el coeficiente alfa de Cronbach.

King, Keohane y Verba (2000) identifican la consistencia —junto con la [[validez]] y la [[completitud]]— como una de las tres condiciones necesarias para que las medidas empleadas en la investigación social reflejen de modo analíticamente útil la realidad que pretenden captar.

## Origen y contexto histórico

La preocupación por la consistencia lógica se remonta al principio de no contradicción formulado por Aristóteles en la *Metafísica* (libro IV): «es imposible que lo mismo se dé y no se dé en lo mismo a la vez y en el mismo sentido». En el ámbito formal, David Hilbert convirtió la demostración de consistencia de los sistemas axiomáticos en el eje de su programa fundacionalista a comienzos del siglo XX. Los teoremas de incompletitud de Kurt Gödel (1931) mostraron que ningún sistema formal suficientemente expresivo puede demostrar su propia consistencia y ser a la vez completo, resultado que impuso límites definitivos a las aspiraciones hilbertianas.

En ciencias sociales, la noción se incorporó a través de la filosofía de la ciencia neopositivista y del racionalismo crítico popperiano, que exigían coherencia lógica interna como requisito previo a la [[contrastabilidad]] empírica de las teorías. En la tradición empírica, la consistencia interna de instrumentos de medición fue sistematizada por la teoría clásica de los tests (Spearman, 1904) y consolidada con la publicación del coeficiente alfa por Lee Cronbach en 1951.

## Desarrollo teórico

### Consistencia lógica de la teoría

Una teoría científica se compone de un conjunto de proposiciones interrelacionadas. Para que resulte fructífera, ese conjunto debe ser *internamente consistente*: no puede afirmar, por ejemplo, que la variable *X* causa *Y* y simultáneamente que *X* impide *Y* bajo las mismas condiciones. La consistencia lógica es una condición necesaria —aunque no suficiente— de la calidad teórica; sin ella, cualquier conclusión es derivable (*ex falso quodlibet*), lo que priva a la teoría de contenido empírico y de posibilidad de refutación.

### Consistencia en la medición

En el plano operacional, la consistencia atañe al proceso de [[operacionalizacion]]. Cuando se traduce un concepto abstracto en [[indicador|indicadores]] observables, es imprescindible que esos indicadores guarden coherencia interna: si tres ítems de un cuestionario miden la «confianza institucional», las respuestas de un mismo sujeto deben covariar. El **alfa de Cronbach** (α) cuantifica esa covariación:

$$\alpha = \frac{k}{k-1}\left(1 - \frac{\sum \sigma_{i}^{2}}{\sigma_{T}^{2}}\right)$$

donde *k* es el número de ítems, $\sigma_{i}^{2}$ la varianza de cada ítem y $\sigma_{T}^{2}$ la varianza total. Valores superiores a 0,70 se consideran aceptables en investigación social.

### Consistencia y [[definicion-operacional]]

La [[definicion-operacional]] de una variable debe alinearse sin contradicciones con la definición conceptual y con las hipótesis en las que participa. Cuando un investigador define «participación política» como la asistencia a manifestaciones pero luego formula hipótesis que incluyen el voto como forma de participación, se produce una inconsistencia entre la operacionalización y el marco teórico que invalida las inferencias.

## Relación con otros conceptos

La consistencia mantiene una relación triádica con la [[validez]] y la [[completitud]]: las tres propiedades constituyen conjuntamente los criterios de calidad de la medición en el esquema de King, Keohane y Verba. Un instrumento puede ser internamente consistente y, sin embargo, no ser válido —medir algo distinto de lo que se pretende—; a la inversa, la validez presupone un umbral mínimo de consistencia.

La [[fiabilidad]] engloba la consistencia como una de sus facetas: un instrumento fiable produce resultados estables tanto a lo largo del tiempo (test-retest) como en la homogeneidad de sus componentes (consistencia interna). En la práctica, evaluar la consistencia interna forma parte del proceso estándar de verificación de la [[fiabilidad]] de escalas y cuestionarios.

Finalmente, la consistencia guarda un vínculo directo con la [[contrastabilidad]]: solo una teoría lógicamente consistente puede generar predicciones empíricas refutables. Si una teoría es inconsistente, cualquier resultado empírico es compatible con ella, y la contrastación pierde sentido.

## Debates y críticas

Un primer debate gira en torno a la **reducción de la consistencia al alfa de Cronbach**. Sijtsma (2009) y McNeish (2018) han mostrado que el alfa subestima la consistencia interna cuando los ítems no son tau-equivalentes y que su valor aumenta artificialmente al añadir ítems redundantes. El coeficiente omega (ω), basado en modelos de análisis factorial, ofrece una estimación más robusta, aunque su adopción sigue siendo minoritaria en la sociología empírica.

Un segundo debate concierne a la **consistencia teórica en marcos pluralistas**. Investigadores pospositivistas argumentan que la exigencia de no contradicción es un criterio demasiado rígido en las ciencias sociales, donde las teorías compiten y los fenómenos son multidimensionales. Desde la perspectiva dialéctica, ciertas contradicciones internas de una teoría podrían reflejar tensiones reales del objeto de estudio, no defectos lógicos.

## Vigencia contemporánea

En la investigación social cuantitativa actual, la evaluación de la consistencia interna se ha convertido en un requisito editorial casi universal: las revistas exigen reportar el alfa de Cronbach —o alternativas— para toda escala utilizada. La crisis de replicación (Open Science Collaboration, 2015) ha reforzado esta exigencia al evidenciar que instrumentos con baja consistencia producen hallazgos difíciles de reproducir.

En el ámbito cualitativo, la noción se traslada a la **coherencia interna del análisis**: las categorías interpretativas deben ser compatibles entre sí y con el marco conceptual adoptado. Lincoln y Guba (1985) proponen la «dependabilidad» como equivalente cualitativo de la fiabilidad/consistencia cuantitativa.

## Ejemplo empírico

En un estudio sobre actitudes hacia la redistribución económica, un equipo diseña una [[escala-likert]] de seis ítems. Tras un piloto con 200 sujetos, calcula un alfa de Cronbach de 0,58, valor inferior al umbral aceptable. El análisis ítem-total revela que dos ítems correlacionan negativamente con el resto: uno pregunta por la «justicia del sistema tributario» (percepción descriptiva) y otro por el «deseo de mayor igualdad» (actitud normativa). La inconsistencia interna se origina en una [[operacionalizacion]] defectuosa que mezcla dimensiones conceptuales distintas. Tras reformular los ítems problemáticos, el alfa asciende a 0,82, evidenciando una consistencia interna adecuada para proseguir con la investigación.

## Véase también

- [[fiabilidad]]
- [[validez]]
- [[completitud]]
- [[operacionalizacion]]
- [[contrastabilidad]]
- [[indicador]]
- [[cuestionario]]
- [[escala-likert]]
- [[definicion-operacional]]

## Fuentes

- King, G., Keohane, R. y Verba, S. (2000). *El diseño de la investigación social*. Madrid: Alianza.
- Cronbach, L. J. (1951). "Coefficient alpha and the internal structure of tests". *Psychometrika*, 16(3), 297–334.
- Sijtsma, K. (2009). "On the use, the misuse, and the very limited usefulness of Cronbach's alpha". *Psychometrika*, 74(1), 107–120.
- McNeish, D. (2018). "Thanks coefficient alpha, we'll take it from here". *Psychological Methods*, 23(3), 412–433.
- Sala, G., Borge, R. y Padró-Solanet, A. (s.f.). *Procedimientos y decisiones para determinar qué se observará*. Módulo 2, Metodología de las ciencias sociales, UOC.
- Lincoln, Y. y Guba, E. (1985). *Naturalistic Inquiry*. Newbury Park: Sage.
