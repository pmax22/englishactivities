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
    /* Avancement d'une activité : moyenne de la meilleure réussite de chaque mission, missions non faites = 0 */
    pageStats(file) {
      const pg = load().pages[file], ms = pg ? Object.values(pg.missions) : [];
      const c = (window.EA_CATALOG || []).find(x => x.f === file);
      const n = Math.max(c && c.m || 0, ms.length) || 1;
      const sum = ms.reduce((s, m) => s + (m.total ? Math.min(1, m.best / m.total) : 0), 0);
      return { done: ms.length, n, pct: Math.round(sum / n * 100) };
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

  /* ── Confort de lecture (DYS) : réglages enregistrés sur l'appareil ── */
  const CKEY = "ea_confort_v1";
  const OPTS = [
    ["big", "Texte plus grand", "Agrandit tout le texte de la page."],
    ["air", "Texte aéré", "Plus d'espace entre les lettres, les mots et les lignes. Plus d'italique ni de mots en majuscules."],
    ["luc", "Police Luciole", "Une police conçue pour une lecture facilitée."],
    ["light", "Fond clair", "Texte foncé sur fond clair au lieu du fond sombre."],
    ["trall", "Toujours afficher les traductions", "Les exemples des leçons sont traduits en français sans avoir à cliquer sur « FR »."]
  ];
  function cload() { try { return JSON.parse(localStorage.getItem(CKEY) || "{}") || {}; } catch (e) { return {}; } }
  function capply(c) { OPTS.forEach(([k]) => document.documentElement.classList.toggle("ea-" + k, !!c[k])); }
  capply(cload());
  const ccss = `
  @font-face { font-family: "Luciole"; src: url("assets/luciole-regular.woff2") format("woff2"); font-weight: 400; font-style: normal; font-display: swap; }
  @font-face { font-family: "Luciole"; src: url("assets/luciole-bold.woff2") format("woff2"); font-weight: 600 900; font-style: normal; font-display: swap; }
  html.ea-big body { zoom: 1.2; }
  html.ea-air body, html.ea-air body *, html.ea-air body *::before, html.ea-air body *::after { letter-spacing: .06em !important; word-spacing: .16em !important; font-style: normal !important; text-transform: none !important; }
  html.ea-air body { line-height: 1.7 !important; }
  html.ea-air body :is(p, li, td, th, dd, label, blockquote, .lesson-body, .lesson-body *, .q-text, .prompt, .tip, .why, .fb, .feedback, .sub) { line-height: 1.75 !important; }
  html.ea-air body :is(p, li) + :is(p, li) { margin-top: .5em; }
  html.ea-luc body, html.ea-luc body *:not(svg):not(svg *) { font-family: "Luciole", "DM Sans", sans-serif !important; }
  html.ea-light { filter: invert(1) hue-rotate(180deg); background: #0e0f14; }
  html.ea-light :is(img, video, picture, canvas, iframe, .ea-noinv) { filter: invert(1) hue-rotate(180deg); }
  .lesson-body .tr, .lesson-body .tr-line { color: #c4b5fd; }
  .lesson-body .tr { display: none; font-style: normal !important; font-size: .95em; }
  .lesson-body .tr.open, html.ea-trall .lesson-body .tr { display: inline; }
  .lesson-body .tr.tr-block.open, html.ea-trall .lesson-body .tr.tr-block { display: block; margin: -2px 0 8px; }
  .lesson-body .tr::before { content: "→ "; }
  .tr-btn { font: inherit; font-style: normal !important; font-size: 11px; font-weight: 700; letter-spacing: .03em; color: var(--muted, #8a8ea3); background: transparent; border: 1px solid var(--border, #2a2d3a); border-radius: 6px; padding: 1px 6px; margin-left: 6px; cursor: pointer; vertical-align: 1px; }
  .tr-btn { color: #c4b5fd; border-color: rgba(196,181,253,.45); }
  .tr-btn:hover, .tr-btn[aria-expanded="true"] { color: #fff; border-color: #c4b5fd; background: rgba(196,181,253,.15); }
  html.ea-trall .tr-btn { display: none; }
  @media print { .lesson-body .tr { display: inline !important; } .lesson-body .tr.tr-block { display: block !important; } .tr-btn { display: none !important; } }
  .ea-cbtn { font: inherit; font-size: 13px; color: var(--muted, #8a8ea3); background: transparent; padding: 6px 12px; border: 1px solid var(--border, #2a2d3a); border-radius: 999px; cursor: pointer; }
  .ea-cbtn:hover { color: var(--text, #fff); }
  .ea-cbtn b { font-weight: 700; margin-right: 4px; }
  .ea-top { display: flex; gap: 8px; flex-wrap: wrap; }
  .ea-top.ea-float { justify-content: flex-end; padding: 12px 14px 0; position: relative; z-index: 50; }
  .ea-cov { position: fixed; inset: 0; background: rgba(0,0,0,.6); z-index: 9999; display: flex; align-items: center; justify-content: center; padding: 16px; }
  .ea-cbox { background: var(--surface, #16181f); color: var(--text, #e8eaf0); border: 1px solid var(--border, #2a2d3a); border-radius: 16px; max-width: 440px; width: 100%; max-height: 90vh; overflow: auto; padding: 20px; font-family: inherit; }
  html.ea-big .ea-cbox { max-height: 72vh; }
  .ea-cbox h2 { font-size: 19px; margin: 0 0 4px; }
  .ea-cbox .ea-cintro { color: var(--muted, #8a8ea3); font-size: 14px; margin: 0 0 14px; line-height: 1.5; }
  .ea-copt { display: flex; gap: 12px; align-items: flex-start; padding: 12px 0; border-top: 1px solid var(--border, #2a2d3a); cursor: pointer; }
  .ea-copt input { width: 22px; height: 22px; margin-top: 2px; flex-shrink: 0; accent-color: #4ecb7f; cursor: pointer; }
  .ea-copt span { display: block; font-weight: 600; font-size: 15px; }
  .ea-copt small { display: block; color: var(--muted, #8a8ea3); font-size: 13px; line-height: 1.45; margin-top: 2px; }
  .ea-cact { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 14px; }
  .ea-cact button { font: inherit; font-size: 14px; padding: 9px 14px; border-radius: 10px; cursor: pointer; border: 1px solid var(--border, #2a2d3a); background: transparent; color: var(--text, #e8eaf0); }
  .ea-cact .ea-call { background: #4ecb7f; color: #0e0f14; border-color: #4ecb7f; font-weight: 600; }
  .ea-cact .ea-cok { margin-left: auto; }
  .ea-ccredit { color: var(--muted, #8a8ea3); font-size: 11px; margin: 14px 0 0; }
  @media print { html.ea-light { filter: none; } html.ea-big body { zoom: 1; } .ea-cbtn { display: none !important; } }`;
  const cst = document.createElement("style"); cst.textContent = ccss; document.head.appendChild(cst);

  function copen() {
    const c = cload();
    const ov = document.createElement("div"); ov.className = "ea-cov";
    ov.innerHTML = `<div class="ea-cbox" role="dialog" aria-modal="true" aria-labelledby="eaCT">
      <h2 id="eaCT">Confort de lecture</h2>
      <p class="ea-cintro">Choisis ce qui t'aide à lire. Tes réglages restent enregistrés sur cet appareil, pour toutes les activités.</p>
      ${OPTS.map(([k, t, d]) => `<label class="ea-copt"><input type="checkbox" data-k="${k}" ${c[k] ? "checked" : ""}><div><span>${t}</span><small>${d}</small></div></label>`).join("")}
      <div class="ea-cact"><button type="button" class="ea-call">Tout activer</button><button type="button" class="ea-creset">Tout désactiver</button><button type="button" class="ea-cok">Fermer</button></div>
      <p class="ea-ccredit">Police Luciole © Laurent Bourcellier &amp; Jonathan Perez, licence CC BY 4.0.</p>
    </div>`;
    const set = (k, v) => { const n = cload(); n[k] = v; try { localStorage.setItem(CKEY, JSON.stringify(n)); } catch (e) {} capply(n); };
    ov.querySelectorAll("input").forEach(i => i.onchange = () => set(i.dataset.k, i.checked));
    const all = v => ov.querySelectorAll("input").forEach(i => { i.checked = v; set(i.dataset.k, v); });
    ov.querySelector(".ea-call").onclick = () => all(true);
    ov.querySelector(".ea-creset").onclick = () => all(false);
    const close = () => { ov.remove(); document.removeEventListener("keydown", esc_); };
    const esc_ = e => { if (e.key === "Escape") close(); };
    ov.querySelector(".ea-cok").onclick = close;
    ov.onclick = e => { if (e.target === ov) close(); };
    document.addEventListener("keydown", esc_);
    document.body.appendChild(ov); ov.querySelector("input").focus();
  }
  EA.openConfort = copen;
  function cbutton() {
    const b = document.createElement("button"); b.type = "button"; b.className = "ea-cbtn";
    b.innerHTML = "<b>Aa</b>Lecture"; b.title = "Confort de lecture"; b.setAttribute("aria-label", "Confort de lecture");
    b.onclick = copen; return b;
  }
  document.addEventListener("DOMContentLoaded", () => {
    let box = document.querySelector(".ea-top");
    if (!box) {
      box = document.createElement("div"); box.className = "ea-top ea-float";
      document.body.prepend(box);
    }
    box.prepend(cbutton());
    /* Traductions des exemples : bouton « FR » pour les afficher */
    document.querySelectorAll(".lesson-body .tr").forEach(tr => {
      const prev = tr.previousElementSibling;
      const block = prev && getComputedStyle(prev).display === "block";
      if (block) tr.classList.add("tr-block");
      const b = document.createElement("button"); b.type = "button"; b.className = "tr-btn"; b.textContent = "FR";
      b.title = "Voir la traduction"; b.setAttribute("aria-expanded", "false");
      b.onclick = () => { const o = tr.classList.toggle("open"); b.setAttribute("aria-expanded", o ? "true" : "false"); };
      if (block) prev.appendChild(b); else tr.parentNode.insertBefore(b, tr);
    });
  });

  /* ── Hors connexion ── */
  if ("serviceWorker" in navigator && location.protocol === "https:") {
    window.addEventListener("load", () => { navigator.serviceWorker.register("sw.js").catch(() => {}); });
  }
})();
