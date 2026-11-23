import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
D_ = {}

D_["cu_usa.html"] = """
## Un pays-continent
Les États-Unis sont le troisième ou quatrième plus grand pays du monde (selon les modes de calcul) et le troisième plus peuplé, avec plus de 330 millions d'habitants. On y trouve tous les paysages : les gratte-ciel de New York, les plaines du **Midwest**, les Rocheuses, les déserts du **Southwest**, les plages de Californie et de Floride, les glaciers de l'Alaska et les volcans d'Hawaï. Le pays compte six fuseaux horaires.

## Une république fédérale
Les **50 states** ont chacun leur gouverneur, leur parlement, leurs lois : la peine de mort, l'âge du permis de conduire ou les taxes varient d'un État à l'autre. Le gouvernement **federal**, à Washington, s'occupe de la défense, de la monnaie, de la diplomatie. La capitale, **Washington, D.C.** (District of Columbia), n'appartient à aucun État ; elle a été construite exprès à la fin du 18e siècle.

## Une nation née d'une révolution
Les 13 colonies britanniques proclament leur indépendance le **4 July 1776**. Le drapeau, **the Stars and Stripes**, garde la mémoire de cette naissance : 13 bandes pour les colonies fondatrices, et une étoile par État (le drapeau a changé 27 fois au fil des ajouts d'États ; le dernier modèle date de 1960, après l'entrée d'Hawaï). L'hymne national, *The Star-Spangled Banner*, évoque un drapeau resté debout pendant une bataille contre les Britanniques en 1814.

## Une nation d'immigrants
Avant les Européens vivaient des millions d'Amérindiens. Puis sont venus les colons européens, les Africains réduits en esclavage, et des vagues d'immigrants du monde entier. Aujourd'hui, environ un Américain sur cinq est d'origine hispanique, et l'espagnol est la deuxième langue du pays. Il n'existe pas de langue officielle inscrite dans la Constitution, même si l'anglais domine.

## Symboles et valeurs
L'aigle à tête blanche (**bald eagle**), la statue de la Liberté, l'Oncle Sam, la devise **In God We Trust** inscrite sur les billets… Les Américains sont attachés à la liberté individuelle, à la religion (bien plus qu'en Europe), à l'esprit d'entreprise et au **American Dream**. Le patriotisme est très visible : drapeaux devant les maisons, serment au drapeau à l'école (**Pledge of Allegiance**), hymne avant les matchs.
"""

D_["cu_institutions_us.html"] = """
## La Constitution de 1787
Après l'indépendance, les 13 États forment d'abord une confédération très faible. En 1787, des délégués réunis à Philadelphie — les **Founding Fathers**, dont George Washington, James Madison et Benjamin Franklin — rédigent une **Constitution**. Courte (7 articles), elle est toujours en vigueur ; on l'a modifiée par 27 **amendments**. Les dix premiers, adoptés en 1791, forment le **Bill of Rights** : liberté d'expression, de religion et de la presse (1er), droit de porter des armes (2e), droit à un procès équitable, etc.

## La séparation des pouvoirs
Inspirés de Montesquieu, les Pères fondateurs craignent la tyrannie. Ils divisent le pouvoir en trois branches qui se surveillent mutuellement : ce sont les **checks and balances**.
- **Legislative branch** : le **Congress**, avec le **Senate** (100 sénateurs, deux par État, élus pour 6 ans) et la **House of Representatives** (435 représentants, répartis selon la population, élus pour 2 ans). Le Congrès vote les lois et le budget, et peut destituer le président par la procédure d'**impeachment**.
- **Executive branch** : le **President**, élu pour 4 ans, deux mandats maximum depuis le 22e amendement (1951). Il dirige l'administration et l'armée, nomme les ministres et les juges, et peut opposer son **veto** aux lois.
- **Judicial branch** : la **Supreme Court**, 9 juges nommés à vie par le président avec l'accord du Sénat. Elle vérifie que les lois respectent la Constitution.

## La Cour suprême, arbitre de la société
Ses décisions ont changé l'histoire : fin de la ségrégation scolaire (*Brown v. Board of Education*, 1954), droit à l'avortement (*Roe v. Wade*, 1973, annulé en 2022 par *Dobbs*), mariage homosexuel dans tout le pays (2015), droit individuel au port d'armes (2008). Comme les juges sont nommés à vie, chaque nomination est un enjeu politique majeur.

## Le fédéralisme
Les États gardent des pouvoirs importants : éducation, police, droit pénal, organisation des élections. C'est pourquoi les lois sur la peine de mort, l'avortement, les armes ou la marijuana varient d'un État à l'autre.

## Deux grands partis
Le système électoral favorise deux partis. Les **Democrats** (symbole : l'âne) sont plutôt favorables à l'intervention de l'État, à la protection sociale et à l'environnement. Les **Republicans** (l'éléphant, surnommés le **GOP**, Grand Old Party) défendent plutôt la baisse des impôts, un État limité et des valeurs traditionnelles. La société américaine est aujourd'hui très polarisée entre ces deux camps.
"""

D_["cu_manifest_destiny.html"] = """
## Une jeune nation qui regarde vers l'ouest
En 1783, les États-Unis s'arrêtent au Mississippi. En 1803, Thomas Jefferson achète à Napoléon l'immense **Louisiana** pour 15 millions de dollars : la superficie du pays double. Jefferson envoie **Lewis and Clark** explorer ce territoire jusqu'au Pacifique (1804-1806), guidés en partie par Sacagawea, une jeune femme shoshone.

## Une idée : la destinée manifeste
En 1845, le journaliste **John O'Sullivan** affirme que les États-Unis ont pour « destinée manifeste » de s'étendre sur tout le continent, une mission confiée par la Providence pour répandre la démocratie. Cette idée, mêlant religion, nationalisme et sentiment de supériorité, sert à justifier les conquêtes. Le tableau *American Progress* de John Gast (1872) la met en image : une femme géante, symbole du progrès, avance vers l'ouest avec un livre et un fil télégraphique, suivie des pionniers et du train, tandis que les Amérindiens et les bisons fuient dans l'ombre.

## La conquête
- 1845 : annexion du Texas, devenu indépendant du Mexique en 1836 (bataille de l'Alamo).
- 1846 : accord avec le Royaume-Uni sur l'Oregon.
- 1846-1848 : guerre contre le Mexique ; par le traité de Guadalupe Hidalgo, le Mexique perd environ la moitié de son territoire (Californie, Nevada, Utah, Arizona…).
- 1848-1849 : la ruée vers l'or (**Gold Rush**) attire 300 000 personnes en Californie.
- 1862 : le **Homestead Act** donne 160 acres de terre à qui la cultive pendant cinq ans.
- 1869 : achèvement du premier chemin de fer transcontinental, construit en grande partie par des ouvriers chinois et irlandais.

## Le prix payé par les Amérindiens
Pour les nations amérindiennes, c'est une tragédie. L'**Indian Removal Act** (1830), voulu par le président Andrew Jackson, force les nations du Sud-Est à partir à l'ouest du Mississippi. Lors de la **Trail of Tears** (1838-1839), des milliers de Cherokees meurent de froid, de faim et de maladie. Plus tard, l'extermination presque totale des bisons prive les peuples des Plaines de leur ressource vitale. Les guerres se multiplient : les Lakotas et les Cheyennes battent l'armée de Custer à **Little Bighorn** (1876), mais finissent vaincus. En 1890, l'armée massacre environ 250 à 300 Lakotas, dont beaucoup de femmes et d'enfants, à **Wounded Knee**. La même année, le recensement déclare la **frontier** fermée.

## Un mythe fondateur… et contesté
L'Ouest a nourri la culture américaine : westerns, cow-boys, esprit pionnier, liberté et individualisme. L'historien Frederick Jackson Turner y voyait la source de la démocratie américaine. Aujourd'hui, beaucoup d'historiens insistent aussi sur la violence de cette conquête, la dépossession des Amérindiens et des Mexicains, et la vision raciste qui l'accompagnait.
"""

D_["cu_red_scare.html"] = """
## La première peur rouge (1919-1920)
Après la révolution russe de 1917, une vague de grèves et quelques attentats anarchistes font craindre une révolution aux États-Unis. Le ministre de la Justice **A. Mitchell Palmer** organise des rafles (**Palmer Raids**) : des milliers d'arrestations, souvent sans preuve, et des centaines d'expulsions d'étrangers, comme la militante Emma Goldman. Les immigrés italiens **Sacco et Vanzetti**, anarchistes, sont exécutés en 1927 au terme d'un procès très contesté.

## La guerre froide et la seconde peur rouge
Après 1945, l'URSS devient l'ennemi. La Chine devient communiste en 1949, l'URSS teste sa bombe atomique la même année, la guerre de Corée éclate en 1950. Des affaires d'espionnage réelles renforcent la peur : Ethel et Julius **Rosenberg** sont exécutés en 1953 pour avoir transmis des secrets atomiques. Le président Truman impose dès 1947 des enquêtes de loyauté aux fonctionnaires.

## Hollywood sur le banc des accusés
La commission de la Chambre des représentants **HUAC** (House Un-American Activities Committee) convoque des artistes. La question rituelle : « *Are you now or have you ever been a member of the Communist Party?* ». On demande aussi de dénoncer des collègues (**to name names**). En 1947, dix scénaristes et réalisateurs, les **Hollywood Ten**, refusent de répondre au nom de la liberté d'expression : ils sont condamnés à la prison. Des centaines d'artistes sont mis sur une **blacklist** et ne trouvent plus de travail ; certains écrivent sous pseudonyme, d'autres s'exilent, comme Charlie Chaplin qui quitte les États-Unis en 1952.

## Le maccarthysme
En février 1950, le sénateur républicain **Joseph McCarthy** affirme détenir une liste de communistes infiltrés au Département d'État. Il ne prouvera jamais ses accusations mais devient extrêmement puissant. Des milliers de personnes perdent leur emploi pour leurs opinions, leurs fréquentations ou leur homosexualité (la « **Lavender Scare** »). Le mot **McCarthyism** désigne aujourd'hui toute accusation sans preuve et toute chasse aux opinions.

## La chute
En 1954, McCarthy s'attaque à l'armée. Les auditions sont retransmises à la télévision : des millions d'Américains découvrent ses méthodes brutales. L'avocat de l'armée, Joseph Welch, lui lance une phrase restée célèbre lui demandant s'il n'a donc aucun sens de la décence. Le journaliste Edward R. Murrow le critique aussi à la télévision. En décembre 1954, le Sénat le condamne officiellement ; il meurt en 1957.

## Une œuvre-clé : The Crucible
En 1953, **Arthur Miller** publie *The Crucible* (*Les Sorcières de Salem*). La pièce raconte les procès en sorcellerie de Salem en 1692, mais tout le monde y voit une allégorie du maccarthysme : une **witch hunt** où la peur fait condamner des innocents. Miller sera lui-même convoqué par la HUAC en 1956 et refusera de dénoncer qui que ce soit.
"""

D_["cu_watergate.html"] = """
## Un cambriolage raté
Dans la nuit du 17 juin 1972, cinq hommes sont arrêtés dans les bureaux du Parti démocrate, dans l'immeuble du **Watergate** à Washington. Ils portent des micros et des appareils photo. On découvre vite qu'ils sont liés au comité de réélection du président républicain **Richard Nixon** (le CRP, surnommé CREEP). La Maison-Blanche parle d'un « cambriolage de troisième ordre ». En novembre 1972, Nixon est réélu triomphalement, en remportant 49 États sur 50.

## Le rôle de la presse
Deux jeunes journalistes du *Washington Post*, **Bob Woodward** et **Carl Bernstein**, enquêtent. Une source mystérieuse, surnommée **Deep Throat**, les guide en leur conseillant de suivre l'argent (« follow the money »). Ils montrent que des fonds de la campagne ont financé des opérations illégales d'espionnage et de sabotage contre les démocrates. On n'apprendra qu'en 2005 que Deep Throat était **Mark Felt**, numéro deux du FBI. Leur histoire a inspiré le film *All the President's Men* (1976).

## Les bandes magnétiques
En 1973, une commission du Sénat mène des auditions télévisées suivies par des millions d'Américains. Un ancien conseiller, John Dean, accuse le président d'avoir participé à l'étouffement de l'affaire (**cover-up**). Puis un collaborateur révèle que Nixon enregistrait secrètement toutes les conversations de son bureau. Le procureur spécial, Archibald Cox, réclame les bandes (**tapes**). Le 20 octobre 1973, Nixon ordonne son renvoi ; le ministre de la Justice et son adjoint démissionnent plutôt que d'obéir : c'est le **Saturday Night Massacre**. En novembre, Nixon déclare à la télévision : « *I am not a crook* ».

## La chute
Le 24 juillet 1974, la Cour suprême ordonne à l'unanimité la remise des bandes. L'une d'elles, la **smoking gun**, prouve que, six jours après le cambriolage, Nixon a demandé à la CIA de bloquer l'enquête du FBI. La commission judiciaire de la Chambre vote des articles d'**impeachment**. Ayant perdu le soutien de son propre parti, Nixon démissionne le 9 août 1974 : c'est le seul président américain à l'avoir fait. **Gerald Ford** lui succède et, un mois plus tard, lui accorde une grâce présidentielle (**pardon**), une décision qui lui coûtera probablement l'élection de 1976.

## L'héritage
Le Watergate a montré la force des contre-pouvoirs : presse libre, justice indépendante, Congrès. Il a aussi installé une méfiance durable envers les dirigeants. Des lois ont été adoptées sur le financement des campagnes. Et le suffixe **-gate** sert désormais à nommer les scandales dans le monde entier.
"""

D_["cu_televangelisme.html"] = """
## Une nation très religieuse
Les États-Unis séparent l'Église et l'État depuis le 1er amendement, mais la religion y tient une place bien plus importante qu'en Europe : beaucoup d'Américains prient chaque jour et vont régulièrement à l'église. Les protestants **evangelicals**, qui mettent l'accent sur la conversion personnelle (être **born again**), la Bible et l'évangélisation, représentent environ un quart de la population.

## De la radio à la télévision
Dès les années 1920, des prédicateurs utilisent la radio pour toucher des millions d'auditeurs, comme Aimee Semple McPherson à Los Angeles. Après 1945, la télévision prend le relais. **Billy Graham** organise des **crusades** dans des stades remplis, diffusées sur les grandes chaînes. Respecté au-delà des croyants, il devient le conseiller spirituel de nombreux présidents.

## L'âge d'or des télévangélistes
Dans les années 1960-1980, certains créent leurs propres empires médiatiques. **Oral Roberts** prêche la guérison miraculeuse et développe la **prosperity gospel** : Dieu récompenserait par la richesse ceux qui donnent généreusement (l'idée du « seed faith »). **Pat Robertson** fonde la chaîne CBN et l'émission *The 700 Club* ; il se présente même à la primaire républicaine de 1988. **Jim et Tammy Faye Bakker** animent le *PTL Club* et construisent un parc d'attractions chrétien, Heritage USA.

## Religion et politique
En 1979, **Jerry Falwell** fonde la **Moral Majority**, qui mobilise les évangéliques contre l'avortement, pour la prière à l'école et les « valeurs familiales ». Ce mouvement, la **Religious Right**, aide Ronald Reagan à gagner en 1980 et devient un pilier du Parti républicain. Le vote évangélique blanc reste aujourd'hui un élément clé des élections américaines.

## Les scandales
En 1987, Jim Bakker est rattrapé par un scandale sexuel puis financier : il est condamné en 1989 pour avoir détourné des millions de dollars donnés par ses fidèles. En 1988, **Jimmy Swaggart**, qui avait dénoncé Bakker, avoue à son tour ses fautes en larmes devant les caméras. Ces affaires font chuter les dons et la crédibilité du télévangélisme.

## Aujourd'hui
Le phénomène continue sous d'autres formes : des **megachurches** de plusieurs dizaines de milliers de fidèles, comme celle de Joel Osteen à Houston, des cultes diffusés en streaming, des prédicateurs influenceurs sur les réseaux sociaux. Leurs partisans y voient une source d'espoir, de communauté et de foi ; leurs critiques dénoncent l'enrichissement personnel (jets privés, exonérations fiscales), la manipulation de personnes fragiles et le mélange entre religion et politique.
"""

D_["cu_armes_usa.html"] = """
## Le deuxième amendement
Adopté en 1791, le **Second Amendment** dit qu'une milice bien organisée étant nécessaire à la sécurité d'un État libre, le droit du peuple de détenir et de porter des armes ne sera pas transgressé. À l'époque, le pays n'a presque pas d'armée permanente et se méfie d'un pouvoir central tyrannique. Depuis, deux lectures s'opposent : un droit **individual** de chaque citoyen, ou un droit **collective** lié aux milices. En 2008 (*District of Columbia v. Heller*), la Cour suprême tranche en faveur du droit individuel à posséder une arme chez soi pour se défendre ; elle l'étend en 2022 au port d'arme hors du domicile.

## Une culture des armes
Il y a plus d'armes à feu que d'habitants aux États-Unis. Pour beaucoup d'Américains, surtout dans les zones rurales et le Sud, l'arme fait partie de l'identité : chasse, tir sportif, tradition familiale, et surtout **self-defence**. La **National Rifle Association** (NRA), fondée en 1871, est devenue un **lobby** très puissant, qui finance des campagnes électorales et s'oppose à la plupart des restrictions.

## Les tueries de masse
Les **mass shootings** frappent régulièrement le pays, y compris les écoles :
- **Columbine** (Colorado, 1999) : deux lycéens tuent 13 personnes. L'événement marque une génération.
- **Sandy Hook** (Connecticut, 2012) : 20 enfants de 6-7 ans et 6 adultes tués dans une école primaire. Aucune grande loi fédérale ne suit.
- **Parkland** (Floride, 2018) : 17 morts. Les lycéens survivants lancent le mouvement **March for Our Lives**, qui réunit des centaines de milliers de jeunes à Washington le 24 mars 2018.
- **Uvalde** (Texas, 2022) : 19 enfants et 2 enseignantes tués. Le Congrès adopte ensuite le **Bipartisan Safer Communities Act**, première loi fédérale importante depuis près de trente ans.
Depuis 2020, selon les statistiques de santé publique, les armes à feu sont la première cause de mortalité des enfants et adolescents américains (accidents, suicides et homicides confondus). Les élèves s'entraînent à se cacher lors d'exercices de confinement (**lockdown drills**).

## Le débat
- Les partisans du **gun control** veulent des vérifications d'antécédents pour tous les achats (**universal background checks**), l'interdiction des fusils d'assaut (comme entre 1994 et 2004), des « **red flag laws** » permettant de retirer temporairement les armes d'une personne jugée dangereuse, un âge minimum relevé.
- Les défenseurs des **gun rights** répondent que le droit est constitutionnel, que les criminels ne respectent pas les lois, que le problème vient de la santé mentale, et que des citoyens armés peuvent arrêter un tireur ; certains proposent même d'armer les enseignants.
Les lois varient beaucoup selon les États : très strictes en Californie ou à New York, très permissives au Texas ou en Floride.
"""

D_["cu_pilgrims.html"] = """
## Les premières colonies anglaises
Les Espagnols et les Français explorent l'Amérique du Nord avant les Anglais. La première colonie anglaise permanente est **Jamestown**, en Virginie, fondée en 1607 par une compagnie commerciale. Les débuts sont terribles (famine, conflits avec les Powhatans), mais le tabac fait sa fortune. En 1619 y arrivent les premiers Africains réduits en esclavage.

## Le Mayflower
En 1620, le **Mayflower** emmène 102 passagers, dont des **Pilgrims** : des protestants puritains qui veulent quitter l'Église d'Angleterre et pratiquer leur foi librement. Avant de débarquer, les hommes signent le **Mayflower Compact**, un accord pour se gouverner eux-mêmes, souvent vu comme un premier pas vers la démocratie américaine. Ils fondent **Plymouth**, dans l'actuel Massachusetts. La moitié meurt pendant le premier hiver.

## Le premier Thanksgiving
Les Wampanoag, et notamment **Squanto** (Tisquantum), qui parle anglais après avoir été capturé et emmené en Europe, apprennent aux colons à cultiver le maïs et à pêcher. À l'automne 1621, colons et Wampanoag partagent un repas de récolte. Ce moment est devenu le mythe fondateur de **Thanksgiving**, fêté le quatrième jeudi de novembre avec la dinde. Pour de nombreux Amérindiens, c'est pourtant un jour de deuil : l'arrivée des colons a conduit à la perte de leurs terres et à des guerres meurtrières.

## Treize colonies très différentes
Au 18e siècle, treize colonies s'étendent le long de la côte Atlantique : la Nouvelle-Angleterre puritaine et commerçante au nord, les colonies du centre plus diverses (New York, Pennsylvanie fondée par les quakers), et le Sud des grandes plantations de tabac, de riz puis de coton, fondées sur l'esclavage.

## Vers l'indépendance
Après la guerre de Sept Ans contre la France (1756-1763), Londres veut faire payer les colons par de nouveaux impôts (Stamp Act, taxe sur le thé…). Les colons protestent : « **No taxation without representation** ». En 1770, des soldats britanniques tuent cinq personnes à Boston (le « Boston Massacre »). En décembre 1773, des colons déguisés en Amérindiens jettent des caisses de thé dans le port : c'est la **Boston Tea Party**. La guerre éclate en 1775.
Le **4 juillet 1776**, le Congrès adopte la **Declaration of Independence**, rédigée surtout par Thomas Jefferson. Elle affirme que tous les hommes sont créés égaux et ont droit à « la vie, la liberté et la recherche du bonheur » — alors que Jefferson lui-même possédait des esclaves. Avec l'aide de la France (La Fayette), les Américains l'emportent à Yorktown en 1781. La paix est signée en 1783, et **George Washington** devient le premier président en 1789.
"""

D_["cu_esclavage.html"] = """
## La traite atlantique
Du 16e au 19e siècle, environ 12 millions d'Africains sont arrachés à leur continent et transportés vers les Amériques dans des conditions effroyables (le **Middle Passage**) ; près de deux millions meurent pendant la traversée. Une petite partie arrive dans les futurs États-Unis, mais la population asservie y augmente rapidement : près de 4 millions de personnes sont esclaves en 1860.

## La vie sous l'esclavage
Dans le Sud, les esclaves travaillent dans les plantations de tabac, de riz, de sucre et surtout de coton, devenu « roi » après l'invention de l'égreneuse en 1793. Ils n'ont aucun droit : les familles sont séparées lors des ventes, il est interdit de leur apprendre à lire, les châtiments corporels sont courants. Ils résistent pourtant : ralentissement du travail, préservation de leur culture (les **spirituals**), fuites, révoltes comme celle de Nat Turner en 1831.

## L'abolitionnisme
Dans le Nord, l'esclavage est aboli progressivement après l'indépendance. Des **abolitionists** réclament sa fin partout. L'**Underground Railroad**, réseau clandestin de maisons sûres, aide des milliers de fugitifs à rejoindre le Nord ou le Canada. **Harriet Tubman**, elle-même évadée, y retourne une douzaine de fois. **Frederick Douglass**, ancien esclave, devient un orateur et écrivain célèbre. Le roman *Uncle Tom's Cabin* (1852) de Harriet Beecher Stowe émeut des millions de lecteurs.

## La guerre de Sécession
L'expansion vers l'ouest pose une question explosive : les nouveaux États seront-ils esclavagistes ou libres ? En 1860, **Abraham Lincoln**, opposé à l'extension de l'esclavage, est élu. Onze États du Sud font sécession et forment la **Confederacy**. La guerre (**Civil War**, 1861-1865) oppose l'**Union** à la Confédération. C'est la guerre la plus meurtrière de l'histoire américaine : plus de 600 000 soldats morts, peut-être davantage.
Le 1er janvier 1863, Lincoln signe l'**Emancipation Proclamation**, qui libère les esclaves des États rebelles ; près de 200 000 soldats noirs rejoignent l'armée de l'Union. La même année, à Gettysburg, il prononce un célèbre discours sur une nation « conçue dans la liberté ». En avril 1865, le Sud capitule ; quelques jours plus tard, Lincoln est assassiné. Le **13th Amendment** abolit l'esclavage en décembre 1865.

## Une liberté inachevée
Pendant la **Reconstruction**, les anciens esclaves obtiennent la citoyenneté et le droit de vote (14e et 15e amendements), et des élus noirs siègent au Congrès. Mais dès les années 1870, les Blancs du Sud reprennent le pouvoir. Les lois **Jim Crow** imposent la ségrégation, le Ku Klux Klan terrorise la population noire, et le droit de vote est confisqué par des taxes et des tests. Il faudra attendre le mouvement des droits civiques des années 1950-1960. Aujourd'hui, **Juneteenth** (19 juin), jour où les derniers esclaves du Texas apprirent leur libération en 1865, est un jour férié fédéral depuis 2021.
"""

D_["cu_droits_civiques.html"] = """
## Le Sud de Jim Crow
Après l'abolition de l'esclavage, les États du Sud mettent en place la ségrégation : écoles, bus, restaurants, toilettes et même cimetières séparés. En 1896, la Cour suprême l'autorise avec la doctrine « **separate but equal** » (*Plessy v. Ferguson*) ; en réalité, les équipements réservés aux Noirs sont bien inférieurs. Le droit de vote est bloqué par des taxes et des tests de lecture, et les lynchages font régner la terreur.

## Les premières victoires
En 1954, la Cour suprême déclare la ségrégation scolaire contraire à la Constitution (*Brown v. Board of Education*). En 1955, le meurtre d'**Emmett Till**, un adolescent de 14 ans tué au Mississippi, bouleverse le pays. Le 1er décembre 1955, à Montgomery (Alabama), **Rosa Parks**, couturière et militante, refuse de céder sa place à un Blanc dans un bus. Son arrestation déclenche le **Montgomery bus boycott** : pendant 381 jours, la population noire marche ou partage ses voitures. Un jeune pasteur de 26 ans en prend la tête : **Martin Luther King Jr.** En 1956, la ségrégation dans les bus est déclarée illégale.

## La non-violence en action
Inspiré par Gandhi, King prône la **non-violence** et la désobéissance civile. Les militants, souvent très jeunes, multiplient les actions :
- 1957 : neuf élèves noirs, les **Little Rock Nine**, entrent dans un lycée blanc de l'Arkansas sous la protection de l'armée.
- 1960 : des étudiants organisent des **sit-ins** dans des cafétérias réservées aux Blancs, à Greensboro puis dans tout le Sud.
- 1961 : les **Freedom Riders** voyagent ensemble, Noirs et Blancs, dans des bus ; certains sont incendiés.
- 1963 : à Birmingham, la police lâche des chiens et des lances à incendie sur des manifestants, dont des enfants. Les images choquent le monde.
Le 28 août 1963, la **March on Washington** rassemble plus de 250 000 personnes ; King y prononce son discours « **I have a dream** », qui rêve d'une Amérique où ses enfants seront jugés sur leur caractère et non sur leur couleur de peau.

## Les lois
Le **Civil Rights Act** de 1964 interdit la discrimination dans les lieux publics et l'emploi. En 1965, les marches de **Selma** à Montgomery, violemment réprimées le 7 mars (« Bloody Sunday » américain), poussent le Congrès à voter le **Voting Rights Act**. King reçoit le prix Nobel de la paix en 1964.

## D'autres voix et la fin tragique
Tous ne partagent pas la stratégie de King. **Malcolm X**, figure de la Nation of Islam, défend la fierté noire et le droit à l'autodéfense ; il est assassiné en 1965. Le mouvement **Black Power** et les Black Panthers émergent. Le 4 avril 1968, King est assassiné à Memphis, où il soutenait une grève d'éboueurs. Des émeutes éclatent dans plus de cent villes. Aujourd'hui, le **Martin Luther King Day** (troisième lundi de janvier) est férié, et des mouvements comme **Black Lives Matter** prolongent la lutte contre les inégalités raciales.
"""

D_["cu_ellis_island.html"] = """
## La statue de la Liberté
Offerte par la France pour le centenaire de l'indépendance, la statue de la Liberté est conçue par Bartholdi, avec une structure de Gustave Eiffel, et inaugurée en 1886 à l'entrée du port de New York. Sur son socle est gravé un poème d'**Emma Lazarus**, *The New Colossus* (1883), dans lequel la statue appelle le monde à lui envoyer ses pauvres et ses opprimés, ces foules qui aspirent à respirer librement. Pour des millions d'immigrants, c'est la première image de l'Amérique.

## Ellis Island, porte d'entrée
De 1892 à 1954, **Ellis Island** est le principal centre d'accueil des immigrants : environ 12 millions de personnes y passent. Aujourd'hui, on estime que près de 40 % des Américains ont au moins un ancêtre passé par cette île. Les passagers de première et deuxième classe sont contrôlés sur le bateau ; les autres, entassés dans l'**steerage** (l'entrepont), passent par Ellis Island.
Le parcours dure quelques heures : montée du grand escalier, observée par des médecins qui repèrent les malades ; examen des yeux ; marques à la craie sur les vêtements de ceux qui doivent être examinés de plus près ; questions sur l'identité, le métier, l'argent. Environ 2 % sont refusés, d'où le surnom d'« **Island of Tears** ».

## D'où viennent-ils ?
Après les Irlandais et les Allemands du milieu du 19e siècle, arrivent surtout des Italiens du Sud, des Juifs d'Europe de l'Est fuyant les pogroms, des Polonais, des Grecs, des Scandinaves. Ils fuient la misère, les persécutions ou le service militaire. Ils s'entassent dans les **tenements** du Lower East Side de New York, travaillent dans les usines, les mines, la construction. Chaque communauté recrée son quartier : Little Italy, Chinatown…

## Le rêve… et les fermetures
L'expression **American Dream**, popularisée en 1931 par l'historien James Truslow Adams, résume la promesse : chacun peut réussir par son travail, quelle que soit son origine. Mais l'accueil n'est pas toujours ouvert. Dès 1882, le **Chinese Exclusion Act** interdit l'immigration chinoise. Dans les années 1920, des lois de **quotas** favorisent l'Europe du Nord et limitent fortement l'arrivée d'Italiens, de Juifs et d'Asiatiques. Elles ne sont abolies qu'en 1965.

## Aujourd'hui
Depuis 1965, la majorité des immigrants viennent d'Amérique latine et d'Asie. L'immigration, notamment illégale à la frontière mexicaine, est l'un des sujets les plus explosifs de la politique américaine. Deux images s'opposent : le **melting pot**, où les cultures fusionnent en une identité américaine, et le **salad bowl**, où chacune garde sa saveur. Ellis Island est devenue un musée de l'immigration, visité chaque année par des millions de personnes en quête de leurs racines.
"""

D_["cu_1929_new_deal.html"] = """
## Les années folles
Après la Première Guerre mondiale, les États-Unis connaissent une forte croissance : voitures (la Ford T), radio, électroménager, cinéma, jazz. Ce sont les **Roaring Twenties**. C'est aussi l'époque de la **Prohibition** (1920-1933), qui interdit l'alcool et fait la fortune des gangsters comme Al Capone. Beaucoup d'Américains achètent des actions à crédit, persuadés que la Bourse montera toujours.

## Le krach
Fin octobre 1929, la Bourse de **Wall Street** s'effondre : le **Black Thursday** (24 octobre) puis le **Black Tuesday** (29 octobre). En quelques semaines, des fortunes disparaissent. Les banques, qui avaient prêté pour spéculer, font faillite en chaîne ; les épargnants perdent tout. Les entreprises licencient, la consommation s'effondre. En 1933, environ un quart des travailleurs sont au chômage. C'est la **Great Depression**, qui gagne aussi l'Europe.

## La misère
Des familles expulsées s'installent dans des bidonvilles appelés **Hoovervilles**, du nom du président Herbert Hoover, accusé d'en faire trop peu en attendant que l'économie se redresse d'elle-même. On fait la queue pour du pain dans les **breadlines** et les soupes populaires. Dans les Grandes Plaines, une sécheresse et des pratiques agricoles qui ont épuisé les sols provoquent d'énormes tempêtes de poussière : le **Dust Bowl**. Des centaines de milliers de fermiers ruinés, les « Okies », partent vers la Californie. John Steinbeck raconte leur exode dans *The Grapes of Wrath* (1939), et la photographe Dorothea Lange immortalise leur détresse.

## Roosevelt et le New Deal
En 1932, le démocrate **Franklin Delano Roosevelt** (FDR) est élu. Dans son discours d'investiture, il affirme que la seule chose à craindre est la peur elle-même. Il promet un **New Deal**, une « nouvelle donne » :
- **Relief** (secours) : aides aux chômeurs et aux plus pauvres ;
- **Recovery** (relance) : grands travaux (routes, barrages, écoles, parcs) via des agences comme le CCC ou la WPA, qui emploient des millions de personnes, y compris des artistes ;
- **Reform** : contrôle des banques et de la Bourse, garantie des dépôts, droits syndicaux, salaire minimum, et en 1935 le **Social Security Act**, qui crée les retraites et l'assurance chômage.
Roosevelt parle directement aux Américains à la radio dans ses **fireside chats** (« causeries au coin du feu »).

## Bilan
Le New Deal n'a pas totalement vaincu la crise : c'est surtout l'effort de guerre, après 1941, qui ramène le plein emploi. Mais il a rendu espoir et transformé durablement le rôle de l'État fédéral. Ses adversaires dénonçaient une dérive vers le socialisme ; ses partisans y voient la naissance d'un État protecteur. Roosevelt est le seul président élu quatre fois (1932, 1936, 1940, 1944), ce qui a conduit à limiter ensuite les présidents à deux mandats.
"""

D_["cu_vietnam.html"] = """
## Pourquoi le Vietnam ?
Après le départ des Français en 1954, le Vietnam est coupé en deux : un Nord communiste et un Sud soutenu par les États-Unis. Selon la **domino theory**, si un pays tombe dans le communisme, ses voisins suivront. Washington envoie d'abord des conseillers militaires. En 1964, après un incident naval dans le golfe du Tonkin, le Congrès donne carte blanche au président Lyndon Johnson. En 1968, plus de 500 000 soldats américains sont au Vietnam.

## Une guerre impossible
Les soldats affrontent une guérilla, le Viêt-cong, qui se cache dans la jungle et parmi les villageois. L'armée bombarde massivement, utilise le napalm et un défoliant toxique, l'**Agent Orange**. En 1968, le massacre de My Lai, où des soldats américains tuent des centaines de civils, choque le monde. Beaucoup de soldats sont des jeunes appelés par la conscription (**the draft**), plus souvent issus de milieux pauvres ou des minorités.

## La première guerre télévisée
Chaque soir, les journaux télévisés montrent des combats, des blessés, des villages en feu. En 1968, l'**offensive du Têt** prouve que la victoire n'est pas proche. Le présentateur Walter Cronkite, très respecté, déclare que la guerre est dans une impasse. L'opinion bascule.

## La contestation
Les campus universitaires deviennent des foyers de protestation. Des jeunes brûlent leur convocation (**draft card**) ; certains fuient au Canada. Le champion de boxe **Muhammad Ali** refuse de partir et perd son titre. En avril 1967, Martin Luther King dénonce lui aussi la guerre. Le 4 mai 1970, à **Kent State** (Ohio), la Garde nationale tire sur des étudiants : quatre morts. Des centaines de milliers de manifestants défilent à Washington.

## La contre-culture
Une partie de la jeunesse rejette le mode de vie de ses parents : la consommation, la guerre, le conformisme. Les **hippies** prônent « **peace and love** », la vie en communauté, la liberté sexuelle ; beaucoup expérimentent les drogues. En 1967, le **Summer of Love** attire des dizaines de milliers de jeunes à San Francisco. En août 1969, le festival de **Woodstock** réunit environ 400 000 personnes autour de Jimi Hendrix, Janis Joplin ou Joan Baez. Cette période voit aussi naître le féminisme moderne, le mouvement écologiste et la lutte pour les droits des homosexuels (émeutes de Stonewall, 1969).

## La fin
Le président Nixon retire progressivement les troupes ; les accords de paix de Paris sont signés en 1973. Le 30 avril 1975, Saïgon tombe aux mains des communistes. Environ 58 000 Américains et peut-être plus de 2 millions de Vietnamiens sont morts. À leur retour, beaucoup de vétérans sont mal accueillis, et souffrent de traumatismes. Le **Vietnam Veterans Memorial** de Washington, un mur noir où sont gravés leurs noms, est inauguré en 1982. Le « syndrome du Vietnam » a longtemps rendu les Américains méfiants envers les interventions militaires.
"""

D_["cu_11_septembre.html"] = """
## Le matin du 11 septembre
Le 11 septembre 2001, 19 terroristes du réseau **al-Qaeda**, dirigé par Oussama ben Laden, détournent quatre avions de ligne. À 8 h 46 puis à 9 h 03, deux avions percutent les tours jumelles du **World Trade Center** à New York, qui s'effondrent dans la matinée. Un troisième avion s'écrase sur le **Pentagon**, le siège du ministère de la Défense, près de Washington. Dans le quatrième, le vol United 93, les passagers, informés par téléphone, se révoltent contre les pirates de l'air ; l'avion s'écrase dans un champ de Pennsylvanie, épargnant sa cible, probablement le Capitole ou la Maison-Blanche.
Près de 3 000 personnes meurent, de plus de 90 nationalités. Parmi elles, plus de 400 secouristes, dont 343 pompiers new-yorkais. Des milliers d'autres tomberont malades à cause des poussières toxiques.

## Un choc mondial
Pour la première fois depuis Pearl Harbor en 1941, les États-Unis sont frappés sur leur sol par une attaque étrangère. Les images, diffusées en direct, font le tour du monde. Un immense élan de solidarité suit : en France, *Le Monde* titre « Nous sommes tous Américains ».

## La « guerre contre le terrorisme »
Le président **George W. Bush** déclare la **War on Terror**. En octobre 2001, les États-Unis et leurs alliés attaquent l'Afghanistan, où le régime des talibans abrite al-Qaïda. En 2003, ils envahissent l'Irak de Saddam Hussein, accusé de posséder des armes de destruction massive — des armes qui n'ont jamais été trouvées, ce qui a fait de cette guerre l'une des plus contestées de l'histoire récente. Ben Laden est tué par un commando américain au Pakistan le 2 mai 2011. Après vingt ans de guerre, les dernières troupes américaines quittent l'Afghanistan en août 2021, et les talibans reprennent le pouvoir.

## Une société transformée
La sécurité devient une obsession : contrôles renforcés dans les aéroports, création du ministère de la **Homeland Security**, **Patriot Act** qui élargit la surveillance. Des révélations sur la torture de prisonniers et sur la prison de **Guantánamo**, où des détenus sont enfermés sans procès, suscitent de vives critiques. Les musulmans américains subissent une hausse des discriminations. Le débat entre sécurité et libertés individuelles reste vif.

## Se souvenir
Sur le site des tours, le **9/11 Memorial** présente deux bassins à l'emplacement exact des tours, entourés des noms des victimes, à côté d'un musée. Le **One World Trade Center**, inauguré en 2014, mesure 1 776 pieds, en écho à l'année de l'indépendance. Chaque 11 septembre, les noms des victimes sont lus lors d'une cérémonie.
"""

D_["cu_conquete_spatiale.html"] = """
## Une course née de la guerre froide
Après 1945, Américains et Soviétiques récupèrent les ingénieurs et les fusées allemandes (comme Wernher von Braun, qui travaillera pour les États-Unis). La conquête de l'espace devient une vitrine de la puissance technologique et un enjeu militaire : une fusée capable d'atteindre l'espace peut aussi porter une bombe atomique.

## L'avance soviétique
Le 4 octobre 1957, l'URSS lance **Sputnik**, premier satellite artificiel. C'est un choc aux États-Unis : on craint d'être dépassé. Le pays crée la **NASA** en 1958 et investit massivement dans l'éducation scientifique. Mais les Soviétiques continuent d'accumuler les premières : la chienne Laïka en orbite (1957), **Youri Gagarine**, premier homme dans l'espace le 12 avril 1961, Valentina Terechkova, première femme en 1963.

## Le pari de Kennedy
En mai 1961, le président **John F. Kennedy** fixe un objectif fou : envoyer un homme sur la Lune et le ramener sain et sauf avant la fin de la décennie. En 1962, à Houston, il explique que l'Amérique choisit d'aller sur la Lune non parce que c'est facile, mais parce que c'est difficile. Les programmes s'enchaînent : **Mercury** (un astronaute ; Alan Shepard en 1961, John Glenn en orbite en 1962), **Gemini** (deux astronautes, sorties dans l'espace, rendez-vous orbitaux), puis **Apollo**.
Des centaines de milliers de personnes y travaillent. Parmi elles, des mathématiciennes afro-américaines comme **Katherine Johnson**, longtemps restées dans l'ombre, dont l'histoire a été racontée dans le film *Hidden Figures* (2016). En 1967, l'incendie d'Apollo 1 coûte la vie à trois astronautes.

## Apollo 11
Le 16 juillet 1969, la fusée géante **Saturn V** décolle de Floride. Le 20 juillet, le module lunaire *Eagle* se pose sur la Lune. **Neil Armstrong** pose le pied sur le sol lunaire et prononce sa phrase célèbre sur le petit pas pour un homme et le bond de géant pour l'humanité. **Buzz Aldrin** le rejoint, pendant que **Michael Collins** reste en orbite. Environ 600 millions de personnes regardent l'événement à la télévision. Les astronautes plantent un drapeau américain et laissent une plaque indiquant qu'ils sont venus en paix pour toute l'humanité.

## Après la Lune
Jusqu'en 1972, douze astronautes marchent sur la Lune. Apollo 13 (1970) frôle la catastrophe, mais l'équipage revient vivant. Puis l'intérêt du public et les budgets diminuent. Viennent la navette spatiale (1981-2011), puis la **Station spatiale internationale**, symbole d'une coopération entre anciens rivaux. Aujourd'hui, des entreprises privées comme SpaceX participent à la conquête, et la NASA prépare le retour d'humains sur la Lune avec le programme **Artemis**, avant, peut-être, Mars.
"""

D_["cu_lycee_us.html"] = """
## Un parcours en 12 années
Aux États-Unis, on compte les années scolaires en **grades**, de 1 à 12. Après l'**elementary school** et la **middle school** (ou junior high), on entre à la **high school** vers 14 ans, pour quatre ans : **freshman** (9th grade), **sophomore** (10th), **junior** (11th), **senior** (12th). La plupart des élèves vont dans une **public school** gratuite, gérée localement : les moyens varient donc beaucoup selon la richesse du quartier.

## Une journée au lycée
Pas d'uniforme dans la plupart des lycées publics. Le **school bus** jaune ramasse les élèves. La journée commence souvent par le **Pledge of Allegiance**, le serment au drapeau. Les élèves changent de salle à chaque cours et rangent leurs affaires dans des casiers (**lockers**) dans les couloirs (**hallways**). Ils choisissent une partie de leurs cours (**electives**) : théâtre, photo, langues, menuiserie, informatique… On déjeune à la **cafeteria**.
Les notes vont de A à F ; leur moyenne donne le **GPA** (Grade Point Average), sur 4. Pour entrer à l'université (**college**), on passe souvent des tests standardisés comme le **SAT** ou l'**ACT**, et on envoie des lettres de motivation qui valorisent les activités extrascolaires.

## Le sport, au cœur de la vie du lycée
Les équipes sportives représentent le lycée et toute la ville. Le vendredi soir, le match de football américain réunit les familles, avec les **cheerleaders** et la fanfare (**marching band**). Les meilleurs athlètes peuvent obtenir des bourses (**scholarships**) pour l'université. Il y a aussi le basketball, le baseball, l'athlétisme, la lutte…

## Les grands moments de l'année
- **Homecoming**, à l'automne : on accueille les anciens élèves, avec un défilé, un match, un bal, et l'élection d'un roi et d'une reine.
- Le **yearbook** : un album avec les photos de tous les élèves, que l'on fait dédicacer par ses amis en fin d'année.
- Le **prom**, bal de fin d'année des juniors et seniors : robes de soirée, costumes, bouquets au poignet (**corsages**), parfois une limousine.
- La **graduation** : en toge et toque (**cap and gown**), les seniors reçoivent leur diplôme et lancent leur toque en l'air.

## Derrière les clichés
Les séries et les films donnent une image très codifiée du lycée américain (les **jocks**, les **nerds**, les populaires…). La réalité est plus variée, et parfois plus dure : inégalités entre établissements riches et pauvres, coût très élevé des études supérieures qui oblige beaucoup d'étudiants à s'endetter, et exercices de confinement face au risque de fusillade.
"""

D_["cu_elections_us.html"] = """
## Un calendrier très long
L'élection présidentielle a lieu tous les quatre ans, le mardi qui suit le premier lundi de novembre. Mais la campagne commence plus d'un an avant. D'abord, chaque parti désigne son candidat lors des **primaries** (votes à bulletin secret) et des **caucuses** (réunions où les électeurs débattent puis votent), organisées État par État de janvier à juin. Les premiers États (traditionnellement l'Iowa et le New Hampshire) ont une influence énorme. En été, chaque parti tient sa **national convention**, grande fête médiatique où le candidat (**nominee**) est officiellement investi et présente son colistier (**running mate**), futur vice-président.

## La campagne
Les candidats s'affrontent lors de **debates** télévisés, multiplient les meetings (**rallies**) et dépensent des sommes colossales en publicités. Depuis l'arrêt *Citizens United* (2010) de la Cour suprême, des **super PACs** peuvent dépenser sans limite pour soutenir un candidat, à condition de ne pas se coordonner officiellement avec lui. Beaucoup d'États permettent de voter en avance ou par correspondance.

## Le collège électoral
Les citoyens ne votent pas directement pour le président, mais pour des grands électeurs (**electors**). Chaque État en a autant que de parlementaires au Congrès (au moins 3) ; la Californie en a 54, le Wyoming 3. Au total : **538**. Il en faut **270** pour gagner. Dans 48 États, le candidat arrivé en tête remporte tous les grands électeurs de l'État (**winner-takes-all**) ; seuls le Maine et le Nebraska les répartissent.

## Swing states et vote populaire
Conséquence : beaucoup d'États sont acquis d'avance (**safe states**), et la campagne se concentre sur quelques **swing states** ou **battleground states** comme la Pennsylvanie, le Michigan, le Wisconsin, la Géorgie, l'Arizona ou le Nevada. Un candidat peut gagner sans avoir la majorité des voix au niveau national : c'est arrivé en 2000 (George W. Bush contre Al Gore, après un recomptage très contesté en Floride) et en 2016 (Donald Trump contre Hillary Clinton). Les défenseurs du système disent qu'il protège les petits États et oblige à faire campagne dans tout le pays ; ses critiques le jugent antidémocratique.

## Et après ?
En décembre, les grands électeurs votent officiellement ; en janvier, le Congrès certifie le résultat. Le nouveau président prête serment le **20 janvier** lors de l'**Inauguration**, devant le Capitole. Tous les deux ans ont aussi lieu les **midterms**, élections de mi-mandat qui renouvellent toute la Chambre des représentants et un tiers du Sénat : elles servent souvent de sanction contre le parti au pouvoir. La participation (**turnout**) est historiquement plus faible qu'en France, mais elle a fortement augmenté lors des élections récentes.
"""

D_["cu_amerindiens.html"] = """
## Avant l'arrivée des Européens
Avant 1492, plusieurs millions de personnes vivent en Amérique du Nord, réparties en centaines de peuples aux langues et aux modes de vie très différents : agriculteurs du Sud-Ouest vivant dans des villages de pierre (les Pueblos), chasseurs de bisons des Plaines, pêcheurs de la côte Pacifique, confédérations politiques comme celle des Iroquois. Les maladies apportées par les Européens (variole, rougeole) tuent une très grande partie de la population, bien avant les guerres.

## Conquête et dépossession
Les traités signés avec les nations amérindiennes sont régulièrement violés. Au 19e siècle, les déportations (Trail of Tears), les guerres et la destruction des bisons conduisent les survivants dans des **reservations**, souvent sur des terres pauvres. À la fin du 19e siècle, la loi Dawes découpe ces réserves en parcelles individuelles : les Amérindiens perdent encore les deux tiers de leurs terres.

## « Tuer l'Indien, sauver l'homme »
À partir de la fin du 19e siècle, des dizaines de milliers d'enfants sont envoyés de force dans des **boarding schools**, des pensionnats destinés à les « civiliser ». Le fondateur de l'un d'eux, Richard Pratt, résumait son projet en une formule : tuer l'Indien pour sauver l'homme. Cheveux coupés, langue interdite, noms changés, mauvais traitements : de nombreux enfants y sont morts. En 2024, le président Biden a présenté des excuses officielles au nom de l'État fédéral. Les Amérindiens ne deviennent citoyens américains qu'en 1924.

## La renaissance et les combats
Dans les années 1960-1970, le mouvement **Red Power** et l'**American Indian Movement** (AIM) réclament le respect des traités : occupation de l'île d'Alcatraz (1969-1971), puis de Wounded Knee (1973). Depuis les années 1970, la politique fédérale reconnaît l'autodétermination des tribus.
Aujourd'hui, plus de 570 nations tribales sont officiellement reconnues. Elles ont leurs gouvernements, leurs tribunaux, leur police et une forme de **sovereignty**. Certaines tirent des revenus importants de casinos, autorisés sur leurs terres. Mais beaucoup de réserves connaissent encore une grande pauvreté, un chômage élevé, des problèmes de santé et un accès difficile à l'eau potable.
En 2016, à **Standing Rock** (Dakota du Nord), des milliers de personnes venues de tout le pays soutiennent les Sioux contre un oléoduc (le Dakota Access Pipeline) qui menace leur eau et des sites sacrés : c'est l'un des plus grands rassemblements amérindiens de l'histoire.

## Visibilité et symboles
Les débats portent aussi sur les représentations : de nombreuses équipes ont abandonné les noms et mascottes jugés offensants (l'équipe de football de Washington est devenue les Commanders). Plusieurs États célèbrent désormais l'**Indigenous Peoples' Day** à la place ou à côté du Columbus Day. En 2021, **Deb Haaland**, du peuple Laguna Pueblo, devient la première Amérindienne ministre fédérale.
"""
