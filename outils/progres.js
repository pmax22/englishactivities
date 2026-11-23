/* ── Mes progrès : tableau de bord + révision des erreurs ── */
const DATA = {}, MDEF = [];
%GENERIC%
function replayable() { return (window.EA ? EA.data().errors : []).filter(e => e.q && e.q.kind); }
function reviewBuild(n) {
  return () => {
    const qs = replayable().slice(0, n).map(e => {
      if (e.q.__docs) Object.assign(DOCS_, e.q.__docs);
      return Object.assign({}, e.q, { instr: (e.q.instr || "") + " · " + e.ptitle });
    });
    return n > 10 ? shuffle(qs) : qs;
  };
}
MISSIONS.push(
  { id: "rev10", icon: "🔁", title: "Revoir mes 10 dernières erreurs", desc: "Les questions que tu as ratées récemment, toutes activités confondues.", build: reviewBuild(10) },
  { id: "revall", icon: "🎯", title: "Revoir toutes mes erreurs", desc: "Jusqu'à 30 questions mélangées. Chaque réponse juste efface l'erreur.", build: reviewBuild(30) });
if (window.EA) EA.onAnswer = (q, ok) => { if (ok && q.__page) EA.resolve(q.__page, q.label); };

const LVN = ["Novice", "Intermédiaire", "Avancé", "Expert"];
function catalogTitle(f) { const c = (window.EA_CATALOG || []).find(x => x.f === f); return c ? c.t : null; }
function diagHtml() {
  let d = null; try { d = JSON.parse(localStorage.getItem("ea_diag") || "null"); } catch (e) {}
  if (!d || !d.notions) return "";
  const cat = window.EA_CATALOG || [], ttl = f => (cat.find(c => c.f === f) || { t: f }).t;
  const row = n => `<div class="dg-item dg-${n.st}"><div class="dg-top"><span class="dg-name">${EA.esc(n.name)}</span><span class="dg-pct">${n.pct}%</span></div>
    <div class="lb-track"><div class="lb-fill" style="width:${n.pct}%"></div></div>
    <div class="dg-links">${n.files.map(f => `<a href="${f}">${EA.esc(ttl(f))} →</a>`).join("")}</div></div>`;
  const tw = d.notions.filter(n => n.st === "tw").sort((a, b) => a.pct - b.pct), fr = d.notions.filter(n => n.st === "fr"), ac = d.notions.filter(n => n.st === "ac");
  return `<div class="seance-title">Mon diagnostic <span class="dash-count">${EA.fmtDate(d.date).split(" ")[0]} · ${d.pct}%</span></div>
    <p class="dash-help">✅ ${ac.length} acquise${ac.length > 1 ? "s" : ""} · ⚠️ ${fr.length} fragile${fr.length > 1 ? "s" : ""} · ❌ ${tw.length} à travailler — <a href="test_niveau.html">refaire le test</a></p>
    ${tw.concat(fr).map(row).join("") || `<p class="dash-help">Toutes les notions testées sont acquises. Bravo !</p>`}`;
}
function drawDash() {
  if (!window.EA) return;
  let box = document.getElementById("dash"), box2 = document.getElementById("dash2");
  if (!box) {
    const menu = document.getElementById("menu");
    box = document.createElement("div"); box.id = "dash"; menu.insertBefore(box, menu.firstChild);
    box2 = document.createElement("div"); box2.id = "dash2"; menu.appendChild(box2);
  }
  const d = EA.data(), pages = Object.entries(d.pages).sort((a, b) => b[1].date - a[1].date);
  const ms = pages.flatMap(([, p]) => Object.values(p.missions));
  const pts = ms.reduce((s, m) => s + m.best, 0), tot = ms.reduce((s, m) => s + m.total, 0);
  const perfect = ms.filter(m => m.best === m.total).length;
  const errs = d.errors, rep = replayable().length;
  let lvl = null; try { lvl = JSON.parse(localStorage.getItem("ea_level") || "null"); } catch (e) {}
  const name = EA.getName();
  box.innerHTML = `
  <div class="dash-name"><input class="answer" id="dName" placeholder="Ton prénom et ta classe" value="${EA.esc(name)}"></div>
  <div class="dash-stats">
    <div><b>${pages.length}</b><span>activités</span></div>
    <div><b>${ms.length}</b><span>missions</span></div>
    <div><b>${tot ? Math.round(pts / tot * 100) : 0}%</b><span>réussite</span></div>
    <div><b>${perfect}</b><span>sans-faute</span></div>
  </div>
  ${lvl ? `<p class="dash-lvl">🗺️ Niveau conseillé par le test : <b>${LVN[lvl.lvl]}</b> · <a href="index.html?niveau=${lvl.lvl}">voir les activités de ce niveau</a></p>`
        : `<p class="dash-lvl">🗺️ Tu ne sais pas par où commencer ? <a href="test_niveau.html">Fais le test de niveau</a>.</p>`}
  ${diagHtml()}
  <div class="seance-title">Mes erreurs à retravailler <span class="dash-count">${errs.length}</span></div>
  ${errs.length ? `<p class="dash-help">${rep ? "Lance une mission ci-dessous : chaque bonne réponse efface l'erreur de la liste." : ""}</p>
    <details class="dash-errs"><summary>Voir la liste</summary>${errs.slice(0, 40).map(e => `<div class="recap-item"><span class="r-ic">❌</span><span class="r-txt">${EA.esc(e.label)} → <b>${EA.esc(e.correct)}</b> <i>(${EA.esc(catalogTitle(e.page) || e.ptitle)})</i></span></div>`).join("")}</details>`
    : `<p class="dash-help">Aucune erreur à revoir. Bravo !</p>`}`;
  box2.innerHTML = `
  ${pages.length ? `<div class="seance-title">Mes activités</div><div class="dash-list">${pages.map(([f, p]) => {
      const st = EA.pageStats(f);
      return `<a class="dash-row" href="${EA.esc(f)}"><span class="dr-t">${EA.esc(catalogTitle(f) || p.title)}</span>
        <span class="dr-m">${st.done}/${st.n} mission${st.n > 1 ? "s" : ""} · ${EA.fmtDate(p.date).split(" ")[0]}</span>
        <span class="dr-s ${st.pct >= 100 ? "done" : ""}">${st.pct}%</span></a>`;
    }).join("")}</div>` : `<p class="dash-empty">Tu n'as encore fait aucune activité. <a href="index.html">Choisis une activité</a> : tes scores apparaîtront ici.</p>`}
  <div class="dash-actions">
    <button class="btn btn-primary" id="dCopy" type="button">📋 Copier mon bilan pour le professeur</button>
    <button class="btn btn-ghost" id="dReset" type="button">🗑️ Tout effacer</button>
  </div>
  <div class="dash-bilan" id="dBilan"></div>`;
  box.querySelector("#dName").onchange = e => { EA.setName(e.target.value); drawDash(); };
  box2.querySelector("#dCopy").onclick = e => {
    const lines = pages.map(([f, p]) => {
      const st = EA.pageStats(f);
      return `${catalogTitle(f) || p.title} : ${st.done}/${st.n} missions, ${st.pct}%`;
    });
    const txt = EA.sign(`${EA.getName() || "(prénom ?)"} — Bilan — ${pages.length} activités, ${ms.length} missions, ${tot ? Math.round(pts / tot * 100) : 0}% — ${EA.fmtDate(Date.now())}`)
      + (lines.length ? "\n" + lines.join("\n") : "");
    box2.querySelector("#dBilan").textContent = txt;
    EA.copy(txt, e.currentTarget);
  };
  const rb = box2.querySelector("#dReset");
  rb.onclick = () => {
    if (rb.dataset.sure) { EA.reset(); drawDash(); renderMenu(); return; }
    rb.dataset.sure = "1"; rb.textContent = "⚠️ Clique encore pour confirmer"; setTimeout(() => { delete rb.dataset.sure; rb.textContent = "🗑️ Tout effacer"; }, 4000);
  };
  const mb = document.getElementById("missions");
  mb.style.display = rep ? "" : "none";
}
document.addEventListener("DOMContentLoaded", drawDash);
window.addEventListener("load", () => { const o = window.showMenu; window.showMenu = function () { o(); drawDash(); }; });
