import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
exec(open(_EA_OUT+"/cuhelp.py", encoding="utf-8").read())

# ═════════ FAST FOOD ═════════
F = "cu_fast_food.html"
DZ(F, """
## La naissance du fast-food
En 1940, les frères Richard et Maurice **McDonald** ouvrent un restaurant à San Bernardino, en Californie. En 1948, ils réorganisent leur cuisine comme une usine : menu réduit, préparation à la chaîne, service en quelques secondes, sans couverts ni assiettes. Un vendeur de machines à milkshakes, **Ray Kroc**, comprend le potentiel du concept : à partir de 1955, il développe la marque en **franchise** dans tout le pays, puis rachète l'entreprise. D'autres chaînes suivent : Burger King, KFC, Pizza Hut, Subway… Le **drive-through** permet de commander sans sortir de sa voiture, en phase avec la culture automobile américaine.

## Toujours plus gros
Au fil des décennies, les portions grossissent : sodas d'un litre, menus « super size », assiettes immenses dans les restaurants. Les aliments **ultra-processed** (industriels), riches en sucre, en sel et en graisses, sont bon marché et omniprésents. En 2004, le documentaire *Super Size Me* montre un réalisateur qui ne mange que chez McDonald's pendant un mois et voit sa santé se dégrader ; la chaîne supprime ensuite son format « Super Size ».

## L'obésité, un problème de santé publique
Selon les données de santé publique, environ 40 % des adultes américains sont obèses. L'obésité augmente les risques de diabète, de maladies cardiaques (**heart attack**), d'hypertension et de certains cancers. Les causes sont multiples : alimentation industrielle bon marché, boissons sucrées, dépendance à la voiture et sédentarité, manque de temps pour cuisiner, et **food deserts**, ces quartiers pauvres où il est difficile d'acheter des produits frais. L'obésité touche plus fortement les populations pauvres et certaines minorités.

## Le Heart Attack Grill, la provocation
À l'extrême, le **Heart Attack Grill**, fondé en 2005 en Arizona par **Jon Basso** puis installé à Las Vegas, a fait de la malbouffe un spectacle : serveuses déguisées en infirmières, clients en blouse d'hôpital, hamburgers appelés « Quadruple Bypass Burger » (près de 10 000 calories), repas gratuits pour les clients de plus de 350 livres (environ 160 kg), et sortie en fauteuil roulant pour ceux qui ne terminent pas leur assiette. Son propriétaire, qui se fait appeler « Dr. Jon », prétendait choquer pour faire réfléchir. Mais des clients ont été victimes de crises cardiaques sur place, et le restaurant a été vivement critiqué par des médecins pour avoir glorifié l'obésité. Son restaurant de Las Vegas a fermé en mai 2026 ; son propriétaire dit vouloir le rouvrir ailleurs.

## La vague du « healthy food »
En réaction, une partie des Américains se tourne vers une alimentation plus saine : marchés de producteurs (**farmers' markets**), produits **organic** (bio), régimes végétariens et **vegan**, **superfoods**, salades et bols « healthy ». En 2010, **Michelle Obama** lance la campagne *Let's Move!* contre l'obésité des enfants et plante un potager à la Maison-Blanche ; une loi améliore la qualité des repas des cantines. Les chaînes affichent désormais les calories sur leurs menus. Mais manger sainement reste souvent plus cher : la **healthy food** est parfois un marqueur social, réservé à ceux qui en ont les moyens.
""", """
a burger = un hamburger
fries = les frites
a soda = un soda
fat = la graisse, gros
sugar = le sucre
healthy = sain
a vegetable = un légume
a heart attack = une crise cardiaque
""", [
 ("Qui ont fondé McDonald's ?", ["Les frères McDonald, en 1940", "Ray Kroc seul", "Henry Ford"], "Ray Kroc l'a ensuite développé en franchise."),
 ("Qu'est-ce qu'un drive-through ?", ["Un service où l'on commande sans sortir de sa voiture", "Une autoroute", "Un restaurant de luxe"], ""),
 ("Que montre le film Super Size Me ?", ["Les effets sur la santé d'un mois de repas chez McDonald's", "La vie d'un cow-boy", "La construction d'un restaurant"], ""),
 ("Environ quelle part des adultes américains est obèse ?", ["Environ 40 %", "Environ 4 %", "Environ 90 %"], ""),
 ("Qu'est-ce que le Heart Attack Grill ?", ["Un restaurant provocateur qui glorifiait la malbouffe", "Un hôpital", "Une salle de sport"], ""),
 ("Pourquoi la healthy food peut-elle être un marqueur social ?", ["Manger sainement coûte souvent plus cher", "Elle est interdite aux pauvres", "Elle n'existe qu'en Europe"], ""),
], [("**Ray Kroc**", "homme d'affaires américain"), ("*Super Size Me*", "documentaire de Morgan Spurlock"), ("**Jon Basso**", "ancien professionnel du fitness"), ("**Michelle Obama**", "épouse du président Barack Obama")])
D = "ff"
culture(F, "Culture : Fast food, obesity and healthy food", 'Fast food <span>&amp; healthy food</span>',
  "Culture · McDonald's, obésité, Heart Attack Grill et retour au « healthy »", ("#fca5a5", "#ca8a04"),
  reperes("Le fast-food est né aux États-Unis. Aujourd'hui, l'obésité y est un grand problème de santé publique, et une partie des Américains se tourne vers une alimentation plus saine.",
    [("1940", "les frères McDonald ouvrent leur restaurant en Californie"), ("1955", "Ray Kroc lance la franchise McDonald's"), ("2004", "le documentaire Super Size Me"),
     ("2005", "création du Heart Attack Grill"), ("2010", "campagne Let's Move! de Michelle Obama"), ("environ 40 %", "des adultes américains sont obèses")],
    "fast food, a portion, junk food, obesity, a heart attack, healthy, organic, a farmers' market"),
  {D: doc("Supersize or salad?", [
    "Fast food was born in the USA. In 1940, the McDonald brothers opened a restaurant in California. They served burgers and fries very quickly, like in a factory. Today, fast-food chains are everywhere in the world.",
    "Fast food is cheap and practical, but it often contains a lot of fat, sugar and salt. Portions have become bigger and bigger. In 2004, the film Super Size Me showed a man who ate only McDonald's food for a month: his health became much worse.",
    "Today, about 40% of American adults are obese. Obesity can cause diabetes and heart attacks. The reasons include cheap junk food, sugary drinks, using the car everywhere, and \"food deserts\", poor areas where it is hard to buy fresh food.",
    "Some restaurants even made fun of it. The Heart Attack Grill, in Las Vegas, served enormous burgers with names like the \"Quadruple Bypass Burger\". Its waitresses were dressed as nurses. Some customers really had heart attacks there, and doctors criticised it a lot. Its Las Vegas restaurant closed in 2026.",
    "But many Americans now prefer healthy food: salads, organic products, vegetables from farmers' markets, vegan dishes. In 2010, Michelle Obama started a campaign against childhood obesity. However, healthy food is often more expensive."])},
  [TF(D, "Fast food was born in the USA.", True, "« Fast food was born in the USA »."),
   TF(D, "Fast food usually contains little fat and sugar.", False, "« a lot of fat, sugar and salt »."),
   TF(D, "Portions have become smaller.", False, "« bigger and bigger »."),
   TF(D, "About 40% of American adults are obese.", True, "« about 40% »."),
   TF(D, "The Heart Attack Grill served healthy salads.", False, "Des hamburgers énormes."),
   TF(D, "Healthy food is often more expensive.", True, "« often more expensive »." )],
  [Q(D, "How did the McDonald brothers serve food?", ["Very quickly, like in a factory.", "Slowly, like in a French restaurant.", "Only at night."]),
   Q(D, "What did Super Size Me show?", ["Eating only fast food for a month damaged a man's health.", "How to cook burgers.", "The history of Las Vegas."]),
   Q(D, "What is a food desert?", ["A poor area where it is hard to buy fresh food.", "A restaurant in the desert.", "A dessert."]),
   Q(D, "Why was the Heart Attack Grill criticised?", ["It glorified unhealthy food.", "It was too expensive.", "It was too small."]),
   Q(D, "What did Michelle Obama do in 2010?", ["She started a campaign against childhood obesity.", "She opened a fast-food chain.", "She became President."])],
  [DT(D, "Qui a développé McDonald's en franchise ?", ["Ray Kroc", "Jon Basso", "Henry Ford", "Walt Disney"]),
   DT(D, "Dans quelle ville se trouvait le Heart Attack Grill ?", ["Las Vegas", "New York", "Chicago", "Miami"]),
   DT(D, "Comment s'appelle la campagne de Michelle Obama ?", ["Let's Move!", "Super Size Me", "Yes We Can", "Eat Fresh"]),
   DT(D, "Comment dit-on « bio » en anglais ?", ["Organic", "Biologic", "Natural fresh", "Healthy food"])],
  [W(D, "Trouve le mot qui veut dire « chaînes » (de restaurants).", "chains"), W(D, "Trouve le mot qui veut dire « malbouffe » (2 mots).", ["junk food"]),
   W(D, "Trouve le mot qui veut dire « infirmières ».", "nurses"), W(D, "Trouve le mot qui veut dire « obésité infantile » (2 mots).", ["childhood obesity"])])

# ═════════ BLM ═════════
F = "cu_blm.html"
DZ(F, """
## Un slogan né en 2013
En février 2012, en Floride, **Trayvon Martin**, un adolescent noir de 17 ans non armé, est tué par George Zimmerman, membre d'une patrouille de voisinage. L'acquittement de Zimmerman en 2013 provoque une vague d'indignation. Trois militantes, **Alicia Garza**, **Patrisse Cullors** et **Opal Tometi**, lancent alors sur les réseaux sociaux le slogan **#BlackLivesMatter** (« les vies noires comptent »).

## Ferguson
En août 2014, à **Ferguson**, dans le Missouri, **Michael Brown**, 18 ans, est tué par un policier. Des manifestations et des émeutes éclatent pendant des semaines. Le mouvement Black Lives Matter devient national. D'autres morts suscitent la colère, comme celle d'Eric Garner à New York en 2014, dont les mots « *I can't breathe* » deviennent un cri de ralliement.

## George Floyd, mai 2020
Le **25 mai 2020**, à **Minneapolis**, **George Floyd**, un homme noir de 46 ans soupçonné d'avoir utilisé un faux billet de 20 dollars, est plaqué au sol par des policiers. L'agent **Derek Chauvin** maintient son genou sur son cou pendant plus de neuf minutes, alors que Floyd répète qu'il ne peut pas respirer. Il meurt. La scène est filmée par une adolescente, **Darnella Frazier**, avec son téléphone. La vidéo bouleverse le monde.

## Des manifestations historiques
En pleine pandémie de Covid-19, des millions d'Américains manifestent dans tout le pays : ce sont parmi les plus grandes mobilisations de l'histoire des États-Unis. Des rassemblements ont lieu aussi à Londres, Paris, Berlin, Sydney… Des statues liées à l'esclavage ou à la colonisation sont déboulonnées, comme celle du marchand d'esclaves Edward Colston à Bristol. Des entreprises, des clubs sportifs et des célébrités affichent leur soutien ; des joueurs posent un genou à terre (**take the knee**) avant les matchs. En avril 2021, Derek Chauvin est reconnu coupable de meurtre.

## Les inégalités raciales
Le mouvement dénonce les **police brutality**, mais aussi le **systemic racism**, le racisme inscrit dans le fonctionnement des institutions : à population égale, les Noirs américains sont plus souvent tués par la police, plus souvent incarcérés, et possèdent en moyenne bien moins de patrimoine que les Blancs, héritage de l'esclavage et de la ségrégation.

## Les débats
Black Lives Matter divise aussi la société américaine. Ses partisans réclament une réforme de la police ; certains vont jusqu'à demander de réduire ses budgets (« **defund the police** »), une idée controversée même parmi les sympathisants. Ses critiques répondent par le slogan « *All Lives Matter* », jugent certaines manifestations violentes et défendent le travail des policiers (« *Blue Lives Matter* »). Le débat sur la police, la justice et le racisme reste au cœur de la vie politique américaine.
""", """
the police = la police
a protest = une manifestation
justice = la justice
racism = le racisme
equality = l'égalité
a video = une vidéo
a statue = une statue
a life = une vie
""", [
 ("Quand et pourquoi le slogan #BlackLivesMatter est-il lancé ?", ["En 2013, après l'acquittement du meurtrier de Trayvon Martin", "En 1963, après un discours", "En 2020, pour une élection"], ""),
 ("Que se passe-t-il à Ferguson en 2014 ?", ["Michael Brown est tué par un policier et des manifestations éclatent", "Une élection présidentielle", "Un match de football"], ""),
 ("Comment le monde découvre-t-il la mort de George Floyd ?", ["Grâce à la vidéo filmée par une adolescente", "Par un communiqué de police", "Par un film de cinéma"], ""),
 ("Que signifie « take the knee » ?", ["Poser un genou à terre en signe de protestation", "Prier", "Abandonner un match"], ""),
 ("Qu'est-ce que le « systemic racism » ?", ["Un racisme inscrit dans le fonctionnement des institutions", "Un racisme individuel", "Une loi"], ""),
 ("Que répondent les critiques du mouvement ?", ["« All Lives Matter » et la défense des policiers", "Ils sont tous d'accord", "Ils demandent plus de manifestations"], ""),
], [("**Trayvon Martin**", "lycéen de Floride"), ("Edward Colston", "marchand d'esclaves du 17e siècle"), ("Covid-19", "pandémie mondiale à partir de 2020")])
D = "bl"
culture(F, "Culture : Black Lives Matter", 'Black Lives <span>Matter</span>',
  "Culture · George Floyd, la police et le racisme aujourd'hui", ("#d4d4d4", "#ca8a04"),
  reperes("Né en 2013, le mouvement Black Lives Matter dénonce les violences policières et le racisme. Il devient mondial après la mort de George Floyd en 2020.",
    [("2012 – 2013", "mort de Trayvon Martin, naissance du slogan #BlackLivesMatter"), ("2014", "mort de Michael Brown à Ferguson"), ("25 mai 2020", "mort de George Floyd à Minneapolis"),
     ("été 2020", "manifestations historiques aux États-Unis et dans le monde"), ("avril 2021", "le policier Derek Chauvin reconnu coupable de meurtre")],
    "racism, police brutality, a protest, justice, equality, systemic racism, a movement, to take the knee"),
  {D: doc("I can't breathe", [
    "Black Lives Matter is a movement against racism and police violence. It started in 2013 on social media, after the death of Trayvon Martin, a 17-year-old Black teenager killed in Florida.",
    "On 25 May 2020, in Minneapolis, a police officer knelt on the neck of George Floyd, a Black man, for more than nine minutes. George Floyd died. A teenager filmed the scene with her phone, and the video shocked the world.",
    "Millions of people protested in the USA and in many other countries. Some statues linked to slavery were removed. Athletes took the knee before matches to show their support.",
    "In 2021, the police officer, Derek Chauvin, was found guilty of murder. The movement also denounces other inequalities: Black Americans are more often sent to prison and are, on average, poorer.",
    "Not everybody supports the movement. Some people answer \"All Lives Matter\" and defend the police. The debate about police and racism is still very strong in the USA."])},
  [TF(D, "Black Lives Matter started in 2013.", True, "« It started in 2013 »."),
   TF(D, "George Floyd died in New York.", False, "À Minneapolis."),
   TF(D, "A teenager filmed the scene.", True, "« A teenager filmed the scene »."),
   TF(D, "The protests only took place in the USA.", False, "« in many other countries »."),
   TF(D, "Derek Chauvin was found guilty of murder.", True, "« found guilty of murder »."),
   TF(D, "Everybody supports the movement.", False, "« Not everybody supports the movement »." )],
  [Q(D, "What is Black Lives Matter?", ["A movement against racism and police violence.", "A political party.", "A sports team."]),
   Q(D, "How did the world see George Floyd's death?", ["Thanks to a video filmed by a teenager.", "On a police report.", "In a film."]),
   Q(D, "What did athletes do to show their support?", ["They took the knee.", "They stopped playing forever.", "They wore masks."]),
   Q(D, "What do some critics say?", ["\"All Lives Matter\", and they defend the police.", "They agree with everything.", "They want more protests."])],
  [DT(D, "Dans quelle ville meurt George Floyd ?", ["Minneapolis", "Ferguson", "New York", "Chicago"]),
   DT(D, "Où meurt Michael Brown en 2014 ?", ["À Ferguson", "À Minneapolis", "À Dallas", "À Montgomery"]),
   DT(D, "Quelle statue est déboulonnée à Bristol ?", ["Celle du marchand d'esclaves Edward Colston", "Celle de Churchill", "Celle de la reine Victoria", "Celle de Shakespeare"]),
   DT(D, "En quelle année Derek Chauvin est-il condamné ?", ["2021", "2020", "2013", "2014"])],
  [W(D, "Trouve le mot qui veut dire « s'est agenouillé » (sur).", "knelt"), W(D, "Trouve le mot qui veut dire « ont manifesté ».", "protested"),
   W(D, "Trouve le mot qui veut dire « coupable ».", "guilty"), W(D, "Trouve le mot qui veut dire « dénonce ».", "denounces")])

# ═════════ BORDER ═════════
F = "cu_frontiere_mexique.html"
DZ(F, """
## Une frontière de plus de 3 000 km
La frontière entre les États-Unis et le Mexique s'étend sur environ 3 100 kilomètres, du Pacifique au golfe du Mexique, à travers des déserts, des montagnes et le fleuve **Rio Grande**. Elle a été fixée en grande partie après la guerre de 1846-1848, quand le Mexique a perdu la Californie, l'Arizona, le Nouveau-Mexique… Beaucoup de familles hispaniques vivaient donc déjà sur ces terres avant qu'elles ne deviennent américaines : comme on le dit parfois, « *we didn't cross the border, the border crossed us* ».

## Des échanges intenses
C'est l'une des frontières les plus fréquentées du monde : des millions de personnes et de camions la traversent légalement pour travailler, étudier, commercer ou rendre visite à leur famille. Des villes jumelles se font face, comme San Diego et Tijuana, ou El Paso et Ciudad Juárez. Les économies des deux pays sont étroitement liées. Pendant la Seconde Guerre mondiale, le programme **Bracero** a fait venir des millions de travailleurs agricoles mexicains.

## L'immigration clandestine
Chaque année, de nombreuses personnes tentent de franchir la frontière sans autorisation, venant du Mexique mais aussi d'Amérique centrale (Guatemala, Honduras, Salvador), du Venezuela, d'Haïti, ou même d'Afrique et d'Asie. Elles fuient la pauvreté, la violence des gangs, les crises politiques ou climatiques. Beaucoup demandent l'asile (**asylum**). Les passeurs (**smugglers**, ou **coyotes**) font payer très cher la traversée. Des milliers de migrants sont morts dans le désert ou en traversant le Rio Grande.
Aux États-Unis vivent environ 11 millions de personnes **undocumented** (sans papiers), dont beaucoup y sont installées depuis des décennies et travaillent dans l'agriculture, la construction, la restauration. Les **Dreamers** sont des jeunes arrivés enfants, qui ont grandi aux États-Unis ; un programme de 2012, le DACA, les protège temporairement de l'expulsion.

## Le mur
Des barrières existent depuis les années 1990 et 2000. Donald Trump a fait de la construction d'un **border wall** une promesse centrale de ses campagnes. La frontière est aujourd'hui surveillée par des milliers d'agents de la **Border Patrol**, des caméras, des drones et des clôtures sur une partie de sa longueur.

## Un débat qui divise
- Pour les partisans d'un contrôle strict : il faut faire respecter la loi, protéger la sécurité du pays, lutter contre le trafic de drogue (comme le fentanyl) et éviter la pression sur les services publics et les salaires.
- Pour les défenseurs des migrants : l'immigration est une richesse et une tradition américaine, l'économie a besoin de ces travailleurs, le droit d'asile doit être respecté, et le mur est coûteux, inefficace et inhumain.
L'immigration est l'un des sujets les plus explosifs de la politique américaine, et les règles changent souvent selon les gouvernements.

## Une Amérique hispanique
Les **Latinos** représentent environ un Américain sur cinq. L'espagnol est parlé dans des millions de foyers, et la culture mexicaine marque profondément le Sud-Ouest : cuisine **Tex-Mex**, musique, fêtes comme le **Día de los Muertos**, et même le **Spanglish**, mélange d'anglais et d'espagnol.
""", """
a border = une frontière
a wall = un mur
a migrant = un migrant
the desert = le désert
a river = un fleuve
a job = un travail
a family = une famille
the law = la loi
""", [
 ("Quelle est la longueur de la frontière ?", ["Environ 3 100 km", "Environ 300 km", "Environ 30 000 km"], ""),
 ("Que signifie « we didn't cross the border, the border crossed us » ?", ["Des Hispaniques vivaient sur ces terres avant qu'elles deviennent américaines", "Ils ont traversé à la nage", "La frontière bouge chaque année"], ""),
 ("Pourquoi des migrants tentent-ils de franchir la frontière ?", ["Pour fuir la pauvreté, la violence ou des crises", "Pour faire du tourisme", "Pour visiter Disney"], ""),
 ("Qui sont les Dreamers ?", ["De jeunes sans-papiers arrivés enfants aux États-Unis", "Des agents de la Border Patrol", "Des passeurs"], ""),
 ("Quels arguments avancent les partisans d'un contrôle strict ?", ["Faire respecter la loi, la sécurité, la lutte contre la drogue", "L'économie a besoin des migrants", "Le mur est inhumain"], ""),
 ("Quelle part de la population américaine est latino ?", ["Environ un Américain sur cinq", "Presque personne", "La moitié"], ""),
], [("**Rio Grande**", "fleuve qui forme une partie de la frontière"), ("fentanyl", "drogue de synthèse très puissante"), ("**Día de los Muertos**", "fête mexicaine des morts")])
D = "bo"
culture(F, "Culture : The US-Mexico border", 'The US-Mexico <span>border</span>',
  "Culture · immigration, mur et Amérique hispanique", ("#fdba74", "#047857"),
  reperes("La frontière entre les États-Unis et le Mexique est l'une des plus traversées du monde, et l'immigration l'un des sujets les plus débattus aux États-Unis.",
    [("1848", "fin de la guerre contre le Mexique : la frontière est fixée"), ("1942 – 1964", "programme Bracero de travailleurs agricoles"), ("2012", "programme DACA pour les Dreamers"),
     ("environ 3 100 km", "longueur de la frontière"), ("environ 1 sur 5", "part des Latinos dans la population américaine")],
    "a border, a wall, immigration, a migrant, asylum, undocumented, a smuggler, a Latino"),
  {D: doc("Crossing the line", [
    "The border between the USA and Mexico is more than 3,000 kilometres long. Every day, millions of people and trucks cross it legally to work, study or visit their families.",
    "But many migrants also try to cross without permission. They come from Mexico, Central America and other countries. They often run away from poverty or violence. Some ask for asylum. Crossing the desert is very dangerous, and thousands have died.",
    "About 11 million undocumented immigrants live in the USA. Many have lived there for years and work in farms, construction or restaurants. Young people who arrived as children are called \"Dreamers\".",
    "Some Americans want a strict control of the border and a big wall, for security reasons. Others think that immigrants help the economy and that the wall is expensive and inhuman. It is one of the most divisive debates in the USA.",
    "Latinos represent about one in five Americans. Spanish is spoken in millions of homes, and Mexican culture, food and music are part of American life."])},
  [TF(D, "Millions of people cross the border legally.", True, "« cross it legally »."),
   TF(D, "Crossing the desert is safe.", False, "« very dangerous »."),
   TF(D, "Some migrants ask for asylum.", True, "« Some ask for asylum »."),
   TF(D, "Dreamers arrived in the USA as adults.", False, "« arrived as children »."),
   TF(D, "All Americans agree about the wall.", False, "« one of the most divisive debates »."),
   TF(D, "Latinos represent about one in five Americans.", True, "« about one in five »." )],
  [Q(D, "Why do migrants leave their countries?", ["To run away from poverty or violence.", "To go on holiday.", "To learn English."]),
   Q(D, "Where do many undocumented immigrants work?", ["In farms, construction or restaurants.", "In the army.", "In the government."]),
   Q(D, "Why do some Americans want a wall?", ["For security reasons.", "To attract tourists.", "To help migrants."]),
   Q(D, "What do critics of the wall say?", ["It is expensive and inhuman.", "It is too small.", "It is too beautiful."])],
  [DT(D, "Quel fleuve forme une partie de la frontière ?", ["Le Rio Grande", "Le Mississippi", "Le Colorado", "L'Amazone"]),
   DT(D, "Quelle ville mexicaine fait face à San Diego ?", ["Tijuana", "Mexico", "Cancún", "Acapulco"]),
   DT(D, "Comment appelle-t-on les passeurs ?", ["Smugglers ou coyotes", "Dreamers", "Rangers", "Cowboys"]),
   DT(D, "Combien de sans-papiers environ vivent aux États-Unis ?", ["Environ 11 millions", "Environ 1 million", "Environ 100 millions", "Environ 100 000"])],
  [W(D, "Trouve le mot qui veut dire « camions ».", "trucks"), W(D, "Trouve le mot qui veut dire « sans papiers ».", "undocumented"),
   W(D, "Trouve le mot qui veut dire « asile ».", "asylum"), W(D, "Trouve le mot qui veut dire « qui divise le plus » (2 mots).", ["most divisive", "the most divisive"])])

# ═════════ HEALTH CARE ═════════
F = "cu_sante_usa.html"
DZ(F, """
## Pas de sécurité sociale universelle
Contrairement à la France ou au Royaume-Uni, les États-Unis n'ont pas de système de santé public couvrant tout le monde. La plupart des Américains ont une **health insurance** privée, souvent fournie par leur employeur. Perdre son emploi peut donc signifier perdre son assurance. Les assurances comportent des **premiums** (cotisations), des **deductibles** (franchises) et des **co-pays** (participations), si bien que même les assurés paient souvent beaucoup de leur poche.

## Les programmes publics
En 1965, le président Lyndon Johnson crée deux programmes publics :
- **Medicare**, pour les personnes de 65 ans et plus ;
- **Medicaid**, pour les personnes à faibles revenus (géré avec les États, avec des règles différentes selon les États).
Les anciens combattants ont aussi leur propre système de santé.

## L'Obamacare
En 2010, le président **Barack Obama** fait voter l'**Affordable Care Act**, surnommé **Obamacare**. La loi oblige les assureurs à accepter les malades chroniques (avant, on pouvait être refusé pour une **pre-existing condition**), permet aux jeunes de rester sur l'assurance de leurs parents jusqu'à 26 ans, élargit Medicaid et aide à payer une assurance. Des millions d'Américains obtiennent ainsi une couverture. La loi a été très contestée par les républicains, mais elle a survécu à de nombreuses tentatives d'abrogation. Aujourd'hui, environ 8 % des Américains n'ont toujours aucune assurance.

## Le système le plus cher du monde
Les États-Unis dépensent pour la santé bien plus que n'importe quel autre pays (environ 17 % de leur richesse nationale), alors que l'espérance de vie y est plus faible que dans la plupart des pays riches. Les prix sont très élevés : une nuit à l'hôpital, une ambulance ou une naissance peuvent coûter des milliers de dollars ; le prix de certains médicaments, comme l'insuline pour les diabétiques, a longtemps fait scandale. Les factures médicales sont une cause fréquente d'endettement des ménages, et certains malades lancent des cagnottes en ligne pour payer leurs soins.

## Un débat politique majeur
- La gauche du Parti démocrate défend un système public pour tous, **Medicare for All**, sur le modèle européen.
- Les républicains préfèrent un système fondé sur le marché, la concurrence et la liberté de choix, et critiquent le coût et l'intervention de l'État.
Entre les deux, beaucoup proposent d'améliorer l'Obamacare. La santé est, élection après élection, l'une des premières préoccupations des Américains.
""", """
health = la santé
a doctor = un médecin
a hospital = un hôpital
insurance = l'assurance
a bill = une facture
medicine = les médicaments
expensive = cher
sick = malade
""", [
 ("Comment la plupart des Américains sont-ils assurés ?", ["Par une assurance privée, souvent fournie par l'employeur", "Par la Sécurité sociale universelle", "Ils ne sont jamais assurés"], ""),
 ("Pour qui est Medicare ?", ["Les personnes de 65 ans et plus", "Les enfants", "Les soldats"], ""),
 ("Qu'a changé l'Obamacare ?", ["Les assureurs doivent accepter les malades chroniques, et des millions de personnes sont couvertes", "Les soins sont devenus gratuits pour tous", "Rien"], ""),
 ("Pourquoi le système américain est-il critiqué ?", ["Il est très cher et l'espérance de vie y est plus faible", "Il n'y a pas de médecins", "Il est gratuit"], ""),
 ("Que défend « Medicare for All » ?", ["Un système public pour tous", "La fin des hôpitaux", "Une assurance réservée aux riches"], ""),
 ("Que préfèrent les républicains ?", ["Un système fondé sur le marché et la concurrence", "Un système entièrement public", "La médecine traditionnelle"], ""),
], [("Lyndon Johnson", "président démocrate de 1963 à 1969"), ("**Barack Obama**", "président démocrate de 2009 à 2017")])
D = "hc"
culture(F, "Culture : Health care in the USA", 'Health care <span>in the USA</span>',
  "Culture · assurances, Obamacare et le système le plus cher du monde", ("#a7f3d0", "#0f766e"),
  reperes("Aux États-Unis, il n'y a pas d'assurance maladie publique pour tous. La plupart des gens dépendent d'une assurance privée, et les soins coûtent très cher.",
    [("1965", "création de Medicare (65 ans et plus) et Medicaid (faibles revenus)"), ("2010", "Affordable Care Act, surnommé Obamacare"),
     ("environ 17 %", "part de la richesse nationale consacrée à la santé"), ("environ 8 %", "d'Américains toujours sans assurance")],
    "health insurance, a premium, a hospital bill, Medicare, Medicaid, Obamacare, uninsured, a prescription"),
  {D: doc("Your money or your health?", [
    "In the USA, there is no free public health system for everybody. Most Americans have private health insurance, often paid partly by their employer. If you lose your job, you can lose your insurance.",
    "Two public programmes exist: Medicare for people over 65, and Medicaid for people with low incomes.",
    "In 2010, President Barack Obama passed a law called the Affordable Care Act, or \"Obamacare\". It helped millions of people to get insurance, and insurers could no longer refuse sick people.",
    "Health care in the USA is the most expensive in the world. A night at the hospital or an ambulance can cost thousands of dollars. Some people get into debt because of medical bills.",
    "Americans disagree about the solution. Some want a public system for all, like in Europe. Others prefer a system based on the market and competition."])},
  [TF(D, "There is a free public health system for everybody in the USA.", False, "« there is no free public health system »."),
   TF(D, "You can lose your insurance if you lose your job.", True, "« you can lose your insurance »."),
   TF(D, "Medicare is for people over 65.", True, "« Medicare for people over 65 »."),
   TF(D, "Obamacare helped millions of people to get insurance.", True, "« helped millions of people »."),
   TF(D, "Health care in the USA is cheap.", False, "« the most expensive in the world »."),
   TF(D, "All Americans agree about health care.", False, "« Americans disagree »." )],
  [Q(D, "Who often pays part of the insurance?", ["The employer.", "The President.", "The hospital."]),
   Q(D, "What is Medicaid?", ["A programme for people with low incomes.", "A medicine.", "A private insurance."]),
   Q(D, "Why do some people get into debt?", ["Because of medical bills.", "Because of holidays.", "Because of cars."]),
   Q(D, "What do some Americans want?", ["A public system for all, like in Europe.", "No doctors.", "Only private hospitals."])],
  [DT(D, "Quel président fait voter l'Obamacare ?", ["Barack Obama", "Lyndon Johnson", "Donald Trump", "Bill Clinton"]),
   DT(D, "En quelle année Medicare est-il créé ?", ["1965", "2010", "1945", "1990"]),
   DT(D, "Jusqu'à quel âge un jeune peut-il rester sur l'assurance de ses parents ?", ["26 ans", "18 ans", "21 ans", "30 ans"]),
   DT(D, "Comment dit-on « assurance maladie » ?", ["Health insurance", "Health money", "Sick card", "Doctor pass"])],
  [W(D, "Trouve le mot qui veut dire « employeur ».", "employer"), W(D, "Trouve le mot qui veut dire « revenus ».", "incomes"),
   W(D, "Trouve le mot qui veut dire « dettes ».", "debt"), W(D, "Trouve le mot qui veut dire « concurrence ».", "competition")])

# ═════════ DEATH PENALTY ═════════
F = "cu_peine_mort.html"
DZ(F, """
## Une exception parmi les démocraties
Les États-Unis sont l'une des rares démocraties occidentales à appliquer encore la **death penalty** (ou **capital punishment**). L'Union européenne l'a abolie partout ; la France l'a abolie en 1981, le Royaume-Uni en 1965 pour le meurtre.

## Un pays divisé
La peine de mort relève surtout des États. Aujourd'hui, 27 États la prévoient, et 23 États, ainsi que Washington, D.C., l'ont abolie. Parmi les États qui la gardent, quatre (dont la Californie) ont suspendu les exécutions par décision de leur gouverneur. Le gouvernement fédéral et l'armée la conservent aussi. Le **Texas** est de loin l'État qui exécute le plus depuis 1976.

## Une histoire en dents de scie
En 1972, la Cour suprême suspend la peine de mort, jugée appliquée de façon arbitraire et discriminatoire (*Furman v. Georgia*). Elle est rétablie en 1976 (*Gregg v. Georgia*). Depuis, la Cour a limité son usage : interdiction d'exécuter des personnes atteintes de déficience intellectuelle (2002) et des personnes qui étaient mineures au moment du crime (2005). Le nombre de nouvelles condamnations a fortement baissé depuis les années 1990, mais les exécutions sont reparties à la hausse en 2025.

## Comment exécute-t-on ?
La méthode principale est la **lethal injection**. Mais les fabricants de médicaments refusent de plus en plus de fournir les produits, si bien que certains États ont réintroduit d'autres méthodes : la chaise électrique, le peloton d'exécution, ou l'asphyxie à l'azote, utilisée pour la première fois en Alabama en 2024. Les condamnés passent souvent des décennies dans le **death row** (le couloir de la mort) avant d'être exécutés, à cause des longs recours.

## Les arguments
- Les partisans (**supporters**) estiment que c'est une juste punition pour les crimes les plus graves, qu'elle apporte une forme de justice aux familles des victimes et qu'elle peut dissuader les criminels.
- Les opposants (**opponents**) rappellent le risque d'exécuter des innocents (depuis 1973, environ 200 condamnés à mort ont été innocentés), les inégalités raciales et sociales dans son application (les accusés pauvres et noirs y sont plus exposés), son coût plus élevé que la prison à vie, et l'absence de preuve qu'elle dissuade davantage. Beaucoup y voient aussi une atteinte aux droits humains.
Selon les sondages, le soutien des Américains à la peine de mort est aujourd'hui à son niveau le plus bas depuis un demi-siècle, mais il reste majoritaire ou proche de la majorité.
""", """
a crime = un crime
a prison = une prison
a judge = un juge
a victim = une victime
innocent = innocent
guilty = coupable
the law = la loi
justice = la justice
""", [
 ("Combien d'États américains prévoient encore la peine de mort ?", ["27", "50", "3"], "23 l'ont abolie."),
 ("Quel État exécute le plus depuis 1976 ?", ["Le Texas", "La Californie", "New York"], ""),
 ("Qu'a décidé la Cour suprême en 1972 ?", ["Elle suspend la peine de mort, jugée arbitraire", "Elle l'étend à tous les États", "Elle abolit les prisons"], "Rétablie en 1976."),
 ("Qu'est-ce que le « death row » ?", ["Le couloir de la mort", "Une rue de Las Vegas", "Un film"], ""),
 ("Quel argument avancent les partisans ?", ["Une juste punition qui apporte justice aux familles des victimes", "Elle coûte moins cher", "Elle protège les innocents"], ""),
 ("Quel argument avancent les opposants ?", ["Le risque d'exécuter des innocents et les inégalités", "Elle est trop rare", "Elle est trop douce"], ""),
], [("*Furman v. Georgia*", "arrêt de la Cour suprême de 1972"), ("*Gregg v. Georgia*", "arrêt de 1976")])
D = "dp"
culture(F, "Culture : The death penalty in the USA", 'The death <span>penalty</span>',
  "Culture · un débat qui divise l'Amérique", ("#e5e5e5", "#404040"),
  reperes("Les États-Unis sont l'une des rares démocraties occidentales à pratiquer encore la peine de mort. Elle dépend surtout de chaque État.",
    [("1972", "la Cour suprême suspend la peine de mort"), ("1976", "elle est rétablie"), ("2002 / 2005", "interdite pour les personnes déficientes intellectuelles / mineures au moment des faits"),
     ("27 contre 23", "États qui la prévoient / qui l'ont abolie"), ("1981", "abolition en France")],
    "the death penalty, an execution, death row, a lethal injection, a trial, a jury, innocent, to abolish"),
  {D: doc("An eye for an eye?", [
    "The USA is one of the few Western democracies that still uses the death penalty. In the European Union, it has been abolished everywhere.",
    "Each state makes its own decision. Today, 27 states still have the death penalty, and 23 states have abolished it. Texas is the state with the most executions.",
    "The main method is lethal injection. Prisoners often wait for many years, sometimes decades, on \"death row\" before their execution.",
    "Supporters of the death penalty say it is a fair punishment for terrible crimes and that it brings justice to the victims' families.",
    "Opponents say that innocent people can be executed by mistake: since 1973, about 200 people on death row have been found innocent. They also say it is used more against poor and Black people, and that it does not stop crime."])},
  [TF(D, "All Western democracies use the death penalty.", False, "« one of the few Western democracies »."),
   TF(D, "Each state decides about the death penalty.", True, "« Each state makes its own decision »."),
   TF(D, "Texas has the most executions.", True, "« Texas is the state with the most executions »."),
   TF(D, "Prisoners are executed a few days after their trial.", False, "« many years, sometimes decades »."),
   TF(D, "About 200 people on death row have been found innocent since 1973.", True, "« about 200 people »."),
   TF(D, "The death penalty has been abolished everywhere in the European Union.", True, "« In the European Union, it has been abolished everywhere »." )],
  [Q(D, "What is the main method of execution?", ["Lethal injection.", "The guillotine.", "Hanging."]),
   Q(D, "What is death row?", ["The place where prisoners wait for execution.", "A street in Texas.", "A court."]),
   Q(D, "What do supporters say?", ["It is a fair punishment and brings justice to families.", "It is too expensive.", "It is dangerous for innocent people."]),
   Q(D, "What do opponents say?", ["Innocent people can be executed by mistake.", "It is not used enough.", "It is too cheap."])],
  [DT(D, "Combien d'États ont aboli la peine de mort ?", ["23", "27", "50", "10"]),
   DT(D, "Quand la France a-t-elle aboli la peine de mort ?", ["1981", "1965", "1945", "2000"]),
   DT(D, "Comment dit-on « le couloir de la mort » ?", ["Death row", "Death road", "Dead street", "Jail line"]),
   DT(D, "Quand la peine de mort est-elle rétablie aux États-Unis ?", ["1976", "1972", "1990", "2005"])],
  [W(D, "Trouve le mot qui veut dire « aboli ».", "abolished"), W(D, "Trouve le mot qui veut dire « une punition ».", ["punishment", "a fair punishment"]),
   W(D, "Trouve le mot qui veut dire « par erreur » (2 mots).", ["by mistake"]), W(D, "Trouve le mot qui veut dire « opposants ».", "opponents")])

# ═════════ HOLLYWOOD ═════════
F = "cu_hollywood.html"
DZ(F, """
## Pourquoi Hollywood ?
Au début du 20e siècle, le cinéma américain se fait surtout à New York. Mais dans les années 1910, de nombreux producteurs s'installent en Californie, dans un quartier de Los Angeles appelé **Hollywood** : il y fait beau toute l'année, on trouve des paysages variés (mer, désert, montagnes) et on y est loin des avocats de Thomas Edison, qui réclamait des droits sur les caméras. En 1923, un immense panneau publicitaire « HOLLYWOODLAND » est installé sur une colline ; raccourci en **HOLLYWOOD**, il devient un symbole mondial.

## Les grands studios
Des studios comme **Paramount**, **Warner Bros.**, **MGM** ou **Universal** produisent des centaines de films par an, comme dans une usine : c'est le **studio system**. Les acteurs sont sous contrat, les **stars** sont fabriquées par la publicité. Le muet donne ses vedettes, comme **Charlie Chaplin**. En 1927, *The Jazz Singer* marque l'arrivée du parlant. En 1929 ont lieu les premiers **Academy Awards**, les **Oscars**. En 1937, Walt Disney sort *Snow White*, premier long métrage d'animation.

## L'âge d'or
Des années 1930 aux années 1950, c'est le **Golden Age** : westerns, comédies musicales, films de gangsters, drames. *Gone with the Wind* (1939), *The Wizard of Oz* (1939), *Casablanca* (1942)… Des stars comme Marilyn Monroe, James Dean ou Marlon Brando deviennent des icônes. Un code de censure, le **Hays Code**, limite la violence et la sexualité à l'écran jusqu'en 1968.

## Le Nouvel Hollywood et les blockbusters
Dans les années 1970, de jeunes réalisateurs (Scorsese, Coppola, Spielberg, Lucas) renouvellent le cinéma. *Jaws* (1975) de Spielberg et *Star Wars* (1977) de Lucas inventent le **blockbuster** : un film à gros budget, sorti l'été dans des milliers de salles, avec produits dérivés. Aujourd'hui, les super-héros, les suites et les franchises dominent le box-office.

## Une puissance mondiale… et des débats
Hollywood est un outil de **soft power** : il diffuse dans le monde entier le mode de vie et les valeurs américaines. Mais il est aussi critiqué : manque de diversité (la campagne **#OscarsSoWhite** en 2015), stéréotypes, inégalités entre hommes et femmes, et scandales d'abus révélés par le mouvement **#MeToo** en 2017. Aujourd'hui, les plateformes de streaming comme Netflix bouleversent l'industrie, et en 2023 les scénaristes et acteurs ont mené une longue grève, notamment pour se protéger face à l'intelligence artificielle.
""", """
a film = un film
an actor = un acteur
a star = une vedette
a studio = un studio
a director = un réalisateur
a cinema = un cinéma
a prize = un prix
a sign = un panneau
""", [
 ("Pourquoi les producteurs s'installent-ils à Hollywood ?", ["Le beau temps, les paysages variés et la distance avec les avocats d'Edison", "Il y avait de l'or", "Le gouvernement les y obligeait"], ""),
 ("Que signifiait à l'origine le panneau HOLLYWOODLAND ?", ["C'était une publicité immobilière", "Le nom d'un studio", "Le nom d'un film"], ""),
 ("Qu'est-ce que le « studio system » ?", ["Des studios qui produisent des films comme dans une usine, avec des acteurs sous contrat", "Une école de cinéma", "Un type de caméra"], ""),
 ("Quel film invente le blockbuster d'été en 1975 ?", ["Jaws (Les Dents de la mer)", "Casablanca", "Snow White"], ""),
 ("Qu'est-ce que le « soft power » ?", ["L'influence d'un pays par sa culture", "Une arme", "Un studio"], ""),
 ("Que dénonçait la campagne #OscarsSoWhite ?", ["Le manque de diversité", "Le prix des billets", "La couleur du tapis rouge"], ""),
], [("Thomas Edison", "inventeur américain"), ("**Charlie Chaplin**", "acteur et réalisateur britannique, créateur de Charlot"), ("Spielberg", "Steven Spielberg, réalisateur"), ("Lucas", "George Lucas, créateur de Star Wars")])
D = "hw"
culture(F, "Culture : Hollywood", 'Hollywood',
  "Culture · l'usine à rêves du cinéma américain", ("#fde68a", "#b91c1c"),
  reperes("Depuis les années 1910, Hollywood, quartier de Los Angeles, est la capitale du cinéma américain et un symbole mondial.",
    [("années 1910", "les producteurs s'installent à Hollywood"), ("1923", "panneau HOLLYWOODLAND"), ("1927", "premier grand film parlant"),
     ("1929", "premiers Oscars"), ("1930 – 1950", "âge d'or des studios"), ("1975 – 1977", "Jaws et Star Wars : naissance du blockbuster")],
    "a film, a studio, a star, a director, the Oscars, a blockbuster, the box office, streaming"),
  {D: doc("The dream factory", [
    "In the 1910s, film producers moved from New York to Hollywood, in Los Angeles. The weather was sunny all year, and there were mountains, beaches and deserts nearby.",
    "Big studios like Paramount and Warner Bros. produced hundreds of films every year. Actors became stars. In 1927, the first big film with sound was released, and the first Oscars took place in 1929.",
    "From the 1930s to the 1950s, it was the golden age of Hollywood, with stars like Marilyn Monroe and James Dean.",
    "In the 1970s, directors like Steven Spielberg and George Lucas invented the blockbuster, with films like Jaws and Star Wars.",
    "Hollywood films are watched all over the world, but Hollywood is also criticised for a lack of diversity. Today, streaming platforms are changing the industry."])},
  [TF(D, "Film producers moved from Los Angeles to New York.", False, "De New York vers Hollywood."),
   TF(D, "The weather in Hollywood was sunny all year.", True, "« sunny all year »."),
   TF(D, "The first Oscars took place in 1929.", True, "« in 1929 »."),
   TF(D, "Marilyn Monroe was a star of the golden age.", True, "« stars like Marilyn Monroe »."),
   TF(D, "Steven Spielberg invented the silent film.", False, "Il a inventé le blockbuster avec Lucas."),
   TF(D, "Hollywood is never criticised.", False, "« criticised for a lack of diversity »." )],
  [Q(D, "Why did producers move to Hollywood?", ["Sunny weather and varied landscapes.", "Cheap cars.", "Because of the Oscars."]),
   Q(D, "What happened in 1927?", ["The first big film with sound was released.", "The first Oscars.", "Star Wars was released."]),
   Q(D, "What is a blockbuster?", ["A very popular big-budget film.", "A small independent film.", "A cinema."]),
   Q(D, "What is changing the industry today?", ["Streaming platforms.", "The radio.", "Silent films."])],
  [DT(D, "Quel est le premier long métrage d'animation de Disney ?", ["Snow White (Blanche-Neige)", "Mickey Mouse", "Le Roi Lion", "Pinocchio"]),
   DT(D, "Comment s'appellent les récompenses du cinéma américain ?", ["Les Oscars", "Les Césars", "Les Grammys", "Les Emmys"]),
   DT(D, "Quel mouvement de 2017 dénonce les abus ?", ["#MeToo", "#OscarsSoWhite", "#BlackLivesMatter", "#Hollywoodland"]),
   DT(D, "Quel code de censure s'applique jusqu'en 1968 ?", ["Le code Hays", "Le code Morse", "Le code civil", "Le code Disney"])],
  [W(D, "Trouve le mot qui veut dire « producteurs ».", "producers"), W(D, "Trouve le mot qui veut dire « sorti » (un film).", "released"),
   W(D, "Trouve le mot qui veut dire « réalisateurs ».", "directors"), W(D, "Trouve le mot qui veut dire « plateformes ».", "platforms")])

# ═════════ US SPORTS ═════════
F = "cu_sports_us.html"
DZ(F, """
## Les quatre grandes ligues
Le sport américain est dominé par quatre grandes ligues professionnelles :
- la **NFL** (football américain), le sport le plus populaire ;
- la **NBA** (basket-ball) ;
- la **MLB** (baseball), longtemps appelé **America's pastime**, le passe-temps national ;
- la **NHL** (hockey sur glace), partagée avec le Canada.
Les équipes sont des **franchises**, des entreprises privées qui peuvent déménager d'une ville à l'autre. Il n'y a ni montée ni descente : les mêmes équipes restent dans la ligue. Pour garder l'équilibre, les plus mauvaises équipes choisissent en premier les meilleurs jeunes joueurs lors de la **draft**, et un plafond salarial (**salary cap**) existe dans plusieurs ligues.

## Le Super Bowl
La finale de la NFL, le **Super Bowl**, a lieu chaque année début février depuis 1967. C'est l'émission de télévision la plus regardée du pays, avec plus de 100 millions de téléspectateurs. Les publicités diffusées pendant le match coûtent des millions de dollars et sont attendues autant que le jeu, tout comme le concert de la mi-temps (**halftime show**). Avant les matchs, les supporters organisent des **tailgate parties**, des barbecues sur les parkings des stades.

## Basket-ball et baseball
Le basket-ball a été inventé en 1891 par **James Naismith**, un professeur canadien, dans un gymnase du Massachusetts, avec des paniers à pêches accrochés aux murs. La NBA a produit des légendes mondiales : Michael Jordan, Kobe Bryant, LeBron James. Le baseball, avec ses longues saisons d'été et sa finale, les **World Series**, est un pilier de la culture américaine ; **Jackie Robinson** a été en 1947 le premier joueur noir de la ligue majeure moderne, un symbole de la lutte contre la ségrégation.

## Le sport universitaire
Une particularité américaine : le sport universitaire est extrêmement populaire. Les matchs de football américain des universités remplissent des stades de 100 000 places, et le tournoi de basket universitaire de mars, la **March Madness**, passionne le pays. Les meilleurs lycéens sportifs obtiennent des bourses (**athletic scholarships**) pour étudier gratuitement.

## Et le « soccer » ?
Le football, appelé **soccer** aux États-Unis, a longtemps été peu suivi chez les hommes, mais il progresse beaucoup, avec la ligue **MLS** et l'arrivée de stars comme Lionel Messi à Miami en 2023. L'équipe féminine américaine est l'une des meilleures du monde, plusieurs fois championne du monde. En 2026, les États-Unis ont accueilli la Coupe du monde masculine avec le Canada et le Mexique.
""", """
a team = une équipe
a player = un joueur
a ball = un ballon
a game = un match
a stadium = un stade
a fan = un supporter
to score = marquer
a coach = un entraîneur
""", [
 ("Quelles sont les quatre grandes ligues ?", ["NFL, NBA, MLB, NHL", "Premier League, Liga, Serie A, Bundesliga", "Rugby, cricket, tennis, golf"], ""),
 ("Qu'a de particulier le système des ligues américaines ?", ["Pas de montée ni de descente, et une draft pour les jeunes joueurs", "Les équipes appartiennent à l'État", "Il n'y a pas de finale"], ""),
 ("Qu'est-ce que le Super Bowl ?", ["La finale de la NFL, l'émission la plus regardée du pays", "Un plat", "Un stade de baseball"], ""),
 ("Qui a inventé le basket-ball ?", ["James Naismith, en 1891", "Michael Jordan", "Abraham Lincoln"], ""),
 ("Pourquoi Jackie Robinson est-il un symbole ?", ["Premier joueur noir de la ligue majeure moderne de baseball, en 1947", "Il a inventé le baseball", "Il a été président"], ""),
 ("Qu'est-ce que la March Madness ?", ["Le tournoi de basket universitaire de mars", "Une fête de printemps", "Une course"], ""),
], [("**James Naismith**", "professeur d'éducation physique d'origine canadienne"), ("Lionel Messi", "footballeur argentin")])
D = "us"
culture(F, "Culture : American sports", 'American <span>sports</span>',
  "Culture · Super Bowl, NBA, baseball et sport universitaire", ("#bfdbfe", "#b91c1c"),
  reperes("Le sport américain est dominé par quatre grandes ligues : football américain (NFL), basket (NBA), baseball (MLB) et hockey (NHL).",
    [("1891", "invention du basket-ball"), ("1947", "Jackie Robinson, premier joueur noir de la MLB moderne"), ("1967", "premier Super Bowl"),
     ("chaque février", "le Super Bowl, émission la plus regardée du pays"), ("2026", "Coupe du monde de football aux États-Unis, au Canada et au Mexique")],
    "a league, a team, a franchise, the draft, a final, a stadium, a scholarship, a halftime show"),
  {D: doc("Game day", [
    "Americans love sport. The four biggest leagues are the NFL (American football), the NBA (basketball), MLB (baseball) and the NHL (ice hockey).",
    "The Super Bowl, the final of the NFL, takes place every February. It is the most watched TV programme in the USA. People also watch it for the adverts and the halftime show.",
    "Basketball was invented in 1891 by a teacher, James Naismith. Players like Michael Jordan and LeBron James became world famous. Baseball is called \"America's pastime\".",
    "University sport is also very popular. Some college football stadiums have 100,000 seats! Good young athletes can get scholarships to study for free.",
    "Soccer is becoming more popular in the USA. The American women's team is one of the best in the world, and in 2026 the USA hosted the men's World Cup with Canada and Mexico."])},
  [TF(D, "The NFL is the league of basketball.", False, "C'est le football américain."),
   TF(D, "The Super Bowl takes place every February.", True, "« every February »."),
   TF(D, "People also watch the Super Bowl for the adverts.", True, "« for the adverts and the halftime show »."),
   TF(D, "Basketball was invented in 1891.", True, "« in 1891 »."),
   TF(D, "University sport is not popular in the USA.", False, "« also very popular »."),
   TF(D, "The American women's soccer team is weak.", False, "« one of the best in the world »." )],
  [Q(D, "What is the Super Bowl?", ["The final of the NFL.", "A baseball stadium.", "A basketball team."]),
   Q(D, "What is called \"America's pastime\"?", ["Baseball.", "Ice hockey.", "Soccer."]),
   Q(D, "What can good young athletes get?", ["Scholarships to study for free.", "A car.", "A house."]),
   Q(D, "Which countries hosted the 2026 World Cup?", ["The USA, Canada and Mexico.", "The USA only.", "Brazil and Argentina."])],
  [DT(D, "Comment s'appelle la finale du baseball ?", ["Les World Series", "Le Super Bowl", "La March Madness", "Les Finals NBA"]),
   DT(D, "Comment les Américains appellent-ils le football ?", ["Soccer", "Football", "Footy", "Kickball"]),
   DT(D, "Quelle star argentine rejoint Miami en 2023 ?", ["Lionel Messi", "Cristiano Ronaldo", "Neymar", "Kylian Mbappé"]),
   DT(D, "Qui est le premier joueur noir de la MLB moderne ?", ["Jackie Robinson", "Michael Jordan", "Muhammad Ali", "Jesse Owens"])],
  [W(D, "Trouve le mot qui veut dire « ligues ».", "leagues"), W(D, "Trouve le mot qui veut dire « publicités ».", "adverts"),
   W(D, "Trouve le mot qui veut dire « places » (dans un stade).", "seats"), W(D, "Trouve le mot qui veut dire « a accueilli » (un événement).", "hosted")])

# ═════════ ROUTE 66 ═════════
F = "cu_route66.html"
DZ(F, """
## La « Mother Road »
Créée en **1926**, la **Route 66** relie Chicago à Santa Monica, au bord du Pacifique, sur près de 4 000 kilomètres à travers huit États : l'Illinois, le Missouri, le Kansas, l'Oklahoma, le Texas, le Nouveau-Mexique, l'Arizona et la Californie. Dans les années 1930, des centaines de milliers de familles du **Dust Bowl** l'empruntent pour fuir vers la Californie ; John Steinbeck l'appelle **the Mother Road** dans *The Grapes of Wrath*.

## La culture de la route
Après la guerre, les Américains achètent massivement des voitures et partent en vacances. Le long de la Route 66 fleurissent les **diners** (petits restaurants à l'américaine), les stations-service, les **motels** (mot formé de *motor* et *hotel*), les cinémas en plein air (**drive-ins**), les enseignes au néon et les attractions étranges, comme le **Cadillac Ranch** au Texas, où des voitures sont plantées dans le sol. Une chanson célèbre, *(Get Your Kicks on) Route 66*, popularise la route.

## Le roi automobile
La voiture est au cœur de l'identité américaine : synonyme de liberté et de réussite. En 1956, le président Eisenhower lance la construction d'un immense réseau d'autoroutes, les **interstates**. Les villes s'étalent en banlieues (**suburbs**) où l'on ne peut presque rien faire sans voiture. Les **drive-throughs** permettent de commander à manger, de retirer de l'argent ou même de se marier sans sortir de son véhicule. Aujourd'hui encore, la grande majorité des Américains vont travailler en voiture, et les transports en commun sont peu développés en dehors des grandes villes.

## Le road trip
Le **road trip**, le grand voyage en voiture à travers le pays, est un rite américain. Le roman *On the Road* (1957) de Jack Kerouac, récit de voyages à travers l'Amérique, devient la bible de la **Beat Generation** : un groupe d'écrivains américains des années 1950 (Jack Kerouac, le poète Allen Ginsberg, William S. Burroughs) qui rejettent le conformisme et la société de consommation de l'Amérique d'après-guerre, et cherchent la liberté dans la route, le jazz, la poésie et la spiritualité. De nombreux films (*Easy Rider*, *Thelma & Louise*) célèbrent la route comme espace de liberté.
[→ En savoir plus : la Beat Generation et les autres générations américaines](cu_generations.html)

## Le déclin et la renaissance
Remplacée par les interstates, la Route 66 est officiellement retirée du réseau en 1985. Des villes qui vivaient des voyageurs dépérissent. Mais des passionnés se mobilisent pour la sauver : des tronçons historiques sont protégés, les vieux motels restaurés, et des touristes du monde entier viennent la parcourir en voiture ou à moto. Le film d'animation *Cars* (2006) de Pixar s'inspire de cette histoire. En 2026, la route a fêté son centenaire.
""", """
a road = une route
a car = une voiture
a motel = un motel
a trip = un voyage
a map = une carte
gas = l'essence (US)
a highway = une autoroute
freedom = la liberté
""", [
 ("Quelles villes relie la Route 66 ?", ["Chicago et Santa Monica", "New York et Miami", "Boston et Seattle"], ""),
 ("Pourquoi Steinbeck l'appelle-t-il « the Mother Road » ?", ["Des familles du Dust Bowl l'empruntaient pour fuir vers la Californie", "Elle a été construite par des mères", "C'est la plus vieille route du monde"], ""),
 ("D'où vient le mot « motel » ?", ["De « motor » et « hotel »", "D'un nom propre", "Du français « mot »"], ""),
 ("Que sont les interstates ?", ["Un grand réseau d'autoroutes lancé en 1956", "Des États", "Des motels"], ""),
 ("Que raconte On the Road de Jack Kerouac ?", ["Des voyages à travers l'Amérique", "La vie d'un fermier", "Une guerre"], ""),
 ("Quel film d'animation s'inspire de la Route 66 ?", ["Cars", "Toy Story", "Shrek"], ""),
], [("Eisenhower", "président républicain de 1953 à 1961"), ("Jack Kerouac", "écrivain américain, 1922-1969")])
D = "r66"
culture(F, "Culture : Route 66 and car culture", 'Route <span>66</span>',
  "Culture · la route mythique et la culture de la voiture", ("#fcd34d", "#1d4ed8"),
  reperes("La Route 66 relie Chicago à la côte Pacifique depuis 1926. Elle symbolise la culture automobile et le goût américain pour le voyage.",
    [("1926", "création de la Route 66"), ("années 1930", "les migrants du Dust Bowl l'empruntent"), ("1956", "lancement du réseau d'autoroutes interstates"),
     ("1957", "On the Road de Jack Kerouac"), ("1985", "la Route 66 est retirée du réseau officiel"), ("2026", "centenaire de la route")],
    "a road, a highway, a road trip, a motel, a diner, a gas station, a suburb, freedom"),
  {D: doc("Get your kicks", [
    "Route 66 was created in 1926. It went from Chicago to Santa Monica, on the Pacific coast, through eight states. It is almost 4,000 kilometres long.",
    "In the 1930s, poor families escaping the Dust Bowl used it to go to California. The writer John Steinbeck called it \"the Mother Road\".",
    "After the Second World War, many Americans bought cars and travelled. Along the road, there were diners, gas stations and motels with neon signs.",
    "Cars are very important in American culture: they symbolise freedom. Today, most Americans drive to work. A road trip across the country is a typical American dream.",
    "In 1985, Route 66 was replaced by big highways. But today, tourists from all over the world come to drive on it. The film Cars was inspired by its story."])},
  [TF(D, "Route 66 was created in 1926.", True, "« created in 1926 »."),
   TF(D, "It goes from New York to Los Angeles.", False, "De Chicago à Santa Monica."),
   TF(D, "Families escaping the Dust Bowl used Route 66.", True, "« used it to go to California »."),
   TF(D, "Cars symbolise freedom for Americans.", True, "« they symbolise freedom »."),
   TF(D, "Most Americans go to work by train.", False, "« most Americans drive to work »."),
   TF(D, "No tourists drive on Route 66 today.", False, "« tourists from all over the world »." )],
  [Q(D, "What did Steinbeck call Route 66?", ["The Mother Road.", "The Highway to Hell.", "The Golden Road."]),
   Q(D, "What could you find along the road?", ["Diners, gas stations and motels.", "Castles and palaces.", "Ski resorts."]),
   Q(D, "What do cars symbolise?", ["Freedom.", "Danger.", "Poverty."]),
   Q(D, "What replaced Route 66 in 1985?", ["Big highways.", "Railways.", "Airports."])],
  [DT(D, "Quelle ville est au départ de la Route 66 ?", ["Chicago", "New York", "Dallas", "Denver"]),
   DT(D, "Combien d'États traverse-t-elle ?", ["Huit", "Deux", "Cinquante", "Treize"]),
   DT(D, "Quel président lance les interstates en 1956 ?", ["Eisenhower", "Kennedy", "Roosevelt", "Lincoln"]),
   DT(D, "Où des Cadillac sont-elles plantées dans le sol ?", ["Au Cadillac Ranch, au Texas", "À Chicago", "À Las Vegas", "À Hollywood"])],
  [W(D, "Trouve le mot qui veut dire « stations-service » (2 mots).", ["gas stations", "gas station"]), W(D, "Trouve le mot qui veut dire « enseignes au néon ».", ["neon signs"]),
   W(D, "Trouve le mot qui veut dire « autoroutes ».", "highways"), W(D, "Trouve le mot qui veut dire « symbolisent ».", "symbolise")])

# ═════════ SILICON VALLEY ═════════
F = "cu_silicon_valley.html"
DZ(F, """
## Une vallée devenue légende
La **Silicon Valley** désigne la région située au sud de la baie de San Francisco, en Californie, autour de villes comme Palo Alto, Mountain View, Cupertino et San José. Son nom vient du **silicon** (silicium), le matériau des puces électroniques fabriquées dans la région à partir des années 1960. L'expression apparaît dans la presse en 1971.

## Tout commence dans un garage
L'université de **Stanford** encourage dès les années 1930-1950 ses étudiants à créer des entreprises. En 1939, deux d'entre eux, Bill Hewlett et David Packard, fondent **HP** dans un garage de Palo Alto, aujourd'hui surnommé « le lieu de naissance de la Silicon Valley ». Dans les années 1950-1960, des entreprises de semi-conducteurs s'installent ; **Intel** est fondée en 1968. Le garage devient un mythe : en 1976, **Steve Jobs** et **Steve Wozniak** créent **Apple** dans le garage des parents de Jobs ; en 1998, **Google** naît dans un garage loué à Menlo Park.

## Le modèle de la Silicon Valley
- Les **startups** : de jeunes entreprises innovantes qui veulent grandir très vite.
- Le **venture capital** : des investisseurs misent sur ces startups en espérant que l'une d'elles devienne géante.
- Une culture de l'échec accepté (« *fail fast* ») : rater n'est pas une honte, c'est apprendre.
- Des bureaux décontractés, des salariés en sweat-shirt, des stock-options.
Des géants y ont leur siège : Apple, Google (Alphabet), Meta (Facebook, créé à Harvard puis installé à Palo Alto), Nvidia, et de nombreuses entreprises d'intelligence artificielle.

## Les critiques
Le succès a un revers. Les prix des logements sont parmi les plus élevés du monde, si bien que des enseignants, des pompiers ou des employés ne peuvent plus y vivre, et que le nombre de sans-abri est élevé dans la région. Les entreprises de la tech sont critiquées pour le manque de diversité de leurs employés (peu de femmes, de Noirs et d'Hispaniques), pour l'exploitation des données personnelles, pour leur influence politique, pour l'addiction aux écrans et pour leur position quasi monopolistique. Le développement rapide de l'intelligence artificielle suscite de nouveaux débats sur l'emploi, la désinformation et la sécurité.

## Un modèle copié partout
De nombreux pays ont tenté de créer leur propre « Silicon » : Silicon Wadi en Israël, Silicon Roundabout à Londres… Mais la combinaison d'universités, d'argent, d'immigration de talents du monde entier et de goût du risque reste difficile à reproduire.
""", """
a computer = un ordinateur
a company = une entreprise
a garage = un garage
a phone = un téléphone
an engineer = un ingénieur
an idea = une idée
data = les données
a screen = un écran
""", [
 ("D'où vient le nom « Silicon Valley » ?", ["Du silicium, le matériau des puces électroniques", "D'un fondateur", "D'une montagne"], ""),
 ("Quelle université a joué un grand rôle ?", ["Stanford", "Oxford", "La Sorbonne"], ""),
 ("Où sont nées HP, Apple et Google ?", ["Dans des garages", "Dans des châteaux", "Dans des universités européennes"], ""),
 ("Que signifie « fail fast » ?", ["Rater n'est pas une honte, c'est apprendre", "Il faut éviter l'échec à tout prix", "Il faut travailler lentement"], ""),
 ("Quel problème touche les habitants de la région ?", ["Les prix très élevés des logements", "Le manque d'emplois", "Le froid"], ""),
 ("Quelle critique fait-on aux géants de la tech ?", ["L'exploitation des données personnelles et le manque de diversité", "Ils sont trop petits", "Ils n'utilisent pas Internet"], ""),
], [("**Steve Jobs**", "cofondateur d'Apple, mort en 2011"), ("**Steve Wozniak**", "ingénieur, cofondateur d'Apple")])
D = "sv"
culture(F, "Culture : Silicon Valley", 'Silicon <span>Valley</span>',
  "Culture · garages, startups et géants de la tech", ("#a5f3fc", "#4338ca"),
  reperes("La Silicon Valley, au sud de San Francisco, est le cœur mondial de l'industrie technologique.",
    [("1939", "HP naît dans un garage de Palo Alto"), ("1968", "création d'Intel"), ("1971", "l'expression « Silicon Valley » apparaît"),
     ("1976", "Apple, dans un garage"), ("1998", "Google, dans un garage"), ("2004", "Facebook s'installe à Palo Alto")],
    "technology, a startup, a chip, an investor, an engineer, data, artificial intelligence, a tech giant"),
  {D: doc("From garages to giants", [
    "Silicon Valley is a region south of San Francisco, in California. Its name comes from silicon, the material used to make computer chips.",
    "Many famous companies started in a garage. In 1939, two students founded HP in Palo Alto. In 1976, Steve Jobs and Steve Wozniak created Apple in a garage, and Google was born in a garage in 1998.",
    "Silicon Valley is famous for its startups, young companies that want to grow very fast. Investors give them money, and failure is not a shame: it is a way to learn.",
    "Today, tech giants like Apple, Google, Meta and Nvidia have their headquarters there. Many companies work on artificial intelligence.",
    "But there are problems: houses are extremely expensive, and tech companies are criticised for using people's personal data and for a lack of diversity."])},
  [TF(D, "Silicon Valley is in California.", True, "« south of San Francisco, in California »."),
   TF(D, "Its name comes from a person called Silicon.", False, "Du silicium."),
   TF(D, "Apple was created in a garage.", True, "« in a garage »."),
   TF(D, "In Silicon Valley, failure is a terrible shame.", False, "« failure is not a shame »."),
   TF(D, "Many companies work on artificial intelligence.", True, "« work on artificial intelligence »."),
   TF(D, "Houses in Silicon Valley are cheap.", False, "« extremely expensive »." )],
  [Q(D, "What is a startup?", ["A young company that wants to grow very fast.", "An old factory.", "A computer."]),
   Q(D, "Who created Apple?", ["Steve Jobs and Steve Wozniak.", "Bill Gates.", "Two Stanford teachers."]),
   Q(D, "What do investors do?", ["They give money to startups.", "They build garages.", "They sell computers."]),
   Q(D, "Why are tech companies criticised?", ["For using personal data and a lack of diversity.", "For being too small.", "For their garages."])],
  [DT(D, "En quelle année Apple est-elle créée ?", ["1976", "1939", "1998", "2004"]),
   DT(D, "Quelle entreprise naît à Palo Alto en 1939 ?", ["HP", "Microsoft", "Amazon", "IBM"]),
   DT(D, "Quelle université est au cœur de la Silicon Valley ?", ["Stanford", "Harvard", "Yale", "Princeton"]),
   DT(D, "Quel réseau social s'installe à Palo Alto en 2004 ?", ["Facebook", "Twitter", "TikTok", "Instagram"])],
  [W(D, "Trouve le mot qui veut dire « puces » (électroniques).", "chips"), W(D, "Trouve le mot qui veut dire « investisseurs ».", "investors"),
   W(D, "Trouve le mot qui veut dire « échec ».", "failure"), W(D, "Trouve le mot qui veut dire « sièges sociaux ».", "headquarters")])

# ═════════ CITIES & STATES ═════════
F = "cu_villes_etats.html"
DZ(F, """
## New York, « the Big Apple »
Avec plus de 8 millions d'habitants, **New York City** est la plus grande ville des États-Unis. Elle compte cinq quartiers (**boroughs**) : Manhattan, Brooklyn, Queens, le Bronx et Staten Island. On y trouve la statue de la Liberté, l'Empire State Building, Times Square, Central Park, Broadway et Wall Street. C'est une ville-monde où l'on parle des centaines de langues. Sa devise officieuse : « la ville qui ne dort jamais ».

## La Californie, « the Golden State »
État le plus peuplé (près de 40 millions d'habitants), la **California** serait, si elle était un pays, l'une des plus grandes économies du monde. Elle abrite Hollywood, la Silicon Valley, des plages, des forêts de séquoias géants, la Vallée de la Mort. Elle est aussi exposée aux tremblements de terre (la faille de San Andreas) et aux incendies de forêt de plus en plus fréquents. Los Angeles et San Francisco, avec son pont du Golden Gate, en sont les villes les plus célèbres.

## Le Texas, « the Lone Star State »
Deuxième État par la superficie et la population, le **Texas** a été une république indépendante de 1836 à 1845, d'où l'étoile unique de son drapeau. Il est célèbre pour ses ranchs, ses cow-boys, son pétrole, son barbecue, ses rodéos et sa fierté locale (« *Don't mess with Texas* »). Houston abrite le centre de contrôle des missions de la NASA, Austin est un centre technologique et musical.

## La Floride, « the Sunshine State »
Avec son climat chaud, ses plages et ses parcs d'attractions comme **Walt Disney World** à Orlando, la **Florida** attire des millions de touristes et de retraités. Miami a une forte culture latino-américaine, notamment cubaine. Les marais des **Everglades** abritent des alligators. Les fusées décollent de Cap Canaveral. L'État est souvent frappé par des ouragans.

## Hawaï, « the Aloha State »
Archipel volcanique du Pacifique, **Hawaii** devient le 50e État en 1959. Peuplé d'abord par des Polynésiens, il fut un royaume indépendant jusqu'au renversement de sa reine en 1893 par des hommes d'affaires américains. C'est le berceau du surf, et le lieu de naissance de Barack Obama.

## Las Vegas, « Sin City »
Au milieu du désert du Nevada, **Las Vegas** s'est développée grâce à la légalisation des jeux d'argent en 1931 et au barrage Hoover voisin. Ses casinos géants, ses hôtels qui imitent Paris, Venise ou l'Égypte, ses spectacles et ses mariages express en font la capitale mondiale du divertissement. Son slogan : « *What happens in Vegas, stays in Vegas* ».

## Et aussi…
**Chicago**, « the Windy City », ville des gratte-ciel et du blues ; **New Orleans**, berceau du jazz, célèbre pour son Mardi Gras et durement frappée par l'ouragan Katrina en 2005 ; **Washington, D.C.**, la capitale fédérale ; ou **Seattle**, ville de Starbucks, d'Amazon et de Microsoft.
""", """
a city = une ville
a state = un État
a beach = une plage
a desert = un désert
a skyscraper = un gratte-ciel
an island = une île
a theme park = un parc d'attractions
a casino = un casino
""", [
 ("Combien de quartiers (boroughs) compte New York ?", ["Cinq", "Deux", "Cinquante"], ""),
 ("Quel est l'État le plus peuplé ?", ["La Californie", "Le Texas", "La Floride"], ""),
 ("Pourquoi le drapeau du Texas n'a-t-il qu'une étoile ?", ["Le Texas a été une république indépendante", "Il n'aime pas les étoiles", "C'est le premier État"], ""),
 ("Qui la Floride attire-t-elle particulièrement ?", ["Des touristes et des retraités", "Des skieurs", "Des mineurs"], ""),
 ("Que s'est-il passé à Hawaï en 1893 ?", ["Sa reine a été renversée par des hommes d'affaires américains", "Il est devenu un État", "Un volcan a explosé"], ""),
 ("Grâce à quoi Las Vegas s'est-elle développée ?", ["La légalisation des jeux d'argent et le barrage Hoover", "Le pétrole", "L'or"], ""),
], [("San Andreas", "grande faille géologique de Californie"), ("Cap Canaveral", "base de lancement de fusées"), ("Katrina", "ouragan qui a inondé La Nouvelle-Orléans")])
D = "vs"
culture(F, "Culture : American cities and states", 'Cities <span>&amp; states</span>',
  "Culture · New York, Californie, Texas, Floride, Hawaï, Las Vegas", ("#93c5fd", "#ca8a04"),
  reperes("Chaque État américain a son surnom et sa personnalité.",
    [("New York", "the Big Apple"), ("California", "the Golden State"), ("Texas", "the Lone Star State"), ("Florida", "the Sunshine State"),
     ("Hawaii", "the Aloha State, 50e État en 1959"), ("Las Vegas", "Sin City"), ("Chicago", "the Windy City")],
    "a city, a state, a nickname, a skyscraper, a beach, a desert, a theme park, a hurricane"),
  {D: doc("From the Big Apple to Sin City", [
    "New York, the \"Big Apple\", is the biggest city in the USA. It has the Statue of Liberty, Times Square, Central Park and many skyscrapers.",
    "California, the \"Golden State\", has the biggest population. It is famous for Hollywood, Silicon Valley and beautiful beaches, but also for earthquakes and forest fires.",
    "Texas, the \"Lone Star State\", is huge. It is famous for cowboys, oil and barbecue. It was an independent country from 1836 to 1845.",
    "Florida, the \"Sunshine State\", is hot and sunny. Millions of tourists visit Walt Disney World, and many retired people live there. Hawaii, in the Pacific Ocean, is the land of volcanoes and surfing.",
    "Las Vegas, in the desert of Nevada, is famous for its casinos and shows. People call it \"Sin City\"."])},
  [TF(D, "New York is the biggest city in the USA.", True, "« the biggest city in the USA »."),
   TF(D, "California has the biggest population.", True, "« the biggest population »."),
   TF(D, "Texas was never independent.", False, "« an independent country from 1836 to 1845 »."),
   TF(D, "Walt Disney World is in Florida.", True, "Florida… « Walt Disney World »."),
   TF(D, "Hawaii is in the Atlantic Ocean.", False, "« in the Pacific Ocean »."),
   TF(D, "Las Vegas is in a desert.", True, "« in the desert of Nevada »." )],
  [Q(D, "What is the nickname of New York?", ["The Big Apple.", "The Golden State.", "Sin City."]),
   Q(D, "What problems does California have?", ["Earthquakes and forest fires.", "Snow and ice.", "Volcanoes."]),
   Q(D, "What is Texas famous for?", ["Cowboys, oil and barbecue.", "Surfing.", "Casinos."]),
   Q(D, "Why do people call Las Vegas \"Sin City\"?", ["Because of its casinos and shows.", "Because it is very hot.", "Because it is old."])],
  [DT(D, "Quel État est surnommé « the Sunshine State » ?", ["La Floride", "La Californie", "Hawaï", "Le Texas"]),
   DT(D, "Quelle ville est surnommée « the Windy City » ?", ["Chicago", "New York", "Seattle", "Boston"]),
   DT(D, "Quand Hawaï devient-il un État ?", ["1959", "1893", "1776", "1945"]),
   DT(D, "Quel ouragan frappe La Nouvelle-Orléans en 2005 ?", ["Katrina", "Sandy", "Andrew", "Irma"])],
  [W(D, "Trouve le mot qui veut dire « gratte-ciel » (pluriel).", "skyscrapers"), W(D, "Trouve le mot qui veut dire « tremblements de terre ».", "earthquakes"),
   W(D, "Trouve le mot qui veut dire « immense ».", "huge"), W(D, "Trouve le mot qui veut dire « retraités » (2 mots).", ["retired people"])])
END()
