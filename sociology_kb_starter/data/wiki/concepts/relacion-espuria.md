---
id: relacion-espuria
title: "Relación espúrea"
note_type: concept
semester: 2026-S1
course: "Metodologia de las ciencias sociales"
related_concepts:
  - correlacion
  - causalidad
  - variable-de-control
  - endogeneidad
  - regresion
  - omision-de-variables
  - operacionalizacion
  - hipotesis
tags:
  - metodología
  - causalidad
  - estadística
  - confusión
  - Lazarsfeld
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\el-proceso-de-investigacion-en-las-ciencias-sociales.md
updated_at: "2026-04-06"
---

# Relación espúrea

## Definición

Una **relación espúrea** (del latín *spurius*, ilegítimo) es una asociación estadística aparente entre dos variables que no refleja un vínculo causal genuino entre ellas, sino que se explica por la influencia de una o varias terceras variables no contempladas en el análisis. Formalmente, si se observa una [[correlacion]] entre X e Y, la relación es espúrea cuando existe una variable confundente W tal que W → X y W → Y, de modo que al controlar W la asociación original desaparece o se reduce drásticamente. La máxima metodológica que condensa este fenómeno es el célebre principio «correlación no implica [[causalidad]]».

En la investigación social empírica, la detección de relaciones espúreas constituye una exigencia ineludible para establecer inferencias causales válidas. Los materiales de la asignatura subrayan que toda relación causal fuerte debe satisfacer cuatro criterios simultáneos: (1) covariación entre X e Y, (2) precedencia temporal de X respecto a Y, (3) mecanismo causal explicable, y (4) ausencia de relación espúrea introducida por una variable T confundente.

## Origen y contexto histórico

La preocupación por distinguir asociaciones genuinas de asociaciones engañosas tiene raíces profundas. Ya **David Hume** (1739) advirtió que la mente humana tiende a inferir conexiones causales a partir de la mera conjunción repetida de eventos, confundiendo regularidad observada con necesidad causal. Karl Pearson, a comienzos del siglo XX, reconoció que las correlaciones estadísticas podían surgir de factores compartidos y no de nexos directos, mientras que George Udny Yule (1926) demostró en su estudio sobre correlaciones espurias en series temporales que tendencias comunes podían generar coeficientes de correlación elevados entre variables causalmente inconexas.

Sin embargo, la elaboración más influyente para las ciencias sociales proviene de **Paul F. Lazarsfeld** y su escuela en la Universidad de Columbia. En las décadas de 1940 y 1950, Lazarsfeld sistematizó el *paradigma de elaboración* (*elaboration paradigm*): un procedimiento analítico consistente en introducir una tercera variable, el *test factor* o factor de prueba, en una relación bivariada para determinar si la asociación original persiste, desaparece o se modifica. Si al controlar la variable T la relación entre X e Y se desvanece, se concluye que era espúrea; si persiste, la relación resiste la prueba de espuriedad. Este procedimiento, desarrollado en colaboración con Patricia Kendall y expuesto en *The Language of Social Research* (1955), se convirtió en piedra angular de la metodología cuantitativa en sociología.

## Desarrollo teórico

### El paradigma de elaboración de Lazarsfeld

El esquema lazarsfeldiano distingue varios escenarios al introducir una [[variable-de-control]]:

- **Espuriedad** (*explanation*): la relación X-Y desaparece al controlar T, porque T es causa común de ambas. La asociación original era un artefacto.
- **Intermediación** (*interpretation*): la relación X-Y desaparece al controlar T, pero T es un mecanismo intermedio (X → T → Y). La relación es genuina; T explica el cómo.
- **Especificación** (*specification*): la relación X-Y persiste solo en ciertos niveles de T (interacción o moderación).

La distinción entre espuriedad e intermediación es teórica, no puramente estadística: exige conocimiento sustantivo del orden causal entre las variables, lo que vincula la técnica estadística con el [[marco-teorico]] del investigador.

### La revolución causal: Pearl y los grafos dirigidos

**Judea Pearl** formalizó el problema de la confusión mediante los *grafos acíclicos dirigidos* (DAGs). En su marco, una variable confundente (*confounder*) es aquella que tiene caminos causales dirigidos tanto hacia la variable de tratamiento como hacia el resultado, generando una asociación no causal, un «camino de puerta trasera» (*back-door path*). El **criterio de puerta trasera** (*back-door criterion*) establece que, para estimar el efecto causal de X sobre Y, basta con condicionar sobre un conjunto de variables que bloquee todos los caminos de puerta trasera sin bloquear ningún camino causal directo. Esta formalización superó la intuición lazarsfeldiana al proporcionar un algoritmo general para identificar qué variables deben controlarse y cuáles no.

### La paradoja de Simpson

Un caso extremo de relación espúrea es la **paradoja de Simpson**: una asociación que se invierte al desagregar los datos por una variable confundente. El ejemplo clásico procede del caso de admisión en la Universidad de Berkeley (1973), donde la tasa global de admisión parecía discriminar a las mujeres, pero al desagregar por departamento la tendencia se invertía, porque las mujeres postulaban preferentemente a departamentos más competitivos. La paradoja ilustra que las relaciones espúreas no solo distorsionan la magnitud de una asociación, sino que pueden invertir su dirección.

## Relación con otros conceptos

La relación espúrea se inserta en una red conceptual densa. La [[correlacion]] es la medida estadística que cuantifica la asociación bivariada susceptible de ser espúrea. La [[causalidad]] es el estándar al que aspira la investigación empírica y del que la espuriedad es la principal amenaza. La [[variable-de-control]] es el instrumento analítico para detectarla. La [[endogeneidad]] en econometría designa un fenómeno más amplio, que incluye la confusión por variables omitidas, y la [[omision-de-variables]] es precisamente el problema que genera el sesgo espúreo en modelos de [[regresion]]. La [[operacionalizacion]] determina la calidad de los indicadores cuyas asociaciones se evalúan: indicadores deficientes pueden producir correlaciones espúreas artefactuales.

Es fundamental distinguir confundentes de mediadores y moderadores. Confundir estos roles produce errores inferenciales graves: controlar un mediador elimina una relación causal genuina, mientras que omitir un confundente la preserva artificialmente.

## Debates y críticas

**Karl Popper** sostuvo que la ciencia no puede verificar relaciones causales sino solo corroborarlas provisionalmente, resistiendo intentos de refutación. La detección de espuriedad forma parte de este proceso de corroboración: cada variable confundente descartada fortalece, sin probar definitivamente, la inferencia causal. El problema, señaló Popper, es que resulta imposible controlar *todas* las posibles variables confundentes, lo que mantiene toda afirmación causal en estatus provisional.

**John Goldthorpe** (*Causation, Statistics and Sociology*, 2001) advirtió que la sociología cuantitativa ha tendido a confiar excesivamente en los controles estadísticos como sustitutos de la experimentación. Goldthorpe señaló que la inclusión mecánica de variables de control en modelos de regresión no garantiza la eliminación de relaciones espúreas si no se dispone de una teoría sustantiva que justifique la selección de controles, posición convergente con la de Pearl.

**David Freedman** (*Statistical Models and Causal Inference*, 2005) radicalizó esta crítica al argumentar que los modelos de regresión estándar no pueden, por sí solos, distinguir asociaciones causales de espúreas: la especificación del modelo depende de supuestos no verificables estadísticamente. Sin una teoría causal sustantiva que oriente la especificación, los controles estadísticos pueden tanto eliminar relaciones espúreas como generar nuevas mediante el sesgo de colisionador, es decir, controlar una variable que es efecto común de X e Y y abrir una asociación espúrea inexistente antes del control.

## Vigencia contemporánea

El problema de la espuriedad ha cobrado renovada relevancia en la era del *big data* y el aprendizaje automático. La disponibilidad de enormes conjuntos de datos incrementa la probabilidad de encontrar correlaciones estadísticamente significativas pero causalmente vacías. La ciencia de datos contemporánea recurre cada vez más a los marcos de inferencia causal de Pearl y Rubin para disciplinar el análisis descriptivo y evitar la proliferación de hallazgos espúreos, especialmente en ámbitos como la epidemiología social, la criminología cuantitativa y la evaluación de políticas públicas.

En sociología, los diseños cuasi-experimentales, como diferencias en diferencias, regresión discontinua o variables instrumentales, se han convertido en estándar de referencia precisamente porque ofrecen estrategias de identificación que eliminan o reducen el riesgo de espuriedad sin depender exclusivamente de controles estadísticos.

## Ejemplo empírico

El caso paradigmático es la asociación entre **consumo de helado y muertes por ahogamiento**: ambas variables correlacionan positivamente, pero la relación es espúrea porque un confundente, la temperatura ambiente, causa simultáneamente el aumento del consumo de helado y la mayor frecuencia de actividades acuáticas. Al controlar la temperatura, la asociación helado-ahogamiento desaparece.

En sociología, un ejemplo clásico procede de los estudios sobre religión y suicidio inspirados en Durkheim: la correlación bruta entre protestantismo y tasas de suicidio podía deberse a diferencias en los niveles de urbanización e industrialización entre regiones protestantes y católicas. Solo al introducir estas variables de control pudo evaluarse si la integración religiosa ejercía un efecto causal autónomo, tal como postulaba la teoría durkheimiana.

## Véase también

- [[correlacion]]
- [[causalidad]]
- [[variable-de-control]]
- [[endogeneidad]]
- [[regresion]]
- [[omision-de-variables]]
- [[operacionalizacion]]
- [[hipotesis]]
- [[experimento]]

## Fuentes

- [[el-proceso-de-investigacion-en-las-ciencias-sociales]] (Metodología de las ciencias sociales)
- Lazarsfeld, Paul F. y Kendall, Patricia L. (1950). "Problems of survey analysis". En Merton, R. K. y Lazarsfeld, P. F. (eds.), *Continuities in Social Research*. Free Press.
- Lazarsfeld, Paul F. y Rosenberg, Morris (eds.) (1955). *The Language of Social Research*. Free Press.
- Pearl, Judea (2009). *Causality: Models, Reasoning, and Inference*. 2.ª ed. Cambridge University Press.
- Freedman, David A. (2005). *Statistical Models and Causal Inference: A Dialogue with the Social Sciences*. Cambridge University Press.
- Goldthorpe, John H. (2001). "Causation, Statistics and Sociology". *European Sociological Review*, 17(1), 1-20.
- Popper, Karl (1959). *The Logic of Scientific Discovery*. Hutchinson.
- Yule, G. Udny (1926). "Why do we sometimes get nonsense-correlations between time-series?". *Journal of the Royal Statistical Society*, 89(1), 1-63.
- Vigen, Tyler (2015). *Spurious Correlations*. Hachette Books.
