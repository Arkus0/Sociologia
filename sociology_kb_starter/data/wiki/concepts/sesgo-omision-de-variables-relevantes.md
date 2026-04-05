---
id: sesgo-omision-de-variables-relevantes
title: "Sesgo: omisión de variables relevantes"
note_type: concept
semester: 2026-S1
course: "Metodología de las ciencias sociales"
related_concepts:
  - omision-de-variables
  - regresion
  - variable-de-control
  - variable-interviniente
  - relacion-espurea
  - endogeneidad
  - sesgo-de-seleccion
  - validez-interna
  - causalidad
  - ineficiencia-inclusion-de-variables-irrelevantes
tags:
  - metodologia
  - sesgo
  - regresion
  - inferencia-causal
  - omision-de-variables
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\metodologia-de-las-ciencias-sociales.md
updated_at: "2026-04-05"
---

## Definición

El **sesgo por omisión de variables relevantes** (*omitted variable bias*, OVB) es la distorsión que se introduce en las estimaciones de un modelo de [[regresion]] cuando se excluye una variable que: (a) es determinante de la [[variable-dependiente]] y (b) está correlacionada con alguna de las variables explicativas incluidas en el modelo. Al omitirla, su efecto queda absorbido por el coeficiente de la variable incluida, de manera que la estimación resulta **sesgada e inconsistente**. Este problema constituye una de las amenazas más frecuentes a la [[validez-interna]] de los estudios observacionales y es tratado extensamente dentro del marco más amplio de la [[omision-de-variables]].

Formalmente, supóngase que la relación verdadera es $y_i = \alpha + \beta x_i + \gamma z_i + u_i$, donde $z$ es la variable omitida. Si $z$ se excluye y se estima $y_i = \alpha' + \beta' x_i + e_i$, el estimador de mínimos cuadrados ordinarios arroja $E[\hat{\beta}'] = \beta + \gamma \cdot \delta_{zx}$, siendo $\delta_{zx}$ el coeficiente de regresión auxiliar de $z$ sobre $x$. El sesgo es $\gamma \delta_{zx}$; solo se anula cuando $\gamma = 0$ (la variable omitida no afecta a $y$) o cuando $\delta_{zx} = 0$ (la variable omitida no correlaciona con $x$).

## Origen y contexto histórico

La preocupación por la especificación incorrecta de modelos se remonta a los debates econométricos de mediados del siglo XX. Ya Frisch (1934) advirtió que la omisión de variables confusoras invalidaba las estimaciones de parámetros estructurales. Posteriormente, Theil (1957) formalizó la expresión algebraica del sesgo en modelos de regresión lineal. En ciencia política y sociología, King, Keohane y Verba (2000) trasladaron el problema al diseño de investigación cualitativo-cuantitativo, señalando que la omisión de variables relevantes es análoga a la falta de control experimental. Ignacio Lago (2008) sistematizó esta discusión para la ciencia política hispanohablante, situando el sesgo de omisión junto a la [[endogeneidad-confusion-de-causas-y-de-consecuencias|endogeneidad]] y el [[sesgo-de-seleccion]] como los tres grandes obstáculos a la inferencia causal válida.

## Desarrollo teórico

Para que exista sesgo por omisión de variables deben cumplirse simultáneamente dos condiciones:

1. **Relevancia.** La variable omitida $z$ tiene un efecto no nulo sobre la variable dependiente ($\gamma \neq 0$); es decir, es una [[variable-interviniente]] o confusora genuina.
2. **Correlación con el regresor.** Existe asociación entre $z$ y alguna de las variables explicativas incluidas ($\text{Cov}(z, x) \neq 0$).

Cuando ambas condiciones se satisfacen, el coeficiente estimado de $x$ captura no solo el efecto directo de $x$ sobre $y$, sino también parte del efecto indirecto que transita a través de $z$. La dirección del sesgo depende del signo de $\gamma \delta_{zx}$: si la correlación entre $z$ y $x$ va en el mismo sentido que el efecto de $z$ sobre $y$, el coeficiente de $x$ estará sobreestimado; en caso contrario, subestimado.

El problema viola el supuesto de exogeneidad estricta del modelo clásico de regresión lineal — $E(u_i \mid x_i) = 0$ —, pues la variable omitida pasa a formar parte del término de error, que deja de ser independiente de los regresores. Con ello, el estimador de mínimos cuadrados ordinarios pierde no solo insesgamiento sino también consistencia.

## Relación con otros conceptos

El sesgo de omisión se sitúa en un campo conceptual densamente conectado. Es una causa directa de [[relacion-espurea]]: cuando una [[variable-de-control]] relevante se excluye, la asociación observada entre $x$ e $y$ refleja en parte la influencia de la variable omitida y no un nexo causal genuino. Guarda estrecha relación con la [[endogeneidad]], puesto que la omisión de $z$ genera correlación entre el regresor y el error, condición definitoria de la endogeneidad en sentido econométrico. Se contrapone simétricamente a la [[ineficiencia-inclusion-de-variables-irrelevantes]]: mientras la omisión sesga, la inclusión de variables irrelevantes no introduce sesgo pero sí aumenta la varianza de los estimadores. Finalmente, conecta con la [[causalidad]], pues toda pretensión de interpretación causal de un coeficiente de [[regresion]] exige haber controlado por las variables confusoras relevantes.

## Debates y críticas

La solución más directa al sesgo de omisión consiste en incluir la variable omitida como [[variable-de-control]], pero esto requiere haberla identificado y medido — condición que rara vez se satisface plenamente en las ciencias sociales —. Las estrategias alternativas incluyen la estimación por **variables instrumentales**, los diseños de **diferencias en diferencias** y la explotación de **experimentos naturales**, todas ellas orientadas a recuperar variación exógena de $x$ no contaminada por $z$. Angrist y Pischke (2009) sistematizaron estas herramientas bajo el paradigma de la *credibility revolution*.

Desde la perspectiva de los grafos causales, Pearl (2009) argumenta que la decisión de incluir o excluir una variable debe derivarse de la estructura causal representada en un DAG (*directed acyclic graph*), y no de criterios puramente estadísticos como la significatividad. Esta posición ha influido crecientemente en la sociología cuantitativa, donde se reconoce que la omisión de variables no es solo un problema técnico, sino que refleja las limitaciones del conocimiento teórico del investigador.

## Vigencia contemporánea

El sesgo de omisión sigue siendo central en la agenda metodológica de las ciencias sociales. La expansión de datos administrativos masivos y técnicas de *machine learning* causal (como *double machine learning* o *causal forests*) busca reducir la dependencia de la correcta especificación del modelo. Sin embargo, ninguna técnica empírica sustituye la necesidad de una teoría causal bien formulada que identifique las variables relevantes. En la enseñanza metodológica, el sesgo de omisión se presenta —junto con la [[endogeneidad-confusion-de-causas-y-de-consecuencias|endogeneidad]] y la [[multicolinealidad]]— como uno de los problemas fundamentales que todo investigador social debe anticipar en la fase de diseño.

## Ejemplo empírico

Considérese un estudio que estima el efecto del gasto educativo por alumno ($x$) sobre el rendimiento académico ($y$) en distintos municipios. Si el modelo no incluye el nivel socioeconómico de las familias ($z$) como [[variable-de-control]], el coeficiente de $x$ estará sesgado: los municipios con mayor gasto tienden a tener familias más acomodadas, y el nivel socioeconómico afecta directamente al rendimiento. Parte del efecto atribuido al gasto educativo corresponde en realidad al entorno familiar. Al omitir $z$, $\hat{\beta}$ sobreestima el verdadero efecto causal del gasto, produciendo una [[relacion-espurea]] parcial. Incluir indicadores de nivel socioeconómico —o emplear una estrategia de variables instrumentales que explote variaciones exógenas en la financiación— permitiría aislar el efecto genuino del gasto sobre el aprendizaje.

## Véase también

- [[omision-de-variables]]
- [[regresion]]
- [[variable-de-control]]
- [[variable-interviniente]]
- [[relacion-espurea]]
- [[endogeneidad]]
- [[sesgo-de-seleccion]]
- [[validez-interna]]
- [[causalidad]]
- [[ineficiencia-inclusion-de-variables-irrelevantes]]

## Fuentes

- King, G., Keohane, R. O. y Verba, S. (2000). *El diseño de la investigación social*. Madrid: Alianza.
- Lago, I. (2008). *La lógica de la explicación en las ciencias sociales* (págs. 75-111). Madrid: Alianza.
- Angrist, J. D. y Pischke, J.-S. (2009). *Mostly Harmless Econometrics*. Princeton University Press.
- Pearl, J. (2009). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
- Wooldridge, J. M. (2009). *Introductory Econometrics: A Modern Approach*. South-Western.
- Clarke, K. A. (2005). "The Phantom Menace: Omitted Variable Bias in Econometric Research". *Conflict Management and Peace Science*, 22(4), 341-352.
