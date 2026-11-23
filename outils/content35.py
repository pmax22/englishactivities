import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
exec(open(_EA_OUT+"/cuhelp.py", encoding="utf-8").read())

# ═════════ EXPLORATEURS ═════════
F = "cu_explorateurs.html"
DZ(F, """
## James Cook, le cartographe du Pacifique
**James Cook** (1728-1779), fils d'un ouvrier agricole du Yorkshire, devient l'un des plus grands navigateurs de l'histoire. Il mène trois grands voyages pour la Royal Navy :
- **1768-1771**, à bord de l'**Endeavour** : il observe à Tahiti le passage de Vénus devant le Soleil, cartographie les côtes de la Nouvelle-Zélande, puis la côte est de l'Australie, qu'il revendique pour la Couronne britannique en 1770.
- **1772-1775** : il franchit le cercle polaire antarctique et prouve qu'il n'existe pas de grand continent austral habitable.
- **1776-1779** : il cherche un passage au nord du Canada, découvre Hawaï pour les Européens et y est tué en 1779 lors d'un affrontement avec les habitants.
Cook est admiré pour ses cartes très précises et pour avoir protégé ses marins du **scorbut** grâce à une alimentation variée. Mais pour les **Māori** et les **Aborigènes**, son arrivée marque le début de la colonisation : dès 1769, des Māori sont tués lors des premières rencontres. Ses statues sont aujourd'hui l'objet de débats.

## Stanley et Livingstone
**David Livingstone** (1813-1873), missionnaire et médecin écossais, explore l'intérieur de l'Afrique australe et centrale. Il est le premier Européen à voir les chutes qu'il nomme **Victoria Falls** (1855), et il dénonce la traite des esclaves. Mais lors de sa recherche des sources du Nil, il disparaît pendant des années. Le journal américain *New York Herald* envoie un journaliste, **Henry Morton Stanley**, le retrouver. En novembre 1871, à Ujiji, au bord du lac Tanganyika, Stanley l'aborde avec une phrase restée célèbre : « *Dr. Livingstone, I presume?* » Livingstone meurt en Afrique en 1873 ; ses compagnons africains, Chuma et Susi, portent son corps sur des centaines de kilomètres jusqu'à la côte. Stanley, lui, travaillera ensuite pour le roi des Belges Léopold II au Congo, où le système colonial sera d'une brutalité extrême. Ces explorations ont ouvert la voie au « partage de l'Afrique » par les puissances européennes.

## Shackleton et l'Endurance : la fin de l'âge héroïque
En 1914, l'Irlandais **Ernest Shackleton** part avec 27 hommes pour traverser l'Antarctique à pied. Mais son navire, l'**Endurance**, est pris dans les glaces de la mer de Weddell, puis écrasé et englouti en 1915. Les hommes campent des mois sur la banquise, puis rejoignent en canots l'île de l'Éléphant. Shackleton et cinq compagnons parcourent alors environ 1 300 km sur une simple chaloupe, le *James Caird*, dans l'un des océans les plus dangereux du monde, jusqu'à l'île de Géorgie du Sud, qu'ils traversent à pied. Après plusieurs tentatives, il revient chercher tous ses hommes : **les 28 survivent**. L'expédition a échoué, mais elle est devenue un modèle de courage et de **leadership**. L'épave de l'Endurance a été retrouvée en 2022, à plus de 3 000 mètres de profondeur, remarquablement conservée.

## Pourquoi explorer ?
Ces voyages mêlent curiosité scientifique, goût de l'aventure, rivalités entre nations, recherche de richesses et volonté de conquête. Ils ont produit des récits épiques… mais aussi la colonisation et la souffrance des peuples rencontrés.
[→ Voir aussi : la conquête spatiale, la nouvelle exploration](cu_conquete_spatiale.html)
""", """
a ship = un navire
a map = une carte
an explorer = un explorateur
ice = la glace
a journey = un voyage
a sailor = un marin
to survive = survivre
a coast = une côte
""", [
 ("Pourquoi Cook est-il admiré ?", ["Pour ses cartes très précises et la santé de ses marins", "Parce qu'il a découvert l'Amérique", "Parce qu'il était roi"], ""),
 ("Pourquoi son arrivée est-elle critiquée aujourd'hui ?", ["Elle marque le début de la colonisation pour les Māori et les Aborigènes", "Il était trop lent", "Il n'a rien découvert"], ""),
 ("Que dit Stanley en retrouvant Livingstone ?", ["« Dr. Livingstone, I presume? »", "« Hello, my friend! »", "« Land ahoy! »"], ""),
 ("Qu'arrive-t-il à l'Endurance ?", ["Il est écrasé par les glaces", "Il arrive au pôle Sud", "Il coule dans un port"], ""),
 ("Combien d'hommes de Shackleton survivent ?", ["Tous les 28", "Aucun", "La moitié"], ""),
 ("Que nous apprend l'histoire de Shackleton ?", ["Le courage et le leadership face au danger", "Qu'il faut toujours réussir", "Qu'il ne faut jamais voyager"], ""),
], [("Māori", "peuple autochtone de Nouvelle-Zélande"), ("Léopold II", "roi des Belges de 1865 à 1909")])
D = "ex"
culture(F, "Culture : Great explorers", 'Great <span>explorers</span>',
  "Culture · Cook, Livingstone, Stanley et Shackleton", ("#bae6fd", "#78350f"),
  reperes("Aux 18e et 19e siècles, des explorateurs britanniques ont parcouru les océans, l'Afrique et l'Antarctique. Leurs voyages fascinent, mais ont aussi ouvert la voie à la colonisation.",
    [("1768 – 1779", "les trois voyages de James Cook"), ("1770", "Cook revendique la côte est de l'Australie"), ("1855", "Livingstone aux chutes Victoria"),
     ("1871", "Stanley retrouve Livingstone"), ("1914 – 1917", "l'expédition de Shackleton"), ("2022", "découverte de l'épave de l'Endurance")],
    "an explorer, an expedition, a voyage, a map, a coast, ice, to survive, leadership"),
  {D: doc("Into the unknown", [
    "James Cook was a British sailor. In the 18th century, he made three long voyages in the Pacific Ocean and drew very precise maps of New Zealand and Australia. But for Māori and Aboriginal people, his arrival was the beginning of colonisation.",
    "David Livingstone was a Scottish explorer in Africa. He disappeared for years, so a journalist, Henry Morton Stanley, went to find him. When he finally met him in 1871, he said: \"Dr. Livingstone, I presume?\"",
    "In 1914, Ernest Shackleton wanted to cross Antarctica. But his ship, the Endurance, was trapped and crushed by the ice.",
    "Shackleton and five men sailed 1,300 kilometres in a small boat to find help. Then he came back to rescue his men. All 28 survived!",
    "Today, these explorers are admired for their courage, but people also discuss the consequences of their journeys."])},
  [TF(D, "James Cook drew maps of New Zealand and Australia.", True, "« very precise maps of New Zealand and Australia »."),
   TF(D, "Livingstone was an English king.", False, "« a Scottish explorer »."),
   TF(D, "Stanley was a journalist.", True, "« a journalist, Henry Morton Stanley »."),
   TF(D, "The Endurance reached the South Pole.", False, "« trapped and crushed by the ice »."),
   TF(D, "Shackleton abandoned his men.", False, "« he came back to rescue his men »."),
   TF(D, "All 28 men survived.", True, "« All 28 survived! »." )],
  [Q(D, "Where did Cook make his voyages?", ["In the Pacific Ocean.", "In the Arctic.", "In Africa."]),
   Q(D, "Why did Stanley go to Africa?", ["To find Livingstone.", "To find gold.", "To become king."]),
   Q(D, "What happened to the Endurance?", ["It was crushed by the ice.", "It arrived in Australia.", "It became a museum."]),
   Q(D, "Why is Shackleton admired?", ["For his courage and for saving all his men.", "Because he reached the Pole first.", "Because he was rich."])],
  [DT(D, "Comment s'appelle le navire du premier voyage de Cook ?", ["L'Endeavour", "L'Endurance", "Le Mayflower", "Le Beagle"]),
   DT(D, "Quelles chutes Livingstone a-t-il nommées ?", ["Les chutes Victoria", "Les chutes du Niagara", "Les chutes Albert", "Les chutes Elizabeth"]),
   DT(D, "Où Cook est-il tué en 1779 ?", ["À Hawaï", "En Australie", "En Antarctique", "À Tahiti"]),
   DT(D, "Comment s'appelle la chaloupe de Shackleton ?", ["Le James Caird", "Le Carpathia", "L'Endeavour", "Le Victoria"])],
  [W(D, "Trouve le mot qui veut dire « précises ».", "precise"), W(D, "Trouve le mot qui veut dire « a disparu ».", "disappeared"),
   W(D, "Trouve le mot qui veut dire « écrasé ».", "crushed"), W(D, "Trouve le mot qui veut dire « secourir ».", "rescue")])

# ═════════ GRANDS DISCOURS ═════════
F = "cu_grands_discours.html"
DZ(F, """
## Le pouvoir des mots
Certains discours ont changé l'histoire. Leur force vient du moment où ils sont prononcés, de la personnalité de l'orateur et de techniques de **rhetoric** (rhétorique) que l'on retrouve d'un discours à l'autre.

## Abraham Lincoln, Gettysburg (1863)
En pleine guerre de Sécession, Lincoln inaugure un cimetière militaire à Gettysburg. Son discours dure à peine deux minutes et compte environ 270 mots. Il rappelle que la nation est fondée sur l'égalité et appelle à défendre un « *government of the people, by the people, for the people* ». C'est l'un des textes les plus célèbres de l'histoire américaine.

## Emmeline Pankhurst, « Freedom or death » (1913)
La leader des **suffragettes** britanniques explique, devant un public américain, pourquoi les femmes sont prêtes à aller jusqu'au bout pour obtenir le droit de vote.

## Winston Churchill (1940)
Devenu Premier ministre en mai 1940, alors que l'Allemagne nazie envahit l'Europe, Churchill déclare n'avoir rien d'autre à offrir que « du sang, du labeur, des larmes et de la sueur » (« *blood, toil, tears and sweat* »). Quelques semaines plus tard, il promet que les Britanniques se battront sur les plages, dans les champs et dans les rues, et ne se rendront jamais : « *we shall never surrender* ». Ses discours, diffusés à la radio, galvanisent le pays.

## John F. Kennedy (1961)
Dans son discours d'investiture, le jeune président appelle à l'engagement civique : ne pas demander ce que le pays peut faire pour soi, mais ce que l'on peut faire pour son pays (« *Ask not what your country can do for you…* »).

## Martin Luther King, « I have a dream » (1963)
Le **28 août 1963**, devant environ 250 000 personnes réunies devant le Lincoln Memorial lors de la marche sur Washington, le pasteur King rêve d'une Amérique où ses enfants seront jugés sur leur caractère et non sur la couleur de leur peau. Une partie du discours est improvisée, après que la chanteuse Mahalia Jackson lui a crié de parler de son rêve. La répétition de « *I have a dream* » en fait l'un des discours les plus célèbres au monde.

## Barack Obama et Malala Yousafzai
En 2008, la campagne de Barack Obama est portée par un slogan repris en chœur par les foules : « *Yes we can* ». En 2013, le jour de ses 16 ans, la jeune Pakistanaise **Malala Yousafzai**, blessée par les talibans pour avoir défendu l'éducation des filles, prend la parole à l'ONU, à New York. Elle affirme qu'un enfant, un professeur, un stylo et un livre peuvent changer le monde. Elle reçoit le prix Nobel de la paix en 2014, à 17 ans.

## Les techniques des grands orateurs
- **La répétition** (anaphore) : « *I have a dream* », « *we shall fight* »…
- **La règle de trois** : « *of the people, by the people, for the people* ».
- **Les oppositions** : « ne demandez pas… demandez plutôt… ».
- **Les images** (métaphores), l'appel aux émotions, les pauses et le rythme.
Aujourd'hui, la parole politique passe aussi par les réseaux sociaux : messages très courts, slogans, vidéos. Elle touche plus de monde, plus vite, mais laisse moins de place à l'argumentation.
[→ Voir aussi : le mouvement des droits civiques](cu_droits_civiques.html)
""", """
a speech = un discours
a speaker = un orateur
a crowd = une foule
a dream = un rêve
freedom = la liberté
to repeat = répéter
a slogan = un slogan
to inspire = inspirer
""", [
 ("Combien de temps dure le discours de Gettysburg ?", ["Environ deux minutes", "Deux heures", "Une journée"], ""),
 ("Que promet Churchill en 1940 ?", ["Que les Britanniques ne se rendront jamais", "La paix avec l'Allemagne", "Des vacances"], ""),
 ("À quoi appelle Kennedy dans son discours de 1961 ?", ["À l'engagement des citoyens pour leur pays", "À la guerre", "À quitter l'Amérique"], ""),
 ("Où MLK prononce-t-il « I have a dream » ?", ["Devant le Lincoln Memorial, à Washington", "À Londres", "À l'ONU"], ""),
 ("Que défend Malala ?", ["L'éducation des filles", "Le sport", "La guerre"], ""),
 ("Qu'est-ce que l'anaphore ?", ["La répétition d'une expression au début des phrases", "Une métaphore", "Un mensonge"], ""),
], [("Mahalia Jackson", "grande chanteuse de gospel"), ("talibans", "mouvement islamiste armé d'Afghanistan et du Pakistan")])
D = "sp"
culture(F, "Culture : Great speeches", 'Great <span>speeches</span>',
  "Culture · Lincoln, Churchill, Kennedy, King, Malala", ("#fde68a", "#1e3a8a"),
  reperes("Des discours célèbres en anglais ont marqué l'histoire grâce à leur message et à leurs techniques : répétition, règle de trois, images.",
    [("1863", "Lincoln à Gettysburg"), ("1940", "Churchill : « we shall never surrender »"), ("1961", "Kennedy : « Ask not… »"),
     ("28 août 1963", "Martin Luther King : « I have a dream »"), ("2008", "Obama : « Yes we can »"), ("2013", "Malala à l'ONU")],
    "a speech, a speaker, an audience, rhetoric, repetition, a slogan, to persuade, to inspire"),
  {D: doc("Words that changed history", [
    "Some speeches changed history. In 1863, during the Civil War, Abraham Lincoln gave a very short speech at Gettysburg. It lasted only two minutes, but it is still famous today.",
    "In 1940, Britain was in great danger. Winston Churchill told the British people that they would never surrender. His speeches on the radio gave them courage.",
    "On 28 August 1963, Martin Luther King spoke in front of 250,000 people in Washington. He repeated \"I have a dream\" and described an America without racism.",
    "In 2013, Malala Yousafzai, a 16-year-old Pakistani girl, spoke at the United Nations about the right of girls to go to school.",
    "Great speakers use special techniques: they repeat key words, they use groups of three, and they speak to people's emotions."])},
  [TF(D, "Lincoln's speech at Gettysburg was very long.", False, "« only two minutes »."),
   TF(D, "Churchill spoke on the radio.", True, "« His speeches on the radio »."),
   TF(D, "Martin Luther King spoke in front of 250,000 people.", True, "« in front of 250,000 people »."),
   TF(D, "King described an America with more racism.", False, "« an America without racism »."),
   TF(D, "Malala spoke at the United Nations.", True, "« at the United Nations »."),
   TF(D, "Great speakers never repeat words.", False, "« they repeat key words »." )],
  [Q(D, "When did Lincoln speak at Gettysburg?", ["During the Civil War.", "During the Second World War.", "In 2008."]),
   Q(D, "What did Churchill's speeches give the British?", ["Courage.", "Money.", "Food."]),
   Q(D, "What did Malala speak about?", ["The right of girls to go to school.", "Football.", "Music."]),
   Q(D, "Name a technique of great speakers.", ["Repeating key words.", "Speaking very fast.", "Never looking at the audience."])],
  [DT(D, "Quel était le slogan d'Obama en 2008 ?", ["« Yes we can »", "« I have a dream »", "« Never surrender »", "« Ask not »"]),
   DT(D, "Quelle suffragette prononce « Freedom or death » ?", ["Emmeline Pankhurst", "Rosa Parks", "Malala Yousafzai", "Eleanor Roosevelt"]),
   DT(D, "À quel âge Malala reçoit-elle le prix Nobel ?", ["17 ans", "30 ans", "12 ans", "45 ans"]),
   DT(D, "Comment dit-on « se rendre » (capituler) ?", ["To surrender", "To render", "To give", "To return"])],
  [W(D, "Trouve le mot qui veut dire « a duré ».", "lasted"), W(D, "Trouve le mot qui veut dire « le courage ».", "courage"),
   W(D, "Trouve le mot qui veut dire « a répété ».", "repeated"), W(D, "Trouve le mot qui veut dire « les émotions ».", "emotions")])

# ═════════ MARK TWAIN ═════════
F = "cu_mark_twain.html"
DZ(F, """
## Un enfant du Mississippi
**Samuel Clemens** naît en 1835 dans le Missouri et grandit à **Hannibal**, une petite ville au bord du **Mississippi**. Le fleuve est alors une grande autoroute : des **steamboats** (bateaux à vapeur à roues) transportent passagers et marchandises entre le Nord et La Nouvelle-Orléans. Le Missouri est un État esclavagiste, et le jeune Samuel grandit en voyant l'esclavage autour de lui.

## Pilote de bateau à vapeur
Son rêve d'enfant se réalise : en 1859, il devient **pilote de steamboat**. Il doit connaître par cœur chaque courant, chaque banc de sable du fleuve. Pour mesurer la profondeur, un marin lance une corde lestée et crie la mesure : « *mark twain!* » signifie « deux brasses » (environ 3,7 mètres), une profondeur sûre pour le bateau. C'est de là que vient son nom de plume, **Mark Twain**. La guerre de Sécession met fin au trafic sur le fleuve et à sa carrière de pilote. Il raconte ces années dans *Life on the Mississippi* (1883).

## Tom Sawyer et Huckleberry Finn
Devenu journaliste puis écrivain célèbre pour son humour, Twain publie *The Adventures of Tom Sawyer* (1876), inspiré de son enfance à Hannibal. Tom est un garçon malin et rêveur ; dans une scène célèbre, puni et obligé de repeindre une palissade, il fait croire à ses copains que c'est un privilège, si bien qu'ils le paient pour travailler à sa place !
Dans *Adventures of Huckleberry Finn* (1884), son ami **Huck**, un garçon pauvre qui fuit son père violent, descend le Mississippi sur un radeau avec **Jim**, un esclave en fuite. Le voyage sur le fleuve est un **voyage initiatique** : Huck, qui a grandi en croyant qu'aider un esclave à s'enfuir est un péché, découvre l'humanité de Jim et décide de l'aider, quitte à « aller en enfer ». Écrit dans la langue parlée du Sud, avec ses dialectes, le roman a été salué par Hemingway comme l'origine de toute la littérature américaine moderne.

## Un classique qui fait débat
*Huckleberry Finn* est une critique de l'esclavage et du racisme, mais il emploie massivement un mot raciste de l'époque, et son personnage de Jim est parfois jugé caricatural. Le livre a donc été retiré de certains programmes scolaires américains, ce qui alimente le débat sur la façon d'enseigner les classiques. En 2024, le romancier Percival Everett a réécrit l'histoire du point de vue de Jim dans *James*, couronné par le prix Pulitzer.

## Un humoriste
Mark Twain est aussi célèbre pour ses conférences et ses mots d'esprit. Né l'année du passage de la comète de Halley, il avait prédit qu'il mourrait à son retour : il meurt en 1910, l'année où la comète revient.
[→ Voir aussi : la géographie des États-Unis](cu_geographie_usa.html)
""", """
a river = un fleuve
a boat = un bateau
a raft = un radeau
a fence = une palissade
an adventure = une aventure
a writer = un écrivain
a slave = un esclave
to escape = s'enfuir
""", [
 ("Où grandit Samuel Clemens ?", ["À Hannibal, au bord du Mississippi", "À New York", "À Londres"], ""),
 ("D'où vient le nom « Mark Twain » ?", ["Du cri des marins mesurant une profondeur sûre", "Du nom de son père", "D'une ville"], ""),
 ("Que fait Tom Sawyer avec la palissade ?", ["Il fait payer ses copains pour la peindre à sa place", "Il la casse", "Il la vend"], ""),
 ("Avec qui Huck descend-il le fleuve ?", ["Jim, un esclave en fuite", "Tom Sawyer", "Son père"], ""),
 ("Que découvre Huck pendant le voyage ?", ["L'humanité de Jim", "Un trésor", "Une ville d'or"], ""),
 ("Pourquoi Huckleberry Finn fait-il débat ?", ["Il emploie un mot raciste et Jim est parfois jugé caricatural", "Il est trop court", "Il est en français"], ""),
], [("Hemingway", "romancier américain, prix Nobel 1954"), ("Percival Everett", "romancier américain contemporain")])
D = "mt"
culture(F, "Culture : Mark Twain and the Mississippi", 'Mark Twain <span>&amp; the Mississippi</span>',
  "Culture · Tom Sawyer, Huckleberry Finn et les bateaux à vapeur", ("#bae6fd", "#92400e"),
  reperes("Mark Twain (1835-1910) a grandi au bord du Mississippi. Il en a fait le décor de ses romans les plus célèbres.",
    [("1835", "naissance de Samuel Clemens"), ("1859", "il devient pilote de bateau à vapeur"), ("1876", "The Adventures of Tom Sawyer"),
     ("1884", "Adventures of Huckleberry Finn"), ("1910", "mort de Mark Twain"), ("2024", "James, de Percival Everett")],
    "a river, a steamboat, a pilot, a raft, an adventure, a pen name, freedom, a classic"),
  {D: doc("Life on the river", [
    "Mark Twain's real name was Samuel Clemens. He grew up in a small town on the Mississippi River. As a young man, he was a pilot on a steamboat.",
    "Sailors measured the depth of the river and shouted \"mark twain!\" when the water was deep enough. Clemens chose this as his pen name.",
    "In The Adventures of Tom Sawyer, Tom is a clever boy. When he has to paint a fence, he makes his friends do it for him, and they even pay him!",
    "In Huckleberry Finn, Huck travels down the river on a raft with Jim, a slave who is escaping. During the journey, Huck decides to help Jim to be free.",
    "Today, the novel is a classic, but it is also criticised for its racist language."])},
  [TF(D, "Mark Twain's real name was Samuel Clemens.", True, "« His real name was Samuel Clemens »."),
   TF(D, "He was a pilot on a plane.", False, "« a pilot on a steamboat »."),
   TF(D, "\"Mark twain\" meant the water was deep enough.", True, "« when the water was deep enough »."),
   TF(D, "Tom Sawyer pays his friends to paint the fence.", False, "Ce sont ses copains qui le paient."),
   TF(D, "Huck travels on a raft with Jim.", True, "« on a raft with Jim »."),
   TF(D, "Huckleberry Finn is never criticised.", False, "« criticised for its racist language »." )],
  [Q(D, "Where did Mark Twain grow up?", ["On the Mississippi River.", "In London.", "In California."]),
   Q(D, "Where does his pen name come from?", ["From a sailors' call on the river.", "From a song.", "From his teacher."]),
   Q(D, "Who is Jim?", ["A slave who is escaping.", "Tom's teacher.", "Huck's father."]),
   Q(D, "What does Huck decide?", ["To help Jim to be free.", "To go home.", "To become a pilot."])],
  [DT(D, "Dans quelle ville Twain grandit-il ?", ["Hannibal", "Chicago", "Boston", "New Orleans"]),
   DT(D, "Quel roman de 2024 raconte l'histoire du point de vue de Jim ?", ["James", "Huck", "Jim's Raft", "The River"]),
   DT(D, "Quelle comète est liée à la naissance et à la mort de Twain ?", ["La comète de Halley", "La comète Hale-Bopp", "La comète de Shoemaker", "Aucune"]),
   DT(D, "Comment dit-on « un radeau » ?", ["A raft", "A boat-bed", "A canoe", "A barge-car"])],
  [W(D, "Trouve le mot qui veut dire « a grandi » (2 mots).", ["grew up"]), W(D, "Trouve le mot qui veut dire « la profondeur ».", "depth"),
   W(D, "Trouve le mot qui veut dire « un nom de plume » (2 mots).", ["pen name"]), W(D, "Trouve le mot qui veut dire « une palissade ».", ["fence", "a fence"])])

# ═════════ SEUSS & POPPINS ═════════
F = "cu_jeux_de_mots.html"
DZ(F, """
## Dr. Seuss, le magicien des rimes
**Theodor Seuss Geisel** (1904-1991), dit **Dr. Seuss**, est l'auteur pour enfants le plus célèbre des États-Unis. Dans les années 1950, on s'inquiète que les enfants américains apprennent mal à lire avec des manuels ennuyeux. Un éditeur lui lance un défi : écrire un livre passionnant avec une liste limitée de mots simples. Résultat : *The Cat in the Hat* (1957), où un chat farfelu en chapeau rayé sème le désordre chez deux enfants seuls à la maison un jour de pluie. Le livre n'utilise qu'environ 230 mots différents. Puis un autre éditeur parie avec lui qu'il ne pourra pas écrire un livre avec seulement **50 mots** : il gagne le pari avec *Green Eggs and Ham* (1960).
Ses livres sont reconnaissables à leurs **rimes**, leur rythme entraînant, leurs créatures étranges et leurs mots inventés. Certains portent un message : *The Lorax* (1971) défend la nature contre l'exploitation industrielle, *How the Grinch Stole Christmas!* (1957) critique la course aux cadeaux. Aux États-Unis, son anniversaire, le 2 mars, est une journée de la lecture dans les écoles. En 2021, ses héritiers ont cessé de publier six livres contenant des images jugées racistes.

## Mary Poppins et le mot le plus long
**Mary Poppins** est une nounou magique créée en 1934 par l'écrivaine **P. L. Travers**, née en Australie. Elle arrive à Londres portée par le vent avec son parapluie, range la chambre d'un claquement de doigts et emmène les enfants Banks dans des aventures fantastiques. Le film de Disney (1964), avec Julie Andrews, est devenu un classique… même si P. L. Travers le détestait. Une chanson du film rend célèbre un mot inventé de 34 lettres : **Supercalifragilisticexpialidocious**, « le mot à dire quand on ne sait pas quoi dire », qui exprime qu'une chose est merveilleuse.

## L'anglais, une langue qui joue
L'anglais se prête particulièrement aux jeux de mots :
- **Nonsense** : Lewis Carroll invente dans le poème *Jabberwocky* (1871) des mots qui sont entrés dans la langue, comme *chortle* (glousser) ; Edward Lear popularise les **limericks**, petits poèmes comiques de cinq vers rimés AABBA.
- **Tongue twisters** (virelangues) : « *She sells seashells by the seashore* », « *Red lorry, yellow lorry* ».
- **Puns** (calembours) : jeux sur les mots qui sonnent pareil.
- **Spoonerisms** : on inverse les premiers sons de deux mots, comme le révérend William Spooner, qui disait paraît-il « *a blushing crow* » au lieu de « *a crushing blow* ».
- **Onomatopoeia** : *buzz*, *splash*, *bang*, *achoo*…
Les mots anglais courts, les accents toniques et les nombreuses rimes donnent à la langue une forte **musicalité**, que les comptines (*nursery rhymes*) font découvrir aux enfants dès le plus jeune âge.
[→ Voir aussi : la littérature jeunesse](cu_litterature_jeunesse.html)
""", """
a rhyme = une rime
a word = un mot
a hat = un chapeau
an umbrella = un parapluie
a nanny = une nounou
a cat = un chat
a joke = une blague
a sound = un son
""", [
 ("Quel défi Dr. Seuss relève-t-il avec The Cat in the Hat ?", ["Écrire un livre passionnant avec peu de mots simples", "Écrire sans rimes", "Écrire en français"], ""),
 ("Combien de mots différents utilise Green Eggs and Ham ?", ["50", "5 000", "500"], ""),
 ("Quel message porte The Lorax ?", ["Il défend la nature", "Il défend les usines", "Il parle de football"], ""),
 ("Comment Mary Poppins arrive-t-elle à Londres ?", ["Portée par le vent avec son parapluie", "En train", "En avion"], ""),
 ("Qu'est-ce qu'un limerick ?", ["Un petit poème comique de cinq vers", "Un fromage", "Une danse"], ""),
 ("Qu'est-ce qu'un tongue twister ?", ["Une phrase difficile à prononcer vite", "Une maladie", "Un mot très long"], ""),
], [("**P. L. Travers**", "écrivaine anglo-australienne, 1899-1996"), ("Julie Andrews", "actrice et chanteuse britannique"), ("Lewis Carroll", "auteur d'Alice au pays des merveilles")])
D = "jm"
culture(F, "Culture : Dr. Seuss, Mary Poppins and wordplay", 'Wordplay <span>&amp; rhymes</span>',
  "Culture · Dr. Seuss, Mary Poppins et la musique de l'anglais", ("#fca5a5", "#2563eb"),
  reperes("Dr. Seuss, Mary Poppins, les limericks et les virelangues montrent combien l'anglais aime jouer avec les sons et les mots.",
    [("1871", "Jabberwocky de Lewis Carroll"), ("1934", "Mary Poppins de P. L. Travers"), ("1957", "The Cat in the Hat de Dr. Seuss"),
     ("1960", "Green Eggs and Ham, avec 50 mots"), ("1964", "le film Mary Poppins"), ("2 mars", "journée de la lecture aux États-Unis")],
    "a rhyme, a pun, a tongue twister, a limerick, nonsense, a made-up word, rhythm, a nursery rhyme"),
  {D: doc("The fun of words", [
    "Dr. Seuss is the most famous children's author in the USA. His books are full of rhymes, strange creatures and made-up words.",
    "In The Cat in the Hat (1957), a crazy cat visits two children on a rainy day. Later, Dr. Seuss wrote Green Eggs and Ham with only 50 different words, because of a bet!",
    "Mary Poppins is a magical nanny created by P. L. Travers in 1934. She arrives in London with her umbrella. In the Disney film, she sings a very long word: supercalifragilisticexpialidocious.",
    "English loves wordplay. Tongue twisters, like \"She sells seashells by the seashore\", are sentences that are difficult to say quickly.",
    "Limericks are funny poems with five lines. Because of its rhymes and rhythm, English can sound like music."])},
  [TF(D, "Dr. Seuss is a famous children's author.", True, "« the most famous children's author »."),
   TF(D, "The Cat in the Hat visits the children on a sunny day.", False, "« on a rainy day »."),
   TF(D, "Green Eggs and Ham uses only 50 different words.", True, "« only 50 different words »."),
   TF(D, "Mary Poppins arrives with a bicycle.", False, "« with her umbrella »."),
   TF(D, "Tongue twisters are easy to say quickly.", False, "« difficult to say quickly »."),
   TF(D, "Limericks have five lines.", True, "« five lines »." )],
  [Q(D, "What are Dr. Seuss's books full of?", ["Rhymes, strange creatures and made-up words.", "Maps and dates.", "Recipes."]),
   Q(D, "Why did Dr. Seuss use only 50 words?", ["Because of a bet.", "Because he was tired.", "Because of the price."]),
   Q(D, "Who is Mary Poppins?", ["A magical nanny.", "A teacher.", "A queen."]),
   Q(D, "What is a tongue twister?", ["A sentence difficult to say quickly.", "A long poem.", "A song."])],
  [DT(D, "Comment s'appelle le personnage qui vole Noël ?", ["Le Grinch", "Le Lorax", "Le Chat", "Horton"]),
   DT(D, "Combien de lettres compte supercalifragilisticexpialidocious ?", ["34", "12", "50", "100"]),
   DT(D, "Qui invente le mot « chortle » ?", ["Lewis Carroll", "Dr. Seuss", "Shakespeare", "Mary Poppins"]),
   DT(D, "Comment dit-on « un jeu de mots, un calembour » ?", ["A pun", "A fun", "A word game", "A riddle"])],
  [W(D, "Trouve le mot qui veut dire « des mots inventés » (2 mots).", ["made-up words"]), W(D, "Trouve le mot qui veut dire « un pari ».", ["bet", "a bet"]),
   W(D, "Trouve le mot qui veut dire « une nounou ».", ["nanny", "magical nanny"]), W(D, "Trouve le mot qui veut dire « le rythme ».", "rhythm")])

# ═════════ MYTHES IRLANDAIS & DRAGONS ═════════
F = "cu_mythes_dragons.html"
DZ(F, """
## L'Irlande, terre de mythes
L'Irlande a conservé un immense trésor de légendes celtes, transmises par les conteurs (**seanchaí**) puis écrites par les moines au Moyen Âge.
- Les **leprechauns** sont de petits cordonniers farceurs qui cachent un chaudron d'or au pied de l'arc-en-ciel. Si vous en attrapez un, il doit vous révéler sa cachette… mais il trouve toujours un moyen de s'échapper.
- La **banshee** (« femme des fées ») pousse des cris déchirants la nuit pour annoncer une mort dans la famille.
- Dans *Les Enfants de Lir*, une belle-mère jalouse transforme quatre enfants en **cygnes** pour 900 ans.
- Le héros **Fionn mac Cumhaill** (Finn McCool) aurait goûté au saumon de la connaissance et obtenu ainsi toute la sagesse du monde. Selon la légende, ce géant aurait construit la **Chaussée des Géants** (Giant's Causeway), en Irlande du Nord, pour aller combattre un géant écossais. En réalité, ses quelque 40 000 colonnes de basalte sont nées d'éruptions volcaniques il y a environ 60 millions d'années.
- **Oisín** suit la belle Niamh au **Tír na nÓg**, le pays de l'éternelle jeunesse ; quand il revient en Irlande, trois siècles ont passé.
- **Cúchulainn**, le « chien de Culann », est le grand guerrier de l'Ulster.

## Le dragon, de l'Est à l'Ouest
Dans les cultures européennes, le dragon est souvent une créature maléfique qui crache du feu et garde des trésors ; en Chine, au contraire, il est un symbole bienfaisant de puissance et de chance.
- **Saint Georges**, patron de l'Angleterre (fêté le 23 avril), est célèbre pour avoir terrassé un dragon et sauvé une princesse ; sa croix rouge sur fond blanc forme le drapeau anglais.
- Le **dragon rouge**, *Y Ddraig Goch*, figure sur le drapeau du **pays de Galles**. Selon la légende, le magicien Merlin aurait révélé au roi Vortigern qu'un dragon rouge (les Bretons) et un dragon blanc (les Saxons) se battaient sous la terre.
- À la fin du poème *Beowulf*, le vieux héros meurt en combattant un dragon.
- Au 20e siècle, Tolkien crée **Smaug**, le dragon avide de *The Hobbit*, et les dragons deviennent des stars de la fantasy, du cinéma et des jeux vidéo, parfois effrayants, parfois amicaux, comme dans *How to Train Your Dragon*.
Sur certaines cartes anciennes, on trouvait la mention « ici sont les dragons » pour désigner les terres inconnues.

## Pourquoi ces légendes ?
Les mythes expliquent des phénomènes naturels (une chaussée de basalte, un cri dans la nuit), transmettent des valeurs (courage, loyauté, sagesse) et renforcent une **identité** nationale : le dragon gallois, la harpe et le trèfle irlandais sont toujours des symboles très présents.
[→ Voir aussi : Halloween, héritier de Samhain](cu_fetes_origines.html)
""", """
a legend = une légende
a giant = un géant
a dragon = un dragon
a swan = un cygne
gold = l'or
a rainbow = un arc-en-ciel
a hero = un héros
a flag = un drapeau
""", [
 ("Que cache un leprechaun ?", ["Un chaudron d'or au pied de l'arc-en-ciel", "Un dragon", "Une épée"], ""),
 ("Que fait la banshee ?", ["Elle annonce une mort par ses cris", "Elle garde les enfants", "Elle danse"], ""),
 ("Qui aurait construit la Chaussée des Géants selon la légende ?", ["Le géant Finn McCool", "Saint Georges", "Des Vikings"], ""),
 ("Que représente le dragon en Chine, contrairement à l'Europe ?", ["Un symbole bienfaisant de puissance et de chance", "Le mal absolu", "La pluie"], ""),
 ("Quel drapeau porte un dragon rouge ?", ["Celui du pays de Galles", "Celui de l'Irlande", "Celui de l'Écosse"], ""),
 ("À quoi servent les mythes ?", ["Expliquer la nature, transmettre des valeurs, renforcer une identité", "Remplacer l'école", "Rien du tout"], ""),
], [("**Tír na nÓg**", "le pays de l'éternelle jeunesse"), ("Ulster", "province du nord de l'Irlande"), ("Smaug", "dragon de The Hobbit")])
D = "md"
culture(F, "Culture : Irish myths and dragons", 'Myths <span>&amp; dragons</span>',
  "Culture · leprechauns, banshees, géants et dragons", ("#86efac", "#b91c1c"),
  reperes("L'Irlande est une terre de mythes celtes, et le dragon est une figure majeure du folklore britannique, du drapeau gallois à saint Georges.",
    [("leprechaun", "petit lutin et son chaudron d'or"), ("banshee", "la messagère de la mort"), ("Giant's Causeway", "40 000 colonnes de basalte"),
     ("23 avril", "Saint-Georges, patron de l'Angleterre"), ("Y Ddraig Goch", "le dragon rouge du pays de Galles")],
    "a myth, a legend, a fairy, a giant, a dragon, a hero, magic, a symbol"),
  {D: doc("Giants, fairies and dragons", [
    "Ireland is a land of myths and legends. Leprechauns are little fairies who hide a pot of gold at the end of the rainbow.",
    "The banshee is a woman who cries in the night when somebody is going to die. In another story, four children are turned into swans for 900 years.",
    "According to a legend, the giant Finn McCool built the Giant's Causeway in Northern Ireland. In reality, it was created by a volcano millions of years ago.",
    "Dragons are important in Britain too. Saint George, the patron saint of England, killed a dragon. The Welsh flag has a red dragon on it.",
    "In European stories, dragons are often dangerous monsters, but in China, they bring good luck."])},
  [TF(D, "Leprechauns hide a pot of gold.", True, "« hide a pot of gold »."),
   TF(D, "The banshee cries when somebody is going to get married.", False, "« when somebody is going to die »."),
   TF(D, "The Giant's Causeway was really built by a giant.", False, "« created by a volcano »."),
   TF(D, "Saint George is the patron saint of England.", True, "« the patron saint of England »."),
   TF(D, "The Welsh flag has a red dragon.", True, "« a red dragon »."),
   TF(D, "In China, dragons bring bad luck.", False, "« they bring good luck »." )],
  [Q(D, "What are leprechauns?", ["Little fairies.", "Giants.", "Dragons."]),
   Q(D, "What happens to the four children in the story?", ["They are turned into swans.", "They become kings.", "They find gold."]),
   Q(D, "What did Saint George do?", ["He killed a dragon.", "He built a causeway.", "He became a swan."]),
   Q(D, "How are dragons different in China?", ["They bring good luck.", "They are smaller.", "They cannot fly."])],
  [DT(D, "Où se trouve la Chaussée des Géants ?", ["En Irlande du Nord", "En Écosse", "Au pays de Galles", "En Cornouailles"]),
   DT(D, "Comment s'appelle le pays de l'éternelle jeunesse ?", ["Tír na nÓg", "Avalon", "Narnia", "Neverland"]),
   DT(D, "Quel est le dragon de The Hobbit ?", ["Smaug", "Toothless", "Puff", "Y Ddraig Goch"]),
   DT(D, "Comment dit-on « une fée » ?", ["A fairy", "A ferry", "A fairy tale", "A fay-ry"])],
  [W(D, "Trouve le mot qui veut dire « un chaudron, un pot ».", ["pot", "a pot"]), W(D, "Trouve le mot qui veut dire « des cygnes ».", "swans"),
   W(D, "Trouve le mot qui veut dire « le saint patron » (2 mots).", ["patron saint"]), W(D, "Trouve le mot qui veut dire « la chance » (2 mots).", ["good luck"])])

# ═════════ BBC ═════════
F = "cu_bbc.html"
DZ(F, """
## « Inform, educate and entertain »
La **British Broadcasting Corporation**, la **BBC**, naît en 1922 et devient en 1927 un service public indépendant, organisé par une charte royale. Son premier directeur, **John Reith**, lui fixe une mission toujours d'actualité : **informer, éduquer et divertir**. Elle lance l'une des premières chaînes de télévision régulières du monde en 1936. Les Britanniques la surnomment affectueusement « **Auntie Beeb** », la « tante BBC ».

## Un financement original : la licence fee
La BBC n'a pas de publicité sur ses chaînes britanniques. Elle est financée principalement par la **licence fee**, une redevance que chaque foyer doit payer s'il regarde la télévision en direct ou utilise son service en ligne, BBC iPlayer : un peu plus de 170 livres par an. Ce système garantit son indépendance vis-à-vis des annonceurs, mais il est régulièrement contesté, surtout par ceux qui regardent surtout des plateformes de streaming.

## La voix de la liberté pendant la guerre
Créé en 1932, le **World Service** diffuse aujourd'hui des informations dans plus de 40 langues. Pendant la Seconde Guerre mondiale, la BBC est la voix de l'espoir pour l'Europe occupée : c'est sur ses ondes que le général **de Gaulle** lance son **appel du 18 juin 1940**, et que sont diffusés les messages codés destinés à la Résistance française. Sa réputation de fiabilité est devenue un atout majeur du **soft power** britannique.

## Des programmes qui ont fait le tour du monde
- **Doctor Who** (depuis 1963), un extraterrestre qui voyage dans le temps à bord d'une cabine téléphonique de police, le TARDIS : la plus longue série de science-fiction de l'histoire.
- Les documentaires animaliers de **David Attenborough**, comme *Planet Earth* ou *Blue Planet II* (2017), qui a fait prendre conscience au public de la pollution des océans par le plastique.
- **EastEnders**, un feuilleton populaire depuis 1985 ; **Strictly Come Dancing**, concours de danse adapté en France sous le nom de *Danse avec les stars* ; *Sherlock* ; *Bluey*, dessin animé australien coproduit par la BBC.
- Les grands événements nationaux : le couronnement d'Elizabeth II en 1953, retransmis à la télévision, les funérailles royales, Wimbledon, le message de Noël du roi.

## Une institution sous surveillance
La BBC doit être **impartiale**. Elle est donc critiquée de tous côtés : trop à gauche pour les uns, trop proche du pouvoir pour les autres. Des scandales l'ont aussi ébranlée, et en 2025 son directeur général a démissionné après une polémique sur le montage d'un discours de Donald Trump dans un documentaire. Le débat sur son financement et son avenir face à Netflix et YouTube reste très vif.
[→ Voir aussi : les médias anglophones](cu_medias.html)
""", """
the news = les informations
a channel = une chaîne
a programme = une émission
a series = une série
a documentary = un documentaire
the radio = la radio
an advert = une publicité
to watch = regarder
""", [
 ("Quelle est la mission de la BBC ?", ["Informer, éduquer et divertir", "Vendre des produits", "Faire de la politique"], ""),
 ("Comment la BBC est-elle financée ?", ["Par une redevance payée par les foyers, la licence fee", "Par la publicité", "Par le roi"], ""),
 ("Quel lien la BBC a-t-elle avec la France ?", ["De Gaulle y a lancé l'appel du 18 juin 1940", "Elle appartient à la France", "Elle est née à Paris"], ""),
 ("Qu'est-ce que Doctor Who ?", ["Une série de science-fiction sur un voyageur du temps", "Un médecin célèbre", "Un journal"], ""),
 ("Qu'a provoqué Blue Planet II ?", ["Une prise de conscience sur la pollution plastique des océans", "Une guerre", "Rien"], ""),
 ("Pourquoi la BBC est-elle critiquée ?", ["On lui reproche parfois de ne pas être impartiale, et son financement est contesté", "Elle n'a pas de séries", "Elle est trop petite"], ""),
], [("**John Reith**", "premier directeur de la BBC"), ("**David Attenborough**", "naturaliste et présentateur, né en 1926")])
D = "bb"
culture(F, "Culture : The BBC", 'The <span>BBC</span>',
  "Culture · « Auntie Beeb », une institution britannique", ("#fecaca", "#111827"),
  reperes("Créée en 1922, la BBC est le grand service public de radio et de télévision britannique, financé par une redevance et connu dans le monde entier.",
    [("1922", "naissance de la BBC"), ("1932", "lancement du service international (World Service)"), ("1936", "début de la télévision"),
     ("18 juin 1940", "l'appel du général de Gaulle"), ("1953", "couronnement d'Elizabeth II à la télévision"), ("1963", "première de Doctor Who")],
    "the BBC, a channel, the licence fee, a documentary, a series, the news, impartial, soft power"),
  {D: doc("Auntie Beeb", [
    "The BBC is the British public broadcaster. It was created in 1922. Its mission is to inform, educate and entertain.",
    "There are no adverts on BBC channels in the UK. People who watch live TV must pay a licence fee every year.",
    "During the Second World War, the BBC was very important. General de Gaulle spoke to the French people on BBC radio on 18 June 1940.",
    "The BBC is famous for its programmes: Doctor Who, the nature documentaries of David Attenborough, and many series and dance shows.",
    "The BBC must be impartial, but some people criticise it, and others think the licence fee is too expensive."])},
  [TF(D, "The BBC was created in 1922.", True, "« created in 1922 »."),
   TF(D, "There are many adverts on BBC channels in the UK.", False, "« There are no adverts »."),
   TF(D, "People who watch live TV must pay a licence fee.", True, "« must pay a licence fee »."),
   TF(D, "De Gaulle spoke on BBC radio in 1940.", True, "« on 18 June 1940 »."),
   TF(D, "David Attenborough makes cooking programmes.", False, "« nature documentaries »."),
   TF(D, "Everybody loves the licence fee.", False, "« others think the licence fee is too expensive »." )],
  [Q(D, "What is the BBC's mission?", ["To inform, educate and entertain.", "To sell products.", "To make films only."]),
   Q(D, "How is the BBC paid for?", ["By the licence fee.", "By adverts.", "By the King."]),
   Q(D, "Who spoke on BBC radio on 18 June 1940?", ["General de Gaulle.", "Churchill.", "The King."]),
   Q(D, "What is David Attenborough famous for?", ["Nature documentaries.", "Science fiction.", "Dance shows."])],
  [DT(D, "Quel est le surnom affectueux de la BBC ?", ["Auntie Beeb", "Big Ben", "The Box", "Uncle Broadcast"]),
   DT(D, "Comment s'appelle la machine à voyager dans le temps de Doctor Who ?", ["Le TARDIS", "Le DeLorean", "L'Enterprise", "Le Time Box"]),
   DT(D, "Quelle émission a inspiré « Danse avec les stars » ?", ["Strictly Come Dancing", "EastEnders", "Top Gear", "Bake Off"]),
   DT(D, "Comment dit-on « la redevance » ?", ["The licence fee", "The TV tax card", "The channel bill", "The remote fee"])],
  [W(D, "Trouve le mot qui veut dire « divertir ».", "entertain"), W(D, "Trouve le mot qui veut dire « des publicités ».", "adverts"),
   W(D, "Trouve le mot qui veut dire « en direct ».", "live"), W(D, "Trouve le mot qui veut dire « impartiale ».", "impartial")])

# ═════════ NATIONAL TRUST ═════════
F = "cu_national_trust.html"
DZ(F, """
## Protéger le patrimoine « pour toujours, pour tous »
En **1895**, trois Britanniques, la réformatrice sociale **Octavia Hill**, l'avocat Robert Hunter et le pasteur Hardwicke Rawnsley, fondent le **National Trust** pour protéger les lieux d'intérêt historique ou de beauté naturelle menacés par l'industrialisation. Leur idée : ces lieux doivent être préservés « *for ever, for everyone* » (pour toujours, pour tous). C'est une association caritative, indépendante de l'État, financée par les cotisations de ses membres, les dons, les visites et les bénévoles (**volunteers**).

## Un géant du patrimoine
Le National Trust protège aujourd'hui en Angleterre, au pays de Galles et en Irlande du Nord :
- plus de 500 lieux historiques : châteaux, manoirs (**stately homes**), jardins, moulins, maisons d'écrivains ;
- de vastes paysages, des forêts, des fermes et une grande partie du littoral, comme les célèbres **falaises blanches de Douvres** ;
- des sites exceptionnels comme la **Chaussée des Géants** en Irlande du Nord.
Avec plus de 5 millions de membres, c'est l'une des plus grandes associations d'Europe. L'Écosse a son propre National Trust for Scotland. Un autre organisme, **English Heritage**, gère d'autres monuments célèbres, comme **Stonehenge** et le mur d'Hadrien.

## Pourquoi tant de châteaux ?
Au 20e siècle, de nombreuses familles aristocratiques ne peuvent plus payer l'entretien de leurs immenses demeures ni les droits de succession. Beaucoup les confient au National Trust, qui les ouvre au public. Les visiteurs y découvrent la vie « *upstairs, downstairs* » : celle des maîtres à l'étage, et celle des domestiques dans les cuisines et les sous-sols, comme dans la série *Downton Abbey*.

## Beatrix Potter et le Lake District
L'autrice de *Peter Rabbit*, **Beatrix Potter**, amie d'Hardwicke Rawnsley, utilise l'argent de ses livres pour acheter des fermes et des terres dans le **Lake District**, région de lacs et de montagnes du nord-ouest de l'Angleterre. À sa mort, en 1943, elle lègue au National Trust 14 fermes et plus de 1 600 hectares, pour protéger le paysage et l'élevage traditionnel de moutons. Le Lake District est aujourd'hui classé au patrimoine mondial de l'UNESCO.

## Un patrimoine à regarder en face
En 2020, le National Trust publie un rapport montrant que plusieurs dizaines de ses demeures sont liées au colonialisme ou à l'esclavage, par l'argent de leurs anciens propriétaires. Pour certains, raconter cette histoire est indispensable ; pour d'autres, l'association s'éloigne de sa mission. Ce débat montre que le **heritage** n'est pas seulement à admirer, mais aussi à comprendre.
[→ Voir aussi : l'époque victorienne](cu_victoriens.html)
""", """
a castle = un château
a garden = un jardin
a house = une maison
the coast = la côte
a cliff = une falaise
a farm = une ferme
a visitor = un visiteur
a volunteer = un bénévole
""", [
 ("Pourquoi le National Trust est-il fondé en 1895 ?", ["Pour protéger des lieux menacés par l'industrialisation", "Pour construire des usines", "Pour vendre des châteaux"], ""),
 ("Comment le National Trust est-il financé ?", ["Par ses membres, les dons, les visites et les bénévoles", "Par l'armée", "Par la BBC"], ""),
 ("Pourquoi de nombreuses familles ont-elles confié leur château au National Trust ?", ["Elles ne pouvaient plus payer l'entretien et les droits de succession", "Elles partaient en vacances", "Le roi l'ordonnait"], ""),
 ("Que montre la vie « upstairs, downstairs » ?", ["La vie des maîtres et celle des domestiques", "Un ascenseur", "Une école"], ""),
 ("Qu'a fait Beatrix Potter ?", ["Elle a légué des fermes et des terres du Lake District", "Elle a construit Stonehenge", "Elle a fondé la BBC"], ""),
 ("Qu'a révélé le rapport de 2020 ?", ["Les liens de certaines demeures avec le colonialisme et l'esclavage", "Des fantômes", "Un trésor"], ""),
], [("**Octavia Hill**", "réformatrice sociale, 1838-1912"), ("**Beatrix Potter**", "autrice et illustratrice, 1866-1943"), ("*Downton Abbey*", "série britannique sur une famille aristocratique")])
D = "nt"
culture(F, "Culture : The National Trust and British heritage", 'The National <span>Trust</span>',
  "Culture · châteaux, jardins, côtes et patrimoine britannique", ("#bbf7d0", "#14532d"),
  reperes("Le National Trust, fondé en 1895, protège des centaines de châteaux, de jardins et de paysages en Angleterre, au pays de Galles et en Irlande du Nord.",
    [("1895", "fondation du National Trust"), ("1943", "legs de Beatrix Potter dans le Lake District"), ("plus de 500", "lieux historiques protégés"),
     ("plus de 5 millions", "de membres"), ("2020", "rapport sur les liens avec le colonialisme et l'esclavage")],
    "heritage, a stately home, a castle, a garden, the coastline, a member, a volunteer, to preserve"),
  {D: doc("For ever, for everyone", [
    "The National Trust is a British charity. It was created in 1895 to protect beautiful places and historic buildings for ever, for everyone.",
    "Today, it looks after more than 500 castles, stately homes and gardens, but also forests, farms, beaches and the White Cliffs of Dover.",
    "Many rich families gave their houses to the National Trust because they were too expensive. Visitors can see the beautiful rooms upstairs and the kitchens where the servants worked downstairs.",
    "Beatrix Potter, the author of Peter Rabbit, gave her farms in the Lake District to the National Trust to protect the landscape.",
    "The National Trust has more than five million members, and thousands of volunteers help it every year."])},
  [TF(D, "The National Trust was created in 1895.", True, "« created in 1895 »."),
   TF(D, "It only protects castles.", False, "« also forests, farms, beaches »."),
   TF(D, "The White Cliffs of Dover are protected by the National Trust.", True, "« the White Cliffs of Dover »."),
   TF(D, "Servants worked upstairs.", False, "« the kitchens where the servants worked downstairs »."),
   TF(D, "Beatrix Potter gave her farms to the National Trust.", True, "« gave her farms »."),
   TF(D, "The National Trust has no volunteers.", False, "« thousands of volunteers »." )],
  [Q(D, "Why was the National Trust created?", ["To protect beautiful places and historic buildings.", "To build new houses.", "To make money for the King."]),
   Q(D, "Why did rich families give their houses?", ["They were too expensive.", "They wanted to move to France.", "They were too small."]),
   Q(D, "What can visitors see?", ["Beautiful rooms upstairs and kitchens downstairs.", "Only gardens.", "Factories."]),
   Q(D, "Who helps the National Trust?", ["Thousands of volunteers.", "The army.", "Nobody."])],
  [DT(D, "Qui gère Stonehenge ?", ["English Heritage", "Le National Trust", "La BBC", "La famille royale"]),
   DT(D, "Quelle autrice a protégé le Lake District ?", ["Beatrix Potter", "Agatha Christie", "Jane Austen", "J. K. Rowling"]),
   DT(D, "Quelle série montre la vie « upstairs, downstairs » ?", ["Downton Abbey", "Doctor Who", "Sherlock", "EastEnders"]),
   DT(D, "Comment dit-on « un bénévole » ?", ["A volunteer", "A voluntary", "A benevolent", "A free worker"])],
  [W(D, "Trouve le mot qui veut dire « une association caritative ».", ["charity", "a British charity"]), W(D, "Trouve le mot qui veut dire « s'occupe de » (2 mots).", ["looks after"]),
   W(D, "Trouve le mot qui veut dire « les domestiques ».", "servants"), W(D, "Trouve le mot qui veut dire « le paysage ».", "landscape")])

# ═════════ JUNETEENTH & COLUMBUS DAY ═════════
F = "cu_juneteenth_columbus.html"
DZ(F, """
## Juneteenth : la fin de l'esclavage
Le 1er janvier 1863, en pleine guerre de Sécession, Abraham Lincoln signe la **Proclamation d'émancipation**, qui déclare libres les esclaves des États confédérés. Mais au Texas, loin des combats, la nouvelle n'est pas appliquée. Ce n'est que le **19 juin 1865**, deux mois après la fin de la guerre, que le général nordiste Gordon Granger arrive à **Galveston** et annonce officiellement que tous les esclaves du Texas, environ 250 000 personnes, sont libres. Le nom **Juneteenth** vient de la contraction de *June* et *nineteenth*. Dès l'année suivante, les Afro-Américains du Texas célèbrent ce « jour du Jubilé » par des pique-niques, des prières, de la musique et des parades. Le 13e amendement, qui abolit définitivement l'esclavage dans tout le pays, est adopté en décembre 1865.
La fête reste longtemps surtout régionale. Elle devient un jour férié au Texas en 1980, puis, après les grandes manifestations de 2020, un **jour férié fédéral** en **2021** : le premier nouveau jour férié national depuis la création du Martin Luther King Day en 1983. On la célèbre avec des barbecues, des lectures de la Proclamation et le drapeau de Juneteenth, rouge, blanc et bleu, avec une étoile en hommage au Texas.

## Columbus Day : une fête contestée
Le **deuxième lundi d'octobre**, les États-Unis célèbrent l'arrivée de **Christophe Colomb** en Amérique le 12 octobre 1492. La fête a une histoire particulière : elle a d'abord été promue par les **Italo-Américains**, longtemps victimes de discriminations, qui voyaient dans le navigateur génois un symbole de fierté. En 1892, après le lynchage de onze Italiens à La Nouvelle-Orléans, le président Benjamin Harrison proclame une célébration nationale du 400e anniversaire. Columbus Day devient un jour férié fédéral en 1937. Des parades italo-américaines ont lieu, notamment à New York.

## Indigenous Peoples' Day
Pour les peuples amérindiens, l'arrivée de Colomb marque le début de la colonisation, des massacres, de l'esclavage et des épidémies qui ont décimé les populations. Depuis les années 1990, de plus en plus de villes et d'États remplacent ou complètent Columbus Day par l'**Indigenous Peoples' Day**, qui célèbre les cultures autochtones. Certaines statues de Colomb ont été retirées ou vandalisées, notamment en 2020. Le président Biden a reconnu officiellement les deux journées en 2021 ; son successeur a ensuite remis l'accent sur Columbus Day. Le débat oppose deux façons de raconter l'histoire nationale.

## Que nous apprennent ces fêtes ?
Les jours fériés ne sont pas neutres : ils disent quelles histoires une nation choisit de célébrer. Juneteenth et Columbus Day montrent comment la mémoire collective évolue et comment des groupes longtemps oubliés font entendre leur voix.
[→ Voir aussi : l'esclavage aux États-Unis](cu_esclavage.html)
""", """
a holiday = un jour férié
freedom = la liberté
a slave = un esclave
a parade = un défilé
a picnic = un pique-nique
a statue = une statue
history = l'histoire
to celebrate = célébrer
""", [
 ("Que s'est-il passé le 19 juin 1865 à Galveston ?", ["On annonce aux esclaves du Texas qu'ils sont libres", "Lincoln est élu", "Colomb arrive"], ""),
 ("D'où vient le nom « Juneteenth » ?", ["De la contraction de June et nineteenth", "D'un général", "D'une ville"], ""),
 ("Quand Juneteenth devient-il un jour férié fédéral ?", ["En 2021", "En 1865", "En 1980"], ""),
 ("Pourquoi les Italo-Américains ont-ils promu Columbus Day ?", ["Colomb était pour eux un symbole de fierté face aux discriminations", "Colomb était américain", "Pour vendre des pâtes"], ""),
 ("Pourquoi Columbus Day est-il contesté ?", ["Pour les Amérindiens, Colomb symbolise le début de la colonisation", "Il tombe un dimanche", "Personne ne le fête"], ""),
 ("Que montrent ces débats ?", ["Que la mémoire collective évolue", "Que l'histoire ne change jamais", "Que les fêtes sont inutiles"], ""),
], [("Gordon Granger", "général de l'armée de l'Union"), ("Benjamin Harrison", "président de 1889 à 1893")])
D = "jc"
culture(F, "Culture : Juneteenth and Columbus Day", 'Juneteenth <span>&amp; Columbus Day</span>',
  "Culture · deux fêtes américaines et leurs débats", ("#fca5a5", "#1e3a8a"),
  reperes("Juneteenth célèbre la fin de l'esclavage ; Columbus Day, l'arrivée de Colomb, est contesté et parfois remplacé par l'Indigenous Peoples' Day.",
    [("12 octobre 1492", "arrivée de Christophe Colomb"), ("1863", "Proclamation d'émancipation"), ("19 juin 1865", "annonce de la liberté à Galveston"),
     ("1937", "Columbus Day, jour férié fédéral"), ("2021", "Juneteenth, jour férié fédéral")],
    "a federal holiday, emancipation, freedom, a celebration, a parade, Indigenous, memory, a controversy"),
  {D: doc("Two holidays, two stories", [
    "Juneteenth is celebrated on 19 June. On that day in 1865, enslaved people in Texas finally learned that they were free. The name is a mix of \"June\" and \"nineteenth\".",
    "For many years, it was mainly celebrated by African Americans in Texas, with picnics and parades. In 2021, it became a national holiday.",
    "Columbus Day is on the second Monday of October. It celebrates the arrival of Christopher Columbus in America in 1492. Italian Americans are very proud of this day.",
    "But for Native Americans, Columbus's arrival was the beginning of colonisation and suffering. So many cities now celebrate Indigenous Peoples' Day instead.",
    "These two holidays show that people do not always agree about how to remember history."])},
  [TF(D, "Juneteenth is celebrated on 19 June.", True, "« on 19 June »."),
   TF(D, "Enslaved people in Texas learned they were free in 1776.", False, "« in 1865 »."),
   TF(D, "Juneteenth became a national holiday in 2021.", True, "« In 2021 »."),
   TF(D, "Columbus Day is in July.", False, "« the second Monday of October »."),
   TF(D, "Italian Americans are proud of Columbus Day.", True, "« very proud of this day »."),
   TF(D, "Everybody agrees about Columbus Day.", False, "« people do not always agree »." )],
  [Q(D, "What happened on 19 June 1865?", ["Enslaved people in Texas learned they were free.", "Columbus arrived.", "Lincoln was born."]),
   Q(D, "How was Juneteenth celebrated?", ["With picnics and parades.", "With fireworks only.", "It was not celebrated."]),
   Q(D, "What does Columbus Day celebrate?", ["The arrival of Columbus in 1492.", "The end of slavery.", "Independence."]),
   Q(D, "What do many cities celebrate instead?", ["Indigenous Peoples' Day.", "Christmas.", "Halloween."])],
  [DT(D, "Dans quelle ville du Texas la liberté est-elle annoncée ?", ["Galveston", "Dallas", "Houston", "Austin"]),
   DT(D, "Quel amendement abolit l'esclavage ?", ["Le 13e", "Le 1er", "Le 2e", "Le 19e"]),
   DT(D, "Quelle fête remplace parfois Columbus Day ?", ["Indigenous Peoples' Day", "Labor Day", "Juneteenth", "Memorial Day"]),
   DT(D, "Comment dit-on « jour férié » ?", ["A holiday", "A free day off work only", "A feast", "A weekday"])],
  [W(D, "Trouve le mot qui veut dire « finalement ».", "finally"), W(D, "Trouve le mot qui veut dire « des défilés ».", "parades"),
   W(D, "Trouve le mot qui veut dire « fiers ».", "proud"), W(D, "Trouve le mot qui veut dire « la souffrance ».", "suffering")])

# ═════════ FAMILLES PRÉSIDENTIELLES ═════════
F = "cu_familles_presidentielles.html"
DZ(F, """
## Vivre à la Maison-Blanche
La **White House**, à Washington, est à la fois la résidence et le bureau du président. Le premier à y habiter est John Adams, en 1800. En 1814, pendant une guerre contre le Royaume-Uni, les soldats britanniques l'incendient ; elle est reconstruite et repeinte en blanc. Le président travaille dans le célèbre **Oval Office**, et sa famille vit dans les appartements privés, sous le regard constant des médias.

## La First Lady
L'épouse du président, la **First Lady**, n'a pas de fonction officielle, mais beaucoup ont marqué l'histoire.
- **Eleanor Roosevelt**, épouse de Franklin D. Roosevelt (1933-1945), tient une chronique dans les journaux, défend les droits des femmes et des Afro-Américains, puis préside la commission de l'ONU qui rédige la **Déclaration universelle des droits de l'homme** (1948).
- **Jacqueline Kennedy** restaure la Maison-Blanche et la fait visiter à la télévision en 1962 ; son élégance fascine le monde entier.
- **Michelle Obama** (2009-2017) plante un potager à la Maison-Blanche et lutte contre l'obésité des enfants ; ses mémoires, *Becoming*, deviennent un best-seller mondial.

## Des dynasties
Plusieurs familles ont donné deux présidents : les **Adams** (John, puis son fils John Quincy), les **Roosevelt** (les cousins Theodore et Franklin) et les **Bush** (George H. W., puis son fils George W.). Les **Kennedy** forment aussi une véritable dynastie politique : John est président, ses frères Robert et Edward sont sénateurs. Leur histoire, faite de gloire et de tragédies, a nourri le mythe de « Camelot ».

## Des enfants et des animaux sous les projecteurs
Grandir à la Maison-Blanche n'est pas simple. Les photos du petit John Kennedy Jr. jouant sous le bureau de son père, ou de Malia et Sasha Obama le jour de leur arrivée, ont fait le tour du monde. Les présidents ont souvent eu des animaux : Theodore Roosevelt avait une véritable ménagerie (poneys, serpents, et même un blaireau), les Obama le chien Bo, les Clinton le chat Socks. Chaque année, le président « gracie » une dinde de Thanksgiving, et des milliers d'enfants participent à la chasse aux œufs de Pâques sur la pelouse (**Easter Egg Roll**), une tradition depuis 1878.

## L'image d'une famille
La famille présidentielle est aussi un outil de communication : elle donne une image humaine, proche, rassurante du président. Les portraits officiels, les photos de Noël, les réseaux sociaux construisent cette image. Les médias s'interrogent souvent sur la frontière entre vie privée et vie publique, surtout pour les enfants.
[→ Voir aussi : les institutions américaines](cu_institutions_us.html)
""", """
a president = un président
the White House = la Maison-Blanche
a family = une famille
a wife = une épouse
a dog = un chien
a garden = un jardin
a photo = une photo
private = privé
""", [
 ("Qui est le premier président à habiter la Maison-Blanche ?", ["John Adams, en 1800", "George Washington", "Abraham Lincoln"], ""),
 ("Qu'a fait Eleanor Roosevelt après la guerre ?", ["Elle a présidé la rédaction de la Déclaration universelle des droits de l'homme", "Elle est devenue présidente", "Elle a construit la Maison-Blanche"], ""),
 ("Qu'a fait Michelle Obama à la Maison-Blanche ?", ["Elle a planté un potager et lutté contre l'obésité des enfants", "Elle a vendu la maison", "Elle a été sénatrice"], ""),
 ("Quelles familles ont donné deux présidents ?", ["Les Adams, les Roosevelt et les Bush", "Les Kennedy et les Obama", "Les Lincoln et les Washington"], ""),
 ("Que fait le président chaque année à Thanksgiving ?", ["Il « gracie » une dinde", "Il plante un arbre", "Il fait un discours à Londres"], ""),
 ("Pourquoi la famille présidentielle est-elle importante pour l'image ?", ["Elle donne une image humaine et rassurante du président", "Elle fait les lois", "Elle commande l'armée"], ""),
], [("Oval Office", "le bureau ovale du président"), ("Camelot", "la cour légendaire du roi Arthur")])
D = "fp"
culture(F, "Culture : America's presidential families", 'Presidential <span>families</span>',
  "Culture · la Maison-Blanche, les First Ladies et les dynasties", ("#bfdbfe", "#b91c1c"),
  reperes("Les familles des présidents américains vivent à la Maison-Blanche sous le regard du monde. Certaines First Ladies ont joué un grand rôle.",
    [("1800", "John Adams, premier habitant de la Maison-Blanche"), ("1814", "incendie de la Maison-Blanche par les Britanniques"), ("1878", "première chasse aux œufs de Pâques"),
     ("1948", "Eleanor Roosevelt et la Déclaration universelle des droits de l'homme"), ("1962", "visite télévisée de Jackie Kennedy")],
    "the White House, the First Lady, the Oval Office, a dynasty, a portrait, a pet, private life, public life"),
  {D: doc("Life in the White House", [
    "The White House, in Washington, is the home and the office of the American President. The first President to live there was John Adams, in 1800.",
    "The President's wife is called the First Lady. Eleanor Roosevelt fought for human rights, and Michelle Obama planted a vegetable garden to encourage children to eat healthy food.",
    "Some families gave two Presidents to the USA, like the Adams, the Roosevelts and the Bushes.",
    "Children and pets also live in the White House. The Obamas had a dog called Bo. Every year, children come to the White House lawn for an Easter egg race.",
    "Photos of the President's family are very popular, but some people think that the children's private life should be protected."])},
  [TF(D, "The White House is in New York.", False, "« in Washington »."),
   TF(D, "John Adams was the first President to live in the White House.", True, "« The first President to live there was John Adams »."),
   TF(D, "The President's wife is called the First Lady.", True, "« is called the First Lady »."),
   TF(D, "Michelle Obama planted a vegetable garden.", True, "« planted a vegetable garden »."),
   TF(D, "The Obamas had a cat called Bo.", False, "« a dog called Bo »."),
   TF(D, "Everybody thinks the children's private life is not important.", False, "« should be protected »." )],
  [Q(D, "What is the White House?", ["The home and office of the President.", "A museum only.", "A hotel."]),
   Q(D, "What did Eleanor Roosevelt fight for?", ["Human rights.", "More taxes.", "Sport."]),
   Q(D, "Name a family that gave two Presidents.", ["The Bushes.", "The Obamas.", "The Lincolns."]),
   Q(D, "What happens every year on the White House lawn?", ["An Easter egg race for children.", "A football match.", "A concert."])],
  [DT(D, "Comment s'appelle le bureau du président ?", ["L'Oval Office", "Le Round Room", "Le Capitol", "Le Pentagone"]),
   DT(D, "Quel président avait une ménagerie avec un blaireau ?", ["Theodore Roosevelt", "Barack Obama", "John Adams", "George Bush"]),
   DT(D, "Comment s'appellent les mémoires de Michelle Obama ?", ["Becoming", "Dreams", "Yes We Can", "First Lady"]),
   DT(D, "Comment dit-on « la pelouse » ?", ["The lawn", "The law", "The grass field", "The park"])],
  [W(D, "Trouve le mot qui veut dire « un potager » (2 mots).", ["vegetable garden"]), W(D, "Trouve le mot qui veut dire « encourager ».", "encourage"),
   W(D, "Trouve le mot qui veut dire « des animaux de compagnie ».", "pets"), W(D, "Trouve le mot qui veut dire « la vie privée » (2 mots).", ["private life"])])

# ═════════ PORTRAITS ═════════
F = "cu_portraits.html"
DZ(F, """
## La National Portrait Gallery de Londres
Fondée en **1856**, la **National Portrait Gallery** est le premier musée au monde consacré aux portraits. Son principe : on n'y expose pas les plus beaux tableaux, mais les portraits des personnes qui ont fait l'histoire et la culture britanniques. Son tout premier tableau, le portrait dit **Chandos**, serait l'une des rares images de **Shakespeare** peintes de son vivant. On y croise aussi les rois et reines Tudor, Elizabeth I parée de perles, les sœurs Brontë peintes par leur frère, Charles Darwin, des stars de la musique et du sport. Rénovée, elle a rouvert ses portes en 2023.

## Le portrait comme outil de pouvoir
Pendant des siècles, le portrait sert à montrer le pouvoir. Le peintre **Hans Holbein** représente Henri VIII debout, jambes écartées, épaules immenses : l'image d'un roi tout-puissant. Les portraits d'**Elizabeth I** sont soigneusement contrôlés : la reine y apparaît toujours jeune, couverte de bijoux et de symboles. Dans le célèbre *Armada Portrait*, peint après la victoire contre la flotte espagnole en 1588, sa main est posée sur un globe : l'Angleterre devient une puissance mondiale.

## Les portraits officiels américains
À Washington, la **National Portrait Gallery** de la Smithsonian Institution présente notamment les portraits de tous les présidents. En 2018, les portraits de Barack et Michelle Obama marquent un tournant : **Kehinde Wiley** peint le président assis devant un mur de feuillages et de fleurs symbolisant les lieux de sa vie (Hawaï, le Kenya, Chicago) ; **Amy Sherald** représente Michelle Obama dans une immense robe, la peau peinte en nuances de gris. Ce sont les premiers artistes noirs choisis pour des portraits présidentiels officiels, et les tableaux attirent des foules.

## Du portrait au selfie
En 1839, à Philadelphie, Robert Cornelius réalise ce que l'on considère comme le premier autoportrait photographique de l'histoire. Aujourd'hui, avec les smartphones, chacun fait son propre portrait : le mot **selfie** a été élu « mot de l'année » par les dictionnaires Oxford en 2013. Comme les rois d'autrefois, nous choisissons l'image que nous voulons donner de nous : la meilleure pose, le meilleur filtre… Un portrait n'est jamais tout à fait la réalité : c'est toujours une **mise en scène**.

## Écrire un portrait
Faire le portrait de quelqu'un, c'est aussi le décrire avec des mots : son apparence (*tall, curly hair, freckles*), son caractère (*shy, brave, funny*), ses goûts. L'**autoportrait** écrit, dans un journal ou un poème, est une façon de se découvrir soi-même.
[→ Voir aussi : la famille royale aujourd'hui](cu_famille_royale.html)
""", """
a portrait = un portrait
a painting = un tableau
a painter = un peintre
a museum = un musée
a queen = une reine
a selfie = un selfie
a face = un visage
a smile = un sourire
""", [
 ("Quelle est l'originalité de la National Portrait Gallery de Londres ?", ["Elle expose les portraits de ceux qui ont fait l'histoire britannique", "Elle n'expose que des paysages", "Elle est la plus récente du monde"], ""),
 ("Comment Holbein représente-t-il Henri VIII ?", ["Comme un roi tout-puissant aux épaules immenses", "Comme un enfant", "De dos"], ""),
 ("Que montre l'Armada Portrait d'Elizabeth I ?", ["La reine la main sur un globe, après la victoire de 1588", "La reine en vacances", "Un navire seulement"], ""),
 ("Qu'ont de particulier les portraits des Obama ?", ["Ce sont les premiers peints par des artistes noirs pour des portraits présidentiels officiels", "Ce sont des photos", "Ils sont en noir et blanc"], ""),
 ("Quel mot est élu « mot de l'année » en 2013 ?", ["Selfie", "Portrait", "Smartphone"], ""),
 ("Pourquoi un portrait n'est-il jamais tout à fait la réalité ?", ["C'est toujours une mise en scène", "Les peintres mentent toujours", "Les couleurs changent"], ""),
], [("**Hans Holbein**", "peintre allemand de la cour d'Henri VIII"), ("**Kehinde Wiley**", "peintre américain"), ("**Amy Sherald**", "peintre américaine")])
D = "pt"
culture(F, "Culture : Portraits and self-portraits", 'Portraits <span>&amp; selfies</span>',
  "Culture · de la National Portrait Gallery au selfie", ("#fde68a", "#7c2d12"),
  reperes("Des portraits royaux aux selfies, le portrait montre l'image que l'on veut donner de soi ou du pouvoir.",
    [("1588", "l'Armada Portrait d'Elizabeth I"), ("1839", "premier autoportrait photographique"), ("1856", "fondation de la National Portrait Gallery"),
     ("2013", "« selfie », mot de l'année"), ("2018", "les portraits officiels de Barack et Michelle Obama")],
    "a portrait, a self-portrait, a selfie, a painter, a gallery, a pose, a filter, an image"),
  {D: doc("Look at me!", [
    "The National Portrait Gallery in London opened in 1856. It shows portraits of famous people from British history: kings, queens, writers, scientists and pop stars.",
    "In the past, portraits showed power. In her portraits, Queen Elizabeth I always looks young and rich, with lots of pearls.",
    "In Washington, there are official portraits of all the American Presidents. In 2018, the portraits of Barack and Michelle Obama were painted by two Black artists. They are very colourful and modern.",
    "Today, everybody can make a self-portrait with a smartphone. In 2013, \"selfie\" became the word of the year.",
    "Like kings in the past, we choose our best pose and our best filter. A portrait never shows the whole truth."])},
  [TF(D, "The National Portrait Gallery opened in 1856.", True, "« opened in 1856 »."),
   TF(D, "It only shows portraits of kings.", False, "« kings, queens, writers, scientists and pop stars »."),
   TF(D, "Elizabeth I always looks old in her portraits.", False, "« always looks young »."),
   TF(D, "The Obamas' portraits were painted by two Black artists.", True, "« by two Black artists »."),
   TF(D, "\"Selfie\" became the word of the year in 2013.", True, "« In 2013 »."),
   TF(D, "A portrait always shows the whole truth.", False, "« never shows the whole truth »." )],
  [Q(D, "Who can you see at the National Portrait Gallery?", ["Famous people from British history.", "Only animals.", "Only landscapes."]),
   Q(D, "What did portraits show in the past?", ["Power.", "Poverty.", "Sport."]),
   Q(D, "How are the Obamas' portraits?", ["Colourful and modern.", "Black and white.", "Very small."]),
   Q(D, "What do we choose when we take a selfie?", ["Our best pose and our best filter.", "A painter.", "A museum."])],
  [DT(D, "Quel portrait célèbre représenterait Shakespeare ?", ["Le portrait Chandos", "L'Armada Portrait", "La Joconde", "Le portrait Holbein"]),
   DT(D, "Qui a peint Henri VIII ?", ["Hans Holbein", "Kehinde Wiley", "J. M. W. Turner", "Andy Warhol"]),
   DT(D, "Qui a peint le portrait de Michelle Obama ?", ["Amy Sherald", "Kehinde Wiley", "Banksy", "Frida Kahlo"]),
   DT(D, "Comment dit-on « des taches de rousseur » ?", ["Freckles", "Spots", "Dots", "Pimples"])],
  [W(D, "Trouve le mot qui veut dire « le pouvoir ».", "power"), W(D, "Trouve le mot qui veut dire « des perles ».", "pearls"),
   W(D, "Trouve le mot qui veut dire « colorés ».", "colourful"), W(D, "Trouve le mot qui veut dire « toute la vérité » (3 mots).", ["the whole truth"])])
END()
