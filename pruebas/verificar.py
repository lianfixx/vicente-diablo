#!/usr/bin/env python3
"""Verificación local del repositorio Vicente Diablo. Sin red y sin dependencias.

Uso: python3 pruebas/verificar.py
Comprueba: (1) hashes del manifiesto de la copia recuperada, (2) enlaces y recursos
locales de las páginas HTML de la raíz, (3) que cada entrada del CHANGELOG tenga
«Agente:», y (4) que no haya patrones de secretos en archivos versionables.
"""
import hashlib, pathlib, re, sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
fallos = []


def hashes():
    total = 0
    for man in sorted(RAIZ.glob("recuperado/*/MANIFIESTO.sha256")):
        vistos = set()
        for linea in man.read_text(encoding="utf-8").splitlines():
            esperado, _, rel = linea.partition("  ")
            archivo = man.parent / rel
            vistos.add(rel)
            if not archivo.is_file():
                fallos.append(f"manifiesto: falta {archivo.relative_to(RAIZ)}")
            elif hashlib.sha256(archivo.read_bytes()).hexdigest() != esperado:
                fallos.append(f"manifiesto: hash distinto en {archivo.relative_to(RAIZ)}")
            total += 1
        for sub in ("sitio", "texto-renderizado"):
            for f in (man.parent / sub).rglob("*"):
                if f.is_file() and f.relative_to(man.parent).as_posix() not in vistos:
                    fallos.append(f"manifiesto: sin registrar {f.relative_to(RAIZ)}")
    return total


def enlaces():
    total = 0
    for pagina in sorted(RAIZ.glob("*.html")):
        texto = pagina.read_text(encoding="utf-8")
        for ref in re.findall(r'(?:href|src)="([^"]+)"', texto):
            if re.match(r"(https?:|mailto:|tel:|#|data:)", ref):
                if ref.startswith("http") and "chatgpt.site/images" in ref:
                    fallos.append(f"{pagina.name}: imagen enlazada al sitio de origen ({ref})")
                continue
            total += 1
            if not (RAIZ / ref.split("#")[0].split("?")[0]).is_file():
                fallos.append(f"{pagina.name}: recurso local inexistente ({ref})")
        for etiqueta in re.findall(r"<a [^>]*target=\"_blank\"[^>]*>", texto):
            if "noopener" not in etiqueta:
                fallos.append(f"{pagina.name}: target=_blank sin rel=noopener ({etiqueta[:70]})")
    return total


def registro():
    entradas = re.split(r"^## ", (RAIZ / "CHANGELOG.md").read_text(encoding="utf-8"), flags=re.M)[1:]
    for e in entradas:
        if "- Agente:" not in e:
            fallos.append(f"CHANGELOG: entrada sin «Agente:» ({e.splitlines()[0]})")
    fechas = [e[:10] for e in entradas]
    if fechas != sorted(fechas, reverse=True):
        fallos.append("CHANGELOG: las entradas no están de la más reciente a la más antigua")
    return len(entradas)


def secretos():
    patron = re.compile(
        r"(sk|rk|pk)_(live|test)_[A-Za-z0-9]{8,}|whsec_[A-Za-z0-9]{8,}|AKIA[0-9A-Z]{16}"
        r"|gh[pousr]_[A-Za-z0-9]{30,}|-----BEGIN [A-Z ]*PRIVATE KEY-----|eyJ[A-Za-z0-9_-]{30,}\."
    )
    total = 0
    for f in RAIZ.rglob("*"):
        if not f.is_file() or ".git" in f.relative_to(RAIZ).parts:
            continue
        if f.suffix.lower() in {".webp", ".png", ".jpg", ".ico"}:
            continue
        total += 1
        if patron.search(f.read_text(encoding="utf-8", errors="ignore")):
            fallos.append(f"secretos: patrón sospechoso en {f.relative_to(RAIZ)}")
    return total


if __name__ == "__main__":
    print(f"manifiesto: {hashes()} archivos comprobados")
    print(f"enlaces locales: {enlaces()} comprobados")
    print(f"registro: {registro()} entradas")
    print(f"secretos: {secretos()} archivos revisados")
    for f in fallos:
        print("FALLO ·", f)
    print("RESULTADO:", "falló" if fallos else "aprobado")
    sys.exit(1 if fallos else 0)
