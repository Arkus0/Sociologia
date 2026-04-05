---
id: muestra
title: "Muestra"
note_type: concept
semester: 2026-S1
course: Metodologia de las ciencias sociales
related_concepts:
  - muestreo
  - muestreo-aleatorio
  - muestreo-estratificado
  - representatividad
  - encuesta
  - tamano-de-la-muestra
  - error-muestral
  - nivel-de-confianza
  - validez-externa
  - poblacion
  - inferencia-cientifica
tags:
  - metodologia
  - muestreo
  - estadistica
  - investigacion-cuantitativa
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\modulo-3.md
updated_at: "2026-04-05"
---

# Muestra

## Definicion

Una **muestra** es un subconjunto de una [[poblacion]] seleccionado con el proposito de estudiar las caracteristicas del conjunto mayor sin necesidad de examinar cada uno de sus elementos. En estadistica y ciencias sociales, la muestra constituye el fundamento operativo de la [[inferencia-cientifica]]: a partir de los datos obtenidos en el subconjunto, se estiman parametros poblacionales con un grado conocido de incertidumbre. La calidad de una investigacion empirica depende en gran medida de que la muestra sea **representativa**, es decir, que reproduzca en escala reducida la estructura y variabilidad de la poblacion de referencia. El vinculo entre muestra y poblacion esta mediado por el **marco muestral** (sampling frame), la lista o registro del que se extraen las unidades, y por el procedimiento de seleccion —probabilistico o no probabilistico— que determina la capacidad de generalizar los hallazgos.

## Origen

La idea de estudiar una parte para conocer el todo tiene antecedentes remotos: el sorteo por lotes aparece en textos biblicos y en practicas administrativas antiguas. En 1786, Pierre-Simon Laplace estimo la poblacion de Francia a partir de una muestra de comunas, calculando ademas cotas probabilisticas del error. Sin embargo, la formalizacion moderna del [[muestreo]] se situa a finales del siglo XIX y comienzos del XX. Anders Kiaer presento ante el Instituto Internacional de Estadistica (1895) la idea de la "muestra representativa", y Aleksandr Chuprov introdujo las encuestas muestrales en la Rusia imperial en la decada de 1870. El desarrollo teorico decisivo llego con Jerzy Neyman, quien en 1934 demostro las propiedades del [[muestreo-estratificado]] con asignacion optima, sentando las bases del muestreo probabilistico moderno.

## Desarrollo teorico

### Muestreo probabilistico

El principio central es que cada unidad de la poblacion debe tener una probabilidad conocida y positiva de ser seleccionada. Las modalidades principales son:

- **[[muestreo-aleatorio]] simple**: todos los subconjuntos de tamano *n* tienen igual probabilidad de ser elegidos. Minimiza el sesgo pero puede resultar ineficiente en poblaciones heterogeneas.
- **Muestreo sistematico**: se selecciona una unidad cada *k* elementos (coeficiente de elevacion *N/n*), con un arranque aleatorio. Es sencillo de aplicar y genera una distribucion uniforme a lo largo del marco muestral.
- **[[muestreo-estratificado]]**: la poblacion se divide en estratos internamente homogeneos y se extrae una submuestra de cada uno. Neyman demostro que la asignacion optima del tamano de submuestra a cada estrato reduce la varianza total del estimador.
- **Muestreo por conglomerados**: la unidad de seleccion es un grupo natural (barrio, hospital, escuela). Es mas economico cuando no se dispone de un listado completo de individuos.
- **Muestreo polietapico**: combina estratificacion, conglomerados y, en ocasiones, cuotas finales. Las grandes [[encuesta]]s de opinion —como el CIS en Espana— utilizan este procedimiento: comunidad autonoma → municipio → seccion censal → ruta → vivienda → cuotas de edad, sexo y situacion laboral.

### Muestreo no probabilistico

Cuando la probabilidad de seleccion no puede determinarse, se habla de muestreo no probabilistico. Incluye:

- **Muestreo por conveniencia**: se eligen los casos mas accesibles; util para estudios piloto pero con limitada [[validez-externa]].
- **Muestreo intencional (purposive)**: el investigador selecciona casos que ilustran el fenomeno de interes. Michael Quinn Patton sistematizo esta logica para la investigacion cualitativa.
- **Muestreo de bola de nieve**: cada participante recluta a otros; es indispensable para poblaciones ocultas o de dificil acceso.
- **Muestreo por cuotas**: se fijan proporciones segun variables demograficas, pero la seleccion dentro de cada cuota no es aleatoria.
- **Muestreo teorico**: propuesto por Barney Glaser y Anselm Strauss en el marco de la teoria fundamentada (grounded theory), la seleccion de casos se guia por la emergencia de categorias analiticas hasta alcanzar la saturacion teorica.

### Tamano de la muestra y precision

El [[tamano-de-la-muestra]] depende de la variabilidad de la poblacion, el [[nivel-de-confianza]] deseado y el margen de [[error-muestral]] aceptable. Para poblaciones grandes, la formula clasica es: *n = Z² · p · q / ε²*. El **teorema central del limite** garantiza que, con muestras suficientemente grandes, la distribucion muestral de la media se aproxima a la normal, lo que permite construir intervalos de confianza y realizar contrastes de hipotesis independientemente de la forma de la distribucion poblacional. La potencia estadistica (poder) indica la probabilidad de detectar un efecto real y se incorpora al calculo del tamano muestral.

## Relacion con otros conceptos

La muestra es inseparable del concepto de [[representatividad]]: una muestra es representativa cuando reproduce la distribucion de las caracteristicas relevantes de la poblacion. El [[error-muestral]] mide la discrepancia entre el estimador muestral y el parametro poblacional; se reduce al aumentar *n* y al utilizar disenos eficientes como la estratificacion. El [[nivel-de-confianza]] expresa la probabilidad de que el intervalo construido contenga el valor real del parametro. La [[validez-externa]] de una investigacion —su capacidad para generalizar resultados— depende directamente de la calidad del muestreo. Por su parte, la [[encuesta]] es el instrumento metodologico que con mayor frecuencia emplea muestras probabilisticas a gran escala.

## Debates y criticas

El episodio mas emblematico sobre los riesgos del muestreo deficiente es el fiasco de la revista *Literary Digest* en 1936: envio cuestionarios a mas de diez millones de personas, obtuvo dos millones de respuestas y predijo la victoria de Alf Landon sobre Franklin D. Roosevelt. El marco muestral —listas de suscriptores de revistas, directorios telefonicos y registros de automoviles— sobrerepresentaba a los sectores acomodados y republicanos. Ese mismo ano, George Gallup, con una muestra de apenas 50.000 casos pero seleccionada con criterios de cuota mas equilibrados, acerto el resultado. El contraste demostro que el tamano de la muestra importa menos que su diseno.

Leslie Kish, en su obra clasica *Survey Sampling* (1965), sistematizo los principios del muestreo probabilistico y advirtio que la representatividad no se logra solo con grandes numeros sino con procedimientos de seleccion rigurosos. Ronald Fisher habia defendido antes la aleatorizacion como garantia de validez inferencial, tanto en muestreo como en diseno experimental.

En el ambito cualitativo, la nocion de muestra se reconfigura: Glaser y Strauss propusieron el muestreo teorico, y Patton desarrollo tipologias de muestreo intencional donde la logica no es la generalizacion estadistica sino la profundidad analitica.

## Vigencia contemporanea

La era digital ha transformado el muestreo. Las encuestas en linea y los paneles web no probabilisticos ofrecen rapidez y bajo costo, pero plantean problemas de cobertura y autoseleccion. El argumento de que el *big data* hace innecesario el muestreo —la tesis del "N = todos"— ha sido criticado por autores como danah boyd y Kate Crawford, quienes senalan que los datos masivos no estan exentos de sesgos sistematicos. Joseph Henrich y colaboradores acunaron el acronimo WEIRD (Western, Educated, Industrialized, Rich, Democratic) para denunciar que la mayor parte de la investigacion psicologica y social se basa en muestras no representativas de la diversidad humana global. Estos debates subrayan que la reflexion sobre la muestra sigue siendo central para la validez de cualquier empresa cientifica.

## Ejemplo empirico

En las elecciones presidenciales estadounidenses de 1936, la revista *Literary Digest* envio cuestionarios postales a 10 millones de personas y recogio 2,4 millones de respuestas, prediciendo una victoria de Landon con el 57 % de los votos. El marco muestral estaba sesgado hacia hogares con telefono y suscripciones a revistas —sectores desproporcionadamente republicanos—. Simultaneamente, George Gallup utilizo una muestra de cuota de 50.000 personas y predijo correctamente la reeleccion de Roosevelt. El caso ilustra que la [[representatividad]] del procedimiento de seleccion es mas determinante que el volumen de datos recogidos, un principio que Kish formalizaria tres decadas despues.

## Vease tambien

- [[muestreo]]
- [[muestreo-aleatorio]]
- [[muestreo-estratificado]]
- [[representatividad]]
- [[encuesta]]
- [[tamano-de-la-muestra]]
- [[error-muestral]]
- [[nivel-de-confianza]]
- [[validez-externa]]
- [[poblacion]]
- [[inferencia-cientifica]]
- [[proceso-de-investigacion]]

## Fuentes

- Kish, L. (1965). *Survey Sampling*. Wiley.
- Neyman, J. (1934). On the Two Different Aspects of the Representative Method. *Journal of the Royal Statistical Society*, 97(4), 558–625.
- Fisher, R. A. (1935). *The Design of Experiments*. Oliver & Boyd.
- Cochran, W. G. (1977). *Sampling Techniques* (3.ª ed.). Wiley.
- Glaser, B. y Strauss, A. (1967). *The Discovery of Grounded Theory*. Aldine.
- Patton, M. Q. (2002). *Qualitative Research and Evaluation Methods* (3.ª ed.). Sage.
- Henrich, J., Heine, S. J. y Norenzayan, A. (2010). The Weirdest People in the World? *Behavioral and Brain Sciences*, 33(2–3), 61–83.
- Borge Bravo, R. y Padro-Solanet, A. (2026). La investigacion cuantitativa. Modulo 3, Metodologia de las ciencias sociales, UOC.
- [[la-investigacion-cuantitativa]] (Metodologia de las ciencias sociales)
