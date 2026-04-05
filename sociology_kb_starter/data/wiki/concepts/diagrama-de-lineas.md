---
id: diagrama-de-lineas
title: Diagrama de líneas
note_type: concept
semester: 2026-S1
course: "Metodologia de las ciencias sociales"
related_concepts:
  - representacion-visual-de-datos
  - estadistica-descriptiva
  - diagrama-de-barras
  - niveles-de-medicion
  - variable-independiente
  - tabla-de-contingencia
  - correlacion
tags:
  - Visualización de datos
  - Estadística descriptiva
  - Series temporales
  - Metodologia de las ciencias sociales
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\modulo-3.md
updated_at: '2025-07-13'
---

# Diagrama de líneas

## Definición

El **diagrama de líneas** (también denominado *gráfico de líneas* o *line chart*) es una forma de [[representacion-visual-de-datos]] que muestra la evolución de una o más variables cuantitativas a lo largo de un eje ordenado —habitualmente el tiempo— mediante puntos de datos (*markers*) conectados por segmentos rectilíneos. Cada punto representa el valor observado de la variable dependiente para un valor concreto de la [[variable-independiente]], y la línea que los une permite al lector percibir tendencias, ciclos y discontinuidades de forma inmediata. Se trata de uno de los gráficos estadísticos más utilizados en ciencias sociales, especialmente cuando el investigador desea comunicar patrones diacrónicos: tasas de desempleo, evolución electoral, curvas demográficas o indicadores de opinión pública.

En el módulo 3 de *La investigación cuantitativa* (Borge y Padró-Solanet, UOC), el diagrama de líneas se presenta como el recurso gráfico privilegiado para representar la evolución temporal de variables numéricas, diferenciándolo del [[diagrama-de-barras]] —más adecuado para comparar categorías discretas— y del gráfico de sectores —reservado para distribuciones de variables nominales—.

## Origen y contexto histórico

Los primeros gráficos de líneas conocidos se atribuyen a Francis Hauksbee, Nicolaus Samuel Cruquius y Johann Heinrich Lambert, aunque fue el ingeniero escocés **William Playfair** (1759-1823) quien los popularizó de manera decisiva. En su obra *The Commercial and Political Atlas* (1786), Playfair representó diez años de gasto de la Marina Real británica mediante una curva temporal, acompañando el gráfico de una descripción detallada que enseñaba al lector a interpretar la variación en el tiempo, dado que la forma de abstracción visual resultaba desconocida para el público de la época. Playfair es además reconocido como inventor del diagrama de barras y del gráfico de sectores, lo que lo convierte en una figura fundacional de la visualización estadística moderna.

Durante el siglo XIX, la expansión de la estadística oficial y los censos nacionales multiplicó el uso de gráficos de líneas en informes gubernamentales y publicaciones científicas. En el siglo XX, autores como Mary Eleanor Spear (*Charting Statistics*, 1952) sistematizaron las convenciones formales del gráfico de líneas, consolidando su papel como herramienta estándar de la [[estadistica-descriptiva]].

## Desarrollo teórico

Desde el punto de vista metodológico, el diagrama de líneas se inscribe en el campo de la estadística univariada y bivariada como instrumento de análisis exploratorio. Su construcción exige al menos una variable cuantitativa continua o discreta y un eje de ordenación (temporal, espacial u ordinal), lo que lo vincula directamente a los [[niveles-de-medicion]]: las variables nominales carecen de un orden inherente que justifique la unión de puntos mediante líneas.

Un aspecto teórico relevante es el **supuesto de interpolación**: al conectar puntos mediante segmentos rectos, el gráfico sugiere implícitamente una continuidad entre observaciones que puede no estar respaldada por los datos. Esta asunción resulta razonable cuando los intervalos de medición son suficientemente breves, pero puede inducir a error si los datos son escasos o la variable presenta saltos abruptos. En contextos experimentales, es habitual superponer una **línea de ajuste** (*best-fit curve*) calculada mediante regresión lineal o polinómica, que distingue la tendencia subyacente del ruido aleatorio de las observaciones.

Edward Tufte, en *The Visual Display of Quantitative Information* (1983), formalizó el principio del **data-ink ratio** (razón datos-tinta): un gráfico eficaz maximiza la proporción de tinta dedicada a representar información y minimiza los elementos decorativos superfluos (*chartjunk*). El diagrama de líneas, por su economía visual —una sola línea puede sintetizar decenas de valores—, constituye uno de los gráficos con mayor data-ink ratio cuando se diseña con sobriedad.

## Relación con otros conceptos

- **[[representacion-visual-de-datos]]**: el diagrama de líneas es una de las formas canónicas de visualización, junto con tablas, diagramas de barras y gráficos de sectores.
- **[[estadistica-descriptiva]]**: funciona como complemento gráfico de medidas de tendencia central y dispersión, revelando patrones que los estadísticos numéricos no capturan.
- **[[diagrama-de-barras]]**: mientras el diagrama de barras compara magnitudes entre categorías discretas, el de líneas enfatiza la continuidad y la dirección del cambio; la elección entre ambos depende del nivel de medición de la variable independiente.
- **[[niveles-de-medicion]]**: solo las variables ordinales o numéricas admiten un eje que justifique la conexión lineal de puntos; emplear líneas con variables nominales constituye un error gráfico frecuente.
- **[[variable-independiente]]**: en el uso convencional, la variable independiente (generalmente el tiempo) se sitúa en el eje horizontal y la dependiente en el vertical.
- **[[tabla-de-contingencia]]**: cuando la relación entre variables ya ha sido cuantificada en una tabla, el diagrama de líneas permite visualizar esa misma información de forma sintética.

## Debates y críticas

La principal crítica al diagrama de líneas concierne al ya mencionado **supuesto de interpolación**: los segmentos rectilíneos entre puntos pueden sugerir una transición gradual donde en realidad hubo discontinuidades. Algunos autores recomiendan utilizar diagramas de puntos (*dot plots*) cuando los datos son escasos o los intervalos irregulares.

Un segundo debate gira en torno a la **comparación de series múltiples**. Representar varias líneas en un mismo gráfico permite comparar tendencias, pero cuando las series poseen escalas muy diferentes o se superponen excesivamente, la legibilidad disminuye y puede inducir interpretaciones erróneas. Las prácticas recomendadas incluyen el uso de ejes secundarios con cautela, la separación en paneles (*small multiples*) y el empleo de colores accesibles a personas con daltonismo.

Finalmente, Tufte advierte contra la manipulación del eje vertical: truncar la escala —no comenzar en cero— puede exagerar visualmente variaciones menores, un recurso retórico frecuente en medios de comunicación y discursos políticos.

## Vigencia contemporánea

En la era de los macrodatos y las herramientas digitales interactivas, el diagrama de líneas mantiene una vigencia indiscutible. Plataformas como Our World in Data, Eurostat y el Banco Mundial lo emplean como formato predeterminado para series temporales socioeconómicas. Los *dashboards* interactivos permiten al usuario filtrar países, períodos y variables, enriqueciendo la exploración sin alterar la lógica gráfica subyacente. En la investigación sociológica cuantitativa, sigue siendo el recurso estándar para presentar resultados longitudinales en artículos y ponencias.

## Ejemplo empírico

Supóngase una investigación que estudia la evolución de la tasa de participación electoral en España entre 1977 y 2023. El eje horizontal representa cada elección general (variable temporal ordenada) y el eje vertical el porcentaje de participación. Al conectar los puntos se percibe una tendencia descendente desde el 78,8 % de 1982 hasta valores cercanos al 66 % en elecciones recientes, con repuntes puntuales (e.g., 2004, 2019-abril). La visualización permite identificar de un vistazo tanto la tendencia secular como las anomalías, facilitando la formulación de hipótesis sobre los factores explicativos —desafección, competitividad electoral, contexto sociopolítico— que la [[correlacion]] y la regresión cuantificarán posteriormente.

## Véase también

- [[representacion-visual-de-datos]]
- [[estadistica-descriptiva]]
- [[diagrama-de-barras]]
- [[niveles-de-medicion]]
- [[variable-independiente]]
- [[tabla-de-contingencia]]
- [[correlacion]]

## Fuentes

- Borge, R. y Padró-Solanet, A. (2026). *La investigación cuantitativa*. Módulo 3, Metodología de las ciencias sociales. Barcelona: UOC. → [[la-investigacion-cuantitativa]]
- Playfair, W. (1786). *The Commercial and Political Atlas*. Londres: Debrett.
- Spear, M. E. (1952). *Charting Statistics*. Nueva York: McGraw-Hill.
- Tufte, E. R. (1983). *The Visual Display of Quantitative Information*. Cheshire, CT: Graphics Press.
- Friendly, M. (2008). "Milestones in the history of thematic cartography, statistical graphics, and data visualization". York University.
