# HANDOFF — Trabajar con los problemas de la OMI

Documento de traspaso para continuar la **transcripción + upsolving** del archivo
de la Olimpiada Mexicana de Informática (OMI). Si llegas **sin contexto previo,
lee esto primero**: tiene todo lo necesario para producir una tarea de principio
a fin. Complementa a [`README.md`](README.md) (estructura) y
[`PROGRESO.md`](PROGRESO.md) (checklist).

_Última actualización: 2026-06-27._

---

## 0. TL;DR — el ciclo de una tarea

1. Abre [`PROGRESO.md`](PROGRESO.md) y elige el primer problema con `[ ]`.
2. Lee su enunciado (ya descargado) y su `meta.json`:
   ```bash
   cd OMI/<año>/<NN Título>
   cat meta.json
   cat statement.md            # si existe (lo más común), o:
   pdftotext -layout statement.pdf -    # si el enunciado es PDF, o:
   # si solo hay meta.json->statement_link (DMOJ): abre/lee esa URL
   ```
3. (Recomendado) baja casos y solución de referencia para **verificar**:
   ```bash
   python3 OMI/download_omi.py --years <año> --cases --refs
   unzip -o "OMI/<año>/<NN Título>/_local/cases.zip" -d "OMI/<año>/<NN Título>/_local/cases"
   ```
4. Resuelve y **verifica tu algoritmo contra el ejemplo y los casos** ANTES de
   escribir la Vista 2.
5. Crea la página y llena las dos vistas:
   ```bash
   cp OMI/TEMPLATE.html "OMI/<año>/<NN Título>/index.html"
   ```
6. Regenera índices y commitea (rutas EXPLÍCITAS, ver §7):
   ```bash
   python3 OMI/build_index.py
   git add "OMI/<año>/<NN Título>/index.html" OMI/PROGRESO.md OMI/index.html index.html
   git commit -m "OMI <año>/<NN>: transcripción y upsolving (<Título>)"
   ```

---

## 1. Estado actual

- **Cobertura:** **30 ediciones** (1ª OMI 1996 → 30ª OMI 2025), **190 problemas**.
- **Enunciados descargados (versionados):** 189 / 190 con `statement.md`/`.pdf` local.
  - 148 desde la **API de omegaUp** → `statement.md` (markdown).
  - 12 desde **DMOJ** (edición 30ª/2025 sobre todo) → `statement.md` (extraído del
    `content-description`, con matemáticas en `\( … \)` e imágenes ya bajadas a
    `images/`). El HTML crudo queda en `_local/statement.html`.
  - 29 en **PDF** (`statement.pdf`): ediciones viejas + 2 de 2025. 4 de ellos se
    rescataron del **Wayback Machine** (host `cmirg.com` está caído).
  - **1 sin fuente:** `2008/04 Sumas Adyacentes` (PDF de cmirg.com caído y sin
    copia en Wayback). Intenta buscarlo en omegaUp por título, o déjalo al final.
- **`meta.json`** está en las 190 carpetas (edición, año, día, juez, límites, urls).
- **Páginas hechas:** ver el contador de [`PROGRESO.md`](PROGRESO.md) (se regenera).
- **Sitio:** el `index.html` raíz es un hub (ICPC + IOI + **OMI**);
  `OMI/index.html` lista las 190 tareas por edición. Ambos se regeneran con
  `build_index.py`.

> El estado “hecho/pendiente” **no** se lleva a mano: se infiere de si existe el
> `index.html` de cada tarea. Por eso `PROGRESO.md` y `OMI/index.html` se
> **regeneran** (§6), no se editan a mano.

---

## 2. La OMI no es IOI/ICPC (lo que cambia el contenido)

| Aspecto | IOI/ICPC | **OMI** |
|---|---|---|
| Idioma | Inglés → **traduces** | **Ya está en español → TRANSCRIBES** (fiel; no traduzcas) |
| Formato | IOI: funcional/interactivo | **E/S clásica** (stdin/stdout); sin funciones a implementar |
| Puntaje | IOI por subtareas | **Subtareas** en la era moderna (≈2017+); ediciones viejas “todo o nada” por caso |
| Paradigma | Algorítmico | Algorítmico **+ Karel** (ediciones 9ª–21ª, 2004–2016) tienen un día de Karel |

- **Vista 1 = transcripción fiel** del enunciado oficial (en español). Ordena y
  limpia erratas de OCR/markdown, **sin cambiar el contenido**. Conserva
  historia, Entrada, Salida, Ejemplos, Límites y Subtareas.
- **KAREL** (días “Karel” de las ediciones 9ª–21ª): no se programa en C++, sino
  en el lenguaje de **Karel el robot** (avanza, gira-izquierda, coge-zumbador,
  deja-zumbador, mientras/si, `define-nueva-instruccion`, etc.). En esas tareas:
  - Vista 1: describe el **mundo** (dimensiones, paredes, zumbadores, posición y
    orientación inicial, mochila) y el objetivo.
  - Vista 2: el razonamiento y el “pseudocódigo” final usan **primitivas de
    Karel**, no C++. Pon la etiqueta «Karel». La plantilla ya trae el bloque.
- **Excepción — tareas interactivas:** aunque la mayoría es E/S clásica, alguna
  tarea moderna es **interactiva** (p. ej. 2025 «Baterías»: minimizas el número
  de **consultas** a una función del evaluador). En esos casos describe el
  **protocolo/funciones** y el **presupuesto de consultas** por subtarea, y la
  etiqueta «Interactivo». No fuerces el molde de stdin/stdout.

---

## 3. Estructura y rutas (exactas)

```
OMI/
├── HANDOFF.md          ← este documento
├── README.md           ← estructura + workflow
├── PROGRESO.md         ← checklist (generado)
├── TEMPLATE.html       ← plantilla a copiar como index.html de cada tarea
├── index.html          ← listado OMI (generado)
├── omi_inventory.json  ← fuente de verdad (parseada de la lista oficial)
├── download_omi.py     ← descargador idempotente (enunciados, casos, soluciones)
├── build_index.py      ← regenera PROGRESO.md, OMI/index.html y la tarjeta del hub
├── assets/mathjax/     ← MathJax autohospedado (lo usa cada index.html de tarea)
└── <año>/              ← año = 1995 + número de edición (1996 = 1ª … 2025 = 30ª)
    ├── <NN Título>/
    │   ├── statement.md    ← enunciado markdown (omegaUp)       (versionado)
    │   ├── statement.pdf   ← enunciado PDF (si aplica)          (versionado)
    │   ├── images/         ← imágenes del enunciado (si hay)    (versionado)
    │   ├── meta.json       ← metadatos (edición, día, límites)  (versionado)
    │   ├── _local/         ← casos, soluciones, html DMOJ       (GITIGNORED)
    │   └── index.html      ← las dos vistas                     (lo creas tú)
```

- **Mapeo edición↔año:** `año = 1995 + edición`. 1ª = 1996, …, 30ª = 2025.
- Página de cada tarea: `OMI/<año>/<NN Título>/index.html` (NN con dos dígitos).
- MathJax desde una tarea: `../../assets/mathjax/tex-svg.js`.
- El hub raíz vive en `../index.html` (un nivel arriba de `OMI/`).

---

## 4. De dónde sale el enunciado (y su formato)

Orden de preferencia (ya resuelto por el descargador, pero conócelo):

1. **`statement.md`** (omegaUp). Markdown con convenciones de omegaUp:
   - Matemáticas con `$...$` (en una transcripción a HTML pásalas a `\( ... \)`).
   - Bloques de ejemplo: `||input` / `||output` / `||description` / `||end`.
   - Imágenes: referenciadas por nombre; ya están en `images/` (embébelas base64).
   - Suele traer secciones `# Problema`, `# Entrada`, `# Salida`, `# Ejemplo`,
     `# Límites`, `# Subtareas`.
2. **`statement.pdf`** (ediciones viejas): `pdftotext -layout statement.pdf -`.
   Si tiene figuras necesarias, extráelas con pymupdf y embébelas (ver
   TEMPLATE.html, instrucción 7).
3. **DMOJ** → ya extraído a `statement.md` (con imágenes en `images/`). El HTML
   original queda en `_local/statement.html`; la URL viva está en
   `meta.json -> statement_link`.

> Para refrescar/forzar una descarga: `python3 OMI/download_omi.py --years <año> --force`.

---

## 5. Cómo redactar cada vista

**Vista 1 — Enunciado.** Transcripción fiel al **español mexicano** del enunciado
oficial. Incluye **Entrada/Salida**, un bloque de **Límites** (tiempo, memoria,
rangos), la tabla de **Subtareas** (si la tarea las tiene; si no, nota “Sin
subtareas”) y el/los **ejemplos** tal cual. Embebe las **figuras** necesarias
como data URI base64. En Karel, usa el bloque «Tarea de Karel».

**Vista 2 — Upsolving (socrática).** Barra de **2–5 etiquetas**, **resumen
mínimo** (sin historia) y **pistas progresivas** en `<details>` que **preguntan**
(“¿Ya pensaste…?”) y van de lo general a lo específico. En tareas modernas razona
**subtarea por subtarea** (qué idea regala cada bloque de puntos). La **última
pista es el upsolving completo**: idea, por qué es correcta, **pseudocódigo** (o
primitivas de Karel) y complejidad.

**Reglas estrictas de contenido:**
- Todo en **español mexicano**, sencillo y directo.
- **NUNCA** código de una solución. Solo **pseudocódigo** (o Karel). Un truco
  propio de lenguaje, **solo C++** y bien señalado.
- Las pistas **preguntan**, no afirman (la última sí es la solución completa).
- Contenido **original**; puedes leer la solución de referencia (`_local/`) para
  entender, pero no copies código al sitio.
- Matemáticas en LaTeX (`\( … \)` / `\[ … \]`); `<code>` solo para
  nombres/variables. Pseudocódigo en `<pre>`. Todo **autocontenido** (sin CDNs;
  imágenes en base64; única dependencia: MathJax autohospedado).

---

## 6. Herramientas y verificación

- **Leer enunciado:** `cat statement.md` · `pdftotext -layout statement.pdf -`.
- **Descargar casos + soluciones de un año** (a `_local/`, gitignored):
  `python3 OMI/download_omi.py --years <año> --cases --refs`.
- **Verificar tu solución** antes de la Vista 2: comprueba el ejemplo a mano y,
  si bajaste los casos, corre tu solución contra `_local/cases/`. La solución de
  referencia oficial queda en `_local/solution.cpp` (úsala para **entender**, no
  para copiar).
- **Jueces en línea** (enviar y autocalificar): **omegaUp**
  (`meta.json -> statement_link` o `omegaup_alias`) y **DMOJ**
  (`dmoj.olimpiadadeinformatica.org.mx`).
- **Regenerar índices:** `python3 OMI/build_index.py` (idempotente; reescribe
  `PROGRESO.md`, `OMI/index.html` y actualiza la tarjeta OMI del hub raíz).

---

## 7. Gotchas / lecciones aprendidas (¡importante!)

1. **Sesiones concurrentes en el MISMO `main`.** Hay otras sesiones/agentes
   committeando IOI/ICPC a `main` en este repo (se vio `HEAD` moverse). Por eso:
   - **Nunca `git add -A` ni `git add .`** — siempre **rutas explícitas** (solo
     tus archivos OMI). Antes de commitear, confirma con `git status` y
     `git rev-parse --abbrev-ref HEAD`.
   - Idealmente trabaja en un **git worktree** dedicado (ver `~/.claude/CLAUDE.md`).
2. **`_local/` NUNCA se sube.** Está en `.gitignore` (`OMI/*/_local/`). Ahí viven
   casos, soluciones y el HTML de DMOJ. No quites la regla ni stagees nada de ahí.
3. **Lo que SÍ se versiona:** `statement.md`, `statement.pdf`, `images/`,
   `meta.json`, `index.html`. (Enunciados e imágenes son parte del sitio.)
4. **Carpetas con acentos y espacios** (`01 El fucho`, `08 Yarbólica`). En bash
   **entrecomilla siempre** las rutas; en los `href` se codifican con `%` —
   `build_index.py` ya lo hace con `urllib.parse.quote`.
5. **No edites `PROGRESO.md` ni `OMI/index.html` a mano** — se regeneran.
6. **omegaUp markdown ≠ HTML.** Convierte `$…$`→`\(…\)`, los bloques
   `||input/||output/||description/||end` a la tabla de «Ejemplo», y embebe las
   imágenes de `images/` en base64.
7. **Enunciados problemáticos:**
   - `2008/04 Sumas Adyacentes`: sin fuente (cmirg.com caído, sin Wayback).
     Busca en omegaUp por título o déjalo al final.
   - DMOJ (2025): el `statement.md` ya trae el enunciado completo e imágenes en
     `images/`; el HTML original está en `_local/statement.html` por si acaso.
8. **`meta.json` puede NO traer límites** de tiempo/memoria (las tareas de DMOJ).
   Búscalos en `_local/statement.html` (la página de DMOJ los muestra) o en el
   propio enunciado; ponlos en la Vista 1.
9. **`statement.md` a veces trae glitches de OCR/markdown:** exponentes rotos
   (`10^5` se ve como `105`), typos, o un encabezado (p. ej. «Salida») embebido
   dentro de un item de «Entrada». **Corrígelos como errata obvia** en la
   transcripción (sin cambiar el contenido); el `statement.md` fuente se queda
   como está (es la fuente cruda).
10. **Casos:** pares `SubX_NN.in` / `SubX_NN.out` agrupados por subtarea. Algunos
    problemas son **special-judge** (varias respuestas válidas): compara
    semánticamente, no por texto. Si una tarea **no tiene casos** (p. ej. 2025
    «Yarbolica»), verifica con **fuerza bruta / pruebas aleatorias** contra tu
    solución o la de referencia (`_local/solution.*`).
11. **Verifica el HTML** tras escribirlo: sin marcadores `{{…}}` sin rellenar, las
    dos vistas presentes, el toggle funcionando y MathJax renderizando.

---

## 8. Orden de trabajo sugerido

Por **edición, de la más reciente a la más antigua** (2025 → 1996), porque las
recientes tienen subtareas y casos limpios (mejor material para upsolving). La
edición **30ª OMI (2025)** ya está hecha como **muestra** del formato — úsala de
referencia. Dentro de una edición, sigue el orden de `PROGRESO.md` (Día 1 → Día 2,
o Karel → Lenguaje).

> Alternativa: cronológico (1996 → 2025) como en IOI. Pregúntale al usuario si
> tiene preferencia; por defecto, reciente → antiguo.

---

## 9. Referencia rápida de comandos

```bash
# elegir tarea: primer [ ] de PROGRESO.md
# leer enunciado + meta
cat "OMI/2024/01 La clase de historia de Juan/statement.md"
cat "OMI/2024/01 La clase de historia de Juan/meta.json"

# casos + solución de referencia (a _local, gitignored)
python3 OMI/download_omi.py --years 2024 --cases --refs

# crear la página y llenarla
cp OMI/TEMPLATE.html "OMI/2024/01 La clase de historia de Juan/index.html"

# regenerar índices + hub
python3 OMI/build_index.py

# commit (rutas EXPLÍCITAS por las sesiones concurrentes)
git add "OMI/2024/01 La clase de historia de Juan/index.html" OMI/PROGRESO.md OMI/index.html index.html
git commit -m "OMI 2024/01: transcripción y upsolving (La clase de historia de Juan)"
```
