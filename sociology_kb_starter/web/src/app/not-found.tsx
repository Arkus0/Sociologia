import Link from "next/link";

export default function NotFound() {
  return (
    <section className="index-page">
      <header className="page-header">
        <h1>Pagina no encontrada</h1>
        <p>
          La entrada que buscas no existe o todavia no ha sido generada en esta
          version de Jotapedia.
        </p>
      </header>
      <p className="empty-state">
        Vuelve a la <Link href="/">portada</Link> o navega por{" "}
        <Link href="/conceptos">conceptos</Link>, <Link href="/autores">autores</Link>{" "}
        y <Link href="/fuentes">fuentes</Link>.
      </p>
    </section>
  );
}
