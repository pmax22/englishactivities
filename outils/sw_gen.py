import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
import glob, os, hashlib, json
R = _EA_REPO; os.chdir(R)
files = sorted(glob.glob("*.html")) + ["manifest.json"] + sorted(glob.glob("assets/*"))
h = hashlib.sha1(b"".join(open(f, "rb").read() for f in files)).hexdigest()[:10]
sw = f'''/* English Activities — fonctionnement hors connexion (généré automatiquement) */
const CACHE = "ea-{h}";
const FILES = {json.dumps(["./"] + files)};
self.addEventListener("install", e => {{
  e.waitUntil(caches.open(CACHE).then(c => Promise.all(FILES.map(f => c.add(f).catch(() => null)))).then(() => self.skipWaiting()));
}});
self.addEventListener("activate", e => {{
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k.startsWith("ea-") && k !== CACHE && k !== "ea-fonts").map(k => caches.delete(k)))).then(() => self.clients.claim()));
}});
self.addEventListener("fetch", e => {{
  const req = e.request; if (req.method !== "GET") return;
  const url = new URL(req.url);
  if (url.origin === location.origin) {{
    /* réseau d'abord (contenu à jour), cache si hors connexion */
    e.respondWith(fetch(req).then(r => {{ if (r.ok) {{ const c = r.clone(); caches.open(CACHE).then(k => k.put(req, c)); }} return r; }})
      .catch(() => caches.match(req, {{ ignoreSearch: true }}).then(r => r || caches.match("index.html"))));
  }} else if (/fonts\\.(googleapis|gstatic)\\.com$/.test(url.hostname)) {{
    e.respondWith(caches.open("ea-fonts").then(c => c.match(req).then(r => r || fetch(req).then(n => {{ c.put(req, n.clone()); return n; }}))));
  }}
}});
'''
open("sw.js", "w").write(sw); print(len(files), h)
