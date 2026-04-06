import { Suspense } from "react";
import Link from "next/link";

import { LegacyQueryRedirector } from "@/components/legacy-query-redirector";
import { loadCatalog, loadQualityReport, loadFacts } from "@/lib/generated-data";
import { getNoteTypeLabel } from "@/lib/wiki-routes";
import { formatDateEs } from "@/lib/wiki-text";
import type { NoteType } from "@/lib/wiki-types";

export default async function HomePage() {
  const catalog = await loadCatalog();
  const canonicalCatalog = catalog.filter((entry) => !entry.isAlias);
  const quality = await loadQualityReport();
  const facts = await loadFacts();
  const counts = countByType(canonicalCatalog.map((entry) => entry.noteType));
  const recent = [...canonicalCatalog]
    .sort((left, right) => right.timestamp.localeCompare(left.timestamp))
    .slice(0, 10);

  const articleOfTheWeek = pickArticleOfTheWeek(canonicalCatalog);

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
            <p>{articleOfTheWeek.preview}</p>
            <Link href={articleOfTheWeek.route} className="article-of-the-week__cta">
              Leer articulo →
            </Link>
          </article>
        ) : null}

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
              <Link href="/grafo">Grafo de conocimiento</Link>
            </li>
            <li>
              <Link href="/stats">Estadisticas</Link>
            </li>
            <li>
              <Link href="/calidad">Calidad editorial</Link>
            </li>
            <li>
              <Link href="/aleatoria">🎲 Articulo aleatorio</Link>
            </li>
          </ul>
        </article>

        {facts.length > 0 ? (
          <article className="portal-card portal-card--wide sabias-que">
            <h2>¿Sabias que...?</h2>
            <ul className="sabias-que__list">
              {pickWeeklyFacts(facts, 4).map((fact, i) => (
                <li key={i} className="sabias-que__item">
                  <p>{fact.text}</p>
                  <Link href={fact.articleRoute}>
                    {fact.articleTitle} →
                  </Link>
                </li>
              ))}
            </ul>
          </article>
        ) : null}

        <article className="portal-card subscribe-card">
          <h2>📬 Suscribete</h2>
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

        <article className="portal-card">
          <h2>Control editorial</h2>
          <ul className="portal-card__list">
            <li>
              <span>Incidencias detectadas</span>
              <span>{quality.summary.issues}</span>
            </li>
            <li>
              <span>Referencias rotas</span>
              <span>{quality.summary.byKind.broken_reference ?? 0}</span>
            </li>
            <li>
              <span>Referencias ambiguas</span>
              <span>{quality.summary.byKind.ambiguous_reference ?? 0}</span>
            </li>
            <li>
              <span>Previews breves</span>
              <span>{quality.summary.byKind.thin_preview ?? 0}</span>
            </li>
          </ul>
          <p style={{ marginTop: "0.9rem" }}>
            <Link href="/calidad">Abrir dashboard editorial</Link>
          </p>
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

/** ISO week key: "2026-W15" — changes every Monday. */
function isoWeekKey(): string {
  const now = new Date();
  const jan4 = new Date(now.getFullYear(), 0, 4);
  const start = new Date(jan4.getTime() - ((jan4.getDay() || 7) - 1) * 86_400_000);
  const week = Math.ceil(((now.getTime() - start.getTime()) / 86_400_000 + 1) / 7);
  return `${now.getFullYear()}-W${String(week).padStart(2, "0")}`;
}

function hashString(s: string): number {
  let h = 0;
  for (const ch of s) h = (h * 31 + ch.charCodeAt(0)) >>> 0;
  return h;
}

function pickArticleOfTheWeek(catalog: Awaited<ReturnType<typeof loadCatalog>>) {
  const candidates = catalog.filter(
    (entry) =>
      (entry.noteType === "concept" || entry.noteType === "author") &&
      !entry.isAlias &&
      entry.preview.trim().length > 50,
  );
  if (candidates.length === 0) return null;
  return candidates[hashString(isoWeekKey()) % candidates.length] ?? candidates[0];
}

function pickWeeklyFacts(facts: Awaited<ReturnType<typeof loadFacts>>, count: number) {
  if (facts.length <= count) return facts;
  const start = hashString(isoWeekKey()) % facts.length;
  const result = [];
  for (let i = 0; i < count; i++) {
    result.push(facts[(start + i) % facts.length]);
  }
  return result;
}
