import type { MetadataRoute } from "next";

import { loadCatalog } from "@/lib/generated-data";

export const dynamic = "force-static";

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const catalog = await loadCatalog();
  const siteUrl = resolveSiteUrl();
  const staticRoutes = [
    "/",
    "/buscar",
    "/conceptos",
    "/autores",
    "/cursos",
    "/fuentes",
    "/grafo",
    "/stats",
    "/calidad",
    "/aleatoria",
  ];

  return [
    ...staticRoutes.map((route) => ({
      url: new URL(route, siteUrl).toString(),
    })),
    ...catalog
      .filter((entry) => !entry.isAlias)
      .map((entry) => ({
      url: new URL(entry.route, siteUrl).toString(),
      lastModified: entry.timestamp,
      })),
  ];
}

function resolveSiteUrl(): string {
  const candidate =
    process.env.NEXT_PUBLIC_SITE_URL ||
    process.env.VERCEL_PROJECT_PRODUCTION_URL ||
    process.env.VERCEL_URL;

  if (!candidate) {
    return "http://localhost:3000";
  }

  return candidate.startsWith("http") ? candidate : `https://${candidate}`;
}
