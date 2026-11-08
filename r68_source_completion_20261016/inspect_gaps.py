import json,sys,collections
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B/'system'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import CATALOG,value
from audit_sources import read
with CommonStore(B/'common.sqlite').connect() as c:rs=CommonStore.heads(c)
for k in ['center','game','competition','competition_rule','service','zone','rental_package','equipment_model','faq']:
 print('KIND',k,json.dumps([{f['key']:f['value_schema']} for f in CATALOG[k]['fields']],ensure_ascii=False))
 print('EXAMPLE',json.dumps(next(r for r in rs.values() if r['kind']==k),ensure_ascii=False)[:4200])
for name in ['user_service_facts_20261008.json','service_policy_answers.json']:
 x=read('data/curated/'+name)
 print('CLAIMS',name,json.dumps(x,ensure_ascii=False))
print('ALIASES',json.dumps(json.loads((B/'AUDIT_SOURCE_STRUCTURE.json').read_text('utf8'))['aliases'][:3],ensure_ascii=False))
for p in (B/'source_snapshot/data/content').rglob('*.json'):
 try:x=json.loads(p.read_text('utf-8-sig'))
 except:continue
 if x.get('kind')=='game_profile':print('GAMEFACT',json.dumps(x['facts'],ensure_ascii=False));break
