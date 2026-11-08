# PSU Esports Chatbot Model Benchmark Report

- Generated at: 2026-09-27T00:54:34
- Case bank: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\eval\model_benchmark_1500.jsonl`
- Runs: 1

## Overall Ranking

| Rank | Run | Model | Pass rate | Avg score | Avg sec | P95 sec | Max sec | LLM calls |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | llm_scb10x_typhoon2.5-qwen3-4b | scb10x/typhoon2.5-qwen3-4b | 90.0% | 97.55 | 1.9362 | 8.0217 | 12.5421 | 14 |

## Group Breakdown

### llm_scb10x_typhoon2.5-qwen3-4b (scb10x/typhoon2.5-qwen3-4b)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 1 | 100.0% | 100.0 | 0.0869 | 0.0869 |
| ambiguous_controls | 1 | 100.0% | 100.0 | 2.7788 | 2.7788 |
| availability_game | 4 | 100.0% | 100.0 | 0.6038 | 0.7118 |
| availability_machine_split | 1 | 100.0% | 100.0 | 0.3422 | 0.3422 |
| availability_service | 1 | 100.0% | 100.0 | 0.2899 | 0.2899 |
| competition_rules | 1 | 100.0% | 100.0 | 0.5908 | 0.5908 |
| compound | 2 | 100.0% | 100.0 | 0.693 | 0.7143 |
| equipment | 1 | 100.0% | 100.0 | 5.398 | 5.398 |
| game_controls | 8 | 87.5% | 98.5 | 0.5969 | 0.8718 |
| game_detail | 1 | 100.0% | 100.0 | 0.5827 | 0.5827 |
| games | 3 | 66.67% | 88.67 | 5.0697 | 8.0217 |
| general_llm | 6 | 66.67% | 91.33 | 6.0137 | 12.5421 |
| members | 1 | 100.0% | 100.0 | 0.2252 | 0.2252 |
| policy_schedule_rules | 1 | 100.0% | 100.0 | 0.3025 | 0.3025 |
| reservation | 1 | 100.0% | 100.0 | 0.2618 | 0.2618 |
| schedule | 1 | 100.0% | 100.0 | 0.5099 | 0.5099 |
| service_fee | 6 | 100.0% | 100.0 | 1.0349 | 3.9854 |

Top errors:
- `missing_any:ขอบคุณ`: 2
- `category_mismatch:clarification`: 1
- `missing_any:The Last of Us Part I / Part II|วิธีเล่น|เล่นได้ที่`: 1
- `mode_mismatch:pipeline:structured_game_controls`: 1

## How To Read

- ค่าเริ่มต้นของ benchmark รันเฉพาะ model เพื่อไม่เสียเวลาทำ baseline ซ้ำ
- คะแนนเป็น heuristic judge สำหรับคัดปัญหาเร็ว ยังไม่ใช่ human approval สุดท้าย
- ดูตัวอย่างคำตอบละเอียดได้ใน `results.csv` และ `results.jsonl` ของแต่ละ run
