import path from "node:path";
import { promises as fs } from "node:fs";

import { buildWikiArtifacts } from "../src/lib/wiki-build";

async function main(): Promise<void> {
  const projectRoot = process.cwd();
  const wikiRoot = await resolveWikiRoot(projectRoot);

  await buildWikiArtifacts({
    wikiRoot,
    outputRoot: path.join(projectRoot, ".generated"),
    publicRoot: path.join(projectRoot, "public", "generated"),
  });
}

async function resolveWikiRoot(startDirectory: string): Promise<string> {
  const explicit = process.env.JOTAPEDIA_WIKI_ROOT?.trim();
  const attempted = new Set<string>();

  if (explicit) {
    const resolved = path.resolve(explicit);
    attempted.add(resolved);
    if (await directoryExists(resolved)) {
      return resolved;
    }
  }

  let current = path.resolve(startDirectory);
  while (true) {
    const candidate = path.join(current, "data", "wiki");
    attempted.add(candidate);
    if (await directoryExists(candidate)) {
      return candidate;
    }

    const parent = path.dirname(current);
    if (parent === current) {
      break;
    }
    current = parent;
  }

  const fallbackCandidates = [
    path.join(startDirectory, "..", "data", "wiki"),
    path.join(startDirectory, "data", "wiki"),
  ];

  for (const candidate of fallbackCandidates) {
    const resolved = path.resolve(candidate);
    attempted.add(resolved);
    if (await directoryExists(resolved)) {
      return resolved;
    }
  }

  throw new Error(
    `No se ha encontrado data/wiki. Rutas comprobadas: ${[...attempted].join(", ")}`,
  );
}

async function directoryExists(candidate: string): Promise<boolean> {
  try {
    const stat = await fs.stat(candidate);
    return stat.isDirectory();
  } catch {
    return false;
  }
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
