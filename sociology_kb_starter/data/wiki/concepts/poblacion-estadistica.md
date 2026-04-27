---
id: poblacion-estadistica
title: "Población estadística"
note_type: concept
semester: 2026-S1
course: "Metodologia de las ciencias sociales"
related_concepts:
  - muestra
  - muestreo
  - sesgo-de-seleccion
  - error-muestral
  - validez-externa
  - encuesta
tags:
  - metodologia
  - investigacion-cuantitativa
  - muestreo
  - inferencia-estadistica
source_notes:
  - wiki/sources/2026-s1/metodologia-de-las-ciencias-sociales/modulo-3.md
  - wiki/sources/2026-s1/metodologia-de-las-ciencias-sociales/la-investigacion-cuantitativa.md
updated_at: "2026-04-27"
---

## Definición

La **población estadística** es el conjunto total de unidades de análisis sobre las que una investigación pretende describir características o estimar parámetros. En sociología aplicada, esta definición debe precisar con rigor cuatro elementos: quiénes están incluidos, dónde están localizados, en qué periodo temporal se observan y bajo qué criterio de pertenencia se consideran parte del universo. Definir bien la población no es un paso formal, sino una decisión que condiciona todo el diseño de [[muestreo]], la interpretación del [[error-muestral]] y el alcance de la [[validez-externa]] de los resultados. Una población mal delimitada puede generar inferencias técnicamente correctas sobre una base empírica equivocada.

## Origen y contexto histórico

La distinción entre universo total y subconjunto observado se consolidó con el desarrollo de la estadística moderna entre finales del siglo XIX y el siglo XX. Anders Kiaer propuso en 1895 el «método representativo» como alternativa al [[censo]], abriendo el debate sobre cuándo una parte puede hablar por el todo. Jerzy Neyman, en su formalización de 1934, dio base matemática a la inferencia desde muestra hacia población, mostrando que la calidad de esa inferencia depende de una definición precisa del universo y de probabilidades de selección conocidas. En investigación social, esta preocupación se volvió central con la expansión de la [[encuesta]] en estudios de opinión, desigualdad y comportamiento político durante la posguerra.

Autores metodológicos como Leslie Kish (*Survey Sampling*, 1965) y Piergiorgio Corbetta (2003) insistieron en que la noción de población no se agota en una categoría abstracta («la ciudadanía», «la juventud»), sino que requiere una traducción operativa verificable para construir un marco muestral utilizable.

## Desarrollo teórico

En metodología cuantitativa, se diferencian tres niveles que suelen confundirse y que deben declararse explícitamente:

### Población objetivo

La **población objetivo** es el universo teórico al que se quiere generalizar. Responde a la pregunta sustantiva de investigación. Por ejemplo: «personas de 18 a 29 años residentes en áreas urbanas de España en 2026».

### Población accesible

La **población accesible** es la parte de la población objetivo que puede alcanzarse efectivamente con los recursos, el modo de contacto y las restricciones del estudio. Si la recogida es por internet y en castellano, quedan fuera quienes no tienen conexión estable o competencia lingüística suficiente para responder.

### Marco muestral

El **marco muestral** es el listado, registro o dispositivo concreto desde el que se seleccionan casos. Puede ser un padrón municipal, un listado telefónico o un panel online. El marco nunca es neutro: si no cubre adecuadamente la población accesible, aparece error de cobertura y aumenta el riesgo de [[sesgo-de-seleccion]].

Esta distinción es clave porque el [[error-muestral]] solo captura variabilidad aleatoria de la selección dentro del marco utilizado; no corrige sesgos sistemáticos por exclusión de segmentos sociales. Por eso, un margen de error pequeño no garantiza por sí mismo buena inferencia si la cobertura es deficiente. En términos de [[validez-externa]], la generalización solo es defendible cuando existe coherencia entre población objetivo, población accesible y marco muestral, además de un diseño de [[muestreo]] consistente.

## Relación con otros conceptos

- La [[muestra]] es un subconjunto de la población; su utilidad depende de que su proceso de selección preserve la estructura relevante del universo definido.
- El [[muestreo]] traduce la definición de población en reglas de selección, por lo que una mala delimitación poblacional arrastra errores de diseño en cadena.
- El [[sesgo-de-seleccion]] surge cuando ciertos perfiles tienen menor probabilidad de entrar en la muestra por problemas de acceso, cobertura o no respuesta.
- El [[error-muestral]] cuantifica incertidumbre aleatoria, pero no reemplaza la evaluación de errores no muestrales asociados a cobertura y medición.
- La [[validez-externa]] depende directamente de cómo se define la población de referencia y de la calidad de su representación empírica.

## Debates y críticas

Un debate contemporáneo central discute si las encuestas no probabilísticas de gran escala pueden sustituir a diseños probabilísticos clásicos. Sus defensores argumentan que el volumen de casos y los ajustes por ponderación compensan déficits de cobertura; sus críticos recuerdan que la ausencia de probabilidades de inclusión conocidas limita la interpretación inferencial.

También se debate el impacto de la no respuesta diferencial. Incluso con buen marco muestral, si responden más personas con mayor nivel educativo o más interés político, la muestra final puede desviarse de la población objetivo. Esto ha llevado a reforzar estrategias de seguimiento, incentivos y calibración post-estratificada, aunque ningún ajuste estadístico recupera por completo grupos ausentes sistemáticamente.

## Vigencia contemporánea

Hoy la discusión sobre población estadística está atravesada por dos problemas de cobertura. Primero, la expansión de encuestas online basadas en paneles de voluntariado introduce autoselección y sobrerrepresenta perfiles digitalmente activos. Segundo, la caída sostenida de tasas de respuesta en encuestas telefónicas y presenciales incrementa la distancia entre población accesible y población finalmente observada.

En consecuencia, buenas prácticas actuales recomiendan: documentar explícitamente la población objetivo, describir límites de acceso, auditar el marco muestral, reportar patrones de no respuesta y declarar con prudencia el alcance de generalización. La calidad metodológica ya no se evalúa solo por tamaño muestral, sino por transparencia sobre cobertura y exclusión.

## Ejemplo empírico

Un estudio urbano sobre uso desigual del espacio público nocturno en Madrid puede definir su **población objetivo** como «personas de 16 a 35 años que residen en distritos urbanos consolidados». La **población accesible** se restringe a quienes pueden ser contactadas en horario vespertino mediante combinación de encuesta web y entrevistas presenciales en nodos de transporte. El **marco muestral** integra dos fuentes: secciones censales para selección de puntos de interceptación y un registro municipal de hogares para invitaciones digitales.

Durante el trabajo de campo se detecta baja respuesta de mujeres jóvenes en franjas nocturnas y subcobertura de población migrante con alta movilidad residencial. El equipo ajusta cuotas de reemplazo, amplía horarios y aplica ponderaciones por distrito, sexo y origen. El caso muestra que definir población no es una decisión inicial cerrada, sino un proceso iterativo que afecta la interpretación del [[sesgo-de-seleccion]], la magnitud del [[error-muestral]] y la defensa de la [[validez-externa]] del estudio.

## Véase también

- [[muestra]]
- [[muestreo]]
- [[sesgo-de-seleccion]]
- [[error-muestral]]
- [[validez-externa]]
- [[representatividad]]
- [[encuesta]]
- [[censo]]

## Fuentes

- [[sources/2026-s1/metodologia-de-las-ciencias-sociales/modulo-3]] (Metodología de las Ciencias Sociales, 2026-S1)
- [[sources/2026-s1/metodologia-de-las-ciencias-sociales/la-investigacion-cuantitativa]] (Metodología de las Ciencias Sociales, 2026-S1)
- Neyman, J. (1934). On the Two Different Aspects of the Representative Method. *Journal of the Royal Statistical Society*, 97(4), 558-625.
- Kish, L. (1965). *Survey Sampling*. John Wiley & Sons.
- Corbetta, P. (2003). *Metodología y técnicas de investigación social*. McGraw-Hill.
- Groves, R. M., et al. (2009). *Survey Methodology* (2nd ed.). Wiley.
- Bethlehem, J. (2010). Selection Bias in Web Surveys. *International Statistical Review*, 78(2), 161-188.
