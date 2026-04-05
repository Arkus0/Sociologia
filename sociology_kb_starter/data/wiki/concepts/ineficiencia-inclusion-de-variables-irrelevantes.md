---
id: ineficiencia-inclusion-de-variables-irrelevantes
title: 'Ineficiencia: inclusión de variables irrelevantes'
note_type: concept
semester: 2026-S1
course: Metodología de las ciencias sociales
related_concepts:
  - ineficiencia-estadistica
  - omision-de-variables
  - regresion
  - variable-de-control
  - multicolinealidad
  - varianza
  - variable-dependiente
  - variable-independiente
tags:
  - metodología
  - especificación de modelos
  - regresión
  - inferencia causal
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\metodologia-de-las-ciencias-sociales.md
updated_at: '2026-04-05T18:00:00+00:00'
---

# Ineficiencia: inclusión de variables irrelevantes

## Definición

La **ineficiencia por inclusión de variables irrelevantes** es un problema de especificación de modelos estadísticos que se produce cuando se incorporan al análisis de [[regresion]] variables explicativas que carecen de relación causal verdadera con la [[variable-dependiente]]. A diferencia de la [[omision-de-variables|omisión de variables relevantes]], que introduce sesgo en los estimadores, la inclusión de variables irrelevantes mantiene la insesgadez de los coeficientes estimados por mínimos cuadrados ordinarios (MCO). Sin embargo, provoca un aumento de la [[varianza]] de dichos estimadores, lo que reduce la precisión y la potencia estadística del modelo.

## Origen y contexto histórico

El problema fue formalizado en el marco de la teoría clásica de la regresión lineal múltiple durante la segunda mitad del siglo XX. King, Keohane y Verba (2000) sistematizaron su tratamiento en el contexto de las ciencias sociales, subrayando que la selección de variables debe guiarse por la teoría causal y no por criterios puramente empíricos. Burnham y Anderson (2002) reforzaron esta advertencia al vincularla al principio de parsimonia: los modelos sobreparametrizados, aunque libres de sesgo, presentan varianzas de muestreo innecesariamente elevadas.

## Desarrollo teórico

Según la teoría de MCO, cuando se añade una [[variable-independiente]] que no tiene efecto real sobre el resultado, el estimador del resto de coeficientes sigue siendo insesgado y consistente. No obstante, los errores estándar de todos los coeficientes tienden a aumentar porque los grados de libertad se reducen y la matriz de covarianzas del estimador se expande. Este fenómeno constituye una forma de [[ineficiencia-estadistica]]: se obtienen estimaciones correctas en promedio, pero con mayor dispersión muestral. En términos prácticos, los intervalos de confianza se amplían y los contrastes de hipótesis pierden potencia, incrementando la probabilidad de no detectar efectos reales (error de tipo II). El problema se agrava cuando la variable irrelevante presenta [[multicolinealidad]] con las variables relevantes, puesto que las correlaciones entre predictores inflan adicionalmente la varianza de los coeficientes.

## Relación con otros conceptos

La ineficiencia por inclusión de variables irrelevantes se sitúa en el polo opuesto del dilema de especificación respecto a la [[omision-de-variables|omisión de variables relevantes]]. Mientras que omitir una [[variable-de-control]] relevante genera sesgo —esto es, estimaciones sistemáticamente desviadas del parámetro verdadero—, incluir una variable superflua sacrifica precisión sin introducir sesgo. Este dilema es central en el [[diseno-de-investigacion-empirica|diseño de investigación empírica]], pues el investigador debe equilibrar el riesgo de sesgo (por omisión) con el riesgo de ineficiencia (por inclusión excesiva). La relación con el sobreajuste (*overfitting*) es directa: un modelo con demasiados predictores se adapta al ruido de la muestra en lugar de capturar la estructura causal subyacente, lo que deteriora su capacidad predictiva fuera de la muestra.

## Debates y críticas

Un primer debate concierne al criterio de selección de variables. Algunos autores defienden estrategias guiadas exclusivamente por la teoría causal, mientras que otros admiten procedimientos empíricos como la selección por pasos (*stepwise*), criticada por su tendencia a capitalizar el azar. Un segundo debate se refiere a la magnitud real del daño: en muestras grandes, la pérdida de eficiencia por una variable irrelevante puede ser trivial, lo que lleva a ciertos investigadores a preferir modelos sobreinclusivos como estrategia conservadora frente al sesgo por omisión. Sin embargo, la paradoja de Freedman advierte que, con muchos predictores sin relación real, algunos aparecerán significativos por azar, generando falsos positivos.

## Vigencia contemporánea

En la era del *big data* y el aprendizaje automático, el problema adquiere nuevo relieve. La disponibilidad de cientos de variables facilita la sobreparametrización. Técnicas de regularización como LASSO y Ridge abordan este dilema penalizando la complejidad del modelo, lo que permite incluir muchos candidatos y dejar que el algoritmo descarte los irrelevantes. En ciencias sociales, no obstante, la interpretabilidad causal sigue exigiendo que la selección de variables se fundamente en marcos teóricos, tal como señalan King, Keohane y Verba.

## Ejemplo empírico

Considérese un estudio que busca explicar la participación electoral a partir del nivel educativo y la edad. Si se añade como predictor el color favorito de los encuestados —variable sin relación causal plausible—, los coeficientes de educación y edad seguirán siendo insesgados, pero sus errores estándar aumentarán. El resultado puede ser que un efecto genuino de la educación deje de alcanzar significación estadística, conduciendo a la conclusión errónea de que la educación no influye en la participación.

## Véase también

- [[ineficiencia-estadistica]]
- [[omision-de-variables]]
- [[regresion]]
- [[multicolinealidad]]
- [[variable-de-control]]
- [[varianza]]
- [[sesgo-de-seleccion]]
- [[variable-dependiente]]
- [[variable-independiente]]

## Fuentes

- King, G., Keohane, R. y Verba, S. (2000). *El diseño de la investigación social*. Alianza Editorial.
- Brady, H. E. y Collier, D. (2010). *Rethinking Social Inquiry*. Rowman & Littlefield.
- Burnham, K. P. y Anderson, D. R. (2002). *Model Selection and Multimodel Inference*. Springer-Verlag.
- Lago, I. (2026). Apuntes de Metodología de las Ciencias Sociales, módulo 2. Universidad Pompeu Fabra.
