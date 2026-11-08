"""C08/C09 source-specific checkpoint; no whole Flow closure."""
import json,hashlib,time
from pathlib import Path
R=Path(__file__).resolve().parent
def read(p):return json.loads(p.read_text('utf8'))
ledger=read(R/'COMPLETION_LEDGER.json');assert len(ledger['requirements'])==76
for r in ledger['requirements']:assert hashlib.sha256(r['text'].encode()).hexdigest()==r['text_sha256']
for n in ['FLOW_MAIN_TH.md','DATA_CONTRACTS_TH.md','IMPLEMENTATION_EVALUATION_TH.md']:assert (R/'spec'/n).read_bytes()==(R.parent/'r123_plan_distillation_architecture_20261023'/n).read_bytes()
assert len(read(R/'AUDIT_GAPS.json')['gaps'])==92
reports={}
for prefix in ['booking_payment_matrix_','game_matrix_','core_verification_','source_guard_verification_','request_coverage_verification_','followup_verification_','authority_fields_chains_','authority_chains_','native_contract_verification_','graph_verification_','wire_compatibility_']:
 p=sorted(p for p in R.glob(prefix+'*/*') if p.name in {'RESULT.json','VERIFICATION.json'})[-1];d=read(p);assert d.get('all_passed',d.get('passed')),p
 reports[prefix.rstrip('_')]={'path':str(p.relative_to(R)),'checks':len(d['checks']),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
reviews=[read(R/p) for p in ['OWNER_REQUIREMENT_REVIEWS.json','REQUEST_REQUIREMENT_REVIEWS.json','EXECUTOR_REQUIREMENT_REVIEWS.json','CATEGORY_REQUIREMENT_REVIEWS.json']];rows=[r for v in reviews for r in v['requirements']];assert len(rows)==len({r['requirement_id'] for r in rows})
obs=sorted(R.glob('SOURCE_PRESERVATION_OBSERVATION_*.json'))[-1];o=read(obs);assert not o['candidate_vs_frozen_parent_differences'] and not o['candidate_vs_live_differences']
status=read(R/'STATUS.json');status.update(last_recorded_at=time.time(),last_component_repairs=['G'+str(n) for n in range(86,93)],requirement_specific_review_ids=[r['requirement_id'] for r in rows],requirement_specific_controlled_criteria_passed=sum(c['state']=='passed_controlled_acceptance' for r in rows for c in r['criteria']),category_review_pending_criteria=sum(c['state']=='review_required' for r in reviews[3]['requirements'] for c in r['criteria']),latest_booking_payment_reports=reports,last_source_preservation_observation=obs.name,candidate_frozen=False,candidate_installed=False,active_installed_revision='R134',complete=False,whole_flow_complete=False,requirement_closure_claimed=False,next_work='Continue C10/C13 individual action/actor/exception/dependency source reviews, C08/C09 composite authority/condition/actor/retained variants and source-date scopes, C04 roles/mode vocabulary/retained variants, C05 device/multiple-platform/physical span proof, G40 dependencies and original training/evaluation/root-source750 requirements. Final exact raw/source/model/freeze/API/activation re-audit pending; never rerun R132 sample/analyzer/baseline/regrade.')
(R/'STATUS.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n','utf8')
header=f'''## ล่าสุดจริง — C08/C09 action/actor/validity/procedure audit; G86–G92 component repaired

R135 working/unfrozen/uninstalled; R134 remains installed and healthy per {obs.name}. Candidate/frozenR134/actualinstalled every SQLite table including WAL equal. No actual user data/approval/history/log changes, frozen R132/R130/R131 changes, model inference/provider HTTP/retraining/restart/subagents. R121 retained context/base selector; failed adapter not promoted; constrained decoder inactive; model stop denied twice by automatic review, never bypass.

G86 valid wrong-payment scenario and studio/customer cancellation receipts were accepted with omitted planner target; policy_scope independently rederives source action/actor from actual question, requires declared FAQ/procedure scope locators and ignores forged delivered intent. G87 booking-time predicate overlapped generic paid booking/date; narrow action family + observer priorities. G88 typed generic refund action absent despite new owner source; registered bounded source refund predicate, retain exact payer/approval/conditions, do not turn refund into credit or infer deadline; specific overpayment stays separate. G89 Common payer facet mismatch/duplicate observation repaired. G90 explicit wrong-date booking plus can I change it no longer treated as unnamed game/machine. G91 expired source cannot establish current policy; unknown interval is partial recorded clause with explicit validity notice; actual reference/date/revision independently checked and unsupported multiple dates/year needs targeted input. G92 known procedure steps did not prove known preconditions; preserve order/documents/deadline/outcome, unknown qualifiers remain partial with explicit missing fields, verifier rejects forged completeness.

Original baseline booking_payment_matrix_1793034390210229400, expiry/unknown validity baseline1793034847119716400, unknown procedure baseline1793034991934989900; DETAILS.json and failed reports retained. Required source refs were initially missing on legacy compiler paths, caught by core/request regressions and fixed centrally in projection.add (not loosening verifier). Fixture procedure steps initially omitted required contact_id:null; that was a test fixture correction, not a runtime implementation bug. Read-only controls compare every isolated source table before/after answering. No actual booking transaction is added.

Latest source-specific reports:
{chr(10).join('- '+n+': '+v['path']+' ('+str(v['checks'])+' checks)' for n,v in reports.items())}

Original76 IDs/text/SHA/spec3files preserved. Individual reviews {len(rows)}, controlled criteria {status['requirement_specific_controlled_criteria_passed']}; category criteria still pending{status['category_review_pending_criteria']}. **No requirement closed/no Flow percentage/no whole semantic accuracy claim.** G01–G92 not exhaustive; G40 broader dependencies still open. Recorder chain record_audit_iteration.py → record_executor_requirement_reviews.py → record_category_requirement_reviews.py → checkpoint_booking_payment.py. Older checkpoints assert85/78/etc and overwrite latest status; do not run them.

Continue C10/C13 finite actual action/actor/exception/dependency source review; C08/C09 composite authority/conditions/actors and actual retained variants/date scopes, C04 player roles/mode synonyms/retained sources, C05 input-device/multiple-platform/physical-subset provenance/retained layouts, G40 and original teacher-label/family-split/training/evaluation requirements. Root/source750 changed QA + R133459/R134delta or explicit supersession and final R135 exact successful same-request messages/schema/profile/adapter/stage/precision/cap330 source replay/assets/actual identity/freeze/API still pending. R132 sample/analyzer already complete2111/5584: never rerun questions/baseline/regrade/Full20554. Activate only proven whole candidate via normal entrypoints + fresh actual installed live SQLite backup all tables then re-audit. Do not delete heartbeat or finish at bounded tests.

## Previous C04 checkpoint

'''
p=R/'CURRENT_HANDOFF_TH.md';p.write_text(header+p.read_text('utf8'),'utf8')
print(json.dumps({'preserved_requirements':76,'individually_reviewed':len(rows),'controlled_criteria':status['requirement_specific_controlled_criteria_passed'],'complete':False}))
