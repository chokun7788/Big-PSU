import sys,os,json,unittest,time
from pathlib import Path
B=Path(__file__).resolve().parent;sys.path[:0]=[str(B/'system'),str(B)]
from harness import test_temp,configure
tag=sys.argv[1];flag=sys.argv[2]=='1';test_temp('support_'+tag);configure('common',flag)
modules=['tests.test_saved_booking_oracle_r32','tests.test_booking_faults_r56','tests.test_p0_calendar_booking_reconciliation_20260925','tests.test_available_equipment_only_20261001']
start=time.perf_counter();r=unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().loadTestsFromNames(modules))
out=B/('SUPPORT_'+tag+'.json');out.write_text(json.dumps({'tests_run':r.testsRun,'failures':[{'test':str(t),'stack':s} for t,s in r.failures],'errors':[{'test':str(t),'stack':s} for t,s in r.errors],'elapsed':time.perf_counter()-start,'format':'common_config','llm_enabled':flag,'provider_fixture_only':True,'actual_new_wordpress_oracle':False},ensure_ascii=False,indent=2),encoding='utf-8');sys.exit(0 if r.wasSuccessful() else 1)
