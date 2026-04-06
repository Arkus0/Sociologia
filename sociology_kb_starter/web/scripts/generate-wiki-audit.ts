import path from "node:path";
import { promises as fs } from "node:fs";

interface QualityBacklogItem {
  route?: string;
  title?: string;
  noteType?: string;
  count: number;
  maxPriority?: number;
  reference?: string;
}

interface QualityReport {
  generatedAt: string;
  summary: {
    issues: number;
    byKind: Record<string, number>;
  };
  backlog: {
    topDocuments: QualityBacklogItem[];
    topReferences: QualityBacklogItem[];
  };
}

interface CatalogEntry {
  noteType: "concept" | "author" | "course" | "source";
  isAlias: boolean;
}

async function main(): Promise<void> {
  const projectRoot = process.cwd();
  const repoRoot = path.resolve(projectRoot, "..");
  const generatedRoot = path.join(projectRoot, ".generated");
  const [qualityReport, catalog] = await Promise.all([
    readJson<QualityReport>(path.join(generatedRoot, "quality-report.json")),
    readJson<CatalogEntry[]>(path.join(generatedRoot, "catalog.json")),
  ]);

  const canonical = catalog.filter((entry) => !entry.isAlias);
  const aliases = catalog.length - canonical.length;
  const byType = canonical.reduce<Record<string, number>>((acc, entry) => {
    acc[entry.noteType] = (acc[entry.noteType] ?? 0) + 1;
    return acc;
  }, {});

  const lines = [
    "# Auditoria Wiki Actual",
    "",
    `Generada el ${qualityReport.generatedAt}.`,
    "",
    "## Inventario",
    "",
    `- Entradas canonicas: ${canonical.length}`,
    `- Alias legacy: ${aliases}`,
    `- Conceptos: ${byType.concept ?? 0}`,
    `- Autores: ${byType.author ?? 0}`,
    `- Cursos: ${byType.course ?? 0}`,
    `- Fuentes: ${byType.source ?? 0}`,
    "",
    "## Calidad",
    "",
    `- Incidencias totales: ${qualityReport.summary.issues}`,
    ...Object.entries(qualityReport.summary.byKind)
      .sort((left, right) => right[1] - left[1])
      .map(([kind, count]) => `- ${kind}: ${count}`),
    "",
    "## Documentos prioritarios",
    "",
    ...qualityReport.backlog.topDocuments.slice(0, 15).map((entry, index) =>
      `${index + 1}. ${entry.title ?? entry.route} (${entry.noteType}, ${entry.count} incidencias, prioridad maxima ${entry.maxPriority ?? 0})`,
    ),
    "",
    "## Referencias recurrentes",
    "",
    ...qualityReport.backlog.topReferences.slice(0, 15).map((entry, index) =>
      `${index + 1}. ${entry.reference} (${entry.count} incidencias, prioridad maxima ${entry.maxPriority ?? 0})`,
    ),
    "",
    "## Lectura operativa",
    "",
    "- La deuda editorial ya esta priorizada por frecuencia e impacto gracias al backlog del linter.",
    "- Los alias siguen disponibles para compatibilidad, pero no deben contaminar indices ni descubrimiento principal.",
    "- La siguiente ronda editorial debe centrarse en stubs de autores y conceptos con missing_required_section o missing_related_concepts.",
    "",
  ];

  await fs.writeFile(
    path.join(repoRoot, "AUDITORIA_WIKI_ACTUAL.md"),
    `${lines.join("\n")}\n`,
    "utf8",
  );
}

async function readJson<T>(filePath: string): Promise<T> {
  return JSON.parse(await fs.readFile(filePath, "utf8")) as T;
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
