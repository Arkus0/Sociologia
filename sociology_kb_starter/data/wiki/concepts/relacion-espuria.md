---
id: relacion-espuria
title: Relación espúrea
note_type: concept
semester: 2026-S1
course: Metodologia de las ciencias sociales
related_concepts:
- causalidad
- variable-de-control
- variable-interviniente
- validez-interna
- covarianza
tags:
- metodologia
- causalidad
- estadistica
---

## Definición

Una **relación espúrea** (o correlación espúrea) es una asociación estadística entre dos variables que no refleja una relación causal real entre ellas, sino que es producida por una tercera variable (variable antecedente o confundente) que causa ambas simultáneamente.

## Estructura

```
     Z (variable antecedente)
    / \
   v   v
   X    Y   → La correlación X-Y desaparece al controlar Z
```

- X e Y parecen estar relacionadas, pero la relación desaparece cuando se **controla** por Z
- Ejemplo clásico: correlación entre ventas de helados y ahogamientos. Ambas variables están causadas por una tercera: la temperatura. No existe relación causal entre helados y ahogamientos.

## Importancia metodológica

- Identificar relaciones espúreas es uno de los mayores desafíos de la investigación social
- Los criterios de [[causalidad]] exigen demostrar que la relación entre X e Y persiste **después de controlar** todas las variables alternativas plausibles
- El [[experimento]] con asignación aleatoria es la mejor herramienta para evitar relaciones espúreas, porque la aleatorización distribuye equitativamente todas las variables confundentes
- En la investigación no experimental (observacional), se utilizan técnicas de [[control estadístico]] (regresión múltiple, análisis multivariado) para detectar y eliminar relaciones espúreas

## Fuentes
- [[El proceso de formulación teórica]]
- [[la-investigacion-cuantitativa|La investigación cuantitativa]]
