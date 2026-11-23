import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
exec(open(_EA_OUT+"/content_helpers.py", encoding="utf-8").read())

def P(word, ok, opts, tip, say=None):
    return C(None, opts, big=word, say=say or word, c=opts.index(ok), keep=True, tip=tip)
def MP(word, a, b, tip):  # paire minimale : on entend word, on choisit entre a et b
    return C(None, [word, b if word == a else a], say=word, listen=True, tip=tip)

# ═════════════ TH ═════════════
TH1, TH2 = "/θ/ (sourd)", "/ð/ (sonore)"
RTH = "<b>/θ/</b> : souffle sans vibration (think, three) · <b>/ð/</b> : la gorge vibre (this, mother). Pour les deux, la langue est entre les dents !"
newpage("phono_th.html", "Prononcer le TH – Entraînement", 'Prononcer le <span>TH</span>',
  "/θ/ comme dans think · /ð/ comme dans this", ("#fcd34d", "#f59e0b"),
  '''      <p>Le <span class="hl">th</span> n'existe pas en français. On place le <b>bout de la langue entre les dents</b> et on souffle.</p>
      <table>
        <tr><th>Son</th><th>Comment ?</th><th>Exemples</th></tr>
        <tr><td><span class="hl">/θ/</span></td><td>sourd : on souffle, la gorge ne vibre pas</td><td>think, three, thank you, mouth, birthday, maths</td></tr>
        <tr><td><span class="hl">/ð/</span></td><td>sonore : la gorge vibre</td><td>this, that, the, mother, brother, they, with</td></tr>
      </table>
      <p>Attention à ne pas dire « s » ou « z » : <span class="ex">think ≠ sink · this ≠ zis</span>. Pose un doigt sur ta gorge pour sentir la vibration du /ð/.</p>''',
  {"th": ("choice", "Écoute : /θ/ ou /ð/ ?", [
      P("think", TH1, [TH1, TH2], RTH), P("three", TH1, [TH1, TH2], RTH), P("thank you", TH1, [TH1, TH2], RTH), P("mouth", TH1, [TH1, TH2], RTH),
      P("birthday", TH1, [TH1, TH2], RTH), P("maths", TH1, [TH1, TH2], RTH), P("thirsty", TH1, [TH1, TH2], RTH),
      P("this", TH2, [TH1, TH2], RTH), P("mother", TH2, [TH1, TH2], RTH), P("brother", TH2, [TH1, TH2], RTH), P("they", TH2, [TH1, TH2], RTH),
      P("weather", TH2, [TH1, TH2], RTH), P("together", TH2, [TH1, TH2], RTH), P("there", TH2, [TH1, TH2], RTH),
    ]),
    "mp": ("choice", "Écoute : quel mot entends-tu ?", [
      MP("think", "think", "sink", "think /θ/ · sink /s/."), MP("sink", "think", "sink", "think /θ/ · sink /s/."), MP("thank", "thank", "sank", "thank /θ/ · sank /s/."),
      MP("mouth", "mouth", "mouse", "mouth /θ/ · mouse /s/."), MP("mouse", "mouth", "mouse", "mouth /θ/ · mouse /s/."), MP("three", "three", "tree", "three /θ/ · tree /t/."),
      MP("tree", "three", "tree", "three /θ/ · tree /t/."), MP("they", "they", "day", "they /ð/ · day /d/."),
    ])},
  [M("th", "👅", "/θ/ ou /ð/ ?", "Écoute et classe les mots.", ["th"], 12),
   M("mp", "👂", "think ou sink ?", "Écoute et choisis le mot entendu.", ["mp"], 8),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["th", "mp"], 12)], tag="Anglais · Phonologie")

# ═════════════ VOYELLES LONGUES / COURTES ═════════════
newpage("phono_voyelles.html", "Voyelles longues et courtes – Entraînement", '<span>ship</span> ou sheep ?',
  "Les voyelles longues et courtes", ("#a5f3fc", "#06b6d4"),
  '''      <p>En anglais, la <b>longueur</b> d'une voyelle change le sens du mot !</p>
      <table>
        <tr><th>Courte</th><th>Longue</th></tr>
        <tr><td><span class="hl">/ɪ/</span> ship, live, sit, it, fill</td><td><span class="hl">/iː/</span> sheep, leave, seat, eat, feel</td></tr>
        <tr><td><span class="hl">/ʊ/</span> full, pull, look</td><td><span class="hl">/uː/</span> fool, pool, Luke</td></tr>
        <tr><td><span class="hl">/æ/</span> cat, hat, cap</td><td><span class="hl">/ɑː/</span> cart, heart, carp</td></tr>
        <tr><td><span class="hl">/ɒ/</span> not, cot, shot</td><td><span class="hl">/ɔː/</span> naught, caught, short</td></tr>
      </table>
      <p>Les deux points <b>ː</b> dans l'alphabet phonétique signifient que le son est <b>long</b>.</p>''',
  {"mp": ("choice", "Écoute : quel mot entends-tu ?", [
      MP("ship", "ship", "sheep", "ship /ɪ/ court · sheep /iː/ long."), MP("sheep", "ship", "sheep", "ship /ɪ/ court · sheep /iː/ long."),
      MP("live", "live", "leave", "live /ɪ/ · leave /iː/."), MP("leave", "live", "leave", "live /ɪ/ · leave /iː/."), MP("sit", "sit", "seat", "sit /ɪ/ · seat /iː/."),
      MP("seat", "sit", "seat", "sit /ɪ/ · seat /iː/."), MP("full", "full", "fool", "full /ʊ/ · fool /uː/."), MP("fool", "full", "fool", "full /ʊ/ · fool /uː/."),
      MP("hat", "hat", "heart", "hat /æ/ · heart /ɑː/."), MP("heart", "hat", "heart", "hat /æ/ · heart /ɑː/."), MP("it", "it", "eat", "it /ɪ/ · eat /iː/."),
      MP("eat", "it", "eat", "it /ɪ/ · eat /iː/."), MP("pull", "pull", "pool", "pull /ʊ/ · pool /uː/."), MP("pool", "pull", "pool", "pull /ʊ/ · pool /uː/."),
    ]),
    "len": ("choice", "Écoute : voyelle courte ou longue ?", [
      P("ship", "courte", ["courte", "longue"], "/ɪ/ court."), P("sheep", "longue", ["courte", "longue"], "/iː/ long."), P("feel", "longue", ["courte", "longue"], "/iː/ long."),
      P("fill", "courte", ["courte", "longue"], "/ɪ/ court."), P("food", "longue", ["courte", "longue"], "/uː/ long."), P("good", "courte", ["courte", "longue"], "/ʊ/ court."),
      P("car", "longue", ["courte", "longue"], "/ɑː/ long."), P("cat", "courte", ["courte", "longue"], "/æ/ court."),
    ])},
  [M("mp", "👂", "ship ou sheep ?", "Écoute et choisis le mot entendu.", ["mp"], 12),
   M("len", "⏱️", "Courte ou longue ?", "Écoute la voyelle.", ["len"], 8),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["mp", "len"], 12)], tag="Anglais · Phonologie")

# ═════════════ H ASPIRÉ ═════════════
newpage("phono_h.html", "Le H aspiré – Entraînement", 'Le <span>H</span> aspiré',
  "hat ou at ? Prononcer le h", ("#fecdd3", "#fb7185"),
  '''      <p>En anglais, le <span class="hl">h</span> se prononce presque toujours : on <b>souffle</b>, comme pour faire de la buée sur une vitre.</p>
      <p class="ex">hat, house, happy, hello, hungry, have, his, her</p>
      <p>Ne pas prononcer le h peut changer le sens : <span class="ex">hat (chapeau) ≠ at (à) · heat (chaleur) ≠ eat (manger) · hear (entendre) ≠ ear (oreille)</span>.</p>
      <p>Quelques mots ont un <b>h muet</b> : <span class="ex">hour, honest, honour, heir</span> → <i>an hour</i>.</p>''',
  {"mp": ("choice", "Écoute : quel mot entends-tu ?", [
      MP("hat", "hat", "at", "hat : on souffle le h."), MP("at", "hat", "at", "at : pas de h."), MP("heat", "heat", "eat", "heat : h soufflé."),
      MP("eat", "heat", "eat", "eat : pas de h."), MP("hear", "hear", "ear", "hear : h soufflé."), MP("ear", "hear", "ear", "ear : pas de h."),
      MP("hill", "hill", "ill", "hill : h soufflé."), MP("ill", "hill", "ill", "ill : pas de h."), MP("hand", "hand", "and", "hand : h soufflé."), MP("and", "hand", "and", "and : pas de h."),
    ]),
    "mute": ("choice", "Le h se prononce-t-il ?", [
      P("house", "oui", ["oui", "non"], "h prononcé."), P("hour", "non", ["oui", "non"], "hour : h muet (an hour)."), P("happy", "oui", ["oui", "non"], "h prononcé."),
      P("honest", "non", ["oui", "non"], "honest : h muet."), P("hello", "oui", ["oui", "non"], "h prononcé."), P("hungry", "oui", ["oui", "non"], "h prononcé."),
    ])},
  [M("mp", "👂", "hat ou at ?", "Écoute et choisis le mot entendu.", ["mp"], 10),
   M("mute", "🤫", "h prononcé ou muet ?", "hour, honest… les exceptions.", ["mute"], 6),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["mp", "mute"], 12)], tag="Anglais · Phonologie")

# ═════════════ INTONATION ═════════════
UP, DOWN = "↗ montante", "↘ descendante"
RI = "Question fermée (réponse yes / no) → intonation <b>montante ↗</b>. Question ouverte (wh-) et phrase affirmative → <b>descendante ↘</b>."
newpage("intonation.html", "L'intonation – Entraînement", 'L\'<span>intonation</span>',
  "Intonation montante ↗ ou descendante ↘", ("#ddd6fe", "#8b5cf6"),
  '''      <p>L'<span class="hl">intonation</span>, c'est la mélodie de la phrase : la voix monte ou descend à la fin.</p>
      <table>
        <tr><th>Type de phrase</th><th>Intonation</th><th>Exemple</th></tr>
        <tr><td>Question fermée (yes / no)</td><td><span class="hl">↗ montante</span></td><td>Do you like pizza? ↗</td></tr>
        <tr><td>Question ouverte (wh-)</td><td><span class="hl">↘ descendante</span></td><td>Where do you live? ↘</td></tr>
        <tr><td>Phrase affirmative</td><td><span class="hl">↘ descendante</span></td><td>I live in Paris. ↘</td></tr>
        <tr><td>Question tag (on est sûr)</td><td><span class="hl">↘ descendante</span></td><td>It's cold, isn't it? ↘</td></tr>
      </table>
      <p>Écoute chaque phrase avec 🔊, puis répète-la en imitant la mélodie.</p>''',
  {"int": ("choice", "Intonation montante ou descendante ?", [
      P("Do you like pizza?", UP, [UP, DOWN], RI), P("Where do you live?", DOWN, [UP, DOWN], RI), P("Are you tired?", UP, [UP, DOWN], RI),
      P("What's your name?", DOWN, [UP, DOWN], RI), P("I live in Paris.", DOWN, [UP, DOWN], RI), P("Can you swim?", UP, [UP, DOWN], RI),
      P("How old are you?", DOWN, [UP, DOWN], RI), P("Is it raining?", UP, [UP, DOWN], RI), P("Did you see the film?", UP, [UP, DOWN], RI),
      P("Why are you late?", DOWN, [UP, DOWN], RI), P("She is my sister.", DOWN, [UP, DOWN], RI), P("Have you got a pen?", UP, [UP, DOWN], RI),
  ])},
  [M("int", "🎵", "↗ ou ↘ ?", "Question fermée, question ouverte ou affirmation ?", ["int"], 12)], tag="Anglais · Phonologie")

# ═════════════ FORMES FAIBLES ═════════════
newpage("formes_faibles.html", "Les formes faibles – Entraînement", 'Les formes <span>faibles</span>',
  "Les petits mots qu'on prononce à peine : /ə/", ("#e9d5ff", "#c084fc"),
  '''      <p>En anglais, on accentue les <b>mots importants</b> (noms, verbes, adjectifs) et on prononce <b>rapidement et faiblement</b> les petits mots grammaticaux : c'est la <span class="hl">forme faible</span>, souvent avec le son <b>/ə/</b> (schwa, un « e » très léger).</p>
      <table>
        <tr><th>Mot</th><th>Forme forte</th><th>Forme faible</th><th>Exemple</th></tr>
        <tr><td>can</td><td>/kæn/</td><td>/kən/</td><td>I can swim.</td></tr>
        <tr><td>to</td><td>/tuː/</td><td>/tə/</td><td>I want to go.</td></tr>
        <tr><td>and</td><td>/ænd/</td><td>/ən/</td><td>fish and chips</td></tr>
        <tr><td>of</td><td>/ɒv/</td><td>/əv/</td><td>a cup of tea</td></tr>
        <tr><td>a</td><td>/eɪ/</td><td>/ə/</td><td>a dog</td></tr>
        <tr><td>was</td><td>/wɒz/</td><td>/wəz/</td><td>He was tired.</td></tr>
      </table>
      <p>On utilise la forme <b>forte</b> en fin de phrase ou pour insister : <span class="ex">Yes, I can! /kæn/</span></p>''',
  {"weak": ("choice", "Quel mot est prononcé faiblement ?", [
      P("I can swim.", "can", ["I", "can", "swim"], "can → /kən/ (forme faible). On accentue swim."),
      P("I want to go home.", "to", ["want", "to", "home"], "to → /tə/. On accentue want, go, home."),
      P("Fish and chips, please.", "and", ["Fish", "and", "chips"], "and → /ən/."),
      P("A cup of tea.", "of", ["cup", "of", "tea"], "of → /əv/."),
      P("He was tired.", "was", ["He", "was", "tired"], "was → /wəz/."),
      P("Bread and butter.", "and", ["Bread", "and", "butter"], "and → /ən/."),
      P("I'm going to the shop.", "to", ["going", "to", "shop"], "to → /tə/."),
      P("Can you help me?", "Can", ["Can", "help", "me"], "Can → /kən/ en début de question."),
    ]),
    "strong": ("choice", "Forme forte ou faible ?", [
      P("Yes, I can!", "forte", ["faible", "forte"], "en fin de phrase → forme forte /kæn/."), P("I can dance.", "faible", ["faible", "forte"], "au milieu → forme faible /kən/."),
      P("Where are you from?", "forte", ["faible", "forte"], "from en fin de phrase → forme forte."), P("I'm from Spain.", "faible", ["faible", "forte"], "from au milieu → forme faible /frəm/."),
  ])},
  [M("weak", "🔉", "Le mot faible", "Quel petit mot est prononcé /ə/ ?", ["weak"], 8),
   M("strong", "🔊", "Forte ou faible ?", "Fin de phrase ou milieu ?", ["strong"], 4),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["weak", "strong"], 12)], tag="Anglais · Phonologie")
print("content10 ok", REGISTRY)
