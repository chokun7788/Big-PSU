"""Recover the omitted existing PC price source in a separate draft DB."""
import sys,json,sqlite3,hashlib,copy,dataclasses
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B/'system'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import template,value,now
from app.knowledge.records import canonical_json
from app.calculator.service_fee import SERVICE_FEES
from app.core.source_registry import get_source,PC_SERVICE_FEE_LOCAL_UPDATE_20260727_ID
target=B/'common_pc_candidate.sqlite'
if target.exists():raise FileExistsError(target)
with sqlite3.connect((B/'common.sqlite').as_uri()+'?mode=ro',uri=True) as src,sqlite3.connect(target) as dst:src.backup(dst)
s=CommonStore(target)
with s.connect() as c:records=s.heads(c);active=dict(c.execute('SELECT * FROM cc_meta'))['active']
services=[r for r in records.values() if r['kind']=='service' and value(r,'platform')=='PC']
audiences={}
for r in records.values():
 if r['kind']!='audience':continue
 n=value(r,'name') or {};en=n.get('en') or n.get('th')
 for label,key in [('PSU Student and Staff','psu_student_staff'),('PSU Alumni and General Student','general_student'),('General Adult','general_adult')]:
  if en==label:audiences[key]=r['record_id']
assert len(services)==2 and len(audiences)==3,(len(services),audiences)
oldrate=next(r for r in records.values() if r['kind']=='rate')
print('RATE_TEMPLATE',json.dumps({k:value(oldrate,k) for k in oldrate['fields']},ensure_ascii=False))
legacy=get_source(PC_SERVICE_FEE_LOCAL_UPDATE_20260727_ID)
assert legacy.trust_level=='user_confirmed'
proof=[]
for rel in ['app/calculator/service_fee.py','app/core/source_registry.py']:
 data=(B/'system'/rel).read_bytes();proof.append({'relative_path':rel,'sha256':hashlib.sha256(data).hexdigest(),'content':data.decode('utf-8-sig')})
saved=[];audit=[]
for service in services:
 for group,amount in SERVICE_FEES['pc']['prices'].items():
  rid='rate_recovered_pc_'+service['record_id']+'_'+group
  r=template('rate');r['record_id']=rid
  vals={'service_id':service['record_id'],'audience_id':audiences[group],'amount_minor':amount*100,'currency':'THB','unit':value(oldrate,'unit'),'duration_minutes':SERVICE_FEES['pc']['minutes_per_session'],'calculation_rule':value(oldrate,'calculation_rule')}
  raw=canonical_json({'mapped_fields':vals,'original_source_registry':dataclasses.asdict(legacy),'original_calculator_pc':SERVICE_FEES['pc'],'source_documents':proof,'booking_service':{'record_id':service['record_id'],'name':value(service,'name'),'platform':value(service,'platform')},'mapping_basis':'The existing PC calculator has one PC category and no separate price tier for its two PC booking options. No new amount or date is inferred.','validity_note':'Update/receipt date is not inferred as effective_from; validity remains unknown.'})
  sid='r66_pc_'+hashlib.sha256(raw.encode()).hexdigest()[:24]
  src={'source_id':sid,'kind':'derived_curated','path':'migration://r66/existing_pc_local_update/'+rid,'sha256':hashlib.sha256(raw.encode()).hexdigest(),'authority_for':['rate'],'observed_at':now(),'trust':'legacy_unreviewed','public_url':None};s.add_source(src,raw,actor='r66-pc-source-recovery')
  for key,v in vals.items():
   if v is not None:r['fields'][key].update(status='known',value=v,evidence_refs=[{'source_id':sid,'locator':'/mapped_fields/'+key}],note='Recovered existing PC calculator/source registry fact. No new price policy.')
  r['validity'].update(state='unknown',effective_from=None,effective_until=None)
  saved.append(s.save(r,actor='r66-pc-source-recovery',expected_version=0,change_note='Recover omitted user-confirmed local PC price source; draft only; do not infer effective dates'))
  audit.append({'record_id':rid,**vals})
with s.connect() as c:assert dict(c.execute('SELECT * FROM cc_meta'))['active']==active
(B/'PC_SOURCE_RECOVERY.json').write_text(json.dumps({'new_draft_db':str(target),'records':audit,'count':len(saved),'source_registry_declared_trust':legacy.trust_level,'new_owner_approval':False,'published':False,'validity':'unknown; no effective date invented'},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'new_draft_rates':len(saved),'published':False}))
