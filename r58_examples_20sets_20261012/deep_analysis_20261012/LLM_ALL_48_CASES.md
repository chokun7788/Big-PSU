# ผล LLM ทั้ง 48 เคส พร้อมผลดิบและข้อจำกัดที่ปฏิเสธ

27 planner attempts / raw outputs; ไม่มีการเรียกโมเดลซ้ำเพื่อมาแทนผลเดิม

## LLM Case 01 — main case 00626

ถาม: เครื่องทดลอง ละอองฝน เล่นพร้อมกันได้กี่คน

ปิด LLM: False • เปิด LLM: False

คำตอบที่ได้:
```text
players_min: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

ควรตอบ:
```text
คนเล่นพร้อมกันของเครื่อง (capacity_persons): 1
```

ไม่มี planner attempt ในเคสนี้ เพราะ gate ก่อนเรียกดู requested_fields/broad/overview ไม่ได้หมายความว่าโมเดลตอบผิด

Plan สุดท้าย:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_resource_03"
    ],
    "requested_fields": [
      "players_min"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "players_min",
      "status": "unknown"
    }
  ],
  "catalog_scope": "common_published"
}
```

## LLM Case 02 — main case 00627

ถาม: เครื่องทดลอง ละอองฝน เครื่องนี้ให้เล่นพร้อมกันสูงสุดกี่คน

ปิด LLM: False • เปิด LLM: False

คำตอบที่ได้:
```text
players_min: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

ควรตอบ:
```text
คนเล่นพร้อมกันของเครื่อง (capacity_persons): 1
```

ไม่มี planner attempt ในเคสนี้ เพราะ gate ก่อนเรียกดู requested_fields/broad/overview ไม่ได้หมายความว่าโมเดลตอบผิด

Plan สุดท้าย:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_resource_03"
    ],
    "requested_fields": [
      "players_min"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "players_min",
      "status": "unknown"
    }
  ],
  "catalog_scope": "common_published"
}
```

## LLM Case 03 — main case 00628

ถาม: แล้วเล่นพร้อมกันได้กี่คน

ปิด LLM: False • เปิด LLM: False

คำตอบที่ได้:
```text
players_min: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

ควรตอบ:
```text
คนเล่นพร้อมกันของเครื่อง (capacity_persons): 1
```

ไม่มี planner attempt ในเคสนี้ เพราะ gate ก่อนเรียกดู requested_fields/broad/overview ไม่ได้หมายความว่าโมเดลตอบผิด

Plan สุดท้าย:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_resource_03"
    ],
    "requested_fields": [
      "players_min"
    ],
    "all_fields": false,
    "method": "history_exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "players_min",
      "status": "unknown"
    }
  ],
  "catalog_scope": "common_published"
}
```

## LLM Case 04 — main case 00629

ถาม: เครื่องทดลอง ละอองฝน เครื่องยังใช้งานได้ไหมและรองรับกี่คน

ปิด LLM: False • เปิด LLM: False

คำตอบที่ได้:
```text
players_min: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

ควรตอบ:
```text
สถานะพร้อมใช้งานทางกายภาพ (operational_status): in_service
คนเล่นพร้อมกันของเครื่อง (capacity_persons): 1
```

ไม่มี planner attempt ในเคสนี้ เพราะ gate ก่อนเรียกดู requested_fields/broad/overview ไม่ได้หมายความว่าโมเดลตอบผิด

Plan สุดท้าย:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_resource_03"
    ],
    "requested_fields": [
      "players_min"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "players_min",
      "status": "unknown"
    }
  ],
  "catalog_scope": "common_published"
}
```

## LLM Case 05 — main case 00632

ถาม: Demo station Drizzle How many people can play at once?

ปิด LLM: False • เปิด LLM: True

คำตอบที่ได้:
```text
**Demo station Drizzle**
• capacity persons: 1 [S1]

English translation is machine generated and has not been reviewed by the owner.
```

ควรตอบ:
```text
คนเล่นพร้อมกันของเครื่อง (capacity_persons): 1
```

Planner attempt:
```json
{
  "checked_plan": {
    "requested_fields": [
      "capacity_persons"
    ],
    "all_fields": false,
    "platform": null,
    "method": "bounded_llm_schema_fields"
  },
  "raw_responses": [
    "{\"requested_fields\": [\"capacity_persons\"], \"all_fields\": false, \"platform\": null}"
  ],
  "record_ids": [
    "demo20_resource_03"
  ]
}
```

platform ผ่านข้อกำหนด; ดู accepted checked_plan และผล scorer แยกกัน

Plan สุดท้าย:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_resource_03"
    ],
    "requested_fields": [
      "capacity_persons"
    ],
    "all_fields": false,
    "method": "bounded_llm_schema_fields",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_resource_03",
      "field": "capacity_persons",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/capacity_persons",
          "source_id": "fixture20_demo20_resource_03"
        }
      ]
    }
  ],
  "catalog_scope": "common_published"
}
```

## LLM Case 06 — main case 00633

ถาม: Demo station Drizzle What is the maximum number of users on this station?

ปิด LLM: False • เปิด LLM: False

คำตอบที่ได้:
```text
summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

ควรตอบ:
```text
คนเล่นพร้อมกันของเครื่อง (capacity_persons): 1
```

ไม่มี planner attempt ในเคสนี้ เพราะ gate ก่อนเรียกดู requested_fields/broad/overview ไม่ได้หมายความว่าโมเดลตอบผิด

Plan สุดท้าย:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_resource_03"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
      "status": "unknown"
    }
  ],
  "catalog_scope": "common_published"
}
```

## LLM Case 07 — main case 00634

ถาม: And How many people can play at once?

ปิด LLM: False • เปิด LLM: False

คำตอบที่ได้:
```text
[None]
```

ควรตอบ:
```text
คนเล่นพร้อมกันของเครื่อง (capacity_persons): 1
```

ไม่มี planner attempt ในเคสนี้ เพราะ gate ก่อนเรียกดู requested_fields/broad/overview ไม่ได้หมายความว่าโมเดลตอบผิด

Plan สุดท้าย:
```json
null
```

## LLM Case 08 — main case 00635

ถาม: Demo station Drizzle Is this station in service and how many people can use it?

ปิด LLM: False • เปิด LLM: False

คำตอบที่ได้:
```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

ควรตอบ:
```text
สถานะพร้อมใช้งานทางกายภาพ (operational_status): in_service
คนเล่นพร้อมกันของเครื่อง (capacity_persons): 1
```

Planner attempt:
```json
{
  "checked_plan": null,
  "raw_responses": [
    "{\"requested_fields\": [\"operational_status\", \"capacity_persons\"], \"all_fields\": false, \"platform\": \"demo20_resource_03\"}"
  ],
  "record_ids": [
    "demo20_resource_03"
  ]
}
```

ปฏิเสธเพราะ platform='demo20_resource_03' ไม่อยู่ใน ['Cockpit', 'Nintendo Switch', 'PC', 'PS5', 'VR'] และไม่ใช่ null; checked_plan คืน None แม้บาง requested_fields ถูกแล้ว

Plan สุดท้าย:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_resource_03"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
  "catalog_scope": "common_published"
}
```

## LLM Case 09 — main case 00866

ถาม: รอบทดลอง ละอองฝน หนึ่งรอบเล่นได้กี่นาที

ปิด LLM: False • เปิด LLM: False

คำตอบที่ได้:
```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

ควรตอบ:
```text
เวลาเล่นต่อรอบ (นาที) (session_minutes): 30
```

Planner attempt:
```json
{
  "checked_plan": null,
  "raw_responses": [
    "{\"requested_fields\": [\"session_minutes\"], \"all_fields\": false, \"platform\": \"service\"}"
  ],
  "record_ids": [
    "demo20_service_03"
  ]
}
```

ปฏิเสธเพราะ platform='service' ไม่อยู่ใน ['Cockpit', 'Nintendo Switch', 'PC', 'PS5', 'VR'] และไม่ใช่ null; checked_plan คืน None แม้บาง requested_fields ถูกแล้ว

Plan สุดท้าย:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_service_03"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
  "catalog_scope": "common_published"
}
```

## LLM Case 10 — main case 00867

ถาม: รอบทดลอง ละอองฝน จองหนึ่งรอบได้เวลาเล่นเท่าไร

ปิด LLM: False • เปิด LLM: False

คำตอบที่ได้:
```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

ควรตอบ:
```text
เวลาเล่นต่อรอบ (นาที) (session_minutes): 30
```

Planner attempt:
```json
{
  "checked_plan": null,
  "raw_responses": [
    "{\"requested_fields\": [\"session_minutes\"], \"all_fields\": false, \"platform\": \"service\"}"
  ],
  "record_ids": [
    "demo20_service_03"
  ]
}
```

ปฏิเสธเพราะ platform='service' ไม่อยู่ใน ['Cockpit', 'Nintendo Switch', 'PC', 'PS5', 'VR'] และไม่ใช่ null; checked_plan คืน None แม้บาง requested_fields ถูกแล้ว

Plan สุดท้าย:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_service_03"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
  "catalog_scope": "common_published"
}
```

## LLM Case 11 — main case 00868

ถาม: แล้วหนึ่งรอบเล่นได้กี่นาที

ปิด LLM: False • เปิด LLM: False

คำตอบที่ได้:
```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

ควรตอบ:
```text
เวลาเล่นต่อรอบ (นาที) (session_minutes): 30
```

Planner attempt:
```json
{
  "checked_plan": null,
  "raw_responses": [
    "{\"requested_fields\": [\"session_minutes\"], \"all_fields\": false, \"platform\": \"service\"}"
  ],
  "record_ids": [
    "demo20_service_03"
  ]
}
```

ปฏิเสธเพราะ platform='service' ไม่อยู่ใน ['Cockpit', 'Nintendo Switch', 'PC', 'PS5', 'VR'] และไม่ใช่ null; checked_plan คืน None แม้บาง requested_fields ถูกแล้ว

Plan สุดท้าย:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_service_03"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "history_exact:pending_fields",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
  "catalog_scope": "common_published"
}
```

## LLM Case 12 — main case 00869

ถาม: รอบทดลอง ละอองฝน เวลาเล่นกับเวลาที่กินช่องจองกี่นาที

ปิด LLM: False • เปิด LLM: False

คำตอบที่ได้:
```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

ควรตอบ:
```text
เวลาเล่นต่อรอบ (นาที) (session_minutes): 30
เวลาที่กันช่องจอง (นาที) (occupancy_minutes): 60
```

Planner attempt:
```json
{
  "checked_plan": null,
  "raw_responses": [
    "{\"requested_fields\": [\"session_minutes\"], \"all_fields\": false, \"platform\": \"service\"}"
  ],
  "record_ids": [
    "demo20_service_03"
  ]
}
```

ปฏิเสธเพราะ platform='service' ไม่อยู่ใน ['Cockpit', 'Nintendo Switch', 'PC', 'PS5', 'VR'] และไม่ใช่ null; checked_plan คืน None แม้บาง requested_fields ถูกแล้ว

Plan สุดท้าย:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_service_03"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
  "catalog_scope": "common_published"
}
```

## LLM Case 13 — main case 00872

ถาม: Demo session Drizzle How many minutes does one session last?

ปิด LLM: False • เปิด LLM: False

คำตอบที่ได้:
```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

ควรตอบ:
```text
เวลาเล่นต่อรอบ (นาที) (session_minutes): 30
```

Planner attempt:
```json
{
  "checked_plan": null,
  "raw_responses": [
    "{\"requested_fields\": [\"session_minutes\"], \"all_fields\": false, \"platform\": \"service\"}"
  ],
  "record_ids": [
    "demo20_service_03"
  ]
}
```

ปฏิเสธเพราะ platform='service' ไม่อยู่ใน ['Cockpit', 'Nintendo Switch', 'PC', 'PS5', 'VR'] และไม่ใช่ null; checked_plan คืน None แม้บาง requested_fields ถูกแล้ว

Plan สุดท้าย:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_service_03"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
  "catalog_scope": "common_published"
}
```

## LLM Case 14 — main case 00873

ถาม: Demo session Drizzle How long can I play in one session?

ปิด LLM: False • เปิด LLM: False

คำตอบที่ได้:
```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

ควรตอบ:
```text
เวลาเล่นต่อรอบ (นาที) (session_minutes): 30
```

Planner attempt:
```json
{
  "checked_plan": null,
  "raw_responses": [
    "{\"requested_fields\": [\"session_minutes\"], \"all_fields\": false, \"platform\": \"service\"}"
  ],
  "record_ids": [
    "demo20_service_03"
  ]
}
```

ปฏิเสธเพราะ platform='service' ไม่อยู่ใน ['Cockpit', 'Nintendo Switch', 'PC', 'PS5', 'VR'] และไม่ใช่ null; checked_plan คืน None แม้บาง requested_fields ถูกแล้ว

Plan สุดท้าย:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_service_03"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
  "catalog_scope": "common_published"
}
```

## LLM Case 15 — main case 00874

ถาม: And How many minutes does one session last?

ปิด LLM: False • เปิด LLM: False

คำตอบที่ได้:
```text
[None]
```

ควรตอบ:
```text
เวลาเล่นต่อรอบ (นาที) (session_minutes): 30
```

ไม่มี planner attempt ในเคสนี้ เพราะ gate ก่อนเรียกดู requested_fields/broad/overview ไม่ได้หมายความว่าโมเดลตอบผิด

Plan สุดท้าย:
```json
null
```

## LLM Case 16 — main case 00875

ถาม: Demo session Drizzle What are the play duration and booking occupancy in minutes?

ปิด LLM: False • เปิด LLM: False

คำตอบที่ได้:
```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

ควรตอบ:
```text
เวลาเล่นต่อรอบ (นาที) (session_minutes): 30
เวลาที่กันช่องจอง (นาที) (occupancy_minutes): 60
```

Planner attempt:
```json
{
  "checked_plan": null,
  "raw_responses": [
    "{\"requested_fields\": [\"session_minutes\", \"occupancy_minutes\"], \"all_fields\": false, \"platform\": \"service\"}"
  ],
  "record_ids": [
    "demo20_service_03"
  ]
}
```

ปฏิเสธเพราะ platform='service' ไม่อยู่ใน ['Cockpit', 'Nintendo Switch', 'PC', 'PS5', 'VR'] และไม่ใช่ null; checked_plan คืน None แม้บาง requested_fields ถูกแล้ว

Plan สุดท้าย:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_service_03"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
  "catalog_scope": "common_published"
}
```

## LLM Case 17 — main case 01346

ถาม: กลุ่มผู้ใช้ ละอองฝน ต้องใช้หลักฐานอะไร

ปิด LLM: False • เปิด LLM: False

คำตอบที่ได้:
```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

ควรตอบ:
```text
หลักฐานที่ต้องแสดง (required_proofs): • DEMO pass Drizzle
```

Planner attempt:
```json
{
  "checked_plan": null,
  "raw_responses": [
    "{\"requested_fields\": [\"required_proofs\"], \"all_fields\": false, \"platform\": \"demo20_audience_03\"}"
  ],
  "record_ids": [
    "demo20_audience_03"
  ]
}
```

ปฏิเสธเพราะ platform='demo20_audience_03' ไม่อยู่ใน ['Cockpit', 'Nintendo Switch', 'PC', 'PS5', 'VR'] และไม่ใช่ null; checked_plan คืน None แม้บาง requested_fields ถูกแล้ว

Plan สุดท้าย:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_audience_03"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
  "catalog_scope": "common_published"
}
```

## LLM Case 18 — main case 01347

ถาม: กลุ่มผู้ใช้ ละอองฝน ต้องเอาเอกสารอะไรมาแสดง

ปิด LLM: False • เปิด LLM: False

คำตอบที่ได้:
```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

ควรตอบ:
```text
หลักฐานที่ต้องแสดง (required_proofs): • DEMO pass Drizzle
```

Planner attempt:
```json
{
  "checked_plan": null,
  "raw_responses": [
    "{\"requested_fields\": [\"required_proofs\"], \"all_fields\": false, \"platform\": \"unknown\"}"
  ],
  "record_ids": [
    "demo20_audience_03"
  ]
}
```

ปฏิเสธเพราะ platform='unknown' ไม่อยู่ใน ['Cockpit', 'Nintendo Switch', 'PC', 'PS5', 'VR'] และไม่ใช่ null; checked_plan คืน None แม้บาง requested_fields ถูกแล้ว

Plan สุดท้าย:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_audience_03"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
  "catalog_scope": "common_published"
}
```

## LLM Case 19 — main case 01348

ถาม: แล้วต้องใช้หลักฐานอะไร

ปิด LLM: False • เปิด LLM: False

คำตอบที่ได้:
```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

ควรตอบ:
```text
หลักฐานที่ต้องแสดง (required_proofs): • DEMO pass Drizzle
```

Planner attempt:
```json
{
  "checked_plan": null,
  "raw_responses": [
    "{\"requested_fields\": [\"required_proofs\"], \"all_fields\": false, \"platform\": \"unknown\"}"
  ],
  "record_ids": [
    "demo20_audience_03"
  ]
}
```

ปฏิเสธเพราะ platform='unknown' ไม่อยู่ใน ['Cockpit', 'Nintendo Switch', 'PC', 'PS5', 'VR'] และไม่ใช่ null; checked_plan คืน None แม้บาง requested_fields ถูกแล้ว

Plan สุดท้าย:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_audience_03"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "history_exact:pending_fields",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
  "catalog_scope": "common_published"
}
```

## LLM Case 20 — main case 01349

ถาม: กลุ่มผู้ใช้ ละอองฝน ใครใช้สิทธิ์กลุ่มนี้ได้และต้องแสดงหลักฐานอะไร

ปิด LLM: False • เปิด LLM: False

คำตอบที่ได้:
```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

ควรตอบ:
```text
ผู้ที่ใช้สิทธิ์ได้ (eligibility): ผู้ใช้สมมุติกลุ่ม 3: ใช้บริการตามรอบทดลอง
หลักฐานที่ต้องแสดง (required_proofs): • DEMO pass Drizzle
```

Planner attempt:
```json
{
  "checked_plan": null,
  "raw_responses": [
    "{\"requested_fields\": [\"eligibility\", \"required_proofs\"], \"all_fields\": false, \"platform\": \"unknown\"}"
  ],
  "record_ids": [
    "demo20_audience_03"
  ]
}
```

ปฏิเสธเพราะ platform='unknown' ไม่อยู่ใน ['Cockpit', 'Nintendo Switch', 'PC', 'PS5', 'VR'] และไม่ใช่ null; checked_plan คืน None แม้บาง requested_fields ถูกแล้ว

Plan สุดท้าย:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_audience_03"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
  "catalog_scope": "common_published"
}
```

## LLM Case 21 — main case 01352

ถาม: Demo visitors Drizzle What proof is required?

ปิด LLM: False • เปิด LLM: False

คำตอบที่ได้:
```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

ควรตอบ:
```text
หลักฐานที่ต้องแสดง (required_proofs): • DEMO pass Drizzle
```

Planner attempt:
```json
{
  "checked_plan": null,
  "raw_responses": [
    "{\"requested_fields\": [\"required_proofs\"], \"all_fields\": false, \"platform\": \"demo20_audience_03\"}"
  ],
  "record_ids": [
    "demo20_audience_03"
  ]
}
```

ปฏิเสธเพราะ platform='demo20_audience_03' ไม่อยู่ใน ['Cockpit', 'Nintendo Switch', 'PC', 'PS5', 'VR'] และไม่ใช่ null; checked_plan คืน None แม้บาง requested_fields ถูกแล้ว

Plan สุดท้าย:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_audience_03"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
  "catalog_scope": "common_published"
}
```

## LLM Case 22 — main case 01353

ถาม: Demo visitors Drizzle Which documents do I need to show?

ปิด LLM: False • เปิด LLM: False

คำตอบที่ได้:
```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

ควรตอบ:
```text
หลักฐานที่ต้องแสดง (required_proofs): • DEMO pass Drizzle
```

Planner attempt:
```json
{
  "checked_plan": null,
  "raw_responses": [
    "{\"requested_fields\": [\"required_proofs\"], \"all_fields\": false, \"platform\": \"demo20_audience_03\"}"
  ],
  "record_ids": [
    "demo20_audience_03"
  ]
}
```

ปฏิเสธเพราะ platform='demo20_audience_03' ไม่อยู่ใน ['Cockpit', 'Nintendo Switch', 'PC', 'PS5', 'VR'] และไม่ใช่ null; checked_plan คืน None แม้บาง requested_fields ถูกแล้ว

Plan สุดท้าย:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_audience_03"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
  "catalog_scope": "common_published"
}
```

## LLM Case 23 — main case 01354

ถาม: And What proof is required?

ปิด LLM: False • เปิด LLM: False

คำตอบที่ได้:
```text
[None]
```

ควรตอบ:
```text
หลักฐานที่ต้องแสดง (required_proofs): • DEMO pass Drizzle
```

ไม่มี planner attempt ในเคสนี้ เพราะ gate ก่อนเรียกดู requested_fields/broad/overview ไม่ได้หมายความว่าโมเดลตอบผิด

Plan สุดท้าย:
```json
null
```

## LLM Case 24 — main case 01355

ถาม: Demo visitors Drizzle Who qualifies for this group and what proof is needed?

ปิด LLM: False • เปิด LLM: False

คำตอบที่ได้:
```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

ควรตอบ:
```text
ผู้ที่ใช้สิทธิ์ได้ (eligibility): Fictional group 3: demo sessions only
หลักฐานที่ต้องแสดง (required_proofs): • DEMO pass Drizzle
```

Planner attempt:
```json
{
  "checked_plan": null,
  "raw_responses": [
    "{\"requested_fields\": [\"name\", \"eligibility\", \"required_proofs\"], \"all_fields\": true, \"platform\": \"demo20_audience_03\"}"
  ],
  "record_ids": [
    "demo20_audience_03"
  ]
}
```

ปฏิเสธเพราะ platform='demo20_audience_03' ไม่อยู่ใน ['Cockpit', 'Nintendo Switch', 'PC', 'PS5', 'VR'] และไม่ใช่ null; checked_plan คืน None แม้บาง requested_fields ถูกแล้ว

Plan สุดท้าย:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_audience_03"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
  "catalog_scope": "common_published"
}
```

## LLM Case 25 — main case 02582

ถาม: โหมดทดลอง ละอองฝน เล่นพร้อมกันได้สูงสุดกี่คน

ปิด LLM: False • เปิด LLM: False

คำตอบที่ได้:
```text
**โหมดทดลอง ละอองฝน**
• จำนวนผู้เล่นขั้นต่ำของโหมด: 1 [S1]
```

ควรตอบ:
```text
จำนวนผู้เล่นสูงสุด (players_max): 1
```

ไม่มี planner attempt ในเคสนี้ เพราะ gate ก่อนเรียกดู requested_fields/broad/overview ไม่ได้หมายความว่าโมเดลตอบผิด

Plan สุดท้าย:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_mode_03"
    ],
    "requested_fields": [
      "players_min"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_game_mode_03",
      "field": "players_min",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/players_min",
          "source_id": "fixture20_demo20_game_mode_03"
        }
      ]
    }
  ],
  "catalog_scope": "common_published"
}
```

## LLM Case 26 — main case 02583

ถาม: โหมดทดลอง ละอองฝน คนเล่นได้เยอะสุดเท่าไหร่

ปิด LLM: False • เปิด LLM: False

คำตอบที่ได้:
```text
ยังไม่มีราคาที่ได้รับการยืนยันในขอบเขตนี้

amount_minor: ยังไม่มีข้อมูลยืนยันสำหรับขอบเขตนี้
```

ควรตอบ:
```text
จำนวนผู้เล่นสูงสุด (players_max): 1
```

ไม่มี planner attempt ในเคสนี้ เพราะ gate ก่อนเรียกดู requested_fields/broad/overview ไม่ได้หมายความว่าโมเดลตอบผิด

Plan สุดท้าย:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_mode_03"
    ],
    "requested_fields": [
      "amount_minor"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "amount_minor",
      "status": "unknown"
    }
  ],
  "catalog_scope": "common_published"
}
```

## LLM Case 27 — main case 02584

ถาม: แล้วเล่นพร้อมกันได้สูงสุดกี่คน

ปิด LLM: False • เปิด LLM: False

คำตอบที่ได้:
```text
**โหมดทดลอง ละอองฝน**
• จำนวนผู้เล่นขั้นต่ำของโหมด: 1 [S1]
```

ควรตอบ:
```text
จำนวนผู้เล่นสูงสุด (players_max): 1
```

ไม่มี planner attempt ในเคสนี้ เพราะ gate ก่อนเรียกดู requested_fields/broad/overview ไม่ได้หมายความว่าโมเดลตอบผิด

Plan สุดท้าย:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_mode_03"
    ],
    "requested_fields": [
      "players_min"
    ],
    "all_fields": false,
    "method": "history_exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_game_mode_03",
      "field": "players_min",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/players_min",
          "source_id": "fixture20_demo20_game_mode_03"
        }
      ]
    }
  ],
  "catalog_scope": "common_published"
}
```

## LLM Case 28 — main case 02585

ถาม: โหมดทดลอง ละอองฝน ต้องมีขั้นต่ำกี่คนและเล่นได้สูงสุดกี่คน

ปิด LLM: False • เปิด LLM: False

คำตอบที่ได้:
```text
**โหมดทดลอง ละอองฝน**
• จำนวนผู้เล่นขั้นต่ำของโหมด: 1 [S1]
```

ควรตอบ:
```text
จำนวนผู้เล่นขั้นต่ำ (players_min): 1
จำนวนผู้เล่นสูงสุด (players_max): 1
```

ไม่มี planner attempt ในเคสนี้ เพราะ gate ก่อนเรียกดู requested_fields/broad/overview ไม่ได้หมายความว่าโมเดลตอบผิด

Plan สุดท้าย:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_mode_03"
    ],
    "requested_fields": [
      "players_min"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_game_mode_03",
      "field": "players_min",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/players_min",
          "source_id": "fixture20_demo20_game_mode_03"
        }
      ]
    }
  ],
  "catalog_scope": "common_published"
}
```

## LLM Case 29 — main case 02587

ถาม: Demo mode Drizzle How many people can play together at most?

ปิด LLM: False • เปิด LLM: False

คำตอบที่ได้:
```text
**Demo mode Drizzle**
• players min: 1 [S1]

English translation is machine generated and has not been reviewed by the owner.
```

ควรตอบ:
```text
จำนวนผู้เล่นสูงสุด (players_max): 1
```

ไม่มี planner attempt ในเคสนี้ เพราะ gate ก่อนเรียกดู requested_fields/broad/overview ไม่ได้หมายความว่าโมเดลตอบผิด

Plan สุดท้าย:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_mode_03"
    ],
    "requested_fields": [
      "players_min"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_game_mode_03",
      "field": "players_min",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/players_min",
          "source_id": "fixture20_demo20_game_mode_03"
        }
      ]
    }
  ],
  "catalog_scope": "common_published"
}
```

## LLM Case 30 — main case 02588

ถาม: Demo mode Drizzle What is the maximum player count?

ปิด LLM: False • เปิด LLM: False

คำตอบที่ได้:
```text
summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

ควรตอบ:
```text
จำนวนผู้เล่นสูงสุด (players_max): 1
```

ไม่มี planner attempt ในเคสนี้ เพราะ gate ก่อนเรียกดู requested_fields/broad/overview ไม่ได้หมายความว่าโมเดลตอบผิด

Plan สุดท้าย:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_mode_03"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
      "status": "unknown"
    }
  ],
  "catalog_scope": "common_published"
}
```

## LLM Case 31 — main case 02589

ถาม: And How many people can play together at most?

ปิด LLM: False • เปิด LLM: False

คำตอบที่ได้:
```text
**Demo mode Drizzle**
• players min: 1 [S1]

English translation is machine generated and has not been reviewed by the owner.
```

ควรตอบ:
```text
จำนวนผู้เล่นสูงสุด (players_max): 1
```

ไม่มี planner attempt ในเคสนี้ เพราะ gate ก่อนเรียกดู requested_fields/broad/overview ไม่ได้หมายความว่าโมเดลตอบผิด

Plan สุดท้าย:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_mode_03"
    ],
    "requested_fields": [
      "players_min"
    ],
    "all_fields": false,
    "method": "history_exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_game_mode_03",
      "field": "players_min",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/players_min",
          "source_id": "fixture20_demo20_game_mode_03"
        }
      ]
    }
  ],
  "catalog_scope": "common_published"
}
```

## LLM Case 32 — main case 02590

ถาม: Demo mode Drizzle What are the minimum and maximum player counts?

ปิด LLM: False • เปิด LLM: True

คำตอบที่ได้:
```text
**Demo mode Drizzle**
• players min: 1 [S1]
• players max: 1 [S2]

English translation is machine generated and has not been reviewed by the owner.
```

ควรตอบ:
```text
จำนวนผู้เล่นขั้นต่ำ (players_min): 1
จำนวนผู้เล่นสูงสุด (players_max): 1
```

Planner attempt:
```json
{
  "checked_plan": {
    "requested_fields": [
      "players_min",
      "players_max"
    ],
    "all_fields": false,
    "platform": null,
    "method": "bounded_llm_schema_fields"
  },
  "raw_responses": [
    "{\"requested_fields\": [\"players_min\", \"players_max\"], \"all_fields\": false, \"platform\": null}"
  ],
  "record_ids": [
    "demo20_game_mode_03"
  ]
}
```

platform ผ่านข้อกำหนด; ดู accepted checked_plan และผล scorer แยกกัน

Plan สุดท้าย:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_game_mode_03"
    ],
    "requested_fields": [
      "players_min",
      "players_max"
    ],
    "all_fields": false,
    "method": "bounded_llm_schema_fields",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_game_mode_03",
      "field": "players_min",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/players_min",
          "source_id": "fixture20_demo20_game_mode_03"
        }
      ]
    },
    {
      "record_id": "demo20_game_mode_03",
      "field": "players_max",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/players_max",
          "source_id": "fixture20_demo20_game_mode_03"
        }
      ]
    }
  ],
  "catalog_scope": "common_published"
}
```

## LLM Case 33 — main case 03582

ถาม: ประกาศวันทดลอง ละอองฝน วันนั้นปิดไหม

ปิด LLM: False • เปิด LLM: False

คำตอบที่ได้:
```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

ควรตอบ:
```text
สถานะวันพิเศษ (state): closed
```

Planner attempt:
```json
{
  "checked_plan": null,
  "raw_responses": [
    "{\"requested_fields\": [\"local_date\", \"zone_ids\", \"state\", \"open_periods\", \"bookable_periods\", \"reason\", \"resolution_policy_id\"], \"all_fields\": false, \"platform\": \"demo20_closure_03\"}"
  ],
  "record_ids": [
    "demo20_closure_03"
  ]
}
```

ปฏิเสธเพราะ platform='demo20_closure_03' ไม่อยู่ใน ['Cockpit', 'Nintendo Switch', 'PC', 'PS5', 'VR'] และไม่ใช่ null; checked_plan คืน None แม้บาง requested_fields ถูกแล้ว

Plan สุดท้าย:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_closure_03"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
  "catalog_scope": "common_published"
}
```

## LLM Case 34 — main case 03583

ถาม: ประกาศวันทดลอง ละอองฝน วันนี้ในประกาศเปิดหรือปิด

ปิด LLM: False • เปิด LLM: False

คำตอบที่ได้:
```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

ควรตอบ:
```text
สถานะวันพิเศษ (state): closed
```

Planner attempt:
```json
{
  "checked_plan": null,
  "raw_responses": [
    "{\"requested_fields\": [\"state\"], \"all_fields\": false, \"platform\": \"demo20_closure_03\"}"
  ],
  "record_ids": [
    "demo20_closure_03"
  ]
}
```

ปฏิเสธเพราะ platform='demo20_closure_03' ไม่อยู่ใน ['Cockpit', 'Nintendo Switch', 'PC', 'PS5', 'VR'] และไม่ใช่ null; checked_plan คืน None แม้บาง requested_fields ถูกแล้ว

Plan สุดท้าย:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_closure_03"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
  "catalog_scope": "common_published"
}
```

## LLM Case 35 — main case 03584

ถาม: แล้ววันนั้นปิดไหม

ปิด LLM: False • เปิด LLM: False

คำตอบที่ได้:
```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

ควรตอบ:
```text
สถานะวันพิเศษ (state): closed
```

Planner attempt:
```json
{
  "checked_plan": null,
  "raw_responses": [
    "{\"requested_fields\": [\"local_date\", \"zone_ids\", \"state\", \"open_periods\", \"bookable_periods\", \"reason\", \"resolution_policy_id\"], \"all_fields\": false, \"platform\": \"demo20_closure_03\"}"
  ],
  "record_ids": [
    "demo20_closure_03"
  ]
}
```

ปฏิเสธเพราะ platform='demo20_closure_03' ไม่อยู่ใน ['Cockpit', 'Nintendo Switch', 'PC', 'PS5', 'VR'] และไม่ใช่ null; checked_plan คืน None แม้บาง requested_fields ถูกแล้ว

Plan สุดท้าย:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_closure_03"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "history_exact:pending_fields",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
  "catalog_scope": "common_published"
}
```

## LLM Case 36 — main case 03585

ถาม: ประกาศวันทดลอง ละอองฝน วันนั้นเปิดปิดยังไงและเพราะอะไร

ปิด LLM: False • เปิด LLM: False

คำตอบที่ได้:
```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

ควรตอบ:
```text
สถานะวันพิเศษ (state): closed
เหตุผล (reason): ประกาศสมมุติ ละอองฝน: closed
```

Planner attempt:
```json
{
  "checked_plan": null,
  "raw_responses": [
    "{\"requested_fields\": [\"local_date\", \"zone_ids\", \"state\", \"open_periods\", \"bookable_periods\", \"reason\", \"resolution_policy_id\"], \"all_fields\": false, \"platform\": \"demo20_closure_03\"}"
  ],
  "record_ids": [
    "demo20_closure_03"
  ]
}
```

ปฏิเสธเพราะ platform='demo20_closure_03' ไม่อยู่ใน ['Cockpit', 'Nintendo Switch', 'PC', 'PS5', 'VR'] และไม่ใช่ null; checked_plan คืน None แม้บาง requested_fields ถูกแล้ว

Plan สุดท้าย:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_closure_03"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
  "catalog_scope": "common_published"
}
```

## LLM Case 37 — main case 03587

ถาม: Demo date notice Drizzle Is it closed on that date?

ปิด LLM: False • เปิด LLM: False

คำตอบที่ได้:
```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

ควรตอบ:
```text
สถานะวันพิเศษ (state): closed
```

Planner attempt:
```json
{
  "checked_plan": null,
  "raw_responses": [
    "{\"requested_fields\": [\"local_date\", \"zone_ids\", \"state\", \"open_periods\", \"bookable_periods\", \"reason\", \"resolution_policy_id\"], \"all_fields\": false, \"platform\": \"demo20_closure_03\"}"
  ],
  "record_ids": [
    "demo20_closure_03"
  ]
}
```

ปฏิเสธเพราะ platform='demo20_closure_03' ไม่อยู่ใน ['Cockpit', 'Nintendo Switch', 'PC', 'PS5', 'VR'] และไม่ใช่ null; checked_plan คืน None แม้บาง requested_fields ถูกแล้ว

Plan สุดท้าย:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_closure_03"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
  "catalog_scope": "common_published"
}
```

## LLM Case 38 — main case 03588

ถาม: Demo date notice Drizzle Does this date notice say open or closed?

ปิด LLM: False • เปิด LLM: False

คำตอบที่ได้:
```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

ควรตอบ:
```text
สถานะวันพิเศษ (state): closed
```

Planner attempt:
```json
{
  "checked_plan": null,
  "raw_responses": [
    "{\"requested_fields\": [\"state\"], \"all_fields\": false, \"platform\": \"demo20_closure_03\"}"
  ],
  "record_ids": [
    "demo20_closure_03"
  ]
}
```

ปฏิเสธเพราะ platform='demo20_closure_03' ไม่อยู่ใน ['Cockpit', 'Nintendo Switch', 'PC', 'PS5', 'VR'] และไม่ใช่ null; checked_plan คืน None แม้บาง requested_fields ถูกแล้ว

Plan สุดท้าย:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_closure_03"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
  "catalog_scope": "common_published"
}
```

## LLM Case 39 — main case 03589

ถาม: And Is it closed on that date?

ปิด LLM: False • เปิด LLM: False

คำตอบที่ได้:
```text
summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

ควรตอบ:
```text
สถานะวันพิเศษ (state): closed
```

ไม่มี planner attempt ในเคสนี้ เพราะ gate ก่อนเรียกดู requested_fields/broad/overview ไม่ได้หมายความว่าโมเดลตอบผิด

Plan สุดท้าย:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_closure_03"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "history_exact:pending_fields",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
      "status": "unknown"
    }
  ],
  "catalog_scope": "common_published"
}
```

## LLM Case 40 — main case 03590

ถาม: Demo date notice Drizzle What is the opening status on that date and why?

ปิด LLM: False • เปิด LLM: False

คำตอบที่ได้:
```text
summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

ควรตอบ:
```text
สถานะวันพิเศษ (state): closed
เหตุผล (reason): Synthetic Drizzle date notice: closed
```

ไม่มี planner attempt ในเคสนี้ เพราะ gate ก่อนเรียกดู requested_fields/broad/overview ไม่ได้หมายความว่าโมเดลตอบผิด

Plan สุดท้าย:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_closure_03"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
      "status": "unknown"
    }
  ],
  "catalog_scope": "common_published"
}
```

## LLM Case 41 — main case 03982

ถาม: ข้อการแข่งขันทดลอง ละอองฝน ข้อนี้กำหนดอะไร

ปิด LLM: False • เปิด LLM: False

คำตอบที่ได้:
```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

ควรตอบ:
```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 3: พักเมื่อเวียนหัว ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

Planner attempt:
```json
{
  "checked_plan": null,
  "raw_responses": [
    "{\"requested_fields\": [\"facet\", \"heading\", \"text\"], \"all_fields\": false, \"platform\": \"demo20_competition_rule_03\"}"
  ],
  "record_ids": [
    "demo20_competition_rule_03"
  ]
}
```

ปฏิเสธเพราะ platform='demo20_competition_rule_03' ไม่อยู่ใน ['Cockpit', 'Nintendo Switch', 'PC', 'PS5', 'VR'] และไม่ใช่ null; checked_plan คืน None แม้บาง requested_fields ถูกแล้ว

Plan สุดท้าย:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_03"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
  "catalog_scope": "common_published"
}
```

## LLM Case 42 — main case 03983

ถาม: ข้อการแข่งขันทดลอง ละอองฝน อยากอ่านข้อความกติกาข้อนี้ให้ครบ

ปิด LLM: True • เปิด LLM: True

คำตอบที่ได้:
```text
**ข้อการแข่งขันทดลอง ละอองฝน**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก ละอองฝน [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: competition_format [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง ละอองฝน [S5]
• เลขข้อเดิม เช่น 6.1.5: 4.3 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 3: พักเมื่อเวียนหัว ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

ควรตอบ:
```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 3: พักเมื่อเวียนหัว ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

ไม่มี planner attempt ในเคสนี้ เพราะ gate ก่อนเรียกดู requested_fields/broad/overview ไม่ได้หมายความว่าโมเดลตอบผิด

Plan สุดท้าย:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_03"
    ],
    "requested_fields": [],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_competition_rule_03",
      "field": "competition_id",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/competition_id",
          "source_id": "fixture20_demo20_competition_rule_03"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_03",
      "field": "completeness",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/completeness",
          "source_id": "fixture20_demo20_competition_rule_03"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_03",
      "field": "depends_on_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/depends_on_ids",
          "source_id": "fixture20_demo20_competition_rule_03"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_03",
      "field": "facet",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/facet",
          "source_id": "fixture20_demo20_competition_rule_03"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_03",
      "field": "heading",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/heading",
          "source_id": "fixture20_demo20_competition_rule_03"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_03",
      "field": "section_number",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/section_number",
          "source_id": "fixture20_demo20_competition_rule_03"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_03",
      "field": "text",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/text",
          "source_id": "fixture20_demo20_competition_rule_03"
        }
      ]
    }
  ],
  "catalog_scope": "common_published"
}
```

## LLM Case 43 — main case 03984

ถาม: แล้วข้อนี้กำหนดอะไร

ปิด LLM: False • เปิด LLM: False

คำตอบที่ได้:
```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

ควรตอบ:
```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 3: พักเมื่อเวียนหัว ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
```

Planner attempt:
```json
{
  "checked_plan": null,
  "raw_responses": [
    "{\"requested_fields\": [\"facet\", \"heading\", \"text\"], \"all_fields\": false, \"platform\": \"demo20_competition_rule_03\"}"
  ],
  "record_ids": [
    "demo20_competition_rule_03"
  ]
}
```

ปฏิเสธเพราะ platform='demo20_competition_rule_03' ไม่อยู่ใน ['Cockpit', 'Nintendo Switch', 'PC', 'PS5', 'VR'] และไม่ใช่ null; checked_plan คืน None แม้บาง requested_fields ถูกแล้ว

Plan สุดท้าย:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_03"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "history_exact:pending_fields",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
  "catalog_scope": "common_published"
}
```

## LLM Case 44 — main case 03985

ถาม: ข้อการแข่งขันทดลอง ละอองฝน กติกาข้อนี้มีเนื้อหาอะไรและข้อมูลครบไหม

ปิด LLM: True • เปิด LLM: True

คำตอบที่ได้:
```text
**ข้อการแข่งขันทดลอง ละอองฝน**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก ละอองฝน [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: competition_format [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง ละอองฝน [S5]
• เลขข้อเดิม เช่น 6.1.5: 4.3 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 3: พักเมื่อเวียนหัว ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

ควรตอบ:
```text
ข้อความข้อกติกาเต็ม (text): ข้อสมมุติ 3: พักเมื่อเวียนหัว ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง
สถานะความครบของข้อกติกา (completeness): complete
```

ไม่มี planner attempt ในเคสนี้ เพราะ gate ก่อนเรียกดู requested_fields/broad/overview ไม่ได้หมายความว่าโมเดลตอบผิด

Plan สุดท้าย:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_03"
    ],
    "requested_fields": [],
    "all_fields": true,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_competition_rule_03",
      "field": "competition_id",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/competition_id",
          "source_id": "fixture20_demo20_competition_rule_03"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_03",
      "field": "completeness",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/completeness",
          "source_id": "fixture20_demo20_competition_rule_03"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_03",
      "field": "depends_on_ids",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/depends_on_ids",
          "source_id": "fixture20_demo20_competition_rule_03"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_03",
      "field": "facet",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/facet",
          "source_id": "fixture20_demo20_competition_rule_03"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_03",
      "field": "heading",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/heading",
          "source_id": "fixture20_demo20_competition_rule_03"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_03",
      "field": "section_number",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/section_number",
          "source_id": "fixture20_demo20_competition_rule_03"
        }
      ]
    },
    {
      "record_id": "demo20_competition_rule_03",
      "field": "text",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/text",
          "source_id": "fixture20_demo20_competition_rule_03"
        }
      ]
    }
  ],
  "catalog_scope": "common_published"
}
```

## LLM Case 45 — main case 03987

ถาม: Demo rule Drizzle What does this rule require?

ปิด LLM: False • เปิด LLM: False

คำตอบที่ได้:
```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

ควรตอบ:
```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 3: for Motion discomfort breaks, follow decision required; exception requires written demo operator approval; not actual rules
```

Planner attempt:
```json
{
  "checked_plan": null,
  "raw_responses": [
    "{\"requested_fields\": [\"facet\", \"heading\", \"text\"], \"all_fields\": false, \"platform\": \"demo20_competition_rule_03\"}"
  ],
  "record_ids": [
    "demo20_competition_rule_03"
  ]
}
```

ปฏิเสธเพราะ platform='demo20_competition_rule_03' ไม่อยู่ใน ['Cockpit', 'Nintendo Switch', 'PC', 'PS5', 'VR'] และไม่ใช่ null; checked_plan คืน None แม้บาง requested_fields ถูกแล้ว

Plan สุดท้าย:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_03"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
  "catalog_scope": "common_published"
}
```

## LLM Case 46 — main case 03988

ถาม: Demo rule Drizzle Please give the full text of this rule.

ปิด LLM: True • เปิด LLM: True

คำตอบที่ได้:
```text
**Demo rule Drizzle**
• text: Fictional clause 3: for Motion discomfort breaks, follow decision required; exception requires written demo operator approval; not actual rules [S1]

English translation is machine generated and has not been reviewed by the owner.
```

ควรตอบ:
```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 3: for Motion discomfort breaks, follow decision required; exception requires written demo operator approval; not actual rules
```

ไม่มี planner attempt ในเคสนี้ เพราะ gate ก่อนเรียกดู requested_fields/broad/overview ไม่ได้หมายความว่าโมเดลตอบผิด

Plan สุดท้าย:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_03"
    ],
    "requested_fields": [
      "text"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": "demo20_competition_rule_03",
      "field": "text",
      "status": "known",
      "evidence_refs": [
        {
          "locator": "/values/text",
          "source_id": "fixture20_demo20_competition_rule_03"
        }
      ]
    }
  ],
  "catalog_scope": "common_published"
}
```

## LLM Case 47 — main case 03989

ถาม: And What does this rule require?

ปิด LLM: False • เปิด LLM: False

คำตอบที่ได้:
```text
summary: No confirmed information in this scope.

English translation is machine generated and has not been reviewed by the owner.
```

ควรตอบ:
```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 3: for Motion discomfort breaks, follow decision required; exception requires written demo operator approval; not actual rules
```

ไม่มี planner attempt ในเคสนี้ เพราะ gate ก่อนเรียกดู requested_fields/broad/overview ไม่ได้หมายความว่าโมเดลตอบผิด

Plan สุดท้าย:
```json
{
  "response_type": "answer",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_03"
    ],
    "requested_fields": [
      "summary"
    ],
    "all_fields": false,
    "method": "history_exact:pending_fields",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [
    {
      "record_id": null,
      "field": "summary",
      "status": "unknown"
    }
  ],
  "catalog_scope": "common_published"
}
```

## LLM Case 48 — main case 03990

ถาม: Demo rule Drizzle What does the rule say and is its content complete?

ปิด LLM: False • เปิด LLM: False

คำตอบที่ได้:
```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

ควรตอบ:
```text
ข้อความข้อกติกาเต็ม (text): Fictional clause 3: for Motion discomfort breaks, follow decision required; exception requires written demo operator approval; not actual rules
สถานะความครบของข้อกติกา (completeness): complete
```

Planner attempt:
```json
{
  "checked_plan": null,
  "raw_responses": [
    "{\"requested_fields\": [\"text\", \"completeness\"], \"all_fields\": false, \"platform\": \"demo20_competition_rule_03\"}"
  ],
  "record_ids": [
    "demo20_competition_rule_03"
  ]
}
```

ปฏิเสธเพราะ platform='demo20_competition_rule_03' ไม่อยู่ใน ['Cockpit', 'Nintendo Switch', 'PC', 'PS5', 'VR'] และไม่ใช่ null; checked_plan คืน None แม้บาง requested_fields ถูกแล้ว

Plan สุดท้าย:
```json
{
  "response_type": "clarification",
  "release_id": "6a976d45840645759f5bd0219c1c0e40",
  "query_plan": {
    "record_ids": [
      "demo20_competition_rule_03"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null
  },
  "obligations": [],
  "catalog_scope": "common_published"
}
```

