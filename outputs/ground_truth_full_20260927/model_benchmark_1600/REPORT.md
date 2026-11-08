# PSU Esports Chatbot Model Benchmark Report

- Generated at: 2026-09-27T01:00:58
- Case bank: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\eval\model_benchmark_1500.jsonl`
- Runs: 1

## Overall Ranking

| Rank | Run | Model | Pass rate | Avg score | Avg sec | P95 sec | Max sec | LLM calls |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | no_llm | No-LLM | 80.88% | 96.1 | 0.6806 | 1.1443 | 11.8452 | 0 |

## Group Breakdown

### no_llm (No-LLM)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 24 | 100.0% | 100.0 | 0.2497 | 1.105 |
| ambiguous_controls | 6 | 100.0% | 100.0 | 0.244 | 0.58 |
| availability_game | 166 | 95.78% | 98.89 | 0.5492 | 0.7864 |
| availability_machine_split | 4 | 100.0% | 100.0 | 0.3327 | 0.3678 |
| availability_service | 23 | 91.3% | 98.61 | 0.4866 | 0.937 |
| competition_rules | 75 | 80.0% | 95.2 | 0.4933 | 1.2426 |
| compound | 89 | 100.0% | 100.0 | 1.046 | 1.5684 |
| equipment | 58 | 98.28% | 99.69 | 0.4063 | 0.5446 |
| game_controls | 345 | 93.91% | 98.02 | 0.5702 | 0.8905 |
| game_detail | 18 | 83.33% | 94.33 | 0.4759 | 0.7807 |
| games | 158 | 94.94% | 98.33 | 0.6765 | 1.0831 |
| general_llm | 275 | 10.18% | 83.43 | 1.2817 | 9.7684 |
| members | 63 | 100.0% | 100.0 | 0.2839 | 0.4146 |
| policy_schedule_rules | 8 | 87.5% | 98.0 | 0.2916 | 0.4735 |
| reservation | 20 | 100.0% | 100.0 | 0.4979 | 0.7278 |
| schedule | 10 | 100.0% | 100.0 | 0.3186 | 0.4117 |
| service_fee | 258 | 99.61% | 99.88 | 0.4889 | 0.6094 |

Top errors:
- `category_mismatch:clarification`: 34
- `missing_any:latency|หน่วง`: 28
- `missing_any:เฟรม|ความละเอียด`: 28
- `missing_any:API|เชื่อมต่อ`: 28
- `missing_any:ขอบคุณ`: 28
- `missing_any:จอง`: 27
- `missing_any:กิจกรรม`: 27
- `missing_any:คีย์บอร์ด|mechanical`: 27

## How To Read

- `No-LLM` คือ baseline ที่ปิด Local LLM และจะรันเฉพาะเมื่อระบุ `--include-no-llm`
- case ที่เป็น `general_llm` ตั้งใจให้ No-LLM decline ได้ แต่ model run ควรตอบได้
- ค่าเริ่มต้นของ benchmark รันเฉพาะ model เพื่อไม่เสียเวลาทำ baseline ซ้ำ
- คะแนนเป็น heuristic judge สำหรับคัดปัญหาเร็ว ยังไม่ใช่ human approval สุดท้าย
- ดูตัวอย่างคำตอบละเอียดได้ใน `results.csv` และ `results.jsonl` ของแต่ละ run
