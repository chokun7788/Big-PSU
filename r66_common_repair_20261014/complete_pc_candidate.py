import sys,json,hashlib,copy,inspect
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path.insert(0,str(B/'system'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import now
from app.knowledge.records import canonical_json
from app.calculator.service_fee import _sessions_for
s=CommonStore(B/'common_pc_candidate.sqlite')
with s.connect() as c:records=s.heads(c)
saved=[]
for rid,r0 in records.items():
 if not rid.startswith('rate_recovered_pc_'):continue
 r=copy.deepcopy(r0);values={'unit':'per_session','persons_min':1,'persons_max':1,'calculation_rule':'session_ceil'}
 code=inspect.getsource(_sessions_for)
 assert 'math.ceil' in code and [_sessions_for('pc',m) for m in [30,60,61,120]]==[1,1,2,2]
 raw=canonical_json({'mapped_fields':values,'legacy_calculator_function':code,'legacy_source_path':'app/calculator/service_fee.py','legacy_file_sha256':hashlib.sha256((B/'system/app/calculator/service_fee.py').read_bytes()).hexdigest(),'existing_pc_capacity':'1 คน','original_field_evidence':r0['fields']['amount_minor']['evidence_refs'],'billing_rule_basis':'Exact existing _sessions_for PC algorithm; one confirmed PC session is 60 minutes. No prorating or new price is invented.'});sid='r66_pc_billing_'+hashlib.sha256(raw.encode()).hexdigest()[:24]
 source={'source_id':sid,'kind':'derived_curated','path':'migration://r66/pc-existing-billing/'+rid,'sha256':hashlib.sha256(raw.encode()).hexdigest(),'authority_for':['rate'],'observed_at':now(),'trust':'legacy_unreviewed','public_url':None};s.add_source(source,raw,actor='r66-existing-billing-recovery')
 for key,value in values.items():r['fields'][key].update(status='known',value=value,evidence_refs=[{'source_id':sid,'locator':'/mapped_fields/'+key}],note='Exact existing calculator algorithm/capacity; draft source recovery.')
 saved.append(s.save(r,actor='r66-existing-billing-recovery',expected_version=r0['revision'],change_note='Preserve existing ceil-session billing in an explicit schema value; no date inferred'))
(B/'PC_BILLING_RECOVERY.json').write_text(json.dumps({'draft_revisions':len(saved),'published':False,'date_inferred':False}),encoding='utf-8')
