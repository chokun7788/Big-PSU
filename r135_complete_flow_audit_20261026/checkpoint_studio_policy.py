"""C10 checkpoint preserving original requirements and unresolved whole task."""
import json,hashlib,time
from pathlib import Path
R=Path(__file__).resolve().parent
def read(p):return json.loads(p.read_text('utf8'))
ledger=read(R/'COMPLETION_LEDGER.json');assert len(ledger['requirements'])==76
for r in ledger['requirements']:assert hashlib.sha256(r['text'].encode()).hexdigest()==r['text_sha256']
for n in ['FLOW_MAIN_TH.md','DATA_CONTRACTS_TH.md','IMPLEMENTATION_EVALUATION_TH.md']:assert (R/'spec'/n).read_bytes()==(R.parent/'r123_plan_distillation_architecture_20261023'/n).read_bytes()
assert len(read(R/'AUDIT_GAPS.json')['gaps'])==98
reports={}
for prefix in ['studio_policy_matrix_','booking_payment_matrix_','core_verification_','source_guard_verification_','set_operations_','native_contract_verification_','graph_verification_','wire_compatibility_']:
 p=sorted(p for p in R.glob(prefix+'*/*') if p.name in {'RESULT.json','VERIFICATION.json'})[-1];d=read(p);assert d.get('all_passed',d.get('passed')),p
 reports[prefix.rstrip('_')]={'path':str(p.relative_to(R)),'checks':len(d['checks']),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
reviews=[read(R/p) for p in ['OWNER_REQUIREMENT_REVIEWS.json','REQUEST_REQUIREMENT_REVIEWS.json','EXECUTOR_REQUIREMENT_REVIEWS.json','CATEGORY_REQUIREMENT_REVIEWS.json']];rows=[r for v in reviews for r in v['requirements']];assert len(rows)==len({r['requirement_id'] for r in rows})
obs=sorted(R.glob('SOURCE_PRESERVATION_OBSERVATION_*.json'))[-1];o=read(obs);assert not o['candidate_vs_frozen_parent_differences'] and not o['candidate_vs_live_differences']
status=read(R/'STATUS.json');status.update(last_recorded_at=time.time(),last_component_repairs=['G'+str(n) for n in range(93,99)],requirement_specific_review_ids=[r['requirement_id'] for r in rows],requirement_specific_controlled_criteria_passed=sum(c['state']=='passed_controlled_acceptance' for r in rows for c in r['criteria']),category_review_pending_criteria=sum(c['state']=='review_required' for r in reviews[3]['requirements'] for c in r['criteria']),latest_studio_policy_reports=reports,last_source_preservation_observation=obs.name,candidate_frozen=False,candidate_installed=False,active_installed_revision='R134',complete=False,whole_flow_complete=False,requirement_closure_claimed=False,next_work='Continue C13 individual event/game/edition/clause/dependency/source comparison audit, C10 same-action cause/actor/condition/exception bindings and mixed-validity list controls, C08/C09 composite authority/retained/date variants, C04 roles/modes/retained variants, C05 device/platform/physical spans, G40 and original teacher-label/family-split/training/evaluation/root-source750 requirements. Final exact raw/source/model/freeze/API/activation re-audit pending. Never rerun R132 sample/analyzer/baseline/regrade.')
(R/'STATUS.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n','utf8')
header=f'''## ล่าสุดจริง — C10 studio-policy source audit; G93–G98 repaired as components

R135 working/unfrozen/uninstalled; R134 remains installed and healthy per {obs.name}, every candidate/frozenR134/actualinstalled SQLite table incl WAL equal. No user data/approval/log/history/frozen R132/R130/R131/model assets modified; no model inference/provider HTTP/retrain/restart/subagents. R121 retained context/base selector; failed new adapter not promoted; constrained decoder inactive. Model stop denied twice by automatic review; never bypass.

C10 original text individually reviewed using actual owner policy saves in isolated SQLite. G93 new owner food-bring/personal-power did not work through normal Common; bounded source families registered, legacy shortcut no longer hides added owner variant without actual authority. G94 consumption receipt could prove bringing with omitted target/forged intent; actual question/source action + topic/subject/mapping refs rechecked independently. G95 installed version also matched install verb; separate predicates. G96 explicit not_applicable conditions were treated unknown; preserve owner status semantics. G97 expired C10 source permission rejected, unknown applicability limited and independent date/revision proofs retained. G98 condition/exception guard could be bypassed without canonical action; common finish path and verifier now reject incomplete permission claims, preserving independent known siblings with explicit partial source gap.

Baseline studio_policy_matrix_1793035547546458500/DETAILS.json; canonical-omission bypass baseline1793035761003953600. Failed reports retained. Controlled seventeen families include literal source actor/condition/exception clauses, not arbitrary prose entailment or actor-role computation. Not_applicable does not infer an unknown exception; lack of evidence does not authorize permission.

Latest reports:
{chr(10).join('- '+n+': '+v['path']+' ('+str(v['checks'])+' checks)' for n,v in reports.items())}

Original76 IDs/text/SHA/spec3files unchanged. Individual reviews {len(rows)}, controlled criteria {status['requirement_specific_controlled_criteria_passed']}, category pending criteria{status['category_review_pending_criteria']}; **no requirement closed/no Flow percentage/no whole semantic accuracy.** G01–G98 not exhaustive; G40 broader dependencies still open. Recorder chain record_audit_iteration.py → record_executor_requirement_reviews.py → record_category_requirement_reviews.py → checkpoint_studio_policy.py. Older checkpoints assert92/85/etc and overwrite latest state; do not run.

Next C13 event/game/edition/clause/dependency/compare source-specific individual review (last category without individual review), C10 same-action cause/actor/exception binding + mixed-validity lists, C08/C09 composite authority/conditions/actual retained variants/date scopes, C04 player roles/mode vocabulary/retained records, C05 device/multiple-platform/physical-subset raw span coverage, G40 and original teacher labels/family split/training/evaluation requirements. Root/source750 changed QA + R133459/R134delta or explicit supersession and final R135 exact successful same-request messages/schema/profile/adapter/stage/precision/cap330 raw/source replay/assets/actual identity/freeze/API remain. R132 sample/analyzer complete2111/5584: never rerun questions/baseline/regrade/Full20554. Activate only proven whole candidate via normal entrypoints + fresh actual installed live SQLite backup every table then re-audit. Keep heartbeat; do not finish at component tests.

## Previous C08/C09 checkpoint

'''
p=R/'CURRENT_HANDOFF_TH.md';p.write_text(header+p.read_text('utf8'),'utf8')
print(json.dumps({'preserved_requirements':76,'individually_reviewed':len(rows),'controlled_criteria':status['requirement_specific_controlled_criteria_passed'],'complete':False}))
