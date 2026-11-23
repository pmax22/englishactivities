import os as _eo
if not _eo.environ.get("EA_OUT"): _eo.environ["EA_OUT"] = _eo.path.dirname(_eo.path.abspath(__file__))
_EA_OUT = _eo.environ["EA_OUT"]; _EA_REPO = _eo.path.dirname(_EA_OUT); _eo.makedirs(_EA_OUT + "/_captures", exist_ok=True)
import sys, json
def add(C):
    p=_EA_OUT+"/index_gen2.py"; s=open(p,encoding="utf-8").read()
    ins=""
    for c in C:
        f,c1,c2,big,small,sub,title,desc,chips,tags,kw,level=c
        assert f'"{f}.html"' not in s, f
        kick="Culture · "+sub.split(" :")[0]
        ins+=f' ("{f}.html", CU, "{c1}", "{c2}", {big!r}, {small!r}, {kick!r}, {title!r}, {desc!r}, {chips!r}, {tags}, {kw!r}),\n'
        s=s.replace(f' "{level}": "', f' "{level}": "{f} ',1)
        k=f'("{sub}", "'; assert k in s, sub; i=s.index(k)+len(k); s=s[:i]+f+" "+s[i:]
    s=s.replace(' ("ce_ecole.html", CO,', ins+' ("ce_ecole.html", CO,',1)
    open(p,"w",encoding="utf-8").write(s)
