---
id: grupo-de-control
title: Grupo de control
note_type: concept
semester: 2026-S1
course: "Metodología de las ciencias sociales"
related_concepts:
  - grupo-experimental
  - experimento
  - cuasiexperimento
  - validez-interna
  - diseno-de-investigacion
  - variable-independiente
  - aleatorizacion
tags:
  - metodología
  - diseño-experimental
  - causalidad
  - investigación-cuantitativa
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\la-investigacion-cuantitativa.md
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\modulo-3.md
updated_at: "2025-07-13"
---

## Definición

El **grupo de control** es el conjunto de sujetos o unidades de observación que, en el marco de un [[experimento]] o ensayo controlado, **no recibe el tratamiento, estímulo o intervención** cuyo efecto se pretende evaluar. Su función primordial consiste en servir como referencia contrafáctica: permite estimar qué habría ocurrido en ausencia de la [[variable-independiente]] manipulada, de modo que cualquier diferencia observada entre el grupo de control y el [[grupo-experimental]] pueda atribuirse causalmente al estímulo y no a factores extraños. La lógica subyacente es que, si ambos grupos son equivalentes en todas las variables relevantes salvo en la exposición al tratamiento, la comparación de resultados aísla el efecto neto de la intervención.

Formalmente, el efecto del estímulo se calcula como:

$$
\text{Efecto} = (O_{2E} - O_{1E}) - (O_{2C} - O_{1C})
$$

donde $E$ es el grupo experimental, $C$ el grupo de control, $O_1$ la verificación anterior y $O_2$ la verificación posterior (Manheim y Rich, 1988).

## Origen y contexto histórico

La idea de comparar un grupo tratado con uno no tratado tiene antecedentes en la medicina del siglo XVIII —James Lind y su ensayo sobre el escorbuto (1747)—, pero su formalización estadística se debe a **Ronald A. Fisher**. En *The Design of Experiments* (1935), Fisher sistematizó los principios de **aleatorización**, **replicación** y **control** que constituyen la base del diseño experimental moderno. La asignación aleatoria de los sujetos a los grupos garantiza, en valor esperado, la equivalencia de todas las variables de confusión, tanto las observadas como las no observadas.

En las ciencias sociales, la adopción del grupo de control fue más tardía y problemática. **Campbell y Stanley** (1963) distinguieron entre diseños experimentales puros —con asignación aleatoria y grupo de control— y [[cuasiexperimento|cuasiexperimentos]], en los que la aleatorización no es factible pero se recurre a estrategias de control estadístico o de emparejamiento para aproximar la lógica contrafáctica.

## Desarrollo teórico

El grupo de control opera bajo la **lógica contrafáctica** de la inferencia causal: para afirmar que $X$ causa $Y$, es necesario demostrar que, en ausencia de $X$, $Y$ no se habría producido (o lo habría hecho en menor medida). Esta noción enlaza con el **modelo de resultados potenciales** de Rubin (1974), donde cada unidad posee dos resultados posibles —con y sin tratamiento— y el efecto causal individual es la diferencia entre ambos. Dado que solo uno de los dos resultados es observable para cada sujeto (el «problema fundamental de la inferencia causal»), el grupo de control proporciona la estimación del resultado medio no observado.

### Modalidades de grupo de control

- **Control con placebo**: el grupo de control recibe una intervención inerte (un placebo) para neutralizar el [[efecto-placebo]] y mantener el cegamiento.
- **Control con lista de espera** (*waitlist control*): los sujetos del grupo de control reciben el tratamiento después de concluida la fase experimental, lo que mitiga objeciones éticas.
- **Control activo**: el grupo recibe un tratamiento alternativo estándar, de modo que se evalúa la superioridad relativa de la nueva intervención.
- **Control histórico**: se emplean datos de períodos anteriores como referencia, aunque este diseño es más vulnerable a amenazas a la [[validez-interna]].

## Relación con otros conceptos

El grupo de control es inseparable del [[grupo-experimental]]: juntos conforman la estructura mínima de un [[diseno-de-investigacion]] experimental. La **asignación aleatoria** ([[aleatorizacion]]) es el mecanismo que asegura la equivalencia inicial entre ambos grupos respecto a variables de confusión (género, edad, nivel educativo, etc.). Cuando la aleatorización no es posible —por ejemplo, en estudios observacionales o en políticas públicas ya implementadas—, se recurre a diseños cuasiexperimentales que intentan reconstruir la lógica del grupo de control mediante técnicas como la diferencia en diferencias, el emparejamiento por puntaje de propensión o la regresión discontinua.

El concepto se vincula directamente con la [[validez-interna]]: cuanto más riguroso es el control de variables extrañas, mayor es la confianza en que la diferencia entre grupos refleja el efecto del tratamiento y no artefactos metodológicos.

## Debates y críticas

### Dilemas éticos en la experimentación social

La asignación de seres humanos a un grupo de control plantea interrogantes éticos ineludibles. Negar deliberadamente un tratamiento potencialmente beneficioso —por ejemplo, un programa educativo o una transferencia económica— a un grupo de personas para servir como referencia empírica ha sido objeto de controversia. Los comités de ética exigen que el diseño incluya salvaguardas: consentimiento informado, análisis interinos y la posibilidad de interrumpir el ensayo si los resultados preliminares muestran un beneficio o daño claro.

### Límites de la experimentación social: la objeción hayekiana

Desde una perspectiva epistemológica, **Friedrich Hayek** argumentó que la complejidad de los fenómenos sociales —con su multiplicidad de variables interrelacionadas y su carácter histórico irrepetible— impone límites estructurales a la experimentación controlada. Para Hayek, la pretensión de replicar en las ciencias sociales la lógica del laboratorio ignora la naturaleza emergente y autoorganizativa del orden social.

### Validez externa frente a validez interna

Un diseño con grupo de control estricto maximiza la [[validez-interna]], pero puede sacrificar **validez externa**: las condiciones controladas del experimento pueden diferir tanto del entorno natural que los resultados no sean generalizables. Campbell y Stanley (1963) señalaron esta tensión como inherente a todo diseño experimental.

## Vigencia contemporánea

La revolución de los **ensayos controlados aleatorizados** (*Randomized Controlled Trials*, RCT) en economía del desarrollo, impulsada por **Abhijit Banerjee** y **Esther Duflo** (Premio Nobel de Economía 2019), ha revitalizado el uso del grupo de control en las ciencias sociales. A través del *Abdul Latif Jameel Poverty Action Lab* (J-PAL), se han realizado cientos de RCTs para evaluar intervenciones en educación, salud, microfinanzas y gobernanza en países en desarrollo. Los grupos de control en estos estudios suelen ser comunidades o individuos que reciben el tratamiento en una fase posterior (diseño de lista de espera), lo que atenúa —sin eliminar— los dilemas éticos.

En el ámbito de las políticas públicas basadas en evidencia (*evidence-based policy*), el grupo de control se ha convertido en el estándar de referencia para evaluar programas sociales, desde transferencias condicionadas de ingresos hasta intervenciones de salud pública.

## Ejemplo empírico

En los estudios citados en el material del curso, se describen experimentos realizados en escuelas inglesas para evaluar el efecto de programas de contenido violento en la agresividad infantil (niños de 7 a 10 años). El [[grupo-experimental]] fue expuesto al contenido violento, mientras que el grupo de control no lo recibió. Se controlaron variables como género, clase social y tipo de escuela, de modo que la composición de ambos grupos fuese idéntica en todos los factores salvo el estímulo. La comparación de las mediciones pre y post intervención permitió aislar el efecto causal del contenido violento sobre la conducta agresiva (Iyengar y Kinder, 1987; material del módulo 3).

## Véase también

- [[grupo-experimental]]
- [[experimento]]
- [[cuasiexperimento]]
- [[validez-interna]]
- [[diseno-de-investigacion]]
- [[variable-independiente]]
- [[aleatorizacion]]
- [[efecto-placebo]]

## Fuentes

- Fisher, R. A. (1935). *The Design of Experiments*. Edinburgh: Oliver & Boyd.
- Campbell, D. T. y Stanley, J. C. (1963). *Experimental and Quasi-Experimental Designs for Research*. Chicago: Rand McNally.
- Rubin, D. B. (1974). "Estimating Causal Effects of Treatments in Randomized and Nonrandomized Studies". *Journal of Educational Psychology*, 66(5), 688-701.
- Banerjee, A. V. y Duflo, E. (2011). *Poor Economics: A Radical Rethinking of the Way to Fight Global Poverty*. New York: PublicAffairs.
- Hayek, F. A. (1952). *The Counter-Revolution of Science*. Glencoe: Free Press.
- Manheim, J. B. y Rich, R. C. (1988). *Empirical Political Analysis: Research Methods in Political Science*. Nueva York: Longman.
- Iyengar, S. y Kinder, D. (1987). *News that Matters: Television and American Opinion*. Chicago: University of Chicago Press.
- Material del curso: Módulo 3, *Metodología de las ciencias sociales*, 2026-S1.
