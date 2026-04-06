"use client";

import { useMemo, useState } from "react";
import Link from "next/link";

import { NOTE_TYPE_LABELS } from "@/lib/wiki-routes";
import { normalizeText } from "@/lib/wiki-text";
import type { QualityIssue, QualityReport } from "@/lib/wiki-types";

const KIND_LABELS: Record<QualityIssue["kind"], string> = {
  broken_reference: "Referencia rota",
  ambiguous_reference: "Referencia ambigua",
  missing_course: "Curso ausente",
  course_variant: "Variante de curso",
  thin_entry: "Entrada breve",
  missing_required_section: "Secciones obligatorias",
  missing_related_concepts: "related_concepts insuficiente",
  orphan_entry: "Entrada huerfana",
  thin_preview: "Preview breve",
};

export function QualityReportView({ report }: { report: QualityReport }) {
  const [query, setQuery] = useState("");
  const [kind, setKind] = useState("");
  const [noteType, setNoteType] = useState("");

  const kinds = useMemo(
    () =>
      [...new Set(report.issues.map((issue) => issue.kind))]
        .sort((left, right) => KIND_LABELS[left].localeCompare(KIND_LABELS[right], "es")),
    [report.issues],
  );
  const noteTypes = useMemo(
    () =>
      [...new Set(report.issues.map((issue) => issue.documentNoteType).filter(Boolean))]
        .sort((left, right) =>
          NOTE_TYPE_LABELS[left as keyof typeof NOTE_TYPE_LABELS].localeCompare(
            NOTE_TYPE_LABELS[right as keyof typeof NOTE_TYPE_LABELS],
            "es",
          ),
        ),
    [report.issues],
  );

  const normalizedQuery = normalizeText(query);
  const filtered = report.issues.filter((issue) => {
    if (kind && issue.kind !== kind) {
      return false;
    }

    if (noteType && issue.documentNoteType !== noteType) {
      return false;
    }

    if (!normalizedQuery) {
      return true;
    }

    const haystack = normalizeText(
      [issue.documentTitle, issue.detail, issue.reference, issue.documentRoute]
        .filter(Boolean)
        .join(" "),
    );
    return haystack.includes(normalizedQuery);
  });

  return (
    <section className="quality-page">
      <header className="page-header">
        <h1>Calidad editorial</h1>
        <p>
          Panel operativo basado en el reporte de compilacion. Permite localizar
          deuda editorial por articulo, tipo de incidencia y referencia.
        </p>
      </header>

      <div className="stats-grid">
        <div className="stat-card">
          <span className="stat-card__value">{report.summary.issues}</span>
          <span className="stat-card__label">Incidencias totales</span>
        </div>
        {Object.entries(report.summary.byKind)
          .sort((left, right) => right[1] - left[1])
          .slice(0, 4)
          .map(([issueKind, count]) => (
            <div className="stat-card" key={issueKind}>
              <span className="stat-card__value">{count}</span>
              <span className="stat-card__label">
                {KIND_LABELS[issueKind as QualityIssue["kind"]]}
              </span>
            </div>
          ))}
      </div>

      <div className="page-toolbar">
        <div className="page-toolbar__filters">
          <label className="filter-box">
            <span>Buscar articulo o referencia</span>
            <input
              type="search"
              value={query}
              onChange={(event) => setQuery(event.target.value)}
              placeholder="Titulo, ruta o referencia"
            />
          </label>
          <label className="filter-box filter-box--compact">
            <span>Tipo de incidencia</span>
            <select value={kind} onChange={(event) => setKind(event.target.value)}>
              <option value="">Todas</option>
              {kinds.map((value) => (
                <option key={value} value={value}>
                  {KIND_LABELS[value]}
                </option>
              ))}
            </select>
          </label>
          <label className="filter-box filter-box--compact">
            <span>Tipo de entrada</span>
            <select value={noteType} onChange={(event) => setNoteType(event.target.value)}>
              <option value="">Todos</option>
              {noteTypes.map((value) => (
                <option key={value} value={value}>
                  {NOTE_TYPE_LABELS[value as keyof typeof NOTE_TYPE_LABELS]}
                </option>
              ))}
            </select>
          </label>
        </div>
        <p className="page-toolbar__count">
          {filtered.length} {filtered.length === 1 ? "incidencia" : "incidencias"}
        </p>
      </div>

      <div className="home-grid">
        <section className="stats-ranking">
          <h2>Documentos prioritarios</h2>
          <ol>
            {report.backlog.topDocuments.slice(0, 15).map((entry) => (
              <li key={entry.route}>
                <Link href={entry.route}>{entry.title}</Link>
                <span>
                  {NOTE_TYPE_LABELS[entry.noteType]} · {entry.count} incidencias
                </span>
              </li>
            ))}
          </ol>
        </section>

        <section className="stats-ranking">
          <h2>Referencias recurrentes</h2>
          <ol>
            {report.backlog.topReferences.slice(0, 15).map((entry) => (
              <li key={entry.reference}>
                <span className="quality-reference">{entry.reference}</span>
                <span>{entry.count} incidencias</span>
              </li>
            ))}
          </ol>
        </section>
      </div>

      <section className="search-results">
        <h2 className="quality-page__results-title">Incidencias detalladas</h2>
        <ul>
          {filtered.map((issue, index) => (
            <li key={`${issue.documentRoute ?? "global"}-${issue.kind}-${issue.detail}-${index}`} className="search-result quality-issue">
              <div className="quality-issue__header">
                <strong>{KIND_LABELS[issue.kind]}</strong>
                <span>Prioridad {issue.priority}</span>
              </div>
              {issue.documentRoute ? (
                <p>
                  <Link href={issue.documentRoute}>{issue.documentTitle}</Link>
                  {issue.documentNoteType ? (
                    <span className="quality-issue__meta">
                      {NOTE_TYPE_LABELS[issue.documentNoteType]}
                    </span>
                  ) : null}
                </p>
              ) : null}
              <p>{issue.detail}</p>
            </li>
          ))}
        </ul>
      </section>
    </section>
  );
}
