import { notFound } from "next/navigation";

import { ArticleView } from "@/components/article-view";
import { loadArticlePayload, loadCatalog } from "@/lib/generated-data";

export async function generateStaticParams() {
  const catalog = await loadCatalog();
  return catalog
    .filter((entry) => entry.noteType === "course")
    .map((entry) => ({ slug: entry.slug }));
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
