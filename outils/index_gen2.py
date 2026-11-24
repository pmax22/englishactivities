import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
import re, json, os, html as H, unicodedata
MC = json.load(open(_EA_OUT+"/mcount.json"))
REPO = _EA_REPO
SECTIONS = [("Grammaire", "Les formes : temps, verbes, noms, pronoms, adjectifs…"),
            ("Syntaxe", "Construire des phrases : questions, liens logiques, phrase complexe."),
            ("Lexique", "Le vocabulaire du quotidien et du métier."),
            ("Phonologie", "Prononcer : les sons, l'accent, l'API, la prosodie."),
            ("Sociolinguistique", "Adapter sa langue à la situation : registres, politesse, variétés d'anglais, expressions."),
            ("Pragmatique", "Agir avec la langue : demander, s'excuser, convaincre, comprendre l'implicite."),
            ("Culture", "Repères historiques, institutions et société du monde anglophone."),
            ("Compréhension", "Lire et écouter des documents, puis répondre à des questions."),
            ("Production", "Écrire et parler : écriture guidée, enregistrement, prononciation.")]
GR, SY, LE, PH, SO, PG, CU, CO, PR = (s[0] for s in SECTIONS)
FAMS = [("Linguistique", "Compétence linguistique", [GR, SY, LE, PH]), ("Sociolinguistique", "Compétence sociolinguistique", [SO]),
        ("Pragmatique", "Compétence pragmatique", [PG]), ("Culturelle", "Compétence culturelle", [CU]),
        ("Comprendre & produire", "Activités langagières", [CO, PR])]
FAM_OF = {sec: f for f, _, secs in FAMS for sec in secs}
CAP = "CAP Sapver"

# (fichier, section, couleurs, grand mot, badge, catégorie, titre, description, pastilles, thèmes, mots-clés)
A = [
 # ── Grammaire ──
 ("be_have_play.html", GR, "#f87171", "#dc2626", "Be", "is · has · plays", "Grammaire · Conjugaison", "Be, Have & Play", "Conjuguer be, have et play au présent : formes affirmative, négative et interrogative.", ["am / is / are", "doesn't", "Does?"], ["Présent"], "etre avoir jouer"),
 ("present_simple.html", GR, "#38bdf8", "#0284c7", "Every day", "he works", "Grammaire · Temps", "Le présent simple", "Habitudes et vérités générales : le -s de la 3e personne, don't / doesn't, Do / Does.", ["-s / -es", "doesn't", "Does?"], ["Présent"], "present simple habitude"),
 ("present_continu.html", GR, "#22d3ee", "#0891b2", "Now", "I am reading", "Grammaire · Temps", "Le présent be + -ing", "Ce qui se passe en ce moment : am / is / are + verbe-ing, et la différence avec le présent simple.", ["be + -ing", "now", "simple / -ing"], ["Présent"], "present continu progressif ing"),
 ("adverbes_frequence.html", GR, "#fb923c", "#ea580c", "Often", "always → never", "Grammaire · Adverbes", "Adverbes de fréquence", "always, usually, often, sometimes, rarely, never : sens, place dans la phrase et How often?", ["always", "sometimes", "never"], ["Présent", "Adjectifs & adverbes"], "frequence how often"),
 ("preterit.html", GR, "#f5c842", "#e07b3f", "Past", "Prétérit simple", "Grammaire · Temps", "Le Prétérit", "Phrases affirmatives, négatives et interrogatives au prétérit simple — réguliers et irréguliers.", ["Affirmatif", "Négatif", "Interrogatif"], ["Passé"], "preterit passe did"),
 ("verbe_regulier_irregulier.html", GR, "#4ecb7f", "#2da866", "Reg?", "Identification", "Grammaire · Verbes", "Régulier ou Irrégulier ?", "Régulier ou irrégulier ? Base verbale, orthographe du -ED, formes irrégulières et intrus.", ["-ed / -ied", "Irréguliers", "Intrus"], ["Passé"], "verbes irreguliers preterit"),
 ("preterit_continu.html", GR, "#facc15", "#ca8a04", "Was -ing", "I was sleeping", "Grammaire · Temps", "Le prétérit be + -ing", "Ce qui était en train de se passer : was / were + verbe-ing, avec when et while.", ["was / were", "when", "while"], ["Passé"], "preterit continu progressif"),
 ("used_to.html", GR, "#7c6af7", "#b47cf0", "Used", "Habitudes passées", "Grammaire · Aspect", "Used To", "Exprimer des habitudes et états passés révolus — formes affirmative, négative et interrogative.", ["used to", "didn't use to", "Did … use to?"], ["Passé"], "habitude passee"),
 ("present_perfect.html", GR, "#f472b6", "#db2777", "Have done", "for · since", "Grammaire · Temps", "Le present perfect", "have / has + participe passé, for / since, ever / never, et la différence avec le prétérit.", ["have done", "for / since", "ever"], ["Passé"], "present perfect participe"),
 ("present_perfect_continu.html", GR, "#f0abfc", "#d946ef", "Been -ing", "I've been waiting", "Grammaire · Temps", "Present perfect be + -ing", "have / has been + verbe-ing : insister sur la durée, et la différence avec le present perfect simple.", ["been + -ing", "for / since", "durée"], ["Passé"], "present perfect continu progressif"),
 ("past_perfect.html", GR, "#fda4af", "#f43f5e", "Had done", "l'action d'avant", "Grammaire · Temps", "Le past perfect", "had + participe passé : l'action antérieure à une autre action passée.", ["had + PP", "already", "before"], ["Passé"], "plus que parfait past perfect"),
 ("futur.html", GR, "#a78bfa", "#7c3aed", "Will", "going to", "Grammaire · Temps", "Le futur", "will ou be going to ? Prédictions, promesses, décisions et projets.", ["will", "won't", "going to"], ["Futur"], "futur will going to"),
 ("modaux.html", GR, "#818cf8", "#4f46e5", "Can", "must · should", "Grammaire · Modaux", "Les modaux", "can, must, mustn't, should, have to, don't have to : capacité, obligation, interdiction, conseil.", ["can", "must", "should"], ["Verbes & modaux"], "modaux obligation conseil"),
 ("probabilite.html", GR, "#a5f3fc", "#22d3ee", "Might", "must · can't", "Grammaire · Modaux", "may, might, must, can't", "Exprimer la probabilité, et les modaux au passé : should have, must have, could have.", ["may / might", "must", "should have"], ["Verbes & modaux"], "probabilite modaux passe"),
 ("imperatif.html", GR, "#4ade80", "#16a34a", "Go!", "Don't · Let's", "Grammaire · Verbes", "L'impératif", "Donner un ordre ou un conseil : base verbale, Don't + BV, Let's + BV.", ["BV", "Don't", "Let's"], ["Verbes & modaux"], "imperatif ordre consigne"),
 ("like_ing.html", GR, "#f9a8d4", "#ec4899", "Like", "I love playing", "Grammaire · Verbes", "Exprimer ses goûts", "love, like, enjoy, don't mind, hate + verbe-ing.", ["love / like", "hate", "+ -ing"], ["Verbes & modaux"], "gouts aimer detester ing"),
 ("verbes_to_ing.html", GR, "#fdba74", "#fb923c", "To / -ing", "want to · enjoy -ing", "Grammaire · Verbes", "Verbe + to ou -ing", "want to go, enjoy swimming : quel verbe est suivi de to + BV, lequel de -ing ?", ["want to", "enjoy -ing", "after -ing"], ["Verbes & modaux"], "infinitif gerondif"),
 ("pronoms_personnels.html", GR, "#60a5fa", "#2563eb", "I · me", "he → him", "Grammaire · Pronoms", "Pronoms personnels", "Pronoms sujets et compléments : I / me, he / him, they / them…", ["Sujet", "Complément", "Traduction"], ["Noms & pronoms"], "pronoms sujet complement"),
 ("pronoms_reflechis.html", GR, "#7dd3fc", "#0ea5e9", "Myself", "each other", "Grammaire · Pronoms", "Les pronoms réfléchis", "myself, yourself, themselves… et each other.", ["myself", "themselves", "each other"], ["Noms & pronoms"], "reflechis"),
 ("possessifs.html", GR, "#fb7185", "#e11d48", "Tom's", "my · his · mine", "Grammaire · Possession", "Les possessifs", "my, your, his, her… · le cas possessif 's · mine, yours, hers…", ["my / his", "'s", "mine"], ["Noms & pronoms"], "possessifs genitif"),
 ("demonstratifs.html", GR, "#fca5a5", "#ef4444", "This", "these · those", "Grammaire · Déterminants", "Les démonstratifs", "this, that, these, those : proche ou loin, singulier ou pluriel.", ["this / that", "these", "those"], ["Noms & pronoms"], "demonstratifs ce cette ces"),
 ("articles.html", GR, "#a3e635", "#65a30d", "a / an", "the · Ø", "Grammaire · Articles", "Les articles", "a, an, the ou pas d'article ? Son voyelle, chose précise, généralités, sports, langues…", ["a / an", "the", "Ø"], ["Noms & pronoms"], "articles a an the"),
 ("pluriels.html", GR, "#fde68a", "#f59e0b", "Children", "-es · -ies · -ves", "Grammaire · Noms", "Le pluriel des noms", "-s, -es, -ies, -ves et les pluriels irréguliers : children, feet, mice…", ["-es / -ies", "-ves", "irréguliers"], ["Noms & pronoms"], "pluriel noms irreguliers"),
 ("there_is.html", GR, "#fbbf24", "#d97706", "There", "is · are", "Grammaire · Groupe nominal", "There is / There are", "Il y a… : is ou are, some ou any, questions et négations.", ["is / are", "some / any", "Is there?"], ["Noms & pronoms"], "il y a some any"),
 ("denombrables.html", GR, "#c4b5fd", "#8b5cf6", "Much?", "many · a lot of", "Grammaire · Quantités", "much, many, a lot of", "Dénombrables et indénombrables : much / many, How much / How many, a few / a little.", ["much / many", "How much?", "a few"], ["Noms & pronoms"], "denombrable quantite"),
 ("someone_anything.html", GR, "#fcd34d", "#eab308", "Someone", "anything · nobody", "Grammaire · Pronoms", "someone, anything, nobody…", "Les composés de some, any, no et every : quelqu'un, rien, partout…", ["some-", "any-", "no- / every-"], ["Noms & pronoms"], "quelqu un rien personne"),
 ("adjectifs.html", GR, "#e879f9", "#c026d3", "Adj.", "a nice sister", "Grammaire · Adjectifs", "Les adjectifs", "Niveau 1 : la place de l'adjectif · Niveau 2 : l'ordre des adjectifs (opinion, taille, âge…).", ["Place", "Invariable", "Ordre"], ["Adjectifs & adverbes"], "adjectifs ordre"),
 ("adverbes_maniere.html", GR, "#86efac", "#22c55e", "Quickly", "good → well", "Grammaire · Adverbes", "Les adverbes de manière", "quick → quickly, good → well : former l'adverbe et le distinguer de l'adjectif.", ["-ly", "well", "adj / adv"], ["Adjectifs & adverbes"], "adverbes maniere ly"),
 ("too_enough.html", GR, "#bef264", "#84cc16", "Too", "enough · so · such", "Grammaire · Degré", "too, enough, so, such", "Trop, assez, si, tellement : leur sens et leur place dans la phrase.", ["too", "enough", "so / such"], ["Adjectifs & adverbes"], "trop assez tellement"),
 ("comparatif.html", GR, "#3ecfcf", "#2fa8d8", "Comp", "Comparatif", "Grammaire · Comparaison", "Le Comparatif", "Comparer des personnes, objets ou situations — formes supérieure, inférieure et égale.", ["-er / more", "less", "as … as"], ["Comparer"], "comparatif than"),
 ("superlatif.html", GR, "#2dd4bf", "#0d9488", "Best", "the tallest", "Grammaire · Comparaison", "Le superlatif", "the -est, the most…, the best / the worst — et la différence avec le comparatif.", ["the -est", "the most", "best"], ["Comparer"], "superlatif most est"),
 ("prepositions.html", GR, "#34d399", "#059669", "in · on · at", "temps et lieu", "Grammaire · Prépositions", "in, on, at", "Les prépositions de temps (at 7, on Monday, in July) et de lieu (at school, on the table, in Paris).", ["Temps", "Lieu", "in / on / at"], ["Prépositions"], "prepositions"),
 ("preterit_cap_sapver.html", GR, "#4ec9f5", "#3f7ee0", "Past", "Prétérit simple", "CAP Sapver · Temps", "Prétérit — Vente & Aide", "Prétérit simple orienté vente et aide à la personne — verbes métiers, vocabulaire professionnel.", ["Affirmatif", "Négatif", "Interrogatif"], ["Passé", CAP], "cap sapver vente preterit"),
 # ── Syntaxe ──
 ("questions_fermees.html", SY, "#ff9f43", "#e8603c", "Did?", "Yes, I did / No, I didn't", "Syntaxe · Questions", "Questions fermées", "Traduire des questions en Did + sujet + BV, puis compléter les réponses affirmatives et négatives.", ["Did + BV", "didn't + BV", "Prétérit"], ["Questions"], "did you questions fermees"),
 ("questions_ouvertes.html", SY, "#f06fa4", "#c44d8a", "Wh-?", "When · Where · Who · How", "Syntaxe · Questions", "Questions ouvertes", "Pronoms interrogatifs, ordre des mots, traduction — et raconter ses dernières vacances.", ["Wh- + did", "How long", "Sum up"], ["Questions"], "when where who what how vacances"),
 ("questions_sujet.html", SY, "#f9a8d4", "#f472b6", "Who?", "called / did you call", "Syntaxe · Questions", "Questions sur le sujet", "Who called you? ou Who did you call? Avec ou sans did selon la fonction du mot interrogatif.", ["Who + verbe", "Who did…?", "What?"], ["Questions"], "question sujet objet"),
 ("question_tags.html", SY, "#c4b5fd", "#a78bfa", "…isn't it?", "tags", "Syntaxe · Questions", "Les question tags", "It's cold, isn't it? · You like pizza, don't you? : la petite question de fin de phrase.", ["isn't it", "don't you", "can't she"], ["Questions"], "question tags n est ce pas"),
 ("exclamatives.html", SY, "#fcd34d", "#f59e0b", "What a…!", "How nice!", "Syntaxe · Exclamatives", "Les exclamatives", "What a beautiful day! How nice! So / such : construire une exclamation.", ["What a", "How", "so / such"], ["Phrase complexe"], "exclamation"),
 ("connecteurs.html", SY, "#93c5fd", "#60a5fa", "But", "because · so", "Syntaxe · Liens logiques", "Les connecteurs", "and, but, because, so, although, however, first, then… : relier ses idées.", ["because", "so", "although"], ["Liens logiques"], "connecteurs mots de liaison"),
 ("relatifs.html", SY, "#67e8f9", "#06b6d4", "Who?", "which · where", "Syntaxe · Phrase complexe", "Les pronoms relatifs", "who, which, that, where, whose : relier deux phrases.", ["who", "which", "where"], ["Phrase complexe"], "relatifs qui que ou"),
 ("subordonnees_temps.html", SY, "#99f6e4", "#2dd4bf", "When I…", "+ présent", "Syntaxe · Phrase complexe", "when + présent", "When I arrive, I'll call you : when, as soon as, until + présent pour parler du futur.", ["when", "as soon as", "until"], ["Phrase complexe", "Liens logiques"], "subordonnee temps futur"),
 ("conditionnel.html", SY, "#fdba74", "#f97316", "If…", "will · would", "Syntaxe · Phrase complexe", "Le conditionnel", "Type 1 : If + présent, will · Type 2 : If + prétérit, would · Type 3 : If + had, would have.", ["Type 1", "Type 2", "Type 3"], ["Phrase complexe"], "if conditionnel would"),
 ("passif.html", SY, "#a5b4fc", "#6366f1", "Made", "is made · was built", "Syntaxe · Phrase complexe", "Le passif", "be + participe passé, au présent et au prétérit, avec by.", ["be + PP", "by", "actif / passif"], ["Phrase complexe"], "passif participe"),
 ("discours_indirect.html", SY, "#d8b4fe", "#a855f7", "He said", "said · told", "Syntaxe · Phrase complexe", "Le discours indirect", "Rapporter des paroles : say ou tell, et la concordance des temps.", ["say / tell", "was / would", "pronoms"], ["Phrase complexe"], "discours indirect rapporte"),
 # ── Lexique ──
 ("se_presenter.html", LE, "#fde047", "#facc15", "Hello!", "My name is…", "Lexique · Communication", "Se présenter", "Dire son nom, son âge, où on habite, ses goûts, et poser les mêmes questions.", ["What's your name?", "I'm 15", "I live in"], ["Vie quotidienne"], "presentation"),
 ("famille.html", LE, "#fda4af", "#fb7185", "Family", "aunt · nephew", "Lexique · Famille", "La famille", "mother, uncle, cousin, niece… et les liens de parenté.", ["Vocabulaire", "Écoute", "Qui est-ce ?"], ["Vie quotidienne"], "famille parents"),
 ("meteo.html", LE, "#7dd3fc", "#38bdf8", "Sunny", "It's raining", "Lexique · Météo", "La météo et les saisons", "What's the weather like? sunny, rainy, windy… et les quatre saisons.", ["Météo", "Saisons", "Écoute"], ["Vie quotidienne"], "meteo temps saisons"),
 ("nourriture.html", LE, "#fdba74", "#f97316", "Food", "breakfast · lunch", "Lexique · Nourriture", "La nourriture", "Aliments, boissons, repas, et commander au restaurant.", ["Aliments", "Repas", "Restaurant"], ["Vie quotidienne"], "nourriture aliments restaurant"),
 ("vetements.html", LE, "#f0abfc", "#e879f9", "Clothes", "T-shirt · dress", "Lexique · Vêtements", "Les vêtements", "T-shirt, jumper, trousers… et wear, put on, take off, try on.", ["Vocabulaire", "Écoute", "try on"], ["Vie quotidienne", CAP], "vetements habits"),
 ("maison.html", LE, "#d9f99d", "#a3e635", "Home", "kitchen · bedroom", "Lexique · Maison", "La maison", "Les pièces, les meubles et les objets de la maison.", ["Pièces", "Meubles", "Écoute"], ["Vie quotidienne"], "maison pieces meubles"),
 ("metiers.html", LE, "#a5b4fc", "#818cf8", "Jobs", "nurse · baker", "Lexique · Métiers", "Les métiers", "doctor, nurse, baker, mechanic… et où ils travaillent.", ["Vocabulaire", "Écoute", "Lieux"], ["Monde du travail"], "metiers professions"),
 ("heure_dates.html", LE, "#93c5fd", "#3b82f6", "7:30", "half past seven", "Lexique · Repères", "Heure, dates et nombres", "Dire l'heure, les dates (the third of May), les nombres et les prix.", ["L'heure", "Les dates", "Les prix"], ["Vie quotidienne"], "heure date nombre ordinal prix"),
 ("phrasal_verbs.html", LE, "#fcd34d", "#fbbf24", "Get up", "look for · give up", "Lexique · Verbes", "Les phrasal verbs", "get up, look for, look after, give up, try on… : verbe + particule.", ["get up", "look for", "give up"], ["Vie quotidienne"], "verbes a particule phrasal"),
 ("cap_vente.html", LE, "#5eead4", "#14b8a6", "Shop", "Can I help you?", "CAP Sapver · Vente", "L'anglais de la vente", "Accueillir, conseiller, encaisser, téléphoner : les phrases utiles au magasin.", ["Accueil", "Caisse", "Téléphone"], ["Monde du travail", CAP], "cap sapver vente client magasin"),
 ("cap_aide.html", LE, "#99f6e4", "#5eead4", "Care", "How do you feel?", "CAP Sapver · Aide à la personne", "L'anglais de l'aide à la personne", "Le corps, la santé, les consignes et les questions pour aider et rassurer.", ["Le corps", "La santé", "Consignes"], ["Monde du travail", CAP], "cap sapver aide personne sante corps"),
 ("cap_ecrit_entretien.html", LE, "#bae6fd", "#7dd3fc", "Dear…", "Yours sincerely", "CAP Sapver · Emploi", "E-mail et entretien d'embauche", "Écrire un e-mail professionnel et répondre aux questions d'un entretien.", ["E-mail", "Entretien", "Qualités"], ["Monde du travail", CAP], "cap sapver mail cv entretien embauche"),
 # ── Phonologie ──
 ("phono_ed.html", PH, "#fca5a5", "#f87171", "/ɪd/", "/t/ · /d/", "Phonologie · Sons", "Prononcer le -ED", "worked /t/, played /d/, wanted /ɪd/ : écoute et classe les verbes.", ["/t/", "/d/", "/ɪd/"], ["Sons"], "prononciation ed preterit"),
 ("phono_s.html", PH, "#fdba74", "#fb923c", "/ɪz/", "/s/ · /z/", "Phonologie · Sons", "Prononcer le -S", "cats /s/, dogs /z/, buses /ɪz/ : pluriels et 3e personne.", ["/s/", "/z/", "/ɪz/"], ["Sons"], "prononciation s pluriel"),
 ("accent_mot.html", PH, "#c4b5fd", "#a78bfa", "TEA-cher", "ho-TEL", "Phonologie · Accent", "L'accent de mot", "Quelle syllabe est accentuée ? Écoute, choisis et répète.", ["2 syllabes", "3 syllabes", "Écoute"], ["Accent"], "accent tonique syllabe"),
 ("lettres_muettes.html", PH, "#86efac", "#4ade80", "Knife", "k · w · h", "Phonologie · Sons", "Les lettres muettes", "knife, write, hour, island : les lettres qu'on écrit mais qu'on ne prononce pas.", ["k", "w", "h"], ["Sons"], "lettres muettes prononciation"),
 ("so_neither.html", SY, "#f9a8d4", "#ec4899", "So do I", "Neither do I", "Syntaxe · Réponses", "So do I / Neither do I", "Dire « moi aussi » et « moi non plus » en reprenant le bon auxiliaire.", ["So do I", "Neither am I", "So can I"], ["Questions"], "moi aussi moi non plus"),
 ("questions_indirectes.html", SY, "#bfdbfe", "#93c5fd", "Can you…", "tell me where…", "Syntaxe · Questions", "Les questions indirectes", "Can you tell me where the station is? : poser une question polie sans inversion.", ["Can you tell me", "Do you know", "if"], ["Questions"], "question indirecte polie"),
 ("causatif.html", SY, "#fed7aa", "#fb923c", "Have it done", "make · let", "Syntaxe · Causatif", "Le causatif", "have something done, make someone do, let someone do : faire faire, obliger, laisser.", ["have done", "make", "let"], ["Phrase complexe"], "causatif faire faire"),
 ("both_either.html", GR, "#a7f3d0", "#34d399", "Both", "either · neither", "Grammaire · Quantifieurs", "both, either, neither", "Les deux, l'un ou l'autre, aucun des deux : both… and, either… or, neither… nor.", ["both", "either", "neither"], ["Noms & pronoms"], "les deux aucun"),
 ("ago_for_since.html", GR, "#fde68a", "#fbbf24", "Ago", "for · since", "Grammaire · Temps", "ago, for, since", "Il y a, pendant, depuis : ne plus confondre ago, for et since.", ["ago", "for", "since"], ["Passé"], "il y a depuis pendant"),
 ("be_used_to.html", GR, "#ddd6fe", "#a78bfa", "Used to", "be used to -ing", "Grammaire · Verbes", "used to / be used to", "Habitude passée (used to + BV) ou être habitué à (be used to + -ing) ?", ["used to", "be used to", "get used to"], ["Verbes & modaux"], "habitue"),
 ("wish.html", GR, "#fbcfe8", "#f472b6", "I wish", "If only…", "Grammaire · Verbes", "wish / if only", "Exprimer un souhait ou un regret : wish + prétérit, wish + past perfect.", ["wish", "if only", "were"], ["Verbes & modaux"], "souhait regret"),
 ("futur_ing.html", GR, "#c4b5fd", "#8b5cf6", "Meeting", "tomorrow", "Grammaire · Temps", "Le présent be + -ing pour le futur", "I'm meeting Tom tomorrow : les rendez-vous et projets organisés.", ["be + -ing", "going to", "will"], ["Futur"], "futur proche rendez vous"),
 ("faux_amis.html", LE, "#fecaca", "#f87171", "Actually", "≠ actuellement", "Lexique · Pièges", "Les faux amis", "actually, library, sensible, to attend… : les mots qui ressemblent au français mais trompent.", ["actually", "library", "sensible"], ["Vie quotidienne"], "faux amis pieges"),
 ("ville_directions.html", LE, "#bbf7d0", "#4ade80", "Turn left", "where is…?", "Lexique · Ville", "La ville et les directions", "Les lieux de la ville, demander et indiquer son chemin.", ["Lieux", "Directions", "Excuse me"], ["Vie quotidienne"], "ville chemin directions"),
 ("ecole.html", LE, "#fef08a", "#facc15", "School", "ruler · rubber", "Lexique · École", "L'école", "Matières, lieux et objets de l'école.", ["Matières", "Objets", "Écoute"], ["Vie quotidienne"], "ecole classe matieres"),
 ("loisirs_sports.html", LE, "#fdba74", "#fb923c", "Sports", "play · do · go", "Lexique · Loisirs", "Les loisirs et les sports", "Sports, loisirs, et quand utiliser play, do ou go.", ["Sports", "Loisirs", "play / do / go"], ["Vie quotidienne"], "loisirs sports"),
 ("transports.html", LE, "#93c5fd", "#3b82f6", "By train", "on foot", "Lexique · Transports", "Les transports", "Les moyens de transport et le vocabulaire du voyage.", ["Transports", "Voyage", "by / on"], ["Vie quotidienne"], "transports voyage"),
 ("emotions.html", LE, "#fbcfe8", "#ec4899", "Happy", "bored · boring", "Lexique · Émotions", "Les émotions et la personnalité", "happy, angry, worried, shy, lazy… et bored ou boring ?", ["Émotions", "Caractère", "-ed / -ing"], ["Vie quotidienne"], "emotions sentiments caractere"),
 ("animaux.html", LE, "#bbf7d0", "#22c55e", "Animals", "cow · monkey", "Lexique · Animaux", "Les animaux", "Animaux domestiques, de la ferme et sauvages.", ["Domestiques", "Ferme", "Sauvages"], ["Vie quotidienne"], "animaux"),
 ("argent_shopping.html", LE, "#86efac", "#16a34a", "£", "How much?", "Lexique · Achats", "L'argent et le shopping", "L'argent, les magasins et les phrases utiles pour acheter.", ["Argent", "Magasins", "How much?"], ["Vie quotidienne", "Monde du travail"], "argent shopping achats"),
 ("phono_th.html", PH, "#fcd34d", "#f59e0b", "TH", "think · this", "Phonologie · Sons", "Prononcer le TH", "/θ/ comme dans think, /ð/ comme dans this… et think ou sink ?", ["/θ/", "/ð/", "think / sink"], ["Sons"], "prononciation th"),
 ("phono_voyelles.html", PH, "#a5f3fc", "#06b6d4", "Ship", "sheep", "Phonologie · Sons", "Voyelles longues et courtes", "ship ou sheep ? full ou fool ? La longueur des voyelles change le sens.", ["ship / sheep", "full / fool", "Écoute"], ["Sons"], "voyelles longues courtes"),
 ("phono_h.html", PH, "#fecdd3", "#fb7185", "Hat", "at", "Phonologie · Sons", "Le H aspiré", "hat ou at ? heat ou eat ? Prononcer le h, et les h muets.", ["hat / at", "h muet", "Écoute"], ["Sons"], "h aspire"),
 ("intonation.html", PH, "#ddd6fe", "#8b5cf6", "↗ ↘", "la mélodie", "Phonologie · Intonation", "L'intonation", "Intonation montante ou descendante selon le type de phrase.", ["↗ yes / no", "↘ wh-", "Écoute"], ["Accent"], "intonation melodie"),
 ("formes_faibles.html", PH, "#e9d5ff", "#c084fc", "/ə/", "can · to · and", "Phonologie · Rythme", "Les formes faibles", "can /kən/, to /tə/, and /ən/ : les petits mots qu'on prononce à peine.", ["/ə/", "can / to", "forte / faible"], ["Accent"], "formes faibles schwa"),
 ("ce_famille.html", CO, "#fde68a", "#f59e0b", "Read", "Meet the Parkers", "Compréhension écrite", "Meet the Parkers", "Un texte court sur une famille anglaise : vrai / faux, questions, vocabulaire.", ["Vrai / faux", "Questions", "Vocabulaire"], ["Lecture"], "comprehension ecrite texte famille"),
 ("ce_vendeuse.html", CO, "#99f6e4", "#14b8a6", "Read", "A day at the shop", "Compréhension écrite", "A day at the shop", "La journée d'une jeune vendeuse à Manchester.", ["Vrai / faux", "Questions", "Vocabulaire"], ["Lecture", CAP], "comprehension ecrite vendeuse magasin"),
 ("ce_londres.html", CO, "#bfdbfe", "#3b82f6", "Read", "A weekend in London", "Compréhension écrite", "A weekend in London", "Le récit d'un voyage scolaire à Londres, au prétérit.", ["Vrai / faux", "Questions", "Vocabulaire"], ["Lecture"], "comprehension ecrite londres voyage"),
 ("co_magasin.html", CO, "#5eead4", "#0d9488", "Listen", "In a clothes shop", "Compréhension orale", "In a clothes shop", "Un dialogue entre une vendeuse et une cliente.", ["Dialogue", "Vrai / faux", "Questions"], ["Écoute", CAP], "comprehension orale dialogue magasin"),
 ("co_message.html", CO, "#c7d2fe", "#6366f1", "Listen", "A phone message", "Compréhension orale", "A phone message", "Un message sur répondeur d'une maison de retraite : dates, heures, numéros.", ["Message", "Chiffres", "Questions"], ["Écoute", CAP], "comprehension orale telephone message"),
 ("co_annonces.html", CO, "#fecaca", "#ef4444", "Listen", "Station & weather", "Compréhension orale", "Station & weather", "Une annonce en gare et un bulletin météo.", ["Annonce", "Météo", "Questions"], ["Écoute"], "comprehension orale gare meteo"),

 ("cu_uk.html", CU, "#93c5fd", "#1d4ed8", "UK", "4 nations", "Culture · Royaume-Uni", "The United Kingdom", "Quatre nations, quatre capitales, le drapeau, la langue : les bases.", ["Nations", "Drapeau", "Capitales"], [], "culture royaume-uni uk angleterre ecosse galles union jack"),
 ("cu_monarchie.html", CU, "#fde68a", "#b45309", "The Crown", "Charles III", "Culture · Royaume-Uni", "The Royal Family", "De Henry VIII à Charles III : rois, reines et monarchie constitutionnelle.", ["Rois", "Reines", "Rôle"], [], "culture monarchie roi reine royal family elizabeth charles"),
 ("cu_institutions_uk.html", CU, "#a7f3d0", "#047857", "Westminster", "MPs · PM", "Culture · Royaume-Uni", "How the UK is governed", "Parlement, Premier ministre, élections, dévolution.", ["Parlement", "Élections", "Partis"], [], "culture institutions parlement westminster premier ministre elections"),
 ("cu_empire.html", CU, "#fca5a5", "#b91c1c", "Empire", "dominions", "Culture · Royaume-Uni", "From Empire to Commonwealth", "L'Empire britannique, les dominions, la décolonisation, le Windrush.", ["Empire", "Dominions", "Commonwealth"], [], "culture empire colonies dominions commonwealth windrush decolonisation inde canada australie"),
 ("cu_brexit.html", CU, "#c7d2fe", "#4338ca", "Brexit", "Leave · Remain", "Culture · Royaume-Uni", "Brexit", "Le référendum de 2016, les arguments, la frontière irlandaise, les conséquences.", ["Référendum", "Arguments", "Conséquences"], [], "culture brexit union europeenne referendum leave remain"),
 ("cu_famine.html", CU, "#bbf7d0", "#15803d", "1845", "Great Famine", "Culture · Irlande", "The Great Famine", "La Grande Famine irlandaise : mildiou, faim, émigration, diaspora.", ["Famine", "Émigration", "Diaspora"], [], "culture irlande grande famine pomme de terre emigration diaspora"),
 ("cu_troubles.html", CU, "#fed7aa", "#c2410c", "Troubles", "Bloody Sunday", "Culture · Irlande du Nord", "Northern Ireland & the Troubles", "Bloody Sunday, blanket et dirty protests, grèves de la faim, accord du Vendredi saint.", ["Bloody Sunday", "H-Blocks", "Paix"], [], "culture irlande du nord troubles bloody sunday dirty protest blanket greve de la faim bobby sands good friday"),
 ("cu_usa.html", CU, "#bfdbfe", "#1e40af", "USA", "50 states", "Culture · États-Unis", "The United States", "50 États, la capitale, le drapeau, l'indépendance : les bases.", ["États", "Drapeau", "4 juillet"], [], "culture etats-unis usa amerique drapeau independance"),
 ("cu_institutions_us.html", CU, "#fecdd3", "#be123c", "We the People", "checks & balances", "Culture · États-Unis", "How the USA is governed", "Constitution, Congrès, Président, Cour suprême, élections.", ["Constitution", "Congrès", "Président"], [], "culture institutions constitution congres president cour supreme elections"),
 ("cu_manifest_destiny.html", CU, "#fcd34d", "#a16207", "Go West", "Manifest Destiny", "Culture · États-Unis", "Manifest Destiny", "La conquête de l'Ouest, la ruée vers l'or, la Piste des larmes, Wounded Knee.", ["Ouest", "Frontière", "Amérindiens"], [], "culture manifest destiny conquete ouest frontiere amerindiens trail of tears ruee vers l'or"),
 ("cu_red_scare.html", CU, "#fecaca", "#991b1b", "Red Scare", "witch hunt", "Culture · États-Unis", "The Red Scare", "La peur du communisme, McCarthy, Hollywood, The Crucible.", ["Guerre froide", "McCarthy", "Hollywood"], [], "culture red scare maccarthysme mccarthy communisme guerre froide chasse aux sorcieres"),
 ("cu_watergate.html", CU, "#ddd6fe", "#6d28d9", "Watergate", "1972 – 1974", "Culture · États-Unis", "The Watergate scandal", "Le cambriolage, les journalistes, les bandes, la démission de Nixon.", ["Nixon", "Presse", "Démission"], [], "culture watergate nixon scandale journalisme washington post"),
 ("cu_televangelisme.html", CU, "#fef08a", "#ca8a04", "Faith & TV", "televangelists", "Culture · États-Unis", "Televangelism", "Religion, télévision et politique : Billy Graham, la Moral Majority, les scandales.", ["Religion", "Télévision", "Politique"], [], "culture televangelisme religion evangelique television droite religieuse"),
 ("cu_armes_usa.html", CU, "#cbd5e1", "#334155", "2nd Amendment", "gun debate", "Culture · États-Unis", "Guns in America", "Le deuxième amendement, la NRA, les tueries scolaires, le débat sur les armes.", ["Constitution", "Débat", "Écoles"], [], "culture armes deuxieme amendement nra tueries scolaires gun control"),
 ("cu_anglophone.html", CU, "#99f6e4", "#0f766e", "English", "worldwide", "Culture · Monde anglophone", "English around the world", "Canada, Australie, Inde, Nigeria… : l'anglais sur tous les continents.", ["Pays", "Variétés", "Capitales"], [], "culture monde anglophone pays anglophones canada australie inde"),
 ("so_registres.html", SO, "#f0abfc", "#a21caf", "Formal?", "Could you…?", "Sociolinguistique · Registres", "Formal or informal?", "Registres de langue, politesse, emails formels.", ["Registres", "Politesse", "Emails"], [CAP], "registre formel informel politesse email soutenu familier"),
 ("so_british_american.html", SO, "#bfdbfe", "#dc2626", "flat", "apartment", "Sociolinguistique · Variétés", "British or American?", "Vocabulaire, orthographe et grammaire : anglais britannique et américain.", ["Vocabulaire", "Orthographe", "Grammaire"], [], "anglais britannique americain differences vocabulaire orthographe"),
 ("so_familier.html", SO, "#fdba74", "#c2410c", "gonna", "mate · dude", "Sociolinguistique · Registres", "Informal English & slang", "gonna, wanna, mate, quid, awesome… : comprendre l'anglais parlé.", ["Formes réduites", "Argot", "Registre"], [], "argot familier slang gonna wanna mate"),
 ("pr_actes_parole.html", PG, "#a5b4fc", "#4f46e5", "Sorry!", "Would you like…?", "Pragmatique · Actes de parole", "Speech acts", "Demander, proposer, accepter, refuser, s'excuser, remercier.", ["Demander", "Proposer", "S'excuser"], [CAP], "actes de parole demander proposer excuser remercier refuser"),
 ("pr_implicite.html", PG, "#fbcfe8", "#be185d", "Not bad…", "understatement", "Pragmatique · Implicite", "Reading between the lines", "Understatement, ironie, politesse indirecte : ce qu'on veut vraiment dire.", ["Implicite", "Ironie", "Tact"], [], "implicite understatement ironie sous-entendu diplomatie"),
 ("pr_argumenter.html", PG, "#86efac", "#15803d", "In my opinion", "However, …", "Pragmatique · Discours", "Give your opinion", "Argumenter, structurer un paragraphe, réagir dans un débat.", ["Opinion", "Arguments", "Débat"], [], "argumenter opinion debat structurer discours"),
 ("cu_vie_uk.html", CU, "#bae6fd", "#0369a1", "Cuppa?", "NHS · pub", "Culture · Royaume-Uni", "Everyday life in Britain", "École, NHS, thé, pub, file d'attente, BBC.", ["École", "Santé", "Pub"], [], "vie quotidienne royaume-uni ecole nhs the pub bbc"),
 ("cu_londres.html", CU, "#fecaca", "#dc2626", "London", "the Tube", "Culture · Royaume-Uni", "London calling", "Visiter Londres : le métro, Big Ben, la Tour, les musées.", ["Monuments", "Transports", "Visite"], [], "londres london visite monuments tube big ben"),
 ("cu_ecosse_galles.html", CU, "#a5b4fc", "#3730a3", "Scotland", "& Wales", "Culture · Royaume-Uni", "Scotland & Wales", "Kilts, lochs, gallois, dragon rouge, référendum de 2014.", ["Écosse", "Galles", "Identité"], [], "ecosse pays de galles scotland wales kilt gallois referendum"),
 ("cu_multiculturel.html", CU, "#fdba74", "#ea580c", "Diversity", "Notting Hill", "Culture · Royaume-Uni", "Multicultural Britain", "Immigration, racisme, carnaval de Notting Hill, scandale Windrush.", ["Immigration", "Diversité", "Débat"], [], "multiculturel immigration diversite notting hill windrush racisme"),
 ("cu_revolution_industrielle.html", CU, "#d6d3d1", "#57534e", "Steam", "1760", "Culture · Royaume-Uni", "The Industrial Revolution", "Usines, charbon, travail des enfants, Dickens.", ["Usines", "Ouvriers", "Dickens"], [], "revolution industrielle usines charbon dickens travail des enfants"),
 ("cu_suffragettes.html", CU, "#d8b4fe", "#7e22ce", "Votes", "for women", "Culture · Royaume-Uni", "The Suffragettes", "Le combat pour le droit de vote des femmes, de 1903 à 1928.", ["Droit de vote", "Militantes", "1918"], [], "suffragettes droit de vote femmes pankhurst feminisme"),
 ("cu_blitz.html", CU, "#94a3b8", "#1e293b", "1940", "Keep calm", "Culture · Royaume-Uni", "The Blitz & Churchill", "La Grande-Bretagne seule face aux bombardements nazis.", ["Churchill", "Bombardements", "RAF"], [], "blitz churchill seconde guerre mondiale bombardements raf"),
 ("cu_thatcher.html", CU, "#93c5fd", "#1e3a8a", "Iron Lady", "1979 – 1990", "Culture · Royaume-Uni", "Thatcher & the 1980s", "Privatisations, grève des mineurs, Malouines : une Grande-Bretagne divisée.", ["Thatcher", "Mineurs", "Malouines"], [], "thatcher annees 80 greve des mineurs malouines privatisations"),
 ("cu_paques_1916.html", CU, "#86efac", "#166534", "1916", "Easter Rising", "Culture · Irlande", "The Easter Rising", "De l'insurrection de Pâques à l'indépendance et à la partition.", ["Insurrection", "Indépendance", "Partition"], [], "irlande insurrection paques 1916 independance michael collins partition"),
 ("cu_irlande_auj.html", CU, "#a7f3d0", "#059669", "Éire", "the craic", "Culture · Irlande", "Ireland today", "Langue irlandaise, tigre celtique, référendums, St Patrick.", ["Société", "Langue", "Économie"], [], "irlande aujourd'hui dublin gaelique tigre celtique"),
 ("cu_pilgrims.html", CU, "#fde68a", "#92400e", "1620", "Mayflower", "Culture · États-Unis", "The Pilgrims & the 13 colonies", "Du Mayflower à la Déclaration d'indépendance.", ["Colonies", "Thanksgiving", "1776"], [], "pelerins mayflower thanksgiving colonies independance boston tea party"),
 ("cu_esclavage.html", CU, "#e7e5e4", "#44403c", "1861", "Civil War", "Culture · États-Unis", "Slavery & the Civil War", "Esclavage, Underground Railroad, Lincoln, guerre de Sécession, Juneteenth.", ["Esclavage", "Lincoln", "Abolition"], [], "esclavage guerre de secession lincoln abolition juneteenth"),
 ("cu_droits_civiques.html", CU, "#fef3c7", "#b45309", "Civil rights", "1955 – 1968", "Culture · États-Unis", "The Civil Rights Movement", "Rosa Parks, Martin Luther King, la fin de la ségrégation.", ["Rosa Parks", "MLK", "Ségrégation"], [], "droits civiques martin luther king rosa parks segregation"),
 ("cu_ellis_island.html", CU, "#99f6e4", "#0f766e", "Liberty", "Ellis Island", "Culture · États-Unis", "Ellis Island & the American Dream", "Une nation d'immigrants : statue de la Liberté, rêve américain.", ["Immigration", "Rêve américain", "New York"], [], "ellis island immigration reve americain statue de la liberte"),
 ("cu_1929_new_deal.html", CU, "#d9f99d", "#4d7c0f", "1929", "New Deal", "Culture · États-Unis", "The Great Depression & the New Deal", "Krach de Wall Street, Dust Bowl, Roosevelt.", ["Krach", "Dust Bowl", "Roosevelt"], [], "crise de 1929 grande depression new deal roosevelt dust bowl"),
 ("cu_vietnam.html", CU, "#bef264", "#3f6212", "Peace", "& love", "Culture · États-Unis", "Vietnam & the counterculture", "La guerre du Vietnam, les manifestations, les hippies, Woodstock.", ["Guerre", "Contestation", "Woodstock"], [], "vietnam contre-culture hippies woodstock manifestations"),
 ("cu_11_septembre.html", CU, "#cbd5e1", "#475569", "9/11", "2001", "Culture · États-Unis", "9/11", "Les attentats du 11 septembre et la « guerre contre le terrorisme ».", ["Attentats", "Conséquences", "Sécurité"], [], "11 septembre attentats world trade center terrorisme"),
 ("cu_conquete_spatiale.html", CU, "#c4b5fd", "#312e81", "Apollo", "one small step", "Culture · États-Unis", "The Space Race", "De Spoutnik à Apollo 11 : la course à la Lune.", ["Espace", "Guerre froide", "Lune"], [], "conquete spatiale apollo lune nasa armstrong"),
 ("cu_lycee_us.html", CU, "#fda4af", "#e11d48", "Prom", "yearbook", "Culture · États-Unis", "High school in the USA", "Casiers, bus jaune, football, prom, graduation.", ["Lycée", "Sport", "Prom"], [], "lycee americain high school prom yearbook graduation"),
 ("cu_elections_us.html", CU, "#bfdbfe", "#b91c1c", "270", "to win", "Culture · États-Unis", "US elections in detail", "Primaires, swing states, collège électoral, vote populaire.", ["Primaires", "Swing states", "Électeurs"], [], "elections americaines primaires college electoral swing states"),
 ("cu_amerindiens.html", CU, "#fcd34d", "#9a3412", "Still here", "574 nations", "Culture · États-Unis", "Native Americans today", "Réserves, souveraineté, pensionnats, Standing Rock.", ["Réserves", "Droits", "Résistance"], [], "amerindiens native americans reserves standing rock"),
 ("cu_australie.html", CU, "#fdba74", "#c2410c", "G'day", "down under", "Culture · Monde anglophone", "Australia", "Aborigènes, bagnards, générations volées, réconciliation.", ["Aborigènes", "Colonisation", "Excuses"], [], "australie aborigenes bagnards generations volees"),
 ("cu_afrique_sud.html", CU, "#86efac", "#ca8a04", "Mandela", "apartheid", "Culture · Monde anglophone", "South Africa & apartheid", "L'apartheid, Soweto, Mandela, la « nation arc-en-ciel ».", ["Apartheid", "Mandela", "Réconciliation"], [], "afrique du sud apartheid mandela soweto"),
 ("cu_inde.html", CU, "#fdba74", "#15803d", "Gandhi", "1947", "Culture · Monde anglophone", "India", "Le Raj, Gandhi, l'indépendance et la partition, Bollywood.", ["Raj", "Gandhi", "Partition"], [], "inde gandhi independance partition raj bollywood"),
 ("cu_canada.html", CU, "#fecaca", "#b91c1c", "Canada", "maple leaf", "Culture · Monde anglophone", "Canada", "Bilinguisme, Québec, peuples autochtones, pensionnats.", ["Bilinguisme", "Québec", "Autochtones"], [], "canada quebec bilinguisme autochtones"),
 ("cu_nouvelle_zelande.html", CU, "#5eead4", "#115e59", "Kia ora", "Aotearoa", "Culture · Monde anglophone", "New Zealand", "Les Maoris, le traité de Waitangi, le haka.", ["Maoris", "Waitangi", "Haka"], [], "nouvelle-zelande maoris waitangi haka all blacks"),
 ("cu_jamaique.html", CU, "#fde047", "#15803d", "One love", "reggae", "Culture · Monde anglophone", "Jamaica", "Histoire, patois, reggae et Bob Marley.", ["Histoire", "Patois", "Reggae"], [], "jamaique reggae bob marley patois caraibes"),
 ("cu_musique.html", CU, "#f9a8d4", "#9d174d", "Blues", "to hip-hop", "Culture · Arts & société", "Music as history", "Blues, jazz, rock, British Invasion, punk, hip-hop.", ["Genres", "Contestation", "Histoire"], [], "musique blues jazz rock beatles punk hip-hop"),
 ("cu_shakespeare.html", CU, "#d9b99b", "#78350f", "To be", "or not to be", "Culture · Arts & société", "William Shakespeare", "Sa vie, le Globe, ses pièces et ses expressions.", ["Théâtre", "Globe", "Expressions"], [], "shakespeare theatre globe hamlet romeo"),
 ("cu_grandes_figures.html", CU, "#fbcfe8", "#a21caf", "Heroes", "5 lives", "Culture · Arts & société", "Great lives", "Nightingale, Turing, Rosa Parks, Mandela, Malala.", ["Biographies", "Combats", "Courage"], [], "grandes figures biographies turing malala mandela nightingale rosa parks"),
 ("cu_medias.html", CU, "#e2e8f0", "#0f172a", "Fake?", "news", "Culture · Arts & société", "The media & fake news", "Tabloïds, BBC, chaînes partisanes, réseaux sociaux, esprit critique.", ["Presse", "Fake news", "Esprit critique"], [], "medias presse tabloids fake news bbc esprit critique"),
 ("so_accents.html", SO, "#c4b5fd", "#6d28d9", "Accents", "RP · Cockney", "Sociolinguistique · Variétés", "Accents of English", "RP, General American, Cockney, écossais, irlandais, australien, indien.", ["Accents", "Rhotique", "Régions"], [], "accents cockney rp americain ecossais irlandais australien"),
 ("so_dialectes.html", SO, "#fcd34d", "#065f46", "Wah gwaan?", "AAVE", "Sociolinguistique · Variétés", "Dialects & creoles", "AAVE, créole jamaïcain, anglais multiculturel de Londres.", ["AAVE", "Créole", "Code-switching"], [], "dialectes aave creole jamaicain patois"),
 ("so_codes_sociaux.html", SO, "#bbf7d0", "#047857", "Small talk", "queue · tip", "Sociolinguistique · Codes sociaux", "Social codes", "Small talk, pourboires, file d'attente, prénoms au travail.", ["Small talk", "Politesse", "Pourboire"], [CAP], "codes sociaux small talk pourboire politesse"),
 ("so_tabous.html", SO, "#fecaca", "#9f1239", "they", "firefighter", "Sociolinguistique · Registres", "Taboos & inclusive language", "Sujets délicats, mots neutres, euphémismes, pronom « they ».", ["Tabous", "Inclusif", "Euphémismes"], [], "tabous langage inclusif euphemismes they"),
 ("pr_telephone.html", PG, "#93c5fd", "#1d4ed8", "Hello?", "hold on", "Pragmatique · Actes de parole", "On the phone", "Répondre, transférer, prendre un message, épeler, dicter un email.", ["Téléphone", "Épeler", "Message"], [CAP], "telephone appel epeler message vocal"),
 ("pr_reclamation.html", PG, "#fca5a5", "#b91c1c", "Sorry!", "refund", "Pragmatique · Actes de parole", "Dealing with complaints", "La méthode LAST face à un client mécontent.", ["Client", "Excuses", "Solutions"], [CAP], "reclamation client mecontent remboursement"),
 ("pr_vendre_negocier.html", PG, "#fde68a", "#d97706", "Deal!", "10% off", "Pragmatique · Actes de parole", "Selling & negotiating", "Découvrir le besoin, argumenter, répondre aux objections, conclure.", ["Vente", "Objections", "Négociation"], [CAP], "vendre negocier vente objections"),
 ("pr_email_pro.html", PG, "#a5f3fc", "#0e7490", "Dear…", "Kind regards", "Pragmatique · Écrit professionnel", "The professional email", "Relance, réclamation, confirmation, candidature.", ["Email", "Formules", "Structure"], [CAP], "email professionnel courriel formules"),
 ("pr_prise_parole.html", PG, "#fbcfe8", "#be185d", "Speech!", "signposting", "Pragmatique · Discours", "Public speaking", "Accrocher, annoncer le plan, conclure, répondre aux questions.", ["Oral", "Présentation", "Questions"], [], "prise de parole presentation oral expose"),
 ("cu_guerre_secession.html", CU, "#bfdbfe", "#475569", "Union", "vs Confederacy", "Culture · États-Unis", "The Civil War: North vs South", "Lincoln contre Davis, industrie contre coton, le duel des cuirassés, le plan Anaconda.", ["Lincoln", "Ironclads", "Blocus"], [], "guerre de secession civil war nord sud lincoln jefferson davis monitor merrimack virginia ironclad anaconda"),
 ("cu_amerindiens_societe.html", CU, "#fdba74", "#7c2d12", "Native", "in society", "Culture · États-Unis", "Native Americans in society", "Réserves, pauvreté, santé, obésité et diabète, fierté retrouvée.", ["Réserves", "Santé", "Société"], [], "amerindiens societe reserves sante obesite diabete pauvrete"),
 ("cu_alaska.html", CU, "#a5f3fc", "#155e75", "Alaska", "Last Frontier", "Culture · États-Unis", "Alaska", "Achat à la Russie, ruée vers l'or, pétrole, Iditarod, changement climatique.", ["Histoire", "Pétrole", "Climat"], [], "alaska russie petrole glaciers climat iditarod"),
 ("cu_lgbt.html", CU, "#f0abfc", "#7c3aed", "Pride", "rainbow flag", "Culture · Arts & société", "LGBTQ+ rights", "De Oscar Wilde à Stonewall et au mariage pour tous : le combat pour l'égalité.", ["Droits", "Stonewall", "Égalité"], [], "lgbt lgbtq gay homosexualite droits pride stonewall mariage"),
 ("cu_1066.html", CU, "#fde68a", "#92400e", '1066', 'Hastings', 'Culture · Royaume-Uni', '1066 : la conquête normande', "Guillaume le Conquérant, Hastings, la tapisserie de Bayeux et les mots français de l'anglais.", ['Histoire', 'Normands', 'Langue'], [], '1066 hastings guillaume normands bayeux'),
 ("cu_tudors.html", CU, "#fecaca", "#991b1b", 'Tudors', 'Henry VIII', 'Culture · Royaume-Uni', 'Les Tudors', "Henri VIII et ses six épouses, la rupture avec Rome, Élisabeth Ire et l'Armada.", ['Histoire', 'Monarchie', 'Religion'], [], 'tudors henry henri viii elizabeth armada anglicane'),
 ("cu_victoriens.html", CU, "#e9d5ff", "#581c87", 'Victoria', '1837-1901', 'Culture · Royaume-Uni', "L'époque victorienne", "La reine Victoria, Dickens, les usines, le travail des enfants et l'Empire.", ['Histoire', 'Société', 'Dickens'], [], 'victoria victorien dickens usines enfants'),
 ("cu_ww1.html", CU, "#fca5a5", "#7f1d1d", 'Poppy', '1914-1918', 'Culture · Royaume-Uni', 'WWI et le poppy', 'Les tranchées, la Somme, les poètes de guerre et le coquelicot du souvenir.', ['Histoire', 'Guerre', 'Mémoire'], [], 'premiere guerre mondiale ww1 poppy coquelicot tranchees somme remembrance'),
 ("cu_welfare_state.html", CU, "#bbf7d0", "#166534", 'NHS', '1945-1948', 'Culture · Royaume-Uni', 'Le Welfare State', '1945 : Attlee, le rapport Beveridge et la naissance du NHS.', ['Histoire', 'Santé', 'Société'], [], 'welfare state nhs attlee beveridge 1945'),
 ("cu_swinging_sixties.html", CU, "#f9a8d4", "#be185d", 'Sixties', 'Swinging London', 'Culture · Royaume-Uni', 'The Swinging Sixties', 'Beatles, mini-jupe, Carnaby Street : Londres capitale de la pop.', ['Musique', 'Mode', 'Jeunesse'], [], 'sixties swinging london beatles minijupe mod'),
 ("cu_classes_uk.html", CU, "#cbd5e1", "#334155", 'Class', 'North & South', 'Culture · Royaume-Uni', 'Classes sociales et Nord-Sud', 'Upper, middle, working class, écoles privées et fracture Nord-Sud.', ['Société', 'Écoles', 'Régions'], [], 'classes sociales nord sud uk public school'),
 ("cu_humour.html", CU, "#fef08a", "#a16207", 'Humour', 'Monty Python', 'Culture · Royaume-Uni', "L'humour britannique", 'Ironie, understatement, autodérision : de Monty Python à Mr Bean.', ['Ironie', 'Séries', 'Codes'], [], 'humour britannique ironie understatement monty python mr bean'),
 ("cu_sport_uk.html", CU, "#86efac", "#14532d", 'Sport', 'Cricket', 'Culture · Royaume-Uni', 'Le sport britannique', 'Football, rugby, cricket, Wimbledon : le Royaume-Uni a inventé le sport moderne.', ['Football', 'Cricket', 'Tennis'], [], 'sport football rugby cricket wimbledon'),
 ("cu_cuisine_uk.html", CU, "#fed7aa", "#9a3412", 'Food', 'Fish and chips', 'Culture · Royaume-Uni', 'La cuisine britannique', 'Full English breakfast, fish and chips, Sunday roast, tea et curry.', ['Repas', 'Tea', 'Plats'], [], 'cuisine nourriture britannique fish chips tea breakfast roast'),
 ("cu_arthur.html", CU, "#c7d2fe", "#3730a3", 'Arthur', 'Excalibur', 'Culture · Arts & société', 'Le roi Arthur', 'Excalibur, Merlin, la Table ronde et le Graal : une légende britannique.', ['Légende', 'Chevaliers', 'Merlin'], [], 'arthur excalibur merlin table ronde graal legende'),
 ("cu_robin_hood.html", CU, "#bbf7d0", "#15803d", 'Robin Hood', 'Sherwood', 'Culture · Arts & société', 'Robin des Bois', 'Le hors-la-loi de Sherwood qui vole les riches pour donner aux pauvres.', ['Légende', 'Sherwood', 'Justice'], [], 'robin hood robin des bois sherwood legende'),
 ("cu_fantomes.html", CU, "#d4d4d8", "#3f3f46", 'Ghosts', 'Loch Ness', 'Culture · Arts & société', 'Fantômes et monstres', 'Châteaux hantés, la Tour de Londres et le monstre du Loch Ness.', ['Légendes', 'Écosse', 'Mystères'], [], 'fantomes ghosts loch ness nessie hante chateau'),
 ("cu_legendes_us.html", CU, "#fde68a", "#78350f", 'Legends', 'Bigfoot', 'Culture · Arts & société', 'Légendes américaines', 'Bigfoot, Sleepy Hollow, Roswell et légendes urbaines.', ['Mythes', 'Folklore', 'Légendes urbaines'], [], 'legendes americaines bigfoot sleepy hollow roswell urbaines'),
 ("cu_roaring_twenties.html", CU, "#fde68a", "#1f2937", '1920s', 'Jazz Age', 'Culture · États-Unis', 'The Roaring Twenties', 'Jazz, flappers, Charleston, voitures et Bourse : les années folles américaines.', ['Histoire', 'Jazz', 'Société'], [], 'roaring twenties annees folles jazz flappers 1920'),
 ("cu_prohibition.html", CU, "#d6d3d1", "#44403c", 'Prohibition', '1920-1933', 'Culture · États-Unis', 'La Prohibition', "L'alcool interdit, les speakeasies, Al Capone et les gangsters.", ['Histoire', 'Gangsters', 'Loi'], [], 'prohibition alcool al capone speakeasy gangsters'),
 ("cu_far_west.html", CU, "#fdba74", "#7c2d12", 'Wild West', 'Cowboys', 'Culture · États-Unis', 'Le Far West', "Cow-boys, ruée vers l'or, chemin de fer et mythes du western.", ['Histoire', 'Cowboys', 'Western'], [], 'far west cowboys western ruee or'),
 ("cu_ww2_usa.html", CU, "#bfdbfe", "#1e3a8a", 'WWII', 'Pearl Harbor', 'Culture · États-Unis', 'Les États-Unis et la WWII', "Pearl Harbor, le D-Day, l'effort de guerre et Hiroshima.", ['Histoire', 'Guerre', 'D-Day'], [], 'seconde guerre mondiale ww2 pearl harbor d-day hiroshima'),
 ("cu_guerre_froide.html", CU, "#e2e8f0", "#991b1b", 'Cold War', '1947-1991', 'Culture · États-Unis', 'La guerre froide', 'USA contre URSS : mur de Berlin, crise de Cuba, course aux armements.', ['Histoire', 'Berlin', 'Cuba'], [], 'guerre froide cold war urss berlin cuba'),
 ("cu_kennedy.html", CU, "#bfdbfe", "#1e40af", 'JFK', '1961-1963', 'Culture · États-Unis', 'John F. Kennedy', "Le jeune président, la Lune, Cuba et l'assassinat de Dallas.", ['Président', 'Dallas', 'Lune'], [], 'kennedy jfk dallas president'),
 ("cu_fast_food.html", CU, "#fca5a5", "#ca8a04", 'Fast food', 'Healthy?', 'Culture · États-Unis', 'Fast food et healthy food', "McDonald's, obésité, Heart Attack Grill et retour au « healthy ».", ['Santé', 'Alimentation', 'Société'], [], 'fast food malbouffe obesite heart attack grill healthy mcdonalds'),
 ("cu_blm.html", CU, "#d4d4d4", "#ca8a04", 'BLM', '2013-2020', 'Culture · États-Unis', 'Black Lives Matter', "George Floyd, la police et le racisme dans l'Amérique d'aujourd'hui.", ['Racisme', 'Police', 'Mouvement'], [], 'black lives matter blm george floyd racisme police'),
 ("cu_frontiere_mexique.html", CU, "#fdba74", "#047857", 'Border', 'US-Mexico', 'Culture · États-Unis', 'La frontière mexicaine', 'Immigration, mur, Dreamers et Amérique hispanique.', ['Immigration', 'Frontière', 'Latinos'], [], 'frontiere mexique immigration mur migrants latinos dreamers'),
 ("cu_sante_usa.html", CU, "#a7f3d0", "#0f766e", 'Health', 'Obamacare', 'Culture · États-Unis', 'La santé aux États-Unis', 'Assurances privées, Medicare, Obamacare : le système le plus cher du monde.', ['Santé', 'Assurance', 'Politique'], [], 'sante assurance obamacare medicare hopital'),
 ("cu_peine_mort.html", CU, "#e5e5e5", "#404040", 'Death penalty', 'Death row', 'Culture · États-Unis', 'La peine de mort', "27 États la gardent, 23 l'ont abolie : arguments et débat.", ['Justice', 'Débat', 'États'], [], 'peine de mort death penalty execution justice'),
 ("cu_hollywood.html", CU, "#fde68a", "#b91c1c", 'Hollywood', 'Oscars', 'Culture · Arts & société', 'Hollywood', "L'usine à rêves : studios, stars, Oscars et blockbusters.", ['Cinéma', 'Stars', 'Industrie'], [], 'hollywood cinema oscars stars studios'),
 ("cu_sports_us.html", CU, "#bfdbfe", "#b91c1c", 'Sports', 'Super Bowl', 'Culture · États-Unis', 'Les sports américains', 'NFL, NBA, baseball, sport universitaire et Super Bowl.', ['Football US', 'Basket', 'Baseball'], [], 'sports americains super bowl nfl nba baseball'),
 ("cu_route66.html", CU, "#fcd34d", "#1d4ed8", 'Route 66', 'Road trip', 'Culture · États-Unis', 'Route 66 et la voiture', 'La Mother Road, les motels, les diners et le road trip.', ['Route', 'Voiture', 'Liberté'], [], 'route 66 voiture road trip motel diner'),
 ("cu_silicon_valley.html", CU, "#a5f3fc", "#4338ca", 'Silicon Valley', 'Startups', 'Culture · États-Unis', 'La Silicon Valley', "Des garages aux géants de la tech : Apple, Google et l'IA.", ['Tech', 'Startups', 'Critiques'], [], 'silicon valley tech apple google startup'),
 ("cu_villes_etats.html", CU, "#93c5fd", "#ca8a04", 'States', 'Big Apple', 'Culture · États-Unis', 'Villes et États', 'New York, Californie, Texas, Floride, Hawaï, Las Vegas.', ['New York', 'Texas', 'Hawaï'], [], 'villes etats new york californie texas floride hawai las vegas chicago'),
 ("cu_hong_kong.html", CU, "#fecaca", "#b91c1c", 'Hong Kong', '1997', 'Culture · Monde anglophone', 'Hong Kong 1997', 'De la colonie britannique à la rétrocession et aux manifestations.', ['Histoire', 'Chine', 'Libertés'], [], 'hong kong 1997 handover chine colonie'),
 ("cu_afrique_anglophone.html", CU, "#86efac", "#b45309", 'Africa', 'Nollywood', 'Culture · Monde anglophone', "L'Afrique anglophone", 'Nigeria, Kenya, Nollywood et Afrobeats.', ['Nigeria', 'Kenya', 'Culture'], [], 'afrique anglophone nigeria kenya nollywood afrobeats'),
 ("cu_singapour.html", CU, "#fecdd3", "#dc2626", 'Singapore', 'Lion City', 'Culture · Monde anglophone', 'Singapour', 'Une cité-État riche, stricte et multilingue, et le Singlish.', ['Asie', 'Économie', 'Singlish'], [], 'singapour singapore singlish asie'),
 ("cu_romans.html", CU, "#e9d5ff", "#7c2d12", 'Novels', 'Classics', 'Culture · Arts & société', 'Les grands romans', 'Austen, Brontë, Orwell, Steinbeck, Harper Lee.', ['Littérature', 'Classiques', 'Thèmes'], [], 'romans litterature austen bronte orwell steinbeck mockingbird'),
 ("cu_litterature_jeunesse.html", CU, "#c4b5fd", "#15803d", 'Stories', 'Once upon a time', 'Culture · Arts & société', 'Littérature jeunesse', 'Alice, Tolkien, Narnia, Roald Dahl et Harry Potter.', ['Fantasy', 'Livres', 'Magie'], [], 'litterature jeunesse harry potter tolkien narnia roald dahl alice'),
 ("cu_art.html", CU, "#fbcfe8", "#2563eb", 'Art', 'Pop & street', 'Culture · Arts & société', 'Turner, Warhol, Banksy', 'Peinture de lumière, pop art et street art.', ['Peinture', 'Pop art', 'Street art'], [], 'art peinture turner warhol banksy pop art street art'),
 ("cu_consommation.html", CU, "#fde047", "#111827", 'Shopping', 'Black Friday', 'Culture · CAP', 'Shopping et consommation', 'Black Friday, Boxing Day, malls, crédit et critiques.', ['Black Friday', 'Soldes', 'Malls'], [CAP], 'consommation shopping black friday boxing day mall soldes'),
 ("cu_travail.html", CU, "#bae6fd", "#334155", 'Work', '9 to 5', 'Culture · CAP', 'Le monde du travail', 'CV, petits boulots, contrats, salaires et pourboires.', ['Emploi', 'Salaires', 'Pourboire'], [CAP], 'travail emploi cv salaire pourboire tip contrat job'),
 ("pronoms_interrogatifs.html", SY, "#f9a8d4", "#f472b6", "How far?", "Who · Whose · Which · How…", "Syntaxe · Questions", "Les mots interrogatifs", "Tous les mots interrogatifs : who, whose, which, why, how much / many, how long, how far, how deep… du niveau novice à expert.", ["Wh- words", "How + adj.", "whom / of which"], [], "les mots interrogatifs pronoms interrogatifs who whom whose what which of which why where when how much how many how long how often how old how far how deep how tall how high how wide how big how heavy how fast how come how about what kind of what time"),
 ("ccf_presenter.html", LE, "#6ee7b7", "#34d399", "He / She", "CCF CAPa SAPVER", "Lexique · Vie quotidienne", "Présenter quelqu'un", "Loisirs, qualités, défauts, et présentation orale d'une personne à partir d'une fiche d'identité tirée au hasard.", ["Hobbies", "Qualities & flaws", "Oral CCF"], [CAP], "presenter quelqu'un ccf capa sapver fiche d'identite present someone he she his her loisirs hobbies qualites defauts qualities flaws oral enregistrement"),
 ("cu_generations.html", CU, "#fde68a", "#0f766e", 'Beat', 'Gen X · Gen Z', 'Culture · Arts & société', 'Beat Generation et générations', "Kerouac, Ginsberg et les beatniks, puis Boomers, Gen X, Millennials, Gen Z.", ['Beat', 'Générations', 'Société'], [], 'beat generation beatnik kerouac ginsberg on the road generations boomers gen x millennials gen z alpha ok boomer'),
 ("cu_titanic.html", CU, "#bae6fd", "#1e3a8a", 'Titanic', '1912', 'Culture · Royaume-Uni', 'Le Titanic', 'Le naufrage de 1912, les classes sociales à bord et les leçons de la catastrophe.', ['Histoire', 'Naufrage', 'Classes'], [], 'titanic naufrage iceberg 1912 belfast paquebot'),
 ("cu_windrush.html", CU, "#fde68a", "#15803d", 'Windrush', '1948', 'Culture · Royaume-Uni', 'La génération Windrush', 'Les Caribéens qui ont reconstruit la Grande-Bretagne, et le scandale de 2018.', ['Immigration', 'NHS', 'Scandale'], [], 'windrush caraibes jamaique immigration notting hill scandale 1948'),
 ("cu_revolution_americaine.html", CU, "#bfdbfe", "#b91c1c", '1776', 'Independence', 'Culture · États-Unis', 'La Révolution américaine', "Boston Tea Party, Déclaration d'indépendance, La Fayette et la Constitution.", ['Histoire', '1776', 'Constitution'], [], 'revolution americaine 1776 independance boston tea party washington constitution la fayette'),
 ("cu_reve_americain.html", CU, "#fde68a", "#166534", 'Dream', 'Wall Street', 'Culture · États-Unis', 'Le rêve américain', 'Du « self-made man » à Wall Street, et le débat sur les inégalités.', ['Réussite', 'Finance', 'Inégalités'], [], 'reve americain american dream wall street bourse self made man inegalites'),
 ("cu_hip_hop.html", CU, "#fbbf24", "#7c3aed", 'Hip-hop', 'Bronx 1973', 'Culture · Arts & société', 'Le hip-hop', 'Né dans le Bronx en 1973 : rap, DJing, breaking, graffiti.', ['Musique', 'Danse', 'Graffiti'], [], 'hip hop rap bronx breaking graffiti dj'),
 ("cu_caraibes.html", CU, "#5eead4", "#ca8a04", 'Caribbean', 'West Indies', 'Culture · Monde anglophone', 'Les Caraïbes anglophones', 'Barbade, Trinidad, esclavage, indépendances, cricket et carnaval.', ['Histoire', 'Culture', 'Climat'], [], 'caraibes barbade trinidad bahamas west indies carnaval cricket rihanna'),
 ("cu_soins_ages.html", CU, "#99f6e4", "#0f766e", 'Care', 'Care home', 'Culture · CAP', 'Soins aux personnes âgées', 'Care homes, aides à domicile et aidants au Royaume-Uni et aux États-Unis.', ['Aide à la personne', 'Vocabulaire', 'Société'], [CAP], 'personnes agees care home maison de retraite aide domicile carer sapver'),
 ("cu_service_client.html", CU, "#5eead4", "#be185d", 'Service', 'Have a nice day!', 'Culture · CAP', 'Le service client', '« Have a nice day! », le client roi, Walmart, Tesco et la politesse au magasin.', ['Vente', 'Politesse', 'Codes'], [CAP], 'service client vente magasin walmart tesco have a nice day sapver'),
 ("cu_ecole_uk.html", CU, "#bfdbfe", "#7f1d1d", 'School', 'Year 7', 'Culture · Royaume-Uni', "L'école au Royaume-Uni", 'Uniformes, houses, assemblies, GCSEs et A-levels.', ['École', 'Uniforme', 'Examens'], [], 'ecole college royaume uni uniforme house gcse a-levels eton'),
 ("cu_famille_royale.html", CU, "#fde68a", "#6d28d9", 'Royals', 'Charles III', 'Culture · Royaume-Uni', "La famille royale aujourd'hui", "Diana, Charles III, William, Harry et l'avenir de la monarchie.", ['Monarchie', 'Diana', 'Débat'], [], 'famille royale diana charles william harry meghan kate monarchie'),
 ("cu_geographie_usa.html", CU, "#bbf7d0", "#b45309", 'USA', 'Coast to coast', 'Culture · États-Unis', 'Géographie des États-Unis', 'Les grandes régions, le Mississippi, Yellowstone et le Grand Canyon.', ['Régions', 'Nature', 'Parcs'], [], 'geographie etats unis regions mississippi yellowstone grand canyon parcs nationaux'),
 ("cu_fetes_origines.html", CU, "#fdba74", "#7c2d12", 'Holidays', 'Trick or treat', 'Culture · Arts & société', 'Les fêtes et leurs origines', "Halloween, Bonfire Night, Thanksgiving, Christmas, St Patrick's Day.", ['Halloween', 'Thanksgiving', 'Noël'], [], 'fetes halloween thanksgiving bonfire night guy fawkes noel christmas saint patrick'),
 ("cu_polar_espions.html", CU, "#d6d3d1", "#991b1b", 'Detectives', '007', 'Culture · Arts & société', 'Détectives et espions', 'Sherlock Holmes, Agatha Christie, James Bond et les vrais espions.', ['Sherlock', 'Poirot', 'Bond'], [], 'sherlock holmes agatha christie poirot james bond espion detective mi6'),
 ("cu_super_heros.html", CU, "#fca5a5", "#1d4ed8", 'Heroes', 'Superman 1938', 'Culture · Arts & société', 'Les super-héros', "De Superman aux films Marvel : ce que les héros racontent de l'Amérique.", ['Comics', 'Marvel', 'Société'], [], 'super heros superman batman marvel spider-man black panther comics'),
 ("cu_sciences.html", CU, "#a5f3fc", "#1d4ed8", 'Science', 'Eureka!', 'Culture · Langue, sciences & religion', 'Sciences et inventions', 'Newton, Darwin, Turing, Edison, les frères Wright, le Web.', ['Savants', 'Inventions', 'Histoire'], [], 'sciences inventions newton darwin turing edison wright web'),
 ("cu_histoire_anglais.html", CU, "#ddd6fe", "#9a3412", 'English', 'Old → Global', 'Culture · Langue, sciences & religion', "L'histoire de la langue anglaise", "Anglo-Saxons, Vikings, Normands, Shakespeare, et l'anglais langue mondiale.", ['Langue', 'Mots', 'Histoire'], [], 'histoire langue anglaise anglo-saxons vikings normands vieil anglais etymologie'),
 ("cu_religion.html", CU, "#e9d5ff", "#1e3a8a", 'Religion', 'In God We Trust', 'Culture · Langue, sciences & religion', 'Religion et société', 'États-Unis très religieux, Royaume-Uni à Église officielle mais peu pratiquant.', ['États-Unis', 'Royaume-Uni', 'Laïcité'], [], 'religion eglise bible belt church of england in god we trust'),
 ("cu_peuples_autochtones.html", CU, "#fdba74", "#7c2d12", 'Indigenous', 'First Nations', 'Culture · Monde anglophone', 'Peuples autochtones', 'Aborigènes, Stolen Generations, First Nations, Inuit et pensionnats.', ['Australie', 'Canada', 'Réconciliation'], [], 'peuples autochtones aborigenes stolen generations first nations inuit pensionnats canada australie'),
 ("cu_orwell.html", CU, "#d4d4d8", "#991b1b", 'Orwell', 'Big Brother', 'Culture · Littérature & théâtre', 'George Orwell', 'Sa vie, Animal Farm, 1984, Big Brother, la novlangue.', ['Littérature', '1984', 'Totalitarisme'], [], 'orwell 1984 animal farm big brother novlangue newspeak dystopie'),
 ("cu_dystopies.html", CU, "#a3a3a3", "#ea580c", 'Dystopia', '451 °F', 'Culture · Littérature & théâtre', 'Les dystopies', "Brave New World, 1984, Fahrenheit 451, The Handmaid's Tale, Hunger Games.", ['Fahrenheit 451', 'Surveillance', 'Censure'], [], 'dystopie utopie fahrenheit 451 bradbury brave new world huxley handmaid hunger games black mirror'),
 ("cu_baldwin.html", CU, "#fcd34d", "#1e3a8a", 'Baldwin', 'Harlem 1935', 'Culture · Littérature & théâtre', 'Go Tell It on the Mountain', 'James Baldwin, Harlem, la religion et les droits civiques.', ['Roman', 'Harlem', 'Droits civiques'], [], 'james baldwin go tell it on the mountain harlem roman spiritual'),
 ("cu_othello.html", CU, "#e5e7eb", "#7f1d1d", 'Othello', 'Jealousy', 'Culture · Littérature & théâtre', 'Othello', 'La tragédie de la jalousie : Iago, le mouchoir et la question raciale.', ['Shakespeare', 'Tragédie', 'Jalousie'], [], 'othello shakespeare iago desdemona jalousie tragedie'),
 ("cu_much_ado.html", CU, "#fbcfe8", "#15803d", 'Much Ado', 'Beatrice & Benedick', 'Culture · Littérature & théâtre', 'Much Ado About Nothing', 'La comédie des malentendus : Beatrice, Benedick, Claudio et Hero.', ['Shakespeare', 'Comédie', 'Amour'], [], 'much ado about nothing beaucoup de bruit pour rien shakespeare beatrice benedick comedie'),
 ("cu_afrique_sud_auj.html", CU, "#86efac", "#ca8a04", 'Rainbow', 'Nation', 'Culture · Monde anglophone', "L'Afrique du Sud aujourd'hui", "La nation arc-en-ciel 30 ans après : langues, politique, inégalités, rugby, amapiano.", ['Société', 'Politique', 'Culture'], [], 'afrique du sud aujourd hui rainbow nation ramaphosa springboks kolisi amapiano trevor noah'),
 ("cu_explorateurs.html", CU, "#bae6fd", "#78350f", 'Explorers', 'Endurance', 'Culture · Royaume-Uni', 'Les grands explorateurs', 'Cook, Livingstone, Stanley et Shackleton : aventure et colonisation.', ['Voyages', 'Pacifique', 'Antarctique'], [], 'explorateurs cook shackleton endurance livingstone stanley exploration'),
 ("cu_grands_discours.html", CU, "#fde68a", "#1e3a8a", 'Speeches', 'I have a dream', 'Culture · Arts & société', 'Les grands discours', "Lincoln, Churchill, Kennedy, Martin Luther King, Malala et l'art de convaincre.", ['Rhétorique', 'Histoire', 'Engagement'], [], 'grands discours i have a dream churchill lincoln kennedy malala rhetorique orateur'),
 ("cu_mark_twain.html", CU, "#bae6fd", "#92400e", 'Twain', 'Mississippi', 'Culture · Littérature & théâtre', 'Mark Twain et le Mississippi', 'Tom Sawyer, Huckleberry Finn et la vie sur le fleuve.', ['Roman', 'Fleuve', 'Aventure'], [], 'mark twain mississippi tom sawyer huckleberry finn steamboat'),
 ("cu_jeux_de_mots.html", CU, "#fca5a5", "#2563eb", 'Wordplay', 'Supercali…', 'Culture · Langue, sciences & religion', 'Dr. Seuss, Mary Poppins et les jeux de mots', "Rimes, limericks, virelangues et musicalité de l'anglais.", ['Rimes', 'Poésie', 'Langue'], [], 'dr seuss mary poppins supercalifragilisticexpialidocious rimes limerick tongue twister jeux de mots'),
 ("cu_mythes_dragons.html", CU, "#86efac", "#b91c1c", 'Myths', 'Leprechaun', 'Culture · Légendes', 'Mythes irlandais et dragons', 'Leprechauns, banshees, Finn McCool, saint Georges et le dragon gallois.', ['Irlande', 'Dragons', 'Folklore'], [], "mythes irlandais leprechaun banshee dragon saint georges pays de galles giant's causeway"),
 ("cu_bbc.html", CU, "#fecaca", "#111827", 'BBC', 'Auntie Beeb', 'Culture · Royaume-Uni', 'La BBC', 'Service public, licence fee, World Service, Doctor Who et Attenborough.', ['Médias', 'Télévision', 'Soft power'], [], 'bbc television radio doctor who attenborough licence fee'),
 ("cu_national_trust.html", CU, "#bbf7d0", "#14532d", 'Heritage', 'National Trust', 'Culture · Royaume-Uni', 'Le National Trust et le patrimoine', "Châteaux, jardins, côtes, Beatrix Potter et le débat sur l'héritage colonial.", ['Patrimoine', 'Châteaux', 'Nature'], [], 'national trust patrimoine chateau jardin beatrix potter lake district heritage'),
 ("cu_juneteenth_columbus.html", CU, "#fca5a5", "#1e3a8a", 'Juneteenth', '19 June', 'Culture · États-Unis', 'Juneteenth et Columbus Day', 'Deux fêtes américaines, deux mémoires, un débat.', ['Fêtes', 'Mémoire', 'Débat'], [], 'juneteenth columbus day indigenous peoples day fete esclavage colomb'),
 ("cu_familles_presidentielles.html", CU, "#bfdbfe", "#b91c1c", 'White House', 'First Lady', 'Culture · États-Unis', 'Les familles présidentielles', "La Maison-Blanche, les First Ladies, les dynasties et l'image du président.", ['Président', 'Famille', 'Image'], [], 'familles presidentielles maison blanche first lady eleanor roosevelt kennedy obama'),
 ("cu_portraits.html", CU, "#fde68a", "#7c2d12", 'Portraits', 'Selfie', 'Culture · Arts & société', 'Portraits et autoportraits', 'La National Portrait Gallery, les portraits du pouvoir, les Obama et le selfie.', ['Peinture', 'Pouvoir', 'Selfie'], [], 'portraits autoportrait national portrait gallery selfie obama holbein elizabeth'),
 ("cu_travail_usa.html", CU, "#bfdbfe", "#7c2d12", 'Work', 'Assembly line', 'Culture · Consommation & travail', 'Le travail aux États-Unis', 'Ford, travail des enfants, teen jobs et philanthropie.', ['Ford', 'Enfants', 'Philanthropie'], [], 'travail etats unis ford chaine de montage travail des enfants teen jobs philanthropie carnegie'),
 ("cu_gag.html", CU, "#fde68a", "#111827", 'Gag', 'Slapstick', 'Culture · Arts & société', 'La mécanique du gag', "Chaplin, Keaton, Laurel et Hardy, Mr Bean : l'art de faire rire.", ['Cinéma', 'Humour', 'Muet'], [], 'gag slapstick chaplin keaton laurel hardy mr bean humour'),
 ("cu_sports_commonwealth.html", CU, "#86efac", "#1e40af", 'Cricket', 'Stanley Cup', 'Culture · Monde anglophone', 'Les sports du Commonwealth', 'Cricket, hockey sur glace au Canada et football australien.', ['Cricket', 'Hockey', 'Aussie Rules'], [], 'sports commonwealth cricket hockey canada aussie rules football australien'),
 ("cu_villes_modeles.html", CU, "#d6d3d1", "#166534", 'Towns', 'Bournville', 'Culture · Monde anglophone', 'Villes modèles et quartiers fermés', 'Bournville et Cadbury, Melbourne, Poundbury et les gated communities.', ['Ville', 'Chocolat', 'Ségrégation'], [], 'bournville cadbury melbourne poundbury gated communities cite jardin ville'),
 ("cu_irlande_atlantique.html", CU, "#86efac", "#0e7490", 'Ireland', 'Wild Atlantic', 'Culture · Irlande', "La Wild Atlantic Way et l'Irlande européenne", "Côte sauvage, terre d'accueil, Union européenne et traditions.", ['Paysages', 'Europe', 'Accueil'], [], 'wild atlantic way irlande europe gaeltacht celtic tiger immigration'),
 ("cu_animaux_journaux.html", CU, "#fde68a", "#166534", 'Diary', 'Paddington', 'Culture · Littérature & théâtre', "Histoires d'animaux et journaux intimes", "Peter Rabbit, Jungle Book, Charlotte's Web, Paddington, Pepys et Adrian Mole.", ['Animaux', 'Journal', 'Lecture'], [], 'animaux fables peter rabbit jungle book paddington journal intime diary pepys adrian mole wimpy kid'),
 ("cu_migrations_vagabonds.html", CU, "#fdba74", "#334155", 'Migrants', 'Hobos', 'Culture · Monde anglophone', 'Migrants et vagabonds', 'Ten Pound Poms, Great Migration, hobos et la figure du vagabond.', ['Australie', 'Migrations', 'Route'], [], 'migrations australie ten pound poms great migration hobo vagabond nomadland'),
 ("cu_publicite.html", CU, "#fca5a5", "#ca8a04", 'Ads', 'Just Do It', 'Culture · Consommation & travail', 'Publicité et soft power', 'Madison Avenue, slogans célèbres, Super Bowl et influence américaine.', ['Publicité', 'Marques', 'Soft power'], [], 'publicite advertising slogan marque soft power super bowl influenceur'),
 ("cu_campus_us.html", CU, "#fbcfe8", "#1d4ed8", 'Campus', 'Greek life', 'Culture · États-Unis', 'Cliques, clubs et fraternités', 'Les cliques du lycée, le yearbook, les clubs et les fraternités.', ['Lycée', 'Université', 'Vie sociale'], [], 'cliques yearbook fraternites sororites campus clubs breakfast club prom homecoming'),
 ("cu_cour_supreme.html", CU, "#e5e7eb", "#1e3a8a", 'Supreme Court', '9 justices', 'Culture · États-Unis', 'La Cour suprême', 'De Plessy à Brown, de Roe à Dobbs, et la fin de la discrimination positive.', ['Justice', 'Droits', 'Inclusion'], [], 'cour supreme supreme court affirmative action discrimination positive brown plessy roe dobbs'),
 ("cu_salem.html", CU, "#a3a3a3", "#7c3aed", 'Salem', '1692', 'Culture · États-Unis', 'Chasses aux sorcières : de Salem à Hollywood', 'Les procès de 1692, The Crucible et le maccarthysme.', ['Histoire', 'Théâtre', 'Justice'], [], 'salem sorcieres witch hunt crucible arthur miller maccarthysme blacklist'),
 ("cu_porto_rico.html", CU, "#fca5a5", "#1d4ed8", 'Puerto Rico', '51st state?', 'Culture · Monde anglophone', 'Porto Rico, le 51e État ?', 'Un territoire américain : citoyenneté, statut, ouragan Maria, reggaeton.', ['Caraïbes', 'Statut', 'Culture'], [], 'porto rico puerto rico territoire 51e etat maria bad bunny'),
 ("cu_mobilisations.html", CU, "#fca5a5", "#1f2937", 'Strike!', '#hashtag', 'Culture · Consommation & travail', 'Des syndicats au hashtag', 'Tolpuddle, grandes grèves, 1er mai, Occupy, #MeToo.', ['Syndicats', 'Grèves', 'Réseaux'], [], 'syndicats trade unions greve mineurs tolpuddle metoo occupy mobilisation hashtag'),
 ("cu_complotisme.html", CU, "#d4d4d8", "#16a34a", 'Conspiracy', 'Fact-check', 'Culture · Arts & société', 'Le complotisme', 'Théories du complot, pourquoi on y croit, comment vérifier.', ['Esprit critique', 'Médias', 'Vérification'], [], 'complotisme conspiracy theories fake news fact checking deepfake theorie du complot'),
 ("cu_jeux_video.html", CU, "#a5b4fc", "#16a34a", 'Games', 'Game on', 'Culture · Arts & société', 'Jeux vidéo et soft power', 'De Pong à Fortnite : une industrie géante et une influence culturelle.', ['Industrie', 'Soft power', 'Débats'], [], 'jeux video video games soft power gta fortnite minecraft esport'),
 ("cu_ia_ecole.html", CU, "#c7d2fe", "#0f766e", 'AI', 'Homework 2.0', 'Culture · Langue, sciences & religion', "L'IA à l'école", 'ChatGPT, tuteurs virtuels, triche, hallucinations et esprit critique.', ['IA', 'Éducation', 'Éthique'], [], 'intelligence artificielle ia chatgpt ecole education triche'),
 ("cu_beaute.html", CU, "#fbcfe8", "#7c2d12", 'Beauty', 'Standards', 'Culture · Arts & société', 'Les canons de beauté', 'Des Préraphaélites aux filtres : normes, concours et body positivity.', ['Art', 'Mode', 'Société'], [], 'beaute canons preraphaelites miss america barbie filtres body positivity'),
 ("cu_ecosse_auj.html", CU, "#bfdbfe", "#1e3a8a", 'Scotland', 'Glasgow · Edinburgh', 'Culture · Royaume-Uni', "L'Écosse aujourd'hui", "Pétrole et éolien, Glasgow et Édimbourg, débat sur l'indépendance.", ['Énergie', 'Villes', 'Indépendance'], [], 'ecosse scotland glasgow edinburgh edimbourg energie eolien petrole independance'),
 ("cu_diaspora_indienne.html", CU, "#fdba74", "#047857", 'Diaspora', 'British Asian', 'Culture · Monde anglophone', 'La diaspora indienne', 'British Asians, générations, identités et influence culturelle.', ['Immigration', 'Générations', 'Identité'], [], 'diaspora indienne british asian inde generations sunak bend it like beckham'),
 ("cu_nature.html", CU, "#bbf7d0", "#1e3a8a", 'Nature', 'Walden', 'Culture · Langue, sciences & religion', "L'être humain et la nature", 'Wordsworth, Thoreau, Muir, Rachel Carson et les extrêmes climatiques.', ['Écologie', 'Littérature', 'Climat'], [], 'nature ecologie wordsworth thoreau walden muir rachel carson climat katrina'),
 ("cu_vancouver_seattle.html", CU, "#a5f3fc", "#166534", 'Cascadia', 'Vancouver · Seattle', 'Culture · Monde anglophone', 'Vancouver et Seattle', 'Deux villes du Pacifique, deux pays : regards croisés.', ['Villes', 'Canada', 'États-Unis'], [], 'vancouver seattle cascadia canada etats unis amazon starbucks'),
 ("cu_caricature.html", CU, "#fef08a", "#1f2937", 'Cartoons', 'Photojournalism', 'Culture · Arts & société', 'Caricature et photojournalisme', 'Hogarth, Punch, Thomas Nast, Dorothea Lange et le pouvoir des images.', ['Presse', 'Images', 'Liberté'], [], 'caricature dessin de presse cartoon photojournalisme hogarth nast dorothea lange'),
 ("cu_logement.html", CU, "#d6d3d1", "#991b1b", 'Housing', 'Home sweet home', 'Culture · Arts & société', 'Logement et mixité sociale', 'Council houses, Right to Buy, Grenfell, redlining et gentrification.', ['Société', 'Inégalités', 'Ville'], [], 'logement housing council house grenfell redlining gentrification mixite sociale'),
 ("cu_memoire.html", CU, "#fca5a5", "#14532d", 'Remember', 'Poppy', 'Culture · Royaume-Uni', 'Mémoire et commémorations', "Remembrance Day, Anzac Day, Vimy, mémoire de l'esclavage et statues.", ['Mémoire', 'Guerres', 'Esclavage'], [], 'memoire commemoration remembrance day poppy anzac vimy statues esclavage'),
 ("cu_espace_qui.html", CU, "#c7d2fe", "#111827", 'Space', 'Who owns it?', 'Culture · États-Unis', "À qui appartient l'espace ?", 'Traité de 1967, SpaceX, Artemis, ressources et débris spatiaux.', ['Espace', 'Droit', 'Éthique'], [], 'espace space spacex artemis traite 1967 debris lune ressources'),
 ("cu_frankenstein.html", CU, "#86efac", "#1f2937", 'Frankenstein', 'Ethics', 'Culture · Littérature & théâtre', "Frankenstein et l'homme parfait", "Mary Shelley, l'eugénisme, Dolly, CRISPR et l'éthique scientifique.", ['Littérature', 'Science', 'Éthique'], [], 'frankenstein mary shelley eugenisme clonage dolly crispr ethique science'),
 ("ce_ecole.html", CO, "#fecaca", "#ef4444", "Read", "A school day", "Compréhension écrite", "A school day in England", "La journée d'un collégien anglais : uniforme, cantine, matières.", ["Vrai / faux", "Questions", "Vocabulaire"], ["Lecture"], "comprehension ecrite ecole school uniforme"),
 ("ce_email.html", CO, "#c4b5fd", "#8b5cf6", "Read", "An email", "Compréhension écrite", "An email from Emma", "Le mail d'une correspondante anglaise qui raconte ses vacances.", ["Vrai / faux", "Questions", "Vocabulaire"], ["Lecture"], "comprehension ecrite email correspondant vacances"),
 ("ce_reseaux.html", CO, "#a5f3fc", "#06b6d4", "Read", "Social media", "Compréhension écrite", "Teens and social media", "Un article de presse : une semaine sans réseaux sociaux.", ["Article", "Opinions", "Connecteurs"], ["Lecture"], "comprehension ecrite article reseaux sociaux telephone"),
 ("co_cafe.html", CO, "#fcd34d", "#d97706", "Listen", "At the café", "Compréhension orale", "At the café", "Commander à boire et à manger, demander le prix.", ["Dialogue", "Prix", "Questions"], ["Écoute"], "comprehension orale cafe commander"),
 ("co_directions.html", CO, "#86efac", "#16a34a", "Listen", "Directions", "Compréhension orale", "Excuse me, where is…?", "Demander et comprendre son chemin dans une ville anglaise.", ["Dialogue", "Itinéraire", "Questions"], ["Écoute"], "comprehension orale chemin directions ville"),
 ("co_entretien.html", CO, "#f9a8d4", "#db2777", "Listen", "Job interview", "Compréhension orale", "A job interview", "Un entretien d'embauche pour un job d'été de vendeur.", ["Entretien", "Qualités", "Questions"], ["Écoute", CAP], "comprehension orale entretien embauche job interview"),
 ("ecriture_guidee.html", PR, "#fb923c", "#ea580c", "Write", "pas à pas", "Production écrite", "Écriture guidée", "Se présenter, raconter, écrire un email, présenter son stage, donner son avis : phrase par phrase, avec des aides.", ["Étapes", "Exemples", "Copier"], [CAP], "production ecrite ecrire redaction expression ecrite email lettre stage"),
 ("expression_orale.html", PR, "#e879f9", "#c026d3", "Speak", "🎙️ enregistre-toi", "Production orale", "Expression orale", "Écouter le modèle, répéter, s'enregistrer, tester sa prononciation et répondre à l'oral.", ["Modèle", "Enregistrer", "Prononciation"], [CAP], "production orale parler prononciation enregistrer micro oral"),
 ("inversion.html", SY, "#fca5a5", "#b91c1c", "Never have I", "inversion", "Expert · Syntaxe", "L'inversion emphatique", "Never have I seen…, Rarely does he…, Had I known… : l'inversion du registre soutenu.", ["Never have I", "Not only", "Had I known"], ["Phrase complexe"], "inversion emphatique soutenu"),
 ("phrases_clivees.html", SY, "#a5f3fc", "#0e7490", "What I need", "is…", "Expert · Syntaxe", "Phrases clivées et emphase", "It was Tom who…, What I need is…, do emphatique : mettre en relief.", ["It is… that", "What… is", "do emphatique"], ["Phrase complexe"], "clivee emphase mise en relief"),
 ("participiales.html", SY, "#bbf7d0", "#15803d", "Having done", "participiales", "Expert · Syntaxe", "Les propositions participiales", "Having finished…, Built in 1889… et le piège du participe flottant.", ["-ing", "having + PP", "PP"], ["Phrase complexe"], "participe proposition participiale"),
 ("conditionnels_mixtes.html", GR, "#fdba74", "#c2410c", "Mixed if", "passé ↔ présent", "Expert · Grammaire", "Les conditionnels mixtes", "If I had studied, I would be… : croiser passé et présent dans l'hypothèse.", ["passé → présent", "présent → passé"], ["Futur"], "conditionnel mixte"),
 ("subjonctif.html", GR, "#ddd6fe", "#7c3aed", "Be it so", "suggest that he be", "Expert · Grammaire", "Le subjonctif anglais", "I suggest that he be…, It's time we left, If I were… : le subjonctif en anglais.", ["suggest that", "It's time", "were"], ["Verbes & modaux"], "subjonctif"),
 ("remember_to_ing.html", GR, "#fde68a", "#b45309", "Remember", "to ≠ -ing", "Expert · Grammaire", "remember to / remember -ing", "remember, forget, stop, try, regret, mean : quand to et -ing changent le sens.", ["remember", "stop", "try"], ["Verbes & modaux"], "infinitif gerondif sens"),
 ("connected_speech.html", PH, "#e9d5ff", "#7e22ce", "Gonna", "wanna · dunno", "Expert · Phonologie", "Connected speech", "Liaisons, élisions, assimilations et formes réduites (gonna, wanna, dunno).", ["liaison", "élision", "gonna"], ["Accent"], "connected speech oral"),
 ("but.html", SY, "#a5f3fc", "#0891b2", "In order to", "so that", "Syntaxe · Liens logiques", "Exprimer le but", "to, in order to, so as not to, so that, for : dire pourquoi on fait quelque chose.", ["to", "in order to", "so that"], [], "but pour afin de"),
 ("conjonctions_avancees.html", SY, "#fecdd3", "#be123c", "Unless", "whereas · despite", "Syntaxe · Liens logiques", "Conjonctions avancées", "unless, in case, as long as, whereas, even though, despite : condition et concession.", ["unless", "in case", "despite"], [], "conjonctions malgre sauf si"),
 ("substitution.html", SY, "#e0e7ff", "#6366f1", "I think so", "I hope not", "Syntaxe · Reprises", "Substitution et ellipse", "I think so, I hope not, I'd love to, Yes I do : éviter les répétitions.", ["I think so", "I hope not", "I'd love to"], [], "reprise ellipse"),
 ("prepositions_dependantes.html", GR, "#99f6e4", "#0f766e", "Good at", "interested in", "Grammaire · Prépositions", "Les prépositions dépendantes", "interested in, good at, afraid of, depend on, wait for… : la bonne préposition après un mot.", ["good at", "wait for", "+ -ing"], [], "prepositions dependantes"),
 ("prepositions_mouvement.html", GR, "#bbf7d0", "#16a34a", "Through", "into · across", "Grammaire · Prépositions", "Les prépositions de mouvement", "into, out of, through, across, along, over, past, towards…", ["into", "through", "across"], [], "prepositions mouvement"),
 ("modaux_complements.html", GR, "#c7d2fe", "#4338ca", "Could", "had better", "Grammaire · Modaux", "Les autres modaux", "could, be able to, had better, ought to, needn't, would rather.", ["could", "had better", "needn't"], [], "modaux capacite conseil"),
 ("quantifieurs.html", GR, "#fef3c7", "#d97706", "All", "every · each", "Grammaire · Quantifieurs", "all, every, each, most", "Les quantifieurs : all, every, each, most, most of, whole, none of.", ["all", "every / each", "most"], [], "quantifieurs tout chaque"),
 ("one_ones.html", GR, "#fbcfe8", "#db2777", "One", "the red one", "Grammaire · Pronoms", "one / ones", "the red one, new ones : remplacer un nom pour ne pas le répéter.", ["one", "ones", "Which one?"], [], "one ones"),
 ("adjectifs_composes.html", GR, "#f5d0fe", "#a21caf", "Ten-year-old", "blue-eyed", "Grammaire · Adjectifs", "Les adjectifs composés", "a ten-year-old boy, a blue-eyed girl, a well-known singer : sans -s !", ["ten-year-old", "blue-eyed"], [], "adjectifs composes"),
 ("comparatif_avance.html", GR, "#99f6e4", "#0d9488", "The more…", "the better", "Grammaire · Comparaison", "Le comparatif avancé", "the more… the more, more and more, as… as possible, not as… as, adverbes.", ["the more", "as possible"], [], "comparatif double progressif"),
 ("expressions_avancees.html", GR, "#fef9c3", "#a16207", "Worth it", "no point -ing", "Expert · Grammaire", "Expressions verbales avancées", "It's worth -ing, there's no point -ing, would rather you…, the rich, be about to.", ["worth -ing", "no point", "would rather"], [], "expressions avancees gerondif"),
 ("ordre_mots.html", SY, "#fde68a", "#ca8a04", "S + V + O", "manière · lieu · temps", "Syntaxe · Ordre des mots", "L'ordre des mots", "Sujet, verbe, complément, puis manière, lieu, temps : construire une phrase dans le bon ordre.", ["S + V + O", "lieu · temps"], [], "ordre des mots"),
 ("double_complement.html", SY, "#bae6fd", "#0284c7", "Give him…", "it to me", "Syntaxe · Compléments", "Les verbes à deux compléments", "give him the book / give the book to him, et give it to me.", ["give him", "to / for"], [], "double complement"),
 ("negation.html", SY, "#fecaca", "#dc2626", "No · not", "none · never", "Syntaxe · Négation", "La négation", "not, no, none, nobody, never : une seule négation par phrase !", ["not / no", "none", "never"], [], "negation"),
 ("homophones.html", PH, "#fbcfe8", "#db2777", "Their", "there · they're", "Phonologie · Sons", "Les homophones", "there / their / they're, to / too / two, write / right… : même son, autre sens.", ["their / there", "to / too", "its / it's"], [], "homophones"),
 ("phono_cup_bird.html", PH, "#fed7aa", "#ea580c", "Cup", "cap · bird", "Phonologie · Sons", "Les sons /ʌ/, /æ/ et /ɜː/", "cup, cat, bird : trois voyelles difficiles pour les francophones.", ["/ʌ/", "/æ/", "/ɜː/"], [], "voyelles cup cat bird"),
 ("diphtongues.html", PH, "#c7d2fe", "#6366f1", "/aɪ/", "make · time · go", "Phonologie · Sons", "Les diphtongues", "make /eɪ/, time /aɪ/, go /əʊ/, now /aʊ/, boy /ɔɪ/.", ["/eɪ/", "/aɪ/", "/əʊ/"], [], "diphtongues"),
 ("graphies.html", PH, "#fde68a", "#d97706", "-ough", "ea · oo · ch", "Phonologie · Sons", "Les graphies trompeuses", "though, through, tough, cough… : une graphie, plusieurs sons.", ["-ough", "ea / oo", "ch"], [], "graphie orthographe prononciation"),
 ("accent_phrase.html", PH, "#a7f3d0", "#059669", "I WANT…", "mots pleins", "Phonologie · Accent", "L'accent de phrase", "Quels mots accentuer dans une phrase, et l'accent contrastif.", ["mots pleins", "contraste"], [], "accent de phrase"),
 ("api_intro.html", PH, "#ddd6fe", "#7c3aed", "/θ/ /ʃ/", "l'API", "Phonologie · API", "L'alphabet phonétique (API)", "Lire les symboles phonétiques des dictionnaires : /θ/, /ʃ/, /ŋ/, /ə/…", ["symboles", "lire", "ː ˈ"], [], "api alphabet phonetique"),
 ("phonemes_morphemes.html", PH, "#e9d5ff", "#9333ea", "un|happi|ness", "phonèmes", "Expert · Phonologie", "Phonèmes et morphèmes", "Compter les phonèmes, découper les mots en morphèmes (préfixe, base, suffixe).", ["phonème", "morphème"], [], "phoneme morpheme grapheme"),
 ("accent_notation.html", PH, "#c4b5fd", "#6d28d9", "/2010/", "1 · 2 · 0", "Expert · Phonologie", "La notation de l'accent", "Schémas accentuels /10/, /01/, /010/, /2010/ : accent primaire, secondaire, inaccentué.", ["/10/", "/010/", "/2010/"], [], "accent notation schema accentuel"),
 ("suffixes_accent.html", PH, "#fbcfe8", "#be185d", "-ic · -ee", "forts / faibles", "Expert · Phonologie", "Les suffixes et l'accent", "Suffixes neutres, contraignants (-ic, -ion, -ity) et accentués (-ee, -eer, -ese).", ["neutres", "contraignants", "accentués"], [], "suffixes forts faibles accentuation"),
 ("prefixes_accent.html", PH, "#bbf7d0", "#047857", "RE·cord", "re·CORD", "Expert · Phonologie", "Préfixes et paires nom / verbe", "Préfixes inaccentués (be-GIN) et paires ˈrecord / reˈcord.", ["préfixes", "nom / verbe"], [], "prefixes accentuation nom verbe"),
 ("composes_accent.html", PH, "#a5f3fc", "#0e7490", "GREENhouse", "green HOUSE", "Expert · Phonologie", "L'accent des mots composés", "Noms composés, groupes nominaux, adjectifs composés, verbes à particule.", ["noms composés", "particules"], [], "mots composes accent"),
 ("transcription_api.html", PH, "#e0e7ff", "#4338ca", "/ˈtiːtʃə/", "transcrire", "Expert · Phonologie", "La transcription phonétique", "Choisir la bonne transcription API d'un mot, et lire une transcription.", ["mot → API", "API → mot"], [], "transcription api"),
 ("reduction_vocalique.html", PH, "#fde68a", "#92400e", "/ə/", "schwa", "Expert · Phonologie", "Réduction vocalique et alternances", "Le schwa et les changements de voyelles quand l'accent se déplace (photograph / photography).", ["schwa", "alternances"], [], "reduction vocalique schwa"),
 ("rythme_anglais.html", PH, "#fca5a5", "#9f1239", "Stress", "stress-timed", "Prosodie · Rythme", "Le rythme de l'anglais", "Une langue accentuelle : les temps forts donnent le rythme.", ["stress-timed", "accents"], [], "rythme prosodie"),
 ("metre_poetique.html", PH, "#fde68a", "#b45309", "da-DUM", "iambic pentameter", "Prosodie · Poésie", "Le mètre poétique", "Iambe, trochée, anapeste, dactyle, pentamètre iambique : scander un vers.", ["iambe", "pentamètre", "scansion"], [], "metre poesie iambique pentameter shakespeare"),
 ("rimes_figures.html", PH, "#bfdbfe", "#1e40af", "ABAB", "sonnet · limerick", "Prosodie · Poésie", "Rimes et figures sonores", "Schémas de rimes, sonnet, limerick, haïku, allitération, assonance, onomatopée.", ["rimes", "sonnet", "allitération"], [], "rimes poesie sonnet alliteration"),
 ("couleurs_nombres.html", LE, "#fca5a5", "#ef4444", "Red", "one · two", "Lexique · Base", "Les couleurs et les nombres", "Les couleurs et les nombres de 1 à 100.", ["Couleurs", "Nombres", "Écoute"], [], "couleurs nombres"),
 ("calendrier.html", LE, "#93c5fd", "#2563eb", "Monday", "January", "Lexique · Base", "Les jours et les mois", "Jours, mois, on / in, today, tomorrow, yesterday.", ["Jours", "Mois", "on / in"], [], "jours mois calendrier"),
 ("pays_nationalites.html", LE, "#bbf7d0", "#15803d", "French", "Spain · Spanish", "Lexique · Monde", "Pays et nationalités", "France / French, Germany / German, the USA / American…", ["Pays", "Nationalités", "Langues"], [], "pays nationalites langues"),
 ("corps_sante.html", LE, "#fecdd3", "#e11d48", "Head", "I've got a cold", "Lexique · Santé", "Le corps et la santé", "Les parties du corps et dire où on a mal.", ["Le corps", "J'ai mal", "Écoute"], [], "corps sante malade"),
 ("technologie.html", LE, "#a5f3fc", "#0891b2", "Wi-Fi", "password · log in", "Lexique · Société", "La technologie et internet", "Appareils, internet, réseaux sociaux et verbes du numérique.", ["Appareils", "Internet", "Écoute"], [], "technologie internet numerique"),
 ("environnement.html", LE, "#86efac", "#15803d", "Green", "recycling", "Lexique · Société", "L'environnement et la nature", "La nature, l'écologie, le climat et les gestes pour la planète.", ["Nature", "Écologie", "Écoute"], [], "environnement ecologie nature climat"),
 ("fetes_traditions.html", CU, "#fcd34d", "#d97706", "Halloween", "Bonfire Night", "Culture · Traditions", "Fêtes et traditions", "Halloween, Bonfire Night, Thanksgiving, Christmas, St Patrick's Day…", ["Fêtes", "Dates", "Traditions"], [], "fetes traditions culture"),
 ("formation_mots.html", LE, "#ddd6fe", "#7c3aed", "un-…-less", "préfixes · suffixes", "Lexique · Formation", "La formation des mots", "Préfixes et suffixes : deviner le sens d'un mot inconnu.", ["préfixes", "suffixes"], [], "formation des mots prefixes suffixes"),
 ("collocations.html", LE, "#fbcfe8", "#be185d", "Make / do", "say / tell", "Lexique · Collocations", "make ou do, say ou tell…", "make / do, say / tell, bring / take, borrow / lend, miss / lose.", ["make / do", "say / tell"], [], "collocations make do"),
 ("idiomes.html", SO, "#fed7aa", "#c2410c", "Idioms", "piece of cake", "Sociolinguistique · Expressions", "Les expressions idiomatiques", "It's raining cats and dogs, break a leg, a piece of cake…", ["sens figuré", "équivalents"], [], "expressions idiomatiques idioms"),
]

CAPS = {'preterit_cap_sapver.html', 'cap_vente.html', 'cap_aide.html', 'cap_ecrit_entretien.html', 'ce_vendeuse.html', 'co_magasin.html', 'co_message.html', 'vetements.html', 'argent_shopping.html', 'co_entretien.html', 'ecriture_guidee.html', 'expression_orale.html'}
LEVELS = ["Novice", "Intermédiaire", "Avancé", "Expert"]
_L = {
 "Novice": "cu_campus_us cu_animaux_journaux cu_sports_commonwealth cu_gag cu_portraits cu_familles_presidentielles cu_bbc cu_mythes_dragons cu_jeux_de_mots cu_ecole_uk cu_famille_royale cu_geographie_usa cu_fetes_origines cu_super_heros cu_titanic cu_hip_hop cu_service_client pronoms_interrogatifs ccf_presenter cu_arthur cu_robin_hood cu_fantomes cu_consommation cu_swinging_sixties cu_sport_uk cu_cuisine_uk cu_far_west cu_hollywood cu_sports_us cu_route66 cu_villes_etats cu_litterature_jeunesse cu_londres cu_vie_uk cu_lycee_us cu_uk cu_usa cu_anglophone couleurs_nombres calendrier pays_nationalites corps_sante be_have_play present_simple present_continu adverbes_frequence pronoms_personnels possessifs articles demonstratifs pluriels there_is adjectifs imperatif like_ing prepositions heure_dates se_presenter famille meteo nourriture vetements maison metiers animaux ecole loisirs_sports transports ce_famille co_magasin phono_h questions_fermees ce_ecole co_cafe ecriture_guidee expression_orale",
 "Intermédiaire": "cu_jeux_video cu_publicite cu_migrations_vagabonds cu_irlande_atlantique cu_villes_modeles cu_travail_usa cu_juneteenth_columbus cu_national_trust cu_mark_twain cu_grands_discours cu_explorateurs cu_much_ado cu_othello cu_dystopies cu_orwell cu_polar_espions cu_sciences cu_histoire_anglais cu_revolution_americaine cu_caraibes cu_soins_ages cu_generations cu_legendes_us cu_travail cu_1066 cu_tudors cu_victoriens cu_ww1 cu_humour cu_roaring_twenties cu_prohibition cu_kennedy cu_fast_food cu_silicon_valley cu_afrique_anglophone cu_singapour cu_art cu_alaska cu_lgbt cu_ecosse_galles cu_irlande_auj cu_pilgrims cu_ellis_island cu_conquete_spatiale cu_canada cu_nouvelle_zelande cu_jamaique cu_musique cu_grandes_figures so_codes_sociaux so_accents pr_telephone pr_reclamation pr_email_pro cu_monarchie cu_institutions_uk cu_institutions_us so_registres so_british_american so_familier pr_actes_parole ordre_mots double_complement negation homophones phono_cup_bird diphtongues graphies technologie environnement fetes_traditions collocations but prepositions_mouvement quantifieurs one_ones adjectifs_composes preterit preterit_cap_sapver verbe_regulier_irregulier questions_ouvertes preterit_continu used_to futur futur_ing comparatif superlatif modaux denombrables someone_anything adverbes_maniere too_enough pronoms_reflechis so_neither both_either ago_for_since exclamatives connecteurs questions_sujet ville_directions emotions argent_shopping cap_vente cap_aide faux_amis phrasal_verbs phono_ed phono_s phono_th phono_voyelles intonation lettres_muettes accent_mot ce_vendeuse co_message ce_email co_directions",
 "Avancé": "cu_frankenstein cu_memoire cu_caricature cu_vancouver_seattle cu_nature cu_diaspora_indienne cu_ecosse_auj cu_beaute cu_ia_ecole cu_complotisme cu_mobilisations cu_porto_rico cu_salem cu_afrique_sud_auj cu_baldwin cu_religion cu_peuples_autochtones cu_windrush cu_reve_americain cu_welfare_state cu_classes_uk cu_ww2_usa cu_guerre_froide cu_blm cu_frontiere_mexique cu_sante_usa cu_peine_mort cu_hong_kong cu_romans cu_guerre_secession cu_amerindiens_societe cu_revolution_industrielle cu_suffragettes cu_blitz cu_multiculturel cu_paques_1916 cu_esclavage cu_droits_civiques cu_1929_new_deal cu_11_septembre cu_amerindiens cu_australie cu_afrique_sud cu_inde cu_shakespeare cu_medias so_tabous pr_vendre_negocier pr_prise_parole cu_empire cu_brexit cu_famine cu_troubles cu_manifest_destiny cu_red_scare cu_armes_usa pr_implicite pr_argumenter accent_phrase api_intro formation_mots idiomes rythme_anglais conjonctions_avancees substitution prepositions_dependantes modaux_complements comparatif_avance present_perfect present_perfect_continu past_perfect probabilite verbes_to_ing be_used_to causatif wish question_tags questions_indirectes relatifs subordonnees_temps conditionnel passif discours_indirect cap_ecrit_entretien formes_faibles ce_londres co_annonces ce_reseaux co_entretien",
 "Expert": "cu_espace_qui cu_logement cu_cour_supreme cu_thatcher cu_vietnam cu_elections_us so_dialectes cu_watergate cu_televangelisme phonemes_morphemes accent_notation suffixes_accent prefixes_accent composes_accent transcription_api reduction_vocalique metre_poetique rimes_figures expressions_avancees inversion phrases_clivees participiales conditionnels_mixtes subjonctif remember_to_ing connected_speech"}
LEVEL = {f + ".html": lv for lv, fs in _L.items() for f in fs.split()}

SUBS = {
 "Grammaire": [
   ("Conjugaison", "be_have_play present_simple present_continu preterit verbe_regulier_irregulier preterit_cap_sapver preterit_continu used_to present_perfect present_perfect_continu ago_for_since past_perfect futur futur_ing"),
   ("Verbes & modaux", "imperatif like_ing modaux modaux_complements probabilite verbes_to_ing be_used_to wish conditionnels_mixtes subjonctif remember_to_ing expressions_avancees"),
   ("Noms & déterminants", "articles pluriels demonstratifs possessifs there_is denombrables quantifieurs both_either"),
   ("Pronoms", "pronoms_personnels pronoms_reflechis someone_anything one_ones"),
   ("Adjectifs & adverbes", "adjectifs adjectifs_composes adverbes_frequence adverbes_maniere too_enough"),
   ("Comparaison", "comparatif superlatif comparatif_avance"),
   ("Prépositions", "prepositions prepositions_mouvement prepositions_dependantes")],
 "Syntaxe": [
   ("Questions & réponses", "questions_fermees pronoms_interrogatifs questions_ouvertes questions_sujet question_tags questions_indirectes so_neither substitution"),
   ("Liens logiques", "connecteurs but subordonnees_temps conjonctions_avancees"),
   ("Phrase complexe", "relatifs conditionnel passif discours_indirect causatif participiales"),
   ("Ordre des mots & négation", "ordre_mots double_complement negation"),
   ("Mise en relief", "exclamatives inversion phrases_clivees")],
 "Lexique": [
   ("Vie quotidienne", "couleurs_nombres ccf_presenter calendrier corps_sante se_presenter famille meteo nourriture vetements maison animaux ecole loisirs_sports transports emotions ville_directions heure_dates argent_shopping"),
   ("Société & culture", "pays_nationalites technologie environnement"),
   ("Formation & expressions", "faux_amis phrasal_verbs formation_mots collocations"),
   ("Monde du travail", "metiers cap_vente cap_aide cap_ecrit_entretien")],
 "Phonologie": [
   ("Les sons", "phono_ed phono_s phono_th phono_voyelles phono_cup_bird diphtongues phono_h lettres_muettes homophones graphies"),
   ("Accent, rythme & intonation", "accent_mot accent_phrase intonation formes_faibles connected_speech"),
   ("API & phonologie avancée", "api_intro phonemes_morphemes transcription_api accent_notation suffixes_accent prefixes_accent composes_accent reduction_vocalique"),
   ("Prosodie & poésie", "rythme_anglais metre_poetique rimes_figures")],
 "Sociolinguistique": [
   ("Registres & politesse", "so_registres so_familier so_tabous"),
   ("Variétés d'anglais", "so_british_american so_accents so_dialectes"),
   ("Codes sociaux", "so_codes_sociaux"),
   ("Expressions", "idiomes")],
 "Pragmatique": [
   ("Actes de parole", "pr_actes_parole pr_telephone pr_reclamation pr_vendre_negocier"),
   ("Implicite", "pr_implicite"),
   ("Argumenter & présenter", "pr_argumenter pr_prise_parole"),
   ("Écrit professionnel", "pr_email_pro")],
 "Culture": [
   ("Royaume-Uni : vie et institutions", "cu_ecosse_auj cu_national_trust cu_bbc cu_ecole_uk cu_famille_royale cu_classes_uk cu_humour cu_sport_uk cu_cuisine_uk cu_uk cu_vie_uk cu_londres cu_ecosse_galles cu_monarchie cu_institutions_uk cu_multiculturel cu_brexit"),
   ("Royaume-Uni : histoire", "cu_memoire cu_explorateurs cu_titanic cu_windrush cu_1066 cu_tudors cu_victoriens cu_ww1 cu_welfare_state cu_swinging_sixties cu_revolution_industrielle cu_empire cu_suffragettes cu_blitz cu_thatcher"),
   ("Irlande", "cu_irlande_atlantique cu_famine cu_paques_1916 cu_troubles cu_irlande_auj"),
   ("États-Unis : vie et institutions", "cu_cour_supreme cu_campus_us cu_familles_presidentielles cu_geographie_usa cu_reve_americain cu_fast_food cu_blm cu_frontiere_mexique cu_sante_usa cu_peine_mort cu_sports_us cu_route66 cu_silicon_valley cu_villes_etats cu_usa cu_lycee_us cu_institutions_us cu_elections_us cu_ellis_island cu_armes_usa cu_televangelisme cu_amerindiens cu_amerindiens_societe cu_alaska"),
   ("États-Unis : histoire", "cu_espace_qui cu_salem cu_juneteenth_columbus cu_revolution_americaine cu_roaring_twenties cu_prohibition cu_far_west cu_ww2_usa cu_guerre_froide cu_kennedy cu_pilgrims cu_manifest_destiny cu_esclavage cu_guerre_secession cu_1929_new_deal cu_red_scare cu_conquete_spatiale cu_droits_civiques cu_vietnam cu_watergate cu_11_septembre"),
   ("Monde anglophone", "cu_vancouver_seattle cu_diaspora_indienne cu_porto_rico cu_migrations_vagabonds cu_villes_modeles cu_sports_commonwealth cu_afrique_sud_auj cu_peuples_autochtones cu_caraibes cu_hong_kong cu_afrique_anglophone cu_singapour cu_anglophone cu_canada cu_nouvelle_zelande cu_australie cu_inde cu_afrique_sud cu_jamaique"),
   ("Légendes", "cu_mythes_dragons cu_arthur cu_robin_hood cu_fantomes cu_legendes_us"),
   ("Consommation & travail", "cu_mobilisations cu_publicite cu_travail_usa cu_soins_ages cu_service_client cu_consommation cu_travail"),
   ("Langue, sciences & religion", "cu_nature cu_ia_ecole cu_jeux_de_mots cu_sciences cu_histoire_anglais cu_religion"),
   ("Littérature & théâtre", "cu_frankenstein cu_animaux_journaux cu_mark_twain cu_shakespeare cu_othello cu_much_ado cu_romans cu_orwell cu_dystopies cu_baldwin cu_litterature_jeunesse cu_polar_espions"),
   ("Arts & société", "cu_logement cu_caricature cu_beaute cu_jeux_video cu_complotisme cu_gag cu_portraits cu_grands_discours cu_fetes_origines cu_super_heros cu_hip_hop cu_generations cu_hollywood cu_art cu_musique cu_grandes_figures cu_medias cu_lgbt fetes_traditions")],
 "Compréhension": [
   ("Compréhension écrite", "ce_famille ce_ecole ce_vendeuse ce_email ce_londres ce_reseaux"),
   ("Compréhension orale", "co_magasin co_cafe co_message co_directions co_annonces co_entretien")],
 "Production": [
   ("Écrit", "ecriture_guidee"),
   ("Oral", "expression_orale")],
}
SUB = {f + ".html": name for sec in SUBS.values() for name, fs in sec for f in fs.split()}
def rgb(h): h = h.lstrip("#"); return ",".join(str(int(h[i:i+2], 16)) for i in (0, 2, 4))
def strip_acc(s): return "".join(c for c in unicodedata.normalize("NFD", s.lower()) if unicodedata.category(c) != "Mn")

missing = [x[0] for x in A if not os.path.exists(f"{REPO}/{x[0]}")]
nolevel = [x[0] for x in A if x[0] not in LEVEL]
nosub = [x[0] for x in A if x[0] not in SUB]; assert not nosub, nosub
badsub = [f for f in SUB if f not in {x[0] for x in A}]; assert not badsub, badsub
assert not nolevel, nolevel
assert not [f for f in LEVEL if f not in {x[0] for x in A}], [f for f in LEVEL if f not in {x[0] for x in A}]
assert not missing, missing
assert len({x[0] for x in A}) == len(A)

def card(i, x):
    href, sec, a, b, big, badge, cat, title, desc, pills, tags, kw = x
    lv = LEVEL[href]
    tags = [SUB[href]] + ([CAP] if CAP in tags or href in CAPS else [])
    search = strip_acc(" ".join([title, desc, cat, badge, " ".join(pills), " ".join(tags), sec, kw, lv]))
    fs = (' style="font-size:' + ('34px' if len(big) > 9 else '42px') + '"') if len(big) > 6 else ""
    p = "\n".join(f'        <span class="pill">{H.escape(t)}</span>' for t in pills)
    return f'''  <a class="card t" href="{href}" data-level="{lv}" data-section="{sec}" data-tags="{H.escape('|'.join(tags))}" data-search="{H.escape(search)}" style="--ca:{a};--cb:{b};--crgb:{rgb(a)};animation-delay:{min(0.35 + 0.03 * i, 0.9):.2f}s">
    <div class="card-bar"></div>
    <div class="card-visual">
      <span class="lvl lvl-{LEVELS.index(lv)}">{lv}</span>
      <span class="big-label"{fs}>{H.escape(big)}</span>
      <span class="badge">{H.escape(badge)}</span>
    </div>
    <div class="card-body">
      <div class="card-category">{H.escape(cat)}</div>
      <div class="card-title">{H.escape(title)}</div>
      <div class="card-desc">{H.escape(desc)}</div>
    </div>
    <div class="card-footer">
      <div class="card-pills">
{p}
      </div>
      <span class="card-arrow">↗</span>
    </div>
  </a>'''

blocks = []
i = 0
seen_fam = set()
for sec, sdesc in SECTIONS:
    fam = FAM_OF[sec]
    if fam not in seen_fam:
        seen_fam.add(fam); flong = [l for f, l, _ in FAMS if f == fam][0]
        blocks.append(f'<div class="fam-head" data-fam="{H.escape(fam)}"><span>{H.escape(flong)}</span></div>')
    parts = []
    for name, fs in SUBS[sec]:
        items = sorted([x for x in A if x[1] == sec and SUB[x[0]] == name], key=lambda x: LEVELS.index(LEVEL[x[0]]))
        cs = []
        for x in items:
            cs.append(card(i, x)); i += 1
        parts.append(f'''  <div class="sub" data-sub="{H.escape(name)}">
    <h3 class="sub-title">{H.escape(name)}<span>{len(items)}</span></h3>
    <div class="grid">
{chr(10).join(cs)}
    </div>
  </div>''')
    blocks.append(f'''<section class="sec" data-sec="{sec}">
  <div class="sec-head"><h2>{sec}</h2><p>{H.escape(sdesc)}</p></div>
{chr(10).join(parts)}
</section>''')

SECTION_TAGS = {sec: [name for name, _ in SUBS[sec]] for sec, _ in SECTIONS}

CSS = '''
  /* ── Sections, recherche, filtres ── */
  .card.t .card-bar { background: linear-gradient(90deg, var(--ca), var(--cb)); }
  .card.t .card-visual { background: radial-gradient(ellipse at 50% 80%, rgba(var(--crgb),0.08) 0%, transparent 70%); }
  .card.t .big-label { color: var(--ca); }
  .card.t .badge { color: var(--ca); border-color: rgba(var(--crgb),0.3); background: rgba(var(--crgb),0.08); }
  .card.t .card-category { color: var(--ca); }
  .card.t:hover { border-color: rgba(var(--crgb),0.35); }
  .card.hidden, .sec.hidden { display: none; }
  .card-visual .big-label { white-space: nowrap; text-align: center; }
  .toolbar { max-width: 1100px; margin: 0 auto 10px; padding: 0 32px; animation: fadeUp 0.6s 0.35s ease both; opacity: 0; }
  .search {
    width: 100%; padding: 13px 18px 13px 44px; font-size: 15px; font-family: inherit; color: var(--text);
    background: var(--surface) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='18' height='18' fill='none' stroke='%238a8ea3' stroke-width='2' viewBox='0 0 24 24'%3E%3Ccircle cx='11' cy='11' r='7'/%3E%3Cpath d='m20 20-3.5-3.5'/%3E%3C/svg%3E") no-repeat 16px center;
    border: 1px solid var(--border); border-radius: 999px; outline: none; transition: border-color .2s;
  }
  .search:focus { border-color: #8a8ea3; }
  .tabs { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 16px; }
  .tab {
    font-family: 'Syne', sans-serif; font-weight: 700; font-size: 15px; padding: 10px 20px; border-radius: 12px; cursor: pointer;
    background: var(--surface); color: var(--muted); border: 1px solid var(--border); transition: all .2s;
  }
  .tab:hover { color: var(--text); border-color: #8a8ea3; }
  .tab.active { background: var(--text); color: var(--bg); border-color: var(--text); }
  .tab .n, .chip .n { opacity: .6; margin-left: 5px; font-size: 11px; font-family: 'DM Sans', sans-serif; font-weight: 400; }
  .chips { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px; }
  .chip {
    font-family: inherit; font-size: 13px; padding: 6px 13px; border-radius: 999px; cursor: pointer;
    background: transparent; color: var(--muted); border: 1px solid var(--border); transition: all .2s;
  }
  .chip:hover { color: var(--text); border-color: #8a8ea3; }
  .chip.active { background: rgba(255,255,255,.12); color: var(--text); border-color: var(--text); }
  .chip.cap { border-style: dashed; }
  .sec { margin-top: 34px; }
  .stabs { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; }
  .stabs[hidden] { display: none; }
  .stab { font-family: 'Syne', sans-serif; font-weight: 700; font-size: 13px; padding: 6px 14px; border-radius: 10px; cursor: pointer;
    background: transparent; color: var(--muted); border: 1px solid var(--border); transition: all .2s; }
  .stab:hover { color: var(--text); } .stab.active { background: rgba(255,255,255,.12); color: var(--text); border-color: var(--text); }
  .stab .n { opacity: .6; margin-left: 5px; font-size: 11px; font-family: 'DM Sans', sans-serif; font-weight: 400; }
  .fam-head { max-width: 1100px; margin: 46px auto -14px; padding: 0 32px; }
  .fam-head span { display: inline-block; font-size: 11px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; color: var(--muted);
    border-bottom: 2px solid var(--border); padding-bottom: 6px; }
  .fam-head.hidden { display: none; }
  .sec-head { max-width: 1100px; margin: 0 auto 16px; padding: 0 32px; display: flex; align-items: baseline; gap: 14px; flex-wrap: wrap; }
  .sec-head h2 { font-family: 'Syne', sans-serif; font-size: 24px; font-weight: 800; letter-spacing: -.5px; }
  .sec-head p { color: var(--muted); font-size: 14px; }
  .lvl { position: absolute; top: 12px; left: 14px; font-size: 10.5px; font-weight: 600; letter-spacing: .5px; text-transform: uppercase; padding: 3px 9px; border-radius: 999px; border: 1px solid; }
  .lvl-0 { color: #4ecb7f; border-color: rgba(78,203,127,.4); background: rgba(78,203,127,.08); }
  .lvl-1 { color: #60a5fa; border-color: rgba(96,165,250,.4); background: rgba(96,165,250,.08); }
  .lvl-2 { color: #fb923c; border-color: rgba(251,146,60,.4); background: rgba(251,146,60,.08); }
  .lvl-3 { color: #f472b6; border-color: rgba(244,114,182,.45); background: rgba(244,114,182,.1); }
  .levels { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px; align-items: center; }
  .levels .lab { font-size: 12px; color: var(--muted); margin-right: 4px; }
  .lv { font-family: inherit; font-size: 12.5px; padding: 6px 13px; border-radius: 999px; cursor: pointer; background: transparent; border: 1px solid var(--border); color: var(--muted); transition: all .2s; }
  .lv:hover { color: var(--text); }
  .lv.active.lvl-0, .lv.active.lvl-1, .lv.active.lvl-2, .lv.active.lvl-3 { font-weight: 600; }
  .lv:not(.active) { color: #c9ccd8; border-color: rgba(255,255,255,.55); background: transparent; }
  .lv:not(.active):hover { color: var(--text); border-color: var(--text); }
  .lv.active.lvl-0 { border-color: #4ecb7f; } .lv.active.lvl-1 { border-color: #60a5fa; } .lv.active.lvl-2 { border-color: #fb923c; } .lv.active.lvl-3 { border-color: #f472b6; }
  .lv.all.active { background: rgba(255,255,255,.12); color: var(--text); border-color: var(--text); }
  .sub { margin-top: 22px; }
  .sub.hidden { display: none; }
  .sub-title { max-width: 1100px; margin: 0 auto 12px; padding: 0 32px; font-family: 'Syne', sans-serif; font-size: 15px; font-weight: 700; color: var(--text); display: flex; align-items: center; gap: 10px; }
  .sub-title::after { content: ''; flex: 1; height: 1px; background: var(--border); }
  .sub-title span { font-family: 'DM Sans', sans-serif; font-size: 11px; font-weight: 400; color: var(--muted); border: 1px solid var(--border); border-radius: 999px; padding: 1px 8px; }
  @media (max-width: 600px) { .sub-title { padding: 0 16px; } }
  /* ── Compact : une ligne par rangée de filtres, défilement horizontal ── */
  .tabs, .stabs, .levels, .chips { flex-wrap: nowrap; overflow-x: auto; scrollbar-width: none; -webkit-overflow-scrolling: touch; padding-bottom: 2px; }
  .tabs::-webkit-scrollbar, .stabs::-webkit-scrollbar, .levels::-webkit-scrollbar, .chips::-webkit-scrollbar { display: none; }
  .tab, .lv, .chip { flex-shrink: 0; white-space: nowrap; }
  .tab { font-size: 14px; padding: 8px 16px; border-radius: 10px; }
  .chips:empty { display: none; }
  .levels .lab { white-space: nowrap; flex-shrink: 0; }
  /* Écran large : tout est visible, sur plusieurs lignes. Mobile : les rubriques passent à la ligne. */
  @media (min-width: 700px) { .tabs, .stabs, .levels, .chips { flex-wrap: wrap; overflow: visible; } }
  .chips { flex-wrap: wrap; overflow: visible; }
  .chip { white-space: normal; }
  @media (max-width: 600px) {
    .hero { padding: 26px 16px 20px; }
    .hero-tag { display: none; }
    h1 { font-size: 34px; }
    .hero-sub { font-size: 14px; margin-top: 8px; }
    .stats-bar { margin-top: 18px; gap: 16px; }
    .stat-num { font-size: 22px; }
    .stat-label { font-size: 10px; }
    .section-label { display: none; }
    .toolbar { margin-bottom: 4px; }
    .search { padding: 11px 14px 11px 40px; font-size: 14px; background-position: 13px center; }
    .tabs { margin-top: 12px; gap: 6px; }
    .tab { font-size: 13px; padding: 7px 12px; }
    .levels, .chips { margin-top: 8px; gap: 6px; }
    .lv, .chip { font-size: 12px; padding: 5px 11px; }
    .sec { margin-top: 22px; }
    .sec-head { margin-bottom: 6px; }
    .sec-head h2 { font-size: 20px; }
    .sec-head p { display: none; }
    .sub { margin-top: 14px; }
    .sub-title { font-size: 13px; margin-bottom: 8px; }
    .card-visual { height: 62px; }
    .card-visual .big-label { font-size: 30px !important; }
    .card-visual .badge { font-size: 11px; padding: 3px 10px; }
    .lvl { top: 8px; left: 10px; font-size: 9px; padding: 2px 7px; }
    .card-body { padding: 12px 16px 14px; }
    .card-category { font-size: 10px; margin-bottom: 4px; }
    .card-title { font-size: 17px; }
    .card-desc { font-size: 13px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
    .card-footer { display: none; }
    .grid { gap: 10px; }
  }
  .empty { text-align: center; color: var(--muted); padding: 40px 0; font-size: 15px; }
  /* ── Accès rapides ── */
  .quick { max-width: 1100px; margin: 0 auto 18px; padding: 0 32px; display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; animation: fadeUp 0.6s 0.3s ease both; opacity: 0; }
  .qk { display: flex; flex-direction: column; gap: 3px; padding: 14px 16px; border-radius: 14px; text-decoration: none; color: var(--text); background: var(--surface); border: 1px solid var(--border); transition: border-color .2s, transform .2s; }
  .qk:hover { transform: translateY(-2px); } .qk b { font-family: 'Syne', sans-serif; font-size: 15px; } .qk span { font-size: 12.5px; color: var(--muted); }
  .qk-1:hover { border-color: #facc15; } .qk-2:hover { border-color: #4ade80; } .qk-3:hover { border-color: #f472b6; }
  .reco { max-width: 1100px; margin: -6px auto 16px; padding: 0 32px; font-size: 14px; color: var(--muted); }
  .reco button { font-family: inherit; font-size: 13px; background: transparent; border: 1px solid var(--border); color: var(--text); border-radius: 999px; padding: 4px 12px; margin-left: 6px; cursor: pointer; }
  .card.done .card-visual::after { content: attr(data-pct); position: absolute; top: 10px; right: 12px; font-size: 10.5px; font-weight: 700; color: #fbbf24; border: 1px solid rgba(251,191,36,.45); background: rgba(15,17,23,.7); border-radius: 999px; padding: 2px 8px; }
  .card.full .card-visual::after { content: "✓ " attr(data-pct); color: #4ade80; border-color: rgba(74,222,128,.45); }
  .pbar { position: absolute; left: 0; right: 0; bottom: 0; height: 4px; background: rgba(255,255,255,.08); }
  .pbar i { display: block; height: 100%; background: #fbbf24; border-radius: 0 2px 2px 0; } .card.full .pbar i { background: #4ade80; }
  .page-footer a { color: inherit; }
  @media (max-width: 600px) {
    .quick { padding: 0 16px; gap: 6px; margin-bottom: 12px; }
    .qk { padding: 10px 8px; text-align: center; } .qk b { font-size: 12.5px; } .qk span { display: none; }
    .reco { padding: 0 16px; font-size: 13px; }
    .card.done .card-visual::after { top: 8px; right: 10px; font-size: 9px; padding: 1px 6px; }
  }
  @media (max-width: 600px) { .toolbar, .sec-head, .fam-head { padding: 0 16px; } .fam-head { margin: 30px auto -10px; } .stab { font-size: 12px; padding: 5px 11px; white-space: nowrap; } }
'''

JS = '''
<script>
(function () {
  const KEY = "ea_index_v2";
  const SECTIONS = %SECTIONS%, STAGS = %STAGS%, CAP = "CAP Sapver";
  const cards = [...document.querySelectorAll(".card.t")], secs = [...document.querySelectorAll(".sec")];
  const tabsBox = document.getElementById("tabs"), chipsBox = document.getElementById("chips"), search = document.getElementById("search"), empty = document.getElementById("empty");
  let st = { fam: "Tout", sec: "", tag: "", q: "", lvl: "" };
  const MCOUNT = %MCOUNT%;
  const LEVELS = %LEVELS%, lvBox = document.getElementById("levels");
  try { st = Object.assign(st, JSON.parse(localStorage.getItem(KEY) || "{}")); } catch (e) {}
  const P = new URLSearchParams(location.search);
  if (P.has("niveau") && LEVELS[+P.get("niveau")]) { st = { fam: "Tout", sec: "", tag: "", q: "", lvl: LEVELS[+P.get("niveau")] }; history.replaceState(null, "", location.pathname); }
  try {
    const pr = JSON.parse(localStorage.getItem("ea_progress_v1") || "null");
    if (pr && pr.pages) cards.forEach(c => {
      const f = c.getAttribute("href"), pg = pr.pages[f]; if (!pg) return;
      const n = MCOUNT[f] || Object.keys(pg.missions).length;
      const sum = Object.values(pg.missions).reduce((s, m) => s + (m.total ? Math.min(1, m.best / m.total) : 0), 0);
      const pct = Math.min(100, Math.round(sum / n * 100)), nd = Object.keys(pg.missions).length;
      c.classList.add("done"); if (pct >= 100) c.classList.add("full");
      c.querySelector(".card-visual").dataset.pct = pct + " %"; c.title = `${Math.min(nd, n)} mission${nd > 1 ? "s" : ""} sur ${n} · ${pct} % de l'activité réussie`;
      const bar = document.createElement("span"); bar.className = "pbar"; bar.innerHTML = `<i style="width:${pct}%"></i>`;
      c.querySelector(".card-visual").appendChild(bar);
    });
    const dv = localStorage.getItem("ea_devoir_last"); if (dv) document.getElementById("qkDevoir").href = "devoir.html" + dv;
    const lv = JSON.parse(localStorage.getItem("ea_level") || "null"), reco = document.getElementById("reco");
    if (lv && LEVELS[lv.lvl]) {
      reco.hidden = false;
      reco.innerHTML = `🗺️ Ton niveau conseillé : <b>${LEVELS[lv.lvl]}</b><button type="button">Afficher ces activités</button>`;
      reco.querySelector("button").onclick = () => { st.fam = "Tout"; st.sec = ""; st.tag = ""; st.q = ""; search.value = ""; st.lvl = LEVELS[lv.lvl]; apply(); };
    }
  } catch (e) {}
  const FAMS = %FAMS%, FAM_OF = {}; FAMS.forEach(f => f.secs.forEach(s => FAM_OF[s] = f.name));
  if (!st.fam) st.fam = FAM_OF[st.sec] || "Tout";
  if (st.fam !== "Tout" && !FAMS.some(f => f.name === st.fam)) st.fam = "Tout";
  if (!SECTIONS.includes(st.sec) || (st.fam !== "Tout" && FAM_OF[st.sec] !== st.fam)) st.sec = "";
  const stabsBox = document.getElementById("stabs"), famHeads = [...document.querySelectorAll(".fam-head")];
  const norm = s => s.toLowerCase().normalize("NFD").replace(/[\\u0300-\\u036f]/g, "");
  const inSec = c => (st.fam === "Tout" || FAM_OF[c.dataset.section] === st.fam) && (!st.sec || c.dataset.section === st.sec) && (!st.lvl || c.dataset.level === st.lvl);
  lvBox.innerHTML = '<span class="lab">Niveau :</span>';
  [""].concat(LEVELS).forEach((l, i) => {
    const b = document.createElement("button"); b.className = "lv " + (l ? "lvl-" + (i - 1) : "all"); b.dataset.lvl = l;
    b.textContent = l || "Tous"; b.onclick = () => { st.lvl = l; apply(); }; lvBox.appendChild(b);
  });
  ["Tout"].concat(FAMS.map(f => f.name)).forEach(f => {
    const b = document.createElement("button"); b.className = "tab"; b.dataset.fam = f;
    b.innerHTML = `${f}<span class="n">${f === "Tout" ? cards.length : cards.filter(c => FAM_OF[c.dataset.section] === f).length}</span>`;
    b.onclick = () => { st.fam = f; st.sec = ""; st.tag = ""; apply(); };
    tabsBox.appendChild(b);
  });
  function drawStabs() {
    const f = FAMS.find(x => x.name === st.fam);
    stabsBox.innerHTML = ""; stabsBox.hidden = !f || f.secs.length < 2;
    if (stabsBox.hidden) return;
    [""].concat(f.secs).forEach(s => {
      const b = document.createElement("button"); b.className = "stab" + (st.sec === s ? " active" : "");
      b.innerHTML = `${s || "Tout"}<span class="n">${cards.filter(c => (s ? c.dataset.section === s : f.secs.includes(c.dataset.section))).length}</span>`;
      b.onclick = () => { st.sec = s; st.tag = ""; apply(); };
      stabsBox.appendChild(b);
    });
  }
  function drawChips() {
    chipsBox.innerHTML = "";
    const f = FAMS.find(x => x.name === st.fam), one = st.sec || (f && f.secs.length === 1 ? f.secs[0] : "");
    let tags = one ? STAGS[one].slice() : [];
    tags = tags.filter((t, i) => tags.indexOf(t) === i);
    if (cards.some(c => inSec(c) && c.dataset.tags.split("|").includes(CAP))) tags.push(CAP);
    if (st.tag && !tags.includes(st.tag)) st.tag = "";
    tags.forEach(t => {
      const n = cards.filter(c => inSec(c) && c.dataset.tags.split("|").includes(t)).length;
      const b = document.createElement("button"); b.className = "chip" + (t === CAP ? " cap" : "") + (st.tag === t ? " active" : "");
      b.innerHTML = `${t}<span class="n">${n}</span>`;
      b.onclick = () => { st.tag = st.tag === t ? "" : t; apply(); };
      chipsBox.appendChild(b);
    });
  }
  search.value = st.q;
  search.addEventListener("input", () => { st.q = search.value; apply(); });
  function apply() {
    const words = norm(st.q).split(/\\s+/).filter(Boolean);
    let shown = 0;
    cards.forEach(c => {
      const ok = inSec(c) && (!st.tag || c.dataset.tags.split("|").includes(st.tag)) && words.every(w => c.dataset.search.includes(w));
      c.classList.toggle("hidden", !ok); if (ok) shown++;
    });
    document.querySelectorAll(".sub").forEach(s => { const n = s.querySelectorAll(".card.t:not(.hidden)").length; s.classList.toggle("hidden", !n); s.querySelector(".sub-title span").textContent = n; });
    secs.forEach(s => s.classList.toggle("hidden", !s.querySelector(".card.t:not(.hidden)")));
    famHeads.forEach(h => h.classList.toggle("hidden", !secs.some(s => FAM_OF[s.dataset.sec] === h.dataset.fam && !s.classList.contains("hidden"))));
    tabsBox.querySelectorAll(".tab").forEach(b => b.classList.toggle("active", b.dataset.fam === st.fam));
    drawStabs();
    lvBox.querySelectorAll(".lv").forEach(b => b.classList.toggle("active", b.dataset.lvl === st.lvl));
    drawChips();
    empty.hidden = shown > 0;
    try { localStorage.setItem(KEY, JSON.stringify(st)); } catch (e) {}
  }
  apply();
})();
</script>
'''.replace("%SECTIONS%", json.dumps([s for s, _ in SECTIONS], ensure_ascii=False)).replace("%LEVELS%", json.dumps(LEVELS, ensure_ascii=False)).replace("%MCOUNT%", json.dumps(MC)).replace("%STAGS%", json.dumps(SECTION_TAGS, ensure_ascii=False)).replace("%FAMS%", json.dumps([{"name": f, "long": l, "secs": ss} for f, l, ss in FAMS], ensure_ascii=False))

s = open(f"{REPO}/index.html", encoding="utf-8").read()
a = s.index('<div class="quick">') if '<div class="quick">' in s else s.index('<p class="section-label">Activités disponibles</p>')
b = s.index('<p class="page-footer">')
QUICK = ('<div class="quick">\n  <a class="qk qk-1" href="test_niveau.html"><b>🗺️ Par où commencer ?</b><span>Test de niveau</span></a>\n'
         '  <a class="qk qk-2" href="progres.html"><b>📈 Mes progrès</b><span>Scores et erreurs à revoir</span></a>\n'
         '  <a class="qk qk-3" href="devoir.html" id="qkDevoir"><b>📌 Travail de la semaine</b><span>Le travail donné par ton prof</span></a>\n</div>\n'
         '<div class="reco" id="reco" hidden></div>\n\n')
body = (QUICK + '<p class="section-label">Activités disponibles</p>\n\n<div class="toolbar">\n  <input class="search" id="search" type="search" placeholder="Rechercher une notion : prétérit, did, adjectifs, météo…" autocomplete="off">\n'
        '  <div class="tabs" id="tabs"></div>\n  <div class="stabs" id="stabs" hidden></div>\n  <div class="levels" id="levels"></div>\n  <div class="chips" id="chips"></div>\n</div>\n\n' + "\n\n".join(blocks) +
        '\n\n<p class="empty" id="empty" hidden>Aucune activité ne correspond à ta recherche.</p>\n\n')
s = s[:a] + body + s[b:]
# CSS : remplacer l'ancien bloc générique par le nouveau
s = re.sub(r"\n  /\* ── Cartes génériques.*?(?=\n  /\* ── FOOTER ── \*/)", "", s, flags=re.S)
s = re.sub(r"\n  /\* ── Sections, recherche, filtres ── \*/.*?(?=\n  /\* ── FOOTER ── \*/)", "", s, flags=re.S)
s = s.replace("  /* ── FOOTER ── */", CSS + "\n  /* ── FOOTER ── */", 1)
s = re.sub(r'<div class="stat-num" id="countActivities">\d+</div>', f'<div class="stat-num" id="countActivities">{len(A)}</div>', s)
s = re.sub(r'<div class="stat-num">\d+</div>\n      <div class="stat-label">(?:Thèmes|Sections)</div>', f'<div class="stat-num">{len(SECTIONS)}</div>\n      <div class="stat-label">Sections</div>', s)
s = re.sub(r"\n<script>\n\(function \(\) \{\n  const KEY = \"ea_index_(filter|v2)\".*?</script>\n", "\n", s, flags=re.S)
s = s.replace("</body>", JS + "</body>", 1)
s = re.sub(r'<p class="page-footer">.*?</p>', '<p class="page-footer">English Activities &nbsp;·&nbsp; Mis à jour 2026 &nbsp;·&nbsp; <a href="prof.html">Espace professeur</a></p>', s, count=1)
s = s.replace('<link rel="manifest" href="manifest.json">\n<meta name="theme-color" content="#0f1117">\n<script src="assets/ea.js"></script>\n', '')
_HEAD = '<link rel="manifest" href="manifest.json">\n<meta name="theme-color" content="#0f1117">\n<link rel="apple-touch-icon" href="assets/icon-192.png">\n<script src="assets/ea.js"></script>\n'
s = s.replace(_HEAD, '')
s = re.sub(r'\n(?:[ \t]*\n){2,}', '\n\n', s)
s = s.replace('</head>', '<link rel="manifest" href="manifest.json">\n<meta name="theme-color" content="#0f1117">\n<link rel="apple-touch-icon" href="assets/icon-192.png">\n<script src="assets/ea.js"></script>\n</head>', 1)
open(f"{REPO}/index.html", "w", encoding="utf-8").write(s)
cat = [{"f": x[0], "t": x[7], "s": x[1], "sub": SUB[x[0]], "l": LEVELS.index(LEVEL[x[0]]), "d": x[8], "m": MC.get(x[0], 1)} for x in A]
open(f"{REPO}/assets/catalog.js", "w", encoding="utf-8").write("window.EA_CATALOG = " + json.dumps(cat, ensure_ascii=False) + ";\n")
print("cards:", len(A), {sec: sum(1 for x in A if x[1] == sec) for sec, _ in SECTIONS}, {l: sum(1 for x in A if LEVEL[x[0]] == l) for l in LEVELS})
print(SECTION_TAGS)
