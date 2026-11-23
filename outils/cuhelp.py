import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
exec(open(_EA_OUT+"/content19.py", encoding="utf-8").read().split("# ════════════════════ ROYAUME-UNI")[0])
def DZ(file, text, pairs, qs, gl=()):
    _GL.setdefault(file, []).extend(gl)
    DOSSIERS[file] = _gloss(file, text)
    N1[file] = (pairs, qs)
def END():
    if _missing: print("GLOSS NOT FOUND:", _missing)
    print("ok")
