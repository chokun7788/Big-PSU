"""Pin source-only repairs and failed-then-repaired dependency evidence."""
import hashlib,json,time
from pathlib import Path
R=Path(__file__).resolve().parent
def read(p):return json.loads(p.read_text('utf8'))
def ref(name):
 p=R/name;return {'path':name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def save(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n','utf8')
new='stick_controller_predicates_1793109239382415500/RESULT.json'
scope='control_scope_1793109239362683900/RESULT.json'
prior='control_predicate_scope_1793109162686329700/RESULT.json'
for path in [new,scope,prior]:assert read(R/path)['all_passed']
before='saved_clause_discovery_1793108869730145200/DETAILS.json';after='saved_clause_discovery_1793109112815122300/DETAILS.json'
old=read(R/before);fresh=read(R/after)
assert sorted(x['row'] for x in old)==list(range(244,261))
assert sorted(x['row'] for x in fresh)==[250,254]
rows={x['row']:x for x in old};delta={x['row']:{'question':rows[x['row']]['question'],'before_answer':rows[x['row']]['answer'],'after_answer':x['answer']} for x in fresh}
findings=[('G123','Full recorded L (Left Stick) label lost to a single-letter L extraction, yielding unknown despite a matching source binding.','precision.py:controls; complete exact source labels precede component-key extraction.'),('G124','Named-game Thai controller-use question Fortnite ใช้จอยยังไง was answered with a game catalog rather than game-specific recorded controls.','control_intent.py:request; recognize bounded controller-use predicates while preserving catalog/compatibility/price/rule exclusions.'),('G125','Affected control-scope re-audit found Which buttons trigger <source action> compiled as list rather than inverse control action although selected facts were a subset.','control_intent.py:request; action predicate precedes plural-buttons list wording.')]
report={'actual_HTTP_or_model_inferences':0,'installed_revision':'R134','candidate_installed':False,'whole_flow_complete':False,'reviews_do_not_equal_training':True,'source_discovery_before':ref(before),'source_discovery_after':ref(after),'retained_failed_regression':ref('control_scope_1793109201331091600/RESULT.json'),'passed_controls':[ref(p) for p in [new,scope,prior]],'passed_control_counts':[15,25,23],'source_answer_deltas':delta,'findings':[{'id':i,'finding':f,'repair':c} for i,f,c in findings],'still_open_source_or_runtime_observations':{'244':'No complete Valorant sportsmanship source confirmed; do not substitute CS2.','245':'Genre source value delivered through bounded compatibility, final semantic execution remains pending.','247':'Truncated role returns no source dispatch; retain incomplete-role ambiguity, not a fabricated name.','248':'Wheel liability question not answered by native source dispatch; locale liability-condition conflict remains.','249':'Price result showed three audiences and did not verify both duration alternatives; retain requested-audience/duration application gap.','252_255':'Physical opening unknown/conflict disclosed separately from recorded play timetable; dated exceptions and final mapping proof remain.','253':'Before-match/on-site query returned source unknown despite multiple recorded linked clauses; routing/completeness investigation remains.','256':'General language query legitimately returns no source dispatch; previous audit harness assumed all questions returned an object. Harness now saves None explicitly and resumes only unsaved rows. This is not a content failure.','258':'General reservation-day/hour query returned no confirmed detail despite recorded bookable periods; native predicate/facet coverage investigation remains.'},'source_records_and_owner_data_modified':False,'remaining':'Other28 original sections/all14 final acceptance, actual model/training/three-arm evaluation/root/paired/final provenance/backup/normal activation/re-audit remain.'}
name='EXPEDITED_CONTROLS_SOURCE_REAUDIT_20261027.json';save(R/name,report)
g=read(R/'AUDIT_GAPS.json')
for i,f,c in findings:
 item={'id':i,'requirements':['C05','FLOW-13','CONTRACT-03'],'finding':f,'state':'implemented_component_verification_final_audit_pending','candidate_code':c,'source_reaudit':ref(name),'evidence':ref(scope if i=='G125' else new),'remaining':report['remaining']}
 existing=next((x for x in g['gaps'] if x['id']==i),None)
 if existing:assert existing==item
 else:g['gaps'].append(item)
g['last_recorded_at']=time.time();save(R/'AUDIT_GAPS.json',g)
s=read(R/'STATUS.json');s['latest_expedited_controls_reaudit']=ref(name)
for i,_,_ in findings:
 if i not in s['last_component_repairs']:s['last_component_repairs'].append(i)
s['last_recorded_at']=time.time();save(R/'STATUS.json',s)
print(json.dumps({'report':name,'repairs':[x[0] for x in findings],'passed_checks':[15,25,23],'whole_flow_complete':False}))
