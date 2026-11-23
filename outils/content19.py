import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
exec(open(_EA_OUT+"/content11.py", encoding="utf-8").read().split("# ═════════════ CE 1")[0])
TAG = "Anglais · Culture"

def DT(doc, question, opts, tip=""):
    return C(question, opts, doc=doc, tip=tip)

def reperes(intro, dates, words):
    h = f"      <p>{intro}</p>\n"
    h += "".join(f'      <p><span class="hl">{d}</span> — {t}</p>\n' for d, t in dates)
    h += f'      <p><b>Mots clés :</b> {words}</p>'
    return h

import re as _re, os as _os
DOSSIERS = {}
for _f in sorted(_os.listdir(_EA_OUT)):
    if _f.startswith("dossiers") and _f.endswith(".py"):
        _g = {}; exec(open(_EA_OUT+"/" + _f, encoding="utf-8").read(), _g); DOSSIERS.update(_g.get("D_", {}))
_GL = {}; exec(open(_EA_OUT+"/gloss.py", encoding="utf-8").read(), _GL); _GL = _GL["G_"]
_missing = []
def _gloss(file, t):
    for term, g in _GL.get(file, []):
        pos = 0
        while True:
            i = t.find(term, pos)
            if i < 0: _missing.append((file, term)); break
            ls = t.rfind("\n", 0, i) + 1
            if t[ls:ls + 3] == "## ": pos = i + 1; continue
            j = i + len(term)
            if t[j:j + 2] == "**" and t[i:i + 2] != "**": j += 2
            t = t[:j] + " \u27e6" + g + "\u27e7" + t[j:]; break
    return t
for _k in list(DOSSIERS): DOSSIERS[_k] = _gloss(_k, DOSSIERS[_k])
if _missing: print("GLOSS NOT FOUND:", _missing)
def _md(t):
    out, lst = [], []
    def flush():
        if lst: out.append("<ul>" + "".join(f"<li>{x}</li>" for x in lst) + "</ul>"); lst.clear()
    for para in t.strip().split("\n"):
        p = para.strip()
        if not p: flush(); continue
        p = _re.sub("\u27e6(.+?)\u27e7", r'<span class="gl">(\1)</span>', p)
        p = _re.sub(r"\[([^\]]+)\]\(([\w./-]+\.html)\)", r'<a class="dz-link" href="\2">\1</a>', p)
        p = _re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", p); p = _re.sub(r"(?<![\w*])\*(.+?)\*(?![\w*])", r"<i>\1</i>", p)
        if p.startswith("## "): flush(); out.append(f"<h4>{p[3:]}</h4>")
        elif p.startswith("- "): lst.append(p[2:])
        else: flush(); out.append(f"<p>{p}</p>")
    flush(); return "\n".join(out)
DOSSIER_CSS = """<style>
  details.dossier { margin-top: 18px; border: 1px solid var(--border); border-radius: 14px; background: var(--surface2); }
  details.dossier > summary { cursor: pointer; padding: 14px 16px; font-weight: 600; list-style: none; display: flex; gap: 10px; align-items: center; flex-wrap: wrap; }
  details.dossier > summary::-webkit-details-marker { display: none; }
  details.dossier > summary .dz-time { font-weight: 400; font-size: 12px; color: var(--muted); border: 1px solid var(--border); border-radius: 999px; padding: 2px 9px; }
  details.dossier > summary::after { content: "▾"; margin-left: auto; color: var(--muted); } details.dossier[open] > summary::after { content: "▴"; }
  .dz-body { padding: 4px 20px 18px; font-size: 16px; line-height: 1.75; max-width: 70ch; }
  .dz-body h4 { text-transform: none; letter-spacing: 0; font-family: 'Syne', sans-serif; font-size: 17px; margin: 20px 0 6px; color: var(--accent); }
  .dz-body p { margin: 0 0 12px; } .dz-body ul { margin: 0 0 12px 20px; } .dz-body li { margin-bottom: 6px; }
  .dz-body b { color: var(--text); } .dz-body .gl { font-size: .86em; color: var(--muted); font-style: italic; } .dz-link { display: inline-block; margin-top: 4px; padding: 8px 14px; border: 1px solid var(--accent); border-radius: 10px; color: var(--accent); font-weight: 600; text-decoration: none; } .dz-src { margin-top: 22px; padding-top: 10px; border-top: 1px dashed var(--border); } .dz-src ul { margin-left: 18px; } .dz-src li { font-size: 14.5px; } .dz-src a { color: var(--accent); } .dz-link:hover { background: rgba(255,255,255,.06); } .dz-top { font-size: 12.5px; color: var(--muted); margin: 0 0 6px; }
  @media (max-width: 560px) { .dz-body { padding: 2px 14px 14px; font-size: 15.5px; } }
</style>"""
_AUTO = {
 "cu_roaring_twenties": ["Roaring Twenties", "années 1920", "années 20", "Années folles", "années folles"],
 "cu_prohibition": ["Prohibition"], "cu_1929_new_deal": ["Grande Dépression", "krach de 1929", "New Deal"],
 "cu_droits_civiques": ["Martin Luther King", "droits civiques", "Rosa Parks"], "cu_esclavage": ["esclavage"],
 "cu_guerre_secession": ["guerre de Sécession"], "cu_shakespeare": ["Shakespeare"], "cu_hollywood": ["Hollywood"],
 "cu_hip_hop": ["hip-hop"], "cu_musique": ["jazz", "blues", "rock'n'roll"], "cu_swinging_sixties": ["Beatles", "Swinging London"],
 "cu_ww1": ["Première Guerre mondiale"], "cu_ww2_usa": ["Seconde Guerre mondiale", "Pearl Harbor"], "cu_blitz": ["Blitz"],
 "cu_guerre_froide": ["guerre froide"], "cu_red_scare": ["maccarthysme", "McCarthy"], "cu_vietnam": ["guerre du Vietnam"],
 "cu_conquete_spatiale": ["conquête spatiale", "course à l'espace", "course à la Lune"], "cu_kennedy": ["Kennedy"],
 "cu_watergate": ["Watergate"], "cu_11_septembre": ["11 septembre"], "cu_empire": ["Empire britannique"],
 "cu_victoriens": ["reine Victoria", "victorien", "victorienne"], "cu_revolution_industrielle": ["révolution industrielle"],
 "cu_suffragettes": ["suffragettes"], "cu_thatcher": ["Thatcher"], "cu_brexit": ["Brexit"], "cu_famine": ["Grande Famine"],
 "cu_troubles": ["Bloody Sunday", "les Troubles"], "cu_pilgrims": ["Pilgrims", "Mayflower", "Pères pèlerins"],
 "cu_revolution_americaine": ["Déclaration d'indépendance", "guerre d'Indépendance"], "cu_far_west": ["Far West", "cow-boys"],
 "cu_ellis_island": ["Ellis Island"], "cu_reve_americain": ["rêve américain", "American Dream"],
 "cu_famille_royale": ["Diana", "Charles III"], "cu_orwell": ["Orwell"], "cu_dystopies": ["dystopie"],
 "cu_generations": ["Beat Generation", "baby boom", "Baby Boomers"], "cu_route66": ["Route 66"], "cu_silicon_valley": ["Silicon Valley"],
 "cu_sante_usa": ["Obamacare", "Medicare"], "cu_blm": ["Black Lives Matter", "George Floyd"], "cu_cour_supreme": ["Cour suprême"],
 "cu_salem": ["Salem"], "cu_windrush": ["Windrush"], "cu_titanic": ["Titanic"], "cu_tudors": ["Henri VIII", "Tudor"],
 "cu_1066": ["Guillaume le Conquérant"], "cu_sciences": ["Newton", "Darwin", "Turing"], "cu_frankenstein": ["Frankenstein"],
 "cu_super_heros": ["super-héros"], "cu_bbc": ["BBC"], "cu_national_trust": ["National Trust"],
 "cu_explorateurs": ["James Cook", "Shackleton", "Livingstone"], "cu_grands_discours": ["I have a dream"],
 "cu_mark_twain": ["Mark Twain", "Huckleberry"], "cu_fetes_origines": ["Thanksgiving", "Halloween", "Bonfire Night"],
 "cu_juneteenth_columbus": ["Juneteenth", "Columbus Day"], "cu_geographie_usa": ["Yellowstone", "Grand Canyon"],
 "cu_caraibes": ["Barbade"], "cu_jamaique": ["Jamaïque", "reggae"], "cu_afrique_sud": ["apartheid", "Mandela"],
 "cu_lgbt": ["Stonewall"], "cu_consommation": ["Black Friday"], "cu_publicite": ["soft power"], "cu_jeux_video": ["jeux vidéo", "jeu vidéo"],
 "cu_complotisme": ["théorie du complot", "théories du complot"], "cu_gag": ["Chaplin", "Mr Bean"],
 "cu_litterature_jeunesse": ["Harry Potter", "Roald Dahl", "Tolkien"], "cu_romans": ["Steinbeck", "Jane Austen", "Brontë"],
 "cu_baldwin": ["James Baldwin"], "cu_peuples_autochtones": ["Stolen Generations", "Aborigènes", "Premières Nations"],
 "cu_armes_usa": ["deuxième amendement", "Second Amendment"], "cu_dystopies_": [], "cu_porto_rico": ["Porto Rico"],
 "cu_explorateurs_": [], "cu_hong_kong": ["Hong Kong"], "cu_inde": ["Gandhi"], "cu_monarchie": ["monarchie britannique"],
 "cu_amerindiens": ["Amérindiens"], "cu_humour": ["Monty Python"], "cu_memoire": ["Remembrance Day", "coquelicot"],
}
def _titles():
    if "_T" in globals(): return _T
    src = open(_EA_OUT+"/index_gen2.py", encoding="utf-8").read()
    g = {}; exec(src.split("\n_L = {")[0], g)
    globals()["_T"] = {a[0][:-5]: a[7] for a in g["A"]}
    return _T
def _autolinks(file, t):
    me = file[:-5]; T = _titles(); found = []
    for tgt, kws in _AUTO.items():
        if tgt == me or not kws or tgt not in T or f"({tgt}.html)" in t: continue
        n = sum(len(_re.findall(r"(?<![\w-])" + _re.escape(k) + r"(?![\w-])", t)) for k in kws)
        if n: found.append((-n, t.find(next(k for k in kws if k in t)), tgt))
    found.sort()
    return "".join(f"\n[→ Voir aussi : {T[tgt]}]({tgt}.html)" for _, _, tgt in found[:4])
def _src_html(file):
    _sg = {}; exec(open(_EA_OUT+"/sources.py", encoding="utf-8").read(), _sg)
    L = _sg["SRC"].get(file[:-5])
    if not L: return ""
    import html as _h
    li = "".join(f'<li><a href="{_h.escape(u)}" target="_blank" rel="noopener">{_h.escape(n)}</a></li>' for n, u in L)
    return ('<div class="dz-src"><h4>Pour aller plus loin</h4><p class="dz-top">Sources fiables, en anglais pour la plupart, '
            'pour vérifier ou approfondir. Liens vérifiés le 23 novembre 2026.</p><ul>' + li + '</ul></div>')
def dossier_html(file):
    t = DOSSIERS.get(file)
    if not t: return ""
    _ex = {}; exec(open(_EA_OUT+"/extras.py", encoding="utf-8").read(), _ex)
    if _ex["EXTRA"].get(file[:-5]): t = t.rstrip() + "\n" + _ex["EXTRA"][file[:-5]].strip()
    t = t.rstrip() + _autolinks(file, t)
    words = len(_re.sub(r"<[^>]+>", " ", t).split()); mins = max(2, round(words / 130))
    return (DOSSIER_CSS + f'\n      <details class="dossier"><summary>📖 Le dossier complet <span class="dz-time">⏱ {mins} min de lecture</span></summary>'
            f'<div class="dz-body"><p class="dz-top">Pour approfondir, au calme : pendant le quart d\'heure lecture, dans le bus… Les mots en gras sont à connaître en anglais.</p>{_md(t)}{_src_html(file)}</div></details>')

N1 = {}
for _f in sorted(_os.listdir(_EA_OUT)):
    if _f.startswith("niveau1_") and _f.endswith(".py"):
        _g = {}; exec(open(_EA_OUT+"/" + _f, encoding="utf-8").read(), _g); N1.update(_g.get("N1_", {}))
G1, G2 = "Niveau 1 · Découverte (en français)", "Niveau 2 · Approfondissement (en anglais)"

def level1(file, docs):
    if file not in N1: return {}, []
    vtxt, dq = N1[file]
    pairs = [tuple(x.strip() for x in l.split("=", 1)) for l in vtxt.strip().split("\n") if "=" in l]
    data, ms = {}, []
    k = 4 if len(pairs) % 4 != 1 else 5
    chunks = [pairs[i:i + k] for i in range(0, len(pairs), k)]
    if len(chunks) > 1 and len(chunks[-1]) < 3: chunks[-2] += chunks.pop()
    data["mv"] = ("match", "Associe chaque mot anglais à sa traduction", [{"kind": "match", "pairs": [list(p) for p in c], "label": "Associer : " + ", ".join(p[0] for p in c)} for c in chunks])
    ms.append(M("mv", "🔗", "Associe les mots", "Relie chaque mot anglais à sa traduction française.", ["mv"], len(chunks), group=G1, ordered=True))
    tv, n = [], len(pairs)
    for i, (en, fr) in enumerate(pairs):
        o = [pairs[(i + j) % n] for j in (2, 5) if n > 5] or [pairs[(i + 1) % n], pairs[(i + 2) % n]]
        if i % 2 == 0: tv.append(C(None, [fr] + [x[1] for x in o], fr=f"Que veut dire « {en} » ?"))
        else: tv.append(C(None, [en] + [x[0] for x in o], fr=f"Comment dit-on « {fr} » en anglais ?"))
    data["tv"] = ("choice", "Choisis la bonne traduction", tv)
    ms.append(M("tv", "🔤", "Que veut dire… ?", "Traduis les mots clés, dans les deux sens.", ["tv"], min(8, len(tv)), group=G1))
    t = DOSSIERS.get(file)
    if t and dq:
        lines = [l.strip() for l in t.strip().split("\n") if l.strip()]
        def _clean(l):
            l = _re.sub(r"\*\*(.+?)\*\*", "\u00a7\u00a7\\1\u00a7\u00a7", l.lstrip("- ")); l = _re.sub(r"\*(.+?)\*", r"\1", l)
            return _re.sub("\u27e6(.+?)\u27e7", r"(\1)", l.replace("\u00a7\u00a7", "**"))
        lines = [l for l in lines if not _re.match(r"\[.*\]\(.*\.html\)$", l.strip())]
        lines = [l if l.startswith("## ") else _clean(l) for l in lines]
        docs["dz"] = {"title": "Relire le dossier complet", "audio": False, "fold": True, "lines": lines}
        data["dq"] = ("choice", "Réponds en t'aidant du dossier complet", [C(q, list(o), doc="dz", tip=tip) for q, o, tip in dq])
        ms.append(M("dq", "📖", "Questions sur le dossier", "Questions en français sur le dossier complet. Tu peux le relire pendant la mission.", ["dq"], len(dq), group=G1, ordered=True))
    return data, ms

def culture(file, title, h1, sub, colors, lesson, docs, tf, qs, dates, ws):
    lesson = lesson + dossier_html(file)
    docs = dict(docs)
    data, ms = level1(file, docs)
    g2 = G2 if ms else None
    data.update({"tf": ("choice", "Vrai ou faux ?", tf), "q": ("choice", "Choisis la bonne réponse", qs)})
    ms += [M("tf", "✅", "Vrai ou faux ?", "Lis chaque affirmation et vérifie dans le document.", ["tf"], len(tf), group=g2, ordered=True),
           M("q", "❓", "Questions de compréhension", "Choisis la bonne réponse.", ["q"], len(qs), group=g2, ordered=True)]
    if dates:
        data["d"] = ("choice", "Dates, personnages et repères", dates)
        ms.append(M("d", "📅", "Repères", "Dates, lieux, personnages : retiens l'essentiel.", ["d"], len(dates), group=g2))
    if ws:
        data["w"] = ("gap", "Trouve le mot dans le document", ws)
        ms.append(M("w", "🔍", "Vocabulaire", "Retrouve le mot anglais dans le document.", ["w"], len(ws), group=g2, ordered=True))
    newpage(file, title, h1, sub, colors, lesson, data, ms, tag=TAG, docs=docs)

def doc(title, lines): return {"title": title, "audio": False, "lines": lines}

# ════════════════════ ROYAUME-UNI ════════════════════
D = "uk"
culture("cu_uk.html", "Culture : The United Kingdom", 'The United <span>Kingdom</span>',
  "Culture · quatre nations, un royaume", ("#93c5fd", "#1d4ed8"),
  reperes("Le <b>Royaume-Uni</b> (the United Kingdom) réunit quatre nations. La <b>Grande-Bretagne</b> (Great Britain), c'est seulement l'île : Angleterre, Écosse, pays de Galles.",
    [("England", "capitale London"), ("Scotland", "capitale Edinburgh"), ("Wales", "capitale Cardiff"), ("Northern Ireland", "capitale Belfast")],
    "a nation, a flag, a patron saint, the pound (£), the King"),
  {D: doc("Welcome to the United Kingdom!", [
    "The United Kingdom, or the UK, is a country made of four nations: England, Scotland, Wales and Northern Ireland. Its full name is \"the United Kingdom of Great Britain and Northern Ireland\".",
    "Great Britain is the name of the biggest island. England, Scotland and Wales are on this island. Northern Ireland is on the island of Ireland, next to the Republic of Ireland, which is a different country.",
    "The capital of the UK is London. It is also the capital of England. The other capitals are Edinburgh in Scotland, Cardiff in Wales and Belfast in Northern Ireland.",
    "Nearly 70 million people live in the UK. The official language is English, but some people also speak Welsh in Wales and Scottish Gaelic in Scotland.",
    "The British flag is called the Union Jack. It mixes the crosses of three patron saints: Saint George for England, Saint Andrew for Scotland and Saint Patrick for Ireland. Wales is not on the flag: its own flag has a red dragon!",
    "The UK has a king. Since 2022, the King is Charles III. The money is the pound sterling (£). And people drive on the left!"])},
  [TF(D, "The UK is made of four nations.", True, "England, Scotland, Wales, Northern Ireland."),
   TF(D, "Great Britain and the United Kingdom mean exactly the same thing.", False, "Great Britain = l'île (sans l'Irlande du Nord)."),
   TF(D, "Northern Ireland is on the island of Great Britain.", False, "Elle est sur l'île d'Irlande."),
   TF(D, "Cardiff is the capital of Wales.", True, "« Cardiff in Wales »."),
   TF(D, "Some people speak Welsh in Wales.", True, "« some people also speak Welsh in Wales »."),
   TF(D, "The Welsh dragon is on the Union Jack.", False, "« Wales is not on the flag »."),
   TF(D, "In the UK, people drive on the right.", False, "« people drive on the left! »")],
  [Q(D, "What is the capital of Scotland?", ["Edinburgh.", "Glasgow.", "Belfast."]),
   Q(D, "What is the British flag called?", ["The Union Jack.", "The Stars and Stripes.", "The Red Dragon."]),
   Q(D, "Who is the patron saint of England?", ["Saint George.", "Saint Andrew.", "Saint Patrick."]),
   Q(D, "What is the money in the UK?", ["The pound sterling.", "The euro.", "The dollar."]),
   Q(D, "Is the Republic of Ireland part of the UK?", ["No, it's a different country.", "Yes, since 2022.", "Yes, it's the fifth nation."])],
  [DT(D, "Quelle est la capitale de l'Irlande du Nord ?", ["Belfast", "Dublin", "Cardiff", "Edinburgh"]),
   DT(D, "Quelle est la plus grande île du Royaume-Uni ?", ["Great Britain", "Ireland", "Wales", "Scotland"]),
   DT(D, "Qui est roi depuis 2022 ?", ["Charles III", "William", "George VI", "Henry VIII"]),
   DT(D, "Combien d'habitants environ ?", ["Près de 70 millions", "Près de 7 millions", "Près de 300 millions", "Près de 30 millions"])],
  [W(D, "Trouve le mot qui veut dire « drapeau ».", "flag"), W(D, "Trouve l'expression qui veut dire « saint patron ».", ["patron saint", "patron saints"]),
   W(D, "Trouve le mot qui veut dire « île ».", "island"), W(D, "Trouve le mot qui veut dire « roi ».", "king")])

D = "roy"
culture("cu_monarchie.html", "Culture : The Royal Family", 'The Royal <span>Family</span>',
  "Culture · la monarchie britannique", ("#fde68a", "#b45309"),
  reperes("Le Royaume-Uni est une <b>monarchie constitutionnelle</b> : le roi est chef de l'État, mais ce sont le Parlement et le gouvernement qui décident. On dit : <i>the monarch reigns but does not rule</i>.",
    [("1534", "Henry VIII rompt avec Rome : naissance de l'Église d'Angleterre"), ("1837 – 1901", "règne de Victoria"), ("1952 – 2022", "règne d'Elizabeth II, 70 ans"),
     ("8 sept. 2022", "mort d'Elizabeth II, Charles III devient roi"), ("6 mai 2023", "couronnement de Charles III à Westminster Abbey")],
    "the monarch, to reign, the throne, the heir, a coronation, the Crown"),
  {D: doc("The Crown: kings and queens of Britain", [
    "The British monarchy is more than a thousand years old. Some kings and queens are very famous. Henry VIII, in the 16th century, had six wives. When the Pope refused his divorce, he created the Church of England and became its head.",
    "Queen Victoria reigned from 1837 to 1901, when Britain had a huge empire. Her reign was so important that we call this period \"the Victorian era\".",
    "Elizabeth II became queen in 1952, when she was only 25. She reigned for 70 years, longer than any other British monarch. When she died in September 2022, millions of people watched her funeral on television.",
    "Her son became King Charles III. He was crowned in Westminster Abbey on 6 May 2023. His wife is Queen Camilla. The heir to the throne is his elder son, William, Prince of Wales. William has three children: George, Charlotte and Louis.",
    "Today, the King has a mostly symbolic role. He is the head of state, but he doesn't make political decisions: he must stay neutral. He opens Parliament every year with the King's Speech, but the speech is written by the government.",
    "Not everyone loves the monarchy. Some people, called republicans, think it is too expensive and that the head of state should be elected. But many British people see the Royal Family as a symbol of history and tradition, and it attracts many tourists to places like Buckingham Palace."])},
  [TF(D, "Henry VIII created the Church of England.", True, "« he created the Church of England »."),
   TF(D, "Queen Victoria reigned in the 20th century only.", False, "1837-1901 : surtout au 19e siècle."),
   TF(D, "Elizabeth II reigned for 70 years.", True, "« She reigned for 70 years »."),
   TF(D, "Charles III was crowned in 2023.", True, "« on 6 May 2023 »."),
   TF(D, "The heir to the throne is Prince George.", False, "C'est William, Prince of Wales."),
   TF(D, "The King writes the King's Speech himself.", False, "« the speech is written by the government »."),
   TF(D, "All British people support the monarchy.", False, "Les « republicans » s'y opposent.")],
  [Q(D, "Why did Henry VIII create the Church of England?", ["Because the Pope refused his divorce.", "Because he wanted to be Pope.", "Because Parliament asked him."]),
   Q(D, "What is \"the Victorian era\"?", ["The period of Queen Victoria's reign.", "A famous palace.", "A war against France."]),
   Q(D, "What is the King's role today?", ["Mostly symbolic: he must stay neutral.", "He chooses the laws.", "He leads the army in wars."]),
   Q(D, "What do republicans want?", ["An elected head of state.", "A stronger king.", "A new queen."]),
   Q(D, "How many children does William have?", ["Three.", "Two.", "Six."])],
  [DT(D, "Quand Elizabeth II est-elle devenue reine ?", ["1952", "1937", "1901", "1972"]),
   DT(D, "Où sont couronnés les monarques britanniques ?", ["Westminster Abbey", "Buckingham Palace", "Windsor Castle", "St Paul's Cathedral"]),
   DT(D, "Qui est l'héritier du trône ?", ["William, Prince of Wales", "Prince Harry", "Prince George", "Queen Camilla"]),
   DT(D, "Combien d'épouses Henry VIII a-t-il eues ?", ["Six", "Deux", "Huit", "Quatre"]),
   DT(D, "Comment appelle-t-on le régime britannique ?", ["Une monarchie constitutionnelle", "Une monarchie absolue", "Une république", "Une dictature"])],
  [W(D, "Trouve le mot qui veut dire « héritier ».", "heir"), W(D, "Trouve le mot qui veut dire « funérailles ».", "funeral"),
   W(D, "Trouve le mot qui veut dire « régner » (au prétérit).", "reigned"), W(D, "Trouve le mot qui veut dire « chef de l'État ».", "head of state")])

D = "gov"
culture("cu_institutions_uk.html", "Culture : How the UK is governed", 'How the UK <span>is governed</span>',
  "Culture · Parlement, Premier ministre, élections", ("#a7f3d0", "#047857"),
  reperes("Le pouvoir politique est au <b>Parlement de Westminster</b>, à Londres. Le Royaume-Uni n'a pas de constitution écrite en un seul texte.",
    [("House of Commons", "650 députés élus (MPs)"), ("House of Lords", "membres non élus, relit les lois"), ("Prime Minister", "chef du gouvernement, au 10 Downing Street"),
     ("1999", "dévolution : parlements en Écosse, au pays de Galles et en Irlande du Nord")],
    "an MP, a general election, a constituency, a majority, a party, devolution"),
  {D: doc("Who runs the country?", [
    "The UK is a parliamentary democracy. The most important institution is Parliament, in the Palace of Westminster, in London. You can see Big Ben, the famous clock tower, next to it.",
    "Parliament has two houses. The House of Commons has 650 Members of Parliament, or MPs. Each MP is elected in a small area called a constituency. The House of Lords is not elected: its members are appointed. They study and improve the laws, but the Commons has the last word.",
    "A general election takes place at least every five years. In each constituency, the candidate with the most votes wins, even without 50% of the votes. This system is called \"first past the post\".",
    "The leader of the party with a majority of MPs becomes Prime Minister. The Prime Minister lives and works at 10 Downing Street and chooses the ministers of the government, called the Cabinet.",
    "For a long time, two big parties have dominated British politics: the Conservative Party (the Tories) and the Labour Party. Other parties include the Liberal Democrats, the Scottish National Party and Reform UK.",
    "Since 1999, Scotland, Wales and Northern Ireland have their own parliaments or assemblies for some subjects, like education and health. This is called devolution."])},
  [TF(D, "The UK Parliament is in Edinburgh.", False, "Au Palace of Westminster, à Londres."),
   TF(D, "The House of Commons has 650 MPs.", True, "« 650 Members of Parliament »."),
   TF(D, "Members of the House of Lords are elected.", False, "« its members are appointed »."),
   TF(D, "A general election takes place at least every five years.", True, "« at least every five years »."),
   TF(D, "A candidate needs more than 50% of the votes to win.", False, "« even without 50% of the votes »."),
   TF(D, "The Prime Minister lives at 10 Downing Street.", True, "« lives and works at 10 Downing Street »."),
   TF(D, "Scotland has its own parliament for some subjects.", True, "C'est la dévolution.")],
  [Q(D, "What is a constituency?", ["The area where an MP is elected.", "A government minister.", "A political party."]),
   Q(D, "Who becomes Prime Minister?", ["The leader of the party with a majority of MPs.", "The oldest MP.", "The person chosen by the King alone."]),
   Q(D, "What is \"first past the post\"?", ["The candidate with the most votes wins.", "The first MP to arrive wins.", "A system with two rounds of voting."]),
   Q(D, "What is the Cabinet?", ["The main ministers of the government.", "The King's family.", "A room in Big Ben."]),
   Q(D, "What is devolution?", ["Giving some powers to Scotland, Wales and Northern Ireland.", "Leaving the European Union.", "Electing the House of Lords."])],
  [DT(D, "Comment appelle-t-on les députés britanniques ?", ["MPs", "Senators", "Lords", "Ministers"]),
   DT(D, "Quel est le surnom du Parti conservateur ?", ["The Tories", "The Whigs", "The Reds", "The Unionists"]),
   DT(D, "En quelle année la dévolution a-t-elle commencé ?", ["1999", "1973", "2016", "1066"]),
   DT(D, "Comment s'appelle la célèbre horloge du Parlement ?", ["Big Ben", "Big Bob", "London Eye", "Tower Bridge"])],
  [W(D, "Trouve le mot qui veut dire « élu » (participe).", "elected"), W(D, "Trouve le mot qui veut dire « une majorité ».", ["a majority", "majority"]),
   W(D, "Trouve le mot qui veut dire « parti politique ».", ["party", "political party"]), W(D, "Trouve le mot qui veut dire « voix, votes ».", "votes")])

D = "emp"
culture("cu_empire.html", "Culture : From Empire to Commonwealth", 'From Empire to <span>Commonwealth</span>',
  "Culture · l'Empire britannique, les dominions, le Commonwealth", ("#fca5a5", "#b91c1c"),
  reperes("Au début du 20e siècle, l'<b>Empire britannique</b> couvre environ un quart des terres émergées. Les colonies de peuplement deviennent des <b>dominions</b>, autonomes, puis indépendantes.",
    [("1867", "le Canada devient le premier dominion"), ("1901", "naissance de l'Australie (fédération)"), ("1907 / 1910", "Nouvelle-Zélande / Union sud-africaine"),
     ("1931", "Statut de Westminster : les dominions sont égaux au Royaume-Uni"), ("1947", "indépendance de l'Inde et partition"),
     ("1948", "arrivée du <i>Windrush</i> : immigration caribéenne"), ("1949", "naissance du Commonwealth moderne")],
    "an empire, a colony, a dominion, self-government, independence, decolonisation"),
  {D: doc("The sun never sets…", [
    "In the 1920s, the British Empire was the largest empire in history. It ruled about a quarter of the world's land and population. People said it was \"the empire on which the sun never sets\", because it was always daytime somewhere in the Empire.",
    "Some colonies had many settlers from Britain, like Canada, Australia, New Zealand and South Africa. They slowly obtained self-government and became \"dominions\": Canada first, in 1867, then Australia in 1901, New Zealand in 1907 and South Africa in 1910.",
    "The dominions fought alongside Britain in the First World War, and they wanted more freedom. In 1931, the Statute of Westminster made them equal to Britain and free to make their own laws.",
    "After the Second World War, Britain was weak and many colonies demanded independence. India became independent in 1947, but it was divided into two countries, India and Pakistan, and millions of people had to move. In Africa and in the Caribbean, many countries became independent in the 1950s and 1960s.",
    "People from the colonies also came to Britain. In 1948, the ship Empire Windrush brought hundreds of workers from the Caribbean. They helped to rebuild the country, and today we call them \"the Windrush generation\".",
    "The Empire disappeared, but the Commonwealth was born in 1949. It is a free association of more than 50 countries, most of them former British colonies. They share the English language and some traditions, like the Commonwealth Games, a sports competition held every four years."])},
  [TF(D, "In the 1920s, the Empire ruled about a quarter of the world.", True, "« about a quarter of the world's land and population »."),
   TF(D, "Australia was the first dominion.", False, "Le Canada, en 1867."),
   TF(D, "The Statute of Westminster made the dominions equal to Britain.", True, "1931."),
   TF(D, "India was divided into two countries in 1947.", True, "India et Pakistan."),
   TF(D, "The Windrush brought workers from India.", False, "« from the Caribbean »."),
   TF(D, "All Commonwealth countries were British colonies.", False, "« most of them »."),
   TF(D, "The Commonwealth Games take place every year.", False, "« every four years »." )],
  [Q(D, "Why was it \"the empire on which the sun never sets\"?", ["Because it was always daytime somewhere in the Empire.", "Because it was very hot.", "Because the King never slept."]),
   Q(D, "What is a dominion?", ["A colony with self-government.", "A British city.", "A war ship."]),
   Q(D, "Why did many colonies get independence after 1945?", ["Britain was weak and colonies demanded independence.", "The King wanted a smaller empire.", "The colonies wanted to join France."]),
   Q(D, "Who are \"the Windrush generation\"?", ["Caribbean people who came to work in Britain after 1948.", "British soldiers in India.", "Settlers in Australia."]),
   Q(D, "What is the Commonwealth today?", ["A free association of more than 50 countries.", "A new British empire.", "A European organisation."])],
  [DT(D, "Quel pays devient dominion en 1867 ?", ["Canada", "Australia", "India", "Jamaica"]),
   DT(D, "Quand l'Inde devient-elle indépendante ?", ["1947", "1931", "1867", "1962"]),
   DT(D, "Quel texte rend les dominions égaux au Royaume-Uni ?", ["Le Statut de Westminster (1931)", "La Magna Carta", "Le Bill of Rights", "Le traité de Versailles"]),
   DT(D, "Quand naît le Commonwealth moderne ?", ["1949", "1901", "1973", "1919"])],
  [W(D, "Trouve le mot qui veut dire « colons ».", "settlers"), W(D, "Trouve le mot qui veut dire « autonomie (gouvernement par soi-même) ».", "self-government"),
   W(D, "Trouve le mot qui veut dire « réclamer, exiger » (au prétérit).", "demanded"), W(D, "Trouve le mot qui veut dire « reconstruire ».", ["rebuild", "to rebuild"])])

D = "brx"
culture("cu_brexit.html", "Culture : Brexit", 'Brexit',
  "Culture · le Royaume-Uni quitte l'Union européenne", ("#c7d2fe", "#4338ca"),
  reperes("<b>Brexit</b> = <i>Britain</i> + <i>exit</i>. Après 47 ans dans la construction européenne, le Royaume-Uni quitte l'Union européenne.",
    [("1973", "entrée dans la CEE"), ("23 juin 2016", "référendum : 51,9 % pour le départ (Leave)"), ("2017 – 2019", "négociations difficiles, Theresa May puis Boris Johnson"),
     ("31 janv. 2020", "sortie officielle de l'UE"), ("1er janv. 2021", "fin de la période de transition"), ("2023", "Windsor Framework sur l'Irlande du Nord")],
    "a referendum, to leave / to remain, sovereignty, a deal, a border, free movement"),
  {D: doc("Leave or Remain?", [
    "The UK joined the European Economic Community in 1973. But many British people always had doubts about Europe. In 2016, Prime Minister David Cameron organised a referendum with a simple question: should the UK remain in the European Union or leave it?",
    "On 23 June 2016, 51.9% of voters chose to leave. The country was divided: England and Wales voted Leave, but Scotland and Northern Ireland voted Remain. Young people voted mostly Remain, older people mostly Leave. David Cameron, who wanted to remain, resigned the next day.",
    "Leave supporters used the slogan \"Take back control\". They wanted Britain to make its own laws, control immigration and stop paying money to the EU. Remain supporters said that leaving would hurt the economy, trade and jobs.",
    "The negotiations were long and difficult. Parliament rejected Theresa May's deal three times. Her successor, Boris Johnson, won a big majority in the December 2019 election with the promise \"Get Brexit done\". The UK officially left the EU on 31 January 2020.",
    "The most difficult question was the border between Northern Ireland, in the UK, and the Republic of Ireland, in the EU. Nobody wanted to bring back a hard border, because of the peace agreement of 1998. So special rules were created for Northern Ireland.",
    "Brexit changed daily life: there are more checks on goods, and Europeans now need visas to work in the UK, like British people in the EU. Years later, the British are still divided about the results of Brexit."])},
  [TF(D, "The UK joined the EEC in 1973.", True, "« in 1973 »."),
   TF(D, "Leave won with more than 60% of the votes.", False, "51,9 %."),
   TF(D, "Scotland voted to remain in the EU.", True, "« Scotland and Northern Ireland voted Remain »."),
   TF(D, "Young people mostly voted Leave.", False, "« Young people voted mostly Remain »."),
   TF(D, "David Cameron wanted to leave the EU.", False, "« who wanted to remain »."),
   TF(D, "Parliament rejected Theresa May's deal three times.", True, "« three times »."),
   TF(D, "The UK left the EU on 31 January 2020.", True, "« officially left the EU on 31 January 2020 »." )],
  [Q(D, "What was the question of the referendum?", ["Should the UK remain in the EU or leave it?", "Should Scotland be independent?", "Should the UK have a new king?"]),
   Q(D, "What did \"Take back control\" mean for Leave supporters?", ["Making their own laws and controlling immigration.", "Joining the euro.", "Giving more money to the EU."]),
   Q(D, "What did Remain supporters fear?", ["Damage to the economy, trade and jobs.", "Too many British tourists.", "A new war in Europe."]),
   Q(D, "Why was the Irish border a difficult question?", ["Nobody wanted a hard border because of the 1998 peace agreement.", "Because Ireland wanted to leave the EU too.", "Because the border is very long."]),
   Q(D, "What changed in daily life?", ["More checks on goods and visas to work.", "People drive on the right.", "The UK adopted the euro."])],
  [DT(D, "Quel Premier ministre a organisé le référendum ?", ["David Cameron", "Boris Johnson", "Theresa May", "Tony Blair"]),
   DT(D, "Quel était le slogan de Boris Johnson en 2019 ?", ["Get Brexit done", "Take back control", "Yes we can", "Keep calm and carry on"]),
   DT(D, "Quel pourcentage a voté Leave ?", ["51,9 %", "48,1 %", "62 %", "75 %"]),
   DT(D, "Quel accord de paix de 1998 rend la frontière irlandaise sensible ?", ["L'accord du Vendredi saint", "Le traité de Rome", "Le Statut de Westminster", "Le traité de Maastricht"])],
  [W(D, "Trouve le mot qui veut dire « démissionner » (au prétérit).", "resigned"), W(D, "Trouve le mot qui veut dire « électeurs ».", "voters"),
   W(D, "Trouve le mot qui veut dire « frontière ».", "border"), W(D, "Trouve le mot qui veut dire « marchandises ».", "goods")])

# ════════════════════ IRLANDE ════════════════════
D = "fam"
culture("cu_famine.html", "Culture : The Great Famine", 'The Great <span>Famine</span>',
  "Culture · l'Irlande de 1845 à 1852", ("#bbf7d0", "#15803d"),
  reperes("En 1845, l'Irlande fait partie du Royaume-Uni depuis l'Acte d'Union de 1800. La majorité des paysans pauvres vit presque uniquement de la pomme de terre. En irlandais, la Grande Famine s'appelle <i>An Gorta Mór</i>.",
    [("1845", "le mildiou (potato blight) détruit les récoltes"), ("1846", "abolition des Corn Laws ; nouvelles récoltes perdues"), ("1847", "« Black '47 », l'année la plus terrible ; soupes populaires"),
     ("1845 – 1852", "environ 1 million de morts, plus d'1 million d'émigrés"), ("Après 1852", "l'émigration continue : immense diaspora irlandaise")],
    "a famine, a crop, a blight, starvation, to emigrate, an eviction, a landlord, the diaspora"),
  {D: doc("When the potatoes turned black", [
    "In the 1840s, Ireland was part of the United Kingdom. About eight million people lived on the island, and most of them were poor farmers. They rented small pieces of land from rich landlords, many of them English or living in England.",
    "For the poorest families, the potato was almost the only food. In 1845, a disease called the potato blight arrived from America. The potatoes turned black and rotten in the fields. The disease came back in the following years, and the worst year was 1847, known as \"Black '47\".",
    "Without potatoes, people had nothing to eat. Hundreds of thousands died of starvation and of diseases like typhus and cholera. Families who couldn't pay their rent were evicted from their homes. Many went to workhouses, where conditions were terrible.",
    "The British government organised some help, like soup kitchens and public works, but it was not enough and it often came too late. Many ministers believed that the state should not interfere with the economy. At the same time, Ireland continued to export food like grain and meat to England.",
    "In total, about one million people died, and more than one million emigrated, mostly to the United States, Canada and Britain. They travelled in overcrowded ships, sometimes called \"coffin ships\", because so many passengers died during the journey.",
    "The Famine changed Ireland forever. The population of the island has never returned to its 1841 level. It also created a huge Irish diaspora: today, tens of millions of Americans have Irish ancestors. For many Irish people, the Famine remains a symbol of British injustice, and it fed the movement for Irish independence."])},
  [TF(D, "In the 1840s, Ireland was an independent country.", False, "« Ireland was part of the United Kingdom »."),
   TF(D, "Most farmers owned their land.", False, "Ils louaient leurs terres (rented) à des landlords."),
   TF(D, "The potato blight arrived in 1845.", True, "« In 1845, a disease called the potato blight arrived »."),
   TF(D, "1847 was the worst year of the Famine.", True, "« Black '47 »."),
   TF(D, "Ireland stopped exporting food during the Famine.", False, "« Ireland continued to export food »."),
   TF(D, "About one million people died.", True, "« about one million people died »."),
   TF(D, "Today, the population of Ireland is bigger than in 1841.", False, "« has never returned to its 1841 level »." )],
  [Q(D, "Why were the poorest families so dependent on potatoes?", ["It was almost their only food.", "Potatoes were very expensive.", "They sold potatoes to England."]),
   Q(D, "What happened to families who couldn't pay their rent?", ["They were evicted from their homes.", "They received free land.", "They became landlords."]),
   Q(D, "Why was the government's help not enough?", ["Many ministers thought the state should not interfere with the economy.", "The Queen refused to help.", "There was no money in Britain."]),
   Q(D, "Why were they called \"coffin ships\"?", ["Because so many passengers died during the journey.", "Because they transported coffins.", "Because they were black."]),
   Q(D, "What is the long-term consequence of the Famine?", ["A huge Irish diaspora and a symbol of British injustice.", "Ireland became richer.", "The potato disappeared from Ireland."])],
  [DT(D, "Comment appelle-t-on la maladie de la pomme de terre ?", ["The potato blight", "The black death", "The cholera", "The typhus"]),
   DT(D, "Quelles sont les dates de la Grande Famine ?", ["1845 – 1852", "1800 – 1815", "1914 – 1918", "1916 – 1922"]),
   DT(D, "Vers quel pays la plupart des émigrés partent-ils ?", ["Les États-Unis", "La France", "L'Australie", "L'Inde"]),
   DT(D, "Comment dit-on « la Grande Famine » en irlandais ?", ["An Gorta Mór", "Sinn Féin", "Dáil Éireann", "Fianna Fáil"])],
  [W(D, "Trouve le mot qui veut dire « propriétaires terriens ».", ["landlords", "landlord"]), W(D, "Trouve le mot qui veut dire « mourir de faim / la famine » (nom en -ation).", "starvation"),
   W(D, "Trouve le mot qui veut dire « expulsés » (participe).", "evicted"), W(D, "Trouve le mot qui veut dire « ancêtres ».", "ancestors")])

D, D2, D3 = "bs", "hb", "gf"
culture("cu_troubles.html", "Culture : Northern Ireland and the Troubles", 'Northern Ireland <span>&amp; the Troubles</span>',
  "Culture · Bloody Sunday, les grèves de la faim, la paix", ("#fed7aa", "#c2410c"),
  reperes("Les <b>Troubles</b> (environ 1968-1998) opposent en Irlande du Nord les <b>unionistes / loyalistes</b> (surtout protestants, attachés au Royaume-Uni) et les <b>nationalistes / républicains</b> (surtout catholiques, favorables à une Irlande unie). Plus de 3 500 personnes sont tuées.",
    [("1968", "marches pour les droits civiques des catholiques"), ("1969", "l'armée britannique est déployée"), ("1971", "internement sans procès"),
     ("30 janv. 1972", "Bloody Sunday à Derry : 13 civils tués, un 14e meurt plus tard"), ("1976 – 1981", "blanket protest, dirty protest et grèves de la faim dans la prison du Maze"),
     ("5 mai 1981", "mort de Bobby Sands après 66 jours de grève de la faim"), ("10 avril 1998", "accord du Vendredi saint (Good Friday Agreement)"),
     ("2010", "rapport Saville : les tirs étaient injustifiés ; excuses du Premier ministre")],
    "a march, civil rights, a paratrooper, internment, a hunger strike, a cell, a ceasefire, power-sharing"),
  {D: doc("Document 1 — Bloody Sunday, Derry, 30 January 1972", [
    "In the 1960s, many Catholics in Northern Ireland suffered discrimination in housing, jobs and elections. Inspired by Martin Luther King in America, they organised civil rights marches. Violence grew, and in 1969 the British army was sent to Northern Ireland.",
    "In August 1971, the government introduced internment: suspects could be put in prison without a trial. Almost all of them were Catholics, and many people were angry.",
    "On Sunday 30 January 1972, about 15,000 people marched peacefully against internment in Derry. British paratroopers opened fire on the crowd. Thirteen unarmed civilians were killed, and another man died a few months later. Several victims were shot in the back while they were running away or helping the wounded.",
    "A first inquiry in 1972 mostly cleared the soldiers. The families fought for the truth for almost forty years. In 2010, a new inquiry, the Saville Report, concluded that the killings were \"unjustified and unjustifiable\" and that the victims were innocent. Prime Minister David Cameron apologised in Parliament.",
    "Bloody Sunday was a turning point: after that day, many young nationalists joined the IRA, and 1972 became the deadliest year of the Troubles."]),
   D2: doc("Document 2 — Protests in the H-Blocks", [
    "Until 1976, prisoners from paramilitary groups had a \"special category status\": they were treated almost like prisoners of war. That year, the British government ended this status. From then on, they were treated as ordinary criminals.",
    "In the H-Blocks of the Maze Prison, republican prisoners refused to wear prison uniforms. They wrapped themselves in blankets: it was the \"blanket protest\". In 1978, they started the \"dirty protest\": they refused to leave their cells to wash and covered the walls of their cells with their own excrement. Women prisoners in Armagh joined a similar protest.",
    "In 1981, the prisoners started a hunger strike. Their leader, Bobby Sands, was elected Member of Parliament while he was in prison. Prime Minister Margaret Thatcher refused to give in: for her, \"crime is crime\" and the prisoners were not political prisoners.",
    "Bobby Sands died on 5 May 1981, after 66 days without food. Nine other hunger strikers died in the following months. Their deaths shocked the world, and the republican movement started to take part in elections."]),
   D3: doc("Document 3 — The road to peace", [
    "After years of violence, secret talks began. In 1994, the IRA declared a ceasefire, and the loyalist groups did the same.",
    "On 10 April 1998, the Good Friday Agreement was signed. Northern Ireland would stay in the UK as long as a majority of its people wanted it, and unionists and nationalists would share power in a new government.",
    "People in both parts of Ireland approved the agreement in a referendum. Peace is still fragile: in Belfast, some \"peace walls\" still separate Catholic and Protestant neighbourhoods."])},
  [TF(D, "In the 1960s, many Catholics suffered discrimination.", True, "« in housing, jobs and elections »."),
   TF(D, "Internment meant prison without a trial.", True, "« without a trial »."),
   TF(D, "The march of 30 January 1972 was violent.", False, "« marched peacefully »."),
   TF(D, "The victims of Bloody Sunday were armed.", False, "« unarmed civilians »."),
   TF(D, "The first inquiry, in 1972, mostly cleared the soldiers.", True, "« mostly cleared the soldiers »."),
   TF(D2, "In 1976, prisoners lost their special category status.", True, "« That year, the British government ended this status »."),
   TF(D2, "The blanket protest started because prisoners refused to wear uniforms.", True, "« refused to wear prison uniforms »."),
   TF(D2, "Margaret Thatcher accepted the prisoners' demands.", False, "« refused to give in »."),
   TF(D2, "Bobby Sands was elected MP while he was in prison.", True, "« elected Member of Parliament while he was in prison »."),
   TF(D3, "The Good Friday Agreement was signed in 1998.", True, "10 avril 1998.")],
  [Q(D, "Who inspired the civil rights marches?", ["Martin Luther King.", "Margaret Thatcher.", "The Queen."]),
   Q(D, "What did the Saville Report conclude in 2010?", ["The killings were unjustified and the victims innocent.", "The soldiers were attacked first.", "The march was illegal."]),
   Q(D, "Why was Bloody Sunday a turning point?", ["Many young nationalists joined the IRA afterwards.", "The Troubles ended immediately.", "The army left Northern Ireland."]),
   Q(D2, "What was the \"dirty protest\"?", ["Prisoners refused to wash and dirtied the walls of their cells.", "Prisoners refused to eat.", "Prisoners escaped from the Maze."]),
   Q(D2, "Why did the prisoners protest?", ["They wanted to be recognised as political prisoners.", "They wanted better food.", "They wanted to be sent to England."]),
   Q(D3, "What does the Good Friday Agreement say?", ["Northern Ireland stays in the UK while the majority wants it, with shared power.", "Northern Ireland joins the Republic of Ireland.", "The British army takes control of the government."]),
   Q(D3, "What are \"peace walls\"?", ["Walls separating Catholic and Protestant neighbourhoods.", "Monuments to the victims.", "The walls of the Maze Prison."])],
  [DT(D, "Où a eu lieu Bloody Sunday ?", ["Derry", "Belfast", "Dublin", "London"]),
   DT(D, "En quelle année a eu lieu Bloody Sunday ?", ["1972", "1981", "1998", "1969"]),
   DT(D2, "Qui menait la grève de la faim de 1981 ?", ["Bobby Sands", "Gerry Adams", "Martin McGuinness", "Ian Paisley"]),
   DT(D2, "Combien de grévistes de la faim sont morts en 1981 ?", ["Dix", "Un", "Treize", "Cent"]),
   DT(D3, "Quel accord met fin aux Troubles ?", ["Good Friday Agreement", "Anglo-Irish Treaty", "Act of Union", "Windsor Framework"]),
   DT(D, "Comment appelle-t-on les partisans du maintien dans le Royaume-Uni ?", ["Unionists", "Republicans", "Nationalists", "Separatists"])],
  [W(D, "Trouve le mot qui veut dire « sans armes ».", "unarmed"), W(D, "Trouve le mot qui veut dire « une enquête officielle ».", ["inquiry", "an inquiry"]),
   W(D2, "Trouve l'expression qui veut dire « grève de la faim ».", ["hunger strike", "a hunger strike"]), W(D3, "Trouve le mot qui veut dire « cessez-le-feu ».", ["ceasefire", "a ceasefire"])])

# ════════════════════ ÉTATS-UNIS ════════════════════
D = "usa"
culture("cu_usa.html", "Culture : The United States", 'The United <span>States</span>',
  "Culture · 50 États, une nation", ("#bfdbfe", "#1e40af"),
  reperes("Les <b>États-Unis d'Amérique</b> (the USA) sont une république fédérale de 50 États. La capitale est <b>Washington, D.C.</b>, mais la plus grande ville est <b>New York</b>.",
    [("4 juillet 1776", "Déclaration d'indépendance : Independence Day"), ("1787", "rédaction de la Constitution"), ("1959", "l'Alaska et Hawaï deviennent les 49e et 50e États")],
    "a state, the federal government, the Stars and Stripes, a nation, the West, the Midwest"),
  {D: doc("Welcome to the USA!", [
    "The United States of America is a huge country in North America, between Canada and Mexico. It is made of 50 states. Forty-eight of them are next to each other. The other two, Alaska and Hawaii, are far away: Alaska is next to Canada and Hawaii is in the Pacific Ocean.",
    "The capital is Washington, D.C., where the President lives, in the White House. But the biggest city is New York, with more than eight million people. Other famous cities are Los Angeles, Chicago and Miami.",
    "More than 330 million people live in the USA. English is the main language, but more than 40 million people speak Spanish at home. Americans have origins all over the world: that's why the USA is often called \"a nation of immigrants\". The first inhabitants were the Native Americans.",
    "The American flag is called the Stars and Stripes. It has 50 stars, one for each state, and 13 stripes for the 13 original colonies. These colonies declared their independence from Britain on 4 July 1776. That's why the 4th of July, Independence Day, is the national holiday, with parades and fireworks.",
    "The national symbol is the bald eagle. The money is the dollar ($). And on the dollar bills, you can read the national motto: \"In God We Trust\"."])},
  [TF(D, "The USA has 50 states.", True, "« It is made of 50 states »."),
   TF(D, "Hawaii is next to Canada.", False, "C'est l'Alaska. Hawaii is in the Pacific Ocean."),
   TF(D, "The capital of the USA is New York.", False, "Washington, D.C."),
   TF(D, "The President lives in the White House.", True, "« where the President lives, in the White House »."),
   TF(D, "Many people speak Spanish at home.", True, "« more than 40 million people »."),
   TF(D, "The flag has 13 stars.", False, "50 stars, 13 stripes."),
   TF(D, "Independence Day is on 4 July.", True, "« the 4th of July, Independence Day »." )],
  [Q(D, "Why is the USA called \"a nation of immigrants\"?", ["Because Americans have origins all over the world.", "Because many Americans live abroad.", "Because the President was an immigrant."]),
   Q(D, "Who were the first inhabitants?", ["The Native Americans.", "The British.", "The Spanish."]),
   Q(D, "What do the 13 stripes represent?", ["The 13 original colonies.", "The 13 biggest cities.", "The 13 presidents."]),
   Q(D, "What is the national symbol?", ["The bald eagle.", "The lion.", "The red dragon."]),
   Q(D, "What is the national motto?", ["In God We Trust.", "God Save the King.", "Liberty, Equality, Fraternity."])],
  [DT(D, "Quels sont les deux pays voisins des USA ?", ["Le Canada et le Mexique", "Le Canada et Cuba", "Le Mexique et le Brésil", "Le Groenland et le Canada"]),
   DT(D, "En quelle année les colonies déclarent-elles leur indépendance ?", ["1776", "1492", "1865", "1620"]),
   DT(D, "Comment s'appelle le drapeau américain ?", ["The Stars and Stripes", "The Union Jack", "Old Glory Jack", "The Star-Spangled Flag"]),
   DT(D, "Quels sont les deux derniers États (1959) ?", ["L'Alaska et Hawaï", "Le Texas et la Californie", "La Floride et l'Alaska", "New York et Hawaï"])],
  [W(D, "Trouve le mot qui veut dire « rayures, bandes ».", "stripes"), W(D, "Trouve le mot qui veut dire « feux d'artifice ».", "fireworks"),
   W(D, "Trouve le mot qui veut dire « habitants ».", "inhabitants"), W(D, "Trouve le mot qui veut dire « devise » (phrase).", "motto")])

D = "usg"
culture("cu_institutions_us.html", "Culture : How the USA is governed", 'How the USA <span>is governed</span>',
  "Culture · Constitution, Congrès, Président, Cour suprême", ("#fecdd3", "#be123c"),
  reperes("La <b>Constitution</b> de 1787 sépare le pouvoir en trois branches qui se contrôlent mutuellement : ce sont les <b>checks and balances</b>.",
    [("Legislative branch", "le Congrès : Senate (100 sénateurs) + House of Representatives (435 représentants)"), ("Executive branch", "le Président, élu pour 4 ans, deux mandats au maximum"),
     ("Judicial branch", "la Cour suprême : 9 juges nommés à vie"), ("1791", "Bill of Rights : les 10 premiers amendements")],
    "the Constitution, an amendment, Congress, a veto, the Supreme Court, the Electoral College"),
  {D: doc("Checks and balances", [
    "The American Constitution was written in 1787. It is the oldest written national constitution still in use. Its first words are famous: \"We the People\". In 1791, ten amendments were added to protect individual rights, like freedom of speech and freedom of religion: this is the Bill of Rights.",
    "The Constitution divides power into three branches. The legislative branch, Congress, makes the laws. It has two houses: the Senate, with two senators for each state, and the House of Representatives, where big states have more representatives than small ones.",
    "The executive branch is led by the President, who applies the laws and commands the army. The President is elected for four years and can serve only two terms. The President can veto a law, but Congress can override the veto with a two-thirds majority.",
    "The judicial branch is led by the Supreme Court. Its nine judges are chosen by the President, approved by the Senate, and they serve for life. They decide if laws respect the Constitution. Their decisions can change American society, on subjects like civil rights, abortion or guns.",
    "Each branch can limit the power of the others: this system is called \"checks and balances\". The goal of the Founding Fathers was to avoid a king or a dictator.",
    "Presidential elections take place every four years, in November. Citizens don't vote directly for the President: they choose electors in each state. A candidate needs 270 of the 538 votes of the Electoral College to win. Two parties dominate politics: the Democrats, whose symbol is a donkey, and the Republicans, whose symbol is an elephant."])},
  [TF(D, "The American Constitution was written in 1787.", True, "« written in 1787 »."),
   TF(D, "The Bill of Rights protects individual rights.", True, "« freedom of speech and freedom of religion »."),
   TF(D, "Each state has two senators.", True, "« two senators for each state »."),
   TF(D, "A President can serve three terms.", False, "« only two terms »."),
   TF(D, "Supreme Court judges are elected by citizens.", False, "Nommés par le Président, approuvés par le Sénat."),
   TF(D, "Citizens vote directly for the President.", False, "« they choose electors in each state »."),
   TF(D, "The Republican symbol is a donkey.", False, "Republicans = elephant ; Democrats = donkey." )],
  [Q(D, "What does Congress do?", ["It makes the laws.", "It commands the army.", "It chooses the judges alone."]),
   Q(D, "What can Congress do against a presidential veto?", ["Override it with a two-thirds majority.", "Nothing.", "Ask the King."]),
   Q(D, "What does the Supreme Court decide?", ["If laws respect the Constitution.", "The date of elections.", "The President's salary."]),
   Q(D, "Why did the Founding Fathers create checks and balances?", ["To avoid a king or a dictator.", "To make laws faster.", "To give more power to the President."]),
   Q(D, "How many electoral votes does a candidate need to win?", ["270.", "538.", "100."])],
  [DT(D, "Quels sont les premiers mots de la Constitution ?", ["We the People", "In God We Trust", "I have a dream", "Liberty or death"]),
   DT(D, "Combien de juges à la Cour suprême ?", ["9", "12", "50", "100"]),
   DT(D, "Comment s'appellent les 10 premiers amendements ?", ["The Bill of Rights", "The Declaration of Independence", "The Magna Carta", "The New Deal"]),
   DT(D, "Combien de sénateurs au total ?", ["100", "50", "435", "538"]),
   DT(D, "Quelle est la durée du mandat présidentiel ?", ["4 ans", "5 ans", "6 ans", "7 ans"])],
  [W(D, "Trouve le mot qui veut dire « liberté d'expression ».", ["freedom of speech"]), W(D, "Trouve le mot qui veut dire « mandats ».", "terms"),
   W(D, "Trouve l'expression qui veut dire « les Pères fondateurs ».", ["the founding fathers", "founding fathers"]), W(D, "Trouve le mot qui veut dire « citoyens ».", "citizens")])

D = "md"
culture("cu_manifest_destiny.html", "Culture : Manifest Destiny", 'Manifest <span>Destiny</span>',
  "Culture · la conquête de l'Ouest et ses victimes", ("#fcd34d", "#a16207"),
  reperes("En 1845, le journaliste John O'Sullivan parle de la « destinée manifeste » des États-Unis : s'étendre d'un océan à l'autre. L'idée justifie l'expansion vers l'Ouest… au détriment des Amérindiens et du Mexique.",
    [("1803", "achat de la Louisiane à la France (Napoléon)"), ("1830", "Indian Removal Act"), ("1838 – 1839", "Trail of Tears : déportation des Cherokees"),
     ("1845", "expression « Manifest Destiny » ; annexion du Texas"), ("1846 – 1848", "guerre contre le Mexique : la Californie devient américaine"),
     ("1848 – 1849", "ruée vers l'or en Californie"), ("1869", "premier chemin de fer transcontinental"), ("1890", "massacre de Wounded Knee ; fin de la Frontière")],
    "the frontier, a settler, a pioneer, westward expansion, a reservation, to annex"),
  {D: doc("From sea to shining sea", [
    "In 1803, the young United States bought Louisiana from France. This huge territory, between the Mississippi River and the Rocky Mountains, doubled the size of the country. Soon, explorers like Lewis and Clark travelled across it to the Pacific Ocean.",
    "In 1845, a journalist, John O'Sullivan, wrote that it was the \"manifest destiny\" of the United States to spread over the whole continent. For many Americans, God had given them the mission to bring democracy and progress to the West. The famous painting American Progress (1872) shows a giant woman flying westward, carrying a telegraph wire, while Native Americans and wild animals run away.",
    "The same year, Texas joined the United States. Then, after a war against Mexico (1846-1848), the USA took California and a huge part of the Southwest. When gold was discovered in California in 1848, thousands of people rushed west: it was the Gold Rush.",
    "Pioneers travelled in covered wagons on long trails, like the Oregon Trail. Later, the Homestead Act (1862) gave free land to settlers, and the first transcontinental railroad was finished in 1869.",
    "But for Native Americans, Manifest Destiny was a tragedy. With the Indian Removal Act of 1830, entire nations were forced to leave their lands. During the \"Trail of Tears\", in 1838 and 1839, thousands of Cherokees died on the way. Later, the buffalo were almost exterminated, wars destroyed many tribes, and the survivors were moved to reservations.",
    "In 1890, the army killed hundreds of Lakota men, women and children at Wounded Knee. The same year, the government announced that the frontier was closed. Today, historians see Manifest Destiny both as the birth of a continental nation and as a justification for conquest."])},
  [TF(D, "The USA bought Louisiana from Spain.", False, "« from France »."),
   TF(D, "The Louisiana Purchase doubled the size of the country.", True, "« doubled the size of the country »."),
   TF(D, "John O'Sullivan was a president.", False, "« a journalist »."),
   TF(D, "Many Americans thought God gave them a mission.", True, "« God had given them the mission »."),
   TF(D, "California became American after a war against Mexico.", True, "1846-1848."),
   TF(D, "The Homestead Act gave free land to settlers.", True, "« gave free land to settlers »."),
   TF(D, "Native Americans benefited from Manifest Destiny.", False, "« for Native Americans, Manifest Destiny was a tragedy »." )],
  [Q(D, "What does \"manifest destiny\" mean?", ["The idea that the USA was destined to spread over the whole continent.", "A treaty with Mexico.", "The name of a railroad."]),
   Q(D, "What does the painting American Progress show?", ["A woman flying westward while Native Americans run away.", "A battle against Mexico.", "The Gold Rush in San Francisco."]),
   Q(D, "What caused the Gold Rush?", ["Gold was discovered in California in 1848.", "The Homestead Act.", "The war against France."]),
   Q(D, "What was the Trail of Tears?", ["The forced removal of the Cherokees, during which thousands died.", "A famous road to Oregon.", "A song by pioneers."]),
   Q(D, "How do historians see Manifest Destiny today?", ["Both as the birth of a nation and a justification for conquest.", "Only as a great success.", "As a myth that never existed."])],
  [DT(D, "En quelle année l'expression « Manifest Destiny » apparaît-elle ?", ["1845", "1776", "1803", "1890"]),
   DT(D, "Quel peuple subit la « Piste des larmes » ?", ["Les Cherokees", "Les Lakotas", "Les Apaches", "Les Inuits"]),
   DT(D, "Quel massacre marque symboliquement la fin de la Frontière (1890) ?", ["Wounded Knee", "Little Bighorn", "Alamo", "Gettysburg"]),
   DT(D, "Quand le premier chemin de fer transcontinental est-il terminé ?", ["1869", "1803", "1848", "1912"]),
   DT(D, "Qui ont exploré la Louisiane jusqu'au Pacifique ?", ["Lewis et Clark", "Bonnie et Clyde", "Washington et Jefferson", "Davy Crockett et Daniel Boone"])],
  [W(D, "Trouve le mot qui veut dire « vers l'ouest ».", "westward"), W(D, "Trouve le mot qui veut dire « colons ».", "settlers"),
   W(D, "Trouve l'expression qui veut dire « ruée vers l'or ».", ["gold rush", "the gold rush"]), W(D, "Trouve le mot qui veut dire « réserves (indiennes) ».", "reservations")])

D = "red"
culture("cu_red_scare.html", "Culture : The Red Scare", 'The Red <span>Scare</span>',
  "Culture · la peur du communisme et le maccarthysme", ("#fecaca", "#991b1b"),
  reperes("La <b>Red Scare</b> (« peur rouge ») désigne deux périodes de peur du communisme aux États-Unis. La seconde, pendant la guerre froide, est appelée <b>McCarthyism</b> : une véritable « chasse aux sorcières ».",
    [("1919 – 1920", "First Red Scare : Palmer Raids, arrestations et expulsions"), ("1947", "la commission HUAC enquête sur Hollywood : les « Hollywood Ten »"),
     ("1950", "le sénateur Joseph McCarthy affirme avoir une liste de communistes"), ("1953", "exécution d'Ethel et Julius Rosenberg ; Arthur Miller écrit <i>The Crucible</i>"),
     ("1954", "auditions télévisées Army-McCarthy ; le Sénat condamne McCarthy")],
    "a witch hunt, a blacklist, to accuse, a spy, loyalty, the Cold War, a hearing"),
  {D: doc("Are you now or have you ever been…?", [
    "After the Russian Revolution of 1917, many Americans feared that communism would spread to the United States. In 1919 and 1920, during the First Red Scare, the government arrested thousands of suspected radicals in the \"Palmer Raids\", and hundreds of foreigners were deported.",
    "The Second Red Scare began after 1945, at the beginning of the Cold War. The Soviet Union became the great enemy, and it tested its first atomic bomb in 1949. Many Americans were convinced that communist spies were hiding everywhere.",
    "A committee of Congress, the House Un-American Activities Committee (HUAC), questioned people about their political ideas. The famous question was: \"Are you now or have you ever been a member of the Communist Party?\" In 1947, ten Hollywood writers and directors refused to answer. They went to prison, and hundreds of artists were put on a blacklist: they couldn't find work anymore.",
    "In 1950, Senator Joseph McCarthy declared that he had a list of communists working in the government. He never proved it, but he accused many people without evidence. This practice of accusing people without proof is now called McCarthyism.",
    "In 1953, Ethel and Julius Rosenberg were executed for giving atomic secrets to the Soviet Union. The same year, the writer Arthur Miller published The Crucible, a play about the Salem witch trials of 1692. Everybody understood that it was really about McCarthyism: a modern \"witch hunt\".",
    "In 1954, McCarthy attacked the army in hearings shown on television. Millions of Americans saw his aggressive methods, and his popularity collapsed. The Senate condemned him the same year, and the Red Scare slowly came to an end."])},
  [TF(D, "The First Red Scare followed the Russian Revolution.", True, "« After the Russian Revolution of 1917 »."),
   TF(D, "The Soviet Union tested its first atomic bomb in 1949.", True, "« in 1949 »."),
   TF(D, "HUAC was a committee of Congress.", True, "« A committee of Congress »."),
   TF(D, "The Hollywood Ten answered all the questions.", False, "« refused to answer »."),
   TF(D, "McCarthy proved that his list was true.", False, "« He never proved it »."),
   TF(D, "The Crucible is about the Salem witch trials.", True, "« a play about the Salem witch trials of 1692 »."),
   TF(D, "Television made McCarthy more popular.", False, "« his popularity collapsed »." )],
  [Q(D, "What were the Palmer Raids?", ["Arrests of thousands of suspected radicals in 1919-1920.", "Attacks by Soviet spies.", "Hollywood films about communists."]),
   Q(D, "What happened to people on the blacklist?", ["They couldn't find work anymore.", "They became famous.", "They were sent to the Soviet Union."]),
   Q(D, "What is McCarthyism?", ["Accusing people without proof.", "A type of communism.", "A Hollywood film style."]),
   Q(D, "Why was The Crucible important?", ["It compared McCarthyism to a witch hunt.", "It defended McCarthy.", "It was written by a Soviet spy."]),
   Q(D, "Why did McCarthy's popularity collapse?", ["Millions saw his aggressive methods on television.", "He became a communist.", "He lost an election in Hollywood."])],
  [DT(D, "Qui est l'auteur de The Crucible ?", ["Arthur Miller", "John Steinbeck", "Ernest Hemingway", "Tennessee Williams"]),
   DT(D, "Quel couple est exécuté pour espionnage en 1953 ?", ["Ethel et Julius Rosenberg", "Bonnie et Clyde", "Sacco et Vanzetti", "John et Jackie Kennedy"]),
   DT(D, "Quand McCarthy lance-t-il ses accusations ?", ["1950", "1919", "1962", "1945"]),
   DT(D, "Que signifie HUAC ?", ["House Un-American Activities Committee", "Hollywood United Actors Club", "House of United American Citizens", "Higher Union of Anti-Communists"])],
  [W(D, "Trouve l'expression qui veut dire « chasse aux sorcières ».", ["witch hunt", "a witch hunt"]), W(D, "Trouve le mot qui veut dire « liste noire ».", ["blacklist", "a blacklist"]),
   W(D, "Trouve le mot qui veut dire « preuve(s) ».", ["evidence", "proof"]), W(D, "Trouve le mot qui veut dire « espions ».", "spies")])

D = "wg"
culture("cu_watergate.html", "Culture : The Watergate scandal", 'The Watergate <span>scandal</span>',
  "Culture · le scandale qui a fait tomber un président", ("#ddd6fe", "#6d28d9"),
  reperes("Le <b>Watergate</b> est le nom d'un immeuble de Washington. Le scandale pousse Richard Nixon à devenir le seul président américain à démissionner. Depuis, le suffixe <b>-gate</b> désigne un scandale.",
    [("17 juin 1972", "cambriolage du siège du Parti démocrate au Watergate"), ("nov. 1972", "Nixon réélu très largement"), ("1973", "auditions au Sénat ; découverte des enregistrements secrets"),
     ("20 oct. 1973", "« Saturday Night Massacre » : renvoi du procureur spécial"), ("24 juil. 1974", "la Cour suprême oblige Nixon à livrer les bandes"),
     ("9 août 1974", "démission de Nixon ; Gerald Ford devient président"), ("8 sept. 1974", "Ford gracie Nixon")],
    "a break-in, a cover-up, a tape, impeachment, to resign, a pardon, a whistleblower, investigative journalism"),
  {D: doc("Follow the money", [
    "On 17 June 1972, five men were arrested inside the headquarters of the Democratic Party, in the Watergate building in Washington. They were trying to put microphones in the offices. The police soon discovered that they were linked to the committee for the re-election of President Richard Nixon, a Republican.",
    "At first, it seemed to be a small burglary. In November 1972, Nixon was re-elected in a landslide. But two young journalists from The Washington Post, Bob Woodward and Carl Bernstein, continued to investigate. A secret source, known as \"Deep Throat\", helped them. In 2005, we learned that he was Mark Felt, a senior official of the FBI.",
    "In 1973, a Senate committee organised hearings shown on television. A White House aide revealed that Nixon secretly recorded all the conversations in his office. Investigators wanted the tapes, but Nixon refused to give them. In October 1973, he even ordered the dismissal of the special prosecutor in charge of the investigation: this was called the \"Saturday Night Massacre\".",
    "\"I am not a crook,\" Nixon told the public. But in July 1974, the Supreme Court decided unanimously that he had to hand over the tapes. One of them, called the \"smoking gun\", proved that Nixon had tried to stop the FBI investigation just six days after the break-in. It was a cover-up.",
    "Congress was preparing to impeach him. On 9 August 1974, Richard Nixon resigned: he is still the only American president to have done so. His vice-president, Gerald Ford, became president and declared: \"Our long national nightmare is over.\" A month later, Ford pardoned Nixon, a controversial decision.",
    "Watergate showed the power of investigative journalism and of checks and balances. It also created a lasting mistrust of politicians. Since then, the suffix \"-gate\" is added to the names of scandals all over the world."])},
  [TF(D, "Five men were arrested in the Republican headquarters.", False, "Au siège du Parti démocrate."),
   TF(D, "Nixon lost the election of November 1972.", False, "« re-elected in a landslide »."),
   TF(D, "Woodward and Bernstein worked for The Washington Post.", True, "« two young journalists from The Washington Post »."),
   TF(D, "Deep Throat was a senior FBI official.", True, "Mark Felt."),
   TF(D, "Nixon recorded the conversations in his office.", True, "« secretly recorded all the conversations »."),
   TF(D, "The Supreme Court decided that Nixon could keep the tapes.", False, "« he had to hand over the tapes »."),
   TF(D, "Gerald Ford pardoned Nixon.", True, "« Ford pardoned Nixon »." )],
  [Q(D, "What were the five men doing in the Watergate building?", ["Trying to put microphones in the offices.", "Stealing money.", "Meeting the President."]),
   Q(D, "What was the \"smoking gun\" tape?", ["A recording proving that Nixon tried to stop the FBI investigation.", "A recording of the break-in.", "A gun found in the White House."]),
   Q(D, "What was the \"Saturday Night Massacre\"?", ["The dismissal of the special prosecutor.", "An attack on journalists.", "A violent riot in Washington."]),
   Q(D, "Why did Nixon resign?", ["Congress was preparing to impeach him.", "He was ill.", "He lost an election."]),
   Q(D, "What are the long-term consequences of Watergate?", ["Mistrust of politicians and the power of investigative journalism.", "The end of the Republican Party.", "A new constitution."])],
  [DT(D, "Quand a eu lieu le cambriolage du Watergate ?", ["17 juin 1972", "9 août 1974", "4 juillet 1976", "22 nov. 1963"]),
   DT(D, "Qui était « Deep Throat » ?", ["Mark Felt", "Bob Woodward", "Gerald Ford", "John Dean"]),
   DT(D, "Qui succède à Nixon ?", ["Gerald Ford", "Jimmy Carter", "Ronald Reagan", "Lyndon Johnson"]),
   DT(D, "Quel journal révèle l'affaire ?", ["The Washington Post", "The New York Times", "The Wall Street Journal", "The Guardian"]),
   DT(D, "Quelle célèbre phrase prononce Nixon ?", ["« I am not a crook »", "« Read my lips »", "« Yes we can »", "« Ich bin ein Berliner »"])],
  [W(D, "Trouve le mot qui veut dire « cambriolage » (dans le 2e paragraphe).", "burglary"), W(D, "Trouve le mot qui veut dire « démissionner » (au prétérit).", "resigned"),
   W(D, "Trouve le mot qui veut dire « étouffement d'une affaire ».", ["cover-up", "a cover-up"]), W(D, "Trouve le mot qui veut dire « méfiance ».", "mistrust")])

D = "tv"
culture("cu_televangelisme.html", "Culture : Televangelism", 'Tele<span>vangelism</span>',
  "Culture · religion, télévision et politique aux États-Unis", ("#fef08a", "#ca8a04"),
  reperes("Les États-Unis sont l'un des pays occidentaux les plus religieux. Les <b>télévangélistes</b> sont des prédicateurs protestants (souvent évangéliques) qui utilisent la radio, la télévision puis Internet. Certains ont joué un rôle politique important.",
    [("années 1920 – 1930", "premiers prédicateurs à la radio"), ("années 1950", "Billy Graham remplit les stades et passe à la télévision"), ("1960", "Pat Robertson fonde la chaîne CBN"),
     ("1979", "Jerry Falwell crée la Moral Majority : naissance de la droite religieuse"), ("1987 – 1988", "scandales Jim Bakker et Jimmy Swaggart"), ("années 2000", "mégachurches, Joel Osteen, prédication en ligne")],
    "a preacher, a sermon, a donation, a megachurch, the Religious Right, the prosperity gospel, born-again"),
  {D: doc("Preaching on the screen", [
    "Religion plays a bigger role in the United States than in most Western countries. Many Americans go to church every week, and many describe themselves as \"born-again\" Christians. Evangelical preachers quickly understood that radio and television could bring their message to millions of homes.",
    "The most famous of them was Billy Graham. From the 1950s, he organised huge \"crusades\" in stadiums, broadcast on television. He met almost every president from Truman to Obama and was respected even by many non-believers.",
    "In the 1960s and 1970s, new preachers created their own TV channels. Pat Robertson founded the Christian Broadcasting Network and its talk show, The 700 Club. Oral Roberts became famous for healing sessions on TV. Some of them preached the \"prosperity gospel\": the idea that God rewards faithful donors with money and success.",
    "Televangelists also became political. In 1979, Jerry Falwell created the Moral Majority, a movement against abortion and for \"traditional family values\". It helped Ronald Reagan win the 1980 election. Since then, the Religious Right has been an important part of the Republican coalition.",
    "In 1987 and 1988, scandals shocked the country. Jim Bakker, who had built a Christian theme park, was convicted of fraud: he had taken millions of dollars from his viewers. Jimmy Swaggart, another star preacher, confessed his sins in tears on live television.",
    "Today, televangelism continues on cable TV and on the Internet, with megachurches of thousands of members. Supporters say these preachers give hope and community to millions of people. Critics denounce their luxurious lifestyle, private jets and tax exemptions, and the mix of religion and politics."])},
  [TF(D, "Religion plays a small role in the USA.", False, "« a bigger role … than in most Western countries »."),
   TF(D, "Billy Graham organised crusades in stadiums.", True, "« huge \"crusades\" in stadiums »."),
   TF(D, "Billy Graham met only one president.", False, "« almost every president from Truman to Obama »."),
   TF(D, "Pat Robertson founded a TV channel.", True, "Christian Broadcasting Network."),
   TF(D, "The Moral Majority was against abortion.", True, "« a movement against abortion »."),
   TF(D, "Jim Bakker was convicted of fraud.", True, "« convicted of fraud »."),
   TF(D, "Everybody agrees that televangelists are positive.", False, "Supporters vs critics." )],
  [Q(D, "What is the \"prosperity gospel\"?", ["The idea that God rewards faithful donors with money and success.", "A gospel written by Billy Graham.", "A tax for churches."]),
   Q(D, "What did the Moral Majority do in 1980?", ["It helped Ronald Reagan win the election.", "It created a TV channel.", "It built a theme park."]),
   Q(D, "Why did Jimmy Swaggart cry on live television?", ["He confessed his sins.", "He lost an election.", "His channel was closed."]),
   Q(D, "What do critics denounce?", ["Luxurious lifestyles, tax exemptions and the mix of religion and politics.", "Their long sermons.", "Their use of the radio."]),
   Q(D, "According to supporters, what do these preachers bring?", ["Hope and community.", "Money and jobs.", "Political power to Democrats."])],
  [DT(D, "Qui fonde la Moral Majority en 1979 ?", ["Jerry Falwell", "Billy Graham", "Pat Robertson", "Oral Roberts"]),
   DT(D, "Quel prédicateur a rencontré presque tous les présidents ?", ["Billy Graham", "Jim Bakker", "Jimmy Swaggart", "Joel Osteen"]),
   DT(D, "Comment appelle-t-on le mouvement politique religieux conservateur ?", ["The Religious Right", "The New Deal", "The Tea Party only", "The Great Awakening Party"]),
   DT(D, "Quand éclatent les grands scandales ?", ["1987 – 1988", "1950 – 1951", "2008 – 2009", "1929 – 1930"])],
  [W(D, "Trouve le mot qui veut dire « prédicateurs ».", "preachers"), W(D, "Trouve le mot qui veut dire « diffusé » (à la télévision).", "broadcast"),
   W(D, "Trouve le mot qui veut dire « condamné » (en justice).", "convicted"), W(D, "Trouve le mot qui veut dire « téléspectateurs ».", "viewers")])

D, D2 = "gun", "sch"
culture("cu_armes_usa.html", "Culture : Guns in America", 'Guns <span>in America</span>',
  "Culture · le deuxième amendement et le débat sur les armes", ("#cbd5e1", "#334155"),
  reperes("Le <b>deuxième amendement</b> (1791) protège « le droit du peuple de détenir et de porter des armes ». Son interprétation divise profondément les Américains, surtout après les tueries dans des écoles.",
    [("1791", "Second Amendment, dans le Bill of Rights"), ("1871", "création de la NRA"), ("1994 – 2004", "interdiction fédérale des fusils d'assaut, non renouvelée"),
     ("1999", "Columbine High School, Colorado"), ("2008", "arrêt Heller : la Cour suprême reconnaît un droit individuel"), ("2012", "Sandy Hook, école primaire, Connecticut"),
     ("2018", "Parkland, Floride, puis la marche March for Our Lives"), ("2022", "Uvalde, Texas ; première grande loi fédérale depuis près de 30 ans")],
    "a gun, a firearm, the right to bear arms, a lobby, a background check, a mass shooting, gun control"),
  {D: doc("Document 1 — The right to bear arms", [
    "The Second Amendment to the Constitution, adopted in 1791, says: \"A well regulated Militia, being necessary to the security of a free State, the right of the people to keep and bear Arms, shall not be infringed.\"",
    "For some Americans, this sentence protects the right of every citizen to own guns, to defend themselves and their family. For others, it only protected the right of the states to have militias, at a time when the country had no professional army. In 2008, the Supreme Court decided that it protects an individual right to have a gun at home for self-defence.",
    "There are more guns than people in the United States. For millions of Americans, especially in rural areas, guns are part of the culture: they are used for hunting, sport or protection. The National Rifle Association (NRA), created in 1871, is one of the most powerful lobbies in the country.",
    "Gun control supporters want universal background checks, a minimum age to buy guns and a ban on assault weapons. Gun rights supporters answer that criminals don't respect laws, that the problem is mental health, and that \"a good guy with a gun\" can stop a bad guy."]),
   D2: doc("Document 2 — Schools under fire", [
    "On 20 April 1999, two students attacked Columbine High School, in Colorado. Thirteen people were killed. It was not the first school shooting, but it shocked the whole country, and many other attacks followed.",
    "In December 2012, a young man killed twenty children aged six and seven and six adults at Sandy Hook Elementary School, in Connecticut. But Congress did not pass any major gun law.",
    "In February 2018, seventeen people were killed at Marjory Stoneman Douglas High School, in Parkland, Florida. This time, the survivors, who were teenagers, started a national movement. On 24 March 2018, hundreds of thousands of young people took part in the \"March for Our Lives\" to demand stricter gun laws.",
    "In May 2022, nineteen children and two teachers were killed in a primary school in Uvalde, Texas. A few weeks later, Congress passed the first important federal gun law in almost thirty years, with more background checks for buyers under 21.",
    "Today, American pupils regularly practise \"lockdown drills\" to learn how to hide in case of an attack. According to official health statistics, since 2020 guns have been the leading cause of death for children and teenagers in the United States. Yet the country remains deeply divided on the answer."])},
  [TF(D, "The Second Amendment was adopted in 1791.", True, "« adopted in 1791 »."),
   TF(D, "All Americans interpret the Second Amendment in the same way.", False, "Deux lectures opposées."),
   TF(D, "In 2008, the Supreme Court recognised an individual right to have a gun at home.", True, "« an individual right to have a gun at home »."),
   TF(D, "There are fewer guns than people in the USA.", False, "« more guns than people »."),
   TF(D, "The NRA is a powerful lobby.", True, "« one of the most powerful lobbies »."),
   TF(D2, "After Sandy Hook, Congress passed a major gun law.", False, "« Congress did not pass any major gun law »."),
   TF(D2, "Teenage survivors of Parkland started a national movement.", True, "March for Our Lives."),
   TF(D2, "A federal gun law was passed in 2022.", True, "« the first important federal gun law in almost thirty years »." )],
  [Q(D, "What do gun rights supporters say?", ["Criminals don't respect laws and the problem is mental health.", "Guns should be banned.", "Only the army should have guns."]),
   Q(D, "What do gun control supporters want?", ["Background checks, a minimum age and a ban on assault weapons.", "More guns in schools.", "To abolish the Constitution."]),
   Q(D, "Why are guns part of the culture for many Americans?", ["They use them for hunting, sport or protection.", "Guns are free.", "It is compulsory to have one."]),
   Q(D2, "What was the \"March for Our Lives\"?", ["A demonstration of young people for stricter gun laws.", "A march organised by the NRA.", "A school sports event."]),
   Q(D2, "What are \"lockdown drills\"?", ["Exercises to learn how to hide in case of an attack.", "Fire exercises.", "Shooting lessons."])],
  [DT(D2, "Dans quel État se trouve Columbine High School ?", ["Colorado", "Texas", "Florida", "Connecticut"]),
   DT(D2, "Quel mouvement naît après Parkland ?", ["March for Our Lives", "Black Lives Matter", "Me Too", "Occupy Wall Street"]),
   DT(D, "Que signifie NRA ?", ["National Rifle Association", "National Republican Army", "New Rights of America", "National Rights Act"]),
   DT(D, "Quand l'interdiction des fusils d'assaut a-t-elle pris fin ?", ["2004", "1994", "2012", "1999"])],
  [W(D, "Trouve le mot qui veut dire « chasse ».", "hunting"), W(D, "Trouve l'expression qui veut dire « vérification des antécédents ».", ["background checks", "background check"]),
   W(D2, "Trouve le mot qui veut dire « survivants ».", "survivors"), W(D2, "Trouve le mot qui veut dire « plus strictes ».", "stricter")])

# ════════════════════ MONDE ANGLOPHONE ════════════════════
D = "eng"
culture("cu_anglophone.html", "Culture : English around the world", 'English <span>around the world</span>',
  "Culture · les pays anglophones", ("#99f6e4", "#0f766e"),
  reperes("L'anglais est langue officielle ou principale dans plus de 50 pays. Environ <b>1,5 milliard</b> de personnes le parlent, dont environ 380 millions comme langue maternelle.",
    [("Canada", "anglais et français ; capitale Ottawa"), ("Australia", "capitale Canberra"), ("New Zealand", "capitale Wellington ; langue maorie"), ("Ireland", "capitale Dublin ; anglais et irlandais"),
     ("India", "l'anglais est une langue officielle associée"), ("South Africa", "12 langues officielles"), ("Jamaica, Nigeria, Singapore…", "d'autres pays anglophones")],
    "a native speaker, an official language, a variety, an accent, a former colony"),
  {D: doc("One language, many voices", [
    "English is spoken on every continent. About 1.5 billion people speak it, but only about a quarter of them are native speakers. For most people, it is a second or a foreign language, used for business, science, travel and the Internet.",
    "Why is English so widespread? First, because of the British Empire, which brought the language to North America, Africa, Asia and Oceania. Then, in the 20th century, because of the power of the United States, its economy, its films and its music.",
    "In Canada, English and French are both official languages. In Ireland, people speak English, but Irish (Gaelic) is also an official language. In New Zealand, Maori is an official language too, and many places have a Maori name.",
    "In India, Hindi is the main official language, but English is used in government, universities and business. In Nigeria, the most populated country in Africa, English helps people from hundreds of different languages to communicate.",
    "Each country has its own variety of English, with its own accent and vocabulary. An Australian may say \"G'day, mate!\" to say hello, a South African may call a traffic light a \"robot\", and in Scotland a small child is a \"wee bairn\". But they can all understand each other!"])},
  [TF(D, "Most English speakers are native speakers.", False, "Seulement environ un quart."),
   TF(D, "The British Empire helped English spread.", True, "« because of the British Empire »."),
   TF(D, "Canada has two official languages.", True, "English and French."),
   TF(D, "In New Zealand, Maori is an official language.", True, "« Maori is an official language too »."),
   TF(D, "Hindi is the main official language of India.", True, "« Hindi is the main official language »."),
   TF(D, "In South Africa, a \"robot\" can be a traffic light.", True, "« call a traffic light a \"robot\" »." )],
  [Q(D, "Why did English spread in the 20th century?", ["Because of the power of the United States.", "Because of the French Revolution.", "Because it is easy."]),
   Q(D, "What is English used for in India?", ["Government, universities and business.", "Only for tourists.", "Nothing: it is forbidden."]),
   Q(D, "Why is English useful in Nigeria?", ["It helps people from hundreds of languages communicate.", "It is the only language there.", "Nigeria is in Europe."]),
   Q(D, "How does an Australian say hello?", ["G'day, mate!", "Wee bairn!", "Howdy, robot!"])],
  [DT(D, "Quelle est la capitale de l'Australie ?", ["Canberra", "Sydney", "Melbourne", "Wellington"]),
   DT(D, "Quelle est la capitale du Canada ?", ["Ottawa", "Toronto", "Montreal", "Vancouver"]),
   DT(D, "Quelle langue est officielle en Nouvelle-Zélande avec l'anglais ?", ["Le maori", "Le gaélique", "Le français", "Le hindi"]),
   DT(D, "Combien de personnes parlent anglais environ ?", ["1,5 milliard", "150 millions", "5 milliards", "380 000"])],
  [W(D, "Trouve l'expression qui veut dire « locuteurs natifs ».", ["native speakers", "native speaker"]), W(D, "Trouve le mot qui veut dire « répandu ».", "widespread"),
   W(D, "Trouve le mot qui veut dire « le plus peuplé ».", ["most populated", "the most populated"])])

print("ok")
