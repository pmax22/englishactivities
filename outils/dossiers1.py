import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
D_ = {}

D_["cu_uk.html"] = """
## Un royaume, quatre nations
Le nom officiel du pays est **the United Kingdom of Great Britain and Northern Ireland**. Il est né d'une série d'unions : le pays de Galles est conquis par l'Angleterre au 13e siècle, l'Angleterre et l'Écosse s'unissent en 1707 pour former la **Great Britain**, puis l'Irlande est rattachée en 1801. Quand la plus grande partie de l'Irlande devient indépendante en 1922, seule l'Irlande du Nord reste dans le Royaume-Uni.
Attention aux mots : **England** n'est qu'une des quatre nations. Dire « English » à un Écossais ou à un Gallois peut le vexer : on dit **British** pour parler de tous les habitants du Royaume-Uni.

## Le drapeau, une histoire d'unions
Le **Union Jack** (ou Union Flag) superpose trois croix : la croix rouge de **Saint George** (Angleterre), la croix blanche en diagonale de **Saint Andrew** (Écosse) et la croix rouge en diagonale de **Saint Patrick** (Irlande). Le pays de Galles, déjà rattaché à l'Angleterre quand le drapeau a été créé, n'y figure pas : il a son propre drapeau avec un **red dragon**.
Chaque nation a aussi son saint patron et sa fête : St David (1er mars), St Patrick (17 mars), St George (23 avril), St Andrew (30 novembre).

## Quelques repères pratiques
- Environ 70 millions d'habitants, dont plus de 80 % en Angleterre.
- La monnaie est la **pound sterling** (£), divisée en 100 **pence**. Le Royaume-Uni n'a jamais adopté l'euro.
- On roule **on the left**, et les distances se comptent en **miles**.
- Les langues : l'anglais partout, le **Welsh** (gallois) au pays de Galles, le **Scottish Gaelic** dans le nord-ouest de l'Écosse, et l'irlandais en Irlande du Nord.

## Pourquoi c'est important aujourd'hui
Depuis 1999, l'Écosse, le pays de Galles et l'Irlande du Nord ont leurs propres parlements pour certains domaines : c'est la **devolution**. L'idée d'indépendance reste forte en Écosse, et le Brexit a relancé le débat sur l'avenir de l'Irlande du Nord. Le Royaume-Uni est donc un pays où l'identité nationale est une question vivante.
"""

D_["cu_monarchie.html"] = """
## Une monarchie très ancienne… mais limitée
La monarchie britannique remonte à plus de mille ans. Mais depuis longtemps, le roi ne gouverne plus seul. En 1215, la **Magna Carta** limite déjà le pouvoir du roi Jean. Au 17e siècle, une guerre civile oppose le roi et le Parlement : Charles Ier est même exécuté en 1649. Après la **Glorious Revolution** de 1688, le **Bill of Rights** (1689) établit que le Parlement est supérieur au roi.
C'est ce qu'on appelle une **constitutional monarchy** : le monarque est **head of state**, mais le pouvoir appartient au Parlement élu et au gouvernement.

## Des souverains célèbres
- **Henry VIII** (règne 1509-1547) : six épouses ; pour divorcer, il rompt avec le pape et crée la **Church of England** (1534). Le monarque en est toujours le chef.
- **Elizabeth I** (1558-1603) : la « reine vierge », époque de Shakespeare et de la victoire contre l'Invincible Armada espagnole (1588).
- **Victoria** (1837-1901) : 63 ans de règne, apogée de l'Empire ; elle est « impératrice des Indes ».
- **Elizabeth II** (1952-2022) : 70 ans de règne, record absolu. Elle a connu 15 Premiers ministres, de Churchill à Liz Truss.
- **Charles III** : roi depuis le 8 septembre 2022, couronné le 6 mai 2023.

## Que fait le roi aujourd'hui ?
Son rôle est surtout symbolique et cérémoniel. Il nomme officiellement le Premier ministre (le chef du parti majoritaire), signe les lois (il ne refuse jamais), ouvre chaque année le Parlement avec le **King's Speech** (écrit par le gouvernement), reçoit les chefs d'État étrangers et représente le pays. Il doit rester politiquement **neutral**. Il est aussi chef d'État d'une quinzaine de pays du Commonwealth, comme le Canada ou l'Australie.

## Pour ou contre ?
Les partisans de la monarchie (**monarchists**) y voient un symbole d'unité, de continuité et un atout touristique. Les **republicans** critiquent son coût, ses privilèges héréditaires et préféreraient un chef d'État élu. Les scandales familiaux ont parfois fragilisé son image, mais la majorité des Britanniques restent favorables à la monarchie, même si ce soutien est plus faible chez les jeunes.
"""

D_["cu_institutions_uk.html"] = """
## Une démocratie sans constitution écrite
Contrairement à la France ou aux États-Unis, le Royaume-Uni n'a pas de constitution rassemblée dans un seul texte : on parle d'**uncodified constitution**. Les règles viennent de lois importantes (Magna Carta, Bill of Rights…), de décisions de justice et de traditions appelées **conventions**. Le principe central est la **parliamentary sovereignty** : le Parlement peut faire ou défaire n'importe quelle loi.

## Le Parlement de Westminster
- La **House of Commons** : 650 **MPs** (Members of Parliament), chacun élu dans une circonscription (**constituency**). C'est la chambre la plus puissante. Les débats y sont célèbres pour leur ton vif : le gouvernement et l'opposition se font face, et un **Speaker** dirige les débats en criant « Order! ».
- La **House of Lords** : ses membres ne sont pas élus. La plupart sont nommés à vie (**life peers**) ; s'y ajoutent des évêques de l'Église d'Angleterre. Elle relit et peut retarder les lois, mais pas les bloquer définitivement.

## Le gouvernement
Après une élection, le roi nomme **Prime Minister** le chef du parti qui a la majorité aux Communes. Le Premier ministre, qui vit au **10 Downing Street**, choisit ses ministres ; les plus importants forment le **Cabinet**. Le principal parti d'opposition forme un **Shadow Cabinet**, un « gouvernement fantôme » prêt à prendre le relais.

## Un mode de scrutin particulier
Les élections générales ont lieu au moins tous les cinq ans, avec le système **first past the post** : dans chaque circonscription, le candidat arrivé en tête gagne, même sans majorité absolue. Ce système favorise les grands partis (**Conservatives** et **Labour**) et peut donner une large majorité de sièges avec moins de la moitié des voix. Les petits partis réclament donc souvent un système plus proportionnel.

## La dévolution
Depuis 1999, l'Écosse (Scottish Parliament), le pays de Galles (**Senedd**) et l'Irlande du Nord (Northern Ireland Assembly) ont leurs propres institutions pour l'éducation, la santé ou les transports. Westminster garde la défense, la diplomatie et l'essentiel de la fiscalité.
"""

D_["cu_empire.html"] = """
## La naissance d'un empire
L'expansion britannique commence à la fin du 16e siècle avec des colonies en Amérique du Nord et dans les Caraïbes. Des compagnies commerciales, comme la **East India Company**, prennent peu à peu le contrôle de territoires immenses, notamment en Inde. L'Empire repose sur la puissance de la **Royal Navy**, le commerce… et aussi sur la traite des esclaves, que le Royaume-Uni abolit en 1807 (puis l'esclavage lui-même en 1833).

## L'apogée
Au début du 20e siècle, l'Empire couvre environ un quart des terres et de la population mondiales : c'est **the empire on which the sun never sets**. Les Britanniques justifient souvent leur domination par une prétendue « mission civilisatrice ». Les colonisés, eux, subissent l'exploitation, les famines, la violence et le racisme.

## Les dominions
Les colonies de peuplement, où vivent de nombreux colons européens, obtiennent progressivement le **self-government** et deviennent des **dominions** : le Canada (1867), l'Australie (1901), la Nouvelle-Zélande (1907), l'Afrique du Sud (1910), puis l'État libre d'Irlande (1922). Après leur participation massive à la Première Guerre mondiale, le **Statute of Westminster** (1931) les rend légalement égaux au Royaume-Uni.

## La décolonisation
Après 1945, le Royaume-Uni est affaibli et les mouvements d'indépendance se multiplient. L'Inde et le Pakistan deviennent indépendants en 1947, dans la douleur de la **partition**. Suivent le Ghana (1957), le Nigeria (1960), la Jamaïque (1962), le Kenya (1963)… Certaines indépendances sont négociées, d'autres arrachées après des conflits violents, comme au Kenya avec la révolte des Mau Mau.

## Le Commonwealth et l'héritage
Le **Commonwealth of Nations** (1949) réunit aujourd'hui 56 pays libres et égaux, dont certains n'ont jamais été colonies britanniques (Mozambique, Rwanda…). L'héritage de l'Empire est partout : la langue anglaise, le cricket, le droit, mais aussi des débats douloureux sur la mémoire coloniale, les restitutions d'objets dans les musées et la place des descendants de colonisés dans la société britannique, comme la **Windrush generation**.
"""

D_["cu_brexit.html"] = """
## Une relation compliquée avec l'Europe
Le Royaume-Uni rejoint la Communauté économique européenne en 1973, avec retard : la France avait refusé deux fois sa candidature dans les années 1960. Dès 1975, un premier référendum confirme l'adhésion (67 % de oui). Mais une partie des Britanniques, notamment chez les conservateurs, se méfie de Bruxelles : on les appelle les **Eurosceptics**. Le pays refuse l'euro et l'espace Schengen.

## Le référendum de 2016
Sous la pression de son parti et de la montée du parti anti-européen UKIP, le Premier ministre **David Cameron** promet un référendum. Le 23 juin 2016, la question est simple : rester (**Remain**) ou partir (**Leave**). Le « Leave » l'emporte avec **51.9 %**.
Les arguments du Leave : reprendre le contrôle des lois (**sovereignty**), de l'immigration et de l'argent versé à l'UE. Le slogan « **Take back control** » a beaucoup marqué. Les arguments du Remain : les avantages du **single market** (marché unique), les emplois, la paix et la coopération.
Le vote révèle des fractures : l'Angleterre et le pays de Galles votent Leave, l'Écosse et l'Irlande du Nord Remain ; les jeunes, les diplômés et les grandes villes votent plutôt Remain, les plus âgés et les régions industrielles en déclin plutôt Leave.

## Trois ans et demi de crise
Theresa May négocie un accord, rejeté trois fois par les députés. Le Parlement est paralysé. **Boris Johnson** lui succède, remporte largement les élections de décembre 2019 avec le slogan « **Get Brexit done** », et le Royaume-Uni quitte l'UE le **31 janvier 2020**. Un accord commercial entre en vigueur le 1er janvier 2021.

## Le casse-tête irlandais
La frontière entre l'Irlande du Nord (Royaume-Uni) et la République d'Irlande (UE) était devenue invisible grâce à l'accord de paix de 1998. Pour éviter de rétablir une **hard border**, des contrôles ont été placés entre la Grande-Bretagne et l'Irlande du Nord, ce qui a provoqué la colère des unionistes. Le **Windsor Framework** (2023) a assoupli ce système.

## Et maintenant ?
Le Brexit a mis fin à la liberté de circulation : il faut désormais des visas pour travailler, et les échanges commerciaux sont plus compliqués. Les sondages montrent que de nombreux Britanniques regrettent aujourd'hui ce choix, mais le sujet reste très sensible et aucun grand parti ne propose de revenir dans l'UE à court terme.
"""

D_["cu_famine.html"] = """
## L'Irlande avant la famine
En 1801, l'**Act of Union** rattache l'Irlande au Royaume-Uni. La majorité de la population est catholique et pauvre ; la terre appartient surtout à de grands propriétaires protestants (**landlords**), souvent absents. Les paysans louent de minuscules parcelles et paient leur loyer en cultivant des céréales destinées à la vente. Pour se nourrir, il leur reste la **potato**, qui pousse bien sur de petites surfaces : un adulte pauvre pouvait en manger plusieurs kilos par jour.

## La catastrophe
En 1845, un champignon venu d'Amérique, le mildiou (**potato blight**), fait pourrir les pommes de terre dans les champs. La maladie revient en 1846, 1848 et 1849. L'hiver 1846-1847, très froid, est le pire : on l'appelle **Black '47**. Les gens meurent de faim (**starvation**) et surtout de maladies comme le typhus et le choléra. Les familles qui ne peuvent plus payer sont expulsées (**evictions**), leurs maisons détruites pour qu'elles ne reviennent pas.

## La réponse britannique, au cœur du débat
Le gouvernement de Robert Peel importe du maïs d'Amérique et abolit les **Corn Laws** (1846). Mais ses successeurs croient au **laissez-faire** : l'État ne doit pas perturber le marché. Les secours prennent la forme de travaux publics souvent inutiles et épuisants, puis de **soup kitchens** en 1847, rapidement arrêtées. Charles Trevelyan, haut fonctionnaire chargé de l'aide, voit même dans la famine une sorte de punition providentielle. Pendant ce temps, l'Irlande continue d'exporter de la viande et des céréales.
Les historiens débattent encore : négligence idéologique ou volonté délibérée ? Beaucoup d'Irlandais parlent d'un crime ; la plupart des historiens évoquent une gestion catastrophique, aggravée par les préjugés anti-irlandais.

## Le bilan
Environ un million de morts et plus d'un million d'émigrés en quelques années. Les **coffin ships** traversent l'Atlantique vers les États-Unis et le Canada ; beaucoup partent aussi pour Liverpool ou Glasgow. L'Irlande comptait plus de 8 millions d'habitants en 1841 ; l'île n'en a toujours pas retrouvé autant aujourd'hui.

## L'héritage
La famine a créé une immense **diaspora** : des dizaines de millions d'Américains ont des ancêtres irlandais, d'où l'importance de la St Patrick's Day aux États-Unis. Elle a aussi nourri le ressentiment contre la Grande-Bretagne et le nationalisme irlandais qui mènera à l'indépendance. En 1997, le Premier ministre Tony Blair a reconnu que Londres avait « failli » envers le peuple irlandais.
"""

D_["cu_troubles.html"] = """
## Aux origines : une île partagée
En 1921, l'Irlande est divisée : le sud devient indépendant, mais six comtés du nord-est, où les protestants sont majoritaires, restent dans le Royaume-Uni. Pendant cinquante ans, l'Irlande du Nord est dirigée par les **unionists** protestants. La minorité catholique, plutôt **nationalist** (favorable à une Irlande unie), subit des discriminations dans l'accès au logement, à l'emploi et au vote : les circonscriptions sont découpées pour favoriser les unionistes (**gerrymandering**).

## Des droits civiques à la violence
À la fin des années 1960, un mouvement pour les droits civiques, inspiré de Martin Luther King, organise des marches. Elles sont violemment réprimées. En 1969, des émeutes éclatent et l'armée britannique est déployée. Des groupes paramilitaires s'arment : côté républicain, l'**IRA** (Irish Republican Army) ; côté loyaliste, l'UVF ou l'UDA. En 1971, l'**internment** permet d'emprisonner sans procès, presque uniquement des catholiques.

## Bloody Sunday (30 janvier 1972)
À Derry, une marche pacifique contre l'internement réunit environ 15 000 personnes. Des parachutistes britanniques ouvrent le feu : 13 civils non armés sont tués, un 14e meurt plus tard. Un premier rapport blanchit l'armée. Il faut attendre 2010 et le rapport **Saville** pour reconnaître que les victimes étaient innocentes ; le Premier ministre David Cameron présente alors des excuses officielles. Bloody Sunday pousse de nombreux jeunes vers l'IRA : 1972 est l'année la plus meurtrière.

## La bataille des prisons
En 1976, Londres supprime le statut spécial des prisonniers paramilitaires : ils doivent porter l'uniforme des criminels de droit commun. Dans les **H-Blocks** de la prison du Maze, les républicains refusent : c'est le **blanket protest**, vêtus d'une simple couverture. En 1978, faute d'avancée, ils lancent le **dirty protest** : ils refusent de se laver et étalent leurs excréments sur les murs de leurs cellules. Des femmes détenues à Armagh mènent une protestation similaire.
En 1981 commence une grève de la faim (**hunger strike**). Son leader, **Bobby Sands**, est élu député pendant sa détention. Margaret Thatcher refuse toute concession. Sands meurt le 5 mai 1981 après 66 jours ; neuf autres grévistes meurent ensuite. Ces morts provoquent une émotion mondiale et poussent le mouvement républicain (Sinn Féin) vers la politique électorale.

## La paix
Plus de 3 500 personnes meurent pendant les Troubles, dont une majorité de civils, et les attentats touchent aussi l'Angleterre. Après des négociations secrètes, l'IRA proclame un cessez-le-feu en 1994. Le **Good Friday Agreement** (10 avril 1998) instaure un gouvernement partagé entre unionistes et nationalistes (**power-sharing**) et prévoit que l'Irlande du Nord restera britannique tant que sa population le souhaitera. La paix tient, mais des **peace walls** séparent encore certains quartiers de Belfast.
"""

D_["cu_vie_uk.html"] = """
## L'école
La scolarité est obligatoire de 5 à 16 ans (et l'éducation ou la formation jusqu'à 18 ans en Angleterre). On passe de la **primary school** à la **secondary school** vers 11 ans. Presque tous les élèves portent un **uniform**, avec les couleurs et le blason de l'établissement : l'idée est de gommer les différences sociales et de créer un sentiment d'appartenance. Les établissements sont souvent organisés en **houses** qui s'affrontent dans des compétitions.
À 16 ans, on passe les **GCSEs** dans de nombreuses matières ; à 18 ans, les **A-levels** dans trois ou quatre matières seulement, qui décident de l'entrée à l'université. Il existe aussi des écoles privées très chères et prestigieuses, paradoxalement appelées **public schools**, comme Eton.

## Le NHS
Créé en 1948 par le gouvernement travailliste, le **National Health Service** offre des soins gratuits au moment où on les reçoit, financés par l'impôt. On s'inscrit chez un **GP** (médecin généraliste) qui oriente vers l'hôpital. Les Britanniques y sont très attachés : lors des Jeux olympiques de Londres en 2012, la cérémonie d'ouverture lui a rendu hommage. Mais le NHS souffre de listes d'attente longues et du manque de personnel, un sujet politique majeur.

## Thé, pub et fish and chips
Le thé arrive au 17e siècle et devient la boisson nationale au 19e, grâce aux plantations de l'Empire en Inde et à Ceylan. On le boit avec du lait, à toute heure ; une **cuppa** console de tout. L'**afternoon tea**, avec scones et sandwiches, est réservé aux grandes occasions.
Le **pub** est le salon de la nation : on y discute, on regarde le football, on joue aux fléchettes ou au **pub quiz**. On commande au bar et on paie tout de suite, on ne laisse généralement pas de pourboire au comptoir, et on paie souvent des tournées (**rounds**) à tour de rôle. Le **Sunday roast** et le **fish and chips** restent des plats emblématiques, même si le curry est l'un des plats préférés du pays.

## Les petites habitudes
Faire la queue (**queuing**) est une règle sacrée. On dit **sorry** très souvent, même quand ce n'est pas sa faute. On parle volontiers de la météo pour briser la glace. Enfin, la **BBC**, créée en 1922 et financée par une redevance (**licence fee**), reste une institution : ses journaux, ses séries et ses documentaires sont regardés dans le monde entier.
"""

D_["cu_londres.html"] = """
## Une ville romaine devenue capitale mondiale
Londres est fondée par les Romains vers 50 après J.-C. sous le nom de **Londinium**, au bord de la **Thames**. Au Moyen Âge, Guillaume le Conquérant y fait construire la **Tower of London** après 1066. En 1666, le **Great Fire of London** détruit une grande partie de la ville ; l'architecte Christopher Wren reconstruit de nombreuses églises, dont la cathédrale **St Paul's**. Au 19e siècle, Londres devient la plus grande ville du monde et le cœur de l'Empire.

## Se déplacer
Le métro, **the Underground** ou **the Tube**, ouvre en 1863 : c'est le plus ancien du monde. Son plan, dessiné par Harry Beck en 1933, a inspiré les plans de métro de nombreuses villes. On paie avec une carte **Oyster** ou sa carte bancaire. Les bus rouges à impériale (**double-decker buses**) et les taxis noirs (**black cabs**) sont des symboles ; pour obtenir leur licence, les chauffeurs de black cab doivent apprendre par cœur des milliers de rues : c'est **The Knowledge**.

## Les incontournables
- **Westminster** : le Parlement et sa tour, rebaptisée Elizabeth Tower en 2012 ; **Big Ben** est le nom de la grande cloche. Juste à côté, Westminster Abbey, où sont couronnés les rois.
- **Buckingham Palace** et la relève de la garde (**Changing of the Guard**).
- La **Tower of London**, qui garde les **Crown Jewels**, et le **Tower Bridge**, souvent confondu avec le London Bridge.
- Les musées gratuits : British Museum, National Gallery, Natural History Museum, Tate Modern dans une ancienne centrale électrique.
- Les quartiers : Camden et ses marchés, Notting Hill, Covent Garden, le **West End** et ses comédies musicales, la **City**, quartier de la finance.

## Une ville-monde
Plus de 300 langues sont parlées à Londres et plus d'un tiers des habitants sont nés à l'étranger. C'est aussi une ville très chère, où le prix des logements pousse de nombreux habitants vers la périphérie. En 2012, Londres est devenue la première ville à accueillir trois fois les Jeux olympiques (1908, 1948, 2012).
"""

D_["cu_ecosse_galles.html"] = """
## L'Écosse, une nation fière de sa différence
L'Écosse a été un royaume indépendant pendant des siècles, souvent en guerre contre l'Angleterre. Ses héros sont des résistants : **William Wallace** (immortalisé par le film *Braveheart*) et **Robert the Bruce**, vainqueur à Bannockburn en 1314. En 1603, le roi d'Écosse Jacques VI hérite du trône d'Angleterre ; en 1707, l'**Act of Union** fusionne les deux parlements.
L'Écosse a pourtant gardé ses propres systèmes juridique, scolaire et religieux (l'Église presbytérienne). Ses traditions sont célèbres : le **kilt** en **tartan** (chaque clan a son motif), la cornemuse (**bagpipes**), les **Highland Games** avec le lancer de tronc, le whisky, le **haggis** (panse de mouton farcie). Le 25 janvier, la **Burns Night** célèbre le poète Robert Burns, auteur de *Auld Lang Syne*, chanté dans le monde entier au Nouvel An.

## La question de l'indépendance
En 1999, l'Écosse retrouve un parlement à Édimbourg. Le **Scottish National Party** (SNP) domine la vie politique et réclame l'indépendance. Au référendum de 2014, le « non » l'emporte avec 55 %. Mais en 2016, les Écossais votent à 62 % contre le Brexit, et beaucoup estiment avoir été entraînés hors de l'UE contre leur volonté. Le débat sur un nouveau référendum continue.

## Le pays de Galles, terre de langue et de chant
Conquis par Édouard Ier à la fin du 13e siècle, le pays de Galles est rattaché à l'Angleterre par des lois du 16e siècle. Édouard fait construire de puissants châteaux, comme ceux de Caernarfon et de Conwy. Depuis, le fils aîné du roi porte le titre de **Prince of Wales**.
Au 19e siècle, le sud du pays devient l'une des grandes régions minières du monde : le charbon gallois part depuis Cardiff. La fermeture des mines dans les années 1980 a durement frappé ces vallées.

## Le gallois, une langue qui renaît
Le **Welsh** est une langue celtique très ancienne. Longtemps méprisé, voire interdit à l'école, il connaît un renouveau : il est enseigné à tous les élèves, les panneaux sont bilingues, une chaîne de télévision (S4C) diffuse en gallois. Environ un habitant sur cinq le parle. Le pays de Galles possède le nom de lieu le plus long d'Europe : Llanfairpwllgwyngyll…
Le rugby y est une passion, tout comme le chant choral, célébré lors des **Eisteddfod**, festivals de musique et de poésie.
"""

D_["cu_revolution_industrielle.html"] = """
## Pourquoi la Grande-Bretagne ?
La révolution industrielle commence en Grande-Bretagne vers 1760 pour plusieurs raisons : des réserves importantes de **coal** (charbon) et de fer, des capitaux issus du commerce colonial et de la traite, un marché intérieur unifié, des inventeurs nombreux, et une agriculture plus productive qui libère de la main-d'œuvre : les **enclosures** chassent beaucoup de petits paysans vers les villes.

## Machines et vapeur
Tout commence dans le textile : de nouvelles machines filent et tissent le coton beaucoup plus vite. La **steam engine** de James Watt (améliorée en 1769) permet d'installer ces machines dans d'immenses usines (**mills**). Manchester devient **Cottonopolis**. Le chemin de fer suit : la première ligne publique ouvre en 1825, et en 1830 la ligne Liverpool-Manchester transporte des voyageurs grâce à la locomotive *Rocket* de George Stephenson. En quelques décennies, un réseau couvre tout le pays.

## La vie des ouvriers
Les villes industrielles grandissent sans plan : logements entassés, absence d'égouts, eau polluée. Le choléra et la tuberculose font des ravages ; l'espérance de vie dans certains quartiers de Manchester ne dépasse pas 25 ans à la naissance (à cause de la mortalité infantile). On travaille 12 à 16 heures par jour, six jours sur sept, pour des salaires très bas.
Les enfants sont employés dans les usines et les mines, parfois dès 5 ou 6 ans, car ils coûtent peu et se glissent sous les machines ou dans les galeries étroites. Les accidents sont fréquents. Le **Factory Act** de 1833 interdit le travail des moins de 9 ans dans le textile ; d'autres lois suivent, notamment en 1842 pour les mines.

## Contestations et réformes
Certains ouvriers, les **Luddites**, cassent les machines qui leur prennent leur travail (1811-1816). Les syndicats (**trade unions**) naissent malgré la répression. Les **Chartists** réclament le droit de vote pour tous les hommes dans les années 1840. Des écrivains comme **Charles Dickens** (*Oliver Twist*, *Hard Times*) dénoncent la misère et les **workhouses**, ces hospices où l'on enferme les pauvres. Karl Marx et Friedrich Engels observent Manchester et Londres pour écrire leurs analyses du capitalisme.

## Le triomphe victorien
En 1851, la **Great Exhibition**, dans le Crystal Palace, un immense palais de verre et de fer, présente au monde les inventions britanniques. Le Royaume-Uni est alors **the workshop of the world**. La révolution industrielle a transformé le paysage, la société et le climat de la planète : c'est le début de l'ère du charbon.
"""

D_["cu_suffragettes.html"] = """
## Le droit de vote, un privilège masculin
Au 19e siècle, le droit de vote s'élargit progressivement aux hommes, mais les femmes en restent exclues. Beaucoup pensent qu'elles doivent rester dans la **domestic sphere**, la maison et la famille. Pourtant, des femmes travaillent, paient des impôts, écrivent, militent.

## Les suffragists : la voie légale
Dès les années 1860, des sociétés réclament le vote des femmes. En 1897, **Millicent Fawcett** les réunit dans la NUWSS. Elles organisent des pétitions, des réunions, des marches pacifiques, et cherchent à convaincre les députés. Elles obtiennent des soutiens, mais aucune loi.

## Les suffragettes : « Deeds, not words »
En 1903, **Emmeline Pankhurst** et ses filles Christabel et Sylvia fondent la **Women's Social and Political Union** (WSPU), avec pour devise « **Deeds, not words** ». Le journal *Daily Mail* les surnomme **suffragettes** pour se moquer d'elles ; elles adoptent fièrement ce nom. Leurs couleurs : violet (dignité), blanc (pureté), vert (espoir).
Leurs méthodes deviennent de plus en plus radicales : interruptions de meetings, enchaînement aux grilles (**railings**), vitrines brisées, boîtes aux lettres incendiées, puis incendies de bâtiments vides. Emprisonnées, elles réclament le statut de prisonnières politiques et font la **hunger strike**. Le gouvernement les nourrit de force (**force-feeding**) avec des tubes, une pratique brutale qui choque l'opinion. En 1913, le **Cat and Mouse Act** permet de libérer les grévistes affaiblies puis de les réarrêter une fois rétablies.
En juin 1913, **Emily Wilding Davison** se précipite sur la piste du Derby d'Epsom et est percutée par le cheval du roi. Ses funérailles rassemblent des milliers de personnes.

## La guerre change tout
En 1914, la WSPU suspend son combat pour soutenir l'effort de guerre. Les femmes remplacent les hommes dans les usines de munitions (**munitionettes**), les transports, les hôpitaux. En 1918, le **Representation of the People Act** accorde le vote aux femmes de plus de 30 ans remplissant certaines conditions de propriété, et à tous les hommes de plus de 21 ans. En 1919, **Nancy Astor** est la première femme à siéger aux Communes. Il faut attendre 1928 pour l'égalité complète, à 21 ans.

## Un héritage discuté
Les historiens débattent encore : la violence des suffragettes a-t-elle accéléré ou retardé le vote des femmes ? Une chose est sûre : leur combat a fait de l'égalité politique un sujet impossible à ignorer. Une statue de Millicent Fawcett se dresse depuis 2018 devant le Parlement, la première statue de femme sur Parliament Square.
"""

D_["cu_blitz.html"] = """
## Seule face à l'Allemagne
Le 3 septembre 1939, le Royaume-Uni déclare la guerre à l'Allemagne nazie après l'invasion de la Pologne. Au printemps 1940, l'armée allemande envahit la Belgique, les Pays-Bas et la France. Le 10 mai 1940, **Winston Churchill** devient Premier ministre. Fin mai, plus de 300 000 soldats britanniques et alliés sont évacués des plages de **Dunkirk** par des navires de guerre et des centaines de petits bateaux civils. En juin, la France signe l'armistice : le Royaume-Uni et son Empire sont seuls.

## Les discours de Churchill
Churchill galvanise la population par des discours restés célèbres. Il promet « **blood, toil, tears and sweat** » (du sang, de la peine, des larmes et de la sueur), affirme que les Britanniques se battront « **on the beaches** » et ne se rendront jamais, et appelle à faire de cette période leur « **finest hour** ».

## La bataille d'Angleterre
À l'été 1940, la Luftwaffe tente de détruire la **Royal Air Force** pour préparer une invasion. Les pilotes de la RAF, aidés par le radar et par des aviateurs polonais, tchèques ou canadiens, résistent. Churchill leur rend hommage : jamais autant de personnes n'avaient dû autant à si peu (« **the Few** »). Hitler renonce à l'invasion.

## Le Blitz
Le Blitz (du mot allemand *Blitzkrieg*, guerre éclair) désigne les bombardements massifs de septembre 1940 à mai 1941. Londres est bombardée 57 nuits de suite ; Coventry, Liverpool, Birmingham, Glasgow ou Plymouth sont aussi touchées. Plus de 40 000 civils sont tués. Les familles se réfugient dans des abris (**Anderson shelters** dans les jardins) ou dans les stations de métro. Les fenêtres doivent être occultées (**blackout**). Le roi George VI et la reine restent à Londres malgré les bombes tombées sur Buckingham Palace.
Dès 1939, l'opération **Pied Piper** a évacué des centaines de milliers d'enfants vers la campagne, une étiquette autour du cou : une expérience souvent douloureuse.

## Le mythe du « Blitz spirit »
On célèbre aujourd'hui le **Blitz spirit**, le courage tranquille des Britanniques sous les bombes. La réalité était plus nuancée : peur, pillages, inégalités entre quartiers riches et pauvres. Mais cette période reste un pilier de l'identité nationale, souvent invoqué dans les moments de crise. L'affiche « **Keep Calm and Carry On** », imprimée en 1939 mais presque jamais diffusée, a été redécouverte en 2000 et est devenue un objet culte. La guerre en Europe se termine le 8 mai 1945 : **VE Day**.
"""

D_["cu_thatcher.html"] = """
## Un pays en crise
Dans les années 1970, le Royaume-Uni est surnommé « l'homme malade de l'Europe » : inflation élevée, industries vieillissantes, grèves à répétition. L'hiver 1978-1979, appelé **Winter of Discontent**, voit les poubelles s'accumuler dans les rues. En mai 1979, les conservateurs gagnent les élections : **Margaret Thatcher**, fille d'épicier, devient la première femme Premier ministre du pays.

## Le thatchérisme
Thatcher s'inspire d'économistes libéraux : il faut réduire le rôle de l'État, lutter contre l'inflation, laisser faire le marché (**free market**). Concrètement :
- les grandes entreprises publiques sont privatisées (**privatisation**) : British Telecom, British Gas, British Airways, l'électricité, l'eau ;
- le **Right to Buy** permet aux locataires de logements sociaux (**council houses**) d'acheter leur logement à prix réduit ;
- les impôts sur les plus hauts revenus baissent ;
- le pouvoir des **trade unions** est réduit par plusieurs lois ;
- la City de Londres est dérégulée en 1986 (le **Big Bang**).
Le chômage dépasse trois millions au début des années 1980, notamment dans les régions industrielles.

## La « Dame de fer »
Le surnom **Iron Lady** lui est donné par un journal soviétique en 1976 ; elle l'adopte avec plaisir. En 1982, l'Argentine envahit les **Falkland Islands** (les Malouines), dans l'Atlantique Sud. Thatcher envoie une flotte ; la guerre dure 74 jours et fait environ 900 morts. La victoire fait remonter sa popularité. Elle s'allie étroitement avec le président américain Ronald Reagan contre l'URSS, et survit à un attentat de l'IRA à Brighton en 1984.

## La grève des mineurs (1984-1985)
Le gouvernement annonce la fermeture de nombreux puits de charbon déficitaires. Le syndicat des mineurs, dirigé par **Arthur Scargill**, lance une grève d'un an. Les affrontements avec la police sont violents, comme à Orgreave en 1984. Les mineurs, affamés, finissent par reprendre le travail sans rien obtenir. Des dizaines de villes minières du nord de l'Angleterre, du pays de Galles et d'Écosse perdent leur principale source d'emplois.

## La chute et l'héritage
En 1990, un nouvel impôt local identique pour tous, la **poll tax**, provoque des émeutes. Divisé, notamment sur l'Europe, son propre parti la pousse à démissionner en novembre 1990. Sa mort, en 2013, a montré à quel point elle divise encore : hommages officiels d'un côté, fêtes dans certaines anciennes villes minières de l'autre. Pour les uns, elle a modernisé l'économie et rendu sa fierté au pays ; pour les autres, elle a détruit des communautés entières et creusé les inégalités.
"""

D_["cu_multiculturel.html"] = """
## Des migrations anciennes
La Grande-Bretagne a toujours été une terre de migrations : Romains, Anglo-Saxons, Vikings, Normands, réfugiés protestants français (huguenots), Irlandais, Juifs d'Europe de l'Est… Des communautés noires existent à Londres depuis le 16e siècle, et des marins indiens (**lascars**) s'installent dans les ports dès le 18e siècle.

## Après 1945 : les enfants de l'Empire
Pour reconstruire le pays, le Royaume-Uni fait appel aux habitants du Commonwealth, qui ont alors la nationalité britannique. En 1948, l'**Empire Windrush** amène environ 500 passagers des Caraïbes. Dans les années 1950-1970 arrivent des travailleurs d'Inde, du Pakistan, du Bangladesh, puis des Indiens chassés d'Ouganda et du Kenya. Ils travaillent dans le NHS, les transports, le textile, les fonderies.
L'accueil est souvent hostile : panneaux « **No Irish, no Blacks, no dogs** » sur certaines pensions, violences, discriminations à l'embauche. En 1958, des émeutes racistes visent les habitants caribéens de Notting Hill. En 1968, le député Enoch Powell prononce un discours alarmiste contre l'immigration qui marque durablement le débat. Le **Race Relations Act** de 1965, renforcé en 1968 et 1976, interdit les discriminations.

## Le carnaval de Notting Hill
En réponse aux émeutes, la militante trinidadienne **Claudia Jones** organise dès 1959 un carnaval caribéen en salle. Il descend dans la rue dans les années 1960 et devient le **Notting Hill Carnival**, qui attire chaque mois d'août plus d'un million de personnes : steel bands, costumes, sound systems, cuisine jamaïcaine.

## Une culture transformée
Le curry est devenu un plat national (le **chicken tikka masala** aurait même été inventé au Royaume-Uni). La musique britannique doit beaucoup aux artistes noirs et asiatiques, du reggae londonien au grime. Les écrivains Zadie Smith et Salman Rushdie, de nombreux sportifs de l'équipe nationale de football, ou des personnalités politiques reflètent cette diversité. En 2021, près d'une personne sur cinq en Angleterre et au pays de Galles se déclarait non blanche.

## Des débats toujours vifs
Le **Windrush scandal** (2018) révèle que des personnes arrivées légalement enfant, il y a des décennies, ont perdu leur emploi, leur logement, ont été détenues ou expulsées faute de papiers, à cause d'une politique dite d'« environnement hostile ». Le gouvernement a dû présenter des excuses et créer un fonds d'indemnisation. L'immigration reste un sujet central des campagnes électorales, entre ceux qui veulent la réduire et ceux qui défendent une société ouverte. Des émeutes visant des hôtels de demandeurs d'asile en 2024 ont montré que les tensions restent fortes.
"""

D_["cu_paques_1916.html"] = """
## Le contexte : le Home Rule en suspens
Au début du 20e siècle, la majorité des Irlandais veut le **Home Rule**, une autonomie dans le cadre du Royaume-Uni. Une loi est votée en 1914, mais suspendue à cause de la Première Guerre mondiale. Les unionistes protestants de l'Ulster, eux, s'arment pour refuser toute autonomie. Une minorité de républicains, membres de l'IRB et de la milice des **Irish Volunteers**, pense que seule une insurrection armée apportera l'indépendance. Leur logique : « England's difficulty is Ireland's opportunity ».

## Six jours à Dublin
Le lundi de Pâques, 24 avril 1916, environ 1 500 insurgés occupent des bâtiments clés de Dublin, dont la Grande Poste (**General Post Office**, GPO). **Patrick Pearse** lit devant le bâtiment la **Proclamation of the Irish Republic**. Parmi les chefs figurent aussi James Connolly, syndicaliste et socialiste, et des femmes comme Constance Markievicz. L'armée britannique riposte avec l'artillerie ; le centre-ville est en ruines. Le 29 avril, les insurgés se rendent. Environ 450 personnes sont mortes, dont de nombreux civils.

## Les exécutions retournent l'opinion
Au départ, beaucoup de Dublinois sont hostiles aux rebelles, d'autant que des milliers d'Irlandais se battent alors dans l'armée britannique. Mais en mai 1916, les autorités font fusiller quinze chefs de l'insurrection ; James Connolly, blessé, est exécuté attaché sur une chaise. Un seizième, Roger Casement, est pendu en août. Ces exécutions transforment les insurgés en martyrs. Le poète **W. B. Yeats** écrit que tout a changé : « *a terrible beauty is born* ».

## De la guerre d'indépendance à la partition
Aux élections de 1918, le parti indépendantiste **Sinn Féin** remporte la majorité des sièges irlandais, refuse de siéger à Londres et proclame un parlement à Dublin, le **Dáil Éireann**. De 1919 à 1921, l'IRA de **Michael Collins** mène une guérilla contre les forces britanniques, dont les unités auxiliaires (les « Black and Tans ») commettent de nombreuses exactions.
Le **Anglo-Irish Treaty** de décembre 1921 crée l'**Irish Free State**, un dominion autonome au sein de l'Empire, tandis que six comtés du nord restent britanniques : c'est la **partition**.

## La guerre civile et la République
Le traité divise les nationalistes : Collins le défend comme une étape vers la liberté ; Éamon de Valera et les anti-traité le rejettent, notamment à cause du serment au roi. La guerre civile (1922-1923) fait des milliers de morts ; Collins est tué dans une embuscade en août 1922. L'Irlande devient pleinement une république en 1949. Chaque année, Pâques reste un moment de commémoration, et le centenaire de 2016 a donné lieu à de grandes cérémonies.
"""

D_["cu_irlande_auj.html"] = """
## Une jeune république
Indépendante depuis 1922 et république depuis 1949, l'Irlande (**Éire** en irlandais) compte un peu plus de 5 millions d'habitants. Son chef d'État est un président élu (rôle surtout symbolique) ; le chef du gouvernement s'appelle le **Taoiseach**. Le pays est membre de l'Union européenne depuis 1973 et utilise l'euro. Il est resté neutre pendant la Seconde Guerre mondiale et n'est pas membre de l'OTAN.

## De l'émigration au « tigre celtique »
Pendant plus d'un siècle après la famine, l'Irlande est un pays pauvre et rural que les jeunes quittent en masse. À partir des années 1990, tout change : grâce aux fonds européens, à une main-d'œuvre jeune et anglophone, et à un impôt sur les sociétés très bas, les investissements affluent. C'est le **Celtic Tiger**. Google, Apple, Meta ou Pfizer installent leur siège européen en Irlande. En 2008, l'éclatement de la bulle immobilière provoque une crise sévère et un plan d'aide européen, mais l'économie repart ensuite. Aujourd'hui, la crise du logement et le coût de la vie sont les grands sujets politiques.

## Une société profondément transformée
Pendant des décennies, l'Église catholique exerce une influence immense sur l'école, les hôpitaux et la morale. Les révélations sur les abus commis par des membres du clergé et dans certaines institutions, à partir des années 1990, provoquent une crise de confiance. La société se sécularise rapidement : en 2015, l'Irlande devient le premier pays au monde à légaliser le **same-sex marriage** par référendum ; en 2018, un autre référendum légalise l'avortement. Ces votes ont été portés notamment par les jeunes.

## La langue irlandaise
L'**Irish** (ou gaélique) est la première langue officielle, l'anglais la seconde. Tous les élèves l'étudient, les panneaux sont bilingues, une chaîne de télévision (TG4) diffuse en irlandais. Mais seule une petite minorité la parle au quotidien, surtout dans les régions de la **Gaeltacht**, sur la côte ouest. Des mots irlandais sont passés dans l'anglais local : **craic** (l'ambiance, le fun), **sláinte** (santé, pour trinquer).

## Culture et passions
L'Irlande a donné au monde de grands écrivains : James Joyce, et quatre prix Nobel de littérature (Yeats, Shaw, Beckett, Seamus Heaney), des musiciens (U2, les Cranberries, Hozier), et une tradition musicale vivante dans les pubs (**sessions**). Les sports gaéliques, le **hurling** et le **Gaelic football**, gérés par la GAA, sont des passions locales, tout comme le rugby. Et le 17 mars, la **St Patrick's Day** est célébrée de Dublin à New York.
"""
