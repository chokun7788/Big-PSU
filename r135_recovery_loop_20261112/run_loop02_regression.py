"""One serial affected regression batch; stop at first failure, retain output."""
import json,subprocess,sys,time
from pathlib import Path
R=Path(__file__).resolve().parent;rows=[]
archive=R/('loop02_test_batch_'+str(time.time_ns())+'.json')
scripts=['probe_audience_scope.py','run_robustness_matrix.py','verify_alternative_duration.py','verify_price_currency.py','verify_bounded_response.py','verify_verified_sources.py']
for script in scripts:
 args=[sys.executable,'-B',str(R/script)]+(['audience_loop02'] if script=='run_robustness_matrix.py' else [])
 started=time.perf_counter();result=subprocess.run(args,cwd=R,capture_output=True,text=True,encoding='utf8')
 rows.append({'script':script,'exit_code':result.returncode,'seconds':time.perf_counter()-started,'stdout':result.stdout,'stderr':result.stderr})
 text=json.dumps({'all_passed':all(x['exit_code']==0 for x in rows),'rows':rows},ensure_ascii=False,indent=2)
 archive.write_text(text,encoding='utf8')
 (R/'LOOP02_TEST_BATCH.json').write_text(text,encoding='utf8')
 print(json.dumps({'script':script,'exit_code':result.returncode,'seconds':rows[-1]['seconds']}),flush=True)
 if result.returncode:sys.exit(result.returncode)
