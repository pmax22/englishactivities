import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
import json, re, sys, html as H
REPO = _EA_REPO
G = _EA_OUT
BASE_CSS = open(f"{G}/base.css", encoding="utf-8").read()
EXTRA_CSS = open(f"{G}/extra.css", encoding="utf-8").read()
ENGINE = open(f"{G}/engine.js", encoding="utf-8").read()

def hex2rgb(h):
    h = h.lstrip("#"); return ",".join(str(int(h[i:i+2], 16)) for i in (0, 2, 4))

def page(file, title, tag, h1, subtitle, colors, lesson, verbs_html, js):
    a, b = colors
    css = BASE_CSS.replace("--accent: #ff9f43;", f"--accent: {a};\n    --accent-rgb: {hex2rgb(a)};").replace("--accent2: #e8603c;", f"--accent2: {b};")
    css = css.replace("255,159,67", hex2rgb(a)).replace("232,96,60", hex2rgb(b))
    LESSON_BLOCK = (f'''  <details class="lesson" open>
    <summary>Rappel de la leçon</summary>
    <div class="lesson-body">
{lesson}
    </div>
  </details>''' if lesson else "")
    out = f'''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;0,700;1,300&display=swap" rel="stylesheet">
<style>{css}{EXTRA_CSS}</style>
<link rel="manifest" href="manifest.json">
<meta name="theme-color" content="#0f1117">
<script src="assets/ea.js"></script>
</head>
<body>

<nav class="topnav"><a class="back" href="index.html">← Toutes les activités</a></nav>

<header>
  <div class="tag">{tag}</div>
  <h1>{h1}</h1>
  <p class="subtitle">{subtitle}</p>
</header>

<!-- ═════ MENU ═════ -->
<main class="wrap" id="menu">
{LESSON_BLOCK}
  <div class="missions" id="missions"></div>
</main>

<!-- ═════ QUIZ ═════ -->
<main class="wrap hidden" id="quiz">
  <div class="card">
    <div class="progress-label"><span id="qTitle"></span><span id="qCount"></span></div>
    <div class="progress-bar-wrap"><div class="progress-bar-fill" id="qBar"></div></div>
    <div class="q-instr" id="qInstr"></div>
    <div id="qArea"></div>
    <div id="qFeedback"></div>
    <div class="actions">
      <button class="btn btn-ghost" onclick="showMenu()">Menu</button>
      <button class="btn btn-ghost hidden" id="btnReset" onclick="resetOrder()">Effacer</button>
      <button class="btn btn-primary" id="btnMain" onclick="mainAction()">Valider</button>
    </div>
  </div>
</main>

<!-- ═════ SCORE ═════ -->
<main class="wrap hidden" id="score">
  <div class="card">
    <div class="q-instr" id="sTitle"></div>
    <div class="stars" id="sStars"></div>
    <div class="score-big" id="sScore"></div>
    <p class="score-msg" id="sMsg"></p>
    <div class="actions" style="justify-content:center">
      <button class="btn btn-ghost" onclick="showMenu()">Retour aux missions</button>
      <button class="btn btn-primary" onclick="startMission(current.id)">Recommencer</button>
    </div>
    <div class="recap" id="sRecap"></div>
  </div>
</main>
{('<section class="wrap">' + verbs_html + '</section>') if verbs_html else ''}

<script>
const STORE_KEY = "ea_{file.replace('.html', '')}_v2";
{js}
{ENGINE}
</script>
</body>
</html>
'''
    open(f"{REPO}/{file}", "w", encoding="utf-8").write(out)
    print("written", file, len(out))

def verb_chips(verbs, title="Verbes au programme · BV → prétérit", legend=True):
    chips = "".join(f'<div class="verb-chip{" irr" if v[2] else ""}">{v[0]} <span>{v[1]}</span><em>{v[3]}</em></div>' for v in verbs)
    leg = '<p class="verb-legend">Bordure colorée = verbe irrégulier. Après <b>did</b> / <b>didn\'t</b>, on utilise toujours la BV.</p>' if legend else ""
    return f'<div class="verb-ref"><div class="verb-ref-title">{title}</div><div class="verb-grid">{chips}</div>{leg}</div>'

PRETERIT_LESSON = '''      <p>Le <span class="hl">prétérit</span> sert à parler d'une action <b>terminée</b> dans le passé.</p>
      <p><b>+ Affirmatif</b> : sujet + verbe au prétérit.</p>
      <div class="formula">Verbes <b>réguliers</b> : BV + <span class="hl">-ED</span> (play → played, settle → settled, marry → married)<br>Verbes <b>irréguliers</b> : forme à apprendre (leave → <span class="hl">left</span>, go → <span class="hl">went</span>)</div>
      <p class="ex">He travelled. · She left.</p>
      <p><b>− Négatif</b> : sujet + <span class="hl">didn't</span> (did not) + BV.</p>
      <p class="ex">He didn't travel. · She didn't leave. <s>She didn't left.</s></p>
      <p><b>? Interrogatif</b> : <span class="hl">Did</span> + sujet + BV + ?</p>
      <p class="ex">Did he travel? · Did she leave?</p>
      <p><b>DID</b> porte déjà la marque du passé : après did / didn't, le verbe reste <b>toujours</b> en base verbale.</p>
      <p>Attention au verbe <b>be</b> : I/he/she/it <span class="hl">was</span> · you/we/they <span class="hl">were</span> → négatif <b>wasn't / weren't</b>, question <b>Was he…? / Were they…?</b> (pas de did).</p>'''

def norm_tokens(s):
    return re.sub(r"[.?!]", "", s.lower()).split()

def build_preterit():
    verbs = [["join","joined",0,"rejoindre",["joined"]],["marry","married",0,"se marier",["married"]],["play","played",0,"jouer",["played"]],
             ["be","was / were",1,"être",["was","were"]],["record","recorded",0,"enregistrer",["recorded"]],["settle","settled",0,"s'installer",["settled"]],
             ["leave","left",1,"partir, quitter",["left"]],["divorce","divorced",0,"divorcer",["divorced"]],["die","died",0,"mourir",["died"]],
             ["travel","travelled",0,"voyager",["travelled","traveled"]]]
    forms = {}
    for v in verbs:
        forms[v[0]] = v[0]
        for p in v[4]: forms[p] = v[0]
    data = json.load(open(_EA_OUT+"/data/preterit.json"))
    phrases = []
    for i, q in enumerate(data):
        a0 = q["answers"][0]
        typ = "inter" if a0.startswith("did ") else "neg" if " did not " in a0 or " didnt " in a0 else "aff"
        disp = q["correct"].split(" / ")
        disp = disp[-1] if typ == "neg" and len(disp) > 1 else disp[0]
        dtok = disp.rstrip(".?!").split()
        begins = []
        verb = None
        for a in q["answers"]:
            t = norm_tokens(a)
            start = 2 if typ == "inter" else 1
            idx = next(k for k in range(start, len(t)) if t[k] in forms)
            verb = forms[t[idx]]
            b = " ".join(t[:idx+1])
            if b not in begins: begins.append(b)
        # longueur du début dans la phrase affichée
        lt = norm_tokens(disp)
        idx = next(k for k in range(2 if typ == "inter" else 1, len(lt)) if lt[k] in forms)
        begin_disp = " ".join(dtok[:idx+1])
        end = " ".join(dtok[idx+1:])
        end = (end + ("?" if typ == "inter" else ".")) if end else ""
        subj = " ".join(dtok[:idx-1]) if typ == "neg" else " ".join(dtok[1:idx]) if typ == "inter" else " ".join(dtok[:idx])
        if typ == "inter": subj = subj  # already mid-sentence form
        phrases.append(dict(fr=q["fr"], type=typ, begin=begins, beginDisplay=begin_disp, end=end, hint=q["hint"], expl=q["explanation"], verb=verb,
                            subj=subj if typ != "inter" else (subj[0].upper() + subj[1:] if subj != "I" else "I")))
    js = "const VERBS = " + json.dumps(verbs, ensure_ascii=False) + ";\nconst PHRASES = " + json.dumps(phrases, ensure_ascii=False, indent=0) + ";\n" + open(f"{G}/preterit_common.js", encoding="utf-8").read()
    page("preterit.html", "Prétérit – Entraînement", "Anglais · Grammaire", 'Le Prétérit <span>Simple</span>',
         "Affirmatif · Négatif · Interrogatif", ("#f5c842", "#e07b3f"), PRETERIT_LESSON, verb_chips(verbs), js)
    return phrases

def build_cap():
    verbs = [["help","helped",0,"aider",["helped"]],["go","went",1,"aller",["went"]],["work","worked",0,"travailler",["worked"]],
             ["teach","taught",1,"enseigner",["taught"]],["start","started",0,"commencer",["started"]],["give","gave",1,"donner",["gave"]],
             ["talk","talked",0,"parler",["talked"]],["be","was / were",1,"être",["was","were"]],["organise","organised",0,"organiser",["organised","organized"]],
             ["sell","sold",1,"vendre",["sold"]],["handle","handled",0,"gérer",["handled"]],["spend","spent",1,"passer (du temps), dépenser",["spent"]],
             ["improve","improved",0,"améliorer",["improved"]],["build","built",1,"construire",["built"]],["join","joined",0,"rejoindre",["joined"]],
             ["learn","learnt / learned",1,"apprendre",["learnt","learned"]],["prepare","prepared",0,"préparer",["prepared"]],["have","had",1,"avoir",["had"]]]
    forms = {}
    for v in verbs:
        forms[v[0]] = v[0]
        for p in v[4]: forms[p] = v[0]
    forms["organize"] = "organise"
    data = json.load(open(_EA_OUT+"/data/preterit_cap_sapver.json"))
    phrases = []
    for q in data:
        typ = q["type"]
        t = q["begin"][0].split()
        verb = None
        for w in t:
            if w in forms and not (typ != "aff" and w in ("did",)): verb = forms[w]
        if verb is None: verb = "be"
        disp = t[:]
        # Affichage : majuscule, I, contraction didn't
        b = " ".join(disp)
        b = re.sub(r"\bdid not\b", "didn't", b); b = re.sub(r"\bwas not\b", "wasn't", b); b = re.sub(r"\bwere not\b", "weren't", b)
        b = re.sub(r"\bi\b", "I", b); b = b[0].upper() + b[1:]
        toks = b.split()
        if typ == "aff": subj = " ".join(toks[:-1])
        elif typ == "neg": subj = " ".join(toks[:-2]) if toks[-2] in ("didn't",) else " ".join(toks[:-1])
        else: subj = " ".join(toks[1:-1]) if verb != "be" else " ".join(toks[1:])
        if verb == "be" and typ == "neg": subj = " ".join(toks[:-1])
        if typ == "inter" and subj and subj != "I": subj = subj[0].upper() + subj[1:]
        phrases.append(dict(fr=q["fr"], type=typ, begin=q["begin"], beginDisplay=b, end=q["end"], hint="", expl=q["explanation"], verb=verb, subj=subj))
    js = "const VERBS = " + json.dumps(verbs, ensure_ascii=False) + ";\nconst PHRASES = " + json.dumps(phrases, ensure_ascii=False, indent=0) + ";\n" + open(f"{G}/preterit_common.js", encoding="utf-8").read()
    lesson = PRETERIT_LESSON.replace("(play → played, settle → settled, marry → married)", "(help → helped, work → worked, prepare → prepared)") \
        .replace("(leave → <span class=\"hl\">left</span>, go → <span class=\"hl\">went</span>)", "(sell → <span class=\"hl\">sold</span>, teach → <span class=\"hl\">taught</span>)") \
        .replace("He travelled. · She left.", "I helped the customer. · She sold a dress.") \
        .replace("He didn't travel. · She didn't leave. <s>She didn't left.</s>", "I didn't help the customer. · She didn't sell a dress. <s>She didn't sold.</s>") \
        .replace("Did he travel? · Did she leave?", "Did you help the customer? · Did she sell a dress?")
    page("preterit_cap_sapver.html", "Prétérit – CAP Sapver", "Anglais · CAP Sapver", 'Le Prétérit <span>Simple</span>',
         "Affirmatif · Négatif · Interrogatif — vocabulaire de la vente", ("#4ec9f5", "#3f7ee0"), lesson, verb_chips(verbs), js)
    return phrases

if __name__ == "__main__":
    which = sys.argv[1:] or ["preterit", "cap"]
    if "preterit" in which: ph = build_preterit()
    if "cap" in which: ph2 = build_cap()
    if "dump" in which:
        for p in build_preterit()[::5] + build_cap()[::12]: print(p["type"], "|", p["beginDisplay"], "|", p["end"], "|", p["subj"], "|", p["verb"], "|", p["begin"])

USED_LESSON = '''      <p><span class="hl">Used to</span> sert à parler d'une <b>habitude</b> ou d'une <b>situation passée</b> qui n'existe plus aujourd'hui.</p>
      <p class="ex">I used to live in the north of the USA. = Avant, j'habitais dans le nord des USA (mais plus maintenant).</p>
      <table>
        <tr><th></th><th>Structure</th><th>Exemple</th></tr>
        <tr><td><b>+</b></td><td>sujet + <span class="hl">used to</span> + BV</td><td>She used to play the piano.</td></tr>
        <tr><td><b>−</b></td><td>sujet + <span class="hl">didn't use to</span> + BV</td><td>He didn't use to go skiing.</td></tr>
        <tr><td><b>?</b></td><td><span class="hl">Did</span> + sujet + <span class="hl">use to</span> + BV ?</td><td>Did you use to live here?</td></tr>
      </table>
      <p>Comme au prétérit, <b>did</b> porte la marque du passé : après did / didn't, on écrit <b>use to</b> (sans -d).</p>
      <p>Réponses courtes : <span class="ex">Yes, I did. / No, I didn't.</span></p>'''

def build_used():
    data = json.load(open(_EA_OUT+"/data/used_to.json"))
    js = "const USED = " + json.dumps(data, ensure_ascii=False, indent=0) + ";\n" + open(f"{G}/used_to.js", encoding="utf-8").read()
    page("used_to.html", "Used To – Entraînement", "Anglais · Grammaire", 'Maîtriser <span>Used To</span>',
         "(+) used to + BV · (−) didn't use to + BV · (?) Did … use to + BV ?", ("#7c6af7", "#b47cf0"), USED_LESSON, "", js)

COMP_LESSON = '''      <p>Le <span class="hl">comparatif</span> sert à comparer deux éléments. <b>Than</b> = que.</p>
      <table>
        <tr><th></th><th>Structure</th><th>Exemple</th></tr>
        <tr><td><b>+</b> plus … que</td><td>adjectif court + <span class="hl">-er than</span><br>adjectif long : <span class="hl">more</span> + adj + <span class="hl">than</span></td><td>Hulk is stronger than Thor.<br>Gold is more expensive than silver.</td></tr>
        <tr><td><b>=</b> aussi … que</td><td><span class="hl">as</span> + adjectif + <span class="hl">as</span></td><td>Batman is as brave as Superman.</td></tr>
        <tr><td><b>−</b> moins … que</td><td><span class="hl">less</span> + adjectif + <span class="hl">than</span></td><td>An ant is less strong than an elephant.</td></tr>
      </table>
      <p><b>Adjectifs courts</b> (1 syllabe, ou 2 syllabes en -y) — attention à l'orthographe :</p>
      <div class="formula">tall → taller · nice → nicer (-e : + r) · hot → hotter (consonne doublée) · heavy → heavier (-y → -ier)</div>
      <p><b>Adjectifs longs</b> (2 syllabes ou plus) : more interesting, more expensive, more popular…</p>
      <p><b>Irréguliers</b> : good → <span class="hl">better</span> · bad → <span class="hl">worse</span></p>'''

ADJ = [["strong","stronger","er"],["fast","faster","er"],["tall","taller","er"],["expensive","more expensive","more"],["hot","hotter","double"],
       ["rich","richer","er"],["long","longer","er"],["old","older","er"],["heavy","heavier","ier"],["interesting","more interesting","more"],
       ["brave","braver","r"],["popular","more popular","more"],["busy","busier","ier"],["tiring","more tiring","more"],["intelligent","more intelligent","more"],
       ["creative","more creative","more"],["difficult","more difficult","more"],["beautiful","more beautiful","more"],["powerful","more powerful","more"],
       ["precious","more precious","more"],["deep","deeper","er"],["bright","brighter","er"],["dangerous","more dangerous","more"],["exciting","more exciting","more"],
       ["big","bigger","double"],["small","smaller","er"],["happy","happier","ier"],["young","younger","er"],["nice","nicer","r"],["thin","thinner","double"],
       ["funny","funnier","ier"],["famous","more famous","more"],["good","better","irr"],["bad","worse","irr"],["easy","easier","ier"],["large","larger","r"]]

def build_comp():
    data = json.load(open(_EA_OUT+"/data/comparatif.json"))
    js = "const ADJ = " + json.dumps(ADJ) + ";\nconst COMP = " + json.dumps(data, ensure_ascii=False, indent=0) + ";\n" + open(f"{G}/comparatif.js", encoding="utf-8").read()
    page("comparatif.html", "Comparatif – Entraînement", "Anglais · Grammaire", 'Le <span>Comparatif</span>',
         "(+) -er than / more … than · (=) as … as · (−) less … than", ("#3ecfcf", "#2fa8d8"), COMP_LESSON, "", js)

REG_LESSON = '''      <p>Au prétérit (affirmatif), les verbes se divisent en deux familles.</p>
      <p><b>Verbes réguliers</b> : base verbale + <span class="hl">-ED</span>. Attention à l'orthographe :</p>
      <table>
        <tr><th>Cas</th><th>Règle</th><th>Exemple</th></tr>
        <tr><td>cas général</td><td>+ <span class="hl">-ed</span></td><td>play → played, walk → walked</td></tr>
        <tr><td>se termine par -e</td><td>+ <span class="hl">-d</span></td><td>live → lived, die → died</td></tr>
        <tr><td>consonne + y</td><td>y → <span class="hl">-ied</span></td><td>marry → married, try → tried</td></tr>
        <tr><td>consonne-voyelle-consonne</td><td>on <span class="hl">double</span> la consonne</td><td>stop → stopped</td></tr>
      </table>
      <p><b>Verbes irréguliers</b> : ils ont une <b>forme spéciale</b>, à apprendre par cœur. <span class="ex">go → went · see → saw · take → took</span></p>
      <p>Rappel : après <b>did / didn't</b>, on revient toujours à la base verbale, même pour un verbe irrégulier.</p>'''

FR_V = {"start":"commencer","play":"jouer","watch":"regarder","record":"enregistrer","join":"rejoindre","travel":"voyager","settle":"s'installer",
        "divorce":"divorcer","die":"mourir","marry":"se marier","live":"vivre, habiter","stop":"arrêter","move":"bouger, déménager","ask":"demander",
        "love":"aimer","open":"ouvrir","try":"essayer","call":"appeler","want":"vouloir","walk":"marcher","go":"aller","come":"venir","see":"voir",
        "take":"prendre","leave":"partir, quitter","say":"dire","know":"savoir, connaître","get":"obtenir","make":"faire, fabriquer","think":"penser",
        "find":"trouver","give":"donner","tell":"raconter, dire","hear":"entendre","write":"écrire","run":"courir","begin":"commencer","fall":"tomber",
        "keep":"garder","meet":"rencontrer"}

def build_regirr():
    s = open(f"{REPO}/verbe_regulier_irregulier.html", encoding="utf-8").read() if not "RV = " in open(f"{REPO}/verbe_regulier_irregulier.html", encoding="utf-8").read() else open(_EA_OUT+"/regirr_orig.html", encoding="utf-8").read()
    rv = [dict(past=p, base=b, type=t, fr=FR_V[b]) for p, b, t in re.findall(r'pastForm: "(\w+)",\s*base: "(\w+)",\s*type: "(\w+)"', s)]
    assert len(rv) == 40, len(rv)
    def chips(t): return "".join(f'<div class="verb-chip">{v["base"]} <span>{v["past"]}</span><em>{v["fr"]}</em></div>' for v in rv if v["type"] == t)
    verbs = ('<details class="verb-ref"><summary class="verb-ref-title">Voir la liste des 40 verbes · BV → prétérit</summary>'
             f'<div class="verb-sub">Réguliers</div><div class="verb-grid">{chips("regular")}</div>'
             f'<div class="verb-sub">Irréguliers</div><div class="verb-grid">{chips("irregular")}</div></details>')
    js = "const RV = " + json.dumps(rv, ensure_ascii=False) + ";\n" + open(f"{G}/regirr.js", encoding="utf-8").read()
    page("verbe_regulier_irregulier.html", "Régulier ou Irrégulier ?", "Anglais · Grammaire", 'Régulier ou <span>Irrégulier</span> ?',
         "Le prétérit des verbes : -ED ou forme spéciale ?", ("#4ecb7f", "#2da866"), REG_LESSON, verbs, js)

if __name__ == "__main__":
    if "used" in which: build_used()
    if "comp" in which: build_comp()
    if "regirr" in which: build_regirr()
