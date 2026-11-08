"""Record current audit state without closing original requirements."""
import json,hashlib,time
from pathlib import Path
R=Path(__file__).resolve().parent
def read(p):return json.loads(p.read_text('utf8'))
ledger=read(R/'COMPLETION_LEDGER.json');assert len(ledger['requirements'])==76
for row in ledger['requirements']:assert hashlib.sha256(row['text'].encode()).hexdigest()==row['text_sha256'],row['id']
for name in ['FLOW_MAIN_TH.md','DATA_CONTRACTS_TH.md','IMPLEMENTATION_EVALUATION_TH.md']:assert (R/'spec'/name).read_bytes()==(R.parent/'r123_plan_distillation_architecture_20261023'/name).read_bytes()
reviews=[read(R/name) for name in ['OWNER_REQUIREMENT_REVIEWS.json','REQUEST_REQUIREMENT_REVIEWS.json','EXECUTOR_REQUIREMENT_REVIEWS.json'] if (R/name).exists()]
rows=[r for review in reviews for r in review['requirements']]
status=read(R/'STATUS.json');status.update(last_recorded_at=time.time(),last_component_repairs=['G31','G32','G33','G34','G35','G36','G37','G38','G39'],requirement_specific_review_ids=[r['requirement_id'] for r in rows],requirement_specific_controlled_criteria_passed=sum(c['state']=='passed_controlled_acceptance' for r in rows for c in r['criteria']),request_contract_review_pending_criteria=sum(c['state']=='review_required' for r in read(R/'REQUEST_REQUIREMENT_REVIEWS.json')['requirements'] for c in r['criteria']),executor_review_pending_criteria=sum(c['state']=='review_required' for r in read(R/'EXECUTOR_REQUIREMENT_REVIEWS.json')['requirements'] for c in r['criteria']) if (R/'EXECUTOR_REQUIREMENT_REVIEWS.json').exists() else None,last_source_preservation_observation=sorted(R.glob('SOURCE_PRESERVATION_OBSERVATION_*.json'))[-1].name,next_work='Implement G40 actual execution dependencies with source-positive/negative outcome controls; finish multi-step/field-scope authority controls, finite capability-pair acceptance, every original requirement/category/training/eval; final source/model/API/freeze/paired/root review/activation re-audits pending',whole_flow_complete=False,complete=False)
(R/'STATUS.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n','utf8')
header='''## ล่าสุดจริง — G31–G34: input derivation / numeric names / style / request isolation

R135ยังworking/unfrozen/uninstalled; R134installedจริง health8115 build common-r134-resolution-scope ณ SOURCE_PRESERVATION_OBSERVATION_1792995712708598900.json. SQLite readonly transaction ทุกtableรวมWAL candidate/frozenR134/actualinstalledR134เท่ากัน; ไม่แตะuserdata/approvals/logs. ไม่มีactualmodelinference/providercall/retrain/restart/subagents/duplicatebenchmarkในรอบนี้. ยังต้องfreshlivebackupตอนactivate ไม่ใช่freeze/assetproof.

G31พบrawgenre→execution summaryที่ไม่มีreceiptยังส่งsupportedclaims; fakeaudit tagก็ผ่าน (execution_derivation_1792993281555642700/DETAILS.json). input_derivation.py require exact raw/normalizeหรือregistered recomputation ที่ผูกrawSHA/sourceepoch/manifest ก่อนpublicCommon/integration/directEngineอ่านข้อมูล. Legitimate parent/shared child, date/month reply, delivered financial/live/game resumesยังใช้ได้; oldreceiptหลังepochเปลี่ยนใช้ไม่ได้; emptyreleaseคืนuniforminvalidplanไม่มีclaims. เก็บraw/ผลเดิมครบ. execution_derivation_1792995596594577400 15ผ่าน; finalregressionกำลังตรวจต่อ.

G32พบOne Hour→1 hourทำชื่อเกมหาย และชื่อ2 Players/Two Sessions/7 Minutesกลายเป็นquantity/phantomverifierneed. named_spans.pyแยกsource-bound name spans; guards/dialogue/unitnormalizer/sharedprefix/independentverifier/compiledslotsคงชื่อแต่รับactualquantityนอกชื่อ รวมคำเดียวกันซ้ำสองตำแหน่ง. Diagnostic named_number_slots_1792994492543865000/DETAILS.json; latest named_number_slots_1792995596435500000 **23ผ่าน** owner-isolatedsourceทั้งnormalCommonและtyped. PC for one hourยังduration60 ไม่ถูกชื่อเกมOne Hourขโมย; actualquantity3peopleไม่ถูกanothergameชื่อนั้นลบ; repeatedquote bindactualslotตำแหน่งหลัง.

G33พบAnswer only that point/keep it brief/ขอคำตอบแบบเดียวกันสร้างfactual sharedtargetหรือmultipleantecedentambiguity (style_scope_1792995444488096900/DETAILS.json). style_scope.py maskเฉพาะexplicitpresentationmodifierรักษาoffset/rawและsourceชื่อเหมือนstyle. contextguard/compiledbindings/dialogueไม่ใช้stylepronoun; complete-stylemisclassified taskถูกลบหลังcaptureproposal. actualit/itsนอกstyleยังใช้deliveredcontext; factualsuffixไม่ถูกทิ้ง. Latest style_scope_1792995868851539600 **53ผ่าน** รวมnormalCommon/directEngine/integration, actualConversationStoredeliveredhistory, sourceKeep It Brief. ไม่อ้างว่ารู้arbitrarylanguageครบหรือsemanticaccuracy.

G34พบintegrationอ่านreader.dialogue_contextเก่าจากrequestก่อนหน้า ทำให้interpretationย้อนไปoldquery; G31guardกันdeliveryแต่false-refusal (style_scope_1792995739602030300/DETAILS.json case direct_integration). ใช้เฉพาะcurrentContext.input.dialogue_resolutionที่checkregisteredแล้ว ไม่เชื่อmutableReaderstate/forgedrequestblob. Lateststylecontrolsใช้2เกมgenreต่างกันและตรวจactualclaimrecordIDs ป้องกันผ่านเพราะข้อความเหมือนกัน.

record_audit_iteration.pyมี42evidencegroups/G01–G34componentverification-finalauditpending. record_request_requirement_reviews.pyตอนนี้8requirements **29controlledcriteriaผ่าน+4ยังreview_required**; รวมownerเดิม4requirements19criteriaเป็น12individualreviews/48criteria ไม่ใช่close76หรือ%Flow. Remaining: activeconstrainedgeneration (ยังไม่active HF12921; kill42136เคยautomaticreviewreject ห้ามเลี่ยง), finalplannersemantics/sourcepairedreview, fullbindingsemantics, remainingrolecontrols. อย่าปิดจากenum/schema.

RegressionหลังG32/style: core54ผ่าน1792995615440778200; extended42ผ่าน1792995604631583300 (bounded14lanes≠fullsemantics); graph21ผ่าน1792995604791562800; sourceguards19ผ่าน1792995605365983600; requestcoverage12ผ่าน1792995609543526300; requestdelivery9ผ่าน1792995612761557200; comparisons8ผ่าน1792995609508773100. หลังfinalG34มีsessionsรอตรวจ: graph99521, extended24152, request_context57439, followup38069, execution_derivation10219, request_identity66254. ตรวจผลจริงด้วยwrite_stdin/RESULTก่อนเริ่มซ้ำ. style20311จบpassedแล้ว. ทุกrunไม่มีactualmodel/HTTP.

**ทำต่อทันที:** อ่านremainingroleตารางDATA_CONTRACTS §5 และoriginalledger/specก่อนสร้างindividualreviews R04–R12/contractอื่น/C01–C14/training-eval-phases. ต้องตรวจsessions≠resourcecount, peraudience, eventedition/condition/negation/setทั้งหมดที่ยังขาด. original76textsha/spec3filesยังตรงเดิม. R132sample+analysisครบ2111keys/5584gradesแล้ว ห้ามrestart/analyzeซ้ำ/inferbaseline/regrade/Full20554. ยังขาดroot/source750changedanswers, R133459/R134delta reviewหรือexplicitsupersession, finalR135source-paired330/snapshot/freeze/actualmodelassets/API/activateพร้อมlivebackupแล้วre-audit. ห้ามลบheartbeatหรือประกาศจบจากcontrolsเหล่านี้. ไม่มีexternalblockที่ทำให้งานอื่นเดินไม่ได้.

## ประวัติก่อน G31

'''
p=R/'CURRENT_HANDOFF_TH.md';old=p.read_text('utf8')
if not old.startswith('## ล่าสุดจริง — G31–G34'):p.write_text(header+old,'utf8')
print(json.dumps({'original_requirements_preserved':76,'specific_criteria_passed':status['requirement_specific_controlled_criteria_passed'],'whole_flow_complete':False}))
