import { SourcesIndexView } from "@/components/sources-index-view";
import { loadCatalog } from "@/lib/generated-data";

export default async function SourcesPage() {
  const catalog = await loadCatalog();
  const entries = catalog
    .filter((entry) => entry.noteType === "source" && !entry.isAlias)
    .sort((left, right) => left.route.localeCompare(right.route, "es"));

  return <SourcesIndexView entries={entries} />;
}
