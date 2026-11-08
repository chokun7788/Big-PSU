# R121 — เปรียบเทียบการตีโจทย์ก่อน/หลังฝึกจริง

วัดคำถามเดิม 30 ข้อ แยก family จากชุดสอน คะแนนนี้เป็นการตีโจทย์เทียบ agent-authored labels ไม่ใช่ความถูกต้องของคำตอบปลายทาง

| ตัววัด | ก่อนฝึก | หลังฝึก | ดีขึ้น / ถอยลง |
|---|---:|---:|---:|
| source_contract_valid | 5/30 | 29/30 | 24 / 0 |
| focus_correct | 14/30 | 20/30 | 7 / 1 |
| domains_correct | 12/30 | 22/30 | 11 / 1 |
| domain_facet_correct | 5/30 | 19/30 | 15 / 1 |
| task_count_correct | 26/30 | 30/30 | 4 / 0 |
| tasks_exact | 2/30 | 17/30 | 15 / 0 |

`tasks_exact` หมายถึงชุด signature (domain, operation, facet, ambiguous) ที่ตรงกันและผ่าน contract ไม่ได้หมายถึง target/constraints ทุกตัวตรง gold ส่วน typed-constraint precision/recall เป็นการเทียบ slot และข้อความตรงตัว ข้อความที่ต่าง gold แต่อ้างจากคำถามถูกอาจยังยอมรับได้ และการไม่มี typed slot ไม่ได้แปลว่าบริบทหาย หากยังอยู่ใน task quote จึงต้อง review ความหมายแยก

## แยกภาษา/locale

### auto

จำนวน 7 ข้อ; focus 4 → 4; domain 6 → 6; exact task signature 2 → 5

### en

จำนวน 17 ข้อ; focus 7 → 11; domain 6 → 11; exact task signature 0 → 7

### th

จำนวน 6 ข้อ; focus 3 → 5; domain 0 → 5; exact task signature 0 → 5

## รายข้อทั้งหมด

### 1. Is PC #03-#10 available right now Please keep the answer concise

- key: `dcac3d3e21d6b35d8ea26146cf8b5fcefa68d1fd277a8adf3302b37a53624d18`; locale: en
- ก่อนฝึก focus/domain/facet/tasks: False/False/False/False
- หลังฝึก focus/domain/facet/tasks: False/False/False/False
- หลังฝึก contract: validated_source_quoted_interpretation; missing typed constraints: [['platform', 'PC'], ['service', 'PC #03-#10'], ['time', 'right now']]

Gold plan:
```json
{
  "focus": "live_status",
  "context_quotes": [
    "right now",
    "PC",
    "PC #03-#10"
  ],
  "tasks": [
    {
      "quote": "Is PC #03-#10 available right now Please keep the answer concise",
      "domain": "live",
      "operation": "availability",
      "facet": "live_status",
      "target": "",
      "constraints": [
        {
          "slot": "time",
          "quote": "right now",
          "source_record_id": ""
        },
        {
          "slot": "platform",
          "quote": "PC",
          "source_record_id": ""
        },
        {
          "slot": "service",
          "quote": "PC #03-#10",
          "source_record_id": ""
        }
      ],
      "ambiguous": false
    }
  ]
}
```

ก่อนฝึก:
```
{
  "focus": "game_availability",
  "context_quotes": [
    "Is PC #03-#10 available right now Please keep the answer concise"
  ],
  "tasks": [
    {
      "quote": "Is PC #03-#10 available right now Please keep the answer concise",
      "domain": "equipment_availability",
      "operation": "availability",
      "facet": "equipment_availability",
      "target": "",
      "constraints": [
        {
          "slot": "audience",
          "quote": "",
          "source_record_id": ""
        },
        {
          "slot": "negation",
          "quote": "",
          "source_record_id": ""
        },
        {
          "slot": "time",
          "quote": "right now",
          "source_record_id": ""
        },
        {
          "slot": "equipment",
          "quote": "PC #03-#10",
          "source_record_id": ""
        }
      ],
      "ambiguous": false
    }
  ]
}
```

หลังฝึก:
```
{"focus":"game_availability","context_quotes":[],"tasks":[{"quote":"Is PC #03-#10 available right now Please keep the answer concise","domain":"schedule","operation":"availability","facet":"bookable_periods","target":"","constraints":[],"ambiguous":false}]}
```

### 2. Under CS2 tournamment ruls, may I change Brightness, Resolution and Crosshair, and where?

- key: `ef5c0b5af4c6794d174d9a9d329fe7e2535c1fac26b3cf0fd1d69f084d64ca96`; locale: en
- ก่อนฝึก focus/domain/facet/tasks: False/False/False/False
- หลังฝึก focus/domain/facet/tasks: False/False/False/False
- หลังฝึก contract: validated_source_quoted_interpretation; missing typed constraints: []

Gold plan:
```json
{
  "focus": "competition_rules",
  "context_quotes": [],
  "tasks": [
    {
      "quote": "Under CS2 tournamment ruls, may I change Brightness, Resolution and Crosshair, and where?",
      "domain": "competition_rules",
      "operation": "rule_lookup",
      "facet": "rule_clause",
      "target": "CS2",
      "constraints": [],
      "ambiguous": false
    }
  ]
}
```

ก่อนฝึก:
```
{
  "focus": "game_controls",
  "context_quotes": [
    "Under CS2 tournamment ruls, may I change Brightness, Resolution and Crosshair, and where?"
  ],
  "tasks": [
    {
      "quote": "Under CS2 tournamment ruls, may I change Brightness, Resolution and Crosshair, and where?",
      "domain": "game_controls",
      "operation": "detail",
      "facet": "input_bindings",
      "target": "Brightness, Resolution and Crosshair",
      "constraints": [
        {
          "slot": "audience",
          "quote": "Under CS2 tournamment ruls",
          "source_record_id": ""
        }
      ],
      "ambiguous": false
    }
  ]
}
```

หลังฝึก:
```
{"focus":"game_controls","context_quotes":[],"tasks":[{"quote":"Under CS2 tournamment ruls, may I change Brightness, Resolution and Crosshair, and where?","domain":"game_controls","operation":"control","facet":"input_bindings","target":"CS2","constraints":[],"ambiguous":false}]}
```

### 3. TEKKEN 8 ถ้าทำผิดกติกาจะโดนปรับแพ้ไหม

- key: `d42ce15f001b4cfd61360f1496c1361fa7880a24f727bc19def9b8bd88c9baa4`; locale: auto
- ก่อนฝึก focus/domain/facet/tasks: True/True/False/False
- หลังฝึก focus/domain/facet/tasks: True/True/True/True
- หลังฝึก contract: validated_source_quoted_interpretation; missing typed constraints: []

Gold plan:
```json
{
  "focus": "competition_rules",
  "context_quotes": [],
  "tasks": [
    {
      "quote": "TEKKEN 8 ถ้าทำผิดกติกาจะโดนปรับแพ้ไหม",
      "domain": "competition_rules",
      "operation": "rule_lookup",
      "facet": "rule_clause",
      "target": "TEKKEN 8",
      "constraints": [],
      "ambiguous": false
    }
  ]
}
```

ก่อนฝึก:
```
{
  "focus": "competition_rules",
  "context_quotes": [
    "TEKKEN 8 ถ้าทำผิดกติกาจะโดนปรับแพ้ไหม"
  ],
  "tasks": [
    {
      "quote": "TEKKEN 8 ถ้าทำผิดกติกาจะโดนปรับแพ้ไหม",
      "domain": "competition_rules",
      "operation": "rule_lookup",
      "facet": "competition_rules",
      "target": "",
      "constraints": [
        {
          "slot": "audience",
          "quote": "TEKKEN 8",
          "source_record_id": ""
        },
        {
          "slot": "negation",
          "quote": "จะโดนปรับแพ้ไหม",
          "source_record_id": ""
        }
      ],
      "ambiguous": false
    }
  ]
}
```

หลังฝึก:
```
{"focus":"competition_rules","context_quotes":[],"tasks":[{"quote":"TEKKEN 8 ถ้าทำผิดกติกาจะโดนปรับแพ้ไหม","domain":"competition_rules","operation":"rule_lookup","facet":"rule_clause","target":"TEKKEN 8","constraints":[],"ambiguous":false}]}
```

### 4. What does the R3 (Click Right Stick) button do in The Last of Us Part I on PlayStation / PS5

- key: `98a88bb46a86278f3df6da929b113d3b0571dc729388a0a818508ef0b9b6fa05`; locale: en
- ก่อนฝึก focus/domain/facet/tasks: True/True/True/False
- หลังฝึก focus/domain/facet/tasks: True/True/True/True
- หลังฝึก contract: validated_source_quoted_interpretation; missing typed constraints: [['platform', 'PlayStation / PS5']]

Gold plan:
```json
{
  "focus": "game_controls",
  "context_quotes": [
    "PlayStation / PS5"
  ],
  "tasks": [
    {
      "quote": "What does the R3 (Click Right Stick) button do in The Last of Us Part I on PlayStation / PS5",
      "domain": "game_controls",
      "operation": "control",
      "facet": "input_bindings",
      "target": "The Last of Us Part I",
      "constraints": [
        {
          "slot": "platform",
          "quote": "PlayStation / PS5",
          "source_record_id": ""
        }
      ],
      "ambiguous": false
    }
  ]
}
```

ก่อนฝึก:
```
{
  "focus": "game_controls",
  "context_quotes": [
    "What does the R3 (Click Right Stick) button do in The Last of Us Part I on PlayStation / PS5"
  ],
  "tasks": [
    {
      "quote": "What does the R3 (Click Right Stick) button do in The Last of Us Part I on PlayStation / PS5",
      "domain": "game_controls",
      "operation": "detail",
      "facet": "input_bindings",
      "target": "R3 (Click Right Stick) button function in The Last of Us Part I on PS5",
      "constraints": [
        {
          "slot": "audience",
          "quote": "What does the R3 (Click Right Stick) button do in The Last of Us Part I on PlayStation / PS5",
          "source_record_id": ""
        }
      ],
      "ambiguous": false
    }
  ]
}
```

หลังฝึก:
```
{"focus":"game_controls","context_quotes":[],"tasks":[{"quote":"What does the R3 (Click Right Stick) button do in The Last of Us Part I on PlayStation / PS5","domain":"game_controls","operation":"control","facet":"input_bindings","target":"The Last of Us Part I","constraints":[],"ambiguous":false}]}
```

### 5. ขอสอบถามหน่อยครับ Nintendo Switch Zone มีอะไรให้ใช้บ้าง

- key: `2d97cb1b2297d0a2bf6c2073dfec0e79e2d0ec3995b47987e2b1eef242f70c70`; locale: th
- ก่อนฝึก focus/domain/facet/tasks: False/False/False/False
- หลังฝึก focus/domain/facet/tasks: True/True/True/True
- หลังฝึก contract: validated_source_quoted_interpretation; missing typed constraints: [['platform', 'Nintendo Switch']]

Gold plan:
```json
{
  "focus": "equipment_inventory",
  "context_quotes": [
    "Nintendo Switch"
  ],
  "tasks": [
    {
      "quote": "ขอสอบถามหน่อยครับ Nintendo Switch Zone มีอะไรให้ใช้บ้าง",
      "domain": "equipment",
      "operation": "list",
      "facet": "name",
      "target": "Nintendo Switch",
      "constraints": [
        {
          "slot": "platform",
          "quote": "Nintendo Switch",
          "source_record_id": ""
        }
      ],
      "ambiguous": false
    }
  ]
}
```

ก่อนฝึก:
```
{
  "focus": "game_catalog",
  "context_quotes": [
    "ขอสอบถามหน่อยครับ Nintendo Switch Zone มีอะไรให้ใช้บ้าง"
  ],
  "tasks": [
    {
      "quote": "ขอสอบถามหน่อยครับ Nintendo Switch Zone มีอะไรให้ใช้บ้าง",
      "domain": "games",
      "operation": "detail",
      "facet": "game_catalog",
      "target": "",
      "constraints": [],
      "ambiguous": false
    }
  ]
}
```

หลังฝึก:
```
{"focus":"equipment_inventory","context_quotes":[],"tasks":[{"quote":"ขอสอบถามหน่อยครับ Nintendo Switch Zone มีอะไรให้ใช้บ้าง","domain":"equipment","operation":"list","facet":"name","target":"","constraints":[],"ambiguous":false}]}
```

### 6. What is PSU Esports Studio - Phuket? I need the official answer

- key: `2a729438da53f233061c6c765da72d9b1735bccabf9f95d04f3096c03e7d0856`; locale: en
- ก่อนฝึก focus/domain/facet/tasks: True/False/False/False
- หลังฝึก focus/domain/facet/tasks: True/True/False/False
- หลังฝึก contract: validated_source_quoted_interpretation; missing typed constraints: []

Gold plan:
```json
{
  "focus": "identity",
  "context_quotes": [],
  "tasks": [
    {
      "quote": "What is PSU Esports Studio - Phuket? I need the official answer",
      "domain": "contact",
      "operation": "detail",
      "facet": "description",
      "target": "",
      "constraints": [],
      "ambiguous": false
    }
  ]
}
```

ก่อนฝึก:
```
{
  "focus": "identity",
  "context_quotes": [
    "What is PSU Esports Studio - Phuket? I need the official answer"
  ],
  "tasks": [
    {
      "quote": "What is PSU Esports Studio - Phuket? I need the official answer",
      "domain": "identity",
      "operation": "detail",
      "facet": "identity",
      "target": "",
      "constraints": [],
      "ambiguous": false
    }
  ]
}
```

หลังฝึก:
```
{"focus":"identity","context_quotes":[],"tasks":[{"quote":"What is PSU Esports Studio - Phuket? I need the official answer","domain":"contact","operation":"detail","facet":"value","target":"","constraints":[],"ambiguous":false}]}
```

### 7. API คืออะไร ตอบเป็นภาษาไทย

- key: `37fafe5389e144930adc532e66ae085dd91fb58fdfbb19f877162cbbf2e29a36`; locale: auto
- ก่อนฝึก focus/domain/facet/tasks: True/True/True/True
- หลังฝึก focus/domain/facet/tasks: True/True/True/True
- หลังฝึก contract: validated_source_quoted_interpretation; missing typed constraints: []

Gold plan:
```json
{
  "focus": "general",
  "context_quotes": [],
  "tasks": [
    {
      "quote": "API คืออะไร ตอบเป็นภาษาไทย",
      "domain": "general",
      "operation": "detail",
      "facet": "",
      "target": "",
      "constraints": [],
      "ambiguous": false
    }
  ]
}
```

ก่อนฝึก:
```
{
  "focus": "general",
  "context_quotes": [
    "API คืออะไร ตอบเป็นภาษาไทย"
  ],
  "tasks": [
    {
      "quote": "API คืออะไร ตอบเป็นภาษาไทย",
      "domain": "general",
      "operation": "detail",
      "facet": "",
      "target": "",
      "constraints": [],
      "ambiguous": false
    }
  ]
}
```

หลังฝึก:
```
{"focus":"general","context_quotes":[],"tasks":[{"quote":"API คืออะไร ตอบเป็นภาษาไทย","domain":"general","operation":"detail","facet":"","target":"","constraints":[],"ambiguous":false}]}
```

### 8. ขอข้อมูลที่ยืนยันได้หน่อยครับ: Tekken 8 เลือกด่านยังไง

- key: `ad28947d610ba429ff05e73c28cf5c3a6b1bbfc7afa9df226af42dffc29a9ed7`; locale: th
- ก่อนฝึก focus/domain/facet/tasks: False/False/False/False
- หลังฝึก focus/domain/facet/tasks: False/False/False/False
- หลังฝึก contract: validated_source_quoted_interpretation; missing typed constraints: []

Gold plan:
```json
{
  "focus": "competition_rules",
  "context_quotes": [],
  "tasks": [
    {
      "quote": "ขอข้อมูลที่ยืนยันได้หน่อยครับ: Tekken 8 เลือกด่านยังไง",
      "domain": "competition_rules",
      "operation": "rule_lookup",
      "facet": "rule_clause",
      "target": "Tekken 8",
      "constraints": [],
      "ambiguous": false
    }
  ]
}
```

ก่อนฝึก:
```
{
  "focus": "game_controls",
  "context_quotes": [
    "ขอข้อมูลที่ยืนยันได้หน่อยครับ: Tekken 8 เลือกด่านยังไง"
  ],
  "tasks": [
    {
      "quote": "ขอข้อมูลที่ยืนยันได้หน่อยครับ: Tekken 8 เลือกด่านยังไง",
      "domain": "games",
      "operation": "detail",
      "facet": "game_controls",
      "target": "เลือกด่านยังไง",
      "constraints": [
        {
          "slot": "audience",
          "quote": "ขอข้อมูลที่ยืนยันได้หน่อยครับ",
          "source_record_id": ""
        },
        {
          "slot": "negation",
          "quote": "",
          "source_record_id": ""
        },
        {
          "slot": "action",
          "quote": "เลือกด่านยังไง",
          "source_record_id": ""
        },
        {
          "slot": "platform",
          "quote": "Tekken 8",
          "source_record_id": ""
        }
      ],
      "ambiguous": false
    }
  ]
}
```

หลังฝึก:
```
{"focus":"game_controls","context_quotes":[],"tasks":[{"quote":"ขอข้อมูลที่ยืนยันได้หน่อยครับ: Tekken 8 เลือกด่านยังไง","domain":"game_controls","operation":"control","facet":"input_bindings","target":"Tekken 8","constraints":[],"ambiguous":false}]}
```

### 9. Please answer from verified studio information: Please tell me: When can I play on Monday afternoon

- key: `9226ff9f7b760af0bf0c83351a5604026900bb7e9d820b7e95960f8e8b406c50`; locale: en
- ก่อนฝึก focus/domain/facet/tasks: False/False/False/False
- หลังฝึก focus/domain/facet/tasks: False/True/False/False
- หลังฝึก contract: validated_source_quoted_interpretation; missing typed constraints: [['date', 'Monday']]

Gold plan:
```json
{
  "focus": "opening_hours",
  "context_quotes": [
    "Monday"
  ],
  "tasks": [
    {
      "quote": "Please answer from verified studio information: Please tell me: When can I play on Monday afternoon",
      "domain": "schedule",
      "operation": "detail",
      "facet": "open_periods",
      "target": "",
      "constraints": [
        {
          "slot": "date",
          "quote": "Monday",
          "source_record_id": ""
        }
      ],
      "ambiguous": false
    }
  ]
}
```

ก่อนฝึก:
```
{
  "focus": "opening_hours",
  "context_quotes": [
    "Please tell me: When can I play on Monday afternoon"
  ],
  "tasks": [
    {
      "quote": "Please tell me: When can I play on Monday afternoon",
      "domain": "opening_hours",
      "operation": "availability",
      "facet": "schedule",
      "target": "",
      "constraints": [
        {
          "slot": "audience",
          "quote": "",
          "source_record_id": ""
        },
        {
          "slot": "negation",
          "quote": "",
          "source_record_id": ""
        },
        {
          "slot": "time",
          "quote": "Monday afternoon",
          "source_record_id": ""
        },
        {
          "slot": "event",
          "quote": "",
          "source_record",
          "source_record_id": ""
        }
      ],
      "ambiguous": false
    }
  ]
}
```

หลังฝึก:
```
{"focus":"bookable_periods","context_quotes":[],"tasks":[{"quote":"Please tell me: When can I play on Monday afternoon","domain":"schedule","operation":"detail","facet":"bookable_periods","target":"","constraints":[],"ambiguous":false}]}
```

### 10. What are the 8 buttons in Tekken 8, ans what is the PC price

- key: `d91ee50a1f6c21f141226b55bb86aaea2935e3a4b5e73b339ff4d83b81a1deaa`; locale: en
- ก่อนฝึก focus/domain/facet/tasks: False/False/False/False
- หลังฝึก focus/domain/facet/tasks: True/False/False/False
- หลังฝึก contract: validated_source_quoted_interpretation; missing typed constraints: [['platform', 'PC'], ['requested_scope', '8 buttons'], ['service', 'PC'], ['service', 'Tekken 8']]

Gold plan:
```json
{
  "focus": "multiple",
  "context_quotes": [
    "PC",
    "8 buttons",
    "Tekken 8"
  ],
  "tasks": [
    {
      "quote": "What are the 8 buttons in Tekken 8",
      "domain": "game_controls",
      "operation": "list",
      "facet": "input_bindings",
      "target": "Tekken 8",
      "constraints": [
        {
          "slot": "platform",
          "quote": "PC",
          "source_record_id": ""
        },
        {
          "slot": "requested_scope",
          "quote": "8 buttons",
          "source_record_id": ""
        }
      ],
      "ambiguous": false
    },
    {
      "quote": "what is the PC price",
      "domain": "service_fee",
      "operation": "price_calculate",
      "facet": "amount",
      "target": "PC",
      "constraints": [
        {
          "slot": "platform",
          "quote": "PC",
          "source_record_id": ""
        },
        {
          "slot": "requested_scope",
          "quote": "8 buttons",
          "source_record_id": ""
        },
        {
          "slot": "service",
          "quote": "PC",
          "source_record_id": ""
        },
        {
          "slot": "service",
          "quote": "Tekken 8",
          "source_record_id": ""
        }
      ],
      "ambiguous": false
    }
  ]
}
```

ก่อนฝึก:
```
{
  "focus": "game_controls",
  "context_quotes": [
    "What are the 8 buttons in Tekken 8"
  ],
  "tasks": [
    {
      "quote": "What are the 8 buttons in Tekken 8",
      "domain": "game_controls",
      "operation": "detail",
      "facet": "game_controls",
      "target": "8 buttons in Tekken 8",
      "constraints": [
        {
          "slot": "audience",
          "quote": "What are the 8 buttons in Tekken 8",
          "source_record_id": ""
        }
      ],
      "ambiguous": false
    }
  ]
}
```

หลังฝึก:
```
{"focus":"multiple","context_quotes":[],"tasks":[{"quote":"What are the 8 buttons in Tekken 8","domain":"games","operation":"detail","facet":"how_to_play","target":"Tekken 8","constraints":[],"ambiguous":false},{"quote":"what is the PC price","domain":"service_fee","operation":"price_calculate","facet":"amount","target":"PC","constraints":[],"ambiguous":false}]}
```

### 11. ก่อนเดินทางไปใช้บริการ อยากทราบว่า คนที่ไม่ใช่นักศึกษา PSU เข้าไปเล่นได้หรือเปล่า

- key: `490a5b13b782510c507fdb5692383211a2537734caa8e7e489f42932969ea534`; locale: th
- ก่อนฝึก focus/domain/facet/tasks: True/False/False/False
- หลังฝึก focus/domain/facet/tasks: True/True/True/True
- หลังฝึก contract: validated_source_quoted_interpretation; missing typed constraints: [['audience', 'นักศึกษา PSU'], ['negation', 'ไม่ใช่นักศึกษา PSU']]

Gold plan:
```json
{
  "focus": "eligibility",
  "context_quotes": [
    "ไม่ใช่นักศึกษา PSU",
    "นักศึกษา PSU"
  ],
  "tasks": [
    {
      "quote": "ก่อนเดินทางไปใช้บริการ อยากทราบว่า คนที่ไม่ใช่นักศึกษา PSU เข้าไปเล่นได้หรือเปล่า",
      "domain": "rules",
      "operation": "detail",
      "facet": "owner_policy",
      "target": "",
      "constraints": [
        {
          "slot": "negation",
          "quote": "ไม่ใช่นักศึกษา PSU",
          "source_record_id": ""
        },
        {
          "slot": "audience",
          "quote": "นักศึกษา PSU",
          "source_record_id": ""
        }
      ],
      "ambiguous": false
    }
  ]
}
```

ก่อนฝึก:
```
{
  "focus": "eligibility",
  "context_quotes": [
    "ก่อนเดินทางไปใช้บริการ อยากทราบว่า คนที่ไม่ใช่นักศึกษา PSU เข้าไปเล่นได้หรือเปล่า"
  ],
  "tasks": [
    {
      "quote": "ก่อนเดินทางไปใช้บริการ อยากทราบว่า คนที่ไม่ใช่นักศึกษา PSU เข้าไปเล่นได้หรือเปล่า",
      "domain": "eligibility",
      "operation": "availability",
      "facet": "eligibility",
      "target": "คนที่ไม่ใช่นักศึกษา PSU เข้าไปเล่นได้หรือเปล่า",
      "constraints": [
        {
          "slot": "audience",
          "quote": "คนที่ไม่ใช่นักศึกษา PSU",
          "source_record_id": ""
        }
      ],
      "ambiguous": false
    }
  ]
}
```

หลังฝึก:
```
{"focus":"eligibility","context_quotes":[],"tasks":[{"quote":"ก่อนเดินทางไปใช้บริการ อยากทราบว่า คนที่ไม่ใช่นักศึกษา PSU เข้าไปเล่นได้หรือเปล่า","domain":"rules","operation":"detail","facet":"owner_policy","target":"","constraints":[],"ambiguous":false}]}
```

### 12. ขอสอบถามหน่อยครับ ใครเป็นผู้ช่วยอธิการบดีฝ่ายวิชาการ

- key: `fe55f25aaebb1da6334206ac51f14ddbe94f9f67fe187a21cdfabd862779dbb9`; locale: th
- ก่อนฝึก focus/domain/facet/tasks: False/False/False/False
- หลังฝึก focus/domain/facet/tasks: True/True/True/True
- หลังฝึก contract: validated_source_quoted_interpretation; missing typed constraints: []

Gold plan:
```json
{
  "focus": "people",
  "context_quotes": [],
  "tasks": [
    {
      "quote": "ขอสอบถามหน่อยครับ ใครเป็นผู้ช่วยอธิการบดีฝ่ายวิชาการ",
      "domain": "members",
      "operation": "role_lookup",
      "facet": "role",
      "target": "",
      "constraints": [],
      "ambiguous": false
    }
  ]
}
```

ก่อนฝึก:
```
{
  "focus": "contact",
  "context_quotes": [
    "ขอสอบถามหน่อยครับ ใครเป็นผู้ช่วยอธิการบดีฝ่ายวิชาการ"
  ],
  "tasks": [
    {
      "quote": "ขอสอบถามหน่อยครับ ใครเป็นผู้ช่วยอธิการบดีฝ่ายวิชาการ",
      "domain": "contact",
      "operation": "role_lookup",
      "facet": "contact",
      "target": "ผู้ช่วยอธิการบดีฝ่ายวิชาการ",
      "constraints": [
            {
              "slot": "audience",
              "quote": "ขอสอบถามหน่อยครับ",
              "source_record_id": ""
            }
          ],
      "ambiguous": false
    }
  ]
}
```

หลังฝึก:
```
{"focus":"people","context_quotes":[],"tasks":[{"quote":"ขอสอบถามหน่อยครับ ใครเป็นผู้ช่วยอธิการบดีฝ่ายวิชาการ","domain":"members","operation":"role_lookup","facet":"role","target":"","constraints":[],"ambiguous":false}]}
```

### 13. General Adult เล่น VR 30 นาที 3 ชั่วโมง เสียกี่บาท

- key: `4ab178afba5082b6f01b75408daa8f3456a0aacb9e7f00da08b95aa9fcbd763d`; locale: auto
- ก่อนฝึก focus/domain/facet/tasks: False/False/False/False
- หลังฝึก focus/domain/facet/tasks: True/True/True/False
- หลังฝึก contract: validated_source_quoted_interpretation; missing typed constraints: []

Gold plan:
```json
{
  "focus": "price",
  "context_quotes": [
    "30 นาที",
    "3 ชั่วโมง",
    "General Adult",
    "VR"
  ],
  "tasks": [
    {
      "quote": "General Adult เล่น VR 30 นาที 3 ชั่วโมง เสียกี่บาท",
      "domain": "service_fee",
      "operation": "price_calculate",
      "facet": "amount",
      "target": "VR",
      "constraints": [
        {
          "slot": "duration",
          "quote": "30 นาที",
          "source_record_id": ""
        },
        {
          "slot": "duration",
          "quote": "3 ชั่วโมง",
          "source_record_id": ""
        },
        {
          "slot": "audience",
          "quote": "General Adult",
          "source_record_id": ""
        },
        {
          "slot": "service",
          "quote": "VR",
          "source_record_id": ""
        }
      ],
      "ambiguous": true
    }
  ]
}
```

ก่อนฝึก:
```
{
  "focus": "price",
  "context_quotes": [
    "General Adult เล่น VR 30 นาที 3 ชั่วโมง เสียกี่บาท"
  ],
  "tasks": [
    {
      "quote": "General Adult เล่น VR 30 นาที 3 ชั่วโมง เสียกี่บาท",
      "domain": "service_fee",
      "operation": "price_calculate",
      "facet": "service_fee",
      "target": "",
      "constraints": [
        {
          "slot": "audience",
          "quote": "General Adult",
          "source_record_id": ""
        },
        {
          "slot": "duration",
          "quote": "30 นาที",
          "source_record_id": ""
        },
        {
          "slot": "sessions",
          "quote": "3 ชั่วโมง",
          "source_record",
          "source_record_id": ""
        },
        {
          "slot": "negation",
          "quote": "",
          "source_record_id": ""
        },
        {
          "slot": "action",
          "quote": "เสียกี่บาท",
          "source_record_id": ""
        }
      ],
      "ambiguous": false
    }
  ]
}
```

หลังฝึก:
```
{"focus":"price","context_quotes":["30 นาที","3 ชั่วโมง","VR"],"tasks":[{"quote":"General Adult เล่น VR 30 นาที 3 ชั่วโมง เสียกี่บาท","domain":"service_fee","operation":"price_calculate","facet":"amount","target":"VR","constraints":[{"slot":"duration","quote":"30 นาที","source_record_id":""},{"slot":"duration","quote":"3 ชั่วโมง","source_record_id":""},{"slot":"service","quote":"VR","source_record_id":""},{"slot":"audience","quote":"General Adult","source_record_id":""}],"ambiguous":false}]}
```

### 14. ก่อนเดินทางไปใช้บริการ อยากทราบว่า ถือขวดน้ำเข้าไปได้หรือเปล่า ไม่ได้ถามเรื่องกิน

- key: `e57f02961055c3c0a53d1c221408cad728f8813afb52ce12e3b8da79576b2b37`; locale: th
- ก่อนฝึก focus/domain/facet/tasks: True/False/False/False
- หลังฝึก focus/domain/facet/tasks: True/True/True/True
- หลังฝึก contract: validated_source_quoted_interpretation; missing typed constraints: [['negation', 'ไม่ได้ถามเรื่องกิน']]

Gold plan:
```json
{
  "focus": "food_bring",
  "context_quotes": [
    "ไม่ได้ถามเรื่องกิน"
  ],
  "tasks": [
    {
      "quote": "ก่อนเดินทางไปใช้บริการ อยากทราบว่า ถือขวดน้ำเข้าไปได้หรือเปล่า ไม่ได้ถามเรื่องกิน",
      "domain": "rules",
      "operation": "detail",
      "facet": "owner_policy",
      "target": "",
      "constraints": [
        {
          "slot": "negation",
          "quote": "ไม่ได้ถามเรื่องกิน",
          "source_record_id": ""
        }
      ],
      "ambiguous": false
    }
  ]
}
```

ก่อนฝึก:
```
{
  "focus": "food_bring",
  "context_quotes": [
    "ก่อนเดินทางไปใช้บริการ อยากทราบว่า ถือขวดน้ำเข้าไปได้หรือเปล่า ไม่ได้ถามเรื่องกิน"
  ],
  "tasks": [
    {
      "quote": "ก่อนเดินทางไปใช้บริการ อยากทราบว่า ถือขวดน้ำเข้าไปได้หรือเปล่า ไม่ได้ถามเรื่องกิน",
      "domain": "food_bring",
      "operation": "availability",
      "facet": "food_bring",
      "target": "ถือขวดน้ำเข้าไปได้หรือเปล่า",
      "constraints": [
        {
          "slot": "negation",
          "quote": "ไม่ได้ถามเรื่องกิน",
          "source_record_id": ""
        }
      ],
      "ambiguous": false
    }
  ]
}
```

หลังฝึก:
```
{"focus":"food_bring","context_quotes":[],"tasks":[{"quote":"ก่อนเดินทางไปใช้บริการ อยากทราบว่า ถือขวดน้ำเข้าไปได้หรือเปล่า ไม่ได้ถามเรื่องกิน","domain":"rules","operation":"detail","facet":"owner_policy","target":"","constraints":[],"ambiguous":false}]}
```

### 15. What do you need to book to paly FINAL FANTASY XVI

- key: `0a00000d589ff1289bde21138edaae2f4071c278c44887ef046325cb4e101ea6`; locale: en
- ก่อนฝึก focus/domain/facet/tasks: False/False/False/False
- หลังฝึก focus/domain/facet/tasks: False/False/False/False
- หลังฝึก contract: validated_source_quoted_interpretation; missing typed constraints: [['service', 'FINAL FANTASY XVI']]

Gold plan:
```json
{
  "focus": "game_availability",
  "context_quotes": [
    "FINAL FANTASY XVI"
  ],
  "tasks": [
    {
      "quote": "What do you need to book to paly FINAL FANTASY XVI",
      "domain": "games",
      "operation": "availability",
      "facet": "studio_services",
      "target": "FINAL FANTASY XVI",
      "constraints": [
        {
          "slot": "service",
          "quote": "FINAL FANTASY XVI",
          "source_record_id": ""
        }
      ],
      "ambiguous": false
    }
  ]
}
```

ก่อนฝึก:
```
{
  "focus": "booking_procedure",
  "context_quotes": [
    "What do you need to book to paly FINAL FANTASY XVI"
  ],
  "tasks": [
    {
      "quote": "What do you need to book to paly FINAL FANTASY XVI",
      "domain": "booking_procedure",
      "operation": "detail",
      "facet": "booking_procedure",
      "target": "",
      "constraints": [
        {
          "slot": "audience",
          "quote": "",
          "source_record_id": ""
        },
        {
          "slot": "platform",
          "quote": "FINAL FANTASY XVI",
          "source_record_id": ""
        },
        {
          "slot": "negation",
          "quote": "",
          "source_record",
          "source_record_id": ""
        },
        {
          "slot": "action",
          "quote": "book",
          "source_record_id": ""
        }
      ],
      "ambiguous": false
    }
  ]
}
```

หลังฝึก:
```
{"focus":"rental","context_quotes":[],"tasks":[{"quote":"What do you need to book to paly FINAL FANTASY XVI","domain":"rental","operation":"detail","facet":"equipment_included","target":"FINAL FANTASY XVI","constraints":[],"ambiguous":false}]}
```

### 16. Please answer from verified studio information: Can I get a refund? Could you check this for me

- key: `644c55c5200510dffc9ab1cb5a160f9d121869e034970f7f7e867f8646bf31b2`; locale: en
- ก่อนฝึก focus/domain/facet/tasks: False/False/False/False
- หลังฝึก focus/domain/facet/tasks: True/True/True/True
- หลังฝึก contract: validated_source_quoted_interpretation; missing typed constraints: []

Gold plan:
```json
{
  "focus": "payment",
  "context_quotes": [],
  "tasks": [
    {
      "quote": "Please answer from verified studio information: Can I get a refund? Could you check this for me",
      "domain": "payment",
      "operation": "detail",
      "facet": "owner_policy",
      "target": "",
      "constraints": [],
      "ambiguous": false
    }
  ]
}
```

ก่อนฝึก:
```
{
  "focus": "booking_policy",
  "context_quotes": [
    "Can I get a refund? Could you check this for me"
  ],
  "tasks": [
    {
      "quote": "Can I get a refund? Could you check this for me",
      "domain": "booking_policy",
      "operation": "rule_lookup",
      "facet": "refund_policy",
      "target": "",
      "constraints": [
        {
          "slot": "negation",
          "quote": "Can I get a refund?",
          "source_record_id": ""
        },
        {
          "slot": "audience",
          "quote": "Could you check this for me",
          "source_record_id": ""
        }
      ],
      "ambiguous": false
    }
  ]
}
```

หลังฝึก:
```
{"focus":"payment","context_quotes":[],"tasks":[{"quote":"Please answer from verified studio information: Can I get a refund? Could you check this for me","domain":"payment","operation":"detail","facet":"owner_policy","target":"","constraints":[],"ambiguous":false}]}
```

### 17. What is the minimum age requirement to enter this VALORANT tournament

- key: `d8b3d77d8bb29bf24b9f7e8bb344c07ab11e81deffd6dcdccfe05df64d49645f`; locale: en
- ก่อนฝึก focus/domain/facet/tasks: True/True/False/False
- หลังฝึก focus/domain/facet/tasks: True/True/True/True
- หลังฝึก contract: validated_source_quoted_interpretation; missing typed constraints: []

Gold plan:
```json
{
  "focus": "competition_rules",
  "context_quotes": [],
  "tasks": [
    {
      "quote": "What is the minimum age requirement to enter this VALORANT tournament",
      "domain": "competition_rules",
      "operation": "rule_lookup",
      "facet": "rule_clause",
      "target": "VALORANT",
      "constraints": [],
      "ambiguous": false
    }
  ]
}
```

ก่อนฝึก:
```
{
  "focus": "competition_rules",
  "context_quotes": [
    "What is the minimum age requirement to enter this VALORANT tournament"
  ],
  "tasks": [
    {
      "quote": "What is the minimum age requirement to enter this VALORANT tournament",
      "domain": "competition_rules",
      "operation": "rule_lookup",
      "facet": "competition_rules",
      "target": "",
      "constraints": [
        {
          "slot": "audience",
          "quote": "the minimum age requirement to enter this VALORANT tournament",
          "source_record_id": ""
        }
      ],
      "ambiguous": false
    }
  ]
}
```

หลังฝึก:
```
{"focus":"competition_rules","context_quotes":[],"tasks":[{"quote":"What is the minimum age requirement to enter this VALORANT tournament","domain":"competition_rules","operation":"rule_lookup","facet":"rule_clause","target":"VALORANT","constraints":[],"ambiguous":false}]}
```

### 18. Could you help me? Under CS2 tournament rules, what are starting money and bomb time in regulation, and what are overtime rounds and starting money?

- key: `5a53efba830e246fce27c03a2ddcbb1132596eed01ca62b16e08baf84057a0d6`; locale: en
- ก่อนฝึก focus/domain/facet/tasks: True/True/True/False
- หลังฝึก focus/domain/facet/tasks: True/True/True/True
- หลังฝึก contract: validated_source_quoted_interpretation; missing typed constraints: []

Gold plan:
```json
{
  "focus": "competition_rules",
  "context_quotes": [],
  "tasks": [
    {
      "quote": "Could you help me? Under CS2 tournament rules, what are starting money and bomb time in regulation, and what are overtime rounds and starting money?",
      "domain": "competition_rules",
      "operation": "rule_lookup",
      "facet": "rule_clause",
      "target": "CS2",
      "constraints": [],
      "ambiguous": false
    }
  ]
}
```

ก่อนฝึก:
```
{
  "focus": "competition_rules",
  "context_quotes": [
    "Under CS2 tournament rules, what are starting money and bomb time in regulation, and what are overtime rounds and starting money?"
  ],
  "tasks": [
    {
      "quote": "Under CS2 tournament rules, what are starting money and bomb time in regulation, and what are overtime rounds and starting money?",
      "domain": "competition_rules",
      "operation": "rule_lookup",
      "facet": "rule_clause",
      "target": "",
      "constraints": [
        {
          "slot": "audience",
          "quote": "Under CS2 tournament rules",
          "source_record_id": ""
        },
        {
          "slot": "negation",
          "quote": "",
          "source_record_id": ""
        },
        {
          "slot": "condition",
          "quote": "",
          "source_record_id": ""
        },
        {
          "slot": "comparison",
          "quote": "",
          "source_record_id": ""
        },
        {
          "slot": "requested_scope",
          "quote": "starting money and bomb time in regulation, and what are overtime rounds and starting money",
          "source_record_id": ""
        },
        {
          "slot": "action",
          "quote": "",
          "source_record_id": ""
        }
      ],
      "ambiguous": false
    }
  ]
}
```

หลังฝึก:
```
{"focus":"competition_rules","context_quotes":[],"tasks":[{"quote":"Could you help me? Under CS2 tournament rules, what are starting money and bomb time in regulation, and what are overtime rounds and starting money?","domain":"competition_rules","operation":"rule_lookup","facet":"rule_clause","target":"CS2","constraints":[],"ambiguous":false}]}
```

### 19. A question about the studio: May I eat at a gaming desk?

- key: `c93db2f4683ad2666000dbd64550645e12fbe7641103333d34be90811bac014b`; locale: en
- ก่อนฝึก focus/domain/facet/tasks: True/False/False/False
- หลังฝึก focus/domain/facet/tasks: True/True/True/True
- หลังฝึก contract: validated_source_quoted_interpretation; missing typed constraints: []

Gold plan:
```json
{
  "focus": "food_consume",
  "context_quotes": [],
  "tasks": [
    {
      "quote": "A question about the studio: May I eat at a gaming desk?",
      "domain": "rules",
      "operation": "detail",
      "facet": "owner_policy",
      "target": "",
      "constraints": [],
      "ambiguous": false
    }
  ]
}
```

ก่อนฝึก:
```
{
  "focus": "food_consume",
  "context_quotes": [
    "May I eat at a gaming desk?"
  ],
  "tasks": [
    {
      "quote": "May I eat at a gaming desk?",
      "domain": "food_consume",
      "operation": "availability",
      "facet": "food_consume",
      "target": "",
      "constraints": [
        {
          "slot": "audience",
          "quote": "May I",
          "source_record_id": ""
        },
        {
          "slot": "negation",
          "quote": "May I",
          "source_record_id": ""
        },
        {
          "slot": "action",
          "quote": "eat",
          "source_record_id": ""
        },
        {
          "slot": "location",
          "quote": "at a gaming desk",
          "source_record_id": ""
        }
      ],
      "ambiguous": false
    }
  ]
}
```

หลังฝึก:
```
{"focus":"food_consume","context_quotes":[],"tasks":[{"quote":"A question about the studio: May I eat at a gaming desk?","domain":"rules","operation":"detail","facet":"owner_policy","target":"","constraints":[],"ambiguous":false}]}
```

### 20. เบอร์ติดต่อคืออะไร

- key: `a6bc6425eb8b8625afdbcabac7e9cb02081e46c2b190fbf65ad9b1cf37e44fa4`; locale: auto
- ก่อนฝึก focus/domain/facet/tasks: True/True/False/False
- หลังฝึก focus/domain/facet/tasks: True/True/True/True
- หลังฝึก contract: validated_source_quoted_interpretation; missing typed constraints: []

Gold plan:
```json
{
  "focus": "contact",
  "context_quotes": [],
  "tasks": [
    {
      "quote": "เบอร์ติดต่อคืออะไร",
      "domain": "contact",
      "operation": "detail",
      "facet": "value",
      "target": "",
      "constraints": [],
      "ambiguous": false
    }
  ]
}
```

ก่อนฝึก:
```
{
  "focus": "contact",
  "context_quotes": [
    "เบอร์ติดต่อคืออะไร"
  ],
  "tasks": [
    {
      "quote": "เบอร์ติดต่อคืออะไร",
      "domain": "contact",
      "operation": "detail",
      "facet": "contact",
      "target": "",
      "constraints": [
        {
          "slot": "audience",
          "quote": "",
          "source_record_id": ""
        }
      ],
      "ambiguous": false
    }
  ]
}
```

หลังฝึก:
```
{"focus":"contact","context_quotes":[],"tasks":[{"quote":"เบอร์ติดต่อคืออะไร","domain":"contact","operation":"detail","facet":"value","target":"","constraints":[],"ambiguous":false}]}
```

### 21. PC ช้กาดจอรุ่นอะไร

- key: `2fe50255e1804a59bbcac8aacf797072089fe2b4d5d3150a412ffe78b89bc3ab`; locale: auto
- ก่อนฝึก focus/domain/facet/tasks: False/True/False/False
- หลังฝึก focus/domain/facet/tasks: False/True/True/True
- หลังฝึก contract: validated_source_quoted_interpretation; missing typed constraints: [['platform', 'PC']]

Gold plan:
```json
{
  "focus": "hardware",
  "context_quotes": [
    "PC"
  ],
  "tasks": [
    {
      "quote": "PC ช้กาดจอรุ่นอะไร",
      "domain": "equipment",
      "operation": "detail",
      "facet": "specifications",
      "target": "",
      "constraints": [
        {
          "slot": "platform",
          "quote": "PC",
          "source_record_id": ""
        }
      ],
      "ambiguous": false
    }
  ]
}
```

ก่อนฝึก:
```
{
  "focus": "equipment_definition",
  "context_quotes": [
    "PC ช้กาดจอรุ่นอะไร"
  ],
  "tasks": [
    {
      "quote": "PC ช้กาดจอรุ่นอะไร",
      "domain": "equipment",
      "operation": "detail",
      "facet": "equipment_definition",
      "target": "",
      "constraints": [
        {
          "slot": "negation",
          "quote": "",
          "source_record_id": ""
        },
        {
          "slot": "audience",
          "quote": "",
          "source_record_id": ""
        },
        {
          "slot": "persons",
          "quote": "",
          "source_record_id": ""
        },
        {
          "slot": "duration",
          "quote": "",
          "source_record_id": ""
        },
        {
          "slot": "sessions",
          "quote": "",
          "source_record_id": ""
        },
        {
          "slot": "service",
          "quote": "",
          "source_record_id": ""
        },
        {
          "slot": "platform",
          "quote": "",
          "source_record_id": ""
        },
        {
          "slot": "date",
          "quote": "",
          "source_record_id": ""
        },
        {
          "slot": "time",
          "quote": "",
          "source_record_id": ""
        },
        {
          "slot": "event",
          "quote": "",
          "source_record_id": ""
        },
        {
          "slot": "condition",
          "quote": "",
          "source_record_id": ""
        },
        {
          "slot": "comparison",
          "quote": "",
          "source_record_id": ""
        },
        {
          "slot": "requested_scope",
          "quote": "",
          "source_record_id": ""
        },
        {
          "slot": "action",
          "quote": "",
          "source_record_id": ""
        }
      ],
      "ambiguous": false
    }
  ]
}
```

หลังฝึก:
```
{"focus":"equipment_definition","context_quotes":[],"tasks":[{"quote":"PC ช้กาดจอรุ่นอะไร","domain":"equipment","operation":"detail","facet":"specifications","target":"PC","constraints":[],"ambiguous":false}]}
```

### 22. How to book Cockpit and what days is it open?

- key: `a603ab1aed328e10dbf5ac72b6a752be2fb77658ea0365896a1776cd04806370`; locale: en
- ก่อนฝึก focus/domain/facet/tasks: False/False/False/False
- หลังฝึก focus/domain/facet/tasks: True/True/False/False
- หลังฝึก contract: validated_source_quoted_interpretation; missing typed constraints: [['service', 'Cockpit']]

Gold plan:
```json
{
  "focus": "multiple",
  "context_quotes": [
    "Cockpit"
  ],
  "tasks": [
    {
      "quote": "How to book Cockpit",
      "domain": "reservation",
      "operation": "detail",
      "facet": "owner_policy",
      "target": "",
      "constraints": [
        {
          "slot": "service",
          "quote": "Cockpit",
          "source_record_id": ""
        }
      ],
      "ambiguous": false
    },
    {
      "quote": "what days is it open",
      "domain": "schedule",
      "operation": "detail",
      "facet": "open_periods",
      "target": "",
      "constraints": [],
      "ambiguous": false
    }
  ]
}
```

ก่อนฝึก:
```
{
  "focus": "booking_procedure",
  "context_quotes": [
    "How to book Cockpit and what days is it open?"
  ],
  "tasks": [
    {
      "quote": "How to book Cockpit",
      "domain": "booking_procedure",
      "operation": "detail",
      "facet": "booking_procedure",
      "target": "",
      "constraints": [
        {
          "slot": "service",
          "quote": "Cockpit",
          "source_record_id": ""
        }
      ],
      "ambiguous": false
    },
    {
      "quote": "what days is it open?",
      "domain": "opening_hours",
      "operation": "detail",
      "facet": "opening_hours",
      "target": "",
      "constraints": [
        {
          "slot": "service",
          "quote": "Cockpit",
          "source_record_id": ""
        }
      ],
      "ambiguous": false
    }
  ]
}
```

หลังฝึก:
```
{"focus":"multiple","context_quotes":[],"tasks":[{"quote":"How to book Cockpit","domain":"reservation","operation":"detail","facet":"owner_policy","target":"","constraints":[],"ambiguous":false},{"quote":"what days is it open","domain":"schedule","operation":"detail","facet":"bookable_periods","target":"","constraints":[],"ambiguous":false}]}
```

### 23. Where is the gaming chair located?

- key: `a93872b2176765c50af14bf5a1a9a32d0d4f1b87b51c4f10493c99ce46e3ef77`; locale: en
- ก่อนฝึก focus/domain/facet/tasks: True/True/False/False
- หลังฝึก focus/domain/facet/tasks: True/True/True/True
- หลังฝึก contract: validated_source_quoted_interpretation; missing typed constraints: []

Gold plan:
```json
{
  "focus": "equipment_location",
  "context_quotes": [],
  "tasks": [
    {
      "quote": "Where is the gaming chair located?",
      "domain": "equipment",
      "operation": "detail",
      "facet": "location",
      "target": "gaming chair",
      "constraints": [],
      "ambiguous": false
    }
  ]
}
```

ก่อนฝึก:
```
{
  "focus": "equipment_location",
  "context_quotes": [
    "Where is the gaming chair located?"
  ],
  "tasks": [
    {
      "quote": "Where is the gaming chair located?",
      "domain": "equipment",
      "operation": "location",
      "facet": "equipment_location",
      "target": "",
      "constraints": [],
      "ambiguous": false
    }
  ]
}
```

หลังฝึก:
```
{"focus":"equipment_location","context_quotes":[],"tasks":[{"quote":"Where is the gaming chair located?","domain":"equipment","operation":"detail","facet":"location","target":"gaming chair","constraints":[],"ambiguous":false}]}
```

### 24. How much does it cost for a student from another university to play Cockpit for one hour, and how do I book it?

- key: `6f3e6d8df4f646b605f95de48ff2c1038a54d4a39af3037b27aef04b9726c579`; locale: en
- ก่อนฝึก focus/domain/facet/tasks: False/True/False/False
- หลังฝึก focus/domain/facet/tasks: True/True/True/True
- หลังฝึก contract: validated_source_quoted_interpretation; missing typed constraints: [['audience', 'student from another university'], ['duration', 'one hour'], ['service', 'Cockpit']]

Gold plan:
```json
{
  "focus": "multiple",
  "context_quotes": [
    "one hour",
    "student from another university",
    "Cockpit"
  ],
  "tasks": [
    {
      "quote": "How much does it cost for a student from another university to play Cockpit for one hour",
      "domain": "service_fee",
      "operation": "price_calculate",
      "facet": "amount",
      "target": "Cockpit",
      "constraints": [
        {
          "slot": "duration",
          "quote": "one hour",
          "source_record_id": ""
        },
        {
          "slot": "audience",
          "quote": "student from another university",
          "source_record_id": ""
        },
        {
          "slot": "service",
          "quote": "Cockpit",
          "source_record_id": ""
        }
      ],
      "ambiguous": false
    },
    {
      "quote": "how do I book it",
      "domain": "reservation",
      "operation": "detail",
      "facet": "owner_policy",
      "target": "",
      "constraints": [
        {
          "slot": "duration",
          "quote": "one hour",
          "source_record_id": ""
        },
        {
          "slot": "service",
          "quote": "Cockpit",
          "source_record_id": ""
        }
      ],
      "ambiguous": false
    }
  ]
}
```

ก่อนฝึก:
```
{
  "focus": "price",
  "context_quotes": [
    "How much does it cost for a student from another university to play Cockpit for one hour"
  ],
  "tasks": [
    {
      "quote": "How much does it cost for a student from another university to play Cockpit for one hour",
      "domain": "service_fee",
      "operation": "price_calculate",
      "facet": "price",
      "target": "amount",
      "constraints": [
        {
          "slot": "audience",
          "quote": "student from another university",
          "source_record_id": ""
        },
        {
          "slot": "service",
          "quote": "Cockpit",
          "source_record_id": ""
        },
        {
          "slot": "duration",
          "quote": "one hour",
          "source_record_id": ""
        }
      ],
      "ambiguous": false
    },
    {
      "quote": "and how do I book it?",
      "domain": "reservation",
      "operation": "availability",
      "facet": "booking_procedure",
      "target": "",
      "constraints": [
        {
          "slot": "service",
          "quote": "Cockpit",
          "source_record_id": ""
        }
      ],
      "ambiguous": false
    }
  ]
}
```

หลังฝึก:
```
{"focus":"multiple","context_quotes":[],"tasks":[{"quote":"How much does it cost for a student from another university to play Cockpit for one hour","domain":"service_fee","operation":"price_calculate","facet":"amount","target":"Cockpit","constraints":[],"ambiguous":false},{"quote":"how do I book it","domain":"reservation","operation":"detail","facet":"owner_policy","target":"","constraints":[],"ambiguous":false}]}
```

### 25. is there any free slot from 14:00 to 15:00 ?

- key: `7dc976a448677ceb0b0642a5446263d7c2c9a53043e5fad402054797cfd82016`; locale: en
- ก่อนฝึก focus/domain/facet/tasks: False/False/False/False
- หลังฝึก focus/domain/facet/tasks: False/False/False/False
- หลังฝึก contract: validated_source_quoted_interpretation; missing typed constraints: [['time', '14:00'], ['time', '15:00']]

Gold plan:
```json
{
  "focus": "live_status",
  "context_quotes": [
    "14:00",
    "15:00"
  ],
  "tasks": [
    {
      "quote": "is there any free slot from 14:00 to 15:00 ?",
      "domain": "live",
      "operation": "availability",
      "facet": "live_status",
      "target": "",
      "constraints": [
        {
          "slot": "time",
          "quote": "14:00",
          "source_record_id": ""
        },
        {
          "slot": "time",
          "quote": "15:00",
          "source_record_id": ""
        }
      ],
      "ambiguous": true
    }
  ]
}
```

ก่อนฝึก:
```
{
  "focus": "availability",
  "context_quotes": [
    "is there any free slot from 14:00 to 15:00 ?"
  ],
  "tasks": [
    {
      "quote": "is there any free slot from 14:00 to 15:00 ?",
      "domain": "availability",
      "operation": "availability",
      "facet": "bookable_periods",
      "target": "",
      "constraints": [
        {
          "slot": "negation",
          "quote": "is there any",
          "source_record_id": ""
        },
        {
          "slot": "time",
          "quote": "from 14:00 to 15:00",
          "source_record_id": ""
        }
      ],
      "ambiguous": false
    }
  ]
}
```

หลังฝึก:
```
{"focus":"bookable_periods","context_quotes":[],"tasks":[{"quote":"is there any free slot from 14:00 to 15:00 ?","domain":"schedule","operation":"availability","facet":"bookable_periods","target":"","constraints":[],"ambiguous":false}]}
```

### 26. Where can I play it? Please use verified information.

- key: `27541a305e44698636412bf6556e3a545bf91e52357a068b098c96e449f31157`; locale: en
- ก่อนฝึก focus/domain/facet/tasks: True/True/False/False
- หลังฝึก focus/domain/facet/tasks: True/True/True/False
- หลังฝึก contract: validated_source_quoted_interpretation; missing typed constraints: []

Gold plan:
```json
{
  "focus": "game_location",
  "context_quotes": [],
  "tasks": [
    {
      "quote": "Where can I play it? Please use verified information.",
      "domain": "games",
      "operation": "detail",
      "facet": "zone",
      "target": "",
      "constraints": [],
      "ambiguous": true
    }
  ]
}
```

ก่อนฝึก:
```
{
  "focus": "game_location",
  "context_quotes": [
    "Where can I play it? Please use verified information."
  ],
  "tasks": [
    {
      "quote": "Where can I play it? Please use verified information.",
      "domain": "games",
      "operation": "availability",
      "facet": "game_location",
      "target": "",
      "constraints": [
        {
          "slot": "audience",
          "quote": "Where can I play it? Please use verified information.",
          "source_record_id": ""
        }
      ],
      "ambiguous": false
    }
  ]
}
```

หลังฝึก:
```
{"focus":"game_location","context_quotes":[],"tasks":[{"quote":"Where can I play it? Please use verified information.","domain":"games","operation":"detail","facet":"zone","target":"it","constraints":[],"ambiguous":false}]}
```

### 27. ถ้าทำเครื่อง Nintendo Switch ตกจะมีค่าปรับไหม

- key: `737ff3d31b174cda802050dc5c2d732fe5166938d56d7d69da6eef37131b703c`; locale: th
- ก่อนฝึก focus/domain/facet/tasks: True/False/False/False
- หลังฝึก focus/domain/facet/tasks: True/True/True/True
- หลังฝึก contract: validated_source_quoted_interpretation; missing typed constraints: [['condition', 'ถ้าทำเครื่อง Nintendo Switch ตกจะมีค่าปรับไหม'], ['platform', 'Nintendo Switch']]

Gold plan:
```json
{
  "focus": "damage",
  "context_quotes": [
    "ถ้าทำเครื่อง Nintendo Switch ตกจะมีค่าปรับไหม",
    "Nintendo Switch"
  ],
  "tasks": [
    {
      "quote": "ถ้าทำเครื่อง Nintendo Switch ตกจะมีค่าปรับไหม",
      "domain": "rules",
      "operation": "detail",
      "facet": "owner_policy",
      "target": "",
      "constraints": [
        {
          "slot": "condition",
          "quote": "ถ้าทำเครื่อง Nintendo Switch ตกจะมีค่าปรับไหม",
          "source_record_id": ""
        },
        {
          "slot": "platform",
          "quote": "Nintendo Switch",
          "source_record_id": ""
        }
      ],
      "ambiguous": false
    }
  ]
}
```

ก่อนฝึก:
```
{
  "focus": "damage",
  "context_quotes": [
    "ถ้าทำเครื่อง Nintendo Switch ตกจะมีค่าปรับไหม"
  ],
  "tasks": [
    {
      "quote": "ถ้าทำเครื่อง Nintendo Switch ตกจะมีค่าปรับไหม",
      "domain": "equipment",
      "operation": "rule_lookup",
      "facet": "rules",
      "target": "",
      "constraints": [
        {
          "slot": "negation",
          "quote": "ถ้า",
          "source_record_id": ""
        },
        {
          "slot": "audience",
          "quote": "ถ้าทำเครื่อง Nintendo Switch ตก",
          "source_record_id": ""
        },
        {
          "slot": "action",
          "quote": "จะมีค่าปรับไหม",
          "source_record_id": ""
        }
      ],
      "ambiguous": false
    }
  ]
}
```

หลังฝึก:
```
{"focus":"damage","context_quotes":[],"tasks":[{"quote":"ถ้าทำเครื่อง Nintendo Switch ตกจะมีค่าปรับไหม","domain":"rules","operation":"detail","facet":"owner_policy","target":"","constraints":[],"ambiguous":false}]}
```

### 28. นายเปนคัยแล้วทำไรไดบ้าง

- key: `4276abf4fadb569677abb1569e9a37271cd1a36a3f5a28ad639d75b45381d731`; locale: auto
- ก่อนฝึก focus/domain/facet/tasks: False/True/True/True
- หลังฝึก focus/domain/facet/tasks: False/True/True/True
- หลังฝึก contract: validated_source_quoted_interpretation; missing typed constraints: []

Gold plan:
```json
{
  "focus": "identity",
  "context_quotes": [],
  "tasks": [
    {
      "quote": "นายเปนคัยแล้วทำไรไดบ้าง",
      "domain": "general",
      "operation": "detail",
      "facet": "",
      "target": "",
      "constraints": [],
      "ambiguous": false
    }
  ]
}
```

ก่อนฝึก:
```
{
  "focus": "general",
  "context_quotes": [
    "นายเปนคัยแล้วทำไรไดบ้าง"
  ],
  "tasks": [
    {
      "quote": "นายเปนคัยแล้วทำไรไดบ้าง",
      "domain": "general",
      "operation": "detail",
      "facet": "",
      "target": "",
      "constraints": [],
      "ambiguous": false
    }
  ]
}
```

หลังฝึก:
```
{"focus":"general","context_quotes":[],"tasks":[{"quote":"นายเปนคัยแล้วทำไรไดบ้าง","domain":"general","operation":"detail","facet":"","target":"","constraints":[],"ambiguous":false}]}
```

### 29. มีเกมแข่งนดมั้ยย

- key: `ab2f8972dde3005af36e57e96b899bf9613410ee746623f53888ba3bd47cad2b`; locale: auto
- ก่อนฝึก focus/domain/facet/tasks: True/True/True/False
- หลังฝึก focus/domain/facet/tasks: False/False/False/False
- หลังฝึก contract: validated_source_quoted_interpretation; missing typed constraints: []

Gold plan:
```json
{
  "focus": "game_catalog",
  "context_quotes": [],
  "tasks": [
    {
      "quote": "มีเกมแข่งนดมั้ยย",
      "domain": "games",
      "operation": "list",
      "facet": "game_catalog",
      "target": "",
      "constraints": [],
      "ambiguous": false
    }
  ]
}
```

ก่อนฝึก:
```
{
  "focus": "game_catalog",
  "context_quotes": [
    "มีเกมแข่งนดมั้ยย"
  ],
  "tasks": [
    {
      "quote": "มีเกมแข่งนดมั้ยย",
      "domain": "games",
      "operation": "availability",
      "facet": "game_catalog",
      "target": "",
      "constraints": [],
      "ambiguous": false
    }
  ]
}
```

หลังฝึก:
```
{"focus":"competition_rules","context_quotes":[],"tasks":[{"quote":"มีเกมแข่งนดมั้ยย","domain":"competition_rules","operation":"list","facet":"rule_clause","target":"","constraints":[],"ambiguous":false}]}
```

### 30. Please use verified studio information: What ID does an external visitor need to use the studio?

- key: `1cf7db3858a13e4841f441117b1a23c40c3e46cf26be6bc9d0b7bb64314f0993`; locale: en
- ก่อนฝึก focus/domain/facet/tasks: False/False/False/False
- หลังฝึก focus/domain/facet/tasks: False/False/False/False
- หลังฝึก contract: vocabulary; missing typed constraints: []

Gold plan:
```json
{
  "focus": "booking_policy",
  "context_quotes": [],
  "tasks": [
    {
      "quote": "Please use verified studio information: What ID does an external visitor need to use the studio?",
      "domain": "reservation",
      "operation": "detail",
      "facet": "owner_policy",
      "target": "",
      "constraints": [],
      "ambiguous": false
    }
  ]
}
```

ก่อนฝึก:
```
{
  "focus": "identity",
  "context_quotes": [
    "What ID does an external visitor need to use the studio?"
  ],
  "tasks": [
    {
      "quote": "What ID does an external visitor need to use the studio?",
      "domain": "identity",
      "operation": "detail",
      "facet": "identity",
      "target": "",
      "constraints": [
        {
          "slot": "audience",
          "quote": "external visitor",
          "source_record_id": ""
        }
      ],
      "ambiguous": false
    }
  ]
}
```

หลังฝึก:
```
{"focus":"identity","context_quotes":[],"tasks":[{"quote":"Please use verified studio information: What ID does an external visitor need to use the studio?","domain":"identity","operation":"detail","facet":"value","target":"","constraints":[],"ambiguous":false}]}
```
