import assert from "node:assert/strict";
import test from "node:test";
import { renderToStaticMarkup } from "react-dom/server";

import { ArticleView } from "./article-view";
import type { ArticlePayload } from "@/lib/wiki-types";

const BASE_ARTICLE: ArticlePayload = {
  id: "norma-social",
  title: "Norma social",
  slug: "norma-social",
  noteType: "concept",
  route: "/conceptos/norma-social",
  routeSegments: ["conceptos", "norma-social"],
  html: "<h2 id=\"definicion\">Definicion</h2><p>Texto academico largo.</p>",
  preview: "Las normas sociales ordenan la convivencia y hacen previsibles las interacciones.",
  hook: "Las normas sociales te dicen cuando hablar, cuando callar y que te costara saltarte el guion.",
  quickPoints: [
    "No son solo leyes: tambien son habitos, miradas y expectativas.",
    "Funcionan porque anticipamos la reaccion del grupo.",
  ],
  whyNow: "Siguen organizando reputacion, visibilidad y autocontrol en plataformas digitales.",
  everydayExample: "En un grupo de WhatsApp de trabajo, responder tarde puede parecer una falta aunque nadie lo haya escrito.",
  timestamp: "2026-04-06T10:00:00.000Z",
  toc: [{ id: "definicion", text: "Definicion", level: 2 }],
  breadcrumbs: [
    { label: "Portada", href: "/" },
    { label: "Conceptos", href: "/conceptos" },
    { label: "Norma social" },
  ],
  infobox: [{ label: "Curso", value: "Introduccion a la sociologia" }],
  aliases: [],
  isAlias: false,
  relatedLinks: [{ title: "Control social", route: "/conceptos/control-social", noteType: "concept" }],
  backlinks: [],
  frontmatterSubset: {},
  wordCount: 480,
};

test("ArticleView renderiza la capa editorial encima del cuerpo largo", () => {
  const html = renderToStaticMarkup(<ArticleView article={BASE_ARTICLE} />);

  assert.match(html, /Las normas sociales te dicen cuando hablar/);
  assert.match(html, /En 30 segundos/);
  assert.match(html, /Por que importa hoy/);
  assert.match(html, /Ejemplo cotidiano/);
  assert.match(html, /Texto academico largo/);
});

test("ArticleView oculta callouts opcionales cuando no hay datos editoriales", () => {
  const html = renderToStaticMarkup(
    <ArticleView
      article={{
        ...BASE_ARTICLE,
        hook: undefined,
        quickPoints: undefined,
        whyNow: undefined,
        everydayExample: undefined,
      }}
    />,
  );

  assert.doesNotMatch(html, /En 30 segundos/);
  assert.doesNotMatch(html, /Por que importa hoy/);
  assert.doesNotMatch(html, /Ejemplo cotidiano/);
  assert.match(html, /Las normas sociales ordenan la convivencia/);
});
