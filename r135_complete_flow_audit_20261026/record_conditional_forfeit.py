"""Keep conditional source excerpts and outstanding conflict separate."""
import json,time
from verification_support import R
from app.knowledge.common.domain_flow.training_contract import file_sha
def read(p):return json.loads(p.read_text('utf8'))
def ref(p):return {'path':str(p.relative_to(R)),'sha256':file_sha(p)}
def save(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n','utf8')
before_path=R/'saved_clause_discovery_1793110072496582900/DETAILS.json';before=next(x for x in read(before_path) if x['row']==261)
test=R/'conditional_forfeit_scope_1793123900654202700';after=read(test/'DETAILS.json')[0];tr=read(test/'RESULT.json');assert tr['all_passed'] and len(tr['checks'])==7 and before['question']==after['question']
dep=sorted(R.glob('rule_dependency_proofs_*/RESULT.json'))[-1];dr=read(dep);assert dr['all_passed']
report={'question':before['question'],'before_answer':before['answer'],'after_answer':after['answer'],'before_source':ref(before_path),'after_source':ref(test/'DETAILS.json'),'source_controls':{**ref(test/'RESULT.json'),'checks':7},'dependency_controls':{**ref(dep),'checks':len(dr['checks'])},'scope':'Three source-bound condition-specific TEKKEN clauses, with unverified condition/completeness warning. No unconditional forfeit or complete-rulebook claim.','source_conflict_review_required':'The retained pause clauses differ in wording about whether an otherwise justified pause can occur; displaying them does not resolve their relationship, authority or currentness.','actual_http_or_model_calls':0,'actual_owner_frozen_data_modified':False,'whole_flow_complete':False}
name=R/'CONDITIONAL_FORFEIT_REAUDIT_20261028.json';save(name,report)
g=read(R/'AUDIT_GAPS.json');item={'id':'G131','requirements':['C13','FLOW-13','CONTRACT-03'],'finding':'A TEKKEN question about possible forfeits returned unconfirmed despite recorded conditional sanction clauses; different breach conditions and round versus unspecified loss must not be collapsed into a universal verdict.','state':'implemented_component_verification_final_audit_pending','candidate_code':'rule_semantics.py: source-bound forfeit-scope detection and full clause selection','evidence':ref(test/'RESULT.json'),'source_reaudit':ref(name),'remaining':'Conflict/authority/version and rulebook completeness remain unresolved; broader condition handling, actual model/paired/final acceptance and all original76/14 obligations remain.'};old=next((x for x in g['gaps'] if x['id']=='G131'),None)
if old:assert old==item
else:g['gaps'].append(item)
g['last_recorded_at']=time.time();save(R/'AUDIT_GAPS.json',g)
s=read(R/'STATUS.json');s['latest_conditional_forfeit_reaudit']=ref(name)
if 'G131' not in s['last_component_repairs']:s['last_component_repairs'].append('G131')
s['last_recorded_at']=time.time();save(R/'STATUS.json',s);print(json.dumps({'report':str(name.relative_to(R)),'source_controls':7,'dependency_controls':len(dr['checks']),'whole_flow_complete':False}))
