/* ── Travail de la semaine (vue élève) : devoir.html?t=Titre&m=Message&l=page1,page2 ── */
const DATA = {}, MDEF = [];
%GENERIC%
function drawDevoir() {
  const p = new URLSearchParams(location.search);
  const files = (p.get("l") || "").split(",").map(s => s.trim()).filter(Boolean).map(s => s.replace(/\.html$/, "") + ".html");
  const cat = window.EA_CATALOG || [];
  const title = p.get("t") || "Travail de la semaine", msg = p.get("m") || "";
  document.querySelector("header h1").innerHTML = esc(title);
  document.title = title;
  try { if (files.length) localStorage.setItem("ea_devoir_last", location.search); } catch (e) {}
  let box = document.getElementById("dv"); if (!box) { box = document.createElement("div"); box.id = "dv"; document.getElementById("menu").appendChild(box); }
  if (!files.length) {
    let last = ""; try { last = localStorage.getItem("ea_devoir_last") || ""; } catch (e) {}
    box.innerHTML = `<div class="card pf-card"><p>Ton professeur ne t'a pas encore donné de lien de travail, ou le lien est incomplet.</p>
      ${last ? `<p><a class="btn btn-primary" href="devoir.html${esc(last)}">Reprendre mon dernier travail</a></p>` : ""}
      <p class="dash-help">Le lien ressemble à : <i>…/devoir.html?t=…&amp;l=…</i>. Demande-le à ton professeur ou cherche-le sur l'ENT.</p>
      <p><a class="btn btn-ghost" href="index.html">Voir toutes les activités</a></p></div>`;
    return;
  }
  const d = window.EA ? EA.data() : { pages: {} };
  let done = 0, pts = 0, tot = 0;
  const rows = files.map((f, i) => {
    const c = cat.find(x => x.f === f) || { t: f.replace(/\.html$/, "").replace(/_/g, " "), s: "" };
    const pg = d.pages[f], ms = pg ? Object.values(pg.missions) : [], st = EA.pageStats(f);
    if (ms.length) done++; pts += st.pct; tot += 100;
    return `<a class="dash-row dv-row ${ms.length ? "dv-done" : ""}" href="${esc(f)}"><span class="wr-n">${ms.length ? "✓" : i + 1}</span>
      <span class="dr-t">${esc(c.t)}</span><span class="dr-m">${ms.length ? `${st.done}/${st.n} mission${st.n > 1 ? "s" : ""}` : "à faire"}</span>
      <span class="dr-s ${st.pct >= 100 ? "done" : ""}">${ms.length ? st.pct + "%" : "→"}</span></a>`;
  });
  box.innerHTML = `${msg ? `<div class="doc"><div class="doc-title">✉️ Message du professeur</div><div class="doc-text"><p>${esc(msg)}</p></div></div>` : ""}
    <div class="dash-name"><input class="answer" id="dvName" placeholder="Ton prénom et ta classe" value="${esc(EA.getName())}"></div>
    <div class="dash-stats"><div><b>${done}/${files.length}</b><span>activités faites</span></div><div><b>${tot ? Math.round(pts / tot * 100) : 0}%</b><span>avancement</span></div></div>
    <p class="dash-help">Fais toutes les missions de chaque activité : le % montre ton avancement. Reviens sur cette page pour voir ton avancement (garde le lien dans tes favoris).</p>
    <div class="dash-list">${rows.join("")}</div>
    <div class="dash-actions"><button class="btn btn-primary" id="dvCopy" type="button">📋 Copier mon bilan pour le professeur</button></div>
    <div class="dash-bilan" id="dvBilan"></div>`;
  box.querySelector("#dvName").onchange = e => { EA.setName(e.target.value); drawDevoir(); };
  box.querySelector("#dvCopy").onclick = e => {
    const lines = files.map(f => { const c = cat.find(x => x.f === f), st = EA.pageStats(f);
      return `${c ? c.t : f} : ${st.done ? st.done + "/" + st.n + " missions, " + st.pct + "%" : "non fait"}`; });
    const txt = EA.sign(`${EA.getName() || "(prénom ?)"} — ${title} — ${done}/${files.length} activités — ${tot ? Math.round(pts / tot * 100) : 0}% — ${EA.fmtDate(Date.now())}`) + "\n" + lines.join("\n");
    box.querySelector("#dvBilan").textContent = txt; EA.copy(txt, e.currentTarget);
  };
}
document.addEventListener("DOMContentLoaded", drawDevoir);
window.addEventListener("pageshow", e => { if (e.persisted) drawDevoir(); });
