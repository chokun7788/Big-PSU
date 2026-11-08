import ast,json
from pathlib import Path
R=Path(__file__).resolve().parent
row=json.loads((R/'ELLIPSIS_SELECTED_JOBS.jsonl').read_text('utf8').splitlines()[1])
(R/'COMPARISON_SELECTED_JOBS.jsonl').write_text(json.dumps(row,ensure_ascii=False)+'\n','utf8')
x=(R/'run_ellipsis_probe.py').read_text('utf8').replace('revision03_system','revision04_system').replace("OUT=R/'ellipsis01'","OUT=R/'comparison01'").replace('ELLIPSIS_SELECTED_JOBS.jsonl','COMPARISON_SELECTED_JOBS.jsonl').replace('serve_candidate03.py','serve_candidate04.py').replace('==2','==1').replace("'requests_per_arm':2,'total_requests':2","'requests_per_arm':1,'total_requests':1")
ast.parse(x);(R/'run_comparison_probe.py').write_text(x,'utf8')
x=(R/'run_execution03.py').read_text('utf8').replace("OUT=R/'execution03'","OUT=R/'execution04'").replace("'inference03'","'inference04'").replace('run_ellipsis_probe.py','run_comparison_probe.py').replace("R/'ellipsis01/TEST_COMPLETE.json'","R/'comparison01/TEST_COMPLETE.json'").replace('requests_per_arm=2','requests_per_arm=1')
ast.parse(x);(R/'run_execution04.py').write_text(x,'utf8')
for old,new in [('verify_context03.py','verify_context04.py'),('verify_regression_context03.py','verify_regression_context04.py')]:
 x=(R/old).read_text('utf8').replace('revision03_system','revision04_system').replace('VERIFICATION03.json','VERIFICATION04.json')
 ast.parse(x);(R/new).write_text(x,'utf8')
print('One retained question prepared to verify the comparison/budget correction')
