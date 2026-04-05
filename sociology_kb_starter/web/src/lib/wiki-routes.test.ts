import test from "node:test";
import assert from "node:assert/strict";

import {
  buildLegacyQueryRedirect,
  buildNoteRoute,
  buildSourceIndexAnchor,
} from "./wiki-routes";

test("buildNoteRoute genera rutas canonicas para conceptos", () => {
  assert.equal(
    buildNoteRoute({
      noteType: "concept",
      slug: "proceso-social",
      relativePath: "concepts/proceso-social.md",
    }),
    "/conceptos/proceso-social",
  );
});

test("buildNoteRoute genera rutas canonicas para sources por path", () => {
  assert.equal(
    buildNoteRoute({
      noteType: "source",
      slug: "modulo-2",
      relativePath:
        "sources/2026-s1/introduccion-a-la-sociologia/modulo-2.md",
    }),
    "/fuentes/2026-s1/introduccion-a-la-sociologia/modulo-2",
  );
});

test("buildLegacyQueryRedirect traduce enlaces legacy de Streamlit", () => {
  assert.equal(
    buildLegacyQueryRedirect({
      view: "search",
      q: "proceso social",
    }),
    "/buscar?q=proceso%20social",
  );

  assert.equal(
    buildLegacyQueryRedirect({
      article: "adam-smith",
      type: "author",
    }),
    "/autores/adam-smith",
  );

  assert.equal(
    buildLegacyQueryRedirect({
      article: "modulo-2",
      type: "source",
    }),
    "/legado/fuentes/modulo-2",
  );
});

test("buildSourceIndexAnchor crea anclas coherentes para fuentes", () => {
  assert.equal(buildSourceIndexAnchor("2026-S1", undefined), "/fuentes#2026-s1");
  assert.equal(
    buildSourceIndexAnchor("2026-S1", "Introduccion a la sociologia"),
    "/fuentes#2026-s1-introduccion-a-la-sociologia",
  );
});
