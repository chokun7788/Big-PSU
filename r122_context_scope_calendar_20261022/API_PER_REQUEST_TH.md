# R122 revision02 — คำถามเดิมผ่าน API จริง

8 คำถามต่อแขน ใช้ Flow และฐานข้อมูลเดียวกัน เปลี่ยน adapter เฉพาะ context stage; คำถามเคยใช้พัฒนาแล้ว จึงไม่ใช่ fresh holdout หรือ Full Test

## ตัวเลข

```json
{
  "scores": {
    "base": {
      "requests": 8,
      "http_200": 8,
      "strict_pass": 0,
      "grades": 15,
      "positive_literal_pass": 0,
      "positive_literal_checks": 5,
      "positive_questions": 2,
      "median_elapsed_sec": 50.297,
      "semantic_accuracy": null,
      "failure_partition_occurrences": {
        "protocol": 14,
        "content_or_format": 6,
        "evidence_identifier": 1,
        "performance": 15
      }
    },
    "trained": {
      "requests": 8,
      "http_200": 8,
      "strict_pass": 0,
      "grades": 15,
      "positive_literal_pass": 4,
      "positive_literal_checks": 5,
      "positive_questions": 2,
      "median_elapsed_sec": 23.68,
      "semantic_accuracy": null,
      "failure_partition_occurrences": {
        "protocol": 14,
        "content_or_format": 2,
        "evidence_identifier": 1,
        "performance": 10
      }
    }
  },
  "by_locale": {
    "base": {
      "en": {
        "requests": 5,
        "http_200": 5,
        "strict_pass": 0,
        "grades": 7,
        "positive_literal_pass": 0,
        "positive_literal_checks": 1,
        "positive_questions": 1,
        "median_elapsed_sec": 47.937,
        "semantic_accuracy": null
      },
      "th": {
        "requests": 3,
        "http_200": 3,
        "strict_pass": 0,
        "grades": 8,
        "positive_literal_pass": 0,
        "positive_literal_checks": 4,
        "positive_questions": 1,
        "median_elapsed_sec": 52.657,
        "semantic_accuracy": null
      }
    },
    "trained": {
      "en": {
        "requests": 5,
        "http_200": 5,
        "strict_pass": 0,
        "grades": 7,
        "positive_literal_pass": 0,
        "positive_literal_checks": 1,
        "positive_questions": 1,
        "median_elapsed_sec": 22.485,
        "semantic_accuracy": null
      },
      "th": {
        "requests": 3,
        "http_200": 3,
        "strict_pass": 0,
        "grades": 8,
        "positive_literal_pass": 4,
        "positive_literal_checks": 4,
        "positive_questions": 1,
        "median_elapsed_sec": 24.875,
        "semantic_accuracy": null
      }
    }
  },
  "model_transport": {
    "actual_backend_requests": 21,
    "success": 21,
    "failed": [],
    "by_stage": {
      "context": 16,
      "evidence_selection": 4,
      "generic_base_inference": 1
    },
    "profiles": {
      "psu-r121-base:latest": 11,
      "psu-r121-trained:latest": 10
    }
  },
  "verification": {
    "parent_source_files_unchanged": 1135,
    "original_protected_files_unchanged": 1138,
    "current_frozen_files_unchanged": 1145,
    "training_frozen_files_unchanged": 13,
    "same_adapter_verified": true,
    "same_model_revision_verified": true,
    "all_runtime_model_variables_verified": true,
    "production_installed": false
  }
}
```

## คำตอบและหลักฐานรายข้อ

### Under CS2 tournamment ruls, may I change Brightness, Resolution and Crosshair, and where?

key: `ef5c0b5af4c6794d174d9a9d329fe7e2535c1fac26b3cf0fd1d69f084d64ca96`; locale: en

#### R121 trained ที่บันทึกไว้ (มีข้อจำกัด config เดิม)

A confirmed English translation is unavailable for some clauses; their Thai source text is retained below.
PSU Phuket CS2 2026 Tournament — 1. Players may customize brightness, resolution, and crosshair settings exclusively within the game and computer screen only: 1. Players may customize brightness, resolution, and crosshair settings only within the game and computer screen exclusively. [S1]
PSU Phuket CS2 2026 Tournament — การตั้งค่าเกม: ผู้เล่นสามารถปรับแต่งความสว่าง (Brightness), ความละเอียดหน้าจอ (Resolution) และเป้าเล็ง (Crosshair) เฉพาะในเกม และหน้าจอคอมพิวเตอร์เท่านั้น [S2]

HTTP 200; 43.281 วินาที

แผน/การตรวจบริบท:
```json
[
  {
    "stage": "context_understanding",
    "reason": "validated_interpretation_proposal",
    "schema_ok": true,
    "transport_ok": true,
    "raw_content": "{\"focus\":\"competition_rules\",\"context_quotes\":[],\"tasks\":[{\"quote\":\"under cs2 tournamment ruls, may i change brightness, resolution and crosshair, and where?\",\"domain\":\"competition_rules\",\"operation\":\"rule_lookup\",\"facet\":\"rule_clause\",\"target\":\"cs2\",\"constraints\":[],\"ambiguous\":false}]}",
    "independent_subtask_reviews": null,
    "context_scope_review": null,
    "model_provenance": {
      "base_repository": "typhoon-ai/typhoon2.5-qwen3-4b",
      "base_revision": "ce0a7416fe82d4404b2b4a253ce3ac095ab1252c",
      "adapter_sha256": "e6a342902a0e469181094c05f412b355cef8cb1f57ce03aa78b6705b67f9b0d8",
      "adapter_active": true,
      "stage": "context",
      "quantization": "NF4",
      "profile_digest": "5a5285d8a6cb1eec20d5eb710606cf03ac8313609da41e7769d33b54f6cbed50"
    }
  },
  {
    "stage": null,
    "reason": null,
    "schema_ok": true,
    "transport_ok": true,
    "raw_content": "{\"plans\": [{\"i\": 0, \"choices\": [1, 2]}]}",
    "independent_subtask_reviews": null,
    "context_scope_review": null,
    "model_provenance": {
      "base_repository": "typhoon-ai/typhoon2.5-qwen3-4b",
      "base_revision": "ce0a7416fe82d4404b2b4a253ce3ac095ab1252c",
      "adapter_sha256": "e6a342902a0e469181094c05f412b355cef8cb1f57ce03aa78b6705b67f9b0d8",
      "adapter_active": false,
      "stage": "evidence_selection",
      "quantization": "NF4",
      "profile_digest": "5a5285d8a6cb1eec20d5eb710606cf03ac8313609da41e7769d33b54f6cbed50"
    }
  }
]
```

ผลเกณฑ์เดิม:
```json
[
  {
    "file": "data/eval/competition_composition_r28_280_20261001.json",
    "row": 41,
    "variant": "question",
    "id": "R28-cs2-custom-settings-en-2",
    "passed": false,
    "failures": [
      "wrong_category",
      "missing_complete_clause:Players may customize brightness, resolution, and crosshair settings only within the game and computer monitor.",
      "first_line_off_topic",
      "wrong_game_source",
      "latency_ceiling"
    ],
    "evidence_level": "complete_clause_composition",
    "grader_detail": null,
    "partitions": {
      "protocol": [
        "wrong_category"
      ],
      "content_or_format": [
        "missing_complete_clause:Players may customize brightness, resolution, and crosshair settings only within the game and computer monitor.",
        "first_line_off_topic"
      ],
      "evidence_identifier": [
        "wrong_game_source"
      ],
      "performance": [
        "latency_ceiling"
      ]
    },
    "positive_literal": true,
    "literal_passed": false,
    "literal_errors": [
      "missing_complete_clause:Players may customize brightness, resolution, and crosshair settings only within the game and computer monitor."
    ]
  }
]
```

#### R122 base

The clause or its required references are incomplete; this rule cannot be confirmed.

HTTP 200; 78.109 วินาที

แผน/การตรวจบริบท:
```json
[
  {
    "stage": "context_understanding",
    "reason": "r121_focus",
    "schema_ok": false,
    "transport_ok": true,
    "raw_content": "{\n  \"focus\": \"rules\",\n  \"context_quotes\": [\n    \"under cs2 tournamment ruls, may i change brightness, resolution and crosshair, and where?\"\n  ],\n  \"tasks\": [\n    {\n      \"quote\": \"under cs2 tournamment ruls, may i change brightness, resolution and crosshair, and where?\",\n      \"domain\": \"rules\",\n      \"operation\": \"rule_lookup\",\n      \"facet\": \"competition_rules\",\n      \"target\": \"rule_clause\",\n      \"constraints\": [\n            {\n              \"slot\": \"audience\",\n              \"quote\": \"under cs2 tournamment ruls\",\n              \"source_record_id\": \"\"\n            },\n            {\n              \"slot\": \"negation\",\n              \"quote\": \"may i\",\n              \"source_record_id\": \"\"\n            },\n            {\n              \"slot\": \"action\",\n              \"quote\": \"change brightness, resolution and crosshair\",\n              \"source_record_id\": \"\"\n            },\n            {\n              \"slot\": \"location\",\n              \"quote\": \"and where?\",\n              \"source_record_id\": \"\"\n            }\n          ],\n      \"ambiguous\": false\n    }\n  ]\n}",
    "independent_subtask_reviews": null,
    "context_scope_review": null,
    "model_provenance": {
      "base_repository": "typhoon-ai/typhoon2.5-qwen3-4b",
      "base_revision": "ce0a7416fe82d4404b2b4a253ce3ac095ab1252c",
      "adapter_sha256": "e6a342902a0e469181094c05f412b355cef8cb1f57ce03aa78b6705b67f9b0d8",
      "adapter_active": false,
      "stage": "context",
      "quantization": "NF4",
      "profile_digest": "320b656c83f3de56b2ee6d9906df42405bac9a0996df1f1b53b55ac88085ab05"
    }
  }
]
```

ผลเกณฑ์เดิม:
```json
[
  {
    "file": "data/eval/competition_composition_r28_280_20261001.json",
    "row": 41,
    "variant": "question",
    "id": "R28-cs2-custom-settings-en-2",
    "passed": false,
    "failures": [
      "wrong_category",
      "missing_complete_clause:Players may customize brightness, resolution, and crosshair settings only within the game and computer monitor.",
      "first_line_off_topic",
      "wrong_game_source",
      "latency_ceiling"
    ],
    "evidence_level": "complete_clause_composition",
    "grader_detail": null,
    "partitions": {
      "protocol": [
        "wrong_category"
      ],
      "content_or_format": [
        "missing_complete_clause:Players may customize brightness, resolution, and crosshair settings only within the game and computer monitor.",
        "first_line_off_topic"
      ],
      "evidence_identifier": [
        "wrong_game_source"
      ],
      "performance": [
        "latency_ceiling"
      ]
    },
    "positive_literal": true,
    "literal_passed": false,
    "literal_errors": [
      "missing_complete_clause:Players may customize brightness, resolution, and crosshair settings only within the game and computer monitor."
    ]
  }
]
```

#### R122 trained

A confirmed English translation is unavailable for some clauses; their Thai source text is retained below.
PSU Phuket CS2 2026 Tournament — 1. Players may customize brightness, resolution, and crosshair settings exclusively within the game and computer screen only: 1. Players may customize brightness, resolution, and crosshair settings only within the game and computer screen exclusively. [S1]
PSU Phuket CS2 2026 Tournament — การตั้งค่าเกม: ผู้เล่นสามารถปรับแต่งความสว่าง (Brightness), ความละเอียดหน้าจอ (Resolution) และเป้าเล็ง (Crosshair) เฉพาะในเกม และหน้าจอคอมพิวเตอร์เท่านั้น [S2]

HTTP 200; 44.234 วินาที

แผน/การตรวจบริบท:
```json
[
  {
    "stage": "context_understanding",
    "reason": "validated_interpretation_proposal",
    "schema_ok": true,
    "transport_ok": true,
    "raw_content": "{\"focus\":\"competition_rules\",\"context_quotes\":[],\"tasks\":[{\"quote\":\"under cs2 tournamment ruls, may i change brightness, resolution and crosshair, and where?\",\"domain\":\"competition_rules\",\"operation\":\"rule_lookup\",\"facet\":\"rule_clause\",\"target\":\"cs2\",\"constraints\":[],\"ambiguous\":false}]}",
    "independent_subtask_reviews": null,
    "context_scope_review": null,
    "model_provenance": {
      "base_repository": "typhoon-ai/typhoon2.5-qwen3-4b",
      "base_revision": "ce0a7416fe82d4404b2b4a253ce3ac095ab1252c",
      "adapter_sha256": "e6a342902a0e469181094c05f412b355cef8cb1f57ce03aa78b6705b67f9b0d8",
      "adapter_active": true,
      "stage": "context",
      "quantization": "NF4",
      "profile_digest": "5a5285d8a6cb1eec20d5eb710606cf03ac8313609da41e7769d33b54f6cbed50"
    }
  },
  {
    "stage": null,
    "reason": null,
    "schema_ok": true,
    "transport_ok": true,
    "raw_content": "{\"plans\": [{\"i\": 0, \"choices\": [1, 2]}]}",
    "independent_subtask_reviews": null,
    "context_scope_review": null,
    "model_provenance": {
      "base_repository": "typhoon-ai/typhoon2.5-qwen3-4b",
      "base_revision": "ce0a7416fe82d4404b2b4a253ce3ac095ab1252c",
      "adapter_sha256": "e6a342902a0e469181094c05f412b355cef8cb1f57ce03aa78b6705b67f9b0d8",
      "adapter_active": false,
      "stage": "evidence_selection",
      "quantization": "NF4",
      "profile_digest": "5a5285d8a6cb1eec20d5eb710606cf03ac8313609da41e7769d33b54f6cbed50"
    }
  }
]
```

ผลเกณฑ์เดิม:
```json
[
  {
    "file": "data/eval/competition_composition_r28_280_20261001.json",
    "row": 41,
    "variant": "question",
    "id": "R28-cs2-custom-settings-en-2",
    "passed": false,
    "failures": [
      "wrong_category",
      "missing_complete_clause:Players may customize brightness, resolution, and crosshair settings only within the game and computer monitor.",
      "first_line_off_topic",
      "wrong_game_source",
      "latency_ceiling"
    ],
    "evidence_level": "complete_clause_composition",
    "grader_detail": null,
    "partitions": {
      "protocol": [
        "wrong_category"
      ],
      "content_or_format": [
        "missing_complete_clause:Players may customize brightness, resolution, and crosshair settings only within the game and computer monitor.",
        "first_line_off_topic"
      ],
      "evidence_identifier": [
        "wrong_game_source"
      ],
      "performance": [
        "latency_ceiling"
      ]
    },
    "positive_literal": true,
    "literal_passed": false,
    "literal_errors": [
      "missing_complete_clause:Players may customize brightness, resolution, and crosshair settings only within the game and computer monitor."
    ]
  }
]
```

### ขอสอบถามหน่อยครับ Nintendo Switch Zone มีอะไรให้ใช้บ้าง

key: `2d97cb1b2297d0a2bf6c2073dfec0e79e2d0ec3995b47987e2b1eef242f70c70`; locale: th

#### R121 trained ที่บันทึกไว้ (มีข้อจำกัด config เดิม)

Nintendo Switch (1-2 Persons) — รายชื่อเกมทั้งหมด: Pokémon Champions; Animal Crossing: New Horizons; It Takes Two; Little Nightmares II; Luigi's Mansion 3; Mario Kart 8 Deluxe; Mario Party Superstars; Monster Hunter Rise; Moving Out 2; New Super Mario Bros. U Deluxe; Nintendo Switch Sports; Overcooked!; Overcooked 2; Ring Fit Adventure; Super Mario Odyssey; Super Smash Bros Ultimate; The Legend of Zelda: Breath of the Wild [S1]
Nintendo Switch (1-4 Persons) — รายชื่อเกมทั้งหมด: Pokémon Champions; Animal Crossing: New Horizons; It Takes Two; Little Nightmares II; Luigi's Mansion 3; Mario Kart 8 Deluxe; Mario Party Superstars; Monster Hunter Rise; Moving Out 2; New Super Mario Bros. U Deluxe; Nintendo Switch Sports; Overcooked!; Overcooked 2; Ring Fit Adventure; Super Mario Odyssey; Super Smash Bros Ultimate; The Legend of Zelda: Breath of the Wild [S2]

HTTP 200; 22.063 วินาที

แผน/การตรวจบริบท:
```json
[
  {
    "stage": "context_understanding",
    "reason": "r121_unbound_target",
    "schema_ok": false,
    "transport_ok": true,
    "raw_content": "{\"focus\":\"equipment_inventory\",\"context_quotes\":[],\"tasks\":[{\"quote\":\"nintendo switch zone มีอะไรให้ใช้บ้าง\",\"domain\":\"equipment\",\"operation\":\"list\",\"facet\":\"usage\",\"target\":\"Nintendo Switch\",\"constraints\":[],\"ambiguous\":false}]}",
    "independent_subtask_reviews": null,
    "context_scope_review": null,
    "model_provenance": {
      "base_repository": "typhoon-ai/typhoon2.5-qwen3-4b",
      "base_revision": "ce0a7416fe82d4404b2b4a253ce3ac095ab1252c",
      "adapter_sha256": "e6a342902a0e469181094c05f412b355cef8cb1f57ce03aa78b6705b67f9b0d8",
      "adapter_active": true,
      "stage": "context",
      "quantization": "NF4",
      "profile_digest": "5a5285d8a6cb1eec20d5eb710606cf03ac8313609da41e7769d33b54f6cbed50"
    }
  },
  {
    "stage": null,
    "reason": null,
    "schema_ok": true,
    "transport_ok": true,
    "raw_content": "{\"plans\": [{\"i\": 0, \"choices\": [1, 2]}]}",
    "independent_subtask_reviews": null,
    "context_scope_review": null,
    "model_provenance": {
      "base_repository": "typhoon-ai/typhoon2.5-qwen3-4b",
      "base_revision": "ce0a7416fe82d4404b2b4a253ce3ac095ab1252c",
      "adapter_sha256": "e6a342902a0e469181094c05f412b355cef8cb1f57ce03aa78b6705b67f9b0d8",
      "adapter_active": false,
      "stage": "evidence_selection",
      "quantization": "NF4",
      "profile_digest": "5a5285d8a6cb1eec20d5eb710606cf03ac8313609da41e7769d33b54f6cbed50"
    }
  }
]
```

ผลเกณฑ์เดิม:
```json
[
  {
    "file": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
    "row": 3499,
    "variant": "question",
    "id": "MASTER-GT-TH-03500",
    "passed": false,
    "failures": [
      "route:knowledge expected:['clarification', 'equipment']",
      "missing all alternatives: ['อุปกรณ์', 'หมายถึงเรื่องไหน', 'Zone']",
      "latency_ceiling"
    ],
    "evidence_level": "literal_content_contract",
    "grader_detail": {
      "strong_outcome_matches": false,
      "positive_content_asserted": true
    },
    "partitions": {
      "protocol": [
        "route:knowledge expected:['clarification', 'equipment']"
      ],
      "content_or_format": [
        "missing all alternatives: ['อุปกรณ์', 'หมายถึงเรื่องไหน', 'Zone']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    },
    "positive_literal": true,
    "literal_passed": false,
    "literal_errors": [
      "missing all alternatives: ['อุปกรณ์', 'หมายถึงเรื่องไหน', 'Zone']"
    ]
  },
  {
    "file": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
    "row": 3499,
    "variant": "question",
    "id": "MASTER-GT-TH-03500",
    "passed": false,
    "failures": [
      "route:knowledge expected:['clarification', 'equipment']",
      "missing all alternatives: ['อุปกรณ์', 'หมายถึงเรื่องไหน', 'Zone']",
      "latency_ceiling"
    ],
    "evidence_level": "literal_content_contract",
    "grader_detail": {
      "strong_outcome_matches": false,
      "positive_content_asserted": true
    },
    "partitions": {
      "protocol": [
        "route:knowledge expected:['clarification', 'equipment']"
      ],
      "content_or_format": [
        "missing all alternatives: ['อุปกรณ์', 'หมายถึงเรื่องไหน', 'Zone']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    },
    "positive_literal": true,
    "literal_passed": false,
    "literal_errors": [
      "missing all alternatives: ['อุปกรณ์', 'หมายถึงเรื่องไหน', 'Zone']"
    ]
  },
  {
    "file": "data/eval/master_ground_truth_th_5000_v1.jsonl",
    "row": 3499,
    "variant": "question",
    "id": "MASTER-GT-TH-03500",
    "passed": false,
    "failures": [
      "route:knowledge expected:['clarification', 'equipment']",
      "missing all alternatives: ['อุปกรณ์', 'หมายถึงเรื่องไหน', 'Zone']",
      "latency_ceiling"
    ],
    "evidence_level": "literal_content_contract",
    "grader_detail": {
      "strong_outcome_matches": false,
      "positive_content_asserted": true
    },
    "partitions": {
      "protocol": [
        "route:knowledge expected:['clarification', 'equipment']"
      ],
      "content_or_format": [
        "missing all alternatives: ['อุปกรณ์', 'หมายถึงเรื่องไหน', 'Zone']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    },
    "positive_literal": true,
    "literal_passed": false,
    "literal_errors": [
      "missing all alternatives: ['อุปกรณ์', 'หมายถึงเรื่องไหน', 'Zone']"
    ]
  },
  {
    "file": "data/eval/master_ground_truth_th_5000_v2.jsonl",
    "row": 3499,
    "variant": "question",
    "id": "MASTER-GT-TH-03500",
    "passed": false,
    "failures": [
      "route:knowledge expected:['clarification', 'equipment']",
      "missing all alternatives: ['อุปกรณ์', 'หมายถึงเรื่องไหน', 'Zone']",
      "latency_ceiling"
    ],
    "evidence_level": "literal_content_contract",
    "grader_detail": {
      "strong_outcome_matches": false,
      "positive_content_asserted": true
    },
    "partitions": {
      "protocol": [
        "route:knowledge expected:['clarification', 'equipment']"
      ],
      "content_or_format": [
        "missing all alternatives: ['อุปกรณ์', 'หมายถึงเรื่องไหน', 'Zone']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    },
    "positive_literal": true,
    "literal_passed": false,
    "literal_errors": [
      "missing all alternatives: ['อุปกรณ์', 'หมายถึงเรื่องไหน', 'Zone']"
    ]
  }
]
```

#### R122 base

Nintendo Switch (1-2 Persons) — รายชื่อเกมทั้งหมด: Pokémon Champions; Animal Crossing: New Horizons; It Takes Two; Little Nightmares II; Luigi's Mansion 3; Mario Kart 8 Deluxe; Mario Party Superstars; Monster Hunter Rise; Moving Out 2; New Super Mario Bros. U Deluxe; Nintendo Switch Sports; Overcooked!; Overcooked 2; Ring Fit Adventure; Super Mario Odyssey; Super Smash Bros Ultimate; The Legend of Zelda: Breath of the Wild [S1]
Nintendo Switch (1-4 Persons) — รายชื่อเกมทั้งหมด: Pokémon Champions; Animal Crossing: New Horizons; It Takes Two; Little Nightmares II; Luigi's Mansion 3; Mario Kart 8 Deluxe; Mario Party Superstars; Monster Hunter Rise; Moving Out 2; New Super Mario Bros. U Deluxe; Nintendo Switch Sports; Overcooked!; Overcooked 2; Ring Fit Adventure; Super Mario Odyssey; Super Smash Bros Ultimate; The Legend of Zelda: Breath of the Wild [S2]

HTTP 200; 30.703 วินาที

แผน/การตรวจบริบท:
```json
[
  {
    "stage": "context_understanding",
    "reason": "r121_facet",
    "schema_ok": false,
    "transport_ok": true,
    "raw_content": "{\n  \"focus\": \"equipment_inventory\",\n  \"context_quotes\": [\n    \"nintendo switch zone มีอะไรให้ใช้บ้าง\"\n  ],\n  \"tasks\": [\n    {\n      \"quote\": \"nintendo switch zone มีอะไรให้ใช้บ้าง\",\n      \"domain\": \"equipment\",\n      \"operation\": \"detail\",\n      \"facet\": \"equipment_inventory\",\n      \"target\": \"\",\n      \"constraints\": [],\n      \"ambiguous\": false\n    }\n  ]\n}",
    "independent_subtask_reviews": null,
    "context_scope_review": null,
    "model_provenance": {
      "base_repository": "typhoon-ai/typhoon2.5-qwen3-4b",
      "base_revision": "ce0a7416fe82d4404b2b4a253ce3ac095ab1252c",
      "adapter_sha256": "e6a342902a0e469181094c05f412b355cef8cb1f57ce03aa78b6705b67f9b0d8",
      "adapter_active": false,
      "stage": "context",
      "quantization": "NF4",
      "profile_digest": "320b656c83f3de56b2ee6d9906df42405bac9a0996df1f1b53b55ac88085ab05"
    }
  },
  {
    "stage": null,
    "reason": null,
    "schema_ok": true,
    "transport_ok": true,
    "raw_content": "{\"plans\": [{\"i\": 0, \"choices\": [1, 2]}]}",
    "independent_subtask_reviews": null,
    "context_scope_review": null,
    "model_provenance": {
      "base_repository": "typhoon-ai/typhoon2.5-qwen3-4b",
      "base_revision": "ce0a7416fe82d4404b2b4a253ce3ac095ab1252c",
      "adapter_sha256": "e6a342902a0e469181094c05f412b355cef8cb1f57ce03aa78b6705b67f9b0d8",
      "adapter_active": false,
      "stage": "evidence_selection",
      "quantization": "NF4",
      "profile_digest": "320b656c83f3de56b2ee6d9906df42405bac9a0996df1f1b53b55ac88085ab05"
    }
  }
]
```

ผลเกณฑ์เดิม:
```json
[
  {
    "file": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
    "row": 3499,
    "variant": "question",
    "id": "MASTER-GT-TH-03500",
    "passed": false,
    "failures": [
      "route:knowledge expected:['clarification', 'equipment']",
      "missing all alternatives: ['อุปกรณ์', 'หมายถึงเรื่องไหน', 'Zone']",
      "latency_ceiling"
    ],
    "evidence_level": "literal_content_contract",
    "grader_detail": {
      "strong_outcome_matches": false,
      "positive_content_asserted": true
    },
    "partitions": {
      "protocol": [
        "route:knowledge expected:['clarification', 'equipment']"
      ],
      "content_or_format": [
        "missing all alternatives: ['อุปกรณ์', 'หมายถึงเรื่องไหน', 'Zone']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    },
    "positive_literal": true,
    "literal_passed": false,
    "literal_errors": [
      "missing all alternatives: ['อุปกรณ์', 'หมายถึงเรื่องไหน', 'Zone']"
    ]
  },
  {
    "file": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
    "row": 3499,
    "variant": "question",
    "id": "MASTER-GT-TH-03500",
    "passed": false,
    "failures": [
      "route:knowledge expected:['clarification', 'equipment']",
      "missing all alternatives: ['อุปกรณ์', 'หมายถึงเรื่องไหน', 'Zone']",
      "latency_ceiling"
    ],
    "evidence_level": "literal_content_contract",
    "grader_detail": {
      "strong_outcome_matches": false,
      "positive_content_asserted": true
    },
    "partitions": {
      "protocol": [
        "route:knowledge expected:['clarification', 'equipment']"
      ],
      "content_or_format": [
        "missing all alternatives: ['อุปกรณ์', 'หมายถึงเรื่องไหน', 'Zone']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    },
    "positive_literal": true,
    "literal_passed": false,
    "literal_errors": [
      "missing all alternatives: ['อุปกรณ์', 'หมายถึงเรื่องไหน', 'Zone']"
    ]
  },
  {
    "file": "data/eval/master_ground_truth_th_5000_v1.jsonl",
    "row": 3499,
    "variant": "question",
    "id": "MASTER-GT-TH-03500",
    "passed": false,
    "failures": [
      "route:knowledge expected:['clarification', 'equipment']",
      "missing all alternatives: ['อุปกรณ์', 'หมายถึงเรื่องไหน', 'Zone']",
      "latency_ceiling"
    ],
    "evidence_level": "literal_content_contract",
    "grader_detail": {
      "strong_outcome_matches": false,
      "positive_content_asserted": true
    },
    "partitions": {
      "protocol": [
        "route:knowledge expected:['clarification', 'equipment']"
      ],
      "content_or_format": [
        "missing all alternatives: ['อุปกรณ์', 'หมายถึงเรื่องไหน', 'Zone']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    },
    "positive_literal": true,
    "literal_passed": false,
    "literal_errors": [
      "missing all alternatives: ['อุปกรณ์', 'หมายถึงเรื่องไหน', 'Zone']"
    ]
  },
  {
    "file": "data/eval/master_ground_truth_th_5000_v2.jsonl",
    "row": 3499,
    "variant": "question",
    "id": "MASTER-GT-TH-03500",
    "passed": false,
    "failures": [
      "route:knowledge expected:['clarification', 'equipment']",
      "missing all alternatives: ['อุปกรณ์', 'หมายถึงเรื่องไหน', 'Zone']",
      "latency_ceiling"
    ],
    "evidence_level": "literal_content_contract",
    "grader_detail": {
      "strong_outcome_matches": false,
      "positive_content_asserted": true
    },
    "partitions": {
      "protocol": [
        "route:knowledge expected:['clarification', 'equipment']"
      ],
      "content_or_format": [
        "missing all alternatives: ['อุปกรณ์', 'หมายถึงเรื่องไหน', 'Zone']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    },
    "positive_literal": true,
    "literal_passed": false,
    "literal_errors": [
      "missing all alternatives: ['อุปกรณ์', 'หมายถึงเรื่องไหน', 'Zone']"
    ]
  }
]
```

#### R122 trained

Nintendo Switch OLED — การใช้งาน: เครื่องเกม Nintendo Switch รุ่น OLED สำหรับเล่นเกมคอนโซลแบบกลุ่มหรือครอบครัว
จอง Nintendo Switch Zone แล้วเล่นผ่าน TV 86 นิ้วและจอยที่ศูนย์จัดไว้ตามรอบบริการ
เล่น Mario Kart 8 Deluxe
เล่น Overcooked 2
เล่น Super Smash Bros Ultimate
เล่น Nintendo Switch Sports [S1]

HTTP 200; 17.563 วินาที

แผน/การตรวจบริบท:
```json
[
  {
    "stage": "context_understanding",
    "reason": "validated_interpretation_proposal",
    "schema_ok": true,
    "transport_ok": true,
    "raw_content": "{\"focus\":\"equipment_inventory\",\"context_quotes\":[],\"tasks\":[{\"quote\":\"nintendo switch zone มีอะไรให้ใช้บ้าง\",\"domain\":\"equipment\",\"operation\":\"list\",\"facet\":\"usage\",\"target\":\"Nintendo Switch\",\"constraints\":[],\"ambiguous\":false}]}",
    "independent_subtask_reviews": null,
    "context_scope_review": null,
    "model_provenance": {
      "base_repository": "typhoon-ai/typhoon2.5-qwen3-4b",
      "base_revision": "ce0a7416fe82d4404b2b4a253ce3ac095ab1252c",
      "adapter_sha256": "e6a342902a0e469181094c05f412b355cef8cb1f57ce03aa78b6705b67f9b0d8",
      "adapter_active": true,
      "stage": "context",
      "quantization": "NF4",
      "profile_digest": "5a5285d8a6cb1eec20d5eb710606cf03ac8313609da41e7769d33b54f6cbed50"
    }
  }
]
```

ผลเกณฑ์เดิม:
```json
[
  {
    "file": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
    "row": 3499,
    "variant": "question",
    "id": "MASTER-GT-TH-03500",
    "passed": false,
    "failures": [
      "route:knowledge expected:['clarification', 'equipment']"
    ],
    "evidence_level": "literal_content_contract",
    "grader_detail": {
      "strong_outcome_matches": false,
      "positive_content_asserted": true
    },
    "partitions": {
      "protocol": [
        "route:knowledge expected:['clarification', 'equipment']"
      ]
    },
    "positive_literal": true,
    "literal_passed": true,
    "literal_errors": []
  },
  {
    "file": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
    "row": 3499,
    "variant": "question",
    "id": "MASTER-GT-TH-03500",
    "passed": false,
    "failures": [
      "route:knowledge expected:['clarification', 'equipment']"
    ],
    "evidence_level": "literal_content_contract",
    "grader_detail": {
      "strong_outcome_matches": false,
      "positive_content_asserted": true
    },
    "partitions": {
      "protocol": [
        "route:knowledge expected:['clarification', 'equipment']"
      ]
    },
    "positive_literal": true,
    "literal_passed": true,
    "literal_errors": []
  },
  {
    "file": "data/eval/master_ground_truth_th_5000_v1.jsonl",
    "row": 3499,
    "variant": "question",
    "id": "MASTER-GT-TH-03500",
    "passed": false,
    "failures": [
      "route:knowledge expected:['clarification', 'equipment']"
    ],
    "evidence_level": "literal_content_contract",
    "grader_detail": {
      "strong_outcome_matches": false,
      "positive_content_asserted": true
    },
    "partitions": {
      "protocol": [
        "route:knowledge expected:['clarification', 'equipment']"
      ]
    },
    "positive_literal": true,
    "literal_passed": true,
    "literal_errors": []
  },
  {
    "file": "data/eval/master_ground_truth_th_5000_v2.jsonl",
    "row": 3499,
    "variant": "question",
    "id": "MASTER-GT-TH-03500",
    "passed": false,
    "failures": [
      "route:knowledge expected:['clarification', 'equipment']"
    ],
    "evidence_level": "literal_content_contract",
    "grader_detail": {
      "strong_outcome_matches": false,
      "positive_content_asserted": true
    },
    "partitions": {
      "protocol": [
        "route:knowledge expected:['clarification', 'equipment']"
      ]
    },
    "positive_literal": true,
    "literal_passed": true,
    "literal_errors": []
  }
]
```

### What are the 8 buttons in Tekken 8, ans what is the PC price

key: `d91ee50a1f6c21f141226b55bb86aaea2935e3a4b5e73b339ff4d83b81a1deaa`; locale: en

#### R121 trained ที่บันทึกไว้ (มีข้อจำกัด config เดิม)

TEKKEN 8 — how to play: Play in rounds. Select a character. Practice basic moves/combo sequences. Read your opponent's timing and reduce their health to zero first. [S1]

Rates last reaffirmed by the owner on 2026-10-20; no new effective interval was established.
PC #01-#02 / PSU Student and Staff — per-person price for the rate duration: 0 THB per person for 60 minutes [S2]
PC #01-#02 / PSU Alumni and General Student — per-person price for the rate duration: 25 THB per person for 60 minutes [S3]
PC #01-#02 / General Adult — per-person price for the rate duration: 70 THB per person for 60 minutes [S4]
PC #03-#10 / PSU Student and Staff — per-person price for the rate duration: 0 THB per person for 60 minutes [S5]
PC #03-#10 / PSU Alumni and General Student — per-person price for the rate duration: 25 THB per person for 60 minutes [S6]
PC #03-#10 / General Adult — per-person price for the rate duration: 70 THB per person for 60 minutes [S7]

HTTP 200; 26.953 วินาที

แผน/การตรวจบริบท:
```json
[
  {
    "stage": "context_understanding",
    "reason": "validated_interpretation_proposal",
    "schema_ok": true,
    "transport_ok": true,
    "raw_content": "{\"focus\":\"multiple\",\"context_quotes\":[],\"tasks\":[{\"quote\":\"what are the 8 buttons in tekken 8\",\"domain\":\"games\",\"operation\":\"detail\",\"facet\":\"how_to_play\",\"target\":\"tekken 8\",\"constraints\":[],\"ambiguous\":false},{\"quote\":\"what is the pc price\",\"domain\":\"service_fee\",\"operation\":\"price_calculate\",\"facet\":\"amount\",\"target\":\"tekken 8\",\"constraints\":[],\"ambiguous\":false}]}",
    "independent_subtask_reviews": null,
    "context_scope_review": null,
    "model_provenance": {
      "base_repository": "typhoon-ai/typhoon2.5-qwen3-4b",
      "base_revision": "ce0a7416fe82d4404b2b4a253ce3ac095ab1252c",
      "adapter_sha256": "e6a342902a0e469181094c05f412b355cef8cb1f57ce03aa78b6705b67f9b0d8",
      "adapter_active": true,
      "stage": "context",
      "quantization": "NF4",
      "profile_digest": "5a5285d8a6cb1eec20d5eb710606cf03ac8313609da41e7769d33b54f6cbed50"
    }
  }
]
```

ผลเกณฑ์เดิม:
```json
[
  {
    "file": "data/eval/master_gt_bilingual_multi_error_2000_20260929_r15.jsonl",
    "row": 1911,
    "variant": "noisy",
    "id": "MASTER-GT-EN-04868",
    "passed": false,
    "failures": [
      "route:knowledge expected:['multi_question']",
      "latency_ceiling"
    ],
    "evidence_level": "literal_content_contract",
    "grader_detail": {
      "strong_outcome_matches": false,
      "positive_content_asserted": false
    },
    "partitions": {
      "protocol": [
        "route:knowledge expected:['multi_question']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    },
    "positive_literal": false,
    "literal_passed": true,
    "literal_errors": []
  }
]
```

#### R122 base

Rates last reaffirmed by the owner on 2026-10-20; no new effective interval was established.
PC #01-#02 / PSU Student and Staff — per-person price for the rate duration: 0 THB per person for 60 minutes [S1]
PC #01-#02 / PSU Alumni and General Student — per-person price for the rate duration: 25 THB per person for 60 minutes [S2]
PC #01-#02 / General Adult — per-person price for the rate duration: 70 THB per person for 60 minutes [S3]
PC #03-#10 / PSU Student and Staff — per-person price for the rate duration: 0 THB per person for 60 minutes [S4]
PC #03-#10 / PSU Alumni and General Student — per-person price for the rate duration: 25 THB per person for 60 minutes [S5]
PC #03-#10 / General Adult — per-person price for the rate duration: 70 THB per person for 60 minutes [S6]

HTTP 200; 25.359 วินาที

แผน/การตรวจบริบท:
```json
[
  {
    "stage": "context_understanding",
    "reason": "independent_context_frame",
    "schema_ok": true,
    "transport_ok": true,
    "raw_content": "{\n  \"focus\": \"game_controls\",\n  \"context_quotes\": [\n    \"what are the 8 buttons in tekken 8\"\n  ],\n  \"tasks\": [\n    {\n      \"quote\": \"what are the 8 buttons in tekken 8\",\n      \"domain\": \"game_controls\",\n      \"operation\": \"detail\",\n      \"facet\": \"input_bindings\",\n      \"target\": \"8 buttons in Tekken 8\",\n      \"constraints\": [],\n      \"ambiguous\": false\n    }\n  ]\n}",
    "independent_subtask_reviews": null,
    "context_scope_review": null,
    "model_provenance": {
      "base_repository": "typhoon-ai/typhoon2.5-qwen3-4b",
      "base_revision": "ce0a7416fe82d4404b2b4a253ce3ac095ab1252c",
      "adapter_sha256": "e6a342902a0e469181094c05f412b355cef8cb1f57ce03aa78b6705b67f9b0d8",
      "adapter_active": false,
      "stage": "context",
      "quantization": "NF4",
      "profile_digest": "320b656c83f3de56b2ee6d9906df42405bac9a0996df1f1b53b55ac88085ab05"
    }
  }
]
```

ผลเกณฑ์เดิม:
```json
[
  {
    "file": "data/eval/master_gt_bilingual_multi_error_2000_20260929_r15.jsonl",
    "row": 1911,
    "variant": "noisy",
    "id": "MASTER-GT-EN-04868",
    "passed": false,
    "failures": [
      "route:knowledge expected:['multi_question']",
      "latency_ceiling"
    ],
    "evidence_level": "literal_content_contract",
    "grader_detail": {
      "strong_outcome_matches": false,
      "positive_content_asserted": false
    },
    "partitions": {
      "protocol": [
        "route:knowledge expected:['multi_question']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    },
    "positive_literal": false,
    "literal_passed": true,
    "literal_errors": []
  }
]
```

#### R122 trained

The source records 12 control entries but does not identify the requested subset of 8 buttons. Known entries are listed below; please specify the button group.
TEKKEN 8 / PlayStation / PS5 — Left Punch: Square — Punch or attack with the left hand — primary button to start fast frame combos [S1]
TEKKEN 8 / PlayStation / PS5 — Right Punch: Triangle — Heavy punch or attack with the right hand — often used for high damage or countering (Counter) [S2]
TEKKEN 8 / PlayStation / PS5 — Left Kick: Cross — Kick with the left leg to intercept or attack and create an opening in the opponent's defense. [S3]
TEKKEN 8 / PlayStation / PS5 — Right Kick: Circle — Deliver a powerful right-leg kick, often for range control or a high-damage low sweep. [S4]
TEKKEN 8 / PlayStation / PS5 — Jump: D-Pad Up — Jump upward to evade low attacks, or press in combination with mid-air attack button [S5]
TEKKEN 8 / PlayStation / PS5 — Move Backward: D-Pad Left — Move the character backward to maintain distance or hold to "Guard" against high and medium attacks from enemies [S6]
TEKKEN 8 / PlayStation / PS5 — Duck: D-Pad Down — Lower the character's stance to dodge punches or high attacks, and block low attacks [S7]
TEKKEN 8 / PlayStation / PS5 — Move: L (Left Stick) — Move the character in general directions, including moving forward and backward. [S8]
TEKKEN 8 / PlayStation / PS5 — Special Style: L1 — Press to toggle the Smart Assist mode, allowing one-button combo and special move execution [S9]
TEKKEN 8 / PlayStation / PS5 — Heat Activate: R1 — Activate the Heat System to enter Overdrive state, buffing attacks and enhancing character abilities [S10]
TEKKEN 8 / PlayStation / PS5 — Heat Smash: R1 (While in Heat) — Release the powerful final move to end a combo, using all remaining Heat gauge at once. [S11]
TEKKEN 8 / PlayStation / PS5 — Pause: Options — Pause the game briefly to enter a menu window, such as checking Move List (move list) or other settings. [S12]

Rates last reaffirmed by the owner on 2026-10-20; no new effective interval was established.
PC #01-#02 / PSU Student and Staff — per-person price for the rate duration: 0 THB per person for 60 minutes [S13]
PC #01-#02 / PSU Alumni and General Student — per-person price for the rate duration: 25 THB per person for 60 minutes [S14]
PC #01-#02 / General Adult — per-person price for the rate duration: 70 THB per person for 60 minutes [S15]
PC #03-#10 / PSU Student and Staff — per-person price for the rate duration: 0 THB per person for 60 minutes [S16]
PC #03-#10 / PSU Alumni and General Student — per-person price for the rate duration: 25 THB per person for 60 minutes [S17]
PC #03-#10 / General Adult — per-person price for the rate duration: 70 THB per person for 60 minutes [S18]

HTTP 200; 28.89 วินาที

แผน/การตรวจบริบท:
```json
[
  {
    "stage": "context_understanding",
    "reason": "validated_interpretation_proposal",
    "schema_ok": true,
    "transport_ok": true,
    "raw_content": "{\"focus\":\"multiple\",\"context_quotes\":[],\"tasks\":[{\"quote\":\"what are the 8 buttons in tekken 8\",\"domain\":\"games\",\"operation\":\"detail\",\"facet\":\"how_to_play\",\"target\":\"tekken 8\",\"constraints\":[],\"ambiguous\":false},{\"quote\":\"what is the pc price\",\"domain\":\"service_fee\",\"operation\":\"price_calculate\",\"facet\":\"amount\",\"target\":\"tekken 8\",\"constraints\":[],\"ambiguous\":false}]}",
    "independent_subtask_reviews": [
      {
        "basis": "legacy_control_frame_and_current_source_target",
        "model_plan_accepted": true,
        "model_reason": "validated_interpretation_proposal",
        "prior_tasks": [
          {
            "quote": "what are the 8 buttons in tekken 8",
            "domain": "games",
            "category": "C04",
            "operation": "detail",
            "facet": "how_to_play",
            "target": "tekken 8",
            "constraints": [],
            "ambiguous": false
          }
        ],
        "business_facts_added": false
      },
      {
        "basis": "unrelated_cross_task_target_removed",
        "source_target": "tekken 8",
        "task_quote": "what is the pc price",
        "business_facts_added": false
      }
    ],
    "context_scope_review": null,
    "model_provenance": {
      "base_repository": "typhoon-ai/typhoon2.5-qwen3-4b",
      "base_revision": "ce0a7416fe82d4404b2b4a253ce3ac095ab1252c",
      "adapter_sha256": "e6a342902a0e469181094c05f412b355cef8cb1f57ce03aa78b6705b67f9b0d8",
      "adapter_active": true,
      "stage": "context",
      "quantization": "NF4",
      "profile_digest": "5a5285d8a6cb1eec20d5eb710606cf03ac8313609da41e7769d33b54f6cbed50"
    }
  }
]
```

ผลเกณฑ์เดิม:
```json
[
  {
    "file": "data/eval/master_gt_bilingual_multi_error_2000_20260929_r15.jsonl",
    "row": 1911,
    "variant": "noisy",
    "id": "MASTER-GT-EN-04868",
    "passed": false,
    "failures": [
      "route:knowledge expected:['multi_question']",
      "latency_ceiling"
    ],
    "evidence_level": "literal_content_contract",
    "grader_detail": {
      "strong_outcome_matches": false,
      "positive_content_asserted": false
    },
    "partitions": {
      "protocol": [
        "route:knowledge expected:['multi_question']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    },
    "positive_literal": false,
    "literal_passed": true,
    "literal_errors": []
  }
]
```

### ก่อนเดินทางไปใช้บริการ อยากทราบว่า คนที่ไม่ใช่นักศึกษา PSU เข้าไปเล่นได้หรือเปล่า

key: `490a5b13b782510c507fdb5692383211a2537734caa8e7e489f42932969ea534`; locale: th

#### R121 trained ที่บันทึกไว้ (มีข้อจำกัด config เดิม)

ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ

HTTP 200; 23.235 วินาที

แผน/การตรวจบริบท:
```json
[
  {
    "stage": "context_understanding",
    "reason": "validated_interpretation_proposal",
    "schema_ok": true,
    "transport_ok": true,
    "raw_content": "{\"focus\":\"eligibility\",\"context_quotes\":[],\"tasks\":[{\"quote\":\"ก่อนเดินทางไปใช้บริการ อยากทราบว่า คนที่ไม่ใช่นักศึกษา psu เข้าไปเล่นได้หรือเปล่า\",\"domain\":\"rules\",\"operation\":\"detail\",\"facet\":\"owner_policy\",\"target\":\"\",\"constraints\":[],\"ambiguous\":false}]}",
    "independent_subtask_reviews": null,
    "context_scope_review": null,
    "model_provenance": {
      "base_repository": "typhoon-ai/typhoon2.5-qwen3-4b",
      "base_revision": "ce0a7416fe82d4404b2b4a253ce3ac095ab1252c",
      "adapter_sha256": "e6a342902a0e469181094c05f412b355cef8cb1f57ce03aa78b6705b67f9b0d8",
      "adapter_active": true,
      "stage": "context",
      "quantization": "NF4",
      "profile_digest": "5a5285d8a6cb1eec20d5eb710606cf03ac8313609da41e7769d33b54f6cbed50"
    }
  }
]
```

ผลเกณฑ์เดิม:
```json
[
  {
    "file": "data/eval/intent_trap_bilingual_1000_v1.jsonl",
    "row": 107,
    "variant": "question",
    "id": "INTENT-TRAP-TH-0108",
    "passed": false,
    "failures": [
      "route:knowledge expected:['reservation', 'rules', 'no_answer', 'clarification', 'service_fee']",
      "latency_ceiling"
    ],
    "evidence_level": "literal_content_contract",
    "grader_detail": {
      "strong_outcome_matches": false,
      "positive_content_asserted": false
    },
    "partitions": {
      "protocol": [
        "route:knowledge expected:['reservation', 'rules', 'no_answer', 'clarification', 'service_fee']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    },
    "positive_literal": false,
    "literal_passed": true,
    "literal_errors": []
  },
  {
    "file": "data/eval/intent_trap_bilingual_1000_v2.jsonl",
    "row": 107,
    "variant": "question",
    "id": "INTENT-TRAP-TH-0108",
    "passed": false,
    "failures": [
      "route:knowledge expected:['reservation', 'rules', 'no_answer', 'clarification', 'service_fee']",
      "latency_ceiling"
    ],
    "evidence_level": "literal_content_contract",
    "grader_detail": {
      "strong_outcome_matches": false,
      "positive_content_asserted": false
    },
    "partitions": {
      "protocol": [
        "route:knowledge expected:['reservation', 'rules', 'no_answer', 'clarification', 'service_fee']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    },
    "positive_literal": false,
    "literal_passed": true,
    "literal_errors": []
  }
]
```

#### R122 base

ผู้ใช้ภายนอก: บุคคลภายนอกใช้บริการทั่วไปได้ทั้งหมด; ไม่ขยายไปเป็นคุณสมบัติแข่ง CS2 ซึ่งเอกสารกำหนดนักศึกษา PSU ภูเก็ต [S1]

HTTP 200; 52.657 วินาที

แผน/การตรวจบริบท:
```json
[
  {
    "stage": "context_understanding",
    "reason": "r121_vocabulary",
    "schema_ok": false,
    "transport_ok": true,
    "raw_content": "{\n  \"focus\": \"eligibility\",\n  \"context_quotes\": [\n    \"ก่อนเดินทางไปใช้บริการ อยากทราบว่า คนที่ไม่ใช่นักศึกษา psu เข้าไปเล่นได้หรือเปล่า\"\n  ],\n  \"tasks\": [\n    {\n      \"quote\": \"ก่อนเดินทางไปใช้บริการ อยากทราบว่า คนที่ไม่ใช่นักศึกษา psu เข้าไปเล่นได้หรือเปล่า\",\n      \"domain\": \"eligibility\",\n      \"operation\": \"availability\",\n      \"facet\": \"eligibility\",\n      \"target\": \"คนที่ไม่ใช่นักศึกษา psu เข้าไปเล่นได้หรือเปล่า\",\n      \"constraints\": [\n        {\n          \"slot\": \"audience\",\n          \"quote\": \"คนที่ไม่ใช่นักศึกษา psu\",\n          \"source_record_id\": \"\"\n        }\n      ],\n      \"ambiguous\": false\n    }\n  ]\n}",
    "independent_subtask_reviews": null,
    "context_scope_review": null,
    "model_provenance": {
      "base_repository": "typhoon-ai/typhoon2.5-qwen3-4b",
      "base_revision": "ce0a7416fe82d4404b2b4a253ce3ac095ab1252c",
      "adapter_sha256": "e6a342902a0e469181094c05f412b355cef8cb1f57ce03aa78b6705b67f9b0d8",
      "adapter_active": false,
      "stage": "context",
      "quantization": "NF4",
      "profile_digest": "320b656c83f3de56b2ee6d9906df42405bac9a0996df1f1b53b55ac88085ab05"
    }
  }
]
```

ผลเกณฑ์เดิม:
```json
[
  {
    "file": "data/eval/intent_trap_bilingual_1000_v1.jsonl",
    "row": 107,
    "variant": "question",
    "id": "INTENT-TRAP-TH-0108",
    "passed": false,
    "failures": [
      "route:knowledge expected:['reservation', 'rules', 'no_answer', 'clarification', 'service_fee']",
      "latency_ceiling"
    ],
    "evidence_level": "literal_content_contract",
    "grader_detail": {
      "strong_outcome_matches": false,
      "positive_content_asserted": false
    },
    "partitions": {
      "protocol": [
        "route:knowledge expected:['reservation', 'rules', 'no_answer', 'clarification', 'service_fee']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    },
    "positive_literal": false,
    "literal_passed": true,
    "literal_errors": []
  },
  {
    "file": "data/eval/intent_trap_bilingual_1000_v2.jsonl",
    "row": 107,
    "variant": "question",
    "id": "INTENT-TRAP-TH-0108",
    "passed": false,
    "failures": [
      "route:knowledge expected:['reservation', 'rules', 'no_answer', 'clarification', 'service_fee']",
      "latency_ceiling"
    ],
    "evidence_level": "literal_content_contract",
    "grader_detail": {
      "strong_outcome_matches": false,
      "positive_content_asserted": false
    },
    "partitions": {
      "protocol": [
        "route:knowledge expected:['reservation', 'rules', 'no_answer', 'clarification', 'service_fee']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    },
    "positive_literal": false,
    "literal_passed": true,
    "literal_errors": []
  }
]
```

#### R122 trained

ผู้ใช้ภายนอก: บุคคลภายนอกใช้บริการทั่วไปได้ทั้งหมด; ไม่ขยายไปเป็นคุณสมบัติแข่ง CS2 ซึ่งเอกสารกำหนดนักศึกษา PSU ภูเก็ต [S1]

HTTP 200; 24.875 วินาที

แผน/การตรวจบริบท:
```json
[
  {
    "stage": "context_understanding",
    "reason": "validated_interpretation_proposal",
    "schema_ok": true,
    "transport_ok": true,
    "raw_content": "{\"focus\":\"eligibility\",\"context_quotes\":[],\"tasks\":[{\"quote\":\"ก่อนเดินทางไปใช้บริการ อยากทราบว่า คนที่ไม่ใช่นักศึกษา psu เข้าไปเล่นได้หรือเปล่า\",\"domain\":\"rules\",\"operation\":\"detail\",\"facet\":\"owner_policy\",\"target\":\"\",\"constraints\":[],\"ambiguous\":false}]}",
    "independent_subtask_reviews": null,
    "context_scope_review": null,
    "model_provenance": {
      "base_repository": "typhoon-ai/typhoon2.5-qwen3-4b",
      "base_revision": "ce0a7416fe82d4404b2b4a253ce3ac095ab1252c",
      "adapter_sha256": "e6a342902a0e469181094c05f412b355cef8cb1f57ce03aa78b6705b67f9b0d8",
      "adapter_active": true,
      "stage": "context",
      "quantization": "NF4",
      "profile_digest": "5a5285d8a6cb1eec20d5eb710606cf03ac8313609da41e7769d33b54f6cbed50"
    }
  }
]
```

ผลเกณฑ์เดิม:
```json
[
  {
    "file": "data/eval/intent_trap_bilingual_1000_v1.jsonl",
    "row": 107,
    "variant": "question",
    "id": "INTENT-TRAP-TH-0108",
    "passed": false,
    "failures": [
      "route:knowledge expected:['reservation', 'rules', 'no_answer', 'clarification', 'service_fee']",
      "latency_ceiling"
    ],
    "evidence_level": "literal_content_contract",
    "grader_detail": {
      "strong_outcome_matches": false,
      "positive_content_asserted": false
    },
    "partitions": {
      "protocol": [
        "route:knowledge expected:['reservation', 'rules', 'no_answer', 'clarification', 'service_fee']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    },
    "positive_literal": false,
    "literal_passed": true,
    "literal_errors": []
  },
  {
    "file": "data/eval/intent_trap_bilingual_1000_v2.jsonl",
    "row": 107,
    "variant": "question",
    "id": "INTENT-TRAP-TH-0108",
    "passed": false,
    "failures": [
      "route:knowledge expected:['reservation', 'rules', 'no_answer', 'clarification', 'service_fee']",
      "latency_ceiling"
    ],
    "evidence_level": "literal_content_contract",
    "grader_detail": {
      "strong_outcome_matches": false,
      "positive_content_asserted": false
    },
    "partitions": {
      "protocol": [
        "route:knowledge expected:['reservation', 'rules', 'no_answer', 'clarification', 'service_fee']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    },
    "positive_literal": false,
    "literal_passed": true,
    "literal_errors": []
  }
]
```

### ก่อนเดินทางไปใช้บริการ อยากทราบว่า ถือขวดน้ำเข้าไปได้หรือเปล่า ไม่ได้ถามเรื่องกิน

key: `e57f02961055c3c0a53d1c221408cad728f8813afb52ce12e3b8da79576b2b37`; locale: th

#### R121 trained ที่บันทึกไว้ (มีข้อจำกัด config เดิม)

ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ

HTTP 200; 24.719 วินาที

แผน/การตรวจบริบท:
```json
[
  {
    "stage": "context_understanding",
    "reason": "validated_interpretation_proposal",
    "schema_ok": true,
    "transport_ok": true,
    "raw_content": "{\"focus\":\"food_bring\",\"context_quotes\":[],\"tasks\":[{\"quote\":\"ก่อนเดินทางไปใช้บริการ อยากทราบว่า ถือขวดน้ำเข้าไปได้หรือเปล่า ไม่ได้ถามเรื่องกิน\",\"domain\":\"rules\",\"operation\":\"detail\",\"facet\":\"owner_policy\",\"target\":\"\",\"constraints\":[],\"ambiguous\":false}]}",
    "independent_subtask_reviews": null,
    "context_scope_review": null,
    "model_provenance": {
      "base_repository": "typhoon-ai/typhoon2.5-qwen3-4b",
      "base_revision": "ce0a7416fe82d4404b2b4a253ce3ac095ab1252c",
      "adapter_sha256": "e6a342902a0e469181094c05f412b355cef8cb1f57ce03aa78b6705b67f9b0d8",
      "adapter_active": true,
      "stage": "context",
      "quantization": "NF4",
      "profile_digest": "5a5285d8a6cb1eec20d5eb710606cf03ac8313609da41e7769d33b54f6cbed50"
    }
  }
]
```

ผลเกณฑ์เดิม:
```json
[
  {
    "file": "data/eval/intent_trap_bilingual_1000_v1.jsonl",
    "row": 207,
    "variant": "question",
    "id": "INTENT-TRAP-TH-0208",
    "passed": false,
    "failures": [
      "route:knowledge expected:['rules', 'no_answer', 'clarification']",
      "latency_ceiling"
    ],
    "evidence_level": "literal_content_contract",
    "grader_detail": {
      "strong_outcome_matches": false,
      "positive_content_asserted": false
    },
    "partitions": {
      "protocol": [
        "route:knowledge expected:['rules', 'no_answer', 'clarification']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    },
    "positive_literal": false,
    "literal_passed": true,
    "literal_errors": []
  },
  {
    "file": "data/eval/intent_trap_bilingual_1000_v2.jsonl",
    "row": 207,
    "variant": "question",
    "id": "INTENT-TRAP-TH-0208",
    "passed": false,
    "failures": [
      "route:knowledge expected:['rules', 'no_answer', 'clarification']",
      "latency_ceiling"
    ],
    "evidence_level": "literal_content_contract",
    "grader_detail": {
      "strong_outcome_matches": false,
      "positive_content_asserted": false
    },
    "partitions": {
      "protocol": [
        "route:knowledge expected:['rules', 'no_answer', 'clarification']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    },
    "positive_literal": false,
    "literal_passed": true,
    "literal_errors": []
  }
]
```

#### R122 base

ยังยืนยันคำตอบให้ครบตามสถานการณ์ที่ถามไม่ได้ครับ กรุณาระบุรายละเอียดหรือแยกคำถามเพิ่มเติมอีกนิด

HTTP 200; 65.75 วินาที

แผน/การตรวจบริบท:
```json
[]
```

ผลเกณฑ์เดิม:
```json
[
  {
    "file": "data/eval/intent_trap_bilingual_1000_v1.jsonl",
    "row": 207,
    "variant": "question",
    "id": "INTENT-TRAP-TH-0208",
    "passed": false,
    "failures": [
      "route:knowledge expected:['rules', 'no_answer', 'clarification']",
      "latency_ceiling"
    ],
    "evidence_level": "literal_content_contract",
    "grader_detail": {
      "strong_outcome_matches": false,
      "positive_content_asserted": false
    },
    "partitions": {
      "protocol": [
        "route:knowledge expected:['rules', 'no_answer', 'clarification']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    },
    "positive_literal": false,
    "literal_passed": true,
    "literal_errors": []
  },
  {
    "file": "data/eval/intent_trap_bilingual_1000_v2.jsonl",
    "row": 207,
    "variant": "question",
    "id": "INTENT-TRAP-TH-0208",
    "passed": false,
    "failures": [
      "route:knowledge expected:['rules', 'no_answer', 'clarification']",
      "latency_ceiling"
    ],
    "evidence_level": "literal_content_contract",
    "grader_detail": {
      "strong_outcome_matches": false,
      "positive_content_asserted": false
    },
    "partitions": {
      "protocol": [
        "route:knowledge expected:['rules', 'no_answer', 'clarification']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    },
    "positive_literal": false,
    "literal_passed": true,
    "literal_errors": []
  }
]
```

#### R122 trained

ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ

HTTP 200; 25.297 วินาที

แผน/การตรวจบริบท:
```json
[
  {
    "stage": "context_understanding",
    "reason": "validated_interpretation_proposal",
    "schema_ok": true,
    "transport_ok": true,
    "raw_content": "{\"focus\":\"food_bring\",\"context_quotes\":[],\"tasks\":[{\"quote\":\"ก่อนเดินทางไปใช้บริการ อยากทราบว่า ถือขวดน้ำเข้าไปได้หรือเปล่า ไม่ได้ถามเรื่องกิน\",\"domain\":\"rules\",\"operation\":\"detail\",\"facet\":\"owner_policy\",\"target\":\"\",\"constraints\":[],\"ambiguous\":false}]}",
    "independent_subtask_reviews": null,
    "context_scope_review": null,
    "model_provenance": {
      "base_repository": "typhoon-ai/typhoon2.5-qwen3-4b",
      "base_revision": "ce0a7416fe82d4404b2b4a253ce3ac095ab1252c",
      "adapter_sha256": "e6a342902a0e469181094c05f412b355cef8cb1f57ce03aa78b6705b67f9b0d8",
      "adapter_active": true,
      "stage": "context",
      "quantization": "NF4",
      "profile_digest": "5a5285d8a6cb1eec20d5eb710606cf03ac8313609da41e7769d33b54f6cbed50"
    }
  }
]
```

ผลเกณฑ์เดิม:
```json
[
  {
    "file": "data/eval/intent_trap_bilingual_1000_v1.jsonl",
    "row": 207,
    "variant": "question",
    "id": "INTENT-TRAP-TH-0208",
    "passed": false,
    "failures": [
      "route:knowledge expected:['rules', 'no_answer', 'clarification']",
      "latency_ceiling"
    ],
    "evidence_level": "literal_content_contract",
    "grader_detail": {
      "strong_outcome_matches": false,
      "positive_content_asserted": false
    },
    "partitions": {
      "protocol": [
        "route:knowledge expected:['rules', 'no_answer', 'clarification']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    },
    "positive_literal": false,
    "literal_passed": true,
    "literal_errors": []
  },
  {
    "file": "data/eval/intent_trap_bilingual_1000_v2.jsonl",
    "row": 207,
    "variant": "question",
    "id": "INTENT-TRAP-TH-0208",
    "passed": false,
    "failures": [
      "route:knowledge expected:['rules', 'no_answer', 'clarification']",
      "latency_ceiling"
    ],
    "evidence_level": "literal_content_contract",
    "grader_detail": {
      "strong_outcome_matches": false,
      "positive_content_asserted": false
    },
    "partitions": {
      "protocol": [
        "route:knowledge expected:['rules', 'no_answer', 'clarification']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    },
    "positive_literal": false,
    "literal_passed": true,
    "literal_errors": []
  }
]
```

### What do you need to book to paly FINAL FANTASY XVI

key: `0a00000d589ff1289bde21138edaae2f4071c278c44887ef046325cb4e101ea6`; locale: en

#### R121 trained ที่บันทึกไว้ (มีข้อจำกัด config เดิม)

Which zone, organization audience and half/full-day package do you want?

HTTP 200; 16.484 วินาที

แผน/การตรวจบริบท:
```json
[
  {
    "stage": "context_understanding",
    "reason": "validated_interpretation_proposal",
    "schema_ok": true,
    "transport_ok": true,
    "raw_content": "{\"focus\":\"rental\",\"context_quotes\":[],\"tasks\":[{\"quote\":\"what do you need to book to paly final fantasy xvi\",\"domain\":\"rental\",\"operation\":\"detail\",\"facet\":\"equipment_included\",\"target\":\"\",\"constraints\":[],\"ambiguous\":false}]}",
    "independent_subtask_reviews": null,
    "context_scope_review": null,
    "model_provenance": {
      "base_repository": "typhoon-ai/typhoon2.5-qwen3-4b",
      "base_revision": "ce0a7416fe82d4404b2b4a253ce3ac095ab1252c",
      "adapter_sha256": "e6a342902a0e469181094c05f412b355cef8cb1f57ce03aa78b6705b67f9b0d8",
      "adapter_active": true,
      "stage": "context",
      "quantization": "NF4",
      "profile_digest": "5a5285d8a6cb1eec20d5eb710606cf03ac8313609da41e7769d33b54f6cbed50"
    }
  }
]
```

ผลเกณฑ์เดิม:
```json
[
  {
    "file": "data/eval/master_gt_bilingual_multi_error_2000_20260929_r15.jsonl",
    "row": 1208,
    "variant": "noisy",
    "id": "MASTER-GT-EN-01807",
    "passed": false,
    "failures": [
      "route:knowledge expected:['games', 'reservation']",
      "status:clarification expected:answer_available"
    ],
    "evidence_level": "literal_content_contract",
    "grader_detail": {
      "strong_outcome_matches": false,
      "positive_content_asserted": false
    },
    "partitions": {
      "protocol": [
        "route:knowledge expected:['games', 'reservation']"
      ],
      "outcome": [
        "status:clarification expected:answer_available"
      ]
    },
    "positive_literal": false,
    "literal_passed": true,
    "literal_errors": []
  }
]
```

#### R122 base

FINAL FANTASY XVI — studio services offering this game: PlayStation 5 #01-#02 [S1]

HTTP 200; 59.578 วินาที

แผน/การตรวจบริบท:
```json
[
  {
    "stage": "context_understanding",
    "reason": "independent_context_frame",
    "schema_ok": false,
    "transport_ok": true,
    "raw_content": "{\n  \"focus\": \"booking_procedure\",\n  \"context_quotes\": [\n    \"what do you need to book to paly final fantasy xvi\"\n  ],\n  \"tasks\": [\n    {\n      \"quote\": \"what do you need to book to paly final fantasy xvi\",\n      \"domain\": \"booking_procedure\",\n      \"operation\": \"detail\",\n      \"facet\": \"booking_procedure\",\n      \"target\": \"\",\n      \"constraints\": [\n        {\n          \"slot\": \"audience\",\n          \"quote\": \"\",\n          \"source_record_id\": \"\"\n        },\n        {\n          \"slot\": \"platform\",\n          \"quote\": \"final fantasy xvi\",\n          \"source_record_id\": \"\"\n        },\n        {\n          \"slot\": \"negation\",\n          \"quote\": \"\",\n          \"source_record_id\": \"\"\n        },\n        {\n          \"slot\": \"action\",\n          \"quote\": \"book\",\n          \"source_record_id\": \"\"\n        }\n      ],\n      \"ambiguous\": false\n    }\n  ]\n}",
    "independent_subtask_reviews": null,
    "context_scope_review": null,
    "model_provenance": {
      "base_repository": "typhoon-ai/typhoon2.5-qwen3-4b",
      "base_revision": "ce0a7416fe82d4404b2b4a253ce3ac095ab1252c",
      "adapter_sha256": "e6a342902a0e469181094c05f412b355cef8cb1f57ce03aa78b6705b67f9b0d8",
      "adapter_active": false,
      "stage": "context",
      "quantization": "NF4",
      "profile_digest": "320b656c83f3de56b2ee6d9906df42405bac9a0996df1f1b53b55ac88085ab05"
    }
  }
]
```

ผลเกณฑ์เดิม:
```json
[
  {
    "file": "data/eval/master_gt_bilingual_multi_error_2000_20260929_r15.jsonl",
    "row": 1208,
    "variant": "noisy",
    "id": "MASTER-GT-EN-01807",
    "passed": false,
    "failures": [
      "route:knowledge expected:['games', 'reservation']",
      "latency_ceiling"
    ],
    "evidence_level": "literal_content_contract",
    "grader_detail": {
      "strong_outcome_matches": false,
      "positive_content_asserted": false
    },
    "partitions": {
      "protocol": [
        "route:knowledge expected:['games', 'reservation']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    },
    "positive_literal": false,
    "literal_passed": true,
    "literal_errors": []
  }
]
```

#### R122 trained

FINAL FANTASY XVI — studio services offering this game: PlayStation 5 #01-#02 [S1]

HTTP 200; 17.484 วินาที

แผน/การตรวจบริบท:
```json
[
  {
    "stage": "context_understanding",
    "reason": "independent_context_frame",
    "schema_ok": true,
    "transport_ok": true,
    "raw_content": "{\"focus\":\"rental\",\"context_quotes\":[],\"tasks\":[{\"quote\":\"what do you need to book to paly final fantasy xvi\",\"domain\":\"rental\",\"operation\":\"detail\",\"facet\":\"equipment_included\",\"target\":\"\",\"constraints\":[],\"ambiguous\":false}]}",
    "independent_subtask_reviews": null,
    "context_scope_review": null,
    "model_provenance": {
      "base_repository": "typhoon-ai/typhoon2.5-qwen3-4b",
      "base_revision": "ce0a7416fe82d4404b2b4a253ce3ac095ab1252c",
      "adapter_sha256": "e6a342902a0e469181094c05f412b355cef8cb1f57ce03aa78b6705b67f9b0d8",
      "adapter_active": true,
      "stage": "context",
      "quantization": "NF4",
      "profile_digest": "5a5285d8a6cb1eec20d5eb710606cf03ac8313609da41e7769d33b54f6cbed50"
    }
  }
]
```

ผลเกณฑ์เดิม:
```json
[
  {
    "file": "data/eval/master_gt_bilingual_multi_error_2000_20260929_r15.jsonl",
    "row": 1208,
    "variant": "noisy",
    "id": "MASTER-GT-EN-01807",
    "passed": false,
    "failures": [
      "route:knowledge expected:['games', 'reservation']"
    ],
    "evidence_level": "literal_content_contract",
    "grader_detail": {
      "strong_outcome_matches": false,
      "positive_content_asserted": false
    },
    "partitions": {
      "protocol": [
        "route:knowledge expected:['games', 'reservation']"
      ]
    },
    "positive_literal": false,
    "literal_passed": true,
    "literal_errors": []
  }
]
```

### How to book Cockpit and what days is it open?

key: `a603ab1aed328e10dbf5ac72b6a752be2fb77658ea0365896a1776cd04806370`; locale: en

#### R121 trained ที่บันทึกไว้ (มีข้อจำกัด config เดิม)

1. how to book cockpit
How to book: The booking steps are: select a service, choose date and time, fill in user information, review the details, make payment by bank transfer, and upload the payment slip. [S1]

2. what days is it open
No confirmed source is available for the requested detail.

HTTP 200; 22.156 วินาที

แผน/การตรวจบริบท:
```json
[
  {
    "stage": "context_understanding",
    "reason": "validated_interpretation_proposal",
    "schema_ok": true,
    "transport_ok": true,
    "raw_content": "{\"focus\":\"multiple\",\"context_quotes\":[],\"tasks\":[{\"quote\":\"how to book cockpit\",\"domain\":\"reservation\",\"operation\":\"detail\",\"facet\":\"owner_policy\",\"target\":\"\",\"constraints\":[],\"ambiguous\":false},{\"quote\":\"what days is it open\",\"domain\":\"schedule\",\"operation\":\"detail\",\"facet\":\"bookable_periods\",\"target\":\"\",\"constraints\":[],\"ambiguous\":false}]}",
    "independent_subtask_reviews": null,
    "context_scope_review": null,
    "model_provenance": {
      "base_repository": "typhoon-ai/typhoon2.5-qwen3-4b",
      "base_revision": "ce0a7416fe82d4404b2b4a253ce3ac095ab1252c",
      "adapter_sha256": "e6a342902a0e469181094c05f412b355cef8cb1f57ce03aa78b6705b67f9b0d8",
      "adapter_active": true,
      "stage": "context",
      "quantization": "NF4",
      "profile_digest": "5a5285d8a6cb1eec20d5eb710606cf03ac8313609da41e7769d33b54f6cbed50"
    }
  }
]
```

ผลเกณฑ์เดิม:
```json
[
  {
    "file": "data/eval/english_shadow_1600_machine_20260908.jsonl",
    "row": 1259,
    "variant": "question",
    "id": "EN-SHADOW-1260",
    "passed": false,
    "failures": [
      "route:knowledge expected:['multi_question']",
      "latency_ceiling"
    ],
    "evidence_level": "route_outcome_only",
    "grader_detail": {
      "strong_outcome_matches": null,
      "positive_content_asserted": false
    },
    "partitions": {
      "protocol": [
        "route:knowledge expected:['multi_question']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    },
    "positive_literal": false,
    "literal_passed": null,
    "literal_errors": []
  }
]
```

#### R122 base

Recorded schedule only: zone and effective dates are unconfirmed; some opening-hour sources conflict. This does not confirm current opening or actual booking eligibility.
Monday — regular play-service timetable: 09:00–12:00 maintenance; 13:00–16:00 open for play [S1]
Tuesday — regular play-service timetable: 09:00–12:00 open for play; 13:00–16:00 open for play [S2]
Wednesday — regular play-service timetable: 09:00–12:00 open for play; 13:00–16:00 open for play [S3]
Thursday — regular play-service timetable: 09:00–12:00 open for play; 13:00–16:00 open for play [S4]
Friday — regular play-service timetable: 09:00–12:00 open for play; 13:00–16:00 maintenance [S5]
Saturday — regular play-service timetable: Closed for play under the regular timetable [S6]
Sunday — regular play-service timetable: Closed for play under the regular timetable [S7]

HTTP 200; 47.937 วินาที

แผน/การตรวจบริบท:
```json
[
  {
    "stage": "context_understanding",
    "reason": "r121_vocabulary",
    "schema_ok": false,
    "transport_ok": true,
    "raw_content": "{\n  \"focus\": \"booking_procedure\",\n  \"context_quotes\": [\n    \"how to book cockpit\"\n  ],\n  \"tasks\": [\n    {\n      \"quote\": \"how to book cockpit\",\n      \"domain\": \"booking_procedure\",\n      \"operation\": \"detail\",\n      \"facet\": \"booking_procedure\",\n      \"target\": \"\",\n      \"constraints\": [\n        {\n          \"slot\": \"action\",\n          \"quote\": \"how to book cockpit\",\n          \"source_record_id\": \"\"\n        }\n      ],\n      \"ambiguous\": false\n    },\n    {\n      \"quote\": \"what days is it open?\",\n      \"domain\": \"opening_hours\",\n      \"operation\": \"detail\",\n      \"facet\": \"opening_hours\",\n      \"target\": \"\",\n      \"constraints\": [\n        {\n          \"slot\": \"action\",\n          \"quote\": \"what days is it open?\",\n          \"source_record_id\": \"\"\n        }\n      ],\n      \"ambiguous\": false\n    }\n  ]\n}",
    "independent_subtask_reviews": null,
    "context_scope_review": null,
    "model_provenance": {
      "base_repository": "typhoon-ai/typhoon2.5-qwen3-4b",
      "base_revision": "ce0a7416fe82d4404b2b4a253ce3ac095ab1252c",
      "adapter_sha256": "e6a342902a0e469181094c05f412b355cef8cb1f57ce03aa78b6705b67f9b0d8",
      "adapter_active": false,
      "stage": "context",
      "quantization": "NF4",
      "profile_digest": "320b656c83f3de56b2ee6d9906df42405bac9a0996df1f1b53b55ac88085ab05"
    }
  }
]
```

ผลเกณฑ์เดิม:
```json
[
  {
    "file": "data/eval/english_shadow_1600_machine_20260908.jsonl",
    "row": 1259,
    "variant": "question",
    "id": "EN-SHADOW-1260",
    "passed": false,
    "failures": [
      "route:knowledge expected:['multi_question']",
      "latency_ceiling"
    ],
    "evidence_level": "route_outcome_only",
    "grader_detail": {
      "strong_outcome_matches": null,
      "positive_content_asserted": false
    },
    "partitions": {
      "protocol": [
        "route:knowledge expected:['multi_question']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    },
    "positive_literal": false,
    "literal_passed": null,
    "literal_errors": []
  }
]
```

#### R122 trained

1. how to book cockpit
How to book: The booking steps are: select a service, choose date and time, fill in user information, review the details, make payment by bank transfer, and upload the payment slip. [S1]

2. what days is it open
Recorded schedule only: zone and effective dates are unconfirmed; some opening-hour sources conflict. This does not confirm current opening or actual booking eligibility.
Monday — regular play-service timetable: 09:00–12:00 maintenance; 13:00–16:00 open for play [S2]
Tuesday — regular play-service timetable: 09:00–12:00 open for play; 13:00–16:00 open for play [S3]
Wednesday — regular play-service timetable: 09:00–12:00 open for play; 13:00–16:00 open for play [S4]
Thursday — regular play-service timetable: 09:00–12:00 open for play; 13:00–16:00 open for play [S5]
Friday — regular play-service timetable: 09:00–12:00 open for play; 13:00–16:00 maintenance [S6]
Saturday — regular play-service timetable: Closed for play under the regular timetable [S7]
Sunday — regular play-service timetable: Closed for play under the regular timetable [S8]

HTTP 200; 22.485 วินาที

แผน/การตรวจบริบท:
```json
[
  {
    "stage": "context_understanding",
    "reason": "validated_interpretation_proposal",
    "schema_ok": true,
    "transport_ok": true,
    "raw_content": "{\"focus\":\"multiple\",\"context_quotes\":[],\"tasks\":[{\"quote\":\"how to book cockpit\",\"domain\":\"reservation\",\"operation\":\"detail\",\"facet\":\"owner_policy\",\"target\":\"\",\"constraints\":[],\"ambiguous\":false},{\"quote\":\"what days is it open\",\"domain\":\"schedule\",\"operation\":\"detail\",\"facet\":\"bookable_periods\",\"target\":\"\",\"constraints\":[],\"ambiguous\":false}]}",
    "independent_subtask_reviews": null,
    "context_scope_review": null,
    "model_provenance": {
      "base_repository": "typhoon-ai/typhoon2.5-qwen3-4b",
      "base_revision": "ce0a7416fe82d4404b2b4a253ce3ac095ab1252c",
      "adapter_sha256": "e6a342902a0e469181094c05f412b355cef8cb1f57ce03aa78b6705b67f9b0d8",
      "adapter_active": true,
      "stage": "context",
      "quantization": "NF4",
      "profile_digest": "5a5285d8a6cb1eec20d5eb710606cf03ac8313609da41e7769d33b54f6cbed50"
    }
  }
]
```

ผลเกณฑ์เดิม:
```json
[
  {
    "file": "data/eval/english_shadow_1600_machine_20260908.jsonl",
    "row": 1259,
    "variant": "question",
    "id": "EN-SHADOW-1260",
    "passed": false,
    "failures": [
      "route:knowledge expected:['multi_question']",
      "latency_ceiling"
    ],
    "evidence_level": "route_outcome_only",
    "grader_detail": {
      "strong_outcome_matches": null,
      "positive_content_asserted": false
    },
    "partitions": {
      "protocol": [
        "route:knowledge expected:['multi_question']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    },
    "positive_literal": false,
    "literal_passed": null,
    "literal_errors": []
  }
]
```

### Please use verified studio information: What ID does an external visitor need to use the studio?

key: `1cf7db3858a13e4841f441117b1a23c40c3e46cf26be6bc9d0b7bb64314f0993`; locale: en

#### R121 trained ที่บันทึกไว้ (มีข้อจำกัด config เดิม)

external visitors: External visitors may use all general studio services. Tournament eligibility is separate. [S1]

HTTP 200; 16.703 วินาที

แผน/การตรวจบริบท:
```json
[
  {
    "stage": "context_understanding",
    "reason": "r121_vocabulary",
    "schema_ok": false,
    "transport_ok": true,
    "raw_content": "{\"focus\":\"identity\",\"context_quotes\":[],\"tasks\":[{\"quote\":\"please use verified studio information: what id does an external visitor need to use the studio?\",\"domain\":\"identity\",\"operation\":\"detail\",\"facet\":\"value\",\"target\":\"\",\"constraints\":[],\"ambiguous\":false}]}",
    "independent_subtask_reviews": null,
    "context_scope_review": null,
    "model_provenance": {
      "base_repository": "typhoon-ai/typhoon2.5-qwen3-4b",
      "base_revision": "ce0a7416fe82d4404b2b4a253ce3ac095ab1252c",
      "adapter_sha256": "e6a342902a0e469181094c05f412b355cef8cb1f57ce03aa78b6705b67f9b0d8",
      "adapter_active": true,
      "stage": "context",
      "quantization": "NF4",
      "profile_digest": "5a5285d8a6cb1eec20d5eb710606cf03ac8313609da41e7769d33b54f6cbed50"
    }
  }
]
```

ผลเกณฑ์เดิม:
```json
[
  {
    "file": "data/eval/intent_trap_bilingual_1000_v1.jsonl",
    "row": 649,
    "variant": "question",
    "id": "INTENT-TRAP-EN-0150",
    "passed": false,
    "failures": [
      "route:knowledge expected:['reservation', 'rules', 'no_answer', 'clarification', 'service_fee']"
    ],
    "evidence_level": "literal_content_contract",
    "grader_detail": {
      "strong_outcome_matches": false,
      "positive_content_asserted": false
    },
    "partitions": {
      "protocol": [
        "route:knowledge expected:['reservation', 'rules', 'no_answer', 'clarification', 'service_fee']"
      ]
    },
    "positive_literal": false,
    "literal_passed": true,
    "literal_errors": []
  },
  {
    "file": "data/eval/intent_trap_bilingual_1000_v2.jsonl",
    "row": 649,
    "variant": "question",
    "id": "INTENT-TRAP-EN-0150",
    "passed": false,
    "failures": [
      "route:knowledge expected:['reservation', 'rules', 'no_answer', 'clarification', 'service_fee']"
    ],
    "evidence_level": "literal_content_contract",
    "grader_detail": {
      "strong_outcome_matches": false,
      "positive_content_asserted": false
    },
    "partitions": {
      "protocol": [
        "route:knowledge expected:['reservation', 'rules', 'no_answer', 'clarification', 'service_fee']"
      ]
    },
    "positive_literal": false,
    "literal_passed": true,
    "literal_errors": []
  },
  {
    "file": "data/eval/intent_trap_english_reference_200_20260926.jsonl",
    "row": 49,
    "variant": "question",
    "id": "INTENT-TRAP-EN-0150",
    "passed": true,
    "failures": [],
    "evidence_level": "route_outcome_only",
    "grader_detail": {
      "strong_outcome_matches": null,
      "positive_content_asserted": false
    },
    "partitions": {},
    "positive_literal": false,
    "literal_passed": null,
    "literal_errors": []
  }
]
```

#### R122 base

Check-in document: When checking in to use the service, you must present your student ID card, staff ID card, or national identification card. [S1]
What documents must I present upon arrival?: At arrival, present a national ID card, university student card, school student card, or passport. [S2]

HTTP 200; 38.547 วินาที

แผน/การตรวจบริบท:
```json
[
  {
    "stage": "context_understanding",
    "reason": "independent_context_frame",
    "schema_ok": false,
    "transport_ok": true,
    "raw_content": "{\n  \"focus\": \"identity\",\n  \"context_quotes\": [\n    \"please use verified studio information: what id does an external visitor need to use the studio?\"\n  ],\n  \"tasks\": [\n    {\n      \"quote\": \"what id does an external visitor need to use the studio?\",\n      \"domain\": \"identity\",\n      \"operation\": \"detail\",\n      \"facet\": \"identity\",\n      \"target\": \"what id\",\n      \"constraints\": [\n        {\n          \"slot\": \"audience\",\n          \"quote\": \"external visitor\",\n          \"source_record_id\": \"\"\n        }\n      ],\n      \"ambiguous\": false\n    }\n  ]\n}",
    "independent_subtask_reviews": null,
    "context_scope_review": null,
    "model_provenance": {
      "base_repository": "typhoon-ai/typhoon2.5-qwen3-4b",
      "base_revision": "ce0a7416fe82d4404b2b4a253ce3ac095ab1252c",
      "adapter_sha256": "e6a342902a0e469181094c05f412b355cef8cb1f57ce03aa78b6705b67f9b0d8",
      "adapter_active": false,
      "stage": "context",
      "quantization": "NF4",
      "profile_digest": "320b656c83f3de56b2ee6d9906df42405bac9a0996df1f1b53b55ac88085ab05"
    }
  },
  {
    "stage": null,
    "reason": null,
    "schema_ok": true,
    "transport_ok": true,
    "raw_content": "{\"plans\": [{\"i\": 0, \"choices\": [1, 2]}]}",
    "independent_subtask_reviews": null,
    "context_scope_review": null,
    "model_provenance": {
      "base_repository": "typhoon-ai/typhoon2.5-qwen3-4b",
      "base_revision": "ce0a7416fe82d4404b2b4a253ce3ac095ab1252c",
      "adapter_sha256": "e6a342902a0e469181094c05f412b355cef8cb1f57ce03aa78b6705b67f9b0d8",
      "adapter_active": false,
      "stage": "evidence_selection",
      "quantization": "NF4",
      "profile_digest": "320b656c83f3de56b2ee6d9906df42405bac9a0996df1f1b53b55ac88085ab05"
    }
  }
]
```

ผลเกณฑ์เดิม:
```json
[
  {
    "file": "data/eval/intent_trap_bilingual_1000_v1.jsonl",
    "row": 649,
    "variant": "question",
    "id": "INTENT-TRAP-EN-0150",
    "passed": false,
    "failures": [
      "route:knowledge expected:['reservation', 'rules', 'no_answer', 'clarification', 'service_fee']",
      "latency_ceiling"
    ],
    "evidence_level": "literal_content_contract",
    "grader_detail": {
      "strong_outcome_matches": false,
      "positive_content_asserted": false
    },
    "partitions": {
      "protocol": [
        "route:knowledge expected:['reservation', 'rules', 'no_answer', 'clarification', 'service_fee']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    },
    "positive_literal": false,
    "literal_passed": true,
    "literal_errors": []
  },
  {
    "file": "data/eval/intent_trap_bilingual_1000_v2.jsonl",
    "row": 649,
    "variant": "question",
    "id": "INTENT-TRAP-EN-0150",
    "passed": false,
    "failures": [
      "route:knowledge expected:['reservation', 'rules', 'no_answer', 'clarification', 'service_fee']",
      "latency_ceiling"
    ],
    "evidence_level": "literal_content_contract",
    "grader_detail": {
      "strong_outcome_matches": false,
      "positive_content_asserted": false
    },
    "partitions": {
      "protocol": [
        "route:knowledge expected:['reservation', 'rules', 'no_answer', 'clarification', 'service_fee']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    },
    "positive_literal": false,
    "literal_passed": true,
    "literal_errors": []
  },
  {
    "file": "data/eval/intent_trap_english_reference_200_20260926.jsonl",
    "row": 49,
    "variant": "question",
    "id": "INTENT-TRAP-EN-0150",
    "passed": false,
    "failures": [
      "latency_ceiling"
    ],
    "evidence_level": "route_outcome_only",
    "grader_detail": {
      "strong_outcome_matches": null,
      "positive_content_asserted": false
    },
    "partitions": {
      "performance": [
        "latency_ceiling"
      ]
    },
    "positive_literal": false,
    "literal_passed": null,
    "literal_errors": []
  }
]
```

#### R122 trained

Check-in document: When checking in to use the service, you must present your student ID card, staff ID card, or national identification card. [S1]
What documents must I present upon arrival?: At arrival, present a national ID card, university student card, school student card, or passport. [S2]

HTTP 200; 22.015 วินาที

แผน/การตรวจบริบท:
```json
[
  {
    "stage": "context_understanding",
    "reason": "independent_context_frame",
    "schema_ok": false,
    "transport_ok": true,
    "raw_content": "{\"focus\":\"identity\",\"context_quotes\":[],\"tasks\":[{\"quote\":\"please use verified studio information: what id does an external visitor need to use the studio?\",\"domain\":\"identity\",\"operation\":\"detail\",\"facet\":\"value\",\"target\":\"\",\"constraints\":[],\"ambiguous\":false}]}",
    "independent_subtask_reviews": null,
    "context_scope_review": null,
    "model_provenance": {
      "base_repository": "typhoon-ai/typhoon2.5-qwen3-4b",
      "base_revision": "ce0a7416fe82d4404b2b4a253ce3ac095ab1252c",
      "adapter_sha256": "e6a342902a0e469181094c05f412b355cef8cb1f57ce03aa78b6705b67f9b0d8",
      "adapter_active": true,
      "stage": "context",
      "quantization": "NF4",
      "profile_digest": "5a5285d8a6cb1eec20d5eb710606cf03ac8313609da41e7769d33b54f6cbed50"
    }
  },
  {
    "stage": null,
    "reason": null,
    "schema_ok": true,
    "transport_ok": true,
    "raw_content": "{\"plans\": [{\"i\": 0, \"choices\": [1, 2]}]}",
    "independent_subtask_reviews": null,
    "context_scope_review": null,
    "model_provenance": {
      "base_repository": "typhoon-ai/typhoon2.5-qwen3-4b",
      "base_revision": "ce0a7416fe82d4404b2b4a253ce3ac095ab1252c",
      "adapter_sha256": "e6a342902a0e469181094c05f412b355cef8cb1f57ce03aa78b6705b67f9b0d8",
      "adapter_active": false,
      "stage": "evidence_selection",
      "quantization": "NF4",
      "profile_digest": "5a5285d8a6cb1eec20d5eb710606cf03ac8313609da41e7769d33b54f6cbed50"
    }
  }
]
```

ผลเกณฑ์เดิม:
```json
[
  {
    "file": "data/eval/intent_trap_bilingual_1000_v1.jsonl",
    "row": 649,
    "variant": "question",
    "id": "INTENT-TRAP-EN-0150",
    "passed": false,
    "failures": [
      "route:knowledge expected:['reservation', 'rules', 'no_answer', 'clarification', 'service_fee']",
      "latency_ceiling"
    ],
    "evidence_level": "literal_content_contract",
    "grader_detail": {
      "strong_outcome_matches": false,
      "positive_content_asserted": false
    },
    "partitions": {
      "protocol": [
        "route:knowledge expected:['reservation', 'rules', 'no_answer', 'clarification', 'service_fee']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    },
    "positive_literal": false,
    "literal_passed": true,
    "literal_errors": []
  },
  {
    "file": "data/eval/intent_trap_bilingual_1000_v2.jsonl",
    "row": 649,
    "variant": "question",
    "id": "INTENT-TRAP-EN-0150",
    "passed": false,
    "failures": [
      "route:knowledge expected:['reservation', 'rules', 'no_answer', 'clarification', 'service_fee']",
      "latency_ceiling"
    ],
    "evidence_level": "literal_content_contract",
    "grader_detail": {
      "strong_outcome_matches": false,
      "positive_content_asserted": false
    },
    "partitions": {
      "protocol": [
        "route:knowledge expected:['reservation', 'rules', 'no_answer', 'clarification', 'service_fee']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    },
    "positive_literal": false,
    "literal_passed": true,
    "literal_errors": []
  },
  {
    "file": "data/eval/intent_trap_english_reference_200_20260926.jsonl",
    "row": 49,
    "variant": "question",
    "id": "INTENT-TRAP-EN-0150",
    "passed": false,
    "failures": [
      "latency_ceiling"
    ],
    "evidence_level": "route_outcome_only",
    "grader_detail": {
      "strong_outcome_matches": null,
      "positive_content_asserted": false
    },
    "partitions": {
      "performance": [
        "latency_ceiling"
      ]
    },
    "positive_literal": false,
    "literal_passed": null,
    "literal_errors": []
  }
]
```
