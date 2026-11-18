# Vicente Diablo | Música en vivo

Sitio público: https://vicente-diablo.emilianomilla.chatgpt.site

## Estado de recuperación

Sitio de artista/música en vivo. El repositorio fue creado vacío; la fuente editable de la plataforma de origen no está disponible en este repositorio y debe localizarse o reconstruirse con evidencia.

## Regla de diseño

Preservar la versión aprobada, identidad, recursos, secciones y comportamiento. No activar cobros, donaciones, formularios ni integraciones sin validar proveedores, beneficiarios y condiciones.

## Reglas de trabajo

- Leer primero `AGENTS.md`, `ia/REGLAS.md` y `ia/PROTOCOLO.md`.
- Separar fuente original recuperada, reconstrucción y propuesta; nunca etiquetar una reconstrucción como fuente original.
- No desplegar, publicar cambios en el sitio, enviar comunicaciones ni activar pagos sin autorización específica.
- Registrar cada cambio y su verificación en `CHANGELOG.md`.
- No incluir secretos, contraseñas, tokens, cookies, datos personales sensibles ni credenciales en Git. Usar variables de entorno locales ignoradas y GitHub Actions Secrets para ejecución protegida.

## Próximos pasos

1. Inventariar la versión pública y sus recursos. *(Hecho el 18/11/2026: `recuperado/2026-11-18/`.)*
2. Localizar exportaciones, archivos fuente y activos originales. *(Activos públicos recuperados; falta la fuente editable.)*
3. Recuperar la implementación exacta cuando sea posible.
4. Si la exportación no existe, reconstruir con fidelidad y documentar las diferencias.
5. Ejecutar verificaciones y registrar limitaciones antes de declarar recuperación completa.


## Qué contiene este repositorio

- `recuperado/2026-11-18/`: **recuperación parcial**. Copia de lo que el sitio publicado entrega al público (7 páginas, scripts, estilos, 9 imágenes, configuración pública) con manifiesto de hashes. Es la referencia fiel del diseño y los textos vigentes. No es la fuente editable.
- `index.html`, `contratar.html`, `apoyar.html`, `epk.html`: **reconstrucción simplificada** del 12/11/2026. No reproduce el diseño publicado (colores, tipografías y secciones distintos); su destino está pendiente de decisión.
- `legal-privacidad.html`, `legal-terminos.html`, `legal-apoyo.html`: transcripciones cotejadas con el sitio el 18/11/2026.
- `docs/AUDITORIA-2026-11-18.md`: auditoría de fondo, antecedente de Claude Design y lo que sigue.
- `docs/INSPECCION-PUBLICA.md`: inspección del 12/11/2026 con su fe de erratas.
- `pruebas/verificar.py`: verificación local (`python3 pruebas/verificar.py`).

**Alcance:** no hay fuente editable, panel administrativo, pagos ni reservas. La identidad, domicilio y contacto del prestador siguen pendientes en los documentos públicos; por eso las solicitudes y cobros permanecen deshabilitados. No se ha desplegado nada desde este repositorio.
