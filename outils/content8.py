import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
exec(open(_EA_OUT+"/content_helpers.py", encoding="utf-8").read())
SECTION_TAG.update({"so_neither.html": "Anglais · Syntaxe", "questions_indirectes.html": "Anglais · Syntaxe", "causatif.html": "Anglais · Syntaxe"})

# ═════════════ SO DO I / NEITHER DO I ═════════════
SN = "Phrase <b>affirmative</b> → <b>So</b> + auxiliaire + I · phrase <b>négative</b> → <b>Neither</b> + auxiliaire + I. On reprend l'auxiliaire de la phrase (do / does / did si pas d'auxiliaire)."
newpage("so_neither.html", "So do I / Neither do I – Entraînement", '<span>So do I</span> / Neither do I',
  "Moi aussi, moi non plus", ("#f9a8d4", "#ec4899"),
  '''      <p>Pour dire <b>moi aussi</b> ou <b>moi non plus</b>, on reprend l'<b>auxiliaire</b> de la phrase.</p>
      <table>
        <tr><th>Phrase</th><th>Moi aussi / moi non plus</th></tr>
        <tr><td>I like pizza.</td><td><span class="hl">So do I.</span></td></tr>
        <tr><td>I'm tired.</td><td><span class="hl">So am I.</span></td></tr>
        <tr><td>I can swim.</td><td><span class="hl">So can I.</span></td></tr>
        <tr><td>I went to London.</td><td><span class="hl">So did I.</span></td></tr>
        <tr><td>I don't like fish.</td><td><span class="hl">Neither do I.</span></td></tr>
        <tr><td>I'm not hungry.</td><td><span class="hl">Neither am I.</span></td></tr>
        <tr><td>I haven't seen it.</td><td><span class="hl">Neither have I.</span></td></tr>
      </table>
      <p>Ordre : <b>So / Neither + auxiliaire + sujet</b>. On peut dire <i>Nor do I</i> = Neither do I. Plus familier : <i>Me too / Me neither</i>.</p>''',
  {"choice": ("choice", "Réponds « moi aussi » ou « moi non plus »", [
      C("I like chocolate. — ____", ["So do I.", "So am I.", "Neither do I."], tip=SN), C("I'm tired. — ____", ["So am I.", "So do I.", "Neither am I."], tip=SN),
      C("I don't like spiders. — ____", ["Neither do I.", "So do I.", "Neither am I."], tip=SN), C("I can play the piano. — ____", ["So can I.", "So do I.", "So am I."], tip=SN),
      C("I went to the cinema yesterday. — ____", ["So did I.", "So do I.", "So went I."], tip=SN), C("I'm not hungry. — ____", ["Neither am I.", "Neither do I.", "So am I."], tip=SN),
      C("I haven't finished. — ____", ["Neither have I.", "Neither do I.", "So have I."], tip=SN), C("I will come. — ____", ["So will I.", "So do I.", "So am I."], tip=SN),
      C("I didn't see the film. — ____", ["Neither did I.", "Neither do I.", "So did I."], tip=SN), C("I've got a cat. — ____", ["So have I.", "So do I.", "So am I."], tip=SN),
      C("I can't swim. — ____", ["Neither can I.", "Neither do I.", "So can't I."], tip=SN), C("I was late. — ____", ["So was I.", "So did I.", "So am I."], tip=SN),
  ])},
  [M("choice", "🤝", "Moi aussi, moi non plus", "So do I, Neither am I…", ["choice"], 12)], )

# ═════════════ BOTH / EITHER / NEITHER ═════════════
newpage("both_either.html", "both, either, neither – Entraînement", '<span>both</span>, either, neither',
  "Les deux, l'un ou l'autre, aucun des deux", ("#a7f3d0", "#34d399"),
  '''      <table>
        <tr><th>Mot</th><th>Sens</th><th>Exemple</th></tr>
        <tr><td><span class="hl">both</span> (… and …)</td><td>les deux</td><td>Both my parents work. · I like both tea and coffee.</td></tr>
        <tr><td><span class="hl">either</span> (… or …)</td><td>l'un ou l'autre</td><td>You can take either bus. · Either Tom or Emma will come.</td></tr>
        <tr><td><span class="hl">neither</span> (… nor …)</td><td>aucun des deux, ni… ni…</td><td>Neither answer is correct. · I like neither tea nor coffee.</td></tr>
      </table>
      <p><b>both</b> est suivi d'un pluriel ; <b>either</b> et <b>neither</b> d'un singulier : <span class="ex">Both books are good. · Neither book is good.</span></p>
      <p>Dans une phrase négative, on utilise <b>either</b> : <span class="ex">I don't like either of them.</span></p>''',
  {"choice": ("choice", "both, either ou neither ?", [
      C("____ my parents are teachers.", ["Both", "Either", "Neither"], keep=True, tip="les deux (pluriel) → both."), C("You can sit on ____ chair. I don't mind.", ["either", "both", "neither"], keep=True, tip="l'un ou l'autre → either."),
      C("____ of my friends came. I was alone.", ["Neither", "Both", "Either"], keep=True, tip="aucun des deux → neither."), C("I like ____ tea and coffee.", ["both", "either", "neither"], keep=True, tip="both … and."),
      C("You can have ____ cake or ice cream.", ["either", "both", "neither"], keep=True, tip="either … or."), C("____ Tom nor Emma was at school.", ["Neither", "Either", "Both"], keep=True, tip="neither … nor."),
      C("I don't like ____ of these songs.", ["either", "neither", "both"], keep=True, tip="phrase négative (don't) → either."), C("____ answers are correct. Well done!", ["Both", "Either", "Neither"], keep=True, tip="les deux réponses → both + pluriel."),
      C("____ answer is correct. Try again!", ["Neither", "Both", "Either"], keep=True, tip="aucune des deux → neither + singulier."), C("We can go ____ on Saturday or on Sunday.", ["either", "both", "neither"], keep=True, tip="either … or."),
  ])},
  [M("choice", "✌️", "both, either ou neither ?", "Les deux, l'un ou l'autre, aucun ?", ["choice"])])

# ═════════════ QUESTIONS INDIRECTES ═════════════
QI = "Dans une question indirecte, on garde l'ordre <b>sujet + verbe</b> (pas d'inversion, pas de do / does / did)."
newpage("questions_indirectes.html", "Les questions indirectes – Entraînement", 'Can you tell me <span>where it is</span>?',
  "Les questions indirectes et polies", ("#bfdbfe", "#93c5fd"),
  '''      <p>Pour poser une question <b>polie</b>, on commence par <i>Can you tell me…? · Do you know…? · Could you tell me…?</i> puis on utilise l'ordre d'une phrase <b>affirmative</b>.</p>
      <table>
        <tr><th>Question directe</th><th>Question indirecte</th></tr>
        <tr><td>Where <b>is</b> the station?</td><td>Can you tell me where the station <b>is</b>?</td></tr>
        <tr><td>What time <b>does</b> the shop <b>open</b>?</td><td>Do you know what time the shop <b>opens</b>?</td></tr>
        <tr><td>How much <b>is</b> this jacket?</td><td>Could you tell me how much this jacket <b>is</b>?</td></tr>
        <tr><td><b>Is</b> there a bank near here?</td><td>Do you know <b>if</b> there is a bank near here?</td></tr>
      </table>
      <p>Pour une question fermée (oui / non), on ajoute <span class="hl">if</span> (si).</p>''',
  {"choice": ("choice", "Choisis la bonne question indirecte", [
      C("Can you tell me where ____ ?", ["the station is", "is the station", "does the station is"], tip=QI), C("Do you know what time ____ ?", ["the shop opens", "does the shop open", "opens the shop"], tip=QI),
      C("Could you tell me how much ____ ?", ["this jacket is", "is this jacket", "costs this jacket"], tip=QI), C("Do you know ____ there is a bank near here?", ["if", "is", "what"], tip="question oui / non → if."),
      C("Can you tell me where ____ ?", ["the toilets are", "are the toilets", "do the toilets are"], tip=QI), C("I'd like to know what ____ .", ["your name is", "is your name", "your name"], tip=QI),
      C("Do you know when ____ ?", ["the bus leaves", "does the bus leave", "leaves the bus"], tip=QI), C("Could you tell me ____ you have this in blue?", ["if", "do", "are"], tip="question oui / non → if."),
      C("Can you tell me how ____ to the museum?", ["I can get", "can I get", "do I get"], tip=QI), C("Do you know who ____ ?", ["that man is", "is that man", "that man"], tip=QI),
    ]),
    "order": ("order", "Remets la question polie dans l'ordre", [
      O("Can you tell me|where|the station|is?", trap="does"), O("Do you know|what time|the film|starts?", trap="does"),
      O("Could you tell me|how much|it|is?", trap="costs"), O("Do you know|if|the shop|is open?", trap="is it"),
    ])},
  [M("choice", "🙋", "La bonne question indirecte", "Sujet + verbe : pas d'inversion !", ["choice"]),
   M("order", "🧩", "Remets dans l'ordre", "Construis la question polie.", ["order"], 4),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["choice", "order"], 12)])

# ═════════════ AGO / FOR / SINCE ═════════════
AFS = "<b>ago</b> = il y a (prétérit) · <b>for</b> = pendant / depuis + durée · <b>since</b> = depuis + point de départ."
newpage("ago_for_since.html", "ago, for, since – Entraînement", '<span>ago</span>, for, since',
  "Il y a, pendant, depuis", ("#fde68a", "#fbbf24"),
  '''      <table>
        <tr><th>Mot</th><th>Sens</th><th>Temps</th><th>Exemple</th></tr>
        <tr><td><span class="hl">ago</span></td><td>il y a (moment passé)</td><td>prétérit</td><td>I went to London <b>two years ago</b>.</td></tr>
        <tr><td><span class="hl">for</span></td><td>pendant / depuis + <b>durée</b></td><td>tous les temps</td><td>I have lived here <b>for ten years</b>.</td></tr>
        <tr><td><span class="hl">since</span></td><td>depuis + <b>point de départ</b></td><td>present perfect</td><td>I have lived here <b>since 2015</b>.</td></tr>
      </table>
      <p><b>ago</b> se place <b>après</b> la durée : <span class="ex">three days ago <s>ago three days</s></span>.</p>''',
  {"choice": ("choice", "ago, for ou since ?", [
      C("I saw him three days ____ .", ["ago", "for", "since"], keep=True, tip=AFS), C("She has worked here ____ 2019.", ["since", "for", "ago"], keep=True, tip=AFS),
      C("We have known each other ____ five years.", ["for", "since", "ago"], keep=True, tip=AFS), C("They moved to Paris a long time ____ .", ["ago", "since", "for"], keep=True, tip=AFS),
      C("I've been waiting ____ an hour!", ["for", "since", "ago"], keep=True, tip=AFS), C("He has been ill ____ Monday.", ["since", "for", "ago"], keep=True, tip=AFS),
      C("The film started ten minutes ____ .", ["ago", "for", "since"], keep=True, tip=AFS), C("I lived in Spain ____ two years.", ["for", "since", "ago"], keep=True, tip=AFS),
      C("We haven't seen her ____ Christmas.", ["since", "for", "ago"], keep=True, tip=AFS), C("I started English six years ____ .", ["ago", "for", "since"], keep=True, tip=AFS),
  ]),
  "tr": ("choice", "Quelle est la bonne traduction ?", [
      C(None, ["I met her two years ago.", "I met her since two years.", "I met her ago two years."], fr="Je l'ai rencontrée il y a deux ans."),
      C(None, ["I have lived here for ten years.", "I live here since ten years.", "I have lived here since ten years."], fr="J'habite ici depuis dix ans.", tip="depuis + durée → for (+ present perfect)."),
      C(None, ["She has been here since Monday.", "She is here since Monday.", "She has been here for Monday."], fr="Elle est là depuis lundi.", tip="depuis + point de départ → since (+ present perfect)."),
      C(None, ["We left an hour ago.", "We left since an hour.", "We left for an hour ago."], fr="Nous sommes partis il y a une heure."),
  ])},
  [M("choice", "⏳", "ago, for ou since ?", "Il y a, pendant ou depuis ?", ["choice"]),
   M("tr", "🔎", "La bonne traduction", "Attention à « depuis » !", ["tr"], 4),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["choice", "tr"], 12)])

# ═════════════ BE USED TO ═════════════
newpage("be_used_to.html", "be used to – Entraînement", 'used to / <span>be used to</span>',
  "Habitude passée ou être habitué à", ("#ddd6fe", "#a78bfa"),
  '''      <table>
        <tr><th>Structure</th><th>Sens</th><th>Exemple</th></tr>
        <tr><td><span class="hl">used to</span> + BV</td><td>habitude <b>passée</b> révolue (avant…)</td><td>I used to live in Paris. (j'habitais à Paris avant)</td></tr>
        <tr><td><span class="hl">be used to</span> + verbe-ing / nom</td><td><b>être habitué à</b></td><td>I'm used to getting up early. (j'ai l'habitude de…)</td></tr>
        <tr><td><span class="hl">get used to</span> + verbe-ing / nom</td><td><b>s'habituer à</b></td><td>You'll get used to the cold.</td></tr>
      </table>
      <p>Attention : après <b>be used to</b>, le verbe est en <b>-ing</b> (to est ici une préposition).</p>''',
  {"choice": ("choice", "Choisis la bonne forme", [
      C("I ____ in Paris, but now I live in Lyon.", ["used to live", "am used to living", "am used to live"], tip="habitude passée révolue → used to + BV."),
      C("I ____ early. I do it every day.", ["am used to getting up", "used to get up", "am used to get up"], tip="être habitué → be used to + -ing."),
      C("She ____ the cold. She's from Norway.", ["is used to", "used to", "uses to"], tip="être habituée au froid → be used to + nom."),
      C("When I was a child, I ____ a lot of sweets.", ["used to eat", "was used to eating", "am used to eat"], tip="habitude passée → used to + BV."),
      C("Don't worry, you'll ____ the new school.", ["get used to", "used to", "be use to"], tip="s'habituer → get used to."),
      C("He ____ working at night, so he isn't tired.", ["is used to", "used to", "uses to"], tip="être habitué → be used to + -ing."),
      C("We ____ go to the beach every summer.", ["used to", "are used to", "were used to"], tip="habitude passée → used to + BV."),
      C("I'm not ____ driving on the left.", ["used to", "use to", "using to"], tip="be used to + -ing."),
  ])},
  [M("choice", "🔁", "used to ou be used to ?", "Avant… ou être habitué à… ?", ["choice"], 8)])

# ═════════════ CAUSATIF ═════════════
newpage("causatif.html", "Le causatif – Entraînement", '<span>have</span> it done · make · let',
  "Faire faire, obliger, laisser", ("#fed7aa", "#fb923c"),
  '''      <table>
        <tr><th>Structure</th><th>Sens</th><th>Exemple</th></tr>
        <tr><td><span class="hl">have / get</span> + objet + participe passé</td><td>faire faire (par un professionnel)</td><td>I had my hair cut. · She got her car repaired.</td></tr>
        <tr><td><span class="hl">make</span> + personne + BV</td><td>obliger quelqu'un à</td><td>My mum makes me tidy my room.</td></tr>
        <tr><td><span class="hl">let</span> + personne + BV</td><td>laisser, permettre</td><td>My dad lets me go out on Saturdays.</td></tr>
      </table>
      <p>Après <b>make</b> et <b>let</b> : base verbale <b>sans to</b>. <span class="ex">They let me stay. <s>They let me to stay.</s></span></p>''',
  {"choice": ("choice", "Choisis la bonne forme", [
      C("I ____ yesterday. (le coiffeur me les a coupés)", ["had my hair cut", "cut my hair", "had cut my hair"], tip="faire faire → have + objet + participe passé."),
      C("My mum ____ my room every Saturday.", ["makes me tidy", "makes me to tidy", "lets me tidying"], tip="obliger → make + personne + BV."),
      C("My parents ____ out until 11.", ["let me stay", "let me to stay", "make me staying"], tip="permettre → let + personne + BV."),
      C("She ____ by a mechanic.", ["had her car repaired", "repaired her car", "had her car repair"], tip="faire réparer → have + objet + participe passé."),
      C("The teacher ____ the exercise again.", ["made us do", "made us to do", "let us doing"], tip="obliger → make + personne + BV."),
      C("We're going to ____ next week.", ["have our house painted", "paint our house by someone", "have our house paint"], tip="faire faire → have + objet + participe passé."),
      C("Will you ____ your phone?", ["let me use", "let me to use", "make me using"], tip="permettre → let + BV."),
      C("I need to ____ . It's too long.", ["get my hair cut", "get cut my hair", "get my hair to cut"], tip="faire faire → get + objet + participe passé."),
  ])},
  [M("choice", "🛠️", "have it done, make ou let ?", "Faire faire, obliger ou laisser.", ["choice"], 8)])

# ═════════════ WISH / IF ONLY ═════════════
newpage("wish.html", "wish / if only – Entraînement", 'I <span>wish</span>… / If only…',
  "Exprimer un souhait ou un regret", ("#fbcfe8", "#f472b6"),
  '''      <table>
        <tr><th>Structure</th><th>Sens</th><th>Exemple</th></tr>
        <tr><td><span class="hl">wish / if only</span> + prétérit</td><td>souhait sur le <b>présent</b> (ce n'est pas le cas)</td><td>I wish I had a dog. (je n'en ai pas) · If only I were taller!</td></tr>
        <tr><td><span class="hl">wish / if only</span> + past perfect</td><td>regret sur le <b>passé</b></td><td>I wish I had studied more. (je n'ai pas assez travaillé)</td></tr>
        <tr><td><span class="hl">wish</span> + would + BV</td><td>agacement, envie qu'une chose change</td><td>I wish you would stop talking!</td></tr>
      </table>
      <p>Avec be, on utilise souvent <b>were</b> : <span class="ex">I wish I were rich.</span></p>''',
  {"choice": ("choice", "Choisis la bonne forme", [
      C("I don't have a car. I wish I ____ a car.", ["had", "have", "would have"], tip="souhait sur le présent → prétérit."),
      C("I didn't study. I wish I ____ more.", ["had studied", "studied", "study"], tip="regret sur le passé → past perfect."),
      C("It's raining. I wish it ____ sunny.", ["were", "is", "will be"], tip="présent → prétérit (were)."),
      C("You're always late! I wish you ____ on time.", ["would be", "are", "had been"], tip="agacement → would + BV."),
      C("I can't swim. If only I ____ swim!", ["could", "can", "will"], tip="présent → prétérit (could)."),
      C("I ate too much. I wish I ____ so much.", ["hadn't eaten", "didn't eat", "don't eat"], tip="regret sur le passé → past perfect."),
      C("I live far from school. I wish I ____ closer.", ["lived", "live", "had lived"], tip="présent → prétérit."),
      C("We missed the bus. If only we ____ earlier!", ["had left", "left", "leave"], tip="regret sur le passé → past perfect."),
  ])},
  [M("choice", "🌠", "Souhaits et regrets", "wish + prétérit ou past perfect ?", ["choice"], 8)])

# ═════════════ PRÉSENT BE + ING POUR LE FUTUR ═════════════
newpage("futur_ing.html", "Le présent be + -ing pour le futur – Entraînement", 'I\'m <span>meeting</span> Tom tomorrow',
  "Parler d'un rendez-vous ou d'un projet organisé", ("#c4b5fd", "#8b5cf6"),
  '''      <p>Le <span class="hl">présent be + -ing</span> peut parler du <b>futur</b> : pour un projet <b>organisé</b>, un rendez-vous fixé (avec une date ou une heure).</p>
      <p class="ex">I'm meeting Tom tomorrow at 5. · We're flying to Rome on Friday. · What are you doing tonight?</p>
      <table>
        <tr><th>Forme</th><th>Usage</th><th>Exemple</th></tr>
        <tr><td>be + -ing</td><td>rendez-vous, projet organisé</td><td>I'm seeing the dentist on Monday.</td></tr>
        <tr><td>be going to</td><td>intention, projet décidé</td><td>I'm going to learn the guitar.</td></tr>
        <tr><td>will</td><td>prédiction, décision sur le moment</td><td>I think it will rain. · I'll help you!</td></tr>
      </table>''',
  {"gap": ("gap", "Mets le verbe au présent be + -ing", [
      G("I ____ Tom tomorrow at 5.", ["am meeting", "'m meeting"], "meet", w=200), G("We ____ to Rome on Friday.", ["are flying", "'re flying"], "fly", w=200),
      G("She ____ the dentist on Monday.", ["is seeing", "'s seeing"], "see", w=200), G("What ____ tonight?", ["are you doing"], "you / do", w=220),
      G("They ____ married in June.", ["are getting", "'re getting"], "get", w=200), G("I ____ football after school today.", ["am playing", "'m playing"], "play", w=200),
    ]),
    "choice": ("choice", "be + -ing, going to ou will ?", [
      C("I ____ the doctor at 3 pm. It's in my diary.", ["am seeing", "will see", "see"], tip="rendez-vous fixé → be + -ing."),
      C("I think it ____ tomorrow.", ["will rain", "is raining", "rains"], tip="prédiction (I think) → will."),
      C("Oh, the phone! I ____ it.", ["'ll answer", "'m answering", "answer"], tip="décision sur le moment → will."),
      C("We ____ to Spain next week. We've got the tickets.", ["are flying", "will fly", "fly"], tip="projet organisé → be + -ing."),
      C("What ____ this weekend?", ["are you doing", "will you do", "do you do"], tip="projet du week-end → be + -ing."),
      C("One day, I ____ a famous singer!", ["will be", "am being", "am"], tip="prédiction lointaine → will."),
  ])},
  [M("gap", "✍️", "Conjugue", "I'm meeting, we're flying…", ["gap"], 6),
   M("choice", "⚖️", "be + -ing, going to ou will ?", "Rendez-vous, prédiction ou décision ?", ["choice"], 6),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["gap", "choice"], 12)])
print("content8 ok", REGISTRY)
