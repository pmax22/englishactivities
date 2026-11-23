/* ── Test de positionnement : diagnostic par notion (acquis / fragile / à travailler) ── */
const DATA = {}, MDEF = [];
%GENERIC%
const NOTIONS = %NOTIONS%;
const LVN = ["Novice", "Intermédiaire", "Avancé", "Expert"];
const IDK = "Je ne sais pas";
const STOP_BELOW = 0.5;           /* si un niveau entier est sous 50 %, on arrête : les niveaux suivants sont trop difficiles */
const ACQUIS = 0.8, FRAGILE = 0.5;
function buildTest() {
  const out = [];
  [0, 1, 2, 3].forEach(l => {
    const qs = [];
    NOTIONS.filter(n => n.l === l).forEach(n => n.qs.forEach(([line, opts, tip]) => {
      const order = shuffle(opts.slice()), options = order.concat(IDK);
      const fill = line.includes("____") ? line.replace("____", opts[0]).replace(/^(.)/, m => m.toUpperCase()) : opts[0];
      qs.push({ kind: "mcq", instr: "Choisis la bonne réponse · " + n.name, label: line, keepOrder: true,
        head: `<div class="fr-line">${esc(line)}</div>`, options, correct: order.indexOf(opts[0]), correctText: fill, tip: tip || "", notion: n.id, lvl: l });
    }));
    out.push(...shuffle(qs));
  });
  return out;
}
MISSIONS.push({ id: "test", icon: "🗺️", title: "Lancer le test", desc: `${NOTIONS.reduce((s, n) => s + n.qs.length, 0)} questions au maximum sur ${NOTIONS.length} notions, environ 15 minutes. Le test s'arrête plus tôt si les questions deviennent trop difficiles.`, build: buildTest });

/* Arrêt anticipé à la fin d'un niveau trop difficile */
nextQuestion = function () {
  const q = questions[qi], nx = questions[qi + 1];
  if (nx && nx.lvl !== q.lvl) {
    const r = recap.filter((x, i) => questions[i].lvl === q.lvl);
    if (r.filter(x => x.ok).length / r.length < STOP_BELOW) { questions = questions.slice(0, qi + 1); showScore(); return; }
  }
  qi++; if (qi < questions.length) renderQuestion(); else showScore();
};

const _show = showScore;
showScore = function () {
  _show();
  if (current.id !== "test") return;
  const sh = document.getElementById("sShare"); if (sh) sh.remove();
  const res = {};
  recap.forEach((r, i) => { const q = questions[i]; const o = res[q.notion] = res[q.notion] || { ok: 0, n: 0 }; o.n++; if (r.ok) o.ok++; });
  const by = [0, 1, 2, 3].map(l => { const r = recap.filter((x, i) => questions[i].lvl === l); return { ok: r.filter(x => x.ok).length, n: r.length }; });
  let lvl = 0;
  for (let l = 0; l < 4; l++) { if (by[l].n && by[l].ok / by[l].n >= 0.7) lvl = Math.min(3, l + 1); else break; }
  const rows = NOTIONS.map(n => {
    const r = res[n.id]; if (!r) return Object.assign({}, n, { pct: null, st: "ne" });
    const pct = Math.round(r.ok / r.n * 100);
    return Object.assign({}, n, { pct, st: pct >= ACQUIS * 100 ? "ac" : pct >= FRAGILE * 100 ? "fr" : "tw" });
  });
  const total = recap.length, good = recap.filter(r => r.ok).length;
  const diag = { date: Date.now(), lvl, pct: Math.round(good / total * 100), notions: rows.filter(r => r.pct != null).map(r => ({ id: r.id, name: r.name, l: r.l, pct: r.pct, st: r.st, files: r.files })) };
  try { localStorage.setItem("ea_level", JSON.stringify({ lvl, date: Date.now(), by })); localStorage.setItem("ea_diag", JSON.stringify(diag)); } catch (e) {}
  const cat = window.EA_CATALOG || [];
  const ttl = f => (cat.find(c => c.f === f) || { t: f.replace(".html", "") }).t;
  const item = r => `<div class="dg-item dg-${r.st}">
      <div class="dg-top"><span class="dg-name">${esc(r.name)}</span><span class="dg-lv">${LVN[r.l]}</span><span class="dg-pct">${r.pct}%</span></div>
      <div class="lb-track"><div class="lb-fill" style="width:${r.pct}%"></div></div>
      ${r.st !== "ac" ? `<div class="dg-links">${r.files.map(f => `<a href="${f}">${esc(ttl(f))} →</a>`).join("")}</div>` : ""}</div>`;
  const group = (st, title, help) => { const g = rows.filter(r => r.st === st).sort((a, b) => a.pct - b.pct || a.l - b.l);
    return g.length ? `<div class="dg-group"><div class="seance-title">${title} <span class="dash-count">${g.length}</span></div><p class="lvl-help">${help}</p>${g.map(item).join("")}</div>` : ""; };
  const ne = rows.filter(r => r.st === "ne");
  document.getElementById("sStars").textContent = "🗺️";
  document.getElementById("sScore").innerHTML = `${diag.pct}<span>%</span>`;
  document.getElementById("sMsg").innerHTML = `<div class="lvl-result">
    <p class="lvl-help" style="text-align:center">${good} bonnes réponses sur ${total} questions.</p>
    <div class="lvl-bars">${by.map((b, i) => `<div class="lvl-bar"><span>${LVN[i]}</span><div class="lb-track"><div class="lb-fill" style="width:${b.n ? b.ok / b.n * 100 : 0}%"></div></div><b>${b.n ? Math.round(b.ok / b.n * 100) + "%" : "—"}</b></div>`).join("")}</div>
    <p class="lvl-reco">Niveau conseillé pour t'entraîner : <b>${LVN[lvl]}</b></p>
    ${group("tw", "❌ À travailler en priorité", "Moins de 50 % de réussite : relis la leçon et fais l'activité proposée.")}
    ${group("fr", "⚠️ Fragile", "De 50 à 79 % : c'est en bonne voie, encore un peu d'entraînement pour consolider.")}
    ${group("ac", "✅ Acquis", "80 % ou plus : bravo, cette notion est maîtrisée.")}
    ${ne.length ? `<div class="dg-group"><div class="seance-title">Non évalué <span class="dash-count">${ne.length}</span></div><p class="lvl-help">Le test s'est arrêté avant ces notions plus difficiles : travaille d'abord les notions ci-dessus. ${ne.map(n => esc(n.name)).join(" · ")}</p></div>` : ""}
    <div class="dash-name" style="margin-top:18px"><input class="answer" id="dgName" placeholder="Ton prénom et ta classe" value="${esc(EA.getName())}"></div>
    <div class="dash-actions"><button class="btn btn-primary" type="button" id="dgCopy">📋 Copier mon diagnostic pour le professeur</button><a class="btn btn-ghost" href="index.html?niveau=${lvl}">Activités ${LVN[lvl]}</a></div>
    <div class="dash-bilan" id="dgOut"></div></div>`;
  document.getElementById("dgName").onchange = e => EA.setName(e.target.value);
  document.getElementById("dgCopy").onclick = e => {
    const L = st => rows.filter(r => r.st === st).map(r => `${r.name} ${r.pct}%`).join(", ") || "—";
    const txt = EA.sign(`${EA.getName() || "(prénom ?)"} — Test de niveau — ${diag.pct}% — niveau conseillé ${LVN[lvl]} — ${EA.fmtDate(Date.now())}`) +
      `\nÀ travailler : ${L("tw")}\nFragile : ${L("fr")}\nAcquis : ${L("ac")}` + (ne.length ? `\nNon évalué : ${ne.map(n => n.name).join(", ")}` : "");
    document.getElementById("dgOut").textContent = txt; EA.copy(txt, e.currentTarget);
  };
  const rc = document.getElementById("sRecap");
  rc.innerHTML = `<details class="dash-errs"><summary>Voir le détail de mes réponses</summary>${rc.innerHTML}</details>`;
};
