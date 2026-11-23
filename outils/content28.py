import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
exec(open(_EA_OUT+"/cuhelp.py", encoding="utf-8").read())

# ═════════ ROARING TWENTIES ═════════
F = "cu_roaring_twenties.html"
DZ(F, """
## L'Amérique après la guerre
Sortis vainqueurs et enrichis de la Première Guerre mondiale, les États-Unis deviennent la première puissance économique du monde. Les années 1920 sont une décennie de prospérité, de modernité et de fête : on les appelle les **Roaring Twenties**, les « années rugissantes » (en France, les années folles).

## La société de consommation
L'industrie produit en masse grâce à la **assembly line** (chaîne de montage) qu'**Henry Ford** a introduite en 1913 : la **Ford Model T** devient abordable, et à la fin de la décennie il y a une voiture pour cinq Américains. Les foyers s'équipent d'électricité, de radios, de réfrigérateurs, d'aspirateurs. La publicité se développe, et on achète à crédit (**on credit**, **installment plan**). Le cinéma triomphe à Hollywood ; en 1927, *The Jazz Singer* est le premier grand film parlant.

## L'âge du jazz
L'écrivain **F. Scott Fitzgerald** baptise l'époque le **Jazz Age**. Le jazz, né à La Nouvelle-Orléans, gagne Chicago et New York. À **Harlem**, quartier noir de New York, c'est la **Harlem Renaissance** : écrivains comme **Langston Hughes**, musiciens comme **Duke Ellington** ou Louis Armstrong font éclater la créativité afro-américaine. Paradoxe : au célèbre **Cotton Club**, les musiciens étaient noirs, mais le public était réservé aux Blancs. On danse le **Charleston**. Le roman *The Great Gatsby* (1925) de Fitzgerald décrit les fêtes extravagantes des riches… et le vide qui se cache derrière.

## Les « flappers »
Les femmes obtiennent le droit de vote en 1920 avec le **19th Amendment**. Les **flappers**, jeunes femmes émancipées, coupent leurs cheveux courts (au carré), portent des robes au genou, se maquillent, fument, dansent et conduisent : elles choquent les générations précédentes et symbolisent une nouvelle liberté.

## L'envers du décor
Tout le monde ne profite pas de la prospérité : les agriculteurs s'appauvrissent, les inégalités se creusent. La décennie est aussi marquée par la **Prohibition**, qui fait la fortune des gangsters, par le retour du **Ku Klux Klan** (plusieurs millions de membres au milieu des années 1920), par la peur des étrangers et des révolutionnaires (la « Red Scare », l'exécution de Sacco et Vanzetti) et par les lois de quotas de 1924 qui limitent l'immigration.

## La fin de la fête
Beaucoup d'Américains spéculent en Bourse avec de l'argent emprunté, persuadés que les cours monteront toujours. En octobre 1929, le krach de **Wall Street** met brutalement fin aux années rugissantes : c'est le début de la **Great Depression** (voir la page *The Great Depression & the New Deal*).
""", """
a car = une voiture
jazz = le jazz
a party = une fête
a dress = une robe
the radio = la radio
money = l'argent
credit = le crédit
a crash = un krach
""", [
 ("Pourquoi les États-Unis deviennent-ils si riches dans les années 1920 ?", ["Ils sortent vainqueurs et enrichis de la Première Guerre mondiale", "Ils ont découvert de l'or", "Ils ont gagné la guerre de Sécession"], ""),
 ("Qu'a permis la chaîne de montage d'Henry Ford ?", ["De produire des voitures en masse et moins chères", "De fabriquer des avions", "De construire des maisons"], ""),
 ("Qu'est-ce que la Harlem Renaissance ?", ["Une explosion de créativité afro-américaine à New York", "Un mouvement religieux", "Une loi"], ""),
 ("Qui sont les flappers ?", ["De jeunes femmes émancipées qui choquent par leur liberté", "Des gangsters", "Des oiseaux"], ""),
 ("Quel est l'envers du décor des années 1920 ?", ["Inégalités, Prohibition, retour du Ku Klux Klan, peur des étrangers", "Une guerre mondiale", "Une famine"], ""),
 ("Qu'est-ce qui met fin aux années rugissantes ?", ["Le krach de Wall Street en 1929", "La Seconde Guerre mondiale", "L'élection de Lincoln"], ""),
], [("**Henry Ford**", "industriel américain, fondateur de la Ford Motor Company"), ("**F. Scott Fitzgerald**", "romancier américain"), ("**Langston Hughes**", "poète afro-américain"), ("**Duke Ellington**", "pianiste et chef d'orchestre de jazz")])
D = "rt"
culture(F, "Culture : The Roaring Twenties", 'The Roaring <span>Twenties</span>',
  "Culture · jazz, voitures, flappers et prospérité, jusqu'au krach", ("#fde68a", "#a16207"),
  reperes("Les années 1920 sont une décennie de prospérité, de modernité et de fête aux États-Unis, jusqu'au krach de 1929.",
    [("1913", "chaîne de montage d'Henry Ford"), ("1920", "19e amendement : droit de vote des femmes ; début de la Prohibition"), ("1925", "The Great Gatsby de F. Scott Fitzgerald"),
     ("1927", "The Jazz Singer, premier grand film parlant"), ("octobre 1929", "krach de Wall Street : début de la Grande Dépression")],
    "prosperity, a car, jazz, a flapper, credit, consumer society, a speakeasy, a crash"),
  {D: doc("The Jazz Age", [
    "After the First World War, the United States became the richest country in the world. The 1920s were a time of prosperity and fun: people call them the \"Roaring Twenties\".",
    "Many families bought cars, radios and fridges, often on credit. Henry Ford produced cars on an assembly line, so the Model T became cheap. Hollywood films became very popular.",
    "It was the Jazz Age. Jazz music spread from New Orleans to Chicago and New York. In Harlem, a Black neighbourhood of New York, writers and musicians created the Harlem Renaissance.",
    "Women got the right to vote in 1920. Young women called \"flappers\" cut their hair short, wore short dresses, danced the Charleston and enjoyed their freedom.",
    "But not everybody was rich, and many people bought shares with borrowed money. In October 1929, the stock market crashed, and the Roaring Twenties ended suddenly."])},
  [TF(D, "After the First World War, the USA became very rich.", True, "« the richest country in the world »."),
   TF(D, "Families never bought things on credit.", False, "« often on credit »."),
   TF(D, "Henry Ford made cars cheaper.", True, "« the Model T became cheap »."),
   TF(D, "Jazz was born in Chicago.", False, "Il vient de La Nouvelle-Orléans."),
   TF(D, "Women got the right to vote in 1920.", True, "« in 1920 »."),
   TF(D, "The Roaring Twenties ended with the crash of 1929.", True, "« In October 1929 »." )],
  [Q(D, "Why are they called the \"Roaring Twenties\"?", ["It was a time of prosperity and fun.", "There were many lions.", "There was a war."]),
   Q(D, "What was the Harlem Renaissance?", ["A cultural movement of Black writers and musicians.", "A new car.", "A political party."]),
   Q(D, "Who were the flappers?", ["Young women who enjoyed their freedom.", "Jazz musicians.", "Car workers."]),
   Q(D, "Why did the stock market crash hurt so many people?", ["Many had bought shares with borrowed money.", "It was too cold.", "Cars were too expensive."])],
  [DT(D, "Qui a écrit The Great Gatsby ?", ["F. Scott Fitzgerald", "Ernest Hemingway", "John Steinbeck", "Mark Twain"]),
   DT(D, "Quelle danse est à la mode ?", ["Le Charleston", "Le rock'n'roll", "La valse", "Le disco"]),
   DT(D, "Quel est le premier grand film parlant ?", ["The Jazz Singer", "King Kong", "Gone with the Wind", "Metropolis"]),
   DT(D, "Quel amendement donne le vote aux femmes ?", ["Le 19e", "Le 13e", "Le 2e", "Le 1er"])],
  [W(D, "Trouve le mot qui veut dire « prospérité ».", "prosperity"), W(D, "Trouve l'expression qui veut dire « chaîne de montage ».", ["assembly line", "an assembly line"]),
   W(D, "Trouve le mot qui veut dire « emprunté ».", "borrowed"), W(D, "Trouve le mot qui veut dire « actions » (en Bourse).", "shares")])

# ═════════ PROHIBITION ═════════
F = "cu_prohibition.html"
DZ(F, """
## Interdire l'alcool
Au 19e siècle, de nombreux Américains, souvent protestants et ruraux, voient dans l'alcool la cause de la violence domestique, de la pauvreté et de la délinquance. Des mouvements de **temperance**, comme la Women's Christian Temperance Union ou l'Anti-Saloon League, militent pour l'interdire. La Première Guerre mondiale renforce leur cause : beaucoup de brasseurs sont d'origine allemande, et il faut économiser les céréales. En 1919, le **18th Amendment** est adopté : à partir du **17 janvier 1920**, la fabrication, la vente et le transport de boissons alcoolisées sont interdits dans tout le pays. C'est la **Prohibition**.

## Une loi massivement contournée
Les Américains continuent de boire. Des bars clandestins, les **speakeasies** (on y parle bas pour ne pas se faire repérer), se multiplient : on y entre avec un mot de passe. Des **bootleggers** importent illégalement de l'alcool du Canada ou des Caraïbes ; d'autres fabriquent un alcool artisanal parfois dangereux, le **moonshine**, distillé la nuit à la lumière de la lune. Les médecins prescrivent du whisky « médical », les églises utilisent du vin de messe… Des chauffeurs de bootleggers, qui modifiaient leurs voitures pour échapper à la police, sont à l'origine des courses automobiles NASCAR.

## L'âge d'or des gangsters
La Prohibition fait la fortune du crime organisé. À Chicago, **Al Capone** contrôle un empire de speakeasies, de brasseries clandestines, de jeux et de prostitution ; il corrompt la police et les juges. Les gangs rivaux s'affrontent à la mitraillette (la « Tommy gun »). Le 14 février 1929, lors du **St Valentine's Day Massacre**, sept membres d'un gang rival sont abattus dans un garage. L'agent fédéral **Eliot Ness** et son équipe d'incorruptibles, **The Untouchables**, traquent Capone, qui est finalement condamné en 1931… pour fraude fiscale.

## La fin de la Prohibition
La Prohibition est un échec : la consommation d'alcool ne disparaît pas, la criminalité explose, et l'État perd d'énormes revenus fiscaux. Avec la Grande Dépression, l'argument économique devient décisif : rouvrir les brasseries créerait des emplois et des taxes. Le président Franklin Roosevelt soutient l'abrogation, et le **21st Amendment** met fin à la Prohibition le **5 décembre 1933**. C'est le seul amendement de l'histoire américaine à en annuler un autre. Certains États et comtés sont toutefois restés « secs » (**dry counties**) bien plus longtemps.

## Une époque mythique
La Prohibition a nourri l'imaginaire : films de gangsters (*Scarface*, *The Untouchables*), séries (*Boardwalk Empire*), et l'image des années folles avec leurs bars secrets. Elle reste un exemple souvent cité dans les débats sur l'interdiction des drogues.
""", """
alcohol = l'alcool
a bar = un bar
a gangster = un gangster
the police = la police
a law = une loi
a secret = un secret
a password = un mot de passe
crime = le crime
""", [
 ("Pourquoi des Américains voulaient-ils interdire l'alcool ?", ["Ils y voyaient la cause de la violence, de la pauvreté et de la délinquance", "Il coûtait trop cher", "Le roi l'avait demandé"], ""),
 ("Qu'est-ce qu'un speakeasy ?", ["Un bar clandestin où l'on entre avec un mot de passe", "Un cours d'anglais", "Une église"], ""),
 ("Qu'est-ce que le moonshine ?", ["Un alcool artisanal fabriqué illégalement", "Une lampe", "Un film"], ""),
 ("Qui est Al Capone ?", ["Le gangster le plus célèbre de Chicago", "Un policier", "Un président"], ""),
 ("Pour quel motif Al Capone est-il finalement condamné ?", ["Fraude fiscale", "Meurtre", "Vol de voiture"], ""),
 ("Pourquoi la Prohibition est-elle abolie en 1933 ?", ["C'est un échec, et rouvrir les brasseries créerait emplois et taxes", "Tout le monde a arrêté de boire", "Les gangsters l'ont demandé"], ""),
], [("Anti-Saloon League", "puissante association anti-alcool"), ("**Al Capone**", "gangster de Chicago, 1899-1947"), ("**Eliot Ness**", "agent fédéral du Trésor")])
D = "pr"
culture(F, "Culture : Prohibition and the gangsters", 'Prohibition <span>&amp; the gangsters</span>',
  "Culture · bars clandestins, Al Capone et Untouchables", ("#d6d3d1", "#292524"),
  reperes("De 1920 à 1933, l'alcool est interdit aux États-Unis. La loi est massivement contournée et fait la fortune des gangsters.",
    [("1919", "18e amendement"), ("17 janv. 1920", "entrée en vigueur de la Prohibition"), ("14 févr. 1929", "massacre de la Saint-Valentin à Chicago"),
     ("1931", "Al Capone condamné pour fraude fiscale"), ("5 déc. 1933", "21e amendement : fin de la Prohibition")],
    "alcohol, a ban, a speakeasy, a bootlegger, a gangster, organised crime, a password, a raid"),
  {D: doc("A dry country?", [
    "In 1920, a new law banned the production and sale of alcohol in the whole United States. This period, called Prohibition, lasted until 1933.",
    "Many people thought alcohol caused violence and poverty. But Americans did not stop drinking. They went to secret bars called speakeasies, where you needed a password to enter.",
    "Criminals called bootleggers sold illegal alcohol. Gangsters became rich and powerful. The most famous was Al Capone, in Chicago. He controlled many speakeasies and paid the police.",
    "In 1929, during the St Valentine's Day Massacre, seven members of a rival gang were killed in Chicago. Federal agent Eliot Ness and his team, the Untouchables, fought against Capone. In 1931, Capone went to prison… for not paying his taxes!",
    "Prohibition was a failure: crime increased and the government lost a lot of money. It ended in 1933."])},
  [TF(D, "Prohibition lasted from 1920 to 1933.", True, "« lasted until 1933 »."),
   TF(D, "Americans completely stopped drinking.", False, "« Americans did not stop drinking »."),
   TF(D, "You needed a password to enter a speakeasy.", True, "« you needed a password »."),
   TF(D, "Al Capone was a police officer.", False, "C'était un gangster."),
   TF(D, "Capone went to prison for murder.", False, "« for not paying his taxes »."),
   TF(D, "Prohibition was a success.", False, "« Prohibition was a failure »." )],
  [Q(D, "Why did some people want to ban alcohol?", ["They thought it caused violence and poverty.", "It was too expensive.", "It was bad for cars."]),
   Q(D, "What were bootleggers?", ["Criminals who sold illegal alcohol.", "Police officers.", "Shoe makers."]),
   Q(D, "Who were the Untouchables?", ["Eliot Ness's team of federal agents.", "Capone's gang.", "A jazz band."]),
   Q(D, "Why was Prohibition a failure?", ["Crime increased and the government lost money.", "Everybody became healthy.", "It lasted too long."])],
  [DT(D, "Quel amendement met fin à la Prohibition ?", ["Le 21e", "Le 18e", "Le 19e", "Le 13e"]),
   DT(D, "Dans quelle ville règne Al Capone ?", ["Chicago", "New York", "Las Vegas", "Boston"]),
   DT(D, "Qui traque Capone ?", ["Eliot Ness", "J. Edgar Hoover", "Wyatt Earp", "Sherlock Holmes"]),
   DT(D, "Quand a lieu le massacre de la Saint-Valentin ?", ["14 février 1929", "4 juillet 1920", "5 décembre 1933", "1er janvier 1925"])],
  [W(D, "Trouve le mot qui veut dire « a interdit ».", "banned"), W(D, "Trouve le mot qui veut dire « mot de passe ».", ["password", "a password"]),
   W(D, "Trouve le mot qui veut dire « rival ».", "rival"), W(D, "Trouve le mot qui veut dire « un échec ».", ["failure", "a failure"])])

# ═════════ FAR WEST ═════════
F = "cu_far_west.html"
DZ(F, """
## Le temps des cow-boys
Après la guerre de Sécession, les grandes plaines du Texas comptent des millions de bovins sauvages, les **longhorns**. Dans les villes de l'Est, la viande se vend cher. Des **cowboys** conduisent alors d'immenses troupeaux sur des centaines de kilomètres, pendant des semaines, jusqu'aux gares du Kansas, comme Abilene ou Dodge City, d'où le bétail part en train : ce sont les **cattle drives**, par exemple sur la **Chisholm Trail**. Le métier est dur, mal payé, dangereux (orages, rivières, vols). Les historiens estiment qu'environ un cow-boy sur quatre était noir, et beaucoup étaient mexicains : les **vaqueros** ont d'ailleurs inventé une grande partie des techniques et du vocabulaire (*lasso*, *rodeo*, *ranch*).

## Villes-champignons et hors-la-loi
Les ruées vers l'or et l'argent font naître des **boomtowns**, villes construites en quelques mois avec leur saloon, leur banque et leur prison. La justice y est souvent expéditive. Des hors-la-loi deviennent célèbres : **Billy the Kid**, **Jesse James**, qui attaquait les banques et les trains, ou Butch Cassidy. En face, des shérifs et marshals comme **Wyatt Earp** : en 1881, il participe à la fusillade d'**O.K. Corral**, à Tombstone (Arizona), qui dure une trentaine de secondes mais devient légendaire.

## Communiquer et se déplacer
Le **Pony Express** (1860-1861) transporte le courrier à cheval entre le Missouri et la Californie en une dizaine de jours, en se relayant ; il disparaît dès l'arrivée du télégraphe transcontinental. Les diligences (**stagecoaches**) et surtout le chemin de fer transcontinental (1869) transforment l'Ouest.

## La naissance du mythe
Dès 1883, **Buffalo Bill** (William Cody), ancien éclaireur, crée le **Wild West Show**, un spectacle qui tourne aux États-Unis et en Europe, avec des cow-boys, des tireurs d'élite comme **Annie Oakley**, et même le chef lakota **Sitting Bull**. Le mythe du Far West est né avant même la fin de la « Frontière ». Au 20e siècle, Hollywood en fait un genre majeur : le **western**, avec John Wayne et les films de John Ford, puis les westerns spaghetti italiens de Sergio Leone. En France, la bande dessinée *Lucky Luke* le parodie.

## Mythe et réalité
Le western a longtemps présenté un monde simple : de courageux pionniers blancs face à des « Indiens » sauvages. La réalité est plus complexe : le Far West était multiculturel (Noirs, Mexicains, Chinois, Amérindiens, immigrés européens) et sa conquête s'est faite au prix de la dépossession des peuples autochtones. Depuis les années 1970, beaucoup de films et de livres offrent une vision plus nuancée, comme *Little Big Man* ou *Dances with Wolves*.
""", """
a cowboy = un cow-boy
a horse = un cheval
a cow = une vache
a ranch = un ranch
a saloon = un saloon
a sheriff = un shérif
a train = un train
a gun = une arme à feu
""", [
 ("Qu'est-ce qu'un « cattle drive » ?", ["Le convoi d'un immense troupeau jusqu'aux gares", "Une course de voitures", "Un spectacle"], ""),
 ("Qui étaient en partie les cow-boys ?", ["Environ un sur quatre était noir, beaucoup étaient mexicains", "Uniquement des Anglais", "Uniquement des soldats"], ""),
 ("Qu'est-ce qu'une boomtown ?", ["Une ville construite très vite pendant une ruée vers l'or", "Une ville bombardée", "Une capitale"], ""),
 ("Que transportait le Pony Express ?", ["Le courrier, à cheval", "Du bétail", "De l'or"], ""),
 ("Qu'est-ce que le Wild West Show de Buffalo Bill ?", ["Un spectacle sur le Far West qui tournait aux États-Unis et en Europe", "Un film", "Une guerre"], ""),
 ("Que cachait souvent le mythe du western ?", ["Un Far West multiculturel et la dépossession des Amérindiens", "Rien du tout", "La vie en Europe"], ""),
], [("**Billy the Kid**", "jeune hors-la-loi tué en 1881"), ("**Wyatt Earp**", "homme de loi de l'Ouest"), ("**Sitting Bull**", "chef lakota, vainqueur à Little Bighorn"), ("Sergio Leone", "réalisateur italien")])
D = "fw"
culture(F, "Culture : The Wild West", 'The Wild <span>West</span>',
  "Culture · cow-boys, hors-la-loi et naissance d'un mythe", ("#fdba74", "#9a3412"),
  reperes("Le Far West (the Wild West) désigne l'Ouest américain de la seconde moitié du 19e siècle. Sa réalité est plus dure et plus diverse que le mythe des westerns.",
    [("1860 – 1861", "Pony Express"), ("1866 – 1885", "grands convois de bétail du Texas au Kansas"), ("1869", "premier chemin de fer transcontinental"),
     ("1881", "fusillade d'O.K. Corral ; mort de Billy the Kid"), ("1883", "Wild West Show de Buffalo Bill"), ("20e siècle", "âge d'or du western à Hollywood")],
    "a cowboy, a herd, cattle, a ranch, a saloon, an outlaw, a sheriff, a western"),
  {D: doc("Cowboys and outlaws", [
    "After the Civil War, there were millions of cows in Texas. Cowboys drove huge herds for weeks to the railway stations of Kansas. It was a hard and dangerous job.",
    "Not all cowboys were white: about one in four was Black, and many were Mexican. Mexican cowboys, the vaqueros, gave us words like \"ranch\" and \"rodeo\".",
    "In the new towns of the West, there were saloons, banks and outlaws. Famous outlaws like Billy the Kid and Jesse James robbed banks and trains. Sheriffs like Wyatt Earp tried to keep order.",
    "In 1883, Buffalo Bill created the Wild West Show, a spectacle with cowboys and Native Americans that travelled in America and Europe. The myth of the Wild West was born.",
    "Later, Hollywood made hundreds of westerns. But the real West was more diverse and more violent, especially for Native Americans, who lost their lands."])},
  [TF(D, "Cowboys drove herds of cows to Kansas.", True, "« to the railway stations of Kansas »."),
   TF(D, "All cowboys were white.", False, "« about one in four was Black, and many were Mexican »."),
   TF(D, "The word \"rodeo\" comes from Mexican cowboys.", True, "« the vaqueros, gave us words like \"ranch\" and \"rodeo\" »."),
   TF(D, "Billy the Kid was a sheriff.", False, "C'était un hors-la-loi."),
   TF(D, "Buffalo Bill's show travelled in Europe.", True, "« travelled in America and Europe »."),
   TF(D, "The real West was exactly like in westerns.", False, "« more diverse and more violent »." )],
  [Q(D, "Why did cowboys drive cows to Kansas?", ["To put them on trains to the East.", "To sell them to Mexico.", "For a rodeo."]),
   Q(D, "What did outlaws rob?", ["Banks and trains.", "Ranches only.", "Churches."]),
   Q(D, "What did Buffalo Bill create?", ["The Wild West Show.", "A railway.", "A bank."]),
   Q(D, "Who suffered most from the conquest of the West?", ["Native Americans.", "Cowboys.", "Sheriffs."])],
  [DT(D, "Où a lieu la fusillade d'O.K. Corral ?", ["À Tombstone", "À Dodge City", "À Abilene", "À San Francisco"]),
   DT(D, "Comment s'appellent les cow-boys mexicains ?", ["Les vaqueros", "Les gauchos", "Les bootleggers", "Les pionniers"]),
   DT(D, "Quel acteur est le symbole du western ?", ["John Wayne", "Charlie Chaplin", "Elvis Presley", "Marlon Brando"]),
   DT(D, "Quelle tireuse d'élite participe au Wild West Show ?", ["Annie Oakley", "Calamity Jane", "Rosa Parks", "Sacagawea"])],
  [W(D, "Trouve le mot qui veut dire « troupeaux ».", "herds"), W(D, "Trouve le mot qui veut dire « hors-la-loi » (pluriel).", "outlaws"),
   W(D, "Trouve le mot qui veut dire « ont volé, ont attaqué » (au prétérit).", "robbed"), W(D, "Trouve le mot qui veut dire « varié, divers ».", "diverse")])

# ═════════ WW2 USA ═════════
F = "cu_ww2_usa.html"
DZ(F, """
## De la neutralité à la guerre
Quand la guerre éclate en Europe en 1939, la plupart des Américains veulent rester à l'écart : c'est l'**isolationism**. Le président **Franklin D. Roosevelt** aide pourtant le Royaume-Uni en lui fournissant armes et matériel (le **Lend-Lease**, 1941) : l'Amérique devient « l'arsenal de la démocratie ».

## Pearl Harbor
Le **7 décembre 1941**, l'aviation japonaise attaque par surprise la base navale de **Pearl Harbor**, à Hawaï. Plus de 2 400 Américains sont tués, de nombreux navires coulés. Roosevelt parle d'une date qui restera marquée par l'infamie (« *a date which will live in infamy* »). Les États-Unis entrent en guerre contre le Japon, puis l'Allemagne leur déclare la guerre.

## Le front intérieur
Toute l'économie se met au service de la guerre : les usines automobiles fabriquent des chars et des avions. Des millions de femmes remplacent les hommes partis au front ; l'affiche de **Rosie the Riveter**, ouvrière en bleu de travail qui montre son biceps, en devient le symbole (« *We Can Do It!* »). Le chômage de la Grande Dépression disparaît.
Mais la guerre révèle aussi des injustices : environ 120 000 personnes d'origine japonaise, en majorité citoyens américains, sont internées dans des camps (**internment camps**) en 1942. Les soldats noirs combattent dans une armée encore ségréguée, comme les célèbres pilotes de **Tuskegee**.

## Deux fronts
Dans le Pacifique, les Américains arrêtent l'avancée japonaise à la bataille navale de **Midway** (juin 1942), puis reprennent les îles une à une, au prix de combats très meurtriers (Iwo Jima, Okinawa). En Europe, ils débarquent en Afrique du Nord, en Italie, puis le **6 juin 1944** en Normandie : c'est le **D-Day**. Sur les plages d'**Omaha** et d'**Utah Beach**, les pertes sont lourdes, mais la libération de l'Europe de l'Ouest commence. L'Allemagne capitule le 8 mai 1945.

## La bombe atomique
Le **Manhattan Project**, programme scientifique secret, met au point la bombe atomique. Le **6 août 1945**, un bombardier américain largue une bombe sur **Hiroshima**, puis le 9 août sur **Nagasaki**. Plus de 100 000 personnes meurent sur le coup, et beaucoup d'autres des suites des radiations. Le Japon capitule. Le débat sur la nécessité de ces bombardements continue : pour certains, ils ont évité une invasion encore plus meurtrière ; pour d'autres, ils ont frappé des civils sans justification suffisante.

## Une superpuissance
Environ 400 000 soldats américains sont morts. Mais les États-Unis sortent de la guerre comme la première puissance économique et militaire du monde. Le **GI Bill** permet à des millions de vétérans d'étudier et d'acheter une maison ; le **Marshall Plan** (1948) aide l'Europe à se reconstruire. Face à l'URSS, une nouvelle confrontation commence : la guerre froide.
""", """
a war = une guerre
a soldier = un soldat
a bomb = une bombe
a factory = une usine
a woman = une femme
a beach = une plage
a ship = un navire
victory = la victoire
""", [
 ("Que voulait la majorité des Américains en 1939 ?", ["Rester à l'écart de la guerre", "Attaquer l'Allemagne immédiatement", "Aider le Japon"], "C'est l'isolationnisme."),
 ("Que se passe-t-il le 7 décembre 1941 ?", ["Le Japon attaque Pearl Harbor", "Le Débarquement", "La fin de la guerre"], ""),
 ("Que symbolise Rosie the Riveter ?", ["Les femmes qui travaillent dans les usines pendant la guerre", "Une infirmière", "Une star de cinéma"], ""),
 ("Quelle injustice touche les Américains d'origine japonaise ?", ["Ils sont internés dans des camps", "Ils doivent quitter le pays", "Ils ne peuvent plus voter"], ""),
 ("Que se passe-t-il le 6 juin 1944 ?", ["Le Débarquement en Normandie", "Pearl Harbor", "Hiroshima"], ""),
 ("Qu'est-ce que le plan Marshall ?", ["Une aide américaine pour reconstruire l'Europe", "Un plan de bataille", "Une bombe"], ""),
], [("Lend-Lease", "loi de prêt-bail"), ("**Rosie the Riveter**", "« Rosie la riveteuse »"), ("**Tuskegee**", "unité d'aviateurs afro-américains"), ("Iwo Jima, Okinawa", "îles japonaises")])
D = "w2"
culture(F, "Culture : America in World War II", 'America in <span>World War II</span>',
  "Culture · Pearl Harbor, le D-Day et la bombe atomique", ("#94a3b8", "#334155"),
  reperes("Attaqués à Pearl Harbor en 1941, les États-Unis entrent dans la Seconde Guerre mondiale et en sortent superpuissance.",
    [("7 déc. 1941", "attaque japonaise sur Pearl Harbor"), ("1942", "internement des Américains d'origine japonaise ; bataille de Midway"), ("6 juin 1944", "D-Day en Normandie"),
     ("8 mai 1945", "capitulation de l'Allemagne"), ("6 et 9 août 1945", "bombes atomiques sur Hiroshima et Nagasaki"), ("2 sept. 1945", "capitulation du Japon")],
    "an attack, a soldier, a landing, the home front, an atomic bomb, a superpower, a veteran"),
  {D: doc("The arsenal of democracy", [
    "When the war started in Europe in 1939, most Americans did not want to fight. But on 7 December 1941, Japanese planes attacked Pearl Harbor, an American naval base in Hawaii. More than 2,400 Americans died, and the USA entered the war.",
    "At home, factories produced planes, tanks and ships. Millions of women worked in factories. The poster of \"Rosie the Riveter\" became their symbol. But about 120,000 Japanese Americans were sent to camps.",
    "On 6 June 1944, D-Day, American, British and Canadian soldiers landed on the beaches of Normandy, in France. It was the beginning of the liberation of Western Europe.",
    "In August 1945, the USA dropped two atomic bombs on the Japanese cities of Hiroshima and Nagasaki. Japan surrendered. People still debate whether these bombings were necessary.",
    "After the war, the USA was the most powerful country in the world. It helped Europe to rebuild with the Marshall Plan."])},
  [TF(D, "Most Americans wanted to fight in 1939.", False, "« most Americans did not want to fight »."),
   TF(D, "Pearl Harbor is in Hawaii.", True, "« an American naval base in Hawaii »."),
   TF(D, "Women worked in factories during the war.", True, "« Millions of women worked in factories »."),
   TF(D, "D-Day took place in Italy.", False, "En Normandie."),
   TF(D, "The USA dropped atomic bombs on two Japanese cities.", True, "Hiroshima et Nagasaki."),
   TF(D, "Everybody agrees that the bombings were necessary.", False, "« People still debate »." )],
  [Q(D, "Why did the USA enter the war?", ["Japan attacked Pearl Harbor.", "Germany invaded Canada.", "Britain asked for money."]),
   Q(D, "What happened to Japanese Americans?", ["About 120,000 were sent to camps.", "They became soldiers in Japan.", "Nothing."]),
   Q(D, "What was D-Day?", ["The landing in Normandy on 6 June 1944.", "The end of the war.", "An attack on Hawaii."]),
   Q(D, "What was the Marshall Plan?", ["American help to rebuild Europe.", "A bomb.", "A battle."])],
  [DT(D, "Quel président dirige les États-Unis pendant la guerre ?", ["Franklin D. Roosevelt", "Abraham Lincoln", "John F. Kennedy", "Richard Nixon"]),
   DT(D, "Comment s'appelle le programme de la bombe atomique ?", ["Le projet Manhattan", "Le projet Apollo", "Le plan Marshall", "Le plan Anaconda"]),
   DT(D, "Quelle bataille navale arrête le Japon en 1942 ?", ["Midway", "Waterloo", "Gettysburg", "Hastings"]),
   DT(D, "Sur quelles plages débarquent les Américains ?", ["Omaha et Utah Beach", "Malibu et Miami", "Brighton et Blackpool", "Waikiki et Honolulu"])],
  [W(D, "Trouve le mot qui veut dire « base navale » (2 mots).", ["naval base", "an american naval base"]), W(D, "Trouve le mot qui veut dire « chars ».", "tanks"),
   W(D, "Trouve le mot qui veut dire « ont débarqué ».", "landed"), W(D, "Trouve le mot qui veut dire « a capitulé ».", "surrendered")])

# ═════════ COLD WAR ═════════
F = "cu_guerre_froide.html"
DZ(F, """
## Deux blocs face à face
Après 1945, les anciens alliés deviennent rivaux. D'un côté, les États-Unis et leurs alliés, défenseurs de la démocratie libérale et du capitalisme ; de l'autre, l'**URSS** et ses alliés communistes. En 1946, Winston Churchill déclare qu'un **Iron Curtain** (rideau de fer) est tombé sur l'Europe. C'est la **Cold War** : une guerre « froide » parce que les deux superpuissances ne s'affrontent jamais directement, de peur d'une guerre nucléaire. Elles s'opposent par alliés interposés, par la propagande, l'espionnage, la course aux armements et la conquête spatiale.

## Berlin, ville symbole
L'Allemagne vaincue est divisée, et Berlin aussi. En 1948-1949, Staline bloque les accès terrestres à Berlin-Ouest ; les Américains organisent un immense **airlift**, un pont aérien qui ravitaille la ville pendant près d'un an. En **1961**, la RDA communiste construit le **Berlin Wall** pour empêcher ses habitants de fuir à l'Ouest. Le président Kennedy s'y rend en 1963 et prononce en allemand sa phrase célèbre « *Ich bin ein Berliner* ».

## Vivre avec la bombe
L'URSS possède la bombe atomique dès 1949. Les deux camps accumulent des milliers d'armes nucléaires : c'est l'équilibre de la terreur. Aux États-Unis, les enfants s'entraînent à l'école à se cacher sous leur bureau en cas d'attaque nucléaire (**duck and cover**), et certaines familles construisent des abris antiatomiques dans leur jardin.

## La crise de Cuba
En octobre 1962, des avions espions américains découvrent que l'URSS installe des missiles nucléaires à **Cuba**, à 150 km des côtes de Floride. Pendant **treize jours**, le monde est au bord de la guerre nucléaire. Kennedy impose un blocus naval de l'île. Finalement, le dirigeant soviétique **Nikita Khrouchtchev** accepte de retirer les missiles, en échange de la promesse américaine de ne pas envahir Cuba et, secrètement, du retrait de missiles américains en Turquie. Après la crise, un « téléphone rouge » relie Washington et Moscou.

## Les guerres « chaudes »
La guerre froide est loin d'être pacifique partout : guerre de Corée (1950-1953), guerre du Vietnam, Afghanistan, conflits en Afrique et en Amérique latine, où chaque camp soutient ses alliés, y compris des dictatures.

## La fin
Dans les années 1980, le président **Ronald Reagan** relance la course aux armements et qualifie l'URSS d'« empire du mal ». En 1987, à Berlin, il lance au dirigeant soviétique : « *Mr. Gorbachev, tear down this wall!* ». **Mikhaïl Gorbatchev** engage des réformes. Le **9 novembre 1989**, le mur de Berlin tombe. L'Allemagne est réunifiée en 1990, et l'URSS disparaît le **26 décembre 1991**. Les États-Unis restent la seule superpuissance.
""", """
a wall = un mur
a bomb = une bombe
a spy = un espion
a missile = un missile
fear = la peur
a crisis = une crise
an enemy = un ennemi
freedom = la liberté
""", [
 ("Pourquoi parle-t-on de guerre « froide » ?", ["Les deux superpuissances ne s'affrontent jamais directement", "Elle a lieu en Sibérie", "Elle a duré un hiver"], ""),
 ("Qu'est-ce que le pont aérien de Berlin ?", ["Le ravitaillement de Berlin-Ouest par avion pendant le blocus", "Un pont sur la Spree", "Une compagnie aérienne"], ""),
 ("Pourquoi le mur de Berlin est-il construit en 1961 ?", ["Pour empêcher les habitants de l'Est de fuir à l'Ouest", "Pour protéger la ville des inondations", "Pour séparer deux équipes"], ""),
 ("Qu'est-ce que « duck and cover » ?", ["Un exercice pour se protéger d'une attaque nucléaire", "Une danse", "Un jeu"], ""),
 ("Comment se termine la crise de Cuba ?", ["L'URSS retire ses missiles", "Les États-Unis envahissent Cuba", "Une guerre nucléaire éclate"], ""),
 ("Quand le mur de Berlin tombe-t-il ?", ["Le 9 novembre 1989", "En 1961", "En 1945"], ""),
], [("Staline", "dirigeant de l'URSS jusqu'en 1953"), ("RDA", "République démocratique allemande, l'Allemagne de l'Est"), ("**Nikita Khrouchtchev**", "dirigeant de l'URSS de 1953 à 1964"), ("**Mikhaïl Gorbatchev**", "dernier dirigeant de l'URSS")])
D = "cw2"
culture(F, "Culture : The Cold War", 'The Cold <span>War</span>',
  "Culture · rideau de fer, mur de Berlin et crise de Cuba", ("#bae6fd", "#991b1b"),
  reperes("De 1947 à 1991, les États-Unis et l'URSS s'opposent sans jamais se faire directement la guerre, sous la menace de l'arme nucléaire.",
    [("1946", "Churchill parle du « rideau de fer »"), ("1948 – 1949", "blocus et pont aérien de Berlin"), ("1949", "création de l'OTAN ; bombe atomique soviétique"),
     ("1961", "construction du mur de Berlin"), ("octobre 1962", "crise des missiles de Cuba"), ("9 nov. 1989", "chute du mur de Berlin"), ("26 déc. 1991", "fin de l'URSS")],
    "a superpower, communism, capitalism, the Iron Curtain, a wall, a missile, a spy, the arms race"),
  {D: doc("Thirteen days", [
    "After the Second World War, the USA and the Soviet Union became enemies. They never fought each other directly, because they were afraid of a nuclear war. This conflict is called the Cold War.",
    "Europe was divided by an \"Iron Curtain\". In 1961, the communists built a wall in Berlin to stop people from escaping to the West.",
    "Both countries built thousands of nuclear weapons. In American schools, children practised \"duck and cover\": hiding under their desks in case of a nuclear attack.",
    "In October 1962, the Americans discovered Soviet nuclear missiles in Cuba, very close to Florida. For thirteen days, the world was close to a nuclear war. Finally, the Soviet Union removed the missiles.",
    "On 9 November 1989, the Berlin Wall fell. Two years later, the Soviet Union disappeared, and the Cold War was over."])},
  [TF(D, "The USA and the Soviet Union fought each other directly.", False, "« They never fought each other directly »."),
   TF(D, "The Berlin Wall was built in 1961.", True, "« In 1961 »."),
   TF(D, "American children practised hiding under their desks.", True, "« duck and cover »."),
   TF(D, "The Soviet missiles were in Mexico.", False, "À Cuba."),
   TF(D, "The Cuban Missile Crisis lasted thirteen days.", True, "« For thirteen days »."),
   TF(D, "The Berlin Wall fell in 1989.", True, "« On 9 November 1989 »." )],
  [Q(D, "Why is it called the \"Cold\" War?", ["The two countries never fought directly.", "It happened in winter.", "It was in the Arctic."]),
   Q(D, "Why was the Berlin Wall built?", ["To stop people from escaping to the West.", "To protect Berlin from the sea.", "To separate two football teams."]),
   Q(D, "Why was Cuba dangerous for the USA?", ["It is very close to Florida.", "It had a big army.", "It had oil."]),
   Q(D, "When did the Soviet Union disappear?", ["In 1991.", "In 1961.", "In 1945."])],
  [DT(D, "Qui parle du « rideau de fer » en 1946 ?", ["Winston Churchill", "John F. Kennedy", "Ronald Reagan", "Staline"]),
   DT(D, "Qui est le dirigeant soviétique pendant la crise de Cuba ?", ["Khrouchtchev", "Gorbatchev", "Staline", "Lénine"]),
   DT(D, "Quel président dit « Tear down this wall! » ?", ["Ronald Reagan", "John F. Kennedy", "Richard Nixon", "Bill Clinton"]),
   DT(D, "Quelle alliance occidentale est créée en 1949 ?", ["L'OTAN", "L'ONU", "L'UE", "Le Commonwealth"])],
  [W(D, "Trouve le mot qui veut dire « ennemis ».", "enemies"), W(D, "Trouve le mot qui veut dire « s'échapper » (en -ing).", "escaping"),
   W(D, "Trouve le mot qui veut dire « armes ».", "weapons"), W(D, "Trouve le mot qui veut dire « a retiré ».", "removed")])

# ═════════ KENNEDY ═════════
F = "cu_kennedy.html"
DZ(F, """
## Un jeune président
**John Fitzgerald Kennedy** (**JFK**) naît en 1917 dans une riche famille catholique d'origine irlandaise du Massachusetts. Pendant la Seconde Guerre mondiale, il devient un héros en sauvant ses hommes après le naufrage de son bateau, le PT-109. Député, puis sénateur, il se présente à l'élection présidentielle de 1960 contre le vice-président républicain Richard Nixon. Le premier **televised debate** de l'histoire est décisif : face à un Nixon fatigué et en sueur, Kennedy paraît jeune, calme et bronzé. Il gagne de justesse et devient, à 43 ans, le plus jeune président élu et le premier président catholique.

## « Ne demandez pas… »
Dans son discours d'investiture, en janvier 1961, il lance une phrase restée célèbre : « *Ask not what your country can do for you — ask what you can do for your country* ». Il parle d'une **New Frontier** : la conquête de l'espace, la lutte contre la pauvreté, l'engagement de la jeunesse. Il crée les **Peace Corps**, des volontaires envoyés aider les pays en développement, et lance le programme qui conduira l'homme sur la Lune.

## Un président de la guerre froide
Son mandat est dominé par l'affrontement avec l'URSS. En 1961, le débarquement d'exilés cubains soutenus par la CIA dans la **Baie des Cochons** pour renverser Fidel Castro est un fiasco. La même année, le mur de Berlin est construit ; en 1963, Kennedy proclame à Berlin « *Ich bin ein Berliner* ». En octobre 1962, il gère la **crise des missiles de Cuba**, qui fait de lui une figure de fermeté et de sang-froid. Il augmente aussi l'engagement militaire américain au Vietnam. Sur les droits civiques, il hésite d'abord puis propose en 1963 une grande loi contre la ségrégation, votée après sa mort.

## Camelot
Avec sa femme **Jacqueline** (« Jackie »), élégante et cultivée, et leurs deux jeunes enfants, Kennedy incarne une image glamour et moderne de la Maison-Blanche, que l'on compare à la cour légendaire du roi Arthur : **Camelot**. Les historiens ont depuis révélé une réalité plus complexe : graves problèmes de santé cachés, nombreuses liaisons.

## Dallas, 22 novembre 1963
Lors d'un déplacement au Texas, Kennedy traverse **Dallas** en voiture décapotable. À 12 h 30, des coups de feu éclatent ; il est mortellement touché à la tête. **Lee Harvey Oswald**, un ancien marine qui avait vécu en URSS, est arrêté. Deux jours plus tard, devant les caméras de télévision, il est abattu par **Jack Ruby**, un patron de boîte de nuit. Le vice-président **Lyndon Johnson** prête serment dans l'avion présidentiel, aux côtés de Jackie, encore vêtue de son tailleur taché de sang.

## Un mystère qui fascine
En 1964, la **Warren Commission** conclut qu'Oswald a agi seul. Mais beaucoup d'Américains n'y croient pas : la mort d'Oswald, le film amateur d'Abraham Zapruder et d'autres éléments ont nourri d'innombrables **conspiracy theories** (Mafia, CIA, Cuba, URSS…), dont aucune n'a été prouvée. Cinq ans plus tard, en 1968, son frère **Robert Kennedy**, candidat à la présidence, est lui aussi assassiné. Pour beaucoup, la mort de JFK marque la fin d'une certaine innocence américaine.
""", """
a president = un président
a speech = un discours
a car = une voiture
a shot = un coup de feu
a debate = un débat
a wife = une épouse
young = jeune
a mystery = un mystère
""", [
 ("Pourquoi le débat télévisé de 1960 a-t-il été décisif ?", ["Kennedy paraissait jeune et calme face à un Nixon fatigué", "Nixon n'est pas venu", "Il a été annulé"], ""),
 ("Quel record Kennedy établit-il en 1960 ?", ["Le plus jeune président élu et le premier président catholique", "Le plus vieux président", "Le premier président noir"], ""),
 ("Que sont les Peace Corps ?", ["Des volontaires envoyés aider les pays en développement", "Une armée secrète", "Une équipe de football"], ""),
 ("Qu'est-ce que la Baie des Cochons ?", ["Un débarquement raté contre Castro à Cuba", "Une plage de Floride", "Une victoire militaire"], ""),
 ("Que se passe-t-il le 22 novembre 1963 ?", ["Kennedy est assassiné à Dallas", "Kennedy est élu", "La crise de Cuba"], ""),
 ("Que conclut la commission Warren ?", ["Oswald a agi seul", "La CIA a tué Kennedy", "Kennedy est vivant"], "Mais beaucoup d'Américains n'y croient pas."),
], [("Fidel Castro", "dirigeant communiste de Cuba"), ("Abraham Zapruder", "spectateur qui a filmé l'assassinat"), ("**Robert Kennedy**", "frère de JFK, ministre de la Justice")])
D = "jfk"
culture(F, "Culture : John F. Kennedy", 'John F. <span>Kennedy</span>',
  "Culture · le jeune président, la guerre froide et Dallas", ("#bfdbfe", "#1e3a8a"),
  reperes("John F. Kennedy, élu en 1960 à 43 ans, incarne la jeunesse et l'espoir. Son assassinat à Dallas en 1963 traumatise l'Amérique.",
    [("1917", "naissance dans le Massachusetts"), ("1960", "élu président après le premier débat télévisé"), ("avril 1961", "fiasco de la Baie des Cochons"),
     ("octobre 1962", "crise des missiles de Cuba"), ("22 nov. 1963", "assassinat à Dallas"), ("1964", "rapport de la commission Warren")],
    "a president, a speech, a debate, a crisis, an assassination, a gunman, a conspiracy theory, a legend"),
  {D: doc("Ask not…", [
    "John F. Kennedy, called JFK, was elected President in 1960. He was only 43, the youngest elected president, and the first Catholic president.",
    "His election was helped by the first televised debate: on TV, Kennedy looked young and calm, while his opponent, Richard Nixon, looked tired. In his first speech, he asked Americans to think about what they could do for their country.",
    "His presidency was marked by the Cold War: the failed invasion of Cuba in 1961, and the Cuban Missile Crisis in 1962. He also promised to send a man to the Moon.",
    "On 22 November 1963, Kennedy was shot in Dallas, Texas, while he was in an open car with his wife, Jackie. Lee Harvey Oswald was arrested, but he was killed two days later.",
    "An official commission said that Oswald acted alone, but many Americans believe in conspiracy theories. Kennedy's death shocked the whole world."])},
  [TF(D, "Kennedy was elected in 1960.", True, "« elected President in 1960 »."),
   TF(D, "He was the oldest elected president.", False, "« the youngest elected president »."),
   TF(D, "On TV, Nixon looked tired.", True, "« Richard Nixon, looked tired »."),
   TF(D, "Kennedy was shot in New York.", False, "À Dallas, au Texas."),
   TF(D, "Oswald was killed two days after his arrest.", True, "« he was killed two days later »."),
   TF(D, "All Americans believe that Oswald acted alone.", False, "« many Americans believe in conspiracy theories »." )],
  [Q(D, "What was special about Kennedy?", ["He was the youngest elected president and the first Catholic president.", "He was an actor.", "He was born in Texas."]),
   Q(D, "What did Kennedy ask Americans in his first speech?", ["To think about what they could do for their country.", "To pay more taxes.", "To leave Cuba."]),
   Q(D, "What happened in Cuba in 1962?", ["The Cuban Missile Crisis.", "A football match.", "Kennedy's wedding."]),
   Q(D, "What is a conspiracy theory?", ["The belief that a secret group organised an event.", "An official report.", "A TV debate."])],
  [DT(D, "Comment s'appelle la femme de Kennedy ?", ["Jacqueline (Jackie)", "Marilyn", "Eleanor", "Hillary"]),
   DT(D, "Qui tue Lee Harvey Oswald ?", ["Jack Ruby", "Robert Kennedy", "Lyndon Johnson", "Fidel Castro"]),
   DT(D, "Qui succède à Kennedy ?", ["Lyndon Johnson", "Richard Nixon", "Gerald Ford", "Robert Kennedy"]),
   DT(D, "Quel surnom donne-t-on à la Maison-Blanche des Kennedy ?", ["Camelot", "Avalon", "Hollywood", "The New Deal"])],
  [W(D, "Trouve le mot qui veut dire « adversaire ».", "opponent"), W(D, "Trouve le mot qui veut dire « raté » (adjectif).", "failed"),
   W(D, "Trouve le mot qui veut dire « une voiture décapotable » (2 mots).", ["open car", "an open car"]), W(D, "Trouve le mot qui veut dire « a choqué ».", "shocked")])
END()
