import os,sys,subprocess,json,time,uuid
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r42_current_path.txt').read_text(encoding='utf-8'))
port=sys.argv[1];minor=sys.argv[2] if len(sys.argv)>2 else '2';env=dict(os.environ,PYTHONIOENCODING='utf-8',PYTHONDONTWRITEBYTECODE='1')
jobs=[
    ('main',f'import r42_probe as p; p.probe.run({port!r},"final_r42_2_main_after_restart")'),
    ('variations',f'import r42_variations as p; p.probe.run({port!r},"final_r42_2_variations")'),
    ('r41_main',f'import r41_probe as p; from pathlib import Path; p.OUT=Path({str(OUT)!r}); p.run({port!r},"final_r42_2_r41_main")'),
    ('r41_variations',f'import r41_variations as p; from pathlib import Path; p.probe.OUT=Path({str(OUT)!r}); p.probe.run({port!r},"final_r42_2_r41_variations")'),
    ('adjacent',f'import r40_targeted_probe as p; import runpy,sys; from pathlib import Path; p.OUT=Path({str(OUT)!r}); sys.argv=["r40_adjacent_http.py",{port!r}]; runpy.run_path("r40_adjacent_http.py",run_name="__main__")'),
    ('policy',f'import r42_policy_http as p; p.probe.run({port!r},"final_r42_2_policy")'),
    ('identity',f'import runpy,sys; sys.argv=["r42_http_identity.py",{port!r},{minor!r}]; runpy.run_path("r42_http_identity.py",run_name="__main__")')]
for name,code in jobs:
    code=code.replace('final_r42_2_',f'final_r42_{minor}_')
    existing=set(OUT.glob('*_summary.json'))
    result=subprocess.run([sys.executable,'-B','-c',code],cwd=BASE,env=env,text=True,encoding='utf-8',capture_output=True,timeout=300)
    filename=OUT/(name+'_http_runner_'+uuid.uuid4().hex[:6]+'.txt')
    with filename.open('x',encoding='utf-8') as f:f.write(result.stdout+result.stderr)
    print(name,'exit',result.returncode,result.stdout[-1300:],result.stderr[-300:],flush=True)
    if result.returncode:sys.exit(result.returncode)
    for summary in set(OUT.glob('*_summary.json'))-existing:
        data=json.loads(summary.read_text(encoding='utf-8'))
        if data['passed']!=data['executed_cases']:
            print('Stop on failed gate:',summary.name,flush=True);sys.exit(1)
