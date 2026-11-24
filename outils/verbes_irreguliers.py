"""Génère verbes_irreguliers.html : la liste des verbes irréguliers avec une recherche.
Si l'élève cherche un verbe absent de la liste, la page lui dit qu'il est régulier
et lui montre son prétérit en -ed."""
import os, json, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen import BASE_CSS, EXTRA_CSS, hex2rgb

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# base verbale, prétérit, participe passé, traduction
V = [
 ("be", "was / were", "been", "être"),
 ("beat", "beat", "beaten", "battre"),
 ("become", "became", "become", "devenir"),
 ("begin", "began", "begun", "commencer"),
 ("bite", "bit", "bitten", "mordre"),
 ("blow", "blew", "blown", "souffler"),
 ("break", "broke", "broken", "casser"),
 ("bring", "brought", "brought", "apporter"),
 ("build", "built", "built", "construire"),
 ("burn", "burnt / burned", "burnt / burned", "brûler"),
 ("buy", "bought", "bought", "acheter"),
 ("catch", "caught", "caught", "attraper"),
 ("choose", "chose", "chosen", "choisir"),
 ("come", "came", "come", "venir"),
 ("cost", "cost", "cost", "coûter"),
 ("cut", "cut", "cut", "couper"),
 ("dig", "dug", "dug", "creuser"),
 ("do", "did", "done", "faire"),
 ("draw", "drew", "drawn", "dessiner"),
 ("dream", "dreamt / dreamed", "dreamt / dreamed", "rêver"),
 ("drink", "drank", "drunk", "boire"),
 ("drive", "drove", "driven", "conduire"),
 ("eat", "ate", "eaten", "manger"),
 ("fall", "fell", "fallen", "tomber"),
 ("feed", "fed", "fed", "nourrir"),
 ("feel", "felt", "felt", "ressentir, se sentir"),
 ("fight", "fought", "fought", "se battre"),
 ("find", "found", "found", "trouver"),
 ("fly", "flew", "flown", "voler (dans les airs)"),
 ("forbid", "forbade", "forbidden", "interdire"),
 ("forget", "forgot", "forgotten", "oublier"),
 ("forgive", "forgave", "forgiven", "pardonner"),
 ("freeze", "froze", "frozen", "geler"),
 ("get", "got", "got / gotten", "obtenir, devenir"),
 ("give", "gave", "given", "donner"),
 ("go", "went", "gone", "aller"),
 ("grow", "grew", "grown", "grandir, cultiver"),
 ("hang", "hung", "hung", "accrocher, suspendre"),
 ("have", "had", "had", "avoir"),
 ("hear", "heard", "heard", "entendre"),
 ("hide", "hid", "hidden", "cacher, se cacher"),
 ("hit", "hit", "hit", "frapper"),
 ("hold", "held", "held", "tenir"),
 ("hurt", "hurt", "hurt", "blesser, faire mal"),
 ("keep", "kept", "kept", "garder"),
 ("know", "knew", "known", "savoir, connaître"),
 ("lead", "led", "led", "mener, diriger"),
 ("learn", "learnt / learned", "learnt / learned", "apprendre"),
 ("leave", "left", "left", "partir, quitter, laisser"),
 ("lend", "lent", "lent", "prêter"),
 ("let", "let", "let", "laisser, permettre"),
 ("light", "lit", "lit", "allumer"),
 ("lose", "lost", "lost", "perdre"),
 ("make", "made", "made", "faire, fabriquer"),
 ("mean", "meant", "meant", "signifier, vouloir dire"),
 ("meet", "met", "met", "rencontrer"),
 ("pay", "paid", "paid", "payer"),
 ("put", "put", "put", "mettre, poser"),
 ("quit", "quit", "quit", "quitter, arrêter"),
 ("read", "read", "read", "lire"),
 ("ride", "rode", "ridden", "aller à vélo, à cheval"),
 ("ring", "rang", "rung", "sonner"),
 ("rise", "rose", "risen", "se lever, monter"),
 ("run", "ran", "run", "courir"),
 ("say", "said", "said", "dire"),
 ("see", "saw", "seen", "voir"),
 ("sell", "sold", "sold", "vendre"),
 ("send", "sent", "sent", "envoyer"),
 ("set", "set", "set", "fixer, régler"),
 ("shake", "shook", "shaken", "secouer"),
 ("shine", "shone", "shone", "briller"),
 ("shoot", "shot", "shot", "tirer"),
 ("show", "showed", "shown", "montrer"),
 ("shut", "shut", "shut", "fermer"),
 ("sing", "sang", "sung", "chanter"),
 ("sink", "sank", "sunk", "couler"),
 ("sit", "sat", "sat", "s'asseoir"),
 ("sleep", "slept", "slept", "dormir"),
 ("smell", "smelt / smelled", "smelt / smelled", "sentir (une odeur)"),
 ("speak", "spoke", "spoken", "parler"),
 ("spell", "spelt / spelled", "spelt / spelled", "épeler"),
 ("spend", "spent", "spent", "dépenser, passer (du temps)"),
 ("stand", "stood", "stood", "être debout"),
 ("steal", "stole", "stolen", "voler (dérober)"),
 ("stick", "stuck", "stuck", "coller"),
 ("sting", "stung", "stung", "piquer"),
 ("swim", "swam", "swum", "nager"),
 ("take", "took", "taken", "prendre"),
 ("teach", "taught", "taught", "enseigner"),
 ("tear", "tore", "torn", "déchirer"),
 ("tell", "told", "told", "dire, raconter"),
 ("think", "thought", "thought", "penser"),
 ("throw", "threw", "thrown", "lancer, jeter"),
 ("understand", "understood", "understood", "comprendre"),
 ("wake", "woke", "woken", "réveiller, se réveiller"),
 ("wear", "wore", "worn", "porter (un vêtement)"),
 ("win", "won", "won", "gagner"),
 ("write", "wrote", "written", "écrire"),
]
assert len({v[0] for v in V}) == len(V)

A, B = "#4ec9f5", "#3f7ee0"
css = BASE_CSS.replace("--accent: #ff9f43;", f"--accent: {A};\n    --accent-rgb: {hex2rgb(A)};").replace("--accent2: #e8603c;", f"--accent2: {B};")
css = css.replace("255,159,67", hex2rgb(A)).replace("232,96,60", hex2rgb(B))
PAGE_CSS = """
  .vi-search { position: sticky; top: 0; z-index: 5; background: var(--bg); padding: 10px 0 12px; }
  .vi-search input { width: 100%; font: inherit; font-size: 17px; padding: 12px 16px; border-radius: 12px; border: 1.5px solid var(--border); background: var(--surface); color: var(--text); outline: none; }
  .vi-search input:focus { border-color: var(--accent); }
  .vi-help { color: var(--muted); font-size: 13px; margin-top: 6px; }
  .vi-msg { margin: 4px 0 14px; padding: 12px 14px; border-radius: 12px; font-size: 15px; line-height: 1.5; }
  .vi-msg.reg { background: rgba(78,203,127,.1); border: 1px solid rgba(78,203,127,.4); }
  .vi-msg.none { background: var(--surface); border: 1px solid var(--border); color: var(--muted); }
  .vi-msg b.hl { color: var(--green); }
  table.vi { width: 100%; border-collapse: collapse; font-size: 15px; }
  table.vi th { text-align: left; font-size: 12px; color: var(--muted); font-weight: 600; padding: 8px 8px; border-bottom: 1px solid var(--border); }
  table.vi td { padding: 9px 8px; border-bottom: 1px solid var(--border); vertical-align: top; }
  table.vi td.bv { font-weight: 700; color: var(--text); font-size: 15px; }
  table.vi td.pt { color: var(--accent); font-weight: 600; }
  table.vi td.fr { color: var(--muted); font-size: 14px; }
  table.vi tr.hit td { background: rgba(var(--accent-rgb),.08); }
  .vi-say { background: none; border: 1px solid var(--border); color: var(--muted); border-radius: 8px; padding: 2px 7px; cursor: pointer; font-size: 13px; margin-left: 4px; }
  .vi-say:hover { color: var(--text); }
  .vi-count { color: var(--muted); font-size: 13px; margin: 2px 0 8px; }
  @media (max-width: 520px) { table.vi { font-size: 14px; } table.vi th, table.vi td { padding: 8px 5px; } table.vi td.fr { font-size: 13px; } }
"""

JS = r"""
const V = %s;
const norm = s => s.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/^to\s+/, "").trim();
const esc = s => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
function forms(v) { return [v[0], ...v[1].split(" / "), ...v[2].split(" / ")].map(norm); }
function edForm(w) {
  if (/e$/.test(w)) return w + "d";
  if (/[^aeiou]y$/.test(w)) return w.slice(0, -1) + "ied";
  const syl = (w.match(/[aeiouy]+/g) || []).length;
  if (syl === 1 && /[^aeiou][aeiou][bcdfgklmnprstvz]$/.test(w)) return w + w.slice(-1) + "ed";
  return w + "ed";
}
const tbody = document.getElementById("vbody"), msg = document.getElementById("vmsg"), cnt = document.getElementById("vcount");
tbody.innerHTML = V.map((v, i) => `<tr data-i="${i}"><td class="bv">${esc(v[0])}</td><td class="pt">${esc(v[1])}</td><td>${esc(v[2])}<button class="vi-say" type="button" title="Écouter" aria-label="Écouter ${esc(v[0])}">▶</button></td><td class="fr">${esc(v[3])}</td></tr>`).join("");
tbody.querySelectorAll(".vi-say").forEach(b => b.onclick = () => {
  const v = V[+b.closest("tr").dataset.i];
  if (!("speechSynthesis" in window)) return;
  speechSynthesis.cancel();
  const u = new SpeechSynthesisUtterance([v[0], v[1], v[2]].join(", ").replace(/ \/ /g, " or "));
  u.lang = "en-GB"; u.rate = .85; speechSynthesis.speak(u);
});
function run() {
  const q = norm(document.getElementById("vq").value);
  let shown = 0, exact = false;
  tbody.querySelectorAll("tr").forEach(tr => {
    const v = V[+tr.dataset.i], f = forms(v), fr = norm(v[3]);
    const ok = !q || f.some(x => x.startsWith(q)) || fr.split(/[,()]\s*|\s+/).some(x => x.startsWith(q));
    const hit = q && f.includes(q);
    if (hit) exact = true;
    tr.hidden = !ok; tr.classList.toggle("hit", !!hit); if (ok) shown++;
  });
  cnt.textContent = q ? `${shown} verbe${shown > 1 ? "s" : ""} trouvé${shown > 1 ? "s" : ""}` : `${V.length} verbes irréguliers`;
  document.querySelector("table.vi thead").hidden = !shown;
  msg.hidden = true;
  if (!q || exact) return;
  if (/^[a-z]{2,}$/.test(q) && !shown) {
    msg.className = "vi-msg reg"; msg.hidden = false;
    msg.innerHTML = `<b>${esc(q)}</b> n'est pas dans la liste des verbes irréguliers. Si c'est bien un verbe anglais, il est <b>régulier</b> : on ajoute <b>-ed</b> → <b class="hl">${esc(edForm(q))}</b> (prétérit et participe passé).`;
  } else if (!shown) {
    msg.className = "vi-msg none"; msg.hidden = false;
    msg.textContent = "Aucun verbe trouvé. Vérifie l'orthographe, ou cherche la base verbale en anglais (ex. : go, buy, take).";
  }
}
document.getElementById("vq").addEventListener("input", run);
const p = new URLSearchParams(location.search).get("q"); if (p) document.getElementById("vq").value = p;
run();
""" % json.dumps(V, ensure_ascii=False)

html = f'''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Les verbes irréguliers</title>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;0,700;1,300&display=swap" rel="stylesheet">
<style>{css}{EXTRA_CSS}{PAGE_CSS}</style>
<link rel="manifest" href="manifest.json">
<meta name="theme-color" content="#0f1117">
<script src="assets/ea.js"></script>
</head>
<body>

<nav class="topnav"><a class="back" href="index.html">← Toutes les activités</a></nav>

<header>
  <div class="tag">Grammaire · Prétérit</div>
  <h1>Les verbes <span>irréguliers</span></h1>
  <p class="subtitle">Base verbale · prétérit · participe passé · traduction</p>
</header>

<main class="wrap" id="menu">
  <div class="vi-search">
    <input id="vq" type="search" placeholder="Cherche un verbe : go, went, aller…" autocomplete="off" autocapitalize="off" spellcheck="false" aria-label="Chercher un verbe">
    <div class="vi-help">Tu peux chercher la base verbale, le prétérit, le participe passé ou le mot en français.</div>
  </div>
  <div id="vmsg" class="vi-msg" hidden></div>
  <div class="vi-count" id="vcount"></div>
  <table class="vi">
    <thead><tr><th>Base verbale</th><th>Prétérit</th><th>Participe passé</th><th>Français</th></tr></thead>
    <tbody id="vbody"></tbody>
  </table>
  <p class="vi-help" style="margin-top:14px">Le prétérit sert à raconter une action terminée : <b>I went</b> to London. Le participe passé sert avec <b>have</b> : I have <b>been</b> to London.</p>
  <p class="vi-help">Pour t'entraîner : <a href="verbe_regulier_irregulier.html">Régulier ou irrégulier ?</a> · <a href="preterit.html">Le prétérit</a></p>
</main>

<script>{JS}</script>
</body>
</html>
'''
open(f"{REPO}/verbes_irreguliers.html", "w", encoding="utf-8").write(html)
print("verbes_irreguliers.html :", len(V), "verbes")
