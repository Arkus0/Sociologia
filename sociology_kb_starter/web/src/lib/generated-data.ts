import { promises as fs } from "node:fs";
import path from "node:path";

import { cache } from "react";

import { routeToArticlePayloadPath } from "./wiki-routes";
import type {
  ArticlePayload,
  CatalogEntry,
  FactCard,
  LegacyLookupEntry,
  QualityReport,
  SearchIndex,
} from "./wiki-types";

const GENERATED_ROOT = path.join(process.cwd(), ".generated");

export const loadCatalog = cache(async (): Promise<CatalogEntry[]> => {
  return readJson<CatalogEntry[]>("catalog.json");
});

export const loadSearchIndex = cache(async (): Promise<SearchIndex> => {
  return readJson<SearchIndex>("search-index.json");
});

export const loadLegacyMap = cache(async (): Promise<LegacyLookupEntry[]> => {
  return readJson<LegacyLookupEntry[]>("legacy-map.json");
});

export const loadQualityReport = cache(async (): Promise<QualityReport> => {
  return readJson<QualityReport>("quality-report.json");
});

export const loadFacts = cache(async (): Promise<FactCard[]> => {
  return readJson<FactCard[]>("facts.json");
});

export async function loadArticlePayload(
  route: string,
): Promise<ArticlePayload | null> {
  try {
    return await readJson<ArticlePayload>(routeToArticlePayloadPath(route));
  } catch (error) {
    if ((error as NodeJS.ErrnoException).code === "ENOENT") {
      return null;
    }
    throw error;
  }
}

async function readJson<T>(relativePath: string): Promise<T> {
  const filePath = path.join(GENERATED_ROOT, relativePath);
  const raw = await fs.readFile(filePath, "utf8");
  return JSON.parse(raw) as T;
}
