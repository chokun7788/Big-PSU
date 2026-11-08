import sys,json,re
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B/'system'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import value
s=CommonStore(B/'common.sqlite')
with s.connect() as c:rs=s.heads(c)
for rid,r in rs.items():
 if r['kind']!='competition_rule':continue
 v=value(r,'text');raw=json.dumps(v,ensure_ascii=False)
 if re.search(sys.argv[1],raw,re.I):print(rid,raw)
