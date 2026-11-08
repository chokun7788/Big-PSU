"""Restore safe entity aliases from legacy code; never promote answer caches."""
import collections,copy,hashlib,json,re,shutil,sqlite3,sys
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'system';sys.path.insert(0,str(S))
load=lambda n:json.loads((R/n).read_text('utf8'))
assert load('http02/TEST_COMPLETE.json')['complete']
freeze=load('http02/RUN_FREEZE.json')['files'];assert all(hashlib.sha256(Path(p).read_bytes()).hexdigest()==h for p,h in freeze.items())
shutil.copytree(S,R/'http02/FROZEN_SYSTEM',ignore=shutil.ignore_patterns('__pycache__','*.pyc','*-wal','*-shm'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import value
store=CommonStore(S/'data/knowledge/common.sqlite')
with store.connect() as db:records={rid:json.loads(p) for rid,p in db.execute('SELECT h.record_id,r.payload FROM cc_heads h JOIN cc_revisions r ON h.record_id=r.record_id AND h.head=r.version WHERE h.withdrawn=0')}
before=copy.deepcopy(records);constants=load('CODE_CONSTANTS.json');decisions=[];added=[]
norm=lambda s:re.sub(r'[^\w]','',str(s).casefold())
def labels(r):
 field='title' if r['kind']=='game' else 'name'
 v=value(r,field) or {};return list(v.values()) if isinstance(v,dict) else [str(v)]
def resolve(kind,identity):
 names=[s for s in re.split(r'\s*/\s*',identity) if len(norm(s))>=5];matches=[]
 for rid,r in records.items():
  if r['kind']!=kind:continue
  hits=[len(norm(a)) for a in labels(r) for b in names if norm(a)==norm(b) or min(len(norm(a)),len(norm(b)))>=10 and (norm(a) in norm(b) or norm(b) in norm(a))]
  if hits:matches.append((max(hits),rid))
 if not matches:return []
 top=max(n for n,_ in matches);return [rid for n,rid in matches if n==top]
def process(source,key,kind,identity,aliases):
 targets=resolve(kind,identity);row={'source_path':source['path'],'constant':source['names'][0],'entry':key,'identity':identity,'target_ids':targets,
  'source_code_sha256':hashlib.sha256((S/source['path']).read_bytes()).hexdigest(),'aliases':aliases}
 if len(targets)!=1:row['disposition']='not_promoted_without_unique_existing_entity';decisions.append(row);return
 rid=targets[0];r=records[rid];count=0
 for a in aliases:
  if not isinstance(a,str) or len(a.strip())<2 or len(a)>200:continue
  lang='th' if re.search('[\u0e00-\u0e7f]',a) else 'en'
  if a in r['aliases'][lang]:continue
  collisions={oid for oid,other in records.items() if other['kind']==kind and oid!=rid and any(norm(a)==norm(s) for s in [*labels(other),*sum(other['aliases'].values(),[])])}
  if collisions:
   added.append({'record_id':rid,'alias':a,'disposition':'ambiguous_alias_not_added','other_ids':sorted(collisions),'source_path':source['path']});continue
  r['aliases'][lang].append(a);count+=1;added.append({'record_id':rid,'alias':a,'locale':lang,'disposition':'added_search_alias_only','source_path':source['path'],'constant':source['names'][0],'entry':key})
 row['disposition']='safe_aliases_added_or_already_present';row['new_aliases']=count;decisions.append(row)
for c in constants:
 if c['path']=='app/runtime/fast_answer.py' and c['names'][0] in {'EQUIPMENT_ITEM_DETAILS','GAME_DETAILS','ZONE_DETAILS'}:
  kind={'EQUIPMENT_ITEM_DETAILS':'equipment_model','GAME_DETAILS':'game','ZONE_DETAILS':'zone'}[c['names'][0]]
  for k,d in c['value'].items():process(c,k,kind,d.get('title') or d.get('name') or k,d.get('aliases',[]))
 if c['path']=='app/pipeline/structured_tools.py' and 'ZONE_ALIASES' in c['names']:
  for name,aliases in c['value'].items():process(c,name,'zone',name,aliases)
receipts=[]
for rid,r in records.items():
 if r!=before[rid]:receipts.append(store.save(r,actor='r119_legacy_code_alias_migration',expected_version=before[rid]['revision'],change_note='Restore uniquely matched search aliases from saved legacy code constants; business values, approvals and withdrawals unchanged'))
result={'entry_decisions':decisions,'alias_decisions':added,'new_aliases':sum(a['disposition']=='added_search_alias_only' for a in added),'ambiguous_aliases_not_added':sum(a['disposition']=='ambiguous_alias_not_added' for a in added),
 'records_revised':len(receipts),'save_receipts':receipts,'answer_cache_texts_promoted':0,'new_business_entities_invented':0,'approvals_changed':False}
(R/'CODE_ALIAS_MIGRATION.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),'utf8')
src=(R/'run_http02.py').read_text('utf8').replace("OUT=R/'http02'","OUT=R/'http03'").replace("'run_http.py','run_http02.py'","'run_http.py','run_http02.py','run_http03.py'")
(R/'run_http03.py').write_text(src,'utf8')
print(json.dumps({k:v for k,v in result.items() if k not in {'entry_decisions','alias_decisions','save_receipts'}},ensure_ascii=False))
