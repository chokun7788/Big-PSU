# R118 — Casebook ก่อน–หลังทุก 48 keys

คำตอบ R115/R117/R118 จาก saved logs; ไม่เรียก baseline ใหม่ คะแนน literal ไม่ทดแทนการอ่าน source/สถานะ partial

## 1. ขอสอบถามหน่อยยครับ บุคคลทั่วไป เล่น PS5 2 ชั่วโมง เสียกี่บาท

Key: `044f667114ab611667f0d97496b6ba029d49dfd88337fc90123cd7a189623458`; locale `th`; original domain `service_fee`

### R115 saved

```text
กรุณาระบุรายการและช่วงเวลาที่ต้องการตรวจสอบเพิ่มเติมครับ
```

### R117 revision03 saved

```text
อัตราที่เจ้าของยืนยันล่าสุด ณ 2026-10-20 (ยังไม่ยืนยันวันเริ่ม–สิ้นสุดใหม่)
ทราบระยะเวลาที่ต้องการแล้ว แต่ยังไม่มีกฎคำนวณที่ยืนยันสำหรับระยะเวลานี้ อัตราด้านล่างเป็นราคาต่อหน่วยที่บันทึกไว้ ไม่ใช่ยอดรวมของคำขอนี้
PlayStation 5 #01-#02 / PSU Student and Staff — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 0 บาทต่อคน สำหรับ 60 นาที [S1]
PlayStation 5 #01-#02 / PSU Alumni and General Student — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 50 บาทต่อคน สำหรับ 60 นาที [S2]
PlayStation 5 #01-#02 / General Adult — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 150 บาทต่อคน สำหรับ 60 นาที [S3]
```

### R118 revision02

```text
อัตราที่เจ้าของยืนยันล่าสุด ณ 2026-10-20 (ยังไม่ยืนยันวันเริ่ม–สิ้นสุดใหม่)
ทราบระยะเวลาที่ต้องการแล้ว แต่ยังไม่มีกฎคำนวณที่ยืนยันสำหรับระยะเวลานี้ อัตราด้านล่างเป็นราคาต่อหน่วยที่บันทึกไว้ ไม่ใช่ยอดรวมของคำขอนี้
PlayStation 5 #01-#02 / PSU Student and Staff — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 0 บาทต่อคน สำหรับ 60 นาที [S1]
PlayStation 5 #01-#02 / PSU Alumni and General Student — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 50 บาทต่อคน สำหรับ 60 นาที [S2]
PlayStation 5 #01-#02 / General Adult — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 150 บาทต่อคน สำหรับ 60 นาที [S3]
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": false,
    "reason": "meaning_transport_or_protocol_failure",
    "tasks": [],
    "event": {
      "id": "15082aa6aadb418c9b89a5ba19f006fa",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": false,
      "schema_ok": false,
      "error": "TimeoutError: timed out",
      "reason": "meaning_transport_or_protocol_failure",
      "elapsed_sec": 3.547,
      "http_attempted": true,
      "input_question": "ยครับ บุคคลทั่วไป เล่น ps5 2 ชั่วโมง เสียกี่บาท",
      "legacy_contrast": {
        "domain": "service_fee",
        "operation": "price_calculate",
        "needs": [
          "calculate_price",
          "show_price_breakdown"
        ],
        "reason": "domain_terms=2; price operation overrides entity/game domain; price terms found"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false
  },
  "need_results": [
    {
      "need_id": "r114_n1",
      "task": "price",
      "category": "C06",
      "source_span": "ยครับ บุคคลทั่วไป เล่น ps5 2 ชั่วโมง เสียกี่บาท",
      "execution_query": "ยครับ บุคคลทั่วไป เล่น ps5 2 ชั่วโมง เสียกี่บาท",
      "status": "partial_supported",
      "reason_codes": [
        "duration_arithmetic_not_declared"
      ],
      "receipts": [
        {
          "record_id": "migrated_rate_playstation_5_60_1_2_psu_student_staff",
          "field": "amount_minor",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/amount_minor",
              "source_id": "r63_db0d7d309783280c60aff0c31a72"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_db0d7d309783280c60aff0c31a72"
            },
            {
              "locator": "/mapped_fields/audience_id",
              "source_id": "r63_db0d7d309783280c60aff0c31a72"
            },
            {
              "locator": "/mapped_fields/duration_minutes",
              "source_id": "r63_db0d7d309783280c60aff0c31a72"
            },
            {
              "locator": "/fields/answer",
              "source_id": "r114_affirm_rate_0d5e3ccb4a50d3a637cb2118"
            },
            {
              "locator": "/fields/scope_note",
              "source_id": "r114_affirm_rate_0d5e3ccb4a50d3a637cb2118"
            }
          ]
        },
        {
          "record_id": "migrated_rate_playstation_5_60_1_2_psu_alumni_general_student",
          "field": "amount_minor",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/amount_minor",
              "source_id": "r63_35a6cefed055bfc60db380f2e0df"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_35a6cefed055bfc60db380f2e0df"
            },
            {
              "locator": "/mapped_fields/audience_id",
              "source_id": "r63_35a6cefed055bfc60db380f2e0df"
            },
            {
              "locator": "/mapped_fields/duration_minutes",
              "source_id": "r63_35a6cefed055bfc60db380f2e0df"
            },
            {
              "locator": "/fields/answer",
              "source_id": "r114_affirm_rate_0d5e3ccb4a50d3a637cb2118"
            },
            {
              "locator": "/fields/scope_note",
              "source_id": "r114_affirm_rate_0d5e3ccb4a50d3a637cb2118"
            }
          ]
        },
        {
          "record_id": "migrated_rate_playstation_5_60_1_2_general_adult",
          "field": "amount_minor",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/amount_minor",
              "source_id": "r63_3ef986791e0dd5833920ff6840db"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_3ef986791e0dd5833920ff6840db"
            },
            {
              "locator": "/mapped_fields/audience_id",
              "source_id": "r63_3ef986791e0dd5833920ff6840db"
            },
            {
              "locator": "/mapped_fields/duration_minutes",
              "source_id": "r63_3ef986791e0dd5833920ff6840db"
            },
            {
              "locator": "/fields/answer",
              "source_id": "r114_affirm_rate_0d5e3ccb4a50d3a637cb2118"
            },
            {
              "locator": "/fields/scope_note",
              "source_id": "r114_affirm_rate_0d5e3ccb4a50d3a637cb2118"
            }
          ]
        }
      ],
      "claim_packets": [
        {
          "fact_id": "C06:migrated_rate_playstation_5_60_1_2_psu_student_staff:amount",
          "record_id": "migrated_rate_playstation_5_60_1_2_psu_student_staff",
          "facet": "amount",
          "value": "0 บาทต่อคน สำหรับ 60 นาที",
          "numeric": 0.0,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/amount_minor",
              "source_id": "r63_db0d7d309783280c60aff0c31a72"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_db0d7d309783280c60aff0c31a72"
            },
            {
              "locator": "/mapped_fields/audience_id",
              "source_id": "r63_db0d7d309783280c60aff0c31a72"
            },
            {
              "locator": "/mapped_fields/duration_minutes",
              "source_id": "r63_db0d7d309783280c60aff0c31a72"
            },
            {
              "locator": "/fields/answer",
              "source_id": "r114_affirm_rate_0d5e3ccb4a50d3a637cb2118"
            },
            {
              "locator": "/fields/scope_note",
              "source_id": "r114_affirm_rate_0d5e3ccb4a50d3a637cb2118"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C06:migrated_rate_playstation_5_60_1_2_psu_alumni_general_student:amount",
          "record_id": "migrated_rate_playstation_5_60_1_2_psu_alumni_general_student",
          "facet": "amount",
          "value": "50 บาทต่อคน สำหรับ 60 นาที",
          "numeric": 50.0,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/amount_minor",
              "source_id": "r63_35a6cefed055bfc60db380f2e0df"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_35a6cefed055bfc60db380f2e0df"
            },
            {
              "locator": "/mapped_fields/audience_id",
              "source_id": "r63_35a6cefed055bfc60db380f2e0df"
            },
            {
              "locator": "/mapped_fields/duration_minutes",
              "source_id": "r63_35a6cefed055bfc60db380f2e0df"
            },
            {
              "locator": "/fields/answer",
              "source_id": "r114_affirm_rate_0d5e3ccb4a50d3a637cb2118"
            },
            {
              "locator": "/fields/scope_note",
              "source_id": "r114_affirm_rate_0d5e3ccb4a50d3a637cb2118"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C06:migrated_rate_playstation_5_60_1_2_general_adult:amount",
          "record_id": "migrated_rate_playstation_5_60_1_2_general_adult",
          "facet": "amount",
          "value": "150 บาทต่อคน สำหรับ 60 นาที",
          "numeric": 150.0,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/amount_minor",
              "source_id": "r63_3ef986791e0dd5833920ff6840db"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_3ef986791e0dd5833920ff6840db"
            },
            {
              "locator": "/mapped_fields/audience_id",
              "source_id": "r63_3ef986791e0dd5833920ff6840db"
            },
            {
              "locator": "/mapped_fields/duration_minutes",
              "source_id": "r63_3ef986791e0dd5833920ff6840db"
            },
            {
              "locator": "/fields/answer",
              "source_id": "r114_affirm_rate_0d5e3ccb4a50d3a637cb2118"
            },
            {
              "locator": "/fields/scope_note",
              "source_id": "r114_affirm_rate_0d5e3ccb4a50d3a637cb2118"
            }
          ],
          "fixture": false,
          "status": "answer"
        }
      ],
      "semantic_correctness_verified": false
    }
  ],
  "sources": [],
  "positive_contracts": [
    {
      "file": "data/eval/master_gt_bilingual_multi_error_2000_20260929_r15.jsonl",
      "row": 585,
      "variant": "noisy",
      "id": "MASTER-GT-TH-00325",
      "passed": false,
      "failures": [
        "route:knowledge expected:['service_fee']",
        "latency_ceiling"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['service_fee']"
        ],
        "performance": [
          "latency_ceiling"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    }
  ]
}
```

## 2. เกมไหนเล่นได้หลายโซน

Key: `1806def707336a05166ef9b2589b66cb0450c840866d7ea5f6b920dccd0823f8`; locale `th`; original domain `games_catalog_availability`

### R115 saved

```text
ข้อมูลที่เลือกยังไม่ยืนยันส่วนที่ถามโดยตรงครับ
```

### R117 revision03 saved

```text
รายการที่ยืนยันได้จากความสัมพันธ์ที่มีอยู่ ยังไม่รับรองว่าครบทุกเกมหรือทุกโซน
TEKKEN 8 — โซนที่ยืนยันว่ามีเกมนี้: PC Zone; PlayStation 5 Zone [S1]
```

### R118 revision02

```text
รายการที่ยืนยันได้จากความสัมพันธ์ที่มีอยู่ ยังไม่รับรองว่าครบทุกเกมหรือทุกโซน
TEKKEN 8 — โซนที่ยืนยันว่ามีเกมนี้: PC Zone; PlayStation 5 Zone [S1]
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "validated_interpretation_proposal",
    "tasks": [
      {
        "quote": "เกมไหนเล่นได้หลายโซน",
        "domain": "games",
        "category": "C04",
        "operation": "list",
        "facet": "zone",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "9bd426877f084582ba68f480eaeeff51",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"เกมไหนเล่นได้หลายโซน\", \"operation\": \"list\", \"domain\": \"games\", \"facet\": \"zone\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 6.125,
      "http_attempted": true,
      "input_question": "เกมไหนเล่นได้หลายโซน",
      "legacy_contrast": {
        "domain": "general",
        "operation": "unknown",
        "needs": [],
        "reason": "domain_terms=2; no clear operation terms"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false
  },
  "need_results": [
    {
      "need_id": "r114_n1",
      "task": "game_detail",
      "category": "C04",
      "source_span": "เกมไหนเล่นได้หลายโซน",
      "execution_query": "เกมไหนเล่นได้หลายโซน ",
      "status": "partial_supported",
      "reason_codes": [
        "confirmed_multi_zone_subset"
      ],
      "receipts": [
        {
          "record_id": "game_detail_tekken_8",
          "field": "zone",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/game_id",
              "source_id": "r63_e7052c75b2767841a51e6dade36a"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_e7052c75b2767841a51e6dade36a"
            },
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_e7052c75b2767841a51e6dade36a"
            },
            {
              "locator": "/mapped_fields/resource_ids",
              "source_id": "r63_65331c20f193ef240c5184e70cf0"
            },
            {
              "locator": "/mapped_fields/zone_id",
              "source_id": "r63_d1a075421a7e30716a11bfad2109"
            },
            {
              "locator": "/mapped_fields/zone_id",
              "source_id": "r63_987b530c2d4da75eb8bca3902798"
            },
            {
              "locator": "/mapped_fields/game_id",
              "source_id": "r63_8328bacbdcca393bd9b93aa9217d"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_8328bacbdcca393bd9b93aa9217d"
            },
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_8328bacbdcca393bd9b93aa9217d"
            },
            {
              "locator": "/mapped_fields/resource_ids",
              "source_id": "r63_5c4c2946432a8b89ef45c675486d"
            },
            {
              "locator": "/mapped_fields/zone_id",
              "source_id": "r63_df5d776c41b16941439e1a363b2e"
            },
            {
              "locator": "/mapped_fields/zone_id",
              "source_id": "r63_0c8c4707f75172e12d434b37297e"
            }
          ]
        }
      ],
      "claim_packets": [
        {
          "fact_id": "C04:game_detail_tekken_8:zone",
          "record_id": "game_detail_tekken_8",
          "facet": "zone",
          "value": "PC Zone; PlayStation 5 Zone",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/game_id",
              "source_id": "r63_e7052c75b2767841a51e6dade36a"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_e7052c75b2767841a51e6dade36a"
            },
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_e7052c75b2767841a51e6dade36a"
            },
            {
              "locator": "/mapped_fields/resource_ids",
              "source_id": "r63_65331c20f193ef240c5184e70cf0"
            },
            {
              "locator": "/mapped_fields/zone_id",
              "source_id": "r63_d1a075421a7e30716a11bfad2109"
            },
            {
              "locator": "/mapped_fields/zone_id",
              "source_id": "r63_987b530c2d4da75eb8bca3902798"
            },
            {
              "locator": "/mapped_fields/game_id",
              "source_id": "r63_8328bacbdcca393bd9b93aa9217d"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_8328bacbdcca393bd9b93aa9217d"
            },
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_8328bacbdcca393bd9b93aa9217d"
            },
            {
              "locator": "/mapped_fields/resource_ids",
              "source_id": "r63_5c4c2946432a8b89ef45c675486d"
            },
            {
              "locator": "/mapped_fields/zone_id",
              "source_id": "r63_df5d776c41b16941439e1a363b2e"
            },
            {
              "locator": "/mapped_fields/zone_id",
              "source_id": "r63_0c8c4707f75172e12d434b37297e"
            }
          ],
          "fixture": false,
          "status": "answer"
        }
      ],
      "semantic_correctness_verified": false
    }
  ],
  "sources": [],
  "positive_contracts": [
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
      "row": 1740,
      "variant": "question",
      "id": "MASTER-GT-TH-01741",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
      "row": 1740,
      "variant": "question",
      "id": "MASTER-GT-TH-01741",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_th_5000_v1.jsonl",
      "row": 1740,
      "variant": "question",
      "id": "MASTER-GT-TH-01741",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_th_5000_v2.jsonl",
      "row": 1740,
      "variant": "question",
      "id": "MASTER-GT-TH-01741",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    }
  ]
}
```

## 3. Please answer from verified studio information: Which studio zone has TEKKEN 8

Key: `8570a28b567efb150998f4e15cebed739de8dcc6c72b66747d9f66b10022607a`; locale `en`; original domain `game_detail`

### R115 saved

```text
TEKKEN 8 — studio services offering this game: PC #01-#02; PlayStation 5 #01-#02 [S1]
```

### R117 revision03 saved

```text
TEKKEN 8 — confirmed studio zones offering this game: PC Zone; PlayStation 5 Zone [S1]
```

### R118 revision02

```text
TEKKEN 8 — confirmed studio zones offering this game: PC Zone; PlayStation 5 Zone [S1]
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "validated_interpretation_proposal",
    "tasks": [
      {
        "quote": "which studio zone has tekken 8",
        "domain": "games",
        "category": "C04",
        "operation": "detail",
        "facet": "zone",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "fa727fe6a07e4ee79b05ae8eadac033d",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"which studio zone has tekken 8\", \"operation\": \"detail\", \"domain\": \"games\", \"facet\": \"zone\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 1.39,
      "http_attempted": true,
      "input_question": "which studio zone has tekken 8",
      "legacy_contrast": {
        "domain": "games",
        "operation": "detail",
        "needs": [
          "summarize_detail",
          "check_availability"
        ],
        "reason": "known game alias found; known game title keeps games domain; no clear operation terms; bare known game title treated as detail"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false
  },
  "need_results": [
    {
      "need_id": "r114_n1",
      "task": "game_detail",
      "category": "C04",
      "source_span": "which studio zone has tekken 8",
      "execution_query": "which studio zone has tekken 8 ",
      "status": "supported",
      "reason_codes": [
        "typed_game_zone_projection"
      ],
      "receipts": [
        {
          "record_id": "game_detail_tekken_8",
          "field": "zone",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/game_id",
              "source_id": "r63_e7052c75b2767841a51e6dade36a"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_e7052c75b2767841a51e6dade36a"
            },
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_e7052c75b2767841a51e6dade36a"
            },
            {
              "locator": "/mapped_fields/resource_ids",
              "source_id": "r63_65331c20f193ef240c5184e70cf0"
            },
            {
              "locator": "/mapped_fields/zone_id",
              "source_id": "r63_d1a075421a7e30716a11bfad2109"
            },
            {
              "locator": "/mapped_fields/zone_id",
              "source_id": "r63_987b530c2d4da75eb8bca3902798"
            },
            {
              "locator": "/mapped_fields/game_id",
              "source_id": "r63_8328bacbdcca393bd9b93aa9217d"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_8328bacbdcca393bd9b93aa9217d"
            },
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_8328bacbdcca393bd9b93aa9217d"
            },
            {
              "locator": "/mapped_fields/resource_ids",
              "source_id": "r63_5c4c2946432a8b89ef45c675486d"
            },
            {
              "locator": "/mapped_fields/zone_id",
              "source_id": "r63_df5d776c41b16941439e1a363b2e"
            },
            {
              "locator": "/mapped_fields/zone_id",
              "source_id": "r63_0c8c4707f75172e12d434b37297e"
            }
          ]
        }
      ],
      "claim_packets": [
        {
          "fact_id": "C04:game_detail_tekken_8:zone",
          "record_id": "game_detail_tekken_8",
          "facet": "zone",
          "value": "PC Zone; PlayStation 5 Zone",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/game_id",
              "source_id": "r63_e7052c75b2767841a51e6dade36a"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_e7052c75b2767841a51e6dade36a"
            },
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_e7052c75b2767841a51e6dade36a"
            },
            {
              "locator": "/mapped_fields/resource_ids",
              "source_id": "r63_65331c20f193ef240c5184e70cf0"
            },
            {
              "locator": "/mapped_fields/zone_id",
              "source_id": "r63_d1a075421a7e30716a11bfad2109"
            },
            {
              "locator": "/mapped_fields/zone_id",
              "source_id": "r63_987b530c2d4da75eb8bca3902798"
            },
            {
              "locator": "/mapped_fields/game_id",
              "source_id": "r63_8328bacbdcca393bd9b93aa9217d"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_8328bacbdcca393bd9b93aa9217d"
            },
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_8328bacbdcca393bd9b93aa9217d"
            },
            {
              "locator": "/mapped_fields/resource_ids",
              "source_id": "r63_5c4c2946432a8b89ef45c675486d"
            },
            {
              "locator": "/mapped_fields/zone_id",
              "source_id": "r63_df5d776c41b16941439e1a363b2e"
            },
            {
              "locator": "/mapped_fields/zone_id",
              "source_id": "r63_0c8c4707f75172e12d434b37297e"
            }
          ],
          "fixture": false,
          "status": "answer"
        }
      ],
      "semantic_correctness_verified": false
    }
  ],
  "sources": [],
  "positive_contracts": [
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
      "row": 7548,
      "variant": "question",
      "id": "MASTER-GT-EN-02549",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_en_5000_v1.jsonl",
      "row": 2548,
      "variant": "question",
      "id": "MASTER-GT-EN-02549",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    }
  ]
}
```

## 4. What are all the buttons in Call of Duty: Warzone

Key: `9813e160d170afb1642c7a117bdc3ab5253f5372ad62a7eb27ecdba7a283c1cb`; locale `en`; original domain `games`

### R115 saved

```text
Call of Duty: Warzone / PlayStation / PS5 — Melee: R3 — Strike with the butt of the weapon. [S1]
Call of Duty: Warzone / PlayStation / PS5 — Fire Weapon: R2 — Pull the trigger to fire the weapon. [S2]
Call of Duty: Warzone / PlayStation / PS5 — Aim Down Sight Behavior: L2 — Raise the weapon to aim down its sights. [S3]
Call of Duty: Warzone / PlayStation / PS5 — Switch Weapon: Triangle — Swap weapons [S4]
Call of Duty: Warzone / PlayStation / PS5 — Pause: Options — Open settings menu and pause game [S5]
Call of Duty: Warzone / PlayStation / PS5 — Jump/Mantle: Cross — Jump or climb obstacles [S6]
Call of Duty: Warzone / PlayStation / PS5 — Use/Reload: Square — Pick up items, open boxes, farm items, or reload ammunition [S7]
Call of Duty: Warzone / PlayStation / PS5 — Scoreboard: Touch Pad — Open leaderboard and tactics map [S8]
```

### R117 revision03 saved

```text
Call of Duty: Warzone / PlayStation / PS5 — Jump/Mantle: Cross — Jump or climb obstacles [S1]
Call of Duty: Warzone / PlayStation / PS5 — Crouch/Prone/Slide: Circle — Press to change stance or slide your knee while running [S2]
Call of Duty: Warzone / PlayStation / PS5 — Use/Reload: Square — Pick up items, open boxes, farm items, or reload ammunition [S3]
Call of Duty: Warzone / PlayStation / PS5 — Switch Weapon: Triangle — Swap weapons [S4]
Call of Duty: Warzone / PlayStation / PS5 — Campaign, Multiplayer or Co-Op specific: D-Pad — Optional commands depending on game mode such as ping or kill streak [S5]
Call of Duty: Warzone / PlayStation / PS5 — Scoreboard: Touch Pad — Open leaderboard and tactics map [S6]
Call of Duty: Warzone / PlayStation / PS5 — Pause: Options — Open settings menu and pause game [S7]
Call of Duty: Warzone / PlayStation / PS5 — Use Tactical Equipment: L1 — Use smoke grenades, flashbangs, or support devices [S8]
Call of Duty: Warzone / PlayStation / PS5 — Use Lethal Equipment: R1 — Use destruction explosives [S9]
Call of Duty: Warzone / PlayStation / PS5 — Aim Down Sight Behavior: L2 — Raise the weapon to aim down its sights. [S10]
Call of Duty: Warzone / PlayStation / PS5 — Fire Weapon: R2 — Pull the trigger to fire the weapon. [S11]
Call of Duty: Warzone / PlayStation / PS5 — Sprint/Tactical Sprint/Steady Aim: L3 — Press to sprint or hold breath while aiming through scope [S12]
Call of Duty: Warzone / PlayStation / PS5 — Melee: R3 — Strike with the butt of the weapon. [S13]
```

### R118 revision02

```text
Call of Duty: Warzone / PlayStation / PS5 — Jump/Mantle: Cross — Jump or climb obstacles [S1]
Call of Duty: Warzone / PlayStation / PS5 — Crouch/Prone/Slide: Circle — Press to change stance or slide your knee while running [S2]
Call of Duty: Warzone / PlayStation / PS5 — Use/Reload: Square — Pick up items, open boxes, farm items, or reload ammunition [S3]
Call of Duty: Warzone / PlayStation / PS5 — Switch Weapon: Triangle — Swap weapons [S4]
Call of Duty: Warzone / PlayStation / PS5 — Campaign, Multiplayer or Co-Op specific: D-Pad — Optional commands depending on game mode such as ping or kill streak [S5]
Call of Duty: Warzone / PlayStation / PS5 — Scoreboard: Touch Pad — Open leaderboard and tactics map [S6]
Call of Duty: Warzone / PlayStation / PS5 — Pause: Options — Open settings menu and pause game [S7]
Call of Duty: Warzone / PlayStation / PS5 — Use Tactical Equipment: L1 — Use smoke grenades, flashbangs, or support devices [S8]
Call of Duty: Warzone / PlayStation / PS5 — Use Lethal Equipment: R1 — Use destruction explosives [S9]
Call of Duty: Warzone / PlayStation / PS5 — Aim Down Sight Behavior: L2 — Raise the weapon to aim down its sights. [S10]
Call of Duty: Warzone / PlayStation / PS5 — Fire Weapon: R2 — Pull the trigger to fire the weapon. [S11]
Call of Duty: Warzone / PlayStation / PS5 — Sprint/Tactical Sprint/Steady Aim: L3 — Press to sprint or hold breath while aiming through scope [S12]
Call of Duty: Warzone / PlayStation / PS5 — Melee: R3 — Strike with the butt of the weapon. [S13]
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "independent_context_frame",
    "tasks": [
      {
        "quote": "what are all the buttons in call of duty: warzone",
        "domain": "game_controls",
        "category": "C05",
        "operation": "list",
        "facet": "input_bindings",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "6c58f4ee1b62422987cb9c1b80c9c918",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"what are all the buttons in call of duty: warzone\", \"operation\": \"detail\", \"domain\": \"games\", \"facet\": \"game_catalog\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "meaning_review": {
        "basis": "legacy_control_frame_and_current_source_target",
        "model_plan_accepted": true,
        "model_reason": "validated_interpretation_proposal",
        "prior_tasks": [
          {
            "quote": "what are all the buttons in call of duty: warzone",
            "domain": "games",
            "category": "C04",
            "operation": "detail",
            "facet": "game_catalog",
            "target": "",
            "constraints": [],
            "ambiguous": false
          }
        ],
        "business_facts_added": false
      },
      "reason": "independent_context_frame",
      "elapsed_sec": 1.469,
      "http_attempted": true,
      "input_question": "what are all the buttons in call of duty: warzone",
      "legacy_contrast": {
        "domain": "games",
        "operation": "detail",
        "needs": [
          "summarize_detail",
          "check_availability"
        ],
        "reason": "known game alias found; known game title keeps games domain; no clear operation terms; bare known game title treated as detail"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false
  },
  "need_results": [
    {
      "need_id": "r114_n1",
      "task": "game_controls",
      "category": "C05",
      "source_span": "what are all the buttons in call of duty: warzone",
      "execution_query": "what are all the buttons in call of duty: warzone ",
      "status": "supported",
      "reason_codes": [
        "complete_source_binding_set"
      ],
      "receipts": [
        {
          "record_id": "controls_ps5_call_of_duty_warzone",
          "field": "binding_0",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_5b8bc3498422785879e64d31"
            }
          ]
        },
        {
          "record_id": "controls_ps5_call_of_duty_warzone",
          "field": "binding_1",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_5b8bc3498422785879e64d31"
            }
          ]
        },
        {
          "record_id": "controls_ps5_call_of_duty_warzone",
          "field": "binding_2",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_5b8bc3498422785879e64d31"
            }
          ]
        },
        {
          "record_id": "controls_ps5_call_of_duty_warzone",
          "field": "binding_3",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_5b8bc3498422785879e64d31"
            }
          ]
        },
        {
          "record_id": "controls_ps5_call_of_duty_warzone",
          "field": "binding_4",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_5b8bc3498422785879e64d31"
            }
          ]
        },
        {
          "record_id": "controls_ps5_call_of_duty_warzone",
          "field": "binding_5",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_5b8bc3498422785879e64d31"
            }
          ]
        },
        {
          "record_id": "controls_ps5_call_of_duty_warzone",
          "field": "binding_6",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_5b8bc3498422785879e64d31"
            }
          ]
        },
        {
          "record_id": "controls_ps5_call_of_duty_warzone",
          "field": "binding_7",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_5b8bc3498422785879e64d31"
            }
          ]
        },
        {
          "record_id": "controls_ps5_call_of_duty_warzone",
          "field": "binding_8",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_5b8bc3498422785879e64d31"
            }
          ]
        },
        {
          "record_id": "controls_ps5_call_of_duty_warzone",
          "field": "binding_9",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_5b8bc3498422785879e64d31"
            }
          ]
        },
        {
          "record_id": "controls_ps5_call_of_duty_warzone",
          "field": "binding_10",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_5b8bc3498422785879e64d31"
            }
          ]
        },
        {
          "record_id": "controls_ps5_call_of_duty_warzone",
          "field": "binding_11",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_5b8bc3498422785879e64d31"
            }
          ]
        },
        {
          "record_id": "controls_ps5_call_of_duty_warzone",
          "field": "binding_12",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_5b8bc3498422785879e64d31"
            }
          ]
        }
      ],
      "claim_packets": [
        {
          "fact_id": "C05:controls_ps5_call_of_duty_warzone:binding_0",
          "record_id": "controls_ps5_call_of_duty_warzone",
          "facet": "binding_0",
          "value": "Cross — Jump or climb obstacles",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_5b8bc3498422785879e64d31"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C05:controls_ps5_call_of_duty_warzone:binding_1",
          "record_id": "controls_ps5_call_of_duty_warzone",
          "facet": "binding_1",
          "value": "Circle — Press to change stance or slide your knee while running",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_5b8bc3498422785879e64d31"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C05:controls_ps5_call_of_duty_warzone:binding_2",
          "record_id": "controls_ps5_call_of_duty_warzone",
          "facet": "binding_2",
          "value": "Square — Pick up items, open boxes, farm items, or reload ammunition",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_5b8bc3498422785879e64d31"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C05:controls_ps5_call_of_duty_warzone:binding_3",
          "record_id": "controls_ps5_call_of_duty_warzone",
          "facet": "binding_3",
          "value": "Triangle — Swap weapons",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_5b8bc3498422785879e64d31"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C05:controls_ps5_call_of_duty_warzone:binding_4",
          "record_id": "controls_ps5_call_of_duty_warzone",
          "facet": "binding_4",
          "value": "D-Pad — Optional commands depending on game mode such as ping or kill streak",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_5b8bc3498422785879e64d31"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C05:controls_ps5_call_of_duty_warzone:binding_5",
          "record_id": "controls_ps5_call_of_duty_warzone",
          "facet": "binding_5",
          "value": "Touch Pad — Open leaderboard and tactics map",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_5b8bc3498422785879e64d31"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C05:controls_ps5_call_of_duty_warzone:binding_6",
          "record_id": "controls_ps5_call_of_duty_warzone",
          "facet": "binding_6",
          "value": "Options — Open settings menu and pause game",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_5b8bc3498422785879e64d31"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C05:controls_ps5_call_of_duty_warzone:binding_7",
          "record_id": "controls_ps5_call_of_duty_warzone",
          "facet": "binding_7",
          "value": "L1 — Use smoke grenades, flashbangs, or support devices",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_5b8bc3498422785879e64d31"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C05:controls_ps5_call_of_duty_warzone:binding_8",
          "record_id": "controls_ps5_call_of_duty_warzone",
          "facet": "binding_8",
          "value": "R1 — Use destruction explosives",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_5b8bc3498422785879e64d31"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C05:controls_ps5_call_of_duty_warzone:binding_9",
          "record_id": "controls_ps5_call_of_duty_warzone",
          "facet": "binding_9",
          "value": "L2 — Raise the weapon to aim down its sights.",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_5b8bc3498422785879e64d31"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C05:controls_ps5_call_of_duty_warzone:binding_10",
          "record_id": "controls_ps5_call_of_duty_warzone",
          "facet": "binding_10",
          "value": "R2 — Pull the trigger to fire the weapon.",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_5b8bc3498422785879e64d31"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C05:controls_ps5_call_of_duty_warzone:binding_11",
          "record_id": "controls_ps5_call_of_duty_warzone",
          "facet": "binding_11",
          "value": "L3 — Press to sprint or hold breath while aiming through scope",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_5b8bc3498422785879e64d31"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C05:controls_ps5_call_of_duty_warzone:binding_12",
          "record_id": "controls_ps5_call_of_duty_warzone",
          "facet": "binding_12",
          "value": "R3 — Strike with the butt of the weapon.",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_5b8bc3498422785879e64d31"
            }
          ],
          "fixture": false,
          "status": "answer"
        }
      ],
      "semantic_correctness_verified": false
    }
  ],
  "sources": [],
  "positive_contracts": []
}
```

## 5. Please answer from verified studio information: May I record video inside the studio

Key: `9efbf2ac2cde1a5718eeb278350f7f40337ba912828386fee3cc8315ebc6326a`; locale `en`; original domain `studio_rules_penalties`

### R115 saved

```text
**Relevant information**
• Confirmed information: In-game screenshots and video capture are allowed; delete them when finished. This does not confirm filming people or the premises. [S1]
• topic: C10 [S2]
• Scope: {"r114_fact": {"category": "C10", "facet": "owner_policy", "subject": {"th": "บันทึกภาพในเกม", "en": "game capture"}, "label": {"th": "เงื่อนไขและวิธีปฏิบัติ", "en": "conditions and procedure"}, "owner_confirmed": true, "source_record_id": "Q033"}} [S3]

English translation is machine generated and has not been reviewed by the owner.
```

### R117 revision03 saved

```text
No confirmed source is available for the requested detail.
```

### R118 revision02

```text
No confirmed source is available for the requested detail.
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "validated_interpretation_proposal",
    "tasks": [
      {
        "quote": "may i record video inside the studio",
        "domain": "rules",
        "category": "C10",
        "operation": "rule_lookup",
        "facet": "owner_policy",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "6af7e65b13264c718e7b6763cab98ce4",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"may i record video inside the studio\", \"operation\": \"rule_lookup\", \"domain\": \"rules\", \"facet\": \"owner_policy\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 1.453,
      "http_attempted": true,
      "input_question": "may i record video inside the studio",
      "legacy_contrast": {
        "domain": "general",
        "operation": "unknown",
        "needs": [],
        "reason": "domain_terms=2; no clear operation terms"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false
  },
  "need_results": [
    {
      "need_id": "r114_n1",
      "task": "policy",
      "category": "C10",
      "source_span": "may i record video inside the studio",
      "execution_query": "may i record video inside the studio ",
      "status": "missing_source",
      "reason_codes": [
        "entity_not_bound"
      ],
      "receipts": [],
      "claim_packets": [],
      "semantic_correctness_verified": false
    }
  ],
  "sources": [],
  "positive_contracts": []
}
```

## 6. กำลังวางแผนไปใช้บริการ เลยอยากทราบว่า ขอข้อมูลที่ยืนยันได้หน่อยครับ: Maintenance คือช่วงไหน

Key: `a9ecf2e1299ecafcd502f509c23241bf23889fad81c1a196d62f13c9c480d7e2`; locale `th`; original domain `schedule_calendar`

### R115 saved

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

### R117 revision03 saved

```text
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
จันทร์ — ช่วงบำรุงรักษา: 09:00–12:00 [S1]
อังคาร — ช่วงบำรุงรักษา: ไม่มี / None [S2]
พุธ — ช่วงบำรุงรักษา: ไม่มี / None [S3]
พฤหัสบดี — ช่วงบำรุงรักษา: ไม่มี / None [S4]
ศุกร์ — ช่วงบำรุงรักษา: 13:00–16:00 [S5]
เสาร์ — ช่วงบำรุงรักษา: ไม่มี / None [S6]
อาทิตย์ — ช่วงบำรุงรักษา: ไม่มี / None [S7]
```

### R118 revision02

```text
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
จันทร์ — ช่วงบำรุงรักษา: 09:00–12:00 [S1]
อังคาร — ช่วงบำรุงรักษา: ไม่มี / None [S2]
พุธ — ช่วงบำรุงรักษา: ไม่มี / None [S3]
พฤหัสบดี — ช่วงบำรุงรักษา: ไม่มี / None [S4]
ศุกร์ — ช่วงบำรุงรักษา: 13:00–16:00 [S5]
เสาร์ — ช่วงบำรุงรักษา: ไม่มี / None [S6]
อาทิตย์ — ช่วงบำรุงรักษา: ไม่มี / None [S7]
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "validated_interpretation_proposal",
    "tasks": [
      {
        "quote": "maintenance คือช่วงไหน",
        "domain": "schedule",
        "category": "C11",
        "operation": "schedule_lookup",
        "facet": "maintenance_periods",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "b981d1d0347d4f258906d916b6f26bb8",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"maintenance คือช่วงไหน\", \"operation\": \"schedule_lookup\", \"domain\": \"schedule\", \"facet\": \"maintenance_periods\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 1.531,
      "http_attempted": true,
      "input_question": "กำลังวางแผนไปใช้บริการ เลยอยากทราบว่า ขอข้อมูลที่ยืนยันได้หน่อยครับ: maintenance คือช่วงไหน",
      "legacy_contrast": {
        "domain": "general",
        "operation": "unknown",
        "needs": [],
        "reason": "domain_terms=2; no clear operation terms"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false
  },
  "need_results": [
    {
      "need_id": "r114_n1",
      "task": "schedule",
      "category": "C11",
      "source_span": "maintenance คือช่วงไหน",
      "execution_query": "maintenance คือช่วงไหน ",
      "status": "supported",
      "reason_codes": [
        "interpreted_recorded_calendar_facet"
      ],
      "receipts": [
        {
          "record_id": "migrated_schedule_0",
          "field": "maintenance_periods",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/maintenance_periods",
              "source_id": "r66_814dc4183099ea3715eb65d5955d"
            }
          ]
        },
        {
          "record_id": "migrated_schedule_1",
          "field": "maintenance_periods",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/maintenance_periods",
              "source_id": "r66_79ad8fe1d8fdf571be9dd857a9b4"
            }
          ]
        },
        {
          "record_id": "migrated_schedule_2",
          "field": "maintenance_periods",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/maintenance_periods",
              "source_id": "r66_aa6f1c71e4e35173d2c541946b8b"
            }
          ]
        },
        {
          "record_id": "migrated_schedule_3",
          "field": "maintenance_periods",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/maintenance_periods",
              "source_id": "r66_78809ecbb55559e2e9b17d51575c"
            }
          ]
        },
        {
          "record_id": "migrated_schedule_4",
          "field": "maintenance_periods",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/maintenance_periods",
              "source_id": "r66_8b8799fa0b0f242ce50dede11782"
            }
          ]
        },
        {
          "record_id": "migrated_schedule_5",
          "field": "maintenance_periods",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/maintenance_periods",
              "source_id": "r66_3723691dd1c4cd09c3134a91d2c8"
            }
          ]
        },
        {
          "record_id": "migrated_schedule_6",
          "field": "maintenance_periods",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/maintenance_periods",
              "source_id": "r66_091dff62944f36ea9ad9068a5c8b"
            }
          ]
        }
      ],
      "claim_packets": [
        {
          "fact_id": "C11:migrated_schedule_0:maintenance_periods",
          "record_id": "migrated_schedule_0",
          "facet": "maintenance_periods",
          "value": "09:00–12:00",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/maintenance_periods",
              "source_id": "r66_814dc4183099ea3715eb65d5955d"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C11:migrated_schedule_1:maintenance_periods",
          "record_id": "migrated_schedule_1",
          "facet": "maintenance_periods",
          "value": "ไม่มี / None",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/maintenance_periods",
              "source_id": "r66_79ad8fe1d8fdf571be9dd857a9b4"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C11:migrated_schedule_2:maintenance_periods",
          "record_id": "migrated_schedule_2",
          "facet": "maintenance_periods",
          "value": "ไม่มี / None",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/maintenance_periods",
              "source_id": "r66_aa6f1c71e4e35173d2c541946b8b"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C11:migrated_schedule_3:maintenance_periods",
          "record_id": "migrated_schedule_3",
          "facet": "maintenance_periods",
          "value": "ไม่มี / None",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/maintenance_periods",
              "source_id": "r66_78809ecbb55559e2e9b17d51575c"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C11:migrated_schedule_4:maintenance_periods",
          "record_id": "migrated_schedule_4",
          "facet": "maintenance_periods",
          "value": "13:00–16:00",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/maintenance_periods",
              "source_id": "r66_8b8799fa0b0f242ce50dede11782"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C11:migrated_schedule_5:maintenance_periods",
          "record_id": "migrated_schedule_5",
          "facet": "maintenance_periods",
          "value": "ไม่มี / None",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/maintenance_periods",
              "source_id": "r66_3723691dd1c4cd09c3134a91d2c8"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C11:migrated_schedule_6:maintenance_periods",
          "record_id": "migrated_schedule_6",
          "facet": "maintenance_periods",
          "value": "ไม่มี / None",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/maintenance_periods",
              "source_id": "r66_091dff62944f36ea9ad9068a5c8b"
            }
          ],
          "fixture": false,
          "status": "answer"
        }
      ],
      "semantic_correctness_verified": false
    }
  ],
  "sources": [],
  "positive_contracts": []
}
```

## 7. God of War Ragnarök ปุ่มทั้งหมดมีอะไรบ้าง

Key: `b2ff4f05d34e5b2a82ae5cb5ede86f5a05bb022cf13531c682a39d936e4de5b7`; locale `th`; original domain `game_controls`

### R115 saved

```text
God of War Ragnarök / PlayStation / PS5 — แผนที่: Touch Pad — เปิดแผนที่โลก [S1]
God of War Ragnarök / PlayStation / PS5 — วิ่งสปรินต์: L3 — กดเพื่อวิ่ง [S2]
God of War Ragnarök / PlayStation / PS5 — เล็ง (กดค้าง): L2 (Hold) — ง้างอาวุธเตรียมขว้าง [S3]
God of War Ragnarök / PlayStation / PS5 — ล็อกเป้าหมาย: R3 — ล็อกเป้าหมายศัตรู [S4]
God of War Ragnarök / PlayStation / PS5 — มุมกล้อง: R — ควบคุมการหมุนมุมกล้อง [S5]
God of War Ragnarök / PlayStation / PS5 — ติดตั้งอาวุธรอง: D-Pad Left — ชักดาบโซ่ Blades of Chaos [S6]
God of War Ragnarök / PlayStation / PS5 — ติดตั้งอาวุธหลัก: D-Pad Right — ชักขวาน Leviathan [S7]
God of War Ragnarök / PlayStation / PS5 — เคลื่อนที่: L — บังคับทิศทางการเดิน [S8]
```

### R117 revision03 saved

```text
God of War Ragnarök / PlayStation / PS5 — เคลื่อนที่: L — บังคับทิศทางการเดิน [S1]
God of War Ragnarök / PlayStation / PS5 — วิ่งสปรินต์: L3 — กดเพื่อวิ่ง [S2]
God of War Ragnarök / PlayStation / PS5 — พลังสปาร์ตัน: L3 + R3 — ระเบิดความโกรธของเครโทสเพื่อเพิ่มพลังโจมตีและฟื้นฟูพลังชีวิต [S3]
God of War Ragnarök / PlayStation / PS5 — มุมกล้อง: R — ควบคุมการหมุนมุมกล้อง [S4]
God of War Ragnarök / PlayStation / PS5 — ล็อกเป้าหมาย: R3 — ล็อกเป้าหมายศัตรู [S5]
God of War Ragnarök / PlayStation / PS5 — เล็ง (กดค้าง): L2 (Hold) — ง้างอาวุธเตรียมขว้าง [S6]
God of War Ragnarök / PlayStation / PS5 — ป้องกัน (กดค้าง): L1 (Hold) — ยกโล่ขึ้นป้องกันการโจมตี และใช้เป็นปุ่มร่วมสำหรับคำสั่ง Runic/Relic [S7]
God of War Ragnarök / PlayStation / PS5 — โจมตีเบา / รูนเบา / ขว้าง: R1 — โจมตีปกติเบา, ขว้างอาวุธเมื่อกดเล็ง, หรือใช้ท่ารูนเบาเมื่อกดค้าง L1 [S8]
God of War Ragnarök / PlayStation / PS5 — โจมตีหนัก / รูนหนัก: R2 — โจมตีปกติหนัก หรือใช้ท่ารูนหนักเมื่อกดค้าง L1 [S9]
God of War Ragnarök / PlayStation / PS5 — เรียกขวานกลับ / ชาร์จพลังอาวุธ: Triangle — เรียกขวานกลับเข้ามือ หรือชาร์จพลังธาตุให้อาวุธเมื่อกดค้าง L1 [S10]
God of War Ragnarök / PlayStation / PS5 — โต้ตอบ / ใช้งานรีลิค: Circle — สำรวจสภาพแวดล้อม หรือใช้งานไอเทม Relic เมื่อกดค้าง L1 [S11]
God of War Ragnarök / PlayStation / PS5 — คู่หูโจมตี: Square — สั่งคู่หูยิงธนูสนับสนุน [S12]
God of War Ragnarök / PlayStation / PS5 — สเตปหลบ / กลิ้งหลบ: Cross — กด 1 ครั้งเพื่อโยกตัวหลบ หรือกด 2 ครั้งติดเพื่อกลิ้งหลบ [S13]
God of War Ragnarök / PlayStation / PS5 — ติดตั้งอาวุธหลัก: D-Pad Right — ชักขวาน Leviathan [S14]
God of War Ragnarök / PlayStation / PS5 — ติดตั้งอาวุธรอง: D-Pad Left — ชักดาบโซ่ Blades of Chaos [S15]
God of War Ragnarök / PlayStation / PS5 — ติดตั้งอาวุธที่สาม: D-Pad Down — ชักหอก Draupnir Spear [S16]
God of War Ragnarök / PlayStation / PS5 — เปลี่ยนชนิดลูกธนู: D-Pad Up — สลับลูกธนูของคู่หู [S17]
God of War Ragnarök / PlayStation / PS5 — หยุดเกม: Options — หยุดเกมและเปิดเมนูหลัก [S18]
God of War Ragnarök / PlayStation / PS5 — แผนที่: Touch Pad — เปิดแผนที่โลก [S19]
```

### R118 revision02

```text
God of War Ragnarök / PlayStation / PS5 — เคลื่อนที่: L — บังคับทิศทางการเดิน [S1]
God of War Ragnarök / PlayStation / PS5 — วิ่งสปรินต์: L3 — กดเพื่อวิ่ง [S2]
God of War Ragnarök / PlayStation / PS5 — พลังสปาร์ตัน: L3 + R3 — ระเบิดความโกรธของเครโทสเพื่อเพิ่มพลังโจมตีและฟื้นฟูพลังชีวิต [S3]
God of War Ragnarök / PlayStation / PS5 — มุมกล้อง: R — ควบคุมการหมุนมุมกล้อง [S4]
God of War Ragnarök / PlayStation / PS5 — ล็อกเป้าหมาย: R3 — ล็อกเป้าหมายศัตรู [S5]
God of War Ragnarök / PlayStation / PS5 — เล็ง (กดค้าง): L2 (Hold) — ง้างอาวุธเตรียมขว้าง [S6]
God of War Ragnarök / PlayStation / PS5 — ป้องกัน (กดค้าง): L1 (Hold) — ยกโล่ขึ้นป้องกันการโจมตี และใช้เป็นปุ่มร่วมสำหรับคำสั่ง Runic/Relic [S7]
God of War Ragnarök / PlayStation / PS5 — โจมตีเบา / รูนเบา / ขว้าง: R1 — โจมตีปกติเบา, ขว้างอาวุธเมื่อกดเล็ง, หรือใช้ท่ารูนเบาเมื่อกดค้าง L1 [S8]
God of War Ragnarök / PlayStation / PS5 — โจมตีหนัก / รูนหนัก: R2 — โจมตีปกติหนัก หรือใช้ท่ารูนหนักเมื่อกดค้าง L1 [S9]
God of War Ragnarök / PlayStation / PS5 — เรียกขวานกลับ / ชาร์จพลังอาวุธ: Triangle — เรียกขวานกลับเข้ามือ หรือชาร์จพลังธาตุให้อาวุธเมื่อกดค้าง L1 [S10]
God of War Ragnarök / PlayStation / PS5 — โต้ตอบ / ใช้งานรีลิค: Circle — สำรวจสภาพแวดล้อม หรือใช้งานไอเทม Relic เมื่อกดค้าง L1 [S11]
God of War Ragnarök / PlayStation / PS5 — คู่หูโจมตี: Square — สั่งคู่หูยิงธนูสนับสนุน [S12]
God of War Ragnarök / PlayStation / PS5 — สเตปหลบ / กลิ้งหลบ: Cross — กด 1 ครั้งเพื่อโยกตัวหลบ หรือกด 2 ครั้งติดเพื่อกลิ้งหลบ [S13]
God of War Ragnarök / PlayStation / PS5 — ติดตั้งอาวุธหลัก: D-Pad Right — ชักขวาน Leviathan [S14]
God of War Ragnarök / PlayStation / PS5 — ติดตั้งอาวุธรอง: D-Pad Left — ชักดาบโซ่ Blades of Chaos [S15]
God of War Ragnarök / PlayStation / PS5 — ติดตั้งอาวุธที่สาม: D-Pad Down — ชักหอก Draupnir Spear [S16]
God of War Ragnarök / PlayStation / PS5 — เปลี่ยนชนิดลูกธนู: D-Pad Up — สลับลูกธนูของคู่หู [S17]
God of War Ragnarök / PlayStation / PS5 — หยุดเกม: Options — หยุดเกมและเปิดเมนูหลัก [S18]
God of War Ragnarök / PlayStation / PS5 — แผนที่: Touch Pad — เปิดแผนที่โลก [S19]
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "validated_interpretation_proposal",
    "tasks": [
      {
        "quote": "god of war ragnarök ปุ่มทั้งหมดมีอะไรบ้าง",
        "domain": "game_controls",
        "category": "C05",
        "operation": "list",
        "facet": "input_bindings",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "c6e79ee33d5e417da1e3096e41ac0ded",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"god of war ragnarök ปุ่มทั้งหมดมีอะไรบ้าง\", \"operation\": \"list\", \"domain\": \"game_controls\", \"facet\": \"input_bindings\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 1.594,
      "http_attempted": true,
      "input_question": "god of war ragnarök ปุ่มทั้งหมดมีอะไรบ้าง",
      "legacy_contrast": {
        "domain": "game_controls",
        "operation": "control",
        "needs": [
          "list_controls"
        ],
        "reason": "known game alias found; control operation overrides domain; control terms found"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false
  },
  "need_results": [
    {
      "need_id": "r114_n1",
      "task": "game_controls",
      "category": "C05",
      "source_span": "god of war ragnarök ปุ่มทั้งหมดมีอะไรบ้าง",
      "execution_query": "god of war ragnarök ปุ่มทั้งหมดมีอะไรบ้าง ",
      "status": "supported",
      "reason_codes": [
        "complete_source_binding_set"
      ],
      "receipts": [
        {
          "record_id": "controls_ps5_god_of_war_ragnar_k",
          "field": "binding_0",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_14fbfe1964de6dfdec8c3b86"
            }
          ]
        },
        {
          "record_id": "controls_ps5_god_of_war_ragnar_k",
          "field": "binding_1",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_14fbfe1964de6dfdec8c3b86"
            }
          ]
        },
        {
          "record_id": "controls_ps5_god_of_war_ragnar_k",
          "field": "binding_2",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_14fbfe1964de6dfdec8c3b86"
            }
          ]
        },
        {
          "record_id": "controls_ps5_god_of_war_ragnar_k",
          "field": "binding_3",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_14fbfe1964de6dfdec8c3b86"
            }
          ]
        },
        {
          "record_id": "controls_ps5_god_of_war_ragnar_k",
          "field": "binding_4",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_14fbfe1964de6dfdec8c3b86"
            }
          ]
        },
        {
          "record_id": "controls_ps5_god_of_war_ragnar_k",
          "field": "binding_5",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_14fbfe1964de6dfdec8c3b86"
            }
          ]
        },
        {
          "record_id": "controls_ps5_god_of_war_ragnar_k",
          "field": "binding_6",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_14fbfe1964de6dfdec8c3b86"
            }
          ]
        },
        {
          "record_id": "controls_ps5_god_of_war_ragnar_k",
          "field": "binding_7",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_14fbfe1964de6dfdec8c3b86"
            }
          ]
        },
        {
          "record_id": "controls_ps5_god_of_war_ragnar_k",
          "field": "binding_8",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_14fbfe1964de6dfdec8c3b86"
            }
          ]
        },
        {
          "record_id": "controls_ps5_god_of_war_ragnar_k",
          "field": "binding_9",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_14fbfe1964de6dfdec8c3b86"
            }
          ]
        },
        {
          "record_id": "controls_ps5_god_of_war_ragnar_k",
          "field": "binding_10",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_14fbfe1964de6dfdec8c3b86"
            }
          ]
        },
        {
          "record_id": "controls_ps5_god_of_war_ragnar_k",
          "field": "binding_11",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_14fbfe1964de6dfdec8c3b86"
            }
          ]
        },
        {
          "record_id": "controls_ps5_god_of_war_ragnar_k",
          "field": "binding_12",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_14fbfe1964de6dfdec8c3b86"
            }
          ]
        },
        {
          "record_id": "controls_ps5_god_of_war_ragnar_k",
          "field": "binding_13",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_14fbfe1964de6dfdec8c3b86"
            }
          ]
        },
        {
          "record_id": "controls_ps5_god_of_war_ragnar_k",
          "field": "binding_14",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_14fbfe1964de6dfdec8c3b86"
            }
          ]
        },
        {
          "record_id": "controls_ps5_god_of_war_ragnar_k",
          "field": "binding_15",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_14fbfe1964de6dfdec8c3b86"
            }
          ]
        },
        {
          "record_id": "controls_ps5_god_of_war_ragnar_k",
          "field": "binding_16",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_14fbfe1964de6dfdec8c3b86"
            }
          ]
        },
        {
          "record_id": "controls_ps5_god_of_war_ragnar_k",
          "field": "binding_17",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_14fbfe1964de6dfdec8c3b86"
            }
          ]
        },
        {
          "record_id": "controls_ps5_god_of_war_ragnar_k",
          "field": "binding_18",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_14fbfe1964de6dfdec8c3b86"
            }
          ]
        }
      ],
      "claim_packets": [
        {
          "fact_id": "C05:controls_ps5_god_of_war_ragnar_k:binding_0",
          "record_id": "controls_ps5_god_of_war_ragnar_k",
          "facet": "binding_0",
          "value": "L — บังคับทิศทางการเดิน",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_14fbfe1964de6dfdec8c3b86"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C05:controls_ps5_god_of_war_ragnar_k:binding_1",
          "record_id": "controls_ps5_god_of_war_ragnar_k",
          "facet": "binding_1",
          "value": "L3 — กดเพื่อวิ่ง",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_14fbfe1964de6dfdec8c3b86"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C05:controls_ps5_god_of_war_ragnar_k:binding_2",
          "record_id": "controls_ps5_god_of_war_ragnar_k",
          "facet": "binding_2",
          "value": "L3 + R3 — ระเบิดความโกรธของเครโทสเพื่อเพิ่มพลังโจมตีและฟื้นฟูพลังชีวิต",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_14fbfe1964de6dfdec8c3b86"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C05:controls_ps5_god_of_war_ragnar_k:binding_3",
          "record_id": "controls_ps5_god_of_war_ragnar_k",
          "facet": "binding_3",
          "value": "R — ควบคุมการหมุนมุมกล้อง",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_14fbfe1964de6dfdec8c3b86"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C05:controls_ps5_god_of_war_ragnar_k:binding_4",
          "record_id": "controls_ps5_god_of_war_ragnar_k",
          "facet": "binding_4",
          "value": "R3 — ล็อกเป้าหมายศัตรู",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_14fbfe1964de6dfdec8c3b86"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C05:controls_ps5_god_of_war_ragnar_k:binding_5",
          "record_id": "controls_ps5_god_of_war_ragnar_k",
          "facet": "binding_5",
          "value": "L2 (Hold) — ง้างอาวุธเตรียมขว้าง",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_14fbfe1964de6dfdec8c3b86"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C05:controls_ps5_god_of_war_ragnar_k:binding_6",
          "record_id": "controls_ps5_god_of_war_ragnar_k",
          "facet": "binding_6",
          "value": "L1 (Hold) — ยกโล่ขึ้นป้องกันการโจมตี และใช้เป็นปุ่มร่วมสำหรับคำสั่ง Runic/Relic",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_14fbfe1964de6dfdec8c3b86"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C05:controls_ps5_god_of_war_ragnar_k:binding_7",
          "record_id": "controls_ps5_god_of_war_ragnar_k",
          "facet": "binding_7",
          "value": "R1 — โจมตีปกติเบา, ขว้างอาวุธเมื่อกดเล็ง, หรือใช้ท่ารูนเบาเมื่อกดค้าง L1",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_14fbfe1964de6dfdec8c3b86"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C05:controls_ps5_god_of_war_ragnar_k:binding_8",
          "record_id": "controls_ps5_god_of_war_ragnar_k",
          "facet": "binding_8",
          "value": "R2 — โจมตีปกติหนัก หรือใช้ท่ารูนหนักเมื่อกดค้าง L1",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_14fbfe1964de6dfdec8c3b86"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C05:controls_ps5_god_of_war_ragnar_k:binding_9",
          "record_id": "controls_ps5_god_of_war_ragnar_k",
          "facet": "binding_9",
          "value": "Triangle — เรียกขวานกลับเข้ามือ หรือชาร์จพลังธาตุให้อาวุธเมื่อกดค้าง L1",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_14fbfe1964de6dfdec8c3b86"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C05:controls_ps5_god_of_war_ragnar_k:binding_10",
          "record_id": "controls_ps5_god_of_war_ragnar_k",
          "facet": "binding_10",
          "value": "Circle — สำรวจสภาพแวดล้อม หรือใช้งานไอเทม Relic เมื่อกดค้าง L1",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_14fbfe1964de6dfdec8c3b86"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C05:controls_ps5_god_of_war_ragnar_k:binding_11",
          "record_id": "controls_ps5_god_of_war_ragnar_k",
          "facet": "binding_11",
          "value": "Square — สั่งคู่หูยิงธนูสนับสนุน",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_14fbfe1964de6dfdec8c3b86"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C05:controls_ps5_god_of_war_ragnar_k:binding_12",
          "record_id": "controls_ps5_god_of_war_ragnar_k",
          "facet": "binding_12",
          "value": "Cross — กด 1 ครั้งเพื่อโยกตัวหลบ หรือกด 2 ครั้งติดเพื่อกลิ้งหลบ",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_14fbfe1964de6dfdec8c3b86"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C05:controls_ps5_god_of_war_ragnar_k:binding_13",
          "record_id": "controls_ps5_god_of_war_ragnar_k",
          "facet": "binding_13",
          "value": "D-Pad Right — ชักขวาน Leviathan",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_14fbfe1964de6dfdec8c3b86"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C05:controls_ps5_god_of_war_ragnar_k:binding_14",
          "record_id": "controls_ps5_god_of_war_ragnar_k",
          "facet": "binding_14",
          "value": "D-Pad Left — ชักดาบโซ่ Blades of Chaos",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_14fbfe1964de6dfdec8c3b86"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C05:controls_ps5_god_of_war_ragnar_k:binding_15",
          "record_id": "controls_ps5_god_of_war_ragnar_k",
          "facet": "binding_15",
          "value": "D-Pad Down — ชักหอก Draupnir Spear",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_14fbfe1964de6dfdec8c3b86"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C05:controls_ps5_god_of_war_ragnar_k:binding_16",
          "record_id": "controls_ps5_god_of_war_ragnar_k",
          "facet": "binding_16",
          "value": "D-Pad Up — สลับลูกธนูของคู่หู",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_14fbfe1964de6dfdec8c3b86"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C05:controls_ps5_god_of_war_ragnar_k:binding_17",
          "record_id": "controls_ps5_god_of_war_ragnar_k",
          "facet": "binding_17",
          "value": "Options — หยุดเกมและเปิดเมนูหลัก",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_14fbfe1964de6dfdec8c3b86"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C05:controls_ps5_god_of_war_ragnar_k:binding_18",
          "record_id": "controls_ps5_god_of_war_ragnar_k",
          "facet": "binding_18",
          "value": "Touch Pad — เปิดแผนที่โลก",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_14fbfe1964de6dfdec8c3b86"
            }
          ],
          "fixture": false,
          "status": "answer"
        }
      ],
      "semantic_correctness_verified": false
    }
  ],
  "sources": [],
  "positive_contracts": [
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
      "row": 3170,
      "variant": "question",
      "id": "MASTER-GT-TH-03171",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
      "row": 3170,
      "variant": "question",
      "id": "MASTER-GT-TH-03171",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_th_5000_v1.jsonl",
      "row": 3170,
      "variant": "question",
      "id": "MASTER-GT-TH-03171",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_th_5000_v2.jsonl",
      "row": 3170,
      "variant": "question",
      "id": "MASTER-GT-TH-03171",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    }
  ]
}
```

## 8. กำลังวางแผนจะไปใช้บริการ อพดีอยากรู้ว่า วันอังคารศูนย์เปิดกี่โมง

Key: `f10707b2c0244f8083805c71be540378e1f2090baa4cfb2a10ad7af8cc422f7f`; locale `th`; original domain `schedule_calendar`

### R115 saved

```text
ข้อมูลที่เชื่อมกับรายการนี้ไม่ถูกต้องหรือไม่อยู่ในขอบเขตที่อนุญาต จึงยังยืนยันคำตอบไม่ได้ครับ
```

### R117 revision03 saved

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### R118 revision02

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "validated_interpretation_proposal",
    "tasks": [
      {
        "quote": "วันอังคารศูนย์เปิดกี่โมง",
        "domain": "schedule",
        "category": "C11",
        "operation": "schedule_lookup",
        "facet": "open_periods",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "ba922462f0c5452ca12e710d061c1199",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"วันอังคารศูนย์เปิดกี่โมง\", \"operation\": \"schedule_lookup\", \"domain\": \"schedule\", \"facet\": \"open_periods\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 1.625,
      "http_attempted": true,
      "input_question": "กำลังวางแผนจะไปใช้บริการ อพดีอยากรู้ว่า วันอังคารศูนย์เปิดกี่โมง",
      "legacy_contrast": {
        "domain": "schedule",
        "operation": "schedule_lookup",
        "needs": [
          "lookup_schedule"
        ],
        "reason": "domain_terms=3; schedule terms found"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false
  },
  "need_results": [
    {
      "need_id": "r114_n1",
      "task": "schedule",
      "category": "C11",
      "source_span": "วันอังคารศูนย์เปิดกี่โมง",
      "execution_query": "วันอังคารศูนย์เปิดกี่โมง ",
      "status": "missing_source",
      "reason_codes": [
        "requested_facet_not_bound"
      ],
      "receipts": [],
      "claim_packets": [],
      "semantic_correctness_verified": false
    }
  ],
  "sources": [],
  "positive_contracts": []
}
```

## 9. กำลังวางแผนไปใช้บริการ เลยอยากทราบว่า ขอข้อมูลเรื่องระงับสิทธิ์ชั่วคราว

Key: `00301c15cd98d9ae70f652fc7e3e088e82b1780bf462c6be801ec81eec2a824a`; locale `th`; original domain `studio_rules_penalties`

### R115 saved

```text
**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: หากผู้ใช้งานละเมิดกฎซ้ำหรือกระทำการรุนแรง อาจถูกระงับสิทธิ์การใช้งานเป็นระยะเวลา 1-7 วัน ขึ้นอยู่กับลักษณะของการละเมิด [S1]
• หัวข้อเชิงความหมาย: knowledge [S2]

**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: หากผู้ใช้งานละเมิดกฎซ้ำหรือกระทำการรุนแรง อาจถูกระงับสิทธิ์การใช้งานชั่วคราวเป็นระยะเวลา 1-7 วัน ขึ้นอยู่กับลักษณะของการละเมิด [S3]
• หัวข้อเชิงความหมาย: penalty [S4]

**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: หากพบการละเมิดกฎ ผู้ใช้งานจะได้รับคำเตือน และอาจถูกระงับสิทธิ์การใช้งานชั่วคราวหรือถาวร ขึ้นอยู่กับความรุนแรง [S5]
• หัวข้อเชิงความหมาย: knowledge [S6]
```

### R117 revision03 saved

```text
**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: หากผู้ใช้งานละเมิดกฎซ้ำหรือกระทำการรุนแรง อาจถูกระงับสิทธิ์การใช้งานเป็นระยะเวลา 1-7 วัน ขึ้นอยู่กับลักษณะของการละเมิด [S1]
• หัวข้อเชิงความหมาย: knowledge [S2]

**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: หากผู้ใช้งานละเมิดกฎซ้ำหรือกระทำการรุนแรง อาจถูกระงับสิทธิ์การใช้งานชั่วคราวเป็นระยะเวลา 1-7 วัน ขึ้นอยู่กับลักษณะของการละเมิด [S3]
• หัวข้อเชิงความหมาย: penalty [S4]

**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: หากพบการละเมิดกฎ ผู้ใช้งานจะได้รับคำเตือน และอาจถูกระงับสิทธิ์การใช้งานชั่วคราวหรือถาวร ขึ้นอยู่กับความรุนแรง [S5]
• หัวข้อเชิงความหมาย: knowledge [S6]
```

### R118 revision02

```text
**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: หากผู้ใช้งานละเมิดกฎซ้ำหรือกระทำการรุนแรง อาจถูกระงับสิทธิ์การใช้งานเป็นระยะเวลา 1-7 วัน ขึ้นอยู่กับลักษณะของการละเมิด [S1]
• หัวข้อเชิงความหมาย: knowledge [S2]

**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: หากผู้ใช้งานละเมิดกฎซ้ำหรือกระทำการรุนแรง อาจถูกระงับสิทธิ์การใช้งานชั่วคราวเป็นระยะเวลา 1-7 วัน ขึ้นอยู่กับลักษณะของการละเมิด [S3]
• หัวข้อเชิงความหมาย: penalty [S4]

**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: หากพบการละเมิดกฎ ผู้ใช้งานจะได้รับคำเตือน และอาจถูกระงับสิทธิ์การใช้งานชั่วคราวหรือถาวร ขึ้นอยู่กับความรุนแรง [S5]
• หัวข้อเชิงความหมาย: knowledge [S6]
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "validated_interpretation_proposal",
    "tasks": [
      {
        "quote": "ขอข้อมูลเรื่องระงับสิทธิ์ชั่วคราว",
        "domain": "general",
        "category": null,
        "operation": "unknown",
        "facet": "",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "4cafc4bcba7b43a2a80a0961b61ddba4",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"ขอข้อมูลเรื่องระงับสิทธิ์ชั่วคราว\", \"operation\": \"unknown\", \"domain\": \"general\", \"facet\": \"\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 1.75,
      "http_attempted": true,
      "input_question": "กำลังวางแผนไปใช้บริการ เลยอยากทราบว่า ขอข้อมูลเรื่องระงับสิทธิ์ชั่วคราว",
      "legacy_contrast": {
        "domain": "general",
        "operation": "unknown",
        "needs": [],
        "reason": "domain_terms=2; no clear operation terms"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false,
    "execution_path": "compatibility_fallback"
  },
  "need_results": [
    {
      "need_id": "n1",
      "task": "policy",
      "predicate": "policy_applicability",
      "source_span": "กำลังวางแผนไปใช้บริการ เลยอยากทราบว่า ขอข้อมูลเรื่องระงับสิทธิ์ชั่วคราว",
      "status": "scope_unverified",
      "reason_codes": [
        "compatibility_scope_not_migrated"
      ],
      "slots": {
        "interpretation": {
          "value": "policy",
          "origin": "current_user",
          "source_span": {
            "start": 0,
            "end": 71,
            "quote": "กำลังวางแผนไปใช้บริการ เลยอยากทราบว่า ขอข้อมูลเรื่องระงับสิทธิ์ชั่วคราว"
          }
        }
      },
      "record_ids": [
        "migrated_faq_curated_penalty_temp_suspension",
        "migrated_faq_rule_penalty_temp_suspension",
        "migrated_faq_curated_penalty_warning_suspension"
      ],
      "receipts": [
        {
          "need_id": "n1",
          "record_id": "migrated_faq_curated_penalty_temp_suspension",
          "field": "answer",
          "predicate": "policy_applicability",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/answer",
              "source_id": "r66_en_2783a88ebbc702b285dfd194"
            }
          ],
          "release_id": "migration-preview-r69",
          "revision": 3,
          "validity": {
            "effective_from": null,
            "effective_until": null,
            "state": "unknown"
          },
          "claim_entailment_verified": false
        },
        {
          "need_id": "n1",
          "record_id": "migrated_faq_curated_penalty_temp_suspension",
          "field": "topic",
          "predicate": "policy_applicability",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/topic",
              "source_id": "r63_80a1ac3271dfe9b81472447da789"
            }
          ],
          "release_id": "migration-preview-r69",
          "revision": 3,
          "validity": {
            "effective_from": null,
            "effective_until": null,
            "state": "unknown"
          },
          "claim_entailment_verified": false
        },
        {
          "need_id": "n1",
          "record_id": "migrated_faq_rule_penalty_temp_suspension",
          "field": "answer",
          "predicate": "policy_applicability",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/answer",
              "source_id": "r63_2b7355ae2f6ab12f12875d61735f"
            }
          ],
          "release_id": "migration-preview-r69",
          "revision": 3,
          "validity": {
            "effective_from": null,
            "effective_until": null,
            "state": "unknown"
          },
          "claim_entailment_verified": false
        },
        {
          "need_id": "n1",
          "record_id": "migrated_faq_rule_penalty_temp_suspension",
          "field": "topic",
          "predicate": "policy_applicability",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/topic",
              "source_id": "r63_2b7355ae2f6ab12f12875d61735f"
            }
          ],
          "release_id": "migration-preview-r69",
          "revision": 3,
          "validity": {
            "effective_from": null,
            "effective_until": null,
            "state": "unknown"
          },
          "claim_entailment_verified": false
        },
        {
          "need_id": "n1",
          "record_id": "migrated_faq_curated_penalty_warning_suspension",
          "field": "answer",
          "predicate": "policy_applicability",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/answer",
              "source_id": "r66_en_0d2713d4131040431385858d"
            }
          ],
          "release_id": "migration-preview-r69",
          "revision": 2,
          "validity": {
            "effective_from": null,
            "effective_until": null,
            "state": "unknown"
          },
          "claim_entailment_verified": false
        },
        {
          "need_id": "n1",
          "record_id": "migrated_faq_curated_penalty_warning_suspension",
          "field": "topic",
          "predicate": "policy_applicability",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/topic",
              "source_id": "r63_ed582c5d3cdd86ae2adb49a0c1ea"
            }
          ],
          "release_id": "migration-preview-r69",
          "revision": 2,
          "validity": {
            "effective_from": null,
            "effective_until": null,
            "state": "unknown"
          },
          "claim_entailment_verified": false
        }
      ],
      "coverage": {
        "version": 1,
        "predicate": "policy_applicability",
        "task": "policy",
        "decision": "scope_unverified",
        "reason_codes": [
          "compatibility_scope_not_migrated"
        ],
        "receipts": [
          {
            "need_id": "n1",
            "record_id": "migrated_faq_curated_penalty_temp_suspension",
            "field": "answer",
            "predicate": "policy_applicability",
            "evidence_refs": [
              {
                "locator": "/mapped_fields/answer",
                "source_id": "r66_en_2783a88ebbc702b285dfd194"
              }
            ],
            "release_id": "migration-preview-r69",
            "revision": 3,
            "validity": {
              "effective_from": null,
              "effective_until": null,
              "state": "unknown"
            },
            "claim_entailment_verified": false
          },
          {
            "need_id": "n1",
            "record_id": "migrated_faq_curated_penalty_temp_suspension",
            "field": "topic",
            "predicate": "policy_applicability",
            "evidence_refs": [
              {
                "locator": "/mapped_fields/topic",
                "source_id": "r63_80a1ac3271dfe9b81472447da789"
              }
            ],
            "release_id": "migration-preview-r69",
            "revision": 3,
            "validity": {
              "effective_from": null,
              "effective_until": null,
              "state": "unknown"
            },
            "claim_entailment_verified": false
          },
          {
            "need_id": "n1",
            "record_id": "migrated_faq_rule_penalty_temp_suspension",
            "field": "answer",
            "predicate": "policy_applicability",
            "evidence_refs": [
              {
                "locator": "/mapped_fields/answer",
                "source_id": "r63_2b7355ae2f6ab12f12875d61735f"
              }
            ],
            "release_id": "migration-preview-r69",
            "revision": 3,
            "validity": {
              "effective_from": null,
              "effective_until": null,
              "state": "unknown"
            },
            "claim_entailment_verified": false
          },
          {
            "need_id": "n1",
            "record_id": "migrated_faq_rule_penalty_temp_suspension",
            "field": "topic",
            "predicate": "policy_applicability",
            "evidence_refs": [
              {
                "locator": "/mapped_fields/topic",
                "source_id": "r63_2b7355ae2f6ab12f12875d61735f"
              }
            ],
            "release_id": "migration-preview-r69",
            "revision": 3,
            "validity": {
              "effective_from": null,
              "effective_until": null,
              "state": "unknown"
            },
            "claim_entailment_verified": false
          },
          {
            "need_id": "n1",
            "record_id": "migrated_faq_curated_penalty_warning_suspension",
            "field": "answer",
            "predicate": "policy_applicability",
            "evidence_refs": [
              {
                "locator": "/mapped_fields/answer",
                "source_id": "r66_en_0d2713d4131040431385858d"
              }
            ],
            "release_id": "migration-preview-r69",
            "revision": 2,
            "validity": {
              "effective_from": null,
              "effective_until": null,
              "state": "unknown"
            },
            "claim_entailment_verified": false
          },
          {
            "need_id": "n1",
            "record_id": "migrated_faq_curated_penalty_warning_suspension",
            "field": "topic",
            "predicate": "policy_applicability",
            "evidence_refs": [
              {
                "locator": "/mapped_fields/topic",
                "source_id": "r63_ed582c5d3cdd86ae2adb49a0c1ea"
              }
            ],
            "release_id": "migration-preview-r69",
            "revision": 2,
            "validity": {
              "effective_from": null,
              "effective_until": null,
              "state": "unknown"
            },
            "claim_entailment_verified": false
          }
        ],
        "semantic_correctness_verified": false
      },
      "coverage_basis": "typed predicate contract where available; unmigrated scope remains unverified"
    }
  ],
  "sources": [],
  "positive_contracts": []
}
```

## 10. How much does it cost for an adult to play VR for one hour?

Key: `0d05eaf601eadf916bc92c4e43a8a10ce1897c3412ccc9c1534782cda7c52ef7`; locale `en`; original domain `service_fee`

### R115 saved

```text
Rates last reaffirmed by the owner on 2026-10-20; no new effective interval was established.
VR Station 30 นาที / PSU Student and Staff — per-person price for the rate duration: 0 THB per person for 30 minutes [S1]
VR Station 30 นาที / PSU Alumni and General Student — per-person price for the rate duration: 190 THB per person for 30 minutes [S2]
VR Station 30 นาที / General Adult — per-person price for the rate duration: 525 THB per person for 30 minutes [S3]
VR Station 1 ชั่วโมง / PSU Student and Staff — per-person price for the rate duration: 0 THB per person for 60 minutes [S4]
VR Station 1 ชั่วโมง / PSU Alumni and General Student — per-person price for the rate duration: 375 THB per person for 60 minutes [S5]
VR Station 1 ชั่วโมง / General Adult — per-person price for the rate duration: 1050 THB per person for 60 minutes [S6]
```

### R117 revision03 saved

```text
Rates last reaffirmed by the owner on 2026-10-20; no new effective interval was established.
VR Station 30 นาที / General Adult — per-person price for the rate duration: 525 THB per person for 30 minutes [S1]
VR Station 1 ชั่วโมง / General Adult — per-person price for the rate duration: 1050 THB per person for 60 minutes [S2]
```

### R118 revision02

```text
Rates last reaffirmed by the owner on 2026-10-20; no new effective interval was established.
VR Station 1 ชั่วโมง / General Adult — per-person price for the rate duration: 1050 THB for 60 minutes under the declared explicit_whole_sessions rule [S1]
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "validated_interpretation_proposal",
    "tasks": [
      {
        "quote": "how much does it cost for an adult to play vr for one hour?",
        "domain": "service_fee",
        "category": "C06",
        "operation": "price_calculate",
        "facet": "amount",
        "target": "",
        "constraints": [
          {
            "slot": "audience",
            "quote": "adult",
            "source_record_id": "audience_general_adult"
          }
        ],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "4aaad2ba2c3c4a6392f2a6bf5ee7f0c8",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"how much does it cost for an adult to play vr for one hour?\", \"operation\": \"price_calculate\", \"domain\": \"service_fee\", \"facet\": \"amount\", \"target\": \"\", \"ambiguous\": false, \"constraints\": [{\"slot\": \"audience\", \"quote\": \"adult\", \"source_record_id\": \"audience_general_adult\"}]}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 7.86,
      "http_attempted": true,
      "input_question": "how much does it cost for an adult to play vr for one hour?",
      "legacy_contrast": {
        "domain": "general",
        "operation": "unknown",
        "needs": [],
        "reason": "domain_terms=2; no clear operation terms"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false
  },
  "need_results": [
    {
      "need_id": "r114_n1",
      "task": "price",
      "category": "C06",
      "source_span": "how much does it cost for an adult to play vr for one hour?",
      "execution_query": "how much does it cost for an adult to play vr for 1 hour?  General Adult",
      "status": "supported",
      "reason_codes": [
        "typed_requested_fields"
      ],
      "receipts": [
        {
          "record_id": "migrated_rate_vr_60_1_5_general_adult",
          "field": "amount_minor",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/amount_minor",
              "source_id": "r63_c9bbab5aacb07f3adf90aab858e0"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_c9bbab5aacb07f3adf90aab858e0"
            },
            {
              "locator": "/mapped_fields/audience_id",
              "source_id": "r63_c9bbab5aacb07f3adf90aab858e0"
            },
            {
              "locator": "/mapped_fields/duration_minutes",
              "source_id": "r63_c9bbab5aacb07f3adf90aab858e0"
            },
            {
              "locator": "/fields/answer",
              "source_id": "r114_affirm_rate_0d5e3ccb4a50d3a637cb2118"
            },
            {
              "locator": "/fields/scope_note",
              "source_id": "r114_affirm_rate_0d5e3ccb4a50d3a637cb2118"
            }
          ]
        }
      ],
      "claim_packets": [
        {
          "fact_id": "C06:migrated_rate_vr_60_1_5_general_adult:amount",
          "record_id": "migrated_rate_vr_60_1_5_general_adult",
          "facet": "amount",
          "value": "1050 THB for 60 minutes under the declared explicit_whole_sessions rule",
          "numeric": 1050.0,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/amount_minor",
              "source_id": "r63_c9bbab5aacb07f3adf90aab858e0"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_c9bbab5aacb07f3adf90aab858e0"
            },
            {
              "locator": "/mapped_fields/audience_id",
              "source_id": "r63_c9bbab5aacb07f3adf90aab858e0"
            },
            {
              "locator": "/mapped_fields/duration_minutes",
              "source_id": "r63_c9bbab5aacb07f3adf90aab858e0"
            },
            {
              "locator": "/fields/answer",
              "source_id": "r114_affirm_rate_0d5e3ccb4a50d3a637cb2118"
            },
            {
              "locator": "/fields/scope_note",
              "source_id": "r114_affirm_rate_0d5e3ccb4a50d3a637cb2118"
            }
          ],
          "fixture": false,
          "status": "answer"
        }
      ],
      "semantic_correctness_verified": false
    }
  ],
  "sources": [],
  "positive_contracts": []
}
```

## 11. กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า มีเมาส์เกใมิ่งให้ไหม

Key: `0f5e0fd0f7f40fed2280aa84538bf0cbe41bd47c2924eaeed55a495188465322`; locale `th`; original domain `equipment`

### R115 saved

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

### R117 revision03 saved

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### R118 revision02

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "validated_interpretation_proposal",
    "tasks": [
      {
        "quote": "กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า มีเมาส์เกใมิ่งให้ไหม",
        "domain": "equipment",
        "category": "C03",
        "operation": "availability",
        "facet": "usage",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "c1cb86e70d1641f8a5be443f85f0d5af",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า มีเมาส์เกใมิ่งให้ไหม\", \"operation\": \"availability\", \"domain\": \"equipment\", \"facet\": \"usage\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 1.953,
      "http_attempted": true,
      "input_question": "กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า มีเมาส์เกใมิ่งให้ไหม",
      "legacy_contrast": {
        "domain": "general",
        "operation": "unknown",
        "needs": [],
        "reason": "domain_terms=2; no clear operation terms"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false
  },
  "need_results": [
    {
      "need_id": "r114_n1",
      "task": "equipment",
      "category": "C03",
      "source_span": "กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า มีเมาส์เกใมิ่งให้ไหม",
      "execution_query": "กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า มีเมาส์เกใมิ่งให้ไหม ",
      "status": "missing_source",
      "reason_codes": [
        "entity_not_bound"
      ],
      "receipts": [],
      "claim_packets": [],
      "semantic_correctness_verified": false
    }
  ],
  "sources": [],
  "positive_contracts": []
}
```

## 12. หำลังจะลงแข่ง VALORANT อยากรู้เรื่องบทลงโทษ

Key: `104194c21fa2ded7f4d2e573457e1dbc6284cb6cb57e978bb6512df8c99a9147`; locale `th`; original domain `competition_rules`

### R115 saved

```text
VALORANT — แนวเกม: เกมยิง Tactical FPS แบบทีม 5v5 [S1]
VALORANT — บริการที่มีเกมนี้: PC #01-#02; PC #03-#10 [S2]
VALORANT — คำอธิบายเกม: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ [S3]
VALORANT — วิธีเล่น: ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือกู้ Spike การเล่นเน้นการเล็ง การสื่อสาร การใช้สกิล และการเล่นเป็นทีม [S4]
```

### R117 revision03 saved

```text
กฎระเบียบและรูปแบบการแข่งขัน VALORANT — บทลงโทษ: เจ้าหน้าที่จะพิจารณาโทษตามเจตนา (Intent) ผลกระทบ (Impact) [S1]
```

### R118 revision02

```text
กฎระเบียบและรูปแบบการแข่งขัน VALORANT — บทลงโทษ: เจ้าหน้าที่จะพิจารณาโทษตามเจตนา (Intent) ผลกระทบ (Impact) [S1]
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "validated_interpretation_proposal",
    "tasks": [
      {
        "quote": "หำลังจะลงแข่ง valorant อยากรู้เรื่องบทลงโทษ",
        "domain": "competition_rules",
        "category": "C13",
        "operation": "rule_lookup",
        "facet": "rule_clause",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "9d2fbdb26ed2410b84037f37e92f60de",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"หำลังจะลงแข่ง valorant อยากรู้เรื่องบทลงโทษ\", \"operation\": \"rule_lookup\", \"domain\": \"competition_rules\", \"facet\": \"rule_clause\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 1.609,
      "http_attempted": true,
      "input_question": "หำลังจะลงแข่ง valorant อยากรู้เรื่องบทลงโทษ",
      "legacy_contrast": {
        "domain": "games",
        "operation": "rule_lookup",
        "needs": [
          "lookup_rule"
        ],
        "reason": "known game alias found; rule terms found"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false
  },
  "need_results": [
    {
      "need_id": "r114_n1",
      "task": "competition_rules",
      "category": "C13",
      "source_span": "หำลังจะลงแข่ง valorant อยากรู้เรื่องบทลงโทษ",
      "execution_query": "หำลังจะลงแข่ง valorant อยากรู้เรื่องบทลงโทษ ",
      "status": "supported",
      "reason_codes": [
        "event_clause_dependency_read"
      ],
      "receipts": [
        {
          "record_id": "r114_valorant_71_rule_clause",
          "field": "answer",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/fields/answer",
              "source_id": "r114_import_63383df8d01ee9aed91a872c"
            }
          ]
        }
      ],
      "claim_packets": [
        {
          "fact_id": "C13:r114_valorant_71_rule_clause:rule_clause",
          "record_id": "r114_valorant_71_rule_clause",
          "facet": "rule_clause",
          "value": "เจ้าหน้าที่จะพิจารณาโทษตามเจตนา (Intent) ผลกระทบ (Impact)",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/fields/answer",
              "source_id": "r114_import_63383df8d01ee9aed91a872c"
            }
          ],
          "fixture": false,
          "status": "answer"
        }
      ],
      "semantic_correctness_verified": false
    }
  ],
  "sources": [],
  "positive_contracts": []
}
```

## 13. รบกวนเช็กข้อมูลของศูนย์ให้หน่อยครับ ขอข้อมูลเรื่องพบปัญหา เครื่อง

Key: `11f9129c3b0361cac8d62bd3fdfd6bb70ad00435c97d5fbce522b4e8a4545a38`; locale `th`; original domain `studio_rules_penalties`

### R115 saved

```text
ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ พบปัญหา — เครื่อง เช่น คำถามตั้งต้น ไม่จำเป็นต้องเก็บทุก paraphrase / ข้อมูลที่ยืนยันได้ / หัวข้อเชิงความหมาย?
```

### R117 revision03 saved

```text
ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ พบปัญหา — เครื่อง เช่น คำถามตั้งต้น ไม่จำเป็นต้องเก็บทุก paraphrase / ข้อมูลที่ยืนยันได้ / หัวข้อเชิงความหมาย?
```

### R118 revision02

```text
ต้องการทราบเรื่องใดเกี่ยวกับ พบปัญหา — เครื่อง ครับ? ขอรายละเอียดสถานการณ์เพิ่มอีกนิดครับ
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "validated_interpretation_proposal",
    "tasks": [
      {
        "quote": "ขอข้อมูลเรื่องพบปัญหา เครื่อง",
        "domain": "general",
        "category": null,
        "operation": "general_answer",
        "facet": "",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "c225296bb03d45caa08915b680e802f5",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"รบกวนเช็กข้อมูลของศูนย์ให้หน่อยครับ\", \"operation\": \"general_answer\", \"domain\": \"general\", \"facet\": \"\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}, {\"quote\": \"ขอข้อมูลเรื่องพบปัญหา เครื่อง\", \"operation\": \"general_answer\", \"domain\": \"general\", \"facet\": \"\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 2.875,
      "http_attempted": true,
      "input_question": "รบกวนเช็กข้อมูลของศูนย์ให้หน่อยครับ ขอข้อมูลเรื่องพบปัญหา เครื่อง",
      "legacy_contrast": {
        "domain": "general",
        "operation": "unknown",
        "needs": [],
        "reason": "domain_terms=2; no clear operation terms"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false,
    "execution_path": "compatibility_fallback"
  },
  "need_results": [
    {
      "need_id": "n1",
      "task": "faq_content",
      "predicate": "unresolved",
      "source_span": "เช็กข้อมูลของศูนย์ให้หน่อยครับ ขอข้อมูลเรื่องพบปัญหา เครื่อง",
      "status": "ambiguous_interpretation",
      "reason_codes": [
        "no_accepted_interpretation"
      ],
      "slots": {},
      "record_ids": [
        "migrated_faq_rule_report_problem"
      ],
      "receipts": [],
      "coverage": {
        "version": 1,
        "predicate": "unresolved",
        "task": "unresolved",
        "decision": "scope_unverified",
        "reason_codes": [
          "compatibility_scope_not_migrated"
        ],
        "receipts": [],
        "semantic_correctness_verified": false
      },
      "coverage_basis": "typed predicate contract where available; unmigrated scope remains unverified",
      "read_graph": {
        "graph": {
          "op": "all_of",
          "children": [
            {
              "op": "all_of",
              "children": [
                {
                  "op": "any_of",
                  "children": [
                    {
                      "op": "all_of",
                      "children": [
                        {
                          "op": "field",
                          "children": [],
                          "record_id": "migrated_faq_rule_report_problem",
                          "key": "answer",
                          "reason": ""
                        }
                      ],
                      "record_id": "",
                      "key": "",
                      "reason": ""
                    }
                  ],
                  "record_id": "",
                  "key": "",
                  "reason": ""
                }
              ],
              "record_id": "",
              "key": "",
              "reason": ""
            }
          ],
          "record_id": "",
          "key": "",
          "reason": ""
        },
        "targets": [
          "migrated_faq_rule_report_problem"
        ],
        "relation_paths": [],
        "evaluation": {
          "status": "supported",
          "receipts": [
            {
              "need_id": "n1",
              "subject": "migrated_faq_rule_report_problem",
              "record_id": "migrated_faq_rule_report_problem",
              "predicate": "unresolved",
              "field": "answer",
              "value": {
                "en": "If there is a usage problem, inappropriate behavior, or any concern, users should notify staff immediately.",
                "th": "หากพบปัญหาการใช้งาน พฤติกรรมที่ไม่เหมาะสม หรือข้อกังวลใด ๆ ควรแจ้งเจ้าหน้าที่ทันที"
              },
              "revision": 3,
              "units": null,
              "applicability": {
                "effective_from": null,
                "effective_until": null,
                "state": "unknown"
              },
              "release_id": "migration-preview-r69",
              "epoch": 2093,
              "evidence_refs": [
                {
                  "locator": "/mapped_fields/answer",
                  "source_id": "r63_f08136af52ab7645109d0a472887"
                }
              ],
              "sources": [
                {
                  "source_id": "r63_f08136af52ab7645109d0a472887",
                  "sha256": "f39afd05d9f2348fcb4fd959e74fbfc7351b05d543e29d47e24450002413c780",
                  "authority_for": [
                    "faq"
                  ],
                  "locator": "/mapped_fields/answer"
                }
              ],
              "verification": "typed_value_and_relation",
              "prose_entailment_verified": false
            }
          ]
        },
        "required_claims_delivered": false
      },
      "claim_packets": []
    }
  ],
  "sources": [],
  "positive_contracts": []
}
```

## 14. ขอสอบถามหน่อยครับ New Super Mario Bros. U Deluxe เล่นได้ที่โซนไหน

Key: `1f7c4f9acc3f321bb2f052679f405ebd9f9bae73ad634842a3e0f95afba60813`; locale `th`; original domain `game_detail`

### R115 saved

```text
New Super Mario Bros. U Deluxe — บริการที่มีเกมนี้: Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons) [S1]
```

### R117 revision03 saved

```text
ยังยืนยันโซนจากความสัมพันธ์ข้อมูลไม่ได้ แต่ยืนยันบริการที่มีเกมนี้ได้ดังนี้
New Super Mario Bros. U Deluxe — บริการที่มีเกมนี้: Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons) [S1]
```

### R118 revision02

```text
ยังยืนยันโซนจากความสัมพันธ์ข้อมูลไม่ได้ แต่ยืนยันบริการที่มีเกมนี้ได้ดังนี้
New Super Mario Bros. U Deluxe — บริการที่มีเกมนี้: Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons) [S1]
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "independent_context_frame",
    "tasks": [
      {
        "quote": "new super mario bros. u deluxe เล่นได้ที่โซนไหน",
        "domain": "games",
        "category": "C04",
        "operation": "detail",
        "facet": "zone",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "d148abb183c0418593f8e118944b8670",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"new super mario bros. u deluxe เล่นได้ที่โซนไหน\", \"operation\": \"availability\", \"domain\": \"games\", \"facet\": \"zone\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "meaning_review": {
        "basis": "current_game_and_explicit_zone_request",
        "model_plan_accepted": true,
        "model_reason": "validated_interpretation_proposal",
        "prior_tasks": [
          {
            "quote": "new super mario bros. u deluxe เล่นได้ที่โซนไหน",
            "domain": "games",
            "category": "C04",
            "operation": "availability",
            "facet": "zone",
            "target": "",
            "constraints": [],
            "ambiguous": false
          }
        ],
        "business_facts_added": false
      },
      "reason": "independent_context_frame",
      "elapsed_sec": 7.062,
      "http_attempted": true,
      "input_question": "new super mario bros. u deluxe เล่นได้ที่โซนไหน",
      "legacy_contrast": {
        "domain": "games",
        "operation": "availability",
        "needs": [
          "check_availability"
        ],
        "reason": "known game alias found; named game location/availability terms found"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false
  },
  "need_results": [
    {
      "need_id": "r114_n1",
      "task": "game_detail",
      "category": "C04",
      "source_span": "new super mario bros. u deluxe เล่นได้ที่โซนไหน",
      "execution_query": "new super mario bros. u deluxe เล่นได้ที่โซนไหน ",
      "status": "partial_supported",
      "reason_codes": [
        "known_services_zone_relation_unconfirmed"
      ],
      "receipts": [
        {
          "record_id": "game_detail_new_super_mario_bros",
          "field": "studio_services",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_dd5c64fb15c50936c875483f60a8"
            },
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_537f6eabb2fac0d78d3e28dadba9"
            }
          ]
        }
      ],
      "claim_packets": [
        {
          "fact_id": "C04:game_detail_new_super_mario_bros:studio_services",
          "record_id": "game_detail_new_super_mario_bros",
          "facet": "studio_services",
          "value": "Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons)",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_dd5c64fb15c50936c875483f60a8"
            },
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_537f6eabb2fac0d78d3e28dadba9"
            }
          ],
          "fixture": false,
          "status": "answer"
        }
      ],
      "semantic_correctness_verified": false
    }
  ],
  "sources": [],
  "positive_contracts": [
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
      "row": 2395,
      "variant": "question",
      "id": "MASTER-GT-TH-02396",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']",
        "missing all alternatives: ['Nintendo Switch Zone']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ],
        "content_or_format": [
          "missing all alternatives: ['Nintendo Switch Zone']"
        ]
      },
      "positive_literal": true,
      "literal_passed": false,
      "literal_errors": [
        "missing all alternatives: ['Nintendo Switch Zone']"
      ]
    },
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
      "row": 2395,
      "variant": "question",
      "id": "MASTER-GT-TH-02396",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']",
        "missing all alternatives: ['Nintendo Switch Zone']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ],
        "content_or_format": [
          "missing all alternatives: ['Nintendo Switch Zone']"
        ]
      },
      "positive_literal": true,
      "literal_passed": false,
      "literal_errors": [
        "missing all alternatives: ['Nintendo Switch Zone']"
      ]
    },
    {
      "file": "data/eval/master_ground_truth_th_5000_v1.jsonl",
      "row": 2395,
      "variant": "question",
      "id": "MASTER-GT-TH-02396",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']",
        "missing all alternatives: ['Nintendo Switch Zone']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ],
        "content_or_format": [
          "missing all alternatives: ['Nintendo Switch Zone']"
        ]
      },
      "positive_literal": true,
      "literal_passed": false,
      "literal_errors": [
        "missing all alternatives: ['Nintendo Switch Zone']"
      ]
    },
    {
      "file": "data/eval/master_ground_truth_th_5000_v2.jsonl",
      "row": 2395,
      "variant": "question",
      "id": "MASTER-GT-TH-02396",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']",
        "missing all alternatives: ['Nintendo Switch Zone']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ],
        "content_or_format": [
          "missing all alternatives: ['Nintendo Switch Zone']"
        ]
      },
      "positive_literal": true,
      "literal_passed": false,
      "literal_errors": [
        "missing all alternatives: ['Nintendo Switch Zone']"
      ]
    }
  ]
}
```

## 15. ขอข้อมูลเรื่องวันศุกร์ maintenance

Key: `2204b0a8c1dcc11cbd923870f71f83a322743817cf363f87ab147b4a1ed481c8`; locale `th`; original domain `reservation_policy`

### R115 saved

```text
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
ศุกร์ — ช่วงบำรุงรักษา: 13:00–16:00 [S1]
```

### R117 revision03 saved

```text
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
ศุกร์ — ช่วงบำรุงรักษา: 13:00–16:00 [S1]
```

### R118 revision02

```text
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
ศุกร์ — ช่วงบำรุงรักษา: 13:00–16:00 [S1]
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "validated_interpretation_proposal",
    "tasks": [
      {
        "quote": "ขอข้อมูลเรื่องวันศุกร์ maintenance",
        "domain": "schedule",
        "category": "C11",
        "operation": "schedule_lookup",
        "facet": "maintenance_periods",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "59ff3eaa07634578a7b66b72048ad4c8",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"ขอข้อมูลเรื่องวันศุกร์ maintenance\", \"operation\": \"schedule_lookup\", \"domain\": \"schedule\", \"facet\": \"maintenance_periods\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 1.687,
      "http_attempted": true,
      "input_question": "ขอข้อมูลเรื่องวันศุกร์ maintenance",
      "legacy_contrast": {
        "domain": "general",
        "operation": "unknown",
        "needs": [],
        "reason": "domain_terms=2; no clear operation terms"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false
  },
  "need_results": [
    {
      "need_id": "r114_n1",
      "task": "schedule",
      "category": "C11",
      "source_span": "ขอข้อมูลเรื่องวันศุกร์ maintenance",
      "execution_query": "ขอข้อมูลเรื่องวันศุกร์ maintenance ",
      "status": "supported",
      "reason_codes": [
        "interpreted_recorded_calendar_facet"
      ],
      "receipts": [
        {
          "record_id": "migrated_schedule_4",
          "field": "maintenance_periods",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/maintenance_periods",
              "source_id": "r66_8b8799fa0b0f242ce50dede11782"
            }
          ]
        }
      ],
      "claim_packets": [
        {
          "fact_id": "C11:migrated_schedule_4:maintenance_periods",
          "record_id": "migrated_schedule_4",
          "facet": "maintenance_periods",
          "value": "13:00–16:00",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/maintenance_periods",
              "source_id": "r66_8b8799fa0b0f242ce50dede11782"
            }
          ],
          "fixture": false,
          "status": "answer"
        }
      ],
      "semantic_correctness_verified": false
    }
  ],
  "sources": [],
  "positive_contracts": []
}
```

## 16. ขอสอบถามหน่อยครับ ขอข้อมูลที่ยืนยันได้หน่อยครับ: pc2 available ตอน 3pm ไหม

Key: `2c110689509d6996841eec18c40041b694e32f32454d3bb7453a15507e5c4ba7`; locale `th`; original domain `reservation_policy`

### R115 saved

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### R117 revision03 saved

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### R118 revision02

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "independent_context_frame",
    "tasks": [
      {
        "quote": "ขอข้อมูลที่ยืนยันได้หน่อยครับ: pc2 available ตอน 3pm ไหม",
        "domain": "live",
        "category": "C12",
        "operation": "availability",
        "facet": "live_status",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "45b378177db4427592cc3edfe9deddac",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": false,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"pc2 available ตอน 3pm ไหม\", \"operation\": \"availability\", \"domain\": \"games\", \"facet\": \"live_status\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}, {\"quote\": \"ขอข้อมูลที่ยืนยันได้หน่อยครับ\", \"operation\": \"general_answer\", \"domain\": \"general\", \"facet\": \"\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "meaning_review": {
        "basis": "dated_named_resource_availability",
        "model_plan_accepted": false,
        "model_reason": "facet_domain_mismatch",
        "prior_tasks": [],
        "business_facts_added": false
      },
      "reason": "independent_context_frame",
      "elapsed_sec": 2.875,
      "http_attempted": true,
      "input_question": "ขอข้อมูลที่ยืนยันได้หน่อยครับ: pc2 available ตอน 3pm ไหม",
      "legacy_contrast": {
        "domain": "general",
        "operation": "unknown",
        "needs": [],
        "reason": "domain_terms=2; no clear operation terms"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false
  },
  "need_results": [
    {
      "need_id": "r114_n1",
      "task": "live_status",
      "category": "C12",
      "source_span": "ขอข้อมูลที่ยืนยันได้หน่อยครับ: pc2 available ตอน 3pm ไหม",
      "execution_query": "ขอข้อมูลที่ยืนยันได้หน่อยครับ: pc2 available ตอน 3pm ไหม ",
      "status": "temporary_failure",
      "reason_codes": [
        "live_binding_or_provider_not_confirmed"
      ],
      "receipts": [],
      "claim_packets": [],
      "semantic_correctness_verified": false
    }
  ],
  "sources": [],
  "positive_contracts": []
}
```

## 17. What position does Ms. Kamlawan Nuansai hold

Key: `2ee7827caaaac21d3837cb4dd86c4e955dd51f018520dfc6f024a287bc9dd91e`; locale `en`; original domain `members_overview_contact`

### R115 saved

```text
**Relevant information**
• Confirmed information: In cases where a user commits serious rule violations or repeatedly violates the rules, such as damaging property or engaging in behavior that poses a threat to others' safety, the user may have their account privileges permanently suspended. [S1]
• topic: penalty [S2]

English translation is machine generated and has not been reviewed by the owner.
```

### R117 revision03 saved

```text
No confirmed source is available for the requested detail.
```

### R118 revision02

```text
No confirmed source is available for the requested detail.
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "validated_interpretation_proposal",
    "tasks": [
      {
        "quote": "what position does ms. kamlawan nuansai hold",
        "domain": "members",
        "category": "C02",
        "operation": "role_lookup",
        "facet": "role",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "17cd7a8420f644978d85b9a52688a324",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"what position does ms. kamlawan nuansai hold\", \"operation\": \"role_lookup\", \"domain\": \"members\", \"facet\": \"role\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 1.468,
      "http_attempted": true,
      "input_question": "what position does ms. kamlawan nuansai hold",
      "legacy_contrast": {
        "domain": "general",
        "operation": "role_lookup",
        "needs": [
          "lookup_people_by_role"
        ],
        "reason": "domain_terms=2; role/position lookup terms found"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false
  },
  "need_results": [
    {
      "need_id": "r114_n1",
      "task": "personnel",
      "category": "C02",
      "source_span": "what position does ms. kamlawan nuansai hold",
      "execution_query": "what position does ms. kamlawan nuansai hold ",
      "status": "missing_source",
      "reason_codes": [
        "entity_not_bound"
      ],
      "receipts": [],
      "claim_packets": [],
      "semantic_correctness_verified": false
    }
  ],
  "sources": [],
  "positive_contracts": []
}
```

## 18. ขอสอบถมหนาอยครับ ศูนย์อยู่ที่ไหน อะ

Key: `3020765f9449c4044241f3945cf7241a89f090e4742bdab7592f7504bc36f074`; locale `th`; original domain `members_overview_contact`

### R115 saved

```text
PSU Esports Studio - Phuket — ที่อยู่: ศูนย์อยู่ที่อาคาร 5 ชั้น 1 มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต 80 หมู่ 1 ถ.วิชิตสงคราม อ.กะทู้ จ.ภูเก็ต 83120ครับ [S1]
ที่จอดรถ — ที่ตั้ง: หน้าตึก 5 [S2]
ที่นั่งพัก — ที่ตั้ง: โซนกลางห้อง [S3]
```

### R117 revision03 saved

```text
**PSU Esports Studio - Phuket**
• ที่อยู่เต็ม: ศูนย์อยู่ที่อาคาร 5 ชั้น 1 มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต 80 หมู่ 1 ถ.วิชิตสงคราม อ.กะทู้ จ.ภูเก็ต 83120ครับ [S1]
```

### R118 revision02

```text
**PSU Esports Studio - Phuket**
• ที่อยู่เต็ม: ศูนย์อยู่ที่อาคาร 5 ชั้น 1 มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต 80 หมู่ 1 ถ.วิชิตสงคราม อ.กะทู้ จ.ภูเก็ต 83120ครับ [S1]
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "validated_interpretation_proposal",
    "tasks": [
      {
        "quote": "ขอสอบถมหนาอยครับ ศูนย์อยู่ที่ไหน อะ",
        "domain": "general",
        "category": null,
        "operation": "unknown",
        "facet": "",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "984c5f9df5484ea39bf8c737caf02116",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"ขอสอบถมหนาอยครับ ศูนย์อยู่ที่ไหน อะ\", \"operation\": \"unknown\", \"domain\": \"general\", \"facet\": \"\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 1.718,
      "http_attempted": true,
      "input_question": "ขอสอบถมหนาอยครับ ศูนย์อยู่ที่ไหน อะ",
      "legacy_contrast": {
        "domain": "general",
        "operation": "unknown",
        "needs": [],
        "reason": "domain_terms=2; no clear operation terms"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false,
    "execution_path": "compatibility_fallback"
  },
  "need_results": [
    {
      "need_id": "n1",
      "task": "center_location",
      "predicate": "center_location",
      "source_span": "ขอสอบถมหนาอยครับ ศูนย์อยู่ที่ไหน อะ",
      "status": "supported",
      "reason_codes": [],
      "slots": {},
      "record_ids": [
        "center_psu_phuket"
      ],
      "receipts": [
        {
          "need_id": "n1",
          "record_id": "center_psu_phuket",
          "field": "address",
          "predicate": "center_location",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/address",
              "source_id": "r66_address_ed6b784142adf13e126a13a3"
            }
          ],
          "release_id": "migration-preview-r69",
          "revision": 3,
          "validity": {
            "effective_from": null,
            "effective_until": null,
            "state": "unknown"
          },
          "claim_entailment_verified": false,
          "predicate_contract_checked": true
        }
      ],
      "coverage": {
        "version": 1,
        "predicate": "center_location",
        "task": "center_location",
        "decision": "contract_supported",
        "reason_codes": [],
        "receipts": [
          {
            "need_id": "n1",
            "record_id": "center_psu_phuket",
            "field": "address",
            "predicate": "center_location",
            "evidence_refs": [
              {
                "locator": "/mapped_fields/address",
                "source_id": "r66_address_ed6b784142adf13e126a13a3"
              }
            ],
            "release_id": "migration-preview-r69",
            "revision": 3,
            "validity": {
              "effective_from": null,
              "effective_until": null,
              "state": "unknown"
            },
            "claim_entailment_verified": false,
            "predicate_contract_checked": true
          }
        ],
        "semantic_correctness_verified": false
      },
      "coverage_basis": "typed predicate contract where available; unmigrated scope remains unverified",
      "read_graph": {
        "graph": {
          "op": "all_of",
          "children": [
            {
              "op": "all_of",
              "children": [
                {
                  "op": "any_of",
                  "children": [
                    {
                      "op": "all_of",
                      "children": [
                        {
                          "op": "field",
                          "children": [],
                          "record_id": "center_psu_phuket",
                          "key": "address",
                          "reason": ""
                        }
                      ],
                      "record_id": "",
                      "key": "",
                      "reason": ""
                    },
                    {
                      "op": "all_of",
                      "children": [
                        {
                          "op": "field",
                          "children": [],
                          "record_id": "center_psu_phuket",
                          "key": "building",
                          "reason": ""
                        },
                        {
                          "op": "field",
                          "children": [],
                          "record_id": "center_psu_phuket",
                          "key": "floor",
                          "reason": ""
                        }
                      ],
                      "record_id": "",
                      "key": "",
                      "reason": ""
                    },
                    {
                      "op": "all_of",
                      "children": [
                        {
                          "op": "field",
                          "children": [],
                          "record_id": "center_psu_phuket",
                          "key": "map_url",
                          "reason": ""
                        }
                      ],
                      "record_id": "",
                      "key": "",
                      "reason": ""
                    }
                  ],
                  "record_id": "",
                  "key": "",
                  "reason": ""
                }
              ],
              "record_id": "",
              "key": "",
              "reason": ""
            }
          ],
          "record_id": "",
          "key": "",
          "reason": ""
        },
        "targets": [
          "center_psu_phuket"
        ],
        "relation_paths": [],
        "evaluation": {
          "status": "supported",
          "receipts": [
            {
              "need_id": "n1",
              "subject": "center_psu_phuket",
              "record_id": "center_psu_phuket",
              "predicate": "center_location",
              "field": "address",
              "value": {
                "en": "Building 5, 1st floor, Prince of Songkla University, Phuket Campus, 80 Moo 1 Wichit Songkhram Road, Kathu, Phuket 83120.",
                "th": "ศูนย์อยู่ที่อาคาร 5 ชั้น 1 มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต 80 หมู่ 1 ถ.วิชิตสงคราม อ.กะทู้ จ.ภูเก็ต 83120ครับ"
              },
              "revision": 3,
              "units": null,
              "applicability": {
                "effective_from": null,
                "effective_until": null,
                "state": "unknown"
              },
              "release_id": "migration-preview-r69",
              "epoch": 2093,
              "evidence_refs": [
                {
                  "locator": "/mapped_fields/address",
                  "source_id": "r66_address_ed6b784142adf13e126a13a3"
                }
              ],
              "sources": [
                {
                  "source_id": "r66_address_ed6b784142adf13e126a13a3",
                  "sha256": "ed6b784142adf13e126a13a3e030a39f8d5cdc3f84c150a3637f174e121e6d45",
                  "authority_for": [
                    "center"
                  ],
                  "locator": "/mapped_fields/address"
                }
              ],
              "verification": "typed_value_and_relation",
              "prose_entailment_verified": false
            }
          ]
        },
        "required_claims_delivered": true
      },
      "claim_packets": [
        {
          "need_id": "n1",
          "subject": "center_psu_phuket",
          "record_id": "center_psu_phuket",
          "predicate": "center_location",
          "field": "address",
          "value": {
            "en": "Building 5, 1st floor, Prince of Songkla University, Phuket Campus, 80 Moo 1 Wichit Songkhram Road, Kathu, Phuket 83120.",
            "th": "ศูนย์อยู่ที่อาคาร 5 ชั้น 1 มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต 80 หมู่ 1 ถ.วิชิตสงคราม อ.กะทู้ จ.ภูเก็ต 83120ครับ"
          },
          "revision": 3,
          "units": null,
          "applicability": {
            "effective_from": null,
            "effective_until": null,
            "state": "unknown"
          },
          "release_id": "migration-preview-r69",
          "epoch": 2093,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/address",
              "source_id": "r66_address_ed6b784142adf13e126a13a3"
            }
          ],
          "sources": [
            {
              "source_id": "r66_address_ed6b784142adf13e126a13a3",
              "sha256": "ed6b784142adf13e126a13a3e030a39f8d5cdc3f84c150a3637f174e121e6d45",
              "authority_for": [
                "center"
              ],
              "locator": "/mapped_fields/address"
            }
          ],
          "verification": "typed_value_and_relation",
          "prose_entailment_verified": false
        }
      ]
    }
  ],
  "sources": [],
  "positive_contracts": []
}
```

## 19. กำลังวางแผนไปใช้บริการ เลยอยากทราบว่า ต้องการจองเครื่องทำยังไง อะ

Key: `36c239903ef9b2645e840586a9db999016c64405aefcfc4914ba3d20f2ecdcdf`; locale `th`; original domain `reservation_policy`

### R115 saved

```text
**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: ขั้นตอนการจองคือ เลือกบริการที่ต้องการ เลือกวันและเวลา กรอกข้อมูลผู้ใช้บริการ ตรวจสอบข้อมูล ชำระเงินโดยโอนเข้าบัญชีธนาคาร และแนบสลิปการโอนเงิน [S1]
```

### R117 revision03 saved

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### R118 revision02

```text
ขั้นตอนการจอง — คำตอบที่ยืนยัน: ขั้นตอนการจองคือ เลือกบริการที่ต้องการ เลือกวันและเวลา กรอกข้อมูลผู้ใช้บริการ ตรวจสอบข้อมูล ชำระเงินโดยโอนเข้าบัญชีธนาคาร และแนบสลิปการโอนเงิน [S1]
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "independent_context_frame",
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
    "event": {
      "id": "9ab369f246074a4bb0a86e2811c362ff",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"ต้องการจองเครื่องทำยังไง อะ\", \"operation\": \"how_to\", \"domain\": \"reservation\", \"facet\": \"owner_policy\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "meaning_review": {
        "basis": "booking_action_before_game_context",
        "model_plan_accepted": true,
        "model_reason": "validated_interpretation_proposal",
        "prior_tasks": [
          {
            "quote": "ต้องการจองเครื่องทำยังไง อะ",
            "domain": "reservation",
            "category": "C08",
            "operation": "how_to",
            "facet": "owner_policy",
            "target": "",
            "constraints": [],
            "ambiguous": false
          }
        ],
        "business_facts_added": false
      },
      "reason": "independent_context_frame",
      "elapsed_sec": 1.907,
      "http_attempted": true,
      "input_question": "กำลังวางแผนไปใช้บริการ เลยอยากทราบว่า ต้องการจองเครื่องทำยังไง อะ",
      "legacy_contrast": {
        "domain": "equipment",
        "operation": "how_to",
        "needs": [
          "steps",
          "controls_if_game"
        ],
        "reason": "domain_terms=2; how-to terms found"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false
  },
  "need_results": [
    {
      "need_id": "r114_n1",
      "task": "procedure",
      "category": "C08",
      "source_span": "กำลังวางแผนไปใช้บริการ เลยอยากทราบว่า ต้องการจองเครื่องทำยังไง อะ",
      "execution_query": "กำลังวางแผนไปใช้บริการ เลยอยากทราบว่า ต้องการจองเครื่องทำยังไง อะ ",
      "status": "supported",
      "reason_codes": [
        "bounded_model_selection"
      ],
      "receipts": [
        {
          "record_id": "migrated_faq_curated_booking_steps",
          "field": "answer",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/answer",
              "source_id": "r66_en_240dd7619c2cdce6429ad607"
            }
          ]
        }
      ],
      "claim_packets": [
        {
          "fact_id": "C08:migrated_faq_curated_booking_steps:owner_policy",
          "record_id": "migrated_faq_curated_booking_steps",
          "facet": "owner_policy",
          "value": "ขั้นตอนการจองคือ เลือกบริการที่ต้องการ เลือกวันและเวลา กรอกข้อมูลผู้ใช้บริการ ตรวจสอบข้อมูล ชำระเงินโดยโอนเข้าบัญชีธนาคาร และแนบสลิปการโอนเงิน",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/answer",
              "source_id": "r66_en_240dd7619c2cdce6429ad607"
            }
          ],
          "fixture": false,
          "status": "answer"
        }
      ],
      "semantic_correctness_verified": false
    }
  ],
  "sources": [],
  "positive_contracts": []
}
```

## 20. กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า VALORANT คือเกมอะไร

Key: `3a769b080c6e4d2fac6862c843d20940c534c0633656de70c192903617523146`; locale `th`; original domain `game_detail`

### R115 saved

```text
VALORANT — คำอธิบายเกม: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ [S1]
```

### R117 revision03 saved

```text
VALORANT — คำอธิบายเกม: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ [S1]
```

### R118 revision02

```text
VALORANT — คำอธิบายเกม: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ [S1]
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "independent_context_frame",
    "tasks": [
      {
        "quote": "กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า valorant คือเกมอะไร",
        "domain": "games",
        "category": "C04",
        "operation": "detail",
        "facet": "summary",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "76b65f66694945dda3ad90667ee6f55d",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า valorant คือเกมอะไร\", \"operation\": \"unknown\", \"domain\": \"games\", \"facet\": \"game_catalog\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "meaning_review": {
        "basis": "current_game_and_definition_request",
        "model_plan_accepted": true,
        "model_reason": "validated_interpretation_proposal",
        "prior_tasks": [
          {
            "quote": "กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า valorant คือเกมอะไร",
            "domain": "games",
            "category": "C04",
            "operation": "unknown",
            "facet": "game_catalog",
            "target": "",
            "constraints": [],
            "ambiguous": false
          }
        ],
        "business_facts_added": false
      },
      "reason": "independent_context_frame",
      "elapsed_sec": 7.343,
      "http_attempted": true,
      "input_question": "กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า valorant คือเกมอะไร",
      "legacy_contrast": {
        "domain": "games",
        "operation": "unknown",
        "needs": [],
        "reason": "game catalog/count terms override zone/equipment domain; no clear operation terms"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false
  },
  "need_results": [
    {
      "need_id": "r114_n1",
      "task": "game_detail",
      "category": "C04",
      "source_span": "กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า valorant คือเกมอะไร",
      "execution_query": "กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า valorant คือเกมอะไร ",
      "status": "supported",
      "reason_codes": [
        "meaning_bound_requested_field"
      ],
      "receipts": [
        {
          "record_id": "game_detail_valorant",
          "field": "summary",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/summary",
              "source_id": "r66_en_05d488ac2703e7c94962ca36"
            }
          ]
        }
      ],
      "claim_packets": [
        {
          "fact_id": "C04:game_detail_valorant:summary",
          "record_id": "game_detail_valorant",
          "facet": "summary",
          "value": "VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/summary",
              "source_id": "r66_en_05d488ac2703e7c94962ca36"
            }
          ],
          "fixture": false,
          "status": "answer"
        }
      ],
      "semantic_correctness_verified": false
    }
  ],
  "sources": [],
  "positive_contracts": []
}
```

## 21. What does the Shift + Q / W / E / R button do in League of Legends on PC

Key: `3cc3c5c383b501e1e992101d842e35427a03a448b4211f41cb66a48820b267ea`; locale `en`; original domain `game_controls`

### R115 saved

```text
League of Legends / PC — Quick cast abilities: Shift + Q / W / E / R — Default value referenced as Shift+Q/W/E/R for quick cast [S1]
```

### R117 revision03 saved

```text
League of Legends / PC — Quick cast abilities: Shift + Q / W / E / R — Default value referenced as Shift+Q/W/E/R for quick cast [S1]
```

### R118 revision02

```text
League of Legends / PC — Quick cast abilities: Shift + Q / W / E / R — Default value referenced as Shift+Q/W/E/R for quick cast [S1]
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "independent_context_frame",
    "tasks": [
      {
        "quote": "what does the shift + q / w / e / r button do in league of legends on pc",
        "domain": "game_controls",
        "category": "C05",
        "operation": "control",
        "facet": "input_bindings",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "fda9c406289845f8a02094029e627335",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"what does the shift + q / w / e / r button do in league of legends on pc\", \"operation\": \"detail\", \"domain\": \"games\", \"facet\": \"how_to_play\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "meaning_review": {
        "basis": "legacy_control_frame_and_current_source_target",
        "model_plan_accepted": true,
        "model_reason": "validated_interpretation_proposal",
        "prior_tasks": [
          {
            "quote": "what does the shift + q / w / e / r button do in league of legends on pc",
            "domain": "games",
            "category": "C04",
            "operation": "detail",
            "facet": "how_to_play",
            "target": "",
            "constraints": [],
            "ambiguous": false
          }
        ],
        "business_facts_added": false
      },
      "reason": "independent_context_frame",
      "elapsed_sec": 1.609,
      "http_attempted": true,
      "input_question": "what does the shift + q / w / e / r button do in league of legends on pc",
      "legacy_contrast": {
        "domain": "games",
        "operation": "detail",
        "needs": [
          "summarize_detail",
          "check_availability"
        ],
        "reason": "known game alias found; known game title keeps games domain; no clear operation terms; bare known game title treated as detail"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false
  },
  "need_results": [
    {
      "need_id": "r114_n1",
      "task": "game_controls",
      "category": "C05",
      "source_span": "what does the shift + q / w / e / r button do in league of legends on pc",
      "execution_query": "what does the shift + q / w / e / r button do in league of legends on pc ",
      "status": "supported",
      "reason_codes": [
        "exact_button_reverse_lookup"
      ],
      "receipts": [
        {
          "record_id": "controls_pc_league_of_legends",
          "field": "binding_2",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_e85b960aad7818c3b1488e70"
            }
          ]
        }
      ],
      "claim_packets": [
        {
          "fact_id": "C05:controls_pc_league_of_legends:binding_2",
          "record_id": "controls_pc_league_of_legends",
          "facet": "binding_2",
          "value": "Shift + Q / W / E / R — Default value referenced as Shift+Q/W/E/R for quick cast",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_e85b960aad7818c3b1488e70"
            }
          ],
          "fixture": false,
          "status": "answer"
        }
      ],
      "semantic_correctness_verified": false
    }
  ],
  "sources": [],
  "positive_contracts": [
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
      "row": 7765,
      "variant": "question",
      "id": "MASTER-GT-EN-02766",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
      "row": 7765,
      "variant": "question",
      "id": "MASTER-GT-EN-02766",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_en_5000_v1.jsonl",
      "row": 2765,
      "variant": "question",
      "id": "MASTER-GT-EN-02766",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_en_5000_v2.jsonl",
      "row": 2765,
      "variant": "question",
      "id": "MASTER-GT-EN-02766",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    }
  ]
}
```

## 22. Please answer from verified studio information: Which zone has the Gaming Chair

Key: `3df1eea3e83aa3fb059025c57f1a6063ac223379a543d818ffc26146c42c59ae`; locale `en`; original domain `equipment`

### R115 saved

```text
Gaming Chair — location: PC Zone [S1]
```

### R117 revision03 saved

```text
Gaming Chair — location: PC Zone [S1]
```

### R118 revision02

```text
Gaming Chair — location: PC Zone [S1]
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "validated_interpretation_proposal",
    "tasks": [
      {
        "quote": "which zone has the gaming chair",
        "domain": "equipment",
        "category": "C03",
        "operation": "unknown",
        "facet": "location",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "63148052763d4c4ba5aa80c9b166bb66",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"which zone has the gaming chair\", \"operation\": \"unknown\", \"domain\": \"equipment\", \"facet\": \"location\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 1.407,
      "http_attempted": true,
      "input_question": "which zone has the gaming chair",
      "legacy_contrast": {
        "domain": "equipment",
        "operation": "unknown",
        "needs": [],
        "reason": "known equipment item alias found; no clear operation terms"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false
  },
  "need_results": [
    {
      "need_id": "r114_n1",
      "task": "equipment",
      "category": "C03",
      "source_span": "which zone has the gaming chair",
      "execution_query": "which zone has the gaming chair ",
      "status": "supported",
      "reason_codes": [
        "meaning_bound_requested_field"
      ],
      "receipts": [
        {
          "record_id": "equipment_gaming_chair",
          "field": "location",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/specifications",
              "source_id": "r63_fc7d8dd97058c5a18e121b2de918"
            }
          ]
        }
      ],
      "claim_packets": [
        {
          "fact_id": "C03:equipment_gaming_chair:location",
          "record_id": "equipment_gaming_chair",
          "facet": "location",
          "value": "PC Zone",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/specifications",
              "source_id": "r63_fc7d8dd97058c5a18e121b2de918"
            }
          ],
          "fixture": false,
          "status": "answer"
        }
      ],
      "semantic_correctness_verified": false
    }
  ],
  "sources": [],
  "positive_contracts": [
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
      "row": 8635,
      "variant": "question",
      "id": "MASTER-GT-EN-03636",
      "passed": false,
      "failures": [
        "route:knowledge expected:['equipment']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['equipment']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
      "row": 8635,
      "variant": "question",
      "id": "MASTER-GT-EN-03636",
      "passed": false,
      "failures": [
        "route:knowledge expected:['equipment']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['equipment']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_en_5000_v1.jsonl",
      "row": 3635,
      "variant": "question",
      "id": "MASTER-GT-EN-03636",
      "passed": false,
      "failures": [
        "route:knowledge expected:['equipment']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['equipment']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_en_5000_v2.jsonl",
      "row": 3635,
      "variant": "question",
      "id": "MASTER-GT-EN-03636",
      "passed": false,
      "failures": [
        "route:knowledge expected:['equipment']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['equipment']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    }
  ]
}
```

## 23. I am preparing for a AOV match. What is the policy for competition equipment and devices

Key: `4b0fb4a4344134b1f575032bdf52be169e19f555edfefbda347310760b6c859d`; locale `en`; original domain `competition_rules`

### R115 saved

```text
Please specify the item and requested time.
```

### R117 revision03 saved

```text
Please specify the item and requested time.
```

### R118 revision02

```text
Please specify the tournament or rulebook edition so I can match the rule you are asking about.
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "validated_interpretation_proposal",
    "tasks": [
      {
        "quote": "i am preparing for a aov match. what is the policy for competition equipment and devices",
        "domain": "competition_rules",
        "category": "C13",
        "operation": "rule_lookup",
        "facet": "rule_clause",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "4b723ac8feef4fde928111ee80f8495f",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"i am preparing for a aov match. what is the policy for competition equipment and devices\", \"operation\": \"rule_lookup\", \"domain\": \"competition_rules\", \"facet\": \"rule_clause\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 1.656,
      "http_attempted": true,
      "input_question": "i am preparing for a aov match. what is the policy for competition equipment and devices",
      "legacy_contrast": {
        "domain": "general",
        "operation": "unknown",
        "needs": [],
        "reason": "domain_terms=2; no clear operation terms"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false
  },
  "need_results": [
    {
      "need_id": "r114_n1",
      "task": "competition_rules",
      "category": "C13",
      "source_span": "i am preparing for a aov match. what is the policy for competition equipment and devices",
      "execution_query": "i am preparing for a aov match. what is the policy for competition equipment and devices ",
      "status": "needs_user_slot",
      "reason_codes": [
        "event_or_rule_not_bound"
      ],
      "receipts": [],
      "claim_packets": [],
      "semantic_correctness_verified": false
    }
  ],
  "sources": [],
  "positive_contracts": []
}
```

## 24. How much does Beat Saber cost

Key: `546c449056ffc350efa88ef0bd5a4b8957fd870fc8d94a2b77700032f0c79ae9`; locale `en`; original domain `service_fee`

### R115 saved

```text
Rates last reaffirmed by the owner on 2026-10-20; no new effective interval was established.
VR Station 30 นาที / PSU Student and Staff — per-person price for the rate duration: 0 THB per person for 30 minutes [S1]
VR Station 30 นาที / PSU Alumni and General Student — per-person price for the rate duration: 190 THB per person for 30 minutes [S2]
VR Station 30 นาที / General Adult — per-person price for the rate duration: 525 THB per person for 30 minutes [S3]
VR Station 1 ชั่วโมง / PSU Student and Staff — per-person price for the rate duration: 0 THB per person for 60 minutes [S4]
VR Station 1 ชั่วโมง / PSU Alumni and General Student — per-person price for the rate duration: 375 THB per person for 60 minutes [S5]
VR Station 1 ชั่วโมง / General Adult — per-person price for the rate duration: 1050 THB per person for 60 minutes [S6]
```

### R117 revision03 saved

```text
No confirmed source is available for the requested detail.
```

### R118 revision02

```text
No confirmed source is available for the requested detail.
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "validated_interpretation_proposal",
    "tasks": [
      {
        "quote": "how much does beat saber cost",
        "domain": "games",
        "category": "C04",
        "operation": "detail",
        "facet": "game_catalog",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "44a664c160bc4ee393d8652d384fc048",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"how much does beat saber cost\", \"operation\": \"detail\", \"domain\": \"games\", \"facet\": \"game_catalog\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 1.672,
      "http_attempted": true,
      "input_question": "how much does beat saber cost",
      "legacy_contrast": {
        "domain": "games",
        "operation": "detail",
        "needs": [
          "summarize_detail",
          "check_availability"
        ],
        "reason": "known game alias found; known game title keeps games domain; no clear operation terms; bare known game title treated as detail"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false
  },
  "need_results": [
    {
      "need_id": "r114_n1",
      "task": "game_detail",
      "category": "C04",
      "source_span": "how much does beat saber cost",
      "execution_query": "how much does beat saber cost ",
      "status": "missing_source",
      "reason_codes": [
        "bounded_model_selection"
      ],
      "receipts": [],
      "claim_packets": [],
      "semantic_correctness_verified": false
    }
  ],
  "sources": [],
  "positive_contracts": []
}
```

## 25. Can I play Beat Saber in the VR Zone? Please answer briefly

Key: `5b2d0e1344332824fb7bb1565e2eb07efde375061314bb3e784fd9becd7abc28`; locale `en`; original domain `games_catalog_availability`

### R115 saved

```text
Beat Saber — studio services offering this game: VR Station 30 นาที; VR Station 1 ชั่วโมง [S1]
```

### R117 revision03 saved

```text
The zone relation is not confirmed; the following studio services are confirmed to offer this game.
Beat Saber — studio services offering this game: VR Station 30 นาที; VR Station 1 ชั่วโมง [S1]
```

### R118 revision02

```text
The zone relation is not confirmed; the following studio services are confirmed to offer this game.
Beat Saber — studio services offering this game: VR Station 30 นาที; VR Station 1 ชั่วโมง [S1]
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "validated_interpretation_proposal",
    "tasks": [
      {
        "quote": "can i play beat saber in the vr zone?",
        "domain": "games",
        "category": "C04",
        "operation": "detail",
        "facet": "zone",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "afac36ff2451400ca27597d6533ffa15",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"can i play beat saber in the vr zone?\", \"operation\": \"detail\", \"domain\": \"games\", \"facet\": \"zone\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 7.203,
      "http_attempted": true,
      "input_question": "can i play beat saber in the vr zone? please answer briefly",
      "legacy_contrast": {
        "domain": "games",
        "operation": "detail",
        "needs": [
          "summarize_detail",
          "check_availability"
        ],
        "reason": "known game alias found; known game title keeps games domain; no clear operation terms; bare known game title treated as detail"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false
  },
  "need_results": [
    {
      "need_id": "r114_n1",
      "task": "game_detail",
      "category": "C04",
      "source_span": "can i play beat saber in the vr zone?",
      "execution_query": "can i play beat saber in the vr zone? ",
      "status": "partial_supported",
      "reason_codes": [
        "known_services_zone_relation_unconfirmed"
      ],
      "receipts": [
        {
          "record_id": "game_detail_beat_saber",
          "field": "studio_services",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_c8765a7c73171b778d07fa723e2e"
            },
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_bdf32eeefd4cdf08374b22602f8c"
            }
          ]
        }
      ],
      "claim_packets": [
        {
          "fact_id": "C04:game_detail_beat_saber:studio_services",
          "record_id": "game_detail_beat_saber",
          "facet": "studio_services",
          "value": "VR Station 30 นาที; VR Station 1 ชั่วโมง",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_c8765a7c73171b778d07fa723e2e"
            },
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_bdf32eeefd4cdf08374b22602f8c"
            }
          ],
          "fixture": false,
          "status": "answer"
        }
      ],
      "semantic_correctness_verified": false
    }
  ],
  "sources": [],
  "positive_contracts": [
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
      "row": 6635,
      "variant": "question",
      "id": "MASTER-GT-EN-01636",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
      "row": 6635,
      "variant": "question",
      "id": "MASTER-GT-EN-01636",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_en_5000_v1.jsonl",
      "row": 1635,
      "variant": "question",
      "id": "MASTER-GT-EN-01636",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_en_5000_v2.jsonl",
      "row": 1635,
      "variant": "question",
      "id": "MASTER-GT-EN-01636",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    }
  ]
}
```

## 26. ช่วยตอบจากข้อมูลที่ยืนยันได้หน่อย: ตอนนี้ศูนย์เปิดมั้ย

Key: `69812416b4c4bda6fc2c08556eabfa8117b4ec25eb72a7ebe7eeec11deac4d58`; locale `th`; original domain `schedule_calendar`

### R115 saved

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### R117 revision03 saved

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### R118 revision02

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "validated_interpretation_proposal",
    "tasks": [
      {
        "quote": "ตอนนี้ศูนย์เปิดมั้ย",
        "domain": "schedule",
        "category": "C11",
        "operation": "schedule_lookup",
        "facet": "open_periods",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "6ae5c59dc688486aa751f75d7cdd21e3",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"ตอนนี้ศูนย์เปิดมั้ย\", \"operation\": \"schedule_lookup\", \"domain\": \"schedule\", \"facet\": \"open_periods\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 1.5,
      "http_attempted": true,
      "input_question": "ตอนนี้ศูนย์เปิดมั้ย",
      "legacy_contrast": {
        "domain": "schedule",
        "operation": "schedule_lookup",
        "needs": [
          "lookup_schedule"
        ],
        "reason": "domain_terms=2; schedule terms found"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false
  },
  "need_results": [
    {
      "need_id": "r114_n1",
      "task": "schedule",
      "category": "C11",
      "source_span": "ตอนนี้ศูนย์เปิดมั้ย",
      "execution_query": "ตอนนี้ศูนย์เปิดมั้ย ",
      "status": "missing_source",
      "reason_codes": [
        "calendar_interval_adapter_required"
      ],
      "receipts": [],
      "claim_packets": [],
      "semantic_correctness_verified": false
    }
  ],
  "sources": [],
  "positive_contracts": []
}
```

## 27. Can I cancel my booking? Please use verified information

Key: `6d26c7feeaf4f6aabd9d6dafc411b75359e43bfa789594941d80c2b94d7cd146`; locale `en`; original domain `reservation_policy`

### R115 saved

```text
The selected source does not directly confirm the requested detail.
```

### R117 revision03 saved

```text
No confirmed source is available for the requested detail.
```

### R118 revision02

```text
Cancel reservation — confirmed answer: Cancellation of reservations must be made at least 1 hour in advance. [S1]
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "independent_context_frame",
    "tasks": [
      {
        "quote": "can i cancel my booking",
        "domain": "reservation",
        "category": "C08",
        "operation": "detail",
        "facet": "owner_policy",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "069ce4a75758458b9e1efdc9664f609d",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"can i cancel my booking\", \"operation\": \"unknown\", \"domain\": \"reservation\", \"facet\": \"owner_policy\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "meaning_review": {
        "basis": "explicit_booking_cancellation_action",
        "model_plan_accepted": true,
        "model_reason": "validated_interpretation_proposal",
        "prior_tasks": [
          {
            "quote": "can i cancel my booking",
            "domain": "reservation",
            "category": "C08",
            "operation": "unknown",
            "facet": "owner_policy",
            "target": "",
            "constraints": [],
            "ambiguous": false
          }
        ],
        "business_facts_added": false
      },
      "reason": "independent_context_frame",
      "elapsed_sec": 1.421,
      "http_attempted": true,
      "input_question": "can i cancel my booking",
      "legacy_contrast": {
        "domain": "reservation",
        "operation": "unknown",
        "needs": [],
        "reason": "domain_terms=2; no clear operation terms"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false
  },
  "need_results": [
    {
      "need_id": "r114_n1",
      "task": "procedure",
      "category": "C08",
      "source_span": "can i cancel my booking",
      "execution_query": "can i cancel my booking ",
      "status": "supported",
      "reason_codes": [
        "equivalent_literal_policy_sources"
      ],
      "receipts": [
        {
          "record_id": "migrated_faq_curated_cancel_1_hour",
          "field": "answer",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/answer",
              "source_id": "r66_en_f816f54a79926f69db6b589a"
            }
          ]
        }
      ],
      "claim_packets": [
        {
          "fact_id": "C08:migrated_faq_curated_cancel_1_hour:owner_policy",
          "record_id": "migrated_faq_curated_cancel_1_hour",
          "facet": "owner_policy",
          "value": "Cancellation of reservations must be made at least 1 hour in advance.",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/answer",
              "source_id": "r66_en_f816f54a79926f69db6b589a"
            }
          ],
          "fixture": false,
          "status": "answer"
        }
      ],
      "semantic_correctness_verified": false
    }
  ],
  "sources": [],
  "positive_contracts": [
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
      "row": 5447,
      "variant": "question",
      "id": "MASTER-GT-EN-00448",
      "passed": false,
      "failures": [
        "route:knowledge expected:['reservation']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['reservation']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
      "row": 5437,
      "variant": "question",
      "id": "MASTER-GT-EN-00438",
      "passed": false,
      "failures": [
        "route:knowledge expected:['reservation']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['reservation']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_en_5000_v1.jsonl",
      "row": 447,
      "variant": "question",
      "id": "MASTER-GT-EN-00448",
      "passed": false,
      "failures": [
        "route:knowledge expected:['reservation']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['reservation']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_en_5000_v2.jsonl",
      "row": 437,
      "variant": "question",
      "id": "MASTER-GT-EN-00438",
      "passed": false,
      "failures": [
        "route:knowledge expected:['reservation']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['reservation']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    }
  ]
}
```

## 28. ขอสอบถามหน่อยครับ Gaming Keyboard อยู่โซนไหน

Key: `6f6cb1e0e7d55a0d08670c39f2c4a858bf27008a510a7c06b6fc870765b3520e`; locale `th`; original domain `equipment`

### R115 saved

```text
Gaming Keyboard — ที่ตั้ง: PC Zone [S1]
```

### R117 revision03 saved

```text
Gaming Keyboard — ที่ตั้ง: PC Zone [S1]
```

### R118 revision02

```text
Gaming Keyboard — ที่ตั้ง: PC Zone [S1]
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "validated_interpretation_proposal",
    "tasks": [
      {
        "quote": "gaming keyboard อยู่โซนไหน",
        "domain": "equipment",
        "category": "C03",
        "operation": "unknown",
        "facet": "location",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "a9661175d4f04c8bb6129703a45d9723",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"gaming keyboard อยู่โซนไหน\", \"operation\": \"unknown\", \"domain\": \"equipment\", \"facet\": \"location\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 1.438,
      "http_attempted": true,
      "input_question": "gaming keyboard อยู่โซนไหน",
      "legacy_contrast": {
        "domain": "equipment",
        "operation": "unknown",
        "needs": [],
        "reason": "known equipment item alias found; no clear operation terms"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false
  },
  "need_results": [
    {
      "need_id": "r114_n1",
      "task": "equipment",
      "category": "C03",
      "source_span": "gaming keyboard อยู่โซนไหน",
      "execution_query": "gaming keyboard อยู่โซนไหน ",
      "status": "supported",
      "reason_codes": [
        "meaning_bound_requested_field"
      ],
      "receipts": [
        {
          "record_id": "equipment_gaming_keyboard",
          "field": "location",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/specifications",
              "source_id": "r63_0d4513c308153752dd234ccd5b9f"
            }
          ]
        }
      ],
      "claim_packets": [
        {
          "fact_id": "C03:equipment_gaming_keyboard:location",
          "record_id": "equipment_gaming_keyboard",
          "facet": "location",
          "value": "PC Zone",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/specifications",
              "source_id": "r63_0d4513c308153752dd234ccd5b9f"
            }
          ],
          "fixture": false,
          "status": "answer"
        }
      ],
      "semantic_correctness_verified": false
    }
  ],
  "sources": [],
  "positive_contracts": [
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
      "row": 3428,
      "variant": "question",
      "id": "MASTER-GT-TH-03429",
      "passed": false,
      "failures": [
        "route:knowledge expected:['equipment']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['equipment']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
      "row": 3428,
      "variant": "question",
      "id": "MASTER-GT-TH-03429",
      "passed": false,
      "failures": [
        "route:knowledge expected:['equipment']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['equipment']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_th_5000_v1.jsonl",
      "row": 3428,
      "variant": "question",
      "id": "MASTER-GT-TH-03429",
      "passed": false,
      "failures": [
        "route:knowledge expected:['equipment']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['equipment']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_th_5000_v2.jsonl",
      "row": 3428,
      "variant": "question",
      "id": "MASTER-GT-TH-03429",
      "passed": false,
      "failures": [
        "route:knowledge expected:['equipment']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['equipment']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    }
  ]
}
```

## 29. กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า วันจันทร์เช้าเปิดหรือปิด

Key: `790d4406db2db9773074032f548a0c38b10f5a2874ea6e57bf911dede2d57b7e`; locale `th`; original domain `schedule_calendar`

### R115 saved

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

### R117 revision03 saved

```text
1. วันจันทร์เช้าเปิดหรือปิด
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ

2. กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า
ยังตีความส่วนนี้ไม่ชัด กรุณาระบุหัวข้อหรือรายการของส่วนนี้เพิ่มครับ
```

### R118 revision02

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "validated_interpretation_proposal",
    "tasks": [
      {
        "quote": "วันจันทร์เช้าเปิดหรือปิด",
        "domain": "schedule",
        "category": "C11",
        "operation": "schedule_lookup",
        "facet": "open_periods",
        "target": "",
        "constraints": [
          {
            "slot": "date",
            "quote": "วันจันทร์",
            "source_record_id": ""
          },
          {
            "slot": "time",
            "quote": "เช้า",
            "source_record_id": ""
          }
        ],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "f9eab80577354b088d051c698fe1efe3",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"วันจันทร์เช้าเปิดหรือปิด\", \"operation\": \"schedule_lookup\", \"domain\": \"schedule\", \"facet\": \"open_periods\", \"target\": \"\", \"ambiguous\": false, \"constraints\": [{\"slot\": \"date\", \"quote\": \"วันจันทร์\", \"source_record_id\": \"\"}, {\"slot\": \"time\", \"quote\": \"เช้า\", \"source_record_id\": \"\"}]}, {\"quote\": \"กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า\", \"operation\": \"general_answer\", \"domain\": \"general\", \"facet\": \"\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 3.813,
      "http_attempted": true,
      "input_question": "กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า วันจันทร์เช้าเปิดหรือปิด",
      "legacy_contrast": {
        "domain": "schedule",
        "operation": "schedule_lookup",
        "needs": [
          "lookup_schedule"
        ],
        "reason": "domain_terms=3; schedule terms found"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false
  },
  "need_results": [
    {
      "need_id": "r114_n1",
      "task": "schedule",
      "category": "C11",
      "source_span": "วันจันทร์เช้าเปิดหรือปิด",
      "execution_query": "วันจันทร์เช้าเปิดหรือปิด ",
      "status": "missing_source",
      "reason_codes": [
        "requested_facet_not_bound"
      ],
      "receipts": [],
      "claim_packets": [],
      "semantic_correctness_verified": false
    }
  ],
  "sources": [],
  "positive_contracts": []
}
```

## 30. Do I need to check in before playing VALORANT?

Key: `83ff647fde496d6bf0fae1997991043856653dbb8db4f253c79c209ee335dce5`; locale `en`; original domain `competition_rules`

### R115 saved

```text
VALORANT — how to play: The attacking team must place Spikes, while the defending team must defend areas or recover Spikes. The game emphasizes aiming, communication, skill usage, and teamwork. [S1]
```

### R117 revision03 saved

```text
VALORANT — studio services offering this game: PC #01-#02; PC #03-#10 [S1]
```

### R118 revision02

```text
Check-in in advance — confirmed answer: Users must check in before the scheduled round starts. They may check in up to 30 minutes early, and must check in prior to the round's start time. [S1]
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "independent_context_frame",
    "tasks": [
      {
        "quote": "do i need to check in before playing valorant?",
        "domain": "reservation",
        "category": "C08",
        "operation": "detail",
        "facet": "owner_policy",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "545cdef16db24cc39da18d6d4f948db6",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"do i need to check in before playing valorant?\", \"operation\": \"detail\", \"domain\": \"games\", \"facet\": \"studio_services\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "meaning_review": {
        "basis": "booking_action_before_game_context",
        "model_plan_accepted": true,
        "model_reason": "validated_interpretation_proposal",
        "prior_tasks": [
          {
            "quote": "do i need to check in before playing valorant?",
            "domain": "games",
            "category": "C04",
            "operation": "detail",
            "facet": "studio_services",
            "target": "",
            "constraints": [],
            "ambiguous": false
          }
        ],
        "business_facts_added": false
      },
      "reason": "independent_context_frame",
      "elapsed_sec": 1.75,
      "http_attempted": true,
      "input_question": "do i need to check in before playing valorant?",
      "legacy_contrast": {
        "domain": "games",
        "operation": "detail",
        "needs": [
          "summarize_detail",
          "check_availability"
        ],
        "reason": "known game alias found; known game title keeps games domain; no clear operation terms; bare known game title treated as detail"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false
  },
  "need_results": [
    {
      "need_id": "r114_n1",
      "task": "procedure",
      "category": "C08",
      "source_span": "do i need to check in before playing valorant?",
      "execution_query": "do i need to check in before playing valorant? ",
      "status": "supported",
      "reason_codes": [
        "bounded_model_selection"
      ],
      "receipts": [
        {
          "record_id": "migrated_faq_curated_checkin_30_minutes",
          "field": "answer",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/answer",
              "source_id": "r66_en_d3e419df3b10c11599619316"
            }
          ]
        }
      ],
      "claim_packets": [
        {
          "fact_id": "C08:migrated_faq_curated_checkin_30_minutes:owner_policy",
          "record_id": "migrated_faq_curated_checkin_30_minutes",
          "facet": "owner_policy",
          "value": "Users must check in before the scheduled round starts. They may check in up to 30 minutes early, and must check in prior to the round's start time.",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/answer",
              "source_id": "r66_en_d3e419df3b10c11599619316"
            }
          ],
          "fixture": false,
          "status": "answer"
        }
      ],
      "semantic_correctness_verified": false
    }
  ],
  "sources": [],
  "positive_contracts": []
}
```

## 31. Could you please help me with this: I am planning a visit and nee to know: What GPU model is inside the PCs

Key: `88b3a23be4d1646dfc07b79b19b6118016e431f6bb281f64facf06b6dc09b0bf`; locale `en`; original domain `equipment`

### R115 saved

```text
I could not match this question to the migrated information. Please specify the game, device or topic you want to know about.
```

### R117 revision03 saved

```text
I could not match this question to the migrated information. Please specify the game, device or topic you want to know about.
```

### R118 revision02

```text
Gaming PC Model MSI MAG Infinite S3 14th — specifications: GPU: NVIDIA GeForce RTX 5060 8GB [S1]
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "independent_context_frame",
    "tasks": [
      {
        "quote": "i am planning a visit and nee to know: what gpu model is inside the pcs",
        "domain": "equipment",
        "category": "C03",
        "operation": "detail",
        "facet": "specifications",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "7e3b8bd6f8f546dc99fb39514968dda4",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"what gpu model is inside the pcs\", \"operation\": \"unknown\", \"domain\": \"general\", \"facet\": \"\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "meaning_review": {
        "basis": "explicit_hardware_component_with_typed_device",
        "model_plan_accepted": true,
        "model_reason": "validated_interpretation_proposal",
        "prior_tasks": [
          {
            "quote": "what gpu model is inside the pcs",
            "domain": "general",
            "category": null,
            "operation": "unknown",
            "facet": "",
            "target": "",
            "constraints": [],
            "ambiguous": false
          }
        ],
        "business_facts_added": false
      },
      "reason": "independent_context_frame",
      "elapsed_sec": 6.891,
      "http_attempted": true,
      "input_question": "i am planning a visit and nee to know: what gpu model is inside the pcs",
      "legacy_contrast": {
        "domain": "general",
        "operation": "unknown",
        "needs": [],
        "reason": "domain_terms=2; no clear operation terms"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false
  },
  "need_results": [
    {
      "need_id": "r114_n1",
      "task": "equipment",
      "category": "C03",
      "source_span": "i am planning a visit and nee to know: what gpu model is inside the pcs",
      "execution_query": "i am planning a visit and nee to know: what gpu model is inside the pcs ",
      "status": "supported",
      "reason_codes": [
        "typed_hardware_component"
      ],
      "receipts": [
        {
          "record_id": "equipment_gaming_pc",
          "field": "specifications",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/specifications",
              "source_id": "r68_specs_6e0321cf25d72b8d6e364a15"
            }
          ]
        }
      ],
      "claim_packets": [
        {
          "fact_id": "C03:equipment_gaming_pc:specifications",
          "record_id": "equipment_gaming_pc",
          "facet": "specifications",
          "value": "GPU: NVIDIA GeForce RTX 5060 8GB",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/specifications",
              "source_id": "r68_specs_6e0321cf25d72b8d6e364a15"
            }
          ],
          "fixture": false,
          "status": "answer"
        }
      ],
      "semantic_correctness_verified": false
    }
  ],
  "sources": [
    {
      "id": "C03:equipment_gaming_pc:specifications:0",
      "url": "https://esports.phuket.psu.ac.th/home"
    }
  ],
  "positive_contracts": []
}
```

## 32. What does the R2 button do in God of War Ragnarök on PlayStation / PS5

Key: `8acac2d360e8eac92ca9d4c4f51558a451fd9368afa41413edb043a5f783aac4`; locale `en`; original domain `game_controls`

### R115 saved

```text
God of War Ragnarök / PlayStation / PS5 — Lock-On: R3 — Lock enemy target [S1]
God of War Ragnarök / PlayStation / PS5 — Map: Touch Pad — Open World Map [S2]
God of War Ragnarök / PlayStation / PS5 — Sprint: L3 — Press to run [S3]
God of War Ragnarök / PlayStation / PS5 — Camera: R — Control camera rotation [S4]
God of War Ragnarök / PlayStation / PS5 — Equip Primary Weapon: D-Pad Right — Draw the Leviathan Axe. [S5]
God of War Ragnarök / PlayStation / PS5 — Equip Tertiary Weapon: D-Pad Down — Draw the Draupnir Spear. [S6]
God of War Ragnarök / PlayStation / PS5 — Move: L — Move directions [S7]
God of War Ragnarök / PlayStation / PS5 — Pause: Options — Pause Game and Open Main Menu [S8]
```

### R117 revision03 saved

```text
God of War Ragnarök / PlayStation / PS5 — Lock-On: R3 — Lock enemy target [S1]
```

### R118 revision02

```text
God of War Ragnarök / PlayStation / PS5 — Heavy Attack / Heavy Runic Attack (While blocking): R2 — Heavy attack or perform Heavy Rune move with L1 held [S1]
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "independent_context_frame",
    "tasks": [
      {
        "quote": "what does the r2 button do in god of war ragnarök on playstation / ps5",
        "domain": "game_controls",
        "category": "C05",
        "operation": "control",
        "facet": "input_bindings",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "5114dd4cf258433d96c3ae1a35d5e60d",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"what does the r2 button do in god of war ragnarök on playstation / ps5\", \"operation\": \"detail\", \"domain\": \"games\", \"facet\": \"how_to_play\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "meaning_review": {
        "basis": "legacy_control_frame_and_current_source_target",
        "model_plan_accepted": true,
        "model_reason": "validated_interpretation_proposal",
        "prior_tasks": [
          {
            "quote": "what does the r2 button do in god of war ragnarök on playstation / ps5",
            "domain": "games",
            "category": "C04",
            "operation": "detail",
            "facet": "how_to_play",
            "target": "",
            "constraints": [],
            "ambiguous": false
          }
        ],
        "business_facts_added": false
      },
      "reason": "independent_context_frame",
      "elapsed_sec": 1.593,
      "http_attempted": true,
      "input_question": "what does the r2 button do in god of war ragnarök on playstation / ps5",
      "legacy_contrast": {
        "domain": "games",
        "operation": "detail",
        "needs": [
          "summarize_detail",
          "check_availability"
        ],
        "reason": "known game alias found; known game title keeps games domain; no clear operation terms; bare known game title treated as detail"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false
  },
  "need_results": [
    {
      "need_id": "r114_n1",
      "task": "game_controls",
      "category": "C05",
      "source_span": "what does the r2 button do in god of war ragnarök on playstation / ps5",
      "execution_query": "what does the r2 button do in god of war ragnarök on playstation / ps5 ",
      "status": "supported",
      "reason_codes": [
        "exact_button_reverse_lookup"
      ],
      "receipts": [
        {
          "record_id": "controls_ps5_god_of_war_ragnar_k",
          "field": "binding_8",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_14fbfe1964de6dfdec8c3b86"
            }
          ]
        }
      ],
      "claim_packets": [
        {
          "fact_id": "C05:controls_ps5_god_of_war_ragnar_k:binding_8",
          "record_id": "controls_ps5_god_of_war_ragnar_k",
          "facet": "binding_8",
          "value": "R2 — Heavy attack or perform Heavy Rune move with L1 held",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_14fbfe1964de6dfdec8c3b86"
            }
          ],
          "fixture": false,
          "status": "answer"
        }
      ],
      "semantic_correctness_verified": false
    }
  ],
  "sources": [],
  "positive_contracts": [
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
      "row": 7875,
      "variant": "question",
      "id": "MASTER-GT-EN-02876",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
      "row": 7875,
      "variant": "question",
      "id": "MASTER-GT-EN-02876",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_en_5000_v1.jsonl",
      "row": 2875,
      "variant": "question",
      "id": "MASTER-GT-EN-02876",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_en_5000_v2.jsonl",
      "row": 2875,
      "variant": "question",
      "id": "MASTER-GT-EN-02876",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_gt_bilingual_multi_error_2000_20260929_r15.jsonl",
      "row": 1229,
      "variant": "clean",
      "id": "MASTER-GT-EN-02876",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    }
  ]
}
```

## 33. Could you please help me with this: Do you have Hades II

Key: `96ef8f719f0c2f5b3ddcc387738a20d2bb764f97b1ee6f99b347c1bcbb604516`; locale `en`; original domain `games_catalog_availability`

### R115 saved

```text
I could not match this question to the migrated information. Please specify the game, device or topic you want to know about.
```

### R117 revision03 saved

```text
No confirmed source is available for the requested detail.
```

### R118 revision02

```text
No confirmed source is available for the requested detail.
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "validated_interpretation_proposal",
    "tasks": [
      {
        "quote": "do you have hades ii",
        "domain": "games",
        "category": "C04",
        "operation": "unknown",
        "facet": "game_catalog",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "c13168fb83904a019a5c199765de8a7f",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"do you have hades ii\", \"operation\": \"unknown\", \"domain\": \"games\", \"facet\": \"game_catalog\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 1.406,
      "http_attempted": true,
      "input_question": "do you have hades ii",
      "legacy_contrast": {
        "domain": "general",
        "operation": "unknown",
        "needs": [],
        "reason": "domain_terms=2; no clear operation terms"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false
  },
  "need_results": [
    {
      "need_id": "r114_n1",
      "task": "game_detail",
      "category": "C04",
      "source_span": "do you have hades ii",
      "execution_query": "do you have hades ii ",
      "status": "missing_source",
      "reason_codes": [
        "entity_not_bound"
      ],
      "receipts": [],
      "claim_packets": [],
      "semantic_correctness_verified": false
    }
  ],
  "sources": [],
  "positive_contracts": []
}
```

## 34. ขอข้อมูลเรื่องอยู่ที่หน

Key: `981fa8d411c3187b27a4d84d72c48e1557a5729e9be1e1b6e06e705a1c21ea17`; locale `th`; original domain `members_overview_contact`

### R115 saved

```text
ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ อยู่ที่ไหน เช่น คำถามตั้งต้น ไม่จำเป็นต้องเก็บทุก paraphrase / ข้อมูลที่ยืนยันได้ / หัวข้อเชิงความหมาย?
```

### R117 revision03 saved

```text
ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ อยู่ที่ไหน เช่น คำถามตั้งต้น ไม่จำเป็นต้องเก็บทุก paraphrase / ข้อมูลที่ยืนยันได้ / หัวข้อเชิงความหมาย?
```

### R118 revision02

```text
ต้องการทราบเรื่องใดเกี่ยวกับ อยู่ที่ไหน ครับ? ขอรายละเอียดสถานการณ์เพิ่มอีกนิดครับ
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "validated_interpretation_proposal",
    "tasks": [
      {
        "quote": "ขอข้อมูลเรื่องอยู่ที่หน",
        "domain": "general",
        "category": null,
        "operation": "unknown",
        "facet": "",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "99d37ca3cc564a61869630e4efb2e437",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"ขอข้อมูลเรื่องอยู่ที่หน\", \"operation\": \"unknown\", \"domain\": \"general\", \"facet\": \"\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 1.375,
      "http_attempted": true,
      "input_question": "ขอข้อมูลเรื่องอยู่ที่หน",
      "legacy_contrast": {
        "domain": "general",
        "operation": "unknown",
        "needs": [],
        "reason": "domain_terms=2; no clear operation terms"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false,
    "execution_path": "compatibility_fallback"
  },
  "need_results": [
    {
      "need_id": "n1",
      "task": "faq_content",
      "predicate": "unresolved",
      "source_span": "ขอข้อมูลเรื่องอยู่ที่หน",
      "status": "ambiguous_interpretation",
      "reason_codes": [
        "no_accepted_interpretation"
      ],
      "slots": {},
      "record_ids": [
        "migrated_faq_rule_contact_location"
      ],
      "receipts": [],
      "coverage": {
        "version": 1,
        "predicate": "unresolved",
        "task": "unresolved",
        "decision": "scope_unverified",
        "reason_codes": [
          "compatibility_scope_not_migrated"
        ],
        "receipts": [],
        "semantic_correctness_verified": false
      },
      "coverage_basis": "typed predicate contract where available; unmigrated scope remains unverified",
      "read_graph": {
        "graph": {
          "op": "all_of",
          "children": [
            {
              "op": "all_of",
              "children": [
                {
                  "op": "any_of",
                  "children": [
                    {
                      "op": "all_of",
                      "children": [
                        {
                          "op": "field",
                          "children": [],
                          "record_id": "migrated_faq_rule_contact_location",
                          "key": "answer",
                          "reason": ""
                        }
                      ],
                      "record_id": "",
                      "key": "",
                      "reason": ""
                    }
                  ],
                  "record_id": "",
                  "key": "",
                  "reason": ""
                }
              ],
              "record_id": "",
              "key": "",
              "reason": ""
            }
          ],
          "record_id": "",
          "key": "",
          "reason": ""
        },
        "targets": [
          "migrated_faq_rule_contact_location"
        ],
        "relation_paths": [],
        "evaluation": {
          "status": "supported",
          "receipts": [
            {
              "need_id": "n1",
              "subject": "migrated_faq_rule_contact_location",
              "record_id": "migrated_faq_rule_contact_location",
              "predicate": "unresolved",
              "field": "answer",
              "value": {
                "en": "PSU Esports Studio - Phuket is located at Prince of Songkla University, Phuket Campus, 80 Moo 1 Vichitsongkram Road, Kathu, Phuket 83120.",
                "th": "PSU Esports Studio - Phuket ตั้งอยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต 80 หมู่ 1 ถ.วิชิตสงคราม อ.กะทู้ จ.ภูเก็ต 83120"
              },
              "revision": 3,
              "units": null,
              "applicability": {
                "effective_from": null,
                "effective_until": null,
                "state": "unknown"
              },
              "release_id": "migration-preview-r69",
              "epoch": 2093,
              "evidence_refs": [
                {
                  "locator": "/mapped_fields/answer",
                  "source_id": "r63_7c316b9e1c38bb831f9907f0ebc4"
                }
              ],
              "sources": [
                {
                  "source_id": "r63_7c316b9e1c38bb831f9907f0ebc4",
                  "sha256": "d5ea2783fda706ed7d0328b2cc2f2975a1abc39bc61ccf6e3f063a8c97a0c665",
                  "authority_for": [
                    "faq"
                  ],
                  "locator": "/mapped_fields/answer"
                }
              ],
              "verification": "typed_value_and_relation",
              "prose_entailment_verified": false
            }
          ]
        },
        "required_claims_delivered": false
      },
      "claim_packets": []
    }
  ],
  "sources": [],
  "positive_contracts": []
}
```

## 35. Counter-Strike 2 map pool ในกติกาคืออะไร

Key: `9be5826ba7589cd62372217790b8d41ffe79b86ed72e19bcca965576441c4da6`; locale `auto`; original domain `competition_rules`

### R115 saved

```text
Counter-Strike 2 — คำอธิบายเกม: Counter-Strike 2 คือเกมยิงแข่งขันแบบทีมที่แบ่งเป็นฝ่ายบุกและฝ่ายรับ โดยมีเป้าหมายหลักเกี่ยวกับการวาง/กู้ระเบิดหรือจัดการฝ่ายตรงข้าม [S1]
```

### R117 revision03 saved

```text
Counter-Strike 2 — คำอธิบายเกม: Counter-Strike 2 คือเกมยิงแข่งขันแบบทีมที่แบ่งเป็นฝ่ายบุกและฝ่ายรับ โดยมีเป้าหมายหลักเกี่ยวกับการวาง/กู้ระเบิดหรือจัดการฝ่ายตรงข้าม [S1]
```

### R118 revision02

```text
PSU Phuket CS2 2026 Tournament — 3. แผนที่ในการแข่งขัน: 3. แผนที่ในการแข่งขัน [S1]
กฎระเบียบและรูปแบบการแข่งขัน Counter-Strike 2 — แผนที่ในการแข่งขัน: ANCIENT, ANUBIS, DUST 2, INFERNO, MIRAGE, NUKE, TRAIN [S2]
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "independent_context_frame",
    "tasks": [
      {
        "quote": "counter-strike 2 map pool ในกติกาคืออะไร",
        "domain": "competition_rules",
        "category": "C13",
        "operation": "rule_lookup",
        "facet": "rule_clause",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "0d22d350bd3547f0be6021a91925885f",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": false,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"counter-strike 2 map pool ในกติกาคืออะไร\", \"operation\": \"rule_lookup\", \"domain\": \"games\", \"facet\": \"rule_clause\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "meaning_review": {
        "basis": "legacy_competition_frame_with_explicit_context",
        "model_plan_accepted": false,
        "model_reason": "facet_domain_mismatch",
        "prior_tasks": [],
        "business_facts_added": false
      },
      "reason": "independent_context_frame",
      "elapsed_sec": 7.125,
      "http_attempted": true,
      "input_question": "counter-strike 2 map pool ในกติกาคืออะไร",
      "legacy_contrast": {
        "domain": "games",
        "operation": "rule_lookup",
        "needs": [
          "lookup_rule"
        ],
        "reason": "known game alias found; rule terms found"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false
  },
  "need_results": [
    {
      "need_id": "r114_n1",
      "task": "competition_rules",
      "category": "C13",
      "source_span": "counter-strike 2 map pool ในกติกาคืออะไร",
      "execution_query": "counter-strike 2 map pool ในกติกาคืออะไร ",
      "status": "supported",
      "reason_codes": [
        "event_clause_dependency_read"
      ],
      "receipts": [
        {
          "record_id": "competition_competition_rules_cs2_psu_phuket_2026_section_028",
          "field": "rule_clause",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/text",
              "source_id": "r66_en_38ef40b806bc9369ecb12733"
            }
          ]
        },
        {
          "record_id": "r114_cs2_29_rule_clause",
          "field": "answer",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/fields/answer",
              "source_id": "r114_import_7ee2ac86b8d7598a851f8cbc"
            }
          ]
        }
      ],
      "claim_packets": [
        {
          "fact_id": "C13:competition_competition_rules_cs2_psu_phuket_2026_section_028:rule_clause",
          "record_id": "competition_competition_rules_cs2_psu_phuket_2026_section_028",
          "facet": "rule_clause",
          "value": "3. แผนที่ในการแข่งขัน",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/text",
              "source_id": "r66_en_38ef40b806bc9369ecb12733"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C13:r114_cs2_29_rule_clause:rule_clause",
          "record_id": "r114_cs2_29_rule_clause",
          "facet": "rule_clause",
          "value": "ANCIENT, ANUBIS, DUST 2, INFERNO, MIRAGE, NUKE, TRAIN",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/fields/answer",
              "source_id": "r114_import_7ee2ac86b8d7598a851f8cbc"
            }
          ],
          "fixture": false,
          "status": "answer"
        }
      ],
      "semantic_correctness_verified": false
    }
  ],
  "sources": [],
  "positive_contracts": []
}
```

## 36. What does the X button do in The Legend of Zelda: Breath of the Wild on Nintendo Switch

Key: `9db7acd10d57c350138db7c81ed44c1c8801e433a40a8c92391497d23d381f14`; locale `en`; original domain `game_controls`

### R115 saved

```text
The Legend of Zelda: Breath of the Wild / Nintendo Switch — Jump / Dodge (While locked): X — Jump over obstacles or dodge when enemy is locked on [S1]
```

### R117 revision03 saved

```text
The Legend of Zelda: Breath of the Wild / Nintendo Switch — Jump / Dodge (While locked): X — Jump over obstacles or dodge when enemy is locked on [S1]
```

### R118 revision02

```text
The Legend of Zelda: Breath of the Wild / Nintendo Switch — Jump / Dodge (While locked): X — Jump over obstacles or dodge when enemy is locked on [S1]
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "independent_context_frame",
    "tasks": [
      {
        "quote": "what does the x button do in the legend of zelda: breath of the wild on nintendo switch",
        "domain": "game_controls",
        "category": "C05",
        "operation": "control",
        "facet": "input_bindings",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "57579af88f5d4761a8f531a699a0f344",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"what does the x button do in the legend of zelda: breath of the wild on nintendo switch\", \"operation\": \"detail\", \"domain\": \"games\", \"facet\": \"how_to_play\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "meaning_review": {
        "basis": "legacy_control_frame_and_current_source_target",
        "model_plan_accepted": true,
        "model_reason": "validated_interpretation_proposal",
        "prior_tasks": [
          {
            "quote": "what does the x button do in the legend of zelda: breath of the wild on nintendo switch",
            "domain": "games",
            "category": "C04",
            "operation": "detail",
            "facet": "how_to_play",
            "target": "",
            "constraints": [],
            "ambiguous": false
          }
        ],
        "business_facts_added": false
      },
      "reason": "independent_context_frame",
      "elapsed_sec": 1.672,
      "http_attempted": true,
      "input_question": "what does the x button do in the legend of zelda: breath of the wild on nintendo switch",
      "legacy_contrast": {
        "domain": "games",
        "operation": "detail",
        "needs": [
          "summarize_detail",
          "check_availability"
        ],
        "reason": "known game alias found; known game title keeps games domain; no clear operation terms; bare known game title treated as detail"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false
  },
  "need_results": [
    {
      "need_id": "r114_n1",
      "task": "game_controls",
      "category": "C05",
      "source_span": "what does the x button do in the legend of zelda: breath of the wild on nintendo switch",
      "execution_query": "what does the x button do in the legend of zelda: breath of the wild on nintendo switch ",
      "status": "supported",
      "reason_codes": [
        "bounded_model_selection"
      ],
      "receipts": [
        {
          "record_id": "controls_nintendo_the_legend_of_zelda_breath_of_the_wild",
          "field": "binding_6",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_cf9e7f5c6e6c507bb3ca3e27"
            }
          ]
        }
      ],
      "claim_packets": [
        {
          "fact_id": "C05:controls_nintendo_the_legend_of_zelda_breath_of_the_wild:binding_6",
          "record_id": "controls_nintendo_the_legend_of_zelda_breath_of_the_wild",
          "facet": "binding_6",
          "value": "X — Jump over obstacles or dodge when enemy is locked on",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_cf9e7f5c6e6c507bb3ca3e27"
            }
          ],
          "fixture": false,
          "status": "answer"
        }
      ],
      "semantic_correctness_verified": false
    }
  ],
  "sources": [],
  "positive_contracts": [
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
      "row": 7737,
      "variant": "question",
      "id": "MASTER-GT-EN-02738",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
      "row": 7737,
      "variant": "question",
      "id": "MASTER-GT-EN-02738",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_en_5000_v1.jsonl",
      "row": 2737,
      "variant": "question",
      "id": "MASTER-GT-EN-02738",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_en_5000_v2.jsonl",
      "row": 2737,
      "variant": "question",
      "id": "MASTER-GT-EN-02738",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    }
  ]
}
```

## 37. Which studio zone has The Last of Us Part I / Part II

Key: `a1c90b6efa66d5a5dba8f4bd8559db108bf0254516e7929f37346ad730e6fd53`; locale `en`; original domain `game_detail`

### R115 saved

```text
The Last of Us Part I / Part II — genre: Game Genre: Action-Adventure / Survival [S1]
```

### R117 revision03 saved

```text
No confirmed source is available for the requested detail.
```

### R118 revision02

```text
The Last of Us Part I — confirmed studio zones offering this game: PlayStation 5 Zone [S1]
Zone relations still unconfirmed for: The Last of Us Part II
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "validated_interpretation_proposal",
    "tasks": [
      {
        "quote": "which studio zone has the last of us part i / part ii",
        "domain": "games",
        "category": "C04",
        "operation": "detail",
        "facet": "zone",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "5d648db3c8f9405e995cf83841008faa",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"which studio zone has the last of us part i / part ii\", \"operation\": \"detail\", \"domain\": \"games\", \"facet\": \"zone\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 7.281,
      "http_attempted": true,
      "input_question": "which studio zone has the last of us part i / part ii",
      "legacy_contrast": {
        "domain": "games",
        "operation": "detail",
        "needs": [
          "summarize_detail",
          "check_availability"
        ],
        "reason": "known game alias found; known game title keeps games domain; no clear operation terms; bare known game title treated as detail"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false
  },
  "need_results": [
    {
      "need_id": "r114_n1",
      "task": "game_detail",
      "category": "C04",
      "source_span": "which studio zone has the last of us part i / part ii",
      "execution_query": "which studio zone has the last of us part i / part ii ",
      "status": "partial_supported",
      "reason_codes": [
        "some_game_zone_relations_unconfirmed"
      ],
      "receipts": [
        {
          "record_id": "migrated_game_the_last_of_us_part_i",
          "field": "zone",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/game_id",
              "source_id": "r63_3aa389ea971ad2483378efa57ed1"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_3aa389ea971ad2483378efa57ed1"
            },
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_3aa389ea971ad2483378efa57ed1"
            },
            {
              "locator": "/mapped_fields/resource_ids",
              "source_id": "r63_5c4c2946432a8b89ef45c675486d"
            },
            {
              "locator": "/mapped_fields/zone_id",
              "source_id": "r63_df5d776c41b16941439e1a363b2e"
            },
            {
              "locator": "/mapped_fields/zone_id",
              "source_id": "r63_0c8c4707f75172e12d434b37297e"
            }
          ]
        }
      ],
      "claim_packets": [
        {
          "fact_id": "C04:migrated_game_the_last_of_us_part_i:zone",
          "record_id": "migrated_game_the_last_of_us_part_i",
          "facet": "zone",
          "value": "PlayStation 5 Zone",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/game_id",
              "source_id": "r63_3aa389ea971ad2483378efa57ed1"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_3aa389ea971ad2483378efa57ed1"
            },
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_3aa389ea971ad2483378efa57ed1"
            },
            {
              "locator": "/mapped_fields/resource_ids",
              "source_id": "r63_5c4c2946432a8b89ef45c675486d"
            },
            {
              "locator": "/mapped_fields/zone_id",
              "source_id": "r63_df5d776c41b16941439e1a363b2e"
            },
            {
              "locator": "/mapped_fields/zone_id",
              "source_id": "r63_0c8c4707f75172e12d434b37297e"
            }
          ],
          "fixture": false,
          "status": "answer"
        }
      ],
      "semantic_correctness_verified": false
    }
  ],
  "sources": [],
  "positive_contracts": [
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
      "row": 7295,
      "variant": "question",
      "id": "MASTER-GT-EN-02296",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
      "row": 7295,
      "variant": "question",
      "id": "MASTER-GT-EN-02296",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_en_5000_v1.jsonl",
      "row": 2295,
      "variant": "question",
      "id": "MASTER-GT-EN-02296",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_en_5000_v2.jsonl",
      "row": 2295,
      "variant": "question",
      "id": "MASTER-GT-EN-02296",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    }
  ]
}
```

## 38. Could you please help me with this: How much does Cockpit cost

Key: `a87e6d5866fea2f6741277c62836106d3b63f80fc9e787f9f094e3bedb00964e`; locale `en`; original domain `service_fee`

### R115 saved

```text
Rates last reaffirmed by the owner on 2026-10-20; no new effective interval was established.
Cockpit #01-#02 / PSU Student and Staff — per-person price for the rate duration: 0 THB per person for 60 minutes [S1]
Cockpit #01-#02 / PSU Alumni and General Student — per-person price for the rate duration: 65 THB per person for 60 minutes [S2]
Cockpit #01-#02 / General Adult — per-person price for the rate duration: 200 THB per person for 60 minutes [S3]
```

### R117 revision03 saved

```text
Rates last reaffirmed by the owner on 2026-10-20; no new effective interval was established.
Cockpit #01-#02 / PSU Student and Staff — per-person price for the rate duration: 0 THB per person for 60 minutes [S1]
Cockpit #01-#02 / PSU Alumni and General Student — per-person price for the rate duration: 65 THB per person for 60 minutes [S2]
Cockpit #01-#02 / General Adult — per-person price for the rate duration: 200 THB per person for 60 minutes [S3]
```

### R118 revision02

```text
Rates last reaffirmed by the owner on 2026-10-20; no new effective interval was established.
Cockpit #01-#02 / PSU Student and Staff — per-person price for the rate duration: 0 THB per person for 60 minutes [S1]
Cockpit #01-#02 / PSU Alumni and General Student — per-person price for the rate duration: 65 THB per person for 60 minutes [S2]
Cockpit #01-#02 / General Adult — per-person price for the rate duration: 200 THB per person for 60 minutes [S3]
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "validated_interpretation_proposal",
    "tasks": [
      {
        "quote": "how much does cockpit cost",
        "domain": "service_fee",
        "category": "C06",
        "operation": "price_calculate",
        "facet": "amount",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "347a45ae6c444309985eb2ecdc01347b",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"how much does cockpit cost\", \"operation\": \"price_calculate\", \"domain\": \"service_fee\", \"facet\": \"amount\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 1.578,
      "http_attempted": true,
      "input_question": "how much does cockpit cost",
      "legacy_contrast": {
        "domain": "general",
        "operation": "unknown",
        "needs": [],
        "reason": "domain_terms=2; no clear operation terms"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false
  },
  "need_results": [
    {
      "need_id": "r114_n1",
      "task": "price",
      "category": "C06",
      "source_span": "how much does cockpit cost",
      "execution_query": "how much does cockpit cost ",
      "status": "supported",
      "reason_codes": [
        "typed_requested_fields"
      ],
      "receipts": [
        {
          "record_id": "migrated_rate_cockpit_60_1_1_psu_student_staff",
          "field": "amount_minor",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/amount_minor",
              "source_id": "r63_7c1e752ae78e8c2c9389e38b650d"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_7c1e752ae78e8c2c9389e38b650d"
            },
            {
              "locator": "/mapped_fields/audience_id",
              "source_id": "r63_7c1e752ae78e8c2c9389e38b650d"
            },
            {
              "locator": "/mapped_fields/duration_minutes",
              "source_id": "r63_7c1e752ae78e8c2c9389e38b650d"
            },
            {
              "locator": "/fields/answer",
              "source_id": "r114_affirm_rate_0d5e3ccb4a50d3a637cb2118"
            },
            {
              "locator": "/fields/scope_note",
              "source_id": "r114_affirm_rate_0d5e3ccb4a50d3a637cb2118"
            }
          ]
        },
        {
          "record_id": "migrated_rate_cockpit_60_1_1_psu_alumni_general_student",
          "field": "amount_minor",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/amount_minor",
              "source_id": "r63_773d8828419240554040c39d9a60"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_773d8828419240554040c39d9a60"
            },
            {
              "locator": "/mapped_fields/audience_id",
              "source_id": "r63_773d8828419240554040c39d9a60"
            },
            {
              "locator": "/mapped_fields/duration_minutes",
              "source_id": "r63_773d8828419240554040c39d9a60"
            },
            {
              "locator": "/fields/answer",
              "source_id": "r114_affirm_rate_0d5e3ccb4a50d3a637cb2118"
            },
            {
              "locator": "/fields/scope_note",
              "source_id": "r114_affirm_rate_0d5e3ccb4a50d3a637cb2118"
            }
          ]
        },
        {
          "record_id": "migrated_rate_cockpit_60_1_1_general_adult",
          "field": "amount_minor",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/amount_minor",
              "source_id": "r63_9671361adf41b3433392c3c8b569"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_9671361adf41b3433392c3c8b569"
            },
            {
              "locator": "/mapped_fields/audience_id",
              "source_id": "r63_9671361adf41b3433392c3c8b569"
            },
            {
              "locator": "/mapped_fields/duration_minutes",
              "source_id": "r63_9671361adf41b3433392c3c8b569"
            },
            {
              "locator": "/fields/answer",
              "source_id": "r114_affirm_rate_0d5e3ccb4a50d3a637cb2118"
            },
            {
              "locator": "/fields/scope_note",
              "source_id": "r114_affirm_rate_0d5e3ccb4a50d3a637cb2118"
            }
          ]
        }
      ],
      "claim_packets": [
        {
          "fact_id": "C06:migrated_rate_cockpit_60_1_1_psu_student_staff:amount",
          "record_id": "migrated_rate_cockpit_60_1_1_psu_student_staff",
          "facet": "amount",
          "value": "0 THB per person for 60 minutes",
          "numeric": 0.0,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/amount_minor",
              "source_id": "r63_7c1e752ae78e8c2c9389e38b650d"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_7c1e752ae78e8c2c9389e38b650d"
            },
            {
              "locator": "/mapped_fields/audience_id",
              "source_id": "r63_7c1e752ae78e8c2c9389e38b650d"
            },
            {
              "locator": "/mapped_fields/duration_minutes",
              "source_id": "r63_7c1e752ae78e8c2c9389e38b650d"
            },
            {
              "locator": "/fields/answer",
              "source_id": "r114_affirm_rate_0d5e3ccb4a50d3a637cb2118"
            },
            {
              "locator": "/fields/scope_note",
              "source_id": "r114_affirm_rate_0d5e3ccb4a50d3a637cb2118"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C06:migrated_rate_cockpit_60_1_1_psu_alumni_general_student:amount",
          "record_id": "migrated_rate_cockpit_60_1_1_psu_alumni_general_student",
          "facet": "amount",
          "value": "65 THB per person for 60 minutes",
          "numeric": 65.0,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/amount_minor",
              "source_id": "r63_773d8828419240554040c39d9a60"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_773d8828419240554040c39d9a60"
            },
            {
              "locator": "/mapped_fields/audience_id",
              "source_id": "r63_773d8828419240554040c39d9a60"
            },
            {
              "locator": "/mapped_fields/duration_minutes",
              "source_id": "r63_773d8828419240554040c39d9a60"
            },
            {
              "locator": "/fields/answer",
              "source_id": "r114_affirm_rate_0d5e3ccb4a50d3a637cb2118"
            },
            {
              "locator": "/fields/scope_note",
              "source_id": "r114_affirm_rate_0d5e3ccb4a50d3a637cb2118"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C06:migrated_rate_cockpit_60_1_1_general_adult:amount",
          "record_id": "migrated_rate_cockpit_60_1_1_general_adult",
          "facet": "amount",
          "value": "200 THB per person for 60 minutes",
          "numeric": 200.0,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/amount_minor",
              "source_id": "r63_9671361adf41b3433392c3c8b569"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_9671361adf41b3433392c3c8b569"
            },
            {
              "locator": "/mapped_fields/audience_id",
              "source_id": "r63_9671361adf41b3433392c3c8b569"
            },
            {
              "locator": "/mapped_fields/duration_minutes",
              "source_id": "r63_9671361adf41b3433392c3c8b569"
            },
            {
              "locator": "/fields/answer",
              "source_id": "r114_affirm_rate_0d5e3ccb4a50d3a637cb2118"
            },
            {
              "locator": "/fields/scope_note",
              "source_id": "r114_affirm_rate_0d5e3ccb4a50d3a637cb2118"
            }
          ],
          "fixture": false,
          "status": "answer"
        }
      ],
      "semantic_correctness_verified": false
    }
  ],
  "sources": [],
  "positive_contracts": []
}
```

## 39. ขอข้อมูลเรื่องเครื่องดื่ม พื้นที่ ครับ

Key: `aefe99111d809f80d0b9d6893353d58fec0237e9276073fe1016557e8df464b2`; locale `th`; original domain `studio_rules_penalties`

### R115 saved

```text
บริการที่ถาม: รับประทานอาหาร

**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น [S1]
```

### R117 revision03 saved

```text
บริการที่ถาม: รับประทานอาหาร

**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น [S1]
```

### R118 revision02

```text
บริการที่ถาม: รับประทานอาหาร

**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น [S1]
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "validated_interpretation_proposal",
    "tasks": [
      {
        "quote": "ขอข้อมูลเรื่องเครื่องดื่ม พื้นที่ ครับ",
        "domain": "general",
        "category": null,
        "operation": "rule_lookup",
        "facet": "",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "5112f4d64d5549fb9e549692bb46eb21",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"ขอข้อมูลเรื่องเครื่องดื่ม พื้นที่ ครับ\", \"operation\": \"rule_lookup\", \"domain\": \"general\", \"facet\": \"\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 1.796,
      "http_attempted": true,
      "input_question": "ขอข้อมูลเรื่องเครื่องดื่ม พื้นที่ ครับ",
      "legacy_contrast": {
        "domain": "general",
        "operation": "rule_lookup",
        "needs": [
          "lookup_rule"
        ],
        "reason": "domain_terms=2; rule terms found"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false,
    "execution_path": "compatibility_fallback"
  },
  "need_results": [
    {
      "need_id": "n1",
      "task": "faq_content",
      "predicate": "unresolved",
      "source_span": "ขอข้อมูลเรื่องเครื่องดื่ม พื้นที่",
      "status": "supported",
      "reason_codes": [
        "typed_graph_and_delivered_claims"
      ],
      "slots": {},
      "record_ids": [
        "migrated_faq_rule_en_food_drink_natural"
      ],
      "receipts": [
        {
          "need_id": "n1",
          "record_id": "migrated_faq_rule_en_food_drink_natural",
          "field": "answer",
          "predicate": "unresolved",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/answer",
              "source_id": "r63_9d9d2bceeab2eeb22316aa42e7f2"
            }
          ],
          "release_id": "migration-preview-r69",
          "revision": 3,
          "validity": {
            "effective_from": null,
            "effective_until": null,
            "state": "unknown"
          },
          "claim_entailment_verified": false
        }
      ],
      "coverage": {
        "version": 1,
        "predicate": "unresolved",
        "task": "unresolved",
        "decision": "scope_unverified",
        "reason_codes": [
          "compatibility_scope_not_migrated"
        ],
        "receipts": [
          {
            "need_id": "n1",
            "record_id": "migrated_faq_rule_en_food_drink_natural",
            "field": "answer",
            "predicate": "unresolved",
            "evidence_refs": [
              {
                "locator": "/mapped_fields/answer",
                "source_id": "r63_9d9d2bceeab2eeb22316aa42e7f2"
              }
            ],
            "release_id": "migration-preview-r69",
            "revision": 3,
            "validity": {
              "effective_from": null,
              "effective_until": null,
              "state": "unknown"
            },
            "claim_entailment_verified": false
          }
        ],
        "semantic_correctness_verified": false
      },
      "coverage_basis": "typed predicate contract where available; unmigrated scope remains unverified",
      "read_graph": {
        "graph": {
          "op": "all_of",
          "children": [
            {
              "op": "all_of",
              "children": [
                {
                  "op": "any_of",
                  "children": [
                    {
                      "op": "all_of",
                      "children": [
                        {
                          "op": "field",
                          "children": [],
                          "record_id": "migrated_faq_rule_en_food_drink_natural",
                          "key": "answer",
                          "reason": ""
                        }
                      ],
                      "record_id": "",
                      "key": "",
                      "reason": ""
                    }
                  ],
                  "record_id": "",
                  "key": "",
                  "reason": ""
                }
              ],
              "record_id": "",
              "key": "",
              "reason": ""
            }
          ],
          "record_id": "",
          "key": "",
          "reason": ""
        },
        "targets": [
          "migrated_faq_rule_en_food_drink_natural"
        ],
        "relation_paths": [],
        "evaluation": {
          "status": "supported",
          "receipts": [
            {
              "need_id": "n1",
              "subject": "migrated_faq_rule_en_food_drink_natural",
              "record_id": "migrated_faq_rule_en_food_drink_natural",
              "predicate": "unresolved",
              "field": "answer",
              "value": {
                "en": "Food and drinks are allowed only in designated areas.",
                "th": "อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น"
              },
              "revision": 3,
              "units": null,
              "applicability": {
                "effective_from": null,
                "effective_until": null,
                "state": "unknown"
              },
              "release_id": "migration-preview-r69",
              "epoch": 2093,
              "evidence_refs": [
                {
                  "locator": "/mapped_fields/answer",
                  "source_id": "r63_9d9d2bceeab2eeb22316aa42e7f2"
                }
              ],
              "sources": [
                {
                  "source_id": "r63_9d9d2bceeab2eeb22316aa42e7f2",
                  "sha256": "dbcf7c4c40b132b199cf8d6495c3a56c142516bb8341b591aa98f276b7bfa889",
                  "authority_for": [
                    "faq"
                  ],
                  "locator": "/mapped_fields/answer"
                }
              ],
              "verification": "typed_value_and_relation",
              "prose_entailment_verified": false
            }
          ]
        },
        "required_claims_delivered": true
      },
      "claim_packets": [
        {
          "need_id": "n1",
          "subject": "migrated_faq_rule_en_food_drink_natural",
          "record_id": "migrated_faq_rule_en_food_drink_natural",
          "predicate": "unresolved",
          "field": "answer",
          "value": {
            "en": "Food and drinks are allowed only in designated areas.",
            "th": "อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น"
          },
          "revision": 3,
          "units": null,
          "applicability": {
            "effective_from": null,
            "effective_until": null,
            "state": "unknown"
          },
          "release_id": "migration-preview-r69",
          "epoch": 2093,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/answer",
              "source_id": "r63_9d9d2bceeab2eeb22316aa42e7f2"
            }
          ],
          "sources": [
            {
              "source_id": "r63_9d9d2bceeab2eeb22316aa42e7f2",
              "sha256": "dbcf7c4c40b132b199cf8d6495c3a56c142516bb8341b591aa98f276b7bfa889",
              "authority_for": [
                "faq"
              ],
              "locator": "/mapped_fields/answer"
            }
          ],
          "verification": "typed_value_and_relation",
          "prose_entailment_verified": false
        }
      ]
    }
  ],
  "sources": [],
  "positive_contracts": []
}
```

## 40. รบกวนเช็กข้อมูลของศูนย์ให้หน่อยครับ ศุกร์บ่ายเปิดไหม

Key: `b32fb6babd0a86f30c5a9863fdc4e6cab54abe142a07ed3b5e3308a9034fb741`; locale `th`; original domain `schedule_calendar`

### R115 saved

```text
ข้อมูลที่เชื่อมกับรายการนี้ไม่ถูกต้องหรือไม่อยู่ในขอบเขตที่อนุญาต จึงยังยืนยันคำตอบไม่ได้ครับ
```

### R117 revision03 saved

```text
1. ศุกร์บ่ายเปิดไหม
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ

2. รบกวนเช็กข้อมูลของศูนย์ให้หน่อยครับ
ยังตีความส่วนนี้ไม่ชัด กรุณาระบุหัวข้อหรือรายการของส่วนนี้เพิ่มครับ
```

### R118 revision02

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "validated_interpretation_proposal",
    "tasks": [
      {
        "quote": "ศุกร์บ่ายเปิดไหม",
        "domain": "schedule",
        "category": "C11",
        "operation": "schedule_lookup",
        "facet": "open_periods",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "9d3032a830464bbe9df0108def4b7137",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"ศุกร์บ่ายเปิดไหม\", \"operation\": \"schedule_lookup\", \"domain\": \"schedule\", \"facet\": \"open_periods\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}, {\"quote\": \"รบกวนเช็กข้อมูลของศูนย์ให้หน่อยครับ\", \"operation\": \"general_answer\", \"domain\": \"general\", \"facet\": \"\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 2.86,
      "http_attempted": true,
      "input_question": "รบกวนเช็กข้อมูลของศูนย์ให้หน่อยครับ ศุกร์บ่ายเปิดไหม",
      "legacy_contrast": {
        "domain": "schedule",
        "operation": "schedule_lookup",
        "needs": [
          "lookup_schedule"
        ],
        "reason": "domain_terms=3; schedule terms found"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false
  },
  "need_results": [
    {
      "need_id": "r114_n1",
      "task": "schedule",
      "category": "C11",
      "source_span": "ศุกร์บ่ายเปิดไหม",
      "execution_query": "ศุกร์บ่ายเปิดไหม ",
      "status": "missing_source",
      "reason_codes": [
        "requested_facet_not_bound"
      ],
      "receipts": [],
      "claim_packets": [],
      "semantic_correctness_verified": false
    }
  ],
  "sources": [],
  "positive_contracts": [
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
      "row": 1517,
      "variant": "question",
      "id": "MASTER-GT-TH-01518",
      "passed": false,
      "failures": [
        "route:knowledge expected:['schedule']",
        "missing all alternatives: ['เปิด', 'ปิด', 'จอง', 'ยกเลิก', 'นาที', 'อาหาร', 'ปรับ', 'กติกา']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['schedule']"
        ],
        "content_or_format": [
          "missing all alternatives: ['เปิด', 'ปิด', 'จอง', 'ยกเลิก', 'นาที', 'อาหาร', 'ปรับ', 'กติกา']"
        ]
      },
      "positive_literal": true,
      "literal_passed": false,
      "literal_errors": [
        "missing all alternatives: ['เปิด', 'ปิด', 'จอง', 'ยกเลิก', 'นาที', 'อาหาร', 'ปรับ', 'กติกา']"
      ]
    },
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
      "row": 1567,
      "variant": "question",
      "id": "MASTER-GT-TH-01568",
      "passed": false,
      "failures": [
        "route:knowledge expected:['schedule']",
        "missing all alternatives: ['เปิด', 'ปิด', 'จอง', 'ยกเลิก', 'นาที', 'อาหาร', 'ปรับ', 'กติกา']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['schedule']"
        ],
        "content_or_format": [
          "missing all alternatives: ['เปิด', 'ปิด', 'จอง', 'ยกเลิก', 'นาที', 'อาหาร', 'ปรับ', 'กติกา']"
        ]
      },
      "positive_literal": true,
      "literal_passed": false,
      "literal_errors": [
        "missing all alternatives: ['เปิด', 'ปิด', 'จอง', 'ยกเลิก', 'นาที', 'อาหาร', 'ปรับ', 'กติกา']"
      ]
    },
    {
      "file": "data/eval/master_ground_truth_th_5000_v1.jsonl",
      "row": 1517,
      "variant": "question",
      "id": "MASTER-GT-TH-01518",
      "passed": false,
      "failures": [
        "route:knowledge expected:['schedule']",
        "missing all alternatives: ['เปิด', 'ปิด', 'จอง', 'ยกเลิก', 'นาที', 'อาหาร', 'ปรับ', 'กติกา']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['schedule']"
        ],
        "content_or_format": [
          "missing all alternatives: ['เปิด', 'ปิด', 'จอง', 'ยกเลิก', 'นาที', 'อาหาร', 'ปรับ', 'กติกา']"
        ]
      },
      "positive_literal": true,
      "literal_passed": false,
      "literal_errors": [
        "missing all alternatives: ['เปิด', 'ปิด', 'จอง', 'ยกเลิก', 'นาที', 'อาหาร', 'ปรับ', 'กติกา']"
      ]
    },
    {
      "file": "data/eval/master_ground_truth_th_5000_v2.jsonl",
      "row": 1567,
      "variant": "question",
      "id": "MASTER-GT-TH-01568",
      "passed": false,
      "failures": [
        "route:knowledge expected:['schedule']",
        "missing all alternatives: ['เปิด', 'ปิด', 'จอง', 'ยกเลิก', 'นาที', 'อาหาร', 'ปรับ', 'กติกา']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['schedule']"
        ],
        "content_or_format": [
          "missing all alternatives: ['เปิด', 'ปิด', 'จอง', 'ยกเลิก', 'นาที', 'อาหาร', 'ปรับ', 'กติกา']"
        ]
      },
      "positive_literal": true,
      "literal_passed": false,
      "literal_errors": [
        "missing all alternatives: ['เปิด', 'ปิด', 'จอง', 'ยกเลิก', 'นาที', 'อาหาร', 'ปรับ', 'กติกา']"
      ]
    }
  ]
}
```

## 41. ขอสอบถามหน่อยครับ บุคคลทั่วไป เล่น PC 1 ชั่วโมง เสียกี่บาท

Key: `c43bbed1c77ced18210eb25beff0dd928a22fd9ec4417fd7df8cf0a106f1d097`; locale `th`; original domain `service_fee`

### R115 saved

```text
อัตราที่เจ้าของยืนยันล่าสุด ณ 2026-10-20 (ยังไม่ยืนยันวันเริ่ม–สิ้นสุดใหม่)
PC #01-#02 / PSU Student and Staff — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 0 บาท สำหรับ 60 นาที ตามกฎ session_ceil [S1]
PC #01-#02 / PSU Alumni and General Student — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 25 บาท สำหรับ 60 นาที ตามกฎ session_ceil [S2]
PC #01-#02 / General Adult — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 70 บาท สำหรับ 60 นาที ตามกฎ session_ceil [S3]
PC #03-#10 / PSU Student and Staff — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 0 บาท สำหรับ 60 นาที ตามกฎ session_ceil [S4]
PC #03-#10 / PSU Alumni and General Student — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 25 บาท สำหรับ 60 นาที ตามกฎ session_ceil [S5]
PC #03-#10 / General Adult — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 70 บาท สำหรับ 60 นาที ตามกฎ session_ceil [S6]
```

### R117 revision03 saved

```text
อัตราที่เจ้าของยืนยันล่าสุด ณ 2026-10-20 (ยังไม่ยืนยันวันเริ่ม–สิ้นสุดใหม่)
PC #01-#02 / General Adult — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 70 บาท สำหรับ 60 นาที ตามกฎ session_ceil [S1]
PC #03-#10 / General Adult — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 70 บาท สำหรับ 60 นาที ตามกฎ session_ceil [S2]
```

### R118 revision02

```text
อัตราที่เจ้าของยืนยันล่าสุด ณ 2026-10-20 (ยังไม่ยืนยันวันเริ่ม–สิ้นสุดใหม่)
PC #01-#02 / General Adult — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 70 บาท สำหรับ 60 นาที ตามกฎ session_ceil [S1]
PC #03-#10 / General Adult — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 70 บาท สำหรับ 60 นาที ตามกฎ session_ceil [S2]
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "validated_interpretation_proposal",
    "tasks": [
      {
        "quote": "บุคคลทั่วไป เล่น pc 1 ชั่วโมง เสียกี่บาท",
        "domain": "service_fee",
        "category": "C06",
        "operation": "price_calculate",
        "facet": "amount",
        "target": "",
        "constraints": [
          {
            "slot": "audience",
            "quote": "บุคคลทั่วไป",
            "source_record_id": "audience_general_adult"
          }
        ],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "86243180482544e8a3633a5b13091f5f",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"บุคคลทั่วไป เล่น pc 1 ชั่วโมง เสียกี่บาท\", \"operation\": \"price_calculate\", \"domain\": \"service_fee\", \"facet\": \"amount\", \"target\": \"\", \"ambiguous\": false, \"constraints\": [{\"slot\": \"audience\", \"quote\": \"บุคคลทั่วไป\", \"source_record_id\": \"audience_general_adult\"}]}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 2.39,
      "http_attempted": true,
      "input_question": "บุคคลทั่วไป เล่น pc 1 ชั่วโมง เสียกี่บาท",
      "legacy_contrast": {
        "domain": "service_fee",
        "operation": "price_calculate",
        "needs": [
          "calculate_price",
          "show_price_breakdown"
        ],
        "reason": "domain_terms=2; price operation overrides entity/game domain; price terms found"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false
  },
  "need_results": [
    {
      "need_id": "r114_n1",
      "task": "price",
      "category": "C06",
      "source_span": "บุคคลทั่วไป เล่น pc 1 ชั่วโมง เสียกี่บาท",
      "execution_query": "บุคคลทั่วไป เล่น pc 1 ชั่วโมง เสียกี่บาท  General Adult",
      "status": "supported",
      "reason_codes": [
        "typed_requested_fields"
      ],
      "receipts": [
        {
          "record_id": "rate_recovered_pc_availability_pc_01_02_general_adult",
          "field": "amount_minor",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/amount_minor",
              "source_id": "r66_pc_97cb854afb6e7b14fc121fbd"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r66_pc_97cb854afb6e7b14fc121fbd"
            },
            {
              "locator": "/mapped_fields/audience_id",
              "source_id": "r66_pc_97cb854afb6e7b14fc121fbd"
            },
            {
              "locator": "/mapped_fields/duration_minutes",
              "source_id": "r66_pc_97cb854afb6e7b14fc121fbd"
            },
            {
              "locator": "/mapped_fields/unit",
              "source_id": "r66_pc_billing_a47164a72974db629e9c3c5d"
            },
            {
              "locator": "/fields/answer",
              "source_id": "r114_affirm_rate_0d5e3ccb4a50d3a637cb2118"
            },
            {
              "locator": "/fields/scope_note",
              "source_id": "r114_affirm_rate_0d5e3ccb4a50d3a637cb2118"
            }
          ]
        },
        {
          "record_id": "rate_recovered_pc_availability_pc_03_10_general_adult",
          "field": "amount_minor",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/amount_minor",
              "source_id": "r66_pc_dc5b4c42405e267135bbf1f8"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r66_pc_dc5b4c42405e267135bbf1f8"
            },
            {
              "locator": "/mapped_fields/audience_id",
              "source_id": "r66_pc_dc5b4c42405e267135bbf1f8"
            },
            {
              "locator": "/mapped_fields/duration_minutes",
              "source_id": "r66_pc_dc5b4c42405e267135bbf1f8"
            },
            {
              "locator": "/mapped_fields/unit",
              "source_id": "r66_pc_billing_b163a45e8cb08113ed5e5665"
            },
            {
              "locator": "/fields/answer",
              "source_id": "r114_affirm_rate_0d5e3ccb4a50d3a637cb2118"
            },
            {
              "locator": "/fields/scope_note",
              "source_id": "r114_affirm_rate_0d5e3ccb4a50d3a637cb2118"
            }
          ]
        }
      ],
      "claim_packets": [
        {
          "fact_id": "C06:rate_recovered_pc_availability_pc_01_02_general_adult:amount",
          "record_id": "rate_recovered_pc_availability_pc_01_02_general_adult",
          "facet": "amount",
          "value": "70 บาท สำหรับ 60 นาที ตามกฎ session_ceil",
          "numeric": 70.0,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/amount_minor",
              "source_id": "r66_pc_97cb854afb6e7b14fc121fbd"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r66_pc_97cb854afb6e7b14fc121fbd"
            },
            {
              "locator": "/mapped_fields/audience_id",
              "source_id": "r66_pc_97cb854afb6e7b14fc121fbd"
            },
            {
              "locator": "/mapped_fields/duration_minutes",
              "source_id": "r66_pc_97cb854afb6e7b14fc121fbd"
            },
            {
              "locator": "/mapped_fields/unit",
              "source_id": "r66_pc_billing_a47164a72974db629e9c3c5d"
            },
            {
              "locator": "/fields/answer",
              "source_id": "r114_affirm_rate_0d5e3ccb4a50d3a637cb2118"
            },
            {
              "locator": "/fields/scope_note",
              "source_id": "r114_affirm_rate_0d5e3ccb4a50d3a637cb2118"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C06:rate_recovered_pc_availability_pc_03_10_general_adult:amount",
          "record_id": "rate_recovered_pc_availability_pc_03_10_general_adult",
          "facet": "amount",
          "value": "70 บาท สำหรับ 60 นาที ตามกฎ session_ceil",
          "numeric": 70.0,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/amount_minor",
              "source_id": "r66_pc_dc5b4c42405e267135bbf1f8"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r66_pc_dc5b4c42405e267135bbf1f8"
            },
            {
              "locator": "/mapped_fields/audience_id",
              "source_id": "r66_pc_dc5b4c42405e267135bbf1f8"
            },
            {
              "locator": "/mapped_fields/duration_minutes",
              "source_id": "r66_pc_dc5b4c42405e267135bbf1f8"
            },
            {
              "locator": "/mapped_fields/unit",
              "source_id": "r66_pc_billing_b163a45e8cb08113ed5e5665"
            },
            {
              "locator": "/fields/answer",
              "source_id": "r114_affirm_rate_0d5e3ccb4a50d3a637cb2118"
            },
            {
              "locator": "/fields/scope_note",
              "source_id": "r114_affirm_rate_0d5e3ccb4a50d3a637cb2118"
            }
          ],
          "fixture": false,
          "status": "answer"
        }
      ],
      "semantic_correctness_verified": false
    }
  ],
  "sources": [],
  "positive_contracts": [
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
      "row": 313,
      "variant": "question",
      "id": "MASTER-GT-TH-00314",
      "passed": false,
      "failures": [
        "route:knowledge expected:['service_fee']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['service_fee']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
      "row": 313,
      "variant": "question",
      "id": "MASTER-GT-TH-00314",
      "passed": false,
      "failures": [
        "route:knowledge expected:['service_fee']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['service_fee']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_th_5000_v1.jsonl",
      "row": 313,
      "variant": "question",
      "id": "MASTER-GT-TH-00314",
      "passed": false,
      "failures": [
        "route:knowledge expected:['service_fee']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['service_fee']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_th_5000_v2.jsonl",
      "row": 313,
      "variant": "question",
      "id": "MASTER-GT-TH-00314",
      "passed": false,
      "failures": [
        "route:knowledge expected:['service_fee']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['service_fee']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    }
  ]
}
```

## 42. Could you please help me with this: Is it open on Sundays

Key: `c8d9c78fa099e0ae2726a3da4066357a96e22d67640aea89f2c41a5ad07103ed`; locale `en`; original domain `schedule_calendar`

### R115 saved

```text
**Service schedule**
• Opening periods: No entries in this field (confirmed) [S1]
• Bookable periods: No entries in this field (confirmed) [S2]
• Maintenance periods: No entries in this field (confirmed) [S3]
• timezone: Asia/Bangkok [S4]
• weekday: 6 [S5]

English translation is machine generated and has not been reviewed by the owner.
```

### R117 revision03 saved

```text
No confirmed source is available for the requested detail.
```

### R118 revision02

```text
No confirmed source is available for the requested detail.
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "validated_interpretation_proposal",
    "tasks": [
      {
        "quote": "is it open on sundays",
        "domain": "schedule",
        "category": "C11",
        "operation": "schedule_lookup",
        "facet": "bookable_periods",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "48df89147ed1464f8fa37774f58a59f2",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"is it open on sundays\", \"operation\": \"schedule_lookup\", \"domain\": \"schedule\", \"facet\": \"bookable_periods\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 1.469,
      "http_attempted": true,
      "input_question": "is it open on sundays",
      "legacy_contrast": {
        "domain": "general",
        "operation": "unknown",
        "needs": [],
        "reason": "domain_terms=2; no clear operation terms"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false
  },
  "need_results": [
    {
      "need_id": "r114_n1",
      "task": "schedule",
      "category": "C11",
      "source_span": "is it open on sundays",
      "execution_query": "is it open on sundays ",
      "status": "missing_source",
      "reason_codes": [
        "entity_not_bound"
      ],
      "receipts": [],
      "claim_packets": [],
      "semantic_correctness_verified": false
    }
  ],
  "sources": [],
  "positive_contracts": []
}
```

## 43. ขอข้อมูลเรื่องนินเทนโด overcooked

Key: `da13326d0ec0fb58f22dec994cbf4c9d74d86f5e8e260eb5bb7e1248bf5a9c56`; locale `th`; original domain `games_catalog_availability`

### R115 saved

```text
Overcooked 2 — แนวเกม: เกม Co-op ทำอาหาร [S1]
Overcooked 2 — บริการที่มีเกมนี้: Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons) [S2]
Overcooked 2 — วิธีเล่น: ช่วยกันหั่นวัตถุดิบ ปรุง เสิร์ฟ ล้างจาน และสื่อสารกับทีมให้ทันเวลา [S3]
Overcooked 2 — คำอธิบายเกม: Overcooked 2 คือเกมทำอาหารแบบร่วมมือกัน ผู้เล่นต้องแบ่งหน้าที่ เตรียมอาหาร เสิร์ฟ และจัดการครัวที่วุ่นวาย [S4]
```

### R117 revision03 saved

```text
Overcooked 2 — แนวเกม: เกม Co-op ทำอาหาร [S1]
Overcooked 2 — บริการที่มีเกมนี้: Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons) [S2]
Overcooked 2 — วิธีเล่น: ช่วยกันหั่นวัตถุดิบ ปรุง เสิร์ฟ ล้างจาน และสื่อสารกับทีมให้ทันเวลา [S3]
Overcooked 2 — คำอธิบายเกม: Overcooked 2 คือเกมทำอาหารแบบร่วมมือกัน ผู้เล่นต้องแบ่งหน้าที่ เตรียมอาหาร เสิร์ฟ และจัดการครัวที่วุ่นวาย [S4]
```

### R118 revision02

```text
Overcooked 2 — แนวเกม: เกม Co-op ทำอาหาร [S1]
Overcooked 2 — บริการที่มีเกมนี้: Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons) [S2]
Overcooked 2 — วิธีเล่น: ช่วยกันหั่นวัตถุดิบ ปรุง เสิร์ฟ ล้างจาน และสื่อสารกับทีมให้ทันเวลา [S3]
Overcooked 2 — คำอธิบายเกม: Overcooked 2 คือเกมทำอาหารแบบร่วมมือกัน ผู้เล่นต้องแบ่งหน้าที่ เตรียมอาหาร เสิร์ฟ และจัดการครัวที่วุ่นวาย [S4]
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "validated_interpretation_proposal",
    "tasks": [
      {
        "quote": "ขอข้อมูลเรื่องนินเทนโด overcooked",
        "domain": "games",
        "category": "C04",
        "operation": "detail",
        "facet": "game_catalog",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "bd1fdff8973648548fbca8e83c9e2ab4",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"ขอข้อมูลเรื่องนินเทนโด overcooked\", \"operation\": \"detail\", \"domain\": \"games\", \"facet\": \"game_catalog\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 1.468,
      "http_attempted": true,
      "input_question": "ขอข้อมูลเรื่องนินเทนโด overcooked",
      "legacy_contrast": {
        "domain": "games",
        "operation": "detail",
        "needs": [
          "summarize_detail",
          "check_availability"
        ],
        "reason": "known game alias found; known game title keeps games domain; no clear operation terms; bare known game title treated as detail"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false
  },
  "need_results": [
    {
      "need_id": "r114_n1",
      "task": "game_detail",
      "category": "C04",
      "source_span": "ขอข้อมูลเรื่องนินเทนโด overcooked",
      "execution_query": "ขอข้อมูลเรื่องนินเทนโด overcooked ",
      "status": "supported",
      "reason_codes": [
        "bounded_model_selection"
      ],
      "receipts": [
        {
          "record_id": "game_detail_overcooked_2",
          "field": "genre",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/genre",
              "source_id": "r66_en_19d003904c819f49966ead52"
            }
          ]
        },
        {
          "record_id": "game_detail_overcooked_2",
          "field": "studio_services",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_ed1cfcd63b1e41dac6dfa85777ef"
            },
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_722589935e7d81ec268f5ddb11e5"
            }
          ]
        },
        {
          "record_id": "game_detail_overcooked_2",
          "field": "how_to_play",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/how_to_play",
              "source_id": "r66_en_19d003904c819f49966ead52"
            }
          ]
        },
        {
          "record_id": "game_detail_overcooked_2",
          "field": "summary",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/summary",
              "source_id": "r66_en_19d003904c819f49966ead52"
            }
          ]
        }
      ],
      "claim_packets": [
        {
          "fact_id": "C04:game_detail_overcooked_2:genre",
          "record_id": "game_detail_overcooked_2",
          "facet": "genre",
          "value": "เกม Co-op ทำอาหาร",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/genre",
              "source_id": "r66_en_19d003904c819f49966ead52"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C04:game_detail_overcooked_2:studio_services",
          "record_id": "game_detail_overcooked_2",
          "facet": "studio_services",
          "value": "Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons)",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_ed1cfcd63b1e41dac6dfa85777ef"
            },
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_722589935e7d81ec268f5ddb11e5"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C04:game_detail_overcooked_2:how_to_play",
          "record_id": "game_detail_overcooked_2",
          "facet": "how_to_play",
          "value": "ช่วยกันหั่นวัตถุดิบ ปรุง เสิร์ฟ ล้างจาน และสื่อสารกับทีมให้ทันเวลา",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/how_to_play",
              "source_id": "r66_en_19d003904c819f49966ead52"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C04:game_detail_overcooked_2:summary",
          "record_id": "game_detail_overcooked_2",
          "facet": "summary",
          "value": "Overcooked 2 คือเกมทำอาหารแบบร่วมมือกัน ผู้เล่นต้องแบ่งหน้าที่ เตรียมอาหาร เสิร์ฟ และจัดการครัวที่วุ่นวาย",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/summary",
              "source_id": "r66_en_19d003904c819f49966ead52"
            }
          ],
          "fixture": false,
          "status": "answer"
        }
      ],
      "semantic_correctness_verified": false
    }
  ],
  "sources": [],
  "positive_contracts": []
}
```

## 44. Which studio zone has Little Nightmares II

Key: `df43bd3875afe1ec13852f6a55eeaa9498f77bad85c26879dc068c595c49b556`; locale `en`; original domain `game_detail`

### R115 saved

```text
Little Nightmares II — studio services offering this game: Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons) [S1]
```

### R117 revision03 saved

```text
The zone relation is not confirmed; the following studio services are confirmed to offer this game.
Little Nightmares II — studio services offering this game: Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons) [S1]
```

### R118 revision02

```text
The zone relation is not confirmed; the following studio services are confirmed to offer this game.
Little Nightmares II — studio services offering this game: Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons) [S1]
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "validated_interpretation_proposal",
    "tasks": [
      {
        "quote": "which studio zone has little nightmares ii",
        "domain": "games",
        "category": "C04",
        "operation": "detail",
        "facet": "zone",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "fb7607a7b6f3427bbe3b5464cd36205e",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"which studio zone has little nightmares ii\", \"operation\": \"detail\", \"domain\": \"games\", \"facet\": \"zone\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 7.094,
      "http_attempted": true,
      "input_question": "which studio zone has little nightmares ii",
      "legacy_contrast": {
        "domain": "games",
        "operation": "detail",
        "needs": [
          "summarize_detail",
          "check_availability"
        ],
        "reason": "known game alias found; known game title keeps games domain; no clear operation terms; bare known game title treated as detail"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false
  },
  "need_results": [
    {
      "need_id": "r114_n1",
      "task": "game_detail",
      "category": "C04",
      "source_span": "which studio zone has little nightmares ii",
      "execution_query": "which studio zone has little nightmares ii ",
      "status": "partial_supported",
      "reason_codes": [
        "known_services_zone_relation_unconfirmed"
      ],
      "receipts": [
        {
          "record_id": "game_detail_little_nightmares_2",
          "field": "studio_services",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_478fbbfb23338128ec3239ec68a4"
            },
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_bf51329075caf6e636d0af619493"
            }
          ]
        }
      ],
      "claim_packets": [
        {
          "fact_id": "C04:game_detail_little_nightmares_2:studio_services",
          "record_id": "game_detail_little_nightmares_2",
          "facet": "studio_services",
          "value": "Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons)",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_478fbbfb23338128ec3239ec68a4"
            },
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_bf51329075caf6e636d0af619493"
            }
          ],
          "fixture": false,
          "status": "answer"
        }
      ],
      "semantic_correctness_verified": false
    }
  ],
  "sources": [],
  "positive_contracts": [
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
      "row": 7241,
      "variant": "question",
      "id": "MASTER-GT-EN-02242",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']",
        "missing all alternatives: ['Nintendo Switch Zone']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ],
        "content_or_format": [
          "missing all alternatives: ['Nintendo Switch Zone']"
        ]
      },
      "positive_literal": true,
      "literal_passed": false,
      "literal_errors": [
        "missing all alternatives: ['Nintendo Switch Zone']"
      ]
    },
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
      "row": 7241,
      "variant": "question",
      "id": "MASTER-GT-EN-02242",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']",
        "missing all alternatives: ['Nintendo Switch Zone']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ],
        "content_or_format": [
          "missing all alternatives: ['Nintendo Switch Zone']"
        ]
      },
      "positive_literal": true,
      "literal_passed": false,
      "literal_errors": [
        "missing all alternatives: ['Nintendo Switch Zone']"
      ]
    },
    {
      "file": "data/eval/master_ground_truth_en_5000_v1.jsonl",
      "row": 2241,
      "variant": "question",
      "id": "MASTER-GT-EN-02242",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']",
        "missing all alternatives: ['Nintendo Switch Zone']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ],
        "content_or_format": [
          "missing all alternatives: ['Nintendo Switch Zone']"
        ]
      },
      "positive_literal": true,
      "literal_passed": false,
      "literal_errors": [
        "missing all alternatives: ['Nintendo Switch Zone']"
      ]
    },
    {
      "file": "data/eval/master_ground_truth_en_5000_v2.jsonl",
      "row": 2241,
      "variant": "question",
      "id": "MASTER-GT-EN-02242",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']",
        "missing all alternatives: ['Nintendo Switch Zone']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ],
        "content_or_format": [
          "missing all alternatives: ['Nintendo Switch Zone']"
        ]
      },
      "positive_literal": true,
      "literal_passed": false,
      "literal_errors": [
        "missing all alternatives: ['Nintendo Switch Zone']"
      ]
    }
  ]
}
```

## 45. ช่วยอธิบายให้เข้าใจง่ายหน่อยว่า ขอข้อมูลเรื่องของหาย อุปกรณ์ เปียก

Key: `e7a3582eb91ae5efaa59505498774e8fb8612e92d4a2b5736d12c78a7b467a5d`; locale `th`; original domain `studio_rules_penalties`

### R115 saved

```text
ยังยืนยันคำตอบให้ครบตามสถานการณ์ที่ถามไม่ได้ครับ กรุณาระบุรายละเอียดหรือแยกคำถามเพิ่มเติมอีกนิด
```

### R117 revision03 saved

```text
ยังยืนยันคำตอบให้ครบตามสถานการณ์ที่ถามไม่ได้ครับ กรุณาระบุรายละเอียดหรือแยกคำถามเพิ่มเติมอีกนิด
```

### R118 revision02

```text
ยังยืนยันคำตอบให้ครบตามสถานการณ์ที่ถามไม่ได้ครับ กรุณาระบุรายละเอียดหรือแยกคำถามเพิ่มเติมอีกนิด
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": null,
  "need_results": [
    {
      "need_id": "n1",
      "task": "equipment_list",
      "predicate": "equipment_in_scope",
      "source_span": "ช่วยอธิบายให้เข้าใจง่ายหน่อยว่า ขอข้อมูลเรื่องของหาย อุปกรณ์ เปียก",
      "status": "missing_source",
      "reason_codes": [
        "unresolved_query_clause",
        "missing_requested_field:specifications",
        "missing_requested_field:usage"
      ],
      "slots": {},
      "record_ids": [
        "migrated_faq_rule_lost_personal_items"
      ],
      "receipts": [],
      "coverage": {
        "version": 1,
        "predicate": "equipment_in_scope",
        "task": "equipment_list",
        "decision": "rejected",
        "reason_codes": [
          "unresolved_query_clause",
          "missing_requested_field:specifications",
          "missing_requested_field:usage"
        ],
        "receipts": [],
        "semantic_correctness_verified": false
      },
      "coverage_basis": "typed predicate contract where available; unmigrated scope remains unverified",
      "read_graph": {
        "graph": {
          "op": "missing",
          "children": [],
          "record_id": "",
          "key": "",
          "reason": "required_relation_missing"
        },
        "targets": [],
        "relation_paths": [],
        "evaluation": {
          "status": "missing_source",
          "reason": "required_relation_missing",
          "receipts": []
        },
        "required_claims_delivered": false
      },
      "claim_packets": []
    }
  ],
  "sources": [],
  "positive_contracts": []
}
```

## 46. Who holds te role of ประธาน

Key: `e869467170e02fba6c045d82f418e6fde8729870e12377a453b4d40e407a5c42`; locale `en`; original domain `members_overview_contact`

### R115 saved

```text
ยังยืนยันขอบเขตข้อมูลบุคลากรที่เปิดเผยได้ไม่ครบ จึงยังแสดงรายละเอียดส่วนนี้ไม่ได้ครับ
```

### R117 revision03 saved

```text
No confirmed source is available for the requested detail.
```

### R118 revision02

```text
Matching personnel records exist, but their public disclosure scope has not been confirmed.
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "validated_interpretation_proposal",
    "tasks": [
      {
        "quote": "who holds te role of ประธาน",
        "domain": "members",
        "category": "C02",
        "operation": "role_lookup",
        "facet": "role",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "b59a55352ff044af99bc169e8b12ae80",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"who holds te role of ประธาน\", \"operation\": \"role_lookup\", \"domain\": \"members\", \"facet\": \"role\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 7.203,
      "http_attempted": true,
      "input_question": "who holds te role of ประธาน",
      "legacy_contrast": {
        "domain": "general",
        "operation": "role_lookup",
        "needs": [
          "lookup_people_by_role"
        ],
        "reason": "domain_terms=2; role/position lookup terms found"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false
  },
  "need_results": [
    {
      "need_id": "r114_n1",
      "task": "personnel",
      "category": "C02",
      "source_span": "who holds te role of ประธาน",
      "execution_query": "who holds te role of ประธาน ",
      "status": "missing_source",
      "reason_codes": [
        "person_public_scope_not_confirmed"
      ],
      "receipts": [],
      "claim_packets": [],
      "semantic_correctness_verified": false
    }
  ],
  "sources": [],
  "positive_contracts": [
    {
      "file": "data/eval/master_gt_bilingual_multi_error_2000_20260929_r15.jsonl",
      "row": 1682,
      "variant": "noisy",
      "id": "MASTER-GT-EN-04524",
      "passed": false,
      "failures": [
        "route:knowledge expected:['members', 'overview']",
        "missing all alternatives: ['นายษุภากรณ์ จิราจินดากุล', 'ประธาน']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['members', 'overview']"
        ],
        "content_or_format": [
          "missing all alternatives: ['นายษุภากรณ์ จิราจินดากุล', 'ประธาน']"
        ]
      },
      "positive_literal": true,
      "literal_passed": false,
      "literal_errors": [
        "missing all alternatives: ['นายษุภากรณ์ จิราจินดากุล', 'ประธาน']"
      ]
    }
  ]
}
```

## 47. ปุ่มของ New Super Mario Bros. U Deluxe มีอะไรบ้าง

Key: `eafe23b9409a6794810e1fcd47cfba8fd823c4a638c203551cf05697f6ae2134`; locale `auto`; original domain `game_controls`

### R115 saved

```text
New Super Mario Bros. U Deluxe / Nintendo Switch — ควบคุมตัวละครด้วย Joy-Con เดี่ยว: One Joy-Con — หน้า Nintendo ระบุว่าใช้ Joy-Con เพียงหนึ่งข้างก็เล่นได้ เหมาะกับการเล่นหลายคน [S1]
```

### R117 revision03 saved

```text
New Super Mario Bros. U Deluxe / Nintendo Switch — ควบคุมตัวละครด้วย Joy-Con เดี่ยว: One Joy-Con — หน้า Nintendo ระบุว่าใช้ Joy-Con เพียงหนึ่งข้างก็เล่นได้ เหมาะกับการเล่นหลายคน [S1]
New Super Mario Bros. U Deluxe / Nintendo Switch — วิ่ง กระโดด และเหยียบศัตรู: Simple controls — หน้า Nintendo อธิบายการเล่นเป็นเกม 2D side-scrolling ที่ใช้การวิ่ง กระโดด และเหยียบศัตรู แต่ไม่ได้ให้ปุ่มละเอียดรายปุ่ม [S2]
```

### R118 revision02

```text
New Super Mario Bros. U Deluxe / Nintendo Switch — ควบคุมตัวละครด้วย Joy-Con เดี่ยว: One Joy-Con — หน้า Nintendo ระบุว่าใช้ Joy-Con เพียงหนึ่งข้างก็เล่นได้ เหมาะกับการเล่นหลายคน [S1]
New Super Mario Bros. U Deluxe / Nintendo Switch — วิ่ง กระโดด และเหยียบศัตรู: Simple controls — หน้า Nintendo อธิบายการเล่นเป็นเกม 2D side-scrolling ที่ใช้การวิ่ง กระโดด และเหยียบศัตรู แต่ไม่ได้ให้ปุ่มละเอียดรายปุ่ม [S2]
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "validated_interpretation_proposal",
    "tasks": [
      {
        "quote": "ปุ่มของ new super mario bros. u deluxe มีอะไรบ้าง",
        "domain": "game_controls",
        "category": "C05",
        "operation": "list",
        "facet": "input_bindings",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "5916638b4ca54a2a964e982347339648",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"ปุ่มของ new super mario bros. u deluxe มีอะไรบ้าง\", \"operation\": \"list\", \"domain\": \"game_controls\", \"facet\": \"input_bindings\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 1.703,
      "http_attempted": true,
      "input_question": "ปุ่มของ new super mario bros. u deluxe มีอะไรบ้าง",
      "legacy_contrast": {
        "domain": "game_controls",
        "operation": "control",
        "needs": [
          "list_controls"
        ],
        "reason": "known game alias found; control operation overrides domain; control terms found"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false
  },
  "need_results": [
    {
      "need_id": "r114_n1",
      "task": "game_controls",
      "category": "C05",
      "source_span": "ปุ่มของ new super mario bros. u deluxe มีอะไรบ้าง",
      "execution_query": "ปุ่มของ new super mario bros. u deluxe มีอะไรบ้าง ",
      "status": "supported",
      "reason_codes": [
        "complete_source_binding_set"
      ],
      "receipts": [
        {
          "record_id": "controls_nintendo_new_super_mario_bros_u_deluxe",
          "field": "binding_0",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_64f92e9643ffa0cae2e8cfc4"
            }
          ]
        },
        {
          "record_id": "controls_nintendo_new_super_mario_bros_u_deluxe",
          "field": "binding_1",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_64f92e9643ffa0cae2e8cfc4"
            }
          ]
        }
      ],
      "claim_packets": [
        {
          "fact_id": "C05:controls_nintendo_new_super_mario_bros_u_deluxe:binding_0",
          "record_id": "controls_nintendo_new_super_mario_bros_u_deluxe",
          "facet": "binding_0",
          "value": "One Joy-Con — หน้า Nintendo ระบุว่าใช้ Joy-Con เพียงหนึ่งข้างก็เล่นได้ เหมาะกับการเล่นหลายคน",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_64f92e9643ffa0cae2e8cfc4"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C05:controls_nintendo_new_super_mario_bros_u_deluxe:binding_1",
          "record_id": "controls_nintendo_new_super_mario_bros_u_deluxe",
          "facet": "binding_1",
          "value": "Simple controls — หน้า Nintendo อธิบายการเล่นเป็นเกม 2D side-scrolling ที่ใช้การวิ่ง กระโดด และเหยียบศัตรู แต่ไม่ได้ให้ปุ่มละเอียดรายปุ่ม",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/bindings",
              "source_id": "r67_buttons_64f92e9643ffa0cae2e8cfc4"
            }
          ],
          "fixture": false,
          "status": "answer"
        }
      ],
      "semantic_correctness_verified": false
    }
  ],
  "sources": [],
  "positive_contracts": [
    {
      "file": "data/eval/model_benchmark_1500.json",
      "row": 973,
      "variant": "question",
      "id": "MB-0974-GC-268",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": null,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    }
  ]
}
```

## 48. On which device can Animal Crossing: New Horizons be played

Key: `f683a42cb3ba63c5f215900a88eb9a00791cc40073305efffd6fd66cf19d93be`; locale `en`; original domain `games_catalog_availability`

### R115 saved

```text
Animal Crossing: New Horizons — studio services offering this game: Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons) [S1]
```

### R117 revision03 saved

```text
Animal Crossing: New Horizons — studio services offering this game: Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons) [S1]
```

### R118 revision02

```text
Animal Crossing: New Horizons — studio services offering this game: Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons) [S1]
```

### แผน ขอบเขต source และเกณฑ์

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "validated_interpretation_proposal",
    "tasks": [
      {
        "quote": "on which device can animal crossing: new horizons be played",
        "domain": "games",
        "category": "C04",
        "operation": "detail",
        "facet": "supported_platforms",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "630b8b4236064f7fbe14f5036a083350",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"on which device can animal crossing: new horizons be played\", \"operation\": \"detail\", \"domain\": \"games\", \"facet\": \"supported_platforms\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 1.469,
      "http_attempted": true,
      "input_question": "on which device can animal crossing: new horizons be played",
      "legacy_contrast": {
        "domain": "games",
        "operation": "detail",
        "needs": [
          "summarize_detail",
          "check_availability"
        ],
        "reason": "known game alias found; known game title keeps games domain; no clear operation terms; bare known game title treated as detail"
      }
    },
    "factual_correctness_verified": false,
    "legacy_answer_read": false
  },
  "need_results": [
    {
      "need_id": "r114_n1",
      "task": "game_detail",
      "category": "C04",
      "source_span": "on which device can animal crossing: new horizons be played",
      "execution_query": "on which device can animal crossing: new horizons be played ",
      "status": "supported",
      "reason_codes": [
        "bounded_model_selection"
      ],
      "receipts": [
        {
          "record_id": "game_detail_animal_crossing",
          "field": "studio_services",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_882ac508c9e98228eaf4f75a66ee"
            },
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_3e8cf44e9aa1744dac7076cfeea4"
            }
          ]
        }
      ],
      "claim_packets": [
        {
          "fact_id": "C04:game_detail_animal_crossing:studio_services",
          "record_id": "game_detail_animal_crossing",
          "facet": "studio_services",
          "value": "Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons)",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_882ac508c9e98228eaf4f75a66ee"
            },
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_3e8cf44e9aa1744dac7076cfeea4"
            }
          ],
          "fixture": false,
          "status": "answer"
        }
      ],
      "semantic_correctness_verified": false
    }
  ],
  "sources": [],
  "positive_contracts": []
}
```
