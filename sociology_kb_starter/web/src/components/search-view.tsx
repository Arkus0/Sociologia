"use client";

import {
  startTransition,
  useDeferredValue,
  useEffect,
  useState,
} from "react";
import Link from "next/link";
import { usePathname, useRouter, useSearchParams } from "next/navigation";

import { NOTE_TYPE_LABELS } from "@/lib/wiki-routes";
import { searchDocuments, suggestDocuments } from "@/lib/wiki-search";
import type { NoteType, SearchIndex } from "@/lib/wiki-types";

const SEARCH_TYPES: NoteType[] = ["concept", "author", "course", "source"];

export function SearchView() {
  const pathname = usePathname();
  const router = useRouter();
  const searchParams = useSearchParams();
  const [query, setQuery] = useState(searchParams.get("q") ?? "");
  const [selectedTypes, setSelectedTypes] = useState<NoteType[]>(
    readSelectedTypes(searchParams),
  );
  const [course, setCourse] = useState(searchParams.get("curso") ?? "");
  const [semester, setSemester] = useState(searchParams.get("semestre") ?? "");
  const [index, setIndex] = useState<SearchIndex | null>(null);
  const [error, setError] = useState<string | null>(null);
  const deferredQuery = useDeferredValue(query);

  useEffect(() => {
    setQuery(searchParams.get("q") ?? "");
    setSelectedTypes(readSelectedTypes(searchParams));
    setCourse(searchParams.get("curso") ?? "");
    setSemester(searchParams.get("semestre") ?? "");
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

  const courseOptions = uniqueValues(index?.docs.map((entry) => entry.course) ?? []);
  const semesterOptions = uniqueValues(index?.docs.map((entry) => entry.semester) ?? []);
  const results =
    index && query.trim()
      ? searchDocuments(index, query.trim(), 25, {
          noteTypes: selectedTypes,
          course: course || undefined,
          semester: semester || undefined,
        })
      : [];
  const suggestions =
    index && deferredQuery.trim()
      ? suggestDocuments(index, deferredQuery.trim(), 6, {
          noteTypes: selectedTypes,
          course: course || undefined,
          semester: semester || undefined,
        })
      : [];

  function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    replaceSearchParams(query, selectedTypes, course, semester);
  }

  function toggleType(noteType: NoteType) {
    const nextTypes = selectedTypes.includes(noteType)
      ? selectedTypes.filter((value) => value !== noteType)
      : [...selectedTypes, noteType];
    const resolvedTypes = nextTypes.length > 0 ? nextTypes : [...SEARCH_TYPES];

    setSelectedTypes(resolvedTypes);
    replaceSearchParams(query, resolvedTypes, course, semester);
  }

  function replaceSearchParams(
    nextQuery: string,
    nextTypes: NoteType[],
    nextCourse: string,
    nextSemester: string,
  ) {
    const params = new URLSearchParams(searchParams.toString());

    if (nextQuery.trim()) {
      params.set("q", nextQuery.trim());
    } else {
      params.delete("q");
    }

    params.delete("tipo");
    for (const noteType of nextTypes) {
      params.append("tipo", noteType);
    }

    if (nextCourse) {
      params.set("curso", nextCourse);
    } else {
      params.delete("curso");
    }

    if (nextSemester) {
      params.set("semestre", nextSemester);
    } else {
      params.delete("semestre");
    }

    const next = params.toString();
    startTransition(() => {
      router.replace(next ? `${pathname}?${next}` : pathname);
    });
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
            id="search-page-input"
            data-jotapedia-search="active"
            type="search"
            value={query}
            onChange={(event) => setQuery(event.target.value)}
            placeholder="Escribe un concepto, autor o tema"
          />
        </label>
        <button type="submit">Buscar</button>
      </form>

      <div className="search-filters" aria-label="Filtrar resultados por tipo">
        {SEARCH_TYPES.map((noteType) => {
          const active = selectedTypes.includes(noteType);
          return (
            <button
              key={noteType}
              type="button"
              className={active ? "is-active" : undefined}
              aria-pressed={active}
              onClick={() => toggleType(noteType)}
            >
              {NOTE_TYPE_LABELS[noteType]}
            </button>
          );
        })}
        <span className="search-filters__hint">Atajo de teclado: /</span>
      </div>

      <div className="search-filters search-filters--selects" aria-label="Filtrar por contexto">
        {courseOptions.length > 0 ? (
          <label className="filter-box filter-box--compact">
            <span>Curso</span>
            <select
              value={course}
              onChange={(event) => {
                const nextCourse = event.target.value;
                setCourse(nextCourse);
                replaceSearchParams(query, selectedTypes, nextCourse, semester);
              }}
            >
              <option value="">Todos</option>
              {courseOptions.map((value) => (
                <option key={value} value={value}>
                  {value}
                </option>
              ))}
            </select>
          </label>
        ) : null}
        {semesterOptions.length > 0 ? (
          <label className="filter-box filter-box--compact">
            <span>Semestre</span>
            <select
              value={semester}
              onChange={(event) => {
                const nextSemester = event.target.value;
                setSemester(nextSemester);
                replaceSearchParams(query, selectedTypes, course, nextSemester);
              }}
            >
              <option value="">Todos</option>
              {semesterOptions.map((value) => (
                <option key={value} value={value}>
                  {value}
                </option>
              ))}
            </select>
          </label>
        ) : null}
      </div>

      {error ? <p className="empty-state">{error}</p> : null}
      {!index && !error ? (
        <p className="empty-state">Cargando indice de busqueda...</p>
      ) : null}

      {index && !query.trim() ? (
        <p className="empty-state">
          Introduce una consulta para explorar la enciclopedia.
        </p>
      ) : null}

      {index && query.trim() && results.length === 0 ? (
        <p className="empty-state">
          No se han encontrado resultados exactos para esa consulta.
        </p>
      ) : null}

      {query.trim() && suggestions.length > 0 && results.length === 0 ? (
        <section className="search-suggestions">
          <h2>Quizas buscabas</h2>
          <ul>
            {suggestions.map((result) => (
              <li key={result.route}>
                <Link href={result.route}>{result.title}</Link>
                <span>{NOTE_TYPE_LABELS[result.noteType]}</span>
              </li>
            ))}
          </ul>
        </section>
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
                  {result.aliases.length > 0 ? (
                    <span>Alias: {result.aliases.join(", ")}</span>
                  ) : null}
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

function readSelectedTypes(searchParams: ReturnType<typeof useSearchParams>): NoteType[] {
  const rawTypes = searchParams.getAll("tipo");
  const selected = rawTypes.filter((value): value is NoteType =>
    SEARCH_TYPES.includes(value as NoteType),
  );
  return selected.length > 0 ? selected : [...SEARCH_TYPES];
}

function uniqueValues(values: Array<string | undefined>): string[] {
  return [...new Set(values.filter((value): value is string => Boolean(value)))]
    .sort((left, right) => left.localeCompare(right, "es"));
}
