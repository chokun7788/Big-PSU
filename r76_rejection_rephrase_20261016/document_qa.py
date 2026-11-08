import ast,json
from pathlib import Path
B=Path(__file__).resolve().parent;checks=[]
def check(name,ok):checks.append({'case':name,'passed':bool(ok)})
for name in ('FLOW_R76_TH.md','REPORT_R76_TH.md','NEXT_STEPS_R76_TH.md','README_R76_TH.md'):
    s=(B/name).read_text(encoding='utf8')
    check('UTF8 '+name,len(s)>300 and '\ufffd' not in s)
    check('Fences '+name,s.count('```')%2==0)
for name in ('test_reply_parser.py','test_rephrase_dialogue.py','test_debug_query.py','audit_preservation.py'):
    ast.parse((B/name).read_text(encoding='utf8'));check('Harness syntax '+name,True)
qa=json.loads((B/'DELIVERY_QA_REVIEWED.json').read_text(encoding='utf8'))
check('Original R75 unchanged',not qa['source_files_changed'] and qa['source_manifest_count']==1424)
check('Logical data and 602 heads preserved',qa['logical_tables_equal'] and qa['heads']==602 and qa['approvals']==0)
for path,expected in [('verification/parser01/RESULTS.json',32),('verification/rephrase02/RESULTS.json',34),('verification/debug01/RESULTS.json',3),('results/regression01/SUMMARY.json',43),('results/scope01/SUMMARY.json',50)]:
    r=json.loads((B/path).read_text(encoding='utf8'));check('Reported result '+path,r['count']==r['passed']==expected)
baseline=json.loads((B/'verification/baseline01/RESULTS.json').read_text(encoding='utf8'))
check('Baseline failure retained',baseline['count']==8 and baseline['passed']==2)
report=(B/'REPORT_R76_TH.md').read_text(encoding='utf8')
check('Report separates model/transport fixture claims',all(s in report for s in ('controlled','WinError 10013','ไม่ใช่ผล inference','ไม่ใช่สถานะ WordPress จริง')))
check('First incomplete round preserved',(B/'verification/rephrase01/CHECKS.jsonl').is_file() and not (B/'verification/rephrase01/RESULTS.json').exists())
check('Final diff exists',(B/'CHANGESET_REVIEWED.patch').is_file())
check('LLM stays enabled',"PSU_EXPERIMENTAL_ALLOW_LLM = '1'" in (B/'Start-New-Chat.ps1').read_text(encoding='utf8'))
result={'count':len(checks),'passed':sum(c['passed'] for c in checks),'checks':checks}
with (B/'DOCUMENT_QA.json').open('x',encoding='utf8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print(json.dumps({k:v for k,v in result.items() if k!='checks'}));raise SystemExit(any(not c['passed'] for c in checks))
