# OMI — Olimpiada Mexicana de Informática (archivo de problemas) 🇲🇽

Problem sets históricos de la **OMI**, extraídos de la lista oficial
[olimpiadadeinformatica.org.mx/Resultados/Problemas](https://www.olimpiadadeinformatica.org.mx/Resultados/Problemas)
(enunciados en omegaUp/DMOJ/PDF y casos de prueba), organizados igual que
[`../IOI/`](../IOI/) y [`../ICPC-World-Finals/`](../ICPC-World-Finals/).

Cobertura: **1ª OMI (1996) – 30ª OMI (2025)** — 30 ediciones, **190 problemas**.

A diferencia de IOI/ICPC, **los enunciados de la OMI ya están en español**: aquí
no se traduce, se **transcribe con fidelidad** y se agrega la guía socrática de
upsolving.

---

## 📁 Estructura

```
OMI/
├── README.md
├── HANDOFF.md             ← LÉELO PRIMERO si continúas sin contexto
├── PROGRESO.md            ← checklist de avance (190 problemas, generado)
├── TEMPLATE.html          ← plantilla a copiar para cada tarea (como index.html)
├── omi_inventory.json     ← fuente de verdad (parseada de la lista oficial)
├── download_omi.py        ← descargador idempotente (enunciados, casos, soluciones)
├── build_index.py         ← regenera PROGRESO.md, OMI/index.html y la tarjeta del hub
├── assets/mathjax/        ← MathJax autohospedado (lo usa cada index.html)
│
└── 2025/                  ← año = 1995 + número de edición (2025 = 30ª OMI)
    ├── 01 El fucho/
    │   ├── statement.md / statement.pdf   ← enunciado oficial       (SÍ se versiona)
    │   ├── images/                        ← figuras del enunciado   (SÍ se versiona)
    │   ├── meta.json                      ← edición, día, límites    (SÍ se versiona)
    │   ├── index.html                     ← transcripción + upsolving (lo genera el agente)
    │   └── _local/                        ← casos / soluciones       (NO se versiona)
    └── ...
```

- **Una carpeta por problema** (`NN Título/`), numeradas en el orden oficial de la
  edición (Día 1 → Día 2, o Karel → Lenguaje).
- Lo que **no** es enunciado (casos, soluciones de referencia, HTML de DMOJ) vive
  en `<año>/<NN Título>/_local/` y está **ignorado por git** (ver `.gitignore`).

---

## 🤖 Transcripción y upsolving (workflow)

> 📋 **¿Continúas sin contexto previo?** Lee primero [`HANDOFF.md`](HANDOFF.md):
> estado, procedimiento paso a paso, de dónde sale cada enunciado, gotchas y
> reglas. Los índices se regeneran con `python3 OMI/build_index.py`.

Cada problema tiene una página HTML autoexplicativa con **dos vistas**: el
**enunciado** (transcripción fiel en español) y una guía **socrática** de pistas
que lleva al upsolving sin spoilear de golpe. Para cada problema:

1. Abre [`PROGRESO.md`](PROGRESO.md) y elige el primer problema sin marcar.
2. Lee su `statement.md`/`statement.pdf` (o `meta.json -> statement_link` en DMOJ).
3. Copia la plantilla: `cp TEMPLATE.html "2025/01 El fucho/index.html"`.
4. Rellena las dos vistas siguiendo las reglas dentro de `TEMPLATE.html`.
5. **Verifica tu solución** contra el ejemplo y los casos (`--cases`) antes de la
   Vista 2.
6. Regenera índices y haz commit (rutas explícitas).

> ⚠️ Diferencias OMI (ya integradas en la plantilla): enunciado **en español**
> (transcribe, no traduzcas); **E/S clásica** (stdin/stdout); **subtareas** en la
> era moderna; un día de **Karel** (ediciones 9ª–21ª). Regla estricta: **nunca**
> código de solución, solo pseudocódigo (o primitivas de Karel); matemáticas en
> LaTeX con MathJax; todo autocontenido.

---

## 🔧 Descargar / actualizar

El descargador es **idempotente** (solo baja lo que falta):

```bash
python3 OMI/download_omi.py                      # enunciados + meta (TODO; ligero, versionable)
python3 OMI/download_omi.py --years 2025         # un año
python3 OMI/download_omi.py --years 2025 --cases --refs   # + casos y soluciones (a _local)
python3 OMI/download_omi.py --cases              # TODOS los casos (varios GB, a _local)
python3 OMI/download_omi.py --force              # vuelve a bajar aunque ya exista
```

Fuentes de enunciado, por preferencia: **API de omegaUp** (markdown) → **PDF
oficial** → **DMOJ** (HTML / URL). Cuando se celebre una OMI nueva, vuelve a
parsear la lista oficial para regenerar `omi_inventory.json` y corre el script.

---

## 🌐 Para practicar (jueces en línea)

- **[omegaUp](https://omegaup.com/)** — la mayoría de los problemas OMI; envía y autocalifica.
- **[DMOJ OMI](https://dmoj.olimpiadadeinformatica.org.mx/)** — ediciones recientes (p. ej. 2025).

## 📜 Procedencia

Todo el material proviene del archivo oficial de la OMI
([olimpiadadeinformatica.org.mx](https://www.olimpiadadeinformatica.org.mx/Resultados/Problemas)),
omegaUp y el repositorio
[ComiteMexicanoDeInformatica/OMI-Archive](https://github.com/ComiteMexicanoDeInformatica/OMI-Archive)
(redacciones, casos y soluciones oficiales, 2017–2023).
