import { IndexView } from "@/components/index-view";
import { loadCatalog } from "@/lib/generated-data";

export default async function ConceptsPage() {
  const catalog = await loadCatalog();
  const entries = catalog
    .filter((entry) => entry.noteType === "concept")
    .sort((left, right) => left.title.localeCompare(right.title, "es"));

  return (
    <IndexView
      title="Conceptos"
      description="Indice alfabetico de conceptos sociologicos presentes en Jotapedia."
      entries={entries}
      emptyMessage="No hay conceptos disponibles."
    />
  );
}
