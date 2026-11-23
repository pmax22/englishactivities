import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
import sys
from playwright.sync_api import sync_playwright
f=sys.argv[1]; ms=[int(x) for x in sys.argv[2].split(",")]
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":860,"height":720})
    pg.goto(f"file://{_EA_REPO}/{f}"); pg.wait_for_timeout(900)
    pg.screenshot(path=f"{_EA_OUT}/_captures/{f}-menu.png", full_page=True)
    for m in ms:
        pg.locator(".mission").nth(m).click(); pg.wait_for_timeout(700)
        pg.screenshot(path=f"{_EA_OUT}/_captures/{f}-m{m+1}.png"); pg.click("text=Menu >> nth=0")
