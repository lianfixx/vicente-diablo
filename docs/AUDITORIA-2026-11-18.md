# Auditoría de fondo · 18 de noviembre de 2026

Agente: Claude Code, a solicitud de Emi. Se leyó completo: este repositorio (15 archivos), el
sitio publicado (7 páginas, en solo lectura) y el proyecto de Claude Design «Vicente Diablo:
Sitio web profesional» (4 páginas, notas de investigación y la skill `apple-design-system` con
sus 6 referencias). No se inició sesión, no se desplegó nada y no se envió ningún mensaje.

## 1. Qué hay, por origen

| Pieza | Origen | Estado |
|---|---|---|
| Sitio publicado en `vicente-diablo.emilianomilla.chatgpt.site` | Plataforma de origen (aplicación con servidor, base de datos, Stripe y acceso de equipo) | Es la versión vigente. Su fuente editable **no** está en este repositorio. |
| `recuperado/2026-11-18/` | Descarga de lo que el sitio entrega al público | **Recuperación parcial** con hashes. Se ve idéntica al sitio. |
| `index.html`, `contratar.html`, `apoyar.html`, `epk.html` | Escritos por ChatGPT el 12/11 | **Reconstrucción simplificada**, no fiel (ver 2.1). |
| `legal-*.html` | Transcripción del 12/11 | Cuerpo fiel; encabezados e introducción corregidos hoy. |
| Proyecto de Claude Design (octubre de 2026) | https://claude.ai/artifact/TKio6xDuLrVZZhxuZ94H7A (privado) | **Propuesta anterior**, distinta del sitio publicado (ver 3). No está en este repositorio. |

## 2. Hallazgos en el repositorio

### 2.1 La reconstrucción de la raíz no corresponde al diseño publicado
- El sitio real es claro (fondo `#fffdf8`, texto verde oscuro `#263d35`, acento mostaza `#d8a82e`),
  con titulares en serif del sistema (Iowan Old Style / Baskerville) y texto en Avenir Next.
  La reconstrucción es oscura, con naranja `#ff6700`, durazno `#fecb8b`, Playfair Display y DM Sans.
  Ninguno de esos cuatro valores aparece en el sitio publicado.
- Faltan en la reconstrucción: la fotografía principal «A todo pulmón», el reproductor con
  «Canciones propias / Más recientes», el selector de idioma, el calendario y el globo de
  `/contratar`, el importe libre de `/apoyar` (mínimo 20, máximo 10 000 MXN), el enlace
  «Acceso del equipo» y la mayor parte del EPK (formación, Maíz d'Elvis, LaChilanBalam,
  colaboraciones, 2025–26).
- Textos alterados: en «Su historia» los rótulos y títulos están invertidos y numerados
  (el sitio dice «Los primeros acordes / Antes de los focos.», sin número); el párrafo de
  `apoyar.html` y el resumen del EPK no son texto del sitio.
- El formulario de `contratar.html` sí refleja el comportamiento real (prepara un mensaje y el
  visitante decide enviarlo por WhatsApp), pero con campos y nombres propios.
- **No se rediseñó.** Se corrigieron solo defectos (2.3). Decisión pendiente de Emi: conservarla
  como borrador o retirarla, ahora que existe la copia fiel.

### 2.2 Fe de erratas de `docs/INSPECCION-PUBLICA.md` (12/11)
- Colores y tipografías descritos no corresponden al sitio (ver 2.1).
- La lista de imágenes omitía `vicente-diablo-hero.webp` y `vicente-guitar.webp`; son 9, no 7.
- El pendiente 1 (texto íntegro de las páginas legales) ya estaba cubierto el mismo 12/11 y hoy
  queda cotejado; el pendiente 3 (activos con hash) queda cubierto por `recuperado/2026-11-18/`.

### 2.3 Defectos corregidos hoy
- Transcripciones legales: títulos («Condiciones de contratación», «Condiciones del apoyo»),
  subtítulos, párrafos introductorios, nota de traducciones y encabezados de sección
  («Quién presta el servicio», «Contenido de la oferta y precio», «Reserva y confirmación del
  pago») ahora coinciden con el sitio. El cuerpo ya coincidía frase por frase.
- La portada dependía de imágenes servidas por el sitio de origen; ahora usa las recuperadas.
- Enlaces que abren otra pestaña sin `rel="noopener"`; `&` sin escapar en el EPK; el enlace al
  aviso de privacidad dentro del formulario se dibujaba como botón naranja.
- `CHANGELOG.md` estaba de lo más antiguo a lo más reciente. La Matriz General mostraba por eso
  «Inicialización documental» como último registro. Se reordenó sin tocar el texto.

### 2.4 Protocolo: piezas que el documento da por hechas y aquí no existen
`ia/PROTOCOLO.md` 1.1.0 es idéntico a la copia de otros proyectos, pero en este repositorio
faltan: `ia/verificar.py`, `ia/instalar.sh`, `ia/guard.py`, `ia/politica.json`,
`ia/test_guard.py`, `ia/plantillas/`, `ia/INSTRUCCIONES_PROYECTO.md`, `.claude/settings.json`,
`CLAUDE.md`, `GEMINI.md`, el workflow `registro-ia.yml` y una skill del proyecto. Consecuencias:
ningún control automático se aplica aquí; `ia/REGLAS.md` no se genera desde una política; los
commits anteriores no llevan `IA-Actor:`. No se inventaron estas piezas: deben copiarse del
repositorio que las mantiene, con una política propia de este proyecto aprobada por Emi.
Mientras tanto existe `pruebas/verificar.py` (hashes, enlaces locales, registro y secretos).

### 2.5 Datos y seguridad
- Sin secretos en el repositorio ni en la copia recuperada (búsqueda de claves de Stripe, tokens y llaves).
- El número de WhatsApp de contacto del equipo aparece en `contratar.html` y en la copia; ya es
  público en el sitio. No se añadió ningún otro dato personal.
- `api/public/config.json` confirma: reservas y aportaciones deshabilitadas; operador, domicilio,
  correo, teléfono y país vacíos. Los tres textos legales lo dicen también.

## 3. El trabajo previo en Claude Design (octubre de 2026)

Proyecto migrado de Claude Design a claude.ai el 13/11/2026 (Claude Design independiente cierra
el 14/12/2026; este proyecto ya está a salvo como artefacto privado de Emi).

**Contenido.** (a) «Presentación para Vicente», 9 láminas con notas del orador; (b) «Preguntas
para Vicente», 37 preguntas en 7 bloques; (c) «Vicente Diablo – Sitio», prototipo bilingüe ES/EN,
claro/oscuro, con seis secciones (Inicio, Historia, Música, Contratar, Donar, Legal);
(d) «Documentos oficiales», 8 documentos: contrato, cotización, anticipos y cancelaciones, rider
de hospitalidad, EPK, aviso de privacidad, términos del sitio y términos de donaciones;
(e) notas de investigación; (f) la skill `apple-design-system` subida como referencia.

**Informe de la migración.** 2 páginas completas y 2 parciales: las notas del orador se conservan
pero no se muestran al presentar; el reproductor de SoundCloud y los enlaces `wa.me` quedan
bloqueados dentro del lienzo.

**No es el sitio publicado.** Son dos trabajos distintos:

| | Claude Design (octubre) | Sitio publicado (noviembre) |
|---|---|---|
| Relato | Puerto Escondido, foro Atemoztli, cita de Fodor's, blues y rock | «De la costa de Oaxaca al mundo», CDMX → Oaxaca → Países Bajos |
| Música | SoundCloud, 10 temas 2011–2018 | Spotify, sencillos 2022–2025 |
| Voz | Primera persona | Tercera persona |
| Aspecto | Rojo chile, oro, verde agave; Gloock | Crema, verde oscuro, mostaza; serif del sistema |
| Apoyo | «Donaciones»: Mercado Pago, PayPal, Stripe, Ko-fi; $50–$1,000 | «Propina»: Stripe; $75, $150, $300 |
| Facebook | `VicenteElDiablo` | `VicenteGarciaElDiablo` |
| Jazzectro | 2013 (SoundCloud) | 2022 (catálogo de Spotify) |

**Estado del prototipo.** Sin datos reales: precios «Desde $X,XXX», WhatsApp, correo y enlaces
de pago vacíos (los botones avisan «por configurar»), fotografías sin colocar. Instagram, TikTok
y YouTube no se pudieron leer entonces; el sitio publicado ya los tiene.

**Observaciones a los 8 documentos** (son plantillas con campos en blanco; ninguno está en uso):
- Correcto: la ley de datos citada es la vigente (DOF 20/03/2025), la autoridad es la Secretaría
  Anticorrupción y Buen Gobierno y los plazos ARCO son 20 + 15 días hábiles.
- A revisar antes de usarlos: (1) llamar «donación» a la aportación; el sitio publicado ya usa
  «propina» y aclara que no es donativo, que es más prudente; (2) la pena del 100 % por cancelar
  con 7 días o menos y la renuncia de fuero pueden no sostenerse frente a un consumidor (Profeco);
  (3) la transferencia de datos a músicos y proveedores «sin consentimiento» debe apoyarse en una
  excepción legal concreta; (4) conservación de 12 meses frente a los 180 días del sitio publicado;
  (5) RFC, régimen fiscal y domicilio del artista en blanco. El propio documento recomienda
  revisión de abogado; sigue pendiente.
- Las notas guardan un teléfono del antiguo foro marcado «no publicar sin confirmar». No se copió.

### 3.1 La skill `apple-design-system`
- Es de un tercero (rukkiecodes, licencia MIT, v1.0.0), pensada para una aplicación móvil en
  React Native llamada QueenSkiilia. No es una skill de Vicente Diablo ni está instalada en
  Claude Code; solo viaja como archivo adjunto del proyecto de diseño.
- Sus 8 reglas: un solo acento azul `#0066cc`, botones píldora, sin sombras, pesos 400/600/700
  (500 prohibido), líneas finas de 1 px, esquinas continuas, mucho aire y alertas propias.
- Incoherencias internas: dice titulares en 700 mientras su fuente canónica dice 600 «y no 700»;
  prohíbe el peso 300 que la fuente sí usa; su escala de radios (6/10/14/20) y de espacios no
  coincide con la de la fuente (5/8/11/18); el README resume 7 reglas y la skill 8; casi todo
  `components.md` y `screens.md` (OTP, pestañas, chat, teclado en Android) no aplica a un sitio web.
- Uso real en el prototipo: solo la estructura (píldoras, aire, secciones alternas, pesos
  400/600/700), por decisión de Emi: «su mundo primero, estructura tipo Apple». El prototipo se
  aparta a propósito del acento único (usa rojo, oro y verde) y tiene una sombra en el aviso
  emergente que la skill prohíbe.
- El sitio publicado no sigue esta skill y no tiene por qué: usa otro lenguaje visual.

## 4. Lo que sigue

1. **Fuente editable.** Exportar o descargar el proyecto desde la plataforma de origen (solo Emi
   tiene acceso). Sin eso, este repositorio no puede reconstruir ni desplegar el sitio real.
2. **Decidir el destino de la reconstrucción simplificada** de la raíz: retirarla o dejarla como borrador.
3. **Decidir qué versión manda** donde chocan (tabla de la sección 3) y preguntarle a Vicente:
   el cuestionario de 37 preguntas ya está listo.
4. **Datos del prestador** (identidad, domicilio, contacto, RFC) antes de habilitar solicitudes o
   cobros. Hasta entonces todo sigue deshabilitado.
5. **Revisión jurídica** de los 8 documentos del prototipo y de los 3 textos publicados.
6. **Instalar las piezas comunes del protocolo** (2.4) con una política para este proyecto.
7. Si Emi lo autoriza, **archivar aquí el proyecto de Claude Design** como propuesta, sin el teléfono no confirmado.
