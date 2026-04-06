import { Suspense } from "react";
import Link from "next/link";

import { LegacyQueryRedirector } from "@/components/legacy-query-redirector";
import {
  getEditorialTeaser,
  getFactKindLabel,
  pickArticleOfTheWeek,
  pickEditorialStarts,
  pickWeeklyFacts,
} from "@/lib/editorial";
import { loadCatalog, loadFacts } from "@/lib/generated-data";
import { getNoteTypeLabel } from "@/lib/wiki-routes";
import { formatDateEs } from "@/lib/wiki-text";
import type { NoteType } from "@/lib/wiki-types";

export default async function HomePage() {
  const catalog = await loadCatalog();
  const canonicalCatalog = catalog.filter((entry) => !entry.isAlias);
  const facts = await loadFacts();
  const counts = countByType(canonicalCatalog.map((entry) => entry.noteType));
  const recent = [...canonicalCatalog]
    .sort((left, right) => right.timestamp.localeCompare(left.timestamp))
    .slice(0, 10);

  const articleOfTheWeek = pickArticleOfTheWeek(canonicalCatalog);
  const editorialStarts = pickEditorialStarts(canonicalCatalog, 3);
  const weeklyFacts = pickWeeklyFacts(facts, 4);

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
        {articleOfTheWeek ? (
          <article className="article-of-the-week portal-card--wide">
            <p className="article-of-the-week__label">Articulo de la semana</p>
            <h2>
              <Link href={articleOfTheWeek.route}>{articleOfTheWeek.title}</Link>
            </h2>
            <p>{getEditorialTeaser(articleOfTheWeek)}</p>
            <Link href={articleOfTheWeek.route} className="article-of-the-week__cta">
              Leer articulo -&gt;
            </Link>
          </article>
        ) : null}

        {weeklyFacts.length > 0 ? (
          <article className="portal-card portal-card--wide sabias-que">
            <h2>¿Sabias que...?</h2>
            <ul className="sabias-que__list">
              {weeklyFacts.map((fact, index) => (
                <li key={`${fact.articleRoute}-${fact.kind}-${index}`} className="sabias-que__item">
                  <span className="sabias-que__badge">{getFactKindLabel(fact.kind)}</span>
                  <p>{fact.text}</p>
                  <Link href={fact.articleRoute}>{fact.articleTitle} -&gt;</Link>
                </li>
              ))}
            </ul>
          </article>
        ) : null}

        {editorialStarts.length > 0 ? (
          <article className="portal-card portal-card--highlight">
            <h2>Empieza aqui</h2>
            <ul className="editorial-starts">
              {editorialStarts.map((entry) => (
                <li key={entry.route}>
                  <div>
                    <Link href={entry.route}>{entry.title}</Link>
                    <p>{getEditorialTeaser(entry)}</p>
                  </div>
                  <span>{getNoteTypeLabel(entry.noteType)}</span>
                </li>
              ))}
            </ul>
          </article>
        ) : null}

        <article className="portal-card">
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
          </ul>
        </article>

        <article className="portal-card">
          <h2>Accesos rapidos</h2>
          <ul className="portal-card__links">
            <li>
              <Link href="/buscar?q=sociologia">Buscar sociologia</Link>
            </li>
            <li>
              <Link href="/grafo">Grafo de conocimiento</Link>
            </li>
            <li>
              <Link href="/aleatoria">Articulo aleatorio</Link>
            </li>
            <li>
              <a href="/generated/feed.xml">RSS de Jotapedia</a>
            </li>
          </ul>
        </article>

        <article className="portal-card subscribe-card">
          <h2>Suscribete</h2>
          <p>
            Cada lunes recibiras el articulo de la semana, datos curiosos y las
            ultimas novedades de Jotapedia.
          </p>
          <form
            action="https://buttondown.com/api/emails/embed-subscribe/jota_sociopedia"
            method="post"
            className="subscribe-card__form"
          >
            <label htmlFor="bd-email" className="sr-only">
              Tu email
            </label>
            <input
              type="email"
              name="email"
              id="bd-email"
              placeholder="tu@email.com"
              required
              className="subscribe-card__input"
            />
            <button type="submit" className="subscribe-card__btn">
              Suscribirme
            </button>
          </form>
          <p className="subscribe-card__hint">
            Tambien puedes seguirnos via{" "}
            <a href="/generated/feed.xml" target="_blank" rel="noopener noreferrer">
              RSS
            </a>{" "}
            con Feedly, Inoreader o Thunderbird.
          </p>
        </article>

        <article className="portal-card portal-card--wide">
          <h2>Articulos recientes</h2>
          <ul className="recent-list">
            {recent.map((entry) => (
              <li key={entry.route}>
                <div>
                  <Link href={entry.route}>{entry.title}</Link>
                  <p>{getEditorialTeaser(entry)}</p>
                </div>
                <span>
                  {getNoteTypeLabel(entry.noteType)} · {formatDateEs(entry.timestamp)}
                </span>
              </li>
            ))}
          </ul>
        </article>
      </section>

      <section className="home-utility-links" aria-label="Accesos utilitarios">
        <Link href="/fuentes">Abrir fuentes ({counts.source})</Link>
        <Link href="/calidad">Dashboard editorial</Link>
        <Link href="/stats">Estadisticas</Link>
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
