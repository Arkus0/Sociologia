---
id: variable-dependiente
title: "Variable dependiente"
note_type: concept
semester: 2026-S1
course: Metodologia de las ciencias sociales
related_concepts:
  - variable-independiente
  - variable-de-control
  - variable-interviniente
  - hipotesis
  - causalidad
  - operacionalizacion
  - diseno-de-investigacion
  - regresion
  - niveles-de-medicion
  - endogeneidad
tags:
  - metodologia
  - variables
  - causalidad
  - diseno-de-investigacion
  - medicion
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\el-proceso-de-formulacion-teorica.md
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\el-proceso-de-investigacion-en-las-ciencias-sociales.md
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\modulo-2.md
updated_at: "2026-04-05"
---

# Variable dependiente

## Definicion

La **variable dependiente** (notacion convencional: *Y*) es aquella propiedad o caracteristica que el investigador busca explicar, predecir o comprender en el marco de una investigacion empirica. En la relacion causal tipica X → Y, la variable dependiente representa el resultado o efecto cuya variacion se atribuye —hipotetica o empiricamente— a una o mas [[variable-independiente|variables independientes]]. Borge Bravo y Padro-Solanet (UOC, Modulo 1) la definen como «lo que se explica» dentro del sistema de variables de una [[hipotesis]].

En la terminologia anglosajona recibe sinonimos segun la tradicion disciplinar: *response variable* (estadistica), *outcome variable* (epidemiologia), *criterion variable* (psicometria), *regressand* (econometria) y *target* o *label* (aprendizaje automatico).

## Origen

La distincion sistematica entre variable dependiente e [[variable-independiente]] en ciencias sociales se consolida a mediados del siglo XX con Paul Lazarsfeld, quien importo al analisis sociologico el «lenguaje de variables» procedente de la estadistica y la psicologia experimental. Lazarsfeld formalizo encuestas y tabulaciones cruzadas que requerian especificar cual era la variable a explicar y cuales las explicativas. Con anterioridad, Durkheim ya habia operado implicitamente con esta logica en *El suicidio* (1897), donde la tasa de suicidio funcionaba como variable dependiente explicada por el grado de integracion social.

## Desarrollo teorico

### La variable dependiente en el diseno de investigacion

Toda [[hipotesis]] especifica al menos una relacion entre una variable independiente (X) y una dependiente (Y), indicando direccion (positiva o negativa) y forma (lineal o curvilinea). La seleccion de la variable dependiente es anterior a la formulacion de hipotesis, pues define la pregunta de investigacion: «¿que queremos explicar?».

### Operacionalizacion y niveles de medicion

La [[operacionalizacion]] de la variable dependiente traduce un concepto abstracto en indicadores empiricos medibles, con una perdida inevitable de contenido teorico. Los [[niveles-de-medicion]] —nominal, ordinal, de intervalo y de razon— determinan las operaciones estadisticas aplicables y condicionan la estrategia analitica del [[diseno-de-investigacion]].

### El marco experimental de Campbell

Donald Campbell sistematizo el papel de la variable dependiente en el diseno experimental y cuasiexperimental. La validez interna depende de que los cambios en Y sean atribuibles exclusivamente a la manipulacion de X, controlando amenazas como la historia o la seleccion diferencial.

### Causalidad y grafos causales

Judea Pearl formalizo las relaciones entre variables mediante grafos aciclicos dirigidos (DAGs). La variable dependiente corresponde al nodo de resultado (*outcome node*), y la identificacion de efectos causales requiere especificar [[variable-de-control|variables de control]] y [[variable-interviniente|variables intervinientes]]. El problema de la [[endogeneidad]] —cuando X e Y se determinan mutuamente o comparten causas no observadas— es un desafio central de la investigacion observacional.

### Popper y el objeto valido de explicacion

Karl Popper subrayo que la ciencia explica regularidades generales, no fenomenos singulares. Un fenomeno constituye una variable dependiente legitima solo cuando puede formularse como una clase de eventos cuya variacion es reproducible y refutable.

## Relacion con otros conceptos

La variable dependiente se situa en el centro de una red conceptual:

- **[[variable-independiente]]**: factor explicativo cuya variacion produce o se asocia con cambios en Y.
- **[[variable-de-control]]**: factor que puede influir en Y y en X simultaneamente; debe neutralizarse para evitar [[relacion-espurea|relaciones espureas]].
- **[[variable-interviniente]]**: mecanismo mediador entre X e Y (X → M → Y).
- **[[hipotesis]]**: enunciado que vincula explicita y formalmente X con Y.
- **[[operacionalizacion]]**: procedimiento que traduce Y de concepto a indicador medible.
- **[[regresion]]**: tecnica estadistica que modela la relacion funcional entre una o mas variables independientes y la variable dependiente.

En modelos complejos es posible trabajar con multiples variables dependientes (analisis multivariado) o con variables que actuan como dependientes en una ecuacion e independientes en otra (ecuaciones estructurales). La moderacion implica que el efecto de X sobre Y cambia segun Z; la mediacion, que X afecta a Y a traves de M.

## Debates y criticas

Un debate recurrente es la adecuacion de la nocion de «dependencia» en contextos de causalidad bidireccional. Algunos autores prefieren *variable de resultado* para evitar la connotacion de pasividad. La tradicion cualitativa cuestiona la reduccion de fenomenos sociales a variables discretas, argumentando que el «lenguaje de variables» fragmenta artificialmente la realidad social. Desde la econometria, la endogeneidad muestra que clasificar una variable como «dependiente» tiene implicaciones tecnicas profundas: la omision de variables relevantes o la causalidad inversa pueden invalidar la inferencia.

## Vigencia contemporanea

En aprendizaje automatico la variable dependiente se reconceptualiza como *target*: el algoritmo busca una funcion que prediga Y a partir de *features*. Sin embargo, capacidad predictiva no equivale a comprension causal. Pearl insiste en que un modelo puede predecir sin explicar, y la variable dependiente ocupa un lugar epistemologico diferente en cada caso. En ciencias sociales computacionales, la disponibilidad de datos digitales masivos plantea nuevos problemas de validez de constructo.

## Ejemplo empirico

En *El suicidio* (1897), Durkheim selecciono la **tasa de suicidio** por pais como variable dependiente. Sus variables independientes incluyeron la confesion religiosa, el estado civil y la integracion social. Mostro que las sociedades protestantes presentaban tasas mas elevadas que las catolicas. La variable fue operacionalizada como suicidios por millon de habitantes, un indicador de intervalo que permitia la comparacion cuantitativa entre unidades.

## Vease tambien

- [[variable-independiente]]
- [[variable-de-control]]
- [[variable-interviniente]]
- [[hipotesis]]
- [[causalidad]]
- [[operacionalizacion]]
- [[diseno-de-investigacion]]
- [[regresion]]
- [[endogeneidad]]
- [[niveles-de-medicion]]

## Fuentes

- Borge Bravo, R. y Padro-Solanet, A. *El proceso de investigacion en las ciencias sociales*. UOC, Modulo 1.
- Borge Bravo, R. y Padro-Solanet, A. *El proceso de formulacion teorica*. UOC (codigo 66239).
- Durkheim, E. (1897). *Le Suicide*. Paris: Felix Alcan.
- Lazarsfeld, P. (1955). «Interpretation of Statistical Relations as a Research Operation». En Lazarsfeld y Rosenberg (eds.), *The Language of Social Research*.
- Campbell, D. y Stanley, J. (1963). *Experimental and Quasi-Experimental Designs for Research*. Chicago: Rand McNally.
- Pearl, J. (2009). *Causality: Models, Reasoning, and Inference*. 2.ª ed. Cambridge University Press.
- Popper, K. (1959). *The Logic of Scientific Discovery*. London: Hutchinson.
- King, G., Keohane, R. y Verba, S. (1994). *Designing Social Inquiry*. Princeton University Press.
- «Dependent and independent variables». *Wikipedia*. Consultado el 5 de abril de 2026.
