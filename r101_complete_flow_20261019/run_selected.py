"""Final related gates, no large legacy/full corpus and no production writes."""
import hashlib,json,subprocess,sys
from pathlib import Path
R=Path(__file__).resolve().parent
tests=[('test_contract_flow.py','gate_contracts05'),('flow_contracts.py','gate_flow04'),
 ('test_all_categories.py','gate_categories03'),('test_semantic_flow.py','gate_semantic04'),
 ('test_live_bindings.py','gate_live04'),('test_published.py','gate_published03'),
 ('test_conflicts.py','gate_conflicts02'),('test_existing_fixture.py','gate_rental03'),
 ('test_existing_competition_fixture.py','gate_rules02'),('test_flow_v2.py','gate_v203')]
def manifest():return {p.relative_to(R/'system').as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in (R/'system').rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc' and not p.name.endswith(('-wal','-shm'))}
before=manifest();rows=[]
for script,tag in tests:
 log=R/(tag+'_RUN.log')
 with log.open('x',encoding='utf8') as f:result=subprocess.run([sys.executable,'-B','-X','utf8',str(R/script),tag],cwd=R.parent,stdout=f,stderr=subprocess.STDOUT)
 summary_path=R/'verification'/tag/'SUMMARY.json'
 summary=json.loads(summary_path.read_text('utf8')) if summary_path.exists() else {}
 row={'script':script,'tag':tag,'exit_code':result.returncode,'summary':summary}
 rows.append(row);(R/'SELECTED_GATES.json').write_text(json.dumps({'runs':rows,'complete':len(rows)==len(tests),'source_unchanged':before==manifest()},ensure_ascii=False,indent=2),'utf8')
 print(script,result.returncode,summary.get('passed'),summary.get('count'),flush=True)
print('All gates completed; raw failures preserved')
sys.exit(any(r['exit_code'] for r in rows))
