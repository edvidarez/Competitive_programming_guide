# IOI — International Olympiad in Informatics (archivo de problemas) 🌍

Problem sets históricos del **IOI**, descargados del sitio oficial
[ioinformatics.org](https://ioinformatics.org/page/contests/10) y organizados
de forma similar a [`../ICPC-World-Finals/`](../ICPC-World-Finals/).

Cobertura actual: **IOI 2003 – 2025** (la *era moderna*, con material completo
y disponible en jueces en línea como [oj.uz](https://oj.uz/problems/source/ioi)
y el [archivo IOI de Codeforces](https://ioi.contest.codeforces.com/)).

---

## 📁 Estructura

```
IOI/
├── README.md
├── download_ioi.py        ← descargador idempotente (regenera todo)
│
├── 2024/
│   ├── 01 Nile/
│   │   └── statement.pdf       ← enunciado oficial  (SÍ se versiona)
│   ├── 02 Message/
│   │   └── statement.pdf
│   ├── ... 06 Sphinx's Riddle/
│   └── _local/                 ← material pesado  (NO se versiona, ver .gitignore)
│       ├── ioi2024tests.zip        ← casos de prueba oficiales
│       ├── ioi2024solutions.zip    ← soluciones de referencia (.zip o .pdf)
│       └── ioi2024practice.zip     ← problemas de práctica (Día 0)
├── 2023/
└── ...
```

- **Una carpeta por tarea** (`NN Nombre/`), con el `statement.pdf` oficial.
- Cada año numera sus tareas como en el sitio oficial (`problem1`, `problem2`, …).
- Todo lo que **no** es enunciado (tests, soluciones, práctica) vive en
  `<año>/_local/` y está **ignorado por git** — se conserva en tu disco para uso
  personal pero **no se publica** en GitHub.

> ⚠️ El `.gitignore` de la raíz excluye `IOI/*/_local/`. No quites esa regla:
> ahí viven las soluciones y los casos de prueba que no deben subirse.

---

## 🔧 Regenerar / actualizar

El script es **idempotente** (solo baja lo que falta):

```bash
python3 IOI/download_ioi.py                    # todo, 2003–2025
python3 IOI/download_ioi.py --years 2025       # un año
python3 IOI/download_ioi.py --statements-only  # solo enunciados (lo de git)
python3 IOI/download_ioi.py --no-tests         # todo menos los .zip de tests
```

Cuando se celebre un IOI nuevo, agrega su `año: id_de_página` al diccionario
`YEAR_PAGE` dentro de `download_ioi.py` (el id sale del índice de Ediciones del
sitio oficial) y vuelve a correr el script.

---

## 🌐 Para practicar (jueces en línea)

- **[oj.uz](https://oj.uz/problems/source/ioi)** — envía y autocalifica, IOI 2003–2025.
- **[Codeforces IOI archive](https://ioi.contest.codeforces.com/)** — un concurso por día de cada IOI desde 2002.
- **[Yandex.Contest](https://contest.yandex.com/ioi/)** — IOI 2003–2018, registro abierto.

## 📜 Procedencia

Todo el material proviene del archivo oficial del IOI en
[ioinformatics.org](https://ioinformatics.org/page/contests/10) («each link
contains problems, test cases and/or solutions»). Los enunciados/tareas del IOI
se publican bajo **CC-BY**.
