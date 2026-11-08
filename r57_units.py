import sys,unittest,json,os,tempfile,time
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r57_current_path.txt').read_text());ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
sys.path.insert(0,str(ROOT));os.chdir(ROOT)
tmp=OUT/(sys.argv[1]+'_tmp');tmp.mkdir();tempfile.tempdir=str(tmp);os.environ['PSU_TEST_TMP_DIR']=str(tmp)
modules=sys.argv[2:] or ['tests.test_remaining_repairs_r56','tests.test_booking_faults_r56','tests.test_service_repairs_r55','tests.test_conversation_flow_r38','tests.test_research_flow_r52','tests.test_user_service_facts_r48','tests.test_live_booking_typo_fixture_20260930','tests.test_semantic_quality_r53','tests.test_experimental_fallback_deadline_stream','tests.test_p0_calendar_booking_reconciliation_20260925']
start=time.perf_counter()
with (OUT/(sys.argv[1]+'.txt')).open('x',encoding='utf-8') as f:
    result=unittest.TextTestRunner(stream=f,verbosity=2).run(unittest.defaultTestLoader.loadTestsFromNames(modules))
summary=dict(tests=result.testsRun,failed=len(result.failures),errors=len(result.errors),elapsed_sec=time.perf_counter()-start,modules=modules)
with (OUT/(sys.argv[1]+'.json')).open('x',encoding='utf-8') as f:json.dump(summary,f,indent=2)
print(summary)
sys.exit(0 if result.wasSuccessful() else 1)
