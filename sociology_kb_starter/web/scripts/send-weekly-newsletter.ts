/**
 * send-weekly-newsletter.ts
 *
 * Reads the generated catalog and facts, picks the article-of-the-week
 * and weekly facts (same algorithm as the home page), and sends
 * a newsletter email via the Buttondown API.
 *
 * Usage:  BUTTONDOWN_API_KEY=xxx tsx scripts/send-weekly-newsletter.ts
 *         (also: JOTAPEDIA_BASE_URL defaults to https://jotapedia.vercel.app)
 */

import { readFile } from "node:fs/promises";
import path from "node:path";

interface CatalogEntry {
  title: string;
  route: string;
  noteType: string;
  preview: string;
  timestamp: string;
  isAlias?: boolean;
}

interface FactCard {
  text: string;
  articleTitle: string;
  articleRoute: string;
}

/* ── helpers (mirrored from page.tsx) ── */

function isoWeekKey(): string {
  const now = new Date();
  const jan4 = new Date(now.getFullYear(), 0, 4);
  const start = new Date(
    jan4.getTime() - ((jan4.getDay() || 7) - 1) * 86_400_000,
  );
  const week = Math.ceil(
    ((now.getTime() - start.getTime()) / 86_400_000 + 1) / 7,
  );
  return `${now.getFullYear()}-W${String(week).padStart(2, "0")}`;
}

function hashString(s: string): number {
  let h = 0;
  for (const ch of s) h = (h * 31 + ch.charCodeAt(0)) >>> 0;
  return h;
}

function pickArticleOfTheWeek(catalog: CatalogEntry[]) {
  const candidates = catalog.filter(
    (e) =>
      (e.noteType === "concept" || e.noteType === "author") &&
      !e.isAlias &&
      e.preview.trim().length > 50,
  );
  if (candidates.length === 0) return null;
  return candidates[hashString(isoWeekKey()) % candidates.length] ?? candidates[0];
}

function pickWeeklyFacts(facts: FactCard[], count: number) {
  if (facts.length <= count) return facts;
  const start = hashString(isoWeekKey()) % facts.length;
  const result: FactCard[] = [];
  for (let i = 0; i < count; i++) {
    result.push(facts[(start + i) % facts.length]);
  }
  return result;
}

/* ── build email HTML ── */

function buildEmailHtml(
  base: string,
  article: CatalogEntry | null,
  facts: FactCard[],
  recent: CatalogEntry[],
): string {
  const week = isoWeekKey();

  let html = `<div style="font-family: Georgia, serif; max-width: 600px; margin: 0 auto; color: #202122;">`;
  html += `<h1 style="font-size: 24px; border-bottom: 2px solid #f97316; padding-bottom: 8px;">📚 Jotapedia — Semana ${week}</h1>`;

  if (article) {
    html += `<h2 style="margin-top: 24px;">Articulo de la semana</h2>`;
    html += `<h3><a href="${base}${article.route}" style="color: #0645ad;">${article.title}</a></h3>`;
    html += `<p style="color: #54595d; line-height: 1.6;">${article.preview}</p>`;
  }

  if (facts.length > 0) {
    html += `<h2 style="margin-top: 24px;">¿Sabias que...?</h2>`;
    html += `<ul style="padding-left: 20px;">`;
    for (const f of facts) {
      html += `<li style="margin-bottom: 10px;">${f.text} — <a href="${base}${f.articleRoute}" style="color: #0645ad;">${f.articleTitle}</a></li>`;
    }
    html += `</ul>`;
  }

  if (recent.length > 0) {
    html += `<h2 style="margin-top: 24px;">Novedades recientes</h2>`;
    html += `<ul style="padding-left: 20px;">`;
    for (const entry of recent) {
      html += `<li style="margin-bottom: 6px;"><a href="${base}${entry.route}" style="color: #0645ad;">${entry.title}</a></li>`;
    }
    html += `</ul>`;
  }

  html += `<hr style="margin-top: 32px; border: none; border-top: 1px solid #c8ccd1;" />`;
  html += `<p style="font-size: 13px; color: #54595d;">Explora la enciclopedia completa en <a href="${base}" style="color: #0645ad;">${base}</a></p>`;
  html += `</div>`;

  return html;
}

/* ── main ── */

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
    .sort((a, b) => b.timestamp.localeCompare(a.timestamp))
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
