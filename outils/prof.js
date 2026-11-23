/* ── Espace professeur : composer un travail de la semaine + vérifier des résultats ── */
const DATA = {}, MDEF = [];
%GENERIC%
const LVN = ["Novice", "Intermédiaire", "Avancé", "Expert"];
let PICK = [];
function draw() {
  const cat = window.EA_CATALOG || [];
  const box = document.createElement("div"); box.id = "prof";
  document.getElementById("menu").appendChild(box);
  const secs = [...new Set(cat.map(c => c.s))];
  box.innerHTML = `
  <div class="seance-title">1 · Composer le travail</div>
  <div class="card pf-card">
    <label class="pf-l">Titre</label><input class="answer pf-in" id="pTitle" placeholder="Ex. : Travail de la semaine — 2nde B" value="Travail de la semaine">
    <label class="pf-l">Message aux élèves (facultatif)</label><input class="answer pf-in" id="pMsg" placeholder="Ex. : À faire avant lundi. Visez 8/10 minimum !">
    <label class="pf-l">Activités choisies <span class="dash-count" id="pCount">0</span></label>
    <div id="pSel" class="pf-sel"><p class="dash-help">Coche des activités dans la liste ci-dessous.</p></div>
    <div class="dash-actions"><button class="btn btn-primary" id="pCopy" type="button">📋 Copier le lien</button><a class="btn btn-ghost" id="pOpen" target="_blank" href="#">👁️ Aperçu élève</a></div>
    <div class="dash-bilan" id="pLink"></div>
  </div>
  <div class="card pf-card">
    <input class="search pf-search" id="pSearch" type="search" placeholder="Filtrer : prétérit, météo, CAP…">
    <div class="pf-filters"><select id="pSec"><option value="">Toutes les sections</option>${secs.map(s => `<option>${s}</option>`).join("")}</select>
    <select id="pLvl"><option value="">Tous les niveaux</option>${LVN.map((l, i) => `<option value="${i}">${l}</option>`).join("")}</select></div>
    <div id="pList" class="pf-list"></div>
  </div>
  <div class="seance-title">2 · Vérifier des résultats d'élèves</div>
  <div class="card pf-card">
    <p class="dash-help">Collez ici les lignes de résultat envoyées par les élèves (une par ligne). Le code de contrôle indique si la ligne a été modifiée à la main.</p>
    <textarea class="answer pf-ta" id="pVer" rows="5" placeholder="Léa 2nde B — Le prétérit — Mission 1 — 9/10 — 23/11/2026 14:02 — code 1A2B3"></textarea>
    <div id="pVerOut"></div>
  </div>`;
  const list = box.querySelector("#pList");
  const norm2 = s => s.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "");
  const renderList = () => {
    const q = norm2(box.querySelector("#pSearch").value), sec = box.querySelector("#pSec").value, lv = box.querySelector("#pLvl").value;
    const rows = cat.slice().sort((a, b) => a.l - b.l).filter(c => (!sec || c.s === sec) && (lv === "" || c.l === +lv) && (!q || norm2(c.t + " " + c.sub + " " + c.s + " " + (c.d || "")).includes(q)));
    list.innerHTML = rows.map(c => `<label class="pf-row"><input type="checkbox" data-f="${c.f}" ${PICK.includes(c.f) ? "checked" : ""}>
      <span class="dr-t">${esc(c.t)}</span><span class="dr-m">${c.s} · ${c.sub}</span><span class="lvl lvl-${c.l}">${LVN[c.l]}</span></label>`).join("") || `<p class="dash-help">Aucune activité.</p>`;
    list.querySelectorAll("input").forEach(i => i.onchange = () => { const f = i.dataset.f; PICK = i.checked ? PICK.concat(f) : PICK.filter(x => x !== f); renderSel(); });
  };
  const link = () => {
    const base = location.href.replace(/[^/]*$/, "");
    const p = new URLSearchParams(); p.set("t", box.querySelector("#pTitle").value.trim() || "Travail de la semaine");
    const m = box.querySelector("#pMsg").value.trim(); if (m) p.set("m", m);
    p.set("l", PICK.map(f => f.replace(/\.html$/, "")).join(","));
    return base + "devoir.html?" + p.toString();
  };
  const renderSel = () => {
    box.querySelector("#pCount").textContent = PICK.length;
    box.querySelector("#pSel").innerHTML = PICK.length ? PICK.map((f, i) => { const c = cat.find(x => x.f === f) || { t: f };
      return `<div class="pf-pick"><span class="wr-n">${i + 1}</span><span class="dr-t">${esc(c.t)}</span>
        <button type="button" data-up="${i}" title="Monter">↑</button><button type="button" data-rm="${i}" title="Retirer">✕</button></div>`; }).join("")
      : `<p class="dash-help">Coche des activités dans la liste ci-dessous.</p>`;
    box.querySelectorAll("[data-rm]").forEach(b => b.onclick = () => { PICK.splice(+b.dataset.rm, 1); renderSel(); renderList(); });
    box.querySelectorAll("[data-up]").forEach(b => b.onclick = () => { const i = +b.dataset.up; if (i > 0) { [PICK[i - 1], PICK[i]] = [PICK[i], PICK[i - 1]]; renderSel(); } });
    const l = link(); box.querySelector("#pLink").textContent = PICK.length ? l : ""; box.querySelector("#pOpen").href = l;
    try { localStorage.setItem("ea_prof_v1", JSON.stringify({ t: box.querySelector("#pTitle").value, m: box.querySelector("#pMsg").value, p: PICK })); } catch (e) {}
  };
  try { const s = JSON.parse(localStorage.getItem("ea_prof_v1") || "null"); if (s) { box.querySelector("#pTitle").value = s.t || ""; box.querySelector("#pMsg").value = s.m || ""; PICK = (s.p || []).filter(f => cat.some(c => c.f === f)); } } catch (e) {}
  ["pSearch", "pSec", "pLvl"].forEach(id => box.querySelector("#" + id).addEventListener("input", renderList));
  ["pTitle", "pMsg"].forEach(id => box.querySelector("#" + id).addEventListener("input", renderSel));
  box.querySelector("#pCopy").onclick = e => { if (!PICK.length) { box.querySelector("#pLink").textContent = "Choisissez au moins une activité."; return; } EA.copy(link(), e.currentTarget); };
  box.querySelector("#pVer").addEventListener("input", e => {
    const out = e.target.value.split("\n").map(l => l.trim()).filter(Boolean).map(l => {
      const v = EA.verify(l);
      return `<div class="recap-item"><span class="r-ic">${v === true ? "✅" : v === false ? "⚠️" : "❔"}</span><span class="r-txt">${esc(l)} <i>${v === true ? "(code valide)" : v === false ? "(code incorrect : ligne modifiée ?)" : "(pas de code)"}</i></span></div>`;
    }).join("");
    box.querySelector("#pVerOut").innerHTML = out;
  });
  renderList(); renderSel();
}
document.addEventListener("DOMContentLoaded", draw);
