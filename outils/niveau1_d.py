import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
N1_ = {}

N1_["cu_guerre_secession.html"] = ("""
the North = le Nord
the South = le Sud
a factory = une usine
a railroad = un chemin de fer
a blockade = un blocus
an ironclad = un cuirassé
a general = un général
to surrender = se rendre, capituler
""", [
 ("Qui est le président de la Confédération ?", ["Jefferson Davis", "Abraham Lincoln", "Ulysses S. Grant"], ""),
 ("Quel était le grand avantage du Nord ?", ["Son industrie, ses chemins de fer et sa population", "Ses plantations de coton", "L'aide de la France"], ""),
 ("Sur quoi le Sud comptait-il ?", ["Ses bons généraux et l'aide du Royaume-Uni et de la France pour le coton", "Ses usines d'armes", "Sa marine"], ""),
 ("Qu'est-ce que le plan Anaconda ?", ["Étouffer le Sud par un blocus et le contrôle du Mississippi", "Une attaque surprise sur Washington", "Un traité de paix"], ""),
 ("Pourquoi la bataille de Hampton Roads est-elle célèbre ?", ["C'est le premier combat entre deux navires cuirassés", "C'est la dernière bataille de la guerre", "Lincoln y a été blessé"], ""),
 ("Que fait Sherman en 1864 ?", ["Il traverse la Géorgie en détruisant l'économie du Sud", "Il signe la paix", "Il libère Jefferson Davis"], "La « marche vers la mer »."),
])

N1_["cu_amerindiens_societe.html"] = ("""
a reservation = une réserve
poverty = la pauvreté
health = la santé
diabetes = le diabète
obesity = l'obésité
food = la nourriture
a city = une ville
hope = l'espoir
""", [
 ("Où vivent la plupart des Amérindiens aujourd'hui ?", ["Hors des réserves, souvent en ville", "Tous dans des réserves", "Au Canada"], "Environ 7 sur 10."),
 ("Quelle est la plus grande réserve ?", ["La Navajo Nation", "Standing Rock", "Manhattan"], ""),
 ("Quel écart d'espérance de vie avec la moyenne américaine ?", ["Environ 8 ans de moins", "Aucun", "10 ans de plus"], ""),
 ("Qu'est-ce qu'un « food desert » ?", ["Une zone où il est difficile de trouver des aliments frais", "Un désert de sable", "Un restaurant fermé"], ""),
 ("D'où vient le frybread ?", ["Des aliments distribués par le gouvernement : farine, sucre, saindoux", "D'une recette française", "D'un fast-food"], ""),
 ("Que demandent les jeunes Amérindiens ?", ["Qu'on arrête les clichés et qu'on les voie comme des citoyens d'aujourd'hui", "Qu'on construise des tipis", "Qu'on ferme les écoles"], ""),
])

N1_["cu_alaska.html"] = ("""
a bear = un ours
a glacier = un glacier
oil = le pétrole
gold = l'or
a dog = un chien
a sled = un traîneau
ice = la glace
the cold = le froid
""", [
 ("À qui les États-Unis ont-ils acheté l'Alaska ?", ["À la Russie", "Au Canada", "Au Royaume-Uni"], "En 1867."),
 ("Pourquoi appelait-on cet achat « Seward's Folly » ?", ["Beaucoup trouvaient que c'était une idée stupide", "Seward était fou", "Le prix était énorme"], ""),
 ("Que reçoit chaque habitant chaque année ?", ["Un chèque d'un fonds alimenté par le pétrole", "Un chien de traîneau", "Un billet d'avion"], ""),
 ("Que s'est-il passé en 1989 ?", ["La marée noire de l'Exxon Valdez", "La découverte de l'or", "L'achat de l'Alaska"], ""),
 ("Que commémore la course de l'Iditarod ?", ["Un relais de chiens qui a apporté un médicament à Nome en 1925", "La ruée vers l'or", "L'arrivée des Russes"], ""),
 ("Pourquoi certains villages doivent-ils déménager ?", ["Le permafrost dégèle et les côtes s'érodent", "Il y a trop de touristes", "Le pétrole les menace"], ""),
])

N1_["cu_lgbt.html"] = ("""
equality = l'égalité
a right = un droit
pride = la fierté
a flag = un drapeau
a law = une loi
marriage = le mariage
an ally = un allié
discrimination = la discrimination
""", [
 ("Que signifie « coming out » ?", ["Révéler son orientation ou son identité à son entourage", "Sortir le soir", "Quitter son pays"], ""),
 ("Pourquoi Oscar Wilde est-il condamné en 1895 ?", ["Pour sa relation avec un homme", "Pour vol", "Pour un livre"], ""),
 ("Que se passe-t-il au Stonewall Inn en 1969 ?", ["Les clients résistent à une descente de police : naissance des marches des fiertés", "Un concert célèbre", "La signature d'une loi"], ""),
 ("Qui a créé le drapeau arc-en-ciel ?", ["Gilbert Baker", "Harvey Milk", "Oscar Wilde"], ""),
 ("Que décide la Cour suprême américaine en 2015 ?", ["Le mariage pour les couples de même sexe dans tous les États", "L'interdiction des Pride", "La fin de l'armée"], ""),
 ("Qu'est-ce qu'un « ally » ?", ["Une personne qui soutient les personnes LGBTQ+", "Un drapeau", "Une loi"], ""),
])
