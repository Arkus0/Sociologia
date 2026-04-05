---
id: chi-cuadrado
title: "Chi-cuadrado (prueba χ²)"
note_type: concept
semester: 2026-S1
course: "Metodologia de las ciencias sociales"
related_concepts:
  - tabla-de-contingencia
  - estadistica-inferencial
  - hipotesis
  - nivel-de-confianza
  - niveles-de-medicion
  - correlacion
  - variable-independiente
tags:
  - estadística
  - prueba-de-hipótesis
  - variables-categóricas
  - Pearson
  - análisis-cuantitativo
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\modulo-3.md
updated_at: "2025-07-13"
---

## Definición

La **prueba de chi-cuadrado** (χ²) es un test estadístico no paramétrico que evalúa si existe una asociación estadísticamente significativa entre dos variables categóricas —nominales u ordinales— mediante la comparación entre las frecuencias observadas y las frecuencias teóricas esperadas bajo el supuesto de independencia. Su fórmula general es:

$$\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}$$

donde $O_i$ representa la frecuencia observada en cada celda y $E_i$ la frecuencia esperada. El valor resultante se compara con la distribución χ² según los grados de libertad correspondientes para determinar si la diferencia entre lo observado y lo esperado es atribuible al azar o refleja una relación genuina entre las variables.

En el marco de la [[estadistica-inferencial]], chi-cuadrado es la herramienta canónica para el análisis de [[tabla-de-contingencia|tablas de contingencia]], donde se cruzan las categorías de dos variables y se contrasta la [[hipotesis|hipótesis nula]] de independencia.

## Origen y contexto histórico

La prueba fue formulada por el matemático y estadístico británico **Karl Pearson** en su artículo seminal de 1900, *"On the Criterion that a Given System of Deviations from the Probable in the Case of a Correlated System of Variables is Such that It Can Be Reasonably Supposed to Have Arisen from Random Sampling"*, publicado en *Philosophical Magazine*. Este trabajo es considerado una de las piedras fundacionales de la estadística moderna.

Pearson desarrolló la prueba en un contexto en el que los métodos estadísticos del siglo XIX asumían mayoritariamente distribuciones normales. Sus trabajos previos (1893-1916) sobre la familia de distribuciones de Pearson le habían permitido modelar observaciones con asimetría, y la prueba χ² surgió como un método de **bondad de ajuste** para evaluar si un modelo teórico se adecuaba a los datos empíricos. Posteriormente, Ronald Fisher refinó la teoría de los grados de libertad asociados a la prueba, consolidando su uso en la investigación aplicada.

## Desarrollo teórico

La prueba χ² de Pearson tiene dos aplicaciones principales:

1. **Prueba de independencia**: evalúa si dos variables categóricas son independientes entre sí. Se construye una [[tabla-de-contingencia]] con las frecuencias cruzadas y se calculan las frecuencias esperadas bajo el supuesto de independencia. Los **grados de libertad** se determinan como $(r - 1)(c - 1)$, donde $r$ es el número de filas y $c$ el de columnas.

2. **Prueba de bondad de ajuste**: contrasta si la distribución observada de una variable se ajusta a una distribución teórica esperada. Los grados de libertad equivalen a $k - 1$, donde $k$ es el número de categorías.

El resultado del estadístico χ² se compara con un valor crítico determinado por los grados de libertad y el [[nivel-de-confianza]] elegido (habitualmente α = 0,05). Si el valor calculado supera el valor crítico, se rechaza la hipótesis nula y se concluye que existe asociación entre las variables.

Un supuesto fundamental es que las frecuencias esperadas en cada celda deben ser suficientemente grandes (convencionalmente ≥ 5). Cuando las muestras son pequeñas y este supuesto se viola, se recurre a la **prueba exacta de Fisher** como alternativa. Asimismo, para tablas 2×2, la **corrección de Yates** por continuidad ajusta la fórmula restando 0,5 a las diferencias absolutas para reducir el error de aproximación.

La prueba χ² indica si existe asociación, pero no informa sobre la **fuerza** de dicha asociación. Para cuantificar la intensidad se utilizan medidas derivadas como la **V de Cramér**, que normaliza el estadístico χ² en un rango de 0 a 1.

## Relación con otros conceptos

La prueba chi-cuadrado se inscribe en una red conceptual amplia dentro de la metodología cuantitativa:

- Se aplica sobre [[tabla-de-contingencia|tablas de contingencia]], el formato estándar para cruzar variables categóricas.
- Opera dentro de la lógica de la [[estadistica-inferencial]], donde se contrastan [[hipotesis|hipótesis]] con datos muestrales.
- Los [[niveles-de-medicion]] determinan su aplicabilidad: χ² es apropiada para variables nominales y ordinales, mientras que la [[correlacion]] de Pearson se emplea para variables de intervalo o razón.
- El [[nivel-de-confianza]] fija el umbral de significación estadística que rige la decisión de rechazar o no la hipótesis nula.
- La [[variable-independiente]] y la variable dependiente estructuran el diseño de la tabla de contingencia: la independiente se dispone en columnas y la dependiente en filas, siguiendo la convención de porcentualizar sobre la variable independiente.

## Debates y críticas

La prueba χ² presenta limitaciones que han generado discusión metodológica:

- **Sensibilidad al tamaño muestral**: con muestras muy grandes, diferencias triviales pueden resultar estadísticamente significativas; con muestras pequeñas, asociaciones reales pueden pasar inadvertidas. La significación estadística no equivale a relevancia sustantiva.
- **No mide intensidad**: el valor de χ² depende del tamaño de la tabla y de la muestra, lo que exige complementarlo con medidas de asociación como la V de Cramér o el coeficiente de contingencia.
- **Supuesto de independencia de observaciones**: cada caso debe contribuir a una sola celda, lo que excluye su uso directo con datos apareados (para los cuales existe la prueba de McNemar).
- **Frecuencias esperadas mínimas**: la aproximación asintótica a la distribución χ² se deteriora con celdas de baja frecuencia esperada, requiriendo alternativas como la prueba exacta de Fisher.

Desde la sociología crítica, se ha señalado que la prueba χ² —como toda herramienta de la estadística frecuentista— presupone un marco positivista de contrastación de hipótesis que puede resultar reduccionista frente a la complejidad de los fenómenos sociales.

## Vigencia contemporánea

La prueba chi-cuadrado sigue siendo uno de los procedimientos estadísticos más utilizados en ciencias sociales, especialmente en el análisis de encuestas y datos censales donde predominan las variables categóricas. Su uso es estándar en software como SPSS, R y Stata. La combinación de χ² con residuos estandarizados ajustados permite identificar qué celdas específicas de una tabla de contingencia contribuyen a la significación global, refinando el análisis. En la era del *big data*, su sensibilidad al tamaño muestral ha intensificado la necesidad de complementarla con medidas de efecto y con enfoques bayesianos.

## Ejemplo empírico

Un investigador desea saber si el **nivel educativo** (primaria, secundaria, universitario) es independiente de la **preferencia partidaria** (partido A, partido B, partido C) en una muestra de 300 votantes. Construye una [[tabla-de-contingencia]] 3×3 con las frecuencias observadas, calcula las esperadas bajo independencia y obtiene χ² = 18,7 con $(3-1)(3-1) = 4$ grados de libertad. El valor crítico para α = 0,05 con 4 gl es 9,49. Como 18,7 > 9,49, rechaza la hipótesis nula y concluye que existe una asociación estadísticamente significativa entre nivel educativo y preferencia partidaria. Para evaluar la intensidad calcula la V de Cramér, obteniendo 0,18, lo que indica una asociación débil pero significativa.

## Véase también

- [[tabla-de-contingencia]]
- [[estadistica-inferencial]]
- [[hipotesis]]
- [[nivel-de-confianza]]
- [[niveles-de-medicion]]
- [[correlacion]]
- [[variable-independiente]]
- [[estadistica-descriptiva]]
- [[encuesta]]

## Fuentes

- Pearson, K. (1900). "On the Criterion that a Given System of Deviations…". *Philosophical Magazine*, 50(302), 157-175.
- Cochran, W. G. (1952). "The Chi-square Test of Goodness of Fit". *The Annals of Mathematical Statistics*, 23(3), 315-345.
- Agresti, A. (2002). *Categorical Data Analysis*. 2.ª ed. Wiley.
- Apuntes de cátedra: Metodología de las ciencias sociales, Módulo 3 — Técnicas cuantitativas y análisis estadístico (UOC, 2026-S1).
