---
id: mediana
title: Mediana
note_type: concept
semester: 2026-S1
course: "Metodologia de las ciencias sociales"
related_concepts:
  - media-aritmetica
  - moda
  - estadistica-descriptiva
  - desviacion-estandar
  - niveles-de-medicion
  - varianza
  - distribucion-de-frecuencias
tags:
  - estadística
  - tendencia-central
  - medidas-de-posición
  - metodología
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\modulo-3.md
updated_at: '2025-07-13'
---

## Definición

La **mediana** es la medida de tendencia central que corresponde al valor que ocupa la posición intermedia en un conjunto de datos ordenados de menor a mayor. Divide la distribución en dos mitades iguales: el 50 % de las observaciones se sitúa por debajo de ella y el 50 % restante por encima. Formalmente, dada una muestra de $n$ observaciones ordenadas $x_1 \le x_2 \le \dots \le x_n$, la mediana se define como:

$$
Me =
\begin{cases}
x_{(n+1)/2} & \text{si } n \text{ es impar} \\[6pt]
\dfrac{x_{n/2} + x_{(n/2)+1}}{2} & \text{si } n \text{ es par}
\end{cases}
$$

La mediana constituye, junto con la [[media-aritmetica]] y la [[moda]], el trío clásico de medidas de tendencia central de la [[estadistica-descriptiva]]. Su propiedad distintiva es la **robustez**: no se ve afectada por valores extremos (*outliers*), lo que la convierte en un indicador preferido cuando las distribuciones son asimétricas o contienen observaciones atípicas.

## Origen y contexto histórico

El concepto de valor central en una serie ordenada tiene raíces en la aritmética renacentista, pero su formalización estadística se produjo en el siglo XIX. Edward Wright (1599) utilizó procedimientos análogos a la mediana para promediar observaciones náuticas, y Gustav Fechner promovió su uso en psicofísica hacia 1878. Sin embargo, fue Francis Galton quien, en el marco de sus estudios sobre herencia y variación biológica, popularizó la mediana como estadístico descriptivo y la vinculó al sistema de cuartiles y percentiles que hoy resulta habitual en las ciencias sociales. A lo largo del siglo XX, la estadística robusta —desarrollada por John Tukey, Peter Huber y otros— revalorizó la mediana frente a la media al demostrar su menor sensibilidad ante distribuciones de colas pesadas, frecuentes en datos socioeconómicos.

## Desarrollo teórico

Desde la perspectiva de la teoría de la probabilidad, la mediana de una variable aleatoria $X$ es cualquier valor $m$ tal que $P(X \le m) \ge 0{,}5$ y $P(X \ge m) \ge 0{,}5$. A diferencia de la media, que minimiza la suma de desviaciones cuadráticas, la mediana minimiza la suma de desviaciones absolutas: $\sum |x_i - c|$ se hace mínima cuando $c = Me$.

La mediana es, a su vez, un caso particular de los **cuantiles**: coincide con el segundo cuartil ($Q_2$), el quinto decil y el percentil 50. Este anclaje dentro del sistema de cuantiles permite su uso como punto de referencia para construir el **rango intercuartílico** ($RIQ = Q_3 - Q_1$), medida de dispersión robusta que acompaña a la mediana del mismo modo en que la [[desviacion-estandar]] acompaña a la [[media-aritmetica]].

En lo que respecta a la eficiencia estadística, la mediana muestral alcanza aproximadamente el 64 % de la eficiencia de la media muestral bajo distribuciones normales; sin embargo, su ventaja crece de forma decisiva cuando los datos contienen contaminación o provienen de distribuciones de colas pesadas, situación habitual en variables como el ingreso, el patrimonio o el tiempo de permanencia en un estado social.

## Relación con otros conceptos

La mediana se inserta en una red conceptual amplia dentro de la metodología cuantitativa:

- **[[media-aritmetica]]**: promedio sensible a valores extremos; coincide con la mediana solo en distribuciones simétricas.
- **[[moda]]**: valor más frecuente; aplicable incluso a datos nominales, mientras que la mediana requiere al menos un [[niveles-de-medicion|nivel ordinal]].
- **[[varianza]] y [[desviacion-estandar]]**: medidas de dispersión asociadas a la media; la mediana se acompaña del rango intercuartílico o de la desviación absoluta mediana.
- **[[niveles-de-medicion]]**: la mediana es calculable a partir del nivel ordinal, lo que la hace más versátil que la media (que exige nivel de intervalo o razón).
- **[[estadistica-descriptiva]]**: marco general en el que la mediana cumple la función de resumir la posición central de un conjunto de datos.

La relación entre media, mediana y moda resulta diagnóstica de la forma de una distribución: cuando la media supera a la mediana, se sospecha asimetría positiva (cola derecha); cuando la media es inferior, asimetría negativa.

## Debates y críticas

Un primer debate atañe a la **pérdida de información**: al basarse en la posición ordinal y no en la magnitud de todos los valores, la mediana descarta información que la media sí aprovecha. En muestras grandes con distribución normal, la media es un estimador más eficiente del parámetro de localización.

Un segundo punto de discusión concierne la **no unicidad**: en distribuciones discretas con un número par de observaciones la mediana se define convencionalmente como la media de los dos valores centrales, pero en rigor cualquier valor del intervalo que los separa cumple la definición formal, lo que exige una convención explícita.

En las ciencias sociales, el debate se traslada a la **elección entre media y mediana** al comunicar resultados. La mediana del ingreso, por ejemplo, se considera un indicador más fiable de la situación económica «típica» de una población que la media, pues esta última se infla por la presencia de ingresos muy elevados. No obstante, algunos economistas argumentan que la media refleja mejor el volumen total de recursos disponibles y resulta necesaria para cálculos fiscales y de producto interior bruto.

## Vigencia contemporánea

En la investigación social actual, la mediana goza de una presencia creciente. Organismos internacionales como la OCDE, Eurostat y el Banco Mundial publican el **ingreso mediano** como indicador principal de bienestar y desigualdad, complementándolo con ratios como la relación entre el percentil 90 y el percentil 10. En la sociología de la estratificación, la mediana del ingreso equivalente permite comparaciones entre hogares de distinto tamaño. En el análisis de encuestas con escalas Likert —variables de nivel ordinal— la mediana constituye la medida de tendencia central apropiada, frente al uso (frecuente pero discutible) de la media.

El auge de la estadística robusta y del análisis exploratorio de datos (EDA) ha reforzado la relevancia de la mediana como paso previo al modelado inferencial, especialmente en contextos de datos abiertos y *big data* donde la presencia de valores atípicos es la norma más que la excepción.

## Ejemplo empírico

Un equipo de investigación social recoge los ingresos mensuales netos (en euros) de diez hogares de un barrio: 900, 1 050, 1 100, 1 200, 1 250, 1 300, 1 400, 1 500, 1 800 y 8 500. La [[media-aritmetica]] es 2 000 €, cifra que sobreestima la situación típica debido al hogar con ingresos de 8 500 €. La mediana, en cambio, se calcula como la media de los dos valores centrales (5.º y 6.º): $Me = (1\,250 + 1\,300)/2 = 1\,275$ €, valor mucho más representativo de la experiencia cotidiana de la mayoría. La diferencia entre media y mediana (725 €) señala una marcada asimetría positiva y advierte sobre la concentración de ingresos en la parte alta de la distribución, información valiosa para el análisis de la desigualdad social.

## Véase también

- [[media-aritmetica]]
- [[moda]]
- [[estadistica-descriptiva]]
- [[desviacion-estandar]]
- [[varianza]]
- [[niveles-de-medicion]]
- [[distribucion-de-frecuencias]]

## Fuentes

- Módulo 3, *Metodología de las ciencias sociales*, UOC, 2026-S1.
- Moore, David S. (1995). *Estadística aplicada básica*. Barcelona: Antonio Bosch.
- DeGroot, Morris H. (1988). *Probabilidad y estadística* (2.ª ed.). Addison-Wesley Iberoamericana.
- Tukey, John W. (1977). *Exploratory Data Analysis*. Addison-Wesley.
- «Mediana (estadística)». *Wikipedia en español*. Consultado el 5 de abril de 2026.
