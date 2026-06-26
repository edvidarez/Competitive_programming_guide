#!/usr/bin/env python3
"""
Descarga estructurada de los problem sets históricos del IOI
(International Olympiad in Informatics) desde el sitio oficial
https://ioinformatics.org

Estructura generada (similar a ICPC-World-Finals/):

    IOI/
      <año>/
        01 Trail Maintenance/
          statement.pdf          <- enunciado oficial (SÍ se sube a git)
        02 Comparing Code/
          statement.pdf
        ...
        _local/                  <- material pesado / NO se sube (ver .gitignore)
          ioi2003tests.zip       <- casos de prueba oficiales
          ioi2003solutions.zip   <- soluciones de referencia (.zip o .pdf)
          ioi2003practice.zip    <- problemas de práctica (Día 0)

Reglas:
  - Los enunciados (statement.pdf) son lo único que se versiona en git.
  - tests / solutions / practice viven en `_local/` (ignorado por .gitignore),
    se conservan en disco para uso personal pero NO se publican.

Uso:
    python3 IOI/download_ioi.py                 # todo, 2003-2025
    python3 IOI/download_ioi.py --years 2024 2025
    python3 IOI/download_ioi.py --statements-only
    python3 IOI/download_ioi.py --no-tests      # omite los .zip de tests (pesados)

Es idempotente: vuelve a correrlo y solo descarga lo que falte.
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import urllib.request
from html import unescape

BASE = "https://ioinformatics.org"
HERE = os.path.dirname(os.path.abspath(__file__))

# año -> id de página en /page/ioi-<año>/<id>  (extraído del índice de Ediciones)
YEAR_PAGE = {
    2003: 29, 2004: 30, 2005: 31, 2006: 32, 2007: 33, 2008: 34, 2009: 35,
    2010: 36, 2011: 37, 2012: 38, 2013: 39, 2014: 40, 2015: 41, 2016: 42,
    2017: 43, 2018: 49, 2019: 51, 2020: 54, 2021: 55, 2022: 56, 2023: 58,
    2024: 59, 2025: 60,
}

ANCHOR_RE = re.compile(
    r'<a\b[^>]*href="(?P<href>/files/[^"]+\.(?:pdf|zip|tgz|tar\.gz|gz))"[^>]*>(?P<text>.*?)</a>',
    re.IGNORECASE | re.DOTALL,
)
TAG_RE = re.compile(r"<[^>]+>")
PROBLEM_RE = re.compile(r"problem(\d+)\.pdf$", re.IGNORECASE)


def log(msg: str) -> None:
    print(msg, flush=True)


def fetch_html(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (IOI-archive-downloader)"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8", "replace")


def clean_text(raw: str) -> str:
    return unescape(TAG_RE.sub("", raw)).strip()


def safe_name(name: str) -> str:
    # nombre de carpeta legible y seguro: solo se neutraliza lo que rompe el FS
    name = name.replace("/", "-").replace(":", " -")
    name = re.sub(r"\s+", " ", name).strip().rstrip(". ")
    return name or "Untitled"


def classify(href: str, text: str):
    """Devuelve (categoria, info). categoria in {statement, tests, solutions, practice, other}."""
    fname = href.rsplit("/", 1)[-1].lower()
    m = PROBLEM_RE.search(fname)
    if m and "solution" not in fname and "practice" not in fname:
        return "statement", int(m.group(1))
    if "test" in fname:
        return "tests", None
    if "solution" in fname:
        return "solutions", None
    if "practice" in fname:
        return "practice", None
    return "other", None


def download(url: str, dest: str) -> str:
    """Descarga con curl (reanuda, sigue redirecciones). Devuelve 'ok'|'skip'|'fail'."""
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        return "skip"
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    tmp = dest + ".part"
    rc = subprocess.run(
        ["curl", "-fL", "--retry", "3", "--retry-delay", "2",
         "-C", "-", "-A", "Mozilla/5.0 (IOI-archive-downloader)",
         "-o", tmp, url],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    ).returncode
    if rc == 0 and os.path.exists(tmp) and os.path.getsize(tmp) > 0:
        os.replace(tmp, dest)
        return "ok"
    # curl -C - falla si el .part ya está completo en algunos servidores: reintenta limpio
    if os.path.exists(tmp):
        os.remove(tmp)
    rc = subprocess.run(
        ["curl", "-fL", "--retry", "3", "-A", "Mozilla/5.0 (IOI-archive-downloader)",
         "-o", tmp, url],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    ).returncode
    if rc == 0 and os.path.exists(tmp) and os.path.getsize(tmp) > 0:
        os.replace(tmp, dest)
        return "ok"
    if os.path.exists(tmp):
        os.remove(tmp)
    return "fail"


def human(n: int) -> str:
    f = float(n)
    for unit in ("B", "KB", "MB", "GB"):
        if f < 1024 or unit == "GB":
            return f"{f:.1f}{unit}"
        f /= 1024
    return f"{f:.1f}GB"


def process_year(year: int, page_id: int, args) -> dict:
    url = f"{BASE}/page/ioi-{year}/{page_id}"
    log(f"\n=== IOI {year}  ({url}) ===")
    try:
        html = fetch_html(url)
    except Exception as e:  # noqa: BLE001
        log(f"  !! no se pudo abrir la página: {e}")
        return {"year": year, "error": str(e)}

    links = []
    for m in ANCHOR_RE.finditer(html):
        href = m.group("href")
        text = clean_text(m.group("text"))
        links.append((href, text))
    # de-dup conservando orden
    seen = set()
    links = [(h, t) for (h, t) in links if not (h in seen or seen.add(h))]

    year_dir = os.path.join(HERE, str(year))
    local_dir = os.path.join(year_dir, "_local")
    counts = {"statement": 0, "tests": 0, "solutions": 0, "practice": 0, "other": 0}
    failed = []
    statements = []

    for href, text in links:
        cat, info = classify(href, text)
        full = BASE + href
        fname = href.rsplit("/", 1)[-1]

        if cat == "statement":
            n = info
            folder = os.path.join(year_dir, f"{n:02d} {safe_name(text)}")
            dest = os.path.join(folder, "statement.pdf")
            statements.append((n, safe_name(text)))
        elif args.statements_only:
            continue
        elif cat == "tests" and args.no_tests:
            log(f"  (omitido tests) {fname}")
            continue
        else:
            dest = os.path.join(local_dir, fname)

        status = download(full, dest)
        counts[cat] += 1 if status != "fail" else 0
        if status == "ok":
            log(f"  ✓ {cat:10s} {fname}  ({human(os.path.getsize(dest))})  «{text}»")
        elif status == "skip":
            log(f"  · {cat:10s} {fname}  (ya estaba)")
        else:
            log(f"  ✗ {cat:10s} {fname}  FALLÓ")
            failed.append(fname)

    log(f"  -> {counts['statement']} enunciados"
        + ("" if args.statements_only else
           f", {counts['tests']} tests, {counts['solutions']} solutions, "
           f"{counts['practice']} practice, {counts['other']} otros"))
    return {"year": year, "counts": counts, "failed": failed,
            "statements": sorted(statements)}


def main() -> int:
    ap = argparse.ArgumentParser(description="Descarga estructurada de problem sets del IOI.")
    ap.add_argument("--years", nargs="*", type=int, help="años específicos (default: 2003-2025)")
    ap.add_argument("--statements-only", action="store_true",
                    help="solo enunciados PDF (lo que se sube a git)")
    ap.add_argument("--no-tests", action="store_true",
                    help="descarga todo menos los .zip de casos de prueba (pesados)")
    args = ap.parse_args()

    years = sorted(args.years) if args.years else sorted(YEAR_PAGE)
    unknown = [y for y in years if y not in YEAR_PAGE]
    if unknown:
        log(f"Años sin mapeo: {unknown}. Disponibles: {sorted(YEAR_PAGE)}")
        return 2

    log(f"Descargando IOI {years[0]}–{years[-1]} en {HERE}")
    results = [process_year(y, YEAR_PAGE[y], args) for y in years]

    total_st = sum(r.get("counts", {}).get("statement", 0) for r in results)
    all_failed = [(r["year"], f) for r in results for f in r.get("failed", [])]
    log("\n========== RESUMEN ==========")
    log(f"Enunciados descargados (a versionar): {total_st}")
    if all_failed:
        log(f"Descargas fallidas: {len(all_failed)}")
        for y, f in all_failed:
            log(f"   {y}: {f}")
    else:
        log("Sin fallos.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
