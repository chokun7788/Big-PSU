"""Actual source transitive clause dependencies and adversarial receipt cuts."""
import copy,json,time,os
from unittest.mock import patch
from verification_support import R
from app.knowledge.common.registry import template
from app.knowledge.common.owner_server import save_owner_record
from app.knowledge.common.store import CommonStore
from app.knowledge.common.snapshot_provider import DraftSnapshotView
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import Understanding,MeaningTask
from app.knowledge.common.domain_flow.plan_contract import compile_request
from app.knowledge.common.domain_flow.obligation_verifier import assess
out=R/('rule_dependency_proofs_'+str(time.time_ns()));out.mkdir();os.environ['PSU_CONVERSATION_STATE_PATH']=str(out/'dialogue.sqlite');store=CommonStore(out/'source.sqlite');store.initialize(allow_demo=False);view=DraftSnapshotView(store);checks={};details=[];bi=lambda s:{'th':s,'en':s}
def create(kind,rid,fields):
 r=template(kind);r['record_id']=rid;r['localization']['en_status']='agent_translated'
 for k,v in fields.items():r['fields'][k]={'status':'known','value':v,'evidence_refs':[],'note':''}
 return save_owner_record(store,r,0,'controlled-test')['record']
game=create('game','game_topaz',{'title':bi('Topaz game')});events={};rules={}
for year in [2025,2026]:
 event=create('competition','cup_'+str(year),{'event_name':bi('Topaz Cup'),'game_id':game['record_id'],'rulebook_release':str(year),'coverage':'complete'});events[year]=event
 for key,heading,text,deps in [('staff','Staff call','Follow the designated official before proceeding.',[]),('safety','Player safety','Disconnect only when staff authorize it.',['staff']),('equipment','Competition equipment','Use the approved input devices and read the linked safety clause.',['safety']),('other','Venue entry','Check identification at entry.',[])]:
  rules[year,key]=create('competition_rule','rule_'+str(year)+'_'+key,{'competition_id':event['record_id'],'section_number':str(len(rules)+1),'facet':'game_specific','heading':bi(heading),'text':bi(str(year)+' '+text),'completeness':'complete','depends_on_ids':['rule_'+str(year)+'_'+d for d in deps]})
def run(q,op='rule_lookup'):
 e=Engine.from_snapshot(view.snapshot());u=Understanding([MeaningTask(q,'competition_rules','C13',op,'rule_clause')],True,'controlled_rule_dependencies',{'model_called':False})
 with patch('urllib.request.urlopen',side_effect=AssertionError('unexpected HTTP')):r=e.answer(q,'en',at='2026-10-26T12:00:00+07:00',allow_llm=False,understanding=u)
 details.append({'question':q,'operation':op,'result':r});return r,e,u
q='What are the competition equipment rules for Topaz Cup 2026?';r,e,u=run(q);expected={'rule_2026_equipment','rule_2026_safety','rule_2026_staff'};checks['actual_transitive_three_clause_chain_delivered']={c['record_id'] for c in r['claims']}==expected;checks['unrelated_clause_not_added']='rule_2026_other' not in {c['record_id'] for c in r['claims']}
snap=r['execution_contract']['request_plan']['snapshot'];task=compile_request(q,u,e.index,snap).tasks[0]
for removed in ['rule_2026_safety','rule_2026_staff']:
 child=copy.deepcopy(r['needs'][0]);child['claims']=[c for c in child['claims'] if c['record_id']!=removed];ledger=assess(e.index,task,child,snap,q);checks['removing_required_dependency_rejected_'+removed]=bool(ledger['fatal']) or any(not o['fulfilled'] for o in ledger['obligations']);details.append({'challenge':'remove_'+removed,'ledger':ledger})
for key in ['depends_on_ids','completeness','competition_id']:
 child=copy.deepcopy(r['needs'][0]);refs=e.index.records['rule_2026_equipment']['fields'][key]['evidence_refs'];child['claims']=[{**c,'evidence_refs':[v for v in c['evidence_refs'] if v not in refs]} if c['record_id']=='rule_2026_equipment' else c for c in child['claims']];checks['required_rule_scope_locator_'+key]=bool(assess(e.index,task,child,snap,q)['fatal'])
r,_,_=run('List all rules for Topaz Cup 2026','list');checks['list_all_current_event_clauses']={c['record_id'] for c in r['claims']}==expected|{'rule_2026_other'}
r,_,_=run('Compare competition equipment rules for Topaz Cup 2025 and Topaz Cup 2026','compare');checks['comparison_retains_each_editions_own_dependency_chain']={c['record_id'] for c in r['claims']}==expected|{'rule_2025_equipment','rule_2025_safety','rule_2025_staff'}
unknown=copy.deepcopy(rules[2026,'equipment']);unknown['fields']['depends_on_ids']={'status':'unknown','value':None,'evidence_refs':[],'note':'Dependency set is not confirmed'};save_owner_record(store,unknown,unknown['revision'],'controlled-test');r,_,_=run(q);checks['unknown_dependency_set_not_assumed_empty']=bool(r['claims']) and r['status']=='partial' and 'linked rule clauses' in r['answer'].lower()
restored=save_owner_record(store,rules[2026,'equipment'],2,'controlled-test')['record'];store.withdraw('rule_2026_safety',actor='controlled-test');r,_,_=run(q);checks['withdrawn_required_dependency_not_silently_skipped']=not r['claims']
report={'all_passed':all(checks.values()),'checks':checks,'actual_model_inferences':0,'actual_http_calls':0,'user_data_modified':False,'controlled_source_not_empirical_accuracy':True};(out/'RESULT.json').write_text(json.dumps(report,indent=2),'utf8');(out/'DETAILS.json').write_text(json.dumps(details,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'output':str(out),**report}));assert report['all_passed']
