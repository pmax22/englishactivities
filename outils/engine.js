/* ═══════════ OUTILS ═══════════ */
function shuffle(arr) { const a = arr.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; }
function norm(s) {
  return String(s).toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "")
    .replace(/[’‘`´]/g, "'")
    .replace(/\bi'm\b/g, "i am").replace(/'re\b/g, " are").replace(/\b(he|she|it|that|what|where|who)'s\b/g, "$1 is")
    .replace(/\bdo not\b/g, "don't").replace(/\bdoes not\b/g, "doesn't").replace(/\bis not\b/g, "isn't").replace(/\bare not\b/g, "aren't")
    .replace(/\bhas not\b/g, "hasn't").replace(/\bhave not\b/g, "haven't")
    .replace(/\bdid not\b/g, "didn't").replace(/\bdidnt\b/g, "didn't")
    .replace(/\bwas not\b/g, "wasn't").replace(/\bwasnt\b/g, "wasn't")
    .replace(/\bwere not\b/g, "weren't").replace(/\bwerent\b/g, "weren't")
    .replace(/[.?!,;:]/g, " ").replace(/\s+/g, " ").trim();
}
function esc(s) { return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;"); }
function capF(s) { return s.charAt(0).toUpperCase() + s.slice(1); }
function pick(arr) { return arr[Math.floor(Math.random() * arr.length)]; }

/* ═══════════ STOCKAGE ═══════════ */
let best = {};
try { best = JSON.parse(localStorage.getItem(STORE_KEY) || "{}") || {}; } catch (e) { best = {}; }
function saveBest() { try { localStorage.setItem(STORE_KEY, JSON.stringify(best)); } catch (e) {} }

/* ═══════════ MENU ═══════════ */
function renderMenu() {
  const box = document.getElementById("missions"); box.innerHTML = "";
  let lastGroup = null, grid = box;
  MISSIONS.forEach((m, i) => {
    if (m.group && m.group !== lastGroup) {
      lastGroup = m.group; box.classList.remove("missions");
      const h = document.createElement("div"); h.className = "seance-title"; h.textContent = m.group; box.appendChild(h);
      grid = document.createElement("div"); grid.className = "missions"; box.appendChild(grid);
    }
    const b = document.createElement("button"); b.className = "mission";
    const bs = best[m.id];
    b.innerHTML = `${bs ? `<span class="m-best ${bs.s === bs.t ? "done" : ""}">★ ${bs.s}/${bs.t}</span>` : ""}
      <span class="m-icon">${m.icon}</span><span class="m-num">Mission ${i + 1}</span>
      <span class="m-title">${m.title}</span><span class="m-desc">${m.desc}</span>`;
    b.onclick = () => startMission(m.id);
    grid.appendChild(b);
  });
}
function showOnly(id) {
  ["menu", "quiz", "score"].forEach(x => document.getElementById(x).classList.toggle("hidden", x !== id));
  window.scrollTo({ top: 0, behavior: "smooth" });
}
function showMenu() { renderMenu(); showOnly("menu"); }

/* ═══════════ MOTEUR ═══════════ */
let current = null, questions = [], qi = 0, score = 0, answered = false, recap = [], orderChosen = [];
let matchSel = null, matchErr = 0, matchDone = 0;

function startMission(id) {
  current = MISSIONS.find(m => m.id === id);
  questions = current.build(); qi = 0; score = 0; recap = [];
  showOnly("quiz"); renderQuestion();
}

function renderQuestion() {
  const q = questions[qi]; answered = false;
  document.getElementById("qTitle").textContent = `Mission ${MISSIONS.indexOf(current) + 1} · ${current.title}`;
  document.getElementById("qCount").textContent = `${qi + 1} / ${questions.length} · Score ${score}`;
  document.getElementById("qBar").style.width = (qi / questions.length * 100) + "%";
  document.getElementById("qInstr").textContent = q.instr;
  document.getElementById("qFeedback").innerHTML = "";
  const area = document.getElementById("qArea"), btn = document.getElementById("btnMain");
  btn.textContent = "Valider"; btn.classList.remove("hidden");
  document.getElementById("btnReset").classList.add("hidden");
  const head = q.head || "";

  if (q.kind === "gap") {
    let bi = 0;
    const line = q.parts.map(p => {
      if (typeof p === "string") return esc(p);
      const i = bi++;
      return `<input class="answer gapin" data-b="${i}" style="width:${p.width || 200}px" autocomplete="off" autocapitalize="off" spellcheck="false" placeholder="${p.ph || ""}">` +
        (p.hint ? `<span class="bvhint">(${esc(p.hint)})</span>` : "");
    }).join("");
    area.innerHTML = head + `<div class="gap-line">${q.sign ? `<span class="sign ${q.sign}">${q.sign === "plus" ? "+" : q.sign === "minus" ? "−" : q.sign === "eq" ? "=" : "?"}</span>` : ""}${line}</div>` + (q.foot || "");
    setTimeout(() => { const f = area.querySelector(".gapin"); if (f) f.focus(); }, 50);
  } else if (q.kind === "mcq") {
    const order = q.keepOrder ? q.options.map((_, i) => i) : shuffle(q.options.map((_, i) => i));
    area.innerHTML = head + `<div class="choices ${q.grid ? "grid" + q.grid : ""}">${order.map(i => `<button class="btn-choice" data-i="${i}">${q.html ? q.options[i] : esc(q.options[i])}</button>`).join("")}</div>`;
    area.querySelectorAll(".btn-choice").forEach(b => b.onclick = () => submitMcq(+b.dataset.i));
    btn.classList.add("hidden");
  } else if (q.kind === "order") {
    orderChosen = [];
    const all = shuffle(q.tiles.concat(q.distractors || []));
    const nD = (q.distractors || []).length;
    const note = nD ? `<div class="order-note"><b>Attention :</b> ${nD > 1 ? nD + " étiquettes sont en trop" : "une étiquette est en trop"} (intrus). Ne ${nD > 1 ? "les" : "l'"}utilise pas.</div>` : "";
    const sg = q.sign || (/n[ée]gati/i.test(q.instr || "") ? "minus" : /interrogati/i.test(q.instr || "") ? "q" : /affirmati/i.test(q.instr || "") ? "plus" : "");
    const sgn = sg ? `<span class="sign ${sg}" title="${sg === "minus" ? "Forme négative" : sg === "q" ? "Forme interrogative" : sg === "plus" ? "Forme affirmative" : ""}">${sg === "plus" ? "+" : sg === "minus" ? "−" : sg === "eq" ? "=" : "?"}</span>` : "";
    area.innerHTML = head + note + `<div class="order-row">${sgn}<div class="order-zone empty" id="zone"></div></div><div class="tiles" id="pool">` +
      all.map(t => `<button class="tile">${esc(t)}</button>`).join("") + `</div>`;
    area.querySelectorAll("#pool .tile").forEach(b => b.onclick = () => addTile(b));
    document.getElementById("btnReset").classList.remove("hidden");
  } else if (q.kind === "match") {
    matchSel = null; matchErr = 0; matchDone = 0;
    const idx = q.pairs.map((_, k) => k), L = shuffle(idx), R = shuffle(idx);
    area.innerHTML = head + `<div class="match"><div class="mcol">${L.map(k => `<button class="mbtn" data-s="0" data-k="${k}" lang="en">${esc(q.pairs[k][0])}</button>`).join("")}</div>` +
      `<div class="mcol">${R.map(k => `<button class="mbtn" data-s="1" data-k="${k}">${esc(q.pairs[k][1])}</button>`).join("")}</div></div>` +
      `<div class="match-info" id="mInfo">Touche un mot anglais, puis sa traduction.</div>`;
    area.querySelectorAll(".mbtn").forEach(b => b.onclick = () => matchClick(b));
    btn.classList.add("hidden");
  }
}

function matchClick(b) {
  if (answered || b.classList.contains("matched")) return;
  const q = questions[qi];
  if (!matchSel || matchSel.dataset.s === b.dataset.s) {
    document.querySelectorAll(".mbtn.sel").forEach(x => x.classList.remove("sel"));
    matchSel = b; b.classList.add("sel"); return;
  }
  const a = matchSel; matchSel = null; a.classList.remove("sel");
  if (a.dataset.k === b.dataset.k) {
    a.classList.add("matched"); b.classList.add("matched"); a.disabled = b.disabled = true; matchDone++;
  } else {
    matchErr++; [a, b].forEach(x => { x.classList.add("miss"); setTimeout(() => x.classList.remove("miss"), 600); });
  }
  document.getElementById("mInfo").textContent = `${matchDone} / ${q.pairs.length} paires trouvées` + (matchErr ? ` · ${matchErr} erreur${matchErr > 1 ? "s" : ""}` : "");
  if (matchDone === q.pairs.length) {
    const ok = matchErr <= 1;
    finish(ok, matchErr + " erreur" + (matchErr > 1 ? "s" : ""), q.correct, ok ? "" : "Plus d'une erreur : refais la mission pour mémoriser les paires.");
  }
}

function addTile(b) { if (answered) return; b.classList.add("used"); orderChosen.push(b); drawZone(); }
function drawZone() {
  const zone = document.getElementById("zone"); zone.innerHTML = "";
  zone.classList.toggle("empty", orderChosen.length === 0);
  orderChosen.forEach((src, k) => {
    const t = document.createElement("button"); t.className = "tile"; t.textContent = src.textContent;
    t.onclick = () => { if (answered) return; src.classList.remove("used"); orderChosen.splice(k, 1); drawZone(); };
    zone.appendChild(t);
  });
}
function resetOrder() { if (answered) return; orderChosen.forEach(s => s.classList.remove("used")); orderChosen = []; drawZone(); }

function mainAction() {
  if (answered) { nextQuestion(); return; }
  const q = questions[qi];
  if (q.kind === "gap") {
    const inputs = [...document.querySelectorAll(".gapin")];
    const empty = inputs.find(i => !i.value.trim());
    if (empty) { empty.focus(); return; }
    const blanks = q.parts.filter(p => typeof p !== "string");
    const vals = inputs.map(i => i.value);
    let allOk = true;
    inputs.forEach((inp, k) => {
      const ok = blanks[k].answers.some(a => norm(a) === norm(inp.value));
      inp.classList.add(ok ? "ok" : "ko"); inp.disabled = true; if (!ok) allOk = false;
    });
    finish(allOk, vals.join(" … "), q.correct, allOk || !q.diagnose ? "" : q.diagnose(vals));
  } else if (q.kind === "order") {
    if (!orderChosen.length) return;
    const val = orderChosen.map(t => t.textContent).join(" ");
    const ok = [q.answer].concat(q.alts || []).some(a => norm(val) === norm(a));
    document.getElementById("zone").classList.add(ok ? "ok" : "ko");
    const ds = q.distractors || [];
    document.querySelectorAll("#pool .tile").forEach(t => { t.disabled = true; if (ds.includes(t.textContent)) t.classList.add("intrus"); });
    if (ds.length && !q._intrus) {
      q._intrus = true;
      const miss = ds.filter(d => !(q.tip || "").includes(d));
      if (miss.length) q.tip = (q.tip ? q.tip + " " : "") + `L'intrus était : <b>${miss.map(esc).join(", ")}</b>.`;
    }
    finish(ok, val, q.answer, "");
  }
}

function submitMcq(i) {
  if (answered) return;
  const q = questions[qi], ok = i === q.correct;
  document.querySelectorAll(".btn-choice").forEach(b => {
    const bi = +b.dataset.i; b.disabled = true;
    b.classList.add(bi === q.correct ? "correct" : bi === i ? "wrong" : "dim");
  });
  const strip = s => String(s).replace(/<[^>]+>/g, "");
  finish(ok, strip(q.options[i]), q.correctText || strip(q.options[q.correct]), "");
}

function finish(ok, given, correct, why) {
  answered = true; if (ok) score++;
  const q = questions[qi];
  recap.push({ ok, label: q.label, given, correct, q });
  if (window.EA && EA.onAnswer) { try { EA.onAnswer(q, ok); } catch (e) {} }
  document.getElementById("qFeedback").innerHTML = ok
    ? `<div class="feedback ok">✅ <b>Bravo !</b> ${esc(correct)}<span class="tip">${q.tip || ""}</span></div>`
    : `<div class="feedback ko">❌ La bonne réponse : <b>${esc(correct)}</b><span class="tip">${why || q.tip || ""}</span></div>`;
  document.getElementById("qCount").textContent = `${qi + 1} / ${questions.length} · Score ${score}`;
  document.getElementById("btnReset").classList.add("hidden");
  const btn = document.getElementById("btnMain");
  btn.textContent = qi + 1 < questions.length ? "Suivant →" : "Voir mon score";
  btn.classList.remove("hidden"); btn.focus();
}

function nextQuestion() { qi++; if (qi < questions.length) renderQuestion(); else showScore(); }

function showScore() {
  const t = questions.length, pct = score / t, prev = best[current.id];
  if (!prev || pct > prev.s / prev.t) { best[current.id] = { s: score, t }; saveBest(); }
  document.getElementById("sTitle").textContent = `Mission ${MISSIONS.indexOf(current) + 1} · ${current.title}`;
  document.getElementById("sScore").innerHTML = `${score}<span>/${t}</span>`;
  const stars = pct === 1 ? 3 : pct >= .7 ? 2 : pct >= .4 ? 1 : 0;
  document.getElementById("sStars").textContent = "★".repeat(stars) + "☆".repeat(3 - stars);
  document.getElementById("sMsg").textContent =
    pct === 1 ? "Perfect! Excellent travail !" : pct >= .7 ? "Very good! Encore un petit effort pour le sans-faute." :
    pct >= .4 ? "Not bad! Relis la leçon et recommence." : "Keep going! Relis le rappel de la leçon puis réessaie.";
  document.getElementById("sRecap").innerHTML = recap.map(r =>
    `<div class="recap-item"><span class="r-ic">${r.ok ? "✅" : "❌"}</span><span class="r-txt">${esc(r.label)} → <b>${esc(r.correct)}</b>${r.ok ? "" : ` <i>(ta réponse : ${esc(r.given)})</i>`}</span></div>`).join("");
  showOnly("score");
  if (window.EA) {
    try {
      const wrongs = recap.filter(r => !r.ok).map(r => {
        const q = Object.assign({}, r.q, { correctText: r.correct });
        const ids = [...String(q.head || "").matchAll(/data-doc="([\w-]+)"/g)].map(m => m[1]);
        if (ids.length && typeof DOCS_ !== "undefined") { q.__docs = {}; ids.forEach(i => q.__docs[i] = DOCS_[i]); }
        return q;
      });
      EA.afterScore({ id: current.id, title: current.title, score, total: t, wrongs });
    } catch (e) {}
  }
}

document.addEventListener("keydown", e => {
  if (e.key !== "Enter" || document.getElementById("quiz").classList.contains("hidden")) return;
  const q = questions[qi];
  if (!q) return;
  if (answered || q.kind !== "mcq") {
    if (!answered && q.kind === "gap") {
      const inputs = [...document.querySelectorAll(".gapin")];
      const idx = inputs.indexOf(document.activeElement);
      if (idx > -1 && idx < inputs.length - 1 && !inputs[idx + 1].value.trim()) { e.preventDefault(); inputs[idx + 1].focus(); return; }
    }
    e.preventDefault(); mainAction();
  }
});

renderMenu();
