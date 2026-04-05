import Link from "next/link";
import { notFound } from "next/navigation";

import { LegacySourceRedirect } from "@/components/legacy-source-redirect";
import { loadCatalog, loadLegacyMap } from "@/lib/generated-data";

export async function generateStaticParams() {
  const legacyMap = await loadLegacyMap();
  return legacyMap.map((entry) => ({ legacyId: entry.legacyId }));
}

export default async function LegacySourcePage({
  params,
}: {
  params: Promise<{ legacyId: string }>;
}) {
  const { legacyId } = await params;
  const legacyMap = await loadLegacyMap();
  const match = legacyMap.find((entry) => entry.legacyId === legacyId);

  if (!match) {
    notFound();
  }

  if (match.status === "exact" && match.targetRoute) {
    return <LegacySourceRedirect targetRoute={match.targetRoute} />;
  }

  const catalog = await loadCatalog();
  const targetRoutes = match.targetRoutes ?? [];
  const relatedEntries = targetRoutes
    .map((route) => catalog.find((entry) => entry.route === route))
    .filter((entry): entry is NonNullable<typeof entry> => Boolean(entry));

  return (
    <section className="index-page">
      <header className="page-header">
        <h1>Fuente ambigua</h1>
        <p>
          El identificador legado <strong>{legacyId}</strong> corresponde a varias
          fuentes. Elige la ruta canonica que quieras abrir.
        </p>
      </header>

      <ul className="legacy-list">
        {relatedEntries.map((entry) => (
          <li key={entry.route} className="index-card">
            <Link href={entry.route}>{entry.title}</Link>
            <p>
              {entry.semester} · {entry.course}
            </p>
          </li>
        ))}
      </ul>
    </section>
  );
}
