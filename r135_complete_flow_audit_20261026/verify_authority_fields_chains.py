"""Owner-attested multi-step authority must cover the actual projected field."""
import copy,json,time
from verification_support import R
from app.knowledge.common.registry import template,value
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.authority_resolution import resolve
from app.knowledge.common.domain_flow.scope import reference_time
from app.knowledge.common.claim_bindings import validate_bindings
out=R/('authority_fields_chains_'+str(time.time_ns()));out.mkdir();store=CommonStore(out/'controlled.sqlite');store.initialize(allow_demo=False);checks={};details=[]
def create(kind,rid,fields):
 r=template(kind);r['record_id']=rid;r['localization']['en_status']='agent_translated';r['validity']={'state':'known','effective_from':'2026-01-01T00:00:00+07:00','effective_until':None}
 for k,v in fields.items():r['fields'][k]={'status':'known','value':v,'evidence_refs':[],'note':''}
 return save_owner_record(store,r,0,'controlled-test')['record']
service=create('service','authority_field_service',{'name':{'th':'บริการอำพัน','en':'Amber service'},'platform':'PC','resource_ids':[]})
records=[create('faq','authority_field_'+name,{'question':{'th':'วิธีจองบริการอำพัน '+name,'en':'How to book Amber '+name+'?'},'answer':{'th':'ขั้นตอน '+name,'en':name+' controlled procedure'},'topic':'C08','intent_key':'booking_steps'}) for name in ['old','middle','new']]
def binding(record,previous=None,field='answer',path=''):
 return {'binding_id':'booking','predicate':'booking_policy','subject_ref':service['record_id'],'value_ref':{'record_id':record['record_id'],'field':field,'path':path,'projection':'identity'},'unit':None,'actor_scope':{'status':'known','value':[]},'conditions_status':'known','condition_refs':[],'exceptions_status':'known','exception_refs':[],'applicability':{'status':'known','effective_from':'2026-01-01T00:00:00+07:00','effective_until':None,'service_ids':[service['record_id']],'duration_minutes':None,'platform':None},'dependency_refs':[],'supersedes_refs':[previous['record_id']+'#booking'] if previous else [],'evidence_refs':[],'authority_refs':[]}
def save(n,field='answer',path=''):
 record=copy.deepcopy(records[n]);record['claim_bindings']=[binding(record,records[n-1] if n else None,field,path)];records[n]=save_owner_record(store,record,record['revision'],'controlled-test',mapping_authority_confirmed=n>0)['record']
for n in range(3):save(n)
def run(label):
 view=DraftSnapshotView(store);engine=Engine.from_snapshot(view.snapshot(),cache_key=view.path);index=engine.index;facts=[f for r in records for f in index.byrecord[r['record_id']] if f['category']=='C08' and f['facet']=='owner_policy'];assert len(facts)==3
 result=resolve(index,facts,reference_time('2026-10-26T12:00:00+07:00'));errors={r['record_id']:validate_bindings(index.records[r['record_id']],index.records,index.source_pairs,publish=False,demo=False) for r in records};details.append({'case':label,'result':result,'validation_errors':errors,'records':{r['record_id']:index.records[r['record_id']] for r in records}});return result,errors
r,errors=run('whole_field_three_revision_chain');checks['valid_multi_step_authority_selects_final_source']=len(r['facts'])==1 and r['facts'][0]['record_id']==records[2]['record_id'] and set(r['superseded'])=={records[0]['record_id'],records[1]['record_id']};checks['chain_mapping_and_authority_source_pointers_valid']=all(not e for e in errors.values())
save(2,'question');r,errors=run('valid_authority_for_question_does_not_replace_answer');checks['different_field_binding_is_valid_source_mapping']=all(not e for e in errors.values());checks['question_authority_cannot_supersede_answer_field']={f['record_id'] for f in r['facts']}=={records[1]['record_id'],records[2]['record_id']}
save(2,'answer','/en');r,errors=run('valid_english_fragment_mapping_does_not_replace_whole_bilingual_answer');checks['projected_language_binding_is_valid_source_mapping']=all(not e for e in errors.values());checks['english_fragment_cannot_remove_whole_bilingual_prior_answer']={f['record_id'] for f in r['facts']}=={records[1]['record_id'],records[2]['record_id']}
save(1,'question');save(2);r,errors=run('superseded_binding_must_cover_actual_prior_projected_claim');checks['old_binding_other_field_cannot_remove_old_answer']=len(r['facts'])==3 and not r['superseded']
save(1);save(2);r,errors=run('restored_exact_whole_field_chain');checks['restored_source_chain_used_without_parser_edit']=len(r['facts'])==1 and r['facts'][0]['record_id']==records[2]['record_id']
centers=[]
for name in ['old','new']:
 record=create('center','authority_field_center_'+name,{'address':{'th':'ที่อยู่ '+name,'en':name+' address'},'building':name+' building'});b=binding(record);b['value_ref']['field']='address';b['supersedes_refs']=[centers[0]['record_id']+'#booking'] if centers else [];record['claim_bindings']=[b];centers.append(save_owner_record(store,record,record['revision'],'controlled-test',mapping_authority_confirmed=bool(centers))['record'])
view=DraftSnapshotView(store);index=Engine.from_snapshot(view.snapshot(),cache_key=view.path).index;facts=[f for r in centers for f in index.byrecord[r['record_id']] if f['facet'] in {'address','building'}];r=resolve(index,facts,reference_time('2026-10-26T12:00:00+07:00'));details.append({'case':'one_field_authority_preserves_other_field_in_same_record','result':r})
checks['supersession_is_per_fact_not_whole_record']={(f['record_id'],f['facet']) for f in r['facts']}=={(centers[0]['record_id'],'building'),(centers[1]['record_id'],'address'),(centers[1]['record_id'],'building')}
identical=create('center','authority_identical_fields',{'address':{'th':'Same room','en':'Same room'},'building':'Same room'});view=DraftSnapshotView(store);index=Engine.from_snapshot(view.snapshot(),cache_key=view.path).index;facts=[f for f in index.byrecord[identical['record_id']] if f['facet'] in {'address','building'}];r=resolve(index,facts,reference_time('2026-10-26T12:00:00+07:00'));details.append({'case':'equal_text_distinct_fields_are_not_literal_duplicate_claims','result':r});checks['identical_text_different_fields_not_deduplicated']=len(r['facts'])==2 and not r['duplicates']
actions=[create('faq','authority_action_'+intent,{'question':{'th':intent,'en':intent},'answer':{'th':'ติดต่อเจ้าหน้าที่','en':'Contact the staff'},'topic':'C08','intent_key':intent}) for intent in ['booking_steps','booking_cancel']];view=DraftSnapshotView(store);index=Engine.from_snapshot(view.snapshot(),cache_key=view.path).index;facts=[f for record in actions for f in index.byrecord[record['record_id']] if f['category']=='C08'];r=resolve(index,facts,reference_time('2026-10-26T12:00:00+07:00'));details.append({'case':'equal_text_different_declared_policy_actions_are_not_duplicate_claims','result':r});checks['identical_text_different_declared_actions_not_deduplicated']=len(r['facts'])==2 and not r['duplicates']
report={'all_passed':all(checks.values()),'checks':checks,'actual_model_inferences':0,'actual_http_calls':0,'user_data_modified':False,'controlled_owner_attestation_not_unrestricted_prose_entailment':True};(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');(out/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
