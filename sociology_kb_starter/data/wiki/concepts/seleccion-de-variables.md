---
id: seleccion-de-variables
title: Selección de variables
note_type: concept
semester: 2026-S1
course: "Metodologia de las ciencias sociales"
related_concepts:
  - "[[variable-dependiente]]"
  - "[[variable-independiente]]"
  - "[[variable-de-control]]"
  - "[[omision-de-variables]]"
  - "[[operacionalizacion]]"
  - "[[marco-teorico]]"
  - "[[endogeneidad]]"
  - "[[validez]]"
tags:
  - selección de variables
  - diseño de investigación
  - sesgo de variable omitida
  - inferencia causal
  - metodología
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\modulo-2.md
updated_at: '2025-07-13'
---

## Definición

La **selección de variables** es la decisión metodológica mediante la cual el investigador determina qué propiedades o características del mundo social incluirá como elementos de su análisis empírico. En el marco de la investigación social, esta operación implica identificar cuál será la [[variable-dependiente]] (el fenómeno que se pretende explicar), cuáles serán las [[variable-independiente|variables independientes]] (los factores explicativos) y qué [[variable-de-control|variables de control]] se incorporarán para aislar relaciones espurias. Se trata de un paso anterior a la [[operacionalizacion]] y estrechamente ligado al [[marco-teorico]], pues la teoría orienta qué variables son relevantes y cómo se espera que interactúen entre sí.

Como señalan King, Keohane y Verba (2000), la lógica de la inferencia científica —compartida por métodos cuantitativos y cualitativos— exige que la selección de variables responda a criterios teóricos explícitos, y no a la mera disponibilidad de datos.

## Origen y contexto histórico

La preocupación formal por seleccionar correctamente las variables de un estudio surge con la consolidación del método hipotético-deductivo en las ciencias sociales durante el siglo XX. La tradición positivista clásica, representada por Durkheim y sus *reglas del método sociológico* (1895), ya exigía delimitar "hechos sociales" observables como paso previo al análisis causal. Sin embargo, fue con el desarrollo de la estadística aplicada a las ciencias sociales —especialmente a partir de los trabajos de Lazarsfeld en la Columbia University durante las décadas de 1940 y 1950— cuando la selección de variables se convirtió en un problema técnico formalizado. Lazarsfeld introdujo la distinción entre variables antecedentes, intervinientes y supresoras, sentando las bases del análisis multivariado que hoy estructura buena parte de la investigación empírica.

En décadas más recientes, la revolución causal impulsada por Judea Pearl desde la informática y la estadística ha replanteado la selección de variables como un problema de identificación causal, introduciendo los **grafos acíclicos dirigidos** (DAGs) como herramienta formal para decidir qué variables incluir o excluir de un modelo.

## Desarrollo teórico

La selección de variables opera en la intersección entre teoría y método. Pueden distinguirse dos grandes enfoques:

**Selección guiada por la teoría (*theory-driven*).** El investigador parte de un marco teórico articulado que especifica relaciones causales esperadas y, a partir de ellas, determina qué variables medir. Este enfoque es dominante en las ciencias sociales y se asocia al método hipotético-deductivo: la teoría genera hipótesis, las hipótesis identifican variables, y las variables se operacionalizan en indicadores. Manheim y Rich subrayan que una buena teoría debe permitir derivar hipótesis contrastables, lo cual supone una selección de variables coherente con las proposiciones teóricas.

**Selección guiada por los datos (*data-driven*).** En este caso, el investigador utiliza técnicas estadísticas —como métodos *stepwise*, LASSO o árboles de decisión— para que los propios datos "descubran" qué variables son relevantes. Aunque popular en la minería de datos y el *machine learning*, este enfoque ha sido ampliamente criticado en las ciencias sociales por su propensión al **sobreajuste** (*overfitting*): un modelo puede ajustarse perfectamente a los datos observados pero carecer de capacidad predictiva sobre nuevos casos, precisamente porque captura ruido aleatorio en lugar de relaciones sustantivas.

El módulo de la UOC (Sala, Borge y Padró-Solanet) sistematiza los principales errores asociados a una mala selección de variables:

1. **[[omision-de-variables|Omisión de variables relevantes]]** → produce **sesgo**: el impacto estimado de las variables incluidas se magnifica cuando las variables omitidas están correlacionadas con las incluidas. Este es el célebre *omitted variable bias* de la econometría.
2. **Inclusión de variables irrelevantes** → produce **ineficiencia**: la varianza de los estimadores aumenta, reduciendo la probabilidad de detectar el efecto real. Es especialmente problemática cuando las variables irrelevantes correlacionan con la dependiente.
3. **[[endogeneidad]]**: cuando los valores de las variables explicativas son consecuencia —y no causa— de la dependiente, la dirección causal queda invertida y los resultados son espurios.

## Relación con otros conceptos

La selección de variables es inseparable del [[marco-teorico]], pues es la teoría la que justifica por qué ciertas variables deben incluirse y otras no. Una vez seleccionadas, las variables atraviesan el proceso de [[operacionalizacion]], donde se traducen en indicadores medibles. La [[variable-dependiente]] constituye el fenómeno a explicar; las [[variable-independiente|variables independientes]] representan los factores explicativos; y las [[variable-de-control|variables de control]] permiten neutralizar explicaciones alternativas. La [[omision-de-variables]] es la amenaza más directa derivada de una selección deficiente, mientras que la [[endogeneidad]] constituye un riesgo cuando la cadena causal no está claramente establecida. Finalmente, los criterios de [[validez]] y [[fiabilidad]] operan como condiciones necesarias: de nada sirve seleccionar las variables correctas si los indicadores utilizados no miden lo que pretenden medir.

## Debates y críticas

El debate más persistente gira en torno a la **tensión entre parsimonia y completitud**. Un modelo con pocas variables es más interpretable pero corre riesgo de omitir factores relevantes; un modelo con muchas variables reduce el sesgo de omisión pero incrementa la ineficiencia y el riesgo de sobreajuste.

Los **métodos stepwise** (selección paso a paso, hacia adelante o hacia atrás) han sido duramente criticados por la comunidad estadística. Harrell (2015) argumenta que estos procedimientos inflacionan los errores de tipo I, producen intervalos de confianza demasiado estrechos y generan modelos inestables que varían sustancialmente con pequeños cambios en los datos.

Frente a estas limitaciones, Pearl (2009) propuso el uso de **grafos acíclicos dirigidos (DAGs)** como herramienta para la selección de variables. Los DAGs permiten representar gráficamente las relaciones causales supuestas y, a partir de criterios formales (como el *backdoor criterion*), identificar el conjunto mínimo de variables de control necesario para estimar un efecto causal sin sesgo. Esta aproximación ha ganado influencia creciente en epidemiología, sociología y ciencia política.

Otra línea crítica proviene de la tradición cualitativa: autores como Ragin (1987) argumentan que la selección de variables impone una lógica *variable-centered* que puede ser inadecuada para fenómenos configuracionales, donde importa la combinación específica de factores y no su efecto aditivo individual.

## Vigencia contemporánea

En la investigación social contemporánea, la selección de variables sigue siendo una decisión central del diseño de investigación. La creciente disponibilidad de grandes volúmenes de datos (*big data*) ha intensificado la tentación de incluir todas las variables disponibles, lo que refuerza la importancia de criterios teóricos sólidos. Simultáneamente, el movimiento de *ciencia abierta* y los registros de pre-análisis exigen que los investigadores declaren sus variables *antes* de acceder a los datos, limitando el *data dredging* y fortaleciendo la transparencia metodológica. Los DAGs de Pearl se han consolidado como herramienta estándar en múltiples disciplinas, y paquetes de software como *dagitty* facilitan su aplicación práctica.

## Ejemplo empírico

Un investigador desea explicar la participación electoral en municipios españoles. Su teoría sugiere que la participación ([[variable-dependiente]]) depende del nivel socioeconómico ([[variable-independiente]]) de la población. Sin embargo, omitir la variable "competitividad electoral" —correlacionada tanto con nivel socioeconómico como con participación— produciría un sesgo de variable omitida: el efecto estimado del nivel socioeconómico absorbería parte del efecto de la competitividad. Para evitarlo, la competitividad debe incluirse como [[variable-de-control]]. Si, además, el investigador incluyera decenas de variables demográficas sin fundamento teórico (densidad de farmacias, temperatura media, etc.), aumentaría la varianza de los estimadores sin mejorar la explicación, incurriendo en el problema de inclusión de variables irrelevantes. Un DAG permitiría representar gráficamente estas relaciones y determinar el conjunto de controles adecuado.

## Véase también

- [[seleccion-de-casos]]
- [[diseno-de-investigacion]]
- [[inferencia-cientifica]]
- [[multicolinealidad]]
- [[hipotesis]]
- [[sobredeterminacion]]

## Fuentes

- King, G., Keohane, R. y Verba, S. (2000). *El diseño de la investigación social*. Madrid: Alianza.
- Sala, G., Borge, R. y Padró-Solanet, A. — [[procedimientos-y-decisiones-para-determinar-que-se-observara]] (Metodologia de las ciencias sociales, UOC).
- Pearl, J. (2009). *Causality: Models, Reasoning, and Inference* (2.ª ed.). Cambridge University Press.
- Harrell, F. E. (2015). *Regression Modeling Strategies* (2.ª ed.). Springer.
- Ragin, C. (1987). *The Comparative Method*. University of California Press.
- Lazarsfeld, P. F. (1955). "Interpretation of Statistical Relations as a Research Operation". En Lazarsfeld y Rosenberg (eds.), *The Language of Social Research*.
