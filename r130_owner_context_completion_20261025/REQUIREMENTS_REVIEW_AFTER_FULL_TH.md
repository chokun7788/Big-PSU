# ตรวจรับ76หัวข้อหลัง Full Test R130

คงid/text/hashทุกข้อครบ76จากต้นฉบับ ไม่มีเปอร์เซ็นต์งานเสร็จหรือการนับmoduleเป็นการผ่านsemantic ทั้งหมด Full Testและrootreviewเสร็จ แต่Flowคุณภาพยังไม่ผ่านครบ ดูJSONสำหรับevidencepaths/remainingissuesรายข้อ

| ID | หัวข้อ | สถานะหลักฐาน | สิ่งที่ยังต้องปิด |
|---|---|---|---|
| FLOW-01 | 1. เป้าหมายและสิ่งที่ต้องแก้ให้ตรงจุด | implementation_evidence_and_measurement_present_acceptance_open | whole_question_semantic_acceptance_not_met |
| FLOW-02 | 2. ภาพรวมสาม Flow ที่ต้องทำงานร่วมกัน | implementation_evidence_and_measurement_present_acceptance_open | cross_component_integration_quality_gaps |
| FLOW-04 | D01 — รับข้อมูลเป็น record ที่มีชนิดและขอบเขต | implementation_evidence_and_measurement_present_acceptance_open | requirement_specific_semantic_acceptance_not_closed_by_generic_gates |
| FLOW-05 | D02 — ตรวจข้อมูลก่อนสร้าง index | implementation_evidence_and_measurement_present_acceptance_open | requirement_specific_semantic_acceptance_not_closed_by_generic_gates |
| FLOW-06 | D03 — แยกความถูกต้องเชิงโครงสร้างจากสิทธิ์เผยแพร่ | implementation_evidence_and_measurement_present_acceptance_open | requirement_specific_semantic_acceptance_not_closed_by_generic_gates |
| FLOW-07 | D04 — Compile snapshot และ capability catalog | implementation_evidence_and_measurement_present_acceptance_open | requirement_specific_semantic_acceptance_not_closed_by_generic_gates |
| FLOW-09 | R00 — รับคำถามและ pin request context | implementation_evidence_and_measurement_present_acceptance_open | requirement_specific_semantic_acceptance_not_closed_by_generic_gates |
| FLOW-10 | R01 — โมเดลเสนอแผนงานที่มีโครงสร้าง | implementation_evidence_and_measurement_present_acceptance_open | retained_wire_protocol_mismatch |
| FLOW-11 | R02 — ตรวจโครงสร้างและข้อความอ้าง | implementation_evidence_and_measurement_present_acceptance_open | schema_enforcement_and_semantic_scope_separate |
| FLOW-12 | R03 — ผูก local slots และ shared context | implementation_evidence_and_measurement_present_acceptance_open | resolved_anaphor_still_clarified; event_scope_lost_across_needs |
| FLOW-13 | R04 — Resolve entities และตรวจ semantics | implementation_evidence_and_measurement_present_acceptance_open | resource_and_predicate_binding_failure |
| FLOW-14 | R05 — สร้าง obligation ledger และ task graph | implementation_evidence_and_measurement_present_acceptance_open | requested_need_missing_before_ledger |
| FLOW-15 | R06 — ตรวจว่า executor ทำ operation นี้ได้จริง | implementation_evidence_and_measurement_present_acceptance_open | declared_capability_not_all_semantic_operations |
| FLOW-16 | R07 — อ่านทุกงานที่ทำแบบ deterministic ได้ก่อน | implementation_evidence_and_measurement_present_acceptance_open | gpu_source_present_but_component_binding_fails |
| FLOW-17 | R08 — จัดการช่องว่างและ model fallback แบบจำกัด | implementation_evidence_and_measurement_present_acceptance_open | model_admission_busy_and_timeout; selector_schema_failure |
| FLOW-18 | R09 — ตรวจหลักฐาน ขอบเขต และความครบ | implementation_evidence_and_measurement_present_acceptance_open | substantive_clause_false_rejection; title_only_false_completion |
| FLOW-19 | R10 — เลือกสถานะต่อ task และต่อคำตอบ | implementation_evidence_and_measurement_present_acceptance_open | provider_unavailable_label_conflates_model_and_live |
| FLOW-20 | R11 — จัดคำตอบจาก claims ที่ผ่านแล้ว | implementation_evidence_and_measurement_present_acceptance_open | document_header_and_rate_scope_presentation |
| FLOW-21 | R12 — เก็บ audit และ regression case | implementation_evidence_and_measurement_present_acceptance_open | requirement_specific_semantic_acceptance_not_closed_by_generic_gates |
| FLOW-22 | 5. Executor ทั้ง 14 หมวด | implementation_evidence_and_measurement_present_acceptance_open | all_14_readers_present_but_not_all_acceptance_closed |
| C01 | C01 ข้อมูลศูนย์/ติดต่อ | implementation_evidence_and_measurement_present_acceptance_open | owner50_api_building_floor_unnecessary_context_latency |
| C02 | C02 บุคลากร | implementation_evidence_and_measurement_present_acceptance_open | public_vs_members_intent; person_alias_role_period_review |
| C03 | C03 อุปกรณ์ | implementation_evidence_and_measurement_present_acceptance_open | gpu_source_present_but_component_binding_fails |
| C04 | C04 เกม | implementation_evidence_and_measurement_present_acceptance_open | pc10_resource_scope_omission; static_game_offering_routed_to_live; mode_and_current_installation_unconfirmed |
| C05 | C05 การควบคุม | implementation_evidence_and_measurement_present_acceptance_open | resolved_anaphor_still_clarified; partial_source_button_layouts |
| C06 | C06 ราคาปกติ | implementation_evidence_and_measurement_present_acceptance_open | audience_group_size_billing_and_effective_interval_review |
| C07 | C07 ราคาเหมา | implementation_evidence_and_measurement_present_acceptance_open | offsite_notebook_rental_substituted_with_onsite_zone_packages |
| C08 | C08 การจอง | implementation_evidence_and_measurement_present_acceptance_open | cancellation_actor_negation_and_source_equivalence; booking_compiled_scope |
| C09 | C09 การชำระเงิน | implementation_evidence_and_measurement_present_acceptance_open | refund_credit_paid_change_scenario_scope_and_validity_review |
| C10 | C10 กฎศูนย์ | implementation_evidence_and_measurement_present_acceptance_open | studio_permission_leaks_into_tournament; capture_vs_filming_scope |
| C11 | C11 ตาราง | implementation_evidence_and_measurement_present_acceptance_open | service_vs_access_vs_live_calendar; typo_fallback_and_validity_review |
| C12 | C12 สถานะจริง | implementation_evidence_and_measurement_present_acceptance_open | controlled_provider_is_not_actual_status_proof; static_catalog_live_misrouting |
| C13 | C13 กติกาแข่งขัน | implementation_evidence_and_measurement_present_acceptance_open | title_only_answer_passes_ledger; full_clause_rejected_as_heading; event_scope_lost_across_needs; facet_mapping_mismatch |
| C14 | C14 ข่าว/กิจกรรม | implementation_evidence_and_measurement_present_acceptance_open | no_real_news_source; general_model_admission_failure; wrong_no_source_clarification_wording |
| FLOW-23 | 6. Flow Distillation ที่ใช้เป็นแกนฝึก planner | implementation_evidence_and_measurement_present_acceptance_open | requirement_specific_semantic_acceptance_not_closed_by_generic_gates |
| FLOW-24 | สิ่งที่สอน | implementation_evidence_and_measurement_present_acceptance_open | requirement_specific_semantic_acceptance_not_closed_by_generic_gates |
| FLOW-25 | สิ่งที่อ่านจาก source ตอนตอบ | implementation_evidence_and_measurement_present_acceptance_open | requirement_specific_semantic_acceptance_not_closed_by_generic_gates |
| FLOW-26 | สิ่งที่ต้องระวัง | implementation_evidence_and_measurement_present_acceptance_open | requirement_specific_semantic_acceptance_not_closed_by_generic_gates |
| FLOW-27 | 7. ตัวอย่างจากคำถามเดิม: เป้าหมายของ Flow นี้ | implementation_evidence_and_measurement_present_acceptance_open | requirement_specific_semantic_acceptance_not_closed_by_generic_gates |
| FLOW-28 | 8. จุดที่ต้องผ่านก่อนถือว่า Flow พร้อม | implementation_evidence_and_measurement_present_acceptance_open | quality_readiness_not_met |
| FLOW-29 | 9. สิ่งที่ได้ในงานวาง Flow รอบนี้ | reference_scope_retained_measurement_linked | requirement_specific_semantic_acceptance_not_closed_by_generic_gates |
| CONTRACT-01 | 1. หลักการร่วม | implementation_evidence_and_measurement_present_acceptance_open | requirement_specific_semantic_acceptance_not_closed_by_generic_gates |
| CONTRACT-02 | 2. RequestContext | implementation_evidence_and_measurement_present_acceptance_open | requirement_specific_semantic_acceptance_not_closed_by_generic_gates |
| CONTRACT-03 | 3. PlannerProposal | implementation_evidence_and_measurement_present_acceptance_open | retained_wire_protocol_mismatch |
| CONTRACT-04 | 4. Task และ vocabulary ของ operation | implementation_evidence_and_measurement_present_acceptance_open | requirement_specific_semantic_acceptance_not_closed_by_generic_gates |
| CONTRACT-05 | 5. Slot: มีทั้งบทบาทและเจ้าของ | implementation_evidence_and_measurement_present_acceptance_open | resource_scope_and_actor_owner_gaps |
| CONTRACT-06 | 6. SharedBinding | implementation_evidence_and_measurement_present_acceptance_open | event_scope_lost_across_needs; resolved_anaphor_still_clarified |
| CONTRACT-07 | 7. ตัวอย่างแผนเชิงโครงสร้างจากคำถาม VR เดิม | implementation_evidence_and_measurement_present_acceptance_open | requirement_specific_semantic_acceptance_not_closed_by_generic_gates |
| CONTRACT-08 | 8. Capability และ ExecutorResult | implementation_evidence_and_measurement_present_acceptance_open | capability_presence_not_semantic_completeness |
| CONTRACT-09 | 9. EvidenceReceipt และ CalculationReceipt | implementation_evidence_and_measurement_present_acceptance_open | source_receipt_not_predicate_entailment |
| CONTRACT-10 | 10. AuthorityResolution | implementation_evidence_and_measurement_present_acceptance_open | equivalence_and_temporal_authority_review |
| CONTRACT-11 | 11. ObligationLedger และ VerifierResult | implementation_evidence_and_measurement_present_acceptance_open | substantive_clause_false_rejection; whole_question_coverage_gaps |
| CONTRACT-12 | 12. Terminal states และข้อความถึงผู้ใช้ | implementation_evidence_and_measurement_present_acceptance_open | unavailable_reason_conflation |
| CONTRACT-13 | 13. ModelGateway และ BudgetLedger | implementation_evidence_and_measurement_present_acceptance_open | busy_timeout_stage_admission |
| CONTRACT-14 | Wire format เทียบกับ internal plan | implementation_evidence_and_measurement_present_acceptance_open | HF_format_not_enforced; explicit_JSON_version_prompt_gap |
| CONTRACT-15 | 14. TrainingExample และ ReviewRecord | training_procedure_evidence_complete_not_answer_accuracy | new_adapter_semantic_promotion_rejected_no_business_data_retraining_needed |
| CONTRACT-16 | 15. การย้ายจาก R122 | implementation_evidence_and_measurement_present_acceptance_open | requirement_specific_semantic_acceptance_not_closed_by_generic_gates |
| PHASE-01 | 1. ขอบเขตและหลักฐานฐานตั้งต้น | implementation_evidence_and_measurement_present_acceptance_open | requirement_specific_semantic_acceptance_not_closed_by_generic_gates |
| PHASE-03 | P0 — Freeze contracts และ capability coverage ทั้ง 14 หมวด | implementation_evidence_and_measurement_present_acceptance_open | requirement_specific_semantic_acceptance_not_closed_by_generic_gates |
| PHASE-04 | P1 — สร้าง task graph, slot ownership และ verifier ก่อนต่อโมเดลใหม่ | implementation_evidence_and_measurement_present_acceptance_open | requirement_specific_semantic_acceptance_not_closed_by_generic_gates |
| PHASE-05 | P2 — ต่อ executors เดิมเข้ากับ contracts ใหม่ให้ครบหมวด | implementation_evidence_and_measurement_present_acceptance_open | requirement_specific_semantic_acceptance_not_closed_by_generic_gates |
| PHASE-06 | P3 — แก้ data/compiler/authority ที่จำเป็น | implementation_evidence_and_measurement_present_acceptance_open | requirement_specific_semantic_acceptance_not_closed_by_generic_gates |
| PHASE-07 | P4 — ตรวจชุดสอนทั้งชุดและสร้าง teacher plan labels | training_procedure_evidence_complete_not_answer_accuracy | new_adapter_semantic_promotion_rejected_no_business_data_retraining_needed |
| PHASE-08 | P5 — Freeze การแบ่งข้อมูลและ metric ก่อนฝึก | training_procedure_evidence_complete_not_answer_accuracy | new_adapter_semantic_promotion_rejected_no_business_data_retraining_needed |
| PHASE-09 | P6 — ฝึก planner ใหม่อย่างมีเหตุผล | training_procedure_evidence_complete_not_answer_accuracy | new_adapter_semantic_promotion_rejected_no_business_data_retraining_needed |
| PHASE-10 | P7 — วัดสามแขนบน engine เดียวกัน | paired_measurement_and_agent_retained_selection_complete | new_weights_not_promoted; retained_protocol_and_execution_gaps_remain |
| PHASE-11 | P8 — ตรวจ readiness และพิจารณาการวัดขนาดใหญ่ | measurement_reporting_complete_quality_acceptance_not_complete | requirement_specific_semantic_acceptance_not_closed_by_generic_gates |
| PHASE-13 | 3.1 Planner metrics | paired_measurement_and_agent_retained_selection_complete | new_weights_not_promoted; retained_protocol_and_execution_gaps_remain |
| PHASE-14 | 3.2 Executor/verifier metrics | measurement_reporting_complete_quality_acceptance_not_complete | requirement_specific_semantic_acceptance_not_closed_by_generic_gates |
| PHASE-15 | 3.3 End-to-end answer metrics | measurement_reporting_complete_quality_acceptance_not_complete | requirement_specific_semantic_acceptance_not_closed_by_generic_gates |
| PHASE-16 | 3.4 Legacy benchmark | saved_baseline_fixed_identity_comparison_complete | source_backend_precision_clock_deadline_confounds; semantic_accuracy_not_inferred |
| PHASE-17 | 4. เกณฑ์ตัดสินว่าจะใช้ adapter ใหม่หรือไม่ | paired_measurement_and_agent_retained_selection_complete | new_weights_not_promoted; retained_protocol_and_execution_gaps_remain |
| PHASE-18 | 5. แผนที่ module สำหรับ implementation | reference_scope_retained_measurement_linked | requirement_specific_semantic_acceptance_not_closed_by_generic_gates |
| PHASE-19 | 6. ความเสี่ยงและวิธีป้องกันในการพัฒนา | implementation_evidence_and_measurement_present_acceptance_open | requirement_specific_semantic_acceptance_not_closed_by_generic_gates |
| PHASE-20 | 7. หลักฐานที่ต้องส่งเมื่อ implement เสร็จ | measurement_reporting_complete_quality_acceptance_not_complete | requirement_specific_semantic_acceptance_not_closed_by_generic_gates |
| PHASE-21 | 8. ที่มาของแนวทางและขอบเขตการอ้าง | reference_scope_retained_measurement_linked | requirement_specific_semantic_acceptance_not_closed_by_generic_gates |
