---
id: estadistica-multivariada
title: Estadística multivariada
note_type: concept
semester: 2026-S1
course: "Metodología de las ciencias sociales"
related_concepts:
  - regresion
  - correlacion
  - variable-de-control
  - estadistica-descriptiva
  - covarianza
  - relacion-espurea
  - estadistica-inferencial
  - variable-independiente
tags:
  - metodología
  - estadística
  - análisis-cuantitativo
  - multivariante
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\la-investigacion-cuantitativa.md
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\modulo-3.md
updated_at: '2025-07-13'
---

## Definición

La **estadística multivariada** (o multivariante) es la rama de la estadística que abarca la observación y el análisis simultáneos de dos o más variables. A diferencia de la [[estadistica-descriptiva|estadística univariada]], que describe la distribución de una sola variable mediante medidas de tendencia central y dispersión, la estadística multivariada examina las **relaciones, estructuras latentes y patrones de asociación** entre múltiples variables, permitiendo al investigador social abordar la complejidad inherente a los fenómenos colectivos. Dentro del análisis cuantitativo, se distingue de la estadística puramente descriptiva porque incorpora herramientas de la [[estadistica-inferencial]] para extrapolar los hallazgos de la muestra a la población de referencia.

Entre sus técnicas principales se encuentran la [[regresion|regresión]] múltiple, el análisis factorial, el análisis de componentes principales (ACP), el análisis de correspondencias múltiples (ACM), el análisis de conglomerados (*cluster analysis*) y los modelos de ecuaciones estructurales (SEM). Todas comparten un objetivo común: reducir la complejidad de un sistema de variables para extraer información sustantiva sobre relaciones causales, tipologías o dimensiones subyacentes.

## Origen y contexto histórico

Los antecedentes de la estadística multivariada se remontan a los trabajos de Francis Galton y Karl Pearson a finales del siglo XIX, quienes formalizaron los conceptos de [[correlacion|correlación]] y [[regresion|regresión]]. Pearson desarrolló el coeficiente de correlación producto-momento y sentó las bases del análisis de componentes principales hacia 1901. En las décadas siguientes, Ronald Fisher contribuyó con el análisis discriminante y el análisis de varianza multivariante (MANOVA), herramientas que ampliaron la capacidad inferencial al caso de múltiples variables dependientes.

El libro de T. W. Anderson, *An Introduction to Multivariate Analysis* (1958), formó a una generación de estadísticos teóricos y aplicados, consolidando el campo como disciplina autónoma. En las ciencias sociales, un hito decisivo fue el *paradigma de la elaboración* de Paul Lazarsfeld (Columbia, años 1940-1950), que sistematizó la introducción de [[variable-de-control|variables de control]] para distinguir relaciones genuinas de [[relacion-espurea|relaciones espureas]]. Lazarsfeld demostró que la asociación bivariada entre dos variables puede desaparecer, atenuarse o invertirse al controlar una tercera, sentando así la lógica del análisis multivariado en la sociología empírica.

## Desarrollo teórico

La lógica multivariada parte de un principio fundamental: los fenómenos sociales son **multicausales**. Cualquier variable dependiente $Y$ resulta de la acción conjunta de múltiples factores $X_1, X_2, \ldots, X_k$, y la omisión de alguno de ellos puede sesgar las estimaciones (sesgo por variable omitida). El modelo general de regresión múltiple formaliza esta idea:

$$Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \cdots + \beta_k X_k + \varepsilon$$

donde cada coeficiente $\beta_j$ estima el efecto parcial de $X_j$ manteniendo constantes las demás variables. La [[covarianza|matriz de covarianzas]] $\Sigma$ constituye el insumo central de la mayoría de las técnicas multivariantes: sus entradas resumen las relaciones lineales entre cada par de variables, y su estructura determina las soluciones del ACP, del análisis factorial y de los SEM.

Las técnicas multivariadas se clasifican habitualmente en tres familias:

1. **Métodos de dependencia**: analizan la influencia de un conjunto de variables independientes sobre una o varias dependientes. Incluyen la regresión múltiple, la regresión logística, el análisis discriminante y el MANOVA.
2. **Métodos de interdependencia**: buscan estructuras latentes sin distinguir entre variables dependientes e independientes. Incluyen el ACP, el análisis factorial exploratorio, el ACM y el análisis de conglomerados.
3. **Métodos estructurales**: los modelos de ecuaciones estructurales (SEM) combinan un componente de medida (que relaciona indicadores observables con constructos latentes) y un componente estructural (que especifica relaciones causales entre constructos).

## Relación con otros conceptos

La estadística multivariada se sitúa en el centro de una red conceptual amplia dentro de la metodología cuantitativa:

- **[[correlacion|Correlación]]**: mide la fuerza y dirección de la asociación lineal bivariada; la correlación parcial extiende esta idea al controlar terceras variables.
- **[[regresion|Regresión]]**: herramienta multivariada por excelencia; permite estimar efectos causales controlando confusores.
- **[[variable-de-control]]**: la lógica lazarsfeldiana de «elaboración» —especificación, explicación, interpretación— depende de la introducción de variables de control en modelos multivariados.
- **[[relacion-espurea]]**: el análisis multivariado permite detectar asociaciones espureas al incorporar la variable antecedente que genera la correlación aparente.
- **[[covarianza]]**: la matriz de covarianzas es la estructura matemática sobre la que operan las principales técnicas multivariantes.
- **[[estadistica-descriptiva]]**: precede necesariamente al análisis multivariado; toda inferencia parte de una descripción previa de los datos.

## Debates y críticas

Uno de los principales debates gira en torno a la **causalidad**. Las técnicas multivariadas permiten controlar variables y estimar efectos parciales, pero la asociación estadística —por sofisticada que sea— no garantiza causalidad. Judea Pearl ha argumentado que los modelos causales estructurales exigen supuestos explícitos que van más allá del ajuste estadístico. En la tradición sociológica, la discusión se remonta a la distinción de Lazarsfeld entre correlación y explicación.

Una segunda crítica señala los **supuestos exigentes** de muchas técnicas: linealidad, normalidad multivariante, homocedasticidad y ausencia de multicolinealidad perfecta. La violación de estos supuestos puede producir estimaciones ineficientes o sesgadas. En la práctica, los investigadores recurren a diagnósticos (VIF, pruebas de normalidad, análisis de residuos) y a métodos robustos (errores estándar robustos, bootstrap) para mitigar estos problemas.

Finalmente, existe un riesgo de **empirismo ciego**: la aplicación mecánica de técnicas multivariadas sin fundamentación teórica puede conducir a hallazgos espurios o carentes de significación sustantiva. La sociología cuantitativa insiste en que los modelos deben estar guiados por hipótesis teóricas, no solo por la disponibilidad de datos.

## Vigencia contemporánea

La estadística multivariada sigue siendo el pilar del análisis cuantitativo en ciencias sociales. Los informes de organismos internacionales (CEPAL, Eurostat, Banco Mundial) utilizan regresiones múltiples, modelos multinivel y técnicas factoriales para analizar desigualdad, pobreza y cohesión social. En la sociología académica, los SEM se han convertido en herramienta estándar para contrastar teorías complejas con datos de encuesta. Más recientemente, las técnicas de *machine learning* (bosques aleatorios, redes neuronales) extienden la lógica multivariada a problemas de clasificación y predicción con grandes volúmenes de datos, aunque su uso en sociología plantea interrogantes sobre interpretabilidad y confirmación teórica.

## Ejemplo empírico

Un estudio desea determinar si el **nivel educativo** ($X_1$) influye en el **ingreso mensual** ($Y$) controlando la **experiencia laboral** ($X_2$) y el **género** ($X_3$). Un modelo de regresión múltiple permite estimar el efecto parcial de cada variable. Si al introducir la variable de control «experiencia laboral» el coeficiente del nivel educativo se reduce significativamente, el investigador infiere que parte de la asociación observada se debía al efecto mediador de la experiencia. Si, en cambio, el coeficiente se mantiene estable, la relación educación-ingreso es robusta al control. Este razonamiento reproduce exactamente la lógica de elaboración de Lazarsfeld aplicada en un marco multivariado.

## Véase también

- [[estadistica-descriptiva]]
- [[estadistica-inferencial]]
- [[regresion]]
- [[correlacion]]
- [[covarianza]]
- [[variable-de-control]]
- [[relacion-espurea]]
- [[variable-independiente]]
- [[tabla-de-contingencia]]

## Fuentes

- Anderson, T. W. (1958). *An Introduction to Multivariate Analysis*. Nueva York: Wiley.
- Lazarsfeld, P. F. (1955). Interpretation of statistical relations as a research operation. En P. F. Lazarsfeld y M. Rosenberg (eds.), *The Language of Social Research*. Glencoe: Free Press.
- King, G., Keohane, R. O. y Verba, S. (2000). *El diseño de la investigación social*. Madrid: Alianza.
- Borge, R. y Padró-Solanet, A. (s.f.). *La investigación cuantitativa: encuesta, experimento y análisis estadístico*. Módulo UOC — Metodología de las ciencias sociales.
- Pearl, J. (2009). *Causality: Models, Reasoning, and Inference*. 2.ª ed. Cambridge University Press.
