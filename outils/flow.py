import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
from playwright.sync_api import sync_playwright
B = "http://localhost:8765/"
with sync_playwright() as p:
    b = p.chromium.launch(); ctx = b.new_context(viewport={"width": 420, "height": 900}); pg = ctx.new_page(); errs = []
    pg.on("pageerror", lambda e: errs.append(str(e)))
    # 1. activité avec erreurs
    pg.goto(B + "present_simple.html"); pg.wait_for_timeout(300)
    pg.locator(".mission").nth(0).click()
    for k in range(40):
        if not pg.locator("#quiz:not(.hidden)").count(): break
        q = pg.evaluate("questions[qi]")
        if k % 2 == 0:  # erreur volontaire
            if q["kind"] == "mcq": pg.locator(f'.btn-choice:not([data-i="{q["correct"]}"])').first.click()
            elif q["kind"] == "gap":
                ins = pg.locator(".gapin");  [ins.nth(i).fill("zzz") for i in range(ins.count())]; pg.click("#btnMain")
            else: pg.click("#btnMain")
        else:
            if q["kind"] == "mcq": pg.locator(f'.btn-choice[data-i="{q["correct"]}"]').click()
            elif q["kind"] == "gap":
                bl = [x for x in q["parts"] if not isinstance(x, str)]; ins = pg.locator(".gapin")
                [ins.nth(i).fill(bl[i]["answers"][0]) for i in range(ins.count())]; pg.click("#btnMain")
            else: pg.click("#btnMain")
        pg.click("#btnMain")
    pg.fill("#eaName", "Léa 2nde B"); pg.press("#eaName", "Tab"); pg.wait_for_timeout(200)
    line = pg.inner_text("#eaText"); print("LINE:", line)
    pg.screenshot(path=_EA_OUT+"/_captures/f1_score.png", full_page=True)
    print("errors stored:", pg.evaluate("EA.data().errors.length"))
    # 2. progrès
    pg.goto(B + "progres.html"); pg.wait_for_timeout(400); pg.screenshot(path=_EA_OUT+"/_captures/f2_progres.png", full_page=True)
    pg.locator(".mission").nth(0).click()
    for k in range(40):
        if not pg.locator("#quiz:not(.hidden)").count(): break
        q = pg.evaluate("questions[qi]")
        if q["kind"] == "mcq": pg.locator(f'.btn-choice[data-i="{q["correct"]}"]').click()
        elif q["kind"] == "gap":
            bl = [x for x in q["parts"] if not isinstance(x, str)]; ins = pg.locator(".gapin")
            [ins.nth(i).fill(bl[i]["answers"][0]) for i in range(ins.count())]; pg.click("#btnMain")
        else:
            import re
            for t in q["tiles"]: pg.locator("#pool .tile:not(.used)", has_text=re.compile("^" + re.escape(t) + "$")).first.click()
            pg.click("#btnMain")
        pg.click("#btnMain")
    print("after review errors:", pg.evaluate("EA.data().errors.length"), pg.inner_text("#sScore"))
    pg.click("#score .btn-ghost"); pg.wait_for_timeout(200)
    # 3. test niveau
    pg.goto(B + "test_niveau.html"); pg.wait_for_timeout(300); pg.locator(".mission").nth(0).click()
    for k in range(30):
        if not pg.locator("#quiz:not(.hidden)").count(): break
        q = pg.evaluate("questions[qi]")
        good = q["lvl"] <= 1
        pg.locator(f'.btn-choice[data-i="{q["correct"]}"]' if good else f'.btn-choice:not([data-i="{q["correct"]}"])').first.click(); pg.click("#btnMain")
    pg.screenshot(path=_EA_OUT+"/_captures/f3_niveau.png", full_page=True); print("level:", pg.evaluate("localStorage.getItem('ea_level')")[:40])
    # 4. index
    pg.goto(B + "index.html"); pg.wait_for_timeout(1200); pg.screenshot(path=_EA_OUT+"/_captures/f4_index.png")
    print("done cards:", pg.locator(".card.done").count(), "reco:", pg.inner_text("#reco"))
    pg.click("#reco button"); pg.wait_for_timeout(300); print("visible after reco:", pg.locator(".card.t:not(.hidden)").count())
    # 5. prof → devoir
    pg.goto(B + "prof.html"); pg.wait_for_timeout(400)
    pg.locator('.pf-row input[data-f="present_simple.html"]').check(); pg.locator('.pf-row input[data-f="meteo.html"]').check()
    link = pg.inner_text("#pLink"); print("LINK:", link)
    pg.fill("#pVer", line + "\n" + line.replace("Léa", "Léo")); pg.wait_for_timeout(200); print(pg.inner_text("#pVerOut"))
    pg.screenshot(path=_EA_OUT+"/_captures/f5_prof.png", full_page=True)
    pg.goto(link); pg.wait_for_timeout(400); pg.screenshot(path=_EA_OUT+"/_captures/f6_devoir.png", full_page=True)
    print("devoir:", pg.inner_text(".dash-stats"))
    # 6. écriture
    pg.goto(B + "ecriture_guidee.html"); pg.wait_for_timeout(300); pg.locator(".mission").nth(0).click(); pg.wait_for_timeout(200)
    t = pg.locator(".wr-in"); t.nth(0).click(); t.nth(0).type("Léa"); t.nth(1).click(); t.nth(1).type("fifteen years old.")
    pg.wait_for_timeout(200); pg.screenshot(path=_EA_OUT+"/_captures/f7_ecr.png", full_page=True)
    print([pg.locator(".wr-msg").nth(i).inner_text() for i in range(2)])
    pg.click("#btnMain"); pg.wait_for_timeout(200); pg.screenshot(path=_EA_OUT+"/_captures/f8_ecr_final.png", full_page=True)
    # 7. oral
    pg.goto(B + "expression_orale.html"); pg.wait_for_timeout(300); pg.locator(".mission").nth(0).click(); pg.wait_for_timeout(200)
    pg.screenshot(path=_EA_OUT+"/_captures/f9_oral.png", full_page=True)
    pg.locator(".mission").count()
    print("ERRS", errs)
    b.close()
