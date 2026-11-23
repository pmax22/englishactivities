import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
exec(open(_EA_OUT+"/content_helpers.py", encoding="utf-8").read())
exec(open(_EA_OUT+"/content6.py", encoding="utf-8").read().split("# ═════════════ SE PRÉSENTER")[0].split('exec(open(_EA_OUT+"/content_helpers.py", encoding="utf-8").read())')[1])
REGISTRY.clear()
def S(em, fr, en, alts=()):
    ans = list(en) if isinstance(en, list) else [en, *alts]
    return G("____", ans, big=(em + " " if em else "") + fr, tip=f"{fr} = <b>{ans[0]}</b>", w=260)
LEX = "Anglais · Lexique"

# ═════════════ COULEURS ET NOMBRES ═════════════
lex("couleurs_nombres.html", "Les couleurs et les nombres – Entraînement", 'Colours & <span>numbers</span>', "Les couleurs et les nombres de 1 à 100", ("#fca5a5", "#ef4444"),
  '''      <p><b>Les couleurs :</b> red (rouge) · blue (bleu) · green (vert) · yellow (jaune) · orange · pink (rose) · purple (violet) · brown (marron) · black (noir) · white (blanc) · grey (gris) · light blue (bleu clair) · dark green (vert foncé)</p>
      <p><b>Les nombres :</b> 1 one · 2 two · 3 three · 4 four · 5 five · 6 six · 7 seven · 8 eight · 9 nine · 10 ten · 11 eleven · 12 twelve · 13 thirteen · 14 fourteen · 15 fifteen · 20 twenty · 30 thirty · 40 forty · 50 fifty · 100 a hundred</p>
      <p>Entre 21 et 99 : on met un tiret → <i>twenty-one, forty-five, ninety-nine</i>. Attention : <b>forty</b> (pas fourty).</p>''',
  [V("🔴", "rouge", "red", "rouge", "read"), V("", "vert", "green", "grey", "great"), V("", "jaune", "yellow", "jelly", "orange"),
   V("", "violet", "purple", "violet", "pink"), V("", "marron", "brown", "maroon", "brain"), V("⚪", "blanc", "white", "blank", "wheat"),
   V("", "gris", "grey", "grease", "green"), V("", "rose", "pink", "rose", "purple"), V("", "15", "fifteen", "fifty", "five-teen"), V("", "40", "forty", "fourty", "fourteen"),
   V("", "12", "twelve", "twenty", "eleven"), V("", "99", "ninety-nine", "nine-nine", "nineteen-nine")],
  [S("🔴", "rouge", "red"), S("🔵", "bleu", "blue"), S("", "vert", "green"), S("", "jaune", "yellow"), S("⚫", "noir", "black"),
   S("", "13", "thirteen"), S("", "20", "twenty"), S("", "8", "eight"), S("", "50", "fifty"), S("", "100", ["a hundred", "one hundred"])],
  [L("purple", "violet", "rose", "pourpre seulement"), L("grey", "gris", "vert", "gras"), L("thirteen", "13", "30", "3"), L("thirty", "30", "13", "33"),
   L("eleven", "11", "7", "12"), L("brown", "marron", "blanc", "bronze"), L("forty-four", "44", "14", "40"), L("pink", "rose", "violet", "orange")])

# ═════════════ CALENDRIER ═════════════
lex("calendrier.html", "Les jours et les mois – Entraînement", 'Days & <span>months</span>', "Les jours, les mois et les prépositions de temps", ("#93c5fd", "#2563eb"),
  '''      <p><b>Les jours</b> (avec une majuscule !) : Monday · Tuesday · Wednesday · Thursday · Friday · Saturday · Sunday</p>
      <p><b>Les mois</b> (avec une majuscule !) : January · February · March · April · May · June · July · August · September · October · November · December</p>
      <p><b>Prépositions :</b> <span class="hl">on</span> + jour / date (on Monday, on 3rd May) · <span class="hl">in</span> + mois / saison / année (in July, in winter, in 2026)</p>
      <p>Expressions : today (aujourd'hui) · tomorrow (demain) · yesterday (hier) · the weekend · next week (la semaine prochaine) · last month (le mois dernier)</p>''',
  [V("", "mardi", "Tuesday", "Thursday", "Tuesdays"), V("", "jeudi", "Thursday", "Tuesday", "Thirsday"), V("", "mercredi", "Wednesday", "Wenesday", "Wendsday"),
   V("", "samedi", "Saturday", "Sunday", "Saterday"), V("", "août", "August", "Aout", "October"), V("", "juin", "June", "July", "Juin"),
   V("", "février", "February", "Febuary", "Fevrier"), V("", "demain", "tomorrow", "yesterday", "today"), V("", "hier", "yesterday", "tomorrow", "last day"),
   V("", "la semaine prochaine", "next week", "last week", "the week next")],
  [S("", "lundi", "Monday"), S("", "mercredi", "Wednesday"), S("", "jeudi", "Thursday"), S("", "dimanche", "Sunday"), S("", "janvier", "January"),
   S("", "mars", "March"), S("", "juillet", "July"), S("", "septembre", "September"), S("", "décembre", "December"), S("", "aujourd'hui", "today")],
  [L("Tuesday", "mardi", "jeudi", "mercredi"), L("Thursday", "jeudi", "mardi", "samedi"), L("Wednesday", "mercredi", "lundi", "vendredi"),
   L("August", "août", "avril", "octobre"), L("June", "juin", "juillet", "janvier"), L("July", "juillet", "juin", "janvier"),
   L("yesterday", "hier", "demain", "aujourd'hui"), L("tomorrow", "demain", "hier", "ce soir")],
  {"prep": ("choice", "on ou in ?", [
      C("My birthday is ____ March.", ["in", "on"], keep=True, tip="mois → in."), C("We have English ____ Monday.", ["on", "in"], keep=True, tip="jour → on."),
      C("School starts ____ September.", ["in", "on"], keep=True, tip="mois → in."), C("The party is ____ 14th July.", ["on", "in"], keep=True, tip="date → on."),
      C("It snows ____ winter.", ["in", "on"], keep=True, tip="saison → in."), C("I'll see you ____ Friday.", ["on", "in"], keep=True, tip="jour → on."),
  ])}, [M("prep", "📅", "on Monday ou in May ?", "La bonne préposition.", ["prep"], 6)], tag=LEX)

# ═════════════ PAYS ET NATIONALITÉS ═════════════
lex("pays_nationalites.html", "Pays et nationalités – Entraînement", 'Countries & <span>nationalities</span>', "Pays, nationalités et langues", ("#bbf7d0", "#15803d"),
  '''      <p>En anglais, les <b>pays</b>, les <b>nationalités</b> et les <b>langues</b> prennent toujours une <b>majuscule</b> : <span class="ex">I'm French. I speak English.</span></p>
      <table>
        <tr><th>Pays</th><th>Nationalité / langue</th><th>Pays</th><th>Nationalité / langue</th></tr>
        <tr><td>France</td><td>French</td><td>Germany</td><td>German</td></tr>
        <tr><td>England / the UK</td><td>English / British</td><td>Spain</td><td>Spanish</td></tr>
        <tr><td>the USA</td><td>American</td><td>Italy</td><td>Italian</td></tr>
        <tr><td>Ireland</td><td>Irish</td><td>China</td><td>Chinese</td></tr>
        <tr><td>Scotland</td><td>Scottish</td><td>Japan</td><td>Japanese</td></tr>
        <tr><td>Wales</td><td>Welsh</td><td>Portugal</td><td>Portuguese</td></tr>
        <tr><td>the Netherlands</td><td>Dutch</td><td>Greece</td><td>Greek</td></tr>
      </table>
      <p>Attention : <b>the</b> USA, <b>the</b> UK, <b>the</b> Netherlands.</p>''',
  [V("", "l'Allemagne", "Germany", "Allemand", "German"), V("", "l'Espagne", "Spain", "Spanish", "Espain"), V("", "chinois", "Chinese", "China", "Chinish"),
   V("", "japonais", "Japanese", "Japan", "Japanish"), V("", "néerlandais", "Dutch", "Netherlish", "Deutsch"), V("", "grec", "Greek", "Grecian", "Greece"),
   V("", "gallois", "Welsh", "Walish", "Wales"), V("", "écossais", "Scottish", "Scotch", "Scotland"), V("", "irlandais", "Irish", "Irelandish", "Ireland"), V("", "portugais", "Portuguese", "Portugish", "Portugal")],
  [S("", "la France", "France"), S("", "français", "French"), S("", "l'Allemagne", "Germany"), S("", "allemand", "German"), S("", "l'Espagne", "Spain"),
   S("", "espagnol", "Spanish"), S("", "italien", "Italian"), S("", "anglais", "English"), S("", "le Japon", "Japan"), S("", "américain", "American")],
  [L("Germany", "l'Allemagne", "la Grèce", "le Danemark"), L("Dutch", "néerlandais", "allemand", "danois"), L("Welsh", "gallois", "écossais", "irlandais"),
   L("Greece", "la Grèce", "la Guinée", "la Grande-Bretagne"), L("Japanese", "japonais", "chinois", "coréen"), L("Spanish", "espagnol", "suédois", "portugais"),
   L("Ireland", "l'Irlande", "l'Islande", "l'Écosse"), L("Scottish", "écossais", "gallois", "suédois")], tag=LEX)

# ═════════════ CORPS ET SANTÉ ═════════════
lex("corps_sante.html", "Le corps et la santé – Entraînement", 'The body & <span>health</span>', "Les parties du corps et dire où on a mal", ("#fecdd3", "#e11d48"),
  '''      <p><b>Le corps :</b> head (tête) · hair (cheveux) · face (visage) · eye (œil) · ear (oreille) · nose (nez) · mouth (bouche) · tooth / teeth (dent) · neck (cou) · shoulder (épaule) · arm (bras) · hand (main) · finger (doigt) · back (dos) · stomach (ventre) · leg (jambe) · knee (genou) · foot / feet (pied) · toe (orteil)</p>
      <p><b>Dire où on a mal :</b> <span class="ex">I've got a headache / a stomachache / toothache / a sore throat. · My leg hurts. · I've got a cold (rhume) / the flu (grippe) / a temperature (fièvre).</span></p>
      <p><b>What's the matter? / What's wrong?</b> = Qu'est-ce qui ne va pas ? · <b>Get well soon!</b> = Bon rétablissement !</p>''',
  [V("👁️", "l'œil", "eye", "ear", "eyes"), V("👂", "l'oreille", "ear", "year", "eye"), V("👃", "le nez", "nose", "knows", "neck"), V("👄", "la bouche", "mouth", "mouse", "month"),
   V("🦷", "la dent", "tooth", "teeth", "dent"), V("💪", "le bras", "arm", "army", "harm"), V("✋", "la main", "hand", "head", "main"), V("🦶", "le pied", "foot", "feet", "food"),
   V("", "le genou", "knee", "knife", "neck"), V("", "l'épaule", "shoulder", "should", "elbow"), V("", "le cou", "neck", "nick", "knee"), V("", "un rhume", "a cold", "a cough", "a hot")],
  [S("👁️", "l'œil", "eye"), S("👂", "l'oreille", "ear"), S("👃", "le nez", "nose"), S("👄", "la bouche", "mouth"), S("✋", "la main", "hand"),
   S("🦵", "la jambe", "leg"), S("", "les dents", "teeth"), S("", "les cheveux", "hair"), S("", "le doigt", "finger"), S("", "le dos", "back")],
  [L("shoulder", "l'épaule", "le coude", "le genou"), L("knee", "le genou", "le nez", "le cou"), L("headache", "mal de tête", "mal de ventre", "la tête"),
   L("toe", "l'orteil", "le doigt", "la cheville"), L("throat", "la gorge", "la langue", "le menton"), L("the flu", "la grippe", "la fièvre", "le rhume"),
   L("finger", "le doigt", "l'ongle", "l'orteil"), L("stomach", "le ventre", "le dos", "la poitrine")],
  {"pain": ("choice", "Qu'est-ce qui ne va pas ?", [
      C(None, ["I've got a headache.", "I've got a toothache.", "I've got a stomachache."], big="🤕 Il a mal à la tête."), C(None, ["I've got a sore throat.", "I've got a sore ear.", "I've got a cold head."], big="😷 Elle a mal à la gorge."),
      C(None, ["I've got a temperature.", "I've got a cold.", "I've got a headache."], big="🤒 Il a de la fièvre."), C(None, ["My back hurts.", "My back is pain.", "I hurt of my back."], big="Elle a mal au dos."),
      C(None, ["Get well soon!", "Good health!", "Be well quick!"], big="Bon rétablissement !"),
  ])}, [M("pain", "🤒", "Dire où on a mal", "headache, sore throat, temperature…", ["pain"], 5)], tag=LEX)

# ═════════════ TECHNOLOGIE ═════════════
lex("technologie.html", "La technologie et internet – Entraînement", 'Technology & <span>the internet</span>', "Le numérique, les réseaux sociaux et les écrans", ("#a5f3fc", "#0891b2"),
  '''      <p><b>Les appareils :</b> smartphone · laptop (ordinateur portable) · tablet (tablette) · screen (écran) · keyboard (clavier) · mouse (souris) · charger (chargeur) · headphones (casque) · battery (batterie)</p>
      <p><b>Internet :</b> website (site web) · password (mot de passe) · username (identifiant) · link (lien) · email · app · social media (réseaux sociaux) · post (publication) · follower · download / upload (télécharger / mettre en ligne) · search engine (moteur de recherche)</p>
      <p><b>Verbes :</b> to log in / log out (se connecter / déconnecter) · to click · to type (taper) · to save (enregistrer) · to share (partager) · to delete (supprimer) · to charge (recharger)</p>''',
  [V("💻", "l'ordinateur portable", "laptop", "portable", "computer bag"), V("⌨️", "le clavier", "keyboard", "keyword", "clavier"), V("🔋", "la batterie", "battery", "drums", "batter"),
   V("🔑", "le mot de passe", "password", "passport", "keyword"), V("🎧", "le casque (audio)", "headphones", "helmet", "headset phone"), V("", "le chargeur", "charger", "loader", "plug"),
   V("", "télécharger", "to download", "to upload", "to telecharge"), V("", "supprimer", "to delete", "to suppress", "to remove off"), V("", "les réseaux sociaux", "social media", "social nets", "social networks media"),
   V("", "se connecter", "to log in", "to connect in", "to log out")],
  [S("💻", "l'ordinateur portable", "laptop"), S("📱", "le téléphone portable", ["smartphone", "mobile phone", "mobile", "phone", "cell phone"]), S("🖱️", "la souris", "mouse"),
   S("⌨️", "le clavier", "keyboard"), S("🔋", "la batterie", "battery"), S("", "l'écran", "screen"), S("", "le mot de passe", "password"), S("", "le lien", "link"),
   S("", "le site web", ["website", "web site"]), S("", "partager", ["share", "to share"])],
  [L("screen", "l'écran", "la souris", "le clavier"), L("password", "le mot de passe", "le passeport", "le mot-clé"), L("to delete", "supprimer", "télécharger", "partager"),
   L("charger", "le chargeur", "le chargé de projet", "la batterie"), L("to upload", "mettre en ligne", "télécharger", "mettre à jour"), L("tablet", "la tablette", "la table", "le comprimé seulement"),
   L("search engine", "le moteur de recherche", "la page d'accueil", "le navigateur"), L("to log out", "se déconnecter", "se connecter", "sortir")], tag=LEX)

# ═════════════ ENVIRONNEMENT ═════════════
lex("environnement.html", "L'environnement et la nature – Entraînement", 'Environment & <span>nature</span>', "La nature, l'écologie et le climat", ("#86efac", "#15803d"),
  '''      <p><b>La nature :</b> forest (forêt) · tree (arbre) · river (rivière) · lake (lac) · mountain (montagne) · beach (plage) · sea / ocean · field (champ) · flower (fleur) · countryside (campagne)</p>
      <p><b>L'écologie :</b> pollution · climate change (changement climatique) · global warming (réchauffement climatique) · waste (déchets) · rubbish / litter (ordures) · plastic · recycling (recyclage) · renewable energy (énergie renouvelable) · endangered species (espèces menacées)</p>
      <p><b>Verbes :</b> to recycle · to protect (protéger) · to save energy (économiser l'énergie) · to waste (gaspiller) · to pollute · to reduce (réduire) · to reuse (réutiliser)</p>''',
  [V("🌲", "la forêt", "forest", "forrest", "wood land"), V("🏞️", "la rivière", "river", "rive", "lake"), V("⛰️", "la montagne", "mountain", "mountin", "hill top"),
   V("🌾", "le champ", "field", "champ", "farm"), V("♻️", "le recyclage", "recycling", "recyclation", "reusing"), V("🌡️", "le réchauffement climatique", "global warming", "climate heat", "world warming"),
   V("", "les déchets", "waste", "dejections", "west"), V("", "gaspiller", "to waste", "to spoil away", "to gasp"), V("", "protéger", "to protect", "to protege", "to defend off"),
   V("", "les espèces menacées", "endangered species", "dangerous species", "threatened spices")],
  [S("🌳", "l'arbre", "tree"), S("🌲", "la forêt", "forest"), S("🌸", "la fleur", "flower"), S("🏖️", "la plage", "beach"), S("🌊", "la mer", "sea"),
   S("", "le lac", "lake"), S("", "la pollution", "pollution"), S("", "recycler", ["recycle", "to recycle"]), S("", "la campagne", "countryside"), S("", "protéger", ["protect", "to protect"])],
  [L("countryside", "la campagne", "le pays", "le côté"), L("waste", "les déchets", "l'ouest", "la taille"), L("climate change", "le changement climatique", "la météo", "le climat seulement"),
   L("to reduce", "réduire", "produire", "rédiger"), L("renewable energy", "l'énergie renouvelable", "l'énergie nouvelle", "l'énergie nucléaire"), L("litter", "les ordures", "la litière seulement", "la lettre"),
   L("field", "le champ", "le fil", "la forêt"), L("to reuse", "réutiliser", "refuser", "recycler")], tag=LEX)

# ═════════════ FÊTES ET TRADITIONS ═════════════
lex("fetes_traditions.html", "Fêtes et traditions – Entraînement", 'Holidays & <span>traditions</span>', "Les fêtes du monde anglophone", ("#fcd34d", "#d97706"),
  '''      <table>
        <tr><th>Fête</th><th>Date</th><th>Traditions</th></tr>
        <tr><td><b>Halloween</b></td><td>31 octobre</td><td>trick or treat, pumpkins (citrouilles), costumes</td></tr>
        <tr><td><b>Bonfire Night</b> (UK)</td><td>5 novembre</td><td>fireworks (feux d'artifice), bonfires (feux de joie), Guy Fawkes</td></tr>
        <tr><td><b>Thanksgiving</b> (USA)</td><td>4e jeudi de novembre</td><td>turkey (dinde), family dinner, giving thanks</td></tr>
        <tr><td><b>Christmas</b></td><td>25 décembre</td><td>Christmas tree, presents, stockings, Father Christmas / Santa Claus, Boxing Day (26 décembre)</td></tr>
        <tr><td><b>St Patrick's Day</b> (Irlande)</td><td>17 mars</td><td>green clothes, shamrock (trèfle), parades</td></tr>
        <tr><td><b>Independence Day</b> (USA)</td><td>4 juillet</td><td>fireworks, barbecues, parades</td></tr>
        <tr><td><b>Easter</b></td><td>mars / avril</td><td>Easter eggs, egg hunt (chasse aux œufs)</td></tr>
      </table>''',
  [V("🎃", "la citrouille", "pumpkin", "pumpking", "melon"), V("🎆", "le feu d'artifice", "fireworks", "fire games", "firecrackers show"), V("🦃", "la dinde", "turkey", "Turkish", "chicken"),
   V("🎁", "le cadeau", "present", "cadeau", "packet"), V("🐣", "Pâques", "Easter", "Eastern", "Pascal"), V("☘️", "le trèfle", "shamrock", "clover leaf", "shampoo"),
   V("", "Noël", "Christmas", "Noel day", "Xmas Eve only"), V("", "le défilé", "parade", "defile", "march past"), V("", "le déguisement", "costume", "disguising", "custom"),
   V("", "le 26 décembre (UK)", "Boxing Day", "Gift Day", "Second Christmas")],
  [S("🎃", "la citrouille", "pumpkin"), S("🎆", "les feux d'artifice", "fireworks"), S("🦃", "la dinde", "turkey"), S("🎁", "le cadeau", ["present", "gift"]),
   S("🐣", "Pâques", "Easter"), S("🎄", "Noël", "Christmas"), S("", "le défilé", "parade"), S("", "la fête (soirée)", "party"), S("", "le déguisement", "costume"), S("", "fêter", ["celebrate", "to celebrate"])],
  [L("pumpkin", "la citrouille", "la pomme de terre", "le pompier"), L("Thanksgiving", "Thanksgiving", "Noël", "Pâques"), L("trick or treat", "des bonbons ou un sort", "un tour de magie", "une fête de rue"),
   L("bonfire", "un feu de joie", "un bon feu de cheminée", "une fête foraine"), L("Easter egg", "un œuf de Pâques", "un œuf de l'Est", "un œuf dur"), L("stocking", "la chaussette de Noël", "le stock", "le bas de laine"),
   L("Boxing Day", "le 26 décembre", "le jour de la boxe", "le 1er janvier"), L("parade", "le défilé", "le paradis", "la parade militaire seulement")],
  {"when": ("choice", "Quand a lieu cette fête ?", [
      C(None, ["le 31 octobre", "le 5 novembre", "le 17 mars"], big="Halloween"), C(None, ["le 5 novembre", "le 31 octobre", "le 4 juillet"], big="Bonfire Night"),
      C(None, ["le 4e jeudi de novembre", "le 25 décembre", "le 1er mai"], big="Thanksgiving"), C(None, ["le 17 mars", "le 14 février", "le 4 juillet"], big="St Patrick's Day"),
      C(None, ["le 4 juillet", "le 14 juillet", "le 5 novembre"], big="Independence Day"), C(None, ["le 26 décembre", "le 24 décembre", "le 1er janvier"], big="Boxing Day"),
  ])}, [M("when", "📆", "Quand ?", "Les dates des fêtes.", ["when"], 6)], tag="Anglais · Culture")

# ═════════════ FORMATION DES MOTS ═════════════
newpage("formation_mots.html", "La formation des mots – Entraînement", 'un<span>happy</span>, care<span>less</span>',
  "Préfixes et suffixes pour deviner le sens des mots", ("#ddd6fe", "#7c3aed"),
  '''      <h4>Les préfixes (au début)</h4>
      <table>
        <tr><th>Préfixe</th><th>Sens</th><th>Exemples</th></tr>
        <tr><td>un-, in-, im-, il-, ir-, dis-</td><td>contraire</td><td>unhappy, impossible, illegal, irregular, dislike</td></tr>
        <tr><td>re-</td><td>de nouveau</td><td>redo, rewrite, replay</td></tr>
        <tr><td>mis-</td><td>mal, de travers</td><td>misunderstand, misspell</td></tr>
        <tr><td>pre- / post-</td><td>avant / après</td><td>prehistoric, postwar</td></tr>
        <tr><td>over- / under-</td><td>trop / pas assez</td><td>overcooked, underpaid</td></tr>
      </table>
      <h4>Les suffixes (à la fin)</h4>
      <table>
        <tr><th>Suffixe</th><th>Sens / nature</th><th>Exemples</th></tr>
        <tr><td>-er, -or, -ist</td><td>la personne qui…</td><td>teacher, actor, artist</td></tr>
        <tr><td>-ful / -less</td><td>plein de / sans</td><td>careful / careless, useful / useless</td></tr>
        <tr><td>-ness, -ment, -tion, -ity</td><td>noms</td><td>happiness, movement, education, reality</td></tr>
        <tr><td>-able, -ous, -al, -ive</td><td>adjectifs</td><td>washable, famous, natural, creative</td></tr>
        <tr><td>-ly</td><td>adverbes</td><td>quickly, carefully</td></tr>
      </table>''',
  {"pref": ("choice", "Quel est le contraire ?", [
      C(None, ["unhappy", "dishappy", "inhappy"], big="happy"), C(None, ["impossible", "unpossible", "dispossible"], big="possible"), C(None, ["dislike", "unlike", "mislike"], big="like (aimer)", tip="unlike = différent de ; dislike = ne pas aimer."),
      C(None, ["illegal", "unlegal", "inlegal"], big="legal"), C(None, ["irregular", "unregular", "inregular"], big="regular"), C(None, ["uncomfortable", "incomfortable", "discomfortable"], big="comfortable"),
      C(None, ["dishonest", "unhonest", "inhonest"], big="honest"), C(None, ["unfair", "infair", "disfair"], big="fair"),
    ]),
    "suf": ("choice", "Que veut dire ce mot ?", [
      C(None, ["sans espoir, désespéré", "plein d'espoir", "qui espère trop"], big="hopeless", tip="-less = sans."), C(None, ["plein d'espoir", "sans espoir", "l'espoir"], big="hopeful", tip="-ful = plein de."),
      C(None, ["une personne qui peint", "la peinture", "peint"], big="painter", tip="-er = la personne qui…"), C(None, ["la gentillesse", "gentiment", "gentil"], big="kindness", tip="-ness = nom."),
      C(None, ["réécrire", "mal écrire", "écrire avant"], big="rewrite", tip="re- = de nouveau."), C(None, ["mal comprendre", "comprendre de nouveau", "ne pas comprendre du tout"], big="misunderstand", tip="mis- = mal."),
      C(None, ["trop cuit", "pas assez cuit", "cuit dessus"], big="overcooked", tip="over- = trop."), C(None, ["lavable", "lavé", "qui lave"], big="washable", tip="-able = qu'on peut…"),
    ]),
    "build": ("gap", "Forme le mot demandé", [
      G("care → sans soin : ____", "careless", tip="-less = sans."), G("use → utile : ____", "useful", tip="-ful = plein de."), G("happy → le bonheur : ____", "happiness", tip="-ness (y → i)."),
      G("teach → la personne qui enseigne : ____", "teacher", tip="-er."), G("do → refaire : ____", "redo", tip="re-."), G("agree → ne pas être d'accord : ____", "disagree", tip="dis-."),
  ])},
  [M("pref", "⬅️", "Les préfixes contraires", "un-, im-, il-, ir-, dis-…", ["pref"], 8),
   M("suf", "➡️", "Deviner le sens", "-less, -ful, -er, re-, mis-…", ["suf"], 8),
   M("build", "🧱", "Former un mot", "careless, useful, happiness…", ["build"], 6),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["pref", "suf", "build"], 12)], tag=LEX)

# ═════════════ COLLOCATIONS ═════════════
MD = "<b>make</b> = fabriquer, créer (a cake, a mistake, a noise, friends, a decision, money) · <b>do</b> = activité, travail (homework, the dishes, sport, a job, your best, the shopping)."
newpage("collocations.html", "make ou do, say ou tell… – Entraînement", '<span>make</span> or do?',
  "make / do, say / tell, bring / take, borrow / lend, miss / lose", ("#fbcfe8", "#be185d"),
  '''      <table>
        <tr><th>Paire</th><th>Différence</th><th>Exemples</th></tr>
        <tr><td><b>make / do</b></td><td>make = créer, fabriquer · do = activité, tâche</td><td>make a cake, a mistake, a decision, a noise, friends · do homework, the dishes, sport, your best</td></tr>
        <tr><td><b>say / tell</b></td><td>tell + personne · say (sans personne)</td><td>She told me the truth. · She said hello. · tell a story, tell a lie, tell the time</td></tr>
        <tr><td><b>bring / take</b></td><td>bring = apporter (vers moi) · take = emporter (ailleurs)</td><td>Bring me a glass. · Take your umbrella!</td></tr>
        <tr><td><b>borrow / lend</b></td><td>borrow = emprunter · lend = prêter</td><td>Can I borrow your pen? · Can you lend me your pen?</td></tr>
        <tr><td><b>miss / lose</b></td><td>miss = rater, manquer · lose = perdre</td><td>I missed the bus. · I lost my keys.</td></tr>
        <tr><td><b>look / see / watch</b></td><td>look at = regarder · see = voir · watch = regarder (TV, match)</td><td>Look at this! · I can see the sea. · watch TV</td></tr>
      </table>''',
  {"md": ("choice", "make ou do ?", [
      C("I always ____ my homework after dinner.", ["do", "make"], keep=True, tip=MD), C("Can you ____ a cake for the party?", ["make", "do"], keep=True, tip=MD),
      C("Everybody can ____ a mistake.", ["make", "do"], keep=True, tip=MD), C("I'll ____ the dishes.", ["do", "make"], keep=True, tip=MD),
      C("Don't ____ so much noise!", ["make", "do"], keep=True, tip=MD), C("She ____ a lot of sport.", ["does", "makes"], keep=True, tip=MD),
      C("It's hard to ____ friends in a new town.", ["make", "do"], keep=True, tip=MD), C("Just ____ your best!", ["do", "make"], keep=True, tip=MD),
      C("We need to ____ a decision.", ["make", "do"], keep=True, tip=MD), C("Who's going to ____ the shopping?", ["do", "make"], keep=True, tip=MD),
    ]),
    "pairs": ("choice", "Choisis le bon verbe", [
      C("Can you ____ me the time?", ["tell", "say"], keep=True, tip="tell the time / tell + personne."), C("He ____ goodbye and left.", ["said", "told"], keep=True, tip="say goodbye."),
      C("Can I ____ your pen?", ["borrow", "lend"], keep=True, tip="emprunter → borrow."), C("Can you ____ me some money?", ["lend", "borrow"], keep=True, tip="prêter → lend."),
      C("Hurry up or you'll ____ the bus!", ["miss", "lose"], keep=True, tip="rater → miss."), C("I've ____ my keys!", ["lost", "missed"], keep=True, tip="perdre → lose."),
      C("____ your umbrella, it's going to rain.", ["Take", "Bring"], keep=True, tip="emporter (ailleurs) → take."), C("Can you ____ me a glass of water, please?", ["bring", "take"], keep=True, tip="apporter (vers moi) → bring."),
      C("We ____ a film last night.", ["watched", "looked"], keep=True, tip="regarder un film → watch."), C("____ at this photo!", ["Look", "Watch", "See"], keep=True, tip="regarder (une chose fixe) → look at."),
  ])},
  [M("md", "🔨", "make ou do ?", "make a cake, do homework…", ["md"]),
   M("pairs", "⚖️", "say / tell, borrow / lend…", "Les paires qui piègent.", ["pairs"]),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["md", "pairs"], 12)], tag=LEX)

# ═════════════ IDIOMES ═════════════
def ID(en, ok, *bad): return C(None, [ok, *bad], big=en, say=en)
newpage("idiomes.html", "Les expressions idiomatiques – Entraînement", 'It\'s raining <span>cats and dogs</span>',
  "Les expressions imagées les plus courantes", ("#fed7aa", "#c2410c"),
  '''      <p>Une <span class="hl">expression idiomatique</span> a un sens <b>figuré</b> : on ne peut pas la traduire mot à mot.</p>
      <table>
        <tr><th>Expression</th><th>Sens</th><th>Équivalent français</th></tr>
        <tr><td>It's raining cats and dogs.</td><td>il pleut très fort</td><td>il pleut des cordes</td></tr>
        <tr><td>Break a leg!</td><td>bonne chance (spectacle)</td><td>merde !</td></tr>
        <tr><td>It's a piece of cake.</td><td>c'est très facile</td><td>c'est du gâteau</td></tr>
        <tr><td>to feel under the weather</td><td>être un peu malade</td><td>ne pas être dans son assiette</td></tr>
        <tr><td>to cost an arm and a leg</td><td>coûter très cher</td><td>coûter les yeux de la tête</td></tr>
        <tr><td>to be over the moon</td><td>être ravi</td><td>être aux anges</td></tr>
        <tr><td>to hit the books</td><td>étudier sérieusement</td><td>se mettre à bosser</td></tr>
        <tr><td>once in a blue moon</td><td>très rarement</td><td>tous les 36 du mois</td></tr>
        <tr><td>to have butterflies in one's stomach</td><td>avoir le trac</td><td>avoir l'estomac noué</td></tr>
        <tr><td>to let the cat out of the bag</td><td>révéler un secret</td><td>vendre la mèche</td></tr>
      </table>''',
  {"sens": ("choice", "Que veut dire cette expression ?", [
      ID("It's raining cats and dogs.", "Il pleut très fort.", "Il y a beaucoup d'animaux dehors.", "Il fait un temps de chien."),
      ID("Break a leg!", "Bonne chance !", "Fais attention à toi !", "Casse-toi !"),
      ID("It's a piece of cake.", "C'est très facile.", "C'est délicieux.", "C'est une petite part."),
      ID("I'm feeling under the weather.", "Je ne me sens pas très bien.", "J'adore la pluie.", "Je suis à l'abri."),
      ID("It costs an arm and a leg.", "Ça coûte très cher.", "C'est dangereux.", "C'est fait à la main."),
      ID("She's over the moon.", "Elle est ravie.", "Elle est dans la lune.", "Elle est astronaute."),
      ID("I need to hit the books.", "Je dois étudier sérieusement.", "Je dois ranger mes livres.", "Je suis en colère contre l'école."),
      ID("I see him once in a blue moon.", "Je le vois très rarement.", "Je le vois la nuit.", "Je le vois chaque mois."),
      ID("I've got butterflies in my stomach.", "J'ai le trac.", "J'ai mal au ventre.", "Je suis amoureux des papillons."),
      ID("He let the cat out of the bag.", "Il a révélé le secret.", "Il a libéré son chat.", "Il a fait une bêtise."),
  ])},
  [M("sens", "💬", "Le sens caché", "Que veulent vraiment dire ces expressions ?", ["sens"])], tag="Anglais · Sociolinguistique")
print("content16 ok", REGISTRY)
