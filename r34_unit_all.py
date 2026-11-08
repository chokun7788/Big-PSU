import sys,json,os,unittest,time
from pathlib import Path
project=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');sys.path.insert(0,str(project))
if len(sys.argv)>2:sys.path.insert(0,sys.argv[2])
sys.path.insert(0,str(Path(__file__).parent/'work/r33_test_dependencies'))
report=Path(Path(__file__).with_name('r34_report_path.txt').read_text(encoding='utf-8').strip());run=sys.argv[1]
os.environ['PSU_BILINGUAL_EN_ENABLED']='1';os.environ['PSU_SEMANTIC_RETRIEVAL']='0'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
suite=unittest.defaultTestLoader.discover(str(project/'tests'),pattern='test_*.py',top_level_dir=str(project))
start=time.perf_counter()
with (report/(run+'_unit_all.log')).open('x',encoding='utf-8') as f:result=unittest.TextTestRunner(stream=f,verbosity=2).run(suite)
summary={'tests':result.testsRun,'elapsed_sec':time.perf_counter()-start,'failures':[(str(t),m) for t,m in result.failures],'errors':[(str(t),m) for t,m in result.errors],'skipped':[(str(t),m) for t,m in result.skipped],'success':result.wasSuccessful()}
with (report/(run+'_unit_all.json')).open('x',encoding='utf-8') as f:json.dump(summary,f,ensure_ascii=False,indent=2)
print(json.dumps(summary,ensure_ascii=False));sys.exit(not result.wasSuccessful())

