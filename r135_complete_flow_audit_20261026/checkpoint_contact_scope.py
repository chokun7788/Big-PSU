"""Current C01 checkpoint preserving all original requirements and open work."""
import json,hashlib,time
from pathlib import Path
R=Path(__file__).resolve().parent
def read(p):return json.loads(p.read_text('utf8'))
ledger=read(R/'COMPLETION_LEDGER.json');assert len(ledger['requirements'])==76
for r in ledger['requirements']:assert hashlib.sha256(r['text'].encode()).hexdigest()==r['text_sha256']
for n in ['FLOW_MAIN_TH.md','DATA_CONTRACTS_TH.md','IMPLEMENTATION_EVALUATION_TH.md']:assert (R/'spec'/n).read_bytes()==(R.parent/'r123_plan_distillation_architecture_20261023'/n).read_bytes()
gaps=read(R/'AUDIT_GAPS.json');assert len(gaps['gaps'])==59
reports={}
for prefix in ['contact_matrix_','core_verification_','source_guard_verification_','followup_verification_','receipt_scope_verification_','graph_verification_','wire_compatibility_','gateway_verification_']:
 p=sorted(p for p in R.glob(prefix+'*/*') if p.name in {'RESULT.json','VERIFICATION.json'})[-1];d=read(p);assert d.get('all_passed',d.get('passed')),p
 reports[prefix.rstrip('_')]={'path':str(p.relative_to(R)),'checks':len(d['checks']),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
reviews=[read(R/p) for p in ['OWNER_REQUIREMENT_REVIEWS.json','REQUEST_REQUIREMENT_REVIEWS.json','EXECUTOR_REQUIREMENT_REVIEWS.json','CATEGORY_REQUIREMENT_REVIEWS.json']];rows=[r for v in reviews for r in v['requirements']];assert len(rows)==len({r['requirement_id'] for r in rows})
obs=sorted(R.glob('SOURCE_PRESERVATION_OBSERVATION_*.json'))[-1];o=read(obs);assert not o['candidate_vs_frozen_parent_differences'] and not o['candidate_vs_live_differences']
status=read(R/'STATUS.json');status.update(last_recorded_at=time.time(),last_component_repairs=['G58','G59'],requirement_specific_review_ids=[r['requirement_id'] for r in rows],requirement_specific_controlled_criteria_passed=sum(c['state']=='passed_controlled_acceptance' for r in rows for c in r['criteria']),category_review_pending_criteria=sum(c['state']=='review_required' for r in reviews[3]['requirements'] for c in r['criteria']),latest_contact_scope_reports=reports,last_source_preservation_observation=obs.name,candidate_frozen=False,candidate_installed=False,active_installed_revision='R134',complete=False,whole_flow_complete=False,requirement_closure_claimed=False,next_work='Continue C03/C04/C05/C08-C10/C13 finite source-operation-field acceptance and G40 multi-service/implicit/combined conditions. Institution associations cannot be invented; actual news source remains absent. Composite authority/saved-source variants, original training/evaluation requirement reviews, root/source750 and final raw/source/model/freeze/API/activation re-audit remain pending.')
(R/'STATUS.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n','utf8')
header=f'''## ล่าสุดจริง — C01 institution/channel field audit; G58–G59 component repaired

R135 working/unfrozen/uninstalled; R134 installedจริง health8115 build common-r134-resolution-scope/sourceSHA db1685eafe9f1d95460614a0948792710c3462cdfac20b90beabd2f12d1ae157. PID/commandlines37660chat/45088editor/42136model12921ตรวจในturnนี้. {obs.name}: readonlyทุกSQLitetableรวมWAL candidate/frozenR134/actualinstalledเท่ากัน. ไม่sourceDB/userdata/approval/log/history/frozenR132/130/131/weightsedit ไม่modelinference/providerHTTP/retrain/restart/subagents. R121retainedcontext/base selectorเดิม; failednewadapterไม่promote; constraineddecodernotactive; modelkillautomaticreviewdenied2ครั้งห้ามเลี่ยง.

G58 diagnostic contact_matrix_1793023361239219800/DETAILS.json: explicitemailกลับมีphoneด้วย และmissingemailแทนด้วยphone; naturalCommonยังไม่มีtypedchanneloperation. ตอนนี้C01read/independentreceiptใช้actualsourcechannelทั้งvalue+officehours, channelfieldlocatorตามclaim, validwrongchannel/omittedlocatorไม่ผ่าน; naturalEnglish/ThaiCommonเข้าสู่typedoperationโดยไม่model. G59 diagnosticเดียวกัน: unknowninstitutionmapแทนด้วยcentermapsอื่น, omittargetvalidothermapreceiptผ่าน. ตอนนี้actualquestionbindinstitution/facilityเอง; unknown/withdrawnไม่borrowneighbor, genericหลายcenterclarify. ไม่มีrelationcenterในcontactschemaจึงไม่inventassociationจากชื่อคล้ายกัน.

C01ครบ10registeredfieldpositivecases +5sourcechanneltypes +unknown/withdrawn/wronginstitution/wrongchannel/missingvalue/missinglocatornegativecontrols. Actualretainedcontactมี1record ตรวจreadonlyexactvalue/sourceidentityแยก ไม่อ้างempiricalaccuracy. RegressionพบC01genericpolitetypoจากretainedsampleถูกnewscopewithheld; แก้genericlanguagebindingให้รับpolitevariantโดยไม่เปิดunknownnamedtarget. Rawfailedreportsคงเดิม. Initialfixturebuilding/floorbilingualผิดschema แก้fixtureเป็นstring ไม่ใช่runtimebug. Intermediatetestchallengeappendแล้วอ่านquestionผิดKeyErrorแก้harness ไม่แก้raw.

Latest reports:
{chr(10).join('- '+n+': '+v['path']+' ('+str(v['checks'])+' checks)' for n,v in reports.items())}

Original76ID/textSHA/spec3filesคงเดิม. Individualreview {len(rows)}requirements/{status['requirement_specific_controlled_criteria_passed']}controlledcriteria; categorypending{status['category_review_pending_criteria']}. **ไม่ปิดrequirementใด/ไม่คิด%Flow**. G01–G59; G40ยังopenmulti-service/implicitroles/combinedconditions. Latestrecorder record_audit_iteration.py → record_executor_requirement_reviews.py → record_category_requirement_reviews.py → checkpoint_contact_scope.py. Oldercheckpointassert54/57หรือทับlateststatusอย่ารัน.

ทำต่อC03/C04/C05/C08–C10/C13และG40; compositeauthority/actualsavedvariants+originaltraining/distillation/label/familysplit/metricrequirementsยังauditinprogress. C14actualnewsยังไม่มี ไม่สร้างข่าว/approval. R132sample/analyzerครบ2111/5584แล้วห้ามrerun/baselineinference/regrade/Full20554. ยังroot/source750changedcases+R133459/R134delta reviewหรือexplicitsupersession, finalR135exactsuccessfulrequest/messages/schema/profile/adapter/stage/precision/cap paired330ไม่มีnewcontextinference, source/input/modelassets/freeze/API. Activateเฉพาะพิสูจน์ครบผ่านnormalentrypointพร้อมfreshactualinstalledliveSQLitebackupทุกtableแล้วreaudit. ห้ามลบheartbeat/declarecompleteจากboundedtests. เดินaudit→repair→test→reauditต่อไม่ถามซ้ำ/ไม่ใช้subagents.

## ประวัติก่อน C01 audit

'''
p=R/'CURRENT_HANDOFF_TH.md';p.write_text(header+p.read_text('utf8'),'utf8');print(json.dumps({'preserved_requirements':76,'individually_reviewed':len(rows),'controlled_criteria':status['requirement_specific_controlled_criteria_passed'],'complete':False}))
