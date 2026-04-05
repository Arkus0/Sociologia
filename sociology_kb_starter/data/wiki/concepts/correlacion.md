---
id: correlacion
title: "Correlación"
note_type: concept
semester: 2026-S1
course: Metodologia de las ciencias sociales
related_concepts:
  - causalidad
  - relacion-espuria
  - covarianza
  - regresion
  - variable-dependiente
  - variable-independiente
  - estadistica-descriptiva
  - estadistica-inferencial
  - operacionalizacion
tags:
  - Metodologia de las ciencias sociales
  - Estadística
  - Análisis cuantitativo
  - Relación entre variables
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\modulo-3.md
updated_at: "2026-04-05"
---

# Correlación

## Definición

La **correlación** es una medida estadística que cuantifica el grado de asociación lineal entre dos variables. Se expresa mediante un coeficiente que oscila entre −1 (relación inversa perfecta) y +1 (relación directa perfecta), siendo 0 la ausencia de relación lineal. En ciencias sociales, la correlación permite detectar regularidades empíricas —por ejemplo, la asociación entre nivel educativo e ingreso— sin que ello implique, por sí solo, un vínculo causal. Se distingue así de la [[causalidad]], que exige condiciones adicionales (mecanismo, temporalidad, control de terceras variables). En el marco del análisis cuantitativo, la correlación forma parte de la [[estadistica-descriptiva]] cuando resume datos observados y de la [[estadistica-inferencial]] cuando se extrapola a la población mediante pruebas de significación.

## Origen

El concepto tiene raíces en la estadística británica del siglo XIX. **Francis Galton** (1822-1911) introdujo la noción de *co-relación* en sus estudios sobre herencia biológica, observando el fenómeno que llamó *regresión a la media*. Su discípulo **Karl Pearson** (1857-1936) formalizó el coeficiente producto-momento (r de Pearson), definiéndolo como el cociente entre la [[covarianza]] de dos variables y el producto de sus desviaciones estándar. En el ámbito sociológico, Émile Durkheim anticipó la lógica correlacional con su método de las *variaciones concomitantes* en *Las reglas del método sociológico* (1895): si dos fenómenos varían conjuntamente de modo sistemático, existe razón para sospechar un nexo explicativo.

## Desarrollo teórico

El campo ha generado diversas variantes del coeficiente según los supuestos y el nivel de medición de las variables:

- **Correlación de Pearson (r)**: mide la asociación lineal entre variables de intervalo o razón. Supone distribución aproximadamente normal y relación lineal. Es sensible a valores atípicos (*outliers*).
- **Correlación de Spearman (ρ)**: correlación de rangos, aplicable a variables ordinales o cuando no se cumplen los supuestos de normalidad. Mide la monotonía de la relación sin exigir linealidad estricta.
- **Correlación parcial**: controla el efecto de una o más terceras variables, aislando la relación neta entre las dos variables de interés. Resulta fundamental para detectar [[relacion-espuria|relaciones espurias]], donde una asociación aparente se debe a una variable confundente.
- **Correlación ecológica**: calculada sobre datos agregados (regiones, países) en lugar de individuos. W. S. Robinson (1950) demostró que extrapolar correlaciones ecológicas al nivel individual constituye una falacia (*paradoja de Robinson*), hallazgo clave para la sociología empírica.

La distinción entre correlación y causalidad constituye un principio epistemológico central. Karl Popper subrayó que las regularidades observadas (correlaciones) no prueban leyes universales: el problema de la inducción impide derivar certeza de la repetición empírica. Judea Pearl profundizó esta distinción al formalizar modelos causales estructurales donde la asociación estadística y la intervención causal operan en niveles lógicos distintos. Donald Campbell, por su parte, mostró que los cuasiexperimentos sociales pueden explotar correlaciones mediante diseños que aproximan —sin alcanzar— el control experimental pleno. El módulo de la UOC sobre investigación cuantitativa sitúa la correlación junto a la [[regresion]] como herramienta de la estadística multivariada, diferenciándola del análisis univariado.

## Relación con otros conceptos

La correlación se articula con una constelación de conceptos metodológicos. La [[covarianza]] es su precursora algebraica sin estandarizar. La [[regresion]] extiende la correlación al modelar la [[variable-dependiente]] como función de una o más [[variable-independiente|variables independientes]]. La [[relacion-espuria]] representa su principal trampa interpretativa. La [[operacionalizacion]] determina la calidad de los indicadores cuyas correlaciones se calculan: indicadores mal operacionalizados producen correlaciones artefactuales. La paradoja de Simpson —donde una correlación se invierte al desagregar los datos por categorías— ilustra la fragilidad del análisis bivariado simple y la necesidad del análisis multivariado.

## Debates y críticas

Tres debates atraviesan el uso de la correlación en ciencias sociales. Primero, la **correlación como sustituto causal**: investigadores sin acceso a diseños experimentales recurren a correlaciones como evidencia indirecta, práctica criticada desde el positivismo lógico y el realismo crítico. Segundo, el **big data** ha reactivado la tensión entre predicción y explicación: algoritmos de aprendizaje automático explotan correlaciones masivas para predecir comportamientos sin ofrecer mecanismos causales. Tercero, la **multiplicidad de pruebas**: al calcular cientos de correlaciones, hallazgos significativos emergen por azar, lo que exige correcciones como Bonferroni.

## Vigencia contemporánea

La correlación sigue siendo la puerta de entrada al análisis relacional en sociología cuantitativa, pero su interpretación se ha enriquecido. Los modelos de ecuaciones estructurales combinan correlaciones observadas con teoría causal latente. Las técnicas de *machine learning* explotan correlaciones no lineales, invisibles a Pearson, con gran capacidad predictiva. Sin embargo, Pearl insiste en que ningún volumen de datos correlacionales reemplaza el razonamiento causal estructural. La tensión entre correlación y causalidad permanece como eje articulador de la metodología social.

## Ejemplo empírico

Durkheim observó una variación concomitante entre la tasa de suicidio y el grado de integración religiosa: las regiones protestantes presentaban tasas más altas que las católicas. Esta correlación ecológica fundamentó su teoría del suicidio egoísta, aunque estudios posteriores mostraron que la relación se debilitaba al controlar variables como la urbanización —un caso clásico de correlación parcial que matiza la asociación original.

## Véase también

- [[causalidad]]
- [[relacion-espuria]]
- [[covarianza]]
- [[regresion]]
- [[variable-dependiente]]
- [[variable-independiente]]
- [[estadistica-descriptiva]]
- [[estadistica-inferencial]]
- [[operacionalizacion]]
- [[proceso-de-investigacion]]

## Fuentes

- [[la-investigacion-cuantitativa]] (Metodologia de las ciencias sociales, Módulo 3)
- Galton, F. (1888). *Co-relations and their measurement*. Proceedings of the Royal Society.
- Pearson, K. (1896). *Mathematical contributions to the theory of evolution*. Philosophical Transactions.
- Robinson, W. S. (1950). Ecological correlations and the behavior of individuals. *American Sociological Review*, 15(3).
- Pearl, J. (2009). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
- Durkheim, É. (1895). *Las reglas del método sociológico*.
