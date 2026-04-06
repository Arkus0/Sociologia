import type { Metadata } from "next";
import Link from "next/link";
import { Source_Sans_3, Source_Serif_4 } from "next/font/google";

import { PrimaryNav } from "@/components/primary-nav";
import { SearchShortcut } from "@/components/search-shortcut";
import { ThemeToggle } from "@/components/theme-toggle";
import { WikilinkTooltips } from "@/components/wikilink-tooltips";
import { SearchAutocomplete } from "@/components/search-autocomplete";

import "./globals.css";

const uiSans = Source_Sans_3({
  variable: "--font-ui",
  subsets: ["latin"],
});

const readingSerif = Source_Serif_4({
  variable: "--font-reading",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Jotapedia",
  description: "Enciclopedia sociologica en castellano construida sobre la wiki del repositorio.",
  metadataBase: new URL(resolveSiteUrl()),
  alternates: {
    types: {
      "application/rss+xml": "/generated/feed.xml",
    },
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="es" className={`${uiSans.variable} ${readingSerif.variable}`}>
      <body>
        <SearchShortcut />
        <WikilinkTooltips />
        <a className="skip-link" href="#contenido">
          Saltar al contenido
        </a>
        <div className="site-frame">
          <header className="site-header">
            <div className="site-header__brand">
              <p className="site-header__eyebrow">Enciclopedia sociologica</p>
              <Link href="/" className="site-header__title">
                Jotapedia
              </Link>
              <p className="site-header__tagline">
                Una wikipedia propia para conceptos, autores, cursos y fuentes.
              </p>
            </div>

            <div className="site-header__actions">
              <form action="/buscar" className="site-search">
                <label htmlFor="site-search-input">Buscar</label>
                <div className="site-search__controls">
                  <SearchAutocomplete
                    inputId="site-search-input"
                    inputName="q"
                    placeholder="Buscar en Jotapedia"
                  />
                  <button type="submit">Ir</button>
                  <ThemeToggle />
                </div>
              </form>

              <nav className="site-header__links" aria-label="Accesos rapidos">
                <Link href="/conceptos">Conceptos</Link>
                <Link href="/autores">Autores</Link>
                <Link href="/cursos">Cursos</Link>
                <Link href="/fuentes">Fuentes</Link>
                <Link href="/grafo">Grafo</Link>
                <Link href="/stats">Stats</Link>
                <a href="/generated/feed.xml" className="rss-link" title="Suscribirse via RSS" target="_blank" rel="noopener noreferrer">
                  RSS
                </a>
              </nav>
            </div>
          </header>

          <div className="site-main">
            <aside className="site-sidebar">
              <PrimaryNav />
            </aside>
            <main id="contenido" className="site-content">
              {children}
            </main>
          </div>
        </div>
      </body>
    </html>
  );
}

function resolveSiteUrl(): string {
  const candidate =
    process.env.NEXT_PUBLIC_SITE_URL ||
    process.env.VERCEL_PROJECT_PRODUCTION_URL ||
    process.env.VERCEL_URL;

  if (!candidate) {
    return "http://localhost:3000";
  }

  return candidate.startsWith("http") ? candidate : `https://${candidate}`;
}
