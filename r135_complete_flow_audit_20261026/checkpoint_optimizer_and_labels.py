"""Record bounded consumer controls and actual label adjudications; no closure."""
import ast,hashlib,json,time
from pathlib import Path
R=Path(__file__).resolve().parent
def read(p):return json.loads(p.read_text('utf8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n','utf8')
def report(prefix):
 p=sorted(R.glob(prefix+'*/RESULT.json'))[-1];d=read(p);assert d['all_passed'] and all(d['checks'].values()),p
 return {'path':str(p.relative_to(R)),'sha256':sha(p),'checks':len(d['checks']),'passed':True}
reports={n:report(p) for n,p in [('training_optimizer','training_optimizer_'),('training_contract','training_contract_'),('training_import','saved_training_import_'),('graph','graph_verification_'),('wire','wire_compatibility_')]}
o=read(R/reports['training_optimizer']['path']);assert not o['optimizer_started'] and o['gpu_optimization_tested'] is False
W=R/'training_review_workbench_1793037663397671000';A=sorted(W.glob('current_admission_*'))[-1];summary=read(A/'SUMMARY.json');manual=W/summary['manual_round'];m=read(manual/'SUMMARY.json')
assert summary['manual_round']=='review_round_008' and summary['individually_reviewed']==155 and summary['unreviewed']==134 and not summary['training_ready']
assert m['prior_adjudications_unchanged'] and m['accepted']==52 and m['corrected_or_enriched']==103 and not (A/'bundle/READY_FOR_OPTIMIZATION.json').exists()
old_code=R/'COMPONENT_CODE_OBSERVATION_1793069695308456800.json';old=read(old_code)['current_candidate_python_sha256']
new_files=['system/app/knowledge/common/domain_flow/training_optimizer.py','system/tools/train_reviewed_planner.py']
assert all(n.replace('/','\\') not in old and n not in old for n in new_files)
baseline=R/('training_optimizer_gap_'+str(time.time_ns()));baseline.mkdir()
finding={'finding':'R135 had an artifact-bound dataset preparer/consumer gate but no optimizer entrypoint consuming it. The historical R129 trainer imports torch before its old generic review assertion and cannot stand in for the current reviewed dataset consumer.',
         'prior_code_manifest':str(old_code.relative_to(R)),'prior_code_manifest_sha256':sha(old_code),'new_consumer_files_absent_from_prior_manifest':new_files,
         'historical_trainer_modified':False,'actual_gpu_execution_proven':False,'actual_real_dataset_admitted':False}
write(baseline/'FINDING.json',finding)
gaps=read(R/'AUDIT_GAPS.json');entry={'id':'G110','requirements':['FLOW-23','PHASE-08','PHASE-09'],'finding':finding['finding'],'baseline':str((baseline/'FINDING.json').relative_to(R)),
 'candidate_code':';'.join(new_files),'evidence':reports['training_optimizer'],'state':'implemented_guarded_consumer_pending_real_protocol_data_gpu_and_final_acceptance',
 'remaining':'Only gate/packing/protocol/path/telemetry/error-state controls are exercised. Actual corpus155/289; real semantic-family/eight-strata/metrics freeze, native transformation corpus, per-type semantic validation, actual GPU optimization with gradients/weights/environment and three-arm/final acceptance remain. R134 installed; no actual training/model calls.'}
gaps['gaps']=[g for g in gaps['gaps'] if g['id']!='G110']+[entry];gaps['last_recorded_at']=time.time();gaps['complete']=False;write(R/'AUDIT_GAPS.json',gaps)
criteria={
 'PHASE-08':[('consumer requires separately pinned semantic-family inventory, all eight recorded strata, sparse-group limits and explicit retained exposure; synthetic gate acceptance is not corpus coverage', ['family_inventory_missing','one_of_eight_strata_missing','empty_stratum_cannot_claim_coverage','sparse_stratum_without_limit','retained_exposed_keys_cannot_be_fresh'])],
 'PHASE-09':[('actual optimizer CLI consumes full row/source/runtime admission before any model framework import; the current partially reviewed real corpus is rejected without a run directory', ['fully_pinned_control_check_only_admitted_without_optimizer','actual_partial_corpus_blocked_before_model_assets_or_frameworks','actual_cli_blocks_partial_corpus_before_framework_import','actual_partial_corpus_did_not_create_run_or_import_frameworks']),
             ('exact template/token prefix and full completion/generation limits are checked without truncation; changed base/runtime/protocol and post-admission errors remain distinct', ['exact_template_completion_prefix_and_labels_preserved','generation_cap_never_silently_truncated','sequence_cap_never_silently_truncated','bpe_prefix_mismatch','base_weight_bytes_changed','changed_runtime_contract_sha256','metrics_without_frozen_criteria','cli_distinguishes_post_admission_failure_from_rejected_data'])]}
t=read(R/'TRAINING_REQUIREMENT_REVIEWS.json');ledger=read(R/'COMPLETION_LEDGER.json');byid={x['id']:x for x in ledger['requirements']};e=reports['training_optimizer']
for row in t['requirements']:
 assert row['original_text']==byid[row['requirement_id']]['text'] and row['original_text_sha256']==byid[row['requirement_id']]['text_sha256']
 row['criteria']=[c for c in row['criteria'] if c.get('iteration')!='optimizer_and_labels']
 for text,checks in criteria.get(row['requirement_id'],[]):
  assert all(o['checks'][c] for c in checks)
  row['criteria'].append({'criterion':text,'state':'passed_controlled_acceptance','evidence':e['path'],'evidence_sha256':e['sha256'],'checks':checks,'iteration':'optimizer_and_labels','actual_optimization_proven':False,'semantic_accuracy_claimed':False})
t['reviewed_at']=time.time();t['no_new_training_or_model_inference']=True;write(R/'TRAINING_REQUIREMENT_REVIEWS.json',t)
for item in ledger['requirements']:
 assert hashlib.sha256(item['text'].encode()).hexdigest()==item['text_sha256']
 if item['id'] in entry['requirements']:
  item['gaps']=list(dict.fromkeys(item['gaps']+['G110']));item['implementation_evidence']=[x for x in item['implementation_evidence'] if x.get('gap')!='G110']+[{'gap':'G110','code':entry['candidate_code']}]
  item['acceptance_evidence']=[x for x in item['acceptance_evidence'] if x.get('path')!=e['path']]+[{**e,'scope':'specific guard controls only; actual optimization/semantic/final acceptance pending'}]
  item.update(implementation_state='candidate_consumer_present_real_training_and_final_acceptance_pending',behavior_acceptance_state='not_closed_open_gap')
assert len(ledger['requirements'])==76;write(R/'COMPLETION_LEDGER.json',ledger)
for name in ['FLOW_MAIN_TH.md','DATA_CONTRACTS_TH.md','IMPLEMENTATION_EVALUATION_TH.md']:assert (R/'spec'/name).read_bytes()==(R.parent/'r123_plan_distillation_architecture_20261023'/name).read_bytes()
rows=[]
for p in R.glob('*_REQUIREMENT_REVIEWS.json'):rows+=read(p)['requirements']
assert len(rows)==len({x['requirement_id'] for x in rows})==48
count=sum(c['state']=='passed_controlled_acceptance' for row in rows for c in row['criteria'])
paths=sorted((R/'system').rglob('*.py'))
for p in paths:ast.parse(p.read_text('utf-8-sig'),filename=str(p))
code=R/('COMPONENT_CODE_OBSERVATION_'+str(time.time_ns())+'.json');write(code,{'checked_at':time.time(),'python_files_ast_checked':len(paths),'current_candidate_python_sha256':{str(p.relative_to(R)):sha(p) for p in paths},'unfrozen_candidate_only':True,'final_acceptance_claimed':False})
obs=sorted(R.glob('SOURCE_PRESERVATION_OBSERVATION_*.json'))[-1];preserved=read(obs);assert not preserved['candidate_vs_live_differences'] and not preserved['candidate_vs_frozen_parent_differences'] and preserved['installed_health_observation']['ok'] is True
status=read(R/'STATUS.json');status.update(phase='complete_flow_audit_consumer_guard_and_individual_labels_in_progress',complete=False,whole_flow_complete=False,candidate_frozen=False,candidate_installed=False,active_installed_revision='R134',last_recorded_at=time.time(),requirement_specific_controlled_criteria_passed=count,last_source_preservation_observation=obs.name,latest_component_code_observation=code.name)
status['latest_training_review']={'workbench':str(W.relative_to(R)),'manual_round':str(manual.relative_to(R)),'summary':str((manual/'SUMMARY.json').relative_to(R)),'current_admission':str(A.relative_to(R)),**summary,'accepted':m['accepted'],'corrected_or_enriched':m['corrected_or_enriched'],'source_answer_issues_remain':m['source_answer_issues_remain'],'semantic_error_rate_claimed':False}
status['latest_training_gate_reports'].update(reports);status['latest_optimizer_and_manual_review_reports']=reports;status['last_identified_implementation_gaps']=['G110']
status['next_work']='Continue actual source-language reviews at original row155 onward (0-154 done155/289;134remain). Native history is the only admitted transform stage; real context/transformation corpus, semantic-family regroup/eight strata and frozen metric thresholds still pending. Consumer exists and guard controls pass; GPU loop/actual training/per-type semantic validation/three-arm evaluation remain unproven. Audit original28 unreviewed sections/all14 category final acceptance, G40 extra predicates and other gaps. Root/source750/R133459/R134delta or explicit R135 supersession, final330 exact successful same-request raw/source/model/assets/freeze/API plus actual-live SQLite full backup/normal activation/re-audit remain. Never rerun R132 questions/analyzer/baselines. Keep heartbeat; no subagents/model stop.'
write(R/'STATUS.json',status)
evidence=read(R/'ITERATION_01_EVIDENCE.json');evidence['recorded_at']=time.time();evidence['evidence']['optimizer_and_actual_labels']={'reports':reports,'manual_rounds':['review_round_007','review_round_008'],'latest_summary':str((manual/'SUMMARY.json').relative_to(R)),'current_admission':str(A.relative_to(R)),'actual_optimizer_started':False,'gpu_optimization_tested':False};write(R/'ITERATION_01_EVIDENCE.json',evidence)
header=f'''## Latest actual checkpoint — G110 guarded optimizer consumer; 155 individual saved-label source reviews

R135 remains unfrozen/uninstalled; R134 actually installed. {obs.name}: all candidate/frozen-parent/live logical SQLite tables inclWAL equal; health8115 common-r134-resolution-scope with unchanged db1685eafe9f1d95460614a0948792710c3462cdfac20b90beabd2f12d1ae157. PID commandlines37660chat/45088editor/42136model checked. No actual owner source/approvals/history/logs/frozenR132/R130/R131/model edits, no model/provider inference/training/restart/subagents. R121 retained context/base selector; failed adapter unpromoted; constrained decoder inactive. Model stop automatic-review denied twice blocked by policy: never bypass.

G110 prior code observation538 files had no optimizer consumer. New system/tools/train_reviewed_planner.py + domain_flow/training_optimizer.py first revalidate actual reviewed rows/source/runtime, then complete local base assets, separately recorded family/eight-strata/sparse limits and frozen three-arm metric/source/clock/locale/provider/budget/exposure/R121-weight protocol. Only afterward can tokenizer/framework/model load. Exact prefix/token/caps without truncation; fixed proven R129 LoRA config, train-only gradients/development-only loss selection, frozen base/adapter hashes/steps/environment intended for real run. Error states distinguish admission rejection from later failed/unknown weight updates. See OPTIMIZER_CONSUMER_TH.md. {reports['training_optimizer']['path']} passes{reports['training_optimizer']['checks']} bounded positive/negative/path/token/telemetry/CLI controls; synthetic model bytes NEVER loaded. Actual155/289 corpus is blocked before frameworks/run creation. GPU loop/gradients/actual training/per-type semantic metrics/three-arm/final proof are NOT established.

Manual rounds007/008 read actual original questions115-154, labels and pinned source fields, then store seven criterion-specific reasons/source record revisions+hashes/prior labels.155 individually adjudicated (52accepted/103corrected or enriched),134unreviewed; original0-154 done. Prior21/46/66/86/96/115/135 immutable. Scope fixes include machine2 versus persons2, controller platform versus offered-game platform/edition, actor/cause/negation/food carry-consume distinctions, literalR button, complete source titles and explicit shared-service/platform edges. Sourceunknown/missing actor coverage/partial Fortnite3binding set remain separate answer-source caveats; corrections are NOT a semantic error rate or business answers. Current {A.relative_to(R)}:155eligible train{summary['eligible_split_counts']['train']}/development{summary['eligible_split_counts']['development']}; noREADY/nooptimizer. RuntimeSHA {summary['current_runtime_contract_sha256']}; sourceSHA {summary['source_identity_sha256']}. Historical154train/17validation/110test unchanged; exposed old test stays development,93stale row.split tags retained.

Re-audit reports: consumer{reports['training_optimizer']['checks']}/admission43/import17/graph21/wire3. Original76 IDs/textSHA/14categories/spec3files preserved.48 individually reviewed requirements/{count} bounded controlled criteria; none finally closed/no Flow percentage. All{len(paths)} candidate Python AST checked/hashes {code.name}. G01-G110 not exhaustive. G108/G109 prior condition/raw-compound repairs retained; all prior tests/evidence remain. Use **checkpoint_optimizer_and_labels.py** now; older checkpoint scripts contain stale counts and must not run afterward. Repacker defaults008/importer expects155. Keep heartbeat.

Next: {status['next_work']}

## Historical checkpoints below — the new heading above supersedes old current-state statements

'''
p=R/'CURRENT_HANDOFF_TH.md';old=p.read_text('utf8');marker='## Historical checkpoints below — the new heading above supersedes old current-state statements\n\n';old=old.split(marker,1)[1] if marker in old else old;p.write_text(header+old,'utf8')
print(json.dumps({'gap_count':len(gaps['gaps']),'requirements':76,'individual_requirement_reviews':48,'controlled_criteria':count,'actual_label_reviews':155,'pending_labels':134,'candidate_python_ast':len(paths),'complete':False,'installed':'R134'}))
