# ตรวจสาเหตุและตัวอย่างทุกข้อที่ไม่ผ่านรอบก่อนแก้

อ่านคู่กับ FINAL_REPORT_TH.md ไม่ถือ extra claims ทั้งหมดเป็นเนื้อหาผิดและไม่ถือ missing fixture เป็นการตอบถูก รายการนี้อ่าน saved raw เท่านั้น ไม่ส่งคำถามใหม่

## C02-Q020 — บุคลากร

รบกวนเช็กให้หน่อย นางสาวณัฐธิดา คำทะเนตร์ ใช้ชื่ออะไร

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, required_claims_missing, state=unclassified

```text
สวัสดีครับ ผมคือผู้ช่วยของ PSU Esports Studio - Phuket ถามเรื่องเกม อุปกรณ์ ราคา วิธีจอง เวลาให้บริการ กฎศูนย์ หรือกติกาการแข่งขันได้ครับ
```

หลัง: strict=True, source_contract_pass, state=answer

```text
นางสาวณัฐธิดา คำทะเนตร์ — ชื่อ: นางสาวณัฐธิดา คำทะเนตร์ [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C02:member_9e9cb3b178e5d76c:display_name",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C02:member_9e9cb3b178e5d76c:display_name",
      "record_id": "member_9e9cb3b178e5d76c",
      "facet": "display_name",
      "value": "นางสาวณัฐธิดา คำทะเนตร์",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/display_name",
          "source_id": "r66_person_review_e9c4bdf9167f1a144118f409"
        }
      ]
    },
    "native_fact_id": "C02:member_9e9cb3b178e5d76c:display_name",
    "native_record_id": "member_9e9cb3b178e5d76c",
    "facet": "display_name",
    "value": "นางสาวณัฐธิดา คำทะเนตร์",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/display_name",
        "source_id": "r66_person_review_e9c4bdf9167f1a144118f409"
      }
    ],
    "legacy_record_id": "member_9e9cb3b178e5d76c"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C02-Q038 — บุคลากร

ช่วยตอบสั้น ๆ ว่า นายปัณณวิชญ์ หนูเรือง ใช้ชื่ออะไร

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, required_claims_missing, state=unclassified

```text
สวัสดีครับ ผมคือผู้ช่วยของ PSU Esports Studio - Phuket ถามเรื่องเกม อุปกรณ์ ราคา วิธีจอง เวลาให้บริการ กฎศูนย์ หรือกติกาการแข่งขันได้ครับ
```

หลัง: strict=True, source_contract_pass, state=answer

```text
นายปัณณวิชญ์ หนูเรือง — ชื่อ: นายปัณณวิชญ์ หนูเรือง [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C02:member_f90051b3c68e16b4:display_name",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C02:member_f90051b3c68e16b4:display_name",
      "record_id": "member_f90051b3c68e16b4",
      "facet": "display_name",
      "value": "นายปัณณวิชญ์ หนูเรือง",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/display_name",
          "source_id": "r66_person_review_7180637c38eddeac565aff09"
        }
      ]
    },
    "native_fact_id": "C02:member_f90051b3c68e16b4:display_name",
    "native_record_id": "member_f90051b3c68e16b4",
    "facet": "display_name",
    "value": "นายปัณณวิชญ์ หนูเรือง",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/display_name",
        "source_id": "r66_person_review_7180637c38eddeac565aff09"
      }
    ],
    "legacy_record_id": "member_f90051b3c68e16b4"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C02-Q044 — บุคลากร

ขอสอบถามหน่อยครับ นายณัฐวัฒน์ นิธิคุณานนต์ ใช้ชื่ออะไร

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, required_claims_missing, state=unclassified

```text
สวัสดีครับ ผมคือผู้ช่วยของ PSU Esports Studio - Phuket ถามเรื่องเกม อุปกรณ์ ราคา วิธีจอง เวลาให้บริการ กฎศูนย์ หรือกติกาการแข่งขันได้ครับ
```

หลัง: strict=True, source_contract_pass, state=answer

```text
นายณัฐวัฒน์ นิธิคุณานนต์ — ชื่อ: นายณัฐวัฒน์ นิธิคุณานนต์ [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C02:member_2035485e1198bd6d:display_name",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C02:member_2035485e1198bd6d:display_name",
      "record_id": "member_2035485e1198bd6d",
      "facet": "display_name",
      "value": "นายณัฐวัฒน์ นิธิคุณานนต์",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/display_name",
          "source_id": "r66_person_review_3b101b0adc35f45731437fa7"
        }
      ]
    },
    "native_fact_id": "C02:member_2035485e1198bd6d:display_name",
    "native_record_id": "member_2035485e1198bd6d",
    "facet": "display_name",
    "value": "นายณัฐวัฒน์ นิธิคุณานนต์",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/display_name",
        "source_id": "r66_person_review_3b101b0adc35f45731437fa7"
      }
    ],
    "legacy_record_id": "member_2035485e1198bd6d"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C02-Q047 — บุคลากร

กำลังวางแผนไปใช้บริการ เลยขอถามว่า นายณัฐพนธ์ อินทรสังขนาวิน ใช้ชื่ออะไร

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, required_claims_missing, state=unclassified

```text
สวัสดีครับ ผมคือผู้ช่วยของ PSU Esports Studio - Phuket ถามเรื่องเกม อุปกรณ์ ราคา วิธีจอง เวลาให้บริการ กฎศูนย์ หรือกติกาการแข่งขันได้ครับ
```

หลัง: strict=True, source_contract_pass, state=answer

```text
นายณัฐพนธ์ อินทรสังขนาวิน — ชื่อ: นายณัฐพนธ์ อินทรสังขนาวิน [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C02:member_a19d2197ce8e1a38:display_name",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C02:member_a19d2197ce8e1a38:display_name",
      "record_id": "member_a19d2197ce8e1a38",
      "facet": "display_name",
      "value": "นายณัฐพนธ์ อินทรสังขนาวิน",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/display_name",
          "source_id": "r66_person_review_be5634d6dfacc5aba646c90d"
        }
      ]
    },
    "native_fact_id": "C02:member_a19d2197ce8e1a38:display_name",
    "native_record_id": "member_a19d2197ce8e1a38",
    "facet": "display_name",
    "value": "นายณัฐพนธ์ อินทรสังขนาวิน",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/display_name",
        "source_id": "r66_person_review_be5634d6dfacc5aba646c90d"
      }
    ],
    "legacy_record_id": "member_a19d2197ce8e1a38"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C02-Q079 — บุคลากร

ขอสอบถามหน่อยครับ นางสาวกมลวรรณ นวลสาย ทำหน้าที่อะไร แล้วขอนางสาวกมลวรรณ นวลสาย ใช้ชื่ออะไร

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, required_claims_missing, state=unclassified

```text
สวัสดีครับ ผมคือผู้ช่วยของ PSU Esports Studio - Phuket ถามเรื่องเกม อุปกรณ์ ราคา วิธีจอง เวลาให้บริการ กฎศูนย์ หรือกติกาการแข่งขันได้ครับ
```

หลัง: strict=True, source_contract_pass, state=answer

```text
นางสาวกมลวรรณ นวลสาย — หน้าที่และตำแหน่ง: กรรมการ [S1]

นางสาวกมลวรรณ นวลสาย — ชื่อ: นางสาวกมลวรรณ นวลสาย [S2]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C02:member_18a751d710b9b30c:role",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C02:member_18a751d710b9b30c:role",
      "record_id": "member_18a751d710b9b30c",
      "facet": "role",
      "value": "กรรมการ",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/role",
          "source_id": "r66_person_review_2f81ce5b9ffc69ed803bc905"
        }
      ]
    },
    "native_fact_id": "C02:member_18a751d710b9b30c:role",
    "native_record_id": "member_18a751d710b9b30c",
    "facet": "role",
    "value": "กรรมการ",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/role",
        "source_id": "r66_person_review_2f81ce5b9ffc69ed803bc905"
      }
    ],
    "legacy_record_id": "member_18a751d710b9b30c"
  },
  {
    "legacy_fact_id": "C02:member_18a751d710b9b30c:display_name",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C02:member_18a751d710b9b30c:display_name",
      "record_id": "member_18a751d710b9b30c",
      "facet": "display_name",
      "value": "นางสาวกมลวรรณ นวลสาย",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/display_name",
          "source_id": "r66_person_review_2f81ce5b9ffc69ed803bc905"
        }
      ]
    },
    "native_fact_id": "C02:member_18a751d710b9b30c:display_name",
    "native_record_id": "member_18a751d710b9b30c",
    "facet": "display_name",
    "value": "นางสาวกมลวรรณ นวลสาย",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/display_name",
        "source_id": "r66_person_review_2f81ce5b9ffc69ed803bc905"
      }
    ],
    "legacy_record_id": "member_18a751d710b9b30c"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C03-Q002 — อุปกรณ์

ขอสอบถามหน่อยครับ อยากดูรายละเอียดฮาร์ดแวร์ Sony PlayStation VR2

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=True, source_contract_pass, state=answer

```text
Sony PlayStation VR2 — สเปก: zone; VR Zone; quantity; 1 Unit [S1]
```

หลัง: strict=True, source_contract_pass, state=answer

```text
Sony PlayStation VR2 — สเปก: zone; VR Zone; quantity; 1 Unit [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C03:equipment_sony_playstation_vr2:specifications",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C03:equipment_sony_playstation_vr2:specifications",
      "record_id": "equipment_sony_playstation_vr2",
      "facet": "specifications",
      "value": "key: zone; unit: None; value: VR Zone; key: quantity; unit: None; value: 1 Unit",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/specifications",
          "source_id": "r63_1dc5af180d92a866489f54c007f0"
        }
      ]
    },
    "native_fact_id": "C03:equipment_sony_playstation_vr2:specifications",
    "native_record_id": "equipment_sony_playstation_vr2",
    "facet": "specifications",
    "value": "key: zone; unit: None; value: VR Zone; key: quantity; unit: None; value: 1 Unit",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/specifications",
        "source_id": "r63_1dc5af180d92a866489f54c007f0"
      }
    ],
    "legacy_record_id": "equipment_sony_playstation_vr2"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": [
    "C03:equipment_sony_playstation_vr2:specifications"
  ]
}
```

## C03-Q006 — อุปกรณ์

รบกวนเช็กให้หน่อย Gaming Chair ใช้สเปกอะไร

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=True, source_contract_pass, state=answer

```text
Gaming Chair — สเปก: zone; PC Zone; quantity; 10 Units [S1]
```

หลัง: strict=True, source_contract_pass, state=answer

```text
Gaming Chair — สเปก: zone; PC Zone; quantity; 10 Units [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C03:equipment_gaming_chair:specifications",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C03:equipment_gaming_chair:specifications",
      "record_id": "equipment_gaming_chair",
      "facet": "specifications",
      "value": "key: zone; unit: None; value: PC Zone; key: quantity; unit: None; value: 10 Units",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/specifications",
          "source_id": "r63_fc7d8dd97058c5a18e121b2de918"
        }
      ]
    },
    "native_fact_id": "C03:equipment_gaming_chair:specifications",
    "native_record_id": "equipment_gaming_chair",
    "facet": "specifications",
    "value": "key: zone; unit: None; value: PC Zone; key: quantity; unit: None; value: 10 Units",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/specifications",
        "source_id": "r63_fc7d8dd97058c5a18e121b2de918"
      }
    ],
    "legacy_record_id": "equipment_gaming_chair"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": [
    "C03:equipment_gaming_chair:specifications"
  ]
}
```

## C03-Q021 — อุปกรณ์

ถามจากข้อมูลที่ศูนย์ให้ไว้ TV 86 นิ้ว ใช้สเปกอะไร

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=True, source_contract_pass, state=answer

```text
TV 86 นิ้ว — สเปก: zone; Nintendo Switch Zone; quantity; 1 Unit [S1]
```

หลัง: strict=True, source_contract_pass, state=answer

```text
TV 86 นิ้ว — สเปก: zone; Nintendo Switch Zone; quantity; 1 Unit [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C03:equipment_tv_86:specifications",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C03:equipment_tv_86:specifications",
      "record_id": "equipment_tv_86",
      "facet": "specifications",
      "value": "key: zone; unit: None; value: Nintendo Switch Zone; key: quantity; unit: None; value: 1 Unit",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/specifications",
          "source_id": "r63_94f44807c17230dc73c9cee08c90"
        }
      ]
    },
    "native_fact_id": "C03:equipment_tv_86:specifications",
    "native_record_id": "equipment_tv_86",
    "facet": "specifications",
    "value": "key: zone; unit: None; value: Nintendo Switch Zone; key: quantity; unit: None; value: 1 Unit",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/specifications",
        "source_id": "r63_94f44807c17230dc73c9cee08c90"
      }
    ],
    "legacy_record_id": "equipment_tv_86"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": [
    "C03:equipment_tv_86:specifications"
  ]
}
```

## C03-Q026 — อุปกรณ์

กำลังวางแผนไปใช้บริการ เลยขอถามว่า อยากดูรายละเอียดฮาร์ดแวร์ PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=True, source_contract_pass, state=answer

```text
PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive — สเปก: zone; PlayStation 5 Zone / VR Zone; quantity; 2 Units in PlayStation 5 Zone and 1 Unit in VR Zone [S1]
```

หลัง: strict=True, source_contract_pass, state=answer

```text
PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive — สเปก: zone; PlayStation 5 Zone / VR Zone; quantity; 2 Units in PlayStation 5 Zone and 1 Unit in VR Zone [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C03:equipment_playstation_5_slim:specifications",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C03:equipment_playstation_5_slim:specifications",
      "record_id": "equipment_playstation_5_slim",
      "facet": "specifications",
      "value": "key: zone; unit: None; value: PlayStation 5 Zone / VR Zone; key: quantity; unit: None; value: 2 Units in PlayStation 5 Zone and 1 Unit in VR Zone",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/specifications",
          "source_id": "r63_7d57d2ab8268727a0ab6df329dde"
        }
      ]
    },
    "native_fact_id": "C03:equipment_playstation_5_slim:specifications",
    "native_record_id": "equipment_playstation_5_slim",
    "facet": "specifications",
    "value": "key: zone; unit: None; value: PlayStation 5 Zone / VR Zone; key: quantity; unit: None; value: 2 Units in PlayStation 5 Zone and 1 Unit in VR Zone",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/specifications",
        "source_id": "r63_7d57d2ab8268727a0ab6df329dde"
      }
    ],
    "legacy_record_id": "equipment_playstation_5_slim"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": [
    "C03:equipment_playstation_5_slim:specifications"
  ]
}
```

## C03-Q031 — อุปกรณ์

ช่วยตอบสั้น ๆ ว่า สเปกของ Gaming PC รุ่น MSI MAG Infinite S3 14th เป็นแบบไหน

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=True, source_contract_pass, state=answer

```text
Gaming PC รุ่น MSI MAG Infinite S3 14th — สเปก: zone; PC Zone; quantity; 10 Units; recorded_source_detail; สเปกที่บันทึกไว้ในโปรเจกต์: Intel Core i5-14400, RAM DDR5 32GB, NVIDIA GeForce RTX 5060 8GB; CPU; Intel Core i5-14400; RAM; DDR5 32GB; GPU; NVIDIA GeForce RTX 5060 8GB [S1]
```

หลัง: strict=True, source_contract_pass, state=answer

```text
Gaming PC รุ่น MSI MAG Infinite S3 14th — สเปก: zone; PC Zone; quantity; 10 Units; recorded_source_detail; สเปกที่บันทึกไว้ในโปรเจกต์: Intel Core i5-14400, RAM DDR5 32GB, NVIDIA GeForce RTX 5060 8GB; CPU; Intel Core i5-14400; RAM; DDR5 32GB; GPU; NVIDIA GeForce RTX 5060 8GB [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C03:equipment_gaming_pc:specifications",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C03:equipment_gaming_pc:specifications",
      "record_id": "equipment_gaming_pc",
      "facet": "specifications",
      "value": "key: zone; unit: None; value: PC Zone; key: quantity; unit: None; value: 10 Units; key: recorded_source_detail; unit: None; value: สเปกที่บันทึกไว้ในโปรเจกต์: Intel Core i5-14400, RAM DDR5 32GB, NVIDIA GeForce RTX 5060 8GB; key: CPU; unit: None; value: Intel Core i5-14400; key: RAM; unit: None; value: DDR5 32GB; key: GPU; unit: None; value: NVIDIA GeForce RTX 5060 8GB",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/specifications",
          "source_id": "r68_specs_6e0321cf25d72b8d6e364a15"
        }
      ]
    },
    "native_fact_id": "C03:equipment_gaming_pc:specifications",
    "native_record_id": "equipment_gaming_pc",
    "facet": "specifications",
    "value": "key: zone; unit: None; value: PC Zone; key: quantity; unit: None; value: 10 Units; key: recorded_source_detail; unit: None; value: สเปกที่บันทึกไว้ในโปรเจกต์: Intel Core i5-14400, RAM DDR5 32GB, NVIDIA GeForce RTX 5060 8GB; key: CPU; unit: None; value: Intel Core i5-14400; key: RAM; unit: None; value: DDR5 32GB; key: GPU; unit: None; value: NVIDIA GeForce RTX 5060 8GB",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/specifications",
        "source_id": "r68_specs_6e0321cf25d72b8d6e364a15"
      }
    ],
    "legacy_record_id": "equipment_gaming_pc"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": [
    "C03:equipment_gaming_pc:specifications"
  ]
}
```

## C03-Q047 — อุปกรณ์

กำลังวางแผนไปใช้บริการ เลยขอถามว่า อยากดูรายละเอียดฮาร์ดแวร์ Gaming Mouse

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=True, source_contract_pass, state=answer

```text
Gaming Mouse — สเปก: zone; PC Zone [S1]
```

หลัง: strict=True, source_contract_pass, state=answer

```text
Gaming Mouse — สเปก: zone; PC Zone [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C03:equipment_gaming_mouse:specifications",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C03:equipment_gaming_mouse:specifications",
      "record_id": "equipment_gaming_mouse",
      "facet": "specifications",
      "value": "key: zone; unit: None; value: PC Zone",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/specifications",
          "source_id": "r63_560abc52790fc644b6cf2203af58"
        }
      ]
    },
    "native_fact_id": "C03:equipment_gaming_mouse:specifications",
    "native_record_id": "equipment_gaming_mouse",
    "facet": "specifications",
    "value": "key: zone; unit: None; value: PC Zone",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/specifications",
        "source_id": "r63_560abc52790fc644b6cf2203af58"
      }
    ],
    "legacy_record_id": "equipment_gaming_mouse"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": [
    "C03:equipment_gaming_mouse:specifications"
  ]
}
```

## C03-Q050 — อุปกรณ์

อยากดูรายละเอียดฮาร์ดแวร์ Gaming Headset

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=True, source_contract_pass, state=answer

```text
Gaming Headset — สเปก: zone; PC Zone [S1]
```

หลัง: strict=True, source_contract_pass, state=answer

```text
Gaming Headset — สเปก: zone; PC Zone [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C03:equipment_gaming_headset:specifications",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C03:equipment_gaming_headset:specifications",
      "record_id": "equipment_gaming_headset",
      "facet": "specifications",
      "value": "key: zone; unit: None; value: PC Zone",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/specifications",
          "source_id": "r63_d1714679f0f758a35733635fbb38"
        }
      ]
    },
    "native_fact_id": "C03:equipment_gaming_headset:specifications",
    "native_record_id": "equipment_gaming_headset",
    "facet": "specifications",
    "value": "key: zone; unit: None; value: PC Zone",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/specifications",
        "source_id": "r63_d1714679f0f758a35733635fbb38"
      }
    ],
    "legacy_record_id": "equipment_gaming_headset"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": [
    "C03:equipment_gaming_headset:specifications"
  ]
}
```

## C03-Q068 — อุปกรณ์

Please answer briefly: Tell me the technical specs of Nintendo Switch OLED. and also Where is Nintendo Switch OLED located?

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=True, source_contract_pass, state=answer

```text
Nintendo Switch OLED — specifications: zone; Nintendo Switch Zone; quantity; 1 Unit [S1]

Nintendo Switch OLED — location: Nintendo Switch Zone [S2]
```

หลัง: strict=True, source_contract_pass, state=answer

```text
Nintendo Switch OLED — specifications: zone; Nintendo Switch Zone; quantity; 1 Unit [S1]

Nintendo Switch OLED — location: Nintendo Switch Zone [S2]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C03:equipment_nintendo_switch_oled:specifications",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C03:equipment_nintendo_switch_oled:specifications",
      "record_id": "equipment_nintendo_switch_oled",
      "facet": "specifications",
      "value": "key: zone; unit: None; value: Nintendo Switch Zone; key: quantity; unit: None; value: 1 Unit",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/specifications",
          "source_id": "r63_24fbd81ab007fe1a031b762baed7"
        }
      ]
    },
    "native_fact_id": "C03:equipment_nintendo_switch_oled:specifications",
    "native_record_id": "equipment_nintendo_switch_oled",
    "facet": "specifications",
    "value": "key: zone; unit: None; value: Nintendo Switch Zone; key: quantity; unit: None; value: 1 Unit",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/specifications",
        "source_id": "r63_24fbd81ab007fe1a031b762baed7"
      }
    ],
    "legacy_record_id": "equipment_nintendo_switch_oled"
  },
  {
    "legacy_fact_id": "C03:equipment_nintendo_switch_oled:location",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C03:equipment_nintendo_switch_oled:location",
      "record_id": "equipment_nintendo_switch_oled",
      "facet": "location",
      "value": "Nintendo Switch Zone",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/specifications",
          "source_id": "r63_24fbd81ab007fe1a031b762baed7"
        }
      ]
    },
    "native_fact_id": "C03:equipment_nintendo_switch_oled:location",
    "native_record_id": "equipment_nintendo_switch_oled",
    "facet": "location",
    "value": "Nintendo Switch Zone",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/specifications",
        "source_id": "r63_24fbd81ab007fe1a031b762baed7"
      }
    ],
    "legacy_record_id": "equipment_nintendo_switch_oled"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": [
    "C03:equipment_nintendo_switch_oled:specifications"
  ]
}
```

## C03-Q070 — อุปกรณ์

Based on the studio sources, Tell me the technical specs of Gaming Monitor. and also How many units of Gaming Monitor are there?

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=True, source_contract_pass, state=answer

```text
Gaming Monitor — specifications: zone; PC Zone; quantity; 10 Units [S1]

Gaming Monitor — quantity: 10 Units [S2]
```

หลัง: strict=True, source_contract_pass, state=answer

```text
Gaming Monitor — specifications: zone; PC Zone; quantity; 10 Units [S1]

Gaming Monitor — quantity: 10 Units [S2]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C03:equipment_gaming_monitor:specifications",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C03:equipment_gaming_monitor:specifications",
      "record_id": "equipment_gaming_monitor",
      "facet": "specifications",
      "value": "key: zone; unit: None; value: PC Zone; key: quantity; unit: None; value: 10 Units",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/specifications",
          "source_id": "r63_5af80ccff359cadb665af2160ab0"
        }
      ]
    },
    "native_fact_id": "C03:equipment_gaming_monitor:specifications",
    "native_record_id": "equipment_gaming_monitor",
    "facet": "specifications",
    "value": "key: zone; unit: None; value: PC Zone; key: quantity; unit: None; value: 10 Units",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/specifications",
        "source_id": "r63_5af80ccff359cadb665af2160ab0"
      }
    ],
    "legacy_record_id": "equipment_gaming_monitor"
  },
  {
    "legacy_fact_id": "C03:equipment_gaming_monitor:quantity",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C03:equipment_gaming_monitor:quantity",
      "record_id": "equipment_gaming_monitor",
      "facet": "quantity",
      "value": "10 Units",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/specifications",
          "source_id": "r63_5af80ccff359cadb665af2160ab0"
        }
      ]
    },
    "native_fact_id": "C03:equipment_gaming_monitor:quantity",
    "native_record_id": "equipment_gaming_monitor",
    "facet": "quantity",
    "value": "10 Units",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/specifications",
        "source_id": "r63_5af80ccff359cadb665af2160ab0"
      }
    ],
    "legacy_record_id": "equipment_gaming_monitor"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": [
    "C03:equipment_gaming_monitor:specifications"
  ]
}
```

## C03-Q072 — อุปกรณ์

ขอสอบถามหน่อยครับ Pulse Elite Wireless Headset ใช้สเปกอะไร แล้วขอPulse Elite Wireless Headset มีข้อมูลเรื่องการใช้งานอย่างไร

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=True, source_contract_pass, state=answer

```text
Pulse Elite Wireless Headset — สเปก: zone; Cockpit Zone; quantity; 2 Units [S1]

Pulse Elite Wireless Headset — การใช้งาน: หูฟังไร้สายสำหรับใช้งานกับชุดเกมใน Cockpit Zone
ใช้งานตามอุปกรณ์ที่เจ้าหน้าที่จัดเตรียมไว้ ถ้าเชื่อมต่อเสียงไม่ได้ควรแจ้งเจ้าหน้าที่
ฟังเสียงเกมขับรถและเพิ่มความสมจริงระหว่างเล่น [S2]
```

หลัง: strict=True, source_contract_pass, state=answer

```text
Pulse Elite Wireless Headset — สเปก: zone; Cockpit Zone; quantity; 2 Units [S1]

Pulse Elite Wireless Headset — การใช้งาน: หูฟังไร้สายสำหรับใช้งานกับชุดเกมใน Cockpit Zone
ใช้งานตามอุปกรณ์ที่เจ้าหน้าที่จัดเตรียมไว้ ถ้าเชื่อมต่อเสียงไม่ได้ควรแจ้งเจ้าหน้าที่
ฟังเสียงเกมขับรถและเพิ่มความสมจริงระหว่างเล่น [S2]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C03:equipment_pulse_elite_headset:specifications",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C03:equipment_pulse_elite_headset:specifications",
      "record_id": "equipment_pulse_elite_headset",
      "facet": "specifications",
      "value": "key: zone; unit: None; value: Cockpit Zone; key: quantity; unit: None; value: 2 Units",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/specifications",
          "source_id": "r63_64c581ece6269a49f0226f1a14e3"
        }
      ]
    },
    "native_fact_id": "C03:equipment_pulse_elite_headset:specifications",
    "native_record_id": "equipment_pulse_elite_headset",
    "facet": "specifications",
    "value": "key: zone; unit: None; value: Cockpit Zone; key: quantity; unit: None; value: 2 Units",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/specifications",
        "source_id": "r63_64c581ece6269a49f0226f1a14e3"
      }
    ],
    "legacy_record_id": "equipment_pulse_elite_headset"
  },
  {
    "legacy_fact_id": "C03:equipment_pulse_elite_headset:usage",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C03:equipment_pulse_elite_headset:usage",
      "record_id": "equipment_pulse_elite_headset",
      "facet": "usage",
      "value": "หูฟังไร้สายสำหรับใช้งานกับชุดเกมใน Cockpit Zone\nใช้งานตามอุปกรณ์ที่เจ้าหน้าที่จัดเตรียมไว้ ถ้าเชื่อมต่อเสียงไม่ได้ควรแจ้งเจ้าหน้าที่\nฟังเสียงเกมขับรถและเพิ่มความสมจริงระหว่างเล่น",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/usage",
          "source_id": "r66_en_4d455508889a0b18368950f6"
        }
      ]
    },
    "native_fact_id": "C03:equipment_pulse_elite_headset:usage",
    "native_record_id": "equipment_pulse_elite_headset",
    "facet": "usage",
    "value": "หูฟังไร้สายสำหรับใช้งานกับชุดเกมใน Cockpit Zone\nใช้งานตามอุปกรณ์ที่เจ้าหน้าที่จัดเตรียมไว้ ถ้าเชื่อมต่อเสียงไม่ได้ควรแจ้งเจ้าหน้าที่\nฟังเสียงเกมขับรถและเพิ่มความสมจริงระหว่างเล่น",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/usage",
        "source_id": "r66_en_4d455508889a0b18368950f6"
      }
    ],
    "legacy_record_id": "equipment_pulse_elite_headset"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": [
    "C03:equipment_pulse_elite_headset:specifications"
  ]
}
```

## C03-Q073 — อุปกรณ์

ช่วยตอบสั้น ๆ ว่า สเปกของ Racezone Full Cockpit V3 เป็นแบบไหน แล้วขอRacezone Full Cockpit V3 มีข้อมูลเรื่องการใช้งานอย่างไร

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=True, source_contract_pass, state=answer

```text
Racezone Full Cockpit V3 — สเปก: zone; Cockpit Zone; quantity; 2 Units [S1]

Racezone Full Cockpit V3 — การใช้งาน: ชุดเบาะและโครงจำลองการขับรถสำหรับเกมแข่งรถ
นั่งใน Cockpit แล้วใช้พวงมาลัย คันเร่ง และเบรกตามที่ตั้งค่าไว้ในเกม
เล่น Gran Turismo 7 แบบจำลองการขับจริงมากขึ้น [S2]
```

หลัง: strict=True, source_contract_pass, state=answer

```text
Racezone Full Cockpit V3 — สเปก: zone; Cockpit Zone; quantity; 2 Units [S1]

Racezone Full Cockpit V3 — การใช้งาน: ชุดเบาะและโครงจำลองการขับรถสำหรับเกมแข่งรถ
นั่งใน Cockpit แล้วใช้พวงมาลัย คันเร่ง และเบรกตามที่ตั้งค่าไว้ในเกม
เล่น Gran Turismo 7 แบบจำลองการขับจริงมากขึ้น [S2]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C03:equipment_racezone_cockpit_v3:specifications",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C03:equipment_racezone_cockpit_v3:specifications",
      "record_id": "equipment_racezone_cockpit_v3",
      "facet": "specifications",
      "value": "key: zone; unit: None; value: Cockpit Zone; key: quantity; unit: None; value: 2 Units",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/specifications",
          "source_id": "r63_fea21874f4a660846b05684cfaf2"
        }
      ]
    },
    "native_fact_id": "C03:equipment_racezone_cockpit_v3:specifications",
    "native_record_id": "equipment_racezone_cockpit_v3",
    "facet": "specifications",
    "value": "key: zone; unit: None; value: Cockpit Zone; key: quantity; unit: None; value: 2 Units",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/specifications",
        "source_id": "r63_fea21874f4a660846b05684cfaf2"
      }
    ],
    "legacy_record_id": "equipment_racezone_cockpit_v3"
  },
  {
    "legacy_fact_id": "C03:equipment_racezone_cockpit_v3:usage",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C03:equipment_racezone_cockpit_v3:usage",
      "record_id": "equipment_racezone_cockpit_v3",
      "facet": "usage",
      "value": "ชุดเบาะและโครงจำลองการขับรถสำหรับเกมแข่งรถ\nนั่งใน Cockpit แล้วใช้พวงมาลัย คันเร่ง และเบรกตามที่ตั้งค่าไว้ในเกม\nเล่น Gran Turismo 7 แบบจำลองการขับจริงมากขึ้น",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/usage",
          "source_id": "r66_en_e61dfafee3fb9317fefe17b6"
        }
      ]
    },
    "native_fact_id": "C03:equipment_racezone_cockpit_v3:usage",
    "native_record_id": "equipment_racezone_cockpit_v3",
    "facet": "usage",
    "value": "ชุดเบาะและโครงจำลองการขับรถสำหรับเกมแข่งรถ\nนั่งใน Cockpit แล้วใช้พวงมาลัย คันเร่ง และเบรกตามที่ตั้งค่าไว้ในเกม\nเล่น Gran Turismo 7 แบบจำลองการขับจริงมากขึ้น",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/usage",
        "source_id": "r66_en_e61dfafee3fb9317fefe17b6"
      }
    ],
    "legacy_record_id": "equipment_racezone_cockpit_v3"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": [
    "C03:equipment_racezone_cockpit_v3:specifications"
  ]
}
```

## C03-Q075 — อุปกรณ์

กำลังวางแผนไปใช้บริการ เลยขอถามว่า Gaming Keyboard ใช้สเปกอะไร แล้วขอGaming Keyboard อยู่โซนไหน

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=True, source_contract_pass, state=answer

```text
Gaming Keyboard — สเปก: zone; PC Zone [S1]

Gaming Keyboard — ที่ตั้ง: PC Zone [S2]
```

หลัง: strict=True, source_contract_pass, state=answer

```text
Gaming Keyboard — สเปก: zone; PC Zone [S1]

Gaming Keyboard — ที่ตั้ง: PC Zone [S2]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C03:equipment_gaming_keyboard:specifications",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C03:equipment_gaming_keyboard:specifications",
      "record_id": "equipment_gaming_keyboard",
      "facet": "specifications",
      "value": "key: zone; unit: None; value: PC Zone",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/specifications",
          "source_id": "r63_0d4513c308153752dd234ccd5b9f"
        }
      ]
    },
    "native_fact_id": "C03:equipment_gaming_keyboard:specifications",
    "native_record_id": "equipment_gaming_keyboard",
    "facet": "specifications",
    "value": "key: zone; unit: None; value: PC Zone",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/specifications",
        "source_id": "r63_0d4513c308153752dd234ccd5b9f"
      }
    ],
    "legacy_record_id": "equipment_gaming_keyboard"
  },
  {
    "legacy_fact_id": "C03:equipment_gaming_keyboard:location",
    "alignment_kind": "aligned",
    "legacy_expected": {
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
      ]
    },
    "native_fact_id": "C03:equipment_gaming_keyboard:location",
    "native_record_id": "equipment_gaming_keyboard",
    "facet": "location",
    "value": "PC Zone",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/specifications",
        "source_id": "r63_0d4513c308153752dd234ccd5b9f"
      }
    ],
    "legacy_record_id": "equipment_gaming_keyboard"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": [
    "C03:equipment_gaming_keyboard:specifications"
  ]
}
```

## C03-Q076 — อุปกรณ์

รบกวนเช็กให้หน่อย สเปกของ Sofa 2 seats เป็นแบบไหน แล้วขอของรุ่น Sofa 2 seats มีให้ใช้กี่ชุด

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=True, source_contract_pass, state=answer

```text
Sofa 2 seats — สเปก: zone; Nintendo Switch Zone; quantity; 2 Sets [S1]

Sofa 2 seats — จำนวนเครื่อง: 2 Sets [S2]
```

หลัง: strict=True, source_contract_pass, state=answer

```text
Sofa 2 seats — สเปก: zone; Nintendo Switch Zone; quantity; 2 Sets [S1]

Sofa 2 seats — จำนวนเครื่อง: 2 Sets [S2]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C03:equipment_sofa_2_seats:specifications",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C03:equipment_sofa_2_seats:specifications",
      "record_id": "equipment_sofa_2_seats",
      "facet": "specifications",
      "value": "key: zone; unit: None; value: Nintendo Switch Zone; key: quantity; unit: None; value: 2 Sets",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/specifications",
          "source_id": "r63_f1338119c0116b217f74cd5f332a"
        }
      ]
    },
    "native_fact_id": "C03:equipment_sofa_2_seats:specifications",
    "native_record_id": "equipment_sofa_2_seats",
    "facet": "specifications",
    "value": "key: zone; unit: None; value: Nintendo Switch Zone; key: quantity; unit: None; value: 2 Sets",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/specifications",
        "source_id": "r63_f1338119c0116b217f74cd5f332a"
      }
    ],
    "legacy_record_id": "equipment_sofa_2_seats"
  },
  {
    "legacy_fact_id": "C03:equipment_sofa_2_seats:quantity",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C03:equipment_sofa_2_seats:quantity",
      "record_id": "equipment_sofa_2_seats",
      "facet": "quantity",
      "value": "2 Sets",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/specifications",
          "source_id": "r63_f1338119c0116b217f74cd5f332a"
        }
      ]
    },
    "native_fact_id": "C03:equipment_sofa_2_seats:quantity",
    "native_record_id": "equipment_sofa_2_seats",
    "facet": "quantity",
    "value": "2 Sets",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/specifications",
        "source_id": "r63_f1338119c0116b217f74cd5f332a"
      }
    ],
    "legacy_record_id": "equipment_sofa_2_seats"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": [
    "C03:equipment_sofa_2_seats:specifications"
  ]
}
```

## C03-Q079 — อุปกรณ์

ขอสอบถามหน่อยครับ Gaming Chair อยู่โซนไหน แล้วขออยากดูรายละเอียดฮาร์ดแวร์ Gaming Chair

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=True, source_contract_pass, state=answer

```text
Gaming Chair — ที่ตั้ง: PC Zone [S1]

Gaming Chair — สเปก: zone; PC Zone; quantity; 10 Units [S2]
```

หลัง: strict=True, source_contract_pass, state=answer

```text
Gaming Chair — ที่ตั้ง: PC Zone [S1]

Gaming Chair — สเปก: zone; PC Zone; quantity; 10 Units [S2]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C03:equipment_gaming_chair:location",
    "alignment_kind": "aligned",
    "legacy_expected": {
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
      ]
    },
    "native_fact_id": "C03:equipment_gaming_chair:location",
    "native_record_id": "equipment_gaming_chair",
    "facet": "location",
    "value": "PC Zone",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/specifications",
        "source_id": "r63_fc7d8dd97058c5a18e121b2de918"
      }
    ],
    "legacy_record_id": "equipment_gaming_chair"
  },
  {
    "legacy_fact_id": "C03:equipment_gaming_chair:specifications",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C03:equipment_gaming_chair:specifications",
      "record_id": "equipment_gaming_chair",
      "facet": "specifications",
      "value": "key: zone; unit: None; value: PC Zone; key: quantity; unit: None; value: 10 Units",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/specifications",
          "source_id": "r63_fc7d8dd97058c5a18e121b2de918"
        }
      ]
    },
    "native_fact_id": "C03:equipment_gaming_chair:specifications",
    "native_record_id": "equipment_gaming_chair",
    "facet": "specifications",
    "value": "key: zone; unit: None; value: PC Zone; key: quantity; unit: None; value: 10 Units",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/specifications",
        "source_id": "r63_fc7d8dd97058c5a18e121b2de918"
      }
    ],
    "legacy_record_id": "equipment_gaming_chair"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": [
    "C03:equipment_gaming_chair:specifications"
  ]
}
```

## C03-Q082 — อุปกรณ์

ถามจากข้อมูลที่ศูนย์ให้ไว้ ประกันของ Cockpit #01 หมดวันไหน

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, expected_state_mismatch, state=unavailable

```text
ระบบตรวจสอบส่วนนี้ไม่พร้อม จึงยังยืนยันคำตอบไม่ได้ครับ
```

หลัง: strict=True, source_contract_pass, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C06-Q003 — ราคาปกติ

ช่วยตอบสั้น ๆ ว่า rate_recovered_pc_availability_pc_01_02_general_student ใช้ได้ยาวนานเท่าไหร่ถ้าบอกเป็นนาที

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, required_claims_missing, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=True, source_contract_pass, state=answer

```text
PC #01-#02 / PSU Alumni and General Student — นาทีต่อรอบ: 60 [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C06:rate_recovered_pc_availability_pc_01_02_general_student:duration_minutes",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:rate_recovered_pc_availability_pc_01_02_general_student:duration_minutes",
      "record_id": "rate_recovered_pc_availability_pc_01_02_general_student",
      "facet": "duration_minutes",
      "value": "60",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/duration_minutes",
          "source_id": "r66_pc_84c88699ada11a14343702a7"
        }
      ]
    },
    "native_fact_id": "C06:rate_recovered_pc_availability_pc_01_02_general_student:duration_minutes",
    "native_record_id": "rate_recovered_pc_availability_pc_01_02_general_student",
    "facet": "duration_minutes",
    "value": "60",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r66_pc_84c88699ada11a14343702a7"
      }
    ],
    "legacy_record_id": "rate_recovered_pc_availability_pc_01_02_general_student"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C06-Q004 — ราคาปกติ

อยากรู้ว่า migrated_rate_vr_60_1_5_psu_student_staff ให้ใช้นานกี่นาที

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, additional_or_wrong_scope_claims, state=answer

```text
นายธนชาติ เอ่งฉ้วน — ชื่อ: นายธนชาติ เอ่งฉ้วน [S1]
นายชนะชัย สิริพันธ์วราภรณ์ — ชื่อ: นายชนะชัย สิริพันธ์วราภรณ์ [S2]
นางสาวกมลวรรณ นวลสาย — ชื่อ: นางสาวกมลวรรณ นวลสาย [S3]
นางสาวชญาภา จันทร์เอิบ — ชื่อ: นางสาวชญาภา จันทร์เอิบ [S4]
นายษุภากรณ์ จิราจินดากุล — ชื่อ: นายษุภากรณ์ จิราจินดากุล [S5]
นายณัฐวัฒน์ นิธิคุณานนต์ — ชื่อ: นายณัฐวัฒน์ นิธิคุณานนต์ [S6]
รศ.ดร.อซีส นันทอมรพงศ์ — ชื่อ: รศ.ดร.อซีส นันทอมรพงศ์ [S7]
รศ.ดร.พันธ์ ทองชุมนุม — ชื่อ: รศ.ดร.พันธ์ ทองชุมนุม [S8]
นายภาสวุฒิ ชูติประชากิจ — ชื่อ: นายภาสวุฒิ ชูติประชากิจ [S9]
นางสาวอาทิตยา แดงประดับ — ชื่อ: นางสาวอาทิตยา แดงประดับ [S10]
ผศ.ดร.ณัฐพงศ์ ทองเทพ — ชื่อ: ผศ.ดร.ณัฐพงศ์ ทองเทพ [S11]
นายพฤทธิ์ เกษตรสมบูรณ์ — ชื่อ: นายพฤทธิ์ เกษตรสมบูรณ์ [S12]
นางสาวณัฐธิดา คำทะเนตร์ — ชื่อ: นางสาวณัฐธิดา คำทะเนตร์ [S13]
นายณัฐพนธ์ อินทรสังขนาวิน — ชื่อ: นายณัฐพนธ์ อินทรสังขนาวิน [S14]
Mr. Amine Abidellaoui — ชื่อ: Mr. Amine Abidellaoui [S15]
นางสาวสุภาสินี ธนภพ — ชื่อ: นางสาวสุภาสินี ธนภพ [S16]
นายอรรถนนท์ สุขแก้ว — ชื่อ: นายอรรถนนท์ สุขแก้ว [S17]
นายสุพศิน อะนะฝรั่ง — ชื่อ: นายสุพศิน อะนะฝรั่ง [S18]
นายอภิวิชญ์ เลิศกมลรักษ์ — ชื่อ: นายอภิวิชญ์ เลิศกมลรักษ์ [S19]
นายนพัทธ์ ฝอยทอง — ชื่อ: นายนพัทธ์ ฝอยทอง [S20]
นายณภัทร เชื้อเหล่าวานิช — ชื่อ: นายณภัทร เชื้อเหล่าวานิช [S21]
ผศ.ดร.นิวัติ แก้วประดับ — ชื่อ: ผศ.ดร.นิวัติ แก้วประดับ [S22]
Mr. Yanis Igoudjil — ชื่อ: Mr. Yanis Igoudjil [S23]
นายภูจิตร จิรวิริยาภรณ์ — ชื่อ: นายภูจิตร จิรวิริยาภรณ์ [S24]
นายปัณณวิชญ์ หนูเรือง — ชื่อ: นายปัณณวิชญ์ หนูเรือง [S25]
```

หลัง: strict=True, source_contract_pass, state=answer

```text
VR Station 1 ชั่วโมง / PSU Student and Staff — นาทีต่อรอบ: 60 [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C06:migrated_rate_vr_60_1_5_psu_student_staff:duration_minutes",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:migrated_rate_vr_60_1_5_psu_student_staff:duration_minutes",
      "record_id": "migrated_rate_vr_60_1_5_psu_student_staff",
      "facet": "duration_minutes",
      "value": "60",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/duration_minutes",
          "source_id": "r63_0c6eb39e6d72e2f3e1224f7674a7"
        }
      ]
    },
    "native_fact_id": "C06:migrated_rate_vr_60_1_5_psu_student_staff:duration_minutes",
    "native_record_id": "migrated_rate_vr_60_1_5_psu_student_staff",
    "facet": "duration_minutes",
    "value": "60",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r63_0c6eb39e6d72e2f3e1224f7674a7"
      }
    ],
    "legacy_record_id": "migrated_rate_vr_60_1_5_psu_student_staff"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C06-Q006 — ราคาปกติ

รบกวนเช็กให้หน่อย migrated_rate_nintendo_switch_60_1_2_psu_alumni_general_student ใช้ได้ยาวนานเท่าไหร่ถ้าบอกเป็นนาที

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, required_claims_missing, state=unavailable

```text
ระบบตีความคำถามไม่พร้อมชั่วคราว กรุณาลองอีกครั้งครับ
```

หลัง: strict=True, source_contract_pass, state=answer

```text
Nintendo Switch (1-2 Persons) / PSU Alumni and General Student — นาทีต่อรอบ: 60 [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C06:migrated_rate_nintendo_switch_60_1_2_psu_alumni_general_student:duration_minutes",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:migrated_rate_nintendo_switch_60_1_2_psu_alumni_general_student:duration_minutes",
      "record_id": "migrated_rate_nintendo_switch_60_1_2_psu_alumni_general_student",
      "facet": "duration_minutes",
      "value": "60",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/duration_minutes",
          "source_id": "r63_2918da02b8bbc3137d7e8e43ef3d"
        }
      ]
    },
    "native_fact_id": "C06:migrated_rate_nintendo_switch_60_1_2_psu_alumni_general_student:duration_minutes",
    "native_record_id": "migrated_rate_nintendo_switch_60_1_2_psu_alumni_general_student",
    "facet": "duration_minutes",
    "value": "60",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r63_2918da02b8bbc3137d7e8e43ef3d"
      }
    ],
    "legacy_record_id": "migrated_rate_nintendo_switch_60_1_2_psu_alumni_general_student"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C06-Q008 — ราคาปกติ

เวลาใช้งานของ rate_recovered_pc_availability_pc_01_02_psu_student_staff นับเป็นกี่นาที

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, required_claims_missing, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=True, source_contract_pass, state=answer

```text
PC #01-#02 / PSU Student and Staff — นาทีต่อรอบ: 60 [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C06:rate_recovered_pc_availability_pc_01_02_psu_student_staff:duration_minutes",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:rate_recovered_pc_availability_pc_01_02_psu_student_staff:duration_minutes",
      "record_id": "rate_recovered_pc_availability_pc_01_02_psu_student_staff",
      "facet": "duration_minutes",
      "value": "60",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/duration_minutes",
          "source_id": "r66_pc_4cd8af9a21a7cacef4532b65"
        }
      ]
    },
    "native_fact_id": "C06:rate_recovered_pc_availability_pc_01_02_psu_student_staff:duration_minutes",
    "native_record_id": "rate_recovered_pc_availability_pc_01_02_psu_student_staff",
    "facet": "duration_minutes",
    "value": "60",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r66_pc_4cd8af9a21a7cacef4532b65"
      }
    ],
    "legacy_record_id": "rate_recovered_pc_availability_pc_01_02_psu_student_staff"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C06-Q010 — ราคาปกติ

ช่วยตอบสั้น ๆ ว่า migrated_rate_cockpit_60_1_1_psu_student_staff ให้ใช้นานกี่นาที

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, additional_or_wrong_scope_claims, state=answer

```text
นายธนชาติ เอ่งฉ้วน — ชื่อ: นายธนชาติ เอ่งฉ้วน [S1]
นายชนะชัย สิริพันธ์วราภรณ์ — ชื่อ: นายชนะชัย สิริพันธ์วราภรณ์ [S2]
นางสาวกมลวรรณ นวลสาย — ชื่อ: นางสาวกมลวรรณ นวลสาย [S3]
นางสาวชญาภา จันทร์เอิบ — ชื่อ: นางสาวชญาภา จันทร์เอิบ [S4]
นายษุภากรณ์ จิราจินดากุล — ชื่อ: นายษุภากรณ์ จิราจินดากุล [S5]
นายณัฐวัฒน์ นิธิคุณานนต์ — ชื่อ: นายณัฐวัฒน์ นิธิคุณานนต์ [S6]
รศ.ดร.อซีส นันทอมรพงศ์ — ชื่อ: รศ.ดร.อซีส นันทอมรพงศ์ [S7]
รศ.ดร.พันธ์ ทองชุมนุม — ชื่อ: รศ.ดร.พันธ์ ทองชุมนุม [S8]
นายภาสวุฒิ ชูติประชากิจ — ชื่อ: นายภาสวุฒิ ชูติประชากิจ [S9]
นางสาวอาทิตยา แดงประดับ — ชื่อ: นางสาวอาทิตยา แดงประดับ [S10]
ผศ.ดร.ณัฐพงศ์ ทองเทพ — ชื่อ: ผศ.ดร.ณัฐพงศ์ ทองเทพ [S11]
นายพฤทธิ์ เกษตรสมบูรณ์ — ชื่อ: นายพฤทธิ์ เกษตรสมบูรณ์ [S12]
นางสาวณัฐธิดา คำทะเนตร์ — ชื่อ: นางสาวณัฐธิดา คำทะเนตร์ [S13]
นายณัฐพนธ์ อินทรสังขนาวิน — ชื่อ: นายณัฐพนธ์ อินทรสังขนาวิน [S14]
Mr. Amine Abidellaoui — ชื่อ: Mr. Amine Abidellaoui [S15]
นางสาวสุภาสินี ธนภพ — ชื่อ: นางสาวสุภาสินี ธนภพ [S16]
นายอรรถนนท์ สุขแก้ว — ชื่อ: นายอรรถนนท์ สุขแก้ว [S17]
นายสุพศิน อะนะฝรั่ง — ชื่อ: นายสุพศิน อะนะฝรั่ง [S18]
นายอภิวิชญ์ เลิศกมลรักษ์ — ชื่อ: นายอภิวิชญ์ เลิศกมลรักษ์ [S19]
นายนพัทธ์ ฝอยทอง — ชื่อ: นายนพัทธ์ ฝอยทอง [S20]
นายณภัทร เชื้อเหล่าวานิช — ชื่อ: นายณภัทร เชื้อเหล่าวานิช [S21]
ผศ.ดร.นิวัติ แก้วประดับ — ชื่อ: ผศ.ดร.นิวัติ แก้วประดับ [S22]
Mr. Yanis Igoudjil — ชื่อ: Mr. Yanis Igoudjil [S23]
นายภูจิตร จิรวิริยาภรณ์ — ชื่อ: นายภูจิตร จิรวิริยาภรณ์ [S24]
นายปัณณวิชญ์ หนูเรือง — ชื่อ: นายปัณณวิชญ์ หนูเรือง [S25]
```

หลัง: strict=True, source_contract_pass, state=answer

```text
Cockpit #01-#02 / PSU Student and Staff — นาทีต่อรอบ: 60 [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C06:migrated_rate_cockpit_60_1_1_psu_student_staff:duration_minutes",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:migrated_rate_cockpit_60_1_1_psu_student_staff:duration_minutes",
      "record_id": "migrated_rate_cockpit_60_1_1_psu_student_staff",
      "facet": "duration_minutes",
      "value": "60",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/duration_minutes",
          "source_id": "r63_7c1e752ae78e8c2c9389e38b650d"
        }
      ]
    },
    "native_fact_id": "C06:migrated_rate_cockpit_60_1_1_psu_student_staff:duration_minutes",
    "native_record_id": "migrated_rate_cockpit_60_1_1_psu_student_staff",
    "facet": "duration_minutes",
    "value": "60",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r63_7c1e752ae78e8c2c9389e38b650d"
      }
    ],
    "legacy_record_id": "migrated_rate_cockpit_60_1_1_psu_student_staff"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C06-Q016 — ราคาปกติ

ขอสอบถามหน่อยครับ migrated_rate_cockpit_60_1_1_psu_alumni_general_student ให้ใช้นานกี่นาที

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, required_claims_missing, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

หลัง: strict=True, source_contract_pass, state=answer

```text
Cockpit #01-#02 / PSU Alumni and General Student — นาทีต่อรอบ: 60 [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C06:migrated_rate_cockpit_60_1_1_psu_alumni_general_student:duration_minutes",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:migrated_rate_cockpit_60_1_1_psu_alumni_general_student:duration_minutes",
      "record_id": "migrated_rate_cockpit_60_1_1_psu_alumni_general_student",
      "facet": "duration_minutes",
      "value": "60",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/duration_minutes",
          "source_id": "r63_773d8828419240554040c39d9a60"
        }
      ]
    },
    "native_fact_id": "C06:migrated_rate_cockpit_60_1_1_psu_alumni_general_student:duration_minutes",
    "native_record_id": "migrated_rate_cockpit_60_1_1_psu_alumni_general_student",
    "facet": "duration_minutes",
    "value": "60",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r63_773d8828419240554040c39d9a60"
      }
    ],
    "legacy_record_id": "migrated_rate_cockpit_60_1_1_psu_alumni_general_student"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C06-Q023 — ราคาปกติ

ขอสอบถามหน่อยครับ เวลาใช้งานของ migrated_rate_cockpit_60_1_1_general_adult นับเป็นกี่นาที

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, required_claims_missing, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

หลัง: strict=True, source_contract_pass, state=answer

```text
Cockpit #01-#02 / General Adult — นาทีต่อรอบ: 60 [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C06:migrated_rate_cockpit_60_1_1_general_adult:duration_minutes",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:migrated_rate_cockpit_60_1_1_general_adult:duration_minutes",
      "record_id": "migrated_rate_cockpit_60_1_1_general_adult",
      "facet": "duration_minutes",
      "value": "60",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/duration_minutes",
          "source_id": "r63_9671361adf41b3433392c3c8b569"
        }
      ]
    },
    "native_fact_id": "C06:migrated_rate_cockpit_60_1_1_general_adult:duration_minutes",
    "native_record_id": "migrated_rate_cockpit_60_1_1_general_adult",
    "facet": "duration_minutes",
    "value": "60",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r63_9671361adf41b3433392c3c8b569"
      }
    ],
    "legacy_record_id": "migrated_rate_cockpit_60_1_1_general_adult"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C06-Q024 — ราคาปกติ

ช่วยตอบสั้น ๆ ว่า migrated_rate_nintendo_switch_60_1_2_general_adult ใช้ได้ยาวนานเท่าไหร่ถ้าบอกเป็นนาที

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, required_claims_missing, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=True, source_contract_pass, state=answer

```text
Nintendo Switch (1-2 Persons) / General Adult — นาทีต่อรอบ: 60 [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C06:migrated_rate_nintendo_switch_60_1_2_general_adult:duration_minutes",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:migrated_rate_nintendo_switch_60_1_2_general_adult:duration_minutes",
      "record_id": "migrated_rate_nintendo_switch_60_1_2_general_adult",
      "facet": "duration_minutes",
      "value": "60",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/duration_minutes",
          "source_id": "r63_0a1368c5d62847fc27f8d2619cdb"
        }
      ]
    },
    "native_fact_id": "C06:migrated_rate_nintendo_switch_60_1_2_general_adult:duration_minutes",
    "native_record_id": "migrated_rate_nintendo_switch_60_1_2_general_adult",
    "facet": "duration_minutes",
    "value": "60",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r63_0a1368c5d62847fc27f8d2619cdb"
      }
    ],
    "legacy_record_id": "migrated_rate_nintendo_switch_60_1_2_general_adult"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C06-Q027 — ราคาปกติ

รบกวนเช็กให้หน่อย migrated_rate_vr_30_1_5_psu_student_staff ใช้ได้ยาวนานเท่าไหร่ถ้าบอกเป็นนาที

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, additional_or_wrong_scope_claims, state=answer

```text
นายธนชาติ เอ่งฉ้วน — ชื่อ: นายธนชาติ เอ่งฉ้วน [S1]
นายชนะชัย สิริพันธ์วราภรณ์ — ชื่อ: นายชนะชัย สิริพันธ์วราภรณ์ [S2]
นางสาวกมลวรรณ นวลสาย — ชื่อ: นางสาวกมลวรรณ นวลสาย [S3]
นางสาวชญาภา จันทร์เอิบ — ชื่อ: นางสาวชญาภา จันทร์เอิบ [S4]
นายษุภากรณ์ จิราจินดากุล — ชื่อ: นายษุภากรณ์ จิราจินดากุล [S5]
นายณัฐวัฒน์ นิธิคุณานนต์ — ชื่อ: นายณัฐวัฒน์ นิธิคุณานนต์ [S6]
รศ.ดร.อซีส นันทอมรพงศ์ — ชื่อ: รศ.ดร.อซีส นันทอมรพงศ์ [S7]
รศ.ดร.พันธ์ ทองชุมนุม — ชื่อ: รศ.ดร.พันธ์ ทองชุมนุม [S8]
นายภาสวุฒิ ชูติประชากิจ — ชื่อ: นายภาสวุฒิ ชูติประชากิจ [S9]
นางสาวอาทิตยา แดงประดับ — ชื่อ: นางสาวอาทิตยา แดงประดับ [S10]
ผศ.ดร.ณัฐพงศ์ ทองเทพ — ชื่อ: ผศ.ดร.ณัฐพงศ์ ทองเทพ [S11]
นายพฤทธิ์ เกษตรสมบูรณ์ — ชื่อ: นายพฤทธิ์ เกษตรสมบูรณ์ [S12]
นางสาวณัฐธิดา คำทะเนตร์ — ชื่อ: นางสาวณัฐธิดา คำทะเนตร์ [S13]
นายณัฐพนธ์ อินทรสังขนาวิน — ชื่อ: นายณัฐพนธ์ อินทรสังขนาวิน [S14]
Mr. Amine Abidellaoui — ชื่อ: Mr. Amine Abidellaoui [S15]
นางสาวสุภาสินี ธนภพ — ชื่อ: นางสาวสุภาสินี ธนภพ [S16]
นายอรรถนนท์ สุขแก้ว — ชื่อ: นายอรรถนนท์ สุขแก้ว [S17]
นายสุพศิน อะนะฝรั่ง — ชื่อ: นายสุพศิน อะนะฝรั่ง [S18]
นายอภิวิชญ์ เลิศกมลรักษ์ — ชื่อ: นายอภิวิชญ์ เลิศกมลรักษ์ [S19]
นายนพัทธ์ ฝอยทอง — ชื่อ: นายนพัทธ์ ฝอยทอง [S20]
นายณภัทร เชื้อเหล่าวานิช — ชื่อ: นายณภัทร เชื้อเหล่าวานิช [S21]
ผศ.ดร.นิวัติ แก้วประดับ — ชื่อ: ผศ.ดร.นิวัติ แก้วประดับ [S22]
Mr. Yanis Igoudjil — ชื่อ: Mr. Yanis Igoudjil [S23]
นายภูจิตร จิรวิริยาภรณ์ — ชื่อ: นายภูจิตร จิรวิริยาภรณ์ [S24]
นายปัณณวิชญ์ หนูเรือง — ชื่อ: นายปัณณวิชญ์ หนูเรือง [S25]
```

หลัง: strict=True, source_contract_pass, state=answer

```text
VR Station 30 นาที / PSU Student and Staff — นาทีต่อรอบ: 30 [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C06:migrated_rate_vr_30_1_5_psu_student_staff:duration_minutes",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:migrated_rate_vr_30_1_5_psu_student_staff:duration_minutes",
      "record_id": "migrated_rate_vr_30_1_5_psu_student_staff",
      "facet": "duration_minutes",
      "value": "30",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/duration_minutes",
          "source_id": "r63_f75ddf25f2e0dd94c12889e2ac05"
        }
      ]
    },
    "native_fact_id": "C06:migrated_rate_vr_30_1_5_psu_student_staff:duration_minutes",
    "native_record_id": "migrated_rate_vr_30_1_5_psu_student_staff",
    "facet": "duration_minutes",
    "value": "30",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r63_f75ddf25f2e0dd94c12889e2ac05"
      }
    ],
    "legacy_record_id": "migrated_rate_vr_30_1_5_psu_student_staff"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C06-Q028 — ราคาปกติ

ถามจากข้อมูลที่ศูนย์ให้ไว้ migrated_rate_vr_30_1_5_psu_alumni_general_student ให้ใช้นานกี่นาที

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, additional_or_wrong_scope_claims, state=answer

```text
VR Station 30 นาที — รายชื่อเกมทั้งหมด: Beat Saber; Horizon Call of the Mountain; Resident Evil 4; Resident Evil Village [S1]
```

หลัง: strict=True, source_contract_pass, state=answer

```text
VR Station 30 นาที / PSU Alumni and General Student — นาทีต่อรอบ: 30 [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C06:migrated_rate_vr_30_1_5_psu_alumni_general_student:duration_minutes",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:migrated_rate_vr_30_1_5_psu_alumni_general_student:duration_minutes",
      "record_id": "migrated_rate_vr_30_1_5_psu_alumni_general_student",
      "facet": "duration_minutes",
      "value": "30",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/duration_minutes",
          "source_id": "r63_d4d5a0745b2e65f3acc6829507db"
        }
      ]
    },
    "native_fact_id": "C06:migrated_rate_vr_30_1_5_psu_alumni_general_student:duration_minutes",
    "native_record_id": "migrated_rate_vr_30_1_5_psu_alumni_general_student",
    "facet": "duration_minutes",
    "value": "30",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r63_d4d5a0745b2e65f3acc6829507db"
      }
    ],
    "legacy_record_id": "migrated_rate_vr_30_1_5_psu_alumni_general_student"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C06-Q030 — ราคาปกติ

ขอสอบถามหน่อยครับ rate_recovered_pc_availability_pc_03_10_general_adult ใช้ได้ยาวนานเท่าไหร่ถ้าบอกเป็นนาที

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, required_claims_missing, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=True, source_contract_pass, state=answer

```text
PC #03-#10 / General Adult — นาทีต่อรอบ: 60 [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C06:rate_recovered_pc_availability_pc_03_10_general_adult:duration_minutes",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:rate_recovered_pc_availability_pc_03_10_general_adult:duration_minutes",
      "record_id": "rate_recovered_pc_availability_pc_03_10_general_adult",
      "facet": "duration_minutes",
      "value": "60",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/duration_minutes",
          "source_id": "r66_pc_dc5b4c42405e267135bbf1f8"
        }
      ]
    },
    "native_fact_id": "C06:rate_recovered_pc_availability_pc_03_10_general_adult:duration_minutes",
    "native_record_id": "rate_recovered_pc_availability_pc_03_10_general_adult",
    "facet": "duration_minutes",
    "value": "60",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r66_pc_dc5b4c42405e267135bbf1f8"
      }
    ],
    "legacy_record_id": "rate_recovered_pc_availability_pc_03_10_general_adult"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C06-Q031 — ราคาปกติ

ช่วยตอบสั้น ๆ ว่า rate_recovered_pc_availability_pc_03_10_general_student ให้ใช้นานกี่นาที

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, required_claims_missing, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=True, source_contract_pass, state=answer

```text
PC #03-#10 / PSU Alumni and General Student — นาทีต่อรอบ: 60 [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C06:rate_recovered_pc_availability_pc_03_10_general_student:duration_minutes",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:rate_recovered_pc_availability_pc_03_10_general_student:duration_minutes",
      "record_id": "rate_recovered_pc_availability_pc_03_10_general_student",
      "facet": "duration_minutes",
      "value": "60",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/duration_minutes",
          "source_id": "r66_pc_b9251e4f325511ac1fc7611d"
        }
      ]
    },
    "native_fact_id": "C06:rate_recovered_pc_availability_pc_03_10_general_student:duration_minutes",
    "native_record_id": "rate_recovered_pc_availability_pc_03_10_general_student",
    "facet": "duration_minutes",
    "value": "60",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r66_pc_b9251e4f325511ac1fc7611d"
      }
    ],
    "legacy_record_id": "rate_recovered_pc_availability_pc_03_10_general_student"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C06-Q032 — ราคาปกติ

อยากรู้ว่า เวลาใช้งานของ migrated_rate_vr_60_1_5_psu_alumni_general_student นับเป็นกี่นาที

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, additional_or_wrong_scope_claims, state=answer

```text
VR Station 1 ชั่วโมง — รายชื่อเกมทั้งหมด: Beat Saber; Horizon Call of the Mountain; Resident Evil 4; Resident Evil Village [S1]
```

หลัง: strict=True, source_contract_pass, state=answer

```text
VR Station 1 ชั่วโมง / PSU Alumni and General Student — นาทีต่อรอบ: 60 [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C06:migrated_rate_vr_60_1_5_psu_alumni_general_student:duration_minutes",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:migrated_rate_vr_60_1_5_psu_alumni_general_student:duration_minutes",
      "record_id": "migrated_rate_vr_60_1_5_psu_alumni_general_student",
      "facet": "duration_minutes",
      "value": "60",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/duration_minutes",
          "source_id": "r63_b4d09ed83a76bc1f15a4563652ed"
        }
      ]
    },
    "native_fact_id": "C06:migrated_rate_vr_60_1_5_psu_alumni_general_student:duration_minutes",
    "native_record_id": "migrated_rate_vr_60_1_5_psu_alumni_general_student",
    "facet": "duration_minutes",
    "value": "60",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r63_b4d09ed83a76bc1f15a4563652ed"
      }
    ],
    "legacy_record_id": "migrated_rate_vr_60_1_5_psu_alumni_general_student"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C06-Q036 — ราคาปกติ

migrated_rate_nintendo_switch_60_1_2_psu_student_staff ใช้ได้ยาวนานเท่าไหร่ถ้าบอกเป็นนาที

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, additional_or_wrong_scope_claims, state=answer

```text
นายธนชาติ เอ่งฉ้วน — ชื่อ: นายธนชาติ เอ่งฉ้วน [S1]
นายชนะชัย สิริพันธ์วราภรณ์ — ชื่อ: นายชนะชัย สิริพันธ์วราภรณ์ [S2]
นางสาวกมลวรรณ นวลสาย — ชื่อ: นางสาวกมลวรรณ นวลสาย [S3]
นางสาวชญาภา จันทร์เอิบ — ชื่อ: นางสาวชญาภา จันทร์เอิบ [S4]
นายษุภากรณ์ จิราจินดากุล — ชื่อ: นายษุภากรณ์ จิราจินดากุล [S5]
นายณัฐวัฒน์ นิธิคุณานนต์ — ชื่อ: นายณัฐวัฒน์ นิธิคุณานนต์ [S6]
รศ.ดร.อซีส นันทอมรพงศ์ — ชื่อ: รศ.ดร.อซีส นันทอมรพงศ์ [S7]
รศ.ดร.พันธ์ ทองชุมนุม — ชื่อ: รศ.ดร.พันธ์ ทองชุมนุม [S8]
นายภาสวุฒิ ชูติประชากิจ — ชื่อ: นายภาสวุฒิ ชูติประชากิจ [S9]
นางสาวอาทิตยา แดงประดับ — ชื่อ: นางสาวอาทิตยา แดงประดับ [S10]
ผศ.ดร.ณัฐพงศ์ ทองเทพ — ชื่อ: ผศ.ดร.ณัฐพงศ์ ทองเทพ [S11]
นายพฤทธิ์ เกษตรสมบูรณ์ — ชื่อ: นายพฤทธิ์ เกษตรสมบูรณ์ [S12]
นางสาวณัฐธิดา คำทะเนตร์ — ชื่อ: นางสาวณัฐธิดา คำทะเนตร์ [S13]
นายณัฐพนธ์ อินทรสังขนาวิน — ชื่อ: นายณัฐพนธ์ อินทรสังขนาวิน [S14]
Mr. Amine Abidellaoui — ชื่อ: Mr. Amine Abidellaoui [S15]
นางสาวสุภาสินี ธนภพ — ชื่อ: นางสาวสุภาสินี ธนภพ [S16]
นายอรรถนนท์ สุขแก้ว — ชื่อ: นายอรรถนนท์ สุขแก้ว [S17]
นายสุพศิน อะนะฝรั่ง — ชื่อ: นายสุพศิน อะนะฝรั่ง [S18]
นายอภิวิชญ์ เลิศกมลรักษ์ — ชื่อ: นายอภิวิชญ์ เลิศกมลรักษ์ [S19]
นายนพัทธ์ ฝอยทอง — ชื่อ: นายนพัทธ์ ฝอยทอง [S20]
นายณภัทร เชื้อเหล่าวานิช — ชื่อ: นายณภัทร เชื้อเหล่าวานิช [S21]
ผศ.ดร.นิวัติ แก้วประดับ — ชื่อ: ผศ.ดร.นิวัติ แก้วประดับ [S22]
Mr. Yanis Igoudjil — ชื่อ: Mr. Yanis Igoudjil [S23]
นายภูจิตร จิรวิริยาภรณ์ — ชื่อ: นายภูจิตร จิรวิริยาภรณ์ [S24]
นายปัณณวิชญ์ หนูเรือง — ชื่อ: นายปัณณวิชญ์ หนูเรือง [S25]
```

หลัง: strict=True, source_contract_pass, state=answer

```text
Nintendo Switch (1-2 Persons) / PSU Student and Staff — นาทีต่อรอบ: 60 [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C06:migrated_rate_nintendo_switch_60_1_2_psu_student_staff:duration_minutes",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:migrated_rate_nintendo_switch_60_1_2_psu_student_staff:duration_minutes",
      "record_id": "migrated_rate_nintendo_switch_60_1_2_psu_student_staff",
      "facet": "duration_minutes",
      "value": "60",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/duration_minutes",
          "source_id": "r63_579558a2b15e8e637e4bae93493c"
        }
      ]
    },
    "native_fact_id": "C06:migrated_rate_nintendo_switch_60_1_2_psu_student_staff:duration_minutes",
    "native_record_id": "migrated_rate_nintendo_switch_60_1_2_psu_student_staff",
    "facet": "duration_minutes",
    "value": "60",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r63_579558a2b15e8e637e4bae93493c"
      }
    ],
    "legacy_record_id": "migrated_rate_nintendo_switch_60_1_2_psu_student_staff"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C06-Q037 — ราคาปกติ

ขอสอบถามหน่อยครับ migrated_rate_playstation_5_60_1_2_psu_alumni_general_student ให้ใช้นานกี่นาที

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, required_claims_missing, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=True, source_contract_pass, state=answer

```text
PlayStation 5 #01-#02 / PSU Alumni and General Student — นาทีต่อรอบ: 60 [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C06:migrated_rate_playstation_5_60_1_2_psu_alumni_general_student:duration_minutes",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:migrated_rate_playstation_5_60_1_2_psu_alumni_general_student:duration_minutes",
      "record_id": "migrated_rate_playstation_5_60_1_2_psu_alumni_general_student",
      "facet": "duration_minutes",
      "value": "60",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/duration_minutes",
          "source_id": "r63_35a6cefed055bfc60db380f2e0df"
        }
      ]
    },
    "native_fact_id": "C06:migrated_rate_playstation_5_60_1_2_psu_alumni_general_student:duration_minutes",
    "native_record_id": "migrated_rate_playstation_5_60_1_2_psu_alumni_general_student",
    "facet": "duration_minutes",
    "value": "60",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r63_35a6cefed055bfc60db380f2e0df"
      }
    ],
    "legacy_record_id": "migrated_rate_playstation_5_60_1_2_psu_alumni_general_student"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C06-Q039 — ราคาปกติ

อยากรู้ว่า migrated_rate_vr_60_1_5_general_adult ใช้ได้ยาวนานเท่าไหร่ถ้าบอกเป็นนาที

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, required_claims_missing, state=unavailable

```text
ระบบตรวจสอบส่วนนี้ไม่พร้อม จึงยังยืนยันคำตอบไม่ได้ครับ
```

หลัง: strict=True, source_contract_pass, state=answer

```text
VR Station 1 ชั่วโมง / General Adult — นาทีต่อรอบ: 60 [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C06:migrated_rate_vr_60_1_5_general_adult:duration_minutes",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:migrated_rate_vr_60_1_5_general_adult:duration_minutes",
      "record_id": "migrated_rate_vr_60_1_5_general_adult",
      "facet": "duration_minutes",
      "value": "60",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/duration_minutes",
          "source_id": "r63_c9bbab5aacb07f3adf90aab858e0"
        }
      ]
    },
    "native_fact_id": "C06:migrated_rate_vr_60_1_5_general_adult:duration_minutes",
    "native_record_id": "migrated_rate_vr_60_1_5_general_adult",
    "facet": "duration_minutes",
    "value": "60",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r63_c9bbab5aacb07f3adf90aab858e0"
      }
    ],
    "legacy_record_id": "migrated_rate_vr_60_1_5_general_adult"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C06-Q040 — ราคาปกติ

กำลังวางแผนไปใช้บริการ เลยขอถามว่า rate_recovered_pc_availability_pc_03_10_psu_student_staff ให้ใช้นานกี่นาที

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, required_claims_missing, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=True, source_contract_pass, state=answer

```text
PC #03-#10 / PSU Student and Staff — นาทีต่อรอบ: 60 [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C06:rate_recovered_pc_availability_pc_03_10_psu_student_staff:duration_minutes",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:rate_recovered_pc_availability_pc_03_10_psu_student_staff:duration_minutes",
      "record_id": "rate_recovered_pc_availability_pc_03_10_psu_student_staff",
      "facet": "duration_minutes",
      "value": "60",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/duration_minutes",
          "source_id": "r66_pc_58034b8509494c7ee96cf734"
        }
      ]
    },
    "native_fact_id": "C06:rate_recovered_pc_availability_pc_03_10_psu_student_staff:duration_minutes",
    "native_record_id": "rate_recovered_pc_availability_pc_03_10_psu_student_staff",
    "facet": "duration_minutes",
    "value": "60",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r66_pc_58034b8509494c7ee96cf734"
      }
    ],
    "legacy_record_id": "rate_recovered_pc_availability_pc_03_10_psu_student_staff"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C06-Q041 — ราคาปกติ

รบกวนเช็กให้หน่อย เวลาใช้งานของ migrated_rate_nintendo_switch_60_3_4_psu_alumni_general_student นับเป็นกี่นาที

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, required_claims_missing, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=True, source_contract_pass, state=answer

```text
Nintendo Switch (1-4 Persons) / PSU Alumni and General Student — นาทีต่อรอบ: 60 [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C06:migrated_rate_nintendo_switch_60_3_4_psu_alumni_general_student:duration_minutes",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:migrated_rate_nintendo_switch_60_3_4_psu_alumni_general_student:duration_minutes",
      "record_id": "migrated_rate_nintendo_switch_60_3_4_psu_alumni_general_student",
      "facet": "duration_minutes",
      "value": "60",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/duration_minutes",
          "source_id": "r63_410cf626364d0b283b3d8f674555"
        }
      ]
    },
    "native_fact_id": "C06:migrated_rate_nintendo_switch_60_3_4_psu_alumni_general_student:duration_minutes",
    "native_record_id": "migrated_rate_nintendo_switch_60_3_4_psu_alumni_general_student",
    "facet": "duration_minutes",
    "value": "60",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r63_410cf626364d0b283b3d8f674555"
      }
    ],
    "legacy_record_id": "migrated_rate_nintendo_switch_60_3_4_psu_alumni_general_student"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C06-Q042 — ราคาปกติ

ถามจากข้อมูลที่ศูนย์ให้ไว้ migrated_rate_nintendo_switch_60_3_4_general_adult ใช้ได้ยาวนานเท่าไหร่ถ้าบอกเป็นนาที

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, required_claims_missing, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=True, source_contract_pass, state=answer

```text
Nintendo Switch (1-4 Persons) / General Adult — นาทีต่อรอบ: 60 [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C06:migrated_rate_nintendo_switch_60_3_4_general_adult:duration_minutes",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:migrated_rate_nintendo_switch_60_3_4_general_adult:duration_minutes",
      "record_id": "migrated_rate_nintendo_switch_60_3_4_general_adult",
      "facet": "duration_minutes",
      "value": "60",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/duration_minutes",
          "source_id": "r63_6677e51768e0aa9b8d52ff1e2cd1"
        }
      ]
    },
    "native_fact_id": "C06:migrated_rate_nintendo_switch_60_3_4_general_adult:duration_minutes",
    "native_record_id": "migrated_rate_nintendo_switch_60_3_4_general_adult",
    "facet": "duration_minutes",
    "value": "60",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r63_6677e51768e0aa9b8d52ff1e2cd1"
      }
    ],
    "legacy_record_id": "migrated_rate_nintendo_switch_60_3_4_general_adult"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C06-Q044 — ราคาปกติ

ขอสอบถามหน่อยครับ เวลาใช้งานของ migrated_rate_playstation_5_60_1_2_general_adult นับเป็นกี่นาที

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, required_claims_missing, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=True, source_contract_pass, state=answer

```text
PlayStation 5 #01-#02 / General Adult — นาทีต่อรอบ: 60 [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C06:migrated_rate_playstation_5_60_1_2_general_adult:duration_minutes",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:migrated_rate_playstation_5_60_1_2_general_adult:duration_minutes",
      "record_id": "migrated_rate_playstation_5_60_1_2_general_adult",
      "facet": "duration_minutes",
      "value": "60",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/duration_minutes",
          "source_id": "r63_3ef986791e0dd5833920ff6840db"
        }
      ]
    },
    "native_fact_id": "C06:migrated_rate_playstation_5_60_1_2_general_adult:duration_minutes",
    "native_record_id": "migrated_rate_playstation_5_60_1_2_general_adult",
    "facet": "duration_minutes",
    "value": "60",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r63_3ef986791e0dd5833920ff6840db"
      }
    ],
    "legacy_record_id": "migrated_rate_playstation_5_60_1_2_general_adult"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C06-Q047 — ราคาปกติ

กำลังวางแผนไปใช้บริการ เลยขอถามว่า เวลาใช้งานของ migrated_rate_vr_30_1_5_general_adult นับเป็นกี่นาที

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, additional_or_wrong_scope_claims, state=answer

```text
VR Station 30 นาที — รายชื่อเกมทั้งหมด: Beat Saber; Horizon Call of the Mountain; Resident Evil 4; Resident Evil Village [S1]
```

หลัง: strict=True, source_contract_pass, state=answer

```text
VR Station 30 นาที / General Adult — นาทีต่อรอบ: 30 [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C06:migrated_rate_vr_30_1_5_general_adult:duration_minutes",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:migrated_rate_vr_30_1_5_general_adult:duration_minutes",
      "record_id": "migrated_rate_vr_30_1_5_general_adult",
      "facet": "duration_minutes",
      "value": "30",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/duration_minutes",
          "source_id": "r63_15ad37bbca1867990b52071d9877"
        }
      ]
    },
    "native_fact_id": "C06:migrated_rate_vr_30_1_5_general_adult:duration_minutes",
    "native_record_id": "migrated_rate_vr_30_1_5_general_adult",
    "facet": "duration_minutes",
    "value": "30",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r63_15ad37bbca1867990b52071d9877"
      }
    ],
    "legacy_record_id": "migrated_rate_vr_30_1_5_general_adult"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C06-Q049 — ราคาปกติ

ถามจากข้อมูลที่ศูนย์ให้ไว้ rate_recovered_pc_availability_pc_01_02_general_adult ให้ใช้นานกี่นาที

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, required_claims_missing, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=True, source_contract_pass, state=answer

```text
PC #01-#02 / General Adult — นาทีต่อรอบ: 60 [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C06:rate_recovered_pc_availability_pc_01_02_general_adult:duration_minutes",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:rate_recovered_pc_availability_pc_01_02_general_adult:duration_minutes",
      "record_id": "rate_recovered_pc_availability_pc_01_02_general_adult",
      "facet": "duration_minutes",
      "value": "60",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/duration_minutes",
          "source_id": "r66_pc_97cb854afb6e7b14fc121fbd"
        }
      ]
    },
    "native_fact_id": "C06:rate_recovered_pc_availability_pc_01_02_general_adult:duration_minutes",
    "native_record_id": "rate_recovered_pc_availability_pc_01_02_general_adult",
    "facet": "duration_minutes",
    "value": "60",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r66_pc_97cb854afb6e7b14fc121fbd"
      }
    ],
    "legacy_record_id": "rate_recovered_pc_availability_pc_01_02_general_adult"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C06-Q050 — ราคาปกติ

เวลาใช้งานของ migrated_rate_nintendo_switch_60_3_4_psu_student_staff นับเป็นกี่นาที

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, additional_or_wrong_scope_claims, state=answer

```text
นายธนชาติ เอ่งฉ้วน — ชื่อ: นายธนชาติ เอ่งฉ้วน [S1]
นายชนะชัย สิริพันธ์วราภรณ์ — ชื่อ: นายชนะชัย สิริพันธ์วราภรณ์ [S2]
นางสาวกมลวรรณ นวลสาย — ชื่อ: นางสาวกมลวรรณ นวลสาย [S3]
นางสาวชญาภา จันทร์เอิบ — ชื่อ: นางสาวชญาภา จันทร์เอิบ [S4]
นายษุภากรณ์ จิราจินดากุล — ชื่อ: นายษุภากรณ์ จิราจินดากุล [S5]
นายณัฐวัฒน์ นิธิคุณานนต์ — ชื่อ: นายณัฐวัฒน์ นิธิคุณานนต์ [S6]
รศ.ดร.อซีส นันทอมรพงศ์ — ชื่อ: รศ.ดร.อซีส นันทอมรพงศ์ [S7]
รศ.ดร.พันธ์ ทองชุมนุม — ชื่อ: รศ.ดร.พันธ์ ทองชุมนุม [S8]
นายภาสวุฒิ ชูติประชากิจ — ชื่อ: นายภาสวุฒิ ชูติประชากิจ [S9]
นางสาวอาทิตยา แดงประดับ — ชื่อ: นางสาวอาทิตยา แดงประดับ [S10]
ผศ.ดร.ณัฐพงศ์ ทองเทพ — ชื่อ: ผศ.ดร.ณัฐพงศ์ ทองเทพ [S11]
นายพฤทธิ์ เกษตรสมบูรณ์ — ชื่อ: นายพฤทธิ์ เกษตรสมบูรณ์ [S12]
นางสาวณัฐธิดา คำทะเนตร์ — ชื่อ: นางสาวณัฐธิดา คำทะเนตร์ [S13]
นายณัฐพนธ์ อินทรสังขนาวิน — ชื่อ: นายณัฐพนธ์ อินทรสังขนาวิน [S14]
Mr. Amine Abidellaoui — ชื่อ: Mr. Amine Abidellaoui [S15]
นางสาวสุภาสินี ธนภพ — ชื่อ: นางสาวสุภาสินี ธนภพ [S16]
นายอรรถนนท์ สุขแก้ว — ชื่อ: นายอรรถนนท์ สุขแก้ว [S17]
นายสุพศิน อะนะฝรั่ง — ชื่อ: นายสุพศิน อะนะฝรั่ง [S18]
นายอภิวิชญ์ เลิศกมลรักษ์ — ชื่อ: นายอภิวิชญ์ เลิศกมลรักษ์ [S19]
นายนพัทธ์ ฝอยทอง — ชื่อ: นายนพัทธ์ ฝอยทอง [S20]
นายณภัทร เชื้อเหล่าวานิช — ชื่อ: นายณภัทร เชื้อเหล่าวานิช [S21]
ผศ.ดร.นิวัติ แก้วประดับ — ชื่อ: ผศ.ดร.นิวัติ แก้วประดับ [S22]
Mr. Yanis Igoudjil — ชื่อ: Mr. Yanis Igoudjil [S23]
นายภูจิตร จิรวิริยาภรณ์ — ชื่อ: นายภูจิตร จิรวิริยาภรณ์ [S24]
นายปัณณวิชญ์ หนูเรือง — ชื่อ: นายปัณณวิชญ์ หนูเรือง [S25]
```

หลัง: strict=True, source_contract_pass, state=answer

```text
Nintendo Switch (1-4 Persons) / PSU Student and Staff — นาทีต่อรอบ: 60 [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C06:migrated_rate_nintendo_switch_60_3_4_psu_student_staff:duration_minutes",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:migrated_rate_nintendo_switch_60_3_4_psu_student_staff:duration_minutes",
      "record_id": "migrated_rate_nintendo_switch_60_3_4_psu_student_staff",
      "facet": "duration_minutes",
      "value": "60",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/duration_minutes",
          "source_id": "r63_21b1df3a0034f4b777a930ca3923"
        }
      ]
    },
    "native_fact_id": "C06:migrated_rate_nintendo_switch_60_3_4_psu_student_staff:duration_minutes",
    "native_record_id": "migrated_rate_nintendo_switch_60_3_4_psu_student_staff",
    "facet": "duration_minutes",
    "value": "60",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r63_21b1df3a0034f4b777a930ca3923"
      }
    ],
    "legacy_record_id": "migrated_rate_nintendo_switch_60_3_4_psu_student_staff"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C06-Q051 — ราคาปกติ

How many minutes does migrated_rate_playstation_5_60_1_2_psu_student_staff cover?

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, additional_or_wrong_scope_claims, state=answer

```text
นายธนชาติ เอ่งฉ้วน — name: นายธนชาติ เอ่งฉ้วน [S1]
นายชนะชัย สิริพันธ์วราภรณ์ — name: นายชนะชัย สิริพันธ์วราภรณ์ [S2]
นางสาวกมลวรรณ นวลสาย — name: นางสาวกมลวรรณ นวลสาย [S3]
นางสาวชญาภา จันทร์เอิบ — name: นางสาวชญาภา จันทร์เอิบ [S4]
นายษุภากรณ์ จิราจินดากุล — name: นายษุภากรณ์ จิราจินดากุล [S5]
นายณัฐวัฒน์ นิธิคุณานนต์ — name: นายณัฐวัฒน์ นิธิคุณานนต์ [S6]
รศ.ดร.อซีส นันทอมรพงศ์ — name: รศ.ดร.อซีส นันทอมรพงศ์ [S7]
รศ.ดร.พันธ์ ทองชุมนุม — name: รศ.ดร.พันธ์ ทองชุมนุม [S8]
นายภาสวุฒิ ชูติประชากิจ — name: นายภาสวุฒิ ชูติประชากิจ [S9]
นางสาวอาทิตยา แดงประดับ — name: นางสาวอาทิตยา แดงประดับ [S10]
ผศ.ดร.ณัฐพงศ์ ทองเทพ — name: ผศ.ดร.ณัฐพงศ์ ทองเทพ [S11]
นายพฤทธิ์ เกษตรสมบูรณ์ — name: นายพฤทธิ์ เกษตรสมบูรณ์ [S12]
นางสาวณัฐธิดา คำทะเนตร์ — name: นางสาวณัฐธิดา คำทะเนตร์ [S13]
นายณัฐพนธ์ อินทรสังขนาวิน — name: นายณัฐพนธ์ อินทรสังขนาวิน [S14]
Mr. Amine Abidellaoui — name: Mr. Amine Abidellaoui [S15]
นางสาวสุภาสินี ธนภพ — name: นางสาวสุภาสินี ธนภพ [S16]
นายอรรถนนท์ สุขแก้ว — name: นายอรรถนนท์ สุขแก้ว [S17]
นายสุพศิน อะนะฝรั่ง — name: นายสุพศิน อะนะฝรั่ง [S18]
นายอภิวิชญ์ เลิศกมลรักษ์ — name: นายอภิวิชญ์ เลิศกมลรักษ์ [S19]
นายนพัทธ์ ฝอยทอง — name: นายนพัทธ์ ฝอยทอง [S20]
นายณภัทร เชื้อเหล่าวานิช — name: นายณภัทร เชื้อเหล่าวานิช [S21]
ผศ.ดร.นิวัติ แก้วประดับ — name: ผศ.ดร.นิวัติ แก้วประดับ [S22]
Mr. Yanis Igoudjil — name: Mr. Yanis Igoudjil [S23]
นายภูจิตร จิรวิริยาภรณ์ — name: นายภูจิตร จิรวิริยาภรณ์ [S24]
นายปัณณวิชญ์ หนูเรือง — name: นายปัณณวิชญ์ หนูเรือง [S25]
```

หลัง: strict=True, source_contract_pass, state=answer

```text
PlayStation 5 #01-#02 / PSU Student and Staff — minutes per session: 60 [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C06:migrated_rate_playstation_5_60_1_2_psu_student_staff:duration_minutes",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:migrated_rate_playstation_5_60_1_2_psu_student_staff:duration_minutes",
      "record_id": "migrated_rate_playstation_5_60_1_2_psu_student_staff",
      "facet": "duration_minutes",
      "value": "60",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/duration_minutes",
          "source_id": "r63_db0d7d309783280c60aff0c31a72"
        }
      ]
    },
    "native_fact_id": "C06:migrated_rate_playstation_5_60_1_2_psu_student_staff:duration_minutes",
    "native_record_id": "migrated_rate_playstation_5_60_1_2_psu_student_staff",
    "facet": "duration_minutes",
    "value": "60",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r63_db0d7d309783280c60aff0c31a72"
      }
    ],
    "legacy_record_id": "migrated_rate_playstation_5_60_1_2_psu_student_staff"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C06-Q054 — ราคาปกติ

I would like to know: What is the duration of rate_recovered_pc_availability_pc_01_02_general_student, in minutes?

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, required_claims_missing, state=unavailable

```text
No confirmed live binding is available, so occupancy cannot be checked.
```

หลัง: strict=True, source_contract_pass, state=answer

```text
PC #01-#02 / PSU Alumni and General Student — minutes per session: 60 [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C06:rate_recovered_pc_availability_pc_01_02_general_student:duration_minutes",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:rate_recovered_pc_availability_pc_01_02_general_student:duration_minutes",
      "record_id": "rate_recovered_pc_availability_pc_01_02_general_student",
      "facet": "duration_minutes",
      "value": "60",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/duration_minutes",
          "source_id": "r66_pc_84c88699ada11a14343702a7"
        }
      ]
    },
    "native_fact_id": "C06:rate_recovered_pc_availability_pc_01_02_general_student:duration_minutes",
    "native_record_id": "rate_recovered_pc_availability_pc_01_02_general_student",
    "facet": "duration_minutes",
    "value": "60",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r66_pc_84c88699ada11a14343702a7"
      }
    ],
    "legacy_record_id": "rate_recovered_pc_availability_pc_01_02_general_student"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C06-Q055 — ราคาปกติ

Based on the studio sources, How many minutes does migrated_rate_vr_60_1_5_psu_student_staff cover?

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, additional_or_wrong_scope_claims, state=answer

```text
นายธนชาติ เอ่งฉ้วน — name: นายธนชาติ เอ่งฉ้วน [S1]
นายชนะชัย สิริพันธ์วราภรณ์ — name: นายชนะชัย สิริพันธ์วราภรณ์ [S2]
นางสาวกมลวรรณ นวลสาย — name: นางสาวกมลวรรณ นวลสาย [S3]
นางสาวชญาภา จันทร์เอิบ — name: นางสาวชญาภา จันทร์เอิบ [S4]
นายษุภากรณ์ จิราจินดากุล — name: นายษุภากรณ์ จิราจินดากุล [S5]
นายณัฐวัฒน์ นิธิคุณานนต์ — name: นายณัฐวัฒน์ นิธิคุณานนต์ [S6]
รศ.ดร.อซีส นันทอมรพงศ์ — name: รศ.ดร.อซีส นันทอมรพงศ์ [S7]
รศ.ดร.พันธ์ ทองชุมนุม — name: รศ.ดร.พันธ์ ทองชุมนุม [S8]
นายภาสวุฒิ ชูติประชากิจ — name: นายภาสวุฒิ ชูติประชากิจ [S9]
นางสาวอาทิตยา แดงประดับ — name: นางสาวอาทิตยา แดงประดับ [S10]
ผศ.ดร.ณัฐพงศ์ ทองเทพ — name: ผศ.ดร.ณัฐพงศ์ ทองเทพ [S11]
นายพฤทธิ์ เกษตรสมบูรณ์ — name: นายพฤทธิ์ เกษตรสมบูรณ์ [S12]
นางสาวณัฐธิดา คำทะเนตร์ — name: นางสาวณัฐธิดา คำทะเนตร์ [S13]
นายณัฐพนธ์ อินทรสังขนาวิน — name: นายณัฐพนธ์ อินทรสังขนาวิน [S14]
Mr. Amine Abidellaoui — name: Mr. Amine Abidellaoui [S15]
นางสาวสุภาสินี ธนภพ — name: นางสาวสุภาสินี ธนภพ [S16]
นายอรรถนนท์ สุขแก้ว — name: นายอรรถนนท์ สุขแก้ว [S17]
นายสุพศิน อะนะฝรั่ง — name: นายสุพศิน อะนะฝรั่ง [S18]
นายอภิวิชญ์ เลิศกมลรักษ์ — name: นายอภิวิชญ์ เลิศกมลรักษ์ [S19]
นายนพัทธ์ ฝอยทอง — name: นายนพัทธ์ ฝอยทอง [S20]
นายณภัทร เชื้อเหล่าวานิช — name: นายณภัทร เชื้อเหล่าวานิช [S21]
ผศ.ดร.นิวัติ แก้วประดับ — name: ผศ.ดร.นิวัติ แก้วประดับ [S22]
Mr. Yanis Igoudjil — name: Mr. Yanis Igoudjil [S23]
นายภูจิตร จิรวิริยาภรณ์ — name: นายภูจิตร จิรวิริยาภรณ์ [S24]
นายปัณณวิชญ์ หนูเรือง — name: นายปัณณวิชญ์ หนูเรือง [S25]
```

หลัง: strict=True, source_contract_pass, state=answer

```text
VR Station 1 ชั่วโมง / PSU Student and Staff — minutes per session: 60 [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C06:migrated_rate_vr_60_1_5_psu_student_staff:duration_minutes",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:migrated_rate_vr_60_1_5_psu_student_staff:duration_minutes",
      "record_id": "migrated_rate_vr_60_1_5_psu_student_staff",
      "facet": "duration_minutes",
      "value": "60",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/duration_minutes",
          "source_id": "r63_0c6eb39e6d72e2f3e1224f7674a7"
        }
      ]
    },
    "native_fact_id": "C06:migrated_rate_vr_60_1_5_psu_student_staff:duration_minutes",
    "native_record_id": "migrated_rate_vr_60_1_5_psu_student_staff",
    "facet": "duration_minutes",
    "value": "60",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r63_0c6eb39e6d72e2f3e1224f7674a7"
      }
    ],
    "legacy_record_id": "migrated_rate_vr_60_1_5_psu_student_staff"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C06-Q057 — ราคาปกติ

Could you help me with this: How many minutes does migrated_rate_nintendo_switch_60_1_2_psu_alumni_general_student cover?

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, required_claims_missing, state=missing_input

```text
I could not match this question to the migrated information. Please specify the game, device or topic you want to know about.
```

หลัง: strict=True, source_contract_pass, state=answer

```text
Nintendo Switch (1-2 Persons) / PSU Alumni and General Student — minutes per session: 60 [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C06:migrated_rate_nintendo_switch_60_1_2_psu_alumni_general_student:duration_minutes",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:migrated_rate_nintendo_switch_60_1_2_psu_alumni_general_student:duration_minutes",
      "record_id": "migrated_rate_nintendo_switch_60_1_2_psu_alumni_general_student",
      "facet": "duration_minutes",
      "value": "60",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/duration_minutes",
          "source_id": "r63_2918da02b8bbc3137d7e8e43ef3d"
        }
      ]
    },
    "native_fact_id": "C06:migrated_rate_nintendo_switch_60_1_2_psu_alumni_general_student:duration_minutes",
    "native_record_id": "migrated_rate_nintendo_switch_60_1_2_psu_alumni_general_student",
    "facet": "duration_minutes",
    "value": "60",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r63_2918da02b8bbc3137d7e8e43ef3d"
      }
    ],
    "legacy_record_id": "migrated_rate_nintendo_switch_60_1_2_psu_alumni_general_student"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C06-Q059 — ราคาปกติ

I would like to know: How many minutes does rate_recovered_pc_availability_pc_01_02_psu_student_staff cover?

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, required_claims_missing, state=unavailable

```text
No confirmed live binding is available, so occupancy cannot be checked.
```

หลัง: strict=True, source_contract_pass, state=answer

```text
PC #01-#02 / PSU Student and Staff — minutes per session: 60 [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C06:rate_recovered_pc_availability_pc_01_02_psu_student_staff:duration_minutes",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:rate_recovered_pc_availability_pc_01_02_psu_student_staff:duration_minutes",
      "record_id": "rate_recovered_pc_availability_pc_01_02_psu_student_staff",
      "facet": "duration_minutes",
      "value": "60",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/duration_minutes",
          "source_id": "r66_pc_4cd8af9a21a7cacef4532b65"
        }
      ]
    },
    "native_fact_id": "C06:rate_recovered_pc_availability_pc_01_02_psu_student_staff:duration_minutes",
    "native_record_id": "rate_recovered_pc_availability_pc_01_02_psu_student_staff",
    "facet": "duration_minutes",
    "value": "60",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r66_pc_4cd8af9a21a7cacef4532b65"
      }
    ],
    "legacy_record_id": "rate_recovered_pc_availability_pc_01_02_psu_student_staff"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C06-Q061 — ราคาปกติ

How many minutes does migrated_rate_cockpit_60_1_1_psu_student_staff cover? and also What is the price for PC #03-#10 / PSU Student and Staff?

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, additional_or_wrong_scope_claims, state=answer

```text
นายธนชาติ เอ่งฉ้วน — name: นายธนชาติ เอ่งฉ้วน [S1]
นายชนะชัย สิริพันธ์วราภรณ์ — name: นายชนะชัย สิริพันธ์วราภรณ์ [S2]
นางสาวกมลวรรณ นวลสาย — name: นางสาวกมลวรรณ นวลสาย [S3]
นางสาวชญาภา จันทร์เอิบ — name: นางสาวชญาภา จันทร์เอิบ [S4]
นายษุภากรณ์ จิราจินดากุล — name: นายษุภากรณ์ จิราจินดากุล [S5]
นายณัฐวัฒน์ นิธิคุณานนต์ — name: นายณัฐวัฒน์ นิธิคุณานนต์ [S6]
รศ.ดร.อซีส นันทอมรพงศ์ — name: รศ.ดร.อซีส นันทอมรพงศ์ [S7]
รศ.ดร.พันธ์ ทองชุมนุม — name: รศ.ดร.พันธ์ ทองชุมนุม [S8]
นายภาสวุฒิ ชูติประชากิจ — name: นายภาสวุฒิ ชูติประชากิจ [S9]
นางสาวอาทิตยา แดงประดับ — name: นางสาวอาทิตยา แดงประดับ [S10]
ผศ.ดร.ณัฐพงศ์ ทองเทพ — name: ผศ.ดร.ณัฐพงศ์ ทองเทพ [S11]
นายพฤทธิ์ เกษตรสมบูรณ์ — name: นายพฤทธิ์ เกษตรสมบูรณ์ [S12]
นางสาวณัฐธิดา คำทะเนตร์ — name: นางสาวณัฐธิดา คำทะเนตร์ [S13]
นายณัฐพนธ์ อินทรสังขนาวิน — name: นายณัฐพนธ์ อินทรสังขนาวิน [S14]
Mr. Amine Abidellaoui — name: Mr. Amine Abidellaoui [S15]
นางสาวสุภาสินี ธนภพ — name: นางสาวสุภาสินี ธนภพ [S16]
นายอรรถนนท์ สุขแก้ว — name: นายอรรถนนท์ สุขแก้ว [S17]
นายสุพศิน อะนะฝรั่ง — name: นายสุพศิน อะนะฝรั่ง [S18]
นายอภิวิชญ์ เลิศกมลรักษ์ — name: นายอภิวิชญ์ เลิศกมลรักษ์ [S19]
นายนพัทธ์ ฝอยทอง — name: นายนพัทธ์ ฝอยทอง [S20]
นายณภัทร เชื้อเหล่าวานิช — name: นายณภัทร เชื้อเหล่าวานิช [S21]
ผศ.ดร.นิวัติ แก้วประดับ — name: ผศ.ดร.นิวัติ แก้วประดับ [S22]
Mr. Yanis Igoudjil — name: Mr. Yanis Igoudjil [S23]
นายภูจิตร จิรวิริยาภรณ์ — name: นายภูจิตร จิรวิริยาภรณ์ [S24]
นายปัณณวิชญ์ หนูเรือง — name: นายปัณณวิชญ์ หนูเรือง [S25]

Rates last reaffirmed by the owner on 2026-10-20; no new effective interval was established.
PC #03-#10 / PSU Student and Staff — per-person price for the rate duration: 0 THB per person for 60 minutes [S26]
```

หลัง: strict=True, source_contract_pass, state=answer

```text
Cockpit #01-#02 / PSU Student and Staff — minutes per session: 60 [S1]

Rates last reaffirmed by the owner on 2026-10-20; no new effective interval was established.
PC #03-#10 / PSU Student and Staff — per-person price for the rate duration: 0 THB per person for 60 minutes [S2]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C06:migrated_rate_cockpit_60_1_1_psu_student_staff:duration_minutes",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:migrated_rate_cockpit_60_1_1_psu_student_staff:duration_minutes",
      "record_id": "migrated_rate_cockpit_60_1_1_psu_student_staff",
      "facet": "duration_minutes",
      "value": "60",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/duration_minutes",
          "source_id": "r63_7c1e752ae78e8c2c9389e38b650d"
        }
      ]
    },
    "native_fact_id": "C06:migrated_rate_cockpit_60_1_1_psu_student_staff:duration_minutes",
    "native_record_id": "migrated_rate_cockpit_60_1_1_psu_student_staff",
    "facet": "duration_minutes",
    "value": "60",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r63_7c1e752ae78e8c2c9389e38b650d"
      }
    ],
    "legacy_record_id": "migrated_rate_cockpit_60_1_1_psu_student_staff"
  },
  {
    "legacy_fact_id": "C06:rate_recovered_pc_availability_pc_03_10_psu_student_staff:amount",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:rate_recovered_pc_availability_pc_03_10_psu_student_staff:amount",
      "record_id": "rate_recovered_pc_availability_pc_03_10_psu_student_staff",
      "facet": "amount",
      "value": "0 THB per person per session",
      "numeric": 0.0,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/amount_minor",
          "source_id": "r66_pc_58034b8509494c7ee96cf734"
        }
      ]
    },
    "native_fact_id": "C06:rate_recovered_pc_availability_pc_03_10_psu_student_staff:amount",
    "native_record_id": "rate_recovered_pc_availability_pc_03_10_psu_student_staff",
    "facet": "amount",
    "value": "0 THB per person for 60 minutes",
    "numeric": 0.0,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/amount_minor",
        "source_id": "r66_pc_58034b8509494c7ee96cf734"
      },
      {
        "locator": "/mapped_fields/service_id",
        "source_id": "r66_pc_58034b8509494c7ee96cf734"
      },
      {
        "locator": "/mapped_fields/audience_id",
        "source_id": "r66_pc_58034b8509494c7ee96cf734"
      },
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r66_pc_58034b8509494c7ee96cf734"
      },
      {
        "locator": "/mapped_fields/unit",
        "source_id": "r66_pc_billing_fa743cf8e92bfceb1844b88c"
      }
    ],
    "legacy_record_id": "rate_recovered_pc_availability_pc_03_10_psu_student_staff"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C06-Q064 — ราคาปกติ

I would like to know: Waht is the price for PC #03-#10 / PSU Student and Staff? and also How many minutes does migrated_rate_cockpit_60_1_1_psu_alumni_general_student cover?

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, additional_or_wrong_scope_claims, state=answer

```text
Rates last reaffirmed by the owner on 2026-10-20; no new effective interval was established.
PC #03-#10 / PSU Student and Staff — per-person price for the rate duration: 0 THB per person for 60 minutes [S1]

Cockpit #01-#02 — all offered games: Gran Turismo 7 [S2]
```

หลัง: strict=True, source_contract_pass, state=answer

```text
Rates last reaffirmed by the owner on 2026-10-20; no new effective interval was established.
PC #03-#10 / PSU Student and Staff — per-person price for the rate duration: 0 THB per person for 60 minutes [S1]

Cockpit #01-#02 / PSU Alumni and General Student — minutes per session: 60 [S2]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C06:rate_recovered_pc_availability_pc_03_10_psu_student_staff:amount",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:rate_recovered_pc_availability_pc_03_10_psu_student_staff:amount",
      "record_id": "rate_recovered_pc_availability_pc_03_10_psu_student_staff",
      "facet": "amount",
      "value": "0 THB per person per session",
      "numeric": 0.0,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/amount_minor",
          "source_id": "r66_pc_58034b8509494c7ee96cf734"
        }
      ]
    },
    "native_fact_id": "C06:rate_recovered_pc_availability_pc_03_10_psu_student_staff:amount",
    "native_record_id": "rate_recovered_pc_availability_pc_03_10_psu_student_staff",
    "facet": "amount",
    "value": "0 THB per person for 60 minutes",
    "numeric": 0.0,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/amount_minor",
        "source_id": "r66_pc_58034b8509494c7ee96cf734"
      },
      {
        "locator": "/mapped_fields/service_id",
        "source_id": "r66_pc_58034b8509494c7ee96cf734"
      },
      {
        "locator": "/mapped_fields/audience_id",
        "source_id": "r66_pc_58034b8509494c7ee96cf734"
      },
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r66_pc_58034b8509494c7ee96cf734"
      },
      {
        "locator": "/mapped_fields/unit",
        "source_id": "r66_pc_billing_fa743cf8e92bfceb1844b88c"
      }
    ],
    "legacy_record_id": "rate_recovered_pc_availability_pc_03_10_psu_student_staff"
  },
  {
    "legacy_fact_id": "C06:migrated_rate_cockpit_60_1_1_psu_alumni_general_student:duration_minutes",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:migrated_rate_cockpit_60_1_1_psu_alumni_general_student:duration_minutes",
      "record_id": "migrated_rate_cockpit_60_1_1_psu_alumni_general_student",
      "facet": "duration_minutes",
      "value": "60",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/duration_minutes",
          "source_id": "r63_773d8828419240554040c39d9a60"
        }
      ]
    },
    "native_fact_id": "C06:migrated_rate_cockpit_60_1_1_psu_alumni_general_student:duration_minutes",
    "native_record_id": "migrated_rate_cockpit_60_1_1_psu_alumni_general_student",
    "facet": "duration_minutes",
    "value": "60",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r63_773d8828419240554040c39d9a60"
      }
    ],
    "legacy_record_id": "migrated_rate_cockpit_60_1_1_psu_alumni_general_student"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C06-Q067 — ราคาปกติ

Could you help me with this: How many minutes does migrated_rate_cockpit_60_1_1_psu_alumni_general_student cover? and also Do the quoted prices include tax?

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, additional_or_wrong_scope_claims, state=answer

```text
Cockpit #01-#02 — all offered games: Gran Turismo 7 [S1]

tax included — conditions and procedure: The quoted price table includes tax. The source note about out-of-hours staff compensation remains separate. [S2]
```

หลัง: strict=True, source_contract_pass, state=answer

```text
Cockpit #01-#02 / PSU Alumni and General Student — minutes per session: 60 [S1]

tax included — conditions and procedure: The quoted price table includes tax. The source note about out-of-hours staff compensation remains separate. [S2]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C06:migrated_rate_cockpit_60_1_1_psu_alumni_general_student:duration_minutes",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:migrated_rate_cockpit_60_1_1_psu_alumni_general_student:duration_minutes",
      "record_id": "migrated_rate_cockpit_60_1_1_psu_alumni_general_student",
      "facet": "duration_minutes",
      "value": "60",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/duration_minutes",
          "source_id": "r63_773d8828419240554040c39d9a60"
        }
      ]
    },
    "native_fact_id": "C06:migrated_rate_cockpit_60_1_1_psu_alumni_general_student:duration_minutes",
    "native_record_id": "migrated_rate_cockpit_60_1_1_psu_alumni_general_student",
    "facet": "duration_minutes",
    "value": "60",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r63_773d8828419240554040c39d9a60"
      }
    ],
    "legacy_record_id": "migrated_rate_cockpit_60_1_1_psu_alumni_general_student"
  },
  {
    "legacy_fact_id": "C06:Q050:owner_policy",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:Q050:owner_policy",
      "record_id": "Q050",
      "facet": "owner_policy",
      "value": "The quoted price table includes tax. The source note about out-of-hours staff compensation remains separate.",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "owner108:Q050",
          "locator": "/answer_th",
          "source_path": "r109_owner_answers_20261020/MERGED_SERVICE_STATEMENTS.json"
        }
      ]
    },
    "native_fact_id": "C06:r114_q050_owner_policy:owner_policy",
    "native_record_id": "r114_q050_owner_policy",
    "facet": "owner_policy",
    "value": "The quoted price table includes tax. The source note about out-of-hours staff compensation remains separate.",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/fields/answer",
        "source_id": "r114_import_09764cfb69e210741bdc3ac6"
      }
    ],
    "legacy_record_id": "Q050"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C06-Q071 — ราคาปกติ

ขอราคาของ Cockpit #01-#02 / PSU Alumni and General Student แล้วขอmigrated_rate_cockpit_60_1_1_general_adult ใช้ได้ยาวนานเท่าไหร่ถ้าบอกเป็นนาที

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, additional_or_wrong_scope_claims, state=answer

```text
อัตราที่เจ้าของยืนยันล่าสุด ณ 2026-10-20 (ยังไม่ยืนยันวันเริ่ม–สิ้นสุดใหม่)
Cockpit #01-#02 / PSU Alumni and General Student — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 65 บาทต่อคน สำหรับ 60 นาที [S1]

Cockpit #01-#02 — รายชื่อเกมทั้งหมด: Gran Turismo 7 [S2]
```

หลัง: strict=True, source_contract_pass, state=answer

```text
อัตราที่เจ้าของยืนยันล่าสุด ณ 2026-10-20 (ยังไม่ยืนยันวันเริ่ม–สิ้นสุดใหม่)
Cockpit #01-#02 / PSU Alumni and General Student — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 65 บาทต่อคน สำหรับ 60 นาที [S1]

Cockpit #01-#02 / General Adult — นาทีต่อรอบ: 60 [S2]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C06:migrated_rate_cockpit_60_1_1_psu_alumni_general_student:amount",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:migrated_rate_cockpit_60_1_1_psu_alumni_general_student:amount",
      "record_id": "migrated_rate_cockpit_60_1_1_psu_alumni_general_student",
      "facet": "amount",
      "value": "65 บาทต่อคนต่อรอบ",
      "numeric": 65.0,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/amount_minor",
          "source_id": "r63_773d8828419240554040c39d9a60"
        }
      ]
    },
    "native_fact_id": "C06:migrated_rate_cockpit_60_1_1_psu_alumni_general_student:amount",
    "native_record_id": "migrated_rate_cockpit_60_1_1_psu_alumni_general_student",
    "facet": "amount",
    "value": "65 บาทต่อคน สำหรับ 60 นาที",
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
      }
    ],
    "legacy_record_id": "migrated_rate_cockpit_60_1_1_psu_alumni_general_student"
  },
  {
    "legacy_fact_id": "C06:migrated_rate_cockpit_60_1_1_general_adult:duration_minutes",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:migrated_rate_cockpit_60_1_1_general_adult:duration_minutes",
      "record_id": "migrated_rate_cockpit_60_1_1_general_adult",
      "facet": "duration_minutes",
      "value": "60",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/duration_minutes",
          "source_id": "r63_9671361adf41b3433392c3c8b569"
        }
      ]
    },
    "native_fact_id": "C06:migrated_rate_cockpit_60_1_1_general_adult:duration_minutes",
    "native_record_id": "migrated_rate_cockpit_60_1_1_general_adult",
    "facet": "duration_minutes",
    "value": "60",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r63_9671361adf41b3433392c3c8b569"
      }
    ],
    "legacy_record_id": "migrated_rate_cockpit_60_1_1_general_adult"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C06-Q072 — ราคาปกติ

ขอสอบถามหน่อยครับ VR Station 1 ชั่วโมง / PSU Alumni and General Student มีค่าบริการเท่าไหร่ แล้วขอmigrated_rate_nintendo_switch_60_1_2_general_adult ให้ใช้นานกี่นาที

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, required_claims_missing, state=partial

```text
อัตราที่เจ้าของยืนยันล่าสุด ณ 2026-10-20 (ยังไม่ยืนยันวันเริ่ม–สิ้นสุดใหม่)
VR Station 1 ชั่วโมง / PSU Alumni and General Student — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 375 บาทต่อคน สำหรับ 60 นาที [S1]

ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

หลัง: strict=True, source_contract_pass, state=answer

```text
อัตราที่เจ้าของยืนยันล่าสุด ณ 2026-10-20 (ยังไม่ยืนยันวันเริ่ม–สิ้นสุดใหม่)
VR Station 1 ชั่วโมง / PSU Alumni and General Student — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 375 บาทต่อคน สำหรับ 60 นาที [S1]

Nintendo Switch (1-2 Persons) / General Adult — นาทีต่อรอบ: 60 [S2]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C06:migrated_rate_vr_60_1_5_psu_alumni_general_student:amount",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:migrated_rate_vr_60_1_5_psu_alumni_general_student:amount",
      "record_id": "migrated_rate_vr_60_1_5_psu_alumni_general_student",
      "facet": "amount",
      "value": "375 บาทต่อคนต่อรอบ",
      "numeric": 375.0,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/amount_minor",
          "source_id": "r63_b4d09ed83a76bc1f15a4563652ed"
        }
      ]
    },
    "native_fact_id": "C06:migrated_rate_vr_60_1_5_psu_alumni_general_student:amount",
    "native_record_id": "migrated_rate_vr_60_1_5_psu_alumni_general_student",
    "facet": "amount",
    "value": "375 บาทต่อคน สำหรับ 60 นาที",
    "numeric": 375.0,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/amount_minor",
        "source_id": "r63_b4d09ed83a76bc1f15a4563652ed"
      },
      {
        "locator": "/mapped_fields/service_id",
        "source_id": "r63_b4d09ed83a76bc1f15a4563652ed"
      },
      {
        "locator": "/mapped_fields/audience_id",
        "source_id": "r63_b4d09ed83a76bc1f15a4563652ed"
      },
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r63_b4d09ed83a76bc1f15a4563652ed"
      }
    ],
    "legacy_record_id": "migrated_rate_vr_60_1_5_psu_alumni_general_student"
  },
  {
    "legacy_fact_id": "C06:migrated_rate_nintendo_switch_60_1_2_general_adult:duration_minutes",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:migrated_rate_nintendo_switch_60_1_2_general_adult:duration_minutes",
      "record_id": "migrated_rate_nintendo_switch_60_1_2_general_adult",
      "facet": "duration_minutes",
      "value": "60",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/duration_minutes",
          "source_id": "r63_0a1368c5d62847fc27f8d2619cdb"
        }
      ]
    },
    "native_fact_id": "C06:migrated_rate_nintendo_switch_60_1_2_general_adult:duration_minutes",
    "native_record_id": "migrated_rate_nintendo_switch_60_1_2_general_adult",
    "facet": "duration_minutes",
    "value": "60",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r63_0a1368c5d62847fc27f8d2619cdb"
      }
    ],
    "legacy_record_id": "migrated_rate_nintendo_switch_60_1_2_general_adult"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C06-Q074 — ราคาปกติ

อยากรู้ว่า เวลาใช้งานของ migrated_rate_cockpit_60_1_1_general_adult นับเป็นกี่นาที แล้วขอNintendo Switch (1-2 Persons) / PSU Alumni and General Student มีค่าบริการเท่าไหร่

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, additional_or_wrong_scope_claims, state=answer

```text
Cockpit #01-#02 — รายชื่อเกมทั้งหมด: Gran Turismo 7 [S1]

อัตราที่เจ้าของยืนยันล่าสุด ณ 2026-10-20 (ยังไม่ยืนยันวันเริ่ม–สิ้นสุดใหม่)
Nintendo Switch (1-2 Persons) / PSU Alumni and General Student — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 50 บาทต่อคน สำหรับ 60 นาที [S2]
```

หลัง: strict=True, source_contract_pass, state=answer

```text
Cockpit #01-#02 / General Adult — นาทีต่อรอบ: 60 [S1]

อัตราที่เจ้าของยืนยันล่าสุด ณ 2026-10-20 (ยังไม่ยืนยันวันเริ่ม–สิ้นสุดใหม่)
Nintendo Switch (1-2 Persons) / PSU Alumni and General Student — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 50 บาทต่อคน สำหรับ 60 นาที [S2]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C06:migrated_rate_cockpit_60_1_1_general_adult:duration_minutes",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:migrated_rate_cockpit_60_1_1_general_adult:duration_minutes",
      "record_id": "migrated_rate_cockpit_60_1_1_general_adult",
      "facet": "duration_minutes",
      "value": "60",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/duration_minutes",
          "source_id": "r63_9671361adf41b3433392c3c8b569"
        }
      ]
    },
    "native_fact_id": "C06:migrated_rate_cockpit_60_1_1_general_adult:duration_minutes",
    "native_record_id": "migrated_rate_cockpit_60_1_1_general_adult",
    "facet": "duration_minutes",
    "value": "60",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r63_9671361adf41b3433392c3c8b569"
      }
    ],
    "legacy_record_id": "migrated_rate_cockpit_60_1_1_general_adult"
  },
  {
    "legacy_fact_id": "C06:migrated_rate_nintendo_switch_60_1_2_psu_alumni_general_student:amount",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:migrated_rate_nintendo_switch_60_1_2_psu_alumni_general_student:amount",
      "record_id": "migrated_rate_nintendo_switch_60_1_2_psu_alumni_general_student",
      "facet": "amount",
      "value": "50 บาทต่อคนต่อรอบ",
      "numeric": 50.0,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/amount_minor",
          "source_id": "r63_2918da02b8bbc3137d7e8e43ef3d"
        }
      ]
    },
    "native_fact_id": "C06:migrated_rate_nintendo_switch_60_1_2_psu_alumni_general_student:amount",
    "native_record_id": "migrated_rate_nintendo_switch_60_1_2_psu_alumni_general_student",
    "facet": "amount",
    "value": "50 บาทต่อคน สำหรับ 60 นาที",
    "numeric": 50.0,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/amount_minor",
        "source_id": "r63_2918da02b8bbc3137d7e8e43ef3d"
      },
      {
        "locator": "/mapped_fields/service_id",
        "source_id": "r63_2918da02b8bbc3137d7e8e43ef3d"
      },
      {
        "locator": "/mapped_fields/audience_id",
        "source_id": "r63_2918da02b8bbc3137d7e8e43ef3d"
      },
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r63_2918da02b8bbc3137d7e8e43ef3d"
      }
    ],
    "legacy_record_id": "migrated_rate_nintendo_switch_60_1_2_psu_alumni_general_student"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C06-Q075 — ราคาปกติ

กำลังวางแผนไปใช้บริการ เลยขอถามว่า migrated_rate_nintendo_switch_60_1_2_general_adult ใช้ได้ยาวนานเท่าไหร่ถ้าบอกเป็นนาที แล้วขอmigrated_rate_vr_30_1_5_psu_student_staff ให้ใช้นานกี่นาที

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, additional_or_wrong_scope_claims, state=partial

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ

นายธนชาติ เอ่งฉ้วน — ชื่อ: นายธนชาติ เอ่งฉ้วน [S1]
นายชนะชัย สิริพันธ์วราภรณ์ — ชื่อ: นายชนะชัย สิริพันธ์วราภรณ์ [S2]
นางสาวกมลวรรณ นวลสาย — ชื่อ: นางสาวกมลวรรณ นวลสาย [S3]
นางสาวชญาภา จันทร์เอิบ — ชื่อ: นางสาวชญาภา จันทร์เอิบ [S4]
นายษุภากรณ์ จิราจินดากุล — ชื่อ: นายษุภากรณ์ จิราจินดากุล [S5]
นายณัฐวัฒน์ นิธิคุณานนต์ — ชื่อ: นายณัฐวัฒน์ นิธิคุณานนต์ [S6]
รศ.ดร.อซีส นันทอมรพงศ์ — ชื่อ: รศ.ดร.อซีส นันทอมรพงศ์ [S7]
รศ.ดร.พันธ์ ทองชุมนุม — ชื่อ: รศ.ดร.พันธ์ ทองชุมนุม [S8]
นายภาสวุฒิ ชูติประชากิจ — ชื่อ: นายภาสวุฒิ ชูติประชากิจ [S9]
นางสาวอาทิตยา แดงประดับ — ชื่อ: นางสาวอาทิตยา แดงประดับ [S10]
ผศ.ดร.ณัฐพงศ์ ทองเทพ — ชื่อ: ผศ.ดร.ณัฐพงศ์ ทองเทพ [S11]
นายพฤทธิ์ เกษตรสมบูรณ์ — ชื่อ: นายพฤทธิ์ เกษตรสมบูรณ์ [S12]
นางสาวณัฐธิดา คำทะเนตร์ — ชื่อ: นางสาวณัฐธิดา คำทะเนตร์ [S13]
นายณัฐพนธ์ อินทรสังขนาวิน — ชื่อ: นายณัฐพนธ์ อินทรสังขนาวิน [S14]
Mr. Amine Abidellaoui — ชื่อ: Mr. Amine Abidellaoui [S15]
นางสาวสุภาสินี ธนภพ — ชื่อ: นางสาวสุภาสินี ธนภพ [S16]
นายอรรถนนท์ สุขแก้ว — ชื่อ: นายอรรถนนท์ สุขแก้ว [S17]
นายสุพศิน อะนะฝรั่ง — ชื่อ: นายสุพศิน อะนะฝรั่ง [S18]
นายอภิวิชญ์ เลิศกมลรักษ์ — ชื่อ: นายอภิวิชญ์ เลิศกมลรักษ์ [S19]
นายนพัทธ์ ฝอยทอง — ชื่อ: นายนพัทธ์ ฝอยทอง [S20]
นายณภัทร เชื้อเหล่าวานิช — ชื่อ: นายณภัทร เชื้อเหล่าวานิช [S21]
ผศ.ดร.นิวัติ แก้วประดับ — ชื่อ: ผศ.ดร.นิวัติ แก้วประดับ [S22]
Mr. Yanis Igoudjil — ชื่อ: Mr. Yanis Igoudjil [S23]
นายภูจิตร จิรวิริยาภรณ์ — ชื่อ: นายภูจิตร จิรวิริยาภรณ์ [S24]
นายปัณณวิชญ์ หนูเรือง — ชื่อ: นายปัณณวิชญ์ หนูเรือง [S25]
```

หลัง: strict=True, source_contract_pass, state=answer

```text
Nintendo Switch (1-2 Persons) / General Adult — นาทีต่อรอบ: 60 [S1]

VR Station 30 นาที / PSU Student and Staff — นาทีต่อรอบ: 30 [S2]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C06:migrated_rate_nintendo_switch_60_1_2_general_adult:duration_minutes",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:migrated_rate_nintendo_switch_60_1_2_general_adult:duration_minutes",
      "record_id": "migrated_rate_nintendo_switch_60_1_2_general_adult",
      "facet": "duration_minutes",
      "value": "60",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/duration_minutes",
          "source_id": "r63_0a1368c5d62847fc27f8d2619cdb"
        }
      ]
    },
    "native_fact_id": "C06:migrated_rate_nintendo_switch_60_1_2_general_adult:duration_minutes",
    "native_record_id": "migrated_rate_nintendo_switch_60_1_2_general_adult",
    "facet": "duration_minutes",
    "value": "60",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r63_0a1368c5d62847fc27f8d2619cdb"
      }
    ],
    "legacy_record_id": "migrated_rate_nintendo_switch_60_1_2_general_adult"
  },
  {
    "legacy_fact_id": "C06:migrated_rate_vr_30_1_5_psu_student_staff:duration_minutes",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:migrated_rate_vr_30_1_5_psu_student_staff:duration_minutes",
      "record_id": "migrated_rate_vr_30_1_5_psu_student_staff",
      "facet": "duration_minutes",
      "value": "30",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/duration_minutes",
          "source_id": "r63_f75ddf25f2e0dd94c12889e2ac05"
        }
      ]
    },
    "native_fact_id": "C06:migrated_rate_vr_30_1_5_psu_student_staff:duration_minutes",
    "native_record_id": "migrated_rate_vr_30_1_5_psu_student_staff",
    "facet": "duration_minutes",
    "value": "30",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r63_f75ddf25f2e0dd94c12889e2ac05"
      }
    ],
    "legacy_record_id": "migrated_rate_vr_30_1_5_psu_student_staff"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C06-Q076 — ราคาปกติ

รบกวนเช็กให้หน่อย เล่น PC #03-#10 / PSU Alumni and General Student คิดกี่บาทต่อคนต่อรอบ แล้วขอเวลาใช้งานของ migrated_rate_vr_30_1_5_psu_alumni_general_student นับเป็นกี่นาที

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, additional_or_wrong_scope_claims, state=answer

```text
อัตราที่เจ้าของยืนยันล่าสุด ณ 2026-10-20 (ยังไม่ยืนยันวันเริ่ม–สิ้นสุดใหม่)
PC #03-#10 / PSU Alumni and General Student — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 25 บาทต่อคน สำหรับ 60 นาที [S1]

VR Station 30 นาที — รายชื่อเกมทั้งหมด: Beat Saber; Horizon Call of the Mountain; Resident Evil 4; Resident Evil Village [S2]
```

หลัง: strict=True, source_contract_pass, state=answer

```text
อัตราที่เจ้าของยืนยันล่าสุด ณ 2026-10-20 (ยังไม่ยืนยันวันเริ่ม–สิ้นสุดใหม่)
PC #03-#10 / PSU Alumni and General Student — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 25 บาทต่อคน สำหรับ 60 นาที [S1]

VR Station 30 นาที / PSU Alumni and General Student — นาทีต่อรอบ: 30 [S2]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C06:rate_recovered_pc_availability_pc_03_10_general_student:amount",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:rate_recovered_pc_availability_pc_03_10_general_student:amount",
      "record_id": "rate_recovered_pc_availability_pc_03_10_general_student",
      "facet": "amount",
      "value": "25 บาทต่อคนต่อรอบ",
      "numeric": 25.0,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/amount_minor",
          "source_id": "r66_pc_b9251e4f325511ac1fc7611d"
        }
      ]
    },
    "native_fact_id": "C06:rate_recovered_pc_availability_pc_03_10_general_student:amount",
    "native_record_id": "rate_recovered_pc_availability_pc_03_10_general_student",
    "facet": "amount",
    "value": "25 บาทต่อคน สำหรับ 60 นาที",
    "numeric": 25.0,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/amount_minor",
        "source_id": "r66_pc_b9251e4f325511ac1fc7611d"
      },
      {
        "locator": "/mapped_fields/service_id",
        "source_id": "r66_pc_b9251e4f325511ac1fc7611d"
      },
      {
        "locator": "/mapped_fields/audience_id",
        "source_id": "r66_pc_b9251e4f325511ac1fc7611d"
      },
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r66_pc_b9251e4f325511ac1fc7611d"
      },
      {
        "locator": "/mapped_fields/unit",
        "source_id": "r66_pc_billing_ae1cb00d0d602cd162fb6b37"
      }
    ],
    "legacy_record_id": "rate_recovered_pc_availability_pc_03_10_general_student"
  },
  {
    "legacy_fact_id": "C06:migrated_rate_vr_30_1_5_psu_alumni_general_student:duration_minutes",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:migrated_rate_vr_30_1_5_psu_alumni_general_student:duration_minutes",
      "record_id": "migrated_rate_vr_30_1_5_psu_alumni_general_student",
      "facet": "duration_minutes",
      "value": "30",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/duration_minutes",
          "source_id": "r63_d4d5a0745b2e65f3acc6829507db"
        }
      ]
    },
    "native_fact_id": "C06:migrated_rate_vr_30_1_5_psu_alumni_general_student:duration_minutes",
    "native_record_id": "migrated_rate_vr_30_1_5_psu_alumni_general_student",
    "facet": "duration_minutes",
    "value": "30",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r63_d4d5a0745b2e65f3acc6829507db"
      }
    ],
    "legacy_record_id": "migrated_rate_vr_30_1_5_psu_alumni_general_student"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C06-Q078 — ราคาปกติ

migrated_rate_vr_30_1_5_psu_student_staff ใช้ได้ยาวนานเท่าไหร่ถ้าบอกเป็นนาที แล้วขอrate_recovered_pc_availability_pc_03_10_general_adult ให้ใช้นานกี่นาที

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, additional_or_wrong_scope_claims, state=partial

```text
1. migrated_rate_vr_30_1_5_psu_student_staff ใช้ได้ยาวนานเท่าไหร่ถ้าบอกเป็นนาที
นายธนชาติ เอ่งฉ้วน — ชื่อ: นายธนชาติ เอ่งฉ้วน [S1]
นายชนะชัย สิริพันธ์วราภรณ์ — ชื่อ: นายชนะชัย สิริพันธ์วราภรณ์ [S2]
นางสาวกมลวรรณ นวลสาย — ชื่อ: นางสาวกมลวรรณ นวลสาย [S3]
นางสาวชญาภา จันทร์เอิบ — ชื่อ: นางสาวชญาภา จันทร์เอิบ [S4]
นายษุภากรณ์ จิราจินดากุล — ชื่อ: นายษุภากรณ์ จิราจินดากุล [S5]
นายณัฐวัฒน์ นิธิคุณานนต์ — ชื่อ: นายณัฐวัฒน์ นิธิคุณานนต์ [S6]
รศ.ดร.อซีส นันทอมรพงศ์ — ชื่อ: รศ.ดร.อซีส นันทอมรพงศ์ [S7]
รศ.ดร.พันธ์ ทองชุมนุม — ชื่อ: รศ.ดร.พันธ์ ทองชุมนุม [S8]
นายภาสวุฒิ ชูติประชากิจ — ชื่อ: นายภาสวุฒิ ชูติประชากิจ [S9]
นางสาวอาทิตยา แดงประดับ — ชื่อ: นางสาวอาทิตยา แดงประดับ [S10]
ผศ.ดร.ณัฐพงศ์ ทองเทพ — ชื่อ: ผศ.ดร.ณัฐพงศ์ ทองเทพ [S11]
นายพฤทธิ์ เกษตรสมบูรณ์ — ชื่อ: นายพฤทธิ์ เกษตรสมบูรณ์ [S12]
นางสาวณัฐธิดา คำทะเนตร์ — ชื่อ: นางสาวณัฐธิดา คำทะเนตร์ [S13]
นายณัฐพนธ์ อินทรสังขนาวิน — ชื่อ: นายณัฐพนธ์ อินทรสังขนาวิน [S14]
Mr. Amine Abidellaoui — ชื่อ: Mr. Amine Abidellaoui [S15]
นางสาวสุภาสินี ธนภพ — ชื่อ: นางสาวสุภาสินี ธนภพ [S16]
นายอรรถนนท์ สุขแก้ว — ชื่อ: นายอรรถนนท์ สุขแก้ว [S17]
นายสุพศิน อะนะฝรั่ง — ชื่อ: นายสุพศิน อะนะฝรั่ง [S18]
นายอภิวิชญ์ เลิศกมลรักษ์ — ชื่อ: นายอภิวิชญ์ เลิศกมลรักษ์ [S19]
นายนพัทธ์ ฝอยทอง — ชื่อ: นายนพัทธ์ ฝอยทอง [S20]
นายณภัทร เชื้อเหล่าวานิช — ชื่อ: นายณภัทร เชื้อเหล่าวานิช [S21]
ผศ.ดร.นิวัติ แก้วประดับ — ชื่อ: ผศ.ดร.นิวัติ แก้วประดับ [S22]
Mr. Yanis Igoudjil — ชื่อ: Mr. Yanis Igoudjil [S23]
นายภูจิตร จิรวิริยาภรณ์ — ชื่อ: นายภูจิตร จิรวิริยาภรณ์ [S24]
นายปัณณวิชญ์ หนูเรือง — ชื่อ: นายปัณณวิชญ์ หนูเรือง [S25]

2. rate_recovered_pc_availability_pc_03_10_general_adult ให้ใช้นานกี่นาที
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=True, source_contract_pass, state=answer

```text
VR Station 30 นาที / PSU Student and Staff — นาทีต่อรอบ: 30 [S1]

PC #03-#10 / General Adult — นาทีต่อรอบ: 60 [S2]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C06:migrated_rate_vr_30_1_5_psu_student_staff:duration_minutes",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:migrated_rate_vr_30_1_5_psu_student_staff:duration_minutes",
      "record_id": "migrated_rate_vr_30_1_5_psu_student_staff",
      "facet": "duration_minutes",
      "value": "30",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/duration_minutes",
          "source_id": "r63_f75ddf25f2e0dd94c12889e2ac05"
        }
      ]
    },
    "native_fact_id": "C06:migrated_rate_vr_30_1_5_psu_student_staff:duration_minutes",
    "native_record_id": "migrated_rate_vr_30_1_5_psu_student_staff",
    "facet": "duration_minutes",
    "value": "30",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r63_f75ddf25f2e0dd94c12889e2ac05"
      }
    ],
    "legacy_record_id": "migrated_rate_vr_30_1_5_psu_student_staff"
  },
  {
    "legacy_fact_id": "C06:rate_recovered_pc_availability_pc_03_10_general_adult:duration_minutes",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:rate_recovered_pc_availability_pc_03_10_general_adult:duration_minutes",
      "record_id": "rate_recovered_pc_availability_pc_03_10_general_adult",
      "facet": "duration_minutes",
      "value": "60",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/duration_minutes",
          "source_id": "r66_pc_dc5b4c42405e267135bbf1f8"
        }
      ]
    },
    "native_fact_id": "C06:rate_recovered_pc_availability_pc_03_10_general_adult:duration_minutes",
    "native_record_id": "rate_recovered_pc_availability_pc_03_10_general_adult",
    "facet": "duration_minutes",
    "value": "60",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r66_pc_dc5b4c42405e267135bbf1f8"
      }
    ],
    "legacy_record_id": "rate_recovered_pc_availability_pc_03_10_general_adult"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C06-Q079 — ราคาปกติ

ขอสอบถามหน่อยครับ migrated_rate_vr_30_1_5_psu_alumni_general_student ให้ใช้นานกี่นาที แล้วขอเวลาใช้งานของ rate_recovered_pc_availability_pc_03_10_general_student นับเป็นกี่นาที

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, additional_or_wrong_scope_claims, state=partial

```text
1. migrated_rate_vr_30_1_5_psu_alumni_general_student ให้ใช้นานกี่นาที
VR Station 30 นาที — รายชื่อเกมทั้งหมด: Beat Saber; Horizon Call of the Mountain; Resident Evil 4; Resident Evil Village [S4]

2. เวลาใช้งานของ rate_recovered_pc_availability_pc_03_10_general_student นับเป็นกี่นาที
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=True, source_contract_pass, state=answer

```text
VR Station 30 นาที / PSU Alumni and General Student — นาทีต่อรอบ: 30 [S1]

PC #03-#10 / PSU Alumni and General Student — นาทีต่อรอบ: 60 [S2]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C06:migrated_rate_vr_30_1_5_psu_alumni_general_student:duration_minutes",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:migrated_rate_vr_30_1_5_psu_alumni_general_student:duration_minutes",
      "record_id": "migrated_rate_vr_30_1_5_psu_alumni_general_student",
      "facet": "duration_minutes",
      "value": "30",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/duration_minutes",
          "source_id": "r63_d4d5a0745b2e65f3acc6829507db"
        }
      ]
    },
    "native_fact_id": "C06:migrated_rate_vr_30_1_5_psu_alumni_general_student:duration_minutes",
    "native_record_id": "migrated_rate_vr_30_1_5_psu_alumni_general_student",
    "facet": "duration_minutes",
    "value": "30",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r63_d4d5a0745b2e65f3acc6829507db"
      }
    ],
    "legacy_record_id": "migrated_rate_vr_30_1_5_psu_alumni_general_student"
  },
  {
    "legacy_fact_id": "C06:rate_recovered_pc_availability_pc_03_10_general_student:duration_minutes",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:rate_recovered_pc_availability_pc_03_10_general_student:duration_minutes",
      "record_id": "rate_recovered_pc_availability_pc_03_10_general_student",
      "facet": "duration_minutes",
      "value": "60",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/duration_minutes",
          "source_id": "r66_pc_b9251e4f325511ac1fc7611d"
        }
      ]
    },
    "native_fact_id": "C06:rate_recovered_pc_availability_pc_03_10_general_student:duration_minutes",
    "native_record_id": "rate_recovered_pc_availability_pc_03_10_general_student",
    "facet": "duration_minutes",
    "value": "60",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r66_pc_b9251e4f325511ac1fc7611d"
      }
    ],
    "legacy_record_id": "rate_recovered_pc_availability_pc_03_10_general_student"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C06-Q080 — ราคาปกติ

ช่วยตอบสั้น ๆ ว่า ขอราคาของ PlayStation 5 #01-#02 / PSU Student and Staff แล้วขอmigrated_rate_vr_60_1_5_psu_alumni_general_student ใช้ได้ยาวนานเท่าไหร่ถ้าบอกเป็นนาที

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, additional_or_wrong_scope_claims, state=answer

```text
อัตราที่เจ้าของยืนยันล่าสุด ณ 2026-10-20 (ยังไม่ยืนยันวันเริ่ม–สิ้นสุดใหม่)
PlayStation 5 #01-#02 / PSU Student and Staff — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 0 บาทต่อคน สำหรับ 60 นาที [S1]

VR Station 1 ชั่วโมง — รายชื่อเกมทั้งหมด: Beat Saber; Horizon Call of the Mountain; Resident Evil 4; Resident Evil Village [S2]
```

หลัง: strict=True, source_contract_pass, state=answer

```text
อัตราที่เจ้าของยืนยันล่าสุด ณ 2026-10-20 (ยังไม่ยืนยันวันเริ่ม–สิ้นสุดใหม่)
PlayStation 5 #01-#02 / PSU Student and Staff — ค่าบริการต่อคนตามระยะเวลาของอัตรา: 0 บาทต่อคน สำหรับ 60 นาที [S1]

VR Station 1 ชั่วโมง / PSU Alumni and General Student — นาทีต่อรอบ: 60 [S2]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C06:migrated_rate_playstation_5_60_1_2_psu_student_staff:amount",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:migrated_rate_playstation_5_60_1_2_psu_student_staff:amount",
      "record_id": "migrated_rate_playstation_5_60_1_2_psu_student_staff",
      "facet": "amount",
      "value": "0 บาทต่อคนต่อรอบ",
      "numeric": 0.0,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/amount_minor",
          "source_id": "r63_db0d7d309783280c60aff0c31a72"
        }
      ]
    },
    "native_fact_id": "C06:migrated_rate_playstation_5_60_1_2_psu_student_staff:amount",
    "native_record_id": "migrated_rate_playstation_5_60_1_2_psu_student_staff",
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
      }
    ],
    "legacy_record_id": "migrated_rate_playstation_5_60_1_2_psu_student_staff"
  },
  {
    "legacy_fact_id": "C06:migrated_rate_vr_60_1_5_psu_alumni_general_student:duration_minutes",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C06:migrated_rate_vr_60_1_5_psu_alumni_general_student:duration_minutes",
      "record_id": "migrated_rate_vr_60_1_5_psu_alumni_general_student",
      "facet": "duration_minutes",
      "value": "60",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/duration_minutes",
          "source_id": "r63_b4d09ed83a76bc1f15a4563652ed"
        }
      ]
    },
    "native_fact_id": "C06:migrated_rate_vr_60_1_5_psu_alumni_general_student:duration_minutes",
    "native_record_id": "migrated_rate_vr_60_1_5_psu_alumni_general_student",
    "facet": "duration_minutes",
    "value": "60",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/duration_minutes",
        "source_id": "r63_b4d09ed83a76bc1f15a4563652ed"
      }
    ],
    "legacy_record_id": "migrated_rate_vr_60_1_5_psu_alumni_general_student"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C08-Q081 — การจองและขั้นตอน

รบกวนเช็กให้หน่อย ถ้าจองเป็นชื่อบริษัทจะได้สิทธิ์พิเศษอะไรที่ประกาศไว้

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, additional_or_wrong_scope_claims, state=answer

```text
**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: ขั้นตอนจองคือ เลือกบริการ เลือกวันและเวลา กรอกข้อมูลผู้ใช้ ตรวจสอบข้อมูล ชำระเงินโดยโอนเข้าบัญชี และแนบสลิปการโอนเงิน [S1]
```

หลัง: strict=True, source_contract_pass, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C08-Q084 — การจองและขั้นตอน

ถามจากข้อมูลที่ศูนย์ให้ไว้ ถ้าจองเป็นชื่อบริษัทจะได้สิทธิ์พิเศษอะไรที่ประกาศไว้

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, additional_or_wrong_scope_claims, state=answer

```text
**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: ขั้นตอนจองคือ เลือกบริการ เลือกวันและเวลา กรอกข้อมูลผู้ใช้ ตรวจสอบข้อมูล ชำระเงินโดยโอนเข้าบัญชี และแนบสลิปการโอนเงิน [S1]
```

หลัง: strict=True, source_contract_pass, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C08-Q087 — การจองและขั้นตอน

ถ้าจองเป็นชื่อบริษัทจะได้สิทธิ์พิเศษอะไรที่ประกาศไว้

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, additional_or_wrong_scope_claims, state=answer

```text
**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: ขั้นตอนจองคือ เลือกบริการ เลือกวันและเวลา กรอกข้อมูลผู้ใช้ ตรวจสอบข้อมูล ชำระเงินโดยโอนเข้าบัญชี และแนบสลิปการโอนเงิน [S1]
```

หลัง: strict=True, source_contract_pass, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C08-Q090 — การจองและขั้นตอน

ขอสอบถามหน่อยครับ ถ้าจองเป็นชื่อบริษัทจะได้สิทธิ์พิเศษอะไรที่ประกาศไว้

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, additional_or_wrong_scope_claims, state=answer

```text
**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: ขั้นตอนจองคือ เลือกบริการ เลือกวันและเวลา กรอกข้อมูลผู้ใช้ ตรวจสอบข้อมูล ชำระเงินโดยโอนเข้าบัญชี และแนบสลิปการโอนเงิน [S1]
```

หลัง: strict=True, source_contract_pass, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C08-Q093 — การจองและขั้นตอน

ช่วยตอบสั้น ๆ ว่า ถ้าจองเป็นชื่อบริษัทจะได้สิทธิ์พิเศษอะไรที่ประกาศไว้

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, additional_or_wrong_scope_claims, state=answer

```text
**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: ขั้นตอนการจองคือ เลือกบริการที่ต้องการ เลือกวันและเวลา กรอกข้อมูลผู้ใช้บริการ ตรวจสอบข้อมูล ชำระเงินโดยโอนเข้าบัญชีธนาคาร และแนบสลิปการโอนเงิน [S1]
```

หลัง: strict=True, source_contract_pass, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C08-Q096 — การจองและขั้นตอน

อยากรู้ว่า ถ้าจองเป็นชื่อบริษัทจะได้สิทธิ์พิเศษอะไรที่ประกาศไว้

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, additional_or_wrong_scope_claims, state=answer

```text
**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: ขั้นตอนจองคือ เลือกบริการ เลือกวันและเวลา กรอกข้อมูลผู้ใช้ ตรวจสอบข้อมูล ชำระเงินโดยโอนเข้าบัญชี และแนบสลิปการโอนเงิน [S1]
```

หลัง: strict=True, source_contract_pass, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C08-Q099 — การจองและขั้นตอน

กำลังวางแผนไปใช้บริการ เลยขอถามว่า ถ้าจองเป็นชื่อบริษัทจะได้สิทธิ์พิเศษอะไรที่ประกาศไว้

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, additional_or_wrong_scope_claims, state=answer

```text
**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: ขั้นตอนการจองคือ เลือกบริการที่ต้องการ เลือกวันและเวลา กรอกข้อมูลผู้ใช้บริการ ตรวจสอบข้อมูล ชำระเงินโดยโอนเข้าบัญชีธนาคาร และแนบสลิปการโอนเงิน [S1]
```

หลัง: strict=True, source_contract_pass, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C09-Q082 — ชำระเงิน/เอกสาร

ถามจากข้อมูลที่ศูนย์ให้ไว้ จ่ายด้วยคริปโตได้กี่สกุล

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, expected_state_mismatch, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=True, source_contract_pass, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C09-Q085 — ชำระเงิน/เอกสาร

จ่ายด้วยคริปโตได้กี่สกุล

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, expected_state_mismatch, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=True, source_contract_pass, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C09-Q088 — ชำระเงิน/เอกสาร

ขอสอบถามหน่อยครับ จ่ายด้วยคริปโตได้กี่สกุล

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, expected_state_mismatch, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=True, source_contract_pass, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C09-Q091 — ชำระเงิน/เอกสาร

ช่วยตอบสั้น ๆ ว่า จ่ายด้วยคริปโตได้กี่สกุล

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, expected_state_mismatch, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=True, source_contract_pass, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C09-Q094 — ชำระเงิน/เอกสาร

อยากรู้ว่า จ่ายด้วยคริปโตได้กี่สกุล

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, expected_state_mismatch, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=True, source_contract_pass, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C09-Q097 — ชำระเงิน/เอกสาร

กำลังวางแผนไปใช้บริการ เลยขอถามว่า จ่ายด้วยคริปโตได้กี่สกุล

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, expected_state_mismatch, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=True, source_contract_pass, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C09-Q100 — ชำระเงิน/เอกสาร

รบกวนเช็กให้หน่อย จ่ายด้วยคริปโตได้กี่สกุล

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, expected_state_mismatch, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=True, source_contract_pass, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C10-Q083 — กฎการใช้บริการ

ถามจากข้อมูลที่ศูนย์ให้ไว้ ถ่ายใบหน้าลูกค้าคนอื่นแล้วเผยแพร่ได้โดยไม่ขอไหม

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, additional_or_wrong_scope_claims, state=answer

```text
**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: ไม่ต้องเป็นนักศึกษา PSU ครับ ขั้นตอนจองที่เผยแพร่ไม่ได้ระบุว่าต้องสมัครสมาชิกแยกก่อนจอง คนภายนอกใช้ช่อง National ID และแสดงบัตรประชาชนตอนเช็กอิน ค่าบริการขึ้นกับกลุ่มผู้ใช้และบริการ [S1]
• หัวข้อเชิงความหมาย: service_policy [S2]
```

หลัง: strict=True, source_contract_pass, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C10-Q086 — กฎการใช้บริการ

ถ่ายใบหน้าลูกค้าคนอื่นแล้วเผยแพร่ได้โดยไม่ขอไหม

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, additional_or_wrong_scope_claims, state=answer

```text
**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: ไม่ต้องเป็นนักศึกษา PSU ครับ ขั้นตอนจองที่เผยแพร่ไม่ได้ระบุว่าต้องสมัครสมาชิกแยกก่อนจอง คนภายนอกใช้ช่อง National ID และแสดงบัตรประชาชนตอนเช็กอิน ค่าบริการขึ้นกับกลุ่มผู้ใช้และบริการ [S1]
• หัวข้อเชิงความหมาย: service_policy [S2]
```

หลัง: strict=True, source_contract_pass, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C10-Q089 — กฎการใช้บริการ

ขอสอบถามหน่อยครับ ถ่ายใบหน้าลูกค้าคนอื่นแล้วเผยแพร่ได้โดยไม่ขอไหม

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, additional_or_wrong_scope_claims, state=answer

```text
**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: ไม่ต้องเป็นนักศึกษา PSU ครับ ขั้นตอนจองที่เผยแพร่ไม่ได้ระบุว่าต้องสมัครสมาชิกแยกก่อนจอง คนภายนอกใช้ช่อง National ID และแสดงบัตรประชาชนตอนเช็กอิน ค่าบริการขึ้นกับกลุ่มผู้ใช้และบริการ [S1]
• หัวข้อเชิงความหมาย: service_policy [S2]
```

หลัง: strict=True, source_contract_pass, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C10-Q092 — กฎการใช้บริการ

ช่วยตอบสั้น ๆ ว่า ถ่ายใบหน้าลูกค้าคนอื่นแล้วเผยแพร่ได้โดยไม่ขอไหม

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, additional_or_wrong_scope_claims, state=answer

```text
**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: ไม่ต้องเป็นนักศึกษา PSU ครับ ขั้นตอนจองที่เผยแพร่ไม่ได้ระบุว่าต้องสมัครสมาชิกแยกก่อนจอง คนภายนอกใช้ช่อง National ID และแสดงบัตรประชาชนตอนเช็กอิน ค่าบริการขึ้นกับกลุ่มผู้ใช้และบริการ [S1]
• หัวข้อเชิงความหมาย: service_policy [S2]
```

หลัง: strict=True, source_contract_pass, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C10-Q095 — กฎการใช้บริการ

อยากรู้ว่า ถ่ายใบหน้าลูกค้าคนอื่นแล้วเผยแพร่ได้โดยไม่ขอไหม

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, additional_or_wrong_scope_claims, state=answer

```text
**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: ไม่ต้องเป็นนักศึกษา PSU ครับ ขั้นตอนจองที่เผยแพร่ไม่ได้ระบุว่าต้องสมัครสมาชิกแยกก่อนจอง คนภายนอกใช้ช่อง National ID และแสดงบัตรประชาชนตอนเช็กอิน ค่าบริการขึ้นกับกลุ่มผู้ใช้และบริการ [S1]
• หัวข้อเชิงความหมาย: service_policy [S2]
```

หลัง: strict=True, source_contract_pass, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C10-Q098 — กฎการใช้บริการ

กำลังวางแผนไปใช้บริการ เลยขอถามว่า ถ่ายใบหน้าลูกค้าคนอื่นแล้วเผยแพร่ได้โดยไม่ขอไหม

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, expected_state_mismatch, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=True, source_contract_pass, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C11-Q003 — ตารางเวลา

ช่วยตอบสั้น ๆ ว่า ถ้าไปวันอังคารเลือกช่วงเล่นอะไรได้บ้าง

Applicability gap: คืน recorded fields พร้อมข้อจำกัด source และ partial; ยังไม่ยืนยันสิทธิ์จอง/เวลาเปิดจริง

ก่อน: strict=True, source_contract_pass, state=answer

```text
อังคาร — ช่วงจองเล่น: 09:00–12:00; 13:00–16:00 [S1]
```

หลัง: strict=False, expected_state_mismatch, state=partial

```text
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
อังคาร — ช่วงจองเล่น: 09:00–12:00; 13:00–16:00 [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C11:migrated_schedule_1:bookable_periods",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C11:migrated_schedule_1:bookable_periods",
      "record_id": "migrated_schedule_1",
      "facet": "bookable_periods",
      "value": "09:00–12:00; 13:00–16:00",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/bookable_periods",
          "source_id": "r66_79ad8fe1d8fdf571be9dd857a9b4"
        }
      ]
    },
    "native_fact_id": "C11:migrated_schedule_1:bookable_periods",
    "native_record_id": "migrated_schedule_1",
    "facet": "bookable_periods",
    "value": "09:00–12:00; 13:00–16:00",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/bookable_periods",
        "source_id": "r66_79ad8fe1d8fdf571be9dd857a9b4"
      }
    ],
    "legacy_record_id": "migrated_schedule_1"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C11-Q005 — ตารางเวลา

กำลังวางแผนไปใช้บริการ เลยขอถามว่า วันเสาร์มีรอบไหนให้จอง

Applicability gap: คืน recorded fields พร้อมข้อจำกัด source และ partial; ยังไม่ยืนยันสิทธิ์จอง/เวลาเปิดจริง

ก่อน: strict=True, source_contract_pass, state=answer

```text
เสาร์ — ช่วงจองเล่น: ไม่มี / None [S1]
```

หลัง: strict=False, expected_state_mismatch, state=partial

```text
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
เสาร์ — ช่วงจองเล่น: ไม่มี / None [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C11:migrated_schedule_5:bookable_periods",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C11:migrated_schedule_5:bookable_periods",
      "record_id": "migrated_schedule_5",
      "facet": "bookable_periods",
      "value": "ไม่มี / None",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/bookable_periods",
          "source_id": "r63_db5d02ff0f0f325d0884bd051b79"
        }
      ]
    },
    "native_fact_id": "C11:migrated_schedule_5:bookable_periods",
    "native_record_id": "migrated_schedule_5",
    "facet": "bookable_periods",
    "value": "ไม่มี / None",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/bookable_periods",
        "source_id": "r63_db5d02ff0f0f325d0884bd051b79"
      }
    ],
    "legacy_record_id": "migrated_schedule_5"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C11-Q010 — ตารางเวลา

ช่วยตอบสั้น ๆ ว่า วันพฤหัสบดีจองเล่นได้กี่โมงถึงกี่โมง

Applicability gap: คืน recorded fields พร้อมข้อจำกัด source และ partial; ยังไม่ยืนยันสิทธิ์จอง/เวลาเปิดจริง

ก่อน: strict=False, required_claims_missing, state=answer

```text
**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: ไม่ได้เปิด 24 ชั่วโมง ตารางบริการแบ่งเป็น Morning 09:00–12:00 และ Afternoon 13:00–16:00 โดยดูตามวันดังนี้: วันจันทร์ (Monday) ช่วงเช้า 09:00–12:00 เป็น Maintenance* เล่นไม่ได้ และเปิดเล่นช่วงบ่าย 13:00–16:00; วันอังคาร-พฤหัสบดี (Tuesday-Thursday) เปิดตามรอบปกติ 09:00–12:00 และ 13:00–16:00; วันศุกร์ (Friday) เปิดช่วงเช้า 09:00–12:00 แต่ช่วงบ่าย 13:00–16:00 เป็น Maintenance** สำหรับ Weekly hardware inspection and cleaning จึงไม่ใช่ช่วงเล่น [S1]
```

หลัง: strict=False, expected_state_mismatch, state=partial

```text
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
พฤหัสบดี — ช่วงจองเล่น: 09:00–12:00; 13:00–16:00 [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C11:migrated_schedule_3:bookable_periods",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C11:migrated_schedule_3:bookable_periods",
      "record_id": "migrated_schedule_3",
      "facet": "bookable_periods",
      "value": "09:00–12:00; 13:00–16:00",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/bookable_periods",
          "source_id": "r66_78809ecbb55559e2e9b17d51575c"
        }
      ]
    },
    "native_fact_id": "C11:migrated_schedule_3:bookable_periods",
    "native_record_id": "migrated_schedule_3",
    "facet": "bookable_periods",
    "value": "09:00–12:00; 13:00–16:00",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/bookable_periods",
        "source_id": "r66_78809ecbb55559e2e9b17d51575c"
      }
    ],
    "legacy_record_id": "migrated_schedule_3"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C11-Q013 — ตารางเวลา

รบกวนเช็กให้หน่อย วันจันทร์จองเล่นได้กี่โมงถึงกี่โมง

Applicability gap: คืน recorded fields พร้อมข้อจำกัด source และ partial; ยังไม่ยืนยันสิทธิ์จอง/เวลาเปิดจริง

ก่อน: strict=False, required_claims_missing, state=answer

```text
**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: ไม่ได้เปิด 24 ชั่วโมง ตารางบริการแบ่งเป็น Morning 09:00–12:00 และ Afternoon 13:00–16:00 โดยดูตามวันดังนี้: วันจันทร์ (Monday) ช่วงเช้า 09:00–12:00 เป็น Maintenance* เล่นไม่ได้ และเปิดเล่นช่วงบ่าย 13:00–16:00; วันอังคาร-พฤหัสบดี (Tuesday-Thursday) เปิดตามรอบปกติ 09:00–12:00 และ 13:00–16:00; วันศุกร์ (Friday) เปิดช่วงเช้า 09:00–12:00 แต่ช่วงบ่าย 13:00–16:00 เป็น Maintenance** สำหรับ Weekly hardware inspection and cleaning จึงไม่ใช่ช่วงเล่น [S1]
```

หลัง: strict=False, expected_state_mismatch, state=partial

```text
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
จันทร์ — ช่วงจองเล่น: 13:00–16:00 [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C11:migrated_schedule_0:bookable_periods",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C11:migrated_schedule_0:bookable_periods",
      "record_id": "migrated_schedule_0",
      "facet": "bookable_periods",
      "value": "13:00–16:00",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/bookable_periods",
          "source_id": "r66_814dc4183099ea3715eb65d5955d"
        }
      ]
    },
    "native_fact_id": "C11:migrated_schedule_0:bookable_periods",
    "native_record_id": "migrated_schedule_0",
    "facet": "bookable_periods",
    "value": "13:00–16:00",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/bookable_periods",
        "source_id": "r66_814dc4183099ea3715eb65d5955d"
      }
    ],
    "legacy_record_id": "migrated_schedule_0"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C11-Q014 — ตารางเวลา

ถามจากข้อมูลที่ศูนย์ให้ไว้ วันอาทิตย์มีรอบไหนให้จอง

Applicability gap: คืน recorded fields พร้อมข้อจำกัด source และ partial; ยังไม่ยืนยันสิทธิ์จอง/เวลาเปิดจริง

ก่อน: strict=True, source_contract_pass, state=answer

```text
อาทิตย์ — ช่วงจองเล่น: ไม่มี / None [S1]
```

หลัง: strict=False, expected_state_mismatch, state=partial

```text
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
อาทิตย์ — ช่วงจองเล่น: ไม่มี / None [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C11:migrated_schedule_6:bookable_periods",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C11:migrated_schedule_6:bookable_periods",
      "record_id": "migrated_schedule_6",
      "facet": "bookable_periods",
      "value": "ไม่มี / None",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/bookable_periods",
          "source_id": "r63_0b8c029e53f349f494c5d60c130c"
        }
      ]
    },
    "native_fact_id": "C11:migrated_schedule_6:bookable_periods",
    "native_record_id": "migrated_schedule_6",
    "facet": "bookable_periods",
    "value": "ไม่มี / None",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/bookable_periods",
        "source_id": "r63_0b8c029e53f349f494c5d60c130c"
      }
    ],
    "legacy_record_id": "migrated_schedule_6"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C11-Q017 — ตารางเวลา

ช่วยตอบสั้น ๆ ว่า วันศุกร์มีรอบไหนให้จอง

Applicability gap: คืน recorded fields พร้อมข้อจำกัด source และ partial; ยังไม่ยืนยันสิทธิ์จอง/เวลาเปิดจริง

ก่อน: strict=True, source_contract_pass, state=answer

```text
ศุกร์ — ช่วงจองเล่น: 09:00–12:00 [S1]
```

หลัง: strict=False, expected_state_mismatch, state=partial

```text
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
ศุกร์ — ช่วงจองเล่น: 09:00–12:00 [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C11:migrated_schedule_4:bookable_periods",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C11:migrated_schedule_4:bookable_periods",
      "record_id": "migrated_schedule_4",
      "facet": "bookable_periods",
      "value": "09:00–12:00",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/bookable_periods",
          "source_id": "r66_8b8799fa0b0f242ce50dede11782"
        }
      ]
    },
    "native_fact_id": "C11:migrated_schedule_4:bookable_periods",
    "native_record_id": "migrated_schedule_4",
    "facet": "bookable_periods",
    "value": "09:00–12:00",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/bookable_periods",
        "source_id": "r66_8b8799fa0b0f242ce50dede11782"
      }
    ],
    "legacy_record_id": "migrated_schedule_4"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C11-Q021 — ตารางเวลา

ถามจากข้อมูลที่ศูนย์ให้ไว้ ถ้าไปวันพุธเลือกช่วงเล่นอะไรได้บ้าง

Applicability gap: คืน recorded fields พร้อมข้อจำกัด source และ partial; ยังไม่ยืนยันสิทธิ์จอง/เวลาเปิดจริง

ก่อน: strict=True, source_contract_pass, state=answer

```text
พุธ — ช่วงจองเล่น: 09:00–12:00; 13:00–16:00 [S1]
```

หลัง: strict=False, expected_state_mismatch, state=partial

```text
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
พุธ — ช่วงจองเล่น: 09:00–12:00; 13:00–16:00 [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C11:migrated_schedule_2:bookable_periods",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C11:migrated_schedule_2:bookable_periods",
      "record_id": "migrated_schedule_2",
      "facet": "bookable_periods",
      "value": "09:00–12:00; 13:00–16:00",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/bookable_periods",
          "source_id": "r66_aa6f1c71e4e35173d2c541946b8b"
        }
      ]
    },
    "native_fact_id": "C11:migrated_schedule_2:bookable_periods",
    "native_record_id": "migrated_schedule_2",
    "facet": "bookable_periods",
    "value": "09:00–12:00; 13:00–16:00",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/bookable_periods",
        "source_id": "r66_aa6f1c71e4e35173d2c541946b8b"
      }
    ],
    "legacy_record_id": "migrated_schedule_2"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C11-Q025 — ตารางเวลา

อยากรู้ว่า วันอังคารจองเล่นได้กี่โมงถึงกี่โมง

Applicability gap: คืน recorded fields พร้อมข้อจำกัด source และ partial; ยังไม่ยืนยันสิทธิ์จอง/เวลาเปิดจริง

ก่อน: strict=False, required_claims_missing, state=answer

```text
**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: ไม่ได้เปิด 24 ชั่วโมง ตารางบริการแบ่งเป็น Morning 09:00–12:00 และ Afternoon 13:00–16:00 โดยดูตามวันดังนี้: วันจันทร์ (Monday) ช่วงเช้า 09:00–12:00 เป็น Maintenance* เล่นไม่ได้ และเปิดเล่นช่วงบ่าย 13:00–16:00; วันอังคาร-พฤหัสบดี (Tuesday-Thursday) เปิดตามรอบปกติ 09:00–12:00 และ 13:00–16:00; วันศุกร์ (Friday) เปิดช่วงเช้า 09:00–12:00 แต่ช่วงบ่าย 13:00–16:00 เป็น Maintenance** สำหรับ Weekly hardware inspection and cleaning จึงไม่ใช่ช่วงเล่น [S1]
```

หลัง: strict=False, expected_state_mismatch, state=partial

```text
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
อังคาร — ช่วงจองเล่น: 09:00–12:00; 13:00–16:00 [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C11:migrated_schedule_1:bookable_periods",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C11:migrated_schedule_1:bookable_periods",
      "record_id": "migrated_schedule_1",
      "facet": "bookable_periods",
      "value": "09:00–12:00; 13:00–16:00",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/bookable_periods",
          "source_id": "r66_79ad8fe1d8fdf571be9dd857a9b4"
        }
      ]
    },
    "native_fact_id": "C11:migrated_schedule_1:bookable_periods",
    "native_record_id": "migrated_schedule_1",
    "facet": "bookable_periods",
    "value": "09:00–12:00; 13:00–16:00",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/bookable_periods",
        "source_id": "r66_79ad8fe1d8fdf571be9dd857a9b4"
      }
    ],
    "legacy_record_id": "migrated_schedule_1"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C11-Q027 — ตารางเวลา

รบกวนเช็กให้หน่อย ถ้าไปวันเสาร์เลือกช่วงเล่นอะไรได้บ้าง

Applicability gap: คืน recorded fields พร้อมข้อจำกัด source และ partial; ยังไม่ยืนยันสิทธิ์จอง/เวลาเปิดจริง

ก่อน: strict=True, source_contract_pass, state=answer

```text
เสาร์ — ช่วงจองเล่น: ไม่มี / None [S1]
```

หลัง: strict=False, expected_state_mismatch, state=partial

```text
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
เสาร์ — ช่วงจองเล่น: ไม่มี / None [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C11:migrated_schedule_5:bookable_periods",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C11:migrated_schedule_5:bookable_periods",
      "record_id": "migrated_schedule_5",
      "facet": "bookable_periods",
      "value": "ไม่มี / None",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/bookable_periods",
          "source_id": "r63_db5d02ff0f0f325d0884bd051b79"
        }
      ]
    },
    "native_fact_id": "C11:migrated_schedule_5:bookable_periods",
    "native_record_id": "migrated_schedule_5",
    "facet": "bookable_periods",
    "value": "ไม่มี / None",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/bookable_periods",
        "source_id": "r63_db5d02ff0f0f325d0884bd051b79"
      }
    ],
    "legacy_record_id": "migrated_schedule_5"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C11-Q032 — ตารางเวลา

อยากรู้ว่า วันพฤหัสบดีมีรอบไหนให้จอง

Applicability gap: คืน recorded fields พร้อมข้อจำกัด source และ partial; ยังไม่ยืนยันสิทธิ์จอง/เวลาเปิดจริง

ก่อน: strict=True, source_contract_pass, state=answer

```text
พฤหัสบดี — ช่วงจองเล่น: 09:00–12:00; 13:00–16:00 [S1]
```

หลัง: strict=False, expected_state_mismatch, state=partial

```text
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
พฤหัสบดี — ช่วงจองเล่น: 09:00–12:00; 13:00–16:00 [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C11:migrated_schedule_3:bookable_periods",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C11:migrated_schedule_3:bookable_periods",
      "record_id": "migrated_schedule_3",
      "facet": "bookable_periods",
      "value": "09:00–12:00; 13:00–16:00",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/bookable_periods",
          "source_id": "r66_78809ecbb55559e2e9b17d51575c"
        }
      ]
    },
    "native_fact_id": "C11:migrated_schedule_3:bookable_periods",
    "native_record_id": "migrated_schedule_3",
    "facet": "bookable_periods",
    "value": "09:00–12:00; 13:00–16:00",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/bookable_periods",
        "source_id": "r66_78809ecbb55559e2e9b17d51575c"
      }
    ],
    "legacy_record_id": "migrated_schedule_3"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C11-Q035 — ตารางเวลา

ถามจากข้อมูลที่ศูนย์ให้ไว้ วันจันทร์มีรอบไหนให้จอง

Applicability gap: คืน recorded fields พร้อมข้อจำกัด source และ partial; ยังไม่ยืนยันสิทธิ์จอง/เวลาเปิดจริง

ก่อน: strict=True, source_contract_pass, state=answer

```text
จันทร์ — ช่วงจองเล่น: 13:00–16:00 [S1]
```

หลัง: strict=False, expected_state_mismatch, state=partial

```text
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
จันทร์ — ช่วงจองเล่น: 13:00–16:00 [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C11:migrated_schedule_0:bookable_periods",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C11:migrated_schedule_0:bookable_periods",
      "record_id": "migrated_schedule_0",
      "facet": "bookable_periods",
      "value": "13:00–16:00",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/bookable_periods",
          "source_id": "r66_814dc4183099ea3715eb65d5955d"
        }
      ]
    },
    "native_fact_id": "C11:migrated_schedule_0:bookable_periods",
    "native_record_id": "migrated_schedule_0",
    "facet": "bookable_periods",
    "value": "13:00–16:00",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/bookable_periods",
        "source_id": "r66_814dc4183099ea3715eb65d5955d"
      }
    ],
    "legacy_record_id": "migrated_schedule_0"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C11-Q036 — ตารางเวลา

ถ้าไปวันอาทิตย์เลือกช่วงเล่นอะไรได้บ้าง

Applicability gap: คืน recorded fields พร้อมข้อจำกัด source และ partial; ยังไม่ยืนยันสิทธิ์จอง/เวลาเปิดจริง

ก่อน: strict=True, source_contract_pass, state=answer

```text
อาทิตย์ — ช่วงจองเล่น: ไม่มี / None [S1]
```

หลัง: strict=False, expected_state_mismatch, state=partial

```text
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
อาทิตย์ — ช่วงจองเล่น: ไม่มี / None [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C11:migrated_schedule_6:bookable_periods",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C11:migrated_schedule_6:bookable_periods",
      "record_id": "migrated_schedule_6",
      "facet": "bookable_periods",
      "value": "ไม่มี / None",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/bookable_periods",
          "source_id": "r63_0b8c029e53f349f494c5d60c130c"
        }
      ]
    },
    "native_fact_id": "C11:migrated_schedule_6:bookable_periods",
    "native_record_id": "migrated_schedule_6",
    "facet": "bookable_periods",
    "value": "ไม่มี / None",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/bookable_periods",
        "source_id": "r63_0b8c029e53f349f494c5d60c130c"
      }
    ],
    "legacy_record_id": "migrated_schedule_6"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C11-Q039 — ตารางเวลา

อยากรู้ว่า ถ้าไปวันศุกร์เลือกช่วงเล่นอะไรได้บ้าง

Applicability gap: คืน recorded fields พร้อมข้อจำกัด source และ partial; ยังไม่ยืนยันสิทธิ์จอง/เวลาเปิดจริง

ก่อน: strict=True, source_contract_pass, state=answer

```text
ศุกร์ — ช่วงจองเล่น: 09:00–12:00 [S1]
```

หลัง: strict=False, expected_state_mismatch, state=partial

```text
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
ศุกร์ — ช่วงจองเล่น: 09:00–12:00 [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C11:migrated_schedule_4:bookable_periods",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C11:migrated_schedule_4:bookable_periods",
      "record_id": "migrated_schedule_4",
      "facet": "bookable_periods",
      "value": "09:00–12:00",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/bookable_periods",
          "source_id": "r66_8b8799fa0b0f242ce50dede11782"
        }
      ]
    },
    "native_fact_id": "C11:migrated_schedule_4:bookable_periods",
    "native_record_id": "migrated_schedule_4",
    "facet": "bookable_periods",
    "value": "09:00–12:00",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/bookable_periods",
        "source_id": "r66_8b8799fa0b0f242ce50dede11782"
      }
    ],
    "legacy_record_id": "migrated_schedule_4"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C11-Q043 — ตารางเวลา

วันพุธจองเล่นได้กี่โมงถึงกี่โมง

Applicability gap: คืน recorded fields พร้อมข้อจำกัด source และ partial; ยังไม่ยืนยันสิทธิ์จอง/เวลาเปิดจริง

ก่อน: strict=False, required_claims_missing, state=answer

```text
**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: ไม่ได้เปิด 24 ชั่วโมง ตารางบริการแบ่งเป็น Morning 09:00–12:00 และ Afternoon 13:00–16:00 โดยดูตามวันดังนี้: วันจันทร์ (Monday) ช่วงเช้า 09:00–12:00 เป็น Maintenance* เล่นไม่ได้ และเปิดเล่นช่วงบ่าย 13:00–16:00; วันอังคาร-พฤหัสบดี (Tuesday-Thursday) เปิดตามรอบปกติ 09:00–12:00 และ 13:00–16:00; วันศุกร์ (Friday) เปิดช่วงเช้า 09:00–12:00 แต่ช่วงบ่าย 13:00–16:00 เป็น Maintenance** สำหรับ Weekly hardware inspection and cleaning จึงไม่ใช่ช่วงเล่น [S1]
```

หลัง: strict=False, expected_state_mismatch, state=partial

```text
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
พุธ — ช่วงจองเล่น: 09:00–12:00; 13:00–16:00 [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C11:migrated_schedule_2:bookable_periods",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C11:migrated_schedule_2:bookable_periods",
      "record_id": "migrated_schedule_2",
      "facet": "bookable_periods",
      "value": "09:00–12:00; 13:00–16:00",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/bookable_periods",
          "source_id": "r66_aa6f1c71e4e35173d2c541946b8b"
        }
      ]
    },
    "native_fact_id": "C11:migrated_schedule_2:bookable_periods",
    "native_record_id": "migrated_schedule_2",
    "facet": "bookable_periods",
    "value": "09:00–12:00; 13:00–16:00",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/bookable_periods",
        "source_id": "r66_aa6f1c71e4e35173d2c541946b8b"
      }
    ],
    "legacy_record_id": "migrated_schedule_2"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C11-Q047 — ตารางเวลา

กำลังวางแผนไปใช้บริการ เลยขอถามว่า วันอังคารมีรอบไหนให้จอง

Applicability gap: คืน recorded fields พร้อมข้อจำกัด source และ partial; ยังไม่ยืนยันสิทธิ์จอง/เวลาเปิดจริง

ก่อน: strict=True, source_contract_pass, state=answer

```text
อังคาร — ช่วงจองเล่น: 09:00–12:00; 13:00–16:00 [S1]
```

หลัง: strict=False, expected_state_mismatch, state=partial

```text
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
อังคาร — ช่วงจองเล่น: 09:00–12:00; 13:00–16:00 [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C11:migrated_schedule_1:bookable_periods",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C11:migrated_schedule_1:bookable_periods",
      "record_id": "migrated_schedule_1",
      "facet": "bookable_periods",
      "value": "09:00–12:00; 13:00–16:00",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/bookable_periods",
          "source_id": "r66_79ad8fe1d8fdf571be9dd857a9b4"
        }
      ]
    },
    "native_fact_id": "C11:migrated_schedule_1:bookable_periods",
    "native_record_id": "migrated_schedule_1",
    "facet": "bookable_periods",
    "value": "09:00–12:00; 13:00–16:00",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/bookable_periods",
        "source_id": "r66_79ad8fe1d8fdf571be9dd857a9b4"
      }
    ],
    "legacy_record_id": "migrated_schedule_1"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C11-Q049 — ตารางเวลา

ถามจากข้อมูลที่ศูนย์ให้ไว้ วันเสาร์จองเล่นได้กี่โมงถึงกี่โมง

Applicability gap: คืน recorded fields พร้อมข้อจำกัด source และ partial; ยังไม่ยืนยันสิทธิ์จอง/เวลาเปิดจริง

ก่อน: strict=False, required_claims_missing, state=answer

```text
**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: ไม่ได้เปิด 24 ชั่วโมง ตารางบริการแบ่งเป็น Morning 09:00–12:00 และ Afternoon 13:00–16:00 โดยดูตามวันดังนี้: วันจันทร์ (Monday) ช่วงเช้า 09:00–12:00 เป็น Maintenance* เล่นไม่ได้ และเปิดเล่นช่วงบ่าย 13:00–16:00; วันอังคาร-พฤหัสบดี (Tuesday-Thursday) เปิดตามรอบปกติ 09:00–12:00 และ 13:00–16:00; วันศุกร์ (Friday) เปิดช่วงเช้า 09:00–12:00 แต่ช่วงบ่าย 13:00–16:00 เป็น Maintenance** สำหรับ Weekly hardware inspection and cleaning จึงไม่ใช่ช่วงเล่น [S1]
```

หลัง: strict=False, expected_state_mismatch, state=partial

```text
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
เสาร์ — ช่วงจองเล่น: ไม่มี / None [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C11:migrated_schedule_5:bookable_periods",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C11:migrated_schedule_5:bookable_periods",
      "record_id": "migrated_schedule_5",
      "facet": "bookable_periods",
      "value": "ไม่มี / None",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/bookable_periods",
          "source_id": "r63_db5d02ff0f0f325d0884bd051b79"
        }
      ]
    },
    "native_fact_id": "C11:migrated_schedule_5:bookable_periods",
    "native_record_id": "migrated_schedule_5",
    "facet": "bookable_periods",
    "value": "ไม่มี / None",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/bookable_periods",
        "source_id": "r63_db5d02ff0f0f325d0884bd051b79"
      }
    ],
    "legacy_record_id": "migrated_schedule_5"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C11-Q054 — ตารางเวลา

I would like to know: What are the bookable hours on Thursday?

Applicability gap: คืน recorded fields พร้อมข้อจำกัด source และ partial; ยังไม่ยืนยันสิทธิ์จอง/เวลาเปิดจริง

ก่อน: strict=False, required_claims_missing, state=answer

```text
**Relevant information**
• Confirmed information: The studio is not open 24 hours. Service sessions are Morning 09:00-12:00 and Afternoon 13:00-16:00. By day: Monday morning 09:00-12:00 is Maintenance* and not playable, while Monday afternoon 13:00-16:00 is open; Tuesday-Thursday follow the regular slots 09:00-12:00 and 13:00-16:00; Friday morning 09:00-12:00 is open, but Friday afternoon 13:00-16:00 is Maintenance** for weekly hardware inspection and cleaning, so it is not playable. [S1]

English translation is machine generated and has not been reviewed by the owner.
```

หลัง: strict=False, expected_state_mismatch, state=partial

```text
Recorded schedule only: zone and effective dates are unconfirmed; some opening-hour sources conflict. This does not confirm current opening or actual booking eligibility.
Thursday — bookable periods: 09:00–12:00; 13:00–16:00 [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C11:migrated_schedule_3:bookable_periods",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C11:migrated_schedule_3:bookable_periods",
      "record_id": "migrated_schedule_3",
      "facet": "bookable_periods",
      "value": "09:00–12:00; 13:00–16:00",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/bookable_periods",
          "source_id": "r66_78809ecbb55559e2e9b17d51575c"
        }
      ]
    },
    "native_fact_id": "C11:migrated_schedule_3:bookable_periods",
    "native_record_id": "migrated_schedule_3",
    "facet": "bookable_periods",
    "value": "09:00–12:00; 13:00–16:00",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/bookable_periods",
        "source_id": "r66_78809ecbb55559e2e9b17d51575c"
      }
    ],
    "legacy_record_id": "migrated_schedule_3"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C11-Q057 — ตารางเวลา

Could you help me with this: When can I reserve a play session on Monday?

Applicability gap: คืน recorded fields พร้อมข้อจำกัด source และ partial; ยังไม่ยืนยันสิทธิ์จอง/เวลาเปิดจริง

ก่อน: strict=True, source_contract_pass, state=answer

```text
Monday — bookable periods: 13:00–16:00 [S1]
```

หลัง: strict=False, expected_state_mismatch, state=partial

```text
Recorded schedule only: zone and effective dates are unconfirmed; some opening-hour sources conflict. This does not confirm current opening or actual booking eligibility.
Monday — bookable periods: 13:00–16:00 [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C11:migrated_schedule_0:bookable_periods",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C11:migrated_schedule_0:bookable_periods",
      "record_id": "migrated_schedule_0",
      "facet": "bookable_periods",
      "value": "13:00–16:00",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/bookable_periods",
          "source_id": "r66_814dc4183099ea3715eb65d5955d"
        }
      ]
    },
    "native_fact_id": "C11:migrated_schedule_0:bookable_periods",
    "native_record_id": "migrated_schedule_0",
    "facet": "bookable_periods",
    "value": "13:00–16:00",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/bookable_periods",
        "source_id": "r66_814dc4183099ea3715eb65d5955d"
      }
    ],
    "legacy_record_id": "migrated_schedule_0"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C11-Q058 — ตารางเวลา

Please answer briefly: What are the bookable hours on Sunday?

Applicability gap: คืน recorded fields พร้อมข้อจำกัด source และ partial; ยังไม่ยืนยันสิทธิ์จอง/เวลาเปิดจริง

ก่อน: strict=False, required_claims_missing, state=answer

```text
**Relevant information**
• Confirmed information: The studio is not open 24 hours. Service sessions are Morning 09:00-12:00 and Afternoon 13:00-16:00. By day: Monday morning 09:00-12:00 is Maintenance* and not playable, while Monday afternoon 13:00-16:00 is open; Tuesday-Thursday follow the regular slots 09:00-12:00 and 13:00-16:00; Friday morning 09:00-12:00 is open, but Friday afternoon 13:00-16:00 is Maintenance** for weekly hardware inspection and cleaning, so it is not playable. [S1]

English translation is machine generated and has not been reviewed by the owner.
```

หลัง: strict=False, expected_state_mismatch, state=partial

```text
Recorded schedule only: zone and effective dates are unconfirmed; some opening-hour sources conflict. This does not confirm current opening or actual booking eligibility.
Sunday — bookable periods: ไม่มี / None [S1]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C11:migrated_schedule_6:bookable_periods",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C11:migrated_schedule_6:bookable_periods",
      "record_id": "migrated_schedule_6",
      "facet": "bookable_periods",
      "value": "ไม่มี / None",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/bookable_periods",
          "source_id": "r63_0b8c029e53f349f494c5d60c130c"
        }
      ]
    },
    "native_fact_id": "C11:migrated_schedule_6:bookable_periods",
    "native_record_id": "migrated_schedule_6",
    "facet": "bookable_periods",
    "value": "ไม่มี / None",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/bookable_periods",
        "source_id": "r63_0b8c029e53f349f494c5d60c130c"
      }
    ],
    "legacy_record_id": "migrated_schedule_6"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C11-Q061 — ตารางเวลา

When can I reserve a play session on Friday? and also Which hours are reserved for maintenance on Friday?

Applicability gap: คืน recorded fields พร้อมข้อจำกัด source และ partial; ยังไม่ยืนยันสิทธิ์จอง/เวลาเปิดจริง

ก่อน: strict=True, source_contract_pass, state=answer

```text
1. when can i reserve a play session on friday
Friday — bookable periods: 09:00–12:00 [S1]

2. which hours are reserved for maintenance on friday
Friday — maintenance periods: 13:00–16:00 [S2]
```

หลัง: strict=False, expected_state_mismatch, state=partial

```text
1. when can i reserve a play session on friday
Recorded schedule only: zone and effective dates are unconfirmed; some opening-hour sources conflict. This does not confirm current opening or actual booking eligibility.
Friday — bookable periods: 09:00–12:00 [S1]

2. which hours are reserved for maintenance on friday
Recorded schedule only: zone and effective dates are unconfirmed; some opening-hour sources conflict. This does not confirm current opening or actual booking eligibility.
Friday — maintenance periods: 13:00–16:00 [S2]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C11:migrated_schedule_4:bookable_periods",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C11:migrated_schedule_4:bookable_periods",
      "record_id": "migrated_schedule_4",
      "facet": "bookable_periods",
      "value": "09:00–12:00",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/bookable_periods",
          "source_id": "r66_8b8799fa0b0f242ce50dede11782"
        }
      ]
    },
    "native_fact_id": "C11:migrated_schedule_4:bookable_periods",
    "native_record_id": "migrated_schedule_4",
    "facet": "bookable_periods",
    "value": "09:00–12:00",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/bookable_periods",
        "source_id": "r66_8b8799fa0b0f242ce50dede11782"
      }
    ],
    "legacy_record_id": "migrated_schedule_4"
  },
  {
    "legacy_fact_id": "C11:migrated_schedule_4:maintenance_periods",
    "alignment_kind": "aligned",
    "legacy_expected": {
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
      ]
    },
    "native_fact_id": "C11:migrated_schedule_4:maintenance_periods",
    "native_record_id": "migrated_schedule_4",
    "facet": "maintenance_periods",
    "value": "13:00–16:00",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/maintenance_periods",
        "source_id": "r66_8b8799fa0b0f242ce50dede11782"
      }
    ],
    "legacy_record_id": "migrated_schedule_4"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C11-Q065 — ตารางเวลา

Based on the studio sources, When can I reserve a play session on Wednesday? and also Which hours are reserved for maintenance on Wednesday?

Applicability gap: คืน recorded fields พร้อมข้อจำกัด source และ partial; ยังไม่ยืนยันสิทธิ์จอง/เวลาเปิดจริง

ก่อน: strict=True, source_contract_pass, state=answer

```text
1. based on the studio sources, when can i reserve a play session on wednesday
Wednesday — bookable periods: 09:00–12:00; 13:00–16:00 [S1]

2. which hours are reserved for maintenance on wednesday
Wednesday — maintenance periods: ไม่มี / None [S2]
```

หลัง: strict=False, expected_state_mismatch, state=partial

```text
1. based on the studio sources, when can i reserve a play session on wednesday
Recorded schedule only: zone and effective dates are unconfirmed; some opening-hour sources conflict. This does not confirm current opening or actual booking eligibility.
Wednesday — bookable periods: 09:00–12:00; 13:00–16:00 [S1]

2. which hours are reserved for maintenance on wednesday
Recorded schedule only: zone and effective dates are unconfirmed; some opening-hour sources conflict. This does not confirm current opening or actual booking eligibility.
Wednesday — maintenance periods: ไม่มี / None [S2]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C11:migrated_schedule_2:bookable_periods",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C11:migrated_schedule_2:bookable_periods",
      "record_id": "migrated_schedule_2",
      "facet": "bookable_periods",
      "value": "09:00–12:00; 13:00–16:00",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/bookable_periods",
          "source_id": "r66_aa6f1c71e4e35173d2c541946b8b"
        }
      ]
    },
    "native_fact_id": "C11:migrated_schedule_2:bookable_periods",
    "native_record_id": "migrated_schedule_2",
    "facet": "bookable_periods",
    "value": "09:00–12:00; 13:00–16:00",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/bookable_periods",
        "source_id": "r66_aa6f1c71e4e35173d2c541946b8b"
      }
    ],
    "legacy_record_id": "migrated_schedule_2"
  },
  {
    "legacy_fact_id": "C11:migrated_schedule_2:maintenance_periods",
    "alignment_kind": "aligned",
    "legacy_expected": {
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
      ]
    },
    "native_fact_id": "C11:migrated_schedule_2:maintenance_periods",
    "native_record_id": "migrated_schedule_2",
    "facet": "maintenance_periods",
    "value": "ไม่มี / None",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/maintenance_periods",
        "source_id": "r66_aa6f1c71e4e35173d2c541946b8b"
      }
    ],
    "legacy_record_id": "migrated_schedule_2"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C11-Q066 — ตารางเวลา

Which hours are reserved for maintenance on Sunday? and also When can I reserve a play session on Sunday?

Applicability gap: คืน recorded fields พร้อมข้อจำกัด source และ partial; ยังไม่ยืนยันสิทธิ์จอง/เวลาเปิดจริง

ก่อน: strict=True, source_contract_pass, state=answer

```text
1. which hours are reserved for maintenance on sunday
Sunday — maintenance periods: ไม่มี / None [S1]

2. when can i reserve a play session on sunday
Sunday — bookable periods: ไม่มี / None [S2]
```

หลัง: strict=False, expected_state_mismatch, state=partial

```text
1. which hours are reserved for maintenance on sunday
Recorded schedule only: zone and effective dates are unconfirmed; some opening-hour sources conflict. This does not confirm current opening or actual booking eligibility.
Sunday — maintenance periods: ไม่มี / None [S1]

2. when can i reserve a play session on sunday
Recorded schedule only: zone and effective dates are unconfirmed; some opening-hour sources conflict. This does not confirm current opening or actual booking eligibility.
Sunday — bookable periods: ไม่มี / None [S2]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C11:migrated_schedule_6:maintenance_periods",
    "alignment_kind": "aligned",
    "legacy_expected": {
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
      ]
    },
    "native_fact_id": "C11:migrated_schedule_6:maintenance_periods",
    "native_record_id": "migrated_schedule_6",
    "facet": "maintenance_periods",
    "value": "ไม่มี / None",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/maintenance_periods",
        "source_id": "r66_091dff62944f36ea9ad9068a5c8b"
      }
    ],
    "legacy_record_id": "migrated_schedule_6"
  },
  {
    "legacy_fact_id": "C11:migrated_schedule_6:bookable_periods",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C11:migrated_schedule_6:bookable_periods",
      "record_id": "migrated_schedule_6",
      "facet": "bookable_periods",
      "value": "ไม่มี / None",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/bookable_periods",
          "source_id": "r63_0b8c029e53f349f494c5d60c130c"
        }
      ]
    },
    "native_fact_id": "C11:migrated_schedule_6:bookable_periods",
    "native_record_id": "migrated_schedule_6",
    "facet": "bookable_periods",
    "value": "ไม่มี / None",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/bookable_periods",
        "source_id": "r63_0b8c029e53f349f494c5d60c130c"
      }
    ],
    "legacy_record_id": "migrated_schedule_6"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C11-Q067 — ตารางเวลา

Could you help me with this: When is maintenance on Tuesday? and also What are the bookable hours on Tuesday?

Applicability gap: คืน recorded fields พร้อมข้อจำกัด source และ partial; ยังไม่ยืนยันสิทธิ์จอง/เวลาเปิดจริง

ก่อน: strict=False, required_claims_missing, state=answer

```text
1. when is maintenance on tuesday
Tuesday — maintenance periods: ไม่มี / None [S1]

2. what are the bookable hours on tuesday
**Relevant information**
• Confirmed information: The studio is not open 24 hours. Service sessions are Morning 09:00-12:00 and Afternoon 13:00-16:00. By day: Monday morning 09:00-12:00 is Maintenance* and not playable, while Monday afternoon 13:00-16:00 is open; Tuesday-Thursday follow the regular slots 09:00-12:00 and 13:00-16:00; Friday morning 09:00-12:00 is open, but Friday afternoon 13:00-16:00 is Maintenance** for weekly hardware inspection and cleaning, so it is not playable. [S2]

English translation is machine generated and has not been reviewed by the owner.
```

หลัง: strict=False, expected_state_mismatch, state=partial

```text
1. when is maintenance on tuesday
Recorded schedule only: zone and effective dates are unconfirmed; some opening-hour sources conflict. This does not confirm current opening or actual booking eligibility.
Tuesday — maintenance periods: ไม่มี / None [S1]

2. what are the bookable hours on tuesday
Recorded schedule only: zone and effective dates are unconfirmed; some opening-hour sources conflict. This does not confirm current opening or actual booking eligibility.
Tuesday — bookable periods: 09:00–12:00; 13:00–16:00 [S2]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C11:migrated_schedule_1:maintenance_periods",
    "alignment_kind": "aligned",
    "legacy_expected": {
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
      ]
    },
    "native_fact_id": "C11:migrated_schedule_1:maintenance_periods",
    "native_record_id": "migrated_schedule_1",
    "facet": "maintenance_periods",
    "value": "ไม่มี / None",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/maintenance_periods",
        "source_id": "r66_79ad8fe1d8fdf571be9dd857a9b4"
      }
    ],
    "legacy_record_id": "migrated_schedule_1"
  },
  {
    "legacy_fact_id": "C11:migrated_schedule_1:bookable_periods",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C11:migrated_schedule_1:bookable_periods",
      "record_id": "migrated_schedule_1",
      "facet": "bookable_periods",
      "value": "09:00–12:00; 13:00–16:00",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/bookable_periods",
          "source_id": "r66_79ad8fe1d8fdf571be9dd857a9b4"
        }
      ]
    },
    "native_fact_id": "C11:migrated_schedule_1:bookable_periods",
    "native_record_id": "migrated_schedule_1",
    "facet": "bookable_periods",
    "value": "09:00–12:00; 13:00–16:00",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/bookable_periods",
        "source_id": "r66_79ad8fe1d8fdf571be9dd857a9b4"
      }
    ],
    "legacy_record_id": "migrated_schedule_1"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C11-Q069 — ตารางเวลา

I would like to know: When can I reserve a play session on Tuesday? and also Which hours are reserved for maintenance on Tuesday?

Applicability gap: คืน recorded fields พร้อมข้อจำกัด source และ partial; ยังไม่ยืนยันสิทธิ์จอง/เวลาเปิดจริง

ก่อน: strict=True, source_contract_pass, state=answer

```text
1. when can i reserve a play session on tuesday
Tuesday — bookable periods: 09:00–12:00; 13:00–16:00 [S1]

2. which hours are reserved for maintenance on tuesday
Tuesday — maintenance periods: ไม่มี / None [S2]
```

หลัง: strict=False, expected_state_mismatch, state=partial

```text
1. when can i reserve a play session on tuesday
Recorded schedule only: zone and effective dates are unconfirmed; some opening-hour sources conflict. This does not confirm current opening or actual booking eligibility.
Tuesday — bookable periods: 09:00–12:00; 13:00–16:00 [S1]

2. which hours are reserved for maintenance on tuesday
Recorded schedule only: zone and effective dates are unconfirmed; some opening-hour sources conflict. This does not confirm current opening or actual booking eligibility.
Tuesday — maintenance periods: ไม่มี / None [S2]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C11:migrated_schedule_1:bookable_periods",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C11:migrated_schedule_1:bookable_periods",
      "record_id": "migrated_schedule_1",
      "facet": "bookable_periods",
      "value": "09:00–12:00; 13:00–16:00",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/bookable_periods",
          "source_id": "r66_79ad8fe1d8fdf571be9dd857a9b4"
        }
      ]
    },
    "native_fact_id": "C11:migrated_schedule_1:bookable_periods",
    "native_record_id": "migrated_schedule_1",
    "facet": "bookable_periods",
    "value": "09:00–12:00; 13:00–16:00",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/bookable_periods",
        "source_id": "r66_79ad8fe1d8fdf571be9dd857a9b4"
      }
    ],
    "legacy_record_id": "migrated_schedule_1"
  },
  {
    "legacy_fact_id": "C11:migrated_schedule_1:maintenance_periods",
    "alignment_kind": "aligned",
    "legacy_expected": {
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
      ]
    },
    "native_fact_id": "C11:migrated_schedule_1:maintenance_periods",
    "native_record_id": "migrated_schedule_1",
    "facet": "maintenance_periods",
    "value": "ไม่มี / None",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/maintenance_periods",
        "source_id": "r66_79ad8fe1d8fdf571be9dd857a9b4"
      }
    ],
    "legacy_record_id": "migrated_schedule_1"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C11-Q070 — ตารางเวลา

Based on the studio sources, Which hours are reserved for maintenance on Thursday? and also When can I reserve a play session on Thursday?

Applicability gap: คืน recorded fields พร้อมข้อจำกัด source และ partial; ยังไม่ยืนยันสิทธิ์จอง/เวลาเปิดจริง

ก่อน: strict=True, source_contract_pass, state=answer

```text
1. based on the studio sources, which hours are reserved for maintenance on thursday
Thursday — maintenance periods: ไม่มี / None [S1]

2. when can i reserve a play session on thursday
Thursday — bookable periods: 09:00–12:00; 13:00–16:00 [S2]
```

หลัง: strict=False, expected_state_mismatch, state=partial

```text
1. based on the studio sources, which hours are reserved for maintenance on thursday
Recorded schedule only: zone and effective dates are unconfirmed; some opening-hour sources conflict. This does not confirm current opening or actual booking eligibility.
Thursday — maintenance periods: ไม่มี / None [S1]

2. when can i reserve a play session on thursday
Recorded schedule only: zone and effective dates are unconfirmed; some opening-hour sources conflict. This does not confirm current opening or actual booking eligibility.
Thursday — bookable periods: 09:00–12:00; 13:00–16:00 [S2]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C11:migrated_schedule_3:maintenance_periods",
    "alignment_kind": "aligned",
    "legacy_expected": {
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
      ]
    },
    "native_fact_id": "C11:migrated_schedule_3:maintenance_periods",
    "native_record_id": "migrated_schedule_3",
    "facet": "maintenance_periods",
    "value": "ไม่มี / None",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/maintenance_periods",
        "source_id": "r66_78809ecbb55559e2e9b17d51575c"
      }
    ],
    "legacy_record_id": "migrated_schedule_3"
  },
  {
    "legacy_fact_id": "C11:migrated_schedule_3:bookable_periods",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C11:migrated_schedule_3:bookable_periods",
      "record_id": "migrated_schedule_3",
      "facet": "bookable_periods",
      "value": "09:00–12:00; 13:00–16:00",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/bookable_periods",
          "source_id": "r66_78809ecbb55559e2e9b17d51575c"
        }
      ]
    },
    "native_fact_id": "C11:migrated_schedule_3:bookable_periods",
    "native_record_id": "migrated_schedule_3",
    "facet": "bookable_periods",
    "value": "09:00–12:00; 13:00–16:00",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/bookable_periods",
        "source_id": "r66_78809ecbb55559e2e9b17d51575c"
      }
    ],
    "legacy_record_id": "migrated_schedule_3"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C11-Q071 — ตารางเวลา

วันเสาร์มีรอบไหนให้จอง แล้วขอช่วงบำรุงรักษาของวันเสาร์คือเวลาใด

Applicability gap: คืน recorded fields พร้อมข้อจำกัด source และ partial; ยังไม่ยืนยันสิทธิ์จอง/เวลาเปิดจริง

ก่อน: strict=True, source_contract_pass, state=answer

```text
1. วันเสาร์มีรอบไหนให้จอง
เสาร์ — ช่วงจองเล่น: ไม่มี / None [S1]

2. ช่วงบำรุงรักษาของวันเสาร์คือเวลาใด
เสาร์ — ช่วงบำรุงรักษา: ไม่มี / None [S2]
```

หลัง: strict=False, expected_state_mismatch, state=partial

```text
1. วันเสาร์มีรอบไหนให้จอง
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
เสาร์ — ช่วงจองเล่น: ไม่มี / None [S1]

2. ช่วงบำรุงรักษาของวันเสาร์คือเวลาใด
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
เสาร์ — ช่วงบำรุงรักษา: ไม่มี / None [S2]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C11:migrated_schedule_5:bookable_periods",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C11:migrated_schedule_5:bookable_periods",
      "record_id": "migrated_schedule_5",
      "facet": "bookable_periods",
      "value": "ไม่มี / None",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/bookable_periods",
          "source_id": "r63_db5d02ff0f0f325d0884bd051b79"
        }
      ]
    },
    "native_fact_id": "C11:migrated_schedule_5:bookable_periods",
    "native_record_id": "migrated_schedule_5",
    "facet": "bookable_periods",
    "value": "ไม่มี / None",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/bookable_periods",
        "source_id": "r63_db5d02ff0f0f325d0884bd051b79"
      }
    ],
    "legacy_record_id": "migrated_schedule_5"
  },
  {
    "legacy_fact_id": "C11:migrated_schedule_5:maintenance_periods",
    "alignment_kind": "aligned",
    "legacy_expected": {
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
      ]
    },
    "native_fact_id": "C11:migrated_schedule_5:maintenance_periods",
    "native_record_id": "migrated_schedule_5",
    "facet": "maintenance_periods",
    "value": "ไม่มี / None",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/maintenance_periods",
        "source_id": "r66_3723691dd1c4cd09c3134a91d2c8"
      }
    ],
    "legacy_record_id": "migrated_schedule_5"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C11-Q072 — ตารางเวลา

ขอสอบถามหน่อยครับ ช่วงบำรุงรักษาของวันพุธคือเวลาใด แล้วขอวันพุธจองเล่นได้กี่โมงถึงกี่โมง

Applicability gap: คืน recorded fields พร้อมข้อจำกัด source และ partial; ยังไม่ยืนยันสิทธิ์จอง/เวลาเปิดจริง

ก่อน: strict=False, required_claims_missing, state=answer

```text
1. ช่วงบำรุงรักษาของวันพุธคือเวลาใด
พุธ — ช่วงบำรุงรักษา: ไม่มี / None [S1]

2. วันพุธจองเล่นได้กี่โมงถึงกี่โมง
**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: ไม่ได้เปิด 24 ชั่วโมง ตารางบริการแบ่งเป็น Morning 09:00–12:00 และ Afternoon 13:00–16:00 โดยดูตามวันดังนี้: วันจันทร์ (Monday) ช่วงเช้า 09:00–12:00 เป็น Maintenance* เล่นไม่ได้ และเปิดเล่นช่วงบ่าย 13:00–16:00; วันอังคาร-พฤหัสบดี (Tuesday-Thursday) เปิดตามรอบปกติ 09:00–12:00 และ 13:00–16:00; วันศุกร์ (Friday) เปิดช่วงเช้า 09:00–12:00 แต่ช่วงบ่าย 13:00–16:00 เป็น Maintenance** สำหรับ Weekly hardware inspection and cleaning จึงไม่ใช่ช่วงเล่น [S2]
```

หลัง: strict=False, expected_state_mismatch, state=partial

```text
1. ช่วงบำรุงรักษาของวันพุธคือเวลาใด
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
พุธ — ช่วงบำรุงรักษา: ไม่มี / None [S1]

2. วันพุธจองเล่นได้กี่โมงถึงกี่โมง
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
พุธ — ช่วงจองเล่น: 09:00–12:00; 13:00–16:00 [S2]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C11:migrated_schedule_2:maintenance_periods",
    "alignment_kind": "aligned",
    "legacy_expected": {
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
      ]
    },
    "native_fact_id": "C11:migrated_schedule_2:maintenance_periods",
    "native_record_id": "migrated_schedule_2",
    "facet": "maintenance_periods",
    "value": "ไม่มี / None",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/maintenance_periods",
        "source_id": "r66_aa6f1c71e4e35173d2c541946b8b"
      }
    ],
    "legacy_record_id": "migrated_schedule_2"
  },
  {
    "legacy_fact_id": "C11:migrated_schedule_2:bookable_periods",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C11:migrated_schedule_2:bookable_periods",
      "record_id": "migrated_schedule_2",
      "facet": "bookable_periods",
      "value": "09:00–12:00; 13:00–16:00",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/bookable_periods",
          "source_id": "r66_aa6f1c71e4e35173d2c541946b8b"
        }
      ]
    },
    "native_fact_id": "C11:migrated_schedule_2:bookable_periods",
    "native_record_id": "migrated_schedule_2",
    "facet": "bookable_periods",
    "value": "09:00–12:00; 13:00–16:00",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/bookable_periods",
        "source_id": "r66_aa6f1c71e4e35173d2c541946b8b"
      }
    ],
    "legacy_record_id": "migrated_schedule_2"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C11-Q076 — ตารางเวลา

รบกวนเช็กให้หน่อย วันพฤหัสบดีจองเล่นได้กี่โมงถึงกี่โมง แล้วขอวันพฤหัสบดีงดเล่นเพื่อ maintenance กี่โมง

Applicability gap: คืน recorded fields พร้อมข้อจำกัด source และ partial; ยังไม่ยืนยันสิทธิ์จอง/เวลาเปิดจริง

ก่อน: strict=False, required_claims_missing, state=answer

```text
1. รบกวนเช็กให้หน่อย วันพฤหัสบดีจองเล่นได้กี่โมงถึงกี่โมง
**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: ไม่ได้เปิด 24 ชั่วโมง ตารางบริการแบ่งเป็น Morning 09:00–12:00 และ Afternoon 13:00–16:00 โดยดูตามวันดังนี้: วันจันทร์ (Monday) ช่วงเช้า 09:00–12:00 เป็น Maintenance* เล่นไม่ได้ และเปิดเล่นช่วงบ่าย 13:00–16:00; วันอังคาร-พฤหัสบดี (Tuesday-Thursday) เปิดตามรอบปกติ 09:00–12:00 และ 13:00–16:00; วันศุกร์ (Friday) เปิดช่วงเช้า 09:00–12:00 แต่ช่วงบ่าย 13:00–16:00 เป็น Maintenance** สำหรับ Weekly hardware inspection and cleaning จึงไม่ใช่ช่วงเล่น [S1]

2. วันพฤหัสบดีงดเล่นเพื่อ maintenance กี่โมง
พฤหัสบดี — ช่วงบำรุงรักษา: ไม่มี / None [S2]
```

หลัง: strict=False, expected_state_mismatch, state=partial

```text
1. รบกวนเช็กให้หน่อย วันพฤหัสบดีจองเล่นได้กี่โมงถึงกี่โมง
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
พฤหัสบดี — ช่วงจองเล่น: 09:00–12:00; 13:00–16:00 [S1]

2. วันพฤหัสบดีงดเล่นเพื่อ maintenance กี่โมง
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
พฤหัสบดี — ช่วงบำรุงรักษา: ไม่มี / None [S2]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C11:migrated_schedule_3:bookable_periods",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C11:migrated_schedule_3:bookable_periods",
      "record_id": "migrated_schedule_3",
      "facet": "bookable_periods",
      "value": "09:00–12:00; 13:00–16:00",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/bookable_periods",
          "source_id": "r66_78809ecbb55559e2e9b17d51575c"
        }
      ]
    },
    "native_fact_id": "C11:migrated_schedule_3:bookable_periods",
    "native_record_id": "migrated_schedule_3",
    "facet": "bookable_periods",
    "value": "09:00–12:00; 13:00–16:00",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/bookable_periods",
        "source_id": "r66_78809ecbb55559e2e9b17d51575c"
      }
    ],
    "legacy_record_id": "migrated_schedule_3"
  },
  {
    "legacy_fact_id": "C11:migrated_schedule_3:maintenance_periods",
    "alignment_kind": "aligned",
    "legacy_expected": {
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
      ]
    },
    "native_fact_id": "C11:migrated_schedule_3:maintenance_periods",
    "native_record_id": "migrated_schedule_3",
    "facet": "maintenance_periods",
    "value": "ไม่มี / None",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/maintenance_periods",
        "source_id": "r66_78809ecbb55559e2e9b17d51575c"
      }
    ],
    "legacy_record_id": "migrated_schedule_3"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C11-Q077 — ตารางเวลา

ถามจากข้อมูลที่ศูนย์ให้ไว้ วันศุกร์งดเล่นเพื่อ maintenance กี่โมง แล้วขอถ้าไปวันศุกร์เลือกช่วงเล่นอะไรได้บ้าง

Applicability gap: คืน recorded fields พร้อมข้อจำกัด source และ partial; ยังไม่ยืนยันสิทธิ์จอง/เวลาเปิดจริง

ก่อน: strict=True, source_contract_pass, state=answer

```text
1. ถามจากข้อมูลที่ศูนย์ให้ไว้ วันศุกร์งดเล่นเพื่อ maintenance กี่โมง
ศุกร์ — ช่วงบำรุงรักษา: 13:00–16:00 [S1]

2. ถ้าไปวันศุกร์เลือกช่วงเล่นอะไรได้บ้าง
ศุกร์ — ช่วงจองเล่น: 09:00–12:00 [S2]
```

หลัง: strict=False, expected_state_mismatch, state=partial

```text
1. ถามจากข้อมูลที่ศูนย์ให้ไว้ วันศุกร์งดเล่นเพื่อ maintenance กี่โมง
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
ศุกร์ — ช่วงบำรุงรักษา: 13:00–16:00 [S1]

2. ถ้าไปวันศุกร์เลือกช่วงเล่นอะไรได้บ้าง
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
ศุกร์ — ช่วงจองเล่น: 09:00–12:00 [S2]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C11:migrated_schedule_4:maintenance_periods",
    "alignment_kind": "aligned",
    "legacy_expected": {
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
      ]
    },
    "native_fact_id": "C11:migrated_schedule_4:maintenance_periods",
    "native_record_id": "migrated_schedule_4",
    "facet": "maintenance_periods",
    "value": "13:00–16:00",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/maintenance_periods",
        "source_id": "r66_8b8799fa0b0f242ce50dede11782"
      }
    ],
    "legacy_record_id": "migrated_schedule_4"
  },
  {
    "legacy_fact_id": "C11:migrated_schedule_4:bookable_periods",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C11:migrated_schedule_4:bookable_periods",
      "record_id": "migrated_schedule_4",
      "facet": "bookable_periods",
      "value": "09:00–12:00",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/bookable_periods",
          "source_id": "r66_8b8799fa0b0f242ce50dede11782"
        }
      ]
    },
    "native_fact_id": "C11:migrated_schedule_4:bookable_periods",
    "native_record_id": "migrated_schedule_4",
    "facet": "bookable_periods",
    "value": "09:00–12:00",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/bookable_periods",
        "source_id": "r66_8b8799fa0b0f242ce50dede11782"
      }
    ],
    "legacy_record_id": "migrated_schedule_4"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C11-Q079 — ตารางเวลา

ขอสอบถามหน่อยครับ วันจันทร์จองเล่นได้กี่โมงถึงกี่โมง แล้วขอวันจันทร์งดเล่นเพื่อ maintenance กี่โมง

Applicability gap: คืน recorded fields พร้อมข้อจำกัด source และ partial; ยังไม่ยืนยันสิทธิ์จอง/เวลาเปิดจริง

ก่อน: strict=False, required_claims_missing, state=answer

```text
1. วันจันทร์จองเล่นได้กี่โมงถึงกี่โมง
**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: ไม่ได้เปิด 24 ชั่วโมง ตารางบริการแบ่งเป็น Morning 09:00–12:00 และ Afternoon 13:00–16:00 โดยดูตามวันดังนี้: วันจันทร์ (Monday) ช่วงเช้า 09:00–12:00 เป็น Maintenance* เล่นไม่ได้ และเปิดเล่นช่วงบ่าย 13:00–16:00; วันอังคาร-พฤหัสบดี (Tuesday-Thursday) เปิดตามรอบปกติ 09:00–12:00 และ 13:00–16:00; วันศุกร์ (Friday) เปิดช่วงเช้า 09:00–12:00 แต่ช่วงบ่าย 13:00–16:00 เป็น Maintenance** สำหรับ Weekly hardware inspection and cleaning จึงไม่ใช่ช่วงเล่น [S1]

2. วันจันทร์งดเล่นเพื่อ maintenance กี่โมง
จันทร์ — ช่วงบำรุงรักษา: 09:00–12:00 [S2]
```

หลัง: strict=False, expected_state_mismatch, state=partial

```text
1. วันจันทร์จองเล่นได้กี่โมงถึงกี่โมง
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
จันทร์ — ช่วงจองเล่น: 13:00–16:00 [S1]

2. วันจันทร์งดเล่นเพื่อ maintenance กี่โมง
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
จันทร์ — ช่วงบำรุงรักษา: 09:00–12:00 [S2]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C11:migrated_schedule_0:bookable_periods",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C11:migrated_schedule_0:bookable_periods",
      "record_id": "migrated_schedule_0",
      "facet": "bookable_periods",
      "value": "13:00–16:00",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/bookable_periods",
          "source_id": "r66_814dc4183099ea3715eb65d5955d"
        }
      ]
    },
    "native_fact_id": "C11:migrated_schedule_0:bookable_periods",
    "native_record_id": "migrated_schedule_0",
    "facet": "bookable_periods",
    "value": "13:00–16:00",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/bookable_periods",
        "source_id": "r66_814dc4183099ea3715eb65d5955d"
      }
    ],
    "legacy_record_id": "migrated_schedule_0"
  },
  {
    "legacy_fact_id": "C11:migrated_schedule_0:maintenance_periods",
    "alignment_kind": "aligned",
    "legacy_expected": {
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
      ]
    },
    "native_fact_id": "C11:migrated_schedule_0:maintenance_periods",
    "native_record_id": "migrated_schedule_0",
    "facet": "maintenance_periods",
    "value": "09:00–12:00",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/maintenance_periods",
        "source_id": "r66_814dc4183099ea3715eb65d5955d"
      }
    ],
    "legacy_record_id": "migrated_schedule_0"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C11-Q080 — ตารางเวลา

ช่วยตอบสั้น ๆ ว่า วันอาทิตย์มีรอบไหนให้จอง แล้วขอช่วงบำรุงรักษาของวันอาทิตย์คือเวลาใด

Applicability gap: คืน recorded fields พร้อมข้อจำกัด source และ partial; ยังไม่ยืนยันสิทธิ์จอง/เวลาเปิดจริง

ก่อน: strict=True, source_contract_pass, state=answer

```text
1. ช่วยตอบสั้น ๆ ว่า วันอาทิตย์มีรอบไหนให้จอง
อาทิตย์ — ช่วงจองเล่น: ไม่มี / None [S1]

2. ช่วงบำรุงรักษาของวันอาทิตย์คือเวลาใด
อาทิตย์ — ช่วงบำรุงรักษา: ไม่มี / None [S2]
```

หลัง: strict=False, expected_state_mismatch, state=partial

```text
1. ช่วยตอบสั้น ๆ ว่า วันอาทิตย์มีรอบไหนให้จอง
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
อาทิตย์ — ช่วงจองเล่น: ไม่มี / None [S1]

2. ช่วงบำรุงรักษาของวันอาทิตย์คือเวลาใด
ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)
อาทิตย์ — ช่วงบำรุงรักษา: ไม่มี / None [S2]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C11:migrated_schedule_6:bookable_periods",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C11:migrated_schedule_6:bookable_periods",
      "record_id": "migrated_schedule_6",
      "facet": "bookable_periods",
      "value": "ไม่มี / None",
      "numeric": null,
      "evidence_refs": [
        {
          "locator": "/mapped_fields/bookable_periods",
          "source_id": "r63_0b8c029e53f349f494c5d60c130c"
        }
      ]
    },
    "native_fact_id": "C11:migrated_schedule_6:bookable_periods",
    "native_record_id": "migrated_schedule_6",
    "facet": "bookable_periods",
    "value": "ไม่มี / None",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/bookable_periods",
        "source_id": "r63_0b8c029e53f349f494c5d60c130c"
      }
    ],
    "legacy_record_id": "migrated_schedule_6"
  },
  {
    "legacy_fact_id": "C11:migrated_schedule_6:maintenance_periods",
    "alignment_kind": "aligned",
    "legacy_expected": {
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
      ]
    },
    "native_fact_id": "C11:migrated_schedule_6:maintenance_periods",
    "native_record_id": "migrated_schedule_6",
    "facet": "maintenance_periods",
    "value": "ไม่มี / None",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/mapped_fields/maintenance_periods",
        "source_id": "r66_091dff62944f36ea9ad9068a5c8b"
      }
    ],
    "legacy_record_id": "migrated_schedule_6"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q001 — สถานะจองสด

Cockpit #01 / 2026-10-21 10:00 ว่างอยู่ไหม

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_cockpit_01_1:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_cockpit_01_1:live_status",
      "record_id": "resource_cockpit_01_1",
      "facet": "live_status",
      "value": "ถูกจอง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_cockpit_01/1"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_cockpit_01_1:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q002 — สถานะจองสด

ขอสอบถามหน่อยครับ ช่วยเช็กว่าจอง PC #05 / 2026-10-21 12:00 ได้หรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_05_3:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_05_3:live_status",
      "record_id": "resource_pc_05_3",
      "facet": "live_status",
      "value": "ข้อมูลเก่า ยืนยันสถานะไม่ได้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_05/3"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_05_3:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q003 — สถานะจองสด

ช่วยตอบสั้น ๆ ว่า อยากรู้ว่า PC #01 / 2026-10-21 10:00 ถูกจองหรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_01_1:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_01_1:live_status",
      "record_id": "resource_pc_01_1",
      "facet": "live_status",
      "value": "ถูกจอง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_01/1"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_01_1:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q004 — สถานะจองสด

อยากรู้ว่า PC #03 / 2026-10-21 09:00 ว่างอยู่ไหม

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_03_0:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_03_0:live_status",
      "record_id": "resource_pc_03_0",
      "facet": "live_status",
      "value": "ว่าง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_03/0"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_03_0:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q005 — สถานะจองสด

กำลังวางแผนไปใช้บริการ เลยขอถามว่า ช่วยเช็กว่าจอง PC #09 / 2026-10-21 09:00 ได้หรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=answer

```text
PC #09 — ที่ตั้ง: PC Zone [S1]
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_09_0:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_09_0:live_status",
      "record_id": "resource_pc_09_0",
      "facet": "live_status",
      "value": "ว่าง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_09/0"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_09_0:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q006 — สถานะจองสด

รบกวนเช็กให้หน่อย อยากรู้ว่า PlayStation 5 #02 / 2026-10-21 11:00 ถูกจองหรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_ps5_02_2:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_ps5_02_2:live_status",
      "record_id": "resource_ps5_02_2",
      "facet": "live_status",
      "value": "ตรวจสถานะไม่ได้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_ps5_02/2"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_ps5_02_2:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q007 — สถานะจองสด

ถามจากข้อมูลที่ศูนย์ให้ไว้ PC #07 / 2026-10-21 12:00 ว่างอยู่ไหม

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_07_3:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_07_3:live_status",
      "record_id": "resource_pc_07_3",
      "facet": "live_status",
      "value": "ข้อมูลเก่า ยืนยันสถานะไม่ได้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_07/3"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_07_3:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q008 — สถานะจองสด

ช่วยเช็กว่าจอง PC #10 / 2026-10-21 12:00 ได้หรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_10_3:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_10_3:live_status",
      "record_id": "resource_pc_10_3",
      "facet": "live_status",
      "value": "ข้อมูลเก่า ยืนยันสถานะไม่ได้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_10/3"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_10_3:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q009 — สถานะจองสด

ขอสอบถามหน่อยครับ อยากรู้ว่า PlayStation 5 #01 / 2026-10-21 09:00 ถูกจองหรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_ps5_01_0:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_ps5_01_0:live_status",
      "record_id": "resource_ps5_01_0",
      "facet": "live_status",
      "value": "ว่าง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_ps5_01/0"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_ps5_01_0:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q010 — สถานะจองสด

ช่วยตอบสั้น ๆ ว่า PC #01 / 2026-10-21 11:00 ว่างอยู่ไหม

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_01_2:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_01_2:live_status",
      "record_id": "resource_pc_01_2",
      "facet": "live_status",
      "value": "ตรวจสถานะไม่ได้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_01/2"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_01_2:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q011 — สถานะจองสด

อยากรู้ว่า ช่วยเช็กว่าจอง PC #06 / 2026-10-21 09:00 ได้หรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=answer

```text
PC #06 — ที่ตั้ง: PC Zone [S1]
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_06_0:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_06_0:live_status",
      "record_id": "resource_pc_06_0",
      "facet": "live_status",
      "value": "ว่าง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_06/0"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_06_0:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q012 — สถานะจองสด

กำลังวางแผนไปใช้บริการ เลยขอถามว่า อยากรู้ว่า PlayStation 5 #02 / 2026-10-21 12:00 ถูกจองหรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_ps5_02_3:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_ps5_02_3:live_status",
      "record_id": "resource_ps5_02_3",
      "facet": "live_status",
      "value": "ข้อมูลเก่า ยืนยันสถานะไม่ได้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_ps5_02/3"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_ps5_02_3:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q013 — สถานะจองสด

รบกวนเช็กให้หน่อย Cockpit #02 / 2026-10-21 10:00 ว่างอยู่ไหม

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_cockpit_02_1:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_cockpit_02_1:live_status",
      "record_id": "resource_cockpit_02_1",
      "facet": "live_status",
      "value": "ถูกจอง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_cockpit_02/1"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_cockpit_02_1:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q014 — สถานะจองสด

ถามจากข้อมูลที่ศูนย์ให้ไว้ ช่วยเช็กว่าจอง PlayStation 5 #01 / 2026-10-21 12:00 ได้หรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=answer

```text
PlayStation 5 #01 — ที่ตั้ง: PlayStation 5 Zone [S1]
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_ps5_01_3:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_ps5_01_3:live_status",
      "record_id": "resource_ps5_01_3",
      "facet": "live_status",
      "value": "ข้อมูลเก่า ยืนยันสถานะไม่ได้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_ps5_01/3"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_ps5_01_3:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q015 — สถานะจองสด

อยากรู้ว่า PC #08 / 2026-10-21 09:00 ถูกจองหรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_08_0:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_08_0:live_status",
      "record_id": "resource_pc_08_0",
      "facet": "live_status",
      "value": "ว่าง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_08/0"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_08_0:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q016 — สถานะจองสด

ขอสอบถามหน่อยครับ PlayStation 5 #02 / 2026-10-21 09:00 ว่างอยู่ไหม

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_ps5_02_0:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_ps5_02_0:live_status",
      "record_id": "resource_ps5_02_0",
      "facet": "live_status",
      "value": "ว่าง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_ps5_02/0"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_ps5_02_0:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q017 — สถานะจองสด

ช่วยตอบสั้น ๆ ว่า ช่วยเช็กว่าจอง PC #08 / 2026-10-21 11:00 ได้หรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=answer

```text
PC #08 — ที่ตั้ง: PC Zone [S1]
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_08_2:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_08_2:live_status",
      "record_id": "resource_pc_08_2",
      "facet": "live_status",
      "value": "ตรวจสถานะไม่ได้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_08/2"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_08_2:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q018 — สถานะจองสด

อยากรู้ว่า อยากรู้ว่า PC #09 / 2026-10-21 10:00 ถูกจองหรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_09_1:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_09_1:live_status",
      "record_id": "resource_pc_09_1",
      "facet": "live_status",
      "value": "ถูกจอง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_09/1"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_09_1:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q019 — สถานะจองสด

กำลังวางแผนไปใช้บริการ เลยขอถามว่า Cockpit #02 / 2026-10-21 09:00 ว่างอยู่ไหม

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_cockpit_02_0:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_cockpit_02_0:live_status",
      "record_id": "resource_cockpit_02_0",
      "facet": "live_status",
      "value": "ว่าง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_cockpit_02/0"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_cockpit_02_0:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q020 — สถานะจองสด

รบกวนเช็กให้หน่อย ช่วยเช็กว่าจอง Cockpit #01 / 2026-10-21 09:00 ได้หรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=answer

```text
Cockpit #01 — ที่ตั้ง: Cockpit Zone [S1]
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_cockpit_01_0:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_cockpit_01_0:live_status",
      "record_id": "resource_cockpit_01_0",
      "facet": "live_status",
      "value": "ว่าง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_cockpit_01/0"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_cockpit_01_0:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q021 — สถานะจองสด

ถามจากข้อมูลที่ศูนย์ให้ไว้ อยากรู้ว่า PC #04 / 2026-10-21 11:00 ถูกจองหรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_04_2:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_04_2:live_status",
      "record_id": "resource_pc_04_2",
      "facet": "live_status",
      "value": "ตรวจสถานะไม่ได้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_04/2"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_04_2:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q022 — สถานะจองสด

PlayStation 5 #01 / 2026-10-21 11:00 ว่างอยู่ไหม

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_ps5_01_2:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_ps5_01_2:live_status",
      "record_id": "resource_ps5_01_2",
      "facet": "live_status",
      "value": "ตรวจสถานะไม่ได้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_ps5_01/2"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_ps5_01_2:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q023 — สถานะจองสด

ขอสอบถามหน่อยครับ ช่วยเช็กว่าจอง PC #04 / 2026-10-21 12:00 ได้หรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_04_3:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_04_3:live_status",
      "record_id": "resource_pc_04_3",
      "facet": "live_status",
      "value": "ข้อมูลเก่า ยืนยันสถานะไม่ได้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_04/3"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_04_3:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q024 — สถานะจองสด

ช่วยตอบสั้น ๆ ว่า อยากรู้ว่า PC #01 / 2026-10-21 12:00 ถูกจองหรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_01_3:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_01_3:live_status",
      "record_id": "resource_pc_01_3",
      "facet": "live_status",
      "value": "ข้อมูลเก่า ยืนยันสถานะไม่ได้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_01/3"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_01_3:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q025 — สถานะจองสด

อยากรู้ว่า PC #01 / 2026-10-21 09:00 ว่างอยู่ไหม

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_01_0:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_01_0:live_status",
      "record_id": "resource_pc_01_0",
      "facet": "live_status",
      "value": "ว่าง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_01/0"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_01_0:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q026 — สถานะจองสด

กำลังวางแผนไปใช้บริการ เลยขอถามว่า ช่วยเช็กว่าจอง PC #03 / 2026-10-21 12:00 ได้หรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=answer

```text
PC #03 — ที่ตั้ง: PC Zone [S1]
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_03_3:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_03_3:live_status",
      "record_id": "resource_pc_03_3",
      "facet": "live_status",
      "value": "ข้อมูลเก่า ยืนยันสถานะไม่ได้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_03/3"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_03_3:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q027 — สถานะจองสด

รบกวนเช็กให้หน่อย อยากรู้ว่า PC #02 / 2026-10-21 12:00 ถูกจองหรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_02_3:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_02_3:live_status",
      "record_id": "resource_pc_02_3",
      "facet": "live_status",
      "value": "ข้อมูลเก่า ยืนยันสถานะไม่ได้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_02/3"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_02_3:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q028 — สถานะจองสด

ถามจากข้อมูลที่ศูนย์ให้ไว้ PC #10 / 2026-10-21 09:00 ว่างอยู่ไหม

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_10_0:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_10_0:live_status",
      "record_id": "resource_pc_10_0",
      "facet": "live_status",
      "value": "ว่าง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_10/0"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_10_0:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q029 — สถานะจองสด

ช่วยเช็กว่าจอง PC #05 / 2026-10-21 10:00 ได้หรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=answer

```text
PC #05 — ที่ตั้ง: PC Zone [S1]
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_05_1:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_05_1:live_status",
      "record_id": "resource_pc_05_1",
      "facet": "live_status",
      "value": "ถูกจอง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_05/1"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_05_1:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q030 — สถานะจองสด

ขอสอบถามหน่อยครับ อยากรู้ว่า PC #02 / 2026-10-21 10:00 ถูกจองหรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_02_1:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_02_1:live_status",
      "record_id": "resource_pc_02_1",
      "facet": "live_status",
      "value": "ถูกจอง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_02/1"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_02_1:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q031 — สถานะจองสด

ช่วยตอบสั้น ๆ ว่า PC #09 / 2026-10-21 11:00 ว่างอยู่ไหม

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_09_2:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_09_2:live_status",
      "record_id": "resource_pc_09_2",
      "facet": "live_status",
      "value": "ตรวจสถานะไม่ได้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_09/2"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_09_2:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q032 — สถานะจองสด

อยากรู้ว่า ช่วยเช็กว่าจอง PC #07 / 2026-10-21 09:00 ได้หรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=answer

```text
PC #07 — ที่ตั้ง: PC Zone [S1]
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_07_0:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_07_0:live_status",
      "record_id": "resource_pc_07_0",
      "facet": "live_status",
      "value": "ว่าง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_07/0"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_07_0:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q033 — สถานะจองสด

กำลังวางแผนไปใช้บริการ เลยขอถามว่า อยากรู้ว่า PlayStation 5 #02 / 2026-10-21 10:00 ถูกจองหรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_ps5_02_1:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_ps5_02_1:live_status",
      "record_id": "resource_ps5_02_1",
      "facet": "live_status",
      "value": "ถูกจอง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_ps5_02/1"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_ps5_02_1:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q034 — สถานะจองสด

รบกวนเช็กให้หน่อย PC #10 / 2026-10-21 11:00 ว่างอยู่ไหม

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_10_2:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_10_2:live_status",
      "record_id": "resource_pc_10_2",
      "facet": "live_status",
      "value": "ตรวจสถานะไม่ได้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_10/2"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_10_2:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q035 — สถานะจองสด

ถามจากข้อมูลที่ศูนย์ให้ไว้ ช่วยเช็กว่าจอง Cockpit #02 / 2026-10-21 12:00 ได้หรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=answer

```text
Cockpit #02 — ที่ตั้ง: Cockpit Zone [S1]
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_cockpit_02_3:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_cockpit_02_3:live_status",
      "record_id": "resource_cockpit_02_3",
      "facet": "live_status",
      "value": "ข้อมูลเก่า ยืนยันสถานะไม่ได้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_cockpit_02/3"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_cockpit_02_3:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q036 — สถานะจองสด

อยากรู้ว่า PC #09 / 2026-10-21 12:00 ถูกจองหรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_09_3:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_09_3:live_status",
      "record_id": "resource_pc_09_3",
      "facet": "live_status",
      "value": "ข้อมูลเก่า ยืนยันสถานะไม่ได้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_09/3"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_09_3:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q037 — สถานะจองสด

ขอสอบถามหน่อยครับ PC #10 / 2026-10-21 10:00 ว่างอยู่ไหม

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_10_1:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_10_1:live_status",
      "record_id": "resource_pc_10_1",
      "facet": "live_status",
      "value": "ถูกจอง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_10/1"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_10_1:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q038 — สถานะจองสด

ช่วยตอบสั้น ๆ ว่า ช่วยเช็กว่าจอง Cockpit #01 / 2026-10-21 11:00 ได้หรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=answer

```text
Cockpit #01 — ที่ตั้ง: Cockpit Zone [S1]
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_cockpit_01_2:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_cockpit_01_2:live_status",
      "record_id": "resource_cockpit_01_2",
      "facet": "live_status",
      "value": "ตรวจสถานะไม่ได้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_cockpit_01/2"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_cockpit_01_2:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q039 — สถานะจองสด

อยากรู้ว่า อยากรู้ว่า PC #08 / 2026-10-21 10:00 ถูกจองหรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_08_1:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_08_1:live_status",
      "record_id": "resource_pc_08_1",
      "facet": "live_status",
      "value": "ถูกจอง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_08/1"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_08_1:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q040 — สถานะจองสด

กำลังวางแผนไปใช้บริการ เลยขอถามว่า PC #02 / 2026-10-21 11:00 ว่างอยู่ไหม

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_02_2:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_02_2:live_status",
      "record_id": "resource_pc_02_2",
      "facet": "live_status",
      "value": "ตรวจสถานะไม่ได้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_02/2"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_02_2:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q041 — สถานะจองสด

รบกวนเช็กให้หน่อย ช่วยเช็กว่าจอง PC #02 / 2026-10-21 09:00 ได้หรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=answer

```text
PC #02 — ที่ตั้ง: PC Zone [S1]
PC #02 — จำนวนคนเล่นพร้อมกัน: 1 [S2]
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_02_0:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_02_0:live_status",
      "record_id": "resource_pc_02_0",
      "facet": "live_status",
      "value": "ว่าง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_02/0"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_02_0:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q042 — สถานะจองสด

ถามจากข้อมูลที่ศูนย์ให้ไว้ อยากรู้ว่า Cockpit #01 / 2026-10-21 12:00 ถูกจองหรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_cockpit_01_3:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_cockpit_01_3:live_status",
      "record_id": "resource_cockpit_01_3",
      "facet": "live_status",
      "value": "ข้อมูลเก่า ยืนยันสถานะไม่ได้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_cockpit_01/3"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_cockpit_01_3:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q043 — สถานะจองสด

PC #08 / 2026-10-21 12:00 ว่างอยู่ไหม

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_08_3:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_08_3:live_status",
      "record_id": "resource_pc_08_3",
      "facet": "live_status",
      "value": "ข้อมูลเก่า ยืนยันสถานะไม่ได้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_08/3"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_08_3:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q044 — สถานะจองสด

ขอสอบถามหน่อยครับ ช่วยเช็กว่าจอง PC #06 / 2026-10-21 11:00 ได้หรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=answer

```text
PC #06 — ที่ตั้ง: PC Zone [S1]
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_06_2:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_06_2:live_status",
      "record_id": "resource_pc_06_2",
      "facet": "live_status",
      "value": "ตรวจสถานะไม่ได้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_06/2"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_06_2:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q045 — สถานะจองสด

ช่วยตอบสั้น ๆ ว่า อยากรู้ว่า PC #04 / 2026-10-21 10:00 ถูกจองหรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_04_1:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_04_1:live_status",
      "record_id": "resource_pc_04_1",
      "facet": "live_status",
      "value": "ถูกจอง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_04/1"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_04_1:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q046 — สถานะจองสด

อยากรู้ว่า PC #04 / 2026-10-21 09:00 ว่างอยู่ไหม

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_04_0:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_04_0:live_status",
      "record_id": "resource_pc_04_0",
      "facet": "live_status",
      "value": "ว่าง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_04/0"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_04_0:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q047 — สถานะจองสด

กำลังวางแผนไปใช้บริการ เลยขอถามว่า ช่วยเช็กว่าจอง PC #07 / 2026-10-21 10:00 ได้หรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=answer

```text
PC #07 — ที่ตั้ง: PC Zone [S1]
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_07_1:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_07_1:live_status",
      "record_id": "resource_pc_07_1",
      "facet": "live_status",
      "value": "ถูกจอง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_07/1"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_07_1:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q048 — สถานะจองสด

รบกวนเช็กให้หน่อย อยากรู้ว่า PC #03 / 2026-10-21 11:00 ถูกจองหรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_03_2:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_03_2:live_status",
      "record_id": "resource_pc_03_2",
      "facet": "live_status",
      "value": "ตรวจสถานะไม่ได้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_03/2"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_03_2:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q049 — สถานะจองสด

ถามจากข้อมูลที่ศูนย์ให้ไว้ PC #05 / 2026-10-21 11:00 ว่างอยู่ไหม

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_05_2:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_05_2:live_status",
      "record_id": "resource_pc_05_2",
      "facet": "live_status",
      "value": "ตรวจสถานะไม่ได้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_05/2"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_05_2:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q050 — สถานะจองสด

ช่วยเช็กว่าจอง PC #05 / 2026-10-21 09:00 ได้หรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=answer

```text
PC #05 — ที่ตั้ง: PC Zone [S1]
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_05_0:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_05_0:live_status",
      "record_id": "resource_pc_05_0",
      "facet": "live_status",
      "value": "ว่าง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_05/0"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_05_0:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q051 — สถานะจองสด

Is PC #06 / 2026-10-21 12:00 available?

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=unavailable

```text
No confirmed live binding is available, so occupancy cannot be checked.
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
No confirmed live binding is available, so occupancy cannot be checked.
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_06_3:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_06_3:live_status",
      "record_id": "resource_pc_06_3",
      "facet": "live_status",
      "value": "Stale data; occupancy is not confirmed",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_06/3"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_06_3:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q052 — สถานะจองสด

Could you help me with this: Can you check whether PC #03 / 2026-10-21 10:00 is already booked?

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=unavailable

```text
No confirmed live binding is available, so occupancy cannot be checked.
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
No confirmed live binding is available, so occupancy cannot be checked.
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_03_1:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_03_1:live_status",
      "record_id": "resource_pc_03_1",
      "facet": "live_status",
      "value": "Booked",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_03/1"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_03_1:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q053 — สถานะจองสด

Please answer briefly: Is Cockpit #02 / 2026-10-21 11:00 available?

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=unavailable

```text
No confirmed live binding is available, so occupancy cannot be checked.
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
No confirmed live binding is available, so occupancy cannot be checked.
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_cockpit_02_2:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_cockpit_02_2:live_status",
      "record_id": "resource_cockpit_02_2",
      "facet": "live_status",
      "value": "Provider unavailable; occupancy is not confirmed",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_cockpit_02/2"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_cockpit_02_2:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q054 — สถานะจองสด

I would like to know: Can you check whether PlayStation 5 #01 / 2026-10-21 10:00 is already booked?

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=unavailable

```text
No confirmed live binding is available, so occupancy cannot be checked.
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
No confirmed live binding is available, so occupancy cannot be checked.
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_ps5_01_1:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_ps5_01_1:live_status",
      "record_id": "resource_ps5_01_1",
      "facet": "live_status",
      "value": "Booked",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_ps5_01/1"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_ps5_01_1:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q055 — สถานะจองสด

Based on the studio sources, Is PC #07 / 2026-10-21 11:00 available?

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=unavailable

```text
No confirmed live binding is available, so occupancy cannot be checked.
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
No confirmed live binding is available, so occupancy cannot be checked.
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_07_2:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_07_2:live_status",
      "record_id": "resource_pc_07_2",
      "facet": "live_status",
      "value": "Provider unavailable; occupancy is not confirmed",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_07/2"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_07_2:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q056 — สถานะจองสด

Can you check whether PC #06 / 2026-10-21 10:00 is already booked?

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=unavailable

```text
No confirmed live binding is available, so occupancy cannot be checked.
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
No confirmed live binding is available, so occupancy cannot be checked.
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_06_1:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_06_1:live_status",
      "record_id": "resource_pc_06_1",
      "facet": "live_status",
      "value": "Booked",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_06/1"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_06_1:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q057 — สถานะจองสด

Could you help me with this: Is Cockpit #01 / 2026-10-21 10:00 available?

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=unavailable

```text
No confirmed live binding is available, so occupancy cannot be checked.
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
No confirmed live binding is available, so occupancy cannot be checked.
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_cockpit_01_1:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_cockpit_01_1:live_status",
      "record_id": "resource_cockpit_01_1",
      "facet": "live_status",
      "value": "Booked",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_cockpit_01/1"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_cockpit_01_1:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q058 — สถานะจองสด

Please answer briefly: Can you check whether PC #05 / 2026-10-21 12:00 is already booked?

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=unavailable

```text
No confirmed live binding is available, so occupancy cannot be checked.
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
No confirmed live binding is available, so occupancy cannot be checked.
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_05_3:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_05_3:live_status",
      "record_id": "resource_pc_05_3",
      "facet": "live_status",
      "value": "Stale data; occupancy is not confirmed",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_05/3"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_05_3:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q059 — สถานะจองสด

I would like to know: Is PC #01 / 2026-10-21 10:00 available?

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=unavailable

```text
No confirmed live binding is available, so occupancy cannot be checked.
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
No confirmed live binding is available, so occupancy cannot be checked.
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_01_1:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_01_1:live_status",
      "record_id": "resource_pc_01_1",
      "facet": "live_status",
      "value": "Booked",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_01/1"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_01_1:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q060 — สถานะจองสด

Based on the studio sources, Can you check whether PC #03 / 2026-10-21 09:00 is already booked?

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=unavailable

```text
No confirmed live binding is available, so occupancy cannot be checked.
```

หลัง: strict=False, fixture_not_in_native_source, state=unavailable

```text
No confirmed live binding is available, so occupancy cannot be checked.
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_03_0:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_03_0:live_status",
      "record_id": "resource_pc_03_0",
      "facet": "live_status",
      "value": "Available",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_03/0"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_03_0:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q061 — สถานะจองสด

Is PC #09 / 2026-10-21 09:00 available? and also Can you check whether PC #10 / 2026-10-21 12:00 is already booked?

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=partial

```text
1. is pc #09 / 2026-10-21 09:00 available
No confirmed live binding is available, so occupancy cannot be checked.

2. can you check whether pc #10 / 2026-10-21 12:00 is already booked
No confirmed live binding is available, so occupancy cannot be checked.
```

หลัง: strict=False, fixture_not_in_native_source, state=partial

```text
1. is pc #09 / 2026-10-21 09:00 available
No confirmed live binding is available, so occupancy cannot be checked.

2. can you check whether pc #10 / 2026-10-21 12:00 is already booked
No confirmed live binding is available, so occupancy cannot be checked.
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_09_0:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_09_0:live_status",
      "record_id": "resource_pc_09_0",
      "facet": "live_status",
      "value": "Available",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_09/0"
        }
      ]
    }
  },
  {
    "legacy_fact_id": "C12:resource_pc_10_3:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_10_3:live_status",
      "record_id": "resource_pc_10_3",
      "facet": "live_status",
      "value": "Stale data; occupancy is not confirmed",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_10/3"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_09_0:live_status",
    "C12:resource_pc_10_3:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q062 — สถานะจองสด

Could you help me with this: Can you check whether PlayStation 5 #02 / 2026-10-21 11:00 is already booked? and also Is PlayStation 5 #01 / 2026-10-21 09:00 available?

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=partial

```text
1. can you check whether ps5 #02 / 2026-10-21 11:00 is already booked
No confirmed live binding is available, so occupancy cannot be checked.

2. is ps5 #01 / 2026-10-21 09:00 available
No confirmed live binding is available, so occupancy cannot be checked.
```

หลัง: strict=False, fixture_not_in_native_source, state=partial

```text
1. can you check whether ps5 #02 / 2026-10-21 11:00 is already booked
No confirmed live binding is available, so occupancy cannot be checked.

2. is ps5 #01 / 2026-10-21 09:00 available
No confirmed live binding is available, so occupancy cannot be checked.
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_ps5_02_2:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_ps5_02_2:live_status",
      "record_id": "resource_ps5_02_2",
      "facet": "live_status",
      "value": "Provider unavailable; occupancy is not confirmed",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_ps5_02/2"
        }
      ]
    }
  },
  {
    "legacy_fact_id": "C12:resource_ps5_01_0:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_ps5_01_0:live_status",
      "record_id": "resource_ps5_01_0",
      "facet": "live_status",
      "value": "Available",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_ps5_01/0"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_ps5_02_2:live_status",
    "C12:resource_ps5_01_0:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q063 — สถานะจองสด

Please answer briefly: Is PC #07 / 2026-10-21 12:00 available? and also Can you check whether PC #01 / 2026-10-21 11:00 is already booked?

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=partial

```text
1. please answer briefly: is pc #07 / 2026-10-21 12:00 available
No confirmed live binding is available, so occupancy cannot be checked.

2. can you check whether pc #01 / 2026-10-21 11:00 is already booked
No confirmed live binding is available, so occupancy cannot be checked.
```

หลัง: strict=False, fixture_not_in_native_source, state=partial

```text
1. please answer briefly: is pc #07 / 2026-10-21 12:00 available
No confirmed live binding is available, so occupancy cannot be checked.

2. can you check whether pc #01 / 2026-10-21 11:00 is already booked
No confirmed live binding is available, so occupancy cannot be checked.
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_07_3:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_07_3:live_status",
      "record_id": "resource_pc_07_3",
      "facet": "live_status",
      "value": "Stale data; occupancy is not confirmed",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_07/3"
        }
      ]
    }
  },
  {
    "legacy_fact_id": "C12:resource_pc_01_2:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_01_2:live_status",
      "record_id": "resource_pc_01_2",
      "facet": "live_status",
      "value": "Provider unavailable; occupancy is not confirmed",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_01/2"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_07_3:live_status",
    "C12:resource_pc_01_2:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q064 — สถานะจองสด

I would like to know: Can you check whether PC #10 / 2026-10-21 12:00 is already booked? and also Is PC #06 / 2026-10-21 09:00 available?

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=partial

```text
1. can you check whether pc #10 / 2026-10-21 12:00 is already booked
No confirmed live binding is available, so occupancy cannot be checked.

2. is pc #06 / 2026-10-21 09:00 available
No confirmed live binding is available, so occupancy cannot be checked.
```

หลัง: strict=False, fixture_not_in_native_source, state=partial

```text
1. can you check whether pc #10 / 2026-10-21 12:00 is already booked
No confirmed live binding is available, so occupancy cannot be checked.

2. is pc #06 / 2026-10-21 09:00 available
No confirmed live binding is available, so occupancy cannot be checked.
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_10_3:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_10_3:live_status",
      "record_id": "resource_pc_10_3",
      "facet": "live_status",
      "value": "Stale data; occupancy is not confirmed",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_10/3"
        }
      ]
    }
  },
  {
    "legacy_fact_id": "C12:resource_pc_06_0:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_06_0:live_status",
      "record_id": "resource_pc_06_0",
      "facet": "live_status",
      "value": "Available",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_06/0"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_10_3:live_status",
    "C12:resource_pc_06_0:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q065 — สถานะจองสด

Based on the studio sources, Is PlayStation 5 #01 / 2026-10-21 09:00 available? and also Can you check whether PlayStation 5 #02 / 2026-10-21 12:00 is already booked?

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=partial

```text
1. based on the studio sources, is ps5 #01 / 2026-10-21 09:00 available
No confirmed live binding is available, so occupancy cannot be checked.

2. can you check whether ps5 #02 / 2026-10-21 12:00 is already booked
No confirmed live binding is available, so occupancy cannot be checked.
```

หลัง: strict=False, fixture_not_in_native_source, state=partial

```text
1. based on the studio sources, is ps5 #01 / 2026-10-21 09:00 available
No confirmed live binding is available, so occupancy cannot be checked.

2. can you check whether ps5 #02 / 2026-10-21 12:00 is already booked
No confirmed live binding is available, so occupancy cannot be checked.
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_ps5_01_0:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_ps5_01_0:live_status",
      "record_id": "resource_ps5_01_0",
      "facet": "live_status",
      "value": "Available",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_ps5_01/0"
        }
      ]
    }
  },
  {
    "legacy_fact_id": "C12:resource_ps5_02_3:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_ps5_02_3:live_status",
      "record_id": "resource_ps5_02_3",
      "facet": "live_status",
      "value": "Stale data; occupancy is not confirmed",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_ps5_02/3"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_ps5_01_0:live_status",
    "C12:resource_ps5_02_3:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q066 — สถานะจองสด

Can you check whether PC #01 / 2026-10-21 11:00 is already booked? and also Is Cockpit #02 / 2026-10-21 10:00 available?

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=partial

```text
1. can you check whether pc #01 / 2026-10-21 11:00 is already booked
No confirmed live binding is available, so occupancy cannot be checked.

2. is cockpit #02 / 2026-10-21 10:00 available
No confirmed live binding is available, so occupancy cannot be checked.
```

หลัง: strict=False, fixture_not_in_native_source, state=partial

```text
1. can you check whether pc #01 / 2026-10-21 11:00 is already booked
No confirmed live binding is available, so occupancy cannot be checked.

2. is cockpit #02 / 2026-10-21 10:00 available
No confirmed live binding is available, so occupancy cannot be checked.
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_01_2:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_01_2:live_status",
      "record_id": "resource_pc_01_2",
      "facet": "live_status",
      "value": "Provider unavailable; occupancy is not confirmed",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_01/2"
        }
      ]
    }
  },
  {
    "legacy_fact_id": "C12:resource_cockpit_02_1:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_cockpit_02_1:live_status",
      "record_id": "resource_cockpit_02_1",
      "facet": "live_status",
      "value": "Booked",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_cockpit_02/1"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_01_2:live_status",
    "C12:resource_cockpit_02_1:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q067 — สถานะจองสด

Could you help me with this: Is PC #06 / 2026-10-21 09:00 available? and also Can you check whether PlayStation 5 #01 / 2026-10-21 12:00 is already booked?

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=partial

```text
1. is pc #06 / 2026-10-21 09:00 available
No confirmed live binding is available, so occupancy cannot be checked.

2. can you check whether ps5 #01 / 2026-10-21 12:00 is already booked
No confirmed live binding is available, so occupancy cannot be checked.
```

หลัง: strict=False, fixture_not_in_native_source, state=partial

```text
1. is pc #06 / 2026-10-21 09:00 available
No confirmed live binding is available, so occupancy cannot be checked.

2. can you check whether ps5 #01 / 2026-10-21 12:00 is already booked
No confirmed live binding is available, so occupancy cannot be checked.
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_06_0:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_06_0:live_status",
      "record_id": "resource_pc_06_0",
      "facet": "live_status",
      "value": "Available",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_06/0"
        }
      ]
    }
  },
  {
    "legacy_fact_id": "C12:resource_ps5_01_3:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_ps5_01_3:live_status",
      "record_id": "resource_ps5_01_3",
      "facet": "live_status",
      "value": "Stale data; occupancy is not confirmed",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_ps5_01/3"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_06_0:live_status",
    "C12:resource_ps5_01_3:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q068 — สถานะจองสด

Please answer briefly: Can you check whether PlayStation 5 #02 / 2026-10-21 12:00 is already booked? and also Is PC #08 / 2026-10-21 09:00 available?

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=partial

```text
1. please answer briefly: can you check whether ps5 #02 / 2026-10-21 12:00 is already booked
No confirmed live binding is available, so occupancy cannot be checked.

2. is pc #08 / 2026-10-21 09:00 available
No confirmed live binding is available, so occupancy cannot be checked.
```

หลัง: strict=False, fixture_not_in_native_source, state=partial

```text
1. please answer briefly: can you check whether ps5 #02 / 2026-10-21 12:00 is already booked
No confirmed live binding is available, so occupancy cannot be checked.

2. is pc #08 / 2026-10-21 09:00 available
No confirmed live binding is available, so occupancy cannot be checked.
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_ps5_02_3:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_ps5_02_3:live_status",
      "record_id": "resource_ps5_02_3",
      "facet": "live_status",
      "value": "Stale data; occupancy is not confirmed",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_ps5_02/3"
        }
      ]
    }
  },
  {
    "legacy_fact_id": "C12:resource_pc_08_0:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_08_0:live_status",
      "record_id": "resource_pc_08_0",
      "facet": "live_status",
      "value": "Available",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_08/0"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_ps5_02_3:live_status",
    "C12:resource_pc_08_0:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q069 — สถานะจองสด

I would like to know: Is Cockpit #02 / 2026-10-21 10:00 available? and also Can you check whether PlayStation 5 #02 / 2026-10-21 09:00 is already booked?

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=partial

```text
1. is cockpit #02 / 2026-10-21 10:00 available
No confirmed live binding is available, so occupancy cannot be checked.

2. can you check whether ps5 #02 / 2026-10-21 09:00 is already booked
No confirmed live binding is available, so occupancy cannot be checked.
```

หลัง: strict=False, fixture_not_in_native_source, state=partial

```text
1. is cockpit #02 / 2026-10-21 10:00 available
No confirmed live binding is available, so occupancy cannot be checked.

2. can you check whether ps5 #02 / 2026-10-21 09:00 is already booked
No confirmed live binding is available, so occupancy cannot be checked.
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_cockpit_02_1:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_cockpit_02_1:live_status",
      "record_id": "resource_cockpit_02_1",
      "facet": "live_status",
      "value": "Booked",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_cockpit_02/1"
        }
      ]
    }
  },
  {
    "legacy_fact_id": "C12:resource_ps5_02_0:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_ps5_02_0:live_status",
      "record_id": "resource_ps5_02_0",
      "facet": "live_status",
      "value": "Available",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_ps5_02/0"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_cockpit_02_1:live_status",
    "C12:resource_ps5_02_0:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q070 — สถานะจองสด

Based on the studio sources, Can you check whether PlayStation 5 #01 / 2026-10-21 12:00 is already booked? and also Is PC #08 / 2026-10-21 11:00 available?

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=partial

```text
1. based on the studio sources, can you check whether ps5 #01 / 2026-10-21 12:00 is already booked
No confirmed live binding is available, so occupancy cannot be checked.

2. is pc #08 / 2026-10-21 11:00 available
No confirmed live binding is available, so occupancy cannot be checked.
```

หลัง: strict=False, fixture_not_in_native_source, state=partial

```text
1. based on the studio sources, can you check whether ps5 #01 / 2026-10-21 12:00 is already booked
No confirmed live binding is available, so occupancy cannot be checked.

2. is pc #08 / 2026-10-21 11:00 available
No confirmed live binding is available, so occupancy cannot be checked.
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_ps5_01_3:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_ps5_01_3:live_status",
      "record_id": "resource_ps5_01_3",
      "facet": "live_status",
      "value": "Stale data; occupancy is not confirmed",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_ps5_01/3"
        }
      ]
    }
  },
  {
    "legacy_fact_id": "C12:resource_pc_08_2:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_08_2:live_status",
      "record_id": "resource_pc_08_2",
      "facet": "live_status",
      "value": "Provider unavailable; occupancy is not confirmed",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_08/2"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_ps5_01_3:live_status",
    "C12:resource_pc_08_2:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q071 — สถานะจองสด

ช่วยเช็กว่าจอง PC #08 / 2026-10-21 09:00 ได้หรือยัง แล้วขออยากรู้ว่า PC #09 / 2026-10-21 10:00 ถูกจองหรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=partial

```text
1. ช่วยเช็กว่าจอง pc #08 / 2026-10-21 09:00 ได้หรือยัง
PC #08 — ที่ตั้ง: PC Zone [S1]

2. อยากรู้ว่า pc #09 / 2026-10-21 10:00 ถูกจองหรือยัง
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=partial

```text
1. ช่วยเช็กว่าจอง pc #08 / 2026-10-21 09:00 ได้หรือยัง
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ

2. อยากรู้ว่า pc #09 / 2026-10-21 10:00 ถูกจองหรือยัง
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_08_0:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_08_0:live_status",
      "record_id": "resource_pc_08_0",
      "facet": "live_status",
      "value": "ว่าง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_08/0"
        }
      ]
    }
  },
  {
    "legacy_fact_id": "C12:resource_pc_09_1:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_09_1:live_status",
      "record_id": "resource_pc_09_1",
      "facet": "live_status",
      "value": "ถูกจอง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_09/1"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_08_0:live_status",
    "C12:resource_pc_09_1:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q072 — สถานะจองสด

ขอสอบถามหน่อยครับ อยากรู้ว่า PlayStation 5 #02 / 2026-10-21 09:00 ถูกจองหรือยัง แล้วขอCockpit #02 / 2026-10-21 09:00 ว่างอยู่ไหม

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=partial

```text
1. อยากรู้ว่า ps5 #02 / 2026-10-21 09:00 ถูกจองหรือยัง
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ

2. cockpit #02 / 2026-10-21 09:00 ว่างอยู่ไหม
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=partial

```text
1. อยากรู้ว่า ps5 #02 / 2026-10-21 09:00 ถูกจองหรือยัง
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ

2. cockpit #02 / 2026-10-21 09:00 ว่างอยู่ไหม
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_ps5_02_0:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_ps5_02_0:live_status",
      "record_id": "resource_ps5_02_0",
      "facet": "live_status",
      "value": "ว่าง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_ps5_02/0"
        }
      ]
    }
  },
  {
    "legacy_fact_id": "C12:resource_cockpit_02_0:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_cockpit_02_0:live_status",
      "record_id": "resource_cockpit_02_0",
      "facet": "live_status",
      "value": "ว่าง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_cockpit_02/0"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_ps5_02_0:live_status",
    "C12:resource_cockpit_02_0:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q073 — สถานะจองสด

ช่วยตอบสั้น ๆ ว่า PC #08 / 2026-10-21 11:00 ว่างอยู่ไหม แล้วขอช่วยเช็กว่าจอง Cockpit #01 / 2026-10-21 09:00 ได้หรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=partial

```text
1. ช่วยตอบสั้น ๆ ว่า pc #08 / 2026-10-21 11:00 ว่างอยู่ไหม
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ

2. ช่วยเช็กว่าจอง cockpit #01 / 2026-10-21 09:00 ได้หรือยัง
Cockpit #01 — ที่ตั้ง: Cockpit Zone [S1]
```

หลัง: strict=False, fixture_not_in_native_source, state=partial

```text
1. ช่วยตอบสั้น ๆ ว่า pc #08 / 2026-10-21 11:00 ว่างอยู่ไหม
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ

2. ช่วยเช็กว่าจอง cockpit #01 / 2026-10-21 09:00 ได้หรือยัง
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_08_2:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_08_2:live_status",
      "record_id": "resource_pc_08_2",
      "facet": "live_status",
      "value": "ตรวจสถานะไม่ได้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_08/2"
        }
      ]
    }
  },
  {
    "legacy_fact_id": "C12:resource_cockpit_01_0:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_cockpit_01_0:live_status",
      "record_id": "resource_cockpit_01_0",
      "facet": "live_status",
      "value": "ว่าง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_cockpit_01/0"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_08_2:live_status",
    "C12:resource_cockpit_01_0:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q074 — สถานะจองสด

อยากรู้ว่า ช่วยเช็กว่าจอง PC #09 / 2026-10-21 10:00 ได้หรือยัง แล้วขออยากรู้ว่า PC #04 / 2026-10-21 11:00 ถูกจองหรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=partial

```text
1. อยากรู้ว่า ช่วยเช็กว่าจอง pc #09 / 2026-10-21 10:00 ได้หรือยัง
PC #09 — ที่ตั้ง: PC Zone [S1]

2. อยากรู้ว่า pc #04 / 2026-10-21 11:00 ถูกจองหรือยัง
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=partial

```text
1. อยากรู้ว่า ช่วยเช็กว่าจอง pc #09 / 2026-10-21 10:00 ได้หรือยัง
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ

2. อยากรู้ว่า pc #04 / 2026-10-21 11:00 ถูกจองหรือยัง
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_09_1:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_09_1:live_status",
      "record_id": "resource_pc_09_1",
      "facet": "live_status",
      "value": "ถูกจอง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_09/1"
        }
      ]
    }
  },
  {
    "legacy_fact_id": "C12:resource_pc_04_2:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_04_2:live_status",
      "record_id": "resource_pc_04_2",
      "facet": "live_status",
      "value": "ตรวจสถานะไม่ได้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_04/2"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_09_1:live_status",
    "C12:resource_pc_04_2:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q075 — สถานะจองสด

กำลังวางแผนไปใช้บริการ เลยขอถามว่า อยากรู้ว่า Cockpit #02 / 2026-10-21 09:00 ถูกจองหรือยัง แล้วขอPlayStation 5 #01 / 2026-10-21 11:00 ว่างอยู่ไหม

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=partial

```text
1. กำลังวางแผนไปใช้บริการ เลยขอถามว่า อยากรู้ว่า cockpit #02 / 2026-10-21 09:00 ถูกจองหรือยัง
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ

2. playstation 5 #01 / 2026-10-21 11:00 ว่างอยู่ไหม
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=partial

```text
1. กำลังวางแผนไปใช้บริการ เลยขอถามว่า อยากรู้ว่า cockpit #02 / 2026-10-21 09:00 ถูกจองหรือยัง
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ

2. playstation 5 #01 / 2026-10-21 11:00 ว่างอยู่ไหม
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_cockpit_02_0:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_cockpit_02_0:live_status",
      "record_id": "resource_cockpit_02_0",
      "facet": "live_status",
      "value": "ว่าง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_cockpit_02/0"
        }
      ]
    }
  },
  {
    "legacy_fact_id": "C12:resource_ps5_01_2:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_ps5_01_2:live_status",
      "record_id": "resource_ps5_01_2",
      "facet": "live_status",
      "value": "ตรวจสถานะไม่ได้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_ps5_01/2"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_cockpit_02_0:live_status",
    "C12:resource_ps5_01_2:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q076 — สถานะจองสด

รบกวนเช็กให้หน่อย Cockpit #01 / 2026-10-21 09:00 ว่างอยู่ไหม แล้วขอช่วยเช็กว่าจอง PC #04 / 2026-10-21 12:00 ได้หรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=partial

```text
1. รบกวนเช็กให้หน่อย cockpit #01 / 2026-10-21 09:00 ว่างอยู่ไหม
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ

2. ช่วยเช็กว่าจอง pc #04 / 2026-10-21 12:00 ได้หรือยัง
PC #04 — ที่ตั้ง: PC Zone [S1]
```

หลัง: strict=False, fixture_not_in_native_source, state=partial

```text
1. รบกวนเช็กให้หน่อย cockpit #01 / 2026-10-21 09:00 ว่างอยู่ไหม
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ

2. ช่วยเช็กว่าจอง pc #04 / 2026-10-21 12:00 ได้หรือยัง
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_cockpit_01_0:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_cockpit_01_0:live_status",
      "record_id": "resource_cockpit_01_0",
      "facet": "live_status",
      "value": "ว่าง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_cockpit_01/0"
        }
      ]
    }
  },
  {
    "legacy_fact_id": "C12:resource_pc_04_3:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_04_3:live_status",
      "record_id": "resource_pc_04_3",
      "facet": "live_status",
      "value": "ข้อมูลเก่า ยืนยันสถานะไม่ได้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_04/3"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_cockpit_01_0:live_status",
    "C12:resource_pc_04_3:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q077 — สถานะจองสด

ถามจากข้อมูลที่ศูนย์ให้ไว้ ช่วยเช็กว่าจอง PC #04 / 2026-10-21 11:00 ได้หรือยัง แล้วขออยากรู้ว่า PC #01 / 2026-10-21 12:00 ถูกจองหรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=partial

```text
1. ถามจากข้อมูลที่ศูนย์ให้ไว้ ช่วยเช็กว่าจอง pc #04 / 2026-10-21 11:00 ได้หรือยัง
PC #04 — ที่ตั้ง: PC Zone [S1]

2. อยากรู้ว่า pc #01 / 2026-10-21 12:00 ถูกจองหรือยัง
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=partial

```text
1. ถามจากข้อมูลที่ศูนย์ให้ไว้ ช่วยเช็กว่าจอง pc #04 / 2026-10-21 11:00 ได้หรือยัง
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ

2. อยากรู้ว่า pc #01 / 2026-10-21 12:00 ถูกจองหรือยัง
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_04_2:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_04_2:live_status",
      "record_id": "resource_pc_04_2",
      "facet": "live_status",
      "value": "ตรวจสถานะไม่ได้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_04/2"
        }
      ]
    }
  },
  {
    "legacy_fact_id": "C12:resource_pc_01_3:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_01_3:live_status",
      "record_id": "resource_pc_01_3",
      "facet": "live_status",
      "value": "ข้อมูลเก่า ยืนยันสถานะไม่ได้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_01/3"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_04_2:live_status",
    "C12:resource_pc_01_3:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q078 — สถานะจองสด

อยากรู้ว่า PlayStation 5 #01 / 2026-10-21 11:00 ถูกจองหรือยัง แล้วขอPC #01 / 2026-10-21 09:00 ว่างอยู่ไหม

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=partial

```text
1. อยากรู้ว่า ps5 #01 / 2026-10-21 11:00 ถูกจองหรือยัง
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ

2. pc #01 / 2026-10-21 09:00 ว่างอยู่ไหม
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=partial

```text
1. อยากรู้ว่า ps5 #01 / 2026-10-21 11:00 ถูกจองหรือยัง
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ

2. pc #01 / 2026-10-21 09:00 ว่างอยู่ไหม
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_ps5_01_2:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_ps5_01_2:live_status",
      "record_id": "resource_ps5_01_2",
      "facet": "live_status",
      "value": "ตรวจสถานะไม่ได้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_ps5_01/2"
        }
      ]
    }
  },
  {
    "legacy_fact_id": "C12:resource_pc_01_0:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_01_0:live_status",
      "record_id": "resource_pc_01_0",
      "facet": "live_status",
      "value": "ว่าง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_01/0"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_ps5_01_2:live_status",
    "C12:resource_pc_01_0:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q079 — สถานะจองสด

ขอสอบถามหน่อยครับ PC #04 / 2026-10-21 12:00 ว่างอยู่ไหม แล้วขอช่วยเช็กว่าจอง PC #03 / 2026-10-21 12:00 ได้หรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=partial

```text
1. pc #04 / 2026-10-21 12:00 ว่างอยู่ไหม
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ

2. ช่วยเช็กว่าจอง pc #03 / 2026-10-21 12:00 ได้หรือยัง
PC #03 — ที่ตั้ง: PC Zone [S1]
```

หลัง: strict=False, fixture_not_in_native_source, state=partial

```text
1. pc #04 / 2026-10-21 12:00 ว่างอยู่ไหม
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ

2. ช่วยเช็กว่าจอง pc #03 / 2026-10-21 12:00 ได้หรือยัง
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_04_3:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_04_3:live_status",
      "record_id": "resource_pc_04_3",
      "facet": "live_status",
      "value": "ข้อมูลเก่า ยืนยันสถานะไม่ได้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_04/3"
        }
      ]
    }
  },
  {
    "legacy_fact_id": "C12:resource_pc_03_3:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_03_3:live_status",
      "record_id": "resource_pc_03_3",
      "facet": "live_status",
      "value": "ข้อมูลเก่า ยืนยันสถานะไม่ได้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_03/3"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_04_3:live_status",
    "C12:resource_pc_03_3:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q080 — สถานะจองสด

ช่วยตอบสั้น ๆ ว่า ช่วยเช็กว่าจอง PC #01 / 2026-10-21 12:00 ได้หรือยัง แล้วขออยากรู้ว่า PC #02 / 2026-10-21 12:00 ถูกจองหรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=partial

```text
1. ช่วยตอบสั้น ๆ ว่า ช่วยเช็กว่าจอง pc #01 / 2026-10-21 12:00 ได้หรือยัง
PC #01 — ที่ตั้ง: PC Zone [S1]

2. อยากรู้ว่า pc #02 / 2026-10-21 12:00 ถูกจองหรือยัง
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=partial

```text
1. ช่วยตอบสั้น ๆ ว่า ช่วยเช็กว่าจอง pc #01 / 2026-10-21 12:00 ได้หรือยัง
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ

2. อยากรู้ว่า pc #02 / 2026-10-21 12:00 ถูกจองหรือยัง
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C12:resource_pc_01_3:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_01_3:live_status",
      "record_id": "resource_pc_01_3",
      "facet": "live_status",
      "value": "ข้อมูลเก่า ยืนยันสถานะไม่ได้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_01/3"
        }
      ]
    }
  },
  {
    "legacy_fact_id": "C12:resource_pc_02_3:live_status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C12:resource_pc_02_3:live_status",
      "record_id": "resource_pc_02_3",
      "facet": "live_status",
      "value": "ข้อมูลเก่า ยืนยันสถานะไม่ได้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:live_provider",
          "locator": "resource_pc_02/3"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C12:resource_pc_01_3:live_status",
    "C12:resource_pc_02_3:live_status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q083 — สถานะจองสด

ถามจากข้อมูลที่ศูนย์ให้ไว้ ช่วยยืนยันรายการจองหมายเลข SECRET-7788 ว่าจ่ายแล้วหรือยัง

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, expected_state_mismatch, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=True, source_contract_pass, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q086 — สถานะจองสด

ช่วยยืนยันรายการจองหมายเลข SECRET-7788 ว่าจ่ายแล้วหรือยัง

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, expected_state_mismatch, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=True, source_contract_pass, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q089 — สถานะจองสด

ขอสอบถามหน่อยครับ ช่วยยืนยันรายการจองหมายเลข SECRET-7788 ว่าจ่ายแล้วหรือยัง

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, expected_state_mismatch, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=True, source_contract_pass, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q092 — สถานะจองสด

ช่วยตอบสั้น ๆ ว่า ช่วยยืนยันรายการจองหมายเลข SECRET-7788 ว่าจ่ายแล้วหรือยัง

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, expected_state_mismatch, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=True, source_contract_pass, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q095 — สถานะจองสด

อยากรู้ว่า ช่วยยืนยันรายการจองหมายเลข SECRET-7788 ว่าจ่ายแล้วหรือยัง

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, expected_state_mismatch, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=True, source_contract_pass, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C12-Q098 — สถานะจองสด

กำลังวางแผนไปใช้บริการ เลยขอถามว่า ช่วยยืนยันรายการจองหมายเลข SECRET-7788 ว่าจ่ายแล้วหรือยัง

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, expected_state_mismatch, state=unavailable

```text
ยังไม่มีการเชื่อมสถานะสดที่ยืนยันได้ จึงตรวจว่าเครื่องว่างหรือไม่ไม่ได้ครับ
```

หลัง: strict=True, source_contract_pass, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C13-Q052 — กติกาการแข่งขัน

Could you help me with this: Under PSU Phuket VALORANT 2026 Tournament, what does the section ประเภทบทลงโทษในเกม specify?

Granularity/overlap: goal clauses ครบ มี source summary เพิ่ม ต้องคง strict fail และไม่เรียก actual content failure อัตโนมัติ

ก่อน: strict=False, additional_or_wrong_scope_claims, state=answer

```text
PSU Phuket VALORANT 2026 Tournament — Types of penalties in the game: Penalty types in the game [S1]
PSU Phuket VALORANT 2026 Tournament — ประเภทบทลงโทษในเกม: การตักเตือน (Warning) สำหรับความผิดครั้งแรกที่มีผลกระทบต่ำ [S2]
PSU Phuket VALORANT 2026 Tournament — ประเภทบทลงโทษในเกม: การย้อนรอบ (Round Rollback) เมื่อการใช้ช่องโหว่ส่งผลต่อรอบนั้นอย่างชัดเจนแต่ระบุเจตนาไม่ได้ [S3]
PSU Phuket VALORANT 2026 Tournament — ประเภทบทลงโทษในเกม: การปรับแพ้ในรอบ (Round Loss) เมื่อพบว่าผู้เล่นหรือทีมมีเจตนาใช้ช่องโหว่เพื่อสร้างความได้เปรียบ [S4]
PSU Phuket VALORANT 2026 Tournament — ประเภทบทลงโทษในเกม: การปรับแพ้ในแผนที่ (Map Forfeit) สำหรับความผิดร้ายแรงหรือความผิดซ้ำที่ส่งผลกระทบต่อผลการแข่งในแผนที่นั้น [S5]
PSU Phuket VALORANT 2026 Tournament — ประเภทบทลงโทษในเกม: การปรับแพ้ในแมตช์ (Match Forfeit) กรณีทุจริต (Cheating) หรือล็อกผล (Match fixing)   [S6]
PSU Phuket VALORANT 2026 Tournament — ประเภทบทลงโทษในเกม: ทางผู้จัดการแข่งขันขอสงวนสิทธิ์ในการเปลี่ยนแปลงแก้ไขกฎระเบียบโดยไม่ต้องแจ้งให้ทราบล่วงหน้า [S7]
PSU Phuket VALORANT 2026 Tournament — ประเภทบทลงโทษในเกม: -------------------------------------------------------------------------------------- [S8]
```

หลัง: strict=False, additional_or_wrong_scope_claims, state=answer

```text
A confirmed English translation is unavailable for some clauses; their Thai source text is retained below.
PSU Phuket VALORANT 2026 Tournament — Types of penalties in the game: Penalty types in the game [S1]
PSU Phuket VALORANT 2026 Tournament — ประเภทบทลงโทษในเกม: การตักเตือน (Warning) สำหรับความผิดครั้งแรกที่มีผลกระทบต่ำ [S2]
PSU Phuket VALORANT 2026 Tournament — ประเภทบทลงโทษในเกม: การย้อนรอบ (Round Rollback) เมื่อการใช้ช่องโหว่ส่งผลต่อรอบนั้นอย่างชัดเจนแต่ระบุเจตนาไม่ได้ [S3]
PSU Phuket VALORANT 2026 Tournament — ประเภทบทลงโทษในเกม: การปรับแพ้ในรอบ (Round Loss) เมื่อพบว่าผู้เล่นหรือทีมมีเจตนาใช้ช่องโหว่เพื่อสร้างความได้เปรียบ [S4]
PSU Phuket VALORANT 2026 Tournament — ประเภทบทลงโทษในเกม: การปรับแพ้ในแผนที่ (Map Forfeit) สำหรับความผิดร้ายแรงหรือความผิดซ้ำที่ส่งผลกระทบต่อผลการแข่งในแผนที่นั้น [S5]
PSU Phuket VALORANT 2026 Tournament — ประเภทบทลงโทษในเกม: การปรับแพ้ในแมตช์ (Match Forfeit) กรณีทุจริต (Cheating) หรือล็อกผล (Match fixing)   [S6]
PSU Phuket VALORANT 2026 Tournament — ประเภทบทลงโทษในเกม: ทางผู้จัดการแข่งขันขอสงวนสิทธิ์ในการเปลี่ยนแปลงแก้ไขกฎระเบียบโดยไม่ต้องแจ้งให้ทราบล่วงหน้า [S7]
PSU Phuket VALORANT 2026 Tournament — ประเภทบทลงโทษในเกม: -------------------------------------------------------------------------------------- [S8]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C13:valorant_76:rule_clause",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C13:valorant_76:rule_clause",
      "record_id": "valorant_76",
      "facet": "rule_clause",
      "value": "การปรับแพ้ในแผนที่ (Map Forfeit) สำหรับความผิดร้ายแรงหรือความผิดซ้ำที่ส่งผลกระทบต่อผลการแข่งในแผนที่นั้น",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "doc108:valorant",
          "locator": "document.xml/paragraph[76]",
          "source_sha256": "a824f58e0fb4dcd1db4ea1097fd02e4d6f5d147822d88dc36a69db5518dbf8d7"
        }
      ]
    },
    "native_fact_id": "C13:r114_valorant_76_rule_clause:rule_clause",
    "native_record_id": "r114_valorant_76_rule_clause",
    "facet": "rule_clause",
    "value": "การปรับแพ้ในแผนที่ (Map Forfeit) สำหรับความผิดร้ายแรงหรือความผิดซ้ำที่ส่งผลกระทบต่อผลการแข่งในแผนที่นั้น",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/fields/answer",
        "source_id": "r114_import_3c0be435c45c3e2853a235dc"
      }
    ],
    "legacy_record_id": "valorant_76"
  },
  {
    "legacy_fact_id": "C13:valorant_73:rule_clause",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C13:valorant_73:rule_clause",
      "record_id": "valorant_73",
      "facet": "rule_clause",
      "value": "การตักเตือน (Warning) สำหรับความผิดครั้งแรกที่มีผลกระทบต่ำ",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "doc108:valorant",
          "locator": "document.xml/paragraph[73]",
          "source_sha256": "a824f58e0fb4dcd1db4ea1097fd02e4d6f5d147822d88dc36a69db5518dbf8d7"
        }
      ]
    },
    "native_fact_id": "C13:r114_valorant_73_rule_clause:rule_clause",
    "native_record_id": "r114_valorant_73_rule_clause",
    "facet": "rule_clause",
    "value": "การตักเตือน (Warning) สำหรับความผิดครั้งแรกที่มีผลกระทบต่ำ",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/fields/answer",
        "source_id": "r114_import_4cdd358824c185a1b59fc7c3"
      }
    ],
    "legacy_record_id": "valorant_73"
  },
  {
    "legacy_fact_id": "C13:valorant_78:rule_clause",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C13:valorant_78:rule_clause",
      "record_id": "valorant_78",
      "facet": "rule_clause",
      "value": "ทางผู้จัดการแข่งขันขอสงวนสิทธิ์ในการเปลี่ยนแปลงแก้ไขกฎระเบียบโดยไม่ต้องแจ้งให้ทราบล่วงหน้า",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "doc108:valorant",
          "locator": "document.xml/paragraph[78]",
          "source_sha256": "a824f58e0fb4dcd1db4ea1097fd02e4d6f5d147822d88dc36a69db5518dbf8d7"
        }
      ]
    },
    "native_fact_id": "C13:r114_valorant_78_rule_clause:rule_clause",
    "native_record_id": "r114_valorant_78_rule_clause",
    "facet": "rule_clause",
    "value": "ทางผู้จัดการแข่งขันขอสงวนสิทธิ์ในการเปลี่ยนแปลงแก้ไขกฎระเบียบโดยไม่ต้องแจ้งให้ทราบล่วงหน้า",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/fields/answer",
        "source_id": "r114_import_e56da98e486b933996e7580e"
      }
    ],
    "legacy_record_id": "valorant_78"
  },
  {
    "legacy_fact_id": "C13:valorant_75:rule_clause",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C13:valorant_75:rule_clause",
      "record_id": "valorant_75",
      "facet": "rule_clause",
      "value": "การปรับแพ้ในรอบ (Round Loss) เมื่อพบว่าผู้เล่นหรือทีมมีเจตนาใช้ช่องโหว่เพื่อสร้างความได้เปรียบ",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "doc108:valorant",
          "locator": "document.xml/paragraph[75]",
          "source_sha256": "a824f58e0fb4dcd1db4ea1097fd02e4d6f5d147822d88dc36a69db5518dbf8d7"
        }
      ]
    },
    "native_fact_id": "C13:r114_valorant_75_rule_clause:rule_clause",
    "native_record_id": "r114_valorant_75_rule_clause",
    "facet": "rule_clause",
    "value": "การปรับแพ้ในรอบ (Round Loss) เมื่อพบว่าผู้เล่นหรือทีมมีเจตนาใช้ช่องโหว่เพื่อสร้างความได้เปรียบ",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/fields/answer",
        "source_id": "r114_import_8fd3e573d71408a2083bbaa0"
      }
    ],
    "legacy_record_id": "valorant_75"
  },
  {
    "legacy_fact_id": "C13:valorant_77:rule_clause",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C13:valorant_77:rule_clause",
      "record_id": "valorant_77",
      "facet": "rule_clause",
      "value": "การปรับแพ้ในแมตช์ (Match Forfeit) กรณีทุจริต (Cheating) หรือล็อกผล (Match fixing)  ",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "doc108:valorant",
          "locator": "document.xml/paragraph[77]",
          "source_sha256": "a824f58e0fb4dcd1db4ea1097fd02e4d6f5d147822d88dc36a69db5518dbf8d7"
        }
      ]
    },
    "native_fact_id": "C13:r114_valorant_77_rule_clause:rule_clause",
    "native_record_id": "r114_valorant_77_rule_clause",
    "facet": "rule_clause",
    "value": "การปรับแพ้ในแมตช์ (Match Forfeit) กรณีทุจริต (Cheating) หรือล็อกผล (Match fixing)  ",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/fields/answer",
        "source_id": "r114_import_c20b0dc83877014b2285fc0e"
      }
    ],
    "legacy_record_id": "valorant_77"
  },
  {
    "legacy_fact_id": "C13:valorant_79:rule_clause",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C13:valorant_79:rule_clause",
      "record_id": "valorant_79",
      "facet": "rule_clause",
      "value": "--------------------------------------------------------------------------------------",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "doc108:valorant",
          "locator": "document.xml/paragraph[79]",
          "source_sha256": "a824f58e0fb4dcd1db4ea1097fd02e4d6f5d147822d88dc36a69db5518dbf8d7"
        }
      ]
    },
    "native_fact_id": "C13:r114_valorant_79_rule_clause:rule_clause",
    "native_record_id": "r114_valorant_79_rule_clause",
    "facet": "rule_clause",
    "value": "--------------------------------------------------------------------------------------",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/fields/answer",
        "source_id": "r114_import_da822a1dc8cf91c226f2f477"
      }
    ],
    "legacy_record_id": "valorant_79"
  },
  {
    "legacy_fact_id": "C13:valorant_74:rule_clause",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C13:valorant_74:rule_clause",
      "record_id": "valorant_74",
      "facet": "rule_clause",
      "value": "การย้อนรอบ (Round Rollback) เมื่อการใช้ช่องโหว่ส่งผลต่อรอบนั้นอย่างชัดเจนแต่ระบุเจตนาไม่ได้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "doc108:valorant",
          "locator": "document.xml/paragraph[74]",
          "source_sha256": "a824f58e0fb4dcd1db4ea1097fd02e4d6f5d147822d88dc36a69db5518dbf8d7"
        }
      ]
    },
    "native_fact_id": "C13:r114_valorant_74_rule_clause:rule_clause",
    "native_record_id": "r114_valorant_74_rule_clause",
    "facet": "rule_clause",
    "value": "การย้อนรอบ (Round Rollback) เมื่อการใช้ช่องโหว่ส่งผลต่อรอบนั้นอย่างชัดเจนแต่ระบุเจตนาไม่ได้",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/fields/answer",
        "source_id": "r114_import_1f48d5bffab0433673ea291f"
      }
    ],
    "legacy_record_id": "valorant_74"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [
    "C13:competition_competition_rules_valorant_psu_phuket_2026_section_010:rule_clause"
  ],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C13-Q055 — กติกาการแข่งขัน

Based on the studio sources, Under PSU Phuket VALORANT 2026 Tournament, what does the section พื้นที่การแข่งขันและกฎระเบียบ specify?

Granularity/overlap: goal clauses ครบ มี source summary เพิ่ม ต้องคง strict fail และไม่เรียก actual content failure อัตโนมัติ

ก่อน: strict=False, additional_or_wrong_scope_claims, state=answer

```text
PSU Phuket VALORANT 2026 Tournament — Competition Venue and Regulations: Competition area and regulations
* During Match Prep, no more than 6 players are allowed.
* Mobile phones, tablets and smartwatches are prohibited in the competition area until the match ends.
* Players may not bring notes or documents into the area. The team captain may bring them, but must give the documents to the referee before every competition.
* Only drinking water in a sealed container and chewing gum are allowed.
Competition process [S1]
PSU Phuket VALORANT 2026 Tournament — พื้นที่การแข่งขันและกฎระเบียบ: จำนวนบุคลากร ในช่วงเตรียมตัว (Match Prep) มีผู้เล่นได้ไม่เกิน 6 คน [S2]
PSU Phuket VALORANT 2026 Tournament — พื้นที่การแข่งขันและกฎระเบียบ: อุปกรณ์อิเล็กทรอนิกส์ ห้ามนำโทรศัพท์มือถือ, แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์ [S3]
PSU Phuket VALORANT 2026 Tournament — พื้นที่การแข่งขันและกฎระเบียบ: เอกสารและโน้ต ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่ หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง [S4]
PSU Phuket VALORANT 2026 Tournament — พื้นที่การแข่งขันและกฎระเบียบ: อาหารและเครื่องดื่ม อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น [S5]
```

หลัง: strict=False, additional_or_wrong_scope_claims, state=answer

```text
A confirmed English translation is unavailable for some clauses; their Thai source text is retained below.
PSU Phuket VALORANT 2026 Tournament — Competition Venue and Regulations: Competition area and regulations
* During Match Prep, no more than 6 players are allowed.
* Mobile phones, tablets and smartwatches are prohibited in the competition area until the match ends.
* Players may not bring notes or documents into the area. The team captain may bring them, but must give the documents to the referee before every competition.
* Only drinking water in a sealed container and chewing gum are allowed.
Competition process [S1]
PSU Phuket VALORANT 2026 Tournament — พื้นที่การแข่งขันและกฎระเบียบ: จำนวนบุคลากร ในช่วงเตรียมตัว (Match Prep) มีผู้เล่นได้ไม่เกิน 6 คน [S2]
PSU Phuket VALORANT 2026 Tournament — พื้นที่การแข่งขันและกฎระเบียบ: อุปกรณ์อิเล็กทรอนิกส์ ห้ามนำโทรศัพท์มือถือ, แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์ [S3]
PSU Phuket VALORANT 2026 Tournament — พื้นที่การแข่งขันและกฎระเบียบ: เอกสารและโน้ต ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่ หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง [S4]
PSU Phuket VALORANT 2026 Tournament — พื้นที่การแข่งขันและกฎระเบียบ: อาหารและเครื่องดื่ม อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น [S5]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C13:valorant_16:rule_clause",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C13:valorant_16:rule_clause",
      "record_id": "valorant_16",
      "facet": "rule_clause",
      "value": "อุปกรณ์อิเล็กทรอนิกส์ ห้ามนำโทรศัพท์มือถือ, แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "doc108:valorant",
          "locator": "document.xml/paragraph[16]",
          "source_sha256": "a824f58e0fb4dcd1db4ea1097fd02e4d6f5d147822d88dc36a69db5518dbf8d7"
        }
      ]
    },
    "native_fact_id": "C13:r114_valorant_16_rule_clause:rule_clause",
    "native_record_id": "r114_valorant_16_rule_clause",
    "facet": "rule_clause",
    "value": "อุปกรณ์อิเล็กทรอนิกส์ ห้ามนำโทรศัพท์มือถือ, แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/fields/answer",
        "source_id": "r114_import_e7a1f0e856d1ad169c7305f1"
      }
    ],
    "legacy_record_id": "valorant_16"
  },
  {
    "legacy_fact_id": "C13:valorant_15:rule_clause",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C13:valorant_15:rule_clause",
      "record_id": "valorant_15",
      "facet": "rule_clause",
      "value": "จำนวนบุคลากร ในช่วงเตรียมตัว (Match Prep) มีผู้เล่นได้ไม่เกิน 6 คน",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "doc108:valorant",
          "locator": "document.xml/paragraph[15]",
          "source_sha256": "a824f58e0fb4dcd1db4ea1097fd02e4d6f5d147822d88dc36a69db5518dbf8d7"
        }
      ]
    },
    "native_fact_id": "C13:r114_valorant_15_rule_clause:rule_clause",
    "native_record_id": "r114_valorant_15_rule_clause",
    "facet": "rule_clause",
    "value": "จำนวนบุคลากร ในช่วงเตรียมตัว (Match Prep) มีผู้เล่นได้ไม่เกิน 6 คน",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/fields/answer",
        "source_id": "r114_import_8d773ff924b88e55fd7ed05a"
      }
    ],
    "legacy_record_id": "valorant_15"
  },
  {
    "legacy_fact_id": "C13:valorant_17:rule_clause",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C13:valorant_17:rule_clause",
      "record_id": "valorant_17",
      "facet": "rule_clause",
      "value": "เอกสารและโน้ต ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่ หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "doc108:valorant",
          "locator": "document.xml/paragraph[17]",
          "source_sha256": "a824f58e0fb4dcd1db4ea1097fd02e4d6f5d147822d88dc36a69db5518dbf8d7"
        }
      ]
    },
    "native_fact_id": "C13:r114_valorant_17_rule_clause:rule_clause",
    "native_record_id": "r114_valorant_17_rule_clause",
    "facet": "rule_clause",
    "value": "เอกสารและโน้ต ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่ หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/fields/answer",
        "source_id": "r114_import_e0a74b7762df88951c196d84"
      }
    ],
    "legacy_record_id": "valorant_17"
  },
  {
    "legacy_fact_id": "C13:valorant_18:rule_clause",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C13:valorant_18:rule_clause",
      "record_id": "valorant_18",
      "facet": "rule_clause",
      "value": "อาหารและเครื่องดื่ม อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "doc108:valorant",
          "locator": "document.xml/paragraph[18]",
          "source_sha256": "a824f58e0fb4dcd1db4ea1097fd02e4d6f5d147822d88dc36a69db5518dbf8d7"
        }
      ]
    },
    "native_fact_id": "C13:r114_valorant_18_rule_clause:rule_clause",
    "native_record_id": "r114_valorant_18_rule_clause",
    "facet": "rule_clause",
    "value": "อาหารและเครื่องดื่ม อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/fields/answer",
        "source_id": "r114_import_f5bd96c02209de83297f00d7"
      }
    ],
    "legacy_record_id": "valorant_18"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [
    "C13:competition_competition_rules_valorant_psu_phuket_2026_section_002:rule_clause"
  ],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C13-Q056 — กติกาการแข่งขัน

Under PSU Phuket VALORANT 2026 Tournament, what does the section 1. เวลานอกทางยุทธวิธี (Tactical Timeout) specify?

Granularity/overlap: goal clauses ครบ มี source summary เพิ่ม ต้องคง strict fail และไม่เรียก actual content failure อัตโนมัติ

ก่อน: strict=False, additional_or_wrong_scope_claims, state=answer

```text
PSU Phuket VALORANT 2026 Tournament — 1. Tactical Timeout: 1. Tactical Timeout
* 2 requests per map during regulation (the first 24 rounds), 60 seconds each.
* In Overtime, each team receives 1 additional request. Unused regulation requests do not carry over. [S1]
PSU Phuket VALORANT 2026 Tournament — 1. เวลานอกทางยุทธวิธี (Tactical Timeout): ขอได้ 2 ครั้งต่อแผนที่ ในรอบปกติ (24 รอบแรก) ครั้งละ 60 วินาที [S2]
PSU Phuket VALORANT 2026 Tournament — 1. เวลานอกทางยุทธวิธี (Tactical Timeout): เมื่อเข้าสู่ช่วงต่อเวลา (Overtime) จะได้เพิ่มอีกทีมละ 1 ครั้ง โดยที่โควตาจากรอบปกติจะไม่ถูกนำมาทบ [S3]
```

หลัง: strict=False, additional_or_wrong_scope_claims, state=answer

```text
A confirmed English translation is unavailable for some clauses; their Thai source text is retained below.
PSU Phuket VALORANT 2026 Tournament — 1. Tactical Timeout: 1. Tactical Timeout
* 2 requests per map during regulation (the first 24 rounds), 60 seconds each.
* In Overtime, each team receives 1 additional request. Unused regulation requests do not carry over. [S1]
PSU Phuket VALORANT 2026 Tournament — 1. เวลานอกทางยุทธวิธี (Tactical Timeout): ขอได้ 2 ครั้งต่อแผนที่ ในรอบปกติ (24 รอบแรก) ครั้งละ 60 วินาที [S2]
PSU Phuket VALORANT 2026 Tournament — 1. เวลานอกทางยุทธวิธี (Tactical Timeout): เมื่อเข้าสู่ช่วงต่อเวลา (Overtime) จะได้เพิ่มอีกทีมละ 1 ครั้ง โดยที่โควตาจากรอบปกติจะไม่ถูกนำมาทบ [S3]
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C13:valorant_47:rule_clause",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C13:valorant_47:rule_clause",
      "record_id": "valorant_47",
      "facet": "rule_clause",
      "value": "เมื่อเข้าสู่ช่วงต่อเวลา (Overtime) จะได้เพิ่มอีกทีมละ 1 ครั้ง โดยที่โควตาจากรอบปกติจะไม่ถูกนำมาทบ",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "doc108:valorant",
          "locator": "document.xml/paragraph[47]",
          "source_sha256": "a824f58e0fb4dcd1db4ea1097fd02e4d6f5d147822d88dc36a69db5518dbf8d7"
        }
      ]
    },
    "native_fact_id": "C13:r114_valorant_47_rule_clause:rule_clause",
    "native_record_id": "r114_valorant_47_rule_clause",
    "facet": "rule_clause",
    "value": "เมื่อเข้าสู่ช่วงต่อเวลา (Overtime) จะได้เพิ่มอีกทีมละ 1 ครั้ง โดยที่โควตาจากรอบปกติจะไม่ถูกนำมาทบ",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/fields/answer",
        "source_id": "r114_import_342c954150c47684a27461f1"
      }
    ],
    "legacy_record_id": "valorant_47"
  },
  {
    "legacy_fact_id": "C13:valorant_46:rule_clause",
    "alignment_kind": "aligned",
    "legacy_expected": {
      "fact_id": "C13:valorant_46:rule_clause",
      "record_id": "valorant_46",
      "facet": "rule_clause",
      "value": "ขอได้ 2 ครั้งต่อแผนที่ ในรอบปกติ (24 รอบแรก) ครั้งละ 60 วินาที",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "doc108:valorant",
          "locator": "document.xml/paragraph[46]",
          "source_sha256": "a824f58e0fb4dcd1db4ea1097fd02e4d6f5d147822d88dc36a69db5518dbf8d7"
        }
      ]
    },
    "native_fact_id": "C13:r114_valorant_46_rule_clause:rule_clause",
    "native_record_id": "r114_valorant_46_rule_clause",
    "facet": "rule_clause",
    "value": "ขอได้ 2 ครั้งต่อแผนที่ ในรอบปกติ (24 รอบแรก) ครั้งละ 60 วินาที",
    "numeric": null,
    "evidence_refs": [
      {
        "locator": "/fields/answer",
        "source_id": "r114_import_a52f1003396c58d1a435bc36"
      }
    ],
    "legacy_record_id": "valorant_46"
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [
    "C13:competition_competition_rules_valorant_psu_phuket_2026_section_006:rule_clause"
  ],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q001 — ข่าว/กิจกรรม

งาน กิจกรรมจำลองทดสอบ 06 ยังสมัครได้ไหม

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_6:status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_6:status",
      "record_id": "fixture_event_6",
      "facet": "status",
      "value": "ปิดรับสมัครแล้ว",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "6/status"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_6:status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q002 — ข่าว/กิจกรรม

ขอสอบถามหน่อยครับ กิจกรรมจำลองทดสอบ 12 ปิดรับสมัครหรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=answer

```text
**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร [S1]
• หัวข้อเชิงความหมาย: C13 [S2]
• ขอบเขตของข้อมูล: {"r114_fact": {"category": "C13", "facet": "rule_clause", "subject": {"th": "กฎระเบียบและรูปแบบการแข่งขัน Counter-Strike 2", "en": "PSU Phuket CS2 2026 Tournament"}, "label": {"th": "ข้อจำกัด", "en": "ข้อจำกัด"}, "section_number": null, "english_translation_missing": true, "source_record_id": "cs2_12"}} [S3]
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_12:status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_12:status",
      "record_id": "fixture_event_12",
      "facet": "status",
      "value": "ปิดรับสมัครแล้ว",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "12/status"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_12:status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q003 — ข่าว/กิจกรรม

ช่วยตอบสั้น ๆ ว่า อยากไป กิจกรรมจำลองทดสอบ 04 ต้องไปวันไหน

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_4:date",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_4:date",
      "record_id": "fixture_event_4",
      "facet": "date",
      "value": "2026-10-25",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "4/date"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_4:date"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q004 — ข่าว/กิจกรรม

อยากรู้ว่า งาน กิจกรรมจำลองทดสอบ 08 ยังสมัครได้ไหม

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=answer

```text
**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: ไม่ต้องเป็นนักศึกษา PSU ครับ ขั้นตอนจองที่เผยแพร่ไม่ได้ระบุว่าต้องสมัครสมาชิกแยกก่อนจอง คนภายนอกใช้ช่อง National ID และแสดงบัตรประชาชนตอนเช็กอิน ค่าบริการขึ้นกับกลุ่มผู้ใช้และบริการ [S1]
• หัวข้อเชิงความหมาย: service_policy [S2]
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_8:status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_8:status",
      "record_id": "fixture_event_8",
      "facet": "status",
      "value": "ปิดรับสมัครแล้ว",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "8/status"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_8:status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q005 — ข่าว/กิจกรรม

กำลังวางแผนไปใช้บริการ เลยขอถามว่า วันจัดงาน กิจกรรมจำลองทดสอบ 02 คือวันที่เท่าไร

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_2:date",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_2:date",
      "record_id": "fixture_event_2",
      "facet": "date",
      "value": "2026-10-23",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "2/date"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_2:date"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q006 — ข่าว/กิจกรรม

รบกวนเช็กให้หน่อย สถานะการรับสมัคร กิจกรรมจำลองทดสอบ 10 เป็นอย่างไร

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_10:status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_10:status",
      "record_id": "fixture_event_10",
      "facet": "status",
      "value": "ปิดรับสมัครแล้ว",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "10/status"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_10:status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q007 — ข่าว/กิจกรรม

ถามจากข้อมูลที่ศูนย์ให้ไว้ งาน กิจกรรมจำลองทดสอบ 01 ยังสมัครได้ไหม

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_1:status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_1:status",
      "record_id": "fixture_event_1",
      "facet": "status",
      "value": "เปิดรับสมัคร",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "1/status"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_1:status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q008 — ข่าว/กิจกรรม

ขอลิงก์สมัครงาน กิจกรรมจำลองทดสอบ 09

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_source

```text
ข้อมูลที่เลือกยังไม่ยืนยันส่วนที่ถามโดยตรงครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_9:registration",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_9:registration",
      "record_id": "fixture_event_9",
      "facet": "registration",
      "value": "https://example.invalid/test-registration/09",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "9/registration"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_9:registration"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q009 — ข่าว/กิจกรรม

ขอสอบถามหน่อยครับ สถานะการรับสมัคร กิจกรรมจำลองทดสอบ 03 เป็นอย่างไร

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_3:status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_3:status",
      "record_id": "fixture_event_3",
      "facet": "status",
      "value": "เปิดรับสมัคร",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "3/status"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_3:status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q010 — ข่าว/กิจกรรม

ช่วยตอบสั้น ๆ ว่า กิจกรรมจำลองทดสอบ 01 จัดวันไหน

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_1:date",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_1:date",
      "record_id": "fixture_event_1",
      "facet": "date",
      "value": "2026-10-22",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "1/date"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_1:date"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q011 — ข่าว/กิจกรรม

อยากรู้ว่า วันจัดงาน กิจกรรมจำลองทดสอบ 10 คือวันที่เท่าไร

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_10:date",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_10:date",
      "record_id": "fixture_event_10",
      "facet": "date",
      "value": "2026-10-31",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "10/date"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_10:date"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q012 — ข่าว/กิจกรรม

กำลังวางแผนไปใช้บริการ เลยขอถามว่า สถานะการรับสมัคร กิจกรรมจำลองทดสอบ 07 เป็นอย่างไร

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_7:status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_7:status",
      "record_id": "fixture_event_7",
      "facet": "status",
      "value": "เปิดรับสมัคร",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "7/status"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_7:status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q013 — ข่าว/กิจกรรม

รบกวนเช็กให้หน่อย งาน กิจกรรมจำลองทดสอบ 02 ยังสมัครได้ไหม

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_2:status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_2:status",
      "record_id": "fixture_event_2",
      "facet": "status",
      "value": "ปิดรับสมัครแล้ว",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "2/status"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_2:status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q014 — ข่าว/กิจกรรม

ถามจากข้อมูลที่ศูนย์ให้ไว้ กิจกรรมจำลองทดสอบ 05 ปิดรับสมัครหรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_5:status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_5:status",
      "record_id": "fixture_event_5",
      "facet": "status",
      "value": "เปิดรับสมัคร",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "5/status"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_5:status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q015 — ข่าว/กิจกรรม

อยากไป กิจกรรมจำลองทดสอบ 06 ต้องไปวันไหน

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_6:date",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_6:date",
      "record_id": "fixture_event_6",
      "facet": "date",
      "value": "2026-10-27",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "6/date"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_6:date"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q016 — ข่าว/กิจกรรม

ขอสอบถามหน่อยครับ จะสมัคร กิจกรรมจำลองทดสอบ 03 ได้จากลิงก์ไหน

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_source

```text
ข้อมูลที่เลือกยังไม่ยืนยันส่วนที่ถามโดยตรงครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_3:registration",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_3:registration",
      "record_id": "fixture_event_3",
      "facet": "registration",
      "value": "https://example.invalid/test-registration/03",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "3/registration"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_3:registration"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q017 — ข่าว/กิจกรรม

ช่วยตอบสั้น ๆ ว่า ขอรายละเอียดของงาน กิจกรรมจำลองทดสอบ 03

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_3:description",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_3:description",
      "record_id": "fixture_event_3",
      "facet": "description",
      "value": "กิจกรรมจำลอง 03 สำหรับตรวจการอ่านข่าว ไม่ใช่กิจกรรมจริง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "3/description"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_3:description"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q018 — ข่าว/กิจกรรม

อยากรู้ว่า มีช่องทางลงทะเบียน กิจกรรมจำลองทดสอบ 01 ไหม

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=answer

```text
**เพจศูนย์อีสปอร์ต**
• ช่องทางติดต่อ: https://www.facebook.com/psuesportsphuket [S1]
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_1:registration",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_1:registration",
      "record_id": "fixture_event_1",
      "facet": "registration",
      "value": "https://example.invalid/test-registration/01",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "1/registration"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_1:registration"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q019 — ข่าว/กิจกรรม

กำลังวางแผนไปใช้บริการ เลยขอถามว่า กิจกรรมจำลองทดสอบ 08 จัดวันไหน

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_8:date",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_8:date",
      "record_id": "fixture_event_8",
      "facet": "date",
      "value": "2026-10-29",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "8/date"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_8:date"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q020 — ข่าว/กิจกรรม

รบกวนเช็กให้หน่อย ขอรายละเอียดของงาน กิจกรรมจำลองทดสอบ 11

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_11:description",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_11:description",
      "record_id": "fixture_event_11",
      "facet": "description",
      "value": "กิจกรรมจำลอง 11 สำหรับตรวจการอ่านข่าว ไม่ใช่กิจกรรมจริง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "11/description"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_11:description"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q021 — ข่าว/กิจกรรม

ถามจากข้อมูลที่ศูนย์ให้ไว้ สถานะการรับสมัคร กิจกรรมจำลองทดสอบ 09 เป็นอย่างไร

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_9:status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_9:status",
      "record_id": "fixture_event_9",
      "facet": "status",
      "value": "เปิดรับสมัคร",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "9/status"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_9:status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q022 — ข่าว/กิจกรรม

จะสมัคร กิจกรรมจำลองทดสอบ 10 ได้จากลิงก์ไหน

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_source

```text
ข้อมูลที่เลือกยังไม่ยืนยันส่วนที่ถามโดยตรงครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_10:registration",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_10:registration",
      "record_id": "fixture_event_10",
      "facet": "registration",
      "value": "https://example.invalid/test-registration/10",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "10/registration"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_10:registration"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q023 — ข่าว/กิจกรรม

ขอสอบถามหน่อยครับ ขอรายละเอียดของงาน กิจกรรมจำลองทดสอบ 08

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_8:description",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_8:description",
      "record_id": "fixture_event_8",
      "facet": "description",
      "value": "กิจกรรมจำลอง 08 สำหรับตรวจการอ่านข่าว ไม่ใช่กิจกรรมจริง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "8/description"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_8:description"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q024 — ข่าว/กิจกรรม

ช่วยตอบสั้น ๆ ว่า อยากไป กิจกรรมจำลองทดสอบ 05 ต้องไปวันไหน

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_5:date",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_5:date",
      "record_id": "fixture_event_5",
      "facet": "date",
      "value": "2026-10-26",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "5/date"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_5:date"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q025 — ข่าว/กิจกรรม

อยากรู้ว่า กิจกรรมจำลองทดสอบ 11 จัดวันไหน

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_11:date",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_11:date",
      "record_id": "fixture_event_11",
      "facet": "date",
      "value": "2026-11-01",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "11/date"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_11:date"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q026 — ข่าว/กิจกรรม

กำลังวางแผนไปใช้บริการ เลยขอถามว่า ขอรายละเอียดของงาน กิจกรรมจำลองทดสอบ 12

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_12:description",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_12:description",
      "record_id": "fixture_event_12",
      "facet": "description",
      "value": "กิจกรรมจำลอง 12 สำหรับตรวจการอ่านข่าว ไม่ใช่กิจกรรมจริง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "12/description"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_12:description"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q027 — ข่าว/กิจกรรม

รบกวนเช็กให้หน่อย มีช่องทางลงทะเบียน กิจกรรมจำลองทดสอบ 12 ไหม

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=answer

```text
**เพจศูนย์อีสปอร์ต**
• ช่องทางติดต่อ: https://www.facebook.com/psuesportsphuket [S1]
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_12:registration",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_12:registration",
      "record_id": "fixture_event_12",
      "facet": "registration",
      "value": "https://example.invalid/test-registration/12",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "12/registration"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_12:registration"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q028 — ข่าว/กิจกรรม

ถามจากข้อมูลที่ศูนย์ให้ไว้ จะสมัคร กิจกรรมจำลองทดสอบ 07 ได้จากลิงก์ไหน

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_7:registration",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_7:registration",
      "record_id": "fixture_event_7",
      "facet": "registration",
      "value": "https://example.invalid/test-registration/07",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "7/registration"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_7:registration"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q029 — ข่าว/กิจกรรม

ขอรายละเอียดของงาน กิจกรรมจำลองทดสอบ 02

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_2:description",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_2:description",
      "record_id": "fixture_event_2",
      "facet": "description",
      "value": "กิจกรรมจำลอง 02 สำหรับตรวจการอ่านข่าว ไม่ใช่กิจกรรมจริง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "2/description"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_2:description"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q030 — ข่าว/กิจกรรม

ขอสอบถามหน่อยครับ กิจกรรมจำลองทดสอบ 09 จัดเกี่ยวกับอะไร

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_9:description",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_9:description",
      "record_id": "fixture_event_9",
      "facet": "description",
      "value": "กิจกรรมจำลอง 09 สำหรับตรวจการอ่านข่าว ไม่ใช่กิจกรรมจริง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "9/description"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_9:description"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q031 — ข่าว/กิจกรรม

ช่วยตอบสั้น ๆ ว่า จะสมัคร กิจกรรมจำลองทดสอบ 11 ได้จากลิงก์ไหน

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_11:registration",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_11:registration",
      "record_id": "fixture_event_11",
      "facet": "registration",
      "value": "https://example.invalid/test-registration/11",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "11/registration"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_11:registration"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q032 — ข่าว/กิจกรรม

อยากรู้ว่า วันจัดงาน กิจกรรมจำลองทดสอบ 07 คือวันที่เท่าไร

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_7:date",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_7:date",
      "record_id": "fixture_event_7",
      "facet": "date",
      "value": "2026-10-28",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "7/date"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_7:date"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q033 — ข่าว/กิจกรรม

กำลังวางแผนไปใช้บริการ เลยขอถามว่า อยากไป กิจกรรมจำลองทดสอบ 09 ต้องไปวันไหน

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_9:date",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_9:date",
      "record_id": "fixture_event_9",
      "facet": "date",
      "value": "2026-10-30",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "9/date"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_9:date"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q034 — ข่าว/กิจกรรม

รบกวนเช็กให้หน่อย กิจกรรมจำลองทดสอบ 12 จัดวันไหน

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_source

```text
ข้อมูลที่เลือกยังไม่ยืนยันส่วนที่ถามโดยตรงครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_12:date",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_12:date",
      "record_id": "fixture_event_12",
      "facet": "date",
      "value": "2026-11-02",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "12/date"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_12:date"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q035 — ข่าว/กิจกรรม

ถามจากข้อมูลที่ศูนย์ให้ไว้ ขอรายละเอียดของงาน กิจกรรมจำลองทดสอบ 05

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_5:description",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_5:description",
      "record_id": "fixture_event_5",
      "facet": "description",
      "value": "กิจกรรมจำลอง 05 สำหรับตรวจการอ่านข่าว ไม่ใช่กิจกรรมจริง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "5/description"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_5:description"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q036 — ข่าว/กิจกรรม

สถานะการรับสมัคร กิจกรรมจำลองทดสอบ 04 เป็นอย่างไรร

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_4:status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_4:status",
      "record_id": "fixture_event_4",
      "facet": "status",
      "value": "ปิดรับสมัครแล้ว",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "4/status"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_4:status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q037 — ข่าว/กิจกรรม

ขอสอบถามหน่อยครับ งาน กิจกรรมจำลองทดสอบ 06 คือกิจกรรมอะไร

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_6:description",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_6:description",
      "record_id": "fixture_event_6",
      "facet": "description",
      "value": "กิจกรรมจำลอง 06 สำหรับตรวจการอ่านข่าว ไม่ใช่กิจกรรมจริง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "6/description"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_6:description"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q038 — ข่าว/กิจกรรม

ช่วยตอบสั้น ๆ ว่า ขอลิงก์สมัครงาน กิจกรรมจำลองทดสอบ 08

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_8:registration",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_8:registration",
      "record_id": "fixture_event_8",
      "facet": "registration",
      "value": "https://example.invalid/test-registration/08",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "8/registration"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_8:registration"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q039 — ข่าว/กิจกรรม

อยากรู้ว่า กิจกรรมจำลองทดสอบ 04 จัดเกี่ยวกับอะไร

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_4:description",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_4:description",
      "record_id": "fixture_event_4",
      "facet": "description",
      "value": "กิจกรรมจำลอง 04 สำหรับตรวจการอ่านข่าว ไม่ใช่กิจกรรมจริง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "4/description"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_4:description"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q040 — ข่าว/กิจกรรม

กำลังวางแผนไปใช้บริการ เลยขอถามว่า จะสมัคร กิจกรรมจำลองทดสอบ 02 ได้จากลิงก์ไหน

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_2:registration",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_2:registration",
      "record_id": "fixture_event_2",
      "facet": "registration",
      "value": "https://example.invalid/test-registration/02",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "2/registration"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_2:registration"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q041 — ข่าว/กิจกรรม

รบกวนเช็กให้หน่อย ขอลิงก์สมัครงาน กิจกรรมจำลองทดสอบ 04

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_4:registration",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_4:registration",
      "record_id": "fixture_event_4",
      "facet": "registration",
      "value": "https://example.invalid/test-registration/04",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "4/registration"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_4:registration"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q042 — ข่าว/กิจกรรม

ถามจากข้อมูลที่ศูนย์ให้ไว้ สถานะการรับสมัคร กิจกรรมจำลองทดสอบ 11 เป็นอย่างไร

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_11:status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_11:status",
      "record_id": "fixture_event_11",
      "facet": "status",
      "value": "เปิดรับสมัคร",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "11/status"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_11:status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q043 — ข่าว/กิจกรรม

จะสมัคร กิจกรรมจำลองทดสอบ 06 ได้จากลิงก์ไหน

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_source

```text
ข้อมูลที่เลือกยังไม่ยืนยันส่วนที่ถามโดยตรงครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_6:registration",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_6:registration",
      "record_id": "fixture_event_6",
      "facet": "registration",
      "value": "https://example.invalid/test-registration/06",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "6/registration"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_6:registration"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q044 — ข่าว/กิจกรรม

ขอสอบถามหน่อยครับ ขอรายละเอียดของงาน กิจกรรมจำลองทดสอบ 07

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_7:description",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_7:description",
      "record_id": "fixture_event_7",
      "facet": "description",
      "value": "กิจกรรมจำลอง 07 สำหรับตรวจการอ่านข่าว ไม่ใช่กิจกรรมจริง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "7/description"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_7:description"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q045 — ข่าว/กิจกรรม

ช่วยตอบสั้น ๆ ว่า กิจกรรมจำลองทดสอบ 01 จัดเกี่ยวกับอะไร

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_1:description",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_1:description",
      "record_id": "fixture_event_1",
      "facet": "description",
      "value": "กิจกรรมจำลอง 01 สำหรับตรวจการอ่านข่าว ไม่ใช่กิจกรรมจริง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "1/description"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_1:description"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q046 — ข่าว/กิจกรรม

อยากรู้ว่า กิจกรรมจำลองทดสอบ 03 จัดวันไหน

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_3:date",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_3:date",
      "record_id": "fixture_event_3",
      "facet": "date",
      "value": "2026-10-24",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "3/date"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_3:date"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q047 — ข่าว/กิจกรรม

กำลังวางแผนไปใช้บริการ เลยขอถามว่า ขอลิงก์สมัครงาน กิจกรรมจำลองทดสอบ 05

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_source

```text
ข้อมูลที่เลือกยังไม่ยืนยันส่วนที่ถามโดยตรงครับ
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_5:registration",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_5:registration",
      "record_id": "fixture_event_5",
      "facet": "registration",
      "value": "https://example.invalid/test-registration/05",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "5/registration"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_5:registration"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q048 — ข่าว/กิจกรรม

รบกวนเช็กให้หน่อย กิจกรรมจำลองทดสอบ 10 จัดเกี่ยวกับอะไร

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_10:description",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_10:description",
      "record_id": "fixture_event_10",
      "facet": "description",
      "value": "กิจกรรมจำลอง 10 สำหรับตรวจการอ่านข่าว ไม่ใช่กิจกรรมจริง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "10/description"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_10:description"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q049 — ข่าว/กิจกรรม

ถามจากข้อมูลที่ศูนย์ให้ไว้ งาน กิจกรรมจำลองทดสอบ 06 ยังสมัครได้ไหม

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_6:status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_6:status",
      "record_id": "fixture_event_6",
      "facet": "status",
      "value": "ปิดรับสมัครแล้ว",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "6/status"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_6:status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q050 — ข่าว/กิจกรรม

กิจกรรมจำลองทดสอบ 12 ปิดรับสมัครหรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=answer

```text
**ข้อมูลที่เกี่ยวข้อง**
• ข้อมูลที่ยืนยันได้: ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร [S1]
• หัวข้อเชิงความหมาย: C13 [S2]
• ขอบเขตของข้อมูล: {"r114_fact": {"category": "C13", "facet": "rule_clause", "subject": {"th": "กฎระเบียบและรูปแบบการแข่งขัน Counter-Strike 2", "en": "PSU Phuket CS2 2026 Tournament"}, "label": {"th": "ข้อจำกัด", "en": "ข้อจำกัด"}, "section_number": null, "english_translation_missing": true, "source_record_id": "cs2_12"}} [S3]
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_12:status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_12:status",
      "record_id": "fixture_event_12",
      "facet": "status",
      "value": "ปิดรับสมัครแล้ว",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "12/status"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_12:status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q051 — ข่าว/กิจกรรม

When does Synthetic test event 04 take place?

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
I could not match this question to the migrated information. Please specify the game, device or topic you want to know about.
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
No confirmed source is available for the requested detail.
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_4:date",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_4:date",
      "record_id": "fixture_event_4",
      "facet": "date",
      "value": "2026-10-25",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "4/date"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_4:date"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q052 — ข่าว/กิจกรรม

Could you help me with this: Has registration closed for Synthetic test event 08?

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
I could not match this question to the migrated information. Please specify the game, device or topic you want to know about.
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
No confirmed source is available for the requested detail.
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_8:status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_8:status",
      "record_id": "fixture_event_8",
      "facet": "status",
      "value": "Registration closed",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "8/status"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_8:status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q053 — ข่าว/กิจกรรม

Please answer briefly: When does Synthetic test event 02 take place?

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
I could not match this question to the migrated information. Please specify the game, device or topic you want to know about.
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
No confirmed source is available for the requested detail.
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_2:date",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_2:date",
      "record_id": "fixture_event_2",
      "facet": "date",
      "value": "2026-10-23",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "2/date"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_2:date"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q054 — ข่าว/กิจกรรม

I would like to know: Has registration closed for Synthetic test event 10?

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
I could not match this question to the migrated information. Please specify the game, device or topic you want to know about.
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
No confirmed source is available for the requested detail.
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_10:status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_10:status",
      "record_id": "fixture_event_10",
      "facet": "status",
      "value": "Registration closed",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "10/status"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_10:status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q055 — ข่าว/กิจกรรม

Based on the studio sources, Is registration for Synthetic test event 01 still open?

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
I could not match this question to the migrated information. Please specify the game, device or topic you want to know about.
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
No confirmed source is available for the requested detail.
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_1:status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_1:status",
      "record_id": "fixture_event_1",
      "facet": "status",
      "value": "Registration open",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "1/status"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_1:status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q056 — ข่าว/กิจกรรม

Give me the registration URL for Synthetic test event 09.

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
I could not match this question to the migrated information. Please specify the game, device or topic you want to know about.
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
No confirmed source is available for the requested detail.
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_9:registration",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_9:registration",
      "record_id": "fixture_event_9",
      "facet": "registration",
      "value": "https://example.invalid/test-registration/09",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "9/registration"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_9:registration"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q057 — ข่าว/กิจกรรม

Could you help me with this: Is registration for Synthetic test event 03 still open?

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
I could not match this question to the migrated information. Please specify the game, device or topic you want to know about.
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
No confirmed source is available for the requested detail.
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_3:status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_3:status",
      "record_id": "fixture_event_3",
      "facet": "status",
      "value": "Registration open",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "3/status"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_3:status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q058 — ข่าว/กิจกรรม

Please answer briefly: What is the date of Synthetic test event 01?

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
I could not match this question to the migrated information. Please specify the game, device or topic you want to know about.
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
No confirmed source is available for the requested detail.
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_1:date",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_1:date",
      "record_id": "fixture_event_1",
      "facet": "date",
      "value": "2026-10-22",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "1/date"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_1:date"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q059 — ข่าว/กิจกรรม

I would like to know: When does Synthetic test event 10 take place?

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
I could not match this question to the migrated information. Please specify the game, device or topic you want to know about.
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
No confirmed source is available for the requested detail.
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_10:date",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_10:date",
      "record_id": "fixture_event_10",
      "facet": "date",
      "value": "2026-10-31",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "10/date"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_10:date"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q060 — ข่าว/กิจกรรม

Based on the studio sources, Has registration closed for Synthetic test event 07?

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
I could not match this question to the migrated information. Please specify the game, device or topic you want to know about.
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
No confirmed source is available for the requested detail.
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_7:status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_7:status",
      "record_id": "fixture_event_7",
      "facet": "status",
      "value": "Registration open",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "7/status"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_7:status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q061 — ข่าว/กิจกรรม

Is registration for Synthetic test event 02 still open? and also What is the date of Synthetic test event 02?

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
I could not match this question to the migrated information. Please specify the game, device or topic you want to know about.
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
No confirmed source is available for the requested detail.

No confirmed source is available for the requested detail.
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_2:status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_2:status",
      "record_id": "fixture_event_2",
      "facet": "status",
      "value": "Registration closed",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "2/status"
        }
      ]
    }
  },
  {
    "legacy_fact_id": "C14:fixture_event_2:date",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_2:date",
      "record_id": "fixture_event_2",
      "facet": "date",
      "value": "2026-10-23",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "2/date"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_2:status",
    "C14:fixture_event_2:date"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q062 — ข่าว/กิจกรรม

Could you help me with this: Has registration closed for Synthetic test event 05? and also When does Synthetic test event 05 take place?

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
I could not match this question to the migrated information. Please specify the game, device or topic you want to know about.
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
No confirmed source is available for the requested detail.

No confirmed source is available for the requested detail.
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_5:status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_5:status",
      "record_id": "fixture_event_5",
      "facet": "status",
      "value": "Registration open",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "5/status"
        }
      ]
    }
  },
  {
    "legacy_fact_id": "C14:fixture_event_5:date",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_5:date",
      "record_id": "fixture_event_5",
      "facet": "date",
      "value": "2026-10-26",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "5/date"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_5:status",
    "C14:fixture_event_5:date"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q063 — ข่าว/กิจกรรม

Please answer briefly: When does Synthetic test event 06 take place? and also Has registration closed for Synthetic test event 06?

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
I could not match this question to the migrated information. Please specify the game, device or topic you want to know about.
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
No confirmed source is available for the requested detail.

No confirmed source is available for the requested detail.
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_6:date",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_6:date",
      "record_id": "fixture_event_6",
      "facet": "date",
      "value": "2026-10-27",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "6/date"
        }
      ]
    }
  },
  {
    "legacy_fact_id": "C14:fixture_event_6:status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_6:status",
      "record_id": "fixture_event_6",
      "facet": "status",
      "value": "Registration closed",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "6/status"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_6:date",
    "C14:fixture_event_6:status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q064 — ข่าว/กิจกรรม

I would like to know: Give me the registration URL for Synthetic test event 03. and also Is registration for Synthetic test event 03 still open?

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
I could not match this question to the migrated information. Please specify the game, device or topic you want to know about.
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
No confirmed source is available for the requested detail.

No confirmed source is available for the requested detail.
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_3:registration",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_3:registration",
      "record_id": "fixture_event_3",
      "facet": "registration",
      "value": "https://example.invalid/test-registration/03",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "3/registration"
        }
      ]
    }
  },
  {
    "legacy_fact_id": "C14:fixture_event_3:status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_3:status",
      "record_id": "fixture_event_3",
      "facet": "status",
      "value": "Registration open",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "3/status"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_3:registration",
    "C14:fixture_event_3:status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q065 — ข่าว/กิจกรรม

Based on the studio sources, What is Synthetic test event 03 about? and also Has registration closed for Synthetic test event 03?

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
I could not match this question to the migrated information. Please specify the game, device or topic you want to know about.
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
No confirmed source is available for the requested detail.

No confirmed source is available for the requested detail.
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_3:description",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_3:description",
      "record_id": "fixture_event_3",
      "facet": "description",
      "value": "Synthetic event 03 for testing news reading; not an actual studio announcement",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "3/description"
        }
      ]
    }
  },
  {
    "legacy_fact_id": "C14:fixture_event_3:status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_3:status",
      "record_id": "fixture_event_3",
      "facet": "status",
      "value": "Registration open",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "3/status"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_3:description",
    "C14:fixture_event_3:status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q066 — ข่าว/กิจกรรม

Give me the registration URL for Synthetic test event 01. and also Is registration for Synthetic test event 01 still open?

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
I could not match this question to the migrated information. Please specify the game, device or topic you want to know about.
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
No confirmed source is available for the requested detail.

No confirmed source is available for the requested detail.
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_1:registration",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_1:registration",
      "record_id": "fixture_event_1",
      "facet": "registration",
      "value": "https://example.invalid/test-registration/01",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "1/registration"
        }
      ]
    }
  },
  {
    "legacy_fact_id": "C14:fixture_event_1:status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_1:status",
      "record_id": "fixture_event_1",
      "facet": "status",
      "value": "Registration open",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "1/status"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_1:registration",
    "C14:fixture_event_1:status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q067 — ข่าว/กิจกรรม

Could you help me with this: When does Synthetic test event 08 take place? and also Has registration closed for Synthetic test event 08?

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
I could not match this question to the migrated information. Please specify the game, device or topic you want to know about.
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
No confirmed source is available for the requested detail.

No confirmed source is available for the requested detail.
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_8:date",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_8:date",
      "record_id": "fixture_event_8",
      "facet": "date",
      "value": "2026-10-29",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "8/date"
        }
      ]
    }
  },
  {
    "legacy_fact_id": "C14:fixture_event_8:status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_8:status",
      "record_id": "fixture_event_8",
      "facet": "status",
      "value": "Registration closed",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "8/status"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_8:date",
    "C14:fixture_event_8:status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q068 — ข่าว/กิจกรรม

Please answer briefly: Describe the event Synthetic test event 11. and also When does Synthetic test event 11 take place?

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
I could not match this question to the migrated information. Please specify the game, device or topic you want to know about.
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
No confirmed source is available for the requested detail.

No confirmed source is available for the requested detail.
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_11:description",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_11:description",
      "record_id": "fixture_event_11",
      "facet": "description",
      "value": "Synthetic event 11 for testing news reading; not an actual studio announcement",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "11/description"
        }
      ]
    }
  },
  {
    "legacy_fact_id": "C14:fixture_event_11:date",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_11:date",
      "record_id": "fixture_event_11",
      "facet": "date",
      "value": "2026-11-01",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "11/date"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_11:description",
    "C14:fixture_event_11:date"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q069 — ข่าว/กิจกรรม

I would like to know: Is registration for Synthetic test event 09 still open? and also Give me the registration URL for Synthetic test event 09.

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
I could not match this question to the migrated information. Please specify the game, device or topic you want to know about.
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
No confirmed source is available for the requested detail.

No confirmed source is available for the requested detail.
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_9:status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_9:status",
      "record_id": "fixture_event_9",
      "facet": "status",
      "value": "Registration open",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "9/status"
        }
      ]
    }
  },
  {
    "legacy_fact_id": "C14:fixture_event_9:registration",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_9:registration",
      "record_id": "fixture_event_9",
      "facet": "registration",
      "value": "https://example.invalid/test-registration/09",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "9/registration"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_9:status",
    "C14:fixture_event_9:registration"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q070 — ข่าว/กิจกรรม

Based on the studio sources, Give me the registration URL for Synthetic test event 10. and also Is registration for Synthetic test event 10 still open?

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=answer

```text
**Relevant information**
• Confirmed information: No refund is given for the original booking when changing services; cancel and book again as previously stated. [S1]
• topic: C08 [S2]
• Scope: {"r114_fact": {"category": "C08", "facet": "owner_policy", "subject": {"th": "เปลี่ยนบริการระหว่างรอบ", "en": "change service"}, "label": {"th": "เงื่อนไขและวิธีปฏิบัติ", "en": "conditions and procedure"}, "owner_confirmed": true, "source_record_id": "Q004"}} [S3]

English translation is machine generated and has not been reviewed by the owner.
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
No confirmed source is available for the requested detail.

No confirmed source is available for the requested detail.
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_10:registration",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_10:registration",
      "record_id": "fixture_event_10",
      "facet": "registration",
      "value": "https://example.invalid/test-registration/10",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "10/registration"
        }
      ]
    }
  },
  {
    "legacy_fact_id": "C14:fixture_event_10:status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_10:status",
      "record_id": "fixture_event_10",
      "facet": "status",
      "value": "Registration closed",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "10/status"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_10:registration",
    "C14:fixture_event_10:status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q071 — ข่าว/กิจกรรม

ขอรายละเอียดของงาน กิจกรรมจำลองทดสอบ 08 แล้วขอสถานะการรับสมัคร กิจกรรมจำลองทดสอบ 08 เป็นอย่างไรร

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ

ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_8:description",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_8:description",
      "record_id": "fixture_event_8",
      "facet": "description",
      "value": "กิจกรรมจำลอง 08 สำหรับตรวจการอ่านข่าว ไม่ใช่กิจกรรมจริง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "8/description"
        }
      ]
    }
  },
  {
    "legacy_fact_id": "C14:fixture_event_8:status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_8:status",
      "record_id": "fixture_event_8",
      "facet": "status",
      "value": "ปิดรับสมัครแล้ว",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "8/status"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_8:description",
    "C14:fixture_event_8:status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q072 — ข่าว/กิจกรรม

ขอสอบถามหน่อยครับ อยากไป กิจกรรมจำลองทดสอบ 05 ต้องไปวันไหน แล้วของาน กิจกรรมจำลองทดสอบ 05 ยังสมัครได้ไหม

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ

ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_5:date",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_5:date",
      "record_id": "fixture_event_5",
      "facet": "date",
      "value": "2026-10-26",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "5/date"
        }
      ]
    }
  },
  {
    "legacy_fact_id": "C14:fixture_event_5:status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_5:status",
      "record_id": "fixture_event_5",
      "facet": "status",
      "value": "เปิดรับสมัคร",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "5/status"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_5:date",
    "C14:fixture_event_5:status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q073 — ข่าว/กิจกรรม

ช่วยตอบสั้น ๆ ว่า กิจกรรมจำลองทดสอบ 11 จัดวันไหน แล้วขอขอรายละเอียดของงาน กิจกรรมจำลองทดสอบ 11

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ

ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_11:date",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_11:date",
      "record_id": "fixture_event_11",
      "facet": "date",
      "value": "2026-11-01",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "11/date"
        }
      ]
    }
  },
  {
    "legacy_fact_id": "C14:fixture_event_11:description",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_11:description",
      "record_id": "fixture_event_11",
      "facet": "description",
      "value": "กิจกรรมจำลอง 11 สำหรับตรวจการอ่านข่าว ไม่ใช่กิจกรรมจริง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "11/description"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_11:date",
    "C14:fixture_event_11:description"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q074 — ข่าว/กิจกรรม

อยากรู้ว่า ขอรายละเอียดของงาน กิจกรรมจำลองทดสอบ 12 แล้วขอสถานะการรับสมัคร กิจกรรมจำลองทดสอบ 12 เป็นอย่างไร

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ

ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_12:description",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_12:description",
      "record_id": "fixture_event_12",
      "facet": "description",
      "value": "กิจกรรมจำลอง 12 สำหรับตรวจการอ่านข่าว ไม่ใช่กิจกรรมจริง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "12/description"
        }
      ]
    }
  },
  {
    "legacy_fact_id": "C14:fixture_event_12:status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_12:status",
      "record_id": "fixture_event_12",
      "facet": "status",
      "value": "ปิดรับสมัครแล้ว",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "12/status"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_12:description",
    "C14:fixture_event_12:status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q075 — ข่าว/กิจกรรม

กำลังวางแผนไปใช้บริการ เลยขอถามว่า มีช่องทางลงทะเบียน กิจกรรมจำลองทดสอบ 12 ไหม แล้วของาน กิจกรรมจำลองทดสอบ 12 ยังสมัครได้ไหม

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังยืนยันคำตอบให้ครบตามสถานการณ์ที่ถามไม่ได้ครับ กรุณาระบุรายละเอียดหรือแยกคำถามเพิ่มเติมอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ

ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_12:registration",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_12:registration",
      "record_id": "fixture_event_12",
      "facet": "registration",
      "value": "https://example.invalid/test-registration/12",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "12/registration"
        }
      ]
    }
  },
  {
    "legacy_fact_id": "C14:fixture_event_12:status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_12:status",
      "record_id": "fixture_event_12",
      "facet": "status",
      "value": "ปิดรับสมัครแล้ว",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "12/status"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_12:registration",
    "C14:fixture_event_12:status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q076 — ข่าว/กิจกรรม

รบกวนเช็กให้หน่อย จะสมัคร กิจกรรมจำลองทดสอบ 07 ได้จากลิงก์ไหน แล้วขอกิจกรรมจำลองทดสอบ 07 ปิดรับสมัครหรือยัง

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ

ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_7:registration",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_7:registration",
      "record_id": "fixture_event_7",
      "facet": "registration",
      "value": "https://example.invalid/test-registration/07",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "7/registration"
        }
      ]
    }
  },
  {
    "legacy_fact_id": "C14:fixture_event_7:status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_7:status",
      "record_id": "fixture_event_7",
      "facet": "status",
      "value": "เปิดรับสมัคร",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "7/status"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_7:registration",
    "C14:fixture_event_7:status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q077 — ข่าว/กิจกรรม

ถามจากข้อมูลที่ศูนย์ให้ไว้ ขอรายละเอียดของงาน กิจกรรมจำลองทดสอบ 02 แล้วขออยากไป กิจกรรมจำลองทดสอบ 02 ต้องไปวันไหน

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ

ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_2:description",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_2:description",
      "record_id": "fixture_event_2",
      "facet": "description",
      "value": "กิจกรรมจำลอง 02 สำหรับตรวจการอ่านข่าว ไม่ใช่กิจกรรมจริง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "2/description"
        }
      ]
    }
  },
  {
    "legacy_fact_id": "C14:fixture_event_2:date",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_2:date",
      "record_id": "fixture_event_2",
      "facet": "date",
      "value": "2026-10-23",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "2/date"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_2:description",
    "C14:fixture_event_2:date"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q078 — ข่าว/กิจกรรม

กิจกรรมจำลองทดสอบ 09 จัดเกี่ยวกับอะไร แล้วขอจะสมัคร กิจกรรมจำลองทดสอบ 09 ได้จากลิงก์ไหน

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ

ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_9:description",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_9:description",
      "record_id": "fixture_event_9",
      "facet": "description",
      "value": "กิจกรรมจำลอง 09 สำหรับตรวจการอ่านข่าว ไม่ใช่กิจกรรมจริง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "9/description"
        }
      ]
    }
  },
  {
    "legacy_fact_id": "C14:fixture_event_9:registration",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_9:registration",
      "record_id": "fixture_event_9",
      "facet": "registration",
      "value": "https://example.invalid/test-registration/09",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "9/registration"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_9:description",
    "C14:fixture_event_9:registration"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q079 — ข่าว/กิจกรรม

ขอสอบถามหน่อยครับ จะสมัคร กิจกรรมจำลองทดสอบ 11 ได้จากลิงก์ไหน แล้วขอขอรายละเอียดของงาน กิจกรรมจำลองทดสอบ 11

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ

ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_11:registration",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_11:registration",
      "record_id": "fixture_event_11",
      "facet": "registration",
      "value": "https://example.invalid/test-registration/11",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "11/registration"
        }
      ]
    }
  },
  {
    "legacy_fact_id": "C14:fixture_event_11:description",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_11:description",
      "record_id": "fixture_event_11",
      "facet": "description",
      "value": "กิจกรรมจำลอง 11 สำหรับตรวจการอ่านข่าว ไม่ใช่กิจกรรมจริง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "11/description"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_11:registration",
    "C14:fixture_event_11:description"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q080 — ข่าว/กิจกรรม

ช่วยตอบสั้น ๆ ว่า วันจัดงาน กิจกรรมจำลองทดสอบ 07 คือวันที่เท่าไร แล้วขอสถานะการรับสมัคร กิจกรรมจำลองทดสอบ 07 เป็นอย่างไร

Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy

ก่อน: strict=False, fixture_not_in_native_source, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=False, fixture_not_in_native_source, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ

ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[
  {
    "legacy_fact_id": "C14:fixture_event_7:date",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_7:date",
      "record_id": "fixture_event_7",
      "facet": "date",
      "value": "2026-10-28",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "7/date"
        }
      ]
    }
  },
  {
    "legacy_fact_id": "C14:fixture_event_7:status",
    "alignment_kind": "fixture_absent_from_native",
    "legacy_expected": {
      "fact_id": "C14:fixture_event_7:status",
      "record_id": "fixture_event_7",
      "facet": "status",
      "value": "เปิดรับสมัคร",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "fixture:news",
          "locator": "7/status"
        }
      ]
    }
  }
]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [
    "C14:fixture_event_7:date",
    "C14:fixture_event_7:status"
  ],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q081 — ข่าว/กิจกรรม

รบกวนเช็กให้หน่อย กิจกรรมจริงที่ไม่ได้อยู่ในข้อมูลเปิดรับกี่ทีม

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, expected_state_mismatch, state=missing_input

```text
ยังยืนยันคำตอบให้ครบตามสถานการณ์ที่ถามไม่ได้ครับ กรุณาระบุรายละเอียดหรือแยกคำถามเพิ่มเติมอีกนิด
```

หลัง: strict=True, source_contract_pass, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q082 — ข่าว/กิจกรรม

ถามจากข้อมูลที่ศูนย์ให้ไว้ ขอข่าวจริงล่าสุดของศูนย์ที่ยืนยันจากระบบสดวันนี้

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, expected_state_mismatch, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=True, source_contract_pass, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q084 — ข่าว/กิจกรรม

ถามจากข้อมูลที่ศูนย์ให้ไว้ กิจกรรมจริงที่ไม่ได้อยู่ในข้อมูลเปิดรับกี่ทีม

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, expected_state_mismatch, state=missing_input

```text
ยังยืนยันคำตอบให้ครบตามสถานการณ์ที่ถามไม่ได้ครับ กรุณาระบุรายละเอียดหรือแยกคำถามเพิ่มเติมอีกนิด
```

หลัง: strict=True, source_contract_pass, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q085 — ข่าว/กิจกรรม

ขอข่าวจริงล่าสุดของศูนย์ที่ยืนยันจากระบบสดวันนี้

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, expected_state_mismatch, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=True, source_contract_pass, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q087 — ข่าว/กิจกรรม

กิจกรรมจริงที่ไม่ได้อยู่ในข้อมูลเปิดรับกี่ทีม

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, expected_state_mismatch, state=missing_input

```text
ยังยืนยันคำตอบให้ครบตามสถานการณ์ที่ถามไม่ได้ครับ กรุณาระบุรายละเอียดหรือแยกคำถามเพิ่มเติมอีกนิด
```

หลัง: strict=True, source_contract_pass, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q088 — ข่าว/กิจกรรม

ขอสอบถามหน่อยครับ ขอข่าวจริงล่าสุดของศูนย์ที่ยืนยันจากระบบสดวันนี้

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, expected_state_mismatch, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=True, source_contract_pass, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q090 — ข่าว/กิจกรรม

ขอสอบถามหน่อยครับ กิจกรรมจริงที่ไม่ได้อยู่ในข้อมูลเปิดรับกี่ทีม

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, expected_state_mismatch, state=missing_input

```text
ยังยืนยันคำตอบให้ครบตามสถานการณ์ที่ถามไม่ได้ครับ กรุณาระบุรายละเอียดหรือแยกคำถามเพิ่มเติมอีกนิด
```

หลัง: strict=True, source_contract_pass, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q091 — ข่าว/กิจกรรม

ช่วยตอบสั้น ๆ ว่า ขอข่าวจริงล่าสุดของศูนย์ที่ยืนยันจากระบบสดวันนี้

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, expected_state_mismatch, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=True, source_contract_pass, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q093 — ข่าว/กิจกรรม

ช่วยตอบสั้น ๆ ว่า กิจกรรมจริงที่ไม่ได้อยู่ในข้อมูลเปิดรับกี่ทีม

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, expected_state_mismatch, state=missing_input

```text
ยังยืนยันคำตอบให้ครบตามสถานการณ์ที่ถามไม่ได้ครับ กรุณาระบุรายละเอียดหรือแยกคำถามเพิ่มเติมอีกนิด
```

หลัง: strict=True, source_contract_pass, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q094 — ข่าว/กิจกรรม

อยากรู้ว่า ขอข่าวจริงล่าสุดของศูนย์ที่ยืนยันจากระบบสดวันนี้

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, expected_state_mismatch, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=True, source_contract_pass, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q096 — ข่าว/กิจกรรม

อยากรู้ว่า กิจกรรมจริงที่ไม่ได้อยู่ในข้อมูลเปิดรับกี่ทีม

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, expected_state_mismatch, state=missing_input

```text
ยังยืนยันคำตอบให้ครบตามสถานการณ์ที่ถามไม่ได้ครับ กรุณาระบุรายละเอียดหรือแยกคำถามเพิ่มเติมอีกนิด
```

หลัง: strict=True, source_contract_pass, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q097 — ข่าว/กิจกรรม

กำลังวางแผนไปใช้บริการ เลยขอถามว่า ขอข่าวจริงล่าสุดของศูนย์ที่ยืนยันจากระบบสดวันนี้

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, expected_state_mismatch, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=True, source_contract_pass, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q099 — ข่าว/กิจกรรม

กำลังวางแผนไปใช้บริการ เลยขอถามว่า กิจกรรมจริงที่ไม่ได้อยู่ในข้อมูลเปิดรับกี่ทีม

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, expected_state_mismatch, state=missing_input

```text
ยังยืนยันคำตอบให้ครบตามสถานการณ์ที่ถามไม่ได้ครับ กรุณาระบุรายละเอียดหรือแยกคำถามเพิ่มเติมอีกนิด
```

หลัง: strict=True, source_contract_pass, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```

## C14-Q100 — ข่าว/กิจกรรม

รบกวนเช็กให้หน่อย ขอข่าวจริงล่าสุดของศูนย์ที่ยืนยันจากระบบสดวันนี้

ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication

ก่อน: strict=False, expected_state_mismatch, state=missing_input

```text
ยังระบุข้อมูลจากชุดที่ย้ายมาให้ตรงคำถามนี้ไม่ได้ครับ กรุณาระบุชื่อเกม อุปกรณ์ หรือหัวข้อที่ต้องการทราบเพิ่มอีกนิด
```

หลัง: strict=True, source_contract_pass, state=missing_source

```text
ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ
```

### Goal/source evidence

```json
[]
```

### หลังแก้: additional/missing/pointer checks

```json
{
  "missing": [],
  "extra": [],
  "wrong": [],
  "evidence_mismatches": [],
  "unknown_refs": [],
  "reference_gaps": [],
  "returned_claim_values_not_literal_in_body": []
}
```
