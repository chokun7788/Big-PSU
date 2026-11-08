# Native unit failures/errors ทุกevent

ข้อมูลจากtemp_fixedทั้ง899functionsต่อformat; subtesteventsอาจซ้ำfunction; fixture4ข้อrerunผ่านแยกในR64; stackฉบับเต็มยังอยู่ในJSON/logเดิม

## 1. legacy / failures / test_planner_accepts_only_relevant_schema_fields (tests.test_common_content_r58.CommonTests.test_planner_accepts_only_relevant_schema_fields)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_common_content_r58.py", line 175, in test_planner_accepts_only_relevant_schema_fields
    for p in ({'requested_fields':['amount_minor'],'all_fields':False,'platform':None},{'requested_fields':['bindings'],'all_fields':False,'platform':'PS4'},{'requested_fields':['bindings'],'all_fields':'true','platform':None}):self.assertIsNone(checked_plan(p,ids,records))
                                                                                                                                                                                                                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: {'requested_fields': ['amount_minor'], 'all_fields': False, 'platform': None, 'method': 'bounded_llm_schema_fields'} is not None

```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 2. legacy / failures / test_truncated_numbered_clause_does_not_borrow_other_penalties (tests.test_competition_composition_r28_20261001.CompositionR28Tests.test_truncated_numbered_clause_does_not_borrow_other_penalties)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_composition_r28_20261001.py", line 46, in test_truncated_numbered_clause_does_not_borrow_other_penalties
    self.assertIn('no_answer',result.mode);self.assertFalse(result.hits)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 'no_answer' not found in 'pipeline:competition_rule_full_sections_source'

```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 3. legacy / failures / test_english_general_match_issue_does_not_use_bug_or_post_match_text (tests.test_competition_target_grounding.CompetitionTargetGroundingTests.test_english_general_match_issue_does_not_use_bug_or_post_match_text)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_target_grounding.py", line 271, in test_english_general_match_issue_does_not_use_bug_or_post_match_text
    self.assertEqual(result.mode, "pipeline:competition_facet_not_covered_no_answer_en")
AssertionError: 'pipeline:user_service_facts' != 'pipeline:competition_facet_not_covered_no_answer_en'
- pipeline:user_service_facts
+ pipeline:competition_facet_not_covered_no_answer_en


```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 4. legacy / failures / test_in_match_contact_requires_a_contact_instruction (tests.test_competition_target_grounding.CompetitionTargetGroundingTests.test_in_match_contact_requires_a_contact_instruction)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_target_grounding.py", line 161, in test_in_match_contact_requires_a_contact_instruction
    self.assertEqual(result.mode, "pipeline:competition_facet_not_covered_no_answer")
AssertionError: 'pipeline:user_service_facts' != 'pipeline:competition_facet_not_covered_no_answer'
- pipeline:user_service_facts
+ pipeline:competition_facet_not_covered_no_answer


```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 5. legacy / failures / test_alumni_price_does_not_fall_back_to_all_groups (tests.test_input_downstream_r29_20261002.InputDownstreamR29Tests.test_alumni_price_does_not_fall_back_to_all_groups)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_input_downstream_r29_20261002.py", line 28, in test_alumni_price_does_not_fall_back_to_all_groups
    self.assertIn('PSU alumni and students from other institutions: 50 THB',result.answer)
AssertionError: 'PSU alumni and students from other institutions: 50 THB' not found in 'Service prices (recorded package rates):\n\nNintendo Switch — 60 minutes/package (1-2 people)\nRequested duration: 60 minutes (1 hours); 1 session(s).\n• PSU alumni / students from other institutions: 50 THB/package\n\nNintendo Switch — 60 minutes/package (3-4 people)\nRequested duration: 60 minutes (1 hours); 1 session(s).\n• PSU alumni / students from other institutions: 100 THB/package\nThe original fee table states validity through 2026-03-31; continued validity for the requested date has not been confirmed.\nSource: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png'

```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 6. legacy / failures / test_eligibility_label_and_duration_are_kept_in_compound_price (tests.test_input_downstream_r29_20261002.InputDownstreamR29Tests.test_eligibility_label_and_duration_are_kept_in_compound_price)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_input_downstream_r29_20261002.py", line 22, in test_eligibility_label_and_duration_are_kept_in_compound_price
    self.assertIn('120 minutes, charged as 2 session', result.answer)
AssertionError: '120 minutes, charged as 2 session' not found in 'Service prices (recorded package rates):\n\nNintendo Switch — 60 minutes/package (1-2 people)\nRequested duration: 120 minutes (2 hours); 2 session(s).\n• PSU students and staff: 0 THB/package × 2 = 0 THB\n\nNintendo Switch — 60 minutes/package (3-4 people)\nRequested duration: 120 minutes (2 hours); 2 session(s).\n• PSU students and staff: 0 THB/package × 2 = 0 THB\nThe original fee table states validity through 2026-03-31; continued validity for the requested date has not been confirmed.\nSource: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png'

```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 7. legacy / failures / test_price_words_can_recover_two_errors_with_values_unchanged (tests.test_input_downstream_r29_20261002.InputDownstreamR29Tests.test_price_words_can_recover_two_errors_with_values_unchanged)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_input_downstream_r29_20261002.py", line 18, in test_price_words_can_recover_two_errors_with_values_unchanged
    self.assertIn('60 minutes, charged as 1 session', result.answer)
AssertionError: '60 minutes, charged as 1 session' not found in 'Service prices (recorded package rates):\n\nVR — 60 minutes/package (1-5 people)\nRequested duration: 60 minutes (1 hours); 1 session(s).\n• PSU students and staff: 0 THB/package\nThe original fee table states validity through 2026-03-31; continued validity for the requested date has not been confirmed.\nSource: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png'

```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 8. legacy / failures / test_semantic_cases (tests.test_integrated_improvement_r21_20261001.IntegratedImprovementTests.test_semantic_cases) (case='tuesday-afternoon')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_integrated_improvement_r21_20261001.py", line 59, in test_semantic_cases
    self.assertTrue(row['passed'], row)
AssertionError: False is not true : {'id': 'tuesday-afternoon', 'locale': 'en', 'question': 'What are the afteronon opening hours on Tuesday', 'expected_route': 'schedule', 'required_groups': (('Tuesday',), ('13:00-16:00',)), 'forbidden': ('09:00-12:00',), 'expected_live_fetch': False, 'live_fetches': 0, 'route': 'schedule', 'mode': 'pipeline:source_operation_schedule_query', 'answer': 'Tuesday: 09:00-12:00 is open for play; 13:00-16:00 is open for play.\nSource: https://esports.computing.psu.ac.th/ (original source in Thai)', 'elapsed_sec': 0.5943, 'passed': False, 'failures': ['forbidden 09:00-12:00'], 'trace': [{'stage': 'timing', 'decision': 'locale_resolution', 'confidence': 1.0, 'detail': '', 'metadata': {'elapsed_ms': 0.13, 'elapsed_sec': 0.0001, 'global_timeout_enabled': True, 'global_timeout_sec': 20.0, 'global_elapsed_sec': 0.0002, 'global_remaining_sec': 19.9998, 'finalizer_reserve_sec': 1.0, 'work_remaining_sec': 18.9998, 'timing_status': 'running'}}, {'stage': 'timing', 'decision': 'intent_cue_preflight', 'confidence': 1.0, 'detail': '', 'metadata': {'elapsed_ms': 79.31, 'elapsed_sec': 0.0793, 'global_timeout_enabled': True, 'global_timeout_sec': 20.0, 'global_elapsed_sec': 0.3284, 'global_remaining_sec': 19.6716, 'finalizer_reserve_sec': 1.0, 'work_remaining_sec': 18.6716, 'timing_status': 'running'}}, {'stage': 'timing', 'decision': 'canonical_preflight', 'confidence': 1.0, 'detail': '', 'metadata': {'elapsed_ms': 0.04, 'elapsed_sec': 0.0, 'global_timeout_enabled': True, 'glo … [ย่อจาก4,761ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 9. legacy / failures / test_semantic_cases (tests.test_integrated_improvement_r21_20261001.IntegratedImprovementTests.test_semantic_cases) (case='compound-price-unclear-action')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_integrated_improvement_r21_20261001.py", line 59, in test_semantic_cases
    self.assertTrue(row['passed'], row)
AssertionError: False is not true : {'id': 'compound-price-unclear-action', 'locale': 'th', 'question': 'PC 2 ชั่วโมง บุคคลทั่วไป ราคาเท่าไหร่ แล้วของยังไง', 'expected_route': 'multi_question', 'required_groups': (('140 บาท',), ('จอง',), ('หมายถึง',)), 'forbidden': (), 'expected_live_fetch': False, 'live_fetches': 0, 'route': 'service_fee', 'mode': 'pipeline:structured_service_fee_conversation', 'answer': 'ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:\n\nPC — 60 นาที/แพ็กเกจ (1 คน)\nระยะเวลาที่ถาม 120 นาที (2 ชั่วโมง) คิดเป็น 2 session (แพ็กเกจ)\n•    บุคคลทั่วไป (General Adult): 70 บาท/แพ็กเกจ × 2 = 140 บาท\nราคา PC อ้างอิงข้อมูลปรับปรุงในระบบวันที่ 2026-07-27\nแหล่งข้อมูล: local://service_fee/pc_price_update_20260727', 'elapsed_sec': 0.2442, 'passed': False, 'failures': ['route service_fee != multi_question', "missing group ('จอง',)", "missing group ('หมายถึง',)"], 'trace': [{'stage': 'timing', 'decision': 'locale_resolution', 'confidence': 1.0, 'detail': '', 'metadata': {'elapsed_ms': 0.12, 'elapsed_sec': 0.0001, 'global_timeout_enabled': True, 'global_timeout_sec': 20.0, 'global_elapsed_sec': 0.0002, 'global_remaining_sec': 19.9998, 'finalizer_reserve_sec': 1.0, 'work_remaining_sec': 18.9998, 'timing_status': 'running'}}, {'stage': 'timing', 'decision': 'intent_cue_preflight', 'confidence': 1.0, 'detail': '', 'metadata': {'elapsed_ms': 108.84, 'elapsed_sec': 0.1088, 'global_timeout_enabled': True, 'global_timeout_sec': 20.0, 'global_elapsed_sec': 0.2262, 'global_remaining_sec': 19.7738, 'finaliz … [ย่อจาก5,684ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 10. legacy / failures / test_routes_match_requested_operations (tests.test_intent_cue_recovery_20260930.IntentCueRecoveryTests.test_routes_match_requested_operations)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_cue_recovery_20260930.py", line 68, in test_routes_match_requested_operations
    self.assertIn("เกมที่ยืนยันได้", compound.answer)
AssertionError: 'เกมที่ยืนยันได้' not found in "คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:\n\nคำถามที่ 1: PS5 ราคาเท่าไหร่\nราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:\n\nPlayStation 5 — 60 นาที/แพ็กเกจ (1-2 คน)\n•    นักศึกษา/นักเรียน/บุคลากร PSU (PSU Student and Staff): 0 บาท/แพ็กเกจ\n•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 50 บาท/แพ็กเกจ\n•    บุคคลทั่วไป (General Adult): 150 บาท/แพ็กเกจ\nตารางต้นฉบับระบุมีผลถึง 2026-03-31 ยังไม่ยืนยันการต่ออายุสำหรับวันที่ต้องการ ตัวเลขด้านบนเป็นอัตราที่บันทึกไว้ครับ\nแหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png\n\nคำถามที่ 2: PlayStation 5 มีเกมอะไรบ้าง\nเกมที่มีข้อมูลยืนยันในโซนที่ถาม\n\nPlayStation 5 Zone (17 เกม)\n•    Call of Duty: Modern Warfare III\n•    Delta Force\n•    EA Sports FC 24\n•    eFootball\n•    FINAL FANTASY XVI\n•    Fortnite\n•    God of War Ragnarok\n•    Hogwarts Legacy\n•    Marvel's Spider-Man 2\n•    NARUTO X BORUTO Ultimate Ninja Storm Connections\n•    Resident Evil 4\n•    Resident Evil Village\n•    TEKKEN 8\n•    THE FINALS\n•    The Last of Us Part I\n•    The Last of Us Part II (Remastered)\n•    Uncharted: Legacy of Thieves Collection\nแหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games"

```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 11. legacy / failures / test_ps5_controller_model_is_not_a_game_button_question (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_ps5_controller_model_is_not_a_game_button_question)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 71, in test_ps5_controller_model_is_not_a_game_button_question
    self.assertEqual(game_buttons.route.category, "games")
AssertionError: 'game_controls' != 'games'
- game_controls
+ games


```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 12. legacy / failures / test_public_access_questions_use_the_requested_facet (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_public_access_questions_use_the_requested_facet) (question='What ID does an external visitor need to use the studio?')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 335, in test_public_access_questions_use_the_requested_facet
    self.assertIn("https://esports.computing.psu.ac.th/", result.answer)
AssertionError: 'https://esports.computing.psu.ac.th/' not found in 'At arrival, present a national ID card, university student card, school student card, or passport.\n\nSource: user-provided service answers (2026-10-08)\n\nlocal://service_policy/user_answers_20261008'

```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 13. legacy / failures / test_public_access_questions_use_the_requested_facet (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_public_access_questions_use_the_requested_facet) (question='Does a public visitor need membership before entering?')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 334, in test_public_access_questions_use_the_requested_facet
    self.assertIn(expected, result.answer)
AssertionError: 'do not need to be a PSU student' not found in 'Membership is not required to use the studio.\n\nSource: user-provided service answers (2026-10-08)\n\nlocal://service_policy/user_answers_20261008'

```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 14. legacy / failures / test_specific_policy_facets_beat_generic_public_access (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_specific_policy_facets_beat_generic_public_access) (question='Does a non-PSU guest need a membership or national ID?')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 354, in test_specific_policy_facets_beat_generic_public_access
    self.assertIn(expected, result.answer)
AssertionError: 'National ID' not found in 'Membership is not required to use the studio.\n\nAt arrival, present a national ID card, university student card, school student card, or passport.\n\nSource: user-provided service answers (2026-10-08)\n\nlocal://service_policy/user_answers_20261008'

```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 15. legacy / failures / test_explicit_negative_rule_beats_broad_member_or_equipment_signal (tests.test_master_ground_truth_route_regressions.MasterGroundTruthRouteRegressionTests.test_explicit_negative_rule_beats_broad_member_or_equipment_signal)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_master_ground_truth_route_regressions.py", line 87, in test_explicit_negative_rule_beats_broad_member_or_equipment_signal
    self.assertEqual("no_answer", membership.route.category)
AssertionError: 'no_answer' != 'reservation'
- no_answer
+ reservation


```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 16. legacy / failures / test_phrase_recovery_keeps_resource_and_duration (tests.test_multi_error_typo_recovery_20260929.MultiErrorTypoRecoveryTests.test_phrase_recovery_keeps_resource_and_duration) (question='PS5 ราาคาเท่าไหน่')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_multi_error_typo_recovery_20260929.py", line 58, in test_phrase_recovery_keeps_resource_and_duration
    self.assertEqual(_answer(question).route.intent, intent)
AssertionError: 'conversation_price_lookup' != 'service_fee_query'
- conversation_price_lookup
+ service_fee_query


```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 17. legacy / failures / test_planner_accepts_only_relevant_schema_fields (tests.test_common_content_r58.CommonTests.test_planner_accepts_only_relevant_schema_fields)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_common_content_r58.py", line 175, in test_planner_accepts_only_relevant_schema_fields
    for p in ({'requested_fields':['amount_minor'],'all_fields':False,'platform':None},{'requested_fields':['bindings'],'all_fields':False,'platform':'PS4'},{'requested_fields':['bindings'],'all_fields':'true','platform':None}):self.assertIsNone(checked_plan(p,ids,records))
                                                                                                                                                                                                                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: {'requested_fields': ['amount_minor'], 'all_fields': False, 'platform': None, 'method': 'bounded_llm_schema_fields'} is not None

```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 18. legacy / failures / test_unknown_button_returns_no_mapping (tests.test_r30_closed_query_boundaries.R30BoundaryTests.test_unknown_button_returns_no_mapping) (q='ปุ่ม R9 ใน Gran Turismo 7 ใช้ทำอะไร')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_r30_closed_query_boundaries.py", line 33, in test_unknown_button_returns_no_mapping
    self.assertIn('no_answer',r.mode);self.assertNotIn('Accelerate',r.answer);self.assertNotIn('•    R2:',r.answer)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 'no_answer' not found in 'pipeline:source_operation_control_lookup'

```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 19. legacy / failures / test_source_supported_focused_cases (tests.test_reliability_flow_20261001.ReliabilityFlowTests.test_source_supported_focused_cases) (id='compound-th-connector')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_reliability_flow_20261001.py", line 132, in test_source_supported_focused_cases
    self.assertTrue(result["passed"], result["failures"])
AssertionError: False is not true : ['route service_fee != multi_question']

```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 20. legacy / failures / test_engine_routes_translation_before_quoted_booking_policy (tests.test_semantic_quality_r53.SemanticQualityTests.test_engine_routes_translation_before_quoted_booking_policy)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_semantic_quality_r53.py", line 55, in test_engine_routes_translation_before_quoted_booking_policy
    self.assertEqual(result.route.category,'general')
AssertionError: 'no_answer' != 'general'
- no_answer
+ general


```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 21. legacy / failures / test_compound_price_and_controls_preserve_both_orders_and_languages (tests.test_targeted_dialogue_r40.TargetedDialogueR40Tests.test_compound_price_and_controls_preserve_both_orders_and_languages)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_targeted_dialogue_r40.py", line 169, in test_compound_price_and_controls_preserve_both_orders_and_languages
    self.assertEqual({t.decision.split('/')[0] for t in children}, {'games','service_fee'})
AssertionError: Items in the first set but not the second:
'game_controls'
Items in the second set but not the first:
'games'

```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 22. legacy / failures / test_multiple_catalog_targets_do_not_drop_second_zone (tests.test_targeted_dialogue_r40.TargetedDialogueR40Tests.test_multiple_catalog_targets_do_not_drop_second_zone)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_targeted_dialogue_r40.py", line 70, in test_multiple_catalog_targets_do_not_drop_second_zone
    self.assertIn('PC Zone', result.answer)
AssertionError: 'PC Zone' not found in 'This request reached the processing time limit, so it was stopped to keep the service responsive.\nPlease try a more specific question, such as naming the zone, game, or topic directly.'

```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 23. legacy / failures / test_explicit_remastered_title_is_not_part_one (tests.test_thai_noisy_input_flow_20260929.ThaiNoisyInputFlowTests.test_explicit_remastered_title_is_not_part_one)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_thai_noisy_input_flow_20260929.py", line 67, in test_explicit_remastered_title_is_not_part_one
    self.assertIn("PlayStation 5", answer.answer)
AssertionError: 'PlayStation 5' not found in 'ยังไม่พบข้อมูลยืนยันของ the last of us part ii ในรายการเกมของศูนย์ครับ กรุณายืนยันชื่อเกมและภาคที่ต้องการอีกครั้ง\nแหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games'

```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 24. legacy / errors / test_dispute_resolution_is_not_display_resolution (tests.test_competition_composition_r28_20261001.CompositionR28Tests.test_dispute_resolution_is_not_display_resolution)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_composition_r28_20261001.py", line 104, in test_dispute_resolution_is_not_display_resolution
    result=answer('What do the CS2 tournament rules say about dispute resolution?','en')
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_composition_r28_20261001.py", line 8, in answer
    return answer_question_pipeline_debug(q,locale=locale,experimental_allow_llm=False,experimental_rag_fallback=True)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4712, in answer_question_pipeline_debug
    return get_pipeline().answer(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1898, in _answer_single
    english_result = answer_english_supported(
                     ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeli … [ย่อจาก2,936ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 25. legacy / errors / test_all_thai_penalty_types_and_conditions (tests.test_competition_content_speed_r26_20261001.CompetitionContentSpeed.test_all_thai_penalty_types_and_conditions)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_content_speed_r26_20261001.py", line 53, in test_all_thai_penalty_types_and_conditions
    result=self.answer('กติกา VALORANT มีบทลงโทษประเภทไหนบ้าง')
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_content_speed_r26_20261001.py", line 19, in answer
    return answer_question_pipeline_debug(q,locale=locale,experimental_allow_llm=llm,experimental_rag_fallback=True,global_timeout_sec=10)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4712, in answer_question_pipeline_debug
    return get_pipeline().answer(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 3565, in _answer_single
    source_hits, source_trace = retrieve_curated(
                                ^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\retr … [ย่อจาก2,314ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 26. legacy / errors / test_missing_pause_proposition_has_no_answer_mode (tests.test_competition_content_speed_r26_20261001.CompetitionContentSpeed.test_missing_pause_proposition_has_no_answer_mode) (locale='th')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_content_speed_r26_20261001.py", line 80, in test_missing_pause_proposition_has_no_answer_mode
    result=self.answer(q,locale)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_content_speed_r26_20261001.py", line 19, in answer
    return answer_question_pipeline_debug(q,locale=locale,experimental_allow_llm=llm,experimental_rag_fallback=True,global_timeout_sec=10)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4712, in answer_question_pipeline_debug
    return get_pipeline().answer(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 3565, in _answer_single
    source_hits, source_trace = retrieve_curated(
                                ^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\retrieval.py", line 900, in retrieve_curated
    return hit … [ย่อจาก2,259ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 27. legacy / errors / test_missing_pause_proposition_has_no_answer_mode (tests.test_competition_content_speed_r26_20261001.CompetitionContentSpeed.test_missing_pause_proposition_has_no_answer_mode) (locale='en')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_content_speed_r26_20261001.py", line 80, in test_missing_pause_proposition_has_no_answer_mode
    result=self.answer(q,locale)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_content_speed_r26_20261001.py", line 19, in answer
    return answer_question_pipeline_debug(q,locale=locale,experimental_allow_llm=llm,experimental_rag_fallback=True,global_timeout_sec=10)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4712, in answer_question_pipeline_debug
    return get_pipeline().answer(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1898, in _answer_single
    english_result = answer_english_supported(
                     ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\bilingual_english.py", line 2762, in answer_english_supported
    … [ย่อจาก2,868ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 28. legacy / errors / test_registered_game_and_facet_determine_intent (tests.test_competition_content_speed_r26_20261001.CompetitionContentSpeed.test_registered_game_and_facet_determine_intent) (q='สอบถามหน่อยครับ กติกา RoV เรื่องการหลุดจากเกมหรือการเชื่อมต่อ ว่าอย่างไร ครับ')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_content_speed_r26_20261001.py", line 25, in test_registered_game_and_facet_determine_intent
    result=self.answer(q,llm=True)
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_content_speed_r26_20261001.py", line 19, in answer
    return answer_question_pipeline_debug(q,locale=locale,experimental_allow_llm=llm,experimental_rag_fallback=True,global_timeout_sec=10)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4712, in answer_question_pipeline_debug
    return get_pipeline().answer(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 3565, in _answer_single
    source_hits, source_trace = retrieve_curated(
                                ^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\retrieval.py", line 900, in retrieve_curated
    return h … [ย่อจาก2,261ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 29. legacy / errors / test_tournament_format_first_sentence_is_format_not_hardware (tests.test_competition_content_speed_r26_20261001.CompetitionContentSpeed.test_tournament_format_first_sentence_is_format_not_hardware)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_content_speed_r26_20261001.py", line 33, in test_tournament_format_first_sentence_is_format_not_hardware
    result=self.answer(q,'en')
           ^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_content_speed_r26_20261001.py", line 19, in answer
    return answer_question_pipeline_debug(q,locale=locale,experimental_allow_llm=llm,experimental_rag_fallback=True,global_timeout_sec=10)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4712, in answer_question_pipeline_debug
    return get_pipeline().answer(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1898, in _answer_single
    english_result = answer_english_supported(
                     ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\bilingual_english.py", line 2762, in answer_english_suppor … [ย่อจาก2,875ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 30. legacy / errors / test_tournament_typo_uses_edit_distance_only_with_registered_target (tests.test_competition_content_speed_r26_20261001.CompetitionContentSpeed.test_tournament_typo_uses_edit_distance_only_with_registered_target)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_content_speed_r26_20261001.py", line 90, in test_tournament_typo_uses_edit_distance_only_with_registered_target
    result=self.answer(q,'en')
           ^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_content_speed_r26_20261001.py", line 19, in answer
    return answer_question_pipeline_debug(q,locale=locale,experimental_allow_llm=llm,experimental_rag_fallback=True,global_timeout_sec=10)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4712, in answer_question_pipeline_debug
    return get_pipeline().answer(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1898, in _answer_single
    english_result = answer_english_supported(
                     ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\bilingual_english.py", line 2762, in answer_english … [ย่อจาก2,882ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 31. legacy / errors / test_entry_timing_measures_before_split (tests.test_competition_contract_r27_20261001.AtomicGraderTests.test_entry_timing_measures_before_split)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_contract_r27_20261001.py", line 95, in test_entry_timing_measures_before_split
    result=answer_question_pipeline_debug('กติกา CS2 ทีมละกี่คน',experimental_allow_llm=False,experimental_rag_fallback=True)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4712, in answer_question_pipeline_debug
    return get_pipeline().answer(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 3565, in _answer_single
    source_hits, source_trace = retrieve_curated(
                                ^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\retrieval.py", line 900, in retrieve_curated
    return hits, PipelineTrace("rag_retrieval", "curated_lexical", confidence, detail, {"category": category, "game": competition_game, "intent": competition_intent,"common_ownership_blocked":ownership_blocked})
                                                                                                              … [ย่อจาก1,952ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 32. legacy / errors / test_cs2_english_table_preserves_pairs_and_continuation_reference (tests.test_competition_format_r25_20261001.CompetitionFormatAcceptance.test_cs2_english_table_preserves_pairs_and_continuation_reference)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_format_r25_20261001.py", line 73, in test_cs2_english_table_preserves_pairs_and_continuation_reference
    result = self.answer('Show the CS2 penalty table', 'en')
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_format_r25_20261001.py", line 23, in answer
    result = answer_question_pipeline_debug(question, locale=locale, experimental_allow_llm=False, experimental_rag_fallback=True, global_timeout_sec=10)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4712, in answer_question_pipeline_debug
    return get_pipeline().answer(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1898, in _answer_single
    english_result = answer_english_supported(
                     ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_202610 … [ย่อจาก2,956ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 33. legacy / errors / test_cs2_table_contains_all_nine_correct_thai_pairs (tests.test_competition_format_r25_20261001.CompetitionFormatAcceptance.test_cs2_table_contains_all_nine_correct_thai_pairs)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_format_r25_20261001.py", line 55, in test_cs2_table_contains_all_nine_correct_thai_pairs
    result = self.answer('ขอตารางบทลงโทษ CS2', 'th')
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_format_r25_20261001.py", line 23, in answer
    result = answer_question_pipeline_debug(question, locale=locale, experimental_allow_llm=False, experimental_rag_fallback=True, global_timeout_sec=10)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4712, in answer_question_pipeline_debug
    return get_pipeline().answer(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 3565, in _answer_single
    source_hits, source_trace = retrieve_curated(
                                ^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\r … [ย่อจาก2,317ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 34. legacy / errors / test_rovs_ipad_answer_is_permission_clause_not_document_heading (tests.test_competition_format_r25_20261001.CompetitionFormatAcceptance.test_rovs_ipad_answer_is_permission_clause_not_document_heading)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_format_r25_20261001.py", line 92, in test_rovs_ipad_answer_is_permission_clause_not_document_heading
    result = self.answer('Can I use a tablet or iPad in the RoV tournament?', 'en')
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_format_r25_20261001.py", line 23, in answer
    result = answer_question_pipeline_debug(question, locale=locale, experimental_allow_llm=False, experimental_rag_fallback=True, global_timeout_sec=10)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4712, in answer_question_pipeline_debug
    return get_pipeline().answer(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1898, in _answer_single
    english_result = answer_english_supported(
                     ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-p … [ย่อจาก3,000ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 35. legacy / errors / test_team_number_is_in_first_english_sentence (tests.test_competition_format_r25_20261001.CompetitionFormatAcceptance.test_team_number_is_in_first_english_sentence)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_format_r25_20261001.py", line 100, in test_team_number_is_in_first_english_sentence
    result = self.answer('How many players are in a CS2 team?', 'en')
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_format_r25_20261001.py", line 23, in answer
    result = answer_question_pipeline_debug(question, locale=locale, experimental_allow_llm=False, experimental_rag_fallback=True, global_timeout_sec=10)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4712, in answer_question_pipeline_debug
    return get_pipeline().answer(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1898, in _answer_single
    english_result = answer_english_supported(
                     ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_2026101 … [ย่อจาก2,955ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 36. legacy / errors / test_technical_communication_first_sentence_and_no_other_pause_type (tests.test_competition_format_r25_20261001.CompetitionFormatAcceptance.test_technical_communication_first_sentence_and_no_other_pause_type) (locale='th')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_format_r25_20261001.py", line 34, in test_technical_communication_first_sentence_and_no_other_pause_type
    result = self.answer(question, locale)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_format_r25_20261001.py", line 23, in answer
    result = answer_question_pipeline_debug(question, locale=locale, experimental_allow_llm=False, experimental_rag_fallback=True, global_timeout_sec=10)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4712, in answer_question_pipeline_debug
    return get_pipeline().answer(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 3565, in _answer_single
    source_hits, source_trace = retrieve_curated(
                                ^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\retri … [ย่อจาก2,313ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 37. legacy / errors / test_technical_communication_first_sentence_and_no_other_pause_type (tests.test_competition_format_r25_20261001.CompetitionFormatAcceptance.test_technical_communication_first_sentence_and_no_other_pause_type) (locale='en')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_format_r25_20261001.py", line 34, in test_technical_communication_first_sentence_and_no_other_pause_type
    result = self.answer(question, locale)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_format_r25_20261001.py", line 23, in answer
    result = answer_question_pipeline_debug(question, locale=locale, experimental_allow_llm=False, experimental_rag_fallback=True, global_timeout_sec=10)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4712, in answer_question_pipeline_debug
    return get_pipeline().answer(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1898, in _answer_single
    english_result = answer_english_supported(
                     ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\bilingual_e … [ย่อจาก2,922ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 38. legacy / errors / test_unknown_technical_duration_does_not_borrow_tactical_or_emergency (tests.test_competition_format_r25_20261001.CompetitionFormatAcceptance.test_unknown_technical_duration_does_not_borrow_tactical_or_emergency) (locale='th')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_format_r25_20261001.py", line 49, in test_unknown_technical_duration_does_not_borrow_tactical_or_emergency
    answer = self.answer(question, locale).answer
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_format_r25_20261001.py", line 23, in answer
    result = answer_question_pipeline_debug(question, locale=locale, experimental_allow_llm=False, experimental_rag_fallback=True, global_timeout_sec=10)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4712, in answer_question_pipeline_debug
    return get_pipeline().answer(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 3565, in _answer_single
    source_hits, source_trace = retrieve_curated(
                                ^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipel … [ย่อจาก2,322ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 39. legacy / errors / test_unknown_technical_duration_does_not_borrow_tactical_or_emergency (tests.test_competition_format_r25_20261001.CompetitionFormatAcceptance.test_unknown_technical_duration_does_not_borrow_tactical_or_emergency) (locale='en')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_format_r25_20261001.py", line 49, in test_unknown_technical_duration_does_not_borrow_tactical_or_emergency
    answer = self.answer(question, locale).answer
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_format_r25_20261001.py", line 23, in answer
    result = answer_question_pipeline_debug(question, locale=locale, experimental_allow_llm=False, experimental_rag_fallback=True, global_timeout_sec=10)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4712, in answer_question_pipeline_debug
    return get_pipeline().answer(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1898, in _answer_single
    english_result = answer_english_supported(
                     ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\bi … [ย่อจาก2,931ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 40. legacy / errors / test_valorant_penalty_types_keep_all_five_source_conditions_once (tests.test_competition_format_r25_20261001.CompetitionFormatAcceptance.test_valorant_penalty_types_keep_all_five_source_conditions_once)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_format_r25_20261001.py", line 106, in test_valorant_penalty_types_keep_all_five_source_conditions_once
    result = self.answer('What do the VALORANT tournament rules say about penalties?', 'en')
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_format_r25_20261001.py", line 23, in answer
    result = answer_question_pipeline_debug(question, locale=locale, experimental_allow_llm=False, experimental_rag_fallback=True, global_timeout_sec=10)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4712, in answer_question_pipeline_debug
    return get_pipeline().answer(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1898, in _answer_single
    english_result = answer_english_supported(
                     ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\ … [ย่อจาก3,020ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 41. legacy / errors / test_checkin_question_does_not_use_an_unrelated_note_rule (tests.test_competition_target_grounding.CompetitionTargetGroundingTests.test_checkin_question_does_not_use_an_unrelated_note_rule)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_target_grounding.py", line 177, in test_checkin_question_does_not_use_an_unrelated_note_rule
    result = answer_question_pipeline_debug(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4712, in answer_question_pipeline_debug
    return get_pipeline().answer(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 3565, in _answer_single
    source_hits, source_trace = retrieve_curated(
                                ^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\retrieval.py", line 900, in retrieve_curated
    return hits, PipelineTrace("rag_retrieval", "curated_lexical", confidence, detail, {"category": category, "game": competition_game, "intent": competition_intent,"common_ownership_blocked":ownership_blocked})
                                                                                                                                                                                                ^^^^^^^^^^^^^^^^^
NameError: name 'ownership_blocked' is not defi … [ย่อจาก1,804ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 42. legacy / errors / test_checkin_renderer_does_not_append_adjacent_match_prep_rules (tests.test_competition_target_grounding.CompetitionTargetGroundingTests.test_checkin_renderer_does_not_append_adjacent_match_prep_rules)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_target_grounding.py", line 189, in test_checkin_renderer_does_not_append_adjacent_match_prep_rules
    result = answer_question_pipeline_debug(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4712, in answer_question_pipeline_debug
    return get_pipeline().answer(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 3565, in _answer_single
    source_hits, source_trace = retrieve_curated(
                                ^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\retrieval.py", line 900, in retrieve_curated
    return hits, PipelineTrace("rag_retrieval", "curated_lexical", confidence, detail, {"category": category, "game": competition_game, "intent": competition_intent,"common_ownership_blocked":ownership_blocked})
                                                                                                                                                                                                ^^^^^^^^^^^^^^^^^
NameError: name 'ownership_blocked' is no … [ย่อจาก1,810ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 43. legacy / errors / test_conduct_query_ranks_conduct_sections_first (tests.test_competition_target_grounding.CompetitionTargetGroundingTests.test_conduct_query_ranks_conduct_sections_first)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_target_grounding.py", line 65, in test_conduct_query_ranks_conduct_sections_first
    hits, _ = retrieve_curated(
              ^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\retrieval.py", line 900, in retrieve_curated
    return hits, PipelineTrace("rag_retrieval", "curated_lexical", confidence, detail, {"category": category, "game": competition_game, "intent": competition_intent,"common_ownership_blocked":ownership_blocked})
                                                                                                                                                                                                ^^^^^^^^^^^^^^^^^
NameError: name 'ownership_blocked' is not defined

```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 44. legacy / errors / test_english_missing_valorant_conduct_does_not_become_translation_pending (tests.test_competition_target_grounding.CompetitionTargetGroundingTests.test_english_missing_valorant_conduct_does_not_become_translation_pending)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_target_grounding.py", line 238, in test_english_missing_valorant_conduct_does_not_become_translation_pending
    result = answer_question_pipeline_debug(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4712, in answer_question_pipeline_debug
    return get_pipeline().answer(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1898, in _answer_single
    english_result = answer_english_supported(
                     ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\bilingual_english.py", line 2762, in answer_english_supported
    competition = _answer_competition(query, route=route)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\bilingual_english.py", line 2121, in _answer_competition
    source_rows, _source_trace = retrieve_curated(
                                 ^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Doc … [ย่อจาก2,429ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 45. legacy / errors / test_english_starting_player_question_does_not_use_match_prep_capacity (tests.test_competition_target_grounding.CompetitionTargetGroundingTests.test_english_starting_player_question_does_not_use_match_prep_capacity)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_target_grounding.py", line 250, in test_english_starting_player_question_does_not_use_match_prep_capacity
    result = answer_question_pipeline_debug(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4712, in answer_question_pipeline_debug
    return get_pipeline().answer(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1898, in _answer_single
    english_result = answer_english_supported(
                     ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\bilingual_english.py", line 2762, in answer_english_supported
    competition = _answer_competition(query, route=route)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\bilingual_english.py", line 2121, in _answer_competition
    source_rows, _source_trace = retrieve_curated(
                                 ^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Docume … [ย่อจาก2,426ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 46. legacy / errors / test_generic_in_match_process_does_not_use_a_graph_setting (tests.test_competition_target_grounding.CompetitionTargetGroundingTests.test_generic_in_match_process_does_not_use_a_graph_setting)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_target_grounding.py", line 203, in test_generic_in_match_process_does_not_use_a_graph_setting
    result = answer_question_pipeline_debug(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4712, in answer_question_pipeline_debug
    return get_pipeline().answer(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 3565, in _answer_single
    source_hits, source_trace = retrieve_curated(
                                ^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\retrieval.py", line 900, in retrieve_curated
    return hits, PipelineTrace("rag_retrieval", "curated_lexical", confidence, detail, {"category": category, "game": competition_game, "intent": competition_intent,"common_ownership_blocked":ownership_blocked})
                                                                                                                                                                                                ^^^^^^^^^^^^^^^^^
NameError: name 'ownership_blocked' is not def … [ย่อจาก1,805ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 47. legacy / errors / test_generic_settings_query_renders_settings_not_timeout (tests.test_competition_target_grounding.CompetitionTargetGroundingTests.test_generic_settings_query_renders_settings_not_timeout)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_target_grounding.py", line 113, in test_generic_settings_query_renders_settings_not_timeout
    result = answer_question_pipeline_debug(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4712, in answer_question_pipeline_debug
    return get_pipeline().answer(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 3565, in _answer_single
    source_hits, source_trace = retrieve_curated(
                                ^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\retrieval.py", line 900, in retrieve_curated
    return hits, PipelineTrace("rag_retrieval", "curated_lexical", confidence, detail, {"category": category, "game": competition_game, "intent": competition_intent,"common_ownership_blocked":ownership_blocked})
                                                                                                                                                                                                ^^^^^^^^^^^^^^^^^
NameError: name 'ownership_blocked' is not defin … [ย่อจาก1,803ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 48. legacy / errors / test_known_source_gap_has_a_machine_readable_reason (tests.test_competition_target_grounding.CompetitionTargetGroundingTests.test_known_source_gap_has_a_machine_readable_reason)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_target_grounding.py", line 140, in test_known_source_gap_has_a_machine_readable_reason
    hits, _ = retrieve_curated(
              ^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\retrieval.py", line 900, in retrieve_curated
    return hits, PipelineTrace("rag_retrieval", "curated_lexical", confidence, detail, {"category": category, "game": competition_game, "intent": competition_intent,"common_ownership_blocked":ownership_blocked})
                                                                                                                                                                                                ^^^^^^^^^^^^^^^^^
NameError: name 'ownership_blocked' is not defined

```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 49. legacy / errors / test_missing_target_facet_does_not_substitute_another_rule (tests.test_competition_target_grounding.CompetitionTargetGroundingTests.test_missing_target_facet_does_not_substitute_another_rule)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_target_grounding.py", line 127, in test_missing_target_facet_does_not_substitute_another_rule
    result = answer_question_pipeline_debug(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4712, in answer_question_pipeline_debug
    return get_pipeline().answer(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 3565, in _answer_single
    source_hits, source_trace = retrieve_curated(
                                ^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\retrieval.py", line 900, in retrieve_curated
    return hits, PipelineTrace("rag_retrieval", "curated_lexical", confidence, detail, {"category": category, "game": competition_game, "intent": competition_intent,"common_ownership_blocked":ownership_blocked})
                                                                                                                                                                                                ^^^^^^^^^^^^^^^^^
NameError: name 'ownership_blocked' is not def … [ย่อจาก1,805ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 50. legacy / errors / test_roster_question_requires_starter_and_substitute_evidence (tests.test_competition_target_grounding.CompetitionTargetGroundingTests.test_roster_question_requires_starter_and_substitute_evidence)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_target_grounding.py", line 165, in test_roster_question_requires_starter_and_substitute_evidence
    result = answer_question_pipeline_debug(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4712, in answer_question_pipeline_debug
    return get_pipeline().answer(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 3565, in _answer_single
    source_hits, source_trace = retrieve_curated(
                                ^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\retrieval.py", line 900, in retrieve_curated
    return hits, PipelineTrace("rag_retrieval", "curated_lexical", confidence, detail, {"category": category, "game": competition_game, "intent": competition_intent,"common_ownership_blocked":ownership_blocked})
                                                                                                                                                                                                ^^^^^^^^^^^^^^^^^
NameError: name 'ownership_blocked' is not  … [ย่อจาก1,808ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 51. legacy / errors / test_team_composition_ranks_the_team_size_section_first (tests.test_competition_target_grounding.CompetitionTargetGroundingTests.test_team_composition_ranks_the_team_size_section_first)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_target_grounding.py", line 76, in test_team_composition_ranks_the_team_size_section_first
    hits, _ = retrieve_curated(
              ^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\retrieval.py", line 900, in retrieve_curated
    return hits, PipelineTrace("rag_retrieval", "curated_lexical", confidence, detail, {"category": category, "game": competition_game, "intent": competition_intent,"common_ownership_blocked":ownership_blocked})
                                                                                                                                                                                                ^^^^^^^^^^^^^^^^^
NameError: name 'ownership_blocked' is not defined

```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 52. legacy / errors / test_competition_schedule_cannot_use_booking_schedule (tests.test_competition_user_questions_r24_20261001.CompetitionUserQuestions.test_competition_schedule_cannot_use_booking_schedule)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_user_questions_r24_20261001.py", line 84, in test_competition_schedule_cannot_use_booking_schedule
    result = answer_question_pipeline_debug('ตาม rulebook เคาน์เตอร์สไตรก์ 2 ตารางบทลงโทษ ต้องทำยังไง', locale='th', experimental_allow_llm=False, experimental_rag_fallback=True, global_timeout_sec=10)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4712, in answer_question_pipeline_debug
    return get_pipeline().answer(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 3565, in _answer_single
    source_hits, source_trace = retrieve_curated(
                                ^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\retrieval.py", line 900, in retrieve_curated
    return hits, PipelineTrace("rag_retrieval", "curated_lexical", confidence, detail, {"category": category, "game": competition_game, "intent": com … [ย่อจาก2,124ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 53. legacy / errors / test_known_numeric_and_negative_clauses (tests.test_competition_user_questions_r24_20261001.CompetitionUserQuestions.test_known_numeric_and_negative_clauses) (query='CS2 แข่งทีมละกี่คน')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_user_questions_r24_20261001.py", line 99, in test_known_numeric_and_negative_clauses
    result = answer_question_pipeline_debug(query, locale='th', experimental_allow_llm=False, experimental_rag_fallback=True, global_timeout_sec=10)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4712, in answer_question_pipeline_debug
    return get_pipeline().answer(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 3565, in _answer_single
    source_hits, source_trace = retrieve_curated(
                                ^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\retrieval.py", line 900, in retrieve_curated
    return hits, PipelineTrace("rag_retrieval", "curated_lexical", confidence, detail, {"category": category, "game": competition_game, "intent": competition_intent,"common_ownership_blocked":ownership_blocked})
                                                          … [ย่อจาก2,004ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 54. legacy / errors / test_known_numeric_and_negative_clauses (tests.test_competition_user_questions_r24_20261001.CompetitionUserQuestions.test_known_numeric_and_negative_clauses) (query='Tekken 8 รูปแบบการแข่งขันเป็นอย่างไร')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_user_questions_r24_20261001.py", line 99, in test_known_numeric_and_negative_clauses
    result = answer_question_pipeline_debug(query, locale='th', experimental_allow_llm=False, experimental_rag_fallback=True, global_timeout_sec=10)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4712, in answer_question_pipeline_debug
    return get_pipeline().answer(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 3565, in _answer_single
    source_hits, source_trace = retrieve_curated(
                                ^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\retrieval.py", line 900, in retrieve_curated
    return hits, PipelineTrace("rag_retrieval", "curated_lexical", confidence, detail, {"category": category, "game": competition_game, "intent": competition_intent,"common_ownership_blocked":ownership_blocked})
                                                          … [ย่อจาก2,004ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 55. legacy / errors / test_known_numeric_and_negative_clauses (tests.test_competition_user_questions_r24_20261001.CompetitionUserQuestions.test_known_numeric_and_negative_clauses) (query='RoV ใช้ Tablet หรือ iPad แข่งได้ไหม')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_user_questions_r24_20261001.py", line 99, in test_known_numeric_and_negative_clauses
    result = answer_question_pipeline_debug(query, locale='th', experimental_allow_llm=False, experimental_rag_fallback=True, global_timeout_sec=10)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4712, in answer_question_pipeline_debug
    return get_pipeline().answer(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 3565, in _answer_single
    source_hits, source_trace = retrieve_curated(
                                ^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\retrieval.py", line 900, in retrieve_curated
    return hits, PipelineTrace("rag_retrieval", "curated_lexical", confidence, detail, {"category": category, "game": competition_game, "intent": competition_intent,"common_ownership_blocked":ownership_blocked})
                                                          … [ย่อจาก2,004ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 56. legacy / errors / test_known_numeric_and_negative_clauses (tests.test_competition_user_questions_r24_20261001.CompetitionUserQuestions.test_known_numeric_and_negative_clauses) (query='VALORANT technical pause สื่อสารได้ไหม')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_user_questions_r24_20261001.py", line 99, in test_known_numeric_and_negative_clauses
    result = answer_question_pipeline_debug(query, locale='th', experimental_allow_llm=False, experimental_rag_fallback=True, global_timeout_sec=10)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4712, in answer_question_pipeline_debug
    return get_pipeline().answer(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 3565, in _answer_single
    source_hits, source_trace = retrieve_curated(
                                ^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\retrieval.py", line 900, in retrieve_curated
    return hits, PipelineTrace("rag_retrieval", "curated_lexical", confidence, detail, {"category": category, "game": competition_game, "intent": competition_intent,"common_ownership_blocked":ownership_blocked})
                                                          … [ย่อจาก2,004ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 57. legacy / errors / test_semantic_cases (tests.test_integrated_improvement_r21_20261001.IntegratedImprovementTests.test_semantic_cases) (case='unknown-person')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_integrated_improvement_r21_20261001.py", line 58, in test_semantic_cases
    row=run_focused_case(case)
        ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_reliability_flow_20261001.py", line 59, in run_focused_case
    result = answer_question_pipeline_debug(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4712, in answer_question_pipeline_debug
    return get_pipeline().answer(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4084, in _answer_single
    rag_hits, rag_trace = retrieve_curated(pre.clean_query, route.category)
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\retrieval.py", line 900, in retrieve_curated
    return hits, PipelineTrace("rag_retrieval", "curated_lexical", confidence, detail, {"category": category, "game": competition_game, "intent": competition_intent,"common_ownership_blocked … [ย่อจาก2,083ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 58. legacy / errors / test_semantic_cases (tests.test_integrated_improvement_r21_20261001.IntegratedImprovementTests.test_semantic_cases) (case='team-size-two-typos')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_integrated_improvement_r21_20261001.py", line 58, in test_semantic_cases
    row=run_focused_case(case)
        ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_reliability_flow_20261001.py", line 59, in run_focused_case
    result = answer_question_pipeline_debug(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4712, in answer_question_pipeline_debug
    return get_pipeline().answer(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1898, in _answer_single
    english_result = answer_english_supported(
                     ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\bilingual_english.py", line 2762, in answer_english_supported
    competition = _answer_competition(query, route=route)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261 … [ย่อจาก2,640ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 59. legacy / errors / test_semantic_cases (tests.test_integrated_improvement_r21_20261001.IntegratedImprovementTests.test_semantic_cases) (case='tactical-pause')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_integrated_improvement_r21_20261001.py", line 58, in test_semantic_cases
    row=run_focused_case(case)
        ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_reliability_flow_20261001.py", line 59, in run_focused_case
    result = answer_question_pipeline_debug(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4712, in answer_question_pipeline_debug
    return get_pipeline().answer(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1898, in _answer_single
    english_result = answer_english_supported(
                     ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\bilingual_english.py", line 2762, in answer_english_supported
    competition = _answer_competition(query, route=route)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261 … [ย่อจาก2,640ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 60. legacy / errors / test_semantic_cases (tests.test_integrated_improvement_r21_20261001.IntegratedImprovementTests.test_semantic_cases) (case='emergency-pause')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_integrated_improvement_r21_20261001.py", line 58, in test_semantic_cases
    row=run_focused_case(case)
        ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_reliability_flow_20261001.py", line 59, in run_focused_case
    result = answer_question_pipeline_debug(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4712, in answer_question_pipeline_debug
    return get_pipeline().answer(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1898, in _answer_single
    english_result = answer_english_supported(
                     ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\bilingual_english.py", line 2762, in answer_english_supported
    competition = _answer_competition(query, route=route)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261 … [ย่อจาก2,640ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 61. legacy / errors / test_review_data_cannot_end_embedded_script (tests.test_intent_trap_review_html.ReviewHtmlTests.test_review_data_cannot_end_embedded_script)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_review_html.py", line 54, in test_review_data_cannot_end_embedded_script
    build_html(source, output)
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tools\build_intent_trap_review_html.py", line 34, in build_html
    template = TEMPLATE.read_text(encoding="utf-8")
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r58_common_content_20261010\system\PSU_Esports_Chatbot_Local\runtime\python\Lib\pathlib.py", line 1027, in read_text
    with self.open(mode='r', encoding=encoding, errors=errors) as f:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r58_common_content_20261010\system\PSU_Esports_Chatbot_Local\runtime\python\Lib\pathlib.py", line 1013, in open
    return io.open(self, mode, buffering, encoding, errors, newline)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\Chokhun\\Documents\\Codex\\2026-09-25\\psu-esports-studio-phuket-chatbot-c-2\\r64_full_comparison_20261013\\system\\review_ui\\intent_trap_400_template.html'

```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 62. legacy / errors / test_review_html_contains_all_400_answers (tests.test_intent_trap_review_html.ReviewHtmlTests.test_review_html_contains_all_400_answers)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_review_html.py", line 23, in test_review_html_contains_all_400_answers
    build_html(DEFAULT_SOURCE, output)
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tools\build_intent_trap_review_html.py", line 16, in build_html
    raw = source.read_bytes()
          ^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r58_common_content_20261010\system\PSU_Esports_Chatbot_Local\runtime\python\Lib\pathlib.py", line 1019, in read_bytes
    with self.open(mode='rb') as f:
         ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r58_common_content_20261010\system\PSU_Esports_Chatbot_Local\runtime\python\Lib\pathlib.py", line 1013, in open
    return io.open(self, mode, buffering, encoding, errors, newline)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\Chokhun\\Documents\\Codex\\2026-09-25\\psu-esports-studio-phuket-chatbot-c-2\\r64_full_comparison_20261013\\system\\reports\\master_ground_truth_eval\\master_gt_eval_20260924_195543_intent_trap_manual_review_v2.jsonl'

```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 63. legacy / errors / test_unverified_thai_studio_claim_is_a_no_answer_outcome (tests.test_master_ground_truth_route_regressions.MasterGroundTruthRouteRegressionTests.test_unverified_thai_studio_claim_is_a_no_answer_outcome)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_master_ground_truth_route_regressions.py", line 224, in test_unverified_thai_studio_claim_is_a_no_answer_outcome
    result = answer_question_pipeline_debug(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4712, in answer_question_pipeline_debug
    return get_pipeline().answer(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4020, in _answer_single
    fallback = build_experimental_fallback(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\experimental_fallback.py", line 1087, in build_experimental_fallback
    rows, details = _retrieve_experimental_rows(
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\experimental_fallback.py", line 259, in _retrieve_experimental_rows
    hybrid_rows, hybrid_trace = retrieve_hybrid_guarded(
                                ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Docum … [ย่อจาก2,819ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 64. legacy / errors / test_phrase_recovery_keeps_resource_and_duration (tests.test_multi_error_typo_recovery_20260929.MultiErrorTypoRecoveryTests.test_phrase_recovery_keeps_resource_and_duration) (question='ติดต่าทาไงหน')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_multi_error_typo_recovery_20260929.py", line 58, in test_phrase_recovery_keeps_resource_and_duration
    self.assertEqual(_answer(question).route.intent, intent)
                     ^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_multi_error_typo_recovery_20260929.py", line 14, in _answer
    return answer_question_pipeline_debug(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4712, in answer_question_pipeline_debug
    return get_pipeline().answer(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4084, in _answer_single
    rag_hits, rag_trace = retrieve_curated(pre.clean_query, route.category)
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\retrieval.py", line 900, in retrieve_curated
    return hits, PipelineTrace("rag_retrieval", "curated_lexical", confidence, detail, {"category": category, "game": competitio … [ย่อจาก2,145ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 65. legacy / errors / test_booking_email_does_not_turn_into_studio_contact (tests.test_p1_verified_answer_paths_20260928.VerifiedAnswerPathTests.test_booking_email_does_not_turn_into_studio_contact)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_p1_verified_answer_paths_20260928.py", line 26, in test_booking_email_does_not_turn_into_studio_contact
    result = self.answer("จองแล้วต้องตรวจสอบอีเมลไหม")
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_p1_verified_answer_paths_20260928.py", line 13, in answer
    return answer_question_pipeline_debug(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4712, in answer_question_pipeline_debug
    return get_pipeline().answer(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4084, in _answer_single
    rag_hits, rag_trace = retrieve_curated(pre.clean_query, route.category)
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\retrieval.py", line 900, in retrieve_curated
    return hits, PipelineTrace("rag_retrieval", "curated_lexical", confidence, detail, {"category": category, "game": … [ย่อจาก2,156ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 66. legacy / errors / test_contact_email_with_thai_spelling (tests.test_p1_verified_answer_paths_20260928.VerifiedAnswerPathTests.test_contact_email_with_thai_spelling)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_p1_verified_answer_paths_20260928.py", line 21, in test_contact_email_with_thai_spelling
    result = self.answer("ขออีเมลติดต่อศูนย์")
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_p1_verified_answer_paths_20260928.py", line 13, in answer
    return answer_question_pipeline_debug(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4712, in answer_question_pipeline_debug
    return get_pipeline().answer(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4084, in _answer_single
    rag_hits, rag_trace = retrieve_curated(pre.clean_query, route.category)
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\retrieval.py", line 900, in retrieve_curated
    return hits, PipelineTrace("rag_retrieval", "curated_lexical", confidence, detail, {"category": category, "game": competition_game, "intent": co … [ย่อจาก2,125ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 67. legacy / errors / test_projects_pairs_without_claiming_human_review (tests.test_project_intent_trap_review_bilingual.BilingualReviewProjectionTests.test_projects_pairs_without_claiming_human_review)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_project_intent_trap_review_bilingual.py", line 30, in test_projects_pairs_without_claiming_human_review
    result = project(self._review_file(Path(directory)))
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_project_intent_trap_review_bilingual.py", line 14, in _review_file
    rows = [json.loads(line) for line in CORPUS.read_text(encoding="utf-8").splitlines() if line.strip()]
                                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r58_common_content_20261010\system\PSU_Esports_Chatbot_Local\runtime\python\Lib\pathlib.py", line 1027, in read_text
    with self.open(mode='r', encoding=encoding, errors=errors) as f:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r58_common_content_20261010\system\PSU_Esports_Chatbot_Local\runtime\python\Lib\pathlib.py", line 1013, in open
    return io.open(self, mode, buffering, encoding, errors, newline)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\Chokhun\\Documents\\Codex\\2026-09-25\\psu-esports-studio-phuket-chatbot-c-2\\r64_full_comparison_20261013\\system\\reports\\master_ground_truth_eval\\master_gt_eval_20260924_195543_intent_trap_manual_review_v2.jsonl'

```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 68. legacy / errors / test_rejects_review_from_another_corpus (tests.test_project_intent_trap_review_bilingual.BilingualReviewProjectionTests.test_rejects_review_from_another_corpus)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_project_intent_trap_review_bilingual.py", line 47, in test_rejects_review_from_another_corpus
    review_path = self._review_file(Path(directory))
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_project_intent_trap_review_bilingual.py", line 14, in _review_file
    rows = [json.loads(line) for line in CORPUS.read_text(encoding="utf-8").splitlines() if line.strip()]
                                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r58_common_content_20261010\system\PSU_Esports_Chatbot_Local\runtime\python\Lib\pathlib.py", line 1027, in read_text
    with self.open(mode='r', encoding=encoding, errors=errors) as f:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r58_common_content_20261010\system\PSU_Esports_Chatbot_Local\runtime\python\Lib\pathlib.py", line 1013, in open
    return io.open(self, mode, buffering, encoding, errors, newline)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\Chokhun\\Documents\\Codex\\2026-09-25\\psu-esports-studio-phuket-chatbot-c-2\\r64_full_comparison_20261013\\system\\reports\\master_ground_truth_eval\\master_gt_eval_20260924_195543_intent_trap_manual_review_v2.jsonl'

```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 69. legacy / errors / test_catalog_all_and_ordinal_ask_for_axis_but_all_zones_is_explicit (tests.test_task_memory_r41.TaskMemoryR41Tests.test_catalog_all_and_ordinal_ask_for_axis_but_all_zones_is_explicit)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_task_memory_r41.py", line 161, in test_catalog_all_and_ordinal_ask_for_axis_but_all_zones_is_explicit
    p=s.begin('s',q,q,locale='en');self.assertIn(p['plan']['message_key'],('scope','ordinal_axis'))
                                                 ~~~~~~~~~^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not subscriptable

```

[legacy_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/legacy_test_all.py_temp_fixed.json)

## 70. common / failures / test_vacancy_typo_frames_use_live_handler_even_offline (tests.test_all_remaining_r32_20261002.AllRemainingR32Tests.test_vacancy_typo_frames_use_live_handler_even_offline) (q='พรุ่งนี้ 13:00 Nintendo Switch วางหรือเปล่า')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_all_remaining_r32_20261002.py", line 17, in test_vacancy_typo_frames_use_live_handler_even_offline
    self.assertTrue(r.mode.startswith('pipeline:live_booking_status_unavailable'))
AssertionError: False is not true

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 71. common / failures / test_planner_accepts_only_relevant_schema_fields (tests.test_common_content_r58.CommonTests.test_planner_accepts_only_relevant_schema_fields)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_common_content_r58.py", line 175, in test_planner_accepts_only_relevant_schema_fields
    for p in ({'requested_fields':['amount_minor'],'all_fields':False,'platform':None},{'requested_fields':['bindings'],'all_fields':False,'platform':'PS4'},{'requested_fields':['bindings'],'all_fields':'true','platform':None}):self.assertIsNone(checked_plan(p,ids,records))
                                                                                                                                                                                                                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: {'requested_fields': ['amount_minor'], 'all_fields': False, 'platform': None, 'method': 'bounded_llm_schema_fields'} is not None

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 72. common / failures / test_dispute_resolution_is_not_display_resolution (tests.test_competition_composition_r28_20261001.CompositionR28Tests.test_dispute_resolution_is_not_display_resolution)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_composition_r28_20261001.py", line 105, in test_dispute_resolution_is_not_display_resolution
    self.assertNotIn('brightness',result.answer.casefold())
AssertionError: 'brightness' unexpectedly found in '**[thai source] ภาพรวมเอกสาร**\n• text: [thai source] กฎระเบียบและรูปแบบการแข่งขัน counter-strike 2 [s1]\n• heading: [thai source] ภาพรวมเอกสาร [s2]\n• section number: 1 [s3]\n• completeness: not yet confirmed\n\n**[thai source] 6. ข้อจำกัด**\n• text: [thai source] 6. ข้อจำกัด [s4]\n• heading: [thai source] 6. ข้อจำกัด [s5]\n• section number: 10 [s6]\n• completeness: not yet confirmed\n\n**[thai source] 1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน**\n• text: [thai source] 1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน [s7]\n• heading: [thai source] 1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน [s8]\n• section number: 11 [s9]\n• completeness: not yet confirmed\n\n**[thai source] 2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร**\n• text: [thai source] 2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร [s10]\n• heading: [thai source] 2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร [s11]\n• section number: 12 [s12]\n• completeness: not yet confirmed\n\n**[thai source] 3. หากสมาชิกคนใดถอนตัว ทีมอาจถูกตัดสิทธิ์**\n• text: [thai source] 3. หากสมาชิกคนใดถอนตัว ทีมอาจถูกตัดสิทธิ์ [s13]\n• heading: [thai source] 3. หากสมาชิกคนใดถอนตัว ทีมอาจถูกตัดสิทธิ์ [s14]\n• section number: 13 [s15]\n• completeness: not yet confirmed\n\n**[thai source] 4. ผู้เล่นสามารถลงแข่งในนามของทีมได้ทีมเดียวเท่านั้น**\n• text: [thai source] 4. ผู้เล่นสามารถลงแข่งในนามของทีมได … [ย่อจาก20,294ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 73. common / failures / test_fee_is_not_late_registration (tests.test_competition_composition_r28_20261001.CompositionR28Tests.test_fee_is_not_late_registration)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_composition_r28_20261001.py", line 32, in test_fee_is_not_late_registration
    self.assertIn('no_answer',result.mode)
AssertionError: 'no_answer' not found in 'pipeline:common_answer'

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 74. common / failures / test_final_decision_is_not_the_final_match (tests.test_competition_composition_r28_20261001.CompositionR28Tests.test_final_decision_is_not_the_final_match)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_composition_r28_20261001.py", line 91, in test_final_decision_is_not_the_final_match
    self.assertIn('Judgment authority',result.answer.splitlines()[0])
AssertionError: 'Judgment authority' not found in '**[Thai source] ภาพรวมเอกสาร**'

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 75. common / failures / test_only_overtime_cannot_borrow_regulation_money (tests.test_competition_composition_r28_20261001.CompositionR28Tests.test_only_overtime_cannot_borrow_regulation_money)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_composition_r28_20261001.py", line 23, in test_only_overtime_cannot_borrow_regulation_money
    self.assertIn('$10,000',result.answer);self.assertNotIn('$800',result.answer)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: '$10,000' not found in 'The requested topic is unclear. Which part of [Thai source] PSU Phuket CS2 2026 Tournament do you need: event name / rulebook release / coverage?'

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 76. common / failures / test_pause_conflict_is_visible_before_permission (tests.test_competition_composition_r28_20261001.CompositionR28Tests.test_pause_conflict_is_visible_before_permission)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_composition_r28_20261001.py", line 63, in test_pause_conflict_is_visible_before_permission
    self.assertIn('conflict',result.mode)
AssertionError: 'conflict' not found in 'pipeline:common_answer'

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 77. common / failures / test_protest_language_and_procedure_preserve_both (tests.test_competition_composition_r28_20261001.CompositionR28Tests.test_protest_language_and_procedure_preserve_both)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_composition_r28_20261001.py", line 27, in test_protest_language_and_procedure_preserve_both
    for term in ('Thai','15 minutes','captain','coach'):self.assertIn(term,result.answer)
                                                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: '15 minutes' not found in '**[Thai source] ภาพรวมเอกสาร**\n• text: [Thai source] กฎระเบียบและรูปแบบการแข่งขัน Counter-Strike 2 [S1]\n• heading: [Thai source] ภาพรวมเอกสาร [S2]\n• section number: 1 [S3]\n• completeness: Not yet confirmed\n\n**[Thai source] 6. ข้อจำกัด**\n• text: [Thai source] 6. ข้อจำกัด [S4]\n• heading: [Thai source] 6. ข้อจำกัด [S5]\n• section number: 10 [S6]\n• completeness: Not yet confirmed\n\n**[Thai source] 1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน**\n• text: [Thai source] 1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน [S7]\n• heading: [Thai source] 1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน [S8]\n• section number: 11 [S9]\n• completeness: Not yet confirmed\n\n**[Thai source] 2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร**\n• text: [Thai source] 2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร [S10]\n• heading: [Thai source] 2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร [S11]\n• section number: 12 [S12]\n• completeness: Not yet confirmed\n\n**[Thai source] 3. หากสมาชิกคนใดถอนตัว ทีมอาจถูกตัดสิทธิ์**\n• text: [Thai source] 3. หากสมาชิกคนใดถอนตัว ทีมอาจถูกตัดสิทธิ์ [S13]\n• heading: [Thai source] 3. หากสมาชิกคนใดถอนตัว ทีมอาจถูกตัดสิทธิ์ [S14]\n• section number: 13 [S15]\n• completeness: Not yet confirmed\n\n**[Thai source] 4.  … [ย่อจาก20,494ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 78. common / failures / test_supported_clause_is_kept_with_unknown_fee (tests.test_competition_composition_r28_20261001.CompositionR28Tests.test_supported_clause_is_kept_with_unknown_fee)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_composition_r28_20261001.py", line 38, in test_supported_clause_is_kept_with_unknown_fee
    self.assertIn('No scripts or macros',result.answer)
AssertionError: 'No scripts or macros' not found in '**[Thai source] ภาพรวมเอกสาร**\n• text: [Thai source] กฎระเบียบและรูปแบบการแข่งขัน Counter-Strike 2 [S1]\n• heading: [Thai source] ภาพรวมเอกสาร [S2]\n• section number: 1 [S3]\n• completeness: Not yet confirmed\n\n**[Thai source] 6. ข้อจำกัด**\n• text: [Thai source] 6. ข้อจำกัด [S4]\n• heading: [Thai source] 6. ข้อจำกัด [S5]\n• section number: 10 [S6]\n• completeness: Not yet confirmed\n\n**[Thai source] 1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน**\n• text: [Thai source] 1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน [S7]\n• heading: [Thai source] 1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน [S8]\n• section number: 11 [S9]\n• completeness: Not yet confirmed\n\n**[Thai source] 2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร**\n• text: [Thai source] 2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร [S10]\n• heading: [Thai source] 2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร [S11]\n• section number: 12 [S12]\n• completeness: Not yet confirmed\n\n**[Thai source] 3. หากสมาชิกคนใดถอนตัว ทีมอาจถูกตัดสิทธิ์**\n• text: [Thai source] 3. หากสมาชิกคนใดถอนตัว ทีมอาจถูกตัดสิทธิ์ [S13]\n• heading: [Thai source] 3. หากสมาชิกคนใดถอนตัว ทีมอาจถูกตัดสิทธิ์ [S14]\n• section number: 13 [S15]\n• completeness: Not yet confirmed\n\n**[Thai source] 4. ผู้เล่นสามารถลงแข่งในนามของทีมได้ทีมเดียวเท่านั้น**\n• text: [Thai source] 4. ผู้เล่นสามารถลงแข่งในนามของทีมได้ทีมเดี … [ย่อจาก20,382ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 79. common / failures / test_truncated_numbered_clause_does_not_borrow_other_penalties (tests.test_competition_composition_r28_20261001.CompositionR28Tests.test_truncated_numbered_clause_does_not_borrow_other_penalties)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_composition_r28_20261001.py", line 47, in test_truncated_numbered_clause_does_not_borrow_other_penalties
    self.assertIn('6.1.5.1',result.answer)
AssertionError: '6.1.5.1' not found in 'This request reached the processing time limit, so it was stopped to keep the service responsive.\nPlease try a more specific question, such as naming the zone, game, or topic directly.'

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 80. common / failures / test_two_equipment_prohibitions_are_both_answered (tests.test_competition_composition_r28_20261001.CompositionR28Tests.test_two_equipment_prohibitions_are_both_answered)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_composition_r28_20261001.py", line 13, in test_two_equipment_prohibitions_are_both_answered
    self.assertIn('No scripts or macros',result.answer)
AssertionError: 'No scripts or macros' not found in '**[Thai source] ภาพรวมเอกสาร**\n• text: [Thai source] กฎระเบียบและรูปแบบการแข่งขัน Counter-Strike 2 [S1]\n• heading: [Thai source] ภาพรวมเอกสาร [S2]\n• section number: 1 [S3]\n• completeness: Not yet confirmed\n\n**[Thai source] 6. ข้อจำกัด**\n• text: [Thai source] 6. ข้อจำกัด [S4]\n• heading: [Thai source] 6. ข้อจำกัด [S5]\n• section number: 10 [S6]\n• completeness: Not yet confirmed\n\n**[Thai source] 1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน**\n• text: [Thai source] 1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน [S7]\n• heading: [Thai source] 1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน [S8]\n• section number: 11 [S9]\n• completeness: Not yet confirmed\n\n**[Thai source] 2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร**\n• text: [Thai source] 2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร [S10]\n• heading: [Thai source] 2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร [S11]\n• section number: 12 [S12]\n• completeness: Not yet confirmed\n\n**[Thai source] 3. หากสมาชิกคนใดถอนตัว ทีมอาจถูกตัดสิทธิ์**\n• text: [Thai source] 3. หากสมาชิกคนใดถอนตัว ทีมอาจถูกตัดสิทธิ์ [S13]\n• heading: [Thai source] 3. หากสมาชิกคนใดถอนตัว ทีมอาจถูกตัดสิทธิ์ [S14]\n• section number: 13 [S15]\n• completeness: Not yet confirmed\n\n**[Thai source] 4. ผู้เล่นสามารถลงแข่งในนามของทีมได้ทีมเดียวเท่านั้น**\n• text: [Thai source] 4. ผู้เล่นสามารถลงแข่งในนามของทีมได้ทีม … [ย่อจาก20,379ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 81. common / failures / test_all_thai_penalty_types_and_conditions (tests.test_competition_content_speed_r26_20261001.CompetitionContentSpeed.test_all_thai_penalty_types_and_conditions)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_content_speed_r26_20261001.py", line 55, in test_all_thai_penalty_types_and_conditions
    self.assertEqual(result.answer.count(term),1)
AssertionError: 4 != 1

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 82. common / failures / test_missing_pause_proposition_has_no_answer_mode (tests.test_competition_content_speed_r26_20261001.CompetitionContentSpeed.test_missing_pause_proposition_has_no_answer_mode) (locale='th')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_content_speed_r26_20261001.py", line 81, in test_missing_pause_proposition_has_no_answer_mode
    self.assertIn('no_answer',result.mode)
AssertionError: 'no_answer' not found in 'pipeline:common_answer'

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 83. common / failures / test_missing_pause_proposition_has_no_answer_mode (tests.test_competition_content_speed_r26_20261001.CompetitionContentSpeed.test_missing_pause_proposition_has_no_answer_mode) (locale='en')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_content_speed_r26_20261001.py", line 81, in test_missing_pause_proposition_has_no_answer_mode
    self.assertIn('no_answer',result.mode)
AssertionError: 'no_answer' not found in 'pipeline:common_answer'

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 84. common / failures / test_registered_game_and_facet_determine_intent (tests.test_competition_content_speed_r26_20261001.CompetitionContentSpeed.test_registered_game_and_facet_determine_intent) (q='สอบถามหน่อยครับ กติกา RoV เรื่องการหลุดจากเกมหรือการเชื่อมต่อ ว่าอย่างไร ครับ')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_content_speed_r26_20261001.py", line 27, in test_registered_game_and_facet_determine_intent
    self.assertEqual(result.route.category,'competition_rules')
AssertionError: 'knowledge' != 'competition_rules'
- knowledge
+ competition_rules


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 85. common / failures / test_registered_game_and_facet_determine_intent (tests.test_competition_content_speed_r26_20261001.CompetitionContentSpeed.test_registered_game_and_facet_determine_intent) (q='สอบถามหน่อยครับ ขออ้างอิงกติกา เทคเค่น 8 ในหัวข้อการตั้งค่าในเกม หน่อย ครับ')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_content_speed_r26_20261001.py", line 27, in test_registered_game_and_facet_determine_intent
    self.assertEqual(result.route.category,'competition_rules')
AssertionError: 'knowledge' != 'competition_rules'
- knowledge
+ competition_rules


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 86. common / failures / test_routing_does_not_grant_source_coverage (tests.test_competition_content_speed_r26_20261001.CompetitionContentSpeed.test_routing_does_not_grant_source_coverage) (locale='th')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_content_speed_r26_20261001.py", line 49, in test_routing_does_not_grant_source_coverage
    self.assertIn('no_answer',result.mode)
AssertionError: 'no_answer' not found in 'pipeline:common_answer'

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 87. common / failures / test_routing_does_not_grant_source_coverage (tests.test_competition_content_speed_r26_20261001.CompetitionContentSpeed.test_routing_does_not_grant_source_coverage) (locale='en')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_content_speed_r26_20261001.py", line 49, in test_routing_does_not_grant_source_coverage
    self.assertIn('no_answer',result.mode)
AssertionError: 'no_answer' not found in 'pipeline:common_clarification'

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 88. common / failures / test_tournament_format_first_sentence_is_format_not_hardware (tests.test_competition_content_speed_r26_20261001.CompetitionContentSpeed.test_tournament_format_first_sentence_is_format_not_hardware)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_content_speed_r26_20261001.py", line 34, in test_tournament_format_first_sentence_is_format_not_hardware
    self.assertRegex(result.answer.splitlines()[0],r'FT2|1v1')
AssertionError: Regex didn't match: 'FT2|1v1' not found in 'The requested topic is unclear. Which part of [Thai source] PSU Esports ปะทะมันส์ สนั่นจอ do you need: event name / rulebook release / coverage?'

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 89. common / failures / test_tournament_typo_uses_edit_distance_only_with_registered_target (tests.test_competition_content_speed_r26_20261001.CompetitionContentSpeed.test_tournament_typo_uses_edit_distance_only_with_registered_target)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_content_speed_r26_20261001.py", line 91, in test_tournament_typo_uses_edit_distance_only_with_registered_target
    self.assertEqual(result.route.category,'competition_rules')
AssertionError: 'knowledge' != 'competition_rules'
- knowledge
+ competition_rules


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 90. common / failures / test_combined_eligibility_roster_registration_preserves_each_topic (tests.test_competition_contract_r27_20261001.AtomicGraderTests.test_combined_eligibility_roster_registration_preserves_each_topic)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_contract_r27_20261001.py", line 74, in test_combined_eligibility_roster_registration_preserves_each_topic
    self.assertIn(clause,result.answer)
AssertionError: 'Open only to students' not found in '**[Thai source] ภาพรวมเอกสาร**\n• text: [Thai source] กฎระเบียบและรูปแบบการแข่งขัน Counter-Strike 2 [S1]\n• heading: [Thai source] ภาพรวมเอกสาร [S2]\n• section number: 1 [S3]\n• completeness: Not yet confirmed\n\n**[Thai source] 6. ข้อจำกัด**\n• text: [Thai source] 6. ข้อจำกัด [S4]\n• heading: [Thai source] 6. ข้อจำกัด [S5]\n• section number: 10 [S6]\n• completeness: Not yet confirmed\n\n**[Thai source] 1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน**\n• text: [Thai source] 1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน [S7]\n• heading: [Thai source] 1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน [S8]\n• section number: 11 [S9]\n• completeness: Not yet confirmed\n\n**[Thai source] 2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร**\n• text: [Thai source] 2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร [S10]\n• heading: [Thai source] 2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร [S11]\n• section number: 12 [S12]\n• completeness: Not yet confirmed\n\n**[Thai source] 3. หากสมาชิกคนใดถอนตัว ทีมอาจถูกตัดสิทธิ์**\n• text: [Thai source] 3. หากสมาชิกคนใดถอนตัว ทีมอาจถูกตัดสิทธิ์ [S13]\n• heading: [Thai source] 3. หากสมาชิกคนใดถอนตัว ทีมอาจถูกตัดสิทธิ์ [S14]\n• section number: 13 [S15]\n• completeness: Not yet confirmed\n\n**[Thai source] 4. ผู้เล่นสามารถลงแข่งในนามของทีมได้ทีมเดียวเท่านั้น**\n• text: [Thai source] 4. ผู้เล่นสามารถลงแข่งในนามของทีมได้ทีมเ … [ย่อจาก20,368ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 91. common / failures / test_entry_timing_measures_before_split (tests.test_competition_contract_r27_20261001.AtomicGraderTests.test_entry_timing_measures_before_split)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_contract_r27_20261001.py", line 98, in test_entry_timing_measures_before_split
    self.assertIn(stage,timing)
AssertionError: 'locale_resolution' not found in {}

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 92. common / failures / test_missing_game_clarifies_without_models (tests.test_competition_contract_r27_20261001.AtomicGraderTests.test_missing_game_clarifies_without_models) (locale='th')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_contract_r27_20261001.py", line 90, in test_missing_game_clarifies_without_models
    self.assertIn('clarification',result.mode)
AssertionError: 'clarification' not found in 'pipeline:common_answer'

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 93. common / failures / test_score_is_a_real_word_not_scope_typo (tests.test_competition_contract_r27_20261001.AtomicGraderTests.test_score_is_a_real_word_not_scope_typo)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_contract_r27_20261001.py", line 34, in test_score_is_a_real_word_not_scope_typo
    self.assertIn('13-0',result.answer.splitlines()[0])
AssertionError: '13-0' not found in 'The requested topic is unclear. Which part of [Thai source] PSU Phuket VALORANT 2026 Tournament do you need: event name / rulebook release / coverage?'

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 94. common / failures / test_settings_include_stage_and_advantage (tests.test_competition_contract_r27_20261001.AtomicGraderTests.test_settings_include_stage_and_advantage)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_contract_r27_20261001.py", line 45, in test_settings_include_stage_and_advantage
    self.assertIn('Stage: Random',result.answer)
AssertionError: 'Stage: Random' not found in 'The requested topic is unclear. Which part of [Thai source] PSU Esports ปะทะมันส์ สนั่นจอ do you need: event name / rulebook release / coverage?'

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 95. common / failures / test_cs2_english_table_preserves_pairs_and_continuation_reference (tests.test_competition_format_r25_20261001.CompetitionFormatAcceptance.test_cs2_english_table_preserves_pairs_and_continuation_reference)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_format_r25_20261001.py", line 73, in test_cs2_english_table_preserves_pairs_and_continuation_reference
    result = self.answer('Show the CS2 penalty table', 'en')
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_format_r25_20261001.py", line 24, in answer
    self.assertEqual(result.route.category, 'competition_rules')
AssertionError: 'knowledge' != 'competition_rules'
- knowledge
+ competition_rules


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 96. common / failures / test_cs2_table_contains_all_nine_correct_thai_pairs (tests.test_competition_format_r25_20261001.CompetitionFormatAcceptance.test_cs2_table_contains_all_nine_correct_thai_pairs)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_format_r25_20261001.py", line 55, in test_cs2_table_contains_all_nine_correct_thai_pairs
    result = self.answer('ขอตารางบทลงโทษ CS2', 'th')
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_format_r25_20261001.py", line 24, in answer
    self.assertEqual(result.route.category, 'competition_rules')
AssertionError: 'knowledge' != 'competition_rules'
- knowledge
+ competition_rules


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 97. common / failures / test_rovs_ipad_answer_is_permission_clause_not_document_heading (tests.test_competition_format_r25_20261001.CompetitionFormatAcceptance.test_rovs_ipad_answer_is_permission_clause_not_document_heading)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_format_r25_20261001.py", line 92, in test_rovs_ipad_answer_is_permission_clause_not_document_heading
    result = self.answer('Can I use a tablet or iPad in the RoV tournament?', 'en')
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_format_r25_20261001.py", line 24, in answer
    self.assertEqual(result.route.category, 'competition_rules')
AssertionError: 'no_answer' != 'competition_rules'
- no_answer
+ competition_rules


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 98. common / failures / test_team_number_is_in_first_english_sentence (tests.test_competition_format_r25_20261001.CompetitionFormatAcceptance.test_team_number_is_in_first_english_sentence)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_format_r25_20261001.py", line 100, in test_team_number_is_in_first_english_sentence
    result = self.answer('How many players are in a CS2 team?', 'en')
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_format_r25_20261001.py", line 24, in answer
    self.assertEqual(result.route.category, 'competition_rules')
AssertionError: 'knowledge' != 'competition_rules'
- knowledge
+ competition_rules


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 99. common / failures / test_technical_communication_first_sentence_and_no_other_pause_type (tests.test_competition_format_r25_20261001.CompetitionFormatAcceptance.test_technical_communication_first_sentence_and_no_other_pause_type) (locale='th')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_format_r25_20261001.py", line 34, in test_technical_communication_first_sentence_and_no_other_pause_type
    result = self.answer(question, locale)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_format_r25_20261001.py", line 24, in answer
    self.assertEqual(result.route.category, 'competition_rules')
AssertionError: 'knowledge' != 'competition_rules'
- knowledge
+ competition_rules


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 100. common / failures / test_technical_communication_first_sentence_and_no_other_pause_type (tests.test_competition_format_r25_20261001.CompetitionFormatAcceptance.test_technical_communication_first_sentence_and_no_other_pause_type) (locale='en')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_format_r25_20261001.py", line 34, in test_technical_communication_first_sentence_and_no_other_pause_type
    result = self.answer(question, locale)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_format_r25_20261001.py", line 24, in answer
    self.assertEqual(result.route.category, 'competition_rules')
AssertionError: 'knowledge' != 'competition_rules'
- knowledge
+ competition_rules


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 101. common / failures / test_thai_english_tekken_settings_match_source_values (tests.test_competition_format_r25_20261001.CompetitionFormatAcceptance.test_thai_english_tekken_settings_match_source_values) (locale='th')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_format_r25_20261001.py", line 118, in test_thai_english_tekken_settings_match_source_values
    result = self.answer(question, locale)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_format_r25_20261001.py", line 24, in answer
    self.assertEqual(result.route.category, 'competition_rules')
AssertionError: 'knowledge' != 'competition_rules'
- knowledge
+ competition_rules


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 102. common / failures / test_thai_english_tekken_settings_match_source_values (tests.test_competition_format_r25_20261001.CompetitionFormatAcceptance.test_thai_english_tekken_settings_match_source_values) (locale='en')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_format_r25_20261001.py", line 118, in test_thai_english_tekken_settings_match_source_values
    result = self.answer(question, locale)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_format_r25_20261001.py", line 24, in answer
    self.assertEqual(result.route.category, 'competition_rules')
AssertionError: 'knowledge' != 'competition_rules'
- knowledge
+ competition_rules


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 103. common / failures / test_unknown_technical_duration_does_not_borrow_tactical_or_emergency (tests.test_competition_format_r25_20261001.CompetitionFormatAcceptance.test_unknown_technical_duration_does_not_borrow_tactical_or_emergency) (locale='th')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_format_r25_20261001.py", line 49, in test_unknown_technical_duration_does_not_borrow_tactical_or_emergency
    answer = self.answer(question, locale).answer
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_format_r25_20261001.py", line 24, in answer
    self.assertEqual(result.route.category, 'competition_rules')
AssertionError: 'knowledge' != 'competition_rules'
- knowledge
+ competition_rules


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 104. common / failures / test_unknown_technical_duration_does_not_borrow_tactical_or_emergency (tests.test_competition_format_r25_20261001.CompetitionFormatAcceptance.test_unknown_technical_duration_does_not_borrow_tactical_or_emergency) (locale='en')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_format_r25_20261001.py", line 49, in test_unknown_technical_duration_does_not_borrow_tactical_or_emergency
    answer = self.answer(question, locale).answer
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_format_r25_20261001.py", line 24, in answer
    self.assertEqual(result.route.category, 'competition_rules')
AssertionError: 'knowledge' != 'competition_rules'
- knowledge
+ competition_rules


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 105. common / failures / test_valorant_penalty_types_keep_all_five_source_conditions_once (tests.test_competition_format_r25_20261001.CompetitionFormatAcceptance.test_valorant_penalty_types_keep_all_five_source_conditions_once)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_format_r25_20261001.py", line 106, in test_valorant_penalty_types_keep_all_five_source_conditions_once
    result = self.answer('What do the VALORANT tournament rules say about penalties?', 'en')
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_format_r25_20261001.py", line 24, in answer
    self.assertEqual(result.route.category, 'competition_rules')
AssertionError: 'knowledge' != 'competition_rules'
- knowledge
+ competition_rules


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 106. common / failures / test_known_game_identity_does_not_compete_with_catalogue (tests.test_competition_session_context_r35.CompetitionSessionContextR35Tests.test_known_game_identity_does_not_compete_with_catalogue)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_session_context_r35.py", line 119, in test_known_game_identity_does_not_compete_with_catalogue
    self.assertEqual(r.route.category,'games')
AssertionError: 'knowledge' != 'games'
- knowledge
+ games


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 107. common / failures / test_checkin_question_does_not_use_an_unrelated_note_rule (tests.test_competition_target_grounding.CompetitionTargetGroundingTests.test_checkin_question_does_not_use_an_unrelated_note_rule)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_target_grounding.py", line 185, in test_checkin_question_does_not_use_an_unrelated_note_rule
    self.assertEqual(result.mode, "pipeline:competition_facet_not_covered_no_answer")
AssertionError: 'pipeline:common_clarification' != 'pipeline:competition_facet_not_covered_no_answer'
- pipeline:common_clarification
+ pipeline:competition_facet_not_covered_no_answer


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 108. common / failures / test_checkin_renderer_does_not_append_adjacent_match_prep_rules (tests.test_competition_target_grounding.CompetitionTargetGroundingTests.test_checkin_renderer_does_not_append_adjacent_match_prep_rules)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_target_grounding.py", line 197, in test_checkin_renderer_does_not_append_adjacent_match_prep_rules
    self.assertEqual(result.mode, "pipeline:competition_source_rag")
AssertionError: 'pipeline:common_clarification' != 'pipeline:competition_source_rag'
- pipeline:common_clarification
+ pipeline:competition_source_rag


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 109. common / failures / test_english_comparison_keeps_both_targets_before_localization_check (tests.test_competition_target_grounding.CompetitionTargetGroundingTests.test_english_comparison_keeps_both_targets_before_localization_check)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_target_grounding.py", line 285, in test_english_comparison_keeps_both_targets_before_localization_check
    self.assertEqual(result.mode, "pipeline:competition_source_localization_pending_en")
AssertionError: 'pipeline:common_partial_answer' != 'pipeline:competition_source_localization_pending_en'
- pipeline:common_partial_answer
+ pipeline:competition_source_localization_pending_en


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 110. common / failures / test_english_general_match_issue_does_not_use_bug_or_post_match_text (tests.test_competition_target_grounding.CompetitionTargetGroundingTests.test_english_general_match_issue_does_not_use_bug_or_post_match_text)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_target_grounding.py", line 271, in test_english_general_match_issue_does_not_use_bug_or_post_match_text
    self.assertEqual(result.mode, "pipeline:competition_facet_not_covered_no_answer_en")
AssertionError: 'pipeline:common_clarification' != 'pipeline:competition_facet_not_covered_no_answer_en'
- pipeline:common_clarification
+ pipeline:competition_facet_not_covered_no_answer_en


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 111. common / failures / test_english_missing_valorant_conduct_does_not_become_translation_pending (tests.test_competition_target_grounding.CompetitionTargetGroundingTests.test_english_missing_valorant_conduct_does_not_become_translation_pending)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_target_grounding.py", line 246, in test_english_missing_valorant_conduct_does_not_become_translation_pending
    self.assertEqual(result.mode, "pipeline:competition_facet_not_covered_no_answer_en")
AssertionError: 'pipeline:common_answer' != 'pipeline:competition_facet_not_covered_no_answer_en'
- pipeline:common_answer
+ pipeline:competition_facet_not_covered_no_answer_en


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 112. common / failures / test_english_protest_question_without_target_requests_a_game (tests.test_competition_target_grounding.CompetitionTargetGroundingTests.test_english_protest_question_without_target_requests_a_game)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_target_grounding.py", line 235, in test_english_protest_question_without_target_requests_a_game
    self.assertEqual(result.mode, "pipeline:competition_target_clarification_en")
AssertionError: 'pipeline:request_timeout_no_answer' != 'pipeline:competition_target_clarification_en'
- pipeline:request_timeout_no_answer
+ pipeline:competition_target_clarification_en


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 113. common / failures / test_english_starting_player_question_does_not_use_match_prep_capacity (tests.test_competition_target_grounding.CompetitionTargetGroundingTests.test_english_starting_player_question_does_not_use_match_prep_capacity)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_target_grounding.py", line 258, in test_english_starting_player_question_does_not_use_match_prep_capacity
    self.assertEqual(result.mode, "pipeline:competition_facet_not_covered_no_answer_en")
AssertionError: 'pipeline:common_clarification' != 'pipeline:competition_facet_not_covered_no_answer_en'
- pipeline:common_clarification
+ pipeline:competition_facet_not_covered_no_answer_en


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 114. common / failures / test_english_untargeted_rule_question_requests_a_game (tests.test_competition_target_grounding.CompetitionTargetGroundingTests.test_english_untargeted_rule_question_requests_a_game)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_target_grounding.py", line 223, in test_english_untargeted_rule_question_requests_a_game
    self.assertEqual(result.mode, "pipeline:competition_target_clarification_en")
AssertionError: 'pipeline:request_timeout_no_answer' != 'pipeline:competition_target_clarification_en'
- pipeline:request_timeout_no_answer
+ pipeline:competition_target_clarification_en


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 115. common / failures / test_generic_in_match_process_does_not_use_a_graph_setting (tests.test_competition_target_grounding.CompetitionTargetGroundingTests.test_generic_in_match_process_does_not_use_a_graph_setting)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_target_grounding.py", line 211, in test_generic_in_match_process_does_not_use_a_graph_setting
    self.assertEqual(result.mode, "pipeline:competition_facet_not_covered_no_answer")
AssertionError: 'pipeline:common_clarification' != 'pipeline:competition_facet_not_covered_no_answer'
- pipeline:common_clarification
+ pipeline:competition_facet_not_covered_no_answer


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 116. common / failures / test_generic_settings_query_renders_settings_not_timeout (tests.test_competition_target_grounding.CompetitionTargetGroundingTests.test_generic_settings_query_renders_settings_not_timeout)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_target_grounding.py", line 121, in test_generic_settings_query_renders_settings_not_timeout
    self.assertEqual(result.mode, "pipeline:competition_source_rag")
AssertionError: 'pipeline:common_clarification' != 'pipeline:competition_source_rag'
- pipeline:common_clarification
+ pipeline:competition_source_rag


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 117. common / failures / test_in_match_contact_requires_a_contact_instruction (tests.test_competition_target_grounding.CompetitionTargetGroundingTests.test_in_match_contact_requires_a_contact_instruction)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_target_grounding.py", line 161, in test_in_match_contact_requires_a_contact_instruction
    self.assertEqual(result.mode, "pipeline:competition_facet_not_covered_no_answer")
AssertionError: 'pipeline:common_clarification' != 'pipeline:competition_facet_not_covered_no_answer'
- pipeline:common_clarification
+ pipeline:competition_facet_not_covered_no_answer


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 118. common / failures / test_missing_target_facet_does_not_substitute_another_rule (tests.test_competition_target_grounding.CompetitionTargetGroundingTests.test_missing_target_facet_does_not_substitute_another_rule)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_target_grounding.py", line 135, in test_missing_target_facet_does_not_substitute_another_rule
    self.assertEqual(result.mode, "pipeline:competition_facet_not_covered_no_answer")
AssertionError: 'pipeline:common_clarification' != 'pipeline:competition_facet_not_covered_no_answer'
- pipeline:common_clarification
+ pipeline:competition_facet_not_covered_no_answer


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 119. common / failures / test_roster_question_requires_starter_and_substitute_evidence (tests.test_competition_target_grounding.CompetitionTargetGroundingTests.test_roster_question_requires_starter_and_substitute_evidence)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_target_grounding.py", line 173, in test_roster_question_requires_starter_and_substitute_evidence
    self.assertEqual(result.mode, "pipeline:competition_facet_not_covered_no_answer")
AssertionError: 'pipeline:common_clarification' != 'pipeline:competition_facet_not_covered_no_answer'
- pipeline:common_clarification
+ pipeline:competition_facet_not_covered_no_answer


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 120. common / failures / test_unsupported_english_rulebook_skips_live_booking (tests.test_competition_target_grounding.CompetitionTargetGroundingTests.test_unsupported_english_rulebook_skips_live_booking)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_target_grounding.py", line 298, in test_unsupported_english_rulebook_skips_live_booking
    self.assertEqual(result.mode, "pipeline:competition_unknown_target_no_answer")
AssertionError: 'pipeline:request_timeout_no_answer' != 'pipeline:competition_unknown_target_no_answer'
- pipeline:request_timeout_no_answer
+ pipeline:competition_unknown_target_no_answer


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 121. common / failures / test_untargeted_rule_question_clarifies_instead_of_defaulting_to_cs2 (tests.test_competition_target_grounding.CompetitionTargetGroundingTests.test_untargeted_rule_question_clarifies_instead_of_defaulting_to_cs2)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_target_grounding.py", line 108, in test_untargeted_rule_question_clarifies_instead_of_defaulting_to_cs2
    self.assertEqual(result.route.category, "competition_rules")
AssertionError: 'no_answer' != 'competition_rules'
- no_answer
+ competition_rules


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 122. common / failures / test_competition_schedule_cannot_use_booking_schedule (tests.test_competition_user_questions_r24_20261001.CompetitionUserQuestions.test_competition_schedule_cannot_use_booking_schedule)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_user_questions_r24_20261001.py", line 85, in test_competition_schedule_cannot_use_booking_schedule
    self.assertEqual(result.route.category, 'competition_rules')
AssertionError: 'knowledge' != 'competition_rules'
- knowledge
+ competition_rules


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 123. common / failures / test_english_overviews_use_recorded_localization (tests.test_competition_user_questions_r24_20261001.CompetitionUserQuestions.test_english_overviews_use_recorded_localization) (game='cs2')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_user_questions_r24_20261001.py", line 72, in test_english_overviews_use_recorded_localization
    self.assertEqual(result.mode, 'pipeline:competition_rule_overview_source')
AssertionError: 'pipeline:common_answer' != 'pipeline:competition_rule_overview_source'
- pipeline:common_answer
+ pipeline:competition_rule_overview_source


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 124. common / failures / test_english_overviews_use_recorded_localization (tests.test_competition_user_questions_r24_20261001.CompetitionUserQuestions.test_english_overviews_use_recorded_localization) (game='tekken 8')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_user_questions_r24_20261001.py", line 72, in test_english_overviews_use_recorded_localization
    self.assertEqual(result.mode, 'pipeline:competition_rule_overview_source')
AssertionError: 'pipeline:common_answer' != 'pipeline:competition_rule_overview_source'
- pipeline:common_answer
+ pipeline:competition_rule_overview_source


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 125. common / failures / test_english_overviews_use_recorded_localization (tests.test_competition_user_questions_r24_20261001.CompetitionUserQuestions.test_english_overviews_use_recorded_localization) (game='valorant')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_user_questions_r24_20261001.py", line 72, in test_english_overviews_use_recorded_localization
    self.assertEqual(result.mode, 'pipeline:competition_rule_overview_source')
AssertionError: 'pipeline:common_answer' != 'pipeline:competition_rule_overview_source'
- pipeline:common_answer
+ pipeline:competition_rule_overview_source


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 126. common / failures / test_known_numeric_and_negative_clauses (tests.test_competition_user_questions_r24_20261001.CompetitionUserQuestions.test_known_numeric_and_negative_clauses) (query='CS2 แข่งทีมละกี่คน')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_user_questions_r24_20261001.py", line 100, in test_known_numeric_and_negative_clauses
    self.assertEqual(result.route.category, 'competition_rules')
AssertionError: 'knowledge' != 'competition_rules'
- knowledge
+ competition_rules


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 127. common / failures / test_known_numeric_and_negative_clauses (tests.test_competition_user_questions_r24_20261001.CompetitionUserQuestions.test_known_numeric_and_negative_clauses) (query='Tekken 8 รูปแบบการแข่งขันเป็นอย่างไร')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_user_questions_r24_20261001.py", line 100, in test_known_numeric_and_negative_clauses
    self.assertEqual(result.route.category, 'competition_rules')
AssertionError: 'knowledge' != 'competition_rules'
- knowledge
+ competition_rules


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 128. common / failures / test_known_numeric_and_negative_clauses (tests.test_competition_user_questions_r24_20261001.CompetitionUserQuestions.test_known_numeric_and_negative_clauses) (query='RoV ใช้ Tablet หรือ iPad แข่งได้ไหม')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_user_questions_r24_20261001.py", line 100, in test_known_numeric_and_negative_clauses
    self.assertEqual(result.route.category, 'competition_rules')
AssertionError: 'no_answer' != 'competition_rules'
- no_answer
+ competition_rules


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 129. common / failures / test_known_numeric_and_negative_clauses (tests.test_competition_user_questions_r24_20261001.CompetitionUserQuestions.test_known_numeric_and_negative_clauses) (query='VALORANT technical pause สื่อสารได้ไหม')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_user_questions_r24_20261001.py", line 100, in test_known_numeric_and_negative_clauses
    self.assertEqual(result.route.category, 'competition_rules')
AssertionError: 'knowledge' != 'competition_rules'
- knowledge
+ competition_rules


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 130. common / failures / test_user_questions_enter_competition_not_catalog (tests.test_competition_user_questions_r24_20261001.CompetitionUserQuestions.test_user_questions_enter_competition_not_catalog) (game='cs2')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_user_questions_r24_20261001.py", line 62, in test_user_questions_enter_competition_not_catalog
    self.assertEqual(result.mode, 'pipeline:competition_rule_overview_source')
AssertionError: 'pipeline:common_answer' != 'pipeline:competition_rule_overview_source'
- pipeline:common_answer
+ pipeline:competition_rule_overview_source


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 131. common / failures / test_user_questions_enter_competition_not_catalog (tests.test_competition_user_questions_r24_20261001.CompetitionUserQuestions.test_user_questions_enter_competition_not_catalog) (game='rov')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_user_questions_r24_20261001.py", line 62, in test_user_questions_enter_competition_not_catalog
    self.assertEqual(result.mode, 'pipeline:competition_rule_overview_source')
AssertionError: 'pipeline:common_answer' != 'pipeline:competition_rule_overview_source'
- pipeline:common_answer
+ pipeline:competition_rule_overview_source


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 132. common / failures / test_user_questions_enter_competition_not_catalog (tests.test_competition_user_questions_r24_20261001.CompetitionUserQuestions.test_user_questions_enter_competition_not_catalog) (game='tekken 8')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_user_questions_r24_20261001.py", line 62, in test_user_questions_enter_competition_not_catalog
    self.assertEqual(result.mode, 'pipeline:competition_rule_overview_source')
AssertionError: 'pipeline:common_answer' != 'pipeline:competition_rule_overview_source'
- pipeline:common_answer
+ pipeline:competition_rule_overview_source


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 133. common / failures / test_user_questions_enter_competition_not_catalog (tests.test_competition_user_questions_r24_20261001.CompetitionUserQuestions.test_user_questions_enter_competition_not_catalog) (game='วาโล')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_user_questions_r24_20261001.py", line 62, in test_user_questions_enter_competition_not_catalog
    self.assertEqual(result.mode, 'pipeline:competition_rule_overview_source')
AssertionError: 'pipeline:common_answer' != 'pipeline:competition_rule_overview_source'
- pipeline:common_answer
+ pipeline:competition_rule_overview_source


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 134. common / failures / test_choices_and_paraphrases (tests.test_conversation_flow_r38.FlowTests.test_choices_and_paraphrases) (locale='en', q='the PC one')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_conversation_flow_r38.py", line 41, in test_choices_and_paraphrases
    self.assertEqual(r.route.category,'service_fee')
AssertionError: 'knowledge' != 'service_fee'
- knowledge
+ service_fee


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 135. common / failures / test_each_every_rule_scope (tests.test_conversation_flow_r38.FlowTests.test_each_every_rule_scope)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_conversation_flow_r38.py", line 251, in test_each_every_rule_scope
    self.assertEqual(result.route.category,'competition_rules')
AssertionError: 'knowledge' != 'competition_rules'
- knowledge
+ competition_rules


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 136. common / failures / test_full_rules_summary_and_delivery (tests.test_conversation_flow_r38.FlowTests.test_full_rules_summary_and_delivery)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_conversation_flow_r38.py", line 182, in test_full_rules_summary_and_delivery
    self.assertEqual(full.mode,'pipeline:competition_rule_full_sections_source')
AssertionError: 'pipeline:common_answer' != 'pipeline:competition_rule_full_sections_source'
- pipeline:common_answer
+ pipeline:competition_rule_full_sections_source


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 137. common / failures / test_booking_policy_fields_answer_the_actual_requested_quantity (tests.test_domain_resume_r42.DomainResumeR42Tests.test_booking_policy_fields_answer_the_actual_requested_quantity)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_domain_resume_r42.py", line 116, in test_booking_policy_fields_answer_the_actual_requested_quantity
    self.assertEqual(r.route.category,'reservation',q)
AssertionError: 'knowledge' != 'reservation'
- knowledge
+ reservation
 : ต้องจองล่วงหน้ากี่วัน

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 138. common / failures / test_invalid_or_excess_resume_plan_cannot_fall_through_to_unrelated_answer (tests.test_domain_resume_r42.DomainResumeR42Tests.test_invalid_or_excess_resume_plan_cannot_fall_through_to_unrelated_answer)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_domain_resume_r42.py", line 151, in test_invalid_or_excess_resume_plan_cannot_fall_through_to_unrelated_answer
    self.assertEqual(r.mode,'pipeline:dialogue_state_clarification')
AssertionError: 'pipeline:common_clarification' != 'pipeline:dialogue_state_clarification'
- pipeline:common_clarification
+ pipeline:dialogue_state_clarification


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 139. common / failures / test_maximum_days_and_minimum_hour_are_different_facets (tests.test_domain_resume_r42.DomainResumeR42Tests.test_maximum_days_and_minimum_hour_are_different_facets)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_domain_resume_r42.py", line 90, in test_maximum_days_and_minimum_hour_are_different_facets
    self.assertIn('booking_maximum_lead_unconfirmed',r.mode)
AssertionError: 'booking_maximum_lead_unconfirmed' not found in 'pipeline:common_clarification'

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 140. common / failures / test_same_operation_compound_resume_reexecutes_every_child (tests.test_domain_resume_r42.DomainResumeR42Tests.test_same_operation_compound_resume_reexecutes_every_child)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_domain_resume_r42.py", line 131, in test_same_operation_compound_resume_reexecutes_every_child
    p=s.begin('s','r','back to the opening hours',locale='en');self.assertEqual(p['plan']['schema_type'],'dialogue_resume_v1')
                                                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 'dialogue_state_clarification_v1' != 'dialogue_resume_v1'
- dialogue_state_clarification_v1
+ dialogue_resume_v1


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 141. common / failures / test_alumni_price_does_not_fall_back_to_all_groups (tests.test_input_downstream_r29_20261002.InputDownstreamR29Tests.test_alumni_price_does_not_fall_back_to_all_groups)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_input_downstream_r29_20261002.py", line 28, in test_alumni_price_does_not_fall_back_to_all_groups
    self.assertIn('PSU alumni and students from other institutions: 50 THB',result.answer)
AssertionError: 'PSU alumni and students from other institutions: 50 THB' not found in 'Service prices (recorded package rates):\n\nNintendo Switch — 60 minutes/package (1-2 people)\nRequested duration: 60 minutes (1 hours); 1 session(s).\n• PSU alumni / students from other institutions: 50 THB/package\n\nNintendo Switch — 60 minutes/package (3-4 people)\nRequested duration: 60 minutes (1 hours); 1 session(s).\n• PSU alumni / students from other institutions: 100 THB/package\nThe original fee table states validity through 2026-03-31; continued validity for the requested date has not been confirmed.\nSource: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png'

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 142. common / failures / test_booking_verb_in_need_to_frame_keeps_operation (tests.test_input_downstream_r29_20261002.InputDownstreamR29Tests.test_booking_verb_in_need_to_frame_keeps_operation)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_input_downstream_r29_20261002.py", line 36, in test_booking_verb_in_need_to_frame_keeps_operation
    self.assertIn('Booking steps:',answer(q).answer)
AssertionError: 'Booking steps:' not found in 'The requested topic is unclear. Which part of [Thai source] Beat Saber do you need: platform / input device / preset / bindings?'

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 143. common / failures / test_eligibility_label_and_duration_are_kept_in_compound_price (tests.test_input_downstream_r29_20261002.InputDownstreamR29Tests.test_eligibility_label_and_duration_are_kept_in_compound_price)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_input_downstream_r29_20261002.py", line 22, in test_eligibility_label_and_duration_are_kept_in_compound_price
    self.assertIn('120 minutes, charged as 2 session', result.answer)
AssertionError: '120 minutes, charged as 2 session' not found in 'Service prices (recorded package rates):\n\nNintendo Switch — 60 minutes/package (1-2 people)\nRequested duration: 120 minutes (2 hours); 2 session(s).\n• PSU students and staff: 0 THB/package × 2 = 0 THB\n\nNintendo Switch — 60 minutes/package (3-4 people)\nRequested duration: 120 minutes (2 hours); 2 session(s).\n• PSU students and staff: 0 THB/package × 2 = 0 THB\nThe original fee table states validity through 2026-03-31; continued validity for the requested date has not been confirmed.\nSource: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png'

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 144. common / failures / test_full_name_suggestion_is_conditional_and_source_spelling_is_exact (tests.test_input_downstream_r29_20261002.InputDownstreamR29Tests.test_full_name_suggestion_is_conditional_and_source_spelling_is_exact)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_input_downstream_r29_20261002.py", line 55, in test_full_name_suggestion_is_conditional_and_source_spelling_is_exact
    self.assertIn('หากหมายถึง ผศ.ดร.ณัฐพงศ์ ทองเทพ',result.answer)
AssertionError: 'หากหมายถึง ผศ.ดร.ณัฐพงศ์ ทองเทพ' not found in 'ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ ผศ.ดร.ณัฐพงศ์ ทองเทพ เช่น ชื่อที่อนุญาตให้เผยแพร่ / ตำแหน่ง/หน้าที่ / รายละเอียดที่เผยแพร่ได้ ไม่ใส่ข้อมูลลูกค้าหรือสลิป?'

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 145. common / failures / test_price_words_can_recover_two_errors_with_values_unchanged (tests.test_input_downstream_r29_20261002.InputDownstreamR29Tests.test_price_words_can_recover_two_errors_with_values_unchanged)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_input_downstream_r29_20261002.py", line 18, in test_price_words_can_recover_two_errors_with_values_unchanged
    self.assertIn('60 minutes, charged as 1 session', result.answer)
AssertionError: '60 minutes, charged as 1 session' not found in 'Service prices (recorded package rates):\n\nVR — 60 minutes/package (1-5 people)\nRequested duration: 60 minutes (1 hours); 1 session(s).\n• PSU students and staff: 0 THB/package\nThe original fee table states validity through 2026-03-31; continued validity for the requested date has not been confirmed.\nSource: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png'

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 146. common / failures / test_vector_control_answer_keeps_secondary_source_review_note (tests.test_input_downstream_r29_20261002.InputDownstreamR29Tests.test_vector_control_answer_keeps_secondary_source_review_note)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_input_downstream_r29_20261002.py", line 66, in test_vector_control_answer_keeps_secondary_source_review_note
    self.assertIn('D-Pad Down',result.answer)
AssertionError: 'D-Pad Down' not found in '**ซูเปอร์มาริโอ้โอดิสซีย์**\n• ปุ่มควบคุม: เพิ่มทีละปุ่มหรือชุดปุ่ม: ยังไม่มีข้อมูลยืนยัน\n• แพลตฟอร์ม เช่น PC หรือ PS5: Nintendo Switch [S1]\n• อุปกรณ์ควบคุม: ยังไม่มีข้อมูลยืนยัน\n• ชื่อชุดปุ่ม เช่น default: ยังไม่มีข้อมูลยืนยัน'

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 147. common / failures / test_semantic_cases (tests.test_integrated_improvement_r21_20261001.IntegratedImprovementTests.test_semantic_cases) (case='polite-not-ps5')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_integrated_improvement_r21_20261001.py", line 59, in test_semantic_cases
    self.assertTrue(row['passed'], row)
AssertionError: False is not true : {'id': 'polite-not-ps5', 'locale': 'th', 'question': 'กำลังวางแผนไปใช้บริการ เลยอยากทราบว่า Counter-Strike 2 เล่นได้ที่โซนไหน', 'expected_route': 'games', 'required_groups': (('Counter-Strike 2',), ('PC Zone',)), 'forbidden': ('ไม่พบเกม', 'PlayStation'), 'expected_live_fetch': False, 'live_fetches': 0, 'route': 'knowledge', 'mode': 'pipeline:common_clarification', 'answer': 'ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ Counter-Strike 2 เช่น ชื่อรายการ+ปี+ประเภทให้ตรง / ฉบับกติกาและวันที่ / เอกสารกติกาครบหรือมีเพียงบางส่วน / แพลตฟอร์ม เช่น PC หรือ PS5?', 'elapsed_sec': 0.1563377999700606, 'passed': False, 'failures': ['route knowledge != games', "missing group ('PC Zone',)"], 'trace': [{'stage': 'common_content', 'decision': 'clarification', 'confidence': 0.0, 'detail': 'typed fields and source-backed joins; uncalibrated confidence', 'metadata': {'response_type': 'clarification', 'release_id': 'EVAL_DRAFT_ONLY', 'query_plan': {'record_ids': ['game_detail_cs2', 'competition_competition_rules_cs2_psu_phuket_2026', 'controls_pc_counter_strike_2', 'availability_pc_01_02', 'availability_pc_03_10'], 'requested_fields': [], 'all_fields': False, 'method': 'exact', 'scope': 'common_published', 'platform': None, 'query_without_entity': 'กำลังวางแผนไปใช้บริการ เลยอยากทราบว่า เล่นได้ที่โซนไหน', 'field_selection': [], 'confidence_calibrated': False, 'request_focus': None, 'authority': {'decision': 'common', 'reason': 'published_target_owned', 'record_ids': ['game_detai … [ย่อจาก2,359ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 148. common / failures / test_semantic_cases (tests.test_integrated_improvement_r21_20261001.IntegratedImprovementTests.test_semantic_cases) (case='spatial-duplicate')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_integrated_improvement_r21_20261001.py", line 59, in test_semantic_cases
    self.assertTrue(row['passed'], row)
AssertionError: False is not true : {'id': 'spatial-duplicate', 'locale': 'th', 'question': 'PUBG: BATTLEGROUNDS เล่นได้ทที่ไหน', 'expected_route': 'games', 'required_groups': (('PUBG',), ('PC',)), 'forbidden': ('09:00',), 'expected_live_fetch': False, 'live_fetches': 0, 'route': 'knowledge', 'mode': 'pipeline:common_clarification', 'answer': 'ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ พับจี เช่น แพลตฟอร์ม เช่น PC หรือ PS5 / อุปกรณ์ควบคุม / ชื่อชุดปุ่ม เช่น default / ปุ่มควบคุม: เพิ่มทีละปุ่มหรือชุดปุ่ม?', 'elapsed_sec': 0.1020375001244247, 'passed': False, 'failures': ['route knowledge != games', "missing group ('PUBG',)"], 'trace': [{'stage': 'common_content', 'decision': 'clarification', 'confidence': 0.0, 'detail': 'typed fields and source-backed joins; uncalibrated confidence', 'metadata': {'response_type': 'clarification', 'release_id': 'EVAL_DRAFT_ONLY', 'query_plan': {'record_ids': ['controls_pc_pubg_battlegrounds', 'availability_pc_01_02', 'availability_pc_03_10'], 'requested_fields': [], 'all_fields': False, 'method': 'exact', 'scope': 'common_published', 'platform': None, 'query_without_entity': 'เล่นได้ทที่ไหน', 'field_selection': [], 'confidence_calibrated': False, 'request_focus': None, 'authority': {'decision': 'common', 'reason': 'published_target_owned', 'record_ids': ['controls_pc_pubg_battlegrounds', 'availability_pc_01_02', 'availability_pc_03_10'], 'release_id': 'EVAL_DRAFT_ONLY', 'epoch': 584}, 'field_authority': [], 'unresolved_clauses': ['เล่นได้ทที่ไหน'], 'semanti … [ย่อจาก2,054ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 149. common / failures / test_semantic_cases (tests.test_integrated_improvement_r21_20261001.IntegratedImprovementTests.test_semantic_cases) (case='vr-duration')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_integrated_improvement_r21_20261001.py", line 59, in test_semantic_cases
    self.assertTrue(row['passed'], row)
AssertionError: False is not true : {'id': 'vr-duration', 'locale': 'th', 'question': 'VR Zone รอบละกีน่าที', 'expected_route': 'reservation', 'required_groups': (('30',), ('60',), ('นาที',)), 'forbidden': (), 'expected_live_fetch': False, 'live_fetches': 0, 'route': 'knowledge', 'mode': 'pipeline:common_clarification', 'answer': 'ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ VR Zone เช่น ชื่อบริการตามหน้า WordPress / แพลตฟอร์ม เช่น PC หรือ PS5 / เวลาเล่น (นาที) / เวลาที่ล็อกเครื่อง (นาที)?', 'elapsed_sec': 0.1045764998998493, 'passed': False, 'failures': ['route knowledge != reservation', "missing group ('30',)", "missing group ('60',)"], 'trace': [{'stage': 'common_content', 'decision': 'clarification', 'confidence': 0.0, 'detail': 'typed fields and source-backed joins; uncalibrated confidence', 'metadata': {'response_type': 'clarification', 'release_id': 'EVAL_DRAFT_ONLY', 'query_plan': {'record_ids': ['zone_vr', 'availability_vr_30', 'availability_vr_60'], 'requested_fields': [], 'all_fields': False, 'method': 'exact', 'scope': 'common_published', 'platform': None, 'query_without_entity': 'รอบละกีน่าที', 'field_selection': [], 'confidence_calibrated': False, 'request_focus': None, 'authority': {'decision': 'common', 'reason': 'published_target_owned', 'record_ids': ['zone_vr', 'availability_vr_30', 'availability_vr_60'], 'release_id': 'EVAL_DRAFT_ONLY', 'epoch': 584}, 'field_authority': [], 'unresolved_clauses': ['รอบละกีน่าที'], 'semantic_review_needed': True, 'semantic_plan_accepted':  … [ย่อจาก2,004ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 150. common / failures / test_semantic_cases (tests.test_integrated_improvement_r21_20261001.IntegratedImprovementTests.test_semantic_cases) (case='game-detail')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_integrated_improvement_r21_20261001.py", line 59, in test_semantic_cases
    self.assertTrue(row['passed'], row)
AssertionError: False is not true : {'id': 'game-detail', 'locale': 'th', 'question': 'ช่วยตอบจาข้อมูลที่ยืนยันได้หน่อย: Counter-Strike 2 คือเกมอะไน', 'expected_route': 'games', 'required_groups': (('Counter-Strike 2',), ('ฝ่ายบุก',), ('ระเบิด',)), 'forbidden': ('ยังไม่พบข้อมูล',), 'expected_live_fetch': False, 'live_fetches': 0, 'route': 'knowledge', 'mode': 'pipeline:common_clarification', 'answer': 'ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ Counter-Strike 2 เช่น ชื่อรายการ+ปี+ประเภทให้ตรง / ฉบับกติกาและวันที่ / เอกสารกติกาครบหรือมีเพียงบางส่วน / แพลตฟอร์ม เช่น PC หรือ PS5?', 'elapsed_sec': 0.09970690007321537, 'passed': False, 'failures': ['route knowledge != games', "missing group ('ฝ่ายบุก',)", "missing group ('ระเบิด',)"], 'trace': [{'stage': 'common_content', 'decision': 'clarification', 'confidence': 0.0, 'detail': 'typed fields and source-backed joins; uncalibrated confidence', 'metadata': {'response_type': 'clarification', 'release_id': 'EVAL_DRAFT_ONLY', 'query_plan': {'record_ids': ['game_detail_cs2', 'competition_competition_rules_cs2_psu_phuket_2026', 'controls_pc_counter_strike_2', 'availability_pc_01_02', 'availability_pc_03_10'], 'requested_fields': [], 'all_fields': False, 'method': 'exact', 'scope': 'common_published', 'platform': None, 'query_without_entity': 'ช่วยตอบจาข้อมูลที่ยืนยันได้หน่อย: คือเกมอะไน', 'field_selection': [], 'confidence_calibrated': False, 'request_focus': None, 'authority': {'decision': 'common', 'reason': 'published_target_owned', 'record_ids':  … [ย่อจาก2,361ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 151. common / failures / test_semantic_cases (tests.test_integrated_improvement_r21_20261001.IntegratedImprovementTests.test_semantic_cases) (case='detail-two-edits')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_integrated_improvement_r21_20261001.py", line 59, in test_semantic_cases
    self.assertTrue(row['passed'], row)
AssertionError: False is not true : {'id': 'detail-two-edits', 'locale': 'th', 'question': 'EA Sports FC 24 คือเดมอะร', 'expected_route': 'games', 'required_groups': (('EA Sports FC 24',), ('ฟุตบอล',), ('ทำประตู',)), 'forbidden': (), 'expected_live_fetch': False, 'live_fetches': 0, 'route': 'knowledge', 'mode': 'pipeline:common_clarification', 'answer': 'ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ EA Sports FC 24 เช่น แพลตฟอร์ม เช่น PC หรือ PS5 / อุปกรณ์ควบคุม / ชื่อชุดปุ่ม เช่น default / ปุ่มควบคุม: เพิ่มทีละปุ่มหรือชุดปุ่ม?', 'elapsed_sec': 0.11462010000832379, 'passed': False, 'failures': ['route knowledge != games', "missing group ('ฟุตบอล',)", "missing group ('ทำประตู',)"], 'trace': [{'stage': 'common_content', 'decision': 'clarification', 'confidence': 0.0, 'detail': 'typed fields and source-backed joins; uncalibrated confidence', 'metadata': {'response_type': 'clarification', 'release_id': 'EVAL_DRAFT_ONLY', 'query_plan': {'record_ids': ['game_detail_ea_sports_fc_24', 'controls_ps5_ea_sports_fc_24', 'availability_ps5_01_02'], 'requested_fields': [], 'all_fields': False, 'method': 'exact', 'scope': 'common_published', 'platform': None, 'query_without_entity': 'คือเดมอะร', 'field_selection': [], 'confidence_calibrated': False, 'request_focus': None, 'authority': {'decision': 'common', 'reason': 'published_target_owned', 'record_ids': ['game_detail_ea_sports_fc_24', 'controls_ps5_ea_sports_fc_24', 'availability_ps5_01_02'], 'release_id': 'EVAL_DRAFT_ONLY', 'epoch': 584}, 'field_authori … [ย่อจาก2,108ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 152. common / failures / test_semantic_cases (tests.test_integrated_improvement_r21_20261001.IntegratedImprovementTests.test_semantic_cases) (case='booking-limit')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_integrated_improvement_r21_20261001.py", line 59, in test_semantic_cases
    self.assertTrue(row['passed'], row)
AssertionError: False is not true : {'id': 'booking-limit', 'locale': 'en', 'question': 'How many sessioons can one booking include', 'expected_route': 'reservation', 'required_groups': (('maximum',), ('3 sessions',)), 'forbidden': ('Booking steps:',), 'expected_live_fetch': False, 'live_fetches': 0, 'route': 'knowledge', 'mode': 'pipeline:common_clarification', 'answer': 'The requested topic is unclear. Which part of [Thai source] สูงสุดกี่ session do you need: question / answer / topic?', 'elapsed_sec': 0.14039479987695813, 'passed': False, 'failures': ['route knowledge != reservation', "missing group ('maximum',)", "missing group ('3 sessions',)"], 'trace': [{'stage': 'common_content', 'decision': 'clarification', 'confidence': 0.0, 'detail': 'typed fields and source-backed joins; uncalibrated confidence', 'metadata': {'response_type': 'clarification', 'release_id': 'EVAL_DRAFT_ONLY', 'query_plan': {'record_ids': ['migrated_faq_rule_booking_max_sessions'], 'requested_fields': [], 'all_fields': False, 'method': 'unique_repeat_edit', 'scope': 'common_published', 'platform': None, 'query_without_entity': 'can one booking include', 'field_selection': [], 'confidence_calibrated': False, 'request_focus': None, 'authority': {'decision': 'common', 'reason': 'published_target_owned', 'record_ids': ['migrated_faq_rule_booking_max_sessions'], 'release_id': 'EVAL_DRAFT_ONLY', 'epoch': 584}, 'field_authority': [], 'unresolved_clauses': ['can one booking include'], 'semantic_review_needed': True, 'sem … [ย่อจาก2,026ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 153. common / failures / test_semantic_cases (tests.test_integrated_improvement_r21_20261001.IntegratedImprovementTests.test_semantic_cases) (case='tuesday-afternoon')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_integrated_improvement_r21_20261001.py", line 59, in test_semantic_cases
    self.assertTrue(row['passed'], row)
AssertionError: False is not true : {'id': 'tuesday-afternoon', 'locale': 'en', 'question': 'What are the afteronon opening hours on Tuesday', 'expected_route': 'schedule', 'required_groups': (('Tuesday',), ('13:00-16:00',)), 'forbidden': ('09:00-12:00',), 'expected_live_fetch': False, 'live_fetches': 0, 'route': 'knowledge', 'mode': 'pipeline:common_clarification', 'answer': 'The requested topic is unclear. Which part of [Thai source] เปิดถึงกี่โมง do you need: question / answer / topic?', 'elapsed_sec': 0.08034180011600256, 'passed': False, 'failures': ['route knowledge != schedule', "missing group ('Tuesday',)", "missing group ('13:00-16:00',)"], 'trace': [{'stage': 'common_content', 'decision': 'clarification', 'confidence': 0.0, 'detail': 'typed fields and source-backed joins; uncalibrated confidence', 'metadata': {'response_type': 'clarification', 'release_id': 'EVAL_DRAFT_ONLY', 'query_plan': {'record_ids': ['migrated_faq_rule_service_schedule'], 'requested_fields': [], 'all_fields': False, 'method': 'exact', 'scope': 'common_published', 'platform': None, 'query_without_entity': 'what are the afteronon on tuesday', 'field_selection': [], 'confidence_calibrated': False, 'request_focus': None, 'authority': {'decision': 'common', 'reason': 'published_target_owned', 'record_ids': ['migrated_faq_rule_service_schedule'], 'release_id': 'EVAL_DRAFT_ONLY', 'epoch': 584}, 'field_authority': [], 'unresolved_clauses': ['what are the afteronon on tuesday'], 'semantic_review_needed': True, 'semant … [ย่อจาก2,023ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 154. common / failures / test_semantic_cases (tests.test_integrated_improvement_r21_20261001.IntegratedImprovementTests.test_semantic_cases) (case='offer-ood')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_integrated_improvement_r21_20261001.py", line 59, in test_semantic_cases
    self.assertTrue(row['passed'], row)
AssertionError: False is not true : {'id': 'offer-ood', 'locale': 'en', 'question': 'Do you offer vernight accommodation? Please use verified information', 'expected_route': 'no_answer', 'required_groups': (('could not find verified',),), 'forbidden': ('Verified equipment', 'Gaming Monitor'), 'expected_live_fetch': False, 'live_fetches': 0, 'route': 'knowledge', 'mode': 'pipeline:common_clarification', 'answer': 'The requested topic is unclear. Which part of [Thai source] อาวุธ do you need: question / answer / topic?', 'elapsed_sec': 17.77977340016514, 'passed': False, 'failures': ['route knowledge != no_answer', "missing group ('could not find verified',)"], 'trace': [{'stage': 'common_content', 'decision': 'clarification', 'confidence': 0.0, 'detail': 'typed fields and source-backed joins; uncalibrated confidence', 'metadata': {'response_type': 'clarification', 'release_id': 'EVAL_DRAFT_ONLY', 'query_plan': {'record_ids': ['migrated_faq_rule_weapons_gambling'], 'requested_fields': [], 'all_fields': False, 'method': 'bounded_fuzzy', 'scope': 'common_published', 'platform': None, 'query_without_entity': 'do you offer vernight accommodation? please use verified information', 'field_selection': [], 'confidence_calibrated': False, 'request_focus': None, 'authority': {'decision': 'common', 'reason': 'published_target_owned', 'record_ids': ['migrated_faq_rule_weapons_gambling'], 'release_id': 'EVAL_DRAFT_ONLY', 'epoch': 584}, 'field_authority': [], 'unresolved_clauses': ['do you offer vernight a … [ย่อจาก2,111ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 155. common / failures / test_semantic_cases (tests.test_integrated_improvement_r21_20261001.IntegratedImprovementTests.test_semantic_cases) (case='member-two-tasks')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_integrated_improvement_r21_20261001.py", line 59, in test_semantic_cases
    self.assertTrue(row['passed'], row)
AssertionError: False is not true : {'id': 'member-two-tasks', 'locale': 'en', 'question': 'How many memberss are there, and who is the president', 'expected_route': 'multi_question', 'required_groups': (('25',), ('university',), ('club',)), 'forbidden': (), 'expected_live_fetch': False, 'live_fetches': 0, 'route': 'no_answer', 'mode': 'pipeline:request_timeout_no_answer', 'answer': 'This request reached the processing time limit, so it was stopped to keep the service responsive.\nPlease try a more specific question, such as naming the zone, game, or topic directly.', 'elapsed_sec': 20.3183, 'passed': False, 'failures': ['route no_answer != multi_question', "missing group ('25',)", "missing group ('university',)", "missing group ('club',)"], 'trace': [{'stage': 'timing', 'decision': 'locale_resolution', 'confidence': 1.0, 'detail': '', 'metadata': {'elapsed_ms': 0.1, 'elapsed_sec': 0.0001, 'global_timeout_enabled': True, 'global_timeout_sec': 20.0, 'global_elapsed_sec': 0.0002, 'global_remaining_sec': 19.9998, 'finalizer_reserve_sec': 1.0, 'work_remaining_sec': 18.9998, 'timing_status': 'running'}}, {'stage': 'timing', 'decision': 'intent_cue_preflight', 'confidence': 1.0, 'detail': '', 'metadata': {'elapsed_ms': 55.93, 'elapsed_sec': 0.0559, 'global_timeout_enabled': True, 'global_timeout_sec': 20.0, 'global_elapsed_sec': 20.2457, 'global_remaining_sec': 0.0, 'finalizer_reserve_sec': 1.0, 'work_remaining_sec': 0.0, 'timing_status': 'running'}}, {'stage': 'timing', 'decision': 'canonical_pr … [ย่อจาก5,099ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 156. common / failures / test_semantic_cases (tests.test_integrated_improvement_r21_20261001.IntegratedImprovementTests.test_semantic_cases) (case='person-operation')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_integrated_improvement_r21_20261001.py", line 59, in test_semantic_cases
    self.assertTrue(row['passed'], row)
AssertionError: False is not true : {'id': 'person-operation', 'locale': 'th', 'question': 'นางาาวกมลวรรณ นวลสาย ทำำแหน่งอะไร', 'expected_route': 'overview', 'required_groups': (('กมลวรรณ',), ('กรรมการ',)), 'forbidden': (), 'expected_live_fetch': False, 'live_fetches': 0, 'route': 'knowledge', 'mode': 'pipeline:common_clarification', 'answer': 'ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ นางสาวกมลวรรณ นวลสาย เช่น ชื่อที่อนุญาตให้เผยแพร่ / ตำแหน่ง/หน้าที่ / รายละเอียดที่เผยแพร่ได้ ไม่ใส่ข้อมูลลูกค้าหรือสลิป?', 'elapsed_sec': 4.501621600007638, 'passed': False, 'failures': ['route knowledge != overview', "missing group ('กรรมการ',)"], 'trace': [{'stage': 'common_content', 'decision': 'clarification', 'confidence': 0.0, 'detail': 'typed fields and source-backed joins; uncalibrated confidence', 'metadata': {'response_type': 'clarification', 'release_id': 'EVAL_DRAFT_ONLY', 'query_plan': {'record_ids': ['member_18a751d710b9b30c'], 'requested_fields': [], 'all_fields': False, 'method': 'bounded_fuzzy', 'scope': 'common_published', 'platform': None, 'query_without_entity': 'นางาาวกมลวรรณ นวลสาย ทำำแหน่งอะไร', 'field_selection': [], 'confidence_calibrated': False, 'request_focus': None, 'authority': {'decision': 'common', 'reason': 'published_target_owned', 'record_ids': ['member_18a751d710b9b30c'], 'release_id': 'EVAL_DRAFT_ONLY', 'epoch': 584}, 'field_authority': [], 'unresolved_clauses': ['นางาาวกมลวรรณ นวลสาย ทำำแหน่งอะไร'], 'semantic_review_needed': True, 'semantic_plan_accepted': False}, 'ob … [ย่อจาก1,993ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 157. common / failures / test_semantic_cases (tests.test_integrated_improvement_r21_20261001.IntegratedImprovementTests.test_semantic_cases) (case='compound-price-unclear-action')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_integrated_improvement_r21_20261001.py", line 59, in test_semantic_cases
    self.assertTrue(row['passed'], row)
AssertionError: False is not true : {'id': 'compound-price-unclear-action', 'locale': 'th', 'question': 'PC 2 ชั่วโมง บุคคลทั่วไป ราคาเท่าไหร่ แล้วของยังไง', 'expected_route': 'multi_question', 'required_groups': (('140 บาท',), ('จอง',), ('หมายถึง',)), 'forbidden': (), 'expected_live_fetch': False, 'live_fetches': 0, 'route': 'knowledge', 'mode': 'pipeline:common_clarification', 'answer': 'ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ วิธีจอง เช่น คำถามตั้งต้น ไม่จำเป็นต้องเก็บทุก paraphrase / คำตอบพร้อมหลักฐานของศูนย์ / หัวข้อเชิงความหมาย?', 'elapsed_sec': 10.060664700111374, 'passed': False, 'failures': ['route knowledge != multi_question', "missing group ('140 บาท',)", "missing group ('หมายถึง',)"], 'trace': [{'stage': 'common_content', 'decision': 'clarification', 'confidence': 0.0, 'detail': 'typed fields and source-backed joins; uncalibrated confidence', 'metadata': {'response_type': 'clarification', 'release_id': 'EVAL_DRAFT_ONLY', 'query_plan': {'record_ids': ['migrated_faq_rule_booking_steps'], 'requested_fields': [], 'all_fields': False, 'method': 'bounded_fuzzy', 'scope': 'common_published', 'platform': None, 'query_without_entity': 'pc 2 ชั่วโมง บุคคลทั่วไป ราคาเท่าไหร่ แล้วของยังไง', 'field_selection': [], 'confidence_calibrated': False, 'request_focus': None, 'authority': {'decision': 'common', 'reason': 'published_target_owned', 'record_ids': ['migrated_faq_rule_booking_steps'], 'release_id': 'EVAL_DRAFT_ONLY', 'epoch': 584}, 'field_authority': [], 'unresolved_clauses': ['pc 2 … [ย่อจาก2,111ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 158. common / failures / test_semantic_cases (tests.test_integrated_improvement_r21_20261001.IntegratedImprovementTests.test_semantic_cases) (case='unknown-minimum-age')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_integrated_improvement_r21_20261001.py", line 59, in test_semantic_cases
    self.assertTrue(row['passed'], row)
AssertionError: False is not true : {'id': 'unknown-minimum-age', 'locale': 'en', 'question': 'What is the minimum sge requrement to enter the VALORANT competition', 'expected_route': 'competition_rules', 'required_groups': (('could not find a verified',),), 'forbidden': ('18 years', '16 years'), 'expected_live_fetch': False, 'live_fetches': 0, 'route': 'knowledge', 'mode': 'pipeline:common_clarification', 'answer': 'The requested topic is unclear. Which part of [Thai source] PSU Phuket VALORANT 2026 Tournament do you need: event name / rulebook release / coverage?', 'elapsed_sec': 0.15171809983439744, 'passed': False, 'failures': ['route knowledge != competition_rules', "missing group ('could not find a verified',)"], 'trace': [{'stage': 'common_content', 'decision': 'clarification', 'confidence': 0.0, 'detail': 'typed fields and source-backed joins; uncalibrated confidence', 'metadata': {'response_type': 'clarification', 'release_id': 'EVAL_DRAFT_ONLY', 'query_plan': {'record_ids': ['competition_competition_rules_valorant_psu_phuket_2026'], 'requested_fields': [], 'all_fields': False, 'method': 'exact', 'scope': 'common_published', 'platform': None, 'query_without_entity': 'what is the minimum sge requrement to enter the competition', 'field_selection': [], 'confidence_calibrated': False, 'request_focus': None, 'authority': {'decision': 'common', 'reason': 'published_target_owned', 'record_ids': ['competition_competition_rules_valorant_psu_phuket_2026'], 'release_id': 'EVAL_DRAFT_ONLY', ' … [ย่อจาก2,186ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 159. common / failures / test_semantic_cases (tests.test_integrated_improvement_r21_20261001.IntegratedImprovementTests.test_semantic_cases) (case='team-size-two-typos')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_integrated_improvement_r21_20261001.py", line 59, in test_semantic_cases
    self.assertTrue(row['passed'], row)
AssertionError: False is not true : {'id': 'team-size-two-typos', 'locale': 'en', 'question': 'Counter-Strike 2 rule teaam size', 'expected_route': 'competition_rules', 'required_groups': (('5',), ('players',)), 'forbidden': (), 'expected_live_fetch': False, 'live_fetches': 0, 'route': 'knowledge', 'mode': 'pipeline:common_clarification', 'answer': 'The requested topic is unclear. Which part of [Thai source] Counter-Strike 2 do you need: event name / rulebook release / coverage / platform?', 'elapsed_sec': 0.12431790004484355, 'passed': False, 'failures': ['route knowledge != competition_rules', "missing group ('5',)", "missing group ('players',)"], 'trace': [{'stage': 'common_content', 'decision': 'clarification', 'confidence': 0.0, 'detail': 'typed fields and source-backed joins; uncalibrated confidence', 'metadata': {'response_type': 'clarification', 'release_id': 'EVAL_DRAFT_ONLY', 'query_plan': {'record_ids': ['game_detail_cs2', 'competition_competition_rules_cs2_psu_phuket_2026', 'controls_pc_counter_strike_2', 'availability_pc_01_02', 'availability_pc_03_10'], 'requested_fields': [], 'all_fields': False, 'method': 'exact', 'scope': 'common_published', 'platform': None, 'query_without_entity': 'rule teaam size', 'field_selection': [], 'confidence_calibrated': False, 'request_focus': None, 'authority': {'decision': 'common', 'reason': 'published_target_owned', 'record_ids': ['game_detail_cs2', 'competition_competition_rules_cs2_psu_phuket_2026', 'controls_pc_counter_strike_2', 'availab … [ย่อจาก2,219ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 160. common / failures / test_semantic_cases (tests.test_integrated_improvement_r21_20261001.IntegratedImprovementTests.test_semantic_cases) (case='ambiguous-procedure')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_integrated_improvement_r21_20261001.py", line 59, in test_semantic_cases
    self.assertTrue(row['passed'], row)
AssertionError: False is not true : {'id': 'ambiguous-procedure', 'locale': 'en', 'question': 'What do the CS2 tornament rules say about in-march procedure', 'expected_route': 'competition_rules', 'required_groups': (('Which competition procedure',), ('before',), ('during',), ('after',)), 'forbidden': ('Step-by-step competition procedure',), 'expected_live_fetch': False, 'live_fetches': 0, 'route': 'knowledge', 'mode': 'pipeline:common_answer', 'answer': '**[Thai source] ภาพรวมเอกสาร**\n• text: [Thai source] กฎระเบียบและรูปแบบการแข่งขัน Counter-Strike 2 [S1]\n• heading: [Thai source] ภาพรวมเอกสาร [S2]\n• section number: 1 [S3]\n• completeness: Not yet confirmed\n\n**[Thai source] 6. ข้อจำกัด**\n• text: [Thai source] 6. ข้อจำกัด [S4]\n• heading: [Thai source] 6. ข้อจำกัด [S5]\n• section number: 10 [S6]\n• completeness: Not yet confirmed\n\n**[Thai source] 1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน**\n• text: [Thai source] 1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน [S7]\n• heading: [Thai source] 1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน [S8]\n• section number: 11 [S9]\n• completeness: Not yet confirmed\n\n**[Thai source] 2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร**\n• text: [Thai source] 2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร [S10]\n• heading: [Thai source] 2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร [S11]\n• section number: 12 [S12]\n• completeness: Not yet confirmed\n\n**[Thai source] 3. หากสมาชิกคนใดถอนตัว ทีมอา … [ย่อจาก70,830ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 161. common / failures / test_semantic_cases (tests.test_integrated_improvement_r21_20261001.IntegratedImprovementTests.test_semantic_cases) (case='pay-play-clarification')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_integrated_improvement_r21_20261001.py", line 59, in test_semantic_cases
    self.assertTrue(row['passed'], row)
AssertionError: False is not true : {'id': 'pay-play-clarification', 'locale': 'en', 'question': 'How to pay Ring Fit Adventure', 'expected_route': 'clarification', 'required_groups': (('playing', 'play'), ('service fee', 'pay')), 'forbidden': (), 'expected_live_fetch': False, 'live_fetches': 0, 'route': 'knowledge', 'mode': 'pipeline:common_clarification', 'answer': 'The requested topic is unclear. Which part of [Thai source] Ring Fit Adventure do you need: platform / input device / preset / bindings?', 'elapsed_sec': 0.182078099809587, 'passed': False, 'failures': ['route knowledge != clarification', "missing group ('playing', 'play')", "missing group ('service fee', 'pay')"], 'trace': [{'stage': 'common_content', 'decision': 'clarification', 'confidence': 0.0, 'detail': 'typed fields and source-backed joins; uncalibrated confidence', 'metadata': {'response_type': 'clarification', 'release_id': 'EVAL_DRAFT_ONLY', 'query_plan': {'record_ids': ['game_detail_ring_fit_adventure', 'availability_nintendo_1_2', 'availability_nintendo_1_4', 'controls_nintendo_ring_fit_adventure'], 'requested_fields': [], 'all_fields': False, 'method': 'exact', 'scope': 'common_published', 'platform': None, 'query_without_entity': 'how to pay', 'field_selection': [], 'confidence_calibrated': False, 'request_focus': None, 'authority': {'decision': 'common', 'reason': 'published_target_owned', 'record_ids': ['game_detail_ring_fit_adventure', 'availability_nintendo_1_2', 'availability_nintendo_1_4', 'controls_nintend … [ย่อจาก2,195ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 162. common / failures / test_semantic_cases (tests.test_integrated_improvement_r21_20261001.IntegratedImprovementTests.test_semantic_cases) (case='technical-pause-comparison')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_integrated_improvement_r21_20261001.py", line 59, in test_semantic_cases
    self.assertTrue(row['passed'], row)
AssertionError: False is not true : {'id': 'technical-pause-comparison', 'locale': 'en', 'question': 'How do CS2 and VALORANT technical pause rules differ?', 'expected_route': 'competition_rules', 'required_groups': (('Counter-Strike 2',), ('VALORANT',), ('two times',), ('10 minutes',), ('disconnection',), ('not communicate', 'may not communicate')), 'forbidden': ('Tactical Timeout', '60 seconds'), 'expected_live_fetch': False, 'live_fetches': 0, 'route': 'knowledge', 'mode': 'pipeline:common_partial_answer', 'answer': '**[Thai source] ภาพรวมเอกสาร**\n• text: [Thai source] กฎระเบียบและรูปแบบการแข่งขัน VALORANT\nรายการ PSU Phuket VALORANT 2026 Tournament\nUpdate: 17/02/2026\nEnglish below\nอุปกรณ์และอุปกรณ์ต่อพ่วง\nในการแข่งขันแบบ LAN ผู้เล่นต้องปฏิบัติตามข้อกำหนดเรื่องอุปกรณ์อย่างเคร่งครัดเพื่อความเท่าเทียม\n* อุปกรณ์ที่นำมาเองได้ คีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย)\n* อุปกรณ์ที่ผู้จัดจัดเตรียมให้ ผู้จัดจะจัดเตรียม PC, จอภาพ, หูฟังพร้อมไมโครโฟน, โต๊ะ และเก้าอี้ให้\n* เทคโนโลยีคีย์บอร์ด อนุญาตให้ใช้ Snap Tap, SOCD หรือเทคโนโลยีที่เทียบเท่าได้ เว้นแต่เจ้าหน้าที่จะสั่งเป็นอย่างอื่น\n* ข้อห้ามสำคัญ\n* ห้ามใช้มาโคร (Macros) ทั้งที่ตั้งค่าผ่านซอฟต์แวร์หรือฮาร์ดแวร์\n* ห้ามติดตั้งโปรแกรมเองบนคอมพิวเตอร์ที่จัดไว้ให้\n* ห้ามเข้าโซเชียลมีเดียหรือเว็บไซต์สื่อสารใด ๆ บนคอมพิวเตอร์แข่งขันนอกจากโปรแกรมที่ทางผู้จัดจัดเตรียมไว้ให้ [S1]\n• heading: [Thai source] ภาพรวมเอกสาร [S2]\n• section number: 1 [S3]\n• comp … [ย่อจาก41,531ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 163. common / failures / test_semantic_cases (tests.test_integrated_improvement_r21_20261001.IntegratedImprovementTests.test_semantic_cases) (case='tactical-pause')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_integrated_improvement_r21_20261001.py", line 59, in test_semantic_cases
    self.assertTrue(row['passed'], row)
AssertionError: False is not true : {'id': 'tactical-pause', 'locale': 'en', 'question': 'VALORANT tactical timeout rules', 'expected_route': 'competition_rules', 'required_groups': (('2',), ('60 seconds',), ('Overtime',)), 'forbidden': ('hardware malfunction',), 'expected_live_fetch': False, 'live_fetches': 0, 'route': 'knowledge', 'mode': 'pipeline:common_answer', 'answer': '**[Thai source] ภาพรวมเอกสาร**\n• text: [Thai source] กฎระเบียบและรูปแบบการแข่งขัน VALORANT\nรายการ PSU Phuket VALORANT 2026 Tournament\nUpdate: 17/02/2026\nEnglish below\nอุปกรณ์และอุปกรณ์ต่อพ่วง\nในการแข่งขันแบบ LAN ผู้เล่นต้องปฏิบัติตามข้อกำหนดเรื่องอุปกรณ์อย่างเคร่งครัดเพื่อความเท่าเทียม\n* อุปกรณ์ที่นำมาเองได้ คีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย)\n* อุปกรณ์ที่ผู้จัดจัดเตรียมให้ ผู้จัดจะจัดเตรียม PC, จอภาพ, หูฟังพร้อมไมโครโฟน, โต๊ะ และเก้าอี้ให้\n* เทคโนโลยีคีย์บอร์ด อนุญาตให้ใช้ Snap Tap, SOCD หรือเทคโนโลยีที่เทียบเท่าได้ เว้นแต่เจ้าหน้าที่จะสั่งเป็นอย่างอื่น\n* ข้อห้ามสำคัญ\n* ห้ามใช้มาโคร (Macros) ทั้งที่ตั้งค่าผ่านซอฟต์แวร์หรือฮาร์ดแวร์\n* ห้ามติดตั้งโปรแกรมเองบนคอมพิวเตอร์ที่จัดไว้ให้\n* ห้ามเข้าโซเชียลมีเดียหรือเว็บไซต์สื่อสารใด ๆ บนคอมพิวเตอร์แข่งขันนอกจากโปรแกรมที่ทางผู้จัดจัดเตรียมไว้ให้ [S1]\n• heading: [Thai source] ภาพรวมเอกสาร [S2]\n• section number: 1 [S3]\n• completeness: Not yet confirmed\n\n**[Thai source] ประเภทบทลงโทษในเกม**\n• text: [Thai source] ประเภทบทลงโทษในเกม [S4]\n• heading: [Thai source] ประเภ … [ย่อจาก41,082ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 164. common / failures / test_semantic_cases (tests.test_integrated_improvement_r21_20261001.IntegratedImprovementTests.test_semantic_cases) (case='emergency-pause')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_integrated_improvement_r21_20261001.py", line 59, in test_semantic_cases
    self.assertTrue(row['passed'], row)
AssertionError: False is not true : {'id': 'emergency-pause', 'locale': 'en', 'question': 'VALORANT emergency pause rules', 'expected_route': 'competition_rules', 'required_groups': (('1',), ('10 minutes',), ('substitute',)), 'forbidden': ('60 seconds',), 'expected_live_fetch': False, 'live_fetches': 0, 'route': 'knowledge', 'mode': 'pipeline:common_answer', 'answer': '**[Thai source] ภาพรวมเอกสาร**\n• text: [Thai source] กฎระเบียบและรูปแบบการแข่งขัน VALORANT\nรายการ PSU Phuket VALORANT 2026 Tournament\nUpdate: 17/02/2026\nEnglish below\nอุปกรณ์และอุปกรณ์ต่อพ่วง\nในการแข่งขันแบบ LAN ผู้เล่นต้องปฏิบัติตามข้อกำหนดเรื่องอุปกรณ์อย่างเคร่งครัดเพื่อความเท่าเทียม\n* อุปกรณ์ที่นำมาเองได้ คีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย)\n* อุปกรณ์ที่ผู้จัดจัดเตรียมให้ ผู้จัดจะจัดเตรียม PC, จอภาพ, หูฟังพร้อมไมโครโฟน, โต๊ะ และเก้าอี้ให้\n* เทคโนโลยีคีย์บอร์ด อนุญาตให้ใช้ Snap Tap, SOCD หรือเทคโนโลยีที่เทียบเท่าได้ เว้นแต่เจ้าหน้าที่จะสั่งเป็นอย่างอื่น\n* ข้อห้ามสำคัญ\n* ห้ามใช้มาโคร (Macros) ทั้งที่ตั้งค่าผ่านซอฟต์แวร์หรือฮาร์ดแวร์\n* ห้ามติดตั้งโปรแกรมเองบนคอมพิวเตอร์ที่จัดไว้ให้\n* ห้ามเข้าโซเชียลมีเดียหรือเว็บไซต์สื่อสารใด ๆ บนคอมพิวเตอร์แข่งขันนอกจากโปรแกรมที่ทางผู้จัดจัดเตรียมไว้ให้ [S1]\n• heading: [Thai source] ภาพรวมเอกสาร [S2]\n• section number: 1 [S3]\n• completeness: Not yet confirmed\n\n**[Thai source] ประเภทบทลงโทษในเกม**\n• text: [Thai source] ประเภทบทลงโทษในเกม [S4]\n• heading: [Thai source] ประเภทบทลงโทษ … [ย่อจาก41,062ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 165. common / failures / test_real_word_collision_asks_instead_of_rewriting (tests.test_intent_cue_recovery_20260930.IntentCueRecoveryTests.test_real_word_collision_asks_instead_of_rewriting)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_cue_recovery_20260930.py", line 80, in test_real_word_collision_asks_instead_of_rewriting
    self.assertEqual("clarification", result.route.category)
AssertionError: 'clarification' != 'knowledge'
- clarification
+ knowledge


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 166. common / failures / test_routes_match_requested_operations (tests.test_intent_cue_recovery_20260930.IntentCueRecoveryTests.test_routes_match_requested_operations)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_cue_recovery_20260930.py", line 65, in test_routes_match_requested_operations
    self.assertEqual("service_fee", answer("PUBG: BATTLEGROUNDS ราคเท่าไฟร่", "th").route.category)
AssertionError: 'service_fee' != 'knowledge'
- service_fee
+ knowledge


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 167. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-TH-0303')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-28']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-28'

- []
+ ['2026-09-28'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 168. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-TH-0304')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-28']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-28'

- []
+ ['2026-09-28'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 169. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-TH-0305')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-28']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-28'

- []
+ ['2026-09-28'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 170. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-TH-0308')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-29']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-29'

- []
+ ['2026-09-29'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 171. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-TH-0310')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-29']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-29'

- []
+ ['2026-09-29'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 172. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-TH-0313')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-30']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-30'

- []
+ ['2026-09-30'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 173. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-TH-0318')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-10-01']

Second list contains 1 additional elements.
First extra element 0:
'2026-10-01'

- []
+ ['2026-10-01'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 174. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-TH-0320')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-10-01']

Second list contains 1 additional elements.
First extra element 0:
'2026-10-01'

- []
+ ['2026-10-01'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 175. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-TH-0321')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-25']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-25'

- []
+ ['2026-09-25'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 176. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-TH-0323')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-25']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-25'

- []
+ ['2026-09-25'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 177. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-TH-0324')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-25']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-25'

- []
+ ['2026-09-25'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 178. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-TH-0325')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-25']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-25'

- []
+ ['2026-09-25'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 179. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-TH-0328')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-28']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-28'

- []
+ ['2026-09-28'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 180. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-TH-0329')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-28']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-28'

- []
+ ['2026-09-28'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 181. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-TH-0333')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-29']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-29'

- []
+ ['2026-09-29'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 182. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-TH-0334')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-29']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-29'

- []
+ ['2026-09-29'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 183. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-TH-0335')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-29']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-29'

- []
+ ['2026-09-29'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 184. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-TH-0338')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-30']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-30'

- []
+ ['2026-09-30'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 185. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-TH-0339')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-30']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-30'

- []
+ ['2026-09-30'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 186. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-TH-0340')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-30']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-30'

- []
+ ['2026-09-30'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 187. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-TH-0343')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-10-01']

Second list contains 1 additional elements.
First extra element 0:
'2026-10-01'

- []
+ ['2026-10-01'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 188. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-TH-0348')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-25']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-25'

- []
+ ['2026-09-25'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 189. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-TH-0349')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-25']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-25'

- []
+ ['2026-09-25'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 190. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-EN-0302')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-28']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-28'

- []
+ ['2026-09-28'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 191. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-EN-0303')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-28']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-28'

- []
+ ['2026-09-28'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 192. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-EN-0304')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-28']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-28'

- []
+ ['2026-09-28'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 193. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-EN-0305')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-28']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-28'

- []
+ ['2026-09-28'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 194. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-EN-0312')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-30']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-30'

- []
+ ['2026-09-30'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 195. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-EN-0313')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-30']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-30'

- []
+ ['2026-09-30'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 196. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-EN-0315')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-30']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-30'

- []
+ ['2026-09-30'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 197. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-EN-0320')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-10-01']

Second list contains 1 additional elements.
First extra element 0:
'2026-10-01'

- []
+ ['2026-10-01'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 198. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-EN-0322')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-25']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-25'

- []
+ ['2026-09-25'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 199. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-EN-0323')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-25']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-25'

- []
+ ['2026-09-25'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 200. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-EN-0325')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-25']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-25'

- []
+ ['2026-09-25'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 201. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-EN-0327')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-28']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-28'

- []
+ ['2026-09-28'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 202. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-EN-0328')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-28']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-28'

- []
+ ['2026-09-28'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 203. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-EN-0330')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-28']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-28'

- []
+ ['2026-09-28'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 204. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-EN-0331')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-29']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-29'

- []
+ ['2026-09-29'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 205. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-EN-0332')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-29']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-29'

- []
+ ['2026-09-29'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 206. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-EN-0333')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-29']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-29'

- []
+ ['2026-09-29'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 207. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-EN-0335')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-29']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-29'

- []
+ ['2026-09-29'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 208. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-EN-0337')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-30']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-30'

- []
+ ['2026-09-30'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 209. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-EN-0338')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-30']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-30'

- []
+ ['2026-09-30'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 210. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-EN-0339')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-30']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-30'

- []
+ ['2026-09-30'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 211. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-EN-0340')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-30']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-30'

- []
+ ['2026-09-30'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 212. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-EN-0343')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-10-01']

Second list contains 1 additional elements.
First extra element 0:
'2026-10-01'

- []
+ ['2026-10-01'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 213. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-EN-0345')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-10-01']

Second list contains 1 additional elements.
First extra element 0:
'2026-10-01'

- []
+ ['2026-10-01'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 214. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-EN-0347')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-25']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-25'

- []
+ ['2026-09-25'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 215. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-EN-0348')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-25']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-25'

- []
+ ['2026-09-25'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 216. common / failures / test_all_weekday_live_questions_request_the_expected_dashboard_date (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_all_weekday_live_questions_request_the_expected_dashboard_date) (case='INTENT-TRAP-EN-0350')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 187, in test_all_weekday_live_questions_request_the_expected_dashboard_date
    self.assertEqual(requested_dates, [case["expected_target"]], result.mode)
AssertionError: Lists differ: [] != ['2026-09-25']

Second list contains 1 additional elements.
First extra element 0:
'2026-09-25'

- []
+ ['2026-09-25'] : pipeline:request_timeout_no_answer

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 217. common / failures / test_damage_is_not_a_game_catalog (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_damage_is_not_a_game_catalog) (question='Who pays when a user damages a gaming chair?')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 60, in test_damage_is_not_a_game_catalog
    self.assertEqual(result.route.category, "penalty")
AssertionError: 'knowledge' != 'penalty'
- knowledge
+ penalty


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 218. common / failures / test_damage_is_not_a_game_catalog (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_damage_is_not_a_game_catalog) (question='Must a player pay repair costs for damaging the VR headset?')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 60, in test_damage_is_not_a_game_catalog
    self.assertEqual(result.route.category, "penalty")
AssertionError: 'no_answer' != 'penalty'
- no_answer
+ penalty


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 219. common / failures / test_existing_penalty_facts_survive_polite_wrappers (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_existing_penalty_facts_survive_polite_wrappers) (question='What is the studio policy for damage responsibility')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 275, in test_existing_penalty_facts_survive_polite_wrappers
    self.assertEqual(result.route.category, "penalty")
AssertionError: 'knowledge' != 'penalty'
- knowledge
+ penalty


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 220. common / failures / test_existing_penalty_facts_survive_polite_wrappers (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_existing_penalty_facts_survive_polite_wrappers) (question='Could you please help me with this: What is the studio policy for severe damage')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 275, in test_existing_penalty_facts_survive_polite_wrappers
    self.assertEqual(result.route.category, "penalty")
AssertionError: 'knowledge' != 'penalty'
- knowledge
+ penalty


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 221. common / failures / test_existing_penalty_facts_survive_polite_wrappers (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_existing_penalty_facts_survive_polite_wrappers) (question='ขอข้อมูลเรื่องระงับสิทธิ์ชั่วคราว ช่วยแนบแหล่งข้อมูลด้วย')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 275, in test_existing_penalty_facts_survive_polite_wrappers
    self.assertEqual(result.route.category, "penalty")
AssertionError: 'knowledge' != 'penalty'
- knowledge
+ penalty


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 222. common / failures / test_food_bringing_and_consumption_answer_distinct_facets (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_food_bringing_and_consumption_answer_distinct_facets)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 83, in test_food_bringing_and_consumption_answer_distinct_facets
    self.assertEqual(result.route.category, "rules")
AssertionError: 'knowledge' != 'rules'
- knowledge
+ rules


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 223. common / failures / test_payment_checkin_damage_and_duration_use_verified_facts (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_payment_checkin_damage_and_duration_use_verified_facts) (question='ขอข้อมูลเรื่องชำระเงินหลัง booking ขอรายละเอียดแบบสั้น ๆ')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 394, in test_payment_checkin_damage_and_duration_use_verified_facts
    self.assertEqual(result.route.category, category)
AssertionError: 'knowledge' != 'reservation'
- knowledge
+ reservation


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 224. common / failures / test_preface_does_not_split_inside_thai_word (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_preface_does_not_split_inside_thai_word)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 38, in test_preface_does_not_split_inside_thai_word
    self.assertEqual(result.route.category, "clarification")
AssertionError: 'knowledge' != 'clarification'
- knowledge
+ clarification


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 225. common / failures / test_ps5_controller_model_is_not_a_game_button_question (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_ps5_controller_model_is_not_a_game_button_question)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 71, in test_ps5_controller_model_is_not_a_game_button_question
    self.assertEqual(game_buttons.route.category, "games")
AssertionError: 'knowledge' != 'games'
- knowledge
+ games


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 226. common / failures / test_public_access_is_not_equipment_inventory (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_public_access_is_not_equipment_inventory)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 76, in test_public_access_is_not_equipment_inventory
    self.assertEqual(result.route.category, "reservation")
AssertionError: 'knowledge' != 'reservation'
- knowledge
+ reservation


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 227. common / failures / test_public_access_language_variants_do_not_become_catalogs (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_public_access_language_variants_do_not_become_catalogs) (question='Does a public visitor need membership before entering?')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 319, in test_public_access_language_variants_do_not_become_catalogs
    self.assertEqual(result.route.category, "reservation")
AssertionError: 'no_answer' != 'reservation'
- no_answer
+ reservation


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 228. common / failures / test_public_access_language_variants_do_not_become_catalogs (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_public_access_language_variants_do_not_become_catalogs) (question='Can a non-student access the Cockpit?')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 319, in test_public_access_language_variants_do_not_become_catalogs
    self.assertEqual(result.route.category, "reservation")
AssertionError: 'no_answer' != 'reservation'
- no_answer
+ reservation


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 229. common / failures / test_public_access_language_variants_do_not_become_catalogs (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_public_access_language_variants_do_not_become_catalogs) (question='คนที่ไม่ใช่นักศึกษา PSU เข้าไปเล่นได้หรือเปล่า')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 319, in test_public_access_language_variants_do_not_become_catalogs
    self.assertEqual(result.route.category, "reservation")
AssertionError: 'no_answer' != 'reservation'
- no_answer
+ reservation


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 230. common / failures / test_public_access_language_variants_do_not_become_catalogs (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_public_access_language_variants_do_not_become_catalogs) (question='คนที่ไม่ได้เรียนที่นี่เข้าใช้ Cockpit ได้หรือไม่')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 319, in test_public_access_language_variants_do_not_become_catalogs
    self.assertEqual(result.route.category, "reservation")
AssertionError: 'no_answer' != 'reservation'
- no_answer
+ reservation


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 231. common / failures / test_public_access_language_variants_do_not_become_catalogs (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_public_access_language_variants_do_not_become_catalogs) (question='Are the PCs for public visitors or students only?')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 319, in test_public_access_language_variants_do_not_become_catalogs
    self.assertEqual(result.route.category, "reservation")
AssertionError: 'no_answer' != 'reservation'
- no_answer
+ reservation


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 232. common / failures / test_public_access_questions_use_the_requested_facet (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_public_access_questions_use_the_requested_facet) (question='What ID does an external visitor need to use the studio?')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 333, in test_public_access_questions_use_the_requested_facet
    self.assertEqual(result.route.category, "reservation")
AssertionError: 'no_answer' != 'reservation'
- no_answer
+ reservation


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 233. common / failures / test_public_access_questions_use_the_requested_facet (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_public_access_questions_use_the_requested_facet) (question='Does a public visitor need membership before entering?')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 333, in test_public_access_questions_use_the_requested_facet
    self.assertEqual(result.route.category, "reservation")
AssertionError: 'no_answer' != 'reservation'
- no_answer
+ reservation


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 234. common / failures / test_specific_policy_facets_beat_generic_public_access (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_specific_policy_facets_beat_generic_public_access) (question='Does a non-PSU guest need a membership or national ID?')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 353, in test_specific_policy_facets_beat_generic_public_access
    self.assertEqual(result.route.category, category)
AssertionError: 'no_answer' != 'reservation'
- no_answer
+ reservation


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 235. common / failures / test_specific_policy_facets_beat_generic_public_access (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_specific_policy_facets_beat_generic_public_access) (question='Are nonstudents allowed to use the studio or only PSU students?')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 353, in test_specific_policy_facets_beat_generic_public_access
    self.assertEqual(result.route.category, category)
AssertionError: 'no_answer' != 'reservation'
- no_answer
+ reservation


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 236. common / failures / test_specific_policy_facets_beat_generic_public_access (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_specific_policy_facets_beat_generic_public_access) (question='Can a non-PSU user charge their phone in the studio?')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 353, in test_specific_policy_facets_beat_generic_public_access
    self.assertEqual(result.route.category, category)
AssertionError: 'knowledge' != 'rules'
- knowledge
+ rules


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 237. common / failures / test_studio_rules_do_not_become_game_catalog_or_clarification (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_studio_rules_do_not_become_game_catalog_or_clarification) (question='What is the studio policy for return equipment games')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 409, in test_studio_rules_do_not_become_game_catalog_or_clarification
    self.assertEqual(result.route.category, "rules")
AssertionError: 'knowledge' != 'rules'
- knowledge
+ rules


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 238. common / failures / test_studio_rules_do_not_become_game_catalog_or_clarification (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_studio_rules_do_not_become_game_catalog_or_clarification) (question='ขอข้อมูลเรื่องทรัพย์สินส่วนตัว สูญหาย')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 409, in test_studio_rules_do_not_become_game_catalog_or_clarification
    self.assertEqual(result.route.category, "rules")
AssertionError: 'knowledge' != 'rules'
- knowledge
+ rules


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 239. common / failures / test_studio_rules_do_not_become_game_catalog_or_clarification (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_studio_rules_do_not_become_game_catalog_or_clarification) (question='ขอข้อมูลเรื่องคำพูดไม่เหมาะสม')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 409, in test_studio_rules_do_not_become_game_catalog_or_clarification
    self.assertEqual(result.route.category, "rules")
AssertionError: 'knowledge' != 'rules'
- knowledge
+ rules


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 240. common / failures / test_studio_rules_do_not_become_game_catalog_or_clarification (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_studio_rules_do_not_become_game_catalog_or_clarification) (question='ของหายแล้วทำอุปกรณ์เสียหายด้วย ต้องทำยังไง')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 409, in test_studio_rules_do_not_become_game_catalog_or_clarification
    self.assertEqual(result.route.category, "rules")
AssertionError: 'knowledge' != 'rules'
- knowledge
+ rules


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 241. common / failures / test_unspecified_english_pay_questions_ask_for_service (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_unspecified_english_pay_questions_ask_for_service) (question='I do not study at PSU; what would I pay to use the studio?')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 263, in test_unspecified_english_pay_questions_ask_for_service
    self.assertEqual(result.route.category, "clarification")
AssertionError: 'no_answer' != 'clarification'
- no_answer
+ clarification


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 242. common / failures / test_unspecified_english_pay_questions_ask_for_service (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_unspecified_english_pay_questions_ask_for_service) (question='What would I pay to use a station if I have not chosen a zone?')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 263, in test_unspecified_english_pay_questions_ask_for_service
    self.assertEqual(result.route.category, "clarification")
AssertionError: 'no_answer' != 'clarification'
- no_answer
+ clarification


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 243. common / failures / test_weekly_booking_does_not_call_live_dashboard (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_weekly_booking_does_not_call_live_dashboard)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 110, in test_weekly_booking_does_not_call_live_dashboard
    self.assertEqual(result.route.category, "schedule")
AssertionError: 'no_answer' != 'schedule'
- no_answer
+ schedule


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 244. common / failures / test_wrapped_unrelated_question_does_not_become_studio_overview (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_wrapped_unrelated_question_does_not_become_studio_overview)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 286, in test_wrapped_unrelated_question_does_not_become_studio_overview
    self.assertEqual(result.route.category, "no_answer")
AssertionError: 'knowledge' != 'no_answer'
- knowledge
+ no_answer


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 245. common / failures / test_failing_examples_reach_the_expected_answer_paths (tests.test_keyboard_neighbor_recovery_20260929.KeyboardNeighborRecoveryTests.test_failing_examples_reach_the_expected_answer_paths)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_keyboard_neighbor_recovery_20260929.py", line 68, in test_failing_examples_reach_the_expected_answer_paths
    self.assertEqual(booking.route.intent, "booking_policy")
AssertionError: 'common_read' != 'booking_policy'
- common_read
+ booking_policy


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 246. common / failures / test_api_unavailable_never_claims_vacancy (tests.test_live_booking_typo_fixture_20260930.LiveBookingTypoFixtureTests.test_api_unavailable_never_claims_vacancy)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_live_booking_typo_fixture_20260930.py", line 69, in test_api_unavailable_never_claims_vacancy
    self.assertIn("ยังยืนยันสถานะ", result.answer)
AssertionError: 'ยังยืนยันสถานะ' not found in 'ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ Cockpit Zone เช่น ชื่อบริการตามหน้า WordPress / แพลตฟอร์ม เช่น PC หรือ PS5 / เวลาเล่น (นาที) / เวลาที่ล็อกเครื่อง (นาที)?'

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 247. common / failures / test_english_answer_uses_same_snapshot (tests.test_live_booking_typo_fixture_20260930.LiveBookingTypoFixtureTests.test_english_answer_uses_same_snapshot)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_live_booking_typo_fixture_20260930.py", line 60, in test_english_answer_uses_same_snapshot
    self.assertEqual("schedule", result.route.category)
AssertionError: 'schedule' != 'knowledge'
- schedule
+ knowledge


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 248. common / failures / test_thai_typo_uses_known_slot_truth (tests.test_live_booking_typo_fixture_20260930.LiveBookingTypoFixtureTests.test_thai_typo_uses_known_slot_truth)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_live_booking_typo_fixture_20260930.py", line 52, in test_thai_typo_uses_known_slot_truth
    self.assertEqual("schedule", result.route.category)
AssertionError: 'schedule' != 'knowledge'
- schedule
+ knowledge


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 249. common / failures / test_ambiguous_english_references_request_clarification (tests.test_master_ground_truth_route_regressions.MasterGroundTruthRouteRegressionTests.test_ambiguous_english_references_request_clarification) (question='Where can I play it')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_master_ground_truth_route_regressions.py", line 107, in test_ambiguous_english_references_request_clarification
    self.assertEqual("clarification", result.route.category)
AssertionError: 'clarification' != 'knowledge'
- clarification
+ knowledge


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 250. common / failures / test_booking_facets_are_not_flattened_to_generic_steps (tests.test_master_ground_truth_route_regressions.MasterGroundTruthRouteRegressionTests.test_booking_facets_are_not_flattened_to_generic_steps) (question='What is the studio policy for late check in?')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_master_ground_truth_route_regressions.py", line 73, in test_booking_facets_are_not_flattened_to_generic_steps
    self.assertEqual(category, result.route.category)
AssertionError: 'reservation' != 'knowledge'
- reservation
+ knowledge


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 251. common / failures / test_booking_facets_are_not_flattened_to_generic_steps (tests.test_master_ground_truth_route_regressions.MasterGroundTruthRouteRegressionTests.test_booking_facets_are_not_flattened_to_generic_steps) (question='How many sessions can one booking include?')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_master_ground_truth_route_regressions.py", line 73, in test_booking_facets_are_not_flattened_to_generic_steps
    self.assertEqual(category, result.route.category)
AssertionError: 'reservation' != 'knowledge'
- reservation
+ knowledge


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 252. common / failures / test_compound_keeps_verified_target_and_booking_step (tests.test_master_ground_truth_route_regressions.MasterGroundTruthRouteRegressionTests.test_compound_keeps_verified_target_and_booking_step)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_master_ground_truth_route_regressions.py", line 138, in test_compound_keeps_verified_target_and_booking_step
    self.assertEqual("multi_question", controls.route.category)
AssertionError: 'multi_question' != 'knowledge'
- multi_question
+ knowledge


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 253. common / failures / test_english_booking_wrappers_do_not_block_verified_intent (tests.test_master_ground_truth_route_regressions.MasterGroundTruthRouteRegressionTests.test_english_booking_wrappers_do_not_block_verified_intent)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_master_ground_truth_route_regressions.py", line 96, in test_english_booking_wrappers_do_not_block_verified_intent
    self.assertEqual("reservation", booking.route.category)
AssertionError: 'reservation' != 'no_answer'
- reservation
+ no_answer


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 254. common / failures / test_english_calendar_keeps_schedule_when_holiday_name_is_thai (tests.test_master_ground_truth_route_regressions.MasterGroundTruthRouteRegressionTests.test_english_calendar_keeps_schedule_when_holiday_name_is_thai)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_master_ground_truth_route_regressions.py", line 212, in test_english_calendar_keeps_schedule_when_holiday_name_is_thai
    self.assertEqual("schedule", closures.route.category)
AssertionError: 'schedule' != 'no_answer'
- schedule
+ no_answer


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 255. common / failures / test_explicit_negative_rule_beats_broad_member_or_equipment_signal (tests.test_master_ground_truth_route_regressions.MasterGroundTruthRouteRegressionTests.test_explicit_negative_rule_beats_broad_member_or_equipment_signal)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_master_ground_truth_route_regressions.py", line 88, in test_explicit_negative_rule_beats_broad_member_or_equipment_signal
    self.assertIn("annual membership", membership.answer.casefold())
AssertionError: 'annual membership' not found in 'this request reached the processing time limit, so it was stopped to keep the service responsive.\nplease try a more specific question, such as naming the zone, game, or topic directly.'

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 256. common / failures / test_game_location_and_capacity_use_static_records (tests.test_master_ground_truth_route_regressions.MasterGroundTruthRouteRegressionTests.test_game_location_and_capacity_use_static_records)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_master_ground_truth_route_regressions.py", line 111, in test_game_location_and_capacity_use_static_records
    self.assertEqual("games", location.route.category)
AssertionError: 'games' != 'knowledge'
- games
+ knowledge


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 257. common / failures / test_missing_english_game_detail_names_target (tests.test_master_ground_truth_route_regressions.MasterGroundTruthRouteRegressionTests.test_missing_english_game_detail_names_target)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_master_ground_truth_route_regressions.py", line 180, in test_missing_english_game_detail_names_target
    self.assertEqual("games", result.route.category)
AssertionError: 'games' != 'knowledge'
- games
+ knowledge


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 258. common / failures / test_official_thai_member_identifiers_in_english_questions (tests.test_master_ground_truth_route_regressions.MasterGroundTruthRouteRegressionTests.test_official_thai_member_identifiers_in_english_questions)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_master_ground_truth_route_regressions.py", line 151, in test_official_thai_member_identifiers_in_english_questions
    self.assertEqual("overview", by_name.route.category)
AssertionError: 'overview' != 'knowledge'
- overview
+ knowledge


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 259. common / failures / test_pc_game_question_uses_machine_catalog_not_game_translation (tests.test_master_ground_truth_route_regressions.MasterGroundTruthRouteRegressionTests.test_pc_game_question_uses_machine_catalog_not_game_translation)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_master_ground_truth_route_regressions.py", line 190, in test_pc_game_question_uses_machine_catalog_not_game_translation
    self.assertEqual("games", absent.route.category)
AssertionError: 'games' != 'knowledge'
- games
+ knowledge


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 260. common / failures / test_static_game_catalog_and_duration_do_not_use_live_booking (tests.test_master_ground_truth_route_regressions.MasterGroundTruthRouteRegressionTests.test_static_game_catalog_and_duration_do_not_use_live_booking)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_master_ground_truth_route_regressions.py", line 78, in test_static_game_catalog_and_duration_do_not_use_live_booking
    self.assertEqual("games", catalog.route.category)
AssertionError: 'games' != 'knowledge'
- games
+ knowledge


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 261. common / failures / test_unknown_game_variants_do_not_expand_to_catalog (tests.test_master_ground_truth_route_regressions.MasterGroundTruthRouteRegressionTests.test_unknown_game_variants_do_not_expand_to_catalog) (question='Is Valorant Mobile available')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_master_ground_truth_route_regressions.py", line 122, in test_unknown_game_variants_do_not_expand_to_catalog
    self.assertIn(result.route.category, {"games", "no_answer"})
AssertionError: 'knowledge' not found in {'no_answer', 'games'}

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 262. common / failures / test_verified_equipment_availability_does_not_enter_game_retrieval (tests.test_master_ground_truth_route_regressions.MasterGroundTruthRouteRegressionTests.test_verified_equipment_availability_does_not_enter_game_retrieval)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_master_ground_truth_route_regressions.py", line 242, in test_verified_equipment_availability_does_not_enter_game_retrieval
    self.assertEqual("equipment", result.route.category)
AssertionError: 'equipment' != 'knowledge'
- equipment
+ knowledge


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 263. common / failures / test_phrase_recovery_keeps_resource_and_duration (tests.test_multi_error_typo_recovery_20260929.MultiErrorTypoRecoveryTests.test_phrase_recovery_keeps_resource_and_duration) (question='PS5 ราาคาเท่าไหน่')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_multi_error_typo_recovery_20260929.py", line 58, in test_phrase_recovery_keeps_resource_and_duration
    self.assertEqual(_answer(question).route.intent, intent)
AssertionError: 'conversation_price_lookup' != 'service_fee_query'
- conversation_price_lookup
+ service_fee_query


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 264. common / failures / test_planner_accepts_only_relevant_schema_fields (tests.test_common_content_r58.CommonTests.test_planner_accepts_only_relevant_schema_fields)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_common_content_r58.py", line 175, in test_planner_accepts_only_relevant_schema_fields
    for p in ({'requested_fields':['amount_minor'],'all_fields':False,'platform':None},{'requested_fields':['bindings'],'all_fields':False,'platform':'PS4'},{'requested_fields':['bindings'],'all_fields':'true','platform':None}):self.assertIsNone(checked_plan(p,ids,records))
                                                                                                                                                                                                                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: {'requested_fields': ['amount_minor'], 'all_fields': False, 'platform': None, 'method': 'bounded_llm_schema_fields'} is not None

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 265. common / failures / test_competition_rule_with_price_word_remains_competition (tests.test_p1_verified_answer_paths_20260928.VerifiedAnswerPathTests.test_competition_rule_with_price_word_remains_competition)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_p1_verified_answer_paths_20260928.py", line 65, in test_competition_rule_with_price_word_remains_competition
    self.assertEqual(result.route.category, "competition_rules")
AssertionError: 'knowledge' != 'competition_rules'
- knowledge
+ competition_rules


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 266. common / failures / test_contact_email_with_thai_spelling (tests.test_p1_verified_answer_paths_20260928.VerifiedAnswerPathTests.test_contact_email_with_thai_spelling)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_p1_verified_answer_paths_20260928.py", line 22, in test_contact_email_with_thai_spelling
    self.assertEqual(result.route.category, "contact")
AssertionError: 'knowledge' != 'contact'
- knowledge
+ contact


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 267. common / failures / test_named_headset_definition_is_item_detail (tests.test_p1_verified_answer_paths_20260928.VerifiedAnswerPathTests.test_named_headset_definition_is_item_detail)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_p1_verified_answer_paths_20260928.py", line 53, in test_named_headset_definition_is_item_detail
    self.assertEqual(result.route.category, "equipment")
AssertionError: 'knowledge' != 'equipment'
- knowledge
+ equipment


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 268. common / failures / test_undated_holiday_opening_request_asks_for_date (tests.test_p1_verified_answer_paths_20260928.VerifiedAnswerPathTests.test_undated_holiday_opening_request_asks_for_date)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_p1_verified_answer_paths_20260928.py", line 32, in test_undated_holiday_opening_request_asks_for_date
    self.assertIn("วันที่เท่าไร", result.answer)
AssertionError: 'วันที่เท่าไร' not found in '**วันหยุดราชการ**\nข้อมูลรุ่นนี้หรือรายการที่อ้างอิงยังไม่ถึงวันมีผลหรือหมดอายุแล้ว จึงยังยืนยันข้อมูลปัจจุบันไม่ได้\n\n**วันหยุดราชการ**\nข้อมูลรุ่นนี้หรือรายการที่อ้างอิงยังไม่ถึงวันมีผลหรือหมดอายุแล้ว จึงยังยืนยันข้อมูลปัจจุบันไม่ได้\n\n**วันหยุดราชการ**\nข้อมูลรุ่นนี้หรือรายการที่อ้างอิงยังไม่ถึงวันมีผลหรือหมดอายุแล้ว จึงยังยืนยันข้อมูลปัจจุบันไม่ได้\n\nstate: หัวข้อนี้อยู่นอกขอบเขตรายการที่เลือก กรุณาระบุบริการหรือรายการที่เกี่ยวข้อง'

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 269. common / failures / test_verified_tekken_price_question_is_service_fee (tests.test_p1_verified_answer_paths_20260928.VerifiedAnswerPathTests.test_verified_tekken_price_question_is_service_fee)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_p1_verified_answer_paths_20260928.py", line 59, in test_verified_tekken_price_question_is_service_fee
    self.assertEqual(result.route.category, "service_fee")
AssertionError: 'knowledge' != 'service_fee'
- knowledge
+ service_fee


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 270. common / failures / test_zone_equipment_request_remains_catalog (tests.test_p1_verified_answer_paths_20260928.VerifiedAnswerPathTests.test_zone_equipment_request_remains_catalog)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_p1_verified_answer_paths_20260928.py", line 69, in test_zone_equipment_request_remains_catalog
    self.assertEqual(result.route.category, "equipment")
AssertionError: 'knowledge' != 'equipment'
- knowledge
+ equipment


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 271. common / failures / test_unknown_button_returns_no_mapping (tests.test_r30_closed_query_boundaries.R30BoundaryTests.test_unknown_button_returns_no_mapping) (q='ปุ่ม R9 ใน Gran Turismo 7 ใช้ทำอะไร')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_r30_closed_query_boundaries.py", line 33, in test_unknown_button_returns_no_mapping
    self.assertIn('no_answer',r.mode);self.assertNotIn('Accelerate',r.answer);self.assertNotIn('•    R2:',r.answer)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 'no_answer' not found in 'pipeline:common_answer'

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 272. common / failures / test_unknown_button_returns_no_mapping (tests.test_r30_closed_query_boundaries.R30BoundaryTests.test_unknown_button_returns_no_mapping) (q='What does the R9 button do in Gran Turismo 7?')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_r30_closed_query_boundaries.py", line 33, in test_unknown_button_returns_no_mapping
    self.assertIn('no_answer',r.mode);self.assertNotIn('Accelerate',r.answer);self.assertNotIn('•    R2:',r.answer)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 'no_answer' not found in 'pipeline:common_clarification'

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 273. common / failures / test_canonical_flag_does_not_swallow_recovered_compound (tests.test_reliability_flow_20261001.ReliabilityFlowTests.test_canonical_flag_does_not_swallow_recovered_compound) (question='PS5 ราคาเท่าไหร่ แล้วมีเกมอะไรบ้าง')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_reliability_flow_20261001.py", line 109, in test_canonical_flag_does_not_swallow_recovered_compound
    self.assertEqual("multi_question", result.route.category)
AssertionError: 'multi_question' != 'knowledge'
- multi_question
+ knowledge


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 274. common / failures / test_canonical_flag_does_not_swallow_recovered_compound (tests.test_reliability_flow_20261001.ReliabilityFlowTests.test_canonical_flag_does_not_swallow_recovered_compound) (question='PS5 ราคาเท่าไหร่ อล้วมีเกมอะไรบ้าง')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_reliability_flow_20261001.py", line 109, in test_canonical_flag_does_not_swallow_recovered_compound
    self.assertEqual("multi_question", result.route.category)
AssertionError: 'multi_question' != 'knowledge'
- multi_question
+ knowledge


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 275. common / failures / test_source_supported_focused_cases (tests.test_reliability_flow_20261001.ReliabilityFlowTests.test_source_supported_focused_cases) (id='equipment-en-delete')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_reliability_flow_20261001.py", line 132, in test_source_supported_focused_cases
    self.assertTrue(result["passed"], result["failures"])
AssertionError: False is not true : ['route knowledge != equipment']

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 276. common / failures / test_source_supported_focused_cases (tests.test_reliability_flow_20261001.ReliabilityFlowTests.test_source_supported_focused_cases) (id='equipment-en-swap')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_reliability_flow_20261001.py", line 132, in test_source_supported_focused_cases
    self.assertTrue(result["passed"], result["failures"])
AssertionError: False is not true : ['route knowledge != equipment', "missing group ('Gaming Monitor',)"]

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 277. common / failures / test_source_supported_focused_cases (tests.test_reliability_flow_20261001.ReliabilityFlowTests.test_source_supported_focused_cases) (id='payment-multi')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_reliability_flow_20261001.py", line 132, in test_source_supported_focused_cases
    self.assertTrue(result["passed"], result["failures"])
AssertionError: False is not true : ['route no_answer != multi_question', "missing group ('10 minutes',)", "missing group ('Student ID',)", "missing group ('phone number',)"]

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 278. common / failures / test_source_supported_focused_cases (tests.test_reliability_flow_20261001.ReliabilityFlowTests.test_source_supported_focused_cases) (id='alcohol-negative')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_reliability_flow_20261001.py", line 132, in test_source_supported_focused_cases
    self.assertTrue(result["passed"], result["failures"])
AssertionError: False is not true : ['route knowledge != rules', "missing group ('prohibited',)"]

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 279. common / failures / test_source_supported_focused_cases (tests.test_reliability_flow_20261001.ReliabilityFlowTests.test_source_supported_focused_cases) (id='game-zone-typo')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_reliability_flow_20261001.py", line 132, in test_source_supported_focused_cases
    self.assertTrue(result["passed"], result["failures"])
AssertionError: False is not true : ['route knowledge != games', "missing group ('PlayStation 5 Zone',)"]

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 280. common / failures / test_source_supported_focused_cases (tests.test_reliability_flow_20261001.ReliabilityFlowTests.test_source_supported_focused_cases) (id='compound-th-connector')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_reliability_flow_20261001.py", line 132, in test_source_supported_focused_cases
    self.assertTrue(result["passed"], result["failures"])
AssertionError: False is not true : ['route knowledge != multi_question', "missing group ('บาท',)", "missing group ('สลิป',)"]

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 281. common / failures / test_source_supported_focused_cases (tests.test_reliability_flow_20261001.ReliabilityFlowTests.test_source_supported_focused_cases) (id='compound-th-tight')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_reliability_flow_20261001.py", line 132, in test_source_supported_focused_cases
    self.assertTrue(result["passed"], result["failures"])
AssertionError: False is not true : ['route knowledge != multi_question', "missing group ('บาท',)", "missing group ('FINAL FANTASY XVI',)", "validation: ('missing_requested_field:amount_minor',)"]

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 282. common / failures / test_source_supported_focused_cases (tests.test_reliability_flow_20261001.ReliabilityFlowTests.test_source_supported_focused_cases) (id='compound-th-three')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_reliability_flow_20261001.py", line 132, in test_source_supported_focused_cases
    self.assertTrue(result["passed"], result["failures"])
AssertionError: False is not true : ['route knowledge != multi_question', "missing group ('บาท',)", "missing group ('FINAL FANTASY XVI',)", "missing group ('สลิป',)"]

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 283. common / failures / test_source_supported_focused_cases (tests.test_reliability_flow_20261001.ReliabilityFlowTests.test_source_supported_focused_cases) (id='r19-sofa')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_reliability_flow_20261001.py", line 132, in test_source_supported_focused_cases
    self.assertTrue(result["passed"], result["failures"])
AssertionError: False is not true : ['route knowledge != equipment']

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 284. common / failures / test_source_supported_focused_cases (tests.test_reliability_flow_20261001.ReliabilityFlowTests.test_source_supported_focused_cases) (id='posttest-conjunction')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_reliability_flow_20261001.py", line 132, in test_source_supported_focused_cases
    self.assertTrue(result["passed"], result["failures"])
AssertionError: False is not true : ['route knowledge != multi_question', "missing group ('payment slip',)", "missing group ('Monday',)"]

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 285. common / failures / test_generic_opening_questions_include_every_day_and_lunch (tests.test_schedule_completeness_r43.ScheduleCompletenessR43Tests.test_generic_opening_questions_include_every_day_and_lunch) (q='What are the studio opening hours?')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_schedule_completeness_r43.py", line 18, in test_generic_opening_questions_include_every_day_and_lunch
    self.assertIn(name+':',r.answer)
AssertionError: 'Monday:' not found in 'The requested topic is unclear. Which part of [Thai source] เปิดถึงกี่โมง do you need: question / answer / topic?'

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 286. common / failures / test_generic_opening_questions_include_every_day_and_lunch (tests.test_schedule_completeness_r43.ScheduleCompletenessR43Tests.test_generic_opening_questions_include_every_day_and_lunch) (q='Opening timetable please')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_schedule_completeness_r43.py", line 18, in test_generic_opening_questions_include_every_day_and_lunch
    self.assertIn(name+':',r.answer)
AssertionError: 'Monday:' not found in '**Service schedule**\n• Opening periods: Conflicting sources; needs a decision\n• timezone: Not yet confirmed\n• weekday: 0 [S1]\n• Applicable zones: Not yet confirmed\n\n**Service schedule**\n• Opening periods: Conflicting sources; needs a decision\n• timezone: Not yet confirmed\n• weekday: 1 [S2]\n• Applicable zones: Not yet confirmed\n\n**Service schedule**\n• Opening periods: Conflicting sources; needs a decision\n• timezone: Not yet confirmed\n• weekday: 2 [S3]\n• Applicable zones: Not yet confirmed\n\n**Service schedule**\n• Opening periods: Conflicting sources; needs a decision\n• timezone: Not yet confirmed\n• weekday: 3 [S4]\n• Applicable zones: Not yet confirmed\n\n**Service schedule**\n• Opening periods: Conflicting sources; needs a decision\n• timezone: Not yet confirmed\n• weekday: 4 [S5]\n• Applicable zones: Not yet confirmed\n\n**Service schedule**\n• Opening periods: No entries in this field (confirmed) [S6]\n• timezone: Not yet confirmed\n• weekday: 5 [S7]\n• Applicable zones: Not yet confirmed\n\n**Service schedule**\n• Opening periods: No entries in this field (confirmed) [S8]\n• timezone: Not yet confirmed\n• weekday: 6 [S9]\n• Applicable zones: Not yet confirmed'

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 287. common / failures / test_generic_opening_questions_include_every_day_and_lunch (tests.test_schedule_completeness_r43.ScheduleCompletenessR43Tests.test_generic_opening_questions_include_every_day_and_lunch) (q='What is the service schedule?')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_schedule_completeness_r43.py", line 18, in test_generic_opening_questions_include_every_day_and_lunch
    self.assertIn(name+':',r.answer)
AssertionError: 'Monday:' not found in 'The requested topic is unclear. Which part of Service schedule do you need: timezone / weekday / Opening periods / Bookable periods?'

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 288. common / failures / test_generic_opening_questions_include_every_day_and_lunch (tests.test_schedule_completeness_r43.ScheduleCompletenessR43Tests.test_generic_opening_questions_include_every_day_and_lunch) (q='Please list opening hours for every day.')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_schedule_completeness_r43.py", line 18, in test_generic_opening_questions_include_every_day_and_lunch
    self.assertIn(name+':',r.answer)
AssertionError: 'Monday:' not found in 'The requested topic is unclear. Which part of [Thai source] เปิดถึงกี่โมง do you need: question / answer / topic?'

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 289. common / failures / test_generic_opening_questions_include_every_day_and_lunch (tests.test_schedule_completeness_r43.ScheduleCompletenessR43Tests.test_generic_opening_questions_include_every_day_and_lunch) (q='Show service hours for all days')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_schedule_completeness_r43.py", line 18, in test_generic_opening_questions_include_every_day_and_lunch
    self.assertIn(name+':',r.answer)
AssertionError: 'Monday:' not found in 'The requested topic is unclear. Which part of [Thai source] เปิดถึงกี่โมง do you need: question / answer / topic?'

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 290. common / failures / test_engine_routes_translation_before_quoted_booking_policy (tests.test_semantic_quality_r53.SemanticQualityTests.test_engine_routes_translation_before_quoted_booking_policy)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_semantic_quality_r53.py", line 55, in test_engine_routes_translation_before_quoted_booking_policy
    self.assertEqual(result.route.category,'general')
AssertionError: 'no_answer' != 'general'
- no_answer
+ general


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 291. common / failures / test_explicit_sofa_target_survives_incidental_display_in_preamble (tests.test_target_integrity_step1_20260930.TargetIntegrityStepOneTests.test_explicit_sofa_target_survives_incidental_display_in_preamble) (question='ขอสอบถามหน่อยครับ Sofa 2 seats คืออุปกรณ์อะไร')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_target_integrity_step1_20260930.py", line 26, in test_explicit_sofa_target_survives_incidental_display_in_preamble
    self.assertEqual("equipment", result.route.category)
AssertionError: 'equipment' != 'knowledge'
- equipment
+ knowledge


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 292. common / failures / test_explicit_sofa_target_survives_incidental_display_in_preamble (tests.test_target_integrity_step1_20260930.TargetIntegrityStepOneTests.test_explicit_sofa_target_survives_incidental_display_in_preamble) (question='จอสอบถามหน่อยครับ Sofa 2 seats คืออุปกรณ์อะไร')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_target_integrity_step1_20260930.py", line 26, in test_explicit_sofa_target_survives_incidental_display_in_preamble
    self.assertEqual("equipment", result.route.category)
AssertionError: 'equipment' != 'knowledge'
- equipment
+ knowledge


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 293. common / failures / test_explicit_sofa_target_survives_incidental_display_in_preamble (tests.test_target_integrity_step1_20260930.TargetIntegrityStepOneTests.test_explicit_sofa_target_survives_incidental_display_in_preamble) (question='จอสอบถาม Sofa 2 seats อยู่โซนไหน')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_target_integrity_step1_20260930.py", line 26, in test_explicit_sofa_target_survives_incidental_display_in_preamble
    self.assertEqual("equipment", result.route.category)
AssertionError: 'equipment' != 'knowledge'
- equipment
+ knowledge


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 294. common / failures / test_explicit_sofa_target_survives_incidental_display_in_preamble (tests.test_target_integrity_step1_20260930.TargetIntegrityStepOneTests.test_explicit_sofa_target_survives_incidental_display_in_preamble) (question='Sofa 2 seats คืออะไร')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_target_integrity_step1_20260930.py", line 26, in test_explicit_sofa_target_survives_incidental_display_in_preamble
    self.assertEqual("equipment", result.route.category)
AssertionError: 'equipment' != 'knowledge'
- equipment
+ knowledge


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 295. common / failures / test_real_display_and_gpu_questions_still_select_the_requested_component (tests.test_target_integrity_step1_20260930.TargetIntegrityStepOneTests.test_real_display_and_gpu_questions_still_select_the_requested_component) (question='Nintendo Switch ใช้ทีวีกี่นิ้ว')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_target_integrity_step1_20260930.py", line 38, in test_real_display_and_gpu_questions_still_select_the_requested_component
    self.assertIn(required, result.answer)
AssertionError: 'TV 86' not found in 'ขออภัยครับ คำถามนี้ใช้เวลาประมวลผลเกินเวลาที่กำหนด เลยหยุดไว้ก่อนเพื่อไม่ให้ระบบค้าง\nลองถามใหม่ให้เฉพาะเจาะจงขึ้น เช่น ระบุโซน เกม หรือเรื่องที่ต้องการถามโดยตรงครับ'

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 296. common / failures / test_booking_navigation_is_not_game_controls (tests.test_targeted_dialogue_r40.TargetedDialogueR40Tests.test_booking_navigation_is_not_game_controls)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_targeted_dialogue_r40.py", line 47, in test_booking_navigation_is_not_game_controls
    self.assertEqual(r.mode, 'pipeline:booking_navigation')
AssertionError: 'pipeline:common_answer' != 'pipeline:booking_navigation'
- pipeline:common_answer
+ pipeline:booking_navigation


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 297. common / failures / test_booking_shortcut_does_not_swallow_second_price_operation (tests.test_targeted_dialogue_r40.TargetedDialogueR40Tests.test_booking_shortcut_does_not_swallow_second_price_operation)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_targeted_dialogue_r40.py", line 150, in test_booking_shortcut_does_not_swallow_second_price_operation
    self.assertEqual(result.mode, 'pipeline:multi_question_splitter')
AssertionError: 'pipeline:request_timeout_no_answer' != 'pipeline:multi_question_splitter'
- pipeline:request_timeout_no_answer
+ pipeline:multi_question_splitter


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 298. common / failures / test_compound_price_and_controls_preserve_both_orders_and_languages (tests.test_targeted_dialogue_r40.TargetedDialogueR40Tests.test_compound_price_and_controls_preserve_both_orders_and_languages)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_targeted_dialogue_r40.py", line 166, in test_compound_price_and_controls_preserve_both_orders_and_languages
    self.assertEqual(result.mode, 'pipeline:multi_question_splitter')
AssertionError: 'pipeline:common_partial_answer' != 'pipeline:multi_question_splitter'
- pipeline:common_partial_answer
+ pipeline:multi_question_splitter


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 299. common / failures / test_excess_selections_clarify_without_executing_partial_scope (tests.test_targeted_dialogue_r40.TargetedDialogueR40Tests.test_excess_selections_clarify_without_executing_partial_scope)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_targeted_dialogue_r40.py", line 138, in test_excess_selections_clarify_without_executing_partial_scope
    self.assertEqual(result.mode, 'pipeline:dialogue_selection_clarification')
AssertionError: 'pipeline:common_clarification' != 'pipeline:dialogue_selection_clarification'
- pipeline:common_clarification
?           ^^^
+ pipeline:dialogue_selection_clarification
?          +++++++++++++ ^^


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 300. common / failures / test_guard_also_runs_for_each_compound_child (tests.test_targeted_dialogue_r40.TargetedDialogueR40Tests.test_guard_also_runs_for_each_compound_child)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_targeted_dialogue_r40.py", line 96, in test_guard_also_runs_for_each_compound_child
    self.assertIn('VALORANT controls:', result.answer)
AssertionError: 'VALORANT controls:' not found in '**VALORANT**\n• bindings: Not yet confirmed\n• platform: PC [S1]\n• input device: Not yet confirmed\n• preset: Not yet confirmed'

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 301. common / failures / test_missing_controls_fast_path_is_bilingual_and_does_not_call_model (tests.test_targeted_dialogue_r40.TargetedDialogueR40Tests.test_missing_controls_fast_path_is_bilingual_and_does_not_call_model) (q='List all game buttons')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_targeted_dialogue_r40.py", line 30, in test_missing_controls_fast_path_is_bilingual_and_does_not_call_model
    self.assertIn('game_control_missing_game_context', r.mode)
AssertionError: 'game_control_missing_game_context' not found in 'pipeline:common_answer'

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 302. common / failures / test_multiple_catalog_targets_do_not_drop_second_zone (tests.test_targeted_dialogue_r40.TargetedDialogueR40Tests.test_multiple_catalog_targets_do_not_drop_second_zone)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_targeted_dialogue_r40.py", line 70, in test_multiple_catalog_targets_do_not_drop_second_zone
    self.assertIn('PC Zone', result.answer)
AssertionError: 'PC Zone' not found in "Published records in the common catalog: 48\n• [Thai source] Animal Crossing: New Horizons\n• [Thai source] Beat Saber\n• [Thai source] Call of Duty: Modern Warfare III\n• [Thai source] Counter-Strike 2\n• [Thai source] EA Sports FC 24\n• [Thai source] FINAL FANTASY XVI\n• [Thai source] Fortnite\n• [Thai source] God of War Ragnarok\n• [Thai source] Gran Turismo 7\n• [Thai source] Hogwarts Legacy\n• [Thai source] Horizon Call of the Mountain\n• [Thai source] It Takes Two\n• [Thai source] League of Legends\n• [Thai source] Little Nightmares II\n• [Thai source] Luigi's Mansion 3\n• [Thai source] Mario Kart 8 Deluxe\n• [Thai source] Mario Party Superstars\n• [Thai source] Monster Hunter Rise\n• [Thai source] Moving Out 2\n• [Thai source] NARUTO X BORUTO Ultimate Ninja Storm Connections\n• [Thai source] New Super Mario Bros. U Deluxe\n• [Thai source] Overcooked 2\n• [Thai source] PUBG: BATTLEGROUNDS\n• [Thai source] Resident Evil 4\n• [Thai source] Resident Evil Village\n• [Thai source] Ring Fit Adventure\n• [Thai source] Marvel's Spider-Man 2\n• [Thai source] Super Mario Odyssey\n• [Thai source] Super Smash Bros Ultimate\n• [Thai source] Nintendo Switch Sports\n• [Thai source] TEKKEN 8\n• [Thai source] The Last of Us Part I / Part II\n• [Thai source] Uncharted: Legacy of Thieves Collection\n• [Thai source] VALORANT\n• [Thai source] Call of Duty: Warzone\n• [Thai source] The Legend of Zelda: Breath of the Wild\n• Arena of Valor (RoV … [ย่อจาก2,055ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 303. common / failures / test_multiple_controls_keep_operation_order_and_deduplicate (tests.test_targeted_dialogue_r40.TargetedDialogueR40Tests.test_multiple_controls_keep_operation_order_and_deduplicate)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_targeted_dialogue_r40.py", line 59, in test_multiple_controls_keep_operation_order_and_deduplicate
    self.assertEqual(result.mode, 'pipeline:multi_question_splitter')
AssertionError: 'pipeline:common_answer' != 'pipeline:multi_question_splitter'
- pipeline:common_answer
+ pipeline:multi_question_splitter


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 304. common / failures / test_demonstrative_game_needs_a_target_without_context (tests.test_thai_noisy_input_flow_20260929.ThaiNoisyInputFlowTests.test_demonstrative_game_needs_a_target_without_context)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_thai_noisy_input_flow_20260929.py", line 74, in test_demonstrative_game_needs_a_target_without_context
    self.assertEqual(named.route.category, "games")
AssertionError: 'knowledge' != 'games'
- knowledge
+ games


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 305. common / failures / test_explicit_remastered_title_is_not_part_one (tests.test_thai_noisy_input_flow_20260929.ThaiNoisyInputFlowTests.test_explicit_remastered_title_is_not_part_one)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_thai_noisy_input_flow_20260929.py", line 67, in test_explicit_remastered_title_is_not_part_one
    self.assertIn("PlayStation 5", answer.answer)
AssertionError: 'PlayStation 5' not found in 'ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ The Last of Us Part II (Remastered) เช่น ชื่อเกมอย่างเป็นทางการ / ชื่อบริการตามหน้า WordPress / แพลตฟอร์ม เช่น PC หรือ PS5 / เวลาเล่น (นาที)?'

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 306. common / failures / test_nintendo_service_capacity_survives_game_title_correction (tests.test_thai_noisy_input_flow_20260929.ThaiNoisyInputFlowTests.test_nintendo_service_capacity_survives_game_title_correction) (label='1-2')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_thai_noisy_input_flow_20260929.py", line 82, in test_nintendo_service_capacity_survives_game_title_correction
    self.assertIn(capacity, result.answer)
AssertionError: '1-2 คน' not found in '**Nintendo Switch (1-2 Persons)**\n• จำนวนคนสูงสุดของบริการ: 2 [S1]\n\nroom_seats: หัวข้อนี้อยู่นอกขอบเขตรายการที่เลือก กรุณาระบุบริการหรือรายการที่เกี่ยวข้อง\n\ncapacity_persons: หัวข้อนี้อยู่นอกขอบเขตรายการที่เลือก กรุณาระบุบริการหรือรายการที่เกี่ยวข้อง'

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 307. common / failures / test_nintendo_service_capacity_survives_game_title_correction (tests.test_thai_noisy_input_flow_20260929.ThaiNoisyInputFlowTests.test_nintendo_service_capacity_survives_game_title_correction) (label='1-4')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_thai_noisy_input_flow_20260929.py", line 82, in test_nintendo_service_capacity_survives_game_title_correction
    self.assertIn(capacity, result.answer)
AssertionError: '1-4 คน' not found in '**Nintendo Switch (1-4 Persons)**\n• จำนวนคนสูงสุดของบริการ: 4 [S1]\n\nroom_seats: หัวข้อนี้อยู่นอกขอบเขตรายการที่เลือก กรุณาระบุบริการหรือรายการที่เกี่ยวข้อง\n\ncapacity_persons: หัวข้อนี้อยู่นอกขอบเขตรายการที่เลือก กรุณาระบุบริการหรือรายการที่เกี่ยวข้อง'

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 308. common / failures / test_nintendo_service_capacity_survives_game_title_correction (tests.test_thai_noisy_input_flow_20260929.ThaiNoisyInputFlowTests.test_nintendo_service_capacity_survives_game_title_correction)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_thai_noisy_input_flow_20260929.py", line 84, in test_nintendo_service_capacity_survives_game_title_correction
    self.assertEqual(sports.route.category, "games")
AssertionError: 'knowledge' != 'games'
- knowledge
+ games


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 309. common / failures / test_number_in_verified_game_title_is_not_a_catalog_count (tests.test_thai_noisy_input_flow_20260929.ThaiNoisyInputFlowTests.test_number_in_verified_game_title_is_not_a_catalog_count)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_thai_noisy_input_flow_20260929.py", line 46, in test_number_in_verified_game_title_is_not_a_catalog_count
    self.assertEqual(known.route.category, "games")
AssertionError: 'knowledge' != 'games'
- knowledge
+ games


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 310. common / failures / test_racing_catalog_and_tournament_question_stay_separate (tests.test_thai_noisy_input_flow_20260929.ThaiNoisyInputFlowTests.test_racing_catalog_and_tournament_question_stay_separate)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_thai_noisy_input_flow_20260929.py", line 31, in test_racing_catalog_and_tournament_question_stay_separate
    self.assertEqual(rules.route.category, "competition_rules")
AssertionError: 'knowledge' != 'competition_rules'
- knowledge
+ competition_rules


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 311. common / failures / test_round_duration_comes_from_verified_service_rows (tests.test_thai_noisy_input_flow_20260929.ThaiNoisyInputFlowTests.test_round_duration_comes_from_verified_service_rows) (question='PC Zone รอบละกี่นาที')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_thai_noisy_input_flow_20260929.py", line 58, in test_round_duration_comes_from_verified_service_rows
    self.assertEqual(result.route.category, "reservation")
AssertionError: 'knowledge' != 'reservation'
- knowledge
+ reservation


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 312. common / failures / test_round_duration_comes_from_verified_service_rows (tests.test_thai_noisy_input_flow_20260929.ThaiNoisyInputFlowTests.test_round_duration_comes_from_verified_service_rows) (question='VR Zone รอบละกี่นาที')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_thai_noisy_input_flow_20260929.py", line 58, in test_round_duration_comes_from_verified_service_rows
    self.assertEqual(result.route.category, "reservation")
AssertionError: 'knowledge' != 'reservation'
- knowledge
+ reservation


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 313. common / failures / test_zone_catalog_and_genre_are_not_single_game_requests (tests.test_thai_noisy_input_flow_20260929.ThaiNoisyInputFlowTests.test_zone_catalog_and_genre_are_not_single_game_requests) (question='PC Zone มีเกมอะไรให้เล่น')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_thai_noisy_input_flow_20260929.py", line 94, in test_zone_catalog_and_genre_are_not_single_game_requests
    self.assertEqual(result.route.category, "games")
AssertionError: 'knowledge' != 'games'
- knowledge
+ games


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 314. common / failures / test_zone_catalog_and_genre_are_not_single_game_requests (tests.test_thai_noisy_input_flow_20260929.ThaiNoisyInputFlowTests.test_zone_catalog_and_genre_are_not_single_game_requests) (question='Cockpit Zone มีเกมอะไรให้เล่นบ้าง')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_thai_noisy_input_flow_20260929.py", line 94, in test_zone_catalog_and_genre_are_not_single_game_requests
    self.assertEqual(result.route.category, "games")
AssertionError: 'knowledge' != 'games'
- knowledge
+ games


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 315. common / failures / test_entire_pipeline_does_not_replace_unrecorded_numeric_edition (tests.test_two_turn_choices_r39.TwoTurnChoicesTests.test_entire_pipeline_does_not_replace_unrecorded_numeric_edition)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_two_turn_choices_r39.py", line 136, in test_entire_pipeline_does_not_replace_unrecorded_numeric_edition
    self.assertEqual(r.mode,'pipeline:game_edition_unconfirmed')
AssertionError: 'pipeline:common_clarification' != 'pipeline:game_edition_unconfirmed'
- pipeline:common_clarification
+ pipeline:game_edition_unconfirmed


```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 316. common / errors / test_conduct_query_ranks_conduct_sections_first (tests.test_competition_target_grounding.CompetitionTargetGroundingTests.test_conduct_query_ranks_conduct_sections_first)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_target_grounding.py", line 65, in test_conduct_query_ranks_conduct_sections_first
    hits, _ = retrieve_curated(
              ^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\retrieval.py", line 900, in retrieve_curated
    return hits, PipelineTrace("rag_retrieval", "curated_lexical", confidence, detail, {"category": category, "game": competition_game, "intent": competition_intent,"common_ownership_blocked":ownership_blocked})
                                                                                                                                                                                                ^^^^^^^^^^^^^^^^^
NameError: name 'ownership_blocked' is not defined

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 317. common / errors / test_known_source_gap_has_a_machine_readable_reason (tests.test_competition_target_grounding.CompetitionTargetGroundingTests.test_known_source_gap_has_a_machine_readable_reason)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_target_grounding.py", line 140, in test_known_source_gap_has_a_machine_readable_reason
    hits, _ = retrieve_curated(
              ^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\retrieval.py", line 900, in retrieve_curated
    return hits, PipelineTrace("rag_retrieval", "curated_lexical", confidence, detail, {"category": category, "game": competition_game, "intent": competition_intent,"common_ownership_blocked":ownership_blocked})
                                                                                                                                                                                                ^^^^^^^^^^^^^^^^^
NameError: name 'ownership_blocked' is not defined

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 318. common / errors / test_team_composition_ranks_the_team_size_section_first (tests.test_competition_target_grounding.CompetitionTargetGroundingTests.test_team_composition_ranks_the_team_size_section_first)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_competition_target_grounding.py", line 76, in test_team_composition_ranks_the_team_size_section_first
    hits, _ = retrieve_curated(
              ^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\retrieval.py", line 900, in retrieve_curated
    return hits, PipelineTrace("rag_retrieval", "curated_lexical", confidence, detail, {"category": category, "game": competition_game, "intent": competition_intent,"common_ownership_blocked":ownership_blocked})
                                                                                                                                                                                                ^^^^^^^^^^^^^^^^^
NameError: name 'ownership_blocked' is not defined

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 319. common / errors / test_live_booking_resume_fetches_again_instead_of_replaying_old_status (tests.test_domain_resume_r42.DomainResumeR42Tests.test_live_booking_resume_fetches_again_instead_of_replaying_old_status)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_domain_resume_r42.py", line 165, in test_live_booking_resume_fetches_again_instead_of_replaying_old_status
    execute(s,'VALORANT controls')
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_domain_resume_r42.py", line 25, in execute
    b['trace']=[asdict(t) for t in result.trace];b['task_contract']=next(t.metadata for t in result.trace if t.stage=='task_answer_contract')
                                                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
StopIteration

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 320. common / errors / test_semantic_cases (tests.test_integrated_improvement_r21_20261001.IntegratedImprovementTests.test_semantic_cases) (case='unknown-person')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_integrated_improvement_r21_20261001.py", line 58, in test_semantic_cases
    row=run_focused_case(case)
        ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_reliability_flow_20261001.py", line 59, in run_focused_case
    result = answer_question_pipeline_debug(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4712, in answer_question_pipeline_debug
    return get_pipeline().answer(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4084, in _answer_single
    rag_hits, rag_trace = retrieve_curated(pre.clean_query, route.category)
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\retrieval.py", line 900, in retrieve_curated
    return hits, PipelineTrace("rag_retrieval", "curated_lexical", confidence, detail, {"category": category, "game": competition_game, "intent": competition_intent,"common_ownership_blocked … [ย่อจาก2,083ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 321. common / errors / test_specific_policy_facets_beat_generic_public_access (tests.test_intent_trap_protected_flow.ProtectedIntentFlowTests.test_specific_policy_facets_beat_generic_public_access) (question='คนนอกใช้ PC ฟรีไหม')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 352, in test_specific_policy_facets_beat_generic_public_access
    result = self.answer(question, locale)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_intent_trap_protected_flow.py", line 26, in answer
    return self.pipeline.answer(
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4084, in _answer_single
    rag_hits, rag_trace = retrieve_curated(pre.clean_query, route.category)
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\retrieval.py", line 900, in retrieve_curated
    return hits, PipelineTrace("rag_retrieval", "curated_lexical", confidence, detail, {"category": category, "game": competition_game, "intent": competition_intent,"common_ownership_blocked":ownership_blocked})
                                                                                                                                                                                                ^^^^^^^^^^^^^^^^^
NameError: nam … [ย่อจาก1,837ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 322. common / errors / test_unverified_thai_studio_claim_is_a_no_answer_outcome (tests.test_master_ground_truth_route_regressions.MasterGroundTruthRouteRegressionTests.test_unverified_thai_studio_claim_is_a_no_answer_outcome)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_master_ground_truth_route_regressions.py", line 224, in test_unverified_thai_studio_claim_is_a_no_answer_outcome
    result = answer_question_pipeline_debug(
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4712, in answer_question_pipeline_debug
    return get_pipeline().answer(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4020, in _answer_single
    fallback = build_experimental_fallback(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\experimental_fallback.py", line 1087, in build_experimental_fallback
    rows, details = _retrieve_experimental_rows(
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\experimental_fallback.py", line 259, in _retrieve_experimental_rows
    hybrid_rows, hybrid_trace = retrieve_hybrid_guarded(
                                ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Docum … [ย่อจาก2,819ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 323. common / errors / test_phrase_recovery_keeps_resource_and_duration (tests.test_multi_error_typo_recovery_20260929.MultiErrorTypoRecoveryTests.test_phrase_recovery_keeps_resource_and_duration) (question='ติดต่าทาไงหน')

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_multi_error_typo_recovery_20260929.py", line 58, in test_phrase_recovery_keeps_resource_and_duration
    self.assertEqual(_answer(question).route.intent, intent)
                     ^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_multi_error_typo_recovery_20260929.py", line 14, in _answer
    return answer_question_pipeline_debug(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4712, in answer_question_pipeline_debug
    return get_pipeline().answer(
           ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 1173, in answer
    return self._answer_single(
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\engine.py", line 4084, in _answer_single
    rag_hits, rag_trace = retrieve_curated(pre.clean_query, route.category)
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\app\pipeline\retrieval.py", line 900, in retrieve_curated
    return hits, PipelineTrace("rag_retrieval", "curated_lexical", confidence, detail, {"category": category, "game": competitio … [ย่อจาก2,145ตัวอักษร; มีข้อมูลเต็มในevidence.sqlite/raw]
```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)

## 324. common / errors / test_catalog_all_and_ordinal_ask_for_axis_but_all_zones_is_explicit (tests.test_task_memory_r41.TaskMemoryR41Tests.test_catalog_all_and_ordinal_ask_for_axis_but_all_zones_is_explicit)

```text
Traceback (most recent call last):
  File "C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r64_full_comparison_20261013\system\tests\test_task_memory_r41.py", line 161, in test_catalog_all_and_ordinal_ask_for_axis_but_all_zones_is_explicit
    p=s.begin('s',q,q,locale='en');self.assertIn(p['plan']['message_key'],('scope','ordinal_axis'))
                                                 ~~~~~~~~~^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not subscriptable

```

[common_test_all.py_temp_fixed.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r64_full_comparison_20261013/common_test_all.py_temp_fixed.json)
