import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
exec(open(_EA_OUT+"/content_helpers.py", encoding="utf-8").read())
SECTION_TAG.update({"but.html": "Anglais · Syntaxe", "substitution.html": "Anglais · Syntaxe", "conjonctions_avancees.html": "Anglais · Syntaxe"})

# ═════════════ BUT ═════════════
newpage("but.html", "Exprimer le but – Entraînement", 'I came <span>to help</span> you',
  "to, in order to, so as to, so that, for", ("#a5f3fc", "#0891b2"),
  '''      <table>
        <tr><th>Structure</th><th>Exemple</th><th>Remarque</th></tr>
        <tr><td><span class="hl">to</span> + BV</td><td>I went to the shop <b>to buy</b> bread.</td><td>le plus courant (<s>for buy</s>)</td></tr>
        <tr><td><span class="hl">in order to / so as to</span> + BV</td><td>She studies <b>in order to</b> pass her exam.</td><td>plus soutenu</td></tr>
        <tr><td><span class="hl">in order not to / so as not to</span> + BV</td><td>I left early <b>so as not to</b> miss the bus.</td><td>but négatif</td></tr>
        <tr><td><span class="hl">so that</span> + sujet + can / will / could</td><td>I'll speak slowly <b>so that</b> you can understand.</td><td>quand le sujet change</td></tr>
        <tr><td><span class="hl">for</span> + nom</td><td>I went to the shop <b>for</b> some bread.</td><td>for + nom, jamais for + verbe</td></tr>
      </table>''',
  {"choice": ("choice", "Choisis la bonne forme", [
      C("I went to the baker's ____ some bread.", ["to buy", "for buy", "for buying"], tip="but + verbe → to + BV."), C("She works hard ____ pass her exams.", ["in order to", "for", "so that"], tip="in order to + BV."),
      C("I left early ____ miss the train.", ["so as not to", "not to so", "for not"], tip="but négatif → so as not to / in order not to."), C("Speak louder ____ everyone can hear you.", ["so that", "to", "for"], tip="sujet différent → so that + can."),
      C("We went to the café ____ a coffee.", ["for", "to", "so that"], tip="for + nom."), C("He saved money ____ buy a car.", ["to", "for", "so"], tip="to + BV."),
      C("I wrote it down ____ I wouldn't forget.", ["so that", "to", "in order"], tip="so that + sujet + would / could."), C("She whispered ____ wake the baby.", ["so as not to", "for not", "to not so"], tip="but négatif."),
  ])},
  [M("choice", "🎯", "Exprimer le but", "to, in order to, so that, for…", ["choice"], 8)])

# ═════════════ PRÉPOSITIONS DÉPENDANTES ═════════════
PD = "Ces prépositions dépendent du mot qui les précède : elles s'apprennent par cœur avec lui. Après une préposition, le verbe est en -ing."
newpage("prepositions_dependantes.html", "Les prépositions dépendantes – Entraînement", 'interested <span>in</span>, good <span>at</span>',
  "Adjectifs et verbes suivis d'une préposition", ("#99f6e4", "#0f766e"),
  '''      <p>Beaucoup d'adjectifs et de verbes sont toujours suivis de la <b>même préposition</b>.</p>
      <table>
        <tr><th>Adjectif + préposition</th><th>Verbe + préposition</th></tr>
        <tr><td>interested <b>in</b> · good / bad <b>at</b> · afraid / scared <b>of</b> · proud <b>of</b> · tired <b>of</b> · fond <b>of</b> · keen <b>on</b> · famous <b>for</b> · responsible <b>for</b> · different <b>from</b> · married <b>to</b> · angry <b>with</b> (quelqu'un) / <b>about</b> (quelque chose) · worried <b>about</b> · excited <b>about</b></td>
        <td>listen <b>to</b> · look <b>at</b> · wait <b>for</b> · depend <b>on</b> · think <b>about / of</b> · belong <b>to</b> · agree <b>with</b> · apologise <b>for</b> · believe <b>in</b> · dream <b>of / about</b> · pay <b>for</b> · talk <b>to</b> (sb) <b>about</b> (sth) · ask <b>for</b></td></tr>
      </table>
      <p>Après une préposition : <b>verbe-ing</b>. <span class="ex">I'm good at drawing. · Thank you for coming.</span></p>''',
  {"adj": ("choice", "Choisis la bonne préposition", [
      C("I'm interested ____ history.", ["in", "on", "for"], keep=True, tip=PD), C("She's very good ____ maths.", ["at", "in", "on"], keep=True, tip=PD),
      C("He's afraid ____ spiders.", ["of", "from", "by"], keep=True, tip=PD), C("I'm proud ____ you!", ["of", "for", "on"], keep=True, tip=PD),
      C("Paris is famous ____ the Eiffel Tower.", ["for", "of", "by"], keep=True, tip=PD), C("This is different ____ what I expected.", ["from", "of", "at"], keep=True, tip=PD),
      C("She's married ____ a doctor.", ["to", "with", "at"], keep=True, tip=PD), C("I'm worried ____ my exam.", ["about", "of", "for"], keep=True, tip=PD),
      C("I'm tired ____ waiting!", ["of", "from", "at"], keep=True, tip=PD), C("He's keen ____ football.", ["on", "in", "of"], keep=True, tip=PD),
    ]),
    "verb": ("choice", "Choisis la bonne préposition", [
      C("I'm listening ____ music.", ["to", "at", "—"], keep=True, tip=PD), C("Look ____ this photo!", ["at", "to", "on"], keep=True, tip=PD),
      C("We're waiting ____ the bus.", ["for", "—", "after"], keep=True, tip=PD), C("It depends ____ the weather.", ["on", "of", "from"], keep=True, tip=PD),
      C("This book belongs ____ me.", ["to", "at", "of"], keep=True, tip=PD), C("I agree ____ you.", ["with", "to", "—"], keep=True, tip=PD),
      C("He apologised ____ being late.", ["for", "of", "to"], keep=True, tip=PD), C("Do you believe ____ ghosts?", ["in", "on", "to"], keep=True, tip=PD),
      C("I paid ____ the tickets.", ["for", "—", "to"], keep=True, tip=PD), C("She dreams ____ becoming a singer.", ["of", "to", "at"], keep=True, tip=PD),
  ])},
  [M("adj", "📎", "Adjectif + préposition", "interested in, good at, afraid of…", ["adj"]),
   M("verb", "🔗", "Verbe + préposition", "listen to, wait for, depend on…", ["verb"]),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["adj", "verb"], 12)])

# ═════════════ PRÉPOSITIONS DE MOUVEMENT ═════════════
PM = "into (dans, en entrant) · out of (hors de) · through (à travers) · across (en traversant une surface) · along (le long de) · up / down (en montant / descendant) · over (par-dessus) · under (sous) · past (devant, en passant) · towards (vers) · around (autour de)."
newpage("prepositions_mouvement.html", "Les prépositions de mouvement – Entraînement", 'into, <span>through</span>, across',
  "Les prépositions de mouvement et de lieu", ("#bbf7d0", "#16a34a"),
  '''      <table>
        <tr><th>Préposition</th><th>Sens</th><th>Exemple</th></tr>
        <tr><td><span class="hl">into</span> / <span class="hl">out of</span></td><td>entrer dans / sortir de</td><td>She ran into the house. · He got out of the car.</td></tr>
        <tr><td><span class="hl">through</span></td><td>à travers (un volume)</td><td>We walked through the forest.</td></tr>
        <tr><td><span class="hl">across</span></td><td>d'un côté à l'autre (surface)</td><td>They swam across the river.</td></tr>
        <tr><td><span class="hl">along</span></td><td>le long de</td><td>I walked along the beach.</td></tr>
        <tr><td><span class="hl">up</span> / <span class="hl">down</span></td><td>en montant / en descendant</td><td>He climbed up the stairs.</td></tr>
        <tr><td><span class="hl">over</span> / <span class="hl">under</span></td><td>par-dessus / dessous</td><td>The cat jumped over the wall.</td></tr>
        <tr><td><span class="hl">past</span></td><td>devant (en passant)</td><td>We drove past the school.</td></tr>
        <tr><td><span class="hl">towards</span> / <span class="hl">around</span></td><td>vers / autour de</td><td>She walked towards me.</td></tr>
      </table>
      <p>Lieu (sans mouvement) : <i>in, on, at, next to, behind, in front of, between, opposite, under, above</i>.</p>''',
  {"choice": ("choice", "Choisis la bonne préposition", [
      C("The cat jumped ____ the wall.", ["over", "through", "into"], tip=PM), C("We walked ____ the forest.", ["through", "across", "over"], tip=PM),
      C("She ran ____ the house to get her bag.", ["into", "in", "through"], tip="entrer dans → into."), C("They swam ____ the river.", ["across", "through", "along"], tip=PM),
      C("He got ____ the car.", ["out of", "out", "off from"], tip=PM), C("I like walking ____ the beach.", ["along", "across", "through"], tip=PM),
      C("He climbed ____ the stairs to his room.", ["up", "on", "over"], tip=PM), C("The train went ____ a tunnel.", ["through", "across", "over"], tip=PM),
      C("We drove ____ the school but didn't stop.", ["past", "through", "into"], tip=PM), C("The dog ran ____ me.", ["towards", "to at", "into to"], tip=PM),
      C("The children walked ____ the lake.", ["around", "through", "into"], tip=PM), C("The ball rolled ____ the table.", ["under", "into", "through"], tip=PM),
  ])},
  [M("choice", "🏃", "Les prépositions de mouvement", "into, through, across, along…", ["choice"], 12)])

# ═════════════ MODAUX : COMPLÉMENTS ═════════════
newpage("modaux_complements.html", "Modaux : could, be able to, had better… – Entraînement", 'could, <span>had better</span>, needn\'t…',
  "Capacité au passé, conseil, absence d'obligation, préférence", ("#c7d2fe", "#4338ca"),
  '''      <table>
        <tr><th>Modal</th><th>Sens</th><th>Exemple</th></tr>
        <tr><td><span class="hl">could</span></td><td>capacité générale au passé</td><td>I could swim when I was five.</td></tr>
        <tr><td><span class="hl">was / were able to</span></td><td>réussir à (une fois, au passé)</td><td>The fire was big, but we were able to escape.</td></tr>
        <tr><td><span class="hl">will be able to</span></td><td>capacité au futur (<s>will can</s>)</td><td>You will be able to drive next year.</td></tr>
        <tr><td><span class="hl">had better</span> ('d better) + BV</td><td>ferait mieux de (conseil fort)</td><td>You'd better hurry!</td></tr>
        <tr><td><span class="hl">ought to</span> + BV</td><td>devrait (= should)</td><td>You ought to see a doctor.</td></tr>
        <tr><td><span class="hl">needn't</span> / don't need to + BV</td><td>pas besoin de</td><td>You needn't come. It's optional.</td></tr>
        <tr><td><span class="hl">would rather</span> ('d rather) + BV</td><td>préférer</td><td>I'd rather stay at home.</td></tr>
        <tr><td><span class="hl">would like</span> + to + BV</td><td>aimerait</td><td>I'd like to travel.</td></tr>
      </table>''',
  {"choice": ("choice", "Choisis le bon modal", [
      C("When I was six, I ____ ride a bike.", ["could", "can", "will be able to"], tip="capacité au passé → could."),
      C("The exam was hard, but I ____ answer all the questions.", ["was able to", "can", "could have"], tip="réussir à, une fois → was able to."),
      C("Next year, you ____ vote.", ["will be able to", "will can", "can to"], tip="futur → will be able to."),
      C("It's late. You ____ go home.", ["'d better", "'d rather", "needn't"], tip="conseil fort → had better."),
      C("You ____ see a doctor about that cough.", ["ought to", "ought", "needn't to"], tip="ought to + BV = should."),
      C("You ____ bring anything. We have everything.", ["needn't", "mustn't", "'d better"], tip="pas besoin → needn't."),
      C("I ____ stay at home tonight. I'm tired.", ["'d rather", "'d better to", "ought"], tip="préférence → would rather + BV."),
      C("____ you like a cup of tea?", ["Would", "Had", "Ought"], tip="proposition polie → Would you like…?"),
      C("He ____ speak English when he arrived in London.", ["couldn't", "can't", "won't be able"], tip="incapacité au passé → couldn't."),
      C("We ____ wear a uniform, but most students do.", ["don't need to", "mustn't", "had better not"], tip="pas obligatoire → don't need to."),
  ])},
  [M("choice", "🧰", "Les autres modaux", "could, be able to, had better, ought to, needn't, would rather.", ["choice"])])

# ═════════════ QUANTIFIEURS ═════════════
newpage("quantifieurs.html", "all, every, each, most – Entraînement", '<span>all</span>, every, each, most',
  "Les quantifieurs", ("#fef3c7", "#d97706"),
  '''      <table>
        <tr><th>Mot</th><th>Sens</th><th>Construction</th><th>Exemple</th></tr>
        <tr><td><span class="hl">all</span></td><td>tous, tout</td><td>all + pluriel / indénombrable · all (of) the…</td><td>All students must come. · all the time</td></tr>
        <tr><td><span class="hl">every</span></td><td>chaque, tous (en général)</td><td>every + <b>singulier</b></td><td>Every student has a book. · every day</td></tr>
        <tr><td><span class="hl">each</span></td><td>chaque (un par un)</td><td>each + singulier · each of + pluriel</td><td>Each player has a number.</td></tr>
        <tr><td><span class="hl">most</span></td><td>la plupart</td><td>most + nom (général) · most <b>of the</b> + nom (précis)</td><td>Most people like music. · Most of my friends play football.</td></tr>
        <tr><td><span class="hl">whole</span></td><td>tout, entier</td><td>the whole + singulier</td><td>the whole day</td></tr>
        <tr><td><span class="hl">none of</span></td><td>aucun de</td><td>none of + pluriel</td><td>None of my friends came.</td></tr>
      </table>
      <p>Attention : <span class="ex">most people <s>the most people</s></span> · <span class="ex">every day = tous les jours</span> mais <span class="ex">all day = toute la journée</span>.</p>''',
  {"choice": ("choice", "Choisis le bon mot", [
      C("____ student has a laptop.", ["Every", "All", "Most"], tip="every + singulier."), C("____ students must wear a uniform.", ["All", "Every", "Each"], tip="all + pluriel."),
      C("____ people like holidays.", ["Most", "The most", "Most of"], tip="général → most (sans the)."), C("____ my friends play football.", ["Most of", "Most", "The most"], tip="groupe précis → most of + my / the."),
      C("I go to school ____ day.", ["every", "all", "each of"], tip="tous les jours → every day."), C("It rained ____ day. (toute la journée)", ["all", "every", "each"], tip="toute la journée → all day."),
      C("____ of the players got a medal.", ["Each", "Every", "All of each"], tip="each of + pluriel (every of n'existe pas)."), C("I read the ____ book in one night.", ["whole", "all", "every"], tip="le livre entier → the whole book."),
      C("____ of my friends came. I was alone.", ["None", "No", "Not"], tip="aucun de → none of."), C("She spent ____ her money on clothes.", ["all", "every", "each"], tip="all + indénombrable."),
  ])},
  [M("choice", "🔢", "all, every, each, most…", "Choisis le bon quantifieur.", ["choice"])])

# ═════════════ ONE / ONES ═════════════
newpage("one_ones.html", "one / ones – Entraînement", 'the red <span>one</span>',
  "Remplacer un nom par one / ones", ("#fbcfe8", "#db2777"),
  '''      <p>Pour ne pas répéter un nom <b>dénombrable</b>, on le remplace par <span class="hl">one</span> (singulier) ou <span class="hl">ones</span> (pluriel).</p>
      <p class="ex">I don't like this T-shirt. I prefer the red <b>one</b>. · These shoes are too small. Have you got bigger <b>ones</b>?</p>
      <p>Questions : <span class="ex">Which one? Which ones?</span></p>
      <p>Pas de one avec un <b>indénombrable</b> : <span class="ex">I like white wine more than red. <s>red one</s></span>. Pas de one après un possessif : <span class="ex">my car and yours <s>your one</s></span>.</p>''',
  {"choice": ("choice", "one, ones ou rien ?", [
      C("I don't like this dress. I prefer the blue ____ .", ["one", "ones", "—"], keep=True, tip="dress = singulier → one."), C("These apples are bad. Can I have some fresh ____ ?", ["ones", "one", "—"], keep=True, tip="pluriel → ones."),
      C("Which ____ do you want, the big one or the small one?", ["one", "ones", "—"], keep=True, tip="choix au singulier → which one."), C("My shoes are old. I need new ____ .", ["ones", "one", "—"], keep=True, tip="shoes = pluriel → ones."),
      C("I prefer white bread to brown ____ .", ["—", "one", "ones"], keep=True, tip="bread est indénombrable → pas de one."), C("This is my bike and that's ____ .", ["yours", "your one", "your ones"], tip="après un possessif → yours (pas your one)."),
      C("Which ____ are yours, the black ones?", ["ones", "one", "—"], keep=True, tip="pluriel → which ones."), C("There are two cakes. I'll take the chocolate ____ .", ["one", "ones", "—"], keep=True, tip="un gâteau → one."),
  ])},
  [M("choice", "☝️", "one, ones ou rien ?", "Éviter de répéter un nom.", ["choice"], 8)])

# ═════════════ ADJECTIFS COMPOSÉS ═════════════
newpage("adjectifs_composes.html", "Les adjectifs composés – Entraînement", 'a ten-<span>year</span>-old boy',
  "Les adjectifs composés", ("#f5d0fe", "#a21caf"),
  '''      <p>Un <span class="hl">adjectif composé</span> est formé de plusieurs mots reliés par des <b>traits d'union</b>. Il se place <b>avant le nom</b> et, comme tout adjectif, il est <b>invariable</b> : pas de -s !</p>
      <table>
        <tr><th>Formation</th><th>Exemple</th></tr>
        <tr><td>nombre + nom (singulier)</td><td>a <b>ten-year-old</b> boy · a <b>two-hour</b> film · a <b>five-star</b> hotel</td></tr>
        <tr><td>adjectif + nom-ed</td><td>a <b>blue-eyed</b> girl · a <b>long-haired</b> cat · a <b>left-handed</b> player</td></tr>
        <tr><td>adjectif / adverbe + participe</td><td>a <b>well-known</b> singer · a <b>good-looking</b> man · a <b>hard-working</b> student</td></tr>
        <tr><td>nom + participe</td><td>a <b>home-made</b> cake · a <b>heart-breaking</b> story</td></tr>
      </table>
      <p class="ex">The boy is ten years old. → He is a ten-year-old boy. <s>a ten-years-old boy</s></p>''',
  {"choice": ("choice", "Choisis le bon adjectif composé", [
      C("My brother is ten years old. He's a ____ boy.", ["ten-year-old", "ten-years-old", "ten year olds"], tip="adjectif invariable : year sans s."),
      C("The film lasts two hours. It's a ____ film.", ["two-hour", "two-hours", "two hours'"], tip="nombre + nom au singulier."),
      C("She has blue eyes. She's a ____ girl.", ["blue-eyed", "blue-eyes", "eyed-blue"], tip="adjectif + nom-ed."),
      C("Everyone knows this singer. He's a ____ singer.", ["well-known", "good-known", "well-knowing"], tip="well + participe passé."),
      C("My grandma made this cake herself. It's a ____ cake.", ["home-made", "house-made", "made-home"], tip="home-made = fait maison."),
      C("He works very hard. He's a ____ student.", ["hard-working", "hard-worked", "working-hard"], tip="hard-working = travailleur."),
      C("The hotel has five stars. It's a ____ hotel.", ["five-star", "five-stars", "five stars'"], tip="nombre + nom au singulier."),
      C("The walk is three kilometres long. It's a ____ walk.", ["three-kilometre", "three-kilometres", "three kilometres long"], tip="nombre + nom au singulier."),
  ])},
  [M("choice", "🔗", "Les adjectifs composés", "a ten-year-old boy, a blue-eyed girl…", ["choice"], 8)])

# ═════════════ COMPARATIF AVANCÉ ═════════════
newpage("comparatif_avance.html", "Le comparatif : compléments – Entraînement", 'The more, <span>the better</span>',
  "Comparatif progressif, double comparatif, as… as possible, comparatif des adverbes", ("#99f6e4", "#0d9488"),
  '''      <table>
        <tr><th>Structure</th><th>Sens</th><th>Exemple</th></tr>
        <tr><td><span class="hl">the</span> + comparatif…, <span class="hl">the</span> + comparatif</td><td>plus… plus…</td><td>The more you practise, the better you get.</td></tr>
        <tr><td>comparatif <span class="hl">and</span> comparatif</td><td>de plus en plus</td><td>It's getting colder and colder. · more and more expensive</td></tr>
        <tr><td><span class="hl">as</span> + adj / adv + <span class="hl">as possible</span></td><td>aussi… que possible</td><td>Come as soon as possible. · as quickly as possible</td></tr>
        <tr><td><span class="hl">not as / not so</span> + adj + <span class="hl">as</span></td><td>pas aussi… que</td><td>He isn't as tall as his brother.</td></tr>
        <tr><td>comparatif des <b>adverbes</b></td><td>more quickly, faster, better, harder</td><td>She runs faster than me. · Drive more carefully!</td></tr>
        <tr><td><span class="hl">much / far / a bit</span> + comparatif</td><td>beaucoup / un peu plus</td><td>much bigger · a bit cheaper</td></tr>
      </table>''',
  {"choice": ("choice", "Choisis la bonne forme", [
      C("The more you read, ____ you write.", ["the better", "better", "the best"], tip="the + comparatif…, the + comparatif."),
      C("It's getting ____ .", ["colder and colder", "more cold and cold", "the colder"], tip="de plus en plus → comparatif and comparatif."),
      C("Please answer ____ .", ["as soon as possible", "as soon possible", "soon as possible"], tip="as + adv + as possible."),
      C("My sister isn't ____ me.", ["as tall as", "as tall than", "so tall like"], tip="not as + adj + as."),
      C("She speaks English ____ than her brother.", ["better", "more good", "more well"], tip="well → better."),
      C("Could you drive ____ , please?", ["more slowly", "slowlier", "more slow"], tip="adverbe long → more + adverbe."),
      C("This phone is ____ more expensive than the other one.", ["much", "very", "more"], tip="beaucoup plus → much + comparatif (pas very)."),
      C("Life is becoming ____ expensive.", ["more and more", "more expensive and", "the more"], tip="de plus en plus + adj long → more and more."),
      C("The ____ , the merrier!", ["more", "most", "much"], tip="expression : the more, the merrier (plus on est de fous…)."),
      C("He works ____ than anyone else.", ["harder", "more hardly", "more hard"], tip="hard → harder."),
  ])},
  [M("choice", "📈", "Le comparatif avancé", "the more… the more, more and more, as… as possible…", ["choice"])])

# ═════════════ SUBSTITUTION ET ELLIPSE ═════════════
newpage("substitution.html", "Substitution et ellipse – Entraînement", 'I think <span>so</span> / I hope <span>not</span>',
  "Éviter les répétitions : so, not, do, to", ("#e0e7ff", "#6366f1"),
  '''      <p>En anglais, on évite de répéter une phrase entière grâce à de petits mots.</p>
      <table>
        <tr><th>Structure</th><th>Exemple</th><th>Sens</th></tr>
        <tr><td>think / hope / guess / suppose + <span class="hl">so</span></td><td>Is it going to rain? — I think so.</td><td>je pense que oui</td></tr>
        <tr><td>hope / think + <span class="hl">not</span> · I don't think <span class="hl">so</span></td><td>Is it going to rain? — I hope not. / I don't think so.</td><td>j'espère que non / je ne pense pas</td></tr>
        <tr><td>auxiliaire seul</td><td>Do you like it? — Yes, I do. · She can swim, but I can't.</td><td>reprise du verbe</td></tr>
        <tr><td><span class="hl">to</span> seul (ellipse)</td><td>Would you like to come? — I'd love to.</td><td>to remplace le verbe</td></tr>
        <tr><td><span class="hl">do so</span> (soutenu)</td><td>He promised to call, but he didn't do so.</td><td>le faire</td></tr>
      </table>''',
  {"choice": ("choice", "Choisis la bonne réponse", [
      C("Is the shop open today? — I think ____ .", ["so", "it", "yes"], tip="I think so = je pense que oui."),
      C("Will it rain tomorrow? — I hope ____ .", ["not", "no", "don't"], tip="j'espère que non → I hope not."),
      C("Is Tom coming? — I don't think ____ .", ["so", "not", "it"], tip="je ne pense pas → I don't think so."),
      C("Would you like to come to my party? — I'd love ____ !", ["to", "it", "so"], tip="ellipse → I'd love to."),
      C("Do you speak Spanish? — Yes, I ____ .", ["do", "speak", "am"], tip="reprise par l'auxiliaire → do."),
      C("She can play the piano, but her brother ____ .", ["can't", "doesn't", "isn't"], tip="reprise par l'auxiliaire → can't."),
      C("Are you coming with us? — I'm afraid ____ .", ["not", "no", "so not"], tip="I'm afraid not = malheureusement non."),
      C("Did you finish your homework? — I tried ____ , but it was too hard.", ["to", "it", "so"], tip="ellipse → I tried to."),
  ])},
  [M("choice", "✂️", "Éviter les répétitions", "I think so, I hope not, I'd love to…", ["choice"], 8)])

# ═════════════ CONJONCTIONS AVANCÉES ═════════════
CJ = "unless = sauf si · in case = au cas où · as long as / provided that = à condition que · whereas = alors que (contraste) · even though = même si / bien que · despite / in spite of + nom ou -ing = malgré."
newpage("conjonctions_avancees.html", "Conjonctions avancées – Entraînement", 'unless, <span>in case</span>, whereas',
  "Condition, contraste, concession", ("#fecdd3", "#be123c"),
  '''      <table>
        <tr><th>Mot</th><th>Sens</th><th>Exemple</th></tr>
        <tr><td><span class="hl">unless</span></td><td>sauf si (= if… not)</td><td>We'll go out unless it rains.</td></tr>
        <tr><td><span class="hl">in case</span></td><td>au cas où</td><td>Take an umbrella in case it rains.</td></tr>
        <tr><td><span class="hl">as long as / provided that</span></td><td>à condition que</td><td>You can go out as long as you're back by 10.</td></tr>
        <tr><td><span class="hl">whereas / while</span></td><td>alors que (contraste)</td><td>I like tea, whereas my sister prefers coffee.</td></tr>
        <tr><td><span class="hl">although / even though</span></td><td>bien que, même si</td><td>Even though he was tired, he kept working.</td></tr>
        <tr><td><span class="hl">despite / in spite of</span> + nom / -ing</td><td>malgré</td><td>Despite the rain, we went out. · in spite of being tired</td></tr>
        <tr><td><span class="hl">however / nevertheless</span></td><td>cependant, néanmoins</td><td>It was expensive. However, we bought it.</td></tr>
      </table>
      <p>Attention : <b>despite</b> n'est jamais suivi d'une phrase complète : <span class="ex">despite <s>it was raining</s> → despite the rain / although it was raining</span>.</p>''',
  {"choice": ("choice", "Choisis la bonne conjonction", [
      C("We'll go to the beach ____ it rains.", ["unless", "in case", "whereas"], tip=CJ), C("Take a jacket ____ it gets cold.", ["in case", "unless", "despite"], tip=CJ),
      C("You can borrow my car ____ you drive carefully.", ["as long as", "despite", "whereas"], tip=CJ), C("I love the mountains, ____ my wife prefers the sea.", ["whereas", "in case", "unless"], tip=CJ),
      C("____ the rain, we went for a walk.", ["Despite", "Although", "Even though"], tip="despite + nom."), C("____ it was raining, we went for a walk.", ["Although", "Despite", "In spite of"], tip="although + phrase complète."),
      C("____ he's very rich, he's not happy.", ["Even though", "Despite", "Unless"], tip=CJ), C("The hotel was expensive. ____, it was very comfortable.", ["However", "Whereas", "Unless"], tip="However en début de phrase."),
      C("I'll lend you the money ____ you pay me back next week.", ["provided that", "unless", "in spite of"], tip=CJ), C("In spite of ____ tired, she finished the race.", ["being", "she was", "be"], tip="in spite of + -ing."),
  ])},
  [M("choice", "🧷", "Conjonctions avancées", "unless, in case, whereas, despite…", ["choice"])])

# ═════════════ EXPRESSIONS AVANCÉES ═════════════
newpage("expressions_avancees.html", "Expressions verbales avancées – Expert", 'It\'s <span>worth</span> seeing',
  "It's worth -ing, there's no point -ing, would rather + prétérit, gérondif sujet…", ("#fef9c3", "#a16207"),
  '''      <table>
        <tr><th>Expression</th><th>Sens</th><th>Exemple</th></tr>
        <tr><td><span class="hl">It's worth</span> + -ing</td><td>ça vaut la peine de</td><td>This museum is worth visiting.</td></tr>
        <tr><td><span class="hl">There's no point</span> (in) + -ing</td><td>ça ne sert à rien de</td><td>There's no point in arguing.</td></tr>
        <tr><td><span class="hl">can't help</span> + -ing</td><td>ne pas pouvoir s'empêcher de</td><td>I can't help laughing.</td></tr>
        <tr><td><span class="hl">look forward to</span> + -ing</td><td>avoir hâte de</td><td>I look forward to seeing you.</td></tr>
        <tr><td><span class="hl">would rather</span> + sujet + <b>prétérit</b></td><td>préférer que quelqu'un…</td><td>I'd rather you stayed. (je préférerais que tu restes)</td></tr>
        <tr><td>gérondif <b>sujet</b></td><td>le fait de…</td><td>Swimming is good for your health.</td></tr>
        <tr><td><span class="hl">the</span> + adjectif</td><td>une catégorie de personnes</td><td>the rich, the poor, the elderly, the young</td></tr>
        <tr><td><span class="hl">be about to</span> + BV</td><td>être sur le point de</td><td>The film is about to start.</td></tr>
      </table>''',
  {"choice": ("choice", "Choisis la bonne forme", [
      C("This film is really worth ____ .", ["seeing", "to see", "see"], tip="worth + -ing."), C("There's no point ____ . He won't change his mind.", ["arguing", "to argue", "argue"], tip="no point (in) + -ing."),
      C("I can't help ____ when I see him.", ["laughing", "to laugh", "laugh"], tip="can't help + -ing."), C("I look forward to ____ from you.", ["hearing", "hear", "heard"], tip="to est une préposition → -ing."),
      C("I'd rather you ____ smoke in the house.", ["didn't", "don't", "won't"], tip="would rather + sujet + prétérit."), C("____ is good for your health.", ["Swimming", "Swim", "To swimming"], tip="gérondif sujet → -ing."),
      C("The government should help ____ .", ["the poor", "the poors", "poor people's"], tip="the + adjectif (invariable) = les pauvres."), C("Hurry up! The train is ____ leave.", ["about to", "about", "near to"], tip="be about to + BV."),
      C("I'd rather ____ at home tonight.", ["stay", "stayed", "to stay"], tip="would rather + BV quand le sujet est le même."), C("Is it worth ____ to the museum?", ["going", "to go", "go"], tip="worth + -ing."),
  ])},
  [M("choice", "🎓", "Expressions avancées", "worth -ing, no point -ing, would rather you…", ["choice"])], tag="Anglais · Expert · Grammaire")
print("content13 ok", REGISTRY)
