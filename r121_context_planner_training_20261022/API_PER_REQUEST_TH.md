# R121 — ผลแชท API ก่อน/หลัง adapter

คำถามเดิม 8 ข้อต่อแขน ฐานข้อมูลและ candidate Flow เดียวกัน เปลี่ยนเฉพาะ context adapter ไม่ใช่ Full Test; positive literal checks ไม่ใช่ semantic accuracy และ strict protocol ของ benchmark เดิมต้องอ่านแยก

## ตัวเลขที่วัดได้

```json
{
  "base": {
    "requests": 8,
    "http_200": 8,
    "validation_ok": 8,
    "grades": 15,
    "strict_pass": 0,
    "positive_grades": 5,
    "positive_pass": 0,
    "positive_requests": 2,
    "timed_out": 0,
    "model_events": 9,
    "transport_ok": 9,
    "schema_ok": 2,
    "provenance_verified_events": 9,
    "context_events": 7,
    "adapter_profile_matches": 7,
    "selector_events": 2,
    "selector_adapter_disabled": 2,
    "failure_partition_occurrences": {
      "protocol": 14,
      "content_or_format": 6,
      "evidence_identifier": 1,
      "performance": 15
    },
    "latency_median_sec": 52.0
  },
  "trained": {
    "requests": 8,
    "http_200": 8,
    "validation_ok": 8,
    "grades": 15,
    "strict_pass": 1,
    "positive_grades": 5,
    "positive_pass": 0,
    "positive_requests": 2,
    "timed_out": 0,
    "model_events": 10,
    "transport_ok": 10,
    "schema_ok": 8,
    "provenance_verified_events": 10,
    "context_events": 8,
    "adapter_profile_matches": 8,
    "selector_events": 2,
    "selector_adapter_disabled": 2,
    "failure_partition_occurrences": {
      "protocol": 14,
      "content_or_format": 6,
      "evidence_identifier": 1,
      "performance": 11,
      "outcome": 1
    },
    "latency_median_sec": 22.6955
  }
}
```

## รายข้อ

### Under CS2 tournamment ruls, may I change Brightness, Resolution and Crosshair, and where?

key: `ef5c0b5af4c6794d174d9a9d329fe7e2535c1fac26b3cf0fd1d69f084d64ca96`; locale: en

#### base

The clause or its required references are incomplete; this rule cannot be confirmed.

HTTP 200; 79.52 วินาที; positive literal 0/1 grades

แผนและหลักฐาน model transport:
```json
[
  {
    "stage": "context_understanding",
    "transport_ok": true,
    "schema_ok": false,
    "reason": "r121_focus",
    "error": null,
    "context_focus": null,
    "context_quotes": null,
    "raw_content": "{\n  \"focus\": \"rules\",\n  \"context_quotes\": [\n    \"under cs2 tournamment ruls, may i change brightness, resolution and crosshair, and where?\"\n  ],\n  \"tasks\": [\n    {\n      \"quote\": \"under cs2 tournamment ruls, may i change brightness, resolution and crosshair, and where?\",\n      \"domain\": \"rules\",\n      \"operation\": \"rule_lookup\",\n      \"facet\": \"competition_rules\",\n      \"target\": \"rule_clause\",\n      \"constraints\": [\n            {\n              \"slot\": \"audience\",\n              \"quote\": \"under cs2 tournamment ruls\",\n              \"source_record_id\": \"\"\n            },\n            {\n              \"slot\": \"negation\",\n              \"quote\": \"may i\",\n              \"source_record_id\": \"\"\n            },\n            {\n              \"slot\": \"action\",\n              \"quote\": \"change brightness, resolution and crosshair\",\n              \"source_record_id\": \"\"\n            },\n            {\n              \"slot\": \"location\",\n              \"quote\": \"and where?\",\n              \"source_record_id\": \"\"\n            }\n          ],\n      \"ambiguous\": false\n    }\n  ]\n}",
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

ผลตรวจ benchmark เดิม:
```json
[
  {
    "id": "R28-cs2-custom-settings-en-2",
    "passed": false,
    "positive_literal": true,
    "literal_passed": false,
    "literal_errors": [
      "missing_complete_clause:Players may customize brightness, resolution, and crosshair settings only within the game and computer monitor."
    ],
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
    }
  }
]
```

#### trained

A confirmed English translation is unavailable for some clauses; their Thai source text is retained below.
PSU Phuket CS2 2026 Tournament — 1. Players may customize brightness, resolution, and crosshair settings exclusively within the game and computer screen only: 1. Players may customize brightness, resolution, and crosshair settings only within the game and computer screen exclusively. [S1]
PSU Phuket CS2 2026 Tournament — การตั้งค่าเกม: ผู้เล่นสามารถปรับแต่งความสว่าง (Brightness), ความละเอียดหน้าจอ (Resolution) และเป้าเล็ง (Crosshair) เฉพาะในเกม และหน้าจอคอมพิวเตอร์เท่านั้น [S2]

HTTP 200; 43.28 วินาที; positive literal 0/1 grades

แผนและหลักฐาน model transport:
```json
[
  {
    "stage": "context_understanding",
    "transport_ok": true,
    "schema_ok": true,
    "reason": "validated_interpretation_proposal",
    "error": null,
    "context_focus": "competition_rules",
    "context_quotes": [],
    "raw_content": "{\"focus\":\"competition_rules\",\"context_quotes\":[],\"tasks\":[{\"quote\":\"under cs2 tournamment ruls, may i change brightness, resolution and crosshair, and where?\",\"domain\":\"competition_rules\",\"operation\":\"rule_lookup\",\"facet\":\"rule_clause\",\"target\":\"cs2\",\"constraints\":[],\"ambiguous\":false}]}",
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
    "transport_ok": true,
    "schema_ok": true,
    "reason": null,
    "error": null,
    "context_focus": null,
    "context_quotes": null,
    "raw_content": "{\"plans\": [{\"i\": 0, \"choices\": [1, 2]}]}",
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

ผลตรวจ benchmark เดิม:
```json
[
  {
    "id": "R28-cs2-custom-settings-en-2",
    "passed": false,
    "positive_literal": true,
    "literal_passed": false,
    "literal_errors": [
      "missing_complete_clause:Players may customize brightness, resolution, and crosshair settings only within the game and computer monitor."
    ],
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
    }
  }
]
```

### ขอสอบถามหน่อยครับ Nintendo Switch Zone มีอะไรให้ใช้บ้าง

key: `2d97cb1b2297d0a2bf6c2073dfec0e79e2d0ec3995b47987e2b1eef242f70c70`; locale: th

#### base

Nintendo Switch (1-2 Persons) — รายชื่อเกมทั้งหมด: Pokémon Champions; Animal Crossing: New Horizons; It Takes Two; Little Nightmares II; Luigi's Mansion 3; Mario Kart 8 Deluxe; Mario Party Superstars; Monster Hunter Rise; Moving Out 2; New Super Mario Bros. U Deluxe; Nintendo Switch Sports; Overcooked!; Overcooked 2; Ring Fit Adventure; Super Mario Odyssey; Super Smash Bros Ultimate; The Legend of Zelda: Breath of the Wild [S1]
Nintendo Switch (1-4 Persons) — รายชื่อเกมทั้งหมด: Pokémon Champions; Animal Crossing: New Horizons; It Takes Two; Little Nightmares II; Luigi's Mansion 3; Mario Kart 8 Deluxe; Mario Party Superstars; Monster Hunter Rise; Moving Out 2; New Super Mario Bros. U Deluxe; Nintendo Switch Sports; Overcooked!; Overcooked 2; Ring Fit Adventure; Super Mario Odyssey; Super Smash Bros Ultimate; The Legend of Zelda: Breath of the Wild [S2]

HTTP 200; 30.22 วินาที; positive literal 0/4 grades

แผนและหลักฐาน model transport:
```json
[
  {
    "stage": "context_understanding",
    "transport_ok": true,
    "schema_ok": false,
    "reason": "r121_facet",
    "error": null,
    "context_focus": null,
    "context_quotes": null,
    "raw_content": "{\n  \"focus\": \"equipment_inventory\",\n  \"context_quotes\": [\n    \"nintendo switch zone มีอะไรให้ใช้บ้าง\"\n  ],\n  \"tasks\": [\n    {\n      \"quote\": \"nintendo switch zone มีอะไรให้ใช้บ้าง\",\n      \"domain\": \"equipment\",\n      \"operation\": \"detail\",\n      \"facet\": \"equipment_inventory\",\n      \"target\": \"\",\n      \"constraints\": [],\n      \"ambiguous\": false\n    }\n  ]\n}",
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
    "transport_ok": true,
    "schema_ok": true,
    "reason": null,
    "error": null,
    "context_focus": null,
    "context_quotes": null,
    "raw_content": "{\"plans\": [{\"i\": 0, \"choices\": [1, 2]}]}",
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

ผลตรวจ benchmark เดิม:
```json
[
  {
    "id": "MASTER-GT-TH-03500",
    "passed": false,
    "positive_literal": true,
    "literal_passed": false,
    "literal_errors": [
      "missing all alternatives: ['อุปกรณ์', 'หมายถึงเรื่องไหน', 'Zone']"
    ],
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
    }
  },
  {
    "id": "MASTER-GT-TH-03500",
    "passed": false,
    "positive_literal": true,
    "literal_passed": false,
    "literal_errors": [
      "missing all alternatives: ['อุปกรณ์', 'หมายถึงเรื่องไหน', 'Zone']"
    ],
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
    }
  },
  {
    "id": "MASTER-GT-TH-03500",
    "passed": false,
    "positive_literal": true,
    "literal_passed": false,
    "literal_errors": [
      "missing all alternatives: ['อุปกรณ์', 'หมายถึงเรื่องไหน', 'Zone']"
    ],
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
    }
  },
  {
    "id": "MASTER-GT-TH-03500",
    "passed": false,
    "positive_literal": true,
    "literal_passed": false,
    "literal_errors": [
      "missing all alternatives: ['อุปกรณ์', 'หมายถึงเรื่องไหน', 'Zone']"
    ],
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
    }
  }
]
```

#### trained

Nintendo Switch (1-2 Persons) — รายชื่อเกมทั้งหมด: Pokémon Champions; Animal Crossing: New Horizons; It Takes Two; Little Nightmares II; Luigi's Mansion 3; Mario Kart 8 Deluxe; Mario Party Superstars; Monster Hunter Rise; Moving Out 2; New Super Mario Bros. U Deluxe; Nintendo Switch Sports; Overcooked!; Overcooked 2; Ring Fit Adventure; Super Mario Odyssey; Super Smash Bros Ultimate; The Legend of Zelda: Breath of the Wild [S1]
Nintendo Switch (1-4 Persons) — รายชื่อเกมทั้งหมด: Pokémon Champions; Animal Crossing: New Horizons; It Takes Two; Little Nightmares II; Luigi's Mansion 3; Mario Kart 8 Deluxe; Mario Party Superstars; Monster Hunter Rise; Moving Out 2; New Super Mario Bros. U Deluxe; Nintendo Switch Sports; Overcooked!; Overcooked 2; Ring Fit Adventure; Super Mario Odyssey; Super Smash Bros Ultimate; The Legend of Zelda: Breath of the Wild [S2]

HTTP 200; 22.06 วินาที; positive literal 0/4 grades

แผนและหลักฐาน model transport:
```json
[
  {
    "stage": "context_understanding",
    "transport_ok": true,
    "schema_ok": false,
    "reason": "r121_unbound_target",
    "error": null,
    "context_focus": null,
    "context_quotes": null,
    "raw_content": "{\"focus\":\"equipment_inventory\",\"context_quotes\":[],\"tasks\":[{\"quote\":\"nintendo switch zone มีอะไรให้ใช้บ้าง\",\"domain\":\"equipment\",\"operation\":\"list\",\"facet\":\"usage\",\"target\":\"Nintendo Switch\",\"constraints\":[],\"ambiguous\":false}]}",
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
    "transport_ok": true,
    "schema_ok": true,
    "reason": null,
    "error": null,
    "context_focus": null,
    "context_quotes": null,
    "raw_content": "{\"plans\": [{\"i\": 0, \"choices\": [1, 2]}]}",
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

ผลตรวจ benchmark เดิม:
```json
[
  {
    "id": "MASTER-GT-TH-03500",
    "passed": false,
    "positive_literal": true,
    "literal_passed": false,
    "literal_errors": [
      "missing all alternatives: ['อุปกรณ์', 'หมายถึงเรื่องไหน', 'Zone']"
    ],
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
    }
  },
  {
    "id": "MASTER-GT-TH-03500",
    "passed": false,
    "positive_literal": true,
    "literal_passed": false,
    "literal_errors": [
      "missing all alternatives: ['อุปกรณ์', 'หมายถึงเรื่องไหน', 'Zone']"
    ],
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
    }
  },
  {
    "id": "MASTER-GT-TH-03500",
    "passed": false,
    "positive_literal": true,
    "literal_passed": false,
    "literal_errors": [
      "missing all alternatives: ['อุปกรณ์', 'หมายถึงเรื่องไหน', 'Zone']"
    ],
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
    }
  },
  {
    "id": "MASTER-GT-TH-03500",
    "passed": false,
    "positive_literal": true,
    "literal_passed": false,
    "literal_errors": [
      "missing all alternatives: ['อุปกรณ์', 'หมายถึงเรื่องไหน', 'Zone']"
    ],
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
    }
  }
]
```

### What are the 8 buttons in Tekken 8, ans what is the PC price

key: `d91ee50a1f6c21f141226b55bb86aaea2935e3a4b5e73b339ff4d83b81a1deaa`; locale: en

#### base

Rates last reaffirmed by the owner on 2026-10-20; no new effective interval was established.
PC #01-#02 / PSU Student and Staff — per-person price for the rate duration: 0 THB per person for 60 minutes [S1]
PC #01-#02 / PSU Alumni and General Student — per-person price for the rate duration: 25 THB per person for 60 minutes [S2]
PC #01-#02 / General Adult — per-person price for the rate duration: 70 THB per person for 60 minutes [S3]
PC #03-#10 / PSU Student and Staff — per-person price for the rate duration: 0 THB per person for 60 minutes [S4]
PC #03-#10 / PSU Alumni and General Student — per-person price for the rate duration: 25 THB per person for 60 minutes [S5]
PC #03-#10 / General Adult — per-person price for the rate duration: 70 THB per person for 60 minutes [S6]

HTTP 200; 25.88 วินาที; positive literal 0/0 grades

แผนและหลักฐาน model transport:
```json
[
  {
    "stage": "context_understanding",
    "transport_ok": true,
    "schema_ok": false,
    "reason": "independent_context_frame",
    "error": null,
    "context_focus": null,
    "context_quotes": null,
    "raw_content": "{\n  \"focus\": \"game_controls\",\n  \"context_quotes\": [\n    \"what are the 8 buttons in tekken 8\"\n  ],\n  \"tasks\": [\n    {\n      \"quote\": \"what are the 8 buttons in tekken 8\",\n      \"domain\": \"game_controls\",\n      \"operation\": \"detail\",\n      \"facet\": \"input_bindings\",\n      \"target\": \"8 buttons in Tekken 8\",\n      \"constraints\": [],\n      \"ambiguous\": false\n    }\n  ]\n}",
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

ผลตรวจ benchmark เดิม:
```json
[
  {
    "id": "MASTER-GT-EN-04868",
    "passed": false,
    "positive_literal": false,
    "literal_passed": true,
    "literal_errors": [],
    "partitions": {
      "protocol": [
        "route:knowledge expected:['multi_question']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    }
  }
]
```

#### trained

TEKKEN 8 — how to play: Play in rounds. Select a character. Practice basic moves/combo sequences. Read your opponent's timing and reduce their health to zero first. [S1]

Rates last reaffirmed by the owner on 2026-10-20; no new effective interval was established.
PC #01-#02 / PSU Student and Staff — per-person price for the rate duration: 0 THB per person for 60 minutes [S2]
PC #01-#02 / PSU Alumni and General Student — per-person price for the rate duration: 25 THB per person for 60 minutes [S3]
PC #01-#02 / General Adult — per-person price for the rate duration: 70 THB per person for 60 minutes [S4]
PC #03-#10 / PSU Student and Staff — per-person price for the rate duration: 0 THB per person for 60 minutes [S5]
PC #03-#10 / PSU Alumni and General Student — per-person price for the rate duration: 25 THB per person for 60 minutes [S6]
PC #03-#10 / General Adult — per-person price for the rate duration: 70 THB per person for 60 minutes [S7]

HTTP 200; 26.95 วินาที; positive literal 0/0 grades

แผนและหลักฐาน model transport:
```json
[
  {
    "stage": "context_understanding",
    "transport_ok": true,
    "schema_ok": true,
    "reason": "validated_interpretation_proposal",
    "error": null,
    "context_focus": "multiple",
    "context_quotes": [],
    "raw_content": "{\"focus\":\"multiple\",\"context_quotes\":[],\"tasks\":[{\"quote\":\"what are the 8 buttons in tekken 8\",\"domain\":\"games\",\"operation\":\"detail\",\"facet\":\"how_to_play\",\"target\":\"tekken 8\",\"constraints\":[],\"ambiguous\":false},{\"quote\":\"what is the pc price\",\"domain\":\"service_fee\",\"operation\":\"price_calculate\",\"facet\":\"amount\",\"target\":\"tekken 8\",\"constraints\":[],\"ambiguous\":false}]}",
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

ผลตรวจ benchmark เดิม:
```json
[
  {
    "id": "MASTER-GT-EN-04868",
    "passed": false,
    "positive_literal": false,
    "literal_passed": true,
    "literal_errors": [],
    "partitions": {
      "protocol": [
        "route:knowledge expected:['multi_question']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    }
  }
]
```

### ก่อนเดินทางไปใช้บริการ อยากทราบว่า คนที่ไม่ใช่นักศึกษา PSU เข้าไปเล่นได้หรือเปล่า

key: `490a5b13b782510c507fdb5692383211a2537734caa8e7e489f42932969ea534`; locale: th

#### base

ระบบตีความคำถามไม่พร้อมชั่วคราว กรุณาลองอีกครั้งครับ

HTTP 200; 54.94 วินาที; positive literal 0/0 grades

แผนและหลักฐาน model transport:
```json
[
  {
    "stage": "context_understanding",
    "transport_ok": true,
    "schema_ok": false,
    "reason": "r121_vocabulary",
    "error": null,
    "context_focus": null,
    "context_quotes": null,
    "raw_content": "{\n  \"focus\": \"eligibility\",\n  \"context_quotes\": [\n    \"ก่อนเดินทางไปใช้บริการ อยากทราบว่า คนที่ไม่ใช่นักศึกษา psu เข้าไปเล่นได้หรือเปล่า\"\n  ],\n  \"tasks\": [\n    {\n      \"quote\": \"ก่อนเดินทางไปใช้บริการ อยากทราบว่า คนที่ไม่ใช่นักศึกษา psu เข้าไปเล่นได้หรือเปล่า\",\n      \"domain\": \"eligibility\",\n      \"operation\": \"availability\",\n      \"facet\": \"eligibility\",\n      \"target\": \"คนที่ไม่ใช่นักศึกษา psu เข้าไปเล่นได้หรือเปล่า\",\n      \"constraints\": [\n        {\n          \"slot\": \"audience\",\n          \"quote\": \"คนที่ไม่ใช่นักศึกษา psu\",\n          \"source_record_id\": \"\"\n        }\n      ],\n      \"ambiguous\": false\n    }\n  ]\n}",
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

ผลตรวจ benchmark เดิม:
```json
[
  {
    "id": "INTENT-TRAP-TH-0108",
    "passed": false,
    "positive_literal": false,
    "literal_passed": true,
    "literal_errors": [],
    "partitions": {
      "protocol": [
        "route:knowledge expected:['reservation', 'rules', 'no_answer', 'clarification', 'service_fee']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    }
  },
  {
    "id": "INTENT-TRAP-TH-0108",
    "passed": false,
    "positive_literal": false,
    "literal_passed": true,
    "literal_errors": [],
    "partitions": {
      "protocol": [
        "route:knowledge expected:['reservation', 'rules', 'no_answer', 'clarification', 'service_fee']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    }
  }
]
```

#### trained

ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ

HTTP 200; 23.23 วินาที; positive literal 0/0 grades

แผนและหลักฐาน model transport:
```json
[
  {
    "stage": "context_understanding",
    "transport_ok": true,
    "schema_ok": true,
    "reason": "validated_interpretation_proposal",
    "error": null,
    "context_focus": "eligibility",
    "context_quotes": [],
    "raw_content": "{\"focus\":\"eligibility\",\"context_quotes\":[],\"tasks\":[{\"quote\":\"ก่อนเดินทางไปใช้บริการ อยากทราบว่า คนที่ไม่ใช่นักศึกษา psu เข้าไปเล่นได้หรือเปล่า\",\"domain\":\"rules\",\"operation\":\"detail\",\"facet\":\"owner_policy\",\"target\":\"\",\"constraints\":[],\"ambiguous\":false}]}",
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

ผลตรวจ benchmark เดิม:
```json
[
  {
    "id": "INTENT-TRAP-TH-0108",
    "passed": false,
    "positive_literal": false,
    "literal_passed": true,
    "literal_errors": [],
    "partitions": {
      "protocol": [
        "route:knowledge expected:['reservation', 'rules', 'no_answer', 'clarification', 'service_fee']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    }
  },
  {
    "id": "INTENT-TRAP-TH-0108",
    "passed": false,
    "positive_literal": false,
    "literal_passed": true,
    "literal_errors": [],
    "partitions": {
      "protocol": [
        "route:knowledge expected:['reservation', 'rules', 'no_answer', 'clarification', 'service_fee']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    }
  }
]
```

### ก่อนเดินทางไปใช้บริการ อยากทราบว่า ถือขวดน้ำเข้าไปได้หรือเปล่า ไม่ได้ถามเรื่องกิน

key: `e57f02961055c3c0a53d1c221408cad728f8813afb52ce12e3b8da79576b2b37`; locale: th

#### base

ยังยืนยันคำตอบให้ครบตามสถานการณ์ที่ถามไม่ได้ครับ กรุณาระบุรายละเอียดหรือแยกคำถามเพิ่มเติมอีกนิด

HTTP 200; 53.97 วินาที; positive literal 0/0 grades

แผนและหลักฐาน model transport:
```json
[]
```

ผลตรวจ benchmark เดิม:
```json
[
  {
    "id": "INTENT-TRAP-TH-0208",
    "passed": false,
    "positive_literal": false,
    "literal_passed": true,
    "literal_errors": [],
    "partitions": {
      "protocol": [
        "route:knowledge expected:['rules', 'no_answer', 'clarification']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    }
  },
  {
    "id": "INTENT-TRAP-TH-0208",
    "passed": false,
    "positive_literal": false,
    "literal_passed": true,
    "literal_errors": [],
    "partitions": {
      "protocol": [
        "route:knowledge expected:['rules', 'no_answer', 'clarification']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    }
  }
]
```

#### trained

ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ

HTTP 200; 24.72 วินาที; positive literal 0/0 grades

แผนและหลักฐาน model transport:
```json
[
  {
    "stage": "context_understanding",
    "transport_ok": true,
    "schema_ok": true,
    "reason": "validated_interpretation_proposal",
    "error": null,
    "context_focus": "food_bring",
    "context_quotes": [],
    "raw_content": "{\"focus\":\"food_bring\",\"context_quotes\":[],\"tasks\":[{\"quote\":\"ก่อนเดินทางไปใช้บริการ อยากทราบว่า ถือขวดน้ำเข้าไปได้หรือเปล่า ไม่ได้ถามเรื่องกิน\",\"domain\":\"rules\",\"operation\":\"detail\",\"facet\":\"owner_policy\",\"target\":\"\",\"constraints\":[],\"ambiguous\":false}]}",
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

ผลตรวจ benchmark เดิม:
```json
[
  {
    "id": "INTENT-TRAP-TH-0208",
    "passed": false,
    "positive_literal": false,
    "literal_passed": true,
    "literal_errors": [],
    "partitions": {
      "protocol": [
        "route:knowledge expected:['rules', 'no_answer', 'clarification']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    }
  },
  {
    "id": "INTENT-TRAP-TH-0208",
    "passed": false,
    "positive_literal": false,
    "literal_passed": true,
    "literal_errors": [],
    "partitions": {
      "protocol": [
        "route:knowledge expected:['rules', 'no_answer', 'clarification']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    }
  }
]
```

### What do you need to book to paly FINAL FANTASY XVI

key: `0a00000d589ff1289bde21138edaae2f4071c278c44887ef046325cb4e101ea6`; locale: en

#### base

FINAL FANTASY XVI — studio services offering this game: PlayStation 5 #01-#02 [S1]

HTTP 200; 53.92 วินาที; positive literal 0/0 grades

แผนและหลักฐาน model transport:
```json
[
  {
    "stage": "context_understanding",
    "transport_ok": true,
    "schema_ok": false,
    "reason": "r121_vocabulary",
    "error": null,
    "context_focus": null,
    "context_quotes": null,
    "raw_content": "{\n  \"focus\": \"booking_procedure\",\n  \"context_quotes\": [\n    \"what do you need to book to paly final fantasy xvi\"\n  ],\n  \"tasks\": [\n    {\n      \"quote\": \"what do you need to book to paly final fantasy xvi\",\n      \"domain\": \"booking_procedure\",\n      \"operation\": \"detail\",\n      \"facet\": \"booking_procedure\",\n      \"target\": \"\",\n      \"constraints\": [\n        {\n          \"slot\": \"audience\",\n          \"quote\": \"\",\n          \"source_record_id\": \"\"\n        },\n        {\n          \"slot\": \"platform\",\n          \"quote\": \"final fantasy xvi\",\n          \"source_record_id\": \"\"\n        },\n        {\n          \"slot\": \"negation\",\n          \"quote\": \"\",\n          \"source_record_id\": \"\"\n        },\n        {\n          \"slot\": \"action\",\n          \"quote\": \"book\",\n          \"source_record_id\": \"\"\n        }\n      ],\n      \"ambiguous\": false\n    }\n  ]\n}",
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
    "transport_ok": true,
    "schema_ok": true,
    "reason": null,
    "error": null,
    "context_focus": null,
    "context_quotes": null,
    "raw_content": "{\"plans\": [{\"i\": 0, \"choices\": [2]}]}",
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

ผลตรวจ benchmark เดิม:
```json
[
  {
    "id": "MASTER-GT-EN-01807",
    "passed": false,
    "positive_literal": false,
    "literal_passed": true,
    "literal_errors": [],
    "partitions": {
      "protocol": [
        "route:knowledge expected:['games', 'reservation']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    }
  }
]
```

#### trained

Which zone, organization audience and half/full-day package do you want?

HTTP 200; 16.48 วินาที; positive literal 0/0 grades

แผนและหลักฐาน model transport:
```json
[
  {
    "stage": "context_understanding",
    "transport_ok": true,
    "schema_ok": true,
    "reason": "validated_interpretation_proposal",
    "error": null,
    "context_focus": "rental",
    "context_quotes": [],
    "raw_content": "{\"focus\":\"rental\",\"context_quotes\":[],\"tasks\":[{\"quote\":\"what do you need to book to paly final fantasy xvi\",\"domain\":\"rental\",\"operation\":\"detail\",\"facet\":\"equipment_included\",\"target\":\"\",\"constraints\":[],\"ambiguous\":false}]}",
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

ผลตรวจ benchmark เดิม:
```json
[
  {
    "id": "MASTER-GT-EN-01807",
    "passed": false,
    "positive_literal": false,
    "literal_passed": true,
    "literal_errors": [],
    "partitions": {
      "protocol": [
        "route:knowledge expected:['games', 'reservation']"
      ],
      "outcome": [
        "status:clarification expected:answer_available"
      ]
    }
  }
]
```

### How to book Cockpit and what days is it open?

key: `a603ab1aed328e10dbf5ac72b6a752be2fb77658ea0365896a1776cd04806370`; locale: en

#### base

1. how to book cockpit
Selected service/game: Cockpit #01-#02

**Relevant information**
• Confirmed information: The booking steps are: select a service, choose date and time, fill in user information, review the details, make payment by bank transfer, and upload the payment slip. [S1]

English translation is machine generated and has not been reviewed by the owner.

2. what days is it open
This part is not clear yet. Please specify its topic or item.

HTTP 200; 50.08 วินาที; positive literal 0/0 grades

แผนและหลักฐาน model transport:
```json
[
  {
    "stage": "context_understanding",
    "transport_ok": true,
    "schema_ok": false,
    "reason": "r121_vocabulary",
    "error": null,
    "context_focus": null,
    "context_quotes": null,
    "raw_content": "{\n  \"focus\": \"booking_procedure\",\n  \"context_quotes\": [\n    \"how to book cockpit\"\n  ],\n  \"tasks\": [\n    {\n      \"quote\": \"how to book cockpit\",\n      \"domain\": \"booking_procedure\",\n      \"operation\": \"detail\",\n      \"facet\": \"booking_procedure\",\n      \"target\": \"\",\n      \"constraints\": [\n        {\n          \"slot\": \"action\",\n          \"quote\": \"how to book cockpit\",\n          \"source_record_id\": \"\"\n        }\n      ],\n      \"ambiguous\": false\n    },\n    {\n      \"quote\": \"what days is it open?\",\n      \"domain\": \"opening_hours\",\n      \"operation\": \"detail\",\n      \"facet\": \"opening_hours\",\n      \"target\": \"\",\n      \"constraints\": [\n        {\n          \"slot\": \"action\",\n          \"quote\": \"what days is it open?\",\n          \"source_record_id\": \"\"\n        }\n      ],\n      \"ambiguous\": false\n    }\n  ]\n}",
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

ผลตรวจ benchmark เดิม:
```json
[
  {
    "id": "EN-SHADOW-1260",
    "passed": false,
    "positive_literal": false,
    "literal_passed": null,
    "literal_errors": [],
    "partitions": {
      "protocol": [
        "route:knowledge expected:['multi_question']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    }
  }
]
```

#### trained

1. how to book cockpit
How to book: The booking steps are: select a service, choose date and time, fill in user information, review the details, make payment by bank transfer, and upload the payment slip. [S1]

2. what days is it open
No confirmed source is available for the requested detail.

HTTP 200; 22.16 วินาที; positive literal 0/0 grades

แผนและหลักฐาน model transport:
```json
[
  {
    "stage": "context_understanding",
    "transport_ok": true,
    "schema_ok": true,
    "reason": "validated_interpretation_proposal",
    "error": null,
    "context_focus": "multiple",
    "context_quotes": [],
    "raw_content": "{\"focus\":\"multiple\",\"context_quotes\":[],\"tasks\":[{\"quote\":\"how to book cockpit\",\"domain\":\"reservation\",\"operation\":\"detail\",\"facet\":\"owner_policy\",\"target\":\"\",\"constraints\":[],\"ambiguous\":false},{\"quote\":\"what days is it open\",\"domain\":\"schedule\",\"operation\":\"detail\",\"facet\":\"bookable_periods\",\"target\":\"\",\"constraints\":[],\"ambiguous\":false}]}",
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

ผลตรวจ benchmark เดิม:
```json
[
  {
    "id": "EN-SHADOW-1260",
    "passed": false,
    "positive_literal": false,
    "literal_passed": null,
    "literal_errors": [],
    "partitions": {
      "protocol": [
        "route:knowledge expected:['multi_question']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    }
  }
]
```

### Please use verified studio information: What ID does an external visitor need to use the studio?

key: `1cf7db3858a13e4841f441117b1a23c40c3e46cf26be6bc9d0b7bb64314f0993`; locale: en

#### base

external visitors: External visitors may use all general studio services. Tournament eligibility is separate. [S1]

HTTP 200; 31.81 วินาที; positive literal 0/0 grades

แผนและหลักฐาน model transport:
```json
[
  {
    "stage": "context_understanding",
    "transport_ok": true,
    "schema_ok": false,
    "reason": "r121_vocabulary",
    "error": null,
    "context_focus": null,
    "context_quotes": null,
    "raw_content": "{\n  \"focus\": \"identity\",\n  \"context_quotes\": [\n    \"please use verified studio information: what id does an external visitor need to use the studio?\"\n  ],\n  \"tasks\": [\n    {\n      \"quote\": \"what id does an external visitor need to use the studio?\",\n      \"domain\": \"identity\",\n      \"operation\": \"detail\",\n      \"facet\": \"identity\",\n      \"target\": \"what id\",\n      \"constraints\": [\n        {\n          \"slot\": \"audience\",\n          \"quote\": \"external visitor\",\n          \"source_record_id\": \"\"\n        }\n      ],\n      \"ambiguous\": false\n    }\n  ]\n}",
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

ผลตรวจ benchmark เดิม:
```json
[
  {
    "id": "INTENT-TRAP-EN-0150",
    "passed": false,
    "positive_literal": false,
    "literal_passed": true,
    "literal_errors": [],
    "partitions": {
      "protocol": [
        "route:knowledge expected:['reservation', 'rules', 'no_answer', 'clarification', 'service_fee']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    }
  },
  {
    "id": "INTENT-TRAP-EN-0150",
    "passed": false,
    "positive_literal": false,
    "literal_passed": true,
    "literal_errors": [],
    "partitions": {
      "protocol": [
        "route:knowledge expected:['reservation', 'rules', 'no_answer', 'clarification', 'service_fee']"
      ],
      "performance": [
        "latency_ceiling"
      ]
    }
  },
  {
    "id": "INTENT-TRAP-EN-0150",
    "passed": false,
    "positive_literal": false,
    "literal_passed": null,
    "literal_errors": [],
    "partitions": {
      "performance": [
        "latency_ceiling"
      ]
    }
  }
]
```

#### trained

external visitors: External visitors may use all general studio services. Tournament eligibility is separate. [S1]

HTTP 200; 16.70 วินาที; positive literal 0/0 grades

แผนและหลักฐาน model transport:
```json
[
  {
    "stage": "context_understanding",
    "transport_ok": true,
    "schema_ok": false,
    "reason": "r121_vocabulary",
    "error": null,
    "context_focus": null,
    "context_quotes": null,
    "raw_content": "{\"focus\":\"identity\",\"context_quotes\":[],\"tasks\":[{\"quote\":\"please use verified studio information: what id does an external visitor need to use the studio?\",\"domain\":\"identity\",\"operation\":\"detail\",\"facet\":\"value\",\"target\":\"\",\"constraints\":[],\"ambiguous\":false}]}",
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

ผลตรวจ benchmark เดิม:
```json
[
  {
    "id": "INTENT-TRAP-EN-0150",
    "passed": false,
    "positive_literal": false,
    "literal_passed": true,
    "literal_errors": [],
    "partitions": {
      "protocol": [
        "route:knowledge expected:['reservation', 'rules', 'no_answer', 'clarification', 'service_fee']"
      ]
    }
  },
  {
    "id": "INTENT-TRAP-EN-0150",
    "passed": false,
    "positive_literal": false,
    "literal_passed": true,
    "literal_errors": [],
    "partitions": {
      "protocol": [
        "route:knowledge expected:['reservation', 'rules', 'no_answer', 'clarification', 'service_fee']"
      ]
    }
  },
  {
    "id": "INTENT-TRAP-EN-0150",
    "passed": true,
    "positive_literal": false,
    "literal_passed": null,
    "literal_errors": [],
    "partitions": {}
  }
]
```
