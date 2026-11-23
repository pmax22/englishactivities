/* PHRASES : [{fr, type: aff|neg|inter, begin: [réponses acceptées], beginDisplay, end, hint, expl, verb, subj}]
   VERBS : [[BV, prétérit affiché, irrégulier, français, [formes du prétérit]]] */
const BV_OF = {};
VERBS.forEach(v => { BV_OF[v[0]] = v[0]; v[4].forEach(p => BV_OF[p] = v[0]); });
const PAST_OF = Object.fromEntries(VERBS.map(v => [v[0], v[4][0]]));
const IRR_OF = Object.fromEntries(VERBS.map(v => [v[0], !!v[2]]));
const TYPE_LABEL = { aff: "Affirmatif", neg: "Négatif", inter: "Interrogatif" };
const SIGN = { aff: "plus", neg: "minus", inter: "q" };

function fullSentence(p) { return (p.beginDisplay + (p.end ? " " + p.end : "")).trim() + (/[.?!]$/.test(p.end) ? "" : (p.type === "inter" ? "?" : ".")); }
function plural(subj) { if (/^(i|you|we|they)$/i.test(subj)) return true; if (/^(he|she|it)$/i.test(subj)) return false; return / and /i.test(subj) || /s$/i.test(subj); }
function subjMid(s) { return /^(He|She|It|We|You|They|The|My|Our|Your|His|Her|Their|A|An)\b/.test(s) ? s.charAt(0).toLowerCase() + s.slice(1) : s; }
function endNoPunct(e) { return (e || "").replace(/\s*[.?!]$/, ""); }

function gapQuestion(p) {
  const v = p.verb, past = PAST_OF[v];
  return {
    kind: "gap", instr: `${TYPE_LABEL[p.type]} · traduis en anglais`, label: p.fr, sign: SIGN[p.type],
    head: `<div class="fr-line">${esc(p.fr)}</div>`,
    parts: [{ answers: p.begin, width: 240, ph: p.type === "inter" ? "Did … ?" : "…" }, p.end ? " " + p.end : (p.type === "inter" ? " ?" : ".")],
    foot: p.hint ? `<p class="small-hint">Aide : <b>${esc(p.hint)}</b></p>` : "",
    correct: fullSentence(p), tip: p.expl,
    diagnose(vals) {
      const t = " " + norm(vals[0]) + " ";
      if (v === "be") return p.expl;
      if (p.type === "aff") {
        if (/ did /.test(t)) return `À l'affirmatif, pas de <b>did</b> : le verbe se met directement au prétérit (<b>${past}</b>).`;
        if (past !== v && t.includes(" " + v + " ")) return `Il faut le prétérit : ${v} → <b>${past}</b>${IRR_OF[v] ? " (irrégulier)" : ""}.`;
      }
      if (p.type === "neg") {
        if (!/ didn't /.test(t)) return "Négatif : <b>didn't</b> (did not) + base verbale.";
        if (past !== v && t.includes(" " + past + " ")) return `Après didn't, le verbe reste en BV : <b>${v}</b>, pas <s>${past}</s>.`;
      }
      if (p.type === "inter") {
        if (!/^ did /.test(t)) return "Interrogatif : la question commence par <b>Did</b> + sujet + BV.";
        if (past !== v && t.includes(" " + past + " ")) return `Après Did, le verbe reste en BV : <b>${v}</b>, pas <s>${past}</s>.`;
      }
      return p.expl;
    }
  };
}

function orderQuestion(p) {
  const v = p.verb, past = PAST_OF[v];
  const tiles = p.beginDisplay.split(" ");
  if (p.end) tiles.push(endNoPunct(p.end));
  const trap = p.type === "aff" ? v : past;
  return {
    kind: "order", instr: `Remets les mots dans l'ordre · ${TYPE_LABEL[p.type]}`, label: p.fr,
    head: `<div class="fr-line">${esc(p.fr)}</div>`,
    tiles, distractors: [trap], answer: fullSentence(p),
    tip: `Le mot <b>${esc(trap)}</b> était un piège : ${p.type === "aff" ? "à l'affirmatif, on utilise le prétérit." : "après did / didn't, on utilise la base verbale."}`
  };
}

function choiceQuestion(p) {
  const v = p.verb, past = PAST_OF[v], S = p.subj, Sm = subjMid(S), E = p.end ? " " + endNoPunct(p.end) : "";
  const doo = plural(S) ? "don't" : "doesn't", Do = plural(S) ? "Do" : "Does";
  let opts;
  if (p.type === "aff") opts = [`${S} ${past}${E}.`, `${S} ${v}${E}.`, `${S} did ${past}${E}.`];
  else if (p.type === "neg") opts = [`${S} didn't ${v}${E}.`, `${S} didn't ${past}${E}.`, `${S} not ${past}${E}.`, `${S} ${doo} ${v}${E}.`];
  else opts = [`Did ${Sm} ${v}${E}?`, `Did ${Sm} ${past}${E}?`, `${S} ${past}${E}?`, `${Do} ${Sm} ${v}${E}?`];
  return {
    kind: "mcq", instr: "Quelle phrase est correcte ?", label: p.fr,
    head: `<div class="fr-line">${esc(p.fr)}</div>`, options: opts, correct: 0, tip: p.expl
  };
}

const notBe = p => p.verb !== "be" && PAST_OF[p.verb] !== p.verb;
const ofType = t => PHRASES.filter(p => p.type === t);

const MISSIONS = [
  { id: "aff", icon: "➕", title: "Affirmatif", desc: "Traduis : sujet + verbe au prétérit (-ED ou forme irrégulière).", build: () => shuffle(ofType("aff")).slice(0, 8).map(gapQuestion) },
  { id: "neg", icon: "➖", title: "Négatif", desc: "Traduis : sujet + didn't + base verbale.", build: () => shuffle(ofType("neg")).slice(0, 8).map(gapQuestion) },
  { id: "inter", icon: "❓", title: "Interrogatif", desc: "Traduis : Did + sujet + base verbale ?", build: () => shuffle(ofType("inter")).slice(0, 8).map(gapQuestion) },
  { id: "order", icon: "🧩", title: "Remets dans l'ordre", desc: "Construis la phrase avec les étiquettes. Attention, un mot est un piège !", build: () => shuffle(PHRASES.filter(notBe)).slice(0, 8).map(orderQuestion) },
  { id: "choice", icon: "🔎", title: "Quelle phrase est correcte ?", desc: "Une seule phrase est juste : repère les erreurs de forme.", build: () => shuffle(PHRASES.filter(notBe)).slice(0, 8).map(choiceQuestion) },
  { id: "mix", icon: "🎲", title: "Tout mélangé", desc: "Affirmatif, négatif et interrogatif mélangés : le grand test !", build: () => shuffle(PHRASES).slice(0, 10).map(gapQuestion) }
];
