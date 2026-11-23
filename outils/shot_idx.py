import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch()
    for w, h, n in ((420, 900, "m"), (1280, 900, "d")):
        pg = b.new_page(viewport={"width": w, "height": h}); pg.goto("http://localhost:8765/index.html"); pg.evaluate("localStorage.clear()"); pg.reload(); pg.wait_for_timeout(1500)
        pg.screenshot(path=f"{_EA_OUT}/_captures/i_{n}_all.png")
        pg.click('.tab[data-fam="Linguistique"]'); pg.wait_for_timeout(500); pg.screenshot(path=f"{_EA_OUT}/_captures/i_{n}_ling.png")
        pg.click('.tab[data-fam="Culturelle"]'); pg.wait_for_timeout(900); pg.screenshot(path=f"{_EA_OUT}/_captures/i_{n}_cult.png", full_page=(n=="d"))
        pg.click('.tab[data-fam="Tout"]'); pg.wait_for_timeout(300); print(n, pg.locator(".fam-head:not(.hidden)").count())
    b.close()
