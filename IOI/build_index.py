#!/usr/bin/env python3
"""
Regenera los índices del archivo IOI a partir del árbol de carpetas.

Es DETERMINISTA e IDEMPOTENTE: el estado "hecho" de cada tarea se infiere de si
existe su `index.html`. No hay estado manual que mantener.

Regenera:
  - IOI/index.html          (listado por año, listo/pendiente, barra de avance)
  - IOI/PROGRESO.md         (checklist con las cuentas por año y el total)
  - index.html (raíz)       (actualiza la barra y el conteo de la tarjeta IOI)

Úsalo DESPUÉS de crear/terminar la `index.html` de una tarea:

    python3 IOI/build_index.py
"""
from __future__ import annotations
import os, re
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))     # .../IOI
REPO = os.path.dirname(HERE)


def scan():
    years = sorted(d for d in os.listdir(HERE) if re.fullmatch(r"\d{4}", d))
    data = []
    for y in years:
        ydir = os.path.join(HERE, y)
        tasks = []
        for name in os.listdir(ydir):
            full = os.path.join(ydir, name)
            if not os.path.isdir(full) or name == "_local":
                continue
            m = re.match(r"(\d+)\s+(.*)", name)
            if not m:
                continue
            num, title = int(m.group(1)), m.group(2)
            has = os.path.exists(os.path.join(full, "index.html"))
            tasks.append((num, title, name, has))
        tasks.sort()
        data.append((y, tasks))
    return data


def write_progreso(data):
    total = sum(len(t) for _, t in data)
    done = sum(1 for _, t in data for x in t if x[3])
    out = [
        "# Progreso de traducción y upsolving — IOI", "",
        f"Total de tareas: **{total}** · Completadas: **{done} / {total}**", "",
        "Marca `[x]` cuando el `index.html` de la tarea esté terminado y revisado.",
        "Avanza por años; cada tarea vive en `IOI/<año>/<NN Título>/` junto a su",
        "`statement.pdf`. Copia `TEMPLATE.html` ahí como `index.html` y rellena las dos",
        "vistas (enunciado traducido + upsolving socrático).", "",
        "> Este archivo se regenera con `python3 IOI/build_index.py` (el estado",
        "> hecho/pendiente se infiere de si existe el `index.html` de cada tarea).", "",
        "> Recordatorio IOI: el puntaje es por **subtareas** con crédito parcial, y",
        "> muchas tareas son **interactivas/funcionales** (implementas funciones, no",
        "> lees stdin). La plantilla ya trae secciones para ambas cosas.", "",
    ]
    for y, tasks in data:
        yd = sum(1 for x in tasks if x[3])
        out += [f"\n## IOI {y} — {yd} / {len(tasks)}", "",
                "| ✓ | # | Título | Archivo |", "|---|---|--------|---------|"]
        for num, title, name, has in tasks:
            mark = "x" if has else " "
            out.append(f"| [{mark}] | {num} | {title} | `{y}/{name}/index.html` |")
    with open(os.path.join(HERE, "PROGRESO.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    return done, total


def write_index(data):
    total = sum(len(t) for _, t in data)
    done = sum(1 for _, t in data for x in t if x[3])
    pct = round(100 * done / total, 1) if total else 0
    blocks = []
    for i, (y, tasks) in enumerate(data):
        yd = sum(1 for x in tasks if x[3])
        lis = []
        for num, title, name, has in tasks:
            href = quote(f"{y}/{name}/index.html")
            if has:
                lis.append(f'<li class="ok"><a href="{href}"><span class="lt">{num}</span> {title}</a> <span class="tag done">listo</span></li>')
            else:
                lis.append(f'<li class="pend"><span class="lt">{num}</span> {title} <span class="tag pend">pendiente</span></li>')
        op = " open" if i == 0 else ""
        blocks.append(
            f'    <details class="year"{op}>\n'
            f'      <summary>{y} <span class="count">{yd}/{len(tasks)}</span></summary>\n'
            f'      <ul>' + "".join(lis) + '</ul>\n'
            f'    </details>')
    html = f'''<!DOCTYPE html>
<html lang="es-MX"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>IOI — Traducción y Upsolving (ES-MX)</title>
<style>
 :root{{--bg:#0f1320;--panel:#171c2e;--panel2:#1f2540;--ink:#e8ecf6;--muted:#9aa6c4;
  --accent:#5b8cff;--accent2:#34d399;--warn:#fbbf24;--border:#2a3252}}
 *{{box-sizing:border-box}} body{{margin:0;background:var(--bg);color:var(--ink);
  font-family:system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;line-height:1.6}}
 .wrap{{max-width:820px;margin:0 auto;padding:28px 20px 80px}}
 a.back{{color:var(--muted);text-decoration:none;font-size:14px}}
 a.back:hover{{color:var(--accent)}}
 h1{{font-size:26px;margin:8px 0 0}} .sub{{color:var(--muted);margin:6px 0 0}}
 .bar{{height:10px;background:var(--panel2);border:1px solid var(--border);border-radius:99px;margin:18px 0 6px;overflow:hidden}}
 .bar > i{{display:block;height:100%;background:linear-gradient(90deg,var(--accent),var(--accent2));width:{pct}%}}
 .prog{{color:var(--muted);font-size:14px}}
 details.year{{border:1px solid var(--border);border-radius:12px;margin:12px 0;background:var(--panel);overflow:hidden}}
 details.year>summary{{cursor:pointer;list-style:none;padding:14px 16px;font-weight:700;font-size:18px;display:flex;justify-content:space-between;align-items:center}}
 details.year>summary::-webkit-details-marker{{display:none}}
 .count{{color:var(--muted);font-weight:500;font-size:14px}}
 ul{{list-style:none;margin:0;padding:6px 12px 14px}}
 li{{padding:8px 10px;border-radius:8px;display:flex;align-items:center;gap:10px}}
 li.ok:hover{{background:var(--panel2)}}
 li a{{color:var(--ink);text-decoration:none;flex:1}}
 li.pend{{color:var(--muted)}}
 .lt{{display:inline-block;width:24px;font-weight:700;color:var(--accent);text-align:center}}
 .tag{{font-size:11px;padding:2px 8px;border-radius:99px;border:1px solid var(--border)}}
 .tag.done{{color:var(--accent2)}} .tag.pend{{color:var(--muted)}}
 footer{{color:var(--muted);font-size:13px;margin-top:30px;border-top:1px solid var(--border);padding-top:14px}}
</style></head><body><div class="wrap">
 <a class="back" href="../index.html">← Inicio</a>
 <h1>IOI · Traducción y Upsolving 🌍</h1>
 <p class="sub">International Olympiad in Informatics — enunciados traducidos al español + guía socrática de pistas (upsolving). {data[0][0]}–{data[-1][0]}.</p>
 <div class="bar"><i></i></div>
 <p class="prog">{done} / {total} tareas con HTML listo</p>

{chr(10).join(blocks)}
 <footer>Cada tarea tiene dos vistas: <b>Enunciado</b> (traducción + límites + subtareas) y
  <b>Upsolving</b> (pistas socráticas, sin código). PDFs originales: ioinformatics.org.</footer>
</div></body></html>
'''
    with open(os.path.join(HERE, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    return done, total, pct


def patch_root_hub(done, total, pct):
    """Actualiza barra y conteo de la tarjeta IOI en el hub raíz (best-effort)."""
    path = os.path.join(REPO, "index.html")
    try:
        html = open(path, encoding="utf-8").read()
    except OSError:
        return "no se encontró index.html raíz"
    m = re.search(r'href="IOI/index\.html".*?</a>', html, re.S)
    if not m:
        return "no se encontró la tarjeta IOI en el hub raíz (sin cambios)"
    block = m.group(0)
    nb = re.sub(r'width:[\d.]+%', f'width:{pct}%', block, count=1)
    nb = re.sub(r'\d+\s*/\s*\d+\s*tareas', f'{done} / {total} tareas', nb, count=1)
    if nb != block:
        open(path, "w", encoding="utf-8").write(html[:m.start()] + nb + html[m.end():])
        return f"hub raíz actualizado ({done}/{total}, {pct}%)"
    return "hub raíz ya estaba al día"


def main():
    data = scan()
    write_progreso(data)
    done, total, pct = write_index(data)
    msg = patch_root_hub(done, total, pct)
    print(f"IOI índices regenerados: {done}/{total} tareas ({pct}%) en {len(data)} años.")
    print(f"  - {msg}")


if __name__ == "__main__":
    main()
