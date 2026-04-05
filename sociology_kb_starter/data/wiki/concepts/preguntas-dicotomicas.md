---
id: preguntas-dicotomicas
title: Preguntas dicotómicas
note_type: concept
semester: 2026-S1
course: "Metodologia de las ciencias sociales"
related_concepts:
  - cuestionario
  - preguntas-abiertas-y-cerradas
  - niveles-de-medicion
  - regresion
  - variable-dependiente
  - fiabilidad
  - tabla-de-contingencia
  - codificacion
tags:
  - Metodologia de las ciencias sociales
  - Cuestionario
  - Encuesta
  - Medición
  - Variables
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\cuaderno-metodologico-cuestionarios.md
updated_at: '2025-07-13'
---

# Preguntas dicotómicas

## Definición

Las **preguntas dicotómicas** son un tipo de pregunta cerrada que ofrece al encuestado únicamente dos opciones de respuesta mutuamente excluyentes y exhaustivas: típicamente «Sí / No», «De acuerdo / En desacuerdo», «Verdadero / Falso» o «Hombre / Mujer». El término proviene del griego *dichotomía* (διχοτομία), que significa «división en dos partes». En el marco de la [[operacionalizacion|operacionalización]] de variables, la pregunta dicotómica genera una **variable binaria** o **variable dummy** que adopta los valores 0 y 1, situándose en el [[niveles-de-medicion|nivel de medición nominal]] más elemental. María José Azofra, en los *Cuadernos Metodológicos* del CIS, las clasifica dentro de la tipología por tipo de respuesta junto a las preguntas categorizadas, de escala numérica y de valoración.

## Origen y contexto histórico

El uso sistemático de preguntas con respuesta binaria se remonta a los primeros censos modernos y a las encuestas de opinión pública del siglo XIX. Charles Booth, en sus estudios sobre la pobreza en Londres (1886-1903), ya empleaba clasificaciones dicotómicas (pobre / no pobre) para mapear las condiciones de vida. Sin embargo, la formalización estadística de la variable dicotómica cobró impulso con la expansión de la investigación por [[encuesta]] en el siglo XX, especialmente a partir de los trabajos de Paul Lazarsfeld en la Bureau of Applied Social Research de la Universidad de Columbia durante las décadas de 1940 y 1950. La incorporación de las *dummy variables* en modelos de [[regresion|regresión]] fue sistematizada por Daniel B. Suits en 1957, quien demostró cómo incluir atributos cualitativos en ecuaciones de regresión mediante variables indicadoras codificadas con valores 0 y 1.

## Desarrollo teórico

Desde la perspectiva del diseño de [[cuestionario|cuestionarios]], las preguntas dicotómicas constituyen la forma más simple de pregunta cerrada. Azofra las distingue de las preguntas categorizadas u ordinales, que ofrecen múltiples opciones ordenadas, y de las [[preguntas-de-escala|preguntas de escala]] numérica, que solicitan una autoubicación en un continuo. Su lógica de construcción se apoya en varios principios:

1. **Exhaustividad**: las dos categorías deben cubrir todo el espectro posible de respuestas (de ahí que se añada con frecuencia la opción «No sabe / No contesta»).
2. **Exclusividad mutua**: el encuestado debe poder situarse inequívocamente en una sola categoría.
3. **Codificación inmediata**: al generar una variable binaria (0/1), la [[codificacion|codificación]] y el análisis estadístico resultan directos y no requieren [[precodificacion|precodificación]] compleja.

En el análisis cuantitativo, la variable resultante opera como **variable dummy** (*indicator variable*). En un modelo de [[regresion|regresión lineal múltiple]], el coeficiente asociado a una dummy estima la diferencia media en la variable dependiente entre la categoría codificada como 1 y la categoría de referencia (codificada como 0), controlando por las demás variables del modelo. Cuando la propia [[variable-dependiente|variable dependiente]] es dicotómica —por ejemplo, «¿Votó usted en las últimas elecciones?»— se recurre a la **regresión logística**, que modela la probabilidad de que el evento ocurra.

La fiabilidad de los ítems dicotómicos se evalúa mediante los coeficientes de **Kuder-Richardson** (KR-20 y KR-21), análogos al alfa de Cronbach pero diseñados específicamente para ítems con respuesta binaria. En el análisis bivariante, el cruce de dos variables dicotómicas produce una [[tabla-de-contingencia|tabla de contingencia]] de 2 × 2, sobre la cual se calculan la **Q de Yule** y el **coeficiente phi** (φ) como medidas de asociación.

## Relación con otros conceptos

Las preguntas dicotómicas se insertan en una red de conceptos metodológicos estrechamente vinculados:

- **[[preguntas-abiertas-y-cerradas|Preguntas abiertas y cerradas]]**: las dicotómicas son el caso extremo de pregunta cerrada, con el menor número posible de categorías de respuesta.
- **[[niveles-de-medicion|Niveles de medición]]**: generan datos nominales (presencia/ausencia), aunque cuando implican orden implícito (mejor/peor) pueden aproximarse al nivel ordinal.
- **[[cuestionario|Cuestionario]]**: dentro de la estructura del cuestionario, las dicotómicas funcionan a menudo como [[preguntas-filtro|preguntas filtro]] que derivan al encuestado hacia bloques específicos de preguntas.
- **[[regresion|Regresión]]** y **[[variable-dependiente|variable dependiente]]**: como variables independientes dummy o como variable dependiente en modelos logísticos.
- **[[fiabilidad|Fiabilidad]]**: los coeficientes KR-20/KR-21 son el estándar para medir la consistencia interna de conjuntos de ítems dicotómicos.

## Debates y críticas

La principal crítica a las preguntas dicotómicas radica en la **pérdida de información**. Al reducir fenómenos complejos a dos categorías, se sacrifica la variabilidad y el matiz propios de las actitudes, opiniones y comportamientos sociales. Esta simplificación puede introducir un **sesgo de elección forzada** (*forced-choice bias*): los encuestados con posiciones intermedias o ambivalentes se ven obligados a elegir una opción que no refleja fielmente su posición, lo que puede distorsionar las distribuciones de respuesta.

Un segundo debate concierne a la **deseabilidad social**: en preguntas dicotómicas sensibles (e.g., «¿Ha consumido drogas ilegales?»), la respuesta binaria no ofrece matices que atenúen la presión social, lo que puede elevar la tasa de respuestas socialmente aceptables. Técnicas como la *randomized response* se han propuesto para mitigar este problema.

Desde la estadística, el uso excesivo de variables dummy en modelos de regresión puede generar la denominada **trampa de la variable dummy** (*dummy variable trap*): si se incluyen indicadores para todas las categorías de una variable, se produce multicolinealidad perfecta, lo que impide la estimación del modelo. La solución estándar consiste en omitir una categoría de referencia.

## Vigencia contemporánea

A pesar de las críticas, las preguntas dicotómicas siguen siendo omnipresentes en la investigación social contemporánea. Los grandes barómetros del CIS, la Encuesta Social Europea (ESS) y la World Values Survey emplean sistemáticamente ítems dicotómicos, particularmente para variables sociodemográficas básicas y comportamientos factuales (votó / no votó, trabaja / no trabaja). En el ámbito del *machine learning* y la ciencia de datos, la codificación *one-hot encoding* generaliza la lógica de la variable dummy a variables categóricas con múltiples niveles, creando múltiples columnas binarias. Además, el auge de las encuestas digitales y los formularios en línea ha reforzado su uso, dada la facilidad de implementación y la rapidez de respuesta que ofrecen los formatos de «Sí / No» en dispositivos móviles.

## Ejemplo empírico

En el Barómetro del CIS de abril de 2024, la pregunta «¿Fue usted a votar en las últimas elecciones generales?» ilustra el uso paradigmático de una pregunta dicotómica. La respuesta (Sí = 1, No = 0) genera una variable binaria que permite: (a) calcular la tasa de participación declarada de la muestra; (b) cruzarla con [[variables-sociodemograficas|variables sociodemográficas]] (edad, nivel educativo, clase social) en [[tabla-de-contingencia|tablas de contingencia]] 2 × *k*; y (c) introducirla como variable dependiente en un modelo de regresión logística para identificar los factores predictivos de la abstención, controlando simultáneamente por ideología, confianza institucional e interés por la política.

## Véase también

- [[cuestionario]]
- [[preguntas-abiertas-y-cerradas]]
- [[niveles-de-medicion]]
- [[regresion]]
- [[variable-dependiente]]
- [[fiabilidad]]
- [[tabla-de-contingencia]]
- [[codificacion]]
- [[preguntas-filtro]]
- [[preguntas-de-escala]]

## Fuentes

- Azofra, M. J. (1999). *Cuadernos Metodológicos 26: Diseño de cuestionarios*. Centro de Investigaciones Sociológicas.
- Suits, D. B. (1957). Use of Dummy Variables in Regression Equations. *Journal of the American Statistical Association*, 52(280), 548-551.
- Draper, N. R. y Smith, H. (1998). *Applied Regression Analysis* (3.ª ed.). Wiley.
- [[cuadernos-metodologicos-cis-26-diseno-de-cuestionarios]] (nota fuente del curso)
