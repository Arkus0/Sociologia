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
  normalizeText,
  slugifyText,
  stripMarkdown,
  stripTitleHeading,
  tokenize,
} from "./wiki-text";
import type {
  ArticlePayload,
  CatalogEntry,
  FactCard,
  FrontmatterSubset,
  InfoboxItem,
  LegacyLookupEntry,
  LinkResolution,
  NoteType,
  QualityIssue,
  QualityReport,
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
  byTitleVariant: Map<string, WikiDocument[]>;
  byRoute: Map<string, WikiDocument>;
  aliasByRoute: Map<string, WikiDocument>;
  aliasesByCanonicalRoute: Map<string, WikiDocument[]>;
  backlinksByRoute: Map<string, RelatedLink[]>;
}

interface RenderEnv {
  headingIds: Record<number, string>;
}

interface ResolveReferenceOptions {
  currentDocument?: WikiDocument;
}

interface BuildWikiArtifactsOptions {
  wikiRoot: string;
  outputRoot: string;
  publicRoot?: string;
}

interface BacklinkSummary {
  total: number;
  concepts: number;
  authors: number;
  courses: number;
  sources: number;
}

const WIKI_SECTIONS = ["concepts", "authors", "courses", "sources"] as const;
const NOTE_PRIORITY: NoteType[] = ["concept", "author", "course"];
const QUALITY_PREVIEW_MIN = 72;
const THIN_ENTRY_MIN: Record<Exclude<NoteType, "source">, number> = {
  concept: 300,
  author: 200,
  course: 150,
};
const ISSUE_PRIORITY: Record<QualityIssue["kind"], number> = {
  broken_reference: 100,
  ambiguous_reference: 95,
  missing_course: 85,
  course_variant: 80,
  missing_required_section: 75,
  thin_entry: 65,
  missing_related_concepts: 60,
  orphan_entry: 55,
  thin_preview: 40,
};
const REQUIRED_SECTIONS: Record<"concept" | "author", Array<{ key: string; patterns: RegExp[] }>> = {
  concept: [
    { key: "Definicion", patterns: [/^definicion$/] },
    { key: "Origen y contexto historico", patterns: [/^origen$/, /^origen y contexto historico$/] },
    { key: "Desarrollo teorico", patterns: [/^desarrollo teorico$/] },
    { key: "Relacion con otros conceptos", patterns: [/^relacion con otros conceptos$/] },
    { key: "Debates y criticas", patterns: [/^debates y criticas$/] },
    { key: "Vigencia contemporanea", patterns: [/^vigencia contemporanea$/] },
    { key: "Ejemplo empirico", patterns: [/^ejemplo empirico$/] },
    { key: "Vease tambien", patterns: [/^vease tambien$/] },
    { key: "Fuentes", patterns: [/^fuentes$/] },
  ],
  author: [
    { key: "Biografia intelectual", patterns: [/^biografia intelectual$/] },
    { key: "Contribuciones principales", patterns: [/^contribuciones principales$/] },
    { key: "Metodo y enfoque", patterns: [/^metodo y enfoque$/] },
    { key: "Obras fundamentales", patterns: [/^obras fundamentales$/] },
    { key: "Influencia y legado", patterns: [/^influencia y legado$/] },
    { key: "Criticas", patterns: [/^criticas$/] },
    { key: "Vease tambien", patterns: [/^vease tambien$/] },
    { key: "Fuentes", patterns: [/^fuentes$/] },
  ],
};

export async function buildWikiArtifacts(
  options: BuildWikiArtifactsOptions,
): Promise<void> {
  const documents = await collectWikiDocuments(options.wikiRoot);
  const registry = buildLinkRegistry(documents);
  registry.backlinksByRoute = buildBacklinkMap(documents, registry);
  const catalog = documents.map((document) => toCatalogEntry(document, registry));
  const articles = documents.map((document) =>
    buildArticlePayload(document, registry),
  );
  const searchIndex = buildSearchIndex(documents, registry);
  const legacyMap = buildLegacyMap(documents);
  const qualityReport = buildQualityReport(documents, registry);
  const facts = buildFactCards(documents, registry);

  await fs.rm(options.outputRoot, { recursive: true, force: true });
  await fs.mkdir(options.outputRoot, { recursive: true });

  await writeJson(path.join(options.outputRoot, "catalog.json"), catalog);
  await writeJson(path.join(options.outputRoot, "search-index.json"), searchIndex);
  await writeJson(path.join(options.outputRoot, "legacy-map.json"), legacyMap);
  await writeJson(
    path.join(options.outputRoot, "quality-report.json"),
    qualityReport,
  );
  await writeJson(path.join(options.outputRoot, "facts.json"), facts);

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
    await writeJson(path.join(options.publicRoot, "catalog.json"), catalog);

    // Copy atlas graph if available (for /grafo page)
    const graphDir = path.join(path.dirname(options.wikiRoot), "graph");
    const graphPath = path.join(graphDir, "atlas_graph.json");
    try {
      const graph = JSON.parse(await fs.readFile(graphPath, "utf8")) as Record<string, unknown>;
      await writeJson(
        path.join(options.publicRoot, "atlas_graph.json"),
        withPublicRoutes(graph, documents),
      );
    } catch {
      // Graph file not available — skip
    }

    // Generate RSS feed
    const siteUrl =
      process.env.NEXT_PUBLIC_SITE_URL ||
      process.env.VERCEL_PROJECT_PRODUCTION_URL ||
      "https://jotapedia.vercel.app";
    const baseUrl = siteUrl.startsWith("http") ? siteUrl : `https://${siteUrl}`;
    const rssXml = buildRssFeed(catalog, facts, baseUrl);
    await fs.writeFile(path.join(options.publicRoot, "feed.xml"), rssXml, "utf8");
  }
}

export async function collectWikiDocuments(
  wikiRoot: string,
): Promise<WikiDocument[]> {
  const files = await collectMarkdownFiles(wikiRoot);
  const rawDocuments = await Promise.all(
    files.map((filePath) => readWikiDocument(filePath, wikiRoot)),
  );
  const documents = normalizeWikiDocuments(rawDocuments);

  return documents.sort((left, right) =>
    left.title.localeCompare(right.title, "es"),
  );
}

export function buildSearchIndex(
  documents: WikiDocument[],
  registry: LinkRegistry,
): SearchIndex {
  const docFreq = new Map<string, number>();
  const docs = getCanonicalDocuments(documents, registry).map<SearchEntry>((document) => {
    const aliases = collectCanonicalAliases(document, registry);
    const fieldTokens = buildSearchFieldTokens(document, aliases);
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
      aliases,
      isAlias: false,
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
  options: ResolveReferenceOptions = {},
): LinkResolution {
  return resolveReferenceInternal(reference, registry, true, options);
}

function resolveReferenceInternal(
  reference: string,
  registry: LinkRegistry,
  collapseAliases: boolean,
  options: ResolveReferenceOptions = {},
): LinkResolution {
  const trimmed = normalizeReferenceValue(reference);
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
    return toLinkResolution(directPathMatch, registry, collapseAliases);
  }

  const slugCandidate = path.basename(normalizedPath.replace(/\.md$/i, ""));
  const normalizedTitle = normalizeText(trimmed);
  const candidates = dedupeDocuments(
    [
      ...(registry.byId.get(trimmed) ?? []),
      ...(registry.byId.get(slugCandidate) ?? []),
      ...(registry.bySlug.get(trimmed) ?? []),
      ...(registry.bySlug.get(slugCandidate) ?? []),
      ...(registry.byTitleVariant.get(normalizedTitle) ?? []),
      ...findLooseMatches(trimmed, registry.byId),
      ...findLooseMatches(slugCandidate, registry.bySlug),
    ].map((document) =>
      collapseAliases ? getCanonicalDocument(document, registry) : document,
    ),
  );

  if (candidates.length === 0) {
    return {
      status: "missing",
      title: titleFromReference(trimmed),
    };
  }

  if (candidates.length === 1) {
    return toLinkResolution(candidates[0], registry, false);
  }

  const contextualCandidate = pickContextualCandidate(candidates, options.currentDocument);
  if (contextualCandidate) {
    return toLinkResolution(contextualCandidate, registry, false);
  }

  const prioritized = pickPreferredCandidate(candidates);
  if (prioritized) {
    return toLinkResolution(prioritized, registry, false);
  }

  return {
    status: "ambiguous",
    title: titleFromReference(trimmed),
    route: buildLegacySourceRoute(slugCandidate),
    noteType: "source",
  };
}

function toLinkResolution(
  document: WikiDocument,
  registry: LinkRegistry,
  collapseAliases: boolean,
): LinkResolution {
  const resolvedDocument = collapseAliases
    ? getCanonicalDocument(document, registry)
    : document;

  return {
    status: "exact",
    title: resolvedDocument.title,
    route: resolvedDocument.route,
    noteType: resolvedDocument.noteType,
  };
}

export function renderMarkdownDocument(
  markdown: string,
  registry: LinkRegistry,
  currentDocument?: WikiDocument,
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

  const processedMarkdown = rewriteWikiLinks(markdown, registry, currentDocument);
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
  const canonicalDocument = getCanonicalDocument(document, registry);
  const referenceDocument = canonicalDocument;
  const courseRoute = referenceDocument.course
    ? resolveReference(slugifyText(referenceDocument.course), registry, {
        currentDocument: referenceDocument,
      }).route
    : undefined;
  const { html, toc } = renderMarkdownDocument(document.body, registry, document);
  const isAlias = canonicalDocument.route !== document.route;

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
    infobox: buildInfobox(document, canonicalDocument, registry),
    aliases: collectCanonicalAliases(canonicalDocument, registry),
    isAlias,
    canonicalEntry: isAlias
      ? {
          title: canonicalDocument.title,
          route: canonicalDocument.route,
          noteType: canonicalDocument.noteType,
        }
      : undefined,
    relatedLinks: buildRelatedLinks(referenceDocument, registry),
    backlinks: registry.backlinksByRoute.get(canonicalDocument.route) ?? [],
    frontmatterSubset: document.frontmatterSubset,
    wordCount: document.wordCount,
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
  const raw = normalizeMarkdownSource(await fs.readFile(absolutePath, "utf8"));
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

  const rawSemester = asString(data.semester);
  const rawCourse = asString(data.course);
  const sourcePath = asString(data.source_path);
  const reviewed = typeof data.reviewed === "boolean" ? data.reviewed : undefined;
  const concepts = normalizeStringArray(data.concepts);
  const authors = normalizeStringArray(data.authors);
  const relatedConcepts = normalizeStringArray(data.related_concepts);
  const sourceNotes = normalizeStringArray(data.source_notes);
  const tags = normalizeStringArray(data.tags);
  const id = asString(data.id) ?? slug;

  const frontmatterSubset: FrontmatterSubset = {};
  if (rawSemester) {
    frontmatterSubset.semester = rawSemester;
  }
  if (rawCourse) {
    frontmatterSubset.course = rawCourse;
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
    rawSemester,
    semester: rawSemester,
    rawCourse,
    course: rawCourse,
    sourcePath,
    reviewed,
    concepts,
    authors,
    relatedConcepts,
    sourceNotes,
    tags,
    outgoingLinks: extractWikiReferences(body),
    aliasTargetReference: extractAliasTargetReference(body),
    frontmatterSubset,
    frontmatter: data,
    wordCount: body.split(/\s+/).filter(Boolean).length,
  };
}

function normalizeWikiDocuments(documents: WikiDocument[]): WikiDocument[] {
  const canonicalCourses = buildCanonicalCourseMap(documents);
  const sourceDocuments = documents.filter((document) => document.noteType === "source");

  return documents.map((document) => {
    const inferredSemester =
      inferDocumentSemester(document, sourceDocuments) ?? document.rawSemester;
    const normalizedCourse = normalizeCourseValue(document.rawCourse, canonicalCourses);
    const inferredCourse =
      normalizeCourseValue(inferDocumentCourse(document, sourceDocuments), canonicalCourses) ??
      (document.noteType === "source"
        ? normalizeCourseValue(document.routeSegments[2], canonicalCourses)
        : undefined);
    const course = normalizedCourse ?? inferredCourse;
    const courseSource = document.rawCourse
      ? normalizedCourse && normalizedCourse !== document.rawCourse
        ? "normalized"
        : "declared"
      : course
        ? "inferred"
        : undefined;

    return {
      ...document,
      semester: inferredSemester,
      course,
      courseSource,
    };
  });
}

function buildCanonicalCourseMap(documents: WikiDocument[]): Map<string, string> {
  const map = new Map<string, string>();

  for (const document of documents) {
    if (document.noteType !== "course") {
      continue;
    }

    const variants = [
      document.id,
      document.slug,
      document.title,
      slugifyText(document.title),
      normalizeText(document.title),
    ];

    for (const variant of variants) {
      const normalized = normalizeText(variant);
      if (normalized) {
        map.set(normalized, document.title);
      }
    }
  }

  return map;
}

function normalizeCourseValue(
  value: string | undefined,
  canonicalCourses: Map<string, string>,
): string | undefined {
  if (!value) {
    return undefined;
  }

  const normalized = normalizeText(value);
  return canonicalCourses.get(normalized) ?? value;
}

function inferDocumentCourse(
  document: WikiDocument,
  sourceDocuments: WikiDocument[],
): string | undefined {
  if (document.noteType === "source") {
    return document.rawCourse;
  }

  if (document.sourceNotes.length === 0) {
    return undefined;
  }

  const candidates = new Set(
    document.sourceNotes
      .map((reference) => resolveSourceDocument(reference, sourceDocuments)?.course)
      .filter((value): value is string => Boolean(value)),
  );

  return candidates.size === 1 ? [...candidates][0] : undefined;
}

function inferDocumentSemester(
  document: WikiDocument,
  sourceDocuments: WikiDocument[],
): string | undefined {
  if (document.noteType === "source") {
    return document.rawSemester ?? document.routeSegments[1];
  }

  if (document.rawSemester) {
    return document.rawSemester;
  }

  const candidates = new Set(
    document.sourceNotes
      .map((reference) => resolveSourceDocument(reference, sourceDocuments)?.semester)
      .filter((value): value is string => Boolean(value)),
  );

  return candidates.size === 1 ? [...candidates][0] : undefined;
}

function resolveSourceDocument(
  reference: string,
  sourceDocuments: WikiDocument[],
): WikiDocument | undefined {
  const normalizedPath = normalizeRelativePath(reference);
  const pathWithExtension = normalizedPath.endsWith(".md")
    ? normalizedPath
    : `${normalizedPath}.md`;
  const direct = sourceDocuments.find(
    (document) => normalizeRelativePath(document.relativePath) === pathWithExtension,
  );
  if (direct) {
    return direct;
  }

  const referenceSlug = path.basename(normalizedPath.replace(/\.md$/i, ""));
  const candidates = sourceDocuments.filter(
    (document) =>
      document.id === reference ||
      document.id === referenceSlug ||
      document.slug === reference ||
      document.slug === referenceSlug,
  );

  if (candidates.length === 1) {
    return candidates[0];
  }

  const uniqueCourses = new Set(candidates.map((document) => document.course).filter(Boolean));
  return candidates.length > 0 && uniqueCourses.size === 1 ? candidates[0] : undefined;
}

function buildLinkRegistry(documents: WikiDocument[]): LinkRegistry {
  const byRelativePath = new Map<string, WikiDocument>();
  const bySlug = new Map<string, WikiDocument[]>();
  const byId = new Map<string, WikiDocument[]>();
  const byTitleVariant = new Map<string, WikiDocument[]>();
  const byRoute = new Map<string, WikiDocument>();
  const aliasByRoute = new Map<string, WikiDocument>();
  const aliasesByCanonicalRoute = new Map<string, WikiDocument[]>();

  for (const document of documents) {
    byRelativePath.set(normalizeRelativePath(document.relativePath), document);
    byRoute.set(document.route, document);
    appendMapValue(bySlug, document.slug, document);
    appendMapValue(byId, document.id, document);
    for (const titleVariant of getTitleVariants(document.title, document.noteType)) {
      appendMapValue(byTitleVariant, titleVariant, document);
    }
  }

  const registry: LinkRegistry = {
    byRelativePath,
    bySlug,
    byId,
    byTitleVariant,
    byRoute,
    aliasByRoute,
    aliasesByCanonicalRoute,
    backlinksByRoute: new Map<string, RelatedLink[]>(),
  };

  for (const document of documents) {
    if (!document.aliasTargetReference) {
      continue;
    }

    const resolution = resolveReferenceInternal(
      document.aliasTargetReference,
      registry,
      false,
      { currentDocument: document },
    );

    if (resolution.status !== "exact" || !resolution.route) {
      continue;
    }

    const targetDocument = byRoute.get(resolution.route);
    if (!targetDocument || targetDocument.route === document.route) {
      continue;
    }

    aliasByRoute.set(document.route, targetDocument);
  }

  for (const [aliasRoute, targetDocument] of aliasByRoute.entries()) {
    const aliasDocument = byRoute.get(aliasRoute);
    const canonicalTarget = getCanonicalDocument(targetDocument, registry);

    if (!aliasDocument) {
      continue;
    }

    aliasByRoute.set(aliasRoute, canonicalTarget);
    appendMapValue(aliasesByCanonicalRoute, canonicalTarget.route, aliasDocument);
  }

  return registry;
}

function buildInfobox(
  document: WikiDocument,
  canonicalDocument: WikiDocument,
  registry: LinkRegistry,
): InfoboxItem[] {
  const isAlias = canonicalDocument.route !== document.route;
  const aliases = collectCanonicalAliases(canonicalDocument, registry);
  const backlinks = registry.backlinksByRoute.get(canonicalDocument.route) ?? [];
  const backlinkSummary = summarizeBacklinks(backlinks);
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

  if (isAlias) {
    items.push({
      label: "Entrada canonica",
      value: canonicalDocument.title,
      href: canonicalDocument.route,
    });
  }

  switch (document.noteType) {
    case "author":
      if (aliases.length > 0 && !isAlias) {
        items.push({
          label: "Alias",
          value: summarizeList(aliases),
        });
      }
      if (canonicalDocument.sourceNotes.length > 0) {
        items.push({
          label: "Fuentes",
          value: String(canonicalDocument.sourceNotes.length),
        });
      }
      if (backlinkSummary.total > 0) {
        items.push({
          label: "Entradas que lo citan",
          value: String(backlinkSummary.total),
        });
      }
      break;
    case "concept":
      if (canonicalDocument.course) {
        const courseMatch = resolveReference(
          slugifyText(canonicalDocument.course),
          registry,
          { currentDocument: canonicalDocument },
        );
        items.push({
          label: "Curso",
          value: canonicalDocument.course,
          href: courseMatch.status === "exact" ? courseMatch.route : undefined,
        });
      }
      if (canonicalDocument.relatedConcepts.length > 0) {
        items.push({
          label: "Relacionados",
          value: String(canonicalDocument.relatedConcepts.length),
        });
      }
      if (canonicalDocument.sourceNotes.length > 0) {
        items.push({
          label: "Notas fuente",
          value: String(canonicalDocument.sourceNotes.length),
        });
      }
      if (backlinkSummary.total > 0) {
        items.push({
          label: "Entradas que enlazan aqui",
          value: String(backlinkSummary.total),
        });
      }
      break;
    case "course":
      if (backlinkSummary.sources > 0) {
        items.push({
          label: "Fuentes del curso",
          value: String(backlinkSummary.sources),
        });
      }
      if (backlinkSummary.concepts > 0) {
        items.push({
          label: "Conceptos asociados",
          value: String(backlinkSummary.concepts),
        });
      }
      if (backlinkSummary.total > 0) {
        items.push({
          label: "Entradas relacionadas",
          value: String(backlinkSummary.total),
        });
      }
      break;
    case "source":
      if (canonicalDocument.semester) {
        items.push({ label: "Semestre", value: canonicalDocument.semester });
      }
      if (canonicalDocument.course) {
        const courseMatch = resolveReference(
          slugifyText(canonicalDocument.course),
          registry,
          { currentDocument: canonicalDocument },
        );
        items.push({
          label: "Curso",
          value: canonicalDocument.course,
          href: courseMatch.status === "exact" ? courseMatch.route : undefined,
        });
      }
      if (canonicalDocument.sourcePath) {
        items.push({
          label: "Archivo fuente",
          value: path.basename(canonicalDocument.sourcePath),
        });
      }
      if (typeof canonicalDocument.reviewed === "boolean") {
        items.push({
          label: "Revisado",
          value: canonicalDocument.reviewed ? "Si" : "No",
        });
      }
      if (canonicalDocument.authors.length > 0) {
        items.push({
          label: "Autores tratados",
          value: String(canonicalDocument.authors.length),
        });
      }
      if (canonicalDocument.concepts.length > 0) {
        items.push({
          label: "Conceptos tratados",
          value: String(canonicalDocument.concepts.length),
        });
      }
      break;
  }

  return items;
}

function buildRelatedLinks(
  document: WikiDocument,
  registry: LinkRegistry,
  limit = 12,
): RelatedLink[] {
  const seeds = collectReferenceSeeds(document);
  const relatedLinks: RelatedLink[] = [];
  const seenRoutes = new Set<string>();

  for (const seed of seeds) {
    const match = resolveReference(seed, registry, { currentDocument: document });
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

function buildSearchFieldTokens(
  document: WikiDocument,
  aliases: string[],
): SearchFieldTokenMap {
  const summary = extractSummary(document.body) || document.preview;
  return {
    title: countTokens(document.title),
    aliases: countTokens(aliases.join(" ")),
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

function rewriteWikiLinks(
  markdown: string,
  registry: LinkRegistry,
  currentDocument?: WikiDocument,
): string {
  return markdown.replace(/\[\[([^[\]]+)\]\]/g, (_match, rawContent: string) => {
    const [reference, alias] = rawContent.split("|");
    const resolution = resolveReference(reference.trim(), registry, { currentDocument });
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

function toCatalogEntry(
  document: WikiDocument,
  registry: LinkRegistry,
): CatalogEntry {
  const canonicalDocument = getCanonicalDocument(document, registry);
  const isAlias = canonicalDocument.route !== document.route;

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
    aliases: collectCanonicalAliases(canonicalDocument, registry),
    isAlias,
    canonicalRoute: isAlias ? canonicalDocument.route : undefined,
    canonicalTitle: isAlias ? canonicalDocument.title : undefined,
    backlinkCount: registry.backlinksByRoute.get(canonicalDocument.route)?.length ?? 0,
    wordCount: document.wordCount,
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

function pickContextualCandidate(
  candidates: WikiDocument[],
  currentDocument?: WikiDocument,
): WikiDocument | undefined {
  if (!currentDocument) {
    return undefined;
  }

  const sameSemesterAndCourse = candidates.filter(
    (candidate) =>
      candidate.noteType === "source" &&
      candidate.semester &&
      currentDocument.semester &&
      normalizeText(candidate.semester) === normalizeText(currentDocument.semester) &&
      candidate.course &&
      currentDocument.course &&
      normalizeText(candidate.course) === normalizeText(currentDocument.course),
  );
  if (sameSemesterAndCourse.length === 1) {
    return sameSemesterAndCourse[0];
  }

  const sameCourse = candidates.filter(
    (candidate) =>
      candidate.noteType === "source" &&
      candidate.course &&
      currentDocument.course &&
      normalizeText(candidate.course) === normalizeText(currentDocument.course),
  );
  if (sameCourse.length === 1) {
    return sameCourse[0];
  }

  const sameSemester = candidates.filter(
    (candidate) =>
      candidate.noteType === "source" &&
      candidate.semester &&
      currentDocument.semester &&
      normalizeText(candidate.semester) === normalizeText(currentDocument.semester),
  );
  if (sameSemester.length === 1) {
    return sameSemester[0];
  }

  return undefined;
}

function getCanonicalDocuments(
  documents: WikiDocument[],
  registry: LinkRegistry,
): WikiDocument[] {
  return dedupeDocuments(
    documents.map((document) => getCanonicalDocument(document, registry)),
  ).sort((left, right) => left.title.localeCompare(right.title, "es"));
}

function getCanonicalDocument(
  document: WikiDocument,
  registry: LinkRegistry,
): WikiDocument {
  let current = document;
  const seenRoutes = new Set<string>();

  while (registry.aliasByRoute.has(current.route)) {
    if (seenRoutes.has(current.route)) {
      break;
    }

    seenRoutes.add(current.route);
    current = registry.aliasByRoute.get(current.route) ?? current;
  }

  return current;
}

function collectCanonicalAliases(
  canonicalDocument: WikiDocument,
  registry: LinkRegistry,
): string[] {
  const aliasDocs = registry.aliasesByCanonicalRoute.get(canonicalDocument.route) ?? [];
  return aliasDocs
    .map((document) => document.title)
    .filter((title) => title !== canonicalDocument.title)
    .sort((left, right) => left.localeCompare(right, "es"));
}

function collectReferenceSeeds(document: WikiDocument): string[] {
  const seeds = [
    ...document.outgoingLinks,
    ...document.relatedConcepts,
    ...document.concepts,
    ...document.authors,
    ...document.sourceNotes,
  ];

  if (document.course) {
    seeds.push(slugifyText(document.course));
  }

  return [...new Set(seeds.map((seed) => seed.trim()).filter(Boolean))];
}

function summarizeBacklinks(backlinks: RelatedLink[]): BacklinkSummary {
  return backlinks.reduce(
    (summary, backlink) => ({
      total: summary.total + 1,
      concepts: summary.concepts + (backlink.noteType === "concept" ? 1 : 0),
      authors: summary.authors + (backlink.noteType === "author" ? 1 : 0),
      courses: summary.courses + (backlink.noteType === "course" ? 1 : 0),
      sources: summary.sources + (backlink.noteType === "source" ? 1 : 0),
    }),
    { total: 0, concepts: 0, authors: 0, courses: 0, sources: 0 },
  );
}

function summarizeList(values: string[], limit = 3): string {
  if (values.length <= limit) {
    return values.join(", ");
  }

  const visible = values.slice(0, limit).join(", ");
  return `${visible} y ${values.length - limit} mas`;
}

function buildBacklinkMap(
  documents: WikiDocument[],
  registry: LinkRegistry,
): Map<string, RelatedLink[]> {
  const backlinks = new Map<string, RelatedLink[]>();
  const seenPairs = new Set<string>();

  for (const document of documents) {
    const canonicalSource = getCanonicalDocument(document, registry);
    const seeds = collectReferenceSeeds(document);

    for (const seed of seeds) {
      const resolution = resolveReference(seed, registry, {
        currentDocument: document,
      });
      if (resolution.status !== "exact" || !resolution.route || !resolution.noteType) {
        continue;
      }

      if (resolution.route === canonicalSource.route) {
        continue;
      }

      const pairKey = `${resolution.route}::${canonicalSource.route}`;
      if (seenPairs.has(pairKey)) {
        continue;
      }

      seenPairs.add(pairKey);
      appendMapValue(backlinks, resolution.route, {
        title: canonicalSource.title,
        route: canonicalSource.route,
        noteType: canonicalSource.noteType,
      });
    }
  }

  for (const [route, links] of backlinks.entries()) {
    backlinks.set(
      route,
      links.sort((left, right) => left.title.localeCompare(right.title, "es")),
    );
  }

  return backlinks;
}

function buildQualityReport(
  documents: WikiDocument[],
  registry: LinkRegistry,
): QualityReport {
  const issues: QualityIssue[] = [];

  for (const document of documents) {
    const canonicalDocument = getCanonicalDocument(document, registry);
    const isAlias = canonicalDocument.route !== document.route;
    const references = isAlias && document.aliasTargetReference
      ? [document.aliasTargetReference]
      : collectReferenceSeeds(document);

    if (!isAlias && document.preview.length < QUALITY_PREVIEW_MIN) {
      issues.push(
        createQualityIssue(document, "thin_preview", {
          detail: `La vista previa es demasiado breve (${document.preview.length} caracteres).`,
        }),
      );
    }

    if (!isAlias && requiresCourse(document) && !document.course) {
      issues.push(
        createQualityIssue(document, "missing_course", {
          detail: "La entrada no tiene curso declarado o inferible de forma univoca.",
        }),
      );
    }

    if (
      !isAlias &&
      document.rawCourse &&
      document.course &&
      normalizeText(document.rawCourse) !== normalizeText(document.course)
    ) {
      issues.push(
        createQualityIssue(document, "course_variant", {
          detail: `Curso normalizado de "${document.rawCourse}" a "${document.course}".`,
        }),
      );
    }

    if (
      !isAlias &&
      document.noteType !== "source" &&
      document.noteType !== "course" &&
      document.wordCount < THIN_ENTRY_MIN[document.noteType]
    ) {
      issues.push(
        createQualityIssue(document, "thin_entry", {
          detail: `La entrada es demasiado breve (${document.wordCount} palabras).`,
        }),
      );
    }

    if (
      !isAlias &&
      (document.noteType === "concept" || document.noteType === "author") &&
      document.relatedConcepts.length < 3
    ) {
      issues.push(
        createQualityIssue(document, "missing_related_concepts", {
          detail: `related_concepts contiene ${document.relatedConcepts.length} entradas; el minimo esperado es 3.`,
        }),
      );
    }

    if (!isAlias && (document.noteType === "concept" || document.noteType === "author")) {
      const missingSections = getMissingRequiredSections(document);
      if (missingSections.length > 0) {
        issues.push(
          createQualityIssue(document, "missing_required_section", {
            detail: `Faltan secciones obligatorias: ${missingSections.join(", ")}.`,
          }),
        );
      }
    }

    if (
      !isAlias &&
      (document.noteType === "concept" || document.noteType === "author") &&
      (registry.backlinksByRoute.get(canonicalDocument.route)?.length ?? 0) === 0
    ) {
      issues.push(
        createQualityIssue(document, "orphan_entry", {
          detail: "La entrada canonica no recibe enlaces entrantes.",
        }),
      );
    }

    for (const reference of references) {
      const resolution = resolveReference(reference, registry, {
        currentDocument: document,
      });
      if (resolution.status === "missing") {
        issues.push(
          createQualityIssue(document, "broken_reference", {
            detail: `Referencia sin resolver: ${reference}`,
            reference,
          }),
        );
        continue;
      }

      if (resolution.status === "ambiguous") {
        issues.push(
          createQualityIssue(document, "ambiguous_reference", {
            detail: `Referencia ambigua: ${reference}`,
            reference,
          }),
        );
      }
    }
  }

  const byKind = issues.reduce<Record<string, number>>((summary, issue) => {
    summary[issue.kind] = (summary[issue.kind] ?? 0) + 1;
    return summary;
  }, {});
  const sortedIssues = issues.sort((left, right) => {
    if (right.priority !== left.priority) {
      return right.priority - left.priority;
    }
    const leftLabel = `${left.documentTitle ?? ""}${left.detail}`;
    const rightLabel = `${right.documentTitle ?? ""}${right.detail}`;
    return leftLabel.localeCompare(rightLabel, "es");
  });

  return {
    generatedAt: new Date().toISOString(),
    summary: {
      issues: sortedIssues.length,
      byKind,
    },
    backlog: buildQualityBacklog(sortedIssues),
    issues: sortedIssues,
  };
}

function createQualityIssue(
  document: WikiDocument,
  kind: QualityIssue["kind"],
  options: {
    detail: string;
    reference?: string;
  },
): QualityIssue {
  return {
    level: "warning",
    kind,
    priority: ISSUE_PRIORITY[kind],
    documentRoute: document.route,
    documentTitle: document.title,
    documentNoteType: document.noteType,
    reference: options.reference,
    detail: options.detail,
  };
}

function requiresCourse(document: WikiDocument): boolean {
  return (
    document.noteType === "concept" ||
    document.noteType === "author" ||
    document.noteType === "source"
  );
}

function getMissingRequiredSections(document: WikiDocument): string[] {
  if (document.noteType !== "concept" && document.noteType !== "author") {
    return [];
  }

  const requirements = REQUIRED_SECTIONS[document.noteType];
  const headings = extractNormalizedHeadings(document.body);

  return requirements
    .filter((section) => !section.patterns.some((pattern) => headings.some((heading) => pattern.test(heading))))
    .map((section) => section.key);
}

function extractNormalizedHeadings(markdown: string): string[] {
  return markdown
    .split(/\r?\n/)
    .map((line) => line.match(/^##\s+(.+?)\s*$/)?.[1])
    .filter((value): value is string => Boolean(value))
    .map((value) => normalizeText(value));
}

function buildQualityBacklog(issues: QualityIssue[]): QualityReport["backlog"] {
  const byDocument = new Map<string, QualityReport["backlog"]["topDocuments"][number]>();
  const byReference = new Map<string, QualityReport["backlog"]["topReferences"][number]>();

  for (const issue of issues) {
    if (issue.documentRoute && issue.documentTitle && issue.documentNoteType) {
      const current = byDocument.get(issue.documentRoute);
      byDocument.set(issue.documentRoute, {
        route: issue.documentRoute,
        title: issue.documentTitle,
        noteType: issue.documentNoteType,
        count: (current?.count ?? 0) + 1,
        maxPriority: Math.max(current?.maxPriority ?? 0, issue.priority),
      });
    }

    if (issue.reference) {
      const current = byReference.get(issue.reference);
      byReference.set(issue.reference, {
        reference: issue.reference,
        count: (current?.count ?? 0) + 1,
        maxPriority: Math.max(current?.maxPriority ?? 0, issue.priority),
      });
    }
  }

  return {
    topDocuments: [...byDocument.values()]
      .sort((left, right) =>
        right.maxPriority - left.maxPriority ||
        right.count - left.count ||
        left.title.localeCompare(right.title, "es"),
      )
      .slice(0, 25),
    topReferences: [...byReference.values()]
      .sort((left, right) =>
        right.maxPriority - left.maxPriority ||
        right.count - left.count ||
        left.reference.localeCompare(right.reference, "es"),
      )
      .slice(0, 25),
  };
}

function extractAliasTargetReference(markdown: string): string | undefined {
  const canonicalSectionMatch = markdown.match(
    /^##\s+(Canonical note|Nota can[oó]nica)\s*$\n?([\s\S]*?)(?=^##\s+|(?![\s\S]))/im,
  );
  if (canonicalSectionMatch?.[2]) {
    const scopedLink = extractWikiReferences(canonicalSectionMatch[2])[0];
    if (scopedLink) {
      return scopedLink;
    }
  }

  const firstBlock = extractFirstMeaningfulBlock(markdown);
  if (!firstBlock) {
    return undefined;
  }

  const firstBlockRaw = extractWikiReferences(firstBlock)[0]?.trim();
  if (!firstBlockRaw) {
    return undefined;
  }

  const normalizedBlock = normalizeText(firstBlock);
  const isAliasBlock =
    normalizedBlock.startsWith("vease [[") ||
    normalizedBlock.includes("entrada canonica es [[") ||
    /canonical note[\s\S]{0,120}\bis\s+\[\[/.test(normalizedBlock);
  if (!isAliasBlock) {
    return undefined;
  }

  return firstBlockRaw.split("|")[0]?.trim();
}

function extractFirstMeaningfulBlock(markdown: string): string | undefined {
  for (const block of markdown.split(/\n\s*\n/)) {
    const lines = block
      .trim()
      .split(/\n/)
      .map((line) => line.trim())
      .filter(Boolean);
    while (lines[0]?.startsWith("#")) {
      lines.shift();
    }
    const trimmed = lines.join("\n").trim();
    if (!trimmed) {
      continue;
    }
    return trimmed;
  }

  return undefined;
}

function normalizeMarkdownSource(raw: string): string {
  return raw.replace(/^\uFEFF/, "").replace(/\r\n/g, "\n").replace(/\r/g, "\n");
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
    .map((item) => (item ? normalizeReferenceValue(item) : undefined))
    .filter((item): item is string => Boolean(item));
}

function normalizeReferenceValue(value: string): string {
  let normalized = value.trim();

  while (normalized.startsWith("[[") && normalized.endsWith("]]")) {
    normalized = normalized.slice(2, -2).trim();
  }

  const [target] = normalized.split("|");
  return target?.trim() ?? "";
}

function getTitleVariants(title: string, noteType?: NoteType): string[] {
  const variants = new Set<string>();
  const normalizedTitle = normalizeText(title);

  if (normalizedTitle) {
    variants.add(normalizedTitle);
  }

  const stem = title.split(/[:\u2014-]/, 1)[0]?.trim();
  const normalizedStem = normalizeText(stem ?? "");
  if (normalizedStem) {
    variants.add(normalizedStem);
  }

  if (noteType === "author" && normalizedTitle) {
    const tokens = normalizedTitle.split(" ").filter(Boolean);
    const withoutInitials = tokens.filter((token, index) => {
      if (index === 0 || index === tokens.length - 1) {
        return true;
      }
      return token.length > 1;
    });

    if (withoutInitials.length >= 2 && withoutInitials.length !== tokens.length) {
      variants.add(withoutInitials.join(" "));
    }

    if (tokens.length >= 3) {
      variants.add(`${tokens[0]} ${tokens[tokens.length - 1]}`);
    }
  }

  return [...variants];
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

export function buildFactCards(
  documents: WikiDocument[],
  registry: LinkRegistry,
): FactCard[] {
  const facts: FactCard[] = [];
  const canonical = getCanonicalDocuments(documents, registry);

  for (const doc of canonical) {
    const candidates = extractFactCandidates(doc);
    for (const text of candidates) {
      facts.push({
        text,
        articleTitle: doc.title,
        articleRoute: doc.route,
        noteType: doc.noteType,
      });
    }
  }

  // Deterministic shuffle so the set varies across builds but is stable within one
  const seed = new Date().toISOString().slice(0, 10);
  let h = 0;
  for (const ch of seed) h = (h * 31 + ch.charCodeAt(0)) >>> 0;
  facts.sort((a, b) => {
    const ha = hashString(a.text, h);
    const hb = hashString(b.text, h);
    return ha - hb;
  });

  return facts.slice(0, 200);
}

function extractFactCandidates(doc: WikiDocument): string[] {
  const results: string[] = [];

  // 1. Core ideas bullets (sources)
  const coreMatch = doc.body.match(/^## Core ideas\s*\n([\s\S]*?)(?=\n## |\n$|$)/m);
  if (coreMatch) {
    const bullets = coreMatch[1]
      .split(/\n/)
      .filter((l) => /^[-*]\s/.test(l.trim()))
      .map((l) => stripMarkdown(l.replace(/^[-*]\s+/, "").trim()))
      .filter((t) => t.length >= 40 && t.length <= 280);
    results.push(...bullets);
  }

  // 2. Definición first sentence (concepts)
  const defMatch = doc.body.match(/^## Definici[oó]n\s*\n([\s\S]*?)(?=\n## |\n$|$)/m);
  if (defMatch) {
    const plain = stripMarkdown(defMatch[1]).trim();
    const firstSentence = plain.match(/^.+?[.!?](?:\s|$)/)?.[0]?.trim();
    if (firstSentence && firstSentence.length >= 40 && firstSentence.length <= 300) {
      results.push(firstSentence);
    }
  }

  // 3. Ejemplo empírico section (concepts)
  const exMatch = doc.body.match(/^## Ejemplo emp[ií]rico\s*\n([\s\S]*?)(?=\n## |\n$|$)/m);
  if (exMatch) {
    const plain = stripMarkdown(exMatch[1]).trim();
    const firstSentence = plain.match(/^.+?[.!?](?:\s|$)/)?.[0]?.trim();
    if (firstSentence && firstSentence.length >= 40 && firstSentence.length <= 300) {
      results.push(firstSentence);
    }
  }

  // 4. Possible exam questions (sources)
  const examMatch = doc.body.match(/^## Possible exam questions\s*\n([\s\S]*?)(?=\n## |\n$|$)/m);
  if (examMatch) {
    const questions = examMatch[1]
      .split(/\n/)
      .filter((l) => /^[-*]\s/.test(l.trim()))
      .map((l) => stripMarkdown(l.replace(/^[-*]\s+/, "").trim()))
      .filter((t) => t.length >= 20 && t.length <= 200);
    results.push(...questions.slice(0, 3));
  }

  return results;
}

function hashString(s: string, seed: number): number {
  let h = seed;
  for (let i = 0; i < s.length; i++) {
    h = (h * 31 + s.charCodeAt(i)) >>> 0;
  }
  return h;
}

function withPublicRoutes(
  graph: Record<string, unknown>,
  documents: WikiDocument[],
): Record<string, unknown> {
  const canonicalDocuments = documents.filter((document) => !document.aliasTargetReference);
  const routeByTypeAndSlug = new Map<string, string>();
  const sourceRouteByRelativePath = new Map<string, string>();

  for (const document of canonicalDocuments) {
    routeByTypeAndSlug.set(`${document.noteType}:${document.slug}`, document.route);
    if (document.noteType === "source") {
      sourceRouteByRelativePath.set(normalizeRelativePath(document.relativePath), document.route);
    }
  }

  const nodes = Array.isArray(graph.nodes) ? graph.nodes : [];

  return {
    ...graph,
    nodes: nodes.map((node) => {
      if (!node || typeof node !== "object") {
        return node;
      }

      const nodeRecord = node as Record<string, unknown>;
      const nodeType = typeof nodeRecord.type === "string" ? nodeRecord.type : "";
      const nodeId = typeof nodeRecord.id === "string" ? nodeRecord.id : "";
      const nodePath = typeof nodeRecord.path === "string" ? normalizeRelativePath(nodeRecord.path) : "";
      const slug = nodeId.includes("::") ? nodeId.split("::")[1] : "";
      const route =
        (nodeType === "source" && nodePath ? sourceRouteByRelativePath.get(nodePath) : undefined) ??
        (slug ? routeByTypeAndSlug.get(`${nodeType}:${slug}`) : undefined);

      return route ? { ...nodeRecord, route } : nodeRecord;
    }),
  };
}

function buildRssFeed(
  catalog: CatalogEntry[],
  facts: FactCard[],
  baseUrl: string,
): string {
  const escXml = (s: string) =>
    s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");

  const recent = [...catalog]
    .filter((e) => !e.isAlias)
    .sort((a, b) => b.timestamp.localeCompare(a.timestamp))
    .slice(0, 30);

  const now = new Date().toUTCString();

  const items = recent.map((entry) => {
    const link = `${baseUrl}${entry.route}`;
    const pubDate = new Date(entry.timestamp).toUTCString();
    const category = getNoteTypeLabel(entry.noteType);

    return `    <item>
      <title>${escXml(entry.title)}</title>
      <link>${escXml(link)}</link>
      <guid isPermaLink="true">${escXml(link)}</guid>
      <pubDate>${pubDate}</pubDate>
      <category>${escXml(category)}</category>
      <description>${escXml(entry.preview)}</description>
    </item>`;
  });

  // Add a few "¿Sabías que...?" items as bonus content
  const factItems = facts.slice(0, 5).map((fact, i) => {
    const link = `${baseUrl}${fact.articleRoute}`;
    return `    <item>
      <title>${escXml(`¿Sabías que...? — ${fact.articleTitle}`)}</title>
      <link>${escXml(link)}</link>
      <guid isPermaLink="false">fact-${i}-${hashString(fact.text, 0)}</guid>
      <pubDate>${now}</pubDate>
      <category>Sabias que</category>
      <description>${escXml(fact.text)}</description>
    </item>`;
  });

  return `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>Jotapedia — Enciclopedia sociologica</title>
    <link>${escXml(baseUrl)}</link>
    <description>Articulos recientes y datos curiosos de sociologia</description>
    <language>es</language>
    <lastBuildDate>${now}</lastBuildDate>
    <atom:link href="${escXml(baseUrl)}/generated/feed.xml" rel="self" type="application/rss+xml"/>
${items.join("\n")}
${factItems.join("\n")}
  </channel>
</rss>`;
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
