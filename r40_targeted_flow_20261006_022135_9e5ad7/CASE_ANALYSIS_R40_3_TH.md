# วิเคราะห์ก่อน/หลังรายเคส r40.3

เปรียบเทียบ 31 เคสเดิมด้วย oracle ชุดสุดท้ายเดียวกัน; raw เดิมไม่ถูกแก้ไข

## clarify-th-0 — missing_controls

- คำถาม: `ขอดูปุ่มควบคุมเกม`
- ก่อน: ผ่าน / `pipeline:game_control_missing_game_context`
- หลัง: ผ่าน / `pipeline:game_control_missing_game_context`
- เงื่อนไขตรวจหลัง: http_success=True, asks_game=True, no_catalog=True
- Trace ก่อนที่บันทึกจริง (คะแนนเป็นคะแนนของขั้นนั้น ไม่ใช่ความน่าจะเป็นว่าตอบถูก):

```json
[
  {
    "stage": "universal_intent",
    "decision": "game_controls/control",
    "confidence": 0.9,
    "detail": "candidate_intent:c1 heuristic fallback",
    "metadata": {
      "method": "llm",
      "llm_attempted": true,
      "llm_first": true,
      "llm_first_skip_reason": "",
      "llm_first_review_reason": "",
      "llm_call": {
        "llm_kind": "universal_intent",
        "llm_model": "scb10x/typhoon2.5-qwen3-4b",
        "llm_timeout_sec": 14.0,
        "llm_configured_timeout_sec": 14.0,
        "llm_num_predict": 18,
        "llm_num_ctx": 1536,
        "llm_cache_hit": true,
        "global_timeout_enabled": true,
        "global_timeout_sec": 18.3498,
        "global_elapsed_sec": 0.1039,
        "global_remaining_sec": 18.246,
        "finalizer_reserve_sec": 1.0,
        "work_remaining_sec": 17.246,
        "timing_status": "running",
        "llm_elapsed_ms": 0.0,
        "llm_response_chars": 0,
        "llm_parsed": true
      },
      "intent_risk_flags": [
        "competing_domain_signals"
      ],
      "input_recovery": {
        "score": 0.2369,
        "language": "th",
        "language_quality": 0.7631,
        "should_review_intent": false,
        "reason": "Thai character n-gram quality=0.763",
        "action": "continue"
      },
      "llm_rejected_reason": "",
      "intent_candidates": [
        {
          "id": "c1",
          "domain": "game_controls",
          "operation": "control",
          "target": "",
          "confidence": 0.9,
          "reason": "heuristic fallback"
        },
        {
          "id": "c2",
          "domain": "games",
          "operation": "unknown",
          "target": "",
          "confidence": 0.95,
          "reason": "router category candidate"
        },
        {
          "id": "c3",
          "domain": "games",
          "operation": "list",
          "target": "",
          "confidence": 0.66,
          "reason": "game-domain catalog alternative"
        },
        {
          "id": "c4",
          "domain": "equipment",
          "operation": "how_to",
          "target": "",
          "confidence": 0.72,
          "reason": "controller equipment phrase"
        }
      ],
      "target": "",
      "filters": {},
      "needs": [],
      "answer_style": "direct_then_details",
      "heuristic": {
        "domain": "game_controls",
        "operation": "control",
        "confidence": 0.9,
        "reason": "domain_terms=3; control operation overrides domain; control terms found"
      }
    }
  }
]
```

**คำตอบก่อน**

ขอชื่อเกมก่อนครับ ยังไม่แน่ใจว่าหมายถึงเกมไหน จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน
ตัวอย่างเกมที่มีข้อมูลปุ่มแล้ว: TEKKEN 8, Mario Kart 8 Deluxe, Call of Duty: Modern Warfare III
เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง` หรือ `Mario Kart 8 Deluxe กดอะไร`

**คำตอบหลัง**

ต้องการดูปุ่มควบคุมของเกมใดครับ? พิมพ์ชื่อเกมที่ต้องการได้เลยครับ

## clarify-th-1 — missing_controls

- คำถาม: `ขอดูปุ่มทั้งหมด`
- ก่อน: ผ่าน / `pipeline:game_control_missing_game_context`
- หลัง: ผ่าน / `pipeline:game_control_missing_game_context`
- เงื่อนไขตรวจหลัง: http_success=True, asks_game=True, no_catalog=True
- Trace ก่อนที่บันทึกจริง (คะแนนเป็นคะแนนของขั้นนั้น ไม่ใช่ความน่าจะเป็นว่าตอบถูก):

```json
[
  {
    "stage": "universal_intent",
    "decision": "game_controls/list",
    "confidence": 0.9,
    "detail": "candidate_intent:c4 operation keyword score=1",
    "metadata": {
      "method": "llm",
      "llm_attempted": true,
      "llm_first": true,
      "llm_first_skip_reason": "",
      "llm_first_review_reason": "",
      "llm_call": {
        "llm_kind": "universal_intent",
        "llm_model": "scb10x/typhoon2.5-qwen3-4b",
        "llm_timeout_sec": 14.0,
        "llm_configured_timeout_sec": 14.0,
        "llm_num_predict": 18,
        "llm_num_ctx": 1536,
        "llm_cache_hit": false,
        "global_timeout_enabled": true,
        "global_timeout_sec": 18.3499,
        "global_elapsed_sec": 0.0942,
        "global_remaining_sec": 18.2558,
        "finalizer_reserve_sec": 1.0,
        "work_remaining_sec": 17.2558,
        "timing_status": "running",
        "llm_health_enabled": true,
        "llm_health_allowed": true,
        "llm_health_status": "ok",
        "llm_health_kind": "universal_intent",
        "llm_health_model": "scb10x/typhoon2.5-qwen3-4b",
        "llm_health_failures": 0,
        "llm_health_cooldown_remaining_sec": 0.0,
        "llm_health_last_error_type": "",
        "llm_health_last_error": "",
        "llm_health_failure_scope": "kind_only",
        "llm_budget_enabled": true,
        "llm_budget_allowed": true,
        "llm_budget_max_calls": 2,
        "llm_budget_used_calls": 1,
        "llm_budget_kind": "universal_intent",
        "llm_concurrency_allowed": true,
        "llm_concurrency_limit": 1,
        "llm_concurrency_wait_sec": 0.2,
        "llm_prompt_chars": 782,
        "llm_candidate_count": 5,
        "llm_compact_candidates_chars": 353,
        "llm_elapsed_ms": 10012.78,
        "llm_response_chars": 39,
        "llm_done_reason": "stop",
        "llm_parsed": true
      },
      "intent_risk_flags": [],
      "input_recovery": {
        "score": 0.2513,
        "language": "th",
        "language_quality": 0.7487,
        "should_review_intent": false,
        "reason": "Thai character n-gram quality=0.749",
        "action": "continue"
      },
      "llm_rejected_reason": "",
      "intent_candidates": [
        {
          "id": "c1",
          "domain": "game_controls",
          "operation": "control",
          "target": "",
          "confidence": 0.9,
          "reason": "heuristic fallback"
        },
        {
          "id": "c2",
          "domain": "general",
          "operation": "unknown",
          "target": "",
          "confidence": 0.55,
          "reason": "router category candidate"
        },
        {
          "id": "c3",
          "domain": "knowledge",
          "operation": "detail",
          "target": "chatbot_greeting",
          "confidence": 0.6,
          "reason": "possible chatbot greeting; tolerate informal spelling"
        },
        {
          "id": "c4",
          "domain": "game_controls",
          "operation": "list",
          "target": "",
          "confidence": 0.66,
          "reason": "operation keyword score=1"
        },
        {
          "id": "c5",
          "domain": "equipment",
          "operation": "how_to",
          "target": "",
          "confidence": 0.72,
          "reason": "controller equipment phrase"
        }
      ],
      "target": "",
      "filters": {},
      "needs": [],
      "answer_style": "summary_bullets",
      "heuristic": {
        "domain": "game_controls",
        "operation": "control",
        "confidence": 0.9,
        "reason": "domain_terms=2; control operation overrides domain; control terms found"
      }
    }
  }
]
```

**คำตอบก่อน**

ขอชื่อเกมก่อนครับ ยังไม่แน่ใจว่าหมายถึงเกมไหน จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน
ตัวอย่างเกมที่มีข้อมูลปุ่มแล้ว: TEKKEN 8, Mario Kart 8 Deluxe, Call of Duty: Modern Warfare III
เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง` หรือ `Mario Kart 8 Deluxe กดอะไร`

**คำตอบหลัง**

ต้องการดูปุ่มควบคุมของเกมใดครับ? พิมพ์ชื่อเกมที่ต้องการได้เลยครับ

## clarify-th-2 — missing_controls

- คำถาม: `ช่วยบอกปุ่มเกมหน่อยครับ`
- ก่อน: ผ่าน / `pipeline:game_control_missing_game_context`
- หลัง: ผ่าน / `pipeline:game_control_missing_game_context`
- เงื่อนไขตรวจหลัง: http_success=True, asks_game=True, no_catalog=True
- Trace ก่อนที่บันทึกจริง (คะแนนเป็นคะแนนของขั้นนั้น ไม่ใช่ความน่าจะเป็นว่าตอบถูก):

```json
[
  {
    "stage": "universal_intent",
    "decision": "game_controls/control",
    "confidence": 0.9,
    "detail": "candidate_intent:c1 heuristic fallback",
    "metadata": {
      "method": "llm",
      "llm_attempted": true,
      "llm_first": true,
      "llm_first_skip_reason": "",
      "llm_first_review_reason": "",
      "llm_call": {
        "llm_kind": "universal_intent",
        "llm_model": "scb10x/typhoon2.5-qwen3-4b",
        "llm_timeout_sec": 14.0,
        "llm_configured_timeout_sec": 14.0,
        "llm_num_predict": 18,
        "llm_num_ctx": 1536,
        "llm_cache_hit": false,
        "global_timeout_enabled": true,
        "global_timeout_sec": 18.35,
        "global_elapsed_sec": 0.0896,
        "global_remaining_sec": 18.2604,
        "finalizer_reserve_sec": 1.0,
        "work_remaining_sec": 17.2603,
        "timing_status": "running",
        "llm_health_enabled": true,
        "llm_health_allowed": true,
        "llm_health_status": "ok",
        "llm_health_kind": "universal_intent",
        "llm_health_model": "scb10x/typhoon2.5-qwen3-4b",
        "llm_health_failures": 0,
        "llm_health_cooldown_remaining_sec": 0.0,
        "llm_health_last_error_type": "",
        "llm_health_last_error": "",
        "llm_health_failure_scope": "kind_only",
        "llm_budget_enabled": true,
        "llm_budget_allowed": true,
        "llm_budget_max_calls": 2,
        "llm_budget_used_calls": 1,
        "llm_budget_kind": "universal_intent",
        "llm_concurrency_allowed": true,
        "llm_concurrency_limit": 1,
        "llm_concurrency_wait_sec": 0.2,
        "llm_prompt_chars": 695,
        "llm_candidate_count": 4,
        "llm_compact_candidates_chars": 261,
        "llm_elapsed_ms": 333.12,
        "llm_response_chars": 39,
        "llm_done_reason": "stop",
        "llm_parsed": true
      },
      "intent_risk_flags": [
        "competing_domain_signals"
      ],
      "input_recovery": {
        "score": 0.2708,
        "language": "th",
        "language_quality": 0.7292,
        "should_review_intent": false,
        "reason": "Thai character n-gram quality=0.729",
        "action": "continue"
      },
      "llm_rejected_reason": "",
      "intent_candidates": [
        {
          "id": "c1",
          "domain": "game_controls",
          "operation": "control",
          "target": "",
          "confidence": 0.9,
          "reason": "heuristic fallback"
        },
        {
          "id": "c2",
          "domain": "games",
          "operation": "unknown",
          "target": "",
          "confidence": 0.95,
          "reason": "router category candidate"
        },
        {
          "id": "c3",
          "domain": "games",
          "operation": "list",
          "target": "",
          "confidence": 0.66,
          "reason": "game-domain catalog alternative"
        },
        {
          "id": "c4",
          "domain": "equipment",
          "operation": "how_to",
          "target": "",
          "confidence": 0.72,
          "reason": "controller equipment phrase"
        }
      ],
      "target": "",
      "filters": {},
      "needs": [],
      "answer_style": "direct_then_details",
      "heuristic": {
        "domain": "game_controls",
        "operation": "control",
        "confidence": 0.9,
        "reason": "domain_terms=3; control operation overrides domain; control terms found"
      }
    }
  }
]
```

**คำตอบก่อน**

ขอชื่อเกมก่อนครับ ยังไม่แน่ใจว่าหมายถึงเกมไหน จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน
ตัวอย่างเกมที่มีข้อมูลปุ่มแล้ว: TEKKEN 8, Mario Kart 8 Deluxe, Call of Duty: Modern Warfare III
เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง` หรือ `Mario Kart 8 Deluxe กดอะไร`

**คำตอบหลัง**

ต้องการดูปุ่มควบคุมของเกมใดครับ? พิมพ์ชื่อเกมที่ต้องการได้เลยครับ

## clarify-th-3 — missing_controls

- คำถาม: `เกมมีปุ่มอะไรบ้าง`
- ก่อน: ผ่าน / `pipeline:game_control_missing_game_context`
- หลัง: ผ่าน / `pipeline:game_control_missing_game_context`
- เงื่อนไขตรวจหลัง: http_success=True, asks_game=True, no_catalog=True
- Trace ก่อนที่บันทึกจริง (คะแนนเป็นคะแนนของขั้นนั้น ไม่ใช่ความน่าจะเป็นว่าตอบถูก):

```json
[
  {
    "stage": "universal_intent",
    "decision": "game_controls/control",
    "confidence": 0.9,
    "detail": "candidate_intent:c1 heuristic fallback",
    "metadata": {
      "method": "llm",
      "llm_attempted": true,
      "llm_first": true,
      "llm_first_skip_reason": "",
      "llm_first_review_reason": "",
      "llm_call": {
        "llm_kind": "universal_intent",
        "llm_model": "scb10x/typhoon2.5-qwen3-4b",
        "llm_timeout_sec": 14.0,
        "llm_configured_timeout_sec": 14.0,
        "llm_num_predict": 18,
        "llm_num_ctx": 1536,
        "llm_cache_hit": false,
        "global_timeout_enabled": true,
        "global_timeout_sec": 18.35,
        "global_elapsed_sec": 0.0884,
        "global_remaining_sec": 18.2616,
        "finalizer_reserve_sec": 1.0,
        "work_remaining_sec": 17.2616,
        "timing_status": "running",
        "llm_health_enabled": true,
        "llm_health_allowed": true,
        "llm_health_status": "ok",
        "llm_health_kind": "universal_intent",
        "llm_health_model": "scb10x/typhoon2.5-qwen3-4b",
        "llm_health_failures": 0,
        "llm_health_cooldown_remaining_sec": 0.0,
        "llm_health_last_error_type": "",
        "llm_health_last_error": "",
        "llm_health_failure_scope": "kind_only",
        "llm_budget_enabled": true,
        "llm_budget_allowed": true,
        "llm_budget_max_calls": 2,
        "llm_budget_used_calls": 1,
        "llm_budget_kind": "universal_intent",
        "llm_concurrency_allowed": true,
        "llm_concurrency_limit": 1,
        "llm_concurrency_wait_sec": 0.2,
        "llm_prompt_chars": 689,
        "llm_candidate_count": 4,
        "llm_compact_candidates_chars": 261,
        "llm_elapsed_ms": 322.49,
        "llm_response_chars": 39,
        "llm_done_reason": "stop",
        "llm_parsed": true
      },
      "intent_risk_flags": [
        "competing_domain_signals"
      ],
      "input_recovery": {
        "score": 0.2057,
        "language": "th",
        "language_quality": 0.7943,
        "should_review_intent": false,
        "reason": "Thai character n-gram quality=0.794",
        "action": "continue"
      },
      "llm_rejected_reason": "",
      "intent_candidates": [
        {
          "id": "c1",
          "domain": "game_controls",
          "operation": "control",
          "target": "",
          "confidence": 0.9,
          "reason": "heuristic fallback"
        },
        {
          "id": "c2",
          "domain": "games",
          "operation": "unknown",
          "target": "",
          "confidence": 0.95,
          "reason": "router category candidate"
        },
        {
          "id": "c3",
          "domain": "games",
          "operation": "list",
          "target": "",
          "confidence": 0.66,
          "reason": "game-domain catalog alternative"
        },
        {
          "id": "c4",
          "domain": "equipment",
          "operation": "how_to",
          "target": "",
          "confidence": 0.72,
          "reason": "controller equipment phrase"
        }
      ],
      "target": "",
      "filters": {},
      "needs": [],
      "answer_style": "direct_then_details",
      "heuristic": {
        "domain": "game_controls",
        "operation": "control",
        "confidence": 0.9,
        "reason": "domain_terms=3; control operation overrides domain; control terms found"
      }
    }
  }
]
```

**คำตอบก่อน**

ขอชื่อเกมก่อนครับ ยังไม่แน่ใจว่าหมายถึงเกมไหน จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน
ตัวอย่างเกมที่มีข้อมูลปุ่มแล้ว: TEKKEN 8, Mario Kart 8 Deluxe, Call of Duty: Modern Warfare III
เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง` หรือ `Mario Kart 8 Deluxe กดอะไร`

**คำตอบหลัง**

ต้องการดูปุ่มควบคุมของเกมใดครับ? พิมพ์ชื่อเกมที่ต้องการได้เลยครับ

## clarify-th-4 — missing_controls

- คำถาม: `ปุ่มควบคุมต้องกดยังไง`
- ก่อน: ผ่าน / `pipeline:game_control_missing_game_context`
- หลัง: ผ่าน / `pipeline:game_control_missing_game_context`
- เงื่อนไขตรวจหลัง: http_success=True, asks_game=True, no_catalog=True
- Trace ก่อนที่บันทึกจริง (คะแนนเป็นคะแนนของขั้นนั้น ไม่ใช่ความน่าจะเป็นว่าตอบถูก):

```json
[
  {
    "stage": "universal_intent",
    "decision": "game_controls/control",
    "confidence": 0.9,
    "detail": "candidate_intent:c1 heuristic fallback",
    "metadata": {
      "method": "llm",
      "llm_attempted": true,
      "llm_first": true,
      "llm_first_skip_reason": "",
      "llm_first_review_reason": "",
      "llm_call": {
        "llm_kind": "universal_intent",
        "llm_model": "scb10x/typhoon2.5-qwen3-4b",
        "llm_timeout_sec": 14.0,
        "llm_configured_timeout_sec": 14.0,
        "llm_num_predict": 18,
        "llm_num_ctx": 1536,
        "llm_cache_hit": false,
        "global_timeout_enabled": true,
        "global_timeout_sec": 18.35,
        "global_elapsed_sec": 0.0895,
        "global_remaining_sec": 18.2605,
        "finalizer_reserve_sec": 1.0,
        "work_remaining_sec": 17.2605,
        "timing_status": "running",
        "llm_health_enabled": true,
        "llm_health_allowed": true,
        "llm_health_status": "ok",
        "llm_health_kind": "universal_intent",
        "llm_health_model": "scb10x/typhoon2.5-qwen3-4b",
        "llm_health_failures": 0,
        "llm_health_cooldown_remaining_sec": 0.0,
        "llm_health_last_error_type": "",
        "llm_health_last_error": "",
        "llm_health_failure_scope": "kind_only",
        "llm_budget_enabled": true,
        "llm_budget_allowed": true,
        "llm_budget_max_calls": 2,
        "llm_budget_used_calls": 1,
        "llm_budget_kind": "universal_intent",
        "llm_concurrency_allowed": true,
        "llm_concurrency_limit": 1,
        "llm_concurrency_wait_sec": 0.2,
        "llm_prompt_chars": 790,
        "llm_candidate_count": 5,
        "llm_compact_candidates_chars": 355,
        "llm_elapsed_ms": 328.14,
        "llm_response_chars": 39,
        "llm_done_reason": "stop",
        "llm_parsed": true
      },
      "intent_risk_flags": [],
      "input_recovery": {
        "score": 0.1723,
        "language": "th",
        "language_quality": 0.8277,
        "should_review_intent": false,
        "reason": "Thai character n-gram quality=0.828",
        "action": "continue"
      },
      "llm_rejected_reason": "",
      "intent_candidates": [
        {
          "id": "c1",
          "domain": "game_controls",
          "operation": "control",
          "target": "",
          "confidence": 0.9,
          "reason": "heuristic fallback"
        },
        {
          "id": "c2",
          "domain": "general",
          "operation": "unknown",
          "target": "",
          "confidence": 0.55,
          "reason": "router category candidate"
        },
        {
          "id": "c3",
          "domain": "knowledge",
          "operation": "detail",
          "target": "chatbot_greeting",
          "confidence": 0.6,
          "reason": "possible chatbot greeting; tolerate informal spelling"
        },
        {
          "id": "c4",
          "domain": "game_controls",
          "operation": "how_to",
          "target": "",
          "confidence": 0.66,
          "reason": "operation keyword score=1"
        },
        {
          "id": "c5",
          "domain": "equipment",
          "operation": "how_to",
          "target": "",
          "confidence": 0.72,
          "reason": "controller equipment phrase"
        }
      ],
      "target": "",
      "filters": {},
      "needs": [],
      "answer_style": "direct_then_details",
      "heuristic": {
        "domain": "game_controls",
        "operation": "control",
        "confidence": 0.9,
        "reason": "domain_terms=2; control operation overrides domain; control terms found"
      }
    }
  }
]
```

**คำตอบก่อน**

ขอชื่อเกมก่อนครับ ยังไม่แน่ใจว่าหมายถึงเกมไหน จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน
ตัวอย่างเกมที่มีข้อมูลปุ่มแล้ว: TEKKEN 8, Mario Kart 8 Deluxe, Call of Duty: Modern Warfare III
เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง` หรือ `Mario Kart 8 Deluxe กดอะไร`

**คำตอบหลัง**

ต้องการดูปุ่มควบคุมของเกมใดครับ? พิมพ์ชื่อเกมที่ต้องการได้เลยครับ

## clarify-th-5 — missing_controls

- คำถาม: `อยากรู้วิธีบังคับเกม`
- ก่อน: ผ่าน / `pipeline:game_control_missing_game_context`
- หลัง: ผ่าน / `pipeline:game_control_missing_game_context`
- เงื่อนไขตรวจหลัง: http_success=True, asks_game=True, no_catalog=True
- Trace ก่อนที่บันทึกจริง (คะแนนเป็นคะแนนของขั้นนั้น ไม่ใช่ความน่าจะเป็นว่าตอบถูก):

```json
[
  {
    "stage": "universal_intent",
    "decision": "general/how_to",
    "confidence": 0.9,
    "detail": "candidate_intent:c1 heuristic fallback",
    "metadata": {
      "method": "llm",
      "llm_attempted": true,
      "llm_first": true,
      "llm_first_skip_reason": "",
      "llm_first_review_reason": "",
      "llm_call": {
        "llm_kind": "universal_intent",
        "llm_model": "scb10x/typhoon2.5-qwen3-4b",
        "llm_timeout_sec": 14.0,
        "llm_configured_timeout_sec": 14.0,
        "llm_num_predict": 18,
        "llm_num_ctx": 1536,
        "llm_cache_hit": false,
        "global_timeout_enabled": true,
        "global_timeout_sec": 18.35,
        "global_elapsed_sec": 0.0852,
        "global_remaining_sec": 18.2648,
        "finalizer_reserve_sec": 1.0,
        "work_remaining_sec": 17.2648,
        "timing_status": "running",
        "llm_health_enabled": true,
        "llm_health_allowed": true,
        "llm_health_status": "ok",
        "llm_health_kind": "universal_intent",
        "llm_health_model": "scb10x/typhoon2.5-qwen3-4b",
        "llm_health_failures": 0,
        "llm_health_cooldown_remaining_sec": 0.0,
        "llm_health_last_error_type": "",
        "llm_health_last_error": "",
        "llm_health_failure_scope": "kind_only",
        "llm_budget_enabled": true,
        "llm_budget_allowed": true,
        "llm_budget_max_calls": 2,
        "llm_budget_used_calls": 1,
        "llm_budget_kind": "universal_intent",
        "llm_concurrency_allowed": true,
        "llm_concurrency_limit": 1,
        "llm_concurrency_wait_sec": 0.2,
        "llm_prompt_chars": 617,
        "llm_candidate_count": 3,
        "llm_compact_candidates_chars": 187,
        "llm_elapsed_ms": 334.9,
        "llm_response_chars": 39,
        "llm_done_reason": "stop",
        "llm_parsed": true
      },
      "intent_risk_flags": [
        "low_candidate_margin"
      ],
      "input_recovery": {
        "score": 0.2974,
        "language": "th",
        "language_quality": 0.7026,
        "should_review_intent": false,
        "reason": "Thai character n-gram quality=0.703",
        "action": "continue"
      },
      "llm_rejected_reason": "",
      "intent_candidates": [
        {
          "id": "c1",
          "domain": "general",
          "operation": "how_to",
          "target": "",
          "confidence": 0.74,
          "reason": "heuristic fallback"
        },
        {
          "id": "c2",
          "domain": "games",
          "operation": "list",
          "target": "",
          "confidence": 0.66,
          "reason": "game-domain catalog alternative"
        },
        {
          "id": "c3",
          "domain": "games",
          "operation": "how_to",
          "target": "",
          "confidence": 0.66,
          "reason": "domain keyword score=1"
        }
      ],
      "target": "",
      "filters": {},
      "needs": [],
      "answer_style": "direct_then_details",
      "heuristic": {
        "domain": "general",
        "operation": "how_to",
        "confidence": 0.74,
        "reason": "domain_terms=2; how-to terms found"
      }
    }
  }
]
```

**คำตอบก่อน**

ขอชื่อเกมก่อนครับ ยังไม่แน่ใจว่าหมายถึงเกมไหน จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน
ตัวอย่างเกมที่มีข้อมูลปุ่มแล้ว: TEKKEN 8, Mario Kart 8 Deluxe, Call of Duty: Modern Warfare III
เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง` หรือ `Mario Kart 8 Deluxe กดอะไร`

**คำตอบหลัง**

ต้องการดูปุ่มควบคุมของเกมใดครับ? พิมพ์ชื่อเกมที่ต้องการได้เลยครับ

## clarify-en-0 — missing_controls

- คำถาม: `Show me the game controls`
- ก่อน: ผ่าน / `pipeline:game_control_missing_game_context_en`
- หลัง: ผ่าน / `pipeline:game_control_missing_game_context_en`
- เงื่อนไขตรวจหลัง: http_success=True, asks_game=True, no_catalog=True
- Trace ก่อนที่บันทึกจริง (คะแนนเป็นคะแนนของขั้นนั้น ไม่ใช่ความน่าจะเป็นว่าตอบถูก):

```json
[
  {
    "stage": "universal_intent",
    "decision": "game_controls/control",
    "confidence": 0.9,
    "detail": "candidate_intent:c1 heuristic fallback",
    "metadata": {
      "method": "llm",
      "llm_attempted": true,
      "llm_first": true,
      "llm_first_skip_reason": "",
      "llm_first_review_reason": "forced bounded intent review for broad English structured response",
      "llm_call": {
        "llm_kind": "universal_intent",
        "llm_model": "scb10x/typhoon2.5-qwen3-4b",
        "llm_timeout_sec": 14.0,
        "llm_configured_timeout_sec": 14.0,
        "llm_num_predict": 18,
        "llm_num_ctx": 1536,
        "llm_cache_hit": true,
        "global_timeout_enabled": true,
        "global_timeout_sec": 18.35,
        "global_elapsed_sec": 0.2861,
        "global_remaining_sec": 18.0638,
        "finalizer_reserve_sec": 1.0,
        "work_remaining_sec": 17.0638,
        "timing_status": "running",
        "llm_elapsed_ms": 0.0,
        "llm_response_chars": 0,
        "llm_parsed": true
      },
      "intent_risk_flags": [
        "competing_domain_signals"
      ],
      "input_recovery": {
        "score": 0.2583,
        "language": "en",
        "language_quality": 0.7417,
        "should_review_intent": false,
        "reason": "English character n-gram quality=0.742",
        "action": "continue"
      },
      "llm_rejected_reason": "",
      "intent_candidates": [
        {
          "id": "c1",
          "domain": "game_controls",
          "operation": "control",
          "target": "",
          "confidence": 0.9,
          "reason": "heuristic fallback"
        },
        {
          "id": "c2",
          "domain": "games",
          "operation": "unknown",
          "target": "",
          "confidence": 0.97,
          "reason": "router category candidate"
        },
        {
          "id": "c3",
          "domain": "games",
          "operation": "list",
          "target": "",
          "confidence": 0.66,
          "reason": "game-domain catalog alternative"
        }
      ],
      "target": "",
      "filters": {},
      "needs": [],
      "answer_style": "direct_then_details",
      "heuristic": {
        "domain": "game_controls",
        "operation": "control",
        "confidence": 0.9,
        "reason": "domain_terms=3; control operation overrides domain; control terms found"
      }
    }
  }
]
```

**คำตอบก่อน**

Which game do you want controls for? Please provide the game title.

**คำตอบหลัง**

Which game do you want controls for? Please provide the game title.

## clarify-en-1 — missing_controls

- คำถาม: `Can I see the game controls?`
- ก่อน: ผ่าน / `pipeline:game_control_missing_game_context_en`
- หลัง: ผ่าน / `pipeline:game_control_missing_game_context_en`
- เงื่อนไขตรวจหลัง: http_success=True, asks_game=True, no_catalog=True
- Trace ก่อนที่บันทึกจริง (คะแนนเป็นคะแนนของขั้นนั้น ไม่ใช่ความน่าจะเป็นว่าตอบถูก):

```json
[
  {
    "stage": "universal_intent",
    "decision": "game_controls/control",
    "confidence": 0.9,
    "detail": "candidate_intent:c1 heuristic fallback",
    "metadata": {
      "method": "llm",
      "llm_attempted": true,
      "llm_first": true,
      "llm_first_skip_reason": "",
      "llm_first_review_reason": "forced bounded intent review for broad English structured response",
      "llm_call": {
        "llm_kind": "universal_intent",
        "llm_model": "scb10x/typhoon2.5-qwen3-4b",
        "llm_timeout_sec": 14.0,
        "llm_configured_timeout_sec": 14.0,
        "llm_num_predict": 18,
        "llm_num_ctx": 1536,
        "llm_cache_hit": true,
        "global_timeout_enabled": true,
        "global_timeout_sec": 18.35,
        "global_elapsed_sec": 0.1096,
        "global_remaining_sec": 18.2404,
        "finalizer_reserve_sec": 1.0,
        "work_remaining_sec": 17.2404,
        "timing_status": "running",
        "llm_elapsed_ms": 0.0,
        "llm_response_chars": 0,
        "llm_parsed": true
      },
      "intent_risk_flags": [
        "competing_domain_signals"
      ],
      "input_recovery": {
        "score": 0.246,
        "language": "en",
        "language_quality": 0.754,
        "should_review_intent": false,
        "reason": "English character n-gram quality=0.754",
        "action": "continue"
      },
      "llm_rejected_reason": "",
      "intent_candidates": [
        {
          "id": "c1",
          "domain": "game_controls",
          "operation": "control",
          "target": "",
          "confidence": 0.9,
          "reason": "heuristic fallback"
        },
        {
          "id": "c2",
          "domain": "games",
          "operation": "unknown",
          "target": "",
          "confidence": 0.97,
          "reason": "router category candidate"
        },
        {
          "id": "c3",
          "domain": "games",
          "operation": "list",
          "target": "",
          "confidence": 0.66,
          "reason": "game-domain catalog alternative"
        }
      ],
      "target": "",
      "filters": {},
      "needs": [],
      "answer_style": "direct_then_details",
      "heuristic": {
        "domain": "game_controls",
        "operation": "control",
        "confidence": 0.9,
        "reason": "domain_terms=3; control operation overrides domain; control terms found"
      }
    }
  }
]
```

**คำตอบก่อน**

Which game do you want controls for? Please provide the game title.

**คำตอบหลัง**

Which game do you want controls for? Please provide the game title.

## clarify-en-2 — missing_controls

- คำถาม: `What buttons can I use?`
- ก่อน: ผ่าน / `pipeline:game_control_missing_game_context_en`
- หลัง: ผ่าน / `pipeline:game_control_missing_game_context_en`
- เงื่อนไขตรวจหลัง: http_success=True, asks_game=True, no_catalog=True
- Trace ก่อนที่บันทึกจริง (คะแนนเป็นคะแนนของขั้นนั้น ไม่ใช่ความน่าจะเป็นว่าตอบถูก):

```json
[
  {
    "stage": "universal_intent",
    "decision": "game_controls/control",
    "confidence": 0.9,
    "detail": "candidate_intent:c2 controller/button phrase",
    "metadata": {
      "method": "llm",
      "llm_attempted": true,
      "llm_first": true,
      "llm_first_skip_reason": "",
      "llm_first_review_reason": "forced bounded intent review for broad English structured response",
      "llm_call": {
        "llm_kind": "universal_intent",
        "llm_model": "scb10x/typhoon2.5-qwen3-4b",
        "llm_timeout_sec": 14.0,
        "llm_configured_timeout_sec": 14.0,
        "llm_num_predict": 18,
        "llm_num_ctx": 1536,
        "llm_cache_hit": true,
        "global_timeout_enabled": true,
        "global_timeout_sec": 18.35,
        "global_elapsed_sec": 0.1191,
        "global_remaining_sec": 18.2309,
        "finalizer_reserve_sec": 1.0,
        "work_remaining_sec": 17.2309,
        "timing_status": "running",
        "llm_elapsed_ms": 0.0,
        "llm_response_chars": 0,
        "llm_parsed": true
      },
      "intent_risk_flags": [],
      "input_recovery": {
        "score": 0.3108,
        "language": "en",
        "language_quality": 0.6892,
        "should_review_intent": false,
        "reason": "English character n-gram quality=0.689",
        "action": "continue"
      },
      "llm_rejected_reason": "",
      "intent_candidates": [
        {
          "id": "c1",
          "domain": "games",
          "operation": "unknown",
          "target": "",
          "confidence": 0.45,
          "reason": "heuristic fallback"
        },
        {
          "id": "c2",
          "domain": "game_controls",
          "operation": "control",
          "target": "",
          "confidence": 0.88,
          "reason": "controller/button phrase"
        },
        {
          "id": "c3",
          "domain": "equipment",
          "operation": "how_to",
          "target": "",
          "confidence": 0.72,
          "reason": "controller equipment phrase"
        }
      ],
      "target": "",
      "filters": {},
      "needs": [],
      "answer_style": "direct_then_details",
      "heuristic": {
        "domain": "games",
        "operation": "unknown",
        "confidence": 0.45,
        "reason": "domain_terms=2; no clear operation terms"
      }
    }
  }
]
```

**คำตอบก่อน**

Which game do you want controls for? Please provide the game title.

**คำตอบหลัง**

Which game do you want controls for? Please provide the game title.

## clarify-en-3 — missing_controls

- คำถาม: `Tell me the keyboard controls please`
- ก่อน: ผิด contract / `pipeline:structured_equipment_catalog_en`
- หลัง: ผ่าน / `pipeline:game_control_missing_game_context_en`
- เงื่อนไขตรวจหลัง: http_success=True, asks_game=True, no_catalog=True
- Trace ก่อนที่บันทึกจริง (คะแนนเป็นคะแนนของขั้นนั้น ไม่ใช่ความน่าจะเป็นว่าตอบถูก):

```json
[]
```

**คำตอบก่อน**

Verified equipment:
- Gaming PC model MSI MAG Infinite S3 14th (PC Zone) - 10 Units
- Gaming Monitor (PC Zone) - 10 Units
- Gaming Keyboard (PC Zone)
- Gaming Mouse (PC Zone)
- Gaming Headset (PC Zone)
- Gaming Chair (PC Zone) - 10 Units
- Logitech G923 TRUEFORCE Racing Wheel (Cockpit Zone) - 2 Units with Driving Force Shifter
- Driving Force Shifter (Cockpit Zone) - 2 Units with Logitech G923
- Racezone Full Cockpit V3 (Cockpit Zone) - 2 Units
- Pulse Elite Wireless Headset (Cockpit Zone) - 2 Units
- Nintendo Switch OLED (Nintendo Switch Zone) - 1 Unit
- PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive (PlayStation 5 Zone / VR Zone) - 2 Units in PlayStation 5 Zone and 1 Unit in VR Zone
- Sony PlayStation VR2 (VR Zone) - 1 Unit
- TV 65 inch (Cockpit Zone) - 2 Units
- TV 86 inch (Nintendo Switch Zone) - 1 Unit
- Sofa 2 seats (Nintendo Switch Zone) - 2 Sets
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

**คำตอบหลัง**

Which game do you want controls for? Please provide the game title.

## clarify-en-4 — missing_controls

- คำถาม: `How do I control the game?`
- ก่อน: ผ่าน / `pipeline:game_control_missing_game_context_en`
- หลัง: ผ่าน / `pipeline:game_control_missing_game_context_en`
- เงื่อนไขตรวจหลัง: http_success=True, asks_game=True, no_catalog=True
- Trace ก่อนที่บันทึกจริง (คะแนนเป็นคะแนนของขั้นนั้น ไม่ใช่ความน่าจะเป็นว่าตอบถูก):

```json
[
  {
    "stage": "universal_intent",
    "decision": "game_controls/control",
    "confidence": 0.9,
    "detail": "candidate_intent:c1 heuristic fallback",
    "metadata": {
      "method": "llm",
      "llm_attempted": true,
      "llm_first": true,
      "llm_first_skip_reason": "",
      "llm_first_review_reason": "forced bounded intent review for broad English structured response",
      "llm_call": {
        "llm_kind": "universal_intent",
        "llm_model": "scb10x/typhoon2.5-qwen3-4b",
        "llm_timeout_sec": 14.0,
        "llm_configured_timeout_sec": 14.0,
        "llm_num_predict": 18,
        "llm_num_ctx": 1536,
        "llm_cache_hit": true,
        "global_timeout_enabled": true,
        "global_timeout_sec": 18.35,
        "global_elapsed_sec": 0.1912,
        "global_remaining_sec": 18.1588,
        "finalizer_reserve_sec": 1.0,
        "work_remaining_sec": 17.1588,
        "timing_status": "running",
        "llm_elapsed_ms": 0.0,
        "llm_response_chars": 0,
        "llm_parsed": true
      },
      "intent_risk_flags": [
        "competing_domain_signals"
      ],
      "input_recovery": {
        "score": 0.3151,
        "language": "en",
        "language_quality": 0.6849,
        "should_review_intent": false,
        "reason": "English character n-gram quality=0.685",
        "action": "continue"
      },
      "llm_rejected_reason": "",
      "intent_candidates": [
        {
          "id": "c1",
          "domain": "game_controls",
          "operation": "control",
          "target": "",
          "confidence": 0.9,
          "reason": "heuristic fallback"
        },
        {
          "id": "c2",
          "domain": "general",
          "operation": "unknown",
          "target": "",
          "confidence": 0.55,
          "reason": "router category candidate"
        },
        {
          "id": "c3",
          "domain": "games",
          "operation": "list",
          "target": "",
          "confidence": 0.66,
          "reason": "game-domain catalog alternative"
        },
        {
          "id": "c4",
          "domain": "games",
          "operation": "unknown",
          "target": "",
          "confidence": 0.66,
          "reason": "domain keyword score=1"
        },
        {
          "id": "c5",
          "domain": "game_controls",
          "operation": "how_to",
          "target": "",
          "confidence": 0.66,
          "reason": "operation keyword score=1"
        }
      ],
      "target": "",
      "filters": {},
      "needs": [],
      "answer_style": "direct_then_details",
      "heuristic": {
        "domain": "game_controls",
        "operation": "control",
        "confidence": 0.9,
        "reason": "domain_terms=2; control operation overrides domain; control terms found"
      }
    }
  }
]
```

**คำตอบก่อน**

Which game do you want controls for? Please provide the game title.

**คำตอบหลัง**

Which game do you want controls for? Please provide the game title.

## clarify-en-5 — missing_controls

- คำถาม: `List all game buttons`
- ก่อน: ผิด contract / `pipeline:game_controls_target_unconfirmed_en`
- หลัง: ผ่าน / `pipeline:game_control_missing_game_context_en`
- เงื่อนไขตรวจหลัง: http_success=True, asks_game=True, no_catalog=True
- Trace ก่อนที่บันทึกจริง (คะแนนเป็นคะแนนของขั้นนั้น ไม่ใช่ความน่าจะเป็นว่าตอบถูก):

```json
[
  {
    "stage": "universal_intent",
    "decision": "games/list",
    "confidence": 0.9,
    "detail": "candidate_intent:c1 heuristic fallback",
    "metadata": {
      "method": "llm",
      "llm_attempted": true,
      "llm_first": true,
      "llm_first_skip_reason": "",
      "llm_first_review_reason": "forced bounded intent review for broad English structured response",
      "llm_call": {
        "llm_kind": "universal_intent",
        "llm_model": "scb10x/typhoon2.5-qwen3-4b",
        "llm_timeout_sec": 14.0,
        "llm_configured_timeout_sec": 14.0,
        "llm_num_predict": 18,
        "llm_num_ctx": 1536,
        "llm_cache_hit": false,
        "global_timeout_enabled": true,
        "global_timeout_sec": 18.35,
        "global_elapsed_sec": 2.6958,
        "global_remaining_sec": 15.6541,
        "finalizer_reserve_sec": 1.0,
        "work_remaining_sec": 14.6541,
        "timing_status": "running",
        "llm_health_enabled": true,
        "llm_health_allowed": true,
        "llm_health_status": "ok",
        "llm_health_kind": "universal_intent",
        "llm_health_model": "scb10x/typhoon2.5-qwen3-4b",
        "llm_health_failures": 0,
        "llm_health_cooldown_remaining_sec": 0.0,
        "llm_health_last_error_type": "",
        "llm_health_last_error": "",
        "llm_health_failure_scope": "kind_only",
        "llm_budget_enabled": true,
        "llm_budget_allowed": true,
        "llm_budget_max_calls": 2,
        "llm_budget_used_calls": 1,
        "llm_budget_kind": "universal_intent",
        "llm_concurrency_allowed": true,
        "llm_concurrency_limit": 1,
        "llm_concurrency_wait_sec": 0.2,
        "llm_prompt_chars": 682,
        "llm_candidate_count": 4,
        "llm_compact_candidates_chars": 261,
        "llm_elapsed_ms": 372.82,
        "llm_response_chars": 39,
        "llm_done_reason": "stop",
        "llm_parsed": true
      },
      "intent_risk_flags": [
        "low_candidate_margin"
      ],
      "input_recovery": {
        "score": 0.2433,
        "language": "en",
        "language_quality": 0.7567,
        "should_review_intent": false,
        "reason": "English character n-gram quality=0.757",
        "action": "continue"
      },
      "llm_rejected_reason": "",
      "intent_candidates": [
        {
          "id": "c1",
          "domain": "games",
          "operation": "list",
          "target": "",
          "confidence": 0.82,
          "reason": "heuristic fallback"
        },
        {
          "id": "c2",
          "domain": "games",
          "operation": "unknown",
          "target": "",
          "confidence": 0.97,
          "reason": "router category candidate"
        },
        {
          "id": "c3",
          "domain": "game_controls",
          "operation": "control",
          "target": "",
          "confidence": 0.88,
          "reason": "controller/button phrase"
        },
        {
          "id": "c4",
          "domain": "equipment",
          "operation": "how_to",
          "target": "",
          "confidence": 0.72,
          "reason": "controller equipment phrase"
        }
      ],
      "target": "",
      "filters": {},
      "needs": [],
      "answer_style": "summary_bullets",
      "heuristic": {
        "domain": "games",
        "operation": "list",
        "confidence": 0.82,
        "reason": "domain_terms=3; list terms found"
      }
    }
  }
]
```

**คำตอบก่อน**

I could not identify a verified game title with matching control information for this request. Please confirm the spelling and exact game edition.
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

**คำตอบหลัง**

Which game do you want controls for? Please provide the game title.

## clarify-en-6 — missing_controls

- คำถาม: `I need the controls`
- ก่อน: ผ่าน / `pipeline:game_control_missing_game_context_en`
- หลัง: ผ่าน / `pipeline:game_control_missing_game_context_en`
- เงื่อนไขตรวจหลัง: http_success=True, asks_game=True, no_catalog=True
- Trace ก่อนที่บันทึกจริง (คะแนนเป็นคะแนนของขั้นนั้น ไม่ใช่ความน่าจะเป็นว่าตอบถูก):

```json
[
  {
    "stage": "universal_intent",
    "decision": "game_controls/control",
    "confidence": 0.9,
    "detail": "candidate_intent:c1 heuristic fallback",
    "metadata": {
      "method": "llm",
      "llm_attempted": true,
      "llm_first": true,
      "llm_first_skip_reason": "",
      "llm_first_review_reason": "forced bounded intent review for broad English structured response",
      "llm_call": {
        "llm_kind": "universal_intent",
        "llm_model": "scb10x/typhoon2.5-qwen3-4b",
        "llm_timeout_sec": 14.0,
        "llm_configured_timeout_sec": 14.0,
        "llm_num_predict": 18,
        "llm_num_ctx": 1536,
        "llm_cache_hit": false,
        "global_timeout_enabled": true,
        "global_timeout_sec": 18.35,
        "global_elapsed_sec": 2.6269,
        "global_remaining_sec": 15.723,
        "finalizer_reserve_sec": 1.0,
        "work_remaining_sec": 14.723,
        "timing_status": "running",
        "llm_health_enabled": true,
        "llm_health_allowed": true,
        "llm_health_status": "ok",
        "llm_health_kind": "universal_intent",
        "llm_health_model": "scb10x/typhoon2.5-qwen3-4b",
        "llm_health_failures": 0,
        "llm_health_cooldown_remaining_sec": 0.0,
        "llm_health_last_error_type": "",
        "llm_health_last_error": "",
        "llm_health_failure_scope": "kind_only",
        "llm_budget_enabled": true,
        "llm_budget_allowed": true,
        "llm_budget_max_calls": 2,
        "llm_budget_used_calls": 1,
        "llm_budget_kind": "universal_intent",
        "llm_concurrency_allowed": true,
        "llm_concurrency_limit": 1,
        "llm_concurrency_wait_sec": 0.2,
        "llm_prompt_chars": 565,
        "llm_candidate_count": 2,
        "llm_compact_candidates_chars": 135,
        "llm_elapsed_ms": 330.53,
        "llm_response_chars": 39,
        "llm_done_reason": "stop",
        "llm_parsed": true
      },
      "intent_risk_flags": [],
      "input_recovery": {
        "score": 0.231,
        "language": "en",
        "language_quality": 0.769,
        "should_review_intent": false,
        "reason": "English character n-gram quality=0.769",
        "action": "continue"
      },
      "llm_rejected_reason": "",
      "intent_candidates": [
        {
          "id": "c1",
          "domain": "game_controls",
          "operation": "control",
          "target": "",
          "confidence": 0.9,
          "reason": "heuristic fallback"
        },
        {
          "id": "c2",
          "domain": "games",
          "operation": "unknown",
          "target": "",
          "confidence": 0.97,
          "reason": "router category candidate"
        }
      ],
      "target": "",
      "filters": {},
      "needs": [],
      "answer_style": "direct_then_details",
      "heuristic": {
        "domain": "game_controls",
        "operation": "control",
        "confidence": 0.9,
        "reason": "domain_terms=2; control operation overrides domain; control terms found"
      }
    }
  }
]
```

**คำตอบก่อน**

Which game do you want controls for? Please provide the game title.

**คำตอบหลัง**

Which game do you want controls for? Please provide the game title.

## multi-controls-th — multi_controls

- คำถาม: `ขอดูปุ่มควบคุมเกม` → `VALORANT กับ Mario Kart 8 Deluxe`
- ก่อน: ผิด contract / `pipeline:no_answer`
- หลัง: ผ่าน / `pipeline:multi_question_splitter`
- เงื่อนไขตรวจหลัง: http_success=True, control_operation=True, all_targets=True, not_missing_target=True
- Trace ก่อนที่บันทึกจริง (คะแนนเป็นคะแนนของขั้นนั้น ไม่ใช่ความน่าจะเป็นว่าตอบถูก):

```json
[
  {
    "stage": "universal_intent",
    "decision": "games/detail",
    "confidence": 0.84,
    "detail": "known game alias found; known game title keeps games domain; no clear operation terms; bare known game title treated as detail",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false,
      "llm_first": false,
      "llm_first_skip_reason": "",
      "llm_first_review_reason": "",
      "llm_call": {},
      "intent_risk_flags": [],
      "input_recovery": {
        "score": 0.1868,
        "language": "en",
        "language_quality": 0.8132,
        "should_review_intent": false,
        "reason": "English character n-gram quality=0.813",
        "action": "continue"
      },
      "llm_rejected_reason": "",
      "intent_candidates": [
        {
          "id": "c1",
          "domain": "games",
          "operation": "detail",
          "target": "",
          "confidence": 0.84,
          "reason": "heuristic fallback"
        },
        {
          "id": "c2",
          "domain": "games",
          "operation": "list",
          "target": "",
          "confidence": 0.66,
          "reason": "game-domain catalog alternative"
        }
      ],
      "target": "",
      "filters": {},
      "needs": [
        "summarize_detail",
        "check_availability"
      ],
      "answer_style": "direct",
      "heuristic": {
        "domain": "games",
        "operation": "detail",
        "confidence": 0.84,
        "reason": "known game alias found; known game title keeps games domain; no clear operation terms; bare known game title treated as detail"
      }
    }
  }
]
```

**คำตอบก่อน**

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

**คำตอบหลัง**

คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:

คำถามที่ 1: VALORANT มีปุ่มควบคุมอะไรบ้าง
VALORANT มีข้อมูลปุ่มควบคุมดังนี้:
PC
•    W / A / S / D: เคลื่อนที่ - W เดินหน้า, A ไปซ้าย, S ถอยหลัง, D ไปขวา
•    Left Shift: เดินช้า - ใช้เดินเงียบหรือเดินแบบควบคุมเสียง
•    Space Bar: กระโดด - กระโดด
•    Left Ctrl: ย่อตัว - ย่อตัวเพื่อลดระดับตัวละคร
•    Left Mouse Button: ยิง - ยิงอาวุธหลัก
•    Right Mouse Button: ยิง/เล็งแบบรอง - ใช้งานโหมดรองของอาวุธหรือเล็งตามชนิดอาวุธ
•    R: รีโหลด - เปลี่ยนกระสุน
•    1 / 2 / 3: เลือกอาวุธ - 1 อาวุธหลัก, 2 อาวุธรอง, 3 อาวุธระยะประชิด
•    4: หยิบ/ใช้ Spike - ใช้กับ Spike เช่น วางหรือกู้ตามสถานการณ์
•    Q / E / C / X: ใช้สกิล Agent - Q/E/C คือสกิลทั่วไป และ X คือ Ultimate
•    F: โต้ตอบกับวัตถุ - ใช้โต้ตอบกับวัตถุในเกม
•    B: เปิดร้านซื้ออาวุธ - เปิดหน้า Armory ในช่วงซื้อของ
•    M: เปิดแผนที่ - เปิด/ปิดแผนที่
•    Tab: ดูตารางคะแนน - กดค้างเพื่อดู scoreboard
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

คำถามที่ 2: Mario Kart 8 Deluxe มีปุ่มควบคุมอะไรบ้าง
Mario Kart 8 Deluxe ปุ่มที่ตรงกับคำถาม:
Nintendo Switch
•    L (Left Stick): เลี้ยว / ควบคุมทิศทาง - บังคับพวงมาลัยรถให้เลี้ยวไปทางซ้ายหรือขวา
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://gameinputdatabase.com/game/57

## multi-controls-en — multi_controls

- คำถาม: `Show me the game controls` → `VALORANT and Mario Kart 8 Deluxe`
- ก่อน: ผิด contract / `pipeline:structured_game_availability_en`
- หลัง: ผ่าน / `pipeline:multi_question_splitter`
- เงื่อนไขตรวจหลัง: http_success=True, control_operation=True, all_targets=True, not_missing_target=True
- Trace ก่อนที่บันทึกจริง (คะแนนเป็นคะแนนของขั้นนั้น ไม่ใช่ความน่าจะเป็นว่าตอบถูก):

```json
[]
```

**คำตอบก่อน**

Mario Kart 8 Deluxe is available on: Nintendo Switch (1-2 Persons), Nintendo Switch (1-4 Persons). Studio zone(s): Nintendo Switch Zone.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

**คำตอบหลัง**

This question contains several topics. Here are the answers separately:

Question 1: What are the controls for VALORANT?
VALORANT controls:
- W / A / S / D: Move
- Left Shift: Walk
- Space Bar: Jump
- Left Ctrl: Crouch
- Left Mouse Button: Fire
- Right Mouse Button: Alternate Fire
- R: Reload
- 1 / 2 / 3: Equip weapons
- 4: Equip/Use Spike
- Q / E / C / X: Use abilities
- F: Use Object
- B: Open Armory
- M: Open Map
- Tab: Show Scoreboard
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

Question 2: What are the controls for Mario Kart 8 Deluxe?
Mario Kart 8 Deluxe controls:
- L (Left Stick): Steer
- A: Accelerate
- B: Brake
- X: Look Backward
- ZL: Use Item / Horn
- ZR: Drift
- + (Plus): Pause
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://gameinputdatabase.com/game/57

## multi-controls-typo-en — multi_controls

- คำถาม: `Show me the game controls` → `Valoant and Beat Saber please`
- ก่อน: ผิด contract / `pipeline:structured_game_controls_en`
- หลัง: ผ่าน / `pipeline:multi_question_splitter`
- เงื่อนไขตรวจหลัง: http_success=True, control_operation=True, all_targets=True, not_missing_target=True
- Trace ก่อนที่บันทึกจริง (คะแนนเป็นคะแนนของขั้นนั้น ไม่ใช่ความน่าจะเป็นว่าตอบถูก):

```json
[]
```

**คำตอบก่อน**

Beat Saber controls:
- Left PS VR2 Sense controller motion: Left-hand saber slash
- Right PS VR2 Sense controller motion: Right-hand saber slash
- Head/body movement: Dodge and position body
Source: https://www.playstation.com/en-us/games/beat-saber/

**คำตอบหลัง**

This question contains several topics. Here are the answers separately:

Question 1: What are the controls for VALORANT?
VALORANT controls:
- W / A / S / D: Move
- Left Shift: Walk
- Space Bar: Jump
- Left Ctrl: Crouch
- Left Mouse Button: Fire
- Right Mouse Button: Alternate Fire
- R: Reload
- 1 / 2 / 3: Equip weapons
- 4: Equip/Use Spike
- Q / E / C / X: Use abilities
- F: Use Object
- B: Open Armory
- M: Open Map
- Tab: Show Scoreboard
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

Question 2: What are the controls for Beat Saber?
Beat Saber controls:
- Left PS VR2 Sense controller motion: Left-hand saber slash
- Right PS VR2 Sense controller motion: Right-hand saber slash
- Head/body movement: Dodge and position body
Source: https://www.playstation.com/en-us/games/beat-saber/

## multi-catalog-th — multi_catalog

- คำถาม: `มีเกมอะไรให้เล่นบ้าง` → `PC กับ PS5`
- ก่อน: ผิด contract / `pipeline:no_answer`
- หลัง: ผ่าน / `pipeline:multi_question_splitter`
- เงื่อนไขตรวจหลัง: http_success=True, all_selected_zones=True, no_unselected_zones=True, catalog_operation=True
- Trace ก่อนที่บันทึกจริง (คะแนนเป็นคะแนนของขั้นนั้น ไม่ใช่ความน่าจะเป็นว่าตอบถูก):

```json
[
  {
    "stage": "universal_intent",
    "decision": "equipment/unknown",
    "confidence": 0.9,
    "detail": "candidate_intent:c1 heuristic fallback",
    "metadata": {
      "method": "llm",
      "llm_attempted": true,
      "llm_first": true,
      "llm_first_skip_reason": "",
      "llm_first_review_reason": "",
      "llm_call": {
        "llm_kind": "universal_intent",
        "llm_model": "scb10x/typhoon2.5-qwen3-4b",
        "llm_timeout_sec": 14.0,
        "llm_configured_timeout_sec": 14.0,
        "llm_num_predict": 18,
        "llm_num_ctx": 1536,
        "llm_cache_hit": false,
        "global_timeout_enabled": true,
        "global_timeout_sec": 18.35,
        "global_elapsed_sec": 0.1396,
        "global_remaining_sec": 18.2104,
        "finalizer_reserve_sec": 1.0,
        "work_remaining_sec": 17.2104,
        "timing_status": "running",
        "llm_health_enabled": true,
        "llm_health_allowed": true,
        "llm_health_status": "ok",
        "llm_health_kind": "universal_intent",
        "llm_health_model": "scb10x/typhoon2.5-qwen3-4b",
        "llm_health_failures": 0,
        "llm_health_cooldown_remaining_sec": 0.0,
        "llm_health_last_error_type": "",
        "llm_health_last_error": "",
        "llm_health_failure_scope": "kind_only",
        "llm_budget_enabled": true,
        "llm_budget_allowed": true,
        "llm_budget_max_calls": 2,
        "llm_budget_used_calls": 1,
        "llm_budget_kind": "universal_intent",
        "llm_concurrency_allowed": true,
        "llm_concurrency_limit": 1,
        "llm_concurrency_wait_sec": 0.2,
        "llm_prompt_chars": 700,
        "llm_candidate_count": 4,
        "llm_compact_candidates_chars": 280,
        "llm_elapsed_ms": 5060.79,
        "llm_response_chars": 39,
        "llm_done_reason": "stop",
        "llm_parsed": true
      },
      "intent_risk_flags": [],
      "input_recovery": {
        "score": 0.5864,
        "language": "en",
        "language_quality": 0.4136,
        "should_review_intent": true,
        "reason": "English character n-gram quality=0.414",
        "action": "bounded_llm_intent_review"
      },
      "llm_rejected_reason": "",
      "intent_candidates": [
        {
          "id": "c1",
          "domain": "equipment",
          "operation": "unknown",
          "target": "",
          "confidence": 0.45,
          "reason": "heuristic fallback"
        },
        {
          "id": "c2",
          "domain": "general",
          "operation": "detail",
          "target": "",
          "confidence": 0.55,
          "reason": "router category candidate"
        },
        {
          "id": "c3",
          "domain": "knowledge",
          "operation": "detail",
          "target": "chatbot_greeting",
          "confidence": 0.6,
          "reason": "possible chatbot greeting; tolerate informal spelling"
        },
        {
          "id": "c4",
          "domain": "equipment",
          "operation": "detail",
          "target": "",
          "confidence": 0.74,
          "reason": "domain keyword score=2"
        }
      ],
      "target": "",
      "filters": {},
      "needs": [],
      "answer_style": "direct",
      "heuristic": {
        "domain": "equipment",
        "operation": "unknown",
        "confidence": 0.45,
        "reason": "domain_terms=2; no clear operation terms"
      }
    }
  }
]
```

**คำตอบก่อน**

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด equipment ตอนนี้ครับ

**คำตอบหลัง**

คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:

คำถามที่ 1: PC มีเกมอะไรบ้าง
PC Zone แยกรายการเกมตามเลขเครื่องดังนี้

PC #01-#02 (60 นาที, 1 คน)
•    TEKKEN 8
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    VALORANT
หมายเหตุ: PC #01-#02 มี TEKKEN 8 แต่ไม่มี Call of Duty: Warzone
หมายเหตุ: PC #01-#02 และ PC #03-#10 มี Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS, VALORANT เหมือนกัน

PC #03-#10 (60 นาที, 1 คน)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    VALORANT
หมายเหตุ: PC #03-#10 มี Call of Duty: Warzone แต่ไม่มี TEKKEN 8
หมายเหตุ: PC #01-#02 และ PC #03-#10 มี Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS, VALORANT เหมือนกัน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

คำถามที่ 2: PlayStation 5 มีเกมอะไรบ้าง
PlayStation 5 Zone มีเกมที่ยืนยันได้ดังนี้

PlayStation 5 #01-#02 (60 นาที, 1-2 คน)
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
หมายเหตุ: PlayStation 5 #01 และ #02 ใช้รายการเกมเดียวกัน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

## multi-catalog-en — multi_catalog

- คำถาม: `What games can I play?` → `PC and PS5`
- ก่อน: ผิด contract / `pipeline:structured_equipment_catalog_en`
- หลัง: ผ่าน / `pipeline:multi_question_splitter`
- เงื่อนไขตรวจหลัง: http_success=True, all_selected_zones=True, no_unselected_zones=True, catalog_operation=True
- Trace ก่อนที่บันทึกจริง (คะแนนเป็นคะแนนของขั้นนั้น ไม่ใช่ความน่าจะเป็นว่าตอบถูก):

```json
[
  {
    "stage": "universal_intent",
    "decision": "equipment/unknown",
    "confidence": 0.9,
    "detail": "candidate_intent:c1 heuristic fallback",
    "metadata": {
      "method": "llm",
      "llm_attempted": true,
      "llm_first": true,
      "llm_first_skip_reason": "",
      "llm_first_review_reason": "forced bounded intent review for broad English structured response",
      "llm_call": {
        "llm_kind": "universal_intent",
        "llm_model": "scb10x/typhoon2.5-qwen3-4b",
        "llm_timeout_sec": 14.0,
        "llm_configured_timeout_sec": 14.0,
        "llm_num_predict": 18,
        "llm_num_ctx": 1536,
        "llm_cache_hit": false,
        "global_timeout_enabled": true,
        "global_timeout_sec": 18.35,
        "global_elapsed_sec": 0.224,
        "global_remaining_sec": 18.126,
        "finalizer_reserve_sec": 1.0,
        "work_remaining_sec": 17.126,
        "timing_status": "running",
        "llm_health_enabled": true,
        "llm_health_allowed": true,
        "llm_health_status": "ok",
        "llm_health_kind": "universal_intent",
        "llm_health_model": "scb10x/typhoon2.5-qwen3-4b",
        "llm_health_failures": 0,
        "llm_health_cooldown_remaining_sec": 0.0,
        "llm_health_last_error_type": "",
        "llm_health_last_error": "",
        "llm_health_failure_scope": "kind_only",
        "llm_budget_enabled": true,
        "llm_budget_allowed": true,
        "llm_budget_max_calls": 2,
        "llm_budget_used_calls": 1,
        "llm_budget_kind": "universal_intent",
        "llm_concurrency_allowed": true,
        "llm_concurrency_limit": 1,
        "llm_concurrency_wait_sec": 0.2,
        "llm_prompt_chars": 700,
        "llm_candidate_count": 4,
        "llm_compact_candidates_chars": 280,
        "llm_elapsed_ms": 342.03,
        "llm_response_chars": 39,
        "llm_done_reason": "stop",
        "llm_parsed": true
      },
      "intent_risk_flags": [],
      "input_recovery": {
        "score": 0.5282,
        "language": "en",
        "language_quality": 0.4718,
        "should_review_intent": true,
        "reason": "English character n-gram quality=0.472",
        "action": "bounded_llm_intent_review"
      },
      "llm_rejected_reason": "",
      "intent_candidates": [
        {
          "id": "c1",
          "domain": "equipment",
          "operation": "unknown",
          "target": "",
          "confidence": 0.45,
          "reason": "heuristic fallback"
        },
        {
          "id": "c2",
          "domain": "general",
          "operation": "detail",
          "target": "",
          "confidence": 0.55,
          "reason": "router category candidate"
        },
        {
          "id": "c3",
          "domain": "knowledge",
          "operation": "detail",
          "target": "chatbot_greeting",
          "confidence": 0.6,
          "reason": "possible chatbot greeting; tolerate informal spelling"
        },
        {
          "id": "c4",
          "domain": "equipment",
          "operation": "detail",
          "target": "",
          "confidence": 0.74,
          "reason": "domain keyword score=2"
        }
      ],
      "target": "",
      "filters": {},
      "needs": [],
      "answer_style": "direct",
      "heuristic": {
        "domain": "equipment",
        "operation": "unknown",
        "confidence": 0.45,
        "reason": "domain_terms=2; no clear operation terms"
      }
    }
  }
]
```

**คำตอบก่อน**

Verified equipment in PlayStation 5 Zone:
- PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive (PlayStation 5 Zone / VR Zone) - 2 Units in PlayStation 5 Zone and 1 Unit in VR Zone
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

**คำตอบหลัง**

This question contains several topics. Here are the answers separately:

Question 1: What games are available in PC?
There are currently 6 verified games in PC Zone.

PC Zone (6 games)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

Question 2: What games are available in PlayStation 5?
There are currently 17 verified games in PlayStation 5 Zone.

PlayStation 5 Zone (17 games)
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
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

## multi-catalog-typo-en — multi_catalog

- คำถาม: `What games can I play?` → `PC and cockpik please`
- ก่อน: ผิด contract / `pipeline:structured_games_catalog_en`
- หลัง: ผ่าน / `pipeline:multi_question_splitter`
- เงื่อนไขตรวจหลัง: http_success=True, all_selected_zones=True, no_unselected_zones=True, catalog_operation=True
- Trace ก่อนที่บันทึกจริง (คะแนนเป็นคะแนนของขั้นนั้น ไม่ใช่ความน่าจะเป็นว่าตอบถูก):

```json
[]
```

**คำตอบก่อน**

There are currently 6 verified games in PC Zone.

PC Zone (6 games)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

**คำตอบหลัง**

This question contains several topics. Here are the answers separately:

Question 1: What games are available in PC?
There are currently 6 verified games in PC Zone.

PC Zone (6 games)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

Question 2: What games are available in Cockpit?
There are currently 1 verified games in Cockpit Zone.

Cockpit Zone (1 game)
•    Gran Turismo 7
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

## roman-edition-en — wrong_edition

- คำถาม: `Show me the game controls` → `TEKKEN IX`
- ก่อน: ผิด contract / `pipeline:structured_game_controls_en`
- หลัง: ผ่าน / `pipeline:game_edition_unconfirmed`
- เงื่อนไขตรวจหลัง: http_success=True, not_other_edition=True, not_missing_target=True, not_catalog=True, source_status=True
- Trace ก่อนที่บันทึกจริง (คะแนนเป็นคะแนนของขั้นนั้น ไม่ใช่ความน่าจะเป็นว่าตอบถูก):

```json
[]
```

**คำตอบก่อน**

TEKKEN 8 controls:
- Square: Left Punch
- Triangle: Right Punch
- Cross: Left Kick
- Circle: Right Kick
- D-Pad Up: Jump
- D-Pad Left: Move Backward
- D-Pad Down: Duck
- L (Left Stick): Move
- L1: Special Style
- R1: Heat Activate
- R1 (While in Heat): Heat Smash
- Options: Pause
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://gameinputdatabase.com/game/83

**คำตอบหลัง**

I do not have verified information for tekken ix in the recorded studio catalog. Please confirm the game title and edition.
Source: https://esports.phuket.psu.ac.th/Services/our-games

## roman-edition-th — wrong_edition

- คำถาม: `ขอดูปุ่มควบคุมเกม` → `TEKKEN IX`
- ก่อน: ผิด contract / `pipeline:structured_game_controls`
- หลัง: ผ่าน / `pipeline:game_edition_unconfirmed`
- เงื่อนไขตรวจหลัง: http_success=True, not_other_edition=True, not_missing_target=True, not_catalog=True, source_status=True
- Trace ก่อนที่บันทึกจริง (คะแนนเป็นคะแนนของขั้นนั้น ไม่ใช่ความน่าจะเป็นว่าตอบถูก):

```json
[
  {
    "stage": "universal_intent",
    "decision": "game_controls/control",
    "confidence": 0.9,
    "detail": "candidate_intent:c1 heuristic fallback",
    "metadata": {
      "method": "llm",
      "llm_attempted": true,
      "llm_first": true,
      "llm_first_skip_reason": "",
      "llm_first_review_reason": "",
      "llm_call": {
        "llm_kind": "universal_intent",
        "llm_model": "scb10x/typhoon2.5-qwen3-4b",
        "llm_timeout_sec": 14.0,
        "llm_configured_timeout_sec": 14.0,
        "llm_num_predict": 18,
        "llm_num_ctx": 1536,
        "llm_cache_hit": false,
        "global_timeout_enabled": true,
        "global_timeout_sec": 18.35,
        "global_elapsed_sec": 0.1938,
        "global_remaining_sec": 18.1561,
        "finalizer_reserve_sec": 1.0,
        "work_remaining_sec": 17.1561,
        "timing_status": "running",
        "llm_health_enabled": true,
        "llm_health_allowed": true,
        "llm_health_status": "ok",
        "llm_health_kind": "universal_intent",
        "llm_health_model": "scb10x/typhoon2.5-qwen3-4b",
        "llm_health_failures": 0,
        "llm_health_cooldown_remaining_sec": 0.0,
        "llm_health_last_error_type": "",
        "llm_health_last_error": "",
        "llm_health_failure_scope": "kind_only",
        "llm_budget_enabled": true,
        "llm_budget_allowed": true,
        "llm_budget_max_calls": 2,
        "llm_budget_used_calls": 1,
        "llm_budget_kind": "universal_intent",
        "llm_concurrency_allowed": true,
        "llm_concurrency_limit": 1,
        "llm_concurrency_wait_sec": 0.2,
        "llm_prompt_chars": 701,
        "llm_candidate_count": 4,
        "llm_compact_candidates_chars": 261,
        "llm_elapsed_ms": 320.89,
        "llm_response_chars": 39,
        "llm_done_reason": "stop",
        "llm_parsed": true
      },
      "intent_risk_flags": [
        "competing_domain_signals"
      ],
      "input_recovery": {
        "score": 0.1972,
        "language": "mixed",
        "language_quality": 0.8028,
        "should_review_intent": false,
        "reason": "Thai character n-gram quality=0.803",
        "action": "continue"
      },
      "llm_rejected_reason": "",
      "intent_candidates": [
        {
          "id": "c1",
          "domain": "game_controls",
          "operation": "control",
          "target": "",
          "confidence": 0.9,
          "reason": "heuristic fallback"
        },
        {
          "id": "c2",
          "domain": "games",
          "operation": "unknown",
          "target": "",
          "confidence": 0.97,
          "reason": "router category candidate"
        },
        {
          "id": "c3",
          "domain": "games",
          "operation": "list",
          "target": "",
          "confidence": 0.66,
          "reason": "game-domain catalog alternative"
        },
        {
          "id": "c4",
          "domain": "equipment",
          "operation": "how_to",
          "target": "",
          "confidence": 0.72,
          "reason": "controller equipment phrase"
        }
      ],
      "target": "",
      "filters": {},
      "needs": [],
      "answer_style": "direct_then_details",
      "heuristic": {
        "domain": "game_controls",
        "operation": "control",
        "confidence": 0.9,
        "reason": "known game alias found; control operation overrides domain; control terms found"
      }
    }
  }
]
```

**คำตอบก่อน**

TEKKEN 8 มีข้อมูลปุ่มควบคุมดังนี้:
PlayStation / PS5
•    Square: หมัดซ้าย / ต่อยซ้าย - ออกหมัดแย็บหรือโจมตีด้วยมือซ้าย เป็นปุ่มหลักในการเริ่มต้นเฟรมคอมโบที่รวดเร็ว
•    Triangle: หมัดขวา / ต่อยขวา - ออกหมัดหนักหรือโจมตีด้วยมือขวา มักใช้ทำดาเมจแรงหรือสวนกลับ (Counter)
•    Cross: ลูกเตะซ้าย - ใช้ขาซ้ายเตะสกัดหรือโจมตีเพื่อเปิดช่องว่างของศัตรู
•    Circle: ลูกเตะขวา - ใช้ขาขวาหวดเตะอย่างรุนแรง มักเป็นท่าเคลียร์ระยะหรือตัดขาที่ทำดาเมจสูง
•    D-Pad Up: กระโดด - ควบคุมให้ตัวละครกระโดดขึ้นด้านบนเพื่อหลบการโจมตีล่าง หรือใช้กดร่วมกับปุ่มโจมตีกลางอากาศ
•    D-Pad Left: ถอยหลัง / บล็อก - บังคับตัวละครให้เดินถอยหลังเพื่อรักษาระยะ หรือใช้กดค้างเพื่อ "บล็อก (Guard)" การโจมตีระดับสูงและระดับกลางของศัตรู
•    D-Pad Down: ย่อตัว / ก้มหลบ - สั่งให้ตัวละครย่อตัวต่ำ ใช้ก้มหลบหมัดหรือการโจมตีระดับสูง (High) และใช้บล็อกการโจมตีระดับต่ำ (Low)
•    L (Left Stick): เคลื่อนที่ - ขยับทิศทางของตัวละคร بشكلทั่วไป หรือใช้โยกทิศทางในการเคลื่อนที่และเดินหน้าถอยหลัง
•    L1: สเปเชียลสไตล์ - กดเพื่อเปิด/ปิดโหมดช่วยเหลืออัจฉริยะ ช่วยให้กดคอมโบและท่าไม้ตายของตัวละครนั้น ๆ ได้ง่ายด้วยปุ่มเดียว
•    R1: เปิดใช้งาน Heat - ระเบิดพลัง Heat System เข้าสู่สถานะโอเวอร์ไดรฟ์เพื่อบัฟการโจมตีและเพิ่มคุณสมบัติพิเศษให้ตัวละคร


[ตัดข้อความในเอกสารนี้; ฉบับเต็มอยู่ raw]

**คำตอบหลัง**

ยังไม่พบข้อมูลยืนยันของ tekken ix ในรายการเกมของศูนย์ครับ กรุณายืนยันชื่อเกมและภาคที่ต้องการอีกครั้ง
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

## new-operation-en — new_detail

- คำถาม: `Show me the game controls` → `What is VALORANT?`
- ก่อน: ผ่าน / `pipeline:structured_game_detail_en`
- หลัง: ผ่าน / `pipeline:structured_game_detail_en`
- เงื่อนไขตรวจหลัง: http_success=True, new_operation=True
- Trace ก่อนที่บันทึกจริง (คะแนนเป็นคะแนนของขั้นนั้น ไม่ใช่ความน่าจะเป็นว่าตอบถูก):

```json
[]
```

**คำตอบก่อน**

Verified English information:
VALORANT
Genre: Tactical 5v5 team-based FPS
Overview: VALORANT is a tactical shooter game where players select agents with unique skills and play as either attackers or defenders in each round.
How to play: Attackers must plant the Spike; defenders must defend the area or defuse the Spike. Play emphasizes aiming, communication, ability use and teamwork.
Available at: PC Zone
Source: https://esports.computing.psu.ac.th/reservation (original source in Thai)

**คำตอบหลัง**

Verified English information:
VALORANT
Genre: Tactical 5v5 team-based FPS
Overview: VALORANT is a tactical shooter game where players select agents with unique skills and play as either attackers or defenders in each round.
How to play: Attackers must plant the Spike; defenders must defend the area or defuse the Spike. Play emphasizes aiming, communication, ability use and teamwork.
Available at: PC Zone
Source: https://esports.computing.psu.ac.th/reservation (original source in Thai)

## new-operation-th — new_detail

- คำถาม: `ขอดูปุ่มควบคุมเกม` → `VALORANT คืออะไร`
- ก่อน: ผ่าน / `pipeline:structured_game_detail`
- หลัง: ผ่าน / `pipeline:structured_game_detail`
- เงื่อนไขตรวจหลัง: http_success=True, new_operation=True
- Trace ก่อนที่บันทึกจริง (คะแนนเป็นคะแนนของขั้นนั้น ไม่ใช่ความน่าจะเป็นว่าตอบถูก):

```json
[
  {
    "stage": "universal_intent",
    "decision": "games/detail",
    "confidence": 0.9,
    "detail": "candidate_intent:c1 heuristic fallback",
    "metadata": {
      "method": "llm",
      "llm_attempted": true,
      "llm_first": true,
      "llm_first_skip_reason": "",
      "llm_first_review_reason": "",
      "llm_call": {
        "llm_kind": "universal_intent",
        "llm_model": "scb10x/typhoon2.5-qwen3-4b",
        "llm_timeout_sec": 14.0,
        "llm_configured_timeout_sec": 14.0,
        "llm_num_predict": 18,
        "llm_num_ctx": 1536,
        "llm_cache_hit": true,
        "global_timeout_enabled": true,
        "global_timeout_sec": 18.35,
        "global_elapsed_sec": 0.0631,
        "global_remaining_sec": 18.2868,
        "finalizer_reserve_sec": 1.0,
        "work_remaining_sec": 17.2868,
        "timing_status": "running",
        "llm_elapsed_ms": 0.0,
        "llm_response_chars": 0,
        "llm_parsed": true
      },
      "intent_risk_flags": [],
      "input_recovery": {
        "score": 0.0726,
        "language": "mixed",
        "language_quality": 0.9274,
        "should_review_intent": false,
        "reason": "Thai character n-gram quality=0.927",
        "action": "continue"
      },
      "llm_rejected_reason": "",
      "intent_candidates": [
        {
          "id": "c1",
          "domain": "games",
          "operation": "detail",
          "target": "",
          "confidence": 0.8,
          "reason": "heuristic fallback"
        },
        {
          "id": "c2",
          "domain": "games",
          "operation": "list",
          "target": "",
          "confidence": 0.66,
          "reason": "game-domain catalog alternative"
        }
      ],
      "target": "",
      "filters": {},
      "needs": [],
      "answer_style": "direct",
      "heuristic": {
        "domain": "games",
        "operation": "detail",
        "confidence": 0.8,
        "reason": "known game alias found; detail terms found"
      }
    }
  }
]
```

**คำตอบก่อน**

VALORANT: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ
แนวเกม: เกมยิง Tactical FPS แบบทีม 5v5
วิธีเล่นโดยสรุป: ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือกู้ Spike การเล่นเน้นการเล็ง การสื่อสาร การใช้สกิล และการเล่นเป็นทีม
เล่นได้ที่: PC Zone
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**คำตอบหลัง**

VALORANT: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ
แนวเกม: เกมยิง Tactical FPS แบบทีม 5v5
วิธีเล่นโดยสรุป: ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือกู้ Spike การเล่นเน้นการเล็ง การสื่อสาร การใช้สกิล และการเล่นเป็นทีม
เล่นได้ที่: PC Zone
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

## unknown-latin-en — unknown_controls

- คำถาม: `Show me the game controls` → `Minecraft`
- ก่อน: ผ่าน / `pipeline:game_controls_target_unconfirmed`
- หลัง: ผ่าน / `pipeline:game_controls_target_unconfirmed`
- เงื่อนไขตรวจหลัง: http_success=True, no_substitute=True, received_name=True, keeps_operation=True
- Trace ก่อนที่บันทึกจริง (คะแนนเป็นคะแนนของขั้นนั้น ไม่ใช่ความน่าจะเป็นว่าตอบถูก):

```json
[]
```

**คำตอบก่อน**

I could not find verified control information for the game you named in the studio records. Please confirm its exact title and edition.
Source: https://esports.phuket.psu.ac.th/Services/our-games

**คำตอบหลัง**

I could not find verified control information for the game you named in the studio records. Please confirm its exact title and edition.
Source: https://esports.phuket.psu.ac.th/Services/our-games

## unknown-thai-th — unknown_controls

- คำถาม: `ขอดูปุ่มควบคุมเกม` → `มายคราฟต์`
- ก่อน: ผิด contract / `pipeline:candidate_margin_clarification`
- หลัง: ผ่าน / `pipeline:game_controls_target_unconfirmed`
- เงื่อนไขตรวจหลัง: http_success=True, no_substitute=True, received_name=True, keeps_operation=True
- Trace ก่อนที่บันทึกจริง (คะแนนเป็นคะแนนของขั้นนั้น ไม่ใช่ความน่าจะเป็นว่าตอบถูก):

```json
[
  {
    "stage": "universal_intent",
    "decision": "general/unknown",
    "confidence": 0.9,
    "detail": "candidate_intent:c1 heuristic fallback",
    "metadata": {
      "method": "llm",
      "llm_attempted": true,
      "llm_first": true,
      "llm_first_skip_reason": "",
      "llm_first_review_reason": "",
      "llm_call": {
        "llm_kind": "universal_intent",
        "llm_model": "scb10x/typhoon2.5-qwen3-4b",
        "llm_timeout_sec": 14.0,
        "llm_configured_timeout_sec": 14.0,
        "llm_num_predict": 18,
        "llm_num_ctx": 1536,
        "llm_cache_hit": false,
        "global_timeout_enabled": true,
        "global_timeout_sec": 18.35,
        "global_elapsed_sec": 0.0647,
        "global_remaining_sec": 18.2852,
        "finalizer_reserve_sec": 1.0,
        "work_remaining_sec": 17.2852,
        "timing_status": "running",
        "llm_health_enabled": true,
        "llm_health_allowed": true,
        "llm_health_status": "ok",
        "llm_health_kind": "universal_intent",
        "llm_health_model": "scb10x/typhoon2.5-qwen3-4b",
        "llm_health_failures": 0,
        "llm_health_cooldown_remaining_sec": 0.0,
        "llm_health_last_error_type": "",
        "llm_health_last_error": "",
        "llm_health_failure_scope": "kind_only",
        "llm_budget_enabled": true,
        "llm_budget_allowed": true,
        "llm_budget_max_calls": 2,
        "llm_budget_used_calls": 1,
        "llm_budget_kind": "universal_intent",
        "llm_concurrency_allowed": true,
        "llm_concurrency_limit": 1,
        "llm_concurrency_wait_sec": 0.2,
        "llm_prompt_chars": 629,
        "llm_candidate_count": 3,
        "llm_compact_candidates_chars": 212,
        "llm_elapsed_ms": 308.49,
        "llm_response_chars": 39,
        "llm_done_reason": "stop",
        "llm_parsed": true
      },
      "intent_risk_flags": [
        "low_candidate_margin"
      ],
      "input_recovery": {
        "score": 0.1748,
        "language": "th",
        "language_quality": 0.8252,
        "should_review_intent": false,
        "reason": "Thai character n-gram quality=0.825",
        "action": "continue"
      },
      "llm_rejected_reason": "",
      "intent_candidates": [
        {
          "id": "c1",
          "domain": "general",
          "operation": "unknown",
          "target": "",
          "confidence": 0.45,
          "reason": "heuristic fallback"
        },
        {
          "id": "c2",
          "domain": "general",
          "operation": "detail",
          "target": "",
          "confidence": 0.55,
          "reason": "router category candidate"
        },
        {
          "id": "c3",
          "domain": "knowledge",
          "operation": "detail",
          "target": "chatbot_greeting",
          "confidence": 0.6,
          "reason": "possible chatbot greeting; tolerate informal spelling"
        }
      ],
      "target": "",
      "filters": {},
      "needs": [],
      "answer_style": "direct",
      "heuristic": {
        "domain": "general",
        "operation": "unknown",
        "confidence": 0.45,
        "reason": "domain_terms=2; no clear operation terms"
      }
    }
  }
]
```

**คำตอบก่อน**

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

**คำตอบหลัง**

ยังไม่พบข้อมูลปุ่มควบคุมที่ยืนยันสำหรับเกมที่คุณระบุในฐานข้อมูลของศูนย์ครับ กรุณาตรวจชื่อเต็มและภาคของเกมอีกครั้ง
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

## known-controls-en — single_controls

- คำถาม: `What are the controls for VALORANT?`
- ก่อน: ผ่าน / `pipeline:structured_game_controls_en`
- หลัง: ผ่าน / `pipeline:structured_game_controls_en`
- เงื่อนไขตรวจหลัง: http_success=True, control_operation=True, all_targets=True, not_missing_target=True
- Trace ก่อนที่บันทึกจริง (คะแนนเป็นคะแนนของขั้นนั้น ไม่ใช่ความน่าจะเป็นว่าตอบถูก):

```json
[]
```

**คำตอบก่อน**

VALORANT controls:
- W / A / S / D: Move
- Left Shift: Walk
- Space Bar: Jump
- Left Ctrl: Crouch
- Left Mouse Button: Fire
- Right Mouse Button: Alternate Fire
- R: Reload
- 1 / 2 / 3: Equip weapons
- 4: Equip/Use Spike
- Q / E / C / X: Use abilities
- F: Use Object
- B: Open Armory
- M: Open Map
- Tab: Show Scoreboard
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

**คำตอบหลัง**

VALORANT controls:
- W / A / S / D: Move
- Left Shift: Walk
- Space Bar: Jump
- Left Ctrl: Crouch
- Left Mouse Button: Fire
- Right Mouse Button: Alternate Fire
- R: Reload
- 1 / 2 / 3: Equip weapons
- 4: Equip/Use Spike
- Q / E / C / X: Use abilities
- F: Use Object
- B: Open Armory
- M: Open Map
- Tab: Show Scoreboard
These controls come from a secondary guide and have not been checked against the studio's installed game and controller settings.
Source: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

## known-controls-th — single_controls

- คำถาม: `VALORANT มีปุ่มอะไรบ้าง`
- ก่อน: ผ่าน / `pipeline:structured_game_controls`
- หลัง: ผ่าน / `pipeline:structured_game_controls`
- เงื่อนไขตรวจหลัง: http_success=True, control_operation=True, all_targets=True, not_missing_target=True
- Trace ก่อนที่บันทึกจริง (คะแนนเป็นคะแนนของขั้นนั้น ไม่ใช่ความน่าจะเป็นว่าตอบถูก):

```json
[
  {
    "stage": "universal_intent",
    "decision": "game_controls/control",
    "confidence": 0.9,
    "detail": "candidate_intent:c1 heuristic fallback",
    "metadata": {
      "method": "llm",
      "llm_attempted": true,
      "llm_first": true,
      "llm_first_skip_reason": "",
      "llm_first_review_reason": "",
      "llm_call": {
        "llm_kind": "universal_intent",
        "llm_model": "scb10x/typhoon2.5-qwen3-4b",
        "llm_timeout_sec": 14.0,
        "llm_configured_timeout_sec": 14.0,
        "llm_num_predict": 18,
        "llm_num_ctx": 1536,
        "llm_cache_hit": false,
        "global_timeout_enabled": true,
        "global_timeout_sec": 18.35,
        "global_elapsed_sec": 0.1534,
        "global_remaining_sec": 18.1965,
        "finalizer_reserve_sec": 1.0,
        "work_remaining_sec": 17.1965,
        "timing_status": "running",
        "llm_health_enabled": true,
        "llm_health_allowed": true,
        "llm_health_status": "ok",
        "llm_health_kind": "universal_intent",
        "llm_health_model": "scb10x/typhoon2.5-qwen3-4b",
        "llm_health_failures": 0,
        "llm_health_cooldown_remaining_sec": 0.0,
        "llm_health_last_error_type": "",
        "llm_health_last_error": "",
        "llm_health_failure_scope": "kind_only",
        "llm_budget_enabled": true,
        "llm_budget_allowed": true,
        "llm_budget_max_calls": 2,
        "llm_budget_used_calls": 1,
        "llm_budget_kind": "universal_intent",
        "llm_concurrency_allowed": true,
        "llm_concurrency_limit": 1,
        "llm_concurrency_wait_sec": 0.2,
        "llm_prompt_chars": 695,
        "llm_candidate_count": 4,
        "llm_compact_candidates_chars": 261,
        "llm_elapsed_ms": 324.93,
        "llm_response_chars": 39,
        "llm_done_reason": "stop",
        "llm_parsed": true
      },
      "intent_risk_flags": [
        "competing_domain_signals"
      ],
      "input_recovery": {
        "score": 0.2145,
        "language": "mixed",
        "language_quality": 0.7855,
        "should_review_intent": false,
        "reason": "Thai character n-gram quality=0.785",
        "action": "continue"
      },
      "llm_rejected_reason": "",
      "intent_candidates": [
        {
          "id": "c1",
          "domain": "game_controls",
          "operation": "control",
          "target": "",
          "confidence": 0.9,
          "reason": "heuristic fallback"
        },
        {
          "id": "c2",
          "domain": "games",
          "operation": "unknown",
          "target": "",
          "confidence": 0.97,
          "reason": "router category candidate"
        },
        {
          "id": "c3",
          "domain": "games",
          "operation": "list",
          "target": "",
          "confidence": 0.66,
          "reason": "game-domain catalog alternative"
        },
        {
          "id": "c4",
          "domain": "equipment",
          "operation": "how_to",
          "target": "",
          "confidence": 0.72,
          "reason": "controller equipment phrase"
        }
      ],
      "target": "",
      "filters": {},
      "needs": [],
      "answer_style": "direct_then_details",
      "heuristic": {
        "domain": "game_controls",
        "operation": "control",
        "confidence": 0.9,
        "reason": "known game alias found; control operation overrides domain; control terms found"
      }
    }
  }
]
```

**คำตอบก่อน**

VALORANT มีข้อมูลปุ่มควบคุมดังนี้:
PC
•    W / A / S / D: เคลื่อนที่ - W เดินหน้า, A ไปซ้าย, S ถอยหลัง, D ไปขวา
•    Left Shift: เดินช้า - ใช้เดินเงียบหรือเดินแบบควบคุมเสียง
•    Space Bar: กระโดด - กระโดด
•    Left Ctrl: ย่อตัว - ย่อตัวเพื่อลดระดับตัวละคร
•    Left Mouse Button: ยิง - ยิงอาวุธหลัก
•    Right Mouse Button: ยิง/เล็งแบบรอง - ใช้งานโหมดรองของอาวุธหรือเล็งตามชนิดอาวุธ
•    R: รีโหลด - เปลี่ยนกระสุน
•    1 / 2 / 3: เลือกอาวุธ - 1 อาวุธหลัก, 2 อาวุธรอง, 3 อาวุธระยะประชิด
•    4: หยิบ/ใช้ Spike - ใช้กับ Spike เช่น วางหรือกู้ตามสถานการณ์
•    Q / E / C / X: ใช้สกิล Agent - Q/E/C คือสกิลทั่วไป และ X คือ Ultimate
•    F: โต้ตอบกับวัตถุ - ใช้โต้ตอบกับวัตถุในเกม
•    B: เปิดร้านซื้ออาวุธ - เปิดหน้า Armory ในช่วงซื้อของ
•    M: เปิดแผนที่ - เปิด/ปิดแผนที่
•    Tab: ดูตารางคะแนน - กดค้างเพื่อดู scoreboard
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

**คำตอบหลัง**

VALORANT มีข้อมูลปุ่มควบคุมดังนี้:
PC
•    W / A / S / D: เคลื่อนที่ - W เดินหน้า, A ไปซ้าย, S ถอยหลัง, D ไปขวา
•    Left Shift: เดินช้า - ใช้เดินเงียบหรือเดินแบบควบคุมเสียง
•    Space Bar: กระโดด - กระโดด
•    Left Ctrl: ย่อตัว - ย่อตัวเพื่อลดระดับตัวละคร
•    Left Mouse Button: ยิง - ยิงอาวุธหลัก
•    Right Mouse Button: ยิง/เล็งแบบรอง - ใช้งานโหมดรองของอาวุธหรือเล็งตามชนิดอาวุธ
•    R: รีโหลด - เปลี่ยนกระสุน
•    1 / 2 / 3: เลือกอาวุธ - 1 อาวุธหลัก, 2 อาวุธรอง, 3 อาวุธระยะประชิด
•    4: หยิบ/ใช้ Spike - ใช้กับ Spike เช่น วางหรือกู้ตามสถานการณ์
•    Q / E / C / X: ใช้สกิล Agent - Q/E/C คือสกิลทั่วไป และ X คือ Ultimate
•    F: โต้ตอบกับวัตถุ - ใช้โต้ตอบกับวัตถุในเกม
•    B: เปิดร้านซื้ออาวุธ - เปิดหน้า Armory ในช่วงซื้อของ
•    M: เปิดแผนที่ - เปิด/ปิดแผนที่
•    Tab: ดูตารางคะแนน - กดค้างเพื่อดู scoreboard
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://www.shacknews.com/article/117434/valorant-pc-controls-and-keybindings

## hardware-not-game-en — not_generic_controls

- คำถาม: `What controller model does the PS5 zone use?`
- ก่อน: ผ่าน / `pipeline:equipment_spec_unverified_en`
- หลัง: ผ่าน / `pipeline:equipment_spec_unverified_en`
- เงื่อนไขตรวจหลัง: http_success=True, not_generic_controls=True
- Trace ก่อนที่บันทึกจริง (คะแนนเป็นคะแนนของขั้นนั้น ไม่ใช่ความน่าจะเป็นว่าตอบถูก):

```json
[
  {
    "stage": "universal_intent",
    "decision": "game_controls/control",
    "confidence": 0.9,
    "detail": "candidate_intent:c1 heuristic fallback",
    "metadata": {
      "method": "llm",
      "llm_attempted": true,
      "llm_first": true,
      "llm_first_skip_reason": "",
      "llm_first_review_reason": "forced bounded intent review for broad English structured response",
      "llm_call": {
        "llm_kind": "universal_intent",
        "llm_model": "scb10x/typhoon2.5-qwen3-4b",
        "llm_timeout_sec": 14.0,
        "llm_configured_timeout_sec": 14.0,
        "llm_num_predict": 18,
        "llm_num_ctx": 1536,
        "llm_cache_hit": false,
        "global_timeout_enabled": true,
        "global_timeout_sec": 18.35,
        "global_elapsed_sec": 2.7862,
        "global_remaining_sec": 15.5637,
        "finalizer_reserve_sec": 1.0,
        "work_remaining_sec": 14.5637,
        "timing_status": "running",
        "llm_health_enabled": true,
        "llm_health_allowed": true,
        "llm_health_status": "ok",
        "llm_health_kind": "universal_intent",
        "llm_health_model": "scb10x/typhoon2.5-qwen3-4b",
        "llm_health_failures": 0,
        "llm_health_cooldown_remaining_sec": 0.0,
        "llm_health_last_error_type": "",
        "llm_health_last_error": "",
        "llm_health_failure_scope": "kind_only",
        "llm_budget_enabled": true,
        "llm_budget_allowed": true,
        "llm_budget_max_calls": 2,
        "llm_budget_used_calls": 1,
        "llm_budget_kind": "universal_intent",
        "llm_concurrency_allowed": true,
        "llm_concurrency_limit": 1,
        "llm_concurrency_wait_sec": 0.2,
        "llm_prompt_chars": 656,
        "llm_candidate_count": 3,
        "llm_compact_candidates_chars": 201,
        "llm_elapsed_ms": 351.59,
        "llm_response_chars": 39,
        "llm_done_reason": "stop",
        "llm_parsed": true
      },
      "intent_risk_flags": [
        "competing_domain_signals"
      ],
      "input_recovery": {
        "score": 0.3336,
        "language": "en",
        "language_quality": 0.6664,
        "should_review_intent": false,
        "reason": "English character n-gram quality=0.666",
        "action": "continue"
      },
      "llm_rejected_reason": "",
      "intent_candidates": [
        {
          "id": "c1",
          "domain": "game_controls",
          "operation": "control",
          "target": "",
          "confidence": 0.9,
          "reason": "heuristic fallback"
        },
        {
          "id": "c2",
          "domain": "games",
          "operation": "unknown",
          "target": "",
          "confidence": 0.97,
          "reason": "router category candidate"
        },
        {
          "id": "c3",
          "domain": "equipment",
          "operation": "how_to",
          "target": "",
          "confidence": 0.74,
          "reason": "domain keyword score=2"
        }
      ],
      "target": "",
      "filters": {},
      "needs": [],
      "answer_style": "direct_then_details",
      "heuristic": {
        "domain": "game_controls",
        "operation": "control",
        "confidence": 0.9,
        "reason": "domain_terms=2; control operation overrides domain; control terms found"
      }
    }
  }
]
```

**คำตอบก่อน**

The published equipment record does not specify the PS5 controller model.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

**คำตอบหลัง**

The published equipment record does not specify the PS5 controller model.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

## booking-button-not-controls-en — not_generic_controls

- คำถาม: `Where is the booking button?`
- ก่อน: ผิด contract / `pipeline:game_controls_target_unconfirmed_en`
- หลัง: ผ่าน / `pipeline:booking_navigation`
- เงื่อนไขตรวจหลัง: http_success=True, not_generic_controls=True, booking_not_game=True
- Trace ก่อนที่บันทึกจริง (คะแนนเป็นคะแนนของขั้นนั้น ไม่ใช่ความน่าจะเป็นว่าตอบถูก):

```json
[
  {
    "stage": "universal_intent",
    "decision": "game_controls/control",
    "confidence": 0.9,
    "detail": "candidate_intent:c3 controller/button phrase",
    "metadata": {
      "method": "llm",
      "llm_attempted": true,
      "llm_first": true,
      "llm_first_skip_reason": "",
      "llm_first_review_reason": "forced bounded intent review for broad English structured response",
      "llm_call": {
        "llm_kind": "universal_intent",
        "llm_model": "scb10x/typhoon2.5-qwen3-4b",
        "llm_timeout_sec": 14.0,
        "llm_configured_timeout_sec": 14.0,
        "llm_num_predict": 18,
        "llm_num_ctx": 1536,
        "llm_cache_hit": false,
        "global_timeout_enabled": true,
        "global_timeout_sec": 18.35,
        "global_elapsed_sec": 2.6812,
        "global_remaining_sec": 15.6687,
        "finalizer_reserve_sec": 1.0,
        "work_remaining_sec": 14.6687,
        "timing_status": "running",
        "llm_health_enabled": true,
        "llm_health_allowed": true,
        "llm_health_status": "ok",
        "llm_health_kind": "universal_intent",
        "llm_health_model": "scb10x/typhoon2.5-qwen3-4b",
        "llm_health_failures": 0,
        "llm_health_cooldown_remaining_sec": 0.0,
        "llm_health_last_error_type": "",
        "llm_health_last_error": "",
        "llm_health_failure_scope": "kind_only",
        "llm_budget_enabled": true,
        "llm_budget_allowed": true,
        "llm_budget_max_calls": 2,
        "llm_budget_used_calls": 1,
        "llm_budget_kind": "universal_intent",
        "llm_concurrency_allowed": true,
        "llm_concurrency_limit": 1,
        "llm_concurrency_wait_sec": 0.2,
        "llm_prompt_chars": 701,
        "llm_candidate_count": 4,
        "llm_compact_candidates_chars": 270,
        "llm_elapsed_ms": 349.18,
        "llm_response_chars": 39,
        "llm_done_reason": "stop",
        "llm_parsed": true
      },
      "intent_risk_flags": [],
      "input_recovery": {
        "score": 0.2978,
        "language": "en",
        "language_quality": 0.7022,
        "should_review_intent": false,
        "reason": "English character n-gram quality=0.702",
        "action": "continue"
      },
      "llm_rejected_reason": "",
      "intent_candidates": [
        {
          "id": "c1",
          "domain": "games",
          "operation": "unknown",
          "target": "",
          "confidence": 0.45,
          "reason": "heuristic fallback"
        },
        {
          "id": "c2",
          "domain": "reservation",
          "operation": "unknown",
          "target": "",
          "confidence": 0.74,
          "reason": "domain keyword score=2"
        },
        {
          "id": "c3",
          "domain": "game_controls",
          "operation": "control",
          "target": "",
          "confidence": 0.88,
          "reason": "controller/button phrase"
        },
        {
          "id": "c4",
          "domain": "equipment",
          "operation": "how_to",
          "target": "",
          "confidence": 0.72,
          "reason": "controller equipment phrase"
        }
      ],
      "target": "",
      "filters": {},
      "needs": [],
      "answer_style": "direct_then_details",
      "heuristic": {
        "domain": "games",
        "operation": "unknown",
        "confidence": 0.45,
        "reason": "domain_terms=2; no clear operation terms"
      }
    }
  }
]
```

**คำตอบก่อน**

I could not identify a verified game title with matching control information for this request. Please confirm the spelling and exact game edition.
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

**คำตอบหลัง**

Open the studio booking page using the link below. I cannot confirm the current button position on that page.
Booking page: https://esports.computing.psu.ac.th/reservation

## equipment-damage-th — not_generic_controls

- คำถาม: `คีย์บอร์ดพังต้องทำยังไง`
- ก่อน: ผ่าน / `pipeline:penalty_fast_path`
- หลัง: ผ่าน / `pipeline:penalty_fast_path`
- เงื่อนไขตรวจหลัง: http_success=True, not_generic_controls=True
- Trace ก่อนที่บันทึกจริง (คะแนนเป็นคะแนนของขั้นนั้น ไม่ใช่ความน่าจะเป็นว่าตอบถูก):

```json
[
  {
    "stage": "universal_intent",
    "decision": "penalty/rule_lookup",
    "confidence": 0.9,
    "detail": "candidate_intent:c1 heuristic fallback",
    "metadata": {
      "method": "llm",
      "llm_attempted": true,
      "llm_first": true,
      "llm_first_skip_reason": "",
      "llm_first_review_reason": "",
      "llm_call": {
        "llm_kind": "universal_intent",
        "llm_model": "scb10x/typhoon2.5-qwen3-4b",
        "llm_timeout_sec": 14.0,
        "llm_configured_timeout_sec": 14.0,
        "llm_num_predict": 18,
        "llm_num_ctx": 1536,
        "llm_cache_hit": false,
        "global_timeout_enabled": true,
        "global_timeout_sec": 18.35,
        "global_elapsed_sec": 0.1353,
        "global_remaining_sec": 18.2146,
        "finalizer_reserve_sec": 1.0,
        "work_remaining_sec": 17.2146,
        "timing_status": "running",
        "llm_health_enabled": true,
        "llm_health_allowed": true,
        "llm_health_status": "ok",
        "llm_health_kind": "universal_intent",
        "llm_health_model": "scb10x/typhoon2.5-qwen3-4b",
        "llm_health_failures": 0,
        "llm_health_cooldown_remaining_sec": 0.0,
        "llm_health_last_error_type": "",
        "llm_health_last_error": "",
        "llm_health_failure_scope": "kind_only",
        "llm_budget_enabled": true,
        "llm_budget_allowed": true,
        "llm_budget_max_calls": 2,
        "llm_budget_used_calls": 1,
        "llm_budget_kind": "universal_intent",
        "llm_concurrency_allowed": true,
        "llm_concurrency_limit": 1,
        "llm_concurrency_wait_sec": 0.2,
        "llm_prompt_chars": 634,
        "llm_candidate_count": 3,
        "llm_compact_candidates_chars": 205,
        "llm_elapsed_ms": 321.73,
        "llm_response_chars": 39,
        "llm_done_reason": "stop",
        "llm_parsed": true
      },
      "intent_risk_flags": [
        "competing_domain_signals"
      ],
      "input_recovery": {
        "score": 0.1421,
        "language": "th",
        "language_quality": 0.8579,
        "should_review_intent": false,
        "reason": "Thai character n-gram quality=0.858",
        "action": "continue"
      },
      "llm_rejected_reason": "",
      "intent_candidates": [
        {
          "id": "c1",
          "domain": "penalty",
          "operation": "rule_lookup",
          "target": "",
          "confidence": 0.9,
          "reason": "heuristic fallback"
        },
        {
          "id": "c2",
          "domain": "equipment",
          "operation": "rule_lookup",
          "target": "",
          "confidence": 0.66,
          "reason": "domain keyword score=1"
        },
        {
          "id": "c3",
          "domain": "penalty",
          "operation": "how_to",
          "target": "",
          "confidence": 0.66,
          "reason": "operation keyword score=1"
        }
      ],
      "target": "",
      "filters": {},
      "needs": [],
      "answer_style": "direct",
      "heuristic": {
        "domain": "penalty",
        "operation": "rule_lookup",
        "confidence": 0.9,
        "reason": "domain_terms=3; rules/penalty route overrides price/control ambiguity; how-to terms found; policy lookup forced by rules/penalty route"
      }
    }
  }
]
```

**คำตอบก่อน**

ต้องรับผิดชอบค่าปรับ/ค่าซ่อมครับ หากทำเมาส์หรืออุปกรณ์ของศูนย์เสียหาย โดยข้อมูลกฎที่มีระบุว่า ความเสียหายเล็กน้อยคิด 100-500 บาท และความเสียหายปานกลางคิด 500-2,000 บาทหรือตามราคาซ่อมจริง หากเสียหายร้ายแรงอาจต้องชดเชยเต็มจำนวนตามราคากลาง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

**คำตอบหลัง**

ต้องรับผิดชอบค่าปรับ/ค่าซ่อมครับ หากทำเมาส์หรืออุปกรณ์ของศูนย์เสียหาย โดยข้อมูลกฎที่มีระบุว่า ความเสียหายเล็กน้อยคิด 100-500 บาท และความเสียหายปานกลางคิด 500-2,000 บาทหรือตามราคาซ่อมจริง หากเสียหายร้ายแรงอาจต้องชดเชยเต็มจำนวนตามราคากลาง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

## explicit-reject-th — not_generic_controls

- คำถาม: `ไม่เอาปุ่ม ขอราคาของ PC`
- ก่อน: ผิด contract / `pipeline:protected_price_missing_service`
- หลัง: ผ่าน / `pipeline:structured_service_fee_conversation`
- เงื่อนไขตรวจหลัง: http_success=True, not_generic_controls=True, price_selected_pc=True
- Trace ก่อนที่บันทึกจริง (คะแนนเป็นคะแนนของขั้นนั้น ไม่ใช่ความน่าจะเป็นว่าตอบถูก):

```json
[
  {
    "stage": "conversation_request",
    "decision": "new_task",
    "confidence": 1.0,
    "detail": "typed slots preserve user filters; assistant options are not selections",
    "metadata": {
      "request_plan": {
        "schema_version": 1,
        "original_query": "ไม่เอาปุ่ม ขอราคาของ PC",
        "resolved_query": "ค่าบริการ ",
        "act": "new_task",
        "tasks": [
          {
            "task_id": "fee-1",
            "domain": "service_fee",
            "operation": "price_lookup",
            "targets": [],
            "scope": {
              "entity_selection": "unresolved",
              "detail_level": "package_rates"
            },
            "filters": {
              "customer_scope": "unspecified",
              "customer_group_ids": [],
              "duration_minutes": null,
              "people_count": null
            },
            "per_target_filters": {},
            "excluded_targets": [
              "pc"
            ],
            "pending_slots": [
              "service"
            ],
            "offered_option_ids": [
              "pc",
              "ps5",
              "nintendo_switch",
              "cockpit",
              "vr"
            ],
            "provenance": {
              "operation": "explicit_user",
              "targets": "unresolved",
              "filters": "explicit_user"
            }
          }
        ],
        "context_used": false,
        "needs_review": false
      },
      "outcome": "clarification_required"
    }
  }
]
```

**คำตอบก่อน**

ต้องการราคาของ PC, PlayStation 5, Nintendo Switch, Cockpit หรือ VR ครับ? เลือกเครื่องเดียวหรือทุกบริการได้ครับ

**คำตอบหลัง**

ราคาค่าบริการตามแพ็กเกจที่บันทึกไว้:

PC — 60 นาที/แพ็กเกจ (1 คน)
•    นักศึกษา/นักเรียน/บุคลากร PSU (PSU Student and Staff): 0 บาท/แพ็กเกจ
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 25 บาท/แพ็กเกจ
•    บุคคลทั่วไป (General Adult): 70 บาท/แพ็กเกจ
ราคา PC อ้างอิงข้อมูลปรับปรุงในระบบวันที่ 2026-07-27
แหล่งข้อมูล: local://service_fee/pc_price_update_20260727

