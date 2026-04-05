---
id: endogeneidad-confusion-de-causas-y-de-consecuencias
title: "Endogeneidad: confusión de causas y de consecuencias"
note_type: concept
semester: 2026-S1
course: "Metodología de las ciencias sociales"
related_concepts:
  - endogeneidad
  - causalidad
  - validez-interna
  - variable-independiente
  - variable-dependiente
  - variable-interviniente
  - relacion-espurea
  - sesgo-de-seleccion
  - correlacion
  - regresion
  - omision-de-variables
tags:
  - metodologia
  - causalidad
  - inferencia-causal
  - sesgo
  - endogeneidad
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\metodologia-de-las-ciencias-sociales.md
updated_at: "2026-04-05"
---

## Definición

La **confusión de causas y de consecuencias** es una manifestación específica del problema de [[endogeneidad]] en la que el investigador no logra distinguir la dirección del nexo causal entre dos variables. En lugar de que la [[variable-independiente]] $x$ cause la [[variable-dependiente]] $y$, puede ocurrir que $y$ influya sobre $x$ (causalidad inversa), que ambas se determinen mutuamente (simultaneidad) o que una tercera variable no observada genere una [[relacion-espurea]] entre ellas. Cuando la dirección de la [[causalidad]] está indeterminada, las estimaciones obtenidas mediante mínimos cuadrados ordinarios resultan sesgadas e inconsistentes, y toda inferencia causal pierde sustento.

Formalmente, en un modelo de [[regresion]] lineal $y_i = \alpha + \beta x_i + \varepsilon_i$, la confusión de causas y consecuencias implica que $\text{Cov}(x_i, \varepsilon_i) \neq 0$ porque parte del efecto atribuido a $x$ procede en realidad de $y$ o de factores omitidos comunes a ambas. El estimador $\hat{\beta}$ deja de aproximar el verdadero efecto causal, comprometiendo la [[validez-interna]] de la investigación.

## Origen y contexto histórico

El problema fue formalizado en el marco de los modelos de ecuaciones simultáneas desarrollados por la Cowles Commission (Haavelmo, Koopmans) durante las décadas de 1940 y 1950, cuando la econometría distinguió entre variables endógenas —determinadas dentro del sistema— y exógenas —predeterminadas fuera de él—. El ejemplo clásico es la relación entre precio y cantidad en un mercado: la demanda depende del precio, pero el precio se ajusta a la demanda, de modo que estimar cualquiera de las dos ecuaciones estructurales por separado genera sesgo de simultaneidad. En las ciencias sociales, King, Keohane y Verba (2000) trasladaron estas preocupaciones al diseño de investigación cualitativo-comparativo, e Ignacio Lago (2008) sistematizó la exposición para la ciencia política hispanohablante, subrayando que la confusión de causas y consecuencias es una de las amenazas más frecuentes a la inferencia válida.

## Desarrollo teórico

La confusión de causas y de consecuencias puede originarse por tres vías principales, todas ellas tratadas como formas de [[endogeneidad]]:

1. **Causalidad inversa (o reversa).** Si la supuesta variable explicativa $x$ es en realidad consecuencia de $y$, el modelo invierte la dirección del efecto. Por ejemplo, atribuir el nivel de democratización a la riqueza nacional puede ignorar que la democracia también favorece el crecimiento económico.

2. **Simultaneidad.** Cuando $x$ causa $y$ y a la vez $y$ causa $x$, ambas variables se codeterminan. En las ecuaciones estructurales $y_i = \beta_1 x_i + u_i$ y $x_i = \gamma_2 y_i + v_i$, estimar cualquiera de ellas por separado produce $E(x_i u_i) \neq 0$.

3. **[[omision-de-variables|Omisión de variables relevantes]].** Una [[variable-interviniente]] no observada $z$ afecta simultáneamente a $x$ y a $y$; su efecto queda absorbido por el término de error y genera [[correlacion]] entre $x$ y $\varepsilon$. El resultado es una asociación estadística que no refleja un nexo causal genuino.

En los tres casos, la consecuencia analítica es idéntica: el coeficiente estimado $\hat{\beta}$ no puede interpretarse como efecto causal.

## Relación con otros conceptos

La confusión de causas y de consecuencias se sitúa en el cruce de varios problemas metodológicos. Comparte mecanismo con la [[relacion-espurea]], pues una variable omitida puede producir una asociación estadística sin que exista nexo causal directo. Se vincula con el [[sesgo-de-seleccion]] cuando la muestra se construye a partir de la variable dependiente, invirtiendo implícitamente la lógica causal —un riesgo que King, Keohane y Verba señalaron como análogo a la endogeneidad en el diseño comparativo—. Asimismo, guarda relación con la [[correlacion]]: constatar que dos variables covarían no permite establecer cuál es causa y cuál efecto, distinción que el investigador debe fundamentar teóricamente.

## Debates y críticas

La solución canónica es la **estimación por variables instrumentales**: se introduce una variable $z$ correlacionada con la variable endógena pero no con el error, lo que permite aislar la variación exógena de $x$. No obstante, encontrar instrumentos válidos es extremadamente difícil; la restricción de exclusión es inverificable empíricamente y un instrumento débil puede amplificar el sesgo. Angrist y Pischke (2009) sistematizaron estrategias de identificación —experimentos naturales, regresión discontinua, diferencias en diferencias— orientadas a resolver la confusión causal sin supuestos estructurales fuertes. Desde otro enfoque, Judea Pearl propuso los grafos acíclicos dirigidos (DAGs) como herramienta para explicitar los supuestos causales y detectar si el modelo confunde causas con consecuencias. Los críticos señalan que, en las ciencias sociales, donde la experimentación es a menudo inviable, la amenaza persiste y exige, ante todo, una formulación teórica rigurosa de la dirección causal antes de la estimación.

## Vigencia contemporánea

El problema de la confusión de causas y consecuencias estructura buena parte de la agenda metodológica actual. La expansión de los diseños cuasiexperimentales, los experimentos de campo y las técnicas de *machine learning* causal responde a la necesidad de obtener estimaciones creíbles cuando la asignación al tratamiento no es aleatoria. En sociología, la discusión se extiende al análisis cualitativo: la selección de casos por la variable dependiente puede entenderse como una forma análoga de inversión causal en el plano del diseño comparativo.

## Ejemplo empírico

Un investigador desea estimar el efecto de la presencia policial ($x$) sobre la tasa de delincuencia ($y$) en distintos barrios. Si se observa una [[correlacion]] positiva entre ambas variables, ¿significa que más policías causan más delitos? La interpretación es evidentemente absurda; lo que ocurre es que la asignación policial responde a la delincuencia previa: los barrios con más delitos reciben más efectivos. Aquí, $y$ causa $x$ (causalidad inversa) y, además, factores no observados como la pobreza o la desigualdad pueden afectar simultáneamente a ambas variables ([[omision-de-variables]]). Una estrategia de variables instrumentales podría explotar cambios exógenos en la dotación policial —por ejemplo, alertas de seguridad no relacionadas con la delincuencia local— para aislar la variación exógena de $x$ y estimar un efecto causal no contaminado por la confusión de causas y consecuencias.

## Véase también

- [[endogeneidad]]
- [[causalidad]]
- [[validez-interna]]
- [[relacion-espurea]]
- [[omision-de-variables]]
- [[sesgo-de-seleccion]]
- [[correlacion]]
- [[regresion]]
- [[variable-independiente]]
- [[variable-dependiente]]
- [[variable-interviniente]]

## Fuentes

- King, G., Keohane, R. O. y Verba, S. (2000). *El diseño de la investigación social*. Madrid: Alianza.
- Lago, I. (2008). *La lógica de la explicación en las ciencias sociales* (págs. 75-111). Madrid: Alianza.
- Angrist, J. D. y Pischke, J.-S. (2009). *Mostly Harmless Econometrics*. Princeton University Press.
- Pearl, J. (2009). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
- Wooldridge, J. M. (2009). *Introductory Econometrics: A Modern Approach*. South-Western.
