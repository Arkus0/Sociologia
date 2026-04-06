"use client";

import { useDeferredValue, useEffect, useRef, useState } from "react";
import { useRouter } from "next/navigation";

import { getEditorialTeaser } from "@/lib/editorial";
import { NOTE_TYPE_LABELS } from "@/lib/wiki-routes";
import { suggestDocuments } from "@/lib/wiki-search";
import type { SearchIndex } from "@/lib/wiki-types";

interface SearchAutocompleteProps {
  inputId: string;
  inputName: string;
  placeholder: string;
}

export function SearchAutocomplete({
  inputId,
  inputName,
  placeholder,
}: SearchAutocompleteProps) {
  const router = useRouter();
  const [query, setQuery] = useState("");
  const [index, setIndex] = useState<SearchIndex | null>(null);
  const [open, setOpen] = useState(false);
  const [highlighted, setHighlighted] = useState(-1);
  const wrapperRef = useRef<HTMLDivElement>(null);
  const deferredQuery = useDeferredValue(query);
  const normalizedQuery = deferredQuery.trim();
  const results =
    index && normalizedQuery.length >= 2
      ? suggestDocuments(index, normalizedQuery, 6)
      : [];
  const activeIndex =
    highlighted >= 0 && highlighted < results.length ? highlighted : -1;

  useEffect(() => {
    let cancelled = false;
    fetch("/generated/search-index.json")
      .then((res) => res.json())
      .then((data: SearchIndex) => {
        if (!cancelled) {
          setIndex(data);
        }
      })
      .catch(() => {});
    return () => {
      cancelled = true;
    };
  }, []);

  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (wrapperRef.current && !wrapperRef.current.contains(event.target as Node)) {
        setOpen(false);
      }
    }

    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  function handleKeyDown(event: React.KeyboardEvent) {
    if (!open || results.length === 0) return;

    if (event.key === "ArrowDown") {
      event.preventDefault();
      setHighlighted((prev) => Math.min(prev + 1, results.length - 1));
      return;
    }

    if (event.key === "ArrowUp") {
      event.preventDefault();
      setHighlighted((prev) => Math.max(prev - 1, 0));
      return;
    }

    if (event.key === "Enter" && activeIndex >= 0) {
      event.preventDefault();
      router.push(results[activeIndex].route);
      setOpen(false);
      return;
    }

    if (event.key === "Escape") {
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
        onChange={(event) => {
          const nextQuery = event.target.value;
          setQuery(nextQuery);
          setHighlighted(-1);
          setOpen(nextQuery.trim().length >= 2);
        }}
        onFocus={() => results.length > 0 && setOpen(true)}
        onKeyDown={handleKeyDown}
        data-jotapedia-search="site"
      />
      {open && results.length > 0 && (
        <ul className="search-autocomplete__dropdown" role="listbox">
          {results.map((entry, index) => (
            <li
              key={entry.route}
              className="search-autocomplete__item"
              data-highlighted={index === activeIndex ? "" : undefined}
              role="option"
              aria-selected={index === activeIndex}
              onMouseDown={() => {
                router.push(entry.route);
                setOpen(false);
              }}
              onMouseEnter={() => setHighlighted(index)}
            >
              <span className="search-autocomplete__item-title">{entry.title}</span>
              <span className="search-autocomplete__item-meta">
                {NOTE_TYPE_LABELS[entry.noteType]}
                {getEditorialTeaser(entry)
                  ? ` - ${getEditorialTeaser(entry).slice(0, 80)}${getEditorialTeaser(entry).length > 80 ? "..." : ""}`
                  : ""}
              </span>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
