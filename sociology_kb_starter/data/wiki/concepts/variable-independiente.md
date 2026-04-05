---
id: variable-independiente
title: "Variable independiente"
note_type: concept
semester: 2026-S1
course: Metodologia de las ciencias sociales
related_concepts:
  - variable-dependiente
  - variable-de-control
  - variable-interviniente
  - hipotesis
  - causalidad
  - operacionalizacion
  - experimento
  - endogeneidad
  - regresion
tags:
  - Metodologia de las ciencias sociales
  - Variables
  - Causalidad
  - Diseno de investigacion
  - Analisis multivariante
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\el-proceso-de-formulacion-teorica.md
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\el-proceso-de-investigacion-en-las-ciencias-sociales.md
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\modulo-2.md
updated_at: "2026-04-05"
---

# Variable independiente

## Definicion

La **variable independiente** (VI) es el factor que el investigador hipotetiza como causa o explicacion de la variacion observada en la [[variable-dependiente]]. En notacion convencional se designa como *X*, de modo que la [[hipotesis]] basica adopta la forma «X → Y». En un [[experimento]] clasico, la VI es el tratamiento que el investigador manipula deliberadamente; en estudios observacionales, es la caracteristica seleccionada cuyo efecto sobre Y se desea estimar. Paul Lazarsfeld la denomino *test factor* dentro de su esquema de elaboracion de relaciones estadisticas, porque es la variable cuyo efecto se «pone a prueba» controlando terceros factores.

La VI recibe multiples sinonimos: *predictor* en modelizacion estadistica, *variable explicativa* en econometria, *regresor* en [[regresion]] lineal y *tratamiento* en diseno experimental. Pese a la diversidad terminologica, la logica subyacente es la misma: la VI es el antecedente teorico desde el cual se pretende explicar la variacion del resultado.

## Origen

El concepto se consolida en la tradicion experimental moderna con Ronald A. Fisher, quien formalizo la **aleatorizacion** como garantia de que la asignacion de sujetos al grupo tratamiento o control no esta contaminada por variables no observadas. La aleatorizacion convierte a la VI en exogena —es decir, libre de correlacion con el termino de error— y permite interpretaciones causales robustas. Karl Popper subrayo que la VI debe quedar especificada *antes* del contraste empirico; de lo contrario, la hipotesis pierde su caracter refutable y cae en la confirmacion *post hoc*.

En las ciencias sociales, Lazarsfeld y sus colaboradores de la Universidad de Columbia sistematizaron el analisis de variables en la decada de 1940, introduciendo la distincion operativa entre VI, [[variable-dependiente]], [[variable-de-control]] y [[variable-interviniente]]. Este vocabulario paso a ser estandar en manuales de metodologia como los empleados en la asignatura (Borge y Padro-Solanet, Manheim y Rich, King, Keohane y Verba).

## Desarrollo teorico

La variable independiente ocupa una posicion central en al menos cuatro marcos metodologicos:

1. **Diseno experimental (Campbell y Stanley).** Donald Campbell establecio los criterios de validez interna y externa. La VI es el tratamiento cuyo efecto neto se aisla mediante grupos de control y aleatorizacion.

2. **Analisis multivariante.** Cuando se incluyen multiples VI (X₁, X₂, … Xₖ) en un modelo de [[regresion]], cada coeficiente estima el efecto parcial manteniendo constantes las demas. El **sesgo por variable omitida** surge cuando una variable relevante queda fuera del modelo y correlaciona con alguna VI incluida.

3. **Variables instrumentales (Angrist y Pischke).** Cuando la VI es endogena, se recurre a una variable instrumental: un factor que afecta a Y *solo* a traves de X. Esta tecnica ha revolucionado la inferencia causal en economia y sociologia cuantitativa.

4. **Grafos causales (Judea Pearl).** Pearl reformulo la VI mediante el concepto de *intervencion* (operador *do*). En un grafo dirigido aciclico, intervenir sobre X equivale a fijar su valor eliminando las flechas entrantes, lo que permite distinguir correlacion de [[causalidad]] genuina.

## Relacion con otros conceptos

La VI no opera de forma aislada. Su efecto sobre Y puede estar mediado por una [[variable-interviniente]] (X → M → Y) o confundido por una [[variable-de-control]] que influye simultaneamente en X e Y. El proceso de [[operacionalizacion]] transforma la VI abstracta en indicadores medibles: por ejemplo, la VI «nivel educativo» puede operacionalizarse como anos de escolaridad, nivel de titulo o puntaje en pruebas estandarizadas. La formulacion correcta de una [[hipotesis]] exige que se especifique la VI, la variable dependiente, la direccion de la relacion (positiva o negativa) y preferiblemente su forma funcional (lineal, curvilinea).

## Debates y criticas

Friedrich Hayek advirtio sobre la **dificultad de aislar variables** en sistemas sociales complejos, donde multiples causas interactuan de forma no lineal y los fenomenos emergentes no se reducen a la suma de efectos individuales. La critica cualitativa, por su parte, cuestiona que la realidad social pueda descomponerse en «variables» discretas. Autores interpretativos argumentan que la pretension de manipular o controlar la VI importa un modelo mecanicista propio de las ciencias naturales que distorsiona procesos sociales inherentemente reflexivos y significativos.

Desde la propia tradicion cuantitativa, el debate sobre [[endogeneidad]] ha mostrado que muchas relaciones presentadas como causales son en realidad espureas. La proliferacion de controles estadisticos no siempre resuelve el problema; de ahi el auge de los disenos cuasiexperimentales, los experimentos naturales y las variables instrumentales como estrategias para recuperar la exogeneidad de la VI.

## Vigencia contemporanea

En la investigacion social actual, la VI sigue siendo el pilar del diseno de investigacion. Los metodos de inferencia causal —diferencias en diferencias, regresion discontinua, emparejamiento por puntaje de propension— se articulan en torno a si la VI es genuinamente exogena. La *credibility revolution* (Angrist, Pischke) ha elevado los estandares, exigiendo que toda VI supuesta causa se acompane de una estrategia explicita de identificacion. En ciencia de datos, la VI se denomina *feature*; la distincion entre variables que explican y variables que meramente predicen sigue siendo metodologicamente crucial.

## Ejemplo empirico

Supongase que se investiga si la participacion en programas de formacion laboral (VI = X) reduce el desempleo (VD = Y). En un [[experimento]] aleatorizado, se asigna a un grupo al programa y a otro como control. La aleatorizacion garantiza comparabilidad, de modo que la diferencia en tasas de desempleo puede atribuirse causalmente a la VI. Si la asignacion no es aleatoria, la [[endogeneidad]] amenaza: quienes se inscriben voluntariamente pueden ser mas motivados. En ese caso, podria emplearse una variable instrumental —la distancia al centro de formacion— para aislar el efecto causal.

## Vease tambien

- [[variable-dependiente]]
- [[variable-de-control]]
- [[variable-interviniente]]
- [[hipotesis]]
- [[causalidad]]
- [[experimento]]
- [[endogeneidad]]
- [[regresion]]
- [[operacionalizacion]]

## Fuentes

- [[el-proceso-de-formulacion-teorica]] — Borge y Padro-Solanet. Variables, hipotesis y causalidad en el proceso de formulacion teorica.
- [[el-proceso-de-investigacion-en-las-ciencias-sociales]] — Borge y Padro-Solanet. Marco teorico, diseno empirico, operacionalizacion de variables.
- Fisher, R. A. (1935). *The Design of Experiments*. Oliver & Boyd.
- Campbell, D. T. y Stanley, J. C. (1963). *Experimental and Quasi-Experimental Designs for Research*. Houghton Mifflin.
- Lazarsfeld, P. F. (1955). «Interpretation of Statistical Relations as a Research Operation». En Lazarsfeld y Rosenberg (eds.), *The Language of Social Research*.
- Angrist, J. D. y Pischke, J.-S. (2009). *Mostly Harmless Econometrics*. Princeton University Press.
- Pearl, J. (2009). *Causality: Models, Reasoning, and Inference*. 2.ª ed. Cambridge University Press.
- Popper, K. R. (1959). *The Logic of Scientific Discovery*. Hutchinson.
- Hayek, F. A. (1964). «The Theory of Complex Phenomena». En *Studies in Philosophy, Politics and Economics*.
