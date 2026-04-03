# Sociology batch ready

Este paquete deja preparada una primera tanda de ingestión casi automática a partir de tus 5 PDFs.

## Contenido
- `raw/2026-s1/...` con los PDFs ya clasificados
- `import_manifest/manifest.json` con semestre, asignatura, autores y conceptos sugeridos
- `notes/by_course/...` con 5 notas fuente iniciales
- `notes/by_concept/...` y `notes/by_author/...` con semillas de la wiki

## Objetivo
Que no tengas que meter a mano metadatos básicos ni pensar la clasificación inicial.

## Siguiente automatización recomendada
1. Script que lea `import_manifest/manifest.json`
2. Copie/normalice archivos en la wiki principal
3. Recompile índices
4. Lance lint
5. Genere commit automático
