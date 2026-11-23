import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
exec(open(_EA_OUT+"/cuhelp.py", encoding="utf-8").read())

# ═════════ HONG KONG ═════════
F = "cu_hong_kong.html"
DZ(F, """
## Une colonie née de l'opium
Au 19e siècle, les marchands britanniques vendent de l'opium en Chine. Quand l'empereur chinois veut interdire ce commerce, le Royaume-Uni déclenche la **première guerre de l'opium** (1839-1842). Vaincue, la Chine doit céder l'île de **Hong Kong** au Royaume-Uni par le traité de Nankin (1842). La péninsule de Kowloon s'y ajoute en 1860, puis en 1898 les **New Territories** sont louées pour 99 ans, jusqu'en 1997.

## Un grand port international
Hong Kong devient un immense port et une place commerciale entre la Chine et le monde. Pendant la Seconde Guerre mondiale, elle est occupée par le Japon (1941-1945). Après la victoire des communistes en Chine en 1949, des centaines de milliers de réfugiés y arrivent. Dans les années 1960-1980, Hong Kong devient l'un des « dragons » asiatiques : industrie, finance, gratte-ciel, cinéma d'arts martiaux (Bruce Lee, Jackie Chan). La population parle surtout le **cantonais**, et l'anglais reste une langue officielle.

## La rétrocession de 1997
À l'approche de la fin du bail, Margaret Thatcher et le dirigeant chinois Deng Xiaoping signent en 1984 la **Sino-British Joint Declaration**. Le **1er juillet 1997**, Hong Kong est rendue à la Chine lors d'une cérémonie sous la pluie, en présence du prince Charles et du dernier gouverneur, Chris Patten. C'est la **handover**. Hong Kong devient une « région administrative spéciale » selon le principe **one country, two systems** : pendant 50 ans, jusqu'en 2047, elle doit garder son système capitaliste, sa justice indépendante, sa liberté de la presse et de manifester.

## Les tensions
Avec le temps, beaucoup d'habitants craignent que Pékin réduise ces libertés. En 2014, le **mouvement des parapluies** réclame des élections libres. En 2019, un projet de loi permettant d'extrader des suspects vers la Chine continentale provoque des manifestations gigantesques, parfois violentes. En 2020, Pékin impose une **loi sur la sécurité nationale** : de nombreux militants et journalistes sont arrêtés, des journaux pro-démocratie ferment, et des centaines de milliers d'habitants émigrent, notamment au Royaume-Uni qui leur ouvre un visa spécial. Pour les autorités chinoises, ces mesures ont rétabli l'ordre ; pour leurs critiques, elles ont mis fin au principe « un pays, deux systèmes ».
""", """
a port = un port
an island = une île
a colony = une colonie
a ceremony = une cérémonie
freedom = la liberté
a protest = une manifestation
an umbrella = un parapluie
a skyscraper = un gratte-ciel
""", [
 ("Comment Hong Kong devient-elle britannique ?", ["Après la première guerre de l'opium, en 1842", "Par un mariage royal", "Par un achat en 1997"], ""),
 ("Pourquoi 1997 ?", ["C'était la fin du bail de 99 ans des New Territories", "C'était l'anniversaire de la reine", "Une guerre éclate"], ""),
 ("Que signifie « one country, two systems » ?", ["Hong Kong garde son système et ses libertés dans la Chine", "Hong Kong a deux présidents", "La Chine devient britannique"], ""),
 ("Que réclame le mouvement des parapluies en 2014 ?", ["Des élections libres", "Plus de pluie", "L'indépendance du Japon"], ""),
 ("Qu'impose Pékin en 2020 ?", ["Une loi sur la sécurité nationale", "Une nouvelle monnaie", "Le retour des Britanniques"], ""),
 ("Quelle langue parle surtout la population ?", ["Le cantonais", "Le japonais", "Le français"], ""),
], [("Margaret Thatcher", "Première ministre britannique de 1979 à 1990"), ("Deng Xiaoping", "dirigeant de la Chine de 1978 à 1992"), ("Chris Patten", "dernier gouverneur britannique de Hong Kong")])
D = "hk"
culture(F, "Culture : Hong Kong 1997", 'Hong Kong <span>1997</span>',
  "Culture · de la colonie britannique à la Chine", ("#fecaca", "#b91c1c"),
  reperes("Colonie britannique pendant plus de 150 ans, Hong Kong a été rendue à la Chine en 1997.",
    [("1842", "Hong Kong cédée au Royaume-Uni après la guerre de l'opium"), ("1898", "les New Territories louées pour 99 ans"), ("1984", "accord entre Thatcher et Deng Xiaoping"),
     ("1er juillet 1997", "la handover : retour à la Chine"), ("2019 – 2020", "grandes manifestations, puis loi sur la sécurité nationale")],
    "a colony, the handover, a lease, a treaty, democracy, freedom of speech, a protest, one country two systems"),
  {D: doc("The handover", [
    "Hong Kong was a British colony for more than 150 years. Britain took the island after a war with China in 1842.",
    "Hong Kong became a very rich city with a huge port, banks and skyscrapers. Most people speak Cantonese, but English is also an official language.",
    "On 1 July 1997, Britain gave Hong Kong back to China. China promised \"one country, two systems\": for 50 years, Hong Kong could keep its freedoms and its own system.",
    "But many inhabitants were worried about their freedom. In 2019, huge protests took place. In 2020, China introduced a national security law, and many activists were arrested.",
    "Many Hong Kongers have moved abroad, especially to the UK. For China, the law brought back order; for its critics, it ended Hong Kong's freedoms."])},
  [TF(D, "Hong Kong was a British colony for more than 150 years.", True, "« more than 150 years »."),
   TF(D, "Most people in Hong Kong speak Japanese.", False, "« Cantonese »."),
   TF(D, "Britain gave Hong Kong back to China in 1997.", True, "« On 1 July 1997 »."),
   TF(D, "China promised \"one country, two systems\" for 100 years.", False, "« for 50 years »."),
   TF(D, "There were huge protests in 2019.", True, "« huge protests »."),
   TF(D, "Nobody left Hong Kong after 2020.", False, "« Many Hong Kongers have moved abroad »." )],
  [Q(D, "When did Britain take Hong Kong?", ["In 1842, after a war with China.", "In 1997.", "In 1066."]),
   Q(D, "What did China promise in 1997?", ["One country, two systems.", "Independence.", "A new queen."]),
   Q(D, "What happened in 2020?", ["China introduced a national security law.", "Hong Kong became British again.", "The port closed."]),
   Q(D, "Where did many Hong Kongers move?", ["Especially to the UK.", "To the Moon.", "To Antarctica."])],
  [DT(D, "Qui signe l'accord de 1984 côté britannique ?", ["Margaret Thatcher", "Winston Churchill", "Tony Blair", "Elizabeth II"]),
   DT(D, "Comment s'appelle le mouvement de 2014 ?", ["Le mouvement des parapluies", "Le printemps de Pékin", "La révolution de velours", "Le Brexit"]),
   DT(D, "Jusqu'à quand le principe doit-il durer ?", ["2047", "1997", "2020", "2097"]),
   DT(D, "Comment appelle-t-on la rétrocession en anglais ?", ["The handover", "The takeover", "The giveaway", "The return trip"])],
  [W(D, "Trouve le mot qui veut dire « libertés ».", "freedoms"), W(D, "Trouve le mot qui veut dire « habitants ».", "inhabitants"),
   W(D, "Trouve le mot qui veut dire « inquiets ».", "worried"), W(D, "Trouve le mot qui veut dire « à l'étranger ».", "abroad")])

# ═════════ AFRIQUE ANGLOPHONE ═════════
F = "cu_afrique_anglophone.html"
DZ(F, """
## L'héritage de l'empire
À la fin du 19e siècle, lors du « partage de l'Afrique », le Royaume-Uni colonise une grande partie du continent : Nigeria, Ghana, Kenya, Ouganda, Afrique du Sud, Zimbabwe, Zambie… Après la Seconde Guerre mondiale, ces pays obtiennent leur indépendance, souvent dans les années 1950-1960 : le **Ghana** est le premier, en 1957. La plupart rejoignent le **Commonwealth**. L'anglais y reste une langue officielle, utilisée dans l'administration, l'école et les affaires, à côté de centaines de langues locales.

## Le Nigeria, géant de l'Afrique
Indépendant depuis **1960**, le **Nigeria** est le pays le plus peuplé d'Afrique, avec plus de 220 millions d'habitants, et l'une de ses premières économies grâce au pétrole. On y parle plus de 500 langues, dont le haoussa, le yoruba et l'igbo ; le **Pidgin English** sert de langue commune à des millions de personnes. Sa plus grande ville, **Lagos**, est l'une des mégapoles les plus dynamiques du monde. Le pays a connu une guerre civile terrible, la guerre du **Biafra** (1967-1970).
Le Nigeria est une puissance culturelle :
- **Nollywood**, son industrie du cinéma, produit des milliers de films par an, l'une des plus grandes au monde en nombre de films ;
- l'**Afrobeats** (Burna Boy, Wizkid, Tems) conquiert les classements mondiaux ;
- la littérature : **Chinua Achebe** (*Things Fall Apart*, 1958), **Wole Soyinka**, premier Africain prix Nobel de littérature en 1986, et **Chimamanda Ngozi Adichie**.

## Le Kenya
Colonie britannique, le **Kenya** connaît dans les années 1950 la révolte des **Mau Mau**, réprimée très durement par les Britanniques. Il devient indépendant en **1963**, avec **Jomo Kenyatta** comme premier dirigeant. On y parle le swahili et l'anglais. Le Kenya est célèbre pour ses safaris et ses parcs nationaux (le Masai Mara), ses coureurs de fond champions du monde, et son innovation numérique : le paiement par téléphone mobile **M-Pesa**, lancé en 2007, y est devenu très courant. La militante écologiste **Wangari Maathai** a reçu le prix Nobel de la paix en 2004 pour avoir fait planter des millions d'arbres.

## Une Afrique jeune et connectée
L'Afrique anglophone est très jeune : au Nigeria, environ la moitié de la population a moins de 18 ans. Les défis restent importants (pauvreté, corruption, insécurité), mais la créativité de ses villes, de ses artistes et de ses entrepreneurs en fait un acteur de plus en plus visible dans le monde anglophone.
""", """
a country = un pays
a language = une langue
a city = une ville
a film = un film
music = la musique
a writer = un écrivain
a runner = un coureur
a tree = un arbre
""", [
 ("Quel est le premier pays d'Afrique noire indépendant de la colonisation britannique ?", ["Le Ghana, en 1957", "Le Kenya, en 1990", "Le Nigeria, en 1900"], ""),
 ("Pourquoi l'anglais est-il parlé au Nigeria et au Kenya ?", ["Ce sont d'anciennes colonies britanniques", "C'est la langue des touristes", "Par hasard"], ""),
 ("Qu'est-ce que Nollywood ?", ["L'industrie du cinéma nigériane", "Un quartier de Londres", "Un parc au Kenya"], ""),
 ("Quel écrivain nigérian a reçu le prix Nobel en 1986 ?", ["Wole Soyinka", "Chinua Achebe", "Burna Boy"], ""),
 ("Qu'est-ce que M-Pesa ?", ["Un système de paiement par téléphone mobile", "Une danse", "Un parc national"], ""),
 ("Pourquoi Wangari Maathai a-t-elle reçu le prix Nobel de la paix ?", ["Elle a fait planter des millions d'arbres", "Elle a gagné un marathon", "Elle a écrit un roman"], ""),
], [("**Jomo Kenyatta**", "premier président du Kenya"), ("**Chinua Achebe**", "romancier nigérian"), ("**Chimamanda Ngozi Adichie**", "romancière nigériane contemporaine"), ("Pidgin English", "langue mêlant anglais et langues africaines")])
D = "af"
culture(F, "Culture : English-speaking Africa", 'English-speaking <span>Africa</span>',
  "Culture · Nigeria, Kenya, Nollywood et Afrobeats", ("#86efac", "#b45309"),
  reperes("De nombreux pays d'Afrique, anciennes colonies britanniques, utilisent l'anglais comme langue officielle. Le Nigeria et le Kenya en sont deux exemples majeurs.",
    [("1957", "indépendance du Ghana"), ("1960", "indépendance du Nigeria"), ("1963", "indépendance du Kenya"), ("1986", "Wole Soyinka, prix Nobel de littérature"),
     ("2004", "Wangari Maathai, prix Nobel de la paix"), ("plus de 220 millions", "habitants au Nigeria")],
    "independence, a former colony, an official language, Pidgin English, Nollywood, Afrobeats, a safari, the Commonwealth"),
  {D: doc("Lagos and Nairobi", [
    "Many African countries were British colonies. After independence, English stayed an official language, used at school and in business, together with many local languages.",
    "Nigeria became independent in 1960. With more than 220 million inhabitants, it is the most populated country in Africa. Its biggest city, Lagos, is a huge and busy megacity.",
    "Nigeria is famous for Nollywood, its film industry, which makes thousands of films every year. Afrobeats singers like Burna Boy are popular all over the world.",
    "Kenya became independent in 1963. People speak Swahili and English. Kenya is famous for safaris, wild animals and long-distance runners. Many Kenyans pay with their mobile phones.",
    "The population of English-speaking Africa is very young, creative and more and more connected."])},
  [TF(D, "Many African countries were British colonies.", True, "« were British colonies »."),
   TF(D, "Nigeria became independent in 1990.", False, "« in 1960 »."),
   TF(D, "Nigeria is the most populated country in Africa.", True, "« the most populated country in Africa »."),
   TF(D, "Nollywood makes only a few films.", False, "« thousands of films every year »."),
   TF(D, "In Kenya, people speak Swahili and English.", True, "« Swahili and English »."),
   TF(D, "The population of English-speaking Africa is old.", False, "« very young »." )],
  [Q(D, "What is Lagos?", ["The biggest city in Nigeria.", "The capital of Kenya.", "A film."]),
   Q(D, "What is Nollywood?", ["Nigeria's film industry.", "A music festival.", "A Kenyan park."]),
   Q(D, "What is Kenya famous for?", ["Safaris, wild animals and runners.", "Snow and skiing.", "Pyramids."]),
   Q(D, "How do many Kenyans pay?", ["With their mobile phones.", "With gold.", "With cheques."])],
  [DT(D, "Quelle est la plus grande ville du Nigeria ?", ["Lagos", "Nairobi", "Accra", "Abuja"]),
   DT(D, "Qui est le premier dirigeant du Kenya indépendant ?", ["Jomo Kenyatta", "Nelson Mandela", "Kwame Nkrumah", "Wole Soyinka"]),
   DT(D, "Quel roman de Chinua Achebe paraît en 1958 ?", ["Things Fall Apart", "Animal Farm", "Of Mice and Men", "Jane Eyre"]),
   DT(D, "Quelle révolte éclate au Kenya dans les années 1950 ?", ["La révolte des Mau Mau", "La guerre du Biafra", "Le Bloody Sunday", "L'Easter Rising"])],
  [W(D, "Trouve le mot qui veut dire « indépendance ».", "independence"), W(D, "Trouve le mot qui veut dire « le plus peuplé » (2 mots).", ["most populated", "the most populated"]),
   W(D, "Trouve le mot qui veut dire « coureurs ».", "runners"), W(D, "Trouve le mot qui veut dire « connectée ».", "connected")])

# ═════════ SINGAPOUR ═════════
F = "cu_singapour.html"
DZ(F, """
## Un comptoir britannique
En **1819**, **Stamford Raffles**, agent de la Compagnie britannique des Indes orientales, fonde un comptoir commercial sur l'île de **Singapore**, au bout de la péninsule malaise. Idéalement placée sur la route maritime entre l'Inde et la Chine, la ville devient un grand port. Des immigrants arrivent de Chine, de Malaisie et d'Inde : c'est l'origine de la société multiethnique d'aujourd'hui. En 1942, Singapour tombe aux mains des Japonais : Churchill qualifie cette défaite de pire désastre de l'histoire militaire britannique.

## L'indépendance forcée
Après la guerre, Singapour obtient l'autonomie, puis rejoint la Malaisie en 1963. Mais les tensions politiques et ethniques sont fortes, et en **1965** Singapour est exclue de la fédération et devient un pays indépendant, sans ressources naturelles. Son premier Premier ministre, **Lee Kuan Yew**, pleure à la télévision en annonçant la séparation, qu'il appelle un « moment d'angoisse ».

## Le miracle économique
En une génération, sous la direction de Lee Kuan Yew (Premier ministre de 1959 à 1990), Singapour passe du statut de port pauvre à celui de l'un des pays les plus riches du monde : port parmi les plus actifs de la planète, place financière, aéroport réputé, entreprises de haute technologie. La plupart des habitants vivent dans des logements publics de qualité, les **HDB flats**. Les élèves singapouriens figurent parmi les meilleurs du monde dans les classements internationaux. La ville est très verte : on l'appelle la « ville-jardin ».

## Une société très encadrée
Singapour est célèbre pour ses règles strictes et ses amendes : jeter un papier par terre, manger dans le métro ou ne pas tirer la chasse d'eau peuvent coûter cher ; la vente de chewing-gum est interdite depuis 1992. La peine de mort existe pour le trafic de drogue. Le même parti, le **People's Action Party**, gouverne sans interruption depuis 1959. Pour ses partisans, ce modèle garantit sécurité, propreté et prospérité ; pour ses critiques, il limite la liberté d'expression et l'opposition politique.

## Une nation multilingue
Singapour a quatre langues officielles : l'**anglais**, le malais, le mandarin et le tamoul. L'anglais est la langue commune, de l'école et du travail. Dans la vie de tous les jours, beaucoup parlent le **Singlish**, un anglais mêlé de mots chinois et malais, ponctué de petites particules comme « *lah* » (« *Don't worry lah!* »). Le gouvernement a longtemps encouragé le « *Speak Good English* », mais le Singlish reste une fierté identitaire. Les **hawker centres**, grands marchés couverts de stands de cuisine de rue, sont même inscrits au patrimoine de l'UNESCO depuis 2020.
""", """
an island = une île
a port = un port
rich = riche
a rule = une règle
a fine = une amende
clean = propre
a language = une langue
street food = la cuisine de rue
""", [
 ("Qui fonde le comptoir britannique de Singapour en 1819 ?", ["Stamford Raffles", "Lee Kuan Yew", "Winston Churchill"], ""),
 ("Pourquoi Singapour devient-elle indépendante en 1965 ?", ["Elle est exclue de la fédération de Malaisie", "Elle gagne une guerre", "Le Royaume-Uni la vend"], ""),
 ("Qu'est-ce qui caractérise l'économie de Singapour ?", ["Un grand port, la finance et la haute technologie", "Le pétrole", "L'agriculture"], ""),
 ("Quelle est la règle célèbre depuis 1992 ?", ["La vente de chewing-gum est interdite", "Les voitures sont interdites", "Il faut parler chinois"], ""),
 ("Combien de langues officielles compte Singapour ?", ["Quatre", "Une", "Dix"], "Anglais, malais, mandarin, tamoul."),
 ("Qu'est-ce que le Singlish ?", ["Un anglais mêlé de mots chinois et malais", "Une chanson", "Un plat"], ""),
], [("**Stamford Raffles**", "administrateur colonial britannique"), ("**Lee Kuan Yew**", "fondateur du Singapour moderne")])
D = "sg"
culture(F, "Culture : Singapore", 'Singapore',
  "Culture · la cité-État anglophone d'Asie", ("#fecdd3", "#dc2626"),
  reperes("Ancien comptoir britannique, Singapour est devenue indépendante en 1965 et compte aujourd'hui parmi les pays les plus riches du monde. L'anglais y est la langue commune.",
    [("1819", "Stamford Raffles fonde un comptoir britannique"), ("1942", "occupation japonaise"), ("1965", "indépendance"),
     ("1959 – 1990", "Lee Kuan Yew Premier ministre"), ("1992", "interdiction de vendre du chewing-gum")],
    "a city-state, a port, a fine, a rule, multicultural, an official language, Singlish, a hawker centre"),
  {D: doc("The Lion City", [
    "Singapore is a small island country in South-East Asia. In 1819, a British man, Stamford Raffles, created a trading post there. It became a big port on the route between India and China.",
    "Singapore became independent in 1965. It had no natural resources, but its first Prime Minister, Lee Kuan Yew, transformed it into one of the richest countries in the world.",
    "Singapore is very clean and very safe, but the rules are strict. You can get a fine for dropping litter or eating on the metro, and selling chewing gum has been forbidden since 1992.",
    "The population is Chinese, Malay and Indian. There are four official languages, but English is the common language at school and at work. Many people also speak \"Singlish\", a mix of English, Chinese and Malay.",
    "Singaporeans love food. They often eat in hawker centres, big markets with many cheap street-food stalls."])},
  [TF(D, "Singapore is in South-East Asia.", True, "« in South-East Asia »."),
   TF(D, "Singapore became independent in 1819.", False, "« in 1965 »."),
   TF(D, "Singapore had a lot of natural resources.", False, "« no natural resources »."),
   TF(D, "Singapore is one of the richest countries in the world.", True, "« one of the richest countries »."),
   TF(D, "You can sell chewing gum freely in Singapore.", False, "« forbidden since 1992 »."),
   TF(D, "English is the common language at school.", True, "« English is the common language »." )],
  [Q(D, "Who created a trading post in Singapore?", ["Stamford Raffles.", "Lee Kuan Yew.", "Queen Victoria."]),
   Q(D, "What can you get a fine for?", ["Dropping litter or eating on the metro.", "Speaking English.", "Eating in hawker centres."]),
   Q(D, "What is Singlish?", ["A mix of English, Chinese and Malay.", "A type of food.", "A dance."]),
   Q(D, "What is a hawker centre?", ["A market with cheap street-food stalls.", "A bank.", "A school."])],
  [DT(D, "Quel est le surnom de Singapour ?", ["The Lion City", "The Big Apple", "The Windy City", "The Garden of Eden"]),
   DT(D, "Qui est le premier Premier ministre de Singapour ?", ["Lee Kuan Yew", "Stamford Raffles", "Deng Xiaoping", "Mahatma Gandhi"]),
   DT(D, "Quelle petite particule est typique du Singlish ?", ["« lah »", "« eh »", "« innit »", "« mate »"]),
   DT(D, "Depuis quand le parti PAP gouverne-t-il ?", ["1959", "1819", "1990", "2020"])],
  [W(D, "Trouve le mot qui veut dire « comptoir commercial » (2 mots).", ["trading post", "a trading post"]), W(D, "Trouve le mot qui veut dire « une amende ».", ["fine", "a fine"]),
   W(D, "Trouve le mot qui veut dire « interdit ».", "forbidden"), W(D, "Trouve le mot qui veut dire « stands ».", "stalls")])

# ═════════ GRANDS ROMANS ═════════
F = "cu_romans.html"
DZ(F, """
## Jane Austen et les sœurs Brontë
Au début du 19e siècle, **Jane Austen** (1775-1817) observe avec ironie la petite noblesse anglaise. Dans *Pride and Prejudice* (1813), la vive Elizabeth Bennet et l'orgueilleux Mr Darcy doivent surmonter leurs préjugés. Austen montre la pression sur les jeunes femmes, qui ne peuvent guère hériter et doivent faire un « bon mariage ».
Dans le Yorkshire, trois sœurs, **Charlotte, Emily et Anne Brontë**, publient d'abord sous des pseudonymes masculins, car les femmes écrivains sont mal acceptées. En 1847 paraissent *Jane Eyre* de Charlotte, histoire d'une orpheline indépendante qui devient gouvernante, et *Wuthering Heights* d'Emily, passion sauvage sur les landes battues par le vent.

## George Orwell
**George Orwell** (1903-1950), écrivain britannique, dénonce les totalitarismes. *Animal Farm* (1945) est une fable : les animaux d'une ferme chassent le fermier, mais les cochons prennent le pouvoir et deviennent aussi tyranniques que les humains, une critique de la révolution russe devenue dictature stalinienne. *Nineteen Eighty-Four* (1949) décrit un monde où un parti unique surveille chacun en permanence (« *Big Brother is watching you* »), réécrit le passé et contrôle même la langue. Des mots comme « Big Brother » ou « orwellien » sont passés dans le langage courant.

## John Steinbeck
L'Américain **John Steinbeck** (1902-1968), prix Nobel en 1962, raconte la Grande Dépression. Dans *Of Mice and Men* (1937), deux ouvriers agricoles itinérants de Californie, George, petit et malin, et Lennie, colosse à l'esprit d'enfant, rêvent d'avoir un jour leur propre ferme. Le rêve se termine tragiquement. *The Grapes of Wrath* (1939) suit une famille de fermiers de l'Oklahoma ruinée par le Dust Bowl.

## Harper Lee
*To Kill a Mockingbird* (1960), de l'Américaine **Harper Lee**, prix Pulitzer, se passe dans une petite ville de l'Alabama des années 1930. La jeune Scout raconte comment son père, l'avocat **Atticus Finch**, défend un homme noir, Tom Robinson, faussement accusé d'avoir agressé une femme blanche. Le roman dénonce le racisme et l'injustice de la ségrégation ; le « mockingbird » (oiseau moqueur), qui ne fait de mal à personne, symbolise l'innocence détruite.

## Pourquoi les lit-on encore ?
Ces livres sont étudiés dans les écoles du monde anglophone parce qu'ils parlent de thèmes universels : l'amour et les préjugés, la place des femmes, la liberté, le pouvoir, la pauvreté, le racisme. Certains ont parfois été retirés de bibliothèques scolaires américaines à cause de leurs thèmes ou de leur langage, ce qui relance régulièrement le débat sur la censure.
[→ Approfondir : George Orwell](cu_orwell.html)
[→ Approfondir : les dystopies, de 1984 à Fahrenheit 451](cu_dystopies.html)
""", """
a novel = un roman
a writer = un écrivain
a book = un livre
a character = un personnage
a farm = une ferme
a dream = un rêve
a lawyer = un avocat
freedom = la liberté
""", [
 ("De quoi parle Pride and Prejudice ?", ["D'amour, de préjugés et de mariage dans la petite noblesse", "D'une guerre", "D'une ferme d'animaux"], ""),
 ("Pourquoi les sœurs Brontë utilisent-elles des pseudonymes masculins ?", ["Les femmes écrivains sont mal acceptées", "Pour se cacher de la police", "Par jeu"], ""),
 ("Que critique Animal Farm ?", ["La révolution russe devenue dictature", "L'agriculture moderne", "La monarchie anglaise"], ""),
 ("Que signifie « Big Brother is watching you » ?", ["Le pouvoir surveille tout le monde", "Mon grand frère me regarde", "Un jeu télévisé"], ""),
 ("De quoi rêvent George et Lennie dans Of Mice and Men ?", ["D'avoir leur propre ferme", "D'aller à Hollywood", "De devenir riches en Bourse"], ""),
 ("Que dénonce To Kill a Mockingbird ?", ["Le racisme et l'injustice de la ségrégation", "La guerre du Vietnam", "La monarchie"], ""),
], [("Dust Bowl", "tempêtes de poussière des années 1930"), ("**Atticus Finch**", "avocat, héros du roman")])
D = "ro"
culture(F, "Culture : Great novels in English", 'Great <span>novels</span>',
  "Culture · Austen, Brontë, Orwell, Steinbeck, Harper Lee", ("#e9d5ff", "#7c2d12"),
  reperes("Quelques grands romans de langue anglaise sont lus et étudiés dans le monde entier.",
    [("1813", "Pride and Prejudice, Jane Austen"), ("1847", "Jane Eyre (Charlotte Brontë) et Wuthering Heights (Emily Brontë)"), ("1937", "Of Mice and Men, John Steinbeck"),
     ("1945", "Animal Farm, George Orwell"), ("1949", "Nineteen Eighty-Four, George Orwell"), ("1960", "To Kill a Mockingbird, Harper Lee")],
    "a novel, a writer, a character, a plot, a theme, a classic, prejudice, injustice"),
  {D: doc("Books that changed the world", [
    "In Pride and Prejudice (1813), Jane Austen tells the story of Elizabeth Bennet and the proud Mr Darcy. At that time, young women had to find a good husband.",
    "The Brontë sisters first published their novels under men's names. In Jane Eyre (1847), an orphan girl becomes a strong and independent woman.",
    "George Orwell wrote Animal Farm, a story about animals who take control of a farm, and Nineteen Eighty-Four, about a world where Big Brother watches everybody.",
    "In Of Mice and Men, John Steinbeck tells the story of two poor farm workers during the Great Depression. They dream of having their own farm.",
    "In To Kill a Mockingbird, by Harper Lee, a lawyer called Atticus Finch defends a Black man in Alabama. The novel is about racism and injustice."])},
  [TF(D, "Pride and Prejudice was written by Jane Austen.", True, "« Jane Austen tells the story »."),
   TF(D, "The Brontë sisters always used their real names.", False, "« under men's names »."),
   TF(D, "In Jane Eyre, an orphan girl becomes independent.", True, "« a strong and independent woman »."),
   TF(D, "Animal Farm is about animals who take control of a farm.", True, "« animals who take control of a farm »."),
   TF(D, "Of Mice and Men is about rich bankers.", False, "« two poor farm workers »."),
   TF(D, "To Kill a Mockingbird is about racism.", True, "« about racism and injustice »." )],
  [Q(D, "Who is Mr Darcy?", ["A proud man in Pride and Prejudice.", "A farmer in Of Mice and Men.", "A lawyer in Alabama."]),
   Q(D, "What is Nineteen Eighty-Four about?", ["A world where Big Brother watches everybody.", "A love story.", "A farm."]),
   Q(D, "What do the farm workers dream of?", ["Having their own farm.", "Becoming actors.", "Going to the Moon."]),
   Q(D, "Who is Atticus Finch?", ["A lawyer who defends a Black man.", "A pig.", "A teacher in London."])],
  [DT(D, "Qui a écrit Wuthering Heights ?", ["Emily Brontë", "Jane Austen", "Charlotte Brontë", "Harper Lee"]),
   DT(D, "Quel prix a reçu To Kill a Mockingbird ?", ["Le prix Pulitzer", "Le prix Nobel de la paix", "Un Oscar", "Le prix Goncourt"]),
   DT(D, "Quel adjectif vient du nom d'Orwell ?", ["Orwellien", "Orweller", "Orwelliste", "Orwelois"]),
   DT(D, "Que symbolise le mockingbird ?", ["L'innocence", "La guerre", "La richesse", "La vitesse"])],
  [W(D, "Trouve le mot qui veut dire « fier, orgueilleux ».", "proud"), W(D, "Trouve le mot qui veut dire « un mari ».", ["husband", "a good husband"]),
   W(D, "Trouve le mot qui veut dire « un orphelin / une orpheline ».", ["orphan", "an orphan"]), W(D, "Trouve le mot qui veut dire « un avocat ».", ["lawyer", "a lawyer"])])

# ═════════ LITTÉRATURE JEUNESSE ═════════
F = "cu_litterature_jeunesse.html"
DZ(F, """
## Un trésor britannique
La littérature pour la jeunesse est l'une des grandes fiertés culturelles du Royaume-Uni. En 1865, **Lewis Carroll** publie *Alice's Adventures in Wonderland* : Alice tombe dans un terrier de lapin et découvre un monde absurde, avec le Chapelier fou et la Reine de cœur. Suivent *Peter Pan* (1904) de J. M. Barrie, le garçon qui ne voulait pas grandir, et *Winnie-the-Pooh* (1926) d'A. A. Milne.

## Tolkien et Lewis, deux amis d'Oxford
**J. R. R. Tolkien** (1892-1973), professeur à Oxford et spécialiste des langues anciennes, invente un monde complet, la Terre du Milieu, avec ses langues, ses cartes et son histoire. *The Hobbit* (1937) raconte l'aventure de Bilbo, un petit hobbit casanier entraîné dans une quête pour reprendre un trésor gardé par le dragon Smaug. *The Lord of the Rings* (1954-1955) en est la suite épique. Tolkien est considéré comme le père de la **fantasy** moderne.
Son ami **C. S. Lewis** écrit *The Chronicles of Narnia* (1950-1956) : quatre enfants, évacués pendant la guerre, traversent une armoire et arrivent dans le pays magique de Narnia, gouverné par le lion Aslan.

## Roald Dahl
**Roald Dahl** (1916-1990), Britannique d'origine norvégienne, ancien pilote de chasse, écrit des histoires drôles, parfois cruelles, où les enfants triomphent des adultes méchants : *Charlie and the Chocolate Factory* (1964), *The BFG* (1982), *The Witches* (1983), *Matilda* (1988). Il invente des mots extravagants (le « gobblefunk »). En 2023, la modification de certains mots de ses livres par son éditeur pour les rendre moins blessants a provoqué un grand débat sur la réécriture des classiques.

## Harry Potter, un phénomène mondial
En **1997**, **J. K. Rowling**, une mère célibataire sans le sou qui écrivait dans les cafés d'Édimbourg, publie *Harry Potter and the Philosopher's Stone*, après avoir été refusée par une douzaine d'éditeurs. La saga en sept tomes, qui suit un jeune sorcier à l'école de **Hogwarts**, s'est vendue à plus de 600 millions d'exemplaires, traduite dans plus de 80 langues, et adaptée en huit films. Elle a donné le goût de la lecture à toute une génération. Son autrice a depuis suscité des controverses en raison de ses prises de position publiques, qui divisent une partie des fans.

## Pourquoi ces histoires marchent-elles ?
Ces livres partagent souvent des ingrédients : un enfant ordinaire qui découvre un monde secret, une quête, le combat entre le bien et le mal, l'amitié et le courage. Beaucoup ont été écrits pour des enfants réels : Alice pour une petite fille de l'entourage de Carroll, *The Hobbit* et *Winnie-the-Pooh* d'abord racontés aux enfants de leurs auteurs.
""", """
a story = une histoire
a wizard = un sorcier
a dragon = un dragon
a witch = une sorcière
magic = la magie
a rabbit = un lapin
a giant = un géant
a quest = une quête
""", [
 ("Que découvre Alice en tombant dans le terrier ?", ["Un monde absurde, le Pays des merveilles", "Un trésor", "Une école de sorcellerie"], ""),
 ("Pourquoi Tolkien est-il appelé le père de la fantasy moderne ?", ["Il a inventé un monde complet, la Terre du Milieu", "Il a inventé le cinéma", "Il a écrit le premier roman"], ""),
 ("Comment les enfants arrivent-ils à Narnia ?", ["En traversant une armoire", "En prenant un train", "En tombant dans un terrier"], ""),
 ("Quel est le point commun des histoires de Roald Dahl ?", ["Les enfants triomphent des adultes méchants", "Elles se passent dans l'espace", "Elles sont sans humour"], ""),
 ("Que s'est-il passé avant la publication de Harry Potter ?", ["Le livre a été refusé par une douzaine d'éditeurs", "Il a d'abord été un film", "Il est sorti en français"], ""),
 ("Quel ingrédient revient souvent dans ces livres ?", ["Un enfant ordinaire qui découvre un monde secret", "Une histoire d'amour d'adultes", "Un manuel scolaire"], ""),
], [("**Lewis Carroll**", "pseudonyme de Charles Dodgson, mathématicien d'Oxford"), ("**C. S. Lewis**", "écrivain et professeur à Oxford"), ("Hogwarts", "Poudlard, l'école de sorcellerie")])
D = "lj"
culture(F, "Culture : Children's literature", "Children's <span>literature</span>",
  "Culture · Alice, Tolkien, Narnia, Roald Dahl, Harry Potter", ("#c4b5fd", "#15803d"),
  reperes("Le Royaume-Uni a produit beaucoup des livres pour la jeunesse les plus célèbres du monde.",
    [("1865", "Alice's Adventures in Wonderland, Lewis Carroll"), ("1937", "The Hobbit, J. R. R. Tolkien"), ("1950", "début des Chronicles of Narnia, C. S. Lewis"),
     ("1964", "Charlie and the Chocolate Factory, Roald Dahl"), ("1997", "Harry Potter and the Philosopher's Stone, J. K. Rowling")],
    "a story, a character, a wizard, a witch, a dragon, fantasy, a quest, a bestseller"),
  {D: doc("Once upon a time", [
    "Many famous children's books come from Britain. In 1865, Lewis Carroll wrote Alice's Adventures in Wonderland, about a girl who falls down a rabbit hole into a strange world.",
    "J. R. R. Tolkien, a professor at Oxford, wrote The Hobbit and The Lord of the Rings. His friend C. S. Lewis wrote The Chronicles of Narnia, where children enter a magic land through a wardrobe.",
    "Roald Dahl wrote funny stories like Charlie and the Chocolate Factory and Matilda. In his books, children are often cleverer than the adults.",
    "In 1997, J. K. Rowling published the first Harry Potter book. Before that, a dozen publishers had refused it! The series sold more than 600 million copies.",
    "These books often tell the story of an ordinary child who discovers a secret world and fights against evil."])},
  [TF(D, "Alice falls down a rabbit hole.", True, "« falls down a rabbit hole »."),
   TF(D, "Tolkien was a professor at Cambridge.", False, "« at Oxford »."),
   TF(D, "In Narnia, children enter through a wardrobe.", True, "« through a wardrobe »."),
   TF(D, "In Roald Dahl's books, adults are always cleverer.", False, "« children are often cleverer »."),
   TF(D, "Harry Potter was accepted by the first publisher.", False, "« a dozen publishers had refused it »."),
   TF(D, "The Harry Potter series sold more than 600 million copies.", True, "« more than 600 million copies »." )],
  [Q(D, "Who wrote Alice's Adventures in Wonderland?", ["Lewis Carroll.", "Roald Dahl.", "J. K. Rowling."]),
   Q(D, "What did Tolkien write?", ["The Hobbit and The Lord of the Rings.", "Matilda.", "Peter Pan."]),
   Q(D, "What did Roald Dahl write?", ["Charlie and the Chocolate Factory and Matilda.", "Narnia.", "Harry Potter."]),
   Q(D, "What happens in many of these books?", ["An ordinary child discovers a secret world.", "Adults go to work.", "Nothing happens."])],
  [DT(D, "Comment s'appelle le monde inventé par Tolkien ?", ["La Terre du Milieu", "Narnia", "Le Pays des merveilles", "Poudlard"]),
   DT(D, "Quel lion gouverne Narnia ?", ["Aslan", "Simba", "Smaug", "Mufasa"]),
   DT(D, "Dans quelle ville J. K. Rowling écrivait-elle dans les cafés ?", ["Édimbourg", "Londres", "Oxford", "Dublin"]),
   DT(D, "Quel personnage ne voulait pas grandir ?", ["Peter Pan", "Bilbo", "Charlie", "Alice"])],
  [W(D, "Trouve le mot qui veut dire « une armoire ».", ["wardrobe", "a wardrobe"]), W(D, "Trouve le mot qui veut dire « plus intelligents ».", "cleverer"),
   W(D, "Trouve le mot qui veut dire « éditeurs ».", "publishers"), W(D, "Trouve le mot qui veut dire « le mal ».", "evil")])

# ═════════ ART ═════════
F = "cu_art.html"
DZ(F, """
## J. M. W. Turner, le peintre de la lumière
**Joseph Mallord William Turner** (1775-1851), fils d'un barbier de Londres, entre très jeune à la Royal Academy. Il peint des paysages, des tempêtes, des incendies et des navires dans des tourbillons de lumière et de couleur, presque abstraits pour son époque. *The Fighting Temeraire* (1839) montre un vieux navire de guerre remorqué par un bateau à vapeur vers sa destruction ; *Rain, Steam and Speed* (1844) représente un train lancé à toute vitesse sous la pluie, symbole de la révolution industrielle. Turner annonce l'impressionnisme. Son visage figure sur le billet de 20 livres depuis 2020, et le **Turner Prize**, créé en 1984, récompense chaque année un artiste contemporain britannique.

## Andy Warhol et le pop art
Dans les années 1950-1960, des artistes britanniques puis américains créent le **pop art** : ils s'inspirent de la publicité, des bandes dessinées et des produits de consommation. L'Américain **Andy Warhol** (1928-1987), ancien illustrateur publicitaire, peint en 1962 les *Campbell's Soup Cans*, 32 tableaux de boîtes de soupe, et reproduit en sérigraphie aux couleurs vives des portraits de stars comme **Marilyn Monroe**. Dans son atelier de New York, **The Factory**, il produit ses œuvres comme en usine. On lui attribue l'idée qu'à l'avenir, chacun connaîtra son quart d'heure de célébrité mondiale. Le pop art pose une question : l'art peut-il être un objet de consommation comme un autre ?

## Banksy, l'artiste invisible
**Banksy** est un artiste de rue (**street artist**) originaire de Bristol, dont l'identité reste officiellement secrète. Depuis les années 1990, il peint au pochoir sur les murs des villes des œuvres pleines d'humour et de critique politique : contre la guerre, la société de consommation, la surveillance, les inégalités. Ses œuvres apparaissent sur le mur de séparation en Cisjordanie, à Calais, en Ukraine… *Girl with Balloon* montre une petite fille laissant s'envoler un ballon rouge en forme de cœur. En 2018, au moment où une version encadrée est vendue aux enchères à Londres pour plus d'un million de livres, une broyeuse cachée dans le cadre la découpe partiellement sous les yeux du public ; rebaptisée *Love is in the Bin*, l'œuvre est revendue en 2021 pour bien plus cher.

## L'art est-il vandalisme ?
Le **street art** pose des questions : un graffiti non autorisé est-il de l'art ou du vandalisme ? Une œuvre peinte sur un mur appartient-elle au propriétaire du mur ? Certaines municipalités effacent les graffitis, d'autres protègent ceux de Banksy sous plexiglas, car ils attirent les touristes et peuvent valoir des fortunes.
""", """
a painter = un peintre
a painting = un tableau
light = la lumière
a museum = un musée
a wall = un mur
a balloon = un ballon (de baudruche)
a soup can = une boîte de soupe
an artist = un artiste
""", [
 ("Que peint surtout Turner ?", ["Des paysages, tempêtes et navires dans la lumière", "Des boîtes de soupe", "Des graffitis"], ""),
 ("Quel mouvement Turner annonce-t-il ?", ["L'impressionnisme", "Le pop art", "Le street art"], ""),
 ("De quoi s'inspire le pop art ?", ["De la publicité, des BD et des produits de consommation", "De la Bible", "De la nature sauvage"], ""),
 ("Qu'est-ce que The Factory ?", ["L'atelier new-yorkais de Warhol", "Une usine de soupe", "Un musée de Londres"], ""),
 ("Que s'est-il passé en 2018 lors de la vente de Girl with Balloon ?", ["Une broyeuse cachée a découpé l'œuvre", "Elle a été volée", "Elle a brûlé"], ""),
 ("Quelle question pose le street art ?", ["Un graffiti est-il de l'art ou du vandalisme ?", "Faut-il peindre à l'huile ?", "Les musées doivent-ils fermer ?"], ""),
], [("Royal Academy", "grande école et institution artistique de Londres"), ("sérigraphie", "technique d'impression permettant de reproduire une image")])
D = "ar"
culture(F, "Culture : Art – Turner, Warhol, Banksy", 'Turner, Warhol <span>&amp; Banksy</span>',
  "Culture · trois artistes, trois révolutions", ("#fbcfe8", "#2563eb"),
  reperes("De la peinture de lumière de Turner au pop art de Warhol et au street art de Banksy : trois grandes figures de l'art anglophone.",
    [("1844", "Rain, Steam and Speed de Turner"), ("1962", "les Campbell's Soup Cans de Warhol"), ("1984", "création du Turner Prize"),
     ("2018", "Girl with Balloon broyée pendant sa vente"), ("2020", "Turner sur le billet de 20 livres")],
    "a painter, a painting, a landscape, pop art, street art, a stencil, an auction, a gallery"),
  {D: doc("From canvas to street", [
    "J. M. W. Turner was a British painter of the 19th century. He painted landscapes, storms and ships full of light and colour. Today, his face is on the £20 note.",
    "Andy Warhol was an American artist of the 1960s. He created pop art: he painted everyday objects like soup cans and famous people like Marilyn Monroe, in bright colours.",
    "Banksy is a street artist from Bristol. Nobody officially knows who he is. He paints on walls with stencils, and his works are often funny and political.",
    "In 2018, his painting Girl with Balloon was sold at an auction in London. Just after the sale, a hidden machine in the frame cut the picture into strips!",
    "Some people think that street art is vandalism. Others think it is art for everybody, in the street and free."])},
  [TF(D, "Turner was an American painter.", False, "« a British painter »."),
   TF(D, "Turner's face is on the £20 note.", True, "« on the £20 note »."),
   TF(D, "Andy Warhol painted soup cans.", True, "« soup cans »."),
   TF(D, "Everybody knows who Banksy is.", False, "« Nobody officially knows who he is »."),
   TF(D, "Banksy paints with stencils.", True, "« with stencils »."),
   TF(D, "Everybody agrees that street art is art.", False, "« Some people think that street art is vandalism »." )],
  [Q(D, "What did Turner paint?", ["Landscapes, storms and ships.", "Soup cans.", "Graffiti."]),
   Q(D, "What is pop art?", ["Art inspired by everyday objects and famous people.", "Very old religious art.", "Music."]),
   Q(D, "Where is Banksy from?", ["Bristol.", "New York.", "Paris."]),
   Q(D, "What happened to Girl with Balloon in 2018?", ["A hidden machine cut it into strips.", "It was stolen.", "It was painted again."])],
  [DT(D, "Quel prix porte le nom de Turner ?", ["Le Turner Prize", "Le Booker Prize", "Le prix Pulitzer", "L'Oscar"]),
   DT(D, "Quelle star Warhol a-t-il représentée ?", ["Marilyn Monroe", "Elvis Presley seulement", "Charlie Chaplin", "Queen Victoria"]),
   DT(D, "Comment a été rebaptisée Girl with Balloon ?", ["Love is in the Bin", "Girl without Balloon", "Broken Heart", "The Shredder"]),
   DT(D, "Comment dit-on « une vente aux enchères » ?", ["An auction", "A sale party", "A market", "A shop"])],
  [W(D, "Trouve le mot qui veut dire « tempêtes ».", "storms"), W(D, "Trouve le mot qui veut dire « un billet » (de banque).", ["note", "the £20 note"]),
   W(D, "Trouve le mot qui veut dire « pochoirs ».", "stencils"), W(D, "Trouve le mot qui veut dire « bandes » (de papier).", "strips")])

# ═════════ CONSOMMATION (CAP) ═════════
F = "cu_consommation.html"
DZ(F, """
## Black Friday
Aux États-Unis, **Thanksgiving** est fêté le quatrième jeudi de novembre. Le lendemain, le **Black Friday**, marque le début de la saison des achats de Noël : les magasins ouvrent très tôt, parfois à l'aube, avec des réductions spectaculaires (**deals**, **doorbusters**). On explique souvent le nom par la comptabilité : c'est le jour où les commerçants « passent dans le noir », c'est-à-dire deviennent bénéficiaires ; à l'origine, la police de Philadelphie l'utilisait pour désigner les embouteillages et la foule de ce jour-là. Les images de clients qui se bousculent à l'ouverture ont fait le tour du monde. Le lundi suivant, le **Cyber Monday** est consacré aux achats en ligne. Le Black Friday s'est exporté au Royaume-Uni, en France et ailleurs.

## Boxing Day
Au Royaume-Uni, au Canada, en Australie… le 26 décembre est le **Boxing Day**. Son nom viendrait des « boîtes » (*boxes*) de cadeaux ou d'argent que les maîtres donnaient autrefois à leurs domestiques et aux commerçants le lendemain de Noël. Aujourd'hui, c'est un jour férié et le grand jour des soldes (**sales**), mais aussi de matchs de football très suivis.

## Le mall
Le **shopping mall** (centre commercial) se développe aux États-Unis après la guerre, avec les banlieues et la voiture. Le premier mall entièrement couvert ouvre en 1956 près de Minneapolis. Le **Mall of America**, dans le Minnesota, l'un des plus grands du pays, abrite même un parc d'attractions. Pour beaucoup d'adolescents américains, le mall a longtemps été un lieu de sortie. Depuis l'essor du commerce en ligne, de nombreux malls ferment (**dead malls**).

## Consommer à crédit
Les Américains et les Britanniques utilisent beaucoup les **credit cards** et achètent souvent à crédit, ce qui peut entraîner un fort endettement. Les formules « achetez maintenant, payez plus tard » (**buy now, pay later**) se sont multipliées. Aux États-Unis, les prix affichés en magasin sont généralement **hors taxes** : la **sales tax** s'ajoute en caisse et varie selon l'État. Les retours (**refunds**, **returns**) sont souvent faciles : on peut rapporter un article avec son ticket de caisse (**receipt**).

## Les critiques
Cette consommation de masse est critiquée : gaspillage, déchets, conditions de travail dans les usines et les entrepôts, pollution liée à la **fast fashion** et aux livraisons. En réaction, certains participent au **Buy Nothing Day** (journée sans achat), le jour même du Black Friday, ou se tournent vers l'occasion (**second-hand**), les **charity shops** britanniques et la réparation.
""", """
a shop = un magasin
a customer = un client
a price = un prix
a discount = une réduction
the sales = les soldes
a receipt = un ticket de caisse
cheap = bon marché
to buy = acheter
""", [
 ("Quand a lieu le Black Friday ?", ["Le lendemain de Thanksgiving, fin novembre", "Le 26 décembre", "Le 1er janvier"], ""),
 ("Qu'est-ce que le Cyber Monday ?", ["Un jour de soldes en ligne, le lundi suivant", "Un jour sans ordinateur", "Une fête religieuse"], ""),
 ("Qu'est-ce que le Boxing Day ?", ["Le 26 décembre, jour férié et de soldes", "Une journée de boxe obligatoire", "Le jour de Thanksgiving"], ""),
 ("Pourquoi de nombreux malls ferment-ils ?", ["À cause de l'essor du commerce en ligne", "À cause de la neige", "Ils sont trop petits"], ""),
 ("Qu'est-ce que la sales tax aux États-Unis ?", ["Une taxe ajoutée en caisse, qui varie selon l'État", "Une réduction", "Un pourboire"], ""),
 ("Qu'est-ce que le Buy Nothing Day ?", ["Une journée sans achat contre la surconsommation", "Une journée de soldes", "Un jour férié"], ""),
], [("Thanksgiving", "fête américaine des récoltes, en famille"), ("fast fashion", "vêtements bon marché renouvelés très vite")])
D = "co"
culture(F, "Culture : Shopping and consumer culture", 'Shopping <span>culture</span>',
  "Culture · Black Friday, Boxing Day, malls et consommation", ("#fde047", "#111827"),
  reperes("Les pays anglophones ont inventé ou popularisé de grands rendez-vous de consommation, comme le Black Friday et le Boxing Day.",
    [("4e jeudi de novembre", "Thanksgiving aux États-Unis"), ("le lendemain", "Black Friday"), ("le lundi suivant", "Cyber Monday"),
     ("26 décembre", "Boxing Day"), ("1956", "premier mall couvert aux États-Unis")],
    "a shop, a customer, a deal, a discount, the sales, a receipt, a refund, second-hand"),
  {D: doc("Shop till you drop", [
    "In the USA, Black Friday is the day after Thanksgiving, at the end of November. Shops open very early and offer big discounts. Some customers queue all night to get the best deals.",
    "The following Monday is Cyber Monday, when people buy online. Black Friday now exists in many countries, including France and the UK.",
    "In the UK, the day after Christmas is Boxing Day. It is a bank holiday, and it is the first day of the winter sales.",
    "Americans often shop in malls, big shopping centres with many shops, restaurants and cinemas. In the USA, the price on the label does not include the tax: you pay a little more at the till.",
    "Some people criticise this mass consumption. On Black Friday, they celebrate Buy Nothing Day, or they buy second-hand clothes in charity shops."])},
  [TF(D, "Black Friday is the day after Thanksgiving.", True, "« the day after Thanksgiving »."),
   TF(D, "On Black Friday, shops open very late.", False, "« Shops open very early »."),
   TF(D, "On Cyber Monday, people buy online.", True, "« people buy online »."),
   TF(D, "Boxing Day is the day before Christmas.", False, "« the day after Christmas »."),
   TF(D, "In the USA, the price on the label includes the tax.", False, "« does not include the tax »."),
   TF(D, "Some people buy second-hand clothes in charity shops.", True, "« in charity shops »." )],
  [Q(D, "What do some customers do on Black Friday?", ["They queue all night.", "They stay in bed.", "They go to church."]),
   Q(D, "What is Boxing Day?", ["The day after Christmas, the first day of the sales.", "A sports competition.", "The day before Thanksgiving."]),
   Q(D, "What is a mall?", ["A big shopping centre.", "A small shop.", "A market in the street."]),
   Q(D, "What is Buy Nothing Day?", ["A day when people buy nothing.", "A day with free products.", "A bank holiday."])],
  [DT(D, "Quel jour est Thanksgiving ?", ["Le 4e jeudi de novembre", "Le 25 décembre", "Le 4 juillet", "Le 1er lundi de septembre"]),
   DT(D, "Comment dit-on « une réduction » ?", ["A discount", "A reduction tax", "A receipt", "A refund"]),
   DT(D, "Comment dit-on « la caisse » (dans un magasin britannique) ?", ["The till", "The bill", "The box", "The tip"]),
   DT(D, "Comment dit-on « d'occasion » ?", ["Second-hand", "Old-hand", "Re-new", "Half-price"])],
  [W(D, "Trouve le mot qui veut dire « font la queue ».", "queue"), W(D, "Trouve le mot qui veut dire « en ligne ».", "online"),
   W(D, "Trouve le mot qui veut dire « l'étiquette ».", ["label", "the label"]), W(D, "Trouve le mot qui veut dire « boutiques caritatives » (2 mots).", ["charity shops"])])

# ═════════ TRAVAIL (CAP) ═════════
F = "cu_travail.html"
DZ(F, """
## Trouver un emploi
Pour postuler, on envoie un **CV** (britannique) ou un **résumé** (américain), souvent avec une **cover letter** (lettre de motivation). Dans les pays anglophones, le CV ne comporte généralement pas de photo, ni l'âge, ni la situation familiale, pour éviter les discriminations. Pendant l'**interview** (entretien d'embauche), on attend du candidat qu'il « se vende », qu'il donne des exemples concrets, qu'il pose des questions et qu'il remercie ensuite par e-mail. Les **references** (personnes pouvant recommander le candidat) ont une grande importance.

## Les petits boulots des jeunes
Dans les pays anglophones, il est très courant que les adolescents travaillent : **babysitting**, **paper round** (distribution de journaux) au Royaume-Uni, **Saturday job** dans un magasin, **summer job** aux États-Unis dans un fast-food, un parc d'attractions ou un camp de vacances, tonte de pelouses (**mowing lawns**). Beaucoup d'étudiants travaillent pour payer leurs études, qui coûtent cher.

## Contrats et temps de travail
Aux États-Unis, la plupart des emplois sont **at-will** : l'employeur peut licencier le salarié à tout moment, sans motif particulier (sauf discrimination), et le salarié peut partir quand il veut. Il n'existe aucune obligation légale fédérale de congés payés : beaucoup de salariés n'ont qu'une dizaine de jours par an, et certains aucun. Le congé maternité payé n'est pas garanti au niveau fédéral.
Au Royaume-Uni, les salariés à temps plein ont droit à 28 jours de congés payés par an (jours fériés compris). Le pays est connu pour ses **zero-hour contracts** (contrats « zéro heure »), où l'employeur n'est pas obligé de fournir un nombre minimum d'heures : flexibles pour certains, précaires pour d'autres. Dans les deux pays, la semaine de travail standard tourne autour de 40 heures, de **9 to 5**.

## Le salaire minimum
- Aux États-Unis, le salaire minimum fédéral est de **7,25 dollars** de l'heure, inchangé depuis 2009, mais de nombreux États et villes fixent un minimum bien plus élevé. Le mouvement **Fight for $15** a milité pour un salaire minimum de 15 dollars.
- Au Royaume-Uni, le **National Living Wage** dépasse 12 livres de l'heure pour les adultes, avec des taux plus faibles pour les plus jeunes et les apprentis.

## Le pourboire
Aux États-Unis, le **tip** (pourboire) n'est pas facultatif dans les restaurants : on laisse généralement 15 à 20 % de l'addition, car les serveurs ont un salaire de base très bas (le minimum fédéral pour les métiers à pourboires n'est que de 2,13 dollars de l'heure, l'employeur devant compléter si les pourboires ne suffisent pas) et vivent en grande partie des pourboires. On en laisse aussi aux chauffeurs de taxi, coiffeurs, livreurs… Au Royaume-Uni, le pourboire est plus modeste, autour de 10 %, et souvent déjà inclus dans l'addition (**service charge**).

## Les relations au travail
On s'appelle souvent par le prénom, même avec son chef. Les réunions commencent par un peu de **small talk**, et l'on évite les critiques trop directes. Aux États-Unis, l'**entrepreneurship** et la réussite individuelle sont très valorisés ; changer souvent d'emploi ou de ville pour progresser est fréquent.
""", """
a job = un emploi
a boss = un patron
a wage = un salaire (horaire)
a contract = un contrat
a holiday = des vacances, un congé
a tip = un pourboire
an interview = un entretien
a waiter = un serveur
""", [
 ("Qu'est-ce qu'une cover letter ?", ["Une lettre de motivation", "Un contrat de travail", "Une fiche de paie"], ""),
 ("Qu'est-ce qui ne figure généralement pas sur un CV anglophone ?", ["La photo, l'âge et la situation familiale", "L'expérience", "Les diplômes"], ""),
 ("Que signifie un emploi « at-will » aux États-Unis ?", ["L'employeur peut licencier à tout moment, sans motif particulier", "On travaille quand on veut", "On ne peut jamais être licencié"], ""),
 ("Qu'est-ce qu'un zero-hour contract ?", ["Un contrat sans nombre minimum d'heures garanti", "Un contrat sans salaire", "Un stage"], ""),
 ("Combien laisse-t-on de pourboire au restaurant aux États-Unis ?", ["Généralement 15 à 20 %", "Rien", "50 %"], ""),
 ("Pourquoi le pourboire est-il si important aux États-Unis ?", ["Le salaire de base des serveurs est très bas", "C'est la loi de tous les pays", "Pour payer les impôts"], ""),
], [("Fight for $15", "mouvement pour un salaire minimum de 15 dollars")])
D = "wk"
culture(F, "Culture : The world of work", 'The world <span>of work</span>',
  "Culture · CV, petits boulots, contrats, salaires et pourboires", ("#bae6fd", "#334155"),
  reperes("Le monde du travail fonctionne différemment aux États-Unis, au Royaume-Uni et en France : contrats, congés, salaires et pourboires.",
    [("7,25 $", "salaire minimum fédéral américain, inchangé depuis 2009"), ("15 à 20 %", "pourboire habituel au restaurant aux États-Unis"),
     ("28 jours", "congés payés légaux au Royaume-Uni"), ("0 jour", "congés payés imposés par la loi fédérale américaine"), ("9 to 5", "les horaires de bureau classiques")],
    "a CV / a résumé, a cover letter, a job interview, a wage, a contract, a tip, to hire, to fire"),
  {D: doc("Nine to five", [
    "To find a job, you send a CV (or a \"résumé\" in the USA) and a cover letter. In English-speaking countries, you usually do not put a photo or your age on your CV.",
    "Many teenagers have small jobs: babysitting, delivering newspapers, working in a shop on Saturdays or in a fast-food restaurant in the summer.",
    "In the USA, most workers can be fired at any time. There is no national law for paid holidays, so many Americans only have about ten days off a year. In the UK, full-time workers have 28 days of paid holiday.",
    "The minimum wage in the USA is $7.25 an hour, but many states pay more. In the UK, it is more than £12 an hour for adults.",
    "In American restaurants, you must leave a tip of 15 to 20%, because waiters earn a very low wage. In the UK, people usually leave about 10%."])},
  [TF(D, "In English-speaking countries, you usually put a photo on your CV.", False, "« you usually do not put a photo »."),
   TF(D, "Many teenagers have small jobs.", True, "« Many teenagers have small jobs »."),
   TF(D, "In the USA, there is a national law for paid holidays.", False, "« There is no national law »."),
   TF(D, "Full-time workers in the UK have 28 days of paid holiday.", True, "« 28 days of paid holiday »."),
   TF(D, "The minimum wage in the USA is $7.25 an hour.", True, "« $7.25 an hour »."),
   TF(D, "In American restaurants, tips are not necessary.", False, "« you must leave a tip »." )],
  [Q(D, "What do Americans call a CV?", ["A résumé.", "A letter.", "A contract."]),
   Q(D, "Name a typical job for teenagers.", ["Babysitting.", "Doctor.", "Pilot."]),
   Q(D, "How many days off do many Americans have?", ["About ten days a year.", "Two months.", "28 days."]),
   Q(D, "Why must you leave a tip in American restaurants?", ["Because waiters earn a very low wage.", "Because food is free.", "Because it is a gift for the cook."])],
  [DT(D, "Comment dit-on « un entretien d'embauche » ?", ["A job interview", "A job meeting", "A work talk", "A hiring date"]),
   DT(D, "Comment dit-on « licencier » (familier) ?", ["To fire", "To hire", "To tip", "To quit"]),
   DT(D, "Comment appelle-t-on un contrat sans heures garanties au Royaume-Uni ?", ["A zero-hour contract", "A part-time job", "A summer job", "A full-time job"]),
   DT(D, "Quel est le pourboire habituel au Royaume-Uni ?", ["Environ 10 %", "Environ 25 %", "Rien du tout", "50 %"])],
  [W(D, "Trouve le mot qui veut dire « une lettre de motivation » (2 mots).", ["cover letter", "a cover letter"]), W(D, "Trouve le mot qui veut dire « licenciés ».", "fired"),
   W(D, "Trouve le mot qui veut dire « salaire (horaire) ».", "wage"), W(D, "Trouve le mot qui veut dire « gagnent ».", "earn")])
END()
