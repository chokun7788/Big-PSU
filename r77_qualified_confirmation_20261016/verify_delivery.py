"""Document/evidence consistency; does not call a model or change data."""
import ast,hashlib,json,sqlite3
from pathlib import Path
B=Path(__file__).resolve().parent
checks=[]
def check(name,ok,detail=None):checks.append({'case':name,'passed':bool(ok),'detail':detail})
for name in ['FLOW_R77_TH.md','REPORT_R77_TH.md','README_R77_TH.md','NEXT_STEPS_R77_TH.md']:
    s=(B/name).read_text(encoding='utf8')
    check(name+' readable',s.startswith('# ') and '\ufffd' not in s and len(s)>500)
    check(name+' Markdown separation',all(i+1==len(s.splitlines()) or not s.splitlines()[i+1].strip() for i,line in enumerate(s.splitlines()) if line.startswith('#')))
expected={'verification/qualified01/RESULTS.json':(34,34),'verification/qualified02/RESULTS.json':(41,41),'verification/rephrase_regression01/RESULTS.json':(34,34),'results/regression01/SUMMARY.json':(43,43),'results/scope01/SUMMARY.json':(50,50)}
for path,pair in expected.items():
    r=json.loads((B/path).read_text(encoding='utf8'));check(path,(r['passed'],r['count'])==pair and r['llm_enabled'],{'passed':r['passed'],'count':r['count']})
old=json.loads((B/'verification/baseline01/RESULTS.json').read_text(encoding='utf8'))
new=json.loads((B/'verification/qualified02/RESULTS.json').read_text(encoding='utf8'))
names={r['case'] for r in old['checks'][1:9]}
check('Paired baseline 0/8 and R77 8/8',len(names)==8 and sum(r['passed'] for r in old['checks'] if r['case'] in names)==0 and sum(r['passed'] for r in new['checks'] if r['case'] in names)==8)
for suite in ['regression01','scope01']:
    h=json.loads((B/'results'/suite/'MODEL_HEALTH.json').read_text(encoding='utf8'))
    actual=[s for s in h['states'] if s['events']]
    check(suite+' real transport unverified',bool(actual) and all(s['successes']==0 and '10013' in s['last_error'] for s in actual))
qa=json.loads((B/'DELIVERY_QA_FINAL.json').read_text(encoding='utf8'))
check('Preserved source files',qa['source_manifest_count']==1425 and not qa['source_files_changed'])
check('Source database unchanged',qa['logical_tables_equal'] and qa['heads']==602 and qa['approvals']==0 and qa['database_source_sha256']==qa['database_copy_sha256'])
check('No active common release',qa['tables']['cc_releases']['rows']==0)
c=sqlite3.connect((B/'system/data/knowledge/common.sqlite').as_uri()+'?mode=ro',uri=True)
try:
    rows=c.execute('select r.payload from cc_revisions r join cc_heads h on h.record_id=r.record_id and h.head=r.version where h.withdrawn=0').fetchall()
    profiles=[json.loads(s[0]) for s in rows if json.loads(s[0])['fields'].get('query_profile',{}).get('status')=='known']
    check('Only two real known query profiles',len(profiles)==2,{'count':len(profiles)})
    check('No fixture records in actual database',not any(json.loads(s[0])['record_id'].startswith('fixture_r77') for s in rows))
finally:c.close()
for rel in qa['changed_code_syntax_checked']:
    ast.parse((B/'system'/rel).read_text(encoding='utf8'));check('Python syntax '+rel,True)
check('Launcher runtime exists',(B.parent/'PSU_Esports_Chat_New_R69/runtime/python/python.exe').is_file())
launcher=(B/'Start-New-Chat.ps1').read_text(encoding='utf8')
check('R77 chat launcher identity and port',"$Port = 8113" in launcher and "PSU_RUNTIME_VERSION = 'R77'" in launcher)
check('R77 editor port','--port 8114' in (B/'Open-Data-Editor.ps1').read_text(encoding='utf8'))
check('Changeset available',(B/'CHANGESET_FINAL.patch').is_file())
result={'count':len(checks),'passed':sum(x['passed'] for x in checks),'checks':checks}
with (B/'DOCUMENT_EVIDENCE_QA.json').open('x',encoding='utf8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print(json.dumps(result,ensure_ascii=False));raise SystemExit(any(not x['passed'] for x in checks))
