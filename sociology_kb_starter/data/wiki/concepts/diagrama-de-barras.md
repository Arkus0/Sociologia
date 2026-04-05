---
id: diagrama-de-barras
title: Diagrama de barras
note_type: concept
semester: 2026-S1
course: "Metodologia de las ciencias sociales"
related_concepts:
  - representacion-visual-de-datos
  - estadistica-descriptiva
  - diagrama-de-lineas
  - niveles-de-medicion
  - tabla-de-contingencia
  - histograma
  - variable-cualitativa
tags:
  - visualización
  - estadística
  - metodología-cuantitativa
  - gráficos
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\modulo-3.md
updated_at: '2025-07-13'
---

## Definición

El **diagrama de barras** —también denominado gráfico de barras o gráfico de columnas— es una forma de [[representacion-visual-de-datos]] que emplea barras rectangulares cuya longitud es proporcional a los valores que representan. Constituye una de las herramientas más elementales y difundidas de la [[estadistica-descriptiva]], utilizada para comparar frecuencias o magnitudes entre categorías de una variable cualitativa o para contrastar una misma variable en distintos momentos temporales. Las barras pueden disponerse en orientación vertical (columnas) u horizontal, y se separan entre sí por espacios iguales que subrayan la naturaleza discreta de las categorías.

En el contexto de la investigación social, el diagrama de barras permite visualizar de manera inmediata la distribución de respuestas a una pregunta de encuesta, la composición de una muestra según variables sociológicamente relevantes —sexo, nivel educativo, clase social— o la evolución de indicadores a lo largo de períodos electorales.

## Origen y contexto histórico

El origen del diagrama de barras se atribuye convencionalmente al ingeniero y economista político escocés **William Playfair**, quien en su obra *The Commercial and Political Atlas* (1786) introdujo las primeras representaciones gráficas de series temporales mediante barras y líneas. Playfair buscaba hacer accesibles datos comerciales y fiscales del gobierno británico a un público no especializado, y su innovación resultó decisiva para la consolidación de la estadística gráfica como disciplina.

No obstante, existen evidencias de usos rudimentarios de barras proporcionales en registros contables y cartográficos que se remontan al menos tres siglos antes de Playfair. La sistematización del recurso gráfico se consolidó en el siglo XIX con los trabajos de **Florence Nightingale** —quien popularizó los diagramas polares durante la guerra de Crimea— y de **Charles Joseph Minard**, pionero de la infografía estadística. En las ciencias sociales, la adopción masiva del diagrama de barras acompañó la expansión de los censos nacionales y las primeras encuestas de opinión en el siglo XX, cuando se hizo imprescindible comunicar resultados cuantitativos a audiencias amplias.

## Desarrollo teórico

Desde la perspectiva metodológica, el diagrama de barras se inscribe en la tradición de la estadística univariada y, más concretamente, en el análisis de distribuciones de frecuencia de variables medidas en [[niveles-de-medicion]] nominal u ordinal. A diferencia del [[histograma]], que representa variables continuas y emplea barras contiguas, el diagrama de barras mantiene espacios entre las barras para señalar que cada categoría es un valor discreto.

Las variantes más habituales son:

- **Barras verticales (columnas):** la disposición más frecuente; cada categoría ocupa un lugar en el eje de abscisas y la altura de la barra indica la frecuencia o el valor.
- **Barras horizontales:** útil cuando las etiquetas de las categorías son extensas o cuando se desea facilitar la comparación ordinal de arriba a abajo. Un caso particular es el *gráfico de eje central* o pirámide de población, muy utilizado en demografía.
- **Barras agrupadas:** yuxtaponen dos o más barras por categoría para comparar subgrupos —por ejemplo, resultados electorales de dos años distintos—.
- **Barras apiladas (superpuestas):** descomponen cada barra en segmentos proporcionales a subcategorías, lo que permite observar tanto el total como la composición interna.

Edward **Tufte** (1983) formuló el principio de la *data-ink ratio* (razón datos-tinta), según el cual un gráfico eficaz maximiza la proporción de tinta dedicada a representar datos reales y minimiza los elementos decorativos superfluos. Aplicado al diagrama de barras, este principio desaconseja sombras, efectos tridimensionales y tramas excesivas que distorsionan la percepción de las magnitudes.

## Relación con otros conceptos

El diagrama de barras mantiene vínculos estrechos con múltiples nociones de la metodología cuantitativa:

- **[[estadistica-descriptiva]]:** constituye una de sus técnicas de resumen visual más básicas, junto con las medidas de tendencia central y dispersión.
- **[[tabla-de-contingencia]]:** las frecuencias cruzadas de dos variables cualitativas pueden representarse mediante barras agrupadas o apiladas, ofreciendo un complemento gráfico a la tabla numérica.
- **[[diagrama-de-lineas]]:** mientras el diagrama de barras subraya comparaciones entre categorías discretas, el diagrama de líneas resalta tendencias continuas en el tiempo; ambos suelen combinarse en informes de investigación.
- **[[niveles-de-medicion]]:** la elección del tipo de gráfico depende del nivel de medición de la variable; el diagrama de barras es apropiado para escalas nominales y ordinales.
- **[[representacion-visual-de-datos]]:** marco general que integra diagramas de barras, diagramas circulares, diagramas de dispersión y otras formas de codificación visual de información cuantitativa.

## Debates y críticas

Un debate recurrente en la literatura metodológica concierne a la capacidad del diagrama de barras para inducir interpretaciones erróneas. La manipulación del eje de ordenadas —por ejemplo, truncando la escala para que no comience en cero— puede exagerar diferencias mínimas entre categorías, un recurso frecuente en medios de comunicación y propaganda política.

Asimismo, Tufte (1983) y Cleveland (1985) han señalado que la proliferación de «chart junk» —adornos visuales innecesarios— distorsiona la lectura precisa de los datos. En el ámbito de la sociología electoral, Few (2004) advierte sobre el abuso de barras tridimensionales que dificultan la comparación exacta de longitudes.

Otro punto de discusión atañe a la pertinencia del diagrama de barras frente a alternativas como el *dot plot* (diagrama de puntos) propuesto por Cleveland, que permite comparaciones más precisas al eliminar el área rectangular. No obstante, la familiaridad universal del diagrama de barras sigue haciéndolo preferible en contextos de comunicación pública de resultados sociológicos.

## Vigencia contemporánea

En la era de los datos masivos y la visualización interactiva, el diagrama de barras conserva plena vigencia como recurso pedagógico y analítico. Herramientas como R (ggplot2), Python (matplotlib, seaborn) y plataformas de *business intelligence* (Tableau, Power BI) generan diagramas de barras con capacidades interactivas —filtrado dinámico, actualización en tiempo real— que amplían su potencial exploratorio.

En la sociología contemporánea, los diagramas de barras se emplean sistemáticamente en la presentación de resultados de encuestas (CIS, Eurobarómetro, Latinobarómetro), informes de organismos internacionales y publicaciones académicas. Los estudios sobre alfabetización estadística subrayan que el diagrama de barras es el tipo de gráfico que los estudiantes comprenden más tempranamente, lo que explica su presencia dominante —cercana al 50 %— en los libros de texto de enseñanza primaria en España.

## Ejemplo empírico

Supóngase una encuesta realizada a 400 estudiantes universitarios sobre su posición ideológica autorreportada (escala nominal: izquierda, centro-izquierda, centro, centro-derecha, derecha). Un diagrama de barras verticales con las cinco categorías en el eje horizontal y las frecuencias absolutas en el eje vertical permite visualizar inmediatamente qué posición concentra más respuestas, detectar asimetrías en la distribución y comparar resultados con los de una encuesta anterior mediante barras agrupadas. Si además se desea desagregar por sexo, un diagrama de barras apiladas mostraría la composición interna de cada categoría ideológica.

## Véase también

- [[representacion-visual-de-datos]]
- [[estadistica-descriptiva]]
- [[diagrama-de-lineas]]
- [[niveles-de-medicion]]
- [[tabla-de-contingencia]]
- [[histograma]]
- [[variable-cualitativa]]

## Fuentes

- Playfair, W. (1786). *The Commercial and Political Atlas*. Londres.
- Tufte, E. R. (1983). *The Visual Display of Quantitative Information*. Cheshire: Graphics Press.
- Cleveland, W. S. (1985). *The Elements of Graphing Data*. Monterey: Wadsworth.
- Few, S. (2004). *Show Me the Numbers: Designing Tables and Graphs to Enlighten*. Oakland: Analytics Press.
- Borge Bravo, R. y Padró-Solanet, A. *La investigación cuantitativa* (Módulo 3, Metodología de las Ciencias Sociales, UOC, 2026-S1).
- García Mendoza, S. (2009). *Guía para la presentación de gráficos estadísticos*. Lima: INEI.
- «Diagrama de barras». *Wikipedia en español*. Consultado el 5 de abril de 2026.
