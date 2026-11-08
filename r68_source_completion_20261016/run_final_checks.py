import json,os,subprocess,sys
from pathlib import Path
B=Path(__file__).resolve().parent
env={**os.environ,'PYTHONUTF8':'1','PYTHONDONTWRITEBYTECODE':'1'}
jobs=[['test_completion.py','1','final_on','candidate05.sqlite'],['test_preserved_behavior.py','0','preserved_final_off','candidate05.sqlite'],['test_preserved_behavior.py','1','preserved_final_on','candidate05.sqlite'],['test_owner_compatibility.py','final'],['test_followups.py'],['verify_completion.py','candidate05.sqlite','final'],['audit_sources.py','candidate05.sqlite','final']]
results=[]
for args in jobs:
 log=B/('RUN_'+args[0].removesuffix('.py')+'_'+(args[2] if len(args)>2 else 'final')+'.log')
 with log.open('x',encoding='utf8') as f:r=subprocess.run([sys.executable,'-B',str(B/args[0]),*args[1:]],stdout=f,stderr=subprocess.STDOUT,env=env)
 results.append({'args':args,'exit_code':r.returncode,'log':str(log)})
 print(json.dumps(results[-1]),flush=True)
 if r.returncode:break
(B/'FINAL_CHECK_COMMANDS.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf8')
raise SystemExit(any(r['exit_code'] for r in results))
