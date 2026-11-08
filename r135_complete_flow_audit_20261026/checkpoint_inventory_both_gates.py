"""Retained inventory and both-price dependency checkpoint; whole audit remains open."""
import json,hashlib,time
from pathlib import Path
R=Path(__file__).resolve().parent
def read(p):return json.loads(p.read_text('utf8'))
ledger=read(R/'COMPLETION_LEDGER.json');assert len(ledger['requirements'])==76
for r in ledger['requirements']:assert hashlib.sha256(r['text'].encode()).hexdigest()==r['text_sha256']
for n in ['FLOW_MAIN_TH.md','DATA_CONTRACTS_TH.md','IMPLEMENTATION_EVALUATION_TH.md']:assert (R/'spec'/n).read_bytes()==(R.parent/'r123_plan_distillation_architecture_20261023'/n).read_bytes()
gaps=read(R/'AUDIT_GAPS.json');assert len(gaps['gaps'])==70
reports={}
for prefix in ['retained_inventory_','both_price_dependencies_','execution_dependencies_','execution_dependency_native_','calculated_dependencies_','boolean_dependencies_','mixed_billing_','price_currency_','core_verification_','source_guard_verification_','graph_verification_','wire_compatibility_','set_operations_']:
 p=sorted(p for p in R.glob(prefix+'*/*') if p.name in {'RESULT.json','VERIFICATION.json'})[-1];d=read(p);assert d.get('all_passed',d.get('passed')),p
 reports[prefix.rstrip('_')]={'path':str(p.relative_to(R)),'checks':len(d['checks']),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
reviews=[read(R/p) for p in ['OWNER_REQUIREMENT_REVIEWS.json','REQUEST_REQUIREMENT_REVIEWS.json','EXECUTOR_REQUIREMENT_REVIEWS.json','CATEGORY_REQUIREMENT_REVIEWS.json']];rows=[r for v in reviews for r in v['requirements']];assert len(rows)==len({r['requirement_id'] for r in rows})
obs=sorted(R.glob('SOURCE_PRESERVATION_OBSERVATION_*.json'))[-1];o=read(obs);assert not o['candidate_vs_frozen_parent_differences'] and not o['candidate_vs_live_differences']
status=read(R/'STATUS.json');status.update(last_recorded_at=time.time(),last_component_repairs=['G66','G67','G68','G69','G70'],requirement_specific_review_ids=[r['requirement_id'] for r in rows],requirement_specific_controlled_criteria_passed=sum(c['state']=='passed_controlled_acceptance' for r in rows for c in r['criteria']),category_review_pending_criteria=sum(c['state']=='review_required' for r in reviews[3]['requirements'] for c in r['criteria']),latest_inventory_both_gate_reports=reports,last_source_preservation_observation=obs.name,candidate_frozen=False,candidate_installed=False,active_installed_revision='R134',complete=False,whole_flow_complete=False,requirement_closure_claimed=False,next_work='Continue C04/C05/C08-C10/C13 finite source-operation-field acceptance and G40 remaining general multi-service/implicit roles/mixed predicates. Actual C03 remaining implicit scope variants, composite authority/saved-source variants, original training/evaluation individual reviews, root/source750 and final exact raw/source/model/freeze/API/activation re-audit remain pending. No sample/analyzer or baseline inference/regrade reruns.')
(R/'STATUS.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n','utf8')
header=f'''## ล่าสุดจริง — actual C03 inventory variants + explicit both-price G40 gate; G66–G70 component repaired

R135 working/unfrozen/uninstalled; R134 installedจริง health8115 build common-r134-resolution-scope/sourceSHA db1685eafe9f1d95460614a0948792710c3462cdfac20b90beabd2f12d1ae157. PID/commandlines37660chat/45088editor/42136model12921ตรวจในturnนี้. {obs.name}: readonlyทุกSQLitetableรวมWAL candidate/frozenR134/actualinstalledเท่ากัน. ไม่sourceDB/userdata/approval/log/history/frozenR132/130/131/weightsedit ไม่modelinference/providerHTTP/retrain/restart/subagents. R121retainedcontext/base selectorเดิม; failednewadapterไม่promote; constraineddecodernotactive; modelkillautomaticreviewdenied2ครั้งห้ามเลี่ยง.

G66 actualretainedPlayStationmodel location='PlayStation 5 Zone / VR Zone' เดิมหายจากbothzoneinventory; G67 PS5aliasหาsourcePlayStation5Zoneไม่เจอแล้วคืนwholeinventory. Baseline retained_inventory_1793024849944680600/DETAILS.json. ตอนนี้literalcompoundทุกtokenต้องexactuniqueactualzone/title/alias, unknowncomponentไม่ยืนยันjoin; platformaliasเทียบsemanticlabelของsourcezoneเอง. Independentcollectionproofเก็บactualspec+zonename refs/revisionsทั้งสองฝั่ง ไม่ใช้metadataเป็นauthority. ตรวจreadonly16actualequipmentmodels/5zones/13knownquantityliteralfieldsครบ; rawquantityเช่น2UnitsPS5+1UnitVRคงqualifierไม่รวมเอง. ไม่ใช่physicalinventorycompleteness/sample-regrade/empiricalaccuracy.

G68 CommonnaturalEnglishlistเดิมคืนnamesผ่านboundedcompatibilityแต่ไม่ใช่registeredlist/setcontract (retained_inventory_1793025016306738300). ตอนนี้explicitinventoryintentเข้าtypedlistโดยแยกpermission/bring/rentalpredicates; actualCommonVRlistมีPS5model+VR2และlistcontractจริง ไม่มีmodel/providerHTTP.

G69 both-priceconditionเดิมไม่เป็นdependency: If both unit prices are below150THBยังreadbookingแม้price100/200มีตัวหนึ่งfalse หรืออีกpriceunknown. Baseline both_price_dependencies_1793025278075586500/DETAILS.json. ตอนนี้explicitbothquantifierมีtwoearlierpriceedges, recomputeeachdistinctsourceprerequisiteจากactualreceipts, alltrueก่อนdispatch; onefalse/bothfalse/unknown/ambiguous3prices/unsupportedaffordable/wrongtotal-unitwithheld. Thai/English+integration/Commonparentbridgeผ่านcontrolledproposals; privateproofrecompute, removeedge/forgedsecondthresholdไม่ผ่าน. Controlledproposalacceptanceไม่ใช่modelsemanticaccuracy. G40ยัง**open**general multi-service/implicitroles/mixedpredicates/othercombinedconditions และfinalacceptance; ไม่อ้างครบทุกcondition.

G70 sourcecurrencyfixคงdurationเมื่อamountunknown ทำให้G41variantข้ามknownservice/missingrateเพราะpoolไม่emptyแล้วเหลือtyped_interpretation_unresolved (execution_dependencies_1793025425862070900). ตอนนี้ถามamountของuniqueboundserviceที่มีแต่durationคือmissing_source/rate_not_recorded_for_bound_service ไม่ถามserviceซ้ำ. Executiondependencies34และcurrency12ผ่านหลังแก้; nonpricedurationยังอ่านได้.

Latest reports:
{chr(10).join('- '+n+': '+v['path']+' ('+str(v['checks'])+' checks)' for n,v in reports.items())}

Original76ID/textSHA/spec3filesคงเดิม. Individualreview {len(rows)}requirements/{status['requirement_specific_controlled_criteria_passed']}controlledcriteria; categorypending{status['category_review_pending_criteria']}. **ไม่ปิดrequirementใด/ไม่คิด%Flow/ไม่จบงาน**. G01–G70; G40ยังopen. Latestrecorder record_audit_iteration.py → record_executor_requirement_reviews.py → record_category_requirement_reviews.py → checkpoint_inventory_both_gates.py. Oldercheckpointsassert65/59/57/54หรือทับlateststatusอย่ารัน.

ทำต่อfiniteC04/C05/C08–C10/C13และG40general multi-service/implicitroles/mixedpredicates; actualC03implicit-scopevariants, compositeauthority/actualsavedvariants+originaltraining/distillation/label/familysplit/metricrequirementsยังauditinprogress. C14actualnewsยังไม่มี ไม่สร้างข่าว/approval. R132sample/analyzerครบ2111/5584แล้วห้ามrerun/baselineinference/regrade/Full20554. ยังroot/source750changedcases+R133459/R134delta reviewหรือexplicitsupersession, finalR135exactsuccessfulrequest/messages/schema/profile/adapter/stage/precision/cap paired330ไม่มีnewcontextinference, source/input/modelassets/freeze/API. Activateเฉพาะพิสูจน์ครบผ่านnormalentrypointพร้อมfreshactualinstalledliveSQLitebackupทุกtableแล้วreaudit. ห้ามลบheartbeat/declarecompleteจากboundedtests. เดินaudit→repair→test→reauditต่อไม่ถามซ้ำ/ไม่ใช้subagents.

## ประวัติก่อน actual inventory / both-price gates

'''
p=R/'CURRENT_HANDOFF_TH.md';p.write_text(header+p.read_text('utf8'),'utf8');print(json.dumps({'preserved_requirements':76,'individually_reviewed':len(rows),'controlled_criteria':status['requirement_specific_controlled_criteria_passed'],'complete':False}))
