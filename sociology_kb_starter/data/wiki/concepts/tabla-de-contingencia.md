---
id: tabla-de-contingencia
title: Tabla de contingencia
note_type: concept
semester: 2026-S1
course: "Metodología de las ciencias sociales"
related_concepts:
  - "[[chi-cuadrado]]"
  - "[[correlacion]]"
  - "[[variable-dependiente]]"
  - "[[variable-independiente]]"
  - "[[estadistica-descriptiva]]"
  - "[[niveles-de-medicion]]"
  - "[[muestreo-aleatorio]]"
tags:
  - estadística
  - análisis-bivariado
  - asociación
  - tabulación-cruzada
  - metodología-cuantitativa
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\modulo-3.md
updated_at: "2025-07-13"
---

## Definición

Una **tabla de contingencia** (también denominada *tabla de tabulación cruzada* o *cross-tabulation*) es un dispositivo de organización estadística que presenta la distribución conjunta de dos o más variables categóricas —[[niveles-de-medicion|nominales u ordinales]]— en forma de matriz de frecuencias. Cada celda de la tabla registra el número de observaciones que pertenecen simultáneamente a una categoría de la variable dispuesta en filas y a una categoría de la variable dispuesta en columnas. A partir de esas frecuencias observadas es posible calcular **frecuencias marginales** (totales de fila y columna), **distribuciones condicionales** (porcentajes dentro de cada fila o columna) y diversos coeficientes de asociación que permiten evaluar si las variables están relacionadas o son estadísticamente independientes.

En su forma más simple, una tabla de contingencia de 2 × 2 cruza dos variables dicotómicas; sin embargo, la estructura se extiende a tablas de *r* × *c* filas y columnas, e incluso a tablas multidimensionales cuando se introduce una tercera variable de control.

## Origen y contexto histórico

El uso sistemático de tablas de contingencia se remonta a los trabajos del estadístico británico **Karl Pearson**, quien a comienzos del siglo XX desarrolló la prueba de [[chi-cuadrado]] (χ²) precisamente para evaluar la independencia entre variables clasificadas en tablas de doble entrada (Pearson, 1900). Previamente, **George Udny Yule** había propuesto en 1900 el coeficiente *Q* de Yule para tablas 2 × 2, una medida de asociación que oscila entre −1 y +1 y que constituyó uno de los primeros intentos formales de cuantificar la relación entre variables cualitativas.

En las ciencias sociales, la tabla de contingencia adquirió centralidad gracias al sociólogo **Paul Lazarsfeld** y la tradición de investigación por encuestas de la Universidad de Columbia. Lazarsfeld sistematizó el denominado *método de elaboración* (*elaboration paradigm*), que consiste en introducir sucesivas variables de control en tablas de contingencia para distinguir relaciones espurias de relaciones genuinas, identificar variables intervinientes y precisar las condiciones bajo las cuales opera una asociación. Este procedimiento se convirtió en la columna vertebral del análisis cuantitativo en sociología durante la segunda mitad del siglo XX.

## Desarrollo teórico

El análisis de una tabla de contingencia se estructura en varios pasos:

1. **Construcción de la tabla.** Se cruzan la [[variable-independiente]] (convencionalmente en columnas) y la [[variable-dependiente]] (en filas), registrando las frecuencias absolutas observadas (*f_o*) en cada celda.
2. **Cálculo de frecuencias marginales.** Los totales de cada fila y cada columna resumen la distribución univariada de cada variable por separado.
3. **Distribuciones condicionales.** Se calculan los porcentajes de cada celda respecto del total de su columna (o de su fila) para comparar las distribuciones de la variable dependiente en cada categoría de la independiente.
4. **Evaluación de la asociación.** La prueba de [[chi-cuadrado]] de Pearson compara las frecuencias observadas con las frecuencias esperadas bajo la hipótesis de independencia. Su estadístico se define como:

   $$\chi^2 = \sum \frac{(f_o - f_e)^2}{f_e}$$

   donde *f_e* = (total de fila × total de columna) / gran total.
5. **Medidas de intensidad.** Una vez rechazada la hipótesis de independencia, se emplean coeficientes para estimar la fuerza de la asociación: el **coeficiente phi** (φ = √(χ²/N)) para tablas 2 × 2, la **V de Cramér** para tablas de mayor dimensión, y la **Q de Yule** cuando ambas variables son dicotómicas.

## Relación con otros conceptos

La tabla de contingencia se sitúa en el cruce de varias herramientas analíticas fundamentales de la [[estadistica-descriptiva]] e inferencial:

- **[[chi-cuadrado]]**: es la prueba de significación por excelencia aplicada a tablas de contingencia; permite decidir si la asociación observada es estadísticamente significativa o producto del azar muestral.
- **[[correlacion]]**: mientras la correlación de Pearson (*r*) mide la asociación lineal entre variables de intervalo o razón, la tabla de contingencia y sus coeficientes (phi, V de Cramér) abordan la relación entre variables con [[niveles-de-medicion]] nominal u ordinal.
- **[[variable-dependiente]] y [[variable-independiente]]**: la disposición convencional de la tabla refleja la distinción teórica entre la variable que se pretende explicar y la que se postula como explicativa.
- **Método de elaboración de Lazarsfeld**: al introducir una tercera variable en tablas parciales, se conecta con las nociones de causalidad, espuriedad y mediación propias del análisis multivariado.

## Debates y críticas

La tabla de contingencia, pese a su utilidad didáctica y analítica, ha recibido diversas críticas:

- **Pérdida de información.** Cuando se categorizan variables originalmente continuas para construir la tabla, se pierde precisión y potencia estadística; técnicas como la regresión logística aprovechan mejor la información disponible.
- **Sensibilidad al tamaño muestral.** El estadístico χ² depende directamente de *N*: con muestras muy grandes, diferencias triviales pueden resultar significativas; con muestras pequeñas, la prueba pierde potencia. De ahí la importancia de complementar la significación con medidas de tamaño del efecto (phi, V de Cramér).
- **Limitación bivariada.** La tabla clásica analiza dos variables a la vez; aunque el método de elaboración permite controlar una tercera, el análisis se vuelve engorroso con muchas variables, lo que favoreció la transición hacia modelos log-lineales y regresión logística a partir de los años 1970.
- **Supuestos de la prueba χ².** La prueba requiere frecuencias esperadas suficientemente grandes (convencionalmente ≥ 5); cuando no se cumple, se recurre a la prueba exacta de Fisher.

## Vigencia contemporánea

A pesar del desarrollo de técnicas multivariantes más sofisticadas, la tabla de contingencia conserva plena vigencia como herramienta exploratoria y pedagógica. En la enseñanza de métodos cuantitativos constituye el primer contacto de los estudiantes con el análisis bivariado. En la práctica investigadora, sigue siendo habitual en informes de encuestas electorales, estudios de salud pública, análisis de movilidad social y evaluación de políticas públicas. Software estadístico como SPSS, R y Python (mediante pandas y scipy) ofrecen rutinas especializadas para su cálculo y visualización, integrándola con pruebas de significación y gráficos de mosaico.

## Ejemplo empírico

Supóngase una encuesta a 200 estudiantes universitarios en la que se cruzan la variable *tipo de centro educativo de procedencia* (público / privado) con la variable *aprobación de la asignatura de estadística* (sí / no):

|                  | Aprueba | No aprueba | **Total** |
|------------------|:-------:|:----------:|:---------:|
| Centro público   |   68    |     42     |  **110**  |
| Centro privado   |   54    |     36     |   **90**  |
| **Total**        | **122** |   **78**   |  **200**  |

Las distribuciones condicionales muestran que el 61,8 % de los estudiantes de centros públicos aprueba frente al 60,0 % de los de centros privados. La diferencia es mínima y la prueba de [[chi-cuadrado]] arrojaría un valor bajo, sugiriendo independencia entre ambas variables en esta muestra. Este resultado llevaría a concluir, provisionalmente, que el tipo de centro no se asocia significativamente con la aprobación.

## Véase también

- [[chi-cuadrado]]
- [[correlacion]]
- [[variable-dependiente]]
- [[variable-independiente]]
- [[estadistica-descriptiva]]
- [[niveles-de-medicion]]
- [[muestreo-aleatorio]]
- [[la-investigacion-cuantitativa]]

## Fuentes

- Borge, Rosa; Padró-Solanet, Albert. "La investigación cuantitativa" [módulo didáctico]. Barcelona: FUOC (PID_00248673).
- Corbetta, Piergiorgio (2003). *Metodología y técnicas de investigación social*. Madrid: McGraw-Hill.
- Anduiza, Eva; Crespo, Ismael; Méndez, Mónica (2009, 2.ª ed.). *Metodología de la Ciencia Política*. Madrid: CIS.
- King, Gary; Keohane, Robert O.; Verba, Sidney (2000). *El diseño de la investigación social*. Madrid: Alianza.
- Pearson, Karl (1900). "On the criterion that a given system of deviations…". *Philosophical Magazine*, 50, 157-175.
- Lazarsfeld, Paul F.; Rosenberg, Morris (eds.) (1955). *The Language of Social Research*. Glencoe: Free Press.
