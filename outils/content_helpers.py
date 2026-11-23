import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
import json
NS = {"__name__": "gen"}
exec(open(_EA_OUT+"/gen.py", encoding="utf-8").read(), NS)
page = NS["page"]
ENGINE_GENERIC = open(_EA_OUT+"/generic.js", encoding="utf-8").read()

def G(line, ans, hint=None, fr=None, tip=None, sign=None, w=None, big=None, bigsub=None, say=None, doc=None):
    d = {"line": line, "ans": [ans] if isinstance(ans, str) else ans}
    for k, v in (("hint", hint), ("fr", fr), ("tip", tip), ("sign", sign), ("w", w), ("big", big), ("bigsub", bigsub), ("say", say), ("doc", doc)):
        if v: d[k] = v
    return d

def C(line, opts, tip=None, fr=None, big=None, keep=False, c=0, bigsub=None, instr=None, say=None, listen=False, doc=None):
    d = {"opts": opts}
    for k, v in (("line", line), ("tip", tip), ("fr", fr), ("big", big), ("keep", keep), ("c", c), ("bigsub", bigsub), ("instr", instr), ("say", say), ("listen", listen), ("doc", doc)):
        if v: d[k] = v
    return d

def O(en, fr=None, trap=None, tip=None, alts=None):
    d = {"en": en}
    for k, v in (("fr", fr), ("trap", trap), ("tip", tip), ("alts", alts)):
        if v: d[k] = v
    return d

REGISTRY = []
SECTION_TAG = {f + '.html': 'Anglais · Syntaxe' for f in ['questions_sujet','question_tags','exclamatives','connecteurs','relatifs','subordonnees_temps','conditionnel','passif','discours_indirect']}
SECTION_TAG['heure_dates.html'] = 'Anglais · Lexique'
def newpage(file, title, h1, sub, colors, lesson, data, mdef, tag="Anglais · Grammaire", docs=None):
    if tag == "Anglais · Grammaire" and file in SECTION_TAG: tag = SECTION_TAG[file]
    data_js = {k: {"kind": v[0], "instr": v[1], "items": v[2]} for k, v in data.items()}
    js = ("const DOCS = " + json.dumps(docs, ensure_ascii=False) + ";\n" if docs else "") + "const DATA = " + json.dumps(data_js, ensure_ascii=False) + ";\nconst MDEF = " + json.dumps(mdef, ensure_ascii=False) + ";\n" + ENGINE_GENERIC
    page(file, title, tag, h1, sub, colors, lesson, "", js)
    REGISTRY.append(file)

def M(id, icon, title, desc, frm, n=10, group=None, ordered=False):
    d = {"id": id, "icon": icon, "title": title, "desc": desc, "from": frm, "n": n}
    if group: d["group"] = group
    if ordered: d["ordered"] = True
    return d
