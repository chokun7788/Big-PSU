# R121 — ตรวจการเชื่อม Flow หลังวิเคราะห์ข้อผิดพลาด

**เป็น posthoc development/regression ไม่ใช่ fresh held-out accuracy** ใช้ adapter เดิมตลอด ไม่มีการฝึกเพิ่มหรือเพิ่มคำถามใหม่ การวัด 30 ข้อของโมเดลยังเก็บแยกตามเดิม

## api02

```json
{
  "requests": 8,
  "http_200": 8,
  "positive_literal_pass": 0,
  "positive_literal_grades": 5,
  "positive_literal_requests": 2,
  "latency_median_sec": 22.6955,
  "new_questions": 0,
  "fresh_heldout": false,
  "frozen_source_unchanged": true
}
```

### Under CS2 tournamment ruls, may I change Brightness, Resolution and Crosshair, and where?

A confirmed English translation is unavailable for some clauses; their Thai source text is retained below.
PSU Phuket CS2 2026 Tournament — 1. Players may customize brightness, resolution, and crosshair settings exclusively within the game and computer screen only: 1. Players may customize brightness, resolution, and crosshair settings only within the game and computer screen exclusively. [S1]
PSU Phuket CS2 2026 Tournament — การตั้งค่าเกม: ผู้เล่นสามารถปรับแต่งความสว่าง (Brightness), ความละเอียดหน้าจอ (Resolution) และเป้าเล็ง (Crosshair) เฉพาะในเกม และหน้าจอคอมพิวเตอร์เท่านั้น [S2]

key `ef5c0b5af4c6794d174d9a9d329fe7e2535c1fac26b3cf0fd1d69f084d64ca96`; HTTP 200; 43.281 วินาที

```json
{
  "understanding_accepted": true,
  "tasks": [
    {
      "quote": "under cs2 tournamment ruls, may i change brightness, resolution and crosshair, and where?",
      "domain": "competition_rules",
      "category": "C13",
      "operation": "rule_lookup",
      "facet": "rule_clause",
      "target": "cs2",
      "constraints": [],
      "ambiguous": false
    }
  ],
  "source_quote_repairs": null,
  "independent_subtask_reviews": null,
  "meaning_review": null,
  "needs": [
    {
      "category": "C13",
      "status": "supported",
      "reason_codes": [
        "bounded_model_selection"
      ],
      "execution_query": "under cs2 tournamment ruls, may i change brightness, resolution and crosshair, and where? "
    }
  ],
  "literal_grades": [
    {
      "id": "R28-cs2-custom-settings-en-2",
      "literal_passed": false,
      "literal_errors": [
        "missing_complete_clause:Players may customize brightness, resolution, and crosshair settings only within the game and computer monitor."
      ]
    }
  ]
}
```

### ขอสอบถามหน่อยครับ Nintendo Switch Zone มีอะไรให้ใช้บ้าง

Nintendo Switch (1-2 Persons) — รายชื่อเกมทั้งหมด: Pokémon Champions; Animal Crossing: New Horizons; It Takes Two; Little Nightmares II; Luigi's Mansion 3; Mario Kart 8 Deluxe; Mario Party Superstars; Monster Hunter Rise; Moving Out 2; New Super Mario Bros. U Deluxe; Nintendo Switch Sports; Overcooked!; Overcooked 2; Ring Fit Adventure; Super Mario Odyssey; Super Smash Bros Ultimate; The Legend of Zelda: Breath of the Wild [S1]
Nintendo Switch (1-4 Persons) — รายชื่อเกมทั้งหมด: Pokémon Champions; Animal Crossing: New Horizons; It Takes Two; Little Nightmares II; Luigi's Mansion 3; Mario Kart 8 Deluxe; Mario Party Superstars; Monster Hunter Rise; Moving Out 2; New Super Mario Bros. U Deluxe; Nintendo Switch Sports; Overcooked!; Overcooked 2; Ring Fit Adventure; Super Mario Odyssey; Super Smash Bros Ultimate; The Legend of Zelda: Breath of the Wild [S2]

key `2d97cb1b2297d0a2bf6c2073dfec0e79e2d0ec3995b47987e2b1eef242f70c70`; HTTP 200; 22.063 วินาที

```json
{
  "understanding_accepted": false,
  "tasks": [],
  "source_quote_repairs": null,
  "independent_subtask_reviews": null,
  "meaning_review": null,
  "needs": [
    {
      "category": "C04",
      "status": "supported",
      "reason_codes": [
        "bounded_model_selection"
      ],
      "execution_query": "nintendo switch zone มีอะไรให้ใช้บ้าง"
    }
  ],
  "literal_grades": [
    {
      "id": "MASTER-GT-TH-03500",
      "literal_passed": false,
      "literal_errors": [
        "missing all alternatives: ['อุปกรณ์', 'หมายถึงเรื่องไหน', 'Zone']"
      ]
    },
    {
      "id": "MASTER-GT-TH-03500",
      "literal_passed": false,
      "literal_errors": [
        "missing all alternatives: ['อุปกรณ์', 'หมายถึงเรื่องไหน', 'Zone']"
      ]
    },
    {
      "id": "MASTER-GT-TH-03500",
      "literal_passed": false,
      "literal_errors": [
        "missing all alternatives: ['อุปกรณ์', 'หมายถึงเรื่องไหน', 'Zone']"
      ]
    },
    {
      "id": "MASTER-GT-TH-03500",
      "literal_passed": false,
      "literal_errors": [
        "missing all alternatives: ['อุปกรณ์', 'หมายถึงเรื่องไหน', 'Zone']"
      ]
    }
  ]
}
```

### What are the 8 buttons in Tekken 8, ans what is the PC price

TEKKEN 8 — how to play: Play in rounds. Select a character. Practice basic moves/combo sequences. Read your opponent's timing and reduce their health to zero first. [S1]

Rates last reaffirmed by the owner on 2026-10-20; no new effective interval was established.
PC #01-#02 / PSU Student and Staff — per-person price for the rate duration: 0 THB per person for 60 minutes [S2]
PC #01-#02 / PSU Alumni and General Student — per-person price for the rate duration: 25 THB per person for 60 minutes [S3]
PC #01-#02 / General Adult — per-person price for the rate duration: 70 THB per person for 60 minutes [S4]
PC #03-#10 / PSU Student and Staff — per-person price for the rate duration: 0 THB per person for 60 minutes [S5]
PC #03-#10 / PSU Alumni and General Student — per-person price for the rate duration: 25 THB per person for 60 minutes [S6]
PC #03-#10 / General Adult — per-person price for the rate duration: 70 THB per person for 60 minutes [S7]

key `d91ee50a1f6c21f141226b55bb86aaea2935e3a4b5e73b339ff4d83b81a1deaa`; HTTP 200; 26.953 วินาที

```json
{
  "understanding_accepted": true,
  "tasks": [
    {
      "quote": "what are the 8 buttons in tekken 8",
      "domain": "games",
      "category": "C04",
      "operation": "detail",
      "facet": "how_to_play",
      "target": "tekken 8",
      "constraints": [],
      "ambiguous": false
    },
    {
      "quote": "what is the pc price",
      "domain": "service_fee",
      "category": "C06",
      "operation": "price_calculate",
      "facet": "amount",
      "target": "tekken 8",
      "constraints": [],
      "ambiguous": false
    }
  ],
  "source_quote_repairs": null,
  "independent_subtask_reviews": null,
  "meaning_review": null,
  "needs": [
    {
      "category": "C04",
      "status": "supported",
      "reason_codes": [
        "meaning_bound_requested_field"
      ],
      "execution_query": "what are the 8 buttons in tekken 8 "
    },
    {
      "category": "C06",
      "status": "supported",
      "reason_codes": [
        "typed_requested_fields"
      ],
      "execution_query": "what is the pc price TEKKEN 8"
    }
  ],
  "literal_grades": []
}
```

### ก่อนเดินทางไปใช้บริการ อยากทราบว่า คนที่ไม่ใช่นักศึกษา PSU เข้าไปเล่นได้หรือเปล่า

ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ

key `490a5b13b782510c507fdb5692383211a2537734caa8e7e489f42932969ea534`; HTTP 200; 23.235 วินาที

```json
{
  "understanding_accepted": true,
  "tasks": [
    {
      "quote": "ก่อนเดินทางไปใช้บริการ อยากทราบว่า คนที่ไม่ใช่นักศึกษา psu เข้าไปเล่นได้หรือเปล่า",
      "domain": "rules",
      "category": "C10",
      "operation": "detail",
      "facet": "owner_policy",
      "target": "",
      "constraints": [],
      "ambiguous": false
    }
  ],
  "source_quote_repairs": null,
  "independent_subtask_reviews": null,
  "meaning_review": null,
  "needs": [
    {
      "category": "C10",
      "status": "missing_source",
      "reason_codes": [
        "entity_not_bound"
      ],
      "execution_query": "ก่อนเดินทางไปใช้บริการ อยากทราบว่า คนที่ไม่ใช่นักศึกษา psu เข้าไปเล่นได้หรือเปล่า "
    }
  ],
  "literal_grades": []
}
```

### ก่อนเดินทางไปใช้บริการ อยากทราบว่า ถือขวดน้ำเข้าไปได้หรือเปล่า ไม่ได้ถามเรื่องกิน

ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ

key `e57f02961055c3c0a53d1c221408cad728f8813afb52ce12e3b8da79576b2b37`; HTTP 200; 24.719 วินาที

```json
{
  "understanding_accepted": true,
  "tasks": [
    {
      "quote": "ก่อนเดินทางไปใช้บริการ อยากทราบว่า ถือขวดน้ำเข้าไปได้หรือเปล่า ไม่ได้ถามเรื่องกิน",
      "domain": "rules",
      "category": "C10",
      "operation": "detail",
      "facet": "owner_policy",
      "target": "",
      "constraints": [],
      "ambiguous": false
    }
  ],
  "source_quote_repairs": null,
  "independent_subtask_reviews": null,
  "meaning_review": null,
  "needs": [
    {
      "category": "C10",
      "status": "missing_source",
      "reason_codes": [
        "entity_not_bound"
      ],
      "execution_query": "ก่อนเดินทางไปใช้บริการ อยากทราบว่า ถือขวดน้ำเข้าไปได้หรือเปล่า ไม่ได้ถามเรื่องกิน "
    }
  ],
  "literal_grades": []
}
```

### What do you need to book to paly FINAL FANTASY XVI

Which zone, organization audience and half/full-day package do you want?

key `0a00000d589ff1289bde21138edaae2f4071c278c44887ef046325cb4e101ea6`; HTTP 200; 16.484 วินาที

```json
{
  "understanding_accepted": true,
  "tasks": [
    {
      "quote": "what do you need to book to paly final fantasy xvi",
      "domain": "rental",
      "category": "C07",
      "operation": "detail",
      "facet": "equipment_included",
      "target": "",
      "constraints": [],
      "ambiguous": false
    }
  ],
  "source_quote_repairs": null,
  "independent_subtask_reviews": null,
  "meaning_review": null,
  "needs": [
    {
      "category": "C07",
      "status": "needs_user_slot",
      "reason_codes": [
        "financial_subject_not_bound"
      ],
      "execution_query": "what do you need to book to paly final fantasy xvi "
    }
  ],
  "literal_grades": []
}
```

### How to book Cockpit and what days is it open?

1. how to book cockpit
How to book: The booking steps are: select a service, choose date and time, fill in user information, review the details, make payment by bank transfer, and upload the payment slip. [S1]

2. what days is it open
No confirmed source is available for the requested detail.

key `a603ab1aed328e10dbf5ac72b6a752be2fb77658ea0365896a1776cd04806370`; HTTP 200; 22.156 วินาที

```json
{
  "understanding_accepted": true,
  "tasks": [
    {
      "quote": "how to book cockpit",
      "domain": "reservation",
      "category": "C08",
      "operation": "detail",
      "facet": "owner_policy",
      "target": "",
      "constraints": [],
      "ambiguous": false
    },
    {
      "quote": "what days is it open",
      "domain": "schedule",
      "category": "C11",
      "operation": "detail",
      "facet": "bookable_periods",
      "target": "",
      "constraints": [],
      "ambiguous": false
    }
  ],
  "source_quote_repairs": null,
  "independent_subtask_reviews": null,
  "meaning_review": null,
  "needs": [
    {
      "category": "C08",
      "status": "supported",
      "reason_codes": [
        "declared_legacy_query_profile"
      ],
      "execution_query": "how to book cockpit "
    },
    {
      "category": "C11",
      "status": "missing_source",
      "reason_codes": [
        "entity_not_bound"
      ],
      "execution_query": "what days is it open "
    }
  ],
  "literal_grades": []
}
```

### Please use verified studio information: What ID does an external visitor need to use the studio?

external visitors: External visitors may use all general studio services. Tournament eligibility is separate. [S1]

key `1cf7db3858a13e4841f441117b1a23c40c3e46cf26be6bc9d0b7bb64314f0993`; HTTP 200; 16.703 วินาที

```json
{
  "understanding_accepted": false,
  "tasks": [],
  "source_quote_repairs": null,
  "independent_subtask_reviews": null,
  "meaning_review": null,
  "needs": [
    {
      "category": "C10",
      "status": "supported",
      "reason_codes": [
        "equivalent_literal_policy_sources"
      ],
      "execution_query": "please use verified studio information: what id does an external visitor need to use the studio"
    }
  ],
  "literal_grades": []
}
```

## guard01

```json
{
  "requests": 14,
  "http_200": 14,
  "positive_literal_pass": 14,
  "positive_literal_grades": 17,
  "positive_literal_requests": 6,
  "latency_median_sec": 24.508,
  "new_questions": 0,
  "fresh_heldout": false,
  "frozen_source_unchanged": true,
  "same_original_8_questions": {
    "positive_pass": 4,
    "positive_grades": 5
  }
}
```

### Under CS2 tournamment ruls, may I change Brightness, Resolution and Crosshair, and where?

A confirmed English translation is unavailable for some clauses; their Thai source text is retained below.
PSU Phuket CS2 2026 Tournament — 1. Players may customize brightness, resolution, and crosshair settings exclusively within the game and computer screen only: 1. Players may customize brightness, resolution, and crosshair settings only within the game and computer screen exclusively. [S1]
PSU Phuket CS2 2026 Tournament — การตั้งค่าเกม: ผู้เล่นสามารถปรับแต่งความสว่าง (Brightness), ความละเอียดหน้าจอ (Resolution) และเป้าเล็ง (Crosshair) เฉพาะในเกม และหน้าจอคอมพิวเตอร์เท่านั้น [S2]

key `ef5c0b5af4c6794d174d9a9d329fe7e2535c1fac26b3cf0fd1d69f084d64ca96`; HTTP 200; 46.359 วินาที

```json
{
  "understanding_accepted": true,
  "tasks": [
    {
      "quote": "under cs2 tournamment ruls, may i change brightness, resolution and crosshair, and where?",
      "domain": "competition_rules",
      "category": "C13",
      "operation": "rule_lookup",
      "facet": "rule_clause",
      "target": "cs2",
      "constraints": [],
      "ambiguous": false
    }
  ],
  "source_quote_repairs": null,
  "independent_subtask_reviews": null,
  "meaning_review": null,
  "needs": [
    {
      "category": "C13",
      "status": "supported",
      "reason_codes": [
        "bounded_model_selection"
      ],
      "execution_query": "under cs2 tournamment ruls, may i change brightness, resolution and crosshair, and where? "
    }
  ],
  "literal_grades": [
    {
      "id": "R28-cs2-custom-settings-en-2",
      "literal_passed": false,
      "literal_errors": [
        "missing_complete_clause:Players may customize brightness, resolution, and crosshair settings only within the game and computer monitor."
      ]
    }
  ]
}
```

### ขอสอบถามหน่อยครับ Nintendo Switch Zone มีอะไรให้ใช้บ้าง

Nintendo Switch OLED — การใช้งาน: เครื่องเกม Nintendo Switch รุ่น OLED สำหรับเล่นเกมคอนโซลแบบกลุ่มหรือครอบครัว
จอง Nintendo Switch Zone แล้วเล่นผ่าน TV 86 นิ้วและจอยที่ศูนย์จัดไว้ตามรอบบริการ
เล่น Mario Kart 8 Deluxe
เล่น Overcooked 2
เล่น Super Smash Bros Ultimate
เล่น Nintendo Switch Sports [S1]

key `2d97cb1b2297d0a2bf6c2073dfec0e79e2d0ec3995b47987e2b1eef242f70c70`; HTTP 200; 16.047 วินาที

```json
{
  "understanding_accepted": true,
  "tasks": [
    {
      "quote": "nintendo switch zone มีอะไรให้ใช้บ้าง",
      "domain": "equipment",
      "category": "C03",
      "operation": "list",
      "facet": "usage",
      "target": "nintendo switch",
      "constraints": [],
      "ambiguous": false
    }
  ],
  "source_quote_repairs": [
    {
      "path": "tasks[0].target",
      "model_quote": "Nintendo Switch",
      "source_quote": "nintendo switch",
      "basis": "unique_case_insensitive_source_span"
    }
  ],
  "independent_subtask_reviews": null,
  "meaning_review": null,
  "needs": [
    {
      "category": "C03",
      "status": "supported",
      "reason_codes": [
        "meaning_bound_requested_field"
      ],
      "execution_query": "nintendo switch zone มีอะไรให้ใช้บ้าง "
    }
  ],
  "literal_grades": [
    {
      "id": "MASTER-GT-TH-03500",
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "id": "MASTER-GT-TH-03500",
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "id": "MASTER-GT-TH-03500",
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "id": "MASTER-GT-TH-03500",
      "literal_passed": true,
      "literal_errors": []
    }
  ]
}
```

### What are the 8 buttons in Tekken 8, ans what is the PC price

No confirmed source is available for the requested detail.

Rates last reaffirmed by the owner on 2026-10-20; no new effective interval was established.
PC #01-#02 / PSU Student and Staff — per-person price for the rate duration: 0 THB per person for 60 minutes [S1]
PC #01-#02 / PSU Alumni and General Student — per-person price for the rate duration: 25 THB per person for 60 minutes [S2]
PC #01-#02 / General Adult — per-person price for the rate duration: 70 THB per person for 60 minutes [S3]
PC #03-#10 / PSU Student and Staff — per-person price for the rate duration: 0 THB per person for 60 minutes [S4]
PC #03-#10 / PSU Alumni and General Student — per-person price for the rate duration: 25 THB per person for 60 minutes [S5]
PC #03-#10 / General Adult — per-person price for the rate duration: 70 THB per person for 60 minutes [S6]

key `d91ee50a1f6c21f141226b55bb86aaea2935e3a4b5e73b339ff4d83b81a1deaa`; HTTP 200; 31.360 วินาที

```json
{
  "understanding_accepted": true,
  "tasks": [
    {
      "quote": "what are the 8 buttons in tekken 8",
      "domain": "equipment",
      "category": "C03",
      "operation": "detail",
      "facet": "usage",
      "target": "tekken 8",
      "constraints": [],
      "ambiguous": false
    },
    {
      "quote": "what is the pc price",
      "domain": "service_fee",
      "category": "C06",
      "operation": "price_calculate",
      "facet": "amount",
      "target": "tekken 8",
      "constraints": [],
      "ambiguous": false
    }
  ],
  "source_quote_repairs": null,
  "independent_subtask_reviews": [
    {
      "basis": "source_equipment_definition_before_name_echo",
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
    }
  ],
  "meaning_review": null,
  "needs": [
    {
      "category": "C03",
      "status": "missing_source",
      "reason_codes": [
        "bounded_model_selection"
      ],
      "execution_query": "what are the 8 buttons in tekken 8 "
    },
    {
      "category": "C06",
      "status": "supported",
      "reason_codes": [
        "typed_requested_fields"
      ],
      "execution_query": "what is the pc price TEKKEN 8"
    }
  ],
  "literal_grades": []
}
```

### ก่อนเดินทางไปใช้บริการ อยากทราบว่า คนที่ไม่ใช่นักศึกษา PSU เข้าไปเล่นได้หรือเปล่า

ผู้ใช้ภายนอก: บุคคลภายนอกใช้บริการทั่วไปได้ทั้งหมด; ไม่ขยายไปเป็นคุณสมบัติแข่ง CS2 ซึ่งเอกสารกำหนดนักศึกษา PSU ภูเก็ต [S1]

key `490a5b13b782510c507fdb5692383211a2537734caa8e7e489f42932969ea534`; HTTP 200; 23.813 วินาที

```json
{
  "understanding_accepted": true,
  "tasks": [
    {
      "quote": "ก่อนเดินทางไปใช้บริการ อยากทราบว่า คนที่ไม่ใช่นักศึกษา psu เข้าไปเล่นได้หรือเปล่า",
      "domain": "rules",
      "category": "C10",
      "operation": "detail",
      "facet": "owner_policy",
      "target": "",
      "constraints": [],
      "ambiguous": false
    }
  ],
  "source_quote_repairs": null,
  "independent_subtask_reviews": null,
  "meaning_review": null,
  "needs": [
    {
      "category": "C10",
      "status": "supported",
      "reason_codes": [
        "equivalent_literal_policy_sources"
      ],
      "execution_query": "ก่อนเดินทางไปใช้บริการ อยากทราบว่า คนที่ไม่ใช่นักศึกษา psu เข้าไปเล่นได้หรือเปล่า "
    }
  ],
  "literal_grades": []
}
```

### ก่อนเดินทางไปใช้บริการ อยากทราบว่า ถือขวดน้ำเข้าไปได้หรือเปล่า ไม่ได้ถามเรื่องกิน

ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ

key `e57f02961055c3c0a53d1c221408cad728f8813afb52ce12e3b8da79576b2b37`; HTTP 200; 25.094 วินาที

```json
{
  "understanding_accepted": true,
  "tasks": [
    {
      "quote": "ก่อนเดินทางไปใช้บริการ อยากทราบว่า ถือขวดน้ำเข้าไปได้หรือเปล่า ไม่ได้ถามเรื่องกิน",
      "domain": "rules",
      "category": "C10",
      "operation": "detail",
      "facet": "owner_policy",
      "target": "",
      "constraints": [],
      "ambiguous": false
    }
  ],
  "source_quote_repairs": null,
  "independent_subtask_reviews": null,
  "meaning_review": null,
  "needs": [
    {
      "category": "C10",
      "status": "missing_source",
      "reason_codes": [
        "entity_not_bound"
      ],
      "execution_query": "ก่อนเดินทางไปใช้บริการ อยากทราบว่า ถือขวดน้ำเข้าไปได้หรือเปล่า ไม่ได้ถามเรื่องกิน "
    }
  ],
  "literal_grades": []
}
```

### What do you need to book to paly FINAL FANTASY XVI

FINAL FANTASY XVI — studio services offering this game: PlayStation 5 #01-#02 [S1]

key `0a00000d589ff1289bde21138edaae2f4071c278c44887ef046325cb4e101ea6`; HTTP 200; 16.422 วินาที

```json
{
  "understanding_accepted": true,
  "tasks": [
    {
      "quote": "what do you need to book to paly final fantasy xvi",
      "domain": "games",
      "category": "C04",
      "operation": "availability",
      "facet": "studio_services",
      "target": "",
      "constraints": [],
      "ambiguous": false
    }
  ],
  "source_quote_repairs": null,
  "independent_subtask_reviews": null,
  "meaning_review": {
    "basis": "source_bound_game_to_bookable_service_relation",
    "model_plan_accepted": true,
    "model_reason": "validated_interpretation_proposal",
    "prior_tasks": [
      {
        "quote": "what do you need to book to paly final fantasy xvi",
        "domain": "rental",
        "category": "C07",
        "operation": "detail",
        "facet": "equipment_included",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "business_facts_added": false
  },
  "needs": [
    {
      "category": "C04",
      "status": "supported",
      "reason_codes": [
        "meaning_bound_requested_field"
      ],
      "execution_query": "what do you need to book to paly final fantasy xvi "
    }
  ],
  "literal_grades": []
}
```

### How to book Cockpit and what days is it open?

1. how to book cockpit
How to book: The booking steps are: select a service, choose date and time, fill in user information, review the details, make payment by bank transfer, and upload the payment slip. [S1]

2. what days is it open
No confirmed source is available for the requested detail.

key `a603ab1aed328e10dbf5ac72b6a752be2fb77658ea0365896a1776cd04806370`; HTTP 200; 21.828 วินาที

```json
{
  "understanding_accepted": true,
  "tasks": [
    {
      "quote": "how to book cockpit",
      "domain": "reservation",
      "category": "C08",
      "operation": "detail",
      "facet": "owner_policy",
      "target": "",
      "constraints": [],
      "ambiguous": false
    },
    {
      "quote": "what days is it open",
      "domain": "schedule",
      "category": "C11",
      "operation": "detail",
      "facet": "bookable_periods",
      "target": "",
      "constraints": [],
      "ambiguous": false
    }
  ],
  "source_quote_repairs": null,
  "independent_subtask_reviews": null,
  "meaning_review": null,
  "needs": [
    {
      "category": "C08",
      "status": "supported",
      "reason_codes": [
        "declared_legacy_query_profile"
      ],
      "execution_query": "how to book cockpit "
    },
    {
      "category": "C11",
      "status": "missing_source",
      "reason_codes": [
        "entity_not_bound"
      ],
      "execution_query": "what days is it open "
    }
  ],
  "literal_grades": []
}
```

### Please use verified studio information: What ID does an external visitor need to use the studio?

Check-in document: When checking in to use the service, you must present your student ID card, staff ID card, or national identification card. [S1]
What documents must I present upon arrival?: At arrival, present a national ID card, university student card, school student card, or passport. [S2]

key `1cf7db3858a13e4841f441117b1a23c40c3e46cf26be6bc9d0b7bb64314f0993`; HTTP 200; 22.250 วินาที

```json
{
  "understanding_accepted": true,
  "tasks": [
    {
      "quote": "please use verified studio information: what id does an external visitor need to use the studio?",
      "domain": "reservation",
      "category": "C08",
      "operation": "detail",
      "facet": "owner_policy",
      "target": "",
      "constraints": [],
      "ambiguous": false
    }
  ],
  "source_quote_repairs": null,
  "independent_subtask_reviews": null,
  "meaning_review": {
    "basis": "identification_documents_requested_before_visitor_eligibility",
    "model_plan_accepted": false,
    "model_reason": "r121_vocabulary",
    "prior_tasks": [],
    "business_facts_added": false
  },
  "needs": [
    {
      "category": "C08",
      "status": "supported",
      "reason_codes": [
        "bounded_model_selection"
      ],
      "execution_query": "please use verified studio information: what id does an external visitor need to use the studio? "
    }
  ],
  "literal_grades": []
}
```

### ขอสอบถามหน่อยครับ Nintendo Switch OLED คืออะไร

Nintendo Switch OLED — การใช้งาน: เครื่องเกม Nintendo Switch รุ่น OLED สำหรับเล่นเกมคอนโซลแบบกลุ่มหรือครอบครัว
จอง Nintendo Switch Zone แล้วเล่นผ่าน TV 86 นิ้วและจอยที่ศูนย์จัดไว้ตามรอบบริการ
เล่น Mario Kart 8 Deluxe
เล่น Overcooked 2
เล่น Super Smash Bros Ultimate
เล่น Nintendo Switch Sports [S1]

key `42582c1e488fe656f9f5c3662337d47965e4f00cf22030c9d973e808b6a6b715`; HTTP 200; 15.203 วินาที

```json
{
  "understanding_accepted": true,
  "tasks": [
    {
      "quote": "nintendo switch oled คืออะไร",
      "domain": "equipment",
      "category": "C03",
      "operation": "detail",
      "facet": "usage",
      "target": "nintendo switch oled",
      "constraints": [],
      "ambiguous": false
    }
  ],
  "source_quote_repairs": [
    {
      "path": "tasks[0].target",
      "model_quote": "Nintendo Switch OLED",
      "source_quote": "nintendo switch oled",
      "basis": "unique_case_insensitive_source_span"
    }
  ],
  "independent_subtask_reviews": null,
  "meaning_review": null,
  "needs": [
    {
      "category": "C03",
      "status": "supported",
      "reason_codes": [
        "meaning_bound_requested_field"
      ],
      "execution_query": "nintendo switch oled คืออะไร "
    }
  ],
  "literal_grades": [
    {
      "id": "MASTER-GT-TH-03525",
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "id": "MASTER-GT-TH-03525",
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "id": "MASTER-GT-TH-03525",
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "id": "MASTER-GT-TH-03525",
      "literal_passed": true,
      "literal_errors": []
    }
  ]
}
```

### PSU Staff เล่น PS5 2 ชั่วโมง เสียกี่บาท

อัตราที่เจ้าของยืนยันล่าสุด ณ 2026-10-20 (ยังไม่ยืนยันวันเริ่ม–สิ้นสุดใหม่)
PlayStation 5 #01-#02 / PSU Student and Staff — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 0 บาท สำหรับ 120 นาที [S1]

key `c7ef53bc74bbcf79c04acf7ca763a1907f7b2b0d48e7e7301b920e7236044502`; HTTP 200; 38.797 วินาที

```json
{
  "understanding_accepted": true,
  "tasks": [
    {
      "quote": "psu staff เล่น ps5 2 ชั่วโมง เสียกี่บาท",
      "domain": "service_fee",
      "category": "C06",
      "operation": "price_calculate",
      "facet": "amount",
      "target": "ps5",
      "constraints": [
        {
          "slot": "duration",
          "quote": "2 ชั่วโมง",
          "source_record_id": ""
        },
        {
          "slot": "platform",
          "quote": "ps5",
          "source_record_id": ""
        },
        {
          "slot": "audience",
          "quote": "psu staff",
          "source_record_id": ""
        }
      ],
      "ambiguous": false
    }
  ],
  "source_quote_repairs": null,
  "independent_subtask_reviews": null,
  "meaning_review": null,
  "needs": [
    {
      "category": "C06",
      "status": "supported",
      "reason_codes": [
        "typed_requested_fields"
      ],
      "execution_query": "psu staff เล่น ps5 2 ชั่วโมง เสียกี่บาท "
    }
  ],
  "literal_grades": [
    {
      "id": "MASTER-GT-TH-00144",
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "id": "MASTER-GT-TH-00144",
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "id": "MASTER-GT-TH-00144",
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "id": "MASTER-GT-TH-00144",
      "literal_passed": true,
      "literal_errors": []
    }
  ]
}
```

### วันศุกร์ช่วงบ่ายปิดใช่ไหม ขอรายละเอียดแบบสั้น ๆ

ศุกร์ — ตารางให้บริการเล่น: ไม่เปิดให้บริการเล่นช่วง 13:00–16:00 เนื่องจากบำรุงรักษาตามตาราง [S1]

key `8711c0d5094ea26fea23b4403fd1e102da385cb8b4a5097c0f623eb9ae9bc4be`; HTTP 200; 27.343 วินาที

```json
{
  "understanding_accepted": true,
  "tasks": [
    {
      "quote": "วันศุกร์ช่วงบ่ายปิดใช่ไหม ขอรายละเอียดแบบสั้น ๆ",
      "domain": "schedule",
      "category": "C11",
      "operation": "detail",
      "facet": "open_periods",
      "target": "",
      "constraints": [
        {
          "slot": "date",
          "quote": "วันศุกร์",
          "source_record_id": ""
        }
      ],
      "ambiguous": false
    }
  ],
  "source_quote_repairs": null,
  "independent_subtask_reviews": null,
  "meaning_review": null,
  "needs": [
    {
      "category": "C11",
      "status": "supported",
      "reason_codes": [
        "recorded_play_service_calendar"
      ],
      "execution_query": "วันศุกร์ช่วงบ่ายปิดใช่ไหม ขอรายละเอียดแบบสั้น ๆ "
    }
  ],
  "literal_grades": [
    {
      "id": "MASTER-GT-TH-01575",
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "id": "MASTER-GT-TH-01575",
      "literal_passed": true,
      "literal_errors": []
    }
  ]
}
```

### How do you use the controller in Little Nightmares II

Little Nightmares II / PlayStation / PS5 — Camera: R (Right Stick) — Pan the camera to view surroundings and control flashlight direction [S1]
Little Nightmares II / PlayStation / PS5 — Move: L (Left Stick) — Move and navigate the character [S2]
Little Nightmares II / PlayStation / PS5 — Flashlight / Remote: Circle — Use to toggle flashlight and press TV remote button [S3]
Little Nightmares II / PlayStation / PS5 — Jump / Throw / Attack: Cross — Use for jumping, throwing items, or swinging weapons to attack [S4]
Little Nightmares II / PlayStation / PS5 — Grab: R1 / R2 — Hold to pick up items, climb stairs, drag objects, or grab Six's hand [S5]
Little Nightmares II / PlayStation / PS5 — Sprint: Square — Press to sprint, increasing movement speed or fleeing speed [S6]

key `5d18afc2c4f40b5b3189925a763a53ed8a208d8d79d1e083b73e62785b1ac4f2`; HTTP 200; 24.563 วินาที

```json
{
  "understanding_accepted": true,
  "tasks": [
    {
      "quote": "how do you use the controller in little nightmares ii",
      "domain": "game_controls",
      "category": "C05",
      "operation": "control",
      "facet": "input_bindings",
      "target": "little nightmares ii",
      "constraints": [],
      "ambiguous": false
    }
  ],
  "source_quote_repairs": [
    {
      "path": "tasks[0].target",
      "model_quote": "Little Nightmares II",
      "source_quote": "little nightmares ii",
      "basis": "unique_case_insensitive_source_span"
    }
  ],
  "independent_subtask_reviews": null,
  "meaning_review": null,
  "needs": [
    {
      "category": "C05",
      "status": "supported",
      "reason_codes": [
        "bounded_model_selection"
      ],
      "execution_query": "how do you use the controller in little nightmares ii "
    }
  ],
  "literal_grades": []
}
```

### กำลังวางแผนไปใช้บริการ เลยอยากทราบว่า ต้องการจองเครื่องทำยังไง อะ

ขั้นตอนการจอง: ขั้นตอนการจองคือ เลือกบริการที่ต้องการ เลือกวันและเวลา กรอกข้อมูลผู้ใช้บริการ ตรวจสอบข้อมูล ชำระเงินโดยโอนเข้าบัญชีธนาคาร และแนบสลิปการโอนเงิน [S1]
วิธีจอง: ขั้นตอนจองคือ เลือกบริการ เลือกวันและเวลา กรอกข้อมูลผู้ใช้ ตรวจสอบข้อมูล ชำระเงินโดยโอนเข้าบัญชี และแนบสลิปการโอนเงิน [S2]
ขั้นตอนจองคือ เลือกบริการ เลือกวันและเวลา กรอกข้อมูลผู้ใช้ ตรวจสอบข้อมูล ชำระเงินโดยโอนเข้าบัญชี และแนบสลิปการโอนเงิน [S3]

key `36c239903ef9b2645e840586a9db999016c64405aefcfc4914ba3d20f2ecdcdf`; HTTP 200; 28.047 วินาที

```json
{
  "understanding_accepted": true,
  "tasks": [
    {
      "quote": "กำลังวางแผนไปใช้บริการ เลยอยากทราบว่า ต้องการจองเครื่องทำยังไง อะ",
      "domain": "reservation",
      "category": "C08",
      "operation": "detail",
      "facet": "owner_policy",
      "target": "",
      "constraints": [],
      "ambiguous": false
    }
  ],
  "source_quote_repairs": null,
  "independent_subtask_reviews": null,
  "meaning_review": null,
  "needs": [
    {
      "category": "C08",
      "status": "supported",
      "reason_codes": [
        "bounded_model_selection"
      ],
      "execution_query": "กำลังวางแผนไปใช้บริการ เลยอยากทราบว่า ต้องการจองเครื่องทำยังไง อะ "
    }
  ],
  "literal_grades": []
}
```

### ขอถามเกี่ยวกับศูนย์หน่อยครับ: อาหารต้องกินในบริเวณที่จัดไว้เท่านั้นหรือเปล่า

ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ

key `dcddcfd2f0b17833219d703b3e88d5a3f4c4dfaf9bde596cd0d3ef89e412600d`; HTTP 200; 24.453 วินาที

```json
{
  "understanding_accepted": true,
  "tasks": [
    {
      "quote": "ขอถามเกี่ยวกับศูนย์หน่อยครับ: อาหารต้องกินในบริเวณที่จัดไว้เท่านั้นหรือเปล่า",
      "domain": "rules",
      "category": "C10",
      "operation": "detail",
      "facet": "owner_policy",
      "target": "",
      "constraints": [],
      "ambiguous": false
    }
  ],
  "source_quote_repairs": null,
  "independent_subtask_reviews": null,
  "meaning_review": null,
  "needs": [
    {
      "category": "C10",
      "status": "missing_source",
      "reason_codes": [
        "entity_not_bound"
      ],
      "execution_query": "ขอถามเกี่ยวกับศูนย์หน่อยครับ: อาหารต้องกินในบริเวณที่จัดไว้เท่านั้นหรือเปล่า "
    }
  ],
  "literal_grades": [
    {
      "id": "INTENT-TRAP-TH-0297",
      "literal_passed": false,
      "literal_errors": [
        "missing all alternatives: ['พื้นที่ที่กำหนด', 'designated area']"
      ]
    },
    {
      "id": "INTENT-TRAP-TH-0297",
      "literal_passed": false,
      "literal_errors": [
        "missing all alternatives: ['พื้นที่ที่กำหนด', 'designated area']"
      ]
    }
  ]
}
```

## priority01

```json
{
  "requests": 4,
  "http_200": 4,
  "positive_literal_pass": 4,
  "positive_literal_grades": 4,
  "positive_literal_requests": 1,
  "latency_median_sec": 23.7035,
  "new_questions": 0,
  "fresh_heldout": false,
  "frozen_source_unchanged": true
}
```

### What are the 8 buttons in Tekken 8, ans what is the PC price

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

key `d91ee50a1f6c21f141226b55bb86aaea2935e3a4b5e73b339ff4d83b81a1deaa`; HTTP 200; 49.719 วินาที

```json
{
  "understanding_accepted": true,
  "tasks": [
    {
      "quote": "what are the 8 buttons in tekken 8",
      "domain": "game_controls",
      "category": "C05",
      "operation": "list",
      "facet": "input_bindings",
      "target": "tekken 8",
      "constraints": [],
      "ambiguous": false
    },
    {
      "quote": "what is the pc price",
      "domain": "service_fee",
      "category": "C06",
      "operation": "price_calculate",
      "facet": "amount",
      "target": "",
      "constraints": [],
      "ambiguous": false
    }
  ],
  "source_quote_repairs": null,
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
  "meaning_review": null,
  "needs": [
    {
      "category": "C05",
      "status": "supported",
      "reason_codes": [
        "complete_source_binding_set"
      ],
      "execution_query": "what are the 8 buttons in tekken 8 "
    },
    {
      "category": "C06",
      "status": "supported",
      "reason_codes": [
        "typed_requested_fields"
      ],
      "execution_query": "what is the pc price TEKKEN 8"
    }
  ],
  "literal_grades": []
}
```

### Please use verified studio information: What ID does an external visitor need to use the studio?

Check-in document: When checking in to use the service, you must present your student ID card, staff ID card, or national identification card. [S1]
What documents must I present upon arrival?: At arrival, present a national ID card, university student card, school student card, or passport. [S2]

key `1cf7db3858a13e4841f441117b1a23c40c3e46cf26be6bc9d0b7bb64314f0993`; HTTP 200; 22.375 วินาที

```json
{
  "understanding_accepted": true,
  "tasks": [
    {
      "quote": "please use verified studio information: what id does an external visitor need to use the studio?",
      "domain": "reservation",
      "category": "C08",
      "operation": "detail",
      "facet": "owner_policy",
      "target": "",
      "constraints": [],
      "ambiguous": false
    }
  ],
  "source_quote_repairs": null,
  "independent_subtask_reviews": null,
  "meaning_review": {
    "basis": "identification_documents_requested_before_visitor_eligibility",
    "model_plan_accepted": false,
    "model_reason": "r121_vocabulary",
    "prior_tasks": [],
    "business_facts_added": false
  },
  "needs": [
    {
      "category": "C08",
      "status": "supported",
      "reason_codes": [
        "bounded_model_selection"
      ],
      "execution_query": "please use verified studio information: what id does an external visitor need to use the studio? "
    }
  ],
  "literal_grades": []
}
```

### ขอสอบถามหน่อยครับ Nintendo Switch OLED คืออะไร

Nintendo Switch OLED — การใช้งาน: เครื่องเกม Nintendo Switch รุ่น OLED สำหรับเล่นเกมคอนโซลแบบกลุ่มหรือครอบครัว
จอง Nintendo Switch Zone แล้วเล่นผ่าน TV 86 นิ้วและจอยที่ศูนย์จัดไว้ตามรอบบริการ
เล่น Mario Kart 8 Deluxe
เล่น Overcooked 2
เล่น Super Smash Bros Ultimate
เล่น Nintendo Switch Sports [S1]

key `42582c1e488fe656f9f5c3662337d47965e4f00cf22030c9d973e808b6a6b715`; HTTP 200; 15.250 วินาที

```json
{
  "understanding_accepted": true,
  "tasks": [
    {
      "quote": "nintendo switch oled คืออะไร",
      "domain": "equipment",
      "category": "C03",
      "operation": "detail",
      "facet": "usage",
      "target": "nintendo switch oled",
      "constraints": [],
      "ambiguous": false
    }
  ],
  "source_quote_repairs": [
    {
      "path": "tasks[0].target",
      "model_quote": "Nintendo Switch OLED",
      "source_quote": "nintendo switch oled",
      "basis": "unique_case_insensitive_source_span"
    }
  ],
  "independent_subtask_reviews": null,
  "meaning_review": null,
  "needs": [
    {
      "category": "C03",
      "status": "supported",
      "reason_codes": [
        "meaning_bound_requested_field"
      ],
      "execution_query": "nintendo switch oled คืออะไร "
    }
  ],
  "literal_grades": [
    {
      "id": "MASTER-GT-TH-03525",
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "id": "MASTER-GT-TH-03525",
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "id": "MASTER-GT-TH-03525",
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "id": "MASTER-GT-TH-03525",
      "literal_passed": true,
      "literal_errors": []
    }
  ]
}
```

### How do you use the controller in Little Nightmares II

Little Nightmares II / PlayStation / PS5 — Camera: R (Right Stick) — Pan the camera to view surroundings and control flashlight direction [S1]
Little Nightmares II / PlayStation / PS5 — Move: L (Left Stick) — Move and navigate the character [S2]
Little Nightmares II / PlayStation / PS5 — Flashlight / Remote: Circle — Use to toggle flashlight and press TV remote button [S3]
Little Nightmares II / PlayStation / PS5 — Jump / Throw / Attack: Cross — Use for jumping, throwing items, or swinging weapons to attack [S4]
Little Nightmares II / PlayStation / PS5 — Grab: R1 / R2 — Hold to pick up items, climb stairs, drag objects, or grab Six's hand [S5]
Little Nightmares II / PlayStation / PS5 — Sprint: Square — Press to sprint, increasing movement speed or fleeing speed [S6]

key `5d18afc2c4f40b5b3189925a763a53ed8a208d8d79d1e083b73e62785b1ac4f2`; HTTP 200; 25.032 วินาที

```json
{
  "understanding_accepted": true,
  "tasks": [
    {
      "quote": "how do you use the controller in little nightmares ii",
      "domain": "game_controls",
      "category": "C05",
      "operation": "control",
      "facet": "input_bindings",
      "target": "little nightmares ii",
      "constraints": [],
      "ambiguous": false
    }
  ],
  "source_quote_repairs": [
    {
      "path": "tasks[0].target",
      "model_quote": "Little Nightmares II",
      "source_quote": "little nightmares ii",
      "basis": "unique_case_insensitive_source_span"
    }
  ],
  "independent_subtask_reviews": null,
  "meaning_review": null,
  "needs": [
    {
      "category": "C05",
      "status": "supported",
      "reason_codes": [
        "bounded_model_selection"
      ],
      "execution_query": "how do you use the controller in little nightmares ii "
    }
  ],
  "literal_grades": []
}
```

## reader01

```json
{
  "requests": 3,
  "http_200": 3,
  "positive_literal_pass": 2,
  "positive_literal_grades": 2,
  "positive_literal_requests": 1,
  "latency_median_sec": 26.359,
  "new_questions": 0,
  "fresh_heldout": false,
  "frozen_source_unchanged": true
}
```

### What are the 8 buttons in Tekken 8, ans what is the PC price

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

key `d91ee50a1f6c21f141226b55bb86aaea2935e3a4b5e73b339ff4d83b81a1deaa`; HTTP 200; 50.344 วินาที

```json
{
  "understanding_accepted": true,
  "tasks": [
    {
      "quote": "what are the 8 buttons in tekken 8",
      "domain": "game_controls",
      "category": "C05",
      "operation": "list",
      "facet": "input_bindings",
      "target": "tekken 8",
      "constraints": [],
      "ambiguous": false
    },
    {
      "quote": "what is the pc price",
      "domain": "service_fee",
      "category": "C06",
      "operation": "price_calculate",
      "facet": "amount",
      "target": "",
      "constraints": [],
      "ambiguous": false
    }
  ],
  "source_quote_repairs": null,
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
  "meaning_review": null,
  "needs": [
    {
      "category": "C05",
      "status": "partial_supported",
      "reason_codes": [
        "requested_control_subset_not_identified"
      ],
      "execution_query": "what are the 8 buttons in tekken 8 "
    },
    {
      "category": "C06",
      "status": "supported",
      "reason_codes": [
        "typed_requested_fields"
      ],
      "execution_query": "what is the pc price TEKKEN 8"
    }
  ],
  "literal_grades": []
}
```

### ขอถามเกี่ยวกับศูนย์หน่อยครับ: อาหารต้องกินในบริเวณที่จัดไว้เท่านั้นหรือเปล่า

อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น [S1]

key `dcddcfd2f0b17833219d703b3e88d5a3f4c4dfaf9bde596cd0d3ef89e412600d`; HTTP 200; 26.359 วินาที

```json
{
  "understanding_accepted": true,
  "tasks": [
    {
      "quote": "ขอถามเกี่ยวกับศูนย์หน่อยครับ: อาหารต้องกินในบริเวณที่จัดไว้เท่านั้นหรือเปล่า",
      "domain": "rules",
      "category": "C10",
      "operation": "detail",
      "facet": "owner_policy",
      "target": "",
      "constraints": [],
      "ambiguous": false
    }
  ],
  "source_quote_repairs": null,
  "independent_subtask_reviews": null,
  "meaning_review": null,
  "needs": [
    {
      "category": "C10",
      "status": "supported",
      "reason_codes": [
        "equivalent_literal_policy_sources"
      ],
      "execution_query": "ขอถามเกี่ยวกับศูนย์หน่อยครับ: อาหารต้องกินในบริเวณที่จัดไว้เท่านั้นหรือเปล่า "
    }
  ],
  "literal_grades": [
    {
      "id": "INTENT-TRAP-TH-0297",
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "id": "INTENT-TRAP-TH-0297",
      "literal_passed": true,
      "literal_errors": []
    }
  ]
}
```

### ก่อนเดินทางไปใช้บริการ อยากทราบว่า ถือขวดน้ำเข้าไปได้หรือเปล่า ไม่ได้ถามเรื่องกิน

ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ

key `e57f02961055c3c0a53d1c221408cad728f8813afb52ce12e3b8da79576b2b37`; HTTP 200; 25.562 วินาที

```json
{
  "understanding_accepted": true,
  "tasks": [
    {
      "quote": "ก่อนเดินทางไปใช้บริการ อยากทราบว่า ถือขวดน้ำเข้าไปได้หรือเปล่า ไม่ได้ถามเรื่องกิน",
      "domain": "rules",
      "category": "C10",
      "operation": "detail",
      "facet": "owner_policy",
      "target": "",
      "constraints": [],
      "ambiguous": false
    }
  ],
  "source_quote_repairs": null,
  "independent_subtask_reviews": null,
  "meaning_review": null,
  "needs": [
    {
      "category": "C10",
      "status": "missing_source",
      "reason_codes": [
        "entity_not_bound"
      ],
      "execution_query": "ก่อนเดินทางไปใช้บริการ อยากทราบว่า ถือขวดน้ำเข้าไปได้หรือเปล่า ไม่ได้ถามเรื่องกิน "
    }
  ],
  "literal_grades": []
}
```
