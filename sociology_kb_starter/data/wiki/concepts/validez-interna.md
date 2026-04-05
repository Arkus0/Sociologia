---
id: validez-interna
title: "Validez interna"
note_type: concept
semester: 2026-S1
course: Metodologia de las ciencias sociales
related_concepts:
  - validez-externa
  - causalidad
  - experimento
  - cuasiexperimento
  - endogeneidad
  - hipotesis
  - diseno-de-investigacion
  - grupo-de-control
  - operacionalizacion
  - variable-dependiente
tags:
  - metodologia
  - causalidad
  - diseno-experimental
  - inferencia-causal
  - validez
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\el-proceso-de-formulacion-teorica.md
updated_at: "2026-04-05"
---

# Validez interna

## Definicion

La **validez interna** es el grado en que un estudio permite establecer conclusiones causales legitimas entre una [[variable-independiente]] y una [[variable-dependiente]], descartando explicaciones alternativas plausibles. Un diseño posee alta validez interna cuando la variacion observada en el efecto puede atribuirse con confianza a la causa manipulada o identificada, y no a factores extraños, sesgos sistematicos o variables de confusion. Tres condiciones clasicas sustentan una inferencia causal internamente valida: precedencia temporal de la causa sobre el efecto, covariacion entre ambas variables y ausencia de explicaciones rivales verosimiles (Shadish, Cook y Campbell, 2002). La validez interna constituye, junto con la [[validez-externa]], uno de los pilares de la calidad de la evidencia empirica en ciencias sociales.

## Origen

El concepto fue formalizado por Donald T. Campbell y Julian C. Stanley en *Experimental and Quasi-Experimental Designs for Research* (1963), obra en la que sistematizaron ocho amenazas clasicas a la validez interna: historia, maduracion, efecto del test, instrumentacion, regresion a la media, seleccion diferencial, mortalidad experimental e interaccion seleccion-maduracion. Campbell y Stanley argumentaron que el [[experimento]] con asignacion aleatoria —el *gold standard*— era el [[diseno-de-investigacion]] que mejor neutralizaba estas amenazas al distribuir aleatoriamente las diferencias preexistentes entre el grupo experimental y el [[grupo-de-control]]. La tipologia surgio en un contexto de expansion de la investigacion educativa y psicologica de posguerra, donde proliferaban estudios observacionales cuyos resultados eran dificiles de interpretar causalmente.

## Desarrollo teorico

La obra posterior de Campbell y Cook (*Quasi-Experimentation*, 1979) amplio el catalogo de amenazas e introdujo estrategias para fortalecer la validez interna sin recurrir a la aleatorizacion pura, inaugurando el campo del [[cuasiexperimento]]. Shadish, Cook y Campbell (2002) consolidaron la sintesis definitiva, organizando la validez en cuatro tipos —interna, externa, de constructo y de conclusion estadistica— y subrayando que la validez interna es cuestion de grado, no de todo o nada.

Paralelamente, el marco contrafactual aportado por Donald Rubin (modelo causal de Rubin) y Jerzy Neyman reformulo la validez interna en terminos de resultados potenciales: un efecto causal se define como la diferencia entre el resultado observado bajo tratamiento y el resultado que se habria observado sin el. La asignacion aleatoria garantiza que, en expectativa, ambos grupos son intercambiables, lo que elimina la [[endogeneidad]] —situacion en la que la variable explicativa esta correlacionada con el termino de error, violando la validez interna—. Karl Popper, desde la filosofia de la ciencia, sostuvo que una inferencia causal solo es valida si las [[hipotesis]] rivales han sido sometidas a intentos genuinos de refutacion; la validez interna, en este sentido, expresa la capacidad del diseño para eliminar explicaciones alternativas.

En la econometria aplicada, Angrist y Pischke (2009) impulsaron la llamada *revolucion de la credibilidad*, promoviendo tecnicas de identificacion causal —variables instrumentales, regresion discontinua, diferencias en diferencias— que buscan aproximar la logica experimental en contextos observacionales, reforzando la validez interna sin necesidad de control de laboratorio.

## Relacion con otros conceptos

La validez interna se encuentra en tension productiva con la [[validez-externa]]: un [[experimento]] de laboratorio altamente controlado maximiza la primera pero puede sacrificar la segunda al crear condiciones artificiales no generalizables. Esta tension aparece de forma explicita en Merton (1957), quien propuso las *teorias de alcance medio* como equilibrio entre ambas exigencias. El [[diseno-de-investigacion]] es el mecanismo practico mediante el cual se gestionan las amenazas: la asignacion aleatoria al [[grupo-de-control]], el cegamiento y la estandarizacion de instrumentos son salvaguardas clasicas. La [[operacionalizacion]] rigurosa de las variables tambien contribuye a la validez interna al reducir el error de medicion sistematico. Cuando la [[endogeneidad]] no puede resolverse por diseño, tecnicas econometricas como las variables instrumentales intentan restaurar la identificacion causal.

## Debates y criticas

La critica mas persistente proviene de la ecologia de la investigacion: los diseños que maximizan la validez interna suelen operar en entornos controlados que difieren sustancialmente del mundo social real, generando lo que Schram (2005) llamo el *problema de la validez interna mutua* —un circuito cerrado entre experimentos y teorias que solo explican fenomenos de laboratorio—. Friedrich Hayek advirtio sobre los limites de la experimentacion en sistemas sociales complejos, donde la multiplicidad de variables interactuantes hace impracticable el control exhaustivo. Desde la tradicion cualitativa, Lincoln y Guba (1985) propusieron criterios alternativos de rigor —credibilidad, transferibilidad, dependabilidad y confirmabilidad— que desplazan la logica experimental y cuestionan la universalidad de la validez interna como estandar. Tambien se ha señalado que la obsesion por la validez interna puede conducir a la *investigacion de preguntas pequeñas*: diseños impecables que responden a interrogantes triviales porque solo estos admiten manipulacion experimental.

## Vigencia contemporanea

En la ciencia social contemporanea, la validez interna sigue siendo el criterio central de la inferencia causal. La *revolucion de la credibilidad* ha trasladado sus exigencias a la investigacion observacional: los articulos en revistas de primer nivel deben presentar una *estrategia de identificacion* que justifique por que la estimacion captura un efecto causal y no una mera asociacion. Al mismo tiempo, el auge del analisis de datos masivos (*big data*) ha reavivado el debate, pues las correlaciones a gran escala no garantizan validez interna sin un diseño causal explícito. Las preregistraciones de estudios y las replicaciones sistematicas representan esfuerzos institucionales por fortalecer simultaneamente la validez interna y la transparencia del proceso investigador.

## Ejemplo empirico

Un caso clasico es la evaluacion del programa *Head Start* en Estados Unidos, que buscaba mejorar el rendimiento educativo de niños de familias desfavorecidas. Los primeros estudios observacionales encontraron efectos positivos, pero su validez interna era cuestionable porque las familias que inscribian a sus hijos podian diferir sistematicamente de las que no lo hacian (sesgo de seleccion). Estudios posteriores utilizaron la regresion discontinua —aprovechando los umbrales de elegibilidad— para aproximar una comparacion cuasiexperimental, fortaleciendo la validez interna de las conclusiones sobre el efecto causal del programa.

## Vease tambien

- [[validez-externa]]
- [[experimento]]
- [[cuasiexperimento]]
- [[causalidad]]
- [[endogeneidad]]
- [[hipotesis]]
- [[diseno-de-investigacion]]
- [[grupo-de-control]]
- [[operacionalizacion]]
- [[variable-dependiente]]
- [[variable-independiente]]

## Fuentes

- Campbell, D. T. y Stanley, J. C. (1963). *Experimental and Quasi-Experimental Designs for Research*. Chicago: Rand McNally.
- Cook, T. D. y Campbell, D. T. (1979). *Quasi-Experimentation: Design and Analysis Issues for Field Settings*. Boston: Houghton Mifflin.
- Shadish, W. R., Cook, T. D. y Campbell, D. T. (2002). *Experimental and Quasi-Experimental Designs for Generalized Causal Inference*. Boston: Houghton Mifflin.
- Angrist, J. D. y Pischke, J.-S. (2009). *Mostly Harmless Econometrics*. Princeton: Princeton University Press.
- Lincoln, Y. S. y Guba, E. G. (1985). *Naturalistic Inquiry*. Beverly Hills: Sage.
- Popper, K. R. (1959). *The Logic of Scientific Discovery*. Londres: Hutchinson.
- Hayek, F. A. (1952). *The Counter-Revolution of Science*. Glencoe: Free Press.
- Borge Bravo, R. y Padro-Solanet i Grau, A. (2026). El proceso de formulacion teorica. En *Metodologia de las ciencias sociales*, UOC [fuente del curso].
