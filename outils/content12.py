import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
exec(open(_EA_OUT+"/content_helpers.py", encoding="utf-8").read())
SX = "Anglais · Expert · Syntaxe"

# ═════════════ INVERSION ═════════════
INV = "Après un adverbe <b>négatif ou restrictif</b> placé en tête (Never, Rarely, Seldom, Not only, Hardly, No sooner, Only then, Little…), on <b>inverse</b> l'auxiliaire et le sujet, comme dans une question."
newpage("inversion.html", "L'inversion emphatique – Expert", '<span>Never</span> have I seen…',
  "L'inversion après un adverbe négatif ou restrictif", ("#fca5a5", "#b91c1c"),
  '''      <p>Dans un registre <b>soutenu</b> (écrit, discours), on peut placer en tête de phrase un adverbe <span class="hl">négatif ou restrictif</span> pour insister. Le sujet et l'auxiliaire sont alors <b>inversés</b>.</p>
      <table>
        <tr><th>Phrase neutre</th><th>Inversion emphatique</th></tr>
        <tr><td>I have never seen such a mess.</td><td><b>Never have I</b> seen such a mess.</td></tr>
        <tr><td>He rarely goes out.</td><td><b>Rarely does he</b> go out.</td></tr>
        <tr><td>She not only sings, but she also dances.</td><td><b>Not only does she</b> sing, but she also dances.</td></tr>
        <tr><td>I had hardly arrived when it started to rain.</td><td><b>Hardly had I</b> arrived when it started to rain.</td></tr>
        <tr><td>He had no sooner left than she called.</td><td><b>No sooner had he</b> left than she called.</td></tr>
        <tr><td>I little knew what would happen.</td><td><b>Little did I</b> know what would happen.</td></tr>
        <tr><td>I understood only then.</td><td><b>Only then did I</b> understand.</td></tr>
      </table>
      <p>Sans auxiliaire dans la phrase de départ, on ajoute <b>do / does / did</b>. On trouve aussi l'inversion dans des conditionnelles soutenues : <span class="ex">Had I known… (= If I had known) · Were I you… · Should you need help…</span></p>''',
  {"choice": ("choice", "Choisis la phrase correcte", [
      C(None, ["Never have I seen such a beautiful place.", "Never I have seen such a beautiful place.", "Never I saw such a beautiful place."], tip=INV),
      C(None, ["Rarely does he go out on weekdays.", "Rarely he goes out on weekdays.", "Rarely goes he out on weekdays."], tip=INV + " Ici : does + he + BV."),
      C(None, ["Not only did she win, but she also broke the record.", "Not only she won, but she also broke the record.", "Not only won she, but she also broke the record."], tip=INV),
      C(None, ["Hardly had we sat down when the phone rang.", "Hardly we had sat down when the phone rang.", "Hardly did we had sat down when the phone rang."], tip=INV),
      C(None, ["No sooner had he left than it started to snow.", "No sooner he had left than it started to snow.", "No sooner had he left when it started to snow."], tip="No sooner… <b>than</b> (et non when)."),
      C(None, ["Little did they know what was waiting for them.", "Little they knew what was waiting for them.", "Little knew they what was waiting for them."], tip=INV),
      C(None, ["Only then did I realise my mistake.", "Only then I realised my mistake.", "Only then realised I my mistake."], tip=INV),
      C(None, ["Seldom have I heard such nonsense.", "Seldom I have heard such nonsense.", "Seldom heard I such nonsense."], tip=INV),
    ]),
    "cond": ("choice", "Conditionnelle avec inversion : choisis l'équivalent", [
      C(None, ["If I had known", "If I knew", "If I would know"], fr="Had I known, I would have come.", tip="Had I known = If I had known (type 3)."),
      C(None, ["If I were you", "If I was you would", "If you were me"], fr="Were I you, I would accept.", tip="Were I you = If I were you."),
      C(None, ["If you need help", "If you should not need help", "You must need help"], fr="Should you need help, call me.", tip="Should you need… = If you (should) need…"),
      C(None, ["If they had arrived earlier", "If they arrive earlier", "If they would arrive earlier"], fr="Had they arrived earlier, they would have met her.", tip="Had they arrived = If they had arrived."),
  ])},
  [M("choice", "🔄", "L'inversion emphatique", "Never have I…, Rarely does he…", ["choice"], 8),
   M("cond", "🎩", "Conditionnelles inversées", "Had I known…, Were I you…, Should you…", ["cond"], 4),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["choice", "cond"], 12)], tag=SX)

# ═════════════ CONDITIONNELS MIXTES ═════════════
newpage("conditionnels_mixtes.html", "Les conditionnels mixtes – Expert", 'Conditionnels <span>mixtes</span>',
  "Croiser le passé et le présent dans une hypothèse", ("#fdba74", "#c2410c"),
  '''      <p>Un <span class="hl">conditionnel mixte</span> combine deux époques différentes dans la condition et dans la conséquence.</p>
      <table>
        <tr><th>Type</th><th>Structure</th><th>Exemple</th></tr>
        <tr><td>Passé → présent</td><td>If + <b>past perfect</b>, would + BV</td><td>If I had studied medicine, I <b>would be</b> a doctor now.</td></tr>
        <tr><td>Présent → passé</td><td>If + <b>prétérit</b>, would have + PP</td><td>If I <b>were</b> braver, I <b>would have spoken</b> to her yesterday.</td></tr>
      </table>
      <p>Rappel : type 2 = If + prétérit, would + BV · type 3 = If + past perfect, would have + PP. Les mixtes croisent ces deux structures.</p>
      <p>Repère les marqueurs de temps : <i>now, today</i> (présent) · <i>yesterday, last year</i> (passé).</p>''',
  {"choice": ("choice", "Choisis la bonne forme", [
      C("If I had taken that job, I ____ rich now.", ["would be", "would have been", "will be"], tip="condition passée → conséquence présente (now) : would + BV."),
      C("If she ____ more careful, she wouldn't have had the accident.", ["were", "had been", "is"], tip="trait permanent (présent) → conséquence passée : prétérit + would have."),
      C("If we hadn't missed the plane, we ____ in Rome today.", ["would be", "would have been", "were"], tip="passé → présent (today) : would + BV."),
      C("If he ____ French, he would have understood the film.", ["spoke", "had spoken", "speaks"], tip="il ne parle pas français (présent) → conséquence passée."),
      C("If I had gone to bed earlier, I ____ so tired now.", ["wouldn't be", "wouldn't have been", "won't be"], tip="passé → présent (now)."),
      C("If I ____ afraid of flying, I would have visited you last year.", ["weren't", "hadn't been", "am not"], tip="peur permanente (présent) → conséquence passée."),
      C("If you had listened to me, we ____ lost now.", ["wouldn't be", "wouldn't have been", "aren't"], tip="passé → présent."),
      C("If they ____ so lazy, they would have finished the project on time.", ["weren't", "hadn't been", "aren't"], tip="trait permanent → conséquence passée."),
  ])},
  [M("choice", "🔀", "Conditionnels mixtes", "Passé → présent, présent → passé.", ["choice"], 8)], tag="Anglais · Expert · Grammaire")

# ═════════════ SUBJONCTIF ═════════════
newpage("subjonctif.html", "Le subjonctif anglais – Expert", 'Le <span>subjonctif</span> anglais',
  "I suggest that he be… · It's time we left · If I were…", ("#ddd6fe", "#7c3aed"),
  '''      <h4>Subjonctif « mandatif » (registre soutenu)</h4>
      <p>Après les verbes et expressions de <b>demande, d'obligation, de recommandation</b> (suggest, recommend, insist, demand, require, it is essential / vital / important that…), le verbe est en <span class="hl">base verbale</span> à toutes les personnes, sans -s, sans do.</p>
      <p class="ex">I suggest that he <b>be</b> on time. · It is essential that she <b>attend</b> the meeting. · They insisted that he <b>not leave</b>.</p>
      <p>En anglais britannique courant, on utilise aussi <b>should</b> + BV : <span class="ex">I suggest that he should be on time.</span></p>
      <h4>Le subjonctif passé (« were »)</h4>
      <p class="ex">If I <b>were</b> you… · I wish she <b>were</b> here. · He talks as if he <b>were</b> the boss.</p>
      <h4>It's (high) time + prétérit</h4>
      <p class="ex">It's time we <b>left</b>. (il est temps que nous partions) · It's high time you <b>found</b> a job.</p>
      <h4>Expressions figées</h4>
      <p class="ex">God save the King · Long live the Queen · Be that as it may · Come what may</p>''',
  {"choice": ("choice", "Choisis la bonne forme", [
      C("I suggest that he ____ on time.", ["be", "is", "will be"], tip="suggest that + BV (subjonctif)."),
      C("It is essential that every student ____ the exam.", ["take", "takes", "took"], tip="it is essential that + BV, sans -s."),
      C("The doctor recommended that she ____ more.", ["rest", "rests", "rested"], tip="recommend that + BV."),
      C("They insisted that he ____ the room.", ["not leave", "doesn't leave", "didn't leave"], tip="négatif du subjonctif : not + BV."),
      C("If I ____ you, I would apologise.", ["were", "am", "be"], tip="subjonctif passé : were."),
      C("It's time we ____ home.", ["went", "go", "will go"], tip="It's time + prétérit."),
      C("He behaves as if he ____ the boss.", ["were", "is", "be"], tip="as if + were."),
      C("The law requires that all drivers ____ insured.", ["be", "are", "were"], tip="require that + BV."),
      C("It's high time you ____ a job.", ["found", "find", "will find"], tip="It's high time + prétérit."),
      C("I wish he ____ here now.", ["were", "is", "be"], tip="wish + were."),
  ])},
  [M("choice", "📜", "Le subjonctif", "suggest that he be, it's time we left, if I were…", ["choice"])], tag="Anglais · Expert · Grammaire")

# ═════════════ PHRASES CLIVÉES ═════════════
newpage("phrases_clivees.html", "Les phrases clivées et l'emphase – Expert", '<span>What</span> I need is…',
  "Mettre en relief : It is… that, What…, do emphatique", ("#a5f3fc", "#0e7490"),
  '''      <p>Pour <b>mettre en relief</b> une partie de la phrase, on peut la « cliver » (la couper en deux).</p>
      <table>
        <tr><th>Structure</th><th>Phrase neutre</th><th>Phrase clivée</th></tr>
        <tr><td><span class="hl">It is / was … that / who</span></td><td>Tom broke the window.</td><td><b>It was Tom who</b> broke the window.</td></tr>
        <tr><td><span class="hl">What … is / was</span> (pseudo-clivée)</td><td>I need a holiday.</td><td><b>What I need is</b> a holiday.</td></tr>
        <tr><td><span class="hl">All … is</span></td><td>I only want some peace.</td><td><b>All I want is</b> some peace.</td></tr>
        <tr><td><span class="hl">The reason why … is that</span></td><td>I'm late because of the traffic.</td><td><b>The reason why</b> I'm late <b>is that</b> there was traffic.</td></tr>
      </table>
      <h4>Le do emphatique</h4>
      <p>Pour insister sur la vérité d'une affirmation : <span class="hl">do / does / did</span> + BV, accentué à l'oral.</p>
      <p class="ex">I <b>do</b> like your dress! (si, vraiment) · She <b>did</b> call you, I promise. · <b>Do</b> sit down.</p>''',
  {"choice": ("choice", "Choisis la phrase qui met en relief l'élément demandé", [
      C(None, ["It was Tom who broke the window.", "Tom it was who broke the window.", "It was Tom which broke the window."], fr="Mettre en relief « Tom » : Tom broke the window.", tip="It was + personne + who…"),
      C(None, ["What I need is a holiday.", "That I need is a holiday.", "What I need it is a holiday."], fr="Mettre en relief « a holiday » : I need a holiday.", tip="What + sujet + verbe + is…"),
      C(None, ["It was in Paris that they met.", "It was in Paris where they met it.", "In Paris it was that they met."], fr="Mettre en relief « in Paris » : They met in Paris.", tip="It was + complément + that…"),
      C(None, ["All I want is some peace and quiet.", "All what I want is some peace and quiet.", "All I want it is some peace and quiet."], fr="Mettre en relief « some peace and quiet ».", tip="All + sujet + verbe + is… (pas de what)."),
      C(None, ["I do like your new haircut!", "I like do your new haircut!", "I am liking your new haircut!"], fr="Insister : « J'aime vraiment ta nouvelle coupe ! »", tip="do emphatique + BV."),
      C(None, ["She did send the email, I saw her.", "She did sent the email, I saw her.", "She sent did the email, I saw her."], fr="Insister : « Elle a bien envoyé le mail. »", tip="did + BV (send)."),
      C(None, ["The reason why I left is that I was tired.", "The reason why I left is because of I was tired.", "The reason I left it is that I was tired."], fr="Mettre en relief la raison du départ.", tip="The reason why… is that…"),
      C(None, ["It's the price that worries me.", "It's the price who worries me.", "What worries me it's the price."], fr="Mettre en relief « the price » : The price worries me.", tip="chose → that (pas who)."),
  ])},
  [M("choice", "🔦", "Mettre en relief", "It is… that, What… is, do emphatique.", ["choice"], 8)], tag=SX)

# ═════════════ PROPOSITIONS PARTICIPIALES ═════════════
newpage("participiales.html", "Les propositions participiales – Expert", '<span>Having finished</span>, he left',
  "Propositions participiales en -ing, having + PP et participe passé", ("#bbf7d0", "#15803d"),
  '''      <p>Une <span class="hl">proposition participiale</span> remplace une subordonnée (when, because, after, which…) pour alléger la phrase, surtout à l'écrit.</p>
      <table>
        <tr><th>Forme</th><th>Sens</th><th>Exemple</th></tr>
        <tr><td>verbe-<b>ing</b></td><td>action simultanée ou cause (sens actif)</td><td><b>Walking</b> down the street, I met Tom. (= While I was walking…)</td></tr>
        <tr><td><b>having</b> + PP</td><td>action antérieure</td><td><b>Having finished</b> his work, he went home. (= After he had finished…)</td></tr>
        <tr><td><b>participe passé</b></td><td>sens passif</td><td><b>Built</b> in 1889, the tower is very famous. (= which was built…)</td></tr>
      </table>
      <p><b>Attention au « participe flottant »</b> (dangling participle) : le sujet sous-entendu de la participiale doit être le <b>même</b> que celui de la principale.</p>
      <p class="ex"><s>Walking down the street, the rain started.</s> (la pluie ne marchait pas !) → Walking down the street, <b>I</b> felt the rain start.</p>''',
  {"choice": ("choice", "Choisis la bonne forme", [
      C("____ his homework, he went out with his friends.", ["Having finished", "Finished", "Being finished"], tip="action antérieure → having + PP."),
      C("____ in 1889, the Eiffel Tower attracts millions of tourists.", ["Built", "Building", "Having built"], tip="sens passif (la tour a été construite) → participe passé."),
      C("____ down the street, I saw an old friend.", ["Walking", "Walked", "Having walked down"], tip="action simultanée, sens actif → -ing."),
      C("____ tired, she went to bed early.", ["Feeling", "Felt", "Having been felt"], tip="cause, sens actif → -ing."),
      C("____ by the noise, the baby started to cry.", ["Frightened", "Frightening", "Having frightened"], tip="sens passif (le bébé est effrayé) → participe passé."),
      C("____ the letter, she burst into tears.", ["Having read", "Read", "Being reading"], tip="action antérieure → having + PP."),
    ]),
    "dangling": ("choice", "Quelle phrase est correcte (sans participe flottant) ?", [
      C(None, ["Walking home, I was caught in the rain.", "Walking home, the rain caught me.", "Walking home, it started to rain on me."], tip="Le sujet de walking doit être le sujet de la principale : I."),
      C(None, ["Having finished dinner, we watched a film.", "Having finished dinner, the film started.", "Having finished dinner, a film was watched."], tip="Ce sont « nous » qui avons fini le dîner → we."),
      C(None, ["Looking out of the window, I saw a fox.", "Looking out of the window, a fox appeared.", "Looking out of the window, there was a fox."], tip="C'est « je » qui regarde → I saw."),
      C(None, ["Tired after the match, the players went straight to bed.", "Tired after the match, the beds were ready.", "Tired after the match, bed was the only option."], tip="Ce sont les joueurs qui sont fatigués."),
  ])},
  [M("choice", "✒️", "-ing, having + PP ou PP ?", "Simultanéité, antériorité ou passif.", ["choice"], 6),
   M("dangling", "⚠️", "Le participe flottant", "Repère la phrase logique.", ["dangling"], 4),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["choice", "dangling"], 10)], tag=SX)

# ═════════════ REMEMBER TO / REMEMBER -ING ═════════════
newpage("remember_to_ing.html", "remember to / remember -ing – Expert", 'remember <span>to</span> / remember <span>-ing</span>',
  "Les verbes dont le sens change avec to ou -ing", ("#fde68a", "#b45309"),
  '''      <p>Certains verbes acceptent <b>to + BV</b> et <b>-ing</b>, mais avec un <span class="hl">sens différent</span>.</p>
      <table>
        <tr><th>Verbe</th><th>+ to + BV</th><th>+ -ing</th></tr>
        <tr><td>remember</td><td>penser à (faire) : <i>Remember to lock the door.</i></td><td>se souvenir d'avoir fait : <i>I remember locking the door.</i></td></tr>
        <tr><td>forget</td><td>oublier de faire : <i>I forgot to call her.</i></td><td>oublier avoir fait : <i>I'll never forget meeting him.</i></td></tr>
        <tr><td>stop</td><td>s'arrêter pour : <i>He stopped to smoke.</i></td><td>arrêter de : <i>He stopped smoking.</i></td></tr>
        <tr><td>try</td><td>essayer de (effort) : <i>Try to open the window.</i></td><td>essayer (pour voir) : <i>Try opening the window.</i></td></tr>
        <tr><td>regret</td><td>regretter de devoir (annonce) : <i>We regret to inform you…</i></td><td>regretter d'avoir fait : <i>I regret saying that.</i></td></tr>
        <tr><td>go on</td><td>passer à autre chose : <i>He went on to become a doctor.</i></td><td>continuer : <i>She went on talking.</i></td></tr>
        <tr><td>mean</td><td>avoir l'intention : <i>I meant to tell you.</i></td><td>impliquer : <i>This job means working at night.</i></td></tr>
      </table>
      <p>Règle générale : <b>to</b> regarde vers l'<b>avenir</b> (l'action est à faire), <b>-ing</b> vers ce qui est <b>déjà fait</b> ou en cours.</p>''',
  {"choice": ("choice", "to + BV ou -ing ?", [
      C("Don't forget ____ the door when you leave.", ["to lock", "locking"], tip="action à faire → to."),
      C("I clearly remember ____ the door. I'm sure it's closed.", ["locking", "to lock"], tip="souvenir d'une action passée → -ing."),
      C("He stopped ____ . He hasn't had a cigarette for a year.", ["smoking", "to smoke"], tip="arrêter de → -ing."),
      C("On the way home, we stopped ____ some bread.", ["to buy", "buying"], tip="s'arrêter pour → to."),
      C("I regret ____ him. I should have kept quiet.", ["telling", "to tell"], tip="regretter d'avoir fait → -ing."),
      C("We regret ____ you that the flight is cancelled.", ["to inform", "informing"], tip="annonce officielle → regret to."),
      C("The computer won't start. Try ____ it off and on again.", ["turning", "to turn"], tip="essayer pour voir → -ing."),
      C("I tried ____ the box, but it was too heavy.", ["to lift", "lifting"], tip="effort (sans succès) → to."),
      C("After university, she went on ____ a famous lawyer.", ["to become", "becoming"], tip="étape suivante → to."),
      C("I meant ____ you, but I forgot.", ["to call", "calling"], tip="avoir l'intention → to."),
      C("Being a nurse means ____ at night.", ["working", "to work"], tip="impliquer → -ing."),
      C("I'll never forget ____ the Pacific for the first time.", ["seeing", "to see"], tip="souvenir → -ing."),
  ])},
  [M("choice", "🧠", "Le sens change !", "remember, stop, try, regret, mean…", ["choice"], 12)], tag="Anglais · Expert · Grammaire")

# ═════════════ CONNECTED SPEECH ═════════════
newpage("connected_speech.html", "Connected speech – Expert", '<span>Connected</span> speech',
  "Liaisons, élisions et formes réduites de l'anglais oral", ("#e9d5ff", "#7e22ce"),
  '''      <p>À l'oral naturel, les mots se <b>lient</b> et certains sons <b>disparaissent</b> ou <b>changent</b> : c'est le <span class="hl">connected speech</span>.</p>
      <table>
        <tr><th>Phénomène</th><th>Exemple écrit</th><th>Ce qu'on entend</th></tr>
        <tr><td>Liaison (linking)</td><td>an apple · turn it off</td><td>a-napple · tur-ni-toff</td></tr>
        <tr><td>Élision (son qui disparaît)</td><td>next door · last night</td><td>nex door · las night</td></tr>
        <tr><td>Assimilation (son qui change)</td><td>don't you · would you</td><td>don-chu · woo-ju</td></tr>
        <tr><td>Formes réduites</td><td>going to · want to · got to</td><td>gonna · wanna · gotta</td></tr>
        <tr><td></td><td>I don't know · let me · give me</td><td>dunno · lemme · gimme</td></tr>
        <tr><td></td><td>What do you… · kind of</td><td>whaddya · kinda</td></tr>
      </table>
      <p>Ces formes réduites sont <b>orales et familières</b> : on les comprend, mais on ne les écrit pas dans un devoir ou un mail professionnel.</p>''',
  {"red": ("choice", "Que signifie cette forme réduite ?", [
      C(None, ["going to", "go into", "gone to"], big="gonna", say="I'm gonna win."), C(None, ["want to", "want a", "wanted"], big="wanna", say="I wanna go."),
      C(None, ["got to", "got a", "gotten"], big="gotta", say="I gotta go."), C(None, ["I don't know", "do not", "done now"], big="dunno", say="I dunno."),
      C(None, ["let me", "lemon", "let's me"], big="lemme", say="Lemme see."), C(None, ["give me", "gimmick", "give it"], big="gimme", say="Gimme that."),
      C(None, ["what do you", "what are you doing", "what you"], big="whaddya", say="Whaddya want?"), C(None, ["kind of", "kind if", "can do"], big="kinda", say="It's kinda cool."),
      C(None, ["don't you", "don't chew", "do you"], big="don-chu", say="Don't you like it?"), C(None, ["would you", "would do", "what you"], big="woo-ju", say="Would you help me?"),
    ]),
    "phen": ("choice", "Quel phénomène entend-on ?", [
      C(None, ["liaison", "élision", "assimilation"], big="an apple → a-napple", say="an apple", keep=True, tip="la consonne finale se lie à la voyelle suivante → liaison."),
      C(None, ["élision", "liaison", "assimilation"], big="next door → nex door", say="next door", keep=True, tip="le t disparaît → élision."),
      C(None, ["assimilation", "élision", "liaison"], big="don't you → don-chu", say="don't you", keep=True, tip="t + y devient « ch » → assimilation."),
      C(None, ["liaison", "assimilation", "élision"], big="turn it off → tur-ni-toff", say="turn it off", keep=True, tip="liaison."),
      C(None, ["élision", "assimilation", "liaison"], big="last night → las night", say="last night", keep=True, tip="le t disparaît → élision."),
      C(None, ["assimilation", "liaison", "élision"], big="would you → woo-ju", say="would you", keep=True, tip="d + y devient « j » → assimilation."),
  ])},
  [M("red", "💬", "gonna, wanna, dunno…", "Retrouve la forme complète.", ["red"]),
   M("phen", "🔗", "Liaison, élision, assimilation", "Identifie le phénomène.", ["phen"], 6),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["red", "phen"], 12)], tag="Anglais · Expert · Phonologie")
print("content12 ok", REGISTRY)
