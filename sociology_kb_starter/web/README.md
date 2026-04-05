# Jotapedia web

Frontend estatico de Jotapedia en Next.js + Vercel. La wiki real sigue viviendo en `../data/wiki/**`; esta app solo genera artefactos derivados y no modifica el contenido fuente.

## Desarrollo

```bash
npm install
npm run dev
```

`npm run dev` regenera primero los artefactos en `web/.generated/**`.

## Build

```bash
npm run build
```

La build es estatica (`output: "export"`) y esta pensada para desplegarse en Vercel con `web/` como `rootDirectory`.

## Scripts

- `npm run wiki:generate`: compila la wiki a catalogo, indice de busqueda, mapa legacy y payloads de articulos.
- `npm run dev`: genera artefactos y arranca Next.js en desarrollo.
- `npm run build`: genera artefactos y crea la exportacion estatica.
- `npm run test`: ejecuta los tests del generador y del routing.

## Garantias

- `data/wiki/**` es la fuente de verdad y no se modifica desde esta app.
- Las rutas publicas canonicamente expuestas estan en castellano.
- La compatibilidad con enlaces legacy de Streamlit se mantiene desde la portada.
