import json
from test_r66_reader import a
from app.knowledge.common.registry import value
with a.store.connect() as c:rs=a.store.heads(c)
for rid,r in rs.items():
 if r['kind']=='person':print(json.dumps({'id':rid,'name':value(r,'display_name'),'role':value(r,'role'),'team':value(r,'team')},ensure_ascii=False))
