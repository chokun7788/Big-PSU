# ผลทดสอบ10%หลังวินิจฉัยข้อ2 — R131

วินิจฉัยก่อนทดสอบเสร็จแล้ว ตามDIAGNOSIS_PRETEST_COMPLETE.json รันคำถามเดิม2111keys/5584grade identities ครบทุกตัว ไม่มีขาดหรือซ้ำ source/input/code/prompt/weights/modelprovenanceไม่เปลี่ยน

รอบนี้ใช้candidateR130เดิม ไม่มีการแก้Flowหรือฝึกโมเดลใหม่ จึงวัดการเกิดซ้ำและผลของเส้นทางทำงาน/คิว ไม่ใช่ผลปรับปรุงคุณภาพหลังfix ไม่ใช้คะแนนต่างจากsavedrunมาอ้างว่าระบบดีขึ้นเอง

## คะแนนภาษา — strictและpositive literalแยกจากsemantic

| แขน | ภาษา | Strict | Literal ผ่าน/eligible | Literal% | Unassessed |
|---|---|---:|---:|---:|---:|
| R64_saved | auto | 236/364 (64.84%) | 200/247 | 80.97 | 13 |
| R64_saved | en | 2252/2728 (82.55%) | 951/994 | 95.67 | 0 |
| R64_saved | th | 1809/2492 (72.59%) | 1274/1315 | 96.88 | 3 |
| R95_saved | auto | 51/364 (14.01%) | 177/247 | 71.66 | 0 |
| R95_saved | en | 287/2728 (10.52%) | 696/994 | 70.02 | 0 |
| R95_saved | th | 225/2492 (9.03%) | 998/1315 | 75.89 | 0 |
| R130_saved | auto | 47/364 (12.91%) | 165/247 | 66.80 | 0 |
| R130_saved | en | 92/2728 (3.37%) | 752/994 | 75.65 | 0 |
| R130_saved | th | 24/2492 (0.96%) | 1041/1315 | 79.16 | 0 |
| R130_repeat_10pct | auto | 46/364 (12.64%) | 165/247 | 66.80 | 0 |
| R130_repeat_10pct | en | 95/2728 (3.48%) | 752/994 | 75.65 | 0 |
| R130_repeat_10pct | th | 23/2492 (0.92%) | 1041/1315 | 79.16 | 0 |

## ทุกหมวดตามinput — คำถามหลายหมวดซ้อนทับได้

| หมวด | จำนวนคำถาม | Strict% | Literal ผ่าน/eligible | Literal% |
|---|---:|---:|---:|---:|
| C00 ทั่วไป/กำกวม/นอกขอบเขต | 111 | 39.31 | 32/59 | 54.24 |
| C01 ศูนย์/ติดต่อ | 135 | 13.25 | 145/155 | 93.55 |
| C02 บุคลากร | 81 | 8.00 | 145/153 | 94.77 |
| C03 อุปกรณ์ | 172 | 3.34 | 175/316 | 55.38 |
| C04 เกม | 475 | 0.93 | 632/724 | 87.29 |
| C05 การควบคุม | 223 | 0.59 | 498/548 | 90.88 |
| C06 ราคาปกติ | 197 | 0.95 | 196/278 | 70.50 |
| C07 เหมา | 1 | 0.00 | 0/1 | 0.00 |
| C08 จอง | 414 | 0.77 | 293/422 | 69.43 |
| C09 ชำระเงิน | 10 | 0.00 | 24/24 | 100.00 |
| C10 กฎศูนย์ | 166 | 3.34 | 126/167 | 75.45 |
| C11 ตาราง | 246 | 0.00 | 91/177 | 51.41 |
| C12 สถานะจริง | 113 | 0.00 | 20/38 | 52.63 |
| C13 แข่งขัน | 452 | 1.29 | 3/90 | 3.33 |
| C14 ข่าว/กิจกรรม | 11 | 5.88 | 0/14 | 0.00 |

C07มีประชากรในFullเดิม6คำถาม เลือก1ตามceil10% และส่วนใหญ่เป็นoffsite ยังสรุปราคาเหมาonsiteทุกoperationไม่ได้ C14ข้อมูลnewsจริงไม่มี sourcegapต้องแยกจากruntimefailure ไม่เอาจำนวนsampleน้อยไปอ้างหมวดผ่าน100%

คำตอบเหมือนsavedR130เดิม2111keys เปลี่ยน0keys ดูREPEAT_ANSWER_CHANGES.json ทุกความต่างยังต้องตรวจความหมาย ไม่ถือchanged=ดีขึ้น

## Model/latency/กลไกที่เกิดซ้ำ

{
  "gateway": {
    "attempts": 54,
    "transport_successes": 30,
    "verified_retained": 24,
    "verified_base": 6
  },
  "http": {
    "attempts": 54,
    "header_transport_ok": 30
  },
  "latency": {
    "median_sec": 0.6390162000025157,
    "p95_sec": 3.613543399987975,
    "p99_sec": 46.36018590000458,
    "max_sec": 150.7230503000028,
    "above_20_sec": 37
  },
  "mechanisms": {
    "model_admission_denied": 926,
    "controlled_live_artifact": 112,
    "gateway_transport_failure": 22,
    "schema_or_version_rejection": 25,
    "requested_field_not_delivered": 11,
    "substantive_clause_not_delivered": 3
  }
}

ใช้contextretained R121adapterบนengine/dataR130 ส่วนselector/genericใช้base Modelpsu-r129:latestคือTyphoon2.5Qwen3-4B HFNF4BF16 ไม่มีการpromoteadapterใหม่ controlledliveunavailableไม่ใช่providerจริงไม่พร้อม

การเทียบsavedR64/R95มีsource/backend/precision/clock/deadlineconfoundsและไม่ใช่causalFloweffect ไม่มีbaselineinference/regradingใหม่ sourcecaseที่ยังไม่ตัดสินคงreview_required Candidateไม่ติดตั้งทับR78

## หลักฐาน

- ITEM02_DETAILED_DIAGNOSIS_TH.md / INDIVIDUAL_SOURCE_REVIEW.json
- CASE_DIAGNOSTICS_REVIEWED.jsonl.gz / ROOT_CAUSE_REGISTER.json
- SOURCE_CAUSAL_EVIDENCE.json / DETERMINISTIC_CAUSAL_PROBES.json
- SELECTION_FREEZE.json / SAMPLE_ALLOCATION.json / RUN_FREEZE.json
- sample01/RESULTS_*.jsonl.gz / COVERAGE.json / SCORES.json
- EXECUTION_COMPLETE.json / MODEL_AND_MECHANISM_AUDIT.json / KNOWN_CASE_REPRODUCTION.json
