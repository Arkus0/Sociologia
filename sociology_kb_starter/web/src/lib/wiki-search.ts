import type { NoteType, SearchEntry, SearchIndex } from "./wiki-types";
import { normalizeText, tokenize } from "./wiki-text";

export const FIELD_WEIGHTS = {
  title: 4,
  aliases: 3,
  concepts: 3,
  authors: 3,
  summary: 2,
  body: 1,
} as const;

interface SearchOptions {
  noteTypes?: NoteType[];
  course?: string;
  semester?: string;
}

export function searchDocuments(
  index: SearchIndex,
  query: string,
  limit = 20,
  options: SearchOptions = {},
): SearchEntry[] {
  const queryTokens = tokenize(query);
  if (queryTokens.length === 0) {
    return [];
  }

  const docs = filterDocs(index.docs, options);
  const totalDocs = Math.max(docs.length, 1);

  return docs
    .map((doc) => ({
      doc,
      score: scoreDocument(doc, queryTokens, index.docFreq, totalDocs),
    }))
    .filter((entry) => entry.score > 0)
    .sort((left, right) => right.score - left.score)
    .slice(0, limit)
    .map((entry) => entry.doc);
}

export function suggestDocuments(
  index: SearchIndex,
  query: string,
  limit = 8,
  options: SearchOptions = {},
): SearchEntry[] {
  const normalizedQuery = normalizeText(query).trim();
  if (!normalizedQuery) {
    return [];
  }

  return filterDocs(index.docs, options)
    .map((doc) => ({
      doc,
      score: scoreSuggestion(doc, normalizedQuery),
    }))
    .filter((entry) => entry.score > 0)
    .sort((left, right) => right.score - left.score)
    .slice(0, limit)
    .map((entry) => entry.doc);
}

function filterDocs(docs: SearchEntry[], options: SearchOptions): SearchEntry[] {
  const allowed = options.noteTypes?.length ? new Set(options.noteTypes) : null;

  return docs.filter((doc) => {
    if (allowed && !allowed.has(doc.noteType)) {
      return false;
    }

    if (options.course && doc.course !== options.course) {
      return false;
    }

    if (options.semester && doc.semester !== options.semester) {
      return false;
    }

    return true;
  });
}

function scoreDocument(
  doc: SearchEntry,
  queryTokens: string[],
  docFreq: Record<string, number>,
  totalDocs: number,
): number {
  let score = 0;

  for (const token of queryTokens) {
    const idf = Math.log((1 + totalDocs) / (1 + (docFreq[token] ?? 0))) + 1;

    for (const [field, weight] of Object.entries(FIELD_WEIGHTS)) {
      const tf = doc.fieldTokens[field as keyof typeof FIELD_WEIGHTS][token] ?? 0;
      if (tf > 0) {
        score += weight * (1 + Math.log(tf)) * idf;
      }
    }
  }

  return score;
}

function scoreSuggestion(doc: SearchEntry, normalizedQuery: string): number {
  const exactTitle = normalizeText(doc.title);
  const aliasText = doc.aliases.map((alias) => normalizeText(alias));
  const preview = normalizeText(doc.preview);
  const context = normalizeText(
    [doc.title, ...doc.aliases, doc.preview, doc.course, doc.semester]
      .filter(Boolean)
      .join(" "),
  );

  if (exactTitle === normalizedQuery || aliasText.includes(normalizedQuery)) {
    return 120;
  }

  if (exactTitle.startsWith(normalizedQuery)) {
    return 96;
  }

  if (aliasText.some((alias) => alias.startsWith(normalizedQuery))) {
    return 90;
  }

  if (exactTitle.includes(normalizedQuery)) {
    return 72;
  }

  if (aliasText.some((alias) => alias.includes(normalizedQuery))) {
    return 64;
  }

  if (preview.includes(normalizedQuery) || context.includes(normalizedQuery)) {
    return 36;
  }

  const bestDistance = Math.min(
    distanceToTerms(normalizedQuery, exactTitle),
    ...aliasText.map((alias) => distanceToTerms(normalizedQuery, alias)),
  );

  if (Number.isFinite(bestDistance) && bestDistance <= 2) {
    return 24 - bestDistance * 6;
  }

  return 0;
}

function distanceToTerms(query: string, value: string): number {
  const queryTokens = tokenize(query);
  const valueTokens = tokenize(value);

  if (queryTokens.length === 0 || valueTokens.length === 0) {
    return Number.POSITIVE_INFINITY;
  }

  let best = Number.POSITIVE_INFINITY;

  for (const queryToken of queryTokens) {
    for (const valueToken of valueTokens) {
      if (Math.abs(queryToken.length - valueToken.length) > 2) {
        continue;
      }

      best = Math.min(best, levenshteinDistance(queryToken, valueToken));
    }
  }

  return best;
}

function levenshteinDistance(left: string, right: string): number {
  if (left === right) {
    return 0;
  }

  if (left.length === 0) {
    return right.length;
  }

  if (right.length === 0) {
    return left.length;
  }

  const previous = Array.from({ length: right.length + 1 }, (_, index) => index);
  const current = new Array<number>(right.length + 1);

  for (let i = 0; i < left.length; i += 1) {
    current[0] = i + 1;

    for (let j = 0; j < right.length; j += 1) {
      const cost = left[i] === right[j] ? 0 : 1;
      current[j + 1] = Math.min(
        current[j] + 1,
        previous[j + 1] + 1,
        previous[j] + cost,
      );
    }

    for (let j = 0; j < previous.length; j += 1) {
      previous[j] = current[j];
    }
  }

  return previous[right.length];
}
