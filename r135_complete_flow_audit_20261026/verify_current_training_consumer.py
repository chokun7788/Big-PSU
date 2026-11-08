"""Current real admission remains blocked before model frameworks or assets."""
import json,subprocess,sys,time
from verification_support import R
W=R/'training_review_workbench_1793037663397671000';A=sorted(W.glob('current_admission_*'))[-1]
s=json.loads((A/'SUMMARY.json').read_text('utf8'));O=R/('training_consumer_current_'+str(time.time_ns()));O.mkdir()
# These are intentionally not base/evaluation proof. The incomplete actual
# inventory must stop before those later admission stages can be reached.
unused=O/'UNUSED_REF.json';unused.write_text('{}\n','utf8')
command=[sys.executable,'-B',str(R/'system/tools/train_reviewed_planner.py'),'--dataset',str(A/'bundle'),'--runtime-contract',str(A/'RUNTIME_CONTRACT.json'),'--base','D:/CodexTraining/psu-r121-20261022/model','--base-manifest-ref',str(unused),'--protocol-ref',str(unused),'--artifact-root',str(R.parent),'--check-only']
p=subprocess.run(command,capture_output=True,text=True,timeout=300);observed=json.loads(p.stdout)
final_round=s['manual_round']=='review_round_013'
checks={'actual_current_dataset_gate_state':s['individually_reviewed']==(289 if final_round else 225) and s['training_ready']==final_round,
 'eligible_quarantine_and_unreviewed_counts_are_distinct':s['eligible_reviewed_rows']==(286 if final_round else 223) and s['quarantined']==(3 if final_round else 2) and s['unreviewed']==(0 if final_round else 64),
 'actual_cli_rejects_missing_base_protocol' if final_round else 'actual_cli_rejects_partial_rows':p.returncode==2 and observed['phase']=='admission_blocked' and not observed['admitted'],
 'no_model_frameworks_imported':observed['model_frameworks_loaded']==[]}
report={'all_passed':all(checks.values()),'checks':checks,'current_admission':str(A.relative_to(R)),'command':command,'process':{'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr},'optimizer_started':False,'actual_model_inferences':0,'base_or_evaluation_protocol_admission_claimed':False}
(O/'RESULT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n','utf8');print(json.dumps({'output':str(O),'all_passed':report['all_passed'],'checks':len(checks)}));assert report['all_passed']
