"""Filet de sécurité pour les pages faites à la main (sans générateur) : y reporte les
évolutions du moteur (engine.js / base.css). Idempotent.
- avertissement « intrus » dans « Remets dans l'ordre »
- signe + / − / ? à gauche de la zone de réponse, « ? » en bleu"""
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

SG = '''    const sg = q.sign || (/n[ée]gati/i.test(q.instr || "") ? "minus" : /interrogati/i.test(q.instr || "") ? "q" : /affirmati/i.test(q.instr || "") ? "plus" : "");
    const sgn = sg ? `<span class="sign ${sg}" title="${sg === "minus" ? "Forme négative" : sg === "q" ? "Forme interrogative" : sg === "plus" ? "Forme affirmative" : ""}">${sg === "plus" ? "+" : sg === "minus" ? "−" : sg === "eq" ? "=" : "?"}</span>` : "";
'''
CSS2 = ("\n  .sign.q { background: rgba(96,165,250,.14); color: #60a5fa; border: 1px solid rgba(96,165,250,.45); }"
        "\n  .order-row { display: flex; align-items: stretch; gap: 10px; margin-bottom: 12px; }"
        "\n  .order-row .order-zone { flex: 1; min-width: 0; margin-bottom: 0; }"
        "\n  .order-row .sign { width: 38px; height: auto; min-height: 38px; margin: 0; font-size: 24px; flex-shrink: 0; }")
done = []
for p in sorted(glob.glob(f"{REPO}/*.html")):
    s = open(p, encoding="utf-8").read()
    if "order-zone empty" not in s or "order-row" in s:
        continue
    s2 = re.sub(r'\n(    area\.innerHTML = [^\n]*?)`<div class="order-zone empty" id="zone"></div>',
                lambda m: "\n" + SG + m.group(1) + '`<div class="order-row">${sgn}<div class="order-zone empty" id="zone"></div></div>', s, count=1)
    s2 = s2.replace(".sign.eq, .sign.q {", ".sign.eq {", 1)
    s2 = re.sub(r"(\n  \.tiles \{[^}]*\})", lambda m: m.group(1) + CSS2, s2, count=1)
    if s2.count("order-row") >= 3:
        open(p, "w", encoding="utf-8").write(s2); done.append(os.path.basename(p))
    else:
        print("SIGNE NON PATCHÉ :", os.path.basename(p))
print("signe patché :", done)
