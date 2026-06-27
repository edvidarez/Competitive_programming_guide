#!/usr/bin/env python3
"""
Regenera los índices del archivo OMI a partir del árbol de carpetas.

Es DETERMINISTA e IDEMPOTENTE: el estado "hecho" de cada tarea se infiere de si
existe su `index.html`. No hay estado manual que mantener.

Regenera:
  - OMI/index.html          (listado por edición/año, listo/pendiente, barra)
  - OMI/PROGRESO.md         (checklist con las cuentas por edición y el total)
  - index.html (raíz)       (actualiza la barra y el conteo de la tarjeta OMI)

Úsalo DESPUÉS de crear/terminar la `index.html` de una tarea:

    python3 OMI/build_index.py
"""
from __future__ import annotations
import json, os, re
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))     # .../OMI
REPO = os.path.dirname(HERE)


def edicion(year):
    return year - 1995            # 1996 -> 1ª, 2025 -> 30ª


def read_dia(full):
    try:
        m = json.load(open(os.path.join(full, "meta.json"), encoding="utf-8"))
        return m.get("dia") or ""
    except Exception:             # noqa: BLE001
        return ""


def scan():
    years = sorted(int(d) for d in os.listdir(HERE) if re.fullmatch(r"\d{4}", d))
    data = []
    for y in years:
        ydir = os.path.join(HERE, str(y))
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
            tasks.append((num, title, name, has, read_dia(full)))
        tasks.sort()
        data.append((y, tasks))
    return data


def write_progreso(data):
    total = sum(len(t) for _, t in data)
    done = sum(1 for _, t in data for x in t if x[3])
    out = [
        "# Progreso de transcripción y upsolving — OMI", "",
        f"Total de problemas: **{total}** · Completados: **{done} / {total}**", "",
        "Marca `[x]` cuando el `index.html` del problema esté terminado y revisado.",
        "Cada problema vive en `OMI/<año>/<NN Título>/` junto a su enunciado",
        "(`statement.md` o `statement.pdf`) y su `meta.json`. Copia `TEMPLATE.html`",
        "ahí como `index.html` y rellena las dos vistas (enunciado fiel + upsolving).", "",
        "> Este archivo se regenera con `python3 OMI/build_index.py` (el estado",
        "> hecho/pendiente se infiere de si existe el `index.html` de cada tarea).", "",
        "> Recordatorio OMI: el enunciado YA está en español (transcríbelo, no lo",
        "> traduzcas). Es E/S clásica (stdin/stdout). Las ediciones modernas (≈2017+)",
        "> usan **subtareas**; las ediciones 9ª–21ª tienen un día de **Karel**.", "",
    ]
    for y, tasks in data:
        yd = sum(1 for x in tasks if x[3])
        ed = edicion(y)
        out += [f"\n## {ed}ª OMI · {y} — {yd} / {len(tasks)}", "",
                "| ✓ | # | Día | Título | Archivo |", "|---|---|-----|--------|---------|"]
        for num, title, name, has, dia in tasks:
            mark = "x" if has else " "
            out.append(f"| [{mark}] | {num} | {dia} | {title} | `{y}/{name}/index.html` |")
    with open(os.path.join(HERE, "PROGRESO.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    return done, total


def write_index(data):
    total = sum(len(t) for _, t in data)
    done = sum(1 for _, t in data for x in t if x[3])
    pct = round(100 * done / total, 1) if total else 0
    blocks = []
    # más reciente primero para que la edición vigente quede arriba y abierta
    for i, (y, tasks) in enumerate(reversed(data)):
        yd = sum(1 for x in tasks if x[3])
        ed = edicion(y)
        lis = []
        for num, title, name, has, dia in tasks:
            href = quote(f"{y}/{name}/index.html")
            diahtml = f' <span class="dia">{dia}</span>' if dia else ""
            if has:
                lis.append(f'<li class="ok"><a href="{href}"><span class="lt">{num}</span> {title}</a>{diahtml} <span class="tag done">listo</span></li>')
            else:
                lis.append(f'<li class="pend"><span class="lt">{num}</span> {title}{diahtml} <span class="tag pend">pendiente</span></li>')
        op = " open" if i == 0 else ""
        blocks.append(
            f'    <details class="year"{op}>\n'
            f'      <summary>{ed}ª OMI <span class="yr">{y}</span> <span class="count">{yd}/{len(tasks)}</span></summary>\n'
            f'      <ul>' + "".join(lis) + '</ul>\n'
            f'    </details>')
    y0, y1 = data[0][0], data[-1][0]
    html = f'''<!DOCTYPE html>
<html lang="es-MX"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>OMI — Transcripción y Upsolving (ES-MX)</title>
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
 details.year>summary{{cursor:pointer;list-style:none;padding:14px 16px;font-weight:700;font-size:18px;display:flex;justify-content:space-between;align-items:center;gap:8px}}
 details.year>summary::-webkit-details-marker{{display:none}}
 .yr{{color:var(--muted);font-weight:500;font-size:14px;margin-right:auto}}
 .count{{color:var(--muted);font-weight:500;font-size:14px}}
 ul{{list-style:none;margin:0;padding:6px 12px 14px}}
 li{{padding:8px 10px;border-radius:8px;display:flex;align-items:center;gap:10px}}
 li.ok:hover{{background:var(--panel2)}}
 li a{{color:var(--ink);text-decoration:none;flex:1}}
 li.pend{{color:var(--muted)}}
 li.pend a{{flex:1}}
 .lt{{display:inline-block;width:24px;font-weight:700;color:var(--accent);text-align:center}}
 .dia{{font-size:11px;color:var(--muted);border:1px solid var(--border);border-radius:99px;padding:1px 8px}}
 .tag{{font-size:11px;padding:2px 8px;border-radius:99px;border:1px solid var(--border)}}
 .tag.done{{color:var(--accent2)}} .tag.pend{{color:var(--muted)}}
 footer{{color:var(--muted);font-size:13px;margin-top:30px;border-top:1px solid var(--border);padding-top:14px}}
</style></head><body><div class="wrap">
 <a class="back" href="../index.html">← Inicio</a>
 <h1>OMI · Transcripción y Upsolving 🇲🇽</h1>
 <p class="sub">Olimpiada Mexicana de Informática — enunciados (en español) + guía socrática de pistas (upsolving). {edicion(y0)}ª–{edicion(y1)}ª OMI ({y0}–{y1}).</p>
 <div class="bar"><i></i></div>
 <p class="prog">{done} / {total} problemas con HTML listo</p>

{chr(10).join(blocks)}
 <footer>Cada problema tiene dos vistas: <b>Enunciado</b> (transcripción fiel + límites + subtareas) y
  <b>Upsolving</b> (pistas socráticas, sin código). Enunciados originales: olimpiadadeinformatica.org.mx, omegaUp, DMOJ.</footer>
</div></body></html>
'''
    with open(os.path.join(HERE, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    return done, total, pct


def patch_root_hub(done, total, pct):
    """Actualiza barra y conteo de la tarjeta OMI en el hub raíz (best-effort)."""
    path = os.path.join(REPO, "index.html")
    try:
        html = open(path, encoding="utf-8").read()
    except OSError:
        return "no se encontró index.html raíz"
    m = re.search(r'href="OMI/index\.html".*?</a>', html, re.S)
    if not m:
        return "no se encontró la tarjeta OMI en el hub raíz (agrégala a mano una vez)"
    block = m.group(0)
    nb = re.sub(r'width:[\d.]+%', f'width:{pct}%', block, count=1)
    nb = re.sub(r'\d+\s*/\s*\d+\s*problemas', f'{done} / {total} problemas', nb, count=1)
    if nb != block:
        open(path, "w", encoding="utf-8").write(html[:m.start()] + nb + html[m.end():])
        return f"hub raíz actualizado ({done}/{total}, {pct}%)"
    return "hub raíz ya estaba al día"


def main():
    data = scan()
    write_progreso(data)
    done, total, pct = write_index(data)
    msg = patch_root_hub(done, total, pct)
    print(f"OMI índices regenerados: {done}/{total} problemas ({pct}%) en {len(data)} ediciones.")
    print(f"  - {msg}")


if __name__ == "__main__":
    main()
