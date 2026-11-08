"""Pin bounded regulation/overtime source review and regression evidence."""
import json,time
from verification_support import R
from app.knowledge.common.domain_flow.training_contract import file_sha
def read(p):return json.loads(p.read_text('utf8'))
def ref(p):return {'path':str(p.relative_to(R)),'sha256':file_sha(p)}
def save(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n','utf8')
source=R/'saved_clause_discovery_1793110072496582900/DETAILS.json';before=next(x for x in read(source) if x['row']==276)
tests=R/'rule_regime_scope_1793123415360008600';controls=read(tests/'RESULT.json');assert controls['all_passed'] and len(controls['checks'])==9
after=read(tests/'DETAILS.json')[0];dep=sorted(R.glob('rule_dependency_proofs_*/RESULT.json'))[-1];dr=read(dep);assert dr['all_passed']
failure=R/'rule_regime_scope_1793123356427316600/RESULT.json';assert not read(failure)['all_passed']
report={'question':before['question'],'before_answer':before['answer'],'after_answer':after['answer'],'before_source':ref(source),'after_source':ref(tests/'DETAILS.json'),'source_controls':{**ref(tests/'RESULT.json'),'checks':9},'dependency_regression':{**ref(dep),'checks':len(dr['checks'])},'retained_initial_failure':ref(failure),'failure_resolution':'The initial missing-source assertion did not accept the explicit stale-snapshot retry and the overtime body predicate also matched a different game timeout mentioning regulation rounds. The source predicate was narrowed to actual rounds-per-side or starting-money configuration, and missing data may safely yield a retry. The earlier harness wrapper also lacked connect(); it was repaired in the isolated test.','source_evidence':'Actual CS2 sections025 and027 provide distinct regulation and overtime clauses; unchanged model, SQL owner data and physical source documents. Event/source and stored completeness warnings remain. Numeric source values are neither hardcoded into candidate routing nor treated as full semantic acceptance.','actual_model_or_http_calls':0,'owner_frozen_data_modified':False,'whole_flow_complete':False,'remaining':'On-site preparation, sanctions, condition coverage, arbitrary competition topics, source authority/version/completeness, actual model/paired/final acceptance and all original76/14 obligations remain.'}
name=R/'RULE_REGIME_SOURCE_REAUDIT_20261028.json';save(name,report)
g=read(R/'AUDIT_GAPS.json');item={'id':'G129','requirements':['C13','FLOW-13','CONTRACT-03'],'finding':'A compound CS2 query for regulation starting money/bomb time and overtime rounds/starting money returned unconfirmed despite two separate source clauses. A first linguistic bridge mistakenly treated a different game timeout as overtime configuration.','state':'implemented_component_verification_final_audit_pending','candidate_code':'rule_semantics.py: separate requested regime topics, source-bound normative clause substance and narrow overtime configuration scope','source_reaudit':ref(name),'evidence':ref(tests/'RESULT.json'),'remaining':report['remaining']};previous=next((x for x in g['gaps'] if x['id']=='G129'),None)
if previous:assert previous==item
else:g['gaps'].append(item)
g['last_recorded_at']=time.time();save(R/'AUDIT_GAPS.json',g)
s=read(R/'STATUS.json');s['latest_rule_regime_reaudit']=ref(name)
if 'G129' not in s['last_component_repairs']:s['last_component_repairs'].append('G129')
s['last_recorded_at']=time.time();save(R/'STATUS.json',s);print(json.dumps({'report':str(name.relative_to(R)),'source_controls':9,'dependency_controls':len(dr['checks']),'whole_flow_complete':False}))
