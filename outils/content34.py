import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
exec(open(_EA_OUT+"/cuhelp.py", encoding="utf-8").read())

# ═════════ ORWELL ═════════
F = "cu_orwell.html"
DZ(F, """
## Eric Blair devient George Orwell
**George Orwell** est le nom de plume d'**Eric Arthur Blair**, né en 1903 en Inde, où son père travaille pour l'administration coloniale britannique. Élève boursier à **Eton**, il ne va pas à l'université : à 19 ans, il devient policier impérial en **Birmanie** (aujourd'hui le Myanmar). Il y découvre de près la violence de la domination coloniale, qu'il racontera dans l'essai *Shooting an Elephant*. En 1927, il démissionne, écœuré.

## Vivre avec les pauvres
Orwell décide de partager la vie des plus pauvres. Il travaille comme plongeur dans les cuisines d'hôtels parisiens et vit parmi les vagabonds de Londres : c'est *Down and Out in Paris and London* (1933). En 1936, il enquête sur les mineurs du nord de l'Angleterre pour *The Road to Wigan Pier* (1937). Il devient socialiste, convaincu que la société doit être plus juste.

## La guerre d'Espagne : la naissance d'un anti-totalitaire
Fin 1936, il part combattre en **Espagne** contre l'armée de Franco, dans une milice de gauche. Il est blessé d'une balle à la gorge. Surtout, il voit les communistes soutenus par Staline pourchasser et emprisonner d'autres militants de gauche, et la propagande mentir sur ce qui se passe. Il le raconte dans *Homage to Catalonia* (1938). Dès lors, il dénonce tous les **totalitarianisms**, de droite comme de gauche : le nazisme, mais aussi le stalinisme, à une époque où beaucoup d'intellectuels refusent de critiquer l'URSS.

## Animal Farm (1945)
Dans cette fable, les animaux de la ferme Manor chassent leur fermier ivrogne et prennent le pouvoir au nom de l'égalité. Mais les cochons, menés par **Napoleon**, accaparent peu à peu tous les privilèges, réécrivent les règles et terrorisent les autres animaux avec des chiens. Le commandement final devient célèbre : tous les animaux sont égaux, mais certains sont plus égaux que d'autres. C'est une allégorie de la révolution russe trahie par Staline. Plusieurs éditeurs refusent d'abord le livre, car l'URSS est alors l'alliée du Royaume-Uni dans la guerre.

## Nineteen Eighty-Four (1949)
Malade de la tuberculose, Orwell écrit son dernier roman sur l'île écossaise de Jura. En 1984, le monde est divisé en trois super-États en guerre permanente. À Londres, en **Oceania**, le Parti contrôle tout. Partout, des affiches proclament « ***Big Brother is watching you*** », et des **telescreens** observent chacun jusque chez lui. **Winston Smith** travaille au **Ministry of Truth**, où il réécrit les archives pour que le passé corresponde toujours à ce que dit le Parti. La **Thought Police** traque les pensées interdites. Le Parti invente une langue appauvrie, la **Newspeak** (novlangue), pour rendre impossible toute pensée critique, et impose la **doublethink**, la capacité de croire deux choses contradictoires à la fois, comme le montrent ses slogans : « *War is peace. Freedom is slavery. Ignorance is strength.* » Winston tombe amoureux de Julia et tente de résister, mais ils sont arrêtés et brisés dans la terrible **Room 101**.
Orwell meurt en janvier 1950, à 46 ans.

## Un héritage vivant
L'adjectif **Orwellian** (orwellien) désigne aujourd'hui toute société de surveillance et de manipulation. L'émission de téléréalité *Big Brother* (1999) a repris son nom. Chaque fois que l'on parle de caméras de surveillance, de données personnelles, de fausses informations ou de « faits alternatifs », on cite Orwell, et les ventes de *1984* remontent. Dans un essai de 1946, *Politics and the English Language*, il conseille aussi d'écrire simplement et clairement, pour ne pas se laisser manipuler par le langage.
[→ Voir aussi : les dystopies](cu_dystopies.html)
""", """
a writer = un écrivain
a pig = un cochon
a farm = une ferme
the truth = la vérité
a lie = un mensonge
a camera = une caméra
the past = le passé
to watch = surveiller, regarder
""", [
 ("Quel est le vrai nom de George Orwell ?", ["Eric Arthur Blair", "Winston Smith", "Big Brother"], ""),
 ("Qu'a-t-il découvert en Birmanie ?", ["La violence de la domination coloniale", "Le communisme", "Le journalisme"], ""),
 ("Pourquoi la guerre d'Espagne est-elle décisive pour lui ?", ["Il voit les staliniens persécuter d'autres militants et mentir", "Il y devient riche", "Il y rencontre Franco"], ""),
 ("Que critique Animal Farm ?", ["La révolution russe trahie par Staline", "L'agriculture", "La monarchie britannique"], ""),
 ("Que fait Winston Smith au Ministry of Truth ?", ["Il réécrit les archives du passé", "Il dit la vérité", "Il surveille les enfants"], ""),
 ("Que signifie « orwellien » aujourd'hui ?", ["Une société de surveillance et de manipulation", "Une ferme moderne", "Un style d'écriture compliqué"], ""),
], [("Franco", "général, dictateur de l'Espagne de 1939 à 1975"), ("**Napoleon**", "le cochon tyran du roman")])
D = "or"
culture(F, "Culture : George Orwell", 'George <span>Orwell</span>',
  "Culture · Animal Farm, 1984 et Big Brother", ("#d4d4d8", "#991b1b"),
  reperes("George Orwell (1903-1950), écrivain britannique, a dénoncé les dictatures et la manipulation dans Animal Farm et Nineteen Eighty-Four.",
    [("1903", "naissance d'Eric Blair en Inde"), ("1922 – 1927", "policier en Birmanie"), ("1936 – 1937", "combat pendant la guerre d'Espagne"),
     ("1945", "Animal Farm"), ("1949", "Nineteen Eighty-Four"), ("1950", "mort d'Orwell, à 46 ans")],
    "a dictatorship, totalitarianism, propaganda, surveillance, Big Brother, Newspeak, doublethink, Orwellian"),
  {D: doc("Big Brother is watching you", [
    "George Orwell was a British writer. His real name was Eric Blair. As a young man, he was a policeman in Burma, then he lived with poor people in Paris and London.",
    "In 1936, he went to fight in the Spanish Civil War. There, he saw how political propaganda lied about the truth. After that, he wrote against all dictatorships.",
    "In Animal Farm (1945), the animals of a farm take power, but the pigs become as cruel as the farmer. It is a story about the Russian Revolution.",
    "In Nineteen Eighty-Four (1949), the Party controls everything. Telescreens watch everybody, and posters say \"Big Brother is watching you\". Winston Smith's job is to change old newspapers so that the past always agrees with the Party.",
    "Today, we use the word \"Orwellian\" to talk about surveillance, lies and control of information."])},
  [TF(D, "George Orwell's real name was Eric Blair.", True, "« His real name was Eric Blair »."),
   TF(D, "Orwell fought in the Spanish Civil War.", True, "« to fight in the Spanish Civil War »."),
   TF(D, "Orwell wrote in favour of dictatorships.", False, "« he wrote against all dictatorships »."),
   TF(D, "In Animal Farm, the pigs become kind and fair.", False, "« as cruel as the farmer »."),
   TF(D, "In 1984, telescreens watch everybody.", True, "« Telescreens watch everybody »."),
   TF(D, "Winston Smith writes new novels.", False, "Il modifie les vieux journaux." )],
  [Q(D, "What did Orwell see in Spain?", ["Propaganda lying about the truth.", "A beautiful revolution.", "The Olympic Games."]),
   Q(D, "What happens in Animal Farm?", ["The pigs take power and become cruel.", "The farmer becomes rich.", "The animals leave the farm."]),
   Q(D, "What do the posters say in 1984?", ["\"Big Brother is watching you\".", "\"Freedom for all\".", "\"Have a nice day\"."]),
   Q(D, "What does \"Orwellian\" mean?", ["Related to surveillance, lies and control.", "Very funny.", "About farms."])],
  [DT(D, "Comment s'appelle la novlangue en anglais ?", ["Newspeak", "Bigspeak", "Truthtalk", "Oldspeak"]),
   DT(D, "Comment s'appelle le cochon tyran d'Animal Farm ?", ["Napoleon", "Snowball", "Boxer", "Winston"]),
   DT(D, "Où Winston est-il brisé ?", ["Dans la Room 101", "Au 221B Baker Street", "À Robben Island", "Dans la Tour de Londres"]),
   DT(D, "Sur quelle île écossaise Orwell écrit-il 1984 ?", ["Jura", "Skye", "Iona", "Man"])],
  [W(D, "Trouve le mot qui veut dire « a menti ».", "lied"), W(D, "Trouve le mot qui veut dire « cruels ».", "cruel"),
   W(D, "Trouve le mot qui veut dire « affiches ».", "posters"), W(D, "Trouve le mot qui veut dire « la surveillance ».", "surveillance")])

# ═════════ DYSTOPIES ═════════
F = "cu_dystopies.html"
DZ(F, """
## Utopie et dystopie
En 1516, l'Anglais **Thomas More** invente le mot **Utopia** (du grec « nulle part ») pour décrire une île imaginaire où la société serait parfaite. Une **dystopia** est l'inverse : une société imaginaire, souvent dans le futur, qui paraît parfaite ou ordonnée mais qui est en réalité un cauchemar d'oppression. Les dystopies grossissent les dangers du présent pour nous avertir : ce sont des romans d'alerte.

## Brave New World (1932)
Dans *Brave New World* d'**Aldous Huxley**, les bébés sont fabriqués en laboratoire et conditionnés pour appartenir à des castes, des Alphas aux Epsilons. Tout le monde est heureux grâce à la consommation, aux loisirs et à une drogue, le **soma**. Il n'y a plus de famille, d'art ni de pensée libre. Là où Orwell imagine un pouvoir qui contrôle par la peur, Huxley imagine un pouvoir qui contrôle par le plaisir.

## Nineteen Eighty-Four (1949)
Le roman de **George Orwell** est la dystopie la plus célèbre : surveillance permanente (**Big Brother is watching you**), réécriture du passé, novlangue, police de la pensée. Il a donné au monde le vocabulaire de la surveillance.

## Fahrenheit 451 (1953)
Dans le roman de l'Américain **Ray Bradbury**, les livres sont interdits. Les pompiers (**firemen**) ne combattent plus les incendies : ils brûlent les livres et les maisons de ceux qui en cachent. Le titre renvoie à la température à laquelle, selon le livre, le papier s'enflamme (environ 233 °C). Le héros, le pompier **Guy Montag**, rencontre une jeune voisine curieuse, Clarisse, qui le fait douter. Sa femme, Mildred, passe ses journées devant des murs-écrans et ne pense à rien. Montag finit par voler des livres, puis rejoint des rebelles qui apprennent chacun un livre par cœur pour le sauver de l'oubli : ils deviennent des « livres vivants ». Bradbury écrit dans l'Amérique du maccarthysme, mais il disait aussi s'inquiéter d'une télévision qui rendrait les gens incapables de lire et de réfléchir. Le réalisateur français **François Truffaut** l'a adapté au cinéma en 1966.

## Les dystopies d'aujourd'hui
- *The Handmaid's Tale* (1985) de la Canadienne **Margaret Atwood** : dans la république de Gilead, les femmes ont perdu tous leurs droits ; certaines, les « servantes », sont forcées d'avoir des enfants pour les élites. Les capes rouges des servantes sont devenues un symbole dans des manifestations pour les droits des femmes.
- *The Hunger Games* (2008) de **Suzanne Collins** : dans le pays de Panem, des adolescents sont obligés de s'affronter à mort dans un jeu télévisé.
- La série britannique *Black Mirror* (depuis 2011) imagine les dérives des nouvelles technologies : réseaux sociaux, notes données à tout le monde, intelligence artificielle.

## Pourquoi les lire aujourd'hui ?
Ces œuvres posent des questions très actuelles : jusqu'où accepter la **surveillance** (caméras, données personnelles, reconnaissance faciale) au nom de la sécurité ? Comment repérer la **propaganda** et les fausses informations ? Faut-il interdire des livres ? Aux États-Unis, le retrait de certains livres des bibliothèques scolaires suscite aujourd'hui un vif débat, et, ironie du sort, *Fahrenheit 451* lui-même a parfois été contesté.
[→ Voir aussi : George Orwell](cu_orwell.html)
""", """
a book = un livre
a fire = un feu
a fireman = un pompier
to burn = brûler
the future = le futur
a rule = une règle
happy = heureux
a screen = un écran
""", [
 ("Qu'est-ce qu'une dystopie ?", ["Une société imaginaire qui est en réalité un cauchemar d'oppression", "Une société parfaite", "Un roman d'amour"], ""),
 ("Comment le pouvoir contrôle-t-il les gens dans Brave New World ?", ["Par le plaisir, la consommation et une drogue", "Par la guerre", "Par les livres"], ""),
 ("Que font les pompiers dans Fahrenheit 451 ?", ["Ils brûlent les livres", "Ils éteignent les incendies", "Ils écrivent des livres"], ""),
 ("Que font les rebelles à la fin de Fahrenheit 451 ?", ["Ils apprennent chacun un livre par cœur", "Ils brûlent la ville", "Ils deviennent pompiers"], ""),
 ("Qui a adapté Fahrenheit 451 au cinéma ?", ["François Truffaut", "Steven Spielberg", "Ray Bradbury"], ""),
 ("Quelle question actuelle posent ces œuvres ?", ["Jusqu'où accepter la surveillance au nom de la sécurité ?", "Comment cuisiner ?", "Qui gagnera le Super Bowl ?"], ""),
], [("**Thomas More**", "humaniste anglais, 1478-1535"), ("**Aldous Huxley**", "écrivain anglais, 1894-1963"), ("**Ray Bradbury**", "écrivain américain de science-fiction, 1920-2012"),
    ("maccarthysme", "chasse aux communistes aux États-Unis dans les années 1950")])
D = "dy"
culture(F, "Culture : Dystopias", 'Dysto<span>pias</span>',
  "Culture · Brave New World, 1984, Fahrenheit 451 et les autres", ("#a3a3a3", "#ea580c"),
  reperes("Une dystopie imagine une société future qui semble ordonnée mais qui opprime ses habitants. Ces romans nous mettent en garde contre les dangers du présent.",
    [("1516", "Utopia de Thomas More"), ("1932", "Brave New World d'Aldous Huxley"), ("1949", "Nineteen Eighty-Four de George Orwell"),
     ("1953", "Fahrenheit 451 de Ray Bradbury"), ("1985", "The Handmaid's Tale de Margaret Atwood"), ("2008", "The Hunger Games de Suzanne Collins")],
    "a dystopia, a utopia, a totalitarian state, surveillance, censorship, propaganda, a rebel, freedom"),
  {D: doc("It was a pleasure to burn", [
    "A dystopia is an imaginary society that looks perfect but is in fact terrible. The people have no freedom. Dystopian novels warn us about the dangers of today.",
    "In Brave New World (1932), people are always happy because they take a drug and buy lots of things. But they cannot think freely.",
    "In Nineteen Eighty-Four (1949), by George Orwell, the government watches everybody: \"Big Brother is watching you\".",
    "In Fahrenheit 451 (1953), by Ray Bradbury, books are forbidden. Firemen do not stop fires: they burn books! The hero, Guy Montag, is a fireman who starts to read books secretly. At the end, he joins rebels who learn books by heart.",
    "Today, The Hunger Games and the TV series Black Mirror continue this tradition. They make us think about technology, surveillance and freedom."])},
  [TF(D, "A dystopia is a perfect society.", False, "« looks perfect but is in fact terrible »."),
   TF(D, "In Brave New World, people take a drug.", True, "« they take a drug »."),
   TF(D, "Fahrenheit 451 was written by George Orwell.", False, "Par Ray Bradbury."),
   TF(D, "In Fahrenheit 451, firemen burn books.", True, "« they burn books »."),
   TF(D, "Guy Montag starts to read books secretly.", True, "« starts to read books secretly »."),
   TF(D, "Dystopias make us think about freedom.", True, "« think about technology, surveillance and freedom »." )],
  [Q(D, "What is a dystopia?", ["An imaginary society that looks perfect but is terrible.", "A happy story.", "A history book."]),
   Q(D, "Why are people happy in Brave New World?", ["They take a drug and buy lots of things.", "They read many books.", "They are free."]),
   Q(D, "What is forbidden in Fahrenheit 451?", ["Books.", "Television.", "Cars."]),
   Q(D, "What do the rebels do?", ["They learn books by heart.", "They burn houses.", "They watch TV."])],
  [DT(D, "Qui a inventé le mot « utopie » ?", ["Thomas More", "George Orwell", "Ray Bradbury", "Shakespeare"]),
   DT(D, "Comment s'appelle la drogue de Brave New World ?", ["Le soma", "Le sucre", "Le gin", "Le fentanyl"]),
   DT(D, "Comment s'appelle le pompier héros de Fahrenheit 451 ?", ["Guy Montag", "Winston Smith", "Guy Fawkes", "Katniss"]),
   DT(D, "Dans quelle dystopie les femmes portent-elles des capes rouges ?", ["The Handmaid's Tale", "The Hunger Games", "Brave New World", "Black Mirror"])],
  [W(D, "Trouve le mot qui veut dire « mettent en garde ».", "warn"), W(D, "Trouve le mot qui veut dire « interdits ».", "forbidden"),
   W(D, "Trouve le mot qui veut dire « brûlent ».", "burn"), W(D, "Trouve le mot qui veut dire « par cœur » (2 mots).", ["by heart"])])

# ═════════ BALDWIN ═════════
F = "cu_baldwin.html"
DZ(F, """
## Un enfant de Harlem
**James Baldwin** naît en 1924 à **Harlem**, le grand quartier noir de New York. Il est l'aîné de neuf enfants et ne connaît pas son père biologique. Son beau-père, David Baldwin, est un prédicateur très sévère, amer face au racisme et à la pauvreté. Adolescent, James devient lui-même prédicateur dans une église pentecôtiste, de 14 à 17 ans, avant de quitter l'Église. Il lit énormément, travaille dans des petits boulots et commence à écrire.

## L'exil à Paris
En 1948, épuisé par le racisme et la ségrégation de l'Amérique, Baldwin part pour **Paris** avec presque rien en poche. Il y vivra une grande partie de sa vie. C'est loin de son pays qu'il parvient à écrire sur lui : « je suis venu en France pour comprendre que j'étais américain », expliquait-il en substance.

## Go Tell It on the Mountain (1953)
Son premier roman, en grande partie autobiographique, se passe à Harlem en **1935**, le jour des 14 ans de **John Grimes**. John grandit dans la peur de son beau-père, **Gabriel**, diacre et prédicateur dur, qui lui préfère son demi-frère Roy. Il se demande s'il doit suivre la voie religieuse qu'on attend de lui, alors qu'il rêve d'un autre monde.
- La première partie suit cette journée.
- La deuxième, *The Prayers of the Saints*, plonge dans le passé de la tante Florence, de Gabriel et de la mère de John, Elizabeth : leur jeunesse dans le Sud ségrégationniste, leur départ vers le Nord pendant la **Great Migration**, leurs fautes et leurs secrets.
- La dernière partie raconte la nuit où John vit une expérience religieuse bouleversante dans la petite église de la famille.
Le roman parle de religion, de famille, de culpabilité, de racisme et de la difficulté de devenir soi-même. Il est souvent classé parmi les grands romans américains du 20e siècle.

## D'où vient le titre ?
Le titre reprend un **spiritual**, un chant religieux afro-américain du 19e siècle, chanté par les esclaves puis par leurs descendants. Les spirituals mêlaient la foi chrétienne et l'espoir de la liberté. « *Go tell it on the mountain* » appelle à annoncer une bonne nouvelle à tous : ici, la « naissance » spirituelle de John.

## Un écrivain engagé
Baldwin publie ensuite des essais puissants sur la question raciale, comme *Notes of a Native Son* (1955) et *The Fire Next Time* (1963), qui fait de lui l'une des grandes voix du **civil rights movement**. Il rentre aux États-Unis pour participer à la lutte, aux côtés de Martin Luther King, et fait la couverture du magazine *Time* en 1963. Son roman *Giovanni's Room* (1956) aborde aussi l'homosexualité, sujet tabou à l'époque. Il meurt en 1987 à **Saint-Paul-de-Vence**, dans le sud de la France. Le documentaire *I Am Not Your Negro* (2016) de Raoul Peck a fait redécouvrir sa pensée à une nouvelle génération.
[→ Voir aussi : le mouvement des droits civiques](cu_droits_civiques.html)
""", """
a novel = un roman
a church = une église
a preacher = un prédicateur
a stepfather = un beau-père
a birthday = un anniversaire
a mountain = une montagne
a song = un chant, une chanson
faith = la foi
""", [
 ("Où est né James Baldwin ?", ["À Harlem, à New York", "À Paris", "En Alabama"], ""),
 ("Pourquoi part-il à Paris en 1948 ?", ["Pour échapper au racisme et à la ségrégation", "Pour étudier la médecine", "Pour devenir acteur"], ""),
 ("Qui est John Grimes ?", ["Le héros du roman, qui a 14 ans", "Le beau-père", "Un pasteur de Paris"], ""),
 ("De quoi parle la deuxième partie du roman ?", ["Du passé de la famille dans le Sud et de la Great Migration", "D'un voyage en France", "D'une guerre"], ""),
 ("D'où vient le titre du roman ?", ["D'un spiritual, chant religieux afro-américain", "D'un poème de Shakespeare", "D'une publicité"], ""),
 ("Quel rôle joue Baldwin dans les années 1960 ?", ["Il devient une grande voix du mouvement des droits civiques", "Il devient président", "Il arrête d'écrire"], ""),
], [("Harlem", "quartier de Manhattan, centre de la culture afro-américaine"), ("Great Migration", "départ de millions de Noirs du Sud vers le Nord, 1910-1970"),
    ("Raoul Peck", "réalisateur haïtien")])
D = "jb"
culture(F, "Culture : James Baldwin – Go Tell It on the Mountain", 'Go Tell It <span>on the Mountain</span>',
  "Culture · James Baldwin, Harlem et les droits civiques", ("#fcd34d", "#1e3a8a"),
  reperes("James Baldwin (1924-1987), grand écrivain afro-américain, raconte dans Go Tell It on the Mountain (1953) une adolescence à Harlem, entre religion et racisme.",
    [("1924", "naissance à Harlem"), ("1948", "départ pour Paris"), ("1953", "Go Tell It on the Mountain"), ("1963", "The Fire Next Time"),
     ("1987", "mort à Saint-Paul-de-Vence"), ("2016", "documentaire I Am Not Your Negro")],
    "a novel, a preacher, a church, faith, a stepfather, a spiritual, racism, the Great Migration"),
  {D: doc("A boy in Harlem", [
    "James Baldwin was born in Harlem, New York, in 1924. His stepfather was a strict preacher. As a teenager, James preached in a church too.",
    "In 1948, he moved to Paris to escape racism in America. He lived in France for a large part of his life.",
    "His first novel, Go Tell It on the Mountain (1953), tells the story of John Grimes, a boy who lives in Harlem. The story takes place on his fourteenth birthday. John is afraid of his stepfather, Gabriel.",
    "The novel also tells the past of John's family, who came from the South to the North. It talks about religion, family, racism and growing up.",
    "The title comes from an old African-American spiritual. Later, Baldwin became an important voice of the civil rights movement."])},
  [TF(D, "James Baldwin was born in Harlem.", True, "« born in Harlem »."),
   TF(D, "His stepfather was a teacher.", False, "« a strict preacher »."),
   TF(D, "Baldwin moved to Paris to escape racism.", True, "« to escape racism »."),
   TF(D, "The story takes place on John's eighteenth birthday.", False, "« his fourteenth birthday »."),
   TF(D, "John's family came from the South.", True, "« came from the South to the North »."),
   TF(D, "The title comes from a pop song.", False, "« an old African-American spiritual »." )],
  [Q(D, "What did Baldwin do as a teenager?", ["He preached in a church.", "He worked in Paris.", "He played baseball."]),
   Q(D, "Who is John afraid of?", ["His stepfather, Gabriel.", "His teacher.", "His brother."]),
   Q(D, "What are the themes of the novel?", ["Religion, family, racism and growing up.", "War and adventure.", "Science and technology."]),
   Q(D, "What did Baldwin become later?", ["An important voice of the civil rights movement.", "A preacher in Paris.", "A politician."])],
  [DT(D, "Dans quelle ville française meurt Baldwin ?", ["Saint-Paul-de-Vence", "Paris", "Marseille", "Lyon"]),
   DT(D, "Quel essai de 1963 le rend célèbre ?", ["The Fire Next Time", "Notes from Underground", "Native Son", "On the Road"]),
   DT(D, "Comment s'appelle la deuxième partie du roman ?", ["The Prayers of the Saints", "The Fire Next Time", "Giovanni's Room", "The Mountain"]),
   DT(D, "Qu'est-ce qu'un spiritual ?", ["Un chant religieux afro-américain", "Un fantôme", "Un prêtre", "Un roman"])],
  [W(D, "Trouve le mot qui veut dire « beau-père ».", "stepfather"), W(D, "Trouve le mot qui veut dire « strict, sévère ».", "strict"),
   W(D, "Trouve le mot qui veut dire « échapper à ».", "escape"), W(D, "Trouve le mot qui veut dire « grandir » (2 mots).", ["growing up", "grow up"])])

# ═════════ OTHELLO ═════════
F = "cu_othello.html"
DZ(F, """
## Une tragédie de la jalousie
*Othello*, écrite par **Shakespeare** vers 1603-1604, s'inspire d'une nouvelle italienne. L'action se passe à **Venise**, puis sur l'île de **Chypre**. **Othello** est un général maure (un homme d'Afrique du Nord), admiré pour son courage, au service de la république de Venise. Il a épousé en secret **Desdemona**, la fille d'un sénateur, Brabantio, qui l'accuse d'avoir ensorcelé sa fille.

## Iago, le manipulateur
L'enseigne **Iago** déteste Othello, notamment parce que celui-ci a choisi **Cassio** plutôt que lui comme lieutenant. Il se présente comme l'ami fidèle de tous, mais il manipule chacun : il fait boire Cassio pour qu'il perde son poste, puis pousse Desdemona à plaider pour lui, ce qui fait croire à Othello qu'elle l'aime. Iago met en garde Othello contre la jalousie, ce « monstre aux yeux verts » (*the green-eyed monster*), tout en la faisant naître en lui.

## Le mouchoir
L'objet clé est un **handkerchief** (mouchoir), premier cadeau d'Othello à Desdemona. Elle le perd ; Emilia, la femme de Iago, le ramasse et le donne à son mari, qui le dépose chez Cassio. Pour Othello, c'est la « preuve » de la trahison. Fou de jalousie, il étouffe Desdemona dans son lit. Emilia révèle alors la vérité et est tuée par Iago. Othello, comprenant qu'il a tué une femme innocente, se donne la mort. Iago refuse de s'expliquer.

## Une pièce sur la race
*Othello* est l'une des premières pièces du théâtre anglais à avoir pour héros tragique un homme noir. Ses ennemis le désignent par des insultes racistes, et il se sent étranger dans la société vénitienne, ce qui le rend vulnérable aux mensonges de Iago. Pendant des siècles, le rôle a été joué par des acteurs blancs maquillés. En 1833, l'Afro-Américain **Ira Aldridge** joue Othello à Londres ; dans les années 1930-1940, **Paul Robeson** marque le rôle, notamment à Broadway en 1943. Aujourd'hui, la pièce fait réfléchir au racisme, à la jalousie, à la manipulation et à la violence faite aux femmes.

## Ce qu'il faut retenir
- **Tragedy** : la pièce finit par la mort des héros.
- Thèmes : jalousie, manipulation, apparences trompeuses, racisme, honneur.
- Iago est l'un des méchants les plus célèbres de la littérature, car on ne comprend jamais complètement ses motivations.
[→ Voir aussi : Shakespeare](cu_shakespeare.html)
""", """
a play = une pièce de théâtre
jealousy = la jalousie
a general = un général
a wife = une épouse
a handkerchief = un mouchoir
a lie = un mensonge
a friend = un ami
innocent = innocent
""", [
 ("Qui est Othello ?", ["Un général maure au service de Venise", "Un roi d'Angleterre", "Un marchand"], ""),
 ("Pourquoi Iago déteste-t-il Othello ?", ["Othello a choisi Cassio plutôt que lui comme lieutenant", "Othello lui a volé de l'argent", "Othello est son frère"], ""),
 ("Quel est l'objet clé de la pièce ?", ["Un mouchoir", "Une bague", "Une lettre"], ""),
 ("Comment finit la pièce ?", ["Othello tue Desdemona puis se donne la mort", "Par un mariage", "Othello devient roi"], ""),
 ("Pourquoi la pièce est-elle importante sur la question raciale ?", ["Son héros tragique est un homme noir, victime de racisme", "Elle se passe en Afrique", "Elle n'en parle pas"], ""),
 ("Que signifie « the green-eyed monster » ?", ["La jalousie", "Un dragon", "Un fantôme"], ""),
], [("Chypre", "île de Méditerranée orientale"), ("**Ira Aldridge**", "acteur afro-américain, 1807-1867"), ("**Paul Robeson**", "chanteur, acteur et militant afro-américain")])
D = "ot"
culture(F, "Culture : Shakespeare – Othello", 'Othello',
  "Culture · Shakespeare, la jalousie et le racisme", ("#e5e7eb", "#7f1d1d"),
  reperes("Othello (vers 1603) est une tragédie de Shakespeare : manipulé par Iago, le général Othello tue sa femme innocente par jalousie.",
    [("vers 1603", "écriture d'Othello"), ("Venise et Chypre", "les lieux de l'action"), ("1833", "Ira Aldridge, premier grand Othello noir à Londres"),
     ("1943", "Paul Robeson joue Othello à Broadway")],
    "a tragedy, a hero, a villain, jealousy, to manipulate, a handkerchief, betrayal, racism"),
  {D: doc("Beware of jealousy", [
    "Othello is a tragedy by William Shakespeare. Othello is a Black general who works for Venice. He secretly marries Desdemona, a senator's daughter.",
    "Iago, one of Othello's soldiers, hates him because Othello chose Cassio, not Iago, as his lieutenant. Iago pretends to be a good friend, but he lies to everybody.",
    "Iago makes Othello believe that Desdemona loves Cassio. He uses a handkerchief, Othello's first gift to Desdemona, as false proof.",
    "Mad with jealousy, Othello kills Desdemona. When he learns that she was innocent, he kills himself.",
    "The play talks about jealousy, lies and racism. For a long time, white actors played Othello. Today, it is usually played by Black actors."])},
  [TF(D, "Othello is a comedy.", False, "« a tragedy »."),
   TF(D, "Othello works for Venice.", True, "« works for Venice »."),
   TF(D, "Iago is a true friend of Othello.", False, "« he lies to everybody »."),
   TF(D, "Iago uses a handkerchief as false proof.", True, "« as false proof »."),
   TF(D, "Desdemona really loved Cassio.", False, "« she was innocent »."),
   TF(D, "The play talks about racism.", True, "« jealousy, lies and racism »." )],
  [Q(D, "Why does Iago hate Othello?", ["Othello chose Cassio as his lieutenant.", "Othello is rich.", "Othello is his brother."]),
   Q(D, "What does Iago make Othello believe?", ["That Desdemona loves Cassio.", "That he is king.", "That Venice is in danger."]),
   Q(D, "What is the handkerchief?", ["Othello's first gift to Desdemona.", "A flag.", "A letter."]),
   Q(D, "What happens at the end?", ["Othello kills Desdemona, then himself.", "They get married again.", "Iago becomes general."])],
  [DT(D, "Comment s'appelle la femme d'Iago ?", ["Emilia", "Desdemona", "Beatrice", "Juliet"]),
   DT(D, "Qui est promu lieutenant à la place d'Iago ?", ["Cassio", "Roderigo", "Brabantio", "Claudio"]),
   DT(D, "Quel acteur joue Othello à Broadway en 1943 ?", ["Paul Robeson", "Laurence Olivier", "Ira Aldridge", "Denzel Washington"]),
   DT(D, "Comment dit-on « un mouchoir » ?", ["A handkerchief", "A hand-towel", "A napkin glove", "A handbag"])],
  [W(D, "Trouve le mot qui veut dire « fait semblant ».", "pretends"), W(D, "Trouve le mot qui veut dire « une fausse preuve » (2 mots).", ["false proof"]),
   W(D, "Trouve le mot qui veut dire « fou de jalousie » (3 mots).", ["mad with jealousy"]), W(D, "Trouve le mot qui veut dire « innocente ».", "innocent")])

# ═════════ MUCH ADO ═════════
F = "cu_much_ado.html"
DZ(F, """
## Une comédie à Messine
*Much Ado About Nothing* (« Beaucoup de bruit pour rien »), écrite par **Shakespeare** vers 1598-1599, se passe à **Messine**, en Sicile. Le prince **Don Pedro** et ses officiers reviennent victorieux de la guerre et séjournent chez le gouverneur **Leonato**. Deux histoires d'amour s'y croisent.

## Beatrice et Benedick : la « joyeuse guerre »
**Beatrice**, la nièce de Leonato, et **Benedick**, un officier, passent leur temps à se moquer l'un de l'autre dans des joutes verbales pleines d'esprit. Tous deux jurent qu'ils ne se marieront jamais. Leurs amis décident de leur jouer un tour : ils organisent des conversations que chacun « surprend » en se cachant, où l'on raconte que l'autre est fou amoureux de lui. Le piège fonctionne : Beatrice et Benedick finissent par s'avouer leur amour. Beatrice, intelligente, indépendante et drôle, est l'une des héroïnes les plus modernes de Shakespeare.

## Claudio et Hero : l'amour trompé
Le jeune officier **Claudio** tombe amoureux de **Hero**, la fille de Leonato, et le mariage est vite décidé. Mais le méchant de la pièce, **Don John**, demi-frère jaloux du prince, veut tout gâcher. Il fait croire à Claudio que Hero le trompe : la nuit, à une fenêtre, Claudio voit son complice Borachio parler à une servante qu'il prend pour Hero. Le jour du mariage, devant l'autel, Claudio accuse publiquement Hero et l'humilie. Hero s'évanouit ; le frère qui devait les marier propose de faire croire qu'elle est morte, le temps de découvrir la vérité. Beatrice, furieuse, demande à Benedick de prouver son amour en défendant l'honneur de sa cousine.

## Dogberry, le gendarme ridicule
La vérité est découverte… par **Dogberry**, le chef de la garde, un personnage comique qui se trompe sans arrêt de mots (il emploie des mots savants à contresens). Malgré sa bêtise, sa patrouille surprend Borachio en train de se vanter du complot. Claudio, rongé de remords, accepte d'épouser une « cousine » de Hero sans la voir : c'est Hero elle-même. La pièce finit par un double mariage et une danse.

## Pourquoi « about nothing » ?
Le titre est un jeu de mots : à l'époque de Shakespeare, *nothing* se prononçait presque comme *noting* (« remarquer, épier »). Or toute la pièce repose sur ce que les personnages voient, entendent, surprennent et interprètent mal. Comme dans *Othello*, un homme croit à une fausse preuve de l'infidélité de sa bien-aimée ; mais ici, la comédie permet de tout réparer. Le film de **Kenneth Branagh** (1993), avec Emma Thompson en Beatrice, a rendu la pièce très populaire.

## Ce qu'il faut retenir
- **Comedy** : malentendus, quiproquos, fin heureuse avec des mariages.
- Thèmes : l'amour, les apparences trompeuses, l'honneur et la réputation des femmes, la guerre des sexes, l'esprit (**wit**).
[→ Voir aussi : Othello, l'autre histoire de fausse preuve](cu_othello.html)
""", """
love = l'amour
a wedding = un mariage
a trick = un tour, une ruse
a joke = une plaisanterie
a window = une fenêtre
a cousin = un cousin, une cousine
to marry = épouser
funny = drôle
""", [
 ("Où se passe la pièce ?", ["À Messine, en Sicile", "À Londres", "À Venise"], ""),
 ("Comment se comportent Beatrice et Benedick au début ?", ["Ils se moquent l'un de l'autre et refusent de se marier", "Ils sont mariés", "Ils sont frère et sœur"], ""),
 ("Quel tour leurs amis leur jouent-ils ?", ["Ils leur font surprendre de fausses conversations amoureuses", "Ils les enferment", "Ils leur volent de l'argent"], ""),
 ("Pourquoi Claudio humilie-t-il Hero au mariage ?", ["Don John lui a fait croire qu'elle le trompait", "Elle a oublié l'alliance", "Il aime Beatrice"], ""),
 ("Qui découvre la vérité ?", ["Dogberry et sa garde", "Don John", "Le prince"], ""),
 ("Quel jeu de mots se cache dans le titre ?", ["nothing / noting (remarquer, épier)", "much / match", "ado / adieu"], ""),
], [("**Kenneth Branagh**", "acteur et réalisateur britannique"), ("Emma Thompson", "actrice britannique")])
D = "ma"
culture(F, "Culture : Shakespeare – Much Ado About Nothing", 'Much Ado <span>About Nothing</span>',
  "Culture · Shakespeare, l'amour et les malentendus", ("#fbcfe8", "#15803d"),
  reperes("Much Ado About Nothing (vers 1598) est une comédie de Shakespeare : deux couples, des ruses, des malentendus et une fin heureuse.",
    [("vers 1598", "écriture de la pièce"), ("Messine", "le lieu de l'action, en Sicile"), ("Beatrice et Benedick", "le couple qui se dispute"),
     ("Claudio et Hero", "le couple trompé par Don John"), ("1993", "le film de Kenneth Branagh")],
    "a comedy, a misunderstanding, a trick, wit, a wedding, to overhear, honour, a happy ending"),
  {D: doc("A merry war", [
    "Much Ado About Nothing is a comedy by Shakespeare. It takes place in Messina, in Sicily, after a war.",
    "Beatrice and Benedick always argue and make fun of each other. They both say they will never marry. Their friends trick them: each one overhears that the other is in love. In the end, they fall in love.",
    "Claudio loves Hero and wants to marry her. But the villain, Don John, makes Claudio believe that Hero is unfaithful. At the wedding, Claudio refuses to marry her.",
    "Luckily, Dogberry, a funny and stupid policeman, discovers the truth. Claudio and Hero finally get married, and so do Beatrice and Benedick.",
    "Like in Othello, a man believes false proof. But this time, it is a comedy, so everything ends happily."])},
  [TF(D, "Much Ado About Nothing is a tragedy.", False, "« a comedy »."),
   TF(D, "Beatrice and Benedick always argue.", True, "« always argue »."),
   TF(D, "Their friends trick them.", True, "« Their friends trick them »."),
   TF(D, "Don John wants to help Claudio.", False, "C'est le méchant (« the villain »)."),
   TF(D, "Dogberry discovers the truth.", True, "« discovers the truth »."),
   TF(D, "The play ends with two weddings.", True, "« Claudio and Hero… and so do Beatrice and Benedick »." )],
  [Q(D, "Where does the play take place?", ["In Messina, in Sicily.", "In London.", "In Venice."]),
   Q(D, "What do Beatrice and Benedick say at the beginning?", ["They will never marry.", "They love each other.", "They want to leave."]),
   Q(D, "What does Don John do?", ["He makes Claudio believe Hero is unfaithful.", "He marries Hero.", "He helps Dogberry."]),
   Q(D, "How is this play different from Othello?", ["It is a comedy, so it ends happily.", "It has no villain.", "It takes place in Cyprus."])],
  [DT(D, "Qui est le méchant de la pièce ?", ["Don John", "Don Pedro", "Leonato", "Benedick"]),
   DT(D, "Qui est la nièce de Leonato ?", ["Beatrice", "Hero", "Desdemona", "Emilia"]),
   DT(D, "Qui a réalisé le film de 1993 ?", ["Kenneth Branagh", "Laurence Olivier", "James Cameron", "Baz Luhrmann"]),
   DT(D, "Comment dit-on « surprendre une conversation » ?", ["To overhear", "To overlook", "To hear over", "To oversee"])],
  [W(D, "Trouve le mot qui veut dire « se disputent ».", "argue"), W(D, "Trouve le mot qui veut dire « se moquer de » (2 mots).", ["make fun", "make fun of"]),
   W(D, "Trouve le mot qui veut dire « infidèle ».", "unfaithful"), W(D, "Trouve le mot qui veut dire « heureusement ».", ["Luckily", "luckily"])])

# ═════════ AFRIQUE DU SUD AUJOURD'HUI ═════════
F = "cu_afrique_sud_auj.html"
DZ(F, """
## La « nation arc-en-ciel », trente ans après
Depuis les premières élections libres de 1994, l'Afrique du Sud est une démocratie, avec l'une des Constitutions les plus progressistes du monde (1996). L'archevêque Desmond Tutu l'avait surnommée la **Rainbow Nation**, la nation arc-en-ciel, pour célébrer sa diversité. Environ 63 millions de personnes y vivent : une large majorité de Noirs, ainsi que des Blancs, des métis (« Coloured ») et des Sud-Africains d'origine indienne.

## Douze langues officielles
Le pays a **12 langues officielles**, dont la langue des signes sud-africaine depuis 2023. La langue maternelle la plus parlée est le **zulu** (isiZulu), suivie du xhosa et de l'afrikaans. L'**anglais** n'est la langue maternelle que d'une petite minorité, mais c'est la langue commune de l'administration, des affaires, des médias et de l'université. Beaucoup de Sud-Africains passent d'une langue à l'autre dans la même conversation.

## Une démocratie qui change
L'**ANC**, le parti de Mandela, a gouverné seul pendant trente ans. Mais les scandales de corruption, notamment sous la présidence de Jacob Zuma (2009-2018), ont abîmé sa réputation. Aux élections de **2024**, l'ANC perd pour la première fois sa majorité absolue, avec environ 40 % des voix. Le président **Cyril Ramaphosa** forme alors un **gouvernement d'unité nationale** avec plusieurs partis, dont la Democratic Alliance, son principal rival. En 2025, Johannesburg accueille le premier sommet du **G20** organisé sur le continent africain.

## Des défis immenses
- **Les inégalités** : selon la Banque mondiale, l'Afrique du Sud est l'un des pays les plus inégalitaires du monde. Des quartiers riches et protégés côtoient des **townships** et des bidonvilles, héritage direct de l'apartheid.
- **Le chômage** touche environ un actif sur trois, et bien davantage chez les jeunes.
- **La criminalité** est très élevée.
- **L'électricité** : pendant des années, la compagnie publique Eskom a imposé des coupures de courant programmées, le **load shedding**, qui ont pesé sur la vie quotidienne et l'économie, avant de nettement diminuer à partir de 2024.
- **La terre** : la question de la réforme agraire, alors qu'une grande partie des terres agricoles reste détenue par la minorité blanche, est un sujet politique très sensible.

## Une culture qui rayonne
- Le **rugby** : les **Springboks**, autrefois symbole des Blancs, ont remporté la Coupe du monde en 2019 et en 2023 avec **Siya Kolisi**, premier capitaine noir de l'équipe, venu d'un township.
- La musique : l'**amapiano**, née dans les townships autour de Johannesburg et Pretoria, conquiert le monde ; la chanteuse **Tyla** a remporté en 2024 le premier Grammy de la meilleure performance musicale africaine.
- L'humoriste **Trevor Noah**, ancien présentateur du *Daily Show* aux États-Unis, raconte dans *Born a Crime* (2016) son enfance : né d'une mère xhosa et d'un père suisse, son existence même était illégale sous l'apartheid.
- Le **braai**, le barbecue, est une institution nationale ; le 24 septembre, jour du patrimoine (Heritage Day), est aussi surnommé « National Braai Day ».
[→ Voir aussi : l'apartheid et Nelson Mandela](cu_afrique_sud.html)
""", """
a language = une langue
a rainbow = un arc-en-ciel
an election = une élection
a job = un emploi
electricity = l'électricité
rugby = le rugby
a barbecue = un barbecue
a township = un township, un quartier pauvre
""", [
 ("Pourquoi parle-t-on de « Rainbow Nation » ?", ["Pour célébrer la diversité du pays", "À cause de la météo", "C'est le nom d'un parti"], ""),
 ("Combien de langues officielles compte l'Afrique du Sud ?", ["12", "2", "1"], ""),
 ("Que se passe-t-il aux élections de 2024 ?", ["L'ANC perd pour la première fois sa majorité absolue", "L'ANC disparaît", "Mandela revient au pouvoir"], ""),
 ("Qu'est-ce que le « load shedding » ?", ["Des coupures de courant programmées", "Une danse", "Un impôt"], ""),
 ("Pourquoi Siya Kolisi est-il un symbole ?", ["Il est le premier capitaine noir des Springboks", "Il est président", "Il chante l'amapiano"], ""),
 ("Pourquoi Trevor Noah dit-il qu'il est « né d'un crime » ?", ["Les couples mixtes étaient interdits sous l'apartheid", "Il est né en prison", "Il a volé quelque chose"], ""),
], [("Desmond Tutu", "archevêque anglican, prix Nobel de la paix 1984"), ("Jacob Zuma", "président de 2009 à 2018"), ("**Cyril Ramaphosa**", "président depuis 2018"),
    ("Democratic Alliance", "principal parti d'opposition")])
D = "sa"
culture(F, "Culture : South Africa today", 'South Africa <span>today</span>',
  "Culture · la nation arc-en-ciel, trente ans après l'apartheid", ("#86efac", "#ca8a04"),
  reperes("Trente ans après la fin de l'apartheid, l'Afrique du Sud est une démocratie très diverse, mais confrontée à de grandes inégalités.",
    [("1994", "premières élections libres, Mandela président"), ("1996", "nouvelle Constitution"), ("12", "langues officielles"),
     ("2019 et 2023", "les Springboks champions du monde"), ("2024", "l'ANC perd sa majorité absolue"), ("2025", "sommet du G20 à Johannesburg")],
    "the Rainbow Nation, an official language, a coalition, inequality, unemployment, a township, a power cut, a braai"),
  {D: doc("The Rainbow Nation", [
    "South Africa became a democracy in 1994. Archbishop Desmond Tutu called it \"the Rainbow Nation\" because of its diversity.",
    "The country has twelve official languages. Zulu is the most spoken first language, but English is the language of business, the media and universities.",
    "In 2024, Nelson Mandela's party, the ANC, lost its majority for the first time. Now, several parties govern together.",
    "South Africa still has big problems: huge inequalities between rich and poor, a lot of unemployment and crime. For years, there were also regular power cuts.",
    "But South African culture is very dynamic. The national rugby team, the Springboks, won the World Cup in 2019 and 2023 with its first Black captain, Siya Kolisi. South African music, like amapiano, is popular all over the world."])},
  [TF(D, "South Africa became a democracy in 1994.", True, "« in 1994 »."),
   TF(D, "English is the most spoken first language.", False, "C'est le zulu."),
   TF(D, "The ANC lost its majority in 2024.", True, "« lost its majority for the first time »."),
   TF(D, "There are no inequalities in South Africa.", False, "« huge inequalities »."),
   TF(D, "The Springboks won the World Cup in 2023.", True, "« in 2019 and 2023 »."),
   TF(D, "Amapiano is only popular in South Africa.", False, "« popular all over the world »." )],
  [Q(D, "Why is South Africa called \"the Rainbow Nation\"?", ["Because of its diversity.", "Because it rains a lot.", "Because of its flag only."]),
   Q(D, "What is English used for?", ["Business, the media and universities.", "Only at home.", "Nothing."]),
   Q(D, "What problems does South Africa have?", ["Inequalities, unemployment and crime.", "Too much snow.", "No sport."]),
   Q(D, "Who is Siya Kolisi?", ["The first Black captain of the Springboks.", "The President.", "A singer."])],
  [DT(D, "Qui a surnommé le pays « la nation arc-en-ciel » ?", ["Desmond Tutu", "Nelson Mandela", "F. W. de Klerk", "Trevor Noah"]),
   DT(D, "Qui est président de l'Afrique du Sud depuis 2018 ?", ["Cyril Ramaphosa", "Jacob Zuma", "Thabo Mbeki", "Nelson Mandela"]),
   DT(D, "Comment s'appelle le barbecue sud-africain ?", ["Le braai", "Le boerewors", "Le potjie", "Le grill"]),
   DT(D, "Quel livre a écrit Trevor Noah ?", ["Born a Crime", "Long Walk to Freedom", "Cry, the Beloved Country", "Things Fall Apart"])],
  [W(D, "Trouve le mot qui veut dire « la diversité ».", "diversity"), W(D, "Trouve le mot qui veut dire « le chômage ».", "unemployment"),
   W(D, "Trouve le mot qui veut dire « des coupures de courant » (2 mots).", ["power cuts"]), W(D, "Trouve le mot qui veut dire « capitaine ».", "captain")])
END()
