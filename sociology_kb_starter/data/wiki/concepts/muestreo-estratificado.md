---
id: muestreo-estratificado
title: Muestreo estratificado
note_type: concept
semester: 2026-S1
course: "Metodologia de las ciencias sociales"
related_concepts:
  - "[[muestreo]]"
  - "[[muestreo-aleatorio]]"
  - "[[representatividad]]"
  - "[[error-muestral]]"
  - "[[variables-sociodemograficas]]"
  - "[[tamano-de-la-muestra]]"
  - "[[varianza]]"
  - "[[muestreo-por-conglomerados]]"
tags:
  - muestreo
  - metodología-cuantitativa
  - estadística
  - diseño-muestral
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\la-investigacion-cuantitativa.md
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\modulo-3.md
updated_at: '2025-07-13'
---

## Definición

El **muestreo estratificado** (*stratified sampling*) es una técnica de [[muestreo]] probabilístico que consiste en dividir la población objeto de estudio en subgrupos mutuamente excluyentes y exhaustivos —denominados **estratos**— que son internamente homogéneos respecto de la variable de interés y externamente heterogéneos entre sí. Dentro de cada estrato se extrae una muestra aleatoria independiente, y los resultados parciales se combinan para obtener estimadores del parámetro poblacional global. La técnica persigue reducir el [[error-muestral]] y aumentar la precisión de las estimaciones en comparación con el [[muestreo-aleatorio|muestreo aleatorio simple]], especialmente cuando la población presenta una heterogeneidad marcada que puede ser capturada por variables de estratificación conocidas.

## Origen y contexto histórico

Los antecedentes del muestreo estratificado se remontan a las encuestas sociales del siglo XIX, cuando los primeros estadísticos intentaban obtener representaciones fiables de poblaciones extensas. Sin embargo, fue **Jerzy Neyman** quien, en su artículo seminal de 1934 (*On the Two Different Aspects of the Representative Method*), proporcionó la fundamentación teórica rigurosa del procedimiento. Neyman demostró que la asignación óptima del tamaño muestral a cada estrato minimiza la [[varianza]] del estimador global, superando así los métodos de selección intencional que predominaban en la estadística aplicada de la época. Su trabajo permitió calcular [[intervalo-de-confianza|intervalos de confianza]] a partir del propio diseño de la muestra, sin necesidad de supuestos paramétricos sobre la distribución poblacional.

En la posguerra, **Leslie Kish** sistematizó la práctica del muestreo estratificado en su obra *Survey Sampling* (1965), referencia canónica para sociólogos, demógrafos y politólogos. Kish integró la estratificación dentro de diseños complejos —combinándola con el [[muestreo-por-conglomerados]] y procedimientos polietápicos— para abordar las necesidades operativas de las grandes encuestas nacionales. A partir de entonces, el muestreo estratificado se convirtió en componente estándar de los diseños muestrales de organismos como el CIS en España, Eurostat y las agencias censales de América Latina.

## Desarrollo teórico

### Lógica de la estratificación

La eficacia del muestreo estratificado descansa en una premisa estadística: si los estratos son internamente homogéneos, la variabilidad dentro de cada estrato es menor que la variabilidad total de la población. Al muestrear por separado cada subgrupo, se controla esa fuente de variación y se obtienen estimadores más precisos. Las variables de estratificación más habituales en ciencias sociales son las [[variables-sociodemograficas]]: sexo, edad, nivel educativo, clase social, región geográfica o situación laboral.

### Tipos de asignación

Existen tres modalidades principales de distribución del tamaño muestral entre los estratos:

1. **Asignación proporcional**: el número de unidades seleccionadas en cada estrato es proporcional al peso relativo del estrato en la población. Si las mujeres representan el 55 % de la población, la muestra contendrá aproximadamente un 55 % de mujeres. Es la modalidad más sencilla y garantiza la [[representatividad]] estructural de la muestra.

2. **Asignación óptima (de Neyman)**: se asignan más casos a los estratos que presentan mayor variabilidad interna y menos a los más homogéneos. Neyman demostró que esta asignación minimiza la varianza del estimador para un tamaño muestral fijo, o bien minimiza el tamaño muestral necesario para alcanzar una precisión deseada. Requiere un conocimiento previo —al menos aproximado— de la desviación estándar de la variable de interés en cada estrato.

3. **Asignación desproporcionada**: se sobrerepresentan deliberadamente ciertos estratos minoritarios para disponer de suficientes casos que permitan análisis estadísticos significativos dentro de cada subgrupo. Es frecuente en estudios sobre minorías étnicas o grupos de difícil acceso. Los resultados globales se corrigen mediante ponderación.

### Formalización básica

Sea una población de tamaño $N$ dividida en $L$ estratos de tamaños $N_1, N_2, \ldots, N_L$. El estimador estratificado de la media poblacional es:

$$\bar{y}_{st} = \sum_{h=1}^{L} W_h \, \bar{y}_h$$

donde $W_h = N_h / N$ es el peso del estrato $h$ y $\bar{y}_h$ es la media muestral del estrato. La varianza del estimador bajo asignación proporcional es siempre menor o igual que la del muestreo aleatorio simple, verificándose la igualdad solo cuando todos los estratos poseen idéntica media.

## Relación con otros conceptos

El muestreo estratificado se inscribe dentro de la familia más amplia del [[muestreo]] probabilístico y constituye una extensión refinada del [[muestreo-aleatorio|muestreo aleatorio simple]]. Mientras este último trata a la población como un todo indiferenciado, la estratificación incorpora información auxiliar para ganar precisión. Se diferencia del [[muestreo-por-conglomerados]] en que este agrupa unidades *internamente heterogéneas* y selecciona algunos conglomerados completos, en tanto que la estratificación divide la población en grupos *internamente homogéneos* y muestrea dentro de todos ellos.

El concepto de [[representatividad]] es central: la estratificación garantiza que la muestra refleja la composición de la población según las variables de estratificación. El [[error-muestral]] resultante depende de la [[varianza]] intraestrato; cuanto más homogéneos sean los estratos, menor será dicho error. El [[tamano-de-la-muestra]] necesario para obtener una precisión dada puede reducirse sensiblemente respecto del muestreo aleatorio simple cuando los estratos están bien definidos.

## Debates y críticas

La principal objeción al muestreo estratificado es de orden práctico: exige disponer de información previa sobre la distribución de la variable de estratificación en la población, lo que presupone un marco muestral detallado. En sociedades con registros administrativos deficientes o poblaciones de difícil localización, esta condición puede resultar inalcanzable. Además, la elección inadecuada de las variables de estratificación —por ejemplo, estratos que no guardan relación con la variable estudiada— anula las ganancias de precisión y añade complejidad operativa sin beneficio.

En el plano epistemológico, autores como Bourdieu han señalado que la clasificación de la población en estratos discretos puede reificar categorías sociales (e.g., «clase media», «joven», «inmigrante»), ocultando la fluidez y la porosidad de las fronteras sociales. Desde la investigación cualitativa, se subraya que la lógica estratificada privilegia la extensión sobre la profundidad analítica, limitando la capacidad de captar significados y procesos subjetivos.

## Vigencia contemporánea

En la investigación social actual, el muestreo estratificado conserva plena vigencia. Las grandes encuestas nacionales —como el Barómetro del CIS, la Encuesta Social Europea (ESS) o la Encuesta Permanente de Hogares en Argentina— emplean diseños polietápicos que combinan estratificación geográfica y sociodemográfica con selección por conglomerados y cuotas en las etapas finales. La estratificación resulta particularmente útil en estudios de desigualdad social, donde interesa desagregar resultados por clase, género o etnia, y en encuestas electorales, donde la heterogeneidad territorial exige garantizar la representación de cada circunscripción.

El auge de los métodos mixtos y del *big data* no ha desplazado la técnica; antes bien, las bases de datos administrativas y los registros digitales proporcionan marcos muestrales cada vez más detallados que facilitan la construcción de estratos precisos.

## Ejemplo empírico

En un estudio sobre satisfacción laboral en una empresa con 180 empleados, distribuidos en cuatro categorías —hombres a jornada completa (90), hombres a media jornada (18), mujeres a jornada completa (9) y mujeres a media jornada (63)—, se desea extraer una muestra estratificada de 40 personas con asignación proporcional. El peso de cada estrato se calcula dividiendo su tamaño por el total: 90/180 = 50 %, 18/180 = 10 %, 9/180 = 5 %, 63/180 = 35 %. Aplicando esos porcentajes a la muestra: 20 hombres a jornada completa, 4 a media jornada, 2 mujeres a jornada completa y 14 a media jornada. Este procedimiento garantiza que cada categoría laboral-género quede representada en la muestra en la misma proporción que en la población, reduciendo el sesgo de selección respecto de un sorteo aleatorio simple.

## Véase también

- [[muestreo]]
- [[muestreo-aleatorio]]
- [[muestreo-por-conglomerados]]
- [[muestreo-polietapico]]
- [[representatividad]]
- [[error-muestral]]
- [[tamano-de-la-muestra]]
- [[varianza]]
- [[variables-sociodemograficas]]
- [[encuesta]]

## Fuentes

- Neyman, J. (1934). "On the Two Different Aspects of the Representative Method: The Method of Stratified Sampling and the Method of Purposive Selection". *Journal of the Royal Statistical Society*, 97(4), 558–625.
- Kish, L. (1965). *Survey Sampling*. Nueva York: Wiley.
- Corbetta, P. (2003). *Metodología y técnicas de investigación social*. Madrid: McGraw-Hill.
- [[la-investigacion-cuantitativa]] (Metodología de las ciencias sociales, 2026-S1)
- [[modulo-3]] (Metodología de las ciencias sociales, 2026-S1)
