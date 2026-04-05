---
id: niveles-de-medicion
title: Niveles de medición
note_type: concept
semester: 2026-S1
course: "Metodologia de las ciencias sociales"
related_concepts:
  - operacionalizacion
  - indicador
  - variable-dependiente
  - estadistica-descriptiva
  - definicion-operacional
  - validez
  - fiabilidad
tags:
  - metodología
  - medición
  - escalas
  - Stevens
  - operacionalización
source_notes:
  - wiki\sources\2026-s1\metodologia-de-las-ciencias-sociales\el-proceso-de-investigacion-en-las-ciencias-sociales.md
updated_at: '2025-07-13'
---

## Definición

Los **niveles de medición** (también denominados *escalas de medida*) constituyen una clasificación jerárquica de las formas en que se asignan valores numéricos o categóricos a las observaciones empíricas. Según la formulación clásica de Stanley Smith Stevens (1946), medir consiste en «la asignación de numerales a objetos o sucesos siguiendo ciertas reglas». A partir de esa definición, Stevens distinguió cuatro escalas —nominal, ordinal, de intervalo y de razón— que determinan qué operaciones matemáticas y qué pruebas estadísticas resultan legítimas para cada variable. La elección del nivel de medición es, por tanto, una decisión metodológica central en el proceso de [[operacionalizacion]] de los conceptos teóricos.

## Origen y contexto histórico

La tipología fue presentada por Stevens en su artículo seminal «On the Theory of Scales of Measurement», publicado en *Science* en 1946. El contexto intelectual era el del positivismo lógico y la aspiración de las ciencias sociales a replicar la exactitud de las ciencias naturales. Stevens, psicofísico de la Universidad de Harvard, buscaba fundamentar la medición psicológica sobre bases formales que permitieran distinguir rigurosamente lo que podía y lo que no podía cuantificarse. Su esquema fue adoptado rápidamente por la sociología empírica, la ciencia política cuantitativa y la psicología social, y sigue siendo un contenido obligado en los manuales de metodología.

## Desarrollo teórico

### Escala nominal

Las variables nominales clasifican a las unidades de análisis en categorías mutuamente excluyentes y exhaustivas, sin establecer orden alguno entre ellas. Los valores funcionan como etiquetas: género (masculino/femenino), confesión religiosa (católica, protestante, judía, musulmana) o nacionalidad. La única operación lógica permitida es la de igualdad o diferencia; la medida de tendencia central apropiada es la moda. Como señalan los materiales del curso, «los valores asignados a cada grupo son solo etiquetas que sirven para diferenciarlos; las operaciones aritméticas no tienen sentido».

### Escala ordinal

Las variables ordinales incorporan, además de la clasificación, una relación de orden: las categorías pueden disponerse de mayor a menor presencia de un atributo, pero la distancia entre ellas no es cuantificable. Es el caso de la clase social (baja, media, alta) o las escalas actitudinales tipo Likert donde un encuestado declara estar «muy de acuerdo», «de acuerdo», «en desacuerdo» o «muy en desacuerdo». Se puede calcular la mediana, pero no la media aritmética. La medida de dispersión habitual es el rango intercuartílico.

### Escala de intervalo

En esta escala las distancias entre valores son iguales y cuantificables, pero el punto cero es arbitrario. El ejemplo canónico es la temperatura en grados Celsius: 0 °C no significa ausencia de temperatura. Se pueden sumar y restar diferencias, pero no dividir ni multiplicar con sentido sustantivo. Muchos índices compuestos de ciencias sociales —por ejemplo, índices de actitud construidos a partir de múltiples [[indicador]]es— operan en este nivel.

### Escala de razón

Posee todas las propiedades de la escala de intervalo más un cero absoluto que indica ausencia real del atributo. Ejemplos clásicos son el ingreso monetario, la edad, el número de hijos o la temperatura en Kelvin. Todas las operaciones aritméticas son válidas, incluidas proporciones y razones. La media geométrica y los coeficientes de variación son estadísticos apropiados.

### Operaciones estadísticas permitidas

| Escala   | Clasificar | Ordenar | Sumar/restar | Multiplicar/dividir | Tendencia central |
|----------|:---:|:---:|:---:|:---:|-------------------|
| Nominal  | ✓ |   |   |   | Moda              |
| Ordinal  | ✓ | ✓ |   |   | Mediana           |
| Intervalo| ✓ | ✓ | ✓ |   | Media aritmética  |
| Razón    | ✓ | ✓ | ✓ | ✓ | Media geométrica  |

## Relación con otros conceptos

La determinación del nivel de medición es un paso inseparable de la [[operacionalizacion]]: al traducir un concepto abstracto en un [[indicador]] observable, el investigador decide simultáneamente la escala en que lo registrará. Esa decisión condiciona las técnicas de [[estadistica-descriptiva]] aplicables y los modelos de [[estadistica-inferencial]] disponibles. La [[definicion-operacional]] de una [[variable-dependiente]] debe explicitar su nivel de medición para garantizar la [[validez]] y la [[fiabilidad]] del instrumento.

La codificación de las variables, como advierte el módulo 3 de los materiales del curso, «tiene que ir de acuerdo con los niveles de medición de las variables (nominal, ordinal, numérico)».

## Debates y críticas

### El problema de las escalas Likert

Uno de los debates metodológicos más persistentes es si las escalas Likert deben tratarse como ordinales o como de intervalo. Quienes defienden el tratamiento intervalar argumentan que, con suficientes puntos de anclaje (cinco o más), los datos se aproximan a una distribución continua y los análisis paramétricos resultan robustos. Los puristas metodológicos insisten en que la distancia psicológica entre «de acuerdo» y «muy de acuerdo» no es necesariamente igual a la distancia entre «en desacuerdo» y «muy en desacuerdo», por lo que solo caben técnicas no paramétricas.

### Crítica constructivista

Desde una perspectiva interpretativista, la pretensión de cuantificar fenómenos sociales complejos —identidad, poder, sentido— mediante escalas numéricas impone una lógica positivista que puede deformar la realidad que intenta captar. El acto de medir no es neutral: la elección de categorías y escalas refleja supuestos teóricos previos y relaciones de poder en la producción de conocimiento.

### Hayek y los límites de la medición social

Friedrich Hayek, en su discurso del Nobel (1974), advirtió sobre la «pretensión del conocimiento»: la imitación irreflexiva de los métodos de las ciencias naturales conduce a medir lo fácilmente cuantificable e ignorar lo que no se deja reducir a números, produciendo una «ciencia falsa» que confunde precisión formal con comprensión real.

### Los conjuntos difusos de Ragin

Charles Ragin propuso los *fuzzy sets* como alternativa a las escalas convencionales. En lugar de clasificar un caso como perteneciente o no a una categoría (lógica binaria nominal), los conjuntos difusos permiten grados de pertenencia entre 0 y 1, integrando así la información cualitativa y cuantitativa para el análisis comparativo de configuraciones causales (*QCA*). Esta propuesta desafía la rigidez de la tipología de Stevens al ofrecer una solución intermedia entre lo nominal y lo intervalar.

## Vigencia contemporánea

La tipología de Stevens sigue siendo el marco de referencia estándar en los cursos de metodología y en los manuales de estadística social. Sin embargo, los avances en modelización —regresión logística ordinal, modelos de ecuaciones estructurales, técnicas bayesianas— han flexibilizado los límites entre niveles: hoy es habitual tratar variables ordinales con técnicas diseñadas para datos continuos bajo ciertas condiciones de robustez. La aparición de grandes volúmenes de datos no estructurados (textos, imágenes, redes) ha ampliado el repertorio de lo medible más allá de las cuatro escalas clásicas, aunque estas siguen organizando el arsenal estadístico básico de las ciencias sociales.

## Ejemplo empírico

En una encuesta sobre desigualdad urbana en Buenos Aires se operacionalizan distintas variables a diferentes niveles:

- **Barrio de residencia** → nominal (Palermo, La Boca, Flores…).
- **Percepción de seguridad** → ordinal (muy inseguro, inseguro, seguro, muy seguro), usando una escala Likert de cuatro puntos.
- **Índice de satisfacción con servicios públicos** → intervalo, construido como promedio de cinco ítems Likert.
- **Ingreso mensual del hogar** → razón (en pesos argentinos, con cero significando ausencia de ingresos).

La elección de cada nivel determina que para el barrio solo se pueda calcular la moda, para la percepción de seguridad la mediana, y para el ingreso la media y la desviación estándar. Un error común sería calcular la media de la variable barrio o interpretar que un hogar con ingreso de $200 000 tiene «el doble» de satisfacción que uno de $100 000.

## Véase también

- [[operacionalizacion]]
- [[indicador]]
- [[variable-dependiente]]
- [[estadistica-descriptiva]]
- [[definicion-operacional]]
- [[validez]]
- [[fiabilidad]]
- [[marco-teorico]]

## Fuentes

- Stevens, S. S. (1946). «On the Theory of Scales of Measurement». *Science*, 103(2684), 677-680.
- Hayek, F. A. (1974). «The Pretence of Knowledge». Discurso del Premio Nobel.
- Ragin, C. C. (2000). *Fuzzy-Set Social Science*. Chicago: University of Chicago Press.
- Salkind, N. J. (1998). *Métodos de investigación* (3.ª ed.). México: Prentice Hall.
- Materiales del curso: Módulo 1, «El proceso de investigación en las ciencias sociales»; Módulo 3, codificación de variables.
- [[el-proceso-de-investigacion-en-las-ciencias-sociales-marco-teorico-y-diseno-empirico]]
