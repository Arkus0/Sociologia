import { IndexView } from "@/components/index-view";
import { loadCatalog } from "@/lib/generated-data";

export default async function CoursesPage() {
  const catalog = await loadCatalog();
  const entries = catalog
    .filter((entry) => entry.noteType === "course" && !entry.isAlias)
    .sort((left, right) => left.title.localeCompare(right.title, "es"));

  return (
    <IndexView
      title="Cursos"
      description="Puertas de entrada a las asignaturas presentes en la wiki sociologica."
      entries={entries}
      emptyMessage="No hay cursos disponibles."
    />
  );
}
