import sys,unittest,time,json
from pathlib import Path
OUT=Path(__file__).resolve().parent;sys.path.insert(0,str(OUT/'system/PSU_Esports_Chatbot_Local'))
modules=['tests.test_studio_scope_r57','tests.test_remaining_repairs_r56','tests.test_booking_faults_r56','tests.test_service_repairs_r55','tests.test_conversation_flow_r38','tests.test_user_service_facts_r48','tests.test_live_booking_typo_fixture_20260930','tests.test_p0_calendar_booking_reconciliation_20260925','tests.test_canonical_knowledge']
suite=unittest.TestSuite(unittest.defaultTestLoader.loadTestsFromName(n) for n in modules);start=time.perf_counter();result=unittest.TextTestRunner(verbosity=1).run(suite)
(OUT/'regression_results.json').write_text(json.dumps({'modules':modules,'tests':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'elapsed':time.perf_counter()-start,'details':[(str(t),s) for t,s in result.failures+result.errors]},ensure_ascii=False,indent=2),encoding='utf-8');sys.exit(not result.wasSuccessful())
