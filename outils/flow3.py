import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
from playwright.sync_api import sync_playwright
B = "http://localhost:8765/"
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 420, "height": 900}); errs = []
    pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.goto(B + "index.html")
    pg.evaluate("""localStorage.setItem('ea_progress_v1', JSON.stringify({errors:[], pages:{
      'be_have_play.html':{title:'x',date:Date.now(),missions:{a:{best:10,total:10},b:{best:8,total:8},c:{best:5,total:5},d:{best:8,total:8},e:{best:6,total:6}}},
      'present_simple.html':{title:'x',date:Date.now(),missions:{a:{best:7,total:10}}}}}))""")
    pg.reload(); pg.wait_for_timeout(1500)
    print([(c.get_attribute("href"), c.locator(".card-visual").get_attribute("data-pct"), c.get_attribute("title")) for c in pg.locator(".card.done").all()])
    pg.screenshot(path=_EA_OUT+"/_captures/h_index.png", clip={"x":0,"y":450,"width":420,"height":700})
    pg.goto(B + "progres.html"); pg.wait_for_timeout(600); print(pg.inner_text(".dash-list"))
    print("ERRS", errs); b.close()
