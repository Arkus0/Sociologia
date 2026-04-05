import type { SearchEntry, SearchIndex } from "./wiki-types";
import { tokenize } from "./wiki-text";

export const FIELD_WEIGHTS = {
  title: 4,
  concepts: 3,
  authors: 3,
  summary: 2,
  body: 1,
} as const;

export function searchDocuments(
  index: SearchIndex,
  query: string,
  limit = 20,
): SearchEntry[] {
  const queryTokens = tokenize(query);
  if (queryTokens.length === 0) {
    return [];
  }

  const totalDocs = Math.max(index.docCount, 1);
  return index.docs
    .map((doc) => ({
      doc,
      score: scoreDocument(doc, queryTokens, index.docFreq, totalDocs),
    }))
    .filter((entry) => entry.score > 0)
    .sort((left, right) => right.score - left.score)
    .slice(0, limit)
    .map((entry) => entry.doc);
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
