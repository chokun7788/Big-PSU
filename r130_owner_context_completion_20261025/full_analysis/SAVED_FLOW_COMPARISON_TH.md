# เทียบ saved Flow เดิม / R95 / R130 ด้วยตัวหารเดียวกัน

ใช้ request keys และ grade identities เดียวกัน ไม่รันคำถาม baseline ใหม่ แบ่งภาษาโดย requested locale จาก frozen workload ทุกแขน ข้อมูล clock/backend/deadline ต่างรุ่น จึงไม่ใช่ causal effect ของ Flow อย่างเดียว

| แขน | ภาษา request | Strict ผ่าน/ทั้งหมด | Strict % | Literal ผ่าน/มีเกณฑ์ | ยังประเมิน literal ไม่ได้ |
|---|---|---:|---:|---:|---:|
| R64_legacy_llm | auto | 2189/3392 | 64.53 | 1882/2301 | 111 |
| R64_legacy_llm | en | 22699/27319 | 83.09 | 9083/9466 | 9 |
| R64_legacy_llm | th | 17713/25100 | 70.57 | 12547/13142 | 74 |
| R95_common_llm | auto | 465/3392 | 13.71 | 1639/2301 | 0 |
| R95_common_llm | en | 2473/27319 | 9.05 | 6721/9466 | 0 |
| R95_common_llm | th | 2092/25100 | 8.33 | 9923/13142 | 0 |
| R130_common_llm | auto | 445/3392 | 13.12 | 1615/2301 | 0 |
| R130_common_llm | en | 802/27319 | 2.94 | 7176/9466 | 0 |
| R130_common_llm | th | 231/25100 | 0.92 | 10259/13142 | 0 |

Positive literal เป็นชุดเกณฑ์ข้อความที่กำหนดจาก input ก่อนดูผล ไม่ใช่ semantic accuracy กรณี execution/grader ไม่สามารถประเมินได้แสดงไว้ในคอลัมน์แยก ไม่ตัดออกจนทำให้คะแนนดูดีขึ้น รายงานคำตรงตัวที่ประเมินได้กับตัวหารทั้งหมดแยกอยู่ใน JSON

การเปลี่ยน route/intent/source-ID หรือ first-line wording ต้องแยกจากความถูกต้องของข้อเท็จจริง กรณีตัดสิน semantic ไม่ได้คง review_required

## การตีความหลังตรวจsource

รวมR130strict1,478/55,811=2.65%; fixedpositive literal19,050/24,909=76.48% R95literal18,283/24,909=73.40%; R64literal23,512/24,909=94.39%และunassessed194คงในตัวหาร ค่าทั้งหมดไม่ใช่semanticansweraccuracy

literalR130ดีกว่าR95ไทย+336/อังกฤษ+455/auto−24checks รวม+767 แต่pairedR95-only2,630/R130-only3,397 ไม่ใช่ดีขึ้นทุกเคส strictR95-only3,761/R130-only209

R130ใช้retainedR121contextweightsหลังnewไม่ผ่านcriticalsource review ส่วนselector/genericเป็นbase บนHFNF4BF16ที่รับformatเพื่อเก็บhashแต่ไม่ได้constrainoutput ต่างจากOllama/GGUFของbaseline ข้อมูลsource/translation/currentvalidity/calendar/clock/deadline/admissionต่างรุ่น จึงไม่อ้างcausalFloweffectและไม่เรียกretainedwire0ว่าlegacyansweraccuracy0

ROOT_CAUSE_REVIEW_TH.mdแยกsource-confirmed content/scope/omissionจากroute/keyword/firstline/completeclause/validity/sourcegaps/transport โดยไม่regradebaselineใหม่
