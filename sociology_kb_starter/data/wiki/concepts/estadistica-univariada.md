---
id: estadistica-univariada
title: Estadística univariada
note_type: concept
semester: 2026-S1
course: "Metodologia de las ciencias sociales"
related_concepts:
  - estadistica-descriptiva
  - estadistica-multivariada
  - media-aritmetica
  - mediana
  - varianza
  - desviacion-estandar
  - niveles-de-medicion
  - moda
tags:
  - estadística
  - análisis-cuantitativo
  - metodología
  - descripción-de-datos
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\la-investigacion-cuantitativa.md
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\modulo-3.md
updated_at: '2025-07-13'
---

## Definición

La **estadística univariada** (o análisis univariante) es la rama de la [[estadistica-descriptiva]] que examina la distribución de una sola variable a la vez. Su objetivo es resumir, organizar y describir las características fundamentales de un conjunto de observaciones referidas a un único atributo, sin considerar relaciones con otras variables. El término proviene del latín *uni-* (uno) y *variata* (variable): datos que consisten en observaciones sobre una única característica. En la práctica de la investigación social, la estadística univariada constituye el primer paso obligado del análisis de datos: antes de explorar asociaciones causales o correlacionales, el investigador debe conocer cómo se comporta cada variable por separado —su tendencia central, su dispersión y la forma de su distribución.

## Origen y contexto histórico

Las raíces del análisis univariado se remontan a la «aritmética política» de los siglos XVII y XVIII, cuando autores como John Graunt y William Petty comenzaron a sistematizar datos demográficos mediante tablas de frecuencias y promedios. La formalización de las medidas de tendencia central y dispersión se consolidó en el siglo XIX con los trabajos de Adolphe Quetelet, quien aplicó la curva normal a datos sociales, y de Francis Galton, que popularizó el uso de la mediana y los percentiles. En el siglo XX, la estadística univariada se integró plenamente en las ciencias sociales a través de manuales metodológicos y del desarrollo de software estadístico (SPSS, Stata, R), convirtiéndose en herramienta estándar de la encuesta social, el censo y la investigación experimental.

## Desarrollo teórico

El análisis univariado se estructura en torno a tres ejes descriptivos, cuya aplicabilidad depende del [[niveles-de-medicion|nivel de medición]] de la variable analizada:

**Medidas de tendencia central.** Permiten identificar el valor más representativo del conjunto de datos. La [[media-aritmetica]] (promedio) es la más utilizada para variables de intervalo y razón, pero resulta sensible a valores extremos (*outliers*). La [[mediana]] —el valor que divide la distribución en dos mitades iguales— es preferible cuando los datos presentan asimetría marcada. La [[moda]] —el valor con mayor frecuencia— es la única medida aplicable a variables nominales. No existe un indicador universalmente superior: la elección depende de la escala de medición y de la forma de la distribución.

**Medidas de dispersión.** Cuantifican la variabilidad de los datos en torno al valor central. El rango (diferencia entre el valor máximo y el mínimo) ofrece una primera aproximación. La [[varianza]] mide la dispersión promedio de las observaciones respecto de la media elevada al cuadrado, mientras que la [[desviacion-estandar]] (desviación típica) —su raíz cuadrada— devuelve la dispersión a las unidades originales de la variable, facilitando la interpretación. Para distribuciones asimétricas u ordinales, el rango intercuartílico resulta más robusto.

**Forma de la distribución.** La asimetría (*skewness*) indica si los datos se concentran más hacia un lado de la media, y la curtosis (*kurtosis*) mide el grado de apuntamiento de la distribución. Estas propiedades son relevantes porque muchas técnicas inferenciales posteriores asumen distribuciones simétricas o normales.

Además de las medidas numéricas, el análisis univariado emplea **representaciones gráficas**: tablas de frecuencias (absolutas, relativas, acumuladas), histogramas, diagramas de barras, gráficos de sectores y diagramas de caja (*box plots*). Estos instrumentos visuales permiten detectar rápidamente patrones, valores atípicos y la forma general de la distribución.

## Relación con otros conceptos

La estadística univariada se sitúa dentro de la [[estadistica-descriptiva]] como su modalidad más elemental. Mientras el análisis univariado describe una variable aislada, la [[estadistica-multivariada]] examina relaciones entre dos o más variables (asociación, correlación, regresión). En la estructura del análisis cuantitativo, ambos niveles se articulan secuencialmente: toda exploración multivariada presupone una descripción univariada previa. A su vez, la estadística descriptiva se distingue de la [[estadistica-inferencial]], que extrapola los hallazgos de una muestra a la población mediante modelos probabilísticos.

El tipo de análisis univariado aplicable depende directamente de los [[niveles-de-medicion]]: para variables nominales solo cabe calcular la [[moda]] y tablas de frecuencias; para ordinales se añade la [[mediana]]; y para variables de intervalo o razón se dispone además de la [[media-aritmetica]], la [[varianza]] y la [[desviacion-estandar]]. Esta correspondencia entre escala y estadístico es un principio fundamental del análisis cuantitativo.

## Debates y críticas

La principal limitación reconocida del análisis univariado es su incapacidad para captar relaciones entre variables. Un investigador que se limite a describir distribuciones aisladas corre el riesgo de omitir asociaciones relevantes o de interpretar erróneamente los datos: la llamada **paradoja de Simpson** muestra cómo tendencias que aparecen en la descripción univariada pueden invertirse cuando se introducen variables de control. En ciencias sociales, donde los fenómenos son inherentemente multidimensionales, la estadística univariada es necesaria pero insuficiente por sí sola. 

Otra crítica frecuente señala la dependencia excesiva del promedio como resumen de la distribución, ocultando heterogeneidades internas. Dos conjuntos de datos con la misma media pueden tener dispersiones radicalmente distintas. Por ello, la buena práctica estadística exige reportar siempre medidas de tendencia central *y* de dispersión conjuntamente.

## Vigencia contemporánea

En la investigación social actual, la estadística univariada conserva plena vigencia como fase exploratoria inicial. Los análisis descriptivos univariados son obligatorios en informes de encuestas (CIS, Eurobarómetro, Latinobarómetro), censos y estudios de mercado. La proliferación de grandes bases de datos (*big data*) y el análisis exploratorio de datos (*Exploratory Data Analysis*, EDA) han revitalizado las técnicas gráficas univariadas: histogramas interactivos, diagramas de densidad y *box plots* comparativos son herramientas cotidianas en entornos como R, Python y Tableau. En el marco de la sociología cuantitativa, la descripción univariada sigue siendo el requisito previo indispensable de cualquier modelización inferencial.

## Ejemplo empírico

En una encuesta sobre condiciones laborales aplicada a 500 trabajadores, el investigador comienza con un análisis univariado de la variable «ingreso mensual en euros». Construye una tabla de frecuencias agrupada por intervalos de ingreso, calcula la [[media-aritmetica]] (1.850 €), la [[mediana]] (1.620 €) y la [[desviacion-estandar]] (780 €). La diferencia entre media y mediana revela una distribución asimétrica positiva: un grupo reducido de altos ingresos eleva el promedio. Un histograma confirma la asimetría y un diagrama de caja identifica varios valores atípicos por encima de 4.000 €. Solo después de esta caracterización univariada, el investigador procede al análisis bivariado (cruce de ingresos con nivel educativo mediante [[tabla-de-contingencia]]) y multivariado (regresión con múltiples predictores).

## Véase también

- [[estadistica-descriptiva]]
- [[estadistica-multivariada]]
- [[estadistica-inferencial]]
- [[media-aritmetica]]
- [[mediana]]
- [[moda]]
- [[varianza]]
- [[desviacion-estandar]]
- [[niveles-de-medicion]]
- [[tabla-de-contingencia]]
- [[tecnicas-cuantitativas]]

## Fuentes

- Borge Bravo, R. y Padró-Solanet, A. «La investigación cuantitativa: encuesta, experimento y análisis estadístico», Módulo 3, *Metodología de las Ciencias Sociales*, UOC, 2026-S1.
- Corbetta, P. *Metodología y técnicas de investigación social*. Madrid: McGraw-Hill.
- Kachigan, S. K. (1986). *Statistical Analysis: An Interdisciplinary Introduction to Univariate & Multivariate Methods*. New York: Radius Press.
- «Univariate (statistics)», *Wikipedia (en)*, consultado en julio de 2025.
