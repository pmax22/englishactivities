import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
exec(open(_EA_OUT+"/cuhelp.py", encoding="utf-8").read())

# ═════════ TITANIC ═════════
F = "cu_titanic.html"
DZ(F, """
## Le plus grand navire du monde
Le **RMS Titanic** est construit à **Belfast**, en Irlande du Nord, par les chantiers Harland & Wolff, pour la compagnie britannique White Star Line. Long de 269 mètres, c'est alors le plus grand navire jamais construit, avec un luxe inédit en première classe : piscine, salle de gym, bains turcs, grand escalier. On le dit « pratiquement insubmersible » (**practically unsinkable**) grâce à ses compartiments étanches.

## Le voyage inaugural
Le **10 avril 1912**, le Titanic quitte **Southampton**, fait escale à Cherbourg puis à Queenstown (aujourd'hui Cobh, en Irlande), et part vers **New York** avec environ 2 200 personnes à bord. On y trouve des millionnaires américains, des familles de la classe moyenne, et surtout des centaines d'émigrants en troisième classe, venus d'Irlande, de Scandinavie, du Moyen-Orient, qui partent commencer une nouvelle vie en Amérique.

## La nuit du naufrage
Le 14 avril, vers 23 h 40, en plein Atlantique Nord, le navire heurte un **iceberg**, malgré plusieurs messages d'alerte reçus dans la journée. Cinq compartiments sont ouverts : le navire est condamné. On fait monter d'abord les femmes et les enfants (**women and children first**), mais il n'y a des canots de sauvetage (**lifeboats**) que pour environ la moitié des passagers, car la loi de l'époque n'en exigeait pas plus. Certains canots partent à moitié vides. Les musiciens de l'orchestre continuent de jouer pour calmer les passagers. Le Titanic se brise en deux et coule vers 2 h 20, le **15 avril 1912**. Plus de 1 500 personnes meurent dans l'eau glaciale. Le paquebot **Carpathia** arrive au matin et recueille environ 700 survivants.

## Un naufrage révélateur des classes sociales
Le naufrage montre de façon brutale les inégalités de la société de l'époque : environ 60 % des passagers de première classe ont survécu, contre environ un quart de ceux de troisième classe, logés dans les ponts inférieurs, loin des canots. Les membres d'équipage ont aussi payé un très lourd tribut.

## Les conséquences
Après la catastrophe, une convention internationale sur la sécurité en mer (**SOLAS**, 1914) impose assez de canots pour tous, des exercices d'évacuation et une veille radio permanente ; une patrouille internationale surveille désormais les icebergs.
L'épave est retrouvée en **1985** par l'océanographe américain Robert Ballard, à près de 4 000 mètres de profondeur. Le film *Titanic* de James Cameron (1997) a rendu l'histoire célèbre dans le monde entier. Depuis 2012, un grand musée, **Titanic Belfast**, se trouve à l'endroit même où le navire a été construit.
""", """
a ship = un navire
an iceberg = un iceberg
a lifeboat = un canot de sauvetage
a passenger = un passager
the crew = l'équipage
to sink = couler
a survivor = un survivant
the sea = la mer
""", [
 ("Où le Titanic a-t-il été construit ?", ["À Belfast", "À New York", "À Paris"], ""),
 ("Pourquoi le disait-on « unsinkable » ?", ["Grâce à ses compartiments étanches", "Parce qu'il était en bois", "Parce qu'il était petit"], ""),
 ("Qui voyageait en troisième classe ?", ["Surtout des émigrants partant vivre en Amérique", "Des millionnaires", "Le capitaine"], ""),
 ("Pourquoi tant de victimes ?", ["Il n'y avait des canots que pour la moitié des passagers environ", "Le navire était en feu", "Il y avait trop de canots"], ""),
 ("Que montre la différence de survie entre les classes ?", ["Les inégalités sociales de l'époque", "Que la troisième classe nageait mieux", "Rien de particulier"], ""),
 ("Qu'impose la convention SOLAS de 1914 ?", ["Assez de canots pour tous et une veille radio permanente", "L'interdiction des paquebots", "Des billets moins chers"], ""),
], [("White Star Line", "compagnie maritime britannique"), ("Robert Ballard", "océanographe américain"), ("James Cameron", "réalisateur canadien")])
D = "ti"
culture(F, "Culture : The Titanic", 'The <span>Titanic</span>',
  "Culture · le naufrage de 1912", ("#bae6fd", "#1e3a8a"),
  reperes("Le Titanic, paquebot britannique réputé insubmersible, a coulé lors de son premier voyage en avril 1912. Plus de 1 500 personnes sont mortes.",
    [("1909 – 1912", "construction à Belfast"), ("10 avril 1912", "départ de Southampton"), ("14 – 15 avril 1912", "collision avec un iceberg et naufrage"),
     ("1914", "convention SOLAS sur la sécurité en mer"), ("1985", "découverte de l'épave"), ("1997", "le film de James Cameron")],
    "a ship, a liner, an iceberg, a lifeboat, the crew, a survivor, to sink, unsinkable"),
  {D: doc("A night to remember", [
    "The Titanic was a British ship built in Belfast. In 1912, it was the biggest ship in the world. People said it was \"unsinkable\".",
    "On 10 April 1912, it left Southampton for New York with about 2,200 people on board: rich passengers in first class, and many poor emigrants in third class.",
    "On the night of 14 April, the Titanic hit an iceberg in the North Atlantic. There were not enough lifeboats for everybody. The rule was \"women and children first\".",
    "The ship sank in less than three hours. More than 1,500 people died in the freezing water. Most first-class passengers survived, but only about a quarter of third-class passengers did.",
    "After the disaster, new laws made ships safer: enough lifeboats for everybody and a radio all night. The wreck was found in 1985."])},
  [TF(D, "The Titanic was built in Belfast.", True, "« built in Belfast »."),
   TF(D, "The Titanic was going to New York.", True, "« for New York »."),
   TF(D, "There were enough lifeboats for everybody.", False, "« not enough lifeboats »."),
   TF(D, "The ship sank in more than ten hours.", False, "« in less than three hours »."),
   TF(D, "Third-class passengers had the same chances as first-class passengers.", False, "Environ un quart seulement ont survécu."),
   TF(D, "The wreck was found in 1985.", True, "« found in 1985 »." )],
  [Q(D, "What did people say about the Titanic?", ["It was unsinkable.", "It was very slow.", "It was dangerous."]),
   Q(D, "What did the Titanic hit?", ["An iceberg.", "Another ship.", "A rock near New York."]),
   Q(D, "What was the rule for the lifeboats?", ["Women and children first.", "First class only.", "The crew first."]),
   Q(D, "What changed after the disaster?", ["Ships became safer.", "Ships became bigger.", "Nothing changed."])],
  [DT(D, "De quel port part le Titanic ?", ["Southampton", "Liverpool", "Belfast", "Londres"]),
   DT(D, "Quel navire recueille les survivants ?", ["Le Carpathia", "L'Olympic", "Le Lusitania", "Le Mayflower"]),
   DT(D, "Comment dit-on « couler » ?", ["To sink", "To swim", "To sail", "To drown a ship"]),
   DT(D, "Combien de personnes environ meurent dans le naufrage ?", ["Plus de 1 500", "Environ 150", "Environ 15 000", "Aucune"])],
  [W(D, "Trouve le mot qui veut dire « insubmersible ».", "unsinkable"), W(D, "Trouve le mot qui veut dire « à bord » (2 mots).", ["on board"]),
   W(D, "Trouve le mot qui veut dire « glaciale ».", "freezing"), W(D, "Trouve le mot qui veut dire « l'épave ».", ["wreck", "the wreck"])])

# ═════════ WINDRUSH ═════════
F = "cu_windrush.html"
DZ(F, """
## L'arrivée de l'Empire Windrush
Le **22 juin 1948**, le navire **HMT Empire Windrush** accoste à Tilbury, près de Londres. À son bord, environ un millier de passagers, en majorité venus des Caraïbes, surtout de la **Jamaïque** et de Trinidad. Beaucoup avaient servi dans l'armée britannique pendant la guerre. Ils répondent à l'appel d'un Royaume-Uni qui manque de main-d'œuvre pour se reconstruire. La même année, une loi (**British Nationality Act 1948**) reconnaît aux habitants de l'Empire et du Commonwealth le statut de citoyens britanniques. Ce bateau donne son nom à toute une génération : la **Windrush generation**, les Caribéens arrivés au Royaume-Uni entre 1948 et 1971.

## Reconstruire le pays
Ces immigrés travaillent dans les hôpitaux du tout nouveau **NHS**, comme infirmières, dans les transports londoniens (chauffeurs et contrôleurs de bus), à la poste, dans les usines. Ils ont contribué directement à la reconstruction du pays.

## Le racisme
L'accueil est souvent dur. Il est difficile de trouver un logement : certaines annonces affichent ouvertement des refus du type « *No Irish, no Blacks, no dogs* ». En 1958, des émeutes racistes éclatent à **Notting Hill**, à Londres. En réponse, la militante Claudia Jones organise en 1959 un carnaval caribéen, ancêtre du **Notting Hill Carnival**, aujourd'hui l'un des plus grands festivals de rue d'Europe. Dans les années 1960, le discours anti-immigration se durcit, et des lois limitent progressivement l'immigration venue du Commonwealth, jusqu'à l'**Immigration Act** de 1971.

## Le scandale Windrush (2018)
En 2018, la presse révèle que des membres de la génération Windrush, arrivés légalement enfants avec le passeport de leurs parents, sont traités comme des immigrés illégaux parce qu'ils n'ont jamais eu de papiers prouvant leur statut. Dans le cadre d'une politique dite de l'« environnement hostile » (**hostile environment**), certains perdent leur emploi, leur logement, l'accès aux soins ; certains sont détenus ou même expulsés vers des pays qu'ils avaient quittés enfants. Le scandale provoque la démission de la ministre de l'Intérieur, Amber Rudd, des excuses officielles et la création d'un programme d'indemnisation, jugé lent par les victimes.

## Une mémoire reconnue
Depuis 2018, le **22 juin** est le **Windrush Day**, journée qui célèbre la contribution des Caribéens britanniques. Des artistes, des écrivains et des sportifs issus de cette génération et de leurs descendants ont profondément marqué la culture britannique.
[→ Voir aussi : la Grande-Bretagne multiculturelle](cu_multiculturel.html)
""", """
a ship = un navire
a worker = un travailleur
a nurse = une infirmière
a bus driver = un chauffeur de bus
a citizen = un citoyen
a passport = un passeport
racism = le racisme
a carnival = un carnaval
""", [
 ("D'où venaient la plupart des passagers du Windrush ?", ["Des Caraïbes, surtout de la Jamaïque", "D'Inde", "Des États-Unis"], ""),
 ("Pourquoi le Royaume-Uni avait-il besoin de travailleurs ?", ["Pour se reconstruire après la guerre", "Pour faire la guerre", "Pour construire le Titanic"], ""),
 ("Où travaillaient beaucoup de ces immigrés ?", ["Dans les hôpitaux du NHS et les transports", "Dans les mines d'or", "Dans l'armée américaine"], ""),
 ("Comment est né le Notting Hill Carnival ?", ["En réponse aux émeutes racistes de 1958", "Pour fêter la reine", "Pour un match de football"], ""),
 ("Qu'a révélé le scandale de 2018 ?", ["Des personnes arrivées légalement ont été traitées comme des immigrés illégaux", "Un vol de passeports", "Un naufrage"], ""),
 ("Que célèbre-t-on le 22 juin ?", ["Le Windrush Day", "La fête nationale", "Noël"], ""),
], [("Tilbury", "port sur la Tamise"), ("Claudia Jones", "journaliste et militante née à Trinidad"), ("Amber Rudd", "ministre de l'Intérieur de 2016 à 2018")])
D = "wd"
culture(F, "Culture : The Windrush generation", 'The Windrush <span>generation</span>',
  "Culture · les Caribéens qui ont reconstruit la Grande-Bretagne", ("#fde68a", "#15803d"),
  reperes("La « génération Windrush » désigne les Caribéens venus travailler au Royaume-Uni après 1948. En 2018, un scandale a révélé l'injustice faite à certains d'entre eux.",
    [("22 juin 1948", "arrivée de l'Empire Windrush"), ("1958", "émeutes racistes de Notting Hill"), ("1959", "premier carnaval caribéen, ancêtre du Notting Hill Carnival"),
     ("1971", "Immigration Act"), ("2018", "le scandale Windrush"), ("22 juin", "Windrush Day, depuis 2018")],
    "a ship, an immigrant, the Commonwealth, a citizen, the NHS, racism, a scandal, to deport"),
  {D: doc("Arrival at Tilbury", [
    "On 22 June 1948, a ship called the Empire Windrush arrived near London. On board, there were hundreds of people from the Caribbean, especially from Jamaica.",
    "Britain needed workers to rebuild the country after the war. Many of these immigrants worked as nurses in the new NHS or as bus drivers in London.",
    "Life was not easy. Many faced racism, and it was hard to find a flat. In 1958, there were racist riots in Notting Hill. The next year, a Caribbean carnival was organised: it became the famous Notting Hill Carnival.",
    "In 2018, a scandal shocked the country. Some people who had arrived legally as children were treated as illegal immigrants because they had no documents. Some lost their jobs, and some were sent away.",
    "The government apologised. Today, every 22 June is Windrush Day, to celebrate the Caribbean community in Britain."])},
  [TF(D, "The Empire Windrush arrived in 1948.", True, "« On 22 June 1948 »."),
   TF(D, "Most passengers came from India.", False, "Des Caraïbes, surtout de la Jamaïque."),
   TF(D, "Many immigrants worked in the NHS.", True, "« as nurses in the new NHS »."),
   TF(D, "Finding a flat was easy.", False, "« it was hard to find a flat »."),
   TF(D, "The Notting Hill Carnival started after the 1958 riots.", True, "« The next year »."),
   TF(D, "In 2018, the government refused to apologise.", False, "« The government apologised »." )],
  [Q(D, "Why did Britain need workers?", ["To rebuild the country after the war.", "To build ships.", "To fight a war."]),
   Q(D, "What jobs did many immigrants do?", ["Nurses and bus drivers.", "Teachers and lawyers.", "Pilots and actors."]),
   Q(D, "What happened in 2018?", ["Some legal immigrants were treated as illegal.", "A new ship arrived.", "The carnival stopped."]),
   Q(D, "What is Windrush Day?", ["A day to celebrate the Caribbean community in Britain.", "A sailing race.", "A bank holiday in Jamaica."])],
  [DT(D, "Dans quel port arrive le Windrush ?", ["Tilbury, près de Londres", "Liverpool", "Belfast", "Southampton"]),
   DT(D, "Qui organise le premier carnaval caribéen en 1959 ?", ["Claudia Jones", "Amber Rudd", "Rosa Parks", "Bob Marley"]),
   DT(D, "Comment s'appelle la politique liée au scandale de 2018 ?", ["L'environnement hostile", "Le Welfare State", "Le Commonwealth", "Le Brexit"]),
   DT(D, "Comment dit-on « expulser » ?", ["To deport", "To export", "To import", "To report"])],
  [W(D, "Trouve le mot qui veut dire « reconstruire ».", "rebuild"), W(D, "Trouve le mot qui veut dire « émeutes ».", "riots"),
   W(D, "Trouve le mot qui veut dire « légalement ».", "legally"), W(D, "Trouve le mot qui veut dire « s'est excusé ».", "apologised")])

# ═════════ 1776 ═════════
F = "cu_revolution_americaine.html"
DZ(F, """
## Treize colonies en colère
Au milieu du 18e siècle, les **Thirteen Colonies** britanniques s'étendent le long de la côte atlantique, du Massachusetts à la Géorgie. Après une longue guerre contre la France (1754-1763), le Royaume-Uni est endetté et décide de faire payer les colons : taxe sur les documents imprimés (**Stamp Act**, 1765), puis sur le thé, le verre, le papier. Les colons protestent : ils n'ont pas de représentants au Parlement de Londres. Leur slogan : « *No taxation without representation* ».

## De la colère à la guerre
- En **1770**, des soldats britanniques tirent sur une foule à Boston : c'est le **Boston Massacre** (5 morts).
- En **1773**, des colons déguisés en Amérindiens jettent des caisses de thé dans le port : la **Boston Tea Party**.
- En **avril 1775**, les premiers coups de feu éclatent à Lexington et Concord : la guerre d'Indépendance commence. **George Washington** prend la tête de l'armée continentale.

## La Déclaration d'indépendance
Le **4 juillet 1776**, à Philadelphie, le Congrès continental adopte la **Declaration of Independence**, rédigée surtout par Thomas Jefferson. Elle affirme que « *all men are created equal* » et ont des droits que nul ne peut leur retirer, dont « la vie, la liberté et la recherche du bonheur ». Le 4 juillet devient la fête nationale, **Independence Day**.
Ce texte contient une profonde contradiction : beaucoup de ses signataires, dont Jefferson lui-même, possèdent des esclaves, et les femmes comme les Amérindiens sont exclus de cette égalité.

## Le rôle de la France
La guerre est longue et difficile pour les Américains. Après leur victoire de **Saratoga** (1777), la France, rivale du Royaume-Uni, s'allie à eux en 1778 et envoie argent, armes, soldats et navires. Le jeune marquis de **La Fayette**, volontaire, devient un proche de Washington. En **1781**, à **Yorktown**, l'armée britannique, encerclée par les troupes de Washington et de Rochambeau et bloquée par la flotte française, capitule. Par le traité de Paris de **1783**, le Royaume-Uni reconnaît l'indépendance des États-Unis.

## Une nouvelle nation
En **1787**, à Philadelphie, les délégués rédigent la **Constitution**, qui commence par « *We the People* » et organise la séparation des pouvoirs : un président, un Congrès et une Cour suprême. En 1789, Washington devient le premier président. En 1791, les dix premiers amendements, le **Bill of Rights**, garantissent les libertés fondamentales : liberté d'expression, de religion, de la presse… La Constitution américaine est la plus ancienne constitution écrite encore en vigueur. La Révolution américaine a inspiré la Révolution française de 1789.
Environ un colon sur cinq, les **Loyalists**, est resté fidèle au roi ; des dizaines de milliers d'entre eux ont fui vers le Canada après la guerre.
[→ Voir aussi : les Pères pèlerins et les colonies](cu_pilgrims.html)
""", """
a colony = une colonie
a tax = un impôt, une taxe
tea = le thé
a war = une guerre
a king = un roi
independence = l'indépendance
freedom = la liberté
a president = un président
""", [
 ("Pourquoi les colons protestent-ils ?", ["Ils paient des taxes sans être représentés au Parlement", "Ils veulent plus de thé", "Ils veulent un roi"], ""),
 ("Qu'est-ce que la Boston Tea Party ?", ["Des colons jettent du thé dans le port pour protester", "Une fête avec du thé", "Une bataille navale"], ""),
 ("Que se passe-t-il le 4 juillet 1776 ?", ["Le Congrès adopte la Déclaration d'indépendance", "La guerre se termine", "Washington devient président"], ""),
 ("Quelle contradiction contient la Déclaration ?", ["Elle proclame l'égalité mais beaucoup de signataires possèdent des esclaves", "Elle est écrite en français", "Elle interdit la liberté"], ""),
 ("Quel rôle joue la France ?", ["Elle s'allie aux Américains et les aide à gagner", "Elle aide les Britanniques", "Elle reste neutre"], ""),
 ("Que garantit le Bill of Rights ?", ["Les libertés fondamentales, comme la liberté d'expression", "Le droit du roi", "Les impôts"], ""),
], [("Thomas Jefferson", "futur 3e président des États-Unis"), ("**La Fayette**", "officier français volontaire"), ("Rochambeau", "général français")])
D = "ar"
culture(F, "Culture : The American Revolution", 'The American <span>Revolution</span>',
  "Culture · 1776 et la naissance des États-Unis", ("#bfdbfe", "#b91c1c"),
  reperes("Entre 1775 et 1783, treize colonies britanniques d'Amérique se révoltent contre le roi et fondent les États-Unis.",
    [("1765", "Stamp Act : « No taxation without representation »"), ("1773", "Boston Tea Party"), ("4 juillet 1776", "Déclaration d'indépendance"),
     ("1778", "alliance avec la France"), ("1781", "victoire de Yorktown"), ("1787", "Constitution des États-Unis"), ("1789", "Washington, premier président")],
    "a colony, a tax, independence, a declaration, a revolution, the Constitution, a right, freedom"),
  {D: doc("No taxation without representation", [
    "In the 18th century, there were thirteen British colonies in America. Britain decided to make the colonists pay new taxes, but they had no representatives in the British Parliament.",
    "The colonists protested. In 1773, in Boston, they threw British tea into the sea: this was the Boston Tea Party. In 1775, the war started. George Washington led the American army.",
    "On 4 July 1776, the colonies declared their independence. The Declaration said that all men are created equal. But many of its authors had slaves.",
    "France helped the Americans with money, ships and soldiers, like the young Marquis de La Fayette. In 1781, the British army surrendered at Yorktown.",
    "In 1787, the Americans wrote the Constitution. In 1789, George Washington became the first President of the United States. Today, Americans celebrate Independence Day every 4 July."])},
  [TF(D, "There were thirteen British colonies in America.", True, "« thirteen British colonies »."),
   TF(D, "The colonists had representatives in the British Parliament.", False, "« they had no representatives »."),
   TF(D, "During the Boston Tea Party, they threw tea into the sea.", True, "« threw British tea into the sea »."),
   TF(D, "France helped the British.", False, "« France helped the Americans »."),
   TF(D, "The British army surrendered at Yorktown.", True, "« surrendered at Yorktown »."),
   TF(D, "George Washington was the first President.", True, "« the first President »." )],
  [Q(D, "Why did the colonists protest?", ["Because of new taxes without representation.", "Because they wanted a king.", "Because they wanted to go back to Britain."]),
   Q(D, "Who led the American army?", ["George Washington.", "Thomas Jefferson.", "Abraham Lincoln."]),
   Q(D, "What did the Declaration say?", ["All men are created equal.", "The king is always right.", "Taxes are good."]),
   Q(D, "How did France help?", ["With money, ships and soldiers.", "With tea.", "It did not help."])],
  [DT(D, "Qui rédige surtout la Déclaration d'indépendance ?", ["Thomas Jefferson", "George Washington", "Benjamin Franklin", "La Fayette"]),
   DT(D, "Dans quelle ville est signée la Déclaration ?", ["Philadelphie", "Boston", "New York", "Washington"]),
   DT(D, "Comment s'appellent les colons restés fidèles au roi ?", ["Les Loyalists", "Les Patriots", "Les Pilgrims", "Les Yankees"]),
   DT(D, "Par quels mots commence la Constitution ?", ["« We the People »", "« God save the King »", "« Yes we can »", "« In God we trust »"])],
  [W(D, "Trouve le mot qui veut dire « impôts, taxes ».", "taxes"), W(D, "Trouve le mot qui veut dire « représentants ».", "representatives"),
   W(D, "Trouve le mot qui veut dire « a dirigé ».", "led"), W(D, "Trouve le mot qui veut dire « a capitulé ».", "surrendered")])

# ═════════ AMERICAN DREAM ═════════
F = "cu_reve_americain.html"
DZ(F, """
## Qu'est-ce que le rêve américain ?
L'**American Dream** est l'idée qu'aux États-Unis, chacun, quelle que soit son origine, peut réussir grâce à son travail et à son talent, et vivre mieux que ses parents. L'expression est popularisée en 1931 par l'historien James Truslow Adams, en pleine Grande Dépression. Elle s'appuie sur la promesse de la Déclaration d'indépendance : le droit de chacun à « la recherche du bonheur ».

## Des symboles
- La **statue de la Liberté** (1886), offerte par la France, accueillait les millions d'immigrants arrivant à New York.
- Le **self-made man**, l'homme qui ne doit sa réussite qu'à lui-même. L'exemple classique est **Andrew Carnegie**, arrivé d'Écosse sans le sou, devenu l'un des hommes les plus riches du monde grâce à l'acier.
- Les romans de Horatio Alger, au 19e siècle, racontent des histoires de jeunes pauvres qui deviennent riches : « *from rags to riches* » (des haillons à la richesse).
- Après 1945, le rêve prend la forme de la maison individuelle en banlieue avec sa pelouse et sa barrière blanche (**white picket fence**), une voiture et des enfants qui iront à l'université.

## Wall Street, cœur de la finance
**Wall Street**, une rue du sud de Manhattan, abrite la Bourse de New York (**New York Stock Exchange**), née d'un accord entre courtiers signé en 1792 sous un platane. Le mot désigne aujourd'hui toute la finance américaine. Wall Street a connu des crises majeures : le krach de **1929**, qui déclenche la Grande Dépression, et la crise financière de **2008**, provoquée par des prêts immobiliers risqués (**subprimes**), qui entraîne la faillite de la banque Lehman Brothers et des millions de saisies de maisons. En 2011, le mouvement **Occupy Wall Street** dénonce les inégalités avec le slogan « *We are the 99%* ».

## Le rêve est-il toujours vivant ?
Des économistes ont mesuré que presque tous les Américains nés en 1940 gagnaient plus que leurs parents au même âge, contre seulement environ la moitié de ceux nés dans les années 1980. Le coût des études, de la santé et du logement rend l'ascension sociale plus difficile, et les inégalités de richesse sont parmi les plus fortes des pays développés.
Pourtant, le rêve américain continue d'attirer : des millions d'immigrants viennent chaque année tenter leur chance, et de nombreux entrepreneurs ont bâti des fortunes en une génération. Pour beaucoup, il signifie moins devenir riche que vivre en sécurité, dans la liberté, et offrir à ses enfants une vie meilleure.
[→ Voir aussi : le krach de 1929 et le New Deal](cu_1929_new_deal.html)
""", """
a dream = un rêve
rich = riche
poor = pauvre
success = la réussite
hard work = le travail acharné
money = l'argent
a bank = une banque
a house = une maison
""", [
 ("Qu'est-ce que le rêve américain ?", ["L'idée que chacun peut réussir grâce à son travail", "Un film", "Une loi"], ""),
 ("Qu'est-ce qu'un « self-made man » ?", ["Un homme qui ne doit sa réussite qu'à lui-même", "Un robot", "Un héritier"], ""),
 ("Que signifie « from rags to riches » ?", ["Passer de la pauvreté à la richesse", "Vendre des vêtements", "Perdre sa fortune"], ""),
 ("Qu'est-ce que Wall Street ?", ["La rue de la Bourse de New York, symbole de la finance", "Un mur à la frontière", "Un quartier de Los Angeles"], ""),
 ("Que dénonce Occupy Wall Street ?", ["Les inégalités", "Les impôts trop bas", "Les immigrants"], ""),
 ("Pourquoi dit-on que le rêve est plus difficile aujourd'hui ?", ["Les études, la santé et le logement coûtent cher", "Il n'y a plus de travail", "Il est interdit"], ""),
], [("**Andrew Carnegie**", "industriel de l'acier, 1835-1919"), ("Horatio Alger", "romancier américain du 19e siècle"), ("Lehman Brothers", "grande banque d'affaires américaine")])
D = "dr"
culture(F, "Culture : The American Dream", 'The American <span>Dream</span>',
  "Culture · réussite, Wall Street et inégalités", ("#fde68a", "#166534"),
  reperes("Le rêve américain, c'est l'idée que chacun peut réussir par son travail. Wall Street, symbole de la finance, en montre la puissance et les crises.",
    [("1776", "le droit à « la recherche du bonheur »"), ("1886", "la statue de la Liberté"), ("1929", "krach de Wall Street"),
     ("1931", "l'expression « American Dream » est popularisée"), ("2008", "crise financière"), ("2011", "Occupy Wall Street")],
    "the American Dream, success, a self-made man, from rags to riches, Wall Street, the stock market, inequality, social mobility"),
  {D: doc("From rags to riches", [
    "The American Dream is the idea that in the USA, everybody can succeed with hard work, and have a better life than their parents.",
    "Some famous people are examples of this dream. Andrew Carnegie arrived from Scotland as a poor boy and became one of the richest men in the world.",
    "After 1945, the dream was a house in the suburbs, a car, and children who would go to university.",
    "Wall Street, in New York, is the centre of American finance. It is a symbol of money and success, but also of crises, like in 1929 and 2008.",
    "Today, many people say the dream is harder to reach, because university, health and houses are very expensive. But millions of immigrants still come to the USA to try their chance."])},
  [TF(D, "The American Dream is the idea that everybody can succeed.", True, "« everybody can succeed »."),
   TF(D, "Andrew Carnegie was born rich.", False, "« a poor boy »."),
   TF(D, "Wall Street is in Los Angeles.", False, "« in New York »."),
   TF(D, "There were crises in 1929 and 2008.", True, "« like in 1929 and 2008 »."),
   TF(D, "University is cheap in the USA.", False, "« very expensive »."),
   TF(D, "Immigrants still come to the USA to try their chance.", True, "« millions of immigrants still come »." )],
  [Q(D, "What is the American Dream?", ["The idea that hard work leads to success.", "A Hollywood film.", "A bank."]),
   Q(D, "Who is Andrew Carnegie?", ["A poor boy who became very rich.", "A President.", "A singer."]),
   Q(D, "What is Wall Street a symbol of?", ["Money and success.", "Sport.", "Religion."]),
   Q(D, "Why is the dream harder to reach today?", ["University, health and houses are expensive.", "There are no schools.", "It is illegal."])],
  [DT(D, "Quel monument accueillait les immigrants à New York ?", ["La statue de la Liberté", "L'Empire State Building", "Le Golden Gate", "La Maison-Blanche"]),
   DT(D, "Quelle banque fait faillite en 2008 ?", ["Lehman Brothers", "Wall Street Bank", "Carnegie Bank", "Bank of England"]),
   DT(D, "Quel est le slogan d'Occupy Wall Street ?", ["« We are the 99% »", "« Yes we can »", "« Make America Great »", "« No taxation »"]),
   DT(D, "Que symbolise la « white picket fence » ?", ["La maison idéale en banlieue", "La frontière", "Une prison", "Une banque"])],
  [W(D, "Trouve le mot qui veut dire « réussir ».", "succeed"), W(D, "Trouve le mot qui veut dire « travail acharné » (2 mots).", ["hard work"]),
   W(D, "Trouve le mot qui veut dire « banlieue ».", "suburbs"), W(D, "Trouve le mot qui veut dire « atteindre ».", "reach")])

# ═════════ HIP-HOP ═════════
F = "cu_hip_hop.html"
DZ(F, """
## Une fête dans le Bronx
Le **11 août 1973**, dans la salle commune d'un immeuble du **Bronx**, à New York, un jeune DJ d'origine jamaïcaine, **DJ Kool Herc**, anime une fête pour la rentrée de sa sœur. Il a une idée : avec deux platines, il fait tourner en boucle le passage instrumental le plus rythmé des disques, le **break**, sur lequel les gens dansent. On considère souvent ce jour comme la naissance du **hip-hop**. Le Bronx est alors un quartier pauvre, abandonné par les pouvoirs publics, frappé par les incendies et la violence ; les jeunes noirs et latinos y inventent une culture à partir de presque rien.

## Les quatre éléments
Le hip-hop n'est pas seulement une musique, mais une culture avec quatre « éléments » :
- le **DJing** : mixer et « scratcher » les disques ;
- le **MCing**, ou **rap** : parler en rythme sur la musique ;
- le **breaking** (ou breakdance) : une danse acrobatique ;
- le **graffiti** : peindre son nom ou des fresques sur les murs et les rames de métro.
Afrika Bambaataa, fondateur de la **Zulu Nation**, veut faire du hip-hop une alternative pacifique à la violence des gangs, autour de valeurs comme « *peace, love, unity and having fun* ».

## Du Bronx au monde
En 1979, *Rapper's Delight* du Sugarhill Gang est le premier grand succès commercial du rap. Dans les années 1980, Grandmaster Flash, Run-DMC et Public Enemy portent des textes sur la vie dans les quartiers et la politique. Dans les années 1990, une rivalité oppose la côte Est et la côte Ouest ; elle se termine tragiquement par l'assassinat de deux stars, Tupac Shakur (1996) et The Notorious B.I.G. (1997). Puis viennent Eminem, Jay-Z, Kanye West, Drake, Kendrick Lamar…

## Une culture devenue dominante
Le hip-hop est devenu le genre musical le plus écouté aux États-Unis. En 2018, le rappeur **Kendrick Lamar** reçoit le prix Pulitzer de musique, une première pour un artiste qui n'est ni classique ni jazz. Le **breaking** a été une discipline olympique aux Jeux de Paris en 2024. Le hip-hop influence la mode (baskets, casquettes, survêtements), la langue et la publicité. Il s'est diffusé partout : la France est l'un des plus grands marchés de rap au monde, et le Royaume-Uni a inventé ses propres genres, comme le **grime**.

## Les critiques
Le rap a souvent été critiqué pour la violence, le sexisme ou le culte de l'argent présents dans certains textes. Ses défenseurs répondent qu'il décrit une réalité sociale, qu'il donne une voix à ceux qu'on n'entend pas, et qu'il existe une grande diversité de rap, engagé, poétique ou festif.
[→ Voir aussi : les musiques anglophones](cu_musique.html)
""", """
music = la musique
a song = une chanson
a dancer = un danseur
a wall = un mur
a party = une fête
a record = un disque
the rhythm = le rythme
a neighbourhood = un quartier
""", [
 ("Où et quand le hip-hop est-il né ?", ["Dans le Bronx, à New York, en 1973", "À Londres en 1960", "À Paris en 1990"], ""),
 ("Qu'a inventé DJ Kool Herc ?", ["Faire tourner en boucle le « break » des disques", "La guitare électrique", "Le graffiti"], ""),
 ("Quels sont les quatre éléments du hip-hop ?", ["DJing, rap, breaking, graffiti", "Chant, piano, violon, opéra", "Football, basket, tennis, golf"], ""),
 ("Que voulait la Zulu Nation ?", ["Une alternative pacifique à la violence des gangs", "Plus de violence", "Interdire la musique"], ""),
 ("Quel prix Kendrick Lamar a-t-il reçu en 2018 ?", ["Le prix Pulitzer de musique", "Un Oscar", "Le prix Nobel"], ""),
 ("Que répondent les défenseurs du rap aux critiques ?", ["Il décrit une réalité sociale et donne une voix aux oubliés", "Il n'existe pas", "Il est toujours violent"], ""),
], [("Afrika Bambaataa", "DJ et pionnier du hip-hop"), ("Sugarhill Gang", "groupe de rap du New Jersey"), ("Tupac Shakur", "rappeur de la côte Ouest")])
D = "hh"
culture(F, "Culture : Hip-hop", 'Hip-<span>hop</span>',
  "Culture · du Bronx à la planète", ("#fbbf24", "#7c3aed"),
  reperes("Né en 1973 dans le Bronx, à New York, le hip-hop est une culture complète (musique, danse, art) devenue le genre le plus écouté aux États-Unis.",
    [("1973", "fête de DJ Kool Herc dans le Bronx"), ("1979", "Rapper's Delight, premier grand succès"), ("années 1990", "rivalité côte Est / côte Ouest"),
     ("2018", "Kendrick Lamar, prix Pulitzer"), ("2024", "le breaking aux Jeux olympiques de Paris")],
    "a DJ, a rapper, a beat, lyrics, breaking, graffiti, a crew, a record"),
  {D: doc("Born in the Bronx", [
    "Hip-hop was born in 1973 in the Bronx, a poor neighbourhood of New York. At a party, DJ Kool Herc played the best rhythmic part of records again and again, and people danced.",
    "Hip-hop is a whole culture with four elements: DJing, rapping, breaking (a kind of dance) and graffiti.",
    "In 1979, the first big rap hit was released. Then many famous rappers appeared, like Run-DMC, Tupac, Eminem, Jay-Z and Kendrick Lamar.",
    "Today, hip-hop is the most popular music genre in the USA. In 2024, breaking was an Olympic sport in Paris. Hip-hop also influences fashion and language.",
    "Some people criticise violent or sexist lyrics. Others say that rap describes social reality and gives a voice to people who are not heard."])},
  [TF(D, "Hip-hop was born in the Bronx.", True, "« in the Bronx »."),
   TF(D, "The Bronx was a rich neighbourhood.", False, "« a poor neighbourhood »."),
   TF(D, "Hip-hop has four elements.", True, "« four elements »."),
   TF(D, "Breaking is a kind of painting.", False, "« a kind of dance »."),
   TF(D, "Hip-hop is the most popular genre in the USA.", True, "« the most popular music genre »."),
   TF(D, "Breaking was an Olympic sport in 2024.", True, "« In 2024, breaking was an Olympic sport »." )],
  [Q(D, "What did DJ Kool Herc do?", ["He played the best rhythmic part of records again and again.", "He sang opera.", "He painted walls."]),
   Q(D, "Name the four elements of hip-hop.", ["DJing, rapping, breaking and graffiti.", "Piano, violin, guitar and drums.", "Rock, pop, jazz and blues."]),
   Q(D, "What does hip-hop influence?", ["Fashion and language.", "Only politics.", "Nothing."]),
   Q(D, "What do some people criticise?", ["Violent or sexist lyrics.", "The dance.", "The DJs' clothes."])],
  [DT(D, "Qui anime la fête de 1973 ?", ["DJ Kool Herc", "Eminem", "Kendrick Lamar", "Bob Marley"]),
   DT(D, "Quel est le premier grand succès du rap ?", ["Rapper's Delight", "Thriller", "Hey Jude", "Hound Dog"]),
   DT(D, "Quel genre britannique vient du hip-hop ?", ["Le grime", "Le punk", "La britpop", "Le skiffle"]),
   DT(D, "Quel rappeur reçoit le prix Pulitzer ?", ["Kendrick Lamar", "Jay-Z", "Drake", "Tupac"])],
  [W(D, "Trouve le mot qui veut dire « quartier ».", "neighbourhood"), W(D, "Trouve le mot qui veut dire « encore et encore » (3 mots).", ["again and again"]),
   W(D, "Trouve le mot qui veut dire « paroles » (d'une chanson).", "lyrics"), W(D, "Trouve le mot qui veut dire « une voix ».", ["voice", "a voice"])])

# ═════════ CARAÏBES ═════════
F = "cu_caraibes.html"
DZ(F, """
## Les Caraïbes anglophones
Plusieurs pays des Caraïbes parlent anglais : la **Jamaïque**, **Trinidad-et-Tobago**, la **Barbade**, les **Bahamas**, Sainte-Lucie, Antigua, Grenade… ainsi que le Guyana et le Belize sur le continent. Ensemble, ils sont parfois appelés les **West Indies**, le nom donné par Christophe Colomb, qui croyait être arrivé aux Indes en 1492.

## L'histoire : sucre et esclavage
Aux 17e et 18e siècles, les Britanniques colonisent ces îles pour y cultiver la **canne à sucre**. La Barbade, colonisée à partir de 1627, devient l'une des colonies les plus riches de l'Empire. Pour travailler dans les plantations, des centaines de milliers d'Africains sont réduits en esclavage et déportés dans des conditions terribles. L'esclavage est aboli dans l'Empire britannique par une loi de 1833 ; les anciens propriétaires reçoivent une énorme compensation financière, mais pas les anciens esclaves. Après l'abolition, des travailleurs venus d'Inde arrivent, notamment à Trinidad, d'où une population très mélangée.

## Les indépendances
Dans les années 1960 et 1970, les îles deviennent indépendantes : la Jamaïque et Trinidad-et-Tobago en **1962**, la Barbade en **1966**, les Bahamas en 1973. La plupart restent membres du Commonwealth, et plusieurs gardent le roi britannique comme chef d'État. Mais le débat sur la monarchie grandit : le **30 novembre 2021**, la Barbade devient une **république**, avec sa propre présidente. Plusieurs pays réclament aussi des **reparations**, des compensations pour l'esclavage.

## Une culture très riche
- **Trinidad** est célèbre pour son **carnaval** et pour avoir inventé le **steelpan** (tambour d'acier) dans les années 1930-1940, ainsi que le calypso et la soca.
- Le **cricket** est une passion : les îles forment ensemble l'équipe des **West Indies**, longtemps l'une des meilleures du monde.
- Dans la vie quotidienne, on parle souvent un **créole** à base d'anglais, comme le *Bajan* à la Barbade.
- La chanteuse **Rihanna**, née à la Barbade, a été nommée héroïne nationale de son pays en 2021.
- La cuisine mêle influences africaines, indiennes et européennes : riz aux haricots rouges, curry, poisson volant, rhum.

## Les défis
Le tourisme est essentiel à l'économie (plages, croisières), mais il rend ces pays fragiles. Les îles sont aussi en première ligne face au **changement climatique** : ouragans de plus en plus violents et montée des océans. La Première ministre de la Barbade, **Mia Mottley**, est devenue une voix importante pour la justice climatique dans le monde.
[→ Voir aussi : la Jamaïque](cu_jamaique.html)
""", """
an island = une île
a beach = une plage
sugar = le sucre
a slave = un esclave
a republic = une république
a drum = un tambour
a hurricane = un ouragan
the sea = la mer
""", [
 ("Pourquoi appelle-t-on ces îles les « West Indies » ?", ["Christophe Colomb croyait être arrivé aux Indes", "Elles sont à l'ouest de l'Inde", "C'est le nom d'un roi"], ""),
 ("Pourquoi les Britanniques colonisent-ils ces îles ?", ["Pour cultiver la canne à sucre", "Pour le pétrole", "Pour le ski"], ""),
 ("Qui reçoit une compensation après l'abolition de 1833 ?", ["Les anciens propriétaires d'esclaves", "Les anciens esclaves", "Personne"], ""),
 ("Que devient la Barbade en 2021 ?", ["Une république", "Une colonie", "Un État américain"], ""),
 ("Qu'est-ce que le steelpan ?", ["Un tambour d'acier inventé à Trinidad", "Une poêle", "Un bateau"], ""),
 ("Quel défi menace particulièrement les îles ?", ["Le changement climatique et les ouragans", "Le froid", "Le manque de touristes"], ""),
], [("Christophe Colomb", "navigateur au service de l'Espagne"), ("**Mia Mottley**", "Première ministre de la Barbade depuis 2018")])
D = "cb"
culture(F, "Culture : The English-speaking Caribbean", 'The <span>Caribbean</span>',
  "Culture · Barbade, Trinidad, cricket et carnaval", ("#5eead4", "#ca8a04"),
  reperes("Plusieurs îles des Caraïbes, anciennes colonies britanniques, parlent anglais. Elles ont une histoire marquée par l'esclavage et une culture très riche.",
    [("1492", "arrivée de Christophe Colomb"), ("1627", "début de la colonisation de la Barbade"), ("1833", "abolition de l'esclavage dans l'Empire britannique"),
     ("1962", "indépendance de la Jamaïque et de Trinidad-et-Tobago"), ("1966", "indépendance de la Barbade"), ("2021", "la Barbade devient une république")],
    "an island, a plantation, slavery, independence, a republic, cricket, a carnival, a hurricane"),
  {D: doc("Sun, sugar and steelpan", [
    "Many Caribbean islands speak English, like Jamaica, Barbados, Trinidad and Tobago, and the Bahamas. They are former British colonies.",
    "In the past, the British grew sugar cane there. Hundreds of thousands of Africans were forced to work as slaves on the plantations. Slavery was abolished in the 1830s.",
    "The islands became independent in the 1960s and 1970s. In 2021, Barbados became a republic: the British king is no longer its head of state.",
    "Caribbean culture is very rich. Trinidad is famous for its carnival and for inventing the steelpan, a drum made of steel. People love cricket, and Rihanna comes from Barbados.",
    "Tourism is very important, but the islands are in danger because of climate change: hurricanes are stronger and the sea level is rising."])},
  [TF(D, "Barbados is a former British colony.", True, "« former British colonies »."),
   TF(D, "The British grew coffee on the islands.", False, "« sugar cane »."),
   TF(D, "Slavery was abolished in the 1830s.", True, "« in the 1830s »."),
   TF(D, "The British king is still the head of state of Barbados.", False, "« no longer its head of state »."),
   TF(D, "The steelpan was invented in Trinidad.", True, "« Trinidad… inventing the steelpan »."),
   TF(D, "Hurricanes are becoming weaker.", False, "« hurricanes are stronger »." )],
  [Q(D, "What did the British grow on the islands?", ["Sugar cane.", "Tea.", "Potatoes."]),
   Q(D, "What happened in Barbados in 2021?", ["It became a republic.", "It became British again.", "It joined the USA."]),
   Q(D, "What is a steelpan?", ["A drum made of steel.", "A kitchen tool.", "A boat."]),
   Q(D, "Why are the islands in danger?", ["Because of climate change.", "Because of tourists.", "Because of cricket."])],
  [DT(D, "Quelle chanteuse est née à la Barbade ?", ["Rihanna", "Beyoncé", "Adele", "Taylor Swift"]),
   DT(D, "Quel sport est une passion dans les Caraïbes anglophones ?", ["Le cricket", "Le hockey sur glace", "Le ski", "Le rugby à XIII"]),
   DT(D, "Comment s'appelle le créole de la Barbade ?", ["Le Bajan", "Le Singlish", "Le Patois de Londres", "Le Spanglish"]),
   DT(D, "Que réclament plusieurs pays pour l'esclavage ?", ["Des reparations", "Des visas", "Des touristes", "Des canons"])],
  [W(D, "Trouve le mot qui veut dire « anciennes » (colonies).", "former"), W(D, "Trouve le mot qui veut dire « canne à sucre » (2 mots).", ["sugar cane"]),
   W(D, "Trouve le mot qui veut dire « chef d'État » (3 mots).", ["head of state"]), W(D, "Trouve le mot qui veut dire « monte » (le niveau de la mer).", "rising")])

# ═════════ CAP : SOINS AUX PERSONNES ÂGÉES ═════════
F = "cu_soins_ages.html"
DZ(F, """
## Une population qui vieillit
Comme en France, la population du Royaume-Uni et des États-Unis vieillit : on vit plus longtemps, et le nombre de personnes très âgées, parfois dépendantes ou atteintes de **dementia** (démence, comme la maladie d'Alzheimer), augmente. Prendre soin des personnes âgées, la **elderly care** ou **social care**, est devenu un grand enjeu de société.

## Au Royaume-Uni
- Les soins médicaux sont gratuits grâce au **NHS**, mais l'aide à la vie quotidienne (se laver, s'habiller, manger) relève de la **social care**, organisée par les collectivités locales (**councils**). Elle n'est pas gratuite pour tout le monde : en Angleterre, les personnes qui ont un certain niveau d'économies ou une maison doivent payer elles-mêmes, ce qui oblige parfois à vendre son logement. Ce système est très débattu.
- Les personnes qui restent chez elles peuvent recevoir la visite de **care workers** (aides à domicile) : on parle de **home care** ou **domiciliary care**.
- Les **care homes** accueillent les résidents qui ne peuvent plus vivre seuls ; les **nursing homes** offrent en plus des soins infirmiers.
- Le secteur manque de personnel : le travail est difficile et souvent mal payé, et une partie des employés vient de l'étranger.
- Environ 5 millions de personnes, en Angleterre et au pays de Galles, sont des **unpaid carers** : elles s'occupent gratuitement d'un proche (parent, conjoint, enfant malade).

## Aux États-Unis
- **Medicare** (pour les 65 ans et plus) paie les soins médicaux, mais presque pas les soins de longue durée.
- Une place en **nursing home** peut coûter plus de 100 000 dollars par an. Beaucoup de familles dépensent toutes leurs économies avant de pouvoir être aidées par **Medicaid**, le programme pour les personnes à faibles revenus.
- Il existe aussi l'**assisted living** (résidences avec services) et les **retirement communities**, des villages de retraités, très nombreux en Floride et en Arizona.
- Les **home health aides** (aides à domicile) font partie des métiers qui recrutent le plus.

## Le métier au quotidien
Les **care workers** aident à la toilette (**personal care**), à l'habillage, aux repas, à la prise des médicaments (**medication**), aux déplacements (**mobility**), en utilisant parfois un fauteuil roulant (**wheelchair**) ou un lève-personne (**hoist**). Mais leur rôle est aussi humain : discuter, rassurer, rompre la solitude (**loneliness**), respecter la dignité et l'intimité de la personne. Au Royaume-Uni, on appelle souvent les personnes âgées par leur prénom, ou affectueusement « *love* » ou « *dear* » dans certaines régions ; en cas de doute, il vaut mieux demander : « *What would you like me to call you?* »
[→ Voir aussi : l'anglais de l'aide à la personne](cap_aide.html)
""", """
an elderly person = une personne âgée
a care home = une maison de retraite
a carer = un aidant, une aide-soignante
a resident = un résident
a wheelchair = un fauteuil roulant
medication = les médicaments
lonely = seul, isolé
to help = aider
""", [
 ("Qu'est-ce que la « social care » au Royaume-Uni ?", ["L'aide à la vie quotidienne (se laver, s'habiller, manger)", "Les soins à l'hôpital", "Les réseaux sociaux"], ""),
 ("La social care est-elle gratuite pour tous en Angleterre ?", ["Non, ceux qui ont des économies ou une maison paient", "Oui, toujours", "Elle n'existe pas"], ""),
 ("Qu'est-ce qu'un « unpaid carer » ?", ["Quelqu'un qui s'occupe gratuitement d'un proche", "Un médecin bénévole", "Un patient"], ""),
 ("Que paie Medicare aux États-Unis ?", ["Les soins médicaux, mais presque pas les soins de longue durée", "Tout, gratuitement", "Rien"], ""),
 ("Que fait un care worker au quotidien ?", ["Il aide à la toilette, l'habillage, les repas et rompt la solitude", "Il opère les patients", "Il vend des médicaments"], ""),
 ("Que vaut-il mieux faire en cas de doute sur la façon d'appeler quelqu'un ?", ["Lui demander : « What would you like me to call you? »", "L'appeler « old man »", "Ne rien dire"], ""),
], [("Alzheimer", "maladie qui touche la mémoire")])
D = "sa"
culture(F, "Culture : Caring for elderly people", 'Caring for <span>elderly people</span>',
  "Culture · CAP Sapver · care homes, carers et aide à domicile", ("#99f6e4", "#0f766e"),
  reperes("Au Royaume-Uni et aux États-Unis, comme en France, les soins aux personnes âgées sont un grand enjeu. Les systèmes et le vocabulaire diffèrent.",
    [("social care", "aide à la vie quotidienne (Royaume-Uni)"), ("care home", "maison de retraite"), ("home care", "aide à domicile"),
     ("environ 5 millions", "d'aidants non rémunérés en Angleterre et au pays de Galles"), ("plus de 100 000 $", "par an pour une maison de retraite aux États-Unis")],
    "an elderly person, a care home, a care worker, a carer, a resident, personal care, mobility, dignity"),
  {D: doc("A day at Rosewood Care Home", [
    "In the UK and the USA, people live longer, and more and more elderly people need help in their daily life.",
    "In the UK, medical care is free with the NHS, but help to wash, dress or eat is called social care, and it is not always free. Some people must sell their house to pay for a care home.",
    "Many elderly people stay at home. Care workers visit them to help with personal care, meals and medication. Millions of people also look after a family member for free: they are unpaid carers.",
    "In the USA, a place in a nursing home is very expensive: it can cost more than $100,000 a year.",
    "Care workers do a difficult job. They help residents to move, eat and wash, but they also talk with them, because many elderly people feel lonely. Respect and dignity are very important."])},
  [TF(D, "People live longer in the UK and the USA.", True, "« people live longer »."),
   TF(D, "Social care is always free in the UK.", False, "« not always free »."),
   TF(D, "Care workers visit elderly people at home.", True, "« Care workers visit them »."),
   TF(D, "Unpaid carers are paid by the government.", False, "« for free »."),
   TF(D, "Nursing homes in the USA are cheap.", False, "« very expensive »."),
   TF(D, "Many elderly people feel lonely.", True, "« many elderly people feel lonely »." )],
  [Q(D, "What is social care?", ["Help to wash, dress or eat.", "Surgery in a hospital.", "A social network."]),
   Q(D, "What do care workers help with?", ["Personal care, meals and medication.", "Driving buses.", "Selling houses."]),
   Q(D, "Who are unpaid carers?", ["People who look after a family member for free.", "Doctors.", "Nurses in hospitals."]),
   Q(D, "Why do care workers talk with residents?", ["Because many elderly people feel lonely.", "To sell them something.", "Because it is the law."])],
  [DT(D, "Comment dit-on « un fauteuil roulant » ?", ["A wheelchair", "A wheel seat", "A rolling chair", "A sofa"]),
   DT(D, "Comment dit-on « une maison de retraite » ?", ["A care home", "A retired house", "An old home", "A rest station"]),
   DT(D, "Comment dit-on « la toilette » (aider à se laver) ?", ["Personal care", "The toilet", "Washing machine", "Bathroom"]),
   DT(D, "Comment dit-on « seul, isolé » ?", ["Lonely", "Lovely", "Lonesome care", "Only"])],
  [W(D, "Trouve le mot qui veut dire « personnes âgées » (2 mots).", ["elderly people"]), W(D, "Trouve le mot qui veut dire « s'habiller ».", "dress"),
   W(D, "Trouve le mot qui veut dire « s'occupent de » (2 mots).", ["look after"]), W(D, "Trouve le mot qui veut dire « la dignité ».", "dignity")])

# ═════════ CAP : SERVICE CLIENT ═════════
F = "cu_service_client.html"
DZ(F, """
## « Have a nice day! »
Dans un magasin américain, le client est accueilli avec un grand sourire : « *Hi, how are you doing today?* », et quitte la caisse avec « *Have a nice day!* ». Cette question « *How are you?* » n'attend pas une vraie réponse : on répond simplement « *Good, thanks! How are you?* ». Les Européens trouvent parfois cette amabilité exagérée ou artificielle ; pour les Américains, c'est simplement la politesse normale, et un service froid est vu comme impoli.

## « The customer is always right »
Cette formule, attribuée aux grands magasins de la fin du 19e siècle (Marshall Field à Chicago, Harry Gordon Selfridge à Londres), résume une culture où la satisfaction du client passe avant tout. Aux États-Unis, il est généralement facile de rapporter un article (**return policy**) et d'être remboursé (**refund**), même sans raison. Les entreprises font tout pour éviter une mauvaise note en ligne (**review**), car les avis des clients ont un énorme poids.

## Walmart et Tesco
- **Walmart**, fondé en 1962 dans l'Arkansas par Sam Walton, est la plus grande entreprise du monde par le chiffre d'affaires et le premier employeur privé des États-Unis. Il est connu pour ses **greeters**, des employés, souvent âgés, chargés d'accueillir les clients à l'entrée, et pour ses prix bas. Il est aussi critiqué pour ses salaires et ses conditions de travail.
- **Tesco** est le premier supermarché britannique. Comme d'autres enseignes, il a généralisé les caisses automatiques (**self-checkouts**), que certains clients apprécient pour leur rapidité et que d'autres critiquent, car elles suppriment des emplois et le contact humain.

## Le style britannique
Au Royaume-Uni, le service est souvent plus réservé. On dit « *Are you alright?* » (qui signifie « Je peux vous aider ? », pas « Ça va mal ? »), « *Cheers* » pour merci, et l'on appelle parfois le client « *love* » dans le Nord. Les Britanniques détestent les situations gênantes : beaucoup n'osent pas se plaindre, ou s'excusent même quand c'est le vendeur qui a fait l'erreur ! La file d'attente (**queue**) est sacrée : passer devant quelqu'un est très mal vu.

## Les phrases clés du vendeur
- Accueillir : « *Hello! Can I help you?* » / « *Are you looking for anything in particular?* »
- Proposer : « *Would you like to try it on?* » / « *We also have it in blue.* »
- Encaisser : « *That's £24.99, please.* » / « *Would you like a bag?* » / « *Cash or card?* »
- Gérer une réclamation : écouter, s'excuser (« *I'm really sorry about that.* »), proposer une solution (« *I can exchange it or give you a refund.* »).
- Prendre congé : « *Thank you, have a nice day!* » / « *Enjoy the rest of your day!* »
[→ Voir aussi : l'anglais de la vente](cap_vente.html)
""", """
a customer = un client
a shop assistant = un vendeur
a smile = un sourire
a bag = un sac
cash = les espèces
a refund = un remboursement
to exchange = échanger
a complaint = une réclamation
""", [
 ("Comment répondre à « How are you? » dans un magasin américain ?", ["« Good, thanks! How are you? »", "Raconter ses problèmes en détail", "Ne rien dire"], ""),
 ("Que signifie « The customer is always right » ?", ["La satisfaction du client passe avant tout", "Le client a toujours tort", "Le client doit payer plus"], ""),
 ("Qu'est-ce qu'un « greeter » chez Walmart ?", ["Un employé qui accueille les clients à l'entrée", "Un vigile", "Un caissier automatique"], ""),
 ("Que veut dire « Are you alright? » dans un magasin britannique ?", ["« Je peux vous aider ? »", "« Vous êtes malade ? »", "« Vous partez ? »"], ""),
 ("Comment réagissent souvent les Britanniques face à un problème ?", ["Beaucoup n'osent pas se plaindre", "Ils crient toujours", "Ils appellent la police"], ""),
 ("Que fait-on face à une réclamation ?", ["Écouter, s'excuser, proposer une solution", "Ignorer le client", "Se fâcher"], ""),
], [("Marshall Field", "fondateur d'un grand magasin de Chicago"), ("Harry Gordon Selfridge", "fondateur du grand magasin Selfridges à Londres"), ("Sam Walton", "fondateur de Walmart")])
D = "sc"
culture(F, "Culture : Customer service", 'Customer <span>service</span>',
  "Culture · CAP Sapver · « Have a nice day! » et le client roi", ("#5eead4", "#be185d"),
  reperes("Aux États-Unis, le service client est très chaleureux ; au Royaume-Uni, il est plus réservé. Connaître ces codes aide à bien accueillir un client anglophone.",
    [("Have a nice day!", "la formule américaine pour prendre congé"), ("The customer is always right", "le client est roi"), ("1962", "création de Walmart"),
     ("Are you alright?", "« Je peux vous aider ? » au Royaume-Uni"), ("Cheers", "« merci » au Royaume-Uni")],
    "a customer, a shop assistant, a refund, an exchange, a receipt, a complaint, a self-checkout, a queue"),
  {D: doc("Service with a smile", [
    "In American shops, shop assistants are usually very friendly. They smile and say \"Hi, how are you today?\". When you leave, they say \"Have a nice day!\".",
    "In the USA, people often say \"the customer is always right\". It is usually easy to return a product and get a refund.",
    "Walmart is the biggest supermarket chain in the USA. Some employees, called greeters, welcome customers at the entrance.",
    "In the UK, service is a little more reserved. A shop assistant may say \"Are you alright?\", which means \"Can I help you?\". British customers often don't like to complain, and queuing is very important.",
    "To deal with a complaint, a good shop assistant listens, apologises and offers a solution: an exchange or a refund."])},
  [TF(D, "American shop assistants are usually very friendly.", True, "« very friendly »."),
   TF(D, "In the USA, it is difficult to get a refund.", False, "« usually easy »."),
   TF(D, "Greeters welcome customers at the entrance.", True, "« welcome customers at the entrance »."),
   TF(D, "In the UK, \"Are you alright?\" means \"Are you ill?\".", False, "Cela veut dire « Can I help you? »."),
   TF(D, "British customers love to complain.", False, "« often don't like to complain »."),
   TF(D, "A good shop assistant listens and apologises.", True, "« listens, apologises and offers a solution »." )],
  [Q(D, "What do American shop assistants say when you leave?", ["Have a nice day!", "Go away!", "See you never!"]),
   Q(D, "What is a greeter?", ["An employee who welcomes customers.", "A manager.", "A security guard."]),
   Q(D, "What is very important in the UK?", ["Queuing.", "Shouting.", "Tipping."]),
   Q(D, "How do you deal with a complaint?", ["Listen, apologise and offer a solution.", "Ignore the customer.", "Call the police."])],
  [DT(D, "Comment dit-on « un remboursement » ?", ["A refund", "A receipt", "A discount", "A refill"]),
   DT(D, "Que signifie « Cheers » dans un magasin britannique ?", ["Merci", "Santé seulement", "Au revoir pour toujours", "Pardon"]),
   DT(D, "Comment demander le moyen de paiement ?", ["« Cash or card? »", "« Money or not? »", "« Pay me now? »", "« Gold or silver? »"]),
   DT(D, "Comment dit-on « faire la queue » ?", ["To queue", "To tail", "To line in", "To wait-list"])],
  [W(D, "Trouve le mot qui veut dire « aimables ».", "friendly"), W(D, "Trouve le mot qui veut dire « à l'entrée » (3 mots).", ["at the entrance"]),
   W(D, "Trouve le mot qui veut dire « se plaindre ».", "complain"), W(D, "Trouve le mot qui veut dire « traiter, gérer » (2 mots).", ["deal with"])])
END()
