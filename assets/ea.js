/* English Activities — socle commun : progrès, erreurs, résultat à partager, impression, hors connexion.
   Tout est stocké dans le navigateur de l'élève (localStorage) : aucune donnée n'est envoyée. */
(function () {
  const KEY = "ea_progress_v1", NAME = "ea_name";
  const PAGE = decodeURIComponent(location.pathname.split("/").pop() || "index.html");

  function load() {
    try { const d = JSON.parse(localStorage.getItem(KEY) || "null"); if (d && d.pages && d.errors) return d; } catch (e) {}
    return { pages: {}, errors: [] };
  }
  function save(d) { try { localStorage.setItem(KEY, JSON.stringify(d)); } catch (e) {} }
  function pageTitle() {
    const h = document.querySelector("header h1");
    return (h ? h.textContent : document.title).replace(/\s+/g, " ").trim();
  }
  function clean(q) {
    try { return JSON.parse(JSON.stringify(q)); } catch (e) { return null; }
  }
  function hash(s) {
    let h = 2166136261;
    for (let i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619); }
    return (h >>> 0).toString(36).toUpperCase().slice(0, 5).padStart(5, "0");
  }
  function fmtDate(t) {
    const d = new Date(t);
    return d.toLocaleDateString("fr-FR") + " " + d.toLocaleTimeString("fr-FR", { hour: "2-digit", minute: "2-digit" });
  }
  function esc(s) { return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;"); }

  const EA = {
    PAGE,
    data: load,
    getName() { try { return localStorage.getItem(NAME) || ""; } catch (e) { return ""; } },
    setName(n) { try { localStorage.setItem(NAME, n.trim()); } catch (e) {} },

    /* Enregistre le résultat d'une mission et les erreurs commises */
    record(missionId, missionTitle, score, total, wrongs) {
      if (PAGE === "progres.html" || PAGE === "test_niveau.html") return;
      const d = load();
      const p = d.pages[PAGE] = d.pages[PAGE] || { missions: {} };
      p.title = pageTitle(); p.date = Date.now();
      const m = p.missions[missionId] = p.missions[missionId] || {};
      m.title = missionTitle; m.last = score; m.total = total; m.best = Math.max(m.best || 0, score);
      m.attempts = (m.attempts || 0) + 1; m.date = Date.now();
      (wrongs || []).forEach(q => {
        if (!q || !q.label) return;
        d.errors = d.errors.filter(e => !(e.page === PAGE && e.label === q.label));
        const c = q.kind ? clean(q) : null;
        if (c && PAGE !== "progres.html") c.__page = PAGE;
        d.errors.unshift({ page: PAGE, ptitle: p.title, label: q.label, correct: q.correctText || q.correct || q.answer || "", q: c, date: Date.now() });
      });
      d.errors = d.errors.slice(0, 120);
      save(d);
    },
    /* Une erreur revue et réussie disparaît de la liste */
    resolve(page, label) {
      const d = load();
      d.errors = d.errors.filter(e => !(e.page === page && e.label === label));
      save(d);
    },
    reset() { save({ pages: {}, errors: [] }); },

    /* Code de contrôle : le professeur peut vérifier qu'une ligne de résultat n'a pas été modifiée (prof.html) */
    sign(text) { return text + " — code " + hash("ea1|" + text.replace(/\s+/g, " ").trim()); },
    verify(line) {
      const m = String(line).trim().match(/^(.*) — code ([0-9A-Z]{5})$/);
      return m ? hash("ea1|" + m[1].replace(/\s+/g, " ").trim()) === m[2] : null;
    },
    fmtDate, esc, pageTitle,
    copy(text, btn) {
      const label = btn ? btn.textContent : "";
      const done = () => { if (btn) { btn.textContent = "✅ Copié"; setTimeout(() => btn.textContent = label, 1500); } };
      try { navigator.clipboard.writeText(text).then(done, () => { fallback(); done(); }); } catch (e) { fallback(); done(); }
      function fallback() { const t = document.createElement("textarea"); t.value = text; document.body.appendChild(t); t.select(); try { document.execCommand("copy"); } catch (e) {} t.remove(); }
    },

    /* Panneau affiché sous le score */
    afterScore(o) {
      EA.record(o.id, o.title, o.score, o.total, o.wrongs);
      const host = document.getElementById("sShare") || (() => {
        const r = document.getElementById("sRecap"); if (!r) return null;
        const div = document.createElement("div"); div.id = "sShare"; r.parentNode.insertBefore(div, r); return div;
      })();
      if (!host) return;
      const t = Date.now();
      const draw = () => {
        const name = EA.getName();
        const text = EA.sign(`${name || "(prénom ?)"} — ${pageTitle()} — ${o.title} — ${o.score}/${o.total} — ${fmtDate(t)}`);
        host.innerHTML = `<div class="ea-share">
          <div class="ea-share-title">📤 Mon résultat à montrer au professeur</div>
          <div class="ea-share-row"><input id="eaName" class="answer" placeholder="Ton prénom et ta classe" value="${esc(name)}">
          <button class="btn btn-primary" id="eaCopy" type="button">📋 Copier</button></div>
          <div class="ea-share-text" id="eaText">${esc(text)}</div>
          <div class="ea-share-hint">Colle ce texte dans l'ENT, ou montre cet écran au professeur. Tes résultats sont aussi dans <a href="progres.html">📈 Mes progrès</a>.</div></div>`;
        host.querySelector("#eaName").addEventListener("change", e => { EA.setName(e.target.value); draw(); });
        if (o.score < o.total) host.querySelector(".ea-share-hint").insertAdjacentHTML("beforeend", " Tes erreurs sont enregistrées : tu pourras les retravailler dans « Revoir mes erreurs ».");
        host.querySelector("#eaCopy").onclick = e => EA.copy(host.querySelector("#eaText").textContent, e.currentTarget);
      };
      draw();
    }
  };
  window.EA = EA;

  /* ── Styles communs (panneau de résultat, impression, barre d'outils) ── */
  const css = `
  .ea-share { margin-top: 18px; padding: 14px 16px; border: 1px solid var(--border, #2a2d3a); border-radius: 14px; background: var(--surface2, #1e2029); }
  .ea-share-title { font-weight: 600; font-size: 14px; margin-bottom: 10px; }
  .ea-share-row { display: flex; gap: 8px; }
  .ea-share-row input { flex: 1; font-size: 15px !important; padding: 10px 14px !important; }
  .ea-share-text { margin-top: 10px; font-size: 13px; color: var(--muted, #8a8ea3); word-break: break-word; }
  .ea-share-hint { margin-top: 6px; font-size: 12px; color: var(--muted, #8a8ea3); }
  .ea-share-hint a { color: var(--accent, #f5c842); }
  .ea-print { float: right; margin: -4px 0 6px 10px; font-size: 12px; padding: 6px 12px; border-radius: 999px; cursor: pointer;
    background: transparent; color: var(--muted, #8a8ea3); border: 1px solid var(--border, #2a2d3a); font-family: inherit; }
  .ea-print:hover { color: var(--text, #fff); }
  .ea-top { display: flex; gap: 8px; flex-wrap: wrap; }
  .ea-top a { color: var(--muted, #8a8ea3); text-decoration: none; font-size: 13px; padding: 6px 12px; border: 1px solid var(--border, #2a2d3a); border-radius: 999px; }
  .ea-top a:hover { color: var(--text, #fff); }
  @media print {
    body.ea-printing { background: #fff !important; color: #000 !important; padding: 0 !important; }
    body.ea-printing * { color: #000 !important; background: transparent !important; border-color: #999 !important; box-shadow: none !important; animation: none !important; opacity: 1 !important; transform: none !important; }
    body.ea-printing > *:not(header):not(#menu):not(section) { display: none !important; }
    body.ea-printing #menu > *:not(details.lesson) { display: none !important; }
    body.ea-printing .ea-print, body.ea-printing summary::after { display: none !important; }
    body.ea-printing header .tag { display: none !important; }
    body.ea-printing details.lesson { border: none !important; }
    body.ea-printing .lesson-body { color: #000 !important; font-size: 12pt; }
    body.ea-printing h1 span, body.ea-printing .hl { font-weight: 700; }
    body.ea-printing table { border-collapse: collapse; }
    body.ea-printing td, body.ea-printing th { border: 1px solid #999 !important; }
  }`;
  const st = document.createElement("style"); st.textContent = css; document.head.appendChild(st);

  document.addEventListener("DOMContentLoaded", () => {
    /* Bouton « Imprimer la fiche » dans le rappel de leçon */
    const lesson = document.querySelector("details.lesson .lesson-body");
    const sum = document.querySelector("details.lesson summary");
    if (lesson && sum && /leçon/i.test(sum.textContent) && !document.querySelector(".ea-print")) {
      const b = document.createElement("button"); b.type = "button"; b.className = "ea-print"; b.textContent = "🖨️ Imprimer la fiche";
      b.onclick = () => {
        document.querySelectorAll("details.lesson").forEach(d => d.open = true);
        document.body.classList.add("ea-printing"); window.print();
        setTimeout(() => document.body.classList.remove("ea-printing"), 500);
      };
      lesson.prepend(b);
    }
    /* Liens rapides à côté du retour à l'index */
    const nav = document.querySelector("nav.topnav");
    if (nav && !nav.querySelector(".ea-top") && PAGE !== "index.html") {
      nav.style.display = "flex"; nav.style.justifyContent = "space-between"; nav.style.alignItems = "center"; nav.style.gap = "8px"; nav.style.flexWrap = "wrap";
      const box = document.createElement("div"); box.className = "ea-top";
      box.innerHTML = PAGE === "progres.html" ? "" : `<a href="progres.html">📈 Mes progrès</a>`;
      nav.appendChild(box);
    }
  });

  /* ── Hors connexion ── */
  if ("serviceWorker" in navigator && location.protocol === "https:") {
    window.addEventListener("load", () => { navigator.serviceWorker.register("sw.js").catch(() => {}); });
  }
})();
