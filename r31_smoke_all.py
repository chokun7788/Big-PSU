import sys,json,os,time,subprocess,concurrent.futures
from pathlib import Path
p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');root=Path(__file__).parent;report=Path((root/'r31_report_path.txt').read_text().strip());run=sys.argv[1]
out=report/(run+'_smokes');out.mkdir(exist_ok=False)
env=dict(os.environ,PSU_BILINGUAL_EN_ENABLED='1',PSU_SEMANTIC_RETRIEVAL='0',PYTHONDONTWRITEBYTECODE='1',PYTHONPATH=os.pathsep.join([str(p),str(root/'work/r30_test_dependencies')]))
def test(f):
    args=[sys.executable,'-u','-X','utf8',str(f)]
    if f.name=='smoke_test_bilingual_web_api.py':args+=['--url',sys.argv[2] if len(sys.argv)>2 else 'http://127.0.0.1:8090']
    start=time.perf_counter()
    with (out/(f.stem+'.log')).open('x',encoding='utf-8') as log:
        try:
            result=subprocess.run(args,cwd=p,env=env,stdout=log,stderr=subprocess.STDOUT,timeout=100)
            code=result.returncode;status='passed' if code==0 else 'failed'
        except subprocess.TimeoutExpired:code=None;status='timeout'
    return {'file':str(f.relative_to(p)),'status':status,'exit_code':code,'elapsed_sec':round(time.perf_counter()-start,3),'log':str(out/(f.stem+'.log'))}
rows=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    for future in concurrent.futures.as_completed([pool.submit(test,f) for f in sorted((p/'tests').glob('smoke_test*.py'))]):
        r=future.result();rows.append(r)
        if r['status']!='passed' or len(rows)%10==0:print(json.dumps({'completed':len(rows),**r},ensure_ascii=False),flush=True)
with (report/(run+'_smoke_all.json')).open('x',encoding='utf-8') as f:json.dump(rows,f,ensure_ascii=False,indent=2)
print(json.dumps({'total':len(rows),'passed':sum(r['status']=='passed' for r in rows),'failed':[r['file'] for r in rows if r['status']!='passed']}),flush=True)
