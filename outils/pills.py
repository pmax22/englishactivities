import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch()
    for w in (1400, 1200, 1000, 900, 800, 700, 650, 600, 500, 400, 360):
        pg=b.new_page(viewport={"width":w,"height":1000})
        pg.goto("file://"+_EA_REPO+"/index.html"); pg.wait_for_timeout(2500)
        print(w, pg.evaluate('''[...document.querySelectorAll(".card.t")].filter(c=>c.querySelector(".card-pills").getBoundingClientRect().height>32).map(c=>c.querySelector(".card-title").textContent)'''))
