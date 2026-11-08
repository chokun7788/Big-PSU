# Smokeทั้งหมดและเหตุที่ต้องตรวจ

exitcode0รับรองว่าสคริปต์ผ่านเกณฑ์ของตัวเอง; exitcode1ต้องอ่านassertionและconfig ไม่เท่ากับคำตอบผิดทุกครั้ง

## 1. legacy / smoke_test_accented_english_game_routing.py

{"file": "smoke_test_accented_english_game_routing.py", "status": "passed", "exit_code": 0, "elapsed": 13.780170799931511}

[smoke_test_accented_english_game_routing.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_accented_english_game_routing.log)
## 2. legacy / smoke_test_adaptive_intent_gate.py

{"file": "smoke_test_adaptive_intent_gate.py", "status": "passed", "exit_code": 0, "elapsed": 7.348811100004241}

[smoke_test_adaptive_intent_gate.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_adaptive_intent_gate.log)
## 3. legacy / smoke_test_ambiguity_gate.py

{"file": "smoke_test_ambiguity_gate.py", "status": "failed", "exit_code": 1, "elapsed": 15.593795999884605}

[smoke_test_ambiguity_gate.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_ambiguity_gate.log)

```text
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_ambiguity_gate.py", line 189, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_ambiguity_gate.py", line 103, in main
    assert_contains(result.answer, ["ขอชื่อเกมก่อน", "TEKKEN 8"], "control query missing game clarification")
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_ambiguity_gate.py", line 19, in assert_contains
    raise AssertionError(f"{label}: missing {missing}\n{text}")
AssertionError: control query missing game clarification: missing ['ขอชื่อเกมก่อน', 'TEKKEN 8']
ต้องการดูปุ่มควบคุมของเกมใดครับ? พิมพ์ชื่อเกมที่ต้องการได้เลยครับ
```
## 4. legacy / smoke_test_answer_formatting.py

{"file": "smoke_test_answer_formatting.py", "status": "passed", "exit_code": 0, "elapsed": 17.017593099968508}

[smoke_test_answer_formatting.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_answer_formatting.log)
## 5. legacy / smoke_test_answer_pipeline.py

{"file": "smoke_test_answer_pipeline.py", "status": "failed", "exit_code": 1, "elapsed": 28.4292433001101}

[smoke_test_answer_pipeline.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_answer_pipeline.log)

```text
    raise AssertionError(f"{question}: missing {missing}\n{result.answer}")
AssertionError: มีให้เช่าจอไปบ้านไหม: missing ['ไม่พบข้อมูล']
ราคาเช่าเหมาโซนสำหรับหน่วยงาน

ยังไม่มีราคาเช่าเหมาในไฟล์สำหรับรายการที่ระบุ: จอไปบ้านไหม

อัตรานี้เป็นราคาเช่าเหมาโซนของหน่วยงาน ไม่ใช่ราคาต่อผู้เล่น/เครื่อง ไฟล์ไม่ได้ระบุจำนวนชั่วโมงของช่วงเช่าหรือวันที่มีผลของอัตรา

แหล่งข้อมูล: ไฟล์ค่าบริการครึ่งวันและเต็มวันที่ผู้ใช้ส่งให้
local://service_fee/zone_rental_fees_20261006
```
## 6. legacy / smoke_test_answer_validator.py

{"file": "smoke_test_answer_validator.py", "status": "passed", "exit_code": 0, "elapsed": 4.557500999886543}

[smoke_test_answer_validator.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_answer_validator.log)
## 7. legacy / smoke_test_audit_regressions.py

{"file": "smoke_test_audit_regressions.py", "status": "failed", "exit_code": 1, "elapsed": 13.59643719997257}

[smoke_test_audit_regressions.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_audit_regressions.log)

```text
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_audit_regressions.py", line 70, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_audit_regressions.py", line 31, in main
    assert_contains(result.answer, ["RoV", "MOBA"], "rov detail")
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_audit_regressions.py", line 19, in assert_contains
    raise AssertionError(f"{label}: missing {missing}\n{text}")
AssertionError: rov detail: missing ['RoV', 'MOBA']
คำถามนี้มีได้หลายความหมายครับ ขอระบุเพิ่มนิดหนึ่งว่าต้องการถามเรื่องไหน: รายชื่อเกม/ข้อมูลเกม
```
## 8. legacy / smoke_test_availability_policy_regressions.py

{"file": "smoke_test_availability_policy_regressions.py", "status": "failed", "exit_code": 1, "elapsed": 27.51728170015849}

[smoke_test_availability_policy_regressions.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_availability_policy_regressions.log)

```text
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_availability_policy_regressions.py", line 135, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_availability_policy_regressions.py", line 116, in main
    check(
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_availability_policy_regressions.py", line 33, in check
    raise AssertionError(f"{question}: category {result.route.category} != {category}\n{result.answer}")
AssertionError: ถ้าจะเล่น Call of Duty ต้องจองอะไร: category clarification != reservation
กรุณาระบุชื่อเกมและภาคให้ชัดเจนครับ ยังเลือกบริการให้ไม่ได้จนกว่าจะพบเกมที่ตรงกับรายการบริการที่ยืนยันได้
```
## 9. legacy / smoke_test_bilingual_locale.py

{"file": "smoke_test_bilingual_locale.py", "status": "passed", "exit_code": 0, "elapsed": 3.5237743998877704}

[smoke_test_bilingual_locale.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_bilingual_locale.log)
## 10. legacy / smoke_test_bilingual_pipeline.py

{"file": "smoke_test_bilingual_pipeline.py", "status": "failed", "exit_code": 1, "elapsed": 11.57168999989517}

[smoke_test_bilingual_pipeline.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_bilingual_pipeline.log)

```text
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_bilingual_pipeline.py", line 352, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_bilingual_pipeline.py", line 55, in main
    assert catalog.mode == "pipeline:structured_games_catalog_en"
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError
```
## 11. legacy / smoke_test_bilingual_web_api.py

{"file": "smoke_test_bilingual_web_api.py", "status": "deferred_actual_http_suite", "reason": "Will run against isolated evaluation web servers, not user server"}

[SUMMARY.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_http_protocol_network/SUMMARY.json)

```text
รันผ่านactual HTTP suiteแยก
```
## 12. legacy / smoke_test_booking_policy_rag_gate.py

{"file": "smoke_test_booking_policy_rag_gate.py", "status": "passed", "exit_code": 0, "elapsed": 2.8810117999091744}

[smoke_test_booking_policy_rag_gate.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_booking_policy_rag_gate.log)
## 13. legacy / smoke_test_booking_price_regression.py

{"file": "smoke_test_booking_price_regression.py", "status": "passed", "exit_code": 0, "elapsed": 22.263706299941987}

[smoke_test_booking_price_regression.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_booking_price_regression.log)
## 14. legacy / smoke_test_boundary_guard.py

{"file": "smoke_test_boundary_guard.py", "status": "failed", "exit_code": 1, "elapsed": 17.352365399943665}

[smoke_test_boundary_guard.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_boundary_guard.log)

```text
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_boundary_guard.py", line 80, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_boundary_guard.py", line 46, in main
    assert mixed.mode == "pipeline:multi_question_splitter", mixed.mode
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: pipeline:structured_service_fee_conversation
```
## 15. legacy / smoke_test_broad_competition_rag_route.py

{"file": "smoke_test_broad_competition_rag_route.py", "status": "passed", "exit_code": 0, "elapsed": 1.926938699791208}

[smoke_test_broad_competition_rag_route.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_broad_competition_rag_route.log)
## 16. legacy / smoke_test_canonical_content.py

{"file": "smoke_test_canonical_content.py", "status": "failed", "exit_code": 1, "elapsed": 2.3544595998246223}

[smoke_test_canonical_content.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_canonical_content.log)

```text
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_canonical_content.py", line 33, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_canonical_content.py", line 20, in main
    assert manifest["record_count"] == len(records)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError
```
## 17. legacy / smoke_test_canonical_publish_gate.py

{"file": "smoke_test_canonical_publish_gate.py", "status": "passed", "exit_code": 0, "elapsed": 2.061859800014645}

[smoke_test_canonical_publish_gate.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_canonical_publish_gate.log)
## 18. legacy / smoke_test_canonical_rag_integration.py

{"file": "smoke_test_canonical_rag_integration.py", "status": "failed", "exit_code": 1, "elapsed": 2.2333209000062197}

[smoke_test_canonical_rag_integration.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_canonical_rag_integration.log)

```text
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_canonical_rag_integration.py", line 66, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_canonical_rag_integration.py", line 27, in main
    game_hits, _ = retrieve_curated("VALORANT เล่นยังไง", "games", limit=3)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\retrieval.py", line 900, in retrieve_curated
    return hits, PipelineTrace("rag_retrieval", "curated_lexical", confidence, detail, {"category": category, "game": competition_game, "intent": competition_intent,"common_ownership_blocked":ownership_blocked})
                                                                                                                                                                                                ^^^^^^^^^^^^^^^^^
NameError: name 'ownership_blocked' is not defined
```
## 19. legacy / smoke_test_chat_logger_postgres.py

{"file": "smoke_test_chat_logger_postgres.py", "status": "passed", "exit_code": 0, "elapsed": 0.6029846000019461}

[smoke_test_chat_logger_postgres.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_chat_logger_postgres.log)
## 20. legacy / smoke_test_chat_logger_sqlite.py

{"file": "smoke_test_chat_logger_sqlite.py", "status": "passed", "exit_code": 0, "elapsed": 0.6513678000774235}

[smoke_test_chat_logger_sqlite.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_chat_logger_sqlite.log)
## 21. legacy / smoke_test_chat_quality_metrics.py

{"file": "smoke_test_chat_quality_metrics.py", "status": "passed", "exit_code": 0, "elapsed": 0.45629299990832806}

[smoke_test_chat_quality_metrics.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_chat_quality_metrics.log)
## 22. legacy / smoke_test_compact_intent_prompt.py

{"file": "smoke_test_compact_intent_prompt.py", "status": "passed", "exit_code": 0, "elapsed": 0.7647494000848383}

[smoke_test_compact_intent_prompt.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_compact_intent_prompt.log)
## 23. legacy / smoke_test_competition_signal_priority.py

{"file": "smoke_test_competition_signal_priority.py", "status": "failed", "exit_code": 1, "elapsed": 12.347441100049764}

[smoke_test_competition_signal_priority.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_competition_signal_priority.log)

```text
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 3565, in _answer_single
    source_hits, source_trace = retrieve_curated(
                                ^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\retrieval.py", line 900, in retrieve_curated
    return hits, PipelineTrace("rag_retrieval", "curated_lexical", confidence, detail, {"category": category, "game": competition_game, "intent": competition_intent,"common_ownership_blocked":ownership_blocked})
                                                                                                                                                                                                ^^^^^^^^^^^^^^^^^
NameError: name 'ownership_blocked' is not defined
```
## 24. legacy / smoke_test_compound_execution.py

{"file": "smoke_test_compound_execution.py", "status": "failed", "exit_code": 1, "elapsed": 11.289996899897233}

[smoke_test_compound_execution.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_compound_execution.log)

```text
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_compound_execution.py", line 111, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_compound_execution.py", line 69, in main
    assert "bounded_parallel" in _decisions(result, "compound_child_execution"), result.trace
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: [PipelineTrace(stage='timing', decision='locale_resolution', confidence=1.0, detail='', metadata={'elapsed_ms': 0.16, 'elapsed_sec': 0.0002, 'global_timeout_enabled': True, 'global_timeout_sec': 10.0, 'global_elapsed_sec': 0.0002, 'global_remaining_sec': 9.9998, 'finalizer_reserve_sec': 1.0, 'work_remaining_sec': 8.9998, 'timing_status': 'running'}), PipelineTrace(stage='timing', decision='intent_cue_preflight', confidence=1.0, detail='', metadata={'elapsed_ms': 79.92, 'elapsed_sec': 0.0799, 'global_timeout_enabled': True, 'global_timeout_sec': 10.0, 'global_elapsed_sec': 5.73, 'global_remaining_sec': 4.27, 'finalizer_reserve_sec': 1.0, 'work_remaining_sec': 3.27, 'timing_status': 'running'}), PipelineTrace(stage='conversation_request', decision='new_task', confidence=1.0, detail='typed slots preserve user filters; assistant options are not selections', metadata={'request_plan': {'schema_version': 1, 'original_query': 'PC ราคาเท่าไหร่ แล้วจองยังไง', 'resolved_query': 'ค่าบริการ PC', 'act': 'new_task', 'tasks': [{'tas … [ย่อจาก5,844ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```
## 25. legacy / smoke_test_compound_question_planner.py

{"file": "smoke_test_compound_question_planner.py", "status": "failed", "exit_code": 1, "elapsed": 20.37477759993635}

[smoke_test_compound_question_planner.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_compound_question_planner.log)

```text

คำถามที่ 2: VR มีเกมอะไร
เกมที่มีข้อมูลยืนยันในโซนที่ถาม

VR Zone (4 เกม)
•    Beat Saber
•    Horizon Call of the Mountain
•    Resident Evil 4
•    Resident Evil Village
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games
```
## 26. legacy / smoke_test_control_catalog_coverage.py

{"file": "smoke_test_control_catalog_coverage.py", "status": "passed", "exit_code": 0, "elapsed": 1.2275366000831127}

[smoke_test_control_catalog_coverage.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_control_catalog_coverage.log)
## 27. legacy / smoke_test_correctness_control_flow_v1.py

{"file": "smoke_test_correctness_control_flow_v1.py", "status": "failed", "exit_code": 1, "elapsed": 6.012696499936283}

[smoke_test_correctness_control_flow_v1.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_correctness_control_flow_v1.log)

```text
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_correctness_control_flow_v1.py", line 193, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_correctness_control_flow_v1.py", line 92, in main
    assert not no_controls.top_candidate.has_controls
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError
```
## 28. legacy / smoke_test_decision_artifact.py

{"file": "smoke_test_decision_artifact.py", "status": "failed", "exit_code": 1, "elapsed": 10.969758100109175}

[smoke_test_decision_artifact.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_decision_artifact.log)

```text
    runpy.run_path(str(p),run_name='__main__')
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_decision_artifact.py", line 76, in <module>
    test_structured_question_has_decision_artifact()
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_decision_artifact.py", line 29, in test_structured_question_has_decision_artifact
    assert artifact["intent"]["domain"] == "members"
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError
```
## 29. legacy / smoke_test_english_compound_split.py

{"file": "smoke_test_english_compound_split.py", "status": "failed", "exit_code": 1, "elapsed": 10.821828300133348}

[smoke_test_english_compound_split.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_english_compound_split.log)

```text
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_english_compound_split.py", line 48, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_english_compound_split.py", line 30, in main
    assert combined.route.category == "multi_question", combined.route
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: PipelineRoute(category='service_fee', intent='conversation_price_lookup', confidence=0.98, answer_type='fact', risk='medium', reason='typed service and customer filters with source-bound coverage')
```
## 30. legacy / smoke_test_english_date_aware_schedule.py

{"file": "smoke_test_english_date_aware_schedule.py", "status": "passed", "exit_code": 0, "elapsed": 1.4997950999531895}

[smoke_test_english_date_aware_schedule.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_english_date_aware_schedule.log)
## 31. legacy / smoke_test_english_draft_preview.py

{"file": "smoke_test_english_draft_preview.py", "status": "failed", "exit_code": 1, "elapsed": 13.52571040019393}

[smoke_test_english_draft_preview.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_english_draft_preview.log)

```text
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_english_draft_preview.py", line 54, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_english_draft_preview.py", line 33, in main
    assert competition.mode == "pipeline:structured_competition_rules_en", competition
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: PipelineAnswer(answer='Selected Arena of Valor (RoV) competition rules from the recorded rulebook:\nTournament: Arena of Valor (RoV) / 2025\n\n\n**Competition format**\n•    1.1. Offline event on September 11, 2025 · Registration: 8:00–8:30 AM · Draw of brackets: 8:30–8:40 AM · Round of 5 teams, Single Elimination BO3: 8:40–10:00 AM · Semifinal Match 1, Single Elimination BO3: 10:00–11:30 AM · Semifinal Match 2, Single Elimination BO3: 12:30–2:00 PM · Bronze Medal Match, Single Elimination BO3: 2:00–3:30 PM · Grand Final, Single Elimination BO3: 3:30–5:00 PM\n\n**Eligibility and registration**\n•    6.1.3. No team may allow any individual not listed on their official roster to participate in the competition. If it is discovered that a competitor’s name does not match the registered list, evidence must be recorded and the match shall be terminated immediately. However, if the match proceeds to completion, both teams shall be deemed to have consented to the competition, and no appeals will be entertained by the organizing team … [ย่อจาก17,014ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```
## 32. legacy / smoke_test_english_format_parity_fixes.py

{"file": "smoke_test_english_format_parity_fixes.py", "status": "failed", "exit_code": 1, "elapsed": 14.352545300032943}

[smoke_test_english_format_parity_fixes.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_english_format_parity_fixes.log)

```text
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_english_format_parity_fixes.py", line 49, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_english_format_parity_fixes.py", line 40, in main
    assert "Official Thai source member record" in manager.answer
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError
```
## 33. legacy / smoke_test_english_game_target_priority.py

{"file": "smoke_test_english_game_target_priority.py", "status": "passed", "exit_code": 0, "elapsed": 15.89598589995876}

[smoke_test_english_game_target_priority.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_english_game_target_priority.log)
## 34. legacy / smoke_test_english_localization_registry.py

{"file": "smoke_test_english_localization_registry.py", "status": "passed", "exit_code": 0, "elapsed": 0.8682951000519097}

[smoke_test_english_localization_registry.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_english_localization_registry.log)
## 35. legacy / smoke_test_english_localization_review_workflow.py

{"file": "smoke_test_english_localization_review_workflow.py", "status": "passed", "exit_code": 0, "elapsed": 0.7255629000719637}

[smoke_test_english_localization_review_workflow.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_english_localization_review_workflow.log)
## 36. legacy / smoke_test_entity_reranker_gate.py

{"file": "smoke_test_entity_reranker_gate.py", "status": "passed", "exit_code": 0, "elapsed": 2.8414117000065744}

[smoke_test_entity_reranker_gate.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_entity_reranker_gate.log)
## 37. legacy / smoke_test_entity_resolver_v2.py

{"file": "smoke_test_entity_resolver_v2.py", "status": "failed", "exit_code": 1, "elapsed": 14.2604568998795}

[smoke_test_entity_resolver_v2.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_entity_resolver_v2.log)

```text
    runpy.run_path(str(p),run_name='__main__')
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_entity_resolver_v2.py", line 70, in <module>
    test_pipeline_clarifies_family_controls_but_allows_family_list()
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_entity_resolver_v2.py", line 56, in test_pipeline_clarifies_family_controls_but_allows_family_list
    assert mario_list.mode == "pipeline:structured_games_family", mario_list.mode
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: pipeline:source_operation_game_list
```
## 38. legacy / smoke_test_facts_composer.py

{"file": "smoke_test_facts_composer.py", "status": "passed", "exit_code": 0, "elapsed": 0.6337383999489248}

[smoke_test_facts_composer.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_facts_composer.log)
## 39. legacy / smoke_test_fast_runtime.py

{"file": "smoke_test_fast_runtime.py", "status": "passed", "exit_code": 0, "elapsed": 5.116721499944106}

[smoke_test_fast_runtime.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_fast_runtime.log)
## 40. legacy / smoke_test_full_eval_regression_fixes.py

{"file": "smoke_test_full_eval_regression_fixes.py", "status": "passed", "exit_code": 0, "elapsed": 25.90884659998119}

[smoke_test_full_eval_regression_fixes.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_full_eval_regression_fixes.log)
## 41. legacy / smoke_test_game_catalog.py

{"file": "smoke_test_game_catalog.py", "status": "failed", "exit_code": 1, "elapsed": 15.436944300075993}

[smoke_test_game_catalog.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_game_catalog.log)

```text
    runpy.run_path(str(p),run_name='__main__')
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_game_catalog.py", line 139, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_game_catalog.py", line 72, in main
    raise AssertionError("surface variant should receive bounded Local LLM intent review")
AssertionError: surface variant should receive bounded Local LLM intent review
```
## 42. legacy / smoke_test_game_controls.py

{"file": "smoke_test_game_controls.py", "status": "failed", "exit_code": 1, "elapsed": 20.226472500013188}

[smoke_test_game_controls.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_game_controls.log)

```text
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_game_controls.py", line 126, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_game_controls.py", line 67, in main
    check(
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_game_controls.py", line 37, in check
    raise AssertionError(f"{question}: expected mode {mode}, got {result.mode}")
AssertionError: มาริโอคาร์ทไลฟ์ปุ่มเร่งเครื่องกดอะไร: expected mode pipeline:structured_game_controls_no_current_game, got pipeline:source_operation_control_lookup
```
## 43. legacy / smoke_test_game_title_typo_correction.py

{"file": "smoke_test_game_title_typo_correction.py", "status": "failed", "exit_code": 1, "elapsed": 20.03428900009021}

[smoke_test_game_title_typo_correction.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_game_title_typo_correction.log)

```text

Cockpit Zone (1 เกม)
•    Gran Turismo 7

VR Zone (4 เกม)
•    Beat Saber
•    Horizon Call of the Mountain
•    Resident Evil 4
•    Resident Evil Village
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games
```
## 44. legacy / smoke_test_genre_alias_formatting.py

{"file": "smoke_test_genre_alias_formatting.py", "status": "failed", "exit_code": 1, "elapsed": 17.332155800191686}

[smoke_test_genre_alias_formatting.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_genre_alias_formatting.log)

```text

Cockpit Zone (1 เกม)
•    Gran Turismo 7

VR Zone (4 เกม)
•    Beat Saber
•    Horizon Call of the Mountain
•    Resident Evil 4
•    Resident Evil Village
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games
```
## 45. legacy / smoke_test_keyboard_input_anomaly.py

{"file": "smoke_test_keyboard_input_anomaly.py", "status": "passed", "exit_code": 0, "elapsed": 0.676622100174427}

[smoke_test_keyboard_input_anomaly.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_keyboard_input_anomaly.log)
## 46. legacy / smoke_test_live_booking_status.py

{"file": "smoke_test_live_booking_status.py", "status": "failed", "exit_code": 1, "elapsed": 6.241817599860951}

[smoke_test_live_booking_status.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_live_booking_status.log)

```text
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_live_booking_status.py", line 352, in test_english_plural_zone_questions_stay_scoped_and_list_all_resources
    self.assertEqual(answer.count("•    "), expected_rows)
AssertionError: 4 != 5

----------------------------------------------------------------------
Ran 17 tests in 4.553s

FAILED (failures=3)
```
## 47. legacy / smoke_test_live_canonical_semantic_rag.py

{"file": "smoke_test_live_canonical_semantic_rag.py", "status": "passed", "exit_code": 0, "elapsed": 8.833421500166878}

[smoke_test_live_canonical_semantic_rag.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_live_canonical_semantic_rag.log)
## 48. legacy / smoke_test_llm_budget_and_fast_split.py

{"file": "smoke_test_llm_budget_and_fast_split.py", "status": "passed", "exit_code": 0, "elapsed": 1.5369690000079572}

[smoke_test_llm_budget_and_fast_split.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_llm_budget_and_fast_split.log)
## 49. legacy / smoke_test_llm_concurrency.py

{"file": "smoke_test_llm_concurrency.py", "status": "passed", "exit_code": 0, "elapsed": 0.9452598998323083}

[smoke_test_llm_concurrency.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_llm_concurrency.log)
## 50. legacy / smoke_test_llm_health_circuit_breaker.py

{"file": "smoke_test_llm_health_circuit_breaker.py", "status": "failed", "exit_code": 1, "elapsed": 2.0619337998796254}

[smoke_test_llm_health_circuit_breaker.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_llm_health_circuit_breaker.log)

```text
    runpy.run_path(str(p),run_name='__main__')
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_llm_health_circuit_breaker.py", line 258, in <module>
    test_general_fallback_skips_when_circuit_open()
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_llm_health_circuit_breaker.py", line 80, in test_general_fallback_skips_when_circuit_open
    assert fallback.mode == "general_llm_unavailable"
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError
```
## 51. legacy / smoke_test_llm_timing_and_general_guard.py

{"file": "smoke_test_llm_timing_and_general_guard.py", "status": "failed", "exit_code": 1, "elapsed": 26.946267700055614}

[smoke_test_llm_timing_and_general_guard.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_llm_timing_and_general_guard.log)

```text
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\experimental_fallback.py", line 259, in _retrieve_experimental_rows
    hybrid_rows, hybrid_trace = retrieve_hybrid_guarded(
                                ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\hybrid_retrieval.py", line 204, in retrieve_hybrid_guarded
    curated_hits, curated_trace = retrieve_curated(query, route.category, limit=candidate_limit)
                                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\retrieval.py", line 900, in retrieve_curated
    return hits, PipelineTrace("rag_retrieval", "curated_lexical", confidence, detail, {"category": category, "game": competition_game, "intent": competition_intent,"common_ownership_blocked":ownership_blocked})
                                                                                                                                                                                                ^^^^^^^^^^^^^^^^^
NameError: name 'ownership_blocked' is not defined
```
## 52. legacy / smoke_test_llm_tool_router.py

{"file": "smoke_test_llm_tool_router.py", "status": "failed", "exit_code": 1, "elapsed": 38.159468999831006}

[smoke_test_llm_tool_router.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_llm_tool_router.log)

```text
    runpy.run_path(str(p),run_name='__main__')
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_llm_tool_router.py", line 152, in <module>
    test_engine_can_refine_general_to_retrieval_route()
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_llm_tool_router.py", line 142, in test_engine_can_refine_general_to_retrieval_route
    assert result.route.category == "competition_rules"
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError
```
## 53. legacy / smoke_test_members_and_game_knowledge.py

{"file": "smoke_test_members_and_game_knowledge.py", "status": "failed", "exit_code": 1, "elapsed": 25.476889500161633}

[smoke_test_members_and_game_knowledge.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_members_and_game_knowledge.log)

```text
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_members_and_game_knowledge.py", line 130, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_members_and_game_knowledge.py", line 44, in main
    check(
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_members_and_game_knowledge.py", line 21, in check
    raise AssertionError(f"{question}: missing {missing}\n{answer}")
AssertionError: สมาชิกทีมมีใครบ้าง: missing ['Members', 'cooperative education and Internship student', 'PSU Phuket Esports Club - PSU Phuket', 'นายชนะชัย', 'นายษุภากรณ์']
เงื่อนไขสมาชิกของศูนย์ใช้แทนข้อกำหนดบัญชีเกมหรือสมาชิกทีมไม่ได้ครับ ต้องตรวจข้อกำหนดของบัญชีเกมหรือรายการแข่งขันนั้นแยกกัน
```
## 54. legacy / smoke_test_model_first_rag_flow.py

{"file": "smoke_test_model_first_rag_flow.py", "status": "failed", "exit_code": 1, "elapsed": 3.9197019999846816}

[smoke_test_model_first_rag_flow.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_model_first_rag_flow.log)

```text
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_model_first_rag_flow.py", line 242, in test_hybrid_retrieval_keeps_default_path_healthy
    hits, trace = retrieve_hybrid_guarded("เกมแนวแข่งรถมีอะไรบ้าง", PipelineRoute("games", "game_catalog_lookup", 0.9, "list", "low", "smoke"))
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\hybrid_retrieval.py", line 204, in retrieve_hybrid_guarded
    curated_hits, curated_trace = retrieve_curated(query, route.category, limit=candidate_limit)
                                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\retrieval.py", line 900, in retrieve_curated
    return hits, PipelineTrace("rag_retrieval", "curated_lexical", confidence, detail, {"category": category, "game": competition_game, "intent": competition_intent,"common_ownership_blocked":ownership_blocked})
                                                                                                                                                                                                ^^^^^^^^^^^^^^^^^
NameError: name 'ownership_blocked' is not defined
```
## 55. legacy / smoke_test_pc_service_fee.py

{"file": "smoke_test_pc_service_fee.py", "status": "passed", "exit_code": 0, "elapsed": 14.092324299970642}

[smoke_test_pc_service_fee.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_pc_service_fee.log)
## 56. legacy / smoke_test_performance_trace.py

{"file": "smoke_test_performance_trace.py", "status": "passed", "exit_code": 0, "elapsed": 1.1365193999372423}

[smoke_test_performance_trace.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_performance_trace.log)
## 57. legacy / smoke_test_pipeline_fixes_20260823.py

{"file": "smoke_test_pipeline_fixes_20260823.py", "status": "failed", "exit_code": 1, "elapsed": 18.783543600002304}

[smoke_test_pipeline_fixes_20260823.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_pipeline_fixes_20260823.log)

```text
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 3565, in _answer_single
    source_hits, source_trace = retrieve_curated(
                                ^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\retrieval.py", line 900, in retrieve_curated
    return hits, PipelineTrace("rag_retrieval", "curated_lexical", confidence, detail, {"category": category, "game": competition_game, "intent": competition_intent,"common_ownership_blocked":ownership_blocked})
                                                                                                                                                                                                ^^^^^^^^^^^^^^^^^
NameError: name 'ownership_blocked' is not defined
```
## 58. legacy / smoke_test_pipeline_timing.py

{"file": "smoke_test_pipeline_timing.py", "status": "passed", "exit_code": 0, "elapsed": 20.648981499951333}

[smoke_test_pipeline_timing.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_pipeline_timing.log)
## 59. legacy / smoke_test_pipeline_warmup.py

{"file": "smoke_test_pipeline_warmup.py", "status": "failed", "exit_code": 1, "elapsed": 34.814689999911934}

[smoke_test_pipeline_warmup.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_pipeline_warmup.log)

```text
    runpy.run_path(str(p),run_name='__main__')
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_pipeline_warmup.py", line 34, in <module>
    test_pipeline_warmup()
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_pipeline_warmup.py", line 17, in test_pipeline_warmup
    assert result.ok, result.errors
           ^^^^^^^^^
AssertionError: ('probe_queries: NameError("name \'ownership_blocked\' is not defined")',)
```
## 60. legacy / smoke_test_pipeline_worker_supervisor.py

{"file": "smoke_test_pipeline_worker_supervisor.py", "status": "failed", "exit_code": 1, "elapsed": 18.03839710005559}

[smoke_test_pipeline_worker_supervisor.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_pipeline_worker_supervisor.log)

```text
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_pipeline_worker_supervisor.py", line 45, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_pipeline_worker_supervisor.py", line 30, in main
    assert call.result.route.category == "overview"
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError
```
## 61. legacy / smoke_test_pipeline_worker_timeout_recovery.py

{"file": "smoke_test_pipeline_worker_timeout_recovery.py", "status": "failed", "exit_code": 1, "elapsed": 28.583860999904573}

[smoke_test_pipeline_worker_timeout_recovery.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_pipeline_worker_timeout_recovery.log)

```text
    runpy.run_path(str(p),run_name='__main__')
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_pipeline_worker_timeout_recovery.py", line 59, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_pipeline_worker_timeout_recovery.py", line 41, in main
    raise AssertionError("replacement worker did not become ready")
AssertionError: replacement worker did not become ready
```
## 62. legacy / smoke_test_product_sla_guards.py

{"file": "smoke_test_product_sla_guards.py", "status": "passed", "exit_code": 0, "elapsed": 4.448229799978435}

[smoke_test_product_sla_guards.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_product_sla_guards.log)
## 63. legacy / smoke_test_query_planner.py

{"file": "smoke_test_query_planner.py", "status": "failed", "exit_code": 1, "elapsed": 13.253093600040302}

[smoke_test_query_planner.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_query_planner.log)

```text
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_query_planner.py", line 194, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_query_planner.py", line 187, in main
    test_engine_uses_validated_plan_without_second_intent_call()
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_query_planner.py", line 168, in test_engine_uses_validated_plan_without_second_intent_call
    assert result.mode == "pipeline:multi_question_splitter", result.mode
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: pipeline:structured_service_fee_conversation
```
## 64. legacy / smoke_test_rag_after_deterministic_fallback.py

{"file": "smoke_test_rag_after_deterministic_fallback.py", "status": "failed", "exit_code": 1, "elapsed": 1.8823527998756617}

[smoke_test_rag_after_deterministic_fallback.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_rag_after_deterministic_fallback.log)

```text
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_rag_after_deterministic_fallback.py", line 163, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_rag_after_deterministic_fallback.py", line 154, in main
    test_general_fallback_reads_rag_before_grounded_llm()
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_rag_after_deterministic_fallback.py", line 47, in test_general_fallback_reads_rag_before_grounded_llm
    assert calls == ["rag", "llm"], calls
           ^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: []
```
## 65. legacy / smoke_test_real_usage_golden.py

{"file": "smoke_test_real_usage_golden.py", "status": "failed", "exit_code": 1, "elapsed": 45.84780770004727}

[smoke_test_real_usage_golden.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_real_usage_golden.log)

```text
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 3565, in _answer_single
    source_hits, source_trace = retrieve_curated(
                                ^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\retrieval.py", line 900, in retrieve_curated
    return hits, PipelineTrace("rag_retrieval", "curated_lexical", confidence, detail, {"category": category, "game": competition_game, "intent": competition_intent,"common_ownership_blocked":ownership_blocked})
                                                                                                                                                                                                ^^^^^^^^^^^^^^^^^
NameError: name 'ownership_blocked' is not defined
```
## 66. legacy / smoke_test_repeated_character_variants.py

{"file": "smoke_test_repeated_character_variants.py", "status": "passed", "exit_code": 0, "elapsed": 3.525730299996212}

[smoke_test_repeated_character_variants.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_repeated_character_variants.log)
## 67. legacy / smoke_test_request_deadline.py

{"file": "smoke_test_request_deadline.py", "status": "failed", "exit_code": 1, "elapsed": 15.822962600039318}

[smoke_test_request_deadline.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_request_deadline.log)

```text
    runpy.run_path(str(p),run_name='__main__')
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_request_deadline.py", line 41, in <module>
    test_no_global_deadline_keeps_normal_fast_answer()
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_request_deadline.py", line 36, in test_no_global_deadline_keeps_normal_fast_answer
    assert result.route.category == "games"
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError
```
## 68. legacy / smoke_test_runtime_input_quality_guard.py

{"file": "smoke_test_runtime_input_quality_guard.py", "status": "failed", "exit_code": 1, "elapsed": 2.5851405998691916}

[smoke_test_runtime_input_quality_guard.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_runtime_input_quality_guard.log)

```text
    runpy.run_path(str(p),run_name='__main__')
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_runtime_input_quality_guard.py", line 60, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_runtime_input_quality_guard.py", line 27, in main
    raise AssertionError(f"expected repeated-character retry, got {repeated}")
AssertionError: expected repeated-character retry, got InputQualityDecision(detected_action='request_retype', applied_action='warn_and_continue', should_short_circuit=False, message='ข้อความนี้อาจมีตัวอักษรซ้ำโดยไม่ตั้งใจ กรุณาตรวจสอบและพิมพ์คำถามใหม่อีกครั้งครับ', features=AnomalyFeatures(input_text='จอองแล้วแก้ไขได้ไหม', layout_score=0.001667, layout_direction='english_intended_thai_active', layout_candidate_preview=None, layout_reason='mapping lacks stronger English orthographic/lexical evidence', layout_spans=(SpanEvidence(direction='english_intended_thai_active', source_span='จอองแล้วแก้ไขได้ไหม', mapped_span="0vv'c]h;cdhw-wfhws,", start=0, end=19, score=0.001667, source_quality=0.686297, target_quality=0.203102, target_seen=False, source_protected=False, reason='mapping lacks stronger English orthographic/lexical evidence'),), repeat_score=0.559482, repeat_candidate_preview='จองแล้วแก้ไขได้ไหม', repeat_reason='removing one repeated character improves quality 0.686->0.763; seen False->False', repeat_spans=(RepeatEvidence(source_span='ออ', candidate_span='จอง … [ย่อจาก2,337ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```
## 69. legacy / smoke_test_scope_guard_fallback.py

{"file": "smoke_test_scope_guard_fallback.py", "status": "failed", "exit_code": 1, "elapsed": 19.65906050009653}

[smoke_test_scope_guard_fallback.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_scope_guard_fallback.log)

```text
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_scope_guard_fallback.py", line 42, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_scope_guard_fallback.py", line 36, in main
    assert result.elapsed < 4.0, (question, result.elapsed, result.mode)
           ^^^^^^^^^^^^^^^^^^^^
AssertionError: ('เครื่องไหนดีที่สุด', 14.5073, 'pipeline:guard_no_answer')
```
## 70. legacy / smoke_test_semantic_general_bypass.py

{"file": "smoke_test_semantic_general_bypass.py", "status": "passed", "exit_code": 0, "elapsed": 1.7872764999046922}

[smoke_test_semantic_general_bypass.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_semantic_general_bypass.log)
## 71. legacy / smoke_test_semantic_rag.py

{"file": "smoke_test_semantic_rag.py", "status": "passed", "exit_code": 0, "elapsed": 7.539229100104421}

[smoke_test_semantic_rag.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_semantic_rag.log)
## 72. legacy / smoke_test_semantic_target_filter.py

{"file": "smoke_test_semantic_target_filter.py", "status": "passed", "exit_code": 0, "elapsed": 2.3383364998735487}

[smoke_test_semantic_target_filter.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_semantic_target_filter.log)
## 73. legacy / smoke_test_session_context.py

{"file": "smoke_test_session_context.py", "status": "failed", "exit_code": 1, "elapsed": 21.980839400086552}

[smoke_test_session_context.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_session_context.log)

```text
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_session_context.py", line 270, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_session_context.py", line 61, in main
    assert result.mode == "pipeline:structured_service_game_availability", result.mode
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: pipeline:source_operation_game_list
```
## 74. legacy / smoke_test_shadow_critic.py

{"file": "smoke_test_shadow_critic.py", "status": "passed", "exit_code": 0, "elapsed": 22.656728699803352}

[smoke_test_shadow_critic.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_shadow_critic.log)
## 75. legacy / smoke_test_source_contract.py

{"file": "smoke_test_source_contract.py", "status": "failed", "exit_code": 1, "elapsed": 17.308044199831784}

[smoke_test_source_contract.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_source_contract.log)

```text
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_source_contract.py", line 98, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_source_contract.py", line 64, in main
    assert_has(pc_ids, SERVICE_FEE_IMAGE_2026_ID, "pc pipeline")
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_source_contract.py", line 37, in assert_has
    raise AssertionError(f"{label}: missing source id {expected}; got {ids}")
AssertionError: pc pipeline: missing source id service_fee_image_2026; got ['pc_service_fee_local_update_20260727']
```
## 76. legacy / smoke_test_structured_tools.py

{"file": "smoke_test_structured_tools.py", "status": "failed", "exit_code": 1, "elapsed": 19.043915500165895}

[smoke_test_structured_tools.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_structured_tools.log)

```text
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_structured_tools.py", line 181, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_structured_tools.py", line 30, in main
    assert result.mode == "pipeline:structured_members_group_count", result.mode
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: pipeline:user_service_facts
```
## 77. legacy / smoke_test_surface_input_recovery.py

{"file": "smoke_test_surface_input_recovery.py", "status": "passed", "exit_code": 0, "elapsed": 19.7608056999743}

[smoke_test_surface_input_recovery.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_surface_input_recovery.log)
## 78. legacy / smoke_test_target_lock.py

{"file": "smoke_test_target_lock.py", "status": "passed", "exit_code": 0, "elapsed": 5.429245900129899}

[smoke_test_target_lock.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_target_lock.log)
## 79. legacy / smoke_test_target_resolver.py

{"file": "smoke_test_target_resolver.py", "status": "passed", "exit_code": 0, "elapsed": 4.848511799937114}

[smoke_test_target_resolver.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_target_resolver.log)
## 80. legacy / smoke_test_timeout_routing_resolver_remediation.py

{"file": "smoke_test_timeout_routing_resolver_remediation.py", "status": "failed", "exit_code": 1, "elapsed": 15.57435499993153}

[smoke_test_timeout_routing_resolver_remediation.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_timeout_routing_resolver_remediation.log)

```text
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_timeout_routing_resolver_remediation.py", line 61, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_timeout_routing_resolver_remediation.py", line 51, in main
    assert answer.route.category == "overview"
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError
```
## 81. legacy / smoke_test_tool_preconditions.py

{"file": "smoke_test_tool_preconditions.py", "status": "passed", "exit_code": 0, "elapsed": 4.161833200138062}

[smoke_test_tool_preconditions.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_tool_preconditions.log)
## 82. legacy / smoke_test_typo_intent_recovery.py

{"file": "smoke_test_typo_intent_recovery.py", "status": "passed", "exit_code": 0, "elapsed": 18.633301499998197}

[smoke_test_typo_intent_recovery.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_typo_intent_recovery.log)
## 83. legacy / smoke_test_universal_intent.py

{"file": "smoke_test_universal_intent.py", "status": "failed", "exit_code": 1, "elapsed": 20.166682600043714}

[smoke_test_universal_intent.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_universal_intent.log)

```text
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_universal_intent.py", line 148, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_universal_intent.py", line 71, in main
    check(
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_universal_intent.py", line 24, in check
    raise AssertionError(f"{question}: missing universal intent")
AssertionError: สมาชิกใน PSU Esport มีกี่หมวด: missing universal intent
```
## 84. legacy / smoke_test_update.py

{"file": "smoke_test_update.py", "status": "failed", "exit_code": 1, "elapsed": 1.1642063001636416}

[smoke_test_update.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_update.log)

```text
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_update.py", line 54, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_update.py", line 37, in main
    assert_contains(result["answer"], expected, question)
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_update.py", line 19, in assert_contains
    raise AssertionError(f"{label}: expected {expected!r} in {text!r}")
AssertionError: เด็กจุฬา เล่น PC กี่บาท: expected 'มหาลัยอื่น' in 'ราคา PC 1 ชั่วโมง (1 คน) สำหรับ ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student)\n•    25 บาท\nหมายเหตุข้อมูล PC: ราคา PC เพิ่มจาก local service fee update 2026-07-27\nแหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png'
```
## 85. legacy / smoke_test_versioned_game_resolution.py

{"file": "smoke_test_versioned_game_resolution.py", "status": "passed", "exit_code": 0, "elapsed": 18.603432999923825}

[smoke_test_versioned_game_resolution.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_smokes/smoke_test_versioned_game_resolution.log)
## 86. common / smoke_test_accented_english_game_routing.py

{"file": "smoke_test_accented_english_game_routing.py", "status": "failed", "exit_code": 1, "elapsed": 9.221330400090665}

[smoke_test_accented_english_game_routing.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_accented_english_game_routing.log)

```text
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_accented_english_game_routing.py", line 34, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_accented_english_game_routing.py", line 26, in main
    assert result.route.category == "games", (result.route, result.answer)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: (PipelineRoute(category='knowledge', intent='common_read', confidence=0.0, answer_type='partial_answer', risk='medium', reason='approved common content'), 'No confirmed control_set data for this scope.\n\nbindings: This attribute is outside the selected record scope; please specify the related service or record.')
```
## 87. common / smoke_test_adaptive_intent_gate.py

{"file": "smoke_test_adaptive_intent_gate.py", "status": "passed", "exit_code": 0, "elapsed": 13.117834000149742}

[smoke_test_adaptive_intent_gate.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_adaptive_intent_gate.log)
## 88. common / smoke_test_ambiguity_gate.py

{"file": "smoke_test_ambiguity_gate.py", "status": "failed", "exit_code": 1, "elapsed": 25.862934699980542}

[smoke_test_ambiguity_gate.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_ambiguity_gate.log)

```text
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_ambiguity_gate.py", line 189, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_ambiguity_gate.py", line 103, in main
    assert_contains(result.answer, ["ขอชื่อเกมก่อน", "TEKKEN 8"], "control query missing game clarification")
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_ambiguity_gate.py", line 19, in assert_contains
    raise AssertionError(f"{label}: missing {missing}\n{text}")
AssertionError: control query missing game clarification: missing ['ขอชื่อเกมก่อน', 'TEKKEN 8']
ต้องการดูปุ่มควบคุมของเกมใดครับ? พิมพ์ชื่อเกมที่ต้องการได้เลยครับ
```
## 89. common / smoke_test_answer_formatting.py

{"file": "smoke_test_answer_formatting.py", "status": "failed", "exit_code": 1, "elapsed": 16.688130000140518}

[smoke_test_answer_formatting.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_answer_formatting.log)

```text
• PC #05
• PC #06
• PC #07
• PC #08
• PC #09
• PC #10
• PlayStation 5 #01
• PlayStation 5 #02

รายการเดิมที่ยังไม่ได้ย้ายและอนุมัติในฐานข้อมูลกลางไม่รวมในรายการนี้
```
## 90. common / smoke_test_answer_pipeline.py

{"file": "smoke_test_answer_pipeline.py", "status": "failed", "exit_code": 1, "elapsed": 47.16916000004858}

[smoke_test_answer_pipeline.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_answer_pipeline.log)

```text
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_answer_pipeline.py", line 256, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_answer_pipeline.py", line 44, in main
    check(
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_answer_pipeline.py", line 29, in check
    raise AssertionError(f"{question}: missing {missing}\n{result.answer}")
AssertionError: วันจันทร์ morning เล่นได้ไหม afternoon เปิดไหม: missing ['Morning เล่นไม่ได้', 'Afternoon เปิด', '13:00', '16:00']
ขออภัยครับ คำถามนี้ใช้เวลาประมวลผลเกินเวลาที่กำหนด เลยหยุดไว้ก่อนเพื่อไม่ให้ระบบค้าง
ลองถามใหม่ให้เฉพาะเจาะจงขึ้น เช่น ระบุโซน เกม หรือเรื่องที่ต้องการถามโดยตรงครับ
```
## 91. common / smoke_test_answer_validator.py

{"file": "smoke_test_answer_validator.py", "status": "passed", "exit_code": 0, "elapsed": 20.65156130003743}

[smoke_test_answer_validator.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_answer_validator.log)
## 92. common / smoke_test_audit_regressions.py

{"file": "smoke_test_audit_regressions.py", "status": "failed", "exit_code": 1, "elapsed": 46.72525739995763}

[smoke_test_audit_regressions.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_audit_regressions.log)

```text
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_audit_regressions.py", line 70, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_audit_regressions.py", line 31, in main
    assert_contains(result.answer, ["RoV", "MOBA"], "rov detail")
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_audit_regressions.py", line 19, in assert_contains
    raise AssertionError(f"{label}: missing {missing}\n{text}")
AssertionError: rov detail: missing ['RoV', 'MOBA']
คำถามนี้มีได้หลายความหมายครับ ขอระบุเพิ่มนิดหนึ่งว่าต้องการถามเรื่องไหน: รายชื่อเกม/ข้อมูลเกม
```
## 93. common / smoke_test_availability_policy_regressions.py

{"file": "smoke_test_availability_policy_regressions.py", "status": "failed", "exit_code": 1, "elapsed": 25.485467599937692}

[smoke_test_availability_policy_regressions.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_availability_policy_regressions.log)

```text
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_availability_policy_regressions.py", line 135, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_availability_policy_regressions.py", line 46, in main
    check(
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_availability_policy_regressions.py", line 33, in check
    raise AssertionError(f"{question}: category {result.route.category} != {category}\n{result.answer}")
AssertionError: PC #01 มี Call of Duty: Warzone ไหม: category knowledge != games
ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ PC #01 เช่น แพลตฟอร์ม เช่น PC หรือ PS5 / อุปกรณ์ควบคุม / ชื่อชุดปุ่ม เช่น default / ปุ่มควบคุม: เพิ่มทีละปุ่มหรือชุดปุ่ม?
```
## 94. common / smoke_test_bilingual_locale.py

{"file": "smoke_test_bilingual_locale.py", "status": "passed", "exit_code": 0, "elapsed": 19.239190599881113}

[smoke_test_bilingual_locale.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_bilingual_locale.log)
## 95. common / smoke_test_bilingual_pipeline.py

{"file": "smoke_test_bilingual_pipeline.py", "status": "failed", "exit_code": 1, "elapsed": 23.915055099874735}

[smoke_test_bilingual_pipeline.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_bilingual_pipeline.log)

```text
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_bilingual_pipeline.py", line 352, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_bilingual_pipeline.py", line 53, in main
    assert catalog.language.effective == "en"
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'effective'
```
## 96. common / smoke_test_bilingual_web_api.py

{"file": "smoke_test_bilingual_web_api.py", "status": "deferred_actual_http_suite", "reason": "Will run against isolated evaluation web servers, not user server"}

[SUMMARY.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_http_protocol_network/SUMMARY.json)

```text
รันผ่านactual HTTP suiteแยก
```
## 97. common / smoke_test_booking_policy_rag_gate.py

{"file": "smoke_test_booking_policy_rag_gate.py", "status": "passed", "exit_code": 0, "elapsed": 46.79642599984072}

[smoke_test_booking_policy_rag_gate.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_booking_policy_rag_gate.log)
## 98. common / smoke_test_booking_price_regression.py

{"file": "smoke_test_booking_price_regression.py", "status": "failed", "exit_code": 1, "elapsed": 66.82001499994658}

[smoke_test_booking_price_regression.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_booking_price_regression.log)

```text
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4084, in _answer_single
    rag_hits, rag_trace = retrieve_curated(pre.clean_query, route.category)
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\retrieval.py", line 900, in retrieve_curated
    return hits, PipelineTrace("rag_retrieval", "curated_lexical", confidence, detail, {"category": category, "game": competition_game, "intent": competition_intent,"common_ownership_blocked":ownership_blocked})
                                                                                                                                                                                                ^^^^^^^^^^^^^^^^^
NameError: name 'ownership_blocked' is not defined
```
## 99. common / smoke_test_boundary_guard.py

{"file": "smoke_test_boundary_guard.py", "status": "failed", "exit_code": 1, "elapsed": 54.19679479999468}

[smoke_test_boundary_guard.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_boundary_guard.log)

```text
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_boundary_guard.py", line 80, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_boundary_guard.py", line 38, in main
    assert sensitive.mode == "pipeline:multi_question_splitter", sensitive.mode
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: pipeline:common_partial_answer
```
## 100. common / smoke_test_broad_competition_rag_route.py

{"file": "smoke_test_broad_competition_rag_route.py", "status": "passed", "exit_code": 0, "elapsed": 17.548305199947208}

[smoke_test_broad_competition_rag_route.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_broad_competition_rag_route.log)
## 101. common / smoke_test_canonical_content.py

{"file": "smoke_test_canonical_content.py", "status": "failed", "exit_code": 1, "elapsed": 13.959276699926704}

[smoke_test_canonical_content.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_canonical_content.log)

```text
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_canonical_content.py", line 33, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_canonical_content.py", line 20, in main
    assert manifest["record_count"] == len(records)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError
```
## 102. common / smoke_test_canonical_publish_gate.py

{"file": "smoke_test_canonical_publish_gate.py", "status": "passed", "exit_code": 0, "elapsed": 7.848995799897239}

[smoke_test_canonical_publish_gate.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_canonical_publish_gate.log)
## 103. common / smoke_test_canonical_rag_integration.py

{"file": "smoke_test_canonical_rag_integration.py", "status": "failed", "exit_code": 1, "elapsed": 10.361314499983564}

[smoke_test_canonical_rag_integration.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_canonical_rag_integration.log)

```text
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_canonical_rag_integration.py", line 66, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_canonical_rag_integration.py", line 27, in main
    game_hits, _ = retrieve_curated("VALORANT เล่นยังไง", "games", limit=3)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\retrieval.py", line 900, in retrieve_curated
    return hits, PipelineTrace("rag_retrieval", "curated_lexical", confidence, detail, {"category": category, "game": competition_game, "intent": competition_intent,"common_ownership_blocked":ownership_blocked})
                                                                                                                                                                                                ^^^^^^^^^^^^^^^^^
NameError: name 'ownership_blocked' is not defined
```
## 104. common / smoke_test_chat_logger_postgres.py

{"file": "smoke_test_chat_logger_postgres.py", "status": "passed", "exit_code": 0, "elapsed": 11.342629400081933}

[smoke_test_chat_logger_postgres.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_chat_logger_postgres.log)
## 105. common / smoke_test_chat_logger_sqlite.py

{"file": "smoke_test_chat_logger_sqlite.py", "status": "passed", "exit_code": 0, "elapsed": 11.74590630014427}

[smoke_test_chat_logger_sqlite.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_chat_logger_sqlite.log)
## 106. common / smoke_test_chat_quality_metrics.py

{"file": "smoke_test_chat_quality_metrics.py", "status": "passed", "exit_code": 0, "elapsed": 9.57271569990553}

[smoke_test_chat_quality_metrics.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_chat_quality_metrics.log)
## 107. common / smoke_test_compact_intent_prompt.py

{"file": "smoke_test_compact_intent_prompt.py", "status": "passed", "exit_code": 0, "elapsed": 6.921823800075799}

[smoke_test_compact_intent_prompt.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_compact_intent_prompt.log)
## 108. common / smoke_test_competition_signal_priority.py

{"file": "smoke_test_competition_signal_priority.py", "status": "failed", "exit_code": 1, "elapsed": 8.659217600012198}

[smoke_test_competition_signal_priority.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_competition_signal_priority.log)

```text
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_competition_signal_priority.py", line 36, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_competition_signal_priority.py", line 29, in main
    assert result.route.category == "competition_rules", (question, result.route, result.answer)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: ('VALORANT ใช้ผู้เล่นกี่คน', PipelineRoute(category='knowledge', intent='common_read', confidence=0.0, answer_type='partial_answer', risk='medium', reason='approved common content'), 'ยังไม่มีข้อมูลยืนยันในส่วน รูปแบบเล่นและเล่นกับเพื่อน สำหรับขอบเขตนี้\n\n**PC #01-#02**\n• จำนวนคนสูงสุดของบริการ: 1 [S1]\n\n**PC #01**\n• จำนวนคนที่เล่นเครื่องนี้พร้อมกันได้: 1 [S2]\n\n**PC #02**\n• จำนวนคนที่เล่นเครื่องนี้พร้อมกันได้: 1 [S3]\n\n**PC Zone**\n• จำนวนที่นั่งในพื้นที่ (ไม่ใช่จำนวนผู้เล่นต่อเครื่อง): ยังไม่มีข้อมูลยืนยัน\n\n**PC #03-#10**\n• จำนวนคนสูงสุดของบริการ: 1 [S4]\n\n**PC #03**\n• จำนวนคนที่เล่นเครื่องนี้พร้อมกันได้: 1 [S5]\n\n**PC #04**\n• จำนวนคนที่เล่นเครื่องนี้พร้อมกันได้: 1 [S6]\n\n**PC #05**\n• จำนวนคนที่เล่นเครื่องนี้พร้อมกันได้: 1 [S7]\n\n**PC #06**\n• จำนวนคนที่เล่นเครื่องนี้พร้อมกันได้: 1 [S8]\n\n**PC #07**\n• จำนวนคนที่เล่นเครื่องนี้พร้อมกันได้: 1 [S9]\n\n**PC #08**\n• จำนวนคนที่เล่นเครื่องนี้พร้อมกันได้: 1 [S10]\n\n**PC #09**\n• จำนวนคนที่เล่นเครื่องนี้พร้อมกันได้: 1 [S11]\n\n**PC #10**\n• จำนวนคนที่เล่นเคร … [ย่อจาก1,921ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```
## 109. common / smoke_test_compound_execution.py

{"file": "smoke_test_compound_execution.py", "status": "failed", "exit_code": 1, "elapsed": 11.381340799853206}

[smoke_test_compound_execution.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_compound_execution.log)

```text
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_compound_execution.py", line 111, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_compound_execution.py", line 69, in main
    assert "bounded_parallel" in _decisions(result, "compound_child_execution"), result.trace
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: [PipelineTrace(stage='common_content', decision='clarification', confidence=0.0, detail='typed fields and source-backed joins; uncalibrated confidence', metadata={'response_type': 'clarification', 'release_id': 'EVAL_DRAFT_ONLY', 'query_plan': {'record_ids': ['migrated_faq_rule_booking_steps'], 'requested_fields': [], 'all_fields': False, 'method': 'exact', 'scope': 'common_published', 'platform': None, 'query_without_entity': 'pc ราคาเท่าไหร่ แล้ว', 'field_selection': [], 'confidence_calibrated': False, 'request_focus': None, 'authority': {'decision': 'common', 'reason': 'published_target_owned', 'record_ids': ['migrated_faq_rule_booking_steps'], 'release_id': 'EVAL_DRAFT_ONLY', 'epoch': 584}, 'field_authority': [], 'unresolved_clauses': ['pc ราคาเท่าไหร่'], 'semantic_review_needed': True, 'semantic_plan_accepted': False}, 'obligations': [], 'catalog_scope': 'common_published', 'coverage_errors': [], 'confidence_calibrated': False, 'validation_scope': 'selected fields and evidence, not human intent correctness'})]
```
## 110. common / smoke_test_compound_question_planner.py

{"file": "smoke_test_compound_question_planner.py", "status": "failed", "exit_code": 1, "elapsed": 9.254356800112873}

[smoke_test_compound_question_planner.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_compound_question_planner.log)

```text
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_compound_question_planner.py", line 91, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_compound_question_planner.py", line 34, in main
    assert result.mode == "pipeline:multi_question_splitter", result.mode
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: pipeline:common_answer
```
## 111. common / smoke_test_control_catalog_coverage.py

{"file": "smoke_test_control_catalog_coverage.py", "status": "passed", "exit_code": 0, "elapsed": 6.672552799805999}

[smoke_test_control_catalog_coverage.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_control_catalog_coverage.log)
## 112. common / smoke_test_correctness_control_flow_v1.py

{"file": "smoke_test_correctness_control_flow_v1.py", "status": "failed", "exit_code": 1, "elapsed": 12.14649789989926}

[smoke_test_correctness_control_flow_v1.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_correctness_control_flow_v1.log)

```text
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_correctness_control_flow_v1.py", line 193, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_correctness_control_flow_v1.py", line 92, in main
    assert not no_controls.top_candidate.has_controls
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError
```
## 113. common / smoke_test_decision_artifact.py

{"file": "smoke_test_decision_artifact.py", "status": "failed", "exit_code": 1, "elapsed": 18.01783309993334}

[smoke_test_decision_artifact.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_decision_artifact.log)

```text
    runpy.run_path(str(p),run_name='__main__')
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_decision_artifact.py", line 76, in <module>
    test_structured_question_has_decision_artifact()
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_decision_artifact.py", line 29, in test_structured_question_has_decision_artifact
    assert artifact["intent"]["domain"] == "members"
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError
```
## 114. common / smoke_test_english_compound_split.py

{"file": "smoke_test_english_compound_split.py", "status": "failed", "exit_code": 1, "elapsed": 24.962012599920854}

[smoke_test_english_compound_split.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_english_compound_split.log)

```text
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_english_compound_split.py", line 48, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_english_compound_split.py", line 30, in main
    assert combined.route.category == "multi_question", combined.route
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: PipelineRoute(category='service_fee', intent='conversation_price_lookup', confidence=0.98, answer_type='fact', risk='medium', reason='typed service and customer filters with source-bound coverage')
```
## 115. common / smoke_test_english_date_aware_schedule.py

{"file": "smoke_test_english_date_aware_schedule.py", "status": "passed", "exit_code": 0, "elapsed": 6.3146119001321495}

[smoke_test_english_date_aware_schedule.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_english_date_aware_schedule.log)
## 116. common / smoke_test_english_draft_preview.py

{"file": "smoke_test_english_draft_preview.py", "status": "failed", "exit_code": 1, "elapsed": 7.826002199901268}

[smoke_test_english_draft_preview.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_english_draft_preview.log)

```text
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_english_draft_preview.py", line 54, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_english_draft_preview.py", line 29, in main
    assert game.mode == "pipeline:structured_game_detail_en", game
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: PipelineAnswer(answer='**God of War Ragnarök**\n• title: God of War Ragnarök [S1]\n• summary: Not yet confirmed\n• how to play: Not yet confirmed\n\n**God of War Ragnarök**\n• game id: God of War Ragnarök [S2]\n• platform: PlayStation / PS5 [S3]\n• input device: Not yet confirmed\n• preset: Not yet confirmed\n• bindings: Not yet confirmed', hits=[{'id': 'migrated_game_god_of_war_ragnar_k:title:S1', 'title': 'Approved center information', 'source_url': '', 'text': 'God of War Ragnarök', 'source_id': 'r63_50d384da3381763f8a3c123b4ef0', 'snapshot_sha256': 'dec75ee01f8c6767bf79ac7f98c40c83d7162dc4d27007afaa2d6b978a65ab1b', 'citation_label': 'S1', 'locator': '/mapped_fields/title', 'metadata': {'common_approved': True, 'title': 'Approved center information', 'release_id': 'EVAL_DRAFT_ONLY'}}, {'id': 'controls_ps5_god_of_war_ragnar_k:game_id:S2', 'title': 'Approved center information', 'source_url': '', 'text': 'migrated_game_god_of_war_ragnar_k', 'source_id': 'r63_4544ab57027abacb7f9d37992f70', 'snapshot_sha256': '9ae98496e58235c3621ff60fba4f8a1c1e1253b777690bac … [ย่อจาก8,238ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```
## 117. common / smoke_test_english_format_parity_fixes.py

{"file": "smoke_test_english_format_parity_fixes.py", "status": "failed", "exit_code": 1, "elapsed": 28.284443099983037}

[smoke_test_english_format_parity_fixes.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_english_format_parity_fixes.log)

```text
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_english_format_parity_fixes.py", line 49, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_english_format_parity_fixes.py", line 40, in main
    assert "Official Thai source member record" in manager.answer
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError
```
## 118. common / smoke_test_english_game_target_priority.py

{"file": "smoke_test_english_game_target_priority.py", "status": "failed", "exit_code": 1, "elapsed": 9.275545499986038}

[smoke_test_english_game_target_priority.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_english_game_target_priority.log)

```text
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_english_game_target_priority.py", line 92, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_english_game_target_priority.py", line 34, in main
    assert game_detail.mode == "pipeline:structured_game_detail_en", game_detail.mode
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: pipeline:common_answer
```
## 119. common / smoke_test_english_localization_registry.py

{"file": "smoke_test_english_localization_registry.py", "status": "passed", "exit_code": 0, "elapsed": 8.063428899971768}

[smoke_test_english_localization_registry.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_english_localization_registry.log)
## 120. common / smoke_test_english_localization_review_workflow.py

{"file": "smoke_test_english_localization_review_workflow.py", "status": "passed", "exit_code": 0, "elapsed": 7.872547300066799}

[smoke_test_english_localization_review_workflow.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_english_localization_review_workflow.log)
## 121. common / smoke_test_entity_reranker_gate.py

{"file": "smoke_test_entity_reranker_gate.py", "status": "passed", "exit_code": 0, "elapsed": 14.043907900108024}

[smoke_test_entity_reranker_gate.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_entity_reranker_gate.log)
## 122. common / smoke_test_entity_resolver_v2.py

{"file": "smoke_test_entity_resolver_v2.py", "status": "failed", "exit_code": 1, "elapsed": 24.62705559981987}

[smoke_test_entity_resolver_v2.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_entity_resolver_v2.log)

```text
    runpy.run_path(str(p),run_name='__main__')
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_entity_resolver_v2.py", line 70, in <module>
    test_pipeline_clarifies_family_controls_but_allows_family_list()
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_entity_resolver_v2.py", line 52, in test_pipeline_clarifies_family_controls_but_allows_family_list
    assert mario_controls.mode == "pipeline:ambiguity_clarification", mario_controls.mode
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: pipeline:common_answer
```
## 123. common / smoke_test_facts_composer.py

{"file": "smoke_test_facts_composer.py", "status": "passed", "exit_code": 0, "elapsed": 8.149715000065044}

[smoke_test_facts_composer.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_facts_composer.log)
## 124. common / smoke_test_fast_runtime.py

{"file": "smoke_test_fast_runtime.py", "status": "passed", "exit_code": 0, "elapsed": 13.276528199901804}

[smoke_test_fast_runtime.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_fast_runtime.log)
## 125. common / smoke_test_full_eval_regression_fixes.py

{"file": "smoke_test_full_eval_regression_fixes.py", "status": "failed", "exit_code": 1, "elapsed": 20.431572600034997}

[smoke_test_full_eval_regression_fixes.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_full_eval_regression_fixes.log)

```text
    runpy.run_path(str(p),run_name='__main__')
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_full_eval_regression_fixes.py", line 83, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_full_eval_regression_fixes.py", line 39, in main
    raise AssertionError(f"text generation should route general, got {result.route.category}/{result.route.intent}")
AssertionError: text generation should route general, got knowledge/common_read
```
## 126. common / smoke_test_game_catalog.py

{"file": "smoke_test_game_catalog.py", "status": "failed", "exit_code": 1, "elapsed": 14.177901800023392}

[smoke_test_game_catalog.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_game_catalog.log)

```text
• eFootball
• God of War Ragnarök
• Mario Kart Live: Home Circuit
• Overcooked!
• Pokémon Champions
• Resident Evil 4 (Remake)
• THE FINALS
• The Last of Us Part I
• The Last of Us Part II
• The Last of Us Part II (Remastered)
```
## 127. common / smoke_test_game_controls.py

{"file": "smoke_test_game_controls.py", "status": "failed", "exit_code": 1, "elapsed": 11.534244999988005}

[smoke_test_game_controls.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_game_controls.log)

```text
• ปุ่มควบคุม: เพิ่มทีละปุ่มหรือชุดปุ่ม: ยังไม่มีข้อมูลยืนยัน
• แพลตฟอร์ม เช่น PC หรือ PS5: PlayStation / PS5 [S37]
• อุปกรณ์ควบคุม: ยังไม่มีข้อมูลยืนยัน
• ชื่อชุดปุ่ม เช่น default: ยังไม่มีข้อมูลยืนยัน

**ปุ่มควบคุมเกม**
• ปุ่มควบคุม: เพิ่มทีละปุ่มหรือชุดปุ่ม: ยังไม่มีข้อมูลยืนยัน
• แพลตฟอร์ม เช่น PC หรือ PS5: PlayStation / PS5 [S38]
• อุปกรณ์ควบคุม: ยังไม่มีข้อมูลยืนยัน
• ชื่อชุดปุ่ม เช่น default: ยังไม่มีข้อมูลยืนยัน
```
## 128. common / smoke_test_game_title_typo_correction.py

{"file": "smoke_test_game_title_typo_correction.py", "status": "failed", "exit_code": 1, "elapsed": 15.480432499898598}

[smoke_test_game_title_typo_correction.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_game_title_typo_correction.log)

```text
• แพลตฟอร์ม เช่น PC หรือ PS5: PC [S11]
• เวลาเล่น (นาที): 60 [S12]
• เวลาที่ล็อกเครื่อง (นาที): ยังไม่มีข้อมูลยืนยัน

**PlayStation 5 #01-#02**
• ชื่อบริการตามหน้า WordPress: PlayStation 5 #01-#02 [S13]
• เครื่องจริงที่ใช้กับบริการนี้: PlayStation 5 #01, PlayStation 5 #02 [S14]
• แพลตฟอร์ม เช่น PC หรือ PS5: PlayStation 5 [S15]
• เวลาเล่น (นาที): 60 [S16]
• เวลาที่ล็อกเครื่อง (นาที): ยังไม่มีข้อมูลยืนยัน
```
## 129. common / smoke_test_genre_alias_formatting.py

{"file": "smoke_test_genre_alias_formatting.py", "status": "failed", "exit_code": 1, "elapsed": 18.526699899928644}

[smoke_test_genre_alias_formatting.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_genre_alias_formatting.log)

```text
• eFootball
• God of War Ragnarök
• Mario Kart Live: Home Circuit
• Overcooked!
• Pokémon Champions
• Resident Evil 4 (Remake)
• THE FINALS
• The Last of Us Part I
• The Last of Us Part II
• The Last of Us Part II (Remastered)
```
## 130. common / smoke_test_keyboard_input_anomaly.py

{"file": "smoke_test_keyboard_input_anomaly.py", "status": "passed", "exit_code": 0, "elapsed": 7.7593771000392735}

[smoke_test_keyboard_input_anomaly.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_keyboard_input_anomaly.log)
## 131. common / smoke_test_live_booking_status.py

{"file": "smoke_test_live_booking_status.py", "status": "failed", "exit_code": 1, "elapsed": 14.280322200153023}

[smoke_test_live_booking_status.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_live_booking_status.log)

```text
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_live_booking_status.py", line 352, in test_english_plural_zone_questions_stay_scoped_and_list_all_resources
    self.assertEqual(answer.count("•    "), expected_rows)
AssertionError: 4 != 5

----------------------------------------------------------------------
Ran 17 tests in 5.585s

FAILED (failures=3)
```
## 132. common / smoke_test_live_canonical_semantic_rag.py

{"file": "smoke_test_live_canonical_semantic_rag.py", "status": "failed", "exit_code": 1, "elapsed": 17.167651699855924}

[smoke_test_live_canonical_semantic_rag.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_live_canonical_semantic_rag.log)

```text
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_live_canonical_semantic_rag.py", line 39, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_live_canonical_semantic_rag.py", line 30, in main
    assert hits, trace.detail
           ^^^^
AssertionError: TimeoutError: timed out
```
## 133. common / smoke_test_llm_budget_and_fast_split.py

{"file": "smoke_test_llm_budget_and_fast_split.py", "status": "passed", "exit_code": 0, "elapsed": 10.94650169997476}

[smoke_test_llm_budget_and_fast_split.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_llm_budget_and_fast_split.log)
## 134. common / smoke_test_llm_concurrency.py

{"file": "smoke_test_llm_concurrency.py", "status": "passed", "exit_code": 0, "elapsed": 8.414728599833325}

[smoke_test_llm_concurrency.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_llm_concurrency.log)
## 135. common / smoke_test_llm_health_circuit_breaker.py

{"file": "smoke_test_llm_health_circuit_breaker.py", "status": "failed", "exit_code": 1, "elapsed": 9.009494500001892}

[smoke_test_llm_health_circuit_breaker.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_llm_health_circuit_breaker.log)

```text
    runpy.run_path(str(p),run_name='__main__')
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_llm_health_circuit_breaker.py", line 258, in <module>
    test_general_fallback_skips_when_circuit_open()
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_llm_health_circuit_breaker.py", line 80, in test_general_fallback_skips_when_circuit_open
    assert fallback.mode == "general_llm_unavailable"
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError
```
## 136. common / smoke_test_llm_timing_and_general_guard.py

{"file": "smoke_test_llm_timing_and_general_guard.py", "status": "failed", "exit_code": 1, "elapsed": 20.996990900021046}

[smoke_test_llm_timing_and_general_guard.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_llm_timing_and_general_guard.log)

```text
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\experimental_fallback.py", line 259, in _retrieve_experimental_rows
    hybrid_rows, hybrid_trace = retrieve_hybrid_guarded(
                                ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\hybrid_retrieval.py", line 204, in retrieve_hybrid_guarded
    curated_hits, curated_trace = retrieve_curated(query, route.category, limit=candidate_limit)
                                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\retrieval.py", line 900, in retrieve_curated
    return hits, PipelineTrace("rag_retrieval", "curated_lexical", confidence, detail, {"category": category, "game": competition_game, "intent": competition_intent,"common_ownership_blocked":ownership_blocked})
                                                                                                                                                                                                ^^^^^^^^^^^^^^^^^
NameError: name 'ownership_blocked' is not defined
```
## 137. common / smoke_test_llm_tool_router.py

{"file": "smoke_test_llm_tool_router.py", "status": "failed", "exit_code": 1, "elapsed": 17.753319300012663}

[smoke_test_llm_tool_router.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_llm_tool_router.log)

```text
    runpy.run_path(str(p),run_name='__main__')
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_llm_tool_router.py", line 152, in <module>
    test_engine_can_refine_general_to_retrieval_route()
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_llm_tool_router.py", line 141, in test_engine_can_refine_general_to_retrieval_route
    assert any(item.stage == "tool_route_refine" for item in result.trace)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError
```
## 138. common / smoke_test_members_and_game_knowledge.py

{"file": "smoke_test_members_and_game_knowledge.py", "status": "failed", "exit_code": 1, "elapsed": 33.55490850005299}

[smoke_test_members_and_game_knowledge.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_members_and_game_knowledge.log)

```text
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_members_and_game_knowledge.py", line 130, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_members_and_game_knowledge.py", line 44, in main
    check(
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_members_and_game_knowledge.py", line 21, in check
    raise AssertionError(f"{question}: missing {missing}\n{answer}")
AssertionError: สมาชิกทีมมีใครบ้าง: missing ['Members', 'cooperative education and Internship student', 'PSU Phuket Esports Club - PSU Phuket', 'นายชนะชัย', 'นายษุภากรณ์']
เงื่อนไขสมาชิกของศูนย์ใช้แทนข้อกำหนดบัญชีเกมหรือสมาชิกทีมไม่ได้ครับ ต้องตรวจข้อกำหนดของบัญชีเกมหรือรายการแข่งขันนั้นแยกกัน
```
## 139. common / smoke_test_model_first_rag_flow.py

{"file": "smoke_test_model_first_rag_flow.py", "status": "failed", "exit_code": 1, "elapsed": 14.178381999954581}

[smoke_test_model_first_rag_flow.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_model_first_rag_flow.log)

```text
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_model_first_rag_flow.py", line 242, in test_hybrid_retrieval_keeps_default_path_healthy
    hits, trace = retrieve_hybrid_guarded("เกมแนวแข่งรถมีอะไรบ้าง", PipelineRoute("games", "game_catalog_lookup", 0.9, "list", "low", "smoke"))
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\hybrid_retrieval.py", line 204, in retrieve_hybrid_guarded
    curated_hits, curated_trace = retrieve_curated(query, route.category, limit=candidate_limit)
                                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\retrieval.py", line 900, in retrieve_curated
    return hits, PipelineTrace("rag_retrieval", "curated_lexical", confidence, detail, {"category": category, "game": competition_game, "intent": competition_intent,"common_ownership_blocked":ownership_blocked})
                                                                                                                                                                                                ^^^^^^^^^^^^^^^^^
NameError: name 'ownership_blocked' is not defined
```
## 140. common / smoke_test_pc_service_fee.py

{"file": "smoke_test_pc_service_fee.py", "status": "passed", "exit_code": 0, "elapsed": 55.99689319985919}

[smoke_test_pc_service_fee.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_pc_service_fee.log)
## 141. common / smoke_test_performance_trace.py

{"file": "smoke_test_performance_trace.py", "status": "passed", "exit_code": 0, "elapsed": 7.344919400056824}

[smoke_test_performance_trace.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_performance_trace.log)
## 142. common / smoke_test_pipeline_fixes_20260823.py

{"file": "smoke_test_pipeline_fixes_20260823.py", "status": "failed", "exit_code": 1, "elapsed": 21.884657100075856}

[smoke_test_pipeline_fixes_20260823.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_pipeline_fixes_20260823.log)

```text
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 3565, in _answer_single
    source_hits, source_trace = retrieve_curated(
                                ^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\retrieval.py", line 900, in retrieve_curated
    return hits, PipelineTrace("rag_retrieval", "curated_lexical", confidence, detail, {"category": category, "game": competition_game, "intent": competition_intent,"common_ownership_blocked":ownership_blocked})
                                                                                                                                                                                                ^^^^^^^^^^^^^^^^^
NameError: name 'ownership_blocked' is not defined
```
## 143. common / smoke_test_pipeline_timing.py

{"file": "smoke_test_pipeline_timing.py", "status": "failed", "exit_code": 1, "elapsed": 9.032697800081223}

[smoke_test_pipeline_timing.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_pipeline_timing.log)

```text
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_pipeline_timing.py", line 56, in <module>
    test_single_question_timing_trace()
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_pipeline_timing.py", line 33, in test_single_question_timing_trace
    _assert_timing_metadata(result)
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_pipeline_timing.py", line 20, in _assert_timing_metadata
    assert timing_items, "pipeline result should include timing trace entries"
           ^^^^^^^^^^^^
AssertionError: pipeline result should include timing trace entries
```
## 144. common / smoke_test_pipeline_warmup.py

{"file": "smoke_test_pipeline_warmup.py", "status": "failed", "exit_code": 1, "elapsed": 60.3370860000141}

[smoke_test_pipeline_warmup.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_pipeline_warmup.log)

```text
    runpy.run_path(str(p),run_name='__main__')
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_pipeline_warmup.py", line 34, in <module>
    test_pipeline_warmup()
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_pipeline_warmup.py", line 17, in test_pipeline_warmup
    assert result.ok, result.errors
           ^^^^^^^^^
AssertionError: ('probe_queries: NameError("name \'ownership_blocked\' is not defined")',)
```
## 145. common / smoke_test_pipeline_worker_supervisor.py

{"file": "smoke_test_pipeline_worker_supervisor.py", "status": "failed", "exit_code": 1, "elapsed": 20.03612419986166}

[smoke_test_pipeline_worker_supervisor.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_pipeline_worker_supervisor.log)

```text
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_pipeline_worker_supervisor.py", line 45, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_pipeline_worker_supervisor.py", line 30, in main
    assert call.result.route.category == "overview"
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError
```
## 146. common / smoke_test_pipeline_worker_timeout_recovery.py

{"file": "smoke_test_pipeline_worker_timeout_recovery.py", "status": "failed", "exit_code": 1, "elapsed": 31.49673489993438}

[smoke_test_pipeline_worker_timeout_recovery.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_pipeline_worker_timeout_recovery.log)

```text
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_pipeline_worker_timeout_recovery.py", line 59, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_pipeline_worker_timeout_recovery.py", line 51, in main
    assert recovered.result.route.category == "overview"
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError
```
## 147. common / smoke_test_product_sla_guards.py

{"file": "smoke_test_product_sla_guards.py", "status": "passed", "exit_code": 0, "elapsed": 10.223416999913752}

[smoke_test_product_sla_guards.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_product_sla_guards.log)
## 148. common / smoke_test_query_planner.py

{"file": "smoke_test_query_planner.py", "status": "failed", "exit_code": 1, "elapsed": 11.71327990014106}

[smoke_test_query_planner.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_query_planner.log)

```text
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_query_planner.py", line 194, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_query_planner.py", line 187, in main
    test_engine_uses_validated_plan_without_second_intent_call()
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_query_planner.py", line 168, in test_engine_uses_validated_plan_without_second_intent_call
    assert result.mode == "pipeline:multi_question_splitter", result.mode
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: pipeline:common_answer
```
## 149. common / smoke_test_rag_after_deterministic_fallback.py

{"file": "smoke_test_rag_after_deterministic_fallback.py", "status": "failed", "exit_code": 1, "elapsed": 8.048709100112319}

[smoke_test_rag_after_deterministic_fallback.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_rag_after_deterministic_fallback.log)

```text
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_rag_after_deterministic_fallback.py", line 163, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_rag_after_deterministic_fallback.py", line 154, in main
    test_general_fallback_reads_rag_before_grounded_llm()
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_rag_after_deterministic_fallback.py", line 47, in test_general_fallback_reads_rag_before_grounded_llm
    assert calls == ["rag", "llm"], calls
           ^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: []
```
## 150. common / smoke_test_real_usage_golden.py

{"file": "smoke_test_real_usage_golden.py", "status": "failed", "exit_code": 1, "elapsed": 76.22461290005594}

[smoke_test_real_usage_golden.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_real_usage_golden.log)

```text
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 3565, in _answer_single
    source_hits, source_trace = retrieve_curated(
                                ^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\retrieval.py", line 900, in retrieve_curated
    return hits, PipelineTrace("rag_retrieval", "curated_lexical", confidence, detail, {"category": category, "game": competition_game, "intent": competition_intent,"common_ownership_blocked":ownership_blocked})
                                                                                                                                                                                                ^^^^^^^^^^^^^^^^^
NameError: name 'ownership_blocked' is not defined
```
## 151. common / smoke_test_repeated_character_variants.py

{"file": "smoke_test_repeated_character_variants.py", "status": "passed", "exit_code": 0, "elapsed": 8.58958170004189}

[smoke_test_repeated_character_variants.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_repeated_character_variants.log)
## 152. common / smoke_test_request_deadline.py

{"file": "smoke_test_request_deadline.py", "status": "failed", "exit_code": 1, "elapsed": 8.848539699800313}

[smoke_test_request_deadline.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_request_deadline.log)

```text
    runpy.run_path(str(p),run_name='__main__')
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_request_deadline.py", line 40, in <module>
    test_global_deadline_can_stop_request()
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_request_deadline.py", line 21, in test_global_deadline_can_stop_request
    assert result.mode == "pipeline:request_timeout_no_answer", result.mode
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: pipeline:common_answer
```
## 153. common / smoke_test_runtime_input_quality_guard.py

{"file": "smoke_test_runtime_input_quality_guard.py", "status": "failed", "exit_code": 1, "elapsed": 7.980370400007814}

[smoke_test_runtime_input_quality_guard.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_runtime_input_quality_guard.log)

```text
    runpy.run_path(str(p),run_name='__main__')
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_runtime_input_quality_guard.py", line 60, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_runtime_input_quality_guard.py", line 27, in main
    raise AssertionError(f"expected repeated-character retry, got {repeated}")
AssertionError: expected repeated-character retry, got InputQualityDecision(detected_action='request_retype', applied_action='warn_and_continue', should_short_circuit=False, message='ข้อความนี้อาจมีตัวอักษรซ้ำโดยไม่ตั้งใจ กรุณาตรวจสอบและพิมพ์คำถามใหม่อีกครั้งครับ', features=AnomalyFeatures(input_text='จอองแล้วแก้ไขได้ไหม', layout_score=0.001667, layout_direction='english_intended_thai_active', layout_candidate_preview=None, layout_reason='mapping lacks stronger English orthographic/lexical evidence', layout_spans=(SpanEvidence(direction='english_intended_thai_active', source_span='จอองแล้วแก้ไขได้ไหม', mapped_span="0vv'c]h;cdhw-wfhws,", start=0, end=19, score=0.001667, source_quality=0.686297, target_quality=0.203102, target_seen=False, source_protected=False, reason='mapping lacks stronger English orthographic/lexical evidence'),), repeat_score=0.559482, repeat_candidate_preview='จองแล้วแก้ไขได้ไหม', repeat_reason='removing one repeated character improves quality 0.686->0.763; seen False->False', repeat_spans=(RepeatEvidence(source_span='ออ', candidate_span='จอง … [ย่อจาก2,336ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```
## 154. common / smoke_test_scope_guard_fallback.py

{"file": "smoke_test_scope_guard_fallback.py", "status": "failed", "exit_code": 1, "elapsed": 11.288574300007895}

[smoke_test_scope_guard_fallback.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_scope_guard_fallback.log)

```text
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_scope_guard_fallback.py", line 42, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_scope_guard_fallback.py", line 34, in main
    assert result.route.category == "no_answer", (question, result.route.category, result.mode)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: ('เครื่องไหนดีที่สุด', 'knowledge', 'pipeline:common_answer')
```
## 155. common / smoke_test_semantic_general_bypass.py

{"file": "smoke_test_semantic_general_bypass.py", "status": "passed", "exit_code": 0, "elapsed": 7.251933400053531}

[smoke_test_semantic_general_bypass.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_semantic_general_bypass.log)
## 156. common / smoke_test_semantic_rag.py

{"file": "smoke_test_semantic_rag.py", "status": "passed", "exit_code": 0, "elapsed": 13.098892300156876}

[smoke_test_semantic_rag.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_semantic_rag.log)
## 157. common / smoke_test_semantic_target_filter.py

{"file": "smoke_test_semantic_target_filter.py", "status": "passed", "exit_code": 0, "elapsed": 7.236151200020686}

[smoke_test_semantic_target_filter.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_semantic_target_filter.log)
## 158. common / smoke_test_session_context.py

{"file": "smoke_test_session_context.py", "status": "failed", "exit_code": 1, "elapsed": 17.259201199980453}

[smoke_test_session_context.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_session_context.log)

```text
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_session_context.py", line 270, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_session_context.py", line 61, in main
    assert result.mode == "pipeline:structured_service_game_availability", result.mode
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: pipeline:common_list
```
## 159. common / smoke_test_shadow_critic.py

{"file": "smoke_test_shadow_critic.py", "status": "passed", "exit_code": 0, "elapsed": 37.31725930003449}

[smoke_test_shadow_critic.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_shadow_critic.log)
## 160. common / smoke_test_source_contract.py

{"file": "smoke_test_source_contract.py", "status": "failed", "exit_code": 1, "elapsed": 18.51717139990069}

[smoke_test_source_contract.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_source_contract.log)

```text
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_source_contract.py", line 98, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_source_contract.py", line 64, in main
    assert_has(pc_ids, SERVICE_FEE_IMAGE_2026_ID, "pc pipeline")
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_source_contract.py", line 37, in assert_has
    raise AssertionError(f"{label}: missing source id {expected}; got {ids}")
AssertionError: pc pipeline: missing source id service_fee_image_2026; got ['pc_service_fee_local_update_20260727']
```
## 161. common / smoke_test_structured_tools.py

{"file": "smoke_test_structured_tools.py", "status": "failed", "exit_code": 1, "elapsed": 20.100132700055838}

[smoke_test_structured_tools.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_structured_tools.log)

```text
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_structured_tools.py", line 181, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_structured_tools.py", line 30, in main
    assert result.mode == "pipeline:structured_members_group_count", result.mode
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: pipeline:user_service_facts
```
## 162. common / smoke_test_surface_input_recovery.py

{"file": "smoke_test_surface_input_recovery.py", "status": "passed", "exit_code": 0, "elapsed": 14.530024799983948}

[smoke_test_surface_input_recovery.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_surface_input_recovery.log)
## 163. common / smoke_test_target_lock.py

{"file": "smoke_test_target_lock.py", "status": "passed", "exit_code": 0, "elapsed": 9.378892000066116}

[smoke_test_target_lock.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_target_lock.log)
## 164. common / smoke_test_target_resolver.py

{"file": "smoke_test_target_resolver.py", "status": "passed", "exit_code": 0, "elapsed": 9.108692599926144}

[smoke_test_target_resolver.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_target_resolver.log)
## 165. common / smoke_test_timeout_routing_resolver_remediation.py

{"file": "smoke_test_timeout_routing_resolver_remediation.py", "status": "failed", "exit_code": 1, "elapsed": 15.94155770004727}

[smoke_test_timeout_routing_resolver_remediation.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_timeout_routing_resolver_remediation.log)

```text
  File "<frozen runpy>", line 287, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_timeout_routing_resolver_remediation.py", line 61, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_timeout_routing_resolver_remediation.py", line 51, in main
    assert answer.route.category == "overview"
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError
```
## 166. common / smoke_test_tool_preconditions.py

{"file": "smoke_test_tool_preconditions.py", "status": "passed", "exit_code": 0, "elapsed": 9.24027800001204}

[smoke_test_tool_preconditions.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_tool_preconditions.log)
## 167. common / smoke_test_typo_intent_recovery.py

{"file": "smoke_test_typo_intent_recovery.py", "status": "passed", "exit_code": 0, "elapsed": 14.198677900014445}

[smoke_test_typo_intent_recovery.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_typo_intent_recovery.log)
## 168. common / smoke_test_universal_intent.py

{"file": "smoke_test_universal_intent.py", "status": "failed", "exit_code": 1, "elapsed": 22.80066359997727}

[smoke_test_universal_intent.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_universal_intent.log)

```text
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_universal_intent.py", line 148, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_universal_intent.py", line 71, in main
    check(
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_universal_intent.py", line 24, in check
    raise AssertionError(f"{question}: missing universal intent")
AssertionError: สมาชิกใน PSU Esport มีกี่หมวด: missing universal intent
```
## 169. common / smoke_test_update.py

{"file": "smoke_test_update.py", "status": "failed", "exit_code": 1, "elapsed": 6.3395849000662565}

[smoke_test_update.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_update.log)

```text
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_update.py", line 54, in <module>
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_update.py", line 37, in main
    assert_contains(result["answer"], expected, question)
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_update.py", line 19, in assert_contains
    raise AssertionError(f"{label}: expected {expected!r} in {text!r}")
AssertionError: เด็กจุฬา เล่น PC กี่บาท: expected 'มหาลัยอื่น' in 'ราคา PC 1 ชั่วโมง (1 คน) สำหรับ ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student)\n•    25 บาท\nหมายเหตุข้อมูล PC: ราคา PC เพิ่มจาก local service fee update 2026-07-27\nแหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png'
```
## 170. common / smoke_test_versioned_game_resolution.py

{"file": "smoke_test_versioned_game_resolution.py", "status": "failed", "exit_code": 1, "elapsed": 11.23295610002242}

[smoke_test_versioned_game_resolution.log](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_smokes/smoke_test_versioned_game_resolution.log)

```text
    raise SystemExit(main())
                     ^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\smoke_test_versioned_game_resolution.py", line 37, in main
    assert "Overcooked! 2" in answer.answer, answer.answer
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: **ปุ่มควบคุมเกม**
• ปุ่มควบคุม: เพิ่มทีละปุ่มหรือชุดปุ่ม: ยังไม่มีข้อมูลยืนยัน
• แพลตฟอร์ม เช่น PC หรือ PS5: PlayStation / PS5 [S1]
• อุปกรณ์ควบคุม: ยังไม่มีข้อมูลยืนยัน
• ชื่อชุดปุ่ม เช่น default: ยังไม่มีข้อมูลยืนยัน
```
