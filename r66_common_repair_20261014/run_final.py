"""Serialized final common-only gates, append-only outputs, frozen code manifest."""
import sys,os,json,hashlib,subprocess,time,urllib.request,sqlite3
from pathlib import Path
B=Path(__file__).resolve().parent;S=B/'system'
tag=sys.argv[1] if len(sys.argv)>1 else 'final04'
out=B/('FINAL_'+tag);out.mkdir(exist_ok=False)
env=os.environ.copy();env.update(PYTHONPATH=str(S),PSU_ESPORTS_NOW='2026-10-14T12:00:00+07:00')
manifest=[{'path':p.relative_to(S).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in (S/'app').rglob('*') if p.is_file() and p.suffix in {'.py','.json','.js'} and '__pycache__' not in p.parts]
(out/'CODE_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
def db_snapshot(name):
 p=out/name
 with sqlite3.connect((B/'common.sqlite').as_uri()+'?mode=ro',uri=True) as src,sqlite3.connect(p) as dst:src.backup(dst)
 return hashlib.sha256(p.read_bytes()).hexdigest()
db_before=db_snapshot('common_start.sqlite')
stages=[]
def status(stage,**extra):
 data={'stage':stage,'completed_stages':stages,'format':'common','legacy_arm_run':False,'clock':'2026-10-14T12:00:00+07:00',**extra};(out/'STATUS.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(data,ensure_ascii=False),flush=True)
def run(stage,args,timeout=1200):
 status(stage,running=True);start=time.perf_counter()
 with (out/(stage+'.log')).open('x',encoding='utf-8') as f:r=subprocess.run([sys.executable,'-B',*map(str,args)],cwd=S,env=env,stdout=f,stderr=subprocess.STDOUT,timeout=timeout)
 item={'stage':stage,'exit_code':r.returncode,'elapsed':time.perf_counter()-start};stages.append(item)
 if r.returncode:raise RuntimeError('Stage failed: '+str(item))
try:
 run('focused',[B/'test_r66_reader.py'])
 run('faq_projection',[B/'test_faq_projection.py'])
 run('billing_recovery',[B/'test_billing_recovery.py'])
 run('versioned_contracts',[B/'test_versioned_contracts.py'])
 run('person_off',[B/'test_person_source_bound.py',tag+'_off','0'])
 run('discovered_off',[B/'test_discovered_cases.py','0'])
 run('residual_off',[B/'test_residual_reader.py','0'])
 run('audience_policy_off',[B/'test_audience_policy.py','0'])
 run('validation_regressions_off',[B/'test_validation_regressions.py','0'])
 run('intent_priority_off',[B/'test_intent_priority.py','0'])
 run('translation_completeness_off',[B/'test_translation_completeness.py','0'])
 run('selector_latency_off',[B/'test_selector_latency.py','0'])
 run('return_policy_off',[B/'test_return_policy.py','0'])
 run('owner_preview_off',[B/'test_owner_preview_state.py','0'])
 run('price_comparison_off',[B/'test_price_comparison.py','0'])
 run('scoped_topics_off',[B/'test_scoped_topics.py','0'])
 run('support_off',[B/'run_support_gates.py',tag+'_off','0'])
 run('new_categories_off',[B/'test_new_all_categories.py',tag+'_off'])
 run('common_native',[B/'run_common_units.py'])
 run('matrix_off',[B/'run_matrix.py',tag+'_off','0'])
 run('http_off',[B/'run_http.py',tag+'_off','0'])
 run('http_slow_off',[B/'run_http.py',tag+'_off_slow','0'])
 # Warm up outside measured requests and preserve actual transport evidence.
 status('model_warmup',running=True)
 request=urllib.request.Request('http://127.0.0.1:11434/api/generate',data=json.dumps({'model':'scb10x/typhoon2.5-qwen3-4b','stream':False,'think':False,'keep_alive':'30m','format':'json','prompt':'Return an empty JSON object.','options':{'temperature':0,'num_ctx':3072,'num_predict':8}}).encode(),headers={'Content-Type':'application/json'})
 with urllib.request.urlopen(request,timeout=90) as response:warm=json.loads(response.read(30000))
 (out/'MODEL_WARMUP.json').write_text(json.dumps({'transport_ok':True,'model':warm.get('model'),'done':warm.get('done'),'total_duration':warm.get('total_duration'),'load_duration':warm.get('load_duration'),'eval_count':warm.get('eval_count')},indent=2),encoding='utf-8')
 run('matrix_llm',[B/'run_matrix.py',tag+'_llm','1'])
 run('http_llm',[B/'run_http.py',tag+'_llm','1'])
 run('http_slow_llm',[B/'run_http.py',tag+'_llm_slow','1'])
 run('discovered_llm',[B/'test_discovered_cases.py','1'])
 run('residual_llm',[B/'test_residual_reader.py','1'])
 run('audience_policy_llm',[B/'test_audience_policy.py','1'])
 run('validation_regressions_llm',[B/'test_validation_regressions.py','1'])
 run('intent_priority_llm',[B/'test_intent_priority.py','1'])
 run('translation_completeness_llm',[B/'test_translation_completeness.py','1'])
 run('selector_latency_llm',[B/'test_selector_latency.py','1'])
 run('return_policy_llm',[B/'test_return_policy.py','1'])
 run('owner_preview_llm',[B/'test_owner_preview_state.py','1'])
 run('price_comparison_llm',[B/'test_price_comparison.py','1'])
 run('scoped_topics_llm',[B/'test_scoped_topics.py','1'])
 run('support_llm',[B/'run_support_gates.py',tag+'_llm','1'])
 run('person_llm',[B/'test_person_source_bound.py',tag+'_llm','1'])
 run('new_categories_llm',[B/'test_new_all_categories.py',tag+'_llm','1'])
 changed=[x['path'] for x in manifest if hashlib.sha256((S/x['path']).read_bytes()).hexdigest()!=x['sha256']]
 if changed:raise RuntimeError('Code changed during final gates: '+str(changed))
 db_after=db_snapshot('common_end.sqlite')
 if db_before!=db_after:raise RuntimeError('Candidate database changed during gates')
 status('complete',running=False,complete=True,code_unchanged=True,database_unchanged=True,database_sha256=db_after)
except Exception as e:
 status('interrupted_or_failed',running=False,complete=False,error=repr(e));raise
