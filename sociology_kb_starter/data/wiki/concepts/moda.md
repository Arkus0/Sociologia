---
id: moda
title: Moda
note_type: concept
semester: 2026-S1
course: "Metodologia de las ciencias sociales"
related_concepts:
  - media-aritmetica
  - mediana
  - estadistica-descriptiva
  - niveles-de-medicion
  - variables-sociodemograficas
  - varianza
  - distribucion-de-frecuencias
tags:
  - estadistica-descriptiva
  - tendencia-central
  - metodologia
  - datos-nominales
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\modulo-3.md
updated_at: '2025-07-13'
---

## Definición

En [[estadistica-descriptiva]], la **moda** es el valor que aparece con mayor frecuencia en un conjunto de datos. Formalmente, dada una distribución de frecuencias, la moda corresponde a la categoría o valor numérico cuya frecuencia absoluta es máxima. A diferencia de la [[media-aritmetica]] y la [[mediana]], la moda no requiere que los datos sean cuantitativos ni que estén ordenados: es la única medida de tendencia central aplicable a todos los [[niveles-de-medicion]], incluido el nivel nominal. Por ejemplo, si en una encuesta sobre confesión religiosa la categoría «católica» registra la mayor cantidad de respuestas, dicha categoría constituye la moda de la distribución.

Una distribución puede ser **unimodal** (una sola moda), **bimodal** (dos valores comparten la frecuencia máxima), **multimodal** (tres o más modas) o **amodal** (todos los valores presentan la misma frecuencia, lo que torna inútil el concepto). La muestra se considera homogénea cuando posee una sola moda y heterogénea cuando presenta más de una.

## Origen y contexto histórico

El término *mode* fue introducido por **Karl Pearson** en 1895, dentro de su artículo «Contributions to the Mathematical Theory of Evolution. II. Skew Variation in Homogeneous Material», publicado en las *Philosophical Transactions of the Royal Society of London*. Pearson tomó la expresión del lenguaje cotidiano —«estar a la moda» designa aquello que la mayoría usa o prefiere— y la trasladó a la estadística para nombrar el valor más frecuente. Con ello vinculó intuitivamente frecuencia social y frecuencia numérica.

No obstante, según W. Allen Wallis y Harry V. Roberts (*Course in Statistics*), una referencia temprana al razonamiento modal puede rastrearse hasta el sitio de Platea (428 a. C.), cuando los atenienses asediados necesitaron estimar la altura de las murallas enemigas contando las capas de ladrillos: la cifra que coincidía en la mayoría de los recuentos —es decir, la moda de las observaciones— se adoptó como la más fiable para construir escaleras de escape.

## Desarrollo teórico

La moda se define de manera diferente según el tipo de datos:

- **Datos no agrupados.** Se identifica directamente el valor con mayor frecuencia absoluta. Para la muestra {1, 3, 6, 6, 6, 7, 12, 17}, la moda es 6.
- **Datos agrupados en intervalos.** Se localiza primero el *intervalo modal* (el de mayor frecuencia absoluta) y luego se calcula la moda mediante la fórmula de interpolación:

$$M_o = L_i + \frac{D_1}{D_1 + D_2} \cdot A_i$$

donde $L_i$ es el límite inferior del intervalo modal, $D_1$ la diferencia entre la frecuencia modal y la premodal, $D_2$ la diferencia entre la frecuencia modal y la postmodal, y $A_i$ la amplitud del intervalo.

- **Distribuciones de probabilidad continuas.** La moda poblacional es el valor $x$ en el que la función de densidad de probabilidad alcanza su máximo. En distribuciones unimodales simétricas —como la [[distribucion-normal]]— media, mediana y moda coinciden; en distribuciones asimétricas se separan, y la relación empírica de Pearson establece: $\text{media} - \text{moda} \approx 3(\text{media} - \text{mediana})$.

Una propiedad relevante es la **invariancia ante transformaciones lineales**: si $X$ se transforma en $aX + b$, la moda se transforma de igual modo. Sin embargo, bajo transformaciones monótonas no lineales, la moda puede cambiar de forma impredecible. Además, la moda es robusta frente a valores atípicos (*outliers*): lecturas extremas no la afectan, a diferencia de la media aritmética.

## Relación con otros conceptos

La moda forma parte de la tríada clásica de **medidas de tendencia central** junto con la [[media-aritmetica]] y la [[mediana]]. Cada una sintetiza la distribución de un modo distinto:

| Medida | Nivel mínimo requerido | Sensibilidad a *outliers* |
|--------|----------------------|--------------------------|
| Moda   | Nominal              | Nula                     |
| Mediana| Ordinal              | Baja                     |
| Media  | De intervalo/razón   | Alta                     |

El vínculo con los [[niveles-de-medicion]] es fundamental: para variables nominales —como religión, estado civil o nacionalidad— la moda es la *única* medida de tendencia central legítima. Para variables ordinales se puede añadir la mediana, y solo en niveles de intervalo o razón resulta válida la media aritmética. Este principio se subraya en los materiales del módulo 3 del curso cuando se señala que «los valores asignados a cada grupo son solo etiquetas que sirven para diferenciarlos; las operaciones aritméticas no tienen sentido».

La moda también se relaciona con la [[varianza]] y las medidas de dispersión: una distribución con moda muy pronunciada (alta frecuencia concentrada en un solo valor) suele exhibir menor dispersión, mientras que distribuciones multimodales indican heterogeneidad interna, lo cual resulta sociológicamente significativo al analizar [[variables-sociodemograficas]].

## Debates y críticas

Las principales limitaciones de la moda como estadístico resumen son:

1. **Inestabilidad muestral.** Su valor depende solo de las frecuencias locales, por lo que puede variar considerablemente entre muestras extraídas de la misma población.
2. **Dependencia de la agrupación.** En datos agrupados, la moda es sensible al número y amplitud de los intervalos elegidos; distintas anchuras de clase pueden producir modas diferentes.
3. **Pobre representatividad.** La moda puede situarse lejos del centro de la distribución y no recoge información del grueso de las observaciones.
4. **Ambigüedad en distribuciones multimodales.** Cuando existen dos o más modas, la síntesis mediante un solo valor pierde toda utilidad descriptiva.

A pesar de estas críticas, los defensores del análisis descriptivo subrayan que la moda proporciona una lectura inmediata y comunicable del dato más típico, lo que la convierte en recurso habitual del periodismo de datos y de los informes de opinión pública, donde se construye un «retrato robot» de un colectivo a partir de las categorías más frecuentes de sus atributos.

## Vigencia contemporánea

En la investigación social cuantitativa actual, la moda conserva un papel indispensable en al menos tres ámbitos:

- **Análisis de variables cualitativas.** Todo estudio que trabaje con categorías nominales —afiliación partidaria, lengua materna, tipo de hogar— recurre a la moda para identificar la categoría predominante.
- **Exploración previa al modelado.** La inspección de la moda (y de la eventual multimodalidad) constituye un paso estándar del análisis exploratorio de datos, pues una distribución bimodal puede sugerir la presencia de subpoblaciones latentes.
- **Encuestas de opinión y marketing político.** Las encuestas preelectorales informan de la opción electoral modal como indicador de la preferencia mayoritaria, complementando las estimaciones de intención de voto basadas en medias ponderadas.

## Ejemplo empírico

En una encuesta a 200 hogares de un barrio metropolitano se pregunta por el nivel de estudios del cabeza de familia (variable nominal: primaria, secundaria, bachillerato, universidad, posgrado). Las frecuencias observadas son: primaria 18, secundaria 52, bachillerato 65, universidad 48, posgrado 17. La **moda** es «bachillerato», la categoría con mayor frecuencia absoluta (65). No tendría sentido calcular la [[media-aritmetica]] de estas categorías, puesto que la variable es nominal; la moda ofrece la única síntesis legítima de tendencia central: el nivel de estudios más frecuente en el barrio es bachillerato.

Si se desagregara la muestra por sexo y se hallase que entre las mujeres la moda es «universidad» y entre los hombres «secundaria», estaríamos ante una distribución bimodal por subgrupos, hallazgo que invitaría a explorar desigualdades de género en el acceso educativo.

## Véase también

- [[media-aritmetica]]
- [[mediana]]
- [[estadistica-descriptiva]]
- [[niveles-de-medicion]]
- [[variables-sociodemograficas]]
- [[varianza]]
- [[distribucion-de-frecuencias]]

## Fuentes

- Pearson, K. (1895). *Contributions to the Mathematical Theory of Evolution. II. Skew Variation in Homogeneous Material*. Philosophical Transactions of the Royal Society of London, Ser. A, 186, 343-414.
- Wallis, W. A. y Roberts, H. V. (1956). *Statistics: A New Approach*. Glencoe: Free Press.
- Módulo 3, *Metodología de las Ciencias Sociales*, 2026-S1 — [[modulo-3]].
- Huot, R. (1999). *Métodos cuantitativos para las ciencias humanas*. Lisboa: Piaget.
- [[la-investigacion-cuantitativa]] (Metodología de las ciencias sociales).
