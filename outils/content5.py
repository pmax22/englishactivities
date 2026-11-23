import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
exec(open(_EA_OUT+"/content_helpers.py", encoding="utf-8").read())

# ═════════════ EXCLAMATIVES ═════════════
newpage("exclamatives.html", "Les exclamatives – Entraînement", '<span>What</span> a day! <span>How</span> nice!',
  "Les phrases exclamatives", ("#fcd34d", "#f59e0b"),
  '''      <table>
        <tr><th>Structure</th><th>Exemple</th></tr>
        <tr><td><span class="hl">What a / an</span> + (adjectif) + nom singulier !</td><td>What a beautiful day! · What an idea!</td></tr>
        <tr><td><span class="hl">What</span> + (adjectif) + nom pluriel / indénombrable !</td><td>What lovely flowers! · What bad weather!</td></tr>
        <tr><td><span class="hl">How</span> + adjectif / adverbe !</td><td>How nice! · How fast he runs!</td></tr>
        <tr><td><span class="hl">so</span> + adjectif · <span class="hl">such (a)</span> + adjectif + nom</td><td>It's so cold! · She's such a nice girl!</td></tr>
      </table>
      <p>Attention : pas de <b>a</b> devant un pluriel ou un indénombrable : <span class="ex">What nice weather! <s>What a nice weather!</s></span></p>''',
  {
    "choice": ("choice", "Choisis la bonne exclamation", [
      C("____ beautiful day!", ["What a", "What", "How"], tip="nom singulier → What a."), C("____ lovely flowers!", ["What", "What a", "How"], tip="nom pluriel → What (sans a)."),
      C("____ nice!", ["How", "What", "What a"], tip="adjectif seul → How."), C("____ awful weather!", ["What", "What an", "How"], tip="weather est indénombrable → What."),
      C("____ interesting idea!", ["What an", "What a", "How"], tip="son voyelle → What an."), C("____ fast he runs!", ["How", "What", "What a"], tip="adverbe → How."),
      C("It's ____ cold today!", ["so", "such", "what"], tip="so + adjectif."), C("She's ____ nice girl!", ["such a", "so", "how"], tip="such a + adjectif + nom."),
      C("____ big house!", ["What a", "How", "What"], tip="nom singulier → What a."), C("____ delicious!", ["How", "What a", "What"], tip="adjectif seul → How."),
    ]),
    "order": ("order", "Remets les mots dans l'ordre", [
      O("What|a|beautiful|dress!", fr="Quelle belle robe !", trap="How"), O("How|tall|you are!", fr="Comme tu es grand !", trap="What"),
      O("What|nice|people!", fr="Quels gens sympathiques !", trap="a"), O("What|an|amazing|film!", fr="Quel film incroyable !", trap="How"),
    ]),
  },
  [M("choice", "❗", "What, What a ou How ?", "Choisis le bon début d'exclamation.", ["choice"]),
   M("order", "🧩", "Remets dans l'ordre", "Attention au piège !", ["order"], 4),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["choice", "order"], 12)])

# ═════════════ CONNECTEURS ═════════════
newpage("connecteurs.html", "Les connecteurs – Entraînement", 'and, but, <span>because</span>…',
  "Relier les idées : les connecteurs logiques", ("#93c5fd", "#60a5fa"),
  '''      <table>
        <tr><th>Sens</th><th>Connecteurs</th><th>Exemple</th></tr>
        <tr><td>addition</td><td><span class="hl">and</span>, also, too</td><td>I like tea and coffee.</td></tr>
        <tr><td>opposition</td><td><span class="hl">but</span>, however, although</td><td>It's cold but sunny. · Although it was late, we stayed.</td></tr>
        <tr><td>cause</td><td><span class="hl">because</span>, as</td><td>I'm tired because I worked a lot.</td></tr>
        <tr><td>conséquence</td><td><span class="hl">so</span>, that's why</td><td>It was raining, so we stayed at home.</td></tr>
        <tr><td>choix</td><td><span class="hl">or</span></td><td>Tea or coffee?</td></tr>
        <tr><td>chronologie</td><td><span class="hl">first, then, after that, finally</span></td><td>First I wake up, then I have breakfast.</td></tr>
        <tr><td>condition</td><td><span class="hl">if, unless</span> (sauf si)</td><td>We'll go out unless it rains.</td></tr>
      </table>''',
  {
    "choice": ("choice", "Choisis le bon connecteur", [
      C("I like pizza ____ I don't like pasta.", ["but", "so", "because"], tip="opposition → but."), C("I'm tired ____ I went to bed late.", ["because", "so", "but"], tip="cause → because."),
      C("It was raining, ____ we stayed at home.", ["so", "because", "although"], tip="conséquence → so."), C("Do you want tea ____ coffee?", ["or", "and", "but"], tip="choix → or."),
      C("____ it was cold, we went swimming.", ["Although", "Because", "So"], tip="opposition (bien que) → Although."), C("____ I wake up, then I have a shower.", ["First", "Finally", "However"], tip="début de la chronologie → First."),
      C("We'll go to the beach ____ it rains.", ["unless", "if", "because"], tip="sauf si → unless."), C("She's very clever. ____, she's lazy.", ["However", "Because", "So"], tip="opposition en début de phrase → However."),
      C("He studied a lot, ____ he passed the exam.", ["so", "but", "or"], tip="conséquence → so."), C("I have a cat ____ a dog.", ["and", "but", "so"], tip="addition → and."),
      C("You can come ____ you finish your homework.", ["if", "unless", "although"], tip="condition → if."), C("We had dinner, ____ we watched a film.", ["then", "although", "because"], tip="chronologie → then."),
    ]),
    "sens": ("choice", "Quel est le sens de ce connecteur ?", [
      C(None, ["cause", "conséquence", "opposition"], big="because", keep=True), C(None, ["conséquence", "cause", "opposition"], big="so", keep=True),
      C(None, ["opposition", "addition", "cause"], big="but", keep=True), C(None, ["opposition", "cause", "chronologie"], big="although", keep=True),
      C(None, ["chronologie", "conséquence", "condition"], big="finally", keep=True), C(None, ["condition", "cause", "addition"], big="unless", keep=True),
      C(None, ["opposition", "conséquence", "addition"], big="however", keep=True),
    ]),
  },
  [M("choice", "🔗", "Choisis le connecteur", "Cause, conséquence, opposition…", ["choice"], 12),
   M("sens", "💡", "Quel sens ?", "Retrouve le sens de chaque connecteur.", ["sens"], 7),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["choice", "sens"], 12)])

# ═════════════ QUESTION TAGS ═════════════
QT = "Le tag reprend l'<b>auxiliaire</b> de la phrase et le <b>pronom</b> sujet. Phrase affirmative → tag négatif ; phrase négative → tag affirmatif."
newpage("question_tags.html", "Les question tags – Entraînement", "It's cold, <span>isn't it?</span>",
  "Les question tags", ("#c4b5fd", "#a78bfa"),
  '''      <p>Le <span class="hl">question tag</span> est une petite question à la fin de la phrase, pour demander confirmation (« n'est-ce pas ? »).</p>
      <div class="formula">phrase <b>affirmative</b> → tag <b>négatif</b> : It's cold, <span class="hl">isn't it</span>?<br>phrase <b>négative</b> → tag <b>affirmatif</b> : You don't like fish, <span class="hl">do you</span>?</div>
      <p>On reprend l'<b>auxiliaire</b> (be, have, can, will…) et le <b>pronom</b> sujet. Sans auxiliaire, on utilise <b>do / does / did</b> :</p>
      <p class="ex">She can swim, can't she? · He went home, didn't he? · Tom plays football, doesn't he?</p>
      <p>Cas particuliers : <span class="ex">I'm late, aren't I? · Let's go, shall we?</span></p>''',
  {
    "choice": ("choice", "Choisis le bon question tag", [
      C("It's cold, ____ ?", ["isn't it", "is it", "doesn't it"], tip=QT), C("You like pizza, ____ ?", ["don't you", "do you", "aren't you"], tip="présent simple sans auxiliaire → don't."),
      C("She can swim, ____ ?", ["can't she", "can she", "doesn't she"], tip="auxiliaire can → can't."), C("They aren't here, ____ ?", ["are they", "aren't they", "do they"], tip="phrase négative → tag affirmatif."),
      C("He went home, ____ ?", ["didn't he", "did he", "wasn't he"], tip="prétérit sans auxiliaire → didn't."), C("We have finished, ____ ?", ["haven't we", "have we", "don't we"], tip="auxiliaire have → haven't."),
      C("You won't forget, ____ ?", ["will you", "won't you", "do you"], tip="won't (négatif) → will."), C("I'm late, ____ ?", ["aren't I", "am I not", "isn't I"], tip="cas particulier : I'm… aren't I?"),
      C("Tom doesn't smoke, ____ ?", ["does he", "doesn't he", "is he"], tip="doesn't → does he."), C("She was tired, ____ ?", ["wasn't she", "was she", "didn't she"], tip="was → wasn't."),
      C("Let's go, ____ ?", ["shall we", "will we", "don't we"], tip="cas particulier : Let's…, shall we?"), C("Your parents live in Lyon, ____ ?", ["don't they", "doesn't they", "aren't they"], tip="your parents = they → don't they."),
    ]),
  },
  [M("choice", "❓", "Choisis le question tag", "isn't it, don't you, can't she…", ["choice"], 12)])

# ═════════════ QUESTIONS SUJET / OBJET ═════════════
newpage("questions_sujet.html", "Questions sur le sujet – Entraînement", '<span>Who</span> called you?',
  "Questions sur le sujet ou sur le complément", ("#f9a8d4", "#f472b6"),
  '''      <p>Quand le mot interrogatif (<b>who, what, which</b>) est le <span class="hl">sujet</span> du verbe, on n'utilise <b>pas</b> do / does / did : l'ordre est celui d'une phrase normale.</p>
      <div class="formula">Question sur le <b>sujet</b> : <span class="hl">Who</span> + verbe ? → <i>Who called you?</i> (Quelqu'un t'a appelé : qui ?)<br>Question sur le <b>complément</b> : <span class="hl">Who did</span> + sujet + BV ? → <i>Who did you call?</i> (Tu as appelé quelqu'un : qui ?)</div>
      <p class="ex">What happened? · Who lives here? · Which team won? · Who did you meet? · What did she say?</p>''',
  {
    "choice": ("choice", "Choisis la bonne question", [
      C(None, ["Who called you?", "Who did call you?", "Who did you call?"], fr="Qui t'a appelé ?", tip="who = sujet → pas de did."),
      C(None, ["Who did you call?", "Who called you?", "Who you called?"], fr="Qui as-tu appelé ?", tip="who = complément → did + sujet + BV."),
      C(None, ["What happened?", "What did happen?", "What did it happen?"], fr="Que s'est-il passé ?", tip="what = sujet → pas de did."),
      C(None, ["Who lives here?", "Who does live here?", "Who do live here?"], fr="Qui habite ici ?", tip="who = sujet → verbe + -s."),
      C(None, ["What did she say?", "What said she?", "What she said?"], fr="Qu'a-t-elle dit ?", tip="what = complément → did + sujet + BV."),
      C(None, ["Which team won?", "Which team did win?", "Which team did it win?"], fr="Quelle équipe a gagné ?", tip="which team = sujet → pas de did."),
      C(None, ["Who did you meet?", "Who met you?", "Who you met?"], fr="Qui as-tu rencontré ?", tip="who = complément → did."),
      C(None, ["Who broke the window?", "Who did break the window?", "Who did the window break?"], fr="Qui a cassé la fenêtre ?", tip="who = sujet → pas de did."),
      C(None, ["What do you want?", "What wants you?", "What you want?"], fr="Qu'est-ce que tu veux ?", tip="what = complément → do + sujet + BV."),
      C(None, ["Who knows the answer?", "Who does know the answer?", "Who do knows the answer?"], fr="Qui connaît la réponse ?", tip="who = sujet."),
    ]),
    "type": ("choice", "Sujet ou complément ?", [
      C(None, ["sujet", "complément"], fr="Who called you?", keep=True, tip="Quelqu'un a appelé → who est sujet."),
      C(None, ["complément", "sujet"], fr="Who did you call?", keep=True, tip="Tu as appelé quelqu'un → who est complément."),
      C(None, ["sujet", "complément"], fr="What happened?", keep=True, tip="Quelque chose est arrivé → sujet."),
      C(None, ["complément", "sujet"], fr="What did you buy?", keep=True, tip="Tu as acheté quelque chose → complément."),
      C(None, ["sujet", "complément"], fr="Who wrote this book?", keep=True, tip="Quelqu'un a écrit → sujet."),
      C(None, ["complément", "sujet"], fr="Who did she invite?", keep=True, tip="Elle a invité quelqu'un → complément."),
    ]),
  },
  [M("choice", "❓", "Choisis la bonne question", "Avec ou sans did ?", ["choice"]),
   M("type", "🔍", "Sujet ou complément ?", "Qui fait l'action ?", ["type"], 6),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["choice", "type"], 12)])

# ═════════════ WHEN + PRÉSENT ═════════════
WH = "Après <b>when, as soon as, before, after, until</b>, on utilise le <b>présent</b> pour parler du futur (jamais will)."
newpage("subordonnees_temps.html", "when + présent – Entraînement", 'When I <span>arrive</span>, I\'ll call you',
  "when, as soon as, before, after, until + présent", ("#99f6e4", "#2dd4bf"),
  '''      <p>Dans une subordonnée de temps qui parle du <b>futur</b>, on utilise le <span class="hl">présent</span> (et non will), contrairement au français.</p>
      <div class="formula"><span class="hl">when / as soon as / before / after / until</span> + présent, … will + BV</div>
      <p class="ex">When I arrive, I'll call you. (Quand j'arriverai…) · I'll wait until you come back. · As soon as she finishes, we'll go.</p>
      <p><s>When I will arrive</s> ✗</p>''',
  {
    "gap": ("gap", "Conjugue le verbe", [
      G("When I ____ , I'll call you.", "arrive", "arrive", tip=WH), G("I'll wait until you ____ back.", "come", "come", tip=WH),
      G("As soon as she ____ , we'll go.", "finishes", "finish", tip=WH + " (she → -es)."), G("We'll have dinner after Dad ____ home.", "gets", "get", tip=WH),
      G("When he ____ 18, he'll learn to drive.", "is", "be", tip=WH), G("I'll tell you when I ____ the results.", "know", "know", tip=WH),
      G("When you ____ to London, you'll see Big Ben.", "go", "go", tip=WH), G("Call me as soon as you ____ .", "land", "land", tip=WH),
      G("When it ____ , we'll go to the beach.", "stops raining", "stop raining", tip=WH, w=200), G("I'll finish this before the film ____ .", "starts", "start", tip=WH),
    ]),
    "choice": ("choice", "Choisis la bonne forme", [
      C("When I ____ older, I'll be a vet.", ["am", "will be", "would be"], tip=WH), C("As soon as I get home, I ____ you.", ["will text", "text", "texted"], tip="proposition principale → will."),
      C("We'll leave when you ____ ready.", ["are", "will be", "were"], tip=WH), C("I'll stay here until you ____ .", ["call", "will call", "called"], tip=WH),
      C("Before you ____ , close the window.", ["leave", "will leave", "left"], tip=WH), C("When she ____ the news, she'll be happy.", ["hears", "will hear", "heard"], tip=WH),
    ]),
  },
  [M("gap", "✍️", "Conjugue", "when / as soon as + présent.", ["gap"]),
   M("choice", "⚖️", "Présent ou will ?", "Jamais will après when !", ["choice"], 6),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["gap", "choice"], 12)])
print("content5 ok", REGISTRY)
