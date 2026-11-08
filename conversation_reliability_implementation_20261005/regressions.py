import os,sys,json,unittest,importlib.util,time,subprocess
from pathlib import Path
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT));os.chdir(ROOT)
os.environ.update(PSU_SEMANTIC_RETRIEVAL='0',PSU_BILINGUAL_EN_ENABLED='1',PSU_PERFORMANCE_TRACE='0',
                 PSU_CHAT_LOG_DIR=str(HERE/'regression_logs'),PSU_CHAT_LOG_SQLITE_PATH=str(HERE/'regression_logs/history.sqlite3'))
names=['test_competition_session_context_r35','test_competition_reliability_r31','test_competition_recorded_year_r32',
       'test_r30_closed_query_boundaries','test_r30_competition_and_ingress', 'test_p0_calendar_booking_reconciliation_20260925',
       'test_live_booking_typo_fixture_20260930']
summary=[]
stamp=time.strftime('%H%M%S')
for name in names:
    spec=importlib.util.spec_from_file_location(name,ROOT/'tests'/f'{name}.py')
    module=importlib.util.module_from_spec(spec);sys.modules[name]=module;spec.loader.exec_module(module)
    with (HERE/f'{stamp}_{name}.log').open('w',encoding='utf-8') as stream:
        result=unittest.TextTestRunner(stream=stream,verbosity=2).run(unittest.defaultTestLoader.loadTestsFromModule(module))
    record={'suite':name,'run':result.testsRun,'failures':[(str(t),txt) for t,txt in result.failures], 'errors':[(str(t),txt) for t,txt in result.errors], 'skipped':result.skipped}
    summary.append(record);print(name,result.testsRun,'failures',len(result.failures),'errors',len(result.errors),flush=True)
for name in ['smoke_test_booking_price_regression','smoke_test_pc_service_fee','smoke_test_decision_artifact','smoke_test_availability_policy_regressions']:
    result=subprocess.run([sys.executable,'-B',str(ROOT/'tests'/f'{name}.py')],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,encoding='utf-8',timeout=180)
    (HERE/f'{stamp}_{name}.log').write_text(result.stdout,encoding='utf-8')
    summary.append({'suite':name,'returncode':result.returncode,'log':f'{stamp}_{name}.log'})
    print(name,result.returncode,flush=True)
(HERE/f'regression_summary_{stamp}.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
