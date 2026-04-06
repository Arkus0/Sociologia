"use client";

import { useEffect, useEffectEvent } from "react";

export function SearchShortcut() {
  const handleKeyDown = useEffectEvent((event: KeyboardEvent) => {
    if (
      event.key !== "/" ||
      event.altKey ||
      event.ctrlKey ||
      event.metaKey ||
      event.shiftKey
    ) {
      return;
    }

    const target = event.target as HTMLElement | null;
    if (
      target instanceof HTMLInputElement ||
      target instanceof HTMLTextAreaElement ||
      target?.isContentEditable
    ) {
      return;
    }

    const input =
      document.querySelector<HTMLInputElement>("[data-jotapedia-search='active']") ??
      document.querySelector<HTMLInputElement>("[data-jotapedia-search='site']");

    if (!input) {
      return;
    }

    event.preventDefault();
    input.focus();
    input.select();
  });

  useEffect(() => {
    window.addEventListener("keydown", handleKeyDown);
    return () => {
      window.removeEventListener("keydown", handleKeyDown);
    };
  }, []);

  return null;
}
