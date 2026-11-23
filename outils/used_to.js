/* USED : [{subject, verb, after, answers, correct, explanation}] */
USED.forEach(q => {
  const a = q.answers[0];
  q.type = a.startsWith("did ") ? "inter" : a.startsWith("didn't") || a.startsWith("did not") ? "neg" : "aff";
  q.bv = q.type === "inter" ? q.verb.split("/")[1].trim() : q.verb.replace(/^not /, "");
  if (q.type === "inter") q.subj = q.verb.split("/")[0].trim();
  q.full = (q.correct + " " + q.after).trim();
});
const TYPE_LABEL = { aff: "Affirmatif", neg: "Négatif", inter: "Interrogatif" };
const SIGN = { aff: "plus", neg: "minus", inter: "q" };
const RULE = {
  aff: "Affirmatif : sujet + <b>used to</b> + base verbale.",
  neg: "Négatif : sujet + <b>didn't use to</b> + base verbale (pas de -d à use après didn't).",
  inter: "Interrogatif : <b>Did</b> + sujet + <b>use to</b> + base verbale ?"
};
const noPunct = s => s.replace(/\s*[.?!]$/, "");

function gapQuestion(q) {
  const parts = q.type === "inter"
    ? [{ answers: q.answers, width: 270, hint: q.verb, ph: "Did …" }, " " + q.after]
    : [q.subject + " ", { answers: q.answers, width: 230, hint: q.verb }, " " + q.after];
  return {
    kind: "gap", instr: `${TYPE_LABEL[q.type]} · complète avec used to`, label: q.full, sign: SIGN[q.type],
    parts, correct: q.full, tip: q.explanation,
    diagnose(vals) {
      const t = " " + norm(vals[0]) + " ";
      if (q.type === "aff" && / use to /.test(t)) return "À l'affirmatif, on écrit <b>used</b> to (avec -d).";
      if (q.type !== "aff" && / used to /.test(t)) return "Après did / didn't, on écrit <b>use</b> to (sans -d).";
      if (q.type === "neg" && !/ didn't /.test(t)) return RULE.neg;
      if (q.type === "inter" && !/^ did /.test(t)) return RULE.inter;
      return q.explanation;
    }
  };
}

function useOrUsed(q) {
  const after = q.after;
  const line = q.type === "aff" ? `${q.subject} ____ ${q.bv} ${after}`
    : q.type === "neg" ? `${q.subject} didn't ____ ${q.bv} ${after}`
    : `Did ${q.subj} ____ ${q.bv} ${after}`;
  return {
    kind: "mcq", grid: 2, instr: "used to ou use to ?", label: line,
    head: `<div class="fr-line">${esc(line)}</div>`,
    options: ["used to", "use to"], correct: q.type === "aff" ? 0 : 1, keepOrder: true,
    correctText: q.full,
    tip: q.type === "aff" ? "Affirmatif → <b>used to</b> (avec -d)." : "Après did / didn't → <b>use to</b> (sans -d) : did porte déjà le passé."
  };
}

function orderQuestion(q) {
  const tiles = q.type === "aff" ? [q.subject, "used to", q.bv, noPunct(q.after)]
    : q.type === "neg" ? [q.subject, "didn't", "use to", q.bv, noPunct(q.after)]
    : ["Did", q.subj, "use to", q.bv, noPunct(q.after)];
  const trap = q.type === "aff" ? "use to" : "used to";
  return {
    kind: "order", instr: `Remets les mots dans l'ordre · ${TYPE_LABEL[q.type]}`, label: q.full,
    head: `<p class="small-hint" style="margin:0 0 14px">${RULE[q.type]}</p>`,
    tiles, distractors: [trap], answer: q.full,
    tip: `L'étiquette <b>${trap}</b> était un piège.`
  };
}

const ofType = t => USED.filter(q => q.type === t);
const MISSIONS = [
  { id: "aff", icon: "➕", title: "Affirmatif", desc: "Complète : sujet + used to + base verbale.", build: () => shuffle(ofType("aff")).slice(0, 8).map(gapQuestion) },
  { id: "neg", icon: "➖", title: "Négatif", desc: "Complète : sujet + didn't use to + base verbale.", build: () => shuffle(ofType("neg")).slice(0, 8).map(gapQuestion) },
  { id: "inter", icon: "❓", title: "Interrogatif", desc: "Complète : Did + sujet + use to + base verbale ?", build: () => shuffle(ofType("inter")).slice(0, 8).map(gapQuestion) },
  { id: "used", icon: "⚖️", title: "used to ou use to ?", desc: "Avec ou sans -d ? Choisis la bonne forme.", build: () => shuffle(USED).slice(0, 10).map(useOrUsed) },
  { id: "order", icon: "🧩", title: "Remets dans l'ordre", desc: "Construis la phrase avec les étiquettes. Attention au piège !", build: () => shuffle(USED).slice(0, 8).map(orderQuestion) },
  { id: "mix", icon: "🎲", title: "Tout mélangé", desc: "Affirmatif, négatif et interrogatif mélangés : le grand test !", build: () => shuffle(USED).slice(0, 10).map(gapQuestion) }
];
