/* COMP : [{type: plus|eq|minus, subject1, subject2, adj, answers, correct, fr, explanation}]
   ADJ : [adjectif, comparatif, règle] */
const COMPARATIVE = Object.fromEntries(ADJ.map(a => [a[0], a[1]]));
const RULES = {
  er: a => `${a} est court → on ajoute <b>-er</b>.`,
  r: a => `${a} se termine par -e → on ajoute seulement <b>-r</b>.`,
  double: a => `${a} se termine par consonne-voyelle-consonne → on <b>double</b> la consonne + -er.`,
  ier: a => `${a} se termine par -y → <b>-ier</b>.`,
  more: a => `${a} est long (2 syllabes ou plus) → <b>more</b> + adjectif.`,
  irr: a => `${a} est irrégulier : à apprendre par cœur !`
};
const RULE_OF = Object.fromEntries(ADJ.map(a => [a[0], a[2]]));
const LABEL = { plus: "Supériorité (+)", eq: "Égalité (=)", minus: "Infériorité (−)" };
const SIGN = { plus: "plus", eq: "eq", minus: "minus" };
const SYM = { plus: "+", eq: "=", minus: "−" };
function plusForm(adj) { return (COMPARATIVE[adj] || "more " + adj) + " than"; }
function formOf(type, adj) { return type === "plus" ? plusForm(adj) : type === "eq" ? `as ${adj} as` : `less ${adj} than`; }
function sentence(q, form) { return `${q.subject1} is ${form} ${q.subject2}.`; }
function badShort(adj) { const r = RULE_OF[adj]; return r === "more" ? (adj.replace(/e$/, "") + "er than") : `more ${adj} than`; }

COMP.forEach(q => { q.full = sentence(q, q.correct.replace(/^is /, "")); });

function gapQuestion(q) {
  return {
    kind: "gap", instr: `${LABEL[q.type]} · complète la phrase`, label: q.fr, sign: SIGN[q.type],
    head: `<div class="fr-line">${esc(q.fr)}</div>`,
    parts: [q.subject1 + " ", { answers: q.answers, width: 260, hint: `${q.adj} ${SYM[q.type]}` }, " " + q.subject2 + "."],
    correct: q.full, tip: q.explanation,
    diagnose(vals) {
      const t = " " + norm(vals[0]) + " ";
      if (!/^ is | are /.test(t)) return "N'oublie pas le verbe <b>is</b> : Hulk <b>is</b> stronger than Thor.";
      if (q.type === "eq" && / than /.test(t)) return "Égalité : <b>as</b> + adjectif + <b>as</b> (pas than).";
      if (q.type !== "eq" && / as /.test(t)) return "Supériorité et infériorité : on utilise <b>than</b> (que).";
      if (q.type === "plus" && RULE_OF[q.adj] && !t.includes(" " + plusForm(q.adj) + " ")) return RULES[RULE_OF[q.adj]](q.adj) + ` → ${plusForm(q.adj)}.`;
      return q.explanation;
    }
  };
}

function formQuestion(a) {
  const [adj, comp, rule] = a;
  const ok = comp + " than";
  let opts;
  if (rule === "irr") opts = [ok, adj + "er than", "more " + adj + " than"];
  else if (rule === "more") opts = [ok, adj.replace(/e$/, "") + "er than", "more " + adj.replace(/e$/, "") + "er than"];
  else opts = [ok, "more " + adj + " than", "more " + comp + " than"];
  return {
    kind: "mcq", instr: "Choisis le bon comparatif de supériorité", label: adj,
    head: `<div class="big-word">${esc(adj)}</div><div class="big-sub">plus … que</div>`,
    options: opts, correct: 0, tip: RULES[rule](adj) + ` → <b>${ok}</b>.`
  };
}

function translateQuestion(q) {
  const right = sentence(q, formOf(q.type, q.adj));
  const otherType = q.type === "eq" ? "plus" : q.type === "plus" ? "eq" : "plus";
  const wrong1 = sentence(q, formOf(otherType, q.adj));
  const wrong2 = q.type === "plus" ? sentence(q, badShort(q.adj)) : q.type === "eq" ? sentence(q, `as ${q.adj} than`) : sentence(q, `less ${plusForm(q.adj).replace(/ than$/, "")} than`);
  return {
    kind: "mcq", instr: "Quelle est la bonne traduction ?", label: q.fr,
    head: `<div class="fr-line">${esc(q.fr)}</div>`,
    options: [q.full, wrong1, wrong2], correct: 0, tip: q.explanation
  };
}

function orderQuestion(q) {
  const form = q.correct.replace(/^is /, "");
  const tiles = [q.subject1, "is", ...form.split(" "), q.subject2];
  const trap = q.type === "eq" ? "than" : q.type === "minus" ? "more" : (RULE_OF[q.adj] === "more" ? "as" : "more");
  return {
    kind: "order", instr: `Remets les mots dans l'ordre · ${LABEL[q.type]}`, label: q.fr,
    head: `<div class="fr-line">${esc(q.fr)}</div>`,
    tiles, distractors: [trap], answer: q.full,
    tip: `Le mot <b>${trap}</b> était un piège.`
  };
}

const ofType = t => COMP.filter(q => q.type === t);
const MISSIONS = [
  { id: "plus", icon: "➕", title: "Supériorité", desc: "plus … que : adjectif + -er than / more + adjectif + than.", build: () => shuffle(ofType("plus")).slice(0, 8).map(gapQuestion) },
  { id: "eq", icon: "⚖️", title: "Égalité", desc: "aussi … que : as + adjectif + as.", build: () => shuffle(ofType("eq")).slice(0, 8).map(gapQuestion) },
  { id: "minus", icon: "➖", title: "Infériorité", desc: "moins … que : less + adjectif + than.", build: () => shuffle(ofType("minus")).slice(0, 8).map(gapQuestion) },
  { id: "form", icon: "📏", title: "Court ou long ?", desc: "-er ou more ? Choisis le bon comparatif de supériorité.", build: () => shuffle(ADJ).slice(0, 10).map(formQuestion) },
  { id: "trad", icon: "🔎", title: "Quelle est la bonne traduction ?", desc: "Lis la phrase en français et choisis la bonne phrase anglaise.", build: () => shuffle(COMP).slice(0, 8).map(translateQuestion) },
  { id: "order", icon: "🧩", title: "Remets dans l'ordre", desc: "Construis la phrase avec les étiquettes. Attention au piège !", build: () => shuffle(COMP).slice(0, 8).map(orderQuestion) },
  { id: "mix", icon: "🎲", title: "Tout mélangé", desc: "Supériorité, égalité et infériorité : le grand test !", build: () => shuffle(COMP).slice(0, 10).map(gapQuestion) }
];
