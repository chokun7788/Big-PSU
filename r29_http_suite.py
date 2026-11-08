import json,sys,os,subprocess,urllib.request,time
from pathlib import Path
root=Path(__file__).parent;project=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
report=Path((root/'r29_report_path.txt').read_text(encoding='utf-8').strip());old=Path((root/'r28_report_path.txt').read_text(encoding='utf-8').strip())
base='http://127.0.0.1:'+sys.argv[1]
health=json.load(urllib.request.urlopen(base+'/health',timeout=5));assert health['runtime']['version']=='2026.10.02-input-context-r29-verified'
with (report/'http_health_before_B.json').open('x',encoding='utf-8') as f:json.dump(health,f,ensure_ascii=False,indent=2)
tasks=[('noise36',[str(root/'r29_http_noise_check.py'),sys.argv[1],'http_noise36_B']),
 ('composition280',[str(project/'tools/run_competition_composition_r28.py'),'--fixture',str(old/'composition_fixture_v3.json'),'--report',str(report),'--run','http_composition280','--url',base,'--llm']),
 ('contract320',[str(project/'tools/run_competition_contract_r27.py'),'--fixture',str(old/'content_contract_fixture_v2.json'),'--report',str(report),'--run','http_contract320','--url',base,'--llm']),
 ('resolution12',[str(project/'tools/run_competition_composition_r28.py'),'--fixture',str(old/'http_resolution_12_fixture.json'),'--report',str(report),'--run','http_resolution12','--url',base,'--llm']),
 ('old36',[str(root/'r29_final_web_check.py'),sys.argv[1],'old36'])]
for name,args in tasks:
    with (report/('http_'+name+'_B_runner.log')).open('x',encoding='utf-8') as f:
        result=subprocess.run([sys.executable,'-u','-X','utf8',*args],cwd=root,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),stdout=f,stderr=subprocess.STDOUT)
    print(json.dumps({'suite':name,'exit_code':result.returncode}),flush=True)
    if result.returncode:raise SystemExit(result.returncode)
health=json.load(urllib.request.urlopen(base+'/health',timeout=5))
with (report/'http_health_after.json').open('x',encoding='utf-8') as f:json.dump(health,f,ensure_ascii=False,indent=2)
print('Actual sequential HTTP suite completed.',flush=True)
