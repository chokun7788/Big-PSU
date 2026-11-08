"""Resume missing pairs only after a Windows status-file replacement failure.

The frozen answer implementation, cases and grader stay unchanged. Progress
replacement is retried and cannot discard an already persisted answer.
"""
import collections,hashlib,json,os,time,traceback,urllib.request
from datetime import datetime
from pathlib import Path
from benchmark import grade
from flow_engine import Engine
R=Path(__file__).resolve().parent;OUT=R/'main_natural'
def read(p):return json.loads(p.read_text('utf8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def atomic(name,value):
 p=OUT/name;tmp=p.with_suffix(p.suffix+'.resume.tmp');raw=json.dumps(value,ensure_ascii=False,indent=2)
 for attempt in range(8):
  try:tmp.write_text(raw,'utf8');os.replace(tmp,p);return
  except PermissionError:
   if attempt==7:
    alternate=OUT/(p.stem+'_IO_RETRY_'+str(time.time_ns())+'.json');alternate.write_text(raw,'utf8')
    with (OUT/'STATUS_IO_WARNINGS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps({'target':name,'alternate':alternate.name,'reason':'Windows PermissionError while updating control file'})+'\n')
    return
   time.sleep(min(.05*2**attempt,1))
def main():
 frozen=read(OUT/'RUN_FREEZE.json')
 assert all(sha(R/p)==h for p,h in frozen['files'].items()),'Frozen implementation/cases changed'
 configs=read(R/'SELECTED_42.json');jobs=[json.loads(x) for x in (R/'EFFECTIVE_QUESTIONS_1400.jsonl').read_text('utf8').splitlines()];byjob={j['id']:j for j in jobs}
 out=OUT/'RESULTS.jsonl';eventsfile=OUT/'MODEL_EVENTS.jsonl'
 rows=[json.loads(x) for x in out.read_text('utf8').splitlines()];seen={(x['flow_id'],x['question_id']) for x in rows};assert len(rows)==len(seen)
 events=[json.loads(x) for x in eventsfile.read_text('utf8').splitlines()]
 attempted={(e['flow_id'],qid) for e in events for qid in e['question_ids']}
 assert not attempted-seen,'A model call has no persisted result; restore it from event before resuming, do not rerun it'
 addendum=read(R/'EXCLUSION_ADDENDUM.json');assert sha(R/'EFFECTIVE_QUESTIONS_1400.jsonl')==addendum['effective_workload_sha256']
 manifest=read(R/'DATA_MANIFEST.json');db=Path(manifest['source_database']);assert sha(db)==manifest['sha256']
 assert sha(R/'EFFECTIVE_QUESTIONS_1400.jsonl')==addendum['effective_workload_sha256']
 with urllib.request.urlopen('http://127.0.0.1:11434/api/tags',timeout=5) as response:tags=json.load(response)
 digest=next(x['digest'] for x in tags['models'] if x['name']==frozen['model']);assert digest==frozen['model_digest_expected']
 start=time.monotonic();prior_elapsed=read(OUT/'STATUS.json').get('elapsed_seconds',0);count=len(rows);engine=Engine();stats=collections.defaultdict(collections.Counter);timings=collections.defaultdict(list)
 def absorb(x):
  c=stats[x['flow_id']];g=x['grade'];j=byjob[x['question_id']];result=x['result']
  c['executions']+=1;c['passed']+=g['passed'];c['missing_source_cases']+=j['stratum']=='missing_source';c['gap_safe']+=j['stratum']=='missing_source' and not result['claims'];c['unavailable']+=result['status']=='unavailable';c['extra_claim_cases']+=bool(g['unrequested_claims']);c['english_translation_missing']+=result['english_translation_missing'];c['model_attempted_cases']+=bool(x['model_event_id']);timings[x['flow_id']].append(result['elapsed_sec'])
 for x in rows:absorb(x)
 atomic('RESUME_CONTROL_EXCLUSION.json',{'reason':'Control restart to enforce owner topic exclusion before C13; prior failure/recovery records retained','retained_pairs':count,'missing_pairs':4200-count,'source_implementation_unchanged':True,'resume_script_sha256':sha(Path(__file__)),'pid':os.getpid(),'started_at':datetime.now().astimezone().isoformat(),'retained_results_sha256_at_resume':sha(out)})
 def progress(flow=None,phase='running'):
  elapsed=prior_elapsed+time.monotonic()-start
  atomic('STATUS.json',{'phase':phase,'completed':count,'planned':4200,'percent':round(count/42,2),'flow':flow,'elapsed_seconds':round(elapsed,2),'eta_minutes_at_current_rate':round((4200-count)*elapsed/max(1,count)/60,2),'pid':os.getpid(),'updated_at':datetime.now().astimezone().isoformat(),'production_changed':False,'resumed_after_status_io_error':True,'counts':{k:dict(v) for k,v in stats.items()}})
 def emit(config,j,plan,elapsed,eid=None):
  nonlocal count
  result=engine.render(config['category'],j['question'],j['locale'],plan);result['elapsed_sec']=elapsed
  x={'flow_id':config['id'],'family':config['family'],'category':config['category'],'question_id':j['id'],'question':j['question'],'locale':j['locale'],'stratum':j['stratum'],'fixture':j['fixture'],'result':result,'grade':grade(j,result),'model_event_id':eid}
  key=(config['id'],j['id']);assert key not in seen
  with out.open('a',encoding='utf8') as f:f.write(json.dumps(x,ensure_ascii=False)+'\n');f.flush()
  seen.add(key);absorb(x);count+=1
  if count%10==0:progress(config['id'])
 progress()
 for config in configs:
  pending=[];missing=[j for j in jobs if j['category']==config['category'] and (config['id'],j['id']) not in seen]
  if not missing:continue
  for j in missing:
   started=time.monotonic();plan=engine.plan(config['category'],j['question'],config['family']);elapsed=time.monotonic()-started
   if config['family']=='hybrid' and plan.get('ambiguous'):pending.append((j,elapsed))
   else:emit(config,j,plan,elapsed)
  for pos in range(0,len(pending),3):
   batch=pending[pos:pos+3];progress(config['id'],'running_model_batch')
   plans,event=engine.semantic_batch(config['category'],[j['question'] for j,_ in batch]);eid=f"{config['id']}-resume-batch-{pos//3+1}";event.update(id=eid,category=config['category'],flow_id=config['id'],question_ids=[j['id'] for j,_ in batch])
   with eventsfile.open('a',encoding='utf8') as f:f.write(json.dumps(event,ensure_ascii=False)+'\n')
   for (j,elapsed),plan in zip(batch,plans):emit(config,j,plan,elapsed+event['elapsed_sec']/len(batch),eid)
  progress(config['id']);print(json.dumps({'flow':config['id'],**dict(stats[config['id']])},ensure_ascii=False),flush=True)
 assert count==4200 and len(seen)==4200 and len(stats)==42 and all(v['executions']==100 for v in stats.values())
 assert all(sha(R/p)==h for p,h in frozen['files'].items())
 assert sha(db)==manifest['sha256']
 assert sha(R/'EFFECTIVE_QUESTIONS_1400.jsonl')==addendum['effective_workload_sha256']
 with urllib.request.urlopen('http://127.0.0.1:11434/api/tags',timeout=5) as response:after=json.load(response)
 assert next(x['digest'] for x in after['models'] if x['name']==frozen['model'])==digest
 atomic('TIMINGS.json',{k:sorted(v) for k,v in timings.items()})
 atomic('TEST_COMPLETE.json',{'complete':True,'completed_executions':4200,'unique_flow_question_pairs':4200,'flows':42,'categories':14,'questions_per_flow':100,'source_unchanged':True,'implementation_unchanged_during_run':True,'model_identity_verified':True,'model_digest':digest,'effective_workload_sha256':sha(R/'EFFECTIVE_QUESTIONS_1400.jsonl'),'owner_exclusion_applied_before_category_execution':True,'evaluation_control_resumed_after_status_io_failure':True,'original_failure_retained':True,'runtime_installed_over_R78':False,'scope':'isolated experimental domain adapters; not full chatbot integration','question_set':'source-grounded natural paraphrase development set; not independent holdout','completed_at':datetime.now().astimezone().isoformat()})
 progress(phase='complete')
if __name__=='__main__':
 try:main()
 except BaseException as e:atomic('RESUME_EXCLUSION_FAILED.json',{'error':repr(e),'traceback':traceback.format_exc()});raise
