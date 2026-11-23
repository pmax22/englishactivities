import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
N1_ = {}

N1_["cu_usa.html"] = ("""
a state = un État
a flag = un drapeau
a star = une étoile
a stripe = une bande, une rayure
an eagle = un aigle
an immigrant = un immigrant
a desert = un désert
a holiday = un jour férié
""", [
 ("Combien d'États composent les États-Unis ?", ["50", "13", "100"], ""),
 ("Que représentent les 13 bandes du drapeau ?", ["Les 13 colonies fondatrices", "Les 13 présidents", "Les 13 plus grandes villes"], ""),
 ("Pourquoi Washington, D.C. est-elle particulière ?", ["Elle n'appartient à aucun État", "C'est la plus grande ville", "C'est une île"], ""),
 ("Quelle est la deuxième langue du pays ?", ["L'espagnol", "Le français", "Le chinois"], ""),
 ("Qu'est-ce que le « Pledge of Allegiance » ?", ["Le serment au drapeau récité à l'école", "Une chanson de Noël", "Un impôt"], ""),
 ("Qu'est-ce qui peut varier d'un État à l'autre ?", ["Les lois, comme la peine de mort ou l'âge du permis", "Le drapeau national", "La monnaie"], ""),
])

N1_["cu_institutions_us.html"] = ("""
the Constitution = la Constitution
an amendment = un amendement
Congress = le Congrès
a senator = un sénateur
a judge = un juge
the Supreme Court = la Cour suprême
power = le pouvoir
a law = une loi
""", [
 ("Qui sont les « Founding Fathers » ?", ["Les auteurs de la Constitution de 1787", "Les premiers colons", "Les juges de la Cour suprême"], ""),
 ("Qu'est-ce que le Bill of Rights ?", ["Les 10 premiers amendements, qui protègent les libertés", "Le budget de l'État", "Une liste de présidents"], ""),
 ("Que signifie « checks and balances » ?", ["Chaque pouvoir limite les autres", "Le président décide de tout", "Les impôts sont équilibrés"], ""),
 ("Combien de mandats un président peut-il faire au maximum ?", ["Deux", "Un", "Autant qu'il veut"], ""),
 ("Comment sont choisis les juges de la Cour suprême ?", ["Nommés à vie par le président avec l'accord du Sénat", "Élus par le peuple", "Tirés au sort"], ""),
 ("Quel est le symbole du Parti démocrate ?", ["L'âne", "L'éléphant", "L'aigle"], ""),
])

N1_["cu_manifest_destiny.html"] = ("""
the West = l'Ouest
a pioneer = un pionnier
gold = l'or
a railroad = un chemin de fer
land = la terre
a tribe = une tribu
a war = une guerre
a buffalo = un bison
""", [
 ("À qui les États-Unis achètent-ils la Louisiane en 1803 ?", ["À Napoléon, pour la France", "À l'Espagne", "Au Royaume-Uni"], ""),
 ("Que signifie « destinée manifeste » ?", ["L'idée que les États-Unis doivent s'étendre sur tout le continent", "Un traité de paix", "Un tableau célèbre"], ""),
 ("Que perd le Mexique après la guerre de 1846-1848 ?", ["Environ la moitié de son territoire", "Sa capitale", "Rien du tout"], ""),
 ("Que donne le Homestead Act de 1862 ?", ["Des terres gratuites à ceux qui les cultivent", "De l'or", "Des chevaux"], ""),
 ("Qu'est-ce que la « Piste des larmes » ?", ["La déportation des Cherokees, où des milliers meurent", "Une route vers la Californie", "Une chanson"], ""),
 ("Que se passe-t-il à Wounded Knee en 1890 ?", ["L'armée massacre des centaines de Lakotas", "Une victoire amérindienne", "La fin de la ruée vers l'or"], ""),
])

N1_["cu_red_scare.html"] = ("""
fear = la peur
a spy = un espion
a list = une liste
to accuse = accuser
a witch hunt = une chasse aux sorcières
proof = la preuve
a writer = un écrivain
a trial = un procès
""", [
 ("Qu'est-ce qui déclenche la première peur rouge en 1919 ?", ["La révolution russe et la peur d'une révolution aux États-Unis", "La crise de 1929", "Le 11 septembre"], ""),
 ("Que demande la commission HUAC aux artistes ?", ["S'ils sont ou ont été communistes, et de dénoncer des collègues", "De tourner des films de guerre", "De payer plus d'impôts"], ""),
 ("Que se passe-t-il pour les artistes sur la « blacklist » ?", ["Ils ne trouvent plus de travail", "Ils deviennent célèbres", "Ils partent en vacances"], ""),
 ("Que désigne le mot « maccarthysme » ?", ["Accuser des gens sans preuve", "Une danse des années 50", "Un parti politique"], ""),
 ("Pourquoi McCarthy perd-il sa popularité en 1954 ?", ["Ses méthodes brutales sont vues à la télévision", "Il devient communiste", "Il perd une élection à Hollywood"], ""),
 ("De quoi parle vraiment The Crucible d'Arthur Miller ?", ["Du maccarthysme, à travers les procès de sorcières de Salem", "D'un voyage sur la Lune", "De la guerre de Sécession"], ""),
])

N1_["cu_watergate.html"] = ("""
a scandal = un scandale
a journalist = un journaliste
a tape = une bande, un enregistrement
to resign = démissionner
a lie = un mensonge
a secret = un secret
a burglar = un cambrioleur
the truth = la vérité
""", [
 ("Que cherchaient les cinq hommes arrêtés au Watergate ?", ["À installer des micros chez les démocrates", "À voler de l'argent", "À rencontrer le président"], ""),
 ("Quel journal révèle l'affaire ?", ["The Washington Post", "The Sun", "Le Monde"], "Woodward et Bernstein."),
 ("Qui était « Deep Throat » ?", ["Mark Felt, numéro deux du FBI", "Un chanteur", "Le vice-président"], "Révélé en 2005."),
 ("Pourquoi les enregistrements secrets sont-ils si importants ?", ["Ils prouvent que Nixon a voulu bloquer l'enquête", "Ils contiennent de la musique", "Ils innocentent Nixon"], ""),
 ("Que fait Nixon le 9 août 1974 ?", ["Il démissionne", "Il est réélu", "Il part sur la Lune"], "Le seul président à l'avoir fait."),
 ("Que désigne aujourd'hui le suffixe « -gate » ?", ["Un scandale", "Une porte", "Une victoire"], ""),
])

N1_["cu_televangelisme.html"] = ("""
a preacher = un prédicateur
a church = une église
faith = la foi
a prayer = une prière
money = l'argent
a donation = un don
television = la télévision
a believer = un croyant
""", [
 ("Comment s'appellent les protestants qui insistent sur la conversion personnelle ?", ["Les évangéliques", "Les catholiques", "Les orthodoxes"], ""),
 ("Qui remplit des stades avec ses « crusades » ?", ["Billy Graham", "Jim Bakker", "Elvis Presley"], ""),
 ("Que dit la « prosperity gospel » ?", ["Que Dieu récompense les donateurs par la richesse", "Qu'il faut être pauvre", "Qu'il ne faut pas regarder la télévision"], ""),
 ("Quel mouvement Jerry Falwell crée-t-il en 1979 ?", ["La Moral Majority", "Le Parti démocrate", "Une chaîne sportive"], ""),
 ("Pourquoi Jim Bakker est-il condamné en 1989 ?", ["Pour avoir détourné l'argent de ses fidèles", "Pour avoir chanté faux", "Pour excès de vitesse"], ""),
 ("Que critiquent les adversaires des télévangélistes ?", ["L'enrichissement et le mélange religion-politique", "Leurs sermons trop courts", "Leurs églises trop petites"], ""),
])

N1_["cu_armes_usa.html"] = ("""
a gun = une arme à feu
a weapon = une arme
a school = une école
a law = une loi
safety = la sécurité
a victim = une victime
hunting = la chasse
a survivor = un survivant
""", [
 ("Que protège le deuxième amendement ?", ["Le droit de détenir et de porter des armes", "La liberté de la presse", "Le droit de vote"], ""),
 ("Qu'a décidé la Cour suprême en 2008 ?", ["Le droit à une arme est un droit individuel", "Les armes sont interdites", "Seule l'armée peut avoir des armes"], ""),
 ("Qu'est-ce que la NRA ?", ["Un lobby très puissant qui défend les armes", "Une école", "Une loi"], ""),
 ("Que lancent les lycéens survivants de Parkland en 2018 ?", ["Le mouvement March for Our Lives", "Un club de tir", "Une chaîne de télévision"], ""),
 ("Que demandent les partisans du « gun control » ?", ["Des vérifications d'antécédents et l'interdiction des fusils d'assaut", "Plus d'armes dans les écoles", "La fin de la police"], ""),
 ("Que répondent les défenseurs des armes ?", ["Les criminels ne respectent pas les lois, le problème est la santé mentale", "Il faut tout interdire", "Les armes sont trop chères"], ""),
])

N1_["cu_pilgrims.html"] = ("""
a ship = un navire
a settler = un colon
a harvest = une récolte
corn = le maïs
tea = le thé
a tax = un impôt, une taxe
freedom = la liberté
a war = une guerre
""", [
 ("Pourquoi les Pilgrims quittent-ils l'Angleterre ?", ["Pour pratiquer librement leur religion", "Pour chercher de l'or", "Pour fuir une guerre"], ""),
 ("Qui aide les colons à survivre ?", ["Les Wampanoag", "Les Français", "Les Espagnols"], ""),
 ("Que célèbre-t-on à Thanksgiving ?", ["Un repas de récolte partagé en 1621", "L'indépendance", "La fin de l'esclavage"], ""),
 ("Pourquoi Thanksgiving est-il un jour de deuil pour certains Amérindiens ?", ["L'arrivée des colons a entraîné la perte de leurs terres et des guerres", "C'est un jour de pluie", "Ils n'aiment pas la dinde"], ""),
 ("Que signifie « No taxation without representation » ?", ["Pas d'impôts sans représentants au Parlement", "Plus aucun impôt", "Des impôts pour tous"], ""),
 ("Qu'est-ce que la Boston Tea Party ?", ["Des colons jettent du thé britannique à la mer", "Une fête avec du thé", "Un parti politique"], ""),
])

N1_["cu_esclavage.html"] = ("""
a slave = un esclave
slavery = l'esclavage
a plantation = une plantation
cotton = le coton
to escape = s'échapper
freedom = la liberté
a war = une guerre
a soldier = un soldat
""", [
 ("Combien d'Africains environ sont déportés vers les Amériques par la traite ?", ["Environ 12 millions", "Environ 12 000", "Environ 1 milliard"], ""),
 ("Qu'est-ce que l'Underground Railroad ?", ["Un réseau secret qui aide les esclaves à fuir", "Un vrai métro", "Une ligne de chemin de fer du Sud"], ""),
 ("Qui est Harriet Tubman ?", ["Une esclave évadée qui en a libéré beaucoup d'autres", "Une présidente", "Une générale sudiste"], ""),
 ("Pourquoi onze États du Sud font-ils sécession ?", ["Après l'élection de Lincoln, opposé à l'extension de l'esclavage", "Pour rejoindre le Mexique", "À cause d'un impôt sur le thé"], ""),
 ("Quel amendement abolit l'esclavage en 1865 ?", ["Le 13e", "Le 1er", "Le 2e"], ""),
 ("Que sont les lois « Jim Crow » ?", ["Des lois de ségrégation dans le Sud", "Des lois contre l'esclavage", "Des lois sur les impôts"], ""),
])

N1_["cu_droits_civiques.html"] = ("""
segregation = la ségrégation
a bus = un bus
a seat = un siège, une place
a march = une marche
a dream = un rêve
equality = l'égalité
a right = un droit
non-violence = la non-violence
""", [
 ("Que signifie « separate but equal » ?", ["Une ségrégation officiellement « égale » mais en réalité injuste", "La fin de la ségrégation", "L'égalité totale"], ""),
 ("Que fait Rosa Parks le 1er décembre 1955 ?", ["Elle refuse de céder sa place à un Blanc dans un bus", "Elle devient présidente", "Elle organise un concert"], ""),
 ("Combien de temps dure le boycott des bus de Montgomery ?", ["381 jours", "3 jours", "10 ans"], ""),
 ("Qui inspire la non-violence de Martin Luther King ?", ["Gandhi", "Lincoln", "Malcolm X"], ""),
 ("Que se passe-t-il le 28 août 1963 ?", ["La marche sur Washington et le discours « I have a dream »", "L'assassinat de Kennedy", "La fin de l'esclavage"], ""),
 ("Que défend Malcolm X, contrairement à King ?", ["La fierté noire et le droit à l'autodéfense", "La ségrégation", "L'esclavage"], ""),
])

N1_["cu_ellis_island.html"] = ("""
an immigrant = un immigrant
an island = une île
a doctor = un médecin
a dream = un rêve
poverty = la pauvreté
a statue = une statue
a neighbourhood = un quartier
hard work = le travail acharné
""", [
 ("Qui a offert la statue de la Liberté ?", ["La France", "Le Royaume-Uni", "L'Italie"], ""),
 ("Combien de personnes environ passent par Ellis Island ?", ["12 millions", "12 000", "120 millions"], ""),
 ("Pourquoi les immigrants passent-ils devant des médecins ?", ["Pour repérer les malades, qui pouvaient être renvoyés", "Pour être vaccinés contre le froid", "Pour devenir médecins"], ""),
 ("Que signifie le « rêve américain » ?", ["Chacun peut réussir par son travail", "Tout le monde devient acteur", "On ne travaille plus"], ""),
 ("Que font les lois de quotas des années 1920 ?", ["Elles limitent l'immigration selon les pays d'origine", "Elles ouvrent les frontières", "Elles ferment New York"], ""),
 ("Quelle est la différence entre « melting pot » et « salad bowl » ?", ["Dans le salad bowl, chaque culture garde son identité", "Aucune", "Le melting pot refuse les immigrés"], ""),
])

N1_["cu_1929_new_deal.html"] = ("""
the stock market = la Bourse
a bank = une banque
a crash = un krach
unemployment = le chômage
dust = la poussière
a farm = une ferme
a job = un emploi
hope = l'espoir
""", [
 ("Que se passe-t-il en octobre 1929 ?", ["La Bourse de Wall Street s'effondre", "Roosevelt est élu", "La Prohibition commence"], ""),
 ("Quelle proportion de travailleurs est au chômage en 1933 ?", ["Environ un quart", "Presque personne", "La moitié"], ""),
 ("Que sont les « Hoovervilles » ?", ["Des bidonvilles de sans-abri", "Des quartiers riches", "Des usines"], ""),
 ("Qu'est-ce que le Dust Bowl ?", ["Des tempêtes de poussière qui détruisent les fermes", "Un match de football", "Une banque"], ""),
 ("Que propose Roosevelt avec le New Deal ?", ["Des aides, de grands travaux et des réformes", "La fin de toutes les aides", "Une guerre"], ""),
 ("Que sont les « fireside chats » ?", ["Les causeries radio de Roosevelt", "Des feux de camp", "Des réunions secrètes"], ""),
])

N1_["cu_vietnam.html"] = ("""
a war = une guerre
a soldier = un soldat
peace = la paix
a student = un étudiant
a festival = un festival
a protest = une manifestation
a veteran = un ancien combattant
the jungle = la jungle
""", [
 ("Pourquoi les États-Unis s'engagent-ils au Vietnam ?", ["Pour empêcher l'extension du communisme (théorie des dominos)", "Pour conquérir du pétrole", "Pour aider la France"], ""),
 ("Pourquoi parle-t-on de « première guerre télévisée » ?", ["Les Américains voient chaque soir des images des combats", "Elle a été filmée par Hollywood", "Elle a duré un jour"], ""),
 ("Que fait Muhammad Ali ?", ["Il refuse de partir à la guerre et perd son titre", "Il devient général", "Il chante à Woodstock"], ""),
 ("Que se passe-t-il à Kent State en 1970 ?", ["La Garde nationale tue quatre étudiants", "Un grand concert", "La fin de la guerre"], ""),
 ("Que prônent les hippies ?", ["« Peace and love »", "La guerre", "La richesse"], ""),
 ("Combien d'Américains sont morts au Vietnam ?", ["Environ 58 000", "Environ 500", "Environ 5 millions"], ""),
])

N1_["cu_11_septembre.html"] = ("""
a plane = un avion
a tower = une tour
a terrorist = un terroriste
a firefighter = un pompier
security = la sécurité
an attack = une attaque, un attentat
a victim = une victime
a memorial = un mémorial
""", [
 ("Combien d'avions sont détournés le 11 septembre 2001 ?", ["Quatre", "Deux", "Dix"], ""),
 ("Que se passe-t-il dans le quatrième avion ?", ["Les passagers se révoltent et l'avion s'écrase en Pennsylvanie", "Il atterrit normalement", "Il frappe la Maison-Blanche"], ""),
 ("Combien de personnes meurent ?", ["Près de 3 000", "Près de 30", "Près de 300 000"], ""),
 ("Que déclare George W. Bush ?", ["La « guerre contre le terrorisme »", "La fin des avions", "La paix avec al-Qaïda"], ""),
 ("Pourquoi la guerre d'Irak (2003) est-elle très contestée ?", ["Les armes de destruction massive n'ont jamais été trouvées", "Elle a duré un jour", "L'Irak a attaqué en premier"], ""),
 ("Qu'est-ce qui a changé dans la vie quotidienne ?", ["Des contrôles beaucoup plus stricts dans les aéroports", "La fin des avions", "Rien"], ""),
])

N1_["cu_conquete_spatiale.html"] = ("""
the Moon = la Lune
a rocket = une fusée
space = l'espace
an astronaut = un astronaute
to land = atterrir, se poser
a satellite = un satellite
a step = un pas
Earth = la Terre
""", [
 ("Pourquoi Spoutnik choque-t-il les Américains en 1957 ?", ["Les Soviétiques ont pris de l'avance technologique", "Il tombe sur New York", "Il fait du bruit"], ""),
 ("Qui est le premier homme dans l'espace ?", ["Youri Gagarine", "Neil Armstrong", "John Glenn"], ""),
 ("Quel objectif Kennedy fixe-t-il en 1961 ?", ["Envoyer un homme sur la Lune avant la fin de la décennie", "Aller sur Mars", "Arrêter la conquête spatiale"], ""),
 ("Qui est Katherine Johnson ?", ["Une mathématicienne de la NASA dont les calculs étaient essentiels", "Une astronaute", "Une présidente"], ""),
 ("Qui marche sur la Lune le 20 juillet 1969 ?", ["Neil Armstrong et Buzz Aldrin", "Michael Collins seul", "Gagarine"], "Collins reste en orbite."),
 ("Quel programme doit ramener des humains sur la Lune ?", ["Artemis", "Apollo", "Sputnik"], ""),
])

N1_["cu_lycee_us.html"] = ("""
a locker = un casier
a grade = une note, une classe
a dance = un bal
a team = une équipe
a club = un club
a hallway = un couloir
a diploma = un diplôme
a bus = un bus
""", [
 ("Combien d'années dure la high school ?", ["Quatre", "Deux", "Six"], ""),
 ("Comment appelle-t-on un élève de dernière année ?", ["Un senior", "Un freshman", "Un sophomore"], ""),
 ("Que range-t-on dans un « locker » ?", ["Ses affaires", "Sa voiture", "Ses notes"], ""),
 ("Qu'est-ce que le GPA ?", ["La moyenne des notes", "Un sport", "Un bal"], ""),
 ("Qu'est-ce que le « prom » ?", ["Le bal de fin d'année", "Un examen", "Un club de sport"], ""),
 ("Que lancent les élèves en l'air à la graduation ?", ["Leur toque", "Leurs livres", "Leurs chaussures"], ""),
])

N1_["cu_elections_us.html"] = ("""
an election = une élection
a candidate = un candidat
a vote = un vote, une voix
a debate = un débat
a campaign = une campagne
a party = un parti
to win = gagner
a voter = un électeur
""", [
 ("À quoi servent les primaires ?", ["À choisir le candidat de chaque parti", "À élire le président directement", "À choisir les juges"], ""),
 ("Combien de grands électeurs faut-il pour gagner ?", ["270", "538", "50"], ""),
 ("Que signifie « winner-takes-all » ?", ["Le candidat en tête dans un État remporte tous ses grands électeurs", "Le gagnant prend tout l'argent", "Il n'y a qu'un candidat"], ""),
 ("Qu'est-ce qu'un « swing state » ?", ["Un État où le résultat est incertain", "Un État qui vote toujours pareil", "Un État sans élection"], ""),
 ("Un candidat peut-il gagner sans la majorité des voix nationales ?", ["Oui, c'est arrivé en 2000 et 2016", "Non, jamais", "Seulement au Texas"], ""),
 ("Quand le nouveau président prête-t-il serment ?", ["Le 20 janvier", "Le 4 juillet", "Le jour de l'élection"], ""),
])

N1_["cu_amerindiens.html"] = ("""
a tribe = une tribu
a reservation = une réserve
a language = une langue
a school = une école
a right = un droit
water = l'eau
sacred = sacré
a child = un enfant
""", [
 ("Qu'est-ce qui a tué une grande partie des Amérindiens avant même les guerres ?", ["Les maladies apportées par les Européens", "Le froid", "Les tempêtes"], ""),
 ("Qu'est-ce qu'une réserve ?", ["Une terre qui appartient à une tribu", "Un hôtel", "Un parc d'attractions"], ""),
 ("Que voulaient les pensionnats (boarding schools) ?", ["Faire abandonner aux enfants leur culture", "Leur apprendre leur langue", "Former des sportifs"], ""),
 ("Quand les Amérindiens deviennent-ils citoyens américains ?", ["En 1924", "En 1776", "En 2000"], ""),
 ("Pourquoi des milliers de personnes manifestent-elles à Standing Rock en 2016 ?", ["Contre un oléoduc qui menace l'eau et des sites sacrés", "Pour un casino", "Pour un match"], ""),
 ("Qui est Deb Haaland ?", ["La première Amérindienne ministre fédérale", "Une championne de tennis", "Une chef de 1830"], ""),
])
