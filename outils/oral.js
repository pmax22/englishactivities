/* ── Expression orale : écouter le modèle, s'enregistrer, se réécouter, tester sa prononciation ── */
const DATA = {}, MDEF = [];
%GENERIC%
const SUJETS = %SUJETS%;
SUJETS.forEach(s => MISSIONS.push({ id: s.id, icon: s.icon, title: s.title, desc: s.desc, group: s.group, build: () => [] }));
const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
const CAN_REC = !!(navigator.mediaDevices && navigator.mediaDevices.getUserMedia && window.MediaRecorder);
let rec = null, recStream = null, idx = 0, sujet = null, scores = {};
function words(t) { return norm(t).replace(/[^a-z0-9' ]/g, " ").split(/\s+/).filter(Boolean); }
function compare(target, said) {
  const T = words(target), S = words(said), used = new Array(S.length).fill(false);
  let ok = 0;
  const html = target.split(/\s+/).map(w => {
    const n = words(w)[0]; if (!n) return esc(w);
    const j = S.findIndex((x, k) => !used[k] && x === n);
    if (j > -1) { used[j] = true; ok++; return `<span class="or-good">${esc(w)}</span>`; }
    return `<span class="or-bad">${esc(w)}</span>`;
  }).join(" ");
  return { pct: T.length ? Math.round(ok / T.length * 100) : 0, html };
}
function stopRec() { try { if (rec && rec.state !== "inactive") rec.stop(); } catch (e) {} try { recStream && recStream.getTracks().forEach(t => t.stop()); } catch (e) {} }
startMission = function (id) {
  stopRec();
  current = MISSIONS.find(m => m.id === id); sujet = SUJETS.find(x => x.id === id); idx = 0; scores = {};
  showOnly("quiz"); drawItem();
};
function drawItem() {
  const it = sujet.items[idx], free = sujet.free;
  document.getElementById("qTitle").textContent = sujet.title;
  document.getElementById("qCount").textContent = `${idx + 1} / ${sujet.items.length}`;
  document.getElementById("qBar").style.width = (idx / sujet.items.length * 100) + "%";
  document.getElementById("qInstr").textContent = free ? "Réponds à l'oral, en anglais. Enregistre-toi puis réécoute-toi." : "Écoute le modèle, répète, enregistre-toi et compare.";
  document.getElementById("qFeedback").innerHTML = "";
  document.getElementById("btnReset").classList.add("hidden");
  const btn = document.getElementById("btnMain");
  btn.textContent = idx + 1 < sujet.items.length ? "Suivant →" : "Terminer"; btn.classList.remove("hidden");
  btn.onclick = () => { stopRec(); if (idx + 1 < sujet.items.length) { idx++; drawItem(); } else finishOral(); };
  const area = document.getElementById("qArea");
  area.innerHTML = (it.fr ? `<div class="fr-line">${esc(it.fr)}</div>` : "") +
    (free ? `<div class="big-word or-q">${esc(it.q)}</div>${it.help ? `<details class="wr-lex"><summary>💡 Aide : début de réponse</summary><div class="or-help">${esc(it.help)}</div></details>` : ""}`
          : `<div class="big-word or-target" lang="en">${esc(it.en)}</div>${it.ph ? `<div class="big-sub">${esc(it.ph)}</div>` : ""}`) +
    `<div class="or-tools">
      ${CAN_SPEAK && !free ? `<button class="btn btn-ghost" type="button" id="orModel">🔊 Modèle</button><button class="btn btn-ghost" type="button" id="orSlow">🐢 Lentement</button>` : ""}
      ${CAN_SPEAK && free && it.model ? `<button class="btn btn-ghost" type="button" id="orModel">🔊 Exemple de réponse</button>` : ""}
      ${CAN_REC ? `<button class="btn btn-primary" type="button" id="orRec">🎙️ M'enregistrer</button><audio id="orAudio" controls class="hidden"></audio>` : `<p class="lvl-help">L'enregistrement n'est pas disponible sur ce navigateur : entraîne-toi à voix haute.</p>`}
      ${SR && !free ? `<button class="btn btn-ghost" type="button" id="orTest">🗣️ Tester ma prononciation</button>` : ""}
      ${free && it.time ? `<span class="or-timer" id="orTimer">⏱ ${it.time} s</span>` : ""}
    </div><div id="orResult"></div>`;
  const say = (t, r) => { try { const u = new SpeechSynthesisUtterance(t); u.lang = "en-GB"; u.rate = r; speechSynthesis.cancel(); speechSynthesis.speak(u); } catch (e) {} };
  const m = area.querySelector("#orModel"); if (m) m.onclick = () => say(free ? it.model : it.en, 0.9);
  const sl = area.querySelector("#orSlow"); if (sl) sl.onclick = () => say(it.en, 0.6);
  const rb = area.querySelector("#orRec");
  if (rb) rb.onclick = async () => {
    if (rec && rec.state === "recording") { stopRec(); return; }
    try {
      recStream = await navigator.mediaDevices.getUserMedia({ audio: true });
      const chunks = []; rec = new MediaRecorder(recStream);
      rec.ondataavailable = e => chunks.push(e.data);
      let timer = null;
      rec.onstop = () => {
        clearInterval(timer);
        const a = area.querySelector("#orAudio"); if (!a) return;
        a.src = URL.createObjectURL(new Blob(chunks, { type: rec.mimeType || "audio/webm" })); a.classList.remove("hidden");
        rb.textContent = "🎙️ Recommencer"; rb.classList.remove("rec-on");
        scores[idx] = scores[idx] || { done: true };
      };
      rec.start(); rb.textContent = "⏹️ Arrêter"; rb.classList.add("rec-on");
      if (free && it.time) {
        let left = it.time; const tEl = area.querySelector("#orTimer");
        timer = setInterval(() => { left--; if (tEl) tEl.textContent = `⏱ ${left} s`; if (left <= 0) stopRec(); }, 1000);
      }
    } catch (e) { document.getElementById("orResult").innerHTML = `<div class="feedback ko">Micro non autorisé. Autorise le micro dans ton navigateur pour t'enregistrer.</div>`; }
  };
  const tb = area.querySelector("#orTest");
  if (tb) tb.onclick = () => {
    const r = new SR(); r.lang = "en-GB"; r.interimResults = false; r.maxAlternatives = 3;
    tb.textContent = "👂 Je t'écoute…";
    r.onresult = e => {
      const alts = [...e.results[0]].map(x => x.transcript);
      const best = alts.map(a => Object.assign(compare(it.en, a), { said: a })).sort((a, b) => b.pct - a.pct)[0];
      scores[idx] = { done: true, pct: Math.max(best.pct, (scores[idx] && scores[idx].pct) || 0) };
      document.getElementById("orResult").innerHTML = `<div class="feedback ${best.pct >= 80 ? "ok" : "ko"}">${best.pct >= 80 ? "✅" : "🔁"} <b>${best.pct}%</b> des mots reconnus<div class="or-cmp">${best.html}</div><span class="tip">Compris : « ${esc(best.said)} »${best.pct < 80 ? " — réécoute le modèle et réessaie." : ""}</span></div>`;
    };
    r.onerror = () => { document.getElementById("orResult").innerHTML = `<div class="feedback ko">Je n'ai rien entendu. Vérifie ton micro et réessaie.</div>`; };
    r.onend = () => { tb.textContent = "🗣️ Tester ma prononciation"; };
    try { r.start(); } catch (e) {}
  };
}
function finishOral() {
  const n = sujet.items.length, done = Object.keys(scores).length;
  const tested = Object.values(scores).filter(s => s.pct != null), avg = tested.length ? Math.round(tested.reduce((a, s) => a + s.pct, 0) / tested.length) : null;
  document.getElementById("sTitle").textContent = sujet.title;
  document.getElementById("sStars").textContent = "🎙️";
  document.getElementById("sScore").innerHTML = `${done}<span>/${n}</span>`;
  document.getElementById("sMsg").innerHTML = `Tu t'es enregistré(e) sur ${done} élément${done > 1 ? "s" : ""} sur ${n}.` + (avg != null ? ` Prononciation : <b>${avg}%</b> des mots reconnus en moyenne.` : "") +
    `<p class="lvl-help">Conseil : réécoute-toi et compare avec le modèle. Recommence jusqu'à être à l'aise !</p>`;
  document.getElementById("sRecap").innerHTML = "";
  showOnly("score");
  if (window.EA) EA.afterScore({ id: sujet.id, title: sujet.title, score: done, total: n, wrongs: [] });
}
