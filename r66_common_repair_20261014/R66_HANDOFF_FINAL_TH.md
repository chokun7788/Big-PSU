# PSU Chatbot — R66 handoff หลังรอบ final20

## โปรเจกต์จริงและผลนำกลับ

ROOT: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data`; code files 31; protected DB hashes unchanged = True; ไม่ได้ restart เว็บที่เปิดค้างหรืออัปเดต portable packages

[APPLIED.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r66_common_repair_20261014/DEPLOY_final20/APPLIED.json); backups อยู่ใน before/app; rollback_verified_code.py มี hash guard ต้องไม่ลบทับ user changes หลัง deployment

## Candidate

ร่าง 588 heads (582 เดิม + PC source-recovered rates 6) อยู่ที่ [candidate.sqlite](C:/Users/Chokhun/Downloads/Learn-LLM/18_PSU_Esports_Update_Route_Data/data/knowledge/migration_r66_20261015/candidate.sqlite); SHA eaadf67aaa324fd64a7ebdbea0769c25cc8ca115bb2a2758026e99de1fffc1be; approvals 0; active release ว่าง; synthetic sources 0 ข้อมูลนี้ไม่แทน approved.sqlite default

## ผลทดสอบล่าสุด

common OFF/ON เท่านั้น; [VERIFIED_final20.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r66_common_repair_20261014/VERIFIED_final20.json); app/data frozen; ไม่ใช่ full 20,554 sweep; 223 selected requests / 503 legacy grades ต่อ mode; มี 480 canonical new-category requests ต่อ modeซึ่งไม่ใช้ model และไม่พิสูจน์ทุก paraphrase

- off: {'requests': 223, 'exceptions': 0, 'validation_rejected_requests': 0, 'grades': 503, 'strict_pass': 133, 'failed_grades': 370, 'content_contract_failed_grades': 30, 'protocol_outcome_failed_grades': 362, 'protocol_outcome_only_failed_grades': 284, 'presentation_failed_grades': 30, 'source_alignment_failed_grades': 39, 'performance_failed_grades': 1}; locale = {'th': {'grades': 324, 'strict_pass': 90}, 'en': {'grades': 179, 'strict_pass': 43}}; model trace observations = {}
- llm: {'requests': 223, 'exceptions': 0, 'validation_rejected_requests': 0, 'grades': 503, 'strict_pass': 125, 'failed_grades': 378, 'content_contract_failed_grades': 32, 'protocol_outcome_failed_grades': 370, 'protocol_outcome_only_failed_grades': 290, 'presentation_failed_grades': 30, 'source_alignment_failed_grades': 39, 'locale_marker_failed_grades': 1, 'performance_failed_grades': 1}; locale = {'th': {'grades': 324, 'strict_pass': 83}, 'en': {'grades': 179, 'strict_pass': 42}}; model trace observations = {'trace_observations': 22, 'attempted': 22, 'transport_ok': 20, 'transport_not_ok': 2, 'schema_accepted': 18, 'final_field_plan_accepted': 0, 'semantic_selection_rejected': 0}

Native common tests 84 มี raw assertion mismatches 2 ข้อจาก contract เก่า เก็บไว้ ไม่เรียกว่า all green; versioned semantic contracts 4 ข้อแยก positive/negative; targeted gates ดู VERIFIED

## การแก้เพิ่มท้ายรอบ

- K: damage fine vs service price, paid manual cancellation vs unpaid timeout, timed occupancy vs installed games
- L/M: damage EN fine ranges; control-note omission 390 rows / 36 records แปลครบเป็นร่าง อ่านคู่ไทย/อังกฤษและแก้ข้อเสนอเพิ่ม 64 จุด; raw proposals/CALLS กับ reviewed copies เก็บแยก; no owner approval
- N: early no-independent-topic-anchor guard และ source-based personal power policy
- O: source-based return-equipment policy; ห้ามอ่าน ID เป็น question; underscore experiment ถูกปฏิเสธและโค้ดนั้นไม่ได้ deploy

## งานที่ยังขาด facts/การยืนยัน

อ่าน [OWNER_CONFIRMATION_REQUIRED_TH.md](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r66_common_repair_20261014/OWNER_CONFIRMATION_REQUIRED_TH.md) และ [PUBLICATION_BLOCKERS_TH.md](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r66_common_repair_20261014/PUBLICATION_BLOCKERS_TH.md); 588 records ยัง blocked publication อย่าเปิด evaluation draft override ใน production หรือสร้าง owner attestation/approvals แทนเขา

บาง core fields เป็น migration metadata ที่เสนอจาก source ได้ (facet/completeness) บางช่องต้องมีข้อมูลเพิ่ม (validity/preset/gesture/conditions); อย่าเหมารวมว่าทุกช่องต้องถามมนุษย์ หรือเดาค่าที่ไม่มี source ให้ผ่าน schema

ราคาเดิมที่หมดอายุ/PC effective date unknown ยังไม่ใช่ current price; คำแปลส่วนอื่นที่ยังไม่ได้ตรวจรายช่องไม่มี semantic guarantee; model transport กับความถูกต้องของเนื้อหาต้องแยกต่อไป

ผู้ใช้ยืนยันแล้ว: booking truth เดิม, lunch 12–13 no booking, VR30 occupies whole hour; ไม่ต้องถามซ้ำและไม่มี real booking oracle ใหม่ใน R66

## ไฟล์หลัก

- [R66_FINAL_REPORT_TH.md](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r66_common_repair_20261014/R66_FINAL_REPORT_TH.md)
- [FLOW_R66_COMPLETE_TH.md](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r66_common_repair_20261014/FLOW_R66_COMPLETE_TH.md)
- [REPAIR_LEDGER_TH.md](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r66_common_repair_20261014/REPAIR_LEDGER_TH.md)
- [REMAINING_FAILURE_ANALYSIS_TH.md](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r66_common_repair_20261014/REMAINING_FAILURE_ANALYSIS_TH.md)
- [TRANSLATION_FAILURE_TAXONOMY_TH.md](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r66_common_repair_20261014/TRANSLATION_FAILURE_TAXONOMY_TH.md)
- [ALL_FAILED_GRADES.md](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r66_common_repair_20261014/AUDIT_final20/ALL_FAILED_GRADES.md)

## รักษางานเดิม

ไม่เขียนทับ R64/R65 results/logs, original ROOT approved.sqlite/R63 migration DB หรือ approvals; untracked R63 folder เดิมยังอยู่ R66 candidate ใหม่แยก folder; ไม่ commit/reset/clean Git

หลังมีการแก้ app/data อีก ผล final20 เป็นประวัติ ไม่ใช่ผลของโค้ดใหม่ ต้องแยก tag/snapshot และไม่อ้างว่ารันทดสอบ legacy อีก
