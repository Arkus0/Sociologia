"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { usePathname, useRouter, useSearchParams } from "next/navigation";

import { NOTE_TYPE_LABELS } from "@/lib/wiki-routes";
import { searchDocuments } from "@/lib/wiki-search";
import type { SearchIndex } from "@/lib/wiki-types";

export function SearchView() {
  const pathname = usePathname();
  const router = useRouter();
  const searchParams = useSearchParams();
  const [query, setQuery] = useState(searchParams.get("q") ?? "");
  const [index, setIndex] = useState<SearchIndex | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setQuery(searchParams.get("q") ?? "");
  }, [searchParams]);

  useEffect(() => {
    let cancelled = false;

    async function loadIndex() {
      try {
        setError(null);
        const response = await fetch("/generated/search-index.json");
        if (!response.ok) {
          throw new Error("No se pudo cargar el indice de busqueda");
        }
        const data = (await response.json()) as SearchIndex;
        if (!cancelled) {
          setIndex(data);
        }
      } catch (loadError) {
        if (!cancelled) {
          setError(
            loadError instanceof Error
              ? loadError.message
              : "No se pudo cargar el indice de busqueda",
          );
        }
      }
    }

    void loadIndex();

    return () => {
      cancelled = true;
    };
  }, []);

  const results = index && query.trim() ? searchDocuments(index, query.trim(), 25) : [];

  function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const params = new URLSearchParams(searchParams.toString());

    if (query.trim()) {
      params.set("q", query.trim());
    } else {
      params.delete("q");
    }

    const next = params.toString();
    router.replace(next ? `${pathname}?${next}` : pathname);
  }

  return (
    <section className="search-page">
      <header className="page-header">
        <h1>Buscar</h1>
        <p>
          Busqueda lexica estatica sobre conceptos, autores, cursos y fuentes de
          Jotapedia.
        </p>
      </header>

      <form className="search-form" onSubmit={handleSubmit}>
        <label>
          <span>Consulta</span>
          <input
            type="search"
            value={query}
            onChange={(event) => setQuery(event.target.value)}
            placeholder="Escribe un concepto, autor o tema"
          />
        </label>
        <button type="submit">Buscar</button>
      </form>

      {error ? <p className="empty-state">{error}</p> : null}
      {!index && !error ? (
        <p className="empty-state">Cargando indice de busqueda…</p>
      ) : null}

      {index && !query.trim() ? (
        <p className="empty-state">
          Introduce una consulta para explorar la enciclopedia.
        </p>
      ) : null}

      {index && query.trim() && results.length === 0 ? (
        <p className="empty-state">
          No se han encontrado resultados para esa consulta.
        </p>
      ) : null}

      {results.length > 0 ? (
        <section className="search-results">
          <p className="page-toolbar__count">
            {results.length} {results.length === 1 ? "resultado" : "resultados"}
          </p>
          <ul>
            {results.map((result) => (
              <li key={result.route} className="search-result">
                <Link href={result.route}>{result.title}</Link>
                <p>{result.preview}</p>
                <div className="search-result__meta">
                  <span>{NOTE_TYPE_LABELS[result.noteType]}</span>
                  {result.course ? <span>{result.course}</span> : null}
                  {result.semester ? <span>{result.semester}</span> : null}
                </div>
              </li>
            ))}
          </ul>
        </section>
      ) : null}
    </section>
  );
}
