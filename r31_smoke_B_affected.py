import json,sys,os,time,subprocess,concurrent.futures
from pathlib import Path
p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');root=Path(__file__).parent;r=Path((root/'r31_report_path.txt').read_text().strip());out=r/'final_B_competition_smokes';out.mkdir(exist_ok=False)
files=[f for f in sorted((p/'tests').glob('smoke_test*.py')) if 'competition' in f.read_text(encoding='utf-8')]
env=dict(os.environ,PSU_BILINGUAL_EN_ENABLED='1',PSU_SEMANTIC_RETRIEVAL='0',PYTHONDONTWRITEBYTECODE='1',PYTHONPATH=os.pathsep.join([str(p),str(root/'work/r30_test_dependencies')]))
def test(path):
    started=time.perf_counter()
    with (out/(path.stem+'.log')).open('x',encoding='utf-8') as log:
        try:z=subprocess.run([sys.executable,'-u','-X','utf8',str(path)],cwd=p,env=env,stdout=log,stderr=subprocess.STDOUT,timeout=100);status='passed' if z.returncode==0 else 'failed';code=z.returncode
        except subprocess.TimeoutExpired:status='timeout';code=None
    return dict(file=str(path.relative_to(p)),status=status,exit_code=code,elapsed_sec=time.perf_counter()-started,log=str(out/(path.stem+'.log')))
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:rows=list(pool.map(test,files))
previous={x['file']:x for x in json.loads((r/'complete_A_smoke_all.json').read_text())}
with (r/'final_B_competition_smoke_summary.json').open('x',encoding='utf-8') as out:json.dump(dict(total=len(rows),passed=sum(x['status']=='passed' for x in rows),rows=rows,new_failures=[x for x in rows if x['status']!='passed' and previous[x['file']]['status']=='passed'],scope='Affected competition smoke files only; full 85-file sweep retained separately. API not run concurrently.'),out,ensure_ascii=False,indent=2)
print(json.dumps(dict(total=len(rows),passed=sum(x['status']=='passed' for x in rows),new_failures=[x['file'] for x in rows if x['status']!='passed' and previous[x['file']]['status']=='passed'])),flush=True)
