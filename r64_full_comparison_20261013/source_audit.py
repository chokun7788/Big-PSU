import collections,json,sqlite3,sys
from pathlib import Path
import harness
B=Path(__file__).resolve().parent;harness.configure('common',False)
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import CATALOG
store=CommonStore(B/'common.sqlite')
with store.connect() as c:records=store.heads(c)
missing=[];time_sensitive=[];placeholders=[]
def slots(v,path=''):
 if isinstance(v,dict):
  if set(v)=={'th','en'}:yield path,v
  else:
   for k,x in v.items():yield from slots(x,path+'/'+k)
 elif isinstance(v,list):
  for i,x in enumerate(v):yield from slots(x,path+'/'+str(i))
for rid,r in records.items():
 for key,f in r['fields'].items():
  if f['status']=='known':
   for path,v in slots(f['value']):
    if v['th'] and not v['en']:missing.append({'record_id':rid,'kind':r['kind'],'field':key,'path':path,'th_chars':len(v['th'])})
    if v['th'] and '{service}' in v['th']:placeholders.append({'record_id':rid,'field':key})
 if r['kind'] in {'rate','rental_package','schedule','closure','competition','competition_rule','news'}:time_sensitive.append({'record_id':rid,'kind':r['kind'],'validity':r['validity']})
report={'records':len(records),'missing_english_slots':len(missing),'missing_english_by_kind':dict(collections.Counter(x['kind'] for x in missing)),'missing_english':missing,'time_sensitive':time_sensitive,'placeholders':placeholders,'scope':'coverage audit only; no translation or source approval'}
(B/'COMMON_SOURCE_AUDIT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in report.items() if k in {'records','missing_english_slots','missing_english_by_kind'}},ensure_ascii=False))
