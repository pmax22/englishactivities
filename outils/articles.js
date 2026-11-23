/* Articles : a / an / the / Ø */
// [nom, article, explication]
const AAN = [
  ["apple", "an", "apple commence par un son voyelle."], ["banana", "a", "banana commence par un son consonne."],
  ["hour", "an", "le h de hour ne se prononce pas : on entend un son voyelle."], ["university", "a", "university se prononce « you- » : son consonne."],
  ["egg", "an", "egg commence par un son voyelle."], ["uniform", "a", "uniform se prononce « you- » : son consonne."],
  ["orange", "an", "orange commence par un son voyelle."], ["dog", "a", "dog commence par un son consonne."],
  ["elephant", "an", "elephant commence par un son voyelle."], ["honest man", "an", "le h de honest ne se prononce pas."],
  ["umbrella", "an", "umbrella commence par un son voyelle."], ["one-euro coin", "a", "one se prononce « wan » : son consonne."],
  ["house", "a", "le h de house se prononce : son consonne."], ["idea", "an", "idea commence par un son voyelle."],
  ["European country", "a", "European se prononce « you- » : son consonne."], ["ice cream", "an", "ice commence par un son voyelle."],
  ["old car", "an", "old commence par un son voyelle (c'est le mot qui suit l'article qui compte)."], ["cat", "a", "cat commence par un son consonne."],
  ["horse", "a", "le h de horse se prononce."], ["interesting book", "an", "interesting commence par un son voyelle."],
  ["yellow bag", "a", "yellow commence par un son consonne."], ["eagle", "an", "eagle commence par un son voyelle."]
];
// [phrase avec ____, article : a | an | the | Ø, explication]
const SENT = [
  ["I have a dog. ____ dog is called Rex.", "the", "On a déjà parlé du chien : on sait lequel → the."],
  ["Can you close ____ door, please?", "the", "On sait de quelle porte on parle → the."],
  ["____ sun is very hot today.", "the", "Le soleil est unique → the."],
  ["She is ____ teacher.", "a", "Métier : en anglais on met a / an."],
  ["He is ____ engineer.", "an", "Métier + son voyelle → an."],
  ["I want ____ apple, please.", "an", "Une pomme (n'importe laquelle), son voyelle → an."],
  ["____ moon is beautiful tonight.", "the", "La lune est unique → the."],
  ["We live in ____ small house.", "a", "Une maison (pas précisée), son consonne → a."],
  ["My father plays ____ guitar.", "the", "Instrument de musique → the."],
  ["It's ____ best day of my life!", "the", "Superlatif (the best) → the."],
  ["I saw ____ elephant at the zoo.", "an", "Un éléphant, son voyelle → an."],
  ["There is ____ cat in the garden.", "a", "Un chat (pas précisé) → a."],
  ["Where is ____ remote control?", "the", "On sait de quelle télécommande on parle → the."],
  ["My mother is ____ nurse.", "a", "Métier → a."],
  ["I love ____ music.", "Ø", "La musique en général → pas d'article."],
  ["____ music in this film is great.", "the", "La musique de CE film (précise) → the."],
  ["She plays ____ tennis every Sunday.", "Ø", "Sport → pas d'article."],
  ["We have ____ breakfast at 7.", "Ø", "Repas → pas d'article."],
  ["They speak ____ English.", "Ø", "Langue → pas d'article."],
  ["He lives in ____ France.", "Ø", "Pays → pas d'article."],
  ["We went to ____ United States.", "the", "Exception : the United States, the United Kingdom."],
  ["I go to the swimming pool on ____ Monday.", "Ø", "Jours de la semaine → pas d'article."],
  ["____ dogs are friendly animals.", "Ø", "Les chiens en général → pas d'article."],
  ["____ dogs next door are noisy.", "the", "Les chiens d'à côté (précis) → the."],
  ["My favourite subject is ____ history.", "Ø", "Matière scolaire → pas d'article."],
  ["I play ____ piano.", "the", "Instrument de musique → the."],
  ["____ children love chocolate.", "Ø", "Les enfants en général → pas d'article."],
  ["____ children in my class are nice.", "the", "Les enfants de ma classe (précis) → the."],
  ["He lives in ____ United Kingdom.", "the", "Exception : the United Kingdom."]
];
const CORRECT = [
  ["Je joue au football.", "I play football.", "I play the football.", "I play a football."],
  ["Elle est médecin.", "She is a doctor.", "She is doctor.", "She is an doctor."],
  ["J'ai un parapluie.", "I have an umbrella.", "I have a umbrella.", "I have umbrella."],
  ["Nous habitons en France.", "We live in France.", "We live in the France.", "We live in a France."],
  ["Nous déjeunons à midi.", "We have lunch at noon.", "We have the lunch at noon.", "We have a lunch at noon."],
  ["Ils parlent espagnol.", "They speak Spanish.", "They speak the Spanish.", "They speak a Spanish."],
  ["Le soleil est chaud.", "The sun is hot.", "Sun is hot.", "A sun is hot."],
  ["La vie est belle.", "Life is beautiful.", "The life is beautiful.", "A life is beautiful."],
  ["J'ai attendu une heure.", "I waited an hour.", "I waited a hour.", "I waited hour."],
  ["Il joue du violon.", "He plays the violin.", "He plays a violin.", "He plays an violin."]
];
const LABEL_ART = { a: "a", an: "an", the: "the", "Ø": "Ø" };
function aanQ(it) {
  const [n, art, why] = it;
  return {
    kind: "mcq", grid: 2, keepOrder: true, instr: "a ou an ?", label: n,
    head: `<div class="big-word">____ ${esc(n)}</div><div class="big-sub">Écoute le premier son du mot !</div>`,
    options: ["a", "an"], correct: art === "a" ? 0 : 1, correctText: `${art} ${n}`, tip: why
  };
}
function fill(line, art) { const r = art === "Ø" ? "" : art; let s = line.replace("____ ", r ? r + " " : ""); return s.charAt(0).toUpperCase() + s.slice(1); }
function sentQ(it, opts, instr) {
  const [line, art, why] = it;
  return {
    kind: "mcq", grid: opts.length, keepOrder: true, instr, label: line, html: true,
    head: `<div class="fr-line">${esc(line)}</div>`,
    options: opts.map(o => o === "Ø" ? "Ø<small>pas d'article</small>" : o), correct: opts.indexOf(art), correctText: fill(line, art), tip: why
  };
}
function correctQ(it) {
  const [fr, ok, ...bad] = it;
  return { kind: "mcq", instr: "Quelle phrase est correcte ?", label: fr, head: `<div class="fr-line">${esc(fr)}</div>`, options: [ok, ...bad], correct: 0,
    tip: "Relis la leçon : sports, repas, langues, pays et généralités → pas d'article ; métiers → a / an ; instruments et choses uniques → the." };
}
const AAT = SENT.filter(s => s[1] !== "Ø"), TZ = SENT.filter(s => s[1] === "the" || s[1] === "Ø");
const MISSIONS = [
  { id: "aan", icon: "🔤", title: "a ou an ?", desc: "Un son consonne → a, un son voyelle → an.", build: () => shuffle(AAN).slice(0, 12).map(aanQ) },
  { id: "aat", icon: "📌", title: "a, an ou the ?", desc: "Un objet quelconque ou un objet précis ?", build: () => shuffle(AAT).slice(0, 10).map(i => sentQ(i, ["a", "an", "the"], "Choisis a, an ou the")) },
  { id: "tz", icon: "🌍", title: "the ou rien ?", desc: "Précis → the ; général, sports, repas, langues, pays → Ø.", build: () => shuffle(TZ).slice(0, 10).map(i => sentQ(i, ["the", "Ø"], "the ou pas d'article ?")) },
  { id: "correct", icon: "🔎", title: "Quelle phrase est correcte ?", desc: "Repère les pièges du français : le football, la vie, médecin…", build: () => shuffle(CORRECT).slice(0, 8).map(correctQ) },
  { id: "mix", icon: "🎲", title: "Tout mélangé", desc: "a, an, the ou Ø : le grand test !", build: () => shuffle(SENT).slice(0, 12).map(i => sentQ(i, ["a", "an", "the", "Ø"], "a, an, the ou Ø ?")) }
];
