import collections,concurrent.futures,json,os,subprocess,sys,time,unittest,shutil
from pathlib import Path
import harness
B=Path(__file__).resolve().parent;stage=B/'system'
def unit(mode,pattern):
 tag=sys.argv[3] if len(sys.argv)>3 else 'initial'
 harness.test_temp(mode+'_'+tag)
 db=B/(mode+'_unit_'+pattern.replace('*','all')+'_'+tag+'.sqlite');shutil.copy2(B/(mode+'.sqlite'),db)
 harness.configure(mode,False,db)
 if str(stage) not in sys.path:sys.path.insert(0,str(stage))
 suite=unittest.defaultTestLoader.discover(str(stage/'tests'),pattern=pattern,top_level_dir=str(stage));start=time.perf_counter()
 log=B/(mode+'_'+pattern.replace('*','all')+'_'+tag+'.log')
 with log.open('x',encoding='utf-8') as f:r=unittest.TextTestRunner(stream=f,verbosity=2).run(suite)
 result={'mode':mode,'pattern':pattern,'tests':r.testsRun,'elapsed':time.perf_counter()-start,'failures':[(str(t),e) for t,e in r.failures],'errors':[(str(t),e) for t,e in r.errors],'skipped':[(str(t),e) for t,e in r.skipped],'success':r.wasSuccessful()}
 (B/(mode+'_'+pattern.replace('*','all')+'_'+tag+'.json')).write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in result.items() if k not in {'failures','errors','skipped'}},ensure_ascii=False),flush=True)
def smoke(mode):
 harness.test_temp(mode+'_smoke')
 harness.configure(mode,False);out=B/(mode+'_smokes');out.mkdir(exist_ok=False)
 env=os.environ.copy();env['PYTHONPATH']=os.pathsep.join([str(stage),str(B)])
 files=sorted((stage/'tests').glob('smoke_test*.py'));results=[]
 def run(p):
  start=time.perf_counter()
  if p.name=='smoke_test_bilingual_web_api.py':return {'file':p.name,'status':'deferred_actual_http_suite','reason':'Will run against isolated evaluation web servers, not user server'}
  with (out/(p.stem+'.log')).open('x',encoding='utf-8') as f:
   try:
    cp=subprocess.run([sys.executable,'-B','-X','utf8',str(B/'smoke_wrapper.py'),mode,str(p)],cwd=stage,env=env,stdout=f,stderr=subprocess.STDOUT,timeout=160)
    return {'file':p.name,'status':'passed' if cp.returncode==0 else 'failed','exit_code':cp.returncode,'elapsed':time.perf_counter()-start}
   except subprocess.TimeoutExpired:return {'file':p.name,'status':'timeout','elapsed':time.perf_counter()-start}
 with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
  for n,r in enumerate(pool.map(run,files),1):
   results.append(r)
   if n%10==0:print(json.dumps({'completed':n,'mode':mode}),flush=True)
 (out/'SUMMARY.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps({'mode':mode,'smokes':collections.Counter(r['status'] for r in results)},ensure_ascii=False),flush=True)
if __name__=='__main__':
 if sys.argv[2]=='smoke':smoke(sys.argv[1])
 else:unit(sys.argv[1],sys.argv[2])
