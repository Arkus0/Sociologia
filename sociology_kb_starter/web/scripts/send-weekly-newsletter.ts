/**
 * send-weekly-newsletter.ts
 *
 * Reads the generated catalog and facts, picks the article-of-the-week
 * and weekly facts, and sends a newsletter email via the Buttondown API.
 *
 * Usage: BUTTONDOWN_API_KEY=xxx tsx scripts/send-weekly-newsletter.ts
 *        (also: JOTAPEDIA_BASE_URL defaults to https://jotapedia.vercel.app)
 */

import { readFile } from "node:fs/promises";
import path from "node:path";

import {
  getEditorialTeaser,
  isoWeekKey,
  pickArticleOfTheWeek,
  pickWeeklyFacts,
} from "../src/lib/editorial";
import type { CatalogEntry, FactCard } from "../src/lib/wiki-types";

function buildEmailHtml(
  base: string,
  article: CatalogEntry | null,
  facts: FactCard[],
  recent: CatalogEntry[],
): string {
  const week = isoWeekKey();

  let html =
    '<div style="font-family: Georgia, serif; max-width: 600px; margin: 0 auto; color: #202122;">';
  html += `<h1 style="font-size: 24px; border-bottom: 2px solid #f97316; padding-bottom: 8px;">Jotapedia - Semana ${week}</h1>`;

  if (article) {
    html += '<h2 style="margin-top: 24px;">Articulo de la semana</h2>';
    html += `<h3><a href="${base}${article.route}" style="color: #0645ad;">${article.title}</a></h3>`;
    html += `<p style="color: #54595d; line-height: 1.6;">${getEditorialTeaser(article)}</p>`;
  }

  if (facts.length > 0) {
    html += '<h2 style="margin-top: 24px;">¿Sabias que...?</h2>';
    html += '<ul style="padding-left: 20px;">';
    for (const fact of facts) {
      html += `<li style="margin-bottom: 10px;">${fact.text} - <a href="${base}${fact.articleRoute}" style="color: #0645ad;">${fact.articleTitle}</a></li>`;
    }
    html += "</ul>";
  }

  if (recent.length > 0) {
    html += '<h2 style="margin-top: 24px;">Novedades recientes</h2>';
    html += '<ul style="padding-left: 20px;">';
    for (const entry of recent) {
      html += `<li style="margin-bottom: 6px;"><a href="${base}${entry.route}" style="color: #0645ad;">${entry.title}</a></li>`;
    }
    html += "</ul>";
  }

  html += '<hr style="margin-top: 32px; border: none; border-top: 1px solid #c8ccd1;" />';
  html += `<p style="font-size: 13px; color: #54595d;">Explora la enciclopedia completa en <a href="${base}" style="color: #0645ad;">${base}</a></p>`;
  html += "</div>";

  return html;
}

async function main() {
  const apiKey = process.env.BUTTONDOWN_API_KEY;
  if (!apiKey) {
    console.error("Missing BUTTONDOWN_API_KEY env var");
    process.exit(1);
  }

  const base = (
    process.env.JOTAPEDIA_BASE_URL ?? "https://jotapedia.vercel.app"
  ).replace(/\/$/, "");

  const generatedDir = path.join(process.cwd(), ".generated");

  const catalog: CatalogEntry[] = JSON.parse(
    await readFile(path.join(generatedDir, "catalog.json"), "utf-8"),
  );
  const facts: FactCard[] = JSON.parse(
    await readFile(path.join(generatedDir, "facts.json"), "utf-8"),
  );

  const article = pickArticleOfTheWeek(catalog);
  const weeklyFacts = pickWeeklyFacts(facts, 4);
  const recent = [...catalog]
    .filter((entry) => !entry.isAlias)
    .sort((left, right) => right.timestamp.localeCompare(left.timestamp))
    .slice(0, 5);

  const week = isoWeekKey();
  const subject = article
    ? `Jotapedia ${week}: ${article.title}`
    : `Jotapedia ${week}: Novedades de la semana`;

  const body = buildEmailHtml(base, article, weeklyFacts, recent);

  console.log(`Sending newsletter: "${subject}"`);

  const response = await fetch("https://api.buttondown.com/v1/emails", {
    method: "POST",
    headers: {
      Authorization: `Token ${apiKey}`,
      "Content-Type": "application/json",
      "X-Buttondown-Live-Dangerously": "true",
    },
    body: JSON.stringify({
      subject,
      body,
      status: "about_to_send",
    }),
  });

  if (!response.ok) {
    const text = await response.text();
    console.error(`Buttondown API error ${response.status}: ${text}`);
    process.exit(1);
  }

  const result = await response.json();
  console.log(`Newsletter sent! ID: ${result.id}`);
}

main();
