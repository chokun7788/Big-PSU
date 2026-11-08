"""Common-only ON evaluation with append-only results and bounded subprocesses."""
from __future__ import annotations
import collections,dataclasses,gzip,hashlib,importlib.util,json,multiprocessing as mp,os,queue,sys,threading,time,traceback,urllib.request
from datetime import datetime,date
from pathlib import Path
R=Path(__file__).resolve().parent;B=R.parent;S=R/'system'
sys.path[:0]=[str(S),str(R)]
def configure(worker):
 t=R/'runtime'/os.getenv('PSU_R88_RUN_TAG','unassigned')/str(worker);t.mkdir(parents=True,exist_ok=True)
 os.environ.update(PYTHONUTF8='1',PYTHONDONTWRITEBYTECODE='1',PYTHONPATH=str(S),PSU_COMMON_CHAT_PROFILE='r69-migration-preview',PSU_KNOWLEDGE_DB=str(S/'data/knowledge/common.sqlite'),PSU_CHAT_LOG_DIR=str(t/'logs'),PSU_CHAT_LOG_SQLITE_PATH=str(t/'logs/transcripts.sqlite'),PSU_CONVERSATION_STATE_PATH=str(t/'state.sqlite'),PSU_CHAT_LOG_WEBHOOK_URL='',PSU_CHAT_LOG_POSTGRES='0',PSU_LOCAL_LLM_ASSIST_ENABLED='1',PSU_EXPERIMENTAL_ALLOW_LLM='1',PSU_BILINGUAL_EN_ENABLED='1',PSU_LLM_PREFLIGHT='0',PSU_PIPELINE_WARMUP='0',PSU_INPUT_QUALITY_GUARD_MODE='enforce',PSU_INPUT_QUALITY_REPEAT_POLICY='warn_and_continue',PSU_PIPELINE_GLOBAL_TIMEOUT_SEC='18',PSU_PRODUCT_BACKEND_TIMEOUT_SEC='20',PSU_QUERY_PLANNER_TIMEOUT_SEC='2.5',PSU_LLM_MAX_CONCURRENCY='1',PSU_SEMANTIC_RETRIEVAL='1',PSU_ESPORTS_NOW='2026-10-16T12:00:00+07:00')
def partitions(failures):
 buckets={k:[] for k in ('protocol','outcome','evidence','content','validation','performance','grader')}
 for reason in failures:
  s=str(reason)
  if s.startswith(('route:','intent:','legacy_mode_prefix:','forbidden_category','route expected','route_mismatch')):k='protocol'
  elif s.startswith(('status:','outcome expected','outcome_mismatch')):k='outcome'
  elif s.startswith(('missing rulebook target','retrieval evidence','wrong_game_evidence')):k='evidence'
  elif s.startswith(('validation','pipeline_exception')):k='validation'
  elif 'latency' in s or 'timeout' in s:k='performance'
  elif s.startswith('grader_exception'):k='grader'
  else:k='content'
  buckets[k].append(s)
 return buckets
def child(conn,worker_id,channel):
 configure(worker_id)
 from app.pipeline.llm_health import configure_model_admission
 configure_model_admission(*channel,1)
 from app.pipeline.engine import answer_question_pipeline_debug
 from app.core.runtime_input_quality_guard import RuntimeInputQualityGuard
 from app.core.locale import resolve_locale
 from app.pipeline.input_recovery import inspect_surface_input
 from app.pipeline.schemas import PipelineAnswer,PipelineRoute,EntityBundle,ValidationResult
 from app.booking import live_status
 from app.runtime import fast_answer
 from unittest.mock import patch
 import reference_grader as grader
 def unavailable(d):return live_status._unavailable(d,'R88 controlled unavailable; no actual booking oracle',error_code='fixture_offline')
 live_status.get_live_booking_status=unavailable;fast_answer.get_live_booking_status=unavailable
 guard=RuntimeInputQualityGuard.from_environment()
 # Observe real local-model HTTP attempts without changing calls or responses.
 native_urlopen=urllib.request.urlopen;calls=[]
 def observed_urlopen(req,*a,**kw):
  url=getattr(req,'full_url',str(req));local_model=(':11434/' in url)
  record={'url':url,'transport_ok':False,'started':time.perf_counter()}
  if local_model:calls.append(record)
  try:
   response=native_urlopen(req,*a,**kw);record['transport_ok']=True;return response
  except Exception as exc:record.update(error_type=type(exc).__name__,error=str(exc));raise
  finally:record['elapsed_sec']=time.perf_counter()-record.pop('started')
 urllib.request.urlopen=observed_urlopen
 conn.send({'event':'ready','pid':os.getpid()})
 while True:
  job=conn.recv()
  if job is None:break
  started=time.perf_counter();calls.clear()
  try:
   q=job['question'];quality=guard.inspect(q);surface=inspect_surface_input(q)
   locale=resolve_locale(q,requested=job['locale'],keyboard_layout_direction=quality.locale_layout_direction,surface_language=surface.language if surface.should_review_intent else None)
   if quality.should_short_circuit:
    text=('The keyboard layout may not match the language you intended. Please check the keyboard language and type the question again.' if locale.effective=='en' else quality.message)
    result=PipelineAnswer(answer=text,hits=[],elapsed=time.perf_counter()-started,mode=quality.mode,confidence=0,route=PipelineRoute('input_guard',quality.flags[0] if quality.flags else 'input_quality',0,'clarification','low','input guard'),entities=EntityBundle(),validation=ValidationResult(True))
   else:
    previous=os.environ.get('PSU_ESPORTS_NOW')
    if job.get('reference_date'):os.environ['PSU_ESPORTS_NOW']=job['reference_date']+'T12:00:00+07:00'
    try:result=answer_question_pipeline_debug(q,locale=job['locale'],locale_decision=locale,experimental_rag_fallback=False,experimental_allow_llm=True,global_timeout_sec=18,recent_history=job.get('history',[]))
    finally:
     if previous is None:os.environ.pop('PSU_ESPORTS_NOW',None)
     else:os.environ['PSU_ESPORTS_NOW']=previous
   grades=[]
   for entry in job['entries']:
    try:g=grader.grade(entry['case'],result,Path(entry['file']).name)
    except Exception as e:g={'passed':False,'failures':['grader_exception:'+type(e).__name__+':'+str(e)],'evidence_level':'grader_error'}
    c=entry['case'];contract=c.get('answer_contract') or c
    positive=bool(c.get('required_clauses') or c.get('clauses') or any(contract.get(k) for k in ('must_contain','must_contain_any','must_contain_all_groups')))
    grades.append({'file':entry['file'],'row':entry['row'],'variant':entry['variant'],'id':c.get('id'),**g,'partitions':partitions(g['failures']),'positive_text_contract':positive,'review_status':c.get('review_status',c.get('review'))})
   response=grader.plain(result)
   response['evaluation']={'format':'common','llm_enabled':True,'profile':'r69-migration-preview','draft_only':True,'legacy_fallback':False,'booking':'controlled_unavailable','reference_clock':job.get('reference_date') or '2026-10-16'}
   row={'key':job['key'],'question':q,'requested_locale':job['locale'],'effective_locale':getattr(result.language,'effective',locale.effective),'stratum':job['r70_stratum'],'elapsed_sec':time.perf_counter()-started,'result':response,'input_quality':quality.to_public_dict(),'grades':grades,'observed_model_http_calls':list(calls)}
   conn.send({'event':'result','row':row})
  except BaseException as e:
   conn.send({'event':'result','row':{'key':job['key'],'question':job['question'],'requested_locale':job['locale'],'stratum':job['r70_stratum'],'elapsed_sec':time.perf_counter()-started,'exception':repr(e),'traceback':traceback.format_exc(),'observed_model_http_calls':list(calls),'grades':[]}})
 conn.close()
def main():
 import argparse
 parser=argparse.ArgumentParser();parser.add_argument('--workers',type=int,default=2);parser.add_argument('--limit',type=int);parser.add_argument('--tag',default='full01');args=parser.parse_args()
 os.environ['PSU_R88_RUN_TAG']=args.tag
 configure('parent')
 out=R/args.tag;out.mkdir(exist_ok=False)
 jobs=[json.loads(s) for s in (R/'SELECTED_JOBS.jsonl').read_text('utf8').splitlines() if s.strip()]
 if args.limit:jobs=jobs[:args.limit]
 q=queue.Queue()
 for job in jobs:q.put(job)
 from app.pipeline.model_admission import ModelAdmissionBroker
 ctx=mp.get_context('spawn');broker=ModelAdmissionBroker(ctx,limit=1);broker.start()
 started=time.perf_counter();lock=threading.Lock();stats={'completed':0,'total':len(jobs),'grades':0,'raw_passed':0,'exceptions':0,'model_attempts':0,'model_transport_successes':0,'workers':args.workers,'format':'common','llm_enabled':True,'running':True}
 baseline=hashlib.sha256((S/'data/knowledge/common.sqlite').read_bytes()).hexdigest()
 def progress():
  elapsed=time.perf_counter()-started
  state={**stats,'elapsed_sec':round(elapsed,2),'percent':round(100*stats['completed']/len(jobs),3),'remaining_minutes_at_current_rate':round((len(jobs)-stats['completed'])*elapsed/max(1,stats['completed'])/60,2),'updated_at':datetime.now().astimezone().isoformat()}
  tmp=out/'PROGRESS.new.json';tmp.write_text(json.dumps(state,ensure_ascii=False,indent=2),encoding='utf8');os.replace(tmp,out/'PROGRESS.json')
  return state
 def loop(i):
  channel=None;p=None;conn=None
  def stop():
   nonlocal p,conn,channel
   if p:
    if p.is_alive():
     try:conn.send(None)
     except (OSError,EOFError):pass
     p.join(.5)
    if p.is_alive():p.terminate();p.join(3)
    conn.close();broker.revoke(channel[2]);p=None
  def start():
   nonlocal p,conn,channel
   channel=broker.register();conn,other=ctx.Pipe();p=ctx.Process(target=child,args=(other,i,channel),name='r88-common-on-'+str(i));p.start();other.close()
   if not conn.poll(90):raise RuntimeError('worker startup timeout')
   event=conn.recv()
   if event.get('event')!='ready':raise RuntimeError(str(event))
  with gzip.open(out/('RESULTS_'+str(i)+'.jsonl.gz'),'xt',encoding='utf8') as f:
   try:
    start()
    while True:
     try:job=q.get_nowait()
     except queue.Empty:break
     try:
      conn.send(job)
      if not conn.poll(28):raise TimeoutError('request watchdog 28 seconds')
      event=conn.recv();row=event['row']
     except Exception as e:
      row={'key':job['key'],'question':job['question'],'requested_locale':job['locale'],'stratum':job['r70_stratum'],'exception':repr(e),'grades':[],'worker_transport_failure':True};stop();start()
     if row.get('exception') and not row.get('grades'):
      row['grades']=[{'file':e['file'],'row':e['row'],'variant':e['variant'],'id':e['case'].get('id'),'passed':False,'failures':['pipeline_exception'],'partitions':partitions(['pipeline_exception']),'positive_text_contract':False,'evidence_level':'execution_failure'} for e in job['entries']]
     f.write(json.dumps(row,ensure_ascii=False)+'\n');f.flush()
     with lock:
      stats['completed']+=1;stats['grades']+=len(row.get('grades',[]));stats['raw_passed']+=sum(g['passed'] for g in row.get('grades',[]));stats['exceptions']+=int(bool(row.get('exception')))
      stats['model_attempts']+=len(row.get('observed_model_http_calls',[]));stats['model_transport_successes']+=sum(x['transport_ok'] for x in row.get('observed_model_http_calls',[]))
      if stats['completed']%25==0:print(json.dumps(progress()),flush=True)
   except BaseException as e:
    with (out/('WORKER_'+str(i)+'_ERROR.txt')).open('x',encoding='utf8') as f:f.write(traceback.format_exc())
   finally:stop()
 with lock:progress()
 threads=[threading.Thread(target=loop,args=(i,)) for i in range(args.workers)]
 try:
  for t in threads:t.start()
  for t in threads:t.join()
 finally:broker.stop()
 with lock:
  stats['running']=False;stats['coverage_complete']=stats['completed']==len(jobs);stats['test_database_unchanged']=baseline==hashlib.sha256((S/'data/knowledge/common.sqlite').read_bytes()).hexdigest();state=progress()
 (out/'RUN_FINISHED.json').write_text(json.dumps(state,ensure_ascii=False,indent=2),encoding='utf8')
 print(json.dumps(state,ensure_ascii=False),flush=True)
 return 0 if stats['coverage_complete'] else 1
if __name__=='__main__':raise SystemExit(main())
