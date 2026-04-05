---
id: regresion
title: "Regresión"
note_type: concept
semester: 2026-S1
course: Metodologia de las ciencias sociales
related_concepts:
  - correlacion
  - causalidad
  - variable-dependiente
  - variable-independiente
  - variable-de-control
  - estadistica-inferencial
  - endogeneidad
  - multicolinealidad
  - omision-de-variables
tags:
  - estadistica
  - metodos-cuantitativos
  - inferencia-causal
  - modelizacion
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\modulo-3.md
updated_at: "2026-04-05"
---

## Definición

El **análisis de regresión** es una técnica estadística que modela la relación funcional entre una [[variable-dependiente]] y una o más [[variable-independiente|variables independientes]]. Su objetivo es estimar cómo cambia el valor esperado de la variable de respuesta cuando se modifican los predictores, manteniendo constantes las demás condiciones. En su forma más elemental — la regresión lineal simple — se ajusta una recta que minimiza la suma de los residuos al cuadrado, procedimiento conocido como **mínimos cuadrados ordinarios** (OLS, *ordinary least squares*). Cuando el modelo incorpora varios predictores se habla de regresión múltiple; cuando la variable dependiente es categórica (por ejemplo, dicotómica) se recurre a la **regresión logística**. La regresión constituye la herramienta cuantitativa más utilizada en ciencias sociales para explorar asociaciones, controlar variables confusoras y, bajo determinados supuestos, aproximar relaciones de [[causalidad]].

## Origen

El término «regresión» fue acuñado por Francis Galton en la década de 1880 al estudiar la herencia de la estatura: observó que los hijos de padres excepcionalmente altos tendían a acercarse a la media poblacional, fenómeno que denominó *regression toward mediocrity* (regresión hacia la mediocridad). Aunque Galton le atribuyó un sentido estrictamente biológico, el método de mínimos cuadrados ya había sido formalizado décadas antes por Legendre (1805) y Gauss (1809) para calcular órbitas planetarias. Fue Karl Pearson, junto con Udny Yule, quien a finales del siglo XIX generalizó la regresión como procedimiento estadístico, vinculándola al [[correlacion|coeficiente de correlación]] y a la distribución normal conjunta de las variables.

## Desarrollo teórico

Ronald A. Fisher transformó la regresión en una herramienta inferencial rigurosa al demostrar, en sus trabajos de 1922 y 1925, que bastaba asumir normalidad condicional de los errores —sin exigir normalidad conjunta— para derivar pruebas de hipótesis y análisis de varianza (ANOVA). Con ello, la regresión dejó de ser un mero ajuste descriptivo y se convirtió en el pilar de la [[estadistica-inferencial]].

En sociología, Paul Lazarsfeld promovió durante las décadas de 1940-1960 el uso sistemático de la regresión para analizar encuestas y estudios de opinión pública, sentando las bases de la investigación cuantitativa empírica. John Goldthorpe, desde la sociología analítica británica, integró modelos de regresión con la teoría de la acción racional para explicar desigualdades educativas y de clase social.

Los supuestos clásicos del modelo OLS incluyen: (1) linealidad de la relación, (2) independencia de los errores, (3) homocedasticidad —varianza constante de los residuos— y (4) normalidad de los términos de error. El teorema de Gauss-Markov garantiza que, bajo estos supuestos, el estimador OLS es el mejor estimador lineal insesgado (BLUE). Sin embargo, la violación de estos supuestos conduce a problemas bien documentados: la [[multicolinealidad]] infla la varianza de los coeficientes; la heterocedasticidad invalida los errores estándar clásicos; la [[endogeneidad]] —debida a [[omision-de-variables|omisión de variables]], simultaneidad o error de medición— sesga los estimadores; y la selección muestral no aleatoria distorsiona la inferencia.

## Relación con otros conceptos

La regresión se vincula estrechamente con la [[correlacion]], aunque no debe confundirse con ella: la correlación mide la fuerza de la asociación lineal entre dos variables sin distinguir dependiente de independiente, mientras que la regresión modela una dirección causal o predictiva específica. El uso de [[variable-de-control|variables de control]] en la regresión múltiple permite aislar el efecto parcial de cada predictor, estrategia central en la investigación observacional. Técnicas como las variables instrumentales, los efectos fijos (*fixed effects*) y las diferencias en diferencias (*differences-in-differences*) se desarrollaron para abordar la [[endogeneidad]] y aproximar inferencias causales a partir de datos no experimentales.

## Debates y críticas

David Freedman argumentó que la regresión, sin una teoría sustantiva sólida, se reduce a un mero ajuste de curvas (*curve fitting*) que nada dice sobre mecanismos causales. Desde la filosofía de las ciencias sociales, Friedrich Hayek advirtió sobre los límites de la predictibilidad en sistemas complejos, cuestionando la aspiración de replicar en lo social la precisión cuantitativa de las ciencias naturales. Judea Pearl, por su parte, señaló que los coeficientes de regresión carecen de interpretación causal sin un modelo estructural (DAG) que explicite las relaciones entre variables, lo que llevó al desarrollo de los modelos de ecuaciones estructurales. En contraposición, Joshua Angrist y Jörn-Steffen Pischke defendieron la regresión como herramienta privilegiada para la inferencia causal cuando se combina con diseños cuasi-experimentales (variables instrumentales, regresión discontinua, diferencias en diferencias), posición expuesta en *Mostly Harmless Econometrics* (2009).

## Vigencia contemporánea

En la investigación social actual, la regresión sigue siendo la técnica cuantitativa dominante, aunque el panorama metodológico se ha ampliado considerablemente. El auge del *machine learning* ha introducido algoritmos predictivos —bosques aleatorios, redes neuronales, métodos de regularización (LASSO, Ridge)— que compiten con la regresión en capacidad predictiva. Sin embargo, cuando el objetivo es la interpretación causal y no solo la predicción, la regresión mantiene ventajas de transparencia y parsimonia. El desarrollo de los métodos de inferencia causal computacional (estimadores de doble robustez, *targeted learning*) combina técnicas de aprendizaje automático con el marco de la regresión para obtener estimaciones causales más flexibles y robustas.

## Ejemplo empírico

En un estudio sobre desigualdad salarial de género, un modelo de regresión múltiple podría especificar el ingreso mensual como [[variable-dependiente]] y el género, la educación, la experiencia laboral y el sector económico como [[variable-independiente|variables independientes]]. El coeficiente asociado al género estimaría la brecha salarial media entre hombres y mujeres *controlando* por las demás variables. Si existieran factores no observados (motivación, redes de contacto) correlacionados tanto con el género como con el salario, el coeficiente padecería sesgo por [[omision-de-variables]]; en tal caso, podrían emplearse variables instrumentales o diseños de efectos fijos para mitigar la [[endogeneidad]].

## Véase también

- [[correlacion]]
- [[causalidad]]
- [[variable-dependiente]]
- [[variable-independiente]]
- [[variable-de-control]]
- [[estadistica-inferencial]]
- [[endogeneidad]]
- [[multicolinealidad]]
- [[omision-de-variables]]

## Fuentes

- Galton, F. (1886). *Regression Towards Mediocrity in Hereditary Stature*. Journal of the Anthropological Institute.
- Fisher, R. A. (1925). *Statistical Methods for Research Workers*. Oliver and Boyd.
- Freedman, D. A. (2009). *Statistical Models: Theory and Practice*. Cambridge University Press.
- Angrist, J. D. y Pischke, J.-S. (2009). *Mostly Harmless Econometrics*. Princeton University Press.
- Pearl, J. (2009). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
- Borge Bravo, R. y Padró-Solanet, A. (2026). *La investigación cuantitativa*. Módulo 3, Metodología de las ciencias sociales — UOC.
- Wikipedia contributors. "Regression analysis". *Wikipedia, The Free Encyclopedia*. Consultado el 5 de abril de 2026.
