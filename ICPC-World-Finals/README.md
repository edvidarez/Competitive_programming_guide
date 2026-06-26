# ICPC World Finals — Traducción y Upsolving en Español 🇲🇽

Este directorio organiza **todos los problemas de las World Finals del ICPC**
(2008 – 2024) para estudiarlos y resolverlos *upsolving* en español mexicano.

La meta: que cada problema tenga un archivo HTML autoexplicativo con **dos
vistas** — el enunciado traducido y una guía socrática de pistas que te lleva,
sin spoilearte de golpe, hasta la solución.

---

## 📁 Estructura

```
ICPC-World-Finals/
├── README.md          ← este archivo (guía para el agente de IA)
├── TEMPLATE.html      ← plantilla a copiar para cada problema
├── PROGRESO.md        ← checklist de avance (200 problemas)
│
├── 2008/
│   ├── problems.pdf   ← PDF oficial del concurso (SOLO enunciados, sin soluciones)
│   ├── A/             ← una carpeta por problema
│   │   └── A.html     ← (lo genera el agente a partir de TEMPLATE.html)
│   ├── B/
│   └── ... K/
├── 2009/
│   └── ...
└── 2024/
    └── ...
```

- Hay **17 años** (2008–2024) y **200 problemas** en total.
- Cada año contiene **únicamente** el `problems.pdf` oficial. **No se guardan
  soluciones** en este repo (ni PDFs de solución, ni editoriales, ni videos).
- Cada problema vive en su propia carpeta (`A/`, `B/`, …). Por ahora solo tiene
  un `.gitkeep`; el agente creará ahí el `LETRA.html`.

> Nota sobre 2022: en el PDF oficial los problemas están etiquetados **P–Z**
> (no A–L). Se respetó la numeración original del concurso.

---

## 🤖 Instrucciones para el agente de IA

Trabaja **problema por problema**. Para cada uno:

1. Abre `PROGRESO.md` y elige el primer problema sin marcar.
2. Lee el enunciado del problema en el `problems.pdf` de ese año (usa el
   número de página correcto; cada problema suele empezar en su propia hoja).
3. Copia `TEMPLATE.html` a la carpeta del problema con el nombre de la letra:
   `cp TEMPLATE.html 2008/A/A.html` (o el equivalente).
4. Rellena las **dos vistas** siguiendo las reglas de abajo.
5. Verifica que el HTML abre bien y que el botón cambia entre las dos vistas.
6. Marca el problema como hecho en `PROGRESO.md` y haz commit con un mensaje
   claro, p. ej. `2008/A: traducción y upsolving (Air Conditioning Machinery)`.

Avanza en orden cronológico (2008 → 2024) salvo que se indique otra cosa.

---

## 📝 Especificación del archivo `LETRA.html`

Cada archivo tiene **dos vistas** que se cambian con un clic (ya implementado
en `TEMPLATE.html`):

### Vista 1 — Enunciado
- **Traducción fiel y completa** del enunciado al **español mexicano**.
- Conserva el contexto/historia del problema, pero redáctalo claro y fácil.
- Incluye **Entrada**, **Salida** y un bloque de **Límites** bien resaltado
  (tiempo, memoria, y cada restricción de las variables como `1 ≤ n ≤ 10^5`).
- Incluye el/los **ejemplos** de entrada y salida tal cual el PDF.
- **🖼️ IMÁGENES CLAVE (obligatorio):** si el PDF tiene figuras/diagramas
  necesarios para entender el problema (formas, ejemplos visuales, esquemas),
  **extráelas del PDF y embébelas** en la Vista 1, justo donde el texto las
  menciona, con un `<figure>` y un pie de figura traducido. Úsalas también en
  la Vista 2 si ayudan al razonamiento. Embébelas como **data URI base64** para
  que el `.html` siga siendo autocontenido. Si la figura es vectorial (no es
  raster embebido), **renderiza la región** de la página (ver Detalles técnicos).
  No inventes diagramas: usa los del PDF.

### Vista 2 — Upsolving (socrática)
- Empieza con un **resumen mínimo**: quita la historia y todo lo que no sea
  parte del problema. Solo *qué te dan* y *qué hay que calcular*.
- Luego una **lista de pistas progresivas**, de lo general a lo específico.
  - Cada pista va **escondida** y se abre con un clic (elemento `<details>`).
  - El tono es **socrático**: pregunta, no afirmes. Ejemplos:
    *"¿Ya pensaste si te sirve verlo como un grafo?"*,
    *"¿Notaste que la respuesta es monótona?"*.
  - Empieza por la **idea clave / observación escondida** y baja en
    granularidad pista tras pista.
  - La **última pista ES el upsolving completo**: explicación paso a paso del
    algoritmo, por qué es correcto, y la complejidad.

### 🧮 Matemáticas con LaTeX (obligatorio)
- **Toda fórmula o expresión matemática va en LaTeX**, renderizada con
  **MathJax** (ya incluido y **autohospedado** en
  `assets/mathjax/tex-svg.js`; la plantilla ya lo carga).
- Escribe matemáticas en línea entre `\( ... \)` y en bloque entre `\[ ... \]`.
  Ejemplos: `\(1 \le n \le 10^5\)`, `\(\frac{n^4-6n^3+24}{24}\)`,
  `\(O(n\log n)\)`, `\(P(n)\equiv 0 \pmod D\)`.
- **No uses `<code>` para matemáticas.** `<code>` es solo para nombres de
  variables de programa, cadenas de salida, archivos y tokens literales.
- El **pseudocódigo** se queda en `<pre>` (MathJax no lo procesa, así debe ser).

### 🚫 Reglas de contenido (estrictas)
- **NUNCA** muestres código de una solución.
- Solo se permite **pseudocódigo** para describir el algoritmo.
- Si de verdad hay un **truco específico de un lenguaje**, que sea **solo C++**
  y bien señalado (p. ej. `__int128`, `nth_element`, `bitset`), nunca la
  solución completa en código.
- Todo en **español mexicano**, sencillo y directo.
- No metas soluciones ajenas al repo. Puedes consultar editoriales externas
  para entender el problema, pero el contenido debe ser **original** y en el
  formato socrático de arriba.

---

## 🔧 Detalles técnicos

- Los `LETRA.html` deben ser **autocontenidos**: todo el CSS/JS va dentro del
  archivo y las **imágenes embebidas** como data URI. La **única** dependencia
  compartida es MathJax, autohospedado en `assets/mathjax/tex-svg.js` y referido
  con ruta relativa `../../assets/mathjax/tex-svg.js` (no se usa ningún CDN).
- Para leer los PDFs puedes usar, por ejemplo, `pymupdf` (`import fitz`) o
  `pdftotext`. Algunos encabezados "Problem X" del PDF son imágenes; ubica el
  problema por su página/título si el texto no aparece.
- **Extraer figuras del PDF** (para la regla de imágenes clave):
  - Si la figura es una imagen raster embebida: `page.get_images()` +
    `doc.extract_image(xref)`.
  - Si es **vectorial** (lo más común en estos PDFs), renderiza solo su región:
    ```python
    import fitz, base64
    doc = fitz.open("problems.pdf"); page = doc[NUM_PAGINA]
    # ubica la franja con page.search_for("Figure 1") y/o page.get_drawings()
    clip = fitz.Rect(x0, y0, x1, y1)              # recorta SOLO la figura
    pix = page.get_pixmap(dpi=300, clip=clip); pix.save("fig.png")
    uri = "data:image/png;base64," + base64.b64encode(open("fig.png","rb").read()).decode()
    # pega 'uri' en el src del <img> del HTML
    ```
  - Recorta sin texto del enunciado alrededor; usa DPI ~300 para que se vea
    nítido. Borra el `.png` temporal: en el repo va embebido en el `.html`.
- Procedencia de los PDFs: [icpcarchive.github.io](https://github.com/icpcarchive/icpcarchive.github.io),
  carpeta `World Finals/ICPC World Finals/`. Aquí se copió **solo** `problems.pdf`
  de cada año.

---

## 📊 Avance

Lleva el control en [`PROGRESO.md`](PROGRESO.md). Hoy: **0 / 200** problemas.
