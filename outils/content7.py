import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
exec(open(_EA_OUT+"/content_helpers.py", encoding="utf-8").read())

def P(word, ok, opts, tip):  # mot à écouter + choix du son
    return C(None, opts, big=word, say=word, c=opts.index(ok), keep=True, tip=tip)

# ═════════════ -ED ═════════════
ED_T, ED_D, ED_ID = "/t/", "/d/", "/ɪd/"
ED = [ED_T, ED_D, ED_ID]
RT = "Après un son sourd (p, k, s, sh, ch, f) → <b>/t/</b>."
RD = "Après un son sonore (voyelle, b, g, l, m, n, v, z…) → <b>/d/</b>."
RI = "Après <b>t</b> ou <b>d</b> → <b>/ɪd/</b> (on entend une syllabe en plus)."
newpage("phono_ed.html", "Prononcer le -ED – Entraînement", 'Prononcer le <span>-ED</span>',
  "/t/ · /d/ · /ɪd/", ("#fca5a5", "#f87171"),
  '''      <p>Le <span class="hl">-ed</span> du prétérit se prononce de <b>trois façons</b> selon le dernier son du verbe.</p>
      <table>
        <tr><th>Son</th><th>Quand ?</th><th>Exemples</th></tr>
        <tr><td><span class="hl">/ɪd/</span></td><td>après <b>t</b> ou <b>d</b> (syllabe en plus)</td><td>wanted, needed, started, visited</td></tr>
        <tr><td><span class="hl">/t/</span></td><td>après un son sourd : p, k, s, sh, ch, f</td><td>stopped, worked, kissed, washed, watched, laughed</td></tr>
        <tr><td><span class="hl">/d/</span></td><td>après les autres sons (voyelles, l, m, n, v, z…)</td><td>played, lived, cleaned, called, opened</td></tr>
      </table>
      <p>Astuce : on ne prononce <b>jamais</b> « é-d » comme en français, sauf pour /ɪd/. Utilise le bouton 🔊 pour écouter chaque mot.</p>''',
  {"ed": ("choice", "Écoute : comment se prononce le -ed ?", [
      P("worked", ED_T, ED, RT), P("watched", ED_T, ED, RT), P("helped", ED_T, ED, RT), P("laughed", ED_T, ED, RT), P("kissed", ED_T, ED, RT),
      P("stopped", ED_T, ED, RT), P("washed", ED_T, ED, RT), P("cooked", ED_T, ED, RT),
      P("played", ED_D, ED, RD), P("lived", ED_D, ED, RD), P("cleaned", ED_D, ED, RD), P("opened", ED_D, ED, RD), P("called", ED_D, ED, RD),
      P("loved", ED_D, ED, RD), P("cried", ED_D, ED, RD), P("travelled", ED_D, ED, RD),
      P("wanted", ED_ID, ED, RI), P("needed", ED_ID, ED, RI), P("started", ED_ID, ED, RI), P("visited", ED_ID, ED, RI),
      P("decided", ED_ID, ED, RI), P("painted", ED_ID, ED, RI), P("waited", ED_ID, ED, RI), P("ended", ED_ID, ED, RI),
  ]),
  "intrus": ("choice", "Quel mot n'a pas le même son -ed que les autres ?", [
      C(None, ["wanted", "worked", "watched", "helped"], tip="wanted → /ɪd/ ; les autres → /t/."), C(None, ["played", "needed", "started", "visited"], tip="played → /d/ ; les autres → /ɪd/."),
      C(None, ["cooked", "lived", "cleaned", "opened"], tip="cooked → /t/ ; les autres → /d/."), C(None, ["decided", "stopped", "kissed", "washed"], tip="decided → /ɪd/ ; les autres → /t/."),
      C(None, ["loved", "laughed", "helped", "watched"], tip="loved → /d/ ; les autres → /t/."),
  ])},
  [M("ed", "🔊", "/t/, /d/ ou /ɪd/ ?", "Écoute et classe chaque verbe.", ["ed"], 12),
   M("intrus", "🕵️", "Trouve l'intrus", "Lequel ne se prononce pas pareil ?", ["intrus"], 5),
   M("mix", "🎲", "Tout mélangé", "Le grand test !", ["ed", "intrus"], 12)], tag="Anglais · Phonologie")

# ═════════════ -S ═════════════
S_S, S_Z, S_IZ = "/s/", "/z/", "/ɪz/"
SS = [S_S, S_Z, S_IZ]
R1 = "Après un son sourd (p, t, k, f) → <b>/s/</b>."
R2 = "Après un son sonore (voyelle, b, d, g, l, m, n, v…) → <b>/z/</b>."
R3 = "Après s, z, sh, ch, ge, x → <b>/ɪz/</b> (on entend une syllabe en plus)."
newpage("phono_s.html", "Prononcer le -S – Entraînement", 'Prononcer le <span>-S</span>',
  "/s/ · /z/ · /ɪz/ — pluriels et 3e personne", ("#fdba74", "#fb923c"),
  '''      <p>Le <span class="hl">-s</span> du pluriel (cats) et de la 3e personne du présent (she works) se prononce de <b>trois façons</b>.</p>
      <table>
        <tr><th>Son</th><th>Quand ?</th><th>Exemples</th></tr>
        <tr><td><span class="hl">/s/</span></td><td>après un son sourd : p, t, k, f</td><td>cats, books, stops, works, laughs</td></tr>
        <tr><td><span class="hl">/z/</span></td><td>après un son sonore : voyelles, b, d, g, l, m, n, v…</td><td>dogs, plays, lives, bags, goes, calls</td></tr>
        <tr><td><span class="hl">/ɪz/</span></td><td>après s, z, sh, ch, ge, x (syllabe en plus)</td><td>buses, watches, washes, boxes, pages</td></tr>
      </table>''',
  {"s": ("choice", "Écoute : comment se prononce le -s ?", [
      P("cats", S_S, SS, R1), P("books", S_S, SS, R1), P("works", S_S, SS, R1), P("stops", S_S, SS, R1), P("eats", S_S, SS, R1), P("laughs", S_S, SS, R1),
      P("dogs", S_Z, SS, R2), P("plays", S_Z, SS, R2), P("lives", S_Z, SS, R2), P("bags", S_Z, SS, R2), P("goes", S_Z, SS, R2), P("reads", S_Z, SS, R2), P("calls", S_Z, SS, R2),
      P("watches", S_IZ, SS, R3), P("buses", S_IZ, SS, R3), P("washes", S_IZ, SS, R3), P("boxes", S_IZ, SS, R3), P("kisses", S_IZ, SS, R3), P("pages", S_IZ, SS, R3), P("oranges", S_IZ, SS, R3),
  ])},
  [M("s", "🔊", "/s/, /z/ ou /ɪz/ ?", "Écoute et classe chaque mot.", ["s"], 12)], tag="Anglais · Phonologie")

# ═════════════ ACCENT DE MOT ═════════════
def stress(word, syl, k):
    opts = ["-".join(s.upper() if i == j else s for i, s in enumerate(syl)) for j in range(len(syl))][:3]
    ok = opts[k]
    return C(None, opts, big=word, say=word, c=k, keep=True, tip=f"On accentue la syllabe <b>{syl[k].upper()}</b> : {ok}.")
newpage("accent_mot.html", "L'accent de mot – Entraînement", "L'<span>accent</span> de mot",
  "Quelle syllabe est accentuée ?", ("#c4b5fd", "#a78bfa"),
  '''      <p>En anglais, dans un mot de plusieurs syllabes, une syllabe est <b>plus forte</b> que les autres : c'est l'<span class="hl">accent tonique</span>. On la prononce plus fort, plus longue et plus haut.</p>
      <p class="ex">TEA-cher · ho-TEL · com-PU-ter · BEAU-ti-ful</p>
      <p>Quelques tendances :</p>
      <p>• La plupart des noms et adjectifs de 2 syllabes sont accentués sur la <b>1re</b> : <i>TEA-cher, HAP-py, PIZ-za</i>.</p>
      <p>• La plupart des verbes de 2 syllabes sont accentués sur la <b>2e</b> : <i>de-CIDE, be-GIN, re-PEAT</i>.</p>
      <p>• Les mots en <b>-tion</b>, <b>-ic</b> sont accentués juste avant : <i>in-for-MA-tion, fan-TAS-tic</i>.</p>
      <p>Utilise le bouton 🔊 pour écouter chaque mot, puis répète-le à voix haute !</p>''',
  {"st": ("choice", "Écoute : quelle syllabe est accentuée ?", [
      stress("teacher", ["tea", "cher"], 0), stress("hotel", ["ho", "tel"], 1), stress("computer", ["com", "pu", "ter"], 1), stress("banana", ["ba", "na", "na"], 1),
      stress("important", ["im", "por", "tant"], 1), stress("photograph", ["pho", "to", "graph"], 0), stress("family", ["fa", "mi", "ly"], 0), stress("holiday", ["ho", "li", "day"], 0),
      stress("tomorrow", ["to", "mor", "row"], 1), stress("decide", ["de", "cide"], 1), stress("Japanese", ["Ja", "pa", "nese"], 2), stress("chocolate", ["cho", "co", "late"], 0),
      stress("breakfast", ["break", "fast"], 0), stress("police", ["po", "lice"], 1), stress("begin", ["be", "gin"], 1), stress("hospital", ["hos", "pi", "tal"], 0),
      stress("information", ["in", "for", "ma", "tion"], 2), stress("fantastic", ["fan", "tas", "tic"], 1), stress("engineer", ["en", "gi", "neer"], 2), stress("pizza", ["piz", "za"], 0),
  ])},
  [M("st", "🔊", "Quelle syllabe est accentuée ?", "Écoute, choisis et répète !", ["st"], 12)], tag="Anglais · Phonologie")

# ═════════════ LETTRES MUETTES ═════════════
def silent(word, letter, others, tip):
    return C(None, [letter] + others, big=word, say=word, keep=True, tip=tip)
newpage("lettres_muettes.html", "Les lettres muettes – Entraînement", 'Les lettres <span>muettes</span>',
  "knife, write, hour, island…", ("#86efac", "#4ade80"),
  '''      <p>En anglais, certaines lettres s'écrivent mais <b>ne se prononcent pas</b> : ce sont les <span class="hl">lettres muettes</span>.</p>
      <table>
        <tr><th>Lettre</th><th>Quand ?</th><th>Exemples</th></tr>
        <tr><td><b>k</b></td><td>devant n en début de mot</td><td>knife, know, knee</td></tr>
        <tr><td><b>w</b></td><td>devant r en début de mot</td><td>write, wrong, wrist</td></tr>
        <tr><td><b>h</b></td><td>dans quelques mots</td><td>hour, honest, what</td></tr>
        <tr><td><b>b</b></td><td>après m en fin de mot</td><td>lamb, climb, comb</td></tr>
        <tr><td><b>l</b></td><td>dans -alk, -alf, -ould</td><td>talk, walk, half, could</td></tr>
        <tr><td><b>t</b></td><td>dans -sten, -stle</td><td>listen, castle</td></tr>
        <tr><td><b>s, d</b></td><td>quelques mots</td><td>island, Wednesday</td></tr>
      </table>''',
  {"mute": ("choice", "Écoute : quelle lettre est muette ?", [
      silent("knife", "k", ["n", "f"], "k muet devant n."), silent("write", "w", ["r", "t"], "w muet devant r."), silent("hour", "h", ["r", "u"], "h muet dans hour."),
      silent("island", "s", ["l", "d"], "s muet dans island."), silent("listen", "t", ["s", "n"], "t muet dans -sten."), silent("lamb", "b", ["m", "l"], "b muet après m."),
      silent("talk", "l", ["k", "t"], "l muet dans -alk."), silent("Wednesday", "d", ["n", "s"], "le premier d de Wednesday est muet."), silent("honest", "h", ["t", "n"], "h muet dans honest."),
      silent("know", "k", ["w", "n"], "k muet devant n."), silent("wrong", "w", ["g", "r"], "w muet devant r."), silent("half", "l", ["f", "h"], "l muet dans -alf."),
      silent("castle", "t", ["s", "l"], "t muet dans -stle."), silent("climb", "b", ["m", "c"], "b muet après m."), silent("could", "l", ["d", "c"], "l muet dans -ould."),
  ])},
  [M("mute", "🔇", "Quelle lettre est muette ?", "Écoute le mot et trouve la lettre qu'on n'entend pas.", ["mute"], 12)], tag="Anglais · Phonologie")
print("content7 ok", REGISTRY)
