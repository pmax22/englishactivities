import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
import re, html as H
REPO = _EA_REPO
T_PRES, T_PAST, T_FUT, T_Q, T_VERB, T_GN, T_COMP, T_REP, T_COMPLEX, T_CAP = (
    "Présent", "Passé", "Futur & conditionnel", "Questions", "Verbes & modaux", "Groupe nominal",
    "Comparer & décrire", "Lieu, temps & nombres", "Phrase complexe", "CAP Sapver")
TAGS = [T_PRES, T_PAST, T_FUT, T_Q, T_VERB, T_GN, T_COMP, T_REP, T_COMPLEX, T_CAP]

# (fichier, couleurs, grand mot, badge, catégorie, titre, description, pastilles, tags, mots-clés)
A = [
  ("be_have_play.html", "#f87171", "#dc2626", "Be", "is · has · plays", "Grammaire · Conjugaison", "Be, Have & Play", "Conjuguer be, have et play au présent : formes affirmative, négative et interrogative.", ["am / is / are", "doesn't", "Does?"], [T_PRES, T_VERB], "être avoir jouer"),
  ("present_simple.html", "#38bdf8", "#0284c7", "Every day", "he works", "Grammaire · Temps", "Le présent simple", "Habitudes et vérités générales : le -s de la 3e personne, don't / doesn't, Do / Does.", ["-s / -es", "doesn't", "Does?"], [T_PRES], "present simple habitude"),
  ("present_continu.html", "#22d3ee", "#0891b2", "Now", "I am reading", "Grammaire · Temps", "Le présent be + -ing", "Ce qui se passe en ce moment : am / is / are + verbe-ing, et la différence avec le présent simple.", ["be + -ing", "now", "simple ou -ing ?"], [T_PRES], "present continu progressif ing"),
  ("adverbes_frequence.html", "#fb923c", "#ea580c", "Often", "always → never", "Grammaire · Adverbes", "Adverbes de fréquence", "always, usually, often, sometimes, rarely, never : sens, place dans la phrase et How often?", ["always", "sometimes", "never"], [T_PRES, T_COMP], "frequence how often"),
  ("preterit.html", "#f5c842", "#e07b3f", "Past", "Prétérit simple", "Grammaire · Temps", "Le Prétérit", "Phrases affirmatives, négatives et interrogatives au prétérit simple — réguliers et irréguliers.", ["Affirmatif", "Négatif", "Interrogatif"], [T_PAST], "preterit passe did"),
  ("verbe_regulier_irregulier.html", "#4ecb7f", "#2da866", "Reg?", "Identification", "Grammaire · Verbes", "Régulier ou Irrégulier ?", "Régulier ou irrégulier ? Base verbale, orthographe du -ED, formes irrégulières et intrus.", ["-ed / -ied", "Irréguliers", "Intrus"], [T_PAST, T_VERB], "verbes irreguliers preterit"),
  ("preterit_continu.html", "#facc15", "#ca8a04", "Was -ing", "I was sleeping", "Grammaire · Temps", "Le prétérit be + -ing", "Ce qui était en train de se passer : was / were + verbe-ing, avec when et while.", ["was / were", "when", "while"], [T_PAST], "preterit continu progressif"),
  ("used_to.html", "#7c6af7", "#b47cf0", "Used", "Habitudes passées", "Grammaire · Aspect", "Used To", "Exprimer des habitudes et états passés révolus — formes affirmative, négative et interrogative.", ["used to", "didn't use to", "Did … use to?"], [T_PAST], "habitude passee"),
  ("present_perfect.html", "#f472b6", "#db2777", "Have done", "for · since", "Grammaire · Temps", "Le present perfect", "have / has + participe passé, for / since, ever / never, et la différence avec le prétérit.", ["have done", "for / since", "ever"], [T_PAST], "present perfect participe"),
  ("questions_fermees.html", "#ff9f43", "#e8603c", "Did?", "Yes, I did / No, I didn't", "Grammaire · Questions", "Questions fermées", "Traduire des questions en Did + sujet + BV, puis compléter les réponses affirmatives et négatives.", ["Did + BV", "didn't + BV", "Prétérit"], [T_PAST, T_Q], "did you questions fermees"),
  ("questions_ouvertes.html", "#f06fa4", "#c44d8a", "Wh-?", "When · Where · Who · How", "Grammaire · Questions", "Questions ouvertes", "Pronoms interrogatifs, ordre des mots, traduction — et raconter ses dernières vacances.", ["Wh- + did", "How long", "Sum up"], [T_PAST, T_Q], "when where who what how vacances"),
  ("futur.html", "#a78bfa", "#7c3aed", "Will", "going to", "Grammaire · Temps", "Le futur", "will ou be going to ? Prédictions, promesses, décisions et projets.", ["will", "won't", "going to"], [T_FUT], "futur will going to"),
  ("conditionnel.html", "#fdba74", "#f97316", "If…", "will · would", "Grammaire · Phrase complexe", "Le conditionnel", "Type 1 : If + présent, will · Type 2 : If + prétérit, would.", ["Type 1", "Type 2", "If I were you"], [T_FUT, T_COMPLEX], "if conditionnel would"),
  ("modaux.html", "#818cf8", "#4f46e5", "Can", "must · should", "Grammaire · Modaux", "Les modaux", "can, must, mustn't, should, have to, don't have to : capacité, obligation, interdiction, conseil.", ["can", "must / mustn't", "should"], [T_VERB], "modaux obligation conseil"),
  ("imperatif.html", "#4ade80", "#16a34a", "Go!", "Don't · Let's", "Grammaire · Verbes", "L'impératif", "Donner un ordre ou un conseil : base verbale, Don't + BV, Let's + BV.", ["BV", "Don't", "Let's"], [T_VERB], "imperatif ordre consigne"),
  ("like_ing.html", "#f9a8d4", "#ec4899", "Like", "I love playing", "Grammaire · Verbes", "Exprimer ses goûts", "love, like, enjoy, don't mind, hate + verbe-ing.", ["love / like", "hate", "+ -ing"], [T_VERB, T_PRES], "gouts aimer detester ing"),
  ("passif.html", "#a5b4fc", "#6366f1", "Made", "is made · was built", "Grammaire · Phrase complexe", "Le passif", "be + participe passé, au présent et au prétérit, avec by.", ["be + participe", "by", "actif / passif"], [T_VERB, T_COMPLEX], "passif participe"),
  ("pronoms_personnels.html", "#60a5fa", "#2563eb", "I · me", "he → him", "Grammaire · Pronoms", "Pronoms personnels", "Pronoms sujets et compléments : I / me, he / him, they / them…", ["Sujet", "Complément", "Traduction"], [T_GN], "pronoms sujet complement"),
  ("possessifs.html", "#fb7185", "#e11d48", "Tom's", "my · his · mine", "Grammaire · Possession", "Les possessifs", "my, your, his, her… · le cas possessif 's · mine, yours, hers…", ["my / his / her", "'s", "mine"], [T_GN], "possessifs genitif"),
  ("articles.html", "#a3e635", "#65a30d", "a / an", "the · Ø", "Grammaire · Articles", "Les articles", "a, an, the ou pas d'article ? Son voyelle, chose précise, généralités, sports, langues…", ["a / an", "the", "Ø"], [T_GN], "articles a an the"),
  ("there_is.html", "#fbbf24", "#d97706", "There", "is · are", "Grammaire · Groupe nominal", "There is / There are", "Il y a… : is ou are, some ou any, questions et négations.", ["is / are", "some / any", "Is there?"], [T_GN, T_REP], "il y a some any"),
  ("denombrables.html", "#c4b5fd", "#8b5cf6", "Much?", "many · a lot of", "Grammaire · Quantités", "much, many, a lot of", "Dénombrables et indénombrables : much / many, How much / How many, a few / a little.", ["much / many", "How much?", "a few"], [T_GN], "denombrable quantite"),
  ("adjectifs.html", "#e879f9", "#c026d3", "Adj.", "a nice sister", "Grammaire · Adjectifs", "Les adjectifs", "Niveau 1 : la place de l'adjectif · Niveau 2 : l'ordre des adjectifs (opinion, taille, âge…).", ["Place", "Invariable", "Ordre"], [T_GN, T_COMP], "adjectifs ordre"),
  ("comparatif.html", "#3ecfcf", "#2fa8d8", "Comp", "Comparatif", "Grammaire · Comparaison", "Le Comparatif", "Comparer des personnes, objets ou situations — formes supérieure, inférieure et égale.", ["-er / more", "less", "as … as"], [T_COMP], "comparatif than"),
  ("superlatif.html", "#2dd4bf", "#0d9488", "Best", "the tallest", "Grammaire · Comparaison", "Le superlatif", "the -est, the most…, the best / the worst — et la différence avec le comparatif.", ["the -est", "the most", "best / worst"], [T_COMP], "superlatif most est"),
  ("prepositions.html", "#34d399", "#059669", "in · on · at", "temps et lieu", "Grammaire · Prépositions", "in, on, at", "Les prépositions de temps (at 7, on Monday, in July) et de lieu (at school, on the table, in Paris).", ["Temps", "Lieu", "in / on / at"], [T_REP], "prepositions"),
  ("heure_dates.html", "#93c5fd", "#3b82f6", "7:30", "half past seven", "Vocabulaire · Repères", "Heure, dates et nombres", "Dire l'heure, les dates (the third of May), les nombres et les prix.", ["L'heure", "Les dates", "Les prix"], [T_REP], "heure date nombre ordinal prix"),
  ("relatifs.html", "#67e8f9", "#06b6d4", "Who?", "which · where", "Grammaire · Phrase complexe", "Les pronoms relatifs", "who, which, that, where, whose : relier deux phrases.", ["who", "which", "where"], [T_COMPLEX], "relatifs qui que ou"),
  ("discours_indirect.html", "#d8b4fe", "#a855f7", "He said", "said · told", "Grammaire · Phrase complexe", "Le discours indirect", "Rapporter des paroles : say ou tell, et la concordance des temps.", ["say / tell", "was / would", "pronoms"], [T_COMPLEX], "discours indirect rapporte"),
  ("preterit_cap_sapver.html", "#4ec9f5", "#3f7ee0", "Past", "Prétérit simple", "CAP Sapver · Temps", "Prétérit — Vente & Aide", "Prétérit simple orienté vente et aide à la personne — verbes métiers, vocabulaire professionnel.", ["Affirmatif", "Négatif", "Interrogatif"], [T_PAST, T_CAP], "cap sapver vente preterit"),
  ("cap_vente.html", "#5eead4", "#14b8a6", "Shop", "Can I help you?", "CAP Sapver · Vente", "L'anglais de la vente", "Accueillir, conseiller, encaisser, téléphoner : les phrases utiles au magasin.", ["Accueil", "Caisse", "Téléphone"], [T_CAP], "cap sapver vente client magasin"),
]

def rgb(h): h = h.lstrip("#"); return ",".join(str(int(h[i:i+2], 16)) for i in (0, 2, 4))
def strip_acc(s):
    import unicodedata
    return "".join(c for c in unicodedata.normalize("NFD", s.lower()) if unicodedata.category(c) != "Mn")

cards = []
for i, (href, a, b, big, badge, cat, title, desc, pills, tags, kw) in enumerate(A):
    search = strip_acc(" ".join([title, desc, cat, badge, " ".join(pills), " ".join(tags), kw]))
    pills_html = "\n".join(f'        <span class="pill">{H.escape(p)}</span>' for p in pills)
    cards.append(f'''  <a class="card t" href="{href}" data-tags="{H.escape('|'.join(tags))}" data-search="{H.escape(search)}" style="--ca:{a};--cb:{b};--crgb:{rgb(a)};animation-delay:{min(0.35 + 0.04 * i, 1.2):.2f}s">
    <div class="card-bar"></div>
    <div class="card-visual">
      <span class="big-label"{' style="font-size:' + ('34px' if len(big) > 9 else '42px') + '"' if len(big) > 6 else ''}>{H.escape(big)}</span>
      <span class="badge">{H.escape(badge)}</span>
    </div>
    <div class="card-body">
      <div class="card-category">{H.escape(cat)}</div>
      <div class="card-title">{H.escape(title)}</div>
      <div class="card-desc">{H.escape(desc)}</div>
    </div>
    <div class="card-footer">
      <div class="card-pills">
{pills_html}
      </div>
      <span class="card-arrow">↗</span>
    </div>
  </a>''')

CSS = '''
  /* ── Cartes génériques (couleurs en variables) ── */
  .card.t .card-bar { background: linear-gradient(90deg, var(--ca), var(--cb)); }
  .card.t .card-visual { background: radial-gradient(ellipse at 50% 80%, rgba(var(--crgb),0.08) 0%, transparent 70%); }
  .card.t .big-label { color: var(--ca); }
  .card.t .badge { color: var(--ca); border-color: rgba(var(--crgb),0.3); background: rgba(var(--crgb),0.08); }
  .card.t .card-category { color: var(--ca); }
  .card.t:hover { border-color: rgba(var(--crgb),0.35); }
  .card.hidden { display: none; }
  .card-visual .big-label { white-space: nowrap; text-align: center; }

  /* ── Recherche et filtres ── */
  .toolbar { max-width: 1100px; margin: 0 auto 22px; padding: 0 32px; animation: fadeUp 0.6s 0.35s ease both; opacity: 0; }
  .search {
    width: 100%; padding: 13px 18px 13px 44px; font-size: 15px; font-family: inherit; color: var(--text);
    background: var(--surface) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='18' height='18' fill='none' stroke='%238a8ea3' stroke-width='2' viewBox='0 0 24 24'%3E%3Ccircle cx='11' cy='11' r='7'/%3E%3Cpath d='m20 20-3.5-3.5'/%3E%3C/svg%3E") no-repeat 16px center;
    border: 1px solid var(--border); border-radius: 999px; outline: none; transition: border-color .2s;
  }
  .search:focus { border-color: #8a8ea3; }
  .chips { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 14px; }
  .chip {
    font-family: inherit; font-size: 13px; padding: 7px 14px; border-radius: 999px; cursor: pointer;
    background: var(--surface); color: var(--muted); border: 1px solid var(--border); transition: all .2s;
  }
  .chip:hover { color: var(--text); border-color: #8a8ea3; }
  .chip.active { background: var(--text); color: var(--bg); border-color: var(--text); font-weight: 500; }
  .chip .n { opacity: .6; margin-left: 4px; font-size: 11px; }
  .empty { grid-column: 1 / -1; text-align: center; color: var(--muted); padding: 40px 0; font-size: 15px; }
  @media (max-width: 600px) { .toolbar { padding: 0 16px; } }
'''

JS = '''
<script>
(function () {
  const KEY = "ea_index_filter";
  const cards = [...document.querySelectorAll(".card.t")];
  const chipsBox = document.getElementById("chips"), search = document.getElementById("search"), empty = document.getElementById("empty");
  const TAGS = %TAGS%;
  let state = { tag: "Tout", q: "" };
  try { state = Object.assign(state, JSON.parse(localStorage.getItem(KEY) || "{}")); } catch (e) {}
  if (state.tag !== "Tout" && !TAGS.includes(state.tag)) state.tag = "Tout";
  const norm = s => s.toLowerCase().normalize("NFD").replace(/[\\u0300-\\u036f]/g, "");
  const count = t => t === "Tout" ? cards.length : cards.filter(c => c.dataset.tags.split("|").includes(t)).length;
  ["Tout"].concat(TAGS).forEach(t => {
    const b = document.createElement("button"); b.className = "chip"; b.dataset.tag = t;
    b.innerHTML = `${t}<span class="n">${count(t)}</span>`;
    b.onclick = () => { state.tag = t; apply(); };
    chipsBox.appendChild(b);
  });
  search.value = state.q;
  search.addEventListener("input", () => { state.q = search.value; apply(); });
  function apply() {
    const words = norm(state.q).split(/\\s+/).filter(Boolean);
    let shown = 0;
    cards.forEach(c => {
      const okTag = state.tag === "Tout" || c.dataset.tags.split("|").includes(state.tag);
      const okQ = words.every(w => c.dataset.search.includes(w));
      c.classList.toggle("hidden", !(okTag && okQ)); if (okTag && okQ) shown++;
    });
    chipsBox.querySelectorAll(".chip").forEach(b => b.classList.toggle("active", b.dataset.tag === state.tag));
    empty.hidden = shown > 0;
    try { localStorage.setItem(KEY, JSON.stringify(state)); } catch (e) {}
  }
  apply();
})();
</script>
'''.replace("%TAGS%", __import__("json").dumps(TAGS, ensure_ascii=False))

s = open(f"{REPO}/index.html", encoding="utf-8").read()
# Grille
a = s.index('<p class="section-label">Activités disponibles</p>')
b = s.index('<p class="page-footer">')
grid = ('<p class="section-label">Activités disponibles</p>\n\n<div class="toolbar">\n  <input class="search" id="search" type="search" placeholder="Rechercher une notion : prétérit, did, adjectifs…" autocomplete="off">\n  <div class="chips" id="chips"></div>\n</div>\n\n'
        '<div class="grid">\n\n' + "\n\n".join(cards) + '\n\n  <p class="empty" id="empty" hidden>Aucune activité ne correspond à ta recherche.</p>\n</div>\n\n')
s = s[:a] + grid + s[b:]
if "/* ── Cartes génériques" not in s:
    s = s.replace("  /* ── FOOTER ── */", CSS + "\n  /* ── FOOTER ── */", 1)
s = re.sub(r'<div class="stat-num" id="countActivities">\d+</div>', f'<div class="stat-num" id="countActivities">{len(A)}</div>', s)
s = s.replace('<div class="stat-num">4</div>\n      <div class="stat-label">Niveaux</div>', f'<div class="stat-num">{len(TAGS)}</div>\n      <div class="stat-label">Thèmes</div>')
s = re.sub(r"\n<script>\n\(function \(\) \{\n  const KEY = \"ea_index_filter\".*?</script>\n", "\n", s, flags=re.S)
s = s.replace("</body>", JS + "</body>", 1)
open(f"{REPO}/index.html", "w", encoding="utf-8").write(s)
import os
missing = [x[0] for x in A if not os.path.exists(f"{REPO}/{x[0]}")]
print("cards:", len(A), "missing files:", missing)
