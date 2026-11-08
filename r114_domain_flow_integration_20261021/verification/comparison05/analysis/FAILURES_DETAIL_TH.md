# ข้อที่ไม่ผ่าน strict ทุกข้อ

การจัดกลุ่มอัตโนมัติด้านล่างยังไม่ใช่การตัดสิน semantic โดยมนุษย์

## same_source_hinted / C12-Q061 / C12

**คำถาม:** Is PC #09 / 2026-10-21 09:00 available? and also Can you check whether PC #10 / 2026-10-21 12:00 is already booked?

**คำตอบ:**

```text
PC #09 / 2026-10-21 09:00 — live availability: Available [S1]

PC #10 / 2026-10-21 12:00 — live availability: Stale data; occupancy is not confirmed [S2]
```

**สถานะ:** answer → partial

**การเลือก:** exact_live_snapshot, exact_live_snapshot

```json
{
  "missing_claims": [],
  "unrequested_claims": [],
  "wrong_values": [],
  "evidence_mismatches": []
}
```

**Expected source refs และ actual claims:**

```json
{
  "expected": [
    {
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
    },
    {
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
  ],
  "actual": [
    {
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
      ],
      "fixture": true,
      "status": "answer"
    },
    {
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
      ],
      "fixture": true,
      "status": "unavailable"
    }
  ]
}
```

## same_source_hinted / C12-Q062 / C12

**คำถาม:** Could you help me with this: Can you check whether PlayStation 5 #02 / 2026-10-21 11:00 is already booked? and also Is PlayStation 5 #01 / 2026-10-21 09:00 available?

**คำตอบ:**

```text
PlayStation 5 #02 / 2026-10-21 11:00 — live availability: Provider unavailable; occupancy is not confirmed [S1]

PlayStation 5 #01 / 2026-10-21 09:00 — live availability: Available [S2]
```

**สถานะ:** answer → partial

**การเลือก:** exact_live_snapshot, exact_live_snapshot

```json
{
  "missing_claims": [],
  "unrequested_claims": [],
  "wrong_values": [],
  "evidence_mismatches": []
}
```

**Expected source refs และ actual claims:**

```json
{
  "expected": [
    {
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
    },
    {
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
  ],
  "actual": [
    {
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
      ],
      "fixture": true,
      "status": "unavailable"
    },
    {
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
      ],
      "fixture": true,
      "status": "answer"
    }
  ]
}
```

## same_source_hinted / C12-Q064 / C12

**คำถาม:** I would like to know: Can you check whether PC #10 / 2026-10-21 12:00 is already booked? and also Is PC #06 / 2026-10-21 09:00 available?

**คำตอบ:**

```text
PC #10 / 2026-10-21 12:00 — live availability: Stale data; occupancy is not confirmed [S1]

PC #06 / 2026-10-21 09:00 — live availability: Available [S2]
```

**สถานะ:** answer → partial

**การเลือก:** exact_live_snapshot, exact_live_snapshot

```json
{
  "missing_claims": [],
  "unrequested_claims": [],
  "wrong_values": [],
  "evidence_mismatches": []
}
```

**Expected source refs และ actual claims:**

```json
{
  "expected": [
    {
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
    },
    {
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
  ],
  "actual": [
    {
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
      ],
      "fixture": true,
      "status": "unavailable"
    },
    {
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
      ],
      "fixture": true,
      "status": "answer"
    }
  ]
}
```

## same_source_hinted / C12-Q065 / C12

**คำถาม:** Based on the studio sources, Is PlayStation 5 #01 / 2026-10-21 09:00 available? and also Can you check whether PlayStation 5 #02 / 2026-10-21 12:00 is already booked?

**คำตอบ:**

```text
PlayStation 5 #01 / 2026-10-21 09:00 — live availability: Available [S1]

PlayStation 5 #02 / 2026-10-21 12:00 — live availability: Stale data; occupancy is not confirmed [S2]
```

**สถานะ:** answer → partial

**การเลือก:** exact_live_snapshot, exact_live_snapshot

```json
{
  "missing_claims": [],
  "unrequested_claims": [],
  "wrong_values": [],
  "evidence_mismatches": []
}
```

**Expected source refs และ actual claims:**

```json
{
  "expected": [
    {
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
    },
    {
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
  ],
  "actual": [
    {
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
      ],
      "fixture": true,
      "status": "answer"
    },
    {
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
      ],
      "fixture": true,
      "status": "unavailable"
    }
  ]
}
```

## same_source_hinted / C12-Q066 / C12

**คำถาม:** Can you check whether PC #01 / 2026-10-21 11:00 is already booked? and also Is Cockpit #02 / 2026-10-21 10:00 available?

**คำตอบ:**

```text
PC #01 / 2026-10-21 11:00 — live availability: Provider unavailable; occupancy is not confirmed [S1]

Cockpit #02 / 2026-10-21 10:00 — live availability: Booked [S2]
```

**สถานะ:** answer → partial

**การเลือก:** exact_live_snapshot, exact_live_snapshot

```json
{
  "missing_claims": [],
  "unrequested_claims": [],
  "wrong_values": [],
  "evidence_mismatches": []
}
```

**Expected source refs และ actual claims:**

```json
{
  "expected": [
    {
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
    },
    {
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
  ],
  "actual": [
    {
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
      ],
      "fixture": true,
      "status": "unavailable"
    },
    {
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
      ],
      "fixture": true,
      "status": "answer"
    }
  ]
}
```

## same_source_hinted / C12-Q067 / C12

**คำถาม:** Could you help me with this: Is PC #06 / 2026-10-21 09:00 available? and also Can you check whether PlayStation 5 #01 / 2026-10-21 12:00 is already booked?

**คำตอบ:**

```text
PC #06 / 2026-10-21 09:00 — live availability: Available [S1]

PlayStation 5 #01 / 2026-10-21 12:00 — live availability: Stale data; occupancy is not confirmed [S2]
```

**สถานะ:** answer → partial

**การเลือก:** exact_live_snapshot, exact_live_snapshot

```json
{
  "missing_claims": [],
  "unrequested_claims": [],
  "wrong_values": [],
  "evidence_mismatches": []
}
```

**Expected source refs และ actual claims:**

```json
{
  "expected": [
    {
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
    },
    {
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
  ],
  "actual": [
    {
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
      ],
      "fixture": true,
      "status": "answer"
    },
    {
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
      ],
      "fixture": true,
      "status": "unavailable"
    }
  ]
}
```

## same_source_hinted / C12-Q068 / C12

**คำถาม:** Please answer briefly: Can you check whether PlayStation 5 #02 / 2026-10-21 12:00 is already booked? and also Is PC #08 / 2026-10-21 09:00 available?

**คำตอบ:**

```text
PlayStation 5 #02 / 2026-10-21 12:00 — live availability: Stale data; occupancy is not confirmed [S1]

PC #08 / 2026-10-21 09:00 — live availability: Available [S2]
```

**สถานะ:** answer → partial

**การเลือก:** exact_live_snapshot, exact_live_snapshot

```json
{
  "missing_claims": [],
  "unrequested_claims": [],
  "wrong_values": [],
  "evidence_mismatches": []
}
```

**Expected source refs และ actual claims:**

```json
{
  "expected": [
    {
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
    },
    {
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
  ],
  "actual": [
    {
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
      ],
      "fixture": true,
      "status": "unavailable"
    },
    {
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
      ],
      "fixture": true,
      "status": "answer"
    }
  ]
}
```

## same_source_hinted / C12-Q073 / C12

**คำถาม:** ช่วยตอบสั้น ๆ ว่า PC #08 / 2026-10-21 11:00 ว่างอยู่ไหม แล้วขอช่วยเช็กว่าจอง Cockpit #01 / 2026-10-21 09:00 ได้หรือยัง

**คำตอบ:**

```text
PC #08 / 2026-10-21 11:00 — สถานะว่างสด: ตรวจสถานะไม่ได้ [S1]

Cockpit #01 / 2026-10-21 09:00 — สถานะว่างสด: ว่าง [S2]
```

**สถานะ:** answer → partial

**การเลือก:** exact_live_snapshot, exact_live_snapshot

```json
{
  "missing_claims": [],
  "unrequested_claims": [],
  "wrong_values": [],
  "evidence_mismatches": []
}
```

**Expected source refs และ actual claims:**

```json
{
  "expected": [
    {
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
    },
    {
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
  ],
  "actual": [
    {
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
      ],
      "fixture": true,
      "status": "unavailable"
    },
    {
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
      ],
      "fixture": true,
      "status": "answer"
    }
  ]
}
```

## same_source_hinted / C12-Q074 / C12

**คำถาม:** อยากรู้ว่า ช่วยเช็กว่าจอง PC #09 / 2026-10-21 10:00 ได้หรือยัง แล้วขออยากรู้ว่า PC #04 / 2026-10-21 11:00 ถูกจองหรือยัง

**คำตอบ:**

```text
PC #09 / 2026-10-21 10:00 — สถานะว่างสด: ถูกจอง [S1]

PC #04 / 2026-10-21 11:00 — สถานะว่างสด: ตรวจสถานะไม่ได้ [S2]
```

**สถานะ:** answer → partial

**การเลือก:** exact_live_snapshot, exact_live_snapshot

```json
{
  "missing_claims": [],
  "unrequested_claims": [],
  "wrong_values": [],
  "evidence_mismatches": []
}
```

**Expected source refs และ actual claims:**

```json
{
  "expected": [
    {
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
    },
    {
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
  ],
  "actual": [
    {
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
      ],
      "fixture": true,
      "status": "answer"
    },
    {
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
      ],
      "fixture": true,
      "status": "unavailable"
    }
  ]
}
```

## same_source_hinted / C12-Q075 / C12

**คำถาม:** กำลังวางแผนไปใช้บริการ เลยขอถามว่า อยากรู้ว่า Cockpit #02 / 2026-10-21 09:00 ถูกจองหรือยัง แล้วขอPlayStation 5 #01 / 2026-10-21 11:00 ว่างอยู่ไหม

**คำตอบ:**

```text
Cockpit #02 / 2026-10-21 09:00 — สถานะว่างสด: ว่าง [S1]

PlayStation 5 #01 / 2026-10-21 11:00 — สถานะว่างสด: ตรวจสถานะไม่ได้ [S2]
```

**สถานะ:** answer → partial

**การเลือก:** exact_live_snapshot, exact_live_snapshot

```json
{
  "missing_claims": [],
  "unrequested_claims": [],
  "wrong_values": [],
  "evidence_mismatches": []
}
```

**Expected source refs และ actual claims:**

```json
{
  "expected": [
    {
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
    },
    {
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
  ],
  "actual": [
    {
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
      ],
      "fixture": true,
      "status": "answer"
    },
    {
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
      ],
      "fixture": true,
      "status": "unavailable"
    }
  ]
}
```

## same_source_hinted / C12-Q076 / C12

**คำถาม:** รบกวนเช็กให้หน่อย Cockpit #01 / 2026-10-21 09:00 ว่างอยู่ไหม แล้วขอช่วยเช็กว่าจอง PC #04 / 2026-10-21 12:00 ได้หรือยัง

**คำตอบ:**

```text
Cockpit #01 / 2026-10-21 09:00 — สถานะว่างสด: ว่าง [S1]

PC #04 / 2026-10-21 12:00 — สถานะว่างสด: ข้อมูลเก่า ยืนยันสถานะไม่ได้ [S2]
```

**สถานะ:** answer → partial

**การเลือก:** exact_live_snapshot, exact_live_snapshot

```json
{
  "missing_claims": [],
  "unrequested_claims": [],
  "wrong_values": [],
  "evidence_mismatches": []
}
```

**Expected source refs และ actual claims:**

```json
{
  "expected": [
    {
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
    },
    {
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
  ],
  "actual": [
    {
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
      ],
      "fixture": true,
      "status": "answer"
    },
    {
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
      ],
      "fixture": true,
      "status": "unavailable"
    }
  ]
}
```

## same_source_hinted / C12-Q078 / C12

**คำถาม:** อยากรู้ว่า PlayStation 5 #01 / 2026-10-21 11:00 ถูกจองหรือยัง แล้วขอPC #01 / 2026-10-21 09:00 ว่างอยู่ไหม

**คำตอบ:**

```text
PlayStation 5 #01 / 2026-10-21 11:00 — สถานะว่างสด: ตรวจสถานะไม่ได้ [S1]

PC #01 / 2026-10-21 09:00 — สถานะว่างสด: ว่าง [S2]
```

**สถานะ:** answer → partial

**การเลือก:** exact_live_snapshot, exact_live_snapshot

```json
{
  "missing_claims": [],
  "unrequested_claims": [],
  "wrong_values": [],
  "evidence_mismatches": []
}
```

**Expected source refs และ actual claims:**

```json
{
  "expected": [
    {
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
    },
    {
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
  ],
  "actual": [
    {
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
      ],
      "fixture": true,
      "status": "unavailable"
    },
    {
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
      ],
      "fixture": true,
      "status": "answer"
    }
  ]
}
```

## automatic_routing / C12-Q061 / C12

**คำถาม:** Is PC #09 / 2026-10-21 09:00 available? and also Can you check whether PC #10 / 2026-10-21 12:00 is already booked?

**คำตอบ:**

```text
PC #09 / 2026-10-21 09:00 — live availability: Available [S1]

PC #10 / 2026-10-21 12:00 — live availability: Stale data; occupancy is not confirmed [S2]
```

**สถานะ:** answer → partial

**การเลือก:** exact_live_snapshot, exact_live_snapshot

```json
{
  "missing_claims": [],
  "unrequested_claims": [],
  "wrong_values": [],
  "evidence_mismatches": []
}
```

**Expected source refs และ actual claims:**

```json
{
  "expected": [
    {
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
    },
    {
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
  ],
  "actual": [
    {
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
      ],
      "fixture": true,
      "status": "answer"
    },
    {
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
      ],
      "fixture": true,
      "status": "unavailable"
    }
  ]
}
```

## automatic_routing / C12-Q062 / C12

**คำถาม:** Could you help me with this: Can you check whether PlayStation 5 #02 / 2026-10-21 11:00 is already booked? and also Is PlayStation 5 #01 / 2026-10-21 09:00 available?

**คำตอบ:**

```text
PlayStation 5 #02 / 2026-10-21 11:00 — live availability: Provider unavailable; occupancy is not confirmed [S1]

PlayStation 5 #01 / 2026-10-21 09:00 — live availability: Available [S2]
```

**สถานะ:** answer → partial

**การเลือก:** exact_live_snapshot, exact_live_snapshot

```json
{
  "missing_claims": [],
  "unrequested_claims": [],
  "wrong_values": [],
  "evidence_mismatches": []
}
```

**Expected source refs และ actual claims:**

```json
{
  "expected": [
    {
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
    },
    {
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
  ],
  "actual": [
    {
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
      ],
      "fixture": true,
      "status": "unavailable"
    },
    {
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
      ],
      "fixture": true,
      "status": "answer"
    }
  ]
}
```

## automatic_routing / C12-Q064 / C12

**คำถาม:** I would like to know: Can you check whether PC #10 / 2026-10-21 12:00 is already booked? and also Is PC #06 / 2026-10-21 09:00 available?

**คำตอบ:**

```text
PC #10 / 2026-10-21 12:00 — live availability: Stale data; occupancy is not confirmed [S1]

PC #06 / 2026-10-21 09:00 — live availability: Available [S2]
```

**สถานะ:** answer → partial

**การเลือก:** exact_live_snapshot, exact_live_snapshot

```json
{
  "missing_claims": [],
  "unrequested_claims": [],
  "wrong_values": [],
  "evidence_mismatches": []
}
```

**Expected source refs และ actual claims:**

```json
{
  "expected": [
    {
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
    },
    {
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
  ],
  "actual": [
    {
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
      ],
      "fixture": true,
      "status": "unavailable"
    },
    {
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
      ],
      "fixture": true,
      "status": "answer"
    }
  ]
}
```

## automatic_routing / C12-Q065 / C12

**คำถาม:** Based on the studio sources, Is PlayStation 5 #01 / 2026-10-21 09:00 available? and also Can you check whether PlayStation 5 #02 / 2026-10-21 12:00 is already booked?

**คำตอบ:**

```text
PlayStation 5 #01 / 2026-10-21 09:00 — live availability: Available [S1]

PlayStation 5 #02 / 2026-10-21 12:00 — live availability: Stale data; occupancy is not confirmed [S2]
```

**สถานะ:** answer → partial

**การเลือก:** exact_live_snapshot, exact_live_snapshot

```json
{
  "missing_claims": [],
  "unrequested_claims": [],
  "wrong_values": [],
  "evidence_mismatches": []
}
```

**Expected source refs และ actual claims:**

```json
{
  "expected": [
    {
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
    },
    {
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
  ],
  "actual": [
    {
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
      ],
      "fixture": true,
      "status": "answer"
    },
    {
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
      ],
      "fixture": true,
      "status": "unavailable"
    }
  ]
}
```

## automatic_routing / C12-Q066 / C12

**คำถาม:** Can you check whether PC #01 / 2026-10-21 11:00 is already booked? and also Is Cockpit #02 / 2026-10-21 10:00 available?

**คำตอบ:**

```text
PC #01 / 2026-10-21 11:00 — live availability: Provider unavailable; occupancy is not confirmed [S1]

Cockpit #02 / 2026-10-21 10:00 — live availability: Booked [S2]
```

**สถานะ:** answer → partial

**การเลือก:** exact_live_snapshot, exact_live_snapshot

```json
{
  "missing_claims": [],
  "unrequested_claims": [],
  "wrong_values": [],
  "evidence_mismatches": []
}
```

**Expected source refs และ actual claims:**

```json
{
  "expected": [
    {
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
    },
    {
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
  ],
  "actual": [
    {
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
      ],
      "fixture": true,
      "status": "unavailable"
    },
    {
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
      ],
      "fixture": true,
      "status": "answer"
    }
  ]
}
```

## automatic_routing / C12-Q067 / C12

**คำถาม:** Could you help me with this: Is PC #06 / 2026-10-21 09:00 available? and also Can you check whether PlayStation 5 #01 / 2026-10-21 12:00 is already booked?

**คำตอบ:**

```text
PC #06 / 2026-10-21 09:00 — live availability: Available [S1]

PlayStation 5 #01 / 2026-10-21 12:00 — live availability: Stale data; occupancy is not confirmed [S2]
```

**สถานะ:** answer → partial

**การเลือก:** exact_live_snapshot, exact_live_snapshot

```json
{
  "missing_claims": [],
  "unrequested_claims": [],
  "wrong_values": [],
  "evidence_mismatches": []
}
```

**Expected source refs และ actual claims:**

```json
{
  "expected": [
    {
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
    },
    {
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
  ],
  "actual": [
    {
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
      ],
      "fixture": true,
      "status": "answer"
    },
    {
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
      ],
      "fixture": true,
      "status": "unavailable"
    }
  ]
}
```

## automatic_routing / C12-Q068 / C12

**คำถาม:** Please answer briefly: Can you check whether PlayStation 5 #02 / 2026-10-21 12:00 is already booked? and also Is PC #08 / 2026-10-21 09:00 available?

**คำตอบ:**

```text
PlayStation 5 #02 / 2026-10-21 12:00 — live availability: Stale data; occupancy is not confirmed [S1]

PC #08 / 2026-10-21 09:00 — live availability: Available [S2]
```

**สถานะ:** answer → partial

**การเลือก:** exact_live_snapshot, exact_live_snapshot

```json
{
  "missing_claims": [],
  "unrequested_claims": [],
  "wrong_values": [],
  "evidence_mismatches": []
}
```

**Expected source refs และ actual claims:**

```json
{
  "expected": [
    {
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
    },
    {
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
  ],
  "actual": [
    {
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
      ],
      "fixture": true,
      "status": "unavailable"
    },
    {
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
      ],
      "fixture": true,
      "status": "answer"
    }
  ]
}
```

## automatic_routing / C12-Q073 / C12

**คำถาม:** ช่วยตอบสั้น ๆ ว่า PC #08 / 2026-10-21 11:00 ว่างอยู่ไหม แล้วขอช่วยเช็กว่าจอง Cockpit #01 / 2026-10-21 09:00 ได้หรือยัง

**คำตอบ:**

```text
PC #08 / 2026-10-21 11:00 — สถานะว่างสด: ตรวจสถานะไม่ได้ [S1]

Cockpit #01 / 2026-10-21 09:00 — สถานะว่างสด: ว่าง [S2]
```

**สถานะ:** answer → partial

**การเลือก:** exact_live_snapshot, exact_live_snapshot

```json
{
  "missing_claims": [],
  "unrequested_claims": [],
  "wrong_values": [],
  "evidence_mismatches": []
}
```

**Expected source refs และ actual claims:**

```json
{
  "expected": [
    {
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
    },
    {
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
  ],
  "actual": [
    {
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
      ],
      "fixture": true,
      "status": "unavailable"
    },
    {
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
      ],
      "fixture": true,
      "status": "answer"
    }
  ]
}
```

## automatic_routing / C12-Q074 / C12

**คำถาม:** อยากรู้ว่า ช่วยเช็กว่าจอง PC #09 / 2026-10-21 10:00 ได้หรือยัง แล้วขออยากรู้ว่า PC #04 / 2026-10-21 11:00 ถูกจองหรือยัง

**คำตอบ:**

```text
PC #09 / 2026-10-21 10:00 — สถานะว่างสด: ถูกจอง [S1]

PC #04 / 2026-10-21 11:00 — สถานะว่างสด: ตรวจสถานะไม่ได้ [S2]
```

**สถานะ:** answer → partial

**การเลือก:** exact_live_snapshot, exact_live_snapshot

```json
{
  "missing_claims": [],
  "unrequested_claims": [],
  "wrong_values": [],
  "evidence_mismatches": []
}
```

**Expected source refs และ actual claims:**

```json
{
  "expected": [
    {
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
    },
    {
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
  ],
  "actual": [
    {
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
      ],
      "fixture": true,
      "status": "answer"
    },
    {
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
      ],
      "fixture": true,
      "status": "unavailable"
    }
  ]
}
```

## automatic_routing / C12-Q075 / C12

**คำถาม:** กำลังวางแผนไปใช้บริการ เลยขอถามว่า อยากรู้ว่า Cockpit #02 / 2026-10-21 09:00 ถูกจองหรือยัง แล้วขอPlayStation 5 #01 / 2026-10-21 11:00 ว่างอยู่ไหม

**คำตอบ:**

```text
Cockpit #02 / 2026-10-21 09:00 — สถานะว่างสด: ว่าง [S1]

PlayStation 5 #01 / 2026-10-21 11:00 — สถานะว่างสด: ตรวจสถานะไม่ได้ [S2]
```

**สถานะ:** answer → partial

**การเลือก:** exact_live_snapshot, exact_live_snapshot

```json
{
  "missing_claims": [],
  "unrequested_claims": [],
  "wrong_values": [],
  "evidence_mismatches": []
}
```

**Expected source refs และ actual claims:**

```json
{
  "expected": [
    {
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
    },
    {
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
  ],
  "actual": [
    {
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
      ],
      "fixture": true,
      "status": "answer"
    },
    {
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
      ],
      "fixture": true,
      "status": "unavailable"
    }
  ]
}
```

## automatic_routing / C12-Q076 / C12

**คำถาม:** รบกวนเช็กให้หน่อย Cockpit #01 / 2026-10-21 09:00 ว่างอยู่ไหม แล้วขอช่วยเช็กว่าจอง PC #04 / 2026-10-21 12:00 ได้หรือยัง

**คำตอบ:**

```text
Cockpit #01 / 2026-10-21 09:00 — สถานะว่างสด: ว่าง [S1]

PC #04 / 2026-10-21 12:00 — สถานะว่างสด: ข้อมูลเก่า ยืนยันสถานะไม่ได้ [S2]
```

**สถานะ:** answer → partial

**การเลือก:** exact_live_snapshot, exact_live_snapshot

```json
{
  "missing_claims": [],
  "unrequested_claims": [],
  "wrong_values": [],
  "evidence_mismatches": []
}
```

**Expected source refs และ actual claims:**

```json
{
  "expected": [
    {
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
    },
    {
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
  ],
  "actual": [
    {
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
      ],
      "fixture": true,
      "status": "answer"
    },
    {
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
      ],
      "fixture": true,
      "status": "unavailable"
    }
  ]
}
```

## automatic_routing / C12-Q078 / C12

**คำถาม:** อยากรู้ว่า PlayStation 5 #01 / 2026-10-21 11:00 ถูกจองหรือยัง แล้วขอPC #01 / 2026-10-21 09:00 ว่างอยู่ไหม

**คำตอบ:**

```text
PlayStation 5 #01 / 2026-10-21 11:00 — สถานะว่างสด: ตรวจสถานะไม่ได้ [S1]

PC #01 / 2026-10-21 09:00 — สถานะว่างสด: ว่าง [S2]
```

**สถานะ:** answer → partial

**การเลือก:** exact_live_snapshot, exact_live_snapshot

```json
{
  "missing_claims": [],
  "unrequested_claims": [],
  "wrong_values": [],
  "evidence_mismatches": []
}
```

**Expected source refs และ actual claims:**

```json
{
  "expected": [
    {
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
    },
    {
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
  ],
  "actual": [
    {
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
      ],
      "fixture": true,
      "status": "unavailable"
    },
    {
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
      ],
      "fixture": true,
      "status": "answer"
    }
  ]
}
```

## reserved_automatic / C13-NEW-001 / C13

**คำถาม:** กติกาของ กฎระเบียบและรูปแบบการแข่งขัน VALORANT หัวข้อ การใช้สกิลเอเจนท์ ระบุเงื่อนไขไว้อย่างไร

**คำตอบ:**

```text
กฎระเบียบและรูปแบบการแข่งขัน VALORANT — การใช้สกิลเอเจนท์: ห้ามวางกล้อง Cypher ในจุดที่มองไม่เห็นหรือทำลายไม่ได้ผ่านการทะลุ Texture ของแผนที่ [S1]
กฎระเบียบและรูปแบบการแข่งขัน VALORANT — การใช้สกิลเอเจนท์: ห้ามใช้สกิลในพื้นที่นอกขอบเขตแผนที่ (Out of boundaries) เพื่อหาข้อมูลหรือสร้างความได้เปรียบ [S2]
กฎระเบียบและรูปแบบการแข่งขัน VALORANT — การใช้สกิลเอเจนท์: ข้อยกเว้นพิเศษ สกิล ZERO/POINT ของ KAY/O สามารถใช้ภายนอกแผนที่หรือจุดที่ทำลายไม่ได้ได้ แต่ตัวมีดห้ามพุ่งทะลุ Texture ที่ควรจะเป็นของแข็ง [S3]
กฎระเบียบและรูปแบบการแข่งขัน VALORANT — การใช้สกิลเอเจนท์: การกระโดดต่อตัว ห้ามใช้ตัวละครเพื่อนร่วมทีมเพื่อกระโดดไปยังจุดที่สูงเกินกว่าระยะกระโดดปกติ [S4]
```

**สถานะ:** answer → answer

**การเลือก:** event_clause_dependency_read

```json
{
  "missing_claims": [],
  "unrequested_claims": [
    "C13:valorant_66:rule_clause",
    "C13:valorant_67:rule_clause",
    "C13:valorant_69:rule_clause"
  ],
  "wrong_values": [],
  "evidence_mismatches": []
}
```

**Expected source refs และ actual claims:**

```json
{
  "expected": [
    {
      "fact_id": "C13:valorant_68:rule_clause",
      "value": "ข้อยกเว้นพิเศษ สกิล ZERO/POINT ของ KAY/O สามารถใช้ภายนอกแผนที่หรือจุดที่ทำลายไม่ได้ได้ แต่ตัวมีดห้ามพุ่งทะลุ Texture ที่ควรจะเป็นของแข็ง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "doc108:valorant",
          "locator": "document.xml/paragraph[68]",
          "source_sha256": "a824f58e0fb4dcd1db4ea1097fd02e4d6f5d147822d88dc36a69db5518dbf8d7"
        }
      ]
    }
  ],
  "actual": [
    {
      "fact_id": "C13:valorant_66:rule_clause",
      "record_id": "valorant_66",
      "facet": "rule_clause",
      "value": "ห้ามวางกล้อง Cypher ในจุดที่มองไม่เห็นหรือทำลายไม่ได้ผ่านการทะลุ Texture ของแผนที่",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "doc108:valorant",
          "locator": "document.xml/paragraph[66]",
          "source_sha256": "a824f58e0fb4dcd1db4ea1097fd02e4d6f5d147822d88dc36a69db5518dbf8d7"
        }
      ],
      "fixture": false,
      "status": "answer"
    },
    {
      "fact_id": "C13:valorant_67:rule_clause",
      "record_id": "valorant_67",
      "facet": "rule_clause",
      "value": "ห้ามใช้สกิลในพื้นที่นอกขอบเขตแผนที่ (Out of boundaries) เพื่อหาข้อมูลหรือสร้างความได้เปรียบ",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "doc108:valorant",
          "locator": "document.xml/paragraph[67]",
          "source_sha256": "a824f58e0fb4dcd1db4ea1097fd02e4d6f5d147822d88dc36a69db5518dbf8d7"
        }
      ],
      "fixture": false,
      "status": "answer"
    },
    {
      "fact_id": "C13:valorant_68:rule_clause",
      "record_id": "valorant_68",
      "facet": "rule_clause",
      "value": "ข้อยกเว้นพิเศษ สกิล ZERO/POINT ของ KAY/O สามารถใช้ภายนอกแผนที่หรือจุดที่ทำลายไม่ได้ได้ แต่ตัวมีดห้ามพุ่งทะลุ Texture ที่ควรจะเป็นของแข็ง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "doc108:valorant",
          "locator": "document.xml/paragraph[68]",
          "source_sha256": "a824f58e0fb4dcd1db4ea1097fd02e4d6f5d147822d88dc36a69db5518dbf8d7"
        }
      ],
      "fixture": false,
      "status": "answer"
    },
    {
      "fact_id": "C13:valorant_69:rule_clause",
      "record_id": "valorant_69",
      "facet": "rule_clause",
      "value": "การกระโดดต่อตัว ห้ามใช้ตัวละครเพื่อนร่วมทีมเพื่อกระโดดไปยังจุดที่สูงเกินกว่าระยะกระโดดปกติ",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "doc108:valorant",
          "locator": "document.xml/paragraph[69]",
          "source_sha256": "a824f58e0fb4dcd1db4ea1097fd02e4d6f5d147822d88dc36a69db5518dbf8d7"
        }
      ],
      "fixture": false,
      "status": "answer"
    }
  ]
}
```

## reserved_automatic / C13-NEW-002 / C13

**คำถาม:** กติกาของ กฎระเบียบและรูปแบบการแข่งขัน Counter-Strike 2 หัวข้อ พฤติกรรมและบทลงโทษ ระบุเงื่อนไขไว้อย่างไร

**คำตอบ:**

```text
กฎระเบียบและรูปแบบการแข่งขัน Counter-Strike 2 — พฤติกรรมและบทลงโทษ: มารยาทผู้เล่น ห้ามพฤติกรรมก้าวร้าว วาจาสร้างความเกลียดชัง (เหยียดเชื้อชาติ/ศาสนา) และการกระทำที่ไม่มีน้ำใจนักกีฬา [S1]
กฎระเบียบและรูปแบบการแข่งขัน Counter-Strike 2 — พฤติกรรมและบทลงโทษ: การใช้บัค ห้ามใช้บัคของแผนที่หรือ Engine เกมเด็ดขาด หากฝ่าฝืนจะถูกปรับแพ้ในรอบ/แผนที่นั้น หรือตัดสิทธิ์ [S2]
กฎระเบียบและรูปแบบการแข่งขัน Counter-Strike 2 — พฤติกรรมและบทลงโทษ: การดูสตรีม ห้ามผู้เล่นดูสตรีมสดระหว่างแข่ง [S3]
```

**สถานะ:** answer → answer

**การเลือก:** event_clause_dependency_read

```json
{
  "missing_claims": [],
  "unrequested_claims": [
    "C13:cs2_36:rule_clause",
    "C13:cs2_38:rule_clause"
  ],
  "wrong_values": [],
  "evidence_mismatches": []
}
```

**Expected source refs และ actual claims:**

```json
{
  "expected": [
    {
      "fact_id": "C13:cs2_37:rule_clause",
      "value": "การใช้บัค ห้ามใช้บัคของแผนที่หรือ Engine เกมเด็ดขาด หากฝ่าฝืนจะถูกปรับแพ้ในรอบ/แผนที่นั้น หรือตัดสิทธิ์",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "doc108:cs2",
          "locator": "document.xml/paragraph[37]",
          "source_sha256": "ab8633990e0cb279313261b34ef6b66cfd658858981c954cda8bfe67190bcbdc"
        }
      ]
    }
  ],
  "actual": [
    {
      "fact_id": "C13:cs2_36:rule_clause",
      "record_id": "cs2_36",
      "facet": "rule_clause",
      "value": "มารยาทผู้เล่น ห้ามพฤติกรรมก้าวร้าว วาจาสร้างความเกลียดชัง (เหยียดเชื้อชาติ/ศาสนา) และการกระทำที่ไม่มีน้ำใจนักกีฬา",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "doc108:cs2",
          "locator": "document.xml/paragraph[36]",
          "source_sha256": "ab8633990e0cb279313261b34ef6b66cfd658858981c954cda8bfe67190bcbdc"
        }
      ],
      "fixture": false,
      "status": "answer"
    },
    {
      "fact_id": "C13:cs2_37:rule_clause",
      "record_id": "cs2_37",
      "facet": "rule_clause",
      "value": "การใช้บัค ห้ามใช้บัคของแผนที่หรือ Engine เกมเด็ดขาด หากฝ่าฝืนจะถูกปรับแพ้ในรอบ/แผนที่นั้น หรือตัดสิทธิ์",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "doc108:cs2",
          "locator": "document.xml/paragraph[37]",
          "source_sha256": "ab8633990e0cb279313261b34ef6b66cfd658858981c954cda8bfe67190bcbdc"
        }
      ],
      "fixture": false,
      "status": "answer"
    },
    {
      "fact_id": "C13:cs2_38:rule_clause",
      "record_id": "cs2_38",
      "facet": "rule_clause",
      "value": "การดูสตรีม ห้ามผู้เล่นดูสตรีมสดระหว่างแข่ง",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "doc108:cs2",
          "locator": "document.xml/paragraph[38]",
          "source_sha256": "ab8633990e0cb279313261b34ef6b66cfd658858981c954cda8bfe67190bcbdc"
        }
      ],
      "fixture": false,
      "status": "answer"
    }
  ]
}
```

## reserved_automatic / C13-NEW-003 / C13

**คำถาม:** กติกาของ กฎระเบียบและรูปแบบการแข่งขัน VALORANT หัวข้อ กฎเกี่ยวกับบั๊ก ระบุเงื่อนไขไว้อย่างไร

**คำตอบ:**

```text
กฎระเบียบและรูปแบบการแข่งขัน VALORANT — กฎเกี่ยวกับบั๊ก: บั๊กคือข้อผิดพลาดในเกมที่ทำให้เกิดผลลัพธ์ที่ไม่ตั้งใจ โดยแบ่งประเภทเพื่อกำหนดแนวทางปฏิบัติ ดังนี้ [S1]
กฎระเบียบและรูปแบบการแข่งขัน VALORANT — กฎเกี่ยวกับบั๊ก: Play Through Bug บั๊กที่ไม่ส่งผลกระทบต่อความยุติธรรมอย่างมีนัยสำคัญ ผู้เล่นต้องเล่นต่อไปและไม่สามารถขอ Challenge ได้ [S2]
กฎระเบียบและรูปแบบการแข่งขัน VALORANT — กฎเกี่ยวกับบั๊ก: Major Bug บั๊กที่ส่งผลกระทบต่อการเล่นหรือกลไกเกมอย่างมากและไม่มีทางแก้ไขเฉพาะหน้า ทีมสามารถขอ Challenge เพื่อตรวจสอบได้ [S3]
กฎระเบียบและรูปแบบการแข่งขัน VALORANT — กฎเกี่ยวกับบั๊ก: Game Breaking Bug บั๊กที่ทำลายความยุติธรรมของรอบนั้นจนไม่สามารถตัดสินผลแพ้ชนะได้ [S4]
```

**สถานะ:** answer → answer

**การเลือก:** event_clause_dependency_read

```json
{
  "missing_claims": [],
  "unrequested_claims": [
    "C13:valorant_56:rule_clause",
    "C13:valorant_57:rule_clause",
    "C13:valorant_58:rule_clause"
  ],
  "wrong_values": [],
  "evidence_mismatches": []
}
```

**Expected source refs และ actual claims:**

```json
{
  "expected": [
    {
      "fact_id": "C13:valorant_55:rule_clause",
      "value": "บั๊กคือข้อผิดพลาดในเกมที่ทำให้เกิดผลลัพธ์ที่ไม่ตั้งใจ โดยแบ่งประเภทเพื่อกำหนดแนวทางปฏิบัติ ดังนี้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "doc108:valorant",
          "locator": "document.xml/paragraph[55]",
          "source_sha256": "a824f58e0fb4dcd1db4ea1097fd02e4d6f5d147822d88dc36a69db5518dbf8d7"
        }
      ]
    }
  ],
  "actual": [
    {
      "fact_id": "C13:valorant_55:rule_clause",
      "record_id": "valorant_55",
      "facet": "rule_clause",
      "value": "บั๊กคือข้อผิดพลาดในเกมที่ทำให้เกิดผลลัพธ์ที่ไม่ตั้งใจ โดยแบ่งประเภทเพื่อกำหนดแนวทางปฏิบัติ ดังนี้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "doc108:valorant",
          "locator": "document.xml/paragraph[55]",
          "source_sha256": "a824f58e0fb4dcd1db4ea1097fd02e4d6f5d147822d88dc36a69db5518dbf8d7"
        }
      ],
      "fixture": false,
      "status": "answer"
    },
    {
      "fact_id": "C13:valorant_56:rule_clause",
      "record_id": "valorant_56",
      "facet": "rule_clause",
      "value": "Play Through Bug บั๊กที่ไม่ส่งผลกระทบต่อความยุติธรรมอย่างมีนัยสำคัญ ผู้เล่นต้องเล่นต่อไปและไม่สามารถขอ Challenge ได้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "doc108:valorant",
          "locator": "document.xml/paragraph[56]",
          "source_sha256": "a824f58e0fb4dcd1db4ea1097fd02e4d6f5d147822d88dc36a69db5518dbf8d7"
        }
      ],
      "fixture": false,
      "status": "answer"
    },
    {
      "fact_id": "C13:valorant_57:rule_clause",
      "record_id": "valorant_57",
      "facet": "rule_clause",
      "value": "Major Bug บั๊กที่ส่งผลกระทบต่อการเล่นหรือกลไกเกมอย่างมากและไม่มีทางแก้ไขเฉพาะหน้า ทีมสามารถขอ Challenge เพื่อตรวจสอบได้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "doc108:valorant",
          "locator": "document.xml/paragraph[57]",
          "source_sha256": "a824f58e0fb4dcd1db4ea1097fd02e4d6f5d147822d88dc36a69db5518dbf8d7"
        }
      ],
      "fixture": false,
      "status": "answer"
    },
    {
      "fact_id": "C13:valorant_58:rule_clause",
      "record_id": "valorant_58",
      "facet": "rule_clause",
      "value": "Game Breaking Bug บั๊กที่ทำลายความยุติธรรมของรอบนั้นจนไม่สามารถตัดสินผลแพ้ชนะได้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "doc108:valorant",
          "locator": "document.xml/paragraph[58]",
          "source_sha256": "a824f58e0fb4dcd1db4ea1097fd02e4d6f5d147822d88dc36a69db5518dbf8d7"
        }
      ],
      "fixture": false,
      "status": "answer"
    }
  ]
}
```

## reserved_automatic / C13-NEW-004 / C13

**คำถาม:** กติกาของ กฎระเบียบและรูปแบบการแข่งขัน Tekken 8 รายการ PSU Esports ปะทะมันส์ สนั่นจอ หัวข้อ การหยุดเกม ระบุเงื่อนไขไว้อย่างไร

**คำตอบ:**

```text
กฎระเบียบและรูปแบบการแข่งขัน Tekken 8 รายการ PSU Esports ปะทะมันส์ สนั่นจอ — การหยุดเกม: ห้ามออกจากเกมก่อนจบการแข่งขัน ยกเว้นได้รับอนุญาตจากกรรมการ [S1]
กฎระเบียบและรูปแบบการแข่งขัน Tekken 8 รายการ PSU Esports ปะทะมันส์ สนั่นจอ — การหยุดเกม: หากออกจากเกมโดยไม่ได้รับอนุญาต จะถูกปรับแพ้ทันที [S2]
กฎระเบียบและรูปแบบการแข่งขัน Tekken 8 รายการ PSU Esports ปะทะมันส์ สนั่นจอ — การหยุดเกม: การกดหยุดเกม (Pause) ทำได้เมื่อผู้เล่นทุกคนยินยอม และมีเหตุผลที่เหมาะสม เช่น อุปกรณ์ขัดข้องหรือเหตุฉุกเฉิน [S3]
```

**สถานะ:** answer → answer

**การเลือก:** event_clause_dependency_read

```json
{
  "missing_claims": [],
  "unrequested_claims": [
    "C13:tekken_32:rule_clause",
    "C13:tekken_34:rule_clause"
  ],
  "wrong_values": [],
  "evidence_mismatches": []
}
```

**Expected source refs และ actual claims:**

```json
{
  "expected": [
    {
      "fact_id": "C13:tekken_33:rule_clause",
      "value": "หากออกจากเกมโดยไม่ได้รับอนุญาต จะถูกปรับแพ้ทันที",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "doc108:tekken",
          "locator": "document.xml/paragraph[33]",
          "source_sha256": "a62ff9f815911e306606d3d934433940eda5215d28385bc8b47ea086052824f9"
        }
      ]
    }
  ],
  "actual": [
    {
      "fact_id": "C13:tekken_32:rule_clause",
      "record_id": "tekken_32",
      "facet": "rule_clause",
      "value": "ห้ามออกจากเกมก่อนจบการแข่งขัน ยกเว้นได้รับอนุญาตจากกรรมการ",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "doc108:tekken",
          "locator": "document.xml/paragraph[32]",
          "source_sha256": "a62ff9f815911e306606d3d934433940eda5215d28385bc8b47ea086052824f9"
        }
      ],
      "fixture": false,
      "status": "answer"
    },
    {
      "fact_id": "C13:tekken_33:rule_clause",
      "record_id": "tekken_33",
      "facet": "rule_clause",
      "value": "หากออกจากเกมโดยไม่ได้รับอนุญาต จะถูกปรับแพ้ทันที",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "doc108:tekken",
          "locator": "document.xml/paragraph[33]",
          "source_sha256": "a62ff9f815911e306606d3d934433940eda5215d28385bc8b47ea086052824f9"
        }
      ],
      "fixture": false,
      "status": "answer"
    },
    {
      "fact_id": "C13:tekken_34:rule_clause",
      "record_id": "tekken_34",
      "facet": "rule_clause",
      "value": "การกดหยุดเกม (Pause) ทำได้เมื่อผู้เล่นทุกคนยินยอม และมีเหตุผลที่เหมาะสม เช่น อุปกรณ์ขัดข้องหรือเหตุฉุกเฉิน",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "doc108:tekken",
          "locator": "document.xml/paragraph[34]",
          "source_sha256": "a62ff9f815911e306606d3d934433940eda5215d28385bc8b47ea086052824f9"
        }
      ],
      "fixture": false,
      "status": "answer"
    }
  ]
}
```

## reserved_automatic / C13-NEW-005 / C13

**คำถาม:** กติกาของ กฎระเบียบและรูปแบบการแข่งขัน Counter-Strike 2 หัวข้อ ห้ามใช้สคริปต์ หรือมาโคร โดยเด็ดขาด ระบุเงื่อนไขไว้อย่างไร

**คำตอบ:**

```text
กฎระเบียบและรูปแบบการแข่งขัน Counter-Strike 2 — ห้ามใช้สคริปต์ หรือมาโคร โดยเด็ดขาด: ห้ามติดตั้งโปรแกรมเองบนคอมพิวเตอร์ที่จัดไว้ให้ [S1]
กฎระเบียบและรูปแบบการแข่งขัน Counter-Strike 2 — ห้ามใช้สคริปต์ หรือมาโคร โดยเด็ดขาด: ห้ามเข้าโซเชียลมีเดียหรือเว็บไซต์สื่อสารใด ๆ บนคอมพิวเตอร์แข่งขันนอกจากโปรแกรมที่ทางผู้จัดจัดเตรียมไว้ให้ [S2]
```

**สถานะ:** answer → answer

**การเลือก:** event_clause_dependency_read

```json
{
  "missing_claims": [],
  "unrequested_claims": [
    "C13:cs2_47:rule_clause"
  ],
  "wrong_values": [],
  "evidence_mismatches": []
}
```

**Expected source refs และ actual claims:**

```json
{
  "expected": [
    {
      "fact_id": "C13:cs2_48:rule_clause",
      "value": "ห้ามเข้าโซเชียลมีเดียหรือเว็บไซต์สื่อสารใด ๆ บนคอมพิวเตอร์แข่งขันนอกจากโปรแกรมที่ทางผู้จัดจัดเตรียมไว้ให้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "doc108:cs2",
          "locator": "document.xml/paragraph[48]",
          "source_sha256": "ab8633990e0cb279313261b34ef6b66cfd658858981c954cda8bfe67190bcbdc"
        }
      ]
    }
  ],
  "actual": [
    {
      "fact_id": "C13:cs2_47:rule_clause",
      "record_id": "cs2_47",
      "facet": "rule_clause",
      "value": "ห้ามติดตั้งโปรแกรมเองบนคอมพิวเตอร์ที่จัดไว้ให้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "doc108:cs2",
          "locator": "document.xml/paragraph[47]",
          "source_sha256": "ab8633990e0cb279313261b34ef6b66cfd658858981c954cda8bfe67190bcbdc"
        }
      ],
      "fixture": false,
      "status": "answer"
    },
    {
      "fact_id": "C13:cs2_48:rule_clause",
      "record_id": "cs2_48",
      "facet": "rule_clause",
      "value": "ห้ามเข้าโซเชียลมีเดียหรือเว็บไซต์สื่อสารใด ๆ บนคอมพิวเตอร์แข่งขันนอกจากโปรแกรมที่ทางผู้จัดจัดเตรียมไว้ให้",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "doc108:cs2",
          "locator": "document.xml/paragraph[48]",
          "source_sha256": "ab8633990e0cb279313261b34ef6b66cfd658858981c954cda8bfe67190bcbdc"
        }
      ],
      "fixture": false,
      "status": "answer"
    }
  ]
}
```

## reserved_automatic / C13-NEW-006 / C13

**คำถาม:** กติกาของ กฎระเบียบและรูปแบบการแข่งขัน VALORANT หัวข้อ กระบวนการหลังจบแมตช์ ระบุเงื่อนไขไว้อย่างไร

**คำตอบ:**

```text
กฎระเบียบและรูปแบบการแข่งขัน VALORANT — กระบวนการหลังจบแมตช์: การบันทึกผล เจ้าหน้าที่จะยืนยัน และบันทึกผลการแข่งทันที [S1]
กฎระเบียบและรูปแบบการแข่งขัน VALORANT — กระบวนการหลังจบแมตช์: การปรับแพ้ (Forfeiture) หากมีการปรับแพ้ ผลการแข่งในแผนที่นั้นจะถูกบันทึกเป็น 13-0 [S2]
```

**สถานะ:** answer → answer

**การเลือก:** event_clause_dependency_read

```json
{
  "missing_claims": [],
  "unrequested_claims": [
    "C13:valorant_41:rule_clause"
  ],
  "wrong_values": [],
  "evidence_mismatches": []
}
```

**Expected source refs และ actual claims:**

```json
{
  "expected": [
    {
      "fact_id": "C13:valorant_42:rule_clause",
      "value": "การปรับแพ้ (Forfeiture) หากมีการปรับแพ้ ผลการแข่งในแผนที่นั้นจะถูกบันทึกเป็น 13-0",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "doc108:valorant",
          "locator": "document.xml/paragraph[42]",
          "source_sha256": "a824f58e0fb4dcd1db4ea1097fd02e4d6f5d147822d88dc36a69db5518dbf8d7"
        }
      ]
    }
  ],
  "actual": [
    {
      "fact_id": "C13:valorant_41:rule_clause",
      "record_id": "valorant_41",
      "facet": "rule_clause",
      "value": "การบันทึกผล เจ้าหน้าที่จะยืนยัน และบันทึกผลการแข่งทันที",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "doc108:valorant",
          "locator": "document.xml/paragraph[41]",
          "source_sha256": "a824f58e0fb4dcd1db4ea1097fd02e4d6f5d147822d88dc36a69db5518dbf8d7"
        }
      ],
      "fixture": false,
      "status": "answer"
    },
    {
      "fact_id": "C13:valorant_42:rule_clause",
      "record_id": "valorant_42",
      "facet": "rule_clause",
      "value": "การปรับแพ้ (Forfeiture) หากมีการปรับแพ้ ผลการแข่งในแผนที่นั้นจะถูกบันทึกเป็น 13-0",
      "numeric": null,
      "evidence_refs": [
        {
          "source_id": "doc108:valorant",
          "locator": "document.xml/paragraph[42]",
          "source_sha256": "a824f58e0fb4dcd1db4ea1097fd02e4d6f5d147822d88dc36a69db5518dbf8d7"
        }
      ],
      "fixture": false,
      "status": "answer"
    }
  ]
}
```

