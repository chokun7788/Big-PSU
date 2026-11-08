import os,sys,subprocess,json,uuid
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r43_current_path.txt').read_text())
port=sys.argv[1];env=dict(os.environ,PYTHONIOENCODING='utf-8',PYTHONDONTWRITEBYTECODE='1')
jobs=[
 ('schedule',f'import r43_schedule_http as p;p.probe.run({port!r},"final_r43_3_schedule")'),
 ('domain_resume',f'import r42_probe as p;from pathlib import Path;p.probe.OUT=Path({str(OUT)!r});p.probe.run({port!r},"final_r43_3_domain_resume")'),
 ('task_memory',f'import r41_probe as p;from pathlib import Path;p.OUT=Path({str(OUT)!r});p.run({port!r},"final_r43_3_task_memory")'),
 ('policy',f'import r42_policy_http as p;from pathlib import Path;p.probe.OUT=Path({str(OUT)!r});p.probe.run({port!r},"final_r43_3_policy")')]
for name,code in jobs:
 existing=set(OUT.glob('*_summary.json'));r=subprocess.run([sys.executable,'-B','-c',code],cwd=BASE,env=env,text=True,encoding='utf-8',capture_output=True,timeout=300)
 with (OUT/(name+'_http_runner_'+uuid.uuid4().hex[:6]+'.txt')).open('x',encoding='utf-8') as f:f.write(r.stdout+r.stderr)
 print(name,r.returncode,r.stdout[-1700:],r.stderr[-400:],flush=True)
 if r.returncode:sys.exit(r.returncode)
 for path in set(OUT.glob('*_summary.json'))-existing:
  data=json.loads(path.read_text())
  if data['health']['runtime']['version']!='2026.10.06-readiness-schedule-r43.3':raise AssertionError('wrong runtime')
  if data['passed']!=data['executed_cases']:print('STOP FAILED',path.name,flush=True);sys.exit(1)
