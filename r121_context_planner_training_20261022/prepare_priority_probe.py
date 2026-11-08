import ast,json
from pathlib import Path
R=Path(__file__).resolve().parent
jobs=list(map(json.loads,(R/'GUARD_SELECTED_JOBS.jsonl').open(encoding='utf8')))
indices=[2,7,8,11];selected=[jobs[i] for i in indices]
(R/'PRIORITY_SELECTED_JOBS.jsonl').write_text(''.join(json.dumps(j,ensure_ascii=False)+'\n' for j in selected),'utf8')
(R/'PRIORITY_SELECTION.json').write_text(json.dumps({'development_only':True,'fresh_heldout':False,'requests':4,'indices_from_guard01':indices,'new_questions':0,'reason':'Check the affected compound, identification, equipment definition, and game-control paths only'},indent=2),'utf8')
x=(R/'serve_guard.py').read_text('utf8').replace("str(R/'revision02_system')","str(R/'revision03_system')");(R/'serve_priority.py').write_text(x,'utf8')
x=(R/'run_guard_probe.py').read_text('utf8').replace("S=R/'revision02_system';OUT=R/'guard01'","S=R/'revision03_system';OUT=R/'priority01'")
x=x.replace('GUARD_SELECTED_JOBS.jsonl','PRIORITY_SELECTED_JOBS.jsonl').replace('serve_guard.py','serve_priority.py').replace('==14','==4').replace("'requests_per_arm':14,'total_requests':14", "'requests_per_arm':4,'total_requests':4").replace('r121-context-guard-r02','r121-context-guard-r03').replace('R121-context-guard-r02','R121-context-guard-r03')
ast.parse(x);(R/'run_priority_probe.py').write_text(x,'utf8')
x=(R/'run_guard_execution.py').read_text('utf8').replace("OUT=R/'execution04'","OUT=R/'execution05'").replace("'inference03'","'inference04'").replace('run_guard_probe.py','run_priority_probe.py').replace("R/'guard01/TEST_COMPLETE.json'","R/'priority01/TEST_COMPLETE.json'").replace('requests_per_arm=14','requests_per_arm=4')
ast.parse(x);(R/'run_priority_execution.py').write_text(x,'utf8');print('Four affected retained cases prepared; no new questions')
