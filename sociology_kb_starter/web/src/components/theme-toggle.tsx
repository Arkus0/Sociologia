"use client";

import { useEffect, useState } from "react";

type Theme = "light" | "dark";

export function ThemeToggle() {
  const [theme, setTheme] = useState<Theme>(getInitialTheme);

  useEffect(() => {
    document.documentElement.setAttribute("data-theme", theme);
    localStorage.setItem("jotapedia-theme", theme);
  }, [theme]);

  function toggle() {
    setTheme((current) => (current === "light" ? "dark" : "light"));
  }

  return (
    <button
      className="theme-toggle"
      onClick={toggle}
      aria-label={theme === "light" ? "Activar modo oscuro" : "Activar modo claro"}
      title={theme === "light" ? "Modo oscuro" : "Modo claro"}
      suppressHydrationWarning
    >
      {theme === "light" ? "Claro" : "Oscuro"}
    </button>
  );
}

function getInitialTheme(): Theme {
  if (typeof window === "undefined") {
    return "light";
  }

  const stored = localStorage.getItem("jotapedia-theme");
  if (stored === "dark" || stored === "light") {
    return stored;
  }

  return window.matchMedia("(prefers-color-scheme: dark)").matches
    ? "dark"
    : "light";
}
