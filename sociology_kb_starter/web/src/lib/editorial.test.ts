import assert from "node:assert/strict";
import test from "node:test";

import {
  getEditorialTeaser,
  pickArticleOfTheWeek,
  pickEditorialStarts,
  pickWeeklyFacts,
} from "./editorial";
import type { CatalogEntry, FactCard } from "./wiki-types";

const FIXTURE_CATALOG: CatalogEntry[] = [
  {
    id: "sociologia",
    slug: "sociologia",
    title: "Sociologia",
    noteType: "concept",
    route: "/conceptos/sociologia",
    routeSegments: ["conceptos", "sociologia"],
    relativePath: "concepts/sociologia.md",
    preview: "La sociologia estudia estructuras, instituciones y cambio social.",
    hook: "La sociologia sirve para ver como problemas aparentemente privados nacen de reglas y estructuras colectivas.",
    timestamp: "2026-04-06T12:00:00.000Z",
    aliases: [],
    isAlias: false,
    backlinkCount: 3,
    wordCount: 620,
  },
  {
    id: "max-weber",
    slug: "max-weber",
    title: "Max Weber",
    noteType: "author",
    route: "/autores/max-weber",
    routeSegments: ["autores", "max-weber"],
    relativePath: "authors/max-weber.md",
    preview: "Autor clasico de la accion social.",
    hook: "Weber sigue siendo util cuando queremos entender por que la gente obedece reglas que no ha elegido.",
    timestamp: "2026-04-05T12:00:00.000Z",
    aliases: [],
    isAlias: false,
    backlinkCount: 4,
    wordCount: 810,
  },
  {
    id: "fuente",
    slug: "fuente",
    title: "Modulo 1",
    noteType: "source",
    route: "/fuentes/2026-s1/introduccion-a-la-sociologia/modulo-1",
    routeSegments: ["fuentes", "2026-s1", "introduccion-a-la-sociologia", "modulo-1"],
    relativePath: "sources/2026-s1/introduccion-a-la-sociologia/modulo-1.md",
    preview: "Fuente de apoyo.",
    timestamp: "2026-04-04T12:00:00.000Z",
    aliases: [],
    isAlias: false,
    backlinkCount: 0,
    wordCount: 300,
  },
];

test("getEditorialTeaser prioriza el hook para home, tarjetas y autocomplete", () => {
  assert.equal(
    getEditorialTeaser({
      hook: "Texto corto con gancho.",
      preview: "Resumen largo academico.",
    }),
    "Texto corto con gancho.",
  );
});

test("pickEditorialStarts devuelve el piloto en el orden editorial previsto", () => {
  const picks = pickEditorialStarts(FIXTURE_CATALOG, 2);
  assert.deepEqual(
    picks.map((entry) => entry.slug),
    ["sociologia", "max-weber"],
  );
});

test("pickArticleOfTheWeek elige solo conceptos y autores canonicos", () => {
  const picked = pickArticleOfTheWeek(FIXTURE_CATALOG, new Date("2026-04-06T09:00:00Z"));
  assert.ok(picked);
  assert.notEqual(picked?.noteType, "source");
});

test("pickWeeklyFacts rota sobre el conjunto sin salirse del limite", () => {
  const facts: FactCard[] = [
    { text: "Uno lo bastante largo para entrar en la rotacion semanal.", articleTitle: "A", articleRoute: "/a", noteType: "concept", kind: "hook" },
    { text: "Dos lo bastante largo para entrar en la rotacion semanal.", articleTitle: "B", articleRoute: "/b", noteType: "concept", kind: "quick_point" },
    { text: "Tres lo bastante largo para entrar en la rotacion semanal.", articleTitle: "C", articleRoute: "/c", noteType: "concept", kind: "why_now" },
  ];

  const picks = pickWeeklyFacts(facts, 2, new Date("2026-04-06T09:00:00Z"));
  assert.equal(picks.length, 2);
  assert.ok(picks.every((fact) => facts.includes(fact)));
});
