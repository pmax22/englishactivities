/* Pronoms personnels : sujet / complément */
// [avant, groupe souligné, après, pronom attendu]
const SUBJ_ITEMS = [
  ["", "Tom", " plays football.", "He"], ["", "My sister", " is very funny.", "She"], ["", "My parents", " live in Paris.", "They"],
  ["", "The cat", " is black.", "It"], ["", "Emma and I", " are best friends.", "We"], ["", "You and Lucas", " are late.", "You"],
  ["", "The children", " are in the garden.", "They"], ["", "My grandmother", " cooks very well.", "She"], ["", "The car", " is red.", "It"],
  ["", "Mr Smith", " is my English teacher.", "He"], ["", "My friends and I", " play video games.", "We"], ["", "The books", " are on the table.", "They"],
  ["", "Léa", " has a dog.", "She"], ["", "The dog", " is hungry.", "It"]
];
const OBJ_ITEMS = [
  ["I love ", "my parents", ".", "them"], ["She calls ", "Tom", " every day.", "him"], ["We visit ", "our grandmother", " on Sundays.", "her"],
  ["He eats ", "the apple", ".", "it"], ["They help ", "Emma and me", ".", "us"], ["I see ", "the children", ".", "them"],
  ["Do you know ", "Mr Smith", "?", "him"], ["My mum loves ", "my sister and me", ".", "us"], ["I like ", "this song", ".", "it"],
  ["The teacher asks ", "you and Lucas", " a question.", "you"], ["Look at ", "the birds", "!", "them"], ["Lucas plays with ", "Léa", ".", "her"],
  ["I watch ", "the film", ".", "it"], ["We talk to ", "the new student", ".", "him"]
];
// [phrase à trou, option sujet, option complément, bonne réponse : 0 = sujet, 1 = complément]
const SO_ITEMS = [
  ["____ like pizza.", "I", "me", 0], ["Can you help ____ ?", "I", "me", 1], ["____ is my best friend.", "He", "Him", 0],
  ["I know ____ very well.", "he", "him", 1], ["____ are from Spain.", "They", "Them", 0], ["Look at ____ !", "they", "them", 1],
  ["____ live in London.", "We", "Us", 0], ["She invited ____ to her party.", "we", "us", 1], ["____ is a teacher.", "She", "Her", 0],
  ["I don't like ____.", "she", "her", 1], ["Tom always helps ____.", "I", "me", 1], ["My dad and ____ play tennis.", "I", "me", 0],
  ["Can you call ____ tonight?", "he", "him", 1], ["____ have a big house.", "They", "Them", 0]
];
// [français, bonne traduction, erreurs…]
const TR_ITEMS = [
  ["Il m'aime.", "He loves me.", "Him loves I.", "He me loves."],
  ["Je les connais.", "I know them.", "I them know.", "I know they."],
  ["Elle nous aide.", "She helps us.", "She us helps.", "Her helps we."],
  ["Nous l'appelons (lui).", "We call him.", "Us call him.", "We him call."],
  ["Ils te regardent.", "They look at you.", "Them look at you.", "They you look at."],
  ["Tu la vois ?", "Do you see her?", "Do you her see?", "Do you see she?"],
  ["Je lui parle (à elle).", "I talk to her.", "I her talk.", "I talk to she."],
  ["Vous m'écoutez.", "You listen to me.", "You me listen.", "You listen to I."],
  ["Nous le mangeons (le gâteau).", "We eat it.", "We it eat.", "Us eat it."],
  ["Elles jouent avec nous.", "They play with us.", "They play with we.", "Them play with us."]
];
const RULE_S = "Pronom <b>sujet</b> : il est placé <b>avant</b> le verbe et fait l'action.";
const RULE_O = "Pronom <b>complément</b> : il est placé <b>après</b> le verbe ou après une préposition (with, to, at…).";

function gapItem(it, kind) {
  const [b, u, a, p] = it;
  return {
    kind: "gap", instr: kind === "s" ? "Remplace le groupe souligné par un pronom sujet" : "Remplace le groupe souligné par un pronom complément",
    label: b + u + a,
    head: `<div class="fr-line">${esc(b)}<u>${esc(u)}</u>${esc(a)}</div>`,
    parts: [b, { answers: [p], width: 110 }, a], correct: b + p + a,
    tip: (kind === "s" ? RULE_S : RULE_O) + ` ${u} → <b>${p}</b>.`
  };
}
function soItem(it) {
  const [line, s, o, c] = it;
  return {
    kind: "mcq", grid: 2, keepOrder: true, instr: "Sujet ou complément ?", label: line,
    head: `<div class="fr-line">${esc(line)}</div>`,
    options: [s, o], correct: c, correctText: line.replace("____", c === 0 ? s : o).replace(" ?", "?").replace(" !", "!"),
    tip: c === 0 ? RULE_S : RULE_O
  };
}
function trItem(it) {
  const [fr, ok, ...bad] = it;
  return {
    kind: "mcq", instr: "Quelle est la bonne traduction ?", label: fr,
    head: `<div class="fr-line">${esc(fr)}</div>`, options: [ok, ...bad], correct: 0,
    tip: "En anglais, le pronom complément se place <b>après</b> le verbe (en français, il est avant)."
  };
}
const MISSIONS = [
  { id: "subj", icon: "👤", title: "Pronoms sujets", desc: "Remplace le groupe souligné : Tom → He, my parents → They…", build: () => shuffle(SUBJ_ITEMS).slice(0, 10).map(i => gapItem(i, "s")) },
  { id: "obj", icon: "🎯", title: "Pronoms compléments", desc: "Remplace le groupe souligné : Tom → him, my parents → them…", build: () => shuffle(OBJ_ITEMS).slice(0, 10).map(i => gapItem(i, "o")) },
  { id: "so", icon: "⚖️", title: "Sujet ou complément ?", desc: "I ou me ? he ou him ? Choisis le bon pronom.", build: () => shuffle(SO_ITEMS).slice(0, 10).map(soItem) },
  { id: "tr", icon: "🔎", title: "Quelle est la bonne traduction ?", desc: "Attention à la place du pronom complément !", build: () => shuffle(TR_ITEMS).slice(0, 8).map(trItem) },
  { id: "mix", icon: "🎲", title: "Tout mélangé", desc: "Pronoms sujets et compléments mélangés : le grand test !", build: () => shuffle(SUBJ_ITEMS.map(i => gapItem(i, "s")).concat(OBJ_ITEMS.map(i => gapItem(i, "o")))).slice(0, 12) }
];
