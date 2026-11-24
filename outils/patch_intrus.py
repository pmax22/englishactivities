"""Filet de sécurité : ajoute l'avertissement « intrus » aux pages dont le moteur
inclus n'a pas encore été régénéré depuis engine.js / base.css. Idempotent."""
import glob, os, re
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

A1 = '''    area.innerHTML = head + `<div class="order-zone empty" id="zone"></div>'''
B1 = '''    const nD = (q.distractors || []).length;
    const note = nD ? `<div class="order-note"><b>Attention :</b> ${nD > 1 ? nD + " étiquettes sont en trop" : "une étiquette est en trop"} (intrus). Ne ${nD > 1 ? "les" : "l'"}utilise pas.</div>` : "";
    area.innerHTML = head + note + `<div class="order-zone empty" id="zone"></div>'''
A2 = '''    document.querySelectorAll("#pool .tile").forEach(t => t.disabled = true);
    finish(ok, val, q.answer, "");'''
B2 = '''    const ds = q.distractors || [];
    document.querySelectorAll("#pool .tile").forEach(t => { t.disabled = true; if (ds.includes(t.textContent)) t.classList.add("intrus"); });
    if (ds.length && !q._intrus) {
      q._intrus = true;
      const miss = ds.filter(d => !(q.tip || "").includes(d));
      if (miss.length) q.tip = (q.tip ? q.tip + " " : "") + `L'intrus était : <b>${miss.map(esc).join(", ")}</b>.`;
    }
    finish(ok, val, q.answer, "");'''
CSS = ("\n  .order-note { font-size: 13px; color: #ff9f43; background: rgba(255,159,67,.08); border: 1px solid rgba(255,159,67,.35); border-radius: 8px; padding: 6px 10px; margin-bottom: 10px; }"
       "\n  .tile.intrus { text-decoration: line-through; border-color: var(--red); opacity: .7; }")

done = []
for p in sorted(glob.glob(f"{REPO}/*.html")):
    s = open(p, encoding="utf-8").read()
    if "q.distractors" not in s or "order-note" in s:
        continue
    o = s
    s = s.replace(A1, B1, 1).replace(A2, B2, 1)
    # variantes des pages faites à la main (questions_fermees / questions_ouvertes)
    s = re.sub(r'\n(    )area\.innerHTML = (q\.head \+ )?`<div class="order-zone empty" id="zone"></div>',
               lambda m: "\n" + "\n".join(B1.split("\n")[:2]) + "\n    area.innerHTML = " + (m.group(2) or "") + "note + `<div class=\"order-zone empty\" id=\"zone\"></div>", s, count=1)
    s = re.sub(r'\n    document\.querySelectorAll\("#pool \.tile"\)\.forEach\(t => t\.disabled = true\);\n    finish\(ok, val, q\.answer(, "")?\);',
               lambda m: "\n" + B2.replace('finish(ok, val, q.answer, "");', "finish(ok, val, q.answer" + (m.group(1) or "") + ");"), s, count=1)
    s = re.sub(r"(\n  \.tiles \{[^}]*\})", lambda m: m.group(1) + CSS, s, count=1)
    if s.count("order-note") >= 2 and "q._intrus" in s:
        open(p, "w", encoding="utf-8").write(s); done.append(os.path.basename(p))
    else:
        print("NON PATCHÉ :", os.path.basename(p))
print("intrus patché :", done)
