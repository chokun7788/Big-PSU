"""Latest recorder: preserve v2 and record real, separately gated v3 lineage."""
import json,subprocess,sys,time
from pathlib import Path
from verification_support import R
from app.knowledge.common.domain_flow.training_contract import IMPLEMENTATION_SHA256,file_sha
if (R/'ROUND013_DATASET_GATE_FINALIZATION.json').is_file():
 subprocess.run([sys.executable,'-B',str(R/'record_round013_completion.py')],check=True)
 raise SystemExit(0)
if '--review-progress-only' in sys.argv:
 subprocess.run([sys.executable,'-B',str(R/'record_expedited_review_progress.py')],check=True)
 raise SystemExit(0)
def read(p):return json.loads(p.read_text('utf8'))
def write(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n','utf8')
def report(prefix):
 p=sorted(R.glob(prefix+'*/RESULT.json'))[-1];d=read(p);cs=d['checks'];ok=all(cs.values()) if isinstance(cs,dict) else all(c['passed'] for c in cs) if isinstance(cs,list) else not d.get('failed');assert ok and d.get('all_passed',True) and not d.get('failed'),p
 return {'path':str(p.relative_to(R)),'sha256':file_sha(p),'checks':len(cs) if isinstance(cs,(dict,list)) else cs,'passed':True}
reports={k:report(p) for k,p in [('v3_admission','protocol_v3_admission_controls_'),('training_contract','training_contract_'),('optimizer','training_optimizer_'),('training_history','training_history_input_'),('training_import','saved_training_import_'),('current_consumer','training_consumer_current_')]}
W=R/'training_review_workbench_1793037663397671000';A=sorted(W.glob('protocol_v3_admission_*'))[-1];s=read(A/'SUMMARY.json');V2=sorted(W.glob('current_admission_*'))[-1]
assert s['eligible']==224 and s['unreviewed']==64 and s['quarantined']==1 and s['eligible_split_counts']['train']==142 and s['eligible_split_counts']['development']==82 and not s['training_ready']
assert read(A/'RUNTIME_CONTRACT.json')['admission_implementation_sha256']==read(V2/'RUNTIME_CONTRACT.json')['admission_implementation_sha256']==IMPLEMENTATION_SHA256
alignment=sorted(R.glob('C11_V3_FACET_REAUDIT_*.json'))[-1];aligned=read(alignment);assert aligned['cohort']==str(A.relative_to(R)) and len(aligned['records'])==18 and aligned['new_semantic_review_records_created']==0
assert not (A/'bundle/READY_FOR_OPTIMIZATION.json').exists() and not (V2/'bundle/READY_FOR_OPTIMIZATION.json').exists()
# Refresh prior component records first; this wrapper is the required LAST
# recorder so its versioned-cohort state cannot be replaced by an older script.
subprocess.run([sys.executable,'-B',str(R/'checkpoint_named_periods.py')],check=True,capture_output=True,text=True)
bad=W/'protocol_v3_admission_1793096254452929400';assert read(bad/'SUMMARY.json')['eligible_split_counts']['development']==0 and not (bad/'bundle/READY_FOR_OPTIMIZATION.json').exists()
gp=R/'AUDIT_GAPS.json';gaps=read(gp);g=next(x for x in gaps['gaps'] if x['id']=='G115')
g.update(v3_admission_evidence=reports['v3_admission'],v3_cohort=str(A.relative_to(R)),
 remaining='Explicit v3 codec and artifact-bound admission/migration now implemented.223 previous individual semantic reviews are reused only after exact version-only replay;191 has a separate individual v3 correction. Retained v2 labels/gateway remain unchanged and old191 remains quarantined.64 original rows and other context transforms remain unreviewed/unsupported, semantic-family/eight-strata/metric freeze and actual optimization/model/three-arm evidence remain pending. Dated closure/changed-hours service-period mapping and final76/14 source/API/freeze/activation/re-audit remain open.')
for gap in gaps['gaps']:
 if gap['id'] in {'G102','G103','G110'}:gap['protocol_v3_admission_evidence']=reports['v3_admission'];gap['protocol_v3_cohort']=str(A.relative_to(R))
entry={'id':'G118','requirements':['CONTRACT-15','PHASE-07','PHASE-08','CONTRACT-14'],
 'finding':'Initial v3 migration builder copied stale all-train proposal tags from manual round011 rather than actual final saved train/validation/test file membership. The first real v3 cohort had205train/0development; it had no READY marker and was never optimized. Source labels/reviews were not semantic failures.',
 'baseline':str((bad/'SUMMARY.json').relative_to(R)),'baseline_sha256':file_sha(bad/'SUMMARY.json'),
 'candidate_code':'prepare_protocol_v3_admission.py;system/app/knowledge/common/domain_flow/training_contract.py',
 'state':'implemented_component_verification_final_audit_pending','evidence':reports['v3_admission'],
 'remaining':'Builder now resolves actual origin file membership; independent control streams all281 saved split keys. Migration gate rejects a stale/forged training split; new manual v3 readmission cannot move an old evaluation row to training. Current real cohort142train/82development,64unreviewed/one retained206quarantine/noREADY. Actual semantic family/strata/evaluation/model and final installation acceptance remain pending.'}
gaps['gaps']=[x for x in gaps['gaps'] if x['id']!='G118']+[entry];gaps.update(last_recorded_at=time.time(),complete=False);write(gp,gaps)
criteria={
 'CONTRACT-15':('wire-version migration reuses an existing semantic review only after pinned original-example/review and exact version-only provenance replay',['actual_prior_individual_review_admitted_after_structural_bridge','changed_facet_cannot_reuse_prior_review','changed_operation_cannot_reuse_prior_review','changed_slot_role_cannot_reuse_prior_review','changed_slot_quote_cannot_reuse_prior_review','changed_raw_input_cannot_reuse_prior_review','changed_family_cannot_reuse_prior_review','changed_origin_method_cannot_reuse_prior_review','missing_migration_record_cannot_reuse_old_review','changed_migration_record_hash_rejected']),
 'PHASE-07':('the corrected named-period target has an individual v3 adjudication; changing wire version cannot promote old quarantine or64 unreviewed labels',['actual_row191_new_v3_semantic_review_admitted','old_v2_row191_quarantine_bytes_and_state_retained','old_quarantine_cannot_be_auto_readmitted_by_migration','accepted_flag_cannot_override_old_quarantined_artifact','unreviewed64_not_promoted_by_wire_version','actual_v3_consumer_blocks_unreviewed_inventory_before_frameworks']),
 'PHASE-08':('actual frozen split-file membership overrides stale proposal tags and old exposed evaluation rows cannot become training or fresh holdout',['independent281_saved_file_memberships_preserved','v3_actual_saved_membership_counts_no_fresh_holdout','exposed_old_test_never_becomes_v3_training_or_fresh_holdout','stale_or_forged_train_tag_cannot_override_saved_eval_file','new_manual_v3_review_does_not_authorize_old_test_to_train','historical_split_files_not_modified'])}
for p in R.glob('*_REQUIREMENT_REVIEWS.json'):
 doc=read(p);changed=False
 for row in doc['requirements']:
  if row['requirement_id'] not in criteria:continue
  criterion,checks=criteria[row['requirement_id']];row['criteria']=[c for c in row['criteria'] if c.get('iteration')!='protocol_v3_admission']+[{'criterion':criterion,'state':'passed_controlled_acceptance','evidence':reports['v3_admission']['path'],'evidence_sha256':reports['v3_admission']['sha256'],'checks':checks,'iteration':'protocol_v3_admission','semantic_accuracy_claimed':False}];row['final_revision_api_and_installation_reaudit_pending']=True;changed=True
 if changed:write(p,doc)
ledger=read(R/'COMPLETION_LEDGER.json');identity=[(r['id'],r['text'],r['text_sha256']) for r in ledger['requirements']]
for row in ledger['requirements']:
 if row['id'] not in set(g['requirements'])|set(entry['requirements']):continue
 if row['id'] in entry['requirements'] and 'G118' not in row['gaps']:row['gaps'].append('G118')
 row['acceptance_evidence']=[e for e in row['acceptance_evidence'] if not (isinstance(e,dict) and e.get('iteration')=='protocol_v3_admission')]+[{**reports['v3_admission'],'iteration':'protocol_v3_admission','scope':'actual lineage/split/admission boundary; not whole corpus semantics, optimization or requirement closure'}]
assert identity==[(r['id'],r['text'],r['text_sha256']) for r in ledger['requirements']] and len(identity)==76;write(R/'COMPLETION_LEDGER.json',ledger)
allrows=[r for p in R.glob('*_REQUIREMENT_REVIEWS.json') for r in read(p)['requirements']];assert len(allrows)==len({r['requirement_id'] for r in allrows})==48;count=sum(c['state']=='passed_controlled_acceptance' for r in allrows for c in r['criteria'])
status=read(R/'STATUS.json');status.update(phase='complete_flow_audit_v3_admission_implemented_remaining_labels_and_dated_exceptions_pending',last_recorded_at=time.time(),requirement_specific_controlled_criteria_passed=count,latest_protocol_v3_admission={'path':str(A.relative_to(R)),**s,'reports':reports},latest_checkpoint_script='checkpoint_protocol_v3_admission.py')
status['experimental_period_protocol_v3'].update(training_consumer_supported_with_explicit_runtime=True,old_v2_row191_readmitted=False,v3_row191_individually_readmitted=True,v3_admission=reports['v3_admission'],whole_corpus_ready=False)
status['c11_protocol_field_reaudit']={'path':alignment.name,'sha256':file_sha(alignment),'existing_questions':18,'new_unique_question_reviews':0}
status['last_component_repairs']+=['G115_versioned_admission_component_only','G118'];status['latest_training_gate_reports'].update(reports)
status['next_work']='Continue original source/label review at225-288:64 remain. Round012 has225 individual reviews:65accepted/158corrected-enriched/2quarantined191+206; V2eligible223(142train/81development). V3separate224eligible=223version-only migrations+individual191readmission,142train/82development,206quarantine retained,64unreviewed; noREADY/nooptimizer. No extra unique reviews are claimed for repacking, migration or field rechecks. Re-audit native named-package predicates/opaque names/unit-price scenario, payment document/proof/source actor scope and topical-fragment clarification; retain original source evidence and unresolved206label quarantine. Then other context transforms, semantic-family/eight-strata/sparse/exposure/metric/protocol/clock/source/budget freeze and actual GPU optimization/three-arm evidence. G115dated closure/changed-hours mapping still open. Original28 requirement sections/all14 final category acceptance/G01-G08/G40/other gaps, root/source750/R133459/R134delta or R135supersession, final330same-successful-request raw/source/model/assets/freeze/API/full-live all-table SQLite backup/normal activation/re-audit remain. R135 mutable/uninstalled; R134 installed; no protected process stop/kill, no R132 rerun/analyzer/baselines/regrade; no subagents; keep heartbeat.'
write(R/'STATUS.json',status)
header=f'''## Latest checkpoint — versioned v3 admission/migration +individual191 readmission; G118 split fix; full Flow OPEN

Use **checkpoint_protocol_v3_admission.py** as the LAST recorder. It runs checkpoint_named_periods internally; do not run that or older recorders afterward. R135 remains unfrozen/uninstalled; R134 still installed/running, no owner/frozen/model data edits, no stop/kill, no actual model inference/optimization. Latest source/process/health/code observations remain in STATUS and the historical checkpoint immediately below.

training_contract now takes an explicit supported wire version from runtime contract (default retained v2). It fingerprints schema/prompt/protocol implementation and checks exact packed messages. v3 uses its own codec. A hashed structural migration pins the original example and exact prior accepted/corrected review; replay changes only contract/version fields and rejects changed facet/operation/slot/quote/input/history/family/origin provenance. This reuses actual earlier semantic review; it does not manufacture223 new reviews. Quarantined prior reviews cannot pass via migration or an accepted flag.

Actual v3 cohort **{A.relative_to(R)}**: all289 original keys,225 individually reviewed:224 eligible (223 version-only proofs + one individually corrected v3 row191), one original206quarantine preserved,142train/82development/0holdout,64unreviewed, NOT_READY/nooptimizer. V3_ADJUDICATION_191.json has the seven explicit raw-question/source reasons for schedule/list/service_periods, exact afternoon quote and seven pinned weekday revisions. No business times/permissions/answer state are targets, no fake teacher trace. Old v2 round012/reviews and original191 quarantine remain unchanged; v2 current **{V2.relative_to(R)}** remains225reviewed/223eligible/2quarantines,142train/81development,64unreviewed. Cohorts and unique-question counts must stay distinct.

G118: first v3 builder inherited stale all-train tags from manual proposals ({bad.name},205train/0development). It had noREADY and never optimized; preserve it. Fixed builder resolves final saved-file membership; gates deny stale/forged migration train tags and prohibit moving old eval rows to training even after new manual v3 readmission. {reports['v3_admission']['path']}33 controls independently stream281 actual saved split keys, reject semantic/provenance/hash/version/split mutations and show actual v3 CLI blocks before frameworks. Actual v2 importer27/gate43/history28/guarded optimizer44/currentconsumer4 still pass; optimizer44 uses controlled synthetic model bytes, not actual GPU updates.

{alignment.name} individually rechecks all18 currently reviewed C11 questions against the new service-period facet: explicit booking, maintenance, broad opening state/hours and scalar closing remain their own fields;191 is the only named play-session-time correction. No further labels changed and no18-question increase in unique reviewed counts. This is field-scope review, not arbitrary-question semantics or current business-answer acceptance.

G115 remains OPEN for64 labels/other context transforms, semantic families/eight strata/metric/source/protocol freeze, actual model generation/optimization/three-arm proof and dated closure/changed-hours mapping. Model gateway remains v2; no new adapter promoted. Protocol adaptation plus supervision must be reported jointly; v2 rawR132 is not v3 evaluation. Original76 IDs/text/hash/spec3files/14categories preserved;48 individual requirement reviews/{count} bounded criteria, none finally closed, no semantic/Flow percentage. Keep heartbeat.

Next: {status['next_work']}

## Historical checkpoint before v3 admission/migration

'''
p=R/'CURRENT_HANDOFF_TH.md';old=p.read_text('utf8');marker='## Historical checkpoint before v3 admission/migration\n\n';old=old.split(marker,1)[1] if marker in old else old;p.write_text(header+old,'utf8');print(json.dumps({'gaps':len(gaps['gaps']),'individual_requirement_reviews':48,'bounded_criteria':count,'v2_eligible':223,'v3_eligible':224,'unreviewed':64,'actual_optimization':False,'complete':False,'installed':'R134'}))

# Persist current source-scope evidence after the historical component recorder.
subprocess.run([sys.executable,'-B',str(R/'record_round012_scope.py')],check=True)
if (R/'training_review_workbench_1793037663397671000/expedited_staged_reviews_20261027/SUMMARY.json').exists():
 subprocess.run([sys.executable,'-B',str(R/'record_expedited_review_progress.py')],check=True)
