---
id: cuasiexperimento
title: Cuasiexperimento
note_type: concept
semester: 2026-S1
course: "Metodologia de las ciencias sociales"
related_concepts:
  - experimento
  - validez-interna
  - validez-externa
  - grupo-de-control
  - grupo-experimental
  - diseno-de-investigacion
  - variable-independiente
  - causalidad
tags:
  - metodología
  - diseño-de-investigación
  - causalidad
  - método-cuantitativo
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\modulo-3.md
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\la-investigacion-cuantitativa.md
updated_at: '2025-07-13'
---

## Definición

Un **cuasiexperimento** es un diseño de investigación empírica que busca estimar el impacto causal de una intervención o tratamiento sobre una población objetivo sin recurrir a la [[asignacion-aleatoria]] de los sujetos a los grupos de estudio. A diferencia del [[experimento]] clásico de laboratorio —donde el investigador asigna aleatoriamente las unidades al [[grupo-experimental]] y al [[grupo-de-control]]—, el cuasiexperimento emplea criterios no aleatorios (puntuaciones de corte, autoselección, asignación administrativa) para distribuir a los participantes. Philip Babcock y otros lo caracterizan como un «experimento sobre el terreno» (*field experiment*), típico de las ciencias sociales, en el que se sacrifica parte del control experimental a cambio de mayor realismo y viabilidad ética.

La fórmula básica de efecto se conserva: **Efecto = (post_E − pre_E) − (post_C − pre_C)**, pero al no poder garantizar la equivalencia inicial de los grupos mediante aleatorización, el cuasiexperimento queda sujeto a amenazas a la [[validez-interna]] que el investigador debe abordar con técnicas estadísticas y de diseño específicas.

## Origen y contexto histórico

El término fue acuñado formalmente por Donald T. Campbell y Julian C. Stanley en su influyente monografía *Experimental and Quasi-Experimental Designs for Research* (1963), donde sistematizaron las amenazas a la validez interna y externa de los diseños experimentales y propusieron alternativas para contextos donde la aleatorización resultaba impracticable. Campbell, psicólogo social preocupado por la evaluación de programas educativos y de políticas públicas, reconoció que las ciencias sociales rara vez podían reproducir las condiciones de un laboratorio y que, no obstante, necesitaban herramientas rigurosas para inferir relaciones causales.

La tradición fue consolidada cuatro décadas después por William R. Shadish, Thomas D. Cook y el propio Campbell en *Experimental and Quasi-Experimental Designs for Generalized Causal Inference* (2002), obra de referencia que amplió la taxonomía de diseños y formalizó los criterios para evaluar la [[validez-externa]] de los hallazgos cuasiexperimentales.

## Desarrollo teórico

### Lógica del diseño

El cuasiexperimento comparte con el [[experimento]] la presencia de una [[variable-independiente]] manipulada (o, al menos, identificada como causa hipotética), una variable dependiente medida y un grupo de comparación. Lo que lo distingue es la ausencia de aleatorización, lo cual obliga a emplear estrategias compensatorias para aislar el efecto causal.

### Principales diseños cuasiexperimentales

1. **Diferencia en diferencias** (*difference-in-differences*, DiD): compara la evolución temporal de un grupo tratado y un grupo de control antes y después de la intervención. Supone que, en ausencia de tratamiento, ambos grupos habrían seguido trayectorias paralelas.
2. **Regresión discontinua** (*regression discontinuity design*, RDD): explota un umbral o puntuación de corte que determina la asignación al tratamiento, comparando unidades justo por encima y por debajo de dicho umbral. Es considerado el diseño cuasiexperimental con mayor [[validez-interna]], pues produce estimaciones insesgadas del efecto local del tratamiento.
3. **Variables instrumentales** (*instrumental variables*, IV): identifica una variable exógena (el «instrumento») que afecta la probabilidad de recibir el tratamiento pero no tiene efecto directo sobre el resultado, permitiendo aislar la variación exógena en la asignación.
4. **Series temporales interrumpidas**: observa la variable dependiente a lo largo de múltiples puntos temporales antes y después de la intervención para detectar cambios en nivel o tendencia.
5. **Pareamiento por puntaje de propensión** (*propensity score matching*): construye pares estadísticamente equivalentes de unidades tratadas y no tratadas según la probabilidad estimada de recibir el tratamiento.

### Amenazas a la validez interna

Campbell y Stanley identificaron amenazas clásicas: historia (eventos externos concurrentes), maduración, regresión a la media, selección diferencial, mortalidad experimental e interacción entre selección y maduración. Shadish, Cook y Campbell (2002) ampliaron esta lista y enfatizaron que cada diseño cuasiexperimental posee un perfil específico de amenazas que el investigador debe evaluar.

## Relación con otros conceptos

El cuasiexperimento se sitúa en un continuo de [[diseno-de-investigacion]] que va del [[experimento]] aleatorizado (máximo control, alta [[validez-interna]]) a los estudios observacionales (mayor realismo, alta [[validez-externa]]). Según los materiales del módulo 3 de Metodología, los factores de control —edad, género, nivel educativo— deben ser lo más homogéneos posible entre el [[grupo-experimental]] y el [[grupo-de-control]], aunque en el cuasiexperimento «no suele haber un verdadero control de la variable independiente ni de las condiciones en las que actúan las variables» (Borge y Padró-Solanet).

Karl Popper sostuvo que la ciencia avanza mediante la [[falsacion]] de hipótesis; el cuasiexperimento, al no poder controlar todas las variables confusoras, dificulta —aunque no imposibilita— la refutación limpia de hipótesis causales, razón por la cual Popper privilegió el experimento estricto como piedra de toque del método científico.

## Debates y críticas

El debate central concierne a la **inferencia causal**: ¿puede un cuasiexperimento establecer relaciones causales con la misma solidez que un experimento aleatorizado? Los puristas experimentales, como recordó Campbell, los denominaron «experimentos mareantes» (*queasy experiments*), señalando que la ausencia de aleatorización deja siempre abierta la posibilidad de sesgos de selección y variables de confusión no observadas.

Friedrich Hayek, desde la tradición liberal austriaca, advirtió sobre los límites de la experimentación social planificada: la complejidad de los fenómenos sociales y la imposibilidad de replicar condiciones controladas a escala societal vuelven problemática toda pretensión de ingeniería social basada en resultados cuasiexperimentales. Esta cautela resuena en el debate contemporáneo sobre la evaluación de políticas públicas.

No obstante, Joshua Angrist y Jörn-Steffen Pischke, en *Mostly Harmless Econometrics* (2009), defendieron vigorosamente el uso de «experimentos naturales» —situaciones en las que una asignación cuasi-aleatoria surge de circunstancias institucionales o históricas— como fuente legítima de identificación causal en economía y ciencias sociales. Su trabajo popularizó las técnicas de variables instrumentales y regresión discontinua como estándares de rigor empírico.

## Vigencia contemporánea

Los diseños cuasiexperimentales dominan hoy la evaluación de políticas públicas, la economía del desarrollo y la epidemiología social. La «revolución de la credibilidad» en economía empírica —reconocida con el Premio Nobel de Economía 2021 a David Card, Joshua Angrist y Guido Imbens— se basa fundamentalmente en el perfeccionamiento de técnicas cuasiexperimentales: diferencia en diferencias, variables instrumentales y regresión discontinua.

En sociología, los cuasiexperimentos permiten evaluar el impacto de reformas educativas, programas de transferencias condicionadas, intervenciones de salud pública y cambios legislativos, combinando el rigor analítico con la viabilidad ética que exige la investigación con seres humanos.

## Ejemplo empírico

Un caso paradigmático es el estudio de David Card (1990) sobre el efecto de la inmigración en los salarios locales, utilizando el éxodo del Mariel (1980) como «experimento natural». La llegada masiva e inesperada de cubanos a Miami proporcionó una variación exógena en la oferta de trabajo que Card comparó con ciudades de control similares mediante un diseño de diferencia en diferencias. El estudio concluyó que el influjo migratorio no redujo significativamente los salarios ni el empleo de los trabajadores nativos, resultado que desafió las predicciones de los modelos de oferta y demanda simples y demostró el poder del diseño cuasiexperimental para abordar cuestiones causales en contextos no experimentales.

## Véase también

- [[experimento]]
- [[validez-interna]]
- [[validez-externa]]
- [[grupo-de-control]]
- [[grupo-experimental]]
- [[diseno-de-investigacion]]
- [[variable-independiente]]
- [[causalidad]]
- [[inferencia-cientifica]]
- [[muestra]]

## Fuentes

- Campbell, D. T. y Stanley, J. C. (1963). *Experimental and Quasi-Experimental Designs for Research*. Chicago: Rand McNally.
- Shadish, W. R., Cook, T. D. y Campbell, D. T. (2002). *Experimental and Quasi-Experimental Designs for Generalized Causal Inference*. Boston: Houghton Mifflin.
- Angrist, J. D. y Pischke, J.-S. (2009). *Mostly Harmless Econometrics: An Empiricist's Companion*. Princeton: Princeton University Press.
- Card, D. (1990). «The Impact of the Mariel Boatlift on the Miami Labor Market». *Industrial and Labor Relations Review*, 43(2), 245-257.
- Corbetta, P. (2003). «Causalidad y experimento». En: *Metodologías y técnicas de investigación social* (cap. 3, págs. 115-156). Madrid: McGraw-Hill.
- Borge, R. y Padró-Solanet, A. (2026). *Metodología de las ciencias sociales*, Módulo 3: «La investigación cuantitativa». Barcelona: UOC.
