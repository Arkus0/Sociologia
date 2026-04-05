import { humanizeSlug, normalizeText, slugifyText } from "./wiki-text";
import type { BreadcrumbItem, NoteType } from "./wiki-types";

export const NOTE_TYPE_LABELS: Record<NoteType, string> = {
  concept: "Concepto",
  author: "Autor",
  course: "Curso",
  source: "Fuente",
};

export const NOTE_TYPE_PLURAL_LABELS: Record<NoteType, string> = {
  concept: "Conceptos",
  author: "Autores",
  course: "Cursos",
  source: "Fuentes",
};

export const NOTE_TYPE_ROUTES: Record<NoteType, string> = {
  concept: "/conceptos",
  author: "/autores",
  course: "/cursos",
  source: "/fuentes",
};

export function normalizeRelativePath(relativePath: string): string {
  return relativePath
    .replace(/\\/g, "/")
    .replace(/^data\/wiki\//i, "")
    .replace(/^wiki\//i, "")
    .replace(/^\/+/, "")
    .trim();
}

export function inferNoteTypeFromRelativePath(relativePath: string): NoteType {
  const normalized = normalizeRelativePath(relativePath);

  if (normalized.startsWith("concepts/")) {
    return "concept";
  }
  if (normalized.startsWith("authors/")) {
    return "author";
  }
  if (normalized.startsWith("courses/")) {
    return "course";
  }
  if (normalized.startsWith("sources/")) {
    return "source";
  }

  throw new Error(`No se puede inferir el tipo de nota para ${relativePath}`);
}

export function buildNoteRoute({
  noteType,
  slug,
  relativePath,
}: {
  noteType: NoteType;
  slug: string;
  relativePath: string;
}): string {
  const normalizedPath = normalizeRelativePath(relativePath);

  if (noteType !== "source") {
    return `${NOTE_TYPE_ROUTES[noteType]}/${slug}`;
  }

  const segments = normalizedPath.replace(/\.md$/i, "").split("/");
  if (segments.length < 4) {
    throw new Error(`Ruta source invalida: ${relativePath}`);
  }

  const [, semester, course, fileSlug] = segments;
  return `/fuentes/${semester}/${course}/${fileSlug}`;
}

export function buildLegacySourceRoute(legacyId: string): string {
  return `/legado/fuentes/${legacyId}`;
}

export function routeToArticlePayloadPath(route: string): string {
  return `articles${route}.json`;
}

export function getCategoryRouteForType(noteType: NoteType): string {
  return NOTE_TYPE_ROUTES[noteType];
}

export function getNoteTypeLabel(noteType: NoteType): string {
  return NOTE_TYPE_LABELS[noteType];
}

export function getNoteTypePluralLabel(noteType: NoteType): string {
  return NOTE_TYPE_PLURAL_LABELS[noteType];
}

export function buildLegacyQueryRedirect(query: {
  view?: string | null;
  type?: string | null;
  article?: string | null;
  q?: string | null;
}): string | null {
  const view = query.view?.trim() ?? "";
  const type = query.type?.trim() ?? "";
  const article = query.article?.trim() ?? "";
  const q = query.q?.trim() ?? "";

  if (view === "home") {
    return "/";
  }

  if (view === "search") {
    return q ? `/buscar?q=${encodeURIComponent(q)}` : "/buscar";
  }

  if (view === "category") {
    switch (type) {
      case "concept":
        return "/conceptos";
      case "author":
        return "/autores";
      case "course":
        return "/cursos";
      case "source":
        return "/fuentes";
      default:
        return "/";
    }
  }

  if (article && type) {
    switch (type) {
      case "concept":
        return `/conceptos/${article}`;
      case "author":
        return `/autores/${article}`;
      case "course":
        return `/cursos/${article}`;
      case "source":
        return buildLegacySourceRoute(article);
      default:
        return null;
    }
  }

  return null;
}

export function buildSourceIndexAnchor(
  semester: string | undefined,
  course: string | undefined,
): string | undefined {
  if (!semester) {
    return undefined;
  }

  if (!course) {
    return `${NOTE_TYPE_ROUTES.source}#${slugifyText(semester)}`;
  }

  return `${NOTE_TYPE_ROUTES.source}#${slugifyText(`${semester}-${course}`)}`;
}

export function buildSourceBreadcrumbs(options: {
  title: string;
  semester?: string;
  course?: string;
  courseRoute?: string;
}): BreadcrumbItem[] {
  const breadcrumbs: BreadcrumbItem[] = [
    { label: "Portada", href: "/" },
    { label: "Fuentes", href: "/fuentes" },
  ];

  if (options.semester) {
    breadcrumbs.push({
      label: options.semester,
      href: buildSourceIndexAnchor(options.semester, undefined),
    });
  }

  if (options.course) {
    breadcrumbs.push({
      label: options.course,
      href:
        options.courseRoute ??
        buildSourceIndexAnchor(options.semester, options.course),
    });
  }

  breadcrumbs.push({ label: options.title });
  return breadcrumbs;
}

export function titleFromReference(reference: string): string {
  const normalized = normalizeRelativePath(reference);
  const stem = normalized.split("/").pop() ?? reference;
  return humanizeSlug(stem.replace(/\.md$/i, ""));
}

export function matchesLooseSlug(candidate: string, value: string): boolean {
  return normalizeText(candidate) === normalizeText(value);
}
