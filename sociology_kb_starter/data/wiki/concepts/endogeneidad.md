---
id: endogeneidad
title: Endogeneidad
note_type: concept
semester: 2026-S1
course: "Metodologia de las ciencias sociales"
related_concepts:
  - relacion-espurea
  - variable-de-control
  - omision-de-variables
  - regresion
  - causalidad
  - validez-interna
  - variable-independiente
  - variable-dependiente
tags:
  - metodologia
  - causalidad
  - econometria
  - sesgo
  - inferencia
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\modulo-2.md
updated_at: '2025-07-13'
---

## Definición

La **endogeneidad** designa la situación en la que una [[variable-independiente]] incluida en un modelo explicativo está correlacionada con el término de error de la ecuación estimada. En términos sustantivos, ello significa que la variable que se supone *causa* del fenómeno estudiado mantiene una relación espuria o inversa con la [[variable-dependiente]], de modo que las estimaciones obtenidas mediante mínimos cuadrados ordinarios (MCO) resultan sesgadas e inconsistentes. Cuando existe endogeneidad, el investigador no puede atribuir de forma fiable un efecto causal a la variable explicativa, lo que compromete la [[validez-interna]] de toda la investigación.

En la formulación canónica de un modelo de [[regresion]] lineal $y_i = \alpha + \beta x_i + \varepsilon_i$, la exogeneidad exige que $E(\varepsilon_i \mid x_i) = 0$. Si esta condición se viola —es decir, si $\text{Cov}(x_i, \varepsilon_i) \neq 0$— el estimador $\hat{\beta}$ deja de ser insesgado y la inferencia causal pierde sustento.

## Origen y contexto histórico

El concepto proviene de los modelos de ecuaciones simultáneas desarrollados en econometría durante las décadas de 1940 y 1950, cuando la Cowles Commission (Haavelmo, Koopmans, Hood) distinguió entre variables endógenas —cuyos valores se determinan dentro del sistema— y variables exógenas —predeterminadas fuera de él—. La noción cobró centralidad en las ciencias sociales a partir de los trabajos de Gary King, Robert Keohane y Sidney Verba (1994), quienes trasladaron estas preocupaciones al ámbito cualitativo-comparativo, y de Ignacio Lago (2008), que sistematizó ejemplos accesibles para la ciencia política hispanohablante.

## Desarrollo teórico

La literatura identifica tres fuentes principales de endogeneidad:

1. **Omisión de variables relevantes.** Cuando una variable $z_i$ afecta simultáneamente a $x_i$ y a $y_i$ pero no se incluye en el modelo, su efecto queda absorbido por el término de error, generando correlación entre $x_i$ y $\varepsilon_i$. Este es el mecanismo más frecuente y está vinculado directamente al problema de la [[omision-de-variables]] y la [[relacion-espurea]].

2. **Simultaneidad (causalidad recíproca).** Si $x$ causa $y$ y a la vez $y$ causa $x$, estimar cualquiera de las dos ecuaciones estructurales por MCO produce sesgo. El ejemplo clásico es la relación entre precio y cantidad en un mercado: la demanda depende del precio, pero el precio se ajusta a la demanda.

3. **Error de medición.** Si en lugar de observar $x_i^*$ se observa $x_i = x_i^* + \nu_i$, el ruido $\nu_i$ se incorpora al error compuesto $u_i = \varepsilon_i - \beta\nu_i$, que queda correlacionado con $x_i$. El sesgo resultante atenúa el coeficiente estimado hacia cero.

En los tres casos, la consecuencia es la misma: el estimador MCO ya no aproxima el verdadero efecto causal $\beta$.

## Relación con otros conceptos

La endogeneidad ocupa un lugar central en la red de problemas del [[diseno-de-investigacion]]. Está estrechamente ligada a la [[relacion-espurea]], pues una variable omitida puede generar una asociación estadística allí donde no existe nexo causal. El recurso habitual para mitigar la omisión de variables es la introducción de una [[variable-de-control]], aunque esta estrategia solo funciona si la variable confusora es observable y se especifica correctamente. Cuando la fuente es la simultaneidad, la endogeneidad compromete la [[causalidad]] atribuida al modelo, pues la dirección del efecto resulta indistinguible sin información adicional. Todo ello incide en la [[validez-interna]]: un diseño afectado por endogeneidad no permite establecer con rigor que $x$ causa $y$.

## Debates y críticas

La solución más difundida es la **estimación por variables instrumentales (VI)**. Un instrumento $z$ debe cumplir dos condiciones: estar correlacionado con la variable endógena (*relevancia*) y no estar correlacionado con el término de error (*restricción de exclusión*). El método de mínimos cuadrados en dos etapas (MC2E) utiliza $z$ para aislar la variación exógena de $x$ y obtener estimadores consistentes, aunque a costa de mayor varianza.

James Heckman (1979) propuso el **modelo de corrección de selección** para un caso particular de endogeneidad derivado del [[sesgo-de-seleccion]]: cuando la muestra observada no es aleatoria, el término de error condicional deja de tener media cero. Su procedimiento en dos etapas —estimación de la probabilidad de selección mediante un probit y corrección del sesgo en la ecuación principal— le valió el Premio Nobel de Economía en 2000.

Desde la perspectiva contrafactual, Joshua Angrist y Jörn-Steffen Pischke (*Mostly Harmless Econometrics*, 2009) sistematizaron un conjunto de estrategias de identificación —experimentos naturales, regresión discontinua, diferencia en diferencias, VI— orientadas a resolver la endogeneidad sin recurrir a supuestos estructurales fuertes. Su enfoque, a veces denominado «revolución de la credibilidad», ha ejercido una enorme influencia en la ciencia política y la sociología cuantitativa.

Desde un ángulo epistemológico distinto, Judea Pearl propuso los **grafos acíclicos dirigidos (DAGs)** como herramienta para formalizar los supuestos causales y detectar fuentes de endogeneidad de forma visual. Los DAGs permiten identificar qué variables deben controlarse y cuáles no, evitando el problema del «mal control» que puede introducir sesgo adicional en lugar de eliminarlo.

No obstante, los críticos señalan que encontrar instrumentos válidos es extremadamente difícil en la práctica. La restricción de exclusión es inverificable empíricamente, y un instrumento débil puede amplificar el sesgo en lugar de corregirlo. En las ciencias sociales, donde la experimentación es a menudo inviable, la endogeneidad sigue siendo un desafío persistente.

## Vigencia contemporánea

El debate sobre la endogeneidad estructura buena parte de la agenda metodológica actual. La difusión de los diseños cuasiexperimentales, los experimentos de campo y las técnicas de *machine learning* causal (bosques causales, *double machine learning*) responde en gran medida a la necesidad de obtener estimaciones creíbles cuando la asignación al tratamiento no es aleatoria. En sociología, la discusión se extiende al análisis cualitativo: la selección de casos por la variable dependiente —criticada por King, Keohane y Verba— puede entenderse como un caso análogo de endogeneidad en el plano del diseño comparativo.

## Ejemplo empírico

Supóngase que un investigador desea estimar el efecto de la participación en programas de formación laboral ($x$) sobre la probabilidad de empleo ($y$). Si la inscripción al programa es voluntaria, quienes se inscriben pueden ser sistemáticamente más motivados o tener mayor capital social, características que también favorecen el empleo pero que no se observan directamente. La [[endogeneidad]] aparece porque $x$ (participación) está correlacionada con factores inobservados incluidos en $\varepsilon$. Una estrategia de variables instrumentales podría utilizar la *distancia al centro de formación* como instrumento: la cercanía predice la participación, pero, bajo supuestos razonables, no afecta al empleo por otra vía que no sea a través del programa. De este modo se aísla la variación exógena de $x$ y se obtiene una estimación menos sesgada del efecto causal.

## Véase también

- [[relacion-espurea]]
- [[variable-de-control]]
- [[omision-de-variables]]
- [[regresion]]
- [[causalidad]]
- [[validez-interna]]
- [[variable-independiente]]
- [[variable-dependiente]]
- [[sesgo-de-seleccion]]
- [[diseno-de-investigacion]]
- [[endogeneidad-confusion-de-causas-y-de-consecuencias]]

## Fuentes

- King, G., Keohane, R. O. y Verba, S. (2000). *El diseño de la investigación social*. Madrid: Alianza.
- Lago, I. (2008). *La lógica de la explicación en las ciencias sociales* (págs. 75-111). Madrid: Alianza.
- Anduiza, E., Crespo, I. y Méndez, M. (1999). *Metodología de la Ciencia Política*. Madrid: CIS.
- Angrist, J. D. y Pischke, J.-S. (2009). *Mostly Harmless Econometrics*. Princeton University Press.
- Heckman, J. J. (1979). «Sample Selection Bias as a Specification Error». *Econometrica*, 47(1), 153-161.
- Pearl, J. (2009). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.
- Wooldridge, J. M. (2009). *Introductory Econometrics: A Modern Approach*. South-Western.
- [[procedimientos-y-decisiones-para-determinar-que-se-observara]] (Metodologia de las ciencias sociales)
