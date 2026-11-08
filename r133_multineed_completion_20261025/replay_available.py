"""Append-only affected-input replay using only successfully received R132 wire.

No HTTP/model/provider is allowed. Cache misses remain unassessed. Inference
latency and queue outcomes cannot be inferred from a fast replay.
"""
import collections,gzip,hashlib,io,json,os,re,sys,time,urllib.request
from pathlib import Path
R=Path(__file__).resolve().parent;P=R.parent/'r132_flow_repairs_20261025';D=R.parent/'r131_diagnostic_review_20261025'
def load(p):return json.loads(p.read_text('utf-8-sig'))
def digest(x):return hashlib.sha256(json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def stream_partial(p):
 try:
  with gzip.open(p,'rt',encoding='utf8') as f:
   for line in f:
    try:yield json.loads(line)
    except ValueError:return
 except (EOFError,UnicodeError):return
out=R/'paired_source01';out.mkdir(exist_ok=True)
lock=out/'RUNNING.lock'
try:fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
except FileExistsError:raise SystemExit('Replay lock exists; verify PID before resuming, never duplicate active work')
os.write(fd,str(os.getpid()).encode());os.close(fd)
try:
 freeze=load(R/'EXECUTION_FREEZE_R133.json')
 changed=[p for p,h in freeze.items() if hashlib.sha256(Path(p).read_bytes()).hexdigest()!=h];assert not changed,changed
 for name in ['graph_protocol.py','model.py','understanding.py','model_gateway.py']:
  assert (R/'system/app/knowledge/common/domain_flow'/name).read_bytes()==(P/'system/app/knowledge/common/domain_flow'/name).read_bytes()
 jobs={j['key']:j for j in map(json.loads,(D/'SELECTED_JOBS.jsonl').open(encoding='utf8'))};members=load(D/'CATEGORY_MEMBERSHIP.json')['members'];eligible=[]
 for k,j in jobs.items():
  text=json.dumps([j['question'],j.get('history',[])],ensure_ascii=False)
  if set(members[k]['categories'])&{'C07','C13'} or re.search(r'แข่ง|กติกา|tourn|competition|rulebook|\bmatch\b|brightness|resolution|crosshair|\bplayers\b.{0,45}\bteam\b|notebook|laptop|off.?site|กลับบ้าน|เช่า|เหมา',text,re.I):eligible.append(k)
 selection={'eligible_keys':eligible,'eligible_requests':len(eligible),'total_selected_requests':len(jobs),'selection_basis':'all C07/C13 plus changed linguistic frames and competition/offsite history; defined independently of new answers','question_set_sha256':hashlib.sha256((D/'SELECTED_JOBS.jsonl').read_bytes()).hexdigest(),'model_inferences':0,'baseline_regrades':0}
 selection_path=out/'SELECTION.json'
 if selection_path.exists():assert load(selection_path)==selection
 else:selection_path.write_text(json.dumps(selection,ensure_ascii=False,indent=2),'utf8')
 measured={}
 for path in sorted((P/'sample01').glob('RESULTS_*.jsonl.gz')):
  for row in stream_partial(path):assert row['key'] not in measured;measured[row['key']]=row
 received={};failures={};per_request_receipts={};health=load(P/'MODEL_BEFORE.json')
 for row in measured.values():
  per_request_receipts[row['key']]={}
  a=(row.get('result') or {}).get('decision_artifact') or {}
  for e in (a.get('request_context') or {}).get('events',[]):
   if e.get('stage')!='R129_model_gateway':continue
   key=(e.get('model_stage'),e.get('profile'),e.get('wire_messages_sha256'),e.get('schema_sha256'))
   per_request_receipts[row['key']][key]=e
   if e.get('transport_ok'):
    prov=e.get('returned_provenance') or {};profile=key[1]
    assert profile in health['profiles'];assert prov.get('adapter_sha256')==health['profiles'][profile] and prov.get('profile_digest')==health['profile_digests'][profile] and prov.get('base_revision')==health['base_revision'] and prov.get('quantization')==health['quantization']
    received[key]=prov
   else:failures[key]=e.get('error','prior_transport_failure')
 raw={}
 log=R.parent/'r129_full_plan_completion_20261024/model_1792867147669903000/REQUESTS.jsonl'
 for line in log.open(encoding='utf8'):
  try:x=json.loads(line)
  except ValueError:continue
  if x.get('started_at',0)<1792937415 or not x.get('transport_ok'):continue
  v=x.get('provenance') or {};key=(v.get('stage'),v.get('effective_profile'),digest(x['input_messages']),digest(x.get('schema')))
  if key in received and v==received[key]:
   if key in raw:assert raw[key]['raw_output']==x['raw_output'],'Conflicting actual outputs for identical verified wire require review'
   raw[key]=x
 # Import the unchanged harness configuration, then select the frozen child.
 sys.path.insert(0,str(P));import run_common
 run_common.R=R;run_common.S=R/'system';sys.path.insert(0,str(R/'system'));os.environ['PSU_R88_RUN_TAG']='paired_source01';run_common.configure('replay')
 from app.pipeline.engine import answer_question_pipeline_debug
 from app.pipeline import llm_health
 from app.core.runtime_input_quality_guard import RuntimeInputQualityGuard
 from app.core.locale import resolve_locale
 from app.pipeline.input_recovery import inspect_surface_input
 from app.pipeline.schemas import PipelineAnswer,PipelineRoute,EntityBundle,ValidationResult
 from app.booking import live_status
 from app.runtime import fast_answer
 import reference_grader as grader
 def unavailable(d):return live_status._unavailable(d,'Same controlled unavailable as frozen R132; not live provider evidence',error_code='fixture_offline')
 live_status.get_live_booking_status=unavailable;fast_answer.get_live_booking_status=unavailable
 calls=[];current_key=None
 def no_network(req,*args,**kw):
  url=getattr(req,'full_url',str(req));assert ':12921/api/chat' in url,'No external/provider HTTP in replay: '+url
  payload=json.loads(req.data);stage=payload.get('stage','generic');profile=payload.get('planner_profile','retained') if stage=='context_understanding' else 'base';key=(stage,profile,digest(payload['messages']),digest(payload.get('format')));rec={'stage':stage,'profile':profile,'messages_sha256':key[2],'schema_sha256':key[3],'new_inference':False};calls.append(rec)
  prior=per_request_receipts[current_key].get(key)
  if prior is not None and not prior.get('transport_ok'):rec['status']='inherited_transport_failure';raise OSError('saved_R132_transport_failure: '+str(prior.get('error')))
  if key not in raw or prior is None:rec['status']='unassessed_cache_miss';raise OSError('strict_replay_cache_miss_no_inference_allowed')
  x=raw[key];cap=max(1,min(int((payload.get('options') or {}).get('num_predict',900)),900 if stage=='context_understanding' else 640));assert x['provenance']['effective_max_new_tokens']==cap
  assert x['provenance']==prior['returned_provenance']
  rec.update(status='verified_actual_raw_reused',generation_cap=cap,original_elapsed_sec=x['elapsed_sec'],generation_deadline_not_remeasured=True)
  return io.BytesIO(json.dumps({'model':health['model'],'message':{'role':'assistant','content':x['raw_output']},'done':True,'eval_count':x['eval_count'],'provenance':x['provenance']},ensure_ascii=False).encode())
 urllib.request.urlopen=no_network
 guard=RuntimeInputQualityGuard.from_environment();result_file=out/'RESULTS.jsonl';existing={x['key'] for x in map(json.loads,result_file.read_text('utf8').splitlines())} if result_file.exists() else set();todo=[k for k in eligible if k in measured and k not in existing];limit=int(os.environ.get('R133_REPLAY_LIMIT','100'))
 with result_file.open('a',encoding='utf8') as stream:
  for key in todo[:limit]:
   # Isolate cases from harness cache-miss cooldowns. This is source replay,
   # never a reproduction of the physical queue or cross-request latency.
   with llm_health._STATE_LOCK:llm_health._STATES.clear()
   current_key=key;j=jobs[key];calls.clear();started=time.perf_counter();q=j['question'];quality=guard.inspect(q);surface=inspect_surface_input(q);locale=resolve_locale(q,requested=j['locale'],keyboard_layout_direction=quality.locale_layout_direction,surface_language=surface.language if surface.should_review_intent else None)
   try:
    os.environ['PSU_ESPORTS_NOW']=(j.get('reference_date') or '2026-10-16')+'T12:00:00+07:00'
    if quality.should_short_circuit:
     text='The keyboard layout may not match the language you intended. Please check the keyboard language and type the question again.' if locale.effective=='en' else quality.message
     response=PipelineAnswer(answer=text,hits=[],elapsed=0,mode=quality.mode,confidence=0,route=PipelineRoute('input_guard',quality.flags[0] if quality.flags else 'input_quality',0,'clarification','low','input guard'),entities=EntityBundle(),validation=ValidationResult(True))
    else:response=answer_question_pipeline_debug(q,locale=j['locale'],locale_decision=locale,experimental_rag_fallback=False,experimental_allow_llm=True,global_timeout_sec=180,recent_history=j.get('history',[]))
    result=grader.plain(response);art=result.get('decision_artifact') or {};denied=any(e.get('stage')=='model_admission_denied' for e in (art.get('request_context') or {}).get('events',[]));transport_gap=any('model_transport_failure' in n.get('reason_codes',[]) for n in art.get('need_results',[]));unassessed=denied or transport_gap or any(c['status'] in {'unassessed_cache_miss','inherited_transport_failure'} for c in calls);grades=[]
    if not unassessed:
     for e in j['entries']:grades.append({'file':e['file'],'row':e['row'],'variant':e['variant'],**grader.grade(e['case'],response,Path(e['file']).name)})
    row={'key':key,'question':q,'requested_locale':j['locale'],'result':result,'saved_R132_answer':(measured[key].get('result') or {}).get('answer'),'answer_changed':result.get('answer')!=(measured[key].get('result') or {}).get('answer'),'replay_calls':list(calls),'new_inferences':0,'replay_status':'unassessed_missing_identical_wire_or_transport_state' if unassessed else 'source_execution_replay_complete_semantic_review_pending','grades':grades,'strict_performance_not_comparable':True,'health_state_isolated_per_request':True,'wall_sec_replay_only':time.perf_counter()-started}
   except Exception as exc:row={'key':key,'question':q,'requested_locale':j['locale'],'replay_status':'review_required_execution_exception','error':repr(exc),'replay_calls':list(calls),'new_inferences':0}
   stream.write(json.dumps(row,ensure_ascii=False)+'\n');stream.flush();print(json.dumps({'key':key[:8],'status':row['replay_status'],'changed':row.get('answer_changed'),'replayed_model_calls':len(calls)},ensure_ascii=False),flush=True)
 rows=[json.loads(l) for l in result_file.read_text('utf8').splitlines()];assert len(rows)==len({x['key'] for x in rows});assert all(x['new_inferences']==0 for x in rows)
 audit=load(out/'FIRST_BATCH_HEALTH_STATE_AUDIT.json')['effective_states'] if (out/'FIRST_BATCH_HEALTH_STATE_AUDIT.json').exists() else {}
 summary={'eligible_requests':len(eligible),'parent_completed_requests_available':len(measured),'replayed_requests':len(rows),'remaining_eligible_unmeasured_or_unreplayed':len(eligible)-len(rows),'statuses_after_saved_result_audit':dict(collections.Counter(audit.get(x['key'],x['replay_status']) for x in rows)),'changed_answers_raw_not_improvement_count':sum(x.get('answer_changed',False) for x in rows),'new_inferences':0,'baseline_regrades':0,'full_R133_fresh_execution_claimed':False,'semantic_review_complete':False,'latency_comparable':False,'updated_at':time.time()};(out/'PROGRESS.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),'utf8');print(json.dumps(summary,ensure_ascii=False))
 assert all(hashlib.sha256(Path(p).read_bytes()).hexdigest()==h for p,h in freeze.items())
finally:
 lock.unlink(missing_ok=True)
