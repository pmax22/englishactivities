import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
N1_ = {}

N1_["cu_uk.html"] = ("""
flag = drapeau
king = roi
island = île
capital = capitale
patron saint = saint patron
to drive on the left = rouler à gauche
the pound = la livre sterling
a nation = une nation
""", [
 ("Que désigne « Great Britain » ?", ["L'île qui réunit l'Angleterre, l'Écosse et le pays de Galles", "Le Royaume-Uni tout entier", "L'Angleterre seule"], "L'Irlande du Nord n'est pas sur l'île de Grande-Bretagne."),
 ("Pourquoi peut-on vexer un Écossais en l'appelant « English » ?", ["Parce que l'Angleterre n'est qu'une des quatre nations", "Parce que les Écossais ne parlent pas anglais", "Parce que l'Écosse n'est pas en Europe"], "On dit British pour tous les habitants du Royaume-Uni."),
 ("Quelles croix forment le Union Jack ?", ["Celles de saint George, saint Andrew et saint Patrick", "Celles de saint David et saint George", "Une seule croix rouge"], "Le pays de Galles n'y figure pas."),
 ("Quel symbole figure sur le drapeau gallois ?", ["Un dragon rouge", "Un lion", "Une harpe"], ""),
 ("Quelle est la monnaie du Royaume-Uni ?", ["La livre sterling", "L'euro", "Le dollar"], "Le Royaume-Uni n'a jamais adopté l'euro."),
 ("Qu'est-ce que la « devolution » ?", ["Des parlements propres à l'Écosse, au pays de Galles et à l'Irlande du Nord", "La sortie de l'Union européenne", "Le retour d'un roi"], "Depuis 1999."),
])

N1_["cu_monarchie.html"] = ("""
king = roi
queen = reine
the throne = le trône
the heir = l'héritier
a coronation = un couronnement
to reign = régner
the Crown = la Couronne
head of state = chef de l'État
""", [
 ("Que signifie « monarchie constitutionnelle » ?", ["Le roi est chef de l'État mais le pouvoir appartient au Parlement et au gouvernement", "Le roi décide de toutes les lois", "Il n'y a pas de roi"], ""),
 ("Pourquoi Henry VIII crée-t-il l'Église d'Angleterre ?", ["Pour pouvoir divorcer malgré le refus du pape", "Pour devenir pape", "Pour faire la guerre à la France"], "En 1534."),
 ("Combien de temps Elizabeth II a-t-elle régné ?", ["70 ans", "25 ans", "63 ans"], "Un record absolu."),
 ("Qui écrit le King's Speech ?", ["Le gouvernement", "Le roi lui-même", "Les journalistes"], "Le roi doit rester neutre."),
 ("Que reprochent les « republicans » à la monarchie ?", ["Son coût et ses privilèges héréditaires", "Son manque de châteaux", "Sa religion"], "Ils préféreraient un chef d'État élu."),
 ("Quel texte de 1689 affirme la supériorité du Parlement sur le roi ?", ["Le Bill of Rights", "La Magna Carta", "Le Brexit"], "La Magna Carta date de 1215."),
])

N1_["cu_institutions_uk.html"] = ("""
Parliament = le Parlement
an MP = un député
an election = une élection
a party = un parti
a majority = une majorité
the Prime Minister = le Premier ministre
a vote = une voix, un vote
a law = une loi
""", [
 ("Qu'a de particulier la constitution britannique ?", ["Elle n'est pas écrite dans un seul texte", "Elle a été écrite en 1958", "Elle est rédigée en français"], "On parle d'uncodified constitution."),
 ("Combien de députés siègent à la Chambre des communes ?", ["650", "100", "577"], ""),
 ("Comment sont choisis la plupart des membres de la Chambre des lords ?", ["Ils sont nommés à vie", "Ils sont élus tous les 5 ans", "Ils sont tirés au sort"], ""),
 ("Où vit le Premier ministre ?", ["Au 10 Downing Street", "À Buckingham Palace", "À la Tour de Londres"], ""),
 ("Que permet le système « first past the post » ?", ["Le candidat arrivé en tête gagne, même sans majorité absolue", "Le plus âgé gagne", "Il y a toujours deux tours"], "Il favorise les grands partis."),
 ("Qu'est-ce que le « Shadow Cabinet » ?", ["Le gouvernement fantôme de l'opposition", "Une pièce secrète du Parlement", "Les ministres du roi"], ""),
])

N1_["cu_empire.html"] = ("""
an empire = un empire
a colony = une colonie
a settler = un colon
independence = l'indépendance
a dominion = un dominion
the Royal Navy = la marine royale
slavery = l'esclavage
to rule = gouverner, dominer
""", [
 ("Sur quoi reposait la puissance de l'Empire britannique ?", ["La Royal Navy et le commerce", "Les montagnes", "L'euro"], "Mais aussi sur la traite des esclaves."),
 ("Quelle part du monde l'Empire couvrait-il à son apogée ?", ["Environ un quart", "La moitié", "Un dixième"], ""),
 ("Qu'est-ce qu'un dominion ?", ["Une colonie de peuplement devenue autonome", "Un château royal", "Une prison"], "Canada, Australie, Nouvelle-Zélande…"),
 ("Que change le Statut de Westminster en 1931 ?", ["Les dominions deviennent égaux au Royaume-Uni", "L'Empire est créé", "L'Inde devient indépendante"], ""),
 ("Que se passe-t-il en Inde en 1947 ?", ["L'indépendance et la partition avec le Pakistan", "Une victoire britannique", "L'arrivée de la reine Victoria"], ""),
 ("Qu'est-ce que le Commonwealth aujourd'hui ?", ["Une association libre de 56 pays", "Un nouvel empire", "Une équipe de football"], ""),
])

N1_["cu_brexit.html"] = ("""
to leave = partir, quitter
to remain = rester
a referendum = un référendum
a deal = un accord
a border = une frontière
sovereignty = la souveraineté
a voter = un électeur
trade = le commerce
""", [
 ("En quelle année le Royaume-Uni entre-t-il dans la Communauté européenne ?", ["1973", "1957", "2016"], ""),
 ("Qui organise le référendum de 2016 ?", ["David Cameron", "Boris Johnson", "Margaret Thatcher"], ""),
 ("Quel score obtient le « Leave » ?", ["51,9 %", "75 %", "48,1 %"], ""),
 ("Que veut dire le slogan « Take back control » ?", ["Reprendre le contrôle des lois, de l'immigration et de l'argent", "Contrôler la météo", "Garder l'euro"], ""),
 ("Quelles nations ont voté pour rester dans l'UE ?", ["L'Écosse et l'Irlande du Nord", "L'Angleterre et le pays de Galles", "Toutes"], ""),
 ("Pourquoi la frontière irlandaise était-elle un casse-tête ?", ["Personne ne voulait rétablir une frontière dure à cause de l'accord de paix", "Elle était trop longue", "L'Irlande voulait quitter l'UE"], ""),
])

N1_["cu_famine.html"] = ("""
famine = la famine
a potato = une pomme de terre
a landlord = un propriétaire
to emigrate = émigrer
hunger = la faim
a disease = une maladie
an eviction = une expulsion
a ship = un bateau
""", [
 ("Pourquoi les paysans irlandais dépendaient-ils de la pomme de terre ?", ["Elle poussait bien sur leurs petites parcelles et les nourrissait", "Ils la vendaient très cher", "C'était obligatoire"], ""),
 ("Qu'est-ce qui détruit les récoltes en 1845 ?", ["Le mildiou, un champignon", "Une guerre", "Une inondation"], "Potato blight."),
 ("Comment appelle-t-on l'année la plus terrible ?", ["Black '47", "Black Friday", "The Great Year"], ""),
 ("Que pense une partie du gouvernement britannique ?", ["Que l'État ne doit pas perturber le marché (laissez-faire)", "Qu'il faut nourrir tout le monde gratuitement", "Qu'il faut rendre l'Irlande indépendante"], ""),
 ("Combien de personnes environ meurent ?", ["Un million", "Dix mille", "Dix millions"], "Et plus d'un million émigrent."),
 ("Quelle est une conséquence durable de la famine ?", ["Une immense diaspora irlandaise, notamment aux États-Unis", "La disparition de la langue anglaise", "La fin de la pomme de terre"], ""),
])

N1_["cu_troubles.html"] = ("""
a march = une marche, une manifestation
civil rights = les droits civiques
a soldier = un soldat
a prisoner = un prisonnier
a hunger strike = une grève de la faim
peace = la paix
a wall = un mur
an agreement = un accord
""", [
 ("De quoi souffraient les catholiques d'Irlande du Nord ?", ["De discriminations pour le logement, l'emploi et le vote", "D'un manque de pluie", "D'une interdiction de parler anglais"], ""),
 ("Que permet l'« internment » en 1971 ?", ["D'emprisonner sans procès", "De voter à 16 ans", "De quitter le pays"], ""),
 ("Que se passe-t-il le 30 janvier 1972 à Derry ?", ["Des parachutistes tirent sur une marche pacifique : 14 morts", "Un accord de paix est signé", "Un attentat contre la reine"], ""),
 ("Qu'est-ce que le « blanket protest » ?", ["Des prisonniers refusent l'uniforme et portent une couverture", "Une manifestation contre le froid", "Une grève des mineurs"], ""),
 ("Qui est Bobby Sands ?", ["Un prisonnier républicain élu député, mort après 66 jours de grève de la faim", "Un Premier ministre britannique", "Un juge"], ""),
 ("Que prévoit l'accord du Vendredi saint (1998) ?", ["Un gouvernement partagé et le maintien dans le Royaume-Uni tant que la majorité le veut", "L'indépendance immédiate", "Le départ de tous les protestants"], ""),
])

N1_["cu_vie_uk.html"] = ("""
a uniform = un uniforme
a doctor = un médecin
tea = le thé
a pub = un pub, un bar
a queue = une file d'attente
an exam = un examen
free = gratuit
a pupil = un élève
""", [
 ("Pourquoi les élèves portent-ils un uniforme ?", ["Pour gommer les différences sociales et créer un sentiment d'appartenance", "Parce qu'il fait froid", "Pour faire du sport"], ""),
 ("Qu'est-ce qu'une « public school » au Royaume-Uni ?", ["Une école privée très chère et prestigieuse", "Une école publique gratuite", "Une université"], "Comme Eton."),
 ("Que veut dire « free at the point of use » pour le NHS ?", ["On ne paie pas au moment des soins", "Les médecins travaillent gratuitement", "Les hôpitaux sont fermés"], "Il est financé par l'impôt."),
 ("Au pub, comment paie-t-on souvent ?", ["Chacun paie une tournée à son tour", "On paie en partant", "On ne paie jamais"], "Les rounds."),
 ("Que faut-il éviter absolument à l'arrêt de bus ?", ["Passer devant tout le monde dans la file", "Dire sorry", "Parler de la météo"], ""),
 ("Quand la BBC a-t-elle été créée ?", ["1922", "1948", "2000"], ""),
])

N1_["cu_londres.html"] = ("""
the Tube = le métro de Londres
a bridge = un pont
a tower = une tour
a museum = un musée
a palace = un palais
a river = une rivière, un fleuve
a bell = une cloche
a fire = un incendie
""", [
 ("Qui a fondé Londres ?", ["Les Romains", "Les Vikings", "Les Américains"], "Londinium."),
 ("Que s'est-il passé en 1666 ?", ["Un grand incendie a détruit une grande partie de la ville", "Le métro a ouvert", "La reine est née"], ""),
 ("Qu'est-ce que Big Ben ?", ["La grande cloche de la tour du Parlement", "Un pont", "Un musée"], ""),
 ("Qu'est-ce que « The Knowledge » ?", ["L'examen des chauffeurs de black cab qui apprennent toutes les rues", "Un musée", "Une université"], ""),
 ("Que garde la Tour de Londres ?", ["Les joyaux de la Couronne", "Le Parlement", "Le métro"], ""),
 ("Que peut-on dire des grands musées londoniens ?", ["Beaucoup sont gratuits", "Ils sont tous fermés", "Ils sont réservés aux Anglais"], ""),
])

N1_["cu_ecosse_galles.html"] = ("""
a castle = un château
a lake = un lac
a mountain = une montagne
a flag = un drapeau
a language = une langue
a poem = un poème
a mine = une mine
independence = l'indépendance
""", [
 ("Qui sont William Wallace et Robert the Bruce ?", ["Des héros écossais qui ont résisté à l'Angleterre", "Des rois anglais", "Des chanteurs"], ""),
 ("Quand l'Écosse et l'Angleterre ont-elles uni leurs parlements ?", ["En 1707", "En 1999", "En 2014"], ""),
 ("Qu'a donné le référendum écossais de 2014 ?", ["55 % de « non » à l'indépendance", "Une large victoire du « oui »", "Il a été annulé"], ""),
 ("Pourquoi beaucoup d'Écossais ont-ils mal vécu le Brexit ?", ["Ils avaient voté à 62 % pour rester dans l'UE", "Ils voulaient l'euro", "Ils n'avaient pas voté"], ""),
 ("Qui porte le titre de « Prince of Wales » ?", ["Le fils aîné du roi", "Le Premier ministre gallois", "Le maire de Cardiff"], ""),
 ("Quelle est la situation du gallois aujourd'hui ?", ["Il renaît : enseigné à l'école, panneaux bilingues", "Il a disparu", "Il est interdit"], ""),
])

N1_["cu_revolution_industrielle.html"] = ("""
a factory = une usine
coal = le charbon
a machine = une machine
a worker = un ouvrier
a child = un enfant
a train = un train
smoke = la fumée
wages = le salaire
""", [
 ("Où et quand commence la révolution industrielle ?", ["En Grande-Bretagne, vers 1760", "En France, en 1900", "Aux États-Unis, en 1600"], ""),
 ("Quelle invention change tout ?", ["La machine à vapeur", "L'électricité", "Internet"], "Améliorée par James Watt."),
 ("Pourquoi surnomme-t-on Manchester « Cottonopolis » ?", ["C'est la capitale mondiale du coton", "Elle est faite en coton", "Il y pleut beaucoup"], ""),
 ("Pourquoi des enfants travaillaient-ils dans les usines ?", ["Ils coûtaient peu et pouvaient se glisser sous les machines", "Ils aimaient ça", "L'école était fermée"], ""),
 ("Que faisaient les Luddites ?", ["Ils cassaient les machines", "Ils construisaient des trains", "Ils écrivaient des romans"], ""),
 ("Quel écrivain dénonce la misère ouvrière ?", ["Charles Dickens", "Shakespeare", "J. K. Rowling"], "Oliver Twist, Hard Times."),
])

N1_["cu_suffragettes.html"] = ("""
the vote = le droit de vote
a woman = une femme
a prison = une prison
a protest = une protestation
equality = l'égalité
a window = une fenêtre
a newspaper = un journal
a right = un droit
""", [
 ("Quelle est la différence entre suffragists et suffragettes ?", ["Les suffragists sont pacifiques, les suffragettes plus radicales", "Il n'y en a aucune", "Les suffragettes sont des hommes"], ""),
 ("Qui fonde la WSPU en 1903 ?", ["Emmeline Pankhurst", "La reine Victoria", "Millicent Fawcett"], ""),
 ("D'où vient le mot « suffragette » ?", ["D'un journal qui voulait se moquer d'elles", "D'une chanson", "D'un roi"], "Elles l'ont adopté fièrement."),
 ("Que font les autorités aux grévistes de la faim en prison ?", ["Elles les nourrissent de force", "Elles les libèrent tout de suite", "Elles leur donnent le droit de vote"], ""),
 ("Quel rôle joue la Première Guerre mondiale ?", ["Les femmes remplacent les hommes au travail et prouvent leurs capacités", "Elle arrête le combat pour toujours", "Elle n'a aucun effet"], ""),
 ("En quelle année les femmes votent-elles à égalité avec les hommes ?", ["1928", "1918", "1945"], ""),
])

N1_["cu_blitz.html"] = ("""
a bomb = une bombe
a shelter = un abri
a plane = un avion
a pilot = un pilote
a speech = un discours
a siren = une sirène
to surrender = se rendre, capituler
courage = le courage
""", [
 ("Pourquoi le Royaume-Uni est-il seul en juin 1940 ?", ["La France a signé l'armistice", "Les États-Unis l'ont attaqué", "Il a quitté la guerre"], ""),
 ("Que se passe-t-il à Dunkerque ?", ["Plus de 300 000 soldats sont évacués par bateau", "Une victoire contre l'Allemagne", "La signature de la paix"], ""),
 ("Que gagne la RAF à l'été 1940 ?", ["La bataille d'Angleterre", "La bataille de Waterloo", "La Coupe du monde"], ""),
 ("Combien de nuits de suite Londres est-elle bombardée ?", ["57", "7", "365"], ""),
 ("Où se réfugient les Londoniens ?", ["Dans des abris et les stations de métro", "Dans les pubs", "En France"], ""),
 ("Qu'est-ce que le « Blitz spirit » ?", ["Le courage tranquille des Britanniques sous les bombes", "Une boisson", "Un avion"], ""),
])

N1_["cu_thatcher.html"] = ("""
a strike = une grève
a miner = un mineur
a trade union = un syndicat
unemployment = le chômage
a tax = un impôt
a war = une guerre
to privatise = privatiser
a riot = une émeute
""", [
 ("Qui est Margaret Thatcher ?", ["La première femme Premier ministre du Royaume-Uni", "Une reine", "Une chanteuse"], ""),
 ("Que fait-elle des grandes entreprises publiques ?", ["Elle les privatise", "Elle les nationalise", "Elle les ferme toutes"], ""),
 ("D'où vient le surnom « Iron Lady » ?", ["D'un journal soviétique, à cause de sa fermeté", "De son métier de forgeronne", "D'un film"], ""),
 ("Contre quel pays se fait la guerre des Malouines en 1982 ?", ["L'Argentine", "L'Espagne", "La France"], ""),
 ("Comment se termine la grève des mineurs ?", ["Par la défaite des mineurs", "Par la victoire des mineurs", "Par l'arrivée de l'armée américaine"], ""),
 ("Pourquoi Thatcher démissionne-t-elle en 1990 ?", ["Après les émeutes de la poll tax, son parti la pousse dehors", "Elle a perdu une guerre", "Elle est devenue reine"], ""),
])

N1_["cu_multiculturel.html"] = ("""
immigration = l'immigration
racism = le racisme
a carnival = un carnaval
a community = une communauté
a worker = un travailleur
diversity = la diversité
a law = une loi
a ship = un navire
""", [
 ("Pourquoi le Royaume-Uni fait-il appel aux habitants du Commonwealth après 1945 ?", ["Pour reconstruire le pays", "Pour faire la guerre", "Pour peupler l'Australie"], ""),
 ("Que voit-on sur certains panneaux des années 1950 ?", ["Des refus de louer aux Noirs et aux Irlandais", "Des publicités pour le thé", "Des horaires de bus"], ""),
 ("Pourquoi le carnaval de Notting Hill a-t-il été créé ?", ["Pour célébrer la culture caribéenne après des émeutes racistes", "Pour fêter la reine", "Pour la Coupe du monde"], ""),
 ("Quel plat est devenu très populaire au Royaume-Uni ?", ["Le curry", "La raclette", "Les sushis"], ""),
 ("Qu'a révélé le scandale Windrush en 2018 ?", ["Des personnes installées légalement ont été détenues ou expulsées", "Le bateau était trop vieux", "Les immigrés refusaient de travailler"], ""),
 ("Quelle part de la population d'Angleterre et du pays de Galles se déclarait non blanche en 2021 ?", ["Près d'une personne sur cinq", "La moitié", "Une personne sur cent"], ""),
])

N1_["cu_paques_1916.html"] = ("""
a rebel = un rebelle
a rising = une insurrection
to surrender = se rendre
an execution = une exécution
a treaty = un traité
a civil war = une guerre civile
a republic = une république
a leader = un chef
""", [
 ("Que réclamaient la plupart des Irlandais avant 1916 ?", ["Le Home Rule, une autonomie", "L'annexion par la France", "Le retour d'un roi irlandais"], ""),
 ("Que proclame Patrick Pearse devant la Grande Poste ?", ["La République irlandaise", "La fin de la guerre", "L'union avec l'Angleterre"], ""),
 ("Pourquoi l'opinion irlandaise change-t-elle après l'insurrection ?", ["Parce que les Britanniques exécutent les chefs", "Parce que les rebelles ont gagné", "Parce que la guerre s'arrête"], ""),
 ("Qui mène la guérilla de 1919-1921 ?", ["Michael Collins", "W. B. Yeats", "Winston Churchill"], ""),
 ("Qu'est-ce que la partition de l'Irlande ?", ["Six comtés du nord restent au Royaume-Uni", "L'Irlande est partagée avec la France", "Dublin devient britannique"], ""),
 ("Quand l'Irlande devient-elle une république ?", ["En 1949", "En 1916", "En 1922"], ""),
])

N1_["cu_irlande_auj.html"] = ("""
a republic = une république
growth = la croissance
a company = une entreprise
a referendum = un référendum
a writer = un écrivain
a language = une langue
fun = l'amusement
the Church = l'Église
""", [
 ("Comment s'appelle le chef du gouvernement irlandais ?", ["Le Taoiseach", "Le Président", "Le Speaker"], ""),
 ("Qu'est-ce que le « Celtic Tiger » ?", ["La forte croissance économique des années 1990", "Un animal sacré", "Une équipe de rugby"], ""),
 ("Pourquoi de grandes entreprises s'installent-elles à Dublin ?", ["Impôt bas, main-d'œuvre jeune et anglophone, fonds européens", "Il fait toujours beau", "Elles y sont obligées"], ""),
 ("Que s'est-il passé en 2015 ?", ["L'Irlande légalise le mariage homosexuel par référendum", "L'Irlande quitte l'UE", "La famine revient"], "Une première mondiale."),
 ("Où parle-t-on encore l'irlandais au quotidien ?", ["Dans la Gaeltacht, sur la côte ouest", "Partout à Dublin", "Nulle part"], ""),
 ("Que veut dire « craic » ?", ["L'ambiance, le fun", "Une crise", "Un sport"], ""),
])
