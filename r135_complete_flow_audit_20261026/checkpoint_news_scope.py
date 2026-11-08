"""Source-specific C14 checkpoint; no requirement closure or activation."""
import json,hashlib,time
from pathlib import Path
R=Path(__file__).resolve().parent
def read(p):return json.loads(p.read_text('utf8'))
ledger=read(R/'COMPLETION_LEDGER.json');assert len(ledger['requirements'])==76
for r in ledger['requirements']:assert hashlib.sha256(r['text'].encode()).hexdigest()==r['text_sha256']
for n in ['FLOW_MAIN_TH.md','DATA_CONTRACTS_TH.md','IMPLEMENTATION_EVALUATION_TH.md']:assert (R/'spec'/n).read_bytes()==(R.parent/'r123_plan_distillation_architecture_20261023'/n).read_bytes()
gaps=read(R/'AUDIT_GAPS.json');assert len(gaps['gaps'])==57
reports={}
for prefix in ['news_matrix_','news_status_verification_','core_verification_','source_guard_verification_','receipt_scope_verification_','graph_verification_','wire_compatibility_']:
 p=sorted(p for p in R.glob(prefix+'*/*') if p.name in {'RESULT.json','VERIFICATION.json','RESULTS.json'})[-1];d=read(p);d=d.get('summary',d)
 assert d.get('all_passed',d.get('passed')),p
 reports[prefix.rstrip('_')]={'path':str(p.relative_to(R)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'checks':len(d['checks'])}
reviews=[read(R/p) for p in ['OWNER_REQUIREMENT_REVIEWS.json','REQUEST_REQUIREMENT_REVIEWS.json','EXECUTOR_REQUIREMENT_REVIEWS.json','CATEGORY_REQUIREMENT_REVIEWS.json']];rows=[r for v in reviews for r in v['requirements']];assert len(rows)==len({r['requirement_id'] for r in rows})
obs=sorted(R.glob('SOURCE_PRESERVATION_OBSERVATION_*.json'))[-1];o=read(obs);assert not o['candidate_vs_frozen_parent_differences'] and not o['candidate_vs_live_differences']
status=read(R/'STATUS.json');status.update(last_recorded_at=time.time(),last_component_repairs=['G55','G56','G57'],requirement_specific_review_ids=[r['requirement_id'] for r in rows],requirement_specific_controlled_criteria_passed=sum(c['state']=='passed_controlled_acceptance' for r in rows for c in r['criteria']),category_review_pending_criteria=sum(c['state']=='review_required' for r in reviews[3]['requirements'] for c in r['criteria']),latest_news_scope_reports=reports,last_source_preservation_observation=obs.name,candidate_frozen=False,candidate_installed=False,active_installed_revision='R134',complete=False,whole_flow_complete=False,requirement_closure_claimed=False,next_work='Continue C01/C03/C04/C05/C08-C10/C13 source-operation-field acceptance and G40 multi-service/implicit/combined conditions. Actual news source absent; no fabricated news. Composite authority/saved-source variants, original training/evaluation requirement reviews and final raw/source/model/freeze/API/activation re-audit remain pending.')
(R/'STATUS.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n','utf8')
header=f'''## ล่าสุดจริง — C14 source/field/publication audit; G55–G57 component repaired

R135 working/unfrozen/uninstalled; R134 installedจริง health8115 build common-r134-resolution-scope/sourceSHA db1685eafe9f1d95460614a0948792710c3462cdfac20b90beabd2f12d1ae157. ตรวจPID/commandlineจริง37660chat/45088editor/42136model12921. {obs.name}: readonlyทุกSQLitetableรวมWAL candidate/frozenR134/actualinstalledเท่ากัน. ไม่sourceDB/userdata/approvals/log/history/frozenR132/130/131/weightsedit ไม่modelinference/providerHTTP/retrain/restart/subagents. R121retainedcontext/base selectorเดิม; failednewadapterไม่promote; constraineddecodernotactive; automaticreviewdeniedmodelkill2ครั้งห้ามเลี่ยง.

G55 baseline news_matrix_1793022728042067500: description aliasไม่ได้body และnaturalCommonถามregistrationlinkในannouncementแต่แสดงunaskedbodyก่อนURL. แก้meaningalias/nativefacet. G56 baselineเดียวกัน: freshstatusTTLทำให้expired/futurepublicationตอบcurrentได้. ตอนนี้publicationvalidityแยกจากobservationfreshness; explicitoldbodyมีhistoricalnotice, unknownvaliditybodypartial+visiblelimit, statusที่publicationไม่ยืนยันwithheld. G57 independentreceiptเดิมplanneromittargetแล้วยอมwrongeditionvalidrefs; ตอนนี้rebindactualquestionกับsourcetitle/alias+editionเอง และsharedaliasหลายeditionต้องclarify. Independentverifierrecomputepublication+requestedobservationdate ปฏิเสธforgedstatusmetadata. ไม่อ้างเวลาจัดงานหรือURLเป็นสถานะสมัคร.

C14ครบ7declaredfieldaliasesมีsourcepositivecases, English/ThaiCommondelivery, expired/future/unknownpublication, historicalbody/statusdistinction, wrongedition/omittarget/sharedalias/wrongdate/forgedpublication negativecontrols. **actualretainednewsrecordsยังว่าง** ตรวจreadonlyแยกจากcontrolledownerfixtures; ไม่สร้างข่าวจริง/approval และไม่อ้างfixtureเป็นempiricalaccuracy.

Latest reports:
{chr(10).join('- '+n+': '+v['path']+' ('+str(v['checks'])+' checks)' for n,v in reports.items())}

Original76ID/textSHA/spec3filesคงเดิม. Individualreview {len(rows)}requirements/{status['requirement_specific_controlled_criteria_passed']}controlledcriteria; categorypending{status['category_review_pending_criteria']}. **ไม่ปิดrequirementใด/ไม่คิด%Flow/ไม่declarecomplete**. G01–G57; G40ยังopenremainingmulti-service/implicitroles/combinedconditions. Latestrecorder record_audit_iteration.py → record_executor_requirement_reviews.py → record_category_requirement_reviews.py → checkpoint_news_scope.py. Oldercheckpointassert54/ทับlateststatusอย่ารัน.

ทำต่อC01/C03/C04/C05/C08–C10/C13และG40; compositeauthority/actualsavedvariants+originaltraining/distillation/label/familysplit/metricrequirementsยังauditinprogress. R132sample/analyzerครบ2111/5584แล้วห้ามrerun/baselineinference/regrade/Full20554. ยังroot/source750changedcases+R133459/R134delta reviewหรือexplicitsupersession, finalR135exactsuccessfulrequest/messages/schema/profile/adapter/stage/precision/cap paired330ไม่มีnewcontextinference, source/input/modelassets/freeze/API. Activateเฉพาะพิสูจน์ครบผ่านnormalentrypointพร้อมfreshactualinstalledliveSQLitebackupทุกtableแล้วreaudit. ห้ามลบheartbeat/หยุดแค่C14testsหรือrootreviewครบ. เดินaudit→repair→test→reauditต่อไม่ถามซ้ำ/ไม่ใช้subagents.

## ประวัติก่อน C14 audit

'''
p=R/'CURRENT_HANDOFF_TH.md';p.write_text(header+p.read_text('utf8'),'utf8');print(json.dumps({'preserved_requirements':76,'individually_reviewed':len(rows),'controlled_criteria':status['requirement_specific_controlled_criteria_passed'],'complete':False}))
