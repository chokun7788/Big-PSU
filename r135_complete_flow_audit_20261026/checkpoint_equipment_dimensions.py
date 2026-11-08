"""C03 source-specific checkpoint without closing any original requirement."""
import json,hashlib,time
from pathlib import Path
R=Path(__file__).resolve().parent
def read(p):return json.loads(p.read_text('utf8'))
ledger=read(R/'COMPLETION_LEDGER.json');assert len(ledger['requirements'])==76
for r in ledger['requirements']:assert hashlib.sha256(r['text'].encode()).hexdigest()==r['text_sha256']
for n in ['FLOW_MAIN_TH.md','DATA_CONTRACTS_TH.md','IMPLEMENTATION_EVALUATION_TH.md']:assert (R/'spec'/n).read_bytes()==(R.parent/'r123_plan_distillation_architecture_20261023'/n).read_bytes()
gaps=read(R/'AUDIT_GAPS.json');assert len(gaps['gaps'])==65
reports={}
for prefix in ['equipment_dimensions_','core_verification_','source_guard_verification_','quantity_roles_','receipt_scope_verification_','graph_verification_','wire_compatibility_','set_operations_']:
 p=sorted(p for p in R.glob(prefix+'*/*') if p.name in {'RESULT.json','VERIFICATION.json'})[-1];d=read(p);assert d.get('all_passed',d.get('passed')),p
 reports[prefix.rstrip('_')]={'path':str(p.relative_to(R)),'checks':len(d['checks']),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
assert len(read(R/reports['equipment_dimensions']['path'])['registered_operation_field_pairs'])==16
reviews=[read(R/p) for p in ['OWNER_REQUIREMENT_REVIEWS.json','REQUEST_REQUIREMENT_REVIEWS.json','EXECUTOR_REQUIREMENT_REVIEWS.json','CATEGORY_REQUIREMENT_REVIEWS.json']];rows=[r for v in reviews for r in v['requirements']];assert len(rows)==len({r['requirement_id'] for r in rows})
obs=sorted(R.glob('SOURCE_PRESERVATION_OBSERVATION_*.json'))[-1];o=read(obs);assert not o['candidate_vs_frozen_parent_differences'] and not o['candidate_vs_live_differences']
status=read(R/'STATUS.json');status.update(last_recorded_at=time.time(),last_component_repairs=['G60','G61','G62','G63','G64','G65'],requirement_specific_review_ids=[r['requirement_id'] for r in rows],requirement_specific_controlled_criteria_passed=sum(c['state']=='passed_controlled_acceptance' for r in rows for c in r['criteria']),category_review_pending_criteria=sum(c['state']=='review_required' for r in reviews[3]['requirements'] for c in r['criteria']),latest_equipment_dimension_reports=reports,last_source_preservation_observation=obs.name,candidate_frozen=False,candidate_installed=False,active_installed_revision='R134',complete=False,whole_flow_complete=False,requirement_closure_claimed=False,next_work='Continue actual C03 platform/inventory/spec variants and finite C04/C05/C08-C10/C13 acceptance, G40 multi-service/implicit/combined conditions, composite authority/saved-source variants, original training/evaluation individual reviews, root/source750 and final exact raw/source/model/freeze/API/activation re-audit. No new context inference or sample/analyzer reruns.')
(R/'STATUS.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n','utf8')
header=f'''## ล่าสุดจริง — C03 source dimensions/inventory audit; G60–G65 component repaired

R135 working/unfrozen/uninstalled; R134 installedจริง health8115 build common-r134-resolution-scope/sourceSHA db1685eafe9f1d95460614a0948792710c3462cdfac20b90beabd2f12d1ae157. PID/commandlines37660chat/45088editor/42136model12921ตรวจในturnนี้. {obs.name}: readonlyทุกSQLitetableรวมWAL candidate/frozenR134/actualinstalledเท่ากัน. ไม่sourceDB/userdata/approval/log/history/frozenR132/130/131/weightsedit ไม่modelinference/providerHTTP/retrain/restart/subagents. R121retainedcontext/base selectorเดิม; failednewadapterไม่promote; constraineddecodernotactive; modelkillautomaticreviewdenied2ครั้งห้ามเลี่ยง.

G60 sourceownerเพิ่มcontrollersspecแล้วregisteredfieldยังอ่านไม่ได้; projectionตอนนี้มีsourceentry+unit ไม่inferจากquantity. G61 duplicatequantityspecขัดกันเดิมเลือกfirstvalue; ตอนนี้withholdambiguousderivedfieldและverifierตรวจactualuniqueentry. G62 receiptเดิมไม่ตรวจclaimfacetเทียบactualfactfacet ทำให้quantityrelabelเป็นcontrollersได้; ตอนนี้independentfacetidentitycheckทุกtypedclaim. Baseline equipment_dimensions_1793023999447548200/DETAILS.json.

G63 omittargetทำให้validothermachinequantityreceiptผ่าน; baseline equipment_dimensions_1793024254349283000/DETAILS.json. Independentactualquestionbindingเพิ่มสำหรับC03scalar/count. RegressionแรกbindGPU/การ์ดจอเป็นจอจนcore13GPUsผิด (core_verification_1793024288948551300); แก้ให้receiptใช้existingcomponent-awarebindingที่ลบcomponentpredicateก่อนentitybinding. Core54ผ่านหลังแก้ ไม่แก้rawpriorresult.

G64 named-zoneinventoryreaderกับverifierคนละscope (verifierอ่านเฉพาะplatform) ทำให้exactsetยังpartial; unknownzoneยังfallbackallinventory. Baseline equipment_dimensions_1793024331408081400/DETAILS.json และequipment_dimensions_1793024443359576900/DETAILS.json. ตอนนี้ใช้sourceinventoryscopeเดียวกันแต่verifierrecomputeเอง, exactzone/alias/source-locationmatch, ambiguouslocationsไม่assignsinglezone, unknownzoneไม่borrowwholeinventory, forgedextra-membermetadataถูกreject. G65 totalcontrollersacrosszoneไม่ใช่per-machinebasis; EnglishCommoncountเดิมไม่เข้าtypedoperation. Baseline equipment_dimensions_1793024151181399200/DETAILS.json. Nativecountintent+sourceunitbasisตรวจแยกทั้งEnglish/Thai. Sourceunitแสดงตามsource ไม่เดาunit.

C03ครบ16registeredoperation-fieldpairsมีactualcontrolledsourcepositive (detail10/count5/list1), machines7/controllers2/seats9/resourceplayers4/service2–6ต่างกันจริง, specs/location/name/type/usage/zoneinventoryมีsourceexpectedvalue. Negativewrongdimension/relabel/wrongdevice/missingcontroller/duplicatequantity/wrongbasis/unknownzone/forgedinventorymembers. ไม่มีphysicalinventorycompleteness/semanticaccuracyclaim; actualretainedinventory/spec/platformvariantsยังต้องreview. Newprojectedsourcefacts/metadataอาจทำfinalsavedrawไม่exactmatch ต้องunassessed ไม่reusewrongrequestraw/ไม่ยิงcontextinferenceซ้ำ.

Latest reports:
{chr(10).join('- '+n+': '+v['path']+' ('+str(v['checks'])+' checks)' for n,v in reports.items())}

Original76ID/textSHA/spec3filesคงเดิม. Individualreview {len(rows)}requirements/{status['requirement_specific_controlled_criteria_passed']}controlledcriteria; categorypending{status['category_review_pending_criteria']}. **ไม่ปิดrequirementใด/ไม่คิด%Flow/ไม่จบงาน**. G01–G65; G40ยังopenmulti-service/implicitroles/combinedconditions. Latestrecorder record_audit_iteration.py → record_executor_requirement_reviews.py → record_category_requirement_reviews.py → checkpoint_equipment_dimensions.py. Oldercheckpointassert54/57/59หรือทับlateststatusอย่ารัน.

ทำต่อactualC03platform/spec/inventoryvariants, finiteC04/C05/C08–C10/C13และG40; compositeauthority/actualsavedvariants+originaltraining/distillation/label/familysplit/metricrequirementsยังauditinprogress. C14actualnewsยังไม่มี ไม่สร้างข่าว/approval. R132sample/analyzerครบ2111/5584แล้วห้ามrerun/baselineinference/regrade/Full20554. ยังroot/source750changedcases+R133459/R134delta reviewหรือexplicitsupersession, finalR135exactsuccessfulrequest/messages/schema/profile/adapter/stage/precision/cap paired330ไม่มีnewcontextinference, source/input/modelassets/freeze/API. Activateเฉพาะพิสูจน์ครบผ่านnormalentrypointพร้อมfreshactualinstalledliveSQLitebackupทุกtableแล้วreaudit. ห้ามลบheartbeat/declarecompleteจากboundedtests. เดินaudit→repair→test→reauditต่อไม่ถามซ้ำ/ไม่ใช้subagents.

## ประวัติก่อน C03 audit

'''
p=R/'CURRENT_HANDOFF_TH.md';p.write_text(header+p.read_text('utf8'),'utf8');print(json.dumps({'preserved_requirements':76,'individually_reviewed':len(rows),'controlled_criteria':status['requirement_specific_controlled_criteria_passed'],'complete':False}))
