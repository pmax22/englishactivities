import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
import re, sys
from playwright.sync_api import sync_playwright
files = sys.argv[1:]
with sync_playwright() as p:
    b = p.chromium.launch()
    for f in files:
        pg = b.new_page(viewport={"width": 900, "height": 1000}); errs = []
        pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.goto(f"file://{_EA_REPO}/{f}"); pg.wait_for_timeout(300)
        n = pg.locator(".mission").count(); res = []
        for i in range(n):
            for rep in range(int(__import__("os").environ.get("REPS","3"))):  # plusieurs tirages pour couvrir les données
                pg.locator(".mission").nth(i).click()
                steps = 0
                while pg.locator("#quiz:not(.hidden)").count() and steps < 40:
                    steps += 1
                    q = pg.evaluate("questions[qi]")
                    if q["kind"] == "mcq":
                        pg.locator(f'.btn-choice[data-i="{q["correct"]}"]').click()
                    elif q["kind"] == "match":
                        for k in range(len(q["pairs"])):
                            pg.locator(f'.mbtn[data-s="0"][data-k="{k}"]').click(); pg.locator(f'.mbtn[data-s="1"][data-k="{k}"]').click()
                    elif q["kind"] == "order":
                        for t in q["tiles"]:
                            pg.locator("#pool .tile:not(.used)", has_text=re.compile("^" + re.escape(t) + "$")).first.click()
                        pg.click("#btnMain")
                    else:
                        blanks = [x for x in q["parts"] if not isinstance(x, str)]
                        ins = pg.locator(".gapin")
                        for k in range(ins.count()): ins.nth(k).fill(blanks[k]["answers"][0])
                        pg.click("#btnMain")
                    if "ko" in (pg.inner_html("#qFeedback") or "") and "feedback ko" in pg.inner_html("#qFeedback"):
                        res.append(f"FAIL m{i+1}: {q.get('label')} -> {pg.inner_text('#qFeedback')[:120]}")
                    pg.click("#btnMain")
                res.append(f"m{i+1} {pg.inner_text('#sScore').replace(chr(10), '')}") if rep == 0 else None
                pg.click("text=Retour aux missions")
        print(f, n, "missions |", " ".join(r for r in res if not r.startswith("FAIL")))
        for r in [r for r in res if r.startswith("FAIL")][:10]: print("  ", r)
        print("   errors:", errs)
        pg.screenshot(path=f"{_EA_OUT}/_captures/{f}.png", full_page=True)
    b.close()
