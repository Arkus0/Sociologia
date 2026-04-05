---
id: nivel-de-confianza
title: Nivel de confianza
note_type: concept
semester: 2026-S1
course: "Metodología de las ciencias sociales"
related_concepts:
  - estadistica-inferencial
  - error-muestral
  - muestra
  - hipotesis
  - tamano-de-la-muestra
  - muestreo
  - intervalo-de-confianza
tags:
  - estadística
  - inferencia
  - metodología-cuantitativa
  - estimación
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\la-investigacion-cuantitativa.md
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\modulo-3.md
updated_at: '2025-07-13'
---

## Definición

El **nivel de confianza** es la probabilidad de que un [[intervalo-de-confianza]] construido a partir de datos muestrales contenga el verdadero valor del parámetro poblacional que se desea estimar. Se expresa como $(1 - \alpha) \times 100\%$, donde $\alpha$ representa el **nivel de significación** o error de tipo I que el investigador está dispuesto a asumir. Así, un nivel de confianza del 95 % implica que, si se repitiera el procedimiento de muestreo un gran número de veces, aproximadamente el 95 % de los intervalos calculados contendrían el parámetro real.

Formalmente, dado un estimador $\hat{\theta}$ del parámetro poblacional $\theta$, se busca un intervalo $[\theta_1, \theta_2]$ tal que:

$$P[\theta_1 \leq \theta \leq \theta_2] = 1 - \alpha$$

Los niveles de confianza más utilizados en la investigación social son el 90 % ($z = 1{,}645$), el 95 % ($z = 1{,}96$) y el 99 % ($z = 2{,}576$), siendo el 95 % el estándar convencional en la mayor parte de las ciencias sociales.

## Origen y contexto histórico

El concepto de nivel de confianza fue formalizado por el matemático polaco **Jerzy Neyman** en su artículo seminal *"Outline of a Theory of Statistical Estimation Based on the Classical Theory of Probability"* (1937), publicado en *Philosophical Transactions of the Royal Society of London*. Neyman desarrolló la teoría de la estimación por intervalos como alternativa a la estimación puntual, proporcionando un marco riguroso para cuantificar la incertidumbre asociada a las inferencias estadísticas. Su trabajo se inscribía en el paradigma frecuentista y representó una respuesta a las ideas fiduciales de Ronald Fisher, con quien mantuvo una prolongada controversia metodológica. La noción se consolidó rápidamente en la práctica de la investigación empírica durante la segunda mitad del siglo XX, convirtiéndose en un pilar de la [[estadistica-inferencial]].

## Desarrollo teórico

El nivel de confianza se comprende a partir de la **distribución muestral** del estimador. Si la distribución poblacional es normal —o el tamaño de la [[muestra]] es suficientemente grande para invocar el Teorema Central del Límite—, la media muestral $\bar{X}$ sigue una distribución $N(\mu, \sigma/\sqrt{n})$. Al estandarizar se obtiene:

$$Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \sim N(0, 1)$$

El valor crítico $z_{\alpha/2}$ delimita las colas de la distribución, de modo que el intervalo de confianza para la media es:

$$\bar{x} \pm z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}$$

El producto $z_{\alpha/2} \cdot SE$ constituye el **margen de error**, magnitud que vincula directamente el nivel de confianza con la precisión de la estimación. Aumentar el nivel de confianza (por ejemplo, del 95 % al 99 %) amplía el intervalo y, por tanto, reduce la precisión de la estimación; reducirlo estrecha el intervalo pero incrementa el riesgo de que el parámetro quede fuera. Esta tensión entre confianza y precisión obliga al investigador a equilibrar ambas exigencias en función de los objetivos del estudio.

Es fundamental señalar que el nivel de confianza se refiere al **procedimiento** y no al intervalo concreto obtenido en una muestra particular. Una vez calculado, el intervalo específico contiene o no contiene el parámetro —es un hecho determinístico—; la probabilidad se predica del método a largo plazo.

## Relación con otros conceptos

El nivel de confianza se articula con un conjunto de nociones interrelacionadas de la metodología cuantitativa:

- **[[error-muestral]]**: el nivel de confianza determina, junto con la variabilidad y el tamaño muestral, la amplitud del margen de error tolerable. Según el temario de Borge y Padró-Solanet (UOC), cuatro factores interrelacionados inciden en el error admisible: variabilidad de la población, tamaño de la población, nivel de confianza deseado y margen de error aceptable.
- **[[tamano-de-la-muestra]]**: la fórmula clásica para el cálculo del tamaño muestral en proporciones, $n = z^2 \cdot p \cdot q / \varepsilon^2$, incorpora el valor $z$ correspondiente al nivel de confianza elegido. A mayor confianza, mayor tamaño muestral requerido.
- **[[hipotesis]]**: en el contraste de hipótesis, el nivel de confianza es el complemento del nivel de significación ($\alpha$). Un contraste al 5 % de significación equivale a un nivel de confianza del 95 %.
- **[[muestreo]]**: solo el muestreo probabilístico permite calcular legítimamente intervalos de confianza, pues presupone que cada elemento de la población tiene una probabilidad conocida de ser seleccionado.
- **[[estadistica-inferencial]]**: el nivel de confianza es uno de los pilares de la inferencia, tanto en la estimación intervalar como en la lógica del contraste de hipótesis.

## Debates y críticas

### Interpretación frecuentista vs. bayesiana

La interpretación frecuentista del nivel de confianza —la que se emplea convencionalmente— se refiere a la frecuencia relativa a largo plazo con que el procedimiento acierta. El enfoque **bayesiano** ofrece una alternativa conceptualmente distinta: el **intervalo de credibilidad**, que permite afirmar directamente que la probabilidad de que el parámetro se encuentre en un intervalo dado es, por ejemplo, del 95 %, condicionada a los datos observados y a una distribución *a priori*. Esta diferencia, aunque técnica, tiene implicaciones profundas para la comunicación de resultados en ciencias sociales.

### El umbral del 95 %

La comunidad científica ha debatido si el umbral convencional del 95 % es adecuado. Benjamin et al. (2018) propusieron elevar el estándar al 99,5 % para resultados que se consideren "descubrimientos", argumentando que el umbral tradicional contribuye a la crisis de replicabilidad. Otros autores abogan por abandonar los umbrales fijos en favor de la comunicación directa del tamaño del efecto y del intervalo de confianza completo, sin dicotomizar los resultados en "significativos" y "no significativos".

### Malinterpretación frecuente

Un error extendido —incluso entre investigadores— consiste en interpretar un intervalo de confianza del 95 % como que "hay un 95 % de probabilidad de que el parámetro esté en este intervalo concreto". Estrictamente, la afirmación correcta es que el *método* genera intervalos que contienen el parámetro en el 95 % de las repeticiones del muestreo.

## Vigencia contemporánea

En la investigación social contemporánea, el nivel de confianza sigue siendo un componente ineludible de cualquier diseño cuantitativo. Las grandes encuestas —como el Barómetro del CIS en España— comunican sus resultados con un margen de error de ±2-3 % para un nivel de confianza del 95,5 %. No obstante, el movimiento de **ciencia abierta** y las directrices de la American Statistical Association (ASA, 2016) promueven una presentación más matizada de la incertidumbre, que no se limite a reportar si un resultado "alcanza" o no el umbral convencional. Las corrientes actuales enfatizan la importancia de reportar intervalos de confianza junto con tamaños del efecto, en lugar de depender exclusivamente de valores *p*.

## Ejemplo empírico

Un equipo de investigación realiza una encuesta sobre intención de voto a una [[muestra]] aleatoria de $n = 1\,000$ personas. La proporción muestral que manifiesta intención de votar al partido A es $\hat{p} = 0{,}45$. Con un [[nivel-de-confianza]] del 95 % ($z = 1{,}96$), el margen de error es:

$$\varepsilon = 1{,}96 \cdot \sqrt{\frac{0{,}45 \times 0{,}55}{1\,000}} \approx \pm 3{,}1 \text{ pp}$$

El intervalo de confianza resultante es $[41{,}9\%;\; 48{,}1\%]$. Esto significa que, si el procedimiento de muestreo se repitiese muchas veces, el 95 % de los intervalos construidos contendría la verdadera proporción poblacional. Si se desease un nivel de confianza del 99 % ($z = 2{,}576$), el margen se ampliaría a $\pm 4{,}1$ pp, y sería necesario aumentar la muestra para mantener la misma precisión.

## Véase también

- [[estadistica-inferencial]]
- [[error-muestral]]
- [[muestra]]
- [[hipotesis]]
- [[tamano-de-la-muestra]]
- [[muestreo]]
- [[inferencia]]
- [[encuesta-de-opinion]]
- [[variable-independiente]]

## Fuentes

- Neyman, J. (1937). "Outline of a Theory of Statistical Estimation Based on the Classical Theory of Probability". *Philosophical Transactions of the Royal Society of London A*, 236, 333-380.
- Fisher, R. A. (1956). *Statistical Methods and Scientific Inference*. Oliver and Boyd.
- Benjamin, D. J. et al. (2018). "Redefine statistical significance". *Nature Human Behaviour*, 2(1), 6-10.
- Wasserstein, R. L. y Lazar, N. A. (2016). "The ASA Statement on p-Values". *The American Statistician*, 70(2), 129-133.
- Borge, R. y Padró-Solanet, A. (2026). *Metodología de las ciencias sociales*. UOC — Módulo 3: La investigación cuantitativa.
