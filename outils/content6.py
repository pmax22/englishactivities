import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
exec(open(_EA_OUT+"/content_helpers.py", encoding="utf-8").read())

def V(em, fr, en, *wrong):  # vocabulaire : français → anglais
    return C(None, [en, *wrong], big=(em + " " if em else "") + fr, tip=f"{fr} = <b>{en}</b>")
def S(em, fr, en, alts=()):  # orthographe : écrire le mot
    return G("____", [en, *alts], big=(em + " " if em else "") + fr, tip=f"{fr} = <b>{en}</b>", w=260)
def L(en, fr, *wrong):  # écoute : anglais entendu → français
    return C(None, [fr, *wrong], say=en, listen=True, tip=f"{en} = <b>{fr}</b>")
def lex(file, title, h1, sub, colors, lesson, vocab, spell, listen, extra=None, extra_m=None, tag="Anglais · Lexique"):
    data = {"vocab": ("choice", "Quel est le mot anglais ?", vocab), "spell": ("gap", "Écris le mot en anglais", spell),
            "listen": ("choice", "Écoute : que veut dire ce mot ?", listen)}
    ms = [M("vocab", "📖", "Le vocabulaire", "Trouve le mot anglais.", ["vocab"]),
          M("spell", "✍️", "Écris le mot", "Attention à l'orthographe !", ["spell"]),
          M("listen", "🔊", "Écoute et comprends", "Écoute le mot et trouve sa traduction.", ["listen"], 8)]
    if extra:
        data.update(extra); ms += extra_m
    ms.append(M("mix", "🎲", "Tout mélangé", "Le grand test !", list(data.keys()), 12))
    newpage(file, title, h1, sub, colors, lesson, data, ms, tag=tag)

# ═════════════ SE PRÉSENTER ═════════════
newpage("se_presenter.html", "Se présenter – Entraînement", 'Hello, <span>my name is…</span>',
  "Se présenter et poser des questions à quelqu'un", ("#fde047", "#facc15"),
  '''      <table>
        <tr><th>Question</th><th>Réponse</th></tr>
        <tr><td>What's your name?</td><td>My name is Léa. / I'm Léa.</td></tr>
        <tr><td>How old are you?</td><td>I'm 15 (years old).</td></tr>
        <tr><td>Where do you live?</td><td>I live in Lyon.</td></tr>
        <tr><td>Where are you from?</td><td>I'm from France. / I'm French.</td></tr>
        <tr><td>When is your birthday?</td><td>It's on the 3rd of May.</td></tr>
        <tr><td>Have you got any brothers or sisters?</td><td>Yes, I've got a brother. / No, I'm an only child.</td></tr>
        <tr><td>What do you like?</td><td>I like football and music.</td></tr>
        <tr><td>What do you do?</td><td>I'm a student. I'm in CAP Sapver.</td></tr>
      </table>
      <p>Attention : l'âge se dit avec <b>be</b> : <span class="ex">I am 15. <s>I have 15.</s></span></p>''',
  {
    "qa": ("choice", "Quelle est la bonne réponse ?", [
      C("What's your name?", ["My name is Tom.", "I'm 15.", "I live in Paris."]), C("How old are you?", ["I'm 16.", "I have 16.", "I'm fine."], tip="l'âge → be : I'm 16."),
      C("Where do you live?", ["I live in Nantes.", "I'm French.", "I'm fine, thanks."]), C("Where are you from?", ["I'm from Spain.", "I'm 14.", "I like music."]),
      C("Have you got any brothers or sisters?", ["Yes, I've got a sister.", "Yes, I am.", "I'm a student."]), C("What do you like?", ["I like dancing.", "I'm Emma.", "On Monday."]),
      C("When is your birthday?", ["It's on the 12th of July.", "I'm 15.", "It's in Lyon."]), C("How are you?", ["I'm fine, thanks.", "I'm 15.", "I'm from Italy."]),
    ]),
    "q": ("choice", "Quelle question faut-il poser ?", [
      C(None, ["How old are you?", "How are you?", "What's your age old?"], fr="Tu veux connaître l'âge de quelqu'un."),
      C(None, ["Where do you live?", "Where are you from?", "Where you live?"], fr="Tu veux savoir dans quelle ville il habite."),
      C(None, ["What's your name?", "How do you call?", "What name you have?"], fr="Tu veux connaître son prénom."),
      C(None, ["Where are you from?", "Where do you live?", "From where you are?"], fr="Tu veux savoir de quel pays il vient."),
      C(None, ["What do you like?", "What do you do?", "What you like?"], fr="Tu veux connaître ses goûts."),
    ]),
    "gap": ("gap", "Complète la présentation", [
      G("My name ____ Lucas.", "is", tip="My name is…"), G("I ____ 15 years old.", ["am", "'m"], tip="l'âge → I am."), G("I ____ in Marseille.", "live", tip="I live in…"),
      G("I'm ____ France.", "from", tip="I'm from + pays."), G("I've ____ two brothers.", "got", tip="I've got…"), G("I ____ playing video games.", ["like", "love", "enjoy"], tip="like + -ing."),
    ]),
  },
  [M("qa", "💬", "Question → réponse", "Trouve la bonne réponse.", ["qa"], 8),
   M("q", "❓", "Quelle question poser ?", "Pose la bonne question.", ["q"], 5),
   M("gap", "✍️", "Complète la présentation", "is, am, live, from, got…", ["gap"], 6),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["qa", "q", "gap"], 12)], tag="Anglais · Lexique")

# ═════════════ FAMILLE ═════════════
lex("famille.html", "La famille – Entraînement", 'La <span>famille</span>', "Family members", ("#fda4af", "#fb7185"),
  '''      <table>
        <tr><th>Français</th><th>Anglais</th><th>Français</th><th>Anglais</th></tr>
        <tr><td>la mère</td><td>mother (mum)</td><td>le père</td><td>father (dad)</td></tr>
        <tr><td>les parents</td><td>parents</td><td>l'enfant</td><td>child (children)</td></tr>
        <tr><td>la sœur</td><td>sister</td><td>le frère</td><td>brother</td></tr>
        <tr><td>la grand-mère</td><td>grandmother (grandma)</td><td>le grand-père</td><td>grandfather (grandpa)</td></tr>
        <tr><td>la tante</td><td>aunt</td><td>l'oncle</td><td>uncle</td></tr>
        <tr><td>la cousine / le cousin</td><td>cousin</td><td>la fille / le fils</td><td>daughter / son</td></tr>
        <tr><td>la nièce</td><td>niece</td><td>le neveu</td><td>nephew</td></tr>
        <tr><td>la femme (épouse)</td><td>wife</td><td>le mari</td><td>husband</td></tr>
      </table>
      <p>Attention : <b>parents</b> = père et mère seulement (les « parents » au sens de famille = <b>relatives</b>).</p>''',
  [V("", "la tante", "aunt", "uncle", "niece"), V("", "le neveu", "nephew", "niece", "cousin"), V("", "la fille (de quelqu'un)", "daughter", "son", "girl friend"),
   V("", "le mari", "husband", "wife", "brother"), V("", "les grands-parents", "grandparents", "big parents", "great parents"), V("", "le fils", "son", "sun", "daughter"),
   V("", "la femme (épouse)", "wife", "woman", "husband"), V("", "le cousin", "cousin", "nephew", "uncle"), V("", "la nièce", "niece", "nephew", "aunt"), V("", "l'oncle", "uncle", "aunt", "grandfather")],
  [S("", "la mère", "mother", ("mum",)), S("", "le frère", "brother"), S("", "la sœur", "sister"), S("", "la tante", "aunt"), S("", "l'oncle", "uncle"),
   S("", "le neveu", "nephew"), S("", "la fille (de quelqu'un)", "daughter"), S("", "le grand-père", "grandfather", ("grandpa",)), S("", "le mari", "husband"), S("", "les enfants", "children")],
  [L("aunt", "la tante", "l'oncle", "la nièce"), L("nephew", "le neveu", "la nièce", "le cousin"), L("daughter", "la fille", "le fils", "la sœur"),
   L("husband", "le mari", "la femme", "le frère"), L("grandmother", "la grand-mère", "le grand-père", "la mère"), L("uncle", "l'oncle", "la tante", "le cousin"),
   L("son", "le fils", "le soleil", "la fille"), L("wife", "l'épouse", "le mari", "la tante")],
  {"logic": ("choice", "Qui est-ce ?", [
      C("My mother's sister is my ____ .", ["aunt", "niece", "cousin"]), C("My father's father is my ____ .", ["grandfather", "uncle", "father-in-law"]),
      C("My uncle's son is my ____ .", ["cousin", "nephew", "brother"]), C("My sister's son is my ____ .", ["nephew", "cousin", "niece"]),
      C("My mother's husband is my ____ .", ["father", "uncle", "grandfather"]), C("My parents' daughter is my ____ .", ["sister", "aunt", "cousin"]),
      C("My brother's daughter is my ____ .", ["niece", "nephew", "aunt"]), C("My grandmother's son is my father or my ____ .", ["uncle", "cousin", "nephew"]),
  ])}, [M("logic", "🧠", "Qui est-ce ?", "My mother's sister is my…", ["logic"], 8)])

# ═════════════ MÉTÉO ═════════════
lex("meteo.html", "La météo et les saisons – Entraînement", "What's the <span>weather</span> like?", "La météo et les saisons", ("#7dd3fc", "#38bdf8"),
  '''      <p><b>What's the weather like?</b> = Quel temps fait-il ?</p>
      <table>
        <tr><th></th><th>It's…</th><th></th><th>It's…</th></tr>
        <tr><td>☀️</td><td>sunny</td><td>🌧️</td><td>rainy / It's raining.</td></tr>
        <tr><td>☁️</td><td>cloudy</td><td>❄️</td><td>snowy / It's snowing.</td></tr>
        <tr><td>💨</td><td>windy</td><td>🌫️</td><td>foggy</td></tr>
        <tr><td>⛈️</td><td>stormy</td><td>🔥 / 🥶</td><td>hot / cold</td></tr>
      </table>
      <p><b>Les saisons :</b> spring (printemps) · summer (été) · autumn (automne) · winter (hiver) → <i>in winter, in summer</i>.</p>
      <p>On dit <b>It's</b> + adjectif : <span class="ex">It's sunny. It's cold.</span> · <b>It's raining / snowing</b> pour ce qui se passe maintenant.</p>''',
  [V("☀️", "ensoleillé", "sunny", "sunday", "sonny"), V("☁️", "nuageux", "cloudy", "clouded", "rainy"), V("🌧️", "pluvieux", "rainy", "rainbow", "windy"),
   V("💨", "venteux", "windy", "windows", "wintry"), V("❄️", "il neige", "it's snowing", "it's snowy day", "it's raining"), V("🌫️", "brumeux", "foggy", "froggy", "cloudy"),
   V("⛈️", "orageux", "stormy", "storming", "thunder"), V("🍂", "l'automne", "autumn", "spring", "winter"), V("🌸", "le printemps", "spring", "summer", "autumn"), V("⛄", "l'hiver", "winter", "summer", "spring")],
  [S("☀️", "ensoleillé", "sunny"), S("☁️", "nuageux", "cloudy"), S("🌧️", "pluvieux", "rainy"), S("💨", "venteux", "windy"), S("🌫️", "brumeux", "foggy"),
   S("🔥", "chaud", "hot"), S("🥶", "froid", "cold"), S("🌸", "le printemps", "spring"), S("🌞", "l'été", "summer"), S("🍂", "l'automne", "autumn")],
  [L("sunny", "ensoleillé", "nuageux", "venteux"), L("windy", "venteux", "pluvieux", "neigeux"), L("cloudy", "nuageux", "brumeux", "orageux"),
   L("autumn", "l'automne", "l'été", "l'hiver"), L("foggy", "brumeux", "venteux", "ensoleillé"), L("winter", "l'hiver", "le printemps", "l'été"),
   L("rainy", "pluvieux", "orageux", "neigeux"), L("summer", "l'été", "l'automne", "le printemps")],
  {"phr": ("choice", "Choisis la bonne phrase", [
      C(None, ["It's raining.", "It rains now.", "It's rainy now day."], fr="Il pleut (en ce moment).", tip="maintenant → It's raining."),
      C(None, ["What's the weather like?", "How is the weather like?", "What weather it is?"], fr="Quel temps fait-il ?"),
      C(None, ["It's cold in winter.", "It's cold on winter.", "It's cold at winter."], fr="Il fait froid en hiver.", tip="saison → in."),
      C(None, ["It's very hot today.", "It does very hot today.", "It makes very hot today."], fr="Il fait très chaud aujourd'hui.", tip="Il fait chaud → It's hot."),
      C(None, ["It's snowing!", "It snows now!", "It's snow!"], fr="Il neige !"),
  ])}, [M("phr", "💬", "Les phrases de la météo", "It's raining, What's the weather like?…", ["phr"], 5)])

# ═════════════ NOURRITURE ═════════════
lex("nourriture.html", "La nourriture – Entraînement", 'Food & <span>drinks</span>', "La nourriture, les boissons et les repas", ("#fdba74", "#f97316"),
  '''      <p><b>Les repas :</b> breakfast (petit-déjeuner) · lunch (déjeuner) · dinner (dîner) · snack (en-cas). On dit <i>have breakfast, have lunch</i>.</p>
      <table>
        <tr><th>Fruits & légumes</th><th>Autres aliments</th><th>Boissons</th></tr>
        <tr><td>apple, banana, pear, strawberry, grapes, orange · carrot, tomato, potato, salad</td><td>bread, cheese, egg, meat, chicken, fish, rice, pasta, cake, sandwich</td><td>water, milk, orange juice, tea, coffee, hot chocolate</td></tr>
      </table>
      <p><b>Au restaurant :</b> <span class="ex">Can I have a pizza, please? · I'd like some water. · What would you like? · The bill, please.</span></p>''',
  [V("🍎", "la pomme", "apple", "pineapple", "potato"), V("🍞", "le pain", "bread", "brain", "pain"), V("🧀", "le fromage", "cheese", "chess", "cream"),
   V("🥚", "l'œuf", "egg", "eye", "oeuf"), V("🍗", "le poulet", "chicken", "kitchen", "pool"), V("🐟", "le poisson", "fish", "poison", "fishing"),
   V("🥕", "la carotte", "carrot", "parrot", "cabbage"), V("🍓", "la fraise", "strawberry", "fresh", "raspberry"), V("🥛", "le lait", "milk", "late", "meal"),
   V("🍐", "la poire", "pear", "pair", "peach"), V("🍇", "le raisin", "grapes", "raisins", "grip"), V("🥔", "la pomme de terre", "potato", "apple of earth", "tomato")],
  [S("🍎", "la pomme", "apple"), S("🍞", "le pain", "bread"), S("🧀", "le fromage", "cheese"), S("🥚", "l'œuf", "egg"), S("🍗", "le poulet", "chicken"),
   S("🐟", "le poisson", "fish"), S("🍌", "la banane", "banana"), S("🍅", "la tomate", "tomato"), S("🍓", "la fraise", "strawberry"), S("💧", "l'eau", "water"),
   S("🍚", "le riz", "rice"), S("🎂", "le gâteau", "cake")],
  [L("bread", "le pain", "la viande", "le beurre"), L("cheese", "le fromage", "le poulet", "la cerise"), L("strawberry", "la fraise", "la paille", "la framboise"),
   L("chicken", "le poulet", "la cuisine", "le fromage"), L("breakfast", "le petit-déjeuner", "le déjeuner", "le dîner"), L("water", "l'eau", "le serveur", "le vin"),
   L("pear", "la poire", "la paire", "la pêche"), L("lunch", "le déjeuner", "le dîner", "le goûter")],
  {"resto": ("choice", "Au restaurant : choisis la bonne phrase", [
      C(None, ["Can I have a pizza, please?", "Give me a pizza.", "I want pizza now."], fr="Tu commandes poliment une pizza."),
      C(None, ["The bill, please.", "The note, please.", "The addition, please."], fr="Tu demandes l'addition.", tip="l'addition = the bill."),
      C(None, ["What would you like?", "What do you want eat?", "What you like?"], fr="Le serveur demande ce que tu veux."),
      C(None, ["I'd like some water, please.", "I'd like a water please some.", "I like water, please."], fr="Tu demandes de l'eau poliment."),
      C(None, ["We have lunch at noon.", "We take the lunch at noon.", "We eat the lunch at noon."], fr="Nous déjeunons à midi.", tip="have lunch, sans article."),
  ])}, [M("resto", "🍽️", "Au restaurant", "Commander poliment.", ["resto"], 5)])

# ═════════════ VÊTEMENTS ═════════════
lex("vetements.html", "Les vêtements – Entraînement", 'Les <span>vêtements</span>', "Clothes", ("#f0abfc", "#e879f9"),
  '''      <table>
        <tr><th>Français</th><th>Anglais</th><th>Français</th><th>Anglais</th></tr>
        <tr><td>un tee-shirt</td><td>a T-shirt</td><td>un pantalon</td><td>trousers (GB) / pants (US)</td></tr>
        <tr><td>un jean</td><td>jeans</td><td>une robe</td><td>a dress</td></tr>
        <tr><td>une jupe</td><td>a skirt</td><td>un pull</td><td>a jumper / a sweater</td></tr>
        <tr><td>une veste</td><td>a jacket</td><td>un manteau</td><td>a coat</td></tr>
        <tr><td>des chaussures</td><td>shoes</td><td>des chaussettes</td><td>socks</td></tr>
        <tr><td>une écharpe</td><td>a scarf</td><td>des gants</td><td>gloves</td></tr>
        <tr><td>une casquette</td><td>a cap</td><td>un chapeau</td><td>a hat</td></tr>
      </table>
      <p>Verbes utiles : <b>wear</b> (porter) · <b>put on</b> (mettre) · <b>take off</b> (enlever) · <b>try on</b> (essayer).</p>
      <p>Attention : <b>jeans</b> et <b>trousers</b> sont toujours au pluriel : <span class="ex">My jeans are blue.</span></p>''',
  [V("👕", "le tee-shirt", "T-shirt", "tea-shirt", "shirt-tee"), V("👗", "la robe", "dress", "robe", "skirt"), V("🧦", "les chaussettes", "socks", "shoes", "sucks"),
   V("🧤", "les gants", "gloves", "gants", "hands"), V("🧣", "l'écharpe", "scarf", "scar", "shawl"), V("🧥", "le manteau", "coat", "cost", "jacket"),
   V("👖", "le jean", "jeans", "gin", "trousers"), V("🧢", "la casquette", "cap", "hat", "cape"), V("👟", "les baskets", "trainers", "baskets", "boots"), V("", "le pull", "jumper", "pull", "shirt")],
  [S("👕", "le tee-shirt", "T-shirt", ("tshirt", "t shirt")), S("👗", "la robe", "dress"), S("🧦", "les chaussettes", "socks"), S("🧤", "les gants", "gloves"),
   S("🧣", "l'écharpe", "scarf"), S("🧥", "le manteau", "coat"), S("👞", "les chaussures", "shoes"), S("🎩", "le chapeau", "hat"), S("", "la jupe", "skirt"), S("", "la veste", "jacket")],
  [L("skirt", "la jupe", "la chemise", "le short"), L("gloves", "les gants", "les lunettes", "les chaussures"), L("jumper", "le pull", "le sauteur", "la veste"),
   L("coat", "le manteau", "le chapeau", "la côte"), L("trousers", "le pantalon", "la trousse", "le jean"), L("scarf", "l'écharpe", "la cicatrice", "le chapeau"),
   L("shoes", "les chaussures", "les chaussettes", "les bottes"), L("dress", "la robe", "le pull", "la veste")],
  {"verbs": ("choice", "wear, put on, take off ou try on ?", [
      C("It's cold. ____ your coat!", ["Put on", "Take off", "Try on"], tip="mettre → put on."), C("Can I ____ these jeans? Where are the fitting rooms?", ["try on", "take off", "wear"], tip="essayer → try on."),
      C("____ your shoes before you come in, please.", ["Take off", "Put on", "Try on"], tip="enlever → take off."), C("She always ____ a red scarf.", ["wears", "puts on", "takes off"], tip="porter (habitude) → wear."),
  ])}, [M("verbs", "👚", "wear, put on, take off…", "Les verbes des vêtements.", ["verbs"], 4)])

# ═════════════ MAISON ═════════════
lex("maison.html", "La maison – Entraînement", 'La <span>maison</span>', "Rooms and furniture", ("#d9f99d", "#a3e635"),
  '''      <p><b>Les pièces :</b> kitchen (cuisine) · living room (salon) · bedroom (chambre) · bathroom (salle de bain) · toilet (toilettes) · garden (jardin) · garage · stairs (escalier) · upstairs / downstairs (en haut / en bas).</p>
      <p><b>Les meubles et objets :</b> bed (lit) · sofa (canapé) · table · chair (chaise) · wardrobe (armoire) · fridge (frigo) · oven (four) · shower (douche) · bath (baignoire) · lamp (lampe) · window (fenêtre) · door (porte).</p>
      <p class="ex">There is a sofa in the living room. · My bedroom is upstairs.</p>''',
  [V("🛏️", "la chambre", "bedroom", "bathroom", "chamber"), V("🛁", "la salle de bain", "bathroom", "bedroom", "bath hall"), V("🍳", "la cuisine", "kitchen", "chicken", "cuisine"),
   V("🛋️", "le canapé", "sofa", "canape", "chair"), V("🚿", "la douche", "shower", "bath", "douche"), V("🚪", "la porte", "door", "port", "window"),
   V("", "la fenêtre", "window", "wind", "door"), V("🌳", "le jardin", "garden", "jardin", "yard man"), V("", "l'escalier", "stairs", "steps up", "escalator"), V("", "l'armoire", "wardrobe", "armour", "cupboard man")],
  [S("🍳", "la cuisine", "kitchen"), S("🛏️", "la chambre", "bedroom"), S("🛁", "la salle de bain", "bathroom"), S("🛋️", "le salon", "living room", ("living-room",)),
   S("🚪", "la porte", "door"), S("🌳", "le jardin", "garden"), S("🚿", "la douche", "shower"), S("", "le frigo", "fridge"), S("", "la chaise", "chair"), S("", "le lit", "bed")],
  [L("kitchen", "la cuisine", "le poulet", "le salon"), L("wardrobe", "l'armoire", "la garde-robe", "le placard"), L("stairs", "l'escalier", "les étoiles", "le grenier"),
   L("bedroom", "la chambre", "la salle de bain", "le salon"), L("fridge", "le frigo", "le four", "la cuisinière"), L("garden", "le jardin", "le garage", "le gardien"),
   L("window", "la fenêtre", "la porte", "le vent"), L("living room", "le salon", "la chambre", "la salle à manger")],
  {"where": ("choice", "Dans quelle pièce ?", [
      C("You cook in the ____ .", ["kitchen", "bedroom", "garage"]), C("You sleep in the ____ .", ["bedroom", "kitchen", "bathroom"]),
      C("You have a shower in the ____ .", ["bathroom", "living room", "garden"]), C("You watch TV in the ____ .", ["living room", "bathroom", "garage"]),
      C("You park the car in the ____ .", ["garage", "garden", "kitchen"]), C("The flowers are in the ____ .", ["garden", "fridge", "wardrobe"]),
  ])}, [M("where", "🏠", "Dans quelle pièce ?", "You cook in the…", ["where"], 6)])

# ═════════════ MÉTIERS ═════════════
lex("metiers.html", "Les métiers – Entraînement", 'Les <span>métiers</span>', "Jobs", ("#a5b4fc", "#818cf8"),
  '''      <p>Pour dire le métier de quelqu'un, on utilise <b>a / an</b> : <span class="ex">She is a nurse. · He is an engineer.</span></p>
      <table>
        <tr><th>Français</th><th>Anglais</th><th>Français</th><th>Anglais</th></tr>
        <tr><td>médecin</td><td>doctor</td><td>infirmier / infirmière</td><td>nurse</td></tr>
        <tr><td>professeur</td><td>teacher</td><td>boulanger</td><td>baker</td></tr>
        <tr><td>boucher</td><td>butcher</td><td>coiffeur</td><td>hairdresser</td></tr>
        <tr><td>mécanicien</td><td>mechanic</td><td>pompier</td><td>firefighter</td></tr>
        <tr><td>policier</td><td>police officer</td><td>agriculteur</td><td>farmer</td></tr>
        <tr><td>cuisinier</td><td>cook / chef</td><td>serveur</td><td>waiter / waitress</td></tr>
        <tr><td>vendeur</td><td>shop assistant</td><td>caissier</td><td>cashier</td></tr>
        <tr><td>aide-soignant(e)</td><td>care assistant</td><td>plombier</td><td>plumber</td></tr>
      </table>
      <p><b>What do you do?</b> = Que fais-tu (comme métier) ? · <b>What do you want to be?</b> = Que veux-tu faire plus tard ?</p>''',
  [V("🩺", "le médecin", "doctor", "medecin", "nurse"), V("", "l'infirmière", "nurse", "nursery", "doctor"), V("🥖", "le boulanger", "baker", "butcher", "banker"),
   V("✂️", "le coiffeur", "hairdresser", "hair cutter", "barbecue"), V("🔧", "le mécanicien", "mechanic", "mechanical", "engineer"), V("🚒", "le pompier", "firefighter", "fireman pump", "pumper"),
   V("👮", "le policier", "police officer", "policeman officer", "politician"), V("🚜", "l'agriculteur", "farmer", "farm", "gardener"), V("", "le vendeur", "shop assistant", "seller man", "shopper"),
   V("", "le caissier", "cashier", "cash man", "banker")],
  [S("🩺", "le médecin", "doctor"), S("", "l'infirmière", "nurse"), S("", "le professeur", "teacher"), S("🥖", "le boulanger", "baker"), S("", "le boucher", "butcher"),
   S("🚜", "l'agriculteur", "farmer"), S("🔧", "le mécanicien", "mechanic"), S("", "le serveur", "waiter"), S("", "le caissier", "cashier"), S("", "le plombier", "plumber")],
  [L("butcher", "le boucher", "le boulanger", "le majordome"), L("nurse", "l'infirmière", "la nourrice", "le médecin"), L("hairdresser", "le coiffeur", "le couturier", "le dentiste"),
   L("waiter", "le serveur", "le cuisinier", "le caissier"), L("firefighter", "le pompier", "le soldat", "le policier"), L("farmer", "l'agriculteur", "le pharmacien", "le boulanger"),
   L("cashier", "le caissier", "le banquier", "le comptable"), L("plumber", "le plombier", "l'électricien", "le peintre")],
  {"where": ("choice", "Où travaille-t-il ?", [
      C("A baker works in a ____ .", ["bakery", "butcher's", "hospital"]), C("A nurse works in a ____ .", ["hospital", "garage", "school"]),
      C("A mechanic works in a ____ .", ["garage", "bakery", "hospital"]), C("A teacher works in a ____ .", ["school", "farm", "shop"]),
      C("A farmer works on a ____ .", ["farm", "school", "hairdresser's"]), C("A shop assistant works in a ____ .", ["shop", "hospital", "farm"]),
  ])}, [M("where", "🏢", "Où travaille-t-il ?", "A baker works in a…", ["where"], 6)])

# ═════════════ PHRASAL VERBS ═════════════
newpage("phrasal_verbs.html", "Les phrasal verbs – Entraînement", '<span>Phrasal</span> verbs',
  "get up, look for, give up, try on…", ("#fcd34d", "#fbbf24"),
  '''      <p>Un <span class="hl">phrasal verb</span> = un verbe + une petite particule (up, on, off, for, after…). La particule <b>change le sens</b> du verbe.</p>
      <table>
        <tr><th>Verbe</th><th>Sens</th><th>Verbe</th><th>Sens</th></tr>
        <tr><td>get up</td><td>se lever</td><td>wake up</td><td>se réveiller</td></tr>
        <tr><td>look for</td><td>chercher</td><td>look after</td><td>s'occuper de</td></tr>
        <tr><td>give up</td><td>abandonner, arrêter</td><td>find out</td><td>découvrir</td></tr>
        <tr><td>turn on / turn off</td><td>allumer / éteindre</td><td>put on / take off</td><td>mettre / enlever (vêtement)</td></tr>
        <tr><td>try on</td><td>essayer (vêtement)</td><td>come back</td><td>revenir</td></tr>
        <tr><td>go out</td><td>sortir</td><td>sit down / stand up</td><td>s'asseoir / se lever</td></tr>
        <tr><td>pick up</td><td>ramasser, aller chercher</td><td>throw away</td><td>jeter</td></tr>
      </table>''',
  {
    "sens": ("choice", "Que veut dire ce phrasal verb ?", [
      C(None, ["se lever", "se réveiller", "monter"], big="get up"), C(None, ["chercher", "regarder", "s'occuper de"], big="look for"),
      C(None, ["s'occuper de", "chercher", "regarder derrière"], big="look after"), C(None, ["abandonner, arrêter", "donner", "monter"], big="give up"),
      C(None, ["éteindre", "allumer", "tourner"], big="turn off"), C(None, ["essayer (un vêtement)", "enlever", "porter"], big="try on"),
      C(None, ["découvrir", "trouver dehors", "perdre"], big="find out"), C(None, ["jeter", "lancer loin", "ranger"], big="throw away"),
      C(None, ["revenir", "venir", "partir"], big="come back"), C(None, ["ramasser, aller chercher", "choisir", "piquer"], big="pick up"),
    ]),
    "part": ("choice", "Choisis la bonne particule", [
      C("I get ____ at 7 every morning.", ["up", "on", "off"], keep=True, tip="get up = se lever."), C("Can you turn ____ the light? It's dark.", ["on", "off", "up"], keep=True, tip="allumer → turn on."),
      C("I'm looking ____ my keys.", ["for", "after", "at"], keep=True, tip="chercher → look for."), C("She looks ____ her little brother.", ["after", "for", "up"], keep=True, tip="s'occuper de → look after."),
      C("Don't give ____ ! You can do it!", ["up", "on", "off"], keep=True, tip="abandonner → give up."), C("Take ____ your shoes, please.", ["off", "on", "out"], keep=True, tip="enlever → take off."),
      C("Can I try ____ this dress?", ["on", "off", "up"], keep=True, tip="essayer → try on."), C("Please sit ____ .", ["down", "up", "on"], keep=True, tip="s'asseoir → sit down."),
    ]),
  },
  [M("sens", "💡", "Quel sens ?", "get up, look for, give up…", ["sens"]),
   M("part", "🧩", "La bonne particule", "up, on, off, for, after…", ["part"], 8),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["sens", "part"], 12)], tag="Anglais · Lexique")

# ═════════════ CAP : AIDE À LA PERSONNE ═════════════
newpage("cap_aide.html", "Anglais de l'aide à la personne – CAP Sapver", "L'anglais de l'<span>aide à la personne</span>",
  "Le corps, la santé, les consignes, rassurer", ("#99f6e4", "#5eead4"),
  '''      <h4>Le corps</h4>
      <p class="ex">head (tête) · arm (bras) · hand (main) · leg (jambe) · foot / feet (pied) · back (dos) · stomach (ventre) · throat (gorge) · tooth / teeth (dent)</p>
      <h4>La santé</h4>
      <p class="ex">I've got a headache (mal à la tête) · a stomachache (mal au ventre) · a sore throat (mal à la gorge) · a temperature (de la fièvre) · My back hurts.</p>
      <h4>Questions utiles</h4>
      <p class="ex">How do you feel? · Are you in pain? · Where does it hurt? · Do you need help? · Are you comfortable? · Would you like some water?</p>
      <h4>Consignes (impératif poli)</h4>
      <p class="ex">Sit down, please. · Can you stand up? · Lie down here. · Take your medicine. · Hold my arm. · Take your time.</p>
      <p><b>Urgence :</b> <span class="ex">Call an ambulance! · Call 112 / 999 (UK).</span></p>''',
  {
    "body": ("choice", "Quel est le mot anglais ?", [
      V("", "la tête", "head", "hat", "hand"), V("", "le bras", "arm", "army", "hand"), V("", "la jambe", "leg", "leek", "foot"), V("", "le dos", "back", "bag", "belly"),
      V("", "le ventre", "stomach", "stomack", "ventral"), V("", "la gorge", "throat", "throw", "gorgeous"), V("", "les dents", "teeth", "tooths", "dents"), V("", "le pied", "foot", "feet", "pied"),
    ]),
    "health": ("choice", "Que dit la personne ?", [
      C(None, ["I've got a headache.", "I have a head pain.", "My head is ache."], fr="Elle a mal à la tête."), C(None, ["I've got a sore throat.", "I've got a bad gorge.", "My throat is ache."], fr="Il a mal à la gorge."),
      C(None, ["I've got a temperature.", "I've got a fever hot.", "I am temperature."], fr="Elle a de la fièvre."), C(None, ["My back hurts.", "My back is hurting me pain.", "I hurt back."], fr="Il a mal au dos."),
      C(None, ["I've got a stomachache.", "I have pain of belly.", "My stomach is sick."], fr="Elle a mal au ventre."), C(None, ["I feel tired.", "I am tiring.", "I feel tire."], fr="Il se sent fatigué."),
    ]),
    "care": ("choice", "Que dites-vous à la personne ?", [
      C(None, ["How do you feel?", "How you feel?", "What do you feel like?"], fr="Vous demandez comment la personne se sent."),
      C(None, ["Where does it hurt?", "Where is it hurt?", "Where do you pain?"], fr="Vous demandez où elle a mal."),
      C(None, ["Sit down, please.", "Sit up you, please.", "You sit, please."], fr="Vous demandez poliment à la personne de s'asseoir."),
      C(None, ["Can you stand up?", "Can you stand on?", "Can you get down?"], fr="Vous demandez si elle peut se lever."),
      C(None, ["Take your time.", "Take the time of you.", "Have your time."], fr="Vous la rassurez : elle n'a pas besoin de se dépêcher."),
      C(None, ["Would you like some water?", "Do you want water or not?", "Drink water."], fr="Vous proposez de l'eau poliment."),
      C(None, ["Hold my arm.", "Keep my arm.", "Hold me arm."], fr="Vous l'aidez à marcher : elle doit tenir votre bras."),
      C(None, ["Call an ambulance!", "Call a hospital car!", "Phone the ambulance man!"], fr="Urgence : il faut appeler une ambulance."),
    ]),
    "listen": ("choice", "Écoute : que veut dire ce mot ?", [
      L("headache", "mal à la tête", "mal au ventre", "la tête"), L("back", "le dos", "le sac", "retour"), L("medicine", "le médicament", "le médecin", "la maladie"),
      L("throat", "la gorge", "la dent", "la bouche"), L("comfortable", "à l'aise, bien installé", "content", "fatigué"), L("stomach", "le ventre", "le dos", "la poitrine"),
    ]),
  },
  [M("body", "🦵", "Le corps", "head, arm, back, stomach…", ["body"], 8),
   M("health", "🤒", "La santé", "I've got a headache, a sore throat…", ["health"], 6),
   M("care", "🤝", "Parler à la personne", "Questions, consignes, rassurer.", ["care"], 8),
   M("listen", "🔊", "Écoute et comprends", "Écoute le mot et trouve sa traduction.", ["listen"], 6),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["body", "health", "care", "listen"], 12)], tag="Anglais · CAP Sapver")

# ═════════════ CAP : ÉCRIT PRO ET ENTRETIEN ═════════════
E1, E2 = "Écrire un e-mail professionnel", "L'entretien d'embauche"
newpage("cap_ecrit_entretien.html", "E-mail et entretien – CAP Sapver", "E-mail & <span>entretien</span> d'embauche",
  "Écrire un mail professionnel · réussir son entretien", ("#bae6fd", "#7dd3fc"),
  '''      <h4>Un e-mail professionnel</h4>
      <table>
        <tr><th>Partie</th><th>Formules</th></tr>
        <tr><td>Saluer</td><td>Dear Mr Smith, / Dear Mrs Brown, · Dear Sir or Madam, (nom inconnu)</td></tr>
        <tr><td>Dire pourquoi on écrit</td><td>I am writing to apply for… · I am writing about…</td></tr>
        <tr><td>Joindre un document</td><td>Please find attached my CV.</td></tr>
        <tr><td>Terminer</td><td>I look forward to hearing from you.</td></tr>
        <tr><td>Signer</td><td>Yours sincerely, (nom connu) · Yours faithfully, (Dear Sir or Madam) · Best regards,</td></tr>
      </table>
      <h4>L'entretien d'embauche</h4>
      <p class="ex">Tell me about yourself. → I'm 17 and I'm studying for a CAP in sales. · Why do you want this job? → I like helping customers. · What are your strengths? → I'm hard-working, punctual and friendly. · Have you got any experience? → I did a work placement in a supermarket. · When can you start? → I'm available from June.</p>''',
  {
    "mail": ("choice", "Choisis la bonne formule", [
      C(None, ["Dear Sir or Madam,", "Hello you,", "Hi guys,"], fr="Vous écrivez à une entreprise sans connaître le nom du destinataire."),
      C(None, ["I am writing to apply for the job of shop assistant.", "I write you for the job.", "I want the job, please."], fr="Vous expliquez que vous postulez au poste de vendeur."),
      C(None, ["Please find attached my CV.", "Look my CV in the mail.", "Here is attached me CV."], fr="Vous indiquez que votre CV est en pièce jointe."),
      C(None, ["I look forward to hearing from you.", "Answer me quickly.", "I wait your answer."], fr="Vous dites que vous attendez une réponse (poliment)."),
      C(None, ["Yours faithfully,", "Bye bye,", "Kisses,"], fr="Vous terminez un mail commencé par « Dear Sir or Madam »."),
      C(None, ["Dear Mrs Brown,", "Dear Mrs,", "Hello Mrs Brown!"], fr="Vous écrivez à Mme Brown."),
    ]),
    "job": ("choice", "Quelle est la meilleure réponse ?", [
      C("Tell me about yourself.", ["I'm 17 and I'm studying for a CAP in sales.", "I'm fine, thank you.", "Yourself is very nice."]),
      C("Why do you want this job?", ["Because I like helping customers.", "Because I want money only.", "Because yes."]),
      C("What are your strengths?", ["I'm hard-working and punctual.", "I'm very strong, I lift weights.", "I have no weaknesses."]),
      C("Have you got any experience?", ["Yes, I did a work placement in a shop.", "Yes, I have 17 years.", "No, I'm not experienced in English."]),
      C("When can you start?", ["I'm available from June.", "I start at 9 o'clock.", "I can start the job."]),
      C("Do you have any questions?", ["Yes, what are the working hours?", "No, I don't have.", "Yes, how old are you?"]),
    ]),
    "adj": ("choice", "Quel est le mot anglais ?", [
      V("", "travailleur", "hard-working", "worker", "hard-work"), V("", "ponctuel", "punctual", "ponctual", "on-time man"),
      V("", "aimable, sympathique", "friendly", "friendful", "kindly"), V("", "un stage", "a work placement", "a stage", "a training stage"),
      V("", "disponible", "available", "disponible", "free time"), V("", "le CV", "CV / résumé", "curriculum", "life paper"),
    ]),
  },
  [M("mail", "✉️", "Les formules du mail", "Dear…, Please find attached…", ["mail"], 6, E1),
   M("job", "🤝", "Répondre aux questions", "Tell me about yourself…", ["job"], 6, E2),
   M("adj", "📖", "Le vocabulaire", "hard-working, punctual, work placement…", ["adj"], 6, E2),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["mail", "job", "adj"], 12, "Les deux")], tag="Anglais · CAP Sapver")
print("content6 ok", REGISTRY)
