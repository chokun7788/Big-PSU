"""Known CSV/closure fixtures only: separate transport from occupancy oracle."""
import unittest,sys,json,os,time
from pathlib import Path
ROOT=Path(__file__).parent;P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');R=Path((ROOT/'r32_report_path.txt').read_text().strip());sys.path.insert(0,str(P));os.environ['PSU_BILINGUAL_EN_ENABLED']='1';os.environ['PSU_SEMANTIC_RETRIEVAL']='0'
names=['tests.test_booking_on_demand_20261001','tests.test_live_booking_typo_fixture_20260930','tests.test_p0_calendar_booking_reconciliation_20260925']
suite=unittest.defaultTestLoader.loadTestsFromNames(names);started=time.perf_counter()
with (R/'R32_KNOWN_BOOKING_FIXTURES.log').open('x',encoding='utf-8') as out:result=unittest.TextTestRunner(stream=out,verbosity=2).run(suite)
summary=dict(tests=result.testsRun,passed=result.testsRun-len(result.failures)-len(result.errors),failures=[(str(t),e) for t,e in result.failures],errors=[(str(t),e) for t,e in result.errors],elapsed=time.perf_counter()-started,transport='mocked exports, not actual WordPress transport confirmation',occupancy='known synthetic approved/cancelled/no-show/VR/lunch/maintenance/special-closure fixtures',real_occupancy='pending_paused_by_user')
with (R/'R32_KNOWN_BOOKING_SUMMARY.json').open('x',encoding='utf-8') as out:json.dump(summary,out,ensure_ascii=False,indent=2)
print(json.dumps(summary,ensure_ascii=False));sys.exit(not result.wasSuccessful())
