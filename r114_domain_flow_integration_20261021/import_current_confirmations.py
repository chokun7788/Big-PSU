"""Preserve the supplied price affirmation as an as-of source, not new dates."""
import hashlib,json,sys
from pathlib import Path
R=Path(__file__).resolve().parent;B=R.parent;sys.path.insert(0,str(R/'system'))
from app.knowledge.common.store import CommonStore
from app.knowledge.common.registry import template,now
from app.knowledge.records import canonical_json
from app.knowledge.common.domain_flow.projection import value

store=CommonStore(R/'system/data/knowledge/common.sqlite');rid='r114_rate_current_confirmation'
with store.connect() as c:records=CommonStore.heads(c)
if rid in records:raise SystemExit('Confirmation already imported; refusing overwrite')
source=json.loads((B/'r109_owner_answers_20261020/MERGED_SERVICE_STATEMENTS.json').read_text('utf8'))
statement=next(x for x in source['statements'] if x['source_question_id']=='group_rates')
fields_for_hash=['service_id','audience_id','amount_minor','currency','duration_minutes','persons_min','persons_max']
def fingerprint(r):return hashlib.sha256(canonical_json({k:value(r,k) for k in fields_for_hash}).encode()).hexdigest()
targets={k:fingerprint(r) for k,r in records.items() if r['kind']=='rate'}
meta={'r114_confirmation':{'kind':'rate_as_of_affirmation','as_of':statement['source_updated_at'],'record_value_hashes':targets,
 'fields_for_hash':fields_for_hash,'original_source_id':statement['id'],'validity_interval_established':False}}
bi=lambda s:{'th':s,'en':s}
values={'question':bi(statement['source_question']),'answer':{'th':statement['answer_th'],'en':'The owner reaffirmed the existing rates at the time of the answer. No new start or end date was established.'},
 'topic':'price','intent_key':'price.as_of_confirmation','related_ids':list(targets),'scope_note':bi(json.dumps(meta,ensure_ascii=False))}
raw=canonical_json({'fields':values,'original_statement':statement});sid='r114_affirm_'+hashlib.sha256(raw.encode()).hexdigest()[:24]
store.add_source({'source_id':sid,'kind':'owner_document','path':'candidate-import://'+rid,'sha256':hashlib.sha256(raw.encode()).hexdigest(),
 'authority_for':['faq'],'observed_at':now(),'trust':'owner_confirmed','public_url':None},raw,actor='codex_candidate_import')
r=template('faq');r['record_id']=rid;r['localization']['en_status']='agent_translated'
for k,v in values.items():r['fields'][k].update(status='known',value=v,evidence_refs=[{'source_id':sid,'locator':'/fields/'+k}],note='Source as-of affirmation; no invented effective dates')
store.save(r,actor='codex_candidate_import',expected_version=0,change_note='Preserve owner current-rate affirmation without changing rate validity or approvals')
(R/'CURRENT_RATE_CONFIRMATION_IMPORT.json').write_text(json.dumps({'record_id':rid,'source_id':sid,'as_of':statement['source_updated_at'],'rate_records_bound':len(targets),'approvals_created':0,'metadata':meta},ensure_ascii=False,indent=2),'utf8')
print(json.dumps({'candidate_confirmation_imported':True,'rates':len(targets),'effective_dates_changed':False}))
