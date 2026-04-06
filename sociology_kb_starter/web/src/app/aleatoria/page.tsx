import { RandomRedirect } from "@/components/random-redirect";
import { loadCatalog } from "@/lib/generated-data";

export default async function RandomArticlePage() {
  const catalog = await loadCatalog();
  const routes = catalog.map((entry) => entry.route);

  return <RandomRedirect routes={routes} />;
}
