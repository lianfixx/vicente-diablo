# Reglas de este repositorio

- Preservar el diseño y el comportamiento vigentes; cualquier cambio visual debe estar expresamente solicitado.
- No sustituir fuentes originales por una implementación parcial sin etiquetarla como reconstrucción.
- No afirmar recuperación completa sin inventario de código, recursos, dependencias, configuración y pruebas.
- No inventar hechos ni completar huecos con datos supuestos.
- No desplegar, publicar en el sitio, activar integraciones o realizar envíos a terceros sin autorización específica.
- Prohibido incluir secretos, tokens activos, contraseñas, cookies de sesión, claves privadas o datos personales sensibles en Git. La visibilidad pública amplifica el riesgo y el historial conserva valores eliminados.
- Guardar secretos de ejecución en variables de entorno locales ignoradas o en GitHub Actions Secrets/entornos protegidos; versionar solo nombres y ejemplos ficticios en `.env.example`.
- No forzar ni borrar ramas o historial remoto; no saltar controles de seguridad.
- Registrar cada cambio en `CHANGELOG.md` en el mismo commit, con la línea `Agente:`.
- Antes de declarar listo, ejecutar las pruebas disponibles y reportar lo no verificable.

## Qué se aplica solo (desde el 25/11/2026)

GitHub corre `python3 ia/verificar.py ci` en cada push y pull request (workflow `control-ia.yml`): el cambio debe actualizar `CHANGELOG.md` con una entrada que traiga la línea `- Agente:`, y lo que agrega no puede traer llaves, contraseñas, CURP, tarjetas ni archivos de credenciales (`.env`, `.pem`, `credentials.json`). Solo revisa lo que el cambio agrega; marca en rojo y no revierte. Lo demás de estas reglas lo cumple cada IA por sí misma. Al empezar con terminal: `python3 ia/verificar.py inicio`.
