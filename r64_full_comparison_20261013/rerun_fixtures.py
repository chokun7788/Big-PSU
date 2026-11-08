import harness,json,unittest,re,shutil
from pathlib import Path
B=Path(__file__).resolve().parent
harness.test_temp('fixture_repair')
db=B/'legacy_fixture_repair.sqlite';shutil.copy2(B/'legacy.sqlite',db)
harness.configure('legacy',False,db)
items=json.loads((B/'FIXTURE_TESTS_TO_RERUN.json').read_text(encoding='utf-8'))
names=[re.search(r'\(([^)]+)\)',x['test']).group(1) for x in items]
suite=unittest.defaultTestLoader.loadTestsFromNames(names)
with (B/'FIXTURE_REPAIR_RERUN.log').open('x',encoding='utf-8') as f:r=unittest.TextTestRunner(stream=f,verbosity=2).run(suite)
summary={'tests':r.testsRun,'failures':[(str(t),e) for t,e in r.failures],'errors':[(str(t),e) for t,e in r.errors],'success':r.wasSuccessful(),'scope':'only four missing-reference-fixture errors; does not erase original errors'}
(B/'FIXTURE_REPAIR_RERUN.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in summary.items() if k not in ('failures','errors')}))
