import type { Metadata } from "next";
import { notFound } from "next/navigation";

import { ArticleView } from "@/components/article-view";
import { loadArticlePayload, loadCatalog } from "@/lib/generated-data";

export async function generateStaticParams() {
  const catalog = await loadCatalog();
  return catalog
    .filter((entry) => entry.noteType === "course")
    .map((entry) => ({ slug: entry.slug }));
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ slug: string }>;
}): Promise<Metadata> {
  const { slug } = await params;
  const route = `/cursos/${slug}`;
  const article = await loadArticlePayload(route);
  if (!article) return {};
  return {
    title: `${article.title} — Jotapedia`,
    description: article.preview,
    alternates: {
      canonical: article.canonicalEntry?.route ?? route,
    },
    robots: article.isAlias ? { index: false, follow: true } : undefined,
    openGraph: { title: `${article.title} — Jotapedia`, description: article.preview, type: "article" },
    twitter: { card: "summary", title: `${article.title} — Jotapedia`, description: article.preview },
  };
}

export default async function CourseArticlePage({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const article = await loadArticlePayload(`/cursos/${slug}`);

  if (!article) {
    notFound();
  }

  return <ArticleView article={article} />;
}
