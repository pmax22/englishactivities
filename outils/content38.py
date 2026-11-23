import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
exec(open(_EA_OUT+"/cuhelp.py", encoding="utf-8").read())

# ═════════ DIASPORA INDIENNE ═════════
F = "cu_diaspora_indienne.html"
DZ(F, """
## Une longue histoire commune
Les liens entre l'Inde et la Grande-Bretagne remontent à l'époque coloniale : marins indiens (les **lascars**) dans les ports anglais, étudiants, soldats (plus de deux millions d'Indiens ont combattu pour l'Empire pendant la Seconde Guerre mondiale). Après l'indépendance et la **Partition** de 1947, de nombreux Indiens, Pakistanais et Bangladais viennent travailler au Royaume-Uni dans les années 1950-1960, dans les usines textiles du Nord, les transports ou près de l'aéroport d'Heathrow, à **Southall**. En 1972, le dictateur ougandais Idi Amin expulse les Asiatiques de son pays : des dizaines de milliers, souvent d'origine indienne, s'installent notamment à **Leicester**.

## Une communauté qui a réussi… et qui a dû se battre
Les Britanniques d'origine indienne sont aujourd'hui environ 1,9 million : c'est la plus grande minorité du pays. Beaucoup ont réussi dans l'éducation, la médecine, le commerce (les épiceries de quartier, les *corner shops*) et la politique : en 2022, **Rishi Sunak** devient le premier Premier ministre d'origine indienne et de religion hindoue. Mais les premières générations ont subi le racisme, les attaques et les discriminations au logement et à l'emploi. Des combats ont été menés, par exemple pour que les sikhs puissent porter leur turban au travail ou à moto.

## Entre deux cultures : les générations
La question des relations entre générations est centrale :
- les **parents immigrés**, qui ont beaucoup sacrifié, tiennent souvent à transmettre la langue (hindi, punjabi, gujarati…), la religion, la cuisine et les traditions familiales, et ont de grandes ambitions scolaires pour leurs enfants ;
- leurs **enfants**, nés au Royaume-Uni, se sentent à la fois britanniques et indiens (**British Asian**), parlent parfois mal la langue de leurs parents et veulent choisir leurs études, leur métier et leur conjoint (débat autour des mariages arrangés).
Le film *Bend It Like Beckham* (2002) raconte l'histoire de Jess, une jeune Anglaise d'origine sikhe qui rêve de jouer au football alors que ses parents veulent qu'elle se comporte en « bonne fille indienne ». L'émission comique de la BBC *Goodness Gracious Me* s'amusait de ces malentendus culturels.

## Une culture qui a transformé la Grande-Bretagne
La diaspora a profondément enrichi la culture britannique : le **curry** est devenu un plat national (le *chicken tikka masala* aurait été inventé à Glasgow), la fête de **Diwali** rassemble chaque année des dizaines de milliers de personnes à Leicester, la musique **bhangra** mêle rythmes punjabi et pop, et Bollywood a ses fans.

## Et aux États-Unis
Aux États-Unis, la diaspora indienne compte environ 5 millions de personnes, souvent très diplômées : les patrons de **Google** (Sundar Pichai) et de **Microsoft** (Satya Nadella) sont nés en Inde, et l'ancienne vice-présidente Kamala Harris est la fille d'une mère indienne. Mais après le 11 septembre 2001, des sikhs ont été victimes d'agressions racistes, confondus avec des musulmans.
[→ Voir aussi : l'Inde et l'Empire](cu_inde.html)
""", """
a family = une famille
a generation = une génération
parents = les parents
a tradition = une tradition
a language = une langue
a wedding = un mariage
a shop = un magasin
to belong = appartenir
""", [
 ("Pourquoi de nombreux Indiens viennent-ils au Royaume-Uni dans les années 1950-1960 ?", ["Pour travailler dans les usines et les transports", "Pour faire du tourisme", "Pour étudier le football"], ""),
 ("Que se passe-t-il en 1972 ?", ["Idi Amin expulse les Asiatiques d'Ouganda", "L'Inde devient indépendante", "Rishi Sunak est élu"], ""),
 ("Qui est Rishi Sunak ?", ["Le premier Premier ministre britannique d'origine indienne", "Un joueur de cricket", "Un acteur de Bollywood"], ""),
 ("Que veulent souvent les enfants nés au Royaume-Uni ?", ["Choisir leurs études, leur métier et leur conjoint", "Retourner tous en Inde", "Abandonner l'école"], ""),
 ("De quoi parle Bend It Like Beckham ?", ["D'une jeune fille d'origine sikhe qui veut jouer au football", "D'un joueur célèbre", "D'un mariage royal"], ""),
 ("Quel plat serait né à Glasgow ?", ["Le chicken tikka masala", "Le fish and chips", "Le haggis"], ""),
], [("Partition", "division de l'Inde britannique en Inde et Pakistan, 1947"), ("Idi Amin", "dictateur de l'Ouganda de 1971 à 1979"), ("sikhs", "fidèles du sikhisme, religion née au Pendjab")])
D = "di"
culture(F, "Culture : The Indian diaspora", 'The Indian <span>diaspora</span>',
  "Culture · British Asians, générations et identités", ("#fdba74", "#047857"),
  reperes("Les Britanniques d'origine indienne forment la plus grande minorité du Royaume-Uni. Leur histoire mêle immigration, réussite, racisme et dialogue entre générations.",
    [("1947", "indépendance et Partition de l'Inde"), ("1950 – 1960", "immigration de travail"), ("1972", "expulsion des Asiatiques d'Ouganda"),
     ("2002", "Bend It Like Beckham"), ("2022", "Rishi Sunak Premier ministre")],
    "a diaspora, an immigrant, a generation, an identity, a tradition, an arranged marriage, British Asian, to belong"),
  {D: doc("Between two worlds", [
    "After India became independent in 1947, many Indians moved to Britain to work in factories and transport. Today, British Indians are the largest minority in the UK.",
    "Many have been very successful in education, medicine and business. In 2022, Rishi Sunak became the first British Prime Minister of Indian origin.",
    "Life was not always easy. The first immigrants often faced racism and discrimination.",
    "Children born in Britain often feel both British and Indian. Sometimes, they disagree with their parents about studies, jobs or marriage. The film Bend It Like Beckham tells the story of Jess, who wants to play football against her parents' wishes.",
    "Indian culture has changed Britain: curry is one of the most popular dishes, and Diwali is celebrated in many cities."])},
  [TF(D, "British Indians are the largest minority in the UK.", True, "« the largest minority »."),
   TF(D, "Rishi Sunak was the first Prime Minister of Indian origin.", True, "« the first British Prime Minister of Indian origin »."),
   TF(D, "The first immigrants never faced racism.", False, "« often faced racism »."),
   TF(D, "Children born in Britain feel only Indian.", False, "« both British and Indian »."),
   TF(D, "Jess wants to play football.", True, "« wants to play football »."),
   TF(D, "Curry is not popular in Britain.", False, "« one of the most popular dishes »." )],
  [Q(D, "Why did many Indians move to Britain?", ["To work in factories and transport.", "To go on holiday.", "To play cricket."]),
   Q(D, "What did the first immigrants often face?", ["Racism and discrimination.", "Nothing difficult.", "Very high wages."]),
   Q(D, "What do children and parents sometimes disagree about?", ["Studies, jobs or marriage.", "The weather.", "Football teams only."]),
   Q(D, "How has Indian culture changed Britain?", ["Curry is popular and Diwali is celebrated.", "Everybody speaks Hindi.", "It hasn't changed anything."])],
  [DT(D, "Dans quelle ville fête-t-on un grand Diwali au Royaume-Uni ?", ["Leicester", "Liverpool", "Cardiff", "Belfast"]),
   DT(D, "Qui dirige Google ?", ["Sundar Pichai", "Satya Nadella", "Rishi Sunak", "Steve Jobs"]),
   DT(D, "Comment appelle-t-on les marins indiens de l'époque coloniale ?", ["Les lascars", "Les sepoys", "Les sikhs", "Les gurkhas"]),
   DT(D, "Comment dit-on « une minorité » ?", ["A minority", "A minor", "A mini group", "A minus"])],
  [W(D, "Trouve le mot qui veut dire « indépendante ».", "independent"), W(D, "Trouve le mot qui veut dire « la plus grande minorité » (3 mots).", ["the largest minority", "largest minority"]),
   W(D, "Trouve le mot qui veut dire « ne sont pas d'accord ».", "disagree"), W(D, "Trouve le mot qui veut dire « les souhaits ».", "wishes")])

# ═════════ NATURE & ÉCRIVAINS ═════════
F = "cu_nature.html"
DZ(F, """
## Les romantiques anglais
À la fin du 18e siècle, alors que la révolution industrielle couvre les villes de fumée, des poètes anglais célèbrent la **nature** comme une source de beauté, d'émotion et presque de sacré. En 1798, **William Wordsworth** et Samuel Taylor Coleridge publient les *Lyrical Ballads*, manifeste du **Romanticism**. Wordsworth, installé dans le **Lake District**, écrit en 1807 un poème célèbre où il se décrit errant « *lonely as a cloud* », jusqu'à la vision d'un champ de jonquilles qui le remplit de joie. Le peintre Turner, de son côté, peint la puissance des tempêtes. Pour les romantiques, la nature élève l'âme et l'industrie la menace.

## Les transcendantalistes américains
Aux États-Unis, Ralph Waldo Emerson publie *Nature* en 1836. Son ami **Henry David Thoreau** part vivre deux ans (1845-1847) dans une cabane qu'il a construite au bord de l'étang de **Walden**, dans le Massachusetts, pour vivre simplement, au contact de la nature. Son livre *Walden* (1854) est devenu une bible pour tous ceux qui veulent ralentir et consommer moins. Thoreau a aussi écrit sur la **désobéissance civile**, qui inspirera Gandhi et Martin Luther King.

## Protéger la nature
- L'Écossais **John Muir** explore la Sierra Nevada et la vallée de **Yosemite** ; il fonde en 1892 le **Sierra Club**, l'une des premières associations écologistes, et convainc le président Theodore Roosevelt de protéger de vastes territoires. Les **parcs nationaux** américains deviennent un modèle mondial.
- En 1962, la biologiste **Rachel Carson** publie *Silent Spring* (Printemps silencieux), qui montre que les pesticides comme le DDT empoisonnent les oiseaux et l'environnement. Le livre fait scandale auprès de l'industrie chimique, mais il conduit à la création de l'Agence américaine de protection de l'environnement en 1970 et à l'interdiction du DDT. La première **Earth Day** a lieu le 22 avril 1970.
- Les peuples autochtones rappellent qu'ils entretenaient depuis des millénaires un lien spirituel avec la terre, et revendiquent un rôle dans sa protection.

## L'être humain face aux éléments
La nature n'est pas seulement belle : elle peut être terrible. Les pays anglophones affrontent des événements météorologiques extrêmes, de plus en plus fréquents avec le **changement climatique** :
- l'ouragan **Katrina** (2005) inonde La Nouvelle-Orléans et fait plus de 1 800 morts, révélant aussi les inégalités sociales ;
- les gigantesques **feux de brousse** de l'été 2019-2020 en Australie (le « Black Summer ») détruisent des millions d'hectares et touchent des milliards d'animaux ;
- en 2021, un « dôme de chaleur » fait grimper la température à près de 50 °C dans un village du Canada, un record.
Écrivains, cinéastes et documentaristes comme David Attenborough font de la nature un grand sujet d'aujourd'hui : comment vivre avec elle, et non contre elle ?
[→ Voir aussi : la géographie des États-Unis et les parcs nationaux](cu_geographie_usa.html)
""", """
nature = la nature
a poet = un poète
a cloud = un nuage
a lake = un lac
a forest = une forêt
a bird = un oiseau
a storm = une tempête
a fire = un feu, un incendie
""", [
 ("Que célèbrent les poètes romantiques ?", ["La nature, source de beauté et d'émotion", "Les usines", "Les grandes villes"], ""),
 ("Que fait Thoreau à Walden ?", ["Il vit deux ans dans une cabane pour vivre simplement", "Il construit une usine", "Il devient président"], ""),
 ("Qu'a fondé John Muir ?", ["Le Sierra Club, association écologiste", "La BBC", "Une compagnie pétrolière"], ""),
 ("Que montre Silent Spring de Rachel Carson ?", ["Que les pesticides empoisonnent les oiseaux et l'environnement", "Que le printemps est silencieux par nature", "Comment cultiver des fleurs"], ""),
 ("Qu'a révélé l'ouragan Katrina ?", ["Les inégalités sociales", "Rien", "La richesse de la ville"], ""),
 ("Quelle question posent aujourd'hui écrivains et documentaristes ?", ["Comment vivre avec la nature et non contre elle", "Comment construire plus d'usines", "Comment éviter de lire"], ""),
], [("Samuel Taylor Coleridge", "poète romantique anglais"), ("**Henry David Thoreau**", "écrivain américain, 1817-1862"), ("**Rachel Carson**", "biologiste américaine, 1907-1964")])
D = "na"
culture(F, "Culture : Humans and nature", 'Humans <span>&amp; nature</span>',
  "Culture · Wordsworth, Thoreau, Muir, Carson et les extrêmes climatiques", ("#bbf7d0", "#1e3a8a"),
  reperes("Des poètes romantiques aux écologistes, les auteurs anglophones ont célébré et défendu la nature. Aujourd'hui, ses colères rappellent l'urgence climatique.",
    [("1798", "Lyrical Ballads de Wordsworth et Coleridge"), ("1854", "Walden de Thoreau"), ("1892", "John Muir fonde le Sierra Club"),
     ("1962", "Silent Spring de Rachel Carson"), ("22 avril 1970", "première Earth Day"), ("2005", "l'ouragan Katrina")],
    "nature, wilderness, a poet, the environment, conservation, a pesticide, climate change, an extreme weather event"),
  {D: doc("Back to nature", [
    "During the Industrial Revolution, English Romantic poets like William Wordsworth wrote about the beauty of nature. For them, nature was almost sacred.",
    "In America, Henry David Thoreau lived alone for two years in a small cabin near Walden Pond. He wanted to live simply. His book Walden is still very popular.",
    "John Muir helped to create national parks, and in 1962 Rachel Carson showed that pesticides were killing birds. Her book changed American laws.",
    "Today, nature can also be dangerous. Hurricanes, floods and huge fires are more frequent because of climate change.",
    "Writers and filmmakers ask an important question: how can humans live with nature, not against it?"])},
  [TF(D, "Romantic poets wrote about the beauty of nature.", True, "« wrote about the beauty of nature »."),
   TF(D, "Thoreau lived in a big city.", False, "« a small cabin near Walden Pond »."),
   TF(D, "John Muir helped to create national parks.", True, "« helped to create national parks »."),
   TF(D, "Rachel Carson showed that pesticides were good for birds.", False, "« were killing birds »."),
   TF(D, "Extreme weather events are more frequent.", True, "« more frequent because of climate change »."),
   TF(D, "Writers think humans should fight against nature.", False, "« live with nature, not against it »." )],
  [Q(D, "What was nature for the Romantic poets?", ["Almost sacred.", "Dangerous only.", "Boring."]),
   Q(D, "Why did Thoreau live in a cabin?", ["He wanted to live simply.", "He was poor.", "He was hiding."]),
   Q(D, "What did Rachel Carson's book change?", ["American laws.", "The weather.", "Fashion."]),
   Q(D, "Why are extreme weather events more frequent?", ["Because of climate change.", "Because of poets.", "Because of national parks."])],
  [DT(D, "Dans quelle région vivait Wordsworth ?", ["Le Lake District", "Les Highlands", "Le Yorkshire", "Le Kent"]),
   DT(D, "Quel livre de Thoreau parle de sa vie dans les bois ?", ["Walden", "Nature", "Silent Spring", "Leaves of Grass"]),
   DT(D, "Quelle vallée John Muir a-t-il fait protéger ?", ["Yosemite", "Death Valley", "Silicon Valley", "Napa Valley"]),
   DT(D, "Comment dit-on « la nature sauvage » ?", ["The wilderness", "The wild nature only", "The forest land", "The savage"])],
  [W(D, "Trouve le mot qui veut dire « sacrée ».", "sacred"), W(D, "Trouve le mot qui veut dire « une cabane ».", ["cabin", "a small cabin"]),
   W(D, "Trouve le mot qui veut dire « des inondations ».", "floods"), W(D, "Trouve le mot qui veut dire « fréquents ».", "frequent")])

# ═════════ VANCOUVER & SEATTLE ═════════
F = "cu_vancouver_seattle.html"
DZ(F, """
## Deux villes jumelles du Pacifique
**Seattle** (États-Unis) et **Vancouver** (Canada) ne sont séparées que par environ 230 kilomètres et une frontière. Elles appartiennent à la même région, que certains appellent **Cascadia** : un littoral découpé, des montagnes enneigées (les Cascades, les Rocheuses), des forêts immenses, un climat doux et… beaucoup de pluie. Ces deux grands ports tournés vers l'Asie partagent bien des traits, mais aussi des différences révélatrices de leurs pays.

## Seattle, la ville des géants
Fondée dans les années 1850 et nommée d'après le chef amérindien **Si'ahl**, Seattle grandit grâce au bois, puis à la ruée vers l'or du Klondike (1897), dont elle est la porte d'entrée. Au 20e siècle, elle devient la ville de **Boeing** (avions), puis de la technologie : **Microsoft** s'installe dans sa banlieue en 1979, **Amazon** y naît en 1994, et le premier café **Starbucks** ouvre en 1971 au marché de Pike Place. Sa tour futuriste, la **Space Needle**, date de l'Exposition universelle de 1962. Au début des années 1990, la scène **grunge** (Nirvana, Pearl Jam) fait de Seattle la capitale du rock ; Jimi Hendrix y est né. La prospérité de la tech a fait flamber les loyers, et la ville est confrontée à un nombre très élevé de sans-abri.

## Vancouver, la métropole multiculturelle
Vancouver porte le nom du navigateur britannique George Vancouver, qui explore la côte en 1792. Elle est construite sur les terres non cédées de trois Premières Nations (Musqueam, Squamish et Tsleil-Waututh). Fondée en 1886, elle devient le terminus du chemin de fer transcanadien. Elle a accueilli l'Exposition universelle de 1986 et les **Jeux olympiques d'hiver de 2010**. Les tournages y sont si nombreux qu'on la surnomme « **Hollywood North** ». Ville très multiculturelle, elle compte une importante communauté chinoise, renforcée par l'arrivée de nombreux Hongkongais avant 1997 ; près de la moitié de ses habitants n'ont pas l'anglais comme langue maternelle. Elle est régulièrement classée parmi les villes les plus agréables à vivre… mais aussi parmi les plus chères pour se loger.

## Regards croisés
- Toutes deux sont des villes **vertes** et sportives : le grand parc Stanley à Vancouver, le kayak et la randonnée à Seattle. Toutes deux ont accueilli des matchs de la Coupe du monde de football de 2026.
- Elles affrontent des défis communs : prix du logement, sans-abrisme, crise des opioïdes, risque de séisme majeur dans la région.
- Mais elles reflètent aussi leurs pays : système de santé public au Canada, assurance privée aux États-Unis ; politique d'immigration canadienne fondée sur l'accueil planifié ; présence forte des Premières Nations dans la vie publique de Vancouver.
La frontière, symbolisée par le Peace Arch, sépare deux pays qui se ressemblent beaucoup, mais qui tiennent à leurs différences.
[→ Voir aussi : le Canada](cu_canada.html)
""", """
a city = une ville
a port = un port
rain = la pluie
a mountain = une montagne
a coffee = un café
a border = une frontière
a rent = un loyer
a tower = une tour
""", [
 ("Qu'ont en commun Seattle et Vancouver ?", ["Montagnes, forêts, pluie et ports tournés vers l'Asie", "Elles sont dans le même pays", "Elles sont dans le désert"], ""),
 ("Quelles grandes entreprises sont nées ou installées à Seattle ?", ["Boeing, Microsoft, Amazon, Starbucks", "Apple et Google", "Coca-Cola et Ford"], ""),
 ("Quelle musique fait de Seattle la capitale du rock au début des années 1990 ?", ["Le grunge", "Le jazz", "La country"], ""),
 ("Pourquoi Vancouver est-elle surnommée « Hollywood North » ?", ["De très nombreux films y sont tournés", "Elle a un grand panneau", "Elle est près d'Hollywood"], ""),
 ("Quel problème touche les deux villes ?", ["Le prix du logement et le sans-abrisme", "Le manque d'eau", "Le froid extrême"], ""),
 ("En quoi les deux villes reflètent-elles leurs pays ?", ["Système de santé, politique d'immigration, place des Premières Nations", "Elles ne reflètent rien", "Par leur météo"], ""),
], [("Si'ahl", "chef des peuples Duwamish et Suquamish"), ("George Vancouver", "officier de la Royal Navy, 1757-1798")])
D = "vs"
culture(F, "Culture : Vancouver and Seattle", 'Vancouver <span>&amp; Seattle</span>',
  "Culture · deux villes du Pacifique, deux pays", ("#a5f3fc", "#166534"),
  reperes("Seattle et Vancouver, séparées par une frontière, partagent la même région. Leurs ressemblances et différences éclairent les États-Unis et le Canada.",
    [("1792", "George Vancouver explore la côte"), ("1886", "fondation de Vancouver"), ("1897", "ruée vers l'or du Klondike"),
     ("1962", "la Space Needle de Seattle"), ("1994", "naissance d'Amazon"), ("2010", "JO d'hiver de Vancouver")],
    "a port, a region, a border, tech companies, multicultural, housing costs, homelessness, First Nations"),
  {D: doc("Two cities, one coast", [
    "Seattle, in the USA, and Vancouver, in Canada, are only about 230 kilometres apart. Both cities are surrounded by mountains, forests and the sea, and it rains a lot.",
    "Seattle is the home of big companies like Boeing, Microsoft, Amazon and Starbucks. It is also the city of grunge music and Jimi Hendrix.",
    "Vancouver is a very multicultural city. Almost half of its inhabitants don't speak English as their first language. Many films are made there, so people call it \"Hollywood North\".",
    "Both cities are beautiful and green, but they have the same problems: houses are very expensive, and many people are homeless.",
    "They are similar, but they show differences between the two countries, for example health care and immigration."])},
  [TF(D, "Seattle and Vancouver are in the same country.", False, "Seattle est aux États-Unis, Vancouver au Canada."),
   TF(D, "It rains a lot in both cities.", True, "« it rains a lot »."),
   TF(D, "Amazon is from Seattle.", True, "« Microsoft, Amazon and Starbucks »."),
   TF(D, "Everybody in Vancouver speaks English as a first language.", False, "« Almost half… don't speak English as their first language »."),
   TF(D, "Houses are cheap in both cities.", False, "« houses are very expensive »."),
   TF(D, "Vancouver is called \"Hollywood North\".", True, "« Hollywood North »." )],
  [Q(D, "How far apart are the two cities?", ["About 230 kilometres.", "About 5,000 kilometres.", "They are in the same street."]),
   Q(D, "What is Seattle the home of?", ["Big companies like Boeing and Amazon.", "The Canadian government.", "Hollywood."]),
   Q(D, "Why is Vancouver called \"Hollywood North\"?", ["Many films are made there.", "It has a big sign.", "It is very sunny."]),
   Q(D, "What problems do both cities have?", ["Expensive houses and homelessness.", "Too much sun.", "No jobs."])],
  [DT(D, "Comment s'appelle la tour futuriste de Seattle ?", ["La Space Needle", "La CN Tower", "L'Empire State", "La Sky Tower"]),
   DT(D, "Quel groupe grunge vient de la région de Seattle ?", ["Nirvana", "The Beatles", "Coldplay", "Oasis"]),
   DT(D, "Quel monument marque la frontière ?", ["Le Peace Arch", "La Statue de la Liberté", "Le Golden Gate", "Le Hadrian's Wall"]),
   DT(D, "Comment dit-on « un sans-abri » ?", ["A homeless person", "A houseless", "A no-home man", "A street worker"])],
  [W(D, "Trouve le mot qui veut dire « entourées ».", "surrounded"), W(D, "Trouve le mot qui veut dire « les habitants ».", "inhabitants"),
   W(D, "Trouve le mot qui veut dire « sans-abri » (adjectif).", "homeless"), W(D, "Trouve le mot qui veut dire « semblables ».", "similar")])

# ═════════ CARICATURE & PHOTOJOURNALISME ═════════
F = "cu_caricature.html"
DZ(F, """
## La caricature, une tradition britannique
Au 18e siècle, le peintre et graveur **William Hogarth** dénonce les vices de la société londonienne. Dans *Gin Lane* (1751), il montre une rue où l'alcool bon marché provoque misère et chaos, en contraste avec la *Beer Street* prospère. Son successeur **James Gillray** ridiculise les rois, les ministres… et Napoléon, qu'il dessine en « petit Boney » colérique : c'est en partie à cause de lui que l'on croit encore que Napoléon était très petit ! En 1841 naît le magazine satirique **Punch**, qui donne au mot *cartoon* son sens moderne de dessin humoristique. Depuis 1961, le magazine *Private Eye* perpétue cette tradition, et les marionnettes de l'émission *Spitting Image* ont caricaturé les dirigeants à la télévision.

## Aux États-Unis : Thomas Nast
Dans les années 1870, le dessinateur **Thomas Nast** attaque dans *Harper's Weekly* la corruption de William « Boss » Tweed, qui contrôle la politique new-yorkaise. Ses dessins, compris même par ceux qui ne savent pas lire, contribuent à la chute de Tweed. Nast a aussi popularisé l'**âne** des démocrates, l'**éléphant** des républicains, et l'image moderne du Père Noël.

## Le photojournalisme : montrer pour faire réagir
- Le photographe **Lewis Hine** dénonce le travail des enfants au début du 20e siècle.
- En 1936, **Dorothea Lange** photographie une mère de famille pauvre entourée de ses enfants dans un camp de travailleurs agricoles : *Migrant Mother* devient le symbole de la Grande Dépression.
- **Robert Capa** photographie le débarquement du 6 juin 1944 depuis les vagues d'Omaha Beach.
- Le magazine *Life* (1936) fait de la photo le cœur de l'information. Pendant la guerre du **Vietnam**, des images de civils victimes de la guerre retournent une partie de l'opinion américaine contre le conflit.
- En 1968, la photo *Earthrise*, prise depuis la Lune, montre la Terre fragile au-dessus de l'horizon lunaire et devient un symbole écologiste.

## Pouvoir et dangers de l'image
Le dessin de presse et la photo peuvent dénoncer, faire rire, émouvoir et pousser à agir. Ils dérangent les puissants : des dessinateurs ont été censurés, emprisonnés, et même tués, comme lors de l'attentat contre *Charlie Hebdo* à Paris en 2015, qui a ému le monde entier et relancé le débat sur la liberté d'expression et ses limites. Aujourd'hui, chacun peut devenir témoin avec son smartphone : en 2020, la vidéo de la mort de George Floyd filmée par une adolescente a changé l'histoire. Mais les images peuvent aussi être recadrées, sorties de leur contexte ou fabriquées par l'intelligence artificielle : il faut apprendre à les **décrypter**.
[→ Voir aussi : l'art de Turner à Banksy](cu_art.html)
""", """
a cartoon = un dessin humoristique
a cartoonist = un dessinateur
a photo = une photo
a photographer = un photographe
a newspaper = un journal
to laugh at = se moquer de
power = le pouvoir
freedom of speech = la liberté d'expression
""", [
 ("Que dénonce Hogarth dans Gin Lane ?", ["Les ravages de l'alcool bon marché", "La guerre", "La monarchie"], ""),
 ("Pourquoi croit-on que Napoléon était très petit ?", ["En partie à cause des caricatures de Gillray", "Parce que c'est vrai", "À cause d'un film"], ""),
 ("Qu'a obtenu Thomas Nast par ses dessins ?", ["La chute du politicien corrompu Boss Tweed", "Un poste de président", "Rien"], ""),
 ("Que symbolise Migrant Mother ?", ["La Grande Dépression", "La guerre du Vietnam", "La conquête spatiale"], ""),
 ("Que montre la photo Earthrise ?", ["La Terre vue depuis la Lune", "Un lever de soleil à Londres", "Une tempête"], ""),
 ("Pourquoi faut-il apprendre à décrypter les images ?", ["Elles peuvent être recadrées, détournées ou fabriquées par IA", "Elles sont toujours vraies", "Elles sont illégales"], ""),
], [("**William Hogarth**", "peintre et graveur anglais, 1697-1764"), ("**Thomas Nast**", "dessinateur américain d'origine allemande"), ("**Dorothea Lange**", "photographe américaine")])
D = "ca"
culture(F, "Culture : Cartoons and photojournalism", 'Cartoons <span>&amp; photos</span>',
  "Culture · caricature, dessin de presse et photojournalisme", ("#fef08a", "#1f2937"),
  reperes("Caricatures et photos de presse ont souvent défié le pouvoir et changé l'opinion publique. Elles posent la question de la liberté d'expression.",
    [("1751", "Gin Lane de Hogarth"), ("1841", "le magazine Punch"), ("1871", "Thomas Nast contre Boss Tweed"),
     ("1936", "Migrant Mother de Dorothea Lange"), ("1968", "la photo Earthrise"), ("2015", "attentat contre Charlie Hebdo")],
    "a cartoon, a caricature, satire, a photojournalist, a newspaper, freedom of speech, censorship, to expose"),
  {D: doc("The power of pictures", [
    "In the 18th century, British artists like William Hogarth used funny drawings to criticise society. Later, the magazine Punch gave the word \"cartoon\" its modern meaning.",
    "In the USA, Thomas Nast drew cartoons against a corrupt politician. Even people who could not read understood them. The politician lost his power.",
    "Photos can also change history. In 1936, Dorothea Lange's photo Migrant Mother showed the poverty of the Great Depression.",
    "During the Vietnam War, photos of civilians shocked many Americans and changed public opinion.",
    "Cartoonists and photographers are sometimes attacked because they criticise powerful people. Today, we must also be careful, because images can be edited or created with AI."])},
  [TF(D, "William Hogarth used drawings to criticise society.", True, "« to criticise society »."),
   TF(D, "Thomas Nast's cartoons were only for educated people.", False, "« Even people who could not read understood them »."),
   TF(D, "Migrant Mother showed the Great Depression.", True, "« the poverty of the Great Depression »."),
   TF(D, "Photos of the Vietnam War had no effect.", False, "« changed public opinion »."),
   TF(D, "Cartoonists are never attacked.", False, "« sometimes attacked »."),
   TF(D, "Images can be created with AI.", True, "« created with AI »." )],
  [Q(D, "What did Punch magazine do?", ["It gave \"cartoon\" its modern meaning.", "It invented photography.", "It sold cars."]),
   Q(D, "Why were Nast's cartoons powerful?", ["Even people who could not read understood them.", "They were very long.", "They were secret."]),
   Q(D, "What did Migrant Mother show?", ["Poverty during the Great Depression.", "A rich family.", "A war."]),
   Q(D, "Why must we be careful with images today?", ["They can be edited or created with AI.", "They are too small.", "They are always true."])],
  [DT(D, "Quel animal symbolise les républicains ?", ["L'éléphant", "L'âne", "L'aigle", "Le lion"]),
   DT(D, "Qui a photographié le débarquement à Omaha Beach ?", ["Robert Capa", "Lewis Hine", "Dorothea Lange", "Banksy"]),
   DT(D, "Quel magazine satirique britannique existe depuis 1961 ?", ["Private Eye", "Punch", "The Sun", "Life"]),
   DT(D, "Comment dit-on « la liberté d'expression » ?", ["Freedom of speech", "Free expression card", "Liberty of talking", "Speech free"])],
  [W(D, "Trouve le mot qui veut dire « critiquer ».", "criticise"), W(D, "Trouve le mot qui veut dire « corrompu ».", "corrupt"),
   W(D, "Trouve le mot qui veut dire « la pauvreté ».", "poverty"), W(D, "Trouve le mot qui veut dire « l'opinion publique » (2 mots).", ["public opinion"])])

# ═════════ LOGEMENT ═════════
F = "cu_logement.html"
DZ(F, """
## « An Englishman's home is his castle »
Au Royaume-Uni, être propriétaire de sa maison est un rêve et un marqueur social très fort. On parle de monter sur l'« échelle de la propriété » (**property ladder**). Ce rêve s'enracine dans une longue histoire où la terre et les grandes demeures appartenaient à une petite aristocratie, la **gentry**.

## Les logements sociaux britanniques
Au 19e siècle, les ouvriers vivent dans des taudis (**slums**) insalubres. Après la Première Guerre mondiale, le gouvernement promet des « logements dignes de héros » et commence à construire des **council houses**, logements sociaux gérés par les communes. Après 1945, la construction explose : à la fin des années 1970, environ un tiers des Britanniques vivent dans un logement social, souvent dans de grands ensembles ou des tours (**tower blocks**).
En 1980, **Margaret Thatcher** lance le **Right to Buy** : les locataires peuvent acheter leur logement social à prix réduit. Près de deux millions de familles deviennent propriétaires, mais le parc social diminue fortement et n'est pas remplacé, ce qui contribue à la crise actuelle.

## La crise du logement
Aujourd'hui, les prix de l'immobilier, surtout à Londres, sont tellement élevés que beaucoup de jeunes ne peuvent plus acheter et restent locataires ou chez leurs parents : on parle de **Generation Rent**. Le 14 juin 2017, l'incendie de la **tour Grenfell**, un immeuble de logements sociaux de Londres, fait 72 morts : le revêtement inflammable posé sur la façade a propagé le feu. L'enquête publique a dénoncé des décennies d'erreurs et de négligences, et beaucoup y ont vu le symbole du mépris envers les habitants pauvres. Pour favoriser la **mixité sociale**, les nouveaux projets immobiliers doivent souvent inclure une part de logements abordables.

## Aux États-Unis : banlieues et ségrégation
Après 1945, les Américains s'installent massivement dans les **suburbs** : à Levittown, près de New York, des milliers de maisons identiques sont construites à la chaîne. Mais l'accès n'est pas le même pour tous. Dans les années 1930, des cartes officielles colorient en rouge les quartiers noirs et immigrés, jugés « à risque », où les banques refusent de prêter : c'est le **redlining**. Beaucoup de lotissements interdisent même la vente aux familles noires. Cette ségrégation résidentielle, interdite en 1968 par le **Fair Housing Act**, a laissé des traces durables : écarts de richesse, écoles inégales. Les grands ensembles de logements publics (**projects**), comme Cabrini-Green à Chicago, ont souvent concentré la pauvreté avant d'être démolis.
Aujourd'hui, la **gentrification** transforme des quartiers populaires (Brooklyn, San Francisco) : de nouveaux habitants plus aisés arrivent, les loyers montent, les anciens habitants doivent partir. Et le nombre de sans-abri a atteint un niveau record.
[→ Voir aussi : classes sociales au Royaume-Uni](cu_classes_uk.html)
""", """
a house = une maison
a flat = un appartement
rent = le loyer
a tenant = un locataire
an owner = un propriétaire
a neighbourhood = un quartier
a tower block = une tour d'habitation
homeless = sans-abri
""", [
 ("Que signifie « property ladder » ?", ["L'échelle de la propriété immobilière", "Une échelle de pompier", "Un escalier"], ""),
 ("Qu'est-ce que le Right to Buy de 1980 ?", ["Le droit pour les locataires d'acheter leur logement social", "Le droit de faire du shopping", "Une loi sur les voitures"], ""),
 ("Quelle a été la conséquence du Right to Buy ?", ["Le parc de logements sociaux a fortement diminué", "Plus de logements sociaux", "Aucune"], ""),
 ("Que s'est-il passé à la tour Grenfell en 2017 ?", ["Un incendie a fait 72 morts", "Elle a été inaugurée", "Elle a été vendue"], ""),
 ("Qu'est-ce que le redlining ?", ["Le refus des banques de prêter dans les quartiers noirs et immigrés", "Un code de la route", "Une couleur de maison"], ""),
 ("Qu'est-ce que la gentrification ?", ["L'arrivée d'habitants aisés qui fait monter les loyers", "La construction de châteaux", "La baisse des prix"], ""),
], [("gentry", "petite noblesse terrienne"), ("Levittown", "banlieue construite à la chaîne près de New York")])
D = "lo"
culture(F, "Culture : Housing and social mix", 'Housing <span>&amp; social mix</span>',
  "Culture · council houses, Grenfell, redlining et gentrification", ("#d6d3d1", "#991b1b"),
  reperes("Le logement révèle les inégalités sociales et raciales au Royaume-Uni comme aux États-Unis.",
    [("1919", "premiers grands programmes de logements sociaux britanniques"), ("années 1930", "le redlining aux États-Unis"), ("1947", "Levittown"),
     ("1968", "Fair Housing Act"), ("1980", "Right to Buy"), ("14 juin 2017", "incendie de la tour Grenfell")],
    "housing, a council house, a tenant, a homeowner, rent, gentrification, segregation, affordable"),
  {D: doc("Home sweet home?", [
    "In Britain, owning your home is a big dream. After the world wars, the government built many council houses for working-class families.",
    "In 1980, Margaret Thatcher allowed tenants to buy their council houses. Many families became owners, but there were fewer social houses for the next generations.",
    "Today, houses are so expensive that many young people cannot buy one. In 2017, a fire in Grenfell Tower, a council tower block in London, killed 72 people.",
    "In the USA, many families moved to the suburbs after 1945. But for a long time, Black families were not allowed to live in many neighbourhoods.",
    "Today, in some poor neighbourhoods, richer people arrive and rents go up. This is called gentrification."])},
  [TF(D, "Owning a home is a big dream in Britain.", True, "« a big dream »."),
   TF(D, "Thatcher allowed tenants to buy their council houses.", True, "« allowed tenants to buy »."),
   TF(D, "Houses are cheap for young people today.", False, "« so expensive »."),
   TF(D, "The Grenfell fire killed 72 people.", True, "« killed 72 people »."),
   TF(D, "Black families could live anywhere in the USA.", False, "« not allowed to live in many neighbourhoods »."),
   TF(D, "Gentrification makes rents go down.", False, "« rents go up »." )],
  [Q(D, "What are council houses?", ["Social houses built for working-class families.", "Castles.", "Hotels."]),
   Q(D, "What was the consequence of Thatcher's policy?", ["Fewer social houses for the next generations.", "More castles.", "Cheaper houses."]),
   Q(D, "What happened at Grenfell Tower?", ["A fire killed 72 people.", "A party.", "A royal visit."]),
   Q(D, "What is gentrification?", ["Richer people arrive and rents go up.", "Houses become free.", "A new garden."])],
  [DT(D, "Comment appelle-t-on les jeunes qui ne peuvent que louer ?", ["Generation Rent", "Generation Z", "Baby Boomers", "Generation Home"]),
   DT(D, "Quelle loi de 1968 interdit la discrimination dans le logement ?", ["Le Fair Housing Act", "Le Right to Buy", "Le Civil Rights Act de 1866", "Le New Deal"]),
   DT(D, "Comment s'appelle la banlieue construite à la chaîne près de New York ?", ["Levittown", "Poundbury", "Bournville", "Brooklyn"]),
   DT(D, "Comment dit-on « un locataire » ?", ["A tenant", "A tenet", "A renter-owner", "A lodger-man"])],
  [W(D, "Trouve le mot qui veut dire « posséder ».", "owning"), W(D, "Trouve le mot qui veut dire « moins de » (pluriel).", "fewer"),
   W(D, "Trouve le mot qui veut dire « une tour d'habitation » (2 mots).", ["tower block"]), W(D, "Trouve le mot qui veut dire « augmentent » (2 mots).", ["go up"])])

# ═════════ MÉMOIRE ═════════
F = "cu_memoire.html"
DZ(F, """
## Le 11 novembre et le coquelicot
Au Royaume-Uni et dans le Commonwealth, la fin de la Première Guerre mondiale est commémorée le **11 novembre**, **Remembrance Day**, et le dimanche le plus proche, **Remembrance Sunday**. À 11 heures, tout s'arrête pour **deux minutes de silence**. À Londres, le roi dépose une couronne de coquelicots devant le **Cenotaph**, un monument « au tombeau vide » inauguré en 1920. Le **poppy** (coquelicot), inspiré du poème du Canadien John McCrae sur les fleurs qui poussaient dans les champs de bataille des Flandres, est porté à la boutonnière par des millions de personnes ; les dons servent à aider les anciens combattants.

## Anzac Day et Vimy
- En Australie et en Nouvelle-Zélande, le **25 avril**, **Anzac Day**, commémore le débarquement de 1915 à Gallipoli, en Turquie, une bataille sanglante devenue un moment fondateur de l'identité de ces deux nations. Les cérémonies commencent à l'aube (**dawn service**).
- Les Canadiens considèrent la bataille de la crête de **Vimy**, en 1917, dans le Pas-de-Calais, comme la naissance de leur nation. Un immense mémorial y a été inauguré en 1936.
- La **Commonwealth War Graves Commission** entretient les tombes de 1,7 million de soldats du Commonwealth dans plus de 150 pays, dont des centaines de cimetières en France, dans la Somme ou en Normandie.
- Aux États-Unis, le **Memorial Day**, dernier lundi de mai, honore les soldats morts au combat ; le **Vietnam Veterans Memorial** à Washington (1982), un long mur noir où sont gravés les noms de plus de 58 000 morts, a inventé une nouvelle forme de mémorial, sobre et propice au recueillement.

## La mémoire de l'esclavage et de la colonisation
Les pages sombres de l'histoire ont mis plus de temps à être commémorées.
- En 2007, pour le bicentenaire de l'abolition de la traite britannique, Liverpool, ancien grand port négrier, ouvre l'**International Slavery Museum**.
- À Washington, le musée national d'histoire et de culture afro-américaines ouvre en 2016 ; en Alabama, un mémorial ouvert en 2018 rend hommage aux milliers de victimes de lynchages.
- Les **statues** de personnalités liées à l'esclavage ou à la colonisation font débat : en 2020, à Bristol, des manifestants jettent dans le port la statue du marchand d'esclaves Edward Colston, aujourd'hui exposée dans un musée. Faut-il déboulonner, contextualiser ou conserver ?
- En Australie et au Canada, des journées et des commissions de réconciliation reconnaissent les souffrances infligées aux peuples autochtones.

## Construire des « lieux de mémoire »
L'historien français Pierre Nora a appelé **lieux de mémoire** les monuments, les dates, les symboles par lesquels une société construit sa mémoire collective. Commémorer, c'est choisir ce que l'on veut transmettre : les héros, mais aussi les victimes ; la fierté, mais aussi la honte. Ces choix évoluent avec chaque génération.
[→ Voir aussi : la Première Guerre mondiale et le poppy](cu_ww1.html)
""", """
a memorial = un mémorial
a poppy = un coquelicot
a soldier = un soldat
a grave = une tombe
silence = le silence
a statue = une statue
to remember = se souvenir
a victim = une victime
""", [
 ("Que fait-on à 11 heures le 11 novembre au Royaume-Uni ?", ["Deux minutes de silence", "Un feu d'artifice", "Un match de football"], ""),
 ("D'où vient le symbole du coquelicot ?", ["Du poème de John McCrae sur les champs de bataille des Flandres", "D'une publicité", "D'une fleur nationale anglaise"], ""),
 ("Que commémore Anzac Day ?", ["Le débarquement de Gallipoli en 1915", "La fin de la guerre de Sécession", "L'indépendance australienne"], ""),
 ("Pourquoi Vimy est-il important pour le Canada ?", ["Cette bataille de 1917 est vue comme la naissance de la nation", "C'est une ville canadienne", "C'est là qu'est né le hockey"], ""),
 ("Qu'est-il arrivé à la statue d'Edward Colston en 2020 ?", ["Des manifestants l'ont jetée dans le port de Bristol", "Elle a été dorée", "Elle a été déplacée à Londres"], ""),
 ("Qu'est-ce qu'un « lieu de mémoire » ?", ["Un monument, une date ou un symbole qui construit la mémoire collective", "Un cimetière seulement", "Une bibliothèque"], ""),
], [("John McCrae", "médecin et poète canadien, 1872-1918"), ("Gallipoli", "péninsule de Turquie"), ("Pierre Nora", "historien français, 1931-2025")])
D = "me"
culture(F, "Culture : Memory and commemoration", 'Memory <span>&amp; remembrance</span>',
  "Culture · Remembrance Day, Anzac Day, Vimy et la mémoire de l'esclavage", ("#fca5a5", "#14532d"),
  reperes("Le monde anglophone commémore ses soldats, mais aussi, de plus en plus, les victimes de l'esclavage et de la colonisation.",
    [("11 novembre", "Remembrance Day"), ("25 avril", "Anzac Day"), ("1917", "bataille de Vimy"), ("1920", "le Cenotaph de Londres"),
     ("1982", "le Vietnam Veterans Memorial"), ("2007", "l'International Slavery Museum de Liverpool")],
    "remembrance, a memorial, a commemoration, a poppy, a veteran, a statue, collective memory, reconciliation"),
  {D: doc("Lest we forget", [
    "Every year on 11 November, the UK and the Commonwealth remember the soldiers who died in wars. At 11 o'clock, people stop for two minutes of silence. Millions wear a red poppy.",
    "In Australia and New Zealand, Anzac Day, on 25 April, remembers the battle of Gallipoli in 1915. In Canada, the battle of Vimy, in France, is seen as the birth of the nation.",
    "In the USA, Memorial Day honours soldiers who died. The Vietnam Veterans Memorial is a black wall with the names of more than 58,000 dead.",
    "Today, countries also remember darker pages of history, like slavery. There is a slavery museum in Liverpool, a former slave-trade port.",
    "Some statues of slave traders have been removed. People disagree: should we remove them, explain them or keep them?"])},
  [TF(D, "People stop for two minutes of silence at 11 o'clock.", True, "« two minutes of silence »."),
   TF(D, "People wear a blue poppy.", False, "« a red poppy »."),
   TF(D, "Anzac Day remembers the battle of Gallipoli.", True, "« the battle of Gallipoli in 1915 »."),
   TF(D, "The battle of Vimy took place in Canada.", False, "« the battle of Vimy, in France »."),
   TF(D, "There is a slavery museum in Liverpool.", True, "« a slavery museum in Liverpool »."),
   TF(D, "Everybody agrees about statues.", False, "« People disagree »." )],
  [Q(D, "What do millions of people wear in November?", ["A red poppy.", "A green hat.", "A white rose."]),
   Q(D, "What is the Vietnam Veterans Memorial?", ["A black wall with the names of the dead.", "A statue of a general.", "A museum of planes."]),
   Q(D, "Why is Liverpool's museum important?", ["Liverpool was a former slave-trade port.", "Liverpool won a war.", "It is the oldest museum."]),
   Q(D, "What is the debate about statues?", ["Should we remove, explain or keep them?", "Should they be bigger?", "Should they be painted?"])],
  [DT(D, "Comment s'appelle le monument aux morts de Londres ?", ["Le Cenotaph", "Big Ben", "Nelson's Column", "Marble Arch"]),
   DT(D, "Quand a lieu Memorial Day aux États-Unis ?", ["Le dernier lundi de mai", "Le 4 juillet", "Le 11 novembre", "Le 25 avril"]),
   DT(D, "Qui a écrit le poème à l'origine du poppy ?", ["John McCrae", "Wilfred Owen", "Rudyard Kipling", "Wordsworth"]),
   DT(D, "Comment dit-on « un ancien combattant » ?", ["A veteran", "An old soldier-man", "A combatant", "A retired war"])],
  [W(D, "Trouve le mot qui veut dire « se souviennent de ».", "remember"), W(D, "Trouve le mot qui veut dire « la naissance ».", "birth"),
   W(D, "Trouve le mot qui veut dire « honore ».", "honours"), W(D, "Trouve le mot qui veut dire « retirées, enlevées ».", "removed")])

# ═════════ ESPACE ═════════
F = "cu_espace_qui.html"
DZ(F, """
## Un traité pour l'espace
En pleine guerre froide, alors que les États-Unis et l'URSS se lancent dans la course à la Lune, l'ONU fait adopter en **1967** le **Outer Space Treaty**. Il pose des principes encore en vigueur : l'espace est « l'apanage de l'humanité tout entière » ; aucun pays ne peut s'approprier la Lune ou un autre corps céleste ; les armes nucléaires sont interdites en orbite ; les États sont responsables des activités de leurs entreprises. Quand Neil Armstrong plante le drapeau américain sur la Lune en 1969, cela ne fait donc pas de la Lune un territoire des États-Unis.

## La nouvelle course à l'espace
Depuis les années 2000, l'espace n'est plus réservé aux États.
- **SpaceX**, l'entreprise d'Elon Musk fondée en 2002, a révolutionné le secteur avec des fusées réutilisables qui reviennent se poser verticalement. Elle transporte des astronautes vers la Station spatiale internationale et déploie des milliers de satellites **Starlink** pour fournir Internet partout sur Terre.
- **Blue Origin**, l'entreprise de Jeff Bezos, et **Virgin Galactic**, celle du Britannique Richard Branson, proposent des vols de **tourisme spatial** à des clients très riches.
- La NASA a lancé le programme **Artemis**, qui vise à renvoyer des humains sur la Lune, y compris pour la première fois une femme, puis à y installer une présence durable. La Chine prépare aussi ses propres missions lunaires habitées.

## À qui appartiennent les ressources de l'espace ?
La Lune et les astéroïdes contiennent de l'eau gelée (utile pour fabriquer du carburant) et des métaux rares. En 2015, une loi américaine autorise les entreprises américaines à posséder les ressources qu'elles extraient de l'espace. En 2020, les États-Unis lancent les **Artemis Accords**, des principes pour l'exploration de la Lune, signés depuis par des dizaines de pays, dont la France ; mais la Chine et la Russie n'y participent pas. Certains y voient une manière de contourner l'esprit du traité de 1967 ; d'autres, un cadre nécessaire pour éviter les conflits.

## Les problèmes de l'espace encombré
- Les **space debris** : des millions de débris (vieux satellites, morceaux de fusées) tournent autour de la Terre à grande vitesse et menacent les satellites et les astronautes.
- Les milliers de satellites des « méga-constellations » gênent les observations des astronomes.
- La domination de quelques milliardaires et de quelques pays pose la question de la gouvernance : qui décide pour l'humanité ?
- L'espace devient aussi un enjeu militaire : plusieurs pays, dont les États-Unis avec leur Space Force créée en 2019, ont des forces spatiales.
[→ Voir aussi : la conquête spatiale](cu_conquete_spatiale.html)
""", """
space = l'espace
the Moon = la Lune
a rocket = une fusée
a satellite = un satellite
a treaty = un traité
to own = posséder
a resource = une ressource
an astronaut = un astronaute
""", [
 ("Que dit le traité de 1967 ?", ["Aucun pays ne peut s'approprier la Lune", "La Lune appartient aux États-Unis", "L'espace est interdit"], ""),
 ("Qu'a révolutionné SpaceX ?", ["Les fusées réutilisables", "Les avions", "Les voitures"], ""),
 ("Qu'est-ce que le tourisme spatial ?", ["Des vols dans l'espace pour des clients très riches", "Des voyages en avion", "Des musées de l'espace"], ""),
 ("Que permet la loi américaine de 2015 ?", ["Que les entreprises possèdent les ressources qu'elles extraient de l'espace", "Que tout le monde aille sur la Lune", "Interdire les fusées"], ""),
 ("Quel danger représentent les débris spatiaux ?", ["Ils menacent les satellites et les astronautes", "Ils tombent sur les villes chaque jour", "Aucun"], ""),
 ("Quelle question de gouvernance se pose ?", ["Qui décide pour l'humanité ?", "Qui paie les billets ?", "Qui construit les stades ?"], ""),
], [("Neil Armstrong", "premier homme sur la Lune, 1969"), ("Artemis", "programme lunaire de la NASA")])
D = "eq"
culture(F, "Culture : Who owns space?", 'Who owns <span>space?</span>',
  "Culture · traités, milliardaires et ressources de l'espace", ("#c7d2fe", "#111827"),
  reperes("Depuis 1967, aucun pays ne peut s'approprier la Lune. Mais l'arrivée des entreprises privées et la course aux ressources posent de nouvelles questions.",
    [("1967", "le traité sur l'espace extra-atmosphérique"), ("1969", "premiers pas sur la Lune"), ("2002", "création de SpaceX"),
     ("2015", "loi américaine sur les ressources spatiales"), ("2019", "création de la Space Force américaine"), ("2020", "les Artemis Accords")],
    "space, a treaty, a satellite, a rocket, space debris, a resource, space tourism, governance"),
  {D: doc("Space for everyone?", [
    "In 1967, a treaty decided that no country can own the Moon or the planets. Space belongs to all humanity.",
    "Today, private companies are very active in space. SpaceX, created by Elon Musk, makes rockets that can land and be used again. Some companies even sell space trips to rich tourists.",
    "The Moon has ice and rare metals. In 2015, the USA allowed its companies to own the resources they take from space. Some people think this goes against the spirit of the treaty.",
    "There are other problems: millions of pieces of space debris turn around the Earth and can damage satellites.",
    "The big question is: who should decide what we do in space, and for whom?"])},
  [TF(D, "A country can own the Moon.", False, "« no country can own the Moon »."),
   TF(D, "SpaceX was created by Elon Musk.", True, "« created by Elon Musk »."),
   TF(D, "Some companies sell space trips to tourists.", True, "« sell space trips to rich tourists »."),
   TF(D, "The Moon has no resources.", False, "« ice and rare metals »."),
   TF(D, "Space debris can damage satellites.", True, "« can damage satellites »."),
   TF(D, "Everybody agrees about the American law of 2015.", False, "« Some people think this goes against… »." )],
  [Q(D, "What did the 1967 treaty decide?", ["No country can own the Moon.", "The Moon is American.", "Space is closed."]),
   Q(D, "What is special about SpaceX rockets?", ["They can land and be used again.", "They are made of wood.", "They are very small."]),
   Q(D, "What did the USA allow in 2015?", ["Companies can own resources taken from space.", "Everyone can fly to Mars.", "Satellites are forbidden."]),
   Q(D, "What is space debris?", ["Pieces of old satellites and rockets.", "Stars.", "Planets."])],
  [DT(D, "Quel milliardaire a fondé Blue Origin ?", ["Jeff Bezos", "Elon Musk", "Richard Branson", "Bill Gates"]),
   DT(D, "Comment s'appelle le programme lunaire de la NASA ?", ["Artemis", "Apollo 2", "Gemini", "Starlink"]),
   DT(D, "Quel Britannique a fondé Virgin Galactic ?", ["Richard Branson", "Tim Berners-Lee", "Alan Turing", "David Attenborough"]),
   DT(D, "Comment dit-on « débris spatiaux » ?", ["Space debris", "Space rubbish only", "Star dust", "Space bits"])],
  [W(D, "Trouve le mot qui veut dire « l'humanité ».", "humanity"), W(D, "Trouve le mot qui veut dire « atterrir ».", "land"),
   W(D, "Trouve le mot qui veut dire « les ressources ».", "resources"), W(D, "Trouve le mot qui veut dire « endommager ».", "damage")])

# ═════════ FRANKENSTEIN & ÉTHIQUE ═════════
F = "cu_frankenstein.html"
DZ(F, """
## Frankenstein, né d'un défi
En juin 1816, l'« année sans été » (une éruption volcanique a assombri le ciel), un groupe d'écrivains anglais est bloqué par la pluie dans une villa au bord du lac Léman, en Suisse : le poète Lord Byron, Percy Shelley et sa compagne, **Mary**, 18 ans. Byron propose un défi : écrire chacun une histoire de fantômes. Mary imagine celle d'un savant qui donne vie à une créature. Publié en **1818**, **Frankenstein, or the Modern Prometheus** est souvent considéré comme le premier roman de **science-fiction**.

## Le savant et sa créature
Le jeune scientifique **Victor Frankenstein**, fasciné par les découvertes sur l'électricité, assemble un corps à partir de morceaux de cadavres et parvient à l'animer. Mais horrifié par l'apparence de sa créature, il l'abandonne aussitôt. La créature, intelligente et sensible, apprend seule à parler et à lire ; rejetée par tous à cause de son aspect, elle devient violente et se venge de son créateur. Attention : **Frankenstein** est le nom du savant, pas du monstre, qui n'a pas de nom ! Le sous-titre fait référence à **Prométhée**, le titan qui vola le feu aux dieux : le roman interroge l'orgueil de l'homme qui veut jouer à Dieu et sa **responsabilité** envers ce qu'il crée.

## La quête de l'homme parfait : l'eugénisme
À la fin du 19e siècle, Francis Galton, cousin de Darwin, invente le mot **eugenics** : l'idée d'« améliorer » l'espèce humaine en favorisant la reproduction des personnes jugées « supérieures ». Au début du 20e siècle, plus de trente États américains adoptent des lois de **stérilisation forcée** visant des personnes handicapées, pauvres ou issues de minorités ; plus de 60 000 Américains en sont victimes, et la Cour suprême les valide en 1927. L'Allemagne nazie s'en inspire, jusqu'au meurtre de masse. Après 1945, l'eugénisme est condamné, mais la question revient avec les progrès de la génétique.

## Des progrès qui posent des questions
- En **1978**, au Royaume-Uni, naît **Louise Brown**, le premier « bébé-éprouvette » conçu par fécondation in vitro : une révolution pour les couples infertiles, critiquée à l'époque comme contre nature.
- En **1996**, à l'Institut Roslin, en Écosse, naît **Dolly**, la première brebis clonée à partir d'une cellule adulte.
- En 2003, le génome humain est entièrement décrypté.
- En 2012, l'Américaine Jennifer Doudna et la Française Emmanuelle Charpentier mettent au point **CRISPR**, des « ciseaux génétiques » qui permettent de modifier l'ADN ; elles reçoivent le prix Nobel en 2020. Ces outils pourraient guérir des maladies génétiques, mais en 2018, un chercheur chinois a modifié l'ADN de bébés, ce qui a provoqué un scandale mondial.

## Les débats éthiques
Peut-on choisir les caractéristiques de ses enfants (**designer babies**) ? Qui aura accès à ces technologies ? Où s'arrête la médecine et où commence l'« amélioration » de l'humain ? Comme Victor Frankenstein, les scientifiques d'aujourd'hui doivent se demander non seulement « peut-on le faire ? », mais aussi « doit-on le faire ? ».
[→ Voir aussi : les dystopies, de Brave New World à 1984](cu_dystopies.html)
""", """
a scientist = un scientifique
a creature = une créature
a monster = un monstre
a novel = un roman
life = la vie
a gene = un gène
to create = créer
responsible = responsable
""", [
 ("Comment Mary Shelley a-t-elle eu l'idée de Frankenstein ?", ["Lors d'un défi d'histoires de fantômes avec Byron", "En lisant un journal", "En regardant un film"], ""),
 ("Qui s'appelle Frankenstein ?", ["Le savant, pas la créature", "Le monstre", "Le village"], ""),
 ("Pourquoi la créature devient-elle violente ?", ["Elle est abandonnée et rejetée par tous", "Elle est née méchante", "Elle a faim"], ""),
 ("Qu'est-ce que l'eugénisme ?", ["L'idée d'« améliorer » l'espèce humaine en contrôlant la reproduction", "Une science du climat", "Une forme d'art"], ""),
 ("Qui est Dolly ?", ["La première brebis clonée, en Écosse en 1996", "Une chanteuse", "Un bébé-éprouvette"], ""),
 ("Quelle question doivent se poser les scientifiques ?", ["Non seulement « peut-on le faire ? » mais aussi « doit-on le faire ? »", "Combien cela rapporte ?", "Aucune"], ""),
], [("Lord Byron", "poète romantique anglais"), ("Prométhée", "titan de la mythologie grecque"), ("Francis Galton", "savant britannique, 1822-1911")])
D = "fk"
culture(F, "Culture : Frankenstein and the perfect human", 'Frankenstein <span>&amp; science</span>',
  "Culture · Mary Shelley, l'eugénisme, Dolly et CRISPR", ("#86efac", "#1f2937"),
  reperes("Depuis Frankenstein (1818), la littérature interroge la responsabilité des scientifiques. Les progrès de la génétique rendent ces questions très actuelles.",
    [("1818", "Frankenstein de Mary Shelley"), ("1883", "Galton invente le mot « eugenics »"), ("1927", "la Cour suprême valide la stérilisation forcée"),
     ("1978", "Louise Brown, premier bébé-éprouvette"), ("1996", "Dolly, la brebis clonée"), ("2012", "CRISPR, les ciseaux génétiques")],
    "a scientist, a creature, responsibility, ethics, eugenics, cloning, genetic engineering, to play God"),
  {D: doc("Playing God", [
    "Mary Shelley was only 18 when she started writing Frankenstein. It was published in 1818 and is often called the first science fiction novel.",
    "In the novel, Victor Frankenstein, a young scientist, creates a living creature. But he is horrified and abandons it. Rejected by everybody, the creature becomes violent.",
    "In the early 20th century, some people wanted to create \"perfect\" humans. This idea, called eugenics, led to terrible injustices in the USA and in Nazi Germany.",
    "Today, science can do amazing things: in 1996, scientists in Scotland cloned a sheep called Dolly, and new tools can change our genes.",
    "These discoveries can cure diseases, but they also raise ethical questions: just because we can do something, should we do it?"])},
  [TF(D, "Mary Shelley was 18 when she started writing Frankenstein.", True, "« only 18 »."),
   TF(D, "Frankenstein is the name of the creature.", False, "C'est le nom du savant (Victor Frankenstein)."),
   TF(D, "Victor abandons his creature.", True, "« abandons it »."),
   TF(D, "Eugenics led to terrible injustices.", True, "« led to terrible injustices »."),
   TF(D, "Dolly was a cloned cow.", False, "« a sheep called Dolly »."),
   TF(D, "New discoveries raise no ethical questions.", False, "« they also raise ethical questions »." )],
  [Q(D, "Why is Frankenstein important?", ["It is often called the first science fiction novel.", "It is the first poem.", "It is a history book."]),
   Q(D, "Why does the creature become violent?", ["It is rejected by everybody.", "It is hungry.", "It is born violent."]),
   Q(D, "What is eugenics?", ["The idea of creating \"perfect\" humans.", "A type of medicine for animals.", "A sport."]),
   Q(D, "What question do new discoveries raise?", ["Just because we can do something, should we do it?", "How much do they cost?", "Who will win a prize?"])],
  [DT(D, "Où Mary Shelley a-t-elle imaginé son roman ?", ["Au bord du lac Léman, en Suisse", "À Londres", "À Édimbourg", "À Paris"]),
   DT(D, "Quel est le sous-titre de Frankenstein ?", ["The Modern Prometheus", "The Monster", "The Creature", "A Ghost Story"]),
   DT(D, "Où est née Dolly ?", ["En Écosse", "Aux États-Unis", "En France", "En Chine"]),
   DT(D, "Comment dit-on « jouer à Dieu » ?", ["To play God", "To be God", "To make God", "To game God"])],
  [W(D, "Trouve le mot qui veut dire « une créature vivante » (2 mots).", ["living creature", "a living creature"]), W(D, "Trouve le mot qui veut dire « horrifié ».", "horrified"),
   W(D, "Trouve le mot qui veut dire « guérir ».", "cure"), W(D, "Trouve le mot qui veut dire « éthiques ».", "ethical")])
END()
