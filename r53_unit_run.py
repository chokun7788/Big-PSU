import sys,os,unittest
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r53_current_path.txt').read_text());ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
sys.path.insert(0,str(ROOT));os.environ['PSU_TEST_TMP_DIR']=str(OUT/'test_tmp')
suite=unittest.defaultTestLoader.loadTestsFromNames(['tests.test_semantic_quality_r53','tests.test_research_flow_r52','tests.test_experimental_fallback_deadline_stream','tests.test_conversation_flow_r38'])
with (OUT/(sys.argv[1] if len(sys.argv)>1 else 'targeted_unit_final.txt')).open('x',encoding='utf-8') as s:
 result=unittest.TextTestRunner(stream=s,verbosity=2).run(suite)
print('tests',result.testsRun,'failures',len(result.failures),'errors',len(result.errors))
raise SystemExit(not result.wasSuccessful())
