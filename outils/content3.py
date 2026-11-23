import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
exec(open(_EA_OUT+"/content_helpers.py", encoding="utf-8").read())

# ═════════════ LIKE + ING ═════════════
newpage("like_ing.html", "Exprimer ses goûts – Entraînement", 'I like <span>playing</span>',
  "love, like, enjoy, don't mind, don't like, hate + verbe-ing", ("#f9a8d4", "#ec4899"),
  '''      <p>Pour parler de ses <b>goûts</b>, on utilise un verbe de goût suivi d'un verbe en <span class="hl">-ing</span>.</p>
      <div class="formula">❤️❤️ <b>love</b> · ❤️ <b>like</b> / <b>enjoy</b> · 😐 <b>don't mind</b> · 👎 <b>don't like</b> · 👎👎 <b>hate</b> &nbsp;+ verbe<span class="hl">-ing</span></div>
      <p class="ex">I love swimming. · She hates getting up early. · He doesn't mind doing the dishes.</p>
      <p><b>Orthographe :</b> swim → swi<b>mming</b> · dance → danc<b>ing</b> · run → ru<b>nning</b> · play → play<b>ing</b>.</p>
      <p>On peut aussi utiliser un nom : <span class="ex">I like pizza.</span> · Question : <span class="ex">Do you like dancing? — Yes, I do. / No, I don't.</span></p>''',
  {
    "gap": ("gap", "Complète avec le verbe en -ing", [
      G("I love ____ .", "swimming", "swim", tip="swim → swimming (consonne doublée)."), G("She hates ____ up early.", "getting", "get", tip="get → getting."),
      G("He enjoys ____ video games.", "playing", "play", tip="play → playing."), G("We don't like ____ .", "running", "run", tip="run → running."),
      G("Do you like ____ ?", "dancing", "dance", tip="dance → dancing (-e enlevé)."), G("My dad doesn't mind ____ .", "cooking", "cook", tip="cook → cooking."),
      G("I hate ____ my room.", "tidying", "tidy", tip="tidy → tidying (le y reste)."), G("They love ____ to music.", "listening", "listen", tip="listen → listening."),
      G("She likes ____ books.", "reading", "read", tip="read → reading."), G("He hates ____ the bus.", "taking", "take", tip="take → taking."),
      G("I enjoy ____ letters.", "writing", "write", tip="write → writing."), G("We like ____ in the park.", "walking", "walk", tip="walk → walking."),
    ]),
    "choice": ("choice", "Quelle phrase est correcte ?", [
      C(None, ["I like playing tennis.", "I like play tennis.", "I like to playing tennis."], tip="like + verbe-ing."),
      C(None, ["She hates cooking.", "She hates cook.", "She hate cooking."], tip="she → hates + verbe-ing."),
      C(None, ["Do you enjoy reading?", "Do you enjoy read?", "Are you enjoy reading?"], tip="Do + sujet + enjoy + verbe-ing ?"),
      C(None, ["He doesn't like swimming.", "He doesn't likes swimming.", "He don't like swimming."], tip="doesn't + like + verbe-ing."),
      C(None, ["I don't mind waiting.", "I don't mind wait.", "I not mind waiting."], tip="don't mind + verbe-ing."),
      C(None, ["They love dancing.", "They love danceing.", "They loves dancing."], tip="dance → dancing ; they → love."),
    ]),
    "order": ("order", "Remets les mots dans l'ordre", [
      O("I|love|playing|football.", fr="J'adore jouer au football.", trap="play"), O("She|doesn't like|getting up|early.", fr="Elle n'aime pas se lever tôt.", trap="get up"),
      O("Do|you|enjoy|cooking?", fr="Tu aimes cuisiner ?", trap="cook"), O("He|hates|doing|his homework.", fr="Il déteste faire ses devoirs.", trap="do"),
      O("We|don't mind|walking.", fr="Ça ne nous dérange pas de marcher.", trap="walk"), O("My sister|loves|singing.", fr="Ma sœur adore chanter.", trap="love"),
    ]),
    "tr": ("choice", "Quelle est la bonne traduction ?", [
      C(None, ["I love swimming.", "I hate swimming.", "I don't mind swimming."], fr="J'adore nager."),
      C(None, ["She hates running.", "She loves running.", "She likes running."], fr="Elle déteste courir."),
      C(None, ["He doesn't mind cooking.", "He doesn't like cooking.", "He hates cooking."], fr="Ça ne le dérange pas de cuisiner."),
      C(None, ["We don't like shopping.", "We don't mind shopping.", "We like shopping."], fr="Nous n'aimons pas faire les magasins."),
      C(None, ["They enjoy travelling.", "They hate travelling.", "They don't mind travelling."], fr="Ils aiment voyager."),
    ]),
  },
  [M("gap", "✍️", "Le verbe en -ing", "swimming, dancing, getting up…", ["gap"]),
   M("tr", "❤️", "J'aime, je déteste…", "love, like, don't mind, hate : quel sens ?", ["tr"], 5),
   M("choice", "🔎", "Quelle phrase est correcte ?", "like + verbe-ing.", ["choice"], 6),
   M("order", "🧩", "Remets dans l'ordre", "Construis la phrase. Attention au piège !", ["order"], 6),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["gap", "tr", "choice", "order"], 12)])

# ═════════════ RELATIFS ═════════════
newpage("relatifs.html", "Les pronoms relatifs – Entraînement", 'who, <span>which</span>, where',
  "Les pronoms relatifs", ("#67e8f9", "#06b6d4"),
  '''      <p>Les <span class="hl">pronoms relatifs</span> relient deux phrases et donnent une précision sur un nom.</p>
      <table>
        <tr><th>Pronom</th><th>Pour…</th><th>Exemple</th></tr>
        <tr><td><span class="hl">who</span></td><td>une <b>personne</b></td><td>The girl who lives next door is my friend.</td></tr>
        <tr><td><span class="hl">which</span></td><td>une <b>chose</b>, un <b>animal</b></td><td>The book which is on the table is mine.</td></tr>
        <tr><td><span class="hl">that</span></td><td>une personne <b>ou</b> une chose</td><td>The film that we saw was great.</td></tr>
        <tr><td><span class="hl">where</span></td><td>un <b>lieu</b></td><td>This is the house where I was born.</td></tr>
        <tr><td><span class="hl">whose</span></td><td>la <b>possession</b> (dont le…)</td><td>The boy whose bike was stolen is sad.</td></tr>
        <tr><td><span class="hl">whom</span></td><td>une personne <b>complément</b> (soutenu)</td><td>The man whom I met was French. · to whom</td></tr>
      </table>
      <h4>Avec ou sans virgules ?</h4>
      <p><b>Relative déterminative</b> (sans virgule) : indispensable pour savoir de qui / quoi on parle. <i>that</i> est possible. <span class="ex">The students who work hard will pass.</span></p>
      <p><b>Relative explicative</b> (entre virgules) : information en plus. <b>Jamais that</b>. <span class="ex">My brother, who lives in London, is a doctor.</span></p>
      <h4>Omission du relatif</h4>
      <p>Quand le relatif est <b>complément</b> (suivi d'un sujet), on peut l'omettre : <span class="ex">The film (that) I saw was great. · The girl (who) you met is my cousin.</span> Impossible quand il est sujet : <span class="ex">The girl who lives next door… <s>The girl lives next door…</s></span></p>''',
  {
    "choice": ("choice", "Choisis le pronom relatif", [
      C("The girl ____ lives next door is my friend.", ["who", "which", "where"], tip="the girl = une personne → who."),
      C("The book ____ is on the table is mine.", ["which", "who", "where"], tip="the book = une chose → which."),
      C("This is the house ____ I was born.", ["where", "which", "who"], tip="un lieu → where."),
      C("I have a dog ____ loves bones.", ["which", "who", "where"], tip="un animal → which."),
      C("The man ____ is talking is my teacher.", ["who", "which", "whose"], tip="une personne → who."),
      C("Paris is the city ____ I live.", ["where", "which", "who"], tip="un lieu → where."),
      C("The boy ____ bike was stolen is sad.", ["whose", "who", "which"], tip="possession (dont le vélo) → whose."),
      C("The phone ____ I bought is great.", ["which", "who", "where"], tip="une chose → which (ou that)."),
      C("She's the singer ____ won the prize.", ["who", "which", "where"], tip="une personne → who."),
      C("That's the restaurant ____ we had dinner.", ["where", "which", "who"], tip="un lieu → where."),
      C("I know a woman ____ speaks five languages.", ["who", "which", "whose"], tip="une personne → who."),
      C("The cake ____ you made is delicious.", ["which", "who", "where"], tip="une chose → which."),
    ]),
    "adv": ("choice", "Relatives : niveau avancé", [
      C(None, ["My sister, who lives in Paris, is a nurse.", "My sister, that lives in Paris, is a nurse.", "My sister who, lives in Paris, is a nurse."], tip="relative explicative (entre virgules) → jamais that."),
      C(None, ["The book I bought is boring.", "The book bought is boring I.", "The book I bought it is boring."], tip="relatif complément → on peut l'omettre (the book (that) I bought)."),
      C(None, ["The woman who called you is my aunt.", "The woman called you is my aunt.", "The woman whom called you is my aunt."], tip="relatif sujet → on ne peut pas l'omettre, et pas de whom."),
      C(None, ["The man to whom I spoke was very kind.", "The man to who I spoke was very kind.", "The man to that I spoke was very kind."], tip="après une préposition (soutenu) → whom."),
      C(None, ["Paris, which is the capital of France, is beautiful.", "Paris, that is the capital of France, is beautiful.", "Paris which, is the capital of France, is beautiful."], tip="explicative → which, pas that."),
      C(None, ["The students who work hard will pass.", "The students, who work hard, will pass all.", "The students that, work hard will pass."], tip="déterminative (seulement ceux qui travaillent) → pas de virgules."),
    ]),
    "order": ("order", "Remets les mots dans l'ordre", [
      O("The girl|who|lives|next door|is nice.", fr="La fille qui habite à côté est gentille.", trap="which"),
      O("This is|the town|where|I|was born.", fr="C'est la ville où je suis né.", trap="which"),
      O("The film|which|we|saw|was great.", fr="Le film que nous avons vu était génial.", trap="who", alts=["The film that we saw was great."]),
      O("I have|a friend|who|plays|the piano.", fr="J'ai un ami qui joue du piano.", trap="where"),
    ]),
  },
  [M("choice", "🎯", "who, which, where ou whose ?", "Personne, chose, lieu ou possession ?", ["choice"], 12),
   M("order", "🧩", "Remets dans l'ordre", "Construis la phrase. Attention au piège !", ["order"], 4),
   M("adv", "🎓", "Virgules, omission, whom", "Relatives déterminatives et explicatives.", ["adv"], 6),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["choice", "order", "adv"], 12)])

# ═════════════ CONDITIONNEL ═════════════
N1 = "Type 1 · If + présent, will"
N2 = "Type 2 · If + prétérit, would"
N3 = "Type 3 · If + had + PP, would have + PP"
newpage("conditionnel.html", "Le conditionnel – Entraînement", 'If… <span>will / would</span>',
  "Les phrases avec if : types 1, 2 et 3", ("#fdba74", "#f97316"),
  '''      <h4>Type 1 : une situation possible / probable</h4>
      <div class="formula"><span class="hl">If</span> + présent simple, <span class="hl">will</span> + BV</div>
      <p class="ex">If it rains, I will stay at home. · If you study, you will pass.</p>
      <p>Jamais de will après if : <span class="ex">If it <s>will rain</s> rains…</span></p>
      <h4>Type 2 : une situation imaginaire</h4>
      <div class="formula"><span class="hl">If</span> + prétérit, <span class="hl">would</span> + BV</div>
      <p class="ex">If I had a million euros, I would buy a house. · If I were you, I would rest.</p>
      <p>Avec be, on dit souvent <b>were</b> à toutes les personnes : <span class="ex">If I were rich…</span></p>
      <h4>Type 3 : une situation passée qui n'a pas eu lieu (regret)</h4>
      <div class="formula"><span class="hl">If</span> + had + participe passé, <span class="hl">would have</span> + participe passé</div>
      <p class="ex">If I had known, I would have come. (Si j'avais su, je serais venu.) · If she had studied, she would have passed.</p>
      <p>La proposition avec if peut aussi venir en second : <span class="ex">I will stay at home if it rains.</span></p>''',
  {
    "t1": ("gap", "Type 1 : conjugue le verbe", [
      G("If it ____ , I will stay at home.", "rains", "rain", tip="après if : présent simple."), G("If you study, you ____ .", ["will pass", "'ll pass"], "pass", tip="will + BV."),
      G("If she ____ late, she will miss the bus.", "is", "be", tip="après if : présent (is)."), G("We will go to the beach if it ____ sunny.", "is", "be", tip="après if : présent."),
      G("If you eat too much, you ____ ill.", ["will be", "'ll be"], "be", tip="will + BV."), G("If he ____ , he will win.", "trains", "train", tip="après if : présent (+ -s)."),
      G("If I see Tom, I ____ him.", ["will tell", "'ll tell"], "tell", tip="will + BV."), G("If they don't hurry, they ____ the train.", ["will miss", "'ll miss", "won't catch"], "miss", tip="will + BV."),
    ]),
    "t2": ("gap", "Type 2 : conjugue le verbe", [
      G("If I ____ a million euros, I would buy a house.", "had", "have", tip="après if : prétérit."), G("If I were rich, I ____ the world.", ["would travel", "'d travel"], "travel", tip="would + BV."),
      G("If she ____ here, she would help us.", ["were", "was"], "be", tip="be → were (ou was)."), G("If I were you, I ____ to bed.", ["would go", "'d go"], "go", tip="would + BV."),
      G("If we ____ a car, we would go to the sea.", "had", "have", tip="après if : prétérit."), G("He would be happy if he ____ the match.", "won", "win", tip="après if : prétérit (win → won)."),
      G("If I could fly, I ____ to the moon.", ["would go", "'d go"], "go", tip="would + BV."), G("If they ____ more, they would pass.", "studied", "study", tip="après if : prétérit."),
    ]),
    "t3": ("gap", "Type 3 : conjugue le verbe", [
      G("If I ____ , I would have come.", "had known", "know", tip="après if : had + participe passé."),
      G("If she had studied, she ____ .", ["would have passed", "'d have passed"], "pass", tip="would have + participe passé.", w=240),
      G("If we ____ earlier, we wouldn't have missed the train.", "had left", "leave", tip="had + participe passé."),
      G("If you had asked me, I ____ you.", ["would have helped", "'d have helped"], "help", tip="would have + participe passé.", w=240),
      G("If it ____ , we would have gone to the beach.", ["hadn't rained", "had not rained"], "not / rain", tip="had not + participe passé."),
      G("He ____ the match if he had trained more.", ["would have won", "'d have won"], "win", tip="would have + participe passé (won).", w=240),
    ]),
    "ch3": ("choice", "Choisis la bonne forme (type 3)", [
      C("If I ____ the answer, I would have told you.", ["had known", "knew", "would have known"], tip="après if : had + PP."),
      C("If they had run, they ____ the bus.", ["would have caught", "would catch", "had caught"], tip="would have + PP."),
      C("She would have come if you ____ her.", ["had invited", "invited", "would have invited"], tip="après if : had + PP."),
      C("If I had seen you, I ____ hello.", ["would have said", "would say", "had said"], tip="would have + PP."),
    ]),
    "ch1": ("choice", "Choisis la bonne forme (type 1)", [
      C("If it ____ tomorrow, we'll stay inside.", ["rains", "will rain", "rained"], tip="après if : présent, jamais will."),
      C("If you call me, I ____ .", ["'ll answer", "answer", "answered"], tip="résultat : will + BV."),
      C("If he ____ hard, he'll succeed.", ["works", "will work", "worked"], tip="après if : présent."),
      C("You'll be tired if you ____ to bed late.", ["go", "will go", "went"], tip="après if : présent."),
    ]),
    "ch2": ("choice", "Choisis la bonne forme (type 2)", [
      C("If I ____ a dog, I would walk it every day.", ["had", "have", "would have"], tip="après if : prétérit."),
      C("If I won the lottery, I ____ a big house.", ["would buy", "will buy", "bought"], tip="résultat : would + BV."),
      C("If I ____ you, I would apologise.", ["were", "am", "would be"], tip="If I were you…"),
      C("She ____ happier if she lived by the sea.", ["would be", "will be", "is"], tip="would + BV."),
    ]),
  },
  [M("t1", "✍️", "Conjugue (type 1)", "If + présent, will + BV.", ["t1"], 8, N1),
   M("ch1", "🔎", "Choisis la bonne forme", "Jamais de will après if !", ["ch1"], 4, N1),
   M("t2", "✍️", "Conjugue (type 2)", "If + prétérit, would + BV.", ["t2"], 8, N2),
   M("ch2", "🔎", "Choisis la bonne forme", "had, were, would…", ["ch2"], 4, N2),
   M("t3", "✍️", "Conjugue (type 3)", "If + had + PP, would have + PP.", ["t3"], 6, N3),
   M("ch3", "🔎", "Choisis la bonne forme", "had known, would have come…", ["ch3"], 4, N3),
   M("mix", "🎲", "Tout mélangé", "Types 1, 2 et 3 : le grand test !", ["t1", "t2", "t3", "ch1", "ch2", "ch3"], 12, "Les trois types")])

# ═════════════ PASSIF ═════════════
newpage("passif.html", "Le passif – Entraînement", 'Le <span>passif</span>',
  "be + participe passé · by …", ("#a5b4fc", "#6366f1"),
  '''      <p>Au <span class="hl">passif</span>, le sujet <b>subit</b> l'action. On l'utilise quand l'auteur de l'action est inconnu ou moins important.</p>
      <div class="formula">sujet + <span class="hl">be</span> (au bon temps) + <span class="hl">participe passé</span> (+ <span class="hl">by</span> + auteur)</div>
      <table>
        <tr><th>Temps</th><th>Actif</th><th>Passif</th></tr>
        <tr><td>présent</td><td>They make cars here.</td><td>Cars <b>are made</b> here.</td></tr>
        <tr><td>prétérit</td><td>Shakespeare wrote Hamlet.</td><td>Hamlet <b>was written</b> by Shakespeare.</td></tr>
      </table>
      <p>Participes passés : réguliers en -ed (cleaned, built…) · irréguliers : made, written, built, sold, eaten, stolen, taken, given…</p>
      <h4>Pour aller plus loin</h4>
      <p><b>Passif avec un modal</b> : modal + <span class="hl">be</span> + PP → <span class="ex">This must be done today. · It can't be repaired.</span></p>
      <p><b>Passif au present perfect / be + -ing</b> : <span class="ex">The room has been cleaned. · The road is being repaired.</span></p>
      <p><b>get</b> + PP (familier) : <span class="ex">He got arrested. · I got paid.</span></p>
      <p><b>It is said that… / He is said to…</b> : <span class="ex">It is said that he is rich. = He is said to be rich.</span></p>''',
  {
    "gap": ("gap", "Mets la phrase au passif", [
      G("English ____ all over the world.", "is spoken", "speak · présent", tip="présent : is + participe (spoken)."),
      G("Hamlet ____ by Shakespeare.", "was written", "write · prétérit", tip="prétérit : was + participe (written)."),
      G("These cars ____ in Germany.", "are made", "make · présent", tip="pluriel, présent : are + made."),
      G("My bike ____ yesterday!", "was stolen", "steal · prétérit", tip="prétérit : was + stolen."),
      G("The Eiffel Tower ____ in 1889.", "was built", "build · prétérit", tip="was + built."),
      G("The windows ____ every week.", "are cleaned", "clean · présent", tip="are + cleaned."),
      G("The letters ____ this morning.", "were sent", "send · prétérit", tip="pluriel, prétérit : were + sent."),
      G("Bread ____ in this shop.", "is sold", "sell · présent", tip="is + sold."),
      G("The thieves ____ by the police.", "were arrested", "arrest · prétérit", tip="were + arrested."),
      G("This song ____ by millions of people.", "is loved", "love · présent", tip="is + loved."),
    ]),
    "choice": ("choice", "Actif ou passif : choisis la bonne forme", [
      C("The cake ____ by my grandmother.", ["was made", "made", "was make"], tip="passif : was + participe passé."),
      C("My grandmother ____ the cake.", ["made", "was made", "is made"], tip="la grand-mère fait l'action → actif."),
      C("The museum ____ every day by thousands of tourists.", ["is visited", "visits", "is visit"], tip="passif présent : is + visited."),
      C("Rice ____ in Asia.", ["is grown", "grows by", "is grow"], tip="passif : is + grown."),
      C("The window ____ by a ball.", ["was broken", "broke", "was broke"], tip="passif : was + broken."),
      C("Thousands of tourists ____ the museum.", ["visit", "are visited", "is visited"], tip="les touristes font l'action → actif."),
    ]),
    "adv": ("choice", "Le passif : niveau avancé", [
      C("This work must ____ today.", ["be done", "done", "been done"], tip="modal + be + PP."), C("The road ____ at the moment.", ["is being repaired", "is repairing", "is been repaired"], tip="be + -ing au passif → is being + PP."),
      C("The room ____ . You can go in.", ["has been cleaned", "has cleaned", "is been cleaned"], tip="present perfect passif → has been + PP."), C("He ____ for speeding yesterday.", ["got arrested", "got arrest", "was arresting"], tip="get + PP (familier)."),
      C("He is said ____ very rich.", ["to be", "being", "be"], tip="He is said to be…"), C("It ____ that the castle is haunted.", ["is said", "says", "is saying"], tip="It is said that…"),
    ]),
    "pp": ("choice", "Choisis le participe passé", [
      C(None, ["made", "maked", "make"], big="make"), C(None, ["written", "wrote", "writed"], big="write"), C(None, ["built", "builded", "build"], big="build"),
      C(None, ["sold", "selled", "sell"], big="sell"), C(None, ["stolen", "stole", "stealed"], big="steal"), C(None, ["spoken", "spoke", "speaked"], big="speak"),
      C(None, ["taken", "took", "taked"], big="take"), C(None, ["given", "gave", "gived"], big="give"),
    ]),
  },
  [M("pp", "📚", "Les participes passés", "made, written, built…", ["pp"], 8),
   M("gap", "✍️", "Mets au passif", "be + participe passé.", ["gap"]),
   M("choice", "⚖️", "Actif ou passif ?", "Qui fait l'action ?", ["choice"], 6),
   M("adv", "🎓", "Passif avancé", "must be done, is being repaired, he is said to…", ["adv"], 6),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["pp", "gap", "choice", "adv"], 12)])

# ═════════════ DISCOURS INDIRECT ═════════════
newpage("discours_indirect.html", "Le discours indirect – Entraînement", 'Le discours <span>indirect</span>',
  "He said (that)… · She told me (that)…", ("#d8b4fe", "#a855f7"),
  '''      <p>Le <span class="hl">discours indirect</span> sert à rapporter les paroles de quelqu'un.</p>
      <p class="ex">Direct : Tom says, "I am tired." → Indirect : Tom says (that) he is tired.</p>
      <p><b>say</b> ou <b>tell</b> ? <span class="ex">He said (that)… · He told <b>me</b> (that)…</span> → tell est suivi de la personne à qui on parle.</p>
      <h4>Après said / told, on recule d'un temps</h4>
      <table>
        <tr><th>Direct</th><th>Indirect</th></tr>
        <tr><td>présent : "I <b>am</b> tired."</td><td>prétérit : He said he <b>was</b> tired.</td></tr>
        <tr><td>"I <b>like</b> pizza."</td><td>She said she <b>liked</b> pizza.</td></tr>
        <tr><td>will : "I <b>will</b> come."</td><td>would : He said he <b>would</b> come.</td></tr>
        <tr><td>can : "I <b>can</b> swim."</td><td>could : She said she <b>could</b> swim.</td></tr>
      </table>
      <p>Les pronoms changent aussi : <span class="ex">"I love <b>my</b> job." → She said she loved <b>her</b> job.</span></p>
      <h4>Rapporter une question</h4>
      <p>Question fermée → <span class="hl">asked if</span> + ordre affirmatif : <span class="ex">"Are you tired?" → He asked me if I was tired.</span></p>
      <p>Question ouverte → <span class="hl">asked</span> + mot interrogatif + ordre affirmatif : <span class="ex">"Where do you live?" → She asked me where I lived.</span></p>
      <h4>Rapporter un ordre ou une demande</h4>
      <p><span class="hl">told / asked</span> + personne + <span class="hl">(not) to</span> + BV : <span class="ex">"Sit down!" → The teacher told us to sit down. · "Don't shout!" → She asked me not to shout.</span></p>
      <p>Les repères de temps changent aussi : today → that day · tomorrow → the next day · yesterday → the day before.</p>''',
  {
    "saytell": ("choice", "say ou tell ?", [
      C("He ____ me that he was tired.", ["told", "said"], tip="+ personne (me) → told."), C("She ____ that she liked pizza.", ["said", "told"], tip="pas de personne → said."),
      C("They ____ us the truth.", ["told", "said"], tip="+ personne (us) → told."), C("Tom ____ he would come.", ["said", "told"], tip="pas de personne → said."),
      C("Can you ____ me the time?", ["tell", "say"], tip="+ personne → tell."), C("What did she ____ ?", ["say", "tell"], tip="pas de personne → say."),
    ]),
    "shift": ("choice", "Rapporte la phrase", [
      C(None, ["He said he was tired.", "He said he is tired.", "He said I was tired."], fr='Tom : "I am tired."', tip="am → was ; I → he."),
      C(None, ["She said she liked pizza.", "She said she likes pizza.", "She said I liked pizza."], fr='Emma : "I like pizza."', tip="like → liked."),
      C(None, ["He said he would come.", "He said he will come.", "He said he came."], fr='Lucas : "I will come."', tip="will → would."),
      C(None, ["She said she could swim.", "She said she can swim.", "She said she swims."], fr='Léa : "I can swim."', tip="can → could."),
      C(None, ["They said they were hungry.", "They said they are hungry.", "They said we were hungry."], fr='Les enfants : "We are hungry."', tip="are → were ; we → they."),
      C(None, ["She said she loved her job.", "She said I loved my job.", "She said she loves my job."], fr='Ma mère : "I love my job."', tip="love → loved ; I → she ; my → her."),
      C(None, ["He told me he didn't like football.", "He told me he doesn't like football.", "He said me he didn't like football."], fr='Tom (à moi) : "I don\'t like football."', tip="don't → didn't ; told me (pas said me)."),
      C(None, ["She said she had a dog.", "She said she has a dog.", "She said she haved a dog."], fr='Emma : "I have a dog."', tip="have → had."),
    ]),
    "qo": ("choice", "Rapporte la question ou l'ordre", [
      C(None, ["He asked me if I was tired.", "He asked me was I tired.", "He asked me if was I tired."], fr='Tom : "Are you tired?"', tip="question fermée → asked if + ordre affirmatif."),
      C(None, ["She asked me where I lived.", "She asked me where did I live.", "She asked me where do I live."], fr='Emma : "Where do you live?"', tip="pas de do / did : ordre affirmatif."),
      C(None, ["The teacher told us to sit down.", "The teacher told us sit down.", "The teacher said us to sit down."], fr='Le professeur : "Sit down!"', tip="told + personne + to + BV."),
      C(None, ["She asked me not to shout.", "She asked me to not shouting.", "She asked me don't shout."], fr="Léa : \"Don't shout!\"", tip="ordre négatif → not to + BV."),
      C(None, ["He asked what time the film started.", "He asked what time did the film start.", "He asked what time the film does start."], fr='Lucas : "What time does the film start?"', tip="ordre affirmatif + recul du temps."),
      C(None, ["They asked if they could come.", "They asked can they come.", "They asked if could they come."], fr='Les enfants : "Can we come?"', tip="can → could, ordre affirmatif."),
    ]),
    "gap": ("gap", "Complète la phrase au discours indirect", [
      G("He said he ____ tired.", "was", "\"I am tired.\"", tip="am → was."), G("She said she ____ chocolate.", "liked", "\"I like chocolate.\"", tip="like → liked."),
      G("They said they ____ come.", "would", "\"We will come.\"", tip="will → would."), G("He said he ____ play the guitar.", "could", "\"I can play the guitar.\"", tip="can → could."),
      G("She said she ____ in Paris.", "lived", "\"I live in Paris.\"", tip="live → lived."), G("Tom said he ____ a new bike.", "had", "\"I have a new bike.\"", tip="have → had."),
    ]),
  },
  [M("saytell", "🗣️", "say ou tell ?", "told me / said that…", ["saytell"], 6),
   M("shift", "🔁", "Rapporte la phrase", "On recule d'un temps et on change les pronoms.", ["shift"], 8),
   M("gap", "✍️", "Complète", "was, liked, would, could…", ["gap"], 6),
   M("qo", "❓", "Questions et ordres", "asked if…, told me to…", ["qo"], 6),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["saytell", "shift", "gap", "qo"], 12)])

# ═════════════ CAP VENTE ═════════════
newpage("cap_vente.html", "Anglais de la vente – CAP Sapver", "L'anglais de la <span>vente</span>",
  "Accueillir, conseiller, encaisser, téléphoner", ("#5eead4", "#14b8a6"),
  '''      <h4>Accueillir le client</h4>
      <p class="ex">Good morning! / Hello! · Can I help you? / May I help you? · Are you looking for something?</p>
      <h4>Conseiller</h4>
      <p class="ex">What size are you? · What colour would you like? · Would you like to try it on? · The fitting rooms are over there. · It suits you!</p>
      <h4>Encaisser</h4>
      <p class="ex">That's £25, please. · How would you like to pay? — By card / In cash. · Here's your receipt. · Would you like a bag?</p>
      <h4>Au téléphone</h4>
      <p class="ex">Hello, [nom du magasin], how can I help you? · Can I take a message? · Hold on, please. · Could you repeat, please?</p>
      <p>Pour être <b>poli</b> : <span class="hl">Would you like…?</span> (voulez-vous…?) · <span class="hl">Could you…?</span> (pourriez-vous…?) · <span class="hl">May I…?</span> (puis-je…?) · please · thank you.</p>''',
  {
    "reply": ("choice", "Choisis la bonne réplique du vendeur", [
      C(None, ["Can I help you?", "What do you want?", "Go away, please."], fr="Une cliente entre dans le magasin et regarde les rayons.", tip="Formule polie d'accueil : Can I help you?"),
      C(None, ["What size are you?", "How old are you?", "What is your name?"], fr="Le client cherche un jean mais ne sait pas quelle taille prendre.", tip="la taille → What size are you?"),
      C(None, ["Would you like to try it on?", "Do you want to buy it now?", "You must buy it."], fr="La cliente hésite devant une robe.", tip="essayer → try on."),
      C(None, ["The fitting rooms are over there.", "The toilets are closed.", "The shop is open."], fr="Le client demande : « Where can I try it on? »", tip="cabines d'essayage = fitting rooms."),
      C(None, ["How would you like to pay?", "How much money have you got?", "Do you have a job?"], fr="À la caisse, vous voulez savoir comment le client va payer.", tip="moyen de paiement → How would you like to pay?"),
      C(None, ["Here's your receipt.", "Here's your recipe.", "Here's your bill of exchange."], fr="Vous donnez le ticket de caisse au client.", tip="ticket de caisse = receipt."),
      C(None, ["Would you like a bag?", "Do you want a bag or not?", "Take a bag."], fr="Vous proposez un sac au client.", tip="proposer poliment → Would you like…?"),
      C(None, ["Can I take a message?", "Call later.", "I don't know."], fr="Au téléphone, la personne demandée est absente.", tip="prendre un message → Can I take a message?"),
      C(None, ["Could you repeat, please?", "What?", "Speak better!"], fr="Au téléphone, vous n'avez pas compris.", tip="poli → Could you repeat, please?"),
      C(None, ["It suits you!", "It's too expensive for you.", "It's ugly."], fr="La veste va très bien au client.", tip="ça vous va bien → It suits you!"),
    ]),
    "price": ("choice", "Comment dit-on ce prix ?", [
      C(None, ["twenty-five pounds", "twenty-five pound", "pounds twenty-five"], big="£25"), C(None, ["nine euros ninety-nine", "nine ninety-nine euros", "euros nine ninety-nine"], big="9,99 €"),
      C(None, ["forty dollars", "fourty dollars", "fourteen dollars"], big="$40"), C(None, ["fifteen pounds fifty", "fifty pounds fifteen", "fifteen fifty pounds"], big="£15.50"),
      C(None, ["a hundred and twenty euros", "a hundred twenty euro", "one hundred and twenty euro"], big="120 €"),
    ]),
    "vocab": ("choice", "Quel est le mot anglais ?", [
      C(None, ["receipt", "recipe", "ticket"], big="ticket de caisse"), C(None, ["fitting room", "fitness room", "trying room"], big="cabine d'essayage"),
      C(None, ["sale", "sold", "promotion price"], big="soldes"), C(None, ["cash", "money card", "change card"], big="espèces"),
      C(None, ["change", "rest", "money back"], big="monnaie (à rendre)"), C(None, ["customer", "costumer", "client man"], big="client"),
      C(None, ["shop assistant", "shop helper", "seller man"], big="vendeur / vendeuse"), C(None, ["discount", "reduction price", "less"], big="réduction"),
      C(None, ["size", "height", "measure"], big="taille (vêtement)"), C(None, ["cash desk", "money table", "pay desk"], big="caisse"),
    ]),
    "order": ("order", "Remets la question polie dans l'ordre", [
      O("Can|I|help|you?", fr="Puis-je vous aider ?"), O("Would|you|like|to try it on?", fr="Voulez-vous l'essayer ?"),
      O("How|would|you|like|to pay?", fr="Comment souhaitez-vous payer ?"), O("What|size|are|you?", fr="Quelle taille faites-vous ?"),
      O("Could|you|repeat,|please?", fr="Pourriez-vous répéter, s'il vous plaît ?"), O("Would|you|like|a bag?", fr="Voulez-vous un sac ?"),
    ]),
  },
  [M("reply", "🛍️", "La bonne réplique", "Accueillir, conseiller, encaisser, téléphoner.", ["reply"]),
   M("vocab", "📖", "Le vocabulaire", "receipt, fitting room, customer…", ["vocab"]),
   M("price", "💶", "Annoncer un prix", "£25, 9,99 €, $40…", ["price"], 5),
   M("order", "🧩", "Les questions polies", "Remets les mots dans l'ordre.", ["order"], 6),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["reply", "vocab", "price", "order"], 12)],
  tag="Anglais · CAP Sapver")
print("content3 ok", REGISTRY)
