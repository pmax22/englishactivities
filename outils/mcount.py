import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
import json, re
from playwright.sync_api import sync_playwright
cat = json.loads(re.search(r"=\s*(\[.*\]);", open(_EA_REPO+"/assets/catalog.js").read(), re.S).group(1))
out = {}
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page()
    for c in cat:
        pg.goto("http://localhost:8765/" + c["f"]); pg.wait_for_timeout(80)
        out[c["f"]] = pg.evaluate("typeof MISSIONS!=='undefined' ? MISSIONS.length : document.querySelectorAll('.mission').length")
    b.close()
json.dump(out, open(_EA_OUT+"/mcount.json", "w"), indent=0)
print(len(out), sorted(set(out.values())), [k for k, v in out.items() if not v])
