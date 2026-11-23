import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
exec(open(_EA_OUT+"/cuhelp.py", encoding="utf-8").read())

# ═════════ ÉCOLE UK ═════════
F = "cu_ecole_uk.html"
DZ(F, """
## Un parcours en « Years »
En Angleterre, l'école est obligatoire à partir de 5 ans (beaucoup d'enfants entrent même en **Reception** à 4 ans), et l'on doit rester en formation jusqu'à 18 ans. Les classes sont numérotées dans l'ordre :
- la **primary school** va de la Year 1 à la Year 6 (de 5 à 11 ans) ;
- la **secondary school** commence en **Year 7** (11-12 ans, l'équivalent de la 6e) et va jusqu'à la Year 11 ;
- à 16 ans, les élèves passent les **GCSEs**, des examens dans une dizaine de matières, notés de 9 (la meilleure note) à 1 ;
- ensuite, en **sixth form** ou dans un **college**, ils préparent souvent trois **A-levels**, l'équivalent du bac, nécessaires pour entrer à l'université.
L'Écosse a son propre système, avec d'autres examens (les **Highers**).

## L'uniforme et la vie de l'école
Presque tous les élèves portent un **uniform** : blazer avec l'écusson de l'école, chemise, cravate (**tie**), pantalon ou jupe, chaussures noires. Ses partisans disent qu'il gomme les différences sociales et crée un sentiment d'appartenance ; ses opposants le trouvent cher et contraignant.
La journée commence souvent par l'**assembly**, un rassemblement de toute l'école ou d'un niveau, puis par l'appel avec le **form tutor**, le professeur principal. Les cours finissent vers 15 h 15, suivis d'activités (**clubs**, sport). À midi, on mange un repas chaud (**school dinner**) ou son **packed lunch**. On appelle les professeurs « *Sir* » ou « *Miss* ».
Beaucoup d'écoles sont divisées en **houses**, des équipes qui mélangent les âges et gagnent des points pour leurs résultats, leur comportement ou les compétitions sportives, comme à Poudlard. Les élèves les plus responsables peuvent devenir **prefects**. Une sanction classique est la **detention**, une retenue.

## Écoles publiques… et « public schools »
- La grande majorité des élèves vont dans des **state schools**, gratuites. La plupart sont des **comprehensive schools**, qui accueillent tout le monde ; quelques **grammar schools** sélectionnent leurs élèves par un examen à 11 ans, le **eleven-plus**.
- Environ 7 % des élèves fréquentent des **independent schools**, payantes, dont certaines s'appellent, de façon trompeuse, **public schools**. Les plus célèbres, comme **Eton** et Harrow, sont des internats (**boarding schools**) très chers qui ont formé de nombreux Premiers ministres. Leur rôle dans la reproduction des élites fait débat.
Les écoles publiques sont inspectées par l'**Ofsted**, qui publie une note pour chaque établissement.
[→ Voir aussi : le lycée américain](cu_lycee_us.html)
""", """
a uniform = un uniforme
a tie = une cravate
a teacher = un professeur
a pupil = un élève
an exam = un examen
a subject = une matière
lunch = le déjeuner
a timetable = un emploi du temps
""", [
 ("À quoi correspond la Year 7 ?", ["À la 6e, première année de secondary school", "À la terminale", "À la maternelle"], ""),
 ("Que passent les élèves à 16 ans ?", ["Les GCSEs", "Les A-levels", "Le bac français"], ""),
 ("Que sont les A-levels ?", ["L'équivalent du bac, pour entrer à l'université", "Un uniforme", "Une sanction"], ""),
 ("Qu'est-ce qu'une « house » ?", ["Une équipe mélangeant les âges qui gagne des points", "La maison du directeur", "Un internat"], ""),
 ("Qu'est-ce qu'une « public school » comme Eton ?", ["Une école privée payante et prestigieuse", "Une école publique gratuite", "Une université"], ""),
 ("Que pensent les partisans de l'uniforme ?", ["Il gomme les différences sociales et crée un sentiment d'appartenance", "Il coûte trop cher", "Il est inutile"], ""),
], [("Poudlard", "l'école de Harry Potter"), ("**Eton**", "internat fondé en 1440 près de Windsor")])
D = "ec"
culture(F, "Culture : School in the UK", 'School <span>in the UK</span>',
  "Culture · uniformes, houses, GCSEs et A-levels", ("#bfdbfe", "#7f1d1d"),
  reperes("Au Royaume-Uni, presque tous les élèves portent un uniforme. Les classes s'appellent Year 1 à Year 13, et les grands examens sont les GCSEs (16 ans) et les A-levels (18 ans).",
    [("4 – 5 ans", "Reception, puis Year 1"), ("11 ans", "Year 7, entrée en secondary school"), ("16 ans", "les GCSEs, notés de 9 à 1"),
     ("18 ans", "les A-levels, pour l'université"), ("environ 7 %", "des élèves en école privée (independent school)")],
    "a uniform, a tie, a house, an assembly, a form tutor, a detention, GCSEs, A-levels"),
  {D: doc("A day at Oakfield Academy", [
    "My name is Amira and I'm in Year 8 at Oakfield Academy, a state school in Leeds. Like almost all British pupils, I wear a uniform: a black blazer, a white shirt and a blue and gold tie.",
    "School starts at 8:45 with registration with my form tutor. On Mondays, we have an assembly with the whole year group. We call our teachers \"Sir\" or \"Miss\".",
    "Our school has four houses. You get points for good work, good behaviour and sport. At the end of the year, the best house wins a cup. If you misbehave, you can get a detention.",
    "At lunchtime, I usually have a packed lunch, but some of my friends have a school dinner. School finishes at 3:15, and then I go to the drama club.",
    "In Year 11, we will take our GCSEs. After that, I want to stay in the sixth form and study three A-levels, then go to university."])},
  [TF(D, "Amira goes to a private school.", False, "« a state school »."),
   TF(D, "Amira wears a uniform.", True, "« I wear a uniform »."),
   TF(D, "Pupils call their teachers by their first name.", False, "« \"Sir\" or \"Miss\" »."),
   TF(D, "You get house points for good behaviour.", True, "« points for good work, good behaviour and sport »."),
   TF(D, "School finishes at 5 pm.", False, "« at 3:15 »."),
   TF(D, "Amira will take her GCSEs in Year 11.", True, "« In Year 11, we will take our GCSEs »." )],
  [Q(D, "What does Amira wear?", ["A blazer, a shirt and a tie.", "Jeans and a T-shirt.", "A sports kit."]),
   Q(D, "What happens on Mondays?", ["An assembly with the whole year group.", "A detention.", "A school trip."]),
   Q(D, "What does the best house win?", ["A cup.", "A holiday.", "Money."]),
   Q(D, "What does Amira want to do after her GCSEs?", ["Study three A-levels in the sixth form.", "Stop school.", "Work in a shop."])],
  [DT(D, "Comment dit-on « une retenue » ?", ["A detention", "A retention", "A punishment day", "A lesson"]),
   DT(D, "Comment s'appelle le panier-repas apporté de la maison ?", ["A packed lunch", "A school dinner", "A lunch box party", "A canteen"]),
   DT(D, "Quel organisme inspecte les écoles ?", ["L'Ofsted", "Le NHS", "La BBC", "Le MI5"]),
   DT(D, "Comment s'appelle l'examen de sélection à 11 ans ?", ["L'eleven-plus", "Le GCSE", "Le SAT", "Le Higher"])],
  [W(D, "Trouve le mot qui veut dire « l'appel ».", "registration"), W(D, "Trouve le mot qui veut dire « le comportement ».", "behaviour"),
   W(D, "Trouve le mot qui veut dire « se conduit mal ».", "misbehave"), W(D, "Trouve le mot qui veut dire « le club de théâtre » (2 mots).", ["drama club", "the drama club"])])

# ═════════ GÉOGRAPHIE USA ═════════
F = "cu_geographie_usa.html"
DZ(F, """
## Un pays-continent
Avec environ 9,8 millions de km², les **États-Unis** sont près de 18 fois plus grands que la France métropolitaine. Ils comptent 50 États et environ 340 millions d'habitants. Le pays s'étend sur plusieurs **time zones** (fuseaux horaires) : quand il est 9 h à New York, il est 6 h à Los Angeles. L'Alaska et Hawaï sont séparés du reste du pays, que l'on appelle les « 48 États contigus » (**the lower 48**).

## Les grandes régions
- **New England** (Nouvelle-Angleterre), au nord-est : les premières colonies, Boston, les universités prestigieuses, les forêts aux couleurs flamboyantes en automne (**fall foliage**).
- **The South** : un climat chaud et humide, l'héritage des plantations et de l'esclavage, la musique (blues, jazz, country), la **Bible Belt**, les ouragans sur la côte.
- **The Midwest** : les **Great Plains**, immenses plaines agricoles de maïs et de blé (le « grenier » du pays), les **Great Lakes** (cinq lacs immenses partagés avec le Canada), Chicago. On y trouve aussi la **Tornado Alley**, souvent frappée par des tornades.
- **The West** : les **Rocky Mountains**, les déserts du Sud-Ouest, le Nevada, l'Arizona, la Californie et la côte Pacifique.
- Plus au nord-ouest, le **Pacific Northwest** (Seattle, Portland) est connu pour ses forêts et sa pluie.

## Fleuves et montagnes
Le **Mississippi**, long d'environ 3 700 km, traverse le pays du nord au sud jusqu'au golfe du Mexique ; avec son affluent le Missouri, il forme l'un des plus grands systèmes fluviaux du monde. À l'est s'élèvent les **Appalachians**, montagnes anciennes et arrondies ; à l'ouest, les **Rocheuses**, beaucoup plus hautes. Le point culminant du pays, le **Denali**, en Alaska, atteint environ 6 190 mètres. La **Death Valley**, en Californie, est l'un des endroits les plus chauds de la planète.

## Les parcs nationaux
En **1872**, **Yellowstone** devient le premier parc national du monde. On y voit des geysers comme Old Faithful, des sources chaudes multicolores, des bisons et des grizzlis. Le **Grand Canyon**, en Arizona, creusé par le fleuve Colorado, mesure près de 450 km de long et jusqu'à 1,8 km de profondeur. **Yosemite**, en Californie, est célèbre pour ses falaises de granit et ses séquoias géants. Un service fédéral, le **National Park Service**, créé en 1916, protège aujourd'hui plus de 60 parcs nationaux, visités chaque année par des centaines de millions de personnes. Le président **Theodore Roosevelt** a beaucoup fait pour la protection de la nature. Mais ces espaces ont souvent été pris aux peuples amérindiens qui y vivaient.
[→ Voir aussi : villes et États américains](cu_villes_etats.html)
""", """
a mountain = une montagne
a river = un fleuve
a lake = un lac
a desert = un désert
a forest = une forêt
a canyon = un canyon
a bear = un ours
a plain = une plaine
""", [
 ("Combien de fois les États-Unis sont-ils plus grands que la France ?", ["Près de 18 fois", "2 fois", "100 fois"], ""),
 ("Pourquoi n'est-il pas la même heure à New York et à Los Angeles ?", ["Le pays s'étend sur plusieurs fuseaux horaires", "Les horloges sont fausses", "C'est l'heure d'été"], ""),
 ("Qu'est-ce qui caractérise le Midwest ?", ["Les grandes plaines agricoles et les Grands Lacs", "Les plages et le surf", "Les montagnes enneigées seulement"], ""),
 ("Quel fleuve traverse le pays du nord au sud ?", ["Le Mississippi", "La Tamise", "Le Rio Grande"], ""),
 ("Quel est le premier parc national du monde ?", ["Yellowstone, en 1872", "Le Grand Canyon", "Central Park"], ""),
 ("Qui a creusé le Grand Canyon ?", ["Le fleuve Colorado", "Des mineurs", "Un tremblement de terre"], ""),
], [("**Theodore Roosevelt**", "président de 1901 à 1909")])
D = "ge"
culture(F, "Culture : The geography of the USA", 'The geography <span>of the USA</span>',
  "Culture · régions, fleuves et parcs nationaux", ("#bbf7d0", "#b45309"),
  reperes("Les États-Unis sont un pays immense aux paysages très variés : plaines, montagnes, déserts, forêts et côtes.",
    [("50", "États"), ("environ 340 millions", "d'habitants"), ("1872", "Yellowstone, premier parc national du monde"),
     ("1916", "création du National Park Service"), ("environ 3 700 km", "longueur du Mississippi"), ("6 190 m", "le Denali, point culminant")],
    "a region, a mountain range, a river, a lake, a plain, a desert, a canyon, a national park"),
  {D: doc("Coast to coast", [
    "The USA is a huge country: it is about 18 times bigger than France. From New York to Los Angeles, there is a three-hour time difference.",
    "In the north-east, New England is famous for its history and its beautiful autumn colours. The South is hot, and it is the home of blues, jazz and country music.",
    "The Midwest has enormous plains with fields of corn and wheat, and the Great Lakes. In the West, there are the Rocky Mountains, deserts and the Pacific coast.",
    "The Mississippi is the most famous river. It flows from the north to the Gulf of Mexico.",
    "The USA created the first national park in the world, Yellowstone, in 1872. You can see geysers, bison and bears there. The Grand Canyon, in Arizona, is another wonderful natural site."])},
  [TF(D, "The USA is about 18 times bigger than France.", True, "« about 18 times bigger »."),
   TF(D, "It is the same time in New York and Los Angeles.", False, "« a three-hour time difference »."),
   TF(D, "The South is cold.", False, "« The South is hot »."),
   TF(D, "The Midwest has fields of corn and wheat.", True, "« fields of corn and wheat »."),
   TF(D, "The Mississippi flows to the Gulf of Mexico.", True, "« to the Gulf of Mexico »."),
   TF(D, "The Grand Canyon is in Florida.", False, "« in Arizona »." )],
  [Q(D, "What is New England famous for?", ["Its history and autumn colours.", "Its deserts.", "Its volcanoes."]),
   Q(D, "What can you find in the West?", ["The Rocky Mountains, deserts and the Pacific coast.", "The Great Lakes.", "New England."]),
   Q(D, "What was the first national park in the world?", ["Yellowstone.", "The Grand Canyon.", "Central Park."]),
   Q(D, "What can you see in Yellowstone?", ["Geysers, bison and bears.", "Kangaroos.", "Penguins."])],
  [DT(D, "Combien de Grands Lacs y a-t-il ?", ["Cinq", "Deux", "Dix", "Cinquante"]),
   DT(D, "Où se trouve le Denali ?", ["En Alaska", "Au Colorado", "À Hawaï", "Au Texas"]),
   DT(D, "Comment s'appelle la région souvent frappée par les tornades ?", ["Tornado Alley", "Death Valley", "Bible Belt", "Silicon Valley"]),
   DT(D, "Comment dit-on « fuseau horaire » ?", ["A time zone", "A time line", "A clock area", "A day zone"])],
  [W(D, "Trouve le mot qui veut dire « énorme ».", "huge"), W(D, "Trouve le mot qui veut dire « champs ».", "fields"),
   W(D, "Trouve le mot qui veut dire « coule » (un fleuve).", "flows"), W(D, "Trouve le mot qui veut dire « ours » (pluriel).", "bears")])

# ═════════ FÊTES ═════════
F = "cu_fetes_origines.html"
DZ(F, """
## Halloween (31 octobre)
Halloween vient d'une ancienne fête celte, **Samhain**, qui marquait la fin des récoltes et le début de l'hiver : on croyait que, cette nuit-là, la frontière entre le monde des vivants et celui des morts s'ouvrait. Le nom vient de **All Hallows' Eve**, la veille de la Toussaint. Au 19e siècle, les immigrants irlandais et écossais apportent la tradition aux États-Unis, où elle devient une immense fête populaire. En Irlande, on creusait des navets pour en faire des lanternes ; en Amérique, on les remplace par des citrouilles : c'est le **jack-o'-lantern**. Les enfants déguisés font du porte-à-porte en criant « *Trick or treat!* » pour obtenir des bonbons.

## Bonfire Night (5 novembre)
En 1605, un groupe de catholiques prépare la **Gunpowder Plot** (la conspiration des Poudres) : faire exploser le Parlement de Londres avec 36 barils de poudre, pendant la visite du roi protestant Jacques Ier. **Guy Fawkes**, chargé de garder les explosifs, est arrêté dans les caves dans la nuit du 4 au 5 novembre. Depuis, les Britanniques célèbrent l'échec du complot avec des feux de joie (**bonfires**), sur lesquels on brûlait autrefois une effigie de Fawkes, le « guy », et des feux d'artifice (**fireworks**). Une comptine traditionnelle commence par « *Remember, remember the fifth of November* ». Le masque stylisé de Guy Fawkes est aujourd'hui utilisé par certains manifestants.

## Thanksgiving (4e jeudi de novembre)
On fait remonter Thanksgiving à **1621** : à Plymouth, les **Pilgrims** et les Amérindiens **Wampanoag** partagent un repas de récolte après le premier hiver, très meurtrier pour les colons. En 1863, en pleine guerre de Sécession, Abraham Lincoln en fait une fête nationale. Aujourd'hui, c'est la grande fête familiale américaine : dinde (**turkey**), purée, sauce aux airelles, tarte à la citrouille, matchs de football américain, et la grande parade du magasin Macy's à New York, depuis 1924. Chaque année, le président « gracie » une dinde. Pour certains Amérindiens, cette date rappelle surtout la colonisation : depuis 1970, ils organisent ce jour-là un **National Day of Mourning** (journée de deuil).

## Christmas à l'anglaise
Le sapin de Noël devient à la mode au Royaume-Uni grâce à la reine Victoria et au prince Albert, d'origine allemande. On ouvre des **Christmas crackers**, des papillotes qui claquent et contiennent un chapeau en papier et une blague ; on mange de la dinde, des **mince pies** et le **Christmas pudding**. À 15 h le 25 décembre, beaucoup regardent le message de Noël du roi, une tradition commencée à la radio en 1932. Les enfants vont voir une **pantomime**, un spectacle comique et familial. Le **Santa Claus** américain vient du **Sinterklaas** des colons hollandais de New York ; son image en costume rouge a été popularisée par des illustrateurs et par la publicité au 20e siècle.

## St Patrick's Day (17 mars)
C'est la fête de saint Patrick, qui aurait évangélisé l'Irlande au 5e siècle et expliqué la Trinité avec un trèfle (**shamrock**). Les grands défilés ont d'abord été organisés… en Amérique, par les immigrants irlandais. Depuis 1962, Chicago teint sa rivière en vert. Partout, on porte du vert et on célèbre la culture irlandaise.
[→ Voir aussi : les Pères pèlerins et le premier Thanksgiving](cu_pilgrims.html)
""", """
a pumpkin = une citrouille
a costume = un déguisement
sweets = les bonbons
a bonfire = un feu de joie
fireworks = un feu d'artifice
a turkey = une dinde
a parade = un défilé
a Christmas tree = un sapin de Noël
""", [
 ("De quelle fête celte vient Halloween ?", ["Samhain", "Noël", "Thanksgiving"], ""),
 ("Pourquoi remplace-t-on les navets par des citrouilles en Amérique ?", ["Les immigrants trouvent des citrouilles sur place", "Les navets sont interdits", "Pour faire de la soupe"], ""),
 ("Que célèbre la Bonfire Night ?", ["L'échec d'un complot pour faire exploser le Parlement en 1605", "La fin de la guerre", "L'anniversaire du roi"], ""),
 ("À quel événement remonte Thanksgiving ?", ["Un repas de récolte entre Pilgrims et Wampanoag en 1621", "L'indépendance en 1776", "La découverte de l'Amérique"], ""),
 ("Que trouve-t-on dans un Christmas cracker ?", ["Un chapeau en papier et une blague", "Du chocolat seulement", "Une dinde"], ""),
 ("Où les grands défilés de la Saint-Patrick ont-ils commencé ?", ["En Amérique, chez les immigrants irlandais", "À Dublin", "À Londres"], ""),
], [("Jacques Ier", "roi d'Angleterre et d'Écosse de 1603 à 1625"), ("Wampanoag", "peuple amérindien du Massachusetts actuel")])
D = "fe"
culture(F, "Culture : Holidays and their origins", 'Holidays <span>&amp; origins</span>',
  "Culture · Halloween, Bonfire Night, Thanksgiving, Christmas, St Patrick's Day", ("#fdba74", "#7c2d12"),
  reperes("Chaque grande fête du monde anglophone a une histoire : celte, religieuse, politique ou coloniale.",
    [("31 octobre", "Halloween, héritier de la fête celte de Samhain"), ("5 novembre", "Bonfire Night, souvenir du complot de 1605"),
     ("4e jeudi de novembre", "Thanksgiving, en souvenir de 1621"), ("25 décembre", "Christmas, avec crackers et message du roi"), ("17 mars", "St Patrick's Day")],
    "a holiday, a tradition, a pumpkin, trick or treat, a bonfire, fireworks, a turkey, a parade"),
  {D: doc("Why do we celebrate?", [
    "Halloween comes from an old Celtic festival. Irish immigrants took it to America, where people started to carve pumpkins. Today, children in costumes go from door to door and say \"Trick or treat!\".",
    "On 5 November, the British celebrate Bonfire Night. In 1605, Guy Fawkes and his friends wanted to blow up Parliament, but he was arrested. People light bonfires and watch fireworks.",
    "Thanksgiving is on the fourth Thursday of November. It remembers a harvest meal in 1621 between the Pilgrims and Native Americans. Families eat turkey and pumpkin pie.",
    "In Britain, people pull Christmas crackers and eat Christmas pudding. Many watch the King's Christmas message on TV.",
    "On 17 March, people all over the world wear green for St Patrick's Day, the national day of Ireland. In Chicago, the river is even coloured green!"])},
  [TF(D, "Halloween comes from an old Celtic festival.", True, "« an old Celtic festival »."),
   TF(D, "Guy Fawkes managed to blow up Parliament.", False, "« he was arrested »."),
   TF(D, "Thanksgiving is in December.", False, "« the fourth Thursday of November »."),
   TF(D, "Families eat turkey at Thanksgiving.", True, "« Families eat turkey »."),
   TF(D, "Many British people watch the King's Christmas message.", True, "« watch the King's Christmas message »."),
   TF(D, "On St Patrick's Day, people wear red.", False, "« wear green »." )],
  [Q(D, "What do children say at Halloween?", ["\"Trick or treat!\"", "\"Happy New Year!\"", "\"Cheers!\""]),
   Q(D, "What did Guy Fawkes want to do?", ["Blow up Parliament.", "Become king.", "Leave England."]),
   Q(D, "What does Thanksgiving remember?", ["A harvest meal in 1621.", "The end of a war.", "The first Christmas."]),
   Q(D, "What happens to the river in Chicago?", ["It is coloured green.", "It freezes.", "It is closed."])],
  [DT(D, "Comment s'appelle la lanterne-citrouille ?", ["Un jack-o'-lantern", "Un pumpkin pie", "Un guy", "Un cracker"]),
   DT(D, "Quel président fait de Thanksgiving une fête nationale ?", ["Abraham Lincoln", "George Washington", "John F. Kennedy", "Theodore Roosevelt"]),
   DT(D, "Quel est le symbole de l'Irlande ?", ["Le trèfle (shamrock)", "La rose", "Le chardon", "La citrouille"]),
   DT(D, "Qui a rendu le sapin de Noël populaire au Royaume-Uni ?", ["Victoria et Albert", "Guy Fawkes", "Henri VIII", "Saint Patrick"])],
  [W(D, "Trouve le mot qui veut dire « sculpter, creuser ».", "carve"), W(D, "Trouve le mot qui veut dire « de porte en porte » (4 mots).", ["from door to door"]),
   W(D, "Trouve le mot qui veut dire « faire exploser » (2 mots).", ["blow up"]), W(D, "Trouve le mot qui veut dire « récolte ».", "harvest")])

# ═════════ SCIENCES ═════════
F = "cu_sciences.html"
DZ(F, """
## Isaac Newton et la gravité
**Isaac Newton** (1643-1727), savant anglais, est l'un des plus grands scientifiques de l'histoire. Selon une anecdote qu'il racontait lui-même, la chute d'une pomme dans son jardin l'aurait fait réfléchir à la force qui attire les objets vers la Terre. Dans les *Principia* (1687), il formule la loi de la **gravitation universelle** et les trois **lois du mouvement** : la même force explique la chute d'une pomme et le mouvement de la Lune. Il travaille aussi sur la lumière et invente un nouveau type de télescope.

## Charles Darwin et l'évolution
De 1831 à 1836, le jeune naturaliste **Charles Darwin** (1809-1882) fait le tour du monde à bord du navire **HMS Beagle**. Aux îles **Galápagos**, il remarque que les pinsons ont des becs différents selon les îles. En 1859, il publie *On the Origin of Species* : les espèces **évoluent** au fil du temps par la **sélection naturelle** ; les individus les mieux adaptés à leur milieu survivent et transmettent leurs caractères. Sa théorie fait scandale, car elle contredit la lecture littérale de la Bible, mais elle est aujourd'hui le fondement de la biologie.

## Ada Lovelace et Alan Turing, pionniers de l'informatique
En 1843, la mathématicienne **Ada Lovelace** écrit ce que l'on considère comme le premier programme informatique, pour une machine à calculer imaginée par Charles Babbage. Un siècle plus tard, **Alan Turing** (1912-1954), à Bletchley Park, contribue à casser les codes de la machine allemande **Enigma** pendant la Seconde Guerre mondiale, ce qui aurait raccourci la guerre. Il pose aussi les bases théoriques de l'ordinateur et de l'intelligence artificielle (le **Turing test**, 1950). Condamné en 1952 pour homosexualité, alors illégale, il meurt en 1954. Il a été gracié à titre posthume en 2013, et son portrait figure sur le billet de 50 livres depuis 2021.

## Des découvertes qui ont changé la vie
- En 1928, l'Écossais **Alexander Fleming** découvre par hasard la **pénicilline**, le premier antibiotique.
- En 1953, à Cambridge, James Watson et Francis Crick décrivent la structure en double hélice de l'**ADN**, en s'appuyant sur une image obtenue par la chercheuse **Rosalind Franklin**, longtemps oubliée.
- En 1989, l'informaticien britannique **Tim Berners-Lee** invente le **World Wide Web** au CERN, près de Genève, et choisit de ne pas le breveter pour qu'il reste gratuit pour tous.

## Les inventeurs américains
- **Alexander Graham Bell**, né en Écosse, dépose en 1876 aux États-Unis le brevet du **téléphone**.
- **Thomas Edison** (1847-1931) invente le phonographe (1877) et met au point une ampoule électrique durable (1879). Il dépose plus de 1 000 brevets et crée l'un des premiers laboratoires de recherche.
- Le **17 décembre 1903**, les frères **Wright** réalisent à Kitty Hawk le premier vol motorisé et contrôlé de l'histoire : 12 secondes et 37 mètres.
[→ Voir aussi : la révolution industrielle](cu_revolution_industrielle.html)
""", """
a scientist = un scientifique
an invention = une invention
a discovery = une découverte
an apple = une pomme
a computer = un ordinateur
a plane = un avion
a light bulb = une ampoule
a code = un code
""", [
 ("Qu'a formulé Newton ?", ["La loi de la gravitation universelle et les lois du mouvement", "La théorie de l'évolution", "Le World Wide Web"], ""),
 ("Qu'a remarqué Darwin aux Galápagos ?", ["Les pinsons ont des becs différents selon les îles", "Des dinosaures vivants", "Un volcan"], ""),
 ("Pourquoi la théorie de Darwin a-t-elle fait scandale ?", ["Elle contredisait la lecture littérale de la Bible", "Elle était fausse", "Elle était en français"], ""),
 ("Qu'a fait Alan Turing pendant la guerre ?", ["Il a aidé à casser les codes de la machine Enigma", "Il a piloté des avions", "Il a inventé la radio"], ""),
 ("Qu'a découvert Alexander Fleming ?", ["La pénicilline, premier antibiotique", "L'ADN", "Le téléphone"], ""),
 ("Pourquoi Tim Berners-Lee n'a-t-il pas breveté le Web ?", ["Pour qu'il reste gratuit pour tous", "Il a oublié", "C'était interdit"], ""),
], [("*Principia*", "ouvrage de Newton en latin"), ("Charles Babbage", "mathématicien et inventeur anglais"), ("Bletchley Park", "centre britannique de décryptage"),
    ("CERN", "laboratoire européen de physique")])
D = "sci"
culture(F, "Culture : Science and inventions", 'Science <span>&amp; inventions</span>',
  "Culture · Newton, Darwin, Turing, Edison et les autres", ("#a5f3fc", "#1d4ed8"),
  reperes("Des savants et inventeurs britanniques et américains ont transformé notre façon de comprendre le monde et de vivre.",
    [("1687", "Newton : la gravitation universelle"), ("1859", "Darwin : De l'origine des espèces"), ("1876", "Bell : le téléphone"), ("1879", "Edison : l'ampoule électrique"),
     ("1903", "premier vol des frères Wright"), ("1928", "Fleming : la pénicilline"), ("1989", "Berners-Lee : le World Wide Web")],
    "a scientist, an inventor, a discovery, an invention, a theory, gravity, evolution, a patent"),
  {D: doc("Great minds", [
    "Isaac Newton was an English scientist. According to a famous story, an apple fell from a tree and made him think about gravity. He explained why things fall and how the planets move.",
    "Charles Darwin travelled around the world on a ship. In 1859, he published his theory of evolution: animals and plants change slowly over time.",
    "During the Second World War, Alan Turing helped to break the secret codes of the German army. He is also one of the fathers of the computer.",
    "In America, Thomas Edison made the first practical light bulb, and in 1903 the Wright brothers flew the first plane. It flew for only 12 seconds!",
    "In 1989, a British scientist, Tim Berners-Lee, invented the World Wide Web. He decided to give it to the world for free."])},
  [TF(D, "Newton was an American scientist.", False, "« an English scientist »."),
   TF(D, "An apple made Newton think about gravity.", True, "« an apple fell from a tree »."),
   TF(D, "Darwin published his theory of evolution in 1859.", True, "« In 1859 »."),
   TF(D, "Turing helped to break German codes.", True, "« break the secret codes of the German army »."),
   TF(D, "The first plane flew for two hours.", False, "« only 12 seconds »."),
   TF(D, "Tim Berners-Lee sold the Web for a lot of money.", False, "« for free »." )],
  [Q(D, "What did Newton explain?", ["Why things fall and how planets move.", "How to make a computer.", "How animals change."]),
   Q(D, "What is the theory of evolution?", ["Animals and plants change slowly over time.", "The Earth is flat.", "Apples fall from trees."]),
   Q(D, "What did Edison make?", ["The first practical light bulb.", "The first plane.", "The Web."]),
   Q(D, "Who invented the World Wide Web?", ["Tim Berners-Lee.", "Thomas Edison.", "Alan Turing."])],
  [DT(D, "Sur quel navire voyage Darwin ?", ["Le HMS Beagle", "Le Titanic", "Le Mayflower", "L'Endeavour"]),
   DT(D, "Quelle mathématicienne a écrit le premier programme ?", ["Ada Lovelace", "Rosalind Franklin", "Marie Curie", "Florence Nightingale"]),
   DT(D, "Qui figure sur le billet de 50 livres depuis 2021 ?", ["Alan Turing", "Isaac Newton", "Charles Darwin", "Winston Churchill"]),
   DT(D, "Qui dépose le brevet du téléphone en 1876 ?", ["Alexander Graham Bell", "Thomas Edison", "Les frères Wright", "Isaac Newton"])],
  [W(D, "Trouve le mot qui veut dire « la gravité ».", "gravity"), W(D, "Trouve le mot qui veut dire « a publié ».", "published"),
   W(D, "Trouve le mot qui veut dire « casser » (des codes).", "break"), W(D, "Trouve le mot qui veut dire « une ampoule » (2 mots).", ["light bulb", "practical light bulb"])])

# ═════════ HISTOIRE DE L'ANGLAIS ═════════
F = "cu_histoire_anglais.html"
DZ(F, """
## Avant l'anglais
Il y a 2 000 ans, les habitants de la Grande-Bretagne, les **Britons**, parlent des langues celtiques, ancêtres du gallois et du gaélique. Les Romains occupent l'île de 43 à 410 environ ; ils laissent des villes et des routes, mais peu de mots.

## Les Anglo-Saxons : naissance du vieil anglais
Au 5e siècle, des peuples germaniques venus des côtes de l'actuelle Allemagne et du Danemark, les **Angles**, les **Saxons** et les Jutes, s'installent en Grande-Bretagne. Leur langue devient l'**Old English** (vieil anglais). Le mot « England » vient de « Angle-land », la terre des Angles. Les mots les plus simples et les plus fréquents de l'anglais viennent de là : *house*, *water*, *eat*, *child*, *love*, *the*, *is*… Le grand poème épique *Beowulf* est écrit dans cette langue, qu'un anglophone d'aujourd'hui ne comprend plus sans l'avoir étudiée.

## Les Vikings
À partir de la fin du 8e siècle, les **Vikings** venus de Scandinavie attaquent puis s'installent dans le nord et l'est de l'Angleterre. Leur langue, le vieux norrois, apporte des mots essentiels : *sky*, *egg*, *window*, *knife*, *skirt*, et même les pronoms *they*, *them*, *their*.

## 1066 : le français à la cour
Après la conquête de **Guillaume le Conquérant** en 1066, la noblesse anglaise parle français pendant environ trois siècles. Des milliers de mots français entrent dans l'anglais, notamment dans le droit, la politique, la cuisine et la mode : *government*, *justice*, *court*, *beauty*, *fashion*… D'où des paires célèbres : l'animal vivant, gardé par les paysans anglo-saxons, a un nom germanique (*cow*, *pig*, *sheep*), mais la viande servie aux seigneurs normands a un nom français (*beef*, *pork*, *mutton*). Environ un tiers du vocabulaire anglais vient du français, directement ou indirectement.

## Du moyen anglais à l'anglais moderne
Vers 1400, **Geoffrey Chaucer** écrit *The Canterbury Tales* en **Middle English**. En 1476, William Caxton installe la première imprimerie en Angleterre, ce qui aide à fixer l'orthographe. Mais au même moment, la prononciation des voyelles change profondément (le **Great Vowel Shift**) : c'est pourquoi l'orthographe anglaise ne correspond plus à la prononciation (*name*, *time*, *house* se prononçaient autrefois à peu près comme ils s'écrivent). **Shakespeare** (1564-1616) enrichit la langue de nombreux mots et expressions ; la Bible du roi Jacques (1611) marque aussi profondément la langue. En 1755, **Samuel Johnson** publie un grand dictionnaire. Aux États-Unis, **Noah Webster** simplifie l'orthographe dans son dictionnaire de 1828 : *colour* devient *color*, *centre* devient *center*.

## Une langue mondiale
Grâce à l'Empire britannique puis à la puissance des États-Unis, l'anglais se répand sur tous les continents. Il emprunte des mots au monde entier : *pyjamas* et *shampoo* (de l'Inde), *ketchup* (d'Asie), *chocolate* et *tomato* (du nahuatl, via l'espagnol), *kangaroo* (d'Australie). Aujourd'hui, environ 1,5 milliard de personnes parlent anglais, mais la grande majorité ne sont pas des locuteurs natifs : c'est la principale **lingua franca** du monde, la langue commune des échanges internationaux, de la science, d'Internet et de l'aviation. On parle même des **Englishes** du monde, chacun avec ses particularités.
[→ Voir aussi : 1066 et la conquête normande](cu_1066.html)
""", """
a language = une langue
a word = un mot
a dictionary = un dictionnaire
spelling = l'orthographe
pronunciation = la prononciation
a speaker = un locuteur
to borrow = emprunter
a king = un roi
""", [
 ("D'où vient le mot « England » ?", ["De « Angle-land », la terre des Angles", "Du latin", "Du français"], ""),
 ("Quels mots les Vikings ont-ils apportés ?", ["sky, egg, window, they", "beef, justice, fashion", "pyjamas, shampoo"], ""),
 ("Pourquoi dit-on « cow » pour l'animal et « beef » pour la viande ?", ["Les paysans parlaient anglo-saxon, les seigneurs normands parlaient français", "C'est un hasard", "Pour éviter les confusions"], ""),
 ("Qu'explique le Great Vowel Shift ?", ["Pourquoi l'orthographe ne correspond plus à la prononciation", "L'arrivée des Vikings", "La naissance de l'Amérique"], ""),
 ("Qu'a fait Noah Webster ?", ["Il a simplifié l'orthographe américaine (color, center)", "Il a écrit Beowulf", "Il a inventé l'imprimerie"], ""),
 ("Que signifie « lingua franca » ?", ["Une langue commune des échanges internationaux", "La langue française", "Une langue morte"], ""),
], [("*Beowulf*", "poème épique anglo-saxon"), ("**Geoffrey Chaucer**", "poète anglais, vers 1343-1400"), ("**Samuel Johnson**", "écrivain et lexicographe anglais"),
    ("nahuatl", "langue des Aztèques")])
D = "he"
culture(F, "Culture : The history of English", 'The history <span>of English</span>',
  "Culture · Anglo-Saxons, Vikings, Normands… et langue mondiale", ("#ddd6fe", "#9a3412"),
  reperes("L'anglais est une langue germanique enrichie par le norrois des Vikings, puis par le français des Normands, avant de devenir la langue mondiale.",
    [("5e siècle", "arrivée des Angles et des Saxons : le vieil anglais"), ("8e – 11e siècle", "les Vikings"), ("1066", "conquête normande : le français à la cour"),
     ("vers 1400", "Chaucer, le moyen anglais"), ("1755", "dictionnaire de Samuel Johnson"), ("1828", "dictionnaire américain de Noah Webster")],
    "a language, a word, to borrow, spelling, pronunciation, a dictionary, a native speaker, a lingua franca"),
  {D: doc("Where do English words come from?", [
    "English is a Germanic language. In the 5th century, the Angles and the Saxons came from Germany and Denmark to Britain. The word \"England\" means \"the land of the Angles\".",
    "Later, the Vikings arrived. They gave English some very common words, like sky, egg and they.",
    "In 1066, the Normans conquered England. For about 300 years, the king and the nobles spoke French. That's why many English words come from French, like government, justice and beef.",
    "English spelling is difficult because the pronunciation changed, but the spelling didn't. Later, Americans simplified some words: colour became color.",
    "Today, about 1.5 billion people speak English, but most of them are not native speakers. English is the international language of science, travel and the Internet."])},
  [TF(D, "English is a Germanic language.", True, "« a Germanic language »."),
   TF(D, "The Angles and the Saxons came from Italy.", False, "« from Germany and Denmark »."),
   TF(D, "The Vikings gave English the word \"sky\".", True, "« like sky, egg and they »."),
   TF(D, "After 1066, the king spoke English.", False, "« the king and the nobles spoke French »."),
   TF(D, "Americans write \"color\" instead of \"colour\".", True, "« colour became color »."),
   TF(D, "Most English speakers are native speakers.", False, "« most of them are not native speakers »." )],
  [Q(D, "What does \"England\" mean?", ["The land of the Angles.", "The land of the Vikings.", "The land of the kings."]),
   Q(D, "Why do many English words come from French?", ["Because the Normans spoke French after 1066.", "Because of tourism.", "Because of Shakespeare."]),
   Q(D, "Why is English spelling difficult?", ["The pronunciation changed but the spelling didn't.", "There are too many letters.", "It has no rules at all."]),
   Q(D, "How many people speak English today?", ["About 1.5 billion.", "About 15 million.", "About 50 billion."])],
  [DT(D, "Quel poème est écrit en vieil anglais ?", ["Beowulf", "Hamlet", "The Canterbury Tales", "Paradise Lost"]),
   DT(D, "Qui écrit The Canterbury Tales ?", ["Geoffrey Chaucer", "William Shakespeare", "Samuel Johnson", "Noah Webster"]),
   DT(D, "Quel mot vient du français ?", ["Beef", "Egg", "Sky", "Water"]),
   DT(D, "Qui installe la première imprimerie en Angleterre en 1476 ?", ["William Caxton", "Guillaume le Conquérant", "Henri VIII", "Isaac Newton"])],
  [W(D, "Trouve le mot qui veut dire « nobles » (seigneurs).", "nobles"), W(D, "Trouve le mot qui veut dire « l'orthographe ».", "spelling"),
   W(D, "Trouve le mot qui veut dire « ont simplifié ».", "simplified"), W(D, "Trouve le mot qui veut dire « locuteurs natifs » (2 mots).", ["native speakers"])])

# ═════════ RELIGION ═════════
F = "cu_religion.html"
DZ(F, """
## Aux États-Unis : un État sans religion officielle…
Le **First Amendment** de la Constitution (1791) interdit au Congrès d'établir une religion officielle et garantit la liberté de culte : c'est la séparation de l'Église et de l'État (**separation of church and state**). Cette liberté remonte à l'histoire des colonies : beaucoup de colons, comme les Pilgrims ou les quakers, fuyaient les persécutions religieuses en Europe.

## … mais une société très religieuse
- La devise nationale est « ***In God We Trust*** », adoptée en 1956 et inscrite sur les billets. Le serment d'allégeance au drapeau, récité dans beaucoup d'écoles, comporte depuis 1954 les mots « *one nation under God* ».
- Environ 6 Américains sur 10 se disent chrétiens : protestants (dont de nombreux **evangelicals**), catholiques (environ un sur cinq), mormons (surtout dans l'Utah)… Il existe aussi des communautés juives, musulmanes, hindoues, bouddhistes.
- Le Sud et une partie du Midwest forment la **Bible Belt**, la « ceinture de la Bible », où la pratique religieuse est très forte. On y trouve des **megachurches** qui rassemblent des milliers de fidèles.
- La religion joue un rôle important en politique, notamment dans les débats sur l'avortement, le mariage ou l'école.
- Mais la société change : près de 3 Américains sur 10, surtout parmi les jeunes, se disent aujourd'hui sans religion (les **nones**).

## Au Royaume-Uni : une Église officielle…
L'**Église d'Angleterre** (Church of England, ou anglicane) est née en 1534, quand Henri VIII rompt avec le pape. C'est une Église **établie** : le roi en est le gouverneur suprême, et 26 évêques siègent à la Chambre des lords. L'Écosse a sa propre Église, presbytérienne (la Church of Scotland). En Irlande du Nord, l'opposition entre catholiques et protestants a marqué l'histoire, notamment pendant les Troubles. Dans les écoles anglaises, l'enseignement religieux (**RE**, religious education) est obligatoire, et la loi prévoit un temps de recueillement quotidien.

## … dans une société peu religieuse
Paradoxalement, les Britanniques sont beaucoup moins pratiquants que les Américains. Au recensement de 2021, moins de la moitié des habitants d'Angleterre et du pays de Galles se déclarent chrétiens (environ 46 %), plus d'un tiers se disent sans religion (environ 37 %), et environ 6,5 % sont musulmans, la deuxième religion du pays. Beaucoup d'églises ferment et sont transformées en appartements, en salles de spectacle ou en restaurants, tandis que d'autres communautés religieuses se développent.
[→ Voir aussi : le télévangélisme](cu_televangelisme.html)
""", """
a church = une église
God = Dieu
a belief = une croyance
religion = la religion
a Christian = un chrétien
a Muslim = un musulman
freedom = la liberté
to pray = prier
""", [
 ("Que garantit le First Amendment ?", ["La liberté de culte et l'absence de religion officielle", "Une religion d'État", "L'interdiction des églises"], ""),
 ("Quelle est la devise nationale des États-Unis ?", ["« In God We Trust »", "« Liberté, Égalité, Fraternité »", "« God Save the King »"], ""),
 ("Qu'est-ce que la Bible Belt ?", ["Une région du Sud où la pratique religieuse est très forte", "Une ceinture vendue dans les églises", "Une loi"], ""),
 ("Qui sont les « nones » ?", ["Les Américains sans religion", "Des religieuses", "Des évangéliques"], ""),
 ("Pourquoi dit-on que l'Église d'Angleterre est « établie » ?", ["Elle est l'Église officielle, liée à l'État et au roi", "Elle est très ancienne", "Elle est riche"], ""),
 ("Quel paradoxe montre le Royaume-Uni ?", ["Une Église officielle mais une société peu religieuse", "Aucune église mais beaucoup de croyants", "Une religion obligatoire"], ""),
], [("quakers", "mouvement religieux protestant pacifiste"), ("mormons", "membres de l'Église de Jésus-Christ des saints des derniers jours")])
D = "re"
culture(F, "Culture : Religion in the US and the UK", 'Religion <span>&amp; society</span>',
  "Culture · « In God We Trust » et l'Église d'Angleterre", ("#e9d5ff", "#1e3a8a"),
  reperes("Les États-Unis n'ont pas de religion officielle mais sont très religieux ; le Royaume-Uni a une Église officielle mais est peu pratiquant.",
    [("1534", "naissance de l'Église d'Angleterre"), ("1791", "First Amendment : liberté religieuse"), ("1956", "« In God We Trust » devient la devise américaine"),
     ("environ 6 sur 10", "Américains se disant chrétiens"), ("2021", "moins de la moitié des Anglais et Gallois se disent chrétiens")],
    "a religion, a church, a belief, freedom of religion, Christianity, Islam, an atheist, secular"),
  {D: doc("God and the state", [
    "In the USA, there is no official religion. The Constitution protects freedom of religion. Many early colonists came to America to practise their religion freely.",
    "But religion is very important in American life. The national motto is \"In God We Trust\", and it is printed on dollar bills. About six Americans out of ten are Christians.",
    "In the South, many people go to church every Sunday. This region is called the Bible Belt. However, more and more young Americans say they have no religion.",
    "In England, the Church of England is the official church, and the King is its head. It was created by Henry VIII in the 16th century.",
    "But today, British people are much less religious than Americans. Less than half of the population say they are Christian, and many old churches have become flats or restaurants."])},
  [TF(D, "There is an official religion in the USA.", False, "« there is no official religion »."),
   TF(D, "\"In God We Trust\" is printed on dollar bills.", True, "« printed on dollar bills »."),
   TF(D, "The Bible Belt is in the North.", False, "« In the South »."),
   TF(D, "More and more young Americans have no religion.", True, "« more and more young Americans »."),
   TF(D, "The Church of England was created by Henry VIII.", True, "« created by Henry VIII »."),
   TF(D, "British people are more religious than Americans.", False, "« much less religious »." )],
  [Q(D, "What does the Constitution protect?", ["Freedom of religion.", "One official church.", "The King."]),
   Q(D, "What is the American national motto?", ["In God We Trust.", "God Save the King.", "Yes We Can."]),
   Q(D, "Who is the head of the Church of England?", ["The King.", "The Pope.", "The Prime Minister."]),
   Q(D, "What has happened to many old British churches?", ["They have become flats or restaurants.", "They have become bigger.", "They have become schools only."])],
  [DT(D, "En quelle année Henri VIII rompt-il avec le pape ?", ["1534", "1066", "1776", "1605"]),
   DT(D, "Dans quel État vivent beaucoup de mormons ?", ["L'Utah", "La Floride", "New York", "L'Alaska"]),
   DT(D, "Quelle est la deuxième religion d'Angleterre et du pays de Galles ?", ["L'islam", "Le bouddhisme", "Le judaïsme", "L'hindouisme"]),
   DT(D, "Comment s'appelle l'enseignement religieux dans les écoles anglaises ?", ["RE", "PE", "RS", "GCSE"])],
  [W(D, "Trouve le mot qui veut dire « librement ».", "freely"), W(D, "Trouve le mot qui veut dire « la devise ».", ["motto", "national motto"]),
   W(D, "Trouve le mot qui veut dire « cependant ».", ["However", "however"]), W(D, "Trouve le mot qui veut dire « moins de la moitié » (3 mots).", ["less than half"])])

# ═════════ POLAR ET ESPIONS ═════════
F = "cu_polar_espions.html"
DZ(F, """
## Sherlock Holmes
En 1887, un jeune médecin écossais, **Arthur Conan Doyle**, publie *A Study in Scarlet*, où apparaît un détective privé qui vit à Londres au **221B Baker Street** : **Sherlock Holmes**. Accompagné de son ami le docteur **Watson**, narrateur des histoires, Holmes résout les énigmes grâce à son sens de l'observation et à la **deduction** : un détail sur une chaussure ou une manche lui suffit pour deviner d'où vient quelqu'un. Il joue du violon, fume la pipe et affronte son ennemi juré, le professeur **Moriarty**. En 1893, Conan Doyle, lassé de son héros, le fait mourir ; devant la colère des lecteurs, il finit par le ressusciter ! Holmes est l'un des personnages les plus adaptés au cinéma et à la télévision, par exemple dans la série *Sherlock* de la BBC (2010), qui le transpose au 21e siècle. Un musée l'attend aujourd'hui au 221B Baker Street.

## Agatha Christie, la reine du crime
**Agatha Christie** (1890-1976) est la romancière la plus vendue de tous les temps, avec environ deux milliards d'exemplaires. Elle a créé deux détectives célèbres : **Hercule Poirot**, un petit Belge élégant, fier de ses « petites cellules grises », et **Miss Marple**, une vieille dame d'un village anglais à qui rien n'échappe. Ses romans sont des **whodunits** (« qui l'a fait ? ») : un meurtre, un lieu fermé, une liste de suspects, et le lecteur essaie de trouver le coupable avant le détective. *Murder on the Orient Express* (1934) et *And Then There Were None* (1939) sont parmi les plus célèbres. Sa pièce *The Mousetrap* est jouée à Londres sans interruption depuis 1952 (sauf pendant la pandémie de Covid), un record mondial.

## James Bond
**Ian Fleming**, ancien officier du renseignement de la marine britannique pendant la Seconde Guerre mondiale, publie en 1953 *Casino Royale*, premier roman de **James Bond**, l'agent **007** du **MI6**, le service secret britannique, qui possède le « permis de tuer ». Gadgets, voitures de luxe, ennemis mégalomanes, voyages exotiques et répliques célèbres (« *Bond. James Bond.* ») : la série de films, commencée en 1962 avec *Dr. No* et Sean Connery, est l'une des plus longues de l'histoire du cinéma. Bond a été joué notamment par Roger Moore, Pierce Brosnan et Daniel Craig. Chaque nouveau choix d'acteur est un événement.

## Les vrais espions
Le Royaume-Uni a réellement deux grands services : le **MI5** pour la sécurité intérieure, et le **MI6** pour le renseignement à l'étranger. Pendant la guerre froide, le pays a été secoué par l'affaire des **Cambridge Five**, cinq diplômés de Cambridge, dont certains travaillaient au plus haut niveau des services secrets, qui espionnaient en réalité pour l'URSS. L'écrivain **John le Carré**, lui-même ancien agent, en a tiré des romans d'espionnage beaucoup plus réalistes et sombres que les aventures de Bond.
[→ Voir aussi : les grands romans](cu_romans.html)
""", """
a detective = un détective
a crime = un crime
a clue = un indice
a suspect = un suspect
a murder = un meurtre
a spy = un espion
a secret = un secret
a gadget = un gadget
""", [
 ("Où habite Sherlock Holmes ?", ["Au 221B Baker Street, à Londres", "À New York", "À Édimbourg"], ""),
 ("Comment Holmes résout-il les énigmes ?", ["Grâce à l'observation et à la déduction", "Grâce à la magie", "Grâce à des aveux"], ""),
 ("Pourquoi Conan Doyle a-t-il ressuscité Holmes ?", ["À cause de la colère des lecteurs", "Par erreur", "Pour un film"], ""),
 ("Qu'est-ce qu'un « whodunit » ?", ["Un roman où il faut trouver le coupable", "Un roman d'amour", "Un film d'action"], ""),
 ("Pour quel service travaille James Bond ?", ["Le MI6, service secret britannique", "Le FBI", "Scotland Yard"], ""),
 ("Qui étaient les Cambridge Five ?", ["Des Britanniques qui espionnaient pour l'URSS", "Des détectives", "Des acteurs de James Bond"], ""),
], [("**Arthur Conan Doyle**", "écrivain et médecin écossais"), ("**Ian Fleming**", "écrivain et ancien officier de renseignement"), ("**John le Carré**", "romancier, ancien agent du MI5 et du MI6")])
D = "pe"
culture(F, "Culture : Detectives and spies", 'Detectives <span>&amp; spies</span>',
  "Culture · Sherlock Holmes, Agatha Christie, James Bond", ("#d6d3d1", "#991b1b"),
  reperes("Le Royaume-Uni a donné au monde les plus célèbres détectives et le plus célèbre espion de la fiction.",
    [("1887", "première aventure de Sherlock Holmes"), ("1920", "premier roman d'Agatha Christie, avec Hercule Poirot"), ("1934", "Murder on the Orient Express"),
     ("1952", "The Mousetrap, toujours jouée à Londres"), ("1953", "Casino Royale, premier roman de James Bond"), ("1962", "premier film de James Bond")],
    "a detective, a clue, a suspect, a murder, a whodunit, a spy, a secret agent, a gadget"),
  {D: doc("Elementary!", [
    "Sherlock Holmes is a famous detective created by Arthur Conan Doyle in 1887. He lives at 221B Baker Street, in London, with his friend Dr Watson. He solves mysteries by observing small details.",
    "Agatha Christie is the best-selling novelist of all time. Her detective Hercule Poirot is a small Belgian man with a moustache. In her novels, the reader tries to find the murderer before the detective.",
    "Her play The Mousetrap has been performed in London since 1952. It is the longest-running play in the world.",
    "James Bond, also called 007, is a British secret agent created by Ian Fleming in 1953. He works for MI6. The Bond films, with their gadgets and fast cars, started in 1962.",
    "Britain has real secret services too: MI5 and MI6. During the Cold War, some British spies secretly worked for the Soviet Union."])},
  [TF(D, "Sherlock Holmes lives in London.", True, "« 221B Baker Street, in London »."),
   TF(D, "Holmes solves mysteries by observing small details.", True, "« by observing small details »."),
   TF(D, "Hercule Poirot is French.", False, "« a small Belgian man »."),
   TF(D, "The Mousetrap has been performed since 1952.", True, "« since 1952 »."),
   TF(D, "James Bond works for the FBI.", False, "« He works for MI6 »."),
   TF(D, "Britain has no real secret services.", False, "« Britain has real secret services too »." )],
  [Q(D, "Who created Sherlock Holmes?", ["Arthur Conan Doyle.", "Agatha Christie.", "Ian Fleming."]),
   Q(D, "What does the reader try to do in Agatha Christie's novels?", ["Find the murderer before the detective.", "Find a treasure.", "Become a spy."]),
   Q(D, "What is James Bond's number?", ["007.", "221B.", "MI5."]),
   Q(D, "What did some British spies do during the Cold War?", ["They worked for the Soviet Union.", "They wrote novels.", "They became actors."])],
  [DT(D, "Qui est l'ami et narrateur de Sherlock Holmes ?", ["Le docteur Watson", "Moriarty", "Poirot", "Q"]),
   DT(D, "Quelle détective est une vieille dame de village ?", ["Miss Marple", "Miss Moneypenny", "Mrs Hudson", "Miss Honey"]),
   DT(D, "Quel est le premier roman de James Bond ?", ["Casino Royale", "Dr. No", "Goldfinger", "Skyfall"]),
   DT(D, "Comment dit-on « un indice » ?", ["A clue", "A glue", "A sign-in", "A hint card"])],
  [W(D, "Trouve le mot qui veut dire « résout ».", "solves"), W(D, "Trouve le mot qui veut dire « le meurtrier ».", ["murderer", "the murderer"]),
   W(D, "Trouve le mot qui veut dire « la plus longue à l'affiche » (2 mots, avec un tiret).", ["longest-running"]), W(D, "Trouve le mot qui veut dire « secrètement ».", "secretly")])

# ═════════ SUPER-HÉROS ═════════
F = "cu_super_heros.html"
DZ(F, """
## Des héros nés d'une époque
Les super-héros américains ne sont pas seulement des personnages de divertissement : chacun est né à un moment précis de l'histoire des États-Unis et porte les espoirs et les peurs de son époque. Les lire, c'est lire l'histoire du pays.

## Superman (1938) : le rêve de l'immigrant
En 1938, en pleine Grande Dépression, le premier numéro d'*Action Comics* présente **Superman**. Ses créateurs, Jerry Siegel et Joe Shuster, sont deux jeunes de Cleveland, fils d'immigrants juifs d'Europe de l'Est. Leur héros est lui-même un immigrant : venu de la planète Krypton, élevé par un couple de fermiers du Kansas, il cache sa vraie identité sous celle du timide journaliste Clark Kent. Il défend d'abord les petites gens contre les patrons corrompus et les politiciens véreux, puis devient le symbole de « *truth, justice and the American way* ». En 1946, l'émission de radio *The Adventures of Superman* lui fait combattre le Ku Klux Klan : les scénaristes utilisent de vrais codes et rituels secrets du Klan, révélés par un militant infiltré, ce qui ridiculise l'organisation devant des millions d'auditeurs.

## Captain America (1941) : un héros pour entrer en guerre
En mars 1941, les États-Unis ne sont pas encore en guerre : beaucoup d'Américains refusent de se mêler du conflit européen. Deux jeunes dessinateurs juifs new-yorkais, **Joe Simon** et **Jack Kirby**, horrifiés par le nazisme, créent **Captain America**. Sur la couverture du premier numéro, le héros, vêtu du drapeau américain, frappe Hitler au visage… neuf mois avant Pearl Harbor. Les créateurs reçoivent des lettres de menaces de groupes pro-nazis. Steve Rogers est un jeune homme chétif, refusé par l'armée, transformé en super-soldat par un sérum expérimental : il incarne l'idée que le courage et les valeurs comptent plus que la force. Pendant la guerre, le personnage sert la **propagande** et soutient le moral des soldats.
Captain America évolue avec le pays. Dans les années 1970, après le scandale du **Watergate**, il découvre que le chef d'un complot criminel est un haut responsable du gouvernement ; écœuré, il abandonne son costume et devient un temps « Nomad », l'homme sans pays. Il incarne alors un patriotisme critique : fidèle aux idéaux de l'Amérique, pas forcément à ses dirigeants. En 1969 apparaît son partenaire **le Faucon** (Sam Wilson), l'un des premiers super-héros afro-américains, qui reprendra plus tard le bouclier de Captain America.

## La peur de la bombe et du savant fou : Hulk et les héros radioactifs
Après Hiroshima (1945), les Américains vivent dans la peur de la **bombe atomique** et de la guerre nucléaire avec l'URSS. Les comics des années 1960 transforment cette peur en récits.
- **Hulk** (1962) : le physicien **Bruce Banner**, un scientifique timide, est exposé aux rayons gamma lors de l'essai d'une bombe qu'il a lui-même conçue, en voulant sauver un adolescent égaré sur le site. Désormais, sous l'effet de la colère, il se transforme en un monstre vert incontrôlable. Hulk reprend deux grands mythes : *Dr Jekyll et Mr Hyde* (le double monstrueux qui sommeille en chacun) et *Frankenstein* (le savant dépassé par sa création). Il exprime la peur d'une **science** devenue trop puissante, capable de détruire l'humanité, et la méfiance envers l'armée qui le pourchasse.
- **Spider-Man** (1962) est mordu par une araignée radioactive ; les **Fantastic Four** (1961) sont transformés par des rayons cosmiques en pleine course à l'espace ; les **X-Men** (1963) sont des mutants, parfois présentés comme les « enfants de l'atome ».
- **Iron Man** (1963), Tony Stark, est un riche fabricant d'armes pris dans la guerre froide et la guerre du Vietnam. Plus tard, le personnage se remet en question sur son rôle de marchand d'armes.
Ces héros sont souvent des **monstres tragiques** : leurs pouvoirs viennent d'un accident scientifique et sont autant une malédiction qu'un don.

## Marvel et les héros « humains »
Chez **Marvel**, le scénariste **Stan Lee** et les dessinateurs Jack Kirby et Steve Ditko inventent des héros qui ont des problèmes de la vie réelle. Peter Parker, alias Spider-Man, est un adolescent qui doit gérer l'école, l'argent et sa tante, et qui apprend qu'un grand pouvoir implique de grandes responsabilités. Les **X-Men**, rejetés et craints par la société, sont lus comme une métaphore des minorités discriminées à l'époque du mouvement des droits civiques ; on compare souvent le pacifique Professeur Xavier et le radical Magneto à deux stratégies de la lutte contre l'oppression. En 1966 naît **Black Panther**, roi d'un pays africain imaginaire, le Wakanda, très avancé technologiquement : le premier super-héros noir des grands comics américains.

## Wonder Woman et la censure
**Wonder Woman** (1941), créée par le psychologue William Moulton Marston, qui a aussi travaillé sur l'un des premiers détecteurs de mensonges (d'où son lasso de vérité), est l'une des premières grandes héroïnes : une guerrière indépendante, pensée comme un modèle pour les filles. En 1954, après un livre accusant les bandes dessinées de rendre les jeunes violents, les éditeurs adoptent le **Comics Code**, une autocensure qui impose des histoires très sages pendant des années.

## Des héros pour réfléchir
Dans les années 1980, le scénariste britannique **Alan Moore** publie *Watchmen* (1986-1987), qui imagine des super-héros vieillissants dans un monde au bord de la guerre nucléaire et pose une question célèbre : qui surveille les surveillants ? Après le 11 septembre 2001, les films de super-héros parlent de terrorisme, de surveillance et de sécurité, comme *Captain America: Civil War* (2016), où les héros se divisent sur la question de savoir s'ils doivent être contrôlés par les gouvernements. En 2014, **Kamala Khan**, une adolescente américaine d'origine pakistanaise et musulmane, devient Ms. Marvel. Depuis *Iron Man* (2008), le **Marvel Cinematic Universe** domine le box-office mondial, même si certains critiques parlent aujourd'hui de lassitude.
Les super-héros forment ainsi une **mythologie moderne** : comme les héros antiques, ils incarnent des valeurs (courage, justice, responsabilité) et des peurs (guerre, bombe, science, surveillance, rejet de l'autre).
""", """
a hero = un héros
a superpower = un superpouvoir
a villain = un méchant
a shield = un bouclier
anger = la colère
a bomb = une bombe
a scientist = un scientifique
a comic = une bande dessinée
""", [
 ("Pourquoi Superman ressemble-t-il à un immigrant ?", ["Il vient d'une autre planète et a été élevé par des fermiers américains", "Il parle une autre langue", "Il vit en Europe"], "Ses créateurs étaient fils d'immigrants."),
 ("Que fait Superman à la radio en 1946 ?", ["Il combat le Ku Klux Klan et ridiculise ses rituels secrets", "Il chante", "Il fait de la publicité"], ""),
 ("Pourquoi Captain America frappe-t-il Hitler dès mars 1941 ?", ["Ses créateurs veulent pousser l'Amérique à combattre le nazisme", "Pour vendre des drapeaux", "Parce que la guerre est finie"], "Neuf mois avant Pearl Harbor."),
 ("Que fait Captain America après le Watergate ?", ["Il abandonne son costume, dégoûté par la corruption", "Il devient président", "Il part sur la Lune"], ""),
 ("Comment Bruce Banner devient-il Hulk ?", ["Il est exposé aux rayons gamma lors de l'essai d'une bombe", "Il est mordu par une araignée", "Il boit une potion magique"], ""),
 ("Quelle peur exprime Hulk ?", ["La peur d'une science trop puissante et de la bombe", "La peur des araignées", "La peur de l'école"], ""),
 ("Que représentent souvent les X-Men ?", ["Les minorités discriminées", "Les soldats", "Les riches"], ""),
 ("Quelle question pose Watchmen ?", ["Qui surveille les surveillants ?", "Qui est le plus fort ?", "Qui a inventé les comics ?"], ""),
], [("Krypton", "planète d'origine imaginaire de Superman"), ("**Jack Kirby**", "dessinateur, co-créateur de Captain America, Hulk et des X-Men"),
    ("**Stan Lee**", "scénariste et éditeur de Marvel, 1922-2018"), ("Hiroshima", "ville japonaise détruite par une bombe atomique américaine en 1945"),
    ("*Dr Jekyll et Mr Hyde*", "roman de Stevenson sur un homme à double personnalité"), ("**Alan Moore**", "scénariste britannique de bandes dessinées")])
D = "sh"
culture(F, "Culture : Superheroes", 'Super<span>heroes</span>',
  "Culture · de Superman à Hulk : ce que les héros racontent de l'Amérique", ("#fca5a5", "#1d4ed8"),
  reperes("Les super-héros sont nés dans les comics américains en 1938. Chacun reflète les valeurs et les peurs de son époque : la crise, la guerre, la bombe, la science, les droits civiques.",
    [("1938", "Superman, pendant la Grande Dépression"), ("mars 1941", "Captain America frappe Hitler, avant l'entrée en guerre"), ("1954", "le Comics Code"),
     ("1962", "Hulk et Spider-Man : la peur de l'atome"), ("1966", "Black Panther"), ("1974", "Captain America abandonne son costume après le Watergate"),
     ("1986", "Watchmen"), ("2008", "Iron Man lance le Marvel Cinematic Universe")],
    "a superhero, a superpower, a villain, a secret identity, propaganda, radiation, a mad scientist, responsibility"),
  {D: doc("Heroes of their time", [
    "Superheroes were born in American comic books. Superman appeared in 1938, during the Great Depression. He came from another planet and grew up on a farm in Kansas. His creators were two sons of Jewish immigrants.",
    "In March 1941, before the USA entered the Second World War, Joe Simon and Jack Kirby created Captain America. On the cover of the first comic, he punched Hitler in the face. The creators wanted Americans to fight against the Nazis.",
    "After the war, Americans were afraid of the atomic bomb. In 1962, Marvel created the Hulk: a scientist, Bruce Banner, is hit by gamma rays during a bomb test. When he is angry, he becomes a huge green monster. The Hulk shows the fear of science that becomes too dangerous.",
    "Other heroes also got their powers from radiation, like Spider-Man. The X-Men are mutants who are rejected by society, like minorities during the civil rights movement. In 1966, Black Panther became the first Black superhero in mainstream comics.",
    "Captain America changed with his country: after the Watergate scandal, he stopped being Captain America for a while because he was disgusted by the government. Superheroes are a modern mythology: they show the values and the fears of each period."])},
  [TF(D, "Superman appeared during the Great Depression.", True, "« in 1938, during the Great Depression »."),
   TF(D, "Captain America was created after the war.", False, "« In March 1941, before the USA entered the Second World War »."),
   TF(D, "Captain America punched Hitler on the first cover.", True, "« he punched Hitler in the face »."),
   TF(D, "Bruce Banner becomes the Hulk when he is happy.", False, "« When he is angry »."),
   TF(D, "The Hulk shows the fear of dangerous science.", True, "« the fear of science that becomes too dangerous »."),
   TF(D, "Captain America always agreed with the government.", False, "« disgusted by the government »." )],
  [Q(D, "Why did Simon and Kirby create Captain America?", ["They wanted Americans to fight the Nazis.", "They wanted to sell flags.", "They wanted to make a funny comic."]),
   Q(D, "What happens to Bruce Banner?", ["He is hit by gamma rays during a bomb test.", "He is bitten by a spider.", "He comes from another planet."]),
   Q(D, "What were Americans afraid of after the war?", ["The atomic bomb.", "Spiders.", "Football."]),
   Q(D, "Who are the X-Men like?", ["Minorities during the civil rights movement.", "Kings and queens.", "Rich businessmen."]),
   Q(D, "Why did Captain America stop for a while?", ["He was disgusted by the government after Watergate.", "He was tired.", "He moved to Europe."])],
  [DT(D, "Qui a créé Captain America ?", ["Joe Simon et Jack Kirby", "Stan Lee seul", "Siegel et Shuster", "Alan Moore"]),
   DT(D, "Quel est le vrai nom de Hulk ?", ["Bruce Banner", "Peter Parker", "Tony Stark", "Steve Rogers"]),
   DT(D, "Quel roman sur un double monstrueux a inspiré Hulk ?", ["Dr Jekyll et Mr Hyde", "Dracula", "Moby Dick", "Peter Pan"]),
   DT(D, "Comment s'appelle le pays de Black Panther ?", ["Le Wakanda", "Krypton", "Gotham", "Asgard"])],
  [W(D, "Trouve le mot qui veut dire « a frappé » (d'un coup de poing).", "punched"), W(D, "Trouve le mot qui veut dire « en colère ».", "angry"),
   W(D, "Trouve le mot qui veut dire « rejetés ».", "rejected"), W(D, "Trouve le mot qui veut dire « dégoûté ».", "disgusted")])

# ═════════ PEUPLES AUTOCHTONES ═════════
F = "cu_peuples_autochtones.html"
DZ(F, """
## Les Aborigènes d'Australie
Les **Aboriginal and Torres Strait Islander peoples** vivent en Australie depuis plus de 50 000 ans : ce sont parmi les plus anciennes cultures vivantes du monde. Avant l'arrivée des Européens, ils formaient des centaines de peuples, parlant plus de 250 langues, avec un lien spirituel profond à la terre, exprimé dans le **Dreaming** (le « Temps du rêve »), ensemble de récits sur la création du monde.
En **1788**, la First Fleet britannique arrive à Sydney. Les colons considèrent le continent comme une **terra nullius**, une « terre n'appartenant à personne », et s'emparent des terres. Les maladies, les violences et la dépossession font s'effondrer la population aborigène.

## Les « Stolen Generations »
Des années 1910 aux années 1970 environ, les autorités australiennes retirent de force des dizaines de milliers d'enfants aborigènes à leurs familles pour les placer dans des institutions ou des familles blanches, afin de les « assimiler ». On appelle ces enfants les **Stolen Generations**. Le **13 février 2008**, le Premier ministre Kevin Rudd présente au Parlement des excuses officielles (« *Sorry* ») au nom de la nation. En 1992, la décision **Mabo** de la Haute Cour avait déjà reconnu que la théorie de la terra nullius était fausse et que des droits fonciers autochtones existaient. En 2023, un référendum proposant de créer un organe consultatif aborigène au Parlement (**the Voice**) a été rejeté par environ 60 % des électeurs. Depuis 2019, il est interdit de grimper sur **Uluru**, rocher sacré pour le peuple Anangu.

## Les peuples autochtones du Canada
Au Canada, on distingue trois groupes : les **First Nations** (Premières Nations), les **Inuit** du Grand Nord et les **Métis**, issus de mélanges entre Autochtones et Européens. Ils représentent environ 5 % de la population.
De la fin du 19e siècle jusqu'en 1996, date de fermeture du dernier établissement, environ 150 000 enfants autochtones ont été envoyés dans des **residential schools**, des pensionnats souvent tenus par des Églises, où il leur était interdit de parler leur langue et où beaucoup ont subi des mauvais traitements. Des milliers d'enfants y sont morts. En 2015, une **Commission de vérité et réconciliation** a qualifié ce système de « génocide culturel ». En 2021, des recherches menées par radar autour d'anciens pensionnats ont signalé de possibles tombes anonymes, ce qui a bouleversé le pays. Le pape François a présenté des excuses en 2022. Depuis 2021, le **30 septembre** est la Journée nationale de la vérité et de la réconciliation, et l'on porte ce jour-là un t-shirt orange (**Orange Shirt Day**).
En 1999, le territoire du **Nunavut**, à majorité inuit, a été créé dans le Grand Nord.

## Aujourd'hui
Dans les deux pays, les populations autochtones restent confrontées à de fortes inégalités (santé, espérance de vie, emploi, incarcération), mais elles revendiquent leurs droits, font revivre leurs langues et leurs cultures, et leurs artistes sont de plus en plus reconnus. Beaucoup d'événements commencent désormais par une reconnaissance des terres (**Acknowledgement of Country** en Australie, **land acknowledgement** au Canada).
[→ Voir aussi : l'Australie](cu_australie.html)
[→ Voir aussi : le Canada](cu_canada.html)
""", """
a people = un peuple
land = la terre
a child = un enfant
a family = une famille
a language = une langue
an apology = des excuses
a school = une école
a right = un droit
""", [
 ("Depuis combien de temps les Aborigènes vivent-ils en Australie ?", ["Plus de 50 000 ans", "200 ans", "1 000 ans"], ""),
 ("Que signifie « terra nullius » ?", ["Une terre n'appartenant à personne", "Une terre sacrée", "Une terre fertile"], ""),
 ("Qui sont les Stolen Generations ?", ["Des enfants aborigènes retirés de force à leurs familles", "Des voleurs", "Des colons"], ""),
 ("Que se passe-t-il le 13 février 2008 ?", ["Le Premier ministre australien présente des excuses officielles", "Un référendum", "L'arrivée de la First Fleet"], ""),
 ("Que subissaient les enfants dans les residential schools ?", ["L'interdiction de parler leur langue et souvent des mauvais traitements", "Des vacances", "Des cours de leur langue"], ""),
 ("Que porte-t-on le 30 septembre au Canada ?", ["Un t-shirt orange", "Un costume", "Un chapeau vert"], ""),
], [("First Fleet", "premiers navires de colons et de forçats britanniques"), ("Kevin Rudd", "Premier ministre australien en 2007-2010 et 2013"), ("**Uluru**", "immense rocher rouge du centre de l'Australie"),
    ("pape François", "chef de l'Église catholique de 2013 à 2025")])
D = "pa"
culture(F, "Culture : Indigenous peoples of Australia and Canada", 'Indigenous <span>peoples</span>',
  "Culture · Aborigènes, Stolen Generations, First Nations et pensionnats", ("#fdba74", "#7c2d12"),
  reperes("En Australie et au Canada, les peuples autochtones ont subi la colonisation et des politiques d'assimilation forcée. Les deux pays ont présenté des excuses.",
    [("plus de 50 000 ans", "présence aborigène en Australie"), ("1788", "arrivée des colons britanniques en Australie"), ("1910 – 1970 environ", "les Stolen Generations"),
     ("1996", "fermeture du dernier pensionnat autochtone au Canada"), ("2008", "excuses officielles du gouvernement australien"), ("30 septembre", "journée de la vérité et de la réconciliation au Canada")],
    "Indigenous, Aboriginal, First Nations, Inuit, assimilation, a residential school, an apology, reconciliation"),
  {D: doc("Saying sorry", [
    "Aboriginal people have lived in Australia for more than 50,000 years. When British colonists arrived in 1788, they took their land.",
    "For many years, the Australian government took Aboriginal children away from their families to make them live like white Australians. These children are called the Stolen Generations. In 2008, the Prime Minister said \"Sorry\" in Parliament.",
    "In Canada, the Indigenous peoples are the First Nations, the Inuit and the Métis. For more than a hundred years, about 150,000 Indigenous children were sent to residential schools, far from their families.",
    "In these schools, they could not speak their own language, and many were badly treated. Thousands of children died. Today, Canada remembers them every 30 September, when people wear orange shirts.",
    "Indigenous peoples still face inequalities, but they are fighting for their rights and their languages and cultures are coming back to life."])},
  [TF(D, "Aboriginal people have lived in Australia for more than 50,000 years.", True, "« more than 50,000 years »."),
   TF(D, "The Stolen Generations were children taken from their families.", True, "« took Aboriginal children away from their families »."),
   TF(D, "The Australian Prime Minister refused to say sorry.", False, "« the Prime Minister said \"Sorry\" »."),
   TF(D, "In residential schools, children could speak their own language.", False, "« they could not speak their own language »."),
   TF(D, "Canadians wear orange shirts on 30 September.", True, "« people wear orange shirts »."),
   TF(D, "Indigenous languages are disappearing completely.", False, "« coming back to life »." )],
  [Q(D, "What did British colonists do in 1788?", ["They took Aboriginal land.", "They learned Aboriginal languages.", "They left Australia."]),
   Q(D, "What happened in 2008?", ["The Australian Prime Minister said \"Sorry\".", "A new colony was created.", "The schools opened."]),
   Q(D, "Who are the Indigenous peoples of Canada?", ["The First Nations, the Inuit and the Métis.", "The French and the British.", "The Aboriginal people."]),
   Q(D, "What are Indigenous peoples fighting for today?", ["Their rights, languages and cultures.", "More schools far from home.", "Nothing."])],
  [DT(D, "Comment s'appellent les récits aborigènes de la création ?", ["Le Dreaming (Temps du rêve)", "Le Big Bang", "La Genèse", "Le Mabo"]),
   DT(D, "Quel rocher sacré est interdit d'escalade depuis 2019 ?", ["Uluru", "Ayers Mountain", "Le Denali", "Le Ben Nevis"]),
   DT(D, "Quel territoire inuit est créé en 1999 ?", ["Le Nunavut", "Le Yukon", "L'Alaska", "Le Québec"]),
   DT(D, "Comment dit-on « des excuses » ?", ["An apology", "An excuse me", "A sorrow", "A pardon card"])],
  [W(D, "Trouve le mot qui veut dire « leur terre » (2 mots).", ["their land"]), W(D, "Trouve le mot qui veut dire « loin de » (2 mots).", ["far from"]),
   W(D, "Trouve le mot qui veut dire « maltraités » (2 mots).", ["badly treated"]), W(D, "Trouve le mot qui veut dire « leurs droits » (2 mots).", ["their rights"])])

# ═════════ FAMILLE ROYALE ═════════
F = "cu_famille_royale.html"
DZ(F, """
## La fin d'un règne historique
La reine **Elizabeth II** est montée sur le trône en 1952, à 25 ans, et a régné plus de 70 ans : un record dans l'histoire britannique. À sa mort, le **8 septembre 2022**, son fils aîné devient roi sous le nom de **Charles III**, à 73 ans. Il est couronné le 6 mai 2023 à l'abbaye de Westminster, avec son épouse, la reine **Camilla**. Charles est connu depuis longtemps pour son engagement en faveur de l'environnement et de l'agriculture biologique.

## Diana, la « princesse du peuple »
En 1981, le prince Charles épouse **Lady Diana Spencer**, 20 ans. Le mariage est regardé par des centaines de millions de téléspectateurs dans le monde. Diana devient l'une des femmes les plus photographiées de la planète. Elle se distingue par sa proximité avec les gens : en 1987, elle serre sans gants la main d'un malade du sida, à une époque où beaucoup croyaient, à tort, que la maladie s'attrapait par simple contact ; elle fait aussi campagne contre les mines antipersonnel. Mais le couple est malheureux et divorce en 1996. Le **31 août 1997**, Diana meurt dans un accident de voiture à Paris, sous le pont de l'Alma, alors que sa voiture est poursuivie par des photographes (**paparazzi**). Le Premier ministre Tony Blair la surnomme « *the People's Princess* ». Des montagnes de fleurs s'accumulent devant les palais, et ses funérailles sont suivies dans le monde entier.

## William et Harry
Diana a eu deux fils.
- **William**, l'aîné, est l'héritier du trône. Il porte le titre de **Prince of Wales**. Avec son épouse **Catherine** (Kate Middleton), rencontrée à l'université, il a trois enfants : George, Charlotte et Louis. George est donc le deuxième dans l'ordre de succession.
- **Harry**, le cadet, a épousé en 2018 l'actrice américaine **Meghan Markle**. En 2020, le couple annonce qu'il se retire de ses fonctions royales et part vivre en Californie. Leurs critiques envers la famille royale, dans une interview télévisée en 2021 puis dans les mémoires de Harry, *Spare* (2023), ont provoqué une crise familiale très médiatisée.
En 2024, le roi Charles et la princesse Catherine ont tous deux annoncé être soignés pour un cancer. Le prince Andrew, frère du roi, a perdu ses titres royaux en 2025 à la suite d'un scandale lié à ses fréquentations.

## La monarchie a-t-elle un avenir ?
La famille royale reste très populaire auprès d'une majorité de Britanniques, en particulier les plus âgés : elle incarne la continuité, attire les touristes et représente le pays à l'étranger. Mais les jeunes sont beaucoup plus partagés. Des groupes **républicains**, comme *Republic*, réclament un chef d'État élu et critiquent le coût de la monarchie, financée en partie par l'argent public. Dans plusieurs pays du Commonwealth, comme la Barbade en 2021, le débat a conduit à abandonner le roi comme chef d'État.
[→ Voir aussi : la monarchie britannique](cu_monarchie.html)
""", """
a king = un roi
a queen = une reine
a prince = un prince
a princess = une princesse
a wedding = un mariage
a crown = une couronne
a palace = un palais
a son = un fils
""", [
 ("Combien de temps a régné Elizabeth II ?", ["Plus de 70 ans", "10 ans", "100 ans"], ""),
 ("Pourquoi Diana était-elle surnommée « la princesse du peuple » ?", ["Pour sa proximité avec les gens", "Parce qu'elle n'était pas mariée", "Parce qu'elle était reine"], ""),
 ("Que s'est-il passé le 31 août 1997 ?", ["Diana meurt dans un accident de voiture à Paris", "Charles devient roi", "William se marie"], ""),
 ("Qui est l'héritier du trône ?", ["Le prince William", "Le prince Harry", "La princesse Charlotte"], ""),
 ("Qu'ont décidé Harry et Meghan en 2020 ?", ["Se retirer de leurs fonctions royales et partir en Californie", "Devenir roi et reine", "Divorcer"], ""),
 ("Que réclament les républicains ?", ["Un chef d'État élu", "Plus de princes", "Un roi plus jeune"], ""),
], [("Westminster", "abbaye de Londres où sont couronnés les rois"), ("Tony Blair", "Premier ministre de 1997 à 2007")])
D = "fr"
culture(F, "Culture : The Royal Family today", 'The Royal <span>Family</span>',
  "Culture · de Diana à Charles III, William et Harry", ("#fde68a", "#6d28d9"),
  reperes("Depuis la mort d'Elizabeth II en 2022, Charles III est roi. La famille royale fascine toujours, mais l'avenir de la monarchie fait débat.",
    [("1952 – 2022", "règne d'Elizabeth II, plus de 70 ans"), ("1981", "mariage de Charles et Diana"), ("31 août 1997", "mort de Diana à Paris"),
     ("2020", "Harry et Meghan quittent leurs fonctions royales"), ("2022", "Charles III devient roi"), ("6 mai 2023", "couronnement de Charles III")],
    "a king, a queen, an heir, the throne, a coronation, a wedding, the paparazzi, a republican"),
  {D: doc("The Windsors", [
    "Queen Elizabeth II reigned for more than 70 years. When she died in 2022, her son became King Charles III.",
    "In 1981, Charles married Diana. She was very popular because she was close to ordinary people. They divorced in 1996, and Diana died in a car crash in Paris in 1997.",
    "Diana had two sons, William and Harry. Prince William is the heir to the throne. He and his wife Catherine have three children: George, Charlotte and Louis.",
    "Prince Harry married an American actress, Meghan Markle. In 2020, they decided to leave their royal duties and moved to California.",
    "Many British people love the Royal Family, but some young people think the country should have an elected head of state."])},
  [TF(D, "Elizabeth II reigned for more than 70 years.", True, "« more than 70 years »."),
   TF(D, "Diana was not popular.", False, "« She was very popular »."),
   TF(D, "Diana died in Paris in 1997.", True, "« in Paris in 1997 »."),
   TF(D, "Prince Harry is the heir to the throne.", False, "« Prince William is the heir »."),
   TF(D, "William and Catherine have three children.", True, "« three children »."),
   TF(D, "Harry and Meghan moved to Australia.", False, "« moved to California »." )],
  [Q(D, "Who became king in 2022?", ["Charles III.", "William.", "Harry."]),
   Q(D, "Why was Diana popular?", ["She was close to ordinary people.", "She was very rich.", "She was a singer."]),
   Q(D, "What did Harry and Meghan do in 2020?", ["They left their royal duties.", "They became king and queen.", "They moved to London."]),
   Q(D, "What do some young British people think?", ["The country should have an elected head of state.", "There should be two kings.", "The Queen should come back."])],
  [DT(D, "Quel titre porte le prince William ?", ["Prince of Wales", "Duke of York", "King of Scotland", "Prince of London"]),
   DT(D, "Où Charles III est-il couronné ?", ["À l'abbaye de Westminster", "À Buckingham Palace", "À Windsor", "À la cathédrale Saint-Paul"]),
   DT(D, "Comment s'appellent les mémoires du prince Harry ?", ["Spare", "Heir", "Crown", "Diana"]),
   DT(D, "Comment dit-on « l'héritier » ?", ["The heir", "The hair", "The air", "The son king"])],
  [W(D, "Trouve le mot qui veut dire « a régné ».", "reigned"), W(D, "Trouve le mot qui veut dire « ont divorcé ».", "divorced"),
   W(D, "Trouve le mot qui veut dire « fonctions » (royales).", "duties"), W(D, "Trouve le mot qui veut dire « élu ».", "elected")])
END()
