import { IndexView } from "@/components/index-view";
import { loadCatalog } from "@/lib/generated-data";

export default async function AuthorsPage() {
  const catalog = await loadCatalog();
  const entries = catalog
    .filter((entry) => entry.noteType === "author" && !entry.isAlias)
    .sort((left, right) => left.title.localeCompare(right.title, "es"));

  return (
    <IndexView
      title="Autores"
      description="Indice alfabetico de autoras y autores referenciados en la wiki."
      entries={entries}
      emptyMessage="No hay autores disponibles."
    />
  );
}
