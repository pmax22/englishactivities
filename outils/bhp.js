/* Be / Have / Play au présent simple : affirmatif, négatif, interrogatif */
// [sujet, personne : i | s3 | pl]
const SUBJECTS = [["I","i"],["You","pl"],["He","s3"],["She","s3"],["We","pl"],["They","pl"],["Tom","s3"],["My sister","s3"],["My parents","pl"],["The children","pl"],["Emma","s3"],["My friends","pl"]];
const COMPS = {
  be: ["happy", "tired", "at school", "in the garden", "at home", "late", "hungry", "French"],
  have: ["a dog", "two brothers", "a new bike", "blue eyes", "a big house", "a cat", "a computer"],
  play: ["football", "the piano", "video games", "tennis", "the guitar", "basketball", "cards"]
};
const VERB_FR = { be: "être", have: "avoir", play: "jouer" };
const FORM_LABEL = { aff: "affirmative", neg: "négative", inter: "interrogative" };
function mid(s) { return /^(My|The)\b/.test(s) ? s.charAt(0).toLowerCase() + s.slice(1) : s; }

function conj(S, p, v, c, form) {
  const s3 = p === "s3";
  if (v === "be") {
    const be = p === "i" ? "am" : s3 ? "is" : "are";
    if (form === "aff") return `${S} ${be} ${c}.`;
    if (form === "neg") return `${S} ${p === "i" ? "am not" : s3 ? "isn't" : "aren't"} ${c}.`;
    return `${capF(be)} ${mid(S)} ${c}?`;
  }
  const aff = v === "have" ? (s3 ? "has" : "have") : (s3 ? "plays" : "play");
  if (form === "aff") return `${S} ${aff} ${c}.`;
  if (form === "neg") return `${S} ${s3 ? "doesn't" : "don't"} ${v} ${c}.`;
  return `${s3 ? "Does" : "Do"} ${mid(S)} ${v} ${c}?`;
}
function rand() {
  const v = pick(["be", "have", "play"]);
  const [S, p] = pick(SUBJECTS);
  return { v, S, p, c: pick(COMPS[v]) };
}
function rule(v, form, p) {
  const s3 = p === "s3";
  if (v === "be") return form === "aff" ? "Be : I <b>am</b> · he/she/it <b>is</b> · you/we/they <b>are</b>."
    : form === "neg" ? "Be : on ajoute simplement <b>not</b> → am not, <b>isn't</b>, <b>aren't</b>. Pas de don't !"
    : "Be : on inverse le sujet et le verbe → <b>Am</b> I…? <b>Is</b> he…? <b>Are</b> they…? Pas de do !";
  if (form === "aff") return v === "have" ? "Have : he/she/it <b>has</b>, les autres <b>have</b>." : "Play : he/she/it + <b>-s</b> → plays.";
  if (form === "neg") return `${capF(v)} : <b>${s3 ? "doesn't" : "don't"}</b> + base verbale (${v})${s3 ? " — pas de -s après doesn't !" : ""}.`;
  return `${capF(v)} : <b>${s3 ? "Does" : "Do"}</b> + sujet + base verbale (${v}) ?`;
}

function conjQuestion() {
  const { v, S, p, c } = rand();
  const ans = conj(S, p, v, c, "aff").replace(S + " ", "").replace(" " + c + ".", "");
  return {
    kind: "gap", instr: "Conjugue le verbe à la forme affirmative", label: `${S} … ${c} (${v})`, sign: "plus",
    parts: [S + " ", { answers: [ans], width: 110, hint: v }, " " + c + "."], correct: conj(S, p, v, c, "aff"), tip: rule(v, "aff", p)
  };
}
function transformQuestion(target, from) {
  const { v, S, p, c } = rand();
  from = from || "aff";
  const src = conj(S, p, v, c, from), ok = conj(S, p, v, c, target);
  /* L'élève n'écrit que la partie qui change : le reste de la phrase est déjà donné. */
  const s3 = p === "s3", full = x => x.replace("n't", " not");
  let mid_, parts;
  if (v === "be") {
    const be = p === "i" ? "am" : s3 ? "is" : "are";
    mid_ = target === "aff" ? [be] : target === "neg" ? (p === "i" ? ["am not"] : [s3 ? "isn't" : "aren't", be + " not"]) : [capF(be) + " " + mid(S)];
  } else {
    const aff = v === "have" ? (s3 ? "has" : "have") : (s3 ? "plays" : "play");
    const aux = s3 ? "doesn't" : "don't";
    mid_ = target === "aff" ? [aff] : target === "neg" ? [aux + " " + v, full(aux) + " " + v] : [(s3 ? "Does" : "Do") + " " + mid(S) + " " + v];
  }
  const w = Math.max(110, Math.min(260, mid_[0].length * 13 + 30));
  if (target === "inter") parts = [{ answers: mid_, width: w, ph: "…" }, " " + c + "?"];
  else parts = [S + " ", { answers: mid_, width: w, ph: "…" }, " " + c + "."];
  return {
    kind: "gap", instr: `Mets la phrase à la forme ${FORM_LABEL[target]}`, label: src, sign: target === "neg" ? "minus" : target === "inter" ? "q" : "plus",
    head: `<div class="fr-line">${esc(src)}</div>`,
    parts, correct: ok, tip: rule(v, target, p),
    diagnose(vals) {
      const t = " " + norm(vals[0]) + " ";
      if (v === "be" && / (do|does|don't|doesn't) /.test(t)) return "Avec <b>be</b>, on n'utilise jamais do / does : " + rule("be", target, p);
      if (v !== "be" && target !== "aff" && / (has|plays) /.test(t)) return `Après ${p === "s3" ? "does / doesn't" : "do / don't"}, le verbe reste en base verbale : <b>${v}</b>.`;
      if (v !== "be" && target !== "aff" && p === "s3" && / (do|don't) /.test(t)) return `Avec ${mid(S)} (he/she/it), on utilise <b>${target === "neg" ? "doesn't" : "Does"}</b>.`;
      return rule(v, target, p);
    }
  };
}
function choiceQuestion() {
  const { v, S, p, c } = rand();
  const form = pick(["aff", "neg", "inter"]), s3 = p === "s3";
  let line, opts, ok;
  if (v === "be") {
    if (form === "aff") { opts = ["am", "is", "are"]; ok = p === "i" ? "am" : s3 ? "is" : "are"; line = `${S} ____ ${c}.`; }
    else if (form === "neg") { opts = ["am not", "isn't", "aren't", "don't"]; ok = p === "i" ? "am not" : s3 ? "isn't" : "aren't"; line = `${S} ____ ${c}.`; }
    else { opts = ["Am", "Is", "Are", "Does"]; ok = p === "i" ? "Am" : s3 ? "Is" : "Are"; line = `____ ${mid(S)} ${c}?`; }
  } else {
    const V = v, Vs = v === "have" ? "has" : "plays";
    if (form === "aff") { opts = [V, Vs, "is " + V]; ok = s3 ? Vs : V; line = `${S} ____ ${c}.`; }
    else if (form === "neg") { opts = ["don't " + V, "doesn't " + V, "doesn't " + Vs]; ok = s3 ? "doesn't " + V : "don't " + V; line = `${S} ____ ${c}.`; }
    else { opts = ["Do", "Does", "Is"]; ok = s3 ? "Does" : "Do"; line = `____ ${mid(S)} ${V} ${c}?`; }
  }
  return {
    kind: "mcq", grid: opts.length === 4 ? 4 : 3, keepOrder: true, instr: `Choisis la bonne forme · ${FORM_LABEL[form]}`, label: line,
    head: `<div class="fr-line">${esc(line)}</div>`, options: opts, correct: opts.indexOf(ok),
    correctText: conj(S, p, v, c, form), tip: rule(v, form, p)
  };
}
function orderQuestion() {
  const { v, S, p, c } = rand();
  const form = pick(["aff", "neg", "inter"]);
  const sent = conj(S, p, v, c, form);
  const body = sent.replace(/[.?]$/, "").replace(" " + c, "");
  const tiles = body.split(" ").reduce((acc, w) => { if (/^(My|The|my|the)$/.test(acc[acc.length - 1])) acc[acc.length - 1] += " " + w; else acc.push(w); return acc; }, []);
  tiles.push(c);
  const s3 = p === "s3";
  const trap = v === "be" ? (form === "inter" || form === "aff" ? (s3 ? "are" : "is") : "don't")
    : form === "aff" ? (s3 ? v : (v === "have" ? "has" : "plays")) : form === "neg" ? (s3 ? "don't" : "doesn't") : (s3 ? "Do" : "Does");
  return {
    kind: "order", instr: `Remets les mots dans l'ordre · forme ${FORM_LABEL[form]}`, label: sent, sign: form === "neg" ? "minus" : form === "inter" ? "q" : "plus",
    tiles, distractors: [trap === "is" && form === "inter" ? "Is" : trap === "are" && form === "inter" ? "Are" : trap], answer: sent,
    tip: rule(v, form, p)
  };
}
const MISSIONS = [
  { id: "conj", icon: "✍️", title: "Conjugue", desc: "Forme affirmative : am / is / are, have / has, play / plays.", build: () => Array.from({ length: 10 }, conjQuestion) },
  { id: "neg", icon: "➖", title: "Forme négative", desc: "He plays football. → He doesn't play football.", build: () => Array.from({ length: 8 }, () => transformQuestion("neg")) },
  { id: "inter", icon: "❓", title: "Forme interrogative", desc: "She has a dog. → Does she have a dog?", build: () => Array.from({ length: 8 }, () => transformQuestion("inter")) },
  { id: "choice", icon: "🔎", title: "Choisis la bonne forme", desc: "is ou are ? don't ou doesn't ? Do ou Does ?", build: () => Array.from({ length: 10 }, choiceQuestion) },
  { id: "order", icon: "🧩", title: "Remets dans l'ordre", desc: "Construis la phrase avec les étiquettes. Attention au piège !", build: () => Array.from({ length: 8 }, orderQuestion) },
  { id: "mix", icon: "🎲", title: "Tout mélangé", desc: "Transforme les phrases à toutes les formes : le grand test !", build: () => Array.from({ length: 10 }, () => { const t = pick(["neg", "inter", "aff"]); return t === "aff" ? transformQuestion("aff", pick(["neg", "inter"])) : transformQuestion(t); }) }
];
