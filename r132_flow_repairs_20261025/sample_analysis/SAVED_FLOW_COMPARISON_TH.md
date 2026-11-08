# ผลวัดหลังแก้R132 — ชุดเดิม10%

ครบ 2111keys / 5584grade identities; เทียบsaved gradesโดยไม่run/regradebaselineใหม่

**รุ่นติดตั้งคือR134 ซึ่งแก้เพิ่มหลังfreezeR132** ผลนี้ยังไม่ใช่fresh executionของR134 ต้องตรวจpaired replayและsource regressionsต่อก่อนปิดงาน

| แขน | requested locale | strictผ่าน/ทั้งหมด | positive literalผ่าน/eligible | unassessed |
|---|---|---:|---:|---:|
| R64_saved | auto | 236/364 | 200/247 | 13 |
| R64_saved | en | 2252/2728 | 951/994 | 0 |
| R64_saved | th | 1809/2492 | 1274/1315 | 3 |
| R95_saved | auto | 51/364 | 177/247 | 0 |
| R95_saved | en | 287/2728 | 696/994 | 0 |
| R95_saved | th | 225/2492 | 998/1315 | 0 |
| R130_saved | auto | 47/364 | 165/247 | 0 |
| R130_saved | en | 92/2728 | 752/994 | 0 |
| R130_saved | th | 24/2492 | 1041/1315 | 0 |
| R131_repeat_saved | auto | 46/364 | 165/247 | 0 |
| R131_repeat_saved | en | 95/2728 | 752/994 | 0 |
| R131_repeat_saved | th | 23/2492 | 1041/1315 | 0 |
| R132_post_fix | auto | 26/364 | 173/247 | 0 |
| R132_post_fix | en | 48/2728 | 759/994 | 0 |
| R132_post_fix | th | 19/2492 | 1087/1315 | 0 |

คำตอบเปลี่ยนจากsavedR130 750keys ไม่ถือchanged=improved ต้องsource review แยกactual contentจากprotocol/keyword/first-line/complete-clause/validity/source gaps/model transport

คง76requirements/14หมวด; C07sampleเพียง1จากประชากร6 และC14ไม่มีnewsจริง ไม่อ้าง100%semantic ไม่อ้างcausalFloweffectจากsavedR64/R95ที่source/backend/precision/clock/deadlineต่างกัน

Model profile/adapter/messages/schema/stage/precision audit: MODEL_AUDIT.json; เวลามีภาระเครื่องร่วมและปิดdebug APIsระหว่างรัน

R134ติดตั้งแล้วตามINSTALLATION_RECEIPT.json ไม่ควรรายงานcandidateยังไม่ติดตั้งทับR78อีก ตัวเปิดเดิมส่งต่อbundleใหม่และเก็บsystem/dataR78เดิมครบ

หมายเหตุแก้ metadata การติดตั้ง 26Oct: ตรวจ INSTALLATION_RECEIPT ของ R134 และ PID/commandline ของ installed chat/editor แล้ว รุ่นติดตั้งปัจจุบันคือ R134; R135 ยังเป็น working candidate ไม่มี fresh score ของ R134/R135 ในรายงานนี้ ข้อความรุ่นติดตั้งเดิมจาก analyzer เก็บใน SAVED_FLOW_COMPARISON_TH.original_generated.md ไม่รัน analyzer/inference/regrade หรือแก้ raw grades เพื่อการแก้เอกสารครั้งนี้
