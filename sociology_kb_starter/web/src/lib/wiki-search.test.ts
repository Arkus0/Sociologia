import assert from "node:assert/strict";
import test from "node:test";

import { searchDocuments, suggestDocuments } from "./wiki-search";
import type { SearchIndex } from "./wiki-types";

const FIXTURE_INDEX: SearchIndex = {
  docCount: 2,
  docFreq: {
    marx: 1,
    clase: 1,
    social: 1,
  },
  docs: [
    {
      route: "/autores/karl-marx",
      title: "Karl Marx",
      noteType: "author",
      preview: "Autor central en la teoria del conflicto.",
      hook: "Marx sirve para leer como el conflicto atraviesa trabajo, clase y poder.",
      semester: "2026-S1",
      course: "Introduccion a la sociologia",
      aliases: ["Marx"],
      isAlias: false,
      fieldTokens: {
        title: { karl: 1, marx: 1 },
        aliases: { marx: 1 },
        concepts: {},
        authors: {},
        summary: { autor: 1, central: 1, teoria: 1, conflicto: 1 },
        body: { clase: 1, social: 1 },
      },
    },
    {
      route: "/conceptos/clase-social",
      title: "Clase social",
      noteType: "concept",
      preview: "Concepto sociologico sobre estratificacion.",
      hook: "La clase social sigue ordenando oportunidades muy concretas en vivienda, estudios y empleo.",
      semester: "2026-S1",
      course: "Metodologia de las ciencias sociales",
      aliases: [],
      isAlias: false,
      fieldTokens: {
        title: { clase: 1, social: 1 },
        aliases: {},
        concepts: {},
        authors: { marx: 1 },
        summary: { concepto: 1, sociologico: 1 },
        body: { clase: 2, social: 2 },
      },
    },
  ],
};

test("searchDocuments incluye alias en el ranking", () => {
  const results = searchDocuments(FIXTURE_INDEX, "marx");
  assert.equal(results[0]?.route, "/autores/karl-marx");
});

test("searchDocuments permite filtrar por tipo", () => {
  const results = searchDocuments(FIXTURE_INDEX, "marx", 20, {
    noteTypes: ["concept"],
  });
  assert.deepEqual(results.map((result) => result.route), [
    "/conceptos/clase-social",
  ]);
});

test("suggestDocuments tolera errores tipograficos simples", () => {
  const suggestions = suggestDocuments(FIXTURE_INDEX, "marxx");
  assert.equal(suggestions[0]?.route, "/autores/karl-marx");
});

test("searchDocuments permite filtrar por curso y semestre", () => {
  const results = searchDocuments(FIXTURE_INDEX, "clase", 20, {
    course: "Metodologia de las ciencias sociales",
    semester: "2026-S1",
  });

  assert.deepEqual(results.map((result) => result.route), [
    "/conceptos/clase-social",
  ]);
});

test("suggestDocuments respeta los filtros de curso", () => {
  const suggestions = suggestDocuments(FIXTURE_INDEX, "marx", 8, {
    course: "Introduccion a la sociologia",
  });

  assert.deepEqual(suggestions.map((result) => result.route), [
    "/autores/karl-marx",
  ]);
});

test("suggestDocuments tambien encuentra coincidencias presentes en el hook editorial", () => {
  const suggestions = suggestDocuments(FIXTURE_INDEX, "vivienda");
  assert.equal(suggestions[0]?.route, "/conceptos/clase-social");
});
