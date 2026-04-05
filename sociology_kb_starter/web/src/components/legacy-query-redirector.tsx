"use client";

import { useEffect } from "react";
import { useRouter, useSearchParams } from "next/navigation";

import { buildLegacyQueryRedirect } from "@/lib/wiki-routes";

export function LegacyQueryRedirector() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const target = buildLegacyQueryRedirect({
    view: searchParams.get("view"),
    type: searchParams.get("type"),
    article: searchParams.get("article"),
    q: searchParams.get("q"),
  });

  useEffect(() => {
    if (!target) {
      return;
    }

    router.replace(target);
  }, [router, target]);

  if (!target) {
    return null;
  }

  return (
    <div className="legacy-banner" role="status">
      Redirigiendo el enlace antiguo a la ruta actual de Jotapedia…
    </div>
  );
}
