# Registro de cambios

## 2026-11-18 · Auditoría de fondo, copia fiel del sitio publicado y correcciones
- Agente: Claude Code
- Solicitud: Emi, 18/11/2026, en sesión de Claude Code: leer todo, auditar de fondo (incluido el trabajo previo en Claude Design), arreglar e indicar lo que sigue.
- Cambios: (1) se descargó en solo lectura la salida compilada del sitio publicado (7 páginas, scripts, estilos, 9 imágenes y configuración pública) con manifiesto de hashes; es recuperación parcial, no fuente editable. (2) Se corrigieron encabezados e introducciones de las tres transcripciones legales para que coincidan con el sitio; el cuerpo ya coincidía. (3) La portada reconstruida usa las imágenes recuperadas en lugar de enlazarlas al sitio de origen; enlaces externos con `rel="noopener noreferrer"`; `&` escapado en el EPK; el enlace al aviso de privacidad del formulario ya no se dibuja como botón. (4) Se documentó la auditoría: la reconstrucción de la raíz no es fiel al diseño publicado, fe de erratas de la inspección del 12/11, antecedente de Claude Design y piezas del protocolo que faltan. (5) Se añadió una verificación local. (6) Este registro se reordenó de lo más reciente a lo más antiguo, como pide `ia/PROTOCOLO.md`; el texto de las entradas anteriores no cambió.
- Archivos: `recuperado/2026-11-18/` (nuevo), `docs/AUDITORIA-2026-11-18.md` (nuevo), `pruebas/verificar.py` (nuevo), `index.html`, `contratar.html`, `epk.html`, `legal-privacidad.html`, `legal-terminos.html`, `legal-apoyo.html`, `docs/INSPECCION-PUBLICA.md`, `README.md`, `CHANGELOG.md`.
- Verificación: `python3 pruebas/verificar.py` → aprobado; comparación visual en navegador de la copia contra el sitio (portada, 1280 px) → idéntica; cotejo frase por frase de los textos legales contra el sitio → cuerpo coincidente tras la corrección; `python3 ia/verificar.py inicio` → no ejecutado (el archivo no existe en este repositorio); revisión jurídica independiente → no ejecutada.
- Pendiente: obtener la fuente editable de la plataforma de origen; decidir si la reconstrucción simplificada de la raíz se conserva o se retira; instalar las piezas comunes del protocolo; datos del prestador y de Vicente antes de habilitar solicitudes o cobros. Detalle en `docs/AUDITORIA-2026-11-18.md`.


## 2026-11-12 · README actualizado
- Agente: ChatGPT (GPT-6)
- Solicitud: recuperar y documentar los seis sitios web.
- Cambios: el README enumera los archivos implementados y distingue reconstrucción de fuente original, integraciones desactivadas y pendientes.
- Archivos: `README.md`.
- Verificación: actualización en GitHub → confirmada; ejecución de build y comparación visual → no ejecutadas.
- Pendiente: validar en navegador y completar recuperación de activos originales.


## 2026-11-12 · Documentos legales públicos y navegación local
- Agente: ChatGPT (GPT-6)
- Solicitud: recuperar páginas públicas de Vicente Diablo y conservar estado operativo.
- Cambios: se incorporaron transcripciones del aviso de privacidad, términos de contratación y condiciones del apoyo voluntario (versión 11/09/2026); navegación local desde portada, contratación y apoyo.
- Archivos: `legal-privacidad.html`, `legal-terminos.html`, `legal-apoyo.html`, `index.html`, `apoyar.html`, `contratar.html`.
- Verificación: escrituras en GitHub → confirmadas; revisión legal independiente y pruebas de navegación → no ejecutadas.
- Pendiente: confirmar identidad/domicilio/contacto del prestador antes de habilitar solicitudes o cobros; mantener pagos deshabilitados.


## 2026-11-12 · Protección de archivos privados
- Agente: ChatGPT (GPT-6)
- Solicitud: recuperación y documentación segura de los proyectos.
- Cambios: se añadió `.gitignore` para excluir entornos, claves, certificados, bases de datos y artefactos privados; `.env.example` contiene solo nombres o comentarios y valores de sustitución ficticios.
- Archivos: `.gitignore`, `.env.example`.
- Verificación: archivos escritos en GitHub → confirmados; escaneo automático de secretos → no ejecutado.
- Pendiente: ejecutar escáner de secretos y configurar variables protegidas si se incorporan integraciones reales.


## 2026-11-12 · Documentación de inspección pública
- Agente: ChatGPT (GPT-6)
- Solicitud: recuperación completa y documentada de los seis proyectos web.
- Cambios: Inspección de portada, contratación, apoyo, EPK, música, redes, activos y estado deshabilitado de pagos.
- Archivos: `docs/INSPECCION-PUBLICA.md`.
- Verificación: archivo escrito y releído por GitHub → confirmado; auditoría visual independiente → no ejecutada.
- Pendiente: resolver las fuentes originales, assets y pruebas indicadas en el informe.


## 2026-11-12 · Corrección de enlaces legales
- Agente: ChatGPT (GPT-6)
- Solicitud: completar la navegación reconstruida sin presentar documentos legales incompletos como definitivos.
- Cambios: el footer enlaza directamente a las páginas legales vigentes del sitio de origen.
- Archivos: `index.html`.
- Verificación: actualización en GitHub → confirmada; navegación automatizada → no ejecutada.
- Pendiente: recuperar versiones legales completas y alojarlas localmente solo después de validarlas.


## 2026-11-12 · Rutas de contratación, apoyo y EPK
- Agente: ChatGPT (GPT-6)
- Solicitud: completar la reconstrucción pública del sitio manteniendo los límites de operación observados.
- Cambios: se añadieron páginas de contratación (prepara un mensaje local a WhatsApp), apoyo (aportes deshabilitados) y EPK (biografía resumida y enlaces a plataformas).
- Archivos: `contratar.html`, `apoyar.html`, `epk.html`.
- Verificación: escrituras en GitHub → confirmadas; prueba real de envío/WhatsApp y comparación visual → no ejecutadas.
- Pendiente: incorporar textos legales originales íntegros, confirmar biografía con artista/equipo, validar formularios y revisar rutas antes de despliegue.


## 2026-11-12 · Reconstrucción inicial de la portada pública
- Agente: ChatGPT (GPT-6)
- Solicitud: recuperar el sitio público de Vicente Diablo y conservar diseño, contenidos y estado operativo observable.
- Cambios: se añadió una portada estática reconstruida con enlaces de música, historia, redes y contratación; aportaciones permanecen deshabilitadas, sin cobros ni recepción de solicitudes.
- Archivos: `index.html`.
- Verificación: escritura en GitHub → confirmada; pruebas de navegador y comparación visual → no ejecutadas.
- Pendiente: construir rutas de contratación, apoyo, EPK y páginas legales a partir de textos originales completos; recuperar activos originales y validar con el responsable.


## 2026-11-12 · Inicialización documental del repositorio
- Agente: ChatGPT (GPT-6)
- Solicitud: autorización del propietario para recuperar y documentar los seis proyectos web; creación de repositorios públicos para los proyectos 4, 5 y 6.
- Cambios: incorporación de reglas de continuidad, preservación de diseño, seguridad y estado honesto de recuperación.
- Archivos: README.md, AGENTS.md, ia/REGLAS.md, ia/PROTOCOLO.md, CHANGELOG.md.
- Verificación: escritura inicial en GitHub → confirmada; revisión funcional del sitio → no ejecutada.
- Pendiente: inventariar fuentes y recursos originales; recuperar o reconstruir implementación con evidencia; añadir pruebas.
