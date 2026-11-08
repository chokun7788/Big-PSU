import ast,hashlib,json,sqlite3
from pathlib import Path
B=Path(__file__).resolve().parent;checks=[]
def read(p):return json.loads((B/p).read_text(encoding='utf-8-sig'))
def check(n,ok,d=None):checks.append({'case':n,'passed':bool(ok),'detail':d})
for p,pair in [('repair02/SUMMARY.json',(38,38)),('results/regression01/SUMMARY.json',(43,43)),('results/scope01/SUMMARY.json',(50,50)),('verification/qualification_regression01/RESULTS.json',(41,41)),('SCOPE_GUARDS_REVIEWED.json',(14,14))]:
 r=read(p);check(p,(r['passed'],r['count'])==pair)
review=read('BASELINE_ORACLE_REVIEW.json');check('Baseline reviewed separately',review['passed']==24 and review['count']==29 and review['protocol_mismatches']==4)
raw=read('baseline02/SUMMARY.json');check('Raw baseline retained',raw['passed']==20 and raw['count']==29)
rows=[json.loads(s) for s in (B/'repair02/TURNS.jsonl').read_text(encoding='utf8').splitlines()]
paired={(r['case'],r['turn']) for r in review['checks']}
check('Same 29 baseline turns now pass',sum(r['passed'] for r in rows if (r['case'],r['turn']) in paired)==29)
check('Real session harness does not mock model',not read('repair02/SUMMARY.json')['model_mocked'])
health=read('repair02/MODEL_HEALTH.json');active=[s for s in health['states'] if s['events']]
check('Model transport remains unverified',bool(active) and all(s['successes']==0 and '10013' in s['last_error'] for s in active))
check('Direct preflight blocked',not read('MODEL_PREFLIGHT.json')['transport_ok'] and '10013' in read('MODEL_PREFLIGHT.json')['error'])
check('TCP startup not claimed',not read('R77_STARTUP_STATUS.json')['launcher_completed'])
qa=read('DELIVERY_QA_FINAL.json');check('R77 source files preserved',not qa['source_files_changed'] and qa['source_manifest_count']==1426)
check('Tables and 602 heads preserved',qa['logical_tables_equal'] and qa['heads']==602 and qa['approvals']==0)
check('Source DB still unchanged',hashlib.sha256((B/'system/data/knowledge/common.sqlite').read_bytes()).hexdigest()==qa['database_copy_sha256'])
for rel in qa['changed_code_syntax_checked']:
 ast.parse((B/'system'/rel).read_text(encoding='utf8'));check('Python syntax '+rel,True)
for p in ['README_R78_TH.md','FLOW_R78_TH.md','REPORT_R78_TH.md','HARNESS_REVIEW.md']:
 s=(B/p).read_text(encoding='utf8');check('Readable '+p,s.startswith('# ') and '\ufffd' not in s)
check('Launcher R78 identity and port',"PSU_RUNTIME_VERSION = 'R78'" in (B/'Start-New-Chat.ps1').read_text(encoding='utf8') and '$Port = 8115' in (B/'Start-New-Chat.ps1').read_text(encoding='utf8'))
check('Launcher runtime exists',(B.parent/'PSU_Esports_Chat_New_R69/runtime/python/python.exe').is_file())
c=sqlite3.connect((B/'system/data/knowledge/common.sqlite').as_uri()+'?mode=ro',uri=True)
try:
 rs=[json.loads(row[0]) for row in c.execute('select r.payload from cc_revisions r join cc_heads h on h.record_id=r.record_id and h.head=r.version')]
 rates=[r for r in rs if r['kind']=='rate'];dated=[r for r in rates if r['validity']['effective_until']=='2026-04-01T00:00:00+07:00']
 check('Rate validity count evidence',len(rates)==24 and len(dated)==18)
 check('No fixtures in actual data',not any(r['record_id'].startswith('fixture_r78') for r in rs))
finally:c.close()
result={'count':len(checks),'passed':sum(x['passed'] for x in checks),'checks':checks}
with (B/'DOCUMENT_EVIDENCE_QA.json').open('x',encoding='utf8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print(json.dumps(result,ensure_ascii=False));raise SystemExit(any(not x['passed'] for x in checks))
