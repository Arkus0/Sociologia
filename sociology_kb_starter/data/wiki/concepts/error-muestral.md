---
id: error-muestral
title: Error muestral
note_type: concept
semester: 2026-S1
course: "Metodologia de las ciencias sociales"
related_concepts:
  - muestra
  - muestreo
  - nivel-de-confianza
  - tamano-de-la-muestra
  - estadistica-inferencial
  - representatividad
  - varianza
  - desviacion-estandar
tags:
  - estadística
  - muestreo
  - inferencia estadística
  - metodología cuantitativa
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\la-investigacion-cuantitativa.md
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\modulo-3.md
updated_at: '2025-07-13'
---

# Error muestral

## Definición

El **error muestral** (o *error de muestreo*) es la diferencia entre el valor de un estadístico calculado a partir de una [[muestra]] y el verdadero valor del parámetro correspondiente en la [[poblacion-estadistica|población]]. Toda vez que se trabaja con un subconjunto y no con la totalidad del universo, el resultado obtenido está sujeto a una variación aleatoria inevitable: esa variación es, precisamente, el error muestral (Särndal, Swensson y Wretman, 1992).

Formalmente, si $\hat{\theta}$ es el estimador muestral y $\theta$ el parámetro poblacional, el error muestral se expresa como:

$$e = \hat{\theta} - \theta$$

En la práctica el parámetro $\theta$ es desconocido, por lo que el error muestral exacto no puede calcularse; lo que sí puede estimarse es su magnitud probable mediante el **error estándar** ($SE$), es decir, la desviación típica de la distribución muestral del estimador. A partir del error estándar se construyen los conceptos de **margen de error** e **intervalo de confianza**, pilares de la [[estadistica-inferencial]].

## Origen y contexto histórico

La formalización del error muestral es inseparable de la historia de la teoría de probabilidades y la estadística matemática. Ya en el siglo XVIII, Abraham de Moivre y Pierre-Simon Laplace sentaron las bases del **teorema central del límite**, que demuestra que la distribución de las medias muestrales tiende a la normalidad conforme crece el tamaño de la muestra, independientemente de la distribución original de la variable. Este teorema proporciona la justificación teórica para cuantificar el error muestral.

En el siglo XX, Jerzy Neyman (1934) revolucionó la inferencia al proponer el método de **intervalos de confianza**, que permite acotar la incertidumbre de una estimación muestral con una probabilidad conocida. La encuesta por muestreo probabilístico se consolidó como herramienta central de las ciencias sociales a partir de los trabajos de Leslie Kish, cuyo manual *Survey Sampling* (1965) sistematizó los procedimientos de [[muestreo]] aleatorio y la estimación de errores asociados.

Un episodio histórico ilustrativo es la encuesta de la revista *Literary Digest* en 1936, que predijo erróneamente la victoria de Alf Landon frente a Franklin D. Roosevelt. Pese a contar con más de dos millones de respuestas, la muestra presentaba un sesgo de cobertura severo (se contactó a suscriptores de la revista y propietarios de automóviles y teléfonos, grupos de renta alta). Este fracaso no fue causado por el error muestral aleatorio, sino por errores no muestrales, y demostró que el tamaño de la muestra no compensa los defectos en el diseño del [[muestreo]].

## Desarrollo teórico

### Error estándar y margen de error

El **error estándar** de la media muestral para una variable con [[varianza]] $\sigma^2$ es:

$$SE(\bar{x}) = \frac{\sigma}{\sqrt{n}}$$

donde $n$ es el [[tamano-de-la-muestra]]. Esta fórmula revela una relación fundamental: el error muestral disminuye en proporción a la raíz cuadrada del tamaño de la muestra. Duplicar la precisión exige cuadruplicar $n$, lo cual impone restricciones prácticas y económicas a toda investigación empírica.

El **margen de error** se obtiene multiplicando el error estándar por el valor crítico $z$ correspondiente al [[nivel-de-confianza]] deseado (por ejemplo, $z = 1{,}96$ para el 95 %). El intervalo de confianza resultante, $\bar{x} \pm z \cdot SE$, proporciona un rango dentro del cual se espera que se encuentre el parámetro poblacional con la probabilidad estipulada (Neyman, 1934).

### Ley de los grandes números

La **ley de los grandes números** complementa el teorema central del límite: a medida que $n \to \infty$, el estadístico muestral converge al parámetro poblacional. Ambos teoremas constituyen la base axiomática de la inferencia estadística y legitiman la práctica del [[muestreo]] probabilístico en la investigación social.

### Factores que determinan el error muestral

Según el temario de Borge y Padró-Solanet (UOC), cuatro factores interrelacionados determinan el error muestral admisible: (1) la **variabilidad** de la población —a mayor heterogeneidad, mayor error—; (2) el **tamaño de la población** —relevante solo cuando $N < 100\,000$—; (3) el **nivel de confianza** deseado; y (4) el **margen de error** tolerable. En la práctica de las encuestas sociales el error aceptable suele fijarse en torno al ±3 %.

## Relación con otros conceptos

El error muestral se sitúa en el centro de una constelación de conceptos metodológicos:

- **[[muestra]] y [[muestreo]]**: el error muestral solo puede cuantificarse rigurosamente cuando la muestra es probabilística; en muestras de conveniencia o por cuotas, no existe base para estimar su magnitud.
- **[[tamano-de-la-muestra]]**: es el factor más directamente controlable para reducir el error muestral. Kish (1965) insistía en que el diseño muestral importa tanto como el tamaño.
- **[[nivel-de-confianza]]**: determina la amplitud del intervalo; un nivel más exigente (99 % frente a 95 %) amplía el margen de error para la misma $n$.
- **[[estadistica-inferencial]]**: el error muestral es la razón de ser de la inferencia: toda generalización de la muestra a la población debe ir acompañada de una medida de incertidumbre.
- **[[representatividad]]**: una muestra representativa minimiza los sesgos sistemáticos, pero no elimina el error muestral aleatorio; ambos aspectos son complementarios.

## Debates y críticas

### Error muestral vs. error no muestral

Robert Groves (1989, 2004) desarrolló el marco del **error total de la encuesta** (*Total Survey Error*, TSE), que distingue entre error muestral y un conjunto de errores no muestrales: error de cobertura, error de no respuesta, error de medición y error de procesamiento. Groves argumentó que la obsesión con el error muestral —fácil de cuantificar— lleva a subestimar fuentes de sesgo más dañinas y difíciles de detectar. En muchas encuestas reales, los errores no muestrales superan con creces al error muestral.

### Incertidumbre e interpretación

Friedrich Hayek (1974), en su discurso del Nobel, advirtió sobre la "pretensión de conocimiento exacto" en las ciencias sociales: los intervalos de confianza y los márgenes de error pueden crear una falsa sensación de precisión cuando los supuestos del modelo no se cumplen. Esta crítica conecta con la tradición popperiana que subraya la provisionalidad de todo conocimiento empírico.

### Controversias sobre el nivel de confianza

La comunidad científica ha debatido si el umbral convencional del 95 % es adecuado. Algunos estadísticos han propuesto elevar el estándar al 99,5 % (Benjamin et al., 2018), mientras que otros abogan por abandonar los umbrales fijos en favor de la comunicación directa del tamaño del efecto y del intervalo de confianza completo.

## Vigencia contemporánea

En la era de los macrodatos (*big data*) y las encuestas en línea, el error muestral adquiere nuevas dimensiones. Las muestras masivas no probabilísticas (paneles web, datos de redes sociales) pueden tener un error muestral estadísticamente ínfimo pero enormes sesgos de cobertura y autoselección. Meng (2018) demostró formalmente que una muestra sesgada de un millón de casos puede ser menos informativa que una muestra probabilística de mil. Este resultado refuerza la relevancia del diseño muestral riguroso y la necesidad de evaluar el error total, no solo el componente muestral.

En la investigación social aplicada, las fichas técnicas de las encuestas continúan reportando el error muestral como indicador de calidad, y los medios de comunicación lo utilizan como medida de credibilidad de los sondeos electorales y de opinión pública.

## Ejemplo empírico

Supóngase una encuesta sobre intención de voto con una [[muestra]] aleatoria simple de $n = 1\,000$ personas, en la que el 45 % declara preferencia por un candidato. El error estándar de la proporción es:

$$SE(\hat{p}) = \sqrt{\frac{\hat{p}(1-\hat{p})}{n}} = \sqrt{\frac{0{,}45 \times 0{,}55}{1000}} \approx 0{,}0157$$

Con un [[nivel-de-confianza]] del 95 % ($z = 1{,}96$), el margen de error es $\pm 3{,}1$ puntos porcentuales. El intervalo de confianza para la proporción poblacional es $[41{,}9\%;\; 48{,}1\%]$. Si se quisiera reducir el margen de error a la mitad ($\pm 1{,}55$ pp), sería necesario cuadruplicar la muestra a $n = 4\,000$.

## Véase también

- [[muestra]]
- [[muestreo]]
- [[tamano-de-la-muestra]]
- [[nivel-de-confianza]]
- [[estadistica-inferencial]]
- [[representatividad]]
- [[varianza]]
- [[desviacion-estandar]]

## Fuentes

- Borge Bravo, R. y Padró-Solanet i Grau, A. (s.f.). *La investigación cuantitativa: encuesta, experimento y análisis estadístico*. Módulo 3, Metodología de las Ciencias Sociales, UOC.
- Groves, R. M. (1989). *Survey Errors and Survey Costs*. Wiley.
- Groves, R. M. et al. (2004). *Survey Methodology*. Wiley.
- Kish, L. (1965). *Survey Sampling*. Wiley.
- Meng, X.-L. (2018). Statistical paradises and paradoxes in big data (I). *Annals of Applied Statistics*, 12(2), 685–726.
- Neyman, J. (1934). On the two different aspects of the representative method. *Journal of the Royal Statistical Society*, 97(4), 558–625.
- Särndal, C.-E., Swensson, B. y Wretman, J. H. (1992). *Model Assisted Survey Sampling*. Springer-Verlag.
