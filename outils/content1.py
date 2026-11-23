import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
exec(open(_EA_OUT+"/content_helpers.py", encoding="utf-8").read())

# ═════════════ PRÉSENT SIMPLE ═════════════
S3 = "he / she / it → verbe + <b>-s</b>."
newpage("present_simple.html", "Présent simple – Entraînement", 'Le présent <span>simple</span>',
  "Habitudes et vérités générales · he / she / it + -s", ("#38bdf8", "#0284c7"),
  '''      <p>Le <span class="hl">présent simple</span> sert à parler des <b>habitudes</b>, des goûts et des vérités générales. Mots repères : <i>every day, usually, often, on Mondays…</i></p>
      <table>
        <tr><th></th><th>I / you / we / they</th><th>he / she / it</th></tr>
        <tr><td><b>+</b></td><td>I work</td><td>she work<span class="hl">s</span></td></tr>
        <tr><td><b>−</b></td><td>I <span class="hl">don't</span> work</td><td>she <span class="hl">doesn't</span> work</td></tr>
        <tr><td><b>?</b></td><td><span class="hl">Do</span> you work?</td><td><span class="hl">Does</span> she work?</td></tr>
      </table>
      <p><b>Orthographe du -s :</b> watch → watch<b>es</b>, go → go<b>es</b>, finish → finish<b>es</b> (après -ch, -sh, -s, -x, -o) · study → stud<b>ies</b> (consonne + y) · have → <b>has</b>.</p>
      <p>Après <b>don't / doesn't / do / does</b> : base verbale, sans -s. <span class="ex">She doesn't like fish. <s>She doesn't likes.</s></span></p>''',
  {
    "aff": ("gap", "Conjugue le verbe au présent simple", [
      G("She ____ in a shop.", "works", "work", tip=S3), G("They ____ in Lyon.", "live", "live", tip="they → base verbale, sans -s."),
      G("My brother ____ TV every evening.", "watches", "watch", tip="watch se termine par -ch → <b>-es</b>."),
      G("Tom ____ to school by bus.", "goes", "go", tip="go → <b>goes</b> (-o → -es)."),
      G("Emma ____ English at university.", "studies", "study", tip="consonne + y → <b>-ies</b>."),
      G("My dad ____ his work at 6.", "finishes", "finish", tip="-sh → <b>-es</b>."),
      G("We ____ football on Saturdays.", "play", "play", tip="we → base verbale."),
      G("He ____ a big dog.", "has", "have", tip="have → <b>has</b> à la 3e personne."),
      G("The shop ____ at 9 o'clock.", "opens", "open", tip=S3),
      G("I ____ my homework after dinner.", "do", "do", tip="I → base verbale."),
      G("She ____ her homework in the evening.", "does", "do", tip="do → <b>does</b>."),
      G("My cat ____ all day.", "sleeps", "sleep", tip=S3),
      G("Lucas ____ to play the guitar.", "tries", "try", tip="consonne + y → <b>-ies</b>."),
      G("My parents ____ coffee every morning.", "drink", "drink", tip="my parents = they → base verbale."),
    ]),
    "spell": ("choice", "Choisis la bonne orthographe (he / she / it)", [
      C(None, ["watches", "watchs", "watchies"], big="watch", tip="-ch → -es."), C(None, ["goes", "gos", "goies"], big="go", tip="-o → -es."),
      C(None, ["studies", "studys", "studyes"], big="study", tip="consonne + y → -ies."), C(None, ["plays", "plaies", "playes"], big="play", tip="voyelle + y → simplement -s."),
      C(None, ["has", "haves", "have"], big="have", tip="have → has."), C(None, ["fixes", "fixs", "fixies"], big="fix", tip="-x → -es."),
      C(None, ["washes", "washs", "washies"], big="wash", tip="-sh → -es."), C(None, ["flies", "flys", "flyes"], big="fly", tip="consonne + y → -ies."),
      C(None, ["does", "dos", "dose"], big="do", tip="do → does."), C(None, ["reads", "reades", "readies"], big="read", tip="cas général : -s."),
      C(None, ["misses", "miss", "missies"], big="miss", tip="-ss → -es."), C(None, ["buys", "buies", "buyes"], big="buy", tip="voyelle + y → -s."),
    ]),
    "neginter": ("choice", "Choisis la bonne forme", [
      C("He ____ like fish.", ["doesn't", "don't", "isn't"], tip="he → doesn't + base verbale."),
      C("I ____ eat meat.", ["don't", "doesn't", "am not"], tip="I → don't + base verbale."),
      C("____ your sister speak English?", ["Does", "Do", "Is"], tip="your sister = she → Does."),
      C("____ you live near here?", ["Do", "Does", "Are"], tip="you → Do."),
      C("She doesn't ____ football.", ["play", "plays", "playing"], tip="après doesn't → base verbale."),
      C("Does he ____ a car?", ["have", "has", "haves"], tip="après Does → base verbale : have."),
      C("My parents ____ work on Sundays.", ["don't", "doesn't", "aren't"], tip="my parents = they → don't."),
      C("____ the shop open on Monday?", ["Does", "Do", "Is it"], tip="the shop = it → Does."),
      C("We ____ go to school on Wednesday afternoon.", ["don't", "doesn't", "not"], tip="we → don't."),
      C("Where ____ Tom live?", ["does", "do", "is"], tip="Tom = he → does."),
      C("What time ____ you get up?", ["do", "does", "are"], tip="you → do."),
      C("Emma ____ like spiders.", ["doesn't", "don't", "isn't"], tip="Emma = she → doesn't."),
    ]),
    "order": ("order", "Remets les mots dans l'ordre", [
      O("She|works|in a bakery.", fr="Elle travaille dans une boulangerie.", trap="work"),
      O("He|doesn't|like|vegetables.", fr="Il n'aime pas les légumes.", trap="likes"),
      O("Do|you|play|the piano?", fr="Est-ce que tu joues du piano ?", trap="Does"),
      O("Does|your brother|speak|Spanish?", fr="Est-ce que ton frère parle espagnol ?", trap="speaks"),
      O("We|don't|go|to school|on Sundays.", fr="Nous n'allons pas à l'école le dimanche.", trap="doesn't"),
      O("My mum|watches|TV|every evening.", fr="Ma mère regarde la télé tous les soirs.", trap="watchs"),
      O("Where|does|Tom|live?", fr="Où habite Tom ?", trap="lives"),
      O("They|have|lunch|at noon.", fr="Ils déjeunent à midi.", trap="has"),
      O("My sister|studies|English.", fr="Ma sœur étudie l'anglais.", trap="studys"),
      O("I|don't|drink|coffee.", fr="Je ne bois pas de café.", trap="doesn't"),
    ]),
  },
  [M("aff", "✍️", "Conjugue", "he / she / it + -s : works, goes, studies…", ["aff"]),
   M("spell", "🔤", "L'orthographe du -s", "-s, -es ou -ies ? Choisis la bonne forme.", ["spell"]),
   M("neginter", "❓", "Négatif et interrogatif", "don't / doesn't, Do / Does + base verbale.", ["neginter"]),
   M("order", "🧩", "Remets dans l'ordre", "Construis la phrase. Attention au piège !", ["order"], 8),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["aff", "neginter", "order"], 12)])

# ═════════════ PRÉSENT EN BE + ING ═════════════
newpage("present_continu.html", "Présent en be + -ing – Entraînement", 'Le présent <span>be + -ing</span>',
  "Ce qui se passe en ce moment · am / is / are + verbe-ing", ("#22d3ee", "#0891b2"),
  '''      <p>Le <span class="hl">présent en be + -ing</span> sert à parler d'une action <b>en cours</b>, en ce moment. Mots repères : <i>now, at the moment, right now, Look!, Listen!</i></p>
      <div class="formula">sujet + <span class="hl">am / is / are</span> + verbe<span class="hl">-ing</span></div>
      <table>
        <tr><th>+</th><th>−</th><th>?</th></tr>
        <tr><td>I am reading.<br>She is reading.<br>They are reading.</td><td>I'm not reading.<br>She isn't reading.<br>They aren't reading.</td><td>Am I reading?<br>Is she reading?<br>Are they reading?</td></tr>
      </table>
      <p><b>Orthographe :</b> write → writ<b>ing</b> (on enlève le -e) · run → ru<b>nning</b>, swim → swi<b>mming</b> (consonne doublée) · lie → l<b>ying</b>.</p>
      <h4>Présent simple ou be + -ing ?</h4>
      <p>Habitude → présent simple : <span class="ex">I go to school every day.</span><br>En ce moment → be + -ing : <span class="ex">I am going to school now.</span></p>''',
  {
    "form": ("gap", "Mets le verbe au présent en be + -ing", [
      G("I ____ a book now.", "am reading", "read", tip="I → am + verbe-ing."),
      G("Look! It ____ .", "is raining", "rain", tip="it → is + verbe-ing."),
      G("They ____ football in the park.", "are playing", "play", tip="they → are + verbe-ing."),
      G("Be quiet! The baby ____ .", "is sleeping", "sleep", tip="the baby = he/she → is."),
      G("She ____ a letter at the moment.", "is writing", "write", tip="write → writing (on enlève le -e)."),
      G("We ____ in the sea right now.", "are swimming", "swim", tip="swim → swimming (consonne doublée)."),
      G("Listen! Someone ____ .", "is singing", "sing", tip="someone → is."),
      G("My parents ____ dinner.", "are cooking", "cook", tip="my parents = they → are."),
      G("Tom ____ to the bus stop.", "is running", "run", tip="run → running (consonne doublée)."),
      G("I ____ TV now.", ["am not watching"], "not / watch", tip="négatif : am not + verbe-ing.", w=220),
      G("The children ____ a cake.", "are making", "make", tip="make → making."),
      G("She ____ on the phone now.", "is talking", "talk", tip="she → is + verbe-ing."),
    ]),
    "vs": ("choice", "Présent simple ou be + -ing ?", [
      C("Look! It ____ .", ["is snowing", "snows"], tip="Look! → en ce moment : be + -ing."),
      C("I ____ to school every day.", ["go", "am going"], tip="every day → habitude : présent simple."),
      C("She ____ TV at the moment.", ["is watching", "watches"], tip="at the moment → be + -ing."),
      C("My dad usually ____ at 7.", ["gets up", "is getting up"], tip="usually → habitude : présent simple."),
      C("Listen! The baby ____ .", ["is crying", "cries"], tip="Listen! → en ce moment."),
      C("We ____ football on Saturdays.", ["play", "are playing"], tip="on Saturdays → habitude."),
      C("Be quiet, I ____ !", ["am working", "work"], tip="en ce moment."),
      C("Cats ____ milk.", ["like", "are liking"], tip="vérité générale → présent simple."),
      C("Where are you? — I ____ in the garden.", ["am sitting", "sit"], tip="en ce moment."),
      C("He never ____ coffee.", ["drinks", "is drinking"], tip="never → habitude."),
      C("Right now, they ____ lunch.", ["are having", "have"], tip="right now → be + -ing."),
      C("She often ____ to music.", ["listens", "is listening"], tip="often → habitude."),
    ]),
    "spell": ("choice", "Choisis la bonne orthographe", [
      C(None, ["writing", "writeing", "writting"], big="write", tip="-e muet : on l'enlève."), C(None, ["running", "runing", "runeing"], big="run", tip="consonne doublée."),
      C(None, ["swimming", "swiming", "swimeing"], big="swim", tip="consonne doublée."), C(None, ["making", "makeing", "makking"], big="make", tip="-e muet : on l'enlève."),
      C(None, ["playing", "plaing", "playying"], big="play", tip="cas général : + ing."), C(None, ["sitting", "siting", "siteing"], big="sit", tip="consonne doublée."),
      C(None, ["dancing", "danceing", "dancking"], big="dance", tip="-e muet : on l'enlève."), C(None, ["lying", "lieing", "liing"], big="lie", tip="-ie → -ying."),
      C(None, ["reading", "readding", "readeing"], big="read", tip="deux voyelles avant la consonne : pas de doublement."), C(None, ["getting", "geting", "geeting"], big="get", tip="consonne doublée."),
    ]),
    "order": ("order", "Remets les mots dans l'ordre", [
      O("She|is|reading|a book.", fr="Elle lit un livre (en ce moment).", trap="reads"),
      O("They|aren't|watching|TV.", fr="Ils ne regardent pas la télé.", trap="don't"),
      O("Are|you|listening|to me?", fr="Tu m'écoutes ?", trap="Do"),
      O("Is|it|raining|now?", fr="Est-ce qu'il pleut maintenant ?", trap="Does"),
      O("I|am|cooking|dinner.", fr="Je prépare le dîner.", trap="cook"),
      O("What|are|you|doing?", fr="Qu'est-ce que tu fais ?", trap="do"),
      O("He|isn't|working|today.", fr="Il ne travaille pas aujourd'hui.", trap="doesn't"),
      O("We|are|waiting|for the bus.", fr="Nous attendons le bus.", trap="is"),
    ]),
  },
  [M("form", "✍️", "Forme be + -ing", "am / is / are + verbe-ing.", ["form"]),
   M("spell", "🔤", "L'orthographe du -ing", "writing, running, lying…", ["spell"]),
   M("vs", "⚖️", "Simple ou be + -ing ?", "Habitude ou action en cours ?", ["vs"]),
   M("order", "🧩", "Remets dans l'ordre", "Construis la phrase. Attention au piège !", ["order"], 8),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["form", "vs", "order"], 12)])

# ═════════════ PRÉTÉRIT EN BE + ING ═════════════
newpage("preterit_continu.html", "Prétérit en be + -ing – Entraînement", 'Le prétérit <span>be + -ing</span>',
  "Ce qui était en train de se passer · was / were + verbe-ing", ("#facc15", "#ca8a04"),
  '''      <p>Le <span class="hl">prétérit en be + -ing</span> décrit une action <b>en cours</b> à un moment du passé (« j'étais en train de… »).</p>
      <div class="formula">sujet + <span class="hl">was / were</span> + verbe<span class="hl">-ing</span><br>I / he / she / it → <b>was</b> · you / we / they → <b>were</b></div>
      <p class="ex">At 8 o'clock, I was having dinner. · They were playing in the garden.</p>
      <p><b>−</b> wasn't / weren't + verbe-ing · <b>?</b> Was he…? / Were they…?</p>
      <h4>Avec when et while</h4>
      <p>L'action longue (en cours) → be + -ing ; l'action courte qui l'interrompt → prétérit simple.</p>
      <p class="ex">I was watching TV <b>when</b> the phone rang. · <b>While</b> she was cooking, the cat jumped on the table.</p>''',
  {
    "form": ("gap", "Mets le verbe au prétérit en be + -ing", [
      G("At 8 o'clock, I ____ dinner.", "was having", "have", tip="I → was + verbe-ing."),
      G("They ____ in the garden when it started to rain.", "were playing", "play", tip="they → were."),
      G("She ____ a book when I arrived.", "was reading", "read", tip="she → was."),
      G("We ____ TV at 9 pm yesterday.", "were watching", "watch", tip="we → were."),
      G("____ at 10 o'clock?", ["What were you doing"], "what / you / do", tip="question : What + were + sujet + verbe-ing ?", w=260),
      G("It ____ when we left school.", "was raining", "rain", tip="it → was."),
      G("My parents ____ when I called.", "were sleeping", "sleep", tip="my parents = they → were."),
      G("He ____ to music, so he didn't hear me.", "was listening", "listen", tip="he → was."),
      G("I ____ attention.", "wasn't paying", "not / pay", tip="négatif : wasn't + verbe-ing."),
      G("You ____ very fast!", "were driving", "drive", tip="you → were ; drive → driving."),
    ]),
    "waswere": ("choice", "was ou were ?", [
      C("I ____ walking to school.", ["was", "were"], keep=True, tip="I → was."), C("They ____ eating pizza.", ["were", "was"], tip="they → were."),
      C("She ____ talking on the phone.", ["was", "were"], keep=True, tip="she → was."), C("We ____ running in the park.", ["were", "was"], tip="we → were."),
      C("My brother ____ playing video games.", ["was", "were"], keep=True, tip="my brother = he → was."), C("You ____ singing in the shower!", ["were", "was"], tip="you → were."),
      C("The dog ____ barking all night.", ["was", "were"], keep=True, tip="the dog = it → was."), C("Tom and Léa ____ dancing.", ["were", "was"], tip="Tom and Léa = they → were."),
    ]),
    "when": ("choice", "Prétérit simple ou be + -ing ?", [
      C("I was watching TV when the phone ____ .", ["rang", "was ringing"], tip="action courte qui interrompt → prétérit simple."),
      C("While she ____ , the cat jumped on the table.", ["was cooking", "cooked"], tip="action longue en cours → be + -ing."),
      C("We ____ dinner when the lights went out.", ["were having", "had"], tip="action longue en cours → be + -ing."),
      C("He fell while he ____ .", ["was skiing", "skied"], tip="while + action longue → be + -ing."),
      C("When I arrived, they ____ .", ["were dancing", "danced"], tip="action en cours au moment où j'arrive."),
      C("It was raining when we ____ the house.", ["left", "were leaving"], tip="action courte → prétérit simple."),
      C("I ____ my keys while I was running.", ["lost", "was losing"], tip="action courte → prétérit simple."),
      C("What were you doing when I ____ you?", ["called", "was calling"], tip="action courte → prétérit simple."),
    ]),
    "order": ("order", "Remets les mots dans l'ordre", [
      O("I|was|sleeping|when you called.", fr="Je dormais quand tu as appelé.", trap="were"),
      O("They|were|playing|football.", fr="Ils jouaient au football.", trap="was"),
      O("Were|you|listening?", fr="Est-ce que tu écoutais ?", trap="Did"),
      O("She|wasn't|working|yesterday.", fr="Elle ne travaillait pas hier.", trap="didn't"),
      O("What|was|he|doing?", fr="Qu'est-ce qu'il faisait ?", trap="did"),
      O("It|was|snowing|this morning.", fr="Il neigeait ce matin.", trap="were"),
    ]),
  },
  [M("form", "✍️", "Forme was / were + -ing", "Conjugue le verbe au prétérit en be + -ing.", ["form"]),
   M("waswere", "⚖️", "was ou were ?", "Choisis le bon auxiliaire.", ["waswere"], 8),
   M("when", "⚡", "Simple ou be + -ing ?", "when / while : action longue ou action courte ?", ["when"], 8),
   M("order", "🧩", "Remets dans l'ordre", "Construis la phrase. Attention au piège !", ["order"], 6),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["form", "waswere", "when", "order"], 12)])

# ═════════════ FUTUR ═════════════
newpage("futur.html", "Le futur – Entraînement", 'Le <span>futur</span>',
  "will + BV · be going to + BV", ("#a78bfa", "#7c3aed"),
  '''      <h4>will + base verbale</h4>
      <p>Pour une <b>prédiction</b> (je pense que…), une <b>décision prise sur le moment</b>, une promesse.</p>
      <div class="formula">sujet + <span class="hl">will</span> ('ll) + BV · négatif : <span class="hl">won't</span> + BV · question : <span class="hl">Will</span> + sujet + BV ?</div>
      <p class="ex">I think it will rain tomorrow. · The phone is ringing! — I'll answer it. · She won't come.</p>
      <h4>be going to + base verbale</h4>
      <p>Pour un <b>projet déjà décidé</b>, ou une prédiction avec une <b>preuve</b> visible.</p>
      <div class="formula">sujet + <span class="hl">am / is / are going to</span> + BV</div>
      <p class="ex">I'm going to visit London next summer. · Look at those clouds! It's going to rain.</p>
      <p>Will est le même pour toutes les personnes : <span class="ex">he will <s>wills</s></span>. Après will, pas de « to ».</p>
      <h4>Pour aller plus loin</h4>
      <p><span class="hl">will be + -ing</span> (futur continu) : action en cours à un moment du futur. <span class="ex">This time tomorrow, I will be flying to New York.</span></p>
      <p><span class="hl">will have + participe passé</span> (futur antérieur) : action terminée avant un moment du futur. <span class="ex">By 6 pm, I will have finished my homework.</span></p>''',
  {
    "will": ("gap", "Complète avec will ou won't + base verbale", [
      G("I think it ____ tomorrow.", ["will rain", "'ll rain"], "rain", tip="prédiction → will + BV."),
      G("Don't worry, I ____ you.", ["will help", "'ll help"], "help", tip="promesse → will + BV."),
      G("She ____ to the party. She's ill.", "won't come", "not / come", tip="négatif : won't + BV."),
      G("____ me tomorrow?", ["Will you call"], "you / call", tip="question : Will + sujet + BV ?", w=200),
      G("In 2050, cars ____ .", "will fly", "fly", tip="prédiction → will."),
      G("He ____ 15 next week.", "will be", "be", tip="will + be."),
      G("I'm cold. — I ____ the window.", ["will close", "'ll close"], "close", tip="décision sur le moment → will."),
      G("They ____ the match. They're too weak.", "won't win", "not / win", tip="négatif : won't + BV."),
    ]),
    "goingto": ("gap", "Complète avec be going to + base verbale", [
      G("I ____ London next summer.", ["am going to visit", "'m going to visit"], "visit", tip="projet → am going to + BV.", w=260),
      G("She ____ a new phone.", ["is going to buy", "'s going to buy"], "buy", tip="she → is going to + BV.", w=260),
      G("Look at those clouds! It ____ .", ["is going to rain", "'s going to rain"], "rain", tip="preuve visible → going to.", w=260),
      G("We ____ a party on Saturday.", ["are going to have", "'re going to have"], "have", tip="we → are going to.", w=260),
      G("They ____ by train.", ["are going to travel", "'re going to travel"], "travel", tip="they → are going to.", w=260),
      G("He ____ football tonight.", ["isn't going to play", "is not going to play"], "not / play", tip="négatif : isn't going to + BV.", w=260),
      G("____ your grandmother?", ["Are you going to visit"], "you / visit", tip="question : Are + sujet + going to + BV ?", w=300),
      G("I ____ my homework after dinner.", ["am going to do", "'m going to do"], "do", tip="projet → going to.", w=260),
    ]),
    "choice": ("choice", "will ou be going to ?", [
      C("The phone is ringing! — OK, I ____ it.", ["'ll answer", "'m going to answer"], tip="décision prise sur le moment → will."),
      C("We've got the tickets. We ____ the concert on Friday.", ["are going to see", "will see"], tip="projet déjà décidé → going to."),
      C("Look at that car! It ____ crash!", ["is going to", "will"], tip="preuve visible → going to."),
      C("I think robots ____ our homework one day.", ["will do", "are going to do"], tip="simple prédiction (je pense que…) → will."),
      C("I've decided: I ____ a doctor.", ["am going to be", "will be"], tip="décision déjà prise → going to."),
      C("I promise I ____ late.", ["won't be", "am not going to be"], tip="promesse → will."),
      C("Maybe it ____ sunny tomorrow.", ["will be", "is going to be"], tip="maybe + prédiction → will."),
      C("She's bought paint. She ____ her room.", ["is going to paint", "will paint"], tip="projet préparé → going to."),
    ]),
    "adv": ("choice", "Futur continu ou futur antérieur ?", [
      C("This time tomorrow, I ____ on the beach.", ["will be lying", "will have lain", "will lie"], tip="en cours à un moment du futur → will be + -ing."),
      C("By the end of the year, she ____ her diploma.", ["will have got", "will be getting", "gets"], tip="terminé avant un moment du futur (by…) → will have + PP."),
      C("At 8 pm, we ____ dinner. Don't call!", ["will be having", "will have had", "have"], tip="en cours à 20 h → will be + -ing."),
      C("By the time you arrive, I ____ the cake.", ["will have made", "will be making", "make"], tip="by the time → will have + PP."),
      C("Next week, they ____ in Spain.", ["will be travelling", "will have travelled", "travel"], tip="en cours pendant la semaine prochaine → will be + -ing."),
      C("By 2030, scientists ____ a cure.", ["will have found", "will be finding", "find"], tip="by 2030 → will have + PP."),
    ]),
    "error": ("choice", "Quelle phrase est correcte ?", [
      C(None, ["She will come.", "She wills come.", "She will comes."], tip="will ne change pas et il est suivi de la BV."),
      C(None, ["I will go to Paris.", "I will to go to Paris.", "I will going to Paris."], tip="après will : BV, pas de to."),
      C(None, ["He is going to play.", "He going to play.", "He is going play."], tip="be + going to + BV."),
      C(None, ["Will you help me?", "Do you will help me?", "You will help me?"], tip="question : Will + sujet + BV ?"),
      C(None, ["They won't come.", "They don't will come.", "They willn't come."], tip="négatif : won't."),
      C(None, ["Are you going to swim?", "Do you going to swim?", "Are you going swim?"], tip="question : Are + sujet + going to + BV ?"),
    ]),
  },
  [M("will", "🔮", "will", "Prédictions, promesses, décisions sur le moment.", ["will"], 8),
   M("goingto", "📅", "be going to", "Projets et prédictions avec une preuve.", ["goingto"], 8),
   M("choice", "⚖️", "will ou going to ?", "Choisis selon la situation.", ["choice"], 8),
   M("error", "🔎", "Quelle phrase est correcte ?", "Repère les erreurs de forme.", ["error"], 6),
   M("adv", "🔭", "will be -ing, will have done", "Futur continu et futur antérieur.", ["adv"], 6),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["will", "goingto", "choice", "error", "adv"], 12)])

# ═════════════ PRESENT PERFECT ═════════════
newpage("present_perfect.html", "Present perfect – Entraînement", 'Le <span>present perfect</span>',
  "have / has + participe passé · for / since · ever / never", ("#f472b6", "#db2777"),
  '''      <p>Le <span class="hl">present perfect</span> relie le passé au présent : une action qui <b>dure encore</b>, ou une <b>expérience</b> (déjà / jamais), sans date précise.</p>
      <div class="formula">sujet + <span class="hl">have / has</span> + participe passé<br>réguliers : -ED (played, lived) · irréguliers : 3e colonne (been, seen, eaten, gone, done…)</div>
      <p class="ex">I have lived here for ten years. · She has never been to London. · Have you ever eaten sushi?</p>
      <p><b>for</b> + durée (for two years, for a week) · <b>since</b> + point de départ (since 2020, since Monday)</p>
      <h4>Present perfect ou prétérit ?</h4>
      <p>Date ou moment précis et terminé (yesterday, last year, in 2019, ago) → <b>prétérit</b> : <span class="ex">I went to London last year.</span><br>Pas de date / jusqu'à maintenant → <b>present perfect</b> : <span class="ex">I have been to London.</span></p>''',
  {
    "form": ("gap", "Mets le verbe au present perfect", [
      G("I ____ here for ten years.", ["have lived", "'ve lived"], "live", tip="I → have + participe passé (lived)."),
      G("She ____ to London twice.", ["has been", "'s been"], "be", tip="she → has ; be → been."),
      G("We ____ this film three times.", ["have seen", "'ve seen"], "see", tip="see → seen (irrégulier)."),
      G("He ____ his homework.", ["has done", "'s done"], "do", tip="do → done."),
      G("They ____ sushi.", "have never eaten", "never / eat", tip="have + never + participe passé (eaten).", w=220),
      G("____ a horse?", ["Have you ever ridden"], "you / ever / ride", tip="question : Have + sujet + ever + participe (ridden).", w=260),
      G("My parents ____ married since 2005.", ["have been", "'ve been"], "be", tip="my parents → have been."),
      G("Tom ____ his phone.", ["has lost", "'s lost"], "lose", tip="lose → lost."),
      G("I ____ my keys yet.", ["haven't found", "have not found"], "not / find", tip="négatif : haven't + participe (found)."),
      G("She ____ English since September.", ["has studied", "'s studied"], "study", tip="study → studied."),
    ]),
    "forsince": ("choice", "for ou since ?", [
      C("I have lived here ____ 2015.", ["since", "for"], keep=True, tip="2015 = point de départ → since."),
      C("She has worked here ____ ten years.", ["for", "since"], tip="ten years = durée → for."),
      C("We have known him ____ Monday.", ["since", "for"], keep=True, tip="Monday = point de départ → since."),
      C("They have been married ____ a long time.", ["for", "since"], tip="a long time = durée → for."),
      C("I have had this bike ____ my birthday.", ["since", "for"], keep=True, tip="my birthday = point de départ → since."),
      C("He has been ill ____ three days.", ["for", "since"], tip="three days = durée → for."),
      C("I haven't seen her ____ last summer.", ["since", "for"], keep=True, tip="last summer = point de départ → since."),
      C("We have waited ____ two hours!", ["for", "since"], tip="two hours = durée → for."),
    ]),
    "vs": ("choice", "Present perfect ou prétérit ?", [
      C("I ____ to London last year.", ["went", "have been"], tip="last year = date passée → prétérit."),
      C("I ____ to London three times.", ["have been", "went"], tip="expérience, sans date → present perfect."),
      C("She ____ her keys yesterday.", ["lost", "has lost"], tip="yesterday → prétérit."),
      C("____ snails?", ["Have you ever eaten", "Did you ever eat"], tip="ever = expérience → present perfect."),
      C("We ____ here since 2010.", ["have lived", "lived"], tip="since → l'action dure encore : present perfect."),
      C("He ____ the match two days ago.", ["watched", "has watched"], tip="ago → prétérit."),
      C("I ____ this film. It's great!", ["have seen", "saw"], tip="pas de date, lien avec maintenant → present perfect."),
      C("In 2019, they ____ to Spain.", ["moved", "have moved"], tip="in 2019 → prétérit."),
    ]),
    "pp": ("choice", "Choisis le participe passé", [
      C(None, ["been", "be", "was"], big="be"), C(None, ["seen", "saw", "seed"], big="see"), C(None, ["eaten", "ate", "eated"], big="eat"),
      C(None, ["gone", "went", "goed"], big="go"), C(None, ["done", "did", "doed"], big="do"), C(None, ["written", "wrote", "writed"], big="write"),
      C(None, ["taken", "took", "taked"], big="take"), C(None, ["played", "plaid", "playen"], big="play", tip="verbe régulier : -ed."),
      C(None, ["bought", "buyed", "buyen"], big="buy"), C(None, ["had", "haved", "hadden"], big="have"),
    ]),
  },
  [M("form", "✍️", "Forme have / has + participe", "Conjugue au present perfect.", ["form"]),
   M("pp", "📚", "Les participes passés", "been, seen, eaten, gone…", ["pp"]),
   M("forsince", "⏳", "for ou since ?", "Durée ou point de départ ?", ["forsince"], 8),
   M("vs", "⚖️", "Present perfect ou prétérit ?", "Avec ou sans date précise ?", ["vs"], 8),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["form", "pp", "forsince", "vs"], 12)])

# ═════════════ IMPÉRATIF ═════════════
newpage("imperatif.html", "L'impératif – Entraînement", "L'<span>impératif</span>",
  "Donner un ordre ou un conseil · BV · Don't + BV · Let's + BV", ("#4ade80", "#16a34a"),
  '''      <p>L'<span class="hl">impératif</span> sert à donner un <b>ordre</b>, une <b>consigne</b> ou un <b>conseil</b>. Il n'y a pas de sujet.</p>
      <table>
        <tr><th></th><th>Structure</th><th>Exemple</th></tr>
        <tr><td><b>+</b></td><td>base verbale</td><td>Open the door! · Sit down, please.</td></tr>
        <tr><td><b>−</b></td><td><span class="hl">Don't</span> + base verbale</td><td>Don't run in the corridor!</td></tr>
        <tr><td>proposer</td><td><span class="hl">Let's</span> + base verbale</td><td>Let's go to the cinema!</td></tr>
      </table>
      <p>On ajoute <b>please</b> pour être poli. Pas de « you » : <span class="ex">Close the window. <s>You close the window.</s></span></p>''',
  {
    "gap": ("gap", "Complète à l'impératif", [
      G("____ the window, please.", "Open", "open", fr="Ouvre la fenêtre, s'il te plaît.", tip="affirmatif : base verbale."),
      G("____ in the corridor!", "Don't run", "not / run", fr="Ne cours pas dans le couloir !", tip="négatif : Don't + BV."),
      G("____ to the cinema!", "Let's go", "let's / go", fr="Allons au cinéma !", tip="proposer : Let's + BV."),
      G("____ down, please.", "Sit", "sit", fr="Asseyez-vous, s'il vous plaît.", tip="base verbale."),
      G("____ your phone in class!", "Don't use", "not / use", fr="N'utilise pas ton téléphone en classe !", tip="Don't + BV."),
      G("____ to me!", "Listen", "listen", fr="Écoute-moi !", tip="base verbale."),
      G("____ a pizza tonight!", "Let's make", "let's / make", fr="Faisons une pizza ce soir !", tip="Let's + BV."),
      G("____ late!", "Don't be", "not / be", fr="Ne sois pas en retard !", tip="Don't + be."),
      G("____ your hands before lunch.", "Wash", "wash", fr="Lave-toi les mains avant le déjeuner.", tip="base verbale."),
      G("____ the light, please.", "Turn off", "turn off", fr="Éteins la lumière, s'il te plaît.", tip="base verbale."),
    ]),
    "choice": ("choice", "Quelle phrase est correcte ?", [
      C(None, ["Don't touch!", "Not touch!", "You don't touch!"], fr="Ne touche pas !", tip="Don't + BV."),
      C(None, ["Close the door.", "You close the door.", "Closes the door."], fr="Ferme la porte.", tip="pas de sujet : BV."),
      C(None, ["Let's play!", "Let's playing!", "Let's to play!"], fr="Jouons !", tip="Let's + BV."),
      C(None, ["Don't shout!", "No shout!", "Don't shouting!"], fr="Ne crie pas !", tip="Don't + BV."),
      C(None, ["Be careful!", "Are careful!", "Being careful!"], fr="Fais attention !", tip="be à l'impératif : Be."),
      C(None, ["Help me, please!", "Helps me, please!", "You help me, please!"], fr="Aide-moi, s'il te plaît !", tip="base verbale."),
      C(None, ["Let's not go.", "Don't let's going.", "Let's don't go."], fr="N'y allons pas.", tip="négatif de Let's : Let's not + BV."),
      C(None, ["Don't forget your bag!", "Not forget your bag!", "Don't forgets your bag!"], fr="N'oublie pas ton sac !", tip="Don't + BV."),
    ]),
    "order": ("order", "Remets les mots dans l'ordre", [
      O("Please|close|the door.", fr="Ferme la porte, s'il te plaît."), O("Don't|eat|in class!", fr="Ne mange pas en classe !", trap="Not"),
      O("Let's|go|to the park!", fr="Allons au parc !", trap="going"), O("Don't|be|late!", fr="Ne sois pas en retard !", trap="are"),
      O("Take|your coat!", fr="Prends ton manteau !", trap="You"), O("Let's|watch|a film!", fr="Regardons un film !", trap="watching"),
    ]),
  },
  [M("gap", "✍️", "Complète à l'impératif", "BV, Don't + BV ou Let's + BV.", ["gap"]),
   M("choice", "🔎", "Quelle phrase est correcte ?", "Repère les erreurs.", ["choice"], 8),
   M("order", "🧩", "Remets dans l'ordre", "Construis la consigne.", ["order"], 6),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["gap", "choice", "order"], 12)])
print("content1 ok", REGISTRY)
