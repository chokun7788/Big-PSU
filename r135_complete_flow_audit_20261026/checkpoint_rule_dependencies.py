"""C13 source-closure checkpoint. No claim of whole Flow completion."""
import json,hashlib,time
from pathlib import Path
R=Path(__file__).resolve().parent
def read(p):return json.loads(p.read_text('utf8'))
ledger=read(R/'COMPLETION_LEDGER.json');assert len(ledger['requirements'])==76
for r in ledger['requirements']:assert hashlib.sha256(r['text'].encode()).hexdigest()==r['text_sha256']
for n in ['FLOW_MAIN_TH.md','DATA_CONTRACTS_TH.md','IMPLEMENTATION_EVALUATION_TH.md']:assert (R/'spec'/n).read_bytes()==(R.parent/'r123_plan_distillation_architecture_20261023'/n).read_bytes()
assert len(read(R/'AUDIT_GAPS.json')['gaps'])==101
reports={}
for prefix in ['rule_dependency_proofs_','competition_relations_','core_verification_','source_guard_verification_','followup_verification_','set_operations_','native_contract_verification_','graph_verification_','wire_compatibility_']:
 p=sorted(p for p in R.glob(prefix+'*/*') if p.name in {'RESULT.json','VERIFICATION.json'})[-1];d=read(p);assert d.get('all_passed',d.get('passed')),p
 reports[prefix.rstrip('_')]={'path':str(p.relative_to(R)),'checks':len(d['checks']),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
reviews=[read(R/p) for p in ['OWNER_REQUIREMENT_REVIEWS.json','REQUEST_REQUIREMENT_REVIEWS.json','EXECUTOR_REQUIREMENT_REVIEWS.json','CATEGORY_REQUIREMENT_REVIEWS.json']];rows=[r for v in reviews for r in v['requirements']];assert len(rows)==len({r['requirement_id'] for r in rows})
assert len(reviews[3]['requirements'])==14
obs=sorted(R.glob('SOURCE_PRESERVATION_OBSERVATION_*.json'))[-1];o=read(obs);assert not o['candidate_vs_frozen_parent_differences'] and not o['candidate_vs_live_differences']
status=read(R/'STATUS.json');status.update(last_recorded_at=time.time(),last_component_repairs=['G99','G100','G101'],requirement_specific_review_ids=[r['requirement_id'] for r in rows],requirement_specific_controlled_criteria_passed=sum(c['state']=='passed_controlled_acceptance' for r in rows for c in r['criteria']),category_review_pending_criteria=sum(c['state']=='review_required' for r in reviews[3]['requirements'] for c in r['criteria']),latest_rule_dependency_reports=reports,last_source_preservation_observation=obs.name,candidate_frozen=False,candidate_installed=False,active_installed_revision='R134',complete=False,whole_flow_complete=False,requirement_closure_claimed=False,next_work='Audit remaining original requirements individually, especially teacher-label/source-revision review, family splits/training/evaluation and metrics. Fourteen category source reviews exist but every final acceptance remains open. Continue G40, composite authority/actor/conditions, actual retained source gaps, C04 modes/roles, C05 device/platform/physical spans and C10 cause/list scopes; root/source750 and final exact raw/source/model/freeze/API/activation re-audit pending. Never rerun R132 sample/analyzer/baseline/regrade.')
(R/'STATUS.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n','utf8')
header=f'''## ล่าสุดจริง — C13 transitive dependency receipts; G99–G101 repaired as components

R135 working/unfrozen/uninstalled; R134 remains installed/healthy per {obs.name}; every candidate/frozenR134/actualinstalled SQLite table incl WAL equal. No user data/approval/log/history/frozen R132/R130/R131/model assets edits, no inference/provider HTTP/retraining/restart/subagents. R121 retained context/base selector; failed new adapter not promoted; constrained decoder inactive; model stop automatic review denied twice, never bypass.

G99 rule reader already traversed dependencies but final verifier accepted removal of direct/downstream clause. New rule_dependencies independently rederives requested lookup/list/compare selection + actual same-event/game closure, required/delivered nodes/revisions/missing/cycles and metadata. G100 actual dependency/completeness/event locators could be omitted; all scope locators mandatory and source event/game/edition refs appended after actual index scope resolution, including legacy FAQ mappings. G101 unknown dependency set was assumed empty; known text now partial with plain-language source limit, not full clause acceptance. Baseline rule_dependency_proofs_1793036049698403300/DETAILS.json preserved. Initial fixture used non-enum facet staff; corrected to schema game_specific, not a runtime bug.

Actual retained sections018/045/046/050/053 read-only audit: kind competition_rule, both depends_on_ids and completeness status unknown/value null/empty evidence, not a new content regression. Existing followup exact source-ID/text assertions preserved, but strict status answer alone is no longer a correct expectation. verify_followup now allows partial only if exact required IDs/content remain, independently checked closure has no missing/errors/fatal, every limit is actual owner unknown field, and visible source notice exists. Earlier failed reports1793036215191499200 retained. No frozen raw/regrade/source field changed. Do not mark source dependencies known just to make tests pass.

Latest reports:
{chr(10).join('- '+n+': '+v['path']+' ('+str(v['checks'])+' checks)' for n,v in reports.items())}

Original76 IDs/text/SHA/spec3files unchanged. Individual reviews {len(rows)}, controlled criteria {status['requirement_specific_controlled_criteria_passed']}; all14 categories now have clause-specific component reviews, all14 still retain final pending criteria. **No requirement closed/no Flow percentage/no whole semantic accuracy claim.** G01–G101 not exhaustive; G40 broader predicates open. Recorder chain record_audit_iteration.py → record_executor_requirement_reviews.py → record_category_requirement_reviews.py → checkpoint_rule_dependencies.py. Older checkpoints assert98/92/etc and overwrite latest state; do not run.

Next audit remaining original requirements individually, especially source-matched teacher-label review, family split/training/evaluation/metrics; generic existing tracker is not proof. Also G40 general dependencies, composite authority/actor/condition/exception/cause bindings, actual retained source variants, C04 player-role/mode vocabulary, C05 device/multiple-platform/physical-subset raw spans, C10 mixed-validity lists and cause scopes. Source-unknown clauses remain source gaps, not automatically implementation failures. FAQ-to-event alias resolution still separate from attested typed relation and arbitrary prose entailment.

Still root/source750 changed QA + R133459/R134delta review or explicit supersession; final R135 exact successful same-request messages/schema/profile/adapter/stage/precision/cap330 raw/source replay/assets/actual identity/freeze/API. R132 sample/analyzer complete2111/5584: never rerun questions/baseline/regrade/Full20554. Activate only proven whole candidate through normal entrypoints + fresh actual installed live SQLite backup every table then re-audit. Keep heartbeat and continue all76, not just bounded tests.

## Previous C10 checkpoint

'''
p=R/'CURRENT_HANDOFF_TH.md';p.write_text(header+p.read_text('utf8'),'utf8')
print(json.dumps({'preserved_requirements':76,'individually_reviewed':len(rows),'controlled_criteria':status['requirement_specific_controlled_criteria_passed'],'complete':False}))
