import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
exec(open(_EA_OUT+"/cuhelp.py", encoding="utf-8").read())

# ═════════ TRAVAIL USA ═════════
F = "cu_travail_usa.html"
DZ(F, """
## Ford et la chaîne de montage
En 1908, **Henry Ford** lance la **Model T**, une voiture simple et solide. Pour la produire en masse, il installe en 1913, dans son usine près de Detroit, la première grande **assembly line** mobile : la voiture avance devant les ouvriers, et chacun répète toujours le même geste. Le temps de montage d'une voiture passe d'environ 12 heures à moins de deux heures, et le prix baisse tellement que des millions d'Américains peuvent en acheter une. Ford s'inspire du **taylorisme**, l'« organisation scientifique du travail » de l'ingénieur Frederick Taylor, qui chronomètre chaque geste pour supprimer les temps morts.
Mais le travail est épuisant et monotone, et les ouvriers quittent vite l'usine. En 1914, Ford crée le **Five Dollar Day** : il double presque les salaires et réduit la journée à 8 heures. Ses ouvriers peuvent ainsi acheter les voitures qu'ils fabriquent : c'est le début de la société de consommation de masse. Charlie Chaplin se moque de ce travail à la chaîne dans *Modern Times* (1936).

## Le travail des enfants
Vers 1900, près de deux millions d'enfants américains travaillent dans les mines, les usines textiles, les conserveries ou dans la rue comme vendeurs de journaux. Le photographe **Lewis Hine** les photographie en secret pour alerter l'opinion. Une loi fédérale de **1938** fixe enfin un âge minimum et un salaire minimum. Pourtant, le travail des enfants n'a pas totalement disparu : aux États-Unis, la loi reste plus souple dans l'agriculture, des enquêtes ont révélé ces dernières années des mineurs, souvent migrants, employés illégalement dans des usines ou des abattoirs, et certains États ont assoupli leurs lois. Dans le monde, l'Organisation internationale du travail estime qu'environ 140 millions d'enfants travaillent encore, y compris dans des pays anglophones comme l'Inde ou le Nigeria.

## Teen jobs
Aux États-Unis, beaucoup d'adolescents ont un petit boulot à partir de 14-16 ans : **babysitting**, tonte de pelouses, fast-food, caisse de supermarché, **lifeguard** à la piscine, **summer camps**. On y voit une façon d'apprendre la responsabilité et la valeur de l'argent ; certains y voient aussi une nécessité pour aider leur famille.

## La philanthropie
Les grandes fortunes américaines ont une tradition de **philanthropy**. **Andrew Carnegie**, roi de l'acier, écrit en 1889 que mourir riche est une honte ; il finance environ 2 500 bibliothèques publiques dans le monde. Les Rockefeller créent une fondation en 1913. Aujourd'hui, la **Gates Foundation** dépense des milliards contre les maladies dans le monde, et avec la **Giving Pledge** (2010), des milliardaires promettent de donner la majorité de leur fortune. Pour leurs partisans, ces dons font énormément de bien. Pour leurs critiques, ils permettent aussi de payer moins d'impôts et donnent à quelques personnes très riches un pouvoir énorme, sans contrôle démocratique.

## Et demain ?
Le travail continue de changer : télétravail depuis la pandémie, **gig economy** (chauffeurs et livreurs payés à la tâche par des applications), automatisation et intelligence artificielle. Le premier lundi de septembre, **Labor Day** rend hommage aux travailleurs américains.
[→ Voir aussi : le monde du travail](cu_travail.html)
""", """
a factory = une usine
a worker = un ouvrier
a car = une voiture
a wage = un salaire
a child = un enfant
a job = un emploi
a library = une bibliothèque
to donate = faire un don
""", [
 ("Qu'est-ce que la chaîne de montage de Ford ?", ["La voiture avance devant les ouvriers qui répètent le même geste", "Un collier", "Un train"], ""),
 ("Pourquoi Ford crée-t-il le Five Dollar Day ?", ["Pour garder ses ouvriers et qu'ils puissent acheter ses voitures", "Pour fêter Noël", "Parce que la loi l'oblige"], ""),
 ("Qu'a fait Lewis Hine ?", ["Il a photographié des enfants au travail pour alerter l'opinion", "Il a inventé la voiture", "Il a fondé une bibliothèque"], ""),
 ("Le travail des enfants a-t-il complètement disparu ?", ["Non, il existe encore, aux États-Unis et dans le monde", "Oui, partout", "Il n'a jamais existé"], ""),
 ("Qu'a financé Andrew Carnegie ?", ["Environ 2 500 bibliothèques publiques", "Des usines d'armes", "Des stades"], ""),
 ("Quelle critique fait-on à la philanthropie ?", ["Elle donne un grand pouvoir à quelques riches sans contrôle démocratique", "Elle ne donne jamais d'argent", "Elle est obligatoire"], ""),
], [("Frederick Taylor", "ingénieur américain, 1856-1915"), ("**Lewis Hine**", "photographe et sociologue américain")])
D = "tu"
culture(F, "Culture : Work in America", 'Work <span>in America</span>',
  "Culture · Ford, le travail des enfants, les teen jobs et la philanthropie", ("#bfdbfe", "#7c2d12"),
  reperes("Les États-Unis ont été un laboratoire du travail moderne : chaîne de montage, consommation de masse, mais aussi travail des enfants et philanthropie.",
    [("1908", "la Ford Model T"), ("1913", "première grande chaîne de montage mobile"), ("1914", "le Five Dollar Day"),
     ("1938", "loi fédérale contre le travail des enfants"), ("2010", "la Giving Pledge des milliardaires"), ("1er lundi de septembre", "Labor Day")],
    "an assembly line, mass production, a wage, child labour, a teen job, philanthropy, a foundation, the gig economy"),
  {D: doc("From the assembly line to the gig economy", [
    "In 1913, Henry Ford created a moving assembly line. Each worker did the same task again and again. Cars became much cheaper, and millions of Americans could buy one.",
    "The work was boring and tiring, so Ford doubled the wages in 1914. His workers could buy the cars they made.",
    "Around 1900, almost two million American children worked in factories and mines. A law stopped most child labour in 1938, but it has not completely disappeared, in the USA or in the world.",
    "Many American teenagers have part-time jobs: babysitting, working in fast-food restaurants or as lifeguards.",
    "Some very rich Americans give a lot of money to good causes. This is called philanthropy. Andrew Carnegie paid for thousands of public libraries."])},
  [TF(D, "Henry Ford created a moving assembly line.", True, "« created a moving assembly line »."),
   TF(D, "Cars became more expensive.", False, "« much cheaper »."),
   TF(D, "Ford doubled the wages in 1914.", True, "« doubled the wages in 1914 »."),
   TF(D, "Child labour has completely disappeared.", False, "« has not completely disappeared »."),
   TF(D, "Many American teenagers have part-time jobs.", True, "« part-time jobs »."),
   TF(D, "Andrew Carnegie paid for public libraries.", True, "« thousands of public libraries »." )],
  [Q(D, "What did each worker do on the assembly line?", ["The same task again and again.", "A whole car alone.", "Nothing."]),
   Q(D, "Why did Ford double the wages?", ["Because the work was boring and tiring.", "Because cars were expensive.", "Because of a war."]),
   Q(D, "Where did children work around 1900?", ["In factories and mines.", "In offices.", "In schools."]),
   Q(D, "What is philanthropy?", ["Giving money to good causes.", "Selling cars.", "Working as a lifeguard."])],
  [DT(D, "Quel film de Chaplin critique le travail à la chaîne ?", ["Modern Times", "The Kid", "The Gold Rush", "The Great Dictator"]),
   DT(D, "Quelle voiture Ford lance-t-il en 1908 ?", ["La Model T", "La Mustang", "La Beetle", "La Cadillac"]),
   DT(D, "Quel jour honore les travailleurs américains ?", ["Labor Day", "Thanksgiving", "Memorial Day", "Juneteenth"]),
   DT(D, "Comment dit-on « une chaîne de montage » ?", ["An assembly line", "A factory chain", "A work line", "A mounting chain"])],
  [W(D, "Trouve le mot qui veut dire « une tâche ».", ["task", "the same task"]), W(D, "Trouve le mot qui veut dire « fatigant ».", "tiring"),
   W(D, "Trouve le mot qui veut dire « le travail des enfants » (2 mots).", ["child labour"]), W(D, "Trouve le mot qui veut dire « maître-nageur ».", ["lifeguards", "lifeguard"])])

# ═════════ GAG ═════════
F = "cu_gag.html"
DZ(F, """
## Le slapstick
Le **slapstick** est un comique physique, fait de chutes, de coups, de poursuites et de catastrophes. Le mot vient d'un bâton de bois double utilisé au théâtre, qui produisait un grand claquement (*slap*) sans faire mal. Né dans le **music-hall** britannique et le vaudeville américain, ce comique sans paroles devient la star du **cinéma muet**, qui peut être compris dans le monde entier.

## Charlie Chaplin
**Charlie Chaplin** (1889-1977) grandit dans la misère à Londres, joue très jeune sur les scènes de music-hall et part aux États-Unis en 1913. Il crée **the Tramp** (Charlot en France), un vagabond au chapeau melon, à la canne, au pantalon trop large et aux chaussures trop grandes, pauvre mais digne et rêveur. Dans *The Gold Rush* (1925), affamé, il fait cuire et mange sa chaussure comme un festin. Ses gags font rire, mais parlent aussi de la pauvreté, du travail à la chaîne (*Modern Times*, 1936) ou de la dictature : dans *The Great Dictator* (1940), il ridiculise Hitler.

## Buster Keaton, Laurel et Hardy
**Buster Keaton**, « l'homme qui ne rit jamais », reste impassible au milieu des catastrophes et réalise lui-même des cascades spectaculaires : dans un film de 1928, une façade de maison s'écroule sur lui et il passe pile par l'ouverture d'une fenêtre. **Laurel et Hardy**, le maigre Anglais Stan Laurel et le gros Américain Oliver Hardy, forment le premier grand duo comique : dans *The Music Box* (1932), ils tentent de monter un piano en haut d'un immense escalier.

## Mr Bean et les héritiers
En 1990, **Rowan Atkinson** crée **Mr Bean**, un homme-enfant presque muet, maladroit et égoïste, qui transforme chaque situation banale (faire ses courses, aller chez le dentiste) en désastre. Comme les films muets, la série n'a presque pas de dialogues : elle a été vendue dans plus de 200 pays. Les studios Aardman de Bristol, avec *Wallace & Gromit*, et de nombreux dessins animés perpétuent ce comique visuel.

## La mécanique du gag
Un bon gag obéit à des règles précises :
- le **timing** : l'effet arrive au bon moment, ni trop tôt ni trop tard ;
- la **surprise** : on attend une chose, il en arrive une autre ;
- l'**exaggeration** : tout est plus grand, plus fort, plus absurde ;
- la **rule of three** : une action se répète deux fois normalement, la troisième fois tout dérape ;
- le **deadpan** : rester totalement sérieux face à l'absurde ;
- le **double take** : un personnage regarde, ne réagit pas, puis comprend et regarde à nouveau, stupéfait ;
- les grands classiques : la peau de banane, la tarte à la crème, la porte qui se referme au mauvais moment.
Le rire naît souvent d'un décalage entre ce qui devrait se passer et ce qui se passe vraiment.
[→ Voir aussi : l'humour britannique](cu_humour.html)
""", """
a joke = une blague
a gag = un gag
to laugh = rire
funny = drôle
to fall = tomber
a banana skin = une peau de banane
a hat = un chapeau
a silent film = un film muet
""", [
 ("Qu'est-ce que le slapstick ?", ["Un comique physique fait de chutes et de catastrophes", "Un discours politique", "Une chanson"], ""),
 ("Pourquoi le cinéma muet est-il compris partout ?", ["Il n'a pas besoin de paroles", "Il est traduit en 50 langues", "Il est très court"], ""),
 ("Qui est the Tramp ?", ["Le vagabond de Chaplin, pauvre mais digne", "Un président", "Un super-héros"], ""),
 ("Que fait Chaplin dans The Great Dictator ?", ["Il ridiculise Hitler", "Il joue un roi", "Il chante"], ""),
 ("Pourquoi Mr Bean a-t-il été vendu dans plus de 200 pays ?", ["La série n'a presque pas de dialogues", "Elle est en français", "Elle est très longue"], ""),
 ("Qu'est-ce que la « rule of three » ?", ["Une action se répète deux fois normalement, la troisième dérape", "Trois acteurs obligatoires", "Trois minutes par gag"], ""),
], [("**Rowan Atkinson**", "acteur britannique né en 1955"), ("Aardman", "studio d'animation en pâte à modeler de Bristol")])
D = "gg"
culture(F, "Culture : The art of the gag", 'The art <span>of the gag</span>',
  "Culture · Chaplin, Keaton, Laurel et Hardy, Mr Bean", ("#fde68a", "#111827"),
  reperes("Du cinéma muet à Mr Bean, le comique visuel anglophone fait rire le monde entier grâce à une mécanique précise.",
    [("1914", "première apparition du Tramp de Chaplin"), ("1925", "The Gold Rush"), ("1932", "The Music Box de Laurel et Hardy"),
     ("1936", "Modern Times"), ("1940", "The Great Dictator"), ("1990", "Mr Bean")],
    "slapstick, a gag, timing, a silent film, a comedian, deadpan, a double take, exaggeration"),
  {D: doc("Make them laugh", [
    "Slapstick is physical comedy: people fall, run, get hit by pies and slip on banana skins. It was very popular in silent films, because everybody in the world could understand it.",
    "Charlie Chaplin was born in London. His famous character, the Tramp, is a poor man with a bowler hat, a cane and very big shoes. In one film, he is so hungry that he eats his shoe!",
    "Buster Keaton never smiled, even in the craziest situations. Laurel and Hardy were a famous duo: one was thin and one was fat.",
    "In 1990, Rowan Atkinson created Mr Bean, a clumsy man who almost never speaks. The series was sold in more than 200 countries.",
    "A good gag needs perfect timing and a surprise: you expect one thing, and something else happens."])},
  [TF(D, "Slapstick is a kind of physical comedy.", True, "« Slapstick is physical comedy »."),
   TF(D, "Silent films were difficult to understand abroad.", False, "« everybody in the world could understand it »."),
   TF(D, "Charlie Chaplin was born in New York.", False, "« born in London »."),
   TF(D, "Buster Keaton never smiled.", True, "« never smiled »."),
   TF(D, "Mr Bean talks a lot.", False, "« almost never speaks »."),
   TF(D, "A good gag needs a surprise.", True, "« perfect timing and a surprise »." )],
  [Q(D, "Why was slapstick popular in silent films?", ["Everybody could understand it.", "It was cheap.", "It had music."]),
   Q(D, "What does the Tramp wear?", ["A bowler hat, a cane and big shoes.", "A crown.", "A superhero costume."]),
   Q(D, "Who are Laurel and Hardy?", ["A famous comic duo.", "Two presidents.", "Two singers."]),
   Q(D, "What does a good gag need?", ["Perfect timing and a surprise.", "A lot of dialogue.", "Sad music."])],
  [DT(D, "Comment appelle-t-on le Tramp de Chaplin en France ?", ["Charlot", "Monsieur Hulot", "Fantômas", "Bécassine"]),
   DT(D, "Qui est « l'homme qui ne rit jamais » ?", ["Buster Keaton", "Charlie Chaplin", "Stan Laurel", "Rowan Atkinson"]),
   DT(D, "Que transportent Laurel et Hardy dans un escalier ?", ["Un piano", "Un frigo", "Une voiture", "Un lit"]),
   DT(D, "Comment dit-on « maladroit » ?", ["Clumsy", "Crazy", "Clever", "Clean"])],
  [W(D, "Trouve le mot qui veut dire « glissent ».", "slip"), W(D, "Trouve le mot qui veut dire « affamé ».", "hungry"),
   W(D, "Trouve le mot qui veut dire « maigre ».", "thin"), W(D, "Trouve le mot qui veut dire « s'attendre à ».", "expect")])

# ═════════ SPORTS COMMONWEALTH ═════════
F = "cu_sports_commonwealth.html"
DZ(F, """
## Des sports nés dans l'Empire
Le Royaume-Uni a codifié au 19e siècle de nombreux sports modernes et les a diffusés dans son Empire. Aujourd'hui encore, les pays du **Commonwealth** partagent ces passions sportives et se retrouvent tous les quatre ans aux **Commonwealth Games**, créés en 1930 au Canada ; Glasgow les a accueillis en 2026.

## Le cricket, du Royaume-Uni à l'Inde
Né en Angleterre, le **cricket** a ses règles écrites depuis 1788 par le Marylebone Cricket Club, au stade de **Lord's**, à Londres. Deux équipes de onze joueurs s'affrontent : un **bowler** lance la balle vers un guichet (**wicket**), un **batsman** la frappe avec une batte plate et court entre les guichets pour marquer des points (**runs**). Un **Test match** peut durer jusqu'à cinq jours, avec une pause pour le thé ! Des formats plus courts sont apparus, comme le **Twenty20** (environ trois heures). Le cricket est aujourd'hui une religion en **Inde**, au Pakistan, au Bangladesh, au Sri Lanka, en Australie, en Afrique du Sud et dans les Caraïbes. La ligue indienne, l'IPL, créée en 2008, est l'une des compétitions les plus riches du monde. Depuis 1882, l'Angleterre et l'Australie se disputent **The Ashes**, une minuscule urne censée contenir les cendres d'un guichet. En anglais, « *it's not cricket* » signifie « ce n'est pas loyal ».

## Le hockey sur glace, passion canadienne
Au Canada, le **ice hockey** est officiellement le sport national d'hiver. Le premier match organisé en salle a lieu à Montréal en 1875. Le gouverneur général Lord Stanley offre en 1892 une coupe devenue le trophée le plus célèbre du sport nord-américain : la **Stanley Cup**, remise chaque année au champion de la NHL, la ligue professionnelle que se partagent clubs canadiens et américains. Le samedi soir, des millions de familles regardent *Hockey Night in Canada*, une émission diffusée depuis les débuts de la radio. On patine sur les lacs gelés, les patinoires de quartier et même dans les jardins. Wayne Gretzky, « *The Great One* », est considéré comme le plus grand joueur de tous les temps, et la rivalité Canada–États-Unis, chez les hommes comme chez les femmes, est intense.

## L'Aussie Rules, le football australien
L'**Australian rules football** est né à **Melbourne** en 1859. Il se joue sur un immense terrain ovale (souvent un terrain de cricket), avec un ballon ovale, entre deux équipes de 18 joueurs. On peut taper le ballon au pied et le passer en le frappant du poing, mais pas le lancer. Les joueurs s'envolent spectaculairement pour attraper le ballon (le **mark**). Un but entre les deux poteaux centraux vaut 6 points. La finale de la ligue professionnelle, l'**AFL Grand Final**, réunit environ 100 000 spectateurs au Melbourne Cricket Ground. Ce sport incarne des valeurs australiennes : endurance, esprit d'équipe, dureté et convivialité. De nombreux joueurs aborigènes en sont des stars, et une ligue féminine existe depuis 2017.

## Et aussi…
Le **rugby** relie aussi le Royaume-Uni, l'Irlande, l'Afrique du Sud, l'Australie et la Nouvelle-Zélande, dont l'équipe, les **All Blacks**, exécute le **haka** māori avant chaque match.
[→ Voir aussi : le sport britannique](cu_sport_uk.html)
""", """
a team = une équipe
a player = un joueur
a ball = une balle, un ballon
a bat = une batte
ice = la glace
to skate = patiner
a cup = une coupe
a match = un match
""", [
 ("Quand se tiennent les Commonwealth Games ?", ["Tous les quatre ans", "Chaque année", "Tous les dix ans"], ""),
 ("Combien de temps peut durer un Test match de cricket ?", ["Jusqu'à cinq jours", "90 minutes", "Une heure"], ""),
 ("Que signifie « it's not cricket » ?", ["Ce n'est pas loyal", "C'est ennuyeux", "Il pleut"], ""),
 ("Qu'est-ce que la Stanley Cup ?", ["Le trophée du champion de hockey de la NHL", "Une tasse de thé", "Un prix de cricket"], ""),
 ("Où est né l'Aussie Rules ?", ["À Melbourne", "À Londres", "À Montréal"], ""),
 ("Quelles valeurs incarne l'Aussie Rules ?", ["Endurance, esprit d'équipe, dureté et convivialité", "Individualisme", "Paresse"], ""),
], [("Lord's", "stade de cricket de Londres"), ("Wayne Gretzky", "hockeyeur canadien, né en 1961")])
D = "sc"
culture(F, "Culture : Commonwealth sports", 'Commonwealth <span>sports</span>',
  "Culture · cricket, hockey sur glace et football australien", ("#86efac", "#1e40af"),
  reperes("Le cricket, le hockey sur glace au Canada et l'Aussie Rules en Australie montrent comment le sport façonne l'identité des pays du Commonwealth.",
    [("1788", "règles du cricket écrites à Lord's"), ("1859", "naissance de l'Aussie Rules à Melbourne"), ("1875", "premier match de hockey en salle à Montréal"),
     ("1882", "début de la rivalité des Ashes"), ("1892", "création de la Stanley Cup"), ("1930", "premiers Commonwealth Games")],
    "a team, a player, a pitch, a bat, a wicket, a rink, a trophy, a rivalry"),
  {D: doc("Bats, sticks and footballs", [
    "Many sports were invented or organised in Britain and spread across the British Empire. Today, Commonwealth countries meet every four years at the Commonwealth Games.",
    "Cricket is very popular in England, India, Pakistan, Australia and the Caribbean. A Test match can last five days, and players stop for a tea break!",
    "In Canada, ice hockey is the national winter sport. Children learn to skate on frozen lakes. The best professional team wins the Stanley Cup.",
    "In Australia, the most popular sport is Australian rules football, born in Melbourne in 1859. Teams of 18 players play on a huge oval field.",
    "These sports are a big part of national identity, and the rivalries between countries are very strong."])},
  [TF(D, "Commonwealth countries meet every four years.", True, "« every four years »."),
   TF(D, "Cricket is not popular in India.", False, "Il est très populaire en Inde."),
   TF(D, "A Test match can last five days.", True, "« can last five days »."),
   TF(D, "Ice hockey is the national summer sport of Canada.", False, "« the national winter sport »."),
   TF(D, "Australian rules football was born in Melbourne.", True, "« born in Melbourne in 1859 »."),
   TF(D, "Aussie Rules teams have 11 players.", False, "« Teams of 18 players »." )],
  [Q(D, "Where is cricket popular?", ["In England, India, Pakistan, Australia and the Caribbean.", "Only in France.", "In Canada only."]),
   Q(D, "What do cricket players do during a Test match?", ["They stop for a tea break.", "They skate.", "They sing."]),
   Q(D, "Where do Canadian children learn to skate?", ["On frozen lakes.", "On the beach.", "In the desert."]),
   Q(D, "What is the shape of an Aussie Rules field?", ["Oval.", "Square.", "Triangular."])],
  [DT(D, "Quel trophée se disputent l'Angleterre et l'Australie au cricket ?", ["The Ashes", "The Stanley Cup", "The Webb Ellis Cup", "The Grand Final"]),
   DT(D, "Qui est surnommé « The Great One » ?", ["Wayne Gretzky", "Sachin Tendulkar", "Don Bradman", "Jonah Lomu"]),
   DT(D, "Quelle danse les All Blacks font-ils avant leurs matchs ?", ["Le haka", "La gigue", "Le Charleston", "La samba"]),
   DT(D, "Comment dit-on « une patinoire » ?", ["A rink", "A ring", "An ice park", "A skate field"])],
  [W(D, "Trouve le mot qui veut dire « se sont répandus ».", "spread"), W(D, "Trouve le mot qui veut dire « une pause thé » (2 mots).", ["tea break", "a tea break"]),
   W(D, "Trouve le mot qui veut dire « gelés ».", "frozen"), W(D, "Trouve le mot qui veut dire « les rivalités ».", "rivalries")])

# ═════════ VILLES MODÈLES ═════════
F = "cu_villes_modeles.html"
DZ(F, """
## Bournville, le village du chocolat
En 1879, les frères **George et Richard Cadbury**, chocolatiers de Birmingham et membres de la communauté religieuse des **quakers**, installent leur usine à la campagne, au sud de la ville. Ils y construisent un village pour leurs ouvriers : **Bournville**. Contrairement aux taudis industriels de l'époque, les maisons y ont des jardins, l'air est sain, il y a des parcs, des terrains de sport, des écoles. Fidèles à leurs principes, les Cadbury n'y autorisent aucun pub : aujourd'hui encore, il n'y en a pas. D'autres industriels ont créé des « villages modèles » semblables, comme Saltaire (laine) ou Port Sunlight (savon).
Le jeune **Roald Dahl**, élève dans un pensionnat, faisait partie des écoliers chargés de tester les nouveaux chocolats Cadbury. Il rêvait de travailler dans un laboratoire secret de chocolatier : ce souvenir a inspiré *Charlie and the Chocolate Factory* (1964). Le réel nourrit ici l'imaginaire.

## Les cités-jardins
En 1898, l'urbaniste Ebenezer Howard imagine les **garden cities**, des villes de taille moyenne qui combinent les avantages de la ville (emplois, culture) et de la campagne (nature, air pur), entourées d'une ceinture verte. Letchworth, créée en 1903, est la première. Ce modèle a inspiré des urbanistes du monde entier.

## Melbourne, « the Garden City »
En Australie, **Melbourne**, capitale de l'État de Victoria, se surnomme la ville-jardin. Elle est célèbre pour ses immenses parcs, comme ses jardins botaniques royaux créés en 1846, ses tramways, ses ruelles couvertes de street art, ses cafés et sa passion pour le sport. Elle a souvent été classée parmi les villes les plus agréables à vivre du monde (**most liveable city**). Pour lutter contre la chaleur, elle mène une politique de plantation d'arbres et a même donné une adresse e-mail à ses arbres… et les habitants leur ont écrit des messages d'amour !

## Poundbury, une ville nouvelle à l'ancienne
Dans le **Dorset**, sur des terres appartenant au duché de Cornouailles, le prince Charles, aujourd'hui roi, fait construire à partir de 1993 **Poundbury**, une extension de la ville de Dorchester. Inspirée par l'urbanisme traditionnel, elle mêle logements, commerces et entreprises, avec des rues pensées pour les piétons plutôt que pour les voitures. Ses admirateurs y voient un quartier humain et durable ; ses critiques la trouvent artificielle, comme un décor de film qui imite le passé.

## Les gated communities, une nouvelle ségrégation ?
Aux États-Unis, des millions de personnes vivent dans des **gated communities**, des quartiers résidentiels entourés de murs ou de grilles, avec une entrée contrôlée par des gardiens, et des règles strictes fixées par une association de propriétaires. On y cherche la sécurité, la tranquillité et un entre-soi. Mais beaucoup y voient une forme de **ségrégation** sociale, voire raciale : ceux qui en ont les moyens se coupent du reste de la ville. En 2012, la mort de Trayvon Martin, tué dans une gated community de Floride, a nourri ce débat.
[→ Voir aussi : villes et États américains](cu_villes_etats.html)
""", """
a village = un village
a factory = une usine
chocolate = le chocolat
a garden = un jardin
a park = un parc
a street = une rue
a gate = un portail
a neighbour = un voisin
""", [
 ("Pourquoi les Cadbury construisent-ils Bournville ?", ["Pour offrir à leurs ouvriers un village sain avec jardins et parcs", "Pour fabriquer des voitures", "Pour accueillir des touristes"], ""),
 ("Pourquoi n'y a-t-il pas de pub à Bournville ?", ["Les Cadbury, quakers, l'interdisaient", "Personne ne boit de bière", "C'est trop cher"], ""),
 ("Quel lien entre Bournville et Roald Dahl ?", ["Il testait les chocolats Cadbury enfant, ce qui a inspiré Charlie", "Il y est né", "Il y a construit une école"], ""),
 ("Qu'est-ce qu'une garden city ?", ["Une ville qui combine les avantages de la ville et de la campagne", "Un grand jardin public", "Un centre commercial"], ""),
 ("Que reprochent les critiques à Poundbury ?", ["D'être artificielle et d'imiter le passé", "D'être trop moderne", "D'être trop grande"], ""),
 ("Pourquoi les gated communities font-elles débat ?", ["On y voit une forme de ségrégation sociale", "Elles sont trop ouvertes", "Elles n'ont pas de maisons"], ""),
], [("quakers", "mouvement protestant attaché à la simplicité et à la paix"), ("Ebenezer Howard", "urbaniste britannique, 1850-1928")])
D = "vm"
culture(F, "Culture : Model villages and cities", 'Model <span>towns</span>',
  "Culture · Bournville, Melbourne, Poundbury et les gated communities", ("#d6d3d1", "#166534"),
  reperes("Des villages ouvriers aux quartiers fermés, les villes anglophones montrent différentes façons de vivre ensemble… ou séparés.",
    [("1879", "l'usine Cadbury s'installe à Bournville"), ("1898", "l'idée des cités-jardins"), ("1903", "Letchworth, première cité-jardin"),
     ("1964", "Charlie and the Chocolate Factory"), ("1993", "début de la construction de Poundbury")],
    "a model village, a garden city, a neighbourhood, a park, a pedestrian street, a gated community, segregation, liveable"),
  {D: doc("Living together", [
    "In 1879, the Cadbury brothers moved their chocolate factory to the countryside near Birmingham. They built a village for their workers, Bournville, with gardens, parks and schools, but no pubs!",
    "As a schoolboy, Roald Dahl tested new Cadbury chocolates. This memory inspired Charlie and the Chocolate Factory.",
    "Melbourne, in Australia, is called the Garden City because of its many parks. It is often ranked as one of the most liveable cities in the world.",
    "In England, King Charles created Poundbury, a new town that looks old. Some people love it, others think it is artificial.",
    "In the USA, many people live in gated communities, with walls and guards. They feel safe, but critics say these places separate rich and poor people."])},
  [TF(D, "The Cadbury factory moved to the countryside.", True, "« to the countryside »."),
   TF(D, "Bournville has many pubs.", False, "« but no pubs! »."),
   TF(D, "Roald Dahl tested Cadbury chocolates.", True, "« tested new Cadbury chocolates »."),
   TF(D, "Melbourne is called the Garden City.", True, "« called the Garden City »."),
   TF(D, "Everybody loves Poundbury.", False, "« others think it is artificial »."),
   TF(D, "Gated communities have no walls.", False, "« with walls and guards »." )],
  [Q(D, "What did the Cadbury brothers build?", ["A village for their workers.", "A castle.", "A stadium."]),
   Q(D, "What inspired Charlie and the Chocolate Factory?", ["Dahl's memory of testing chocolates.", "A trip to Belgium.", "A film."]),
   Q(D, "Why is Melbourne called the Garden City?", ["Because of its many parks.", "Because it sells flowers.", "Because it is small."]),
   Q(D, "What do critics say about gated communities?", ["They separate rich and poor people.", "They are too cheap.", "They are not safe."])],
  [DT(D, "Dans quelle région se trouve Poundbury ?", ["Le Dorset", "Le Yorkshire", "Le Kent", "Les Cornouailles"]),
   DT(D, "Quelle est la première cité-jardin ?", ["Letchworth", "Bournville", "Poundbury", "Milton Keynes"]),
   DT(D, "Près de quelle ville se trouve Bournville ?", ["Birmingham", "Londres", "Manchester", "Bristol"]),
   DT(D, "Comment dit-on « un piéton » ?", ["A pedestrian", "A walker-man", "A footman", "A pedal"])],
  [W(D, "Trouve le mot qui veut dire « la campagne ».", "countryside"), W(D, "Trouve le mot qui veut dire « un souvenir ».", ["memory", "This memory"]),
   W(D, "Trouve le mot qui veut dire « artificielle ».", "artificial"), W(D, "Trouve le mot qui veut dire « séparent ».", "separate")])

# ═════════ IRLANDE : WILD ATLANTIC WAY ═════════
F = "cu_irlande_atlantique.html"
DZ(F, """
## The Wild Atlantic Way
Lancée en 2014, la **Wild Atlantic Way** est l'une des plus longues routes touristiques côtières du monde : environ 2 500 kilomètres le long de la côte ouest de l'Irlande, de la péninsule d'Inishowen, au nord, jusqu'à Kinsale, au sud. Elle traverse des paysages spectaculaires :
- les **Cliffs of Moher**, falaises qui plongent de plus de 200 mètres dans l'Atlantique ;
- **Skellig Michael**, un rocher escarpé où des moines vivaient dès le 6e siècle, devenu célèbre grâce au film *Star Wars* ;
- le **Connemara** et ses tourbières, les îles d'Aran et leurs murets de pierre, la ville festive de **Galway** ;
- des plages où l'on surfe parmi les plus grosses vagues d'Europe.
Le long de cette côte se trouvent aussi des **Gaeltacht**, des régions où l'on parle encore l'**irlandais** (le gaélique) au quotidien. La route inspire photographes, musiciens et écrivains, et a fortement développé le tourisme dans des régions rurales longtemps pauvres.

## Céad míle fáilte : une terre d'accueil
« *Céad míle fáilte* », « cent mille fois bienvenue » : l'hospitalité irlandaise est légendaire. Pendant des siècles pourtant, l'Irlande a été une terre d'**émigration** : après la Grande Famine, des millions d'Irlandais sont partis pour les États-Unis, le Royaume-Uni ou l'Australie. Depuis les années 1990, la tendance s'est inversée : avec la croissance économique du « **Celtic Tiger** », le pays attire des immigrants. Aujourd'hui, environ un habitant sur cinq est né à l'étranger : Polonais, Brésiliens, Indiens, et, depuis 2022, des dizaines de milliers de réfugiés ukrainiens. Cette transformation rapide pose aussi des défis : crise du logement, tensions et manifestations, notamment à Dublin en 2023.

## L'Irlande sur la scène européenne
L'Irlande, indépendante depuis 1922, entre dans la Communauté économique européenne en **1973**, en même temps que le Royaume-Uni et le Danemark. L'Europe finance routes, ports et universités, et l'agriculture irlandaise bénéficie de la politique agricole commune. Le pays adopte l'**euro** et attire les sièges européens de géants de la technologie, comme Google, Apple ou Meta, grâce à une fiscalité avantageuse, qui suscite des critiques de ses partenaires européens. Contrairement au Royaume-Uni, les Irlandais restent très attachés à l'Union européenne : après le **Brexit**, l'Irlande est le principal pays anglophone de l'UE, et la question de la frontière avec l'Irlande du Nord a été au cœur des négociations. En 2026, l'Irlande assure pour la huitième fois la présidence tournante du Conseil de l'Union européenne.

## Traditions et modernité
L'Irlande d'aujourd'hui est à la fois très moderne et attachée à ses traditions : la musique traditionnelle dans les pubs (les **sessions**), les sports gaéliques (football gaélique et **hurling**), la danse irlandaise popularisée par *Riverdance*, la langue irlandaise enseignée à l'école. En quelques décennies, la société a aussi beaucoup changé : en 2015, l'Irlande est devenue le premier pays au monde à légaliser le mariage homosexuel par référendum.
[→ Voir aussi : l'Irlande aujourd'hui](cu_irlande_auj.html)
""", """
a cliff = une falaise
the coast = la côte
a wave = une vague
an island = une île
a road = une route
welcome = bienvenue
a tradition = une tradition
Europe = l'Europe
""", [
 ("Qu'est-ce que la Wild Atlantic Way ?", ["Une route touristique de 2 500 km le long de la côte ouest", "Une autoroute vers Dublin", "Un bateau"], ""),
 ("Qu'est-ce qu'une Gaeltacht ?", ["Une région où l'on parle encore l'irlandais", "Un pub", "Une falaise"], ""),
 ("Que signifie « Céad míle fáilte » ?", ["Cent mille fois bienvenue", "Bonne nuit", "Au revoir"], ""),
 ("Comment l'Irlande a-t-elle changé depuis les années 1990 ?", ["De terre d'émigration, elle est devenue terre d'immigration", "Elle a quitté l'Europe", "Elle est devenue britannique"], ""),
 ("Quand l'Irlande entre-t-elle dans l'Europe ?", ["En 1973", "En 1922", "En 2016"], ""),
 ("Que s'est-il passé en 2015 ?", ["L'Irlande a légalisé le mariage homosexuel par référendum", "L'Irlande a quitté l'UE", "La Wild Atlantic Way a fermé"], ""),
], [("**Skellig Michael**", "rocher monastique classé à l'UNESCO"), ("Celtic Tiger", "période de forte croissance, 1995-2007"), ("*Riverdance*", "spectacle de danse irlandaise de 1994")])
D = "ia"
culture(F, "Culture : Ireland – the Wild Atlantic Way and Europe", 'The Wild <span>Atlantic Way</span>',
  "Culture · Irlande : côte sauvage, terre d'accueil et Europe", ("#86efac", "#0e7490"),
  reperes("La Wild Atlantic Way longe la côte ouest de l'Irlande. Le pays, autrefois terre d'émigration, est devenu une terre d'accueil très attachée à l'Europe.",
    [("1922", "indépendance de l'État libre d'Irlande"), ("1973", "entrée dans la Communauté européenne"), ("1995 – 2007", "le Celtic Tiger"),
     ("2014", "lancement de la Wild Atlantic Way"), ("2015", "référendum sur le mariage pour tous"), ("2026", "présidence irlandaise de l'Union européenne")],
    "a coastal route, a cliff, a wave, hospitality, emigration, immigration, the European Union, tradition"),
  {D: doc("Wild and welcoming", [
    "The Wild Atlantic Way is a tourist route along the west coast of Ireland. It is about 2,500 kilometres long. You can see huge cliffs, small islands and beautiful beaches.",
    "In some villages on this coast, people still speak Irish every day. The music in the pubs and the traditional sports are very popular.",
    "For a long time, millions of Irish people emigrated to America and Britain. But since the 1990s, Ireland has become rich, and many immigrants have come to live there.",
    "Ireland joined the European Community in 1973, and it uses the euro. Unlike the UK, Ireland did not want to leave the European Union.",
    "Today, Ireland is a modern country that is proud of its traditions."])},
  [TF(D, "The Wild Atlantic Way is on the east coast of Ireland.", False, "« the west coast »."),
   TF(D, "Some people on this coast still speak Irish.", True, "« still speak Irish every day »."),
   TF(D, "Millions of Irish people emigrated in the past.", True, "« millions of Irish people emigrated »."),
   TF(D, "Ireland has always been a poor country.", False, "« Ireland has become rich »."),
   TF(D, "Ireland joined the European Community in 1973.", True, "« in 1973 »."),
   TF(D, "Ireland left the European Union with the UK.", False, "« Ireland did not want to leave »." )],
  [Q(D, "What can you see on the Wild Atlantic Way?", ["Huge cliffs, small islands and beaches.", "Skyscrapers.", "Deserts."]),
   Q(D, "Where did Irish people emigrate in the past?", ["To America and Britain.", "To China.", "To Antarctica."]),
   Q(D, "What happened since the 1990s?", ["Ireland became rich and immigrants came.", "Ireland became poor.", "Ireland left Europe."]),
   Q(D, "What currency does Ireland use?", ["The euro.", "The pound.", "The dollar."])],
  [DT(D, "Quelles falaises célèbres longe la route ?", ["Les Cliffs of Moher", "Les White Cliffs of Dover", "Les Seven Sisters", "Les falaises d'Étretat"]),
   DT(D, "Quel film a rendu Skellig Michael célèbre ?", ["Star Wars", "Harry Potter", "Titanic", "Braveheart"]),
   DT(D, "Quel sport gaélique se joue avec une crosse ?", ["Le hurling", "Le cricket", "Le curling", "Le polo"]),
   DT(D, "Comment dit-on « émigrer » ?", ["To emigrate", "To immigrate", "To migrate in", "To exile"])],
  [W(D, "Trouve le mot qui veut dire « falaises ».", "cliffs"), W(D, "Trouve le mot qui veut dire « ont émigré ».", "emigrated"),
   W(D, "Trouve le mot qui veut dire « contrairement au » (1 mot).", ["Unlike", "unlike"]), W(D, "Trouve le mot qui veut dire « fier ».", "proud")])

# ═════════ ANIMAUX & JOURNAUX ═════════
F = "cu_animaux_journaux.html"
DZ(F, """
## Des animaux qui nous font la leçon
Depuis les fables d'Ésope, traduites en anglais dès 1484, les animaux servent à raconter des histoires qui enseignent une morale. La littérature anglophone en a fait une spécialité.
- **Peter Rabbit** (1902), de **Beatrix Potter** : un petit lapin désobéissant se faufile dans le potager de Mr McGregor, manque de se faire attraper et perd ses vêtements. Leçon : il faut écouter ses parents !
- **The Jungle Book** (1894), de **Rudyard Kipling** : Mowgli, petit d'homme élevé par les loups en Inde, apprend la « loi de la jungle » avec l'ours Baloo et la panthère Bagheera, face au tigre Shere Khan.
- **Black Beauty** (1877), d'Anna Sewell, raconté par un cheval lui-même, dénonce la cruauté envers les animaux et a fait progresser leur protection.
- **Charlotte's Web** (1952), de l'Américain E. B. White : une araignée, Charlotte, sauve le cochon Wilbur de l'abattoir en tissant des mots élogieux dans sa toile. Une histoire d'amitié, de mort et de transmission.
- **Paddington** (1958), de Michael Bond : un petit ours venu du Pérou, avec une étiquette autour du cou demandant de prendre soin de lui, est accueilli par une famille londonienne. L'auteur s'était inspiré des enfants évacués pendant la guerre. Paddington est devenu un symbole de l'accueil et de la politesse.
- *Animal Farm* d'Orwell utilise aussi des animaux, mais pour une fable politique destinée aux adultes.

## Le journal de bord et le journal intime
Écrire chaque jour ce que l'on vit est une vieille tradition anglaise.
- **Samuel Pepys**, haut fonctionnaire londonien, tient de 1660 à 1669 un journal en écriture codée. Il y raconte la grande peste de 1665 et le **Grand Incendie de Londres** de 1666 : il enterre même son fromage parmesan dans son jardin pour le protéger des flammes ! Son journal est un trésor pour les historiens.
- Les **logbooks**, journaux de bord des navires, comme ceux de James Cook, racontaient chaque jour la météo, la route et les événements.
- **Le journal d'Anne Frank**, écrit en néerlandais, est l'un des livres les plus lus au monde en anglais.
- **The Secret Diary of Adrian Mole, Aged 13¾** (1982), de Sue Townsend, est le journal hilarant d'un adolescent anglais persuadé d'être un génie incompris.
- **Diary of a Wimpy Kid** (2007), de l'Américain Jeff Kinney, mélange texte et dessins : Greg Heffley raconte ses malheurs au collège… en précisant que c'est un *journal*, pas un *diary* !

## Pourquoi écrire un journal ?
Pour se souvenir, pour réfléchir, pour exprimer ce qu'on n'ose pas dire, ou simplement pour rire de soi. Aujourd'hui, les **blogs**, les **vlogs** et les stories des réseaux sociaux sont des formes modernes du journal… mais publiques, alors que le *diary* était secret.
[→ Voir aussi : la littérature jeunesse](cu_litterature_jeunesse.html)
""", """
an animal = un animal
a rabbit = un lapin
a bear = un ours
a spider = une araignée
a pig = un cochon
a diary = un journal intime
a secret = un secret
a lesson = une leçon
""", [
 ("À quoi servent les animaux dans les fables ?", ["À enseigner une morale", "À faire peur", "À rien"], ""),
 ("Qui élève Mowgli ?", ["Des loups", "Des lapins", "Des ours polaires"], ""),
 ("Comment Charlotte sauve-t-elle Wilbur ?", ["En tissant des mots élogieux dans sa toile", "En le cachant", "En appelant la police"], ""),
 ("D'où vient Paddington ?", ["Du Pérou", "D'Australie", "Du Canada"], ""),
 ("Que raconte Samuel Pepys dans son journal ?", ["La grande peste et le Grand Incendie de Londres", "La conquête de l'espace", "Sa vie à New York"], ""),
 ("Quelle est la différence entre un diary et les stories ?", ["Le diary était secret, les stories sont publiques", "Il n'y en a aucune", "Les stories sont écrites à la main"], ""),
], [("Ésope", "fabuliste de la Grèce antique"), ("**Rudyard Kipling**", "écrivain britannique né en Inde, prix Nobel 1907"), ("**Samuel Pepys**", "administrateur de la marine anglaise, 1633-1703")])
D = "aj"
culture(F, "Culture : Animal stories and diaries", 'Animals <span>&amp; diaries</span>',
  "Culture · Peter Rabbit, Paddington, Pepys et Adrian Mole", ("#fde68a", "#166534"),
  reperes("Les animaux qui parlent et les journaux intimes sont deux grandes traditions de la littérature anglophone.",
    [("1666", "Pepys raconte le Grand Incendie de Londres"), ("1894", "The Jungle Book"), ("1902", "Peter Rabbit"),
     ("1952", "Charlotte's Web"), ("1958", "Paddington"), ("1982", "Adrian Mole"), ("2007", "Diary of a Wimpy Kid")],
    "a fable, a moral, a character, a diary, a logbook, to keep a diary, a secret, a lesson"),
  {D: doc("Dear Diary...", [
    "Many English stories use animals to teach a lesson. Peter Rabbit does not listen to his mother and goes into Mr McGregor's garden. He nearly gets caught!",
    "In Charlotte's Web, a clever spider saves her friend, a pig called Wilbur. Paddington is a little bear from Peru who arrives in London with a label around his neck.",
    "People have also kept diaries for centuries. In the 17th century, Samuel Pepys wrote about the Great Fire of London. He buried his cheese in the garden to save it!",
    "Adrian Mole and Greg Heffley, from Diary of a Wimpy Kid, are two funny teenagers who write about their problems at school.",
    "Today, blogs and social media stories are a modern kind of diary, but they are public, not secret."])},
  [TF(D, "Peter Rabbit always listens to his mother.", False, "« does not listen to his mother »."),
   TF(D, "Charlotte is a spider.", True, "« a clever spider »."),
   TF(D, "Paddington comes from Peru.", True, "« a little bear from Peru »."),
   TF(D, "Samuel Pepys wrote about the Great Fire of London.", True, "« about the Great Fire of London »."),
   TF(D, "Pepys buried his money in the garden.", False, "« He buried his cheese »."),
   TF(D, "Social media stories are secret.", False, "« they are public, not secret »." )],
  [Q(D, "Why do stories use animals?", ["To teach a lesson.", "To sell books only.", "To scare children."]),
   Q(D, "Who is Wilbur?", ["A pig.", "A bear.", "A rabbit."]),
   Q(D, "What did Pepys bury?", ["His cheese.", "His books.", "His cat."]),
   Q(D, "What do Adrian Mole and Greg Heffley write about?", ["Their problems at school.", "Their travels in space.", "The war."])],
  [DT(D, "Qui a écrit The Jungle Book ?", ["Rudyard Kipling", "Beatrix Potter", "Roald Dahl", "Lewis Carroll"]),
   DT(D, "Quel âge a Adrian Mole dans le titre ?", ["13 ans et 3/4", "10 ans", "16 ans", "18 ans"]),
   DT(D, "Quel animal raconte Black Beauty ?", ["Un cheval", "Un chien", "Un chat", "Un loup"]),
   DT(D, "Comment dit-on « tenir un journal » ?", ["To keep a diary", "To hold a diary", "To make a diary", "To do a diary"])],
  [W(D, "Trouve le mot qui veut dire « se faire attraper » (2 mots).", ["gets caught", "get caught"]), W(D, "Trouve le mot qui veut dire « une étiquette ».", ["label", "a label"]),
   W(D, "Trouve le mot qui veut dire « a enterré ».", "buried"), W(D, "Trouve le mot qui veut dire « publiques ».", "public")])

# ═════════ MIGRATIONS & VAGABONDS ═════════
F = "cu_migrations_vagabonds.html"
DZ(F, """
## Partir pour l'Australie
Après la Seconde Guerre mondiale, l'Australie veut augmenter rapidement sa population : « *populate or perish* » (peupler ou périr), dit le ministre de l'Immigration en 1947. Le gouvernement paie presque entièrement le voyage des Britanniques qui acceptent d'émigrer : ils ne paient que dix livres. Entre 1945 et 1972, plus d'un million de ces « **Ten Pound Poms** » partent vers le soleil et l'espoir d'une vie meilleure ; certains, déçus par les camps d'accueil rudimentaires, rentrent au pays.
Pendant longtemps, l'Australie applique la **White Australia policy**, qui limite l'immigration non européenne. Elle n'est complètement abandonnée qu'en 1973. Depuis, le pays accueille des immigrants du monde entier : Grecs et Italiens d'abord, puis Vietnamiens, Chinois, Indiens… Aujourd'hui, près d'un Australien sur trois est né à l'étranger. La politique envers les demandeurs d'asile arrivés par bateau, retenus dans des centres situés sur des îles du Pacifique, reste très critiquée.

## Migrer à l'intérieur des États-Unis
Les Américains sont un peuple très mobile.
- Entre 1910 et 1970, environ six millions d'Afro-Américains quittent le Sud rural et ségrégationniste pour les villes industrielles du Nord et de l'Ouest : c'est la **Great Migration**.
- Dans les années 1930, les **Okies**, fermiers ruinés par le **Dust Bowl**, partent vers la Californie, comme la famille Joad de *The Grapes of Wrath* de Steinbeck.
- Aujourd'hui, beaucoup quittent les grandes villes chères du Nord-Est et de la Californie pour la **Sun Belt** : le Texas, la Floride, l'Arizona.

## Le vagabond, figure américaine
Après la guerre de Sécession, puis surtout pendant la Grande Dépression, des centaines de milliers d'hommes sans emploi, les **hobos**, voyagent clandestinement à bord des trains de marchandises à la recherche de petits boulots. Ils ont leur propre langage, et laissent à la craie des signes secrets pour prévenir les suivants (« ici, femme gentille », « chien méchant »). Le chanteur Woody Guthrie et l'écrivain Jack London, qui a lui-même été hobo, racontent cette vie.
Le vagabond devient un personnage littéraire et cinématographique : le **Tramp** de Chaplin, les voyageurs de la **Beat Generation**, Chris McCandless dans *Into the Wild*, qui abandonne tout pour vivre seul en Alaska, ou les retraités qui vivent dans leur camionnette après la crise de 2008 dans *Nomadland* (2020). Il incarne à la fois la liberté, le refus de la société de consommation, mais aussi la pauvreté et l'exclusion.
[→ Voir aussi : la Beat Generation et les générations](cu_generations.html)
""", """
a migrant = un migrant
a ship = un navire
a train = un train
a job = un emploi
freedom = la liberté
poverty = la pauvreté
a journey = un voyage
to move = déménager
""", [
 ("Qui sont les « Ten Pound Poms » ?", ["Des Britanniques qui émigraient en Australie pour dix livres", "Des joueurs de cricket", "Des fruits"], ""),
 ("Qu'était la White Australia policy ?", ["Une politique qui limitait l'immigration non européenne", "Une loi sur la neige", "Une fête"], ""),
 ("Qu'est-ce que la Great Migration ?", ["Le départ de millions d'Afro-Américains du Sud vers le Nord", "Une migration d'oiseaux", "La conquête de l'Ouest"], ""),
 ("Qui sont les hobos ?", ["Des travailleurs sans emploi voyageant clandestinement en train", "Des cow-boys", "Des chanteurs"], ""),
 ("À quoi servaient les signes à la craie des hobos ?", ["À prévenir les suivants (femme gentille, chien méchant)", "À décorer les trains", "À jouer"], ""),
 ("Que symbolise le vagabond ?", ["La liberté, mais aussi la pauvreté et l'exclusion", "La richesse", "Le pouvoir"], ""),
], [("Woody Guthrie", "chanteur folk américain, 1912-1967"), ("Jack London", "écrivain américain, auteur de Croc-Blanc")])
D = "mv"
culture(F, "Culture : Migrants and wanderers", 'Migrants <span>&amp; wanderers</span>',
  "Culture · les Ten Pound Poms, la Great Migration et les hobos", ("#fdba74", "#334155"),
  reperes("Émigrer en Australie, traverser les États-Unis, vivre sur la route : les pays anglophones sont marqués par les migrations et la figure du vagabond.",
    [("1910 – 1970", "la Great Migration des Afro-Américains"), ("années 1930", "les hobos et les Okies du Dust Bowl"), ("1945 – 1972", "les Ten Pound Poms partent en Australie"),
     ("1973", "fin de la White Australia policy"), ("2020", "le film Nomadland")],
    "a migrant, to emigrate, to settle, a hobo, a freight train, the road, freedom, poverty"),
  {D: doc("On the move", [
    "After the Second World War, Australia needed more people. British people could travel there for only ten pounds! More than a million of them went. They were called \"Ten Pound Poms\".",
    "Today, almost one Australian out of three was born in another country.",
    "Americans move a lot. Between 1910 and 1970, about six million African Americans left the South to live in the cities of the North.",
    "During the Great Depression, many poor men, called hobos, travelled secretly on freight trains to look for work.",
    "The wanderer is a famous character in American books and films. It is a symbol of freedom, but also of poverty."])},
  [TF(D, "British people could go to Australia for only ten pounds.", True, "« for only ten pounds »."),
   TF(D, "Very few British people went to Australia.", False, "« More than a million »."),
   TF(D, "Almost one Australian out of three was born abroad.", True, "« almost one Australian out of three »."),
   TF(D, "African Americans left the North to live in the South.", False, "Ils ont quitté le Sud pour le Nord."),
   TF(D, "Hobos travelled on freight trains.", True, "« on freight trains »."),
   TF(D, "The wanderer is only a symbol of wealth.", False, "« freedom, but also of poverty »." )],
  [Q(D, "Why did Australia want British immigrants?", ["It needed more people.", "It needed cricket players.", "It wanted to become British."]),
   Q(D, "Where did African Americans go during the Great Migration?", ["To the cities of the North.", "To Africa.", "To the South."]),
   Q(D, "What were hobos looking for?", ["Work.", "Gold.", "Holidays."]),
   Q(D, "What does the wanderer symbolise?", ["Freedom and poverty.", "Money and power.", "School."])],
  [DT(D, "Comment appelle-t-on les fermiers ruinés de l'Oklahoma ?", ["Les Okies", "Les hobos", "Les Poms", "Les Yankees"]),
   DT(D, "Quel film de 2020 parle de retraités vivant dans leur camionnette ?", ["Nomadland", "Into the Wild", "On the Road", "Modern Times"]),
   DT(D, "Vers quelle région partent beaucoup d'Américains aujourd'hui ?", ["La Sun Belt", "La Rust Belt", "La Bible Belt", "L'Alaska"]),
   DT(D, "Comment dit-on « un train de marchandises » ?", ["A freight train", "A free train", "A goods car", "A cargo bus"])],
  [W(D, "Trouve le mot qui veut dire « avait besoin de ».", "needed"), W(D, "Trouve le mot qui veut dire « né » (dans un autre pays).", "born"),
   W(D, "Trouve le mot qui veut dire « secrètement ».", "secretly"), W(D, "Trouve le mot qui veut dire « la pauvreté ».", "poverty")])

# ═════════ PUBLICITÉ ═════════
F = "cu_publicite.html"
DZ(F, """
## L'Amérique, patrie de la publicité
La publicité moderne se développe aux États-Unis à la fin du 19e siècle, avec les journaux, les marques nationales et les grands magasins. Après 1945, les agences de **Madison Avenue**, à New York, deviennent les maîtres de la communication : on les voit dans la série *Mad Men*. La télévision fait entrer les **commercials** dans tous les foyers. Aujourd'hui, les publicités diffusées pendant le **Super Bowl** coûtent plusieurs millions de dollars pour 30 secondes et sont attendues autant que le match.

## Des slogans et des images inoubliables
- **Coca-Cola** (1886) a construit l'une des marques les plus célèbres du monde. Dans les années 1930, ses publicités de Noël popularisent l'image d'un **Santa Claus** jovial, en costume rouge et blanc.
- **Nike** lance en 1988 un slogan de trois mots devenu universel : « *Just Do It* ».
- En 1984, **Apple** présente son ordinateur Macintosh pendant le Super Bowl avec une publicité inspirée du roman *1984* d'Orwell : une jeune femme brise l'écran d'un « Big Brother » pour libérer la foule.
- Les publicités jouent sur les **emotions** (rire, nostalgie, peur de manquer quelque chose), les **celebrities**, la répétition, le rêve d'un mode de vie.

## La publicité, arme du soft power
En 1990, le politologue américain **Joseph Nye** invente l'expression **soft power** : la capacité d'un pays à influencer les autres par l'attraction de sa culture, de ses valeurs et de ses produits, plutôt que par la force (**hard power**). Les marques américaines, comme Coca-Cola, McDonald's, Levi's, Apple ou Netflix, font rêver le monde entier à l'**American way of life**. Pendant la guerre froide, ces produits étaient même vus comme des symboles de la liberté occidentale face à l'URSS.

## Les limites et les débats
La publicité est critiquée pour pousser à la surconsommation, cibler les enfants, véhiculer des stéréotypes ou diffuser des images corporelles irréalistes. Les pays anglophones l'encadrent : au Royaume-Uni, une autorité indépendante (l'ASA) peut interdire une publicité trompeuse, et depuis 2026, les publicités pour la malbouffe sont interdites à la télévision avant 21 h. Sur les réseaux sociaux, les **influencers** doivent signaler leurs contenus sponsorisés (#ad). Savoir décrypter une publicité, c'est apprendre à repérer qui parle, à qui, et pour vendre quoi.
[→ Voir aussi : Shopping et consommation](cu_consommation.html)
""", """
an advert = une publicité
a slogan = un slogan
a brand = une marque
a product = un produit
to buy = acheter
a customer = un client
an influencer = un influenceur
a logo = un logo
""", [
 ("Que représente Madison Avenue ?", ["Le cœur des agences de publicité à New York", "Une autoroute", "Un stade"], ""),
 ("Quel rôle a joué Coca-Cola pour Santa Claus ?", ["Ses publicités ont popularisé le Père Noël en rouge et blanc", "Elle l'a inventé en 1886", "Aucun"], ""),
 ("De quoi s'inspire la publicité Apple de 1984 ?", ["Du roman 1984 d'Orwell", "D'un film de Chaplin", "Du Super Bowl"], ""),
 ("Qu'est-ce que le soft power ?", ["Influencer par l'attraction de sa culture et de ses produits", "La force militaire", "Un logiciel"], ""),
 ("Que reproche-t-on à la publicité ?", ["Pousser à surconsommer, cibler les enfants, véhiculer des stéréotypes", "Être trop rare", "Être gratuite"], ""),
 ("Que doivent faire les influenceurs ?", ["Signaler leurs contenus sponsorisés", "Arrêter de publier", "Payer leurs abonnés"], ""),
], [("**Joseph Nye**", "politologue américain, 1937-2025"), ("*Mad Men*", "série sur une agence de publicité des années 1960")])
D = "pb"
culture(F, "Culture : Advertising and soft power", 'Advertising <span>&amp; soft power</span>',
  "Culture · slogans, marques et influence américaine", ("#fca5a5", "#ca8a04"),
  reperes("La publicité moderne est née aux États-Unis. Avec les marques américaines, elle diffuse dans le monde l'American way of life : c'est le soft power.",
    [("1886", "naissance de Coca-Cola"), ("années 1930", "le Santa Claus de Coca-Cola"), ("1984", "la publicité « 1984 » d'Apple"),
     ("1988", "« Just Do It » de Nike"), ("1990", "Joseph Nye invente le « soft power »")],
    "an advert, a commercial, a slogan, a brand, a target, soft power, an influencer, to persuade"),
  {D: doc("Buy me!", [
    "Modern advertising was born in the USA. In the 1950s and 60s, the big agencies were on Madison Avenue, in New York.",
    "Some slogans are famous all over the world, like Nike's \"Just Do It\". The adverts shown during the Super Bowl cost millions of dollars.",
    "Adverts use emotions, celebrities and humour to make us want to buy. They also sell a dream: a lifestyle.",
    "American brands like Coca-Cola, McDonald's and Apple are known everywhere. They spread the American way of life. This influence is called soft power.",
    "But advertising is also criticised. Some people say it makes us buy things we don't need. In the UK, junk food adverts are now banned on TV before 9 pm."])},
  [TF(D, "Modern advertising was born in the USA.", True, "« born in the USA »."),
   TF(D, "The big agencies were in Los Angeles.", False, "« on Madison Avenue, in New York »."),
   TF(D, "Super Bowl adverts are very cheap.", False, "« cost millions of dollars »."),
   TF(D, "Adverts sell a dream.", True, "« They also sell a dream »."),
   TF(D, "Soft power is the influence of brands and culture.", True, "« This influence is called soft power »."),
   TF(D, "In the UK, junk food adverts are allowed on TV at any time.", False, "« banned on TV before 9 pm »." )],
  [Q(D, "Where were the big agencies?", ["On Madison Avenue, in New York.", "In London.", "In Paris."]),
   Q(D, "What do adverts use?", ["Emotions, celebrities and humour.", "Only numbers.", "Only silence."]),
   Q(D, "What is soft power?", ["Influence through culture and brands.", "Military power.", "Electricity."]),
   Q(D, "Why is advertising criticised?", ["It makes us buy things we don't need.", "It is too short.", "It is boring."])],
  [DT(D, "Quel est le slogan de Nike ?", ["« Just Do It »", "« Think Different »", "« I'm lovin' it »", "« Yes we can »"]),
   DT(D, "Qui a inventé l'expression « soft power » ?", ["Joseph Nye", "George Orwell", "Henry Ford", "Steve Jobs"]),
   DT(D, "Quelle série montre une agence de publicité des années 1960 ?", ["Mad Men", "Friends", "Sherlock", "The Office"]),
   DT(D, "Comment dit-on « une marque » ?", ["A brand", "A mark", "A sign", "A label shop"])],
  [W(D, "Trouve le mot qui veut dire « les agences ».", "agencies"), W(D, "Trouve le mot qui veut dire « un mode de vie ».", ["lifestyle", "a lifestyle"]),
   W(D, "Trouve le mot qui veut dire « répandent, diffusent ».", "spread"), W(D, "Trouve le mot qui veut dire « interdites ».", "banned")])

# ═════════ CAMPUS US ═════════
F = "cu_campus_us.html"
DZ(F, """
## Les cliques du lycée
Dans les lycées américains, et surtout dans les films et les séries qui les représentent, les élèves se regroupent souvent en **cliques** : les **jocks** (sportifs vedettes), les **cheerleaders**, les **nerds** ou **geeks** (passionnés d'informatique ou de sciences), les **theater kids**, les **goths**… Le film *The Breakfast Club* (1985), où cinq élèves très différents passent un samedi en retenue et découvrent qu'ils se ressemblent plus qu'ils ne le pensaient, a popularisé ces stéréotypes. *Mean Girls* (2004) se moque de la cruauté des groupes de filles populaires. Dans la réalité, les frontières entre groupes sont souvent plus floues, mais la pression pour « appartenir » est forte.

## Les clubs et les activités
Les lycées américains proposent de très nombreuses activités : équipes sportives, fanfare (**marching band**), théâtre, club de débat, robotique, journal du lycée, **Model UN** (simulation des Nations unies), clubs de bénévolat… Ces **extracurricular activities** comptent beaucoup pour entrer dans les universités les plus sélectives, qui veulent des élèves engagés.

## Le yearbook et les traditions
À la fin de chaque année, chaque élève reçoit le **yearbook**, un album qui contient la photo de tous les élèves, des clubs, des équipes et des événements de l'année. On le fait signer par ses amis avec des messages personnels. Les élèves de terminale (**seniors**) votent pour des « **superlatives** » : « *Most likely to succeed* » (celui qui a le plus de chances de réussir), « *Best smile* », « *Class clown* »… Les grandes traditions sont le **homecoming** (fête d'automne avec match de football et élection d'un roi et d'une reine), le **prom** (bal de fin d'année) et la **graduation**, où l'on lance son chapeau carré en l'air.

## Fraternités et sororités
À l'université, de nombreux étudiants rejoignent des **fraternities** (pour les garçons) ou des **sororities** (pour les filles), des associations désignées par des lettres grecques, comme *Kappa Alpha Theta*. La première société à lettres grecques, Phi Beta Kappa, est fondée en 1776. Les membres vivent souvent ensemble dans une grande maison sur le campus, organisent des soirées, des actions caritatives et se constituent un réseau d'amis qui peut les aider toute leur vie : de nombreux présidents, chefs d'entreprise et sénateurs en ont été membres. Pour entrer, il faut passer par une période de sélection, le **rush**.
Mais ce système est critiqué : il peut être élitiste et coûteux, favoriser l'alcool, et certains rituels d'initiation dangereux et humiliants, le **hazing**, ont causé des morts. De nombreux États ont adopté des lois pour les interdire.
[→ Voir aussi : le lycée américain](cu_lycee_us.html)
""", """
a group = un groupe
a club = un club
a yearbook = un album de fin d'année
a dance = un bal
a team = une équipe
popular = populaire
a member = un membre
a party = une fête, une soirée
""", [
 ("Qu'est-ce qu'une clique ?", ["Un groupe d'élèves qui se ressemblent", "Un bruit", "Un cours"], ""),
 ("Que montre The Breakfast Club ?", ["Cinq élèves différents qui découvrent qu'ils se ressemblent", "Un match de football", "Un petit-déjeuner géant"], ""),
 ("Pourquoi les activités extrascolaires sont-elles importantes ?", ["Elles comptent pour entrer dans les universités sélectives", "Elles sont obligatoires par la loi", "Elles rapportent de l'argent"], ""),
 ("Que trouve-t-on dans un yearbook ?", ["Les photos des élèves et des événements de l'année", "Les notes des élèves", "Le règlement"], ""),
 ("Que sont les fraternités et sororités ?", ["Des associations étudiantes à lettres grecques", "Des familles nombreuses", "Des équipes de sport"], ""),
 ("Pourquoi ce système est-il critiqué ?", ["Il peut être élitiste et certains rituels (hazing) sont dangereux", "Il est trop ouvert", "Il est gratuit"], ""),
], [("Phi Beta Kappa", "la plus ancienne société étudiante à lettres grecques")])
D = "cp"
culture(F, "Culture : Cliques, clubs and Greek life", 'Cliques <span>&amp; campus life</span>',
  "Culture · cliques, yearbooks, fraternités et sororités", ("#fbcfe8", "#1d4ed8"),
  reperes("Au lycée et à l'université aux États-Unis, la vie sociale passe par les cliques, les clubs, le yearbook et les fraternités.",
    [("1776", "Phi Beta Kappa, première société à lettres grecques"), ("1985", "The Breakfast Club"), ("2004", "Mean Girls"),
     ("homecoming", "la fête d'automne"), ("prom", "le bal de fin d'année")],
    "a clique, a jock, a nerd, a yearbook, a club, a fraternity, a sorority, peer pressure"),
  {D: doc("Where do you belong?", [
    "In American high school films, students are often in cliques: the jocks, the cheerleaders, the nerds or the theater kids.",
    "In The Breakfast Club, five very different students spend a Saturday in detention and discover that they have a lot in common.",
    "Schools have lots of clubs, like drama, robotics or debate. These activities are important to get into a good university.",
    "At the end of the year, students get a yearbook with photos of everybody. Friends write messages in it.",
    "At university, many students join fraternities or sororities, groups with Greek letters. They live together and help each other, but some traditions can be dangerous."])},
  [TF(D, "In films, American students are often in cliques.", True, "« often in cliques »."),
   TF(D, "In The Breakfast Club, the students have nothing in common.", False, "« a lot in common »."),
   TF(D, "Clubs are important to get into a good university.", True, "« important to get into a good university »."),
   TF(D, "Friends write messages in the yearbook.", True, "« Friends write messages in it »."),
   TF(D, "Fraternities use Chinese letters.", False, "« Greek letters »."),
   TF(D, "All fraternity traditions are safe.", False, "« some traditions can be dangerous »." )],
  [Q(D, "Name a clique.", ["The jocks.", "The teachers.", "The parents."]),
   Q(D, "Where do the five students spend their Saturday?", ["In detention.", "At the beach.", "At a party."]),
   Q(D, "What is in a yearbook?", ["Photos of everybody.", "Exam results.", "Recipes."]),
   Q(D, "What do fraternity members often do?", ["They live together and help each other.", "They never meet.", "They work in shops."])],
  [DT(D, "Comment s'appelle la fête d'automne avec un roi et une reine ?", ["Homecoming", "Prom", "Graduation", "Halloween"]),
   DT(D, "Comment s'appellent les rituels d'initiation dangereux ?", ["Le hazing", "Le rush", "Le prom", "Le dating"]),
   DT(D, "Que veut dire « Most likely to succeed » ?", ["Celui qui a le plus de chances de réussir", "Le plus drôle", "Le plus grand", "Le plus sportif"]),
   DT(D, "Comment dit-on « une retenue » ?", ["Detention", "Retention", "Holding", "Stop"])],
  [W(D, "Trouve le mot qui veut dire « en commun » (2 mots).", ["in common"]), W(D, "Trouve le mot qui veut dire « une université ».", "university"),
   W(D, "Trouve le mot qui veut dire « rejoignent ».", "join"), W(D, "Trouve le mot qui veut dire « dangereuses ».", "dangerous")])
END()
