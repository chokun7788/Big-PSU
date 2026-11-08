import collections,json,sys,re
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B/'system'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import value
def read(rel):
 p=B/'source_snapshot'/rel
 return [json.loads(s) for s in p.read_text('utf-8-sig').splitlines() if s.strip()] if p.suffix=='.jsonl' else json.loads(p.read_text('utf-8-sig'))
with CommonStore(B/'common.sqlite').connect() as c:rs=CommonStore.heads(c)
def strings(v):
 if isinstance(v,dict):
  for x in v.values():yield from strings(x)
 elif isinstance(v,list):
  for x in v:yield from strings(x)
 elif isinstance(v,str):yield v
alltext='\n'.join(s for r in rs.values() for s in strings(r['fields']))
for x in read('data/curated/member_profiles.jsonl'):print('PERSON',x['name'],x['group'])
for x in read('data/curated/equipment_item_details.jsonl'):print('EQUIP',x['id'],x['item'],x['what_th'])
for path in ['data/curated/user_service_facts_20261008.json','data/curated/service_policy_answers.json','data/sources/user_service_answers_20261008.json']:
 x=read(path)
 print('POLICY',path)
 for k,c in x.get('claims',{}).items():
  a=c['answers'];a=a if 'th' in a else {k:v for k,v in a.items()}
  for sub,val in ([('answer',a)] if 'th' in a else a.items()):print(k,sub,json.dumps(val,ensure_ascii=False),'TH_PRESENT',val.get('th','') in alltext,'EN_PRESENT',val.get('en','') in alltext)
 for v in x.get('items',[]):
  print('ITEM',json.dumps(v,ensure_ascii=False))
for x in json.loads((B/'AUDIT_SOURCE_STRUCTURE.json').read_text('utf8'))['descriptions']:
 if not x['exact']:print('FULLDESC',x['row'],x['game'],x['description'])
