"""Run all 42 adapters on frozen equal workloads, retaining every answer."""
import ast,collections,hashlib,json,os,time,traceback,urllib.request
from datetime import datetime
from pathlib import Path
R=Path(__file__).resolve().parent
def read(name):return json.loads((R/name).read_text('utf8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def atomic(name,value):
 p=R/name;tmp=p.with_suffix(p.suffix+'.tmp');tmp.write_text(json.dumps(value,ensure_ascii=False,indent=2),'utf8');os.replace(tmp,p)
def normal(x):return ' '.join(str(x).split()).casefold()

def grade(job,result):
 expected=job['expected'];want={x['fact_id']:x for x in expected['claims']};got={x['fact_id']:x for x in result.get('claims',[])}
 missing=sorted(want.keys()-got.keys());extra=sorted(got.keys()-want.keys());wrong=[];evidence=[]
 for fid in want.keys()&got.keys():
  a=want[fid];b=got[fid]
  if a.get('numeric') is not None:
   if b.get('numeric')!=a['numeric']:wrong.append(fid+':numeric')
  elif normal(a['value'])!=normal(b['value']):wrong.append(fid+':value')
  if a['evidence_refs']!=b.get('evidence_refs'):evidence.append(fid)
 status_ok=result.get('status')==expected['status']
 matched=len(want.keys()&got.keys())-len(wrong)
 return {'passed':not missing and not extra and not wrong and not evidence and status_ok,'missing_claims':missing,'unrequested_claims':extra,'wrong_values':wrong,'evidence_mismatches':evidence,'status_ok':status_ok,'expected_status':expected['status'],'actual_status':result.get('status'),'matched_claims':matched,'expected_claims':len(want),'returned_claims':len(got),'metric':'source-claim identity/value/scope/expected-state exact check; not independent human semantic accuracy'}

def main():
 for p in R.glob('*.py'):ast.parse(p.read_text('utf8'),filename=str(p))
 workload=read('WORKLOAD_MANIFEST.json')
 assert sha(R/'QUESTIONS_1400.jsonl')==workload['question_set_sha256']
 assert sha(R/'COMMON_READ_MODEL.json')==workload['read_model_sha256']
 configs=read('SELECTED_42.json');jobs=[json.loads(s) for s in (R/'QUESTIONS_1400.jsonl').read_text('utf8').splitlines()]
 freeze_files=['flow_engine.py','benchmark.py','prepare_data.py','build_questions.py','SELECTED_42.json','DESIGNS_140.json','COMMON_READ_MODEL.json','QUESTIONS_1400.jsonl']
 freeze={n:sha(R/n) for n in freeze_files};atomic('RUN_FREEZE.json',{'files':freeze,'workload':workload,'model':'scb10x/typhoon2.5-qwen3-4b:latest','model_digest_expected':'b1f251ef835962b270ba48266d4e32e6f90b29f10930d0712ef5eaabec773a05','started_at':datetime.now().astimezone().isoformat(),'cross_flow_output_cache':False})
 with urllib.request.urlopen('http://127.0.0.1:11434/api/tags',timeout=5) as r:tags=json.load(r)
 model=next(m for m in tags['models'] if m['name']=='scb10x/typhoon2.5-qwen3-4b:latest')
 assert model['digest']=='b1f251ef835962b270ba48266d4e32e6f90b29f10930d0712ef5eaabec773a05'
 from flow_engine import Engine
 engine=Engine();out=R/'RESULTS.jsonl';events=R/'MODEL_EVENTS.jsonl'
 if out.exists():raise RuntimeError('Refusing to overwrite existing results')
 started=time.monotonic();count=0;summary=collections.defaultdict(lambda:collections.Counter());timings=collections.defaultdict(list)
 def progress(flow=None,phase='running'):
  elapsed=time.monotonic()-started
  atomic('STATUS.json',{'phase':phase,'completed':count,'planned':4200,'percent':round(count/42,2),'flow':flow,'elapsed_seconds':round(elapsed,2),'eta_minutes_at_current_rate':round((4200-count)*elapsed/max(1,count)/60,2),'updated_at':datetime.now().astimezone().isoformat(),'pid':os.getpid(),'production_changed':False,'counts':{k:dict(v) for k,v in summary.items()}})
 def emit(config,job,plan,elapsed,model_event=None):
  nonlocal count
  result=engine.render(config['category'],job['question'],job['locale'],plan);result['elapsed_sec']=elapsed
  g=grade(job,result);row={'flow_id':config['id'],'family':config['family'],'category':config['category'],'question_id':job['id'],'question':job['question'],'locale':job['locale'],'stratum':job['stratum'],'fixture':job['fixture'],'result':result,'grade':g,'model_event_id':model_event}
  with out.open('a',encoding='utf8') as f:f.write(json.dumps(row,ensure_ascii=False)+'\n');f.flush()
  c=summary[config['id']];c['executions']+=1;c['passed']+=g['passed'];c['missing_source_cases']+=job['stratum']=='missing_source';c['gap_safe']+=job['stratum']=='missing_source' and not result['claims'];c['unavailable']+=result['status']=='unavailable';c['extra_claim_cases']+=bool(g['unrequested_claims']);c['english_translation_missing']+=result['english_translation_missing'];c['model_attempted_cases']+=bool(model_event)
  timings[config['id']].append(elapsed);count+=1
  if count%10==0:progress(config['id'])
 progress()
 for config in configs:
  selected=[j for j in jobs if j['category']==config['category']];pending=[]
  for job in selected:
   start=time.monotonic();plan=engine.plan(config['category'],job['question'],config['family']);elapsed=time.monotonic()-start
   if config['family']=='hybrid' and plan.get('ambiguous'):pending.append((job,plan,elapsed))
   else:emit(config,job,plan,elapsed)
  for pos in range(0,len(pending),3):
   batch=pending[pos:pos+3];progress(config['id'],'running_model_batch')
   plans,event=engine.semantic_batch(config['category'],[j['question'] for j,_,_ in batch]);eid=f"{config['id']}-batch-{pos//3+1}";event.update(id=eid,category=config['category'],flow_id=config['id'],question_ids=[j['id'] for j,_,_ in batch])
   with events.open('a',encoding='utf8') as f:f.write(json.dumps(event,ensure_ascii=False)+'\n')
   for (job,prior,el),plan in zip(batch,plans):emit(config,job,plan,el+event['elapsed_sec']/len(batch),eid)
  progress(config['id']);print(json.dumps({'flow':config['id'],**dict(summary[config['id']])},ensure_ascii=False),flush=True)
 assert count==4200 and all(v['executions']==100 for v in summary.values()) and len(summary)==42
 changed=[p for p,h in freeze.items() if sha(R/p)!=h];assert not changed,changed
 db=Path(read('DATA_MANIFEST.json')['source_database']);assert sha(db)==read('DATA_MANIFEST.json')['sha256']
 with urllib.request.urlopen('http://127.0.0.1:11434/api/tags',timeout=5) as r:after=json.load(r)
 assert next(m['digest'] for m in after['models'] if m['name']==model['name'])==model['digest']
 atomic('TIMINGS.json',{k:sorted(v) for k,v in timings.items()})
 atomic('TEST_COMPLETE.json',{'complete':True,'completed_executions':count,'unique_flow_question_pairs':count,'flows':42,'categories':14,'questions_per_flow':100,'source_unchanged':True,'implementation_unchanged_during_run':True,'model_identity_verified':True,'model_digest':model['digest'],'runtime_installed_over_R78':False,'scope':'isolated experimental domain adapters; not full chatbot integration','question_set':'source-derived templated development set, not independent holdout','completed_at':datetime.now().astimezone().isoformat()})
 progress(phase='complete')

if __name__=='__main__':
 try:main()
 except BaseException as exc:
  atomic('FAILED.json',{'error':repr(exc),'traceback':traceback.format_exc(),'pid':os.getpid(),'production_changed':False});raise
