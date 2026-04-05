---
id: sesgo-de-seleccion
title: Sesgo de selección
note_type: concept
semester: 2026-S1
course: "Metodologia de las ciencias sociales"
related_concepts:
  - muestreo
  - representatividad
  - validez-interna
  - endogeneidad
  - relacion-espurea
  - cuasiexperimento
  - variable-dependiente
tags:
  - metodología
  - inferencia-causal
  - diseño-de-investigación
  - sesgos
  - estadística
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\modulo-2.md
updated_at: '2025-07-13'
---

## Definición

El **sesgo de selección** (*selection bias*) es un error sistemático que se produce cuando los individuos, casos u observaciones incluidos en un estudio no constituyen una muestra representativa de la población de referencia, debido a que el procedimiento de selección está correlacionado con la variable de interés. A diferencia del error aleatorio, el sesgo de selección tiene una dirección predecible y no se reduce aumentando el tamaño muestral; su presencia compromete la [[validez-interna]] de cualquier inferencia causal o descriptiva. En términos formales, aparece cuando $P(S=1 \mid X, Y) \neq P(S=1)$, es decir, cuando la probabilidad de ser seleccionado en la muestra depende de las variables explicativas o del resultado estudiado.

En ciencias sociales, el sesgo de selección es especialmente relevante porque la asignación aleatoria de tratamientos rara vez es factible: no se puede asignar al azar la pobreza, la pertenencia étnica o la experiencia bélica. Toda investigación observacional enfrenta, en mayor o menor grado, el riesgo de que las unidades analizadas difieran sistemáticamente de aquellas excluidas.

## Origen y contexto histórico

La preocupación por la selección no aleatoria de casos se remonta a los primeros debates sobre muestreo estadístico a finales del siglo XIX, pero adquirió formalización plena en el siglo XX. En epidemiología, Joseph Berkson (1946) demostró que la selección de pacientes hospitalarios podía generar asociaciones espurias entre enfermedades —lo que hoy se conoce como **sesgo de Berkson**—. En econometría, James Heckman (1979) formuló el célebre **modelo de corrección de selección** (*Heckit*), que estima la probabilidad de inclusión en la muestra mediante una ecuación auxiliar (ecuación de selección) para corregir las estimaciones sustantivas. Este trabajo le valió el Premio Nobel de Economía en 2000 y sigue siendo referencia obligada en ciencias sociales cuantitativas.

En la ciencia política comparada, [[gary-king]], [[robert-keohane]] y [[sidney-verba]] (1994) alertaron sobre un caso particular de sesgo de selección: la **selección de casos por la variable dependiente**. Cuando un investigador estudia solo los casos en los que ocurrió el fenómeno de interés (e.g., revoluciones, guerras civiles), no puede observar variación en el resultado y, por tanto, no puede identificar relaciones causales válidas.

## Desarrollo teórico

El sesgo de selección puede clasificarse en varias modalidades según su mecanismo generador:

1. **Autoselección** (*self-selection bias*): los sujetos deciden participar en función de características relacionadas con el resultado. Por ejemplo, quienes se inscriben voluntariamente en un programa de capacitación laboral suelen estar más motivados que quienes no lo hacen, con lo cual el efecto medido del programa combina el tratamiento con la motivación previa.

2. **Sesgo de supervivencia** (*survivorship bias*): se analizan únicamente los casos que superaron un filtro previo, ignorando los que fueron eliminados. En sociología organizacional, estudiar solo las empresas que sobreviven conduce a sobreestimar la eficacia de ciertas estrategias gerenciales.

3. **Sesgo del voluntario** (*volunteer bias*): los participantes voluntarios poseen atributos distintos a los de la población general — mayor nivel educativo, mayor interés en el tema —, lo que distorsiona la generalización.

4. **Sesgo de Berkson**: la selección condicionada a una institución (hospital, cárcel, universidad) genera correlaciones artificiales entre variables que en la población general son independientes.

5. **Sesgo de selección por la variable dependiente**: como señalan King, Keohane y Verba (KKV), seleccionar casos según el valor del resultado impide estimar correctamente el efecto de las variables independientes, ya que se trunca la variación en $Y$. La recomendación metodológica es seleccionar por la [[variable-independiente]], lo que se aproxima al diseño experimental.

6. **Sesgo de colisionador** (*collider bias*): en el marco de los grafos causales de Judea Pearl (2009), condicionar el análisis sobre una variable que es efecto común de dos causas (*collider*) abre un camino espurio entre ellas, generando una [[relacion-espurea]]. Este mecanismo formaliza muchas formas de sesgo de selección dentro de la lógica de los modelos causales estructurales.

## Relación con otros conceptos

El sesgo de selección se inscribe en una red de problemas metodológicos interrelacionados. Compromete directamente la [[representatividad]] de la muestra y, con ella, la validez externa del estudio. A nivel interno, erosiona la [[validez-interna]] porque la asociación observada entre variables puede deberse al mecanismo de selección y no a una relación causal genuina. Está estrechamente vinculado a la [[endogeneidad]]: cuando la selección depende de la variable dependiente, las variables explicativas quedan correlacionadas con el término de error, violando los supuestos de los modelos de regresión. Los diseños de [[cuasiexperimento]] —como la regresión discontinua o el *propensity score matching*— constituyen estrategias para mitigar el sesgo de selección cuando la asignación aleatoria no es posible. Asimismo, un [[muestreo]] probabilístico bien diseñado es la primera línea de defensa contra este sesgo.

## Debates y críticas

Existen tensiones importantes en torno al sesgo de selección. En el debate cuantitativo-cualitativo, algunos autores argumentan que la advertencia de KKV contra la selección por la variable dependiente es excesiva para los estudios cualitativos comparados, donde la selección de casos responde a lógicas distintas (casos más similares, casos más diferentes) que no se reducen a la lógica estadística. Collier y Mahoney (1996) sostienen que la selección por la variable dependiente puede ser legítima si el objetivo es identificar condiciones necesarias, no causas probabilísticas.

En econometría, la corrección de Heckman ha sido criticada por su sensibilidad a los supuestos distribucionales (normalidad bivariada) y por las dificultades para encontrar un instrumento válido —una variable que afecte la selección pero no el resultado—. Métodos más recientes, como los estimadores de *bounds* parciales de Manski (1990) o el análisis de sensibilidad de Rosenbaum (2002), ofrecen alternativas menos dependientes de supuestos paramétricos.

## Vigencia contemporánea

El sesgo de selección sigue siendo un desafío central en la investigación social del siglo XXI. La proliferación de datos digitales (*Big Data*) no resuelve el problema: las muestras masivas provenientes de redes sociales, registros administrativos o plataformas digitales presentan sesgos de cobertura y autoselección que pueden ser más graves que los de las encuestas tradicionales. La «revolución de la credibilidad» en economía y ciencia política —con su énfasis en experimentos naturales, variables instrumentales y diseños de regresión discontinua— puede entenderse como una respuesta institucional al problema del sesgo de selección. Técnicas como el *propensity score matching*, la doble diferencia (*difference-in-differences*) y los modelos de efectos fijos son herramientas estándar del investigador contemporáneo para aproximarse a inferencias causales válidas en contextos observacionales.

## Ejemplo empírico

Un caso clásico es el estudio de los determinantes de las guerras civiles. Si un investigador analiza únicamente países que experimentaron conflicto armado (selección por la variable dependiente), puede concluir que la diversidad étnica es una causa necesaria del conflicto, puesto que muchos de esos países son étnicamente diversos. Sin embargo, al incluir en la muestra países diversos que *no* sufrieron guerras civiles, la correlación se debilita o desaparece. Fearon y Laitin (2003) demostraron precisamente esto: la diversidad étnica, una vez controlada por otros factores, no era un predictor significativo de guerra civil. El sesgo de selección por la variable dependiente había inflado artificialmente su aparente efecto causal.

## Véase también

- [[muestreo]]
- [[representatividad]]
- [[validez-interna]]
- [[endogeneidad]]
- [[relacion-espurea]]
- [[cuasiexperimento]]
- [[variable-independiente]]
- [[variable-dependiente]]
- [[seleccion-de-casos]]
- [[diseno-de-investigacion]]

## Fuentes

- King, Gary; Keohane, Robert O.; Verba, Sidney (2000). *El diseño de la investigación social: la inferencia científica en los estudios cualitativos*. Madrid: Alianza.
- Heckman, James J. (1979). "Sample Selection Bias as a Specification Error". *Econometrica*, 47(1), 153–161.
- Pearl, Judea (2009). *Causality: Models, Reasoning, and Inference*. 2.ª ed. Cambridge: Cambridge University Press.
- Collier, David; Mahoney, James (1996). "Insights and Pitfalls: Selection Bias in Qualitative Research". *World Politics*, 49(1), 56–91.
- Fearon, James D.; Laitin, David D. (2003). "Ethnicity, Insurgency, and Civil War". *American Political Science Review*, 97(1), 75–90.
- Sala, Gemma; Borge, Rosa; Padró-Solanet, Albert. "Procedimientos y decisiones para determinar qué se observará". Barcelona: FUOC (PID_00248675).
- [[procedimientos-y-decisiones-para-determinar-que-se-observara]] (Metodologia de las ciencias sociales)
