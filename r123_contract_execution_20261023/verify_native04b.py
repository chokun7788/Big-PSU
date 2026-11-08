"""Native adapter/context fault gates using retained questions; no inference.

Provider observations are controlled fixtures, never real occupancy evidence.
"""
import copy,hashlib,json,os,sys,time,traceback
from pathlib import Path
from datetime import datetime,date,timedelta
from unittest.mock import patch
R=Path(__file__).resolve().parent;S=R/'revision04_system';ROOT=R.parent
OUT=R/('native_verification_'+str(time.time_ns()));OUT.mkdir()
os.environ.update(PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_DOMAIN_FLOW_ENABLED='1',PYTHONDONTWRITEBYTECODE='1')
sys.path.insert(0,str(S))
from app.knowledge.common.domain_flow.engine import Engine
from app.knowledge.common.domain_flow.understanding import parse,Understanding,MeaningTask
from app.knowledge.common.domain_flow.integration import answer
from app.knowledge.common.domain_flow.contracts import RequestBudget,Plan
from app.knowledge.common.domain_flow.request_provenance import capture,map_span
from app.knowledge.common.domain_flow.native_contract import receipt_checks,invalidate,attach_native,prepare
from app.knowledge.common.answer import CommonAnswerer
from app.knowledge.common.migrated_view import MigratedView
from app.knowledge.common.flow_context import request_context
from app.knowledge.common.normalized_query import normalize_query
from app.knowledge.common.registry import value
from app.booking.live_status import LiveBookingSnapshot,LiveResource,LiveSlot,resolve_live_target_date
from app.knowledge.common.domain_flow.scope import reference_time

def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def write(name,value):(OUT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2),'utf8')
freeze={str(p.resolve()):sha(p) for p in S.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc'}
freeze[str(Path(__file__).resolve())]=sha(Path(__file__));write('RUN_FREEZE.json',freeze)
checks={};outputs=[];calls=[]
try:
 store=MigratedView(S/'data/knowledge/common.sqlite');snap=store.snapshot();engine=Engine.from_snapshot(snap)
 records=snap['release']['records'];at=reference_time('2026-10-21T14:00:00+07:00')
 labels=[json.loads(s) for split in ('train','validation','test') for s in (ROOT/'r121_context_planner_training_20261022'/(split+'.jsonl')).read_text('utf8').splitlines()]
 def task_meaning(row):
  u=parse(json.dumps(row['label'],ensure_ascii=False),row['question']);assert u.accepted
  return u
 def run(row,provider=None,**kwargs):
  with patch('app.booking.live_status.get_live_booking_status',provider or unavailable):
   out=answer(CommonAnswerer(store),row['question'],locale='en' if row['question'].isascii() else 'th',at=at,
      planner=None,_understanding=task_meaning(row),**kwargs)
  assert out is not None
  outputs.append({'key':row['key'],'question':row['question'],'answer':out.answer,'artifact':out.decision_artifact,
     'validation':out.validation.ok,'controlled_provider_fixture':True})
  return out
 def fixture(day,*,stale=False,wrong_date=False,ok=True):
  calls.append(day);generated=at-timedelta(minutes=60) if stale else at
  resources=[]
  for r in records.values():
   if r['kind']!='live_binding':continue
   raw=next((x['raw'] for x in value(r,'status_mapping') or [] if x['normalized']=='free'),None)
   if raw is None:continue
   resources.append(LiveResource(value(r,'external_resource_key'),'controlled test',1,raw,1,(LiveSlot('09:00','18:00',raw,0,0,1),)))
  return LiveBookingSnapshot(ok=ok,date='1999-01-01' if wrong_date else day,now=at.isoformat(),generated_at=generated.isoformat(),
      source='controlled_verification_fixture',center_open=True,center_reason='fixture',open_periods=(('09:00','18:00'),),resources=tuple(resources),
      error_code='' if ok else 'controlled_provider_unavailable')
 def unavailable(day):return fixture(day,ok=False)

 checks['relative_date_uses_pinned_request_clock']=resolve_live_target_date('tomorrow',reference_date=date(2020,1,1))=='2020-01-02'
 checks['explicit_iso_date_preserved']=resolve_live_target_date('2020-02-04',reference_date=date(2020,1,1))=='2020-02-04'
 # Retained questions with actual source bindings. Native and typed-source
 # outcomes are both recorded; a binding gap must not turn into occupancy.
 live_rows=[x for x in labels if len(x['label']['tasks'])==1 and x['label']['tasks'][0]['domain']=='live'][:8]
 for row in live_rows:run(row)
 checks['all_retained_live_outputs_have_contract']=all(x['artifact'].get('execution_contract') for x in outputs)
 checks['provider_failure_never_becomes_supported']=all(not any(t.get('terminal_state')=='supported' for t in x['artifact']['execution_contract'].get('tasks',[])) for x in outputs)
 checks['live_provider_reads_use_pinned_day']=all(day.startswith('2026-10-') for day in calls)
 bound=next((x for x in live_rows if any('live_binding' in json.dumps(y['artifact'],ensure_ascii=False) and y['key']==x['key'] for y in outputs)),None)
 # Find a genuinely executed provider path, rather than silently treating an
 # unknown resource guard as a successful provider test.
 bound=next((x for x in live_rows if any(y['key']==x['key'] and y['artifact']['execution_contract'].get('path')=='native_calendar_live_bridge' for y in outputs)),None)
 checks['at_least_one_real_native_live_path_exercised']=bound is not None
 if bound:
  fresh=run(bound,fixture);stale=run(bound,lambda d:fixture(d,stale=True));wrong=run(bound,lambda d:fixture(d,wrong_date=True))
  fresh_c=fresh.decision_artifact['execution_contract']
  checks['fresh_native_observation_receipts_checked']=bool(fresh_c['tasks'][0]['live_observations']) and all(o.get('binding_mapping_and_clock_checked') for o in fresh_c['tasks'][0]['live_observations'] if o['terminal_state']=='supported')
  checks['stale_observation_not_supported']=not any(o['terminal_state']=='supported' for o in stale.decision_artifact['execution_contract']['tasks'][0]['live_observations'])
  checks['wrong_observation_date_not_supported']=not any(o['terminal_state']=='supported' for o in wrong.decision_artifact['execution_contract']['tasks'][0]['live_observations'])
  forged=copy.deepcopy(fresh.decision_artifact)
  obs=(forged.get('live_booking') or {}).get('observations',[])
  if obs:
   obs[0].update(status='supported',freshness_checked=True,observed_at=(at-timedelta(days=3)).isoformat())
   from dataclasses import replace
   checks['forged_freshness_flag_rejected']='native_live_mapping_or_freshness_mismatch' in receipt_checks(replace(fresh,decision_artifact=forged),snap,at)[2]
  else:checks['forged_freshness_flag_rejected']=False
  with request_context():
   before=len(calls)
   run(bound,fixture);run(bound,fixture)
   checks['same_request_provider_snapshot_reused']=len(calls)-before==1
 # Native opening adapter path is forced only at dispatch, with the real
 # copied records, normal native implementation and real finish/attach.
 opening=next(x for x in labels if x['question']=='ขอสอบถามหน่อยครับ วันนี้เปิดไหม')
 original_plan=Engine.plan
 def route_native(self,cat,q,*args,**kwargs):
  return Plan(category='C11',reason='controlled_native_dispatch') if cat=='C11' else original_plan(self,cat,q,*args,**kwargs)
 with patch.object(Engine,'plan',route_native):cal=run(opening)
 checks['native_calendar_has_compiled_plan']=cal.decision_artifact['execution_contract']['path']=='native_calendar_live_bridge'
 checks['calendar_does_not_assert_live_occupancy']=cal.decision_artifact['query_plan'].get('live_availability_asserted') is False
 # Verify a real receipt rejection independently of current calendar gaps.
 bogus=copy.deepcopy(cal.decision_artifact);bogus['obligations']=[{'record_id':next(iter(records)),'field':'imaginary','status':'known','evidence_refs':[{'source_id':'forged','locator':'x'}]}]
 from dataclasses import replace
 checks['forged_native_source_pointer_rejected']='native_source_receipt_mismatch' in receipt_checks(replace(cal,decision_artifact=bogus),snap,at)[2]
 compound=next(x for x in labels if x['question']=='How to book VR and what days are available')
 combined=run(compound);cc=combined.decision_artifact['execution_contract']
 checks['compound_compiles_whole_question_once']=cc['path']=='native_compound_bridge' and len(cc['request_plan']['tasks'])==2
 checks['compound_keeps_two_task_results']=len(cc['tasks'])==2
 checks['compound_does_not_claim_global_typed_first']=cc['typed_reads_before_fallback'] is False
 # An unrelated conversation history must not disable the compiled executor.
 booking=next(x for x in labels if len(x['label']['tasks'])==1 and x['label']['tasks'][0]['domain']=='reservation')
 q=booking['question'];proposal=task_meaning(booking)
 history=[{'role':'assistant','content':'Untrusted old prose says everything is free.'}]
 with request_context():h=engine.answer(q,'en',at=at,allow_llm=False,history=history,understanding=proposal)
 checks['ordinary_history_does_not_bypass_compiler']=h['execution_contract']['path']=='compiled_legacy_wire'
 checks['untrusted_prose_not_accepted_as_state']=h['execution_contract']['request_context']['history']['native_delivered_state_accepted'] is False
 # Provenance mapping with an existing retained question, including removed
 # polite prefix. Capture the raw input at the real request-context boundary.
 raw=opening['question'];normalized=normalize_query(raw)
 with request_context() as ctx:
  ctx.input={'raw_question':raw,'normalized_question':normalized.text,'span_map':normalized.public()}
  p=capture(normalized.text);span={'start':0,'end':len(normalized.text),'text':normalized.text};m=map_span(p,span)
 checks['normalized_span_maps_back_to_current_raw']=m['text']==raw[m['start']:m['end']] and m['start']>0
 # Real saved missing-input envelope; not assistant answer text. Derived text
 # is deliberately not labeled as a literal quote of the current user turn.
 current='30 minutes';prior='VR price';pending={'version':1,'category':'C06','query':prior,'root_ids':[],'slot':'duration'}
 trusted=[{'role':'assistant','delivery_status':'server_written','common_read_state':{'schema_version':1,'r114_pending':pending}}]
 from app.knowledge.common.domain_flow.financial import resume_financial
 from app.knowledge.common.domain_flow.request_provenance import derived_input
 resumed=resume_financial(current,trusted,records)
 with request_context() as ctx:
  ctx.input={'raw_question':current}
  derived_input(resumed,'delivered_financial_resume',[{'origin':'delivered_pending_query','text':prior},{'origin':'current_user_reply','text':current}])
  c=capture(resumed,trusted);m=map_span(c,{'start':0,'end':len(prior),'text':prior})
 checks['resumed_history_never_fakes_current_raw_span']=c['input_basis']=='delivered_financial_resume' and m['status']=='derived_source_basis'
 checks['resume_inherits_no_answer_facts']=c['history']['facts_inherited'] is False
 invalidated=invalidate(cc)
 checks['retry_clears_all_top_level_receipts']=all(t['terminal_state']=='not_current' and not t['receipts'] for t in invalidated['tasks'])
 checks['retry_clears_nested_child_receipts']=all(not n.get('receipts') for t in invalidated['tasks'] for n in t.get('child_contract',{}).get('tasks',[]))
 checks['candidate_unchanged_during_verification']=all(sha(Path(p))==h for p,h in freeze.items())
 write('OUTPUTS.json',outputs)
 write('VERIFICATION.json',{'all_passed':all(checks.values()),'checks':checks,'provider_calls':calls,'new_model_calls':0,
  'actual_http_test':False,'semantic_accuracy':None,'fresh_occupancy_verified':False,'controlled_native_dispatch_fixture':True})
 print(json.dumps({'all_passed':all(checks.values()),'checks':checks,'output':str(OUT)},ensure_ascii=False,indent=2),flush=True)
 assert all(checks.values())
except Exception:
 write('FAILURE.json',{'checks':checks,'error':traceback.format_exc()});print(traceback.format_exc(),flush=True);raise
