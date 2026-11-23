/* Adverbes de fréquence */
const ADVS = [["always", "100 %", "toujours"], ["usually", "90 %", "d'habitude"], ["often", "70 %", "souvent"], ["sometimes", "50 %", "parfois"], ["rarely", "10 %", "rarement"], ["never", "0 %", "jamais"]];
// [français, sujet, verbe (be ou autre), adverbe, suite]
const SENT = [
  ["Je joue toujours au football le samedi.", "I", "play", "always", "football on Saturdays"],
  ["Il est souvent en retard.", "He", "is", "often", "late"],
  ["Nous ne mangeons jamais de viande.", "We", "eat", "never", "meat"],
  ["Elle est toujours gentille.", "She", "is", "always", "nice"],
  ["Ils regardent parfois la télé.", "They", "watch", "sometimes", "TV"],
  ["D'habitude, je me lève à 7 heures.", "I", "get up", "usually", "at 7"],
  ["Mon frère lit rarement des livres.", "My brother", "reads", "rarely", "books"],
  ["Tu es souvent fatigué.", "You", "are", "often", "tired"],
  ["Elle va souvent à la piscine.", "She", "goes", "often", "to the swimming pool"],
  ["Nous sommes rarement malades.", "We", "are", "rarely", "ill"],
  ["Tom ne boit jamais de café.", "Tom", "drinks", "never", "coffee"],
  ["Je suis parfois triste.", "I", "am", "sometimes", "sad"],
  ["D'habitude, mes parents travaillent le lundi.", "My parents", "work", "usually", "on Mondays"],
  ["Le bus est toujours plein.", "The bus", "is", "always", "full"],
  ["Elle prend toujours le bus.", "She", "takes", "always", "the bus"],
  ["Ils ne sont jamais à l'heure.", "They", "are", "never", "on time"],
  ["Je fais rarement mes devoirs le dimanche.", "I", "do", "rarely", "my homework on Sundays"],
  ["Mon chat dort souvent sur mon lit.", "My cat", "sleeps", "often", "on my bed"]
];
const HOW = [
  ["une fois par semaine", "once a week", "twice a week", "one time by week"],
  ["deux fois par mois", "twice a month", "two times by month", "once a month"],
  ["tous les jours", "every day", "all the days", "every days"],
  ["trois fois par an", "three times a year", "three time a year", "three times by year"],
  ["tous les matins", "every morning", "all the mornings", "each mornings"],
  ["une fois par mois", "once a month", "one time by month", "twice a month"],
  ["tous les week-ends", "every weekend", "all the weekends", "every weekends"]
];
const isBe = v => /^(am|is|are)$/.test(v);
const sentence = s => { const [, S, v, a, r] = s; return (isBe(v) ? `${S} ${v} ${a}` : `${S} ${a} ${v}`) + (r ? " " + r : "") + "."; };
const begin = s => { const [, S, v, a] = s; return isBe(v) ? `${S} ${v} ${a}` : `${S} ${a} ${v}`; };
const RULE = s => isBe(s[2])
  ? `Avec <b>be</b> (am / is / are), l'adverbe se place <b>après</b> le verbe : ${s[1]} ${s[2]} <b>${s[3]}</b>…`
  : `Avec les autres verbes, l'adverbe se place <b>avant</b> le verbe : ${s[1]} <b>${s[3]}</b> ${s[2]}…`;
const lower = S => /^(My|The)\b/.test(S) ? S.charAt(0).toLowerCase() + S.slice(1) : S;

function advQuestion() {
  const [en, pct, fr] = pick(ADVS);
  const byPct = Math.random() < .5;
  return {
    kind: "mcq", grid: 3, keepOrder: true, instr: byPct ? "Quel adverbe correspond à ce pourcentage ?" : "Traduis l'adverbe",
    label: byPct ? pct : fr, head: `<div class="big-word">${esc(byPct ? pct : fr)}</div>`,
    options: ADVS.map(a => a[0]), correct: ADVS.findIndex(a => a[0] === en), correctText: `${en} (${pct} · ${fr})`,
    tip: "always 100 % · usually 90 % · often 70 % · sometimes 50 % · rarely 10 % · never 0 %"
  };
}
function gapQuestion(s) {
  const answers = [begin(s)];
  if (s[3] === "sometimes" || s[3] === "usually") answers.push(`${s[3]} ${lower(s[1])} ${s[2]}`);
  return {
    kind: "gap", instr: "Traduis : attention à la place de l'adverbe", label: s[0],
    head: `<div class="fr-line">${esc(s[0])}</div>`,
    parts: [{ answers, width: 240 }, (s[4] ? " " + s[4] : "") + "."], correct: sentence(s), tip: RULE(s),
    diagnose(vals) {
      const t = " " + norm(vals[0]) + " ";
      if (!t.includes(" " + s[3] + " ")) return `L'adverbe attendu est <b>${s[3]}</b> (${ADVS.find(a => a[0] === s[3])[2]}).`;
      if (s[3] === "never" && /n't|not/.test(t)) return "<b>never</b> est déjà négatif : pas de don't / not avec never.";
      return RULE(s);
    }
  };
}
function orderQuestion(s) {
  const tiles = (isBe(s[2]) ? [s[1], s[2], s[3]] : [s[1], s[3], s[2]]).concat(s[4] ? [s[4]] : []);
  const alts = (s[3] === "sometimes" || s[3] === "usually") ? [`${capF(s[3])} ${lower(s[1])} ${s[2]}${s[4] ? " " + s[4] : ""}`] : [];
  return { kind: "order", instr: "Remets les mots dans l'ordre", label: s[0], head: `<div class="fr-line">${esc(s[0])}</div>`,
    tiles, distractors: [], answer: sentence(s), alts, tip: RULE(s) };
}
function choiceQuestion(s) {
  const [, S, v, a, r] = s, R = r ? " " + r : "";
  const ok = sentence(s);
  const wrong = isBe(v) ? `${S} ${a} ${v}${R}.` : `${S} ${v} ${a}${R}.`;
  const opts = [ok, wrong];
  if (a === "always" || a === "never") opts.push(`${capF(a)} ${lower(S)} ${v}${R}.`);
  return { kind: "mcq", instr: "Quelle phrase est correcte ?", label: s[0], head: `<div class="fr-line">${esc(s[0])}</div>`,
    options: opts, correct: 0, tip: RULE(s) };
}
function howQuestion(h) {
  const [fr, ok, ...bad] = h;
  return { kind: "mcq", instr: "How often? · Traduis l'expression", label: fr, head: `<div class="fr-line">${esc(fr)}</div>`,
    options: [ok, ...bad], correct: 0,
    tip: "once = une fois · twice = deux fois · three times = trois fois · <b>a</b> week / <b>a</b> month = par semaine / par mois · every + singulier. Ces expressions se placent en <b>fin</b> de phrase." };
}
const MISSIONS = [
  { id: "adv", icon: "📊", title: "Quel adverbe ?", desc: "Associe chaque adverbe à son pourcentage et à sa traduction.", build: () => Array.from({ length: 10 }, advQuestion) },
  { id: "order", icon: "🧩", title: "Remets dans l'ordre", desc: "Où va l'adverbe ? Avant le verbe, ou après be ?", build: () => shuffle(SENT).slice(0, 8).map(orderQuestion) },
  { id: "choice", icon: "🔎", title: "Quelle phrase est correcte ?", desc: "She is always late ou She always is late ?", build: () => shuffle(SENT).slice(0, 8).map(choiceQuestion) },
  { id: "trad", icon: "✍️", title: "Traduis", desc: "Écris le début de la phrase : sujet + adverbe + verbe (ou be + adverbe).", build: () => shuffle(SENT).slice(0, 8).map(gapQuestion) },
  { id: "how", icon: "📅", title: "How often?", desc: "once a week, twice a month, every day…", build: () => shuffle(HOW).slice(0, 7).map(howQuestion) },
  { id: "mix", icon: "🎲", title: "Tout mélangé", desc: "Le grand test !", build: () => shuffle([].concat(shuffle(SENT).slice(0, 4).map(gapQuestion), shuffle(SENT).slice(0, 3).map(choiceQuestion), shuffle(SENT).slice(0, 3).map(orderQuestion))) }
];
