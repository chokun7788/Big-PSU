import json,os,sys,subprocess,time,urllib.request
from pathlib import Path
root=Path(__file__).parent;project=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');report=Path((root/'r28_report_path.txt').read_text(encoding='utf-8').strip())
sys.path.insert(0,str(project))
from app.knowledge.localization import approved_localization
port=sys.argv[1];url='http://127.0.0.1:'+port
for n in range(30):
    try:health=json.load(urllib.request.urlopen(url+'/health',timeout=2));break
    except OSError:
        if n==29:raise
        time.sleep(.5)
assert health['runtime']['version']=='2026.10.02-competition-composition-r28-guard-verified'
with (report/'http_final_health_before.json').open('x',encoding='utf-8') as f:json.dump(health,f,ensure_ascii=False,indent=2)
source={r['id']:r for r in (json.loads(x) for x in (project/'data/competition_rules/competition_rule_chunks.jsonl').read_text(encoding='utf-8').splitlines() if x.strip())}
ids=['competition_rules_cs2_psu_phuket_2026_s06_c01','competition_rules_cs2_psu_phuket_2026_s58_c01']
clauses=[]
for i in ids:
    text=approved_localization(source[i],'text');assert text
    clauses+= [line.strip() for line in text.splitlines() if line.strip()]
failed=[json.loads(x) for x in (report/'full_r28_A_details.jsonl').read_text(encoding='utf-8').splitlines() if x.strip()]
cases=[dict(id=r['id'],anchor='dispute-resolution',locale='en',kind='regression',mutation=r['mutation'],question=r['question'],status='answer',clauses=clauses,sources=ids) for r in failed if 'wrong_facet_evidence' in r['failures']]
assert len(cases)==12
with (report/'http_resolution_12_fixture.json').open('x',encoding='utf-8') as f:json.dump({'cases':cases,'scope':'12 true wrong-facet cases from unchanged Gold, expected source s06/s58 English clauses; not owner approval'},f,ensure_ascii=False,indent=2)
text=(root/'r28_final_web_check.py').read_text(encoding='utf-8').replace('2026.10.02-competition-composition-r28-verified','2026.10.02-competition-composition-r28-guard-verified')
with (root/'r28_guard_web_check.py').open('x',encoding='utf-8') as f:f.write(text)
tasks=[
 ('280',[str(project/'tools/run_competition_composition_r28.py'),'--fixture',str(report/'composition_fixture_v3.json'),'--report',str(report),'--run','verified_http280','--url',url,'--llm']),
 ('resolution12',[str(project/'tools/run_competition_composition_r28.py'),'--fixture',str(report/'http_resolution_12_fixture.json'),'--report',str(report),'--run','verified_http_resolution12','--url',url,'--llm']),
 ('320',[str(project/'tools/run_competition_contract_r27.py'),'--fixture',str(report/'content_contract_fixture_v2.json'),'--report',str(report),'--run','verified_http320','--url',url,'--llm']),
 ('36',[str(root/'r28_guard_web_check.py'),port,'guard_verified_regression']),
]
for label,args in tasks:
    with (report/('verified_http_'+label+'_runner.log')).open('x',encoding='utf-8') as f:result=subprocess.run([sys.executable,'-u','-X','utf8',*args],cwd=root,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),stdout=f,stderr=subprocess.STDOUT)
    print(json.dumps({'completed':label,'exit_code':result.returncode}),flush=True)
    if result.returncode:raise SystemExit(result.returncode)
health=json.load(urllib.request.urlopen(url+'/health',timeout=3))
with (report/'http_final_health_after.json').open('x',encoding='utf-8') as f:json.dump(health,f,ensure_ascii=False,indent=2)
print('Sequential web suite completed.')
