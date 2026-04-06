"use client";

import { useCallback, useEffect, useRef, useState } from "react";

import { getEditorialTeaser } from "@/lib/editorial";
import { NOTE_TYPE_LABELS } from "@/lib/wiki-routes";
import type { CatalogEntry, NoteType } from "@/lib/wiki-types";

export function WikilinkTooltips() {
  const [catalog, setCatalog] = useState<CatalogEntry[] | null>(null);
  const [tooltip, setTooltip] = useState<{
    title: string;
    preview: string;
    noteType: NoteType;
    x: number;
    y: number;
  } | null>(null);
  const timeoutRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  useEffect(() => {
    let cancelled = false;
    fetch("/generated/catalog.json")
      .then((res) => res.json())
      .then((data: CatalogEntry[]) => {
        if (!cancelled) setCatalog(data);
      })
      .catch(() => {});
    return () => { cancelled = true; };
  }, []);

  const handleMouseEnter = useCallback(
    (event: MouseEvent) => {
      if (!catalog) return;
      const target = event.target as HTMLElement;
      const anchor = target.closest<HTMLAnchorElement>("a[href^='/conceptos/'], a[href^='/autores/'], a[href^='/cursos/'], a[href^='/fuentes/']");
      if (!anchor || !anchor.closest(".wiki-article-body")) return;

      const href = anchor.getAttribute("href") ?? "";
      const entry = catalog.find((e) => e.route === href);
      if (!entry) return;
      const teaser = getEditorialTeaser(entry);
      if (!teaser) return;

      if (timeoutRef.current) {
        clearTimeout(timeoutRef.current);
      }
      const rect = anchor.getBoundingClientRect();
      setTooltip({
        title: entry.title,
        preview: teaser,
        noteType: entry.noteType,
        x: rect.left + rect.width / 2,
        y: rect.top,
      });
    },
    [catalog],
  );

  const handleMouseLeave = useCallback(
    (event: MouseEvent) => {
      const target = event.target as HTMLElement;
      if (target.closest(".wiki-article-body a")) {
        timeoutRef.current = setTimeout(() => setTooltip(null), 120);
      }
    },
    [],
  );

  useEffect(() => {
    document.addEventListener("mouseover", handleMouseEnter, { passive: true });
    document.addEventListener("mouseout", handleMouseLeave, { passive: true });
    return () => {
      document.removeEventListener("mouseover", handleMouseEnter);
      document.removeEventListener("mouseout", handleMouseLeave);
    };
  }, [handleMouseEnter, handleMouseLeave]);

  if (!tooltip) return null;

  return (
    <div
      className="wiki-tooltip"
      style={{
        position: "fixed",
        left: `${tooltip.x}px`,
        top: `${tooltip.y - 8}px`,
        transform: "translateX(-50%) translateY(-100%)",
      }}
    >
      <p className="wiki-tooltip__type">{NOTE_TYPE_LABELS[tooltip.noteType]}</p>
      <p className="wiki-tooltip__title">{tooltip.title}</p>
      <p className="wiki-tooltip__preview">{tooltip.preview}</p>
    </div>
  );
}
