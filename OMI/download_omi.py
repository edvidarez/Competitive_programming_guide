#!/usr/bin/env python3
"""
Descargador idempotente del archivo OMI (Olimpiada Mexicana de Informática).

Lee `OMI/omi_inventory.json` (la fuente de verdad, parseada de la lista oficial
de problemas) y, para cada problema, crea su carpeta y baja lo disponible:

  OMI/<año>/<NN Título>/
    ├── statement.md      ← enunciado (markdown de omegaUp)         [versionado]
    ├── statement.pdf     ← enunciado (PDF oficial, si aplica)      [versionado]
    ├── images/           ← imágenes del enunciado (omegaUp)        [versionado]
    ├── meta.json         ← metadatos (edición, día, límites, urls) [versionado]
    └── _local/           ← casos, soluciones de referencia, etc.   [GITIGNORED]
        ├── cases.zip         (con --cases)
        ├── solution.cpp      (con --refs)
        ├── editorial.*       (con --refs)
        └── statement.html    (fallback DMOJ)

Prioridad del enunciado:  omegaUp API (markdown) > PDF oficial > DMOJ (HTML).

El estado "resuelto" de una tarea NO se guarda aquí: lo infiere build_index.py
de si existe `index.html` en la carpeta de la tarea.

Uso:
    python3 OMI/download_omi.py                      # enunciados + meta (TODO; ligero, versionable)
    python3 OMI/download_omi.py --years 2025         # solo un año
    python3 OMI/download_omi.py --years 2025 --cases --refs   # + casos y soluciones (a _local)
    python3 OMI/download_omi.py --cases              # baja TODOS los casos (varios GB, a _local)
    python3 OMI/download_omi.py --force              # vuelve a bajar aunque ya exista
"""
from __future__ import annotations
import argparse, base64, json, os, re, ssl, sys, time, urllib.request, urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))          # .../OMI
INV  = os.path.join(HERE, "omi_inventory.json")

UA = {"User-Agent": "Mozilla/5.0 (OMI-archive downloader; +https://github.com/edvidarez/Competitive_programming_guide)"}
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE   # algunos hosts viejos tienen cadenas TLS rotas


def fetch(url, timeout=40, tries=3):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
                return r.read()
        except Exception as e:                       # noqa: BLE001
            last = e
            time.sleep(0.6 * (i + 1))
    raise last


def fetch_json(url, **kw):
    return json.loads(fetch(url, **kw).decode("utf-8", "replace"))


# --- GitHub OMI-Archive (ediciones 2017–2023): casos/soluciones viven en
#     carpetas del repo, enlazadas como github.com/.../tree/<branch>/<path>. ---

def is_github_tree(url):
    return bool(url) and "github.com" in url and "/tree/" in url


def github_tree_files(url):
    """Lista (name, download_url) de los archivos de una carpeta del repo
    (un nivel; las carpetas cases/ y solutions/ del archivo son planas)."""
    m = re.match(r"https://github\.com/([^/]+)/([^/]+)/tree/([^/]+)/(.+)", url)
    if not m:
        return []
    owner, repo, branch, path = m.groups()
    api = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}?ref={branch}"
    try:
        items = fetch_json(api)
    except Exception:                                 # noqa: BLE001
        return []
    if not isinstance(items, list):
        return []
    return [(it["name"], it.get("download_url")) for it in items
            if it.get("type") == "file" and it.get("download_url")]


def download_github_dir(url, dstdir, force, limit=None):
    files = github_tree_files(url)
    if not files:
        return 0
    os.makedirs(dstdir, exist_ok=True)
    n = 0
    for name, durl in (files[:limit] if limit else files):
        dst = os.path.join(dstdir, name)
        if os.path.exists(dst) and not force:
            continue
        try:
            save(dst, fetch(durl, timeout=90)); n += 1
        except Exception:                             # noqa: BLE001
            pass
    return n


def slug_year(rec):
    return str(rec["year"])


def prob_dir(rec):
    return os.path.join(HERE, slug_year(rec), rec["folder"])


def save(path, data, mode="wb"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, mode) as f:
        f.write(data)


# ----------------------------------------------------------------------------- statements

def get_omegaup(rec, pdir, force):
    """Baja el enunciado markdown + imágenes desde la API pública de omegaUp."""
    alias = rec["omegaup_alias"]
    md_path = os.path.join(pdir, "statement.md")
    if os.path.exists(md_path) and not force:
        return "skip"
    url = f"https://omegaup.com/api/problem/details/?problem_alias={alias}"
    try:
        d = fetch_json(url)
    except Exception as e:                            # noqa: BLE001
        return f"ERR api: {e}"
    if d.get("status") != "ok":
        return f"ERR status={d.get('status')} ({d.get('error','')[:60]})"
    st = d.get("statement") or {}
    md = st.get("markdown") or ""
    if not md:
        return "ERR sin markdown"
    save(md_path, md.encode("utf-8"))
    # límites (para meta)
    rec["_limits"] = (d.get("settings") or {}).get("limits") or {}
    # imágenes (versionadas, junto al enunciado)
    imgs = st.get("images") or {}
    n = 0
    for name, val in imgs.items():
        try:
            if isinstance(val, str) and val.startswith("data:"):
                b = base64.b64decode(val.split(",", 1)[1])
            elif isinstance(val, str) and val.startswith("http"):
                b = fetch(val)
            else:
                b = base64.b64decode(val)
            safe = re.sub(r"[^A-Za-z0-9._-]", "_", name)
            save(os.path.join(pdir, "images", safe), b)
            n += 1
        except Exception:                             # noqa: BLE001
            pass
    return f"ok md+{n}img"


def get_pdf(rec, pdir, force):
    pdf_path = os.path.join(pdir, "statement.pdf")
    if os.path.exists(pdf_path) and not force:
        return "skip"
    try:
        b = fetch(rec["pdf_url"])
    except Exception as e:                            # noqa: BLE001
        rec["_statement_status"] = "dead-link"
        return f"ERR pdf (host caído?): {str(e)[:50]}"
    if not b[:4] == b"%PDF":
        rec["_statement_status"] = "not-a-pdf"
        return "ERR no parece PDF"
    save(pdf_path, b)
    return "ok pdf"


def get_dmoj(rec, pdir, force):
    """DMOJ no expone markdown público fácil; guardamos el HTML en _local como
    respaldo y dejamos la URL en meta para leer el enunciado al resolver."""
    html_path = os.path.join(pdir, "_local", "statement.html")
    if os.path.exists(html_path) and not force:
        return "skip"
    try:
        b = fetch(rec["statement_link"])
    except Exception as e:                            # noqa: BLE001
        return f"ERR dmoj: {str(e)[:50]}"
    save(html_path, b)
    rec["_statement_status"] = "dmoj-html (lee statement_link al resolver)"
    return "ok dmoj-html→_local"


# ----------------------------------------------------------------------------- heavy (gitignored)

def get_cases(rec, pdir, force):
    url = rec.get("casos")
    if not url:
        return None
    casesdir = os.path.join(pdir, "_local", "cases")
    # Ediciones del archivo (2017–2023): los casos son una carpeta de GitHub.
    if is_github_tree(url):
        if os.path.isdir(casesdir) and os.listdir(casesdir) and not force:
            return "skip"
        n = download_github_dir(url, casesdir, force)
        return f"ok github cases ({n} archivos)" if n else "ERR github cases vacío"
    # Resto (sitio oficial): un .zip directo.
    dst = os.path.join(pdir, "_local", "cases.zip")
    if os.path.exists(dst) and not force:
        return "skip"
    try:
        b = fetch(url, timeout=120)
    except Exception as e:                            # noqa: BLE001
        return f"ERR cases: {str(e)[:50]}"
    if b[:2] != b"PK":                                # no es un zip (HTML de error/redirección)
        return f"ERR cases: respuesta no-zip ({len(b)} bytes)"
    save(dst, b)
    return f"ok cases.zip ({len(b)//1024} KB)"


def get_refs(rec, pdir, force):
    msgs = []
    for key, name in (("codigos", "solution"), ("soluciones", "editorial")):
        url = rec.get(key)
        if not url:
            continue
        # Carpeta de GitHub (archivo 2017–2023): baja todos los archivos.
        if is_github_tree(url):
            d = os.path.join(pdir, "_local", f"{name}s")
            n = download_github_dir(url, d, force)
            # copia la primera solución .cpp/.c como _local/solution.cpp (lo que busca el solver)
            if name == "solution" and n:
                for fn in sorted(os.listdir(d)):
                    if fn.endswith((".cpp", ".cc", ".c", ".py", ".java")):
                        import shutil
                        shutil.copyfile(os.path.join(d, fn), os.path.join(pdir, "_local", "solution" + os.path.splitext(fn)[1]))
                        break
            msgs.append(f"{name}:{'ok('+str(n)+')' if n else 'ERR'}")
            continue
        ext = os.path.splitext(url.split("?")[0])[1] or ".bin"
        dst = os.path.join(pdir, "_local", f"{name}{ext}")
        if os.path.exists(dst) and not force:
            msgs.append(f"{name}:skip"); continue
        try:
            save(dst, fetch(url, timeout=60))
            msgs.append(f"{name}:ok")
        except Exception:                             # noqa: BLE001
            msgs.append(f"{name}:ERR")
    return ", ".join(msgs) if msgs else None


# ----------------------------------------------------------------------------- meta

META_FIELDS = ["edicion", "clave", "year", "num", "dia", "titulo", "judge",
               "statement_link", "omegaup_alias", "dmoj_code", "pdf_url",
               "casos", "codigos", "soluciones"]


def write_meta(rec, pdir):
    meta = {k: rec.get(k) for k in META_FIELDS}
    if rec.get("_limits"):
        meta["limits"] = rec["_limits"]
    if rec.get("_statement_status"):
        meta["statement_status"] = rec["_statement_status"]
    save(os.path.join(pdir, "meta.json"),
         (json.dumps(meta, ensure_ascii=False, indent=1) + "\n").encode("utf-8"))


# ----------------------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description="Descarga el archivo OMI.")
    ap.add_argument("--years", nargs="*", type=int, help="años a procesar (p. ej. 2025 2024)")
    ap.add_argument("--cases", action="store_true", help="baja casos de prueba a _local (pesado)")
    ap.add_argument("--refs", action="store_true", help="baja soluciones/códigos de referencia a _local")
    ap.add_argument("--statements-only", action="store_true", help="solo enunciados + meta (default)")
    ap.add_argument("--force", action="store_true", help="re-descarga aunque ya exista")
    ap.add_argument("--sleep", type=float, default=0.25, help="pausa entre requests")
    args = ap.parse_args()

    inv = json.load(open(INV, encoding="utf-8"))
    if args.years:
        inv = [r for r in inv if r["year"] in args.years]

    n_ok = n_err = 0
    for rec in inv:
        pdir = prob_dir(rec)
        os.makedirs(pdir, exist_ok=True)
        tag = f"{rec['edicion']:9s} {rec['num2']} {rec['titulo'][:26]:26s}"

        # --- enunciado (versionado) ---
        if rec.get("omegaup_alias"):
            st = get_omegaup(rec, pdir, args.force)
        elif rec.get("pdf_url"):
            st = get_pdf(rec, pdir, args.force)
        elif rec.get("dmoj_code"):
            st = get_dmoj(rec, pdir, args.force)
        else:
            st = "ERR sin fuente"
        if st and st.startswith("ERR"):
            n_err += 1
        else:
            n_ok += 1

        extra = []
        if args.cases and not args.statements_only:
            c = get_cases(rec, pdir, args.force)
            if c:
                extra.append(c)
        if args.refs and not args.statements_only:
            r = get_refs(rec, pdir, args.force)
            if r:
                extra.append(r)

        write_meta(rec, pdir)
        print(f"  {tag} | {st}" + (f" | {' | '.join(extra)}" if extra else ""))
        time.sleep(args.sleep)

    print(f"\nOMI descarga: {n_ok} enunciados OK, {n_err} con problema, sobre {len(inv)} tareas.")
    if n_err:
        print("  (Revisa los ERR: hosts caídos (cmirg.com) o DMOJ; el enunciado se lee de statement_link.)")


if __name__ == "__main__":
    main()
