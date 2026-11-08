"""Curated clause-level reviews; no generic evidence copied across the 76 items."""
import json,hashlib,time
from pathlib import Path
R=Path(__file__).resolve().parent
def read(p):return json.loads(p.read_text('utf8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def latest(prefix):
 p=sorted(R.glob(prefix+'*/RESULT.json'))[-1];d=read(p);assert d['all_passed'];return p,d
data,dd=latest('data_ingestion_');owner,od=latest('owner_contract_verification_');wire,wd=latest('wire_compatibility_')
competition,cd=latest('competition_relations_')
boundary,bd=latest('source_instruction_boundary_')
def criterion(text,kind,*names):
 p,d=(data,dd) if kind=='data' else (competition,cd) if kind=='competition' else (boundary,bd) if kind=='boundary' else (owner,od)
 assert names and all(d['checks'].get(n) is True for n in names),(text,names)
 return {'criterion':text,'state':'passed_controlled_acceptance','evidence':str(p.relative_to(R)),'evidence_sha256':sha(p),'checks':list(names)}
def pending(text,why):return {'criterion':text,'state':'review_required','reason':why}
reviews={
'FLOW-04':[
 criterion('เพิ่ม game alias / equipment / price ตามชนิดเดิมและถาม typed ได้โดยไม่เปลี่ยน weights หรือ prompt','data','new_game_alias_reaches_typed_answer_without_training','new_equipment_source_reaches_typed_answer_without_training','new_rate_reaches_typed_answer_without_training','edited_rate_changes_next_typed_answer_without_training'),
 criterion('game-service และ rate-service/audience เป็น relation จริงพร้อม source pointers','data','valid_price_relation_and_currency_accepted','offering_projection_keeps_relation_evidence','wrong_service_kind_reported'),
 criterion('operation ใหม่ยัง unsupported จนมี reader contract','data','unknown_operation_not_advertised_or_silently_detail'),
 criterion('competition rule ผูก game/event/edition และ dependency จากsourceจริง ไม่เลือกฉบับใกล้เคียง','competition','valid_event_and_rule_foreign_keys_accepted','rule_cannot_link_game_as_event','event_cannot_link_rule_as_game','cross_edition_rule_dependency_rejected','cyclic_rule_dependency_rejected','edition_2025_source_delivered_only','edition_2026_source_delivered_only','nonnumeric_rulebook_release_is_source_bound','other_edition_receipt_rejected_independently','game_title_year_does_not_choose_event_release'),
],
'FLOW-05':[
 criterion('type / currency / unit / duration / foreign keys ตรวจต่อ field ก่อน index','data','currency_rejected_before_index','unit_rejected_before_index','duration_zero_rejected_before_index','duration_string_rejected_before_index','negative_price_rejected_before_index','missing_service_reported','wrong_service_kind_reported'),
 criterion('unknown / not_applicable / conflicted เป็นสถานะแยก ไม่ assert value','data','unknown_has_explicit_nonasserting_representation','not_applicable_has_explicit_nonasserting_representation','conflicted_has_explicit_nonasserting_representation','conflicted_not_publishable'),
 criterion('การแก้เนื้อหาทำให้ translation review เก่าใช้ต่อไม่ได้','owner','content_edit_invalidates_translation_review'),
 criterion('withdrawal และ revision ทำให้ผลเก่าถูกถอน/ตรวจ stale request','owner','withdrawn_published_content_not_in_next_index','epoch_invalidates_inflight_snapshot','rollback_does_not_resurrect_withdrawn'),
 criterion('owner เห็น missing/incomplete game-service relation และรับเฉพาะ target kind ถูก','data','missing_game_service_relation_reported','incomplete_offering_relation_not_ready','related_wrong_target_kind_not_ready','explicit_relation_resolves_owner_gap','unfinished_sibling_does_not_erase_complete_relation'),
 criterion('schedule validation ใช้ contiguous union และยังปฏิเสธช่องว่างจริง','data','adjacent_opening_union_accepts_valid_booking','real_opening_gap_rejects_booking'),
 criterion('คำสั่งในเอกสารคงเป็น data และ adversarial selector proposal ไม่สร้าง approval/publication หรือข้ามbudget (ไม่ใช่การวัดความต้านทาน prompt injection ของโมเดลจริง)','boundary','source_command_stays_in_json_data_not_a_message_role','trusted_selector_instruction_explicitly_denies_source_authority','model_extras_cannot_create_authority_actions','invented_source_choice_rejected','source_command_cannot_bypass_zero_budget','source_and_adversarial_response_do_not_approve_or_publish','owner_record_stays_draft'),
],
'FLOW-06':[
 criterion('save ที่ผ่าน schema ยังคง draft ไม่สร้าง approval/publication','owner','save_is_draft_not_approval','draft_not_silently_published','unapproved_publish_rejected'),
 criterion('การ publish ต้อง explicit revision/hash และการแก้ต้อง review ใหม่','owner','reviewed_fixture_publish_requires_explicit_revision_hash','new_revision_does_not_inherit_old_approval','stale_edit_rejected'),
 criterion('published view คงรุ่นเดิมจน publish และ draft view แยกชัด','owner','published_snapshot_keeps_prior_revision','draft_view_explicitly_separate','publish_idempotent'),
 criterion('audit ครอบ save/review/publish/edit/withdraw และ rollbackไม่ฟื้นwithdrawn','owner','save_review_publish_edit_withdraw_audited','rollback_does_not_resurrect_withdrawn'),
],
'FLOW-07':[
 criterion('request pin records/aliases เป็น revision เดียว และ sourcechange invalidate request เก่า','data','pinned_records_and_aliases_remain_one_revision','source_change_invalidates_old_request'),
 criterion('capability catalog ผูกกับ source index จริงและไม่รับ arbitrary operations','data','catalog_is_bound_to_added_price_and_game_sources','offering_projection_keeps_relation_evidence','unknown_operation_not_advertised_or_silently_detail'),
 criterion('เพิ่ม/แก้ราคา เกม อุปกรณ์ แล้ว typed อ่านข้อมูลใหม่โดยไม่ฝึก','data','new_game_alias_reaches_typed_answer_without_training','new_equipment_source_reaches_typed_answer_without_training','new_rate_reaches_typed_answer_without_training','edited_rate_changes_next_typed_answer_without_training'),
 criterion('คำถามต่อเกม อุปกรณ์ และราคาที่เพิ่มใหม่ผ่าน normal CommonAnswerer โดยไม่ inject MeaningTask หรือใช้ model/provider HTTP','data','game_new_data_works_through_normal_common_answerer','equipment_new_data_works_through_normal_common_answerer','rate_new_data_works_through_normal_common_answerer'),
]}
files=['app/knowledge/common/registry.py','app/knowledge/common/store.py','app/knowledge/store.py','app/knowledge/common/task_registry.py','app/knowledge/common/snapshot_provider.py','app/knowledge/common/domain_flow/projection.py','app/knowledge/common/domain_flow/index.py','app/knowledge/common/domain_flow/capabilities.py','app/knowledge/common/domain_flow/model.py','app/knowledge/common/domain_flow/scope.py','app/knowledge/common/domain_flow/receipt_scope.py']
ledger=read(R/'COMPLETION_LEDGER.json');byid={x['id']:x for x in ledger['requirements']};rows=[]
for rid,criteria in reviews.items():
 row={'requirement_id':rid,'original_text_sha256':byid[rid]['text_sha256'],'criteria':criteria,'all_listed_clauses_controlled_passed':all(c['state']=='passed_controlled_acceptance' for c in criteria),'final_revision_api_and_installation_reaudit_pending':True,'whole_semantic_accuracy_claimed':False}
 rows.append(row);byid[rid]['individual_review']={'path':'OWNER_REQUIREMENT_REVIEWS.json','requirement_id':rid,'state':'controlled_acceptance_passed_final_revision_pending' if row['all_listed_clauses_controlled_passed'] else 'clause_level_review_in_progress','remaining_criteria':[c['criterion'] for c in criteria if c['state']=='review_required']}
payload={'reviewed_at':time.time(),'candidate':'R135 working unfrozen uninstalled','whole_flow_complete':False,'limits':['controlled source tests do not prove all natural-language questions','model instruction-following resistance and arbitrary new-name planning are unassessed','final candidate source replay/API/installation acceptance still pending'],'final_model_wire_unchanged_evidence':str(wire.relative_to(R)),'code_sha256':{f:sha(R/'system'/f) for f in files},'requirements':rows}
(R/'OWNER_REQUIREMENT_REVIEWS.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n','utf8');(R/'COMPLETION_LEDGER.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n','utf8')
print(json.dumps({'individual_requirements_reviewed':list(reviews),'component_clauses_passed':sum(c['state']=='passed_controlled_acceptance' for row in rows for c in row['criteria']),'remaining_clause_reviews':sum(c['state']=='review_required' for row in rows for c in row['criteria']),'whole_flow_complete':False}))
