"""Finish a source-to-field mismatch discovered during the second review."""
import copy,hashlib,json,sqlite3,sys
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B/'system'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import value,now,safe_url,validate
from app.knowledge.records import canonical_json
db=B/'candidate05.sqlite'
if db.exists():raise SystemExit('Existing candidate05 preserved')
with sqlite3.connect((B/'candidate04.sqlite').as_uri()+'?mode=ro',uri=True) as s,sqlite3.connect(db) as d:s.backup(d)
store=CommonStore(db)
with store.connect() as c:rs=store.heads(c);sources=store.sources(c)
lineage=json.loads((B/'MIGRATION_LINEAGE.json').read_text('utf8'));repairs=[]
rel='data/curated/equipment_item_details.jsonl';p=B/'source_snapshot'/rel;raw=[json.loads(s) for s in p.read_text('utf8').splitlines() if s.strip()];x=raw[0]
assert x['id']=='equipment_gaming_pc'
specs=[{'key':'CPU','value':'Intel Core i5-14400','unit':None},{'key':'RAM','value':'DDR5 32GB','unit':None},{'key':'GPU','value':'NVIDIA GeForce RTX 5060 8GB','unit':None}]
assert all(s['value'] in x['note_th'] for s in specs)
rid=x['id'];v=value(rs[rid],'specifications')+specs
lineage.append({'record_id':rid,'field':'specifications','source_path':rel,'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'locator':'/0/note_th','source_value':x['note_th'],'mapped_value':v,'transform':'retain old zone/quantity and extract the three literal labeled hardware values; no external/current-spec assertion'})
r=copy.deepcopy(rs[rid]);r['fields']['specifications']['value']=v
payload={'mapped_fields':{'specifications':v},'field_lineage':[lineage[-1]],'status':'draft_only_not_owner_approved'};body=canonical_json(payload);sid='r68_specs_'+hashlib.sha256(body.encode()).hexdigest()[:24]
store.add_source({'source_id':sid,'kind':'derived_curated','path':'migration://r68/pc-specifications','sha256':hashlib.sha256(body.encode()).hexdigest(),'authority_for':['equipment_model'],'observed_at':now(),'trust':'legacy_unreviewed','public_url':x['source_url']},body,actor='r68-structured-repair')
r['fields']['specifications']['evidence_refs']=[{'source_id':sid,'locator':'/mapped_fields/specifications'}]
store.save(r,expected_version=r['revision'],actor='r68-structured-repair',change_note='Literal PC hardware facts existed only in usage text; expose them through specifications too')
with store.connect() as c:rs=store.heads(c);sources=store.sources(c)
# New migration evidence may cite the exact public source URL when all its
# original field locators agree on that URL. Never infer approval from an URL.
for rid,r in rs.items():
 current=copy.deepcopy(r);changed=False
 for sid in {ref['source_id'] for f in r['fields'].values() for ref in f.get('evidence_refs',[]) if ref['source_id'].startswith('r68_')}:
  source,body=sources[sid]
  if source.get('public_url'):continue
  data=json.loads(body);urls=set()
  for row in data.get('field_lineage',[]):
   sp=B/'source_snapshot'/row['source_path']
   if sp.suffix not in {'.json','.jsonl'}:continue
   if sp.suffix=='.jsonl':o=[json.loads(s) for s in sp.read_text('utf-8-sig').splitlines() if s.strip()];o=o[int(row['locator'].split('/')[1])]
   else:o=json.loads(sp.read_text('utf-8-sig'))
   url=o.get('source_url') or o.get('facts',{}).get('source_url')
   if url and safe_url(url):urls.add(url)
  if len(urls)!=1:continue
  url=next(iter(urls));new_source={**source,'source_id':'r68_url_'+hashlib.sha256((sid+url).encode()).hexdigest()[:24],'public_url':url,'observed_at':now()}
  store.add_source(new_source,body,actor='r68-source-citations')
  for field,f in current['fields'].items():
   for ref in f.get('evidence_refs',[]):
    if ref['source_id']==sid:ref['source_id']=new_source['source_id'];changed=True;repairs.append({'record_id':rid,'field':field,'source_id':sid,'replacement_source_id':new_source['source_id'],'public_url':url})
 if changed:store.save(current,expected_version=r['revision'],actor='r68-source-citations',change_note='Preserve source snapshot and trust; expose only its unique exact HTTPS source URL')
(B/'MIGRATION_LINEAGE.json').write_text(json.dumps(lineage,ensure_ascii=False,indent=2),encoding='utf8')
(B/'SOURCE_CITATION_REPAIRS.json').write_text(json.dumps(repairs,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps({'added_specifications':3,'citation_fields':len(repairs),'citation_records':len({x['record_id'] for x in repairs}),'candidate':str(db)}))
