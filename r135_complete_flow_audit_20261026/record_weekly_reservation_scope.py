"""Pin the reservation-calendar scope repair without claiming category completion."""
import json,time
from verification_support import R
from app.knowledge.common.domain_flow.training_contract import file_sha
def read(p):return json.loads(p.read_text('utf8'))
def ref(p):return {'path':str(p.relative_to(R)),'sha256':file_sha(p)}
def save(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n','utf8')
before_path=R/'saved_clause_discovery_1793108869730145200/DETAILS.json';before=next(r for r in read(before_path) if r['row']==258)
after_path=R/'saved_clause_discovery_1793123703943377600/DETAILS.json';after=read(after_path)[0];assert after['row']==258 and before['question']==after['question']
weekly=R/'weekly_calendar_1793123797783196600/RESULT.json';windows=R/'calendar_windows_1793123740666751200/RESULT.json'
assert read(weekly)['all_passed'] and read(windows)['all_passed']
failed=R/'weekly_calendar_1793123740687008500/RESULT.json';assert not read(failed)['all_passed']
report={'question':before['question'],'before_answer':before['answer'],'after_answer':after['answer'],'before_source':ref(before_path),'after_source':ref(after_path),'weekly_controls':{**ref(weekly),'checks':36},'window_regression':{**ref(windows),'checks':26},'retained_initial_harness_failure':ref(failed),'harness_correction':'An initial negative assertion incorrectly rejected a legitimate compound plan with separate reservation-calendar and price tasks. The corrected control verifies that both tasks survive rather than rejecting all calendar tasks.','bounds':'Only the recorded weekday booking periods are represented. Effective date interval and applicable resource or zone remain explicitly unconfirmed; these facts do not prove live vacancy or physical opening hours.','actual_model_or_http_calls':0,'actual_owner_frozen_data_modified':False,'whole_flow_complete':False}
name=R/'WEEKLY_RESERVATION_SCOPE_REAUDIT_20261028.json';save(name,report)
g=read(R/'AUDIT_GAPS.json');item={'id':'G130','requirements':['C11','FLOW-13','CONTRACT-03'],'finding':'A request for all studio service days and hours for reservations returned no confirmed detail because weekday-only native detection missed the weekly booking predicate.','state':'implemented_component_verification_final_audit_pending','candidate_code':'calendar_sets.py:weekly_requested; native_intents.py:weekly reservation-calendar predicate','evidence':ref(weekly),'source_reaudit':ref(name),'remaining':'Dated exceptions, applicability, other calendar predicates, actual model/API/paired/final acceptance and all original76/14 obligations remain.'};old=next((x for x in g['gaps'] if x['id']=='G130'),None)
if old:assert old==item
else:g['gaps'].append(item)
g['last_recorded_at']=time.time();save(R/'AUDIT_GAPS.json',g)
s=read(R/'STATUS.json');s['latest_weekly_reservation_reaudit']=ref(name)
if 'G130' not in s['last_component_repairs']:s['last_component_repairs'].append('G130')
s['last_recorded_at']=time.time();save(R/'STATUS.json',s);print(json.dumps({'report':str(name.relative_to(R)),'weekly_controls':36,'window_controls':26,'whole_flow_complete':False}))
