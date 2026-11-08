import json, os, subprocess, sys, urllib.request
from pathlib import Path

base=Path(__file__).parent
project=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
report=Path((base/'r27_report_path.txt').read_text(encoding='utf-8').strip())
port=sys.argv[1]
env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
tasks=[
 ('320',[str(project/'tools/run_competition_contract_r27.py'),'--fixture',str(report/'content_contract_fixture_v2.json'),'--report',str(report),'--run','http_verified_320','--url','http://127.0.0.1:'+port,'--llm']),
 ('128',[str(base/'r27_new_questions.py'),'http_verified_128',port]),
 ('regression',[str(base/'r27_verified_web_check.py'),port,'verified_regression']),
 ('old80',[str(base/'r27_r26_content_check.py'),'http_verified_old80',port]),
 ('speed',[str(base/'r27_clarification_speed.py'),port,'verified_r27']),
]
before=json.load(urllib.request.urlopen('http://127.0.0.1:'+port+'/health',timeout=3))
with (report/'verified_http_health_before.json').open('x',encoding='utf-8') as f:json.dump(before,f,ensure_ascii=False,indent=2)
for label,args in tasks:
    with (report/('verified_http_'+label+'_runner.log')).open('x',encoding='utf-8') as f:
        result=subprocess.run([sys.executable,'-u','-X','utf8','-W','ignore',*args],cwd=base,env=env,stdout=f,stderr=subprocess.STDOUT)
    print(json.dumps({'completed':label,'exit_code':result.returncode}),flush=True)
    if result.returncode:raise SystemExit(result.returncode)
after=json.load(urllib.request.urlopen('http://127.0.0.1:'+port+'/health',timeout=3))
with (report/'verified_http_health_after.json').open('x',encoding='utf-8') as f:json.dump(after,f,ensure_ascii=False,indent=2)
