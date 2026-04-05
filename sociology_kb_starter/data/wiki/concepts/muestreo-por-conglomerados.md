---
id: muestreo-por-conglomerados
title: Muestreo por conglomerados
note_type: concept
semester: 2026-S1
course: "Metodologia de las ciencias sociales"
related_concepts:
  - muestreo
  - muestreo-aleatorio
  - muestreo-polietapico
  - muestreo-estratificado
  - error-muestral
  - representatividad
  - muestra
tags:
  - metodología
  - muestreo
  - investigación-cuantitativa
  - diseño-muestral
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\la-investigacion-cuantitativa.md
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\modulo-3.md
updated_at: '2025-07-13'
---

## Definición

El **muestreo por conglomerados** (*cluster sampling*) es una técnica de [[muestreo]] probabilístico en la que la unidad primaria de selección no es el individuo, sino un grupo natural preexistente —denominado *conglomerado* o *cluster*— al que pertenecen los sujetos de la población objetivo. Ejemplos típicos de conglomerados son hospitales, escuelas, viviendas, empresas, secciones censales o barrios. Una vez seleccionada aleatoriamente una muestra de conglomerados, se estudian todos los elementos que los integran (muestreo en una etapa) o bien se extrae una submuestra dentro de cada conglomerado seleccionado (muestreo en dos o más etapas). La técnica constituye una alternativa operativa al [[muestreo-aleatorio|muestreo aleatorio simple]] cuando no se dispone de un listado completo de los individuos de la población o cuando los costos de desplazamiento hacen inviable la dispersión geográfica que implica la selección puramente aleatoria.

## Origen y contexto histórico

Los fundamentos del muestreo por conglomerados se remontan a los trabajos pioneros de **Morris Hansen, William Hurwitz y William Madow**, quienes en *Sample Survey Methods and Theory* (1953) sistematizaron los procedimientos de selección en etapas aplicados a los censos y encuestas del Bureau of the Census de Estados Unidos. Poco después, **Leslie Kish** consolidó la teoría del muestreo aplicada a las ciencias sociales en su obra canónica *Survey Sampling* (1965), donde formalizó los diseños complejos —estratificados, por conglomerados y polietápicos— que las grandes encuestas nacionales necesitaban para cubrir poblaciones extensas con recursos limitados. En el ámbito hispanohablante, los barómetros del Centro de Investigaciones Sociológicas (CIS) adoptaron tempranamente diseños [[muestreo-polietapico|polietápicos]] que combinan conglomerados geográficos con cuotas finales de edad, sexo y situación laboral.

## Desarrollo teórico

### Lógica del diseño

El principio rector es que cada conglomerado debe ser internamente **heterogéneo** (reproducir en pequeña escala la variabilidad de la población) y que los conglomerados deben ser **homogéneos entre sí**. Esta condición es exactamente la inversa de la que rige el [[muestreo-estratificado]]: en la estratificación se buscan estratos internamente homogéneos y heterogéneos entre sí para reducir la varianza de los estimadores; en el muestreo por conglomerados, la ganancia no es de precisión sino de economía operativa.

### Modalidades

- **Una etapa**: se selecciona aleatoriamente un subconjunto de conglomerados y se encuesta a *todos* los individuos de cada conglomerado elegido.
- **Dos etapas**: se seleccionan conglomerados y, dentro de cada uno, se extrae una [[muestra]] aleatoria de individuos.
- **Múltiples etapas (polietápico)**: se aplican sucesivas selecciones aleatorias en niveles jerárquicos —por ejemplo, comunidad autónoma → municipio → sección censal → vivienda → individuo—, procedimiento habitual en las grandes [[encuesta]]s de opinión.

### Efecto de diseño e ICC

El **efecto de diseño** (*design effect*, DEFF) cuantifica la pérdida de precisión del muestreo por conglomerados respecto al muestreo aleatorio simple del mismo tamaño. Se define como la razón entre la varianza del estimador bajo el diseño complejo y la varianza bajo muestreo aleatorio simple. El DEFF depende fundamentalmente de la **correlación intraclase** (*intraclass correlation coefficient*, ICC o *rho*): cuanto mayor sea la similitud de los individuos dentro de un mismo conglomerado, mayor será el DEFF y, por tanto, mayor el [[error-muestral]] para un tamaño de muestra dado. En la práctica, el investigador debe aumentar el número total de entrevistas para compensar esta pérdida de precisión, lo que atenúa —sin eliminar— la ventaja económica del diseño.

### Conglomerados de tamaño desigual

Cuando los conglomerados difieren sensiblemente en tamaño, la selección con **probabilidad proporcional al tamaño** (PPT) permite corregir el sesgo que supondría dar la misma probabilidad de inclusión a un barrio de 500 habitantes que a uno de 10 000. En este esquema, los conglomerados grandes tienen mayor probabilidad de ser seleccionados, pero dentro de cada uno se realiza el mismo número de entrevistas, de modo que cada individuo de la población conserva una probabilidad de selección igual.

## Relación con otros conceptos

El muestreo por conglomerados se sitúa dentro de la familia de técnicas de [[muestreo]] probabilístico y mantiene relaciones estrechas con varios conceptos metodológicos:

- Frente al [[muestreo-aleatorio|muestreo aleatorio simple]], sacrifica precisión a cambio de viabilidad logística y reducción de costos.
- Frente al [[muestreo-estratificado]], invierte la lógica de la homogeneidad interna/externa de los subgrupos.
- Constituye el componente central del [[muestreo-polietapico]], que lo combina con estratificación y, en ocasiones, cuotas finales.
- La magnitud del [[error-muestral]] en un diseño por conglomerados es siempre mayor que en un diseño aleatorio simple del mismo *n*, lo que obliga a calcular tamaños de muestra ajustados.
- La [[representatividad]] del diseño descansa en que los conglomerados seleccionados reproduzcan la heterogeneidad de la población total.

## Debates y críticas

La principal crítica al muestreo por conglomerados es la **pérdida de eficiencia estadística**. Cuando la correlación intraclase es elevada —es decir, los individuos de un mismo conglomerado se parecen mucho—, las observaciones adicionales dentro del grupo aportan poca información nueva, y la varianza del estimador puede ser notablemente mayor que la del muestreo aleatorio simple. En contextos urbanos segregados (por clase social, etnia, nivel educativo), los barrios tienden a ser internamente homogéneos, lo que eleva el DEFF y debilita la precisión de las estimaciones.

Otro debate relevante concierne a la **determinación del número óptimo de conglomerados frente al número de individuos por conglomerado**. En general, es preferible seleccionar muchos conglomerados con pocos individuos cada uno que pocos conglomerados con muchos individuos, porque la primera opción reduce la correlación intraclase efectiva y mejora la precisión global.

## Vigencia contemporánea

El muestreo por conglomerados sigue siendo una herramienta indispensable en la investigación social contemporánea. Las encuestas de hogares de organismos internacionales (Banco Mundial, OMS, UNICEF) emplean sistemáticamente diseños por conglomerados geográficos para estimar indicadores de pobreza, mortalidad y cobertura de salud en países donde no existen padrones actualizados. En epidemiología, el método «30 × 7» de la OMS (30 conglomerados de 7 hogares) se ha utilizado extensamente para estimar la mortalidad en contextos de conflicto armado y emergencia humanitaria. En sociología electoral, los barómetros del CIS continúan recurriendo a diseños polietápicos con conglomerados de secciones censales como unidades primarias de muestreo.

## Ejemplo empírico

Un equipo de investigación desea estimar la proporción de hogares en situación de pobreza energética en una comunidad autónoma española. Dado que no existe un listado completo de hogares, se opta por un diseño por conglomerados en dos etapas: en la primera etapa se seleccionan aleatoriamente 40 secciones censales (conglomerados) de las 2 000 existentes, con probabilidad proporcional al número de viviendas; en la segunda etapa se eligen 15 viviendas al azar dentro de cada sección seleccionada, obteniendo una muestra de 600 hogares. El DEFF estimado es 1,8, lo que significa que la varianza del estimador es un 80 % mayor que la que se obtendría con 600 hogares seleccionados por muestreo aleatorio simple. Para alcanzar la misma precisión que un MAS de 600, se necesitarían aproximadamente 1 080 hogares (600 × 1,8). Aun así, el ahorro logístico —concentrar entrevistadores en 40 puntos en lugar de dispersarlos por toda la comunidad— compensa ampliamente el incremento del tamaño muestral.

## Véase también

- [[muestreo]]
- [[muestreo-aleatorio]]
- [[muestreo-estratificado]]
- [[muestreo-polietapico]]
- [[error-muestral]]
- [[representatividad]]
- [[muestra]]
- [[encuesta]]

## Fuentes

- Hansen, M. H., Hurwitz, W. N. y Madow, W. G. (1953). *Sample Survey Methods and Theory*. Nueva York: John Wiley & Sons.
- Kish, L. (1965). *Survey Sampling*. Nueva York: John Wiley & Sons.
- Cea D'Ancona, M. Á. (2012). *Fundamentos y aplicaciones en metodología cuantitativa*. Madrid: Síntesis.
- Apuntes de cátedra, Metodología de las ciencias sociales, 2026-S1 — [[la-investigacion-cuantitativa]], [[modulo-3|Módulo 3]].
