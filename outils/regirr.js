/* RV : [{past, base, type: regular|irregular, fr}] */
function regRule(base) {
  if (/e$/.test(base)) return `${base} se termine par -e → on ajoute seulement <b>-d</b>.`;
  if (/[^aeiou]y$/.test(base)) return `${base} se termine par consonne + y → <b>-ied</b>.`;
  if (base === "stop") return `${base} : consonne-voyelle-consonne → on <b>double</b> la consonne + -ed.`;
  if (base === "travel") return `${base} : en anglais britannique, on double le l → <b>travelled</b>.`;
  return `Verbe régulier : BV + <b>-ed</b>.`;
}
function regularize(base) {
  if (/e$/.test(base)) return base + "d";
  if (/[^aeiou]y$/.test(base)) return base.slice(0, -1) + "ied";
  return base + "ed";
}
const REG = RV.filter(v => v.type === "regular"), IRR = RV.filter(v => v.type === "irregular");

function typeQuestion(v) {
  return {
    kind: "mcq", grid: 2, html: true, keepOrder: true, instr: "Régulier ou irrégulier ?", label: v.past,
    head: `<div class="big-word">${esc(v.past)}</div><div class="big-sub">Ce verbe au prétérit est-il régulier ou irrégulier ?</div>`,
    options: ["Régulier<small>BV + -ed / -d / -ied</small>", "Irrégulier<small>forme spéciale</small>"],
    correct: v.type === "regular" ? 0 : 1, correctText: (v.type === "regular" ? "Régulier" : "Irrégulier") + ` (${v.base} → ${v.past})`,
    tip: `Base verbale : <b>${v.base}</b> (${v.fr}).`
  };
}
function baseQuestion(v) {
  return {
    kind: "gap", instr: "Retrouve la base verbale", label: v.past,
    head: `<div class="big-word">${esc(v.past)}</div><div class="big-sub">Quelle est la base verbale de ce verbe ?</div>`,
    parts: ["to ", { answers: [v.base], width: 200 }], correct: v.base,
    tip: `${v.past} → <b>${v.base}</b> (${v.fr}).`
  };
}
function pastRegQuestion(v) {
  return {
    kind: "gap", instr: "Écris le prétérit (verbes réguliers)", label: v.base,
    head: `<div class="big-word">${esc(v.base)}</div><div class="big-sub">${esc(v.fr)} · attention à l'orthographe !</div>`,
    parts: [{ answers: [v.past].concat(v.base === "travel" ? ["traveled"] : []), width: 220 }], correct: v.past,
    tip: regRule(v.base)
  };
}
function pastIrrQuestion(v) {
  const opts = [v.past, regularize(v.base), v.past + (/e$/.test(v.past) ? "d" : "ed")];
  return {
    kind: "mcq", instr: "Choisis le bon prétérit (verbes irréguliers)", label: v.base,
    head: `<div class="big-word">${esc(v.base)}</div><div class="big-sub">${esc(v.fr)}</div>`,
    options: opts, correct: 0, tip: `${v.base} est irrégulier → <b>${v.past}</b>. Pas de -ed !`
  };
}
function intrusQuestion(i) {
  const findIrr = i % 2 === 0;
  const many = shuffle(findIrr ? REG : IRR).slice(0, 3), odd = pick(findIrr ? IRR : REG);
  const all = [odd].concat(many);
  return {
    kind: "mcq", grid: 2, instr: "Trouve l'intrus", label: findIrr ? "Lequel est irrégulier ?" : "Lequel est régulier ?",
    head: `<div class="fr-line">${findIrr ? "Lequel de ces verbes est <b>irrégulier</b> ?" : "Lequel de ces verbes est <b>régulier</b> ?"}</div>`.replace(/&lt;/g, "<"),
    options: all.map(v => v.past), correct: 0,
    correctText: `${odd.past} (${odd.base})`,
    tip: `${odd.past} vient de <b>${odd.base}</b> : il est ${findIrr ? "irrégulier" : "régulier"}. Les autres : ${many.map(v => v.past + " (" + v.base + ")").join(", ")}.`
  };
}

const MISSIONS = [
  { id: "type", icon: "⚖️", title: "Régulier ou irrégulier ?", desc: "Lis le verbe au prétérit et trouve sa nature.", build: () => shuffle(RV).slice(0, 10).map(typeQuestion) },
  { id: "base", icon: "🔙", title: "Retrouve la base verbale", desc: "went → go : remonte du prétérit à la base verbale.", build: () => shuffle(RV).slice(0, 10).map(baseQuestion) },
  { id: "reg", icon: "✍️", title: "Prétérit des réguliers", desc: "-ed, -d, -ied ou consonne doublée ? Écris le prétérit.", build: () => shuffle(REG).slice(0, 10).map(pastRegQuestion) },
  { id: "irr", icon: "⚡", title: "Prétérit des irréguliers", desc: "Choisis la bonne forme : pas de -ed pour les irréguliers !", build: () => shuffle(IRR).slice(0, 10).map(pastIrrQuestion) },
  { id: "intrus", icon: "🕵️", title: "Trouve l'intrus", desc: "Quatre verbes, un seul est différent : lequel ?", build: () => [0,1,2,3,4,5,6,7].map(intrusQuestion) }
];
