# R82 automated local LLM + chat check

```json
{
  "started_utc": "2026-10-17T07:48:11.242355+00:00",
  "completed": false,
  "llm_enabled_verified": false,
  "real_model_generation_verified": false,
  "full_test": false,
  "production_data_modified": false,
  "settings_modified": false,
  "model_downloaded": false,
  "network_bypass_attempted": false,
  "obstacle": {
    "type": "StopCheck",
    "message": "Socket permission denied (10013). No alternate connection path or privilege change was attempted. Open this runner from ordinary Windows."
  },
  "count": 0,
  "expected_count": 14,
  "passed": 0,
  "database_unchanged": true,
  "by_language": {
    "th": {
      "count": 0,
      "passed": 0
    },
    "en": {
      "count": 0,
      "passed": 0
    }
  },
  "chat_selector": {
    "actual_calls_attempted": 0,
    "calls_with_valid_schema": 0,
    "failures": []
  },
  "all_answer_contracts_passed": false,
  "all_attempted_selector_calls_returned_valid_schema": false
}
```

Answer contracts, direct model generation and model selector calls are separate results. The model was explicitly warmed before chat timings. A valid schema is not independent proof of semantic accuracy. No full corpus was run.
