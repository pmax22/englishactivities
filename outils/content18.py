import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
exec(open(_EA_OUT+"/content_helpers.py", encoding="utf-8").read())
REPO = _EA_REPO
def jsf(name, **kw):
    s = open(f"{_EA_OUT}/{name}", encoding="utf-8").read().replace("%GENERIC%", ENGINE_GENERIC)
    for k, v in kw.items(): s = s.replace(f"%{k}%", json.dumps(v, ensure_ascii=False))
    return s

PCSS = '''<style>
  .dash-name { margin-bottom: 14px; } .dash-name input { width: 100%; font-size: 16px !important; padding: 12px 16px !important; }
  .dash-stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(70px, 1fr)); gap: 10px; margin-bottom: 14px; }
  .dash-stats div { background: var(--surface); border: 1px solid var(--border); border-radius: 14px; padding: 14px 10px; text-align: center; }
  .dash-stats b { display: block; font-family: 'Syne', sans-serif; font-size: 24px; color: var(--accent); }
  .dash-stats span { font-size: 12px; color: var(--muted); }
  .dash-lvl, .dash-help, .dash-empty, .lvl-help { font-size: 14px; color: var(--muted); margin: 8px 0 14px; line-height: 1.5; }
  .dash-lvl a, .dash-help a, .dash-empty a { color: var(--accent); }
  .dash-list { display: flex; flex-direction: column; gap: 6px; margin-bottom: 16px; text-align: left; }
  .dash-row { display: flex; align-items: center; gap: 10px; padding: 11px 14px; background: var(--surface); border: 1px solid var(--border); border-radius: 12px; text-decoration: none; color: var(--text); }
  .dash-row:hover { border-color: var(--accent); }
  .dr-t { flex: 1; font-weight: 500; font-size: 14px; min-width: 0; }
  .dr-m { font-size: 12px; color: var(--muted); white-space: nowrap; }
  .dr-s { font-family: 'Syne', sans-serif; font-weight: 700; color: var(--accent); min-width: 42px; text-align: right; }
  .dr-s.done { color: #4ade80; }
  .dash-count { display: inline-block; font-size: 12px; background: var(--surface2); border: 1px solid var(--border); border-radius: 999px; padding: 1px 9px; margin-left: 6px; color: var(--muted); }
  .dash-errs summary { cursor: pointer; color: var(--muted); font-size: 14px; margin-bottom: 8px; }
  .dash-actions { display: flex; gap: 10px; flex-wrap: wrap; margin: 16px 0 8px; }
  .dash-bilan { white-space: pre-wrap; font-size: 13px; color: var(--muted); word-break: break-all; margin-bottom: 18px; }
  #missions:empty { display: none; } #dash2 { margin-top: 18px; }
  @media (max-width: 560px) { .dash-stats div { padding: 10px 4px; } .dash-stats b { font-size: 20px; } .dash-stats span { font-size: 11px; } }
  .lvl-result { text-align: left; } .lvl-bars { display: flex; flex-direction: column; gap: 8px; margin: 6px 0 14px; }
  .lvl-bar { display: grid; grid-template-columns: 110px 1fr 44px; align-items: center; gap: 10px; font-size: 14px; }
  .lb-track { height: 10px; background: var(--surface2); border-radius: 99px; overflow: hidden; } .lb-fill { height: 100%; background: linear-gradient(90deg, var(--accent), var(--accent2)); }
  .lvl-reco { font-size: 18px; margin: 10px 0 4px; } .lvl-reco b { color: var(--accent); }
  .wr-step { background: var(--surface2); border: 1px solid var(--border); border-radius: 14px; padding: 12px 14px; margin-bottom: 10px; }
  .wr-step.ok { border-color: rgba(74,222,128,.5); }
  .wr-q { font-size: 14px; margin-bottom: 8px; display: flex; gap: 8px; align-items: baseline; }
  .wr-n { display: inline-flex; align-items: center; justify-content: center; min-width: 22px; height: 22px; border-radius: 50%; background: var(--accent); color: #111; font-size: 12px; font-weight: 700; flex-shrink: 0; }
  .wr-in { width: 100%; resize: vertical; font-size: 16px !important; padding: 10px 12px !important; font-family: inherit; text-align: left !important; }
  .wr-tools { display: flex; gap: 10px; align-items: center; margin-top: 6px; flex-wrap: wrap; }
  .wr-ex, .pf-pick button { background: transparent; border: 1px solid var(--border); color: var(--muted); border-radius: 999px; padding: 4px 10px; font-size: 12px; cursor: pointer; font-family: inherit; }
  .wr-msg { font-size: 13px; color: var(--muted); } .wr-step.ok .wr-msg { color: #4ade80; }
  .wr-model { margin-top: 8px; font-size: 14px; font-style: italic; color: var(--accent); }
  .wr-lex { margin-bottom: 12px; font-size: 14px; } .wr-lex summary { cursor: pointer; color: var(--muted); margin-bottom: 8px; }
  .wr-lex .pill { display: inline-block; margin: 0 4px 6px 0; }
  .wr-final { text-align: left; background: var(--surface2); border: 1px solid var(--border); border-radius: 14px; padding: 16px; font-size: 16px; line-height: 1.7; margin: 10px 0; color: var(--text); }
  .wr-final-tools { display: flex; gap: 10px; flex-wrap: wrap; justify-content: center; }
  .or-tools { display: flex; gap: 10px; flex-wrap: wrap; justify-content: center; align-items: center; margin: 16px 0 10px; }
  .or-tools audio { width: 100%; max-width: 360px; } .rec-on { background: #ef4444 !important; color: #fff !important; }
  .or-timer { font-family: 'Syne', sans-serif; font-weight: 700; color: var(--accent); }
  .or-cmp { font-size: 18px; margin: 8px 0; } .or-good { color: #4ade80; } .or-bad { color: #f87171; text-decoration: underline wavy; }
  .or-q { font-size: 24px !important; } .or-target { font-size: 26px !important; } .or-help { font-style: italic; color: var(--accent); }
  .pf-card { margin-bottom: 16px; text-align: left; } .pf-l { display: block; font-size: 13px; color: var(--muted); margin: 10px 0 6px; }
  .pf-in, .pf-ta, .pf-search { width: 100%; font-size: 15px !important; padding: 10px 14px !important; text-align: left !important; font-family: inherit; }
  .pf-filters { display: flex; gap: 8px; margin: 10px 0; flex-wrap: wrap; }
  .pf-filters select { background: var(--surface2); color: var(--text); border: 1px solid var(--border); border-radius: 10px; padding: 8px 10px; font-family: inherit; }
  .pf-list { max-height: 420px; overflow-y: auto; display: flex; flex-direction: column; gap: 4px; }
  .pf-row { display: flex; align-items: center; gap: 10px; padding: 8px 10px; border-radius: 10px; cursor: pointer; }
  .pf-row:hover { background: var(--surface2); } .pf-row input { accent-color: var(--accent); width: 18px; height: 18px; }
  .pf-row .lvl { font-size: 11px; padding: 2px 8px; border-radius: 99px; border: 1px solid var(--border); color: var(--muted); white-space: nowrap; }
  .pf-sel { display: flex; flex-direction: column; gap: 6px; } .pf-pick { display: flex; align-items: center; gap: 8px; font-size: 14px; }
  .dv-done { border-color: rgba(74,222,128,.4); } .dv-done .wr-n { background: #4ade80; }
  .dg-group { margin-top: 18px; }
  .dg-item { background: var(--surface2); border: 1px solid var(--border); border-left: 4px solid var(--border); border-radius: 12px; padding: 10px 14px; margin-bottom: 8px; }
  .dg-top { display: flex; align-items: baseline; gap: 8px; margin-bottom: 6px; } .dg-name { flex: 1; font-weight: 600; font-size: 14px; }
  .dg-lv { font-size: 11px; color: var(--muted); } .dg-pct { font-family: 'Syne', sans-serif; font-weight: 800; font-size: 16px; }
  .dg-item .lb-track { height: 7px; } .dg-links { display: flex; flex-wrap: wrap; gap: 6px 14px; margin-top: 8px; font-size: 13px; }
  .dg-links a { color: var(--accent); text-decoration: none; } .dg-links a:hover { text-decoration: underline; }
  .dg-tw { border-left-color: #f87171; } .dg-tw .dg-pct { color: #f87171; } .dg-tw .lb-fill { background: #f87171; }
  .dg-fr { border-left-color: #fbbf24; } .dg-fr .dg-pct { color: #fbbf24; } .dg-fr .lb-fill { background: #fbbf24; }
  .dg-ac { border-left-color: #4ade80; } .dg-ac .dg-pct { color: #4ade80; } .dg-ac .lb-fill { background: #4ade80; }
  @media (max-width: 560px) { .dr-m { display: none; } .lvl-bar { grid-template-columns: 90px 1fr 40px; } }
</style>
'''
def finalize(file):
    p = f"{REPO}/{file}"; s = open(p, encoding="utf-8").read()
    s = s.replace('<script src="assets/ea.js"></script>', '<script src="assets/catalog.js"></script>\n<script src="assets/ea.js"></script>\n' + PCSS, 1)
    s = s.replace("<summary>Rappel de la leçon</summary>", "<summary>Mode d'emploi</summary>")
    open(p, "w", encoding="utf-8").write(s)

# ═════════════ MES PROGRÈS ═════════════
page("progres.html", "Mes progrès", "English Activities", 'Mes <span>progrès</span>',
     "Tes scores, tes erreurs à retravailler et ton bilan à envoyer au professeur.", ("#4ade80", "#16a34a"), None, "", jsf("progres.js"))
finalize("progres.html")

# ═════════════ TEST DE NIVEAU (diagnostic par notion) ═════════════
def N(id, name, l, files, qs): return {"id": id, "name": name, "l": l, "files": [f + ".html" for f in files.split()], "qs": [list(q) for q in qs]}
NONE = "(pas d'article)"
NOTIONS = [
 N("be", "Be et have got", 0, "be_have_play", [("My parents ____ teachers.", ["are", "is", "am", "be"], "they → are."),
    ("She ____ got blue eyes.", ["has", "have", "is", "does"], "she → has got."), ("____ you hungry?", ["Are", "Do", "Have", "Is"], "be : Are you…?")]),
 N("ps", "Présent simple", 0, "present_simple adverbes_frequence", [("My brother ____ in a bank.", ["works", "work", "working", "is work"], "3e personne : -s."),
    ("She ____ like fish.", ["doesn't", "don't", "isn't", "not"], "she → doesn't + BV."), ("Where ____ your father live?", ["does", "do", "is", "did"], "your father = he → does.")]),
 N("pc", "Présent be + -ing", 0, "present_continu", [("Be quiet! The baby ____.", ["is sleeping", "sleeps", "sleep", "is sleep"], "En ce moment : be + -ing."),
    ("What ____ you doing now?", ["are", "do", "is", "does"], "you → are + -ing."), ("Look! They ____ football in the rain.", ["are playing", "play", "plays", "playing"], "Look! → action en cours.")]),
 N("pro", "Pronoms et possessifs", 0, "pronoms_personnels possessifs", [("This is Tom. I like ____ very much.", ["him", "he", "his", "her"], "Complément masculin : him."),
    ("Emma and ____ sister are twins.", ["her", "his", "she", "their"], "Emma → her (possesseur féminin)."), ("Is this your bag? — Yes, it's ____.", ["mine", "my", "me", "I"], "Pronom possessif : mine.")]),
 N("art", "Articles et pluriels", 0, "articles pluriels", [("I've got two ____.", ["children", "childs", "child", "childrens"], "Pluriel irrégulier : children."),
    ("She is ____ engineer.", ["an", "a", "the", NONE], "Métier : a / an ; an devant un son voyelle."), ("I love ____ music.", [NONE, "the", "a", "an"], "Sens général : pas d'article.")]),
 N("there", "There is / prépositions", 0, "there_is prepositions heure_dates", [("There ____ a lot of people in the street.", ["are", "is", "have", "has"], "people est pluriel → there are."),
    ("My birthday is ____ May.", ["in", "on", "at", "of"], "in + mois."), ("See you ____ Monday!", ["on", "in", "at", "to"], "on + jour.")]),
 N("lex0", "Vocabulaire du quotidien", 0, "famille nourriture calendrier", [("Your mother's brother is your…", ["uncle", "cousin", "nephew", "grandfather"], "uncle = oncle."),
    ("Which word is a vegetable?", ["carrot", "pear", "cheese", "bread"], "carrot = carotte."), ("« Mercredi » in English is…", ["Wednesday", "Tuesday", "Thursday", "Saturday"], "Wednesday.")]),
 N("pret", "Prétérit", 1, "preterit verbe_regulier_irregulier", [("Last summer, we ____ to Spain.", ["went", "go", "goed", "have gone"], "Last summer → prétérit : go → went."),
    ("She ____ a new phone yesterday.", ["bought", "buyed", "buys", "has bought"], "buy → bought."), ("I ____ my keys this morning, so I was late.", ["lost", "lose", "losed", "have lose"], "lose → lost.")]),
 N("quest", "Poser des questions", 1, "questions_fermees questions_ouvertes questions_sujet", [("____ you see the match last night?", ["Did", "Do", "Were", "Have"], "Question au prétérit : Did + BV."),
    ("Where ____ they go last summer?", ["did", "do", "were", "have"], "Wh- + did + sujet + BV."), ("How much ____ this T-shirt cost?", ["does", "do", "is", "are"], "this T-shirt = it → does.")]),
 N("fut", "Le futur", 1, "futur", [("Look at those clouds! It ____ rain.", ["is going to", "will to", "goes to", "is raining to"], "Indice visible → be going to."),
    ("I think he ____ pass his exam.", ["will", "is going", "goes", "would to"], "Prédiction / opinion : will."), ("I've planned it: tomorrow I ____ my grandmother.", ["am going to visit", "visit", "will to visit", "visiting"], "Projet décidé → be going to.")]),
 N("comp", "Comparatif et superlatif", 1, "comparatif superlatif", [("This exercise is ____ than the first one.", ["easier", "more easy", "easyer", "the easiest"], "Adjectif court : -er (y → ier)."),
    ("She is ____ student in the class.", ["the best", "the better", "the goodest", "best"], "good → the best."), ("My bag is as heavy ____ yours.", ["as", "than", "that", "like"], "as … as.")]),
 N("mod", "Les modaux", 1, "modaux", [("You ____ smoke in the hospital. It's forbidden.", ["mustn't", "don't have to", "needn't", "can"], "Interdiction : mustn't."),
    ("____ I open the window, please?", ["Can", "Must", "Should to", "Do"], "Demander la permission : Can I…?"), ("You look tired. You ____ go to bed.", ["should", "must to", "ought", "can to"], "Conseil : should + BV.")]),
 N("qty", "Quantité (much, many, some, any)", 1, "denombrables quantifieurs", [("How ____ money have you got?", ["much", "many", "lot", "few"], "money est indénombrable → much."),
    ("There isn't ____ milk left.", ["any", "some", "no", "many"], "Phrase négative → any."), ("I need ____ information.", ["some", "an", "a few", "many"], "information est indénombrable.")]),
 N("pho", "Prononciation (-ed, lettres muettes)", 1, "phono_ed lettres_muettes", [("Dans « walked », -ed se prononce…", ["/t/", "/d/", "/ɪd/"], "Après /k/ (son sourd) → /t/."),
    ("Dans « wanted », -ed se prononce…", ["/ɪd/", "/t/", "/d/"], "Après t ou d → /ɪd/."), ("Quelle lettre est muette dans « listen » ?", ["t", "l", "s", "n"], "listen /ˈlɪsən/.")]),
 N("pro2", "Vocabulaire professionnel", 1, "cap_vente argent_shopping cap_ecrit_entretien", [("Where do customers pay in a shop?", ["at the till", "in the fitting room", "on the shelf", "in the warehouse"], "the till = la caisse."),
    ("« Un ticket de caisse » =", ["a receipt", "a recipe", "a ticket", "a bill"], "a recipe = une recette !"), ("« Un stage en entreprise » =", ["a work placement", "a stage", "a job centre", "a workshop"], "stage est un faux ami.")]),
 N("pp", "Present perfect, for / since / ago", 2, "present_perfect ago_for_since", [("I have never ____ to Japan.", ["been", "went", "go", "was"], "have + participe passé : been."),
    ("She has lived here ____ 2010.", ["since", "for", "ago", "during"], "Point de départ → since."), ("We met three years ____.", ["ago", "since", "for", "before"], "Prétérit + durée + ago.")]),
 N("pastp", "Past perfect et prétérit be + -ing", 2, "past_perfect preterit_continu", [("When the phone rang, I ____ a shower.", ["was having", "had", "have had", "am having"], "Action en cours dans le passé : was + -ing."),
    ("When we arrived, the train ____ already left.", ["had", "has", "was", "did"], "Antériorité dans le passé : had + PP."), ("He was tired because he ____ all day.", ["had worked", "has worked", "works", "was work"], "Cause antérieure : past perfect.")]),
 N("cond", "Le conditionnel (if)", 2, "conditionnel", [("If I ____ rich, I would travel the world.", ["were", "am", "will be", "would be"], "Type 2 : if + prétérit (were)."),
    ("If you heat ice, it ____.", ["melts", "would melt", "melted", "will melting"], "Vérité générale : if + présent, présent."), ("If she had studied, she ____ the exam.", ["would have passed", "would pass", "will pass", "passed"], "Type 3 : would have + PP.")]),
 N("pass", "Le passif", 2, "passif", [("This bridge ____ in 1890.", ["was built", "built", "is build", "has build"], "be + participe passé."),
    ("English ____ all over the world.", ["is spoken", "speaks", "is speaking", "spoken"], "Passif au présent : is spoken."), ("The letters ____ tomorrow.", ["will be sent", "will send", "are send", "will sent"], "Passif au futur : will be + PP.")]),
 N("ind", "Discours indirect", 2, "discours_indirect questions_indirectes", [("She said she ____ tired.", ["was", "is being", "be", "were been"], "Concordance des temps : is → was."),
    ("He asked me where I ____.", ["lived", "did I live", "do I live", "living"], "Question indirecte : pas d'inversion."), ("She told me ____ the door.", ["to close", "close", "closing", "that close"], "Ordre rapporté : tell + to + BV.")]),
 N("rel", "Pronoms relatifs", 2, "relatifs", [("The man ____ lives next door is a doctor.", ["who", "which", "whose", "what"], "Antécédent humain sujet : who."),
    ("This is the book ____ I told you about.", ["that", "who", "what", "whose"], "Antécédent non humain : that / which."), ("That's the girl ____ brother is in my class.", ["whose", "who's", "who", "which"], "Possession : whose.")]),
 N("conn", "Connecteurs logiques", 2, "connecteurs conjonctions_avancees", [("I was ill, ____ I stayed at home.", ["so", "but", "because", "although"], "Conséquence : so."),
    ("____ it was raining, we went out.", ["Although", "Because", "Despite", "So"], "Concession + proposition : although."), ("He is rich. ____, he isn't happy.", ["However", "Therefore", "Moreover", "Because"], "Opposition : however.")]),
 N("toing", "Verbe + to ou -ing", 2, "verbes_to_ing like_ing", [("I enjoy ____ in the sea.", ["swimming", "to swim", "swim", "swam"], "enjoy + -ing."),
    ("She decided ____ a new job.", ["to find", "finding", "find", "found"], "decide + to."), ("I'm looking forward to ____ you.", ["seeing", "see", "saw", "be seeing"], "look forward to + -ing (to est une préposition).")]),
 N("inv", "Inversion emphatique", 3, "inversion", [("Never ____ such a mess!", ["have I seen", "I have seen", "I saw", "did I saw"], "Never en tête → inversion."),
    ("Not only ____ late, but he also forgot his books.", ["was he", "he was", "he is", "did he was"], "Not only + inversion."), ("Had I known, I ____ earlier.", ["would have come", "would come", "will come", "had come"], "Had I known = If I had known.")]),
 N("wish", "Wish et conditionnels mixtes", 3, "wish conditionnels_mixtes", [("I wish I ____ more time now.", ["had", "have", "would have", "will have"], "Regret présent : wish + prétérit."),
    ("If I had taken the job, I ____ rich now.", ["would be", "would have been", "will be", "am"], "Mixte : passé → conséquence présente."), ("I wish you ____ making that noise!", ["would stop", "stop", "stopped", "will stop"], "Agacement : wish + would.")]),
 N("subj", "Subjonctif, it's time, I'd rather", 3, "subjonctif", [("It's high time we ____.", ["left", "leave", "will leave", "have left"], "It's high time + prétérit."),
    ("I'd rather you ____ tell anyone.", ["didn't", "don't", "won't", "not"], "I'd rather + sujet + prétérit."), ("The doctor insisted that he ____ in bed.", ["stay", "stays", "will stay", "is staying"], "Subjonctif : base verbale.")]),
 N("cleft", "Mise en relief et participiales", 3, "phrases_clivees participiales", [("____ I need is a holiday.", ["What", "That", "Which", "It"], "Pseudo-clivée : What I need is…"),
    ("____ by the noise, she woke up.", ["Disturbed", "Disturbing", "To disturb", "Disturb"], "Participiale passive."), ("It was Tom ____ broke the window.", ["who", "which", "what", "whose"], "Clivée : It was … who.")]),
]
import os
assert not [f for n in NOTIONS for f in n["files"] if not os.path.exists(f"{REPO}/{f}")], [f for n in NOTIONS for f in n["files"] if not os.path.exists(f"{REPO}/{f}")]
LES = '''      <p><b>Ce test fait le point sur ce que tu sais déjà.</b> Il ne compte pas, il n'est pas noté. Il porte sur <b>27 notions</b>, avec 3 questions par notion, de la plus simple à la plus difficile.</p>
      <p>Si tu ne connais pas la réponse, choisis <b>« Je ne sais pas »</b> plutôt que de répondre au hasard : le diagnostic sera plus juste. Si un niveau est trop difficile, le test s'arrête tout seul.</p>
      <p>À la fin, tu verras ton score en %, ton niveau conseillé et la liste de tes notions <b>✅ acquises</b>, <b>⚠️ fragiles</b> et <b>❌ à travailler</b>, avec les activités du site pour progresser. Ton diagnostic reste dans « Mes progrès ».</p>'''
page("test_niveau.html", "Par où commencer ? Test de niveau", "English Activities", 'Par où <span>commencer ?</span>',
     "Un test pour savoir ce qui est acquis et ce qui est à travailler.", ("#facc15", "#ca8a04"), LES, "", jsf("niveau.js", NOTIONS=NOTIONS))
finalize("test_niveau.html")

# ═════════════ ÉCRITURE GUIDÉE ═════════════
def ST(fr, start, ex, need=(), min=4): return {"fr": fr, "start": start, "ex": ex, "need": [list(n) for n in need], "min": min}
PAST = [r"\b(was|were|had|went|did|saw|ate|got|made|took|came|met|bought|played|visited|watched|stayed|walked|liked|loved|enjoyed|danced|cooked|helped|worked|listened|\w+ed)\b", "Utilise un verbe au prétérit (-ed ou irrégulier)."]
SUJETS_W = [
 {"id": "presente", "icon": "🙋", "group": "Novice", "title": "Me présenter", "desc": "Nom, âge, ville, famille, goûts : un petit portrait de toi.",
  "consigne": "Écris une phrase par étape. Le début est donné : complète-le.", "lex": ["I live in", "I have got", "brother / sister", "I like / I love", "I don't like", "my favourite", "because"],
  "steps": [ST("Dis comment tu t'appelles.", "My name is", "My name is Léa.", [[r"my name is \w+", "Donne ton prénom après « My name is »."]], 4),
            ST("Dis ton âge.", "I am", "I am fifteen years old.", [[r"\b(am|'m)\b", "Pour l'âge on utilise be : I am…"], [r"years old|\d+|teen|ty", "Indique ton âge."]], 3),
            ST("Dis où tu habites.", "I live in", "I live in Rennes, in Brittany.", [[r"live in", "Utilise « I live in »."]], 4),
            ST("Parle de ta famille.", "I have got", "I have got a brother and a sister.", [[r"ha(ve|s) got|have", "Utilise « I have got »."]], 5),
            ST("Dis ce que tu aimes faire.", "I like", "I like playing football and listening to music.", [[r"\b(like|love|enjoy)\b", "Utilise like / love / enjoy."]], 4),
            ST("Dis ce que tu n'aimes pas.", "I don't like", "I don't like getting up early.", [[r"don't|do not", "Utilise « I don't like »."]], 4),
            ST("Donne ta matière ou ton activité préférée et dis pourquoi.", "My favourite", "My favourite subject is English because it is useful.", [[r"favourite|favorite", "Utilise « my favourite »."], [r"because", "Justifie avec « because »."]], 6)]},
 {"id": "journee", "icon": "⏰", "group": "Novice", "title": "Ma journée type", "desc": "Raconter une journée habituelle au présent simple.",
  "consigne": "Raconte ta journée habituelle, au présent simple. Pense aux connecteurs (first, then, after that…).", "lex": ["get up", "have breakfast", "go to school", "have lunch", "come back home", "do my homework", "go to bed", "always / usually / often / never"],
  "steps": [ST("À quelle heure te lèves-tu ?", "I usually get up at", "I usually get up at seven o'clock.", [[r"get up", "Utilise « get up »."]], 6),
            ST("Que fais-tu ensuite ?", "First,", "First, I have a shower and I have breakfast.", [[r"first", "Commence par « First »."]], 5),
            ST("Comment vas-tu au lycée ?", "Then,", "Then, I go to school by bus.", [[r"\bby\b|walk|on foot", "Dis comment : by bus, by car, on foot…"]], 5),
            ST("Que fais-tu le midi ?", "At lunchtime,", "At lunchtime, I eat in the canteen with my friends.", [], 5),
            ST("Que fais-tu après les cours ?", "After school,", "After school, I often play video games or I go to the gym.", [[r"always|usually|often|sometimes|never", "Ajoute un adverbe de fréquence (often, sometimes…)."]], 6),
            ST("À quelle heure te couches-tu ?", "Finally,", "Finally, I go to bed at ten thirty.", [[r"go(es)? to bed", "Utilise « go to bed »."]], 5)]},
 {"id": "weekend", "icon": "🎉", "group": "Intermédiaire", "title": "Mon dernier week-end", "desc": "Raconter au prétérit avec des connecteurs.",
  "consigne": "Raconte ton dernier week-end (ou un week-end imaginaire) au prétérit.", "lex": ["last weekend", "on Saturday", "went / saw / ate / had / met", "visited / played / watched", "it was great / boring", "then / after that / finally"],
  "steps": [ST("Où étais-tu le week-end dernier ?", "Last weekend, I", "Last weekend, I was at my grandparents' house.", [PAST], 5),
            ST("Qu'as-tu fait samedi ?", "On Saturday,", "On Saturday, I went shopping with my friends.", [PAST], 5),
            ST("Et ensuite ?", "Then,", "Then, we ate a pizza in a small restaurant.", [PAST], 5),
            ST("Qu'as-tu fait dimanche ?", "On Sunday,", "On Sunday, I watched a film and I did my homework.", [PAST], 5),
            ST("As-tu fait quelque chose de spécial ou de drôle ?", "The best moment was when", "The best moment was when my dog jumped into the lake!", [PAST], 7),
            ST("Donne ton avis sur ce week-end.", "It was", "It was a great weekend because I spent time with my family.", [[r"was", "Utilise « It was… »."], [r"because", "Justifie avec « because »."]], 6)]},
 {"id": "email", "icon": "✉️", "group": "Intermédiaire", "title": "Email à un correspondant", "desc": "Écrire un premier email : salutation, présentation, questions, formule finale.",
  "consigne": "Tu écris à un(e) correspondant(e) anglais(e) pour la première fois.", "lex": ["Dear… / Hi…", "I'm your new pen friend", "What about you?", "Do you like…?", "Write back soon!", "Best wishes / Love"],
  "steps": [ST("Salue ton correspondant (prénom : Tom).", "Hi Tom,", "Hi Tom,", [[r"hi|hello|dear", "Commence par Hi / Hello / Dear."]], 2),
            ST("Présente-toi en une phrase (nom, âge, ville).", "My name is", "My name is Hugo, I am sixteen and I live near Lyon.", [], 8),
            ST("Explique pourquoi tu écris.", "I am writing to you because", "I am writing to you because I am your new French pen friend.", [[r"because", "Utilise « because »."]], 8),
            ST("Parle de tes loisirs.", "In my free time,", "In my free time, I like playing basketball and drawing.", [[r"like|love|enjoy|play", "Utilise like / love / play…"]], 7),
            ST("Pose-lui deux questions.", "What about you?", "What about you? Do you have any brothers or sisters? What do you like doing?", [[r"\?", "Pose au moins une question (avec « ? »)."], [r"\b(do|does|are|is|have|what|where|how)\b", "Utilise do / are / what… pour ta question."]], 6),
            ST("Termine ton email.", "Write back soon!", "Write back soon! Best wishes, Hugo", [[r"soon|wishes|love|bye|regards", "Utilise une formule de fin : Write back soon, Best wishes…"]], 3)]},
 {"id": "stage", "icon": "🏪", "group": "CAP · Monde du travail", "title": "Présenter mon stage", "desc": "Présenter l'entreprise, tes missions et ton bilan de stage (PFMP).",
  "consigne": "Présente ta période de formation en entreprise (PFMP).", "lex": ["I did my work placement in…", "a shop / a supermarket / a bakery", "I served customers", "I worked at the till", "I put products on the shelves", "my tutor / my colleagues", "I learnt how to…"],
  "steps": [ST("Où as-tu fait ton stage ?", "I did my work placement in", "I did my work placement in a clothes shop in Nantes.", [[r"work placement|internship|placement", "Utilise « work placement »."]], 7),
            ST("Combien de temps a-t-il duré ?", "It lasted", "It lasted four weeks, from March to April.", [[r"week|month|day", "Indique la durée (weeks, days…)."]], 4),
            ST("Décris l'entreprise.", "It is", "It is a small shop with five employees.", [], 5),
            ST("Quelles étaient tes missions ?", "I", "I served customers, I worked at the till and I put products on the shelves.", [PAST], 8),
            ST("Qu'as-tu appris ?", "I learnt how to", "I learnt how to talk to customers and how to use the till.", [[r"learn(t|ed)|how to", "Utilise « I learnt how to… »."]], 7),
            ST("Donne ton bilan.", "I liked this placement because", "I liked this placement because my colleagues were very nice.", [[r"because", "Justifie avec « because »."]], 7)]},
 {"id": "projets", "icon": "🚀", "group": "Intermédiaire", "title": "Mes projets d'avenir", "desc": "Parler de l'avenir avec going to, will et I'd like to.",
  "consigne": "Parle de tes projets pour l'année prochaine et pour plus tard.", "lex": ["next year", "I'm going to", "I'd like to", "I will", "I hope to", "maybe / probably", "because"],
  "steps": [ST("Que vas-tu faire l'année prochaine ?", "Next year, I am going to", "Next year, I am going to start a vocational diploma.", [[r"going to", "Utilise « going to »."]], 7),
            ST("Quel métier aimerais-tu faire ?", "I would like to be", "I would like to be a nurse.", [[r"would like|'d like", "Utilise « I would like to »."]], 6),
            ST("Pourquoi ?", "because", "I want to do this job because I like helping people.", [[r"because", "Utilise « because »."]], 6),
            ST("Où aimerais-tu vivre plus tard ?", "Later, I hope to live", "Later, I hope to live in a big city near the sea.", [], 6),
            ST("Fais une prédiction sur ta vie dans 10 ans.", "In ten years, I will", "In ten years, I will probably have a family and a dog.", [[r"\bwill\b|'ll", "Utilise « will »."]], 7)]},
 {"id": "avis", "icon": "⚖️", "group": "Avancé", "title": "Donner son avis argumenté", "desc": "« Should mobile phones be banned at school? » : introduction, arguments, conclusion.",
  "consigne": "Sujet : Should mobile phones be banned at school? Donne ton avis de façon organisée.", "lex": ["In my opinion,", "Firstly, / Secondly,", "Moreover, / What's more,", "However, / On the other hand,", "For example,", "To conclude, / All in all,"],
  "steps": [ST("Présente le sujet.", "Nowadays,", "Nowadays, most teenagers have a smartphone and use it all the time.", [], 8),
            ST("Donne ton opinion.", "In my opinion,", "In my opinion, phones should be banned in class but not during breaks.", [[r"opinion|think|believe", "Utilise In my opinion / I think."]], 8),
            ST("Premier argument.", "Firstly,", "Firstly, phones distract students and they can't concentrate.", [[r"first", "Commence par « Firstly »."]], 8),
            ST("Deuxième argument, avec un exemple.", "Moreover,", "Moreover, some students use social media to bully others, for example by posting photos.", [[r"for example|for instance|such as", "Donne un exemple (for example…)."]], 10),
            ST("Présente un argument opposé.", "However,", "However, phones can be useful to look for information or to call parents.", [[r"however|on the other hand|but", "Utilise However / On the other hand."]], 8),
            ST("Conclus.", "To conclude,", "To conclude, I think we should use phones only when the teacher allows it.", [[r"conclude|all in all|to sum up", "Utilise To conclude / All in all."]], 8)]},
 {"id": "candidature", "icon": "📝", "group": "CAP · Monde du travail", "title": "Lettre de candidature", "desc": "Postuler à un job d'été : présentation, motivation, qualités.",
  "consigne": "Tu postules pour un job d'été de vendeur / vendeuse dans un supermarché anglais.", "lex": ["Dear Sir or Madam,", "I am writing to apply for…", "I am interested in…", "I have experience in…", "I am punctual / friendly / hard-working", "I look forward to hearing from you.", "Yours faithfully,"],
  "steps": [ST("Formule d'appel formelle.", "Dear Sir or Madam,", "Dear Sir or Madam,", [[r"dear", "Commence par « Dear »."]], 3),
            ST("Dis pour quel poste tu postules.", "I am writing to apply for", "I am writing to apply for the job of sales assistant advertised on your website.", [[r"apply", "Utilise « apply for »."]], 9),
            ST("Présente-toi (âge, formation).", "I am", "I am eighteen and I am studying sales at a vocational school in France.", [], 9),
            ST("Parle de ton expérience.", "I have", "I have already worked in a supermarket during my work placement.", [[r"\b(have|has)\b.*\b(worked|done|been|had)\b|experience", "Parle de ton expérience (I have worked / experience)."]], 8),
            ST("Donne deux qualités.", "I am", "I am punctual and friendly, and I like working in a team.", [[r"punctual|friendly|hard-working|polite|patient|serious|reliable|organised|organized|dynamic|motivated", "Cite au moins une qualité (punctual, friendly…)."]], 6),
            ST("Termine la lettre.", "I look forward to hearing from you.", "I look forward to hearing from you. Yours faithfully, Lucas Martin", [[r"look forward|faithfully|sincerely|regards", "Utilise une formule de fin formelle."]], 6)]},
]
LES_W = '''      <p><b>Comment ça marche ?</b> Choisis un sujet. Pour chaque étape, écris <b>une phrase en anglais</b> : le début est proposé, à toi de la compléter.</p>
      <p>Des vérifications automatiques t'aident : <span class="hl">majuscule</span>, <span class="hl">point final</span>, <span class="hl">I en majuscule</span>, mots-clés attendus, longueur. Le bouton <b>💡 Exemple</b> montre un modèle si tu bloques.</p>
      <p>À la fin, ton texte est assemblé : tu peux l'<b>écouter</b>, le <b>copier</b> pour l'envoyer au professeur. Ton brouillon est gardé automatiquement sur cet appareil.</p>'''
page("ecriture_guidee.html", "Écriture guidée", "Anglais · Production écrite", 'Écriture <span>guidée</span>',
     "Écrire un texte étape par étape, avec des aides et des vérifications.", ("#fb923c", "#ea580c"), LES_W, "", jsf("ecriture.js", SUJETS=SUJETS_W))
finalize("ecriture_guidee.html")

# ═════════════ EXPRESSION ORALE ═════════════
def R(en, fr=None, ph=None): d = {"en": en}; fr and d.update(fr=fr); ph and d.update(ph=ph); return d
def F(q, help=None, model=None, time=45, fr=None): return {"q": q, "help": help, "model": model, "time": time, "fr": fr}
SUJETS_O = [
 {"id": "salut", "icon": "👋", "group": "Répéter", "title": "Se présenter", "desc": "Phrases simples pour se présenter.",
  "items": [R("Hello, my name is Tom.", "Bonjour, je m'appelle Tom."), R("I am sixteen years old.", "J'ai seize ans."), R("I live in a small town near Paris.", "J'habite une petite ville près de Paris."),
            R("I have got two brothers.", "J'ai deux frères."), R("I like listening to music.", "J'aime écouter de la musique."), R("Nice to meet you!", "Ravi(e) de te rencontrer !")]},
 {"id": "sons", "icon": "👅", "group": "Répéter", "title": "Les sons difficiles", "desc": "th, h, -ed, voyelles longues : des phrases pour s'entraîner.",
  "items": [R("I think three things.", ph="th : la langue entre les dents"), R("Happy birthday, Harry!", ph="h : on souffle"), R("I walked, I played, I wanted.", ph="-ed : /t/, /d/, /ɪd/"),
            R("This is the thirteenth time.", ph="th doux et th dur"), R("Sheep and ship are different.", ph="/iː/ long, /ɪ/ court"), R("The bird heard the word.", ph="/ɜː/")]},
 {"id": "vente", "icon": "🛍️", "group": "Répéter", "title": "CAP · Accueillir un client", "desc": "Les phrases clés du vendeur ou de la vendeuse.",
  "items": [R("Good morning, can I help you?", "Bonjour, puis-je vous aider ?"), R("What size are you?", "Quelle taille faites-vous ?"), R("The fitting rooms are over there.", "Les cabines sont par là-bas."),
            R("Would you like to try it on?", "Voulez-vous l'essayer ?"), R("That's twenty-five pounds, please.", "Ça fait 25 livres, s'il vous plaît."), R("Would you like a bag?", "Voulez-vous un sac ?"), R("Have a nice day!", "Bonne journée !")]},
 {"id": "phrases", "icon": "🎵", "group": "Répéter", "title": "Rythme et intonation", "desc": "Mots accentués, formes faibles, questions qui montent.",
  "items": [R("What do you want to do?", ph="« do you » se prononce très vite"), R("I can swim, but I can't dance.", ph="can faible /kən/, can't fort"), R("Are you ready?", ph="intonation montante ↗"),
            R("Where do you live?", ph="intonation descendante ↘"), R("It's a beautiful day, isn't it?", ph="question tag ↘"), R("I'd like a cup of tea, please.", ph="a cup of → /ə kʌp əv/")]},
 {"id": "libre1", "icon": "💬", "group": "S'exprimer librement", "title": "Parler de soi (1 minute)", "desc": "Réponds à des questions personnelles sans préparer.", "free": True,
  "items": [F("Tell me about yourself.", "My name is… I am… I live in…", "My name is Sarah. I am sixteen and I live in Lille with my parents and my little brother.", 45),
            F("What do you do in your free time?", "In my free time, I…", "In my free time, I play basketball with my friends and I watch series.", 45),
            F("What did you do last weekend?", "Last weekend, I went… / I watched…", "Last weekend, I went to the cinema with my cousin and I visited my grandmother.", 45),
            F("What would you like to do in the future?", "I would like to be… because…", "I would like to be a hairdresser because I love being creative.", 45)]},
 {"id": "libre2", "icon": "🏪", "group": "S'exprimer librement", "title": "CAP · L'oral de l'examen", "desc": "Questions types : stage, métier, qualités.", "free": True,
  "items": [F("Where did you do your work placement?", "I did my work placement in…", "I did my work placement in a supermarket in Brest, for six weeks.", 60),
            F("What were your tasks?", "I served customers, I…", "I served customers, I worked at the till and I put products on the shelves.", 60),
            F("What are your qualities?", "I am… and I…", "I am punctual and polite, and I like working in a team.", 45),
            F("Why do you want to work in sales?", "I want to work in sales because…", "I want to work in sales because I like meeting people and giving advice.", 45)]},
 {"id": "libre3", "icon": "🗣️", "group": "S'exprimer librement", "title": "Donner son avis", "desc": "Prendre position et justifier (niveau avancé).", "free": True,
  "items": [F("Should homework be banned?", "In my opinion… because… However…", "In my opinion, homework shouldn't be banned because it helps us practise. However, there is sometimes too much.", 60),
            F("Is social media good or bad for teenagers?", "I think… On the one hand… On the other hand…", "I think social media is both good and bad. On the one hand, it helps us stay in touch. On the other hand, it can be addictive.", 60),
            F("Would you prefer to live in a city or in the countryside?", "I would rather live in… because…", "I would rather live in a city because there are more shops, jobs and things to do.", 60)]},
]
LES_O = '''      <p><b>Comment ça marche ?</b> Écoute le <b>🔊 modèle</b> (ou en <b>🐢 lentement</b>), répète à voix haute, puis <b>🎙️ enregistre-toi</b> et réécoute-toi pour comparer.</p>
      <p>Sur certains navigateurs (Chrome, Edge, Safari), le bouton <b>🗣️ Tester ma prononciation</b> affiche les mots reconnus en <span style="color:#4ade80">vert</span> et ceux à retravailler en <span style="color:#f87171">rouge</span>. Ce n'est qu'une aide : la machine se trompe parfois !</p>
      <p>Dans « S'exprimer librement », réponds à la question en anglais avant la fin du chrono. Utilise l'aide si tu bloques. <b>Tes enregistrements restent sur ton appareil</b> : rien n'est envoyé.</p>'''
page("expression_orale.html", "Expression orale", "Anglais · Production orale", 'Expression <span>orale</span>',
     "Écouter, répéter, s'enregistrer et se réécouter.", ("#e879f9", "#c026d3"), LES_O, "", jsf("oral.js", SUJETS=SUJETS_O))
finalize("expression_orale.html")

# ═════════════ ESPACE PROF ═════════════
LES_P = '''      <p><b>Travail de la semaine en 3 étapes :</b> 1. donnez un titre, 2. cochez les activités, 3. copiez le lien et collez-le sur l'ENT (ou projetez-le en classe).</p>
      <p>Les élèves voient la liste, cochée au fur et à mesure qu'ils font les activités, puis copient un <b>bilan</b> avec leur prénom et un <b>code de contrôle</b>. Aucun compte, aucune donnée envoyée : tout reste dans le navigateur de l'élève.</p>
      <p>Dans chaque activité, l'élève peut aussi copier son résultat de mission. Collez ces lignes plus bas pour vérifier qu'elles n'ont pas été modifiées.</p>'''
page("prof.html", "Espace professeur", "English Activities · Professeur", 'Espace <span>professeur</span>',
     "Composer un travail de la semaine et vérifier les résultats.", ("#60a5fa", "#2563eb"), LES_P, "", jsf("prof.js"))
finalize("prof.html")

# ═════════════ DEVOIR (vue élève) ═════════════
page("devoir.html", "Travail de la semaine", "English Activities", 'Travail de la <span>semaine</span>',
     "Les activités demandées par ton professeur.", ("#f472b6", "#db2777"), None, "", jsf("devoir.js"))
finalize("devoir.html")
print("ok")
