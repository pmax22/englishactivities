import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
exec(open(_EA_OUT+"/content_helpers.py", encoding="utf-8").read())

# ═════════════ DÉMONSTRATIFS ═════════════
TD = "<b>this</b> (singulier, proche) · <b>that</b> (singulier, loin) · <b>these</b> (pluriel, proche) · <b>those</b> (pluriel, loin)."
newpage("demonstratifs.html", "Les démonstratifs – Entraînement", '<span>this</span>, that, these, those',
  "Les démonstratifs : proche ou loin, singulier ou pluriel", ("#fca5a5", "#ef4444"),
  '''      <table>
        <tr><th></th><th>Proche (ici)</th><th>Loin (là-bas)</th></tr>
        <tr><td><b>Singulier</b></td><td><span class="hl">this</span> book</td><td><span class="hl">that</span> book</td></tr>
        <tr><td><b>Pluriel</b></td><td><span class="hl">these</span> books</td><td><span class="hl">those</span> books</td></tr>
      </table>
      <p class="ex">This bag here is mine. · Look at that car over there! · These shoes are new. · Who are those people?</p>
      <p>Mots repères : <b>here</b> (ici) → this / these · <b>over there</b> (là-bas) → that / those.</p>''',
  {
    "choice": ("choice", "this, that, these ou those ?", [
      C("____ book here is mine.", ["This", "That", "These", "Those"], keep=True, tip=TD), C("Look at ____ birds over there!", ["those", "these", "this", "that"], keep=True, tip=TD),
      C("____ shoes I'm wearing are new.", ["These", "Those", "This", "That"], keep=True, tip=TD), C("Who is ____ man over there?", ["that", "this", "these", "those"], keep=True, tip=TD),
      C("I love ____ song! (on l'écoute maintenant)", ["this", "that", "these", "those"], keep=True, tip=TD), C("Can you see ____ mountains in the distance?", ["those", "these", "this", "that"], keep=True, tip=TD),
      C("____ apples here are delicious.", ["These", "Those", "This", "That"], keep=True, tip=TD), C("Do you remember ____ day at the beach last year?", ["that", "this", "these", "those"], keep=True, tip="that peut aussi renvoyer à un moment éloigné dans le temps."),
      C("____ is my sister, next to me.", ["This", "That", "These", "Those"], keep=True, tip=TD), C("____ houses over there are very old.", ["Those", "These", "This", "That"], keep=True, tip=TD),
    ]),
    "tr": ("choice", "Quelle est la bonne traduction ?", [
      C(None, ["These cakes are good.", "This cakes are good.", "Those cake are good."], fr="Ces gâteaux (ici) sont bons."),
      C(None, ["That girl is my cousin.", "This girl over there is my cousin.", "Those girl is my cousin."], fr="Cette fille là-bas est ma cousine."),
      C(None, ["Those cars are fast.", "That cars are fast.", "These car are fast."], fr="Ces voitures (là-bas) sont rapides."),
      C(None, ["This is my phone.", "These is my phone.", "That are my phone."], fr="Ceci est mon téléphone (je l'ai dans la main)."),
      C(None, ["These are my friends.", "This are my friends.", "Those is my friends."], fr="Voici mes amis (à côté de moi)."),
    ]),
    "order": ("order", "Remets les mots dans l'ordre", [
      O("These|shoes|are|too small.", fr="Ces chaussures (que je porte) sont trop petites.", trap="This"),
      O("Look at|that|beautiful|car!", fr="Regarde cette belle voiture (là-bas) !", trap="those"),
      O("Those|people|are|tourists.", fr="Ces gens (là-bas) sont des touristes.", trap="That"),
      O("This|is|my|bedroom.", fr="Voici ma chambre.", trap="These"),
    ]),
  },
  [M("choice", "👉", "this, that, these ou those ?", "Proche ou loin ? Singulier ou pluriel ?", ["choice"]),
   M("tr", "🔎", "Quelle est la bonne traduction ?", "Attention au pluriel !", ["tr"], 5),
   M("order", "🧩", "Remets dans l'ordre", "Construis la phrase. Attention au piège !", ["order"], 4),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["choice", "tr", "order"], 12)])

# ═════════════ PLURIELS IRRÉGULIERS ═════════════
newpage("pluriels.html", "Le pluriel des noms – Entraînement", 'Le pluriel des <span>noms</span>',
  "-s, -es, -ies, -ves et pluriels irréguliers", ("#fde68a", "#f59e0b"),
  '''      <p>En général, on ajoute <span class="hl">-s</span> : a book → two books.</p>
      <table>
        <tr><th>Cas</th><th>Règle</th><th>Exemple</th></tr>
        <tr><td>-s, -ss, -sh, -ch, -x, -o</td><td>+ <span class="hl">-es</span></td><td>bus → buses, box → boxes, tomato → tomatoes</td></tr>
        <tr><td>consonne + y</td><td>y → <span class="hl">-ies</span></td><td>baby → babies, city → cities (mais day → days)</td></tr>
        <tr><td>-f / -fe</td><td>→ <span class="hl">-ves</span></td><td>knife → knives, leaf → leaves, wife → wives</td></tr>
      </table>
      <p><b>Pluriels irréguliers</b> à connaître : child → <span class="hl">children</span> · man → <span class="hl">men</span> · woman → <span class="hl">women</span> · person → <span class="hl">people</span> · foot → <span class="hl">feet</span> · tooth → <span class="hl">teeth</span> · mouse → <span class="hl">mice</span> · fish → fish · sheep → sheep.</p>''',
  {
    "irr": ("gap", "Écris le pluriel", [
      G("one child → two ____", "children", tip="pluriel irrégulier."), G("one man → two ____", "men", tip="pluriel irrégulier."),
      G("one woman → two ____", "women", tip="pluriel irrégulier."), G("one person → two ____", "people", tip="person → people."),
      G("one foot → two ____", "feet", tip="pluriel irrégulier."), G("one tooth → two ____", "teeth", tip="pluriel irrégulier."),
      G("one mouse → two ____", "mice", tip="pluriel irrégulier."), G("one fish → two ____", "fish", tip="fish ne change pas."),
      G("one sheep → two ____", "sheep", tip="sheep ne change pas."),
    ]),
    "reg": ("gap", "Écris le pluriel (attention à l'orthographe)", [
      G("one box → two ____", "boxes", tip="-x → -es."), G("one baby → two ____", "babies", tip="consonne + y → -ies."),
      G("one knife → two ____", "knives", tip="-fe → -ves."), G("one bus → two ____", "buses", tip="-s → -es."),
      G("one city → two ____", "cities", tip="consonne + y → -ies."), G("one leaf → two ____", "leaves", tip="-f → -ves."),
      G("one tomato → two ____", "tomatoes", tip="-o → -es."), G("one day → two ____", "days", tip="voyelle + y → simplement -s."),
      G("one watch → two ____", "watches", tip="-ch → -es."), G("one wife → two ____", "wives", tip="-fe → -ves."),
      G("one potato → two ____", "potatoes", tip="-o → -es."), G("one toy → two ____", "toys", tip="voyelle + y → -s."),
    ]),
    "choice": ("choice", "Choisis le bon pluriel", [
      C(None, ["children", "childs", "childrens"], big="child"), C(None, ["teeth", "tooths", "teeths"], big="tooth"),
      C(None, ["people", "persons", "peoples"], big="person", tip="person → people (persons existe mais est rare)."), C(None, ["mice", "mouses", "mices"], big="mouse"),
      C(None, ["women", "womans", "womens"], big="woman"), C(None, ["knives", "knifes", "knifs"], big="knife"),
      C(None, ["babies", "babys", "babyes"], big="baby"), C(None, ["feet", "foots", "feets"], big="foot"),
    ]),
  },
  [M("reg", "✍️", "-es, -ies, -ves", "Les règles d'orthographe du pluriel.", ["reg"]),
   M("irr", "⚡", "Les pluriels irréguliers", "children, men, feet, mice…", ["irr"], 9),
   M("choice", "🔎", "Choisis le bon pluriel", "Repère la bonne forme.", ["choice"], 8),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["reg", "irr", "choice"], 12)])

# ═════════════ ADVERBES DE MANIÈRE ═════════════
newpage("adverbes_maniere.html", "Les adverbes de manière – Entraînement", 'Les adverbes de <span>manière</span>',
  "quick → quickly · good → well", ("#86efac", "#22c55e"),
  '''      <p>L'<span class="hl">adverbe de manière</span> dit <b>comment</b> on fait une action. Il se place en général <b>après le verbe</b> (ou après le complément).</p>
      <div class="formula">adjectif + <span class="hl">-ly</span> : quick → quick<b>ly</b>, careful → careful<b>ly</b>, slow → slow<b>ly</b></div>
      <p><b>Orthographe :</b> easy → eas<b>ily</b>, happy → happ<b>ily</b> (y → ily) · gentle → gent<b>ly</b>, terrible → terrib<b>ly</b> (-le → -ly).</p>
      <p><b>Irréguliers :</b> good → <span class="hl">well</span> · fast → <span class="hl">fast</span> · hard → <span class="hl">hard</span> · late → late.</p>
      <h4>Adjectif ou adverbe ?</h4>
      <p>L'adjectif décrit un <b>nom</b> : <span class="ex">She is a careful driver.</span> · L'adverbe décrit un <b>verbe</b> : <span class="ex">She drives carefully.</span></p>''',
  {
    "form": ("gap", "Forme l'adverbe", [
      G("quick → ____", "quickly", tip="+ ly."), G("careful → ____", "carefully", tip="+ ly."), G("easy → ____", "easily", tip="y → ily."),
      G("happy → ____", "happily", tip="y → ily."), G("good → ____", "well", tip="irrégulier : good → well."), G("fast → ____", "fast", tip="fast ne change pas."),
      G("slow → ____", "slowly", tip="+ ly."), G("quiet → ____", "quietly", tip="+ ly."), G("gentle → ____", "gently", tip="-le → -ly."),
      G("terrible → ____", "terribly", tip="-le → -ly."), G("hard → ____", "hard", tip="hard ne change pas (hardly = à peine !)."), G("beautiful → ____", "beautifully", tip="+ ly."),
    ]),
    "adjadv": ("choice", "Adjectif ou adverbe ?", [
      C("She is a ____ driver.", ["careful", "carefully"], tip="décrit le nom driver → adjectif."), C("She drives ____ .", ["carefully", "careful"], tip="décrit le verbe drives → adverbe."),
      C("He speaks English very ____ .", ["well", "good"], tip="décrit le verbe speaks → adverbe : well."), C("He is a ____ football player.", ["good", "well"], tip="décrit le nom player → adjectif : good."),
      C("The children played ____ in the garden.", ["happily", "happy"], tip="décrit le verbe → adverbe."), C("This exercise is ____ .", ["easy", "easily"], tip="après be → adjectif."),
      C("Please talk ____ . The baby is sleeping.", ["quietly", "quiet"], tip="décrit le verbe → adverbe."), C("He works very ____ .", ["hard", "hardly"], tip="hard = dur (hardly = à peine)."),
      C("She runs very ____ .", ["fast", "fastly"], tip="fast ne change pas."), C("The test was ____ difficult.", ["terribly", "terrible"], tip="modifie l'adjectif difficult → adverbe."),
    ]),
  },
  [M("form", "✍️", "Forme l'adverbe", "quick → quickly, good → well…", ["form"]),
   M("adjadv", "⚖️", "Adjectif ou adverbe ?", "careful ou carefully ? good ou well ?", ["adjadv"]),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["form", "adjadv"], 12)])

# ═════════════ SOMEONE, ANYTHING, NOBODY ═════════════
SA = "<b>some-</b> : affirmatif · <b>any-</b> : négatif et questions · <b>no-</b> : sens négatif avec un verbe affirmatif · <b>every-</b> : tout le monde, tout, partout."
newpage("someone_anything.html", "someone, anything, nobody… – Entraînement", '<span>someone</span>, anything, nobody',
  "Les composés de some, any, no et every", ("#fcd34d", "#eab308"),
  '''      <table>
        <tr><th></th><th>personne</th><th>chose</th><th>lieu</th></tr>
        <tr><td><b>some-</b> (+)</td><td>someone / somebody</td><td>something</td><td>somewhere</td></tr>
        <tr><td><b>any-</b> (−, ?)</td><td>anyone / anybody</td><td>anything</td><td>anywhere</td></tr>
        <tr><td><b>no-</b></td><td>no one / nobody</td><td>nothing</td><td>nowhere</td></tr>
        <tr><td><b>every-</b></td><td>everyone / everybody</td><td>everything</td><td>everywhere</td></tr>
      </table>
      <p class="ex">Someone is at the door. · I didn't see anything. · Is there anyone here? · Nobody knows. · I looked everywhere.</p>
      <p>Attention : pas de double négation. <span class="ex">I saw nothing. = I didn't see anything. <s>I didn't see nothing.</s></span></p>''',
  {
    "choice": ("choice", "Choisis le bon mot", [
      C("____ is knocking at the door.", ["Someone", "Anyone", "Nothing"], tip=SA), C("I didn't see ____ .", ["anything", "something", "nothing"], tip="négatif avec didn't → any-."),
      C("Is there ____ in the kitchen?", ["anyone", "someone", "no one"], tip="question → any-."), C("____ knows the answer. It's too difficult!", ["Nobody", "Anybody", "Somebody"], tip="personne ne… → nobody."),
      C("I want to go ____ hot for my holidays.", ["somewhere", "anywhere", "nowhere"], tip="affirmatif → some-."), C("There's ____ in the fridge. It's empty!", ["nothing", "anything", "something"], tip="verbe affirmatif + sens négatif → nothing."),
      C("I can't find my keys ____ .", ["anywhere", "somewhere", "nowhere"], tip="négatif (can't) → any-."), C("____ loves this film. It's very popular.", ["Everyone", "Anyone", "No one"], tip="tout le monde → everyone."),
      C("Would you like ____ to drink?", ["something", "anything", "nothing"], tip="offre polie → some- (même dans une question)."), C("He has looked ____ for his phone.", ["everywhere", "anywhere", "nowhere"], tip="partout → everywhere."),
    ]),
    "tr": ("choice", "Quelle est la bonne traduction ?", [
      C(None, ["I didn't see anybody.", "I didn't see nobody.", "I saw anybody."], fr="Je n'ai vu personne.", tip="pas de double négation."),
      C(None, ["Somebody called you.", "Anybody called you.", "Nobody called you."], fr="Quelqu'un t'a appelé."),
      C(None, ["There is nothing to eat.", "There isn't nothing to eat.", "There is anything to eat."], fr="Il n'y a rien à manger."),
      C(None, ["Everything is ready.", "Anything is ready.", "Something are ready."], fr="Tout est prêt."),
      C(None, ["Is anyone there?", "Is someone not there?", "Is nobody there?"], fr="Il y a quelqu'un ?"),
    ]),
  },
  [M("choice", "🎯", "Choisis le bon mot", "some-, any-, no- ou every- ?", ["choice"]),
   M("tr", "🔎", "Quelle est la bonne traduction ?", "Pas de double négation !", ["tr"], 5),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["choice", "tr"], 12)])

# ═════════════ TOO / ENOUGH / SO / SUCH ═════════════
newpage("too_enough.html", "too, enough, so, such – Entraînement", '<span>too</span>, enough, so, such',
  "Trop, assez, si, tellement", ("#bef264", "#84cc16"),
  '''      <table>
        <tr><th>Mot</th><th>Sens</th><th>Place</th><th>Exemple</th></tr>
        <tr><td><span class="hl">too</span></td><td>trop</td><td>too + adjectif</td><td>It's too hot.</td></tr>
        <tr><td><span class="hl">enough</span></td><td>assez</td><td><b>adjectif + enough</b><br>enough + nom</td><td>He's old enough.<br>We have enough money.</td></tr>
        <tr><td><span class="hl">so</span></td><td>si, tellement</td><td>so + adjectif</td><td>She is so nice!</td></tr>
        <tr><td><span class="hl">such</span></td><td>un(e) tel(le), si</td><td>such (a) + adjectif + nom</td><td>It's such a nice day!</td></tr>
      </table>
      <p>Attention à la place de <b>enough</b> avec un adjectif : <span class="ex">tall enough <s>enough tall</s></span>.</p>''',
  {
    "choice": ("choice", "Choisis la bonne réponse", [
      C("I can't drink this tea. It's ____ hot.", ["too", "enough", "such"], tip="trop → too + adjectif."), C("He can't drive. He isn't ____ .", ["old enough", "enough old", "too old"], tip="adjectif + enough."),
      C("We don't have ____ to buy a car.", ["enough money", "money enough", "too money"], tip="enough + nom."), C("She is ____ nice!", ["so", "such", "too much"], tip="so + adjectif."),
      C("It's ____ beautiful day!", ["such a", "so a", "so"], tip="such a + adjectif + nom."), C("This bag is ____ heavy for me.", ["too", "enough", "so much"], tip="trop → too."),
      C("Are you ____ to reach the shelf?", ["tall enough", "enough tall", "too tall"], tip="adjectif + enough."), C("They are ____ good friends!", ["such", "so", "such a"], tip="such + adjectif + nom pluriel (pas de a)."),
      C("I'm ____ tired that I can't think.", ["so", "such", "too"], tip="so + adjectif + that…"), C("There aren't ____ for everyone.", ["enough chairs", "chairs enough", "too chairs"], tip="enough + nom."),
    ]),
    "order": ("order", "Remets les mots dans l'ordre", [
      O("It's|too|cold|to swim.", fr="Il fait trop froid pour nager.", trap="enough"), O("She isn't|old|enough|to vote.", fr="Elle n'est pas assez âgée pour voter.", trap="too"),
      O("It was|such|a|good|film!", fr="C'était un si bon film !", trap="so"), O("He is|so|funny!", fr="Il est tellement drôle !", trap="such"),
      O("We have|enough|time.", fr="Nous avons assez de temps.", trap="too"),
    ]),
  },
  [M("choice", "🎯", "Choisis la bonne réponse", "too, enough, so ou such ?", ["choice"]),
   M("order", "🧩", "Remets dans l'ordre", "Attention à la place de enough !", ["order"], 5),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["choice", "order"], 12)])

# ═════════════ PRONOMS RÉFLÉCHIS ═════════════
newpage("pronoms_reflechis.html", "Les pronoms réfléchis – Entraînement", '<span>myself</span>, yourself…',
  "Les pronoms réfléchis et each other", ("#7dd3fc", "#0ea5e9"),
  '''      <p>Le <span class="hl">pronom réfléchi</span> s'utilise quand le sujet fait l'action <b>sur lui-même</b> (moi-même, toi-même…).</p>
      <table>
        <tr><th>Sujet</th><th>I</th><th>you</th><th>he</th><th>she</th><th>it</th><th>we</th><th>you (pl.)</th><th>they</th></tr>
        <tr><td>Réfléchi</td><td>myself</td><td>yourself</td><td>himself</td><td>herself</td><td>itself</td><td>ourselves</td><td>yourselves</td><td>themselves</td></tr>
      </table>
      <p class="ex">I hurt myself. · She made the cake herself. · Enjoy yourselves!</p>
      <p><b>each other</b> = l'un l'autre (action réciproque) : <span class="ex">Tom and Emma love each other.</span></p>
      <p>Attention : beaucoup de verbes pronominaux français ne le sont pas en anglais : <span class="ex">se lever = get up · se laver = wash · se réveiller = wake up</span>.</p>''',
  {
    "gap": ("gap", "Complète avec le pronom réfléchi", [
      G("I hurt ____ when I fell.", "myself", "I"), G("She made this dress ____ .", "herself", "she"), G("He looked at ____ in the mirror.", "himself", "he"),
      G("We enjoyed ____ at the party.", "ourselves", "we"), G("They built the house ____ .", "themselves", "they"), G("Be careful! Don't cut ____ !", "yourself", "you"),
      G("Children, help ____ to some cake!", "yourselves", "you (pluriel)"), G("The cat is washing ____ .", "itself", "it"), G("Tom taught ____ to play the guitar.", "himself", "Tom"),
      G("Emma, did you do it ____ ?", "yourself", "you"),
    ]),
    "each": ("choice", "Réfléchi ou each other ?", [
      C("Tom and Emma love ____ .", ["each other", "themselves"], tip="l'un l'autre → each other."), C("They looked at ____ in the mirror.", ["themselves", "each other"], tip="chacun se regarde lui-même → themselves."),
      C("We help ____ with our homework.", ["each other", "ourselves"], tip="on s'aide mutuellement → each other."), C("The two friends call ____ every day.", ["each other", "themselves"], tip="réciproque → each other."),
      C("I taught ____ to swim.", ["myself", "each other"], tip="sur soi-même → myself."), C("Lucas and Léa write to ____ .", ["each other", "themselves"], tip="réciproque → each other."),
    ]),
  },
  [M("gap", "✍️", "Complète", "myself, himself, ourselves…", ["gap"]),
   M("each", "🤝", "Réfléchi ou each other ?", "soi-même ou l'un l'autre ?", ["each"], 6),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["gap", "each"], 12)])

# ═════════════ PRESENT PERFECT BE + ING ═════════════
newpage("present_perfect_continu.html", "Present perfect be + -ing – Entraînement", 'Present perfect <span>be + -ing</span>',
  "have / has been + verbe-ing · for / since", ("#f0abfc", "#d946ef"),
  '''      <p>Le <span class="hl">present perfect be + -ing</span> insiste sur la <b>durée</b> d'une action qui a commencé dans le passé et qui <b>continue</b> (ou vient de s'arrêter).</p>
      <div class="formula">sujet + <span class="hl">have / has been</span> + verbe<span class="hl">-ing</span> (+ for / since)</div>
      <p class="ex">I have been waiting for an hour! (j'attends depuis une heure) · She has been learning English since 2020.</p>
      <p><b>Question :</b> How long have you been living here? · <b>Négatif :</b> I haven't been sleeping well.</p>
      <h4>Simple ou be + -ing ?</h4>
      <p>Résultat, nombre de fois → present perfect simple : <span class="ex">I have written three emails.</span><br>Durée, activité en cours → be + -ing : <span class="ex">I have been writing emails all morning.</span></p>''',
  {
    "gap": ("gap", "Mets le verbe au present perfect be + -ing", [
      G("I ____ for an hour!", ["have been waiting", "'ve been waiting"], "wait", w=260), G("She ____ English since 2020.", ["has been learning", "'s been learning"], "learn", w=260),
      G("They ____ football all afternoon.", ["have been playing", "'ve been playing"], "play", w=260), G("It ____ since this morning.", ["has been raining", "'s been raining"], "rain", w=260),
      G("We ____ here for ten years.", ["have been living", "'ve been living"], "live", w=260), G("He ____ on his project all day.", ["has been working", "'s been working"], "work", w=260),
      G("How long ____ ?", ["have you been running"], "you / run", w=280), G("My parents ____ the house for weeks.", ["have been painting", "'ve been painting"], "paint", w=260),
    ]),
    "vs": ("choice", "Simple ou be + -ing ?", [
      C("I ____ three emails this morning.", ["have written", "have been writing"], tip="un nombre / un résultat → simple."), C("I ____ emails all morning.", ["have been writing", "have written"], tip="durée → be + -ing."),
      C("She ____ her keys. She can't get in.", ["has lost", "has been losing"], tip="résultat → simple."), C("You look tired. ____ ?", ["Have you been running", "Have you run"], tip="activité récente qui explique la situation → be + -ing."),
      C("We ____ that film twice.", ["have seen", "have been seeing"], tip="nombre de fois → simple."), C("He ____ for two hours. He's exhausted.", ["has been studying", "has studied"], tip="durée → be + -ing."),
    ]),
  },
  [M("gap", "✍️", "Conjugue", "have / has been + verbe-ing.", ["gap"], 8),
   M("vs", "⚖️", "Simple ou be + -ing ?", "Résultat ou durée ?", ["vs"], 6),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["gap", "vs"], 12)])

# ═════════════ PAST PERFECT ═════════════
newpage("past_perfect.html", "Le past perfect – Entraînement", 'Le <span>past perfect</span>',
  "had + participe passé · l'action d'avant", ("#fda4af", "#f43f5e"),
  '''      <p>Le <span class="hl">past perfect</span> (plus-que-parfait) exprime une action <b>antérieure</b> à une autre action passée.</p>
      <div class="formula">sujet + <span class="hl">had</span> + participe passé</div>
      <p class="ex">When I arrived at the station, the train <b>had</b> already <b>left</b>. (le train est parti avant que j'arrive)</p>
      <p>Mots repères : <b>already</b>, <b>before</b>, <b>after</b>, <b>when</b>, <b>by the time</b>.</p>
      <p><b>Négatif :</b> I hadn't seen him before. · <b>Question :</b> Had you eaten before the film?</p>
      <h4>Past perfect be + -ing</h4>
      <p><span class="hl">had been + verbe-ing</span> insiste sur la <b>durée</b> d'une action avant un moment du passé.</p>
      <p class="ex">I had been waiting for an hour when the bus finally arrived. · She was tired because she had been running.</p>''',
  {
    "gap": ("gap", "Mets le verbe au past perfect", [
      G("When I arrived, the train ____ .", "had left", "leave"), G("She was hungry because she ____ breakfast.", ["hadn't eaten", "had not eaten"], "not / eat"),
      G("I ____ that film before, so I knew the end.", "had seen", "see"), G("When we got home, someone ____ the door.", "had opened", "open"),
      G("He ____ before his trip to London.", ["had never flown"], "never / fly", w=220), G("They were tired because they ____ all day.", "had worked", "work"),
      G("By the time the police came, the thief ____ .", "had escaped", "escape"), G("She ____ her homework before dinner.", "had finished", "finish"),
    ]),
    "first": ("choice", "Quelle action a eu lieu en premier ?", [
      C(None, ["Le train est parti.", "Je suis arrivé."], fr="When I arrived, the train had left.", tip="had left → action la plus ancienne."),
      C(None, ["Elle a mangé.", "Elle est sortie."], fr="She went out after she had eaten.", tip="had eaten → avant."),
      C(None, ["Il avait perdu ses clés.", "Il a appelé sa mère."], fr="He called his mum because he had lost his keys.", tip="had lost → avant."),
      C(None, ["Le film avait commencé.", "Nous sommes arrivés."], fr="When we arrived, the film had started.", tip="had started → avant."),
      C(None, ["J'avais fini mes devoirs.", "J'ai regardé la télé."], fr="I watched TV after I had finished my homework.", tip="had finished → avant."),
    ]),
    "cont": ("gap", "Mets le verbe au past perfect be + -ing", [
      G("I ____ for an hour when the bus arrived.", "had been waiting", "wait", w=230), G("She was out of breath because she ____ .", "had been running", "run", w=230),
      G("They ____ for three years when they got married.", "had been dating", "date", w=230), G("His eyes were red: he ____ .", "had been crying", "cry", w=230),
      G("We ____ all day, so we were exhausted.", "had been working", "work", w=230), G("How long ____ there before you moved?", ["had you been living"], "you / live", w=260),
    ]),
    "choice": ("choice", "Prétérit ou past perfect ?", [
      C("When I got to the party, Tom ____ home.", ["had gone", "went"], tip="Tom est parti avant mon arrivée → past perfect."),
      C("I ____ the door and went in.", ["opened", "had opened"], tip="actions successives → prétérit."),
      C("She couldn't pay because she ____ her purse.", ["had forgotten", "forgot"], tip="l'oubli est antérieur → past perfect."),
      C("Yesterday I ____ up at 7.", ["got", "had got"], tip="simple action passée → prétérit."),
    ]),
  },
  [M("gap", "✍️", "Conjugue", "had + participe passé.", ["gap"], 8),
   M("first", "⏮️", "Qu'est-ce qui s'est passé avant ?", "Repère l'action la plus ancienne.", ["first"], 5),
   M("choice", "⚖️", "Prétérit ou past perfect ?", "Choisis le bon temps.", ["choice"], 4),
   M("cont", "⏳", "had been + -ing", "La durée avant un moment du passé.", ["cont"], 6),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["gap", "first", "choice", "cont"], 12)])

# ═════════════ PROBABILITÉ & MODAUX AU PASSÉ ═════════════
G1, G2 = "Probabilité au présent", "Modaux au passé"
newpage("probabilite.html", "may, might, must, can't – Entraînement", 'may, might, <span>must</span>, can\'t',
  "La probabilité et les modaux au passé", ("#a5f3fc", "#22d3ee"),
  '''      <h4>Exprimer la probabilité</h4>
      <table>
        <tr><th>Certitude</th><th>Modal</th><th>Exemple</th></tr>
        <tr><td>presque sûr (oui)</td><td><span class="hl">must</span></td><td>He must be tired. (il doit être fatigué)</td></tr>
        <tr><td>possible</td><td><span class="hl">may / might / could</span></td><td>It might rain. (il se peut qu'il pleuve)</td></tr>
        <tr><td>presque sûr (non)</td><td><span class="hl">can't</span></td><td>It can't be true! (ça ne peut pas être vrai)</td></tr>
      </table>
      <h4>Les modaux au passé : modal + have + participe passé</h4>
      <p><span class="hl">should have</span> + PP = aurait dû (reproche, regret) : <span class="ex">You should have studied.</span></p>
      <p><span class="hl">must have</span> + PP = a dû (déduction) : <span class="ex">She must have missed the bus.</span></p>
      <p><span class="hl">could have</span> + PP = aurait pu : <span class="ex">You could have called me!</span></p>
      <p><span class="hl">can't have</span> + PP = n'a pas pu : <span class="ex">He can't have finished already.</span></p>''',
  {
    "prob": ("choice", "Choisis le bon modal", [
      C("He has worked all day. He ____ be tired.", ["must", "can't", "might"], tip="déduction presque sûre → must."),
      C("Take an umbrella. It ____ rain later.", ["might", "must", "can't"], tip="possibilité → might / may."),
      C("That ____ be Tom. He's in London today!", ["can't", "must", "may"], tip="impossible → can't."),
      C("I'm not sure. She ____ be at home.", ["may", "must", "can't"], tip="possible → may."),
      C("You've just eaten! You ____ be hungry!", ["can't", "must", "might"], tip="impossible → can't."),
      C("The lights are on. They ____ be at home.", ["must", "can't", "shouldn't"], tip="déduction → must."),
      C("We ____ go to Spain this summer, we haven't decided.", ["might", "must", "can't"], tip="pas sûr → might."),
      C("This ring costs €10! It ____ be real gold.", ["can't", "must", "might"], tip="impossible → can't."),
    ]),
    "past": ("choice", "Choisis le modal au passé", [
      C("You failed the test. You ____ more.", ["should have studied", "must have studied", "can't have studied"], tip="reproche → should have + PP."),
      C("She's late. She ____ the bus.", ["must have missed", "should have missed", "can't have missed"], tip="déduction → must have + PP."),
      C("Why didn't you tell me? You ____ me!", ["could have called", "must have called", "can't have called"], tip="aurait pu → could have + PP."),
      C("He ____ already. He only started 5 minutes ago!", ["can't have finished", "must have finished", "should have finished"], tip="impossible → can't have + PP."),
      C("The ground is wet. It ____ during the night.", ["must have rained", "should have rained", "can't have rained"], tip="déduction → must have + PP."),
      C("I'm sorry, I ____ so rude.", ["shouldn't have been", "mustn't have been", "can't have been"], tip="regret → shouldn't have + PP."),
    ]),
  },
  [M("prob", "🤔", "must, may, might ou can't ?", "Sûr, possible ou impossible ?", ["prob"], 8, G1),
   M("past", "⏪", "should have, must have…", "Regret, déduction ou reproche au passé.", ["past"], 6, G2),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["prob", "past"], 12, "Les deux")])

# ═════════════ VERBES + TO / -ING ═════════════
TO = "want, need, decide, hope, learn, would like, plan, promise, forget + <b>to</b> + BV."
ING = "enjoy, finish, stop, mind, avoid, keep, practise, can't stand + verbe-<b>ing</b>."
newpage("verbes_to_ing.html", "Verbe + to ou -ing – Entraînement", 'want <span>to</span> / enjoy <span>-ing</span>',
  "Verbes suivis de to + BV ou de verbe-ing", ("#fdba74", "#fb923c"),
  '''      <p>Quand deux verbes se suivent, le second est soit à l'<b>infinitif avec to</b>, soit en <b>-ing</b>. Cela dépend du premier verbe.</p>
      <table>
        <tr><th>+ to + BV</th><th>+ verbe-ing</th><th>les deux</th></tr>
        <tr><td>want, need, decide, hope, learn, would like, plan, promise, forget, agree</td><td>enjoy, finish, stop, mind, avoid, keep, practise, can't stand, suggest</td><td>like, love, hate, start, begin</td></tr>
      </table>
      <p class="ex">I want to travel. · She decided to leave. · He enjoys cooking. · Stop talking! · I like reading / I like to read.</p>
      <p>Après une <b>préposition</b>, toujours -ing : <span class="ex">I'm good at drawing. · Thank you for helping me.</span></p>''',
  {
    "choice": ("choice", "to + BV ou -ing ?", [
      C("I want ____ a doctor.", ["to become", "becoming"], tip=TO), C("She enjoys ____ .", ["swimming", "to swim"], tip=ING), C("He decided ____ .", ["to leave", "leaving"], tip=TO),
      C("Stop ____ ! I'm trying to work.", ["talking", "to talk"], tip=ING), C("We hope ____ you soon.", ["to see", "seeing"], tip=TO), C("Have you finished ____ ?", ["eating", "to eat"], tip=ING),
      C("I'd like ____ a coffee, please.", ["to have", "having"], tip="would like + to."), C("Do you mind ____ the window?", ["opening", "to open"], tip=ING),
      C("They learnt ____ at school.", ["to swim", "swimming"], tip=TO), C("You should avoid ____ too much sugar.", ["eating", "to eat"], tip=ING),
      C("I'm good at ____ .", ["drawing", "to draw"], tip="après une préposition (at) → -ing."), C("Don't forget ____ the door!", ["to lock", "locking"], tip=TO),
      C("He keeps ____ the same mistake.", ["making", "to make"], tip=ING), C("Thank you for ____ me.", ["helping", "to help"], tip="après une préposition (for) → -ing."),
    ]),
    "gap": ("gap", "Complète avec to + BV ou verbe-ing", [
      G("I need ____ more.", "to study", "study"), G("She can't stand ____ .", "waiting", "wait"), G("We plan ____ to Italy.", "to go", "go"),
      G("He practises ____ the piano every day.", "playing", "play"), G("They promised ____ early.", "to come", "come"), G("I'm interested in ____ photos.", "taking", "take"),
    ]),
  },
  [M("choice", "⚖️", "to + BV ou -ing ?", "Ça dépend du premier verbe !", ["choice"], 12),
   M("gap", "✍️", "Complète", "to study, waiting…", ["gap"], 6),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["choice", "gap"], 12)])
print("content4 ok", REGISTRY)
