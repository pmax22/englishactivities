import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
exec(open(_EA_OUT+"/content_helpers.py", encoding="utf-8").read())
PHO, EXP = "Anglais · Phonologie", "Anglais · Expert · Phonologie"

def P(word, ok, opts, tip, say=None, keep=True):
    return C(None, opts, big=word, say=say or word, c=opts.index(ok), keep=keep, tip=tip)
def MP(word, a, b, tip):
    return C(None, [word, b if word == a else a], say=word, listen=True, tip=tip)
def ST(word, syl, k, tip=""):  # où tombe l'accent ?
    opts = ["-".join(s.upper() if i == j else s for i, s in enumerate(syl)) for j in range(len(syl))]
    return C(None, opts[:4], big=word, say=word, c=k, keep=True, tip=tip or f"Accent sur <b>{syl[k].upper()}</b>.")

# ═════════════ HOMOPHONES ═════════════
newpage("homophones.html", "Les homophones – Entraînement", 'there, <span>their</span>, they\'re',
  "Des mots qui se prononcent pareil mais s'écrivent différemment", ("#fbcfe8", "#db2777"),
  '''      <p>Les <span class="hl">homophones</span> se prononcent de la même façon mais n'ont ni la même orthographe ni le même sens.</p>
      <table>
        <tr><th>Mots</th><th>Sens</th></tr>
        <tr><td>there / their / they're</td><td>là / leur(s) / they are</td></tr>
        <tr><td>to / too / two</td><td>à, vers / aussi, trop / deux</td></tr>
        <tr><td>your / you're</td><td>ton, votre / you are</td></tr>
        <tr><td>its / it's</td><td>son, sa (chose) / it is</td></tr>
        <tr><td>write / right</td><td>écrire / droite, juste</td></tr>
        <tr><td>know / no · knew / new</td><td>savoir / non · savait / nouveau</td></tr>
        <tr><td>hear / here · see / sea</td><td>entendre / ici · voir / mer</td></tr>
        <tr><td>buy / by / bye · for / four</td><td>acheter / par / au revoir · pour / quatre</td></tr>
        <tr><td>where / wear · meet / meat · son / sun</td><td>où / porter · rencontrer / viande · fils / soleil</td></tr>
      </table>
      <p>Astuce : si tu peux remplacer par <b>they are / you are / it is</b>, il faut l'apostrophe.</p>''',
  {"choice": ("choice", "Choisis le bon homophone", [
      C("____ house is very big.", ["Their", "There", "They're"], keep=True, tip="leur maison → their."), C("Put the box over ____ .", ["there", "their", "they're"], keep=True, tip="là-bas → there."),
      C("____ coming tomorrow.", ["They're", "Their", "There"], keep=True, tip="they are → they're."), C("I have ____ brothers.", ["two", "too", "to"], keep=True, tip="deux → two."),
      C("This tea is ____ hot.", ["too", "to", "two"], keep=True, tip="trop → too."), C("Is this ____ bag?", ["your", "you're"], keep=True, tip="ton sac → your."),
      C("____ very kind!", ["You're", "Your"], keep=True, tip="you are → you're."), C("The dog is eating ____ food.", ["its", "it's"], keep=True, tip="sa nourriture → its (sans apostrophe)."),
      C("Turn ____ at the traffic lights.", ["right", "write"], keep=True, tip="à droite → right."), C("I don't ____ the answer.", ["know", "no"], keep=True, tip="savoir → know."),
      C("Can you ____ me?", ["hear", "here"], keep=True, tip="entendre → hear."), C("I want to ____ a new phone.", ["buy", "by", "bye"], keep=True, tip="acheter → buy."),
      C("____ are you going?", ["Where", "Wear", "Were"], keep=True, tip="où → where."), C("We swam in the ____ .", ["sea", "see"], keep=True, tip="la mer → sea."),
  ])},
  [M("choice", "👯", "Le bon homophone", "there / their / they're, to / too / two…", ["choice"], 12)], tag=PHO)

# ═════════════ CUP / CAP / BIRD ═════════════
UH, AE, ER = "/ʌ/ (cup)", "/æ/ (cat)", "/ɜː/ (bird)"
newpage("phono_cup_bird.html", "Les sons /ʌ/, /æ/ et /ɜː/ – Entraînement", '<span>cup</span>, cap, bird',
  "Trois voyelles difficiles pour les francophones", ("#fed7aa", "#ea580c"),
  '''      <table>
        <tr><th>Son</th><th>Comment ?</th><th>Exemples</th></tr>
        <tr><td><span class="hl">/ʌ/</span></td><td>bouche peu ouverte, son bref proche d'un « a » sourd</td><td>cup, sun, love, money, mother, bus, young</td></tr>
        <tr><td><span class="hl">/æ/</span></td><td>bouche très ouverte, entre « a » et « è »</td><td>cat, black, apple, hat, man, bag</td></tr>
        <tr><td><span class="hl">/ɜː/</span></td><td>son long, comme dans « heure » sans arrondir les lèvres</td><td>bird, work, learn, her, turn, girl, first</td></tr>
      </table>
      <p>Attention : <b>o</b> se prononce souvent /ʌ/ : <i>love, money, mother, come, son, some</i>. Et <b>wor-</b> se prononce /wɜː/ : <i>work, word, world</i>.</p>''',
  {"mp": ("choice", "Écoute : quel mot entends-tu ?", [
      MP("cup", "cup", "cap", "cup /ʌ/ · cap /æ/."), MP("cap", "cup", "cap", "cup /ʌ/ · cap /æ/."), MP("hut", "hut", "hat", "hut /ʌ/ · hat /æ/."),
      MP("hat", "hut", "hat", "hut /ʌ/ · hat /æ/."), MP("bug", "bug", "bag", "bug /ʌ/ · bag /æ/."), MP("bag", "bug", "bag", "bug /ʌ/ · bag /æ/."),
      MP("fun", "fun", "fan", "fun /ʌ/ · fan /æ/."), MP("work", "work", "walk", "work /ɜː/ · walk /ɔː/."), MP("walk", "work", "walk", "work /ɜː/ · walk /ɔː/."),
      MP("bird", "bird", "bud", "bird /ɜː/ · bud /ʌ/."),
    ]),
    "cls": ("choice", "Écoute : quel son entends-tu ?", [
      P("sun", UH, [UH, AE, ER], "/ʌ/."), P("love", UH, [UH, AE, ER], "o → /ʌ/."), P("money", UH, [UH, AE, ER], "o → /ʌ/."), P("mother", UH, [UH, AE, ER], "o → /ʌ/."),
      P("black", AE, [UH, AE, ER], "/æ/."), P("apple", AE, [UH, AE, ER], "/æ/."), P("man", AE, [UH, AE, ER], "/æ/."),
      P("learn", ER, [UH, AE, ER], "/ɜː/."), P("her", ER, [UH, AE, ER], "/ɜː/."), P("turn", ER, [UH, AE, ER], "/ɜː/."), P("girl", ER, [UH, AE, ER], "/ɜː/."), P("world", ER, [UH, AE, ER], "wor- → /ɜː/."),
  ])},
  [M("mp", "👂", "cup ou cap ?", "Écoute et choisis le mot entendu.", ["mp"]),
   M("cls", "🔤", "/ʌ/, /æ/ ou /ɜː/ ?", "Classe les mots selon leur voyelle.", ["cls"], 12),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["mp", "cls"], 12)], tag=PHO)

# ═════════════ DIPHTONGUES ═════════════
DIP = ["/eɪ/ (make)", "/aɪ/ (time)", "/əʊ/ (go)", "/aʊ/ (now)", "/ɔɪ/ (boy)"]
newpage("diphtongues.html", "Les diphtongues – Entraînement", 'Les <span>diphtongues</span>',
  "make, time, go, now, boy : deux sons en un", ("#c7d2fe", "#6366f1"),
  '''      <p>Une <span class="hl">diphtongue</span> est une voyelle qui <b>glisse</b> d'un son vers un autre dans la même syllabe.</p>
      <table>
        <tr><th>Diphtongue</th><th>Exemples</th><th>Diphtongue</th><th>Exemples</th></tr>
        <tr><td><span class="hl">/eɪ/</span></td><td>make, rain, day, great</td><td><span class="hl">/aʊ/</span></td><td>now, house, cow, town</td></tr>
        <tr><td><span class="hl">/aɪ/</span></td><td>time, my, light, buy</td><td><span class="hl">/ɔɪ/</span></td><td>boy, coin, enjoy, toy</td></tr>
        <tr><td><span class="hl">/əʊ/</span></td><td>go, home, know, road</td><td><span class="hl">/ɪə/ · /eə/ · /ʊə/</span></td><td>here, near · hair, where · tour</td></tr>
      </table>
      <p>Piège : le <b>a</b> de <i>make, name, table</i> se dit /eɪ/, le <b>i</b> de <i>time, nice, like</i> se dit /aɪ/, le <b>o</b> de <i>go, home, phone</i> se dit /əʊ/.</p>''',
  {"cls": ("choice", "Écoute : quelle diphtongue entends-tu ?", [
      P("make", DIP[0], DIP, "a + consonne + e → /eɪ/."), P("rain", DIP[0], DIP, "ai → /eɪ/."), P("day", DIP[0], DIP, "ay → /eɪ/."), P("great", DIP[0], DIP, "great → /eɪ/ (exception de -ea)."),
      P("time", DIP[1], DIP, "i + consonne + e → /aɪ/."), P("light", DIP[1], DIP, "igh → /aɪ/."), P("buy", DIP[1], DIP, "buy → /aɪ/."),
      P("home", DIP[2], DIP, "o + consonne + e → /əʊ/."), P("know", DIP[2], DIP, "ow → /əʊ/ ici."), P("road", DIP[2], DIP, "oa → /əʊ/."),
      P("house", DIP[3], DIP, "ou → /aʊ/."), P("town", DIP[3], DIP, "ow → /aʊ/ ici."), P("boy", DIP[4], DIP, "oy → /ɔɪ/."), P("coin", DIP[4], DIP, "oi → /ɔɪ/."),
  ])},
  [M("cls", "〰️", "Quelle diphtongue ?", "Écoute et classe les mots.", ["cls"], 12)], tag=PHO)

# ═════════════ ACCENT DE PHRASE ═════════════
newpage("accent_phrase.html", "L'accent de phrase – Entraînement", "L'accent de <span>phrase</span>",
  "Mots pleins et mots outils · accent contrastif", ("#a7f3d0", "#059669"),
  '''      <p>Dans une phrase, on accentue les <b>mots pleins</b> (ceux qui portent le sens) et on prononce faiblement les <b>mots outils</b>.</p>
      <table>
        <tr><th>Mots accentués (pleins)</th><th>Mots inaccentués (outils)</th></tr>
        <tr><td>noms, verbes principaux, adjectifs, adverbes, mots interrogatifs, négations (can't, don't)</td><td>articles, prépositions, pronoms, auxiliaires, conjonctions (a, the, to, of, and, he, is, can…)</td></tr>
      </table>
      <p class="ex">I WANT to BUY a NEW CAR. · WHERE do you LIVE?</p>
      <h4>Accent contrastif</h4>
      <p>On peut accentuer un mot pour <b>corriger</b> ou <b>insister</b>, ce qui change le sens :</p>
      <p class="ex">I didn't take YOUR bike. (j'ai pris celui de quelqu'un d'autre) · I didn't take your BIKE. (j'ai pris autre chose)</p>''',
  {"words": ("choice", "Quels mots sont accentués ?", [
      C(None, ["WANT, BUY, NEW, CAR", "I, TO, A", "I, WANT, TO, A"], big="I want to buy a new car.", say="I want to buy a new car.", tip="mots pleins : verbes, adjectif, nom."),
      C(None, ["WHERE, LIVE", "DO, YOU", "WHERE, DO, YOU"], big="Where do you live?", say="Where do you live?", tip="mot interrogatif + verbe principal."),
      C(None, ["CAT, SLEEPING, SOFA", "THE, IS, ON", "IS, ON, THE"], big="The cat is sleeping on the sofa.", say="The cat is sleeping on the sofa.", tip="noms et verbe principal."),
      C(None, ["CAN'T, COME, TOMORROW", "SHE, CAN'T", "SHE, COME"], big="She can't come tomorrow.", say="She can't come tomorrow.", tip="la négation can't est accentuée."),
      C(None, ["DRINK, CUP, TEA", "A, OF", "I'D, LIKE, A"], big="I'd like to drink a cup of tea.", say="I'd like to drink a cup of tea.", tip="like est souvent accentué aussi ; jamais a, to, of."),
    ]),
    "contrast": ("choice", "Que veut dire la phrase avec cet accent ?", [
      C(None, ["Ce n'est pas moi qui ai pris ton vélo.", "J'ai pris le vélo de quelqu'un d'autre.", "J'ai pris ta voiture, pas ton vélo."], big="I didn't take your bike.", bigsub="accent sur I", say="I didn't take your bike.", tip="accent sur I → quelqu'un d'autre l'a pris."),
      C(None, ["J'ai pris le vélo de quelqu'un d'autre.", "Ce n'est pas moi.", "Je l'ai acheté, pas pris."], big="I didn't take YOUR bike.", say="I didn't take your bike.", tip="accent sur YOUR → c'était un autre vélo."),
      C(None, ["J'ai pris autre chose que ton vélo.", "Ce n'est pas moi.", "J'ai pris le vélo de ton frère."], big="I didn't take your BIKE.", say="I didn't take your bike.", tip="accent sur BIKE → un autre objet."),
      C(None, ["Je l'ai emprunté ou acheté, pas pris.", "C'était le vélo de quelqu'un d'autre.", "Ce n'est pas moi."], big="I didn't TAKE your bike.", say="I didn't take your bike.", tip="accent sur TAKE → une autre action."),
  ])},
  [M("words", "🎯", "Les mots accentués", "Mots pleins ou mots outils ?", ["words"], 5),
   M("contrast", "⚡", "L'accent contrastif", "Le sens change selon le mot accentué.", ["contrast"], 4),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["words", "contrast"], 9)], tag=PHO)

# ═════════════ GRAPHIES TROMPEUSES ═════════════
newpage("graphies.html", "Les graphies trompeuses – Entraînement", 'though, through, <span>tough</span>',
  "Une même graphie, plusieurs prononciations", ("#fde68a", "#d97706"),
  '''      <p>En anglais, une même suite de lettres peut se prononcer de façons très différentes.</p>
      <table>
        <tr><th>Graphie</th><th>Prononciations</th></tr>
        <tr><td><b>-ough</b></td><td>though /əʊ/ · through /uː/ · tough, enough /ʌf/ · cough /ɒf/ · bought, thought /ɔː/ · plough /aʊ/</td></tr>
        <tr><td><b>ea</b></td><td>eat, sea /iː/ · bread, head /e/ · great, break /eɪ/ · bear, wear /eə/ · heart /ɑː/</td></tr>
        <tr><td><b>oo</b></td><td>food, moon /uː/ · book, good /ʊ/ · blood, flood /ʌ/ · door, floor /ɔː/</td></tr>
        <tr><td><b>ow</b></td><td>now, cow /aʊ/ · know, snow /əʊ/</td></tr>
        <tr><td><b>ch</b></td><td>chair /tʃ/ · school, Christmas /k/ · machine /ʃ/</td></tr>
      </table>''',
  {"rhyme": ("choice", "Quel mot rime avec celui-ci ?", [
      C(None, ["go", "too", "cow"], big="though", say="though", tip="though /ðəʊ/ rime avec go."), C(None, ["blue", "cow", "off"], big="through", say="through", tip="through /θruː/ rime avec blue."),
      C(None, ["stuff", "go", "off"], big="tough", say="tough", tip="tough /tʌf/ rime avec stuff."), C(None, ["off", "stuff", "now"], big="cough", say="cough", tip="cough /kɒf/ rime avec off."),
      C(None, ["red", "need", "made"], big="bread", say="bread", tip="bread /bred/ rime avec red."), C(None, ["late", "street", "bed"], big="great", say="great", tip="great /ɡreɪt/ rime avec late."),
      C(None, ["mud", "food", "good"], big="blood", say="blood", tip="blood /blʌd/ rime avec mud."), C(None, ["could", "food", "mud"], big="good", say="good", tip="good /ɡʊd/ rime avec could."),
      C(None, ["sport", "out", "boat"], big="bought", say="bought", tip="bought /bɔːt/ rime avec sport."), C(None, ["more", "food", "good"], big="door", say="door", tip="door /dɔː/ rime avec more."),
    ]),
    "ch": ("choice", "Comment se prononce ch ?", [
      P("chair", "/tʃ/", ["/tʃ/", "/k/", "/ʃ/"], "chair /tʃ/."), P("school", "/k/", ["/tʃ/", "/k/", "/ʃ/"], "school /k/ (origine grecque)."),
      P("machine", "/ʃ/", ["/tʃ/", "/k/", "/ʃ/"], "machine /ʃ/ (origine française)."), P("Christmas", "/k/", ["/tʃ/", "/k/", "/ʃ/"], "Christmas /k/."),
      P("cheese", "/tʃ/", ["/tʃ/", "/k/", "/ʃ/"], "cheese /tʃ/."), P("chef", "/ʃ/", ["/tʃ/", "/k/", "/ʃ/"], "chef /ʃ/ (origine française)."),
  ])},
  [M("rhyme", "🎶", "Ça rime ?", "-ough, ea, oo : trouve la rime.", ["rhyme"]),
   M("ch", "🔤", "ch : /tʃ/, /k/ ou /ʃ/ ?", "chair, school, machine…", ["ch"], 6),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["rhyme", "ch"], 12)], tag=PHO)

# ═════════════ INTRO API ═════════════
def SYM(sym, ok, others, tip):
    return C(None, [ok] + others, big=sym, bigsub="Quel mot contient ce son ?", tip=tip)
newpage("api_intro.html", "L'alphabet phonétique – Entraînement", "L'alphabet <span>phonétique</span> (API)",
  "Lire les symboles des dictionnaires", ("#ddd6fe", "#7c3aed"),
  '''      <p>L'<span class="hl">alphabet phonétique international (API)</span> note les <b>sons</b>, pas les lettres. On l'écrit entre barres obliques : <i>/ʃɪp/</i> = ship. Chaque symbole correspond à un seul son.</p>
      <table>
        <tr><th>Consonnes</th><th>Exemple</th><th>Voyelles</th><th>Exemple</th></tr>
        <tr><td>/θ/</td><td><b>th</b>ink</td><td>/iː/ · /ɪ/</td><td>sh<b>ee</b>p · sh<b>i</b>p</td></tr>
        <tr><td>/ð/</td><td><b>th</b>is</td><td>/uː/ · /ʊ/</td><td>f<b>oo</b>d · b<b>oo</b>k</td></tr>
        <tr><td>/ʃ/</td><td><b>sh</b>e</td><td>/æ/ · /ʌ/</td><td>c<b>a</b>t · c<b>u</b>p</td></tr>
        <tr><td>/tʃ/ · /dʒ/</td><td><b>ch</b>air · <b>J</b>une</td><td>/ɑː/ · /ɔː/</td><td>c<b>ar</b> · d<b>oor</b></td></tr>
        <tr><td>/ʒ/</td><td>mea<b>s</b>ure</td><td>/ɜː/</td><td>b<b>ir</b>d</td></tr>
        <tr><td>/ŋ/</td><td>si<b>ng</b></td><td>/ə/ (schwa)</td><td><b>a</b>bout, teach<b>er</b></td></tr>
        <tr><td>/j/</td><td><b>y</b>es</td><td>/ɒ/ · /e/</td><td>h<b>o</b>t · b<b>e</b>d</td></tr>
      </table>
      <p>Le signe <b>ː</b> indique une voyelle <b>longue</b>. L'apostrophe haute <b>ˈ</b> se place <b>avant</b> la syllabe accentuée : /ˈtiːtʃə/.</p>''',
  {"sym": ("choice", "Quel mot contient ce son ?", [
      SYM("/θ/", "think", ["this", "tin"], "/θ/ = th sourd."), SYM("/ð/", "mother", ["thank", "dog"], "/ð/ = th sonore."), SYM("/ʃ/", "shoe", ["chair", "sun"], "/ʃ/ = sh."),
      SYM("/tʃ/", "chicken", ["shop", "cat"], "/tʃ/ = ch de chair."), SYM("/dʒ/", "jam", ["yes", "shop"], "/dʒ/ = j de June."), SYM("/ŋ/", "sing", ["sin", "sign"], "/ŋ/ = ng final."),
      SYM("/j/", "yellow", ["jelly", "eel"], "/j/ = y de yes."), SYM("/ʒ/", "television", ["tension", "jet"], "/ʒ/ = s de measure, television."),
      SYM("/iː/", "sheep", ["ship", "shape"], "/iː/ = i long."), SYM("/ʌ/", "cup", ["cap", "cop"], "/ʌ/ = u de cup."), SYM("/ɜː/", "word", ["ward", "wood"], "/ɜː/ = ir, ur, wor."), SYM("/ə/", "about", ["apple", "able"], "/ə/ = schwa, voyelle faible."),
    ]),
    "read": ("choice", "Quel mot est transcrit ?", [
      C(None, ["ship", "sheep", "chip"], big="/ʃɪp/", say="ship"), C(None, ["think", "sink", "this"], big="/θɪŋk/", say="think"), C(None, ["cup", "cap", "cop"], big="/kʌp/", say="cup"),
      C(None, ["bird", "bed", "bud"], big="/bɜːd/", say="bird"), C(None, ["June", "yawn", "shoe"], big="/dʒuːn/", say="June"), C(None, ["yes", "jazz", "geese"], big="/jes/", say="yes"),
  ])},
  [M("sym", "🔣", "Quel mot contient ce son ?", "Associe le symbole à un mot.", ["sym"], 12),
   M("read", "📖", "Lis la transcription", "Retrouve le mot transcrit.", ["read"], 6),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["sym", "read"], 12)], tag=PHO)

# ═════════════ EXPERT : PHONÈMES ET MORPHÈMES ═════════════
newpage("phonemes_morphemes.html", "Phonèmes et morphèmes – Expert", '<span>Phonèmes</span> & morphèmes',
  "Compter les sons, découper les mots", ("#e9d5ff", "#9333ea"),
  '''      <h4>Phonème et graphème</h4>
      <p>Un <span class="hl">phonème</span> est la plus petite unité de <b>son</b> qui permet de distinguer deux mots (/ʃɪp/ ≠ /ʃiːp/). Un <span class="hl">graphème</span> est la lettre ou le groupe de lettres qui l'écrit (sh, ee, igh…).</p>
      <p class="ex">knight : 6 lettres, mais 3 phonèmes /n aɪ t/ · think : 5 lettres, 4 phonèmes /θ ɪ ŋ k/ · box : 3 lettres, 4 phonèmes /b ɒ k s/</p>
      <h4>Morphème</h4>
      <p>Un <span class="hl">morphème</span> est la plus petite unité de <b>sens</b>. On distingue :</p>
      <p>• le morphème <b>libre</b> (la base, qui peut exister seule) : <i>happy, play, teach</i> ;</p>
      <p>• les morphèmes <b>liés</b> : préfixes (<i>un-, re-, dis-</i>), suffixes dérivationnels (<i>-ness, -er, -less</i>) et flexions (<i>-s, -ed, -ing</i>).</p>
      <p class="ex">unhappiness = un + happi + ness (3 morphèmes) · teachers = teach + er + s (3) · replayed = re + play + ed (3)</p>''',
  {"pho": ("choice", "Combien de phonèmes ?", [
      C(None, ["3", "4", "5"], big="ship", say="ship", keep=True, tip="/ʃ ɪ p/ : sh = un seul son."), C(None, ["4", "5", "3"], big="think", say="think", keep=True, tip="/θ ɪ ŋ k/."),
      C(None, ["3", "5", "4"], big="knife", say="knife", keep=True, tip="/n aɪ f/ : k et e muets."), C(None, ["4", "3", "2"], big="box", say="box", keep=True, tip="/b ɒ k s/ : x = deux sons."),
      C(None, ["2", "3", "5"], big="eight", say="eight", keep=True, tip="/eɪ t/."), C(None, ["3", "4", "7"], big="through", say="through", keep=True, tip="/θ r uː/."),
      C(None, ["4", "3", "6"], big="school", say="school", keep=True, tip="/s k uː l/."), C(None, ["3", "4", "6"], big="knight", say="knight", keep=True, tip="/n aɪ t/."),
      C(None, ["3", "4", "5"], big="cheese", say="cheese", keep=True, tip="/tʃ iː z/."), C(None, ["4", "3", "5"], big="six", say="six", keep=True, tip="/s ɪ k s/."),
    ]),
    "morph": ("choice", "Comment se découpe ce mot en morphèmes ?", [
      C(None, ["un + happi + ness", "unha + ppi + ness", "un + happiness"], big="unhappiness", tip="préfixe + base + suffixe (3 morphèmes)."),
      C(None, ["teach + er + s", "tea + chers", "teacher + s + er"], big="teachers", tip="base + suffixe -er + pluriel -s."),
      C(None, ["re + play + ed", "rep + lay + ed", "replay + d"], big="replayed", tip="préfixe re- + base + -ed."),
      C(None, ["care + less", "car + eless", "ca + re + less"], big="careless", tip="base + suffixe -less."),
      C(None, ["un + believ + able", "unbe + liev + able", "un + belie + vable"], big="unbelievable", tip="un- + believe + -able."),
      C(None, ["friend + ship + s", "fri + end + ships", "friends + hip"], big="friendships", tip="base + -ship + -s."),
    ]),
    "count": ("choice", "Combien de morphèmes ?", [
      C(None, ["1", "2", "3"], big="cat", keep=True, tip="une seule unité de sens."), C(None, ["2", "1", "3"], big="dogs", keep=True, tip="dog + s."),
      C(None, ["2", "3", "1"], big="walked", keep=True, tip="walk + ed."), C(None, ["3", "2", "4"], big="unkindness", keep=True, tip="un + kind + ness."),
      C(None, ["2", "1", "3"], big="impossible", keep=True, tip="im + possible."), C(None, ["3", "2", "4"], big="rebuilding", keep=True, tip="re + build + ing."),
  ])},
  [M("pho", "🔊", "Compter les phonèmes", "Combien de sons dans ce mot ?", ["pho"]),
   M("morph", "✂️", "Découper en morphèmes", "Préfixe, base, suffixe.", ["morph"], 6),
   M("count", "🔢", "Compter les morphèmes", "Combien d'unités de sens ?", ["count"], 6),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["pho", "morph", "count"], 12)], tag=EXP)

# ═════════════ EXPERT : NOTATION DE L'ACCENT ═════════════
def PAT(word, ok, opts, tip):
    return C(None, opts, big=word, say=word, c=opts.index(ok), keep=True, tip=tip)
newpage("accent_notation.html", "La notation de l'accent – Expert", 'Accent <span>1</span>, <span>2</span>, <span>0</span>',
  "Schémas accentuels : /10/, /01/, /010/, /2010/…", ("#c4b5fd", "#6d28d9"),
  '''      <p>Dans la tradition française d'analyse de l'anglais, on note l'accent de chaque syllabe par un chiffre :</p>
      <table>
        <tr><th>Chiffre</th><th>Sens</th><th>Symbole API</th></tr>
        <tr><td><span class="hl">1</span></td><td>accent <b>primaire</b> (la syllabe la plus forte)</td><td>ˈ (en haut, avant la syllabe)</td></tr>
        <tr><td><span class="hl">2</span></td><td>accent <b>secondaire</b></td><td>ˌ (en bas, avant la syllabe)</td></tr>
        <tr><td><span class="hl">0</span></td><td>syllabe <b>inaccentuée</b> (voyelle souvent réduite en /ə/ ou /ɪ/)</td><td>—</td></tr>
      </table>
      <p class="ex">teacher /10/ · hotel /01/ · computer /010/ · family /100/ · information /2010/ /ˌɪnfəˈmeɪʃn/ · Japanese /201/</p>
      <p>Un mot a toujours <b>un seul</b> accent primaire. L'accent secondaire apparaît généralement deux syllabes avant le primaire dans les mots longs.</p>''',
  {"pat": ("choice", "Quel est le schéma accentuel ?", [
      PAT("teacher", "/10/", ["/10/", "/01/"], "TEA-cher."), PAT("hotel", "/01/", ["/10/", "/01/"], "ho-TEL."), PAT("garden", "/10/", ["/10/", "/01/"], "GAR-den."), PAT("begin", "/01/", ["/10/", "/01/"], "be-GIN."),
      PAT("computer", "/010/", ["/100/", "/010/", "/001/"], "com-PU-ter."), PAT("family", "/100/", ["/100/", "/010/", "/001/"], "FA-mi-ly."), PAT("banana", "/010/", ["/100/", "/010/", "/001/"], "ba-NA-na."),
      PAT("important", "/010/", ["/100/", "/010/", "/201/"], "im-POR-tant."), PAT("Japanese", "/201/", ["/100/", "/010/", "/201/"], "ˌJa-pa-ˈNESE."), PAT("afternoon", "/201/", ["/100/", "/010/", "/201/"], "ˌaf-ter-ˈNOON."),
      PAT("information", "/2010/", ["/1000/", "/0100/", "/2010/"], "ˌin-for-ˈMA-tion."), PAT("photographer", "/0100/", ["/1000/", "/0100/", "/2010/"], "pho-TO-gra-pher."),
      PAT("photographic", "/2010/", ["/1000/", "/0100/", "/2010/"], "ˌpho-to-ˈGRA-phic."), PAT("economy", "/0100/", ["/1000/", "/0100/", "/2010/"], "e-CO-no-my."),
      PAT("economic", "/2010/", ["/1000/", "/0100/", "/2010/"], "ˌe-co-ˈNO-mic."), PAT("understand", "/201/", ["/100/", "/010/", "/201/"], "ˌun-der-ˈSTAND."),
  ])},
  [M("pat", "🔢", "Le schéma accentuel", "/10/, /01/, /010/, /2010/…", ["pat"], 12)], tag=EXP)

# ═════════════ EXPERT : SUFFIXES ═════════════
NEU, CON, ACC = "neutre (faible)", "contraignant", "accentué (fort)"
def SUF(word, kind, tip): return C(None, [NEU, CON, ACC], big=word, say=word, c=[NEU, CON, ACC].index(kind), keep=True, tip=tip)
newpage("suffixes_accent.html", "Les suffixes et l'accent – Expert", 'Suffixes <span>forts</span> et faibles',
  "Comment les suffixes déplacent (ou non) l'accent", ("#fbcfe8", "#be185d"),
  '''      <p>Les suffixes n'ont pas tous le même effet sur la place de l'accent. Les grammaires anglicistes en distinguent trois familles (les termes varient selon les manuels) :</p>
      <table>
        <tr><th>Famille</th><th>Effet</th><th>Suffixes</th><th>Exemples</th></tr>
        <tr><td><span class="hl">neutres</span> (faibles)</td><td>ne déplacent <b>pas</b> l'accent de la base</td><td>-ness, -ful, -less, -ment, -er, -or, -ly, -ing, -ed, -ship, -hood, -dom, -able, -ish</td><td>ˈhappy → ˈhappiness · emˈploy → emˈployment · ˈcomfort → ˈcomfortable</td></tr>
        <tr><td><span class="hl">contraignants</span></td><td>accent sur la syllabe <b>juste avant</b> le suffixe (/-1/)</td><td>-ic, -ical, -ion, -ian, -ial, -ious, -ity</td><td>ecoˈnomic · deˈcision · muˈsician · poˈlitical · possiˈbility</td></tr>
        <tr><td><span class="hl">accentués</span> (forts, autoaccentués)</td><td>portent <b>eux-mêmes</b> l'accent primaire</td><td>-ee, -eer, -ese, -ette, -oo, -ique, -esque, -ade</td><td>emploˈyee · engiˈneer · Japaˈnese · cigaˈrette · kangaˈroo · uˈnique</td></tr>
      </table>
      <p class="ex">ˈphotograph → phoˈtographer (-er : neutre mais base phoˈtography) → photoˈgraphic (-ic : contraignant)</p>''',
  {"kind": ("choice", "Quel type de suffixe ?", [
      SUF("happiness", NEU, "-ness est neutre : ˈhappy → ˈhappiness."), SUF("careful", NEU, "-ful est neutre."), SUF("employment", NEU, "-ment est neutre : emˈploy → emˈployment."),
      SUF("friendship", NEU, "-ship est neutre."), SUF("economic", CON, "-ic : accent sur la syllabe précédente (eco-NO-mic)."), SUF("decision", CON, "-ion : de-CI-sion."),
      SUF("musician", CON, "-ian : mu-SI-cian."), SUF("possibility", CON, "-ity : possi-BI-lity."), SUF("delicious", CON, "-ious : de-LI-cious."),
      SUF("employee", ACC, "-ee porte l'accent : emplo-YEE."), SUF("engineer", ACC, "-eer porte l'accent : engi-NEER."), SUF("Chinese", ACC, "-ese porte l'accent : Chi-NESE."),
      SUF("cigarette", ACC, "-ette porte l'accent."), SUF("unique", ACC, "-ique porte l'accent : u-NIQUE."),
    ]),
    "stress": ("choice", "Où tombe l'accent primaire ?", [
      ST("electric", ["e", "lec", "tric"], 1, "-ic : syllabe avant le suffixe."), ST("scientific", ["sci", "en", "ti", "fic"], 2, "-ic : syllabe avant le suffixe (TI)."),
      ST("education", ["e", "du", "ca", "tion"], 2, "-ion : syllabe avant (CA)."), ST("political", ["po", "li", "ti", "cal"], 1, "-ical : syllabe avant (LI)."),
      ST("official", ["of", "fi", "cial"], 1, "-ial : syllabe avant (FI)."), ST("volunteer", ["vo", "lun", "teer"], 2, "-eer accentué."),
      ST("guarantee", ["gua", "ran", "tee"], 2, "-ee accentué."), ST("comfortable", ["com", "for", "ta", "ble"], 0, "-able neutre : comme ˈcomfort."),
  ])},
  [M("kind", "🏷️", "Neutre, contraignant ou accentué ?", "Classe chaque suffixe.", ["kind"], 12),
   M("stress", "🎯", "Où tombe l'accent ?", "Applique la règle du suffixe.", ["stress"], 8),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["kind", "stress"], 12)], tag=EXP)

# ═════════════ EXPERT : PRÉFIXES ET PAIRES NOM / VERBE ═════════════
newpage("prefixes_accent.html", "Préfixes et paires nom / verbe – Expert", '<span>RE</span>cord / re<span>CORD</span>',
  "Les préfixes inaccentués et les paires nom / verbe", ("#bbf7d0", "#047857"),
  '''      <h4>Les préfixes</h4>
      <p>Dans les <b>verbes de deux syllabes</b> formés d'un préfixe (be-, de-, re-, pre-, ex-, con-, for-, mis-…), le préfixe est <b>inaccentué</b> : l'accent tombe sur la <b>base</b> → schéma /01/.</p>
      <p class="ex">beˈgin · deˈcide · reˈmain · preˈfer · exˈplain · conˈtain · forˈget · misˈtake</p>
      <h4>Les paires nom / verbe</h4>
      <p>Certains mots de deux syllabes s'écrivent pareil mais changent d'accent : le <b>nom</b> (et l'adjectif) est accentué sur le <b>préfixe</b> (/10/), le <b>verbe</b> sur la <b>base</b> (/01/).</p>
      <table>
        <tr><th>Nom /10/</th><th>Verbe /01/</th></tr>
        <tr><td>a ˈrecord (un disque, un record)</td><td>to reˈcord (enregistrer)</td></tr>
        <tr><td>a ˈpresent (un cadeau)</td><td>to preˈsent (présenter)</td></tr>
        <tr><td>an ˈobject (un objet)</td><td>to obˈject (s'opposer)</td></tr>
        <tr><td>an ˈincrease · an ˈexport · a ˈprotest · ˈproduce</td><td>to inˈcrease · to exˈport · to proˈtest · to proˈduce</td></tr>
      </table>
      <p>La voyelle du préfixe inaccentué se réduit souvent : <span class="ex">ˈrecord /ˈrekɔːd/ · reˈcord /rɪˈkɔːd/</span>.</p>''',
  {"nv": ("choice", "Où tombe l'accent dans cette phrase ?", [
      C(None, ["RE-cord", "re-CORD"], fr="She broke the world record.", big="record", keep=True, c=0, tip="nom → accent sur le préfixe /10/."),
      C(None, ["re-CORD", "RE-cord"], fr="I want to record a song.", big="record", keep=True, tip="verbe → accent sur la base /01/."),
      C(None, ["PRE-sent", "pre-SENT"], fr="Thank you for the present!", big="present", keep=True, tip="nom → /10/."),
      C(None, ["pre-SENT", "PRE-sent"], fr="She will present her project.", big="present", keep=True, tip="verbe → /01/."),
      C(None, ["OB-ject", "ob-JECT"], fr="What is this strange object?", big="object", keep=True, tip="nom → /10/."),
      C(None, ["ob-JECT", "OB-ject"], fr="I object to this decision.", big="object", keep=True, tip="verbe → /01/."),
      C(None, ["in-CREASE", "IN-crease"], fr="Prices will increase next year.", big="increase", keep=True, tip="verbe → /01/."),
      C(None, ["PRO-test", "pro-TEST"], fr="There was a big protest in the city.", big="protest", keep=True, tip="nom → /10/."),
    ]),
    "pref": ("choice", "Où tombe l'accent ?", [
      ST("begin", ["be", "gin"], 1, "préfixe inaccentué dans un verbe de 2 syllabes."), ST("decide", ["de", "cide"], 1, "préfixe inaccentué."), ST("explain", ["ex", "plain"], 1, "préfixe inaccentué."),
      ST("forget", ["for", "get"], 1, "préfixe inaccentué."), ST("prefer", ["pre", "fer"], 1, "préfixe inaccentué."), ST("remain", ["re", "main"], 1, "préfixe inaccentué."),
  ])},
  [M("nv", "🔁", "Nom ou verbe ?", "RE-cord / re-CORD selon la phrase.", ["nv"], 8),
   M("pref", "🔤", "Les préfixes inaccentués", "be-GIN, de-CIDE, ex-PLAIN…", ["pref"], 6),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["nv", "pref"], 12)], tag=EXP)

# ═════════════ EXPERT : MOTS COMPOSÉS ═════════════
newpage("composes_accent.html", "L'accent des mots composés – Expert", 'a <span>GREEN</span>house / a green <span>HOUSE</span>',
  "Noms composés, groupes nominaux, adjectifs composés et verbes à particule", ("#a5f3fc", "#0e7490"),
  '''      <table>
        <tr><th>Type</th><th>Accent</th><th>Exemples</th></tr>
        <tr><td><b>Nom composé</b></td><td>sur le <b>1er élément</b> (/1 0/)</td><td>a ˈgreenhouse (une serre) · a ˈblackboard · a ˈbedroom · ˈfootball · a ˈhot dog</td></tr>
        <tr><td><b>Adjectif + nom</b> (groupe libre)</td><td>sur le <b>nom</b></td><td>a green ˈhouse (une maison verte) · a black ˈboard (une planche noire)</td></tr>
        <tr><td><b>Adjectif composé</b></td><td>généralement sur le <b>2e élément</b></td><td>well-ˈknown · bad-ˈtempered · home-ˈmade</td></tr>
        <tr><td><b>Verbe à particule</b></td><td>sur la <b>particule</b></td><td>to get ˈup · to break ˈdown · to take ˈoff</td></tr>
        <tr><td><b>Nom tiré d'un verbe à particule</b></td><td>sur le <b>1er élément</b></td><td>a ˈbreakdown · ˈtakeoff · a ˈcheckout</td></tr>
      </table>''',
  {"cmp": ("choice", "Où tombe l'accent principal ?", [
      C(None, ["GREEN-house", "green HOUSE"], fr="We grow tomatoes in a greenhouse. (une serre)", big="greenhouse", keep=True, tip="nom composé → 1er élément."),
      C(None, ["green HOUSE", "GREEN-house"], fr="They live in a green house. (une maison peinte en vert)", big="green house", keep=True, tip="adjectif + nom → sur le nom."),
      C(None, ["BLACK-board", "black BOARD"], fr="The teacher wrote on the blackboard.", big="blackboard", keep=True, tip="nom composé → 1er élément."),
      C(None, ["BED-room", "bed ROOM"], big="bedroom", keep=True, tip="nom composé → 1er élément."),
      C(None, ["well-KNOWN", "WELL-known"], fr="She's a well-known singer.", big="well-known", keep=True, tip="adjectif composé → 2e élément."),
      C(None, ["get UP", "GET up"], fr="I get up at seven.", big="get up", keep=True, tip="verbe à particule → particule."),
      C(None, ["BREAK-down", "break-DOWN"], fr="The car had a breakdown.", big="breakdown", keep=True, tip="nom tiré d'un verbe à particule → 1er élément."),
      C(None, ["break DOWN", "BREAK down"], fr="My car might break down.", big="break down", keep=True, tip="verbe à particule → particule."),
      C(None, ["home-MADE", "HOME-made"], fr="This cake is home-made.", big="home-made", keep=True, tip="adjectif composé → 2e élément."),
      C(None, ["FOOT-ball", "foot-BALL"], big="football", keep=True, tip="nom composé → 1er élément."),
  ])},
  [M("cmp", "🧱", "Où tombe l'accent ?", "Nom composé, groupe nominal ou verbe à particule ?", ["cmp"])], tag=EXP)

# ═════════════ EXPERT : TRANSCRIPTION ═════════════
newpage("transcription_api.html", "La transcription phonétique – Expert", '/ˈtrænskrɪpʃn/',
  "Lire et choisir la bonne transcription en API", ("#e0e7ff", "#4338ca"),
  '''      <p>Pour transcrire un mot en API (anglais britannique standard), on note chaque <b>phonème</b>, l'<b>accent</b> (ˈ avant la syllabe accentuée) et la <b>longueur</b> des voyelles (ː).</p>
      <p><b>Pièges fréquents :</b></p>
      <p>• les voyelles <b>inaccentuées</b> se réduisent souvent en /ə/ : <i>banana /bəˈnɑːnə/, teacher /ˈtiːtʃə/</i> ;</p>
      <p>• le <b>r</b> final ne se prononce pas en anglais britannique devant une consonne : <i>car /kɑː/, teacher /ˈtiːtʃə/</i> ;</p>
      <p>• les <b>lettres muettes</b> ne se transcrivent pas : <i>knife /naɪf/, write /raɪt/</i> ;</p>
      <p>• les <b>diphtongues</b> s'écrivent avec deux symboles : <i>go /ɡəʊ/, make /meɪk/</i>.</p>''',
  {"w2t": ("choice", "Choisis la bonne transcription", [
      C(None, ["/ˈtiːtʃə/", "/ˈteɪtʃər/", "/tiːˈtʃə/"], big="teacher", say="teacher"), C(None, ["/ˈwɔːtə/", "/ˈwɒtər/", "/wɔːˈtə/"], big="water", say="water"),
      C(None, ["/haʊs/", "/hɔːs/", "/hoʊz/"], big="house", say="house"), C(None, ["/naɪf/", "/knaɪf/", "/nɪf/"], big="knife", say="knife"),
      C(None, ["/bəˈnɑːnə/", "/ˈbænænə/", "/bəˈnænə/"], big="banana", say="banana"), C(None, ["/kəmˈpjuːtə/", "/ˈkɒmpjuːtə/", "/kəmˈpuːtər/"], big="computer", say="computer"),
      C(None, ["/ɪˈnʌf/", "/ˈenɒf/", "/ɪˈnəʊ/"], big="enough", say="enough"), C(None, ["/ˈmeʒə/", "/ˈmeʃə/", "/ˈmiːʒər/"], big="measure", say="measure"),
      C(None, ["/wɜːk/", "/wɔːk/", "/wʊrk/"], big="work", say="work"), C(None, ["/ˈbjuːtɪfl/", "/ˈbeʊtɪfʊl/", "/bjuːˈtɪfl/"], big="beautiful", say="beautiful"),
      C(None, ["/ðəʊ/", "/θruː/", "/ðaʊ/"], big="though", say="though"), C(None, ["/ˈfəʊtəɡrɑːf/", "/fəˈtɒɡrɑːf/", "/ˈfɒtəɡræf/"], big="photograph", say="photograph"),
    ]),
    "t2w": ("choice", "Quel mot est transcrit ?", [
      C(None, ["chair", "share", "cheer"], big="/tʃeə/", say="chair"), C(None, ["boy", "buy", "bay"], big="/bɔɪ/", say="boy"), C(None, ["make", "mike", "milk"], big="/meɪk/", say="make"),
      C(None, ["through", "though", "throw"], big="/θruː/", say="through"), C(None, ["bought", "boat", "but"], big="/bɔːt/", say="bought"), C(None, ["here", "hair", "hire"], big="/hɪə/", say="here"),
      C(None, ["English", "angels", "England"], big="/ˈɪŋɡlɪʃ/", say="English"), C(None, ["friendly", "frankly", "freely"], big="/ˈfrendli/", say="friendly"),
  ])},
  [M("w2t", "✍️", "Mot → transcription", "Choisis la bonne transcription API.", ["w2t"], 12),
   M("t2w", "📖", "Transcription → mot", "Retrouve le mot transcrit.", ["t2w"], 8),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["w2t", "t2w"], 12)], tag=EXP)

# ═════════════ EXPERT : RÉDUCTION VOCALIQUE ═════════════
newpage("reduction_vocalique.html", "Réduction vocalique et alternances – Expert", 'ˈphotograph / pho<span>ˈto</span>graphy',
  "Le schwa, les voyelles réduites et les alternances accentuelles", ("#fde68a", "#92400e"),
  '''      <p>En anglais, les voyelles des syllabes <b>inaccentuées</b> se <b>réduisent</b>, le plus souvent en <span class="hl">/ə/</span> (schwa), parfois en /ɪ/. Quand l'accent se déplace dans une famille de mots, la qualité des voyelles change :</p>
      <table>
        <tr><th>Mot</th><th>Transcription</th><th>Schéma</th></tr>
        <tr><td>photograph</td><td>/ˈfəʊtəɡrɑːf/</td><td>/102/ ou /100/</td></tr>
        <tr><td>photography</td><td>/fəˈtɒɡrəfi/</td><td>/0100/</td></tr>
        <tr><td>photographic</td><td>/ˌfəʊtəˈɡræfɪk/</td><td>/2010/</td></tr>
        <tr><td>Canada · Canadian</td><td>/ˈkænədə/ · /kəˈneɪdiən/</td><td>/100/ · /0100/</td></tr>
        <tr><td>politics · political</td><td>/ˈpɒlətɪks/ · /pəˈlɪtɪkl/</td><td>/100/ · /0100/</td></tr>
      </table>
      <p>La voyelle <b>pleine</b> (/æ/, /ɒ/, /eɪ/…) apparaît sous l'accent ; la même lettre devient /ə/ quand elle n'est plus accentuée.</p>''',
  {"red": ("choice", "Choisis la bonne réponse", [
      C(None, ["/ə/", "/æ/", "/ɑː/"], fr="Dans banana /bəˈnɑːnə/, comment se prononce le premier a (inaccentué) ?", tip="syllabe inaccentuée → schwa."),
      C(None, ["/fəˈtɒɡrəfi/", "/ˈfəʊtɒɡrəfi/", "/fəʊˈtəɡræfi/"], fr="Quelle est la transcription de photography ?", say="photography", tip="accent sur -TO- : /ɒ/ pleine, les autres réduites."),
      C(None, ["/kəˈneɪdiən/", "/ˈkænədiən/", "/kæˈnædiən/"], fr="Quelle est la transcription de Canadian ?", say="Canadian", tip="accent sur -NA- : /eɪ/ ; le premier a se réduit."),
      C(None, ["/pəˈlɪtɪkl/", "/ˈpɒlɪtɪkl/", "/pɒˈlətɪkl/"], fr="Quelle est la transcription de political ?", say="political", tip="-ical contraignant : accent sur LI, le o se réduit."),
      C(None, ["la 2e", "la 1re", "la 3e"], fr="Dans photographic /ˌfəʊtəˈɡræfɪk/, quelle syllabe a une voyelle réduite ?", tip="pho (2) · to /tə/ (0, réduite) · GRA (1) · phic /ɪ/ (0)."),
      C(None, ["/ɪ/ ou /ə/ : rɪˈkɔːd", "/e/ : reˈkɔːd", "/iː/ : riːˈkɔːd"], fr="Le verbe to record (/01/) : comment se prononce re- ?", say="to record", tip="préfixe inaccentué → voyelle réduite."),
  ])},
  [M("red", "🔻", "Voyelles réduites", "Le schwa et les alternances accentuelles.", ["red"], 6)], tag=EXP)

# ═════════════ PROSODIE : RYTHME ═════════════
PRO = "Anglais · Expert · Prosodie"
newpage("rythme_anglais.html", "Le rythme de l'anglais – Prosodie", 'Le <span>rythme</span> de l\'anglais',
  "Une langue accentuelle (stress-timed)", ("#fca5a5", "#9f1239"),
  '''      <p>Le français est une langue <b>syllabique</b> : chaque syllabe dure à peu près le même temps. L'anglais est une langue <span class="hl">accentuelle</span> (<i>stress-timed</i>) : ce sont les <b>syllabes accentuées</b> qui reviennent à intervalles réguliers, et les syllabes inaccentuées entre elles sont <b>compressées</b>.</p>
      <p class="ex">CATS · CHASE · MICE <br>The CATS · will CHASE · the MICE <br>The CATS · will have CHASED · the MICE</p>
      <p>Ces trois phrases ont <b>3 accents</b> : elles durent à peu près le même temps, malgré un nombre de syllabes différent.</p>
      <p>Pour bien parler anglais : appuie sur les mots pleins, et « avale » les mots outils (formes faibles, schwa).</p>''',
  {"count": ("choice", "Combien d'accents dans cette phrase ?", [
      C(None, ["3", "5", "7"], big="The cats will chase the mice.", say="The cats will chase the mice.", keep=True, tip="CATS, CHASE, MICE."),
      C(None, ["2", "4", "5"], big="Where do you live?", say="Where do you live?", keep=True, tip="WHERE, LIVE."),
      C(None, ["4", "3", "6"], big="I want to buy a new car.", say="I want to buy a new car.", keep=True, tip="WANT, BUY, NEW, CAR."),
      C(None, ["3", "2", "6"], big="She's reading a book in the garden.", say="She's reading a book in the garden.", keep=True, tip="READ-, BOOK, GAR-."),
      C(None, ["3", "4", "8"], big="It's the best film of the year.", say="It's the best film of the year.", keep=True, tip="BEST, FILM, YEAR."),
    ]),
    "time": ("choice", "Laquelle de ces phrases dure à peu près le même temps que « DOGS BARK LOUDLY » ?", [
      C(None, ["The dogs are barking loudly.", "Dogs.", "The dogs are barking very loudly at the cats in the garden."], tip="même nombre d'accents (DOGS, BARK, LOUD-) → même durée approximative."),
      C(None, ["My friend has bought a car.", "A car.", "My best friend has just bought a brand new red car."], fr="Et pour « FRIEND BOUGHT CAR » ?", tip="3 accents : FRIEND, BOUGHT, CAR."),
  ])},
  [M("count", "🥁", "Compter les accents", "Combien de temps forts ?", ["count"], 5),
   M("time", "⏱️", "Même durée ?", "Les accents donnent le rythme.", ["time"], 2),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["count", "time"], 7)], tag=PRO)

# ═════════════ PROSODIE : MÈTRE ═════════════
FEET = ["iambe (da-DUM)", "trochée (DUM-da)", "anapeste (da-da-DUM)", "dactyle (DUM-da-da)", "spondée (DUM-DUM)"]
def FT(word, k, tip): return C(None, FEET[:4] if k < 4 else FEET, big=word, say=word, c=k, keep=True, tip=tip)
METRES = ["dimètre (2)", "trimètre (3)", "tétramètre (4)", "pentamètre (5)", "hexamètre (6)"]
newpage("metre_poetique.html", "Le mètre poétique – Prosodie", 'iambic <span>pentameter</span>',
  "Pieds, mètres et scansion de la poésie anglaise", ("#fde68a", "#b45309"),
  '''      <p>La poésie anglaise traditionnelle repose sur l'alternance de syllabes <b>accentuées</b> (DUM) et <b>inaccentuées</b> (da). Un motif répété s'appelle un <span class="hl">pied</span> (<i>foot</i>).</p>
      <table>
        <tr><th>Pied</th><th>Motif</th><th>Exemple</th></tr>
        <tr><td><b>iambe</b> (iamb)</td><td>da-DUM (/01/)</td><td>a-BOUT, to-DAY</td></tr>
        <tr><td><b>trochée</b> (trochee)</td><td>DUM-da (/10/)</td><td>GAR-den, HAP-py</td></tr>
        <tr><td><b>anapeste</b> (anapest)</td><td>da-da-DUM (/001/)</td><td>un-der-STAND, in-ter-RUPT</td></tr>
        <tr><td><b>dactyle</b> (dactyl)</td><td>DUM-da-da (/100/)</td><td>BEAU-ti-ful, HOL-i-day</td></tr>
        <tr><td><b>spondée</b> (spondee)</td><td>DUM-DUM (/11/)</td><td>HEART-BREAK</td></tr>
      </table>
      <p>Le <b>mètre</b> indique le nombre de pieds par vers : dimètre (2), trimètre (3), tétramètre (4), <b>pentamètre (5)</b>, hexamètre (6).</p>
      <p>Le <span class="hl">pentamètre iambique</span> (5 iambes, 10 syllabes) est le vers de Shakespeare :</p>
      <p class="ex">shall I | com-PARE | thee TO | a SUM | mer's DAY ? → da-DUM × 5 (Sonnet 18, 1609)</p>
      <p>Autres exemples du domaine public : <i>TY-ger TY-ger, BURN-ing BRIGHT</i> (Blake, 1794 : tétramètre trochaïque) · <i>'twas the NIGHT be-fore CHRIST-mas</i> (1823 : anapestes).</p>''',
  {"foot": ("choice", "Quel pied correspond à ce mot ?", [
      FT("today", 0, "to-DAY : da-DUM."), FT("about", 0, "a-BOUT : da-DUM."), FT("begin", 0, "be-GIN : da-DUM."),
      FT("garden", 1, "GAR-den : DUM-da."), FT("happy", 1, "HAP-py : DUM-da."), FT("sister", 1, "SIS-ter : DUM-da."),
      FT("understand", 2, "un-der-STAND : da-da-DUM."), FT("interrupt", 2, "in-ter-RUPT : da-da-DUM."),
      FT("beautiful", 3, "BEAU-ti-ful : DUM-da-da."), FT("holiday", 3, "HOL-i-day : DUM-da-da."), FT("heartbreak", 4, "HEART-BREAK : DUM-DUM."),
    ]),
    "line": ("choice", "Analyse le vers", [
      C(None, ["pentamètre iambique", "tétramètre trochaïque", "hexamètre dactylique"], big="Shall I compare thee to a summer's day?", say="Shall I compare thee to a summer's day?", tip="Shakespeare, Sonnet 18 : 5 × da-DUM."),
      C(None, ["tétramètre trochaïque", "pentamètre iambique", "trimètre anapestique"], big="Tyger Tyger, burning bright", say="Tyger Tyger, burning bright", tip="Blake : TY-ger | TY-ger | BURN-ing | BRIGHT → 4 trochées (le dernier incomplet)."),
      C(None, ["5", "4", "10"], fr="Combien de pieds dans un pentamètre ?", tip="penta = 5."), C(None, ["10", "5", "12"], fr="Combien de syllabes dans un pentamètre iambique régulier ?", tip="5 pieds × 2 syllabes = 10."),
      C(None, ["da-DUM", "DUM-da", "da-da-DUM"], fr="Quel est le motif d'un iambe ?", tip="iambe = inaccentuée + accentuée."),
      C(None, ["tétramètre", "trimètre", "pentamètre"], fr="Un vers de 4 pieds est un…", tip="tetra = 4."),
  ])},
  [M("foot", "🦶", "Les pieds", "iambe, trochée, anapeste, dactyle, spondée.", ["foot"], 11),
   M("line", "📜", "Scander un vers", "pentamètre iambique, tétramètre trochaïque…", ["line"], 6),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["foot", "line"], 12)], tag=PRO)

# ═════════════ PROSODIE : RIMES ET FIGURES SONORES ═════════════
newpage("rimes_figures.html", "Rimes et figures sonores – Prosodie", 'Rhyme, <span>rhythm</span> & sound',
  "Schémas de rimes, formes poétiques et figures sonores", ("#bfdbfe", "#1e40af"),
  '''      <h4>Les schémas de rimes</h4>
      <p>On note chaque son de rime par une lettre : les vers qui riment ensemble ont la même lettre.</p>
      <table>
        <tr><th>Schéma</th><th>Nom</th></tr>
        <tr><td>AABB</td><td>rimes suivies (<i>couplets</i>)</td></tr>
        <tr><td>ABAB</td><td>rimes croisées (<i>alternate rhyme</i>)</td></tr>
        <tr><td>ABBA</td><td>rimes embrassées (<i>enclosed rhyme</i>)</td></tr>
      </table>
      <h4>Les formes poétiques</h4>
      <p><b>Sonnet shakespearien</b> : 14 vers en pentamètre iambique, ABAB CDCD EFEF GG (3 quatrains + 1 distique final) · <b>Sonnet pétrarquien</b> : ABBAABBA + CDECDE · <b>Limerick</b> : 5 vers humoristiques, AABBA · <b>Haïku</b> : 3 vers de 5-7-5 syllabes, sans rime.</p>
      <h4>Les figures sonores</h4>
      <p><b>Allitération</b> : répétition d'une consonne initiale (<i>Big brown bears bounce</i>) · <b>Assonance</b> : répétition d'un son voyelle (<i>the rain in Spain stays mainly</i>) · <b>Onomatopée</b> : mot qui imite un son (<i>buzz, bang, splash</i>) · <b>Rime intérieure</b> : rime à l'intérieur du vers · <b>Enjambement</b> : la phrase continue sur le vers suivant.</p>''',
  {"scheme": ("choice", "Quel est le schéma de rimes ?", [
      C(None, ["AABB", "ABAB", "ABBA"], fr="…night / …light / …day / …play", keep=True, tip="night-light (A), day-play (B) → AABB."),
      C(None, ["ABAB", "AABB", "ABBA"], fr="…tree / …sun / …sea / …fun", keep=True, tip="tree-sea (A), sun-fun (B) → ABAB."),
      C(None, ["ABBA", "ABAB", "AABB"], fr="…cat / …moon / …June / …hat", keep=True, tip="cat-hat (A), moon-June (B) → ABBA."),
      C(None, ["AABBA", "ABABA", "AAAAA"], fr="Quel est le schéma d'un limerick ?", keep=True, tip="limerick : AABBA."),
      C(None, ["14", "12", "10"], fr="Combien de vers dans un sonnet ?", keep=True, tip="un sonnet = 14 vers."),
      C(None, ["ABAB CDCD EFEF GG", "ABBA ABBA CDE CDE", "AABB CCDD EEFF GG"], fr="Quel est le schéma du sonnet shakespearien ?", tip="3 quatrains à rimes croisées + un distique."),
      C(None, ["5-7-5", "7-5-7", "5-5-5"], fr="Combien de syllabes dans les 3 vers d'un haïku ?", tip="haïku : 5-7-5."),
    ]),
    "fig": ("choice", "Quelle figure sonore ?", [
      C(None, ["allitération", "assonance", "onomatopée"], big="Big brown bears bounce on blue balloons.", say="Big brown bears bounce on blue balloons.", tip="répétition du son /b/ initial."),
      C(None, ["onomatopée", "allitération", "assonance"], big="Buzz! Bang! Splash!", say="Buzz! Bang! Splash!", tip="des mots qui imitent des sons."),
      C(None, ["assonance", "allitération", "onomatopée"], big="The rain in Spain stays mainly in the plain.", say="The rain in Spain stays mainly in the plain.", tip="répétition du son voyelle /eɪ/."),
      C(None, ["allitération", "rime intérieure", "enjambement"], big="Silly snakes slide slowly south.", say="Silly snakes slide slowly south.", tip="répétition du son /s/ initial."),
      C(None, ["rime intérieure", "assonance", "onomatopée"], big="I bring fresh showers for the thirsting flowers.", say="I bring fresh showers for the thirsting flowers.", tip="showers / flowers riment dans le même vers (Shelley, 1820)."),
      C(None, ["onomatopée", "assonance", "enjambement"], big="The clock went tick-tock, the dog went woof.", say="The clock went tick-tock, the dog went woof.", tip="tick-tock, woof imitent des sons."),
  ])},
  [M("scheme", "🎼", "Rimes et formes", "AABB, ABAB, sonnet, limerick, haïku.", ["scheme"], 7),
   M("fig", "🎨", "Les figures sonores", "allitération, assonance, onomatopée…", ["fig"], 6),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["scheme", "fig"], 12)], tag=PRO)
print("content15 ok", REGISTRY)
