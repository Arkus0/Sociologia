"use client";

import { useState } from "react";
import Link from "next/link";

import { getEditorialTeaser } from "@/lib/editorial";
import { NOTE_TYPE_LABELS } from "@/lib/wiki-routes";
import { normalizeText } from "@/lib/wiki-text";
import type { CatalogEntry } from "@/lib/wiki-types";

interface IndexViewProps {
  title: string;
  description: string;
  entries: CatalogEntry[];
  emptyMessage: string;
}

export function IndexView({
  title,
  description,
  entries,
  emptyMessage,
}: IndexViewProps) {
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
        entry.hook,
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

  const groups = groupEntries(filtered);

  return (
    <section className="index-page">
      <header className="page-header">
        <h1>{title}</h1>
        <p>{description}</p>
      </header>

      <div className="page-toolbar">
        <div className="page-toolbar__filters">
          <label className="filter-box">
            <span>Filtrar indice</span>
            <input
              type="search"
              name="filtro"
              value={query}
              onChange={(event) => setQuery(event.target.value)}
              placeholder={`Buscar dentro de ${title.toLowerCase()}`}
            />
          </label>
          {courses.length > 0 ? (
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
          ) : null}
          {semesters.length > 0 ? (
            <label className="filter-box filter-box--compact">
              <span>Semestre</span>
              <select
                value={semester}
                onChange={(event) => setSemester(event.target.value)}
              >
                <option value="">Todos</option>
                {semesters.map((value) => (
                  <option key={value} value={value}>
                    {value}
                  </option>
                ))}
              </select>
            </label>
          ) : null}
        </div>
        <p className="page-toolbar__count">
          {filtered.length} {filtered.length === 1 ? "entrada" : "entradas"}
        </p>
      </div>

      {filtered.length === 0 ? (
        <p className="empty-state">{emptyMessage}</p>
      ) : (
        <div className="index-groups">
          {groups.map(([letter, items]) => (
            <section key={letter} className="index-group">
              <h2>{letter}</h2>
              <ul>
                {items.map((entry) => (
                  <li key={entry.route} className="index-card">
                    <Link href={entry.route}>{entry.title}</Link>
                    <p>{getEditorialTeaser(entry)}</p>
                    <div className="index-card__meta">
                      <span>{NOTE_TYPE_LABELS[entry.noteType]}</span>
                      {entry.isAlias ? (
                        <span>Alias de {entry.canonicalTitle}</span>
                      ) : null}
                      {entry.backlinkCount > 0 ? (
                        <span>
                          {entry.backlinkCount}{" "}
                          {entry.backlinkCount === 1 ? "enlace entrante" : "enlaces entrantes"}
                        </span>
                      ) : null}
                    </div>
                  </li>
                ))}
              </ul>
            </section>
          ))}
        </div>
      )}
    </section>
  );
}

function groupEntries(entries: CatalogEntry[]): Array<[string, CatalogEntry[]]> {
  const groups = new Map<string, CatalogEntry[]>();

  for (const entry of entries) {
    const letter = entry.title.charAt(0).toUpperCase() || "#";
    groups.set(letter, [...(groups.get(letter) ?? []), entry]);
  }

  return [...groups.entries()].sort(([left], [right]) => left.localeCompare(right, "es"));
}

function uniqueValues(values: Array<string | undefined>): string[] {
  return [...new Set(values.filter((value): value is string => Boolean(value)))]
    .sort((left, right) => left.localeCompare(right, "es"));
}
