"""Preserve bounded repairs and an immutable semantic amendment separately."""
import json,time
from verification_support import R
from app.knowledge.common.domain_flow.training_contract import file_sha
def read(p):return json.loads(p.read_text('utf8'))
def ref(name):return {'path':name,'sha256':file_sha(R/name)}
def save(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n','utf8')
period='named_periods_1793110748091086700/RESULT.json';phone='declared_phone_field_1793111278541984400/RESULT.json';contact='contact_matrix_1793111271638366200/RESULT.json';core='core_verification_1793111292825237800/RESULT.json'
for n in [period,phone,contact]:assert read(R/n)['all_passed']
assert not read(R/core).get('failed')
amend='training_review_workbench_1793037663397671000/semantic_amendments_round014/AMENDMENT_266.json';assert read(R/amend)['current_v2_v3_cohorts_modified'] is False
before='saved_clause_discovery_1793110072496582900/DETAILS.json';after_period='saved_clause_discovery_1793110693421155600/DETAILS.json';after_contact='saved_clause_discovery_1793111194014373300/DETAILS.json'
old={d['row']:d for d in read(R/before)};deltas=[]
for path,row in [(after_period,267),(after_contact,278)]:
 new=next(d for d in read(R/path) if d['row']==row);deltas.append({'row':row,'question':new['question'],'before_answer':old[row]['answer'],'after_answer':new['answer'],'after_ref':ref(path)})
report={'candidate_installed':False,'installed_revision':'R134','actual_HTTP_or_model_inferences':0,'actual_optimizer_runs':0,'source_owner_frozen_model_assets_modified':False,'period_controls':{**ref(period),'checks':56},'phone_controls':{**ref(phone),'checks':11},'contact_regression':{**ref(contact),'checks':27},'core_regression':{**ref(core),'checks':54},'deltas':deltas,'semantic_amendment':ref(amend),'new_unique_questions_from_amendment':0,'current_cohorts_rebuilt':False,'identity_scope_still_review_required':True,'identity_probe_history':[ref('saved_clause_discovery_1793110909522790900/DETAILS.json'),ref('saved_clause_discovery_1793110969009646800/DETAILS.json'),ref('saved_clause_discovery_1793111044367366300/DETAILS.json'),ref('saved_clause_discovery_1793111130733689000/DETAILS.json'),ref('saved_clause_discovery_1793111194014373300/DETAILS.json')],'identity_experiment_handling':'Native identity/projection experiments did not pass bound-target/contact-subject source receipts. Their changes were removed; only proven explicit phone projection remains. Identity is still unconfirmed, not declared repaired.','remaining':'Dated service closure/changed-hours mapping, C13 predicates/compound regime clauses, damage conditions, price audience/duration proof, general reservation days/hours, semantic amendments/families/strata/protocol/model/actual optimization/three arms, remaining28 original sections/all14category/root/paired/final freeze/API/backup/normalactivation/re-audit remain.'}
name='PERIOD_PHONE_AMENDMENT_REAUDIT_20261027.json';save(R/name,report)
g=read(R/'AUDIT_GAPS.json')
items=[('G126','Explicit play-time question with weekday and named afternoon lacked the noun session, so native period recognition missed it and broad compatibility FAQ displaced the Monday scope.','period_scope.py:request',period,'implemented_component_verification_final_audit_pending'),('G127','Explicit source-declared contact_phone FAQ was projected as generic owner_policy and removed by channel filtering, leaving a source-backed phone question unconfirmed.','projection.py/contact_scope.py; source-declared typed phone fields, exact channel/subject checks, metadata refs and source edits',phone,'implemented_component_verification_final_audit_pending'),('G128','Row266 stage-selection label inserted competition context although raw wording did not specify ordinary gameplay versus tournament rules.','semantic_amendments_round014/AMENDMENT_266.json',amend,'individual_semantic_correction_staged_current_cohorts_not_refreshed')]
for i,f,c,e,state in items:
 item={'id':i,'requirements':['C11'] if i=='G126' else ['C01'] if i=='G127' else ['FLOW-13','CONTRACT-03'],'finding':f,'state':state,'candidate_code':c,'evidence':ref(e),'source_reaudit':ref(name),'remaining':report['remaining']}
 existing=next((x for x in g['gaps'] if x['id']==i),None)
 if existing:assert existing==item
 else:g['gaps'].append(item)
g['last_recorded_at']=time.time();save(R/'AUDIT_GAPS.json',g)
s=read(R/'STATUS.json');s['latest_period_phone_amendment_reaudit']=ref(name);s['latest_semantic_amendments']={'path':'training_review_workbench_1793037663397671000/semantic_amendments_round014','original_rows':[266],'adjudicated':True,'compiled':False,'new_unique_original_questions':0,'optimization_allowed_before_compile':False,'evidence':ref(amend)}
for i,_,_,_,_ in items:
 if i not in s['last_component_repairs']:s['last_component_repairs'].append(i)
s['last_recorded_at']=time.time();save(R/'STATUS.json',s)
print(json.dumps({'report':name,'source_controls':[56,11],'affected_regressions':[27,54],'row266_amendment_staged':True,'whole_flow_complete':False}))
