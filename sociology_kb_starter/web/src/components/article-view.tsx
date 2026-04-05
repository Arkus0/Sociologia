import Link from "next/link";

import { formatDateEs } from "@/lib/wiki-text";
import { NOTE_TYPE_LABELS } from "@/lib/wiki-routes";
import type { ArticlePayload } from "@/lib/wiki-types";

export function ArticleView({ article }: { article: ArticlePayload }) {
  return (
    <article className="article-page">
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
          <p className="article-summary">{article.preview}</p>
          <p className="article-timestamp">
            Ultima actualizacion: {formatDateEs(article.timestamp)}
          </p>
        </div>
      </header>

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
