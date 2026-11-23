import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
exec(open(_EA_OUT+"/cuhelp.py", encoding="utf-8").read())

F = "cu_generations.html"
DZ(F, """
## Qu'est-ce qu'une « génération » ?
Aux États-Unis, on aime donner un nom aux **generations**, c'est-à-dire aux groupes de personnes nées à peu près à la même époque et qui ont vécu les mêmes grands événements pendant leur jeunesse. Les dates varient selon les auteurs ; celles qui suivent sont approximatives. Ces étiquettes sont pratiques mais aussi critiquées : elles créent des **stereotypes**, car tous les gens d'une même génération ne se ressemblent pas.

## La « Lost Generation »
La **Lost Generation** (la « génération perdue ») désigne les jeunes qui ont combattu ou grandi pendant la Première Guerre mondiale. L'expression est attribuée à l'écrivaine Gertrude Stein et popularisée par **Ernest Hemingway**. Dans les années 1920, plusieurs écrivains américains de cette génération vivent à Paris, comme Hemingway et **F. Scott Fitzgerald**, auteur de *The Great Gatsby* (1925), roman des Roaring Twenties.

## La « Greatest Generation » et la « Silent Generation »
La **Greatest Generation** (nés environ entre 1901 et 1927) a grandi pendant la Grande Dépression puis combattu pendant la Seconde Guerre mondiale. Le nom vient d'un livre du journaliste Tom Brokaw (1998). La **Silent Generation** (environ 1928-1945), enfants de la crise et de la guerre, a la réputation d'avoir été plus discrète et conformiste.

## La Beat Generation
La **Beat Generation** n'est pas une génération démographique, mais un mouvement littéraire et artistique des années 1950. Un petit groupe d'amis écrivains, rencontrés à New York, rejettent l'Amérique conformiste et matérialiste d'après-guerre : la vie en banlieue, le travail de bureau, la consommation. Ils cherchent la liberté dans la route, le **jazz**, la poésie, les drogues et les spiritualités orientales comme le bouddhisme.
- **Jack Kerouac** publie *On the Road* (1957), récit de voyages à travers l'Amérique avec son ami Neal Cassady, écrit d'un seul jet sur un long rouleau de papier.
- Le poète **Allen Ginsberg** lit *Howl* en 1955 à San Francisco ; le poème est poursuivi pour obscénité, mais un juge le déclare légal en 1957, une victoire pour la liberté d'expression.
- **William S. Burroughs** écrit *Naked Lunch* (1959), un roman expérimental.
Le mot « beat » veut dire à la fois « épuisé, vaincu » et évoque le rythme du jazz ; Kerouac y voyait aussi l'idée de « béatitude ». Les médias inventent le mot moqueur **beatnik** en 1958. La librairie City Lights à San Francisco devient leur lieu de rendez-vous. La Beat Generation a ouvert la voie aux **hippies** des années 1960 et influencé des artistes comme Bob Dylan.
[→ Voir aussi : la Route 66 et le road trip](cu_route66.html)

## Les Baby Boomers
Après 1945, les naissances explosent : c'est le **baby boom**. Les **Baby Boomers** (environ 1946-1964) grandissent dans une Amérique prospère, avec la télévision et le rock'n'roll. Jeunes, beaucoup participent aux grands mouvements des années 1960 : droits civiques, opposition à la guerre du Vietnam, mouvement hippie, festival de **Woodstock** (1969). Aujourd'hui, ils sont à la retraite ou proches de la retraite, et possèdent une grande part des richesses du pays.

## La Génération X
La **Generation X** (environ 1965-1980) tient son nom d'un roman du Canadien Douglas Coupland (1991). Moins nombreuse, elle a grandi avec la chaîne MTV, les premiers jeux vidéo et ordinateurs personnels, et souvent avec des parents qui travaillaient tous les deux ou divorcés : on parle des **latchkey kids**, enfants qui rentraient seuls de l'école avec la clé autour du cou.

## Les Millennials
Les **Millennials**, ou **Generation Y** (environ 1981-1996), sont devenus adultes autour de l'an 2000. Ils ont connu l'arrivée d'Internet, du téléphone portable et des réseaux sociaux, les attentats du 11 septembre 2001 et la crise économique de 2008. On les dit souvent endettés par leurs études et confrontés à des logements très chers.

## La Génération Z et la Génération Alpha
La **Generation Z** (environ 1997-2012), ou **Gen Z**, est la première génération de **digital natives** : elle a grandi avec un smartphone et les réseaux sociaux. Elle est souvent décrite comme très sensible au climat, à la santé mentale et à la diversité. En 2019, l'expression « ***OK boomer*** » devient virale : une réponse ironique des jeunes aux adultes qui critiquent leur génération.
La **Generation Alpha**, née à partir des années 2010, est celle des enfants des Millennials, qui grandissent avec les tablettes et l'intelligence artificielle. Vous en faites peut-être partie, ou vous êtes de la Gen Z !
""", """
a generation = une génération
young = jeune
old = vieux, âgé
a writer = un écrivain
a poem = un poème
a road = une route
a baby = un bébé
a smartphone = un smartphone
""", [
 ("Pourquoi les noms de générations sont-ils critiqués ?", ["Ils créent des stéréotypes", "Ils sont trop longs", "Ils sont en anglais"], ""),
 ("Qu'a vécu la « Lost Generation » ?", ["La Première Guerre mondiale", "Internet", "Le baby boom"], ""),
 ("Qu'est-ce que la Beat Generation ?", ["Un mouvement littéraire des années 1950 qui rejette le conformisme", "Une génération née après 2010", "Un groupe de rock"], ""),
 ("Quel livre de Jack Kerouac est la bible de la Beat Generation ?", ["On the Road (1957)", "The Great Gatsby", "Howl"], ""),
 ("Pourquoi parle-t-on de « baby boom » ?", ["Les naissances explosent après 1945", "Les bébés sont bruyants", "Une bombe explose"], ""),
 ("Qu'est-ce qu'un « digital native » ?", ["Quelqu'un qui a grandi avec le numérique", "Un Amérindien", "Un informaticien"], "C'est le cas de la Gen Z."),
], [("Gertrude Stein", "écrivaine américaine installée à Paris"), ("**Ernest Hemingway**", "romancier américain, prix Nobel 1954"), ("Tom Brokaw", "journaliste de télévision américain"),
    ("Neal Cassady", "ami de Kerouac, modèle du héros de On the Road"), ("City Lights", "librairie et maison d'édition de Lawrence Ferlinghetti"), ("Bob Dylan", "chanteur américain, prix Nobel de littérature 2016"),
    ("MTV", "chaîne de télévision musicale créée en 1981")])
D = "gn"
culture(F, "Culture : Beat Generation and other generations", 'Beat Generation <span>&amp; co</span>',
  "Culture · de la Lost Generation à la Gen Z", ("#fde68a", "#0f766e"),
  reperes("Les Américains donnent un nom à chaque génération. La Beat Generation, elle, est un mouvement littéraire des années 1950.",
    [("1914 – 1920s", "la Lost Generation (Hemingway, Fitzgerald)"), ("années 1950", "la Beat Generation : Kerouac, Ginsberg, Burroughs"), ("1946 – 1964", "les Baby Boomers"),
     ("1965 – 1980", "la Generation X"), ("1981 – 1996", "les Millennials (Gen Y)"), ("1997 – 2012", "la Gen Z, puis la Gen Alpha")],
    "a generation, the Beat Generation, a beatnik, a baby boomer, Gen X, a millennial, Gen Z, a digital native"),
  {D: doc("Talking about my generation", [
    "Americans like to give names to generations. A generation is a group of people born at about the same time.",
    "The Beat Generation was a group of American writers in the 1950s, like Jack Kerouac and Allen Ginsberg. They rejected the boring, conformist life of their time. They loved travelling, jazz and poetry. Kerouac's novel On the Road (1957) tells the story of journeys across America.",
    "After the Second World War, a lot of babies were born. This generation is called the Baby Boomers. When they were young, many of them protested against the Vietnam War.",
    "Then came Generation X, the Millennials and Generation Z. Gen Z grew up with smartphones and social media: they are \"digital natives\".",
    "These names are useful, but they also create stereotypes: not everybody in a generation is the same!"])},
  [TF(D, "A generation is a group of people born at about the same time.", True, "« born at about the same time »."),
   TF(D, "The Beat Generation was a group of writers in the 1950s.", True, "« in the 1950s »."),
   TF(D, "The Beat writers loved a conformist life.", False, "« They rejected the boring, conformist life »."),
   TF(D, "On the Road is a novel by Allen Ginsberg.", False, "C'est un roman de Jack Kerouac."),
   TF(D, "Gen Z grew up with smartphones.", True, "« grew up with smartphones »."),
   TF(D, "Everybody in a generation is the same.", False, "« not everybody in a generation is the same »." )],
  [Q(D, "What did the Beat writers love?", ["Travelling, jazz and poetry.", "Shopping and TV.", "Office work."]),
   Q(D, "What is On the Road about?", ["Journeys across America.", "A farm in Oklahoma.", "A war in Europe."]),
   Q(D, "Why are they called Baby Boomers?", ["A lot of babies were born after the war.", "They liked bombs.", "They were very loud."]),
   Q(D, "What is a digital native?", ["Someone who grew up with digital technology.", "An old computer.", "A Native American."])],
  [DT(D, "Qui a écrit le poème Howl ?", ["Allen Ginsberg", "Jack Kerouac", "Ernest Hemingway", "Bob Dylan"]),
   DT(D, "Comment les médias appellent-ils les membres de la Beat Generation ?", ["Les beatniks", "Les boomers", "Les hippies", "Les millennials"]),
   DT(D, "Quelle génération est née environ entre 1965 et 1980 ?", ["La Generation X", "La Gen Z", "La Silent Generation", "Les Baby Boomers"]),
   DT(D, "Quelle expression ironique devient virale en 2019 ?", ["« OK boomer »", "« Yes we can »", "« Make love not war »", "« Beat it »"])],
  [W(D, "Trouve le mot qui veut dire « ont rejeté ».", "rejected"), W(D, "Trouve le mot qui veut dire « voyages » (pluriel).", "journeys"),
   W(D, "Trouve le mot qui veut dire « ont manifesté ».", "protested"), W(D, "Trouve le mot qui veut dire « ont grandi » (2 mots).", ["grew up"])])
END()
