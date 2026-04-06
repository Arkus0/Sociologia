"use client";

import { useState } from "react";

interface ShareBarProps {
  title: string;
  path: string;
}

export function ShareBar({ title, path }: ShareBarProps) {
  const [copied, setCopied] = useState(false);

  const fullUrl = typeof window !== "undefined"
    ? `${window.location.origin}${path}`
    : path;

  const twitterUrl = `https://twitter.com/intent/tweet?text=${encodeURIComponent(title)}&url=${encodeURIComponent(fullUrl)}`;
  const whatsappUrl = `https://wa.me/?text=${encodeURIComponent(`${title} ${fullUrl}`)}`;

  async function copyLink() {
    try {
      await navigator.clipboard.writeText(fullUrl);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch {
      // Fallback: do nothing
    }
  }

  return (
    <div className="share-bar">
      <a
        href={twitterUrl}
        target="_blank"
        rel="noopener noreferrer"
        aria-label="Compartir en Twitter"
      >
        𝕏 Compartir
      </a>
      <a
        href={whatsappUrl}
        target="_blank"
        rel="noopener noreferrer"
        aria-label="Compartir en WhatsApp"
      >
        💬 WhatsApp
      </a>
      <button onClick={copyLink} aria-label="Copiar enlace">
        {copied ? "✓ Copiado" : "🔗 Copiar enlace"}
      </button>
    </div>
  );
}
