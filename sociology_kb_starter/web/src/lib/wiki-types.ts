export type NoteType = "concept" | "author" | "course" | "source";

export interface FrontmatterSubset {
  semester?: string;
  course?: string;
  source_path?: string;
  reviewed?: boolean;
  updated_at?: string;
  compiled_at?: string;
}

export interface WikiDocument {
  id: string;
  slug: string;
  title: string;
  noteType: NoteType;
  relativePath: string;
  route: string;
  routeSegments: string[];
  body: string;
  preview: string;
  timestamp: string;
  semester?: string;
  course?: string;
  sourcePath?: string;
  reviewed?: boolean;
  concepts: string[];
  authors: string[];
  relatedConcepts: string[];
  sourceNotes: string[];
  tags: string[];
  outgoingLinks: string[];
  aliasTargetReference?: string;
  frontmatterSubset: FrontmatterSubset;
  frontmatter: Record<string, unknown>;
  wordCount: number;
}

export interface CatalogEntry {
  id: string;
  slug: string;
  title: string;
  noteType: NoteType;
  route: string;
  routeSegments: string[];
  relativePath: string;
  preview: string;
  timestamp: string;
  semester?: string;
  course?: string;
  aliases: string[];
  isAlias: boolean;
  canonicalRoute?: string;
  canonicalTitle?: string;
  backlinkCount: number;
  wordCount: number;
}

export interface TocEntry {
  id: string;
  text: string;
  level: 2 | 3;
}

export interface BreadcrumbItem {
  label: string;
  href?: string;
}

export interface RelatedLink {
  title: string;
  route: string;
  noteType: NoteType;
}

export interface InfoboxItem {
  label: string;
  value: string;
  href?: string;
}

export interface ArticlePayload {
  id: string;
  title: string;
  slug: string;
  noteType: NoteType;
  route: string;
  routeSegments: string[];
  html: string;
  preview: string;
  timestamp: string;
  semester?: string;
  course?: string;
  toc: TocEntry[];
  breadcrumbs: BreadcrumbItem[];
  infobox: InfoboxItem[];
  aliases: string[];
  isAlias: boolean;
  canonicalEntry?: RelatedLink;
  relatedLinks: RelatedLink[];
  backlinks: RelatedLink[];
  frontmatterSubset: FrontmatterSubset;
  wordCount: number;
}

export interface SearchFieldTokenMap {
  title: Record<string, number>;
  aliases: Record<string, number>;
  concepts: Record<string, number>;
  authors: Record<string, number>;
  summary: Record<string, number>;
  body: Record<string, number>;
}

export interface SearchEntry {
  route: string;
  title: string;
  noteType: NoteType;
  preview: string;
  semester?: string;
  course?: string;
  aliases: string[];
  isAlias: boolean;
  canonicalRoute?: string;
  canonicalTitle?: string;
  fieldTokens: SearchFieldTokenMap;
}

export interface SearchIndex {
  docCount: number;
  docFreq: Record<string, number>;
  docs: SearchEntry[];
}

export interface LegacyLookupEntry {
  legacyType: "source";
  legacyId: string;
  status: "exact" | "ambiguous";
  targetRoute?: string;
  targetRoutes?: string[];
}

export interface LinkResolution {
  status: "exact" | "ambiguous" | "missing";
  title: string;
  route?: string;
  noteType?: NoteType;
}

export interface QualityIssue {
  level: "warning";
  kind:
    | "broken_reference"
    | "ambiguous_reference"
    | "duplicate_id"
    | "thin_preview";
  documentRoute?: string;
  documentTitle?: string;
  detail: string;
}

export interface QualityReport {
  generatedAt: string;
  summary: {
    issues: number;
    byKind: Record<string, number>;
  };
  issues: QualityIssue[];
}

export interface FactCard {
  text: string;
  articleTitle: string;
  articleRoute: string;
  noteType: NoteType;
}
