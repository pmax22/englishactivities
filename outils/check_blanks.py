import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
import re,sys
for f in sys.argv[1:]:
    s=open(f,encoding="utf-8").read()
    for m in re.finditer(r'\b[GC]\("((?:[^"\\]|\\.)*)"',s):
        n=m.group(1).count("____")
        if n>1 or (m.group(0).startswith("G") and n!=1): print(f,"BAD:",m.group(1))
