"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";

export function LegacySourceRedirect({ targetRoute }: { targetRoute: string }) {
  const router = useRouter();

  useEffect(() => {
    router.replace(targetRoute);
  }, [router, targetRoute]);

  return (
    <div className="legacy-banner" role="status">
      Redirigiendo a la fuente canonica…
    </div>
  );
}
