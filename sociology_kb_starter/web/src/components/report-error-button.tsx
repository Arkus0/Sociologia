"use client";

import { useCallback, useRef, useState } from "react";

interface Props {
  title: string;
  route: string;
}

export function ReportErrorButton({ title, route }: Props) {
  const [open, setOpen] = useState(false);
  const [success, setSuccess] = useState(false);
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  const handleSubmit = useCallback(
    async (e: React.FormEvent) => {
      e.preventDefault();
      const desc = textareaRef.current?.value.trim() ?? "";
      if (desc.length < 10) return;

      const text = [
        `[Error reportado]`,
        `Articulo: ${title}`,
        `Ruta: ${route}`,
        `Descripcion: ${desc}`,
      ].join("\n");

      try {
        await navigator.clipboard.writeText(text);
      } catch {
        const ta = document.createElement("textarea");
        ta.value = text;
        ta.style.position = "fixed";
        ta.style.opacity = "0";
        document.body.appendChild(ta);
        ta.select();
        document.execCommand("copy");
        document.body.removeChild(ta);
      }

      setSuccess(true);
      setTimeout(() => {
        setOpen(false);
        setSuccess(false);
        if (textareaRef.current) textareaRef.current.value = "";
      }, 3000);
    },
    [title, route],
  );

  if (success) {
    return (
      <div className="report-error">
        <p className="report-error__success">
          ✓ Copiado al portapapeles — pegalo en un mensaje al equipo
        </p>
      </div>
    );
  }

  return (
    <div className="report-error">
      {!open ? (
        <button
          type="button"
          className="report-error__trigger"
          onClick={() => setOpen(true)}
        >
          ⚠️ Informar de un error
        </button>
      ) : (
        <form className="report-error__form" onSubmit={handleSubmit}>
          <label>
            Describe el error que has encontrado
            <textarea
              ref={textareaRef}
              required
              minLength={10}
              placeholder="Escribe al menos 10 caracteres..."
            />
          </label>
          <div className="report-error__actions">
            <button type="submit">Enviar</button>
            <button
              type="button"
              onClick={() => {
                setOpen(false);
                if (textareaRef.current) textareaRef.current.value = "";
              }}
            >
              Cancelar
            </button>
          </div>
        </form>
      )}
    </div>
  );
}
