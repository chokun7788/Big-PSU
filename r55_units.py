import os,sys,unittest,json,time
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r55_current_path.txt').read_text());ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
sys.path.insert(0,str(ROOT));os.chdir(ROOT);os.environ['PSU_TEST_TMP_DIR']=str(OUT/('test_tmp_'+sys.argv[1]))
Path(os.environ['PSU_TEST_TMP_DIR']).mkdir(exist_ok=True)
names=sys.argv[2:] or ['tests.test_service_repairs_r55']
with (OUT/('units_'+sys.argv[1]+'.txt')).open('x',encoding='utf-8') as f:
    suite=unittest.defaultTestLoader.loadTestsFromNames(names);start=time.perf_counter();result=unittest.TextTestRunner(stream=f,verbosity=2).run(suite)
    record=dict(tests=result.testsRun,failures=len(result.failures),errors=len(result.errors),elapsed=time.perf_counter()-start,modules=names)
    (OUT/('units_'+sys.argv[1]+'.json')).write_text(json.dumps(record,indent=2),encoding='utf-8');print(record)
    for test,detail in result.failures+result.errors:print(str(test),detail)
