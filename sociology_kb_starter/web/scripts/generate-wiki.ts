import path from "node:path";

import { buildWikiArtifacts } from "../src/lib/wiki-build";

async function main(): Promise<void> {
  const projectRoot = process.cwd();

  await buildWikiArtifacts({
    wikiRoot: path.join(projectRoot, "..", "data", "wiki"),
    outputRoot: path.join(projectRoot, ".generated"),
    publicRoot: path.join(projectRoot, "public", "generated"),
  });
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
