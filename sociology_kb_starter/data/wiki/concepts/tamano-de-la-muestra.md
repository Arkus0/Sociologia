---
id: tamano-de-la-muestra
title: Tamaño de la muestra
note_type: concept
semester: 2026-S1
course: "Metodologia de las ciencias sociales"
related_concepts:
  - muestra
  - error-muestral
  - nivel-de-confianza
  - muestreo
  - representatividad
  - estadistica-inferencial
  - varianza
  - muestreo-estratificado
tags:
  - metodología
  - estadística
  - muestreo
  - investigación-cuantitativa
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\la-investigacion-cuantitativa.md
updated_at: '2025-07-13'
---

## Definición

El **tamaño de la muestra** (*n*) es el número de unidades de observación —individuos, hogares, organizaciones u otras entidades— que componen la [[muestra]] extraída de una [[poblacion-estadistica|población]] para una investigación empírica. Constituye una decisión metodológica central en todo diseño cuantitativo, pues de él dependen la precisión de las estimaciones, la capacidad de detectar efectos reales y la viabilidad económica y logística del estudio. En ciencias sociales, donde la variabilidad del comportamiento humano es elevada y los recursos son finitos, la determinación del tamaño muestral obliga a equilibrar rigor estadístico y restricciones prácticas.

## Origen y contexto histórico

La preocupación por cuántos casos son suficientes para representar una población surgió en paralelo al desarrollo de la [[estadistica-inferencial|estadística inferencial]]. En el siglo XVIII, Abraham de Moivre formuló tempranamente la relación entre el tamaño muestral y la dispersión de las estimaciones, y Pierre-Simon Laplace extendió estas ideas al establecer las bases del **teorema central del límite**, que demuestra que la distribución de las medias muestrales converge hacia la normalidad conforme *n* crece, con independencia de la distribución original de la variable.

A lo largo del siglo XIX, Adolphe Quetelet y Francis Galton impulsaron la aplicación de la estadística a fenómenos sociales, pero fue en el siglo XX cuando la determinación formal del tamaño muestral se consolidó. Jerzy Neyman, en los años 1930, demostró que la asignación óptima de casos a cada estrato en el [[muestreo-estratificado|muestreo estratificado]] minimiza la [[varianza]] del estimador global. En 1969, Jacob Cohen publicó *Statistical Power Analysis for the Behavioral Sciences*, obra que sistematizó el **análisis de potencia** (*power analysis*) y estableció un marco para calcular el tamaño muestral necesario para detectar un efecto de magnitud predeterminada con una probabilidad dada, transformando la práctica de la investigación social y biomédica.

## Desarrollo teórico

### Factores determinantes

Según las fuentes del curso de Metodología de las Ciencias Sociales (UOC), el tamaño de la muestra depende de cuatro factores interrelacionados:

1. **Variabilidad de la población**: cuanto más heterogénea sea la población respecto a la variable de interés, mayor *n* se requiere para obtener estimaciones precisas.
2. **Tamaño de la población (*N*)**: solo resulta relevante cuando *N* es inferior a 100 000; por encima de ese umbral, la corrección por finitud es despreciable.
3. **[[nivel-de-confianza|Nivel de confianza]]** (1 − α): expresa la probabilidad de que el intervalo estimado contenga el parámetro real. El nivel convencional es del 95 % (*Z* = 1,96).
4. **[[error-muestral|Margen de error]]** (ε): la máxima diferencia aceptable entre el estadístico muestral y el parámetro poblacional. En encuestas sociales, el margen típico es ±3 %.

### Fórmulas fundamentales

Para **poblaciones infinitas** o muy grandes, cuando se estima una proporción y se desconoce la desviación estándar, la fórmula básica es:

$$n = \frac{Z_{\alpha}^{2} \cdot p \cdot q}{\varepsilon^{2}}$$

donde *p* es la proporción esperada del atributo en la población, *q* = 1 − *p*, y cuando se desconoce *p* se asume *p* = *q* = 0,5 (máxima variabilidad). Para **poblaciones finitas**, se aplica la corrección:

$$n = \frac{N \cdot Z_{\alpha}^{2} \cdot p \cdot q}{\varepsilon^{2}(N-1) + Z_{\alpha}^{2} \cdot p \cdot q}$$

Cuando se conoce la **desviación estándar** (σ) de la población —o se estima mediante una muestra piloto—, la fórmula se expresa como:

$$n = \frac{N \cdot \sigma^{2} \cdot Z_{\alpha}^{2}}{\varepsilon^{2}(N-1) + \sigma^{2} \cdot Z_{\alpha}^{2}}$$

### Rendimientos decrecientes

Una propiedad crucial derivada del teorema central del límite es que el [[error-muestral]] disminuye en proporción a la raíz cuadrada de *n*: duplicar la precisión exige cuadruplicar el tamaño muestral. Este principio de **rendimientos decrecientes** impone restricciones económicas y operativas a toda investigación empírica: a partir de cierto umbral, incrementar *n* produce mejoras marginales de precisión a un coste desproporcionado.

### Análisis de potencia

El enfoque de Cohen formalizó la relación entre cuatro magnitudes: tamaño del efecto, nivel de significación (α), potencia estadística (1 − β) y tamaño muestral. Fijadas tres cualesquiera, la cuarta queda determinada. Este marco es especialmente relevante en diseños experimentales y cuasiexperimentales en ciencias sociales, donde efectos pequeños pero sustantivos pueden pasar inadvertidos si la muestra es insuficiente (error de tipo II).

## Relación con otros conceptos

El tamaño de la muestra se sitúa en el cruce de varios pilares de la metodología cuantitativa. Es inseparable del [[muestreo]], pues cada procedimiento —aleatorio simple, estratificado, por conglomerados— implica fórmulas de cálculo específicas. Se vincula directamente con el [[error-muestral]]: a mayor *n*, menor error estándar, y por tanto mayor [[representatividad]] de las estimaciones. El [[nivel-de-confianza]] fija el grado de certidumbre que el investigador exige, y opera como multiplicador en las fórmulas de cálculo. La [[varianza]] poblacional determina cuántos casos son necesarios para capturar la dispersión real del fenómeno. Finalmente, la [[estadistica-inferencial]] proporciona el marco teórico que justifica la extrapolación de la muestra a la población, siendo el tamaño muestral una condición necesaria —aunque no suficiente— para la validez de dicha inferencia.

## Debates y críticas

Un primer debate recurrente es la **confusión entre tamaño y calidad**. El célebre fracaso de la encuesta de la revista *Literary Digest* en 1936 —que predijo erróneamente la victoria de Alf Landon con más de dos millones de respuestas— demostró que un tamaño muestral enorme no compensa los defectos en el diseño del [[muestreo]]: el sesgo de cobertura invalidó la muestra pese a su magnitud.

Un segundo problema concierne a la **sensibilidad al tamaño muestral** de pruebas como el [[chi-cuadrado]]: con muestras muy grandes, diferencias triviales resultan estadísticamente significativas, mientras que con muestras pequeñas asociaciones reales pasan inadvertidas. Esta paradoja ha intensificado la exigencia de complementar la significación estadística con medidas de tamaño del efecto.

Desde la estadística bayesiana, se cuestiona la rigidez de los umbrales convencionales (α = 0,05, potencia del 80 %) y se proponen enfoques adaptativos que permiten recalcular *n* a medida que se acumulan datos. Asimismo, en la era del *big data*, la abundancia de datos observacionales plantea nuevos desafíos: el tamaño puede ser virtualmente ilimitado, pero los sesgos de selección y la falta de aleatorización amenazan la validez inferencial.

## Vigencia contemporánea

La determinación del tamaño muestral sigue siendo un paso obligatorio en todo protocolo de investigación social cuantitativa. Las agencias de financiación y los comités de ética exigen justificaciones formales del cálculo de *n*. Software especializado —G*Power, paquetes de R como `pwr` y `samplesize`, módulos de Stata— ha facilitado enormemente los cálculos de potencia. En encuestas electorales y de opinión, los organismos demoscópicos trabajan típicamente con muestras de entre 1 000 y 2 500 individuos para poblaciones nacionales, lo que con muestreo aleatorio arroja márgenes de error del ±2 % al ±3 % con un 95 % de confianza. Paralelamente, la proliferación de meta-análisis ha reforzado la importancia de reportar tamaños muestrales y tamaños de efecto para permitir la agregación de resultados entre estudios.

## Ejemplo empírico

Una investigadora desea estimar la proporción de estudiantes universitarios favorables a una reforma curricular. No dispone de estimaciones previas, por lo que asume máxima variabilidad (*p* = *q* = 0,5). Fija un nivel de confianza del 95 % (*Z* = 1,96) y un margen de error del ±3 %. La universidad tiene 30 000 estudiantes. Aplicando la fórmula para poblaciones finitas:

$$n = \frac{30\,000 \times 1{,}96^{2} \times 0{,}5 \times 0{,}5}{0{,}03^{2} \times 29\,999 + 1{,}96^{2} \times 0{,}5 \times 0{,}5} \approx 1\,031$$

Se necesitan aproximadamente 1 031 encuestas. Nótese que para una población infinita la fórmula simplificada daría *n* ≈ 1 068: la corrección por finitud apenas reduce el tamaño, confirmando que para *N* > 100 000 el efecto del tamaño poblacional es despreciable.

## Véase también

- [[muestra]]
- [[error-muestral]]
- [[nivel-de-confianza]]
- [[muestreo]]
- [[muestreo-estratificado]]
- [[representatividad]]
- [[estadistica-inferencial]]
- [[varianza]]
- [[chi-cuadrado]]
- [[encuesta-de-opinion]]

## Fuentes

- Apuntes del módulo 3, *Metodología de las Ciencias Sociales* (UOC, 2026-S1): [[la-investigacion-cuantitativa-encuesta-experimento-y-analisis-estadistico]]
- Cohen, J. (1988). *Statistical Power Analysis for the Behavioral Sciences* (2.ª ed.). Lawrence Erlbaum.
- Neyman, J. (1934). On the two different aspects of the representative method. *Journal of the Royal Statistical Society*, 97(4), 558-625.
- Martínez Bencardino, C. (2012). *Estadística y muestreo* (13.ª ed.). ECOE Ediciones.
- King, G., Keohane, R. O. y Verba, S. (2000). *El diseño de la investigación social*. Alianza.
