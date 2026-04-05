import { Suspense } from "react";
import Link from "next/link";

import { LegacyQueryRedirector } from "@/components/legacy-query-redirector";
import { loadCatalog } from "@/lib/generated-data";
import { getNoteTypeLabel } from "@/lib/wiki-routes";
import { formatDateEs } from "@/lib/wiki-text";
import type { NoteType } from "@/lib/wiki-types";

export default async function HomePage() {
  const catalog = await loadCatalog();
  const counts = countByType(catalog.map((entry) => entry.noteType));
  const recent = [...catalog]
    .sort((left, right) => right.timestamp.localeCompare(left.timestamp))
    .slice(0, 10);

  return (
    <section className="home-page">
      <Suspense fallback={null}>
        <LegacyQueryRedirector />
      </Suspense>

      <header className="home-hero">
        <div className="home-hero__content">
          <p className="home-hero__eyebrow">Portada</p>
          <h1>Jotapedia</h1>
          <p>
            Enciclopedia sociologica en castellano, generada a partir de la wiki
            del repositorio y organizada como una biblioteca de consulta rapida.
          </p>
          <form action="/buscar" className="home-hero__search">
            <label htmlFor="home-search-input">Buscar en la enciclopedia</label>
            <div>
              <input
                id="home-search-input"
                type="search"
                name="q"
                placeholder="Concepto, autor, tema o fuente"
              />
              <button type="submit">Buscar</button>
            </div>
          </form>
        </div>
      </header>

      <section className="home-grid">
        <article className="portal-card portal-card--highlight">
          <h2>Explorar por secciones</h2>
          <ul className="portal-card__list">
            <li>
              <Link href="/conceptos">Conceptos</Link>
              <span>{counts.concept}</span>
            </li>
            <li>
              <Link href="/autores">Autores</Link>
              <span>{counts.author}</span>
            </li>
            <li>
              <Link href="/cursos">Cursos</Link>
              <span>{counts.course}</span>
            </li>
            <li>
              <Link href="/fuentes">Fuentes</Link>
              <span>{counts.source}</span>
            </li>
          </ul>
        </article>

        <article className="portal-card">
          <h2>Accesos rapidos</h2>
          <ul className="portal-card__links">
            <li>
              <Link href="/buscar?q=sociologia">Buscar sociologia</Link>
            </li>
            <li>
              <Link href="/conceptos">Indice de conceptos</Link>
            </li>
            <li>
              <Link href="/autores">Autores citados</Link>
            </li>
            <li>
              <Link href="/fuentes">Materiales de curso</Link>
            </li>
          </ul>
        </article>

        <article className="portal-card portal-card--wide">
          <h2>Articulos recientes</h2>
          <ul className="recent-list">
            {recent.map((entry) => (
              <li key={entry.route}>
                <div>
                  <Link href={entry.route}>{entry.title}</Link>
                  <p>{entry.preview}</p>
                </div>
                <span>
                  {getNoteTypeLabel(entry.noteType)} · {formatDateEs(entry.timestamp)}
                </span>
              </li>
            ))}
          </ul>
        </article>
      </section>
    </section>
  );
}

function countByType(noteTypes: NoteType[]) {
  return noteTypes.reduce(
    (counts, noteType) => ({
      ...counts,
      [noteType]: counts[noteType] + 1,
    }),
    { concept: 0, author: 0, course: 0, source: 0 },
  );
}
