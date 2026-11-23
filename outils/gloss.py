import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
# Courtes explications ajoutées à la première mention d'un nom dans les dossiers.
G_ = {
"cu_uk.html": [
 ("devolution", "transfert de certains pouvoirs de Londres vers les nations"),
],
"cu_monarchie.html": [
 ("roi Jean", "Jean sans Terre, roi d'Angleterre de 1199 à 1216"),
 ("Glorious Revolution", "le roi catholique Jacques II est chassé et remplacé par sa fille Marie et son mari Guillaume d'Orange"),
 ("Invincible Armada", "immense flotte envoyée par le roi d'Espagne pour envahir l'Angleterre"),
 ("de Churchill à Liz Truss", "Churchill : Premier ministre pendant la Seconde Guerre mondiale ; Liz Truss : Première ministre en 2022, restée 49 jours"),
],
"cu_institutions_uk.html": [
 ("Shadow Cabinet", "les futurs ministres de l'opposition, chacun suivant un ministre en poste"),
],
"cu_empire.html": [
 ("East India Company", "compagnie de marchands britanniques créée en 1600 pour commercer avec l'Asie"),
 ("Mau Mau", "mouvement de rébellion kényan contre les colons britanniques, 1952-1960"),
 ("Windrush generation", "les immigrés caribéens arrivés après 1948"),
],
"cu_brexit.html": [
 ("Bruxelles", "siège des institutions européennes"),
 ("UKIP", "UK Independence Party, parti qui réclamait la sortie de l'UE"),
 ("David Cameron", "Premier ministre conservateur de 2010 à 2016"),
 ("Theresa May", "Première ministre conservatrice de 2016 à 2019"),
 ("Boris Johnson", "ancien maire de Londres, Premier ministre de 2019 à 2022"),
 ("unionistes", "partisans du maintien de l'Irlande du Nord dans le Royaume-Uni"),
],
"cu_famine.html": [
 ("Robert Peel", "Premier ministre conservateur de 1841 à 1846"),
 ("Corn Laws", "lois qui taxaient les céréales importées et maintenaient le prix du pain élevé"),
 ("Tony Blair", "Premier ministre travailliste de 1997 à 2007"),
],
"cu_troubles.html": [
 ("Martin Luther King", "pasteur noir américain, leader du mouvement pour les droits civiques"),
 ("l'UVF ou l'UDA", "groupes armés protestants loyalistes"),
 ("À Derry", "deuxième ville d'Irlande du Nord, appelée Londonderry par les unionistes"),
 ("David Cameron", "Premier ministre britannique de 2010 à 2016"),
 ("Margaret Thatcher", "Première ministre conservatrice de 1979 à 1990"),
 ("Sinn Féin", "parti politique républicain, proche de l'IRA"),
 ("Belfast", "capitale de l'Irlande du Nord"),
],
"cu_vie_uk.html": [
 ("comme Eton", "pensionnat de garçons près de Windsor, qui a formé de nombreux Premiers ministres"),
 ("Ceylan", "l'actuel Sri Lanka"),
],
"cu_londres.html": [
 ("Guillaume le Conquérant", "duc de Normandie devenu roi d'Angleterre après la bataille de Hastings en 1066"),
 ("Harry Beck", "dessinateur industriel employé par le métro"),
],
"cu_ecosse_galles.html": [
 ("Braveheart", "film de Mel Gibson sorti en 1995"),
 ("Bannockburn", "bataille où les Écossais battent l'armée anglaise"),
 ("Jacques VI", "fils de la reine d'Écosse Marie Stuart"),
 ("Édouard Ier", "roi d'Angleterre de 1272 à 1307"),
],
"cu_revolution_industrielle.html": [
 ("enclosures", "clôture des champs communs au profit des grands propriétaires"),
 ("James Watt", "ingénieur écossais"),
 ("George Stephenson", "ingénieur anglais, pionnier du chemin de fer"),
 ("Karl Marx et Friedrich Engels", "penseurs allemands, auteurs du Manifeste du Parti communiste en 1848"),
 ("Charles Dickens", "le plus célèbre romancier anglais du 19e siècle"),
],
"cu_suffragettes.html": [
 ("Daily Mail", "journal populaire britannique"),
 ("Nancy Astor", "élue conservatrice, d'origine américaine"),
],
"cu_blitz.html": [
 ("Winston Churchill", "homme politique conservateur, Premier ministre de 1940 à 1945 puis de 1951 à 1955"),
 ("Dunkirk", "Dunkerque, port du nord de la France"),
 ("la Luftwaffe", "l'armée de l'air allemande"),
 ("Le roi George VI", "roi de 1936 à 1952, père d'Elizabeth II"),
],
"cu_thatcher.html": [
 ("Ronald Reagan", "président républicain des États-Unis de 1981 à 1989"),
 ("comme à Orgreave", "cokerie près de Sheffield, où des milliers de policiers et de grévistes s'affrontent"),
 ("attentat de l'IRA", "groupe armé républicain irlandais"),
],
"cu_multiculturel.html": [
 ("Enoch Powell", "député conservateur"),
 ("Zadie Smith et Salman Rushdie", "romanciers britanniques de renommée mondiale"),
],
"cu_paques_1916.html": [
 ("membres de l'IRB", "Irish Republican Brotherhood, société secrète républicaine"),
 ("Constance Markievicz", "aristocrate devenue révolutionnaire, première femme élue au Parlement britannique en 1918"),
 ("Roger Casement", "diplomate irlandais arrêté alors qu'il tentait d'obtenir des armes de l'Allemagne"),
 ("W. B. Yeats", "grand poète irlandais, prix Nobel de littérature 1923"),
 ("Black and Tans", "forces auxiliaires britanniques, surnommées ainsi à cause de leurs uniformes dépareillés"),
 ("Éamon de Valera", "chef républicain, futur chef du gouvernement puis président de l'Irlande"),
],
"cu_irlande_auj.html": [
 ("James Joyce", "auteur du roman Ulysses"),
 ("gérés par la GAA", "Gaelic Athletic Association, fédération des sports gaéliques"),
],
"cu_institutions_us.html": [
 ("George Washington", "chef de l'armée pendant la guerre d'indépendance, puis premier président"),
 ("James Madison", "principal rédacteur de la Constitution, futur 4e président"),
 ("Benjamin Franklin", "savant, inventeur du paratonnerre et diplomate"),
 ("Montesquieu", "philosophe français du 18e siècle, théoricien de la séparation des pouvoirs"),
],
"cu_manifest_destiny.html": [
 ("Thomas Jefferson", "3e président des États-Unis de 1801 à 1809, principal auteur de la Déclaration d'indépendance"),
 ("à Napoléon", "alors à la tête de la France"),
 ("Lewis and Clark", "deux officiers de l'armée, Meriwether Lewis et William Clark"),
 ("bataille de l'Alamo", "fort où les défenseurs texans furent tués par l'armée mexicaine"),
 ("l'armée de Custer", "officier de cavalerie américain, tué lors de cette bataille"),
 ("Andrew Jackson", "7e président des États-Unis, de 1829 à 1837"),
],
"cu_red_scare.html": [
 ("Emma Goldman", "militante anarchiste d'origine russe"),
 ("Le président Truman", "président démocrate de 1945 à 1953"),
 ("Charlie Chaplin", "acteur et réalisateur, créateur du personnage de Charlot"),
 ("Arthur Miller", "grand dramaturge américain"),
],
"cu_watergate.html": [
 ("Richard Nixon", "président républicain élu en 1968"),
 ("du FBI", "la police fédérale américaine"),
 ("à la CIA", "le service de renseignement extérieur"),
 ("Gerald Ford", "le vice-président de Nixon"),
],
"cu_televangelisme.html": [
 ("Aimee Semple McPherson", "prédicatrice pentecôtiste vedette des années 1920"),
 ("Ronald Reagan", "acteur devenu président républicain de 1981 à 1989"),
],
"cu_pilgrims.html": [
 ("guerre de Sept Ans", "conflit mondial où la Grande-Bretagne prend le Canada à la France"),
 ("Thomas Jefferson", "futur 3e président des États-Unis"),
 ("La Fayette", "jeune noble français venu combattre aux côtés des Américains"),
 ("à Yorktown", "ville de Virginie où l'armée britannique capitule"),
],
"cu_esclavage.html": [
 ("Nat Turner", "esclave et prédicateur de Virginie"),
 ("Harriet Beecher Stowe", "romancière abolitionniste"),
 ("à Gettysburg", "bataille décisive en Pennsylvanie, gagnée par le Nord"),
 ("Ku Klux Klan", "organisation raciste et violente créée après la guerre"),
],
"cu_droits_civiques.html": [
 ("par Gandhi", "leader non violent de l'indépendance de l'Inde"),
 ("Black Panthers", "organisation révolutionnaire noire créée en 1966"),
],
"cu_ellis_island.html": [
 ("Bartholdi", "sculpteur français"),
 ("Gustave Eiffel", "ingénieur, constructeur de la tour Eiffel"),
 ("Emma Lazarus", "poétesse new-yorkaise"),
 ("pogroms", "violences meurtrières contre les Juifs"),
],
"cu_1929_new_deal.html": [
 ("Al Capone", "célèbre gangster de Chicago"),
 ("Herbert Hoover", "président républicain de 1929 à 1933"),
 ("John Steinbeck", "romancier américain, prix Nobel de littérature 1962"),
],
"cu_vietnam.html": [
 ("Lyndon Johnson", "président démocrate de 1963 à 1969"),
 ("le Viêt-cong", "guérilla communiste du Sud-Vietnam"),
 ("Muhammad Ali", "champion du monde de boxe"),
 ("Martin Luther King", "leader du mouvement pour les droits civiques"),
 ("Jimi Hendrix, Janis Joplin ou Joan Baez", "stars du rock et de la folk"),
 ("Nixon", "président républicain de 1969 à 1974"),
 ("Stonewall", "bar gay de New York où les clients se révoltent contre une descente de police"),
],
"cu_11_septembre.html": [
 ("Pearl Harbor", "base navale américaine d'Hawaï attaquée par le Japon"),
 ("talibans", "mouvement islamiste au pouvoir en Afghanistan"),
 ("Saddam Hussein", "dictateur au pouvoir en Irak depuis 1979"),
 ("Guantánamo", "base militaire américaine située à Cuba"),
],
"cu_conquete_spatiale.html": [
 ("Wernher von Braun", "ingénieur allemand qui avait conçu les missiles V2 pour les nazis"),
 ("Laïka", "premier être vivant envoyé en orbite"),
 ("SpaceX", "entreprise spatiale fondée par Elon Musk"),
],
"cu_elections_us.html": [
 ("Al Gore", "vice-président démocrate"),
],
"cu_amerindiens.html": [
 ("la loi Dawes", "loi fédérale de 1887"),
 ("le président Biden", "président démocrate de 2021 à 2025"),
 ("Columbus Day", "jour férié en l'honneur de Christophe Colomb"),
],
"cu_australie.html": [
 ("James Cook", "navigateur et explorateur britannique"),
 ("arrêt **Mabo**", "du nom d'Eddie Mabo, habitant du détroit de Torres qui a porté l'affaire en justice"),
 ("Kevin Rudd", "Premier ministre travailliste"),
],
"cu_afrique_sud.html": [
 ("guerre des Boers", "guerre entre les Britanniques et les républiques boers"),
 ("procès de Rivonia", "procès des dirigeants de l'ANC"),
 ("F. W. de Klerk", "dernier président blanc de l'apartheid"),
 ("Desmond Tutu", "archevêque anglican, prix Nobel de la paix 1984"),
 ("Springboks", "l'équipe nationale de rugby, symbole des Blancs sous l'apartheid"),
],
"cu_inde.html": [
 ("Empire moghol", "empire musulman qui domina l'Inde du 16e au 18e siècle"),
 ("Muhammad Ali Jinnah", "fondateur du Pakistan"),
 ("Le Cachemire", "région du nord revendiquée par l'Inde et le Pakistan"),
],
"cu_canada.html": [
 ("Jacques Cartier", "explorateur français originaire de Saint-Malo"),
 ("Samuel de Champlain", "explorateur français"),
 ("plaines d'Abraham", "bataille décisive devant la ville de Québec"),
],
"cu_nouvelle_zelande.html": [
 ("Abel Tasman", "navigateur néerlandais"),
 ("James Cook", "navigateur et explorateur britannique"),
],
"cu_jamaique.html": [
 ("Samuel Sharpe", "esclave et prédicateur baptiste"),
 ("Haïlé Sélassié", "dernier empereur d'Éthiopie, de 1930 à 1974"),
 ("Shelly-Ann Fraser-Pryce", "sprinteuse, plusieurs fois championne olympique"),
],
"cu_musique.html": [
 ("Robert Johnson ou Muddy Waters", "grands guitaristes et chanteurs de blues"),
 ("Louis Armstrong", "trompettiste et chanteur"),
 ("**Harlem**", "quartier noir de New York"),
 ("Duke Ellington, Billie Holiday, puis Miles Davis ou John Coltrane", "grands musiciens et chanteuse de jazz"),
 ("Chuck Berry, Little Richard", "pionniers noirs du rock"),
 ("Ed Sullivan Show", "émission de variétés très populaire"),
 ("**Bob Dylan**", "chanteur folk, prix Nobel de littérature 2016"),
 ("Aretha Franklin", "chanteuse surnommée la reine de la soul"),
],
"cu_shakespeare.html": [
 ("Jacques Ier", "roi d'Écosse devenu roi d'Angleterre en 1603"),
 ("puritains", "protestants très stricts"),
 ("Ben Jonson", "dramaturge, ami et rival de Shakespeare"),
],
"cu_grandes_figures.html": [
 ("Gordon Brown", "Premier ministre travailliste de 2007 à 2010"),
 ("NAACP", "grande association de défense des droits des Noirs"),
 ("talibans", "mouvement islamiste armé"),
],
"cu_medias.html": [
 ("Rupert Murdoch", "magnat australo-américain des médias"),
 ("**Leveson**", "du nom du juge qui l'a dirigée"),
],
"cu_guerre_secession.html": [
 ("**Robert E. Lee**", "général de la Confédération, le plus célèbre du Sud"),
 ("John Ericsson", "ingénieur d'origine suédoise"),
 ("Winfield Scott", "commandant en chef de l'armée de l'Union au début de la guerre"),
 ("**Ulysses S. Grant**", "général de l'Union, futur président de 1869 à 1877"),
 ("**William T. Sherman**", "général de l'Union"),
],
"cu_amerindiens_societe.html": [
 ("Reservation Dogs", "série télévisée diffusée de 2021 à 2023"),
],
"cu_alaska.html": [
 ("guerre de Crimée", "guerre de 1853-1856 perdue par la Russie contre le Royaume-Uni, la France et l'Empire ottoman"),
 ("Jack London", "écrivain américain, aventurier"),
 ("Aléoutiennes", "chaîne d'îles volcaniques au sud-ouest de l'Alaska"),
],
"cu_lgbt.html": [
 ("Marsha P. Johnson", "militante trans afro-américaine"),
 ("ACT UP", "association de lutte contre le sida fondée à New York en 1987"),
],
}
