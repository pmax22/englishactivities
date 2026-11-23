/* ── Écriture guidée : chaque sujet = une suite d'étapes, l'élève écrit chaque phrase ── */
const DATA = {}, MDEF = [];
%GENERIC%
const SUJETS = %SUJETS%;
SUJETS.forEach(s => MISSIONS.push({ id: s.id, icon: s.icon, title: s.title, desc: s.desc, group: s.group, build: () => [] }));
const DKEY = "ea_ecriture_v1";
function drafts() { try { return JSON.parse(localStorage.getItem(DKEY) || "{}"); } catch (e) { return {}; } }
function saveDraft(id, vals) { const d = drafts(); d[id] = vals; try { localStorage.setItem(DKEY, JSON.stringify(d)); } catch (e) {} }
function checkLine(txt, step) {
  const t = txt.trim(), msgs = [];
  if (!t) return { ok: false, msgs: [] };
  const words = t.split(/\s+/).filter(Boolean).length;
  if (!/^[A-Z"«]/.test(t)) msgs.push("Commence ta phrase par une majuscule.");
  if (!/[.!?]["»]?$/.test(t)) msgs.push("Termine ta phrase par un point (. ! ?).");
  if (/(^|\s)i(\s|'|’|$)/.test(t)) msgs.push("« I » (je) s'écrit toujours en majuscule.");
  (step.need || []).forEach(([re, why]) => { if (!new RegExp(re, "i").test(t)) msgs.push(why); });
  if (step.min && words < step.min) msgs.push(`Écris au moins ${step.min} mots (tu en as ${words}).`);
  return { ok: msgs.length === 0, msgs };
}
startMission = function (id) {
  current = MISSIONS.find(m => m.id === id);
  const s = SUJETS.find(x => x.id === id), saved = drafts()[id] || {};
  showOnly("quiz");
  document.getElementById("qTitle").textContent = s.title;
  document.getElementById("qCount").textContent = `${s.steps.length} étapes`;
  document.getElementById("qBar").style.width = "0%";
  document.getElementById("qInstr").textContent = s.consigne;
  document.getElementById("qFeedback").innerHTML = "";
  document.getElementById("btnReset").classList.add("hidden");
  const btn = document.getElementById("btnMain");
  btn.textContent = "Voir mon texte"; btn.classList.remove("hidden");
  const area = document.getElementById("qArea");
  area.innerHTML = (s.lex ? `<details class="wr-lex"><summary>📚 Boîte à mots</summary><div>${s.lex.map(w => `<span class="pill">${esc(w)}</span>`).join(" ")}</div></details>` : "") +
    s.steps.map((st, i) => `<div class="wr-step" data-i="${i}">
      <div class="wr-q"><span class="wr-n">${i + 1}</span>${esc(st.fr)}</div>
      <textarea class="answer wr-in" rows="2" placeholder="${esc(st.start || "")}…" spellcheck="true" lang="en">${esc(saved[i] || "")}</textarea>
      <div class="wr-tools"><button type="button" class="wr-ex">💡 Exemple</button><span class="wr-msg"></span></div>
      <div class="wr-model hidden">${esc(st.ex)}</div></div>`).join("");
  const ins = [...area.querySelectorAll(".wr-in")];
  const update = () => {
    let done = 0;
    ins.forEach((el, i) => {
      if (!el.value.trim() && s.steps[i].start && document.activeElement === el) { el.value = s.steps[i].start + " "; }
      const r = checkLine(el.value, s.steps[i]), box = el.closest(".wr-step");
      box.classList.toggle("ok", r.ok); if (r.ok) done++;
      box.querySelector(".wr-msg").innerHTML = el.value.trim() ? (r.ok ? "✅ Bien !" : "⚠️ " + r.msgs.map(esc).join(" ")) : "";
    });
    document.getElementById("qBar").style.width = (done / ins.length * 100) + "%";
    document.getElementById("qCount").textContent = `${done} / ${ins.length} phrases validées`;
    saveDraft(id, ins.map(x => x.value));
  };
  ins.forEach(el => { el.addEventListener("input", update); el.addEventListener("blur", update);
    el.addEventListener("focus", () => { if (!el.value.trim() && s.steps[+el.closest(".wr-step").dataset.i].start) { el.value = s.steps[+el.closest(".wr-step").dataset.i].start + " "; el.setSelectionRange(el.value.length, el.value.length); } }); });
  area.querySelectorAll(".wr-ex").forEach(b => b.onclick = () => b.closest(".wr-step").querySelector(".wr-model").classList.toggle("hidden"));
  update();
  btn.onclick = () => showText(s, ins.map(x => x.value.trim()).filter(Boolean), ins.filter(el => el.closest(".wr-step").classList.contains("ok")).length);
};
function showText(s, lines, ok) {
  const text = lines.join(" ");
  const words = text.split(/\s+/).filter(Boolean).length;
  document.getElementById("sTitle").textContent = s.title;
  document.getElementById("sStars").textContent = "✍️";
  document.getElementById("sScore").innerHTML = `${words}<span> mots</span>`;
  document.getElementById("sMsg").innerHTML = `<div class="wr-final" lang="en">${esc(text) || "<i>Ton texte est vide.</i>"}</div>
    <div class="wr-final-tools">${CAN_SPEAK && text ? sayBtn(text, "Écouter mon texte") : ""}
    <button class="btn btn-ghost" type="button" id="wrCopy">📋 Copier mon texte</button></div>
    <p class="lvl-help">${ok} phrase${ok > 1 ? "s" : ""} sur ${s.steps.length} validée${ok > 1 ? "s" : ""} par les vérifications automatiques. Elles ne remplacent pas la correction du professeur : relis-toi bien (accords, -s, temps des verbes).</p>`;
  document.getElementById("sRecap").innerHTML = "";
  showOnly("score");
  const share = (EA.getName() || "(prénom ?)") + " — " + s.title + " — " + words + " mots\n" + text;
  document.getElementById("wrCopy").onclick = e => EA.copy(share, e.currentTarget);
  if (window.EA) EA.record(s.id, s.title, ok, s.steps.length, []);
  document.querySelector("#score .btn-primary").onclick = () => startMission(s.id);
}
