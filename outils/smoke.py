import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
import glob, os, re
from playwright.sync_api import sync_playwright
os.chdir(_EA_REPO)
files = sorted(glob.glob("*.html")); bad = []
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(); errs = []
    pg.on("pageerror", lambda e: errs.append(str(e)))
    for f in files:
        errs.clear(); pg.goto("http://localhost:8765/" + f); pg.wait_for_timeout(150)
        ok = pg.evaluate("!!window.EA")
        if errs or not ok: bad.append((f, ok, errs[:2]))
    hrefs = set(re.findall(r'href="([\w_]+\.html)', open("index.html").read()))
    miss = [h for h in hrefs if not os.path.exists(h)]
    print(len(files), "pages; bad:", bad, "missing links:", miss)
    b.close()

# garde-fou : une option de quiz ne doit jamais être un nom de fichier
import re as _re2, glob as _g2
_bad = [f for f in _g2.glob(_EA_REPO+"/*.html") if _re2.search(r'\["[a-z0-9_]+\.html", "(True|False)"\]|\["(True|False)", "[a-z0-9_]+\.html"\]', open(f, encoding="utf-8").read())]
print("options cassées :", _bad)
