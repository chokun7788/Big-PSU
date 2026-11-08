# R66 — รายการแก้ไขและข้อจำกัดครบหมวด

อ่านคู่กับ Flow, raw failures และ release audit; “มีวิธีแก้และมี test” ไม่เท่ากับ “ทุกคำถามถูกต้อง”

## 1. Execution และ ownership

**สาเหตุ:** retrieve_curated ใช้ guard/state ไม่ครบ และกรองหลังจำกัดจำนวน ทำให้ทั้ง crash และตกหล่นได้

**สิ่งที่ทำ:** ย้าย guard_hits ไปก่อน limit และใช้รายการที่ผ่าน guard จริง ไม่กลืน NameError

**หลักฐานการเปลี่ยน:** [retrieval.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r66_common_repair_20261014/system/app/pipeline/retrieval.py)

**การตรวจ:** ตรวจ exceptions/validation แยก; common sample และ withdrawal fixtures

**ขอบเขตที่ยังเหลือ:** ยังไม่ใช่การพิสูจน์ทุก branch ของ legacy; ไม่ได้รัน legacy arm

## 2. การชนของ target

**สาเหตุ:** ชื่อเกม ชุดปุ่ม บริการ และ FAQ ใช้ข้อความร่วมกัน; longest alias เพียงอย่างเดียวเลือกชนิดผิด

**สิ่งที่ทำ:** เลือก operation ก่อน แล้วค้นบทบาทที่เกี่ยวข้องจากชื่อ source อีกรอบ ตาม game_id เฉพาะเจตนาที่ควรตาม; all ของ control_set ยังเป็น control_set

**หลักฐานการเปลี่ยน:** [query_scope.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r66_common_repair_20261014/system/app/knowledge/common/query_scope.py)

**การตรวจ:** new-record 24 หมวด; genre, identity, ราคา PC games; ถอน rate แล้วไม่ crash

**ขอบเขตที่ยังเหลือ:** fuzzy ที่ไม่ชัดยังต้องถาม ไม่เปลี่ยนเป็นเดา

## 3. Field กับความหมายคำถาม

**สาเหตุ:** JSON ผ่าน schema ไม่ได้พิสูจน์ว่าเลือกช่องตรงคำถาม; What is the price เคยร้องขอ summary ด้วย

**สิ่งที่ทำ:** typed needs และ clause coverage มาก่อน proposal; ไม่รับ unverified intent; What is summary ใช้เฉพาะ identity frame; เพิ่มคำระดับชนิดข้อมูล usage/role/specs

**หลักฐานการเปลี่ยน:** [planner.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r66_common_repair_20261014/system/app/knowledge/common/planner.py)

**การตรวจ:** negative metadata/field tests และ versioned contracts

**ขอบเขตที่ยังเหลือ:** paraphrase ที่ยังไม่มีหลักฐานจับคู่ยัง abstain/clarify; ไม่มีหลักประกันทุกประโยค

## 4. LLM เลือกผิดเอกสาร

**สาเหตุ:** How much is it เคยถูกโยงกับค่าปรับ; parent/Nintendo ไปตารางราคา; schema indices ถูกแต่เจตนาผิด

**สิ่งที่ทำ:** ราคาไม่มี target ไม่ให้ entity selector สุ่มเลือก FAQ; ตรวจ topic overlap กับ question/title แยกจาก body; rejected selection ไม่ทำให้ transport circuit เสีย

**หลักฐานการเปลี่ยน:** [entity_search.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r66_common_repair_20261014/system/app/knowledge/common/entity_search.py)

**การตรวจ:** negative topic alignment; real model trace แยก schema กับ final plan

**ขอบเขตที่ยังเหลือ:** topic overlap เป็น safeguard ไม่ใช่ NLI หรือ semantic correctness oracle

## 5. กติกาการแข่งขัน

**สาเหตุ:** facet เดียวกลบอีกคำถาม และเอกสารยาวกลบข้อเฉพาะ; 1-1 ถูกตัดออกจากคำค้น

**สิ่งที่ทำ:** union facets/clauses, source-only fallback, term ที่เป็นอัตราส่วน, source order/dependencies และ map-list หลังหัวข้อที่พิสูจน์ได้

**หลักฐานการเปลี่ยน:** [query_scope.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r66_common_repair_20261014/system/app/knowledge/common/query_scope.py)

**การตรวจ:** CS2 roster+food, protests, map pool/veto; Tekken tie; VALORANT macros+food

**ขอบเขตที่ยังเหลือ:** lexical fallback ระบุ semantic_verified=false; ยังต้องตรวจคำตอบที่ไม่ผ่าน content contracts ใน audit

## 6. ปุ่มและแพลตฟอร์ม

**สาเหตุ:** bindings unknown ทั้งก้อนแม้ limitations มีปุ่ม; PC ถูก strip; PS5 กับ PlayStation / PS5 ไม่เท่ากัน

**สิ่งที่ทำ:** อ่าน partial representation ที่ lossless และมี note/provenance; ไม่แต่ง gesture; platform จาก raw query และ equivalence เฉพาะหมายเลขเดียวกัน; filter ปุ่ม/action

**หลักฐานการเปลี่ยน:** [answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r66_common_repair_20261014/system/app/knowledge/common/answer.py)

**การตรวจ:** R3 vutton, Mario A, PC preset, ไม่ยืม PS4 จาก PS5, unknown gestures

**ขอบเขตที่ยังเหลือ:** เวอร์ชันเกม/preset/context ที่ source ไม่ระบุยัง unknown

## 7. รายการเกมที่ให้เล่น

**สาเหตุ:** มีข้อมูลการแข่งขันไม่ได้แปลว่าศูนย์มีเกมนั้น; metadata 48 รายการไม่ใช่ offered catalog

**สิ่งที่ทำ:** ใช้ offered game_service ที่เชื่อม service/resource/zone จริง และแยก game-supported platform จาก venue offering

**หลักฐานการเปลี่ยน:** [query_scope.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r66_common_repair_20261014/system/app/knowledge/common/query_scope.py)

**การตรวจ:** PC 6, PS5 17, ทั้งศูนย์ 42 ตาม source ชุดนี้

**ขอบเขตที่ยังเหลือ:** การติดตั้งรายเครื่องที่ไม่มี installed_resource_ids ยังไม่ควรอ้างว่ามีหรือไม่มีแน่นอน

## 8. อุปกรณ์และสเปก

**สาเหตุ:** equipment_model ไม่ถูกตามจากบริการ; note ที่มีสเปกจริงไม่ได้อ่าน

**สิ่งที่ทำ:** ตาม declared graph และ exact source zone metadata ของ migration; นำ note เดิมเข้า specifications แบบ source-bound

**หลักฐานการเปลี่ยน:** [relations.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r66_common_repair_20261014/system/app/knowledge/common/relations.py)

**การตรวจ:** PC i5-14400 / DDR5 32GB / RTX 5060 8GB, zone ของ monitor, usage

**ขอบเขตที่ยังเหลือ:** ไม่มีการเดา model/resource FK จากชื่อคล้าย

## 9. ราคา PC ที่ตกหล่น

**สาเหตุ:** R63 ไม่มี PC rates แต่ระบบเก่ามี user-confirmed local update 2026-07-27; การบอกไม่มีข้อมูลทั้งระบบไม่ถูก

**สิ่งที่ทำ:** กู้ 0/25/70 บาทต่อ 60 นาทีจาก calculator และ source_registry เป็น 6 draft rates สำหรับ PC booking options 2 ชุด; แนบ source SHA

**หลักฐานการเปลี่ยน:** [PC_SOURCE_RECOVERY.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r66_common_repair_20261014/PC_SOURCE_RECOVERY.json)

**การตรวจ:** source-bound price tests และ snapshot migration

**ขอบเขตที่ยังเหลือ:** วันที่ได้รับ/อัปเดตไม่เท่ากับวันมีผล; คง validity unknown และ publication blocked

## 10. การคำนวณราคา

**สาเหตุ:** schema fixed/linear เดิมอธิบาย ceil-session ไม่ครบ และ reader แสดงแค่ฐานราคา

**สิ่งที่ทำ:** เพิ่ม session_ceil แบบ additive, คำนวณด้วยจำนวนรอบเต็มตาม source algorithm, ไม่คูณจำนวนคนหรือปัดเศษเงินที่ไม่มีสูตร

**หลักฐานการเปลี่ยน:** [billing.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r66_common_repair_20261014/system/app/knowledge/common/billing.py)

**การตรวจ:** 1/30/59/60/61/90/120/121/180 นาที, TH/EN, ฟรี, party, missing rule, expired

**ขอบเขตที่ยังเหลือ:** การคำนวณอัตราที่บันทึกไม่ยืนยัน current applicability หรือว่าจองเวลาเหล่านั้นได้

## 11. ราคาอื่นและอายุข้อมูล

**สาเหตุ:** GT บางชุดคาดราคาเก่าหลัง 31 มีนาคม; บางระบบเคยคูณราคาจากแถวหมดอายุ

**สิ่งที่ทำ:** ยืนยัน validity แบบ [from,until), แสดงบริการ/กลุ่มและเหตุผลหมดอายุ ไม่เปลี่ยนวันให้ผ่าน GT; ราคาไม่ทราบวันมีผลเป็น partial

**หลักฐานการเปลี่ยน:** [answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r66_common_repair_20261014/system/app/knowledge/common/answer.py)

**การตรวจ:** expired rates ไม่คืนยอดปัจจุบัน, current-source-date tests

**ขอบเขตที่ยังเหลือ:** ต้องมีอัตราฉบับปัจจุบัน/วันมีผลจากเจ้าของ

## 12. เหมาและงบ

**สาเหตุ:** ครึ่งวัน/เต็มวันปน hourly; งบถูกเข้าใจว่ามีเครื่องว่าง

**สิ่งที่ทำ:** แยก period/zone/audience, สูตร known เท่านั้น; แสดงตัวเลือกราคาโดยไม่อ้าง availability; ฟรีไม่หารศูนย์หรือสรุปเล่นไม่จำกัด

**หลักฐานการเปลี่ยน:** [budget.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r66_common_repair_20261014/system/app/knowledge/common/budget.py)

**การตรวจ:** rental periods, group/unknown rate/free bounds

**ขอบเขตที่ยังเหลือ:** ไม่มี source ระยะเวลา/ภาษี/ส่วนลด ห้ามแต่ง 4/8 ชั่วโมงหรือยอดเพิ่ม

## 13. ตารางและวันพิเศษ

**สาเหตุ:** area hours กับ bookable ไม่เหมือนกัน; closure อนาคตอาจถูก now กรอง; optional FK เก่าทำให้ fact อื่นหาย

**สิ่งที่ทำ:** bookable 09–12/13–16 ตาม source เดิม; 12–13 ไม่เปิดจองตามผู้ใช้; closure ตาม query date; effective ตาม required path

**หลักฐานการเปลี่ยน:** [answer.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r66_common_repair_20261014/system/app/knowledge/common/answer.py)

**การตรวจ:** 33 provider/calendar support tests ทั้ง flags; Monday/Friday/Maintenance/TH/EN

**ขอบเขตที่ยังเหลือ:** เวลาเปิดพื้นที่ที่ source ขัดกันยังไม่เลือกนโยบายเอง

## 14. สถานะจองและ live binding

**สาเหตุ:** transport success ไม่เท่ากับ occupancy truth; ข้อมูลหมวดบริการไม่ใช่สถานะเครื่อง

**สิ่งที่ทำ:** คง existing live adapter; common live intent defer รวม English bare device; oracle แยก HTTP/freshness/count/date/hash และ VR occupancy

**หลักฐานการเปลี่ยน:** [query_scope.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r66_common_repair_20261014/system/app/knowledge/common/query_scope.py)

**การตรวจ:** saved booking oracle, available-only, provider failures; ไม่ใช่ real booking oracle ใหม่

**ขอบเขตที่ยังเหลือ:** ผู้ใช้ยืนยันสถานะจริงเดิมแล้ว; new arbitrary provider/live_binding ยังไม่มี operational coverage เพียงเพราะอ่าน metadata ได้

## 15. บทสนทนาและ all

**สาเหตุ:** bare PC/เกม/ราคา/ทั้งหมด ทำ scope หายหรือสืบหัวข้อเก่ามาผิด

**สิ่งที่ทำ:** typed state เก็บ record/scope/operation/fields/platform และ resolve ใหม่เมื่อเปลี่ยนเรื่อง; all ไม่ขยายเป็น internal metadata โดยอัตโนมัติ

**หลักฐานการเปลี่ยน:** [dialogue.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r66_common_repair_20261014/system/app/knowledge/common/dialogue.py)

**การตรวจ:** 12 sessions / 24 turns ทั้ง flags; PS5→games, game→price, booking summary

**ขอบเขตที่ยังเหลือ:** multi-user capacity ไม่ได้พิสูจน์ด้วย single-session correctness tests

## 16. หลายคำขอและหน่วยของข้อจำกัด

**สาเหตุ:** games กับราคาไม่ split; 3 sessions ต่อการจองถูกตีความเป็นต่อวันได้

**สิ่งที่ทำ:** bounded operation composition รวมกับ/และ, remap citations, partial ต่อ clause; max-session source แยก per-booking กับ daily unknown

**หลักฐานการเปลี่ยน:** [composition.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r66_common_repair_20261014/system/app/knowledge/common/composition.py)

**การตรวจ:** PC ราคา+จอง+หลักฐาน, PS5 games+ราคา, daily-limit counterexample

**ขอบเขตที่ยังเหลือ:** เงื่อนไขเพิ่มที่ยังไม่ตีความจะระบุเป็น partial ไม่ถือว่าตอบครบ

## 17. พิมพ์ผิดและคำปกติ

**สาเหตุ:** ชื่อผิดต้องกู้ แต่ valid word/ตัวเลขต้องไม่ถูกบิดเป็นชื่อเกม

**สิ่งที่ทำ:** bounded edits/keyboard context/unique margin, รักษาตัวเลข; token boundary สำหรับ fuzzy Latin; schema language lexicon ไม่เพิ่มชื่อรายเคส

**หลักฐานการเปลี่ยน:** [name_candidates.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r66_common_repair_20261014/system/app/knowledge/common/name_candidates.py)

**การตรวจ:** cockpik, R3 vutton, edition numeric protection, cooperative ไม่เป็น Overcooked

**ขอบเขตที่ยังเหลือ:** ยังไม่อ้างว่ารองรับ noise ทุกระดับหรือทุกภาษา

## 18. แปลและ proper names

**สาเหตุ:** ตัวเลขตรงแต่ความหมายผิด เช่น gum→checkers, starting money→prize pool, Treasurer→Priest; JSON ซ้อนใน prose

**สิ่งที่ทำ:** แปลเป็น draft, validate literals/JSON/prohibitions/exceptions, source-bound manual repairs; review person roles และเก็บชื่อไทยหากไม่มี English spelling ที่ยืนยัน

**หลักฐานการเปลี่ยน:** [translation.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r66_common_repair_20261014/system/app/knowledge/common/translation.py)

**การตรวจ:** 791 ช่องเดิมที่เคยว่างมี proposals; reviewed repairs + person-source tests; original English ไม่ถูกปลอมว่า owner-reviewed

**ขอบเขตที่ยังเหลือ:** การตรวจอัตโนมัติไม่พิสูจน์ semantics ทุกช่อง; official romanization และ current roster ไม่เดา

## 19. เว็บ/lock/ประสิทธิภาพ

**สาเหตุ:** ส่ง HTTP response แล้วแต่ยังถือ session lock ขณะ save delivery; next turn ได้ 409; fuzzy scan ซ้ำแพง

**สิ่งที่ทำ:** ปล่อย session lock หลัง response และ state commit ก่อน bookkeeping; acknowledgement ไม่ถูก downgrading; cache normalization + similarity upper bounds

**หลักฐานการเปลี่ยน:** [server.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r66_common_repair_20261014/system/app/web_api/server.py)

**การตรวจ:** actual HTTP normal + delay delivery 350 ms ทั้ง flags; code/data frozen; timing ต่อ mode แยก

**ขอบเขตที่ยังเหลือ:** ไม่ได้เป็น load test หรือ SLA; ไม่ลด guard เพื่อเพิ่ม throughput

## 20. การประเมินและส่งใช้

**สาเหตุ:** strict score ปน protocol/content/source IDs/latency; draft ถูกเรียก approved; test exit 0 ทั้งที่ assertions fail

**สิ่งที่ทำ:** เก็บ raw graders และ classify ใหม่แยก; provenance จาก exact original document/chunk; draft/demo labels; code+DB snapshots; native known-contract mismatches ยังรายงาน; backup/hash compare ก่อน copy code

**หลักฐานการเปลี่ยน:** [evidence.py](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r66_common_repair_20261014/system/app/knowledge/common/evidence.py)

**การตรวจ:** paired old common results จาก SQLite ไม่รัน legacy; 24-kind fixtures; deployment hashes

**ขอบเขตที่ยังเหลือ:** strict pass ไม่ใช่ semantic accuracy; 223 เป็น sampling ของ 36 corpora ไม่ใช่ full 20,554

## จุดที่พบจากการตรวจคำตอบจริงหลังรายการหลัก

- Source gaps: ที่อยู่, damage/payment/booking-required, equipment family, platform-equivalent rates และ installation รายเครื่อง ตาม [FLOW_E_RESIDUAL_SOURCE_GAPS_TH.md](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r66_common_repair_20261014/FLOW_E_RESIDUAL_SOURCE_GAPS_TH.md)
- New scoped data: FAQ/policy/procedure, shared resource และ typed preconditions ตาม [FLOW_F_SCOPED_NEW_DATA_TH.md](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r66_common_repair_20261014/FLOW_F_SCOPED_NEW_DATA_TH.md)
- Audience semantics: Thai/EN ตามชื่อกลุ่ม source, ไม่ infer คนนอกเป็นผู้ใหญ่, ไม่ให้กลุ่ม Alumni ที่มีคำว่า Student ถูกคิดเป็น PSU staff; unknown age/take-home policy ระบุขาดข้อใด ตาม [FLOW_G_AUDIENCE_AND_POLICY_GAPS_TH.md](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r66_common_repair_20261014/FLOW_G_AUDIENCE_AND_POLICY_GAPS_TH.md)
- Validation regressions: policy priority ต้องอยู่หลัง competition context; exact FAQ ต้องแยก generic question tail; typed address ไม่ให้ model แย่งไป FAQ contact ตาม [FLOW_H_VALIDATION_REGRESSIONS_TH.md](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r66_common_repair_20261014/FLOW_H_VALIDATION_REGRESSIONS_TH.md)
- Translation: indestructible มีต้นฉบับ EN เทียบ, Kata Noi→Kathu เทียบ Thai, เครื่อง→machine มิใช่ flight และศูนย์→studio มิใช่ zero; เป็น draft revisions เก็บต้นฉบับ ไม่ได้ owner approve

## Follow-up และ preview state ที่พบเพิ่ม

[FLOW_I_PRICE_FOLLOWUP_TH.md](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r66_common_repair_20261014/FLOW_I_PRICE_FOLLOWUP_TH.md) อธิบายการแยก scope/กลุ่ม/ระยะเวลาจากราคาคำตอบเดิม เปลี่ยนกลุ่มแล้วอ่าน rate ใหม่ และใช้ backend common_read_state ใน Owner preview; ทดสอบ actual HTTP ไทย/อังกฤษ ไม่ใช้เพียงการตรวจรูป JSON

## การจัดลำดับ intent และตรวจคำแปลตกหล่น

[FLOW_K_INTENT_PRIORITY_TH.md](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r66_common_repair_20261014/FLOW_K_INTENT_PRIORITY_TH.md) แยกค่าปรับจากค่าบริการ การยกเลิกเองจากการถูกยกเลิกเพราะไม่จ่าย และ live availability จาก installed games; 10 tests ต่อ flag

[FLOW_L_TRANSLATION_COMPLETENESS_TH.md](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r66_common_repair_20261014/FLOW_L_TRANSLATION_COMPLETENESS_TH.md) กู้ช่วงค่าปรับอังกฤษจากต้นฉบับไทยและ existing English natural FAQ เป็น revision ใหม่ เก็บ source/revision เดิมครบ ตรวจพบ 36 control records / 390 note rows ที่ EN ว่าง: adapter กู้ข้อความไทยพร้อม Translation pending และ partial status เฉพาะแถวที่ตอบ ไม่อ้างว่าแปลครบ

ขณะตรวจพบ What does A do ยังไม่เข้า controls แม้ระบุเกม จึงเพิ่มกรอบไวยากรณ์ของปุ่มอย่างมีขอบเขต ไม่ใช้ what does ทุกคำเป็น controls; FAQ caption ไม่แสดง regex .* ของข้อมูลย้ายเดิม การแก้ไม่เปลี่ยนชื่อเกมหรือ source strings

## สถานะหลังลูป M/N

English notes 390 แถวเติมและ agent source-review แล้ว มี 64 semantic revisions เพิ่มจาก model proposals; fallback ภาษาไทยใช้เพื่อความเข้ากันได้กับข้อมูลเก่าที่แปลไม่ครบ มิใช่งานค้าง 390 แถวใน candidate ล่าสุด ดู [CONTROL_NOTE_AGENT_REVIEW.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r66_common_repair_20261014/CONTROL_NOTE_AGENT_REVIEW.json) และ [FLOW_N_SELECTOR_LATENCY_TH.md](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r66_common_repair_20261014/FLOW_N_SELECTOR_LATENCY_TH.md)
