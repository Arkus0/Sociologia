---
id: multicolinealidad
title: Multicolinealidad
note_type: concept
semester: 2026-S1
course: "Metodologia de las ciencias sociales"
related_concepts:
  - "[[regresion]]"
  - "[[correlacion]]"
  - "[[variable-independiente]]"
  - "[[variable-dependiente]]"
  - "[[covarianza]]"
  - "[[seleccion-de-variables]]"
  - "[[sobredeterminacion]]"
  - "[[endogeneidad]]"
tags:
  - metodología
  - estadística
  - regresión
  - diseño-de-investigación
  - inferencia
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\metodologia-de-las-ciencias-sociales.md
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\modulo-2.md
updated_at: "2025-07-13"
---

## Definición

La **multicolinealidad** es un problema estadístico que se presenta en los modelos de [[regresion]] múltiple cuando dos o más [[variable-independiente|variables independientes]] están fuertemente correlacionadas entre sí. En presencia de multicolinealidad, aunque las variables explicativas mantengan su poder predictivo conjunto sobre la [[variable-dependiente]], resulta imposible aislar con precisión el efecto individual de cada una de ellas. Formalmente, se dice que existe multicolinealidad cuando la matriz de datos $X'X$ es casi singular, es decir, cuando su determinante se aproxima a cero.

Se distinguen dos tipos fundamentales. La **multicolinealidad exacta** (o perfecta) se produce cuando una variable independiente es una combinación lineal exacta de otra u otras, lo que implica un coeficiente de [[correlacion]] igual a 1 y la imposibilidad matemática de calcular los estimadores por mínimos cuadrados ordinarios (MCO), puesto que $\det(X'X) = 0$. La **multicolinealidad aproximada** (o imperfecta), mucho más frecuente en la investigación empírica, se da cuando la correlación entre variables explicativas es alta —pero no perfecta—, de modo que $\det(X'X) \approx 0$. En este caso los estimadores MCO sí pueden calcularse, pero sus propiedades se deterioran significativamente.

## Origen y contexto histórico

El concepto de multicolinealidad surge dentro de la tradición econométrica de la primera mitad del siglo XX, vinculado al desarrollo de los modelos de regresión lineal múltiple. Ragnar Frisch, uno de los fundadores de la econometría, fue entre los primeros en identificar formalmente el problema hacia la década de 1930, al advertir que la estimación de parámetros se volvía inestable cuando las variables explicativas coexistían con patrones de variación similares. Posteriormente, la formalización del problema se consolidó en los manuales clásicos de econometría (Johnston, 1972; Gujarati, 1978) y se extendió a todas las ciencias sociales que emplean técnicas de regresión.

En el ámbito de la metodología de las ciencias sociales, la multicolinealidad se enmarca dentro de las amenazas al [[diseno-de-investigacion]] válido. King, Keohane y Verba (2000) la vinculan al problema más general de la **indeterminación**: la imposibilidad de establecer relaciones causales fiables cuando las condiciones del diseño no permiten aislar los efectos de cada variable.

## Desarrollo teórico

### Consecuencias de la multicolinealidad

Las consecuencias principales de la multicolinealidad aproximada son:

1. **Inflación de las varianzas** de los estimadores: al ser $(X'X)^{-1}$ muy grande, las varianzas de los coeficientes $\hat{\beta}_i$ se disparan, lo que reduce la precisión de las estimaciones.
2. **Inestabilidad de los coeficientes**: pequeños cambios en la muestra o en la especificación del modelo generan variaciones desproporcionadas en los valores estimados de los parámetros.
3. **Pérdida de significación estadística**: los errores estándar inflados producen intervalos de confianza más amplios y estadísticos $t$ más pequeños, de modo que variables que realmente influyen pueden aparecer como no significativas.
4. **Dificultad para la interpretación causal**: no se puede distinguir el efecto separado de cada variable independiente sobre la dependiente.

Es importante señalar que la multicolinealidad no afecta la capacidad global de predicción del modelo ni viola los supuestos de Gauss-Markov; los estimadores MCO siguen siendo insesgados. El problema reside en su **eficiencia**: la varianza de los estimadores es mayor de lo deseable.

### Detección

El instrumento más difundido para diagnosticar la multicolinealidad es el **factor de inflación de la varianza** (VIF, *variance inflation factor*):

$$VIF(\hat{\beta}_i) = \frac{1}{1 - R_{x_i}^2}$$

donde $R_{x_i}^2$ es el coeficiente de determinación de la regresión auxiliar de $x_i$ sobre las demás variables independientes. Un VIF superior a 10 se considera indicativo de multicolinealidad grave. Otros métodos de detección incluyen el análisis de los **autovalores** de la matriz $X'X$ y el cálculo del **número de condición**: valores de $IC > 30$ señalan multicolinealidad severa. También puede examinarse la **matriz de correlaciones** entre las variables exógenas: si su determinante se acerca a cero, existen indicios del problema.

### Soluciones

Entre las estrategias habituales para mitigar la multicolinealidad se cuentan:

- **Aumentar el tamaño de la muestra**: más observaciones pueden reducir la [[covarianza]] entre estimadores y mejorar la precisión.
- **Eliminar variables redundantes**: si dos variables miden esencialmente lo mismo, suprimir una de ellas reduce la colinealidad con una pérdida mínima de capacidad explicativa. Esto conecta con el problema general de la [[seleccion-de-variables]].
- **Análisis de componentes principales (PCA)**: transformar las variables correlacionadas en un conjunto de componentes ortogonales que retienen la mayor parte de la información original.
- **Regresión Ridge**: introducir un parámetro de penalización $\lambda$ que reduce la varianza de los estimadores a costa de un pequeño sesgo, ofreciendo un mejor equilibrio entre sesgo y varianza.
- **Centrar las variables**: restar la media a cada variable puede reducir la colinealidad en modelos con términos de interacción.

## Relación con otros conceptos

La multicolinealidad está estrechamente vinculada a la [[sobredeterminacion]]: ambas son manifestaciones del problema de la indeterminación. Mientras que la sobredeterminación se refiere a tener más variables que casos, la multicolinealidad se centra en la correlación entre las [[variable-independiente|variables independientes]] dentro de un modelo de [[regresion]]. Desde la perspectiva de King, Keohane y Verba, la multicolinealidad es "el mismo problema que la sobredeterminación, pero visto desde el punto de vista de la estadística multivariante".

El concepto se relaciona también con la [[endogeneidad]], pues ambos comprometen la validez de las inferencias causales, aunque por mecanismos distintos. Mientras la multicolinealidad dificulta la separación de efectos entre variables independientes, la endogeneidad cuestiona la dirección misma de la relación causal.

## Debates y críticas

Existe un debate relevante sobre la gravedad real de la multicolinealidad. Algunos autores sostienen que se trata de un "problema de datos" más que de un error de especificación: si el interés radica en la predicción global y no en los coeficientes individuales, la multicolinealidad puede ser irrelevante. Goldberger (1991) argumentó que la multicolinealidad no es un "pecado" del investigador sino una limitación inherente a los datos disponibles, comparable a un tamaño muestral insuficiente («micronumerosidad»).

Otros críticos señalan que la eliminación mecánica de variables para reducir el VIF puede introducir un **sesgo por omisión de variable relevante**, problema potencialmente más grave que la propia multicolinealidad. La decisión de excluir una variable debe sustentarse en argumentos teóricos, no meramente estadísticos.

## Vigencia contemporánea

En la investigación social actual, la multicolinealidad sigue siendo una preocupación central. La disponibilidad de conjuntos de datos masivos con decenas o cientos de variables —como encuestas de panel, datos administrativos o *big data*— incrementa la probabilidad de encontrar correlaciones altas entre predictores. Las técnicas de *machine learning* como la regularización (Lasso, Ridge, Elastic Net) ofrecen soluciones escalables que penalizan automáticamente la redundancia entre variables. Asimismo, el uso creciente de **modelos multinivel** y de **ecuaciones estructurales** permite abordar la multicolinealidad dentro de marcos más complejos que los de la regresión lineal clásica.

## Ejemplo empírico

Supongamos una investigación que pretende explicar el nivel de participación electoral (variable dependiente) a partir de tres variables independientes: nivel de ingresos, años de educación y estatus ocupacional. Estas tres variables suelen estar fuertemente correlacionadas entre sí (las personas con más educación tienden a tener empleos de mayor estatus y mayores ingresos). Al estimar el modelo de regresión múltiple, los VIF de cada variable podrían superar 8 o 10, indicando multicolinealidad grave. Los coeficientes individuales resultarían inestables y posiblemente no significativos, a pesar de que el modelo en su conjunto muestre un $R^2$ elevado. Una solución consistiría en construir un índice compuesto de nivel socioeconómico mediante PCA, en lugar de incluir las tres variables por separado.

## Véase también

- [[regresion]]
- [[correlacion]]
- [[variable-independiente]]
- [[covarianza]]
- [[sobredeterminacion]]
- [[seleccion-de-variables]]
- [[endogeneidad]]
- [[diseno-de-investigacion]]

## Fuentes

- King, G., Keohane, R. y Verba, S. (2000). *El diseño de la investigación social*. Madrid: Alianza.
- Sala, G., Borge, R. y Padró-Solanet, A. "Procedimientos y decisiones para determinar qué se observará". Módulo UOC, PID_00248675.
- Gujarati, D. (2003). *Econometría*. México: McGraw-Hill.
- Goldberger, A. S. (1991). *A Course in Econometrics*. Cambridge: Harvard University Press.
- Wikipedia contributors. "Multicolinealidad". *Wikipedia, la enciclopedia libre*.
