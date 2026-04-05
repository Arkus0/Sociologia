import { promises as fs } from "node:fs";
import path from "node:path";

import matter from "gray-matter";
import MarkdownIt from "markdown-it";

import {
  buildLegacySourceRoute,
  buildNoteRoute,
  buildSourceBreadcrumbs,
  getCategoryRouteForType,
  getNoteTypeLabel,
  inferNoteTypeFromRelativePath,
  matchesLooseSlug,
  normalizeRelativePath,
  routeToArticlePayloadPath,
  titleFromReference,
} from "./wiki-routes";
import {
  escapeMarkdownLabel,
  extractPreview,
  extractSummary,
  extractWikiReferences,
  formatDateEs,
  humanizeSlug,
  slugifyText,
  stripMarkdown,
  stripTitleHeading,
  tokenize,
} from "./wiki-text";
import type {
  ArticlePayload,
  CatalogEntry,
  FrontmatterSubset,
  InfoboxItem,
  LegacyLookupEntry,
  LinkResolution,
  NoteType,
  RelatedLink,
  SearchEntry,
  SearchFieldTokenMap,
  SearchIndex,
  TocEntry,
  WikiDocument,
} from "./wiki-types";

interface LinkRegistry {
  byRelativePath: Map<string, WikiDocument>;
  bySlug: Map<string, WikiDocument[]>;
  byId: Map<string, WikiDocument[]>;
}

interface RenderEnv {
  headingIds: Record<number, string>;
}

interface BuildWikiArtifactsOptions {
  wikiRoot: string;
  outputRoot: string;
  publicRoot?: string;
}

const WIKI_SECTIONS = ["concepts", "authors", "courses", "sources"] as const;
const NOTE_PRIORITY: NoteType[] = ["concept", "author", "course"];

export async function buildWikiArtifacts(
  options: BuildWikiArtifactsOptions,
): Promise<void> {
  const documents = await collectWikiDocuments(options.wikiRoot);
  const registry = buildLinkRegistry(documents);
  const catalog = documents.map(toCatalogEntry);
  const articles = documents.map((document) =>
    buildArticlePayload(document, registry),
  );
  const searchIndex = buildSearchIndex(documents);
  const legacyMap = buildLegacyMap(documents);

  await fs.rm(options.outputRoot, { recursive: true, force: true });
  await fs.mkdir(options.outputRoot, { recursive: true });

  await writeJson(path.join(options.outputRoot, "catalog.json"), catalog);
  await writeJson(path.join(options.outputRoot, "search-index.json"), searchIndex);
  await writeJson(path.join(options.outputRoot, "legacy-map.json"), legacyMap);

  for (const article of articles) {
    const payloadPath = path.join(
      options.outputRoot,
      routeToArticlePayloadPath(article.route),
    );
    await writeJson(payloadPath, article);
  }

  if (options.publicRoot) {
    await fs.rm(options.publicRoot, { recursive: true, force: true });
    await fs.mkdir(options.publicRoot, { recursive: true });
    await writeJson(path.join(options.publicRoot, "search-index.json"), searchIndex);
  }
}

export async function collectWikiDocuments(
  wikiRoot: string,
): Promise<WikiDocument[]> {
  const files = await collectMarkdownFiles(wikiRoot);
  const documents = await Promise.all(
    files.map((filePath) => readWikiDocument(filePath, wikiRoot)),
  );

  return documents.sort((left, right) =>
    left.title.localeCompare(right.title, "es"),
  );
}

export function buildSearchIndex(documents: WikiDocument[]): SearchIndex {
  const docFreq = new Map<string, number>();
  const docs = documents.map<SearchEntry>((document) => {
    const fieldTokens = buildSearchFieldTokens(document);
    const mergedTokens = new Set<string>();

    for (const field of Object.values(fieldTokens)) {
      for (const token of Object.keys(field)) {
        mergedTokens.add(token);
      }
    }

    for (const token of mergedTokens) {
      docFreq.set(token, (docFreq.get(token) ?? 0) + 1);
    }

    return {
      route: document.route,
      title: document.title,
      noteType: document.noteType,
      preview: document.preview,
      semester: document.semester,
      course: document.course,
      fieldTokens,
    };
  });

  return {
    docCount: docs.length,
    docFreq: Object.fromEntries(docFreq.entries()),
    docs,
  };
}

export function buildLegacyMap(documents: WikiDocument[]): LegacyLookupEntry[] {
  const grouped = new Map<string, string[]>();

  for (const document of documents) {
    if (document.noteType !== "source") {
      continue;
    }
    appendMapValue(grouped, document.id, document.route);
  }

  return [...grouped.entries()]
    .map<LegacyLookupEntry>(([legacyId, routes]) => {
      const uniqueRoutes = [...new Set(routes)].sort((left, right) =>
        left.localeCompare(right, "es"),
      );
      if (uniqueRoutes.length === 1) {
        return {
          legacyType: "source",
          legacyId,
          status: "exact",
          targetRoute: uniqueRoutes[0],
        };
      }

      return {
        legacyType: "source",
        legacyId,
        status: "ambiguous",
        targetRoutes: uniqueRoutes,
      };
    })
    .sort((left, right) => left.legacyId.localeCompare(right.legacyId, "es"));
}

export function resolveReference(
  reference: string,
  registry: LinkRegistry,
): LinkResolution {
  const trimmed = reference.trim();
  if (!trimmed) {
    return {
      status: "missing",
      title: "Enlace sin destino",
    };
  }

  const normalizedPath = normalizeRelativePath(trimmed);
  const pathWithExtension = normalizedPath.endsWith(".md")
    ? normalizedPath
    : `${normalizedPath}.md`;

  const directPathMatch = registry.byRelativePath.get(pathWithExtension);
  if (directPathMatch) {
    return {
      status: "exact",
      title: directPathMatch.title,
      route: directPathMatch.route,
      noteType: directPathMatch.noteType,
    };
  }

  const slugCandidate = path.basename(normalizedPath.replace(/\.md$/i, ""));
  const candidates = dedupeDocuments([
    ...(registry.byId.get(trimmed) ?? []),
    ...(registry.byId.get(slugCandidate) ?? []),
    ...(registry.bySlug.get(trimmed) ?? []),
    ...(registry.bySlug.get(slugCandidate) ?? []),
    ...findLooseMatches(trimmed, registry.byId),
    ...findLooseMatches(slugCandidate, registry.bySlug),
  ]);

  if (candidates.length === 0) {
    return {
      status: "missing",
      title: titleFromReference(trimmed),
    };
  }

  if (candidates.length === 1) {
    const [match] = candidates;
    return {
      status: "exact",
      title: match.title,
      route: match.route,
      noteType: match.noteType,
    };
  }

  const prioritized = pickPreferredCandidate(candidates);
  if (prioritized) {
    return {
      status: "exact",
      title: prioritized.title,
      route: prioritized.route,
      noteType: prioritized.noteType,
    };
  }

  return {
    status: "ambiguous",
    title: titleFromReference(trimmed),
    route: buildLegacySourceRoute(slugCandidate),
    noteType: "source",
  };
}

export function renderMarkdownDocument(
  markdown: string,
  registry: LinkRegistry,
): { html: string; toc: TocEntry[] } {
  const md = new MarkdownIt({
    html: false,
    linkify: true,
  });

  const defaultHeadingOpen =
    md.renderer.rules.heading_open ??
    ((tokens, idx, options, _env, self) => self.renderToken(tokens, idx, options));

  md.renderer.rules.heading_open = (tokens, idx, options, env, self) => {
    const headingIds = (env as RenderEnv).headingIds;
    const headingId = headingIds[idx];
    if (headingId) {
      tokens[idx].attrSet("id", headingId);
    }
    return defaultHeadingOpen(tokens, idx, options, env, self);
  };

  const processedMarkdown = rewriteWikiLinks(markdown, registry);
  const env: RenderEnv = { headingIds: {} };
  const tokens = md.parse(processedMarkdown, env);
  const slugCounts = new Map<string, number>();
  const toc: TocEntry[] = [];

  for (let index = 0; index < tokens.length; index += 1) {
    const token = tokens[index];
    if (token.type !== "heading_open") {
      continue;
    }

    const level = Number(token.tag.slice(1));
    const inlineToken = tokens[index + 1];
    const title = inlineToken?.content?.trim() ?? "";
    const slug = createUniqueSlug(title, slugCounts);

    env.headingIds[index] = slug;

    if (level === 2 || level === 3) {
      toc.push({
        id: slug,
        text: title,
        level,
      });
    }
  }

  return {
    html: md.renderer.render(tokens, md.options, env),
    toc,
  };
}

export function buildArticlePayload(
  document: WikiDocument,
  registry: LinkRegistry,
): ArticlePayload {
  const courseRoute = document.course
    ? resolveReference(slugifyText(document.course), registry).route
    : undefined;
  const { html, toc } = renderMarkdownDocument(document.body, registry);

  return {
    id: document.id,
    title: document.title,
    slug: document.slug,
    noteType: document.noteType,
    route: document.route,
    routeSegments: document.routeSegments,
    html,
    preview: document.preview,
    timestamp: document.timestamp,
    semester: document.semester,
    course: document.course,
    toc,
    breadcrumbs:
      document.noteType === "source"
        ? buildSourceBreadcrumbs({
            title: document.title,
            semester: document.semester,
            course: document.course,
            courseRoute,
          })
        : [
            { label: "Portada", href: "/" },
            {
              label: categoryLabel(document.noteType),
              href: getCategoryRouteForType(document.noteType),
            },
            { label: document.title },
          ],
    infobox: buildInfobox(document, registry),
    relatedLinks: buildRelatedLinks(document, registry),
    frontmatterSubset: document.frontmatterSubset,
  };
}

async function collectMarkdownFiles(root: string): Promise<string[]> {
  const files: string[] = [];
  for (const section of WIKI_SECTIONS) {
    await walkMarkdownFiles(path.join(root, section), files);
  }
  return files;
}

async function walkMarkdownFiles(directory: string, results: string[]): Promise<void> {
  const entries = await fs.readdir(directory, { withFileTypes: true });

  for (const entry of entries) {
    if (entry.name.startsWith(".")) {
      continue;
    }

    const fullPath = path.join(directory, entry.name);
    if (entry.isDirectory()) {
      await walkMarkdownFiles(fullPath, results);
      continue;
    }

    if (entry.isFile() && entry.name.toLowerCase().endsWith(".md")) {
      results.push(fullPath);
    }
  }
}

async function readWikiDocument(
  absolutePath: string,
  wikiRoot: string,
): Promise<WikiDocument> {
  const raw = await fs.readFile(absolutePath, "utf8");
  const { data, content } = matter(raw);
  const stat = await fs.stat(absolutePath);

  const relativePath = normalizeRelativePath(path.relative(wikiRoot, absolutePath));
  const slug = path.basename(absolutePath, ".md");
  const noteType = normalizeNoteType(
    asString(data.note_type) ?? inferNoteTypeFromRelativePath(relativePath),
  );
  const title = asString(data.title) ?? humanizeSlug(slug);
  const body = stripTitleHeading(content, title);
  const timestamp = normalizeTimestamp(data.updated_at ?? data.compiled_at, stat.mtime);

  const semester = asString(data.semester);
  const course = asString(data.course);
  const sourcePath = asString(data.source_path);
  const reviewed = typeof data.reviewed === "boolean" ? data.reviewed : undefined;
  const concepts = normalizeStringArray(data.concepts);
  const authors = normalizeStringArray(data.authors);
  const relatedConcepts = normalizeStringArray(data.related_concepts);
  const sourceNotes = normalizeStringArray(data.source_notes);
  const tags = normalizeStringArray(data.tags);
  const id = asString(data.id) ?? slug;

  const frontmatterSubset: FrontmatterSubset = {};
  if (semester) {
    frontmatterSubset.semester = semester;
  }
  if (course) {
    frontmatterSubset.course = course;
  }
  if (sourcePath) {
    frontmatterSubset.source_path = sourcePath;
  }
  if (typeof reviewed === "boolean") {
    frontmatterSubset.reviewed = reviewed;
  }
  if (asString(data.updated_at)) {
    frontmatterSubset.updated_at = asString(data.updated_at);
  }
  if (asString(data.compiled_at)) {
    frontmatterSubset.compiled_at = asString(data.compiled_at);
  }

  const route = buildNoteRoute({ noteType, slug, relativePath });

  return {
    id,
    slug,
    title,
    noteType,
    relativePath,
    route,
    routeSegments: route.replace(/^\/+/, "").split("/"),
    body,
    preview: extractPreview(body),
    timestamp,
    semester,
    course,
    sourcePath,
    reviewed,
    concepts,
    authors,
    relatedConcepts,
    sourceNotes,
    tags,
    outgoingLinks: extractWikiReferences(body),
    frontmatterSubset,
    frontmatter: data,
  };
}

function buildLinkRegistry(documents: WikiDocument[]): LinkRegistry {
  const byRelativePath = new Map<string, WikiDocument>();
  const bySlug = new Map<string, WikiDocument[]>();
  const byId = new Map<string, WikiDocument[]>();

  for (const document of documents) {
    byRelativePath.set(normalizeRelativePath(document.relativePath), document);
    appendMapValue(bySlug, document.slug, document);
    appendMapValue(byId, document.id, document);
  }

  return { byRelativePath, bySlug, byId };
}

function buildInfobox(
  document: WikiDocument,
  registry: LinkRegistry,
): InfoboxItem[] {
  const items: InfoboxItem[] = [
    {
      label: "Tipo",
      value: getNoteTypeLabel(document.noteType),
    },
    {
      label: "Actualizado",
      value: formatDateEs(document.timestamp),
    },
  ];

  if (document.semester) {
    items.push({ label: "Semestre", value: document.semester });
  }

  if (document.course) {
    const courseMatch = resolveReference(slugifyText(document.course), registry);
    items.push({
      label: "Curso",
      value: document.course,
      href: courseMatch.status === "exact" ? courseMatch.route : undefined,
    });
  }

  if (document.sourcePath) {
    items.push({
      label: "Archivo fuente",
      value: path.basename(document.sourcePath),
    });
  }

  if (typeof document.reviewed === "boolean") {
    items.push({
      label: "Revisado",
      value: document.reviewed ? "Si" : "No",
    });
  }

  if (document.relatedConcepts.length > 0) {
    items.push({
      label: "Relacionados",
      value: String(document.relatedConcepts.length),
    });
  }

  if (document.sourceNotes.length > 0) {
    items.push({
      label: "Notas fuente",
      value: String(document.sourceNotes.length),
    });
  }

  if (document.authors.length > 0) {
    items.push({
      label: "Autores citados",
      value: String(document.authors.length),
    });
  }

  if (document.concepts.length > 0) {
    items.push({
      label: "Conceptos citados",
      value: String(document.concepts.length),
    });
  }

  return items;
}

function buildRelatedLinks(
  document: WikiDocument,
  registry: LinkRegistry,
  limit = 12,
): RelatedLink[] {
  const seeds = [
    ...document.relatedConcepts,
    ...document.sourceNotes,
    ...document.concepts.map((concept) => slugifyText(concept)),
    ...document.authors.map((author) => slugifyText(author)),
    ...document.outgoingLinks,
  ];

  const relatedLinks: RelatedLink[] = [];
  const seenRoutes = new Set<string>();

  for (const seed of seeds) {
    const match = resolveReference(seed, registry);
    if (match.status === "missing" || !match.route || !match.noteType) {
      continue;
    }
    if (match.route === document.route || seenRoutes.has(match.route)) {
      continue;
    }

    seenRoutes.add(match.route);
    relatedLinks.push({
      title: match.title,
      route: match.route,
      noteType: match.noteType,
    });

    if (relatedLinks.length >= limit) {
      break;
    }
  }

  return relatedLinks;
}

function buildSearchFieldTokens(document: WikiDocument): SearchFieldTokenMap {
  const summary = extractSummary(document.body) || document.preview;
  return {
    title: countTokens(document.title),
    concepts: countTokens(document.concepts.join(" ")),
    authors: countTokens(document.authors.join(" ")),
    summary: countTokens(summary),
    body: countTokens(stripMarkdown(document.body)),
  };
}

function countTokens(value: string): Record<string, number> {
  const counts = new Map<string, number>();

  for (const token of tokenize(value)) {
    counts.set(token, (counts.get(token) ?? 0) + 1);
  }

  return Object.fromEntries(counts.entries());
}

function rewriteWikiLinks(markdown: string, registry: LinkRegistry): string {
  return markdown.replace(/\[\[([^[\]]+)\]\]/g, (_match, rawContent: string) => {
    const [reference, alias] = rawContent.split("|");
    const resolution = resolveReference(reference.trim(), registry);
    const label =
      alias?.trim() ||
      (resolution.status === "missing"
        ? titleFromReference(reference.trim())
        : resolution.title);

    if (resolution.status === "missing" || !resolution.route) {
      return escapeMarkdownLabel(label);
    }

    return `[${escapeMarkdownLabel(label)}](${resolution.route})`;
  });
}

function createUniqueSlug(title: string, counts: Map<string, number>): string {
  const base = slugifyText(title) || "seccion";
  const current = counts.get(base) ?? 0;
  counts.set(base, current + 1);
  return current === 0 ? base : `${base}-${current + 1}`;
}

function toCatalogEntry(document: WikiDocument): CatalogEntry {
  return {
    id: document.id,
    slug: document.slug,
    title: document.title,
    noteType: document.noteType,
    route: document.route,
    routeSegments: document.routeSegments,
    relativePath: document.relativePath,
    preview: document.preview,
    timestamp: document.timestamp,
    semester: document.semester,
    course: document.course,
  };
}

function dedupeDocuments(documents: WikiDocument[]): WikiDocument[] {
  const byRoute = new Map<string, WikiDocument>();
  for (const document of documents) {
    byRoute.set(document.route, document);
  }
  return [...byRoute.values()];
}

function findLooseMatches(
  reference: string,
  registryMap: Map<string, WikiDocument[]>,
): WikiDocument[] {
  const matches: WikiDocument[] = [];

  for (const [candidate, docs] of registryMap.entries()) {
    if (matchesLooseSlug(candidate, reference)) {
      matches.push(...docs);
    }
  }

  return matches;
}

function pickPreferredCandidate(
  candidates: WikiDocument[],
): WikiDocument | undefined {
  for (const noteType of NOTE_PRIORITY) {
    const match = candidates.find((candidate) => candidate.noteType === noteType);
    if (match) {
      return match;
    }
  }

  return undefined;
}

function appendMapValue<T>(map: Map<string, T[]>, key: string, value: T): void {
  map.set(key, [...(map.get(key) ?? []), value]);
}

function normalizeNoteType(value: string): NoteType {
  if (value === "concept" || value === "author" || value === "course" || value === "source") {
    return value;
  }

  throw new Error(`Tipo de nota no soportado: ${value}`);
}

function normalizeStringArray(value: unknown): string[] {
  if (!Array.isArray(value)) {
    return [];
  }

  return value
    .map((item) => asString(item))
    .filter((item): item is string => Boolean(item));
}

function asString(value: unknown): string | undefined {
  if (typeof value !== "string") {
    return undefined;
  }

  const trimmed = value.trim();
  return trimmed.length > 0 ? trimmed : undefined;
}

function normalizeTimestamp(value: unknown, fallbackDate: Date): string {
  if (value instanceof Date && !Number.isNaN(value.getTime())) {
    return value.toISOString();
  }

  if (typeof value === "string" && value.trim()) {
    const parsed = new Date(value);
    if (!Number.isNaN(parsed.getTime())) {
      return parsed.toISOString();
    }
  }

  return fallbackDate.toISOString();
}

async function writeJson(filePath: string, data: unknown): Promise<void> {
  await fs.mkdir(path.dirname(filePath), { recursive: true });
  await fs.writeFile(filePath, JSON.stringify(data), "utf8");
}

function categoryLabel(noteType: NoteType): string {
  switch (noteType) {
    case "concept":
      return "Conceptos";
    case "author":
      return "Autores";
    case "course":
      return "Cursos";
    case "source":
      return "Fuentes";
  }
}
