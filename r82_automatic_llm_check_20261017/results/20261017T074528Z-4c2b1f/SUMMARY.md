# R82 automated local LLM + chat check

```json
{
  "started_utc": "2026-10-17T07:45:28.972916+00:00",
  "completed": true,
  "llm_enabled_verified": true,
  "real_model_generation_verified": true,
  "full_test": false,
  "production_data_modified": false,
  "settings_modified": false,
  "model_downloaded": false,
  "network_bypass_attempted": false,
  "ready_probe_exact": true,
  "ready_probe_seconds": 39.812,
  "count": 14,
  "expected_count": 14,
  "passed": 14,
  "database_unchanged": true,
  "by_language": {
    "th": {
      "count": 6,
      "passed": 6
    },
    "en": {
      "count": 8,
      "passed": 8
    }
  },
  "chat_selector": {
    "actual_calls_attempted": 3,
    "calls_with_valid_schema": 1,
    "failures": [
      {
        "case": "th-personal",
        "question": "ผมเอาอุปกรณ์อินพุตส่วนตัวมาใช้ได้ไหม",
        "failure": "timeout"
      },
      {
        "case": "th-reject",
        "question": "ผมเอาอุปกรณ์อินพุตส่วนตัวมาใช้ได้ไหม",
        "failure": "timeout"
      }
    ]
  },
  "all_answer_contracts_passed": true,
  "all_attempted_selector_calls_returned_valid_schema": false
}
```

Answer contracts, direct model generation and model selector calls are separate results. The model was explicitly warmed before chat timings. A valid schema is not independent proof of semantic accuracy. No full corpus was run.
