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
