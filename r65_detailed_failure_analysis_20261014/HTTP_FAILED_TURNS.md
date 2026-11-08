# HTTP failuresที่ใช้protocolถูก

อ่านผลจริงทุกturnที่ไม่ผ่าน แยกliteral expectation/transport/เนื้อหา; serverstateอยู่ในOBSERVATIONS.json

## legacy session9 turn2: สรุปคือทำยังไง

```json
{
  "session": 8,
  "turn": 1,
  "q": "สรุปคือทำยังไง",
  "failures": [
    "missing required: ขั้นตอนจอง"
  ],
  "answer": "จองคิวเล่นเกม/ใช้อุปกรณ์ได้ผ่านระบบจองออนไลน์ครับ\nขั้นตอนโดยสรุปคือ 1) เลือกบริการหรือโซนที่ต้องการใช้ 2) เลือกวันและรอบเวลา 3) กรอก Student ID/Staff ID/National ID ชื่อ นามสกุล อีเมล และเบอร์โทรศัพท์ 4) ตรวจสอบข้อมูลและชำระเงินโดยโอนเข้าบัญชีที่ระบบแจ้ง 5) แนบสลิปและยืนยันการจอง\nต้องจองล่วงหน้าอย่างน้อย 1 ชั่วโมง และหลังจองต้องชำระเงินภายใน 10 นาทีครับ\nแหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation",
  "mode": "pipeline:source_operation_booking_how_to",
  "state": {
    "schema_version": 1,
    "revision": 2,
    "active_task": null,
    "task_memory_schema_version": 1,
    "requested_tasks": [
      {
        "schema_version": 1,
        "key": "reservation/booking_policy",
        "domain": "reservation",
        "operation": "booking_policy",
        "targets": [],
        "offered_options": [],
        "query": "สรุปขั้นตอนจองทำยังไง",
        "price_task": null,
        "rental_plan": null,
        "seed_question": "สรุปคือทำยังไง",
        "mode": "pipeline:source_operation_booking_how_to",
        "route_category": "reservation",
        "route_intent": "booking_how_to",
        "response_id": "c2ddb3cda7074f68acec5d6f4babffe2",
        "status": "answered",
        "provenance": "server_completed_user_request",
        "acknowledged": false
      }
    ],
    "current_task_keys": [
      "reservation/booking_policy"
    ],
    "delivery": {
      "r64-evaluation-turn-8-0": "client_acknowledged",
      "r64-evaluation-turn-8-1": "prepared"
    },
    "storage": "sqlite_parent_state",
    "survives_server_restart": true,
    "persistence": {
      "enabled": true,
      "ready": true,
      "last_error": "",
      "writes": 82,
      "restores": 0
    }
  },
  "task_contract": {
    "schema_version": 1,
    "kind": "single",
    "status": "answered",
    "outcome": "answered_complete",
    "category": "reservation",
    "intent": "booking_how_to",
    "source_count": 1,
    "coverage_meaning": "execution_status_not_factual_accuracy"
  }
}
```

## legacy session11 turn2: แล้วแต่ละหมวดมีใครบ้าง

```json
{
  "session": 10,
  "turn": 1,
  "q": "แล้วแต่ละหมวดมีใครบ้าง",
  "failures": [
    "missing required: Members",
    "missing required: cooperative"
  ],
  "answer": "คำถามนี้ยังกว้างเกินไปครับ ยังไม่แน่ใจว่าต้องการถามเรื่องไหนของ PSU Esports Studio - Phuket\nถามให้เจาะจงได้ เช่น `มีเกมอะไรบ้าง`, `มีอุปกรณ์อะไรบ้าง`, `จองยังไง`, `ราคา PS5 เท่าไหร่` หรือ `TEKKEN 8 มีปุ่มอะไรบ้าง`",
  "mode": "pipeline:ambiguity_clarification",
  "state": {
    "schema_version": 1,
    "revision": 2,
    "active_task": null,
    "task_memory_schema_version": 1,
    "requested_tasks": [
      {
        "schema_version": 1,
        "key": "reservation/booking_policy",
        "domain": "reservation",
        "operation": "booking_policy",
        "targets": [],
        "offered_options": [],
        "query": "สมาชิก PSU Esport มีกี่หมวด",
        "price_task": null,
        "rental_plan": null,
        "seed_question": "สมาชิก PSU Esport มีกี่หมวด",
        "mode": "pipeline:user_service_facts",
        "route_category": "reservation",
        "route_intent": "user_service_facts",
        "response_id": "cc6fd5126cad4f8fb2dc433836d5dcea",
        "status": "answered",
        "provenance": "server_completed_user_request",
        "acknowledged": true
      }
    ],
    "current_task_keys": [],
    "delivery": {
      "r64-evaluation-turn-10-0": "client_acknowledged",
      "r64-evaluation-turn-10-1": "prepared"
    },
    "storage": "sqlite_parent_state",
    "survives_server_restart": true,
    "persistence": {
      "enabled": true,
      "ready": true,
      "last_error": "",
      "writes": 96,
      "restores": 0
    }
  },
  "task_contract": {
    "schema_version": 1,
    "kind": "single",
    "status": "clarification",
    "outcome": "needs_clarification",
    "category": "clarification",
    "intent": "ambiguity_gate_clarification",
    "source_count": 0,
    "coverage_meaning": "execution_status_not_factual_accuracy"
  }
}
```

## common session1 turn2: ปุ่ม

```json
{
  "session": 0,
  "turn": 1,
  "q": "ปุ่ม",
  "failures": [
    "transport:<HTTPError 409: 'Conflict'>"
  ],
  "answer": null,
  "mode": null,
  "state": null,
  "task_contract": null
}
```

## common session2 turn2: ปุ่มเร่งเครื่องกดอะไร

```json
{
  "session": 1,
  "turn": 1,
  "q": "ปุ่มเร่งเครื่องกดอะไร",
  "failures": [
    "missing required: Mario Kart 8 Deluxe",
    "missing required: เร่งเครื่อง"
  ],
  "answer": "**มาริโอ้คาร์ท 8**\n• ปุ่มควบคุม: เพิ่มทีละปุ่มหรือชุดปุ่ม: ยังไม่มีข้อมูลยืนยัน\n• แพลตฟอร์ม เช่น PC หรือ PS5: Nintendo Switch [S1]\n• อุปกรณ์ควบคุม: ยังไม่มีข้อมูลยืนยัน\n• ชื่อชุดปุ่ม เช่น default: ยังไม่มีข้อมูลยืนยัน",
  "mode": "pipeline:common_answer",
  "state": {
    "schema_version": 1,
    "revision": 2,
    "active_task": null,
    "task_memory_schema_version": 1,
    "requested_tasks": [],
    "current_task_keys": [],
    "delivery": {
      "r64-evaluation-turn-1-0": "client_acknowledged",
      "r64-evaluation-turn-1-1": "prepared"
    },
    "storage": "sqlite_parent_state",
    "survives_server_restart": true,
    "persistence": {
      "enabled": true,
      "ready": true,
      "last_error": "",
      "writes": 39,
      "restores": 0
    }
  },
  "task_contract": {}
}
```

## common session3 turn2: ราคา

```json
{
  "session": 2,
  "turn": 1,
  "q": "ราคา",
  "failures": [
    "missing required: TEKKEN 8"
  ],
  "answer": "**ค่าบริการ**\nข้อมูลรุ่นนี้หรือรายการที่อ้างอิงยังไม่ถึงวันมีผลหรือหมดอายุแล้ว จึงยังยืนยันข้อมูลปัจจุบันไม่ได้\n\n**ค่าบริการ**\nข้อมูลรุ่นนี้หรือรายการที่อ้างอิงยังไม่ถึงวันมีผลหรือหมดอายุแล้ว จึงยังยืนยันข้อมูลปัจจุบันไม่ได้\n\n**ค่าบริการ**\nข้อมูลรุ่นนี้หรือรายการที่อ้างอิงยังไม่ถึงวันมีผลหรือหมดอายุแล้ว จึงยังยืนยันข้อมูลปัจจุบันไม่ได้\n\nยังไม่มีราคาที่ได้รับการยืนยันในขอบเขตนี้\n\nยังไม่มีราคาที่ได้รับการยืนยันในขอบเขตนี้\n\nยังไม่มีราคาที่ได้รับการยืนยันในขอบเขตนี้\n\n**ค่าบริการ**\nข้อมูลรุ่นนี้หรือรายการที่อ้างอิงยังไม่ถึงวันมีผลหรือหมดอายุแล้ว จึงยังยืนยันข้อมูลปัจจุบันไม่ได้\n\n**ค่าบริการ**\nข้อมูลรุ่นนี้หรือรายการที่อ้างอิงยังไม่ถึงวันมีผลหรือหมดอายุแล้ว จึงยังยืนยันข้อมูลปัจจุบันไม่ได้\n\n**ค่าบริการ**\nข้อมูลรุ่นนี้หรือรายการที่อ้างอิงยังไม่ถึงวันมีผลหรือหมดอายุแล้ว จึงยังยืนยันข้อมูลปัจจุบันไม่ได้\n\namount_minor: หัวข้อนี้อยู่นอกขอบเขตรายการที่เลือก กรุณาระบุบริการหรือรายการที่เกี่ยวข้อง",
  "mode": "pipeline:common_answer",
  "state": {
    "schema_version": 1,
    "revision": 2,
    "active_task": null,
    "task_memory_schema_version": 1,
    "requested_tasks": [],
    "current_task_keys": [],
    "delivery": {
      "r64-evaluation-turn-2-0": "client_acknowledged",
      "r64-evaluation-turn-2-1": "prepared"
    },
    "storage": "sqlite_parent_state",
    "survives_server_restart": true,
    "persistence": {
      "enabled": true,
      "ready": true,
      "last_error": "",
      "writes": 46,
      "restores": 0
    }
  },
  "task_contract": {}
}
```

## common session4 turn2: เกม

```json
{
  "session": 3,
  "turn": 1,
  "q": "เกม",
  "failures": [
    "missing required: PC",
    "missing required: เกม"
  ],
  "answer": "รายการที่เผยแพร่ในฐานข้อมูลกลาง: 48\n• Animal Crossing: New Horizons\n• Beat Saber\n• Call of Duty: Modern Warfare III\n• Counter-Strike 2\n• EA Sports FC 24\n• FINAL FANTASY XVI\n• Fortnite\n• God of War Ragnarok\n• Gran Turismo 7\n• Hogwarts Legacy\n• Horizon Call of the Mountain\n• It Takes Two\n• League of Legends\n• Little Nightmares II\n• Luigi's Mansion 3\n• Mario Kart 8 Deluxe\n• Mario Party Superstars\n• Monster Hunter Rise\n• Moving Out 2\n• NARUTO X BORUTO Ultimate Ninja Storm Connections\n• New Super Mario Bros. U Deluxe\n• Overcooked 2\n• PUBG: BATTLEGROUNDS\n• Resident Evil 4\n• Resident Evil Village\n• Ring Fit Adventure\n• Marvel's Spider-Man 2\n• Super Mario Odyssey\n• Super Smash Bros Ultimate\n• Nintendo Switch Sports\n• TEKKEN 8\n• The Last of Us Part I / Part II\n• Uncharted: Legacy of Thieves Collection\n• VALORANT\n• Call of Duty: Warzone\n• The Legend of Zelda: Breath of the Wild\n• Arena of Valor (RoV)\n• Delta Force\n• eFootball\n• God of War Ragnarök\n• Mario Kart Live: Home Circuit\n• Overcooked!\n• Pokémon Champions\n• Resident Evil 4 (Remake)\n• THE FINALS\n• The Last of Us Part I\n• The Last of Us Part II\n• The Last of Us Part II (Remastered)",
  "mode": "pipeline:common_list",
  "state": {
    "schema_version": 1,
    "revision": 2,
    "active_task": null,
    "task_memory_schema_version": 1,
    "requested_tasks": [],
    "current_task_keys": [],
    "delivery": {
      "r64-evaluation-turn-3-0": "client_acknowledged",
      "r64-evaluation-turn-3-1": "prepared"
    },
    "storage": "sqlite_parent_state",
    "survives_server_restart": true,
    "persistence": {
      "enabled": true,
      "ready": true,
      "last_error": "",
      "writes": 53,
      "restores": 0
    }
  },
  "task_contract": {}
}
```

## common session6 turn2: อุปกรณ์

```json
{
  "session": 5,
  "turn": 1,
  "q": "อุปกรณ์",
  "failures": [
    "missing required: อุปกรณ์"
  ],
  "answer": "รายการที่เผยแพร่ในฐานข้อมูลกลาง: 14\n• Cockpit #01\n• Cockpit #02\n• PC #01\n• PC #02\n• PC #03\n• PC #04\n• PC #05\n• PC #06\n• PC #07\n• PC #08\n• PC #09\n• PC #10\n• PlayStation 5 #01\n• PlayStation 5 #02\n\nรายการเดิมที่ยังไม่ได้ย้ายและอนุมัติในฐานข้อมูลกลางไม่รวมในรายการนี้",
  "mode": "pipeline:common_list",
  "state": {
    "schema_version": 1,
    "revision": 2,
    "active_task": null,
    "task_memory_schema_version": 1,
    "requested_tasks": [],
    "current_task_keys": [],
    "delivery": {
      "r64-evaluation-turn-5-0": "client_acknowledged",
      "r64-evaluation-turn-5-1": "prepared"
    },
    "storage": "sqlite_parent_state",
    "survives_server_restart": true,
    "persistence": {
      "enabled": true,
      "ready": true,
      "last_error": "",
      "writes": 67,
      "restores": 0
    }
  },
  "task_contract": {}
}
```

## common session7 turn2: จอง

```json
{
  "session": 6,
  "turn": 1,
  "q": "จอง",
  "failures": [
    "missing required: PC"
  ],
  "answer": "ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ วิธีจอง เช่น คำถามตั้งต้น ไม่จำเป็นต้องเก็บทุก paraphrase / คำตอบพร้อมหลักฐานของศูนย์ / หัวข้อเชิงความหมาย?",
  "mode": "pipeline:common_clarification",
  "state": {
    "schema_version": 1,
    "revision": 2,
    "active_task": null,
    "task_memory_schema_version": 1,
    "requested_tasks": [],
    "current_task_keys": [],
    "delivery": {
      "r64-evaluation-turn-6-0": "client_acknowledged",
      "r64-evaluation-turn-6-1": "prepared"
    },
    "storage": "sqlite_parent_state",
    "survives_server_restart": true,
    "persistence": {
      "enabled": true,
      "ready": true,
      "last_error": "",
      "writes": 74,
      "restores": 0
    }
  },
  "task_contract": {}
}
```

## common session8 turn2: แล้วจะเล่นต้องทำไง

```json
{
  "session": 7,
  "turn": 1,
  "q": "แล้วจะเล่นต้องทำไง",
  "failures": [
    "missing required: NARUTO",
    "missing required: จอง"
  ],
  "answer": "ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ นารูโตะ เอ็กซ์ โบรูโตะ เช่น แพลตฟอร์ม เช่น PC หรือ PS5 / อุปกรณ์ควบคุม / ชื่อชุดปุ่ม เช่น default / ปุ่มควบคุม: เพิ่มทีละปุ่มหรือชุดปุ่ม?",
  "mode": "pipeline:common_clarification",
  "state": {
    "schema_version": 1,
    "revision": 2,
    "active_task": null,
    "task_memory_schema_version": 1,
    "requested_tasks": [],
    "current_task_keys": [],
    "delivery": {
      "r64-evaluation-turn-7-0": "client_acknowledged",
      "r64-evaluation-turn-7-1": "prepared"
    },
    "storage": "sqlite_parent_state",
    "survives_server_restart": true,
    "persistence": {
      "enabled": true,
      "ready": true,
      "last_error": "",
      "writes": 81,
      "restores": 0
    }
  },
  "task_contract": {}
}
```

## common session9 turn2: สรุปคือทำยังไง

```json
{
  "session": 8,
  "turn": 1,
  "q": "สรุปคือทำยังไง",
  "failures": [
    "missing required: ขั้นตอนจอง",
    "missing required: เลือกบริการ"
  ],
  "answer": "ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ วิธีจอง เช่น คำถามตั้งต้น ไม่จำเป็นต้องเก็บทุก paraphrase / คำตอบพร้อมหลักฐานของศูนย์ / หัวข้อเชิงความหมาย?",
  "mode": "pipeline:common_clarification",
  "state": {
    "schema_version": 1,
    "revision": 2,
    "active_task": null,
    "task_memory_schema_version": 1,
    "requested_tasks": [
      {
        "schema_version": 1,
        "key": "reservation/booking_policy",
        "domain": "reservation",
        "operation": "booking_policy",
        "targets": [],
        "offered_options": [],
        "query": "แล้วจองไง",
        "price_task": null,
        "rental_plan": null,
        "seed_question": "แล้วจองไง",
        "mode": "pipeline:structured_reservation_fact",
        "route_category": "reservation",
        "route_intent": "booking_policy",
        "response_id": "11d05ac9f5bb40d0a24a6dc141b7f832",
        "status": "answered",
        "provenance": "server_completed_user_request",
        "acknowledged": true
      }
    ],
    "current_task_keys": [],
    "delivery": {
      "r64-evaluation-turn-8-0": "client_acknowledged",
      "r64-evaluation-turn-8-1": "prepared"
    },
    "storage": "sqlite_parent_state",
    "survives_server_restart": true,
    "persistence": {
      "enabled": true,
      "ready": true,
      "last_error": "",
      "writes": 88,
      "restores": 0
    }
  },
  "task_contract": {}
}
```

## common session10 turn2: แล้วมีเกมอะไรบ้าง

```json
{
  "session": 9,
  "turn": 1,
  "q": "แล้วมีเกมอะไรบ้าง",
  "failures": [
    "missing required: PlayStation 5",
    "missing required: เกม"
  ],
  "answer": "รายการที่เผยแพร่ในฐานข้อมูลกลาง: 48\n• Animal Crossing: New Horizons\n• Beat Saber\n• Call of Duty: Modern Warfare III\n• Counter-Strike 2\n• EA Sports FC 24\n• FINAL FANTASY XVI\n• Fortnite\n• God of War Ragnarok\n• Gran Turismo 7\n• Hogwarts Legacy\n• Horizon Call of the Mountain\n• It Takes Two\n• League of Legends\n• Little Nightmares II\n• Luigi's Mansion 3\n• Mario Kart 8 Deluxe\n• Mario Party Superstars\n• Monster Hunter Rise\n• Moving Out 2\n• NARUTO X BORUTO Ultimate Ninja Storm Connections\n• New Super Mario Bros. U Deluxe\n• Overcooked 2\n• PUBG: BATTLEGROUNDS\n• Resident Evil 4\n• Resident Evil Village\n• Ring Fit Adventure\n• Marvel's Spider-Man 2\n• Super Mario Odyssey\n• Super Smash Bros Ultimate\n• Nintendo Switch Sports\n• TEKKEN 8\n• The Last of Us Part I / Part II\n• Uncharted: Legacy of Thieves Collection\n• VALORANT\n• Call of Duty: Warzone\n• The Legend of Zelda: Breath of the Wild\n• Arena of Valor (RoV)\n• Delta Force\n• eFootball\n• God of War Ragnarök\n• Mario Kart Live: Home Circuit\n• Overcooked!\n• Pokémon Champions\n• Resident Evil 4 (Remake)\n• THE FINALS\n• The Last of Us Part I\n• The Last of Us Part II\n• The Last of Us Part II (Remastered)",
  "mode": "pipeline:common_list",
  "state": {
    "schema_version": 1,
    "revision": 2,
    "active_task": null,
    "task_memory_schema_version": 1,
    "requested_tasks": [
      {
        "schema_version": 1,
        "key": "games/list",
        "domain": "games",
        "operation": "list",
        "targets": [
          "ps5"
        ],
        "offered_options": [],
        "query": "PS5 มีเกมกี่เกม",
        "price_task": null,
        "rental_plan": null,
        "seed_question": "PS5 มีเกมกี่เกม",
        "mode": "pipeline:source_operation_game_list",
        "route_category": "games",
        "route_intent": "game_list",
        "response_id": "43792ec0af3942fa962b35baf11775df",
        "status": "answered",
        "provenance": "server_completed_user_request",
        "acknowledged": true
      }
    ],
    "current_task_keys": [],
    "delivery": {
      "r64-evaluation-turn-9-0": "client_acknowledged",
      "r64-evaluation-turn-9-1": "prepared"
    },
    "storage": "sqlite_parent_state",
    "survives_server_restart": true,
    "persistence": {
      "enabled": true,
      "ready": true,
      "last_error": "",
      "writes": 95,
      "restores": 0
    }
  },
  "task_contract": {}
}
```

## common session11 turn2: แล้วแต่ละหมวดมีใครบ้าง

```json
{
  "session": 10,
  "turn": 1,
  "q": "แล้วแต่ละหมวดมีใครบ้าง",
  "failures": [
    "missing required: Members",
    "missing required: cooperative"
  ],
  "answer": "คำถามนี้ยังกว้างเกินไปครับ ยังไม่แน่ใจว่าต้องการถามเรื่องไหนของ PSU Esports Studio - Phuket\nถามให้เจาะจงได้ เช่น `มีเกมอะไรบ้าง`, `มีอุปกรณ์อะไรบ้าง`, `จองยังไง`, `ราคา PS5 เท่าไหร่` หรือ `TEKKEN 8 มีปุ่มอะไรบ้าง`",
  "mode": "pipeline:ambiguity_clarification",
  "state": {
    "schema_version": 1,
    "revision": 2,
    "active_task": null,
    "task_memory_schema_version": 1,
    "requested_tasks": [
      {
        "schema_version": 1,
        "key": "reservation/booking_policy",
        "domain": "reservation",
        "operation": "booking_policy",
        "targets": [],
        "offered_options": [],
        "query": "สมาชิก PSU Esport มีกี่หมวด",
        "price_task": null,
        "rental_plan": null,
        "seed_question": "สมาชิก PSU Esport มีกี่หมวด",
        "mode": "pipeline:user_service_facts",
        "route_category": "reservation",
        "route_intent": "user_service_facts",
        "response_id": "2195db29c1ed4736b425402670276fbf",
        "status": "answered",
        "provenance": "server_completed_user_request",
        "acknowledged": true
      }
    ],
    "current_task_keys": [],
    "delivery": {
      "r64-evaluation-turn-10-0": "client_acknowledged",
      "r64-evaluation-turn-10-1": "prepared"
    },
    "storage": "sqlite_parent_state",
    "survives_server_restart": true,
    "persistence": {
      "enabled": true,
      "ready": true,
      "last_error": "",
      "writes": 102,
      "restores": 0
    }
  },
  "task_contract": {
    "schema_version": 1,
    "kind": "single",
    "status": "clarification",
    "outcome": "needs_clarification",
    "category": "clarification",
    "intent": "ambiguity_gate_clarification",
    "source_count": 0,
    "coverage_meaning": "execution_status_not_factual_accuracy"
  }
}
```

## common session12 turn2: จองเครื่องยังไง

```json
{
  "session": 11,
  "turn": 1,
  "q": "จองเครื่องยังไง",
  "failures": [
    "missing required: เลือกบริการ"
  ],
  "answer": "ยังตีความหัวข้อที่ถามไม่ชัด ต้องการส่วนใดของ วิธีจอง เช่น คำถามตั้งต้น ไม่จำเป็นต้องเก็บทุก paraphrase / คำตอบพร้อมหลักฐานของศูนย์ / หัวข้อเชิงความหมาย?",
  "mode": "pipeline:common_clarification",
  "state": {
    "schema_version": 1,
    "revision": 2,
    "active_task": null,
    "task_memory_schema_version": 1,
    "requested_tasks": [],
    "current_task_keys": [],
    "delivery": {
      "r64-evaluation-turn-11-0": "client_acknowledged",
      "r64-evaluation-turn-11-1": "prepared"
    },
    "storage": "sqlite_parent_state",
    "survives_server_restart": true,
    "persistence": {
      "enabled": true,
      "ready": true,
      "last_error": "",
      "writes": 109,
      "restores": 0
    }
  },
  "task_contract": {}
}
```
