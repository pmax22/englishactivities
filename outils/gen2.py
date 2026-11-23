import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
exec(open(_EA_OUT+"/gen.py", encoding="utf-8").read(), globals() | {"__name__": "gen"}) if False else None
G_NS = {"__name__": "gen"}
exec(open(_EA_OUT+"/gen.py", encoding="utf-8").read(), G_NS)
globals().update({k: v for k, v in G_NS.items() if not k.startswith("__")})
def js(f): return open(f"{_EA_OUT}/{f}", encoding="utf-8").read()

PRON_LESSON = '''      <p>Les <span class="hl">pronoms personnels</span> remplacent un nom. Il y en a deux sortes :</p>
      <table>
        <tr><th>Français</th><th>Sujet</th><th>Complément</th></tr>
        <tr><td>je / me</td><td>I</td><td>me</td></tr>
        <tr><td>tu / te</td><td>you</td><td>you</td></tr>
        <tr><td>il / le, lui</td><td>he</td><td>him</td></tr>
        <tr><td>elle / la, lui</td><td>she</td><td>her</td></tr>
        <tr><td>il, elle (chose, animal)</td><td>it</td><td>it</td></tr>
        <tr><td>nous</td><td>we</td><td>us</td></tr>
        <tr><td>vous</td><td>you</td><td>you</td></tr>
        <tr><td>ils, elles / les, leur</td><td>they</td><td>them</td></tr>
      </table>
      <p><b>Sujet</b> : placé <b>avant</b> le verbe. <span class="ex">He plays football.</span></p>
      <p><b>Complément</b> : placé <b>après</b> le verbe ou après une préposition (with, to, at, for…). <span class="ex">I love him. · Look at them!</span></p>
      <p>Attention : <b>I</b> prend toujours une majuscule. <b>It</b> s'utilise pour les choses et les animaux. <b>You</b> = tu ou vous.</p>
      <p>En français le pronom complément est avant le verbe, en anglais il est <b>après</b> : <span class="ex">Je les connais → I know them.</span></p>'''

BHP_LESSON = '''      <p>Au <span class="hl">présent simple</span>, trois verbes à connaître par cœur.</p>
      <h4>Be (être)</h4>
      <table>
        <tr><th></th><th>I</th><th>he / she / it</th><th>you / we / they</th></tr>
        <tr><td><b>+</b></td><td>I am (I'm)</td><td>he is (he's)</td><td>they are (they're)</td></tr>
        <tr><td><b>−</b></td><td>I am not</td><td>he isn't</td><td>they aren't</td></tr>
        <tr><td><b>?</b></td><td>Am I…?</td><td>Is he…?</td><td>Are they…?</td></tr>
      </table>
      <p>Avec <b>be</b>, jamais de do / does : on ajoute <b>not</b> et on <b>inverse</b> sujet et verbe pour la question.</p>
      <h4>Have (avoir) et Play (jouer)</h4>
      <table>
        <tr><th></th><th>I / you / we / they</th><th>he / she / it</th></tr>
        <tr><td><b>+</b></td><td>I have · I play</td><td>she <span class="hl">has</span> · she play<span class="hl">s</span></td></tr>
        <tr><td><b>−</b></td><td>I <span class="hl">don't</span> have · I don't play</td><td>she <span class="hl">doesn't</span> have · she doesn't play</td></tr>
        <tr><td><b>?</b></td><td><span class="hl">Do</span> you have…? · Do you play…?</td><td><span class="hl">Does</span> she have…? · Does she play…?</td></tr>
      </table>
      <p>Après <b>don't / doesn't / do / does</b>, le verbe reste en <b>base verbale</b> : <span class="ex">He doesn't play football. <s>He doesn't plays.</s> · Does she have a dog? <s>Does she has?</s></span></p>'''

ART_LESSON = '''      <h4>a / an (un, une)</h4>
      <p>Pour parler d'une chose <b>quelconque</b>, au singulier, et pour les <b>métiers</b> : <span class="ex">a dog · She is a teacher.</span></p>
      <div class="formula"><span class="hl">a</span> + son consonne : a cat, a house, a university (« you »)<br><span class="hl">an</span> + son voyelle : an apple, an old car, an hour (h muet)</div>
      <h4>the (le, la, les)</h4>
      <p>Pour une chose <b>précise</b> ou déjà connue, une chose <b>unique</b>, les <b>instruments</b>, les <b>superlatifs</b> : <span class="ex">the dog next door · the sun · She plays the piano. · the best</span></p>
      <h4>Ø (pas d'article)</h4>
      <p>Pour parler en <b>général</b> (pluriel ou indénombrable) et devant les <b>sports</b>, <b>repas</b>, <b>langues</b>, <b>pays</b>, <b>jours</b>, <b>matières</b> :</p>
      <p class="ex">I love music. · Dogs are friendly. · I play football. · We have lunch. · They speak English. · He lives in France.</p>
      <p>Exceptions : <b>the</b> United States, <b>the</b> United Kingdom.</p>'''

ADJ_LESSON = '''      <h4>Niveau 1 · La place de l'adjectif</h4>
      <p>En anglais, l'adjectif se place <b>avant le nom</b> : <span class="ex">a nice sister · a red car</span>. Après le verbe <b>be</b>, il est seul : <span class="ex">I am nice.</span></p>
      <p>L'adjectif est <b>invariable</b> : pas de -s au pluriel, pas de -e au féminin. <span class="ex">two black cats <s>blacks</s> · a nice sister</span></p>
      <h4>Niveau 2 · L'ordre des adjectifs</h4>
      <p>Quand il y a plusieurs adjectifs, ils suivent un ordre précis :</p>
      <div class="formula"><b>Opinion</b> → <b>Taille</b> → <b>Âge</b> → <b>Forme</b> → <b>Couleur</b> → <b>Origine</b> → <b>Matière</b> → nom</div>
      <table>
        <tr><th>Opinion</th><th>Taille</th><th>Âge</th><th>Forme</th><th>Couleur</th><th>Origine</th><th>Matière</th></tr>
        <tr><td>beautiful, nice, ugly</td><td>big, small, tall</td><td>old, new, young</td><td>round, square</td><td>red, black</td><td>French, Italian</td><td>wooden, leather</td></tr>
      </table>
      <p class="ex">a beautiful old Italian car · a big round wooden table · a lovely little black cat</p>
      <p>Astuce : d'abord ce que je <b>pense</b>, puis ce que je <b>vois</b>, puis d'où ça <b>vient</b> et en quoi c'est <b>fait</b>.</p>'''

page("pronoms_personnels.html", "Pronoms personnels – Entraînement", "Anglais · Grammaire", 'Les pronoms <span>personnels</span>',
     "Sujet : I, you, he… · Complément : me, you, him…", ("#60a5fa", "#2563eb"), PRON_LESSON, "", js("pronoms.js"))
page("be_have_play.html", "Be, Have, Play – Entraînement", "Anglais · Grammaire", '<span>Be</span>, <span>Have</span> &amp; <span>Play</span>',
     "Présent simple · affirmatif, négatif, interrogatif", ("#f87171", "#dc2626"), BHP_LESSON, "", js("bhp.js"))
page("articles.html", "Les articles – Entraînement", "Anglais · Grammaire", 'Les <span>articles</span>',
     "a · an · the · Ø (pas d'article)", ("#a3e635", "#65a30d"), ART_LESSON, "", js("articles.js"))
page("adjectifs.html", "Les adjectifs – Entraînement", "Anglais · Grammaire", 'Les <span>adjectifs</span>',
     "Niveau 1 : la place de l'adjectif · Niveau 2 : l'ordre des adjectifs", ("#e879f9", "#c026d3"), ADJ_LESSON, "", js("adjectifs.js"))

ADV_LESSON = '''      <p>Les <span class="hl">adverbes de fréquence</span> disent à quelle fréquence on fait quelque chose.</p>
      <table>
        <tr><th>always</th><th>usually</th><th>often</th><th>sometimes</th><th>rarely</th><th>never</th></tr>
        <tr><td>100 %</td><td>90 %</td><td>70 %</td><td>50 %</td><td>10 %</td><td>0 %</td></tr>
        <tr><td>toujours</td><td>d'habitude</td><td>souvent</td><td>parfois</td><td>rarement</td><td>jamais</td></tr>
      </table>
      <p><b>Place de l'adverbe :</b></p>
      <div class="formula">Avec <b>be</b> : sujet + am / is / are + <span class="hl">adverbe</span> → She is <b>always</b> late.<br>Avec les autres verbes : sujet + <span class="hl">adverbe</span> + verbe → I <b>always</b> play football.</div>
      <p><b>never</b> est déjà négatif : <span class="ex">I never drink coffee. <s>I don't never drink.</s></span></p>
      <p><b>sometimes</b> et <b>usually</b> peuvent aussi se placer en début de phrase : <span class="ex">Sometimes they watch TV.</span></p>
      <p><b>How often…?</b> = à quelle fréquence ? On peut répondre avec une expression en fin de phrase : <span class="ex">once a week (une fois par semaine) · twice a month · three times a year · every day</span></p>'''
page("adverbes_frequence.html", "Adverbes de fréquence – Entraînement", "Anglais · Grammaire", 'Les adverbes de <span>fréquence</span>',
     "always · usually · often · sometimes · rarely · never", ("#fb923c", "#ea580c"), ADV_LESSON, "", js("adverbes.js"))
