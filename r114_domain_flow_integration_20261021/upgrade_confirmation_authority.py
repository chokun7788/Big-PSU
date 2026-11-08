"""Bind the existing owner per-person clarification to the imported rate scope."""
import hashlib,json,sys
from pathlib import Path
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R/'system'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import now
from app.knowledge.records import canonical_json
from app.knowledge.common.domain_flow.projection import value
store=CommonStore(R/'system/data/knowledge/common.sqlite');current=store.get('r114_rate_current_confirmation');record=current['record']
statements=json.loads((R.parent/'r109_owner_answers_20261020/MERGED_SERVICE_STATEMENTS.json').read_text('utf8'))['statements']
basis=next(x for x in statements if x['source_question_id']=='Q049')
scope=json.loads(value(record,'scope_note')['th']);scope['r114_confirmation']['per_person_scope']={'source_id':basis['id'],'answer_th':basis['answer_th'],'limits':basis.get('limits')}
record['fields']['scope_note']['value']={'th':json.dumps(scope,ensure_ascii=False),'en':json.dumps(scope,ensure_ascii=False)}
values={k:f['value'] for k,f in record['fields'].items() if f['status']=='known'}
raw=canonical_json({'fields':values,'original_per_person_statement':basis,'purpose':'As-of existing rate confirmation with explicit per-person basis; no effective-date change'})
sid='r114_affirm_rate_'+hashlib.sha256(raw.encode()).hexdigest()[:24]
store.add_source({'source_id':sid,'kind':'owner_document','path':'candidate-import://rate-owner-affirmation','sha256':hashlib.sha256(raw.encode()).hexdigest(),
 'authority_for':['faq','rate'],'observed_at':now(),'trust':'owner_confirmed','public_url':None},raw,actor='codex_candidate_import')
for k,f in record['fields'].items():
    if f['status']=='known':f['evidence_refs']=[{'source_id':sid,'locator':'/fields/'+k}]
result=store.save(record,actor='codex_candidate_import',expected_version=record['revision'],change_note='Attach existing owner per-person statement and rate source authority; no approval or validity change')
(R/'RATE_BILLING_BASIS_IMPORT.json').write_text(json.dumps({'record_id':record['record_id'],'new_version':result['version'],'source_id':sid,
 'original_statement':basis,'source_authority':['faq','rate'],'approvals_created':0,'effective_dates_changed':False},ensure_ascii=False,indent=2),'utf8')
print('Bound existing owner per-person statement to the existing rate affirmation.')
