"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

const PRIMARY_LINKS = [
  { href: "/", label: "Portada" },
  { href: "/conceptos", label: "Conceptos" },
  { href: "/autores", label: "Autores" },
  { href: "/cursos", label: "Cursos" },
  { href: "/fuentes", label: "Fuentes" },
  { href: "/grafo", label: "Grafo de conocimiento" },
  { href: "/stats", label: "Estadisticas" },
  { href: "/buscar", label: "Buscar" },
  { href: "/aleatoria", label: "🎲 Articulo aleatorio" },
];

export function PrimaryNav() {
  const pathname = usePathname();

  return (
    <nav className="portal-navigation" aria-label="Navegacion principal">
      <section className="portal-navigation__group">
        <h2>Navegacion</h2>
        <ul>
          {PRIMARY_LINKS.map((link) => {
            const active =
              link.href === "/"
                ? pathname === "/"
                : pathname === link.href || pathname.startsWith(`${link.href}/`);

            return (
              <li key={link.href}>
                <Link
                  href={link.href}
                  className={active ? "is-active" : undefined}
                >
                  {link.label}
                </Link>
              </li>
            );
          })}
        </ul>
      </section>

      <section className="portal-navigation__group">
        <h2>Proyecto</h2>
        <p>
          Jotapedia es una enciclopedia sociologica generada a partir de la wiki
          local del repositorio.
        </p>
      </section>
    </nav>
  );
}
