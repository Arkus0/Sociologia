"use client";

import { useState } from "react";
import Link from "next/link";

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
  const normalizedQuery = normalizeText(query);
  const filtered = entries.filter((entry) => {
    if (!normalizedQuery) {
      return true;
    }

    const haystack = normalizeText(
      [entry.title, entry.preview, entry.course, entry.semester].filter(Boolean).join(" "),
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
                    <p>{entry.preview}</p>
                    <span>{NOTE_TYPE_LABELS[entry.noteType]}</span>
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
