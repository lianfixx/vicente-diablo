# Copia recuperada del sitio publicado · 18 de noviembre de 2026

**Qué es:** recuperación parcial. Es la salida compilada que el sitio
https://vicente-diablo.emilianomilla.chatgpt.site entrega a cualquier visitante, descargada en
solo lectura. **No es la fuente editable** (componentes, servidor, base de datos y configuración
siguen en la plataforma de origen).

| Carpeta | Contenido |
|---|---|
| `sitio/` | Las 7 páginas públicas (`/`, `/contratar`, `/apoyar`, `/epk`, `/legal/privacidad`, `/legal/terminos`, `/legal/apoyo`), sus scripts y estilos (`assets/`), las 9 imágenes (`images/`), `favicon.svg`, `og.png`, `robots.txt`, `sitemap.xml`, `manifest.webmanifest` y las tres respuestas públicas de `api/public/` (configuración, fechas y tarifas). |
| `texto-renderizado/` | Texto visible de cada página después de cargar en navegador. Los textos legales se cargan por script, así que aquí está su redacción íntegra. |
| `MANIFIESTO.sha256` | Hash SHA-256 de cada archivo. `python3 pruebas/verificar.py` lo comprueba. |

## Cómo verla

```
cd recuperado/2026-11-18/sitio && python3 -m http.server 8000
```

Abrir http://localhost:8000. Debe servirse desde la raíz porque las rutas son absolutas.

## Límites conocidos

- Sin servidor no responden `/api/*` ni la navegación interna `*.rsc`; cada página abre bien si se
  carga directamente. Calendario, cotizador, pagos y recepción de solicitudes no funcionan aquí.
- No se descargó `/admin` ni `/pago` (el sitio los excluye en `robots.txt`) y no se inició sesión.
- El HTML conserva una etiqueta de Cloudflare (`/cdn-cgi/...`) que la red añade al servir; en local da 404 sin efecto.
- Estado observado en `api/public/config.json`: reservas y aportaciones deshabilitadas; operador,
  domicilio y contacto vacíos; sin fechas ni tarifas publicadas.
- Las fotografías y portadas pertenecen a sus titulares. Están aquí como evidencia de recuperación
  porque ya son públicas en el sitio; su uso en otros materiales requiere la autorización que el
  propio EPK pide.
