---
id: estadistica-inferencial
title: Estadística inferencial
note_type: concept
semester: 2026-S1
course: "Metodologia de las ciencias sociales"
related_concepts:
  - estadistica-descriptiva
  - muestra
  - nivel-de-confianza
  - hipotesis
  - chi-cuadrado
  - regresion
  - variable
  - probabilidad
tags:
  - metodología
  - estadística
  - investigación cuantitativa
  - inferencia
  - prueba de hipótesis
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\la-investigacion-cuantitativa.md
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\modulo-3.md
updated_at: '2025-07-13'
---

## Definición

La **estadística inferencial** es la rama de la estadística que se ocupa de extraer conclusiones, generalizaciones y predicciones acerca de una [[poblacion-estadistica|población]] a partir del análisis de una [[muestra]] representativa. A diferencia de la [[estadistica-descriptiva]], que se limita a resumir y organizar los datos observados, la estadística inferencial emplea métodos probabilísticos para extrapolar los resultados muestrales al conjunto de la población de referencia. Como señala la bibliografía del curso de Metodología, «la estadística inferencial es la que intenta inferir los parámetros poblacionales de los valores estadísticos observados en la muestra» (Módulo 3).

En las ciencias sociales, esta rama resulta indispensable porque los investigadores rara vez pueden estudiar la totalidad de una población: trabajan con muestras y necesitan herramientas formales para determinar si los patrones encontrados son generalizables o si podrían deberse al azar muestral.

## Origen y contexto histórico

Los fundamentos de la estadística inferencial se consolidan entre finales del siglo XIX y la primera mitad del siglo XX. **Ronald A. Fisher** (1890-1962) sentó las bases de la prueba de significación estadística en obras como *Statistical Methods for Research Workers* (1925), introduciendo el concepto de *p-value* como medida de la evidencia contra una hipótesis nula. Fisher concebía el contraste como un procedimiento inductivo: los datos «hablan» y el investigador interpreta la fuerza de la evidencia.

Poco después, **Jerzy Neyman** y **Egon Pearson** propusieron en la década de 1930 un marco alternativo centrado en la toma de decisiones: la distinción formal entre hipótesis nula (H₀) e hipótesis alternativa (H₁), los errores de tipo I y tipo II, y la noción de potencia estadística. Este enfoque —más deductivo— buscaba establecer reglas de decisión a largo plazo que controlasen las tasas de error.

Paralelamente, la tradición **bayesiana**, con raíces en el teorema de Thomas Bayes (1763), fue marginal durante gran parte del siglo XX pero resurgió con fuerza a partir de los años 1990, impulsada por el aumento de la capacidad computacional y los métodos de simulación como las cadenas de Markov (MCMC).

## Desarrollo teórico

La estadística inferencial abarca dos grandes familias de procedimientos:

1. **Estimación de parámetros**: busca aproximar valores desconocidos de la población. Puede ser *puntual* (un único valor, como la media muestral como estimador de la media poblacional) o *intervalar* (un rango de valores plausibles expresado mediante un [[nivel-de-confianza|intervalo de confianza]]).

2. **Contraste de hipótesis**: permite decidir, con un nivel de riesgo controlado, si los datos muestrales son compatibles con una [[hipotesis|hipótesis]] formulada sobre la población. El procedimiento clásico incluye la formulación de H₀ y H₁, la elección de un nivel de significación (α), el cálculo de un estadístico de prueba y su comparación con una distribución teórica.

Entre las pruebas inferenciales más utilizadas en ciencias sociales se encuentran:

- La prueba *t* de Student para comparar medias.
- El análisis de varianza (**ANOVA**) para comparar más de dos grupos.
- La prueba de [[chi-cuadrado]] (χ²) para analizar relaciones entre variables categóricas.
- Los modelos de [[regresion|regresión]] lineal y logística para estudiar relaciones entre variables.

## Relación con otros conceptos

La estadística inferencial presupone y complementa a la [[estadistica-descriptiva]]: todo análisis inferencial comienza con la descripción y la representación visual de los datos. A su vez, depende críticamente de la calidad del [[muestra|muestreo]]; una muestra sesgada invalida cualquier inferencia, por sofisticada que sea la técnica empleada.

El concepto de [[nivel-de-confianza]] es central: expresa la probabilidad de que el intervalo calculado contenga el verdadero parámetro poblacional. Las [[hipotesis|hipótesis]] de investigación se traducen en hipótesis estadísticas susceptibles de contraste. King, Keohane y Verba (2000) sostienen que la lógica inferencial es común a los métodos cuantitativos y cualitativos; lo que varía es la forma de seleccionar y recoger datos, no el razonamiento subyacente.

## Debates y críticas

La práctica de la estadística inferencial ha sido objeto de intensos debates:

- **Fisher vs. Neyman-Pearson**: la confusión entre ambos marcos —frecuente en manuales de ciencias sociales— lleva a un «híbrido incoherente» donde se reporta el *p-value* fisheriano pero se interpreta como regla de decisión neymaniana. Gigerenzer (2004) denominó a esta mezcla «el ritual nulo» (*null ritual*).

- **Crisis de replicación**: desde mediados de la década de 2010, numerosos estudios en psicología y sociología no pudieron ser replicados, poniendo en cuestión el uso mecánico de umbrales de significación (p < 0,05). La **American Statistical Association** emitió en 2016 una declaración histórica advirtiendo contra la interpretación simplista de los *p-values* y señalando que «ningún índice único debe sustituir al razonamiento científico».

- **Karl Popper** y la filosofía de la ciencia: desde una lectura popperiana, las pruebas estadísticas pueden entenderse como intentos de falsación; sin embargo, la confirmación por vía estadística no equivale a verificación definitiva, lo que refuerza la necesidad de replicación y triangulación de métodos.

- **Tamaño del efecto vs. significación**: numerosos metodólogos insisten en que la significación estadística no equivale a relevancia sustantiva. Un efecto puede ser estadísticamente significativo pero trivial en términos prácticos, especialmente con muestras grandes.

## Vigencia contemporánea

En la investigación social actual conviven tres paradigmas inferenciales:

1. El **frecuentista clásico**, aún predominante en encuestas y estudios experimentales.
2. La **inferencia bayesiana**, cada vez más adoptada en ciencias sociales gracias a software como Stan y a la posibilidad de incorporar información previa (*priors*) en el análisis.
3. Los **métodos basados en simulación y remuestreo** (*bootstrap*, permutaciones), que relajan supuestos distribucionales y resultan especialmente útiles con muestras pequeñas o distribuciones no normales.

La tendencia contemporánea apunta hacia la complementariedad: reportar intervalos de confianza y tamaños del efecto junto con (o en lugar de) los *p-values*, utilizar análisis bayesianos cuando la información previa es relevante, y priorizar la replicabilidad y la transparencia en el diseño de investigación.

## Ejemplo empírico

Un equipo de investigación desea saber si el nivel educativo de los padres influye en las aspiraciones profesionales de los hijos en una ciudad. No puede encuestar a toda la población, por lo que selecciona una [[muestra]] aleatoria de 400 familias. Calcula la media de aspiraciones profesionales (variable ordinal) para cada nivel educativo parental (primario, secundario, universitario) y aplica un **ANOVA** para determinar si las diferencias entre los grupos son estadísticamente significativas. Con un *p-value* inferior a 0,01 y un tamaño del efecto (η²) de 0,12, concluye que existen diferencias relevantes entre grupos, lo que sugiere que el capital cultural transmitido por la familia —en línea con Bourdieu— tiene un efecto mesurable sobre las expectativas de los hijos.

## Véase también

- [[estadistica-descriptiva]]
- [[muestra]]
- [[nivel-de-confianza]]
- [[hipotesis]]
- [[chi-cuadrado]]
- [[regresion]]
- [[variable]]
- [[proceso-de-investigacion]]

## Fuentes

- Material del curso: *Metodología de las ciencias sociales*, Módulo 3 – «El análisis estadístico de los datos» (UOC, 2026-S1).
- Material del curso: *La investigación cuantitativa: encuesta, experimento y análisis estadístico* (UOC, 2026-S1).
- Fisher, R. A. (1925). *Statistical Methods for Research Workers*. Edinburgh: Oliver & Boyd.
- Neyman, J. y Pearson, E. S. (1933). «On the Problem of the Most Efficient Tests of Statistical Hypotheses». *Philosophical Transactions of the Royal Society A*, 231, 289-337.
- King, G., Keohane, R. O. y Verba, S. (2000). *El diseño de la investigación social*. Madrid: Alianza.
- Gigerenzer, G. (2004). «Mindless Statistics». *Journal of Socio-Economics*, 33(5), 587-606.
- Wasserstein, R. L. y Lazar, N. A. (2016). «The ASA Statement on p-Values». *The American Statistician*, 70(2), 129-133.
- Wikipedia contributors. «Estadística inferencial». *Wikipedia, la enciclopedia libre*.
