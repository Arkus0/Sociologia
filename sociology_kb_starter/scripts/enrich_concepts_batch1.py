"""
Batch enrichment script for sociology wiki concept entries.
Generates academic content following WIKI_RULES.md standards.
Preserves existing frontmatter (source_notes, updated_at) while replacing stub body.
"""

import os
import yaml
import datetime

CONCEPTS_DIR = "data/wiki/concepts"

# ── Concept definitions ────────────────────────────────────────────────
# Each entry: slug -> dict with fields for generating the page
# Keys: title, semester, course, related_concepts, tags, body (markdown)

CONCEPTS = {}

def c(slug, title, semester, course, related, tags, body):
    CONCEPTS[slug] = {
        "title": title,
        "semester": semester,
        "course": course,
        "related_concepts": related,
        "tags": tags,
        "body": body
    }

# ════════════════════════════════════════════════════════════════════════
# CORE INTRO-SOCIOLOGY CONCEPTS
# ════════════════════════════════════════════════════════════════════════

c("socializacion",
  "Socialización", "2026-S1", "Introduccion a la sociologia",
  ["socializacion-primaria","socializacion-secundaria","interiorizacion","rol-social","control-social","agentes-de-socializacion","otros-significativos","otro-generalizado"],
  ["Introduccion a la sociologia","socializacion","proceso-social"],
  """## Definición
La socialización es el proceso continuo mediante el cual los individuos aprenden e interiorizan las normas, valores, roles y expectativas de la sociedad en que viven, convirtiéndose así en miembros competentes de una comunidad. No se limita a la infancia: se extiende a lo largo de toda la vida, desde la adquisición del lenguaje y los primeros vínculos afectivos hasta la adaptación a nuevos entornos laborales, culturales o migratorios. Como señaló Karl Marx, "la naturaleza real del hombre es la totalidad de las relaciones sociales".

## Origen y contexto histórico
El concepto se desarrolla en la tradición del [[interaccionismo-simbolico]] de [[george-herbert-mead]], quien distinguió entre los [[otros-significativos]] (figuras afectivas insustituibles de la infancia) y el [[otro-generalizado]] (la conciencia colectiva interiorizada que guía la conducta adulta). [[peter-berger]] y [[thomas-luckmann]], en *La construcción social de la realidad* (1966), sistematizaron la distinción entre [[socializacion-primaria]] y [[socializacion-secundaria]], y el concepto de [[alternacion]] como resocialización radical.

## Desarrollo teórico
### Socialización primaria
Ocurre en la infancia, en el seno de la familia y los primeros agentes de socialización. Es la más intensa porque configura el "mundo dado por descontado" — el individuo no percibe el suyo como uno de los mundos posibles, sino como *el* mundo en su totalidad. Requiere vínculo afectivo fuerte con los [[otros-significativos]].

### Socialización secundaria
Proceso de aprendizaje que se produce a lo largo de la vida adulta al adquirir nuevos [[rol-social|roles]] (laborales, asociativos, migratorios). No requiere vínculos afectivos fuertes; se guía por el [[otro-generalizado]]. La sociedad moderna multiplica los contextos de socialización secundaria.

### Alternación
[[peter-berger]] define la alternación como un cambio radical de identidad equivalente a "volver a nacer" en una nueva comunidad (conversiones religiosas, migraciones profundas, cambios de clase social). Requiere nuevos otros significativos y un contexto donde las nuevas pautas sean normales.

## Relación con otros conceptos
- La [[interiorizacion]] es el mecanismo central de la socialización: el mundo social se vuelve parte de la personalidad
- El [[control-social]] opera como complemento de la socialización: cuando la interiorización no basta, la sociedad corrige
- Los [[agentes-de-socializacion]] (familia, escuela, medios, pares) son los vehículos concretos del proceso
- El resultado de la socialización es la capacidad de desempeñar [[rol-social|roles sociales]] competentemente
- La [[desviacion-social]] aparece como el reverso de la socialización exitosa

## Debates y críticas
La principal crítica cuestiona si la socialización explica la reproducción del orden social a costa de invisibilizar la agencia individual. ¿Somos lo que la sociedad hace de nosotros o lo que hacemos a partir de ello? Sartre sintetizó: "soy lo que hago a partir de lo que los demás han hecho de mí". Bourdieu refinó el debate con el concepto de *habitus*: disposiciones socialmente adquiridas que generan prácticas sin determinarlas mecánicamente.

## Vigencia contemporánea
La socialización digital plantea nuevos desafíos: los algoritmos de redes sociales funcionan como agentes de socialización que seleccionan qué normas, valores e imágenes del mundo llegan a cada individuo. Las "burbujas informativas" fragmentan el otro generalizado compartido. La pandemia de COVID-19 evidenció el papel de la socialización presencial en el desarrollo infantil.

## Ejemplo empírico
Los estudios sobre "niños salvajes" (Genie Wiley, Oxana Malaya) documentan los efectos de una socialización primaria ausente: retrasos irreversibles en lenguaje, cognición y capacidad relacional. Confirman empíricamente que el ser humano se constituye como persona a través de la interacción social.

## Véase también
- [[socializacion-primaria]]
- [[socializacion-secundaria]]
- [[interiorizacion]]
- [[otros-significativos]]
- [[otro-generalizado]]
- [[control-social]]
- [[alternacion]]
- [[agentes-de-socializacion]]
- [[rol-social]]

## Fuentes
- [[el-proceso-de-socializacion]] (Introduccion a la sociologia)
- [[la-perspectiva-sociologica]] (Introduccion a la sociologia)
- [[la-sociedad-i-el-proceso-de-socializacion]] (Introduccion a la sociologia)
- Berger, Peter L.; Luckmann, Thomas (1966). *La construcción social de la realidad*.
- Mead, George H. (1934). *Mind, Self, and Society*.""")


c("control-social",
  "Control social", "2026-S1", "Introduccion a la sociologia",
  ["socializacion","desviacion-social","etiquetaje","estigma","normalidad","poder","institucion-social"],
  ["Introduccion a la sociologia","control-social","poder"],
  """## Definición
El control social es el conjunto de mecanismos — formales e informales, externos e interiorizados — mediante los cuales una sociedad presiona a sus miembros para que se ajusten a las normas y expectativas establecidas. Abarca desde la fuerza física y la ley hasta la vergüenza, la culpa y el rumor. Es complementario a la [[socializacion]]: donde la interiorización no basta, el control social interviene para corregir la desviación.

## Origen y contexto histórico
[[emile-durkheim]] fue el primero en analizar sistemáticamente el control social al estudiar la [[solidaridad-mecanica]] de las sociedades simples, donde la conciencia colectiva impone conformidad mediante sanciones directas. [[max-weber]] amplió el análisis al distinguir tipos de [[dominacion-legal-racional|dominación]] (tradicional, carismática y legal-racional), cada una con sus mecanismos de control propios. [[erving-goffman]] exploró el control en la vida cotidiana: la gestión de la impresión, el estigma y la vergüenza como reguladores de la conducta.

## Desarrollo teórico
### Mecanismos explícitos
- Fuerza física (policía, ejército)
- Presión económica (despido, multas, incentivos)
- Dispositivos legales (leyes, contratos, reglamentos)

### Mecanismos informales
- Marginación social, rumores, oprobio
- Honor y reputación
- "Cancelación" en redes sociales

### Mecanismos interiorizados
Los más poderosos según [[erving-goffman]]:
- **Vergüenza**: experiencia interna de la mirada desaprobadora del otro — "nos cambia el color de la piel"
- **Culpa**: desaprobación propia sin necesidad de recriminación externa
Cuando estos mecanismos funcionan, la vigilancia externa se vuelve innecesaria.

## Relación con otros conceptos
- La [[normalidad]] es la definición de lo aceptable que el control social mantiene y reproduce
- La [[desviacion-social]] es aquello que el control social busca prevenir o castigar
- El [[etiquetaje]] es un mecanismo de control que asigna identidades negativas a los desviados
- El [[estigma]] ([[erving-goffman]]) es la marca social que resulta de la etiqueta de desviado
- El [[poder]] determina quién define las normas y quién es controlado

## Debates y críticas
Foucault radicalizó el análisis del control social con el concepto de *disciplina*: en la sociedad moderna el control no se ejerce principalmente por la fuerza sino mediante instituciones (escuela, hospital, prisión) que producen sujetos normalizados. La crítica central: el control social es presentado como neutral, pero siempre refleja relaciones de [[poder]] desiguales — los poderosos definen la norma y los marginados la sufren.

## Vigencia contemporánea
La vigilancia digital (cámaras, redes sociales, algoritmos, *social scoring*) inaugura una nueva era de control social. En China, el Sistema de Crédito Social formaliza mecanismos que hasta ahora eran informales. La "cultura de la cancelación" en plataformas digitales funciona como control social descentralizado.

## Ejemplo empírico
El video analizado por Roger Martínez y Jose Mansilla sobre el turismo masivo ilustra cómo el control social opera en la definición de lo "normal": antes se celebraba masivamente; ahora se etiqueta como problemático, pero el turismo "de calidad" (de clase alta) sigue siendo aceptable, lo que revela quién tiene poder para definir la norma.

## Véase también
- [[socializacion]]
- [[desviacion-social]]
- [[normalidad]]
- [[etiquetaje]]
- [[estigma]]
- [[poder]]
- [[institucion-social]]

## Fuentes
- [[normalidad-desviacion-y-poder]] (Introduccion a la sociologia)
- [[el-proceso-de-socializacion]] (Introduccion a la sociologia)
- [[la-perspectiva-sociologica]] (Introduccion a la sociologia)
- Goffman, Erving (1963). *Stigma: Notes on the Management of Spoiled Identity*.""")


c("rol-social",
  "Rol social", "2026-S1", "Introduccion a la sociologia",
  ["socializacion","institucion-social","estigma","genero","clase-social","control-social","identidad-social"],
  ["Introduccion a la sociologia","rol-social","estructura-social"],
  """## Definición
Un rol social es una manera tipificada de actuar asociada a una posición determinada en la estructura social. Cada rol lleva consigo un conjunto de expectativas sobre cómo debe comportarse quien lo ocupa (alumno, profesor, madre, trabajador) y un margen de interpretación personal. En una sociedad, cada individuo desempeña simultáneamente múltiples roles que pueden ser complementarios o entrar en conflicto.

## Origen y contexto histórico
El concepto proviene de la metáfora teatral: "rol" (del francés *rôle*) significa "papel". [[george-herbert-mead]] y el interaccionismo simbólico formalizaron su uso sociológico al mostrar que la identidad se construye a través de la interacción y la adopción de roles. [[erving-goffman]], en *La presentación de la persona en la vida cotidiana* (1959), desarrolló la "dramaturgia social": la vida social como representación teatral donde interpretamos roles con máscaras (*persona*), mantenemos una "fachada" pública y un "bastidor" privado.

## Desarrollo teórico
### Teoría de los roles
- Los roles son **maneras tipificadas de actuar** ligadas a posiciones sociales
- Existe un guion social (expectativas del rol) y un margen de interpretación (estilo personal)
- El conflicto de roles surge cuando las expectativas de dos roles son incompatibles (ej.: madre/profesional)

### Roles y estructura social
Los roles que adoptamos o se nos atribuyen están condicionados por la posición en la estructura social:
- El **género** condiciona qué roles se asignan (ej.: "jugar a fútbol es de niños")
- La **clase social** determina qué roles son accesibles
- El **prestigio** asociado a ciertos roles reproduce la desigualdad

### Etimología: persona = máscara
En el teatro clásico, la *persona* era la máscara del actor. Sociológicamente, todos llevamos "máscaras" — representamos roles. La perspectiva sociológica es **desenmascaradora**: revela los roles que interpretamos y las máscaras que usamos.

## Relación con otros conceptos
- La [[socializacion]] es el proceso por el cual aprendemos a desempeñar roles
- Las [[institucion-social|instituciones sociales]] son el conjunto de pautas que regulan los roles
- El [[genero]] es un sistema de roles socialmente construidos (no biológicamente determinados)
- El [[estigma]] aparece cuando alguien fracasa en la representación del rol esperado
- La [[rutinizacion]] convierte los roles en comportamientos automáticos

## Debates y críticas
La crítica feminista ha señalado que la teoría de los roles puede naturalizar la desigualdad al presentar roles desiguales (ama de casa, cuidadora) como simples "diferencias funcionales". Bourdieu prefiere hablar de *habitus*: no solo representamos roles, sino que los incorporamos en disposiciones corporales y mentales que reproducen la dominación sin que lo percibamos.

## Vigencia contemporánea
La economía de plataformas crea nuevos roles ambiguos (trabajador/autónomo/emprendedor) que desafían las categorías clásicas. La fluidez de identidades de género desestabiliza la asignación tradicional de roles por sexo. El teletrabajo difumina la separación entre roles profesionales y familiares.

## Ejemplo empírico
Marta Rovira (UOC) ilustra la asignación de roles de género con su experiencia infantil: "me decían que no podía jugar a fútbol porque es de niños". Cuando creces descubres que es la sociedad — no la naturaleza — la que determina qué roles corresponden a cada género.

## Véase también
- [[socializacion]]
- [[institucion-social]]
- [[genero]]
- [[identidad-social]]
- [[estigma]]
- [[rutinizacion]]
- [[estratificacion-social]]

## Fuentes
- [[el-proceso-de-socializacion]] (Introduccion a la sociologia)
- [[la-perspectiva-sociologica]] (Introduccion a la sociologia)
- [[la-sociedad-ii-el-proceso-de-institucionalizacion]] (Introduccion a la sociologia)
- Goffman, Erving (1959). *La presentación de la persona en la vida cotidiana*.""")


c("alienacion",
  "Alienación", "2026-S1", "Introduccion a la sociologia",
  ["reificacion","fetichismo-de-la-mercancia","lucha-de-clases","modo-de-produccion","division-del-trabajo","clase-social"],
  ["Introduccion a la sociologia","sociologia-clasica","marxismo"],
  """## Definición
La alienación (del latín *alienus*, ajeno) es el proceso mediante el cual el ser humano se vuelve extraño a sí mismo, a su trabajo, a los productos de su actividad y a los demás. En la teoría de [[karl-marx]], es la condición fundamental del trabajador en el [[modo-de-produccion]] capitalista: al no controlar ni los medios de producción ni el producto de su trabajo, el obrero se convierte en un apéndice de la máquina y pierde su esencia como ser creativo y social.

## Origen y contexto histórico
Marx desarrolló el concepto en los *Manuscritos económico-filosóficos* (1844), influido por la noción hegeliana de *Entfremdung* (extrañamiento): para Hegel, la alienación era una fase necesaria del despliegue del Espíritu. Marx la materializó: la alienación no es un problema del pensamiento sino de las condiciones materiales de existencia. La [[division-del-trabajo]] capitalista separa al productor de su producto, convirtiéndolo en mercancía.

## Desarrollo teórico
### Las cuatro dimensiones de la alienación (Marx)
1. **Del producto**: el trabajador no posee lo que produce; el objeto se le enfrenta como algo ajeno
2. **Del proceso de trabajo**: el trabajo es externo al obrero, no le pertenece; se siente "fuera de sí"
3. **De la especie** (*Gattungswesen*): el trabajo alienado convierte la actividad vital humana en mero medio de subsistencia, negando la esencia creativa del ser humano
4. **De los otros**: la alienación destruye las relaciones humanas auténticas; los demás se convierten en competidores

### Fetichismo de la mercancía
En *El Capital* (1867), Marx transforma la alienación filosófica en el concepto de [[fetichismo-de-la-mercancia]]: las relaciones sociales entre personas aparecen como relaciones entre cosas (mercancías). El valor, que es trabajo humano cristalizado, parece una propiedad natural del objeto.

## Relación con otros conceptos
- La [[reificacion]] (Berger-Luckmann, Lukács) generaliza la alienación: el ser humano olvida que ha producido el mundo social y lo vive como facticidad ajena
- La [[lucha-de-clases]] es la respuesta colectiva a la alienación: solo la transformación de las relaciones de producción puede superarla
- La [[anomia]] durkheimiana es la contraparte funcionalista de la alienación marxista: ambas señalan una ruptura entre el individuo y la sociedad, pero por causas y soluciones distintas
- La [[division-del-trabajo]] es tanto causa de alienación (Marx) como fuente de [[solidaridad-organica]] (Durkheim)

## Debates y críticas
Weber desplazó el foco: la alienación no es solo económica sino burocrática — la [[jaula-de-hierro]] de la racionalización moderna atrapa al individuo con independencia de la propiedad de los medios. Los frankfurtianos (Marcuse, Adorno) ampliaron la alienación al consumo y la industria cultural: en el capitalismo avanzado, los trabajadores son también alienados como consumidores.

## Vigencia contemporánea
La "uberización" del trabajo actualiza las cuatro dimensiones de la alienación: el repartidor de plataforma no controla el algoritmo (proceso), no posee la app (producto), reduce su actividad a entregas mecánicas (especie) y compite contra otros repartidores (otros). La gamificación laboral añade una dimensión nueva: la alienación se presenta como "engagement" o diversión.

## Ejemplo empírico
Las cadenas de montaje de Amazon, documentadas por investigaciones periodísticas y sociológicas, muestran trabajadores cuyo ritmo está dictado por algoritmos, que no pueden comunicarse entre sí y cuyo rendimiento se mide en segundos. Ilustran las cuatro dimensiones de la alienación marxista en pleno siglo XXI.

## Véase también
- [[reificacion]]
- [[fetichismo-de-la-mercancia]]
- [[lucha-de-clases]]
- [[division-del-trabajo]]
- [[anomia]]
- [[jaula-de-hierro]]

## Fuentes
- [[el-pensamiento-sociologico-i-los-fundadores]] (Introduccion a la sociologia)
- [[diferenciacion-social-y-division-del-trabajo]] (Introduccion a la sociologia)
- Marx, Karl (1844). *Manuscritos económico-filosóficos*.
- Marx, Karl (1867). *El Capital*, vol. I.""")


c("anomia",
  "Anomía", "2026-S1", "Introduccion a la sociologia",
  ["solidaridad-mecanica","solidaridad-organica","division-del-trabajo","hecho-social","conciencia-colectiva","alienacion","individualismo"],
  ["Introduccion a la sociologia","sociologia-clasica","durkheimiana"],
  """## Definición
La anomía (del griego *a-nomos*, sin ley) es la situación social caracterizada por la ausencia, debilitamiento o contradicción de las normas que regulan el comportamiento colectivo. En la teoría de [[emile-durkheim]], la anomía surge cuando los cambios sociales rápidos (industrialización, crisis económicas) destruyen los marcos normativos sin que se hayan consolidado otros nuevos, dejando a los individuos sin referentes para orientar su conducta. Es una patología social, no individual.

## Origen y contexto histórico
Durkheim introdujo el concepto en *La división del trabajo social* (1893) para describir una forma patológica de la [[division-del-trabajo]]: cuando la especialización crece más rápido que la regulación moral, la sociedad pierde cohesión. Lo desarrolló en *El suicidio* (1897), donde identificó el **suicidio anómico** como el tipo asociado a la desregulación normativa — aumenta en crisis económicas tanto por empobrecimiento como por enriquecimiento repentino, porque ambos rompen las expectativas normativas.

## Desarrollo teórico
### Anomía en Durkheim
- En sociedades de [[solidaridad-mecanica]], la anomía es rara porque la [[conciencia-colectiva]] es fuerte y uniforme
- En sociedades de [[solidaridad-organica]], la diferenciación funcional puede generar anomía si no se desarrollan nuevas formas de regulación moral
- La anomía es una crisis de integración normativa, no de integración social (que produce el suicidio egoísta)

### Anomía en Merton
Robert K. Merton reformuló el concepto en "Social Structure and Anomie" (1938): la anomía surge de la discrepancia entre metas culturales (éxito económico) y medios institucionales legítimos (educación, trabajo). Los individuos responden con: conformismo, innovación (medios ilegítimos), ritualismo, retraimiento o rebelión.

## Relación con otros conceptos
- La [[solidaridad-organica]] necesita regulación moral para evitar la anomía; sin ella, la [[division-del-trabajo]] produce patología en vez de cohesión
- La [[alienacion]] marxista y la anomía durkheimiana son diagnósticos paralelos de la modernidad: Marx señala causas económicas, Durkheim causas morales
- El [[individualismo]] moderno es condición necesaria de la anomía: en sociedades con conciencia colectiva fuerte no hay espacio para ella
- La [[desviacion-social]] puede ser una respuesta individual a la anomía (innovación en Merton)

## Debates y críticas
La principal crítica a Durkheim es su conservadurismo implícito: diagnosticar anomía implica que existe un estado "normal" de regulación al cual hay que volver, lo que dificulta pensar la transformación social radical. Merton fue criticado por presuponer que el "sueño americano" es universal y que la desviación es siempre respuesta a la falta de medios.

## Vigencia contemporánea
Bauman habla de "modernidad líquida" — un estado de anomía permanente donde la flexibilidad y la incertidumbre se normalizan. La precariedad laboral, la crisis de la vivienda y el nihilismo digital son interpretados como manifestaciones contemporáneas de anomía. La polarización política puede leerse como intento de reconstruir marcos normativos en una sociedad anómica.

## Ejemplo empírico
Los estudios de Durkheim mostraron que las tasas de suicidio aumentaban tanto en recesiones como en booms económicos: en ambos casos se rompen las expectativas normativas sobre lo que uno puede esperar de la vida. Este hallazgo contraintuitivo confirmaba que el suicidio anómico es un fenómeno social, no psicológico.

## Véase también
- [[solidaridad-mecanica]]
- [[solidaridad-organica]]
- [[division-del-trabajo]]
- [[hecho-social]]
- [[alienacion]]
- [[desviacion-social]]

## Fuentes
- [[el-pensamiento-sociologico-i-los-fundadores]] (Introduccion a la sociologia)
- [[diferenciacion-social-y-division-del-trabajo]] (Introduccion a la sociologia)
- Durkheim, Émile (1893). *La división del trabajo social*.
- Durkheim, Émile (1897). *El suicidio*.
- Merton, Robert K. (1938). "Social Structure and Anomie".""")


c("institucion-social",
  "Institución social", "2026-S1", "Introduccion a la sociologia",
  ["institucionalizacion","socializacion","rutinizacion","rol-social","legitimidad","control-social","dialectica-social"],
  ["Introduccion a la sociologia","estructura-social"],
  """## Definición
Una institución social es un conjunto estable y organizado de pautas, normas y roles que regulan un ámbito fundamental de la vida colectiva (familia, educación, economía, religión, política). Las instituciones no son edificios ni organizaciones concretas, sino los patrones de conducta tipificados y legitimados que hacen predecible la vida social. Sin instituciones — sin rutinas, roles, estructuras — no hay sociedad.

## Origen y contexto histórico
[[peter-berger]] y [[thomas-luckmann]], en *La construcción social de la realidad* (1966), explican la [[institucionalizacion]] como proceso dialéctico en tres momentos: (1) **exteriorización** (el ser humano produce el mundo social), (2) **objetivación** (ese mundo se solidifica y adquiere facticidad) y (3) **interiorización** (el mundo objetivado vuelve a la conciencia mediante la [[socializacion]]). [[emile-durkheim]] ya había definido las instituciones como "hechos sociales" que se imponen al individuo con fuerza coercitiva.

## Desarrollo teórico
### La dialéctica social (Berger y Luckmann)
La institucionalización surge de la **habitualización**: toda acción repetida se tipifica. Cuando dos individuos tipifican mutuamente sus acciones habitualizadas, nace una institución. La institución se transmite a las generaciones siguientes como realidad objetiva — los hijos no la vivieron en su formación y la perciben como "así son las cosas".

### Legitimidad
Las instituciones requieren [[legitimidad]] — explicaciones y justificaciones que las hagan plausibles para quienes no participaron en su creación. Berger y Luckmann distinguen cuatro niveles de legitimación, desde la simple transmisión lingüística hasta los "universos simbólicos" que integran toda la realidad institucional.

### Instituciones y cambio
Las instituciones cambian (familia, trabajo, religión han cambiado profundamente), pero **no pueden desaparecer**: sin pautas que regulen la interacción, la vida social sería caos.

## Relación con otros conceptos
- La [[rutinizacion]] es el mecanismo básico de la institucionalización: las sorpresas se convierten en rutinas que se tipifican
- Los [[rol-social|roles]] son las cristalizaciones de la institución en posiciones concretas
- La [[socializacion]] es el proceso por el cual las instituciones se transmiten a los nuevos miembros
- La [[reificacion]] es el grado máximo de institucionalización: se olvida que la institución es producto humano
- La [[burocracia]] (Weber) es una forma institucional característica de la [[modernidad]]

## Debates y críticas
Marx consideraba las instituciones como superestructura determinada por la base económica y al servicio de la clase dominante. El institucionalismo sociológico (DiMaggio, Powell) mostró que las instituciones pueden persistir por "isomorfismo" (imitación entre organizaciones) sin que sirvan a ningún interés claro. La crítica feminista revela que la institución familiar ha legitimado históricamente la desigualdad de género.

## Vigencia contemporánea
La "desinstitucionalización" de la vida contemporánea (matrimonios menos estables, trabajos más precarios, educación más flexible) no elimina las instituciones sino que las transforma. Las plataformas digitales (Uber, Airbnb) crean nuevas instituciones informales con reglas propias (ratings, algoritmos) que regulan comportamientos sin la legitimación tradicional.

## Ejemplo empírico
La familia es el ejemplo paradigmático de institución social: tiene roles tipificados (padre, madre, hijo), normas de conducta (responsabilidades parentales, herencia), mecanismos de control (presión familiar, vergüenza) y formas de legitimación (amor, religión, ley). Pero su forma concreta varía enormemente entre culturas y épocas.

## Véase también
- [[institucionalizacion]]
- [[rutinizacion]]
- [[rol-social]]
- [[legitimidad]]
- [[socializacion]]
- [[reificacion]]
- [[burocracia]]

## Fuentes
- [[la-perspectiva-sociologica]] (Introduccion a la sociologia)
- [[la-sociedad-ii-el-proceso-de-institucionalizacion]] (Introduccion a la sociologia)
- Berger, Peter L.; Luckmann, Thomas (1966). *La construcción social de la realidad*.""")


c("burocracia",
  "Burocracia", "2026-S1", "Introduccion a la sociologia",
  ["dominacion-legal-racional","racionalizacion","jaula-de-hierro","tipos-ideales","modernidad","institucion-social"],
  ["Introduccion a la sociologia","sociologia-clasica","weberiana"],
  """## Definición
La burocracia es la forma de organización racional-legal caracterizada por una jerarquía definida, una división sistemática del trabajo, reglas impersonales codificadas, procedimientos estandarizados y la selección del personal según competencias técnicas. [[max-weber]] la identificó como el tipo de [[dominacion-legal-racional|dominación legal-racional]] propio de la [[modernidad]], al mismo tiempo eficiente e inevitable, pero también potencialmente alienante — una "jaula de hierro" de la [[racionalizacion]].

## Origen y contexto histórico
Weber desarrolló su análisis de la burocracia en *Economía y sociedad* (1922) como parte de su tipología de la dominación. Observó que la burocratización avanzaba tanto en el Estado como en la empresa, la Iglesia y los partidos políticos. Para Weber, la burocracia era técnicamente superior a cualquier otra forma de organización, del mismo modo que la máquina era superior a la producción manual, pero este mismo triunfo conllevaba la pérdida de sentido y libertad.

## Desarrollo teórico
### Características del tipo ideal burocrático
1. **Jerarquía de autoridad**: cadena de mando clara, de arriba a abajo
2. **Reglas escritas e impersonales**: la autoridad reside en el cargo, no en la persona
3. **División del trabajo por especialización**: cada funcionario tiene competencias definidas
4. **Selección meritocrática**: ingreso y promoción por capacidad técnica, no por herencia o favoritismo
5. **Separación entre vida privada y cargo**: los bienes del cargo no pertenecen al funcionario
6. **Documentación escrita**: toda acción se registra en expedientes

### La jaula de hierro
Weber advirtió que la burocracia, una vez plenamente desarrollada, es "prácticamente indestructible": su eficiencia la hace imprescindible y su impersonalidad impide la alternativa. La [[jaula-de-hierro]] (*stahlhartes Gehäuse*) designa esta trampa de la [[racionalizacion]]: una sociedad técnicamente perfecta pero espiritualmente vacía.

## Relación con otros conceptos
- Es la expresión organizativa de la [[racionalizacion]] (proceso central de la modernidad según Weber)
- Se opone a la [[dominacion-carismatica]] (personal, emocional) y a la [[dominacion-tradicional]] (basada en la costumbre)
- Los [[tipos-ideales]] son la herramienta metodológica que Weber usa para construir el modelo — ninguna burocracia real coincide exactamente con el tipo ideal
- La [[alienacion]] marxista tiene su equivalente weberiano en la despersonalización burocrática

## Debates y críticas
Merton señaló las "disfunciones de la burocracia": las reglas pensadas como medios se convierten en fines (ritualismo), la impersonalidad genera rigidez y la especialización impide ver el conjunto. Crozier (1964) mostró que los actores dentro de las burocracias desarrollan estrategias informales de poder que subvierten el modelo racional. La crítica feminista señala que la burocracia reproduce la separación público/privado que invisibiliza el trabajo doméstico.

## Vigencia contemporánea
La burocracia digital (formularios electrónicos, algoritmos de decisión automatizada) intensifica la impersonalidad weberiana: no es ya un funcionario quien decide sino un código informático inaccesible. Los debates sobre "gobierno abierto" y "administración ágil" intentan romper la jaula de hierro, pero las organizaciones tienden a reburocratizarse.

## Ejemplo empírico
El sistema sanitario público ilustra la tensión burocrática: la atención médica requiere reglas impersonales (protocolos, listas de espera) para ser equitativa, pero los pacientes demandan una atención personalizada que la lógica burocrática dificulta.

## Véase también
- [[racionalizacion]]
- [[jaula-de-hierro]]
- [[dominacion-legal-racional]]
- [[tipos-ideales]]
- [[modernidad]]
- [[institucion-social]]

## Fuentes
- [[el-pensamiento-sociologico-i-los-fundadores]] (Introduccion a la sociologia)
- [[la-sociedad-ii-el-proceso-de-institucionalizacion]] (Introduccion a la sociologia)
- Weber, Max (1922). *Economía y sociedad*.""")


c("interiorizacion",
  "Interiorización", "2026-S1", "Introduccion a la sociologia",
  ["socializacion","socializacion-primaria","exteriorizacion","objetivacion","mundo-dado-por-descontado","instituciones"],
  ["Introduccion a la sociologia","proceso-social"],
  """## Definición
La interiorización es el proceso por el cual el individuo asimila las normas, valores, relaciones y expectativas del entorno social hasta convertirlos en parte de su propia personalidad. Es el tercer momento de la dialéctica social de [[peter-berger]] y [[thomas-luckmann]] (tras la [[exteriorizacion]] y la [[objetivacion]]): la sociedad, que fue producto humano, vuelve a entrar en la conciencia individual y es vivida como "mi" mundo, "mis" valores, "mi" forma de pensar.

## Origen y contexto histórico
Berger y Luckmann sistematizaron el concepto en *La construcción social de la realidad* (1966), apoyándose en la fenomenología de Schütz y el interaccionismo de Mead. Marta Rovira (UOC) lo sintetiza así: lo que aprendemos en la infancia no conforma "uno de los mundos posibles" sino **el mundo en su totalidad**. De ahí la resistencia a cambiar prejuicios: están interiorizados como realidad incuestionable.

## Desarrollo teórico
- La interiorización comienza en la [[socializacion-primaria]] con los [[otros-significativos]] y continúa durante toda la vida
- El resultado es el [[mundo-dado-por-descontado]]: un "manual" para actuar en sociedad que funciona precisamente porque no es cuestionado
- Cuando la interiorización es exitosa, los límites entre libertad personal y [[control-social]] se desdibujan: "la sociedad está dentro de nosotros"
- La interiorización no es pasiva — el sujeto no es un recipiente vacío, sino que interpreta y negocia lo que interioriza

## Relación con otros conceptos
- Es el mecanismo central de la [[socializacion]]: sin interiorización no hay persona social
- Se complementa con [[exteriorizacion]] (el ser humano produce el mundo social) y [[objetivacion]] (el mundo adquiere facticidad)
- El [[mundo-dado-por-descontado]] es su resultado: la realidad cotidiana percibida como "la realidad"
- La [[reificacion]] es una interiorización "excesiva": el sujeto olvida completamente el origen humano de las instituciones

## Debates y críticas
Bourdieu criticó la dicotomía exterior/interior como demasiado simple y propuso el *habitus*: disposiciones incorporadas que no son ni puramente externas ni puramente internas. La interiorización bergeriana presupone un sujeto que "recibe" la sociedad, mientras que Bourdieu insiste en que la sociedad se inscribe en el cuerpo (posturas, gustos, acentos).

## Vigencia contemporánea
Los algoritmos de recomendación interiorizan preferencias que el individuo vive como "sus" gustos, cuando en realidad son el resultado de patrones de consumo masivos filtrados por inteligencia artificial. La personalización digital produce mundos-dados-por-descontado cada vez más fragmentados.

## Ejemplo empírico
Los prejuicios raciales o de género se interiorizan en la infancia y operan como esquemas automáticos — los tests de asociación implícita (IAT) demuestran que incluso personas que rechazan conscientemente los prejuicios los tienen interiorizados a nivel inconsciente.

## Véase también
- [[socializacion]]
- [[exteriorizacion]]
- [[objetivacion]]
- [[mundo-dado-por-descontado]]
- [[reificacion]]

## Fuentes
- [[el-proceso-de-socializacion]] (Introduccion a la sociologia)
- [[la-sociedad-i-el-proceso-de-socializacion]] (Introduccion a la sociologia)
- [[la-sociedad-ii-el-proceso-de-institucionalizacion]] (Introduccion a la sociologia)
- Berger, Peter L.; Luckmann, Thomas (1966). *La construcción social de la realidad*.""")


c("reificacion",
  "Reificación", "2026-S1", "Introduccion a la sociologia",
  ["alienacion","interiorizacion","objetivacion","institucion-social","perspectiva-sociologica","fetichismo-de-la-mercancia"],
  ["Introduccion a la sociologia","sociologia-clasica"],
  """## Definición
La reificación (del latín *res*, cosa) es el proceso por el cual los seres humanos olvidan que han producido el mundo social y lo viven como si fuera una realidad ajena, natural o sobrehumana — "como si fuesen cosas", en palabras de [[peter-berger]] y [[thomas-luckmann]]. El mundo reificado es un mundo deshumanizado donde el individuo no se reconoce como productor de sus propias instituciones.

## Origen y contexto histórico
El término proviene del marxismo: [[karl-marx]] analizó la reificación como [[fetichismo-de-la-mercancia]] en *El Capital* (1867): las relaciones sociales entre personas aparecen como relaciones entre cosas. Georg Lukács lo generalizó en *Historia y conciencia de clase* (1923): la reificación es la forma de conciencia propia del capitalismo. Berger y Luckmann lo integraron en su teoría constructivista: la reificación es la fase extrema de la [[objetivacion]], cuando se pierde la conciencia del origen humano de las instituciones.

## Desarrollo teórico
Berger y Luckmann definen la reificación como "la aprehensión de los fenómenos humanos como si fuesen cosas [...] como hechos de la naturaleza, resultados de leyes cósmicas o manifestaciones de la voluntad divina". La reificación implica:
- El ser humano olvida que él mismo ha creado el mundo social
- La [[dialectica-social]] entre productor y productos se vuelve invisible
- El mundo aparece como *opus alienum* (obra ajena) sobre el cual el individuo no tiene control

La [[perspectiva-sociologica]] es, según Estruch, una perspectiva **desreificadora**: invierte el camino de la reificación recuperando la conciencia de que la sociedad es producto humano.

## Relación con otros conceptos
- La [[alienacion]] marxista es la forma económica de la reificación: el trabajador no se reconoce en su producto
- La [[interiorizacion]] puede conducir a la reificación cuando el sujeto interioriza la realidad social como inmutable
- La [[perspectiva-sociologica]] es la antítesis de la reificación: es una perspectiva **relativizadora** que revela la construcción social de la realidad
- "Sociológicamente no hay nada natural" — la reificación consiste precisamente en llamar "natural" a lo que es social

## Debates y críticas
Habermas criticó el concepto lukácsiano de reificación como demasiado totalizante: no toda objetivación es reificación, y las instituciones cumplen funciones necesarias. La socialización requiere cierto grado de objetivación para funcionar — el problema comienza cuando se pierde toda conciencia del carácter construido.

## Vigencia contemporánea
Los algoritmos presentan sus resultados como "objetivos" y "neutrales", ocultando las decisiones humanas (de diseño, de datos, de valores) que los producen. La reificación algorítmica es una nueva forma de reificación: el código como "naturaleza" digital.

## Ejemplo empírico
Cuando se afirma que "es natural que la mujer cuide de los hijos", se está reificando un arreglo social históricamente variable: en otras épocas y culturas el cuidado se organizaba de formas muy distintas. La perspectiva sociológica desreifica: revela la construcción social detrás de lo que parece natural.

## Véase también
- [[alienacion]]
- [[fetichismo-de-la-mercancia]]
- [[interiorizacion]]
- [[objetivacion]]
- [[perspectiva-sociologica]]

## Fuentes
- [[la-perspectiva-sociologica]] (Introduccion a la sociologia)
- [[la-sociedad-ii-el-proceso-de-institucionalizacion]] (Introduccion a la sociologia)
- Berger, Peter L.; Luckmann, Thomas (1966). *La construcción social de la realidad*, pág. 116.
- Marx, Karl (1867). *El Capital*, vol. I.
- Lukács, Georg (1923). *Historia y conciencia de clase*.""")


c("normalidad",
  "Normalidad", "2026-S1", "Introduccion a la sociologia",
  ["desviacion-social","poder","control-social","etiquetaje","estigma","perspectiva-sociologica"],
  ["Introduccion a la sociologia","control-social"],
  """## Definición
La normalidad es un concepto sociológico relativo que designa aquello que una sociedad o grupo define como aceptable, habitual o conforme a la norma. No es un estado objetivo ni universal: lo que es "normal" depende siempre del grupo de referencia, el contexto histórico y, crucialmente, de las relaciones de [[poder]]. La sociología revela que la normalidad es una construcción social, no un hecho natural.

## Origen y contexto histórico
El análisis sociológico de la normalidad se remonta a [[emile-durkheim]], quien en *Las reglas del método sociológico* (1895) definió lo "normal" estadísticamente (lo que se da en la mayoría de los casos) pero reconoció que esta definición no captura la dimensión normativa. Roger Martínez y Jose Mansilla (UOC, 2022) sistematizaron la reflexión: la normalidad puede significar lo mayoritario, lo habitual, lo ajustado a la norma, lo obvio o el no desviarse.

## Desarrollo teórico
### Normalidad y poder
- Aunque equiparamos lo normal con lo mayoritario, frecuentemente tiene más que ver con el [[poder]] que con la cantidad
- Una minoría poderosa puede hacer creer a la mayoría que lo que hace o piensa no es normal
- "Hay normalidades que son más normales que otras" (paráfrasis de Orwell)
- Los que tienen poder (clases altas, medios de comunicación, políticos) tienen más capacidad para definir lo normal

### Relatividad de la normalidad
- "Nosotros somos los otros de los otros" — lo que vemos como diferente es lo que nos ve como diferentes
- La normalidad varía entre culturas, épocas y clases sociales
- Hoy se cuestiona no solo cómo se define lo normal, sino la misma idea de que exista "una" normalidad (ej.: identidades de género)

## Relación con otros conceptos
- La [[desviacion-social]] es lo que se sale de la normalidad — pero quién define la normalidad define la desviación
- El [[control-social]] mantiene los límites de lo normal mediante mecanismos que van de la fuerza a la vergüenza
- El [[etiquetaje]] asigna la categoría de "desviado" a quien transgrede la normalidad
- El [[estigma]] marca socialmente a quien ha sido etiquetado como anormal
- La [[perspectiva-sociologica]] desnaturaliza la normalidad: muestra que lo "normal" es socialmente construido

## Debates y críticas
Foucault argumentó que la normalización es el mecanismo central del poder moderno: no se castiga la desviación, se produce la normalidad a través de instituciones disciplinarias (escuela, hospital, prisión). La crítica queer ha puesto en cuestión la "heteronormalidad" como régimen de poder que patologiza las disidencias sexuales y de género.

## Vigencia contemporánea
La pandemia de COVID-19 generó un intenso debate sobre la "nueva normalidad": ¿quién la define y en beneficio de quién? Los movimientos de neurodiversidad rechazan la categoría de "anormalidad" para el autismo o el TDAH, proponiendo que la diversidad neurológica es parte de la normalidad humana.

## Ejemplo empírico
El turismo masivo: antes era "normal" celebrarlo como desarrollo; ahora los movimientos vecinales lo etiquetan como problema. Pero el turismo "de calidad" (de alto poder adquisitivo) sigue siendo normal — revelando que el poder económico define qué turismo es aceptable.

## Véase también
- [[desviacion-social]]
- [[poder]]
- [[control-social]]
- [[etiquetaje]]
- [[estigma]]
- [[perspectiva-sociologica]]

## Fuentes
- [[normalidad-desviacion-y-poder]] (Introduccion a la sociologia)
- Martínez, Roger; Mansilla, Jose (2022). "Normalidad, desviación y poder". Barcelona: UOC.""")


# ── Batch write function ───────────────────────────────────────────────

def write_enriched_concepts():
    written = 0
    skipped = 0
    for slug, data in CONCEPTS.items():
        filepath = os.path.join(CONCEPTS_DIR, f"{slug}.md")

        # Read existing file to preserve source_notes and updated_at
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
            # Skip if already enriched
            if "This page aggregates references to" not in content:
                skipped += 1
                print(f"  SKIP (already enriched): {slug}")
                continue

        # Build new frontmatter
        fm = {
            "id": slug,
            "title": data["title"],
            "note_type": "concept",
            "semester": data["semester"],
            "course": data["course"],
            "related_concepts": data["related_concepts"],
            "tags": data["tags"],
        }
        # Preserve compiler-managed fields
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
