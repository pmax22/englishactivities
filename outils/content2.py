import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
exec(open(_EA_OUT+"/content_helpers.py", encoding="utf-8").read())

# ═════════════ SUPERLATIF ═════════════
newpage("superlatif.html", "Le superlatif – Entraînement", 'Le <span>superlatif</span>',
  "the -est · the most … · the best / the worst", ("#2dd4bf", "#0d9488"),
  '''      <p>Le <span class="hl">superlatif</span> sert à dire qu'un élément est <b>le plus</b> (ou le moins) d'un groupe.</p>
      <table>
        <tr><th>Adjectif</th><th>Règle</th><th>Exemple</th></tr>
        <tr><td>court</td><td><span class="hl">the</span> + adj + <span class="hl">-est</span></td><td>the tallest, the fastest</td></tr>
        <tr><td>long</td><td><span class="hl">the most</span> + adj</td><td>the most expensive</td></tr>
        <tr><td>irrégulier</td><td>good → <span class="hl">the best</span> · bad → <span class="hl">the worst</span></td><td>the best film</td></tr>
      </table>
      <p><b>Orthographe :</b> nice → the nic<b>est</b> · big → the bi<b>ggest</b> · happy → the happ<b>iest</b>.</p>
      <p>Le moins : <span class="hl">the least</span> + adj → <span class="ex">the least expensive</span>. Dans un lieu : <b>in</b> → <span class="ex">the tallest building in the world</span>.</p>
      <p>Rappel comparatif : <span class="ex">taller than</span> (2 éléments) · superlatif : <span class="ex">the tallest</span> (tout le groupe).</p>''',
  {
    "gap": ("gap", "Complète avec le superlatif", [
      G("Everest is ____ mountain in the world.", "the highest", "high", tip="court → the + -est."),
      G("This is ____ dress in the shop.", "the most expensive", "expensive", tip="long → the most + adj."),
      G("It's ____ film of the year!", "the best", "good", tip="good → the best."),
      G("Tom is ____ boy in my class.", "the tallest", "tall", tip="court → the tallest."),
      G("That was ____ day of my life.", "the worst", "bad", tip="bad → the worst."),
      G("The blue whale is ____ animal.", "the biggest", "big", tip="big → biggest (consonne doublée)."),
      G("Maths is ____ subject for me.", "the most difficult", "difficult", tip="long → the most."),
      G("She is ____ person I know.", "the happiest", "happy", tip="-y → -iest."),
      G("This is ____ book in the library.", "the most interesting", "interesting", tip="long → the most."),
      G("July is ____ month of the year.", "the hottest", "hot", tip="hot → hottest."),
      G("Lucas is ____ student in the school.", "the youngest", "young", tip="court → -est."),
      G("It's ____ restaurant in town.", "the nicest", "nice", tip="-e → + st."),
    ]),
    "form": ("choice", "Choisis le bon superlatif", [
      C(None, ["the tallest", "the most tall", "the taller"], big="tall"), C(None, ["the most beautiful", "the beautifulest", "the most beautifulest"], big="beautiful"),
      C(None, ["the best", "the goodest", "the most good"], big="good"), C(None, ["the biggest", "the bigest", "the most big"], big="big"),
      C(None, ["the worst", "the baddest", "the most bad"], big="bad"), C(None, ["the easiest", "the easyest", "the most easy"], big="easy"),
      C(None, ["the most popular", "the popularest", "the more popular"], big="popular"), C(None, ["the hottest", "the hotest", "the most hot"], big="hot"),
      C(None, ["the nicest", "the niceest", "the most nice"], big="nice"), C(None, ["the most dangerous", "the dangerousest", "the dangerest"], big="dangerous"),
    ]),
    "cs": ("choice", "Comparatif ou superlatif ?", [
      C("Tom is ____ than Lucas.", ["taller", "the tallest"], tip="than → comparatif (2 éléments)."),
      C("Tom is ____ boy in the class.", ["the tallest", "taller"], tip="dans tout le groupe → superlatif."),
      C("A car is ____ than a bike.", ["more expensive", "the most expensive"], tip="than → comparatif."),
      C("It's ____ car in the world.", ["the most expensive", "more expensive"], tip="in the world → superlatif."),
      C("My dog is ____ than your cat.", ["bigger", "the biggest"], tip="than → comparatif."),
      C("This is ____ pizza in town!", ["the best", "better"], tip="in town → superlatif."),
      C("English is ____ than Maths for me.", ["easier", "the easiest"], tip="than → comparatif."),
      C("She is ____ singer in the world.", ["the worst", "worse"], tip="in the world → superlatif."),
    ]),
    "order": ("order", "Remets les mots dans l'ordre", [
      O("It's|the|biggest|city|in France.", fr="C'est la plus grande ville de France.", trap="more"),
      O("She is|the|most|famous|singer.", fr="C'est la chanteuse la plus célèbre.", trap="than"),
      O("This is|the|best|day|of my life!", fr="C'est le meilleur jour de ma vie !", trap="goodest"),
      O("He is|the|youngest|in the family.", fr="C'est le plus jeune de la famille.", trap="most"),
      O("It's|the|most|expensive|bag|in the shop.", fr="C'est le sac le plus cher du magasin.", trap="expensivest"),
    ]),
  },
  [M("gap", "✍️", "Complète", "the -est, the most… ou irrégulier ?", ["gap"]),
   M("form", "📏", "Court ou long ?", "Choisis la bonne forme du superlatif.", ["form"]),
   M("cs", "⚖️", "Comparatif ou superlatif ?", "taller than ou the tallest ?", ["cs"], 8),
   M("order", "🧩", "Remets dans l'ordre", "Construis la phrase. Attention au piège !", ["order"], 5),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["gap", "form", "cs", "order"], 12)])

# ═════════════ MODAUX ═════════════
newpage("modaux.html", "Les modaux – Entraînement", 'Les <span>modaux</span>',
  "can · must · should · have to", ("#818cf8", "#4f46e5"),
  '''      <table>
        <tr><th>Modal</th><th>Sens</th><th>Exemple</th></tr>
        <tr><td><span class="hl">can</span> / can't</td><td>capacité, permission</td><td>I can swim. · Can I go out?</td></tr>
        <tr><td><span class="hl">must</span></td><td>obligation (forte, personnelle)</td><td>You must wear a helmet.</td></tr>
        <tr><td><span class="hl">mustn't</span></td><td><b>interdiction</b></td><td>You mustn't smoke here.</td></tr>
        <tr><td><span class="hl">should</span> / shouldn't</td><td>conseil</td><td>You should sleep more.</td></tr>
        <tr><td><span class="hl">have to</span> / has to</td><td>obligation (règle extérieure)</td><td>She has to wear a uniform.</td></tr>
        <tr><td><span class="hl">don't have to</span></td><td><b>absence d'obligation</b></td><td>You don't have to come.</td></tr>
      </table>
      <p>can, must, should : <b>même forme</b> pour toutes les personnes, suivis de la <b>base verbale sans to</b>. <span class="ex">He can swim. <s>He cans swim. He can to swim.</s></span></p>
      <p>Attention : <b>mustn't</b> = c'est interdit · <b>don't have to</b> = ce n'est pas obligatoire.</p>''',
  {
    "meaning": ("choice", "Choisis le bon modal", [
      C("You ____ smoke here. It's forbidden.", ["mustn't", "don't have to", "can"], tip="interdiction → mustn't."),
      C("Tomorrow is Sunday: I ____ get up early.", ["don't have to", "mustn't", "can't"], tip="pas obligatoire → don't have to."),
      C("You look tired. You ____ go to bed.", ["should", "can", "mustn't"], tip="conseil → should."),
      C("My little brother ____ read. He's only three.", ["can't", "mustn't", "shouldn't"], tip="incapacité → can't."),
      C("____ I open the window, please?", ["Can", "Must", "Should"], tip="demander la permission → Can."),
      C("In France, you ____ drive on the right.", ["have to", "can", "should"], tip="règle → have to."),
      C("You ____ eat so many sweets. It's bad for you.", ["shouldn't", "can't", "don't have to"], tip="conseil négatif → shouldn't."),
      C("She ____ speak three languages!", ["can", "must", "has to"], tip="capacité → can."),
      C("Students ____ use their phones in class.", ["mustn't", "don't have to", "should"], tip="interdiction → mustn't."),
      C("It's free! You ____ pay.", ["don't have to", "mustn't", "can't"], tip="pas obligatoire → don't have to."),
      C("You ____ wear a helmet on a motorbike. It's the law.", ["must", "can", "should"], tip="obligation → must."),
      C("If you're ill, you ____ see a doctor.", ["should", "can't", "mustn't"], tip="conseil → should."),
    ]),
    "form": ("choice", "Quelle phrase est correcte ?", [
      C(None, ["He can swim.", "He cans swim.", "He can to swim."], tip="modal : même forme + BV sans to."),
      C(None, ["She should rest.", "She shoulds rest.", "She should resting."], tip="should + BV."),
      C(None, ["Can you help me?", "Do you can help me?", "You can help me?"], tip="question : Can + sujet + BV ?"),
      C(None, ["You mustn't run.", "You don't must run.", "You mustn't to run."], tip="négatif : mustn't + BV."),
      C(None, ["He has to work.", "He have to work.", "He has work."], tip="he → has to + BV."),
      C(None, ["Does she have to go?", "Has she to go?", "Does she has to go?"], tip="question : Does + sujet + have to + BV ?"),
      C(None, ["I can't come.", "I don't can come.", "I can't to come."], tip="négatif : can't + BV."),
      C(None, ["They should study.", "They should to study.", "They should studying."], tip="should + BV."),
    ]),
    "gap": ("gap", "Complète avec le modal qui convient", [
      G("I ____ play the guitar.", ["can"], "capacité", tip="capacité → can."),
      G("You ____ touch that! It's dangerous.", ["mustn't", "must not"], "interdiction", tip="interdiction → mustn't."),
      G("You ____ see this film. It's great!", ["should"], "conseil", tip="conseil → should."),
      G("She ____ wear a uniform at school.", ["has to"], "obligation (règle)", tip="règle → has to."),
      G("We ____ hurry. We have time.", ["don't have to", "do not have to"], "pas obligatoire", tip="absence d'obligation → don't have to."),
      G("____ I borrow your pen?", ["Can"], "permission", tip="permission → Can."),
      G("He ____ swim. He never learnt.", ["can't", "cannot"], "incapacité", tip="incapacité → can't."),
      G("You ____ go to bed so late.", ["shouldn't", "should not"], "conseil négatif", tip="conseil négatif → shouldn't."),
    ]),
  },
  [M("meaning", "🎯", "Choisis le bon modal", "Capacité, obligation, interdiction ou conseil ?", ["meaning"]),
   M("gap", "✍️", "Complète", "Le sens est donné entre parenthèses.", ["gap"], 8),
   M("form", "🔎", "Quelle phrase est correcte ?", "can + BV sans to, pas de -s…", ["form"], 8),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["meaning", "gap", "form"], 12)])

# ═════════════ THERE IS / THERE ARE ═════════════
newpage("there_is.html", "There is / There are – Entraînement", 'There <span>is</span> / There <span>are</span>',
  "Il y a … · some / any", ("#fbbf24", "#d97706"),
  '''      <p><span class="hl">There is / There are</span> = il y a.</p>
      <table>
        <tr><th></th><th>Singulier / indénombrable</th><th>Pluriel</th></tr>
        <tr><td><b>+</b></td><td>There <span class="hl">is</span> a cat. · There is some milk.</td><td>There <span class="hl">are</span> some apples.</td></tr>
        <tr><td><b>−</b></td><td>There <span class="hl">isn't</span> a cat. · There isn't any milk.</td><td>There <span class="hl">aren't</span> any apples.</td></tr>
        <tr><td><b>?</b></td><td><span class="hl">Is there</span> a cat? · Is there any milk?</td><td><span class="hl">Are there</span> any apples?</td></tr>
      </table>
      <p><b>some</b> (des, du, de la) → phrases <b>affirmatives</b> · <b>any</b> → phrases <b>négatives</b> et <b>questions</b>.</p>
      <p>Au passé : <span class="ex">There was a cat. · There were some apples.</span></p>''',
  {
    "isare": ("choice", "is ou are ?", [
      C("There ____ a cat in the garden.", ["is", "are"], keep=True, tip="a cat = singulier → is."), C("There ____ two books on the table.", ["are", "is"], tip="two books = pluriel → are."),
      C("There ____ some milk in the fridge.", ["is", "are"], keep=True, tip="milk = indénombrable → is."), C("There ____ some students in the classroom.", ["are", "is"], tip="pluriel → are."),
      C("There ____ a lot of people here.", ["are", "is"], tip="people = pluriel → are."), C("There ____ an apple in my bag.", ["is", "are"], keep=True, tip="singulier → is."),
      C("____ there any shops near here?", ["Are", "Is"], tip="shops = pluriel → Are there."), C("____ there a bank in this street?", ["Is", "Are"], keep=True, tip="a bank = singulier → Is there."),
      C("There ____ any bread left.", ["isn't", "aren't"], keep=True, tip="bread = indénombrable → isn't."), C("There ____ any chairs in the room.", ["aren't", "isn't"], tip="pluriel → aren't."),
    ]),
    "someany": ("choice", "some ou any ?", [
      C("There are ____ apples on the table.", ["some", "any"], keep=True, tip="affirmatif → some."), C("There aren't ____ eggs.", ["any", "some"], tip="négatif → any."),
      C("Is there ____ water?", ["any", "some"], tip="question → any."), C("I'd like ____ tea, please.", ["some", "any"], keep=True, tip="affirmatif (offre, demande) → some."),
      C("We don't have ____ money.", ["any", "some"], tip="négatif → any."), C("There is ____ cheese in the fridge.", ["some", "any"], keep=True, tip="affirmatif → some."),
      C("Are there ____ good films on TV?", ["any", "some"], tip="question → any."), C("She bought ____ flowers.", ["some", "any"], keep=True, tip="affirmatif → some."),
    ]),
    "gap": ("gap", "Complète la phrase", [
      G("____ a big park in my town.", ["There is", "There's"], "il y a", tip="singulier → There is."),
      G("____ twenty students in my class.", ["There are"], "il y a", tip="pluriel → There are."),
      G("____ any milk?", ["Is there"], "est-ce qu'il y a", tip="question + indénombrable → Is there."),
      G("____ any cinemas in your village?", ["Are there"], "est-ce qu'il y a", tip="question + pluriel → Are there."),
      G("____ any sugar.", ["There isn't", "There is not"], "il n'y a pas", tip="négatif + indénombrable → There isn't."),
      G("____ any trains today.", ["There aren't", "There are not"], "il n'y a pas", tip="négatif + pluriel → There aren't."),
      G("____ a lot of cars yesterday.", ["There were"], "il y avait", tip="passé + pluriel → There were."),
      G("____ a storm last night.", ["There was"], "il y avait", tip="passé + singulier → There was."),
    ]),
    "order": ("order", "Remets les mots dans l'ordre", [
      O("There are|some|apples|on the table.", fr="Il y a des pommes sur la table.", trap="any"),
      O("There isn't|any|milk.", fr="Il n'y a pas de lait.", trap="some"),
      O("Is there|a bakery|near here?", fr="Est-ce qu'il y a une boulangerie près d'ici ?", trap="Are there"),
      O("Are there|any|students|in the room?", fr="Est-ce qu'il y a des élèves dans la salle ?", trap="some"),
      O("There is|a cat|in the garden.", fr="Il y a un chat dans le jardin.", trap="There are"),
    ]),
  },
  [M("isare", "⚖️", "is ou are ?", "Singulier, pluriel ou indénombrable ?", ["isare"]),
   M("someany", "🔀", "some ou any ?", "Affirmatif, négatif ou question ?", ["someany"], 8),
   M("gap", "✍️", "Complète", "There is, There are, Is there…?", ["gap"], 8),
   M("order", "🧩", "Remets dans l'ordre", "Construis la phrase. Attention au piège !", ["order"], 5),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["isare", "someany", "gap", "order"], 12)])

# ═════════════ POSSESSIFS ═════════════
newpage("possessifs.html", "Les possessifs – Entraînement", 'Les <span>possessifs</span>',
  "my, your, his, her… · Tom's bike · mine, yours…", ("#fb7185", "#e11d48"),
  '''      <table>
        <tr><th>Sujet</th><th>Adjectif possessif</th><th>Pronom possessif</th></tr>
        <tr><td>I</td><td>my</td><td>mine</td></tr><tr><td>you</td><td>your</td><td>yours</td></tr>
        <tr><td>he</td><td>his</td><td>his</td></tr><tr><td>she</td><td>her</td><td>hers</td></tr>
        <tr><td>it</td><td>its</td><td>—</td></tr><tr><td>we</td><td>our</td><td>ours</td></tr><tr><td>they</td><td>their</td><td>theirs</td></tr>
      </table>
      <p><b>his ou her ?</b> En anglais, on regarde le <b>possesseur</b> (pas l'objet) : <span class="ex">Tom and his sister · Emma and her brother</span>.</p>
      <p>L'adjectif possessif est suivi d'un nom : <span class="ex">This is my bag.</span> Le pronom possessif le remplace : <span class="ex">This bag is mine.</span></p>
      <h4>Le cas possessif 's</h4>
      <p>possesseur + <span class="hl">'s</span> + objet : <span class="ex">le vélo de Tom → Tom's bike</span> · au pluriel en -s : <span class="ex">my parents' car</span>.</p>''',
  {
    "adj": ("gap", "Complète avec l'adjectif possessif", [
      G("Tom loves ____ dog.", "his", "Tom", tip="possesseur : Tom → his."), G("Emma is with ____ brother.", "her", "Emma", tip="possesseur : Emma → her."),
      G("We visit ____ grandparents on Sundays.", "our", "we", tip="we → our."), G("They sold ____ house.", "their", "they", tip="they → their."),
      G("I can't find ____ keys.", "my", "I", tip="I → my."), G("Is this ____ pen?", "your", "you", tip="you → your."),
      G("The cat is eating ____ food.", "its", "the cat", tip="animal / chose → its."), G("Lucas and ____ sister are twins.", "his", "Lucas", tip="Lucas → his."),
      G("My mother loves ____ job.", "her", "my mother", tip="my mother → her."), G("The children are playing with ____ toys.", "their", "the children", tip="they → their."),
    ]),
    "hishers": ("choice", "his ou her ?", [
      C("Paul and ____ mother.", ["his", "her"], keep=True, tip="possesseur : Paul (garçon) → his."), C("Sarah and ____ father.", ["her", "his"], tip="possesseur : Sarah → her."),
      C("My dad and ____ car.", ["his", "her"], keep=True, tip="possesseur : my dad → his."), C("Léa is wearing ____ new shoes.", ["her", "his"], tip="possesseur : Léa → her."),
      C("Tom is talking to ____ sister.", ["his", "her"], keep=True, tip="possesseur : Tom → his."), C("Emma and ____ boyfriend.", ["her", "his"], tip="possesseur : Emma → her."),
    ]),
    "gen": ("order", "Construis le groupe avec 's", [
      O("Tom's|bike", fr="le vélo de Tom", trap="the"), O("my sister's|room", fr="la chambre de ma sœur", trap="of"),
      O("Emma's|dog", fr="le chien d'Emma", trap="the"), O("my parents'|car", fr="la voiture de mes parents", trap="of"),
      O("the teacher's|desk", fr="le bureau du professeur", trap="of"), O("Lucas's|phone", fr="le téléphone de Lucas", alts=["Lucas' phone"], trap="the"),
    ]),
    "pron": ("choice", "Choisis le pronom possessif", [
      C("This book is ____ .", ["mine", "my", "me"], fr="Ce livre est à moi.", tip="à moi → mine."),
      C("Is this bag ____ ?", ["yours", "your", "you"], fr="Ce sac est à toi ?", tip="à toi → yours."),
      C("The red car is ____ .", ["his", "him", "he's"], fr="La voiture rouge est à lui.", tip="à lui → his."),
      C("This phone is ____ .", ["hers", "her", "she"], fr="Ce téléphone est à elle.", tip="à elle → hers."),
      C("The house is ____ .", ["ours", "our", "us"], fr="La maison est à nous.", tip="à nous → ours."),
      C("These shoes are ____ .", ["theirs", "their", "them"], fr="Ces chaussures sont à eux.", tip="à eux → theirs."),
    ]),
  },
  [M("adj", "✍️", "my, your, his, her…", "Complète avec l'adjectif possessif.", ["adj"]),
   M("hishers", "⚖️", "his ou her ?", "Regarde le possesseur !", ["hishers"], 6),
   M("gen", "🧩", "Le cas possessif 's", "le vélo de Tom → Tom's bike.", ["gen"], 6),
   M("pron", "🎯", "mine, yours, his…", "Les pronoms possessifs.", ["pron"], 6),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["adj", "hishers", "gen", "pron"], 12)])

# ═════════════ PRÉPOSITIONS ═════════════
T = "Temps : <b>at</b> + heure / moment précis · <b>on</b> + jour, date · <b>in</b> + mois, saison, année, partie de la journée."
P = "Lieu : <b>in</b> = dans (espace fermé, ville, pays) · <b>on</b> = sur (surface) · <b>at</b> = à (un point précis : at school, at home)."
newpage("prepositions.html", "in / on / at – Entraînement", '<span>in</span> · <span>on</span> · <span>at</span>',
  "Les prépositions de temps et de lieu", ("#34d399", "#059669"),
  '''      <h4>Le temps</h4>
      <table>
        <tr><th>at</th><th>on</th><th>in</th></tr>
        <tr><td>heure, moment précis<br><i>at 7 o'clock, at noon, at night, at Christmas</i></td><td>jour, date<br><i>on Monday, on 3rd May, on my birthday</i></td><td>mois, saison, année, partie de la journée<br><i>in July, in winter, in 2025, in the morning</i></td></tr>
      </table>
      <h4>Le lieu</h4>
      <table>
        <tr><th>at</th><th>on</th><th>in</th></tr>
        <tr><td>un point précis<br><i>at school, at home, at the bus stop</i></td><td>une surface<br><i>on the table, on the wall, on the floor</i></td><td>à l'intérieur, ville, pays<br><i>in the box, in Paris, in France</i></td></tr>
      </table>''',
  {
    "time": ("choice", "in, on ou at ? (le temps)", [
      C("The film starts ____ 8 o'clock.", ["at", "on", "in"], keep=True, tip=T), C("My birthday is ____ May.", ["in", "on", "at"], keep=True, tip=T),
      C("We have English ____ Monday.", ["on", "in", "at"], keep=True, tip=T), C("I was born ____ 2012.", ["in", "on", "at"], keep=True, tip=T),
      C("It's cold ____ winter.", ["in", "on", "at"], keep=True, tip=T), C("I get up ____ 7 am.", ["at", "in", "on"], keep=True, tip=T),
      C("See you ____ Friday!", ["on", "at", "in"], keep=True, tip=T), C("I do my homework ____ the evening.", ["in", "at", "on"], keep=True, tip=T),
      C("The shop is closed ____ Christmas Day.", ["on", "at", "in"], keep=True, tip="jour précis (Christmas Day) → on."), C("Owls sleep during the day and hunt ____ night.", ["at", "in", "on"], keep=True, tip="at night (expression)."),
      C("School finishes ____ July.", ["in", "on", "at"], keep=True, tip=T), C("We eat ____ noon.", ["at", "on", "in"], keep=True, tip=T),
    ]),
    "place": ("choice", "in, on ou at ? (le lieu)", [
      C("The keys are ____ the table.", ["on", "in", "at"], keep=True, tip=P), C("She lives ____ Paris.", ["in", "at", "on"], keep=True, tip=P),
      C("I'm ____ school.", ["at", "in", "on"], keep=True, tip=P), C("The cat is ____ the box.", ["in", "on", "at"], keep=True, tip=P),
      C("There's a poster ____ the wall.", ["on", "in", "at"], keep=True, tip=P), C("My parents are ____ home.", ["at", "in", "on"], keep=True, tip=P),
      C("We live ____ France.", ["in", "at", "on"], keep=True, tip=P), C("Wait for me ____ the bus stop.", ["at", "in", "on"], keep=True, tip=P),
      C("Your book is ____ your bag.", ["in", "on", "at"], keep=True, tip=P), C("The plates are ____ the floor!", ["on", "in", "at"], keep=True, tip=P),
    ]),
  },
  [M("time", "🕒", "Le temps", "at 7 o'clock, on Monday, in July…", ["time"]),
   M("place", "📍", "Le lieu", "at school, on the table, in Paris…", ["place"]),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["time", "place"], 12)])

# ═════════════ HEURE, DATES, NOMBRES ═════════════
newpage("heure_dates.html", "Heure, dates et nombres – Entraînement", "L'heure, les <span>dates</span> et les nombres",
  "What time is it? · the third of May · fifteen / fifty", ("#93c5fd", "#3b82f6"),
  '''      <h4>L'heure</h4>
      <table>
        <tr><th>7:00</th><th>7:15</th><th>7:30</th><th>7:45</th><th>7:10</th><th>7:50</th></tr>
        <tr><td>seven o'clock</td><td>(a) quarter past seven</td><td>half past seven</td><td>(a) quarter to eight</td><td>ten past seven</td><td>ten to eight</td></tr>
      </table>
      <p><b>past</b> = et (jusqu'à la demie) · <b>to</b> = moins (après la demie). On peut aussi dire simplement <i>seven fifteen, seven thirty</i>. Am = le matin, pm = l'après-midi / le soir.</p>
      <h4>Les dates</h4>
      <p>On utilise les nombres <b>ordinaux</b> : 1st <b>first</b> · 2nd <b>second</b> · 3rd <b>third</b> · 4th fourth · 5th <b>fifth</b> · 12th <b>twelfth</b> · 20th <b>twentieth</b> · 21st twenty-first</p>
      <p class="ex">le 3 mai → the third of May (écrit : 3rd May / May 3rd). Les mois prennent une majuscule.</p>
      <h4>Les nombres</h4>
      <p>Attention : 13 thir<b>teen</b> / 30 thir<b>ty</b> · 15 fif<b>teen</b> / 50 fif<b>ty</b>. 100 = a hundred · 1,000 = a thousand. Prix : £3.50 = three pounds fifty.</p>''',
  {
    "time": ("choice", "What time is it?", [
      C(None, ["half past seven", "half to seven", "seven and half"], big="7:30", keep=False, tip="30 → half past."),
      C(None, ["a quarter past three", "a quarter to three", "three and quarter"], big="3:15", tip="15 → a quarter past."),
      C(None, ["a quarter to nine", "a quarter past nine", "a quarter to eight"], big="8:45", tip="45 → a quarter to + l'heure suivante."),
      C(None, ["ten past four", "ten to four", "four past ten"], big="4:10", tip="10 → ten past."),
      C(None, ["twenty to six", "twenty past six", "twenty to five"], big="5:40", tip="40 → twenty to + l'heure suivante."),
      C(None, ["eleven o'clock", "eleven hours", "o'clock eleven"], big="11:00", tip="heure pile → o'clock."),
      C(None, ["five to twelve", "five past twelve", "five to eleven"], big="11:55", tip="55 → five to + l'heure suivante."),
      C(None, ["twenty-five past two", "twenty-five to two", "two and twenty-five"], big="2:25", tip="25 → twenty-five past."),
    ]),
    "ord": ("gap", "Écris le nombre ordinal en lettres", [
      G("____", "first", "1st", tip="1st → first."), G("____", "second", "2nd", tip="2nd → second."), G("____", "third", "3rd", tip="3rd → third."),
      G("____", "fifth", "5th", tip="5th → fifth (ve → f)."), G("____", "twelfth", "12th", tip="12th → twelfth."), G("____", "twentieth", "20th", tip="20th → twentieth (y → ie)."),
      G("____", ["twenty-first", "twenty first"], "21st", tip="21st → twenty-first."), G("____", "ninth", "9th", tip="9th → ninth (pas de e)."),
      G("____", "fourth", "4th", tip="4th → fourth."), G("____", ["thirty-first", "thirty first"], "31st", tip="31st → thirty-first."),
    ]),
    "date": ("choice", "Comment dit-on cette date ?", [
      C(None, ["the third of May", "the three of May", "May the three"], big="le 3 mai", tip="date → nombre ordinal : third."),
      C(None, ["the first of January", "the one of January", "the first January of"], big="le 1er janvier", tip="first."),
      C(None, ["the fourteenth of July", "the fourteen of July", "the fourth of July"], big="le 14 juillet", tip="fourteenth."),
      C(None, ["the twenty-fifth of December", "the twenty-five of December", "the twentieth-fifth of December"], big="le 25 décembre", tip="twenty-fifth."),
      C(None, ["the second of October", "the two of October", "the twice of October"], big="le 2 octobre", tip="second."),
      C(None, ["the thirty-first of August", "the thirty-one of August", "the thirteenth of August"], big="le 31 août", tip="thirty-first."),
    ]),
    "num": ("choice", "Choisis le bon nombre", [
      C(None, ["fifteen", "fifty", "five-teen"], big="15", tip="15 = fifteen · 50 = fifty."), C(None, ["fifty", "fifteen", "five-ty"], big="50", tip="50 = fifty."),
      C(None, ["thirteen", "thirty", "three-teen"], big="13", tip="13 = thirteen."), C(None, ["thirty", "thirteen", "threety"], big="30", tip="30 = thirty."),
      C(None, ["forty", "fourty", "fourteen"], big="40", tip="40 = forty (pas de u !)."), C(None, ["a hundred and twenty", "one hundred twenty and", "a hundred twenty"], big="120", tip="120 = a hundred and twenty."),
      C(None, ["three pounds fifty", "three fifty pounds", "pounds three fifty"], big="£3.50", tip="£3.50 = three pounds fifty."),
      C(None, ["twelve euros ninety-nine", "twelve ninety-nine euros", "euros twelve ninety-nine"], big="12,99 €", tip="12,99 € = twelve euros ninety-nine."),
    ]),
  },
  [M("time", "🕒", "What time is it?", "past, to, half, quarter…", ["time"], 8),
   M("ord", "🔢", "Les nombres ordinaux", "first, second, third…", ["ord"]),
   M("date", "📅", "Les dates", "le 3 mai → the third of May.", ["date"], 6),
   M("num", "💶", "Nombres et prix", "fifteen ou fifty ? £3.50…", ["num"], 8),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["time", "ord", "date", "num"], 12)])

# ═════════════ DÉNOMBRABLES ═════════════
newpage("denombrables.html", "Dénombrables et indénombrables – Entraînement", 'much, <span>many</span>, a lot of',
  "Dénombrables et indénombrables", ("#c4b5fd", "#8b5cf6"),
  '''      <p>Un nom <span class="hl">dénombrable</span> se compte : <i>an apple, two apples</i>. Un nom <span class="hl">indénombrable</span> ne se compte pas et n'a pas de pluriel : <i>water, money, bread, information, homework, advice</i>.</p>
      <table>
        <tr><th></th><th>Dénombrable (pluriel)</th><th>Indénombrable</th></tr>
        <tr><td>beaucoup (−, ?)</td><td><span class="hl">many</span> apples</td><td><span class="hl">much</span> water</td></tr>
        <tr><td>beaucoup (+)</td><td colspan="2"><span class="hl">a lot of</span> apples / a lot of water</td></tr>
        <tr><td>combien ?</td><td><span class="hl">How many</span> apples?</td><td><span class="hl">How much</span> water? · How much is it? (prix)</td></tr>
        <tr><td>un peu de / quelques</td><td><span class="hl">a few</span> apples</td><td><span class="hl">a little</span> water</td></tr>
      </table>
      <p>Pièges : <i>money, bread, homework, information, furniture, hair</i> sont indénombrables : <span class="ex">much money <s>many moneys</s></span>.</p>''',
  {
    "cnt": ("choice", "Dénombrable ou indénombrable ?", [
      C(None, ["dénombrable", "indénombrable"], big="apple", keep=True, tip="an apple, two apples."), C(None, ["indénombrable", "dénombrable"], big="water", tip="on ne compte pas l'eau."),
      C(None, ["indénombrable", "dénombrable"], big="money", tip="money est indénombrable (on compte les euros, pas « les argents »)."),
      C(None, ["dénombrable", "indénombrable"], big="chair", keep=True, tip="a chair, three chairs."), C(None, ["indénombrable", "dénombrable"], big="bread", tip="bread est indénombrable."),
      C(None, ["indénombrable", "dénombrable"], big="homework", tip="homework est indénombrable (pas de s)."), C(None, ["dénombrable", "indénombrable"], big="egg", keep=True, tip="an egg, six eggs."),
      C(None, ["indénombrable", "dénombrable"], big="information", tip="information est indénombrable (pas de s)."), C(None, ["dénombrable", "indénombrable"], big="friend", keep=True, tip="a friend, two friends."),
      C(None, ["indénombrable", "dénombrable"], big="milk", tip="milk est indénombrable."),
    ]),
    "much": ("choice", "much ou many ?", [
      C("How ____ apples do you want?", ["many", "much"], tip="apples = dénombrable → many."), C("How ____ water do you drink?", ["much", "many"], tip="water = indénombrable → much."),
      C("I don't have ____ money.", ["much", "many"], tip="money = indénombrable → much."), C("There aren't ____ students today.", ["many", "much"], tip="students = dénombrable → many."),
      C("How ____ is this T-shirt?", ["much", "many"], tip="prix → How much."), C("Did you take ____ photos?", ["many", "much"], tip="photos = dénombrable → many."),
      C("We haven't got ____ time.", ["much", "many"], tip="time = indénombrable → much."), C("How ____ brothers have you got?", ["many", "much"], tip="brothers = dénombrable → many."),
      C("She doesn't eat ____ bread.", ["much", "many"], tip="bread = indénombrable → much."), C("How ____ homework do you have?", ["much", "many"], tip="homework = indénombrable → much."),
    ]),
    "few": ("choice", "a few ou a little ?", [
      C("I have ____ friends in London.", ["a few", "a little"], tip="friends = dénombrable → a few."), C("Can I have ____ milk, please?", ["a little", "a few"], tip="milk = indénombrable → a little."),
      C("Wait ____ minutes.", ["a few", "a little"], tip="minutes = dénombrable → a few."), C("I speak ____ Spanish.", ["a little", "a few"], tip="Spanish = indénombrable → a little."),
      C("There are ____ apples left.", ["a few", "a little"], tip="apples → a few."), C("Add ____ salt.", ["a little", "a few"], tip="salt → a little."),
    ]),
  },
  [M("cnt", "🔢", "Dénombrable ou pas ?", "Peut-on le compter ?", ["cnt"]),
   M("much", "⚖️", "much ou many ?", "How much / How many…", ["much"]),
   M("few", "🤏", "a few ou a little ?", "Quelques / un peu de.", ["few"], 6),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["cnt", "much", "few"], 12)])
print("content2 ok", REGISTRY)
