---
id: fiabilidad
title: Fiabilidad
note_type: concept
semester: 2026-S1
course: "Metodologia de las ciencias sociales"
related_concepts:
  - validez
  - instrumento-de-medicion
  - operacionalizacion
  - encuesta
  - error-muestral
  - variable-dependiente
  - diseno-de-investigacion
tags:
  - metodología
  - medición
  - psicometría
  - investigación-cuantitativa
  - teoría-clásica-de-tests
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\modulo-2.md
updated_at: '2025-07-13'
---

## Definición

La **fiabilidad** (también denominada *confiabilidad* en la tradición latinoamericana) es una propiedad fundamental de todo [[instrumento-de-medicion]] que hace referencia al grado de **consistencia y estabilidad** de las puntuaciones obtenidas a lo largo de sucesivos procesos de medición. En términos formales, un instrumento es fiable cuando medidas repetidas del mismo fenómeno, realizadas en condiciones equivalentes, producen resultados idénticos o muy semejantes. Como señalan King, Keohane y Verba (1994), la fiabilidad constituye una de las tres condiciones —junto con la [[validez]] y la completitud— para que los valores asignados a las variables representen de modo analíticamente útil la realidad social.

Conviene distinguir fiabilidad de validez: un instrumento puede arrojar resultados altamente consistentes (fiable) y, sin embargo, no medir aquello que pretende medir (inválido). Un reloj que siempre adelanta cinco minutos es fiable pero no válido. La relación inversa no se sostiene: la validez presupone un grado mínimo de fiabilidad.

## Origen y contexto histórico

El estudio sistemático de la fiabilidad se inscribe en la **teoría clásica de los tests** (TCT), cuyo marco formal fue establecido por Charles Spearman entre 1904 y 1913. Spearman propuso un modelo lineal según el cual la puntuación empírica (*X*) que obtiene un sujeto es la suma de su puntuación verdadera (*V*) y un componente de error aleatorio (*E*): $X = V + E$. A partir de este supuesto, la fiabilidad se define como la proporción de varianza verdadera respecto de la varianza total observada:

$$\rho_{xx'} = \frac{\sigma_V^2}{\sigma_X^2} = 1 - \frac{\sigma_E^2}{\sigma_X^2}$$

Este modelo orientó durante todo el siglo XX la construcción de escalas en psicología, educación y ciencias sociales, y sentó las bases para los procedimientos de estimación que se utilizan hasta hoy.

## Desarrollo teórico

### Tipos de fiabilidad

La TCT distingue varios procedimientos para estimar la fiabilidad, cada uno sensible a fuentes de error distintas:

1. **Test-retest (estabilidad temporal)**. Se aplica el mismo instrumento en dos momentos diferentes y se calcula la correlación de Pearson entre ambas puntuaciones. Un intervalo demasiado breve introduce efectos de memoria; uno demasiado largo, factores de maduración o cambio real.

2. **Formas paralelas (equivalencia)**. Se construyen dos versiones del instrumento con ítems distintos que miden el mismo constructo. La correlación entre ambas formas indica el grado de equivalencia. Es el método más robusto en teoría, pero la construcción de formas genuinamente paralelas resulta costosa.

3. **Consistencia interna**. Se basa en una sola aplicación y evalúa la homogeneidad de los ítems.
   - El **alfa de Cronbach** (1951), el índice más utilizado en ciencias sociales, indica en qué grado covarían los ítems de una escala: valores superiores a 0,70 se consideran aceptables; por encima de 0,80, buenos.
   - Los coeficientes de **Kuder-Richardson** (KR-20 y KR-21) se aplican a ítems dicotómicos.
   - El coeficiente **omega** (Ω), basado en análisis factorial, supera ciertas limitaciones del alfa cuando los ítems no son tau-equivalentes.

4. **Fiabilidad inter-evaluadores**. Cuando la medición depende de juicios humanos (codificación de entrevistas, análisis de contenido), se calcula el **kappa de Cohen** (κ), que corrige el acuerdo esperable por azar. Es especialmente relevante en la [[operacionalizacion]] de variables cualitativas.

### Factores que afectan la fiabilidad

Dos factores principales modulan la fiabilidad: la **longitud del instrumento** (más ítems tienden a aumentar la fiabilidad, según la fórmula de Spearman-Brown) y la **variabilidad de la muestra** (mayor heterogeneidad produce coeficientes más altos, lo que obliga a reportar siempre la muestra de referencia).

## Relación con otros conceptos

La fiabilidad es inseparable del proceso de [[operacionalizacion]]: traducir conceptos abstractos en indicadores medibles exige garantizar que dichos indicadores funcionen de manera consistente. En el diseño de una [[encuesta]], por ejemplo, las preguntas de consistencia —formulaciones ligeramente distintas del mismo contenido intercaladas en el cuestionario— sirven como control interno de fiabilidad. Las variables sociodemográficas (sexo, edad, nivel educativo) se consideran las más fiables porque su referente empírico es menos ambiguo que el de variables actitudinales.

La fiabilidad guarda también una relación directa con el [[error-muestral]]: un instrumento poco fiable incrementa la varianza de error en las estimaciones, reduciendo la potencia estadística del [[diseno-de-investigacion]]. Por ello, evaluar la fiabilidad antes de la recogida de datos —mediante pruebas piloto— constituye una práctica metodológica esencial.

En cuanto a la [[validez]], ambas propiedades son complementarias: un instrumento válido requiere ser fiable, pero la fiabilidad por sí sola no garantiza validez. Esta distinción aparece recurrentemente en los manuales de metodología (King, Keohane y Verba, 1994; Corbetta, 2007).

## Debates y críticas

### La hegemonía del alfa de Cronbach

A pesar de su popularidad, el alfa de Cronbach ha sido objeto de críticas sustanciales. Investigadores como Sijtsma (2009) y McNeish (2018) señalan que el alfa subestima la fiabilidad cuando los ítems no son tau-equivalentes y que su valor depende del número de ítems, lo que permite inflarlo artificialmente añadiendo preguntas redundantes. Alternativas como el coeficiente omega ganan terreno, aunque el alfa sigue siendo el estándar de facto en la mayoría de revistas.

### La crisis de replicación

Desde 2011, la **crisis de replicación** ha sacudido la psicología social y, por extensión, las ciencias sociales empíricas. El *Reproducibility Project* (Open Science Collaboration, 2015) logró replicar con éxito menos del 40 % de los estudios seleccionados. Karl Popper había señalado la **reproducibilidad** como rasgo definitorio de la ciencia; el fracaso en replicar hallazgos pone en cuestión no solo la fiabilidad de los instrumentos, sino la de todo el proceso de investigación, incluyendo las prácticas de análisis y publicación.

### Fiabilidad en la investigación cualitativa

La tradición cualitativa rechaza trasladar acríticamente los criterios cuantitativos de fiabilidad. Lincoln y Guba (1985) proponen como equivalente funcional la **dependability** (dependabilidad), que se asegura mediante un *audit trail*: un registro detallado de las decisiones metodológicas, la codificación y el análisis, que permite a un evaluador externo verificar la coherencia del proceso. Este criterio reconoce que en la investigación interpretativa el instrumento principal es el propio investigador, cuyas percepciones no pueden estandarizarse como un cuestionario.

## Vigencia contemporánea

En el panorama actual, la fiabilidad ocupa un lugar central en al menos tres frentes. Primero, las **normas de reporte** (APA, 7.ª ed.) exigen informar coeficientes de fiabilidad para toda escala utilizada. Segundo, la disponibilidad de software estadístico (SPSS, R, jamovi) ha democratizado el cálculo de indicadores más sofisticados como el omega y la fiabilidad compuesta. Tercero, el movimiento de **ciencia abierta** promueve la publicación de materiales de medición, datos y código de análisis, lo que permite evaluar la fiabilidad de forma independiente y acumulativa.

En sociología, donde gran parte de la investigación empírica descansa sobre datos de [[encuesta]] —como los del CIS, el Eurobarómetro o la Encuesta Social Europea—, la fiabilidad de los instrumentos condiciona la calidad de las inferencias sobre actitudes, valores y comportamientos colectivos.

## Ejemplo empírico

Supongamos que un equipo de investigación diseña una escala de diez ítems para medir la *confianza institucional* en una muestra de 500 ciudadanos. Tras aplicar la escala, calcula un alfa de Cronbach de 0,84, lo que indica buena consistencia interna. A continuación, administra la escala a un subgrupo de 100 personas dos semanas después (test-retest) y obtiene una correlación de 0,78, aceptable pero inferior al alfa, lo que sugiere que parte de la variabilidad se debe a fluctuaciones temporales en la opinión. Para las preguntas abiertas codificadas por dos analistas, el kappa de Cohen resulta 0,71, señalando un acuerdo sustancial. Estos tres indicadores, tomados en conjunto, proporcionan un panorama completo de la fiabilidad del instrumento antes de emprender el análisis sustantivo.

## Véase también

- [[validez]]
- [[instrumento-de-medicion]]
- [[operacionalizacion]]
- [[encuesta]]
- [[error-muestral]]
- [[variable-dependiente]]
- [[diseno-de-investigacion]]
- [[proceso-de-investigacion]]

## Fuentes

- King, G., Keohane, R. O. y Verba, S. (1994). *Designing Social Inquiry*. Princeton University Press.
- Cronbach, L. J. (1951). "Coefficient alpha and the internal structure of tests". *Psychometrika*, 16(3), 297–334.
- Muñiz, J. (1998). "Fiabilidad". En *Teoría clásica de los tests* (5.ª ed.). Madrid: Pirámide.
- Prieto, G. y Delgado, A. R. (2010). "Fiabilidad y validez". *Papeles del Psicólogo*, 31(1), 67–74.
- Lincoln, Y. S. y Guba, E. G. (1985). *Naturalistic Inquiry*. Sage.
- Open Science Collaboration (2015). "Estimating the reproducibility of psychological science". *Science*, 349(6251), aac4716.
- McNeish, D. (2018). "Thanks coefficient alpha, we'll take it from here". *Psychological Methods*, 23(3), 412–433.
- Corbetta, P. (2007). *Metodología y técnicas de investigación social*. McGraw-Hill.
- Apuntes UOC, Módulo 2: Procedimientos y decisiones para determinar qué se observará (Sala, Borge, Padró-Solanet).
