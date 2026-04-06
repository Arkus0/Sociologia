"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";

export function RandomRedirect({ routes }: { routes: string[] }) {
  const router = useRouter();

  useEffect(() => {
    if (routes.length === 0) {
      return;
    }

    const nextRoute = routes[Math.floor(Math.random() * routes.length)];
    router.replace(nextRoute);
  }, [router, routes]);

  return (
    <section className="index-page">
      <header className="page-header">
        <h1>Articulo aleatorio</h1>
        <p>Seleccionando una pagina de Jotapedia...</p>
      </header>
    </section>
  );
}
