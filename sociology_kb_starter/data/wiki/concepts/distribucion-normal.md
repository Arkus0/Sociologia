---
id: distribucion-normal
title: "Distribución normal"
note_type: concept
semester: 2026-S1
course: Metodologia de las ciencias sociales
related_concepts:
  - media-aritmetica
  - desviacion-estandar
  - varianza
  - intervalo-de-confianza
  - inferencia-estadistica
  - distribucion-de-frecuencias
  - niveles-de-medicion
tags:
  - distribucion-normal
  - estadistica
  - metodologia
updated_at: "2026-04-27"
---

# Distribución normal

## Definición

La **distribución normal** (o gaussiana) es una distribución de probabilidad continua, unimodal y simétrica alrededor de su media. Se representa como una “campana” y queda completamente determinada por dos parámetros: la **media** ($\mu$), que fija la localización del centro, y la **desviación estándar** ($\sigma$), que fija la escala o dispersión.

Su densidad es:

$$
f(x)=\frac{1}{\sigma\sqrt{2\pi}}\exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right),\quad -\infty < x < \infty
$$

## Supuestos y propiedades básicas

Para su uso en investigación social aplicada suelen asumirse, al menos de forma aproximada, los siguientes puntos:

1. **Variable cuantitativa** medida en escala de intervalo o razón.
2. **Observaciones independientes** (o dependencia modelada explícitamente).
3. **Ausencia de sesgos extremos de medición** que deformen la forma de la distribución.
4. **Tamaño muestral suficiente** para apoyar aproximaciones normales en estimadores (por teorema central del límite), incluso cuando la variable original no es perfectamente normal.

Propiedades clave:

- **Simetría**: media, mediana y moda coinciden.
- **Regla 68-95-99,7**: en una normal, aproximadamente 68 % de los casos cae en $\mu\pm1\sigma$, 95 % en $\mu\pm2\sigma$ y 99,7 % en $\mu\pm3\sigma$.
- **Estandarización**: cualquier normal puede transformarse a normal estándar con $Z=(X-\mu)/\sigma$.
- **Rol inferencial**: muchas pruebas paramétricas y estimaciones de error estándar descansan en normalidad exacta o asintótica.

## Interpretación sociológica de la media y la desviación estándar

En sociología cuantitativa, la **media** no es solo un promedio matemático: funciona como referencia de “posición típica” de una población en una dimensión social (ingresos, años de escolaridad, puntajes de actitudes, etc.).

La **desviación estándar** expresa cuánta heterogeneidad social hay alrededor de esa referencia:

- desviación baja: mayor concentración de trayectorias o condiciones de vida;
- desviación alta: mayor dispersión, desigualdad o segmentación.

Interpretar conjuntamente media y desviación permite distinguir situaciones empíricas con mismo promedio pero estructuras sociales diferentes. Dos grupos pueden compartir media de ingreso y, sin embargo, uno presentar baja dispersión (relativa homogeneidad) y otro alta dispersión (polarización).

## Relación con otros conceptos

- **[[desviacion-estandar]]**: parámetro central de escala en la normal; determina el “ancho” de la campana.
- **[[varianza]]**: es $\sigma^2$; en normalidad resume la dispersión cuadrática total.
- **[[intervalo-de-confianza]]**: bajo supuestos paramétricos, la normal (o la t en muestras pequeñas) sustenta la construcción de intervalos para medias y coeficientes.
- **[[inferencia-estadistica]]**: pruebas de hipótesis, errores estándar y modelos lineales usan normalidad en distintos niveles (variable, residuos o distribución muestral del estimador).
- **[[media-aritmetica]]**: coincide con mediana y moda solo cuando la distribución es simétrica.
- **[[distribucion-de-frecuencias]]**: herramienta diagnóstica inicial para evaluar forma, asimetría y colas.

## Límites y precauciones

La normalidad es una referencia potente, pero no universal. En ciencias sociales deben considerarse estos límites:

1. **No normalidad**: muchas variables reales son asimétricas (por ejemplo, ingresos o patrimonio).
2. **Colas pesadas**: eventos extremos son más frecuentes que en una normal; la media y la desviación se vuelven menos estables.
3. **Variables ordinales**: en escalas Likert, tratar la variable como normal puede ser una aproximación discutible; conviene evaluar alternativas ordinales o robustas.
4. **Transformaciones**: aplicar logaritmos, raíz cuadrada o Box-Cox puede mejorar simetría, pero cambia la interpretación sustantiva de parámetros y efectos.
5. **Diagnóstico empírico obligatorio**: antes de asumir normalidad conviene inspeccionar histograma, QQ-plot, asimetría/curtosis y plausibilidad teórica del mecanismo generador.

## Ejemplo empírico (encuesta)

Un equipo releva una encuesta de hogares con dos variables:

- **Puntuación de satisfacción con servicios públicos** (0–100).
- **Ingreso mensual del hogar**.

### Caso A: cuándo sí es razonable aproximar normalidad

En la puntuación 0–100, la muestra muestra distribución aproximadamente simétrica, sin colas extremas y con concentración alrededor del centro. En este escenario, usar media y desviación estándar para resumir y construir [[intervalo-de-confianza]] para la media resulta defendible.

### Caso B: cuándo no conviene asumir normalidad

En ingreso mensual aparece fuerte asimetría a la derecha (pocos hogares con ingresos muy altos) y presencia de outliers. Aquí la media queda inflada y la desviación estándar aumenta por valores extremos. Es preferible complementar con mediana, percentiles y métodos robustos; si se modela paramétricamente, puede evaluarse transformación logarítmica del ingreso y verificar supuestos en la escala transformada.

## Véase también

- [[media-aritmetica]]
- [[desviacion-estandar]]
- [[varianza]]
- [[intervalo-de-confianza]]
- [[inferencia-estadistica]]
- [[distribucion-de-frecuencias]]
- [[niveles-de-medicion]]

## Fuentes

- Módulo 3, *Metodología de las ciencias sociales*, UOC, 2026-S1.
- DeGroot, Morris H. (1988). *Probabilidad y estadística* (2.ª ed.). Addison-Wesley Iberoamericana.
- Moore, David S. (1995). *Estadística aplicada básica*. Barcelona: Antonio Bosch.
- Field, Andy (2018). *Discovering Statistics Using IBM SPSS Statistics* (5th ed.). Sage.
