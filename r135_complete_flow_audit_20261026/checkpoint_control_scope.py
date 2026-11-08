"""C05 source-scope checkpoint; full 76-requirement completion remains open."""
import json,hashlib,time
from pathlib import Path
R=Path(__file__).resolve().parent
def read(p):return json.loads(p.read_text('utf8'))
ledger=read(R/'COMPLETION_LEDGER.json');assert len(ledger['requirements'])==76
for r in ledger['requirements']:assert hashlib.sha256(r['text'].encode()).hexdigest()==r['text_sha256']
for n in ['FLOW_MAIN_TH.md','DATA_CONTRACTS_TH.md','IMPLEMENTATION_EVALUATION_TH.md']:assert (R/'spec'/n).read_bytes()==(R.parent/'r123_plan_distillation_architecture_20261023'/n).read_bytes()
gaps=read(R/'AUDIT_GAPS.json');assert len(gaps['gaps'])==78
reports={}
for prefix in ['control_scope_','core_verification_','source_guard_verification_','receipt_scope_verification_','projection_receipts_','collection_verification_','graph_verification_','wire_compatibility_']:
 p=sorted(p for p in R.glob(prefix+'*/*') if p.name in {'RESULT.json','VERIFICATION.json'})[-1];d=read(p);assert d.get('all_passed',d.get('passed')),p
 reports[prefix.rstrip('_')]={'path':str(p.relative_to(R)),'checks':len(d['checks']),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
reviews=[read(R/p) for p in ['OWNER_REQUIREMENT_REVIEWS.json','REQUEST_REQUIREMENT_REVIEWS.json','EXECUTOR_REQUIREMENT_REVIEWS.json','CATEGORY_REQUIREMENT_REVIEWS.json']];rows=[r for v in reviews for r in v['requirements']];assert len(rows)==len({r['requirement_id'] for r in rows})
obs=sorted(R.glob('SOURCE_PRESERVATION_OBSERVATION_*.json'))[-1];o=read(obs);assert not o['candidate_vs_frozen_parent_differences'] and not o['candidate_vs_live_differences']
status=read(R/'STATUS.json');status.update(last_recorded_at=time.time(),last_component_repairs=['G71','G72','G73','G74','G75','G76','G77','G78'],requirement_specific_review_ids=[r['requirement_id'] for r in rows],requirement_specific_controlled_criteria_passed=sum(c['state']=='passed_controlled_acceptance' for r in rows for c in r['criteria']),category_review_pending_criteria=sum(c['state']=='review_required' for r in reviews[3]['requirements'] for c in r['criteria']),latest_control_scope_reports=reports,last_source_preservation_observation=obs.name,candidate_frozen=False,candidate_installed=False,active_installed_revision='R134',complete=False,whole_flow_complete=False,requirement_closure_claimed=False,next_work='Continue C05 input-device/multiple-platform/raw physical-subset provenance and actual retained layout coverage, C04/C08-C10/C13 finite source-operation-field acceptance, G40 general multi-service/implicit roles/mixed conditions, authority/saved-source variants and original training/evaluation requirements. Root/source750 and final exact raw/source/model/freeze/API/activation re-audit remain pending; never rerun sample/analyzer/baseline inference/regrade.')
(R/'STATUS.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n','utf8')
header=f'''## ล่าสุดจริง — C05 source action/platform/gesture/physical subset audit; G71–G78 component repaired

R135 working/unfrozen/uninstalled; R134 installedจริง health8115 build common-r134-resolution-scope/sourceSHA db1685eafe9f1d95460614a0948792710c3462cdfac20b90beabd2f12d1ae157. PID/commandlines37660chat/45088editor/42136model12921ตรวจจริงในturnนี้. {obs.name}: readonlyทุกSQLitetableรวมWAL candidate/frozenR134/actualinstalledเท่ากัน. ไม่sourceDB/userdata/approval/log/history/frozenR132/130/131/weightsedit ไม่modelinference/providerHTTP/retrain/restart/subagents. R121retainedcontext/base selectorเดิม; failednewadapterไม่promote; constraineddecodernotactive; modelkillautomaticreviewdenied2ครั้งห้ามเลี่ยง.

G71 newownercontrol_setมีgame_idแต่gamealiasไม่เข้าดัชนี จึงbindgameไม่ได้ (control_scope_1793026124690434900/DETAILS.json). ตอนนี้typedgamejoin/aliasesพร้อมactualgame/platform/title refsและไม่ใช้wrongkindtarget. G72 projectionทิ้งgesture/context; G73 actionfamilyจับheavyattackจากJumpnoteเชิงปฏิเสธ; G75 validotherplatformreceiptเมื่อomittargetผ่าน; G76 validownerplatformPS5ถูกfilterหาsubstringplaystationจนไม่ตอบ. Baselineหลังแก้binding: control_scope_1793026203256908800/DETAILS.json. ตอนนี้purebindingprojectionเก็บgesture/context/notes/chord, actionmatchเฉพาะactualactionlabel, platformcanonicalsource scopeใช้ทั้งreaderและindependentreceipt. Verifierเทียบactualbindingrow/facet/value/game และactualscopefieldlocators.

G74 จำนวน3bindingentriesไม่ใช่3physicalbuttons และforgedcomplete_setเคยกลับเป็นsupported (control_scope_1793026598355698200/DETAILS.json). Rawcountที่ไม่ระบุkeyไม่เลือกsubsetเอง; explicitK,L1,R1พิสูจน์จากsourcebuttonsarraysว่ามี3keysแต่ต้อง2entries(KและL1+R1chord), independentverifier/collectionrecomputeทุกครั้ง. Sourcebuttoncountwordในknownentitynameถูกmaskก่อน; derivedcanonicalkeynamesไม่ใช่modelauthority. Subsetparsercasefoldregressionเมื่อlegacyreadernormquerylowercaseถูกจับระหว่างพัฒนาแล้วแก้เก็บcanonicalsourcekeys; failedrawreportsคงเดิม.

G77 listเดิมmergeคนละpresetที่samegame/platformและexplicitpresetไม่filter (control_scope_1793026598355698200). ตอนนี้recordlayoutsแยก, explicitactualpreset/versionเลือกเอง, unknown/ambiguousscopeไม่guess; sourcepreset/versionแสดง**หลังrequestedcontent**. G78 CommonWhichbuttonsชื่อnewactionกลายเป็นfulllayoutlistเพราะbuttonsplural (control_scope_1793031560247476700); ตอนนี้source-declaredactionใช้controloperation. Commonactualsourceactiontestไม่ได้modelproposal/inference.

C05มีindividualreviewตามoriginaltextแล้ว แต่ยังไม่close: controlledownerPC/PS5+presets+versions, hold/press/simultaneous/context+negative notes, action/reverse/allbindings/identifiedphysicalsubset/unidentifiedcount/forgedcompleteness/wrongplatform/requiredscope refs. Initialfixtureinput_devicekeyboardและbilingualpresetผิดschema แก้fixtureเป็นkeyboard_mouse/string ไม่ใช่runtimebug. PS5positiveเปลี่ยนจากmemorymutationเป็นactualowner-saveในisolatedDBเพื่อมีvalidsourceattestation. Actualretainedlayoutcoverage/inputdevice/multipleplatform/rawsubsetspanprovenanceและadditionalgesturevocabularyยังต้องaudit ไม่ใช่hardwarebuttoninventoryหรือempiricalaccuracyproof.

Latest reports:
{chr(10).join('- '+n+': '+v['path']+' ('+str(v['checks'])+' checks)' for n,v in reports.items())}

Original76ID/textSHA/spec3filesคงเดิม. Individualreview {len(rows)}requirements/{status['requirement_specific_controlled_criteria_passed']}controlledcriteria; categorypending{status['category_review_pending_criteria']}. **ไม่ปิดrequirementใด/ไม่คิด%Flow/ไม่จบงาน**. G01–G78; G40ยังopengeneral multi-service/implicitroles/mixedpredicates/finalacceptance. Latestrecorder record_audit_iteration.py → record_executor_requirement_reviews.py → record_category_requirement_reviews.py → checkpoint_control_scope.py. Oldercheckpointsassert70/65/59/57/54หรือทับlateststatusอย่ารัน.

ทำต่อC05ข้างต้น, finiteC04/C08–C10/C13, G40, compositeauthority/actualsavedvariants+originaltraining/distillation/label/familysplit/metricrequirementsยังauditinprogress. C14actualnewsยังไม่มี ไม่สร้างข่าว/approval. R132sample/analyzerครบ2111/5584แล้วห้ามrerun/baselineinference/regrade/Full20554. ยังroot/source750changedcases+R133459/R134delta reviewหรือexplicitsupersession, finalR135exactsuccessfulrequest/messages/schema/profile/adapter/stage/precision/cap paired330ไม่มีnewcontextinference, source/input/modelassets/freeze/API. NewC05projectedvalues/refsอาจทำcachedselectorrequestไม่ตรง ต้องunassessedไม่reusewrongraw. Activateเฉพาะพิสูจน์ครบผ่านnormalentrypointพร้อมfreshactualinstalledliveSQLitebackupทุกtableแล้วreaudit. ห้ามลบheartbeat/declarecompleteจากboundedtests. เดินaudit→repair→test→reauditต่อไม่ถามซ้ำ/ไม่ใช้subagents.

## ประวัติก่อน C05 source scope audit

'''
p=R/'CURRENT_HANDOFF_TH.md';p.write_text(header+p.read_text('utf8'),'utf8');print(json.dumps({'preserved_requirements':76,'individually_reviewed':len(rows),'controlled_criteria':status['requirement_specific_controlled_criteria_passed'],'complete':False}))
