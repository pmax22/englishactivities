import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
exec(open(_EA_OUT+"/cuhelp.py", encoding="utf-8").read())

# ═════════ COUR SUPRÊME ═════════
F = "cu_cour_supreme.html"
DZ(F, """
## Neuf juges nommés à vie
La **Supreme Court**, à Washington, est la plus haute juridiction des États-Unis. Elle compte **neuf juges** (**justices**), nommés **à vie** par le président et confirmés par le Sénat. Leur nomination est donc un enjeu politique majeur : un président peut influencer le pays pendant des décennies. Depuis l'arrêt *Marbury v. Madison* (1803), la Cour peut annuler une loi qu'elle juge contraire à la Constitution : c'est le **judicial review**.

## Une matrice d'exclusion…
- *Dred Scott v. Sandford* (1857) : la Cour déclare que les Noirs, esclaves ou libres, ne peuvent pas être citoyens américains. Cet arrêt contribue à déclencher la guerre de Sécession.
- *Plessy v. Ferguson* (1896) : la ségrégation est jugée constitutionnelle si les équipements sont « séparés mais égaux » (**separate but equal**), ce qui légitime pendant des décennies les lois Jim Crow.

## … et d'inclusion
- *Brown v. Board of Education* (1954) : la Cour déclare à l'unanimité que la ségrégation dans les écoles publiques est inconstitutionnelle. L'avocat de la NAACP, **Thurgood Marshall**, deviendra en 1967 le premier juge noir de la Cour.
- *Loving v. Virginia* (1967) : les interdictions de mariage entre personnes de couleurs de peau différentes sont abolies.
- *Obergefell v. Hodges* (2015) : le mariage homosexuel devient un droit dans tout le pays.
- En 1973, *Roe v. Wade* reconnaît un droit fédéral à l'avortement ; en 2022, l'arrêt *Dobbs* l'annule et renvoie la question aux États, une décision qui divise profondément le pays.

## La discrimination positive
L'**affirmative action** désigne les politiques qui visent à favoriser l'accès des minorités historiquement discriminées à l'université ou à l'emploi. En 1978 (*Bakke*), la Cour interdit les quotas raciaux mais autorise les universités à tenir compte de l'origine parmi d'autres critères. En **2023**, dans une affaire contre l'université **Harvard**, la Cour met fin à la prise en compte de l'origine ethnique dans les admissions.
- Pour ses partisans, la discrimination positive corrigeait des inégalités héritées de l'esclavage et de la ségrégation, et favorisait la diversité.
- Pour ses opposants, elle était elle-même une discrimination, notamment envers certains candidats asiatiques-américains, et seul le mérite individuel devrait compter.
Les universités cherchent désormais d'autres moyens de favoriser la **social mobility**, par exemple en tenant compte du milieu social des candidats.

## Une Cour politique ?
Aujourd'hui, six juges ont été nommés par des présidents républicains et trois par des démocrates. Les uns saluent une Cour fidèle au texte de la Constitution, les autres dénoncent une institution trop politisée. Ce débat montre le poids considérable du pouvoir judiciaire dans la démocratie américaine.
[→ Voir aussi : les institutions américaines](cu_institutions_us.html)
""", """
a judge = un juge
a court = un tribunal
the law = la loi
a right = un droit
a decision = une décision
equal = égal
a university = une université
a minority = une minorité
""", [
 ("Comment sont nommés les juges de la Cour suprême ?", ["À vie, par le président, avec l'accord du Sénat", "Élus par le peuple pour 4 ans", "Tirés au sort"], ""),
 ("Qu'est-ce que le judicial review ?", ["Le pouvoir d'annuler une loi contraire à la Constitution", "Un examen d'avocat", "Une élection"], ""),
 ("Que décide Plessy v. Ferguson (1896) ?", ["La ségrégation est légale si « séparés mais égaux »", "La fin de l'esclavage", "Le droit de vote des femmes"], ""),
 ("Que décide Brown v. Board of Education (1954) ?", ["La ségrégation à l'école est inconstitutionnelle", "Les écoles deviennent payantes", "L'avortement est autorisé"], ""),
 ("Qu'a décidé la Cour en 2023 sur l'affirmative action ?", ["Elle met fin à la prise en compte de l'origine dans les admissions", "Elle l'étend", "Elle crée des quotas"], ""),
 ("Que pensent les opposants de la discrimination positive ?", ["Que c'est une discrimination et que seul le mérite doit compter", "Qu'elle ne va pas assez loin", "Qu'elle n'existe pas"], ""),
], [("NAACP", "grande association de défense des droits des Afro-Américains"), ("Jim Crow", "nom donné aux lois de ségrégation du Sud")])
D = "cs"
culture(F, "Culture : The US Supreme Court", 'The Supreme <span>Court</span>',
  "Culture · neuf juges, de la ségrégation à la discrimination positive", ("#e5e7eb", "#1e3a8a"),
  reperes("La Cour suprême des États-Unis a parfois légitimé l'exclusion, parfois imposé l'inclusion. Ses décisions changent la vie de millions d'Américains.",
    [("1803", "Marbury v. Madison : le contrôle de constitutionnalité"), ("1857", "Dred Scott"), ("1896", "Plessy v. Ferguson : « separate but equal »"),
     ("1954", "Brown v. Board of Education"), ("2015", "Obergefell : mariage pour tous"), ("2022", "Dobbs annule Roe v. Wade"), ("2023", "fin de l'affirmative action à l'université")],
    "the Supreme Court, a justice, a ruling, the Constitution, segregation, affirmative action, a minority, a landmark case"),
  {D: doc("Nine judges, big decisions", [
    "The Supreme Court is the highest court in the USA. It has nine judges, who are chosen by the President and stay for life. They can cancel a law if it goes against the Constitution.",
    "In the past, the Court sometimes supported discrimination. In 1896, it said that segregation was legal if things were \"separate but equal\".",
    "But in 1954, in Brown v. Board of Education, it decided that segregation in schools was unconstitutional. Later, it also protected interracial and same-sex marriage.",
    "Affirmative action helped minorities to get into universities. In 2023, the Court ended the use of race in university admissions. Some people celebrated, others were angry.",
    "Today, many Americans think the Court has become too political. Its decisions have a huge impact on everyday life."])},
  [TF(D, "The Supreme Court has nine judges.", True, "« nine judges »."),
   TF(D, "The judges are elected by the people.", False, "« chosen by the President »."),
   TF(D, "In 1896, the Court said segregation was illegal.", False, "Elle l'a jugée légale."),
   TF(D, "Brown v. Board of Education ended segregation in schools.", True, "« segregation in schools was unconstitutional »."),
   TF(D, "In 2023, the Court ended the use of race in admissions.", True, "« ended the use of race »."),
   TF(D, "Everybody agrees with the Court's decisions.", False, "« Some people celebrated, others were angry »." )],
  [Q(D, "Who chooses the Supreme Court judges?", ["The President.", "The people.", "The King."]),
   Q(D, "What can the Court do?", ["Cancel a law that goes against the Constitution.", "Make new taxes.", "Declare war."]),
   Q(D, "What did the Court decide in 1954?", ["Segregation in schools was unconstitutional.", "Women could vote.", "Slavery was legal."]),
   Q(D, "What do many Americans think today?", ["The Court has become too political.", "The Court is useless.", "The Court should have 100 judges."])],
  [DT(D, "Qui est le premier juge noir de la Cour suprême ?", ["Thurgood Marshall", "Martin Luther King", "Barack Obama", "Clarence Thomas"]),
   DT(D, "Quelle université est au cœur de l'affaire de 2023 ?", ["Harvard", "Yale", "Stanford", "Oxford"]),
   DT(D, "Quel arrêt annule Roe v. Wade en 2022 ?", ["Dobbs", "Brown", "Plessy", "Loving"]),
   DT(D, "Comment dit-on « la discrimination positive » ?", ["Affirmative action", "Positive racism", "Good discrimination", "Equal action"])],
  [W(D, "Trouve le mot qui veut dire « annuler ».", "cancel"), W(D, "Trouve le mot qui veut dire « inconstitutionnelle ».", "unconstitutional"),
   W(D, "Trouve le mot qui veut dire « les admissions ».", "admissions"), W(D, "Trouve le mot qui veut dire « un impact énorme » (2 mots).", ["huge impact", "a huge impact"])])

# ═════════ SALEM ═════════
F = "cu_salem.html"
DZ(F, """
## Salem, 1692
Au début de l'année 1692, dans le village puritain de **Salem**, au Massachusetts, plusieurs jeunes filles, dont la fille et la nièce du pasteur, sont prises de convulsions et de cris inexplicables. Les médecins ne trouvent pas de cause : on conclut à la **sorcellerie**. Sous pression, les jeunes filles accusent trois femmes marginales, dont **Tituba**, une esclave originaire des Caraïbes qui travaille chez le pasteur. Tituba « avoue » et affirme qu'il y a d'autres sorcières dans le village.

## La spirale des accusations
Une véritable panique s'empare de la région. Plus de 200 personnes sont accusées, souvent des femmes, des pauvres, des voisins en conflit ou des personnes qui ne respectent pas les normes. Un tribunal spécial accepte la « **spectral evidence** » : un témoin peut affirmer avoir vu l'esprit de l'accusé l'attaquer en rêve. Ceux qui avouent sont épargnés, ceux qui clament leur innocence sont condamnés : **19 personnes sont pendues**, un vieil homme, Giles Corey, meurt écrasé sous des pierres pour avoir refusé de plaider, et plusieurs meurent en prison. À l'automne 1692, devant les excès, le gouverneur arrête les procès. Des années plus tard, des juges et des jurés présentent des excuses publiques ; la dernière accusée a été officiellement innocentée… en 2022.

## Pourquoi cette folie ?
Les historiens avancent plusieurs explications : la peur de la guerre contre des tribus amérindiennes, les rivalités entre familles du village, la rigidité religieuse des **puritains**, l'hystérie collective, la place des femmes indépendantes, perçues comme une menace. Salem montre comment la peur peut détruire la justice.

## De Salem à Hollywood : The Crucible
En 1953, le dramaturge **Arthur Miller** écrit *The Crucible* (Les Sorcières de Salem). La pièce raconte les procès de 1692, mais tout le monde comprend qu'elle parle du présent : le **maccarthysme**. Au début des années 1950, le sénateur Joseph McCarthy et une commission du Congrès traquent les communistes supposés. Des centaines d'Américains sont interrogés et poussés à dénoncer leurs amis ; à Hollywood, des scénaristes et des acteurs sont placés sur une **liste noire** (**blacklist**) et ne peuvent plus travailler. Miller lui-même est convoqué en 1956 et refuse de donner des noms.

## La « chasse aux sorcières » aujourd'hui
L'expression **witch hunt** désigne désormais toute persécution fondée sur la peur, la rumeur et la présomption de culpabilité plutôt que sur des preuves. Elle est souvent utilisée dans le débat politique, et parfois à propos des emballements sur les réseaux sociaux, où une personne peut être jugée par la foule avant d'avoir pu se défendre : on parle de **trial by media**. Salem, devenue une destination touristique très fréquentée à Halloween, rappelle l'importance de la présomption d'innocence.
[→ Voir aussi : la peur rouge (Red Scare)](cu_red_scare.html)
""", """
a witch = une sorcière
a trial = un procès
a judge = un juge
fear = la peur
to accuse = accuser
guilty = coupable
innocent = innocent
a rumour = une rumeur
""", [
 ("Pourquoi les jeunes filles de Salem accusent-elles des femmes ?", ["Leurs crises inexplicables sont attribuées à la sorcellerie", "Elles veulent de l'argent", "Le roi l'ordonne"], ""),
 ("Qu'est-ce que la « spectral evidence » ?", ["Le témoignage d'avoir vu l'esprit de l'accusé en rêve", "Une preuve scientifique", "Une photo"], ""),
 ("Combien de personnes sont pendues ?", ["19", "200", "2"], ""),
 ("De quoi parle vraiment The Crucible ?", ["Du maccarthysme des années 1950", "De la guerre de Sécession", "D'Halloween"], ""),
 ("Qu'est-ce que la blacklist d'Hollywood ?", ["Une liste de personnes accusées de communisme qui ne pouvaient plus travailler", "Une liste de films", "Un prix"], ""),
 ("Que désigne aujourd'hui « witch hunt » ?", ["Une persécution fondée sur la peur et la rumeur", "Une fête", "Un jeu vidéo"], ""),
], [("**Tituba**", "esclave accusée en 1692"), ("puritains", "protestants très stricts venus d'Angleterre"), ("**Arthur Miller**", "dramaturge américain, 1915-2005")])
D = "sl"
culture(F, "Culture : Witch hunts, from Salem to Hollywood", 'Witch <span>hunts</span>',
  "Culture · Salem 1692, The Crucible et le maccarthysme", ("#a3a3a3", "#7c3aed"),
  reperes("En 1692, à Salem, une panique collective conduit à l'exécution de 19 personnes accusées de sorcellerie. Arthur Miller en a fait une métaphore du maccarthysme.",
    [("1692", "les procès de Salem"), ("1950 – 1954", "le maccarthysme"), ("1953", "The Crucible d'Arthur Miller"),
     ("1956", "Miller refuse de dénoncer des noms"), ("2022", "la dernière accusée de Salem innocentée")],
    "a witch hunt, a trial, an accusation, evidence, hysteria, a blacklist, guilty, the presumption of innocence"),
  {D: doc("The Crucible", [
    "In 1692, in the small Puritan village of Salem, Massachusetts, some girls started to scream and shake. People thought it was witchcraft.",
    "The girls accused several women. Soon, more than 200 people were accused. There was no real evidence, but 19 people were hanged.",
    "In 1953, Arthur Miller wrote a play about Salem called The Crucible. But it was also about his own time: the McCarthy era, when people were accused of being communists.",
    "In Hollywood, some writers and actors were blacklisted and could not work. Miller himself refused to give names.",
    "Today, the expression \"witch hunt\" means attacking people because of fear and rumours, not because of proof."])},
  [TF(D, "The Salem witch trials took place in 1692.", True, "« In 1692 »."),
   TF(D, "There was strong evidence against the accused.", False, "« There was no real evidence »."),
   TF(D, "19 people were hanged.", True, "« 19 people were hanged »."),
   TF(D, "The Crucible is a novel by Mark Twain.", False, "C'est une pièce d'Arthur Miller."),
   TF(D, "Some Hollywood actors were blacklisted.", True, "« were blacklisted »."),
   TF(D, "Arthur Miller gave the names of his friends.", False, "« refused to give names »." )],
  [Q(D, "What did people think was happening in Salem?", ["Witchcraft.", "An illness.", "A war."]),
   Q(D, "What is The Crucible about?", ["Salem and the McCarthy era.", "A love story in Paris.", "A football team."]),
   Q(D, "What happened to blacklisted people?", ["They could not work.", "They became famous.", "They won prizes."]),
   Q(D, "What does \"witch hunt\" mean today?", ["Attacking people because of fear and rumours.", "Looking for real witches.", "A Halloween game."])],
  [DT(D, "Dans quel État se trouve Salem ?", ["Le Massachusetts", "La Virginie", "New York", "La Californie"]),
   DT(D, "Qui est la première femme accusée qui « avoue » ?", ["Tituba", "Abigail", "Elizabeth Proctor", "Mary Shelley"]),
   DT(D, "Quel sénateur donne son nom à la chasse aux communistes ?", ["Joseph McCarthy", "John Kennedy", "Richard Nixon", "Abraham Lincoln"]),
   DT(D, "Comment dit-on « une preuve » ?", ["Evidence / proof", "Prove", "A test", "Witness"])],
  [W(D, "Trouve le mot qui veut dire « la sorcellerie ».", "witchcraft"), W(D, "Trouve le mot qui veut dire « pendus ».", "hanged"),
   W(D, "Trouve le mot qui veut dire « mis sur liste noire ».", "blacklisted"), W(D, "Trouve le mot qui veut dire « une preuve ».", "proof")])

# ═════════ PORTO RICO ═════════
F = "cu_porto_rico.html"
DZ(F, """
## Une île des Caraïbes devenue américaine
**Puerto Rico** est une île des Caraïbes d'environ 3,2 millions d'habitants. Peuplée à l'origine par les **Taínos**, elle est colonisée par l'Espagne après le passage de Christophe Colomb en 1493 et reste espagnole pendant 400 ans. En **1898**, après sa victoire dans la guerre hispano-américaine, les États-Unis s'emparent de l'île. Depuis, Porto Rico est un **territoire** des États-Unis.

## Citoyens… mais pas tout à fait
Depuis une loi de **1917**, les Portoricains sont **citoyens américains** : ils peuvent s'installer librement aux États-Unis, ont un passeport américain et ont servi dans l'armée américaine. Depuis 1952, l'île a sa propre Constitution et son gouverneur élu ; elle s'appelle officiellement un **Commonwealth** (« État libre associé »). Mais ses habitants **ne votent pas à l'élection présidentielle** et n'ont au Congrès qu'un représentant sans droit de vote. Ils paient certains impôts fédéraux, mais pas tous, et reçoivent moins d'aides que les États.

## Le 51e État ?
Le statut de l'île divise ses habitants en trois camps :
- devenir le **51e État** des États-Unis, avec tous les droits ;
- garder le statut actuel ;
- devenir un pays **indépendant**.
Lors des derniers référendums consultatifs, le statut d'État est arrivé en tête, mais avec une forte abstention, et la décision finale appartient au Congrès américain, qui ne l'a jamais accordée. Ce débat pose la question d'un héritage colonial au sein même des États-Unis.

## Une île dans la tempête
En septembre 2017, l'**ouragan Maria** dévaste l'île. Le réseau électrique est détruit et certaines zones restent sans courant pendant des mois. Selon une étude officielle, près de 3 000 personnes sont mortes des conséquences de la catastrophe. La lenteur des secours fédéraux est vivement critiquée. L'île traverse aussi une grave crise de la dette depuis les années 2010. Beaucoup de Portoricains partent vivre sur le continent : il y a aujourd'hui plus de Portoricains aux États-Unis continentaux (notamment à New York et en Floride) que sur l'île.

## Une culture qui conquiert le monde
L'espagnol est la langue principale, l'anglais est co-officiel. La culture portoricaine, mélange d'héritages taíno, espagnol et africain, rayonne dans le monde : la salsa et le **reggaeton** (Daddy Yankee, Luis Fonsi et le tube *Despacito*), et surtout **Bad Bunny**, l'un des artistes les plus écoutés de la planète, qui chante presque uniquement en espagnol et a assuré le 8 février 2026 le spectacle de la mi-temps du Super Bowl, en grande partie en espagnol. Le créateur de la comédie musicale *Hamilton*, Lin-Manuel Miranda, est d'origine portoricaine.
[→ Voir aussi : les Caraïbes anglophones](cu_caraibes.html)
""", """
an island = une île
a citizen = un citoyen
a state = un État
to vote = voter
a hurricane = un ouragan
electricity = l'électricité
independence = l'indépendance
Spanish = l'espagnol
""", [
 ("Depuis quand Porto Rico est-il un territoire américain ?", ["1898", "1776", "1959"], ""),
 ("Les Portoricains sont-ils citoyens américains ?", ["Oui, depuis 1917", "Non, jamais", "Seulement les enfants"], ""),
 ("Que ne peuvent pas faire les habitants de l'île ?", ["Voter à l'élection présidentielle", "Voyager aux États-Unis", "Parler espagnol"], ""),
 ("Quelles sont les trois options pour le statut de l'île ?", ["51e État, statut actuel ou indépendance", "Royaume, empire ou colonie", "Espagne, France ou Mexique"], ""),
 ("Qu'a provoqué l'ouragan Maria en 2017 ?", ["Des destructions massives et près de 3 000 morts", "Rien de grave", "L'indépendance"], ""),
 ("Quel artiste portoricain est l'un des plus écoutés au monde ?", ["Bad Bunny", "Bob Marley", "Rihanna"], ""),
], [("Taínos", "peuple autochtone des Grandes Antilles"), ("Lin-Manuel Miranda", "auteur et compositeur américain")])
D = "pr"
culture(F, "Culture : Puerto Rico – the 51st state?", 'Puerto <span>Rico</span>',
  "Culture · un territoire américain entre deux mondes", ("#fca5a5", "#1d4ed8"),
  reperes("Porto Rico est un territoire des États-Unis depuis 1898. Ses habitants sont citoyens américains mais ne votent pas pour le président. Doit-il devenir le 51e État ?",
    [("1493", "arrivée de Christophe Colomb"), ("1898", "l'île passe aux États-Unis"), ("1917", "les Portoricains deviennent citoyens américains"),
     ("1952", "Constitution et statut de Commonwealth"), ("2017", "l'ouragan Maria")],
    "a territory, a citizen, statehood, independence, a referendum, a hurricane, a colony, the mainland"),
  {D: doc("American, but not quite", [
    "Puerto Rico is an island in the Caribbean. It was Spanish for 400 years, then it became an American territory in 1898.",
    "Puerto Ricans are American citizens, but they cannot vote for the President, and they have no voting member in Congress.",
    "Some Puerto Ricans want the island to become the 51st American state. Others prefer the current status, and some want independence.",
    "In 2017, Hurricane Maria destroyed a lot of the island. Many people had no electricity for months, and thousands died. Many Puerto Ricans moved to the mainland.",
    "Puerto Rican music is famous all over the world, from salsa to reggaeton. Bad Bunny is one of the most listened-to artists on the planet."])},
  [TF(D, "Puerto Rico was Spanish for 400 years.", True, "« Spanish for 400 years »."),
   TF(D, "Puerto Ricans are not American citizens.", False, "« Puerto Ricans are American citizens »."),
   TF(D, "Puerto Ricans can vote for the President.", False, "« they cannot vote for the President »."),
   TF(D, "Everybody wants independence.", False, "Les avis sont partagés."),
   TF(D, "Hurricane Maria hit the island in 2017.", True, "« In 2017, Hurricane Maria »."),
   TF(D, "Bad Bunny is very famous.", True, "« one of the most listened-to artists »." )],
  [Q(D, "When did Puerto Rico become American?", ["In 1898.", "In 1776.", "In 2017."]),
   Q(D, "What can't Puerto Ricans do?", ["Vote for the President.", "Travel to the USA.", "Speak English."]),
   Q(D, "What do some Puerto Ricans want?", ["To become the 51st state.", "To become Spanish again.", "To leave the Caribbean."]),
   Q(D, "What happened after Hurricane Maria?", ["Many people had no electricity for months.", "Nothing changed.", "The island became a state."])],
  [DT(D, "Quel peuple vivait sur l'île avant les Espagnols ?", ["Les Taínos", "Les Aztèques", "Les Māori", "Les Inuit"]),
   DT(D, "Quel tube de 2017 a fait connaître le reggaeton ?", ["Despacito", "Macarena", "La Bamba", "Gangnam Style"]),
   DT(D, "Comment s'appelle officiellement le statut de l'île ?", ["Commonwealth (État libre associé)", "Dominion", "Colonie royale", "Protectorat"]),
   DT(D, "Comment dit-on « le statut d'État » ?", ["Statehood", "Statement", "Stateship", "Status quo"])],
  [W(D, "Trouve le mot qui veut dire « un territoire ».", "territory"), W(D, "Trouve le mot qui veut dire « le statut actuel » (2 mots).", ["current status", "the current status"]),
   W(D, "Trouve le mot qui veut dire « a détruit ».", "destroyed"), W(D, "Trouve le mot qui veut dire « le continent » (États-Unis).", "mainland")])

# ═════════ MOBILISATIONS ═════════
F = "cu_mobilisations.html"
DZ(F, """
## Les débuts du syndicalisme britannique
En 1834, six ouvriers agricoles du village de Tolpuddle, dans le Dorset, forment une association pour refuser une baisse de leurs salaires. Ils sont condamnés à être déportés en Australie. Une immense pétition de 800 000 signatures obtient leur libération : les **Tolpuddle Martyrs** deviennent les héros du mouvement ouvrier. Dans les années 1830-1840, les **chartistes** réclament le droit de vote pour tous les hommes. En 1868, les syndicats (**trade unions**) se regroupent dans le **TUC**, puis fondent au début du 20e siècle le **Parti travailliste** (Labour Party).

## Grèves historiques
- En 1926, la **grève générale** paralyse le Royaume-Uni pendant neuf jours en soutien aux mineurs.
- En 1984-1985, la **grève des mineurs** contre les fermetures de mines décidées par le gouvernement de Margaret Thatcher dure un an et se termine par la défaite des grévistes. Des films comme *Billy Elliot* ou *Pride* racontent cette période. Le nombre de syndiqués britanniques a ensuite été divisé par deux.
- Aux États-Unis, la répression d'une manifestation pour la journée de huit heures à Chicago en 1886 est à l'origine du **1er mai**, fête internationale des travailleurs. En 1911, l'incendie de l'usine Triangle, à New York, où 146 ouvrières meurent enfermées, conduit à de nouvelles lois de sécurité. Dans les années 1960, **César Chávez** organise les ouvriers agricoles hispaniques de Californie et lance un boycott national du raisin.
- Ces dernières années, les syndicats reviennent dans l'actualité : grèves des scénaristes et acteurs d'Hollywood en 2023, des ouvriers de l'automobile, ou tentatives de syndicalisation chez Amazon et Starbucks.

## Du pavé au hashtag
Au 21e siècle, les mobilisations passent aussi par Internet.
- **Occupy Wall Street** (2011) dénonce les inégalités avec le slogan « *We are the 99%* ».
- **#BlackLivesMatter** (2013) devient un mouvement mondial en 2020.
- **#MeToo** : lancé en 2006 par la militante américaine Tarana Burke, le mot-dièse devient viral en octobre 2017 ; des millions de femmes témoignent de violences sexuelles.
- Les grèves scolaires pour le climat, lancées en 2018 par la jeune Suédoise Greta Thunberg, mobilisent des millions de jeunes dans le monde anglophone.
Les réseaux sociaux permettent de mobiliser très vite, sans organisation lourde, et de donner la parole à ceux qu'on n'entendait pas. Mais on parle aussi de **slacktivism** : cliquer sur « j'aime » ou partager une publication ne suffit pas toujours à changer les choses. Les mouvements les plus efficaces combinent souvent l'action en ligne et la mobilisation dans la rue.
[→ Voir aussi : le monde du travail](cu_travail.html)
""", """
a union = un syndicat
a strike = une grève
a worker = un travailleur
a protest = une manifestation
a petition = une pétition
a wage = un salaire
a hashtag = un mot-dièse
to share = partager
""", [
 ("Pourquoi les Tolpuddle Martyrs sont-ils célèbres ?", ["Condamnés pour avoir formé une association, ils sont libérés grâce à une pétition", "Ce sont des rois", "Ils ont inventé le hashtag"], ""),
 ("Que réclament les chartistes ?", ["Le droit de vote pour tous les hommes", "La fin du football", "Des châteaux"], ""),
 ("Comment se termine la grève des mineurs de 1984-1985 ?", ["Par la défaite des grévistes", "Par leur victoire totale", "Par une guerre"], ""),
 ("D'où vient le 1er mai ?", ["D'une manifestation pour la journée de huit heures à Chicago en 1886", "D'une fête religieuse", "D'une victoire militaire"], ""),
 ("Qu'est-ce que #MeToo ?", ["Un mouvement où des millions de femmes témoignent de violences sexuelles", "Une application", "Un syndicat"], ""),
 ("Qu'est-ce que le « slacktivism » ?", ["Un militantisme en ligne qui ne suffit pas toujours à changer les choses", "Une grève générale", "Une loi"], ""),
], [("TUC", "Trades Union Congress, confédération syndicale britannique"), ("**César Chávez**", "syndicaliste américain, 1927-1993"), ("Tarana Burke", "militante américaine")])
D = "mb"
culture(F, "Culture : From trade unions to hashtags", 'From unions <span>to hashtags</span>',
  "Culture · grèves, syndicats et mobilisations en ligne", ("#fca5a5", "#1f2937"),
  reperes("Des premiers syndicats britanniques aux mouvements nés sur les réseaux sociaux, les formes de mobilisation populaire ont beaucoup changé.",
    [("1834", "les Tolpuddle Martyrs"), ("1886", "Chicago : origine du 1er mai"), ("1926", "grève générale britannique"),
     ("1984 – 1985", "grève des mineurs"), ("2011", "Occupy Wall Street"), ("2017", "#MeToo devient viral")],
    "a trade union, a strike, a protest, a petition, a demand, a movement, a hashtag, to go viral"),
  {D: doc("Raise your voice", [
    "In 1834, six farm workers from Tolpuddle formed a union. They were punished and sent to Australia, but a huge petition helped to free them. Since then, unions have fought for better wages and working conditions.",
    "There were famous strikes in Britain, like the General Strike of 1926 and the miners' strike of 1984-85 against Margaret Thatcher.",
    "In the USA, May Day comes from a protest in Chicago in 1886, when workers asked for an eight-hour day.",
    "Today, many movements start online. #MeToo became viral in 2017, when millions of women shared their stories. Young people also organised school strikes for the climate.",
    "Social media helps people to mobilise quickly, but clicking \"like\" is not always enough to change things."])},
  [TF(D, "The Tolpuddle workers were sent to Australia.", True, "« sent to Australia »."),
   TF(D, "Unions fight for lower wages.", False, "« better wages »."),
   TF(D, "The miners' strike was against Margaret Thatcher.", True, "« against Margaret Thatcher »."),
   TF(D, "May Day comes from a protest in London.", False, "« in Chicago in 1886 »."),
   TF(D, "#MeToo became viral in 2017.", True, "« in 2017 »."),
   TF(D, "Clicking \"like\" always changes things.", False, "« not always enough »." )],
  [Q(D, "What do unions fight for?", ["Better wages and working conditions.", "More taxes.", "Longer days."]),
   Q(D, "What did workers ask for in Chicago in 1886?", ["An eight-hour day.", "More holidays in Australia.", "A new king."]),
   Q(D, "What happened with #MeToo?", ["Millions of women shared their stories.", "A union was created.", "A strike started."]),
   Q(D, "What is the limit of social media?", ["Clicking \"like\" is not always enough.", "It is too slow.", "Nobody uses it."])],
  [DT(D, "Quel parti les syndicats britanniques fondent-ils ?", ["Le Labour Party", "Le Conservative Party", "Le Liberal Party", "Le SNP"]),
   DT(D, "Quel film parle de la grève des mineurs ?", ["Billy Elliot", "Mary Poppins", "Titanic", "Notting Hill"]),
   DT(D, "Qui organise les ouvriers agricoles de Californie ?", ["César Chávez", "Henry Ford", "Martin Luther King", "Tarana Burke"]),
   DT(D, "Comment dit-on « une grève » ?", ["A strike", "A strip", "A stroke", "A street"])],
  [W(D, "Trouve le mot qui veut dire « un syndicat ».", ["union", "a union"]), W(D, "Trouve le mot qui veut dire « libérer ».", "free"),
   W(D, "Trouve le mot qui veut dire « les conditions de travail » (2 mots).", ["working conditions"]), W(D, "Trouve le mot qui veut dire « se mobiliser ».", "mobilise")])

# ═════════ COMPLOTISME ═════════
F = "cu_complotisme.html"
DZ(F, """
## Qu'est-ce qu'une théorie du complot ?
Une **conspiracy theory** affirme qu'un événement important est en réalité organisé en secret par un groupe puissant qui cache la vérité au public. Elle refuse l'explication officielle et prétend révéler ce qu'« on ne vous dit pas ». Ces théories ne sont pas nouvelles, mais Internet et les réseaux sociaux les diffusent aujourd'hui plus vite et plus loin que jamais.

## Quelques théories célèbres
- **Le faux alunissage** : selon cette théorie, les astronautes américains ne seraient jamais allés sur la Lune en 1969, et les images auraient été tournées en studio. Les preuves de ces missions (centaines de kilos de roches lunaires, réflecteurs laser encore utilisés, photos prises depuis l'orbite lunaire) sont pourtant nombreuses.
- **L'assassinat de Kennedy** (1963) : une commission officielle conclut que Lee Harvey Oswald a agi seul, mais une grande partie des Américains croient encore à un complot.
- **Roswell et la Zone 51** : en 1947, un objet s'écrase au Nouveau-Mexique ; l'armée parle d'un ballon, et la rumeur d'extraterrestres cachés par le gouvernement est née. L'objet était un ballon militaire secret de surveillance.
- **La Terre plate**, les « chemtrails », les théories sur le 11 septembre ou sur les vaccins.
- Dans les années 2010, la mouvance **QAnon**, née sur des forums américains, a rassemblé des milliers de personnes autour d'affirmations sans aucune preuve, avec des conséquences bien réelles.

## Pourquoi y croit-on ?
- Les complots offrent une explication simple et rassurante à des événements choquants ou complexes : il y a forcément un coupable.
- La **méfiance** envers les gouvernements, les médias ou les scientifiques. Elle est parfois nourrie par de vrais scandales cachés, comme le Watergate ou l'expérience de Tuskegee, où des médecins américains ont laissé des malades noirs sans traitement pendant des décennies.
- Le **biais de confirmation** : on retient ce qui confirme ce qu'on pense déjà.
- Les **algorithmes** des réseaux sociaux, qui mettent en avant les contenus spectaculaires, et les **bulles de filtre**, où l'on ne voit que des avis semblables au sien.
- Le sentiment d'appartenir à un groupe qui « sait la vérité ».
L'exemple d'Andrew Wakefield, un médecin britannique qui avait publié en 1998 une étude frauduleuse liant un vaccin à l'autisme, montre les dégâts possibles : l'étude a été retirée et lui radié, mais la méfiance envers les vaccins a perduré.

## Comment s'en protéger ?
- Vérifier la **source** : qui parle, avec quelles compétences, dans quel but ?
- Croiser les informations, consulter des sites de **fact-checking**.
- Se méfier des affirmations extraordinaires sans preuves extraordinaires.
- Appliquer le **rasoir d'Ockham** : l'explication la plus simple est souvent la bonne.
- Avec l'intelligence artificielle, les fausses images et vidéos (**deepfakes**) rendent cette vigilance encore plus nécessaire.
[→ Voir aussi : les médias anglophones](cu_medias.html)
""", """
a theory = une théorie
the truth = la vérité
a lie = un mensonge
a source = une source
proof = une preuve
to believe = croire
fake = faux
a rumour = une rumeur
""", [
 ("Qu'affirme une théorie du complot ?", ["Qu'un groupe puissant organise en secret un événement et cache la vérité", "Que la science a toujours raison", "Que tout est un hasard"], ""),
 ("Quelles preuves existent des missions lunaires ?", ["Des roches lunaires, des réflecteurs laser, des photos depuis l'orbite", "Aucune", "Seulement des films"], ""),
 ("Qu'était réellement l'objet de Roswell ?", ["Un ballon militaire secret de surveillance", "Un vaisseau extraterrestre", "Un avion de ligne"], ""),
 ("Qu'est-ce que le biais de confirmation ?", ["Retenir ce qui confirme ce qu'on pense déjà", "Vérifier toutes les sources", "Changer d'avis souvent"], ""),
 ("Pourquoi la méfiance est-elle parfois compréhensible ?", ["De vrais scandales ont été cachés, comme le Watergate", "Parce que tout est faux", "Parce que les médias n'existent pas"], ""),
 ("Comment se protéger des fausses informations ?", ["Vérifier les sources et croiser les informations", "Croire la première vidéo", "Ne rien lire"], ""),
], [("Lee Harvey Oswald", "assassin présumé de Kennedy"), ("Tuskegee", "étude médicale contraire à l'éthique, 1932-1972"), ("Ockham", "philosophe anglais du 14e siècle")])
D = "cp"
culture(F, "Culture : Conspiracy theories", 'Conspiracy <span>theories</span>',
  "Culture · « chacun sa vérité ? » : le défi du complotisme", ("#d4d4d8", "#16a34a"),
  reperes("Les théories du complot se diffusent rapidement sur Internet. Comprendre pourquoi on y croit aide à mieux vérifier l'information.",
    [("1947", "Roswell"), ("1963", "assassinat de Kennedy"), ("1969", "premiers pas sur la Lune"),
     ("1998", "étude frauduleuse sur les vaccins"), ("années 2010", "QAnon et les réseaux sociaux")],
    "a conspiracy theory, evidence, a source, fact-checking, fake news, confirmation bias, a filter bubble, a deepfake"),
  {D: doc("Who can you trust?", [
    "A conspiracy theory says that a powerful group secretly organised an important event and is hiding the truth.",
    "For example, some people believe that the Moon landing in 1969 was filmed in a studio. But there is a lot of evidence that astronauts really went to the Moon.",
    "Why do people believe these theories? They give simple explanations, people don't trust governments, and social media shows us more of what we already think.",
    "Sometimes, governments really did hide things, like the Watergate scandal. This makes some people suspicious of everything.",
    "To protect yourself, check who is speaking, compare different sources and use fact-checking websites. Be careful with photos and videos: they can be fake."])},
  [TF(D, "A conspiracy theory says a secret group is hiding the truth.", True, "« is hiding the truth »."),
   TF(D, "There is no evidence that astronauts went to the Moon.", False, "« a lot of evidence »."),
   TF(D, "Conspiracy theories give simple explanations.", True, "« They give simple explanations »."),
   TF(D, "Governments never hid anything.", False, "« governments really did hide things »."),
   TF(D, "You should compare different sources.", True, "« compare different sources »."),
   TF(D, "Photos and videos are always real.", False, "« they can be fake »." )],
  [Q(D, "What do some people believe about the Moon landing?", ["It was filmed in a studio.", "It happened twice.", "It was in 2020."]),
   Q(D, "Why do people believe conspiracy theories?", ["They give simple explanations.", "They are always true.", "Teachers recommend them."]),
   Q(D, "Why are some people suspicious?", ["Governments sometimes hid real scandals.", "They love governments.", "They never use the Internet."]),
   Q(D, "How can you protect yourself?", ["Check sources and use fact-checking websites.", "Share everything.", "Believe the first video."])],
  [DT(D, "Comment s'appelle la mouvance conspirationniste née vers 2017 ?", ["QAnon", "Occupy", "#MeToo", "Anonymous"]),
   DT(D, "Comment appelle-t-on les fausses vidéos créées par IA ?", ["Des deepfakes", "Des selfies", "Des memes", "Des podcasts"]),
   DT(D, "Où se trouve Roswell ?", ["Au Nouveau-Mexique", "Au Texas", "En Floride", "Au Nevada"]),
   DT(D, "Comment dit-on « digne de confiance » ?", ["Trustworthy", "Trustful", "Truth", "Trusty-full"])],
  [W(D, "Trouve le mot qui veut dire « secrètement ».", "secretly"), W(D, "Trouve le mot qui veut dire « des preuves ».", "evidence"),
   W(D, "Trouve le mot qui veut dire « méfiants ».", "suspicious"), W(D, "Trouve le mot qui veut dire « faux ».", "fake")])

# ═════════ JEUX VIDÉO ═════════
F = "cu_jeux_video.html"
DZ(F, """
## Une invention américaine
Les premiers jeux vidéo naissent dans des laboratoires américains : *Tennis for Two* (1958) sur un écran d'oscilloscope, puis *Spacewar!* (1962) au MIT. En 1972, la société **Atari** lance *Pong*, une simple partie de tennis électronique, et crée l'industrie du jeu vidéo. Après un effondrement du marché en 1983, l'entreprise japonaise **Nintendo** relance le secteur, et le jeu vidéo devient un dialogue permanent entre le Japon et le monde anglophone.

## Une industrie géante
Aujourd'hui, le jeu vidéo rapporte plus d'argent que le cinéma et la musique réunis. Les États-Unis y occupent une place centrale : **Microsoft** (Xbox, depuis 2001), **Electronic Arts** (jeux de sport), **Activision** (*Call of Duty*), **Epic Games** (*Fortnite*, 2017). Microsoft a racheté *Minecraft*, créé en Suède, puis Activision Blizzard. Le Royaume-Uni est aussi une grande puissance : la série *Grand Theft Auto* (**GTA**), l'une des plus vendues de l'histoire, est développée par Rockstar North à Édimbourg, et *Tomb Raider* est né à Derby. L'**e-sport** remplit des stades et attire des millions de spectateurs en ligne.

## Un instrument de soft power
Les jeux vidéo diffusent dans le monde entier des images, des valeurs et des récits souvent américains : les villes des États-Unis reconstituées dans *GTA*, les super-héros, l'armée américaine dans les jeux de guerre. En 2002, l'armée américaine a même créé son propre jeu, *America's Army*, comme outil de recrutement. Le jeu vidéo façonne l'imaginaire des jeunes comme le cinéma hollywoodien l'a fait au 20e siècle : on parle de **soft power**. Des pays comme la Chine, la Corée du Sud ou la Pologne développent aujourd'hui leurs propres jeux pour concurrencer cette influence.

## Les débats
- **La violence** : depuis les années 1990, certains accusent les jeux violents de rendre les jeunes agressifs ; les études scientifiques ne montrent pas de lien clair avec les actes violents.
- **L'addiction** : l'Organisation mondiale de la santé a reconnu en 2019 le « trouble du jeu vidéo » (**gaming disorder**) pour les cas graves.
- **Les loot boxes**, coffres virtuels payants au contenu aléatoire, sont comparées à des jeux d'argent et ont été interdites ou encadrées dans certains pays.
- **La représentation** : les femmes et les minorités ont longtemps été absentes ou caricaturées ; les jeux se diversifient, mais les débats restent vifs.
- **Mais aussi** : les jeux développent la créativité (*Minecraft* est utilisé dans des écoles), la coopération, l'anglais des joueurs du monde entier… et sont reconnus comme une forme d'art et de narration.
[→ Voir aussi : la Silicon Valley](cu_silicon_valley.html)
""", """
a video game = un jeu vidéo
a player = un joueur
a screen = un écran
to play = jouer
a console = une console
a level = un niveau
violent = violent
an industry = une industrie
""", [
 ("Quel jeu lance l'industrie du jeu vidéo en 1972 ?", ["Pong", "Fortnite", "Minecraft"], ""),
 ("Pourquoi dit-on que le jeu vidéo est une industrie géante ?", ["Il rapporte plus que le cinéma et la musique réunis", "Il emploie tout le monde", "Il est gratuit"], ""),
 ("Où est développé GTA ?", ["À Édimbourg, par Rockstar North", "À Tokyo", "À Paris"], ""),
 ("Pourquoi parle-t-on de soft power ?", ["Les jeux diffusent des images et des valeurs souvent américaines", "Les jeux sont doux", "Les jeux sont interdits"], ""),
 ("Que disent les études sur les jeux violents ?", ["Elles ne montrent pas de lien clair avec les actes violents", "Ils rendent tout le monde violent", "Ils rendent pacifique"], ""),
 ("Pourquoi les loot boxes sont-elles critiquées ?", ["Elles ressemblent à des jeux d'argent", "Elles sont gratuites", "Elles sont trop lentes"], ""),
], [("MIT", "Massachusetts Institute of Technology"), ("Atari", "entreprise américaine pionnière du jeu vidéo")])
D = "jv"
culture(F, "Culture : Video games and soft power", 'Video <span>games</span>',
  "Culture · une industrie géante et une nouvelle forme de soft power", ("#a5b4fc", "#16a34a"),
  reperes("Né aux États-Unis, le jeu vidéo est devenu une industrie plus puissante que le cinéma et un outil d'influence culturelle.",
    [("1958", "Tennis for Two"), ("1972", "Pong d'Atari"), ("2001", "la Xbox de Microsoft"),
     ("2002", "America's Army, jeu de l'armée américaine"), ("2017", "Fortnite"), ("2019", "l'OMS reconnaît le « gaming disorder »")],
    "a video game, a gamer, a console, e-sports, an industry, soft power, addiction, a loot box"),
  {D: doc("Game on", [
    "The first video games were created in American laboratories. In 1972, Atari launched Pong, a simple tennis game, and the video game industry was born.",
    "Today, video games make more money than films and music together. American companies like Microsoft and Epic Games, and British studios like Rockstar North, are very powerful.",
    "Video games spread American images and values all over the world, like Hollywood films. This is a form of soft power. The US Army even created its own game to recruit soldiers.",
    "Some people worry about violence, addiction and loot boxes, which look like gambling.",
    "But games can also develop creativity and cooperation, and many players learn English while playing online."])},
  [TF(D, "The first video games were created in Japan.", False, "« in American laboratories »."),
   TF(D, "Pong was a tennis game.", True, "« a simple tennis game »."),
   TF(D, "Video games make less money than films.", False, "« more money than films and music together »."),
   TF(D, "The US Army created its own video game.", True, "« created its own game »."),
   TF(D, "Loot boxes look like gambling.", True, "« look like gambling »."),
   TF(D, "Players can learn English while playing online.", True, "« learn English while playing online »." )],
  [Q(D, "What was Pong?", ["A simple tennis game.", "A football game.", "A war game."]),
   Q(D, "Why are video games a form of soft power?", ["They spread American images and values.", "They are soft.", "They are cheap."]),
   Q(D, "Why did the US Army create a game?", ["To recruit soldiers.", "To make money.", "To teach maths."]),
   Q(D, "What are the positive sides of games?", ["Creativity, cooperation and learning English.", "Nothing.", "Only money."])],
  [DT(D, "Quelle entreprise japonaise relance le jeu vidéo après 1983 ?", ["Nintendo", "Sony", "Sega", "Atari"]),
   DT(D, "Dans quelle ville est développé GTA ?", ["Édimbourg", "Londres", "Los Angeles", "Montréal"]),
   DT(D, "Quel jeu suédois Microsoft a-t-il racheté ?", ["Minecraft", "Fortnite", "Tetris", "Pong"]),
   DT(D, "Comment dit-on « jeux d'argent » ?", ["Gambling", "Money games", "Betting box", "Gaming"])],
  [W(D, "Trouve le mot qui veut dire « a lancé ».", "launched"), W(D, "Trouve le mot qui veut dire « recruter ».", "recruit"),
   W(D, "Trouve le mot qui veut dire « la dépendance ».", "addiction"), W(D, "Trouve le mot qui veut dire « la créativité ».", "creativity")])

# ═════════ IA & ÉCOLE ═════════
F = "cu_ia_ecole.html"
DZ(F, """
## Novembre 2022 : le choc ChatGPT
Le 30 novembre 2022, l'entreprise américaine **OpenAI**, basée à San Francisco, rend public **ChatGPT**, un agent conversationnel capable de répondre à des questions, de rédiger des textes, de résumer, de traduire ou de coder. En deux mois, il atteint 100 millions d'utilisateurs, un record. Les écoles et universités du monde anglophone sont parmi les premières à réagir.

## Interdire ou apprendre à s'en servir ?
- Dans un premier temps, certaines institutions **interdisent** l'outil : les écoles publiques de New York le bloquent en janvier 2023… avant de revenir sur leur décision quelques mois plus tard.
- Les universités britanniques et américaines publient des règles : l'utilisation de l'IA peut être autorisée, encadrée ou interdite selon les devoirs, et doit souvent être déclarée.
- Les gouvernements, comme le ministère de l'Éducation anglais, publient des recommandations : l'IA peut aider les enseignants à préparer des cours ou à alléger certaines tâches, mais ne doit pas remplacer le jugement humain.
- Des plateformes éducatives développent des **AI tutors**, des tuteurs virtuels qui guident l'élève par des questions plutôt que de donner directement la réponse.

## Les promesses
- Un accompagnement personnalisé, disponible à toute heure, adapté au rythme de chaque élève.
- Une aide pour les élèves en difficulté, ou ayant des besoins particuliers (lecture, traduction, reformulation).
- Un gain de temps pour les enseignants.
- La possibilité d'apprendre à poser de bonnes questions et à vérifier les réponses : la **AI literacy** (culture de l'IA) devient une compétence enseignée.

## Les risques
- **La triche** : rendre un devoir écrit par une machine. Les logiciels censés détecter les textes d'IA sont peu fiables et peuvent accuser à tort ; certains enseignants reviennent aux devoirs faits en classe et aux oraux.
- **Les erreurs** : l'IA peut inventer des faits avec assurance (on parle d'**hallucinations**) ; il faut toujours vérifier.
- **La dépendance** : si l'outil pense à notre place, apprend-on encore à écrire, à raisonner, à mémoriser ?
- **Les inégalités** entre élèves qui ont accès à des outils performants et les autres.
- **Les données personnelles** des élèves et les **biais** reproduits par les systèmes.

## Une vieille question
En 1950, le Britannique **Alan Turing** se demandait déjà si une machine pouvait « penser ». À l'école, la question devient : à quoi sert d'apprendre ce qu'une machine sait faire ? Pour beaucoup d'enseignants, la réponse est claire : pour comprendre, pour exercer son esprit critique, et pour rester maître de l'outil plutôt que l'inverse.
[→ Voir aussi : les sciences et les inventions](cu_sciences.html)
""", """
artificial intelligence = l'intelligence artificielle
a chatbot = un agent conversationnel
homework = les devoirs
to cheat = tricher
a mistake = une erreur
to check = vérifier
a tool = un outil
a teacher = un enseignant
""", [
 ("Quand ChatGPT est-il rendu public ?", ["Fin novembre 2022", "En 1950", "En 2010"], ""),
 ("Comment ont réagi les écoles publiques de New York ?", ["Elles l'ont interdit, puis sont revenues sur leur décision", "Elles l'ont rendu obligatoire", "Elles n'ont rien fait"], ""),
 ("Qu'est-ce qu'un AI tutor ?", ["Un tuteur virtuel qui guide l'élève par des questions", "Un professeur robot dans la classe", "Un logiciel de triche"], ""),
 ("Que sont les « hallucinations » de l'IA ?", ["Des faits inventés présentés avec assurance", "Des rêves", "Des images"], ""),
 ("Pourquoi les détecteurs de textes d'IA posent-ils problème ?", ["Ils sont peu fiables et peuvent accuser à tort", "Ils sont trop chers", "Ils n'existent pas"], ""),
 ("Pourquoi apprendre ce qu'une machine sait faire ?", ["Pour comprendre, exercer son esprit critique et maîtriser l'outil", "Ce n'est plus utile", "Pour remplacer la machine"], ""),
], [("OpenAI", "entreprise américaine d'intelligence artificielle"), ("**Alan Turing**", "mathématicien britannique, 1912-1954")])
D = "ai"
culture(F, "Culture : AI at school", 'AI <span>at school</span>',
  "Culture · l'intelligence artificielle et l'apprentissage dans le monde anglophone", ("#c7d2fe", "#0f766e"),
  reperes("Depuis la sortie de ChatGPT en 2022, les écoles anglophones se demandent comment utiliser l'intelligence artificielle sans renoncer à apprendre.",
    [("1950", "Turing se demande si une machine peut penser"), ("30 novembre 2022", "sortie de ChatGPT"), ("janvier 2023", "New York bloque ChatGPT dans ses écoles"),
     ("2023 →", "règles et recommandations des universités et des gouvernements")],
    "artificial intelligence, a chatbot, a prompt, to cheat, a tutor, a hallucination, critical thinking, AI literacy"),
  {D: doc("Homework 2.0", [
    "In November 2022, the American company OpenAI launched ChatGPT. It can answer questions and write texts in a few seconds. Students started using it immediately.",
    "At first, some schools banned it because they were afraid of cheating. Then, many decided it was better to teach students how to use it well.",
    "AI can help students: it can explain a lesson again, translate, or give examples. It can also help teachers to save time.",
    "But AI makes mistakes. It sometimes invents facts, so you must always check. And if AI does all the work, you don't learn anything.",
    "Many teachers think the most important skill today is critical thinking: understanding, checking and staying in control of the tool."])},
  [TF(D, "ChatGPT was launched in November 2022.", True, "« In November 2022 »."),
   TF(D, "All schools welcomed ChatGPT immediately.", False, "« some schools banned it »."),
   TF(D, "AI can help teachers to save time.", True, "« help teachers to save time »."),
   TF(D, "AI never makes mistakes.", False, "« AI makes mistakes »."),
   TF(D, "You should always check what AI says.", True, "« you must always check »."),
   TF(D, "If AI does all the work, you learn a lot.", False, "« you don't learn anything »." )],
  [Q(D, "Why did some schools ban ChatGPT?", ["They were afraid of cheating.", "It was too expensive.", "It was too slow."]),
   Q(D, "How can AI help students?", ["It can explain a lesson again or give examples.", "It can do their sport.", "It can sleep for them."]),
   Q(D, "What is the problem with AI?", ["It sometimes invents facts.", "It is always right.", "It cannot write."]),
   Q(D, "What is the most important skill today, according to many teachers?", ["Critical thinking.", "Typing fast.", "Copying."])],
  [DT(D, "Quelle entreprise a créé ChatGPT ?", ["OpenAI", "Google", "Apple", "BBC"]),
   DT(D, "Quel savant britannique s'est demandé en 1950 si une machine peut penser ?", ["Alan Turing", "Isaac Newton", "Charles Darwin", "Tim Berners-Lee"]),
   DT(D, "Comment appelle-t-on les erreurs inventées par l'IA ?", ["Des hallucinations", "Des bugs de vision", "Des rêves", "Des selfies"]),
   DT(D, "Comment dit-on « tricher » ?", ["To cheat", "To chat", "To chase", "To check"])],
  [W(D, "Trouve le mot qui veut dire « immédiatement ».", "immediately"), W(D, "Trouve le mot qui veut dire « ont interdit ».", "banned"),
   W(D, "Trouve le mot qui veut dire « invente ».", "invents"), W(D, "Trouve le mot qui veut dire « l'esprit critique » (2 mots).", ["critical thinking"])])

# ═════════ BEAUTÉ ═════════
F = "cu_beaute.html"
DZ(F, """
## Les Préraphaélites et la beauté victorienne
En 1848, de jeunes peintres anglais, dont **Dante Gabriel Rossetti** et **John Everett Millais**, fondent la **Pre-Raphaelite Brotherhood**. Ils veulent retrouver les couleurs vives et la sincérité des peintres d'avant Raphaël. Leurs tableaux imposent un idéal féminin : peau très pâle, longue chevelure ondulée souvent rousse, cou allongé, regard mélancolique, inspiré des héroïnes de légendes et de Shakespeare. Pour *Ophelia* (1851-1852), Millais fait poser son modèle, Elizabeth Siddal, pendant des heures dans une baignoire ; elle en tombe malade. À la même époque, la mode victorienne impose aux femmes le **corset**, qui serre la taille au risque d'abîmer la santé.

## Le 20e siècle : des canons qui changent
Chaque époque a ses normes : les **flappers** aux cheveux courts des années 1920, les stars glamour d'Hollywood, la silhouette très mince du mannequin britannique **Twiggy** dans les années 1960, les « supermodels » des années 1990. En 1959, la poupée **Barbie**, créée par l'Américaine Ruth Handler, impose une silhouette irréaliste à des générations d'enfants ; en 2016, elle est déclinée en plusieurs morphologies, et le film *Barbie* (2023) joue avec ces clichés.

## Les concours de beauté
Le concours **Miss America** naît en 1921 à Atlantic City, d'abord pour attirer les touristes après l'été. En 1968, des militantes féministes manifestent devant le concours : elles jettent dans une « poubelle de la liberté » des symboles de l'oppression des femmes (soutiens-gorge, faux cils, talons hauts), dénonçant un spectacle qui juge les femmes comme du bétail. Les **beauty pageants** existent toujours, notamment pour les enfants aux États-Unis, ce qui fait débat, mais beaucoup ont supprimé l'épreuve en maillot de bain et mettent en avant les talents et l'engagement des candidates.

## L'ère des filtres
Aujourd'hui, les réseaux sociaux diffusent des images retouchées en permanence : **filters**, applications de retouche, poses étudiées. Beaucoup de jeunes comparent leur apparence à ces images irréalistes, ce qui peut nuire à l'estime de soi. Des réactions apparaissent :
- la campagne *Real Beauty* de la marque Dove (2004) montre des femmes de tous âges et de toutes morphologies ;
- le mouvement **body positivity** revendique l'acceptation de tous les corps ;
- au Royaume-Uni, l'autorité de la publicité a interdit des publicités trop retouchées ;
- la mode met davantage en avant la diversité des couleurs de peau, des tailles, des âges et des handicaps.

## La beauté, une construction
Les normes de beauté ne sont pas naturelles : elles dépendent des époques, des cultures, de l'économie (la mode, les cosmétiques) et des rapports de pouvoir. La mode peut aussi servir à **revendiquer** : les suffragettes en blanc, les punks, les vêtements qui affirment une identité culturelle ou religieuse.
[→ Voir aussi : portraits et autoportraits](cu_portraits.html)
""", """
beauty = la beauté
beautiful = beau, belle
a model = un mannequin, un modèle
a painting = un tableau
hair = les cheveux
a filter = un filtre
a body = un corps
fashion = la mode
""", [
 ("Quel idéal féminin imposent les Préraphaélites ?", ["Peau pâle, longue chevelure ondulée, regard mélancolique", "Cheveux courts et peau bronzée", "Aucun"], ""),
 ("Que montre l'histoire d'Ophelia de Millais ?", ["Le modèle tombe malade après avoir posé des heures dans une baignoire", "Un portrait de la reine", "Un paysage"], ""),
 ("Que critique-t-on à Barbie ?", ["Sa silhouette irréaliste", "Sa couleur", "Son prix"], ""),
 ("Que font les féministes devant Miss America en 1968 ?", ["Elles jettent des symboles de l'oppression dans une « poubelle de la liberté »", "Elles gagnent le concours", "Elles chantent"], ""),
 ("Quel effet peuvent avoir les filtres sur les réseaux sociaux ?", ["Nuire à l'estime de soi par des images irréalistes", "Rendre tout le monde heureux", "Aucun effet"], ""),
 ("Pourquoi dit-on que la beauté est une construction ?", ["Les normes dépendent des époques, des cultures et de l'économie", "Elle est naturelle", "Elle ne change jamais"], ""),
], [("Raphaël", "peintre italien de la Renaissance"), ("**Twiggy**", "mannequin britannique des années 1960")])
D = "be"
culture(F, "Culture : Beauty standards", 'Beauty <span>standards</span>',
  "Culture · des Préraphaélites aux filtres", ("#fbcfe8", "#7c2d12"),
  reperes("Des peintres préraphaélites aux réseaux sociaux, les normes de beauté changent selon les époques. Elles sont aujourd'hui remises en question.",
    [("1848", "la Pre-Raphaelite Brotherhood"), ("1921", "premier concours Miss America"), ("1959", "la poupée Barbie"),
     ("1968", "manifestation féministe devant Miss America"), ("2004", "la campagne Real Beauty")],
    "a beauty standard, a model, appearance, a filter, self-esteem, body positivity, diversity, fashion"),
  {D: doc("Mirror, mirror", [
    "In the 19th century, the Pre-Raphaelite painters showed women with pale skin, long wavy hair and a sad look. This became an ideal of beauty.",
    "Beauty standards change all the time. In the 1920s, women cut their hair short. In the 1960s, the model Twiggy was very thin.",
    "The Miss America beauty pageant started in 1921. In 1968, feminists protested against it, because they said it judged women only on their bodies.",
    "Today, social media is full of filters and edited photos. Many young people compare themselves to these unrealistic images, and they can feel bad about themselves.",
    "But things are changing: more brands show people of all sizes, ages and colours. Many people now say that beauty is diverse."])},
  [TF(D, "The Pre-Raphaelites painted women with short hair.", False, "« long wavy hair »."),
   TF(D, "Beauty standards never change.", False, "« change all the time »."),
   TF(D, "Twiggy was a model in the 1960s.", True, "« In the 1960s, the model Twiggy »."),
   TF(D, "Feminists protested against Miss America in 1968.", True, "« In 1968, feminists protested »."),
   TF(D, "Filters show realistic images.", False, "« unrealistic images »."),
   TF(D, "More brands show people of all sizes.", True, "« people of all sizes, ages and colours »." )],
  [Q(D, "What did Pre-Raphaelite women look like?", ["Pale skin, long wavy hair and a sad look.", "Short hair and big smiles.", "Tanned skin."]),
   Q(D, "Why did feminists protest in 1968?", ["The pageant judged women only on their bodies.", "They wanted to win.", "It was too long."]),
   Q(D, "What is the problem with filters?", ["People compare themselves to unrealistic images.", "They are too expensive.", "They are illegal."]),
   Q(D, "What is changing today?", ["Brands show more diversity.", "Nothing.", "Filters are banned everywhere."])],
  [DT(D, "Qui a peint Ophelia ?", ["John Everett Millais", "J. M. W. Turner", "Andy Warhol", "Hans Holbein"]),
   DT(D, "Qui a créé Barbie ?", ["Ruth Handler", "Twiggy", "Greta Gerwig", "Coco Chanel"]),
   DT(D, "Dans quelle ville naît Miss America ?", ["Atlantic City", "Los Angeles", "Las Vegas", "Miami"]),
   DT(D, "Comment dit-on « l'estime de soi » ?", ["Self-esteem", "Self-service", "Self-love only", "Self-beauty"])],
  [W(D, "Trouve le mot qui veut dire « ondulés ».", "wavy"), W(D, "Trouve le mot qui veut dire « maigre, mince ».", "thin"),
   W(D, "Trouve le mot qui veut dire « irréalistes ».", "unrealistic"), W(D, "Trouve le mot qui veut dire « variée, diverse ».", "diverse")])

# ═════════ ÉCOSSE : ÉNERGIE, GLASGOW, ÉDIMBOURG ═════════
F = "cu_ecosse_auj.html"
DZ(F, """
## Du pétrole au vent : l'énergie écossaise
Au début des années 1970, on découvre d'importants gisements de **pétrole** et de gaz en **mer du Nord**, au large de l'Écosse. **Aberdeen** devient la capitale européenne du pétrole. Les nationalistes écossais lancent alors le slogan « *It's Scotland's oil* », affirmant que cette richesse devrait profiter d'abord à l'Écosse. Mais les gisements s'épuisent et le pétrole contribue au réchauffement climatique.
L'Écosse est aujourd'hui une pionnière des **renewable energies** : ses vents puissants alimentent d'immenses parcs éoliens, sur terre comme en mer ; elle teste l'énergie des marées dans le détroit de Pentland, et utilise l'hydroélectricité de ses lochs. Certaines années, elle produit en énergies renouvelables l'équivalent de la quasi-totalité de sa consommation d'électricité. Elle vise la neutralité carbone en 2045. Le défi : reconvertir les travailleurs du pétrole sans abandonner les régions qui en dépendent.

## Glasgow, la ville ouvrière qui s'est réinventée
**Glasgow**, la plus grande ville d'Écosse, a été au 19e siècle la « deuxième ville de l'Empire ». Sur les rives de la **Clyde**, ses chantiers construisaient une grande partie des navires du monde, dont les paquebots *Queen Mary* et *Queen Elizabeth 2*. La désindustrialisation de la seconde moitié du 20e siècle provoque chômage et pauvreté. La ville se réinvente par la culture : capitale européenne de la culture en 1990, musées, musique (de nombreux groupes de rock), design. Elle a accueilli la conférence sur le climat **COP26** en 2021 et les Jeux du Commonwealth en 2014 et 2026. Les Glaswegians sont réputés pour leur humour et leur chaleur. La rivalité footballistique entre le **Celtic** (associé historiquement aux catholiques d'origine irlandaise) et les **Rangers** (protestants) est l'une des plus intenses du monde.

## Édimbourg, la capitale
**Édimbourg**, capitale de l'Écosse, est dominée par son château construit sur un ancien volcan. Sa vieille ville médiévale et sa « nouvelle ville » géorgienne du 18e siècle sont classées au patrimoine mondial de l'UNESCO. Chaque mois d'août, l'**Edinburgh Festival Fringe**, créé en 1947, en fait le plus grand festival des arts du monde. La ville est un centre financier, universitaire et politique : depuis 1999, elle accueille le **Parlement écossais**, à Holyrood. J. K. Rowling y a écrit les premiers *Harry Potter*.

## Un royaume toujours uni ?
En 2014, les Écossais votent à 55 % contre l'indépendance. Mais en 2016, ils votent à 62 % contre le Brexit, que le Royaume-Uni décide pourtant. Le Scottish National Party réclame depuis un nouveau référendum, que Londres refuse. La question de l'indépendance reste ouverte et divise les Écossais.
[→ Voir aussi : l'Écosse et le pays de Galles](cu_ecosse_galles.html)
""", """
oil = le pétrole
wind = le vent
energy = l'énergie
a ship = un navire
a capital = une capitale
a castle = un château
a festival = un festival
independence = l'indépendance
""", [
 ("Que devient Aberdeen dans les années 1970 ?", ["La capitale européenne du pétrole", "Une ville fantôme", "La capitale de l'Écosse"], ""),
 ("Pourquoi l'Écosse est-elle pionnière des énergies renouvelables ?", ["Grâce à ses vents, ses marées et ses lochs", "Grâce à son soleil", "Grâce au charbon"], ""),
 ("Pour quoi Glasgow était-elle célèbre au 19e siècle ?", ["Ses chantiers navals sur la Clyde", "Ses vignes", "Ses plages"], ""),
 ("Comment Glasgow s'est-elle réinventée ?", ["Par la culture, la musique et le design", "En construisant des mines", "En devenant capitale"], ""),
 ("Qu'est-ce que le Fringe ?", ["Le plus grand festival des arts du monde, à Édimbourg", "Un club de football", "Un parti politique"], ""),
 ("Pourquoi la question de l'indépendance revient-elle après 2016 ?", ["Les Écossais ont voté contre le Brexit, qui a pourtant eu lieu", "L'Écosse a gagné la Coupe du monde", "Le pétrole a disparu"], ""),
], [("Pentland", "détroit au nord de l'Écosse"), ("Holyrood", "quartier d'Édimbourg où siège le Parlement écossais")])
D = "es"
culture(F, "Culture : Scotland today – energy, Glasgow and Edinburgh", 'Scotland <span>today</span>',
  "Culture · énergie, Glasgow et Édimbourg, indépendance", ("#bfdbfe", "#1e3a8a"),
  reperes("L'Écosse passe du pétrole aux énergies renouvelables. Glasgow la ville ouvrière et Édimbourg la capitale montrent deux visages d'un pays qui débat de son indépendance.",
    [("1947", "premier Edinburgh Festival Fringe"), ("années 1970", "pétrole de la mer du Nord"), ("1990", "Glasgow, capitale européenne de la culture"),
     ("1999", "Parlement écossais"), ("2014", "55 % contre l'indépendance"), ("2045", "objectif de neutralité carbone")],
    "oil, renewable energy, a wind farm, a shipyard, deindustrialisation, a festival, a parliament, independence"),
  {D: doc("Two cities, one nation", [
    "In the 1970s, oil was discovered in the North Sea, near Scotland. Aberdeen became the oil capital of Europe.",
    "Today, Scotland produces a lot of renewable energy, especially from the wind. It wants to reach net zero by 2045.",
    "Glasgow is Scotland's biggest city. It was famous for building ships. When the industry disappeared, the city reinvented itself through culture and music.",
    "Edinburgh is the capital. It has a castle on an old volcano and the biggest arts festival in the world every August. The Scottish Parliament is there.",
    "In 2014, most Scots voted to stay in the UK. But after Brexit, the question of independence came back."])},
  [TF(D, "Oil was discovered in the North Sea in the 1970s.", True, "« In the 1970s »."),
   TF(D, "Scotland produces no renewable energy.", False, "« a lot of renewable energy »."),
   TF(D, "Glasgow is the capital of Scotland.", False, "C'est Édimbourg."),
   TF(D, "Glasgow was famous for building ships.", True, "« famous for building ships »."),
   TF(D, "Edinburgh's festival takes place every August.", True, "« every August »."),
   TF(D, "In 2014, most Scots voted for independence.", False, "« most Scots voted to stay »." )],
  [Q(D, "What became Aberdeen?", ["The oil capital of Europe.", "The capital of Scotland.", "A ski resort."]),
   Q(D, "Where does Scotland's renewable energy mostly come from?", ["The wind.", "The sun.", "Coal."]),
   Q(D, "How did Glasgow reinvent itself?", ["Through culture and music.", "By building more ships.", "By becoming the capital."]),
   Q(D, "What happened after Brexit?", ["The question of independence came back.", "Scotland joined France.", "Nothing."])],
  [DT(D, "Sur quel fleuve se trouvaient les chantiers de Glasgow ?", ["La Clyde", "La Tamise", "La Tweed", "Le Forth"]),
   DT(D, "Quel grand événement climatique Glasgow a-t-elle accueilli en 2021 ?", ["La COP26", "Le G7", "Les JO", "L'Eurovision"]),
   DT(D, "Où siège le Parlement écossais ?", ["À Holyrood, Édimbourg", "À Glasgow", "À Westminster", "À Aberdeen"]),
   DT(D, "Comment dit-on « un parc éolien » ?", ["A wind farm", "A wind park", "A windmill garden", "An air farm"])],
  [W(D, "Trouve le mot qui veut dire « a été découvert » (2 mots).", ["was discovered"]), W(D, "Trouve le mot qui veut dire « renouvelable ».", "renewable"),
   W(D, "Trouve le mot qui veut dire « s'est réinventée » (2 mots).", ["reinvented itself"]), W(D, "Trouve le mot qui veut dire « rester ».", "stay")])
END()
