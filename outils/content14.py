import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
exec(open(_EA_OUT+"/content_helpers.py", encoding="utf-8").read())
SECTION_TAG.update({f: "Anglais · Syntaxe" for f in ["ordre_mots.html", "double_complement.html", "negation.html"]})

# ═════════════ ORDRE DES MOTS ═════════════
newpage("ordre_mots.html", "L'ordre des mots – Entraînement", "L'ordre des <span>mots</span>",
  "Sujet, verbe, complément · manière, lieu, temps", ("#fde68a", "#ca8a04"),
  '''      <p>En anglais, l'ordre des mots est <b>fixe</b> :</p>
      <div class="formula"><b>Sujet</b> + <b>verbe</b> + <b>complément d'objet</b> + <b>manière</b> + <b>lieu</b> + <b>temps</b></div>
      <p class="ex">She speaks English very well. · I went to school by bus yesterday. · He drove carefully to work this morning.</p>
      <p>On ne sépare <b>jamais</b> le verbe de son complément d'objet : <span class="ex">She speaks English very well. <s>She speaks very well English.</s></span></p>
      <p>Le <b>temps</b> peut aussi venir en tête de phrase : <span class="ex">Yesterday, I went to school by bus.</span></p>
      <p>Les adverbes de fréquence (always, often…) se placent avant le verbe, mais après be : <span class="ex">I often go there. · She is always late.</span></p>''',
  {"choice": ("choice", "Quelle phrase est correcte ?", [
      C(None, ["She speaks English very well.", "She speaks very well English.", "She very well speaks English."], tip="verbe + complément + manière : on ne sépare pas speaks et English."),
      C(None, ["I went to school by bus yesterday.", "I went yesterday by bus to school.", "I yesterday went to school by bus."], tip="lieu + manière + temps (ou temps en tête)."),
      C(None, ["He plays the piano every day.", "He plays every day the piano.", "He every day plays the piano."], tip="complément avant le temps."),
      C(None, ["We watched a film at the cinema last night.", "We watched at the cinema a film last night.", "We last night watched a film at the cinema."], tip="complément + lieu + temps."),
      C(None, ["I like chocolate very much.", "I like very much chocolate.", "I very much chocolate like."], tip="on ne sépare pas like et chocolate."),
      C(None, ["They often eat pizza on Fridays.", "They eat often pizza on Fridays.", "Often they eat on Fridays pizza."], tip="adverbe de fréquence avant le verbe."),
      C(None, ["Last summer, we travelled to Italy by car.", "Last summer, we travelled by car Italy to.", "We travelled last summer by car to Italy."], tip="temps en tête, puis verbe + lieu + manière."),
      C(None, ["She opened the door slowly.", "She opened slowly the door.", "She slowly the door opened."], tip="verbe + complément + manière."),
    ]),
    "order": ("order", "Remets les mots dans l'ordre", [
      O("She|speaks|English|very well.", fr="Elle parle très bien anglais."), O("I|went|to school|by bus|yesterday.", fr="Je suis allé à l'école en bus hier.", alts=["Yesterday I went to school by bus."]),
      O("He|plays|tennis|every Sunday.", fr="Il joue au tennis tous les dimanches.", alts=["Every Sunday he plays tennis."]), O("We|had|lunch|in the garden.", fr="Nous avons déjeuné dans le jardin."),
      O("They|always|watch|TV|in the evening.", fr="Ils regardent toujours la télé le soir."), O("I|like|football|a lot.", fr="J'aime beaucoup le football."),
  ])},
  [M("choice", "🔎", "Quelle phrase est correcte ?", "Où placer chaque élément ?", ["choice"], 8),
   M("order", "🧩", "Remets dans l'ordre", "Sujet, verbe, complément, manière, lieu, temps.", ["order"], 6),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["choice", "order"], 12)])

# ═════════════ DOUBLE COMPLÉMENT ═════════════
newpage("double_complement.html", "Les verbes à deux compléments – Entraînement", 'Give <span>him</span> the book',
  "give, send, show, tell, buy… + deux compléments", ("#bae6fd", "#0284c7"),
  '''      <p>Certains verbes ont <b>deux compléments</b> : une chose et une personne (<i>give, send, show, lend, tell, buy, bring, offer, teach</i>). Deux ordres sont possibles :</p>
      <table>
        <tr><th>Ordre</th><th>Exemple</th></tr>
        <tr><td>verbe + <b>personne</b> + <b>chose</b> (sans préposition)</td><td>I gave <b>my sister</b> a present.</td></tr>
        <tr><td>verbe + <b>chose</b> + <b>to / for</b> + <b>personne</b></td><td>I gave a present <b>to</b> my sister. · I bought a cake <b>for</b> my mum.</td></tr>
      </table>
      <p><b>to</b> avec give, send, show, lend, tell, teach, offer · <b>for</b> avec buy, make, get, cook.</p>
      <p>Quand la chose est un <b>pronom</b> (it, them), on préfère : verbe + it + to + personne : <span class="ex">Give it to me. <s>Give me it.</s></span></p>
      <p>Pas de préposition juste après le verbe : <span class="ex"><s>I gave to my sister a present.</s></span></p>''',
  {"choice": ("choice", "Quelle phrase est correcte ?", [
      C(None, ["I gave my sister a present.", "I gave to my sister a present.", "I gave a present my sister."], tip="verbe + personne + chose, sans préposition."),
      C(None, ["She sent a letter to her grandma.", "She sent to her grandma a letter.", "She sent a letter her grandma to."], tip="verbe + chose + to + personne."),
      C(None, ["Can you show me the photos?", "Can you show to me the photos?", "Can you show the photos me?"], tip="verbe + personne + chose."),
      C(None, ["Give it to me, please.", "Give me it to, please.", "Give to me it, please."], tip="pronom chose → give it to me."),
      C(None, ["He bought a bike for his son.", "He bought a bike to his son.", "He bought for his son a bike."], tip="buy → for."),
      C(None, ["The teacher told us a funny story.", "The teacher told to us a funny story.", "The teacher said us a funny story."], tip="tell + personne + chose (say ne s'utilise pas ainsi)."),
      C(None, ["My mum made a cake for me.", "My mum made a cake to me.", "My mum made for me a cake."], tip="make → for."),
      C(None, ["Lend them to her.", "Lend her to them.", "Lend to her them."], tip="pronom chose (them) → lend them to her."),
  ])},
  [M("choice", "🎁", "Deux compléments", "give him the book / give the book to him.", ["choice"], 8)])

# ═════════════ NÉGATION ═════════════
NG = "<b>not</b> avec un verbe (don't, isn't, can't…) · <b>no</b> + nom (= not any) · <b>none</b> = aucun (pronom) · <b>nobody, nothing, nowhere, never</b> ont déjà un sens négatif : pas de double négation !"
newpage("negation.html", "La négation – Entraînement", 'not, <span>no</span>, none, never',
  "Construire une phrase négative sans double négation", ("#fecaca", "#dc2626"),
  '''      <table>
        <tr><th>Mot</th><th>Usage</th><th>Exemple</th></tr>
        <tr><td><span class="hl">not</span></td><td>avec un auxiliaire ou be</td><td>I don't like it. · She isn't here. · He can't swim.</td></tr>
        <tr><td><span class="hl">no</span> + nom</td><td>= not any (aucun)</td><td>There's no milk. = There isn't any milk.</td></tr>
        <tr><td><span class="hl">none</span> (of)</td><td>aucun (sans nom après)</td><td>How many tickets are left? — None. · None of my friends came.</td></tr>
        <tr><td><span class="hl">nobody / nothing / nowhere</span></td><td>personne / rien / nulle part</td><td>Nobody called. · I saw nothing.</td></tr>
        <tr><td><span class="hl">never</span></td><td>jamais</td><td>I never eat meat.</td></tr>
        <tr><td><span class="hl">not… any more / any longer</span></td><td>ne… plus</td><td>She doesn't live here any more.</td></tr>
      </table>
      <p>En anglais, <b>une seule négation</b> par phrase : <span class="ex">I don't know anybody. = I know nobody. <s>I don't know nobody.</s></span></p>''',
  {"choice": ("choice", "Choisis la bonne forme", [
      C("There's ____ milk in the fridge.", ["no", "not", "none"], tip="no + nom."), C("I ____ like vegetables.", ["don't", "no", "none"], tip="verbe → don't."),
      C("How many apples are left? — ____ .", ["None", "No", "Not"], tip="pronom sans nom → none."), C("I didn't see ____ .", ["anybody", "nobody", "somebody"], tip="déjà didn't → anybody (pas de double négation)."),
      C("____ came to the party. It was empty.", ["Nobody", "Anybody", "Not anybody"], tip="personne → nobody en sujet."), C("She ____ eats meat. She's vegetarian.", ["never", "doesn't never", "not never"], tip="never seul suffit."),
      C("He doesn't live here ____ .", ["any more", "no more", "never more"], tip="ne… plus → not… any more."), C("____ of my friends can swim.", ["None", "No", "Nobody"], tip="none of + pluriel."),
      C("I have ____ idea.", ["no", "not", "none"], tip="no + nom."), C("There isn't ____ bread left.", ["any", "no", "none"], tip="isn't + any."),
  ]),
  "dbl": ("choice", "Quelle phrase est correcte ?", [
      C(None, ["I don't know anybody here.", "I don't know nobody here.", "I know anybody here."], fr="Je ne connais personne ici.", tip="une seule négation."),
      C(None, ["She never says anything.", "She never says nothing.", "She doesn't never say anything."], fr="Elle ne dit jamais rien.", tip="never + anything."),
      C(None, ["We didn't go anywhere.", "We didn't go nowhere.", "We went anywhere."], fr="Nous ne sommes allés nulle part."),
      C(None, ["Nobody knows the answer.", "Nobody doesn't know the answer.", "Anybody knows the answer."], fr="Personne ne connaît la réponse."),
  ])},
  [M("choice", "🚫", "not, no, none, never…", "Choisis la bonne négation.", ["choice"]),
   M("dbl", "⚠️", "Pas de double négation", "Une seule négation par phrase.", ["dbl"], 4),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["choice", "dbl"], 12)])
print("content14 ok", REGISTRY)
