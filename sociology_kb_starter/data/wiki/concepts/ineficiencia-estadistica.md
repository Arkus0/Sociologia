---
id: ineficiencia-estadistica
title: "Ineficiencia estadística"
note_type: concept
semester: 2026-S1
course: Metodología de las ciencias sociales
related_concepts:
  - regresion
  - varianza
  - error-muestral
  - tamano-de-la-muestra
  - nivel-de-confianza
  - variable-de-control
  - multicolinealidad
  - estadistica-inferencial
  - ineficiencia-inclusion-de-variables-irrelevantes
tags:
  - metodología
  - estadística
  - estimación
  - diseño-de-investigación
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\modulo-2.md
updated_at: '2026-04-05T22:00:00+00:00'
---

# Ineficiencia estadística

## Definición

La **ineficiencia estadística** designa la pérdida de precisión en la estimación de parámetros cuando un modelo incluye variables irrelevantes o emplea procedimientos de estimación subóptimos. Un estimador ineficiente presenta una [[varianza]] mayor de la necesaria para obtener una estimación insesgada del parámetro de interés, lo que se traduce en intervalos de confianza más amplios y menor potencia estadística. En el contexto de la investigación social, la ineficiencia se manifiesta típicamente cuando se introducen demasiadas [[variable-de-control|variables de control]] en un modelo de [[regresion|regresión]], fenómeno conocido como sobreajuste (*overfitting*), o cuando el diseño muestral no aprovecha de forma óptima la información disponible.

## Origen y contexto histórico

El concepto de eficiencia estadística fue formalizado por Ronald A. Fisher en 1921, al establecer la cota inferior de Cramér-Rao: la varianza de cualquier estimador insesgado no puede ser menor que el inverso de la información de Fisher. Un estimador que alcanza esa cota se denomina *eficiente*; todo estimador que no la alcance es, por definición, ineficiente. A lo largo del siglo XX, la noción se integró en la econometría y en las ciencias sociales cuantitativas a través de los mínimos cuadrados ordinarios (MCO) y del teorema de Gauss-Markov, que garantiza que MCO es el estimador lineal insesgado de mínima varianza bajo supuestos clásicos.

## Desarrollo teórico

La ineficiencia puede originarse por diversas vías. La más relevante para la investigación social es la **inclusión de variables irrelevantes** en un modelo explicativo. Según King, Keohane y Verba (2000), cuando se añaden variables independientes que carecen de relación causal con la variable dependiente, la [[varianza]] de los coeficientes estimados aumenta sin que se reduzca el sesgo. Esto ocurre porque cada variable adicional consume grados de libertad y dispersa la capacidad explicativa del modelo.

Formalmente, si un estimador insesgado $T$ tiene varianza $\text{Var}(T)$ superior al límite de Cramér-Rao $I(\theta)^{-1}$, su eficiencia relativa $e(T) = I(\theta)^{-1} / \text{Var}(T)$ será inferior a 1. Cuanto más se aleje de la unidad, mayor será la ineficiencia. En la práctica, esto implica que se necesitaría un [[tamano-de-la-muestra|tamaño de muestra]] proporcionalmente mayor para alcanzar el mismo [[nivel-de-confianza|nivel de confianza]] que un estimador eficiente.

Además, la presencia de [[multicolinealidad]] entre las variables incluidas agrava la ineficiencia, pues infla la varianza de los coeficientes de las variables correlacionadas entre sí, dificultando la identificación del efecto individual de cada una.

## Relación con otros conceptos

La ineficiencia se distingue del **sesgo por omisión de variables**: mientras que omitir una variable relevante introduce sesgo sistemático en las estimaciones, incluir una variable irrelevante no sesga los coeficientes pero incrementa su varianza. Sala, Borge y Padró-Solanet lo sintetizan así: la omisión de variables relevantes produce sesgo; la [[ineficiencia-inclusion-de-variables-irrelevantes|inclusión de variables irrelevantes]] produce ineficiencia. Ambos problemas forman parte del conjunto de amenazas a la validez en la selección de variables del [[diseno-de-investigacion-empirica|diseño de investigación]].

La ineficiencia guarda relación directa con el [[error-muestral]], pues un estimador ineficiente amplifica la incertidumbre asociada a la muestra. También se vincula con la [[estadistica-inferencial]], ya que intervalos de confianza más anchos reducen la capacidad de rechazar hipótesis nulas falsas.

## Debates y críticas

Existe un debate metodológico sobre el equilibrio entre sesgo e ineficiencia. Algunos investigadores prefieren incluir variables de control adicionales para evitar el sesgo por omisión, aun a costa de cierta ineficiencia. Otros argumentan que la proliferación de controles puede ser tan perjudicial como la omisión si reduce la potencia estadística hasta impedir la detección de efectos reales. La estrategia óptima depende del tamaño muestral y del conocimiento teórico previo sobre las relaciones causales.

Asimismo, desde la estadística robusta se señala que un estimador eficiente para una distribución concreta puede resultar muy ineficiente cuando la distribución real difiere de la supuesta, por ejemplo ante la presencia de valores atípicos. Esto ha motivado el uso de estimadores M y de métodos resistentes que sacrifican eficiencia teórica a cambio de mayor estabilidad.

## Vigencia contemporánea

Con la disponibilidad de grandes bases de datos en ciencias sociales, el riesgo de ineficiencia por sobreajuste se ha intensificado. Las técnicas de selección de modelos —como los criterios de información de Akaike (AIC) y bayesiano (BIC)— permiten evaluar formalmente si la inclusión de variables adicionales mejora el ajuste lo suficiente como para compensar la pérdida de grados de libertad. Los métodos de regularización (LASSO, Ridge) ofrecen alternativas que penalizan la complejidad del modelo y reducen la ineficiencia derivada de la sobreparametrización.

## Ejemplo empírico

Supóngase un estudio que analiza el efecto de la educación sobre la participación electoral, controlando por edad, ingreso, género y región. Si el investigador añade además variables como el color favorito o la estatura de los encuestados —sin justificación teórica—, los coeficientes de las variables relevantes mantendrán su insesgadez, pero su [[varianza]] aumentará. El resultado será que el efecto de la educación, aunque correctamente estimado en promedio, tendrá un intervalo de confianza más amplio, y es posible que no alcance significación estadística pese a existir un efecto real. La ineficiencia habrá reducido la potencia del test.

## Véase también

- [[regresion]]
- [[varianza]]
- [[error-muestral]]
- [[multicolinealidad]]
- [[ineficiencia-inclusion-de-variables-irrelevantes]]
- [[seleccion-de-variables]]
- [[estadistica-inferencial]]
- [[variable-de-control]]

## Fuentes

- Sala, Gemma; Borge, Rosa; Padró-Solanet, Albert. "Procedimientos y decisiones para determinar qué se observará". Barcelona: FUOC (PID_00248675).
- King, Gary; Keohane, Robert O.; Verba, Sidney (2000). *El diseño de la investigación social*. Madrid: Alianza.
- Fisher, Ronald A. (1921). "On the Mathematical Foundations of Theoretical Statistics". *Philosophical Transactions of the Royal Society of London A*, 222, 309–368.
- Greene, William H. (2012). *Econometric Analysis* (7.ª ed.). Boston: Pearson.
