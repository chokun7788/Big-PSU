"""Prepare posthoc development checks, never report them as a fresh test."""
import ast,json
from pathlib import Path
R=Path(__file__).resolve().parent
rows=lambda p:list(map(json.loads,p.open(encoding='utf8')))
alljobs={j['key']:j for j in rows(R/'ALL_RETAINED_JOBS.jsonl')}
jobs=rows(R/'API_SELECTED_JOBS.jsonl');known={j['key'] for j in jobs};reg=[]
for focus in ['equipment_definition','price','opening_hours','game_controls','booking_procedure','food_consume']:
 x=next(x for x in rows(R/'train.jsonl') if x['key'] not in known and x['label']['focus']==focus and x['key'] in alljobs)
 known.add(x['key']);jobs.append(alljobs[x['key']]);reg.append({'key':x['key'],'focus':focus,'question':x['question']})
assert len(jobs)==14
(R/'GUARD_SELECTED_JOBS.jsonl').write_text(''.join(json.dumps(j,ensure_ascii=False)+'\n' for j in jobs),'utf8')
(R/'GUARD_SELECTION.json').write_text(json.dumps({'development_only':True,'fresh_heldout':False,'previous_api_questions':8,'known_training_regression_questions':reg,'new_questions':0,'same_adapter_as_original_experiment':True},ensure_ascii=False,indent=2),'utf8')
x=(R/'serve_frozen.py').read_text('utf8');assert "str(R/'system')" in x
(R/'serve_guard.py').write_text(x.replace("str(R/'system')","str(R/'revision02_system')"),'utf8')
x=(R/'run_api_comparison02.py').read_text('utf8').replace("S=R/'system';OUT=R/'api02'","S=R/'revision02_system';OUT=R/'guard01'")
x=x.replace('API_SELECTED_JOBS.jsonl','GUARD_SELECTED_JOBS.jsonl').replace('serve_frozen.py','serve_guard.py')
x=x.replace("for profile in ['psu-r121-base:latest','psu-r121-trained:latest']", "for profile in ['psu-r121-trained:latest']")
x=x.replace('==8','==14').replace('==16','==14').replace("'requests_per_arm':8,'total_requests':16", "'requests_per_arm':14,'total_requests':14,'development_only':True,'fresh_heldout':False")
x=x.replace("PSU_RUNTIME_PROFILE='r121-context-lora',PSU_RUNTIME_VERSION='R121-context-lora'", "PSU_RUNTIME_PROFILE='r121-context-guard-r02',PSU_RUNTIME_VERSION='R121-context-guard-r02'")
ast.parse(x);(R/'run_guard_probe.py').write_text(x,'utf8')
x=(R/'resume_api.py').read_text('utf8').replace("OUT=R/'execution03'","OUT=R/'execution04'")
x=x.replace("'inference02'","'inference03'").replace('run_api_comparison02.py','run_guard_probe.py').replace("R/'api02/TEST_COMPLETE.json'","R/'guard01/TEST_COMPLETE.json'").replace('requests_per_arm=8','requests_per_arm=14').replace("'API02 failed'","'Development guard check failed'")
ast.parse(x);(R/'run_guard_execution.py').write_text(x,'utf8')
print(json.dumps({'prepared':True,'development_questions':14,'new_questions':0,'regression':reg},ensure_ascii=False,indent=2))
