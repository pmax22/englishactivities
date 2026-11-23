import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
exec(open(_EA_OUT+"/content_helpers.py", encoding="utf-8").read())
exec(open(_EA_OUT+"/content6.py", encoding="utf-8").read().split("# ═════════════ SE PRÉSENTER")[0].split('exec(open(_EA_OUT+"/content_helpers.py", encoding="utf-8").read())')[1])
REGISTRY.clear()

# ═════════════ FAUX AMIS ═════════════
def FA(en, ok, piege, autre, tip):
    return C(None, [ok, piege, autre], big=en, say=en, tip=tip)
newpage("faux_amis.html", "Les faux amis – Entraînement", 'Les <span>faux amis</span>',
  "Ces mots qui ressemblent au français… mais ne veulent pas dire la même chose", ("#fecaca", "#f87171"),
  '''      <p>Un <span class="hl">faux ami</span> est un mot anglais qui ressemble à un mot français mais qui a un <b>autre sens</b>.</p>
      <table>
        <tr><th>Anglais</th><th>veut dire</th><th>ne veut PAS dire</th><th>qui se dit</th></tr>
        <tr><td>actually</td><td>en fait</td><td>actuellement</td><td>currently, now</td></tr>
        <tr><td>library</td><td>bibliothèque</td><td>librairie</td><td>bookshop</td></tr>
        <tr><td>sensible</td><td>raisonnable</td><td>sensible</td><td>sensitive</td></tr>
        <tr><td>to attend</td><td>assister à</td><td>attendre</td><td>to wait</td></tr>
        <tr><td>a coin</td><td>une pièce de monnaie</td><td>un coin</td><td>a corner</td></tr>
        <tr><td>a journey</td><td>un voyage, un trajet</td><td>une journée</td><td>a day</td></tr>
        <tr><td>a cave</td><td>une grotte</td><td>une cave</td><td>a cellar</td></tr>
        <tr><td>eventually</td><td>finalement</td><td>éventuellement</td><td>possibly</td></tr>
        <tr><td>a location</td><td>un emplacement</td><td>une location</td><td>a rental</td></tr>
        <tr><td>to rest</td><td>se reposer</td><td>rester</td><td>to stay</td></tr>
      </table>''',
  {"sens": ("choice", "Que veut vraiment dire ce mot ?", [
      FA("actually", "en fait", "actuellement", "activement", "actuellement = currently."), FA("library", "bibliothèque", "librairie", "liberté", "librairie = bookshop."),
      FA("sensible", "raisonnable", "sensible", "sensationnel", "sensible (émotif) = sensitive."), FA("to attend", "assister à", "attendre", "entendre", "attendre = to wait."),
      FA("a coin", "une pièce de monnaie", "un coin", "une coiffe", "un coin = a corner."), FA("a journey", "un voyage, un trajet", "une journée", "un journal", "une journée = a day."),
      FA("a cave", "une grotte", "une cave", "un caveau", "une cave = a cellar."), FA("eventually", "finalement", "éventuellement", "évidemment", "éventuellement = possibly."),
      FA("a location", "un emplacement", "une location", "une localité", "une location = a rental."), FA("to rest", "se reposer", "rester", "restaurer", "rester = to stay."),
      FA("a car", "une voiture", "un car", "une carte", "un car = a coach."), FA("a chance", "une occasion, une possibilité", "la chance", "un chant", "la chance = luck."),
      FA("a lecture", "un cours magistral, une conférence", "une lecture", "un lecteur", "une lecture = a reading."), FA("to pretend", "faire semblant", "prétendre", "prendre", "prétendre = to claim."),
    ]),
    "en": ("choice", "Comment dit-on en anglais ?", [
      V("", "une librairie", "a bookshop", "a library", "a bookery"), V("", "actuellement", "currently", "actually", "actively"),
      V("", "attendre", "to wait", "to attend", "to hear"), V("", "un coin (de rue)", "a corner", "a coin", "a angle"),
      V("", "une journée", "a day", "a journey", "a journal"), V("", "rester", "to stay", "to rest", "to remain on"),
      V("", "la chance", "luck", "chance", "lucky"), V("", "un car (autocar)", "a coach", "a car", "a bus car"),
    ])},
  [M("sens", "🪤", "Le vrai sens", "Ne te fais pas piéger !", ["sens"], 12),
   M("en", "🔁", "Le bon mot anglais", "librairie, actuellement, attendre…", ["en"], 8),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["sens", "en"], 12)], tag="Anglais · Lexique")

# ═════════════ VILLE ET DIRECTIONS ═════════════
newpage("ville_directions.html", "La ville et les directions – Entraînement", 'Excuse me, where is <span>the station</span>?',
  "Les lieux de la ville et indiquer un chemin", ("#bbf7d0", "#4ade80"),
  '''      <h4>Les lieux</h4>
      <p class="ex">station (gare) · bus stop (arrêt de bus) · bank · post office (poste) · chemist's (pharmacie) · baker's (boulangerie) · supermarket · town hall (mairie) · library (bibliothèque) · hospital · museum · park · square (place) · church (église)</p>
      <h4>Demander son chemin</h4>
      <p class="ex">Excuse me, where is the station? · How can I get to the museum? · Is there a bank near here?</p>
      <h4>Indiquer le chemin</h4>
      <p class="ex">Go straight on (tout droit) · Turn left / right (tournez à gauche / droite) · Take the first street on the left · Cross the road (traversez) · It's next to (à côté de) · opposite (en face de) · between (entre) · on the corner (à l'angle) · It's on your left.</p>''',
  {"places": ("choice", "Quel est le mot anglais ?", [
      V("🚉", "la gare", "station", "gare", "stop"), V("💊", "la pharmacie", "chemist's", "pharmacy shop", "drugstore man"), V("🏦", "la banque", "bank", "bench", "banc"),
      V("📮", "la poste", "post office", "poste", "mail shop"), V("🏛️", "la mairie", "town hall", "mayor", "city house"), V("📚", "la bibliothèque", "library", "bookshop", "biblioteca"),
      V("⛪", "l'église", "church", "chapel man", "eglise"), V("🚏", "l'arrêt de bus", "bus stop", "bus station stop", "bus halt"), V("🏥", "l'hôpital", "hospital", "hostel", "hotel"),
      V("", "la place (de la ville)", "square", "place", "plaza"),
    ]),
    "dir": ("choice", "Que veut dire cette indication ?", [
      C(None, ["Allez tout droit.", "Tournez à droite.", "Traversez la rue."], big="Go straight on.", say="Go straight on."),
      C(None, ["Tournez à gauche.", "Tournez à droite.", "Restez à gauche."], big="Turn left.", say="Turn left."),
      C(None, ["Traversez la rue.", "Prenez la rue.", "Suivez la route."], big="Cross the road.", say="Cross the road."),
      C(None, ["C'est en face de la banque.", "C'est à côté de la banque.", "C'est derrière la banque."], big="It's opposite the bank.", say="It's opposite the bank."),
      C(None, ["C'est à côté de la poste.", "C'est en face de la poste.", "C'est loin de la poste."], big="It's next to the post office.", say="It's next to the post office."),
      C(None, ["C'est entre le parc et l'église.", "C'est derrière le parc.", "C'est après l'église."], big="It's between the park and the church.", say="It's between the park and the church."),
      C(None, ["Prenez la première rue à droite.", "Prenez la première à gauche.", "C'est la première maison."], big="Take the first street on the right.", say="Take the first street on the right."),
      C(None, ["C'est au coin de la rue.", "C'est au bout de la rue.", "C'est dans la rue."], big="It's on the corner.", say="It's on the corner."),
    ]),
    "ask": ("choice", "Quelle est la bonne phrase ?", [
      C(None, ["Excuse me, where is the station?", "Sorry, where the station?", "Hello, the station is where?"], fr="Vous demandez poliment où est la gare."),
      C(None, ["How can I get to the museum?", "How I go to museum?", "Where I can go museum?"], fr="Vous demandez comment aller au musée."),
      C(None, ["Is there a chemist's near here?", "There is a chemist near?", "Is it a chemist's here near?"], fr="Vous demandez s'il y a une pharmacie près d'ici."),
      C(None, ["Turn right at the traffic lights.", "Turn on right at the lights.", "Go right of the lights."], fr="Vous dites de tourner à droite au feu."),
    ])},
  [M("places", "🏙️", "Les lieux de la ville", "station, chemist's, town hall…", ["places"]),
   M("dir", "🗺️", "Comprendre un itinéraire", "Go straight on, turn left, opposite…", ["dir"], 8),
   M("ask", "🙋", "Demander son chemin", "Excuse me, where is…?", ["ask"], 4),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["places", "dir", "ask"], 12)], tag="Anglais · Lexique")

# ═════════════ ÉCOLE ═════════════
lex("ecole.html", "L'école – Entraînement", 'At <span>school</span>', "Matières, lieux et objets de l'école", ("#fef08a", "#facc15"),
  '''      <p><b>Les matières :</b> English · French · Maths · History · Geography · Science · Biology · Physics · Chemistry · PE (sport) · Art · Music · Technology</p>
      <p><b>Les lieux :</b> classroom (salle de classe) · playground (cour) · canteen (cantine) · library (CDI) · gym (gymnase) · staffroom (salle des profs)</p>
      <p><b>Les objets :</b> pen (stylo) · pencil (crayon) · rubber (gomme) · ruler (règle) · schoolbag (cartable) · pencil case (trousse) · exercise book (cahier) · glue (colle) · scissors (ciseaux)</p>
      <p>Les matières n'ont pas d'article : <span class="ex">I like Maths. <s>I like the Maths.</s></span> · <b>timetable</b> = emploi du temps.</p>''',
  [V("✏️", "le crayon", "pencil", "pen", "crayon"), V("📏", "la règle", "ruler", "rule", "rubber"), V("", "la gomme", "rubber", "gum", "ruler"),
   V("✂️", "les ciseaux", "scissors", "cisors", "cutters"), V("🎒", "le cartable", "schoolbag", "cartable", "pencil case"), V("", "la trousse", "pencil case", "trouser", "box pen"),
   V("", "la cantine", "canteen", "cantina", "kitchen"), V("", "la cour de récréation", "playground", "court", "garden"), V("", "l'emploi du temps", "timetable", "use of time", "agenda"),
   V("", "l'EPS (sport)", "PE", "EPS", "sport class")],
  [S("✏️", "le crayon", "pencil"), S("🖊️", "le stylo", "pen"), S("📏", "la règle", "ruler"), S("", "la gomme", "rubber", ("eraser",)), S("✂️", "les ciseaux", "scissors"),
   S("", "l'histoire", "history"), S("", "les mathématiques", "maths", ("math",)), S("", "la géographie", "geography"), S("", "la salle de classe", "classroom"), S("", "le cahier", "exercise book", ("notebook",))],
  [L("rubber", "la gomme", "le caoutchouc rouge", "la règle"), L("timetable", "l'emploi du temps", "la table", "le calendrier"), L("canteen", "la cantine", "le gymnase", "la cour"),
   L("ruler", "la règle", "le roi", "la gomme"), L("chemistry", "la chimie", "la physique", "la pharmacie"), L("playground", "la cour de récréation", "le terrain de jeu vidéo", "le gymnase"),
   L("pencil case", "la trousse", "le crayon", "le taille-crayon"), L("homework", "les devoirs", "le travail à la maison", "la maison")])

# ═════════════ LOISIRS ET SPORTS ═════════════
lex("loisirs_sports.html", "Les loisirs et les sports – Entraînement", 'Free time & <span>sports</span>', "Loisirs, sports et play / do / go", ("#fdba74", "#fb923c"),
  '''      <p><b>Sports :</b> football · basketball · tennis · swimming · running · cycling · horse riding · skiing · judo · dancing</p>
      <p><b>Loisirs :</b> reading · drawing · playing video games · listening to music · watching films · going out with friends · cooking · shopping</p>
      <h4>play, do ou go ?</h4>
      <table>
        <tr><th>play</th><th>do</th><th>go</th></tr>
        <tr><td>sports de ballon, jeux, instruments<br><i>play football, play cards, play the guitar</i></td><td>sports individuels, arts martiaux<br><i>do judo, do gymnastics, do yoga</i></td><td>activités en -ing<br><i>go swimming, go skiing, go shopping</i></td></tr>
      </table>''',
  [V("⚽", "le football", "football", "footing", "soccer ball"), V("🏊", "la natation", "swimming", "natation", "swim pool"), V("🚴", "le vélo (sport)", "cycling", "velo", "biking ride"),
   V("🏇", "l'équitation", "horse riding", "equitation", "horse running"), V("⛷️", "le ski", "skiing", "skying", "snowing"), V("🎨", "le dessin", "drawing", "design", "painting room"),
   V("🎣", "la pêche", "fishing", "peaching", "fish hunting"), V("🏃", "la course à pied", "running", "footing", "racing walk"), V("🎮", "les jeux vidéo", "video games", "games videos", "videogames play"),
   V("🎸", "la guitare", "guitar", "gitar", "guitare")],
  [S("⚽", "le football", "football"), S("🏊", "la natation", "swimming"), S("🎨", "le dessin", "drawing"), S("🎣", "la pêche", "fishing"), S("🏃", "la course à pied", "running"),
   S("🎾", "le tennis", "tennis"), S("🚴", "le cyclisme", "cycling"), S("⛷️", "le ski", "skiing"), S("💃", "la danse", "dancing", ("dance",)), S("📖", "la lecture", "reading")],
  [L("horse riding", "l'équitation", "la course de chevaux", "le cheval"), L("swimming", "la natation", "le saut", "la plongée"), L("cycling", "le cyclisme", "le recyclage", "la course"),
   L("drawing", "le dessin", "le tiroir", "la peinture"), L("fishing", "la pêche", "le poisson", "la chasse"), L("skiing", "le ski", "le patinage", "la luge"),
   L("hiking", "la randonnée", "l'escalade", "la course"), L("climbing", "l'escalade", "la randonnée", "la natation")],
  {"pdg": ("choice", "play, do ou go ?", [
      C("I ____ football on Saturdays.", ["play", "do", "go"], keep=True, tip="sport de ballon → play."), C("She ____ judo.", ["does", "plays", "goes"], keep=True, tip="art martial → do."),
      C("We ____ swimming every week.", ["go", "play", "do"], keep=True, tip="activité en -ing → go."), C("He ____ the guitar.", ["plays", "does", "goes"], keep=True, tip="instrument → play."),
      C("They ____ skiing in winter.", ["go", "do", "play"], keep=True, tip="activité en -ing → go."), C("I ____ yoga with my mum.", ["do", "play", "go"], keep=True, tip="activité individuelle → do."),
      C("Do you ____ tennis?", ["play", "do", "go"], keep=True, tip="sport de raquette → play."), C("Let's ____ shopping!", ["go", "do", "play"], keep=True, tip="activité en -ing → go."),
  ])}, [M("pdg", "🏅", "play, do ou go ?", "play football, do judo, go swimming…", ["pdg"], 8)])

# ═════════════ TRANSPORTS ═════════════
lex("transports.html", "Les transports – Entraînement", 'Les <span>transports</span>', "Moyens de transport et voyage", ("#93c5fd", "#3b82f6"),
  '''      <p><b>Moyens de transport :</b> car · bus · coach (car) · train · plane · boat · bike · motorbike · underground / tube (métro) · taxi · on foot (à pied)</p>
      <p><b>by</b> + moyen de transport : <span class="ex">by car, by train, by bus</span> · mais <b>on foot</b> (à pied).</p>
      <p><b>Le voyage :</b> ticket (billet) · single / return ticket (aller simple / aller-retour) · platform (quai) · timetable (horaires) · luggage (bagages) · passport · to get on / off (monter / descendre) · to miss the bus (rater le bus) · delayed (en retard)</p>''',
  [V("🚗", "la voiture", "car", "voiture", "carriage"), V("🚌", "le bus", "bus", "buss", "coach car"), V("🚆", "le train", "train", "trane", "railway"),
   V("✈️", "l'avion", "plane", "avion", "airplain"), V("🚲", "le vélo", "bike", "velo", "cycle bike"), V("🚇", "le métro (Londres)", "underground", "metro way", "subterrain"),
   V("🎫", "le billet", "ticket", "bill", "note"), V("🧳", "les bagages", "luggage", "baggages", "bagages"), V("", "le quai (de gare)", "platform", "quay", "dock"), V("", "un aller-retour", "a return ticket", "a go-back ticket", "a round"),
  ],
  [S("🚗", "la voiture", "car"), S("🚆", "le train", "train"), S("✈️", "l'avion", "plane", ("airplane", "aeroplane")), S("🚲", "le vélo", "bike", ("bicycle",)), S("🚢", "le bateau", "boat", ("ship",)),
   S("🏍️", "la moto", "motorbike", ("motorcycle",)), S("🎫", "le billet", "ticket"), S("🧳", "les bagages", "luggage"), S("", "le car (autocar)", "coach"), S("", "le passeport", "passport")],
  [L("coach", "le car, l'autocar", "l'entraîneur sportif", "le carrosse"), L("platform", "le quai", "la plateforme pétrolière", "le hall"), L("luggage", "les bagages", "le luxe", "le billet"),
   L("delayed", "en retard", "annulé", "à l'heure"), L("return ticket", "un aller-retour", "un aller simple", "un remboursement"), L("underground", "le métro", "le sous-sol", "le parking"),
   L("motorbike", "la moto", "le moteur", "le vélo"), L("on foot", "à pied", "au pied", "en bus")],
  {"by": ("choice", "by ou on ?", [
      C("I go to school ____ bus.", ["by", "on", "in"], keep=True, tip="by + moyen de transport."), C("She goes to work ____ foot.", ["on", "by", "in"], keep=True, tip="à pied → on foot."),
      C("We travelled to London ____ train.", ["by", "on", "with"], keep=True, tip="by train."), C("They came ____ car.", ["by", "on", "with"], keep=True, tip="by car."),
  ])}, [M("by", "🚦", "by car ou on foot ?", "Le bon petit mot.", ["by"], 4)])

# ═════════════ ÉMOTIONS ═════════════
lex("emotions.html", "Les émotions et la personnalité – Entraînement", 'How do you <span>feel</span>?', "Émotions et traits de caractère", ("#fbcfe8", "#ec4899"),
  '''      <p><b>How do you feel? / How are you?</b> → I feel… / I'm…</p>
      <p><b>Émotions :</b> happy (heureux) · sad (triste) · angry (en colère) · scared / afraid (effrayé) · tired (fatigué) · bored (qui s'ennuie) · excited (impatient, enthousiaste) · worried (inquiet) · surprised · nervous (stressé) · proud (fier) · embarrassed (gêné)</p>
      <p><b>Personnalité :</b> kind (gentil) · funny (drôle) · shy (timide) · lazy (paresseux) · hard-working (travailleur) · friendly (sympathique) · rude (impoli) · polite (poli) · brave (courageux) · generous</p>
      <p>Attention : <b>bored</b> = je m'ennuie · <b>boring</b> = ennuyeux (ce qui m'ennuie). Même chose : <i>interested / interesting, tired / tiring</i>.</p>''',
  [V("😊", "heureux", "happy", "happen", "glad man"), V("😢", "triste", "sad", "sorry", "tired"), V("😠", "en colère", "angry", "hungry", "anger"),
   V("😨", "effrayé", "scared", "scary", "scarred"), V("😴", "fatigué", "tired", "tiring", "sleepy man"), V("😟", "inquiet", "worried", "worrying", "nervous man"),
   V("😳", "gêné", "embarrassed", "pregnant", "embarrassing"), V("", "timide", "shy", "timid man", "shame"), V("", "paresseux", "lazy", "lousy", "crazy"), V("", "fier", "proud", "fierce", "pride")],
  [S("😊", "heureux", "happy"), S("😢", "triste", "sad"), S("😠", "en colère", "angry"), S("😨", "effrayé", "scared", ("afraid", "frightened")), S("😴", "fatigué", "tired"),
   S("", "gentil", "kind", ("nice",)), S("", "drôle", "funny"), S("", "timide", "shy"), S("", "paresseux", "lazy"), S("", "poli", "polite")],
  [L("angry", "en colère", "affamé", "triste"), L("worried", "inquiet", "fatigué", "pressé"), L("proud", "fier", "fort", "prudent"),
   L("bored", "qui s'ennuie", "ennuyeux", "fatigué"), L("excited", "impatient, enthousiaste", "excité seulement", "énervé"), L("rude", "impoli", "rude au toucher", "dur"),
   L("shy", "timide", "le ciel", "gêné"), L("hard-working", "travailleur", "dur à travailler", "fatigant")],
  {"ing": ("choice", "-ed ou -ing ?", [
      C("This film is so ____ . I'm falling asleep.", ["boring", "bored"], tip="le film ennuie → boring."), C("I'm ____ . There's nothing to do.", ["bored", "boring"], tip="je m'ennuie → bored."),
      C("The match was really ____ !", ["exciting", "excited"], tip="le match passionne → exciting."), C("I'm ____ in history.", ["interested", "interesting"], tip="je m'intéresse → interested."),
      C("Work is ____ . I need a holiday.", ["tiring", "tired"], tip="le travail fatigue → tiring."), C("She was ____ by the news.", ["surprised", "surprising"], tip="elle est surprise → surprised."),
  ])}, [M("ing", "🎭", "bored ou boring ?", "-ed (je ressens) ou -ing (ça provoque) ?", ["ing"], 6)])

# ═════════════ ANIMAUX ═════════════
lex("animaux.html", "Les animaux – Entraînement", 'Les <span>animaux</span>', "Animals", ("#bbf7d0", "#22c55e"),
  '''      <p><b>Animaux domestiques :</b> dog · cat · rabbit (lapin) · hamster · fish · bird (oiseau) · guinea pig (cochon d'Inde)</p>
      <p><b>À la ferme :</b> cow (vache) · horse (cheval) · pig (cochon) · sheep (mouton) · chicken / hen (poule) · duck (canard) · goat (chèvre)</p>
      <p><b>Animaux sauvages :</b> lion · tiger · elephant · monkey (singe) · bear (ours) · wolf (loup) · fox (renard) · snake (serpent) · whale (baleine) · shark (requin) · mouse / mice (souris)</p>''',
  [V("🐄", "la vache", "cow", "vach", "calf"), V("🐷", "le cochon", "pig", "pork", "coach"), V("🐑", "le mouton", "sheep", "ship", "mutton"),
   V("🐒", "le singe", "monkey", "donkey", "singer"), V("🐻", "l'ours", "bear", "beer", "bore"), V("🐺", "le loup", "wolf", "loop", "fox"),
   V("🦊", "le renard", "fox", "wolf", "renard"), V("🐍", "le serpent", "snake", "snack", "serpent"), V("🐋", "la baleine", "whale", "wall", "baleen"),
   V("🦆", "le canard", "duck", "canard", "dock"), V("🐰", "le lapin", "rabbit", "lapin", "hare bit"), V("🐐", "la chèvre", "goat", "goal", "sheep")],
  [S("🐶", "le chien", "dog"), S("🐱", "le chat", "cat"), S("🐴", "le cheval", "horse"), S("🐄", "la vache", "cow"), S("🐷", "le cochon", "pig"),
   S("🐒", "le singe", "monkey"), S("🐻", "l'ours", "bear"), S("🐦", "l'oiseau", "bird"), S("🐭", "la souris", "mouse"), S("🐍", "le serpent", "snake")],
  [L("monkey", "le singe", "l'âne", "la monnaie"), L("bear", "l'ours", "la bière", "le sanglier"), L("sheep", "le mouton", "le bateau", "la chèvre"),
   L("whale", "la baleine", "le requin", "le mur"), L("goat", "la chèvre", "le but", "le mouton"), L("duck", "le canard", "le chien", "le quai"),
   L("wolf", "le loup", "le renard", "la laine"), L("rabbit", "le lapin", "le rat", "le lièvre seulement")])

# ═════════════ ARGENT ET SHOPPING ═════════════
newpage("argent_shopping.html", "L'argent et le shopping – Entraînement", 'How <span>much</span> is it?',
  "Faire des achats, l'argent, les magasins", ("#86efac", "#16a34a"),
  '''      <p><b>L'argent :</b> money · cash (espèces) · a coin (une pièce) · a note (un billet) · change (la monnaie rendue) · a credit card · a receipt (ticket de caisse) · cheap (pas cher) · expensive (cher) · a discount (une réduction) · the sales (les soldes)</p>
      <p><b>Les magasins :</b> baker's (boulangerie) · butcher's (boucherie) · chemist's (pharmacie) · newsagent's (marchand de journaux) · clothes shop · shoe shop · supermarket · bookshop (librairie)</p>
      <p><b>Phrases utiles :</b> <span class="ex">How much is it? / How much are they? · Can I pay by card? · Have you got this in a smaller size? · I'll take it. · I'm just looking, thanks.</span></p>''',
  {"vocab": ("choice", "Quel est le mot anglais ?", [
      V("💶", "un billet (de banque)", "a note", "a ticket", "a bill paper"), V("🪙", "une pièce de monnaie", "a coin", "a piece", "a corner"), V("", "pas cher", "cheap", "chip", "expensive"),
      V("", "cher", "expensive", "dear money", "cheap"), V("", "la monnaie (rendue)", "change", "money back", "coins back"), V("", "les soldes", "the sales", "the soldes", "the sold"),
      V("🥖", "la boulangerie", "baker's", "boulanger", "bread shop man"), V("📚", "la librairie", "bookshop", "library", "book library"), V("", "une réduction", "a discount", "a reduction price", "a less"),
    ]),
    "phr": ("choice", "Quelle est la bonne phrase ?", [
      C(None, ["How much is it?", "How many is it?", "How much it costs?"], fr="Vous demandez le prix d'un article."),
      C(None, ["How much are these shoes?", "How much is these shoes?", "How many cost these shoes?"], fr="Vous demandez le prix de ces chaussures."),
      C(None, ["Can I pay by card?", "Can I pay with card?", "Can I pay in card?"], fr="Vous demandez si vous pouvez payer par carte."),
      C(None, ["I'm just looking, thanks.", "I'm only watching, thanks.", "I look only, thanks."], fr="Le vendeur vous propose de l'aide, mais vous regardez seulement."),
      C(None, ["Have you got this in a smaller size?", "Have you this in smaller size?", "You have it more small?"], fr="Vous voulez une taille plus petite."),
      C(None, ["I'll take it.", "I take it now.", "I will to take it."], fr="Vous décidez d'acheter l'article."),
    ]),
    "listen": ("choice", "Écoute : que veut dire ce mot ?", [
      L("receipt", "le ticket de caisse", "la recette", "le reçu bancaire"), L("cash", "les espèces", "la caisse", "la carte"), L("change", "la monnaie rendue", "le change", "le chèque"),
      L("cheap", "pas cher", "la puce", "cher"), L("discount", "une réduction", "un décompte", "une remise en question"), L("newsagent's", "le marchand de journaux", "l'agence de presse", "la librairie"),
    ])},
  [M("vocab", "💶", "Le vocabulaire", "coin, note, cheap, discount…", ["vocab"], 9),
   M("phr", "🛍️", "Les phrases utiles", "How much is it? Can I pay by card?", ["phr"], 6),
   M("listen", "🔊", "Écoute et comprends", "Écoute le mot et trouve sa traduction.", ["listen"], 6),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["vocab", "phr", "listen"], 12)], tag="Anglais · Lexique")
print("content9 ok", REGISTRY)
