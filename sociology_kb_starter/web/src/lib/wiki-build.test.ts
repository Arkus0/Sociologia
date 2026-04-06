import test from "node:test";
import assert from "node:assert/strict";
import os from "node:os";
import path from "node:path";
import { promises as fs } from "node:fs";

import { buildWikiArtifacts } from "./wiki-build";

test("buildWikiArtifacts compila markdown, resuelve wikilinks y no modifica la wiki fuente", async () => {
  const tempRoot = await fs.mkdtemp(path.join(os.tmpdir(), "jotapedia-web-"));
  const wikiRoot = path.join(tempRoot, "wiki");
  const outputRoot = path.join(tempRoot, ".generated");
  const publicRoot = path.join(tempRoot, "public", "generated");

  await fs.mkdir(path.join(wikiRoot, "concepts"), { recursive: true });
  await fs.mkdir(path.join(wikiRoot, "authors"), { recursive: true });
  await fs.mkdir(path.join(wikiRoot, "courses"), { recursive: true });
  await fs.mkdir(
    path.join(wikiRoot, "sources", "2026-s1", "introduccion-a-la-sociologia"),
    { recursive: true },
  );
  await fs.mkdir(
    path.join(
      wikiRoot,
      "sources",
      "2026-s1",
      "metodologia-de-las-ciencias-sociales",
    ),
    { recursive: true },
  );

  const files = new Map<string, string>([
    [
      path.join(wikiRoot, "concepts", "proceso-social.md"),
      `---
id: proceso-social
title: "Proceso social"
note_type: concept
updated_at: "2026-04-05"
related_concepts:
  - "[[hipotesis-social]]"
authors:
  - Karl Marx
---

# Proceso social

## Definicion

Enlace a [[hipotesis-social]], enlace ambiguo a [[modulo-2]] y referencia a [[marx]].

> Cita de apoyo

| Campo | Valor |
| --- | --- |
| A | B |
`,
    ],
    [
      path.join(wikiRoot, "concepts", "hipotesis-social.md"),
      `---
id: hipotesis-social
title: "Hipotesis social"
note_type: concept
updated_at: "2026-04-05"
---

# Hipotesis social

## Definicion

Una hipotesis de ejemplo.
`,
    ],
    [
      path.join(wikiRoot, "concepts", "modelo-isi.md"),
      `---
id: modelo-isi
title: "Modelo ISI (Industrializacion por Sustitucion de Importaciones)"
note_type: concept
updated_at: "2026-04-05"
---

# Modelo ISI

## Definicion

Concepto de prueba para validar referencias humanizadas.
`,
    ],
    [
      path.join(wikiRoot, "authors", "karl-marx.md"),
      `---
id: karl-marx
title: "Karl Marx"
note_type: author
updated_at: "2026-04-05"
source_notes:
  - modulo-2
---

# Karl Marx

## Resumen

Autor de prueba para validar alias y backlinks.
`,
    ],
    [
      path.join(wikiRoot, "authors", "salvador-cardus.md"),
      `---
id: salvador-cardus
title: "Salvador Cardus i Ros"
note_type: author
updated_at: "2026-04-05"
---

# Salvador Cardus i Ros

## Biographical sketch

Autor de prueba para validar referencias humanizadas.
`,
    ],
    [
      path.join(wikiRoot, "authors", "marx.md"),
      `\ufeff---
id: marx
title: "Marx"
note_type: author
updated_at: "2026-04-05"
---

Véase [[karl-marx|Karl Marx]].
`,
    ],
    [
      path.join(wikiRoot, "courses", "introduccion-a-la-sociologia.md"),
      `---
id: introduccion-a-la-sociologia
title: "Introduccion a la sociologia"
note_type: course
updated_at: "2026-04-05"
---

# Introduccion a la sociologia

## Alcance

Curso de prueba.
`,
    ],
    [
      path.join(
        wikiRoot,
        "sources",
        "2026-s1",
        "introduccion-a-la-sociologia",
        "modulo-2.md",
      ),
      `---
id: modulo-2
title: "Modulo 2"
note_type: source
semester: 2026-S1
course: Introduccion a la sociologia
concepts:
  - Modelo ISI
authors:
  - Salvador Cardús
compiled_at: "2026-04-05T00:00:00+00:00"
---

# Modulo 2

## Summary

Material introductorio.
`,
    ],
    [
      path.join(
        wikiRoot,
        "sources",
        "2026-s1",
        "metodologia-de-las-ciencias-sociales",
        "modulo-2.md",
      ),
      `---
id: modulo-2
title: "Modulo 2 de metodologia"
note_type: source
semester: 2026-S1
course: Metodologia de las ciencias sociales
compiled_at: "2026-04-05T00:00:00+00:00"
---

# Modulo 2 de metodologia

## Summary

Material metodologico.
`,
    ],
  ]);

  for (const [filePath, contents] of files) {
    await fs.writeFile(filePath, contents, "utf8");
  }

  const beforeSnapshot = await snapshotMarkdownFiles(wikiRoot);

  await buildWikiArtifacts({
    wikiRoot,
    outputRoot,
    publicRoot,
  });

  const afterSnapshot = await snapshotMarkdownFiles(wikiRoot);
  assert.deepEqual(afterSnapshot, beforeSnapshot);

  const catalog = JSON.parse(
    await fs.readFile(path.join(outputRoot, "catalog.json"), "utf8"),
  ) as Array<{ route: string }>;
  assert.ok(catalog.some((entry) => entry.route === "/conceptos/proceso-social"));

  const legacyMap = JSON.parse(
    await fs.readFile(path.join(outputRoot, "legacy-map.json"), "utf8"),
  ) as Array<{
    legacyId: string;
    status: string;
    targetRoutes?: string[];
  }>;
  assert.deepEqual(
    legacyMap.find((entry) => entry.legacyId === "modulo-2"),
    {
      legacyId: "modulo-2",
      legacyType: "source",
      status: "ambiguous",
      targetRoutes: [
        "/fuentes/2026-s1/introduccion-a-la-sociologia/modulo-2",
        "/fuentes/2026-s1/metodologia-de-las-ciencias-sociales/modulo-2",
      ],
    },
  );

  const article = JSON.parse(
    await fs.readFile(
      path.join(outputRoot, "articles", "conceptos", "proceso-social.json"),
      "utf8",
    ),
  ) as {
    html: string;
    toc: Array<{ id: string; text: string; level: number }>;
  };

  assert.match(article.html, /href="\/conceptos\/hipotesis-social"/);
  assert.match(article.html, /href="\/legado\/fuentes\/modulo-2"/);
  assert.match(article.html, /href="\/autores\/karl-marx"/);
  assert.match(article.html, /<blockquote>/);
  assert.match(article.html, /<table>/);
  assert.deepEqual(article.toc, [
    { id: "definicion", text: "Definicion", level: 2 },
  ]);

  const aliasArticle = JSON.parse(
    await fs.readFile(
      path.join(outputRoot, "articles", "autores", "marx.json"),
      "utf8",
    ),
  ) as {
    isAlias: boolean;
    canonicalEntry?: { route: string; title: string };
    backlinks: Array<{ route: string }>;
  };
  assert.equal(aliasArticle.isAlias, true);
  assert.deepEqual(aliasArticle.canonicalEntry, {
    route: "/autores/karl-marx",
    title: "Karl Marx",
    noteType: "author",
  });
  assert.ok(
    aliasArticle.backlinks.some((entry) => entry.route === "/conceptos/proceso-social"),
  );

  const searchIndex = JSON.parse(
    await fs.readFile(path.join(outputRoot, "search-index.json"), "utf8"),
  ) as {
    docs: Array<{ route: string; aliases: string[] }>;
  };
  assert.ok(searchIndex.docs.some((entry) => entry.route === "/autores/karl-marx"));
  assert.ok(!searchIndex.docs.some((entry) => entry.route === "/autores/marx"));
  assert.deepEqual(
    searchIndex.docs.find((entry) => entry.route === "/autores/karl-marx")?.aliases,
    ["Marx"],
  );

  const qualityReport = JSON.parse(
    await fs.readFile(path.join(outputRoot, "quality-report.json"), "utf8"),
  ) as {
    summary: { byKind: Record<string, number> };
    issues: Array<{ kind: string; detail: string; documentRoute?: string }>;
  };
  assert.ok((qualityReport.summary.byKind.ambiguous_reference ?? 0) >= 1);
  assert.equal(qualityReport.summary.byKind.duplicate_id, undefined);
  assert.ok(
    !qualityReport.issues.some(
      (issue) =>
        issue.documentRoute === "/autores/marx" &&
        issue.kind === "thin_preview",
    ),
  );
  assert.ok(
    !qualityReport.issues.some(
      (issue) =>
        issue.documentRoute === "/conceptos/proceso-social" &&
        issue.detail === "Referencia sin resolver: Karl Marx",
    ),
  );
  assert.ok(
    !qualityReport.issues.some(
      (issue) =>
        issue.documentRoute === "/conceptos/proceso-social" &&
        issue.detail === "Referencia sin resolver: [[hipotesis-social]]",
    ),
  );
  assert.ok(
    !qualityReport.issues.some(
      (issue) =>
        issue.documentRoute ===
          "/fuentes/2026-s1/introduccion-a-la-sociologia/modulo-2" &&
        issue.detail === "Referencia sin resolver: Modelo ISI",
    ),
  );
  assert.ok(
    !qualityReport.issues.some(
      (issue) =>
        issue.documentRoute ===
          "/fuentes/2026-s1/introduccion-a-la-sociologia/modulo-2" &&
        issue.detail === "Referencia sin resolver: Salvador Cardús",
    ),
  );

  const publicSearchIndex = await fs.readFile(
    path.join(publicRoot, "search-index.json"),
    "utf8",
  );
  assert.ok(publicSearchIndex.length > 0);
});

async function snapshotMarkdownFiles(root: string) {
  const files = await collectMarkdownFiles(root);
  const snapshot = new Map<string, string>();

  for (const filePath of files) {
    const relative = path.relative(root, filePath).replace(/\\/g, "/");
    snapshot.set(relative, await fs.readFile(filePath, "utf8"));
  }

  return [...snapshot.entries()].sort(([left], [right]) =>
    left.localeCompare(right, "es"),
  );
}

async function collectMarkdownFiles(root: string): Promise<string[]> {
  const results: string[] = [];
  await walk(root, results);
  return results.sort((left, right) => left.localeCompare(right, "es"));
}

async function walk(directory: string, results: string[]): Promise<void> {
  const entries = await fs.readdir(directory, { withFileTypes: true });

  for (const entry of entries) {
    const fullPath = path.join(directory, entry.name);
    if (entry.isDirectory()) {
      await walk(fullPath, results);
      continue;
    }
    if (entry.isFile() && entry.name.endsWith(".md")) {
      results.push(fullPath);
    }
  }
}
