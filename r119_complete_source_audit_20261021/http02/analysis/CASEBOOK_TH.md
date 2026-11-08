# คำถามเดิม 48 ข้อ — คำตอบและหลักฐานรายข้อ

เป็น development regression ที่เลือกจาก Full เดิม ไม่ใช่ Full ใหม่และใช้คำนวณความถูกต้องทั้งระบบไม่ได้ คะแนน positive ตรวจ literal/clause ตามโจทย์เดิม ส่วน strict รวม protocol และ performance จึงเป็นคนละเกณฑ์กับความถูกต้องเนื้อหา

| รุ่น | Positive literal/clause | ข้อผ่าน positive ทุกแถว | Strict |
|---|---:|---:|---:|
| Legacy_R64_saved | 62/62 (100.00%) | 18/18 (100.00%) | 133/164 (81.10%) |
| R115_saved | 25/62 (40.32%) | 7/18 (38.89%) | 0/164 (0.00%) |
| R118_revision02_saved | 49/62 (79.03%) | 14/18 (77.78%) | 0/164 (0.00%) |
| R119_revision01 | 62/62 (100.00%) | 18/18 (100.00%) | 0/164 (0.00%) |
| R119_revision02 | 62/62 (100.00%) | 18/18 (100.00%) | 0/164 (0.00%) |

## 044f667114ab611667f0d97496b6ba029d49dfd88337fc90123cd7a189623458

ขอสอบถามหน่อยยครับ บุคคลทั่วไป เล่น PS5 2 ชั่วโมง เสียกี่บาท

### Legacy_R64_saved

```text
ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:

PlayStation 5 — 60 นาที/แพ็กเกจ (1-2 คน)
ระยะเวลาที่ถาม 120 นาที (2 ชั่วโมง) คิดเป็น 2 session (แพ็กเกจ)
•    บุคคลทั่วไป (General Adult): 150 บาท/แพ็กเกจ × 2 = 300 บาท
ตารางต้นฉบับระบุมีผลถึง 2026-03-31 ยังไม่ยืนยันการต่ออายุสำหรับวันที่ต้องการ ตัวเลขด้านบนเป็นอัตราที่บันทึกไว้ครับ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

### R115_saved

```text
กรุณาระบุรายการและช่วงเวลาที่ต้องการตรวจสอบเพิ่มเติมครับ
```

### R118_revision02_saved

```text
อัตราที่เจ้าของยืนยันล่าสุด ณ 2026-10-20 (ยังไม่ยืนยันวันเริ่ม–สิ้นสุดใหม่)
ทราบระยะเวลาที่ต้องการแล้ว แต่ยังไม่มีกฎคำนวณที่ยืนยันสำหรับระยะเวลานี้ อัตราด้านล่างเป็นราคาต่อหน่วยที่บันทึกไว้ ไม่ใช่ยอดรวมของคำขอนี้
PlayStation 5 #01-#02 / PSU Student and Staff — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 0 บาทต่อคน สำหรับ 60 นาที [S1]
PlayStation 5 #01-#02 / PSU Alumni and General Student — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 50 บาทต่อคน สำหรับ 60 นาที [S2]
PlayStation 5 #01-#02 / General Adult — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 150 บาทต่อคน สำหรับ 60 นาที [S3]
```

### R119_revision01

```text
อัตราที่เจ้าของยืนยันล่าสุด ณ 2026-10-20 (ยังไม่ยืนยันวันเริ่ม–สิ้นสุดใหม่)
PlayStation 5 #01-#02 / General Adult — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 300 บาท สำหรับ 120 นาที ตามกฎ session_ceil [S1]
```

### R119_revision02

```text
อัตราที่เจ้าของยืนยันล่าสุด ณ 2026-10-20 (ยังไม่ยืนยันวันเริ่ม–สิ้นสุดใหม่)
PlayStation 5 #01-#02 / General Adult — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 300 บาท สำหรับ 120 นาที ตามกฎ session_ceil [S1]
```

### แผนและหลักฐานที่เลือก

```json
{
  "understanding": {
    "version": "r117",
    "accepted": false,
    "reason": "unbound_or_duplicate_quote",
    "tasks": [],
    "event": {
      "id": "c19f8ca56f104dd48dbc951d0b008c2a",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": false,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"ยครับ บุคคลทั่วไป เล่น ps5 2 ชั่วโมง เสียกี่บาท\", \"operation\": \"price_calculate\", \"domain\": \"service_fee\", \"facet\": \"amount\", \"target\": \"\", \"ambiguous\": false, \"constraints\": [{\"slot\": \"audience\", \"quote\": \"บุคคลทั่วไป\", \"source_record_id\": \"audience_general_adult\"}, {\"slot\": \"duration\", \"quote\": \"2 ชั่วโมง\", \"source_record_id\": \"\"}, {\"slot\": \"platform\", \"quote\": \"ps5\", \"source_record_id\": \"\"}]}, {\"quote\": \"ยครับ บุคคลทั่วไป เล่น ps5 2 ชั่วโมง เสียกี่บาท\", \"operation\": \"price_calculate\", \"domain\": \"service_fee\", \"facet\": \"amount\", \"target\": \"\", \"ambiguous\": false, \"constraints\": [{\"slot\": \"audience\", \"quote\": \"บุคคลทั่วไป\", \"source_record_id\": \"audience_general_adult\"}, {\"slot\": \"duration\", \"quote\": \"2 ชั่วโมง\", \"source_record_id\": \"\"}, {\"slot\": \"platform\", \"quote\": \"ps5\", \"source_record_id\": \"\"}]}]}",
      "reason": "unbound_or_duplicate_quote",
      "elapsed_sec": 12.188,
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
      "status": "supported",
      "reason_codes": [
        "typed_requested_fields"
      ],
      "receipts": [
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
          "fact_id": "C06:migrated_rate_playstation_5_60_1_2_general_adult:amount",
          "record_id": "migrated_rate_playstation_5_60_1_2_general_adult",
          "facet": "amount",
          "value": "300 บาท สำหรับ 120 นาที ตามกฎ session_ceil",
          "numeric": 300.0,
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
  "grades": [
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


## 1806def707336a05166ef9b2589b66cb0450c840866d7ea5f6b920dccd0823f8

เกมไหนเล่นได้หลายโซน

### Legacy_R64_saved

```text
ตอนนี้มีเกมที่ยืนยันได้ทั้งหมด 42 เกมครับ

PC Zone (6 เกม)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT

PlayStation 5 Zone (17 เกม)
•    Call of Duty: Modern Warfare III
•    Delta Force
•    EA Sports FC 24
•    eFootball
•    FINAL FANTASY XVI
•    Fortnite
•    God of War Ragnarok
•    Hogwarts Legacy
•    Marvel's Spider-Man 2
•    NARUTO X BORUTO Ultimate Ninja Storm Connections
•    Resident Evil 4
•    Resident Evil Village
•    TEKKEN 8
•    THE FINALS
•    The Last of Us Part I
•    The Last of Us Part II (Remastered)
•    Uncharted: Legacy of Thieves Collection

Nintendo Switch Zone (17 เกม)
•    Animal Crossing: New Horizons
•    It Takes Two
•    Little Nightmares II
•    Luigi's Mansion 3
•    Mario Kart 8 Deluxe
•    Mario Party Superstars
•    Monster Hunter Rise
•    Moving Out 2
•    New Super Mario Bros. U Deluxe
•    Nintendo Switch Sports
•    Overcooked!
•    Overcooked! 2
•    Pokémon Champions
•    Ring Fit Adventure
•    Super Mario Odyssey
•    Super Smash Bros Ultimate
•    The Legend of Zelda: Breath of The Wild

Cockpit Zone (1 เกม)
•    Gran Turismo 7

VR Zone (4 เกม)
•    Beat Saber
•    Horizon Call of the Mountain
•    Resident Evil 4
•    Resident Evil Village
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games
```

### R115_saved

```text
ข้อมูลที่เลือกยังไม่ยืนยันส่วนที่ถามโดยตรงครับ
```

### R118_revision02_saved

```text
รายการที่ยืนยันได้จากความสัมพันธ์ที่มีอยู่ ยังไม่รับรองว่าครบทุกเกมหรือทุกโซน
TEKKEN 8 — โซนที่ยืนยันว่ามีเกมนี้: PC Zone; PlayStation 5 Zone [S1]
```

### R119_revision01

```text
รายการที่ยืนยันได้จากความสัมพันธ์ที่มีอยู่ ยังไม่รับรองว่าครบทุกเกมหรือทุกโซน
Gran Turismo 7 — โซนที่ยืนยันว่ามีเกมนี้: Cockpit Zone; PlayStation 5 Zone [S1]
Resident Evil 4 — โซนที่ยืนยันว่ามีเกมนี้: PlayStation 5 Zone; VR Zone [S2]
Resident Evil Village — โซนที่ยืนยันว่ามีเกมนี้: PlayStation 5 Zone; VR Zone [S3]
TEKKEN 8 — โซนที่ยืนยันว่ามีเกมนี้: PC Zone; PlayStation 5 Zone [S4]
```

### R119_revision02

```text
รายการที่ยืนยันได้จากความสัมพันธ์ที่มีอยู่ ยังไม่รับรองว่าครบทุกเกมหรือทุกโซน
Gran Turismo 7 — โซนที่ยืนยันว่ามีเกมนี้: Cockpit Zone; PlayStation 5 Zone [S1]
Resident Evil 4 — โซนที่ยืนยันว่ามีเกมนี้: PlayStation 5 Zone; VR Zone [S2]
Resident Evil Village — โซนที่ยืนยันว่ามีเกมนี้: PlayStation 5 Zone; VR Zone [S3]
TEKKEN 8 — โซนที่ยืนยันว่ามีเกมนี้: PC Zone; PlayStation 5 Zone [S4]
```

### แผนและหลักฐานที่เลือก

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
      "id": "d65b5017b75542dfa015dbf8b982da6c",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"เกมไหนเล่นได้หลายโซน\", \"operation\": \"list\", \"domain\": \"games\", \"facet\": \"zone\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 2.454,
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
          "record_id": "game_detail_gran_turismo_7",
          "field": "zone",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_62f2533d0067428586082b6ac1b9"
            },
            {
              "locator": "/mapped_fields/venue_zone_ids",
              "source_id": "r68_url_649481d517be78a8964f6206"
            },
            {
              "locator": "/mapped_fields/name",
              "source_id": "r63_07f7e79d70221b8c20fc453bb3f1"
            },
            {
              "locator": "/mapped_fields/name",
              "source_id": "r63_0f06f91de3bd8af3813677578766"
            },
            {
              "locator": "/mapped_fields/game_id",
              "source_id": "r63_0451c72722b56f3491560d0278fb"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_0451c72722b56f3491560d0278fb"
            },
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_0451c72722b56f3491560d0278fb"
            },
            {
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_b528b3043f26783598ac17771581"
            },
            {
              "locator": "/mapped_fields/resource_ids",
              "source_id": "r63_d5a2927bb1bdd0505aa56847c308"
            },
            {
              "locator": "/mapped_fields/zone_id",
              "source_id": "r63_5fac69dd9f4669e85f363bf380a6"
            },
            {
              "locator": "/mapped_fields/zone_id",
              "source_id": "r63_e0b4f2188b93a81a655c901d745e"
            }
          ]
        },
        {
          "record_id": "game_detail_resident_evil_4",
          "field": "zone",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_43708aa5fda4bd823c9508dbb4fa"
            },
            {
              "locator": "/mapped_fields/venue_zone_ids",
              "source_id": "r68_url_f00be062c1ba36a2c76f0d42"
            },
            {
              "locator": "/mapped_fields/name",
              "source_id": "r63_0f06f91de3bd8af3813677578766"
            },
            {
              "locator": "/mapped_fields/name",
              "source_id": "r63_ec5fdd211eba9cf47c9fd3fcca0e"
            },
            {
              "locator": "/mapped_fields/game_id",
              "source_id": "r63_47744b570d87aececc8391631db9"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_47744b570d87aececc8391631db9"
            },
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_47744b570d87aececc8391631db9"
            },
            {
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_40839d0d488aa9b51d61acd7601c"
            },
            {
              "locator": "/mapped_fields/game_id",
              "source_id": "r63_f2f8c7db217fef45f92f97f56f59"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_f2f8c7db217fef45f92f97f56f59"
            },
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_f2f8c7db217fef45f92f97f56f59"
            },
            {
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_bb17ddf961a4a2f199a813640845"
            },
            {
              "locator": "/mapped_fields/game_id",
              "source_id": "r63_3b6394bcdb8d496c814721b4f647"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_3b6394bcdb8d496c814721b4f647"
            },
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_3b6394bcdb8d496c814721b4f647"
            },
            {
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_2634ae0f9c80f4c2b3cf7ef479fd"
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
        },
        {
          "record_id": "game_detail_resident_evil_village",
          "field": "zone",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_43708aa5fda4bd823c9508dbb4fa"
            },
            {
              "locator": "/mapped_fields/venue_zone_ids",
              "source_id": "r68_url_aa6e0a4528f3ad5df0e667d9"
            },
            {
              "locator": "/mapped_fields/name",
              "source_id": "r63_0f06f91de3bd8af3813677578766"
            },
            {
              "locator": "/mapped_fields/name",
              "source_id": "r63_ec5fdd211eba9cf47c9fd3fcca0e"
            },
            {
              "locator": "/mapped_fields/game_id",
              "source_id": "r63_12e1cc2218f086a5563693f7bea9"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_12e1cc2218f086a5563693f7bea9"
            },
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_12e1cc2218f086a5563693f7bea9"
            },
            {
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_40839d0d488aa9b51d61acd7601c"
            },
            {
              "locator": "/mapped_fields/game_id",
              "source_id": "r63_7e10e37d8026a0446ffc334dfe63"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_7e10e37d8026a0446ffc334dfe63"
            },
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_7e10e37d8026a0446ffc334dfe63"
            },
            {
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_bb17ddf961a4a2f199a813640845"
            },
            {
              "locator": "/mapped_fields/game_id",
              "source_id": "r63_61c17435f7cd2a45c8d807de09da"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_61c17435f7cd2a45c8d807de09da"
            },
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_61c17435f7cd2a45c8d807de09da"
            },
            {
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_2634ae0f9c80f4c2b3cf7ef479fd"
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
        },
        {
          "record_id": "game_detail_tekken_8",
          "field": "zone",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_9df16b21071a334474fd40839855"
            },
            {
              "locator": "/mapped_fields/venue_zone_ids",
              "source_id": "r68_url_e2f0a3fc50c3c324ff2a565f"
            },
            {
              "locator": "/mapped_fields/name",
              "source_id": "migration_zone_pc"
            },
            {
              "locator": "/mapped_fields/name",
              "source_id": "r63_0f06f91de3bd8af3813677578766"
            },
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
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_b5377fed53b354ba4dcf453e2f5e"
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
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_2634ae0f9c80f4c2b3cf7ef479fd"
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
          "fact_id": "C04:game_detail_gran_turismo_7:zone",
          "record_id": "game_detail_gran_turismo_7",
          "facet": "zone",
          "value": "Cockpit Zone; PlayStation 5 Zone",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_62f2533d0067428586082b6ac1b9"
            },
            {
              "locator": "/mapped_fields/venue_zone_ids",
              "source_id": "r68_url_649481d517be78a8964f6206"
            },
            {
              "locator": "/mapped_fields/name",
              "source_id": "r63_07f7e79d70221b8c20fc453bb3f1"
            },
            {
              "locator": "/mapped_fields/name",
              "source_id": "r63_0f06f91de3bd8af3813677578766"
            },
            {
              "locator": "/mapped_fields/game_id",
              "source_id": "r63_0451c72722b56f3491560d0278fb"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_0451c72722b56f3491560d0278fb"
            },
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_0451c72722b56f3491560d0278fb"
            },
            {
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_b528b3043f26783598ac17771581"
            },
            {
              "locator": "/mapped_fields/resource_ids",
              "source_id": "r63_d5a2927bb1bdd0505aa56847c308"
            },
            {
              "locator": "/mapped_fields/zone_id",
              "source_id": "r63_5fac69dd9f4669e85f363bf380a6"
            },
            {
              "locator": "/mapped_fields/zone_id",
              "source_id": "r63_e0b4f2188b93a81a655c901d745e"
            }
          ],
          "fixture": false,
          "status": "answer"
        },
        {
          "fact_id": "C04:game_detail_resident_evil_4:zone",
          "record_id": "game_detail_resident_evil_4",
          "facet": "zone",
          "value": "PlayStation 5 Zone; VR Zone",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_43708aa5fda4bd823c9508dbb4fa"
            },
            {
              "locator": "/mapped_fields/venue_zone_ids",
              "source_id": "r68_url_f00be062c1ba36a2c76f0d42"
            },
            {
              "locator": "/mapped_fields/name",
              "source_id": "r63_0f06f91de3bd8af3813677578766"
            },
            {
              "locator": "/mapped_fields/name",
              "source_id": "r63_ec5fdd211eba9cf47c9fd3fcca0e"
            },
            {
              "locator": "/mapped_fields/game_id",
              "source_id": "r63_47744b570d87aececc8391631db9"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_47744b570d87aececc8391631db9"
            },
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_47744b570d87aececc8391631db9"
            },
            {
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_40839d0d488aa9b51d61acd7601c"
            },
            {
              "locator": "/mapped_fields/game_id",
              "source_id": "r63_f2f8c7db217fef45f92f97f56f59"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_f2f8c7db217fef45f92f97f56f59"
            },
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_f2f8c7db217fef45f92f97f56f59"
            },
            {
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_bb17ddf961a4a2f199a813640845"
            },
            {
              "locator": "/mapped_fields/game_id",
              "source_id": "r63_3b6394bcdb8d496c814721b4f647"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_3b6394bcdb8d496c814721b4f647"
            },
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_3b6394bcdb8d496c814721b4f647"
            },
            {
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_2634ae0f9c80f4c2b3cf7ef479fd"
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
        },
        {
          "fact_id": "C04:game_detail_resident_evil_village:zone",
          "record_id": "game_detail_resident_evil_village",
          "facet": "zone",
          "value": "PlayStation 5 Zone; VR Zone",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_43708aa5fda4bd823c9508dbb4fa"
            },
            {
              "locator": "/mapped_fields/venue_zone_ids",
              "source_id": "r68_url_aa6e0a4528f3ad5df0e667d9"
            },
            {
              "locator": "/mapped_fields/name",
              "source_id": "r63_0f06f91de3bd8af3813677578766"
            },
            {
              "locator": "/mapped_fields/name",
              "source_id": "r63_ec5fdd211eba9cf47c9fd3fcca0e"
            },
            {
              "locator": "/mapped_fields/game_id",
              "source_id": "r63_12e1cc2218f086a5563693f7bea9"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_12e1cc2218f086a5563693f7bea9"
            },
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_12e1cc2218f086a5563693f7bea9"
            },
            {
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_40839d0d488aa9b51d61acd7601c"
            },
            {
              "locator": "/mapped_fields/game_id",
              "source_id": "r63_7e10e37d8026a0446ffc334dfe63"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_7e10e37d8026a0446ffc334dfe63"
            },
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_7e10e37d8026a0446ffc334dfe63"
            },
            {
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_bb17ddf961a4a2f199a813640845"
            },
            {
              "locator": "/mapped_fields/game_id",
              "source_id": "r63_61c17435f7cd2a45c8d807de09da"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_61c17435f7cd2a45c8d807de09da"
            },
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_61c17435f7cd2a45c8d807de09da"
            },
            {
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_2634ae0f9c80f4c2b3cf7ef479fd"
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
        },
        {
          "fact_id": "C04:game_detail_tekken_8:zone",
          "record_id": "game_detail_tekken_8",
          "facet": "zone",
          "value": "PC Zone; PlayStation 5 Zone",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_9df16b21071a334474fd40839855"
            },
            {
              "locator": "/mapped_fields/venue_zone_ids",
              "source_id": "r68_url_e2f0a3fc50c3c324ff2a565f"
            },
            {
              "locator": "/mapped_fields/name",
              "source_id": "migration_zone_pc"
            },
            {
              "locator": "/mapped_fields/name",
              "source_id": "r63_0f06f91de3bd8af3813677578766"
            },
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
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_b5377fed53b354ba4dcf453e2f5e"
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
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_2634ae0f9c80f4c2b3cf7ef479fd"
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
  "grades": [
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


## 8570a28b567efb150998f4e15cebed739de8dcc6c72b66747d9f66b10022607a

Please answer from verified studio information: Which studio zone has TEKKEN 8

### Legacy_R64_saved

```text
TEKKEN 8 is available on: PC #01-#02, PlayStation 5 #01-#02. Studio zone(s): PC Zone, PlayStation 5 Zone.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)
```

### R115_saved

```text
TEKKEN 8 — studio services offering this game: PC #01-#02; PlayStation 5 #01-#02 [S1]
```

### R118_revision02_saved

```text
TEKKEN 8 — confirmed studio zones offering this game: PC Zone; PlayStation 5 Zone [S1]
```

### R119_revision01

```text
TEKKEN 8 — confirmed studio zones offering this game: PC Zone; PlayStation 5 Zone [S1]
```

### R119_revision02

```text
TEKKEN 8 — confirmed studio zones offering this game: PC Zone; PlayStation 5 Zone [S1]
```

### แผนและหลักฐานที่เลือก

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
      "id": "68f7b2d08db444a4811bd6837c23bacd",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"which studio zone has tekken 8\", \"operation\": \"detail\", \"domain\": \"games\", \"facet\": \"zone\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 1.875,
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
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_9df16b21071a334474fd40839855"
            },
            {
              "locator": "/mapped_fields/venue_zone_ids",
              "source_id": "r68_url_e2f0a3fc50c3c324ff2a565f"
            },
            {
              "locator": "/mapped_fields/name",
              "source_id": "migration_zone_pc"
            },
            {
              "locator": "/mapped_fields/name",
              "source_id": "r63_0f06f91de3bd8af3813677578766"
            },
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
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_b5377fed53b354ba4dcf453e2f5e"
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
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_2634ae0f9c80f4c2b3cf7ef479fd"
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
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_9df16b21071a334474fd40839855"
            },
            {
              "locator": "/mapped_fields/venue_zone_ids",
              "source_id": "r68_url_e2f0a3fc50c3c324ff2a565f"
            },
            {
              "locator": "/mapped_fields/name",
              "source_id": "migration_zone_pc"
            },
            {
              "locator": "/mapped_fields/name",
              "source_id": "r63_0f06f91de3bd8af3813677578766"
            },
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
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_b5377fed53b354ba4dcf453e2f5e"
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
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_2634ae0f9c80f4c2b3cf7ef479fd"
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
  "grades": [
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


## 9813e160d170afb1642c7a117bdc3ab5253f5372ad62a7eb27ecdba7a283c1cb

What are all the buttons in Call of Duty: Warzone

### Legacy_R64_saved

```text
Call of Duty: Warzone controls:
- Cross: Jump/Mantle
- Circle: Crouch/Prone/Slide
- Square: Use/Reload
- Triangle: Switch Weapon
- D-Pad: Campaign, Multiplayer or Co-Op specific
- Touch Pad: Scoreboard
- Options: Pause
- L1: Use Tactical Equipment
- R1: Use Lethal Equipment
- L2: Aim Down Sight Behavior
- R2: Fire Weapon
- L3: Sprint/Tactical Sprint/Steady Aim
- R3: Melee
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://gameaccess.info/call-of-duty-warzone-battle-royale-mode-controls/
```

### R115_saved

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

### R118_revision02_saved

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

### R119_revision01

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

### R119_revision02

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

### แผนและหลักฐานที่เลือก

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
      "id": "a521dd893d194be39423ac409882dab6",
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
      "elapsed_sec": 1.937,
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
  "grades": [
    {
      "file": "data/eval/english_shadow_1600_machine_20260908.jsonl",
      "row": 258,
      "variant": "question",
      "id": "EN-SHADOW-0259",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']",
        "legacy_mode_prefix:['pipeline:structured_game_controls']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": null,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']",
          "legacy_mode_prefix:['pipeline:structured_game_controls']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
      "row": 8150,
      "variant": "question",
      "id": "MASTER-GT-EN-03151",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": false,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
      "row": 8150,
      "variant": "question",
      "id": "MASTER-GT-EN-03151",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": false,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_en_5000_v1.jsonl",
      "row": 3150,
      "variant": "question",
      "id": "MASTER-GT-EN-03151",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": false,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_en_5000_v2.jsonl",
      "row": 3150,
      "variant": "question",
      "id": "MASTER-GT-EN-03151",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": false,
      "literal_passed": true,
      "literal_errors": []
    }
  ]
}
```


## 9efbf2ac2cde1a5718eeb278350f7f40337ba912828386fee3cc8315ebc6326a

Please answer from verified studio information: May I record video inside the studio

### Legacy_R64_saved

```text
Permission and conditions for photography or video recording in the studio have not been confirmed.

Source: user-provided service answers (2026-10-08)

local://service_policy/user_answers_20261008
```

### R115_saved

```text
**Relevant information**
• Confirmed information: In-game screenshots and video capture are allowed; delete them when finished. This does not confirm filming people or the premises. [S1]
• topic: C10 [S2]
• Scope: {"r114_fact": {"category": "C10", "facet": "owner_policy", "subject": {"th": "บันทึกภาพในเกม", "en": "game capture"}, "label": {"th": "เงื่อนไขและวิธีปฏิบัติ", "en": "conditions and procedure"}, "owner_confirmed": true, "source_record_id": "Q033"}} [S3]

English translation is machine generated and has not been reviewed by the owner.
```

### R118_revision02_saved

```text
No confirmed source is available for the requested detail.
```

### R119_revision01

```text
No confirmed source is available for the requested detail.
```

### R119_revision02

```text
No confirmed source is available for the requested detail.
```

### แผนและหลักฐานที่เลือก

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
      "id": "d02b33a4438345fba2999138ccaad517",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"may i record video inside the studio\", \"operation\": \"rule_lookup\", \"domain\": \"rules\", \"facet\": \"owner_policy\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 2.015,
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
  "grades": [
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
      "row": 8824,
      "variant": "question",
      "id": "MASTER-GT-EN-03825",
      "passed": false,
      "failures": [
        "route:knowledge expected:['no_answer', 'overview', 'rules']",
        "status:answer expected:no_answer_expected"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['no_answer', 'overview', 'rules']"
        ],
        "outcome": [
          "status:answer expected:no_answer_expected"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
      "row": 8824,
      "variant": "question",
      "id": "MASTER-GT-EN-03825",
      "passed": false,
      "failures": [
        "route:knowledge expected:['no_answer', 'overview', 'rules']",
        "status:answer expected:no_answer_expected"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['no_answer', 'overview', 'rules']"
        ],
        "outcome": [
          "status:answer expected:no_answer_expected"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_en_5000_v1.jsonl",
      "row": 3824,
      "variant": "question",
      "id": "MASTER-GT-EN-03825",
      "passed": false,
      "failures": [
        "route:knowledge expected:['no_answer', 'overview', 'rules']",
        "status:answer expected:no_answer_expected"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['no_answer', 'overview', 'rules']"
        ],
        "outcome": [
          "status:answer expected:no_answer_expected"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_en_5000_v2.jsonl",
      "row": 3824,
      "variant": "question",
      "id": "MASTER-GT-EN-03825",
      "passed": false,
      "failures": [
        "route:knowledge expected:['no_answer', 'overview', 'rules']",
        "status:answer expected:no_answer_expected"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['no_answer', 'overview', 'rules']"
        ],
        "outcome": [
          "status:answer expected:no_answer_expected"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_gt_bilingual_multi_error_2000_20260929_r15.jsonl",
      "row": 1532,
      "variant": "clean",
      "id": "MASTER-GT-EN-03825",
      "passed": false,
      "failures": [
        "route:knowledge expected:['no_answer', 'overview', 'rules']",
        "status:answer expected:no_answer_expected"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['no_answer', 'overview', 'rules']"
        ],
        "outcome": [
          "status:answer expected:no_answer_expected"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    }
  ]
}
```


## a9ecf2e1299ecafcd502f509c23241bf23889fad81c1a196d62f13c9c480d7e2

กำลังวางแผนไปใช้บริการ เลยอยากทราบว่า ขอข้อมูลที่ยืนยันได้หน่อยครับ: Maintenance คือช่วงไหน

### Legacy_R64_saved

```text
วันและช่วงเวลาให้บริการตามตารางปกติ (ไม่ใช่สถานะเครื่องว่างแบบสด):
•    วันจันทร์: เปิด 13:00-16:00; Maintenance 09:00-12:00
•    วันอังคาร-พฤหัสบดี: เปิด 09:00-12:00, 13:00-16:00
•    วันศุกร์: เปิด 09:00-12:00; Maintenance 13:00-16:00
•    วันเสาร์-อาทิตย์: ไม่มีรอบให้บริการหรือจองตามตารางปกติ
วันปิดพิเศษมีผลก่อนตารางปกติ และช่วงที่เปิดไม่ได้ยืนยันว่าเครื่องยังว่างครับ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

### R115_saved

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

### R118_revision02_saved

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

### R119_revision01

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

### R119_revision02

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

### แผนและหลักฐานที่เลือก

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
      "id": "e5b0591193634c5393b8f3bb8dcf811e",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"maintenance คือช่วงไหน\", \"operation\": \"schedule_lookup\", \"domain\": \"schedule\", \"facet\": \"maintenance_periods\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 2.109,
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
  "grades": [
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
      "row": 1450,
      "variant": "question",
      "id": "MASTER-GT-TH-01451",
      "passed": false,
      "failures": [
        "route:knowledge expected:['schedule']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['schedule']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
      "row": 1490,
      "variant": "question",
      "id": "MASTER-GT-TH-01491",
      "passed": false,
      "failures": [
        "route:knowledge expected:['schedule']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['schedule']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_th_5000_v1.jsonl",
      "row": 1450,
      "variant": "question",
      "id": "MASTER-GT-TH-01451",
      "passed": false,
      "failures": [
        "route:knowledge expected:['schedule']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['schedule']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_th_5000_v2.jsonl",
      "row": 1490,
      "variant": "question",
      "id": "MASTER-GT-TH-01491",
      "passed": false,
      "failures": [
        "route:knowledge expected:['schedule']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['schedule']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    }
  ]
}
```


## b2ff4f05d34e5b2a82ae5cb5ede86f5a05bb022cf13531c682a39d936e4de5b7

God of War Ragnarök ปุ่มทั้งหมดมีอะไรบ้าง

### Legacy_R64_saved

```text
God of War Ragnarök มีข้อมูลปุ่มควบคุมดังนี้:
PlayStation / PS5
•    L: เคลื่อนที่ - บังคับทิศทางการเดิน
•    L3: วิ่งสปรินต์ - กดเพื่อวิ่ง
•    L3 + R3: พลังสปาร์ตัน - ระเบิดความโกรธของเครโทสเพื่อเพิ่มพลังโจมตีและฟื้นฟูพลังชีวิต
•    R: มุมกล้อง - ควบคุมการหมุนมุมกล้อง
•    R3: ล็อกเป้าหมาย - ล็อกเป้าหมายศัตรู
•    L2 (Hold): เล็ง (กดค้าง) - ง้างอาวุธเตรียมขว้าง
•    L1 (Hold): ป้องกัน (กดค้าง) - ยกโล่ขึ้นป้องกันการโจมตี และใช้เป็นปุ่มร่วมสำหรับคำสั่ง Runic/Relic
•    R1: โจมตีเบา / รูนเบา / ขว้าง - โจมตีปกติเบา, ขว้างอาวุธเมื่อกดเล็ง, หรือใช้ท่ารูนเบาเมื่อกดค้าง L1
•    R2: โจมตีหนัก / รูนหนัก - โจมตีปกติหนัก หรือใช้ท่ารูนหนักเมื่อกดค้าง L1
•    Triangle: เรียกขวานกลับ / ชาร์จพลังอาวุธ - เรียกขวานกลับเข้ามือ หรือชาร์จพลังธาตุให้อาวุธเมื่อกดค้าง L1
•    Circle: โต้ตอบ / ใช้งานรีลิค - สำรวจสภาพแวดล้อม หรือใช้งานไอเทม Relic เมื่อกดค้าง L1
•    Square: คู่หูโจมตี - สั่งคู่หูยิงธนูสนับสนุน
•    Cross: สเตปหลบ / กลิ้งหลบ - กด 1 ครั้งเพื่อโยกตัวหลบ หรือกด 2 ครั้งติดเพื่อกลิ้งหลบ
•    D-Pad Right: ติดตั้งอาวุธหลัก - ชักขวาน Leviathan
•    D-Pad Left: ติดตั้งอาวุธรอง - ชักดาบโซ่ Blades of Chaos
•    D-Pad Down: ติดตั้งอาวุธที่สาม - ชักหอก Draupnir Spear
•    D-Pad Up: เปลี่ยนชนิดลูกธนู - สลับลูกธนูของคู่หู
•    Options: หยุดเกม - หยุดเกมและเปิดเมนูหลัก
•    Touch Pad: แผนที่ - เปิดแผนที่โลก
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://gameinputdatabase.com/game/14
```

### R115_saved

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

### R118_revision02_saved

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

### R119_revision01

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

### R119_revision02

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

### แผนและหลักฐานที่เลือก

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
      "id": "b56dbb1543c843efa7373a2c91921688",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"god of war ragnarök ปุ่มทั้งหมดมีอะไรบ้าง\", \"operation\": \"list\", \"domain\": \"game_controls\", \"facet\": \"input_bindings\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 2.109,
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
  "grades": [
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


## f10707b2c0244f8083805c71be540378e1f2090baa4cfb2a10ad7af8cc422f7f

กำลังวางแผนจะไปใช้บริการ อพดีอยากรู้ว่า วันอังคารศูนย์เปิดกี่โมง

### Legacy_R64_saved

```text
วันอังคาร: เปิดให้เล่น 09:00-12:00 และ 13:00-16:00

รายละเอียดจากตาราง:
•    วันอังคาร: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = open
แหล่งข้อมูล: https://esports.computing.psu.ac.th/
```

### R115_saved

```text
ข้อมูลที่เชื่อมกับรายการนี้ไม่ถูกต้องหรือไม่อยู่ในขอบเขตที่อนุญาต จึงยังยืนยันคำตอบไม่ได้ครับ
```

### R118_revision02_saved

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### R119_revision01

```text
อังคาร — ตารางให้บริการเล่น: เปิดให้บริการเล่นตามตาราง 09:00–12:00, 13:00–16:00 [S1]
```

### R119_revision02

```text
อังคาร — ตารางให้บริการเล่น: เปิดให้บริการเล่นตามตาราง 09:00–12:00, 13:00–16:00 [S1]
```

### แผนและหลักฐานที่เลือก

```json
{
  "understanding": {
    "version": "r117",
    "accepted": false,
    "reason": "invented_constraint",
    "tasks": [],
    "event": {
      "id": "85b966c7300f488a9743afb9bada1aa5",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": false,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"วันอังคารศูนย์เปิดกี่โมง\", \"operation\": \"schedule_lookup\", \"domain\": \"schedule\", \"facet\": \"open_periods\", \"target\": \"\", \"ambiguous\": false, \"constraints\": [{\"slot\": \"date\", \"quote\": \"วันอังคาร\", \"source_record_id\": \"\"}, {\"slot\": \"audience\", \"quote\": \"\", \"source_record_id\": \"\"}]}, {\"quote\": \"กำลังวางแผนจะไปใช้บริการ อพดีอยากรู้ว่า\", \"operation\": \"general_answer\", \"domain\": \"general\", \"facet\": \"\", \"target\": \"\", \"ambiguous\": false, \"constraints\": [{\"slot\": \"audience\", \"quote\": \"กำลังวางแผนจะไปใช้บริการ อพดีอยากรู้ว่า\", \"source_record_id\": \"\"}]}, {\"quote\": \"อพดีอยากรู้ว่า\", \"operation\": \"general_answer\", \"domain\": \"general\", \"facet\": \"\", \"target\": \"\", \"ambiguous\": false, \"constraints\": [{\"slot\": \"audience\", \"quote\": \"อพดีอยากรู้ว่า\", \"source_record_id\": \"\"}]}]}",
      "reason": "invented_constraint",
      "elapsed_sec": 6.703,
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
      "source_span": "กำลังวางแผนจะไปใช้บริการ อพดีอยากรู้ว่า วันอังคารศูนย์เปิดกี่โมง",
      "execution_query": "กำลังวางแผนจะไปใช้บริการ อพดีอยากรู้ว่า วันอังคารศูนย์เปิดกี่โมง",
      "status": "supported",
      "reason_codes": [
        "recorded_play_service_calendar"
      ],
      "receipts": [
        {
          "record_id": "migrated_schedule_1",
          "field": "service_periods",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/service_slots",
              "source_id": "r119_894b92f0a7840a44223c83a6324b"
            }
          ]
        }
      ],
      "claim_packets": [
        {
          "fact_id": "C11:migrated_schedule_1:service_periods",
          "record_id": "migrated_schedule_1",
          "facet": "service_periods",
          "value": "เปิดให้บริการเล่นตามตาราง 09:00–12:00, 13:00–16:00",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/service_slots",
              "source_id": "r119_894b92f0a7840a44223c83a6324b"
            }
          ],
          "fixture": false,
          "status": "answer"
        }
      ],
      "semantic_correctness_verified": false
    }
  ],
  "grades": [
    {
      "file": "data/eval/master_gt_bilingual_multi_error_2000_20260929_r15.jsonl",
      "row": 913,
      "variant": "noisy",
      "id": "MASTER-GT-TH-01273",
      "passed": false,
      "failures": [
        "route:knowledge expected:['schedule']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['schedule']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    }
  ]
}
```


## 00301c15cd98d9ae70f652fc7e3e088e82b1780bf462c6be801ec81eec2a824a

กำลังวางแผนไปใช้บริการ เลยอยากทราบว่า ขอข้อมูลเรื่องระงับสิทธิ์ชั่วคราว

### Legacy_R64_saved

```text
หากผู้ใช้งานละเมิดกฎซ้ำหรือกระทำการรุนแรง อาจถูกระงับสิทธิ์การใช้งานชั่วคราวเป็นระยะเวลา 1-7 วัน ขึ้นอยู่กับลักษณะของการละเมิด
แหล่งข้อมูล: https://esports.computing.psu.ac.th/
```

### R115_saved

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

### R118_revision02_saved

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

### R119_revision01

```text
ยังยืนยันคำตอบให้ครบตามสถานการณ์ที่ถามไม่ได้ครับ กรุณาระบุรายละเอียดหรือแยกคำถามเพิ่มเติมอีกนิด
```

### R119_revision02

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### แผนและหลักฐานที่เลือก

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "validated_interpretation_proposal",
    "tasks": [
      {
        "quote": "ขอข้อมูลเรื่องระงับสิทธิ์ชั่วคราว",
        "domain": "rules",
        "category": "C10",
        "operation": "unknown",
        "facet": "",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "4ec42b21f7b243c0a94805cfc2bb12aa",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"ขอข้อมูลเรื่องระงับสิทธิ์ชั่วคราว\", \"operation\": \"unknown\", \"domain\": \"rules\", \"facet\": \"\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 2.047,
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
    "legacy_answer_read": false
  },
  "need_results": [
    {
      "need_id": "r114_n1",
      "task": "policy",
      "category": "C10",
      "source_span": "ขอข้อมูลเรื่องระงับสิทธิ์ชั่วคราว",
      "execution_query": "ขอข้อมูลเรื่องระงับสิทธิ์ชั่วคราว ",
      "status": "missing_source",
      "reason_codes": [
        "entity_not_bound"
      ],
      "receipts": [],
      "claim_packets": [],
      "semantic_correctness_verified": false
    }
  ],
  "grades": [
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
      "row": 3724,
      "variant": "question",
      "id": "MASTER-GT-TH-03725",
      "passed": false,
      "failures": [
        "route:knowledge expected:['penalty']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['penalty']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
      "row": 3724,
      "variant": "question",
      "id": "MASTER-GT-TH-03725",
      "passed": false,
      "failures": [
        "route:knowledge expected:['penalty']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['penalty']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_th_5000_v1.jsonl",
      "row": 3724,
      "variant": "question",
      "id": "MASTER-GT-TH-03725",
      "passed": false,
      "failures": [
        "route:knowledge expected:['penalty']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['penalty']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_th_5000_v2.jsonl",
      "row": 3724,
      "variant": "question",
      "id": "MASTER-GT-TH-03725",
      "passed": false,
      "failures": [
        "route:knowledge expected:['penalty']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['penalty']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    }
  ]
}
```


## 0d05eaf601eadf916bc92c4e43a8a10ce1897c3412ccc9c1534782cda7c52ef7

How much does it cost for an adult to play VR for one hour?

### Legacy_R64_saved

```text
Service prices (recorded package rates):

VR — 60 minutes/package (1-5 people)
Requested duration: 60 minutes (1 hours); 1 session(s).
• General adults: 1,050 THB/package
The original fee table states validity through 2026-03-31; continued validity for the requested date has not been confirmed.
Source: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

### R115_saved

```text
Rates last reaffirmed by the owner on 2026-10-20; no new effective interval was established.
VR Station 30 นาที / PSU Student and Staff — per-person price for the rate duration: 0 THB per person for 30 minutes [S1]
VR Station 30 นาที / PSU Alumni and General Student — per-person price for the rate duration: 190 THB per person for 30 minutes [S2]
VR Station 30 นาที / General Adult — per-person price for the rate duration: 525 THB per person for 30 minutes [S3]
VR Station 1 ชั่วโมง / PSU Student and Staff — per-person price for the rate duration: 0 THB per person for 60 minutes [S4]
VR Station 1 ชั่วโมง / PSU Alumni and General Student — per-person price for the rate duration: 375 THB per person for 60 minutes [S5]
VR Station 1 ชั่วโมง / General Adult — per-person price for the rate duration: 1050 THB per person for 60 minutes [S6]
```

### R118_revision02_saved

```text
Rates last reaffirmed by the owner on 2026-10-20; no new effective interval was established.
VR Station 1 ชั่วโมง / General Adult — per-person price for the rate duration: 1050 THB for 60 minutes under the declared explicit_whole_sessions rule [S1]
```

### R119_revision01

```text
Rates last reaffirmed by the owner on 2026-10-20; no new effective interval was established.
VR Station 30 นาที / General Adult — per-person price for the rate duration: 525 THB per person for 30 minutes [S1]
VR Station 1 ชั่วโมง / General Adult — per-person price for the rate duration: 1050 THB per person for 60 minutes [S2]
```

### R119_revision02

```text
Rates last reaffirmed by the owner on 2026-10-20; no new effective interval was established.
VR Station 30 นาที / General Adult — per-person price for the rate duration: 525 THB per person for 30 minutes [S1]
VR Station 1 ชั่วโมง / General Adult — per-person price for the rate duration: 1050 THB per person for 60 minutes [S2]
```

### แผนและหลักฐานที่เลือก

```json
{
  "understanding": {
    "version": "r117",
    "accepted": false,
    "reason": "unbound_or_duplicate_quote",
    "tasks": [],
    "event": {
      "id": "878ff8bc42594af0a4fba48c4a4c506a",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": false,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"how much does it cost for an adult to play vr for one hour?\", \"operation\": \"price_calculate\", \"domain\": \"service_fee\", \"facet\": \"amount\", \"target\": \"\", \"ambiguous\": false, \"constraints\": [{\"slot\": \"audience\", \"quote\": \"adult\", \"source_record_id\": \"audience_general_adult\"}, {\"slot\": \"duration\", \"quote\": \"one hour\", \"source_record_id\": \"\"}, {\"slot\": \"service\", \"quote\": \"play vr\", \"source_record_id\": \"\"}]}, {\"quote\": \"\", \"operation\": \"unknown\", \"domain\": \"general\", \"facet\": \"\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "unbound_or_duplicate_quote",
      "elapsed_sec": 4.297,
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
      "source_span": "how much does it cost for an adult to play vr for one hour",
      "execution_query": "how much does it cost for an adult to play vr for one hour",
      "status": "supported",
      "reason_codes": [
        "typed_requested_fields"
      ],
      "receipts": [
        {
          "record_id": "migrated_rate_vr_30_1_5_general_adult",
          "field": "amount_minor",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/amount_minor",
              "source_id": "r63_15ad37bbca1867990b52071d9877"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_15ad37bbca1867990b52071d9877"
            },
            {
              "locator": "/mapped_fields/audience_id",
              "source_id": "r63_15ad37bbca1867990b52071d9877"
            },
            {
              "locator": "/mapped_fields/duration_minutes",
              "source_id": "r63_15ad37bbca1867990b52071d9877"
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
          "fact_id": "C06:migrated_rate_vr_30_1_5_general_adult:amount",
          "record_id": "migrated_rate_vr_30_1_5_general_adult",
          "facet": "amount",
          "value": "525 THB per person for 30 minutes",
          "numeric": 525.0,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/amount_minor",
              "source_id": "r63_15ad37bbca1867990b52071d9877"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_15ad37bbca1867990b52071d9877"
            },
            {
              "locator": "/mapped_fields/audience_id",
              "source_id": "r63_15ad37bbca1867990b52071d9877"
            },
            {
              "locator": "/mapped_fields/duration_minutes",
              "source_id": "r63_15ad37bbca1867990b52071d9877"
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
          "fact_id": "C06:migrated_rate_vr_60_1_5_general_adult:amount",
          "record_id": "migrated_rate_vr_60_1_5_general_adult",
          "facet": "amount",
          "value": "1050 THB per person for 60 minutes",
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
  "grades": [
    {
      "file": "data/eval/english_shadow_1600_machine_20260908.jsonl",
      "row": 1212,
      "variant": "question",
      "id": "EN-SHADOW-1213",
      "passed": false,
      "failures": [
        "route:knowledge expected:['service_fee']",
        "legacy_english_thai_prose_flag"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": null,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['service_fee']"
        ],
        "content_or_format": [
          "legacy_english_thai_prose_flag"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    }
  ]
}
```


## 0f5e0fd0f7f40fed2280aa84538bf0cbe41bd47c2924eaeed55a495188465322

กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า มีเมาส์เกใมิ่งให้ไหม

### Legacy_R64_saved

```text
มีอุปกรณ์ที่ยืนยันได้ดังนี้ครับ
•    Gaming Mouse อยู่ใน PC Zone
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home
```

### R115_saved

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

### R118_revision02_saved

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### R119_revision01

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### R119_revision02

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### แผนและหลักฐานที่เลือก

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
      "id": "0cf02481e06a418bbc9690df0e011ea5",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า มีเมาส์เกใมิ่งให้ไหม\", \"operation\": \"availability\", \"domain\": \"equipment\", \"facet\": \"usage\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 2.671,
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
  "grades": [
    {
      "file": "data/eval/master_gt_bilingual_multi_error_2000_20260929_r15.jsonl",
      "row": 626,
      "variant": "noisy",
      "id": "MASTER-GT-TH-03372",
      "passed": false,
      "failures": [
        "route:knowledge expected:['equipment']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['equipment']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    }
  ]
}
```


## 104194c21fa2ded7f4d2e573457e1dbc6284cb6cb57e978bb6512df8c99a9147

หำลังจะลงแข่ง VALORANT อยากรู้เรื่องบทลงโทษ

### Legacy_R64_saved

```text

```

### R115_saved

```text
VALORANT — แนวเกม: เกมยิง Tactical FPS แบบทีม 5v5 [S1]
VALORANT — บริการที่มีเกมนี้: PC #01-#02; PC #03-#10 [S2]
VALORANT — คำอธิบายเกม: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ [S3]
VALORANT — วิธีเล่น: ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือกู้ Spike การเล่นเน้นการเล็ง การสื่อสาร การใช้สกิล และการเล่นเป็นทีม [S4]
```

### R118_revision02_saved

```text
กฎระเบียบและรูปแบบการแข่งขัน VALORANT — บทลงโทษ: เจ้าหน้าที่จะพิจารณาโทษตามเจตนา (Intent) ผลกระทบ (Impact) [S1]
```

### R119_revision01

```text
กฎระเบียบและรูปแบบการแข่งขัน VALORANT — บทลงโทษ: เจ้าหน้าที่จะพิจารณาโทษตามเจตนา (Intent) ผลกระทบ (Impact) [S1]
```

### R119_revision02

```text
กฎระเบียบและรูปแบบการแข่งขัน VALORANT — บทลงโทษ: เจ้าหน้าที่จะพิจารณาโทษตามเจตนา (Intent) ผลกระทบ (Impact) [S1]
```

### แผนและหลักฐานที่เลือก

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
      "id": "522a8b0453a64ecfa31cea6adfbe1392",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"หำลังจะลงแข่ง valorant อยากรู้เรื่องบทลงโทษ\", \"operation\": \"rule_lookup\", \"domain\": \"competition_rules\", \"facet\": \"rule_clause\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 2.031,
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
  "grades": [
    {
      "file": "data/eval/master_gt_bilingual_multi_error_2000_20260929_r15.jsonl",
      "row": 656,
      "variant": "noisy",
      "id": "MASTER-GT-TH-04244",
      "passed": false,
      "failures": [
        "route:knowledge expected:['competition_rules']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['competition_rules']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    }
  ]
}
```


## 11f9129c3b0361cac8d62bd3fdfd6bb70ad00435c97d5fbce522b4e8a4545a38

รบกวนเช็กข้อมูลของศูนย์ให้หน่อยครับ ขอข้อมูลเรื่องพบปัญหา เครื่อง

### Legacy_R64_saved

```text
หากพบปัญหาการใช้งานหรือเครื่องมีปัญหา โปรดแจ้งเจ้าหน้าที่ทันที
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

### R115_saved

```text
ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ พบปัญหา — เครื่อง เช่น คำถามตั้งต้น ไม่จำเป็นต้องเก็บทุก paraphrase / ข้อมูลที่ยืนยันได้ / หัวข้อเชิงความหมาย?
```

### R118_revision02_saved

```text
ต้องการทราบเรื่องใดเกี่ยวกับ พบปัญหา — เครื่อง ครับ? ขอรายละเอียดสถานการณ์เพิ่มอีกนิดครับ
```

### R119_revision01

```text
ต้องการทราบเรื่องใดเกี่ยวกับ พบปัญหา — เครื่อง ครับ? ขอรายละเอียดสถานการณ์เพิ่มอีกนิดครับ
```

### R119_revision02

```text
ต้องการทราบเรื่องใดเกี่ยวกับ พบปัญหา — เครื่อง ครับ? ขอรายละเอียดสถานการณ์เพิ่มอีกนิดครับ
```

### แผนและหลักฐานที่เลือก

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "validated_interpretation_proposal",
    "tasks": [
      {
        "quote": "รบกวนเช็กข้อมูลของศูนย์ให้หน่อยครับ ขอข้อมูลเรื่องพบปัญหา เครื่อง",
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
      "id": "bdaf414abadc4924ad4325ac10e31d7b",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"รบกวนเช็กข้อมูลของศูนย์ให้หน่อยครับ ขอข้อมูลเรื่องพบปัญหา เครื่อง\", \"operation\": \"general_answer\", \"domain\": \"general\", \"facet\": \"\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 2.468,
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
              "revision": 4,
              "units": null,
              "applicability": {
                "effective_from": null,
                "effective_until": null,
                "state": "unknown"
              },
              "release_id": "migration-preview-r69",
              "epoch": 2377,
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
  "grades": [
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
      "row": 3747,
      "variant": "question",
      "id": "MASTER-GT-TH-03748",
      "passed": false,
      "failures": [
        "route:knowledge expected:['rules']",
        "status:clarification expected:answer_available"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['rules']"
        ],
        "outcome": [
          "status:clarification expected:answer_available"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
      "row": 3747,
      "variant": "question",
      "id": "MASTER-GT-TH-03748",
      "passed": false,
      "failures": [
        "route:knowledge expected:['rules']",
        "status:clarification expected:answer_available"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['rules']"
        ],
        "outcome": [
          "status:clarification expected:answer_available"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_th_5000_v1.jsonl",
      "row": 3747,
      "variant": "question",
      "id": "MASTER-GT-TH-03748",
      "passed": false,
      "failures": [
        "route:knowledge expected:['rules']",
        "status:clarification expected:answer_available"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['rules']"
        ],
        "outcome": [
          "status:clarification expected:answer_available"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_th_5000_v2.jsonl",
      "row": 3747,
      "variant": "question",
      "id": "MASTER-GT-TH-03748",
      "passed": false,
      "failures": [
        "route:knowledge expected:['rules']",
        "status:clarification expected:answer_available"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['rules']"
        ],
        "outcome": [
          "status:clarification expected:answer_available"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    }
  ]
}
```


## 1f7c4f9acc3f321bb2f052679f405ebd9f9bae73ad634842a3e0f95afba60813

ขอสอบถามหน่อยครับ New Super Mario Bros. U Deluxe เล่นได้ที่โซนไหน

### Legacy_R64_saved

```text
ได้ครับ New Super Mario Bros. U Deluxe เล่นได้ที่ Nintendo Switch Zone - Nintendo Switch (1-2 Persons), Nintendo Switch Zone - Nintendo Switch (1-4 Persons)
แหล่งข้อมูล: https://esports.computing.psu.ac.th/
```

### R115_saved

```text
New Super Mario Bros. U Deluxe — บริการที่มีเกมนี้: Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons) [S1]
```

### R118_revision02_saved

```text
ยังยืนยันโซนจากความสัมพันธ์ข้อมูลไม่ได้ แต่ยืนยันบริการที่มีเกมนี้ได้ดังนี้
New Super Mario Bros. U Deluxe — บริการที่มีเกมนี้: Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons) [S1]
```

### R119_revision01

```text
New Super Mario Bros. U Deluxe — โซนที่ยืนยันว่ามีเกมนี้: Nintendo Switch Zone [S1]
```

### R119_revision02

```text
New Super Mario Bros. U Deluxe — โซนที่ยืนยันว่ามีเกมนี้: Nintendo Switch Zone [S1]
```

### แผนและหลักฐานที่เลือก

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
      "id": "1f730397a64041d99dabe10b63ba997f",
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
      "elapsed_sec": 7.282,
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
      "status": "supported",
      "reason_codes": [
        "typed_game_zone_projection"
      ],
      "receipts": [
        {
          "record_id": "game_detail_new_super_mario_bros",
          "field": "zone",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_aee35089e84c0acaa114bfd306f9"
            },
            {
              "locator": "/mapped_fields/venue_zone_ids",
              "source_id": "r68_url_7085a4eee4ef0278970d4cc4"
            },
            {
              "locator": "/mapped_fields/name",
              "source_id": "r63_65978ce05d77e443d405488570f6"
            },
            {
              "locator": "/mapped_fields/game_id",
              "source_id": "r63_dd5c64fb15c50936c875483f60a8"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_dd5c64fb15c50936c875483f60a8"
            },
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_dd5c64fb15c50936c875483f60a8"
            },
            {
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_bb06613f34063f9f3815210a0c3e"
            },
            {
              "locator": "/mapped_fields/game_id",
              "source_id": "r63_537f6eabb2fac0d78d3e28dadba9"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_537f6eabb2fac0d78d3e28dadba9"
            },
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_537f6eabb2fac0d78d3e28dadba9"
            },
            {
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_0ee2edc67d0cd1f9a3abcd97d565"
            }
          ]
        }
      ],
      "claim_packets": [
        {
          "fact_id": "C04:game_detail_new_super_mario_bros:zone",
          "record_id": "game_detail_new_super_mario_bros",
          "facet": "zone",
          "value": "Nintendo Switch Zone",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_aee35089e84c0acaa114bfd306f9"
            },
            {
              "locator": "/mapped_fields/venue_zone_ids",
              "source_id": "r68_url_7085a4eee4ef0278970d4cc4"
            },
            {
              "locator": "/mapped_fields/name",
              "source_id": "r63_65978ce05d77e443d405488570f6"
            },
            {
              "locator": "/mapped_fields/game_id",
              "source_id": "r63_dd5c64fb15c50936c875483f60a8"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_dd5c64fb15c50936c875483f60a8"
            },
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_dd5c64fb15c50936c875483f60a8"
            },
            {
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_bb06613f34063f9f3815210a0c3e"
            },
            {
              "locator": "/mapped_fields/game_id",
              "source_id": "r63_537f6eabb2fac0d78d3e28dadba9"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_537f6eabb2fac0d78d3e28dadba9"
            },
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_537f6eabb2fac0d78d3e28dadba9"
            },
            {
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_0ee2edc67d0cd1f9a3abcd97d565"
            }
          ],
          "fixture": false,
          "status": "answer"
        }
      ],
      "semantic_correctness_verified": false
    }
  ],
  "grades": [
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
      "row": 2395,
      "variant": "question",
      "id": "MASTER-GT-TH-02396",
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
      "row": 2395,
      "variant": "question",
      "id": "MASTER-GT-TH-02396",
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
      "row": 2395,
      "variant": "question",
      "id": "MASTER-GT-TH-02396",
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
      "row": 2395,
      "variant": "question",
      "id": "MASTER-GT-TH-02396",
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


## 2204b0a8c1dcc11cbd923870f71f83a322743817cf363f87ab147b4a1ed481c8

ขอข้อมูลเรื่องวันศุกร์ maintenance

### Legacy_R64_saved

```text
วันและช่วงเวลาให้บริการตามตารางปกติ (ไม่ใช่สถานะเครื่องว่างแบบสด):
•    วันจันทร์: เปิด 13:00-16:00; Maintenance 09:00-12:00
•    วันอังคาร-พฤหัสบดี: เปิด 09:00-12:00, 13:00-16:00
•    วันศุกร์: เปิด 09:00-12:00; Maintenance 13:00-16:00
•    วันเสาร์-อาทิตย์: ไม่มีรอบให้บริการหรือจองตามตารางปกติ
วันปิดพิเศษมีผลก่อนตารางปกติ และช่วงที่เปิดไม่ได้ยืนยันว่าเครื่องยังว่างครับ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

### R115_saved

```text
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
ศุกร์ — ช่วงบำรุงรักษา: 13:00–16:00 [S1]
```

### R118_revision02_saved

```text
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
ศุกร์ — ช่วงบำรุงรักษา: 13:00–16:00 [S1]
```

### R119_revision01

```text
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
ศุกร์ — ช่วงบำรุงรักษา: 13:00–16:00 [S1]
```

### R119_revision02

```text
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
ศุกร์ — ช่วงบำรุงรักษา: 13:00–16:00 [S1]
```

### แผนและหลักฐานที่เลือก

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
      "id": "2fef7a6731304c20bb8c60c902970dea",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"ขอข้อมูลเรื่องวันศุกร์ maintenance\", \"operation\": \"schedule_lookup\", \"domain\": \"schedule\", \"facet\": \"maintenance_periods\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 1.969,
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
  "grades": [
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
      "row": 416,
      "variant": "question",
      "id": "MASTER-GT-TH-00417",
      "passed": false,
      "failures": [
        "route:knowledge expected:['reservation']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['reservation']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
      "row": 1261,
      "variant": "question",
      "id": "MASTER-GT-TH-01262",
      "passed": false,
      "failures": [
        "route:knowledge expected:['reservation', 'schedule']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['reservation', 'schedule']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_th_5000_v1.jsonl",
      "row": 416,
      "variant": "question",
      "id": "MASTER-GT-TH-00417",
      "passed": false,
      "failures": [
        "route:knowledge expected:['reservation']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['reservation']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_th_5000_v2.jsonl",
      "row": 1261,
      "variant": "question",
      "id": "MASTER-GT-TH-01262",
      "passed": false,
      "failures": [
        "route:knowledge expected:['reservation', 'schedule']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['reservation', 'schedule']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    }
  ]
}
```


## 2c110689509d6996841eec18c40041b694e32f32454d3bb7453a15507e5c4ba7

ขอสอบถามหน่อยครับ ขอข้อมูลที่ยืนยันได้หน่อยครับ: pc2 available ตอน 3pm ไหม

### Legacy_R64_saved

```text
วันที่ 2026-10-14 (เวลาไทย) ยังยืนยันสถานะเปิด-ปิดและ Slot แบบสดไม่ได้ เพราะการเชื่อมต่อระบบจองยังไม่พร้อมใช้งานครับ
ผมจะไม่เอาตารางเก่ามาแสดงว่าเป็นข้อมูลจองแบบสด กรุณาลองใหม่อีกครั้งหรือดูหน้าจองโดยตรง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

### R115_saved

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### R118_revision02_saved

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### R119_revision01

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### R119_revision02

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### แผนและหลักฐานที่เลือก

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
      "id": "14e8c23eba374c98ae75312eb38f9d32",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": false,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"pc2 available ตอน 3pm ไหม\", \"operation\": \"availability\", \"domain\": \"games\", \"facet\": \"live_status\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "meaning_review": {
        "basis": "dated_named_resource_availability",
        "model_plan_accepted": false,
        "model_reason": "facet_domain_mismatch",
        "prior_tasks": [],
        "business_facts_added": false
      },
      "reason": "independent_context_frame",
      "elapsed_sec": 1.938,
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
  "grades": [
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
      "row": 525,
      "variant": "question",
      "id": "MASTER-GT-TH-00526",
      "passed": false,
      "failures": [
        "route:knowledge expected:['reservation']",
        "status:answer expected:live_lookup_required"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['reservation']"
        ],
        "outcome": [
          "status:answer expected:live_lookup_required"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
      "row": 505,
      "variant": "question",
      "id": "MASTER-GT-TH-00506",
      "passed": false,
      "failures": [
        "route:knowledge expected:['reservation', 'schedule']",
        "status:answer expected:live_lookup_required"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['reservation', 'schedule']"
        ],
        "outcome": [
          "status:answer expected:live_lookup_required"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_th_5000_v1.jsonl",
      "row": 525,
      "variant": "question",
      "id": "MASTER-GT-TH-00526",
      "passed": false,
      "failures": [
        "route:knowledge expected:['reservation']",
        "status:answer expected:live_lookup_required"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['reservation']"
        ],
        "outcome": [
          "status:answer expected:live_lookup_required"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_th_5000_v2.jsonl",
      "row": 505,
      "variant": "question",
      "id": "MASTER-GT-TH-00506",
      "passed": false,
      "failures": [
        "route:knowledge expected:['reservation', 'schedule']",
        "status:answer expected:live_lookup_required"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['reservation', 'schedule']"
        ],
        "outcome": [
          "status:answer expected:live_lookup_required"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    }
  ]
}
```


## 2ee7827caaaac21d3837cb4dd86c4e955dd51f018520dfc6f024a287bc9dd91e

What position does Ms. Kamlawan Nuansai hold

### Legacy_R64_saved

```text
I could not verify a member record for Ms. Kamlawan Nuansai. Please provide the exact name from the official member directory; I cannot infer an official identity from an unverified English spelling.
```

### R115_saved

```text
**Relevant information**
• Confirmed information: In cases where a user commits serious rule violations or repeatedly violates the rules, such as damaging property or engaging in behavior that poses a threat to others' safety, the user may have their account privileges permanently suspended. [S1]
• topic: penalty [S2]

English translation is machine generated and has not been reviewed by the owner.
```

### R118_revision02_saved

```text
No confirmed source is available for the requested detail.
```

### R119_revision01

```text
According to the recorded source profile:
นางสาวกมลวรรณ นวลสาย — role: Committee member [S1]
```

### R119_revision02

```text
According to the recorded source profile:
นางสาวกมลวรรณ นวลสาย — role: Committee member [S1]
```

### แผนและหลักฐานที่เลือก

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
      "id": "9c9fc13091824d1f917ee1c78fc8ff45",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"what position does ms. kamlawan nuansai hold\", \"operation\": \"role_lookup\", \"domain\": \"members\", \"facet\": \"role\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 1.843,
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
      "status": "supported",
      "reason_codes": [
        "typed_requested_fields"
      ],
      "receipts": [
        {
          "record_id": "member_18a751d710b9b30c",
          "field": "role",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/role",
              "source_id": "r66_person_review_2f81ce5b9ffc69ed803bc905"
            }
          ]
        }
      ],
      "claim_packets": [
        {
          "fact_id": "C02:member_18a751d710b9b30c:role",
          "record_id": "member_18a751d710b9b30c",
          "facet": "role",
          "value": "Committee member",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/role",
              "source_id": "r66_person_review_2f81ce5b9ffc69ed803bc905"
            }
          ],
          "fixture": false,
          "status": "answer"
        }
      ],
      "semantic_correctness_verified": false
    }
  ],
  "grades": [
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
      "row": 9629,
      "variant": "question",
      "id": "MASTER-GT-EN-04630",
      "passed": false,
      "failures": [
        "route:knowledge expected:['members', 'overview']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['members', 'overview']"
        ]
      },
      "positive_literal": false,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
      "row": 9629,
      "variant": "question",
      "id": "MASTER-GT-EN-04630",
      "passed": false,
      "failures": [
        "route:knowledge expected:['members', 'overview']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['members', 'overview']"
        ]
      },
      "positive_literal": false,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_en_5000_v1.jsonl",
      "row": 4629,
      "variant": "question",
      "id": "MASTER-GT-EN-04630",
      "passed": false,
      "failures": [
        "route:knowledge expected:['members', 'overview']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['members', 'overview']"
        ]
      },
      "positive_literal": false,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_en_5000_v2.jsonl",
      "row": 4629,
      "variant": "question",
      "id": "MASTER-GT-EN-04630",
      "passed": false,
      "failures": [
        "route:knowledge expected:['members', 'overview']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['members', 'overview']"
        ]
      },
      "positive_literal": false,
      "literal_passed": true,
      "literal_errors": []
    }
  ]
}
```


## 3020765f9449c4044241f3945cf7241a89f090e4742bdab7592f7504bc36f074

ขอสอบถมหนาอยครับ ศูนย์อยู่ที่ไหน อะ

### Legacy_R64_saved

```text
ศูนย์อยู่ที่อาคาร 5 ชั้น 1 มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต 80 หมู่ 1 ถ.วิชิตสงคราม อ.กะทู้ จ.ภูเก็ต 83120 ครับ

แหล่งข้อมูล: คำตอบที่ผู้ใช้ยืนยัน (2026-10-08)

local://service_policy/user_answers_20261008
```

### R115_saved

```text
PSU Esports Studio - Phuket — ที่อยู่: ศูนย์อยู่ที่อาคาร 5 ชั้น 1 มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต 80 หมู่ 1 ถ.วิชิตสงคราม อ.กะทู้ จ.ภูเก็ต 83120ครับ [S1]
ที่จอดรถ — ที่ตั้ง: หน้าตึก 5 [S2]
ที่นั่งพัก — ที่ตั้ง: โซนกลางห้อง [S3]
```

### R118_revision02_saved

```text
**PSU Esports Studio - Phuket**
• ที่อยู่เต็ม: ศูนย์อยู่ที่อาคาร 5 ชั้น 1 มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต 80 หมู่ 1 ถ.วิชิตสงคราม อ.กะทู้ จ.ภูเก็ต 83120ครับ [S1]
```

### R119_revision01

```text
**PSU Esports Studio - Phuket**
• ที่อยู่เต็ม: ศูนย์อยู่ที่อาคาร 5 ชั้น 1 มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต 80 หมู่ 1 ถ.วิชิตสงคราม อ.กะทู้ จ.ภูเก็ต 83120ครับ [S1]
```

### R119_revision02

```text
**PSU Esports Studio - Phuket**
• ที่อยู่เต็ม: ศูนย์อยู่ที่อาคาร 5 ชั้น 1 มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต 80 หมู่ 1 ถ.วิชิตสงคราม อ.กะทู้ จ.ภูเก็ต 83120ครับ [S1]
```

### แผนและหลักฐานที่เลือก

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
        "operation": "general_answer",
        "facet": "",
        "target": "",
        "constraints": [],
        "ambiguous": false
      }
    ],
    "event": {
      "id": "b1243ebead824aae87269f565e9c05fa",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"ขอสอบถมหนาอยครับ ศูนย์อยู่ที่ไหน อะ\", \"operation\": \"general_answer\", \"domain\": \"general\", \"facet\": \"\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 2.172,
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
              "epoch": 2377,
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
          "epoch": 2377,
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
  "grades": [
    {
      "file": "data/eval/master_gt_bilingual_multi_error_2000_20260929_r15.jsonl",
      "row": 779,
      "variant": "noisy",
      "id": "MASTER-GT-TH-04707",
      "passed": false,
      "failures": [
        "route:knowledge expected:['contact', 'overview']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['contact', 'overview']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    }
  ]
}
```


## 36c239903ef9b2645e840586a9db999016c64405aefcfc4914ba3d20f2ecdcdf

กำลังวางแผนไปใช้บริการ เลยอยากทราบว่า ต้องการจองเครื่องทำยังไง อะ

### Legacy_R64_saved

```text
ขั้นตอนจองโดยสรุป:
•    เลือกบริการหรือโซนที่ต้องการใช้
•    เลือกวันและรอบเวลาที่ต้องการ
•    กรอก Student ID/Staff ID/National ID, ชื่อ, นามสกุล, อีเมล และเบอร์โทรศัพท์
•    ตรวจสอบข้อมูลและชำระเงินโดยโอนเข้าบัญชีที่ระบบแจ้ง
•    หลังจองต้องชำระเงินภายใน 10 นาที
•    แนบสลิปและยืนยันการจอง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/
```

### R115_saved

```text
**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: ขั้นตอนการจองคือ เลือกบริการที่ต้องการ เลือกวันและเวลา กรอกข้อมูลผู้ใช้บริการ ตรวจสอบข้อมูล ชำระเงินโดยโอนเข้าบัญชีธนาคาร และแนบสลิปการโอนเงิน [S1]
```

### R118_revision02_saved

```text
ขั้นตอนการจอง — คำตอบที่ยืนยัน: ขั้นตอนการจองคือ เลือกบริการที่ต้องการ เลือกวันและเวลา กรอกข้อมูลผู้ใช้บริการ ตรวจสอบข้อมูล ชำระเงินโดยโอนเข้าบัญชีธนาคาร และแนบสลิปการโอนเงิน [S1]
```

### R119_revision01

```text
ขั้นตอนการจอง — คำตอบที่ยืนยัน: ขั้นตอนการจองคือ เลือกบริการที่ต้องการ เลือกวันและเวลา กรอกข้อมูลผู้ใช้บริการ ตรวจสอบข้อมูล ชำระเงินโดยโอนเข้าบัญชีธนาคาร และแนบสลิปการโอนเงิน [S1]
```

### R119_revision02

```text
ขั้นตอนการจอง — คำตอบที่ยืนยัน: ขั้นตอนการจองคือ เลือกบริการที่ต้องการ เลือกวันและเวลา กรอกข้อมูลผู้ใช้บริการ ตรวจสอบข้อมูล ชำระเงินโดยโอนเข้าบัญชีธนาคาร และแนบสลิปการโอนเงิน [S1]
```

### แผนและหลักฐานที่เลือก

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
      "id": "9f69e357e16f48278fb6354265e2072d",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": false,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"ต้องการจองเครื่องทำยังไง อะ\", \"operation\": \"how_to\", \"domain\": \"equipment\", \"facet\": \"how_to_play\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "meaning_review": {
        "basis": "booking_action_before_game_context",
        "model_plan_accepted": false,
        "model_reason": "facet_domain_mismatch",
        "prior_tasks": [],
        "business_facts_added": false
      },
      "reason": "independent_context_frame",
      "elapsed_sec": 2.531,
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
  "grades": [
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
      "row": 655,
      "variant": "question",
      "id": "MASTER-GT-TH-00656",
      "passed": false,
      "failures": [
        "route:knowledge expected:['reservation']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['reservation']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
      "row": 615,
      "variant": "question",
      "id": "MASTER-GT-TH-00616",
      "passed": false,
      "failures": [
        "route:knowledge expected:['reservation']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['reservation']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_th_5000_v1.jsonl",
      "row": 655,
      "variant": "question",
      "id": "MASTER-GT-TH-00656",
      "passed": false,
      "failures": [
        "route:knowledge expected:['reservation']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['reservation']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_th_5000_v2.jsonl",
      "row": 615,
      "variant": "question",
      "id": "MASTER-GT-TH-00616",
      "passed": false,
      "failures": [
        "route:knowledge expected:['reservation']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['reservation']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    }
  ]
}
```


## 3a769b080c6e4d2fac6862c843d20940c534c0633656de70c192903617523146

กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า VALORANT คือเกมอะไร

### Legacy_R64_saved

```text
VALORANT: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ
แนวเกม: เกมยิง Tactical FPS แบบทีม 5v5
วิธีเล่นโดยสรุป: ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือกู้ Spike การเล่นเน้นการเล็ง การสื่อสาร การใช้สกิล และการเล่นเป็นทีม
เล่นได้ที่: PC Zone
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
```

### R115_saved

```text
VALORANT — คำอธิบายเกม: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ [S1]
```

### R118_revision02_saved

```text
VALORANT — คำอธิบายเกม: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ [S1]
```

### R119_revision01

```text
VALORANT — คำอธิบายเกม: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ [S1]
```

### R119_revision02

```text
VALORANT — คำอธิบายเกม: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ [S1]
```

### แผนและหลักฐานที่เลือก

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
      "id": "1f50748b5f7b45ab8b3f34a0788991aa",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"valorant คือเกมอะไร\", \"operation\": \"unknown\", \"domain\": \"games\", \"facet\": \"game_catalog\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "meaning_review": {
        "basis": "current_game_and_definition_request",
        "model_plan_accepted": true,
        "model_reason": "validated_interpretation_proposal",
        "prior_tasks": [
          {
            "quote": "valorant คือเกมอะไร",
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
      "elapsed_sec": 7.156,
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
  "grades": [
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
      "row": 2309,
      "variant": "question",
      "id": "MASTER-GT-TH-02310",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
      "row": 2309,
      "variant": "question",
      "id": "MASTER-GT-TH-02310",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_th_5000_v1.jsonl",
      "row": 2309,
      "variant": "question",
      "id": "MASTER-GT-TH-02310",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_th_5000_v2.jsonl",
      "row": 2309,
      "variant": "question",
      "id": "MASTER-GT-TH-02310",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/rag_robustness_ground_truth_v1.jsonl",
      "row": 26,
      "variant": "question",
      "id": "RAG-ROBUST-TH-027",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    }
  ]
}
```


## 3cc3c5c383b501e1e992101d842e35427a03a448b4211f41cb66a48820b267ea

What does the Shift + Q / W / E / R button do in League of Legends on PC

### Legacy_R64_saved

```text
League of Legends controls:
- Shift + Q / W / E / R: Quick cast abilities
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://dignitas.gg/articles/blogs/Unknown/8721/improving-inputs-effective-keybinds-for-lol
```

### R115_saved

```text
League of Legends / PC — Quick cast abilities: Shift + Q / W / E / R — Default value referenced as Shift+Q/W/E/R for quick cast [S1]
```

### R118_revision02_saved

```text
League of Legends / PC — Quick cast abilities: Shift + Q / W / E / R — Default value referenced as Shift+Q/W/E/R for quick cast [S1]
```

### R119_revision01

```text
League of Legends / PC — Quick cast abilities: Shift + Q / W / E / R — Default value referenced as Shift+Q/W/E/R for quick cast [S1]
```

### R119_revision02

```text
League of Legends / PC — Quick cast abilities: Shift + Q / W / E / R — Default value referenced as Shift+Q/W/E/R for quick cast [S1]
```

### แผนและหลักฐานที่เลือก

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
      "id": "17c3a6904e6248bea282933263bcbd82",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"what does the shift + q / w / e / r button do in league of legends on pc\", \"operation\": \"detail\", \"domain\": \"games\", \"facet\": \"game_catalog\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
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
            "facet": "game_catalog",
            "target": "",
            "constraints": [],
            "ambiguous": false
          }
        ],
        "business_facts_added": false
      },
      "reason": "independent_context_frame",
      "elapsed_sec": 1.969,
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
  "grades": [
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


## 3df1eea3e83aa3fb059025c57f1a6063ac223379a543d818ffc26146c42c59ae

Please answer from verified studio information: Which zone has the Gaming Chair

### Legacy_R64_saved

```text
Verified equipment record: Gaming Chair is listed in PC Zone.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)
```

### R115_saved

```text
Gaming Chair — location: PC Zone [S1]
```

### R118_revision02_saved

```text
Gaming Chair — location: PC Zone [S1]
```

### R119_revision01

```text
pc zone.*equipment — confirmed answer: The PC Zone has 10 Gaming Monitors, 10 Gaming Chairs, Gaming Keyboards, Gaming Headsets, Gaming Mice, and 10 MSI MAG Infinite S3 14th Gaming PCs. [S1]
```

### R119_revision02

```text
Gaming Chair — location: PC Zone [S1]
```

### แผนและหลักฐานที่เลือก

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
      "id": "9129dd743f864d4a9e86890fcd6e01c0",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"which zone has the gaming chair\", \"operation\": \"unknown\", \"domain\": \"equipment\", \"facet\": \"location\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 1.735,
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
  "grades": [
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


## 4b0fb4a4344134b1f575032bdf52be169e19f555edfefbda347310760b6c859d

I am preparing for a AOV match. What is the policy for competition equipment and devices

### Legacy_R64_saved

```text

```

### R115_saved

```text
Please specify the item and requested time.
```

### R118_revision02_saved

```text
Please specify the tournament or rulebook edition so I can match the rule you are asking about.
```

### R119_revision01

```text
Please specify the tournament or rulebook edition so I can match the rule you are asking about.
```

### R119_revision02

```text
Please specify the tournament or rulebook edition so I can match the rule you are asking about.
```

### แผนและหลักฐานที่เลือก

```json
{
  "understanding": {
    "version": "r117",
    "accepted": true,
    "reason": "validated_interpretation_proposal",
    "tasks": [
      {
        "quote": "what is the policy for competition equipment and devices",
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
      "id": "8c09d34a415b4468ae2fae48c56f79c9",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"what is the policy for competition equipment and devices\", \"operation\": \"rule_lookup\", \"domain\": \"competition_rules\", \"facet\": \"rule_clause\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 1.844,
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
      "source_span": "what is the policy for competition equipment and devices",
      "execution_query": "what is the policy for competition equipment and devices ",
      "status": "needs_user_slot",
      "reason_codes": [
        "event_or_rule_not_bound"
      ],
      "receipts": [],
      "claim_packets": [],
      "semantic_correctness_verified": false
    }
  ],
  "grades": [
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
      "row": 9128,
      "variant": "question",
      "id": "MASTER-GT-EN-04129",
      "passed": false,
      "failures": [
        "route:knowledge expected:['competition_rules']",
        "status:clarification expected:answer_available"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['competition_rules']"
        ],
        "outcome": [
          "status:clarification expected:answer_available"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
      "row": 9128,
      "variant": "question",
      "id": "MASTER-GT-EN-04129",
      "passed": false,
      "failures": [
        "route:knowledge expected:['competition_rules']",
        "status:clarification expected:answer_available"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['competition_rules']"
        ],
        "outcome": [
          "status:clarification expected:answer_available"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_en_5000_v1.jsonl",
      "row": 4128,
      "variant": "question",
      "id": "MASTER-GT-EN-04129",
      "passed": false,
      "failures": [
        "route:knowledge expected:['competition_rules']",
        "status:clarification expected:answer_available"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['competition_rules']"
        ],
        "outcome": [
          "status:clarification expected:answer_available"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_en_5000_v2.jsonl",
      "row": 4128,
      "variant": "question",
      "id": "MASTER-GT-EN-04129",
      "passed": false,
      "failures": [
        "route:knowledge expected:['competition_rules']",
        "status:clarification expected:answer_available"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['competition_rules']"
        ],
        "outcome": [
          "status:clarification expected:answer_available"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    }
  ]
}
```


## 546c449056ffc350efa88ef0bd5a4b8957fd870fc8d94a2b77700032f0c79ae9

How much does Beat Saber cost

### Legacy_R64_saved

```text
The question does not specify the duration, so both verified packages are shown.
VR - 30 minutes (1-5 people)
- PSU students and staff: 0 THB
- PSU alumni and students from other institutions: 190 THB
- General adults: 525 THB
VR - 1 hour (1-5 people)
- PSU students and staff: 0 THB
- PSU alumni and students from other institutions: 375 THB
- General adults: 1,050 THB
Prices are calculated deterministically from the Service Fee 2026 table.
Source: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (original source in Thai)
```

### R115_saved

```text
Rates last reaffirmed by the owner on 2026-10-20; no new effective interval was established.
VR Station 30 นาที / PSU Student and Staff — per-person price for the rate duration: 0 THB per person for 30 minutes [S1]
VR Station 30 นาที / PSU Alumni and General Student — per-person price for the rate duration: 190 THB per person for 30 minutes [S2]
VR Station 30 นาที / General Adult — per-person price for the rate duration: 525 THB per person for 30 minutes [S3]
VR Station 1 ชั่วโมง / PSU Student and Staff — per-person price for the rate duration: 0 THB per person for 60 minutes [S4]
VR Station 1 ชั่วโมง / PSU Alumni and General Student — per-person price for the rate duration: 375 THB per person for 60 minutes [S5]
VR Station 1 ชั่วโมง / General Adult — per-person price for the rate duration: 1050 THB per person for 60 minutes [S6]
```

### R118_revision02_saved

```text
No confirmed source is available for the requested detail.
```

### R119_revision01

```text
VR glasses.*horizon — confirmed answer: VR Station games include Beat Saber and Horizon Call of the Mountain. [S1]
```

### R119_revision02

```text
confirmed answer: VR Station games include Beat Saber and Horizon Call of the Mountain. [S1]
```

### แผนและหลักฐานที่เลือก

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
      "id": "447897cbf6ea4e6c9945cf54479de50e",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"how much does beat saber cost\", \"operation\": \"detail\", \"domain\": \"games\", \"facet\": \"game_catalog\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 1.843,
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
      "status": "supported",
      "reason_codes": [
        "declared_legacy_query_profile"
      ],
      "receipts": [
        {
          "record_id": "migrated_faq_rule_vr_specific_games",
          "field": "answer",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/answer",
              "source_id": "r63_bf8fbedc035d62fa423c09dc2b9f"
            }
          ]
        }
      ],
      "claim_packets": [
        {
          "fact_id": "C04:migrated_faq_rule_vr_specific_games:owner_policy",
          "record_id": "migrated_faq_rule_vr_specific_games",
          "facet": "owner_policy",
          "value": "VR Station games include Beat Saber and Horizon Call of the Mountain.",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/answer",
              "source_id": "r63_bf8fbedc035d62fa423c09dc2b9f"
            }
          ],
          "fixture": false,
          "status": "answer"
        }
      ],
      "semantic_correctness_verified": false
    }
  ],
  "grades": [
    {
      "file": "data/eval/english_shadow_1600_machine_20260908.jsonl",
      "row": 67,
      "variant": "question",
      "id": "EN-SHADOW-0068",
      "passed": false,
      "failures": [
        "route:knowledge expected:['service_fee']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": null,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['service_fee']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
      "row": 5133,
      "variant": "question",
      "id": "MASTER-GT-EN-00134",
      "passed": false,
      "failures": [
        "route:knowledge expected:['service_fee']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['service_fee']"
        ]
      },
      "positive_literal": false,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
      "row": 5133,
      "variant": "question",
      "id": "MASTER-GT-EN-00134",
      "passed": false,
      "failures": [
        "route:knowledge expected:['service_fee']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['service_fee']"
        ]
      },
      "positive_literal": false,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_en_5000_v1.jsonl",
      "row": 133,
      "variant": "question",
      "id": "MASTER-GT-EN-00134",
      "passed": false,
      "failures": [
        "route:knowledge expected:['service_fee']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['service_fee']"
        ]
      },
      "positive_literal": false,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_en_5000_v2.jsonl",
      "row": 133,
      "variant": "question",
      "id": "MASTER-GT-EN-00134",
      "passed": false,
      "failures": [
        "route:knowledge expected:['service_fee']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['service_fee']"
        ]
      },
      "positive_literal": false,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_gt_bilingual_multi_error_2000_20260929_r15.jsonl",
      "row": 1712,
      "variant": "clean",
      "id": "MASTER-GT-EN-00134",
      "passed": false,
      "failures": [
        "route:knowledge expected:['service_fee']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['service_fee']"
        ]
      },
      "positive_literal": false,
      "literal_passed": true,
      "literal_errors": []
    }
  ]
}
```


## 5b2d0e1344332824fb7bb1565e2eb07efde375061314bb3e784fd9becd7abc28

Can I play Beat Saber in the VR Zone? Please answer briefly

### Legacy_R64_saved

```text
Beat Saber is available on: VR Station 30 minutes, VR Station 1 hour. Studio zone(s): VR Zone.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)
```

### R115_saved

```text
Beat Saber — studio services offering this game: VR Station 30 นาที; VR Station 1 ชั่วโมง [S1]
```

### R118_revision02_saved

```text
The zone relation is not confirmed; the following studio services are confirmed to offer this game.
Beat Saber — studio services offering this game: VR Station 30 นาที; VR Station 1 ชั่วโมง [S1]
```

### R119_revision01

```text
VR glasses.*horizon — confirmed answer: VR Station games include Beat Saber and Horizon Call of the Mountain. [S1]
```

### R119_revision02

```text
confirmed answer: VR Station games include Beat Saber and Horizon Call of the Mountain. [S1]
```

### แผนและหลักฐานที่เลือก

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
      "id": "ae588e6e4bd849dca9adc1dddf76c4d3",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"can i play beat saber in the vr zone?\", \"operation\": \"detail\", \"domain\": \"games\", \"facet\": \"zone\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 1.937,
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
      "status": "supported",
      "reason_codes": [
        "declared_legacy_query_profile"
      ],
      "receipts": [
        {
          "record_id": "migrated_faq_rule_vr_specific_games",
          "field": "answer",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/answer",
              "source_id": "r63_bf8fbedc035d62fa423c09dc2b9f"
            }
          ]
        }
      ],
      "claim_packets": [
        {
          "fact_id": "C04:migrated_faq_rule_vr_specific_games:owner_policy",
          "record_id": "migrated_faq_rule_vr_specific_games",
          "facet": "owner_policy",
          "value": "VR Station games include Beat Saber and Horizon Call of the Mountain.",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/answer",
              "source_id": "r63_bf8fbedc035d62fa423c09dc2b9f"
            }
          ],
          "fixture": false,
          "status": "answer"
        }
      ],
      "semantic_correctness_verified": false
    }
  ],
  "grades": [
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


## 69812416b4c4bda6fc2c08556eabfa8117b4ec25eb72a7ebe7eeec11deac4d58

ช่วยตอบจากข้อมูลที่ยืนยันได้หน่อย: ตอนนี้ศูนย์เปิดมั้ย

### Legacy_R64_saved

```text
ตอนนี้ยังเล่นไม่ได้ครับ รอบเปิดถัดไปของวันนี้คือ Morning 09:00-12:00
เวลาระบบ: 03:56 น. วันที่ 14/10/2026 (วันพุธ) ตามเวลาไทย

ตารางประจำที่ใช้ตรวจ:
•    วันจันทร์: 09:00-12:00 Maintenance*, 13:00-16:00 เปิดให้บริการ
•    วันอังคาร-พฤหัสบดี: 09:00-12:00 และ 13:00-16:00 เปิดให้บริการ
•    วันศุกร์: 09:00-12:00 เปิดให้บริการ, 13:00-16:00 Maintenance
•    วันหยุด/วันปิดพิเศษของศูนย์จะดูจากไฟล์ปิดบริการก่อนตารางประจำ
แหล่งข้อมูลตารางบริการ: https://esports.computing.psu.ac.th/reservation
```

### R115_saved

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### R118_revision02_saved

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### R119_revision01

```text
พุธ — ตารางให้บริการเล่น: วันที่ 2026-10-21 อยู่นอกช่วงให้บริการเล่นที่บันทึกไว้ [S1]
```

### R119_revision02

```text
พุธ — ตารางให้บริการเล่น: วันที่ 2026-10-21 อยู่นอกช่วงให้บริการเล่นที่บันทึกไว้ [S1]
```

### แผนและหลักฐานที่เลือก

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
      "id": "b3b432be7f7e4f7c9d3bc6c6db0b4dce",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"ตอนนี้ศูนย์เปิดมั้ย\", \"operation\": \"schedule_lookup\", \"domain\": \"schedule\", \"facet\": \"open_periods\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 2.0,
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
      "status": "supported",
      "reason_codes": [
        "recorded_play_service_calendar"
      ],
      "receipts": [
        {
          "record_id": "migrated_schedule_2",
          "field": "service_periods",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/service_slots",
              "source_id": "r119_62eb78d6057b7cba29a54d3c2f4a"
            }
          ]
        }
      ],
      "claim_packets": [
        {
          "fact_id": "C11:migrated_schedule_2:service_periods",
          "record_id": "migrated_schedule_2",
          "facet": "service_periods",
          "value": "วันที่ 2026-10-21 อยู่นอกช่วงให้บริการเล่นที่บันทึกไว้",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/service_slots",
              "source_id": "r119_62eb78d6057b7cba29a54d3c2f4a"
            }
          ],
          "fixture": false,
          "status": "answer"
        }
      ],
      "semantic_correctness_verified": false
    }
  ],
  "grades": [
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
      "row": 1385,
      "variant": "question",
      "id": "MASTER-GT-TH-01386",
      "passed": false,
      "failures": [
        "route:knowledge expected:['reservation', 'schedule']",
        "status:answer expected:live_lookup_required"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['reservation', 'schedule']"
        ],
        "outcome": [
          "status:answer expected:live_lookup_required"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
      "row": 1415,
      "variant": "question",
      "id": "MASTER-GT-TH-01416",
      "passed": false,
      "failures": [
        "route:knowledge expected:['reservation', 'schedule']",
        "status:answer expected:live_lookup_required"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['reservation', 'schedule']"
        ],
        "outcome": [
          "status:answer expected:live_lookup_required"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_th_5000_v1.jsonl",
      "row": 1385,
      "variant": "question",
      "id": "MASTER-GT-TH-01386",
      "passed": false,
      "failures": [
        "route:knowledge expected:['reservation', 'schedule']",
        "status:answer expected:live_lookup_required"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['reservation', 'schedule']"
        ],
        "outcome": [
          "status:answer expected:live_lookup_required"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_th_5000_v2.jsonl",
      "row": 1415,
      "variant": "question",
      "id": "MASTER-GT-TH-01416",
      "passed": false,
      "failures": [
        "route:knowledge expected:['reservation', 'schedule']",
        "status:answer expected:live_lookup_required"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['reservation', 'schedule']"
        ],
        "outcome": [
          "status:answer expected:live_lookup_required"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    }
  ]
}
```


## 6d26c7feeaf4f6aabd9d6dafc411b75359e43bfa789594941d80c2b94d7cd146

Can I cancel my booking? Please use verified information

### Legacy_R64_saved

```text
Cancellations must be made at least 1 hour in advance.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)
```

### R115_saved

```text
The selected source does not directly confirm the requested detail.
```

### R118_revision02_saved

```text
Cancel reservation — confirmed answer: Cancellation of reservations must be made at least 1 hour in advance. [S1]
```

### R119_revision01

```text
Cancel reservation — confirmed answer: Cancellation of reservations must be made at least 1 hour in advance. [S1]
```

### R119_revision02

```text
Cancel reservation — confirmed answer: Cancellation of reservations must be made at least 1 hour in advance. [S1]
```

### แผนและหลักฐานที่เลือก

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
      "id": "4574ea68129545388f9cd496d8a77470",
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
      "elapsed_sec": 1.844,
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
  "grades": [
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


## 6f6cb1e0e7d55a0d08670c39f2c4a858bf27008a510a7c06b6fc870765b3520e

ขอสอบถามหน่อยครับ Gaming Keyboard อยู่โซนไหน

### Legacy_R64_saved

```text
Gaming Keyboard: คีย์บอร์ดสำหรับควบคุมเกมและพิมพ์บน Gaming PC
อยู่ที่: PC Zone
ใช้สำหรับ:
•    ควบคุมเกม PC
•    พิมพ์ข้อมูล
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home
```

### R115_saved

```text
Gaming Keyboard — ที่ตั้ง: PC Zone [S1]
```

### R118_revision02_saved

```text
Gaming Keyboard — ที่ตั้ง: PC Zone [S1]
```

### R119_revision01

```text
Gaming Keyboard — ที่ตั้ง: PC Zone [S1]
```

### R119_revision02

```text
Gaming Keyboard — ที่ตั้ง: PC Zone [S1]
```

### แผนและหลักฐานที่เลือก

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
      "id": "8297836f385f4a8ba161e84c66508a4e",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"gaming keyboard อยู่โซนไหน\", \"operation\": \"unknown\", \"domain\": \"equipment\", \"facet\": \"location\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 1.89,
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
  "grades": [
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


## 790d4406db2db9773074032f548a0c38b10f5a2874ea6e57bf911dede2d57b7e

กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า วันจันทร์เช้าเปิดหรือปิด

### Legacy_R64_saved

```text
วันจันทร์: เปิดให้เล่นช่วง 13:00-16:00 ส่วน 09:00-12:00 เป็น Maintenance*

รายละเอียดจากตาราง:
•    วันจันทร์: Morning 09:00-12:00 = maintenance, Afternoon 13:00-16:00 = open
แหล่งข้อมูล: https://esports.computing.psu.ac.th/
```

### R115_saved

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

### R118_revision02_saved

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### R119_revision01

```text
จันทร์ — ตารางให้บริการเล่น: ไม่เปิดให้บริการเล่นช่วง 09:00–12:00 เนื่องจากบำรุงรักษาตามตาราง [S1]
```

### R119_revision02

```text
จันทร์ — ตารางให้บริการเล่น: ไม่เปิดให้บริการเล่นช่วง 09:00–12:00 เนื่องจากบำรุงรักษาตามตาราง [S1]
```

### แผนและหลักฐานที่เลือก

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
      "id": "41566b1f2fe34eada24a62133fcb9c31",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"วันจันทร์เช้าเปิดหรือปิด\", \"operation\": \"schedule_lookup\", \"domain\": \"schedule\", \"facet\": \"open_periods\", \"target\": \"\", \"ambiguous\": false, \"constraints\": [{\"slot\": \"date\", \"quote\": \"วันจันทร์\", \"source_record_id\": \"\"}, {\"slot\": \"time\", \"quote\": \"เช้า\", \"source_record_id\": \"\"}]}, {\"quote\": \"กำลังวางแผนจะไปใช้บริการ\", \"operation\": \"general_answer\", \"domain\": \"general\", \"facet\": \"\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 4.344,
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
      "status": "supported",
      "reason_codes": [
        "recorded_play_service_calendar"
      ],
      "receipts": [
        {
          "record_id": "migrated_schedule_0",
          "field": "service_periods",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/service_slots",
              "source_id": "r119_f603c2010874442cef87f3d422ee"
            }
          ]
        }
      ],
      "claim_packets": [
        {
          "fact_id": "C11:migrated_schedule_0:service_periods",
          "record_id": "migrated_schedule_0",
          "facet": "service_periods",
          "value": "ไม่เปิดให้บริการเล่นช่วง 09:00–12:00 เนื่องจากบำรุงรักษาตามตาราง",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/service_slots",
              "source_id": "r119_f603c2010874442cef87f3d422ee"
            }
          ],
          "fixture": false,
          "status": "answer"
        }
      ],
      "semantic_correctness_verified": false
    }
  ],
  "grades": [
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
      "row": 1270,
      "variant": "question",
      "id": "MASTER-GT-TH-01271",
      "passed": false,
      "failures": [
        "route:knowledge expected:['schedule']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['schedule']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
      "row": 1280,
      "variant": "question",
      "id": "MASTER-GT-TH-01281",
      "passed": false,
      "failures": [
        "route:knowledge expected:['schedule']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['schedule']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_th_5000_v1.jsonl",
      "row": 1270,
      "variant": "question",
      "id": "MASTER-GT-TH-01271",
      "passed": false,
      "failures": [
        "route:knowledge expected:['schedule']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['schedule']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_th_5000_v2.jsonl",
      "row": 1280,
      "variant": "question",
      "id": "MASTER-GT-TH-01281",
      "passed": false,
      "failures": [
        "route:knowledge expected:['schedule']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['schedule']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_gt_bilingual_multi_error_2000_20260929_r15.jsonl",
      "row": 808,
      "variant": "clean",
      "id": "MASTER-GT-TH-01281",
      "passed": false,
      "failures": [
        "route:knowledge expected:['schedule']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['schedule']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/rag_robustness_ground_truth_v1.jsonl",
      "row": 162,
      "variant": "question",
      "id": "RAG-ROBUST-TH-163",
      "passed": false,
      "failures": [
        "route:knowledge expected:['schedule']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['schedule']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    }
  ]
}
```


## 83ff647fde496d6bf0fae1997991043856653dbb8db4f253c79c209ee335dce5

Do I need to check in before playing VALORANT?

### Legacy_R64_saved

```text

```

### R115_saved

```text
VALORANT — how to play: The attacking team must place Spikes, while the defending team must defend areas or recover Spikes. The game emphasizes aiming, communication, skill usage, and teamwork. [S1]
```

### R118_revision02_saved

```text
Check-in in advance — confirmed answer: Users must check in before the scheduled round starts. They may check in up to 30 minutes early, and must check in prior to the round's start time. [S1]
```

### R119_revision01

```text
Check-in in advance — confirmed answer: Users must check in before the scheduled round starts. They may check in up to 30 minutes early, and must check in prior to the round's start time. [S1]
```

### R119_revision02

```text
Check-in in advance — confirmed answer: Users must check in before the scheduled round starts. They may check in up to 30 minutes early, and must check in prior to the round's start time. [S1]
```

### แผนและหลักฐานที่เลือก

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
      "id": "0518ab24b99a4558a0f3a38b6ade976b",
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
      "elapsed_sec": 2.141,
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
  "grades": [
    {
      "file": "data/eval/english_shadow_1600_machine_20260908.jsonl",
      "row": 547,
      "variant": "question",
      "id": "EN-SHADOW-0548",
      "passed": false,
      "failures": [
        "route:knowledge expected:['competition_rules']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": null,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['competition_rules']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    }
  ]
}
```


## 88b3a23be4d1646dfc07b79b19b6118016e431f6bb281f64facf06b6dc09b0bf

Could you please help me with this: I am planning a visit and nee to know: What GPU model is inside the PCs

### Legacy_R64_saved

```text
The published equipment record does not verify the GPU model inside the studio PCs.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)
```

### R115_saved

```text
I could not match this question to the migrated information. Please specify the game, device or topic you want to know about.
```

### R118_revision02_saved

```text
Gaming PC Model MSI MAG Infinite S3 14th — specifications: GPU: NVIDIA GeForce RTX 5060 8GB [S1]
```

### R119_revision01

```text
Gaming PC Model MSI MAG Infinite S3 14th — specifications: GPU: NVIDIA GeForce RTX 5060 8GB [S1]
```

### R119_revision02

```text
Gaming PC Model MSI MAG Infinite S3 14th — specifications: GPU: NVIDIA GeForce RTX 5060 8GB [S1]
```

### แผนและหลักฐานที่เลือก

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
      "id": "7659b564eaac4a7385dafc6b7e393839",
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
      "elapsed_sec": 7.093,
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
  "grades": [
    {
      "file": "data/eval/master_gt_bilingual_multi_error_2000_20260929_r15.jsonl",
      "row": 1972,
      "variant": "noisy",
      "id": "MASTER-GT-EN-03579",
      "passed": false,
      "failures": [
        "route:knowledge expected:['equipment', 'no_answer']",
        "status:answer expected:no_answer_expected"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['equipment', 'no_answer']"
        ],
        "outcome": [
          "status:answer expected:no_answer_expected"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    }
  ]
}
```


## 8acac2d360e8eac92ca9d4c4f51558a451fd9368afa41413edb043a5f783aac4

What does the R2 button do in God of War Ragnarök on PlayStation / PS5

### Legacy_R64_saved

```text
God of War Ragnarok controls:
- R2: Heavy Attack / Heavy Runic Attack (While blocking)
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://gameinputdatabase.com/game/14
```

### R115_saved

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

### R118_revision02_saved

```text
God of War Ragnarök / PlayStation / PS5 — Heavy Attack / Heavy Runic Attack (While blocking): R2 — Heavy attack or perform Heavy Rune move with L1 held [S1]
```

### R119_revision01

```text
God of War Ragnarök / PlayStation / PS5 — Heavy Attack / Heavy Runic Attack (While blocking): R2 — Heavy attack or perform Heavy Rune move with L1 held [S1]
```

### R119_revision02

```text
God of War Ragnarök / PlayStation / PS5 — Heavy Attack / Heavy Runic Attack (While blocking): R2 — Heavy attack or perform Heavy Rune move with L1 held [S1]
```

### แผนและหลักฐานที่เลือก

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
      "id": "2c8262518a6249f2b11bc7a8f19f994f",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"what does the r2 button do in god of war ragnarök on playstation / ps5\", \"operation\": \"detail\", \"domain\": \"games\", \"facet\": \"game_catalog\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
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
            "facet": "game_catalog",
            "target": "",
            "constraints": [],
            "ambiguous": false
          }
        ],
        "business_facts_added": false
      },
      "reason": "independent_context_frame",
      "elapsed_sec": 1.984,
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
  "grades": [
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


## 96ef8f719f0c2f5b3ddcc387738a20d2bb764f97b1ee6f99b347c1bcbb604516

Could you please help me with this: Do you have Hades II

### Legacy_R64_saved

```text
I could not find Hades II in the verified PSU game records. I will not substitute another game.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)
```

### R115_saved

```text
I could not match this question to the migrated information. Please specify the game, device or topic you want to know about.
```

### R118_revision02_saved

```text
No confirmed source is available for the requested detail.
```

### R119_revision01

```text
No confirmed source is available for the requested detail.
```

### R119_revision02

```text
No confirmed source is available for the requested detail.
```

### แผนและหลักฐานที่เลือก

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
      "id": "0559919dbf58441094d8e244260b48eb",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"do you have hades ii\", \"operation\": \"unknown\", \"domain\": \"games\", \"facet\": \"game_catalog\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 1.796,
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
  "grades": [
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
      "row": 7142,
      "variant": "question",
      "id": "MASTER-GT-EN-02143",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games', 'no_answer']",
        "status:answer expected:no_answer_expected"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games', 'no_answer']"
        ],
        "outcome": [
          "status:answer expected:no_answer_expected"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
      "row": 7044,
      "variant": "question",
      "id": "MASTER-GT-EN-02045",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games', 'no_answer']",
        "status:answer expected:no_answer_expected"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games', 'no_answer']"
        ],
        "outcome": [
          "status:answer expected:no_answer_expected"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_en_5000_v1.jsonl",
      "row": 2142,
      "variant": "question",
      "id": "MASTER-GT-EN-02143",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games', 'no_answer']",
        "status:answer expected:no_answer_expected"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games', 'no_answer']"
        ],
        "outcome": [
          "status:answer expected:no_answer_expected"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_en_5000_v2.jsonl",
      "row": 2044,
      "variant": "question",
      "id": "MASTER-GT-EN-02045",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games', 'no_answer']",
        "status:answer expected:no_answer_expected"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games', 'no_answer']"
        ],
        "outcome": [
          "status:answer expected:no_answer_expected"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    }
  ]
}
```


## 981fa8d411c3187b27a4d84d72c48e1557a5729e9be1e1b6e06e705a1c21ea17

ขอข้อมูลเรื่องอยู่ที่หน

### Legacy_R64_saved

```text
ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```

### R115_saved

```text
ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ อยู่ที่ไหน เช่น คำถามตั้งต้น ไม่จำเป็นต้องเก็บทุก paraphrase / ข้อมูลที่ยืนยันได้ / หัวข้อเชิงความหมาย?
```

### R118_revision02_saved

```text
ต้องการทราบเรื่องใดเกี่ยวกับ อยู่ที่ไหน ครับ? ขอรายละเอียดสถานการณ์เพิ่มอีกนิดครับ
```

### R119_revision01

```text
ต้องการทราบเรื่องใดเกี่ยวกับ อยู่ที่ไหน ครับ? ขอรายละเอียดสถานการณ์เพิ่มอีกนิดครับ
```

### R119_revision02

```text
ต้องการทราบเรื่องใดเกี่ยวกับ อยู่ที่ไหน ครับ? ขอรายละเอียดสถานการณ์เพิ่มอีกนิดครับ
```

### แผนและหลักฐานที่เลือก

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
      "id": "ad5172ce8ee74013a54826936655491e",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"ขอข้อมูลเรื่องอยู่ที่หน\", \"operation\": \"unknown\", \"domain\": \"general\", \"facet\": \"\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 1.781,
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
              "revision": 4,
              "units": null,
              "applicability": {
                "effective_from": null,
                "effective_until": null,
                "state": "unknown"
              },
              "release_id": "migration-preview-r69",
              "epoch": 2377,
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
  "grades": [
    {
      "file": "data/eval/master_gt_bilingual_multi_error_2000_20260929_r15.jsonl",
      "row": 517,
      "variant": "noisy",
      "id": "MASTER-GT-TH-04544",
      "passed": false,
      "failures": [
        "route:knowledge expected:['contact']",
        "status:clarification expected:answer_available"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['contact']"
        ],
        "outcome": [
          "status:clarification expected:answer_available"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    }
  ]
}
```


## 9be5826ba7589cd62372217790b8d41ffe79b86ed72e19bcca965576441c4da6

Counter-Strike 2 map pool ในกติกาคืออะไร

### Legacy_R64_saved

```text
คำตอบ: 1. ANCIENT, ANUBIS, DUST 2, INFERNO, MIRAGE, NUKE, TRAIN

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

### R115_saved

```text
Counter-Strike 2 — คำอธิบายเกม: Counter-Strike 2 คือเกมยิงแข่งขันแบบทีมที่แบ่งเป็นฝ่ายบุกและฝ่ายรับ โดยมีเป้าหมายหลักเกี่ยวกับการวาง/กู้ระเบิดหรือจัดการฝ่ายตรงข้าม [S1]
```

### R118_revision02_saved

```text
PSU Phuket CS2 2026 Tournament — 3. แผนที่ในการแข่งขัน: 3. แผนที่ในการแข่งขัน [S1]
กฎระเบียบและรูปแบบการแข่งขัน Counter-Strike 2 — แผนที่ในการแข่งขัน: ANCIENT, ANUBIS, DUST 2, INFERNO, MIRAGE, NUKE, TRAIN [S2]
```

### R119_revision01

```text
PSU Phuket CS2 2026 Tournament — 3. แผนที่ในการแข่งขัน: 3. แผนที่ในการแข่งขัน [S1]
กฎระเบียบและรูปแบบการแข่งขัน Counter-Strike 2 — แผนที่ในการแข่งขัน: ANCIENT, ANUBIS, DUST 2, INFERNO, MIRAGE, NUKE, TRAIN [S2]
```

### R119_revision02

```text
PSU Phuket CS2 2026 Tournament — 3. แผนที่ในการแข่งขัน: 3. แผนที่ในการแข่งขัน [S1]
กฎระเบียบและรูปแบบการแข่งขัน Counter-Strike 2 — แผนที่ในการแข่งขัน: ANCIENT, ANUBIS, DUST 2, INFERNO, MIRAGE, NUKE, TRAIN [S2]
```

### แผนและหลักฐานที่เลือก

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
      "id": "c71d03d184a04cc2b555f2549bad0a1a",
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
      "elapsed_sec": 7.562,
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
  "grades": [
    {
      "file": "data/ground_truth/ground_truth_competition_rules_v1_228.jsonl",
      "row": 20,
      "variant": "question",
      "id": "competition_v1_021",
      "passed": false,
      "failures": [
        "legacy_mode_prefix:['pipeline:competition_fact_card']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": null,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "legacy_mode_prefix:['pipeline:competition_fact_card']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    }
  ]
}
```


## 9db7acd10d57c350138db7c81ed44c1c8801e433a40a8c92391497d23d381f14

What does the X button do in The Legend of Zelda: Breath of the Wild on Nintendo Switch

### Legacy_R64_saved

```text
The Legend of Zelda: Breath of the Wild controls:
- X: Jump / Dodge (While locked)
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://gameinputdatabase.com/game/31
```

### R115_saved

```text
The Legend of Zelda: Breath of the Wild / Nintendo Switch — Jump / Dodge (While locked): X — Jump over obstacles or dodge when enemy is locked on [S1]
```

### R118_revision02_saved

```text
The Legend of Zelda: Breath of the Wild / Nintendo Switch — Jump / Dodge (While locked): X — Jump over obstacles or dodge when enemy is locked on [S1]
```

### R119_revision01

```text
The Legend of Zelda: Breath of the Wild / Nintendo Switch — Jump / Dodge (While locked): X — Jump over obstacles or dodge when enemy is locked on [S1]
```

### R119_revision02

```text
The Legend of Zelda: Breath of the Wild / Nintendo Switch — Jump / Dodge (While locked): X — Jump over obstacles or dodge when enemy is locked on [S1]
```

### แผนและหลักฐานที่เลือก

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
      "id": "aff51eaa04a34d9c91b17a2b84339966",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"what does the x button do in the legend of zelda: breath of the wild on nintendo switch\", \"operation\": \"detail\", \"domain\": \"games\", \"facet\": \"game_catalog\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
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
            "facet": "game_catalog",
            "target": "",
            "constraints": [],
            "ambiguous": false
          }
        ],
        "business_facts_added": false
      },
      "reason": "independent_context_frame",
      "elapsed_sec": 1.984,
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
  "grades": [
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


## a1c90b6efa66d5a5dba8f4bd8559db108bf0254516e7929f37346ad730e6fd53

Which studio zone has The Last of Us Part I / Part II

### Legacy_R64_saved

```text
The Last of Us Part I / Part II is listed in: PlayStation 5 Zone.
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)
```

### R115_saved

```text
The Last of Us Part I / Part II — genre: Game Genre: Action-Adventure / Survival [S1]
```

### R118_revision02_saved

```text
The Last of Us Part I — confirmed studio zones offering this game: PlayStation 5 Zone [S1]
Zone relations still unconfirmed for: The Last of Us Part II
```

### R119_revision01

```text
The Last of Us Part I — confirmed studio zones offering this game: PlayStation 5 Zone [S1]
Zone relations still unconfirmed for: The Last of Us Part II
```

### R119_revision02

```text
The Last of Us Part I — confirmed studio zones offering this game: PlayStation 5 Zone [S1]
Zone relations still unconfirmed for: The Last of Us Part II
```

### แผนและหลักฐานที่เลือก

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
      "id": "857534bcb8244a1f866627140a895c66",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"which studio zone has the last of us part i / part ii\", \"operation\": \"detail\", \"domain\": \"games\", \"facet\": \"zone\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 7.219,
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
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_dba105642fac9b5a0dd694101800"
            },
            {
              "locator": "/mapped_fields/name",
              "source_id": "r63_0f06f91de3bd8af3813677578766"
            },
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
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_2634ae0f9c80f4c2b3cf7ef479fd"
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
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_dba105642fac9b5a0dd694101800"
            },
            {
              "locator": "/mapped_fields/name",
              "source_id": "r63_0f06f91de3bd8af3813677578766"
            },
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
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_2634ae0f9c80f4c2b3cf7ef479fd"
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
  "grades": [
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


## a87e6d5866fea2f6741277c62836106d3b63f80fc9e787f9f094e3bedb00964e

Could you please help me with this: How much does Cockpit cost

### Legacy_R64_saved

```text
Service prices (recorded package rates):

Cockpit — 60 minutes/package (1 person)
• PSU students and staff: 0 THB/package
• PSU alumni / students from other institutions: 65 THB/package
• General adults: 200 THB/package
The original fee table states validity through 2026-03-31; continued validity for the requested date has not been confirmed.
Source: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

### R115_saved

```text
Rates last reaffirmed by the owner on 2026-10-20; no new effective interval was established.
Cockpit #01-#02 / PSU Student and Staff — per-person price for the rate duration: 0 THB per person for 60 minutes [S1]
Cockpit #01-#02 / PSU Alumni and General Student — per-person price for the rate duration: 65 THB per person for 60 minutes [S2]
Cockpit #01-#02 / General Adult — per-person price for the rate duration: 200 THB per person for 60 minutes [S3]
```

### R118_revision02_saved

```text
Rates last reaffirmed by the owner on 2026-10-20; no new effective interval was established.
Cockpit #01-#02 / PSU Student and Staff — per-person price for the rate duration: 0 THB per person for 60 minutes [S1]
Cockpit #01-#02 / PSU Alumni and General Student — per-person price for the rate duration: 65 THB per person for 60 minutes [S2]
Cockpit #01-#02 / General Adult — per-person price for the rate duration: 200 THB per person for 60 minutes [S3]
```

### R119_revision01

```text
Rates last reaffirmed by the owner on 2026-10-20; no new effective interval was established.
Cockpit #01-#02 / PSU Student and Staff — per-person price for the rate duration: 0 THB per person for 60 minutes [S1]
Cockpit #01-#02 / PSU Alumni and General Student — per-person price for the rate duration: 65 THB per person for 60 minutes [S2]
Cockpit #01-#02 / General Adult — per-person price for the rate duration: 200 THB per person for 60 minutes [S3]
```

### R119_revision02

```text
Rates last reaffirmed by the owner on 2026-10-20; no new effective interval was established.
Cockpit #01-#02 / PSU Student and Staff — per-person price for the rate duration: 0 THB per person for 60 minutes [S1]
Cockpit #01-#02 / PSU Alumni and General Student — per-person price for the rate duration: 65 THB per person for 60 minutes [S2]
Cockpit #01-#02 / General Adult — per-person price for the rate duration: 200 THB per person for 60 minutes [S3]
```

### แผนและหลักฐานที่เลือก

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
      "id": "b99c771f03fc4128b325a53d308fd8f1",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"how much does cockpit cost\", \"operation\": \"price_calculate\", \"domain\": \"service_fee\", \"facet\": \"amount\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 1.843,
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
  "grades": [
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
      "row": 5387,
      "variant": "question",
      "id": "MASTER-GT-EN-00388",
      "passed": false,
      "failures": [
        "route:knowledge expected:['service_fee']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['service_fee']"
        ]
      },
      "positive_literal": false,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
      "row": 5387,
      "variant": "question",
      "id": "MASTER-GT-EN-00388",
      "passed": false,
      "failures": [
        "route:knowledge expected:['service_fee']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['service_fee']"
        ]
      },
      "positive_literal": false,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_en_5000_v1.jsonl",
      "row": 387,
      "variant": "question",
      "id": "MASTER-GT-EN-00388",
      "passed": false,
      "failures": [
        "route:knowledge expected:['service_fee']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['service_fee']"
        ]
      },
      "positive_literal": false,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_en_5000_v2.jsonl",
      "row": 387,
      "variant": "question",
      "id": "MASTER-GT-EN-00388",
      "passed": false,
      "failures": [
        "route:knowledge expected:['service_fee']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['service_fee']"
        ]
      },
      "positive_literal": false,
      "literal_passed": true,
      "literal_errors": []
    }
  ]
}
```


## aefe99111d809f80d0b9d6893353d58fec0237e9276073fe1016557e8df464b2

ขอข้อมูลเรื่องเครื่องดื่ม พื้นที่ ครับ

### Legacy_R64_saved

```text
อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น
แหล่งข้อมูล: https://esports.computing.psu.ac.th/
```

### R115_saved

```text
บริการที่ถาม: รับประทานอาหาร

**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น [S1]
```

### R118_revision02_saved

```text
บริการที่ถาม: รับประทานอาหาร

**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น [S1]
```

### R119_revision01

```text
บริการที่ถาม: รับประทานอาหาร

**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น [S1]
```

### R119_revision02

```text
บริการที่ถาม: รับประทานอาหาร

**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น [S1]
```

### แผนและหลักฐานที่เลือก

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
      "id": "91f7a1428bec4032b8f1fe78cc097cc3",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"ขอข้อมูลเรื่องเครื่องดื่ม พื้นที่ ครับ\", \"operation\": \"rule_lookup\", \"domain\": \"general\", \"facet\": \"\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 2.078,
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
          "revision": 4,
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
            "revision": 4,
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
              "revision": 4,
              "units": null,
              "applicability": {
                "effective_from": null,
                "effective_until": null,
                "state": "unknown"
              },
              "release_id": "migration-preview-r69",
              "epoch": 2377,
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
          "revision": 4,
          "units": null,
          "applicability": {
            "effective_from": null,
            "effective_until": null,
            "state": "unknown"
          },
          "release_id": "migration-preview-r69",
          "epoch": 2377,
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
  "grades": [
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
      "row": 3849,
      "variant": "question",
      "id": "MASTER-GT-TH-03850",
      "passed": false,
      "failures": [
        "route:knowledge expected:['rules']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['rules']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
      "row": 3849,
      "variant": "question",
      "id": "MASTER-GT-TH-03850",
      "passed": false,
      "failures": [
        "route:knowledge expected:['rules']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['rules']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_th_5000_v1.jsonl",
      "row": 3849,
      "variant": "question",
      "id": "MASTER-GT-TH-03850",
      "passed": false,
      "failures": [
        "route:knowledge expected:['rules']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['rules']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_th_5000_v2.jsonl",
      "row": 3849,
      "variant": "question",
      "id": "MASTER-GT-TH-03850",
      "passed": false,
      "failures": [
        "route:knowledge expected:['rules']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['rules']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    }
  ]
}
```


## b32fb6babd0a86f30c5a9863fdc4e6cab54abe142a07ed3b5e3308a9034fb741

รบกวนเช็กข้อมูลของศูนย์ให้หน่อยครับ ศุกร์บ่ายเปิดไหม

### Legacy_R64_saved

```text
วันศุกร์: เปิดให้เล่นช่วง 09:00-12:00 ส่วน 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning

รายละเอียดจากตาราง:
•    วันศุกร์: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = maintenance
แหล่งข้อมูล: https://esports.computing.psu.ac.th/
```

### R115_saved

```text
ข้อมูลที่เชื่อมกับรายการนี้ไม่ถูกต้องหรือไม่อยู่ในขอบเขตที่อนุญาต จึงยังยืนยันคำตอบไม่ได้ครับ
```

### R118_revision02_saved

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### R119_revision01

```text
ศุกร์ — ตารางให้บริการเล่น: ไม่เปิดให้บริการเล่นช่วง 13:00–16:00 เนื่องจากบำรุงรักษาตามตาราง [S1]
```

### R119_revision02

```text
ศุกร์ — ตารางให้บริการเล่น: ไม่เปิดให้บริการเล่นช่วง 13:00–16:00 เนื่องจากบำรุงรักษาตามตาราง [S1]
```

### แผนและหลักฐานที่เลือก

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
      "id": "a3fc24a762dd4dacb61af910d6814c1a",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"ศุกร์บ่ายเปิดไหม\", \"operation\": \"schedule_lookup\", \"domain\": \"schedule\", \"facet\": \"open_periods\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}, {\"quote\": \"รบกวนเช็กข้อมูลของศูนย์ให้หน่อยครับ\", \"operation\": \"general_answer\", \"domain\": \"general\", \"facet\": \"\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 3.391,
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
      "status": "supported",
      "reason_codes": [
        "recorded_play_service_calendar"
      ],
      "receipts": [
        {
          "record_id": "migrated_schedule_4",
          "field": "service_periods",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/service_slots",
              "source_id": "r119_469008c95e51b537e25e630b4b9a"
            }
          ]
        }
      ],
      "claim_packets": [
        {
          "fact_id": "C11:migrated_schedule_4:service_periods",
          "record_id": "migrated_schedule_4",
          "facet": "service_periods",
          "value": "ไม่เปิดให้บริการเล่นช่วง 13:00–16:00 เนื่องจากบำรุงรักษาตามตาราง",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/service_slots",
              "source_id": "r119_469008c95e51b537e25e630b4b9a"
            }
          ],
          "fixture": false,
          "status": "answer"
        }
      ],
      "semantic_correctness_verified": false
    }
  ],
  "grades": [
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
      "row": 1517,
      "variant": "question",
      "id": "MASTER-GT-TH-01518",
      "passed": false,
      "failures": [
        "route:knowledge expected:['schedule']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['schedule']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
      "row": 1567,
      "variant": "question",
      "id": "MASTER-GT-TH-01568",
      "passed": false,
      "failures": [
        "route:knowledge expected:['schedule']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['schedule']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_th_5000_v1.jsonl",
      "row": 1517,
      "variant": "question",
      "id": "MASTER-GT-TH-01518",
      "passed": false,
      "failures": [
        "route:knowledge expected:['schedule']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['schedule']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_th_5000_v2.jsonl",
      "row": 1567,
      "variant": "question",
      "id": "MASTER-GT-TH-01568",
      "passed": false,
      "failures": [
        "route:knowledge expected:['schedule']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['schedule']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    }
  ]
}
```


## c43bbed1c77ced18210eb25beff0dd928a22fd9ec4417fd7df8cf0a106f1d097

ขอสอบถามหน่อยครับ บุคคลทั่วไป เล่น PC 1 ชั่วโมง เสียกี่บาท

### Legacy_R64_saved

```text
ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:

PC — 60 นาที/แพ็กเกจ (1 คน)
ระยะเวลาที่ถาม 60 นาที (1 ชั่วโมง) คิดเป็น 1 session (แพ็กเกจ)
•    บุคคลทั่วไป (General Adult): 70 บาท/แพ็กเกจ
ราคา PC อ้างอิงข้อมูลปรับปรุงในระบบวันที่ 2026-07-27
แหล่งข้อมูล: local://service_fee/pc_price_update_20260727
```

### R115_saved

```text
อัตราที่เจ้าของยืนยันล่าสุด ณ 2026-10-20 (ยังไม่ยืนยันวันเริ่ม–สิ้นสุดใหม่)
PC #01-#02 / PSU Student and Staff — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 0 บาท สำหรับ 60 นาที ตามกฎ session_ceil [S1]
PC #01-#02 / PSU Alumni and General Student — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 25 บาท สำหรับ 60 นาที ตามกฎ session_ceil [S2]
PC #01-#02 / General Adult — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 70 บาท สำหรับ 60 นาที ตามกฎ session_ceil [S3]
PC #03-#10 / PSU Student and Staff — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 0 บาท สำหรับ 60 นาที ตามกฎ session_ceil [S4]
PC #03-#10 / PSU Alumni and General Student — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 25 บาท สำหรับ 60 นาที ตามกฎ session_ceil [S5]
PC #03-#10 / General Adult — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 70 บาท สำหรับ 60 นาที ตามกฎ session_ceil [S6]
```

### R118_revision02_saved

```text
อัตราที่เจ้าของยืนยันล่าสุด ณ 2026-10-20 (ยังไม่ยืนยันวันเริ่ม–สิ้นสุดใหม่)
PC #01-#02 / General Adult — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 70 บาท สำหรับ 60 นาที ตามกฎ session_ceil [S1]
PC #03-#10 / General Adult — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 70 บาท สำหรับ 60 นาที ตามกฎ session_ceil [S2]
```

### R119_revision01

```text
อัตราที่เจ้าของยืนยันล่าสุด ณ 2026-10-20 (ยังไม่ยืนยันวันเริ่ม–สิ้นสุดใหม่)
PC #01-#02 / General Adult — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 70 บาท สำหรับ 60 นาที ตามกฎ session_ceil [S1]
PC #03-#10 / General Adult — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 70 บาท สำหรับ 60 นาที ตามกฎ session_ceil [S2]
```

### R119_revision02

```text
อัตราที่เจ้าของยืนยันล่าสุด ณ 2026-10-20 (ยังไม่ยืนยันวันเริ่ม–สิ้นสุดใหม่)
PC #01-#02 / General Adult — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 70 บาท สำหรับ 60 นาที ตามกฎ session_ceil [S1]
PC #03-#10 / General Adult — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 70 บาท สำหรับ 60 นาที ตามกฎ session_ceil [S2]
```

### แผนและหลักฐานที่เลือก

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
      "id": "13800f21694b4c96bf13a2c3b76f786d",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"บุคคลทั่วไป เล่น pc 1 ชั่วโมง เสียกี่บาท\", \"operation\": \"price_calculate\", \"domain\": \"service_fee\", \"facet\": \"amount\", \"target\": \"\", \"ambiguous\": false, \"constraints\": [{\"slot\": \"audience\", \"quote\": \"บุคคลทั่วไป\", \"source_record_id\": \"audience_general_adult\"}]}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 2.891,
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
  "grades": [
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


## c8d9c78fa099e0ae2726a3da4066357a96e22d67640aea89f2c41a5ad07103ed

Could you please help me with this: Is it open on Sundays

### Legacy_R64_saved

```text
Sunday: no regular service period is listed.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)
```

### R115_saved

```text
**Service schedule**
• Opening periods: No entries in this field (confirmed) [S1]
• Bookable periods: No entries in this field (confirmed) [S2]
• Maintenance periods: No entries in this field (confirmed) [S3]
• timezone: Asia/Bangkok [S4]
• weekday: 6 [S5]

English translation is machine generated and has not been reviewed by the owner.
```

### R118_revision02_saved

```text
No confirmed source is available for the requested detail.
```

### R119_revision01

```text
Sunday — regular play-service timetable: Closed for play under the regular timetable. [S1]
```

### R119_revision02

```text
Sunday — regular play-service timetable: Closed for play under the regular timetable. [S1]
```

### แผนและหลักฐานที่เลือก

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
      "id": "979c85ab489f4b828f8463a5656b142c",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"is it open on sundays\", \"operation\": \"schedule_lookup\", \"domain\": \"schedule\", \"facet\": \"bookable_periods\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 1.906,
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
      "status": "supported",
      "reason_codes": [
        "recorded_play_service_calendar"
      ],
      "receipts": [
        {
          "record_id": "migrated_schedule_6",
          "field": "service_periods",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/service_slots",
              "source_id": "r119_71946c26d16898b73041525bdd30"
            }
          ]
        }
      ],
      "claim_packets": [
        {
          "fact_id": "C11:migrated_schedule_6:service_periods",
          "record_id": "migrated_schedule_6",
          "facet": "service_periods",
          "value": "Closed for play under the regular timetable.",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/service_slots",
              "source_id": "r119_71946c26d16898b73041525bdd30"
            }
          ],
          "fixture": false,
          "status": "answer"
        }
      ],
      "semantic_correctness_verified": false
    }
  ],
  "grades": [
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
      "row": 6418,
      "variant": "question",
      "id": "MASTER-GT-EN-01419",
      "passed": false,
      "failures": [
        "route:knowledge expected:['reservation', 'schedule']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['reservation', 'schedule']"
        ]
      },
      "positive_literal": false,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
      "row": 6438,
      "variant": "question",
      "id": "MASTER-GT-EN-01439",
      "passed": false,
      "failures": [
        "route:knowledge expected:['reservation', 'schedule']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['reservation', 'schedule']"
        ]
      },
      "positive_literal": false,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_en_5000_v1.jsonl",
      "row": 1418,
      "variant": "question",
      "id": "MASTER-GT-EN-01419",
      "passed": false,
      "failures": [
        "route:knowledge expected:['reservation', 'schedule']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['reservation', 'schedule']"
        ]
      },
      "positive_literal": false,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_en_5000_v2.jsonl",
      "row": 1438,
      "variant": "question",
      "id": "MASTER-GT-EN-01439",
      "passed": false,
      "failures": [
        "route:knowledge expected:['reservation', 'schedule']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['reservation', 'schedule']"
        ]
      },
      "positive_literal": false,
      "literal_passed": true,
      "literal_errors": []
    }
  ]
}
```


## da13326d0ec0fb58f22dec994cbf4c9d74d86f5e8e260eb5bb7e1248bf5a9c56

ขอข้อมูลเรื่องนินเทนโด overcooked

### Legacy_R64_saved

```text
Overcooked มีหลายเกมในรายการปัจจุบันครับ คำถามนี้จึงยังไม่ชัดว่าหมายถึงเกมไหน ถ้าต้องการถามเรื่องข้อมูลเกม ขอเลือกเกมก่อน:
•    Overcooked! (Nintendo Switch Zone)
•    Overcooked! 2 (Nintendo Switch Zone)
```

### R115_saved

```text
Overcooked 2 — แนวเกม: เกม Co-op ทำอาหาร [S1]
Overcooked 2 — บริการที่มีเกมนี้: Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons) [S2]
Overcooked 2 — วิธีเล่น: ช่วยกันหั่นวัตถุดิบ ปรุง เสิร์ฟ ล้างจาน และสื่อสารกับทีมให้ทันเวลา [S3]
Overcooked 2 — คำอธิบายเกม: Overcooked 2 คือเกมทำอาหารแบบร่วมมือกัน ผู้เล่นต้องแบ่งหน้าที่ เตรียมอาหาร เสิร์ฟ และจัดการครัวที่วุ่นวาย [S4]
```

### R118_revision02_saved

```text
Overcooked 2 — แนวเกม: เกม Co-op ทำอาหาร [S1]
Overcooked 2 — บริการที่มีเกมนี้: Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons) [S2]
Overcooked 2 — วิธีเล่น: ช่วยกันหั่นวัตถุดิบ ปรุง เสิร์ฟ ล้างจาน และสื่อสารกับทีมให้ทันเวลา [S3]
Overcooked 2 — คำอธิบายเกม: Overcooked 2 คือเกมทำอาหารแบบร่วมมือกัน ผู้เล่นต้องแบ่งหน้าที่ เตรียมอาหาร เสิร์ฟ และจัดการครัวที่วุ่นวาย [S4]
```

### R119_revision01

```text
นินเทนโด.*overcooked — คำตอบที่ยืนยัน: เกม Nintendo Switch ที่มีในรายการรวมถึง Mario Kart 8 Deluxe, Overcooked 2, Nintendo Switch Sports และ Super Smash Bros Ultimate [S1]
```

### R119_revision02

```text
คำตอบที่ยืนยัน: เกม Nintendo Switch ที่มีในรายการรวมถึง Mario Kart 8 Deluxe, Overcooked 2, Nintendo Switch Sports และ Super Smash Bros Ultimate [S1]
```

### แผนและหลักฐานที่เลือก

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
      "id": "6bd9dbbe5fc248f287c787e32ed0cdf9",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"ขอข้อมูลเรื่องนินเทนโด overcooked\", \"operation\": \"detail\", \"domain\": \"games\", \"facet\": \"game_catalog\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 1.922,
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
        "declared_legacy_query_profile"
      ],
      "receipts": [
        {
          "record_id": "migrated_faq_rule_switch_specific_games",
          "field": "answer",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/answer",
              "source_id": "r63_3b00a8c908d318c4f1c1ed3c8b5f"
            }
          ]
        }
      ],
      "claim_packets": [
        {
          "fact_id": "C04:migrated_faq_rule_switch_specific_games:owner_policy",
          "record_id": "migrated_faq_rule_switch_specific_games",
          "facet": "owner_policy",
          "value": "เกม Nintendo Switch ที่มีในรายการรวมถึง Mario Kart 8 Deluxe, Overcooked 2, Nintendo Switch Sports และ Super Smash Bros Ultimate",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/answer",
              "source_id": "r63_3b00a8c908d318c4f1c1ed3c8b5f"
            }
          ],
          "fixture": false,
          "status": "answer"
        }
      ],
      "semantic_correctness_verified": false
    }
  ],
  "grades": [
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
      "row": 1607,
      "variant": "question",
      "id": "MASTER-GT-TH-01608",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
      "row": 1607,
      "variant": "question",
      "id": "MASTER-GT-TH-01608",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_th_5000_v1.jsonl",
      "row": 1607,
      "variant": "question",
      "id": "MASTER-GT-TH-01608",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_th_5000_v2.jsonl",
      "row": 1607,
      "variant": "question",
      "id": "MASTER-GT-TH-01608",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_gt_bilingual_multi_error_2000_20260929_r15.jsonl",
      "row": 723,
      "variant": "clean",
      "id": "MASTER-GT-TH-01608",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    }
  ]
}
```


## df43bd3875afe1ec13852f6a55eeaa9498f77bad85c26879dc068c595c49b556

Which studio zone has Little Nightmares II

### Legacy_R64_saved

```text
Little Nightmares II is available on: Nintendo Switch (1-2 Persons), Nintendo Switch (1-4 Persons). Studio zone(s): Nintendo Switch Zone.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)
```

### R115_saved

```text
Little Nightmares II — studio services offering this game: Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons) [S1]
```

### R118_revision02_saved

```text
The zone relation is not confirmed; the following studio services are confirmed to offer this game.
Little Nightmares II — studio services offering this game: Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons) [S1]
```

### R119_revision01

```text
Little Nightmares II — confirmed studio zones offering this game: Nintendo Switch Zone [S1]
```

### R119_revision02

```text
Little Nightmares II — confirmed studio zones offering this game: Nintendo Switch Zone [S1]
```

### แผนและหลักฐานที่เลือก

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
      "id": "d8134ee0c2994076a0766a8abbe06d4f",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"which studio zone has little nightmares ii\", \"operation\": \"detail\", \"domain\": \"games\", \"facet\": \"zone\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 1.86,
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
      "status": "supported",
      "reason_codes": [
        "typed_game_zone_projection"
      ],
      "receipts": [
        {
          "record_id": "game_detail_little_nightmares_2",
          "field": "zone",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_b274d1294972d1e3fa196c516542"
            },
            {
              "locator": "/mapped_fields/venue_zone_ids",
              "source_id": "r68_url_13702ea8439b64c7c7199c93"
            },
            {
              "locator": "/mapped_fields/name",
              "source_id": "r63_65978ce05d77e443d405488570f6"
            },
            {
              "locator": "/mapped_fields/game_id",
              "source_id": "r63_478fbbfb23338128ec3239ec68a4"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_478fbbfb23338128ec3239ec68a4"
            },
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_478fbbfb23338128ec3239ec68a4"
            },
            {
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_bb06613f34063f9f3815210a0c3e"
            },
            {
              "locator": "/mapped_fields/game_id",
              "source_id": "r63_bf51329075caf6e636d0af619493"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_bf51329075caf6e636d0af619493"
            },
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_bf51329075caf6e636d0af619493"
            },
            {
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_0ee2edc67d0cd1f9a3abcd97d565"
            }
          ]
        }
      ],
      "claim_packets": [
        {
          "fact_id": "C04:game_detail_little_nightmares_2:zone",
          "record_id": "game_detail_little_nightmares_2",
          "facet": "zone",
          "value": "Nintendo Switch Zone",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_b274d1294972d1e3fa196c516542"
            },
            {
              "locator": "/mapped_fields/venue_zone_ids",
              "source_id": "r68_url_13702ea8439b64c7c7199c93"
            },
            {
              "locator": "/mapped_fields/name",
              "source_id": "r63_65978ce05d77e443d405488570f6"
            },
            {
              "locator": "/mapped_fields/game_id",
              "source_id": "r63_478fbbfb23338128ec3239ec68a4"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_478fbbfb23338128ec3239ec68a4"
            },
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_478fbbfb23338128ec3239ec68a4"
            },
            {
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_bb06613f34063f9f3815210a0c3e"
            },
            {
              "locator": "/mapped_fields/game_id",
              "source_id": "r63_bf51329075caf6e636d0af619493"
            },
            {
              "locator": "/mapped_fields/service_id",
              "source_id": "r63_bf51329075caf6e636d0af619493"
            },
            {
              "locator": "/mapped_fields/offered",
              "source_id": "r63_bf51329075caf6e636d0af619493"
            },
            {
              "locator": "/mapped_fields/studio_zone_ids",
              "source_id": "r119_0ee2edc67d0cd1f9a3abcd97d565"
            }
          ],
          "fixture": false,
          "status": "answer"
        }
      ],
      "semantic_correctness_verified": false
    }
  ],
  "grades": [
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
      "row": 7241,
      "variant": "question",
      "id": "MASTER-GT-EN-02242",
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
      "row": 7241,
      "variant": "question",
      "id": "MASTER-GT-EN-02242",
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
      "row": 2241,
      "variant": "question",
      "id": "MASTER-GT-EN-02242",
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
      "row": 2241,
      "variant": "question",
      "id": "MASTER-GT-EN-02242",
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


## e7a3582eb91ae5efaa59505498774e8fb8612e92d4a2b5736d12c78a7b467a5d

ช่วยอธิบายให้เข้าใจง่ายหน่อยว่า ขอข้อมูลเรื่องของหาย อุปกรณ์ เปียก

### Legacy_R64_saved

```text
กรุณาตรวจสอบทรัพย์สินของท่านทุกครั้งระหว่างการใช้บริการ หากมีการสูญหาย ศูนย์ขอสงวนสิทธิ์ไม่รับผิดชอบในทุกกรณี
แหล่งข้อมูล: https://esports.computing.psu.ac.th/
```

### R115_saved

```text
ยังยืนยันคำตอบให้ครบตามสถานการณ์ที่ถามไม่ได้ครับ กรุณาระบุรายละเอียดหรือแยกคำถามเพิ่มเติมอีกนิด
```

### R118_revision02_saved

```text
ยังยืนยันคำตอบให้ครบตามสถานการณ์ที่ถามไม่ได้ครับ กรุณาระบุรายละเอียดหรือแยกคำถามเพิ่มเติมอีกนิด
```

### R119_revision01

```text
ยังยืนยันคำตอบให้ครบตามสถานการณ์ที่ถามไม่ได้ครับ กรุณาระบุรายละเอียดหรือแยกคำถามเพิ่มเติมอีกนิด
```

### R119_revision02

```text
ยังยืนยันคำตอบให้ครบตามสถานการณ์ที่ถามไม่ได้ครับ กรุณาระบุรายละเอียดหรือแยกคำถามเพิ่มเติมอีกนิด
```

### แผนและหลักฐานที่เลือก

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
  "grades": [
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
      "row": 3985,
      "variant": "question",
      "id": "MASTER-GT-TH-03986",
      "passed": false,
      "failures": [
        "route:knowledge expected:['rules']",
        "status:clarification expected:answer_available"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['rules']"
        ],
        "outcome": [
          "status:clarification expected:answer_available"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
      "row": 3985,
      "variant": "question",
      "id": "MASTER-GT-TH-03986",
      "passed": false,
      "failures": [
        "route:knowledge expected:['rules']",
        "status:clarification expected:answer_available"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['rules']"
        ],
        "outcome": [
          "status:clarification expected:answer_available"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_th_5000_v1.jsonl",
      "row": 3985,
      "variant": "question",
      "id": "MASTER-GT-TH-03986",
      "passed": false,
      "failures": [
        "route:knowledge expected:['rules']",
        "status:clarification expected:answer_available"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['rules']"
        ],
        "outcome": [
          "status:clarification expected:answer_available"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_th_5000_v2.jsonl",
      "row": 3985,
      "variant": "question",
      "id": "MASTER-GT-TH-03986",
      "passed": false,
      "failures": [
        "route:knowledge expected:['rules']",
        "status:clarification expected:answer_available"
      ],
      "evidence_level": "route_outcome_only",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['rules']"
        ],
        "outcome": [
          "status:clarification expected:answer_available"
        ]
      },
      "positive_literal": false,
      "literal_passed": null,
      "literal_errors": []
    }
  ]
}
```


## e869467170e02fba6c045d82f418e6fde8729870e12377a453b4d40e407a5c42

Who holds te role of ประธาน

### Legacy_R64_saved

```text
Verified PSU Esports Studio - Phuket member directory:
Names retain the exact spelling in the official Thai source; role labels are translated.
- นายษุภากรณ์ จิราจินดากุล: Chairperson (ประธาน)
Source: https://esports.phuket.psu.ac.th/about-us/Members (original source in Thai)
```

### R115_saved

```text
ยังยืนยันขอบเขตข้อมูลบุคลากรที่เปิดเผยได้ไม่ครบ จึงยังแสดงรายละเอียดส่วนนี้ไม่ได้ครับ
```

### R118_revision02_saved

```text
Matching personnel records exist, but their public disclosure scope has not been confirmed.
```

### R119_revision01

```text
According to the recorded source profile:
นายษุภากรณ์ จิราจินดากุล — role: Chair [S1]
```

### R119_revision02

```text
According to the recorded source profile:
นายษุภากรณ์ จิราจินดากุล — role: Chair [S1]
```

### แผนและหลักฐานที่เลือก

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
      "id": "c257b5af4a5b464a84d8caad8f8118aa",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"who holds te role of ประธาน\", \"operation\": \"role_lookup\", \"domain\": \"members\", \"facet\": \"role\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 7.094,
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
      "status": "supported",
      "reason_codes": [
        "inverse_role_to_people"
      ],
      "receipts": [
        {
          "record_id": "member_1d884f11f3890dea",
          "field": "role",
          "status": "known",
          "evidence_refs": [
            {
              "locator": "/mapped_fields/role",
              "source_id": "r66_person_review_06a15a8e9bce9275b3e25033"
            }
          ]
        }
      ],
      "claim_packets": [
        {
          "fact_id": "C02:member_1d884f11f3890dea:role",
          "record_id": "member_1d884f11f3890dea",
          "facet": "role",
          "value": "Chair",
          "numeric": null,
          "evidence_refs": [
            {
              "locator": "/mapped_fields/role",
              "source_id": "r66_person_review_06a15a8e9bce9275b3e25033"
            }
          ],
          "fixture": false,
          "status": "answer"
        }
      ],
      "semantic_correctness_verified": false
    }
  ],
  "grades": [
    {
      "file": "data/eval/master_gt_bilingual_multi_error_2000_20260929_r15.jsonl",
      "row": 1682,
      "variant": "noisy",
      "id": "MASTER-GT-EN-04524",
      "passed": false,
      "failures": [
        "route:knowledge expected:['members', 'overview']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": true
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['members', 'overview']"
        ]
      },
      "positive_literal": true,
      "literal_passed": true,
      "literal_errors": []
    }
  ]
}
```


## eafe23b9409a6794810e1fcd47cfba8fd823c4a638c203551cf05697f6ae2134

ปุ่มของ New Super Mario Bros. U Deluxe มีอะไรบ้าง

### Legacy_R64_saved

```text
New Super Mario Bros. U Deluxe มีข้อมูลปุ่มควบคุมดังนี้:
Nintendo Switch
•    One Joy-Con: ควบคุมตัวละครด้วย Joy-Con เดี่ยว - หน้า Nintendo ระบุว่าใช้ Joy-Con เพียงหนึ่งข้างก็เล่นได้ เหมาะกับการเล่นหลายคน
•    Simple controls: วิ่ง กระโดด และเหยียบศัตรู - หน้า Nintendo อธิบายการเล่นเป็นเกม 2D side-scrolling ที่ใช้การวิ่ง กระโดด และเหยียบศัตรู แต่ไม่ได้ให้ปุ่มละเอียดรายปุ่ม
แหล่งข้อมูล: https://www.nintendo.com/sg/switch/adal/index.html
```

### R115_saved

```text
New Super Mario Bros. U Deluxe / Nintendo Switch — ควบคุมตัวละครด้วย Joy-Con เดี่ยว: One Joy-Con — หน้า Nintendo ระบุว่าใช้ Joy-Con เพียงหนึ่งข้างก็เล่นได้ เหมาะกับการเล่นหลายคน [S1]
```

### R118_revision02_saved

```text
New Super Mario Bros. U Deluxe / Nintendo Switch — ควบคุมตัวละครด้วย Joy-Con เดี่ยว: One Joy-Con — หน้า Nintendo ระบุว่าใช้ Joy-Con เพียงหนึ่งข้างก็เล่นได้ เหมาะกับการเล่นหลายคน [S1]
New Super Mario Bros. U Deluxe / Nintendo Switch — วิ่ง กระโดด และเหยียบศัตรู: Simple controls — หน้า Nintendo อธิบายการเล่นเป็นเกม 2D side-scrolling ที่ใช้การวิ่ง กระโดด และเหยียบศัตรู แต่ไม่ได้ให้ปุ่มละเอียดรายปุ่ม [S2]
```

### R119_revision01

```text
New Super Mario Bros. U Deluxe / Nintendo Switch — ควบคุมตัวละครด้วย Joy-Con เดี่ยว: One Joy-Con — หน้า Nintendo ระบุว่าใช้ Joy-Con เพียงหนึ่งข้างก็เล่นได้ เหมาะกับการเล่นหลายคน [S1]
New Super Mario Bros. U Deluxe / Nintendo Switch — วิ่ง กระโดด และเหยียบศัตรู: Simple controls — หน้า Nintendo อธิบายการเล่นเป็นเกม 2D side-scrolling ที่ใช้การวิ่ง กระโดด และเหยียบศัตรู แต่ไม่ได้ให้ปุ่มละเอียดรายปุ่ม [S2]
```

### R119_revision02

```text
New Super Mario Bros. U Deluxe / Nintendo Switch — ควบคุมตัวละครด้วย Joy-Con เดี่ยว: One Joy-Con — หน้า Nintendo ระบุว่าใช้ Joy-Con เพียงหนึ่งข้างก็เล่นได้ เหมาะกับการเล่นหลายคน [S1]
New Super Mario Bros. U Deluxe / Nintendo Switch — วิ่ง กระโดด และเหยียบศัตรู: Simple controls — หน้า Nintendo อธิบายการเล่นเป็นเกม 2D side-scrolling ที่ใช้การวิ่ง กระโดด และเหยียบศัตรู แต่ไม่ได้ให้ปุ่มละเอียดรายปุ่ม [S2]
```

### แผนและหลักฐานที่เลือก

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
      "id": "3dc0e152e9c0483796521df478880e5f",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"ปุ่มของ new super mario bros. u deluxe มีอะไรบ้าง\", \"operation\": \"list\", \"domain\": \"game_controls\", \"facet\": \"input_bindings\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 2.016,
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
  "grades": [
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


## f683a42cb3ba63c5f215900a88eb9a00791cc40073305efffd6fd66cf19d93be

On which device can Animal Crossing: New Horizons be played

### Legacy_R64_saved

```text
Animal Crossing: New Horizons is available on: Nintendo Switch (1-2 Persons), Nintendo Switch (1-4 Persons). Studio zone(s): Nintendo Switch Zone.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)
```

### R115_saved

```text
Animal Crossing: New Horizons — studio services offering this game: Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons) [S1]
```

### R118_revision02_saved

```text
Animal Crossing: New Horizons — studio services offering this game: Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons) [S1]
```

### R119_revision01

```text
Animal Crossing: New Horizons — studio services offering this game: Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons) [S1]
```

### R119_revision02

```text
Animal Crossing: New Horizons — studio services offering this game: Nintendo Switch (1-2 Persons); Nintendo Switch (1-4 Persons) [S1]
```

### แผนและหลักฐานที่เลือก

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
      "id": "a1c4fd8aeba34443a539faa99fe8e7db",
      "stage": "context_understanding",
      "model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "transport_ok": true,
      "schema_ok": true,
      "response_model": "scb10x/typhoon2.5-qwen3-4b:latest",
      "identity_verified": true,
      "raw_content": "{\"tasks\": [{\"quote\": \"on which device can animal crossing: new horizons be played\", \"operation\": \"detail\", \"domain\": \"games\", \"facet\": \"supported_platforms\", \"target\": \"\", \"ambiguous\": false, \"constraints\": []}]}",
      "reason": "validated_interpretation_proposal",
      "elapsed_sec": 1.86,
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
  "grades": [
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v1.jsonl",
      "row": 6952,
      "variant": "question",
      "id": "MASTER-GT-EN-01953",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": false,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_bilingual_10000_v2.jsonl",
      "row": 6856,
      "variant": "question",
      "id": "MASTER-GT-EN-01857",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": false,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_en_5000_v1.jsonl",
      "row": 1952,
      "variant": "question",
      "id": "MASTER-GT-EN-01953",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": false,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_ground_truth_en_5000_v2.jsonl",
      "row": 1856,
      "variant": "question",
      "id": "MASTER-GT-EN-01857",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": false,
      "literal_passed": true,
      "literal_errors": []
    },
    {
      "file": "data/eval/master_gt_bilingual_multi_error_2000_20260929_r15.jsonl",
      "row": 1614,
      "variant": "clean",
      "id": "MASTER-GT-EN-01857",
      "passed": false,
      "failures": [
        "route:knowledge expected:['games']"
      ],
      "evidence_level": "literal_content_contract",
      "grader_detail": {
        "strong_outcome_matches": false,
        "positive_content_asserted": false
      },
      "partitions": {
        "protocol": [
          "route:knowledge expected:['games']"
        ]
      },
      "positive_literal": false,
      "literal_passed": true,
      "literal_errors": []
    }
  ]
}
```
