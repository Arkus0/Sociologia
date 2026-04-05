---
id: varianza
title: Varianza
note_type: concept
semester: 2026-S1
course: "Metodologia de las ciencias sociales"
related_concepts:
  - desviacion-estandar
  - media-aritmetica
  - estadistica-descriptiva
  - regresion
  - correlacion
  - covarianza
  - error-muestral
tags:
  - estadistica
  - dispersion
  - metodologia-cuantitativa
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\modulo-3.md
updated_at: "2025-07-13"
---

## Definición

La **varianza** (σ²) es una medida de dispersión estadística que cuantifica la dispersión de un conjunto de datos respecto a su [[media-aritmetica|media aritmética]]. Formalmente, se define como la esperanza matemática del cuadrado de las desviaciones de cada observación respecto al valor medio:

$$\text{Var}(X) = E\left[(X - \mu)^2\right] = \frac{1}{N}\sum_{i=1}^{N}(x_i - \mu)^2$$

donde $\mu$ es la media poblacional y $N$ el tamaño de la población. Expresada de forma equivalente, $\text{Var}(X) = E[X^2] - (E[X])^2$, es decir, la media de los cuadrados menos el cuadrado de la media.

La varianza siempre es mayor o igual que cero y su unidad de medida corresponde al cuadrado de la unidad de la variable original (si la variable mide ingresos en pesos, la varianza se expresa en pesos²). Esta dificultad interpretativa motivó el uso paralelo de la [[desviacion-estandar|desviación estándar]], definida como la raíz cuadrada positiva de la varianza ($\sigma = \sqrt{\sigma^2}$), que recupera la unidad original de los datos.

## Origen y contexto histórico

El término **varianza** fue acuñado por **Ronald A. Fisher** en su artículo de 1918 *The Correlation Between Relatives on the Supposition of Mendelian Inheritance*, publicado en las *Transactions of the Royal Society of Edinburgh*. Fisher argumentó que, al analizar causas independientes de variabilidad, resultaba algebraicamente conveniente trabajar con el cuadrado de la desviación típica en lugar de con la desviación misma. En sus propias palabras: «denominaremos a esta cantidad varianza».

Antes de la formalización de Fisher, la tradición biométrica británica —encabezada por **Francis Galton** y **Karl Pearson**— ya utilizaba la desviación típica como medida de dispersión, pero fue Fisher quien consolidó la varianza como unidad fundamental del análisis estadístico. Su posterior desarrollo del **análisis de varianza** (ANOVA) en la década de 1920 convirtió al concepto en piedra angular de la estadística experimental y, por extensión, de la investigación social cuantitativa.

## Desarrollo teórico

### Varianza poblacional y varianza muestral

En la práctica de las ciencias sociales rara vez se accede a la totalidad de la población, por lo que es necesario estimar la varianza a partir de una muestra. La **varianza muestral** emplea el divisor $n - 1$ (corrección de Bessel) en lugar de $n$ para obtener un estimador insesgado de la varianza poblacional:

$$s^2 = \frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2$$

Esta corrección compensa el hecho de que la media muestral $\bar{x}$ ya consume un grado de libertad.

### Análisis de varianza (ANOVA)

Fisher desarrolló el ANOVA como técnica para descomponer la variabilidad total de una variable en componentes atribuibles a factores específicos. En su forma más simple (ANOVA de un factor), la varianza total se particiona en **varianza intergrupal** (entre grupos) y **varianza intragrupal** (dentro de los grupos). Si la varianza entre grupos es significativamente mayor que la varianza dentro de los grupos, se concluye que el factor analizado tiene un efecto estadísticamente significativo. Esta lógica es esencial en diseños experimentales y cuasiexperimentales en sociología, donde se comparan grupos de tratamiento y de control.

### Varianza explicada y R²

En modelos de [[regresion|regresión]], el **coeficiente de determinación** ($R^2$) expresa la proporción de la varianza de la [[variable-dependiente]] que es explicada por las variables independientes. Un $R^2 = 0{,}65$ indica que el modelo explica el 65 % de la variabilidad observada. La fracción restante corresponde a la varianza no explicada, atribuible a variables omitidas o al error aleatorio. Este indicador permite evaluar el poder explicativo de un modelo y es ampliamente reportado en la investigación social cuantitativa.

## Relación con otros conceptos

La varianza se articula con una constelación de conceptos de la [[estadistica-descriptiva|estadística descriptiva]] e inferencial:

- La [[desviacion-estandar]] es su raíz cuadrada y constituye la medida de dispersión más utilizada en la comunicación de resultados, al conservar la misma unidad que la variable.
- La [[media-aritmetica]] es el punto de referencia respecto al cual se calculan las desviaciones; sin media, la varianza carece de sentido.
- La [[covarianza]] generaliza la varianza al caso bivariado: mide la variación conjunta de dos variables. De hecho, la varianza puede entenderse como la covarianza de una variable consigo misma: $\text{Var}(X) = \text{Cov}(X, X)$.
- La [[correlacion|correlación]] estandariza la covarianza dividiéndola por el producto de las desviaciones estándar, produciendo un coeficiente adimensional entre –1 y +1.
- La [[regresion]] utiliza la descomposición de la varianza para estimar efectos causales y generar predicciones.
- El [[error-muestral]] depende directamente de la varianza poblacional: a mayor varianza, mayor error estándar de la media muestral ($SE = \sigma / \sqrt{n}$).

## Debates y críticas

Un primer debate concierne la **sensibilidad a valores atípicos**: al elevar las desviaciones al cuadrado, la varianza otorga un peso desproporcionado a las observaciones extremas. En distribuciones con colas pesadas —frecuentes en datos de ingresos o patrimonio— otras medidas de dispersión robustas (como el rango intercuartílico o la desviación absoluta mediana) pueden ser preferibles.

Una segunda crítica apunta a la **interpretabilidad** directa: al expresarse en unidades al cuadrado, la varianza resulta poco intuitiva para audiencias no especializadas, razón por la cual la desviación estándar suele preferirse en la presentación de resultados.

Desde la perspectiva de la modelización social, la inclusión de variables irrelevantes en un modelo de regresión aumenta la varianza de los estimadores (ineficiencia), mientras que la omisión de variables relevantes introduce sesgo. Este dilema sesgo-varianza (*bias-variance tradeoff*) constituye un problema central en la especificación de modelos cuantitativos.

## Vigencia contemporánea

La varianza mantiene una presencia ubicua en la investigación social contemporánea. Los modelos multinivel —empleados para analizar datos jerárquicos como alumnos anidados en escuelas— descomponen la varianza en niveles (individual, grupal, institucional), permitiendo identificar en qué estrato se concentra la mayor variabilidad. El análisis de componentes principales (ACP) busca ejes que capturen la máxima varianza de un conjunto multidimensional de variables. En la evaluación de políticas públicas mediante ensayos controlados aleatorios, la varianza del estimador del efecto causal determina la precisión de las conclusiones; el muestreo estratificado y el emparejamiento buscan precisamente reducir esa varianza.

## Ejemplo empírico

Una investigación sobre desigualdad educativa mide la puntuación en una prueba estandarizada de 200 estudiantes de cuatro escuelas. Las puntuaciones tienen una media global de 72 puntos. La varianza total calculada es $s^2 = 144$, de modo que la desviación estándar es $s = 12$ puntos. Un ANOVA de un factor revela que la varianza intergrupal (entre escuelas) representa el 40 % de la varianza total, mientras que el 60 % restante es varianza intragrupal (diferencias individuales dentro de cada escuela). Esto indica que el tipo de escuela explica una proporción sustancial de las diferencias de rendimiento, lo que orienta la discusión hacia factores institucionales —recursos, formación docente, contexto socioeconómico del alumnado— como determinantes de la desigualdad.

## Véase también

- [[desviacion-estandar]]
- [[media-aritmetica]]
- [[estadistica-descriptiva]]
- [[regresion]]
- [[correlacion]]
- [[covarianza]]
- [[error-muestral]]
- [[chi-cuadrado]]
- [[variable-dependiente]]

## Fuentes

- Fisher, R. A. (1918). "The Correlation Between Relatives on the Supposition of Mendelian Inheritance". *Transactions of the Royal Society of Edinburgh*, 52(2), 399–433.
- Borge Bravo, R. y Padró-Solanet, A. (2026). *Metodología de las ciencias sociales*, Módulo 3: «Técnicas cuantitativas y cualitativas». UOC.
- Agresti, A. y Finlay, B. (2009). *Statistical Methods for the Social Sciences* (4.ª ed.). Pearson.
- "Varianza". *Wikipedia en español*. Consultado el 5 de abril de 2026.
