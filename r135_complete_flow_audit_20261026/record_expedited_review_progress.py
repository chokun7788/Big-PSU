"""Fast audit-only progress recorder; invoked by the canonical checkpoint."""
import json,time
from pathlib import Path
from verification_support import R
from app.knowledge.common.domain_flow.training_contract import file_sha,digest,source_identity

def read(p):return json.loads(p.read_text('utf8'))
W=R/'training_review_workbench_1793037663397671000';O=W/'expedited_staged_reviews_20261027';summary=read(O/'SUMMARY.json');base=W/summary['base_compiled_manual_round'];examples=[json.loads(x) for x in (base/'EXAMPLES.jsonl').read_text('utf8').splitlines()];lookup={x['annotation_provenance']['historical_review_ref']['line']-1:x for x in examples};source=read(W/'SOURCE_SNAPSHOT.json');records=[]
base_sha=file_sha(base/'EXAMPLES.jsonl');source_sha=file_sha(W/'SOURCE_SNAPSHOT.json');identity=digest(source_identity(source))
for p in sorted(O.glob('STAGED_*.json')):
 d=read(p);x=lookup[d['original_row']];assert d['raw_question']==x['raw_question'] and d['question_key']==x['question_key'] and d['prior_label']==x['plan_label'] and d['base_example_ref']['sha256']==base_sha and d['source_snapshot_ref']['sha256']==source_sha and d['source_identity_sha256']==identity
 for rid,evidence in d['source_field_evidence'].items():assert evidence=={'revision':source['release']['records'][rid]['revision'],'record_sha256':digest(source['release']['records'][rid])}
 records.append({'path':str(p.relative_to(R)),'sha256':file_sha(p),'original_row':d['original_row'],'decision':d['decision']})
assert len(records)==summary['staged_individual_reviews'] and summary['staged_reviews_admitted_to_current_cohorts'] is False
window=read(R/'EXPEDITED_WINDOW_20261027.json');status=read(R/'STATUS.json');status['latest_staged_language_reviews']={'path':str((O/'SUMMARY.json').relative_to(R)),'sha256':file_sha(O/'SUMMARY.json'),**summary,'records':records};status['last_recorded_at']=time.time();status['latest_checkpoint_script']='checkpoint_protocol_v3_admission.py --review-progress-only';status['expedited_window'].update(method='stage actual individual reviews, then single final cohort compile; dependency-scoped tests only',gpu_free_MiB_observed=window['gpu_observation']['free_MiB'])
remaining=sorted(set(range(225,289))-{d['original_row'] for d in records});nextrow=remaining[0] if remaining else None
status['next_work']=f"Expedited5-8h window in EXPEDITED_WINDOW_20261027.json. Continue original manual source/label review at{nextrow}: {len(remaining)} not individually reviewed. {len(records)} actual staged reviews are pinned, but NOT admitted: compiled round012/current v2 still225reviews223eligible, v3 separate224eligible, noREADY/nooptimizer. Do not repack/rebuild cohorts or repeat unchanged tests after every small batch; compose all64 staged rows once after individual review is complete, then refresh v3 lineage and run relevant gates once. After source-label review, finish shared implementation gaps/G115 dated exceptions/remaining28 sections/all14 final category acceptance, context transforms/families/eight strata/metrics/protocol/source/clock/budgets freeze, actual optimization/three-arm evidence with measured memory feasibility, root/source750/R133459/R134delta or supersession/final330 exact same-successful-request raw/source/model/assets/freeze/API/full-live backup/normal activation/re-audit. GPU6GB has about2GBfree while protected model runs: no stop/kill, no fake training proof, no R132/analyzer/baseline reruns or subagents. Legacy code+data delivery is done; do not redo it. Keep heartbeat; no whole-flow completion claim from the expedited time target."
(R/'STATUS.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n','utf8')
header=f'''## Latest expedited checkpoint — actual staged reviews, single final cohort build pending

User requested attempting completion in5–8hours by changing work order/removing repetition, with original76/14 scope retained. Start2026-10-27T13:23:31Z (20:23Asia/Bangkok),5h checkpoint2026-10-27T18:23:31Z,8h checkpoint2026-10-27T21:23:31Z. See EXPEDITED_WINDOW_20261027.json. This is a target, not a completion certificate. Read-only GPU observation: RTX4050Laptop6GB,4083MiBused/2058MiBfree; selected protected model remains running. Actual optimization/three-arm capacity/time remain a material constraint, not a reason to invent proof or stop useful audit work.

Canonical checkpoint remains **checkpoint_protocol_v3_admission.py**. Use **--review-progress-only** while staging: it invokes only this fast evidence recorder, preserving compiled cohorts and all previous component findings. Its full mode still records period/v3/round012 source-scope evidence and then current staged progress. Never call inner/old recorders afterward.

Actual staged individual source/label reviews: **{len(records)} rows**, {summary['staged_rows']}; all seven criterion-specific manual reasons/raw questions/proposed label/source revisions/hashes are pinned in {O.relative_to(R)}. **{summary['unique_original_questions_read_including_staged']} unique original questions read including staging**, **{len(remaining)} still not individually reviewed**, next{nextrow}. Staged reviews are not yet admitted, not a new model measurement and not whole-requirement acceptance. Prior compiled round012225reviews and current v2223eligible/v3separate224eligible remain unchanged/noREADY/nooptimizer; their unreviewed64 is the cohort admission inventory, distinct from current manual staging progress. Once all64 are individually reviewed, compile/admit once and refresh the v3 migration/readmissions against actual current reviews. No fake teacher traces, no business answers in targets, no fresh-holdout claim from exposed rows.

Retain48 requirement-specific reviews/212 bounded criteria, all76 final closures still pending. Native source discovery225 shows the expected verification-time clause and unchanged-status follow-up with an explicit generic condition-application warning; retain this as a G40 condition-proof review item rather than deleting the warning or counting it as a source content regression. Other source-read controls/unknown validity caveats remain in the historical checkpoint below. Legacy code+data ZIP with detailed head/sender guide is complete; no repackage/retest needed without changes.

Latest additional source-only candidate repair report: {status.get('latest_expedited_controls_reaudit',{})}. G123 full stick-label precedence, G124 named-game controller-use routing and G125 inverse action predicate passed15 new/25 source-scope/23 predicate controls. The failed source-scope report remains retained. No model inference or installed-runtime change; other observed source/predicate gaps are explicitly listed in that report. Do not rerun these unchanged controls solely to refresh a checkpoint.

Next: {status['next_work']}

## Historical checkpoint before expedited staged review

'''
p=R/'CURRENT_HANDOFF_TH.md';old=p.read_text('utf8');marker='## Historical checkpoint before expedited staged review\n\n';old=old.split(marker,1)[1] if marker in old else old;p.write_text(header+old,'utf8')
print(json.dumps({'staged_individual_reviews':len(records),'unique_questions_read_including_staged':summary['unique_original_questions_read_including_staged'],'not_individually_reviewed':len(remaining),'next_row':nextrow,'cohorts_rebuilt':False,'tests_repeated':False,'actual_training':False,'whole_flow_complete':False}))
