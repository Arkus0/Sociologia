---
id: variable-de-control
title: Variable de control
note_type: concept
semester: 2026-S1
course: "Metodología de las ciencias sociales"
related_concepts:
  - variable-dependiente
  - variable-independiente
  - relacion-espurea
  - regresion
  - omision-de-variables
  - endogeneidad
  - causalidad
  - operacionalizacion
tags:
  - metodología
  - análisis-multivariado
  - causalidad
  - control-estadístico
  - Lazarsfeld
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\el-proceso-de-formulacion-teorica.md
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\el-proceso-de-investigacion-en-las-ciencias-sociales.md
updated_at: '2025-07-13'
---

## Definición

Una **variable de control** es aquella que el investigador mantiene constante —o cuyo efecto neutraliza estadísticamente— con el fin de aislar la relación entre la [[variable-independiente]] y la [[variable-dependiente]]. Su función es eliminar explicaciones rivales: si la asociación entre X e Y persiste una vez que se ha controlado Z, la hipótesis de que Z confunde dicha relación queda descartada. Si, por el contrario, la asociación desaparece al introducir Z, se concluye que la relación original era [[relacion-espurea|espuria]].

En la práctica, controlar una variable significa segmentar la muestra según las categorías de Z y observar si la relación X → Y se mantiene dentro de cada estrato, o bien incluir Z como predictor adicional en un modelo de [[regresion]]. La lógica subyacente es común tanto al diseño experimental —donde el control se logra mediante aleatorización y manipulación directa— como al diseño observacional —donde se recurre al control estadístico—, aunque las garantías causales difieren sustancialmente entre ambos contextos.

## Origen y contexto histórico

La idea de neutralizar factores ajenos al fenómeno estudiado tiene raíces en la tradición experimental de las ciencias naturales, pero su formalización en ciencias sociales se asocia con dos momentos clave. En primer lugar, Émile Durkheim planteó en *Las reglas del método sociológico* (1895) el **método de las variaciones concomitantes**, inspirado en los cánones de John Stuart Mill: para establecer que un fenómeno A causa B, es necesario descartar que un tercer factor C explique la covariación observada. Durkheim aplicó esta lógica en *El suicidio* (1897), donde controló sistemáticamente variables como la religión, el estado civil y la integración social para aislar los determinantes de las tasas de suicidio.

En segundo lugar, **Paul F. Lazarsfeld** y la Escuela de Columbia sistematizaron, durante las décadas de 1940 y 1950, el **paradigma de la elaboración** (*elaboration paradigm*), un procedimiento analítico que consiste en introducir una tercera variable (la variable de control o «variable test») en una relación bivariada previamente observada. Este paradigma, desarrollado en el contexto de la investigación por [[encuesta]] y el análisis de tablas cruzadas, permitió distinguir entre relaciones genuinas y espurias sin necesidad de recurrir a la experimentación.

## Desarrollo teórico

### El paradigma de la elaboración de Lazarsfeld

Lazarsfeld formalizó tres resultados posibles al introducir una variable de control en una relación bivariada:

1. **Explicación** (*explanation*): la relación original entre X e Y desaparece al controlar Z, y Z es *antecedente* a ambas variables. La relación era espuria; Z era la causa común.
2. **Interpretación** (*interpretation*): la relación desaparece al controlar Z, pero Z es *interviniente* —se sitúa en la cadena causal entre X e Y—. La variable de control revela el mecanismo a través del cual X afecta a Y.
3. **Especificación** (*specification*): la relación persiste en algunos estratos de Z pero no en otros. Z actúa como variable moderadora: la intensidad o el sentido de la relación X → Y depende del valor de Z.

Este esquema aportó a la sociología empírica una gramática analítica para razonar sobre [[causalidad]] con datos observacionales y sigue siendo la base pedagógica del análisis multivariado en los manuales de metodología.

### Control estadístico y análisis multivariado

Con la difusión de la [[regresion]] lineal múltiple y la regresión logística, la noción de «controlar» una variable se extendió más allá de las tablas cruzadas. En un modelo de regresión, cada coeficiente parcial se interpreta como el efecto de la variable correspondiente *manteniendo constantes* las demás variables incluidas. Esta operación estadística equivale conceptualmente a la elaboración lazarsfeldiana, pero permite manejar simultáneamente un número elevado de variables de control y variables continuas.

John H. Goldthorpe, en *On Sociology* (2000), argumentó que el control estadístico mediante regresión constituye la herramienta más potente disponible para la sociología cuantitativa cuando la experimentación no es viable, siempre que el investigador justifique teóricamente la selección de las variables incluidas en el modelo.

### La perspectiva causal contemporánea

Judea Pearl, desde el marco de los **diagramas causales** (DAGs, *directed acyclic graphs*), formalizó matemáticamente las condiciones bajo las cuales controlar una variable elimina el sesgo de confusión. El criterio de la *puerta trasera* (*back-door criterion*) establece que, para estimar el efecto causal de X sobre Y, es suficiente condicionar sobre un conjunto de variables que bloquee todos los caminos espurios entre X e Y sin bloquear los caminos causales. Esta formalización reveló que controlar la variable equivocada —por ejemplo, un colisionador— puede *introducir* sesgo en lugar de eliminarlo, un problema invisible en la aproximación clásica.

## Relación con otros conceptos

La variable de control se sitúa en una red conceptual densa. Su razón de ser es prevenir la [[relacion-espurea]]: una asociación estadística entre X e Y que desaparece al considerar un factor confusor Z. El problema de la [[omision-de-variables]] surge precisamente cuando se omite una variable de control relevante, generando estimaciones sesgadas e inconsistentes —lo que en econometría se denomina [[endogeneidad]]—. El control es, además, inseparable del concepto de [[causalidad]]: solo tras neutralizar explicaciones alternativas puede un investigador avanzar inferencias causales con alguna garantía. La [[operacionalizacion]] previa de la variable de control —su traducción en indicadores medibles— condiciona enteramente la calidad del control ejercido.

## Debates y críticas

David Freedman, en una serie de artículos influyentes reunidos en *Statistical Models: Theory and Practice* (2009), cuestionó la confianza excesiva en el control estadístico mediante regresión. Según Freedman, la inclusión mecánica de variables de control sin un modelo causal sustantivo conduce a resultados artificiosos: los coeficientes parciales solo tienen interpretación causal bajo supuestos muy exigentes —linealidad, ausencia de errores de medición, correcta especificación funcional— que rara vez se verifican en la investigación social.

Desde la sociología cualitativa, se ha señalado que la lógica del control estadístico presupone una ontología atomista que descompone los fenómenos sociales en variables discretas, perdiendo de vista la totalidad configuracional de los procesos sociales. Andrew Abbott (*The System of Professions*, 1988) criticó el «pensamiento por variables» como inadecuado para captar la temporalidad narrativa de los procesos históricos.

Un debate técnico adicional concierne a la selección de las variables de control. Incluir variables postratamiento (afectadas por la variable independiente) puede sesgar el efecto estimado; controlar un colisionador abre caminos espurios. La revolución de la inferencia causal gráfica (Pearl, 2009) ha contribuido a disciplinar esta selección, exigiendo que responda a un modelo causal explícito y no a una búsqueda puramente empírica de «significatividad estadística».

## Vigencia contemporánea

En la sociología cuantitativa actual, el control de variables es omnipresente. Los modelos de regresión multinivel, los modelos de efectos fijos para datos de panel y las técnicas de emparejamiento (*matching*) constituyen estrategias sofisticadas de control. Al mismo tiempo, la revolución de la credibilidad (*credibility revolution*) en economía y ciencias sociales ha desplazado el énfasis desde la acumulación de controles hacia los **diseños de identificación**: instrumentos, regresiones en discontinuidad y experimentos naturales que resuelven el problema de la confusión de forma más robusta que el control estadístico convencional.

Los diagramas causales de Pearl y el marco de resultados potenciales de Rubin han proporcionado lenguajes formales para decidir *qué* controlar y *por qué*, superando la práctica anterior de incluir «todos los controles disponibles». Esta formalización ha tenido un impacto creciente en la sociología, como atestiguan los trabajos de Morgan y Winship (*Counterfactuals and Causal Inference*, 2007; 2ª ed. 2015).

## Ejemplo empírico

En el material del curso se plantea la hipótesis: «Cuanto mayor es el grado de sofisticación política, mayor es la participación electoral». Una hipótesis rival introduce una variable de control: «La sofisticación política y la participación electoral dependen del nivel de recursos socioeconómicos de los electores; por lo tanto, la relación entre sofisticación política y participación es espuria». Para contrastar esta hipótesis, el investigador segmenta la muestra según nivel socioeconómico y examina si la relación entre sofisticación y participación persiste dentro de cada estrato. Si desaparece, el nivel socioeconómico era un confusor; si se mantiene, la relación es genuina y el nivel socioeconómico queda descartado como explicación alternativa. Este procedimiento ilustra fielmente la lógica de la elaboración lazarsfeldiana.

## Véase también

- [[variable-dependiente]]
- [[variable-independiente]]
- [[relacion-espurea]]
- [[regresion]]
- [[omision-de-variables]]
- [[endogeneidad]]
- [[causalidad]]
- [[operacionalizacion]]
- [[encuesta]]
- [[hipotesis]]
- [[investigacion-cuantitativa]]

## Fuentes

- Durkheim, É. (1895). *Les règles de la méthode sociologique*. Alcan.
- Lazarsfeld, P. F., Berelson, B. y Gaudet, H. (1944). *The People's Choice*. Columbia University Press.
- Lazarsfeld, P. F. (1955). «Interpretation of statistical relations as a research operation». En Lazarsfeld, P. F. y Rosenberg, M. (eds.), *The Language of Social Research*. Free Press, pp. 115-125.
- Rosenberg, M. (1968). *The Logic of Survey Analysis*. Basic Books.
- Goldthorpe, J. H. (2000). *On Sociology: Numbers, Narratives, and the Integration of Research and Theory*. Oxford University Press.
- Freedman, D. A. (2009). *Statistical Models: Theory and Practice*. 2.ª ed. Cambridge University Press.
- Pearl, J. (2009). *Causality: Models, Reasoning, and Inference*. 2.ª ed. Cambridge University Press.
- Morgan, S. L. y Winship, C. (2015). *Counterfactuals and Causal Inference*. 2.ª ed. Cambridge University Press.
- Material del curso: [[el-proceso-de-formulacion-teorica]], [[el-proceso-de-investigacion-en-las-ciencias-sociales]].
