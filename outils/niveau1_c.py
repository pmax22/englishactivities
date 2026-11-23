import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
N1_ = {}

N1_["cu_anglophone.html"] = ("""
a language = une langue
a speaker = un locuteur
a country = un pays
an accent = un accent
a word = un mot
the world = le monde
to speak = parler
an island = une île
""", [
 ("Pourquoi dit-on « pork » pour la viande de porc ?", ["Le mot vient du français, après la conquête normande de 1066", "C'est un mot viking", "C'est un mot américain"], ""),
 ("Quelles sont les deux grandes vagues de diffusion de l'anglais ?", ["L'Empire britannique puis la puissance des États-Unis", "La Renaissance puis la Révolution française", "Les Vikings puis les Romains"], ""),
 ("Combien de personnes environ parlent anglais ?", ["1,5 milliard", "15 millions", "8 milliards"], "Dont environ 380 millions de natifs."),
 ("Qu'est-ce qu'une « lingua franca » ?", ["Une langue commune entre personnes de langues différentes", "La langue française", "Une langue morte"], ""),
 ("Que sont les « World Englishes » ?", ["Les variétés d'anglais propres à chaque pays", "Des dictionnaires", "Des compétitions"], ""),
 ("Qui parle anglais le plus souvent dans le monde aujourd'hui ?", ["Des personnes dont ce n'est pas la langue maternelle", "Uniquement les Anglais", "Uniquement les Américains"], ""),
])

N1_["cu_australie.html"] = ("""
a convict = un bagnard
a prison = une prison
land = la terre
a child = un enfant
an apology = des excuses
a rock = un rocher
a fleet = une flotte
a culture = une culture
""", [
 ("Depuis combien de temps les Aborigènes vivent-ils en Australie ?", ["Au moins 65 000 ans", "200 ans", "2 000 ans"], ""),
 ("Pourquoi le Royaume-Uni envoie-t-il des bagnards en Australie ?", ["Il cherche un nouveau lieu pour ses condamnés après la perte de l'Amérique", "Pour trouver de l'or", "Pour faire du tourisme"], ""),
 ("Que signifie « terra nullius » ?", ["Une terre qui n'appartiendrait à personne", "Une terre sacrée", "Une prison"], ""),
 ("Que sont les « Stolen Generations » ?", ["Des enfants aborigènes retirés de force à leurs familles", "Des bagnards évadés", "Des sportifs"], ""),
 ("Que se passe-t-il le 13 février 2008 ?", ["Le Premier ministre présente des excuses officielles", "L'Australie devient une république", "La First Fleet arrive"], ""),
 ("Pourquoi certains appellent-ils le 26 janvier « Invasion Day » ?", ["Il marque le début de la colonisation", "C'est un jour de guerre contre le Japon", "C'est un match de cricket"], ""),
])

N1_["cu_afrique_sud.html"] = ("""
apartheid = l'apartheid
a prison = une prison
a pass = un laissez-passer
a vote = un vote
freedom = la liberté
a leader = un dirigeant
a student = un élève, un étudiant
peace = la paix
""", [
 ("Que signifie « apartheid » ?", ["Séparation", "Liberté", "Égalité"], ""),
 ("Que devaient porter les Noirs pour entrer dans les zones blanches ?", ["Un laissez-passer", "Un uniforme", "Un drapeau"], ""),
 ("Que se passe-t-il à Sharpeville en 1960 ?", ["La police tire sur une manifestation pacifique : 69 morts", "Mandela est libéré", "Des élections ont lieu"], ""),
 ("Pourquoi les élèves de Soweto manifestent-ils en 1976 ?", ["Contre l'enseignement imposé en afrikaans", "Pour plus de vacances", "Pour le rugby"], ""),
 ("Combien d'années Mandela passe-t-il en prison ?", ["27 ans", "2 ans", "50 ans"], ""),
 ("Que choisit Mandela au lieu de la vengeance ?", ["La réconciliation", "La guerre", "L'exil"], ""),
])

N1_["cu_inde.html"] = ("""
independence = l'indépendance
salt = le sel
a march = une marche
a border = une frontière
a refugee = un réfugié
non-violence = la non-violence
a festival = une fête
a film = un film
""", [
 ("Qu'est-ce que le « Raj » ?", ["La période de domination britannique directe sur l'Inde", "Un roi indien", "Une fête"], ""),
 ("Que défend Gandhi ?", ["La résistance non violente", "La lutte armée", "L'union avec le Royaume-Uni"], ""),
 ("Pourquoi Gandhi marche-t-il jusqu'à la mer en 1930 ?", ["Pour fabriquer du sel, en violation d'un monopole britannique", "Pour se baigner", "Pour quitter l'Inde"], ""),
 ("Qu'est-ce que la partition de 1947 ?", ["La division entre l'Inde et le Pakistan", "La fin de l'Empire romain", "Une guerre contre la Chine"], ""),
 ("Que se passe-t-il pendant la partition ?", ["Des millions de réfugiés et des centaines de milliers de morts", "Tout se passe dans le calme", "Rien de particulier"], ""),
 ("Qu'est-ce que Bollywood ?", ["L'industrie du cinéma de Mumbai", "Un sport", "Une fête des lumières"], ""),
])

N1_["cu_canada.html"] = ("""
a province = une province
French = le français
a maple leaf = une feuille d'érable
a school = une école
ice hockey = le hockey sur glace
a referendum = un référendum
a flag = un drapeau
abroad = à l'étranger
""", [
 ("Qui a fondé Québec en 1608 ?", ["Samuel de Champlain", "Jacques Cartier", "James Cook"], ""),
 ("Que célèbre le Canada Day, le 1er juillet ?", ["La Confédération de 1867", "La découverte de l'Amérique", "La fin de la guerre"], ""),
 ("Quelles sont les deux langues officielles du Canada ?", ["L'anglais et le français", "L'anglais et l'espagnol", "Le français et l'inuktitut"], ""),
 ("Qu'a donné le référendum québécois de 1995 ?", ["Le « non » l'emporte de justesse avec 50,6 %", "Le Québec devient indépendant", "Il n'a pas eu lieu"], ""),
 ("Que sont les « residential schools » ?", ["Des pensionnats où l'on voulait assimiler les enfants autochtones", "Des universités", "Des écoles de hockey"], ""),
 ("Quelle image le Canada donne-t-il de sa diversité ?", ["Une mosaïque", "Un melting pot", "Une prison"], ""),
])

N1_["cu_nouvelle_zelande.html"] = ("""
a treaty = un traité
a chief = un chef
a canoe = une pirogue
a bird = un oiseau
a dance = une danse
a volcano = un volcan
a tribe = une tribu
the right to vote = le droit de vote
""", [
 ("D'où viennent les Maoris ?", ["De Polynésie", "D'Australie", "D'Europe"], ""),
 ("Que veut dire « Aotearoa » ?", ["Le pays du long nuage blanc", "La terre des volcans", "L'île du nord"], ""),
 ("Quel est le problème du traité de Waitangi ?", ["Les versions anglaise et maorie ne disent pas la même chose", "Personne ne l'a signé", "Il est écrit en néerlandais"], ""),
 ("Que fait la Nouvelle-Zélande en 1893 ?", ["Elle est le premier pays autonome à donner le vote aux femmes", "Elle devient indépendante", "Elle invente le rugby"], ""),
 ("Pourquoi surnomme-t-on les Néo-Zélandais « Kiwis » ?", ["D'après un oiseau qui ne vole pas et ne vit que là", "D'après un fruit", "D'après une ville"], ""),
 ("Que font les All Blacks avant chaque match ?", ["Le haka, une danse maorie", "Une prière", "Un concert"], ""),
])

N1_["cu_jamaique.html"] = ("""
sugar = le sucre
a slave = un esclave
music = la musique
a singer = un chanteur
a runner = un coureur
a pirate = un pirate
an island = une île
freedom = la liberté
""", [
 ("Qui étaient les premiers habitants de la Jamaïque ?", ["Les Taïnos", "Les Maoris", "Les Vikings"], ""),
 ("Sur quoi reposait la richesse de la colonie ?", ["Les plantations de canne à sucre et l'esclavage", "Les mines d'or", "Le tourisme"], ""),
 ("Qui sont les Maroons ?", ["Des esclaves fugitifs qui ont formé des communautés libres", "Des pirates", "Des colons anglais"], ""),
 ("Quand la Jamaïque devient-elle indépendante ?", ["Le 6 août 1962", "En 1494", "En 2018"], ""),
 ("Quel artiste a rendu le reggae célèbre dans le monde entier ?", ["Bob Marley", "Elvis Presley", "Usain Bolt"], ""),
 ("Qu'est-ce que le patois jamaïcain ?", ["Un créole né de l'anglais et des langues africaines", "Une danse", "Un plat"], ""),
])

N1_["cu_musique.html"] = ("""
a song = une chanson
a singer = un chanteur
a band = un groupe
a guitar = une guitare
a record = un disque
a protest = une protestation
a party = une fête
a dance = une danse
""", [
 ("Que sont les spirituals ?", ["Des chants religieux d'espoir chantés par les esclaves", "Des danses de salon", "Des chansons de Noël anglaises"], ""),
 ("Où naît le jazz ?", ["À La Nouvelle-Orléans", "À Londres", "À Paris"], ""),
 ("Qu'est-ce que la « British Invasion » ?", ["Le succès des groupes britanniques aux États-Unis dans les années 60", "Une guerre", "Un festival"], ""),
 ("Qu'est-ce que Motown ?", ["Un label de Detroit qui a fait triompher des artistes noirs", "Une ville", "Une guitare"], ""),
 ("Que dénonce le punk londonien des années 70 ?", ["Le chômage et l'establishment", "La guerre du Vietnam", "L'esclavage"], ""),
 ("Où et quand naît le hip-hop ?", ["Dans le Bronx, à New York, en 1973", "À Londres en 1960", "À Paris en 1990"], ""),
])

N1_["cu_shakespeare.html"] = ("""
a play = une pièce de théâtre
a stage = une scène
an actor = un acteur
a poem = un poème
a king = un roi
a tragedy = une tragédie
a comedy = une comédie
a word = un mot
""", [
 ("Où est né Shakespeare ?", ["À Stratford-upon-Avon", "À Londres", "À Édimbourg"], ""),
 ("Comment était le Globe Theatre ?", ["Un théâtre rond en bois, à ciel ouvert", "Un grand cinéma", "Un théâtre en pierre fermé"], ""),
 ("Qui sont les « groundlings » ?", ["Les spectateurs pauvres, debout devant la scène", "Les acteurs", "Les rois"], ""),
 ("Qui jouait les rôles de femmes ?", ["De jeunes garçons", "Des actrices", "Personne"], ""),
 ("Quelle expression vient de Shakespeare ?", ["« To break the ice »", "« Keep calm and carry on »", "« Yes we can »"], ""),
 ("Pourquoi le First Folio est-il si important ?", ["Sans lui, la moitié de ses pièces auraient été perdues", "C'est son premier poème", "C'est un théâtre"], ""),
])

N1_["cu_grandes_figures.html"] = ("""
a nurse = une infirmière
a code = un code
a hero = un héros
a prize = un prix
courage = le courage
a school = une école
a bus = un bus
a computer = un ordinateur
""", [
 ("Pourquoi appelle-t-on Florence Nightingale « la dame à la lampe » ?", ["Elle visitait les malades la nuit avec une lampe", "Elle vendait des lampes", "Elle a inventé l'électricité"], ""),
 ("Quel code Alan Turing a-t-il aidé à déchiffrer ?", ["Enigma, le code de l'armée allemande", "Le code de la route", "Le code Morse"], ""),
 ("Pourquoi Turing a-t-il été condamné en 1952 ?", ["Pour homosexualité, alors illégale", "Pour espionnage", "Pour vol"], "Il a été gracié en 2013."),
 ("Que montre l'histoire de Rosa Parks ?", ["Elle était une militante qui refusait de céder, pas seulement « fatiguée »", "Elle était chauffeuse de bus", "Elle était présidente"], ""),
 ("Comment appelle-t-on affectueusement Mandela ?", ["Madiba", "Mahatma", "Iron Lady"], ""),
 ("Pour quoi Malala se bat-elle ?", ["Le droit des filles à aller à l'école", "Le droit de vote", "Le sport féminin"], ""),
])

N1_["cu_medias.html"] = ("""
a newspaper = un journal
a headline = un gros titre
a journalist = un journaliste
the news = les informations
a source = une source
fake = faux
a video = une vidéo
to check = vérifier
""", [
 ("Qu'est-ce qu'un tabloïd ?", ["Un journal populaire avec gros titres, célébrités et scandales", "Un journal d'analyse sérieux", "Une chaîne de télévision"], ""),
 ("Pourquoi le News of the World a-t-il fermé en 2011 ?", ["Ses journalistes piratent des téléphones", "Il n'avait plus de lecteurs", "Il a gagné un prix"], ""),
 ("Comment la BBC est-elle financée ?", ["Par une redevance payée par les foyers", "Par la publicité", "Par le roi"], ""),
 ("Qu'est-ce qu'une « echo chamber » ?", ["S'informer seulement par des médias qui confirment ses opinions", "Une salle de concert", "Un journal anglais"], ""),
 ("Qu'est-ce qu'un deepfake ?", ["Une vidéo truquée par l'intelligence artificielle", "Un journal", "Un jeu vidéo"], ""),
 ("Quel est un bon réflexe face à une information choquante ?", ["Vérifier si d'autres médias sérieux en parlent", "La partager tout de suite", "La croire si elle est drôle"], ""),
])
