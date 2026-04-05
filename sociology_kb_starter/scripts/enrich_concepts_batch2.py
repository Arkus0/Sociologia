"""
Batch enrichment script 2 – Sociology classics + Durkheim + Marx + Weber concepts
"""
import os, yaml

CONCEPTS_DIR = "data/wiki/concepts"
CONCEPTS = {}

def c(slug, title, semester, course, related, tags, body):
    CONCEPTS[slug] = {"title": title, "semester": semester, "course": course,
                      "related_concepts": related, "tags": tags, "body": body}

# ═══ DURKHEIM CONCEPTS ═══

c("hecho-social",
  "Hecho social", "2026-S1", "Introduccion a la sociologia",
  ["conciencia-colectiva","solidaridad-mecanica","solidaridad-organica","anomia","sociologia-como-ciencia","positivismo"],
  ["Introduccion a la sociologia","sociologia-clasica","durkheimiana"],
  """## Definición
Un hecho social es, según [[emile-durkheim]], toda manera de hacer, pensar y sentir que es externa al individuo y ejerce sobre él una coacción. Los hechos sociales se reconocen por tres características: (1) son **exteriores** al individuo — existen antes de que él nazca; (2) son **coercitivos** — se imponen con fuerza, aunque a menudo no lo percibamos; y (3) son **generales** — se distribuyen en el conjunto de la sociedad. El lenguaje, las leyes, las costumbres y las corrientes de opinión son hechos sociales.

## Origen y contexto histórico
Durkheim definió el concepto en *Las reglas del método sociológico* (1895) para fundamentar la sociología como ciencia autónoma. Frente a la psicología (que estudia hechos individuales) y la filosofía (que especula), la sociología tiene su propio objeto: los hechos sociales. La famosa regla metodológica de Durkheim es: "hay que tratar los hechos sociales como cosas" — no porque *sean* cosas, sino porque deben estudiarse con la misma objetividad que los fenómenos naturales.

## Desarrollo teórico
### Coacción y exterioridad
La coacción del hecho social se manifiesta de múltiples formas: la presión de la opinión pública, la sanción legal, el ridículo social, la vergüenza. Durkheim argumenta que incluso cuando creemos actuar libremente, los hechos sociales nos condicionan: elegimos "libremente" casarnos, pero la institución del matrimonio, con todas sus normas, existía antes que nosotros.

### Hechos sociales materiales e inmateriales
- **Materiales**: instituciones, leyes, arquitectura social
- **Inmateriales**: la [[conciencia-colectiva]], las corrientes de opinión, las representaciones colectivas

### Método sociológico
Para estudiar hechos sociales hay que: (1) descartar las prenociones (sentido común), (2) definir el fenómeno por características externas observables, (3) buscar las causas en otros hechos sociales (no en hechos individuales).

## Relación con otros conceptos
- La [[conciencia-colectiva]] es un hecho social inmaterial: el conjunto de creencias y sentimientos comunes a los miembros de una sociedad
- La [[sociologia-como-ciencia]] se funda en la existencia de hechos sociales como objeto propio
- La [[anomia]] es una patología del hecho social: la ausencia de regulación normativa
- El [[positivismo]] de Comte inspira a Durkheim, pero este lo supera al definir un objeto específico

## Debates y críticas
Weber objetó que los hechos sociales no existen "fuera" del individuo: la sociología debe comprender el **sentido subjetivo** que los actores dan a sus acciones ([[accion-social]]). La sociología interpretativa (Weber, interaccionismo) critica el objetivismo durkheimiano. Sin embargo, la intuición de Durkheim — que hay realidades sociales irreductibles a la suma de acciones individuales — sigue siendo fundacional.

## Vigencia contemporánea
Las redes sociales demuestran la coerción de los hechos sociales: un individuo puede intentar ignorar una tendencia viral, pero la presión del entorno digital (likes, retweets, algoritmos) ejerce una coacción real sobre su conducta y opiniones.

## Ejemplo empírico
El suicidio como hecho social: Durkheim demostró que las tasas de suicidio son regulares y predecibles según variables sociales (religión, estado civil, integración social), lo que prueba que el suicidio — aparentemente el acto más individual — es un hecho social.

## Véase también
- [[conciencia-colectiva]]
- [[solidaridad-mecanica]]
- [[solidaridad-organica]]
- [[anomia]]
- [[sociologia-como-ciencia]]

## Fuentes
- [[el-pensamiento-sociologico-i-los-fundadores]] (Introduccion a la sociologia)
- [[diferenciacion-social-y-division-del-trabajo]] (Introduccion a la sociologia)
- Durkheim, Émile (1895). *Las reglas del método sociológico*.""")


c("conciencia-colectiva",
  "Conciencia colectiva", "2026-S1", "Introduccion a la sociologia",
  ["hecho-social","solidaridad-mecanica","division-del-trabajo","anomia","individualismo"],
  ["Introduccion a la sociologia","sociologia-clasica","durkheimiana"],
  """## Definición
La conciencia colectiva es el conjunto de creencias, sentimientos, valores y representaciones comunes a los miembros de una sociedad, que existe con vida propia independientemente de las conciencias individuales que la componen. No es la suma de las conciencias individuales sino una realidad *sui generis* que ejerce coacción sobre ellas. Es el "cemento moral" que mantiene unida a la sociedad.

## Origen y contexto histórico
[[emile-durkheim]] desarrolló el concepto en *La división del trabajo social* (1893) para explicar el fundamento de la cohesión social. En las sociedades segmentarias (clanes, tribus), la conciencia colectiva es intensa, abarca casi toda la vida individual y deja poco margen a la diferencia personal: es el fundamento de la [[solidaridad-mecanica]].

## Desarrollo teórico
- En sociedades de [[solidaridad-mecanica]]: la conciencia colectiva es fuerte, precisa y envolvente — cubre prácticamente toda la vida del individuo
- En sociedades de [[solidaridad-organica]]: se debilita, se vuelve más abstracta y general, dejando espacio a la diferencia individual y al [[individualismo]]
- La conciencia colectiva no desaparece con la modernidad: cambia de contenido (de religión a derechos humanos, de tradición a ciencia)
- Se manifiesta en: derecho penal (crímenes = ofensas a la conciencia colectiva), rituales colectivos, indignación moral pública

## Relación con otros conceptos
- Es el principal [[hecho-social]] inmaterial en Durkheim
- Funda la [[solidaridad-mecanica]] por semejanza
- Su debilitamiento en la [[modernidad]] genera riesgo de [[anomia]]
- El [[individualismo]] moderno es, paradójicamente, un valor de la nueva conciencia colectiva

## Debates y críticas
El concepto ha sido criticado por su vaguedad: ¿cómo se mide la conciencia colectiva? ¿De toda la sociedad o de grupos específicos? Weber prefirió analizar valores y creencias como orientaciones subjetivas de la acción, no como entidades supraindividuales.

## Vigencia contemporánea
Las redes sociales hacen visible la conciencia colectiva en tiempo real: la indignación viral, los hashtags compartidos y las "cancelaciones" son manifestaciones de una conciencia colectiva digitalizada.

## Ejemplo empírico
Las reacciones colectivas a atentados terroristas (concentraciones espontáneas, lemas compartidos como "Je suis Charlie") muestran la conciencia colectiva en acción: una efervescencia moral que reafirma los valores compartidos.

## Véase también
- [[hecho-social]]
- [[solidaridad-mecanica]]
- [[solidaridad-organica]]
- [[anomia]]
- [[individualismo]]

## Fuentes
- [[el-pensamiento-sociologico-i-los-fundadores]] (Introduccion a la sociologia)
- [[diferenciacion-social-y-division-del-trabajo]] (Introduccion a la sociologia)
- Durkheim, Émile (1893). *La división del trabajo social*.""")


c("solidaridad-mecanica",
  "Solidaridad mecánica", "2026-S1", "Introduccion a la sociologia",
  ["solidaridad-organica","conciencia-colectiva","division-del-trabajo","hecho-social","modernidad"],
  ["Introduccion a la sociologia","sociologia-clasica","durkheimiana"],
  """## Definición
La solidaridad mecánica es el tipo de cohesión social propio de las sociedades simples, segmentarias o premodernas, fundada en la **semejanza** entre sus miembros. En estas sociedades, los individuos comparten las mismas creencias, valores y formas de vida; la [[conciencia-colectiva]] es intensa y envolvente, dejando poco espacio a la diferencia personal. El término "mecánica" alude a la analogía con las moléculas de un cuerpo inorgánico: iguales e intercambiables.

## Origen y contexto histórico
[[emile-durkheim]] formuló el concepto en *La división del trabajo social* (1893) para responder a la pregunta: ¿qué mantiene unida a la sociedad? Frente al individualismo utilitarista (la sociedad como contrato entre individuos egoístas), Durkheim argumentó que la cohesión social tiene fundamentos morales, y que estos varían según el tipo de sociedad.

## Desarrollo teórico
### Características
- Los miembros son similares en creencias, valores y actividades
- El derecho es **represivo**: el delito ofende a la conciencia colectiva y la respuesta es el castigo ejemplar
- Hay poca [[division-del-trabajo]]: todos hacen más o menos lo mismo
- La individualidad está absorbida por el grupo

### Transición histórica
Con el aumento de la densidad material y moral (más población, más interacciones), surge la [[division-del-trabajo]], que fragmenta la conciencia colectiva y genera [[solidaridad-organica]]. La transición no es automática ni pacífica: puede producir [[anomia]].

## Relación con otros conceptos
- Se opone a [[solidaridad-organica]] como los dos polos de la cohesión social
- La [[conciencia-colectiva]] fuerte es su fundamento
- La [[division-del-trabajo]] la disuelve al diferenciarse las funciones
- El concepto gemelo en Tönnies es *Gemeinschaft* (comunidad) vs. *Gesellschaft* (sociedad)

## Debates y críticas
La dicotomía mecánica/orgánica simplifica sociedades reales que combinan ambos tipos. Las sociedades modernas conservan elementos de solidaridad mecánica (nacionalismo, rituales deportivos, "nosotros" frente a "ellos"). La comunidad no desaparece con la modernidad; se transforma.

## Ejemplo empírico
Las comunidades religiosas cerradas (amish, haredi) ilustran la solidaridad mecánica contemporánea: creencias compartidas, baja diferenciación interna, control social intenso y castigo de la desviación (excomunión).

## Véase también
- [[solidaridad-organica]]
- [[conciencia-colectiva]]
- [[division-del-trabajo]]
- [[anomia]]

## Fuentes
- [[el-pensamiento-sociologico-i-los-fundadores]] (Introduccion a la sociologia)
- [[diferenciacion-social-y-division-del-trabajo]] (Introduccion a la sociologia)
- Durkheim, Émile (1893). *La división del trabajo social*.""")


c("solidaridad-organica",
  "Solidaridad orgánica", "2026-S1", "Introduccion a la sociologia",
  ["solidaridad-mecanica","division-del-trabajo","conciencia-colectiva","anomia","individualismo","modernidad"],
  ["Introduccion a la sociologia","sociologia-clasica","durkheimiana"],
  """## Definición
La solidaridad orgánica es el tipo de cohesión social propio de las sociedades modernas, complejas y diferenciadas, fundada en la **interdependencia funcional** entre individuos y grupos especializados. En estas sociedades, la [[division-del-trabajo]] hace que cada persona realice una función distinta, lo que genera una dependencia mutua análoga a la de los órganos de un cuerpo vivo — de ahí "orgánica".

## Origen y contexto histórico
[[emile-durkheim]] la formuló en *La división del trabajo social* (1893) como respuesta a la paradoja moderna: ¿cómo puede mantenerse unida una sociedad donde los individuos son cada vez más diferentes? Su respuesta: la diferenciación misma genera un nuevo tipo de solidaridad, basada no en la semejanza sino en la complementariedad.

## Desarrollo teórico
### Características
- Los miembros son diferentes, especializados y funcionalmente interdependientes
- El derecho es **restitutivo** (civil, comercial, laboral): busca restaurar el equilibrio, no castigar
- La [[conciencia-colectiva]] se debilita y se vuelve más abstracta: valores generales como la dignidad humana y la libertad individual
- El [[individualismo]] emerge como valor central — paradójicamente, es el individualismo lo que la sociedad moderna comparte

### Condiciones de éxito
Para que la solidaridad orgánica funcione sin [[anomia]], se requiere:
- Regulación moral de las relaciones entre funciones (corporaciones profesionales)
- Justicia en la distribución de funciones (contra la "división del trabajo forzada")
- Densidad moral suficiente (contacto e interacción entre grupos)

## Relación con otros conceptos
- Se opone a [[solidaridad-mecanica]] (cohesión por semejanza)
- Depende de la [[division-del-trabajo]] como mecanismo generador
- La [[anomia]] es su patología: cuando la interdependencia existe sin regulación moral
- El [[individualismo]] moral (respeto sagrado por la persona) es su expresión normativa

## Debates y críticas
Marx argumentaría que la interdependencia funcional enmascara la explotación: la [[division-del-trabajo]] capitalista no genera complementariedad sino [[alienacion]]. Durkheim respondería que el problema no es la división del trabajo en sí, sino su forma anómica o forzada.

## Ejemplo empírico
La pandemia de COVID-19 reveló la solidaridad orgánica: la interdependencia entre sanitarios, transportistas, agricultores, científicos y gobiernos se hizo visible. Al mismo tiempo, la ruptura de las cadenas de suministro mostró los riesgos de una interdependencia sin regulación adecuada.

## Véase también
- [[solidaridad-mecanica]]
- [[division-del-trabajo]]
- [[conciencia-colectiva]]
- [[anomia]]
- [[individualismo]]

## Fuentes
- [[el-pensamiento-sociologico-i-los-fundadores]] (Introduccion a la sociologia)
- [[diferenciacion-social-y-division-del-trabajo]] (Introduccion a la sociologia)
- Durkheim, Émile (1893). *La división del trabajo social*.""")


c("division-del-trabajo",
  "División del trabajo", "2026-S1", "Introduccion a la sociologia",
  ["solidaridad-organica","solidaridad-mecanica","anomia","alienacion","clase-social","modernidad","diferenciacion-social"],
  ["Introduccion a la sociologia","sociologia-clasica"],
  """## Definición
La división del trabajo es el proceso de especialización funcional por el cual las tareas productivas y reproductivas se distribuyen entre individuos, grupos o instituciones. En sociología tiene un doble significado: para [[emile-durkheim]] es el fundamento de la [[solidaridad-organica]] y la cohesión moderna; para [[karl-marx]] es el mecanismo que genera [[alienacion]], explotación y [[lucha-de-clases]]. Adam Smith la analizó como fuente de eficiencia económica.

## Origen y contexto histórico
Smith (*La riqueza de las naciones*, 1776) mostró que la división del trabajo multiplica la productividad (ejemplo de la fábrica de alfileres). Durkheim (1893) la transformó en concepto sociológico: no es solo un fenómeno económico sino el principio organizador de las sociedades modernas. Marx (*El Capital*, 1867) reveló su cara oscura: la división entre trabajo manual e intelectual y entre propietarios y trabajadores.

## Desarrollo teórico
### División del trabajo en Durkheim
- Causa: aumento de la densidad material (población) y moral (interacciones)
- Efecto positivo: genera [[solidaridad-organica]] por interdependencia funcional
- Formas patológicas: la división anómica (sin regulación) y la división forzada (contra las aptitudes naturales)
- No es solo económica: también se dividen funciones jurídicas, administrativas, científicas, artísticas

### División del trabajo en Marx
- La división técnica del trabajo (dentro de la fábrica) degrada al trabajador convirtiéndolo en apéndice de la máquina
- La división social del trabajo (entre sectores) genera clases con intereses antagónicos
- La división sexual del trabajo asigna a la mujer el trabajo reproductivo no remunerado

## Relación con otros conceptos
- Para Durkheim: genera [[solidaridad-organica]]; su patología es la [[anomia]]
- Para Marx: genera [[alienacion]] y [[lucha-de-clases]]
- La [[diferenciacion-social]] (Spencer, Simmel) es un concepto más amplio que incluye la división del trabajo como caso particular
- La [[burocracia]] weberiana es una forma de división del trabajo racionalizada
- La división sexual del trabajo fundamenta la crítica del [[patriarcado]]

## Debates y críticas
Durkheim idealizó la división del trabajo al separarla de las relaciones de poder; Marx la redujo al conflicto de clases ignorando sus funciones integradoras. La síntesis contemporánea reconoce ambas dimensiones: la especialización genera interdependencia *y* desigualdad.

## Ejemplo empírico
Las cadenas globales de valor: un iPhone implica diseño en California, extracción de minerales en Congo, ensamblaje en China y venta global — división del trabajo planetaria que genera interdependencia y desigualdad simultáneamente.

## Véase también
- [[solidaridad-organica]]
- [[solidaridad-mecanica]]
- [[anomia]]
- [[alienacion]]
- [[clase-social]]
- [[diferenciacion-social]]

## Fuentes
- [[diferenciacion-social-y-division-del-trabajo]] (Introduccion a la sociologia)
- [[el-pensamiento-sociologico-i-los-fundadores]] (Introduccion a la sociologia)
- Durkheim, Émile (1893). *La división del trabajo social*.
- Marx, Karl (1867). *El Capital*, vol. I.""")


c("clase-social",
  "Clase social", "2026-S1", "Introduccion a la sociologia",
  ["lucha-de-clases","estratificacion-social","modo-de-produccion","movilidad-social","division-del-trabajo","desigualdad-social","infraestructura-y-superestructura"],
  ["Introduccion a la sociologia","sociologia-clasica","desigualdad"],
  """## Definición
Una clase social es un grupo de personas que comparten una posición similar en la estructura económica de la sociedad, lo que les confiere intereses, condiciones de vida y oportunidades similares. Para [[karl-marx]], las clases se definen por la relación con los **medios de producción** (propietarios vs. desposeídos); para [[max-weber]], la clase es una de las tres dimensiones de la [[estratificacion-social]], junto con el estatus y el partido, y se define por la **situación de mercado** (capacidades, cualificaciones y bienes que se poseen).

## Origen y contexto histórico
Marx y Engels escribieron en el *Manifiesto comunista* (1848): "la historia de todas las sociedades que han existido hasta nuestro días es la historia de la [[lucha-de-clases]]". En cada [[modo-de-produccion]] existe una clase dominante (amos, señores feudales, burgueses) y una clase dominada (esclavos, siervos, proletarios). Weber (1922) complejizó el modelo al distinguir clase económica, estamento social y partido político.

## Desarrollo teórico
### Clase en Marx
- La clase se define por la relación con los medios de producción
- Burguesía y proletariado son las dos clases fundamentales del capitalismo
- La "clase en sí" (posición objetiva) debe convertirse en "clase para sí" (conciencia de clase) para actuar políticamente
- La [[infraestructura-y-superestructura|infraestructura]] económica determina la [[infraestructura-y-superestructura|superestructura]] ideológica

### Clase en Weber
- La clase se define por la situación de mercado: qué bienes y cualificaciones se poseen
- Hay cuatro clases: propietarios, intelectuales-administrativos, pequeña burguesía y clase obrera
- La clase no determina directamente la acción: entre la posición y la acción intervienen el estatus y la organización política
- Goldthorpe desarrolló una clasificación neoweberiana de 11 clases basada en las relaciones de empleo

## Relación con otros conceptos
- La [[estratificacion-social]] es el sistema general de desigualdad; la clase es uno de sus ejes
- La [[movilidad-social]] mide los movimientos entre clases (inter e intrageneracional)
- La [[division-del-trabajo]] estructura las posiciones de clase
- El [[genero]], la etnia y la edad intersectan con la clase (interseccionalidad)

## Debates y críticas
La teoría de clases ha sido cuestionada por la "desaparición" de la clase obrera industrial en Occidente. Bourdieu reformuló las clases como posiciones en un espacio multidimensional (capital económico, cultural, social y simbólico). Los estudios empíricos muestran que la clase social sigue siendo el mejor predictor de resultados educativos, salud y esperanza de vida.

## Vigencia contemporánea
La "clase creativa" (Florida), el "precariado" (Standing) y los "trabajadores de plataformas" son categorías que intentan actualizar el análisis de clases para el siglo XXI. La desigualdad económica creciente (Piketty, *El capital en el siglo XXI*) ha revitalizado el análisis de clases.

## Ejemplo empírico
Los estudios PISA muestran sistemáticamente que el nivel socioeconómico familiar (proxy de clase social) es el factor que más influye en el rendimiento educativo, por encima del esfuerzo individual, el tipo de escuela o la nacionalidad.

## Véase también
- [[lucha-de-clases]]
- [[estratificacion-social]]
- [[modo-de-produccion]]
- [[movilidad-social]]
- [[division-del-trabajo]]

## Fuentes
- [[el-pensamiento-sociologico-i-los-fundadores]] (Introduccion a la sociologia)
- [[diferenciacion-social-y-division-del-trabajo]] (Introduccion a la sociologia)
- [[la-sociedad-ii-el-proceso-de-institucionalizacion]] (Introduccion a la sociologia)
- Marx, Karl; Engels, Friedrich (1848). *Manifiesto comunista*.
- Weber, Max (1922). *Economía y sociedad*.""")


c("lucha-de-clases",
  "Lucha de clases", "2026-S1", "Introduccion a la sociologia",
  ["clase-social","modo-de-produccion","alienacion","materialismo-historico","infraestructura-y-superestructura"],
  ["Introduccion a la sociologia","sociologia-clasica","marxismo"],
  """## Definición
La lucha de clases es, en la teoría de [[karl-marx]], el motor de la historia: el conflicto permanente entre las clases sociales que ocupan posiciones antagónicas en la estructura económica — los propietarios de los medios de producción y los que solo poseen su fuerza de trabajo. No es una guerra puntual, sino una tensión estructural que atraviesa todas las instituciones sociales: el Estado, el derecho, la cultura, la educación y la familia.

## Origen y contexto histórico
Marx y Engels abrieron el *Manifiesto comunista* (1848) con la célebre frase: "La historia de todas las sociedades que han existido hasta nuestros días es la historia de la lucha de clases. Libres y esclavos, patricios y plebeyos, señores y siervos, maestros artesanos y oficiales, en una palabra: opresores y oprimidos". Cada [[modo-de-produccion]] genera su propia forma de lucha de clases.

## Desarrollo teórico
- La lucha de clases se manifiesta tanto en el plano económico (explotación, huelgas, negociación salarial) como en el ideológico (la clase dominante impone sus ideas como "sentido común")
- La transición entre modos de producción se produce por revolución: cuando las fuerzas productivas entran en contradicción con las relaciones de producción
- La "clase en sí" debe convertirse en "clase para sí" — la conciencia de clase transforma la posición objetiva en acción política
- La [[alienacion]] impide la conciencia de clase: el trabajador alienado no reconoce sus intereses colectivos

## Relación con otros conceptos
- La [[clase-social]] define los actores del conflicto
- El [[modo-de-produccion]] determina la forma de la lucha
- La [[infraestructura-y-superestructura]] explica por qué la lucha no es solo económica
- El [[materialismo-historico]] es la teoría general que enmarca la lucha de clases
- La [[alienacion]] es un obstáculo para la conciencia de clase

## Debates y críticas
Weber argumentó que el conflicto social no se reduce a las clases económicas: el estatus y el poder político generan sus propias líneas de fractura. Dahrendorf (1959) reformuló la lucha de clases como conflicto de autoridad dentro de organizaciones, ampliando el concepto más allá de la propiedad. Las teorías interseccionales muestran que la lucha de clases se cruza con la de género, raza y otros ejes de desigualdad.

## Vigencia contemporánea
Los movimientos sociales contemporáneos (Occupy Wall Street, chalecos amarillos, protestas por la vivienda) reactualizan la lucha de clases en nuevos formatos. La brecha creciente entre el 1% más rico y el resto de la población (Piketty, Oxfam) muestra que la tensión de clases sigue vigente.

## Ejemplo empírico
La Revolución Industrial generó una lucha de clases visible: jornadas de 16 horas, trabajo infantil, ausencia de derechos. Los movimientos obreros conquistaron progresivamente derechos (jornada de 8 horas, sufragio universal, seguridad social) a través de huelgas, sindicatos y partidos de clase.

## Véase también
- [[clase-social]]
- [[modo-de-produccion]]
- [[alienacion]]
- [[materialismo-historico]]
- [[infraestructura-y-superestructura]]

## Fuentes
- [[el-pensamiento-sociologico-i-los-fundadores]] (Introduccion a la sociologia)
- Marx, Karl; Engels, Friedrich (1848). *Manifiesto comunista*.
- Marx, Karl (1867). *El Capital*, vol. I.""")


c("modo-de-produccion",
  "Modo de producción", "2026-S1", "Introduccion a la sociologia",
  ["clase-social","lucha-de-clases","materialismo-historico","infraestructura-y-superestructura","alienacion"],
  ["Introduccion a la sociologia","sociologia-clasica","marxismo"],
  """## Definición
El modo de producción es, en la teoría de [[karl-marx]], la forma específica en que una sociedad organiza la producción de los bienes necesarios para su subsistencia. Comprende dos elementos: (1) las **fuerzas productivas** (tecnología, trabajo humano, recursos naturales) y (2) las **relaciones de producción** (relaciones sociales de propiedad que determinan quién controla los medios de producción y cómo se distribuye el producto). La unidad de ambos define el carácter de una sociedad.

## Origen y contexto histórico
Marx desarrolló el concepto en *La ideología alemana* (1845-46), *El manifiesto comunista* (1848) y *El Capital* (1867). Identificó una sucesión histórica de modos de producción: comunismo primitivo → esclavismo → feudalismo → capitalismo → (proyectado) socialismo/comunismo. Cada transición se produce por la contradicción entre fuerzas productivas en expansión y relaciones de producción que las frenan.

## Desarrollo teórico
- Las fuerzas productivas tienden a crecer (innovación tecnológica, acumulación de saber)
- Las relaciones de producción se cristalizan en formas de propiedad
- Cuando las fuerzas productivas superan las relaciones, se produce una crisis que puede resolverse por revolución
- El modo de producción capitalista se caracteriza por: propiedad privada de los medios, trabajo asalariado, producción de mercancías y acumulación de capital

## Relación con otros conceptos
- La [[infraestructura-y-superestructura]] distingue la base económica (modo de producción) de las formas ideológicas
- La [[clase-social]] se define por la posición en las relaciones de producción
- La [[lucha-de-clases]] es el mecanismo de transición entre modos
- La [[alienacion]] es la condición del trabajador en el modo de producción capitalista

## Debates y críticas
El esquema de sucesión lineal de modos de producción ha sido criticado como eurocéntrico (no se aplica a China, India o América precolombina). El "modo de producción asiático" fue un intento de Marx de incluir sociedades no europeas, pero generó más problemas que soluciones. Los neomarxistas han abandonado el determinismo tecnológico: las transiciones no son automáticas.

## Ejemplo empírico
La transición del feudalismo al capitalismo en Europa: el cercamiento de tierras comunales obligó a los campesinos a migrar a las ciudades y vender su fuerza de trabajo, creando al proletariado industrial y las condiciones del modo de producción capitalista.

## Véase también
- [[clase-social]]
- [[lucha-de-clases]]
- [[materialismo-historico]]
- [[infraestructura-y-superestructura]]
- [[alienacion]]

## Fuentes
- [[el-pensamiento-sociologico-i-los-fundadores]] (Introduccion a la sociologia)
- Marx, Karl (1867). *El Capital*, vol. I.
- Marx, Karl; Engels, Friedrich (1845-46). *La ideología alemana*.""")


c("materialismo-historico",
  "Materialismo histórico", "2026-S1", "Introduccion a la sociologia",
  ["modo-de-produccion","lucha-de-clases","infraestructura-y-superestructura","clase-social","alienacion"],
  ["Introduccion a la sociologia","sociologia-clasica","marxismo"],
  """## Definición
El materialismo histórico es la concepción marxista de la historia según la cual las condiciones materiales de existencia — la forma en que los seres humanos producen y reproducen su vida material — determinan la estructura social, política e ideológica de cada época. No son las ideas las que hacen la historia, sino las relaciones económicas concretas: "no es la conciencia la que determina el ser social, sino el ser social el que determina la conciencia" ([[karl-marx]], *Contribución a la crítica de la economía política*, 1859).

## Origen y contexto histórico
Marx y Engels formularon el materialismo histórico en *La ideología alemana* (1845-46) como inversión del idealismo hegeliano: si para Hegel la historia es el despliegue de las ideas, para Marx las ideas son el reflejo de las condiciones materiales. El materialismo histórico no es un determinismo económico mecánico: las condiciones materiales determinan "en última instancia", pero la superestructura tiene autonomía relativa.

## Desarrollo teórico
- La historia se estructura en [[modo-de-produccion|modos de producción]] sucesivos
- La [[infraestructura-y-superestructura|infraestructura]] (fuerzas productivas + relaciones de producción) condiciona la [[infraestructura-y-superestructura|superestructura]] (Estado, derecho, religión, cultura)
- El motor del cambio histórico es la [[lucha-de-clases]], generada por las contradicciones del modo de producción
- El método es dialéctico: las contradicciones internas generan su propia superación

## Relación con otros conceptos
- El [[modo-de-produccion]] es la unidad básica del análisis materialista
- La [[infraestructura-y-superestructura]] describe la arquitectura de cada formación social
- La [[lucha-de-clases]] es el mecanismo de transformación histórica
- Se opone al idealismo, al [[positivismo]] y al [[racionalismo-critico]]

## Debates y críticas
El materialismo histórico ha sido acusado de **determinismo económico**: ¿todo se reduce a la economía? Engels matizó al final de su vida (carta a Bloch, 1890): "el factor determinante *en última instancia* es la producción, pero los distintos elementos de la superestructura ejercen su influencia sobre el curso de las luchas históricas". Weber mostró que la cultura puede ser un factor autónomo: la [[etica-protestante]] influyó en el desarrollo del capitalismo.

## Vigencia contemporánea
El análisis materialista sigue siendo central para entender la desigualdad global, las cadenas de suministro y la relación entre economía y política. Sin embargo, se complementa con análisis culturales (Bourdieu), interseccionales (género, raza) y ecológicos (límites materiales del capitalismo).

## Ejemplo empírico
La Revolución Francesa (1789): la burguesía, que había acumulado poder económico bajo el feudalismo, necesitaba transformar las relaciones políticas (superestructura) para que correspondieran a su posición económica (infraestructura). La revolución fue la expresión política de una contradicción material.

## Véase también
- [[modo-de-produccion]]
- [[lucha-de-clases]]
- [[infraestructura-y-superestructura]]
- [[clase-social]]

## Fuentes
- [[el-pensamiento-sociologico-i-los-fundadores]] (Introduccion a la sociologia)
- Marx, Karl (1859). *Contribución a la crítica de la economía política*.""")


c("infraestructura-y-superestructura",
  "Infraestructura y superestructura", "2026-S1", "Introduccion a la sociologia",
  ["materialismo-historico","modo-de-produccion","clase-social","lucha-de-clases","alienacion","reificacion"],
  ["Introduccion a la sociologia","sociologia-clasica","marxismo"],
  """## Definición
Infraestructura (o base) y superestructura son los dos niveles del modelo arquitectónico marxista de la sociedad. La **infraestructura** es la estructura económica: el conjunto de fuerzas productivas y relaciones de producción que constituyen el [[modo-de-produccion]]. La **superestructura** es el conjunto de instituciones políticas, jurídicas, ideológicas, religiosas y culturales que se erigen sobre esa base. Para [[karl-marx]], la infraestructura condiciona la superestructura: "el molino de mano os dará la sociedad con el señor feudal; el molino de vapor, la sociedad con el capitalista industrial".

## Origen y contexto histórico
Marx formuló la metáfora en el *Prefacio a la contribución a la crítica de la economía política* (1859): "El conjunto de las relaciones de producción forma la estructura económica de la sociedad, la base real sobre la que se levanta la superestructura jurídica y política".

## Desarrollo teórico
- La infraestructura comprende: medios de producción, fuerza de trabajo, relaciones de propiedad
- La superestructura comprende: Estado, leyes, ideología, religión, arte, filosofía
- La relación no es mecánica: la superestructura tiene **autonomía relativa** y puede influir sobre la base
- La ideología dominante es la ideología de la clase dominante: justifica las relaciones de producción existentes
- La [[reificacion]] es el efecto ideológico de la superestructura: se naturaliza lo que es producto histórico

## Relación con otros conceptos
- El [[materialismo-historico]] es la teoría general que articula infraestructura y superestructura
- La [[alienacion]] se produce en la infraestructura (trabajo) y se justifica en la superestructura (ideología)
- La [[clase-social]] se define en la infraestructura pero combate en ambos niveles

## Debates y críticas
Gramsci desarrolló el concepto de **hegemonía**: la clase dominante no solo controla los medios de producción sino que logra hacer pasar sus intereses como intereses generales a través de la cultura y la educación (superestructura). Althusser distinguió entre "aparatos represivos del Estado" (policía, ejército) e "ideológicos" (escuela, medios, familia). La crítica principal: la metáfora arquitectónica simplifica relaciones complejas.

## Ejemplo empírico
Las leyes laborales (superestructura) reflejan la correlación de fuerzas entre clases (infraestructura): cuando los sindicatos son fuertes se aprueban leyes proteccionistas; cuando el capital domina, se flexibilizan o eliminan.

## Véase también
- [[materialismo-historico]]
- [[modo-de-produccion]]
- [[clase-social]]
- [[alienacion]]
- [[reificacion]]

## Fuentes
- [[el-pensamiento-sociologico-i-los-fundadores]] (Introduccion a la sociologia)
- Marx, Karl (1859). *Contribución a la crítica de la economía política*.""")


# ═══ WEBER CONCEPTS ═══

c("racionalizacion",
  "Racionalización", "2026-S1", "Introduccion a la sociologia",
  ["burocracia","jaula-de-hierro","modernidad","secularizacion","desencanto-del-mundo","tipos-ideales","etica-protestante"],
  ["Introduccion a la sociologia","sociologia-clasica","weberiana"],
  """## Definición
La racionalización es, para [[max-weber]], el proceso histórico central de la [[modernidad]] occidental: la progresiva sustitución de la tradición, la magia, la costumbre y la afectividad por el cálculo racional, la eficiencia y la previsibilidad como principios organizadores de la vida social. Afecta a todas las esferas: economía (capitalismo contable), política ([[burocracia]]), derecho (codificado), ciencia (método experimental), música (temperamento), religión ([[secularizacion]]).

## Origen y contexto histórico
Weber desarrolló el concepto a lo largo de toda su obra, especialmente en *La ética protestante y el espíritu del capitalismo* (1904) y en *Economía y sociedad* (1922). La pregunta central de Weber era: ¿por qué la racionalización se desarrolló de forma única en Occidente? Su respuesta: la convergencia entre la [[etica-protestante]] (ascetismo intramundano), el derecho romano, la ciencia griega y la administración burocrática.

## Desarrollo teórico
### Tipos de racionalidad
- **Teórica**: dominio conceptual de la realidad mediante abstracciones
- **Práctica**: cálculo medios-fines en la vida cotidiana
- **Formal** (o instrumental): aplicación de reglas, cálculos y procedimientos impersonales
- **Sustantiva** (o material): orientación por valores últimos (justicia, igualdad, salvación)

La tensión central de la modernidad para Weber es el conflicto entre racionalidad formal (eficiencia del sistema) y racionalidad sustantiva (sentido humano).

### Desencanto del mundo
La racionalización produce [[desencanto-del-mundo]]: la ciencia y la técnica sustituyen a la magia y la religión como formas de explicar el mundo. "Ya no hay fuerzas misteriosas en juego; en principio, todo puede ser dominado mediante el cálculo".

## Relación con otros conceptos
- La [[burocracia]] es la forma organizativa de la racionalización
- La [[jaula-de-hierro]] es su consecuencia alienante: un mundo racional pero sin sentido
- La [[secularizacion]] es la racionalización del ámbito religioso
- Los [[tipos-ideales]] son la herramienta metodológica para analizar la racionalización

## Debates y críticas
Habermas distinguió racionalización sistémica (mercado, burocracia) de racionalización comunicativa (diálogo, consenso), argumentando que Weber solo analizó la primera. La Escuela de Frankfurt (Adorno, Horkheimer) radicalizó la crítica: la "razón instrumental" no libera sino que domina — Auschwitz fue un acto burocráticamente racional.

## Ejemplo empírico
La gestión algorítmica del trabajo (Amazon, Uber): cada movimiento del trabajador se calcula, mide y optimiza. Es la racionalización formal llevada al extremo, donde la eficiencia del sistema prevalece sobre el bienestar del individuo.

## Véase también
- [[burocracia]]
- [[jaula-de-hierro]]
- [[modernidad]]
- [[desencanto-del-mundo]]
- [[etica-protestante]]
- [[tipos-ideales]]

## Fuentes
- [[el-pensamiento-sociologico-i-los-fundadores]] (Introduccion a la sociologia)
- Weber, Max (1904). *La ética protestante y el espíritu del capitalismo*.
- Weber, Max (1922). *Economía y sociedad*.""")


c("jaula-de-hierro",
  "Jaula de hierro", "2026-S1", "Introduccion a la sociologia",
  ["racionalizacion","burocracia","modernidad","alienacion","desencanto-del-mundo"],
  ["Introduccion a la sociologia","sociologia-clasica","weberiana"],
  """## Definición
La jaula de hierro (*stahlhartes Gehäuse*, literalmente "estuche duro como el acero") es la metáfora con la que [[max-weber]] describe la condición del ser humano moderno atrapado en un sistema de [[racionalizacion]] burocrática del que ya no puede escapar. La eficiencia, la calculabilidad y la impersonalidad que caracterizan la [[burocracia]] y el capitalismo crean un orden que funciona con independencia de la voluntad humana: "una jaula de hierro" que condiciona la vida de todos.

## Origen y contexto histórico
Weber usó la metáfora al final de *La ética protestante y el espíritu del capitalismo* (1904-05): los puritanos querían ser "profesionales" por devoción religiosa; el capitalismo moderno ya no necesita esa motivación — el sistema funciona por sí solo. "El manto ligero de la preocupación por los bienes externos se ha convertido en una jaula de hierro". La traducción por Talcott Parsons como "iron cage" se ha mantenido en la tradición anglosajona.

## Desarrollo teórico
- La jaula de hierro no es una dictadura personal sino un sistema impersonal: reglas, procedimientos, cálculos
- La [[burocracia]], una vez establecida, es "prácticamente indestructible" porque su eficiencia la hace indispensable
- El individuo moderno está atrapado entre la necesidad de racionalización (sin ella no hay medicina, transporte, derecho) y la pérdida de sentido vital que conlleva
- Weber era profundamente pesimista: no veía alternativa al avance de la racionalización

## Relación con otros conceptos
- La [[racionalizacion]] es el proceso que construye la jaula
- La [[burocracia]] es su forma organizativa concreta
- La [[alienacion]] marxista y la jaula de hierro weberiana son diagnósticos paralelos desde tradiciones distintas
- El [[desencanto-del-mundo]] es la dimensión cultural de la jaula: un mundo sin misterio ni sentido último

## Debates y críticas
Mommsen argumentó que *Gehäuse* no significa "jaula" sino "estuche" o "armazón", suavizando la metáfora: no estamos *encerrados* sino *arropados* por la racionalización. Bauman reinterpretó la jaula para la modernidad líquida: el problema contemporáneo no es el exceso de orden sino su ausencia — la jaula se ha derretido y nos quedamos sin estructura.

## Ejemplo empírico
El sistema fiscal: nadie puede escapar de la racionalización tributaria. Las declaraciones de impuestos, los algoritmos de detección de fraude y la burocracia fiscal son ejemplos de la jaula de hierro: el ciudadano está atrapado en un sistema impersonal que funciona con independencia de su voluntad.

## Véase también
- [[racionalizacion]]
- [[burocracia]]
- [[modernidad]]
- [[desencanto-del-mundo]]
- [[alienacion]]

## Fuentes
- [[el-pensamiento-sociologico-i-los-fundadores]] (Introduccion a la sociologia)
- Weber, Max (1904-05). *La ética protestante y el espíritu del capitalismo*.""")


c("tipos-ideales",
  "Tipos ideales", "2026-S1", "Introduccion a la sociologia",
  ["burocracia","racionalizacion","tipos-de-accion-social","dominacion-legal-racional","dominacion-carismatica","dominacion-tradicional","sociologia-como-ciencia"],
  ["Introduccion a la sociologia","sociologia-clasica","weberiana","metodologia"],
  """## Definición
Los tipos ideales (*Idealtypen*) son construcciones conceptuales elaboradas por el investigador que acentúan deliberadamente ciertos rasgos de un fenómeno social para hacerlo inteligible. No son descripciones de la realidad ni modelos normativos ("ideal" no significa "deseable" sino "puro, construido mentalmente"). Son herramientas heurísticas: la realidad se compara con el tipo ideal para identificar sus desviaciones y peculiaridades. [[max-weber]] los definió como "una utopía que no se encuentra en ninguna parte de la realidad".

## Origen y contexto histórico
Weber formuló el método del tipo ideal en "La 'objetividad' del conocimiento en las ciencias sociales" (1904) y lo aplicó en toda su obra: la [[burocracia]] es un tipo ideal (ninguna burocracia real cumple todas las características), al igual que la [[dominacion-carismatica]], la [[etica-protestante]] o el capitalismo racional.

## Desarrollo teórico
### Construcción del tipo ideal
1. Se seleccionan ciertos rasgos de un fenómeno
2. Se acentúan deliberadamente hasta su coherencia lógica máxima
3. Se obtiene un cuadro mental homogéneo e internamente consistente
4. Se compara con la realidad empírica para medir las distancias

### Función metodológica
- No se pregunta si la realidad "encaja" en el tipo ideal, sino *en qué medida y por qué se desvía*
- Los tipos ideales permiten comparar sociedades, épocas e instituciones usando un patrón común
- Son necesariamente **unilaterales**: resaltan un aspecto a costa de otros

## Relación con otros conceptos
- La [[burocracia]], la [[dominacion-legal-racional]], la [[dominacion-carismatica]] y la [[dominacion-tradicional]] son tipos ideales
- Los [[tipos-de-accion-social]] (racional con arreglo a fines, racional con arreglo a valores, tradicional, afectiva) son tipos ideales
- Se oponen al método positivista que busca leyes generales: Weber aboga por la comprensión (*Verstehen*) de casos singulares

## Debates y críticas
La crítica más frecuente es la circularidad: ¿cómo se seleccionan los rasgos "relevantes" sin teoría previa? Schutz señaló que los tipos ideales de Weber son "construcciones de segundo grado" (construidas sobre las de los propios actores). Parsons los convirtió en clasificaciones rígidas, traicionando su espíritu heurístico.

## Ejemplo empírico
Ningún líder carismático (Jesús, Napoleón, Gandhi) cumple exactamente las características del tipo ideal de [[dominacion-carismatica]], pero comparar cada caso con el tipo ideal permite entender qué tiene de carismático y qué no.

## Véase también
- [[burocracia]]
- [[dominacion-legal-racional]]
- [[dominacion-carismatica]]
- [[tipos-de-accion-social]]
- [[racionalizacion]]

## Fuentes
- [[el-pensamiento-sociologico-i-los-fundadores]] (Introduccion a la sociologia)
- Weber, Max (1904). "La 'objetividad' del conocimiento en las ciencias sociales".""")


# ═══ WRITE ═══

def write_enriched_concepts():
    import os, yaml
    written = 0
    skipped = 0
    for slug, data in CONCEPTS.items():
        filepath = os.path.join(CONCEPTS_DIR, f"{slug}.md")
        existing_fm = {}
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            if content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    try:
                        existing_fm = yaml.safe_load(parts[1]) or {}
                    except:
                        pass
            if "This page aggregates references to" not in content:
                skipped += 1
                print(f"  SKIP (enriched): {slug}")
                continue

        fm = {
            "id": slug, "title": data["title"], "note_type": "concept",
            "semester": data["semester"], "course": data["course"],
            "related_concepts": data["related_concepts"], "tags": data["tags"],
        }
        if "source_notes" in existing_fm:
            fm["source_notes"] = existing_fm["source_notes"]
        if "updated_at" in existing_fm:
            fm["updated_at"] = existing_fm["updated_at"]

        fm_str = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False)
        full_content = f"---\n{fm_str}---\n\n{data['body'].strip()}\n"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(full_content)
        written += 1
        print(f"  WROTE: {slug}")
    print(f"\nDone: {written} written, {skipped} skipped")

if __name__ == "__main__":
    write_enriched_concepts()
