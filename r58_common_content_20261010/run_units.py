import sys,unittest,json,time
from pathlib import Path
OUT=Path(__file__).resolve().parent;CAND=OUT/'system/PSU_Esports_Chatbot_Local';sys.path.insert(0,str(CAND))
run_id=sys.argv[1] if len(sys.argv)>1 else '1'
start=time.monotonic();suite=unittest.defaultTestLoader.loadTestsFromName('tests.test_common_content_r58')
result=unittest.TextTestRunner(verbosity=2).run(suite)
(OUT/f'unit_results_{run_id}.json').write_text(json.dumps({'tests':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'elapsed_sec':time.monotonic()-start,'failure_details':[(str(t),msg) for t,msg in result.failures+result.errors]},ensure_ascii=False,indent=2),encoding='utf-8')
sys.exit(not result.wasSuccessful())
