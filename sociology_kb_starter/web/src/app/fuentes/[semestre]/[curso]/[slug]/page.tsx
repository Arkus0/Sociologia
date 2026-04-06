import type { Metadata } from "next";
import { notFound } from "next/navigation";

import { ArticleView } from "@/components/article-view";
import { loadArticlePayload, loadCatalog } from "@/lib/generated-data";

export async function generateStaticParams() {
  const catalog = await loadCatalog();
  return catalog
    .filter((entry) => entry.noteType === "source")
    .map((entry) => {
      const [, semestre, curso, slug] = entry.routeSegments;
      return { semestre, curso, slug };
    });
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ semestre: string; curso: string; slug: string }>;
}): Promise<Metadata> {
  const { semestre, curso, slug } = await params;
  const article = await loadArticlePayload(`/fuentes/${semestre}/${curso}/${slug}`);
  if (!article) return {};
  return {
    title: `${article.title} — Jotapedia`,
    description: article.preview,
    openGraph: { title: `${article.title} — Jotapedia`, description: article.preview, type: "article" },
    twitter: { card: "summary", title: `${article.title} — Jotapedia`, description: article.preview },
  };
}

export default async function SourceArticlePage({
  params,
}: {
  params: Promise<{ semestre: string; curso: string; slug: string }>;
}) {
  const { semestre, curso, slug } = await params;
  const article = await loadArticlePayload(`/fuentes/${semestre}/${curso}/${slug}`);

  if (!article) {
    notFound();
  }

  return <ArticleView article={article} />;
}
