/* Format générique : DATA = { clé: { kind: "gap" | "choice" | "order", instr, items: [...] } }
   gap    : { line: "She ____ in a shop.", ans: [...], hint, fr, tip, sign }
   choice : { line?: "…____…", fr?, big?, opts: [bonne, fausses…], keep, grid, tip }   (bonne réponse = opts[c || 0])
   order  : { en: "I|am going to|visit|London.", fr, trap, tip, alts }
   MDEF   : [{ id, icon, title, desc, from: [clés], n, group }] */
const CAN_SPEAK = typeof window !== "undefined" && "speechSynthesis" in window;
function speak(t) {
  try { const u = new SpeechSynthesisUtterance(t); u.lang = "en-GB"; u.rate = 0.85; speechSynthesis.cancel(); speechSynthesis.speak(u); } catch (e) {}
}
document.addEventListener("click", e => { const b = e.target.closest(".say"); if (b) speak(b.dataset.say); });
function sayBtn(t, label) { return `<button class="say" type="button" data-say="${esc(t)}">🔊 ${label || "Écouter"}</button>`; }
const DOCS_ = typeof DOCS !== "undefined" ? DOCS : {};
function speakLines(lines) {
  try {
    speechSynthesis.cancel();
    const voices = speechSynthesis.getVoices().filter(v => /^en(-|_)/i.test(v.lang));
    const speakers = [];
    lines.forEach(l => {
      const m = l.match(/^([A-Z][\w ]{0,20}):\s*(.*)$/);
      const who = m ? m[1] : "", text = m ? m[2] : l;
      if (who && !speakers.includes(who)) speakers.push(who);
      const k = Math.max(0, speakers.indexOf(who));
      const u = new SpeechSynthesisUtterance(text); u.lang = "en-GB"; u.rate = 0.85;
      if (voices.length > 1) u.voice = voices[k % voices.length]; else u.pitch = k % 2 ? 1.35 : 0.9;
      speechSynthesis.speak(u);
    });
  } catch (e) {}
}
document.addEventListener("click", e => { const b = e.target.closest(".say-doc"); if (b) speakLines(DOCS_[b.dataset.doc].lines); });
function docBox(id) {
  const d = DOCS_[id]; if (!d) return "";
  const body = d.lines.map(l => l.startsWith("## ") ? `<h4 class="doc-h">${esc(l.slice(3))}</h4>` :
    `<p>${d.fold ? esc(l).replace(/\*\*(.+?)\*\*/g, "<b>$1</b>") : esc(l).replace(/^([A-Z][\w ]{0,20}):/, "<b>$1 :</b>")}</p>`).join("");
  if (d.fold) return `<details class="doc doc-fold"><summary>📖 ${esc(d.title)}</summary><div class="doc-text">${body}</div></details>`;
  if (d.audio) return `<div class="doc"><div class="doc-title">🎧 ${esc(d.title)}</div>
    <button class="say say-doc" type="button" data-doc="${id}">🔊 Écouter le document</button>
    <details class="transcript"><summary>Afficher le texte (seulement si tu bloques)</summary>${body}</details></div>`;
  return `<div class="doc"><div class="doc-title">📄 ${esc(d.title)}</div><div class="doc-text">${body}</div></div>`;
}
function headOf(it) {
  if (it.doc) return docBox(it.doc) + (it.fr ? `<div class="fr-line">${esc(it.fr)}</div>` : "");
  if (it.listen) return `<div class="listen-box">${sayBtn(it.say, "Écouter le mot")}${CAN_SPEAK ? "" : `<div class="big-word">${esc(it.say)}</div>`}</div>`;
  return (it.fr ? `<div class="fr-line">${esc(it.fr)}</div>` : "") +
    (it.say ? `<div class="say-row">${sayBtn(it.say)}</div>` : "") +
    (it.big ? `<div class="big-word">${esc(it.big)}</div>` + (it.bigsub ? `<div class="big-sub">${esc(it.bigsub)}</div>` : "") : "");
}
function gapQ(it, instr) {
  const [pre, post] = it.line.split("____");
  const w = it.w || Math.min(420, Math.max(110, 13 * Math.max(...it.ans.map(a => a.length)) + 50));
  return { kind: "gap", instr: it.instr || instr, label: it.fr || it.line, sign: it.sign,
    head: headOf(it), parts: [pre, { answers: it.ans, width: w, hint: it.hint }, post],
    correct: (pre + it.ans[0] + post).trim(), tip: it.tip || "" };
}
function choiceQ(it, instr) {
  let c = it.c || 0, opts = it.opts;
  const line = it.line;
  if (it.keep) { const good = opts[c]; opts = opts.slice().sort((a, b) => a.localeCompare(b)); c = opts.indexOf(good); }
  const fill = line && line.includes("____") ? line.replace("____", opts[c]).replace(/^(.)/, m => m.toUpperCase()) : null;
  return { kind: "mcq", grid: it.grid || (opts.every(o => o.length <= 12) && opts.length <= 4 ? opts.length : undefined),
    keepOrder: !!it.keep, instr: it.instr || instr, label: it.fr || line || it.big,
    head: headOf(it) + (line ? `<div class="fr-line">${esc(line)}</div>` : ""),
    options: opts, correct: c, correctText: fill || undefined, tip: it.tip || "" };
}
function orderQ(it, instr) {
  const answer = it.en.replace(/\|/g, " ");
  const tiles = (it.en.includes("|") ? it.en.split("|") : it.en.split(" ")).map(t => t.replace(/[.?!]$/, "")).filter(Boolean);
  return { kind: "order", instr: it.instr || instr, label: it.fr || answer, head: headOf(it),
    tiles, distractors: it.trap ? [].concat(it.trap) : [], answer, alts: it.alts, tip: it.tip || "" };
}
function matchQ(it, instr) {
  return { kind: "match", instr: it.instr || instr, label: it.label || it.pairs.map(p => p[0]).join(", "), head: headOf(it),
    pairs: it.pairs, correct: it.pairs.map(p => p[0] + " = " + p[1]).join(" · "), tip: it.tip || "" };
}
const BUILD = { gap: gapQ, choice: choiceQ, order: orderQ, match: matchQ };
const MISSIONS = MDEF.map(m => Object.assign({}, m, {
  build: () => (m.ordered ? (x => x) : shuffle)(m.from.flatMap(k => DATA[k].items.map(it => [it, DATA[k]])))
    .slice(0, m.n || 10).map(([it, d]) => BUILD[it.kind || d.kind](it, d.instr))
}));
