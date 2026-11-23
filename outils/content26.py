import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
exec(open(_EA_OUT+"/cuhelp.py", encoding="utf-8").read())

# ═════════ 1066 ═════════
F = "cu_1066.html"
DZ(F, """
## L'Angleterre avant 1066
Après le départ des Romains au 5e siècle, des peuples germaniques, les **Anglo-Saxons**, s'installent en Grande-Bretagne et donnent naissance à l'anglais. Aux 9e et 10e siècles, les **Vikings** venus du Danemark et de Norvège envahissent une partie du pays. Au début de l'année 1066, le roi Édouard le Confesseur meurt sans enfant. Trois hommes revendiquent le trône : **Harold Godwinson**, un puissant seigneur anglais couronné aussitôt ; le roi de Norvège **Harald Hardrada** ; et **Guillaume**, duc de Normandie, cousin d'Édouard, qui affirme que la couronne lui avait été promise.

## Une année, trois batailles
En septembre 1066, Harald Hardrada débarque dans le nord de l'Angleterre. Harold le bat à Stamford Bridge. Mais quelques jours plus tard, Guillaume traverse la Manche et débarque dans le sud. Harold redescend à marche forcée avec une armée épuisée. Le **14 octobre 1066**, à **Hastings**, la bataille dure toute la journée. Les Normands, avec leurs cavaliers et leurs archers, finissent par l'emporter ; Harold est tué, selon la tradition, d'une flèche dans l'œil. Guillaume, désormais appelé **William the Conqueror**, est couronné à Westminster le jour de Noël 1066.

## La tapisserie de Bayeux
L'histoire de la conquête est racontée sur la **Bayeux Tapestry**, une broderie d'environ 70 mètres de long réalisée peu après les faits, probablement en Angleterre. C'est une véritable bande dessinée médiévale : on y voit la traversée en bateau, les chevaux, la bataille, la mort de Harold. Elle est conservée à Bayeux, en Normandie, et doit être prêtée au British Museum pendant sa restauration.

## Une nouvelle Angleterre
Les Normands remplacent l'aristocratie anglo-saxonne. Ils construisent des châteaux pour contrôler le pays, comme la **Tower of London**, et de grandes cathédrales. En 1086, Guillaume fait réaliser le **Domesday Book**, un immense inventaire de toutes les terres et richesses du royaume, pour lever les impôts.

## Le français dans l'anglais
Pendant près de trois siècles, la cour et la noblesse parlent français, tandis que le peuple parle anglais. C'est pourquoi l'anglais contient des milliers de mots d'origine française : *government*, *justice*, *army*, *castle*, *beef*, *pork*, *mutton*… Les animaux vivants gardent leur nom anglais (*cow*, *pig*, *sheep*), car ils sont élevés par les paysans anglophones ; la viande servie aux seigneurs prend un nom venu du français. Aujourd'hui encore, la devise de la monarchie britannique est en français : « Dieu et mon droit ».
""", """
a battle = une bataille
an arrow = une flèche
a king = un roi
a knight = un chevalier
a horse = un cheval
a castle = un château
a crown = une couronne
an army = une armée
""", [
 ("Combien d'hommes revendiquent le trône en 1066 ?", ["Trois", "Un seul", "Dix"], "Harold, Harald Hardrada et Guillaume."),
 ("Où et quand a lieu la bataille décisive ?", ["À Hastings, le 14 octobre 1066", "À Londres, en 1100", "À Bayeux, en 1066"], ""),
 ("Comment meurt Harold, selon la tradition ?", ["D'une flèche dans l'œil", "Noyé", "De vieillesse"], ""),
 ("Qu'est-ce que la tapisserie de Bayeux ?", ["Une longue broderie qui raconte la conquête", "Un château", "Un livre d'impôts"], ""),
 ("Pourquoi dit-on « pork » pour la viande et « pig » pour l'animal ?", ["La viande servie aux seigneurs francophones prend un nom venu du français", "C'est un hasard", "Pig est un mot viking"], ""),
], [("Édouard le Confesseur", "roi d'Angleterre de 1042 à 1066"), ("Stamford Bridge", "près de York, dans le nord de l'Angleterre"), ("Domesday Book", "le « livre du Jugement dernier »")])
D = "nc"
culture(F, "Culture : 1066, the Norman Conquest", '1066: the Norman <span>Conquest</span>',
  "Culture · Guillaume le Conquérant et la bataille de Hastings", ("#fde68a", "#92400e"),
  reperes("En 1066, Guillaume, duc de Normandie, conquiert l'Angleterre. C'est un tournant majeur : nouvelle noblesse, nouveaux châteaux… et des milliers de mots français dans la langue anglaise.",
    [("janvier 1066", "mort du roi Édouard le Confesseur"), ("25 sept. 1066", "Harold bat les Vikings à Stamford Bridge"), ("14 oct. 1066", "bataille de Hastings, mort de Harold"),
     ("25 déc. 1066", "Guillaume couronné roi à Westminster"), ("1086", "Domesday Book, inventaire du royaume")],
    "a battle, a conquest, a duke, a knight, an archer, a castle, a tapestry, the throne"),
  {D: doc("The year that changed England", [
    "In January 1066, the English king Edward the Confessor died without children. Three men wanted the crown: Harold, an English lord, Harald Hardrada, the king of Norway, and William, the Duke of Normandy, in France.",
    "Harold was crowned king. In September, he defeated the Norwegian army in the north of England. But a few days later, William landed in the south with thousands of soldiers and horses.",
    "On 14 October 1066, the two armies fought near Hastings. The battle lasted all day. In the end, the Normans won and Harold was killed, perhaps by an arrow in his eye. On Christmas Day, William was crowned king in Westminster. He is known as William the Conqueror.",
    "The Normans built many castles to control the country, like the Tower of London. The story of the conquest is told on the Bayeux Tapestry, a 70-metre embroidery, like a medieval comic strip.",
    "For about three centuries, the kings and nobles of England spoke French. That's why English has thousands of French words, like \"government\", \"castle\" or \"beef\". Even today, the motto of the British monarchy is in French: \"Dieu et mon droit\"."])},
  [TF(D, "Edward the Confessor had many children.", False, "« died without children »."),
   TF(D, "William was the Duke of Normandy.", True, "« the Duke of Normandy »."),
   TF(D, "The Battle of Hastings took place in 1066.", True, "« On 14 October 1066 »."),
   TF(D, "Harold won the Battle of Hastings.", False, "« the Normans won »."),
   TF(D, "The Bayeux Tapestry tells the story of the conquest.", True, "« The story of the conquest is told on the Bayeux Tapestry »."),
   TF(D, "The motto of the British monarchy is in Latin.", False, "En français : « Dieu et mon droit »." )],
  [Q(D, "Who defeated the Norwegian army?", ["Harold.", "William.", "Edward."]),
   Q(D, "When was William crowned?", ["On Christmas Day 1066.", "On 14 October 1066.", "In 1086."]),
   Q(D, "Why did the Normans build castles?", ["To control the country.", "For tourists.", "To keep the tapestry."]),
   Q(D, "Why does English have so many French words?", ["Kings and nobles spoke French for about three centuries.", "The English loved French food.", "Because of the Vikings."])],
  [DT(D, "Où est conservée la tapisserie ?", ["À Bayeux", "À Londres", "À Hastings", "À Rouen"]),
   DT(D, "Quel inventaire Guillaume fait-il réaliser en 1086 ?", ["Le Domesday Book", "La Magna Carta", "Le Bill of Rights", "Le First Folio"]),
   DT(D, "Comment appelle-t-on Guillaume ?", ["William the Conqueror", "William the Great", "William the Confessor", "William the Norman King of France"]),
   DT(D, "De quel pays vient Harald Hardrada ?", ["La Norvège", "La Normandie", "Le Danemark", "L'Écosse"])],
  [W(D, "Trouve le mot qui veut dire « flèche ».", ["arrow", "an arrow"]), W(D, "Trouve le mot qui veut dire « seigneur ».", "lord"),
   W(D, "Trouve le mot qui veut dire « broderie ».", ["embroidery", "an embroidery"]), W(D, "Trouve le mot qui veut dire « devise ».", "motto")])

# ═════════ TUDORS ═════════
F = "cu_tudors.html"
DZ(F, """
## Une nouvelle dynastie
En 1485, après une longue guerre civile entre deux familles nobles, la **Wars of the Roses** (la guerre des Deux-Roses, entre les York à la rose blanche et les Lancastre à la rose rouge), Henri Tudor bat le roi Richard III et devient **Henry VII**. Il épouse une princesse York pour réconcilier les deux camps : la rose des Tudors mêle le rouge et le blanc. Sa dynastie règne jusqu'en 1603.

## Henry VIII et ses six épouses
Son fils **Henry VIII** (1509-1547) est un roi cultivé et sportif, puis de plus en plus tyrannique. Il veut un fils pour lui succéder. Le pape refusant d'annuler son mariage avec Catherine d'Aragon, il rompt avec Rome et se proclame chef de la **Church of England** en 1534. Il ferme les monastères et s'empare de leurs richesses. Ses six épouses ont connu des destins tragiques ; les écoliers anglais apprennent une comptine pour s'en souvenir : « *Divorced, beheaded, died; divorced, beheaded, survived* ». Anne Boleyn, mère de la future Elizabeth I, est décapitée.

## Les enfants d'Henry
Après Henry, son fils Édouard VI règne peu de temps, puis sa fille **Mary I**, catholique, qui fait brûler des centaines de protestants : on la surnomme **Bloody Mary**. En 1558, sa demi-sœur **Elizabeth I** monte sur le trône.

## Elizabeth I, la « reine vierge »
Elizabeth règne 45 ans (1558-1603). Elle ne se marie jamais et affirme être mariée à son royaume : on l'appelle **the Virgin Queen**. Elle impose une Église anglicane modérée. Son règne est menacé par les complots catholiques autour de sa cousine **Mary, Queen of Scots**, qu'elle finit par faire exécuter en 1587. En 1588, le roi d'Espagne Philippe II envoie l'**Invincible Armada** envahir l'Angleterre ; la flotte anglaise, aidée par les tempêtes, la met en déroute. Dans un discours célèbre, Elizabeth affirme avoir le corps d'une faible femme mais le cœur et l'estomac d'un roi.

## L'âge d'or élisabéthain
C'est une époque de rayonnement : Shakespeare écrit ses pièces, les théâtres se multiplient à Londres, les marins anglais comme **Francis Drake** font le tour du monde et pillent les navires espagnols, les premières tentatives de colonies en Amérique ont lieu (la Virginie est nommée en l'honneur de la reine vierge). À sa mort en 1603, sans enfant, la couronne passe au roi d'Écosse Jacques VI : c'est la fin des Tudors.
""", """
a queen = une reine
a wife = une épouse
a divorce = un divorce
to behead = décapiter
a church = une église
a fleet = une flotte
a sailor = un marin
a storm = une tempête
""", [
 ("Comment Henry VII met-il fin à la guerre des Deux-Roses ?", ["En épousant une princesse York", "En gagnant une course", "En quittant l'Angleterre"], ""),
 ("Pourquoi Henry VIII rompt-il avec Rome ?", ["Le pape refuse d'annuler son mariage", "Il veut devenir pape", "Il déteste l'Italie"], ""),
 ("Pourquoi surnomme-t-on Mary I « Bloody Mary » ?", ["Elle a fait brûler des centaines de protestants", "Elle aimait les cocktails", "Elle a gagné une guerre"], ""),
 ("Pourquoi appelle-t-on Elizabeth I « la reine vierge » ?", ["Elle ne s'est jamais mariée", "Elle n'a jamais régné", "Elle était très jeune"], ""),
 ("Qu'arrive-t-il à l'Invincible Armada en 1588 ?", ["Elle est mise en déroute par la flotte anglaise et les tempêtes", "Elle conquiert Londres", "Elle se perd en Amérique"], ""),
 ("Qui succède à Elizabeth I ?", ["Le roi d'Écosse Jacques VI", "Henry IX", "Bloody Mary"], ""),
], [("Richard III", "dernier roi de la famille York, mort au combat"), ("Catherine d'Aragon", "princesse espagnole, première épouse d'Henry VIII"), ("Philippe II", "roi catholique d'Espagne, ennemi d'Elizabeth"), ("Francis Drake", "marin et corsaire anglais, deuxième navigateur à faire le tour du monde")])
D = "td"
culture(F, "Culture : The Tudors", 'The <span>Tudors</span>',
  "Culture · Henry VIII, Elizabeth I et l'âge d'or élisabéthain", ("#fecaca", "#991b1b"),
  reperes("Les Tudors règnent sur l'Angleterre de 1485 à 1603. C'est l'époque de la rupture avec Rome, d'Henry VIII et de ses six épouses, puis du grand règne d'Elizabeth I.",
    [("1485", "Henry VII, premier roi Tudor"), ("1509 – 1547", "règne d'Henry VIII"), ("1534", "naissance de l'Église d'Angleterre"),
     ("1558 – 1603", "règne d'Elizabeth I"), ("1588", "défaite de l'Invincible Armada espagnole"), ("1603", "mort d'Elizabeth : fin des Tudors")],
    "a dynasty, a queen, a wife, to behead, a church, a fleet, a plot, a golden age"),
  {D: doc("Kings, queens and six wives", [
    "The Tudor family ruled England from 1485 to 1603. The most famous Tudor king is Henry VIII. He married six times, because he desperately wanted a son.",
    "When the Pope refused to cancel his first marriage, Henry broke with Rome and created the Church of England in 1534. Two of his wives were beheaded, including Anne Boleyn, the mother of Elizabeth.",
    "After Henry's death, his daughter Mary I, a Catholic, burned hundreds of Protestants. People called her \"Bloody Mary\".",
    "In 1558, Elizabeth I became queen. She never married, so she was called \"the Virgin Queen\". In 1588, the King of Spain sent a huge fleet, the Spanish Armada, to invade England, but the English navy and terrible storms destroyed it.",
    "Elizabeth's reign was a golden age: Shakespeare wrote his plays, and sailors like Francis Drake travelled around the world. She died in 1603 without children, and the crown went to the King of Scotland."])},
  [TF(D, "The Tudors ruled England for more than a century.", True, "1485-1603."),
   TF(D, "Henry VIII married three times.", False, "Six fois."),
   TF(D, "Henry VIII created the Church of England.", True, "« created the Church of England in 1534 »."),
   TF(D, "Mary I was a Protestant.", False, "« a Catholic »."),
   TF(D, "Elizabeth I had many children.", False, "« died … without children »."),
   TF(D, "Storms helped to destroy the Spanish Armada.", True, "« terrible storms destroyed it »." )],
  [Q(D, "Why did Henry VIII marry six times?", ["He wanted a son.", "He liked parties.", "The Pope asked him."]),
   Q(D, "Who was Anne Boleyn?", ["Henry's wife and Elizabeth's mother.", "A Spanish queen.", "A sailor."]),
   Q(D, "Why was Elizabeth called \"the Virgin Queen\"?", ["She never married.", "She was very young.", "She lived in a church."]),
   Q(D, "Why was her reign a golden age?", ["Shakespeare wrote and sailors explored the world.", "There was no war.", "Everybody was rich."])],
  [DT(D, "Quand l'Armada est-elle vaincue ?", ["1588", "1534", "1603", "1485"]),
   DT(D, "Qui est la mère d'Elizabeth I ?", ["Anne Boleyn", "Catherine d'Aragon", "Mary Stuart", "Jane Seymour"]),
   DT(D, "Quel pays envoie l'Armada ?", ["L'Espagne", "La France", "Les Pays-Bas", "Le Portugal"]),
   DT(D, "Comment surnomme-t-on Mary I ?", ["Bloody Mary", "The Virgin Queen", "Good Queen Mary", "Mary the Great"])],
  [W(D, "Trouve le mot qui veut dire « décapitées ».", "beheaded"), W(D, "Trouve le mot qui veut dire « flotte ».", "fleet"),
   W(D, "Trouve le mot qui veut dire « marine (de guerre) ».", "navy"), W(D, "Trouve le mot qui veut dire « marins ».", "sailors")])

# ═════════ VICTORIANS ═════════
F = "cu_victoriens.html"
DZ(F, """
## Une reine, une époque
**Queen Victoria** monte sur le trône en 1837, à 18 ans, et règne 63 ans, jusqu'en 1901. Son mariage avec le prince allemand **Albert** donne neuf enfants, qui épousent des familles royales de toute l'Europe : on la surnomme « la grand-mère de l'Europe ». À la mort d'Albert en 1861, elle porte le deuil jusqu'à la fin de sa vie. L'époque victorienne est celle de la puissance britannique : révolution industrielle, Empire immense, inventions.

## Le progrès
Les Victoriens croient au progrès. Le chemin de fer couvre le pays ; le télégraphe relie Londres au monde ; la photographie, le timbre-poste (le **Penny Black**, 1840, premier timbre du monde), le téléphone (inventé par Graham Bell, un Écossais émigré) apparaissent. Charles **Darwin** publie *On the Origin of Species* (1859) sur l'évolution, qui choque les croyants. Londres construit le premier métro (1863) et un immense réseau d'égouts après la « Grande Puanteur » de 1858, quand la Tamise empeste au point d'arrêter le Parlement.

## La morale victorienne
La société est très stricte : respectabilité, religion, travail, pudeur. Les femmes de la bourgeoisie doivent être des épouses et des mères parfaites, sans droit de vote. Les enfants doivent être « vus et non entendus ». Mais derrière cette façade, la misère, la prostitution et l'alcoolisme sont partout dans les quartiers pauvres.

## La misère des villes
Les pauvres s'entassent dans des **slums**. Les **workhouses** accueillent les indigents dans des conditions volontairement dures, pour décourager la « paresse » : familles séparées, travail épuisant, nourriture maigre. Charles Dickens, qui a travaillé enfant dans une usine, les dénonce dans *Oliver Twist*. Les enfants des rues vendent des allumettes, ramonent les cheminées ou volent.

## Jack l'Éventreur et la face sombre de Londres
En 1888, dans le quartier pauvre de **Whitechapel**, dans l'East End de Londres, au moins cinq femmes sont assassinées par un tueur jamais identifié, surnommé **Jack the Ripper**. La presse populaire s'empare de l'affaire, qui révèle la misère de ces quartiers. Le mystère fascine encore aujourd'hui. C'est aussi l'époque où l'écrivain **Arthur Conan Doyle** crée **Sherlock Holmes** (1887), le détective qui résout les énigmes de ce Londres de brouillard et de becs de gaz.

## L'héritage
Les Victoriens ont laissé de nombreuses traditions : le sapin de Noël popularisé par Albert, les cartes de Noël, les grands musées, les parcs publics, le football organisé. Mais aussi l'image d'une société hypocrite, fière de sa puissance et dure envers ses pauvres.
""", """
a queen = une reine
an invention = une invention
a stamp = un timbre
the poor = les pauvres
a detective = un détective
a murder = un meurtre
a chimney = une cheminée
a Christmas tree = un sapin de Noël
""", [
 ("Combien de temps Victoria a-t-elle régné ?", ["63 ans", "10 ans", "100 ans"], ""),
 ("Pourquoi la surnomme-t-on « la grand-mère de l'Europe » ?", ["Ses enfants ont épousé des familles royales de toute l'Europe", "Elle était très âgée", "Elle a conquis l'Europe"], ""),
 ("Qu'est-ce que le Penny Black ?", ["Le premier timbre-poste du monde", "Une pièce de monnaie", "Un journal"], ""),
 ("Qu'est-ce qu'une workhouse ?", ["Un hospice très dur où l'on enfermait les pauvres", "Une usine moderne", "Une école"], ""),
 ("Qui est Jack the Ripper ?", ["Un tueur jamais identifié qui a tué des femmes à Whitechapel", "Un policier célèbre", "Un roi"], ""),
 ("Quel détective naît à cette époque ?", ["Sherlock Holmes", "Hercule Poirot", "Batman"], ""),
], [("Albert", "prince allemand, mari de Victoria"), ("Graham Bell", "inventeur écossais installé en Amérique"), ("Charles **Darwin**", "naturaliste anglais"), ("Arthur Conan Doyle", "médecin et écrivain écossais")])
D = "vic"
culture(F, "Culture : Victorian Britain", 'Victorian <span>Britain</span>',
  "Culture · progrès, morale stricte et misère des villes", ("#d8b4fe", "#4c1d95"),
  reperes("L'époque victorienne (1837-1901) est celle de la toute-puissance britannique : industrie, Empire, inventions… mais aussi d'une morale stricte et d'une grande misère.",
    [("1837", "Victoria devient reine à 18 ans"), ("1840", "le Penny Black, premier timbre du monde"), ("1851", "Grande Exposition au Crystal Palace"),
     ("1859", "Darwin publie sa théorie de l'évolution"), ("1887", "première aventure de Sherlock Holmes"), ("1888", "meurtres de Jack l'Éventreur à Whitechapel"), ("1901", "mort de Victoria")],
    "progress, an invention, the poor, a workhouse, a slum, respectability, a detective, fog"),
  {D: doc("Light and shadows", [
    "Queen Victoria reigned from 1837 to 1901, for 63 years. During this period, Britain was the richest and most powerful country in the world.",
    "The Victorians loved progress. They built railways, the first underground, and invented the first postage stamp. The scientist Charles Darwin explained the theory of evolution.",
    "Victorian society was very strict. People had to be respectable, religious and hard-working. Children had to be \"seen and not heard\".",
    "But many people were very poor. They lived in dirty slums, and some had to go to workhouses, where life was very hard. The writer Charles Dickens described their misery.",
    "In 1888, a mysterious killer, Jack the Ripper, murdered several women in Whitechapel, a poor area of London. He was never caught. At the same time, the writer Arthur Conan Doyle created a famous detective: Sherlock Holmes."])},
  [TF(D, "Victoria reigned for 63 years.", True, "« for 63 years »."),
   TF(D, "Britain was a poor country during her reign.", False, "« the richest and most powerful country »."),
   TF(D, "The Victorians invented the first postage stamp.", True, "« the first postage stamp »."),
   TF(D, "Victorian children were encouraged to talk a lot.", False, "« seen and not heard »."),
   TF(D, "Jack the Ripper was caught by the police.", False, "« He was never caught »."),
   TF(D, "Sherlock Holmes was created by Charles Dickens.", False, "Par Arthur Conan Doyle." )],
  [Q(D, "What did Charles Darwin explain?", ["The theory of evolution.", "How to build trains.", "The rules of football."]),
   Q(D, "What were workhouses?", ["Places where the poor had a very hard life.", "Modern factories.", "Rich houses."]),
   Q(D, "Where did Jack the Ripper kill?", ["In Whitechapel, a poor area of London.", "In Manchester.", "In Buckingham Palace."]),
   Q(D, "What was Victorian society like?", ["Very strict, religious and respectable.", "Very relaxed.", "Without rules."])],
  [DT(D, "Quel est le prénom du mari de Victoria ?", ["Albert", "George", "Edward", "William"]),
   DT(D, "Quand ont lieu les meurtres de Jack l'Éventreur ?", ["1888", "1837", "1901", "1859"]),
   DT(D, "Qui a écrit Oliver Twist ?", ["Charles Dickens", "Arthur Conan Doyle", "Charles Darwin", "Jane Austen"]),
   DT(D, "Comment s'appelle le premier timbre ?", ["Le Penny Black", "Le Red Penny", "Le Victoria Stamp", "Le Royal Mail"])],
  [W(D, "Trouve le mot qui veut dire « timbre-poste » (2 mots).", ["postage stamp", "a postage stamp"]), W(D, "Trouve le mot qui veut dire « respectable ».", "respectable"),
   W(D, "Trouve le mot qui veut dire « tueur ».", ["killer", "a killer"]), W(D, "Trouve le mot qui veut dire « attrapé ».", "caught")])

# ═════════ WW1 ═════════
F = "cu_ww1.html"
DZ(F, """
## Le Royaume-Uni entre en guerre
En août 1914, l'Allemagne envahit la Belgique pour attaquer la France. Le Royaume-Uni, garant de la neutralité belge, déclare la guerre. Au début, l'armée britannique est petite et composée de volontaires. Une immense campagne de recrutement est lancée : l'affiche du ministre **Lord Kitchener** pointant du doigt (« *Your country needs you* ») devient célèbre. Des amis, des collègues, des équipes de football s'engagent ensemble dans les **Pals battalions**. À partir de 1916, le service militaire devient obligatoire (**conscription**).

## La vie dans les tranchées
Sur le front occidental, en France et en Belgique, la guerre de mouvement s'arrête vite : les soldats s'enterrent dans des **trenches**. Ils vivent dans la boue, avec les rats, les poux, le froid, sous les obus. Entre les tranchées ennemies s'étend le **no man's land**. Les soldats souffrent du « pied de tranchée » et d'un traumatisme nouveau, le **shell shock**. Les armes modernes (mitrailleuses, artillerie, gaz) rendent les attaques terriblement meurtrières.

## La Somme et Passchendaele
Le **1er juillet 1916**, premier jour de la bataille de la **Somme**, l'armée britannique perd près de 20 000 morts et 40 000 blessés : le jour le plus sanglant de son histoire. La bataille dure cinq mois pour quelques kilomètres. En 1917, à **Passchendaele**, en Belgique, les soldats se noient littéralement dans la boue. Des troupes de tout l'Empire combattent : Canadiens, Australiens, Néo-Zélandais (les **ANZAC** à Gallipoli), Indiens, Africains.

## La trêve de Noël
À Noël 1914, sur certaines parties du front, des soldats britanniques et allemands sortent spontanément des tranchées, échangent des cigarettes, chantent et jouent parfois au football dans le no man's land : c'est la **Christmas truce**. Le commandement interdit ensuite ce genre de fraternisation.

## Les poètes de guerre
Des soldats-poètes comme **Wilfred Owen** et **Siegfried Sassoon** décrivent l'horreur des tranchées et dénoncent le mensonge de la gloire militaire. Owen est tué une semaine avant l'armistice.

## Se souvenir : le coquelicot
La guerre s'arrête le **11 novembre 1918** à 11 heures. Le Royaume-Uni et l'Empire ont perdu près d'un million de soldats. Le **poppy** (coquelicot), qui poussait sur les champs de bataille de Flandre, devient le symbole du souvenir, inspiré du poème *In Flanders Fields* écrit en 1915 par le médecin canadien John McCrae. Chaque année, autour du 11 novembre, les Britanniques portent un coquelicot en papier ; le **Remembrance Sunday**, le roi dépose une gerbe au **Cenotaph** de Londres, et tout le pays observe **two minutes' silence**.
""", """
a soldier = un soldat
a trench = une tranchée
mud = la boue
a poppy = un coquelicot
a battle = une bataille
a poet = un poète
silence = le silence
peace = la paix
""", [
 ("Pourquoi le Royaume-Uni entre-t-il en guerre en 1914 ?", ["L'Allemagne envahit la Belgique", "La France attaque Londres", "La Russie l'y oblige"], ""),
 ("Que montre la célèbre affiche de Lord Kitchener ?", ["Un homme qui pointe du doigt : « Your country needs you »", "Un coquelicot", "Une tranchée"], ""),
 ("Que vivent les soldats dans les tranchées ?", ["La boue, les rats, le froid et les obus", "Le confort et le repos", "Les vacances"], ""),
 ("Que se passe-t-il le 1er juillet 1916 ?", ["Le jour le plus sanglant de l'armée britannique, sur la Somme", "La fin de la guerre", "La trêve de Noël"], ""),
 ("Qu'est-ce que la trêve de Noël 1914 ?", ["Des soldats ennemis fraternisent spontanément", "Un traité de paix", "Une grande bataille"], ""),
 ("Pourquoi le coquelicot est-il le symbole du souvenir ?", ["Il poussait sur les champs de bataille de Flandre", "C'est la fleur du roi", "Il est rouge comme le drapeau"], ""),
], [("**Lord Kitchener**", "ministre de la Guerre britannique"), ("Gallipoli", "presqu'île turque, lieu d'une offensive alliée ratée en 1915"), ("**Wilfred Owen**", "poète et officier anglais"), ("**Cenotaph**", "monument aux morts de Londres")])
D = "ww1"
culture(F, "Culture : The First World War", 'The Great <span>War</span>',
  "Culture · les tranchées, la Somme et les coquelicots", ("#fca5a5", "#7f1d1d"),
  reperes("De 1914 à 1918, la Grande Guerre fait près d'un million de morts dans l'armée britannique et de l'Empire. Chaque année, les Britanniques s'en souviennent en portant un coquelicot.",
    [("4 août 1914", "le Royaume-Uni déclare la guerre à l'Allemagne"), ("Noël 1914", "trêve spontanée sur le front"), ("1916", "conscription obligatoire"),
     ("1er juillet 1916", "premier jour de la Somme : près de 20 000 morts britanniques"), ("1917", "Passchendaele, la bataille de la boue"), ("11 nov. 1918, 11 h", "armistice")],
    "a trench, mud, a shell, the front, no man's land, a volunteer, a poppy, remembrance"),
  {D: doc("Lest we forget", [
    "In August 1914, Germany invaded Belgium and Britain declared war. Hundreds of thousands of young men volunteered to fight. A famous poster showed Lord Kitchener pointing his finger: \"Your country needs you\".",
    "On the Western Front, in France and Belgium, soldiers lived in trenches. They suffered from mud, rats, cold and constant shelling. The land between the enemy trenches was called \"no man's land\".",
    "At Christmas 1914, on some parts of the front, British and German soldiers stopped fighting. They sang carols, exchanged gifts and even played football together.",
    "On 1 July 1916, the first day of the Battle of the Somme, almost 20,000 British soldiers were killed. It is the bloodiest day in the history of the British army.",
    "The war ended on 11 November 1918 at 11 o'clock. Every year, British people wear a red poppy to remember the soldiers who died. The poppy grew on the battlefields of Flanders. On Remembrance Sunday, the whole country observes two minutes' silence."])},
  [TF(D, "Britain declared war after Germany invaded Belgium.", True, "« Germany invaded Belgium and Britain declared war »."),
   TF(D, "At first, the soldiers were all forced to fight.", False, "Ils étaient d'abord volontaires."),
   TF(D, "No man's land was the land between the trenches.", True, "« The land between the enemy trenches »."),
   TF(D, "British and German soldiers played football at Christmas 1914.", True, "« even played football together »."),
   TF(D, "The first day of the Somme was a British victory with few deaths.", False, "« almost 20,000 British soldiers were killed »."),
   TF(D, "The war ended on 11 November 1918.", True, "« at 11 o'clock »." )],
  [Q(D, "What did Lord Kitchener's poster say?", ["Your country needs you.", "Keep calm and carry on.", "Make love, not war."]),
   Q(D, "What did soldiers suffer from in the trenches?", ["Mud, rats, cold and shelling.", "Heat and sun.", "Boredom only."]),
   Q(D, "Why do British people wear a poppy?", ["To remember the soldiers who died.", "Because it is spring.", "To celebrate the King."]),
   Q(D, "What happens on Remembrance Sunday?", ["The country observes two minutes' silence.", "People play football.", "There is a big party."])],
  [DT(D, "Où pousse le coquelicot du souvenir ?", ["En Flandre", "En Écosse", "À Londres", "Aux États-Unis"]),
   DT(D, "Quelle bataille de 1917 est célèbre pour sa boue ?", ["Passchendaele", "Hastings", "Waterloo", "Dunkerque"]),
   DT(D, "À quelle heure l'armistice entre-t-il en vigueur ?", ["11 heures", "Midi", "Minuit", "8 heures"]),
   DT(D, "Quel poète-soldat meurt une semaine avant l'armistice ?", ["Wilfred Owen", "Shakespeare", "Robert Burns", "Lord Byron"])],
  [W(D, "Trouve le mot qui veut dire « tranchées ».", "trenches"), W(D, "Trouve le mot qui veut dire « boue ».", "mud"),
   W(D, "Trouve le mot qui veut dire « coquelicot ».", ["poppy", "a red poppy", "red poppy"]), W(D, "Trouve le mot qui veut dire « champs de bataille ».", "battlefields")])

# ═════════ WELFARE STATE ═════════
F = "cu_welfare_state.html"
DZ(F, """
## Gagner la guerre… puis la paix
En 1942, en pleine guerre, l'économiste **William Beveridge** publie un rapport qui devient un best-seller. Il veut combattre cinq « géants » : la misère (**want**), la maladie (**disease**), l'ignorance, l'insalubrité des logements (**squalor**) et l'oisiveté, c'est-à-dire le chômage. Il propose une protection sociale « du berceau à la tombe » (**from the cradle to the grave**). Les Britanniques, qui ont tout sacrifié pendant la guerre, attendent un monde plus juste.

## La surprise de 1945
En juillet 1945, quelques semaines après la victoire en Europe, les élections générales créent la surprise : **Winston Churchill**, héros de la guerre, est battu à plate couture. Le Parti travailliste de **Clement Attlee** obtient une large majorité. Les électeurs ont voté pour l'avenir : des logements, des emplois, la santé.

## La construction de l'État-providence
Le gouvernement Attlee construit le **welfare state** :
- le **National Health Service** (1948), imaginé par le ministre **Aneurin Bevan**, fils de mineur gallois : soins gratuits pour tous, financés par l'impôt ;
- la **National Insurance** : allocations chômage, maladie, retraite, maternité ;
- des allocations familiales ;
- la construction massive de logements sociaux (**council houses**) pour remplacer les maisons détruites et les taudis ;
- la scolarité gratuite et obligatoire jusqu'à 15 ans (loi de 1944).
Le gouvernement nationalise aussi les grandes industries : les mines de charbon, les chemins de fer, l'électricité, la sidérurgie, la Banque d'Angleterre.

## Le consensus d'après-guerre
Pendant près de trente ans, conservateurs et travaillistes acceptent globalement ce modèle : c'est le **post-war consensus**. Le niveau de vie augmente, le chômage est bas. En 1957, le Premier ministre conservateur Harold Macmillan peut dire aux Britanniques qu'ils n'ont « jamais été aussi bien lotis ».

## Remises en cause
Dans les années 1970, la crise économique et l'inflation mettent fin au consensus. **Margaret Thatcher**, à partir de 1979, privatise une grande partie des entreprises nationalisées et réduit le rôle de l'État, mais ne touche pas au cœur du NHS, trop populaire. Aujourd'hui, le débat continue : faut-il plus d'État ou plus de marché ? Le NHS, lui, reste l'institution dont les Britanniques sont le plus fiers.
""", """
health = la santé
a hospital = un hôpital
a house = une maison
a job = un emploi
free = gratuit
a tax = un impôt
an election = une élection
poverty = la pauvreté
""", [
 ("Que propose le rapport Beveridge en 1942 ?", ["Une protection sociale « du berceau à la tombe »", "La fin des hôpitaux", "Une nouvelle guerre"], ""),
 ("Que se passe-t-il aux élections de 1945 ?", ["Churchill est battu par le travailliste Clement Attlee", "Churchill gagne largement", "Il n'y a pas d'élection"], ""),
 ("Quand le NHS est-il créé ?", ["En 1948", "En 1914", "En 1979"], ""),
 ("Qu'est-ce qu'une council house ?", ["Un logement social", "Un palais", "Une mairie"], ""),
 ("Qu'est-ce que le « post-war consensus » ?", ["L'accord des grands partis sur l'État-providence", "Un traité de paix", "Une loi sur la guerre"], ""),
 ("Que fait Margaret Thatcher à partir de 1979 ?", ["Elle privatise beaucoup d'entreprises nationalisées", "Elle crée le NHS", "Elle augmente le rôle de l'État"], ""),
], [("**William Beveridge**", "économiste libéral"), ("**Clement Attlee**", "chef du Parti travailliste, Premier ministre de 1945 à 1951"), ("Harold Macmillan", "Premier ministre conservateur de 1957 à 1963")])
D = "ws"
culture(F, "Culture : 1945 and the welfare state", '1945 &amp; the <span>welfare state</span>',
  "Culture · Attlee, le NHS et la protection sociale", ("#bbf7d0", "#166534"),
  reperes("Après la Seconde Guerre mondiale, le gouvernement travailliste de Clement Attlee crée l'<b>État-providence</b> (welfare state) : santé gratuite, allocations, logements sociaux.",
    [("1942", "rapport Beveridge : combattre les « cinq géants »"), ("juillet 1945", "victoire travailliste : Attlee remplace Churchill"), ("1946 – 1951", "nationalisations : mines, chemins de fer, électricité"),
     ("5 juillet 1948", "naissance du NHS"), ("1945 – années 1970", "le « consensus d'après-guerre »")],
    "the welfare state, health care, a benefit, a council house, to nationalise, a pension, unemployment"),
  {D: doc("From the cradle to the grave", [
    "During the Second World War, the British people suffered a lot. They wanted a better and fairer country after the war.",
    "In 1942, William Beveridge wrote a report about five \"giants\" to defeat: poverty, disease, ignorance, bad housing and unemployment. He wanted to protect people \"from the cradle to the grave\".",
    "In July 1945, there was a surprise: Winston Churchill, the war hero, lost the election. The Labour Party of Clement Attlee won a big majority.",
    "Attlee's government created the welfare state. In 1948, the National Health Service gave free health care to everybody. People also received benefits when they were ill, old or unemployed, and the government built thousands of council houses.",
    "The government also nationalised big industries, like coal mines and railways. Today, the NHS is still the institution British people are most proud of."])},
  [TF(D, "The British people wanted a fairer country after the war.", True, "« a better and fairer country »."),
   TF(D, "Beveridge wrote about five giants.", True, "« five \"giants\" »."),
   TF(D, "Churchill won the 1945 election.", False, "« Winston Churchill … lost the election »."),
   TF(D, "The NHS was created in 1948.", True, "« In 1948 »."),
   TF(D, "Health care in the NHS was expensive.", False, "« free health care »."),
   TF(D, "The government nationalised coal mines.", True, "« nationalised big industries, like coal mines »." )],
  [Q(D, "What does \"from the cradle to the grave\" mean?", ["From birth to death.", "From school to work.", "From London to Edinburgh."]),
   Q(D, "Which party won in 1945?", ["The Labour Party.", "The Conservative Party.", "The Liberal Party."]),
   Q(D, "What are council houses?", ["Houses built by the government.", "Palaces.", "Hospitals."]),
   Q(D, "What did people receive when they were ill or unemployed?", ["Benefits.", "Nothing.", "A house in the countryside."])],
  [DT(D, "Qui écrit le rapport de 1942 ?", ["William Beveridge", "Clement Attlee", "Winston Churchill", "Aneurin Bevan"]),
   DT(D, "Quel ministre a imaginé le NHS ?", ["Aneurin Bevan", "Margaret Thatcher", "Tony Blair", "Harold Macmillan"]),
   DT(D, "Quel Premier ministre crée l'État-providence ?", ["Clement Attlee", "Winston Churchill", "Margaret Thatcher", "Boris Johnson"]),
   DT(D, "Combien de « géants » à combattre ?", ["Cinq", "Trois", "Dix", "Un"])],
  [W(D, "Trouve le mot qui veut dire « berceau ».", ["cradle", "the cradle"]), W(D, "Trouve le mot qui veut dire « tombe ».", ["grave", "the grave"]),
   W(D, "Trouve le mot qui veut dire « allocations ».", "benefits"), W(D, "Trouve le mot qui veut dire « fiers ».", "proud")])

# ═════════ SWINGING SIXTIES ═════════
F = "cu_swinging_sixties.html"
DZ(F, """
## Une jeunesse qui veut s'amuser
Après les privations de la guerre et le rationnement (qui ne se termine qu'en 1954), les années 1960 marquent une explosion de liberté. La génération du **baby-boom** a de l'argent de poche, du temps libre et l'envie de rompre avec ses parents. Londres devient la capitale mondiale de la mode et de la musique : le magazine américain *Time* titre en 1966 sur « *London: The Swinging City* ».

## La musique
Les **Beatles**, venus de Liverpool, déclenchent la **Beatlemania** à partir de 1963 : des foules d'adolescentes hurlent à leurs concerts. Ils conquièrent ensuite l'Amérique. Les **Rolling Stones**, plus rebelles, les Who, les Kinks font de la **British Invasion** un phénomène mondial. Des radios pirates, émettant depuis des bateaux en mer comme Radio Caroline, diffusent la pop que la BBC passe trop peu.

## La mode
Sur **Carnaby Street** et King's Road, des boutiques vendent des vêtements colorés et bon marché. La créatrice **Mary Quant** popularise la **miniskirt**. Le mannequin **Twiggy**, silhouette très fine et grands yeux, devient une icône. Les **mods**, en costumes ajustés et scooters, s'opposent aux **rockers**, en blousons de cuir et motos. La **Mini**, petite voiture lancée en 1959, et le drapeau britannique imprimé partout deviennent des symboles du « cool » britannique.

## Une société qui change
Les lois évoluent vite à la fin des années 1960 : abolition de la peine de mort pour meurtre (1965), dépénalisation partielle de l'homosexualité et légalisation de l'avortement (1967), divorce facilité (1969). La pilule contraceptive se diffuse. On parle de **permissive society**. Pour certains, c'est une libération ; pour d'autres, un déclin moral.

## L'autre face
Le « Swinging London » concerne surtout une minorité de jeunes Londoniens aisés. Dans le reste du pays, beaucoup vivent encore modestement. Et la fin de la décennie est plus sombre : tensions sociales, début des Troubles en Irlande du Nord, crise économique qui approche. Mais l'image de Londres comme capitale du « cool » est restée : c'est l'époque de James Bond au cinéma, d'*Austin Powers* plus tard en parodie, et de la victoire de l'Angleterre à la Coupe du monde de football de 1966, à Wembley.
""", """
fashion = la mode
a skirt = une jupe
a band = un groupe
a car = une voiture
young people = les jeunes
freedom = la liberté
a shop = une boutique
a model = un mannequin
""", [
 ("Pourquoi les années 1960 sont-elles une explosion de liberté ?", ["Après les privations de la guerre, les jeunes ont de l'argent et du temps libre", "La guerre recommence", "Les jeunes travaillent plus"], ""),
 ("D'où viennent les Beatles ?", ["De Liverpool", "De Londres", "De New York"], ""),
 ("Qui popularise la minijupe ?", ["Mary Quant", "Twiggy", "La reine"], ""),
 ("Qu'est-ce qui oppose les mods et les rockers ?", ["Leur style : costumes et scooters contre cuir et motos", "Leur religion", "Leur ville"], ""),
 ("Qu'est-ce que la « permissive society » ?", ["Une société plus libre, avec des lois plus tolérantes", "Une société très stricte", "Une société sans lois"], ""),
 ("Que gagne l'Angleterre en 1966 ?", ["La Coupe du monde de football", "Les Jeux olympiques", "Une guerre"], ""),
], [("Radio Caroline", "radio pirate qui émettait depuis un bateau"), ("**Twiggy**", "mannequin anglaise née en 1949"), ("Wembley", "grand stade de Londres")])
D = "ss"
culture(F, "Culture : The Swinging Sixties", 'The Swinging <span>Sixties</span>',
  "Culture · Londres, capitale du « cool »", ("#f9a8d4", "#0ea5e9"),
  reperes("Dans les années 1960, Londres devient la capitale mondiale de la jeunesse, de la pop et de la mode.",
    [("1963", "début de la Beatlemania"), ("1964", "la « British Invasion » aux États-Unis"), ("1965", "Mary Quant popularise la minijupe"),
     ("1966", "le magazine Time parle de « Swinging London » ; l'Angleterre gagne la Coupe du monde"), ("1967", "lois plus libérales : homosexualité, avortement")],
    "fashion, a miniskirt, a band, a fan, a scooter, freedom, a teenager, cool"),
  {D: doc("London swings", [
    "In the 1960s, life changed for young people in Britain. After the hard years of the war, they had money, free time and new ideas.",
    "London became the world capital of music and fashion. The Beatles, a band from Liverpool, were so popular that fans screamed at their concerts: this was \"Beatlemania\".",
    "Young people bought colourful clothes in the shops of Carnaby Street. The designer Mary Quant made the miniskirt popular, and the model Twiggy became a fashion icon.",
    "Two groups of young people were rivals: the mods, with smart suits and scooters, and the rockers, with leather jackets and motorbikes.",
    "Society also changed: new laws gave people more freedom. And in 1966, England won the football World Cup at Wembley!"])},
  [TF(D, "After the war, young people had more money and free time.", True, "« they had money, free time »."),
   TF(D, "The Beatles came from London.", False, "« a band from Liverpool »."),
   TF(D, "Mary Quant made the miniskirt popular.", True, "« made the miniskirt popular »."),
   TF(D, "The mods rode motorbikes.", False, "Les mods avaient des scooters."),
   TF(D, "England won the World Cup in 1966.", True, "« at Wembley »."),
   TF(D, "Carnaby Street was famous for its banks.", False, "Pour ses boutiques de mode." )],
  [Q(D, "What was Beatlemania?", ["The huge popularity of the Beatles.", "A disease.", "A shop."]),
   Q(D, "Who was Twiggy?", ["A model and fashion icon.", "A singer.", "A football player."]),
   Q(D, "What did the rockers wear?", ["Leather jackets.", "Smart suits.", "Miniskirts."]),
   Q(D, "Which city was the capital of music and fashion?", ["London.", "Paris.", "New York."])],
  [DT(D, "Où l'Angleterre gagne-t-elle la Coupe du monde ?", ["À Wembley", "À Rio", "À Paris", "À Liverpool"]),
   DT(D, "Quelle rue est célèbre pour ses boutiques ?", ["Carnaby Street", "Downing Street", "Abbey Road", "Baker Street"]),
   DT(D, "Quel magazine parle de « Swinging London » ?", ["Time", "Vogue", "The Sun", "Le Monde"]),
   DT(D, "Quelle petite voiture est un symbole de l'époque ?", ["La Mini", "La Ford T", "La Coccinelle", "La 2CV"])],
  [W(D, "Trouve le mot qui veut dire « mode ».", "fashion"), W(D, "Trouve le mot qui veut dire « hurlaient ».", "screamed"),
   W(D, "Trouve le mot qui veut dire « vestes en cuir ».", ["leather jackets", "leather jacket"]), W(D, "Trouve le mot qui veut dire « coloré ».", "colourful")])
END()
