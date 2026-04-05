---
id: covarianza
title: Covarianza
note_type: concept
semester: 2026-S1
course: "Metodologia de las ciencias sociales"
related_concepts:
  - correlacion
  - varianza
  - regresion
  - variable-dependiente
  - variable-independiente
  - estadistica-descriptiva
  - coeficiente-de-pearson
  - tabla-de-contingencia
tags:
  - estadística
  - análisis-cuantitativo
  - asociación
  - variables
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\el-proceso-de-investigacion-en-las-ciencias-sociales.md
updated_at: '2025-07-13'
---

## Definición

La **covarianza** es una medida estadística que indica el grado de variación conjunta de dos [[variable-dependiente|variables]] respecto a sus medias. Formalmente, dadas dos variables aleatorias $X$ e $Y$, la covarianza se define como:

$$\text{Cov}(X, Y) = E\bigl[(X - E[X])(Y - E[Y])\bigr] = E[XY] - E[X]\,E[Y]$$

En su versión muestral —la que se emplea habitualmente en la investigación social empírica— el estimador insesgado es:

$$S_{xy} = \frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})$$

El signo de la covarianza revela la dirección de la asociación lineal: una covarianza **positiva** indica que valores altos de una variable tienden a acompañar valores altos de la otra; una covarianza **negativa** señala una relación inversa; y una covarianza **igual a cero** sugiere la ausencia de relación lineal, aunque no implica necesariamente independencia estadística.

## Origen y contexto histórico

La noción de covarianza se desarrolló en el marco de la estadística matemática de finales del siglo XIX y principios del XX, ligada a los trabajos de Karl Pearson y Francis Galton sobre correlación y regresión. Pearson formalizó la medida al construir su célebre coeficiente de [[correlacion|correlación]], que normaliza la covarianza dividiéndola entre el producto de las desviaciones típicas de ambas variables. A lo largo del siglo XX, la covarianza se incorporó como herramienta fundamental de las ciencias sociales cuantitativas, en particular dentro del análisis multivariante, el análisis factorial y los modelos de ecuaciones estructurales.

## Desarrollo teórico

### Covarianza y varianza

La [[varianza]] constituye un caso particular de la covarianza cuando ambas variables son idénticas: $\text{Cov}(X, X) = \text{Var}(X)$. Esta relación subraya que la covarianza generaliza la idea de dispersión al espacio bivariado.

### Del signo a la magnitud: el coeficiente de Pearson

Dado que la magnitud de la covarianza depende de las unidades de medida de las variables, su interpretación directa resulta limitada. Para obtener una medida adimensional y comparable, se estandariza dividiéndola por las desviaciones típicas:

$$r_{xy} = \frac{S_{xy}}{S_x \, S_y}$$

El resultado es el coeficiente de [[correlacion|correlación de Pearson]] ($r$), acotado entre $-1$ y $+1$. El cálculo de $r$ se basa, por tanto, en las desviaciones típicas y covarianzas entre las variables, y solo puede aplicarse rigurosamente a variables numéricas de nivel de medida al menos de intervalo.

### Matriz de covarianzas

En el caso multivariante, la covarianza se extiende a la **matriz de covarianzas** $\Sigma$, cuya entrada $(i, j)$ es $\text{Cov}(X_i, X_j)$ y cuya diagonal principal contiene las varianzas de cada variable. Esta matriz es central en técnicas como la [[regresion|regresión]] múltiple, el análisis de componentes principales y el análisis factorial, todos ellos habituales en la investigación sociológica.

### Covarianza y regresión

La pendiente del modelo de [[regresion|regresión lineal simple]] se obtiene directamente a partir de la covarianza:

$$\hat{\beta}_1 = \frac{\text{Cov}(X, Y)}{\text{Var}(X)}$$

Así, la covarianza no solo cuantifica la asociación, sino que fundamenta la estimación de efectos entre una [[variable-independiente]] y una [[variable-dependiente]].

## Relación con otros conceptos

- **[[correlacion]]**: la correlación de Pearson es la versión estandarizada de la covarianza, lo que facilita la comparación entre pares de variables medidos en unidades distintas.
- **[[varianza]]**: la covarianza de una variable consigo misma; ambas medidas comparten lógica de dispersión respecto a la media.
- **[[regresion]]**: la covarianza alimenta el cálculo de los coeficientes de regresión, tanto en modelos simples como múltiples.
- **[[variable-dependiente]] y [[variable-independiente]]**: la covarianza entre ellas es requisito para postular relaciones explicativas.
- **[[estadistica-descriptiva]]**: la covarianza se clasifica entre las medidas de asociación bivariada, junto con tablas de contingencia y coeficientes de correlación.
- **[[tabla-de-contingencia]]**: cuando las variables son nominales y no cabe hablar de covarianza, se recurre a tablas de contingencia y al [[chi-cuadrado]] para evaluar la asociación.

## Debates y críticas

1. **Linealidad**: la covarianza capta exclusivamente relaciones lineales. Dos variables pueden presentar una asociación curvilínea intensa y arrojar covarianza cercana a cero, lo que exige complementar el análisis con gráficos de dispersión y transformaciones no lineales.
2. **Sensibilidad a valores extremos**: al basarse en desviaciones respecto a la media, la covarianza resulta vulnerable a observaciones atípicas, problema frecuente en datos de encuesta con muestras pequeñas.
3. **Covarianza no implica causalidad**: como destacan los materiales del curso de Metodología, las relaciones de covarianza "son poco explicativas porque no nos muestran qué es lo que hace cambiar simultáneamente a las dos variables". Una covarianza significativa puede obedecer a causalidad directa, inversa o a la influencia de una tercera variable (relación espúrea). Las ciencias sociales aspiran a superar la mera covarianza para establecer relaciones causales que requieren, además, precedencia temporal, mecanismo causal plausible y control de variables intervinientes.
4. **Nivel de medida**: la covarianza exige variables cuantitativas (intervalo o razón). Para variables ordinales o nominales se precisan medidas alternativas.

## Vigencia contemporánea

La covarianza permanece como pieza angular de la investigación cuantitativa en sociología. En los modelos de ecuaciones estructurales (SEM), el análisis parte de la matriz de covarianzas observada, que se compara con la matriz reproducida por el modelo teórico. El aprendizaje automático aplicado a datos sociales también recurre a la estructura de covarianza para la reducción de dimensiones y la detección de patrones latentes. En la era de los datos masivos, las matrices de covarianza de gran dimensión plantean desafíos computacionales y de estimación que han impulsado técnicas de regularización (como la estimación *shrinkage*), cada vez más presentes en la sociología computacional.

## Ejemplo empírico

Supongamos que un investigador desea analizar la relación entre el **nivel educativo** (años de escolarización) y los **ingresos mensuales** (en euros) en una muestra de 200 individuos. Si la covarianza muestral $S_{xy}$ resulta positiva y elevada, ello sugiere que a mayor escolarización tienden a corresponder mayores ingresos. No obstante, como señala la literatura metodológica, esta covarianza podría deberse al estatus familiar, por lo que el investigador deberá controlar por variables como el origen socioeconómico mediante [[regresion|regresión múltiple]] antes de interpretar la relación como causal.

## Véase también

- [[correlacion]]
- [[varianza]]
- [[regresion]]
- [[variable-dependiente]]
- [[variable-independiente]]
- [[estadistica-descriptiva]]
- [[chi-cuadrado]]
- [[tabla-de-contingencia]]

## Fuentes

- Material del curso *Metodología de las Ciencias Sociales* (2026-S1), Módulos 1 y 3.
- [[el-proceso-de-investigacion-en-las-ciencias-sociales-marco-teorico-y-diseno-empirico]]
- Wikipedia, «Covarianza», disponible en: https://es.wikipedia.org/wiki/Covarianza.
