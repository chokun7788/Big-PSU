import ast,json
from pathlib import Path
R=Path(__file__).resolve().parent
jobs=list(map(json.loads,(R/'GUARD_SELECTED_JOBS.jsonl').open(encoding='utf8')));indices=[2,13,4];selected=[jobs[i] for i in indices]
(R/'READER_SELECTED_JOBS.jsonl').write_text(''.join(json.dumps(j,ensure_ascii=False)+'\n' for j in selected),'utf8')
(R/'READER_SELECTION.json').write_text(json.dumps({'development_only':True,'fresh_heldout':False,'requests':3,'indices_from_guard01':indices,'new_questions':0,'reason':'Observed count mismatch, missed consumption policy, and bring-vs-consume scope guard'},indent=2),'utf8')
x=(R/'serve_priority.py').read_text('utf8').replace("str(R/'revision03_system')","str(R/'revision04_system')");(R/'serve_reader.py').write_text(x,'utf8')
x=(R/'run_priority_probe.py').read_text('utf8').replace("S=R/'revision03_system';OUT=R/'priority01'","S=R/'revision04_system';OUT=R/'reader01'")
x=x.replace('PRIORITY_SELECTED_JOBS.jsonl','READER_SELECTED_JOBS.jsonl').replace('serve_priority.py','serve_reader.py').replace('==4','==3').replace("'requests_per_arm':4,'total_requests':4", "'requests_per_arm':3,'total_requests':3").replace('r121-context-guard-r03','r121-context-guard-r04').replace('R121-context-guard-r03','R121-context-guard-r04')
ast.parse(x);(R/'run_reader_probe.py').write_text(x,'utf8')
x=(R/'run_priority_execution.py').read_text('utf8').replace("OUT=R/'execution05'","OUT=R/'execution06'").replace("'inference04'","'inference05'").replace('run_priority_probe.py','run_reader_probe.py').replace("R/'priority01/TEST_COMPLETE.json'","R/'reader01/TEST_COMPLETE.json'").replace('requests_per_arm=4','requests_per_arm=3')
ast.parse(x);(R/'run_reader_execution.py').write_text(x,'utf8');print('Three affected retained cases prepared; no new questions')
