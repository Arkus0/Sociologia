---
id: muestreo-polietapico
title: Muestreo polietápico
note_type: concept
semester: 2026-S1
course: "Metodologia de las ciencias sociales"
related_concepts:
  - muestreo
  - muestreo-por-conglomerados
  - muestreo-estratificado
  - encuesta
  - representatividad
  - error-muestral
  - nivel-de-confianza
tags:
  - metodología
  - muestreo
  - investigación-cuantitativa
  - diseño-muestral
  - CIS
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\modulo-3.md
updated_at: "2025-07-13"
---

## Definición

El **muestreo polietápico** (*multi-stage sampling*) es un procedimiento de selección muestral probabilístico que opera en etapas sucesivas, empleando unidades de muestreo progresivamente más pequeñas en cada fase. En lugar de extraer directamente individuos de un marco muestral completo —operación a menudo impracticable en poblaciones extensas y dispersas—, el investigador selecciona primero agregados grandes (*unidades primarias de muestreo*, UPM o *Primary Sampling Units*, PSU), después subunidades dentro de las UPM seleccionadas (*unidades secundarias de muestreo*, USM o SSU), y así sucesivamente hasta alcanzar las unidades finales de observación. Cada etapa puede aplicar un tipo de [[muestreo]] distinto —estratificado, por conglomerados, aleatorio simple o sistemático—, de modo que el diseño resultante combina las ventajas de varios métodos en un esquema integrado.

Formalmente, si la población se divide en $M$ unidades primarias, de las cuales se seleccionan $m$, y dentro de cada UPM seleccionada se eligen $n_i$ unidades secundarias, la probabilidad de inclusión de un individuo cualquiera es el producto de las probabilidades de selección en cada etapa. Este principio multiplicativo exige el uso de ponderaciones y estimadores específicos (como el estimador de Horvitz-Thompson) para obtener inferencias insesgadas.

## Origen y contexto histórico

Los fundamentos del muestreo por etapas se remontan a los debates sobre la representatividad estadística de la primera mitad del siglo XX. En la conferencia del Instituto Internacional de Estadística de 1925, **Jerzy Neyman** sentó las bases del muestreo probabilístico al demostrar que la selección aleatoria permitía cuantificar el error de estimación. Sin embargo, fue la necesidad práctica de realizar grandes encuestas nacionales —censos parciales, estudios de empleo, encuestas electorales— lo que impulsó el desarrollo de diseños por etapas.

En las décadas de 1940 y 1950, organismos como la *U.S. Census Bureau* y la *Survey Research Center* de la Universidad de Míchigan adoptaron diseños polietápicos para sus encuestas continuas. **Leslie Kish**, en su obra canónica *Survey Sampling* (1965), formalizó la teoría de los diseños complejos —estratificados, por conglomerados y polietápicos— y proporcionó las herramientas analíticas necesarias para calcular varianzas y efectos de diseño (*design effects*, DEFF). En España, el Centro de Investigaciones Sociológicas (CIS) adoptó tempranamente estos diseños para sus barómetros de opinión pública, consolidando el muestreo polietápico como estándar de la investigación social española.

## Desarrollo teórico

El diseño polietápico se estructura típicamente en las siguientes fases:

1. **Primera etapa – Selección de UPM**: se estratifica la población según criterios geográficos o administrativos (comunidades autónomas, provincias) y se seleccionan conglomerados (municipios, secciones censales). La selección suele realizarse con **probabilidad proporcional al tamaño** (*Probability Proportional to Size*, PPS), de modo que las unidades más pobladas tienen mayor probabilidad de ser incluidas, garantizando la [[representatividad]] de la muestra.

2. **Segunda etapa – Selección de USM**: dentro de cada UPM seleccionada, se eligen subunidades (secciones censales, manzanas, rutas). Esta selección puede ser aleatoria simple o sistemática.

3. **Tercera etapa (y siguientes) – Selección de unidades finales**: se seleccionan viviendas dentro de las secciones y, finalmente, individuos dentro de las viviendas. En la práctica española, la selección del individuo final se realiza frecuentemente mediante **cuotas** de sexo, edad y situación laboral, lo que introduce un componente no estrictamente probabilístico en la última etapa.

Un concepto central en los diseños polietápicos es el **efecto de diseño** (DEFF), definido como la razón entre la varianza del estimador bajo el diseño complejo y la varianza que se obtendría con un [[muestreo]] aleatorio simple del mismo tamaño. Valores de DEFF superiores a 1 indican que el diseño complejo es menos eficiente que el muestreo aleatorio simple, lo cual es habitual en diseños por conglomerados debido a la homogeneidad intragrupo. La **afijación proporcional** —distribución de entrevistas proporcional al peso poblacional de cada estrato— y la estratificación contribuyen a reducir el DEFF.

## Relación con otros conceptos

El muestreo polietápico se sitúa en la intersección de varios procedimientos muestrales. Del [[muestreo-estratificado]] hereda la división de la población en subgrupos homogéneos internamente y heterogéneos entre sí, lo que reduce la varianza de los estimadores. Del [[muestreo-por-conglomerados]] toma la idea de seleccionar agrupaciones naturales de individuos (municipios, secciones censales, viviendas) en lugar de individuos aislados, lo que reduce drásticamente los costes operativos del trabajo de campo.

La relación con la [[encuesta]] es orgánica: los grandes estudios por encuesta —barómetros, encuestas electorales, encuestas de salud— recurren casi invariablemente a diseños polietápicos porque permiten cubrir territorios extensos sin necesidad de disponer de un listado exhaustivo de todos los miembros de la población. El concepto de [[representatividad]] adquiere aquí una dimensión operativa concreta: el diseño polietápico es representativo en la medida en que cada individuo de la población tiene una probabilidad conocida y positiva de ser seleccionado, y las ponderaciones corrigen las desigualdades en dichas probabilidades.

Asimismo, el [[error-muestral]] en diseños polietápicos es más complejo de calcular que en el muestreo aleatorio simple. Las fórmulas estándar ($\varepsilon = Z \sqrt{p \cdot q / n}$) solo ofrecen una aproximación; el cálculo riguroso requiere considerar la estructura multinivel del diseño y, habitualmente, emplear técnicas de replicación (*jackknife*, *bootstrap*) o linealización de Taylor.

## Debates y críticas

Una crítica frecuente al muestreo polietápico concierne a la **última etapa de selección por cuotas**. Si bien las primeras etapas son estrictamente probabilísticas, la selección final del individuo por cuotas de sexo, edad y situación laboral introduce un componente discrecional que, en rigor, impide calcular probabilidades exactas de inclusión. Los defensores argumentan que las cuotas, controladas demográficamente, minimizan el sesgo de no respuesta y resultan operativamente indispensables en encuestas domiciliarias presenciales.

Otro debate relevante es el de la **precisión frente al coste**. El muestreo polietápico sacrifica eficiencia estadística (DEFF > 1) a cambio de viabilidad logística. En poblaciones con alta homogeneidad intraconglomerado (*intraclass correlation* elevada), el efecto de diseño puede ser considerable, y la muestra efectiva resulta sensiblemente menor que la muestra nominal. Esto obliga a incrementar el tamaño muestral para alcanzar niveles aceptables de [[error-muestral]], típicamente ±2-3 puntos porcentuales para un nivel de confianza del 95,5 %.

Desde la perspectiva contemporánea, la creciente dificultad para realizar entrevistas presenciales domiciliarias ha llevado a cuestionar la sostenibilidad de los diseños polietápicos clásicos, impulsando la transición hacia encuestas telefónicas (CATI) y en línea (CAWI) con marcos muestrales diferentes.

## Vigencia contemporánea

El muestreo polietápico sigue siendo el diseño de referencia para las grandes encuestas presenciales nacionales. El CIS lo emplea en sus barómetros mensuales, la Encuesta de Población Activa (EPA) del INE utiliza un diseño bietápico estratificado, y organismos internacionales como Eurostat y la OMS lo aplican en encuestas transnacionales. En el ámbito académico, los paquetes estadísticos especializados —*survey* en R, *svy* en Stata— permiten incorporar la estructura del diseño complejo en el análisis, calculando errores estándar corregidos y efectos de diseño.

La combinación de muestreo polietápico con técnicas de **calibración** y **postestratificación** permite ajustar los pesos muestrales a distribuciones poblacionales conocidas (sexo, edad, comunidad autónoma), mejorando la precisión de las estimaciones sin alterar el diseño de campo.

## Ejemplo empírico

El **Barómetro mensual del CIS** constituye el caso paradigmático de muestreo polietápico en España. Según la ficha técnica del estudio n.º 2.026 (febrero 1996), el diseño se describe como «polietápico, estratificado por conglomerados, con selección de las unidades primarias (secciones) de forma aleatoria proporcional y de las unidades últimas (individuos) por rutas aleatorias y cuotas de sexo y edad». Los estratos se forman cruzando las 17 comunidades autónomas con 7 categorías de tamaño de hábitat (desde menos de 2 000 habitantes hasta más de 1 000 000). La muestra diseñada es de 2 500 [[encuesta|entrevistas]] distribuidas en 159 municipios y 48 provincias, con afijación proporcional. Para un nivel de confianza del 95,5 % (2σ) y bajo supuesto de máxima variabilidad ($p = q = 0{,}5$), el [[error-muestral]] es de ±2 puntos para el conjunto de la muestra. Este diseño permite obtener estimaciones fiables de la opinión pública española con un coste operativo asumible, cubriendo todo el territorio nacional.

## Véase también

- [[muestreo]]
- [[muestreo-estratificado]]
- [[muestreo-por-conglomerados]]
- [[encuesta]]
- [[representatividad]]
- [[error-muestral]]
- [[nivel-de-confianza]]
- [[variable-independiente]]

## Fuentes

- Kish, L. (1965). *Survey Sampling*. Nueva York: John Wiley & Sons.
- Scheafer, R. L., Mendenhall, W. y Ott, L. (1987). *Elementos de muestreo*. México: Grupo Editorial Iberoamérica.
- Material docente UOC, Módulo 3: «Muestreo» (Metodología de las ciencias sociales, 2026-S1).
- Gil Estallo, Á. «Mostreig» (págs. 1-22). Barcelona: UOC.
- Pedret, R., Sagnier, L., García, I. y Morell, S. «El muestreo». En: *Técnicas cuantitativas para la obtención de información* (págs. 33-53). Barcelona: UOC.
- Centro de Investigaciones Sociológicas (CIS). Fichas técnicas de los Barómetros mensuales.
