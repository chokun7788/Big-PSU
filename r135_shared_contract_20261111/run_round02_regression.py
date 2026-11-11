"""One serial affected regression batch; preserves every result, stops on failure."""
import json,subprocess,sys,time
from pathlib import Path
R=Path(__file__).resolve().parent
scripts=['run_robustness_matrix.py','verify_shared_contract.py','verify_control_scope.py','verify_verified_sources.py','verify_typo_recovery.py','verify_bounded_response.py']
rows=[]
for script in scripts:
 started=time.perf_counter()
 args=[sys.executable,'-B',str(R/script)]
 if script=='run_robustness_matrix.py':args.append('round02_final')
 result=subprocess.run(args,cwd=R,capture_output=True,text=True,encoding='utf8')
 rows.append({'script':script,'exit_code':result.returncode,'seconds':time.perf_counter()-started,'stdout':result.stdout,'stderr':result.stderr})
 (R/'ROUND02_TEST_BATCH.json').write_text(json.dumps({'all_passed':all(r['exit_code']==0 for r in rows),'rows':rows},ensure_ascii=False,indent=2),encoding='utf8')
 print(json.dumps({'script':script,'exit_code':result.returncode,'seconds':rows[-1]['seconds']}),flush=True)
 if result.returncode:sys.exit(result.returncode)
