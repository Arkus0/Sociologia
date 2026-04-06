import Link from "next/link";

import { getEditorialTeaser } from "@/lib/editorial";
import { formatDateEs } from "@/lib/wiki-text";
import { NOTE_TYPE_LABELS } from "@/lib/wiki-routes";
import type { ArticlePayload } from "@/lib/wiki-types";
import { ReadingProgress } from "./reading-progress";
import { ShareBar } from "./share-bar";
import { ReportErrorButton } from "./report-error-button";

export function ArticleView({ article }: { article: ArticlePayload }) {
  const readingMinutes = Math.max(1, Math.round(article.wordCount / 200));

  return (
    <article className="article-page">
      <ReadingProgress />
      <nav className="breadcrumbs" aria-label="Migas de pan">
        <ol>
          {article.breadcrumbs.map((item) => (
            <li key={`${item.label}-${item.href ?? "current"}`}>
              {item.href ? <Link href={item.href}>{item.label}</Link> : item.label}
            </li>
          ))}
        </ol>
      </nav>

      <header className="article-header">
        <div className="article-header__main">
          <p className="article-kicker">{NOTE_TYPE_LABELS[article.noteType]}</p>
          <h1>{article.title}</h1>
          <p className="article-summary">{getEditorialTeaser(article)}</p>
          <p className="article-timestamp">
            Ultima actualizacion: {formatDateEs(article.timestamp)}
            {" · "}
            <span className="article-reading-time">{readingMinutes} min de lectura</span>
          </p>
          <div
            style={{ display: "flex", alignItems: "start", gap: "0.75rem", flexWrap: "wrap" }}
          >
            <ShareBar title={article.title} path={article.route} />
            <ReportErrorButton title={article.title} route={article.route} />
          </div>
        </div>
      </header>

      {article.isAlias && article.canonicalEntry ? (
        <section className="article-banner article-banner--alias">
          <p>
            Esta pagina actua como alias historico. La entrada canonica es{" "}
            <Link href={article.canonicalEntry.route}>{article.canonicalEntry.title}</Link>.
          </p>
        </section>
      ) : null}

      {article.aliases.length > 0 && !article.isAlias ? (
        <section className="article-banner">
          <p>
            Tambien puedes encontrar esta entrada como:{" "}
            {article.aliases.map((alias, index) => (
              <span key={alias}>
                {index > 0 ? ", " : null}
                <strong>{alias}</strong>
              </span>
            ))}
            .
          </p>
        </section>
      ) : null}

      {article.quickPoints && article.quickPoints.length > 0 ? (
        <section className="article-editorial article-editorial--quick">
          <h2>En 30 segundos</h2>
          <ul>
            {article.quickPoints.map((point) => (
              <li key={point}>{point}</li>
            ))}
          </ul>
        </section>
      ) : null}

      {article.whyNow || article.everydayExample ? (
        <section className="article-editorial-grid">
          {article.whyNow ? (
            <article className="article-editorial">
              <h2>Por que importa hoy</h2>
              <p>{article.whyNow}</p>
            </article>
          ) : null}
          {article.everydayExample ? (
            <article className="article-editorial">
              <h2>Ejemplo cotidiano</h2>
              <p>{article.everydayExample}</p>
            </article>
          ) : null}
        </section>
      ) : null}

      <div className="article-layout">
        <div className="article-main">
          <div
            className="wiki-article-body"
            dangerouslySetInnerHTML={{ __html: article.html }}
          />
        </div>

        <aside className="article-side">
          {article.infobox.length > 0 ? (
            <section className="infobox">
              <h2>Ficha</h2>
              <dl>
                {article.infobox.map((item) => (
                  <div key={`${item.label}-${item.value}`}>
                    <dt>{item.label}</dt>
                    <dd>
                      {item.href ? <Link href={item.href}>{item.value}</Link> : item.value}
                    </dd>
                  </div>
                ))}
              </dl>
            </section>
          ) : null}

          {article.toc.length > 0 ? (
            <section className="toc">
              <h2>Indice</h2>
              <ol>
                {article.toc.map((entry) => (
                  <li key={entry.id} className={`toc-level-${entry.level}`}>
                    <a href={`#${entry.id}`}>{entry.text}</a>
                  </li>
                ))}
              </ol>
            </section>
          ) : null}

          {article.backlinks.length > 0 ? (
            <section className="backlinks-panel">
              <h2>Que enlaza aqui</h2>
              <ul>
                {article.backlinks.map((link) => (
                  <li key={link.route}>
                    <Link href={link.route}>{link.title}</Link>
                    <span>{NOTE_TYPE_LABELS[link.noteType]}</span>
                  </li>
                ))}
              </ul>
            </section>
          ) : null}
        </aside>
      </div>

      {article.relatedLinks.length > 0 ? (
        <section className="related-panel">
          <h2>Articulos relacionados</h2>
          <ul>
            {article.relatedLinks.map((link) => (
              <li key={link.route}>
                <Link href={link.route}>{link.title}</Link>
                <span>{NOTE_TYPE_LABELS[link.noteType]}</span>
              </li>
            ))}
          </ul>
        </section>
      ) : null}
    </article>
  );
}
