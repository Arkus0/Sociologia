"use client";

import { useState } from "react";
import Link from "next/link";

import { normalizeText, slugifyText } from "@/lib/wiki-text";
import type { CatalogEntry } from "@/lib/wiki-types";

export function SourcesIndexView({ entries }: { entries: CatalogEntry[] }) {
  const [query, setQuery] = useState("");
  const normalizedQuery = normalizeText(query);
  const filtered = entries.filter((entry) => {
    if (!normalizedQuery) {
      return true;
    }

    const haystack = normalizeText(
      [
        entry.title,
        entry.preview,
        entry.course,
        entry.semester,
        entry.canonicalTitle,
        ...entry.aliases,
      ]
        .filter(Boolean)
        .join(" "),
    );
    return haystack.includes(normalizedQuery);
  });

  const grouped = groupSources(filtered);

  return (
    <section className="index-page">
      <header className="page-header">
        <h1>Fuentes</h1>
        <p>
          Materiales de curso, modulos y notas fuente organizados por semestre y
          asignatura.
        </p>
      </header>

      <div className="page-toolbar">
        <label className="filter-box">
          <span>Filtrar fuentes</span>
          <input
            type="search"
            value={query}
            onChange={(event) => setQuery(event.target.value)}
            placeholder="Buscar por titulo, semestre o curso"
          />
        </label>
        <p className="page-toolbar__count">
          {filtered.length} {filtered.length === 1 ? "fuente" : "fuentes"}
        </p>
      </div>

      {filtered.length === 0 ? (
        <p className="empty-state">
          No hay fuentes que coincidan con ese filtro.
        </p>
      ) : (
        <div className="sources-groups">
          {grouped.map(([semester, courses]) => (
            <section
              key={semester}
              className="sources-semester"
              id={slugifyText(semester)}
            >
              <h2>{semester}</h2>
              {courses.map(([course, courseEntries]) => (
                <section
                  key={`${semester}-${course}`}
                  className="sources-course"
                  id={slugifyText(`${semester}-${course}`)}
                >
                  <h3>{course}</h3>
                  <ul>
                    {courseEntries.map((entry) => (
                      <li key={entry.route} className="index-card">
                        <Link href={entry.route}>{entry.title}</Link>
                        <p>{entry.preview}</p>
                        <div className="index-card__meta">
                          {entry.backlinkCount > 0 ? (
                            <span>
                              {entry.backlinkCount}{" "}
                              {entry.backlinkCount === 1
                                ? "entrada relacionada"
                                : "entradas relacionadas"}
                            </span>
                          ) : null}
                        </div>
                      </li>
                    ))}
                  </ul>
                </section>
              ))}
            </section>
          ))}
        </div>
      )}
    </section>
  );
}

function groupSources(entries: CatalogEntry[]) {
  const semesters = new Map<string, Map<string, CatalogEntry[]>>();

  for (const entry of entries) {
    const semester = entry.semester ?? "Sin semestre";
    const course = entry.course ?? "Sin curso";
    const semesterMap = semesters.get(semester) ?? new Map<string, CatalogEntry[]>();
    semesterMap.set(course, [...(semesterMap.get(course) ?? []), entry]);
    semesters.set(semester, semesterMap);
  }

  return [...semesters.entries()]
    .sort(([left], [right]) => right.localeCompare(left, "es"))
    .map(([semester, courses]) => [
      semester,
      [...courses.entries()].sort(([left], [right]) =>
        left.localeCompare(right, "es"),
      ),
    ] as const);
}
