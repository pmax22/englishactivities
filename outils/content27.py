import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
exec(open(_EA_OUT+"/cuhelp.py", encoding="utf-8").read())

# ═════════ CLASSES ═════════
F = "cu_classes_uk.html"
DZ(F, """
## Une société de classes
Au Royaume-Uni, la notion de **social class** reste très présente dans les esprits. Traditionnellement, on distingue :
- l'**upper class** : l'aristocratie et les très grandes fortunes, souvent héritières de terres et de titres (ducs, comtes, lords) ;
- la **middle class** : professions libérales, cadres, enseignants, fonctionnaires ;
- la **working class** : ouvriers, employés, métiers manuels.
La classe ne dépend pas seulement de l'argent : elle se reconnaît à l'accent, au vocabulaire, à l'école fréquentée, aux loisirs, à ce qu'on mange et même à la façon dont on appelle le repas du soir (*dinner*, *supper* ou *tea*).

## L'école, clé de la reproduction sociale
Environ 7 % des élèves fréquentent des écoles privées très chères (paradoxalement appelées **public schools**, comme Eton ou Harrow). Pourtant, leurs anciens élèves occupent une grande partie des postes les plus prestigieux : juges, généraux, journalistes, ministres. Beaucoup passent ensuite par les universités d'**Oxford** et de **Cambridge**, surnommées **Oxbridge**. De nombreux Premiers ministres sont passés par Eton puis Oxford.

## Les accents, marqueurs sociaux
L'accent dit beaucoup de l'origine sociale et géographique. La **Received Pronunciation**, l'accent « chic » longtemps exigé à la BBC, s'oppose aux accents régionaux et populaires (Cockney, Scouse à Liverpool, Geordie à Newcastle, Brummie à Birmingham). Le dramaturge George Bernard Shaw disait qu'un Anglais ne peut ouvrir la bouche sans qu'un autre Anglais le méprise. Cette idée est au cœur de sa pièce *Pygmalion*, adaptée en comédie musicale *My Fair Lady*.

## La fracture Nord-Sud
Le **North-South divide** désigne l'écart entre le sud-est de l'Angleterre, autour de Londres, riche et dynamique (finance, services), et le nord (Manchester, Liverpool, Newcastle, Sheffield…), longtemps cœur industriel. La fermeture des mines, des chantiers navals et des usines dans les années 1980 a durement frappé le nord : chômage, pauvreté, villes en déclin. L'espérance de vie, les salaires et les prix de l'immobilier restent nettement plus élevés dans le sud. Les gouvernements successifs ont promis de rééquilibrer le pays (« **levelling up** »), avec des résultats discutés.

## Une société qui change
La société britannique est aujourd'hui plus mobile et plus diverse qu'autrefois, et beaucoup de gens se définissent autrement que par la classe. Mais les études montrent que l'origine sociale pèse encore fortement sur la réussite. L'humour britannique adore d'ailleurs se moquer de ces différences, de la série *Downton Abbey* aux sketchs sur les manières de la haute société.
""", """
the upper class = la classe supérieure
the working class = la classe ouvrière
a school = une école
a university = une université
an accent = un accent
the North = le Nord
rich = riche
poor = pauvre
""", [
 ("À quoi reconnaît-on la classe sociale au Royaume-Uni ?", ["À l'accent, à l'école, aux loisirs, au vocabulaire", "Uniquement au salaire", "À la couleur des yeux"], ""),
 ("Qu'est-ce qu'une « public school » britannique ?", ["Une école privée très chère", "Une école publique gratuite", "Une université"], ""),
 ("Que désigne « Oxbridge » ?", ["Les universités d'Oxford et de Cambridge", "Un pont de Londres", "Un parti politique"], ""),
 ("Qu'est-ce que la Received Pronunciation ?", ["L'accent « chic » de référence", "L'accent de Liverpool", "Une langue"], ""),
 ("Qu'est-ce que le « North-South divide » ?", ["L'écart de richesse entre le sud-est et le nord de l'Angleterre", "La frontière avec l'Écosse", "Un match de football"], ""),
 ("Pourquoi le nord a-t-il été durement frappé dans les années 1980 ?", ["La fermeture des mines, des chantiers et des usines", "Une inondation", "Une guerre"], ""),
], [("Eton ou Harrow", "deux des écoles privées les plus prestigieuses du pays"), ("George Bernard Shaw", "dramaturge irlandais, prix Nobel de littérature 1925"), ("*Downton Abbey*", "série sur une famille aristocratique et ses domestiques au début du 20e siècle")])
D = "cl"
culture(F, "Culture : Class and the North-South divide", 'Class &amp; the <span>North-South divide</span>',
  "Culture · une société encore marquée par les classes sociales", ("#e9d5ff", "#6b21a8"),
  reperes("Au Royaume-Uni, la classe sociale se lit dans l'accent, l'école, les loisirs. Et un fossé sépare le sud-est riche du nord industriel.",
    [("upper class", "aristocratie et grandes fortunes"), ("middle class", "professions intellectuelles, cadres"), ("working class", "ouvriers et employés"),
     ("7 %", "des élèves dans des écoles privées, mais une grande partie des élites"), ("années 1980", "désindustrialisation du nord")],
    "social class, an accent, a private school, a degree, wealth, poverty, a region, inequality"),
  {D: doc("Posh or not?", [
    "In Britain, people often talk about social class. Traditionally, there is the upper class, the middle class and the working class. Class is not only about money: it is also about your accent, your school and your hobbies.",
    "Only about 7% of British children go to private schools, called \"public schools\", like Eton. But many judges, journalists and politicians went to these schools, and then to Oxford or Cambridge.",
    "Accents are very important. Some people speak with a \"posh\" accent, called Received Pronunciation. Others have strong regional accents, like Scouse in Liverpool or Geordie in Newcastle.",
    "There is also a big difference between the North and the South of England. The South-East, around London, is rich. The North was the heart of industry, but many mines and factories closed in the 1980s, and some towns became poor.",
    "Today, British society is more mixed than before, but studies show that your social background still has an influence on your success."])},
  [TF(D, "Class is only about money in Britain.", False, "« not only about money »."),
   TF(D, "Most British children go to private schools.", False, "Seulement environ 7 %."),
   TF(D, "Eton is a private school.", True, "« private schools, called \"public schools\", like Eton »."),
   TF(D, "Geordie is the accent of Newcastle.", True, "« Geordie in Newcastle »."),
   TF(D, "The South-East of England is the poorest region.", False, "« The South-East, around London, is rich »."),
   TF(D, "Many factories closed in the North in the 1980s.", True, "« many mines and factories closed in the 1980s »." )],
  [Q(D, "What does \"posh\" mean?", ["Upper class, chic.", "Poor.", "Northern."]),
   Q(D, "Where do many judges and politicians study?", ["At private schools, then Oxford or Cambridge.", "Only abroad.", "At home."]),
   Q(D, "Why did some northern towns become poor?", ["Mines and factories closed.", "There was a flood.", "People moved to Scotland."]),
   Q(D, "What do studies show today?", ["Social background still influences success.", "Class has disappeared.", "Everybody is rich."])],
  [DT(D, "Quel est l'accent de Liverpool ?", ["Scouse", "Geordie", "Cockney", "Brummie"]),
   DT(D, "Que désigne « Oxbridge » ?", ["Oxford et Cambridge", "Un quartier de Londres", "Une école primaire", "Un journal"]),
   DT(D, "Quelle pièce de Shaw parle des accents ?", ["Pygmalion", "Hamlet", "Oliver Twist", "Macbeth"]),
   DT(D, "Quelle région est la plus riche ?", ["Le sud-est, autour de Londres", "Le nord-est", "Le pays de Galles", "L'Écosse"])],
  [W(D, "Trouve le mot qui veut dire « chic, de la haute » (familier).", "posh"), W(D, "Trouve le mot qui veut dire « juges ».", "judges"),
   W(D, "Trouve le mot qui veut dire « usines ».", "factories"), W(D, "Trouve le mot qui veut dire « origine sociale » (2 mots).", ["social background", "background"])])

# ═════════ HUMOUR ═════════
F = "cu_humour.html"
DZ(F, """
## Un humour qui fait partie de l'identité
Les Britanniques sont très fiers de leur **sense of humour**, et le considèrent comme un trait national. On en plaisante partout : au travail, dans les discours officiels, même aux enterrements. Ne pas comprendre une blague, ou prendre au sérieux une remarque ironique, peut créer des malentendus.

## Les ingrédients de l'humour britannique
- **Irony** et **sarcasm** : dire le contraire de ce qu'on pense, sur un ton neutre. *Lovely weather!* sous une pluie battante.
- **Understatement** : minimiser. Un Britannique qui vient de se casser la jambe peut dire *It's a bit painful*.
- **Self-deprecation** : se moquer de soi-même, de ses échecs, de son pays. C'est une façon d'éviter de paraître prétentieux.
- **Deadpan** : raconter quelque chose de drôle avec un visage totalement impassible.
- L'**absurd** : des situations sans queue ni tête, poussées à l'extrême.
- La **banter** : des moqueries amicales entre proches, qui montrent la complicité.

## Les grands noms
Les **Monty Python**, une troupe apparue à la télévision en 1969 (*Monty Python's Flying Circus*), ont révolutionné l'humour avec leurs sketchs absurdes et leurs films comme *Monty Python and the Holy Grail* (1975), parodie de la légende du roi Arthur. **Mr Bean**, créé par Rowan Atkinson en 1990, fait rire le monde entier presque sans paroles. Des séries comme *Fawlty Towers*, *Blackadder* ou *The Office* (créée par Ricky Gervais, adaptée ensuite aux États-Unis et en France) sont devenues des classiques.

## Humour britannique contre humour américain
On dit souvent que l'humour américain est plus direct, optimiste et explicite, tandis que l'humour britannique est plus sec, plus sombre et moqueur, avec des personnages ratés et malheureux. C'est bien sûr une généralisation, mais la comparaison des deux versions de *The Office* l'illustre bien : le héros britannique est pathétique, l'américain finit par être attachant.

## Un outil social
L'humour sert à briser la glace, à désamorcer les tensions, à critiquer les puissants et à supporter les difficultés : pendant le Blitz, les Londoniens plaisantaient sous les bombes. Pour un étranger, comprendre l'humour britannique est une étape importante pour vraiment comprendre la culture du pays.
""", """
a joke = une blague
funny = drôle
to laugh = rire
a smile = un sourire
irony = l'ironie
a sketch = un sketch
serious = sérieux
silly = idiot, ridicule
""", [
 ("Que signifie « understatement » ?", ["Minimiser ce qu'on dit", "Exagérer", "Crier"], "Ex. : « It's a bit painful » après s'être cassé la jambe."),
 ("Qu'est-ce que la « self-deprecation » ?", ["Se moquer de soi-même", "Se vanter", "Se fâcher"], ""),
 ("Que fait un humoriste « deadpan » ?", ["Il raconte une chose drôle avec un visage impassible", "Il rit très fort", "Il pleure"], ""),
 ("Qui sont les Monty Python ?", ["Une troupe d'humoristes célèbre pour l'absurde", "Un groupe de rock", "Des serpents"], ""),
 ("Qui a créé Mr Bean ?", ["Rowan Atkinson", "Ricky Gervais", "Charlie Chaplin"], ""),
 ("À quoi sert l'humour dans la société britannique ?", ["Briser la glace, désamorcer les tensions, critiquer les puissants", "Uniquement à vendre des produits", "À rien"], ""),
], [("Rowan Atkinson", "acteur anglais"), ("Ricky Gervais", "humoriste et acteur anglais")])
D = "hu"
culture(F, "Culture : British humour", 'British <span>humour</span>',
  "Culture · ironie, autodérision et absurde", ("#fde68a", "#ca8a04"),
  reperes("L'humour britannique repose sur l'ironie, l'<b>understatement</b> (l'art de minimiser), l'autodérision et l'absurde.",
    [("1969", "Monty Python's Flying Circus à la télévision"), ("1975", "Monty Python and the Holy Grail"), ("1990", "première de Mr Bean"), ("2001", "The Office, de Ricky Gervais")],
    "a joke, irony, sarcasm, understatement, self-deprecation, deadpan, absurd, banter"),
  {D: doc("Are you joking?", [
    "British people are very proud of their sense of humour. They joke all the time, even in serious situations.",
    "British humour is often ironic: people say the opposite of what they think. For example, when it is raining heavily, someone may say: \"Lovely weather, isn't it?\"",
    "Understatement is also typical. A British person with a broken leg might say: \"It's a bit painful.\" British people also like to laugh at themselves: this is called self-deprecation.",
    "The Monty Python, a group of comedians, became famous in 1969 for their absurd sketches. Later, Rowan Atkinson created Mr Bean, a funny character who hardly speaks.",
    "Humour helps British people to break the ice, to avoid conflicts and to face difficult times. To understand the British, you must understand their jokes!"])},
  [TF(D, "British people rarely joke.", False, "« They joke all the time »."),
   TF(D, "Irony means saying the opposite of what you think.", True, "« people say the opposite of what they think »."),
   TF(D, "\"It's a bit painful\" about a broken leg is an example of understatement.", True, "C'est minimiser."),
   TF(D, "Self-deprecation means laughing at other people.", False, "C'est rire de soi-même."),
   TF(D, "The Monty Python became famous in 1969.", True, "« in 1969 »."),
   TF(D, "Mr Bean talks a lot.", False, "« hardly speaks »." )],
  [Q(D, "What does \"Lovely weather, isn't it?\" mean when it rains?", ["It's ironic: the weather is terrible.", "The person loves rain.", "It will be sunny soon."]),
   Q(D, "What kind of sketches made the Monty Python famous?", ["Absurd sketches.", "Romantic sketches.", "Political speeches."]),
   Q(D, "Who created Mr Bean?", ["Rowan Atkinson.", "The Monty Python.", "The Queen."]),
   Q(D, "Why is humour useful for the British?", ["To break the ice and avoid conflicts.", "To win elections.", "To learn French."])],
  [DT(D, "Quelle série de Ricky Gervais a été adaptée en France ?", ["The Office", "Mr Bean", "Blackadder", "Fawlty Towers"]),
   DT(D, "Quel film des Monty Python parodie le roi Arthur ?", ["Monty Python and the Holy Grail", "Life of Brian", "Mr Bean's Holiday", "Robin Hood"]),
   DT(D, "Comment appelle-t-on les moqueries amicales entre amis ?", ["Banter", "Deadpan", "Understatement", "Sarcasm"]),
   DT(D, "En quelle année Mr Bean apparaît-il ?", ["1990", "1969", "2001", "1975"])],
  [W(D, "Trouve le mot qui veut dire « humoristes ».", "comedians"), W(D, "Trouve le mot qui veut dire « absurde ».", "absurd"),
   W(D, "Trouve l'expression qui veut dire « briser la glace ».", ["break the ice", "to break the ice"]), W(D, "Trouve le mot qui veut dire « blagues ».", "jokes")])

# ═════════ SPORT UK ═════════
F = "cu_sport_uk.html"
DZ(F, """
## Le pays qui a inventé les sports modernes
Au 19e siècle, les Britanniques codifient de nombreux sports pratiqués aujourd'hui dans le monde entier : le football (règles fixées en 1863 par la **Football Association**), le rugby (né, selon la légende, en 1823 à l'école de Rugby, quand un élève prit le ballon à la main), le tennis moderne, le golf (en Écosse), la boxe, le badminton… Les **public schools** victoriennes voyaient le sport comme un moyen de former le caractère : esprit d'équipe, courage, **fair play**. L'Empire a ensuite diffusé ces sports sur tous les continents.

## Le football, une religion
Le football est le sport roi. La **Premier League**, créée en 1992, est le championnat le plus regardé du monde. Les grands clubs — Manchester United, Liverpool, Arsenal, Chelsea, Manchester City… — sont devenus des marques mondiales. Les supporters sont fidèles à leur club toute leur vie, souvent par tradition familiale. Le **derby** oppose deux clubs d'une même ville. L'Angleterre n'a gagné qu'une Coupe du monde, en 1966 ; l'Écosse, le pays de Galles et l'Irlande du Nord ont chacun leur propre équipe nationale.

## Le rugby et le Six Nations
Le rugby est très populaire au pays de Galles, en Écosse et dans certaines régions d'Angleterre. Chaque année, le **Six Nations** oppose l'Angleterre, l'Écosse, le pays de Galles, l'Irlande, la France et l'Italie. Le match Angleterre-France est souvent appelé « le Crunch ».

## Wimbledon
Le plus ancien tournoi de tennis du monde se joue depuis 1877 à **Wimbledon**, dans le sud de Londres, sur gazon. Les traditions y sont strictes : les joueurs doivent être habillés presque entièrement en blanc, et le public déguste des **strawberries and cream**. Andy Murray, écossais, a mis fin en 2013 à 77 ans d'attente d'un vainqueur britannique chez les hommes.

## Le cricket, expliqué simplement
Le **cricket** est le sport d'été par excellence. Deux équipes de onze joueurs s'affrontent. Un **bowler** lance la balle vers un **batsman** (ou **batter**), qui la frappe avec une batte plate pour protéger son **wicket**, trois piquets plantés derrière lui, et marquer des points (**runs**) en courant entre deux wickets. Les matchs peuvent durer… jusqu'à cinq jours pour les **Test matches**, avec des pauses pour le thé ! Le cricket est une passion en Inde, au Pakistan, en Australie ou aux Caraïbes. La série de matchs entre l'Angleterre et l'Australie s'appelle **The Ashes**.

## Autres traditions
Le **Grand National** (course hippique), la **Boat Race** entre Oxford et Cambridge sur la Tamise, le Marathon de Londres, ou encore les fléchettes (**darts**) et le snooker dans les pubs font aussi partie de la culture sportive britannique.
""", """
a team = une équipe
a match = un match
a fan = un supporter
a ball = un ballon, une balle
to win = gagner
to lose = perdre
a tournament = un tournoi
a referee = un arbitre
""", [
 ("Pourquoi les public schools victoriennes aimaient-elles le sport ?", ["Pour former le caractère : esprit d'équipe, courage, fair play", "Pour gagner de l'argent", "Pour remplacer les cours"], ""),
 ("Comment est né le rugby selon la légende ?", ["Un élève de l'école de Rugby a pris le ballon à la main", "Un roi l'a inventé", "Il vient de France"], ""),
 ("Qu'est-ce que la Premier League ?", ["Le championnat d'Angleterre de football", "Un tournoi de tennis", "Une course de chevaux"], ""),
 ("Quelle tradition respecte-t-on à Wimbledon ?", ["Les joueurs s'habillent en blanc et on mange des fraises à la crème", "On joue sous la pluie", "Les joueurs portent des kilts"], ""),
 ("Que fait un batsman au cricket ?", ["Il frappe la balle pour protéger son wicket et marquer des runs", "Il arbitre", "Il lance la balle"], ""),
 ("Combien de temps peut durer un Test match ?", ["Jusqu'à cinq jours", "90 minutes", "Une heure"], ""),
], [("Andy Murray", "joueur de tennis écossais, ancien numéro 1 mondial"), ("**The Ashes**", "les Cendres, trophée minuscule disputé depuis 1882")])
D = "sp"
culture(F, "Culture : Sport in Britain", 'Sport in <span>Britain</span>',
  "Culture · football, rugby, Wimbledon et le cricket expliqué", ("#86efac", "#15803d"),
  reperes("Les Britanniques ont codifié de nombreux sports modernes au 19e siècle, et l'Empire les a diffusés dans le monde entier.",
    [("1823", "naissance légendaire du rugby à l'école de Rugby"), ("1863", "règles du football fixées par la Football Association"), ("1877", "premier tournoi de Wimbledon"),
     ("1966", "l'Angleterre gagne la Coupe du monde"), ("1992", "création de la Premier League")],
    "a team, a match, a fan, a league, a tournament, a pitch, fair play, cricket"),
  {D: doc("A sporting nation", [
    "Britain gave the world many modern sports. In the 19th century, the British wrote the rules of football, rugby, tennis and many others.",
    "Football is the most popular sport. The Premier League, the English championship, is watched all over the world. Fans support their club all their life, like Liverpool or Manchester United.",
    "Rugby is very popular in Wales, Scotland and Ireland. Every year, the Six Nations tournament brings together England, Scotland, Wales, Ireland, France and Italy.",
    "Wimbledon, in London, is the oldest tennis tournament in the world. Players must wear white clothes, and people eat strawberries and cream.",
    "Cricket is the typical summer sport. A bowler throws the ball and a batter hits it. Some cricket matches last up to five days, with a break for tea!"])},
  [TF(D, "The British wrote the rules of football.", True, "« the British wrote the rules of football »."),
   TF(D, "The Premier League is only watched in England.", False, "« watched all over the world »."),
   TF(D, "The Six Nations is a rugby tournament.", True, "« the Six Nations tournament »."),
   TF(D, "At Wimbledon, players can wear any colour.", False, "« must wear white clothes »."),
   TF(D, "Cricket is a winter sport.", False, "« the typical summer sport »."),
   TF(D, "Some cricket matches last five days.", True, "« up to five days »." )],
  [Q(D, "Where is rugby very popular?", ["In Wales, Scotland and Ireland.", "Only in London.", "In the USA."]),
   Q(D, "What do people eat at Wimbledon?", ["Strawberries and cream.", "Fish and chips.", "Hot dogs."]),
   Q(D, "What does a batter do in cricket?", ["He hits the ball.", "He throws the ball.", "He serves tea."]),
   Q(D, "Which country is in the Six Nations?", ["France.", "Spain.", "Germany."])],
  [DT(D, "Quand la Premier League est-elle créée ?", ["1992", "1863", "1966", "1877"]),
   DT(D, "Comment appelle-t-on la série de matchs de cricket Angleterre-Australie ?", ["The Ashes", "The Crunch", "The Derby", "The Grand National"]),
   DT(D, "Quel Écossais gagne Wimbledon en 2013 ?", ["Andy Murray", "Roger Federer", "Rory McIlroy", "Tim Henman"]),
   DT(D, "Où se joue Wimbledon ?", ["À Londres", "À Manchester", "À Édimbourg", "À Cardiff"])],
  [W(D, "Trouve le mot qui veut dire « règles ».", "rules"), W(D, "Trouve le mot qui veut dire « supporters ».", "fans"),
   W(D, "Trouve le mot qui veut dire « fraises ».", "strawberries"), W(D, "Trouve le mot qui veut dire « une pause ».", ["break", "a break"])])

# ═════════ CUISINE UK ═════════
F = "cu_cuisine_uk.html"
DZ(F, """
## Une mauvaise réputation… injuste ?
La cuisine britannique a longtemps eu mauvaise réputation, surtout auprès des Français : légumes trop cuits, sauces fades. Cette image date en partie de la Seconde Guerre mondiale et de l'après-guerre, quand le **rationing** (rationnement, jusqu'en 1954) limitait la viande, le beurre, le sucre et les œufs. Depuis, la gastronomie britannique s'est profondément renouvelée, et Londres compte aujourd'hui parmi les capitales mondiales de la cuisine.

## Les classiques
- Le **full English breakfast** : œufs, bacon, saucisses, haricots blancs à la sauce tomate (**baked beans**), tomates, champignons, boudin noir (**black pudding**) et toasts.
- Le **fish and chips** : poisson pané frit et frites, arrosés de vinaigre de malt, longtemps emballés dans du papier journal. Apparu au 19e siècle, c'est le plat populaire par excellence.
- Le **Sunday roast** : rôti de bœuf, d'agneau ou de poulet, pommes de terre rôties, légumes, **Yorkshire puddings** (petits soufflés de pâte) et **gravy** (sauce au jus de viande).
- Les **pies** : tourtes à la viande (steak and kidney pie, shepherd's pie à l'agneau haché recouvert de purée).
- Le **haggis** écossais, le **Welsh rarebit** gallois (pain au fromage fondu), les **Cornish pasties** de Cornouailles.

## L'heure du thé
L'**afternoon tea**, inventé selon la tradition par la duchesse de Bedford dans les années 1840 pour combler la faim entre déjeuner et dîner, se compose de thé, de petits sandwiches au concombre, de **scones** avec de la **clotted cream** et de la confiture, et de gâteaux. On en sert aujourd'hui dans les grands hôtels pour les occasions spéciales. Une question divise le pays : faut-il mettre la crème ou la confiture en premier sur le scone ?

## Une cuisine du monde
La cuisine britannique est aussi le reflet de son histoire coloniale et de ses migrations. Le **curry** est l'un des plats préférés des Britanniques ; il existe des milliers de restaurants indiens et bangladais. On trouve aussi partout de la cuisine chinoise, caribéenne, turque ou polonaise.

## Bien manger, un défi
Le Royaume-Uni a aussi des problèmes de nutrition : forte consommation de plats industriels et de sucre, et un taux d'obésité parmi les plus élevés d'Europe. En 2005, le chef **Jamie Oliver** a mené une campagne célèbre pour améliorer les repas des cantines scolaires, et en 2018 une taxe sur les boissons très sucrées (la **sugar tax**) a été introduite.
""", """
breakfast = le petit-déjeuner
fish = le poisson
chips = les frites
a pie = une tourte
a roast = un rôti
tea = le thé
a cake = un gâteau
jam = la confiture
""", [
 ("Pourquoi la cuisine britannique a-t-elle eu mauvaise réputation ?", ["En partie à cause du rationnement pendant et après la guerre", "Parce qu'il n'y a pas de restaurants", "Parce que les Anglais ne mangent pas"], ""),
 ("Que trouve-t-on dans un full English breakfast ?", ["Œufs, bacon, saucisses, baked beans", "Croissants et café", "Riz et poisson cru"], ""),
 ("Comment mange-t-on traditionnellement le fish and chips ?", ["Avec du vinaigre de malt", "Avec de la crème", "Avec du chocolat"], ""),
 ("Qu'est-ce qu'un Yorkshire pudding ?", ["Un petit soufflé de pâte servi avec le rôti", "Un dessert au chocolat", "Une boisson"], ""),
 ("Quel plat est devenu l'un des préférés des Britanniques ?", ["Le curry", "La raclette", "La paella"], ""),
 ("Qu'a fait le chef Jamie Oliver en 2005 ?", ["Une campagne pour améliorer les repas des cantines", "Un restaurant sur la Lune", "Une taxe sur le thé"], ""),
], [("duchesse de Bedford", "dame d'honneur de la reine Victoria"), ("**Jamie Oliver**", "chef cuisinier anglais très médiatique")])
D = "fo"
culture(F, "Culture : British food", 'British <span>food</span>',
  "Culture · au-delà des clichés : breakfast, pies et afternoon tea", ("#fed7aa", "#c2410c"),
  reperes("La cuisine britannique, longtemps moquée, est riche de plats traditionnels et s'est ouverte aux saveurs du monde entier.",
    [("1940 – 1954", "rationnement alimentaire"), ("années 1840", "naissance de l'afternoon tea"), ("19e siècle", "apparition du fish and chips"),
     ("2005", "campagne de Jamie Oliver pour les cantines"), ("2018", "taxe sur les boissons sucrées")],
    "a full English breakfast, fish and chips, a roast, a pie, gravy, a scone, curry, a takeaway"),
  {D: doc("More than fish and chips", [
    "British food does not always have a good reputation. But British people are proud of many traditional dishes.",
    "A full English breakfast is a big meal: eggs, bacon, sausages, beans, tomatoes, mushrooms and toast. Fish and chips is the most famous takeaway: fried fish with chips, and malt vinegar.",
    "On Sundays, many families eat a Sunday roast: roast beef or chicken, roast potatoes, vegetables, Yorkshire puddings and gravy. Pies, like shepherd's pie, are also very popular.",
    "Afternoon tea is a special treat: tea, small sandwiches, scones with cream and jam, and cakes.",
    "British food is also international. Curry is one of the favourite dishes in the country, and you can find food from all over the world in British cities."])},
  [TF(D, "British food always has a good reputation.", False, "« does not always have a good reputation »."),
   TF(D, "A full English breakfast is a light meal.", False, "« a big meal »."),
   TF(D, "Fish and chips is a takeaway.", True, "« the most famous takeaway »."),
   TF(D, "Shepherd's pie is a type of pie.", True, "« Pies, like shepherd's pie »."),
   TF(D, "Scones are eaten with cream and jam.", True, "« scones with cream and jam »."),
   TF(D, "Curry is not popular in Britain.", False, "« one of the favourite dishes »." )],
  [Q(D, "What do people put on fish and chips?", ["Malt vinegar.", "Chocolate.", "Honey."]),
   Q(D, "When do families eat a roast?", ["On Sundays.", "For breakfast.", "Only at Christmas."]),
   Q(D, "What is gravy?", ["A meat sauce.", "A cake.", "A drink."]),
   Q(D, "What is afternoon tea?", ["A special treat with tea, sandwiches, scones and cakes.", "A breakfast.", "A takeaway."])],
  [DT(D, "Jusqu'à quand dure le rationnement ?", ["1954", "1945", "1918", "1970"]),
   DT(D, "De quelle région vient le haggis ?", ["L'Écosse", "Le pays de Galles", "Londres", "La Cornouailles"]),
   DT(D, "Que met-on traditionnellement sur un scone ?", ["De la crème et de la confiture", "Du ketchup", "Du fromage râpé", "Du vinaigre"]),
   DT(D, "Quelle taxe est créée en 2018 ?", ["Une taxe sur les boissons sucrées", "Une taxe sur le thé", "Une taxe sur le fish and chips", "Une taxe sur les scones"])],
  [W(D, "Trouve le mot qui veut dire « plat à emporter ».", ["takeaway", "a takeaway"]), W(D, "Trouve le mot qui veut dire « champignons ».", "mushrooms"),
   W(D, "Trouve le mot qui veut dire « une gâterie, un plaisir ».", ["treat", "a treat", "a special treat"]), W(D, "Trouve le mot qui veut dire « frit ».", "fried")])

# ═════════ ARTHUR ═════════
F = "cu_arthur.html"
DZ(F, """
## Un roi entre histoire et légende
Le roi **Arthur** est le héros le plus célèbre de la Grande-Bretagne. A-t-il existé ? Les historiens n'en sont pas sûrs. Il pourrait s'inspirer d'un chef breton (celte) qui aurait combattu les envahisseurs anglo-saxons vers l'an 500, après le départ des Romains. Au 12e siècle, l'écrivain **Geoffrey of Monmouth** raconte sa vie dans une *Histoire des rois de Bretagne* très imaginative. La légende est ensuite enrichie par des auteurs français, comme **Chrétien de Troyes**, puis rassemblée en anglais par **Thomas Malory** dans *Le Morte d'Arthur* (1485).

## L'épée dans la pierre
Selon la légende, Arthur est le fils caché du roi Uther Pendragon. Élevé loin de la cour, il devient roi en retirant d'un rocher une épée que nul autre ne pouvait arracher. Plus tard, la mystérieuse **Lady of the Lake** lui confie l'épée magique **Excalibur**. Il est conseillé par le grand magicien **Merlin**.

## Camelot et la Table ronde
Arthur règne depuis son château de **Camelot**. Il réunit autour de lui les meilleurs chevaliers : **Lancelot**, Gauvain (Gawain), Perceval, Galahad… Ils s'assoient autour d'une **Round Table**, ronde pour qu'aucun ne se sente supérieur aux autres. Les **Knights of the Round Table** suivent un code d'honneur, la chevalerie (**chivalry**) : protéger les faibles, être loyal, courageux et courtois.

## La quête du Graal
Les chevaliers partent à la recherche du **Holy Grail**, la coupe utilisée par le Christ lors de la Cène, aux pouvoirs mystérieux. Seul le chevalier le plus pur, Galahad, parvient à le trouver.

## La chute de Camelot
Le royaume s'effondre à cause de trahisons : l'amour entre la reine **Guinevere**, épouse d'Arthur, et Lancelot divise les chevaliers ; le neveu (ou fils) d'Arthur, **Mordred**, se révolte. Dans une dernière bataille, Arthur tue Mordred mais est mortellement blessé. Il est emporté vers l'île magique d'**Avalon**. La légende dit qu'il ne serait pas mort et reviendra quand la Grande-Bretagne aura besoin de lui : on l'appelle « le roi d'autrefois et de demain ».

## Une légende toujours vivante
Des lieux revendiquent le souvenir d'Arthur, comme **Tintagel** en Cornouailles ou **Glastonbury**, où des moines prétendirent au 12e siècle avoir trouvé sa tombe. La légende a inspiré d'innombrables œuvres : romans, films (*Excalibur*, *Kaamelott* en France), dessins animés (*Merlin l'enchanteur* de Disney), et même la parodie des Monty Python, *Monty Python and the Holy Grail*.
""", """
a king = un roi
a sword = une épée
a stone = une pierre
a knight = un chevalier
a wizard = un magicien
a castle = un château
a quest = une quête
a lake = un lac
""", [
 ("Le roi Arthur a-t-il vraiment existé ?", ["Les historiens n'en sont pas sûrs", "Oui, c'est certain", "Non, il a été inventé en 2000"], ""),
 ("Comment Arthur devient-il roi ?", ["En retirant une épée d'un rocher", "En gagnant une course", "En épousant une reine"], ""),
 ("Pourquoi la Table ronde est-elle ronde ?", ["Pour qu'aucun chevalier ne se sente supérieur aux autres", "Parce que c'était moins cher", "Pour danser autour"], ""),
 ("Qu'est-ce que le Saint Graal ?", ["La coupe utilisée par le Christ lors de la Cène", "Une épée", "Un château"], ""),
 ("Qu'est-ce qui provoque la chute de Camelot ?", ["Les trahisons : Lancelot et Guenièvre, la révolte de Mordred", "Une inondation", "Une invasion viking"], ""),
 ("Où Arthur est-il emporté à la fin ?", ["Sur l'île d'Avalon", "À Londres", "En France"], ""),
], [("Geoffrey of Monmouth", "clerc gallois du 12e siècle"), ("Chrétien de Troyes", "poète français du 12e siècle"), ("Thomas Malory", "chevalier et écrivain anglais du 15e siècle"), ("*Kaamelott*", "série française d'Alexandre Astier")])
D = "ar"
culture(F, "Culture : King Arthur", 'King <span>Arthur</span>',
  "Culture · Excalibur, Merlin et les chevaliers de la Table ronde", ("#c7d2fe", "#3730a3"),
  reperes("Le roi Arthur est un héros légendaire de la Grande-Bretagne. Son histoire mêle magie, chevalerie et trahison.",
    [("vers 500", "un possible chef breton combattant les Anglo-Saxons"), ("12e siècle", "Geoffrey of Monmouth, puis Chrétien de Troyes racontent la légende"), ("1485", "Le Morte d'Arthur de Thomas Malory")],
    "a king, a knight, a sword, a wizard, a quest, the Round Table, the Holy Grail, chivalry"),
  {D: doc("The once and future king", [
    "King Arthur is the most famous legendary hero of Britain. Nobody knows if he really existed.",
    "According to the legend, young Arthur became king when he pulled a sword out of a stone. No other man could do it. Later, the Lady of the Lake gave him a magic sword called Excalibur.",
    "Arthur lived in the castle of Camelot with his wife, Queen Guinevere. He was helped by Merlin, a powerful wizard. His best knights, like Lancelot, sat around the Round Table, so that nobody was more important than the others.",
    "The knights went on a quest to find the Holy Grail, a magic cup. Only Galahad, the purest knight, found it.",
    "But Lancelot fell in love with Guinevere, and Arthur's nephew Mordred betrayed him. In a last battle, Arthur was badly wounded and taken to the magic island of Avalon. Some people say he will come back one day."])},
  [TF(D, "Historians are sure that Arthur existed.", False, "« Nobody knows if he really existed »."),
   TF(D, "Arthur pulled a sword out of a stone.", True, "« he pulled a sword out of a stone »."),
   TF(D, "Excalibur was given by the Lady of the Lake.", True, "« the Lady of the Lake gave him a magic sword »."),
   TF(D, "Merlin was a knight.", False, "« a powerful wizard »."),
   TF(D, "Lancelot found the Holy Grail.", False, "C'est Galahad."),
   TF(D, "Mordred betrayed Arthur.", True, "« Mordred betrayed him »." )],
  [Q(D, "Why was the table round?", ["So that nobody was more important than the others.", "Because it was cheaper.", "Because Merlin liked circles."]),
   Q(D, "What is the Holy Grail?", ["A magic cup.", "A sword.", "A castle."]),
   Q(D, "Who fell in love with Guinevere?", ["Lancelot.", "Merlin.", "Galahad."]),
   Q(D, "Where was Arthur taken at the end?", ["To the island of Avalon.", "To Camelot.", "To London."])],
  [DT(D, "Comment s'appelle le château d'Arthur ?", ["Camelot", "Avalon", "Tintagel", "Windsor"]),
   DT(D, "Comment s'appelle l'épée magique ?", ["Excalibur", "Durandal", "Joyeuse", "Glamdring"]),
   DT(D, "Quel lieu de Cornouailles est lié à Arthur ?", ["Tintagel", "Brighton", "Oxford", "Liverpool"]),
   DT(D, "Qui a écrit Le Morte d'Arthur (1485) ?", ["Thomas Malory", "Shakespeare", "Chrétien de Troyes", "Tolkien"])],
  [W(D, "Trouve le mot qui veut dire « épée ».", ["sword", "a sword"]), W(D, "Trouve le mot qui veut dire « magicien ».", ["wizard", "a wizard"]),
   W(D, "Trouve le mot qui veut dire « chevaliers ».", "knights"), W(D, "Trouve le mot qui veut dire « a trahi ».", "betrayed")])

# ═════════ ROBIN HOOD ═════════
F = "cu_robin_hood.html"
DZ(F, """
## Un hors-la-loi au grand cœur
**Robin Hood** est le héros d'une des légendes anglaises les plus populaires : un **outlaw** qui vole les riches pour donner aux pauvres. Il vit caché dans la forêt de **Sherwood**, près de **Nottingham**, avec sa bande de compagnons, les **Merry Men**. C'est un archer extraordinaire, capable de fendre une flèche déjà plantée dans la cible.

## Les personnages
- **Little John**, son fidèle lieutenant, un géant (son surnom est une plaisanterie) ;
- **Friar Tuck**, un moine joyeux et gourmand qui sait se battre ;
- **Maid Marian**, la femme qu'il aime ;
- **Will Scarlet** et d'autres compagnons ;
- et leur grand ennemi, le cruel **Sheriff of Nottingham**, qui écrase le peuple d'impôts.
Dans de nombreuses versions, l'histoire se déroule à la fin du 12e siècle : le bon roi **Richard the Lionheart** (Richard Cœur de Lion) est parti en croisade, et son frère, le méchant prince **John** (Jean sans Terre), opprime le pays. Robin reste fidèle au vrai roi, qui finit par revenir et lui pardonner.

## A-t-il existé ?
Personne ne le sait. Des ballades populaires parlent de Robin Hood dès le 14e et le 15e siècle. Il pourrait s'inspirer d'un ou plusieurs hors-la-loi réels. Le nom « Robinhood » apparaît même dans des registres judiciaires comme surnom donné aux criminels. Les premières ballades le montrent plutôt comme un simple brigand ; c'est au fil des siècles qu'il devient un noble déchu, défenseur des opprimés.

## Pourquoi cette légende plaît-elle autant ?
Robin Hood incarne la justice contre l'abus de pouvoir, la liberté de la forêt contre les lois injustes, la ruse contre la force. À l'époque, les forêts royales étaient réservées à la chasse du roi : chasser un cerf pouvait être puni de mort. Le hors-la-loi qui vit dans les bois et nargue les autorités est donc un héros du peuple.

## Une légende sans fin
L'histoire a été racontée d'innombrables fois : dans des romans, comme *Ivanhoe* de Walter Scott, au cinéma (avec Errol Flynn en 1938, Kevin Costner en 1991, Russell Crowe en 2010), dans le dessin animé de Disney de 1973 où Robin est un renard, ou à la télévision. Aujourd'hui, Nottingham accueille une statue de Robin Hood, et l'expression « *a Robin Hood tax* » désigne un impôt qui prend aux riches pour aider les pauvres.
""", """
an outlaw = un hors-la-loi
a forest = une forêt
an arrow = une flèche
the rich = les riches
the poor = les pauvres
a thief = un voleur
a sheriff = un shérif
a bow = un arc
""", [
 ("Que fait Robin des Bois ?", ["Il vole les riches pour donner aux pauvres", "Il vole les pauvres", "Il protège le shérif"], ""),
 ("Où vit-il caché ?", ["Dans la forêt de Sherwood", "À Londres", "En Écosse"], ""),
 ("Qui est son grand ennemi ?", ["Le shérif de Nottingham", "Little John", "Richard Cœur de Lion"], ""),
 ("Pourquoi le surnom de Little John est-il drôle ?", ["C'est un géant", "Il est très petit", "Il s'appelle Paul"], ""),
 ("Pourquoi chasser dans la forêt royale était-il dangereux ?", ["Elle était réservée au roi : on pouvait être puni de mort", "Il y avait des loups", "Il faisait trop froid"], ""),
 ("Que signifie « a Robin Hood tax » ?", ["Un impôt qui prend aux riches pour aider les pauvres", "Une taxe sur les arcs", "Un impôt sur les forêts"], ""),
], [("**Richard the Lionheart**", "roi d'Angleterre de 1189 à 1199, parti en croisade"), ("*Ivanhoe*", "roman historique de 1819"), ("Walter Scott", "écrivain écossais")])
D = "rh"
culture(F, "Culture : Robin Hood", 'Robin <span>Hood</span>',
  "Culture · le hors-la-loi de la forêt de Sherwood", ("#bbf7d0", "#14532d"),
  reperes("Robin des Bois est un hors-la-loi légendaire qui vole les riches pour donner aux pauvres, dans la forêt de Sherwood, près de Nottingham.",
    [("fin du 12e siècle", "époque où se déroule souvent l'histoire (Richard Cœur de Lion, prince Jean)"), ("14e – 15e siècles", "premières ballades sur Robin Hood"), ("1973", "dessin animé de Disney, Robin en renard")],
    "an outlaw, a forest, an archer, a bow, an arrow, the rich, the poor, a sheriff"),
  {D: doc("Rob the rich, give to the poor", [
    "Robin Hood is a famous English hero. According to the legend, he was an outlaw who stole from the rich to give to the poor.",
    "He lived in Sherwood Forest, near Nottingham, with his friends, the Merry Men: Little John, a very tall man, Friar Tuck, a funny monk, and many others. He loved Maid Marian.",
    "Robin was the best archer in England. His great enemy was the cruel Sheriff of Nottingham, who took money from poor people.",
    "In many stories, good King Richard the Lionheart was away, and his bad brother, Prince John, ruled the country. Robin stayed loyal to Richard.",
    "Nobody knows if Robin Hood really existed, but people have told his story for more than 600 years, in songs, books and films."])},
  [TF(D, "Robin Hood stole from the poor.", False, "« stole from the rich to give to the poor »."),
   TF(D, "He lived in Sherwood Forest.", True, "« in Sherwood Forest »."),
   TF(D, "Little John was a very small man.", False, "« a very tall man »."),
   TF(D, "Friar Tuck was a monk.", True, "« a funny monk »."),
   TF(D, "The Sheriff of Nottingham was Robin's friend.", False, "« His great enemy »."),
   TF(D, "We are sure that Robin Hood really existed.", False, "« Nobody knows »." )],
  [Q(D, "Who were the Merry Men?", ["Robin's friends.", "The Sheriff's soldiers.", "The King's sons."]),
   Q(D, "Who did Robin love?", ["Maid Marian.", "Queen Guinevere.", "The Sheriff's sister."]),
   Q(D, "What was Robin's talent?", ["He was the best archer in England.", "He was a great singer.", "He was a wizard."]),
   Q(D, "Who was Robin loyal to?", ["King Richard the Lionheart.", "Prince John.", "The Sheriff."])],
  [DT(D, "Près de quelle ville se trouve Sherwood ?", ["Nottingham", "Londres", "York", "Cambridge"]),
   DT(D, "Quel animal est Robin dans le Disney de 1973 ?", ["Un renard", "Un lion", "Un ours", "Un loup"]),
   DT(D, "Qui est le frère méchant de Richard ?", ["Le prince Jean", "Le shérif", "Little John", "Mordred"]),
   DT(D, "Depuis quand raconte-t-on son histoire ?", ["Plus de 600 ans", "50 ans", "2 000 ans", "Depuis 1973"])],
  [W(D, "Trouve le mot qui veut dire « hors-la-loi ».", ["outlaw", "an outlaw"]), W(D, "Trouve le mot qui veut dire « a volé ».", "stole"),
   W(D, "Trouve le mot qui veut dire « archer ».", "archer"), W(D, "Trouve le mot qui veut dire « fidèle ».", "loyal")])

# ═════════ GHOSTS ═════════
F = "cu_fantomes.html"
DZ(F, """
## Le pays le plus hanté du monde ?
Les Britanniques adorent les histoires de fantômes, et le Royaume-Uni est souvent présenté comme l'un des pays les plus « hantés » du monde. Avec ses vieux châteaux, ses manoirs, ses pubs centenaires, ses champs de bataille et sa météo brumeuse, il offre un décor parfait. De nombreux sites proposent des **ghost tours**, visites guidées nocturnes, en particulier à Londres, à York et à Édimbourg.

## Des fantômes royaux
La **Tower of London** serait hantée par **Anne Boleyn**, la deuxième épouse d'Henry VIII, décapitée en 1536 : on dit qu'elle erre, la tête sous le bras. On y évoque aussi les « princes de la Tour », deux jeunes princes disparus en 1483. **Hampton Court Palace** aurait son propre spectre : Catherine Howard, cinquième épouse d'Henry, qui courrait en hurlant dans une galerie.

## Édimbourg et York
Sous les rues d'Édimbourg se cachent des **vaults**, des caves voûtées où vivaient autrefois les plus pauvres ; on y organise des visites à la lanterne. **York**, ville fortifiée du nord de l'Angleterre, se dit la ville la plus hantée d'Europe : on raconte qu'un jeune ouvrier y aurait vu dans une cave une troupe de soldats romains fantômes traverser le mur.

## Le monstre du Loch Ness
En Écosse, le **Loch Ness**, un lac long et très profond, abriterait une créature mystérieuse : **Nessie**. Des récits anciens existent, mais la légende moderne naît en 1933, quand une route est construite le long du lac et que des témoins disent avoir vu un animal. En 1934, une célèbre photo semble montrer une longue tête et un cou sortant de l'eau ; on découvrira en 1994 que c'était un trucage réalisé avec un jouet sous-marin. Malgré les recherches scientifiques, aucune preuve n'a jamais été trouvée, mais Nessie attire chaque année des milliers de touristes.

## Halloween et les traditions
**Halloween** vient d'une ancienne fête celte, **Samhain**, célébrée en Irlande et en Écosse à la fin des récoltes, quand on croyait que la frontière entre le monde des vivants et celui des morts s'amincissait. Les immigrants irlandais et écossais l'ont apportée aux États-Unis, qui l'ont transformée en grande fête commerciale avant qu'elle ne revienne en Europe. À l'origine, on creusait des navets, pas des citrouilles !

## Les histoires qui font peur
La littérature britannique est riche en récits d'horreur et de fantômes : *Frankenstein* de Mary Shelley (1818), *Dracula* de l'Irlandais Bram Stoker (1897), *A Christmas Carol* de Dickens avec ses trois fantômes de Noël, ou *The Woman in Black*. Raconter des **ghost stories** au coin du feu, notamment à Noël, est une vieille tradition anglaise.
""", """
a ghost = un fantôme
a castle = un château
a monster = un monstre
a lake = un lac
fear = la peur
haunted = hanté
a legend = une légende
a photo = une photo
""", [
 ("Qu'est-ce qu'un « ghost tour » ?", ["Une visite guidée nocturne sur les lieux hantés", "Un tour de magie", "Un jeu vidéo"], ""),
 ("Quel fantôme hanterait la Tour de Londres ?", ["Anne Boleyn, la tête sous le bras", "Shakespeare", "Nessie"], ""),
 ("Quelle ville se dit la plus hantée d'Europe ?", ["York", "Paris", "Dublin"], ""),
 ("Quand naît la légende moderne de Nessie ?", ["En 1933, après la construction d'une route le long du lac", "En 1066", "En 2000"], ""),
 ("Qu'était la célèbre photo de 1934 ?", ["Un trucage réalisé avec un jouet", "Une vraie preuve", "Une baleine"], ""),
 ("D'où vient Halloween ?", ["D'une ancienne fête celte, Samhain", "D'une fête américaine récente", "D'une fête romaine"], ""),
], [("**Anne Boleyn**", "deuxième épouse d'Henry VIII, mère d'Elizabeth I"), ("Hampton Court Palace", "palais d'Henry VIII près de Londres"), ("Mary Shelley", "romancière anglaise"), ("Bram Stoker", "écrivain irlandais")])
D = "gh"
culture(F, "Culture : Ghosts and Loch Ness", 'Ghosts <span>&amp; Nessie</span>',
  "Culture · châteaux hantés, monstre du Loch Ness et Halloween", ("#a5b4fc", "#1e1b4b"),
  reperes("Les Britanniques adorent les histoires de fantômes. Châteaux, pubs et lacs écossais ont tous leur légende.",
    [("1536", "exécution d'Anne Boleyn, dont le fantôme hanterait la Tour de Londres"), ("1897", "Dracula de Bram Stoker"), ("1933", "naissance de la légende moderne de Nessie"),
     ("1934", "la fausse photo du monstre"), ("31 octobre", "Halloween, héritée de la fête celte de Samhain")],
    "a ghost, a castle, haunted, a monster, a lake, a legend, scary, a pumpkin"),
  {D: doc("Things that go bump in the night", [
    "Britain is often called one of the most haunted countries in the world. Many old castles, houses and pubs have their own ghost stories.",
    "The Tower of London is said to be haunted by Anne Boleyn, the wife of Henry VIII. She was beheaded in 1536, and people say she walks with her head under her arm!",
    "In Scotland, Loch Ness is a very deep lake. Some people believe that a monster, Nessie, lives in it. A famous photo from 1934 seemed to show the monster, but it was a fake.",
    "Halloween comes from an old Celtic festival in Ireland and Scotland. People believed that ghosts came back on that night. Irish immigrants took the tradition to America.",
    "British writers also love scary stories: Dracula, Frankenstein or the ghosts of A Christmas Carol. Telling ghost stories at Christmas is an old English tradition."])},
  [TF(D, "Many British castles have ghost stories.", True, "« have their own ghost stories »."),
   TF(D, "Anne Boleyn was the wife of Henry VIII.", True, "« the wife of Henry VIII »."),
   TF(D, "Loch Ness is a small and shallow lake.", False, "« a very deep lake »."),
   TF(D, "The 1934 photo was a real proof of Nessie.", False, "« it was a fake »."),
   TF(D, "Halloween comes from a Celtic festival.", True, "« an old Celtic festival »."),
   TF(D, "Telling ghost stories at Christmas is an English tradition.", True, "« an old English tradition »." )],
  [Q(D, "What do people say about Anne Boleyn's ghost?", ["She walks with her head under her arm.", "She sings every night.", "She lives in Loch Ness."]),
   Q(D, "What is Nessie?", ["A legendary monster in Loch Ness.", "A castle.", "A ghost in London."]),
   Q(D, "Who took Halloween to America?", ["Irish immigrants.", "The Romans.", "The Vikings."]),
   Q(D, "Which story has ghosts at Christmas?", ["A Christmas Carol.", "Dracula.", "Robin Hood."])],
  [DT(D, "Qui a écrit Dracula ?", ["Bram Stoker", "Mary Shelley", "Charles Dickens", "Shakespeare"]),
   DT(D, "Dans quel pays se trouve le Loch Ness ?", ["L'Écosse", "L'Irlande", "Le pays de Galles", "L'Angleterre"]),
   DT(D, "Comment s'appelait la fête celte d'origine ?", ["Samhain", "Beltane", "Yule", "Diwali"]),
   DT(D, "Que creusait-on à l'origine à Halloween ?", ["Des navets", "Des citrouilles", "Des pommes", "Des carottes"])],
  [W(D, "Trouve le mot qui veut dire « hanté ».", "haunted"), W(D, "Trouve le mot qui veut dire « décapitée ».", "beheaded"),
   W(D, "Trouve le mot qui veut dire « un faux, un trucage ».", ["fake", "a fake"]), W(D, "Trouve le mot qui veut dire « effrayantes ».", "scary")])

# ═════════ US LEGENDS ═════════
F = "cu_legendes_us.html"
DZ(F, """
## Des mythes amérindiens
Bien avant l'arrivée des Européens, les peuples amérindiens racontaient des mythes pour expliquer le monde : la création de la Terre sur le dos d'une tortue géante (chez les Iroquois et d'autres peuples, d'où le nom de **Turtle Island** pour l'Amérique du Nord), le **Coyote** et le **Raven**, figures rusées et farceuses qui volent le feu ou la lumière pour les donner aux humains, ou le **Thunderbird**, oiseau géant dont les battements d'ailes provoquent le tonnerre. Ces récits, transmis oralement, sont toujours vivants et respectés comme une partie de la spiritualité de ces peuples.

## Les « tall tales » des pionniers
Au 19e siècle, les pionniers et les travailleurs de l'Ouest inventent des **tall tales**, des histoires volontairement exagérées et drôles :
- **Paul Bunyan**, bûcheron géant, accompagné de **Babe the Blue Ox**, son bœuf bleu ; ses pas auraient creusé les lacs du Minnesota ;
- **Pecos Bill**, cow-boy élevé par des coyotes, qui chevauchait une tornade ;
- **John Henry**, ouvrier noir du chemin de fer, qui défie une machine à vapeur pour creuser un tunnel, gagne… puis meurt d'épuisement : un symbole de la dignité des travailleurs face aux machines ;
- **Johnny Appleseed**, personnage inspiré d'un homme réel, John Chapman, qui plantait des pommiers partout sur son passage.

## Les monstres d'Amérique
Comme le Loch Ness, l'Amérique a ses créatures mystérieuses : le **Bigfoot** (ou Sasquatch), grand singe velu qui vivrait dans les forêts du Nord-Ouest ; le **Mothman** de Virginie-Occidentale ; le **Jersey Devil** du New Jersey. Aucune preuve scientifique n'existe, mais ces créatures font vivre des festivals, des musées et des émissions de télévision.

## Les légendes urbaines
Les **urban legends** sont des histoires modernes racontées comme vraies, souvent « arrivées à l'ami d'un ami » : des crocodiles dans les égouts de New York, l'auto-stoppeuse fantôme qui disparaît de la voiture, **Bloody Mary** qu'on invoque devant un miroir… Elles circulent aujourd'hui sur Internet sous la forme de **creepypastas**, histoires effrayantes partagées en ligne, comme celle de **Slender Man**.

## Washington, Lincoln et les mythes patriotiques
L'histoire américaine a aussi ses légendes. On raconte que le jeune **George Washington** aurait abattu le cerisier de son père et avoué : « Je ne peux pas mentir ». Cette anecdote, inventée par un biographe après sa mort, servait à enseigner l'honnêteté aux enfants. Ces mythes montrent comment une nation se raconte et se choisit des héros.
""", """
a legend = une légende
a giant = un géant
a monster = un monstre
a forest = une forêt
a story = une histoire
a turtle = une tortue
a tree = un arbre
true = vrai
""", [
 ("Pourquoi certains peuples amérindiens appellent-ils l'Amérique « Turtle Island » ?", ["Selon un mythe, la Terre a été créée sur le dos d'une tortue géante", "Il y a beaucoup de tortues", "C'est une île"], ""),
 ("Qu'est-ce qu'une « tall tale » ?", ["Une histoire volontairement exagérée et drôle", "Une histoire vraie", "Un conte de fées européen"], ""),
 ("Qui est Paul Bunyan ?", ["Un bûcheron géant accompagné d'un bœuf bleu", "Un président", "Un monstre"], ""),
 ("Que symbolise John Henry ?", ["La dignité des travailleurs face aux machines", "La richesse", "La guerre"], ""),
 ("Où vivrait le Bigfoot ?", ["Dans les forêts du Nord-Ouest", "Dans un lac écossais", "À New York"], ""),
 ("Pourquoi l'histoire du cerisier de Washington a-t-elle été inventée ?", ["Pour enseigner l'honnêteté aux enfants", "Pour vendre des cerises", "Pour gagner une élection"], ""),
], [("John Chapman", "pépiniériste américain du début du 19e siècle"), ("**George Washington**", "premier président des États-Unis")])
D = "lu"
culture(F, "Culture : American myths and legends", 'American <span>legends</span>',
  "Culture · mythes amérindiens, tall tales, Bigfoot et légendes urbaines", ("#fcd34d", "#7c2d12"),
  reperes("Des mythes amérindiens aux légendes urbaines d'Internet, l'Amérique a toujours raconté des histoires pour expliquer le monde, faire rire ou faire peur.",
    [("tradition orale", "mythes amérindiens : Turtle Island, Coyote, Thunderbird"), ("19e siècle", "tall tales des pionniers : Paul Bunyan, Pecos Bill, John Henry"), ("depuis les années 1950", "le Bigfoot devient célèbre"), ("21e siècle", "creepypastas sur Internet")],
    "a legend, a myth, a tall tale, a giant, a monster, an urban legend, a hero, scary"),
  {D: doc("Tall tales and strange creatures", [
    "Long before Europeans arrived, Native Americans told myths to explain the world. Some peoples believed that the Earth was created on the back of a giant turtle.",
    "In the 19th century, pioneers invented \"tall tales\", funny stories with lots of exaggeration. Paul Bunyan was a giant lumberjack with a blue ox called Babe. People said his footprints made the lakes of Minnesota!",
    "John Henry was a strong railroad worker. He raced against a steam machine to dig a tunnel. He won, but he died of exhaustion. He is a symbol of workers against machines.",
    "America also has its monsters. Bigfoot is a big, hairy creature that some people say lives in the forests of the North-West. But there is no scientific proof.",
    "Today, urban legends are modern stories that people tell as true, like crocodiles in the sewers of New York. They often spread on the Internet."])},
  [TF(D, "Native Americans told myths to explain the world.", True, "« to explain the world »."),
   TF(D, "Tall tales are serious and realistic stories.", False, "« funny stories with lots of exaggeration »."),
   TF(D, "Paul Bunyan had a blue ox.", True, "« a blue ox called Babe »."),
   TF(D, "John Henry lost the race against the machine.", False, "« He won »."),
   TF(D, "Scientists have proved that Bigfoot exists.", False, "« there is no scientific proof »."),
   TF(D, "Urban legends often spread on the Internet.", True, "« They often spread on the Internet »." )],
  [Q(D, "What did some Native peoples believe about the Earth?", ["It was created on the back of a giant turtle.", "It was flat.", "It was made by Paul Bunyan."]),
   Q(D, "What made the lakes of Minnesota, according to the tall tale?", ["Paul Bunyan's footprints.", "A tornado.", "Bigfoot."]),
   Q(D, "What happened to John Henry?", ["He won the race but died of exhaustion.", "He became president.", "He lived in a forest."]),
   Q(D, "What is an urban legend?", ["A modern story told as true.", "A real news story.", "A Native myth."])],
  [DT(D, "Quel cow-boy chevauchait une tornade ?", ["Pecos Bill", "Paul Bunyan", "John Henry", "Davy Crockett"]),
   DT(D, "Comment s'appelle aussi le Bigfoot ?", ["Sasquatch", "Nessie", "Yeti des Alpes", "Thunderbird"]),
   DT(D, "Qui plantait des pommiers partout ?", ["Johnny Appleseed", "George Washington", "Paul Bunyan", "Abraham Lincoln"]),
   DT(D, "Quel oiseau géant provoque le tonnerre dans les mythes ?", ["Le Thunderbird", "Le Raven", "L'aigle chauve", "Le Phénix"])],
  [W(D, "Trouve le mot qui veut dire « bûcheron ».", ["lumberjack", "a giant lumberjack"]), W(D, "Trouve le mot qui veut dire « empreintes de pas ».", "footprints"),
   W(D, "Trouve le mot qui veut dire « épuisement ».", "exhaustion"), W(D, "Trouve le mot qui veut dire « égouts ».", "sewers")])
END()
