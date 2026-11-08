import ast,json
from pathlib import Path
R=Path(__file__).resolve().parent;OLD=R.parent/'r121_context_planner_training_20261022'
jobs=[json.loads(s) for s in (OLD/'ALL_RETAINED_JOBS.jsonl').read_text('utf8').splitlines()]
prefixes=['What is the price of Cockpit and what games are available','How is VR for 30 minutes different from VR for 1 hour']
selected=[next(j for j in jobs if j['question'].startswith(p)) for p in prefixes]
(R/'ELLIPSIS_SELECTED_JOBS.jsonl').write_text(''.join(json.dumps(j,ensure_ascii=False)+'\n' for j in selected),'utf8')
x=(R/'run_api02.py').read_text('utf8').replace("R/'revision02_system'","R/'revision03_system'").replace("OUT=R/'api02'","OUT=R/'ellipsis01'")
x=x.replace('API_SELECTED_JOBS.jsonl','ELLIPSIS_SELECTED_JOBS.jsonl').replace('serve_candidate02.py','serve_candidate03.py')
x=x.replace("for profile in ['psu-r121-base:latest','psu-r121-trained:latest']:","for profile in ['psu-r121-trained:latest']:")
x=x.replace("==8","==2").replace("==16","==2").replace("'requests_per_arm':8,'total_requests':16","'requests_per_arm':2,'total_requests':2")
ast.parse(x);(R/'run_ellipsis_probe.py').write_text(x,'utf8')
x=(R/'run_execution02.py').read_text('utf8').replace("OUT=R/'execution02'","OUT=R/'execution03'").replace("'inference02'","'inference03'").replace('run_api02.py','run_ellipsis_probe.py').replace("R/'api02/TEST_COMPLETE.json'","R/'ellipsis01/TEST_COMPLETE.json'").replace('requests_per_arm=8','requests_per_arm=2')
ast.parse(x);(R/'run_execution03.py').write_text(x,'utf8')
for old,new,output_old,output_new in [('verify_context02.py','verify_context03.py','OFFLINE_CONTEXT_VERIFICATION02.json','OFFLINE_CONTEXT_VERIFICATION03.json'),('verify_regression_context.py','verify_regression_context03.py','CONTEXT_REGRESSION_VERIFICATION.json','CONTEXT_REGRESSION_VERIFICATION03.json')]:
 x=(R/old).read_text('utf8').replace("R/'revision02_system'","R/'revision03_system'").replace(output_old,output_new)
 ast.parse(x);(R/new).write_text(x,'utf8')
print('Two retained compound questions prepared; no new benchmark questions')
