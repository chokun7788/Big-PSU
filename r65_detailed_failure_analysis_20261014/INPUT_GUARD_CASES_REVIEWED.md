# Input guard: mismatchที่ตรวจทานแล้ว

แทนการเลือกkeyในappendixฉบับร่างที่ไม่ครอบคลุมsuffix _match; ไม่แก้gradeหรือlogR64

## 1. legacy / KIA-0018 / ;yoouhgxbfws,

```json
{
  "id": "KIA-0018",
  "input": ";yoouhgxbfws,",
  "expected": {
    "id": "KIA-0018",
    "split": "test",
    "observed_input": ";yoouhgxbfws,",
    "canonical_question": "วันนี้เปิดไหม",
    "expected_flags": [
      "keyboard_layout_mismatch"
    ],
    "should_detect_keyboard_layout": true,
    "should_detect_repeated_character": false,
    "should_block_answer": true,
    "expected_action": "request_retype",
    "anomaly_family": "layout_th_to_en_full",
    "layout_direction": "thai_intended_english_active",
    "corruption_scope": "full_thai_script",
    "repeat_interpretation": "none",
    "contains_adjacent_repeat": true,
    "length_band": "08_15",
    "difficulty": "medium",
    "label_confidence": "high",
    "generation_note": "manual short-query layout mismatch",
    "source_group": "manual_edge_case",
    "source_case_id": null,
    "source_expected_category": null
  },
  "actual": {
    "action": "request_retype",
    "detected_action": "request_retype",
    "applied_action": "request_retype",
    "should_retype": true,
    "flags": [
      "keyboard_layout_mismatch",
      "repeated_character_typo"
    ],
    "layout_score": 0.668508,
    "repeat_score": 0.560799,
    "guard_status": "flagged",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 3.339
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 2. legacy / KIA-0187 / เฟรมเรตกับความละเอียดดต่างกันยังไง ขอแบบเข้าใจง่าย

```json
{
  "id": "KIA-0187",
  "input": "เฟรมเรตกับความละเอียดดต่างกันยังไง ขอแบบเข้าใจง่าย",
  "expected": {
    "id": "KIA-0187",
    "split": "test",
    "observed_input": "เฟรมเรตกับความละเอียดดต่างกันยังไง ขอแบบเข้าใจง่าย",
    "canonical_question": "เฟรมเรตกับความละเอียดต่างกันยังไง ขอแบบเข้าใจง่าย",
    "expected_flags": [
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": false,
    "should_detect_repeated_character": true,
    "should_block_answer": false,
    "expected_action": "soft_flag_typo",
    "anomaly_family": "repeat_thai_internal",
    "layout_direction": null,
    "corruption_scope": "single_character_inside_thai_span",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "41_plus",
    "difficulty": "medium",
    "label_confidence": "high",
    "generation_note": "duplicated Thai base character 'ด'",
    "source_group": "general_llm",
    "source_case_id": "MB-1347-GL-022",
    "source_expected_category": [
      "general",
      "knowledge"
    ]
  },
  "actual": {
    "action": "continue",
    "detected_action": "continue",
    "applied_action": "continue",
    "should_retype": false,
    "flags": [],
    "layout_score": 0.005192,
    "repeat_score": 0.466557,
    "guard_status": "passed",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 3.648
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 3. legacy / KIA-0190 / PUBG อยู่โซซนไหน

```json
{
  "id": "KIA-0190",
  "input": "PUBG อยู่โซซนไหน",
  "expected": {
    "id": "KIA-0190",
    "split": "calibration",
    "observed_input": "PUBG อยู่โซซนไหน",
    "canonical_question": "PUBG อยู่โซนไหน",
    "expected_flags": [
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": false,
    "should_detect_repeated_character": true,
    "should_block_answer": false,
    "expected_action": "soft_flag_typo",
    "anomaly_family": "repeat_thai_internal",
    "layout_direction": null,
    "corruption_scope": "single_character_inside_thai_span",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "16_40",
    "difficulty": "medium",
    "label_confidence": "high",
    "generation_note": "duplicated Thai base character 'ซ' inside 'โซน'",
    "source_group": "availability_game",
    "source_case_id": "MB-0668-AG-015",
    "source_expected_category": "games"
  },
  "actual": {
    "action": "continue",
    "detected_action": "continue",
    "applied_action": "continue",
    "should_retype": false,
    "flags": [],
    "layout_score": 0.005488,
    "repeat_score": 0.528719,
    "guard_status": "passed",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 2.149
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 4. legacy / KIA-0192 / Gaming PC รุ่น MSI MAG Infinite S3 14th อยู่โซซนไหน

```json
{
  "id": "KIA-0192",
  "input": "Gaming PC รุ่น MSI MAG Infinite S3 14th อยู่โซซนไหน",
  "expected": {
    "id": "KIA-0192",
    "split": "test",
    "observed_input": "Gaming PC รุ่น MSI MAG Infinite S3 14th อยู่โซซนไหน",
    "canonical_question": "Gaming PC รุ่น MSI MAG Infinite S3 14th อยู่โซนไหน",
    "expected_flags": [
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": false,
    "should_detect_repeated_character": true,
    "should_block_answer": false,
    "expected_action": "soft_flag_typo",
    "anomaly_family": "repeat_thai_internal",
    "layout_direction": null,
    "corruption_scope": "single_character_inside_thai_span",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "41_plus",
    "difficulty": "medium",
    "label_confidence": "high",
    "generation_note": "duplicated Thai base character 'ซ' inside 'โซน'",
    "source_group": "equipment",
    "source_case_id": "MB-0413-E-012",
    "source_expected_category": [
      "equipment",
      "games"
    ]
  },
  "actual": {
    "action": "continue",
    "detected_action": "continue",
    "applied_action": "continue",
    "should_retype": false,
    "flags": [],
    "layout_score": 0.005488,
    "repeat_score": 0.528719,
    "guard_status": "passed",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 4.513
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 5. legacy / KIA-0194 / VALORANT ถ้าใช้ bug จะโดดนอะไร

```json
{
  "id": "KIA-0194",
  "input": "VALORANT ถ้าใช้ bug จะโดดนอะไร",
  "expected": {
    "id": "KIA-0194",
    "split": "test",
    "observed_input": "VALORANT ถ้าใช้ bug จะโดดนอะไร",
    "canonical_question": "VALORANT ถ้าใช้ bug จะโดนอะไร",
    "expected_flags": [
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": false,
    "should_detect_repeated_character": true,
    "should_block_answer": false,
    "expected_action": "soft_flag_typo",
    "anomaly_family": "repeat_thai_internal",
    "layout_direction": null,
    "corruption_scope": "single_character_inside_thai_span",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "16_40",
    "difficulty": "medium",
    "label_confidence": "high",
    "generation_note": "duplicated Thai base character 'ด'",
    "source_group": "competition_rules",
    "source_case_id": "MB-0547-CR-011",
    "source_expected_category": "competition_rules"
  },
  "actual": {
    "action": "continue",
    "detected_action": "continue",
    "applied_action": "continue",
    "should_retype": false,
    "flags": [],
    "layout_score": 0.005143,
    "repeat_score": 0.548758,
    "guard_status": "passed",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 2.505
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 6. legacy / KIA-0204 / Counter-Strike 2 ใช้จออยยังไง

```json
{
  "id": "KIA-0204",
  "input": "Counter-Strike 2 ใช้จออยยังไง",
  "expected": {
    "id": "KIA-0204",
    "split": "test",
    "observed_input": "Counter-Strike 2 ใช้จออยยังไง",
    "canonical_question": "Counter-Strike 2 ใช้จอยยังไง",
    "expected_flags": [
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": false,
    "should_detect_repeated_character": true,
    "should_block_answer": false,
    "expected_action": "soft_flag_typo",
    "anomaly_family": "repeat_thai_internal",
    "layout_direction": null,
    "corruption_scope": "single_character_inside_thai_span",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "16_40",
    "difficulty": "medium",
    "label_confidence": "high",
    "generation_note": "duplicated Thai base character 'อ'",
    "source_group": "game_controls",
    "source_case_id": "MB-0264-GC-018",
    "source_expected_category": "games"
  },
  "actual": {
    "action": "continue",
    "detected_action": "continue",
    "applied_action": "continue",
    "should_retype": false,
    "flags": [],
    "layout_score": 0.001927,
    "repeat_score": 0.522255,
    "guard_status": "passed",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 1.528
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 7. legacy / KIA-0226 / ช่วยสรุปวิธีพูดขอบคุณณแบบสุภาพ 2 ประโยค ขอแบบเข้าใจง่าย

```json
{
  "id": "KIA-0226",
  "input": "ช่วยสรุปวิธีพูดขอบคุณณแบบสุภาพ 2 ประโยค ขอแบบเข้าใจง่าย",
  "expected": {
    "id": "KIA-0226",
    "split": "test",
    "observed_input": "ช่วยสรุปวิธีพูดขอบคุณณแบบสุภาพ 2 ประโยค ขอแบบเข้าใจง่าย",
    "canonical_question": "ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ขอแบบเข้าใจง่าย",
    "expected_flags": [
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": false,
    "should_detect_repeated_character": true,
    "should_block_answer": false,
    "expected_action": "soft_flag_typo",
    "anomaly_family": "repeat_thai_internal",
    "layout_direction": null,
    "corruption_scope": "single_character_inside_thai_span",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "41_plus",
    "difficulty": "medium",
    "label_confidence": "high",
    "generation_note": "duplicated Thai base character 'ณ'",
    "source_group": "general_llm",
    "source_case_id": "MB-1350-GL-025",
    "source_expected_category": [
      "general",
      "knowledge"
    ]
  },
  "actual": {
    "action": "continue",
    "detected_action": "continue",
    "applied_action": "continue",
    "should_retype": false,
    "flags": [],
    "layout_score": 0.005413,
    "repeat_score": 0.510341,
    "guard_status": "passed",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 3.382
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 8. legacy / KIA-0231 / Gaming Monitor อยู่โซซนไหน

```json
{
  "id": "KIA-0231",
  "input": "Gaming Monitor อยู่โซซนไหน",
  "expected": {
    "id": "KIA-0231",
    "split": "test",
    "observed_input": "Gaming Monitor อยู่โซซนไหน",
    "canonical_question": "Gaming Monitor อยู่โซนไหน",
    "expected_flags": [
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": false,
    "should_detect_repeated_character": true,
    "should_block_answer": false,
    "expected_action": "soft_flag_typo",
    "anomaly_family": "repeat_thai_internal",
    "layout_direction": null,
    "corruption_scope": "single_character_inside_thai_span",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "16_40",
    "difficulty": "medium",
    "label_confidence": "high",
    "generation_note": "duplicated Thai base character 'ซ' inside 'โซน'",
    "source_group": "equipment",
    "source_case_id": "MB-0416-E-015",
    "source_expected_category": [
      "equipment",
      "games"
    ]
  },
  "actual": {
    "action": "continue",
    "detected_action": "continue",
    "applied_action": "continue",
    "should_retype": false,
    "flags": [],
    "layout_score": 0.012333,
    "repeat_score": 0.528719,
    "guard_status": "passed",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 1.15
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 9. legacy / KIA-0242 / VALORANT อยู่โโซนไหน

```json
{
  "id": "KIA-0242",
  "input": "VALORANT อยู่โโซนไหน",
  "expected": {
    "id": "KIA-0242",
    "split": "test",
    "observed_input": "VALORANT อยู่โโซนไหน",
    "canonical_question": "VALORANT อยู่โซนไหน",
    "expected_flags": [
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": false,
    "should_detect_repeated_character": true,
    "should_block_answer": false,
    "expected_action": "soft_flag_typo",
    "anomaly_family": "repeat_thai_mark_or_vowel",
    "layout_direction": null,
    "corruption_scope": "thai_vowel_or_tone_mark",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "16_40",
    "difficulty": "hard",
    "label_confidence": "high",
    "generation_note": "duplicated Thai vowel/tone character 'โ'",
    "source_group": "availability_game",
    "source_case_id": "MB-0672-AG-019",
    "source_expected_category": "games"
  },
  "actual": {
    "action": "continue",
    "detected_action": "continue",
    "applied_action": "continue",
    "should_retype": false,
    "flags": [],
    "layout_score": 0.005472,
    "repeat_score": 0.525782,
    "guard_status": "passed",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 1.156
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 10. legacy / KIA-0252 / เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาาพหนึ่งประโยค ขอแบบเข้าใจง่าย

```json
{
  "id": "KIA-0252",
  "input": "เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาาพหนึ่งประโยค ขอแบบเข้าใจง่าย",
  "expected": {
    "id": "KIA-0252",
    "split": "test",
    "observed_input": "เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาาพหนึ่งประโยค ขอแบบเข้าใจง่าย",
    "canonical_question": "เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาพหนึ่งประโยค ขอแบบเข้าใจง่าย",
    "expected_flags": [
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": false,
    "should_detect_repeated_character": true,
    "should_block_answer": false,
    "expected_action": "soft_flag_typo",
    "anomaly_family": "repeat_thai_mark_or_vowel",
    "layout_direction": null,
    "corruption_scope": "thai_vowel_or_tone_mark",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "41_plus",
    "difficulty": "hard",
    "label_confidence": "high",
    "generation_note": "duplicated Thai vowel/tone character 'า'",
    "source_group": "general_llm",
    "source_case_id": "MB-1352-GL-027",
    "source_expected_category": [
      "general",
      "knowledge"
    ]
  },
  "actual": {
    "action": "continue",
    "detected_action": "continue",
    "applied_action": "continue",
    "should_retype": false,
    "flags": [],
    "layout_score": 0.005611,
    "repeat_score": 0.531295,
    "guard_status": "passed",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 5.643
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 11. legacy / KIA-0261 / PS5 ราคาเท่าไหร่ แแล้วมีเกมอะไรบ้าง

```json
{
  "id": "KIA-0261",
  "input": "PS5 ราคาเท่าไหร่ แแล้วมีเกมอะไรบ้าง",
  "expected": {
    "id": "KIA-0261",
    "split": "test",
    "observed_input": "PS5 ราคาเท่าไหร่ แแล้วมีเกมอะไรบ้าง",
    "canonical_question": "PS5 ราคาเท่าไหร่ แล้วมีเกมอะไรบ้าง",
    "expected_flags": [
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": false,
    "should_detect_repeated_character": true,
    "should_block_answer": false,
    "expected_action": "soft_flag_typo",
    "anomaly_family": "repeat_thai_mark_or_vowel",
    "layout_direction": null,
    "corruption_scope": "thai_vowel_or_tone_mark",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "16_40",
    "difficulty": "hard",
    "label_confidence": "high",
    "generation_note": "duplicated Thai vowel/tone character 'แ'",
    "source_group": "compound",
    "source_case_id": "MB-1254-C-018",
    "source_expected_category": "multi_question"
  },
  "actual": {
    "action": "continue",
    "detected_action": "continue",
    "applied_action": "continue",
    "should_retype": false,
    "flags": [],
    "layout_score": 0.005266,
    "repeat_score": 0.472115,
    "guard_status": "passed",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 1.523
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 12. legacy / KIA-0270 / Gaming Keyboard อยู่โโซนไหน

```json
{
  "id": "KIA-0270",
  "input": "Gaming Keyboard อยู่โโซนไหน",
  "expected": {
    "id": "KIA-0270",
    "split": "calibration",
    "observed_input": "Gaming Keyboard อยู่โโซนไหน",
    "canonical_question": "Gaming Keyboard อยู่โซนไหน",
    "expected_flags": [
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": false,
    "should_detect_repeated_character": true,
    "should_block_answer": false,
    "expected_action": "soft_flag_typo",
    "anomaly_family": "repeat_thai_mark_or_vowel",
    "layout_direction": null,
    "corruption_scope": "thai_vowel_or_tone_mark",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "16_40",
    "difficulty": "hard",
    "label_confidence": "high",
    "generation_note": "duplicated Thai vowel/tone character 'โ'",
    "source_group": "equipment",
    "source_case_id": "MB-0419-E-018",
    "source_expected_category": [
      "equipment",
      "games"
    ]
  },
  "actual": {
    "action": "continue",
    "detected_action": "continue",
    "applied_action": "continue",
    "should_retype": false,
    "flags": [],
    "layout_score": 0.005472,
    "repeat_score": 0.525782,
    "guard_status": "passed",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 1.42
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 13. legacy / KIA-0277 / วันนี้มีข่าาว esports อะไรล่าสุด

```json
{
  "id": "KIA-0277",
  "input": "วันนี้มีข่าาว esports อะไรล่าสุด",
  "expected": {
    "id": "KIA-0277",
    "split": "test",
    "observed_input": "วันนี้มีข่าาว esports อะไรล่าสุด",
    "canonical_question": "วันนี้มีข่าว esports อะไรล่าสุด",
    "expected_flags": [
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": false,
    "should_detect_repeated_character": true,
    "should_block_answer": false,
    "expected_action": "soft_flag_typo",
    "anomaly_family": "repeat_thai_mark_or_vowel",
    "layout_direction": null,
    "corruption_scope": "thai_vowel_or_tone_mark",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "16_40",
    "difficulty": "hard",
    "label_confidence": "high",
    "generation_note": "duplicated Thai vowel/tone character 'า'",
    "source_group": "ambiguity_no_answer",
    "source_case_id": "MB-0648-ANA-022",
    "source_expected_category": [
      "no_answer",
      "games",
      "general"
    ]
  },
  "actual": {
    "action": "continue",
    "detected_action": "continue",
    "applied_action": "continue",
    "should_retype": false,
    "flags": [],
    "layout_score": 0.012269,
    "repeat_score": 0.522849,
    "guard_status": "passed",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 1.328
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 14. legacy / KIA-0310 / กี่บบาท

```json
{
  "id": "KIA-0310",
  "input": "กี่บบาท",
  "expected": {
    "id": "KIA-0310",
    "split": "calibration",
    "observed_input": "กี่บบาท",
    "canonical_question": "กี่บาท",
    "expected_flags": [
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": false,
    "should_detect_repeated_character": true,
    "should_block_answer": false,
    "expected_action": "soft_flag_typo",
    "anomaly_family": "repeat_short_token",
    "layout_direction": null,
    "corruption_scope": "short_query_or_token",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "04_07",
    "difficulty": "hard",
    "label_confidence": "high",
    "generation_note": "manual short repeated-character case: thai_consonant",
    "source_group": "manual_edge_case",
    "source_case_id": null,
    "source_expected_category": null
  },
  "actual": {
    "action": "continue",
    "detected_action": "continue",
    "applied_action": "continue",
    "should_retype": false,
    "flags": [],
    "layout_score": 0.005246,
    "repeat_score": 0.51247,
    "guard_status": "passed",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 0.727
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 15. legacy / KIA-0320 / เกมอะไรร

```json
{
  "id": "KIA-0320",
  "input": "เกมอะไรร",
  "expected": {
    "id": "KIA-0320",
    "split": "calibration",
    "observed_input": "เกมอะไรร",
    "canonical_question": "เกมอะไร",
    "expected_flags": [
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": false,
    "should_detect_repeated_character": true,
    "should_block_answer": false,
    "expected_action": "soft_flag_typo",
    "anomaly_family": "repeat_short_token",
    "layout_direction": null,
    "corruption_scope": "short_query_or_token",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "08_15",
    "difficulty": "hard",
    "label_confidence": "high",
    "generation_note": "manual short repeated-character case: thai_consonant",
    "source_group": "manual_edge_case",
    "source_case_id": null,
    "source_expected_category": null
  },
  "actual": {
    "action": "continue",
    "detected_action": "continue",
    "applied_action": "continue",
    "should_retype": false,
    "flags": [],
    "layout_score": 0.007406,
    "repeat_score": 0.509828,
    "guard_status": "passed",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 0.833
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 16. legacy / KIA-0332 / TEKKEN 8 dy[ Resident Evil Village ,ux6j,,vtwi[hk'

```json
{
  "id": "KIA-0332",
  "input": "TEKKEN 8 dy[ Resident Evil Village ,ux6j,,vtwi[hk'",
  "expected": {
    "id": "KIA-0332",
    "split": "test",
    "observed_input": "TEKKEN 8 dy[ Resident Evil Village ,ux6j,,vtwi[hk'",
    "canonical_question": "TEKKEN 8 กับ Resident Evil Village มีปุ่มอะไรบ้าง",
    "expected_flags": [
      "keyboard_layout_mismatch",
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": true,
    "should_detect_repeated_character": true,
    "should_block_answer": true,
    "expected_action": "request_retype",
    "anomaly_family": "combined_layout_and_repeat",
    "layout_direction": "thai_intended_english_active",
    "corruption_scope": "full_thai_script_plus_repeated_key",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "41_plus",
    "difficulty": "hard",
    "label_confidence": "high",
    "generation_note": "duplicated Thai base character 'ม'; then mapped Thai characters to English-key positions",
    "source_group": "compound",
    "source_case_id": "MB-1261-C-025",
    "source_expected_category": [
      "games",
      "multi_question"
    ]
  },
  "actual": {
    "action": "request_retype",
    "detected_action": "request_retype",
    "applied_action": "request_retype",
    "should_retype": true,
    "flags": [
      "keyboard_layout_mismatch"
    ],
    "layout_score": 0.823518,
    "repeat_score": 0.546227,
    "guard_status": "flagged",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 4.075
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 17. legacy / KIA-0340 / Counter3Strike 2 ,klkp0tFffovtwi

```json
{
  "id": "KIA-0340",
  "input": "Counter3Strike 2 ,klkp0tFffovtwi",
  "expected": {
    "id": "KIA-0340",
    "split": "calibration",
    "observed_input": "Counter3Strike 2 ,klkp0tFffovtwi",
    "canonical_question": "Counter-Strike 2 มาสายจะโดนอะไร",
    "expected_flags": [
      "keyboard_layout_mismatch",
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": true,
    "should_detect_repeated_character": true,
    "should_block_answer": true,
    "expected_action": "request_retype",
    "anomaly_family": "combined_layout_and_repeat",
    "layout_direction": "thai_intended_english_active",
    "corruption_scope": "full_thai_script_plus_repeated_key",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "16_40",
    "difficulty": "hard",
    "label_confidence": "high",
    "generation_note": "duplicated Thai base character 'ด'; then mapped Thai characters to English-key positions",
    "source_group": "competition_rules",
    "source_case_id": "MB-0569-CR-033",
    "source_expected_category": "competition_rules"
  },
  "actual": {
    "action": "request_retype",
    "detected_action": "request_retype",
    "applied_action": "request_retype",
    "should_retype": true,
    "flags": [
      "keyboard_layout_mismatch"
    ],
    "layout_score": 0.565078,
    "repeat_score": 0.54432,
    "guard_status": "flagged",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 2.167
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 18. legacy / KIA-0348 / Gaming Headset vp^jF::owso

```json
{
  "id": "KIA-0348",
  "input": "Gaming Headset vp^jF::owso",
  "expected": {
    "id": "KIA-0348",
    "split": "test",
    "observed_input": "Gaming Headset vp^jF::owso",
    "canonical_question": "Gaming Headset อยู่โซนไหน",
    "expected_flags": [
      "keyboard_layout_mismatch",
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": true,
    "should_detect_repeated_character": true,
    "should_block_answer": true,
    "expected_action": "request_retype",
    "anomaly_family": "combined_layout_and_repeat",
    "layout_direction": "thai_intended_english_active",
    "corruption_scope": "full_thai_script_plus_repeated_key",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "16_40",
    "difficulty": "hard",
    "label_confidence": "high",
    "generation_note": "duplicated Thai base character 'ซ' inside 'โซน'; then mapped Thai characters to English-key positions",
    "source_group": "equipment",
    "source_case_id": "MB-0425-E-024",
    "source_expected_category": [
      "equipment",
      "games"
    ]
  },
  "actual": {
    "action": "request_retype",
    "detected_action": "request_retype",
    "applied_action": "request_retype",
    "should_retype": true,
    "flags": [
      "keyboard_layout_mismatch"
    ],
    "layout_score": 0.470279,
    "repeat_score": 0.528719,
    "guard_status": "flagged",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 1.525
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 19. legacy / KIA-0351 / Gran Turismo 7 dy[ Overcooked! 2 ,ux6j,,vtwi[hk'

```json
{
  "id": "KIA-0351",
  "input": "Gran Turismo 7 dy[ Overcooked! 2 ,ux6j,,vtwi[hk'",
  "expected": {
    "id": "KIA-0351",
    "split": "test",
    "observed_input": "Gran Turismo 7 dy[ Overcooked! 2 ,ux6j,,vtwi[hk'",
    "canonical_question": "Gran Turismo 7 กับ Overcooked! 2 มีปุ่มอะไรบ้าง",
    "expected_flags": [
      "keyboard_layout_mismatch",
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": true,
    "should_detect_repeated_character": true,
    "should_block_answer": true,
    "expected_action": "request_retype",
    "anomaly_family": "combined_layout_and_repeat",
    "layout_direction": "thai_intended_english_active",
    "corruption_scope": "full_thai_script_plus_repeated_key",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "41_plus",
    "difficulty": "hard",
    "label_confidence": "high",
    "generation_note": "duplicated Thai base character 'ม'; then mapped Thai characters to English-key positions",
    "source_group": "compound",
    "source_case_id": "MB-1263-C-027",
    "source_expected_category": [
      "games",
      "multi_question"
    ]
  },
  "actual": {
    "action": "request_retype",
    "detected_action": "request_retype",
    "applied_action": "request_retype",
    "should_retype": true,
    "flags": [
      "keyboard_layout_mismatch"
    ],
    "layout_score": 0.823745,
    "repeat_score": 0.546227,
    "guard_status": "flagged",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 2.727
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 20. legacy / KIA-0352 / =j;pli6x;bTur^f-v[86Ic[[ll64kr 2 xitFp8 9v[gxHo4kKkwmp

```json
{
  "id": "KIA-0352",
  "input": "=j;pli6x;bTur^f-v[86Ic[[ll64kr 2 xitFp8 9v[gxHo4kKkwmp",
  "expected": {
    "id": "KIA-0352",
    "split": "test",
    "observed_input": "=j;pli6x;bTur^f-v[86Ic[[ll64kr 2 xitFp8 9v[gxHo4kKkwmp",
    "canonical_question": "ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ตอบเป็นภาษาไทย",
    "expected_flags": [
      "keyboard_layout_mismatch",
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": true,
    "should_detect_repeated_character": true,
    "should_block_answer": true,
    "expected_action": "request_retype",
    "anomaly_family": "combined_layout_and_repeat",
    "layout_direction": "thai_intended_english_active",
    "corruption_scope": "full_thai_script_plus_repeated_key",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "41_plus",
    "difficulty": "hard",
    "label_confidence": "high",
    "generation_note": "duplicated Thai base character 'ส'; then mapped Thai characters to English-key positions",
    "source_group": "general_llm",
    "source_case_id": "MB-1360-GL-035",
    "source_expected_category": [
      "general",
      "knowledge"
    ]
  },
  "actual": {
    "action": "request_retype",
    "detected_action": "request_retype",
    "applied_action": "request_retype",
    "should_retype": true,
    "flags": [
      "keyboard_layout_mismatch"
    ],
    "layout_score": 0.652818,
    "repeat_score": 0.503353,
    "guard_status": "flagged",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 3.01
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 21. legacy / KIA-0356 / Fortnite .=h0vvppy'w'

```json
{
  "id": "KIA-0356",
  "input": "Fortnite .=h0vvppy'w'",
  "expected": {
    "id": "KIA-0356",
    "split": "test",
    "observed_input": "Fortnite .=h0vvppy'w'",
    "canonical_question": "Fortnite ใช้จอยยังไง",
    "expected_flags": [
      "keyboard_layout_mismatch",
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": true,
    "should_detect_repeated_character": true,
    "should_block_answer": true,
    "expected_action": "request_retype",
    "anomaly_family": "combined_layout_and_repeat",
    "layout_direction": "thai_intended_english_active",
    "corruption_scope": "full_thai_script_plus_repeated_key",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "16_40",
    "difficulty": "hard",
    "label_confidence": "high",
    "generation_note": "duplicated Thai base character 'อ'; then mapped Thai characters to English-key positions",
    "source_group": "game_controls",
    "source_case_id": "MB-0276-GC-030",
    "source_expected_category": "games"
  },
  "actual": {
    "action": "request_retype",
    "detected_action": "request_retype",
    "applied_action": "request_retype",
    "should_retype": true,
    "flags": [
      "keyboard_layout_mismatch"
    ],
    "layout_score": 0.534856,
    "repeat_score": 0.522255,
    "guard_status": "flagged",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 1.994
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 22. legacy / KIA-0361 / cx]8e;jk reservation gxHo4kKkwmpp 9v[gxHo4kKkwmp

```json
{
  "id": "KIA-0361",
  "input": "cx]8e;jk reservation gxHo4kKkwmpp 9v[gxHo4kKkwmp",
  "expected": {
    "id": "KIA-0361",
    "split": "test",
    "observed_input": "cx]8e;jk reservation gxHo4kKkwmpp 9v[gxHo4kKkwmp",
    "canonical_question": "แปลคำว่า reservation เป็นภาษาไทย ตอบเป็นภาษาไทย",
    "expected_flags": [
      "keyboard_layout_mismatch",
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": true,
    "should_detect_repeated_character": true,
    "should_block_answer": true,
    "expected_action": "request_retype",
    "anomaly_family": "combined_layout_and_repeat",
    "layout_direction": "thai_intended_english_active",
    "corruption_scope": "full_thai_script_plus_repeated_key",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "41_plus",
    "difficulty": "hard",
    "label_confidence": "high",
    "generation_note": "duplicated Thai base character 'ย'; then mapped Thai characters to English-key positions",
    "source_group": "general_llm",
    "source_case_id": "MB-1361-GL-036",
    "source_expected_category": [
      "general",
      "knowledge"
    ]
  },
  "actual": {
    "action": "request_retype",
    "detected_action": "request_retype",
    "applied_action": "request_retype",
    "should_retype": true,
    "flags": [
      "keyboard_layout_mismatch"
    ],
    "layout_score": 0.699046,
    "repeat_score": 0.52036,
    "guard_status": "flagged",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 1.728
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 23. legacy / KIA-0364 / Delta Force vp^jF::owso

```json
{
  "id": "KIA-0364",
  "input": "Delta Force vp^jF::owso",
  "expected": {
    "id": "KIA-0364",
    "split": "test",
    "observed_input": "Delta Force vp^jF::owso",
    "canonical_question": "Delta Force อยู่โซนไหน",
    "expected_flags": [
      "keyboard_layout_mismatch",
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": true,
    "should_detect_repeated_character": true,
    "should_block_answer": true,
    "expected_action": "request_retype",
    "anomaly_family": "combined_layout_and_repeat",
    "layout_direction": "thai_intended_english_active",
    "corruption_scope": "full_thai_script_plus_repeated_key",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "16_40",
    "difficulty": "hard",
    "label_confidence": "high",
    "generation_note": "duplicated Thai base character 'ซ' inside 'โซน'; then mapped Thai characters to English-key positions",
    "source_group": "availability_game",
    "source_case_id": "MB-0687-AG-029",
    "source_expected_category": "games"
  },
  "actual": {
    "action": "request_retype",
    "detected_action": "request_retype",
    "applied_action": "request_retype",
    "should_retype": true,
    "flags": [
      "keyboard_layout_mismatch"
    ],
    "layout_score": 0.474863,
    "repeat_score": 0.528719,
    "guard_status": "flagged",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 1.439
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 24. legacy / KIA-0369 / Beat Saber dy[ VALORANT ,ux6j,,vtwi[hk'

```json
{
  "id": "KIA-0369",
  "input": "Beat Saber dy[ VALORANT ,ux6j,,vtwi[hk'",
  "expected": {
    "id": "KIA-0369",
    "split": "test",
    "observed_input": "Beat Saber dy[ VALORANT ,ux6j,,vtwi[hk'",
    "canonical_question": "Beat Saber กับ VALORANT มีปุ่มอะไรบ้าง",
    "expected_flags": [
      "keyboard_layout_mismatch",
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": true,
    "should_detect_repeated_character": true,
    "should_block_answer": true,
    "expected_action": "request_retype",
    "anomaly_family": "combined_layout_and_repeat",
    "layout_direction": "thai_intended_english_active",
    "corruption_scope": "full_thai_script_plus_repeated_key",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "16_40",
    "difficulty": "hard",
    "label_confidence": "high",
    "generation_note": "duplicated Thai base character 'ม'; then mapped Thai characters to English-key positions",
    "source_group": "compound",
    "source_case_id": "MB-1265-C-029",
    "source_expected_category": [
      "games",
      "multi_question"
    ]
  },
  "actual": {
    "action": "request_retype",
    "detected_action": "request_retype",
    "applied_action": "request_retype",
    "should_retype": true,
    "flags": [
      "keyboard_layout_mismatch"
    ],
    "layout_score": 0.824745,
    "repeat_score": 0.546227,
    "guard_status": "flagged",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 2.399
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 25. legacy / KIA-0370 / g-upoxitFp8xit=kly,ryoTNdb0dii,c[[ll64krso7j'xitFp8 9v[gxHo4kKkwmp

```json
{
  "id": "KIA-0370",
  "input": "g-upoxitFp8xit=kly,ryoTNdb0dii,c[[ll64krso7j'xitFp8 9v[gxHo4kKkwmp",
  "expected": {
    "id": "KIA-0370",
    "split": "calibration",
    "observed_input": "g-upoxitFp8xit=kly,ryoTNdb0dii,c[[ll64krso7j'xitFp8 9v[gxHo4kKkwmp",
    "canonical_question": "เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาพหนึ่งประโยค ตอบเป็นภาษาไทย",
    "expected_flags": [
      "keyboard_layout_mismatch",
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": true,
    "should_detect_repeated_character": true,
    "should_block_answer": true,
    "expected_action": "request_retype",
    "anomaly_family": "combined_layout_and_repeat",
    "layout_direction": "thai_intended_english_active",
    "corruption_scope": "full_thai_script_plus_repeated_key",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "41_plus",
    "difficulty": "hard",
    "label_confidence": "high",
    "generation_note": "duplicated Thai base character 'ส'; then mapped Thai characters to English-key positions",
    "source_group": "general_llm",
    "source_case_id": "MB-1362-GL-037",
    "source_expected_category": [
      "general",
      "knowledge"
    ]
  },
  "actual": {
    "action": "request_retype",
    "detected_action": "request_retype",
    "applied_action": "request_retype",
    "should_retype": true,
    "flags": [
      "keyboard_layout_mismatch"
    ],
    "layout_score": 0.728602,
    "repeat_score": 0.443842,
    "guard_status": "flagged",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 4.86
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 26. legacy / KIA-0374 / Fortnite x6j,gx]ujpo preset 00vpdfvtwi

```json
{
  "id": "KIA-0374",
  "input": "Fortnite x6j,gx]ujpo preset 00vpdfvtwi",
  "expected": {
    "id": "KIA-0374",
    "split": "test",
    "observed_input": "Fortnite x6j,gx]ujpo preset 00vpdfvtwi",
    "canonical_question": "Fortnite ปุ่มเปลี่ยน preset จอยกดอะไร",
    "expected_flags": [
      "keyboard_layout_mismatch",
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": true,
    "should_detect_repeated_character": true,
    "should_block_answer": true,
    "expected_action": "request_retype",
    "anomaly_family": "combined_layout_and_repeat",
    "layout_direction": "thai_intended_english_active",
    "corruption_scope": "full_thai_script_plus_repeated_key",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "16_40",
    "difficulty": "hard",
    "label_confidence": "high",
    "generation_note": "duplicated Thai base character 'จ'; then mapped Thai characters to English-key positions",
    "source_group": "game_controls",
    "source_case_id": "MB-0278-GC-032",
    "source_expected_category": "games"
  },
  "actual": {
    "action": "request_retype",
    "detected_action": "request_retype",
    "applied_action": "request_retype",
    "should_retype": true,
    "flags": [
      "keyboard_layout_mismatch"
    ],
    "layout_score": 0.725955,
    "repeat_score": 0.478062,
    "guard_status": "flagged",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 2.001
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 27. legacy / KIA-0375 / Gaming Chair vp^jF::owso

```json
{
  "id": "KIA-0375",
  "input": "Gaming Chair vp^jF::owso",
  "expected": {
    "id": "KIA-0375",
    "split": "calibration",
    "observed_input": "Gaming Chair vp^jF::owso",
    "canonical_question": "Gaming Chair อยู่โซนไหน",
    "expected_flags": [
      "keyboard_layout_mismatch",
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": true,
    "should_detect_repeated_character": true,
    "should_block_answer": true,
    "expected_action": "request_retype",
    "anomaly_family": "combined_layout_and_repeat",
    "layout_direction": "thai_intended_english_active",
    "corruption_scope": "full_thai_script_plus_repeated_key",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "16_40",
    "difficulty": "hard",
    "label_confidence": "high",
    "generation_note": "duplicated Thai base character 'ซ' inside 'โซน'; then mapped Thai characters to English-key positions",
    "source_group": "equipment",
    "source_case_id": "MB-0428-E-027",
    "source_expected_category": [
      "equipment",
      "games"
    ]
  },
  "actual": {
    "action": "request_retype",
    "detected_action": "request_retype",
    "applied_action": "request_retype",
    "should_retype": true,
    "flags": [
      "keyboard_layout_mismatch"
    ],
    "layout_score": 0.473196,
    "repeat_score": 0.528719,
    "guard_status": "flagged",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 1.663
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 28. legacy / KIA-0379 / 8upN[viNf mechanical 8nvvtwic[[lyhoo 9v[gxHo4kKkwmp

```json
{
  "id": "KIA-0379",
  "input": "8upN[viNf mechanical 8nvvtwic[[lyhoo 9v[gxHo4kKkwmp",
  "expected": {
    "id": "KIA-0379",
    "split": "test",
    "observed_input": "8upN[viNf mechanical 8nvvtwic[[lyhoo 9v[gxHo4kKkwmp",
    "canonical_question": "คีย์บอร์ด mechanical คืออะไรแบบสั้น ตอบเป็นภาษาไทย",
    "expected_flags": [
      "keyboard_layout_mismatch",
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": true,
    "should_detect_repeated_character": true,
    "should_block_answer": true,
    "expected_action": "request_retype",
    "anomaly_family": "combined_layout_and_repeat",
    "layout_direction": "thai_intended_english_active",
    "corruption_scope": "full_thai_script_plus_repeated_key",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "41_plus",
    "difficulty": "hard",
    "label_confidence": "high",
    "generation_note": "duplicated Thai base character 'น'; then mapped Thai characters to English-key positions",
    "source_group": "general_llm",
    "source_case_id": "MB-1363-GL-038",
    "source_expected_category": [
      "general",
      "knowledge"
    ]
  },
  "actual": {
    "action": "request_retype",
    "detected_action": "request_retype",
    "applied_action": "request_retype",
    "should_retype": true,
    "flags": [
      "keyboard_layout_mismatch"
    ],
    "layout_score": 0.847515,
    "repeat_score": 0.512933,
    "guard_status": "flagged",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 3.783
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 29. legacy / KIA-0470 / วันนี้เปิดไหม???

```json
{
  "id": "KIA-0470",
  "input": "วันนี้เปิดไหม???",
  "expected": {
    "id": "KIA-0470",
    "split": "calibration",
    "observed_input": "วันนี้เปิดไหม???",
    "canonical_question": "วันนี้เปิดไหม???",
    "expected_flags": [],
    "should_detect_keyboard_layout": false,
    "should_detect_repeated_character": false,
    "should_block_answer": false,
    "expected_action": "continue",
    "anomaly_family": "valid_expressive_repetition",
    "layout_direction": null,
    "corruption_scope": "none",
    "repeat_interpretation": "expressive",
    "contains_adjacent_repeat": true,
    "length_band": "16_40",
    "difficulty": "hard",
    "label_confidence": "medium",
    "generation_note": "intentional chat-style elongation or repeated punctuation; must not be treated as an accidental key repeat",
    "source_group": "manual_edge_case",
    "source_case_id": null,
    "source_expected_category": null
  },
  "actual": {
    "action": "request_retype",
    "detected_action": "request_retype",
    "applied_action": "warn_and_continue",
    "should_retype": false,
    "flags": [
      "repeated_character_typo"
    ],
    "layout_score": 0.004502,
    "repeat_score": 0.560799,
    "guard_status": "flagged",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 1.181,
    "notice": "ข้อความนี้อาจมีตัวอักษรซ้ำโดยไม่ตั้งใจ กรุณาตรวจสอบและพิมพ์คำถามใหม่อีกครั้งครับ"
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 30. common / KIA-0018 / ;yoouhgxbfws,

```json
{
  "id": "KIA-0018",
  "input": ";yoouhgxbfws,",
  "expected": {
    "id": "KIA-0018",
    "split": "test",
    "observed_input": ";yoouhgxbfws,",
    "canonical_question": "วันนี้เปิดไหม",
    "expected_flags": [
      "keyboard_layout_mismatch"
    ],
    "should_detect_keyboard_layout": true,
    "should_detect_repeated_character": false,
    "should_block_answer": true,
    "expected_action": "request_retype",
    "anomaly_family": "layout_th_to_en_full",
    "layout_direction": "thai_intended_english_active",
    "corruption_scope": "full_thai_script",
    "repeat_interpretation": "none",
    "contains_adjacent_repeat": true,
    "length_band": "08_15",
    "difficulty": "medium",
    "label_confidence": "high",
    "generation_note": "manual short-query layout mismatch",
    "source_group": "manual_edge_case",
    "source_case_id": null,
    "source_expected_category": null
  },
  "actual": {
    "action": "request_retype",
    "detected_action": "request_retype",
    "applied_action": "request_retype",
    "should_retype": true,
    "flags": [
      "keyboard_layout_mismatch",
      "repeated_character_typo"
    ],
    "layout_score": 0.668508,
    "repeat_score": 0.560799,
    "guard_status": "flagged",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 1.884
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 31. common / KIA-0187 / เฟรมเรตกับความละเอียดดต่างกันยังไง ขอแบบเข้าใจง่าย

```json
{
  "id": "KIA-0187",
  "input": "เฟรมเรตกับความละเอียดดต่างกันยังไง ขอแบบเข้าใจง่าย",
  "expected": {
    "id": "KIA-0187",
    "split": "test",
    "observed_input": "เฟรมเรตกับความละเอียดดต่างกันยังไง ขอแบบเข้าใจง่าย",
    "canonical_question": "เฟรมเรตกับความละเอียดต่างกันยังไง ขอแบบเข้าใจง่าย",
    "expected_flags": [
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": false,
    "should_detect_repeated_character": true,
    "should_block_answer": false,
    "expected_action": "soft_flag_typo",
    "anomaly_family": "repeat_thai_internal",
    "layout_direction": null,
    "corruption_scope": "single_character_inside_thai_span",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "41_plus",
    "difficulty": "medium",
    "label_confidence": "high",
    "generation_note": "duplicated Thai base character 'ด'",
    "source_group": "general_llm",
    "source_case_id": "MB-1347-GL-022",
    "source_expected_category": [
      "general",
      "knowledge"
    ]
  },
  "actual": {
    "action": "continue",
    "detected_action": "continue",
    "applied_action": "continue",
    "should_retype": false,
    "flags": [],
    "layout_score": 0.005192,
    "repeat_score": 0.466557,
    "guard_status": "passed",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 3.169
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 32. common / KIA-0190 / PUBG อยู่โซซนไหน

```json
{
  "id": "KIA-0190",
  "input": "PUBG อยู่โซซนไหน",
  "expected": {
    "id": "KIA-0190",
    "split": "calibration",
    "observed_input": "PUBG อยู่โซซนไหน",
    "canonical_question": "PUBG อยู่โซนไหน",
    "expected_flags": [
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": false,
    "should_detect_repeated_character": true,
    "should_block_answer": false,
    "expected_action": "soft_flag_typo",
    "anomaly_family": "repeat_thai_internal",
    "layout_direction": null,
    "corruption_scope": "single_character_inside_thai_span",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "16_40",
    "difficulty": "medium",
    "label_confidence": "high",
    "generation_note": "duplicated Thai base character 'ซ' inside 'โซน'",
    "source_group": "availability_game",
    "source_case_id": "MB-0668-AG-015",
    "source_expected_category": "games"
  },
  "actual": {
    "action": "continue",
    "detected_action": "continue",
    "applied_action": "continue",
    "should_retype": false,
    "flags": [],
    "layout_score": 0.005488,
    "repeat_score": 0.528719,
    "guard_status": "passed",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 1.209
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 33. common / KIA-0192 / Gaming PC รุ่น MSI MAG Infinite S3 14th อยู่โซซนไหน

```json
{
  "id": "KIA-0192",
  "input": "Gaming PC รุ่น MSI MAG Infinite S3 14th อยู่โซซนไหน",
  "expected": {
    "id": "KIA-0192",
    "split": "test",
    "observed_input": "Gaming PC รุ่น MSI MAG Infinite S3 14th อยู่โซซนไหน",
    "canonical_question": "Gaming PC รุ่น MSI MAG Infinite S3 14th อยู่โซนไหน",
    "expected_flags": [
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": false,
    "should_detect_repeated_character": true,
    "should_block_answer": false,
    "expected_action": "soft_flag_typo",
    "anomaly_family": "repeat_thai_internal",
    "layout_direction": null,
    "corruption_scope": "single_character_inside_thai_span",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "41_plus",
    "difficulty": "medium",
    "label_confidence": "high",
    "generation_note": "duplicated Thai base character 'ซ' inside 'โซน'",
    "source_group": "equipment",
    "source_case_id": "MB-0413-E-012",
    "source_expected_category": [
      "equipment",
      "games"
    ]
  },
  "actual": {
    "action": "continue",
    "detected_action": "continue",
    "applied_action": "continue",
    "should_retype": false,
    "flags": [],
    "layout_score": 0.005488,
    "repeat_score": 0.528719,
    "guard_status": "passed",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 4.473
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 34. common / KIA-0194 / VALORANT ถ้าใช้ bug จะโดดนอะไร

```json
{
  "id": "KIA-0194",
  "input": "VALORANT ถ้าใช้ bug จะโดดนอะไร",
  "expected": {
    "id": "KIA-0194",
    "split": "test",
    "observed_input": "VALORANT ถ้าใช้ bug จะโดดนอะไร",
    "canonical_question": "VALORANT ถ้าใช้ bug จะโดนอะไร",
    "expected_flags": [
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": false,
    "should_detect_repeated_character": true,
    "should_block_answer": false,
    "expected_action": "soft_flag_typo",
    "anomaly_family": "repeat_thai_internal",
    "layout_direction": null,
    "corruption_scope": "single_character_inside_thai_span",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "16_40",
    "difficulty": "medium",
    "label_confidence": "high",
    "generation_note": "duplicated Thai base character 'ด'",
    "source_group": "competition_rules",
    "source_case_id": "MB-0547-CR-011",
    "source_expected_category": "competition_rules"
  },
  "actual": {
    "action": "continue",
    "detected_action": "continue",
    "applied_action": "continue",
    "should_retype": false,
    "flags": [],
    "layout_score": 0.005143,
    "repeat_score": 0.548758,
    "guard_status": "passed",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 2.282
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 35. common / KIA-0204 / Counter-Strike 2 ใช้จออยยังไง

```json
{
  "id": "KIA-0204",
  "input": "Counter-Strike 2 ใช้จออยยังไง",
  "expected": {
    "id": "KIA-0204",
    "split": "test",
    "observed_input": "Counter-Strike 2 ใช้จออยยังไง",
    "canonical_question": "Counter-Strike 2 ใช้จอยยังไง",
    "expected_flags": [
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": false,
    "should_detect_repeated_character": true,
    "should_block_answer": false,
    "expected_action": "soft_flag_typo",
    "anomaly_family": "repeat_thai_internal",
    "layout_direction": null,
    "corruption_scope": "single_character_inside_thai_span",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "16_40",
    "difficulty": "medium",
    "label_confidence": "high",
    "generation_note": "duplicated Thai base character 'อ'",
    "source_group": "game_controls",
    "source_case_id": "MB-0264-GC-018",
    "source_expected_category": "games"
  },
  "actual": {
    "action": "continue",
    "detected_action": "continue",
    "applied_action": "continue",
    "should_retype": false,
    "flags": [],
    "layout_score": 0.001927,
    "repeat_score": 0.522255,
    "guard_status": "passed",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 1.822
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 36. common / KIA-0226 / ช่วยสรุปวิธีพูดขอบคุณณแบบสุภาพ 2 ประโยค ขอแบบเข้าใจง่าย

```json
{
  "id": "KIA-0226",
  "input": "ช่วยสรุปวิธีพูดขอบคุณณแบบสุภาพ 2 ประโยค ขอแบบเข้าใจง่าย",
  "expected": {
    "id": "KIA-0226",
    "split": "test",
    "observed_input": "ช่วยสรุปวิธีพูดขอบคุณณแบบสุภาพ 2 ประโยค ขอแบบเข้าใจง่าย",
    "canonical_question": "ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ขอแบบเข้าใจง่าย",
    "expected_flags": [
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": false,
    "should_detect_repeated_character": true,
    "should_block_answer": false,
    "expected_action": "soft_flag_typo",
    "anomaly_family": "repeat_thai_internal",
    "layout_direction": null,
    "corruption_scope": "single_character_inside_thai_span",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "41_plus",
    "difficulty": "medium",
    "label_confidence": "high",
    "generation_note": "duplicated Thai base character 'ณ'",
    "source_group": "general_llm",
    "source_case_id": "MB-1350-GL-025",
    "source_expected_category": [
      "general",
      "knowledge"
    ]
  },
  "actual": {
    "action": "continue",
    "detected_action": "continue",
    "applied_action": "continue",
    "should_retype": false,
    "flags": [],
    "layout_score": 0.005413,
    "repeat_score": 0.510341,
    "guard_status": "passed",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 3.114
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 37. common / KIA-0231 / Gaming Monitor อยู่โซซนไหน

```json
{
  "id": "KIA-0231",
  "input": "Gaming Monitor อยู่โซซนไหน",
  "expected": {
    "id": "KIA-0231",
    "split": "test",
    "observed_input": "Gaming Monitor อยู่โซซนไหน",
    "canonical_question": "Gaming Monitor อยู่โซนไหน",
    "expected_flags": [
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": false,
    "should_detect_repeated_character": true,
    "should_block_answer": false,
    "expected_action": "soft_flag_typo",
    "anomaly_family": "repeat_thai_internal",
    "layout_direction": null,
    "corruption_scope": "single_character_inside_thai_span",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "16_40",
    "difficulty": "medium",
    "label_confidence": "high",
    "generation_note": "duplicated Thai base character 'ซ' inside 'โซน'",
    "source_group": "equipment",
    "source_case_id": "MB-0416-E-015",
    "source_expected_category": [
      "equipment",
      "games"
    ]
  },
  "actual": {
    "action": "continue",
    "detected_action": "continue",
    "applied_action": "continue",
    "should_retype": false,
    "flags": [],
    "layout_score": 0.012333,
    "repeat_score": 0.528719,
    "guard_status": "passed",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 3.653
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 38. common / KIA-0242 / VALORANT อยู่โโซนไหน

```json
{
  "id": "KIA-0242",
  "input": "VALORANT อยู่โโซนไหน",
  "expected": {
    "id": "KIA-0242",
    "split": "test",
    "observed_input": "VALORANT อยู่โโซนไหน",
    "canonical_question": "VALORANT อยู่โซนไหน",
    "expected_flags": [
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": false,
    "should_detect_repeated_character": true,
    "should_block_answer": false,
    "expected_action": "soft_flag_typo",
    "anomaly_family": "repeat_thai_mark_or_vowel",
    "layout_direction": null,
    "corruption_scope": "thai_vowel_or_tone_mark",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "16_40",
    "difficulty": "hard",
    "label_confidence": "high",
    "generation_note": "duplicated Thai vowel/tone character 'โ'",
    "source_group": "availability_game",
    "source_case_id": "MB-0672-AG-019",
    "source_expected_category": "games"
  },
  "actual": {
    "action": "continue",
    "detected_action": "continue",
    "applied_action": "continue",
    "should_retype": false,
    "flags": [],
    "layout_score": 0.005472,
    "repeat_score": 0.525782,
    "guard_status": "passed",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 2.192
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 39. common / KIA-0252 / เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาาพหนึ่งประโยค ขอแบบเข้าใจง่าย

```json
{
  "id": "KIA-0252",
  "input": "เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาาพหนึ่งประโยค ขอแบบเข้าใจง่าย",
  "expected": {
    "id": "KIA-0252",
    "split": "test",
    "observed_input": "เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาาพหนึ่งประโยค ขอแบบเข้าใจง่าย",
    "canonical_question": "เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาพหนึ่งประโยค ขอแบบเข้าใจง่าย",
    "expected_flags": [
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": false,
    "should_detect_repeated_character": true,
    "should_block_answer": false,
    "expected_action": "soft_flag_typo",
    "anomaly_family": "repeat_thai_mark_or_vowel",
    "layout_direction": null,
    "corruption_scope": "thai_vowel_or_tone_mark",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "41_plus",
    "difficulty": "hard",
    "label_confidence": "high",
    "generation_note": "duplicated Thai vowel/tone character 'า'",
    "source_group": "general_llm",
    "source_case_id": "MB-1352-GL-027",
    "source_expected_category": [
      "general",
      "knowledge"
    ]
  },
  "actual": {
    "action": "continue",
    "detected_action": "continue",
    "applied_action": "continue",
    "should_retype": false,
    "flags": [],
    "layout_score": 0.005611,
    "repeat_score": 0.531295,
    "guard_status": "passed",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 5.621
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 40. common / KIA-0261 / PS5 ราคาเท่าไหร่ แแล้วมีเกมอะไรบ้าง

```json
{
  "id": "KIA-0261",
  "input": "PS5 ราคาเท่าไหร่ แแล้วมีเกมอะไรบ้าง",
  "expected": {
    "id": "KIA-0261",
    "split": "test",
    "observed_input": "PS5 ราคาเท่าไหร่ แแล้วมีเกมอะไรบ้าง",
    "canonical_question": "PS5 ราคาเท่าไหร่ แล้วมีเกมอะไรบ้าง",
    "expected_flags": [
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": false,
    "should_detect_repeated_character": true,
    "should_block_answer": false,
    "expected_action": "soft_flag_typo",
    "anomaly_family": "repeat_thai_mark_or_vowel",
    "layout_direction": null,
    "corruption_scope": "thai_vowel_or_tone_mark",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "16_40",
    "difficulty": "hard",
    "label_confidence": "high",
    "generation_note": "duplicated Thai vowel/tone character 'แ'",
    "source_group": "compound",
    "source_case_id": "MB-1254-C-018",
    "source_expected_category": "multi_question"
  },
  "actual": {
    "action": "continue",
    "detected_action": "continue",
    "applied_action": "continue",
    "should_retype": false,
    "flags": [],
    "layout_score": 0.005266,
    "repeat_score": 0.472115,
    "guard_status": "passed",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 2.171
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 41. common / KIA-0270 / Gaming Keyboard อยู่โโซนไหน

```json
{
  "id": "KIA-0270",
  "input": "Gaming Keyboard อยู่โโซนไหน",
  "expected": {
    "id": "KIA-0270",
    "split": "calibration",
    "observed_input": "Gaming Keyboard อยู่โโซนไหน",
    "canonical_question": "Gaming Keyboard อยู่โซนไหน",
    "expected_flags": [
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": false,
    "should_detect_repeated_character": true,
    "should_block_answer": false,
    "expected_action": "soft_flag_typo",
    "anomaly_family": "repeat_thai_mark_or_vowel",
    "layout_direction": null,
    "corruption_scope": "thai_vowel_or_tone_mark",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "16_40",
    "difficulty": "hard",
    "label_confidence": "high",
    "generation_note": "duplicated Thai vowel/tone character 'โ'",
    "source_group": "equipment",
    "source_case_id": "MB-0419-E-018",
    "source_expected_category": [
      "equipment",
      "games"
    ]
  },
  "actual": {
    "action": "continue",
    "detected_action": "continue",
    "applied_action": "continue",
    "should_retype": false,
    "flags": [],
    "layout_score": 0.005472,
    "repeat_score": 0.525782,
    "guard_status": "passed",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 1.589
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 42. common / KIA-0277 / วันนี้มีข่าาว esports อะไรล่าสุด

```json
{
  "id": "KIA-0277",
  "input": "วันนี้มีข่าาว esports อะไรล่าสุด",
  "expected": {
    "id": "KIA-0277",
    "split": "test",
    "observed_input": "วันนี้มีข่าาว esports อะไรล่าสุด",
    "canonical_question": "วันนี้มีข่าว esports อะไรล่าสุด",
    "expected_flags": [
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": false,
    "should_detect_repeated_character": true,
    "should_block_answer": false,
    "expected_action": "soft_flag_typo",
    "anomaly_family": "repeat_thai_mark_or_vowel",
    "layout_direction": null,
    "corruption_scope": "thai_vowel_or_tone_mark",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "16_40",
    "difficulty": "hard",
    "label_confidence": "high",
    "generation_note": "duplicated Thai vowel/tone character 'า'",
    "source_group": "ambiguity_no_answer",
    "source_case_id": "MB-0648-ANA-022",
    "source_expected_category": [
      "no_answer",
      "games",
      "general"
    ]
  },
  "actual": {
    "action": "continue",
    "detected_action": "continue",
    "applied_action": "continue",
    "should_retype": false,
    "flags": [],
    "layout_score": 0.012269,
    "repeat_score": 0.522849,
    "guard_status": "passed",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 2.315
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 43. common / KIA-0310 / กี่บบาท

```json
{
  "id": "KIA-0310",
  "input": "กี่บบาท",
  "expected": {
    "id": "KIA-0310",
    "split": "calibration",
    "observed_input": "กี่บบาท",
    "canonical_question": "กี่บาท",
    "expected_flags": [
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": false,
    "should_detect_repeated_character": true,
    "should_block_answer": false,
    "expected_action": "soft_flag_typo",
    "anomaly_family": "repeat_short_token",
    "layout_direction": null,
    "corruption_scope": "short_query_or_token",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "04_07",
    "difficulty": "hard",
    "label_confidence": "high",
    "generation_note": "manual short repeated-character case: thai_consonant",
    "source_group": "manual_edge_case",
    "source_case_id": null,
    "source_expected_category": null
  },
  "actual": {
    "action": "continue",
    "detected_action": "continue",
    "applied_action": "continue",
    "should_retype": false,
    "flags": [],
    "layout_score": 0.005246,
    "repeat_score": 0.51247,
    "guard_status": "passed",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 0.834
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 44. common / KIA-0320 / เกมอะไรร

```json
{
  "id": "KIA-0320",
  "input": "เกมอะไรร",
  "expected": {
    "id": "KIA-0320",
    "split": "calibration",
    "observed_input": "เกมอะไรร",
    "canonical_question": "เกมอะไร",
    "expected_flags": [
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": false,
    "should_detect_repeated_character": true,
    "should_block_answer": false,
    "expected_action": "soft_flag_typo",
    "anomaly_family": "repeat_short_token",
    "layout_direction": null,
    "corruption_scope": "short_query_or_token",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "08_15",
    "difficulty": "hard",
    "label_confidence": "high",
    "generation_note": "manual short repeated-character case: thai_consonant",
    "source_group": "manual_edge_case",
    "source_case_id": null,
    "source_expected_category": null
  },
  "actual": {
    "action": "continue",
    "detected_action": "continue",
    "applied_action": "continue",
    "should_retype": false,
    "flags": [],
    "layout_score": 0.007406,
    "repeat_score": 0.509828,
    "guard_status": "passed",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 1.037
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 45. common / KIA-0332 / TEKKEN 8 dy[ Resident Evil Village ,ux6j,,vtwi[hk'

```json
{
  "id": "KIA-0332",
  "input": "TEKKEN 8 dy[ Resident Evil Village ,ux6j,,vtwi[hk'",
  "expected": {
    "id": "KIA-0332",
    "split": "test",
    "observed_input": "TEKKEN 8 dy[ Resident Evil Village ,ux6j,,vtwi[hk'",
    "canonical_question": "TEKKEN 8 กับ Resident Evil Village มีปุ่มอะไรบ้าง",
    "expected_flags": [
      "keyboard_layout_mismatch",
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": true,
    "should_detect_repeated_character": true,
    "should_block_answer": true,
    "expected_action": "request_retype",
    "anomaly_family": "combined_layout_and_repeat",
    "layout_direction": "thai_intended_english_active",
    "corruption_scope": "full_thai_script_plus_repeated_key",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "41_plus",
    "difficulty": "hard",
    "label_confidence": "high",
    "generation_note": "duplicated Thai base character 'ม'; then mapped Thai characters to English-key positions",
    "source_group": "compound",
    "source_case_id": "MB-1261-C-025",
    "source_expected_category": [
      "games",
      "multi_question"
    ]
  },
  "actual": {
    "action": "request_retype",
    "detected_action": "request_retype",
    "applied_action": "request_retype",
    "should_retype": true,
    "flags": [
      "keyboard_layout_mismatch"
    ],
    "layout_score": 0.823518,
    "repeat_score": 0.546227,
    "guard_status": "flagged",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 4.117
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 46. common / KIA-0340 / Counter3Strike 2 ,klkp0tFffovtwi

```json
{
  "id": "KIA-0340",
  "input": "Counter3Strike 2 ,klkp0tFffovtwi",
  "expected": {
    "id": "KIA-0340",
    "split": "calibration",
    "observed_input": "Counter3Strike 2 ,klkp0tFffovtwi",
    "canonical_question": "Counter-Strike 2 มาสายจะโดนอะไร",
    "expected_flags": [
      "keyboard_layout_mismatch",
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": true,
    "should_detect_repeated_character": true,
    "should_block_answer": true,
    "expected_action": "request_retype",
    "anomaly_family": "combined_layout_and_repeat",
    "layout_direction": "thai_intended_english_active",
    "corruption_scope": "full_thai_script_plus_repeated_key",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "16_40",
    "difficulty": "hard",
    "label_confidence": "high",
    "generation_note": "duplicated Thai base character 'ด'; then mapped Thai characters to English-key positions",
    "source_group": "competition_rules",
    "source_case_id": "MB-0569-CR-033",
    "source_expected_category": "competition_rules"
  },
  "actual": {
    "action": "request_retype",
    "detected_action": "request_retype",
    "applied_action": "request_retype",
    "should_retype": true,
    "flags": [
      "keyboard_layout_mismatch"
    ],
    "layout_score": 0.565078,
    "repeat_score": 0.54432,
    "guard_status": "flagged",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 1.597
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 47. common / KIA-0348 / Gaming Headset vp^jF::owso

```json
{
  "id": "KIA-0348",
  "input": "Gaming Headset vp^jF::owso",
  "expected": {
    "id": "KIA-0348",
    "split": "test",
    "observed_input": "Gaming Headset vp^jF::owso",
    "canonical_question": "Gaming Headset อยู่โซนไหน",
    "expected_flags": [
      "keyboard_layout_mismatch",
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": true,
    "should_detect_repeated_character": true,
    "should_block_answer": true,
    "expected_action": "request_retype",
    "anomaly_family": "combined_layout_and_repeat",
    "layout_direction": "thai_intended_english_active",
    "corruption_scope": "full_thai_script_plus_repeated_key",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "16_40",
    "difficulty": "hard",
    "label_confidence": "high",
    "generation_note": "duplicated Thai base character 'ซ' inside 'โซน'; then mapped Thai characters to English-key positions",
    "source_group": "equipment",
    "source_case_id": "MB-0425-E-024",
    "source_expected_category": [
      "equipment",
      "games"
    ]
  },
  "actual": {
    "action": "request_retype",
    "detected_action": "request_retype",
    "applied_action": "request_retype",
    "should_retype": true,
    "flags": [
      "keyboard_layout_mismatch"
    ],
    "layout_score": 0.470279,
    "repeat_score": 0.528719,
    "guard_status": "flagged",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 1.482
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 48. common / KIA-0351 / Gran Turismo 7 dy[ Overcooked! 2 ,ux6j,,vtwi[hk'

```json
{
  "id": "KIA-0351",
  "input": "Gran Turismo 7 dy[ Overcooked! 2 ,ux6j,,vtwi[hk'",
  "expected": {
    "id": "KIA-0351",
    "split": "test",
    "observed_input": "Gran Turismo 7 dy[ Overcooked! 2 ,ux6j,,vtwi[hk'",
    "canonical_question": "Gran Turismo 7 กับ Overcooked! 2 มีปุ่มอะไรบ้าง",
    "expected_flags": [
      "keyboard_layout_mismatch",
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": true,
    "should_detect_repeated_character": true,
    "should_block_answer": true,
    "expected_action": "request_retype",
    "anomaly_family": "combined_layout_and_repeat",
    "layout_direction": "thai_intended_english_active",
    "corruption_scope": "full_thai_script_plus_repeated_key",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "41_plus",
    "difficulty": "hard",
    "label_confidence": "high",
    "generation_note": "duplicated Thai base character 'ม'; then mapped Thai characters to English-key positions",
    "source_group": "compound",
    "source_case_id": "MB-1263-C-027",
    "source_expected_category": [
      "games",
      "multi_question"
    ]
  },
  "actual": {
    "action": "request_retype",
    "detected_action": "request_retype",
    "applied_action": "request_retype",
    "should_retype": true,
    "flags": [
      "keyboard_layout_mismatch"
    ],
    "layout_score": 0.823745,
    "repeat_score": 0.546227,
    "guard_status": "flagged",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 2.626
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 49. common / KIA-0352 / =j;pli6x;bTur^f-v[86Ic[[ll64kr 2 xitFp8 9v[gxHo4kKkwmp

```json
{
  "id": "KIA-0352",
  "input": "=j;pli6x;bTur^f-v[86Ic[[ll64kr 2 xitFp8 9v[gxHo4kKkwmp",
  "expected": {
    "id": "KIA-0352",
    "split": "test",
    "observed_input": "=j;pli6x;bTur^f-v[86Ic[[ll64kr 2 xitFp8 9v[gxHo4kKkwmp",
    "canonical_question": "ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ตอบเป็นภาษาไทย",
    "expected_flags": [
      "keyboard_layout_mismatch",
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": true,
    "should_detect_repeated_character": true,
    "should_block_answer": true,
    "expected_action": "request_retype",
    "anomaly_family": "combined_layout_and_repeat",
    "layout_direction": "thai_intended_english_active",
    "corruption_scope": "full_thai_script_plus_repeated_key",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "41_plus",
    "difficulty": "hard",
    "label_confidence": "high",
    "generation_note": "duplicated Thai base character 'ส'; then mapped Thai characters to English-key positions",
    "source_group": "general_llm",
    "source_case_id": "MB-1360-GL-035",
    "source_expected_category": [
      "general",
      "knowledge"
    ]
  },
  "actual": {
    "action": "request_retype",
    "detected_action": "request_retype",
    "applied_action": "request_retype",
    "should_retype": true,
    "flags": [
      "keyboard_layout_mismatch"
    ],
    "layout_score": 0.652818,
    "repeat_score": 0.503353,
    "guard_status": "flagged",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 2.677
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 50. common / KIA-0356 / Fortnite .=h0vvppy'w'

```json
{
  "id": "KIA-0356",
  "input": "Fortnite .=h0vvppy'w'",
  "expected": {
    "id": "KIA-0356",
    "split": "test",
    "observed_input": "Fortnite .=h0vvppy'w'",
    "canonical_question": "Fortnite ใช้จอยยังไง",
    "expected_flags": [
      "keyboard_layout_mismatch",
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": true,
    "should_detect_repeated_character": true,
    "should_block_answer": true,
    "expected_action": "request_retype",
    "anomaly_family": "combined_layout_and_repeat",
    "layout_direction": "thai_intended_english_active",
    "corruption_scope": "full_thai_script_plus_repeated_key",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "16_40",
    "difficulty": "hard",
    "label_confidence": "high",
    "generation_note": "duplicated Thai base character 'อ'; then mapped Thai characters to English-key positions",
    "source_group": "game_controls",
    "source_case_id": "MB-0276-GC-030",
    "source_expected_category": "games"
  },
  "actual": {
    "action": "request_retype",
    "detected_action": "request_retype",
    "applied_action": "request_retype",
    "should_retype": true,
    "flags": [
      "keyboard_layout_mismatch"
    ],
    "layout_score": 0.534856,
    "repeat_score": 0.522255,
    "guard_status": "flagged",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 2.246
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 51. common / KIA-0361 / cx]8e;jk reservation gxHo4kKkwmpp 9v[gxHo4kKkwmp

```json
{
  "id": "KIA-0361",
  "input": "cx]8e;jk reservation gxHo4kKkwmpp 9v[gxHo4kKkwmp",
  "expected": {
    "id": "KIA-0361",
    "split": "test",
    "observed_input": "cx]8e;jk reservation gxHo4kKkwmpp 9v[gxHo4kKkwmp",
    "canonical_question": "แปลคำว่า reservation เป็นภาษาไทย ตอบเป็นภาษาไทย",
    "expected_flags": [
      "keyboard_layout_mismatch",
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": true,
    "should_detect_repeated_character": true,
    "should_block_answer": true,
    "expected_action": "request_retype",
    "anomaly_family": "combined_layout_and_repeat",
    "layout_direction": "thai_intended_english_active",
    "corruption_scope": "full_thai_script_plus_repeated_key",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "41_plus",
    "difficulty": "hard",
    "label_confidence": "high",
    "generation_note": "duplicated Thai base character 'ย'; then mapped Thai characters to English-key positions",
    "source_group": "general_llm",
    "source_case_id": "MB-1361-GL-036",
    "source_expected_category": [
      "general",
      "knowledge"
    ]
  },
  "actual": {
    "action": "request_retype",
    "detected_action": "request_retype",
    "applied_action": "request_retype",
    "should_retype": true,
    "flags": [
      "keyboard_layout_mismatch"
    ],
    "layout_score": 0.699046,
    "repeat_score": 0.52036,
    "guard_status": "flagged",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 2.987
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 52. common / KIA-0364 / Delta Force vp^jF::owso

```json
{
  "id": "KIA-0364",
  "input": "Delta Force vp^jF::owso",
  "expected": {
    "id": "KIA-0364",
    "split": "test",
    "observed_input": "Delta Force vp^jF::owso",
    "canonical_question": "Delta Force อยู่โซนไหน",
    "expected_flags": [
      "keyboard_layout_mismatch",
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": true,
    "should_detect_repeated_character": true,
    "should_block_answer": true,
    "expected_action": "request_retype",
    "anomaly_family": "combined_layout_and_repeat",
    "layout_direction": "thai_intended_english_active",
    "corruption_scope": "full_thai_script_plus_repeated_key",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "16_40",
    "difficulty": "hard",
    "label_confidence": "high",
    "generation_note": "duplicated Thai base character 'ซ' inside 'โซน'; then mapped Thai characters to English-key positions",
    "source_group": "availability_game",
    "source_case_id": "MB-0687-AG-029",
    "source_expected_category": "games"
  },
  "actual": {
    "action": "request_retype",
    "detected_action": "request_retype",
    "applied_action": "request_retype",
    "should_retype": true,
    "flags": [
      "keyboard_layout_mismatch"
    ],
    "layout_score": 0.474863,
    "repeat_score": 0.528719,
    "guard_status": "flagged",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 1.801
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 53. common / KIA-0369 / Beat Saber dy[ VALORANT ,ux6j,,vtwi[hk'

```json
{
  "id": "KIA-0369",
  "input": "Beat Saber dy[ VALORANT ,ux6j,,vtwi[hk'",
  "expected": {
    "id": "KIA-0369",
    "split": "test",
    "observed_input": "Beat Saber dy[ VALORANT ,ux6j,,vtwi[hk'",
    "canonical_question": "Beat Saber กับ VALORANT มีปุ่มอะไรบ้าง",
    "expected_flags": [
      "keyboard_layout_mismatch",
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": true,
    "should_detect_repeated_character": true,
    "should_block_answer": true,
    "expected_action": "request_retype",
    "anomaly_family": "combined_layout_and_repeat",
    "layout_direction": "thai_intended_english_active",
    "corruption_scope": "full_thai_script_plus_repeated_key",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "16_40",
    "difficulty": "hard",
    "label_confidence": "high",
    "generation_note": "duplicated Thai base character 'ม'; then mapped Thai characters to English-key positions",
    "source_group": "compound",
    "source_case_id": "MB-1265-C-029",
    "source_expected_category": [
      "games",
      "multi_question"
    ]
  },
  "actual": {
    "action": "request_retype",
    "detected_action": "request_retype",
    "applied_action": "request_retype",
    "should_retype": true,
    "flags": [
      "keyboard_layout_mismatch"
    ],
    "layout_score": 0.824745,
    "repeat_score": 0.546227,
    "guard_status": "flagged",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 2.204
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 54. common / KIA-0370 / g-upoxitFp8xit=kly,ryoTNdb0dii,c[[ll64krso7j'xitFp8 9v[gxHo4kKkwmp

```json
{
  "id": "KIA-0370",
  "input": "g-upoxitFp8xit=kly,ryoTNdb0dii,c[[ll64krso7j'xitFp8 9v[gxHo4kKkwmp",
  "expected": {
    "id": "KIA-0370",
    "split": "calibration",
    "observed_input": "g-upoxitFp8xit=kly,ryoTNdb0dii,c[[ll64krso7j'xitFp8 9v[gxHo4kKkwmp",
    "canonical_question": "เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาพหนึ่งประโยค ตอบเป็นภาษาไทย",
    "expected_flags": [
      "keyboard_layout_mismatch",
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": true,
    "should_detect_repeated_character": true,
    "should_block_answer": true,
    "expected_action": "request_retype",
    "anomaly_family": "combined_layout_and_repeat",
    "layout_direction": "thai_intended_english_active",
    "corruption_scope": "full_thai_script_plus_repeated_key",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "41_plus",
    "difficulty": "hard",
    "label_confidence": "high",
    "generation_note": "duplicated Thai base character 'ส'; then mapped Thai characters to English-key positions",
    "source_group": "general_llm",
    "source_case_id": "MB-1362-GL-037",
    "source_expected_category": [
      "general",
      "knowledge"
    ]
  },
  "actual": {
    "action": "request_retype",
    "detected_action": "request_retype",
    "applied_action": "request_retype",
    "should_retype": true,
    "flags": [
      "keyboard_layout_mismatch"
    ],
    "layout_score": 0.728602,
    "repeat_score": 0.443842,
    "guard_status": "flagged",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 5.991
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 55. common / KIA-0374 / Fortnite x6j,gx]ujpo preset 00vpdfvtwi

```json
{
  "id": "KIA-0374",
  "input": "Fortnite x6j,gx]ujpo preset 00vpdfvtwi",
  "expected": {
    "id": "KIA-0374",
    "split": "test",
    "observed_input": "Fortnite x6j,gx]ujpo preset 00vpdfvtwi",
    "canonical_question": "Fortnite ปุ่มเปลี่ยน preset จอยกดอะไร",
    "expected_flags": [
      "keyboard_layout_mismatch",
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": true,
    "should_detect_repeated_character": true,
    "should_block_answer": true,
    "expected_action": "request_retype",
    "anomaly_family": "combined_layout_and_repeat",
    "layout_direction": "thai_intended_english_active",
    "corruption_scope": "full_thai_script_plus_repeated_key",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "16_40",
    "difficulty": "hard",
    "label_confidence": "high",
    "generation_note": "duplicated Thai base character 'จ'; then mapped Thai characters to English-key positions",
    "source_group": "game_controls",
    "source_case_id": "MB-0278-GC-032",
    "source_expected_category": "games"
  },
  "actual": {
    "action": "request_retype",
    "detected_action": "request_retype",
    "applied_action": "request_retype",
    "should_retype": true,
    "flags": [
      "keyboard_layout_mismatch"
    ],
    "layout_score": 0.725955,
    "repeat_score": 0.478062,
    "guard_status": "flagged",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 1.972
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 56. common / KIA-0375 / Gaming Chair vp^jF::owso

```json
{
  "id": "KIA-0375",
  "input": "Gaming Chair vp^jF::owso",
  "expected": {
    "id": "KIA-0375",
    "split": "calibration",
    "observed_input": "Gaming Chair vp^jF::owso",
    "canonical_question": "Gaming Chair อยู่โซนไหน",
    "expected_flags": [
      "keyboard_layout_mismatch",
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": true,
    "should_detect_repeated_character": true,
    "should_block_answer": true,
    "expected_action": "request_retype",
    "anomaly_family": "combined_layout_and_repeat",
    "layout_direction": "thai_intended_english_active",
    "corruption_scope": "full_thai_script_plus_repeated_key",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "16_40",
    "difficulty": "hard",
    "label_confidence": "high",
    "generation_note": "duplicated Thai base character 'ซ' inside 'โซน'; then mapped Thai characters to English-key positions",
    "source_group": "equipment",
    "source_case_id": "MB-0428-E-027",
    "source_expected_category": [
      "equipment",
      "games"
    ]
  },
  "actual": {
    "action": "request_retype",
    "detected_action": "request_retype",
    "applied_action": "request_retype",
    "should_retype": true,
    "flags": [
      "keyboard_layout_mismatch"
    ],
    "layout_score": 0.473196,
    "repeat_score": 0.528719,
    "guard_status": "flagged",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 1.57
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 57. common / KIA-0379 / 8upN[viNf mechanical 8nvvtwic[[lyhoo 9v[gxHo4kKkwmp

```json
{
  "id": "KIA-0379",
  "input": "8upN[viNf mechanical 8nvvtwic[[lyhoo 9v[gxHo4kKkwmp",
  "expected": {
    "id": "KIA-0379",
    "split": "test",
    "observed_input": "8upN[viNf mechanical 8nvvtwic[[lyhoo 9v[gxHo4kKkwmp",
    "canonical_question": "คีย์บอร์ด mechanical คืออะไรแบบสั้น ตอบเป็นภาษาไทย",
    "expected_flags": [
      "keyboard_layout_mismatch",
      "repeated_character_typo"
    ],
    "should_detect_keyboard_layout": true,
    "should_detect_repeated_character": true,
    "should_block_answer": true,
    "expected_action": "request_retype",
    "anomaly_family": "combined_layout_and_repeat",
    "layout_direction": "thai_intended_english_active",
    "corruption_scope": "full_thai_script_plus_repeated_key",
    "repeat_interpretation": "accidental",
    "contains_adjacent_repeat": true,
    "length_band": "41_plus",
    "difficulty": "hard",
    "label_confidence": "high",
    "generation_note": "duplicated Thai base character 'น'; then mapped Thai characters to English-key positions",
    "source_group": "general_llm",
    "source_case_id": "MB-1363-GL-038",
    "source_expected_category": [
      "general",
      "knowledge"
    ]
  },
  "actual": {
    "action": "request_retype",
    "detected_action": "request_retype",
    "applied_action": "request_retype",
    "should_retype": true,
    "flags": [
      "keyboard_layout_mismatch"
    ],
    "layout_score": 0.847515,
    "repeat_score": 0.512933,
    "guard_status": "flagged",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 3.421
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```

## 58. common / KIA-0470 / วันนี้เปิดไหม???

```json
{
  "id": "KIA-0470",
  "input": "วันนี้เปิดไหม???",
  "expected": {
    "id": "KIA-0470",
    "split": "calibration",
    "observed_input": "วันนี้เปิดไหม???",
    "canonical_question": "วันนี้เปิดไหม???",
    "expected_flags": [],
    "should_detect_keyboard_layout": false,
    "should_detect_repeated_character": false,
    "should_block_answer": false,
    "expected_action": "continue",
    "anomaly_family": "valid_expressive_repetition",
    "layout_direction": null,
    "corruption_scope": "none",
    "repeat_interpretation": "expressive",
    "contains_adjacent_repeat": true,
    "length_band": "16_40",
    "difficulty": "hard",
    "label_confidence": "medium",
    "generation_note": "intentional chat-style elongation or repeated punctuation; must not be treated as an accidental key repeat",
    "source_group": "manual_edge_case",
    "source_case_id": null,
    "source_expected_category": null
  },
  "actual": {
    "action": "request_retype",
    "detected_action": "request_retype",
    "applied_action": "warn_and_continue",
    "should_retype": false,
    "flags": [
      "repeated_character_typo"
    ],
    "layout_score": 0.004502,
    "repeat_score": 0.560799,
    "guard_status": "flagged",
    "guard_mode": "enforce",
    "repeat_policy": "warn_and_continue",
    "profile_version": "keyboard-profile-v1:2a863a4176572043",
    "guard_elapsed_ms": 1.183,
    "notice": "ข้อความนี้อาจมีตัวอักษรซ้ำโดยไม่ตั้งใจ กรุณาตรวจสอบและพิมพ์คำถามใหม่อีกครั้งครับ"
  },
  "layout_match": true,
  "repeat_match": false,
  "legacy_block_policy_match": true
}
```
