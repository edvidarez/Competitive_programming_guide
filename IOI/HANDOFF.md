# HANDOFF — Trabajar con los problemas del IOI

Documento de traspaso para continuar la traducción + upsolving del archivo IOI.
Si llegas sin contexto previo, **lee esto primero**. Complementa a
[`README.md`](README.md) (estructura) y [`PROGRESO.md`](PROGRESO.md) (checklist).

_Última actualización: 2026-06-26._

---

## 1. Estado actual

- **Material descargado:** IOI **2003–2025** (23 ediciones, 142 tareas). Los
  enunciados (`statement.pdf`) están versionados; tests/soluciones/práctica
  viven en `<año>/_local/` y están **gitignored** (no se publican).
- **Páginas hechas:** **1 / 142.**
  - `2003/01 Trail Maintenance/index.html` ✅ (MST incremental con union-find).
- **Próxima sin hacer:** `2003/02 Comparing Code` (orden cronológico).
- **Sitio:** el `index.html` raíz es un hub (ICPC + IOI); `IOI/index.html` lista
  las 142 tareas (listo/pendiente). Ambos se regeneran con `build_index.py`.

> El estado “hecho/pendiente” **no** se lleva a mano: se infiere de si existe el
> `index.html` de cada tarea. Por eso `PROGRESO.md` e `IOI/index.html` se
> **regeneran** (ver §6), no se editan a mano.

---

## 2. Cómo continuar (TL;DR)

Para cada tarea, en orden:

1. Abre [`PROGRESO.md`](PROGRESO.md) y elige la primera `[ ]`.
2. Lee su enunciado: `pdftotext -layout "<año>/<NN Título>/statement.pdf" -`.
3. Copia la plantilla a esa carpeta **como `index.html`**:
   `cp TEMPLATE.html "<año>/<NN Título>/index.html"`.
4. Rellena las **dos vistas** (enunciado traducido + upsolving socrático)
   siguiendo las reglas embebidas en `TEMPLATE.html` y la §7 de aquí.
5. **Verifica el algoritmo contra el ejemplo oficial** antes de dar por buena la
   Vista 2 (usa los tests de `_local/` si hace falta; ver §6).
6. Regenera índices y haz commit:
   ```
   python3 IOI/build_index.py
   git add "IOI/<año>/<NN Título>/index.html" IOI/PROGRESO.md IOI/index.html index.html
   git commit -m "IOI <año>/<NN>: traducción y upsolving (<Título>)"
   ```

---

## 3. Estructura y rutas (exactas)

```
IOI/
├── HANDOFF.md          ← este documento
├── README.md           ← estructura + workflow
├── PROGRESO.md         ← checklist (generado)
├── TEMPLATE.html       ← plantilla a copiar como index.html de cada tarea
├── index.html          ← listado IOI (generado)
├── download_ioi.py     ← descargador de enunciados/tests/soluciones (2003–2025)
├── build_index.py      ← regenera PROGRESO.md, IOI/index.html y la tarjeta del hub
├── assets/mathjax/     ← MathJax autohospedado (lo usa cada index.html de tarea)
└── <año>/
    ├── <NN Título>/
    │   ├── statement.pdf   ← enunciado oficial            (versionado)
    │   └── index.html      ← las dos vistas               (lo creas tú)
    └── _local/             ← tests/soluciones/práctica    (gitignored, NO subir)
```

- La página de cada tarea es `<año>/<NN Título>/index.html` (NN con dos dígitos).
- Referencia a MathJax desde una tarea: `../../assets/mathjax/tex-svg.js`.
- Enlace al PDF desde la tarea: `statement.pdf` (misma carpeta).
- El hub raíz vive en `../index.html` (un nivel arriba de `IOI/`).

---

## 4. IOI ≠ ICPC (lo que cambia el contenido)

| Aspecto | ICPC | IOI |
|---|---|---|
| Formato | E/S clásica (stdin/stdout) | A menudo **funcional/interactivo** (implementas funciones; el grader las llama) o **output-only** |
| Puntaje | Por caso, todo o nada | Por **subtareas** con **crédito parcial** (cada subtarea = restricciones + puntos) |
| Razonamiento upsolving | Una idea → solución | **Subtarea por subtarea**: cada bloque de puntos suele esconder una idea nueva, de fuerza bruta a la solución de 100 |

Casos especiales que ya aparecieron y que la plantilla soporta:

- **Ediciones viejas sin subtareas (≈2003–2009):** algunas tareas puntúan por
  caso (“todo o nada”), como ICPC. En esos casos **no inventes subtareas**:
  pon la nota “Sin subtareas” (ver `2003/01` como ejemplo).
- **Tareas “online/reactivas”** (p. ej. `2003/01`): son stdin/stdout pero debes
  responder cada consulta antes de leer la siguiente. El PDF puede llamarlas
  “interactive task” aunque no haya firmas de función.
- **Funcionales/interactivas modernas:** usa la sección «Detalles de
  implementación» de la plantilla para las firmas; borra «Entrada/Salida».
- **Output-only:** indícalo en «Detalles de implementación».

La sección «Subtareas» de la plantilla es obligatoria **cuando la tarea las
tiene**; cópiala de la tabla del PDF (número, puntos, restricciones).

---

## 5. Cómo redactar cada vista

**Vista 1 — Enunciado:** traducción fiel y completa al **español mexicano**.
Conserva la historia pero hazlo claro. Incluye Entrada/Salida **o** Detalles de
implementación según el tipo, un bloque de **Límites** (tiempo, memoria, rangos),
la tabla de **Subtareas** (si aplica) y el/los ejemplos tal cual el PDF.
**Figuras clave del PDF: extráelas y embébelas** como data URI base64 (ver §6).

**Vista 2 — Upsolving (socrática):** barra de **2–5 etiquetas** (vocabulario en
`TEMPLATE.html`; añade *Interactivo* cuando aplique), **resumen mínimo** (sin
historia), y **pistas progresivas** en `<details>` que **preguntan** (“¿Ya
pensaste…?”) y van de lo general a lo específico, razonando subtarea por
subtarea. La **última pista es el upsolving completo** (idea, por qué es
correcto, pseudocódigo y complejidad).

---

## 6. Herramientas y verificación

- **Leer PDF:** `pdftotext -layout statement.pdf -` (instalado).
  ⚠️ `pymupdf` (`import fitz`) **no está instalado** en esta máquina; si lo
  necesitas para figuras: `pip install pymupdf`, o usa `pdfimages`/`pdftoppm`.
- **Extraer una figura vectorial** (lo común en estos PDFs) — renderiza su región
  con pymupdf y embébela en base64 (ver receta en `TEMPLATE.html`, instrucción 7).
- **Validar tu solución** antes de escribir la Vista 2:
  - Comprueba a mano que tu algoritmo reproduce el **ejemplo del PDF**.
  - Material oficial en `<año>/_local/` (gitignored): `unzip` el `tests.zip` para
    casos reales; el `solutions.zip`/`.pdf` trae la solución de referencia.
  - Jueces en línea para enviar y autocalificar: **oj.uz**
    (`/problems/source/ioi`), **archivo IOI de Codeforces**
    (`ioi.contest.codeforces.com`), **Yandex.Contest** (2003–2018).
- **Regenerar índices:** `python3 IOI/build_index.py` (idempotente; reescribe
  `PROGRESO.md`, `IOI/index.html` y actualiza la tarjeta IOI del hub raíz).
- **Descargar un IOI nuevo:** agrega `año: id_de_página` a `YEAR_PAGE` en
  `download_ioi.py` y corre `python3 IOI/download_ioi.py --years <año>`.

---

## 7. Gotchas / lecciones aprendidas (¡importante!)

1. **Sesión concurrente de ICPC en el MISMO working tree.** Hay otra
   sesión/agente committeando trabajo de ICPC a `main` en este checkout (se vio
   `HEAD` moverse entre commits). Por eso:
   - **Nunca `git add -A` ni `git add .`** — siempre **rutas explícitas** (solo
     tus archivos IOI). Así no capturas el trabajo ajeno.
   - Antes de commitear, confirma con `git status` que solo van tus rutas.
   - Si vas a trabajar en serie, considera un **git worktree** dedicado para
     aislarte (ver `~/.claude/CLAUDE.md`).
2. **`_local/` NUNCA se sube.** Está en `.gitignore` (`IOI/*/_local/`). No quites
   esa regla ni stagees nada de ahí (son varios GB de tests/soluciones).
3. **Nombres de carpeta con espacios** (`01 Trail Maintenance`). En los `href`
   del índice se codifican como `%20` — `build_index.py` ya lo hace con
   `urllib.parse.quote`. En bash, **entrecomilla siempre** las rutas.
4. **No edites `PROGRESO.md` ni `IOI/index.html` a mano** — se regeneran con
   `build_index.py` a partir de qué tareas tienen `index.html`. Si los editas,
   el script los sobrescribe.
5. **Autocontenido:** cada `index.html` de tarea lleva su CSS/JS inline y las
   imágenes embebidas en base64. La única dependencia es MathJax autohospedado
   (`../../assets/mathjax/tex-svg.js`). **Sin CDNs.**
6. **Matemáticas en LaTeX** entre `\( ... \)` / `\[ ... \]` (MathJax). `<code>`
   es solo para nombres de funciones/variables y tokens literales, **no** para
   matemáticas. El pseudocódigo va en `<pre>` (MathJax no lo toca).
7. **Verifica el HTML** tras escribirlo: sin marcadores `{{…}}` sin rellenar, las
   dos vistas presentes y el toggle funcionando.

---

## 8. Reglas estrictas de contenido

- Todo en **español mexicano**, sencillo y directo.
- **NUNCA** muestres código de una solución. Solo **pseudocódigo**. Si hay un
  truco propio de un lenguaje, que sea **solo C++** y bien señalado.
- Las pistas **preguntan**, no afirman. La última pista sí es la solución completa.
- Contenido **original** en el formato socrático. Puedes consultar editoriales
  para entender, pero no copies soluciones ajenas al repo.

---

## 9. Decisiones abiertas

- **Orden de trabajo:** por ahora **cronológico (2003 → 2025)**, como ICPC. El
  usuario aún no decide si prefiere empezar por años recientes (2024/2025, que
  ejercitan mejor subtareas + tareas interactivas). Pregúntale si retomas.

---

## 10. Referencia rápida de comandos

```bash
# leer un enunciado
pdftotext -layout "IOI/2003/02 Comparing Code/statement.pdf" -

# crear la página de una tarea
cp IOI/TEMPLATE.html "IOI/2003/02 Comparing Code/index.html"

# (rellenar las dos vistas en ese index.html)

# regenerar índices + hub
python3 IOI/build_index.py

# commit (rutas EXPLÍCITAS por la sesión concurrente)
git add "IOI/2003/02 Comparing Code/index.html" IOI/PROGRESO.md IOI/index.html index.html
git commit -m "IOI 2003/02: traducción y upsolving (Comparing Code)"
git push origin HEAD
```
