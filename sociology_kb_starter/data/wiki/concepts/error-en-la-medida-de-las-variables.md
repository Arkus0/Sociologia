---
id: error-en-la-medida-de-las-variables
title: "Error en la medida de las variables"
note_type: concept
semester: 2026-S1
course: Metodología de las ciencias sociales
related_concepts:
  - "[[fiabilidad]]"
  - "[[validez]]"
  - "[[indicador]]"
  - "[[operacionalizacion]]"
  - "[[cuestionario]]"
  - "[[variable-dependiente]]"
  - "[[variable-independiente]]"
  - "[[regresion]]"
  - "[[correlacion]]"
  - "[[sesgo-del-entrevistador]]"
  - "[[error-muestral]]"
tags:
  - metodología
  - medición
  - error-sistemático
  - error-aleatorio
  - inferencia-causal
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\metodologia-de-las-ciencias-sociales.md
updated_at: '2026-04-05T18:00:00+00:00'
---

# Error en la medida de las variables

## Definición

El error en la medida de las variables designa la discrepancia entre el valor observado de una variable y su valor verdadero. En términos formales, si $Y^*$ es el valor verdadero y $Y$ el valor registrado, el error de medición $e$ se define como $e = Y - Y^*$. Este error puede descomponerse en dos componentes aditivos: el **error sistemático** (sesgo), que desplaza las mediciones de manera constante en una dirección determinada, y el **error aleatorio** (ruido), que introduce variaciones impredecibles de una observación a otra. Mientras que el error aleatorio se relaciona con la [[fiabilidad]] del instrumento —su capacidad de producir resultados consistentes—, el error sistemático compromete la [[validez]] de la medición, es decir, la correspondencia entre lo que se mide y lo que se pretende medir.

## Origen y contexto histórico

La reflexión sobre los errores de medición se remonta a la astronomía y la física del siglo XVIII, cuando la teoría de los mínimos cuadrados de Gauss y Legendre proporcionó un marco matemático para tratar las discrepancias observacionales. En las ciencias sociales, el problema adquirió relevancia a mediados del siglo XX, cuando la difusión de encuestas y técnicas estadísticas puso de manifiesto que conceptos como actitudes, creencias o clase social no se observan directamente, sino a través de [[indicador|indicadores]] imperfectos. King, Keohane y Verba (2000) situaron el error de medición como uno de los problemas centrales de la inferencia causal, junto con el sesgo de selección de casos, la multicolinealidad y la omisión de variables relevantes.

## Desarrollo teórico

El proceso de [[operacionalizacion]] —la traducción de un concepto abstracto en variables observables— constituye la fuente primaria de error de medición en la investigación social. Cuando un investigador diseña un [[cuestionario]], cada pregunta funciona como un [[indicador]] que aproxima una dimensión del concepto teórico, pero ningún indicador lo capta perfectamente.

El **error aleatorio** se manifiesta como variación no sistemática en las respuestas: diferencias de interpretación entre encuestados, fluctuaciones en la atención o ambigüedades en la formulación de las preguntas. Su efecto principal es reducir la precisión de las estimaciones; sin embargo, al ser no correlacionado, puede mitigarse aumentando el tamaño de la muestra o promediando múltiples indicadores.

El **error sistemático**, en cambio, sesga las estimaciones en una dirección constante. Fuentes habituales en ciencias sociales incluyen el [[sesgo-del-entrevistador]], la deseabilidad social, los efectos de orden en el cuestionario o la calibración inadecuada de escalas. A diferencia del error aleatorio, el error sistemático no se reduce con la repetición de mediciones y requiere estrategias específicas de diseño para su control.

Un resultado estadístico fundamental es que el error de medición en la [[variable-independiente]] produce **sesgo de atenuación**: los coeficientes de [[regresion]] se subestiman sistemáticamente, acercándose a cero. Si, por el contrario, el error afecta solo a la [[variable-dependiente]], los coeficientes permanecen insesgados, pero el coeficiente de determinación ($R^2$) disminuye. Esta asimetría tiene consecuencias prácticas decisivas para la investigación empírica.

## Relación con otros conceptos

El error de medición se vincula estrechamente con la [[fiabilidad]] y la [[validez]], los dos criterios fundamentales de calidad de un instrumento. Una medición fiable presenta bajo error aleatorio; una medición válida presenta bajo error sistemático. Asimismo, el concepto se conecta con el [[error-muestral]], aunque ambos operan en planos distintos: el error muestral se refiere a la discrepancia entre una estimación muestral y el parámetro poblacional derivada del proceso de selección de casos, mientras que el error de medición afecta a la calidad de los datos individuales. La [[correlacion]] observada entre dos variables medidas con error será siempre inferior a la correlación verdadera, un fenómeno conocido como atenuación.

## Debates y críticas

Una línea de discusión relevante se refiere a si el error de medición puede considerarse verdaderamente aleatorio en ciencias sociales. Varios autores argumentan que los patrones de respuesta en encuestas suelen presentar componentes sistemáticos difíciles de distinguir del ruido aleatorio. Otra crítica apunta a la dificultad de estimar la magnitud del error cuando no existe un estándar de referencia externo —un «valor verdadero» conocido—, situación habitual al medir conceptos latentes como la ideología política o la cohesión social. Los modelos de ecuaciones estructurales y la teoría clásica de los tests ofrecen soluciones parciales, pero descansan sobre supuestos no siempre verificables.

## Vigencia contemporánea

Con la expansión de los métodos mixtos, los datos digitales y las técnicas de procesamiento de lenguaje natural, las fuentes de error de medición se han diversificado. La codificación automatizada de textos, la medición de sentimientos en redes sociales o el uso de registros administrativos como proxies de variables sociológicas introducen formas de error que no encajan plenamente en la dicotomía clásica. La corrección por error de medición —mediante variables instrumentales, modelos MTMM (multirrasgo-multimétodo) o calibración con submuestras— sigue siendo un área activa de desarrollo metodológico.

## Ejemplo empírico

En una encuesta sobre satisfacción con la democracia, la pregunta «¿Está usted satisfecho con el funcionamiento de la democracia en su país?» introduce error de medición por varias vías. Encuestados con distintos marcos de referencia interpretan «funcionamiento» de maneras diferentes (error aleatorio). Si la encuesta se realiza en período electoral, la exposición a campañas puede desplazar las respuestas hacia posiciones más extremas (error sistemático). Un análisis de [[regresion]] que utilice esta variable como predictor subestimará su efecto real sobre el comportamiento de voto, ilustrando el sesgo de atenuación.

## Véase también

- [[fiabilidad]]
- [[validez]]
- [[operacionalizacion]]
- [[indicador]]
- [[cuestionario]]
- [[variable-independiente]]
- [[variable-dependiente]]
- [[error-muestral]]
- [[sesgo-del-entrevistador]]
- [[regresion]]

## Fuentes

- King, G., Keohane, R. y Verba, S. (2000). *El diseño de la investigación social*. Alianza Editorial.
- Brady, H. E. y Collier, D. (2010). *Rethinking Social Inquiry*. Rowman & Littlefield.
- Saris, W. E. y Gallhofer, I. N. (2014). *Design, Evaluation and Analysis of Questionnaires for Survey Research*. Wiley.
- Bland, J. M. y Altman, D. G. (1996). «Statistics Notes: Measurement Error». *BMJ*, 313(7059), 744.
- Cochran, W. G. (1968). «Errors of Measurement in Statistics». *Technometrics*, 10(4), 637–666.
