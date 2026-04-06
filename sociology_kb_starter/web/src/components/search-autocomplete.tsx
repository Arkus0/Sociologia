"use client";

import { useEffect, useRef, useState } from "react";
import { useRouter } from "next/navigation";

import { NOTE_TYPE_LABELS } from "@/lib/wiki-routes";
import { suggestDocuments } from "@/lib/wiki-search";
import type { SearchEntry, SearchIndex } from "@/lib/wiki-types";

interface SearchAutocompleteProps {
  inputId: string;
  inputName: string;
  placeholder: string;
  formAction?: string;
}

export function SearchAutocomplete({
  inputId,
  inputName,
  placeholder,
  formAction = "/buscar",
}: SearchAutocompleteProps) {
  const router = useRouter();
  const [query, setQuery] = useState("");
  const [index, setIndex] = useState<SearchIndex | null>(null);
  const [results, setResults] = useState<SearchEntry[]>([]);
  const [open, setOpen] = useState(false);
  const [highlighted, setHighlighted] = useState(-1);
  const wrapperRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    let cancelled = false;
    fetch("/generated/search-index.json")
      .then((res) => res.json())
      .then((data: SearchIndex) => {
        if (!cancelled) setIndex(data);
      })
      .catch(() => {});
    return () => { cancelled = true; };
  }, []);

  useEffect(() => {
    if (!index || query.trim().length < 2) {
      setResults([]);
      setOpen(false);
      return;
    }
    const suggestions = suggestDocuments(index, query.trim(), 6);
    setResults(suggestions);
    setOpen(suggestions.length > 0);
    setHighlighted(-1);
  }, [query, index]);

  useEffect(() => {
    function handleClickOutside(e: MouseEvent) {
      if (wrapperRef.current && !wrapperRef.current.contains(e.target as Node)) {
        setOpen(false);
      }
    }
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  function handleKeyDown(e: React.KeyboardEvent) {
    if (!open || results.length === 0) return;
    if (e.key === "ArrowDown") {
      e.preventDefault();
      setHighlighted((prev) => Math.min(prev + 1, results.length - 1));
    } else if (e.key === "ArrowUp") {
      e.preventDefault();
      setHighlighted((prev) => Math.max(prev - 1, 0));
    } else if (e.key === "Enter" && highlighted >= 0) {
      e.preventDefault();
      router.push(results[highlighted].route);
      setOpen(false);
    } else if (e.key === "Escape") {
      setOpen(false);
    }
  }

  return (
    <div className="search-autocomplete" ref={wrapperRef}>
      <input
        id={inputId}
        name={inputName}
        type="search"
        placeholder={placeholder}
        autoComplete="off"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        onFocus={() => results.length > 0 && setOpen(true)}
        onKeyDown={handleKeyDown}
        data-jotapedia-search="site"
      />
      {open && results.length > 0 && (
        <ul className="search-autocomplete__dropdown" role="listbox">
          {results.map((entry, i) => (
            <li
              key={entry.route}
              className="search-autocomplete__item"
              data-highlighted={i === highlighted ? "" : undefined}
              role="option"
              aria-selected={i === highlighted}
              onMouseDown={() => {
                router.push(entry.route);
                setOpen(false);
              }}
              onMouseEnter={() => setHighlighted(i)}
            >
              <span className="search-autocomplete__item-title">{entry.title}</span>
              <span className="search-autocomplete__item-meta">
                {NOTE_TYPE_LABELS[entry.noteType]}
                {entry.preview ? ` · ${entry.preview.slice(0, 80)}…` : ""}
              </span>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
