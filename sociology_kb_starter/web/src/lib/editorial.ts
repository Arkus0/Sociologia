import type { CatalogEntry, FactCard, SearchEntry } from "./wiki-types";

const EDITORIAL_CANDIDATE_TYPES = new Set(["concept", "author"]);

export const EDITORIAL_PILOT_SLUGS = [
  "sociologia",
  "perspectiva-sociologica",
  "socializacion",
  "lenguaje",
  "norma-social",
  "desviacion-social",
  "genero",
  "identidad-social",
  "hecho-social",
  "anomia",
  "poder",
  "burocracia",
  "max-weber",
  "emile-durkheim",
  "karl-marx",
  "erving-goffman",
  "pierre-bourdieu",
  "george-herbert-mead",
  "peter-berger",
  "thomas-luckmann",
] as const;

type EntryWithEditorialTeaser = Pick<CatalogEntry, "preview" | "hook">;
type EntryWithSelectionData = Pick<
  CatalogEntry,
  "slug" | "noteType" | "isAlias" | "preview" | "hook"
>;
type SearchLikeEntry = Pick<SearchEntry, "preview" | "hook">;

export function getEditorialTeaser(entry: EntryWithEditorialTeaser | SearchLikeEntry): string {
  const hook = entry.hook?.trim();
  if (hook) {
    return hook;
  }
  return entry.preview.trim();
}

export function getFactKindLabel(kind: FactCard["kind"]): string {
  switch (kind) {
    case "hook":
      return "Idea clave";
    case "quick_point":
      return "En 30 segundos";
    case "why_now":
      return "Importa hoy";
    case "example":
      return "Caso cotidiano";
  }
}

export function hashString(value: string): number {
  let hash = 0;
  for (const character of value) {
    hash = (hash * 31 + character.charCodeAt(0)) >>> 0;
  }
  return hash;
}

export function isoWeekKey(now = new Date()): string {
  const jan4 = new Date(now.getFullYear(), 0, 4);
  const start = new Date(
    jan4.getTime() - ((jan4.getDay() || 7) - 1) * 86_400_000,
  );
  const week = Math.ceil(((now.getTime() - start.getTime()) / 86_400_000 + 1) / 7);
  return `${now.getFullYear()}-W${String(week).padStart(2, "0")}`;
}

export function pickArticleOfTheWeek<T extends EntryWithSelectionData>(
  catalog: T[],
  now = new Date(),
): T | null {
  const candidates = catalog.filter(
    (entry) =>
      EDITORIAL_CANDIDATE_TYPES.has(entry.noteType) &&
      !entry.isAlias &&
      getEditorialTeaser(entry).length > 50,
  );
  if (candidates.length === 0) {
    return null;
  }
  return candidates[hashString(isoWeekKey(now)) % candidates.length] ?? candidates[0];
}

export function pickWeeklyFacts<T>(
  facts: T[],
  count: number,
  now = new Date(),
): T[] {
  if (facts.length <= count) {
    return facts;
  }
  const start = hashString(isoWeekKey(now)) % facts.length;
  const result: T[] = [];
  for (let index = 0; index < count; index += 1) {
    result.push(facts[(start + index) % facts.length]);
  }
  return result;
}

export function pickEditorialStarts<T extends EntryWithSelectionData>(
  catalog: T[],
  count = 3,
): T[] {
  const pilotOrder = new Map<string, number>(
    EDITORIAL_PILOT_SLUGS.map((slug, index) => [slug, index]),
  );

  return [...catalog]
    .filter(
      (entry) =>
        !entry.isAlias &&
        EDITORIAL_CANDIDATE_TYPES.has(entry.noteType) &&
        pilotOrder.has(entry.slug) &&
        getEditorialTeaser(entry).length > 40,
    )
    .sort((left, right) => {
      const leftOrder = pilotOrder.get(left.slug) ?? Number.MAX_SAFE_INTEGER;
      const rightOrder = pilotOrder.get(right.slug) ?? Number.MAX_SAFE_INTEGER;
      return leftOrder - rightOrder;
    })
    .slice(0, count);
}
