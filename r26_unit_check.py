import json,os,sys,unittest
from pathlib import Path
project=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
sys.path.insert(0,str(project));os.environ['PSU_BILINGUAL_EN_ENABLED']='1';os.environ['PSU_SEMANTIC_RETRIEVAL']='0'
report=Path(Path(__file__).with_name('r26_report_path.txt').read_text(encoding='utf-8').strip())
names=['tests.test_competition_content_speed_r26_20261001','tests.test_competition_format_r25_20261001','tests.test_competition_user_questions_r24_20261001','tests.test_competition_target_grounding','tests.test_competition_source_facets','tests.test_competition_taxonomy_contract','tests.test_intent_cue_recovery_20260930','tests.test_integrated_improvement_r21_20261001','tests.test_booking_on_demand_20261001','tests.test_available_equipment_only_20261001','tests.test_keyboard_neighbor_recovery_20260929']
with (report/(sys.argv[1]+'_unit.log')).open('x',encoding='utf-8') as f:result=unittest.TextTestRunner(stream=f,verbosity=2).run(unittest.defaultTestLoader.loadTestsFromNames(names))
summary={'tests':result.testsRun,'failures':[(str(t),msg) for t,msg in result.failures],'errors':[(str(t),msg) for t,msg in result.errors],'success':result.wasSuccessful(),'modules':names}
with (report/(sys.argv[1]+'_unit.json')).open('x',encoding='utf-8') as f:json.dump(summary,f,ensure_ascii=False,indent=2)
print(json.dumps(summary,ensure_ascii=False));sys.exit(not result.wasSuccessful())
