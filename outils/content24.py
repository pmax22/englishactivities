import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
exec(open(_EA_OUT+"/content_helpers.py", encoding="utf-8").read())
SOC, PRA = "Anglais · Sociolinguistique", "Anglais · Pragmatique"
def ask(fr, opts, tip=None): return C(None, opts, fr=fr, tip=tip)

# ════════════════════ SOCIOLINGUISTIQUE ════════════════════
LES = '''      <p>L'anglais se prononce de façons très différentes selon les régions et les milieux sociaux. Aucun accent n'est « meilleur » qu'un autre !</p>
      <p><b>RP</b> (Received Pronunciation, « l'anglais de la BBC ») : accent britannique de référence, non rhotique : le <i>r</i> final ne se prononce pas (<i>car</i> = /kɑː/).</p>
      <p><b>General American</b> : accent américain de référence, <b>rhotique</b> (<i>car</i> = /kɑːr/) ; le <i>t</i> entre deux voyelles devient presque un <i>d</i> : <i>water</i> → « wader ».</p>
      <p><b>Cockney</b> (Londres) : <i>h</i> muet (<i>'ouse</i>), coup de glotte (<i>wa'er</i>), <i>th</i> → <i>f</i> (<i>fink</i>), argot rimé (<i>apples and pears</i> = stairs).</p>
      <p><b>Écossais</b> : <i>r</i> roulé, <i>loch</i>, <i>wee</i> (petit), <i>aye</i> (oui) · <b>Irlandais</b> : <i>th</i> → <i>t</i> (<i>tree</i> pour three), <i>grand</i> (très bien), <i>craic</i> · <b>Sud des USA</b> : voyelles traînantes (<i>drawl</i>), <i>y'all</i> · <b>Australien</b> : intonation montante, <i>day</i> sonne presque comme « die », <i>mate</i></p>
      <p><b>Anglais indien</b> : <i>r</i> et <i>t</i> rétroflexes, rythme syllabique, expressions comme <i>prepone</i> (avancer un rendez-vous).</p>'''
A1 = [ask("Le h ne se prononce pas (« 'ouse » pour house), « water » devient « wa'er ».", ["Cockney", "Scottish", "General American"]),
      ask("Le r est roulé, on dit « wee » pour petit et « aye » pour oui.", ["Scottish", "Australian", "Cockney"]),
      ask("« Three » sonne comme « tree » et « That's grand! » veut dire « C'est super ! »", ["Irish", "Indian", "RP"]),
      ask("Le r final se prononce toujours et « water » sonne comme « wader ».", ["General American", "RP", "Cockney"]),
      ask("Voyelles allongées et traînantes, « y'all » pour vous tous.", ["Southern American", "Scottish", "Australian"]),
      ask("Intonation qui monte en fin de phrase, « G'day, mate! ».", ["Australian", "Irish", "Southern American"]),
      ask("Accent « de la BBC », sans r final, considéré comme la référence britannique.", ["RP", "Cockney", "General American"]),
      ask("« Apples and pears » veut dire « stairs » : c'est de l'argot rimé.", ["Cockney", "Irish", "Indian"]),
      ask("« Can we prepone the meeting? » (avancer la réunion).", ["Indian English", "Scottish English", "Australian English"]),
      ask("« I fink so » : le th devient f.", ["Cockney", "RP", "General American"])]
A2 = [C("car", ["/kɑːr/ (r prononcé)", "/kɑː/ (r muet)"], fr="Comment un Américain prononce-t-il ce mot ?", keep=True),
      C("car", ["/kɑː/ (r muet)", "/kɑːr/ (r prononcé)"], fr="Comment prononce-t-on ce mot en RP (anglais britannique standard) ?", keep=True),
      C("water", ["« wader » (t presque comme un d)", "« wa'er » (coup de glotte)", "« water » (t bien net)"], fr="Prononciation américaine ?", keep=True),
      C("water", ["« wa'er » (coup de glotte)", "« wader »", "« vater »"], fr="Prononciation cockney ?", keep=True),
      C(None, ["rhotique", "non rhotique"], fr="Un accent où le r final se prononce (comme en Écosse, en Irlande ou aux USA) est…", keep=True),
      C(None, ["non rhotique", "rhotique"], fr="Un accent où le r final ne se prononce pas (RP, Australie, Cockney) est…", keep=True)]
newpage("so_accents.html", "Les accents de l'anglais", 'Accents of <span>English</span>', "RP, General American, Cockney, écossais, irlandais, australien, indien",
  ("#c4b5fd", "#6d28d9"), LES,
  {"a1": ("choice", "Quel accent ?", A1), "a2": ("choice", "Rhotique ou pas ?", A2)},
  [M("a1", "🗺️", "Reconnaître un accent", "Associe chaque description à un accent.", ["a1"], 10),
   M("a2", "👂", "Le r et le t", "Accents rhotiques, coup de glotte, t américain.", ["a2"], 6)], tag=SOC)

LES = '''      <p>Un <b>dialecte</b> n'est pas de l'anglais « fautif » : c'est une variété avec ses propres règles, aussi cohérentes que celles de l'anglais standard. Les linguistes étudient ces règles sans les juger.</p>
      <p><b>AAVE</b> (African American Vernacular English) : <i>habitual be</i> : <i>She be working</i> = elle travaille habituellement · absence de copule : <i>He tired</i> = he is tired · double négation : <i>I don't know nothing</i> · <i>finna</i> = about to · <i>ain't</i>.</p>
      <p><b>Créole jamaïcain (Patwa)</b> : <i>Wah gwaan?</i> = What's going on? · <i>Mi deh yah</i> = I'm here · <i>Mi nuh know</i> = I don't know · <i>Unu</i> = you (plural) · <i>Likkle</i> = little.</p>
      <p>Ces variétés ont beaucoup influencé l'anglais des jeunes du monde entier, à travers le hip-hop, le reggae et le <b>Multicultural London English</b> (<i>innit, bare</i> = beaucoup, <i>peng</i> = beau).</p>
      <p>On parle de <b>code-switching</b> quand une personne passe d'une variété à l'autre selon la situation.</p>'''
D1 = [C("She be working on Saturdays.", ["She usually works on Saturdays.", "She is working right now.", "She will work on Saturday."], fr="AAVE : que signifie cette phrase ?", tip="Le « habitual be » marque l'habitude."),
      C("He tired.", ["He is tired.", "He was tired.", "He tires."], fr="AAVE : que signifie cette phrase ?", tip="Absence de la copule be."),
      C("I'm finna leave.", ["I'm about to leave.", "I finally left.", "I'm fine and I leave."], fr="AAVE : que signifie « finna » ?"),
      C("I don't know nothing about it.", ["I don't know anything about it.", "I know everything about it.", "I know nothing, I'm lying."], fr="AAVE : que signifie cette phrase ?", tip="Double négation = une seule négation en anglais standard."),
      C("Wah gwaan?", ["What's going on?", "Where are you going?", "Who's gone?"], fr="Jamaïcain : que signifie cette question ?"),
      C("Mi deh yah.", ["I'm here.", "I'm tired.", "I'm going."], fr="Jamaïcain : que signifie cette phrase ?"),
      C("Mi nuh know.", ["I don't know.", "I know now.", "My new knowledge."], fr="Jamaïcain : que signifie cette phrase ?"),
      C("Unu ready?", ["Are you (all) ready?", "Is one ready?", "Are we ready?"], fr="Jamaïcain : que signifie « unu » ?"),
      C("There were bare people at the party, innit.", ["There were lots of people at the party, weren't there?", "There were no people at the party.", "People were naked at the party."], fr="Multicultural London English : que signifie cette phrase ?"),
      C("That dress is peng!", ["That dress is beautiful!", "That dress is expensive!", "That dress is ugly!"], fr="Multicultural London English : que signifie « peng » ?")]
D2 = [C(None, ["C'est une variété avec ses propres règles.", "C'est de l'anglais plein de fautes.", "C'est une langue inventée par les jeunes."], fr="Pour un linguiste, l'AAVE…"),
      C(None, ["Passer d'une variété de langue à une autre selon la situation.", "Changer de mot de passe.", "Traduire mot à mot."], fr="Le code-switching, c'est…"),
      C(None, ["Le hip-hop et le reggae.", "La BBC et la presse de qualité.", "Les dictionnaires."], fr="Qu'est-ce qui a diffusé ces variétés dans le monde ?")]
newpage("so_dialectes.html", "Dialectes : AAVE et créole jamaïcain", 'Dialects <span>&amp; creoles</span>', "AAVE, créole jamaïcain, anglais multiculturel de Londres",
  ("#fcd34d", "#065f46"), LES,
  {"d1": ("choice", "Que signifie cette phrase ?", D1), "d2": ("choice", "Comprendre les dialectes", D2)},
  [M("d1", "🗝️", "Décoder", "Traduis en anglais standard.", ["d1"], 10),
   M("d2", "🔬", "Regard de linguiste", "Ce qu'est (et n'est pas) un dialecte.", ["d2"], 3)], tag=SOC)

LES = '''      <p>Parler une langue, c'est aussi connaître les <b>codes sociaux</b> de ceux qui la parlent.</p>
      <p><b>Small talk</b> : on parle de la météo, du week-end, du trajet… pas du salaire, de la religion ni de la politique avec des inconnus.</p>
      <p><b>« How are you? »</b> n'est pas une vraie question : on répond <i>Fine, thanks. And you?</i> · <b>« Sorry »</b> se dit très souvent, même quand ce n'est pas notre faute.</p>
      <p><b>Saluer</b> : poignée de main ou simple <i>Hi</i> ; pas de bise ! · Au travail, on utilise souvent le <b>prénom</b>, même avec son chef.</p>
      <p><b>Pourboire</b> : aux États-Unis, 15 à 20 % au restaurant (le service n'est pas inclus) ; au Royaume-Uni, environ 10 % si le service n'est pas compté.</p>
      <p><b>Faire la queue</b> est sacré au Royaume-Uni · La <b>ponctualité</b> compte au travail, mais à une fête on arrive souvent un peu après l'heure.</p>'''
K1 = [ask("Un collègue anglais te demande « How are you? » en passant.", ["Fine, thanks. And you?", "Not great, my back hurts and I slept badly…", "Why do you ask?"], "C'est une formule, pas une vraie question."),
      ask("Tu dois faire la conversation (small talk) avec un client.", ["Lovely weather today, isn't it?", "How much do you earn?", "Who did you vote for?"]),
      ask("Tu rencontres ton tuteur de stage britannique pour la première fois.", ["Tu lui serres la main.", "Tu lui fais la bise.", "Tu le prends dans tes bras."]),
      ask("Au restaurant aux États-Unis, l'addition est de 50 $. Quel pourboire laisser ?", ["Environ 8 à 10 $", "Rien, le service est compris", "50 $"], "15 à 20 % aux USA."),
      ask("À l'arrêt de bus à Londres, plusieurs personnes attendent.", ["Tu te mets au bout de la file.", "Tu montes en premier.", "Tu attends sur le côté et tu fonces quand le bus arrive."]),
      ask("Quelqu'un te bouscule dans la rue à Londres.", ["Il y a de bonnes chances que vous disiez « Sorry! » tous les deux.", "Il faut exiger des excuses.", "On ne dit rien."]),
      ask("Ta manager s'appelle Sarah Jones et te dit « Call me Sarah ».", ["Tu l'appelles Sarah.", "Tu continues à dire Madam Jones.", "Tu l'appelles Boss."]),
      ask("On t'invite à une fête « from 8 pm ».", ["Arriver vers 8 h 15 – 8 h 30 est normal.", "Il faut arriver à 7 h 30.", "On peut arriver à minuit."]),
      ask("Quel sujet éviter avec un collègue que tu connais peu ?", ["La religion et la politique.", "Le week-end.", "Les séries télé."]),
      ask("On te dit « Thank you! » après un service.", ["You're welcome! / No problem!", "Yes.", "Thank you too, goodbye."])]
newpage("so_codes_sociaux.html", "Les codes sociaux du monde anglophone", 'Social <span>codes</span>', "Small talk, politesse, pourboires, file d'attente : les règles non écrites",
  ("#bbf7d0", "#047857"), LES,
  {"k1": ("choice", "Que fais-tu dans cette situation ?", K1)},
  [M("k1", "🤝", "Les règles non écrites", "Choisis le comportement adapté.", ["k1"], 10)], tag=SOC)

LES = '''      <p>Certains sujets sont <b>tabous</b> ou délicats en pays anglophone, et certains mots sont devenus <b>offensants</b>. Le <b>langage inclusif</b> évite d'exclure ou de blesser.</p>
      <p><b>Questions à éviter</b> : <i>How much do you earn? How old are you? How much do you weigh?</i> (avec des inconnus ou des collègues).</p>
      <p><b>Mots neutres</b> : <i>firefighter</i> (pas fireman), <i>police officer</i> (pas policeman), <i>flight attendant</i> (pas stewardess), <i>chairperson</i>, <i>humankind</i>.</p>
      <p><b>They</b> peut désigner une seule personne dont on ne connaît pas le genre, ou qui préfère ce pronom : <i>Someone left their bag. Ask them.</i></p>
      <p><b>Handicap</b> : <i>a person with a disability, a wheelchair user</i> · <b>Âge</b> : <i>older people, senior citizens</i></p>
      <p><b>Euphémismes</b> : <i>to pass away</i> (mourir) · <i>between jobs</i> (au chômage) · <i>restroom / bathroom</i> (toilettes, USA) · <i>to let someone go</i> (licencier)</p>'''
T1 = [C("fireman", ["firefighter", "fire guy", "fire officer lady"], fr="Choisis le mot neutre (non genré)."), C("policeman", ["police officer", "police person man", "cop lady"], fr="Choisis le mot neutre."),
      C("stewardess", ["flight attendant", "air girl", "plane waitress"], fr="Choisis le mot neutre."), C("chairman", ["chairperson", "chairboy", "seat man"], fr="Choisis le mot neutre."),
      C("mankind", ["humankind", "peoplekind", "menkind"], fr="Choisis le mot neutre."), C("businessmen", ["businesspeople", "businessmans", "business guys"], fr="Choisis le mot neutre.")]
T2 = [C("He died last year.", ["He passed away last year.", "He went away last year.", "He passed last year's exam."], fr="Choisis l'euphémisme plus délicat."),
      C("I'm unemployed.", ["I'm between jobs.", "I'm on holiday.", "I'm retired."], fr="Choisis l'euphémisme."),
      C("Where are the toilets? (USA)", ["Where's the restroom?", "Where's the toilet room?", "Where's the WC box?"], fr="Formulation la plus courante et polie aux USA."),
      C("They fired him.", ["They let him go.", "They let him in.", "They let him down."], fr="Choisis l'euphémisme."),
      C("old people", ["older people / senior citizens", "ancient people", "old ones"], fr="Choisis la formulation respectueuse."),
      C("a disabled", ["a person with a disability", "a handicap", "an invalid"], fr="Choisis la formulation respectueuse.")]
T3 = [ask("Someone left ____ umbrella in the classroom. (genre inconnu)", ["their", "his", "its"], "they / their pour une personne dont on ne connaît pas le genre."),
      ask("Quelle question est la plus acceptable avec un collègue britannique ?", ["Did you have a nice weekend?", "How much do you earn?", "How old are you exactly?"]),
      ask("Un client te demande ton salaire. Tu réponds poliment…", ["Oh, I'd rather not say, sorry!", "Mind your own business!", "More than you!"]),
      ask("Alex préfère le pronom « they ». Comment parler d'Alex ?", ["They are coming later.", "He is coming later.", "It is coming later."])]
newpage("so_tabous.html", "Tabous et langage inclusif", 'Taboos <span>&amp; inclusive language</span>', "Sujets délicats, mots neutres, euphémismes",
  ("#fecaca", "#9f1239"), LES,
  {"t1": ("choice", "Choisis le mot neutre", T1), "t2": ("choice", "Choisis la formulation délicate", T2), "t3": ("choice", "En situation", T3)},
  [M("t1", "⚖️", "Mots neutres", "firefighter, police officer, flight attendant…", ["t1"], 6),
   M("t2", "🕊️", "Euphémismes", "Dire les choses avec délicatesse.", ["t2"], 6),
   M("t3", "💬", "En situation", "Questions à éviter et pronom « they ».", ["t3"], 4)], tag=SOC)

# ════════════════════ PRAGMATIQUE ════════════════════
LES = '''      <p><b>Répondre</b> : <i>Good morning, Green's Supermarket, Emma speaking. How can I help you?</i></p>
      <p><b>Demander quelqu'un</b> : <i>Could I speak to Mr Brown, please?</i> → <i>Who's calling, please? / Hold on, please. / I'll put you through.</i></p>
      <p><b>Absent</b> : <i>I'm afraid he's not available at the moment. Can I take a message? / Would you like to leave a message?</i></p>
      <p><b>Problèmes</b> : <i>Could you speak up, please? / Could you repeat that? / Could you spell that, please? / Sorry, the line is bad.</i></p>
      <p><b>Épeler et dicter</b> : <i>double L</i> (ll) · <i>@</i> = <i>at</i> · <i>.</i> = <i>dot</i> · <i>_</i> = <i>underscore</i> · <i>-</i> = <i>hyphen / dash</i> · <i>0</i> = <i>oh</i> ou <i>zero</i> · <i>33</i> = <i>double three</i></p>
      <p><b>Message vocal</b> : <i>Hello, this is Léa Martin. I'm calling about… Could you call me back on…? Thank you, bye.</i></p>'''
P1 = [ask("Tu décroches au magasin.", ["Good morning, Green's Supermarket, how can I help you?", "Yes? What?", "Allo, who is it?"]),
      ask("Tu veux parler à Mr Brown.", ["Could I speak to Mr Brown, please?", "Give me Mr Brown.", "Is Brown here or not?"]),
      ask("Tu demandes qui appelle.", ["Who's calling, please?", "Who are you?", "What's your problem?"]),
      ask("Tu fais patienter la personne.", ["Hold on, please.", "Stop talking.", "Wait me."]),
      ask("Tu transfères l'appel.", ["I'll put you through.", "I'll put you down.", "I'll put you out."]),
      ask("Mr Brown est absent.", ["I'm afraid he's not available. Can I take a message?", "He's not here, bye.", "Call later, I'm busy."]),
      ask("Tu n'entends pas bien.", ["Could you speak up, please?", "Shout!", "Speak more big."]),
      ask("Tu veux que la personne épelle son nom.", ["Could you spell that, please?", "Write it.", "How do you letter it?"]),
      ask("Tu termines l'appel.", ["Thank you for calling. Goodbye!", "OK bye bye finish.", "End."]),
      ask("Message vocal : tu demandes qu'on te rappelle.", ["Could you call me back on 06 12 34 56 78?", "Call me now!", "You must phone me."])]
P2 = [C("lea.martin@mail.com", ["lea dot martin at mail dot com", "lea point martin arobase mail point com", "lea full stop martin at mail full stop com"], fr="Comment dicte-t-on cette adresse email ?"),
      C("tom_baker@shop.co.uk", ["tom underscore baker at shop dot co dot uk", "tom dash baker at shop dot co dot uk", "tom line baker arobase shop point co point uk"], fr="Comment dicte-t-on cette adresse ?"),
      C("Phillips", ["P-H-I-double L-I-P-S", "P-H-I-two L-I-P-S", "P-H-I-L-L-I-P-S-S"], fr="Comment épelle-t-on ce nom ?"),
      C("0207 334 9010", ["oh two oh seven, double three four, nine oh one oh", "zero two zero seven, three three four, nine zero ten", "o two hundred seven, three hundred thirty-four, ninety ten"], fr="Comment dicte-t-on ce numéro (à la britannique) ?"),
      C("Smith-Jones", ["S-M-I-T-H hyphen J-O-N-E-S", "S-M-I-T-H line J-O-N-E-S", "S-M-I-T-H and J-O-N-E-S"], fr="Comment épelle-t-on ce nom composé ?")]
P3 = [O("Good morning, Green's Supermarket, how can I help you?|Hello, could I speak to the manager, please?|Who's calling, please?|This is Paul Smith from Fresh Farms.|Hold on, please, I'll put you through.",
        "Remets l'appel dans l'ordre : demander le responsable."),
      O("Hello, Bella Shoes, Lucie speaking.|Hi, could I speak to Mr Lee, please?|I'm afraid he's not available. Can I take a message?|Yes, could you ask him to call me back?|Of course. Could you spell your name, please?",
        "Remets l'appel dans l'ordre : prendre un message.")]
newpage("pr_telephone.html", "Au téléphone", 'On the <span>phone</span>', "Répondre, transférer, prendre un message, épeler, laisser un message vocal",
  ("#93c5fd", "#1d4ed8"), LES,
  {"p1": ("choice", "Que dis-tu au téléphone ?", P1), "p2": ("choice", "Épeler et dicter", P2), "p3": ("order", "Remets l'appel dans l'ordre", P3)},
  [M("p1", "📞", "Les phrases du téléphone", "Répondre, transférer, prendre un message.", ["p1"], 10),
   M("p2", "🔤", "Épeler et dicter", "Adresses email, noms, numéros.", ["p2"], 5),
   M("p3", "🧩", "Un appel complet", "Remets les répliques dans l'ordre.", ["p3"], 2)], tag=PRA)

LES = '''      <p>Face à un client mécontent, on applique la méthode <b>LAST</b> :</p>
      <p><span class="hl">Listen</span> — écouter sans interrompre : <i>I see. / Go on, please.</i></p>
      <p><span class="hl">Apologise</span> — s'excuser au nom du magasin : <i>I'm very sorry about that. / I do apologise for the inconvenience.</i></p>
      <p><span class="hl">Solve</span> — proposer une solution : <i>Would you like a refund or an exchange? / Let me see what I can do. / I'll call my manager.</i></p>
      <p><span class="hl">Thank</span> — remercier : <i>Thank you for your patience. / Thank you for letting us know.</i></p>
      <p><b>À éviter</b> : <i>It's not my fault. / Calm down! / That's impossible.</i> · <b>Vocabulaire</b> : <i>a refund</i> (remboursement), <i>an exchange</i>, <i>a receipt</i> (ticket de caisse), <i>faulty / damaged</i> (défectueux / abîmé), <i>a credit note</i> (avoir).</p>'''
R1 = [ask("« This kettle doesn't work! I bought it yesterday! »", ["I'm very sorry about that. Do you have your receipt?", "It's not my fault.", "Calm down, please!"]),
      ask("Le client explique longuement son problème.", ["I see. Go on, please.", "Hurry up, I'm busy.", "Yes, yes, I know."]),
      ask("Tu proposes une solution.", ["Would you like a refund or an exchange?", "You can't do anything.", "Buy another one."]),
      ask("Tu ne peux pas décider seul(e).", ["Let me call my manager.", "That's impossible.", "Go away."]),
      ask("Le client n'a pas son ticket de caisse.", ["I'm afraid I can't refund it without a receipt, but I can offer you a credit note.", "No receipt, no money, bye.", "You're lying."]),
      ask("Le problème est réglé.", ["Thank you for your patience.", "Finally!", "Don't come back."]),
      ask("Le client a attendu longtemps.", ["I do apologise for the wait.", "Everyone waits.", "It's normal."]),
      ask("Le produit est arrivé abîmé.", ["I'm sorry it arrived damaged. We'll send you a new one.", "It was fine when it left.", "Too bad."])]
R2 = [C("I see. Go on, please.", ["Listen", "Apologise", "Solve", "Thank"], keep=True, fr="Quelle étape de la méthode LAST ?"),
      C("I do apologise for the inconvenience.", ["Apologise", "Listen", "Solve", "Thank"], keep=True, fr="Quelle étape ?"),
      C("Would you like a refund or an exchange?", ["Solve", "Listen", "Apologise", "Thank"], keep=True, fr="Quelle étape ?"),
      C("Thank you for letting us know.", ["Thank", "Solve", "Listen", "Apologise"], keep=True, fr="Quelle étape ?"),
      C("un remboursement", ["a refund", "a refunding", "a reimbursal"], fr="Vocabulaire : comment dit-on…"), C("un ticket de caisse", ["a receipt", "a recipe", "a ticket"], fr="Vocabulaire : comment dit-on…"),
      C("défectueux", ["faulty", "faultless", "defective-ing"], fr="Vocabulaire : comment dit-on…"), C("un avoir", ["a credit note", "a have", "a bill"], fr="Vocabulaire : comment dit-on…")]
newpage("pr_reclamation.html", "Gérer une réclamation client", 'Dealing with <span>complaints</span>', "La méthode LAST : écouter, s'excuser, résoudre, remercier",
  ("#fca5a5", "#b91c1c"), LES,
  {"r1": ("choice", "Que réponds-tu au client ?", R1), "r2": ("choice", "Méthode et vocabulaire", R2)},
  [M("r1", "😤", "Un client mécontent", "Choisis la bonne réponse à chaque étape.", ["r1"], 8),
   M("r2", "🛠️", "La méthode LAST", "Reconnais les étapes et le vocabulaire.", ["r2"], 8)], tag=PRA)

LES = '''      <p><b>Découvrir le besoin</b> : <i>What are you looking for? / Is it for you or a gift? / What's your budget?</i></p>
      <p><b>Argumenter</b> : parler des <b>avantages</b> pour le client, pas seulement des caractéristiques : <i>It's waterproof, so you can wear it in the rain.</i> · <i>It's on sale. / It's our best-seller.</i></p>
      <p><b>Vente additionnelle</b> : <i>Would you like the matching scarf? / Can I suggest…?</i></p>
      <p><b>Répondre aux objections</b> : <i>It's too expensive.</i> → <i>I understand. It's high quality, so it will last longer. / We also have a cheaper model.</i></p>
      <p><b>Conclure</b> : <i>Shall I wrap it for you? / Would you like to pay by card?</i></p>
      <p><b>Négocier</b> : <i>Could you do a better price? / If you buy two, I can give you 10% off. / Let's meet halfway. / That's my final offer.</i></p>'''
V1 = [ask("Tu découvres le besoin du client.", ["What are you looking for?", "Buy this one.", "We close in five minutes."]),
      ask("Tu demandes si c'est un cadeau.", ["Is it for you or is it a gift?", "Who is it for, tell me?", "Is it free?"]),
      ask("Tu présentes un avantage.", ["It's waterproof, so you can wear it in the rain.", "It's a coat.", "It has buttons."]),
      ask("Tu proposes un article complémentaire.", ["Would you like the matching scarf?", "Buy more things.", "Do you want everything?"]),
      ask("« It's too expensive. »", ["I understand. We also have a cheaper model.", "No, it isn't.", "Then go somewhere else."]),
      ask("Tu conclus la vente.", ["Shall I wrap it for you?", "So? Yes or no?", "Pay now."]),
      ask("Le client hésite.", ["Would you like to try it on?", "Hurry up, please.", "Everybody buys it."]),
      ask("Tu proposes une remise pour deux articles.", ["If you buy two, I can give you 10% off.", "Two is cheaper maybe.", "Buy two, it's obligatory."])]
V2 = [C("Could you do a better price?", ["Le client demande une réduction.", "Le client accepte le prix.", "Le client veut payer plus."], fr="Que se passe-t-il ?"),
      C("Let's meet halfway.", ["Coupons la poire en deux.", "Rencontrons-nous à mi-chemin dans la rue.", "Arrêtons de négocier."], fr="Que signifie cette expression ?"),
      C("That's my final offer.", ["C'est ma dernière proposition.", "C'est ma première offre.", "C'est gratuit."], fr="Que signifie cette expression ?"),
      C("It's our best-seller.", ["C'est notre meilleure vente.", "C'est notre meilleur vendeur.", "C'est en solde."], fr="Que signifie cette expression ?"),
      C("It's on sale.", ["C'est en solde.", "C'est à vendre.", "C'est vendu."], fr="Que signifie cette expression ?"),
      C("It will last longer.", ["Il durera plus longtemps.", "Il arrivera plus tard.", "C'est le dernier."], fr="Que signifie cette expression ?")]
newpage("pr_vendre_negocier.html", "Vendre et négocier", 'Selling <span>&amp; negotiating</span>', "Découvrir le besoin, argumenter, répondre aux objections, conclure",
  ("#fde68a", "#d97706"), LES,
  {"v1": ("choice", "Que dis-tu au client ?", V1), "v2": ("choice", "Les expressions de la négociation", V2)},
  [M("v1", "🛍️", "Une vente réussie", "Du besoin du client à la conclusion.", ["v1"], 8),
   M("v2", "🤝", "Négocier", "Comprendre les expressions de la négociation.", ["v2"], 6)], tag=PRA)

LES = '''      <p><b>Structure d'un email professionnel :</b></p>
      <p>1. <b>Objet clair</b> : <i>Subject: Order #4521 – Delivery delay</i> · 2. <b>Salutation</b> : <i>Dear Mr Smith, / Dear Sir or Madam, / Hello Sarah,</i></p>
      <p>3. <b>But</b> : <i>I am writing to… (enquire about / complain about / confirm / apply for…)</i> · <i>I'm just following up on my email of 3 May.</i></p>
      <p>4. <b>Détails</b> · 5. <b>Action attendue</b> : <i>Could you please…? / I would be grateful if you could… / Please find attached…</i></p>
      <p>6. <b>Formule finale</b> : <i>I look forward to hearing from you.</i> · 7. <b>Signature</b> : <i>Kind regards, / Best regards, / Yours sincerely,</i> + nom, poste.</p>'''
E1 = [ask("Tu écris pour confirmer un rendez-vous.", ["I am writing to confirm our meeting on Monday at 10 a.m.", "Monday 10 OK.", "We meet Monday, yes?"]),
      ask("Tu relances un fournisseur qui n'a pas répondu.", ["I'm just following up on my email of 3 May.", "Why don't you answer?", "Answer me now."]),
      ask("Tu te plains d'une livraison en retard.", ["I am writing to complain about the late delivery of order #4521.", "Your delivery is rubbish.", "Where is my stuff?"]),
      ask("Tu joins un document.", ["Please find attached the invoice.", "Here is attached thing.", "Look at the paper."]),
      ask("Tu demandes poliment une action.", ["I would be grateful if you could send me a new catalogue.", "Send me a catalogue.", "I want a catalogue."]),
      ask("Formule finale avant la signature.", ["I look forward to hearing from you.", "Answer quickly.", "Bye bye."]),
      ask("Objet clair pour une réclamation.", ["Subject: Order #4521 – Damaged items", "Subject: Hello", "Subject: Problem!!!"]),
      ask("Tu remercies pour une réponse rapide.", ["Thank you for your quick reply.", "Good, you answered.", "Finally an answer."])]
E2 = [O("Subject: Order #4521 – Delivery delay|Dear Mr Smith,|I am writing about my order #4521 of 2 May.|The items have not arrived yet, although delivery was promised within five days.|Could you please tell me when I will receive them?|I look forward to hearing from you.|Kind regards, Emma Leroy",
        "Remets l'email dans l'ordre : retard de livraison."),
      O("Subject: Work placement application|Dear Sir or Madam,|I am writing to apply for a work placement in your shop.|I am a student in sales and I am available from June.|Please find attached my CV.|I look forward to hearing from you.|Yours faithfully, Hugo Bernard",
        "Remets l'email dans l'ordre : candidature de stage.")]
newpage("pr_email_pro.html", "L'email professionnel", 'The professional <span>email</span>', "Objet, salutation, but, demande, formule finale : relance, réclamation, confirmation",
  ("#a5f3fc", "#0e7490"), LES,
  {"e1": ("choice", "Choisis la bonne phrase", E1), "e2": ("order", "Remets l'email dans l'ordre", E2)},
  [M("e1", "✉️", "Les bonnes formules", "Confirmer, relancer, se plaindre, joindre un document.", ["e1"], 8),
   M("e2", "🧩", "Construire un email", "Remets les parties dans l'ordre.", ["e2"], 2)], tag=PRA)

LES = '''      <p><b>Accrocher</b> : une question (<i>Have you ever wondered…?</i>), un chiffre (<i>Did you know that…?</i>), une anecdote (<i>Last year, something happened to me…</i>).</p>
      <p><b>Annoncer le plan</b> : <i>Today I'm going to talk about… First, I'll… Then, I'll… Finally…</i></p>
      <p><b>Guider l'auditoire (signposting)</b> : <i>Let's move on to… / To illustrate this… / As you can see on this slide… / This brings me to my next point.</i></p>
      <p><b>Conclure</b> : <i>To sum up… / In conclusion… / Thank you for listening. Are there any questions?</i></p>
      <p><b>Répondre aux questions</b> : <i>That's a great question. / I'm not sure, but I'll find out. / Could you repeat the question?</i></p>
      <p><b>Conseils</b> : regarde ton public, parle lentement, fais des pauses, ne lis pas tes notes.</p>'''
S1 = [ask("Tu ouvres ta présentation par une question.", ["Have you ever wondered why we sleep?", "So, sleep. Here.", "I'm going to read my notes."]),
      ask("Tu annonces ton plan.", ["First, I'll explain…, then I'll show you…, and finally…", "There is a plan somewhere.", "I talk and you listen."]),
      ask("Tu passes à la partie suivante.", ["Let's move on to my second point.", "Next. Next. Next.", "Now other thing."]),
      ask("Tu montres un graphique.", ["As you can see on this slide, sales doubled.", "Look the slide.", "Slide is here."]),
      ask("Tu donnes un exemple.", ["To illustrate this, let me tell you a story.", "Example: example.", "I give example now."]),
      ask("Tu conclus.", ["To sum up, sleep is essential for our health.", "That's all, bye.", "Finished."]),
      ask("Tu invites les questions.", ["Thank you for listening. Are there any questions?", "Questions? No? Good.", "Don't ask questions."]),
      ask("On te pose une question dont tu ne connais pas la réponse.", ["I'm not sure, but I'll find out and let you know.", "That's a stupid question.", "I don't care."]),
      ask("Tu ouvres avec un chiffre.", ["Did you know that we spend a third of our lives asleep?", "Number: one third.", "Sleep is a lot."]),
      ask("Tu remercies le public au début.", ["Good morning everyone, and thank you for coming.", "Hello, sit down.", "OK, it's me."])]
S2 = [O("Good morning everyone, and thank you for coming.|Have you ever wondered why teenagers are always tired?|Today I'm going to talk about sleep.|First, I'll explain why we need sleep.|Then, I'll give you some tips to sleep better.|To sum up, sleep is essential.|Thank you for listening. Are there any questions?",
        "Remets la présentation dans l'ordre.")]
newpage("pr_prise_parole.html", "Prendre la parole en public", 'Public <span>speaking</span>', "Accrocher, annoncer le plan, guider, conclure, répondre aux questions",
  ("#fbcfe8", "#be185d"), LES,
  {"s1": ("choice", "Que dis-tu ?", S1), "s2": ("order", "Remets la présentation dans l'ordre", S2)},
  [M("s1", "🎤", "Les phrases de l'orateur", "De l'accroche aux questions du public.", ["s1"], 10),
   M("s2", "🧩", "Une présentation complète", "Remets les étapes dans l'ordre.", ["s2"], 1)], tag=PRA)
print("ok")
