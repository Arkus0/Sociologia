---
id: media-aritmetica
title: Media aritmética
note_type: concept
semester: 2026-S1
course: "Metodologia de las ciencias sociales"
related_concepts:
  - mediana
  - moda
  - varianza
  - desviacion-estandar
  - estadistica-descriptiva
  - niveles-de-medicion
  - covarianza
  - distribucion-normal
tags:
  - estadística
  - medidas-de-tendencia-central
  - metodología-cuantitativa
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\modulo-3.md
updated_at: "2025-07-13"
---

## Definición

La **media aritmética** —comúnmente denominada *promedio* o simplemente *media*— es la medida de tendencia central que se obtiene sumando todos los valores observados de una variable y dividiendo el resultado entre el número total de observaciones. Formalmente, dados $n$ valores $x_1, x_2, \dots, x_n$, la media muestral se define como:

$$\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i = \frac{x_1 + x_2 + \cdots + x_n}{n}$$

Cuando el conjunto de datos corresponde a la totalidad de una población, se habla de **media poblacional** y se denota con la letra griega $\mu$; cuando proviene de una muestra, se denomina **media muestral** ($\bar{x}$). Esta distinción es fundamental en [[estadistica-inferencial]], donde la media muestral funciona como estimador insesgado de la media poblacional.

La media aritmética solo tiene sentido para variables medidas en escala de **intervalo** o **de razón**, es decir, aquellas en las que las distancias entre valores son cuantificables y homogéneas. Calcularla sobre variables nominales u ordinales constituye un error metodológico frecuente que los [[niveles-de-medicion]] permiten evitar.

## Origen y contexto histórico

El concepto de promedio tiene raíces antiguas: los astrónomos babilónicos ya utilizaban promedios para suavizar observaciones celestes. Sin embargo, la formalización estadística moderna se atribuye a la tradición europea de los siglos XVII y XVIII. **Abraham de Moivre** y **Pierre-Simon Laplace** desarrollaron las bases probabilísticas que vincularían la media con la distribución normal.

El hito más relevante para las ciencias sociales lo estableció el astrónomo y estadístico belga **Adolphe Quetelet** (1796-1874). En su obra *Sur l'homme et le développement de ses facultés* (1835), Quetelet introdujo el concepto del **«hombre medio»** (*l'homme moyen*): un individuo ficticio cuyos atributos físicos y morales coinciden con los promedios de la población. Esta idea revolucionó el pensamiento social al proponer que las regularidades estadísticas de los fenómenos humanos —tasas de criminalidad, estatura, propensión al matrimonio— obedecían a leyes análogas a las de la física. La media aritmética dejaba de ser un mero recurso de cálculo para convertirse en herramienta de descripción sociológica.

## Desarrollo teórico

La media aritmética posee propiedades algebraicas que fundamentan su uso extendido en la investigación cuantitativa:

1. **Centro de gravedad.** La suma de las desviaciones respecto de la media es siempre cero: $\sum (x_i - \bar{x}) = 0$. La media es el único valor que equilibra las distancias positivas y negativas de todos los datos.
2. **Mínimos cuadrados.** La media minimiza la suma de las desviaciones al cuadrado $\sum (x_i - c)^2$; ninguna otra constante $c$ produce un valor inferior. Esta propiedad la conecta directamente con la [[varianza]] y con la [[regresion]] por mínimos cuadrados ordinarios.
3. **Invarianza bajo transformación lineal.** Si cada dato se transforma como $y_i = a + bx_i$, entonces $\bar{y} = a + b\bar{x}$. Esto garantiza la coherencia al cambiar unidades de medida.
4. **Acotación.** La media se sitúa siempre entre el valor mínimo y el máximo de la distribución: $\min(x_i) \leq \bar{x} \leq \max(x_i)$.

Una extensión importante es la **media ponderada**, en la que cada observación recibe un peso $w_i$ proporcional a su relevancia o frecuencia:

$$\bar{x}_w = \frac{\sum w_i \, x_i}{\sum w_i}$$

En sociología, la ponderación es habitual cuando las muestras no son autoponderadas: por ejemplo, al corregir la sobrerrepresentación de ciertos estratos en una [[encuesta]]. Otra variante es la **media recortada** (*trimmed mean*), que excluye un porcentaje de valores extremos antes de calcular el promedio, ofreciendo mayor robustez frente a outliers.

## Relación con otros conceptos

La media aritmética forma parte de la tríada clásica de medidas de tendencia central junto con la [[mediana]] y la [[moda]]. En distribuciones simétricas —como la [[distribucion-normal]]— las tres coinciden; en distribuciones asimétricas divergen, y la elección entre ellas depende del nivel de medición y del objetivo analítico.

La [[varianza]] y la [[desviacion-estandar]] son medidas de dispersión definidas a partir de la media: la varianza es el promedio de las desviaciones cuadráticas respecto de $\bar{x}$, y la desviación estándar es su raíz cuadrada. Sin la media, estas medidas carecerían de punto de referencia. La [[covarianza]], a su vez, generaliza la idea al medir la variación conjunta de dos variables respecto de sus medias respectivas.

Dentro de la [[estadistica-descriptiva]], la media resume la posición central de una distribución y constituye el insumo básico para técnicas más complejas: análisis de varianza (ANOVA), pruebas *t* de Student, [[regresion]] lineal y correlación de Pearson. Su aplicabilidad está condicionada por los [[niveles-de-medicion]]: solo las escalas de intervalo y de razón la admiten legítimamente.

## Debates y críticas

La media aritmética ha sido objeto de críticas persistentes en las ciencias sociales:

- **Sensibilidad a valores atípicos.** Un único dato extremo puede desplazar la media de forma drástica, tornándola poco representativa del conjunto. En la distribución del ingreso, por ejemplo, unos pocos individuos de renta muy alta elevan la media muy por encima de lo que percibe la mayoría de la población, mientras la mediana refleja mejor la experiencia típica. Darrell Huff popularizó esta advertencia en *How to Lie with Statistics* (1954).
- **Falacia ecológica.** Interpretar la media de un agregado como si describiera a cada individuo del grupo constituye un error lógico clásico señalado por William S. Robinson (1950): la media de ingreso de un barrio no implica que todos sus habitantes ganen esa cantidad.
- **Inaplicabilidad a escalas no métricas.** Calcular promedios sobre variables ordinales —como escalas Likert de satisfacción— es una práctica extendida pero metodológicamente cuestionable, dado que la distancia entre categorías no es homogénea.

## Vigencia contemporánea

En la investigación social actual, la media aritmética mantiene un papel central pero matizado. Las encuestas de hogares (como la Encuesta Permanente de Hogares en Argentina o la Encuesta de Población Activa en España) reportan medias de ingreso, horas trabajadas y años de escolaridad junto con medianas y percentiles para ofrecer un panorama más completo. Los métodos de estadística robusta —medias recortadas, estimadores M de Huber— se aplican cada vez más cuando las distribuciones no son gaussianas. En el ámbito del *big data* y la sociología computacional, las medias se calculan sobre volúmenes masivos de datos digitales (tiempos de conexión, frecuencia de interacciones), donde la escala mitiga el efecto de valores atípicos individuales pero plantea nuevos desafíos de representatividad.

## Ejemplo empírico

Un equipo de investigación desea describir el ingreso mensual de 200 hogares de un barrio periférico. Tras la recolección de datos, obtiene una media de $185 000 y una mediana de $142 000. La diferencia indica una distribución asimétrica positiva: un subgrupo reducido de hogares con ingresos elevados «arrastra» la media hacia arriba. El equipo decide reportar ambas medidas y calcular la [[desviacion-estandar]] ($95 000) para cuantificar la dispersión. Adicionalmente, calcula la media recortada al 5 % ($161 000), que excluye los valores más extremos y ofrece un valor intermedio más estable. Este procedimiento ilustra por qué la media aritmética, siendo indispensable, debe complementarse con otras estadísticas descriptivas para evitar conclusiones simplistas sobre la realidad social.

## Véase también

- [[mediana]]
- [[moda]]
- [[varianza]]
- [[desviacion-estandar]]
- [[estadistica-descriptiva]]
- [[niveles-de-medicion]]
- [[covarianza]]
- [[regresion]]
- [[distribucion-normal]]
- [[error-muestral]]

## Fuentes

- Quetelet, A. (1835). *Sur l'homme et le développement de ses facultés, ou Essai de physique sociale*. París: Bachelier.
- Huff, D. (1954). *How to Lie with Statistics*. Nueva York: W. W. Norton.
- Medhi, J. (1992). *Statistical Methods: An Introductory Text*. Nueva Delhi: New Age International, pp. 53-58.
- Material del curso: [[la-investigacion-cuantitativa]] (Metodología de las ciencias sociales, 2026-S1).
