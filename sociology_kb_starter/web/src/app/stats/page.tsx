import Link from "next/link";

import { loadCatalog, loadQualityReport } from "@/lib/generated-data";
import { getNoteTypeLabel } from "@/lib/wiki-routes";
import type { CatalogEntry, NoteType } from "@/lib/wiki-types";

export default async function StatsPage() {
  const catalog = await loadCatalog();
  const quality = await loadQualityReport();

  const canonical = catalog.filter((e) => !e.isAlias);
  const byType = groupBy(canonical, (e) => e.noteType);
  const totalArticles = canonical.length;
  const totalWords = canonical.reduce((sum, e) => sum + e.wordCount, 0);

  // Most-linked articles (by backlink count)
  const mostLinked = [...canonical]
    .sort((a, b) => b.backlinkCount - a.backlinkCount)
    .slice(0, 15);

  // Recently updated
  const recentlyUpdated = [...canonical]
    .sort((a, b) => b.timestamp.localeCompare(a.timestamp))
    .slice(0, 10);

  // Longest articles
  const longest = [...canonical]
    .sort((a, b) => b.wordCount - a.wordCount)
    .slice(0, 10);

  return (
    <section className="stats-page">
      <header className="page-header">
        <h1>Estadisticas de Jotapedia</h1>
        <p>
          Un vistazo cuantitativo a la enciclopedia. Datos generados en tiempo
          de compilacion.
        </p>
      </header>

      <div className="stats-grid">
        <div className="stat-card">
          <span className="stat-card__value">{totalArticles}</span>
          <span className="stat-card__label">Articulos</span>
        </div>
        {(["concept", "author", "course", "source"] as NoteType[]).map((type) => (
          <div className="stat-card" key={type}>
            <span className="stat-card__value">{byType[type]?.length ?? 0}</span>
            <span className="stat-card__label">{getNoteTypeLabel(type)}</span>
          </div>
        ))}
        <div className="stat-card">
          <span className="stat-card__value">{formatNumber(totalWords)}</span>
          <span className="stat-card__label">Palabras totales</span>
        </div>
        <div className="stat-card">
          <span className="stat-card__value">
            {totalArticles > 0 ? Math.round(totalWords / totalArticles) : 0}
          </span>
          <span className="stat-card__label">Palabras / articulo</span>
        </div>
        <div className="stat-card">
          <span className="stat-card__value">{quality.summary.issues}</span>
          <span className="stat-card__label">Incidencias</span>
        </div>
      </div>

      <div className="home-grid">
        <section className="stats-ranking">
          <h2>Articulos mas enlazados</h2>
          <ol>
            {mostLinked.map((entry) => (
              <li key={entry.route}>
                <Link href={entry.route}>{entry.title}</Link>
                <span>{entry.backlinkCount} backlinks</span>
              </li>
            ))}
          </ol>
        </section>

        <section className="stats-ranking">
          <h2>Articulos mas largos</h2>
          <ol>
            {longest.map((entry) => (
              <li key={entry.route}>
                <Link href={entry.route}>{entry.title}</Link>
                <span>{formatNumber(entry.wordCount)} palabras</span>
              </li>
            ))}
          </ol>
        </section>

        <section className="stats-ranking portal-card--wide">
          <h2>Ultimas actualizaciones</h2>
          <ol>
            {recentlyUpdated.map((entry) => (
              <li key={entry.route}>
                <Link href={entry.route}>{entry.title}</Link>
                <span>{getNoteTypeLabel(entry.noteType)} · {entry.timestamp.slice(0, 10)}</span>
              </li>
            ))}
          </ol>
        </section>
      </div>
    </section>
  );
}

function groupBy<T>(items: T[], key: (item: T) => string): Record<string, T[]> {
  const result: Record<string, T[]> = {};
  for (const item of items) {
    const k = key(item);
    (result[k] ??= []).push(item);
  }
  return result;
}

function formatNumber(n: number): string {
  if (n >= 1000) {
    return `${(n / 1000).toFixed(1).replace(/\.0$/, "")}k`;
  }
  return String(n);
}
