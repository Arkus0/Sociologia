---
id: desviacion-estandar
title: Desviación estándar
note_type: concept
semester: 2026-S1
course: "Metodología de las ciencias sociales"
related_concepts:
  - varianza
  - media-aritmetica
  - estadistica-descriptiva
  - error-muestral
  - nivel-de-confianza
  - distribucion-normal
  - coeficiente-de-variacion
tags:
  - estadística
  - dispersión
  - metodología-cuantitativa
  - análisis-de-datos
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\modulo-3.md
updated_at: '2025-07-13'
---

## Definición

La **desviación estándar** (también denominada *desviación típica*; símbolo σ para poblaciones, *s* para muestras) es una medida de [[estadistica-descriptiva]] que cuantifica el grado de dispersión o variabilidad de un conjunto de datos respecto de su [[media-aritmetica]]. Formalmente, se define como la **raíz cuadrada de la [[varianza]]**:

$$
\sigma = \sqrt{\frac{1}{N}\sum_{i=1}^{N}(x_i - \mu)^2}
$$

donde $N$ es el tamaño de la población, $x_i$ cada observación y $\mu$ la media poblacional. A diferencia de la varianza —que se expresa en unidades al cuadrado—, la desviación estándar conserva las mismas unidades que los datos originales, lo que facilita su interpretación sustantiva. Una desviación estándar baja indica que los valores tienden a agruparse cerca de la media; una alta señala que se dispersan en un rango amplio.

## Origen y contexto histórico

El concepto de cuantificar la dispersión de las observaciones se remonta a Carl Friedrich Gauss, quien a principios del siglo XIX empleó la noción de *error medio* (*mittlerer Fehler*) en sus trabajos de astronomía y geodesia. Sin embargo, fue **Karl Pearson** quien en 1894, en una comunicación a la Royal Society de Londres titulada *"On the dissection of asymmetrical frequency curves"*, acuñó formalmente el término *standard deviation*, que desplazó denominaciones anteriores. La estandarización del nombre acompañó la profesionalización de la estadística como disciplina auxiliar de las ciencias sociales y naturales durante el último cuarto del siglo XIX.

Friedrich Bessel, décadas antes (1815-1818), había propuesto la corrección que lleva su nombre: al estimar la desviación estándar poblacional a partir de una muestra, se divide por $N-1$ en lugar de $N$. Esta **corrección de Bessel** compensa el sesgo inherente a la estimación muestral y constituye la práctica estándar en investigación social.

## Desarrollo teórico

### Desviación estándar poblacional y muestral

Cuando se dispone de todos los elementos de una población, se calcula la desviación estándar poblacional (σ). En ciencias sociales, sin embargo, lo habitual es trabajar con muestras. La desviación estándar muestral se calcula como:

$$
s = \sqrt{\frac{1}{N-1}\sum_{i=1}^{N}(x_i - \bar{x})^2}
$$

El denominador $N-1$ corresponde a los *grados de libertad* del vector de desviaciones y produce un estimador insesgado de la varianza poblacional.

### Distribución normal y la regla 68-95-99,7

En una [[distribucion-normal]], la desviación estándar determina la forma de la curva de campana. La **regla empírica** establece que aproximadamente el 68,27 % de las observaciones caen dentro de ±1σ de la media, el 95,45 % dentro de ±2σ, y el 99,73 % dentro de ±3σ. Esta propiedad es fundamental para la investigación por encuestas: permite estimar, antes de realizar el estudio, la proporción de casos que se situarán dentro de un margen dado.

### Puntuaciones estándar (*z-scores*)

Cualquier observación puede convertirse en una **puntuación estándar** o *z-score* mediante la fórmula $z = (x - \mu) / \sigma$. Esta transformación sitúa todos los valores en una escala común con media 0 y desviación estándar 1, posibilitando la comparación entre distribuciones con unidades o escalas diferentes —por ejemplo, comparar ingresos y años de escolarización—.

## Relación con otros conceptos

La desviación estándar es inseparable de la [[varianza]]: la primera es la raíz cuadrada de la segunda, y ambas pertenecen al conjunto de medidas de dispersión de la [[estadistica-descriptiva]]. Junto con la [[media-aritmetica]], forma el par mínimo para resumir una distribución unimodal simétrica.

En el ámbito de la estadística inferencial, la desviación estándar alimenta el cálculo del **error estándar** (σ/√n), que a su vez define el [[error-muestral]] y los intervalos de confianza. La amplitud de estos intervalos depende del [[nivel-de-confianza]] elegido: un intervalo del 95 % abarca ±1,96 desviaciones estándar alrededor de la media muestral. De este modo, varianza, desviación estándar, error muestral y nivel de confianza forman una cadena conceptual que articula el paso de la descripción a la inferencia.

El **coeficiente de variación** (CV = s/x̄) permite comparar la dispersión relativa de distribuciones con medias distintas, resolviendo la limitación de que la desviación estándar es sensible a la escala de medición.

## Debates y críticas

1. **Sensibilidad a valores extremos.** Al basarse en desviaciones al cuadrado, la desviación estándar otorga un peso desproporcionado a los *outliers*. En distribuciones asimétricas —frecuentes en datos de ingresos, por ejemplo— medidas alternativas como la desviación media absoluta o el rango intercuartílico pueden resultar más robustas.

2. **Supuesto de normalidad.** La regla 68-95-99,7 solo es válida estrictamente para distribuciones normales. En ciencias sociales, muchas variables (participación electoral, fecundidad, tasas de criminalidad) presentan distribuciones asimétricas o con colas pesadas, donde la desviación estándar puede inducir interpretaciones erróneas si se aplica mecánicamente.

3. **Estimación muestral y tamaño de muestra.** Aunque la corrección de Bessel elimina el sesgo de la varianza muestral, la desviación estándar muestral sigue siendo un estimador ligeramente sesgado de σ. El sesgo es relevante para muestras pequeñas (N < 10) y decrece como 1/N a medida que crece el tamaño muestral.

## Vigencia contemporánea

La desviación estándar permanece como la medida de dispersión más utilizada en la investigación social cuantitativa. Los informes de organismos internacionales (CEPAL, Eurostat, Banco Mundial) expresan la variabilidad de indicadores sociales —IDH, tasa de pobreza, coeficiente de Gini— mediante desviaciones estándar. En el análisis de encuestas de opinión, el margen de error publicado en los medios es, en esencia, un múltiplo de la desviación estándar de la distribución muestral. Asimismo, las técnicas multivariantes contemporáneas (análisis factorial, modelos multinivel, *machine learning*) utilizan la estandarización de variables —basada en la desviación estándar— como paso previo imprescindible.

## Ejemplo empírico

Supóngase una encuesta a 200 estudiantes universitarios sobre las horas semanales dedicadas al estudio. Los resultados arrojan una media de 15 horas y una desviación estándar de 4 horas. Si la distribución es aproximadamente normal:

- El 68 % de los estudiantes estudia entre 11 y 19 horas (15 ± 4).
- El 95 % estudia entre 7 y 23 horas (15 ± 8).
- Un estudiante que declara 25 horas obtiene un *z-score* de (25 − 15)/4 = 2,5, situándose 2,5 desviaciones estándar por encima de la media, un valor que solo el 0,6 % de la población alcanzaría.

Este tipo de análisis permite a los investigadores identificar patrones atípicos y evaluar la heterogeneidad del fenómeno estudiado.

## Véase también

- [[varianza]]
- [[media-aritmetica]]
- [[estadistica-descriptiva]]
- [[error-muestral]]
- [[nivel-de-confianza]]
- [[distribucion-normal]]
- [[coeficiente-de-variacion]]

## Fuentes

- Borge Bravo, R. y Padró-Solanet i Grau, A. *Metodología de las ciencias sociales*, Módulo 3: Análisis estadístico de datos (UOC, 2026-S1).
- Pearson, K. (1894). "On the dissection of asymmetrical frequency curves". *Philosophical Transactions of the Royal Society A*, 185, 71-110.
- «Desviación típica». *Wikipedia, la enciclopedia libre*. Consultado el 13 de julio de 2025.
