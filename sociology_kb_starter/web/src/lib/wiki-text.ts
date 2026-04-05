const TOKEN_RE = /[\p{L}\p{N}]{2,}/gu;
const SUMMARY_RE = /^##\s+(summary|resumen)\s*$/im;
const HEADING_RE = /^#{1,6}\s+/;

export function normalizeText(value: string): string {
  return (value ?? "")
    .normalize("NFKD")
    .replace(/\p{Diacritic}/gu, "")
    .toLowerCase();
}

export function slugifyText(value: string): string {
  return normalizeText(value)
    .replace(/[^a-z0-9\s-]/g, " ")
    .trim()
    .replace(/\s+/g, "-")
    .replace(/-+/g, "-");
}

export function tokenize(value: string): string[] {
  return normalizeText(value).match(TOKEN_RE) ?? [];
}

export function humanizeSlug(slug: string): string {
  const cleaned = slug
    .replace(/\.md$/i, "")
    .replace(/[_/\\]+/g, " ")
    .replace(/-/g, " ")
    .trim();

  if (!cleaned) {
    return "Sin titulo";
  }

  return cleaned.charAt(0).toUpperCase() + cleaned.slice(1);
}

export function escapeMarkdownLabel(value: string): string {
  return value.replace(/([\[\]\\])/g, "\\$1");
}

export function stripMarkdown(value: string): string {
  return value
    .replace(/```[\s\S]*?```/g, " ")
    .replace(/`([^`]+)`/g, "$1")
    .replace(/!\[[^\]]*]\([^)]*\)/g, " ")
    .replace(/\[([^\]]+)]\(([^)]+)\)/g, "$1")
    .replace(/\[\[([^[\]]+)\]\]/g, "$1")
    .replace(/^>\s?/gm, "")
    .replace(/^[-*+]\s+/gm, "")
    .replace(/^\d+\.\s+/gm, "")
    .replace(/\|/g, " ")
    .replace(/[#*_~>-]/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}

export function stripTitleHeading(markdown: string, title: string): string {
  const lines = markdown.replace(/^\uFEFF/, "").split(/\r?\n/);
  const firstContentIndex = lines.findIndex((line) => line.trim().length > 0);

  if (firstContentIndex === -1) {
    return markdown.trim();
  }

  const firstLine = lines[firstContentIndex].trim();
  if (
    firstLine.startsWith("# ") &&
    normalizeText(firstLine.slice(2)) === normalizeText(title)
  ) {
    lines.splice(firstContentIndex, 1);
  }

  return lines.join("\n").trim();
}

export function extractSummary(markdown: string): string {
  const match = markdown.match(SUMMARY_RE);
  if (!match || match.index === undefined) {
    return "";
  }

  const remainder = markdown.slice(match.index + match[0].length).trim();
  const nextHeading = remainder.search(/^##\s+/m);
  const fragment = nextHeading === -1 ? remainder : remainder.slice(0, nextHeading);
  return stripMarkdown(fragment).trim();
}

export function extractPreview(markdown: string, maxLength = 220): string {
  const explicitSummary = extractSummary(markdown);
  const candidate = explicitSummary || firstMeaningfulParagraph(markdown);
  const collapsed = stripMarkdown(candidate).replace(/\s+/g, " ").trim();

  if (collapsed.length <= maxLength) {
    return collapsed;
  }

  return `${collapsed.slice(0, maxLength - 1).trimEnd()}…`;
}

export function extractWikiReferences(markdown: string): string[] {
  const matches = markdown.matchAll(/\[\[([^[\]]+)\]\]/g);
  const refs: string[] = [];

  for (const match of matches) {
    const raw = match[1]?.trim();
    if (!raw) {
      continue;
    }

    const [target] = raw.split("|");
    if (target?.trim()) {
      refs.push(target.trim());
    }
  }

  return refs;
}

export function formatDateEs(value: string | undefined): string {
  if (!value) {
    return "Sin fecha";
  }

  const date = new Date(value);
  if (Number.isNaN(date.getTime())) {
    return value;
  }

  return new Intl.DateTimeFormat("es-ES", {
    day: "numeric",
    month: "long",
    year: "numeric",
  }).format(date);
}

function firstMeaningfulParagraph(markdown: string): string {
  const blocks = markdown.split(/\n\s*\n/);

  for (const block of blocks) {
    const trimmed = block.trim();
    if (!trimmed) {
      continue;
    }
    if (HEADING_RE.test(trimmed)) {
      continue;
    }
    return trimmed;
  }

  return markdown;
}
