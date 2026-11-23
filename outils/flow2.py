import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
from playwright.sync_api import sync_playwright
import random
B = "http://localhost:8765/"
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 420, "height": 900}); errs = []
    pg.on("pageerror", lambda e: errs.append(str(e)))
    for mode in ("strong", "weak"):
        pg.goto(B + "test_niveau.html"); pg.wait_for_timeout(300); pg.locator(".mission").nth(0).click(); n = 0
        while pg.locator("#quiz:not(.hidden)").count() and n < 100:
            q = pg.evaluate("questions[qi]"); n += 1
            good = (random.random() < (0.85 if q["lvl"] < 2 else 0.6)) if mode == "strong" else (q["lvl"] == 0 and random.random() < 0.5)
            pg.locator(f'.btn-choice[data-i="{q["correct"]}"]' if good else f'.btn-choice:not([data-i="{q["correct"]}"])').first.click(); pg.click("#btnMain")
        print(mode, n, "questions", pg.inner_text("#sScore"))
        pg.wait_for_timeout(800); pg.screenshot(path=f"{_EA_OUT}/_captures/g_{mode}.png", full_page=True)
    pg.click("#dgCopy"); print(pg.inner_text("#dgOut"))
    pg.goto(B + "progres.html"); pg.wait_for_timeout(800); pg.screenshot(path=_EA_OUT+"/_captures/g_prog.png", full_page=True)
    print("ERRS", errs); b.close()
