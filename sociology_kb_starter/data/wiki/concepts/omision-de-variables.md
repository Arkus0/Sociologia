---
id: omision-de-variables
title: Omisión de variables
note_type: concept
semester: 2026-S1
course: "Metodologia de las ciencias sociales"
related_concepts:
  - endogeneidad
  - relacion-espurea
  - variable-de-control
  - regresion
  - seleccion-de-variables
  - causalidad
  - variable-independiente
  - validez-interna
tags:
  - econometría
  - sesgo
  - especificación
  - regresión
  - metodología-cuantitativa
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\modulo-2.md
updated_at: '2025-07-13'
---

## Definición

La **omisión de variables** (*omitted variable bias*, OVB) designa el sesgo sistemático que se introduce en los estimadores de un modelo de [[regresion]] cuando una variable relevante queda excluida de la especificación. En términos formales, si el modelo verdadero es:

$$y_i = a + b\,x_i + c\,z_i + u_i$$

pero el investigador estima únicamente $y_i = \alpha + \hat{b}\,x_i + \epsilon_i$ omitiendo $z_i$, el estimador $\hat{b}$ no recupera el efecto parcial $b$ sino una combinación $b + c\,f$, donde $f$ es el coeficiente de la regresión auxiliar de $z$ sobre $x$. El sesgo $c \cdot f$ aparece siempre que se cumplen **dos condiciones simultáneas**: (1) la variable omitida $z$ es un determinante de la variable dependiente $y$ ($c \neq 0$) y (2) $z$ está correlacionada con al menos una [[variable-independiente]] incluida en el modelo ($f \neq 0$). Cuando cualquiera de estas condiciones no se satisface, la omisión no genera sesgo, aunque puede reducir la eficiencia del estimador.

## Origen y contexto histórico

El problema de la omisión de variables se formalizó en el marco de la econometría clásica durante la segunda mitad del siglo XX, vinculado al desarrollo de los supuestos del teorema de Gauss-Markov para mínimos cuadrados ordinarios (OLS). Autores como Arthur Goldberger y William Greene sistematizaron las consecuencias de la mala especificación del modelo lineal. Greene (1993) dedicó un tratamiento detallado a las propiedades del estimador OLS bajo omisión, mostrando que el sesgo persiste incluso asintóticamente —es decir, que el estimador no es solo sesgado sino también **inconsistente**—. En el campo de las ciencias sociales, la preocupación por las variables omitidas se acentuó con la expansión del análisis multivariante a partir de las décadas de 1960 y 1970, cuando se hizo evidente que muchas relaciones aparentemente causales desaparecían al introducir controles adicionales.

## Desarrollo teórico

### La fórmula del sesgo

En notación matricial, si $Y = X\beta + Z\delta + U$ y se omite $Z$, el estimador OLS de $\beta$ resulta:

$$E[\hat{\beta} \mid X] = \beta + (X'X)^{-1}X'Z\,\delta$$

El segundo sumando es el sesgo. Su **dirección** depende del signo del producto entre $\delta$ (efecto de la variable omitida sobre $y$) y la correlación entre $Z$ y $X$. Si ambas relaciones son del mismo signo, el sesgo es positivo (sobreestimación); si son de signo opuesto, es negativo (subestimación). Esta regla de signos constituye una herramienta diagnóstica fundamental para evaluar la dirección probable del sesgo cuando se sospecha la existencia de confusores no observados.

### Variables instrumentales como solución

Cuando la variable omitida no es observable —lo que impide su inclusión directa como [[variable-de-control]]—, la econometría recurre a las **variables instrumentales** (IV). Un instrumento válido debe estar correlacionado con la variable independiente problemática pero no tener efecto directo sobre $y$ excepto a través de $x$. El estimador de mínimos cuadrados en dos etapas (2SLS) permite recuperar un estimador consistente de $b$ bajo estos supuestos. Sin embargo, encontrar instrumentos convincentes constituye uno de los desafíos más discutidos en la investigación empírica.

### DAGs y la perspectiva causal de Pearl

Desde la década de 2000, los **grafos acíclicos dirigidos** (DAGs) propuestos por Judea Pearl ofrecen un marco gráfico complementario para diagnosticar la omisión de variables. En un DAG, una variable confusora $z$ que tiene flechas hacia $x$ y hacia $y$ genera un *back-door path* que sesga la estimación del efecto causal. El criterio de la puerta trasera (*back-door criterion*) permite identificar el conjunto mínimo de variables que deben condicionarse para bloquear las vías espurias, proporcionando así una guía teórica para la [[seleccion-de-variables]] en modelos causales.

## Relación con otros conceptos

La omisión de variables es la fuente más frecuente de [[endogeneidad]] en los modelos de regresión: cuando $z$ queda fuera del modelo, su efecto se absorbe en el término de error, generando correlación entre $x$ y $\varepsilon$. Este mecanismo está estrechamente ligado a la [[relacion-espurea]], puesto que la asociación observada entre $x$ e $y$ puede deberse enteramente al confusor omitido y no a un nexo causal genuino. La estrategia habitual de mitigación consiste en incorporar la variable confusora como [[variable-de-control]], siempre que sea observable y se especifique correctamente. A nivel de diseño, el problema incide directamente sobre la [[validez-interna]]: un modelo con variables omitidas relevantes no permite inferir con rigor que $x$ causa $y$. En la práctica, la decisión de qué variables incluir u omitir forma parte del problema más amplio de la [[seleccion-de-variables]], donde debe ponderarse el sesgo de omisión frente a la ineficiencia que produce la inclusión de variables irrelevantes (el denominado *trade-off* sesgo-varianza).

## Debates y críticas

Un primer debate concierne a la **detectabilidad** del sesgo: dado que la variable omitida es, por definición, no observada en la especificación del investigador, el sesgo no puede estimarse directamente. Técnicas como el análisis de sensibilidad de Oster (2019) y los límites de Altonji, Elder y Taber (2005) ofrecen aproximaciones indirectas, evaluando cuán grande debería ser la selección por inobservables para invalidar un resultado. Un segundo debate apunta a la tentación de incluir indiscriminadamente variables de control para «protegerse» del OVB: esta práctica puede introducir nuevos sesgos si alguna de las variables añadidas es un mediador causal o un colisionador, como muestra la teoría de DAGs. Clarke (2005) advirtió que el temor al OVB ha generado una cultura de «regresiones de fregadero» (*kitchen-sink regressions*) que compromete la interpretabilidad de los modelos en ciencias sociales.

## Vigencia contemporánea

En la investigación social contemporánea, la preocupación por la omisión de variables motiva el recurso a diseños cuasi-experimentales —como diferencias en diferencias, regresión discontinua y variables instrumentales— que explotan fuentes exógenas de variación para sortear los confusores no observados. En el ámbito del *big data* y el aprendizaje automático, métodos como *double machine learning* (Chernozhukov et al., 2018) combinan técnicas de predicción flexible con estimación causal para reducir el sesgo por variables omitidas en entornos de alta dimensionalidad. No obstante, la lógica fundamental del OVB sigue siendo la misma que formulara la econometría clásica: sin una teoría sustantiva que guíe la especificación, ningún método estadístico garantiza la identificación del efecto [[causalidad|causal]] de interés.

## Ejemplo empírico

Un investigador desea estimar el efecto del nivel educativo ($x$) sobre el ingreso ($y$). Si omite la variable «habilidad innata» ($z$), que se correlaciona positivamente tanto con la educación como con el ingreso, el estimador OLS del retorno educativo estará sesgado **al alza**: $\hat{b} = b + c \cdot f$ donde tanto $c > 0$ como $f > 0$. Este es el conocido problema de la «habilidad omitida» en la ecuación minceriana. Card (1999) utilizó la proximidad geográfica a universidades como variable instrumental para aislar el efecto causal de la educación, obteniendo estimaciones que en algunos casos resultaron menores que las de OLS, consistentes con un sesgo positivo por variable omitida.

## Véase también

- [[endogeneidad]]
- [[relacion-espurea]]
- [[variable-de-control]]
- [[regresion]]
- [[seleccion-de-variables]]
- [[causalidad]]
- [[variable-independiente]]
- [[validez-interna]]
- [[multicolinealidad]]
- [[sesgo-omision-de-variables-relevantes]]

## Fuentes

- Greene, W. H. (1993). *Econometric Analysis* (2.ª ed.). Macmillan, pp. 245-246.
- Wooldridge, J. M. (2009). *Introductory Econometrics: A Modern Approach* (4.ª ed.). Cengage Learning, pp. 89-93.
- Clarke, K. A. (2005). "The Phantom Menace: Omitted Variable Bias in Econometric Research". *Conflict Management and Peace Science*, 22(4), 341-352.
- Pearl, J. (2009). *Causality: Models, Reasoning, and Inference* (2.ª ed.). Cambridge University Press.
- Card, D. (1999). "The Causal Effect of Education on Earnings". *Handbook of Labor Economics*, vol. 3A, 1801-1863.
- Fuente del curso: [[procedimientos-y-decisiones-para-determinar-que-se-observara]] (Metodología de las ciencias sociales, Módulo 2).
