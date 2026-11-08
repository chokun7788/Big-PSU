import ast,json
from pathlib import Path
B=Path(__file__).resolve().parent;checks=[]
def check(name,ok):checks.append({'case':name,'passed':bool(ok)})
for name in ('FLOW_R75_TH.md','REPORT_R75_TH.md','REMAINING_WORK_R75_TH.md','README_R75_TH.md'):
    s=(B/name).read_text(encoding='utf8')
    check('UTF8 '+name,len(s)>300 and '\ufffd' not in s)
    check('Fences '+name,s.count('```')%2==0)
for name in ('test_confirmation.py','test_task_language.py','audit_preservation.py'):
    ast.parse((B/name).read_text(encoding='utf8'));check('Harness syntax '+name,True)
qa=json.loads((B/'DELIVERY_QA_FINAL.json').read_text(encoding='utf8'))
check('Original system unchanged',not qa['source_files_changed'])
check('602 heads and logical DB identical',qa['heads']==602 and qa['logical_tables_equal'] and qa['approvals']==0)
for path,count in [('verification/confirmation01/RESULTS.json',28),('verification/language02/RESULTS.json',16),('results/regression01/SUMMARY.json',43),('results/scope01/SUMMARY.json',50)]:
    r=json.loads((B/path).read_text(encoding='utf8'));check('Reported score '+path,r['count']==r['passed']==count)
report=(B/'REPORT_R75_TH.md').read_text(encoding='utf8')
check('Report preserves extra-turn tradeoff and real model limitation',all(s in report for s in ('หนึ่งรอบ','WinError 10013','model successes=0','ไม่ใช่หลักฐานว่าโมเดล')))
check('Final diff is present',(B/'CHANGESET_FINAL.patch').is_file())
check('Runtime LLM stays ON',"PSU_EXPERIMENTAL_ALLOW_LLM = '1'" in (B/'Start-New-Chat.ps1').read_text(encoding='utf8'))
result={'count':len(checks),'passed':sum(c['passed'] for c in checks),'checks':checks}
with (B/'DOCUMENT_QA.json').open('x',encoding='utf8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print(json.dumps({k:v for k,v in result.items() if k!='checks'}));raise SystemExit(any(not c['passed'] for c in checks))
