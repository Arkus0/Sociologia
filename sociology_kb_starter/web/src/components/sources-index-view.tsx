"use client";

import { useState } from "react";
import Link from "next/link";

import { normalizeText, slugifyText } from "@/lib/wiki-text";
import type { CatalogEntry } from "@/lib/wiki-types";

export function SourcesIndexView({ entries }: { entries: CatalogEntry[] }) {
  const [query, setQuery] = useState("");
  const [course, setCourse] = useState("");
  const [semester, setSemester] = useState("");
  const normalizedQuery = normalizeText(query);
  const courses = uniqueValues(entries.map((entry) => entry.course));
  const semesters = uniqueValues(entries.map((entry) => entry.semester));
  const filtered = entries.filter((entry) => {
    if (course && entry.course !== course) {
      return false;
    }

    if (semester && entry.semester !== semester) {
      return false;
    }

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
        <div className="page-toolbar__filters">
          <label className="filter-box">
            <span>Filtrar fuentes</span>
            <input
              type="search"
              value={query}
              onChange={(event) => setQuery(event.target.value)}
              placeholder="Buscar por titulo, semestre o curso"
            />
          </label>
          <label className="filter-box filter-box--compact">
            <span>Curso</span>
            <select value={course} onChange={(event) => setCourse(event.target.value)}>
              <option value="">Todos</option>
              {courses.map((value) => (
                <option key={value} value={value}>
                  {value}
                </option>
              ))}
            </select>
          </label>
          <label className="filter-box filter-box--compact">
            <span>Semestre</span>
            <select value={semester} onChange={(event) => setSemester(event.target.value)}>
              <option value="">Todos</option>
              {semesters.map((value) => (
                <option key={value} value={value}>
                  {value}
                </option>
              ))}
            </select>
          </label>
        </div>
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

function uniqueValues(values: Array<string | undefined>): string[] {
  return [...new Set(values.filter((value): value is string => Boolean(value)))]
    .sort((left, right) => left.localeCompare(right, "es"));
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
