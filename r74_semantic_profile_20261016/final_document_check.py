"""Syntax and document evidence checks, without opening network sockets."""
import ast,json,re
from pathlib import Path
B=Path(__file__).resolve().parent
checks=[]
def check(name,ok,detail=None):checks.append({'case':name,'passed':bool(ok),'detail':detail})
for name in ('semantic_profile','entity_search','answer','request_roles','unconfirmed_request'):
    p=B/'system/app/knowledge/common'/f'{name}.py'
    ast.parse(p.read_text(encoding='utf8'),filename=str(p));check('Python syntax '+name,True)
for name in ('run_targeted','test_semantic_profiles','audit_delivery','payment_boundary_cases','semantic_acceptance_cases'):
    p=B/f'{name}.py';ast.parse(p.read_text(encoding='utf8'),filename=str(p));check('Harness syntax '+name,True)
qa=json.loads((B/'DELIVERY_QA.json').read_text(encoding='utf8'))
check('Original R73 system unchanged',not qa['source_files_changed'])
check('All knowledge tables identical',qa['logical_tables_equal'] and qa['heads']==602 and not qa['schema_errors'])
for name in ('FLOW_R74_TH.md','REPORT_R74_TH.md','README_R74_TH.md'):
    p=B/name;s=p.read_text(encoding='utf8')
    check('UTF8/document content '+name,'\ufffd' not in s and len(s)>100)
    check('Document fence balance '+name,s.count('```')%2==0)
report=(B/'REPORT_R74_TH.md').read_text(encoding='utf8')
check('Report distinguishes controlled model outputs',all(x in report for x in ('32/32','7/8','WinError 10013','SEMANTIC_LIMITATION.json')))
check('Report explicitly retains semantic failure limitation','ยังรับได้' in report and 'independent semantic judge' in report)
summary=json.loads((B/'verification/semantic02/RESULTS.json').read_text(encoding='utf8'))
check('Controlled fixtures reported honestly',summary['count']==32 and summary['passed']==32 and summary['controlled_model_responses'] and not summary['real_model_inference_verified'])
base=json.loads((B/'results/baseline_boundary01/ORACLE_REVIEW.json').read_text(encoding='utf8'))
new=json.loads((B/'results/boundary02/ORACLE_REVIEW.json').read_text(encoding='utf8'))
check('Stored answers compared with same corrected oracle',base['passed']==11 and new['passed']==14 and base['count']==new['count']==14 and base['new_requests']==new['new_requests']==0)
check('LLM remains enabled in launcher',"PSU_EXPERIMENTAL_ALLOW_LLM = '1'" in (B/'Start-New-Chat.ps1').read_text(encoding='utf8'))
check('Old route IDs absent from production selection code',all('procedure_wrong_slip' not in (B/'system/app/knowledge/common'/f'{name}.py').read_text(encoding='utf8') for name in ('semantic_profile','entity_search','question_profiles','answer')))
result={'checks':checks,'passed':sum(x['passed'] for x in checks),'count':len(checks),'no_model_or_browser_claim':True}
with (B/'DOCUMENT_QA.json').open('x',encoding='utf8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print(json.dumps({k:v for k,v in result.items() if k!='checks'}))
raise SystemExit(any(not x['passed'] for x in checks))
