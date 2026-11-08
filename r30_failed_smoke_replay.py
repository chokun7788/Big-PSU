import sys,json,os,time,subprocess,concurrent.futures
from pathlib import Path
root=Path(__file__).parent;p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');r=Path((root/'r30_report_path.txt').read_text().strip());run=sys.argv[1]
baseline=p/'owner_local_delivery_20261002_input_context_r29_verified/PSU_Esports_Chatbot_Local'
paths=[v['file'] for v in json.loads((r/'sweep_A_smoke_all.json').read_text()) if v['status']!='passed']
out=r/(run+'_failed_smoke_replay');out.mkdir(exist_ok=False)
env=dict(os.environ,PSU_BILINGUAL_EN_ENABLED='1',PSU_SEMANTIC_RETRIEVAL='0',PYTHONDONTWRITEBYTECODE='1',PYTHONPATH=os.pathsep.join([str(p),str(root/'work/r30_test_dependencies')]))
def test(path,version):
    loadroot=baseline if version=='r29_baseline' else p
    code='import sys,runpy;loadroot,path=sys.argv[1:3];sys.path.insert(0,loadroot);sys.argv=[path];runpy.run_path(path,run_name="__main__")'
    start=time.perf_counter();logpath=out/(version+'_'+Path(path).stem+'.log')
    with logpath.open('x',encoding='utf-8') as log:
        try:
            result=subprocess.run([sys.executable,'-u','-X','utf8','-c',code,str(loadroot),str(p/path)],cwd=p,env=env,stdout=log,stderr=subprocess.STDOUT,timeout=100)
            status='passed' if result.returncode==0 else 'failed';exit_code=result.returncode
        except subprocess.TimeoutExpired:status='timeout';exit_code=None
    return {'file':path,'version':version,'status':status,'exit_code':exit_code,'elapsed':time.perf_counter()-start,'log':str(logpath)}
rows=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
    for f in concurrent.futures.as_completed([pool.submit(test,path,version) for path in paths for version in ['r29_baseline','r30_candidate']]):
        row=f.result();rows.append(row);print(json.dumps({k:v for k,v in row.items() if k!='log'}),flush=True)
with (r/(run+'_smoke_replay.json')).open('x',encoding='utf-8') as f:json.dump(rows,f,ensure_ascii=False,indent=2)
