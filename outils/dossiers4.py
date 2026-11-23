import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
D_ = {}

D_["cu_guerre_secession.html"] = """
## Deux pays dans un seul
En 1860, les États-Unis forment en réalité deux sociétés très différentes. Le **North** s'industrialise : usines, banques, grandes villes, immigrants européens, agriculture de petites fermes familiales. Le **South** est rural : une petite élite de planteurs possède d'immenses plantations de coton cultivées par près de 4 millions d'esclaves. Le coton est la première exportation du pays et part vers les usines textiles britanniques.
Le conflit porte d'abord sur l'extension de l'esclavage dans les nouveaux territoires de l'Ouest. Quand Abraham Lincoln est élu en 1860, les États du Sud estiment que leur mode de vie est menacé et font sécession.

## Lincoln contre Davis
- **Abraham Lincoln**, né dans une cabane en bois du Kentucky, avocat autodidacte, républicain. Son but premier : sauver l'**Union**. Il finit par faire de l'abolition de l'esclavage un objectif de guerre. Il est réputé pour son éloquence et sa capacité à tenir le pays uni malgré les défaites.
- **Jefferson Davis**, riche planteur du Mississippi, ancien officier et ministre de la Guerre, devient président de la **Confederacy**. Il défend les droits des États (**states' rights**) et l'esclavage. Autoritaire et souvent en conflit avec ses généraux et les gouverneurs, il dirige un pays où chaque État tient à son indépendance.
Ironie de l'histoire : les deux hommes sont nés dans le Kentucky, à moins de 200 kilomètres l'un de l'autre.

## Le poids de l'industrie
Le Nord a tous les atouts : plus de deux fois plus d'habitants, plus de 90 % de la production industrielle, l'essentiel des usines d'armes, deux fois plus de voies ferrées, le réseau télégraphique, une marine de guerre. Les **railroads** transportent rapidement troupes et ravitaillement ; le **telegraph** permet à Lincoln de suivre les batailles presque en direct depuis Washington. La guerre de Sécession est souvent considérée comme la première guerre industrielle moderne : fusils plus précis, photographie de guerre, ballons d'observation, et même un premier sous-marin, le *H. L. Hunley*, côté sudiste.
Le Sud compte sur la qualité de ses généraux, comme **Robert E. Lee**, sur la défense de son territoire, et sur le « roi coton » : il espère que le Royaume-Uni et la France interviendront pour protéger leur approvisionnement. Ils ne le feront jamais, notamment parce que l'opinion européenne rejette l'esclavage.

## Le duel des cuirassés
Le Sud récupère une frégate du Nord coulée dans un port de Virginie, le **Merrimack**, et la transforme en navire blindé de plaques de fer : le **CSS Virginia**. Le Nord réplique avec l'**USS Monitor**, un navire bas sur l'eau, surmonté d'une tourelle pivotante, conçu par l'ingénieur John Ericsson. Le 8 mars 1862, à **Hampton Roads**, la Virginia coule deux navires de bois de l'Union. Le lendemain, le Monitor arrive : les deux **ironclads** se canonnent pendant des heures sans pouvoir se percer. Match nul, mais révolution navale : toutes les marines du monde comprennent que les navires en bois sont dépassés.

## L'étouffement du Sud
Dès 1861, le général Winfield Scott propose l'**Anaconda Plan** : comme un serpent qui étouffe sa proie, la marine de l'Union impose un **blockade** des ports du Sud et prend le contrôle du Mississippi pour couper la Confédération en deux. Le coton ne peut plus être exporté, les armes et les médicaments importés se raréfient, l'inflation explose : le pain devient hors de prix dans les villes du Sud, où éclatent même des émeutes de la faim.
En juillet 1863, deux victoires changent tout : **Gettysburg**, où l'invasion du Nord par Lee est stoppée, et **Vicksburg**, qui donne le Mississippi à l'Union. Le général **Ulysses S. Grant** mène ensuite une guerre d'usure contre Lee en Virginie, tandis que **William T. Sherman** prend Atlanta puis mène sa **March to the Sea** à travers la Géorgie (novembre-décembre 1864), détruisant voies ferrées, fermes, entrepôts et usines : c'est une guerre totale, qui vise l'économie et le moral du Sud.

## La fin
Affamée, encerclée, moins nombreuse, l'armée de Lee capitule à **Appomattox** le 9 avril 1865. Grant laisse les soldats sudistes rentrer chez eux avec leurs chevaux. Cinq jours plus tard, Lincoln est assassiné au théâtre par un sympathisant sudiste. Jefferson Davis, capturé en mai, passe deux ans en prison mais n'est jamais jugé. Le bilan est terrible : plus de 600 000 soldats morts, un Sud ravagé, mais une Union préservée et l'esclavage aboli par le 13e amendement.
"""

D_["cu_amerindiens_societe.html"] = """
## Qui sont les Amérindiens aujourd'hui ?
Lors du recensement de 2020, près de 10 millions d'Américains se sont déclarés amérindiens ou autochtones d'Alaska, seuls ou avec d'autres origines, soit environ 3 % de la population. Il existe plus de 570 **tribal nations** reconnues par l'État fédéral, et d'autres qui ne le sont pas. Chaque nation a sa langue, son histoire, ses règles d'appartenance. Il n'y a donc pas « un » peuple amérindien, mais des centaines.

## Les réserves
On compte environ 326 **reservations**. La plus grande, la **Navajo Nation**, s'étend sur l'Arizona, l'Utah et le Nouveau-Mexique ; elle est plus grande que plusieurs États américains. Les tribus y exercent une forme de **sovereignty** : elles ont leur gouvernement, leur police, leurs tribunaux. Mais la terre est souvent pauvre et isolée, héritage des déplacements forcés du 19e siècle.
La pauvreté y est beaucoup plus élevée que la moyenne nationale, le chômage aussi. Une partie des foyers de la Navajo Nation vit encore sans eau courante ni électricité. Les routes, Internet et les services publics manquent. Pourtant, environ 7 Amérindiens sur 10 vivent aujourd'hui hors des réserves, souvent en ville, où ils sont parfois encore plus invisibles.

## Une santé fragile
Les Amérindiens ont l'espérance de vie la plus faible de tous les groupes de la population américaine : environ 70 ans, contre 78 ans en moyenne selon des données récentes. Ils sont particulièrement touchés par l'**obesity** et le **type 2 diabetes** : la mortalité due au diabète y est environ trois fois plus élevée que dans le reste du pays. On observe aussi des taux élevés de maladies cardiaques, d'addictions et de suicides, notamment chez les jeunes.

## Pourquoi ?
Les spécialistes insistent sur plusieurs causes, qui s'additionnent :
- la **poverty**, qui oblige à acheter la nourriture la moins chère ;
- les **food deserts** : dans beaucoup de zones isolées, le seul magasin propose surtout des produits industriels et des sodas, tandis que les fruits et légumes frais sont rares et chers ;
- la perte des modes de vie et d'alimentation traditionnels (chasse, pêche, cueillette, agriculture), après la perte des terres ;
- l'histoire de l'aide alimentaire : pendant des décennies, le gouvernement a distribué des **commodity foods** (farine blanche, sucre, saindoux, viande en conserve). Le **frybread**, galette frite devenue plat populaire, en est né ; certains y voient un symbole culturel, d'autres le symbole d'un régime alimentaire imposé ;
- le **historical trauma** : les violences, les déportations et les pensionnats ont laissé des traces sur plusieurs générations ;
- un système de santé insuffisant : l'**Indian Health Service** (IHS), créé en 1955, est régulièrement critiqué pour son manque de moyens et de personnel.

## Des raisons d'espérer
Beaucoup de tribus réagissent. Des programmes remettent à l'honneur les aliments traditionnels (maïs, haricots, courges, bison), les jardins communautaires, la course à pied et les sports traditionnels. Les **tribal colleges** enseignent les langues autochtones. Certaines tribus investissent les revenus de leurs casinos dans des écoles, des cliniques et des maisons de retraite.
La culture amérindienne est aussi plus visible que jamais : la série *Reservation Dogs* (2021-2023), écrite et jouée par des Amérindiens, raconte avec humour la vie d'adolescents dans une réserve de l'Oklahoma ; l'actrice **Lily Gladstone** a reçu un Golden Globe en 2024 ; des Amérindiennes siègent au Congrès. Les jeunes militent aussi contre les clichés (plumes, tipis, mascottes sportives) et rappellent une évidence : les Amérindiens ne sont pas un peuple du passé, mais des citoyens du présent.
"""

D_["cu_alaska.html"] = """
## Un territoire immense
L'**Alaska** est de loin le plus grand État américain : plus de deux fois le Texas, environ trois fois la France. Mais il ne compte qu'environ 730 000 habitants. Sa capitale, **Juneau**, n'est accessible qu'en avion ou en bateau ; la plus grande ville est **Anchorage**. Le détroit de Béring le sépare de la Russie : à certains endroits, seulement 4 kilomètres séparent une île américaine d'une île russe. On le surnomme **The Last Frontier**, la dernière frontière.

## Les premiers habitants
L'Alaska est peuplé depuis plus de 10 000 ans. C'est par là que les premiers humains seraient arrivés en Amérique, en traversant un pont de terre qui reliait l'Asie à l'Amérique pendant la dernière glaciation. Aujourd'hui, les **Alaska Natives** représentent environ 15 % de la population : Inupiat et Yupik sur les côtes arctiques et de l'Ouest, Athabascans à l'intérieur, Tlingit et Haïdas au sud-est, célèbres pour leurs mâts totémiques.

## De la Russie aux États-Unis
Au 18e siècle, des marchands russes s'installent pour chasser la loutre de mer, dont la fourrure se vend très cher en Chine. Mais la colonie coûte cher et la Russie, affaiblie après la guerre de Crimée, préfère la vendre plutôt que de la voir prise par les Britanniques. En 1867, les États-Unis l'achètent pour 7,2 millions de dollars, environ deux centimes l'acre. Beaucoup d'Américains se moquent de cet achat d'une « glacière » et l'appellent **Seward's Folly**.
L'histoire leur donne tort. À la fin des années 1890, la ruée vers l'or du Klondike, au Canada voisin, puis celle de Nome attirent des dizaines de milliers de chercheurs d'or. L'écrivain Jack London en tire des romans comme *The Call of the Wild*. Pendant la Seconde Guerre mondiale, le Japon occupe même deux îles de l'archipel des Aléoutiennes. L'Alaska devient le 49e État en 1959.

## L'or noir
En 1968, on découvre un gigantesque gisement de pétrole à **Prudhoe Bay**, sur la côte arctique. Un oléoduc de près de 1 300 kilomètres, le **Trans-Alaska Pipeline**, est construit pour acheminer le pétrole jusqu'au port de Valdez, au sud. Le pétrole enrichit l'État : depuis 1982, chaque habitant reçoit chaque année un chèque du **Permanent Fund**, un fonds alimenté par les revenus pétroliers. L'Alaska n'a pas d'impôt sur le revenu au niveau de l'État.
Mais le pétrole a un prix. En 1989, le pétrolier **Exxon Valdez** s'échoue sur un récif et déverse des dizaines de millions de litres de pétrole ; des centaines de milliers d'oiseaux et des milliers de loutres meurent. Le débat entre exploitation pétrolière et protection de la nature, notamment dans le refuge arctique national, reste brûlant.

## Une nature extrême
Glaciers, volcans, ours bruns et grizzlis, orignaux, baleines, saumons… Le **Denali**, 6 190 mètres, est le plus haut sommet d'Amérique du Nord. Au-delà du cercle polaire, le soleil ne se couche pas en été et ne se lève pas pendant des semaines en hiver ; on peut y admirer les **northern lights**. Chaque mois de mars, l'**Iditarod**, une course de chiens de traîneau de plus de 1 500 kilomètres, traverse l'État ; elle commémore une course de relais qui apporta un sérum contre la diphtérie à Nome en 1925.

## En première ligne du changement climatique
L'Alaska se réchauffe environ deux fois plus vite que la moyenne mondiale. Le **permafrost**, le sol gelé en permanence, dégèle : les routes et les maisons s'affaissent, les côtes s'érodent. La banquise, indispensable à la chasse traditionnelle, recule. Certains villages autochtones, comme Newtok, ont dû être déplacés : leurs habitants sont parmi les premiers **climate refugees** des États-Unis.
"""

D_["cu_lgbt.html"] = """
## Que signifie LGBTQ+ ?
Le sigle désigne les personnes **lesbian** (femmes attirées par les femmes), **gay** (hommes attirés par les hommes, ou plus largement personnes homosexuelles), **bisexual** (attirées par plusieurs genres), **transgender** (dont l'identité de genre ne correspond pas au sexe attribué à la naissance), **queer** (terme parapluie, autrefois insulte, aujourd'hui revendiqué), et le « + » pour toutes les autres identités. On parle de **coming out** quand une personne révèle son orientation ou son identité à son entourage.

## Un long passé de répression
Au Royaume-Uni, les relations entre hommes sont punies de mort jusqu'en 1861, puis de prison. En 1895, l'écrivain **Oscar Wilde**, au sommet de sa gloire, est condamné à deux ans de travaux forcés ; il meurt ruiné à Paris en 1900. En 1952, le mathématicien Alan Turing est condamné à son tour. Aux États-Unis, dans les années 1950, des milliers de fonctionnaires sont licenciés parce qu'ils sont homosexuels : on parle de **Lavender Scare**. L'homosexualité est alors considérée comme une maladie mentale par les médecins américains, jusqu'en 1973.

## Les premières victoires
En 1967, le **Sexual Offences Act** dépénalise l'homosexualité masculine en Angleterre et au pays de Galles (en 1980 en Écosse, en 1982 en Irlande du Nord), mais sous conditions et avec un âge de consentement différent. Aux États-Unis, les lois varient selon les États ; la Cour suprême n'annule les dernières lois pénalisant l'homosexualité qu'en 2003.

## Stonewall et la naissance des Pride
Dans la nuit du 28 juin 1969, la police fait une descente au **Stonewall Inn**, un bar gay de New York. Pour la première fois, les clients résistent ; parmi eux, des personnes trans et des personnes noires et latinas, comme Marsha P. Johnson. Plusieurs nuits d'émeutes suivent. Un an plus tard, les premières **Pride marches** commémorent l'événement. Aujourd'hui, juin est le **Pride Month** dans le monde entier. En 1978, l'artiste **Gilbert Baker** crée le drapeau arc-en-ciel, devenu le symbole du mouvement.
En 1977, **Harvey Milk** est élu au conseil municipal de San Francisco, l'un des premiers élus ouvertement gays du pays. Il est assassiné l'année suivante, avec le maire de la ville, par un ancien collègue.

## Les années sida
Dans les années 1980, l'épidémie de **AIDS** (sida) frappe durement les hommes gays. Les gouvernements réagissent lentement, et la maladie renforce les préjugés : certains journaux parlent de « peste gay ». Des militants, comme ceux du groupe ACT UP, se battent pour obtenir des recherches et des traitements. Au Royaume-Uni, la loi **Section 28** (1988-2003) interdit même aux écoles de « promouvoir » l'homosexualité, empêchant les enseignants d'en parler. Aux États-Unis, la règle « **Don't Ask, Don't Tell** » (1993-2011) oblige les militaires homosexuels à cacher leur orientation.

## Vers l'égalité
Les lois changent à partir des années 2000. Au Royaume-Uni, le **civil partnership** est créé en 2005, puis le mariage est ouvert aux couples de même sexe en 2014 (en 2020 en Irlande du Nord). En 2015, l'Irlande devient le premier pays à l'approuver par référendum, et le 26 juin 2015, la Cour suprême américaine le légalise dans tous les États avec l'arrêt *Obergefell v. Hodges*. En 2013, la reine accorde une grâce posthume à Alan Turing ; en 2017, une loi, surnommée « loi Turing », gracie des dizaines de milliers d'hommes condamnés pour homosexualité.

## Et aujourd'hui ?
Les personnes LGBTQ+ ont aujourd'hui des droits inédits au Royaume-Uni et aux États-Unis, mais l'égalité n'est pas complète. Les insultes, le harcèlement scolaire et les violences existent toujours. Les droits des personnes **transgender** font l'objet de débats politiques intenses dans les deux pays, notamment sur l'accès aux soins, le sport ou l'école ; les opinions y sont très divisées. Partout, des associations et des **allies**, des personnes qui soutiennent sans forcément être concernées, luttent contre l'**homophobia** et la **transphobia**.
"""
