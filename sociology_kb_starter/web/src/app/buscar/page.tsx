import { Suspense } from "react";

import { SearchView } from "@/components/search-view";

export default function SearchPage() {
  return (
    <Suspense fallback={<p className="empty-state">Preparando la busqueda…</p>}>
      <SearchView />
    </Suspense>
  );
}
