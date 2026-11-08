"""Retained-plan replay and source/graph fault injection. No fresh inference.

These are implementation checks, not a semantic accuracy benchmark.
"""
import ast,copy,hashlib,json,os,sys,time,traceback
from pathlib import Path
R=Path(__file__).resolve().parent;ROOT=R.parent;OLD=ROOT/'r122_context_scope_calendar_20261022';TRAIN=ROOT/'r121_context_planner_training_20261022';S=R/'revision04_system'
OUT=R/('verification_'+str(time.time_ns()));OUT.mkdir()
os.environ.update(PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_DOMAIN_FLOW_ENABLED='1',PYTHONDONTWRITEBYTECODE='1')
sys.path.insert(0,str(S))
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.domain_flow.understanding import parse,Understanding,MeaningTask
from app.knowledge.common.domain_flow.meaning_review import review
from app.knowledge.common.domain_flow.context_guard import apply as guard
from app.knowledge.common.domain_flow.plan_contract import compile_request
from app.knowledge.common.domain_flow.obligation_verifier import assess
from app.knowledge.common.domain_flow.capabilities import matrix
from app.knowledge.common.domain_flow.contracts import Plan,RequestBudget
from app.knowledge.common.domain_flow.model import EvidenceSelector

def load(p):return json.loads(p.read_text('utf8'))
def rows(p):return [json.loads(s) for s in p.read_text('utf8').splitlines()]
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def write(name,v):(OUT/name).write_text(json.dumps(v,ensure_ascii=False,indent=2),'utf8')
freeze={str(p.resolve()):sha(p) for p in S.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc'}
freeze[str(Path(__file__).resolve())]=sha(Path(__file__));write('RUN_FREEZE.json',freeze)
checks={};replays=[]
try:
 engine=Engine.from_snapshot(MigratedView(S/'data/knowledge/common.sqlite').snapshot());index=engine.index
 snapshot={'release_id':engine.data.get('release_id'),'epoch':engine.data.get('epoch'),'reference_time':'2026-10-21T12:00:00+07:00'}
 def interpreted(raw,q):
  u=parse(raw,q);u.event['raw_content']=raw
  return review(q,index,u)
 labels=[(split,x) for split in ['train','validation','test'] for x in rows(TRAIN/(split+'.jsonl'))]
 compiled_labels=[]
 for split,x in labels:
  u=parse(json.dumps(x['label'],ensure_ascii=False),x['question']);assert u.accepted
  u=guard(x['question'],index,u);plan=compile_request(x['question'],u,index,snapshot)
  compiled_labels.append({'split':split,'key':x['key'],'question':x['question'],'plan':plan.as_dict()})
 write('LABEL_CONTRACT_AUDIT.json',compiled_labels)
 checks['all_289_prior_annotations_compile']=len(compiled_labels)==289
 checks['local_slots_stay_within_task']=all(t['source_span']['start']<=s['source_span']['start']<s['source_span']['end']<=t['source_span']['end'] for r in compiled_labels for t in r['plan']['tasks'] for s in t['slots'] if s['scope']=='local')
 write('CAPABILITY_MATRIX.json',matrix());checks['matrix_covers_14_categories']=len(matrix())==14
 checks['capabilities_do_not_claim_all_operations']=all(not r['all_operations_implemented'] for r in matrix())
 gold=rows(TRAIN/'test.jsonl');saved=rows(TRAIN/'train02/trained_test.jsonl')
 for g,pred in zip(gold,saved):
  assert g['key']==pred['key'];u=interpreted(pred['raw_output'],g['question']);before=copy.deepcopy(u.as_dict())
  result=engine.answer(g['question'],g['locale'],at=snapshot['reference_time'],allow_llm=False,understanding=u)
  checks['planner_proposal_not_mutated']=checks.get('planner_proposal_not_mutated',True) and u.as_dict()==before
  replays.append({'key':g['key'],'question':g['question'],'source':'saved_r121_trained_proposal','result':result})
 write('SAVED_PLANNER_REPLAY.json',replays)
 checks['30_retained_planner_outputs_replayed']=len(replays)==30
 checks['replay_has_no_model_calls']=all(not r['result']['model_events'] for r in replays)
 api=rows(OLD/'api02/trained/RESULTS.jsonl')+rows(OLD/'ellipsis01/trained/RESULTS.jsonl')
 api_replays=[]
 for row in api:
  old_u=row['response']['decision_artifact']['understanding'];q=old_u['event']['input_question']
  u=interpreted(old_u['event']['raw_content'],q)
  answer=engine.answer(q,row['locale'],at=snapshot['reference_time'],allow_llm=False,understanding=u)
  api_replays.append({'key':row['key'],'question':q,'result':answer})
 write('RETAINED_API_PROPOSAL_REPLAY.json',api_replays)
 checks['button_projection_not_false_gap']=replays[3]['result']['status']=='answer'
 checks['legacy_value_profile_not_false_gap']=all(replays[i]['result']['status']=='answer' for i in [5,19])
 checks['count_of_capacity_is_field_scope']=all(not any(o['kind']=='collection_scope' for o in t['obligations']) for row in compiled_labels for t in row['plan']['tasks'] if t['category']=='C03' and t['operation']=='count')
 checks['unproven_equipment_list_remains_partial']=api_replays[1]['result']['status']=='partial'
 checks['no_source_fatal_on_retained_proposals']=not any(t.get('fatal') for row in replays+api_replays for t in row['result'].get('execution_contract',{}).get('tasks',[]))

 vr=api_replays[-1];q=vr['question'];result=vr['result'];contract=result['execution_contract'];task0=contract['request_plan']['tasks'][0]
 checks['vr_has_both_source_durations']={c['value'] for c in result['needs'][0]['claims'] if c['facet']=='duration_minutes'}=={'30','60'}
 checks['vr_booking_keeps_source_claims']=bool(result['needs'][1]['claims'])
 checks['vr_booking_has_no_duration_slots']=not any(s['kind']=='duration' for s in contract['request_plan']['tasks'][1]['slots'])
 checks['vr_binding_does_not_wait_for_price']=all(not b['execution_dependency'] for b in contract['request_plan']['tasks'][1]['bindings'])
 checks['vr_comparison_options_verified']=all(o['fulfilled'] for o in result['needs'][0]['execution_contract']['obligations'] if o['kind']=='duration_option')
 # Recompile to dataclasses for direct fault injection, retaining the exact
 # same original question and plan. No new benchmark question is introduced.
 old_u=api[-1]['response']['decision_artifact']['understanding'];u=guard(q,index,interpreted(old_u['event']['raw_content'],q));compiled=compile_request(q,u,index,snapshot)
 first=copy.deepcopy(result['needs'][0]);first['claims']=[c for c in first['claims'] if str(index.records[c['record_id']]['fields']['duration_minutes']['value'])!='60']
 lost=assess(index,compiled.tasks[0],first,snapshot,q)
 checks['missing_comparison_option_detected']=not lost['all_obligations_fulfilled'] and 'comparison_option_not_delivered' in lost['reason_codes']
 tampered=copy.deepcopy(result['needs'][0]);tampered['claims'][0]['numeric']=999999
 bad=assess(index,compiled.tasks[0],tampered,snapshot,q)
 checks['forged_number_rejected']='source_receipt_numeric_mismatch' in bad['fatal']
 tampered=copy.deepcopy(result['needs'][0]);tampered['claims'][0]['evidence_refs']=[{'source_id':'not-in-snapshot','locator':'/invented'}]
 checks['forged_reference_rejected']=bool(assess(index,compiled.tasks[0],tampered,snapshot,q)['fatal'])
 tampered=copy.deepcopy(result['needs'][0]);tampered['claims'][0]['value']='Free access for everyone regardless of price'
 checks['forged_price_words_rejected']='source_receipt_value_mismatch' in assess(index,compiled.tasks[0],tampered,snapshot,q)['fatal']
 tampered=copy.deepcopy(result['needs'][0]);amount=next(c for c in tampered['claims'] if c['facet']=='amount');amount['numeric']=None
 checks['missing_price_number_rejected']='source_receipt_numeric_missing' in assess(index,compiled.tasks[0],tampered,snapshot,q)['fatal']

 tampered=copy.deepcopy(result['needs'][1]);tampered['claims'][0]['value']='invented permission'
 checks['forged_policy_text_rejected']='source_receipt_value_mismatch' in assess(index,compiled.tasks[1],tampered,snapshot,q)['fatal']
 tampered=copy.deepcopy(compiled);tampered.tasks[1].bindings[0].source_task_id='t2'
 try:tampered.validate();cycle=False
 except ValueError:cycle=True
 checks['cyclic_reference_rejected']=cycle
 # A pending first task must not prevent the later typed booking read. The
 # selector has zero budget and a transport that fails if a network call leaks.
 reads=[];native_plan=engine.plan
 def tracked_plan(cat,query,at=None,meaning=None):
  reads.append(cat)
  if cat=='C06':
   fact=next(f for f in index.bycat['C06'] if f['facet']=='amount')
   return Plan(category=cat,ambiguous=True,candidates=[fact['id']],facets=['amount'])
  return native_plan(cat,query,at,meaning)
 class Selector(EvidenceSelector):
  def select(self,tasks,budget):
   assert 'C08' in reads,'Fallback was scheduled before later typed read'
   return super().select(tasks,budget)
 def forbidden(*args,**kwargs):raise AssertionError('Unexpected network/model call')
 probe=Engine(engine.data,selector=Selector(transport=forbidden),_index=index);probe.plan=tracked_plan
 after=probe.answer(q,'en',at=snapshot['reference_time'],allow_llm=True,budget=RequestBudget(max_model_calls=0),understanding=interpreted(old_u['event']['raw_content'],q))
 checks['typed_booking_read_precedes_fallback']=reads[:2]==['C06','C08']
 checks['budget_exhaustion_is_not_transport_failure']=after['needs'][0]['execution_contract']['terminal_state']=='budget_exhausted'
 checks['later_booking_survives_zero_model_budget']=bool(after['needs'][1]['claims'])
 checks['budget_notice_does_not_claim_service_down']='unavailable' not in after['needs'][0]['answer'].lower()
 write('BUDGET_SCHEDULER_PROBE.json',after)
 unsupported=interpreted(old_u['event']['raw_content'],q);unsupported.tasks[0].facet='amount'
 unsupported_result=engine.answer(q,'en',at=snapshot['reference_time'],allow_llm=False,understanding=unsupported)
 checks['unsupported_compare_not_silently_detail']=unsupported_result['needs'][0]['reason']=='unsupported_operation' and not unsupported_result['needs'][0]['claims']
 checks['unsupported_first_task_does_not_drop_booking']=bool(unsupported_result['needs'][1]['claims'])
 invalid=Understanding([MeaningTask('not a substring','service_fee','C06','detail','amount')],True)
 bounded=engine.answer(q,'en',at=snapshot['reference_time'],allow_llm=False,understanding=invalid)
 checks['invalid_plan_is_bounded_without_facts']=bounded['status']=='missing_input' and not bounded['claims']
 for p in S.rglob('*.py'):ast.parse(p.read_text('utf-8-sig'))
 checks['candidate_python_sources_parse']=True
 checks['database_unchanged']=sha(S/'data/knowledge/common.sqlite')==freeze[str((S/'data/knowledge/common.sqlite').resolve())]
 checks['candidate_unchanged_during_verification']=all(sha(Path(p))==h for p,h in freeze.items())
 parent=load(R/'PARENT_FREEZE.json');checks['all_parent_files_unchanged']=all(sha(Path(p))==h for p,h in parent.items())
 summary={'all_passed':all(checks.values()),'checks':checks,'retained_annotation_rows':len(labels),'saved_planner_outputs':len(replays),'saved_api_proposals':len(api_replays),'new_model_inferences':0,'fresh_semantic_accuracy':None,'full_test':False,'production_installed':False,'output':str(OUT)}
 write('VERIFICATION.json',summary);print(json.dumps(summary,ensure_ascii=False,indent=2),flush=True)
 assert all(checks.values()),'Foundation checks failed; preserve this attempt'
except BaseException as exc:
 write('FAILED.json',{'error':repr(exc),'traceback':traceback.format_exc(),'checks_completed':checks});raise
