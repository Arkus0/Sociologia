---
id: inferencia
title: Inferencia
note_type: concept
semester: 2026-S1
course: "Metodologia de las ciencias sociales"
related_concepts:
  - estadistica-inferencial
  - hipotesis
  - muestra
  - causalidad
  - nivel-de-confianza
  - metodo-cientifico
  - diseno-de-investigacion
tags:
  - metodologia
  - estadistica
  - epistemologia
  - investigacion-cuantitativa
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\el-proceso-de-formulacion-teorica.md
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\el-proceso-de-investigacion-en-las-ciencias-sociales.md
updated_at: '2025-07-13'
---

## Definición

La **inferencia** es el proceso lógico mediante el cual se extraen conclusiones a partir de datos, evidencias u observaciones disponibles. En las ciencias sociales, el término abarca tanto la inferencia estadística —estimación de parámetros poblacionales y contraste de [[hipotesis]]— como la inferencia causal —determinación de relaciones causa-efecto entre fenómenos sociales—. King, Keohane y Verba (2000) sitúan la inferencia como el objetivo primordial de toda investigación científica: más allá de la mera acumulación de observaciones empíricas, la ciencia aspira a revelar hechos no observados y a identificar relaciones causales entre fenómenos.

La [[estadistica-inferencial]] constituye la rama de la estadística que se ocupa de elaborar conclusiones, generalizaciones o predicciones acerca de una población estadística basándose en el análisis de una [[muestra]] representativa. A diferencia de la estadística descriptiva, que se limita a resumir los datos observados, la inferencia utiliza métodos probabilísticos para extender los resultados obtenidos en la muestra al conjunto de la población.

## Origen y contexto histórico

Los fundamentos modernos de la inferencia estadística se consolidaron en la primera mitad del siglo XX. Ronald A. Fisher estableció en los años 1920 los principios de la estimación por máxima verosimilitud, el diseño experimental y la prueba de significación. Su enfoque proponía evaluar la compatibilidad de los datos observados con una hipótesis nula mediante el *p-valor*, sin necesidad de formular una hipótesis alternativa explícita.

Paralelamente, Jerzy Neyman y Egon Pearson desarrollaron en los años 1930 un marco rival centrado en la decisión entre dos hipótesis (nula y alternativa), introduciendo conceptos como el error de tipo I, el error de tipo II y la potencia estadística. Aunque en la práctica docente y aplicada ambos enfoques se fusionaron en un híbrido, sus fundamentos filosóficos divergen considerablemente: Fisher concebía la inferencia como un proceso inductivo de aprendizaje, mientras que Neyman y Pearson la entendían como un procedimiento de decisión con tasas de error controladas a largo plazo.

La tradición bayesiana, con antecedentes en el teorema de Bayes (1763) y los trabajos de Laplace, permaneció marginal durante gran parte del siglo XX. Su renacimiento a partir de los años 1990, impulsado por el aumento de la capacidad computacional y los métodos de Monte Carlo por cadenas de Markov (MCMC), ha transformado el panorama de la inferencia en múltiples disciplinas.

## Desarrollo teórico

La inferencia estadística comprende dos grandes familias de procedimientos: la **estimación** (puntual e intervalar) y el **contraste de hipótesis**. La estimación puntual proporciona un valor único como mejor aproximación del parámetro poblacional, mientras que la estimación intervalar ofrece un rango —el intervalo de confianza— dentro del cual se espera que se encuentre dicho parámetro con un determinado [[nivel-de-confianza]]. El contraste de hipótesis permite evaluar si los datos observados son compatibles con una proposición teórica previamente formulada.

Desde la perspectiva **frecuentista**, la probabilidad se define como la frecuencia relativa a largo plazo de un evento en repeticiones hipotéticas del experimento. Bajo este paradigma, los parámetros son constantes fijas y desconocidas, y la incertidumbre reside en los datos muestrales. En cambio, la **inferencia bayesiana** trata los parámetros como variables aleatorias dotadas de una distribución de probabilidad previa (*prior*), que se actualiza a la luz de los datos observados para obtener una distribución posterior (*posterior*). Esta perspectiva permite incorporar información previa y proporciona interpretaciones probabilísticas directas sobre los parámetros de interés.

La obra fundamental de King, Keohane y Verba, *El diseño de la investigación social: la inferencia científica en los estudios cualitativos* (2000), argumenta que todos los métodos de investigación —cuantitativos y cualitativos— comparten una misma lógica inferencial definida por cuatro características: (1) el objetivo es hacer inferencias, (2) los procedimientos son públicos, (3) las conclusiones son inciertas y provisionales, y (4) el contenido es el método como garante de justicia procedimental.

## Relación con otros conceptos

La inferencia se articula estrechamente con una constelación de conceptos metodológicos. La [[muestra]] es la condición de posibilidad de toda inferencia estadística: sin un procedimiento adecuado de muestreo probabilístico, las generalizaciones carecen de validez. La [[hipotesis]] constituye el punto de partida del contraste inferencial, pues toda prueba estadística requiere la formulación precisa de proposiciones contrastables. El [[nivel-de-confianza]] cuantifica el grado de certeza asociado a las estimaciones inferenciales.

La distinción entre inferencia estadística e inferencia causal ([[causalidad]]) resulta crucial. La mera asociación estadística entre variables no demuestra causalidad; se requieren diseños específicos —experimentos aleatorizados, variables instrumentales, diferencias en diferencias— para sustentar afirmaciones causales. El [[diseno-de-investigacion]] determina las condiciones bajo las cuales la inferencia será más o menos válida, atendiendo a la selección de casos, la operacionalización de variables y el control de sesgos.

## Debates y críticas

El debate Fisher-Neyman-Pearson sigue reverberando en la práctica científica contemporánea. La llamada «crisis de replicabilidad» ha puesto en evidencia los abusos del *p-valor* y las prácticas de *p-hacking*, generando movimientos a favor del abandono de los umbrales arbitrarios de significación (Wasserstein y Lazar, 2016).

Karl Popper planteó una crítica filosófica profunda a la inferencia inductiva. Desde su racionalismo crítico, Popper argumentó que la ciencia no avanza por acumulación inductiva de confirmaciones, sino por la formulación de conjeturas audaces y su posterior refutación (falsacionismo). En esta perspectiva, la inferencia legítima es deductiva: de la teoría se deducen consecuencias empíricas que los datos pueden refutar, pero nunca verificar definitivamente.

Friedrich Hayek, desde la tradición liberal austriaca, advirtió sobre los límites de la inferencia estadística aplicada a la planificación social. Hayek sostenía que la complejidad de los fenómenos sociales —con sus innumerables variables interrelacionadas y su dependencia de conocimiento disperso— hacía que las inferencias basadas en agregados estadísticos fueran insuficientes para orientar intervenciones centralizadas.

Brady y Collier (2010) matizaron la tesis unificadora de King, Keohane y Verba, señalando que los métodos cualitativos poseen estándares inferenciales propios que no se reducen a los de la estadística cuantitativa, aunque ambas tradiciones comparten herramientas y estándares comunes (*diverse tools, shared standards*).

## Vigencia contemporánea

La revolución de la **inferencia causal** ha transformado las ciencias sociales en las últimas dos décadas. Judea Pearl desarrolló el marco de los modelos causales estructurales y el *do-calculus*, proporcionando herramientas formales para distinguir correlación de [[causalidad]]. Joshua Angrist y Guido Imbens —galardonados con el Premio Nobel de Economía en 2021— sistematizaron el uso de experimentos naturales y variables instrumentales para estimar efectos causales cuando la aleatorización no es factible.

La inferencia bayesiana ha ganado terreno considerable en las ciencias sociales. Su capacidad para incorporar información previa, manejar modelos jerárquicos complejos y proporcionar estimaciones probabilísticas intuitivas la ha convertido en herramienta preferida en áreas como la ciencia política cuantitativa, la psicología y la sociología computacional. Paralelamente, los métodos de aprendizaje automático (*machine learning*) han introducido nuevas formas de inferencia predictiva que complementan —pero no sustituyen— los enfoques explicativos tradicionales.

## Ejemplo empírico

Un investigador desea determinar si un programa de transferencias monetarias condicionadas reduce la deserción escolar en una región. A partir de una [[muestra]] aleatoria de 2.000 familias —1.000 beneficiarias y 1.000 de control—, calcula que la tasa de deserción es del 8 % en el grupo tratado y del 14 % en el grupo de control. Mediante un contraste de [[hipotesis]] (prueba *t* de diferencia de proporciones), obtiene un *p-valor* < 0,01 y un intervalo de confianza al 95 % para la diferencia de [–9,2 %; –2,8 %]. La inferencia estadística permite concluir —con incertidumbre cuantificada— que existe una diferencia significativa entre ambos grupos. Si, además, el diseño garantiza la asignación aleatoria, se puede realizar una inferencia causal: el programa *causa* una reducción de aproximadamente 6 puntos porcentuales en la deserción escolar.

## Véase también

- [[estadistica-inferencial]]
- [[hipotesis]]
- [[muestra]]
- [[causalidad]]
- [[nivel-de-confianza]]
- [[metodo-cientifico]]
- [[diseno-de-investigacion]]
- [[variables]]

## Fuentes

- King, G.; Keohane, R. O.; Verba, S. (2000). *El diseño de la investigación social: la inferencia científica en los estudios cualitativos*. Madrid: Alianza Editorial.
- Brady, H. E.; Collier, D. (2010). *Rethinking Social Inquiry: Diverse Tools, Shared Standards*. Lanham: Rowman & Littlefield.
- Fisher, R. A. (1925). *Statistical Methods for Research Workers*. Edinburgh: Oliver & Boyd.
- Neyman, J.; Pearson, E. S. (1933). "On the Problem of the Most Efficient Tests of Statistical Hypotheses". *Philosophical Transactions of the Royal Society A*, 231, 289–337.
- Pearl, J. (2009). *Causality: Models, Reasoning, and Inference*. Cambridge: Cambridge University Press.
- Angrist, J. D.; Pischke, J.-S. (2009). *Mostly Harmless Econometrics: An Empiricist's Companion*. Princeton: Princeton University Press.
- Popper, K. (1959). *The Logic of Scientific Discovery*. London: Hutchinson.
- Hayek, F. A. (1945). "The Use of Knowledge in Society". *American Economic Review*, 35(4), 519–530.
- Wasserstein, R. L.; Lazar, N. A. (2016). "The ASA Statement on p-Values". *The American Statistician*, 70(2), 129–133.
- Módulo 2: Procedimientos y decisiones para determinar qué se observará (FUOC, PID_00248675).
- Módulo 3: La investigación cuantitativa (FUOC, PID_00248676).
