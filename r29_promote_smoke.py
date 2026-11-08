import json,sys,os,subprocess,time,urllib.request
from pathlib import Path
root=Path(__file__).parent;report=Path((root/'r29_report_path.txt').read_text(encoding='utf-8').strip())
for attempt in range(40):
    try:
        health=json.load(urllib.request.urlopen('http://127.0.0.1:8090/health',timeout=2));break
    except OSError:
        if attempt==39:raise
        time.sleep(.5)
assert health['runtime']['version']=='2026.10.02-input-context-r29-verified'
for name,args in [('ready_noise36',[str(root/'r29_http_noise_check.py'),'8090','http_ready_noise36']),('ready_old36',[str(root/'r29_final_web_check.py'),'8090','ready_old36'])]:
    with (report/(name+'_runner.log')).open('x',encoding='utf-8') as f:
        result=subprocess.run([sys.executable,'-u','-X','utf8',*args],cwd=root,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),stdout=f,stderr=subprocess.STDOUT)
    print(json.dumps({'suite':name,'exit_code':result.returncode}),flush=True)
    if result.returncode:raise SystemExit(result.returncode)
health=json.load(urllib.request.urlopen('http://127.0.0.1:8090/health',timeout=5))
with (report/'ready_health.json').open('x',encoding='utf-8') as f:json.dump(health,f,ensure_ascii=False,indent=2)
print('Ready web r29 passed 72 actual HTTP checks.',flush=True)
