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
  - hipotesis-social
---

# Proceso social

## Definicion

Enlace a [[hipotesis-social]] y enlace ambiguo a [[modulo-2]].

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
  assert.match(article.html, /<blockquote>/);
  assert.match(article.html, /<table>/);
  assert.deepEqual(article.toc, [
    { id: "definicion", text: "Definicion", level: 2 },
  ]);

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
