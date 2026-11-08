"""Update review/traceability artifacts only; measured output is immutable."""
import collections,hashlib,json,re,time
from pathlib import Path
O=Path(__file__).resolve().parent;R=O.parent
def load(p):return json.loads(p.read_text('utf-8-sig'))
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2),'utf8')
verify=load(O/'INDEPENDENT_COMPLETION_VERIFICATION.json')
assert not verify['changed_or_missing_files'] and not verify['provenance_errors']
audit=load(O/'ROOT_REVIEW_STREAM_AUDIT.json');cases=load(O/'AGENT_SOURCE_CASE_REVIEW.json')
assert audit['raw_requests_read']==20554 and audit['grades_read']==55811 and audit['failed_grade_rows_read']==54333
assert len(cases['cases'])==34 and len({c['key'] for c in cases['cases']})==34
assert (O/'ROOT_CAUSE_REVIEW_TH.md').stat().st_size>60000

# Preserve all original requirements and source text verbatim; add actual evidence.
p=R/'REQUIREMENTS_TRACEABILITY.json';original=load(p)
backup=R/'REQUIREMENTS_TRACEABILITY_BEFORE_FULL_REVIEW.json'
if not backup.exists():backup.write_bytes(p.read_bytes())
prior=[(q['id'],q.get('sha256'),q['text']) for q in original['requirements']]
table={}
for line in (R.parent/'r129_full_plan_completion_20261024/IMPLEMENTATION_REVIEW_TH.md').read_text('utf8').splitlines():
 if not line.startswith('| '):continue
 cells=line.split('|')
 if len(cells)<5:continue
 ident=cells[1].strip().split(' ')[0]
 table[ident]=re.findall(r'`([^`]+)`',cells[3])
issues={
 'C01':['owner50_api_building_floor_unnecessary_context_latency'],
 'C02':['public_vs_members_intent','person_alias_role_period_review'],
 'C03':['gpu_source_present_but_component_binding_fails'],
 'C04':['pc10_resource_scope_omission','static_game_offering_routed_to_live','mode_and_current_installation_unconfirmed'],
 'C05':['resolved_anaphor_still_clarified','partial_source_button_layouts'],
 'C06':['audience_group_size_billing_and_effective_interval_review'],
 'C07':['offsite_notebook_rental_substituted_with_onsite_zone_packages'],
 'C08':['cancellation_actor_negation_and_source_equivalence','booking_compiled_scope'],
 'C09':['refund_credit_paid_change_scenario_scope_and_validity_review'],
 'C10':['studio_permission_leaks_into_tournament','capture_vs_filming_scope'],
 'C11':['service_vs_access_vs_live_calendar','typo_fallback_and_validity_review'],
 'C12':['controlled_provider_is_not_actual_status_proof','static_catalog_live_misrouting'],
 'C13':['title_only_answer_passes_ledger','full_clause_rejected_as_heading','event_scope_lost_across_needs','facet_mapping_mismatch'],
 'C14':['no_real_news_source','general_model_admission_failure','wrong_no_source_clarification_wording']}
cross={
 'FLOW-01':['whole_question_semantic_acceptance_not_met'], 'FLOW-02':['cross_component_integration_quality_gaps'],
 'FLOW-10':['retained_wire_protocol_mismatch'], 'FLOW-11':['schema_enforcement_and_semantic_scope_separate'],
 'FLOW-12':['resolved_anaphor_still_clarified','event_scope_lost_across_needs'],
 'FLOW-13':['resource_and_predicate_binding_failure'], 'FLOW-14':['requested_need_missing_before_ledger'],
 'FLOW-15':['declared_capability_not_all_semantic_operations'], 'FLOW-16':['gpu_source_present_but_component_binding_fails'],
 'FLOW-17':['model_admission_busy_and_timeout','selector_schema_failure'],
 'FLOW-18':['substantive_clause_false_rejection','title_only_false_completion'],
 'FLOW-19':['provider_unavailable_label_conflates_model_and_live'],
 'FLOW-20':['document_header_and_rate_scope_presentation'],
 'FLOW-22':['all_14_readers_present_but_not_all_acceptance_closed'],
 'FLOW-28':['quality_readiness_not_met'],
 'CONTRACT-03':['retained_wire_protocol_mismatch'], 'CONTRACT-05':['resource_scope_and_actor_owner_gaps'],
 'CONTRACT-06':['event_scope_lost_across_needs','resolved_anaphor_still_clarified'],
 'CONTRACT-08':['capability_presence_not_semantic_completeness'],
 'CONTRACT-09':['source_receipt_not_predicate_entailment'],
 'CONTRACT-10':['equivalence_and_temporal_authority_review'],
 'CONTRACT-11':['substantive_clause_false_rejection','whole_question_coverage_gaps'],
 'CONTRACT-12':['unavailable_reason_conflation'], 'CONTRACT-13':['busy_timeout_stage_admission'],
 'CONTRACT-14':['HF_format_not_enforced','explicit_JSON_version_prompt_gap']}
gate_files=[]
for pattern,file in [('graph_verification_*','RESULT.json'),('gateway_verification_*','RESULT.json'),('comparison_verification_*','RESULT.json'),('extended_*','RESULTS.json'),('source_guard_verification_*','VERIFICATION.json'),('live_verification_*','VERIFICATION.json'),('owner_scope_verification_*','RESULT.json'),('source_match_metadata_*','RESULT.json')]:
 candidates=[x/file for x in R.glob(pattern) if (x/file).exists()]
 chosen=max(candidates,key=lambda x:x.stat().st_mtime)
 d=load(chosen);assert d.get('summary',d).get('all_passed')
 gate_files.append(str(chosen.relative_to(R)))
for req in original['requirements']:
 ident=req['id']; refs=[]
 for name in table.get(ident,[]):
  path=R/name
  if not path.exists():path=R.parent/'r129_full_plan_completion_20261024'/name
  if path.exists():refs.append(str(path.resolve()))
 req['implementation']=refs
 req['implementation_evidence_is_not_semantic_acceptance']=True
 req['acceptance_evidence']=[str((R/n).resolve()) for n in ['READINESS.json','PLANNER_ADJUDICATION_R130.json','full_analysis/COVERAGE.json','full_analysis/ROOT_CAUSE_REVIEW_TH.md','full_analysis/AGENT_SOURCE_CASE_REVIEW.json','full_analysis/INDEPENDENT_COMPLETION_VERIFICATION.json']]
 req['full_evaluation_complete']=True
 req['root_cause_group_review_complete']=True
 req['semantic_acceptance_complete']=False
 req['acceptance_state']='measured_full_coverage_root_review_complete_quality_acceptance_open'
 req['remaining_issues']=issues.get(ident,cross.get(ident,['requirement_specific_semantic_acceptance_not_closed_by_generic_gates']))
 req['status']='implementation_evidence_and_measurement_present_acceptance_open'
 if ident in ['PHASE-07','PHASE-08','PHASE-09','CONTRACT-15']:
  req['status']='training_procedure_evidence_complete_not_answer_accuracy'
  req['acceptance_evidence'].extend([str((R.parent/'r129_full_plan_completion_20261024'/n).resolve()) for n in ['training_v2/DATASET_FREEZE.json','training_v2/train01/TRAINING_COMPLETE.json','training_v2/train01/OPTIMIZATION_PROOF.json']])
  req['remaining_issues']=['new_adapter_semantic_promotion_rejected_no_business_data_retraining_needed']
 elif ident in ['PHASE-10','PHASE-13','PHASE-17']:
  req['status']='paired_measurement_and_agent_retained_selection_complete'
  req['remaining_issues']=['new_weights_not_promoted','retained_protocol_and_execution_gaps_remain']
 elif ident=='PHASE-16':
  req['status']='saved_baseline_fixed_identity_comparison_complete'
  req['acceptance_evidence'].append(str((O/'FIXED_DENOMINATOR_SCORES.json').resolve()))
  req['remaining_issues']=['source_backend_precision_clock_deadline_confounds','semantic_accuracy_not_inferred']
 elif ident in ['PHASE-11','PHASE-14','PHASE-15','PHASE-20']:
  req['status']='measurement_reporting_complete_quality_acceptance_not_complete'
 elif ident in ['FLOW-29','PHASE-18','PHASE-21']:
  req['status']='reference_scope_retained_measurement_linked'
 req['scope_retained']=True
assert prior==[(q['id'],q.get('sha256'),q['text']) for q in original['requirements']]
assert len(prior)==76
original.update(overall_complete=False,completion_percent=None,accuracy_percent=None,full_evaluation_complete=True,root_cause_group_review_complete=True,semantic_acceptance_complete=False,production_installed=False,known_quality_gaps_remain=True,mechanism_gate_evidence=gate_files,completion_basis='full measurement and source review complete; original Flow quality requirements remain open',updated_at_unix=time.time())
write(p,original)

matrix=['# ตรวจรับ76หัวข้อหลัง Full Test R130','', 'คงid/text/hashทุกข้อครบ76จากต้นฉบับ ไม่มีเปอร์เซ็นต์งานเสร็จหรือการนับmoduleเป็นการผ่านsemantic ทั้งหมด Full Testและrootreviewเสร็จ แต่Flowคุณภาพยังไม่ผ่านครบ ดูJSONสำหรับevidencepaths/remainingissuesรายข้อ','', '| ID | หัวข้อ | สถานะหลักฐาน | สิ่งที่ยังต้องปิด |','|---|---|---|---|']
for q in original['requirements']:matrix.append('| '+q['id']+' | '+q['title']+' | '+q['status']+' | '+'; '.join(q['remaining_issues'])+' |')
(R/'REQUIREMENTS_REVIEW_AFTER_FULL_TH.md').write_text('\n'.join(matrix)+'\n','utf8')

final=load(O/'ANALYSIS_FINAL.json');final.update(human_agent_root_cause_review_complete=True,root_cause_group_review_complete=True,individual_source_case_reviews=34,source_confirmed_content_failure_examples=15,exhaustive_semantic_adjudication=False,semantic_accuracy=None,overall_task_complete=False,evaluation_and_root_review_complete=True,flow_quality_acceptance_complete=False,all_76_requirements_retained=True,production_installed=False,evidence=['ROOT_CAUSE_REVIEW_TH.md','AGENT_SOURCE_CASE_REVIEW.json','AGENT_REVIEW_SOURCE_EVIDENCE.json','ALL_REASON_TRIAGE.json','INDEPENDENT_COMPLETION_VERIFICATION.json'],review_completed_at_unix=time.time())
write(O/'ANALYSIS_FINAL.json',final)
full=load(R/'FULL_TEST_COMPLETE.json');full.update(root_cause_review_pending=False,root_cause_group_review_complete=True,semantic_accuracy=None,flow_quality_acceptance_complete=False);write(R/'FULL_TEST_COMPLETE.json',full)
state=load(R/'STATUS.json');state.update(phase='full_evaluation_and_root_review_complete_quality_acceptance_open',complete=False,full_test_complete=True,analysis_complete=True,root_cause_review_complete=True,flow_quality_acceptance_complete=False,production_installed=False,updated_at=time.time(),completion_note='Full Test/report finished; original Flow quality requirements remain open.');write(R/'STATUS.json',state)

report=(O/'FINAL_REPORT_TH.md').read_text('utf8')
report=report.replace('ยังต้องตรวจ ROOT_CAUSE_REVIEW_TH.md โดยอ้าง raw responses และ source evidence ทุกกลุ่ม ข้อที่ตัดสินไม่ได้คง review_required ไม่เหมารวม keyword/clause fail เป็นคำตอบผิดจริง',
 'ROOT_CAUSE_REVIEW_TH.md ตรวจรากปัญหาครบทุกกลุ่มจากraw20,554requests/55,811gradesและ921reasonstringsแล้ว มี34case adjudicationsพร้อมsource77records/209snapshots ยืนยันตัวอย่างcontent/scope/omissionfailure15requests ไม่ใช่จำนวนผิดทั้งหมดและไม่ใช้คิดsemanticaccuracy คงreview_requiredสำหรับข้อที่ยังไม่ตัดสิน Flowยังไม่ผ่านคุณภาพครบ76ข้อ')
report += '''
## ข้อพบสำคัญหลังตรวจsourceจริง

- ข้อมูลGPUและกติกาCS2มีแล้ว แต่binding/verifierทำให้ไม่ตอบ; CS2textเท่ากับheadingถูกตัดทิ้ง ขณะที่ชื่อเอกสารTekkenformatกลับผ่านledger
- คำถามPC#10เสียresource scope; คำถามดูสตรีมระหว่างแข่งกลับตอบนโยบายสตรีมในศูนย์; tournamentfoodscopeหายระหว่างหลายneed
- availableในคำถามcatalogถูกส่งlive; explicititผูกเกมแล้วแต่ยังถามชื่อเกมซ้ำ; offsite notebookถูกแทนด้วยราคาเหมาโซน
- ชื่อกลุ่มcontrolled_provider_unavailable4,132กว้างเกินไป:3,160taskเป็นmodel-coded และ972ไม่มีreasoncode ต้องแยกจากliveartifacts1,082requests ห้ามอ้างทุกกลุ่มเป็นproviderจริงล่ม
- actualHTTP425/สำเร็จ263/timeouts162; successfulgatewayทุก263ตรวจprofile/adapter/messages/schema/stageได้ (retained199/base64) แต่HTTP/JSONไม่ใช่semanticcorrect
- median0.663s/p953.575s/p9947.175s/max151.130s ยังมี340requestsเกิน20s

คะแนนstrictตกหนักจากroute/intent/modecontract แต่literalก็ยังตามsavedR64 จึงยังไม่มีหลักฐานว่าคุณภาพใกล้Flowเดิมแล้ว รายละเอียดfixeddenominator/unknownและbaselineconfoundsในSAVED_FLOW_COMPARISON_TH.md และ FIXED_DENOMINATOR_SCORES.json

ตรวจhash2,361filesและlogicalsource/modelprovenanceซ้ำแบบread-onlyแล้วไม่เปลี่ยน ไม่มีbaselineinferenceใหม่ Candidateไม่ติดตั้งทับR78 งานวัดและรายงานเสร็จ; งานแก้คุณภาพยังเปิดอยู่
'''
(O/'FINAL_REPORT_TH.md').write_text(report,'utf8')
compare=(O/'SAVED_FLOW_COMPARISON_TH.md').read_text('utf8')
compare+='''
## การตีความหลังตรวจsource

รวมR130strict1,478/55,811=2.65%; fixedpositive literal19,050/24,909=76.48% R95literal18,283/24,909=73.40%; R64literal23,512/24,909=94.39%และunassessed194คงในตัวหาร ค่าทั้งหมดไม่ใช่semanticansweraccuracy

literalR130ดีกว่าR95ไทย+336/อังกฤษ+455/auto−24checks รวม+767 แต่pairedR95-only2,630/R130-only3,397 ไม่ใช่ดีขึ้นทุกเคส strictR95-only3,761/R130-only209

R130ใช้retainedR121contextweightsหลังnewไม่ผ่านcriticalsource review ส่วนselector/genericเป็นbase บนHFNF4BF16ที่รับformatเพื่อเก็บhashแต่ไม่ได้constrainoutput ต่างจากOllama/GGUFของbaseline ข้อมูลsource/translation/currentvalidity/calendar/clock/deadline/admissionต่างรุ่น จึงไม่อ้างcausalFloweffectและไม่เรียกretainedwire0ว่าlegacyansweraccuracy0

ROOT_CAUSE_REVIEW_TH.mdแยกsource-confirmed content/scope/omissionจากroute/keyword/firstline/completeclause/validity/sourcegaps/transport โดยไม่regradebaselineใหม่
'''
(O/'SAVED_FLOW_COMPARISON_TH.md').write_text(compare,'utf8')
handoff=(R/'CURRENT_HANDOFF_TH.md').read_text('utf8')
new='''## สถานะหลัง Full Test และ agent root review — ใหม่กว่าข้อความขั้นรันด้านล่าง

Full R130 full01 ครบ20554keys/55811gradeidentitiesแล้ว ตรวจfrozen2361files/logicalsource/modelจริง263successfulgatewaycallsไม่เปลี่ยน ไม่มีmissing/duplicate หลังอ่านraw/allfailures/perrequestครบ จัด921reasonstringsทุกกลุ่ม ทำROOT_CAUSE_REVIEW_TH.mdจริง70kchars/34manualsourcecases/77records/209snapshots มี15ตัวอย่างconfirmedcontent/scope/omissionfailure ไม่ใช่จำนวนผิดทั้งหมด ไม่มีoverallsemanticaccuracy

ดูfull_analysis/ANALYSIS_FINAL.json, FINAL_REPORT_TH.md, FIXED_DENOMINATOR_SCORES.json, SAVED_FLOW_COMPARISON_TH.md, INDEPENDENT_COMPLETION_VERIFICATION.json และ REQUIREMENTS_REVIEW_AFTER_FULL_TH.md คง76requirements/source textเดิมครบ และยังoverall_complete=false/qualityacceptance=false ไม่ประกาศFlowครบหรือพร้อมติดตั้ง งานวัดและรายงานจบ แต่ยังต้องแก้protocol/admission, C13clauseverifier+eventscope, resource/GPUbinding, anaphor, negativecancel, cataloglive และrenderer/validityในcandidateถัดไป ห้ามแก้frozenR130หรือผลเดิม

คะแนนliteralR130ไทย78.06/en75.81/auto70.19ยังตามsavedR64; strictถูกroutecontractกดหนัก ไม่ใช่semanticaccuracy2.65% newไม่ได้promoteยังใช้retainedบนengineR130 Candidateไม่ติดตั้งR78 เมื่อส่งผลไทยแล้วปิดheartbeatการติดตามFullรอบนี้ตามคำสั่ง ไม่ใช่รับรองFlowผ่านครบ

'''
(R/'CURRENT_HANDOFF_TH.md').write_text(new+handoff,'utf8')
print(json.dumps({'traceability_requirements':len(prior),'source_texts_unchanged':True,'analysis_complete':True,'flow_quality_complete':False,'reports_ready':True},ensure_ascii=False))
