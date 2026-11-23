/* Adjectifs — Niveau 1 : place de l'adjectif · Niveau 2 : ordre des adjectifs */
const N1 = "Niveau 1 · La place de l'adjectif", N2 = "Niveau 2 · L'ordre des adjectifs";
// Phrases à remettre dans l'ordre [français, anglais, piège éventuel]
const L1_SENT = [
  ["Je suis gentil(le).", "I am nice"], ["J'ai une sœur gentille.", "I have a nice sister"], ["Elle a un gros chien.", "She has a big dog"],
  ["Ils habitent dans une petite maison.", "They live in a small house"], ["C'est une voiture rouge.", "It is a red car"],
  ["Mon frère est grand.", "My brother is tall"], ["Nous avons un jardin magnifique.", "We have a beautiful garden"],
  ["Il porte des chaussures noires.", "He wears black shoes", "blacks"], ["Le film est intéressant.", "The film is interesting"],
  ["J'ai deux chats noirs.", "I have two black cats", "blacks"], ["C'est un livre intéressant.", "It is an interesting book"],
  ["Ma mère a les yeux bleus.", "My mother has blue eyes", "blues"], ["Tom a un vélo neuf.", "Tom has a new bike"],
  ["Ils ont des enfants heureux.", "They have happy children", "happys"]
];
// Groupes nominaux [français, déterminant, adjectif, nom, pluriel ?, lexique]
const L1_NP = [
  ["un chat noir", "a", "black", "cat", 0, "chat = cat · noir = black"], ["une grande maison", "a", "big", "house", 0, "maison = house · grand = big"],
  ["un livre intéressant", "an", "interesting", "book", 0, "livre = book · intéressant = interesting"], ["des fleurs rouges", "", "red", "flowers", 1, "fleurs = flowers · rouge = red"],
  ["un garçon timide", "a", "shy", "boy", 0, "garçon = boy · timide = shy"], ["une vieille voiture", "an", "old", "car", 0, "voiture = car · vieux = old"],
  ["des chaussures neuves", "", "new", "shoes", 1, "chaussures = shoes · neuf = new"], ["un film drôle", "a", "funny", "film", 0, "film = film · drôle = funny"],
  ["une jolie robe", "a", "pretty", "dress", 0, "robe = dress · joli = pretty"], ["une pomme verte", "a", "green", "apple", 0, "pomme = apple · vert = green"],
  ["deux chiens méchants", "two", "nasty", "dogs", 1, "chien = dog · méchant = nasty"], ["des élèves gentils", "", "nice", "students", 1, "élève = student · gentil = nice"],
  ["une longue journée", "a", "long", "day", 0, "journée = day · long = long"], ["trois petits oiseaux", "three", "small", "birds", 1, "oiseau = bird · petit = small"]
];
const np = (d, a, n) => (d ? d + " " : "") + a + " " + n;

// Niveau 2 — catégories
const CATS = ["Opinion", "Taille", "Âge", "Forme", "Couleur", "Origine", "Matière"];
const CAT_FR = { Opinion: "ce que j'en pense", Taille: "la taille", "Âge": "l'âge", Forme: "la forme", Couleur: "la couleur", Origine: "l'origine", "Matière": "la matière" };
const ADJ_CAT = [
  ["beautiful","Opinion"],["lovely","Opinion"],["ugly","Opinion"],["delicious","Opinion"],["nice","Opinion"],["horrible","Opinion"],
  ["big","Taille"],["small","Taille"],["tiny","Taille"],["huge","Taille"],["long","Taille"],["little","Taille"],
  ["old","Âge"],["new","Âge"],["young","Âge"],["ancient","Âge"],
  ["round","Forme"],["square","Forme"],["oval","Forme"],["rectangular","Forme"],
  ["red","Couleur"],["blue","Couleur"],["black","Couleur"],["green","Couleur"],["brown","Couleur"],
  ["French","Origine"],["Italian","Origine"],["Chinese","Origine"],["English","Origine"],["American","Origine"],["Swiss","Origine"],
  ["wooden","Matière"],["cotton","Matière"],["plastic","Matière"],["leather","Matière"],["metal","Matière"],["silk","Matière"],["woollen","Matière"]
];
const CAT_OF = Object.fromEntries(ADJ_CAT);
// [français, adjectifs dans le bon ordre, nom, déterminant ('' = pluriel sans article)]
const L2_NP = [
  ["une belle vieille voiture italienne", ["beautiful", "old", "Italian"], "car", "a"],
  ["une grande table ronde en bois", ["big", "round", "wooden"], "table", "a"],
  ["un joli petit chat noir", ["lovely", "little", "black"], "cat", "a"],
  ["un vieux pull rouge en laine", ["old", "red", "woollen"], "jumper", "a"],
  ["de délicieuses pommes vertes françaises", ["delicious", "green", "French"], "apples", ""],
  ["un grand sac marron en cuir", ["big", "brown", "leather"], "bag", "a"],
  ["une nouvelle montre suisse en métal", ["new", "Swiss", "metal"], "watch", "a"],
  ["une jolie robe bleue en soie", ["pretty", "blue", "silk"], "dress", "a"],
  ["un petit vase chinois ancien", ["small", "ancient", "Chinese"], "vase", "a"],
  ["une affreuse vieille chaise en plastique", ["ugly", "old", "plastic"], "chair", "a"],
  ["un énorme chien noir", ["huge", "black"], "dog", "a"],
  ["une gentille jeune fille anglaise", ["nice", "young", "English"], "girl", "a"],
  ["un long manteau noir en cuir", ["long", "black", "leather"], "coat", "a"],
  ["de beaux grands arbres verts", ["beautiful", "tall", "green"], "trees", ""]
];
CAT_OF.pretty = "Opinion"; CAT_OF.tall = "Taille";
function art(det, first) { return det === "" ? "" : /^[aeiou]/i.test(first) ? "an" : "a"; }
function phrase(adjs, noun, det) { const a = art(det, adjs[0]); return (a ? a + " " : "") + adjs.join(" ") + " " + noun; }
function orderTip(adjs) { return "Ordre : " + adjs.map(a => `${a} (<b>${CAT_OF[a] || "?"}</b>)`).join(" → ") + "."; }

/* Niveau 1 */
function l1Order(it) {
  const [fr, en, trap] = it;
  return { kind: "order", instr: "Remets les mots dans l'ordre", label: fr, head: `<div class="fr-line">${esc(fr)}</div>`,
    tiles: en.split(" "), distractors: trap ? [trap] : [], answer: en,
    tip: trap ? `L'adjectif est <b>invariable</b> : pas de -s au pluriel (<s>${trap}</s>).` : "L'adjectif se place <b>avant</b> le nom (a nice sister) ou après le verbe be (I am nice)." };
}
function l1Choice(it) {
  const [fr, d, a, n, pl] = it;
  const ok = np(d, a, n);
  const opts = [ok, (d ? d + " " : "") + n + " " + a];
  if (pl) opts.push(np(d, a + "s", n));
  return { kind: "mcq", instr: "Quelle traduction est correcte ?", label: fr, head: `<div class="fr-line">${esc(fr)}</div>`,
    options: opts, correct: 0, tip: "En anglais, l'adjectif se place <b>avant</b> le nom et il est <b>invariable</b> (pas de -s, pas de -e)." };
}
function l1Type(it) {
  const [fr, d, a, n, pl, lex] = it;
  return { kind: "gap", instr: "Traduis le groupe de mots", label: fr, head: `<div class="fr-line">${esc(fr)}</div>`,
    parts: [{ answers: [np(d, a, n)], width: 300 }], foot: `<p class="small-hint">Lexique : <b>${esc(lex)}</b></p>`,
    correct: np(d, a, n), tip: "Adjectif <b>avant</b> le nom, sans -s ni -e." + (d === "an" ? " Et <b>an</b> devant un son voyelle !" : ""),
    diagnose(vals) {
      const t = norm(vals[0]);
      if (t === norm((d ? d + " " : "") + n + " " + a)) return "En anglais, l'adjectif se place <b>avant</b> le nom.";
      if (t.includes(a + "s ")) return "L'adjectif est <b>invariable</b> : pas de -s au pluriel.";
      if (d === "an" && t.startsWith("a ")) return "Devant un son voyelle, on utilise <b>an</b>.";
      return null;
    } };
}
/* Niveau 2 */
function l2Cat(it) {
  const [a, c] = it;
  return { kind: "mcq", grid: 4, keepOrder: true, instr: "À quelle catégorie appartient cet adjectif ?", label: a,
    head: `<div class="big-word">${esc(a)}</div>`, options: CATS, correct: CATS.indexOf(c), correctText: `${a} → ${c}`,
    tip: `${a} indique ${CAT_FR[c]}.` };
}
function l2Order(it) {
  const [fr, adjs, noun, det] = it, ok = phrase(adjs, noun, det);
  return { kind: "order", instr: "Remets les adjectifs dans l'ordre", label: fr, head: `<div class="fr-line">${esc(fr)}</div>`,
    tiles: ok.split(" "), distractors: [], answer: ok, tip: orderTip(adjs) };
}
function l2Choice(it) {
  const [fr, adjs, noun, det] = it, ok = phrase(adjs, noun, det);
  const perms = [];
  const sw = (arr, i, j) => { const b = arr.slice(); [b[i], b[j]] = [b[j], b[i]]; return b; };
  [[0, 1], [1, 2], [0, 2]].forEach(([i, j]) => { if (j < adjs.length) perms.push(phrase(sw(adjs, i, j), noun, det)); });
  const opts = [ok].concat(shuffle(perms.filter(p => p !== ok)).slice(0, 2));
  return { kind: "mcq", instr: "Quel est le bon ordre ?", label: fr, head: `<div class="fr-line">${esc(fr)}</div>`,
    options: opts, correct: 0, tip: orderTip(adjs) };
}
const MISSIONS = [
  { group: N1, id: "n1order", icon: "🧩", title: "Remets dans l'ordre", desc: "I am nice · I have a nice sister : où va l'adjectif ?", build: () => shuffle(L1_SENT).slice(0, 10).map(l1Order) },
  { group: N1, id: "n1choice", icon: "🔎", title: "Quelle traduction est correcte ?", desc: "a black cat ou a cat black ?", build: () => shuffle(L1_NP).slice(0, 8).map(l1Choice) },
  { group: N1, id: "n1type", icon: "✍️", title: "Traduis", desc: "Écris le groupe en anglais avec le lexique donné.", build: () => shuffle(L1_NP).slice(0, 8).map(l1Type) },
  { group: N2, id: "n2cat", icon: "🏷️", title: "Quelle catégorie ?", desc: "Opinion, taille, âge, forme, couleur, origine ou matière ?", build: () => shuffle(ADJ_CAT).slice(0, 12).map(l2Cat) },
  { group: N2, id: "n2order", icon: "🧩", title: "Remets les adjectifs dans l'ordre", desc: "a beautiful old Italian car : construis le groupe de mots.", build: () => shuffle(L2_NP).slice(0, 8).map(l2Order) },
  { group: N2, id: "n2choice", icon: "📐", title: "Quel est le bon ordre ?", desc: "Choisis le groupe de mots où les adjectifs sont bien rangés.", build: () => shuffle(L2_NP).slice(0, 8).map(l2Choice) }
];
