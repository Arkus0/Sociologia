---
id: muestreo
title: Muestreo
note_type: concept
semester: 2026-S1
course: "Metodologia de las ciencias sociales"
related_concepts:
  - muestra
  - muestreo-aleatorio
  - muestreo-estratificado
  - muestreo-por-conglomerados
  - muestreo-polietapico
  - representatividad
  - error-muestral
tags:
  - muestreo
  - metodologia
  - estadistica
  - investigacion-cuantitativa
  - probabilidad
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\la-investigacion-cuantitativa.md
updated_at: '2025-07-13'
---

## Definición

El **muestreo** es el procedimiento mediante el cual se selecciona un subconjunto de unidades —la [[muestra]]— a partir de una población o universo de estudio, con el fin de realizar inferencias válidas sobre las características del conjunto total. En ciencias sociales constituye una operación metodológica fundamental: dado que rara vez es posible observar a todos los individuos de una población, la calidad de cualquier investigación empírica depende en gran medida de la rigurosidad con que se diseñe y ejecute el proceso de selección muestral.

Se distinguen dos grandes familias de técnicas: el **muestreo probabilístico**, en el que cada unidad tiene una probabilidad conocida y positiva de ser incluida en la muestra, y el **muestreo no probabilístico**, en el que la selección depende de criterios deliberados del investigador y no permite calcular errores de estimación con las herramientas de la teoría de probabilidades. Ambas familias sirven a lógicas de investigación distintas y poseen ventajas y limitaciones propias.

## Origen y contexto histórico

Los primeros intentos sistemáticos de seleccionar muestras representativas se remontan a las encuestas sociales del siglo XIX, pero la fundamentación teórica del muestreo probabilístico se consolidó en el siglo XX. **Jerzy Neyman** (1934) sentó las bases de la inferencia basada en el diseño muestral al demostrar las propiedades del [[muestreo-estratificado]] con asignación óptima, superando los métodos de selección intencional que predominaban hasta entonces. Su trabajo permitió calcular intervalos de confianza a partir del propio diseño de la muestra, sin necesidad de supuestos paramétricos sobre la distribución poblacional.

En la posguerra, **Leslie Kish** sistematizó la teoría y la práctica del muestreo en encuestas sociales en su obra *Survey Sampling* (1965), que se convirtió en referencia canónica para sociólogos, demógrafos y politólogos. Kish formalizó los diseños complejos —estratificados, por conglomerados y polietápicos— que las grandes encuestas nacionales necesitaban para cubrir poblaciones extensas con recursos limitados. En la tradición cualitativa, **Barney Glaser y Anselm Strauss** (1967) propusieron el *muestreo teórico* dentro de la Grounded Theory, un enfoque no probabilístico en el que la selección de casos se guía por la necesidad de saturar categorías analíticas emergentes.

## Desarrollo teórico

### Muestreo probabilístico

El principio rector del muestreo probabilístico es que toda unidad de la población tenga una probabilidad conocida y no nula de ser seleccionada. Ello permite aplicar la teoría de probabilidades para estimar parámetros poblacionales y cuantificar el [[error-muestral]]. Sus principales modalidades son:

- **[[muestreo-aleatorio|Muestreo aleatorio simple]]**: cada individuo tiene la misma probabilidad de selección. Requiere un *marco muestral* completo —un listado exhaustivo de la población— y resulta viable en poblaciones pequeñas o bien registradas.
- **Muestreo sistemático**: se selecciona un individuo de cada *k* elementos (donde *k* = N/n, el coeficiente de elevación). Es operativamente más sencillo que el aleatorio simple, pero puede introducir sesgos si la lista presenta periodicidades.
- **[[muestreo-estratificado|Muestreo estratificado]]**: la población se divide en estratos internamente homogéneos y externamente heterogéneos; dentro de cada estrato se extrae una muestra aleatoria. Neyman demostró que la asignación óptima del tamaño muestral a cada estrato minimiza la varianza del estimador global. La asignación puede ser proporcional al tamaño del estrato o bien óptima, asignando más casos a los estratos de mayor variabilidad.
- **[[muestreo-por-conglomerados|Muestreo por conglomerados]]**: la unidad de selección primaria es un grupo natural (barrio, escuela, hospital) que se supone internamente heterogéneo y representativo de la población. Se seleccionan algunos conglomerados y se estudian todos o parte de sus miembros. Es la opción indicada cuando no se dispone de un listado individual de la población.
- **[[muestreo-polietapico|Muestreo polietápico]]**: combina sucesivas etapas de selección —estratificación, conglomerados, cuotas— en un diseño de embudo. Las grandes encuestas nacionales (e.g., el Barómetro del CIS en España) utilizan diseños polietápicos: comunidad autónoma → municipio → sección censal → ruta aleatoria → vivienda → cuotas de sexo, edad y situación laboral.

El **tamaño de la muestra** depende de la variabilidad de la población, el nivel de confianza deseado, el margen de error aceptable y, en menor medida, el tamaño de la población (irrelevante cuando N > 100 000). Para poblaciones infinitas, la fórmula básica es: n = Z² · p · q / ε².

### Muestreo no probabilístico

Cuando el marco muestral es inexistente, la población es de difícil acceso o la investigación persigue profundidad analítica antes que [[representatividad]] estadística, se recurre a técnicas no probabilísticas:

- **Muestreo por cuotas**: se fijan proporciones según variables de distribución conocida (género, edad, clase social) y el entrevistador selecciona libremente dentro de cada cuota. Es la técnica más frecuente en sondeos de opinión y estudios de mercado.
- **Muestreo de bola de nieve**: los primeros informantes sirven como puerta de entrada a otros con características análogas. Resulta indicado para poblaciones clandestinas, minoritarias o dispersas (e.g., usuarios de drogas, migrantes indocumentados).
- **Muestreo intencional o por decisión razonada**: el investigador selecciona casos en función de sus características relevantes para la pregunta de investigación.
- **Muestreo teórico** (Glaser y Strauss, 1967): la selección es guiada por las categorías emergentes del análisis; nuevos casos se incorporan hasta alcanzar la *saturación teórica*, es decir, hasta que nuevos datos dejan de aportar información adicional.
- **Muestreo por conveniencia**: se seleccionan las unidades más accesibles. Es el menos riguroso, pero puede resultar admisible en estudios exploratorios o piloto.

## Relación con otros conceptos

El muestreo se articula con la noción de [[muestra]] como producto del proceso de selección, y con la de [[representatividad]] como criterio de calidad de dicha selección. El [[error-muestral]] cuantifica la discrepancia esperable entre los estimadores muestrales y los parámetros poblacionales; solo es calculable en diseños probabilísticos. En la práctica de la [[encuesta]], el muestreo constituye uno de los tres pilares —junto con el [[cuestionario]] y el tratamiento estadístico— que determinan la validez de los resultados. El muestreo también se conecta con la [[fiabilidad]] de las mediciones: un diseño muestral deficiente compromete la reproducibilidad de los hallazgos.

## Debates y críticas

Un debate clásico opone la tradición probabilística —que privilegia la representatividad estadística y la generalización— a los enfoques cualitativos, que priorizan la profundidad y la relevancia teórica de los casos. Kish (1965) sostenía que solo el muestreo probabilístico permite inferencias legítimas; en contraste, autores como **Michael Patton** (2002) defienden que el muestreo intencional puede producir conocimiento más rico cuando la pregunta de investigación exige comprensión en profundidad.

Una crítica contemporánea relevante proviene de **Joseph Henrich, Steven Heine y Ara Norenzayan** (2010), quienes señalaron que la mayor parte de la investigación en ciencias sociales y del comportamiento se basa en muestras de poblaciones WEIRD (*Western, Educated, Industrialized, Rich, Democratic*), lo que compromete gravemente la generalización de resultados a la humanidad en su conjunto. Esta crítica no se dirige al muestreo dentro de una población, sino a la selección sesgada de las poblaciones mismas que se estudian.

Otra tensión permanente se refiere al *marco muestral*: la distancia entre la población objetivo y la población efectivamente muestreada —debida a registros incompletos, tasas de no respuesta o exclusiones sistemáticas— introduce sesgos que ningún diseño probabilístico puede corregir por sí solo.

## Vigencia contemporánea

El muestreo permanece en el centro de la investigación social contemporánea, aunque enfrenta nuevos desafíos. La caída de las tasas de respuesta en encuestas telefónicas y presenciales ha impulsado el desarrollo de métodos mixtos y de muestreo en entornos digitales (encuestas online, datos de redes sociales), donde los marcos muestrales son difusos. Técnicas como el *respondent-driven sampling* (Heckathorn, 1997) combinan la lógica de bola de nieve con correcciones probabilísticas para poblaciones ocultas. El diseño de muestras para Big Data y el debate sobre la validez inferencial de datos no probabilísticos masivos constituyen fronteras actuales de la disciplina.

## Ejemplo empírico

El **Barómetro del Centro de Investigaciones Sociológicas (CIS)** ilustra un diseño de [[muestreo-polietapico]] estratificado aplicado a la investigación social. Se administra mensualmente a una muestra de aproximadamente 2 500 individuos en todo el territorio español. El diseño procede en varias etapas: primero se estratifica por comunidad autónoma y tamaño de municipio; luego se seleccionan aleatoriamente secciones censales (conglomerados); dentro de cada sección se traza una ruta aleatoria para seleccionar viviendas; finalmente, se aplican cuotas de sexo, edad y situación laboral para determinar qué persona del hogar será entrevistada. Este diseño polietápico permite obtener estimaciones con un margen de error de ±2 % para un nivel de confianza del 95,5 %, combinando la eficiencia de la estratificación con la operatividad del muestreo por conglomerados.

## Véase también

- [[muestra]]
- [[muestreo-aleatorio]]
- [[muestreo-estratificado]]
- [[muestreo-por-conglomerados]]
- [[muestreo-polietapico]]
- [[representatividad]]
- [[error-muestral]]
- [[encuesta]]
- [[nivel-de-confianza]]
- [[investigacion-cuantitativa]]

## Fuentes

- Kish, L. (1965). *Survey Sampling*. Wiley.
- Neyman, J. (1934). On the Two Different Aspects of the Representative Method. *Journal of the Royal Statistical Society*, 97(4), 558–625.
- Glaser, B. G. y Strauss, A. L. (1967). *The Discovery of Grounded Theory*. Aldine.
- Cochran, W. G. (1977). *Sampling Techniques* (3.ª ed.). Wiley.
- Henrich, J., Heine, S. J. y Norenzayan, A. (2010). The Weirdest People in the World? *Behavioral and Brain Sciences*, 33(2-3), 61–83.
- Patton, M. Q. (2002). *Qualitative Research and Evaluation Methods* (3.ª ed.). Sage.
- Heckathorn, D. D. (1997). Respondent-Driven Sampling. *Social Problems*, 44(2), 174–199.
- Módulo 3, Metodología de las Ciencias Sociales (UOC), 2026-S1.
