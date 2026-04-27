---
id: aleatorizacion
title: Aleatorización
note_type: concept
semester: 2026-S1
course: Metodos de investigacion social
related_concepts:
  - experimento
  - validez-interna
  - variable-independiente
  - inferencia-causal
  - sesgo-de-seleccion
tags:
  - metodos-de-investigacion-social
  - metodologia-cuantitativa
  - causalidad
updated_at: "2026-04-27"
---

## Definición
La **aleatorización** es el procedimiento por el cual unidades de análisis (personas, grupos, escuelas, municipios) se asignan al azar a condiciones de tratamiento y control dentro de un [[experimento]]. Su objetivo central es asegurar que, antes de la intervención, ambos grupos sean comparables en promedio respecto de características observables y no observables. Esta equivalencia probabilística permite atribuir diferencias posteriores en el resultado a la [[variable-independiente]] manipulada, fortaleciendo la [[inferencia-causal]] y la [[validez-interna]]. En términos prácticos, la aleatorización reduce el [[sesgo-de-seleccion]]: evita que la asignación dependa de decisiones del investigador o de los propios participantes.

## Origen y contexto histórico
La formalización moderna de la aleatorización se asocia a Ronald A. Fisher en la estadística experimental agrícola de los años 1920 y 1930, especialmente en *The Design of Experiments* (1935). Su adopción en ciencias sociales fue más tardía por restricciones éticas, logísticas y políticas. Desde la segunda mitad del siglo XX, psicología social, economía del desarrollo y políticas públicas incorporaron diseños experimentales aleatorizados para evaluar programas, con expansión notable desde los años 2000 en evaluaciones de impacto a gran escala.

## Desarrollo teórico
La lógica teórica de la aleatorización descansa en el marco de resultados potenciales: cada unidad tendría un resultado con tratamiento y otro sin tratamiento, pero solo uno es observable. Al asignar tratamiento al azar, la diferencia media entre grupos estima el efecto causal promedio bajo supuestos explícitos.

Existen variantes relevantes: aleatorización simple, por bloques (para mejorar balance en covariables clave), por conglomerados o *clusters* (cuando se intervienen escuelas/barrios completos) y diseños escalonados. Cada variante resuelve problemas empíricos distintos y plantea compromisos entre precisión estadística, costos y factibilidad.

La aleatorización no elimina todos los problemas metodológicos: puede coexistir con incumplimiento del tratamiento, deserción diferencial, efectos de contagio entre grupos o baja validez externa. Por eso, se complementa con protocolos de implementación, análisis de robustez y transparencia en pre-registro.

## Relación con otros conceptos
- Se integra en el [[experimento]] como mecanismo central de identificación causal.
- Refuerza la [[validez-interna]] al neutralizar sesgos de asignación.
- Opera sobre la [[variable-independiente]] al decidir quién recibe la intervención.
- Sustenta la [[inferencia-causal]] cuando se cumplen supuestos de diseño e implementación.
- Mitiga el [[sesgo-de-seleccion]], aunque no sustituye control de atrición o medición.

## Debates y críticas
La principal crítica sostiene que la aleatorización privilegia preguntas “intervenibles” y puede dejar fuera procesos estructurales difíciles de experimentar (desigualdad histórica, instituciones, cultura política). Otra crítica apunta a la validez externa: un efecto causal estimado en un contexto no siempre se generaliza a otros. También existen debates éticos sobre asignar o negar tratamientos socialmente valiosos.

## Vigencia contemporánea
En la década de 2010 y 2020, la aleatorización se consolidó en evaluación de políticas educativas, sanitarias y de transferencia monetaria. A la vez, se amplió el debate sobre replicabilidad, transparencia de datos y análisis pre-registrados. En entornos digitales, plataformas realizan experimentos A/B continuos, trasladando la lógica de aleatorización al diseño de interfaces y algoritmos, con nuevas discusiones éticas sobre consentimiento y gobernanza de datos.

## Ejemplo empírico
Un municipio que desea evaluar tutorías escolares puede asignar aleatoriamente escuelas a programa (tratamiento) o continuidad habitual (control). Si, tras un curso, el rendimiento mejora de forma estadísticamente significativa en el grupo tratado, y se descartan sesgos de implementación, la diferencia se interpreta como efecto causal del programa bajo ese contexto.

## Véase también
- [[experimento]]
- [[validez-interna]]
- [[variable-independiente]]
- [[inferencia-causal]]
- [[sesgo-de-seleccion]]

## Fuentes
- Fisher, R. A. (1935). *The Design of Experiments*.
- Rubin, D. B. (1974). “Estimating Causal Effects of Treatments in Randomized and Nonrandomized Studies”.
- Shadish, W. R., Cook, T. D., & Campbell, D. T. (2002). *Experimental and Quasi-Experimental Designs for Generalized Causal Inference*.
- Duflo, E., Glennerster, R., & Kremer, M. (2007). “Using Randomization in Development Economics Research”.
