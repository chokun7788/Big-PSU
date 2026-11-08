"""C04 component checkpoint; preserves every original requirement and open work."""
import json,hashlib,time
from pathlib import Path
R=Path(__file__).resolve().parent
def read(p):return json.loads(p.read_text('utf8'))
ledger=read(R/'COMPLETION_LEDGER.json');assert len(ledger['requirements'])==76
for r in ledger['requirements']:assert hashlib.sha256(r['text'].encode()).hexdigest()==r['text_sha256']
for n in ['FLOW_MAIN_TH.md','DATA_CONTRACTS_TH.md','IMPLEMENTATION_EVALUATION_TH.md']:assert (R/'spec'/n).read_bytes()==(R.parent/'r123_plan_distillation_architecture_20261023'/n).read_bytes()
gaps=read(R/'AUDIT_GAPS.json');assert len(gaps['gaps'])==85
reports={}
for prefix in ['game_matrix_','core_verification_','source_guard_verification_','receipt_scope_verification_','set_operations_','shared_relation_binding_','graph_verification_','wire_compatibility_']:
 p=sorted(p for p in R.glob(prefix+'*/*') if p.name in {'RESULT.json','VERIFICATION.json'})[-1];d=read(p);assert d.get('all_passed',d.get('passed')),p
 reports[prefix.rstrip('_')]={'path':str(p.relative_to(R)),'checks':len(d['checks']),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
reviews=[read(R/p) for p in ['OWNER_REQUIREMENT_REVIEWS.json','REQUEST_REQUIREMENT_REVIEWS.json','EXECUTOR_REQUIREMENT_REVIEWS.json','CATEGORY_REQUIREMENT_REVIEWS.json']];rows=[r for v in reviews for r in v['requirements']];assert len(rows)==len({r['requirement_id'] for r in rows})
obs=sorted(R.glob('SOURCE_PRESERVATION_OBSERVATION_*.json'))[-1];o=read(obs);assert not o['candidate_vs_frozen_parent_differences'] and not o['candidate_vs_live_differences']
status=read(R/'STATUS.json');status.update(last_recorded_at=time.time(),last_component_repairs=['G'+str(n) for n in range(79,86)],requirement_specific_review_ids=[r['requirement_id'] for r in rows],requirement_specific_controlled_criteria_passed=sum(c['state']=='passed_controlled_acceptance' for r in rows for c in r['criteria']),category_review_pending_criteria=sum(c['state']=='review_required' for r in reviews[3]['requirements'] for c in r['criteria']),latest_game_matrix_reports=reports,last_source_preservation_observation=obs.name,candidate_frozen=False,candidate_installed=False,active_installed_revision='R134',complete=False,whole_flow_complete=False,requirement_closure_claimed=False,next_work='Continue C08/C09/C10/C13 source-specific operation/condition/authority reviews, C04 additional player roles/mode synonyms/retained variants, C05 remaining input-device/multiple-platform/physical span controls, G40 dependencies, original training/evaluation and root/source750 review. Final exact raw/source/model/freeze/API/activation re-audit pending. Never rerun completed R132 sample/analyzer/baseline/regrade.')
(R/'STATUS.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n','utf8')
header=f'''## ล่าสุดจริง — C04 game/player/offering matrix; G79–G85 component repaired

R135 working/unfrozen/uninstalled; R134 remains installed, source/health confirmed in {obs.name}; every candidate/frozen-parent/live SQLite table including WAL is equal. No owner data/approvals/history/logs, frozen R132/R130/R131, model assets or installed lifecycle changed. No actual inference/provider HTTP/retraining/subagents. R121 retained context/base selector remains; failed adapter not promoted, constrained decoder inactive, model stop denied by automatic review twice and must not be bypassed.

C04 original text individually reviewed. G79 platform-scoped offered service/zone is independently recomputed from actual game→offered service→resource→zone and field refs; supported platform is not studio availability. G80 unknown minimum is not one, source mode range/platform/studio-supported predicates and locators preserved. G81 requested player subset no longer gets unfiltered catalog; Common English words/digits, Thai and mixed language checked. G82 final persons verifier uses source min≤count≤max, not equality to max. G83 generic zone list reads current recorded relation subset. G84 valid wrong-game receipt with omitted target rejected. G85 multiple/bounded/fractional counts do not silently become one exact count; unsupported roles/bounds explicitly need input. Diagnostic original game_matrix_1793032769038384800/DETAILS.json retained.

Owner already rejected wrong-reference-kind offers. Defensive invalid-memory snapshot test is not an owner-accepted source bug. Initial fixture schema mistakes (mode_name not bilingual, invalid reference target) were corrected as fixtures, not claimed runtime repairs. During integration, requested zone projection initially lacked zone-name source refs; renderer now adds actual recomputed path refs, verifier independently permits only those actual refs and checks exact metadata/value/path/revisions. Failed reports retained.

Latest reports:
{chr(10).join('- '+n+': '+v['path']+' ('+str(v['checks'])+' checks)' for n,v in reports.items())}

Original76 IDs/text/SHA/spec3files preserved. Individual reviews {len(rows)}, controlled criteria {status['requirement_specific_controlled_criteria_passed']}; **no requirement closed, no Flow percentage or whole semantic accuracy claimed**. G01–G85 not exhaustive, G40 still open beyond bounded implemented predicates. Current recorder chain record_audit_iteration.py → record_executor_requirement_reviews.py → record_category_requirement_reviews.py → checkpoint_game_matrix.py. Older checkpoints assert78/70/65/etc and can overwrite latest status; do not run.

Continue actual C08/C09/C10/C13 action/condition/authority/source-specific reviews, C04 player roles/mode synonyms/retained variants, C05 input-device/multiple-platform/raw physical-subset provenance/retained layouts, G40 general dependencies, and original teacher label/family split/training/evaluation requirements. Root/source750 changed QA + R133459/R134delta or explicit supersession and final R135 exact successful same-request wire330 source replay/assets/actual identity/freeze/API remain. R132 sample/analyzer already complete2111/5584; never rerun questions/baseline inference/regrade/Full20554. Activate only proven complete candidate with fresh actual installed live SQLite backup all tables, normal entrypoints and re-audit. Keep heartbeat until full authorized Flow complete.

## Previous C05 checkpoint

'''
p=R/'CURRENT_HANDOFF_TH.md';p.write_text(header+p.read_text('utf8'),'utf8')
print(json.dumps({'preserved_requirements':76,'individually_reviewed':len(rows),'controlled_criteria':status['requirement_specific_controlled_criteria_passed'],'complete':False}))
