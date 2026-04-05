---
id: muestreo-aleatorio
title: Muestreo aleatorio
note_type: concept
semester: 2026-S1
course: "Metodologia de las ciencias sociales"
related_concepts:
  - "[[muestreo]]"
  - "[[muestra]]"
  - "[[muestreo-estratificado]]"
  - "[[muestreo-por-conglomerados]]"
  - "[[representatividad]]"
  - "[[error-muestral]]"
  - "[[nivel-de-confianza]]"
  - "[[inferencia-cientifica]]"
tags:
  - metodología
  - estadística
  - encuesta
  - probabilidad
  - muestreo
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\la-investigacion-cuantitativa.md
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\modulo-3.md
updated_at: '2025-07-13'
---

## Definición

El **muestreo aleatorio** es un procedimiento de selección muestral en el que todos los individuos de la [[poblacion|población]] tienen una **probabilidad positiva y conocida** de ser incluidos en la [[muestra]]. Esta condición —denominada *equiprobabilidad* en su variante más simple— constituye el requisito fundamental para que los resultados obtenidos en la muestra puedan generalizarse a la población mediante [[inferencia-cientifica|inferencia estadística]]. A diferencia de los procedimientos no probabilísticos (por cuotas, bola de nieve, conveniencia), el muestreo aleatorio permite calcular el [[error-muestral]] y establecer [[nivel-de-confianza|niveles de confianza]], lo que lo convierte en el estándar de la investigación cuantitativa.

En contra de una intuición ingenua, extraer una muestra aleatoria no significa emplear procedimientos laxos de selección. Al contrario: para garantizar la aleatoriedad es necesario disponer de un **marco muestral** completo —un listado exhaustivo de las unidades que componen la población— y emplear mecanismos rigurosos de selección (tablas de números aleatorios, generadores computacionales de números pseudoaleatorios).

## Origen y contexto histórico

Los fundamentos matemáticos del muestreo probabilístico se consolidaron en la primera mitad del siglo XX. Un hito decisivo fue el artículo de **Jerzy Neyman** (1934), "On the Two Different Aspects of the Representative Method", donde demostró la superioridad del muestreo aleatorio estratificado con afijación óptima frente al método de selección intencionada que defendía A. L. Bowley. La propuesta de Neyman sistematizó el cálculo de intervalos de confianza y sentó las bases de la teoría moderna del [[muestreo]].

Durante la Segunda Guerra Mundial, la necesidad de encuestas rápidas y fiables impulsó la adopción generalizada de diseños probabilísticos en agencias gubernamentales como el U.S. Census Bureau y el Government Social Survey británico. En las décadas siguientes, la difusión de las **tablas de números aleatorios** (Fisher & Yates, 1938) y, más tarde, de los **generadores computacionales** de números pseudoaleatorios democratizó el acceso a procedimientos de selección rigurosos.

## Desarrollo teórico

### Muestreo aleatorio simple (MAS)

Es la modalidad más elemental: cada unidad de la población tiene exactamente la misma probabilidad de ser seleccionada (1/*N*). Se asigna un número a cada individuo del marco muestral y se extraen *n* unidades mediante sorteo o tabla de números aleatorios. Es adecuado cuando la población es relativamente **homogénea** respecto a las variables de interés. Su principal limitación es que, con poblaciones grandes y dispersas, puede resultar logísticamente costoso y no garantizar la presencia de subgrupos minoritarios relevantes.

### Muestreo aleatorio sistemático

A partir de un listado completo de la población, se selecciona un individuo de cada *k*, donde *k* = *N*/*n* es el **coeficiente de elevación**. Se elige aleatoriamente un punto de inicio entre 1 y *k*, y luego se selecciona cada *k*-ésimo elemento. Es operativamente más sencillo que el MAS, pero puede introducir sesgos si el listado presenta periodicidades ocultas.

### Variantes complejas

Para resolver problemas de heterogeneidad poblacional y costes de acceso, se han desarrollado diseños que mantienen la aleatoriedad:

- **[[muestreo-estratificado|Muestreo aleatorio estratificado]]**: la población se divide en estratos internamente homogéneos y heterogéneos entre sí; dentro de cada estrato se extrae una muestra aleatoria simple. Reduce la varianza de los estimadores y garantiza la presencia de subgrupos relevantes.
- **[[muestreo-por-conglomerados|Muestreo por conglomerados]]**: la unidad muestral inicial no es el individuo sino una agrupación natural (escuelas, hospitales, viviendas). Los conglomerados deben ser internamente heterogéneos y homogéneos entre sí.
- **Muestreo polietápico**: combina estratificación, conglomerados y cuotas en sucesivas etapas. Es el diseño habitual de las grandes encuestas de opinión en España (comunidad autónoma → municipio → sección censal → ruta → vivienda → individuo por cuotas de edad, sexo y situación laboral).

## Relación con otros conceptos

El muestreo aleatorio es condición necesaria de la [[representatividad]]: solo si la selección es probabilística cabe hablar con rigor de una muestra representativa de la población. El concepto está estrechamente ligado al [[error-muestral]], que cuantifica la discrepancia esperable entre el estadístico muestral y el parámetro poblacional. Las fórmulas clásicas del error muestral (ε = Z·√(p·q/n) para poblaciones infinitas) presuponen un diseño aleatorio.

El **tamaño de la muestra** depende de cuatro factores interrelacionados: la variabilidad de la población, el tamaño de la población (solo relevante cuando *N* < 100.000), el [[nivel-de-confianza]] deseado y el margen de error aceptable. En la práctica, el margen de error habitual en encuestas sociales es de ±3 puntos porcentuales con un nivel de confianza del 95 % (Z = 1,96).

## Debates y críticas

La principal crítica al muestreo aleatorio es de orden **práctico**: rara vez se dispone de un marco muestral perfecto. Los censos se desactualizan, las listas telefónicas excluyen a segmentos de la población, y las encuestas *online* enfrentan problemas de autoselección. Estas limitaciones han llevado a algunos metodólogos a cuestionar la superioridad automática del muestreo probabilístico sobre el no probabilístico cuando el marco muestral es deficiente.

Un segundo debate concierne a la **tasa de respuesta**: incluso con un diseño aleatorio impecable, si la tasa de respuesta es baja y la no-respuesta no es aleatoria, la muestra final puede estar sesgada (sesgo de no respuesta). La creciente dificultad para obtener tasas de respuesta aceptables en encuestas presenciales y telefónicas ha intensificado este problema desde finales del siglo XX.

Por último, los diseños polietápicos con selección final por cuotas —muy extendidos en la práctica comercial y mediática— introducen un componente no probabilístico en la última etapa, lo que técnicamente invalida el cálculo estándar del error muestral, aunque se reporte como si fuera plenamente aleatorio.

## Vigencia contemporánea

A pesar de estas limitaciones, el muestreo aleatorio sigue siendo el **estándar normativo** de la investigación social empírica. Los avances en registros administrativos digitalizados, padrones continuos y bases de datos integradas han mejorado la calidad de los marcos muestrales disponibles. Paralelamente, la generación de números aleatorios por computadora ha eliminado las dificultades operativas de la selección aleatoria.

En el contexto de las encuestas *online* y del *Big Data*, emergen enfoques híbridos que combinan muestras probabilísticas de referencia con paneles de acceso (*opt-in*) y técnicas de ponderación y calibración (propensity score matching, raking) para aproximar la representatividad de los diseños probabilísticos clásicos.

## Ejemplo empírico

El **Centro de Investigaciones Sociológicas (CIS)** realiza sus barómetros mensuales mediante un diseño polietápico, estratificado por comunidad autónoma y tamaño de municipio, con selección aleatoria de secciones censales y rutas, y selección final del individuo por cuotas de sexo y edad. Para una muestra típica de 2.500 entrevistas, el error muestral teórico —en el supuesto de muestreo aleatorio simple— es de ±2,0 puntos porcentuales con un nivel de confianza del 95,5 % (Z = 2). Este dato ilustra tanto la utilidad práctica de las fórmulas del muestreo aleatorio como la distancia entre el modelo teórico simple y el diseño real.

## Véase también

- [[muestreo]]
- [[muestra]]
- [[muestreo-estratificado]]
- [[muestreo-por-conglomerados]]
- [[representatividad]]
- [[error-muestral]]
- [[nivel-de-confianza]]
- [[encuesta]]
- [[inferencia-cientifica]]

## Fuentes

- [[la-investigacion-cuantitativa]] — Borge Bravo, R. & Padró-Solanet, A. *La investigación cuantitativa: encuesta, experimento y análisis estadístico*. Módulo 3, Metodología de las Ciencias Sociales, UOC.
- [[modulo-3]] — Material docente, Metodología de las Ciencias Sociales, 2026-S1.
- Neyman, J. (1934). "On the Two Different Aspects of the Representative Method: The Method of Stratified Sampling and the Method of Purposive Selection". *Journal of the Royal Statistical Society*, 97(4), 558–625.
- Scheafer, R. L.; Mendenhall, W.; Ott, L. (1987). *Elementos de muestreo*. México: Grupo Editorial Iberoamérica.
- Kish, L. (1965). *Survey Sampling*. New York: Wiley.
