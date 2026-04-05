---
id: variable-interviniente
title: "Variable interviniente"
note_type: concept
semester: 2026-S1
course: Metodología de las ciencias sociales
related_concepts:
  - variable-dependiente
  - variable-independiente
  - variable-de-control
  - causalidad
  - correlacion
  - regresion
  - problema-de-la-caja-negra
  - hipotesis
  - relacion-espurea
tags:
  - Metodología de las ciencias sociales
  - Variables
  - Causalidad
  - Mediación
  - Diseño de investigación
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\el-proceso-de-formulacion-teorica.md
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\el-proceso-de-investigacion-en-las-ciencias-sociales.md
updated_at: '2026-04-05T22:00:00+00:00'
---

# Variable interviniente

## Definición

La **variable interviniente** —también denominada variable mediadora— es aquella que se sitúa en la cadena causal entre una [[variable-independiente]] (X) y una [[variable-dependiente]] (Y), de modo que explica el *mecanismo* a través del cual X produce su efecto sobre Y. El esquema básico es X → M → Y: la variable independiente influye en la mediadora, y esta, a su vez, influye en la dependiente. Si al introducir M en el modelo la relación directa entre X e Y se reduce sustancialmente o desaparece, se concluye que M media —total o parcialmente— dicha relación. En la literatura metodológica en castellano se habla de variable interviniente; en la tradición anglosajona se emplea el término *mediator variable* o *intervening variable*.

## Origen y contexto histórico

El concepto de variable interviniente proviene de la psicología conductista de mediados del siglo XX. Edward C. Tolman (1938) introdujo la noción de *intervening variables* para explicar procesos cognitivos inobservables que mediaban entre estímulo y respuesta. En ciencias sociales, la idea se consolidó con la formulación del método hipotético-deductivo y la tipología de variables propuesta por Manheim y Rich (1988), quienes distinguieron entre variable dependiente, independiente, interviniente, antecedente y [[variable-de-control]]. Baron y Kenny (1986) formalizaron los pasos estadísticos para el análisis de mediación, estableciendo un procedimiento que se convirtió en referencia estándar durante décadas.

## Desarrollo teórico

Según Borge Bravo y Padró-Solanet, en el sistema de variables de una [[hipotesis]], la variable interviniente ocupa una posición intermedia que conecta la causa propuesta con el efecto observado. Su inclusión obedece a una exigencia epistémica: establecer no solo que X y Y covarían, sino *por qué* lo hacen. El modelo clásico de mediación requiere demostrar tres relaciones: (1) X predice significativamente a Y, (2) X predice significativamente a M, y (3) al controlar M, el efecto de X sobre Y se reduce o anula. Cuando la relación X → Y desaparece por completo se habla de mediación total; cuando solo se atenúa, de mediación parcial. Desarrollos posteriores —como el test de Sobel y el método de bootstrapping de Preacher y Hayes— han perfeccionado la evaluación estadística de estos efectos indirectos, superando las limitaciones de potencia y supuestos de normalidad del procedimiento original.

## Relación con otros conceptos

La variable interviniente se distingue de otros tipos de terceras variables. La [[variable-de-control]] es una variable cuyo efecto se neutraliza para evitar una [[relacion-espurea]]: si T causa simultáneamente a X y a Y, la relación observada entre estas últimas puede ser espuria. La variable moderadora, en cambio, altera la *intensidad* o la *dirección* de la relación X → Y según sus niveles, sin formar parte de la cadena causal. El [[problema-de-la-caja-negra]], señalado en la bibliografía del curso, describe precisamente la situación en la que se conoce la [[correlacion]] entre variables pero se ignoran los mecanismos intermedios: la variable interviniente es la herramienta conceptual para abrir esa caja negra. Asimismo, la [[omision-de-variables]] relevantes —incluida la variable mediadora— puede conducir a estimaciones sesgadas del efecto causal, problema central en el análisis de [[regresion]].

## Debates y críticas

El análisis de mediación no está exento de controversia. En primer lugar, el procedimiento de Baron y Kenny ha sido criticado por su baja potencia estadística y por exigir un efecto total significativo como paso previo, requisito que Hayes (2009) calificó de innecesario. En segundo lugar, la mediación estadística es fundamentalmente correlacional: la mera reducción del coeficiente de X al incluir M no garantiza que M sea el mecanismo causal real, ya que podrían existir variables confusoras no observadas que afecten tanto a M como a Y. Judea Pearl (2001) ha propuesto un enfoque causal basado en contrafactuales y el operador *do*, que permite distinguir rigurosamente entre efectos directos e indirectos sin depender del supuesto de ausencia de confusión. En ciencias sociales, donde la experimentación es a menudo inviable, estas limitaciones adquieren particular relevancia.

## Vigencia contemporánea

En la investigación social actual, el análisis de mediación se ha integrado en marcos más amplios de inferencia causal. Los modelos de ecuaciones estructurales (SEM), el análisis de mediación causal de Pearl y los diseños mixtos que combinan métodos cuantitativos y cualitativos permiten abordar con mayor rigor la identificación de mecanismos. La [[causalidad]] en ciencias sociales exige no solo covariación y precedencia temporal, sino un argumento teórico sobre el proceso intermedio, requisito que sitúa a la variable interviniente en el centro de la explicación científica contemporánea.

## Ejemplo empírico

Supóngase que se investiga por qué el nivel educativo de los padres (X) influye en el rendimiento académico de los hijos (Y). Una hipótesis plausible es que la educación parental eleva la disponibilidad de recursos culturales en el hogar —libros, actividades, expectativas académicas— (M), y son estos recursos los que inciden directamente en el rendimiento. Si al controlar M la relación X → Y se reduce significativamente, se concluye que los recursos culturales actúan como variable interviniente, proporcionando una explicación mecanística que supera la mera constatación de la correlación.

## Véase también

- [[variable-dependiente]]
- [[variable-independiente]]
- [[variable-de-control]]
- [[causalidad]]
- [[problema-de-la-caja-negra]]
- [[relacion-espurea]]
- [[hipotesis]]
- [[regresion]]

## Fuentes

- Borge Bravo, R. y Padró-Solanet, A. *El proceso de formulación teórica*. Metodología de las Ciencias Sociales, UOC, 2026-S1.
- Borge Bravo, R. y Padró-Solanet, A. *El proceso de investigación en las ciencias sociales: marco teórico y diseño empírico*. Metodología de las Ciencias Sociales, UOC, 2026-S1.
- Baron, R. M. y Kenny, D. A. (1986). «The Moderator-Mediator Variable Distinction in Social Psychological Research». *Journal of Personality and Social Psychology*, 51(6), 1173–1182.
- Hayes, A. F. (2009). «Beyond Baron and Kenny: Statistical Mediation Analysis in the New Millennium». *Communication Monographs*, 76(4), 408–420.
- Pearl, J. (2001). «Direct and Indirect Effects». *Proceedings of the 17th Conference on Uncertainty in Artificial Intelligence*, 411–420.
- MacKinnon, D. P. (2008). *Introduction to Statistical Mediation Analysis*. New York: Erlbaum.
