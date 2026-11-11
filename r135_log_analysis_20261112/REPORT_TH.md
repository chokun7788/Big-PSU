# รายงานวิเคราะห์ผลลัพธ์และปัญหาจาก log ที่บันทึกไว้ทั้งหมดในขอบเขตรอบนี้

วันที่จัดทำ: 12 พฤศจิกายน 2026 (Asia/Bangkok)

## 1. ข้อสรุปที่หลักฐานรองรับ

ระบบมีทั้งปัญหาที่ตอบไม่ได้จริง ปัญหาการแยกงาน/ตรวจความครบ ปัญหาข้อความกำกวม และข้อจำกัดของข้อมูลต้นทาง ไม่ใช่เพียงไม่มีลิงก์อ้างอิง ส่วนการแก้ล่าสุดพิสูจน์ว่าบางกลุ่มดีขึ้น แต่ยังไม่มีผลชุดใหญ่ของโค้ดล่าสุดที่ใช้รับรองภาพรวม

**ข้อแลกเปลี่ยนที่พบจริงเมื่อจับคู่ 200 คำถามเดียวกัน:** Hybrid10 เดิม unavailable 22/200 → Bounded35/200 → Verified36/200 ขณะที่เวลารวมคำขอลดจาก4,158.454sเป็น370.948s จึงมีทั้งความเร็วที่ดีขึ้นและความพร้อมตอบที่แย่ลงในผลวัดย้อนหลังชุดนี้ ไม่ใช่ดีขึ้นทุกด้าน และยังแยกผลของเวลา/source/backendออกจากตัวFlowทั้งหมดไม่ได้

อ่านผลที่เซฟไว้ 5 รอบ รวม **4,623 แถวคำตอบ** และ matched assistant traces ของรอบ 10% กับ 200 สองรอบรวม **2,511 แถว** แบบ SQLite read-only พร้อมหลักฐาน focused รอบ02 อีก 27 คำถาม source-only และ 21 คำขอ HTTP การนับแถวข้ามรอบมีคำถามซ้ำ จึงห้ามเรียกว่า 4,623 คำถามไม่ซ้ำหรือความแม่นยำของรุ่นล่าสุด

การตรวจทุกแถวเป็นการอ่านและจัดกลุ่มด้วยสคริปต์ ไม่ใช่การรับรองความหมายโดยมนุษย์ทุกแถว ส่วนตัวอย่างที่อ่านเชิงคุณภาพระบุแยกด้านล่าง ไม่มีการเรียกโมเดล รันทดสอบใหม่ ให้คะแนน literal ใหม่ หรือแก้ข้อมูลจริง/ผล frozen

ขอบเขต “ทั้งหมด”: ทั้งหมดของไฟล์ RESULTS.jsonl ทั้งห้ารอบที่ระบุใน INPUT_MANIFEST.json พร้อม trace และ focused evidence ที่ระบุ ไม่รวมทุกแชตส่วนตัว ทุกไฟล์สำรอง ทุกการทดลองในประวัติโครงการ และไม่ได้รับประกันว่าพบ bug ทุกตัว

## 2. ปริมาณงาน สถานะ และเวลาของแต่ละรุ่น
| รุ่น | แถว / unique keys | HTTP 200 | common_unavailable | partial | median / p95 / max (วินาที) | >60s |
|---|---|---|---|---|---|---|
| R135 5% เดิม (7 พ.ย.) | 1056 / 1056 | 1056 | 197 | 393 | 1.040 / 57.800 / 121.359 | 47 |
| Hybrid48 5% (8 พ.ย.) | 1056 / 1056 | 1056 | 198 | 414 | 1.394 / 62.720 / 119.451 | 65 |
| Hybrid 10% (10–11 พ.ย.) | 2111 / 2111 | 2111 | 324 | 835 | 1.263 / 91.944 / 2859.009 | 362 |
| Bounded 200 | 200 / 200 | 200 | 35 | 89 | 1.072 / 6.953 / 17.108 | 0 |
| Verified-source 200 | 200 / 200 | 200 | 36 | 87 | 0.922 / 5.895 / 15.242 | 0 |

Hybrid48 5% มี `common_live_unavailable` อีก 1 ข้อ แยกจาก `common_unavailable` 198 ข้อ จึงมี 199 ข้อที่ชื่อ mode มี unavailable รวมกัน ห้ามสลับตัวหารโดยไม่ระบุ

ทุกชุดไม่มี key ซ้ำภายในไฟล์ และไม่มี outer `timed_out=true` ตาม response ที่บันทึก แต่ไม่ได้แปลว่าไม่มี timeout ภายในโมเดลหรือไม่เกินงบเวลาที่ตั้งไว้

### คะแนน literal ที่เซฟไว้ (ไม่คำนวณใหม่)

| รุ่น | matched | not matched | ไม่มีเกณฑ์ literal รองรับ | ไฟล์คะแนน |
|---|---|---|---|---|
| R135 5% เดิม (7 พ.ย.) | 1002 | 253 | 1527 | r135_eval5_20261107\SCORES_LITERAL.json |
| Hybrid48 5% (8 พ.ย.) | 988 | 267 | 1527 | r135_hybrid48_20261108\evaluation\SCORES_LITERAL.json |
| Hybrid 10% (10–11 พ.ย.) | 1946 | 541 | 3097 | r135_hybrid_eval10_20261110\evaluation\SCORES_LITERAL.json |
| Bounded 200 | 202 | 53 | 250 | r135_bounded_eval200_20261111\evaluation\SCORES_COMPARISON.json |
| Verified-source 200 | 196 | 59 | 250 | r135_verified_eval200_20261111\evaluation\SCORES_COMPARISON.json |

สำหรับ 10%: matched 1,946 / 2,487 supported grade identities (78.25% ของเกณฑ์ข้อความที่รองรับ), not matched 541, unsupported 3,097; มี 1,242/2,111 คำถามไม่มีเกณฑ์ literal รองรับเลย เทียบ R134 ที่บันทึกไว้ 2,008/2,487: ผ่านทั้งคู่ 1,882, เฉพาะรุ่นใหม่ 64, เฉพาะเก่า 126, ไม่ผ่านทั้งคู่ 415 ตัวเลขนี้ไม่ใช่ semantic accuracy และ 541 ไม่ใช่จำนวนคำตอบผิดทางความหมาย

## 3. เปรียบเทียบเฉพาะ 200 keys เดียวกัน

| รุ่น / subset | จำนวน | unavailable | partial | รวมเวลาคำขอ (s) | median / max (s) | >60s |
|---|---|---|---|---|---|---|
| Hybrid 10% (10–11 พ.ย.) | 200 | 22 | 96 | 4158.454 | 1.223 / 151.475 | 27 |
| Bounded 200 | 200 | 35 | 89 | 436.970 | 1.072 / 17.108 | 0 |
| Verified-source 200 | 200 | 36 | 87 | 370.948 | 0.922 / 15.242 | 0 |

ทั้งสามชุดจับคู่ได้ครบ 200 keys เวลารวมข้างบนเป็นผลรวม elapsed ของคำขอ ไม่รวม preflight/ช่วงว่างทั้งหมด รอบ verified เคยรายงานทั้งรอบ 384 วินาที ขณะที่ผลรวมคำขอ 370.948 วินาที จึงไม่ขัดกัน เปรียบเทียบนี้ยังมีความต่างของข้อมูล เวลาและสถานะ backend; ไม่สรุปว่าแพตช์ทำให้เวลาหรือคะแนนเปลี่ยนทั้งหมด

Literal ที่บันทึกบน 200 ชุดนี้: Hybrid10 subset 203/255 → bounded 202/255 → verified 196/255; R134 197/255 ส่วนต่าง bounded→verified มีเพียง 2 คำถาม: 5 grade identities รอ `3 sessions` แต่เว็บที่ตรวจตอนแก้ระบุ 6 และอีก 1 ของ Shifter ไป unavailable ไม่แก้เกณฑ์หรือบวกคะแนนกลับเอง ส่วน net1 identity ระหว่าง Hybrid10 subset→bounded ยังไม่มี per-criterion paired-difference file ที่อ่านได้ในขอบเขตนี้ จึงไม่อ้างว่าแจกแจง semantic cause ของส่วนต่างทั้งหมดครบแล้ว

เทียบ Hybrid10→Verified: มี 15 คำถามที่เดิมไม่ใช่ common_unavailable แล้วกลายเป็น unavailable และ 1 คำถามที่ฟื้นจาก unavailable เป็นสถานะอื่น ทั้งนี้การฟื้นเป็น partial/unconfirmed ยังไม่ใช่การตอบครบ

| คำถามที่กลายเป็น unavailable | สถานะเดิม | เวลาเดิม→ใหม่ (s) |
|---|---|---|
| What can you use a PlayStation 5 Slim with Ultra HD Blu-ray Disc Drive for | pipeline:common_partial_answer | 96.621 → 1.093 |
| In The Legend of Zelda: Breath of the Wild, what button do you press to shrink | pipeline:common_unconfirmed | 14.966 → 5.785 |
| Whete can VALORANT be plaed | pipeline:common_partial_answer | 44.625 → 0.888 |
| Driving Force Shifter อยู่ซนไหน | pipeline:common_answer | 27.884 → 0.914 |
| ตามกติกกาการแข่่งขัน CS2 เปลี่ยนสมาชิกทีมหลังเริ่มรายการได้หรือไม่ | pipeline:common_partial_answer | 96.086 → 1.419 |
| Where can you play Monster Hunter Rise? | pipeline:common_partial_answer | 28.072 → 0.777 |
| Please answer from verified studio information: What is the studio policy for monday play | pipeline:common_unconfirmed | 35.333 → 5.866 |
| Does the PC Zone have gaming monitors? I need the official answer. | pipeline:common_partial_answer | 52.068 → 0.961 |
| ช่วยตอบจากข้อมูลทียืนยันได้หน่อย: Gaming Keyboard อยู่โซนไกน | pipeline:common_partial_answer | 91.759 → 5.895 |
| อธิบายคำว่า latency ในระบบคอมพิวเตอร์แบบสั้น ๆ ตอบเป็นภาษาไทย | pipeline:common_unconfirmed | 50.525 → 0.751 |
| In God of War Ragnarök, what button is used for movement? | pipeline:common_unconfirmed | 17.841 → 0.753 |
| Where can you play Horizon Call of the Mountain | pipeline:common_partial_answer | 33.787 → 1.074 |
| ขอข้อมูลเรื่องวันศุกร์ ตรวจอุปกรณ์ | pipeline:common_partial_answer | 99.342 → 5.951 |
| How do you use the controller in Resident Evil Village | pipeline:common_unconfirmed | 23.528 → 5.774 |
| ขอสอบถามหน่อยครับ นักศึกษา PSU เฃ่น VR 30 นาที เสียกี่บท | pipeline:common_partial_answer | 73.833 → 5.879 |

## 4. “ไม่มีข้อมูลยืนยัน” ต้องแยกเป็นหลายชนิด

| สถานะ | ความหมายที่ควรใช้ | ห้ามสรุป |
|---|---|---|
| unavailable | กระบวนการตีโจทย์/ตรวจหลักฐานยังไม่พร้อมในคำขอนั้น | ต้นทางไม่มีข้อมูล หรือโมเดลล่มทุกครั้ง |
| partial | บางส่วนมีข้อมูล แต่ความครบ/เงื่อนไข/ช่วงมีผลยังไม่ยืนยัน | คำตอบทุกบรรทัดผิด |
| unconfirmed / not_current | ยังยืนยันขอบเขต ปัจจุบัน หรือ live state ไม่ได้ | ไม่มี URL อย่างเดียว |
| clarification | ต้องการข้อมูลเพิ่มหรือความหมายกำกวม | ระบบเสียทุกกรณี |
| HTTP 200 | ส่ง response กลับได้ | เนื้อหาถูกต้อง |
| ไม่มี public URL | sources ที่ส่งออกไม่มี URL สาธารณะ | ไม่มี internal claims/receipts เสมอไป |

### ข้อมูลอ้างอิงที่ส่งออก

| รุ่น | ไม่มี public URL ใน response.sources | มี public URL | หมายเหตุ |
|---|---|---|---|
| R135 5% เดิม (7 พ.ย.) | 1011 | 45 | ตรวจช่อง sources เท่านั้น; ไม่รวม URL ในคำตอบ/ข้อมูลวันหยุด |
| Hybrid48 5% (8 พ.ย.) | 1014 | 42 | ตรวจช่อง sources เท่านั้น; ไม่รวม URL ในคำตอบ/ข้อมูลวันหยุด |
| Hybrid 10% (10–11 พ.ย.) | 2033 | 78 | ตรวจช่อง sources เท่านั้น; ไม่รวม URL ในคำตอบ/ข้อมูลวันหยุด |
| Bounded 200 | 195 | 5 | ตรวจช่อง sources เท่านั้น; ไม่รวม URL ในคำตอบ/ข้อมูลวันหยุด |
| Verified-source 200 | 168 | 32 | ตรวจช่อง sources เท่านั้น; ไม่รวม URL ในคำตอบ/ข้อมูลวันหยุด |

หลังแก้เว็บใน 200 เดียวกัน จำนวนไม่มี URL ใน sources ลดจาก 195 เป็น 168 แต่ไม่ได้ทำให้ unavailable หายไป (35→36) จึงมีหลักฐานชัดว่าการเติมลิงก์อย่างเดียวไม่แก้ทุกปัญหา ลิงก์หน้าเว็บ, หลักฐานภายใน, สิทธิ์เผยแพร่, ช่วงมีผล และการรองรับสิ่งที่ถาม เป็นคนละข้อกำหนด

## 5. สิ่งที่พบจาก model receipts และ flow traces

| รุ่น / ขอบเขต | จำนวน | มี event admission_denied | บันทึก timeout โดยตรง | gateway ส่งสำเร็จอย่างน้อยครั้งหนึ่ง | gateway ล้มอย่างน้อยครั้งหนึ่ง |
|---|---|---|---|---|---|
| Hybrid 10% (10–11 พ.ย.) / all | 2111 | 0 | 400 | 464 | 400 |
| Hybrid 10% (10–11 พ.ย.) / unavailable | 324 | 0 | 321 | 93 | 321 |
| Bounded 200 / all | 200 | 57 | 17 | 9 | 17 |
| Bounded 200 / unavailable | 35 | 28 | 12 | 0 | 12 |
| Verified-source 200 / all | 200 | 60 | 17 | 8 | 17 |
| Verified-source 200 / unavailable | 36 | 30 | 14 | 0 | 14 |

จำนวนต่อแถวซ้อนกันได้: คำขอเดียวอาจเรียกสำเร็จครั้งหนึ่งแล้วล้มอีกครั้ง หรือถูกปฏิเสธ stage หนึ่งและ timeout อีก stage หนึ่ง Event admission_denied เป็นหลักฐานว่าตัว app ไม่ส่ง stage นั้นต่อ ไม่ใช่หลักฐานว่าถูกระบบอนุมัติของ Codex ปฏิเสธ และยังไม่ระบุว่ามาจาก cooldown/concurrency/health เฉพาะเหตุใดหากไม่มีรายละเอียดเพิ่ม

### ตรวจ receipt ชั้น admission เพิ่มแล้ว

| รุ่น | คำขอที่ถูกdenied | health statusจากreceipt | ในunavailable |
|---|---|---|---|
| Bounded 200 | 57 | {'cooldown': 57} | {'cooldown': 28} |
| Verified-source 200 | 60 | {'cooldown': 60} | {'cooldown': 30} |

receiptระบุ circuit breaker cooldown active, failure_scope=kind_only, last_error_type=TimeoutError และ http_attempted=false เช่น Monster Hunter Rise ใช้จอยยังไง: evidence_selection ถูกปฏิเสธด้วยcooldownเหลือ86.34วินาทีหลังfailure2ครั้ง **เป็น health gate ของแอป local ไม่ใช่ permission block ของ Codex** ไม่ควรปิดguardทั้งชุดเพื่อให้เรียกได้ ควรตรวจdeadline/cooldown recovery, half-open probesแบบจำกัด และทางตอบข้อมูลที่ทำด้วยโค้ดได้

ใน36unavailableของverified200: timeoutอย่างเดียว6, admission-deniedอย่างเดียว22, มีทั้งสองอย่าง8 รวม36 ข้อมูลนี้อธิบายสิ่งที่เกิดในคำขอได้ชัดขึ้น แต่ยังไม่พิสูจน์ว่าโมเดลล่มถาวรหรือทุกข้อจะตอบถูกหากเรียกโมเดลสำเร็จ

### Reason codes: มีไว้ชี้ทาง ไม่ใช่ข้อสรุปสาเหตุ

**Hybrid 10% (10–11 พ.ย.) — ทุกสถานะคำตอบ**

| reason ที่บันทึก | จำนวนคำขอที่พบ (ซ้อนกันได้) |
|---|---|
| no_accepted_replacement_task | 2068 |
| independent_request_or_constraint_coverage_unresolved | 1005 |
| source_operation_projection_present | 879 |
| unrecognised_factual_predicate | 545 |
| discourse_prefix | 494 |
| canonical_competition_scope | 362 |
| requested_need_not_source_verified | 354 |
| compatibility_scope_not_migrated | 327 |
| model_transport_failure | 324 |
| invalid_task_graph | 314 |
| bounded_compatibility_requested_operation_unverified | 270 |
| typed_requested_fields | 256 |
| independent_context_frame | 234 |
| bounded_compatibility_operation_not_independently_verified | 228 |
| request_constraint_application_unverified | 208 |
| no_supported_task | 194 |
| clause_semantics_needed | 178 |
| canonical_named_game_control_predicate | 172 |

**Verified-source 200 — ทุกสถานะคำตอบ**

| reason ที่บันทึก | จำนวนคำขอที่พบ (ซ้อนกันได้) |
|---|---|
| no_accepted_replacement_task | 195 |
| independent_request_or_constraint_coverage_unresolved | 99 |
| source_operation_projection_present | 89 |
| meaning_transport_or_protocol_failure | 60 |
| unrecognised_factual_predicate | 49 |
| discourse_prefix | 38 |
| bounded_compatibility_requested_operation_unverified | 37 |
| compatibility_scope_not_migrated | 33 |
| model_transport_failure | 27 |
| independent_context_frame | 25 |
| typed_requested_fields | 24 |
| bounded_compatibility_operation_not_independently_verified | 23 |
| no_supported_task | 21 |
| request_constraint_application_unverified | 19 |
| requested_need_not_source_verified | 18 |
| canonical_named_game_control_predicate | 18 |
| r101_model_unavailable | 15 |
| store_or_snapshot_unavailable | 15 |

รายการนับใหม่ด้านบนตรวจทุกสถานะ ไม่ใช่เฉพาะ unavailable และข้าม snapshot/raw source fields เพื่อไม่เอาข้อมูลต้นทางมาปนกับ diagnostics จึงต้องไม่เทียบจำนวนตรง ๆ กับ UNAVAILABLE_TRACE_AUDIT เก่าซึ่งนับเฉพาะ324ข้อ เช่น no_accepted_replacement_task ปรากฏในคำตอบที่อ่านได้ด้วย จึงไม่ใช่ bug ทุกครั้ง

### First-stage labels ใน flow audit

| stage label | Hybrid10 จำนวนคำขอ | Verified200 จำนวนคำขอ |
|---|---|---|
| applicability_validity | 1 | 1 |
| evidence_insufficient | 274 | 29 |
| model_body_schema | 3 | 0 |
| model_queue_transport | 121 | 15 |
| processing_or_transport | 200 | 21 |
| rendering_or_source_undercoverage | 908 | 90 |
| state_binding | 104 | 6 |
| task_interpretation | 11 | 0 |

นี่เป็น attribution ที่ระบบเขียนเอง ไม่ใช่การพิสูจน์ว่า rendering เป็น root cause ตามจำนวนทั้งหมด ต้องอ่านคำถาม/คำตอบและ receipts ประกอบ

## 6. รายการปัญหาและข้อจำกัดพร้อมแนวทางแก้

| ID | ระดับ | ปัญหา | สถานะ | หลักฐาน | แนวทาง |
|---|---|---|---|---|---|
| LOG-01 | P1 | การรอโมเดลกินเวลาและงบไม่หยุดทุกเส้นทาง | พบจริงในรอบเก่า; hard deadline ยังไม่พิสูจน์ | Hybrid10 >60s362ข้อ; มี gateway timeout ตรง ๆ และ outlier2,859.009s | ใช้ monotonic request deadline ร่วม, cap connect/read/queue แต่ละ stage, จบด้วย verified partial, ตรวจ cancellation และ deadline telemetry |
| LOG-02 | P1 | model admission ถูกปฏิเสธแต่ข้อความแสดงเป็น transport/model unavailable | เปิด | verified200 พบ model_admission_denied ใน trace; บางข้อไม่มี gateway transport attempt | แยก not_attempted/admission/timeout/protocol/schema ให้ตรง; เก็บ health/cooldown/concurrency cause โดยไม่ retry วน |
| LOG-03 | P1 | คำถามชัดแต่ native predicate ไม่ครอบคลุมหรือคำผิดพาไปโมเดล | แก้บางกลุ่มแล้ว; ที่เหลือเปิด | Shifter อยู่ซนไหน, Gaming Keyboard อยู่โซนไกน, บุคคล/เกมหลายคำถามไปfallback | ใช้ source-bound vocabulary + bounded spelling candidates; รักษา raw/name/number/polarity; ambiguity ต้องถาม |
| LOG-04 | P1 | แยกงานเกิน/ซ้ำ แล้วแจ้งว่างานเดิมยังไม่ตอบ | แก้ boundary/occurrenceเฉพาะขอบเขต; ต้องตรวจ output ต่อ | PUBG genre ตอบแล้วแต่แจ้งไม่มีแผน; PS5 usage และวันจันทร์มีหัวข้อซ้ำ | ใช้ need IDs/raw spans ร่วม, reconcile completion กับ claims, deduplicateเฉพาะงานเดียวกัน ไม่รวมคนละบริการ |
| LOG-05 | P0 | ชื่อเกม/ภาค/แพลตฟอร์มถูกยืมข้ามเป้าหมาย | แก้ numeric family C04/C05 เฉพาะกรณีที่ตรวจ | TEKKEN9→8 ก่อนแก้; compatibilitydescriptionหลุดหลังแก้typedเพียงชั้นเดียว | ตรวจ source relation ที่ selector/receipt/final delivery; ไม่มี fallbackเลี่ยงguard; Roman/DLC/wordsequelsยังต้องตรวจ |
| LOG-06 | P0/P1 | คำผิดในกลุ่มผู้ใช้ทำให้แสดงราคาหลายกลุ่ม รวม0บาทที่ไม่ใช่คำตอบเฉพาะผู้ถาม | ต้องยืนยันสถานะปัจจุบัน; พบจริงใน frozen200 | นักศึกษาต่งามหาลัยNintendoส่ง6อัตรารวมPSU0บาท แม้ไม่ได้ฟันธงว่าฟรี | แยก audience unresolved จาก audience all; ถามยืนยันว่าเป็นนักศึกษาต่างสถาบันก่อนคำนวณ; ห้ามเลือกPSUจากคำว่านักศึกษาอย่างเดียว |
| LOG-07 | P0/P1 | ราคา/จำนวน/ระยะเวลา: คำตอบกับคำชี้แจงไม่สอดคล้อง | บางกลุ่มแก้แล้ว แต่ไม่ครอบคลุมหลายservice | PC30นาทีแสดง0บาทสำหรับ30นาทีแล้วแจ้งไม่ยืนยัน30นาที; PS5ถาม30แต่แสดง60พร้อมcaveat | ให้ proofผูก task/rate/rule/person/service ทุกบรรทัด; แยก rate display กับ payable total; รักษา normal positives |
| LOG-08 | P1 | ช่วงจำนวนคน/หน่วยเรียกเก็บยังคลุมเครือ | เปิดตามsourceบางรายการ | Nintendo/VR มีคนเป็นช่วง และ unitบางrateunknown; ยังไม่พิสูจน์การหารคนหรือราคาเหมารวม | รักษาช่วงคน, ถาม allocation, ไม่สร้างราคาต่อคนเอง; owner-confirmed billing unitเป็นข้อมูลที่ต้องเพิ่ม |
| LOG-09 | P1 | ตารางเปิดอาคาร/เล่น/จอง/สถานะว่างสดไม่ใช่เรื่องเดียวกัน | เปิดบางoperation; การระงับบางข้อสมเหตุผล | VR equipment ถูกตีเป็นlive availability; Cockpit14–15มีURLแต่mappingไม่ครบ | แยก operation/static inventory vs live occupancy, require date/time/resource IDs, cache statusแยกจากschedule |
| LOG-10 | P1 | ข้อมูล policy/personnel ยังไม่มีช่วงมีผลชัด | ข้อมูลยังไม่ครบ ไม่ใช่ไม่มีเว็บอย่างเดียว | หลายpartialแสดงบทบาท/กฎพร้อม validity caveat | เพิ่ม effective interval/approval/source authorityเมื่อเจ้าของยืนยัน; ไม่เดาวัน; จัดcaveatสั้นและตรงขอบเขต |
| LOG-11 | P1 | ข้อความต้นทางหลายฉบับซ้ำหรือscopeยังไม่ชัด | เปิด | เครื่องดื่มแสดง2sourceข้อความเหมือนกันพร้อมvariant warning | ผูก revision/scope/authorityก่อนยุบ; เท่ากันทางข้อความไม่พิสูจน์scopeเดียวกัน |
| LOG-12 | P1 | กติกาแข่งขันต้องผูก event/edition/clause และความครบ | เปิดบางส่วน | บางข้อส่งกฎงานหนึ่งพร้อมขอให้ยืนยันงาน; บางข้อtimeout evidence_selection | แยกถามตัวงานจากอ่านข้อกฎ, รองรับtargetedclause+dependency, อย่าใช้ชื่อเกมแทนตัวงาน |
| LOG-13 | P2 | ข้อความจากข้อมูลต้นทางไม่สะอาด | เปิด | อาหรับปนTEKKEN8และตัวอักษร literal\n ในCockpitusage | เพิ่มdata-qualityauditแยกจากsemanticguard; แก้ผ่านownerworkflow/สำเนาและเก็บrevision ไม่rewriteเงียบ ๆ |
| LOG-14 | P1/P2 | literalเกณฑ์เก่าทำให้คำตอบตามsourceใหม่ดูคะแนนลด | พบจริง; ต้องแยกจากbug | 5criteriaคาด3sessionsแต่เว็บที่ตรวจได้6; Shifterอีก1เป็นunavailableจริง | เก็บคะแนนเดิมและsource-alignedreviewคู่กัน; versiongoldsetและtimestamp ไม่เปลี่ยนตัวหารเพื่อทำคะแนน |
| LOG-15 | P1 | publiccitation, internalreceipt และsource applicabilityถูกเข้าใจเป็นเรื่องเดียว | เปิดบางเส้นทาง | verified200มีURLเพิ่มแต่unavailableไม่ลด; livebookingมีURLแต่ยืนยันสถานะไม่ได้ | แสดงsourceเมื่อexactpinsตรง, แยก noURL/noevidence/notcurrent/targetmismatch; URLไม่ใช่ใบอนุญาตให้claim |
| LOG-16 | P1 | การวัดยังไม่ครอบคลุมการใช้งานทั้งหมด | เปิด | 27focused/149checks/21HTTPไม่ใช่broadscoreใหม่; C07ใน200มีเพียง1ตัวอย่าง | เก็บheldoutไม่ใช้ฝึก, controlledsparsecategorytestsแยก, owner/editor lifecycleและattachmentsยังต้องผ่านgates |
| LOG-17 | P2 | logโตและdiagnosticซ้ำทำให้ตรวจยาก/ใช้พื้นที่มาก | พบจริง | transcriptsรอบ10%ประมาณ4.59GBสำหรับ2111คำขอ; response logประมาณ21.7MB | แยก compactrequestledgerจากartifact blobs/source snapshotsตามhash, retention/rotation, เก็บreceiptpointerครบก่อนลดข้อมูล |
| LOG-18 | P1 | ถามนอกขอบเขตอาจเสียเวลาเรียกmodelก่อนบอกขอบเขต | พบในตัวอย่าง; ยังไม่ใช่ทุกoutofscope | will it rain tomorrow15.242sและserver/client13.963sไปunavailable | ใช้boundedoutofscoperouteเมื่อหลักฐานชัด, ไม่เดาคำตอบสภาพอากาศ; ambiguityยังใช้budgetจำกัด |

ระดับ P0/P1 เป็นลำดับความสำคัญตามผลกระทบและความเสี่ยง ไม่ใช่คำยืนยันว่าคำตอบทุกข้อในกลุ่มผิด ปัญหาทางไฟล์/โฟลเดอร์ไม่พบหลักฐานว่าเป็นต้นเหตุโดยตรงของกรณีเหล่านี้: logsชี้ไปที่ field/target/relation/reader/budget ต้องไม่จัดโฟลเดอร์ใหม่แทนการแก้ binding

## 7. กรณีเวลาเกินงบที่ต้องไม่มองข้าม

| รุ่น | เกิน global limit ที่รายงาน | เกินแต่ timed_out=false |
|---|---|---|
| Hybrid 10% (10–11 พ.ย.) | 1 | 1 |
| Bounded 200 | 0 | 0 |
| Verified-source 200 | 0 | 0 |

กรณีช้าที่สุดใน frozen Hybrid10: `Please check: What do the RoV tournament ruls say about the competition format? please.` client 2,859.009s, response wall 2,858.9373s, configured global limit190s, deadline remaining0 แต่ timing_status=completed และ timed_out=false ตัวเลขทั้งฝั่งclientและserverสอดคล้องกัน จึงไม่ใช่แค่ผลรวมเวลารอบ แต่ยังไม่มีหลักฐานแยกว่าเกิดจาก blockingcall, processpause/เครื่องsleep หรือเส้นทางใด เพราะ request_context ของคำขอนี้ไม่มี gatewayevent การไม่มีeventไม่พิสูจน์ว่าไม่ได้เรียกผ่านทางอื่น

สรุปได้เพียงว่ารอบนั้นยังไม่บังคับเวลาหรือรายงานสถานะเกินงบได้ครบทุกเส้นทาง ส่วน bounded200/verified200เร็วขึ้นจริงตามelapsed แต่ยังเป็นการจำกัดแบบcooperative ไม่ใช่harddeadlineproof

## 8. ตัวอย่างที่อ่านคำถาม–คำตอบและตรวจความสอดคล้องจริง

การวิเคราะห์ด้านล่างเป็น intent/output review เฉพาะตัวอย่าง ไม่ใช่ source entailment acceptance ทั้งหมด และเป็นผลของรุ่นที่ระบุ ไม่ย้ายข้อผิด frozen ไปกล่าวหาว่ายังเกิดในโค้ดล่าสุดโดยไม่มีผลใหม่

### ตัวอย่าง 1 — ผู้ใช้ถามการถ่ายวิดีโอภายในสถานที่

- รุ่น: verified_200; key `c137296b97e3f28d83912421eda5acce608c6514b8195f85d8e786813498ac50`
- คำถาม: I am planning a visit and need to know: May I record video inside the studio?
- สถานะ/เวลา: `pipeline:common_partial_answer` / 1.066s
- คำตอบที่เซฟไว้:

> An in-game capture policy does not establish permission to film the premises or people. The recorded source scope is shown below.
> In-game screenshots and video capture are allowed; delete them when finished. This does not confirm filming people or the premises.
> The policy validity interval is unconfirmed. The recorded clause does not establish current permission.

**วิเคราะห์:** แยกin-gamecaptureจากถ่ายบุคคล/สถานที่ได้ การwithholdpermissionสมเหตุผลจากขอบเขตที่แสดง ไม่ควรเอากฎcaptureไปอนุญาตถ่ายสถานที่

**ควรแก้/รักษา:** คงscopeguard แต่ตอบข้อจำกัดก่อนและลดข้อความซ้ำ

### ตัวอย่าง 2 — ต้องการวิธีใช้อุปกรณ์PS5

- รุ่น: verified_200; key `227ea7ee0beee57012b2bda07a4b24210e9b09a4aa642ccb82be1f85f942a567`
- คำถาม: Could you please help me with this: How do I use the PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive
- สถานะ/เวลา: `pipeline:common_partial_answer` / 4.377s
- คำตอบที่เซฟไว้:

> **how do i use the playstation 5 slim with ultra hd blu-ray disc drive**
>
> **usage**: PlayStation 5 console gaming equipment for console gaming and as a base for selected VR Zones. Book PlayStation 5 Zone or VR Zone according to desired service, then play pre-set games on schedule. Play Marvel's Spider-Man 2. Play TEKKEN 8. Play Fortnite. Play God of War Ragnarok. Supports VR Zone using PlayStation VR2.
> **PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive**
>
> **how do i use the playstation 5 slim with ultra hd blu-ray disc drive**
>
> No confirmed source is available for the requested detail.

**วิเคราะห์:** มีusageแล้วแต่หัวข้อซ้ำและบอกไม่มีsourceสำหรับdetailอีกครั้ง ทำให้ไม่รู้ว่าตอบส่วนใดแล้ว

**ควรแก้/รักษา:** reconcile need IDs และบอกเฉพาะขั้นตอนที่sourceยังไม่มี

### ตัวอย่าง 3 — ต้องการรายการอุปกรณ์ที่มีในVRZone

- รุ่น: verified_200; key `70580dbafcf62f55cb7c3dd508c72043894bd70ae58807cdbf43df8452656075`
- คำถาม: Please tell me: What equipment is available in the VR Zone? Please use verified information
- สถานะ/เวลา: `pipeline:common_partial_answer` / 0.957s
- คำตอบที่เซฟไว้:

> **what equipment is available in the vr zone**
>
> Recorded equipment in the requested scope
> - PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive
> - Sony PlayStation VR2
>
> **what equipment is available in the vr zone**
>
> Please specify the item and requested time.

**วิเคราะห์:** ตอบรายการแล้วกลับขอเวลา อาจสับสนstaticinventoryกับliveavailability

**ควรแก้/รักษา:** ตรวจoperationก่อนบังคับtime slot

### ตัวอย่าง 4 — ถามแนวเกมPUBG

- รุ่น: verified_200; key `07c763b10d8997393a45bcdbaabfe93c079aacbd774f29f96caa3832a4629878`
- คำถาม: ขอสอบถามหน่อยครับ PUBG เป็นเกมแนวไหน
- สถานะ/เวลา: `pipeline:common_partial_answer` / 0.788s
- คำตอบที่เซฟไว้:

> **แนวเกม**: เกม Battle Royale
> **PUBG: BATTLEGROUNDS**
>
> ส่วนที่ยังไม่มีแผนประมวลผลที่ยืนยันได้: pubg เป็นเกมแนวไหน

**วิเคราะห์:** ตอบBattleRoyaleแล้วแจ้งส่วนเดิมยังไม่มีแผน เป็นcompletion/output inconsistency

**ควรแก้/รักษา:** ผูกcoverageกับneedและclaimที่ส่งจริง

### ตัวอย่าง 5 — ถามราคานักศึกษาPSUเล่นPC30นาที

- รุ่น: verified_200; key `7dc588121765be2792f3be6f8db0071b58ebb4009f4c925c6ee284b136b2d36f`
- คำถาม: นักศึกษา PSU เล่น PC 30 นาที เสียกี่บาท
- สถานะ/เวลา: `pipeline:common_partial_answer` / 1.161s
- คำตอบที่เซฟไว้:

> **PC #01-#02 / PSU Student and Staff**
> 0 บาท สำหรับ 30 นาที
> **PC #03-#10 / PSU Student and Staff**
> 0 บาท สำหรับ 30 นาที
> อัตราที่เจ้าของยืนยันล่าสุด ณ 2026-10-20 (ยังไม่ยืนยันวันเริ่ม–สิ้นสุดใหม่)
>
> ยังยืนยันการใช้เงื่อนไขต่อไปนี้ในคำตอบไม่ได้: 30 นาที

**วิเคราะห์:** แสดง0บาทสำหรับ30นาทีแล้วแจ้งยังไม่ยืนยัน30นาที ต้นเหตุที่ควรตรวจคือproofของหลายservice/renderer ไม่ใช่เติมURLอย่างเดียว

**ควรแก้/รักษา:** ให้rate/durationproofแต่ละserviceตรงกับข้อความและpartialstate

### ตัวอย่าง 6 — พิมพ์ผิดแต่สื่อว่านักศึกษาต่างมหาวิทยาลัยเล่นNintendo30นาที

- รุ่น: verified_200; key `9baf9105a9fb80b9173340cfca87b95d89e0f08f82071915601f60978af935af`
- คำถาม: ขอสอบถามหน่อยครับ นักศึกษาต่งามหาลัย เล่น Nintendo Switch 30 นาที เสียกี่บาท
- สถานะ/เวลา: `pipeline:common_partial_answer` / 1.089s
- คำตอบที่เซฟไว้:

> อัตราตามช่วงจำนวนคนในแหล่งข้อมูล: 1–2, 3–4 คน; คำนวณยอดรวมไม่ได้จนกว่าจะยืนยันการจัดคนและหน่วยเรียกเก็บ
> **Nintendo Switch (1-2 Persons) / PSU Student and Staff**
> 0 บาทต่อคน สำหรับ 60 นาที — 1–2 คนตามขอบเขตต้นทาง
> **Nintendo Switch (1-2 Persons) / PSU Alumni and General Student**
> 50 บาทต่อคน สำหรับ 60 นาที — 1–2 คนตามขอบเขตต้นทาง
> **Nintendo Switch (1-2 Persons) / General Adult**
> 140 บาทต่อคน สำหรับ 60 นาที — 1–2 คนตามขอบเขตต้นทาง
> **Nintendo Switch (1-4 Persons) / PSU Student and Staff**
> 0 บาทต่อคน สำหรับ 60 นาที — 3–4 คนตามขอบเขตต้นทาง
> **Nintendo Switch (1-4 Persons) / PSU Alumni and General Student**
> 100 บาทต่อคน สำหรับ 60 นาที — 3–4 คนตามขอบเขตต้นทาง
> **Nintendo Switch (1-4 Persons) / General Adult**
> 280 บาทต่อคน สำหรับ 60 นาที — 3–4 คนตามขอบเขตต้นทาง
> อัตราที่เจ้าของยืนยันล่าสุด ณ 2026-10-20 (ยังไม่ยืนยันวันเริ่ม–สิ้นสุดใหม่)
>
> ยังยืนยันการใช้เงื่อนไขต่อไปนี้ในคำตอบไม่ได้: 30 นาที

**วิเคราะห์:** ส่งราคา6รายการรวมPSU0บาท แม้เป็นalternative ไม่ฟันธงว่าฟรี แต่ไม่ตอบกลุ่มที่ตั้งใจและเสี่ยงสับสน

**ควรแก้/รักษา:** ถามยืนยันaudienceเมื่อไม่มั่นใจ;อย่ากลายเป็นall audiencesโดยปริยาย

### ตัวอย่าง 7 — ถามPS5นักศึกษาต่างมหาวิทยาลัย30นาที

- รุ่น: verified_200; key `ce48c51aaa345c0c35e3a80dcc74d0579d6b4070a68c404f49c498736d08c35c`
- คำถาม: How much does it xost for a student from another university to play PS5 for 30 minutes
- สถานะ/เวลา: `pipeline:common_partial_answer` / 1.047s
- คำตอบที่เซฟไว้:

> Source person ranges: 1–2 people; a total cannot be calculated until allocation and billing units are confirmed.
> **PlayStation 5 / PSU Alumni and General Student**
> 50 THB per person for 60 minutes — 1–2 people in the recorded source scope
> Rates last reaffirmed by the owner on 2026-10-20; no new effective interval was established.
>
> Application of these requested constraints remains unverified: 30 minutes

**วิเคราะห์:** ส่งอัตรา60นาทีและบอก30ยังยืนยันไม่ได้ แยกได้ว่าไม่ได้ตอบยอด30ครบ;ยังต้องถาม/พิสูจน์roundingrule

**ควรแก้/รักษา:** บอกก่อนว่านี่เป็นอัตราอ้างอิง60นาทีและยอดที่ถามยังไม่ยืนยัน

### ตัวอย่าง 8 — ถามCockpitบุคคลทั่วไป30นาที

- รุ่น: verified_200; key `99e58322f22105f7f5fc09134ef72b9d2355e0fb44b48cd67822e0b96e03c6f5`
- คำถาม: General adult plays cockpit for 30 minutes, how much does it cost?
- สถานะ/เวลา: `pipeline:common_answer` / 0.967s
- คำตอบที่เซฟไว้:

> **Cockpit / General Adult**
> 200 THB for 30 minutes
> Rates last reaffirmed by the owner on 2026-10-20; no new effective interval was established.

**วิเคราะห์:** ตอบ200THB;ตรวจfrozenrateพบ20000minor/60นาทีและsession_ceil จึงไม่สรุปว่า200ผิดจากการหารครึ่ง แต่ข้อความยังไม่อธิบายceilและunitยังunknownในrecord

**ควรแก้/รักษา:** แสดงกติกาคิดเต็มช่วงตามsourceและตรวจหน่วย/approvalก่อนclaimpayabletotal

### ตัวอย่าง 9 — ต้องการเครื่องCockpitที่ว่าง14–15

- รุ่น: verified_200; key `36c4c5f316fbaba1a03cb02d0543234b1606c4e8c6b70447ade02748425cd149`
- คำถาม: อยากรู้ว่า ช่วง 14:00-15:00 Cockpit Zone เครื่องไหนว่างบ้าง
- สถานะ/เวลา: `pipeline:common_unconfirmed` / 1.908s
- คำตอบที่เซฟไว้:

> ดึงข้อมูลระบบจองได้ แต่ข้อมูลช่วงเวลาหรือการจับคู่บริการยังยืนยันไม่ครบ จึงยังบอกว่าว่างหรือถูกจองไม่ได้ครับ
> แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
> ยังยืนยันไม่ได้: Cockpit #1 (1 Person), Cockpit #2 (1 Person)

**วิเคราะห์:** มีลิงก์จองจริงแต่mappingหรือwindowยังไม่ครบ จึงไม่สามารถสรุปfree/occupiedได้

**ควรแก้/รักษา:** ถามวันที่/จับresourceและwindowให้ครบ ไม่เดาว่างจากschedule

### ตัวอย่าง 10 — ถามวิธีจองและวันเปิดสองเรื่อง

- รุ่น: verified_200; key `91170922dba40c4c9335d6d2234009d4c587c393e5f863298778b1c1d068ea4d`
- คำถาม: Cockpit จองยังไง แล้วเปิดวันไหนบ้าง
- สถานะ/เวลา: `pipeline:common_partial_answer` / 1.138s
- คำตอบที่เซฟไว้:

> **cockpit จองยังไง**
>
> ขั้นตอนการจอง
> 1. เลือกบริการที่ต้องการ
> 2. เลือกวันและเวลา
> 3. กรอกข้อมูลผู้ใช้บริการ
> 4. ตรวจสอบข้อมูล
> 5. ชำระเงินโดยโอนเข้าบัญชีธนาคาร
> 6. แนบสลิปการโอนเงิน
> [S1]
>
> **เปิดวันไหนบ้าง**
>
> ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ

**วิเคราะห์:** ส่ง6ขั้นตอนจอง แต่วันเปิดยังไม่มีข้อมูลยืนยัน;partialถูกสะท้อนแต่ยังไม่ครบเจตนา

**ควรแก้/รักษา:** ตรวจservicecalendarbindingของsiblingโดยไม่ทิ้งbooking

### ตัวอย่าง 11 — ถามจองได้กี่sessions

- รุ่น: verified_200; key `46182d9ba58edbb20f085b98d0f6b7b82c836832b43f8da8751f5a1f96b338a1`
- คำถาม: How many sessions can one booking include? Could you check this for me
- สถานะ/เวลา: `pipeline:common_partial_answer` / 0.799s
- คำตอบที่เซฟไว้:

> One booking can include up to 6 sessions. Payment is due immediately after booking; if it is not paid within 10 minutes, the booking is cancelled. [S1]
> The policy validity interval is unconfirmed. The recorded clause does not establish current permission.

**วิเคราะห์:** ตอบ6 แต่literalเก่ารอ3 จึงเป็นsource/criterionversionconfound5identities ไม่ใช่5semanticbugs

**ควรแก้/รักษา:** รักษาคะแนนเก่าและแนบsource-alignedcheckที่มีอยู่

### ตัวอย่าง 12 — ถามตำแหน่งShifterด้วยคำพิมพ์ตก

- รุ่น: verified_200; key `41012f5c83e7677c556132b420329ddeeddecb5cc52392d26ffd96482d213616`
- คำถาม: Driving Force Shifter อยู่ซนไหน
- สถานะ/เวลา: `pipeline:common_unavailable` / 0.914s
- คำตอบที่เซฟไว้:

> ระบบตรวจสอบส่วนนี้ไม่พร้อม จึงยังยืนยันคำตอบไม่ได้ครับ

**วิเคราะห์:** frozenตอบunavailableจริง;มีแพตช์native+fieldและHTTPหลังวัดที่บันทึกแล้ว จัดเป็นhistoricalrepairedwithinbounds

**ควรแก้/รักษา:** ไม่อ้าง196scoreรวมแพตช์หลังวัด

### ตัวอย่าง 13 — ถามวันจันทร์เช้าเปิดหรือปิด

- รุ่น: verified_200; key `8b03ee50da5f0a02e4a0cb26fd37ac3f0b226e7634b32075fdf3c0e0400ddbad`
- คำถาม: ช่วยตอบจากข้อมูลที่ยืนยันได้หน่อย: กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า วันจันทร์เช้าเปิดหรือปิด
- สถานะ/เวลา: `pipeline:common_partial_answer` / 0.926s
- คำตอบที่เซฟไว้:

> **กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า วันจันทร์เช้าเปิดหรือปิด**
>
> พบข้อมูลที่เกี่ยวข้อง แต่ยังไม่พบคำตอบตรงส่วนที่ถามครับ
>
> **กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า วันจันทร์เช้าเปิดหรือปิด**
>
> ช่วงเวลาเปิดพื้นที่ในต้นทางยังขัดแย้งกัน ยืนยันได้เฉพาะตารางบริการเล่นด้านล่างครับ
> วันจันทร์ **ไม่เปิดให้บริการ** เนื่องจากเป็นช่วงบำรุงรักษาครับ
> เป็นตารางบริการเล่นที่บันทึกไว้ ยังไม่ยืนยันช่วงวันที่มีผล / ขอบเขตเครื่องหรือโซนที่ใช้ ไม่ใช่สถานะเครื่องว่างแบบสดครับ

**วิเคราะห์:** เริ่มบอกไม่พบคำตอบแล้วตอบปิดบำรุงรักษาในหัวข้อเดิมซ้ำ;ยังต้องแยกopeningกับplayservice

**ควรแก้/รักษา:** นำdirectanswerที่มีscopeก่อนและตัดorphanneednotice

### ตัวอย่าง 14 — ถามดื่มเครื่องดื่มได้หรือไม่

- รุ่น: verified_200; key `382fe8f396d714c1378b09ed7eb764a5d49e48ddd3189aac8047bae0644a5c38`
- คำถาม: Could you check the studio information for me? Please telk me: Are drinks allowed
- สถานะ/เวลา: `pipeline:common_partial_answer` / 1.062s
- คำตอบที่เซฟไว้:

> Several recorded policy versions have unresolved scope or conditions. Each source is retained; confirm the applicable version with the studio.
> Permitted to consume food and beverages only in designated areas [S1]
> Food and drinks are allowed only in designated areas. [S2]
> The policy validity interval is unconfirmed. The recorded clause does not establish current permission.

**วิเคราะห์:** สองpolicyให้ใจความเหมือนกันแต่ระบบยังมองvariantsunresolved;ไม่ใช่ข้อขัดแย้งข้อความโดยตรง

**ควรแก้/รักษา:** ตรวจscope/version/sourceก่อนยุบและอธิบายจุดต่างจริง

### ตัวอย่าง 15 — ถามกติกาTEKKEN8เรื่องsetting

- รุ่น: verified_200; key `e428a2156c0eb3909c3af048050043db617404f7d851aab7eecfcb45307342b5`
- คำถาม: Please check: What do the TEKKEN 8 tournament ruls say about in-game settings? please.
- สถานะ/เวลา: `pipeline:common_partial_answer` / 0.858s
- คำตอบที่เซฟไว้:

> Characters and settings
> * Any character may be selected except DLC characters.
> * Character customization is prohibited in all cases, including outfits, hairstyles, fighting effects and auras.
> * Only default skins may be used.
> * Assist buttons or special assistance systems are allowed.
> * Bugs or glitches that provide an advantage are prohibited.
> * Once a game starts, pausing for any reason is prohibited.
> * Deliberately pausing immediately results in a loss of 1 round.
> Game Settings
> * Number of rounds per game (Round): 3
> * Time per round (Timer): 60 seconds
> * Advantage: No advantage
> * Stage: Random
> The source has not confirmed all linked rule clauses or that the text is complete. The recorded text is shown above.
> **PSU Esports ปะทะมันส์ สนั่นจอ**
> Please confirm that the displayed event rules apply to your match.

**วิเคราะห์:** ส่งclauseหลายข้อและชื่องานพร้อมcaveat ยังต้องยืนยันeventและdependencies;มีเนื้อหาไม่เท่ากับครบกฎที่ใช้จริง

**ควรแก้/รักษา:** ถามตัวงานเมื่อจำเป็น, ไม่ขยายกฎeventหนึ่งไปทุกงาน

## 9. unavailable ทั้ง 36 ข้อใน verified200

นี่คือรายการผลเก่าเพื่อจัดคิว ไม่ใช่ยืนยันว่าทั้ง36ยังล้มในcandidateปัจจุบัน reasonแสดงย่อ;รายละเอียดทั้งหมดดูQUESTION_AUDIT/HTML

| key | คำถาม | วินาที | model event ที่ตรวจพบ | reasonสำคัญ |
|---|---|---|---|---|
| 4dffea636fcbde0489bce9fd88bf69c2f5e8c3ab52cad3f1a936f139ee8b5e0b | will it rain tomorrow ? | 15.242 | R129_model_gateway | bounded_compatibility_operation_not_independently_verified, independent_request_or_constraint_coverage_unresolved, meaning_transport_or_protocol_failure, model_transport_failure, no_supported_task, r101_model_unavailable, store_or_snapshot_unavailable, unrecognised_factual_predicate |
| 82b07728dc5370e10d58e3d846063cb7c4e217db2f122874dfb571e661f9e60f | server กับ client ต่างกันยังไง ช่วยสรุปใจความสำคัญ | 13.963 | R129_model_gateway | bounded_compatibility_operation_not_independently_verified, independent_request_or_constraint_coverage_unresolved, meaning_transport_or_protocol_failure, model_transport_failure, no_supported_task, r101_model_unavailable, store_or_snapshot_unavailable, unrecognised_factual_predicate |
| c5bb62edb9d098af57aafac43c6dd753e1bc1432f2aaa3ef9a98b6aa8b25d965 | ช่วยดูหน่อย ขออ้างอิงกติกา เคาน์เตอร์สไตรก์ 2 ในหัวข้อคุณสมบัติ รายชื่อผู้เล่น และการลงทะเบียน หน่อย ครับ | 5.683 | R129_model_gateway | canonical_competition_scope, clause_semantics_needed, model_transport_failure, requested_need_not_source_verified |
| e7dc0e64320733b62a58955da6b27deb99b3be25b07ea49d3c39594a6c8f8239 | What is an API, in natural Thai? | 4.556 | model_admission_denied | bounded_compatibility_operation_not_independently_verified, independent_request_or_constraint_coverage_unresolved, meaning_transport_or_protocol_failure, model_admission, no_supported_task, r101_model_unavailable, required_relation_missing, store_or_snapshot_unavailable, unrecognised_factual_predicate |
| 80822a260bdd122e45cc7b36102ca940a6f9676eac1d339290fdb534394d24cc | ช่วยตอบจากข้อมูลทียืนยันได้หน่อย: Gaming Keyboard อยู่โซนไกน | 5.895 | R129_model_gateway, model_admission_denied | bounded_compatibility_requested_operation_unverified, independent_request_or_constraint_coverage_unresolved, meaning_transport_or_protocol_failure, model_transport_failure |
| cca6a13bcd8557fa52422ba2da8e717e6841f37490b4e55a131b2001d0ef68ba | Where can you play Horizon Call of the Mountain | 1.074 | model_admission_denied | bounded_compatibility_requested_operation_unverified, independent_request_or_constraint_coverage_unresolved, meaning_transport_or_protocol_failure, model_transport_failure, unrecognised_factual_predicate |
| 3ccffd03b89ab207cffb82b42d3d484bd8ece9e7b3f83e9f53bffbd233cdf05c | Monster Hunter Rise ใช้จอยยังไง | 0.861 | model_admission_denied | action_not_bound, canonical_named_game_control_predicate, collection_completeness_not_proven, collection_members_not_proven, model_transport_failure, requested_need_not_source_verified |
| 776357b78c7b6a09602e7234226281c069a660c5e4cf187171d38a229be610d3 | ถ้าไปช้าจะเป็นอะไรไหม | 3.547 | model_admission_denied | bounded_compatibility_operation_not_independently_verified, independent_request_or_constraint_coverage_unresolved, meaning_transport_or_protocol_failure, model_admission, no_supported_task, r101_model_unavailable, request_constraint_application_unverified, store_or_snapshot_unavailable, unrecognised_factual_predicate |
| 88ef50aef55f6985198e03a17c2175daa766ec677a79bb8a6526ced153ce7490 | Could you cite the Counter Strike 2 rule concerning registration | 0.907 | model_admission_denied | canonical_competition_scope, clause_semantics_needed, model_transport_failure, requested_need_not_source_verified |
| 43b2873212efc69c3bf7005567e686b27bcae4c85945d75c195e73ea5aec223c | ตามกติกกาการแข่่งขัน CS2 เปลี่ยนสมาชิกทีมหลังเริ่มรายการได้หรือไม่ | 1.419 | model_admission_denied | bounded_compatibility_requested_operation_unverified, independent_request_or_constraint_coverage_unresolved, meaning_transport_or_protocol_failure, model_transport_failure |
| edc25eb1eafe9aa094ce6665eac4635863feea3fb999e5a5143b084d07d4636b | What's the difference between server and client without giving long examples? | 5.736 | model_admission_denied | bounded_compatibility_operation_not_independently_verified, independent_request_or_constraint_coverage_unresolved, meaning_transport_or_protocol_failure, model_admission, no_supported_task, r101_model_unavailable, store_or_snapshot_unavailable, unrecognised_factual_predicate |
| 1100db2e70bfb1912d3e4e62242cbf2470999901aaa67ad5d40d7d192060b4d6 | What can you use a PlayStation 5 Slim with Ultra HD Blu-ray Disc Drive for | 1.093 | model_admission_denied | bounded_compatibility_requested_operation_unverified, independent_request_or_constraint_coverage_unresolved, meaning_transport_or_protocol_failure, model_transport_failure, unrecognised_factual_predicate |
| 70997b13c9d5bb133901d0b1070d3be4c01c956c03ece8e2bb8c13ee04d29c2d | Please answer from verified studio information: What is the studio policy for monday play | 5.866 | R129_model_gateway, model_admission_denied | bounded_compatibility_requested_operation_unverified, discourse_prefix, independent_request_or_constraint_coverage_unresolved, meaning_transport_or_protocol_failure, model_transport_failure, unrecognised_factual_predicate |
| d604f5b5ba61c5756117ef941c27bc3b60ed5d78318b53a3095998969a50c3d4 | ขอข้อมูลเรื่องวันศุกร์ ตรวจอุปกรณ์ | 5.951 | R129_model_gateway, model_admission_denied | bounded_compatibility_requested_operation_unverified, independent_request_or_constraint_coverage_unresolved, meaning_transport_or_protocol_failure, model_transport_failure |
| 8c1d09106534d760a4884f4d0cabc3447dcf5d438854e65124aef37390d37188 | อธิบายคำว่า latency ในระบบคอมพิวเตอร์แบบสั้น ๆ ตอบเป็นภาษาไทย | 0.751 | model_admission_denied | bounded_compatibility_requested_operation_unverified, independent_request_or_constraint_coverage_unresolved, meaning_transport_or_protocol_failure, model_transport_failure |
| c5ff78a3089e9f00b4239e2423da005f17d4fc1ab2735e7c9ff28c8ebd83ba0a | In God of War Ragnarök, what button is used for movement? | 0.753 | model_admission_denied | action_not_bound, canonical_named_game_control_predicate, model_transport_failure, requested_need_not_source_verified |
| fd56a79dfeee45d55048673fa88051142b243373dc3343c2bffd443962a8aaca | มี Minecraft ให้เล่นไหม | 8.379 | R129_model_gateway, model_admission_denied | bounded_compatibility_operation_not_independently_verified, independent_request_or_constraint_coverage_unresolved, meaning_transport_or_protocol_failure, model_transport_failure, no_supported_task, r101_model_unavailable, store_or_snapshot_unavailable, unrecognised_factual_predicate |
| 508e5893907f73e6432f97e11f2062551805010bd9793a0186f083db56563647 | Are drins allowwd | 8.677 | R129_model_gateway, model_admission_denied | bounded_compatibility_operation_not_independently_verified, independent_request_or_constraint_coverage_unresolved, meaning_transport_or_protocol_failure, model_transport_failure, no_supported_task, r101_model_unavailable, store_or_snapshot_unavailable |
| 425fc15b19e682b2e4eea1c9a4cd56bf1bda07b7fdc254d33c07f115550ad6f6 | ถ้าจะไปใช้บริการจริง ขอข้อมูลเรื่องพบปัญหา เคื่อง | 3.833 | model_admission_denied | bounded_compatibility_operation_not_independently_verified, independent_request_or_constraint_coverage_unresolved, meaning_transport_or_protocol_failure, model_admission, no_supported_task, r101_model_unavailable, request_constraint_application_unverified, store_or_snapshot_unavailable |
| da50ab2947e251f9dda831ed078099cefa03850aa485aa04f4bcd293a8d01697 | How do you use the controller in Resident Evil Village | 5.774 | R129_model_gateway | action_not_bound, canonical_named_game_control_predicate, collection_completeness_not_proven, collection_members_not_proven, model_transport_failure, requested_need_not_source_verified |
| f3e7737ddcee99f824bf030fe87f9209515a4ca38a4afe34c4621da734818716 | What is a GPU in simple terms? Please give exactly one paragraph. | 4.773 | model_admission_denied | bounded_compatibility_operation_not_independently_verified, independent_request_or_constraint_coverage_unresolved, meaning_transport_or_protocol_failure, model_admission, no_supported_task, r101_model_unavailable, required_relation_missing, store_or_snapshot_unavailable, unrecognised_factual_predicate |
| b92638b91e1406df242e2fd262dbd0416eb8dbca6b41c885dffefd422ea9a269 | Explain the term latency in a short way, specifically for gaming contexts | 3.903 | model_admission_denied | bounded_compatibility_operation_not_independently_verified, factual_need_omitted_from_plan, independent_request_or_constraint_coverage_unresolved, meaning_transport_or_protocol_failure, model_admission, no_supported_task, r101_model_unavailable, store_or_snapshot_unavailable |
| 17f82798b4ffd7ff17ced7afd8c59adf6f1ccfd08736366351b18b826106a81d | In The Legend of Zelda: Breath of the Wild, what button do you press to shrink | 5.785 | R129_model_gateway | action_not_bound, canonical_named_game_control_predicate, model_transport_failure, requested_need_not_source_verified |
| aa201af3defdb69acef0463093034cb24275242f46ff180d420fa5fe7d921079 | How is the rulebook scope and tournament identity handled in the Tekken 8 tournament rules | 5.678 | R129_model_gateway | canonical_competition_scope, clause_semantics_needed, model_transport_failure, requested_need_not_source_verified |
| 41ece310d223e4e58788a2e0d7cf681c4a9fa532eaaa0a9d25935571f8a4f63f | Could you chekc this using verified information: Will it rain tomorrow | 9.267 | R129_model_gateway, model_admission_denied | bounded_compatibility_operation_not_independently_verified, independent_request_or_constraint_coverage_unresolved, meaning_transport_or_protocol_failure, model_transport_failure, no_supported_task, r101_model_unavailable, store_or_snapshot_unavailable |
| 2dfa7f57805aa86968f269ed9fd24b0750c6e44d163504017efa2a7b8393acd5 | JSON คืออะไร ขอแบบเข้าใจง่าย | 8.833 | R129_model_gateway, model_admission_denied | bounded_compatibility_operation_not_independently_verified, independent_request_or_constraint_coverage_unresolved, meaning_transport_or_protocol_failure, model_transport_failure, no_supported_task, r101_model_unavailable, store_or_snapshot_unavailable, unrecognised_factual_predicate |
| a1aee02bdee0601f4bda22a70b0b8c6cc0c87140f20dafc08ad92cb31fede704 | Whoo is the secretary | 3.670 | model_admission_denied | bounded_compatibility_operation_not_independently_verified, independent_request_or_constraint_coverage_unresolved, meaning_transport_or_protocol_failure, model_admission, no_supported_task, r101_model_unavailable, store_or_snapshot_unavailable |
| 73da6de3ccd6987bedcc29323cf3bde852c1c5a32a83cdaa3dd11b58665493db | Does the PC Zone have gaming monitors? I need the official answer. | 0.961 | model_admission_denied | bounded_compatibility_requested_operation_unverified, independent_request_or_constraint_coverage_unresolved, meaning_transport_or_protocol_failure, model_transport_failure, unrecognised_factual_predicate |
| 356e65ab3c34f5b92010c923eed1351c991b5f1bfba6b25a7e6a2bb399047e7b | Whete can VALORANT be plaed | 0.888 | model_admission_denied | bounded_compatibility_requested_operation_unverified, independent_request_or_constraint_coverage_unresolved, meaning_transport_or_protocol_failure, model_transport_failure, unrecognised_factual_predicate |
| 60626fbc933662857285ceb833b62eb11920fcb7c8e30e5fc4ef3069da2e80f1 | กติกา CS2 คำตัดสินใครถือเป็นที่สุดและผู้จัดเปลี่ยนกฎได้ไหม | 0.895 | model_admission_denied | canonical_competition_scope, clause_semantics_needed, model_transport_failure, requested_need_not_source_verified |
| babc90d43b062d0aadf2b8134caafc36c458ad3fe859f0d677699783f26c8d1a | Tell me more about that. | 4.194 | model_admission_denied | bounded_compatibility_operation_not_independently_verified, independent_request_or_constraint_coverage_unresolved, meaning_transport_or_protocol_failure, model_admission, no_supported_task, r101_model_unavailable, store_or_snapshot_unavailable |
| efe8ec50749130e3a344b84b72c2cff9b86d712d15ca11f6b149a80634953f91 | ขอสอบถามหน่อยครับ นักศึกษา PSU เฃ่น VR 30 นาที เสียกี่บท | 5.879 | R129_model_gateway, model_admission_denied | bounded_compatibility_requested_operation_unverified, discourse_prefix, independent_request_or_constraint_coverage_unresolved, meaning_transport_or_protocol_failure, model_transport_failure, request_constraint_application_unverified, unrecognised_factual_predicate |
| 7abfe9c7129fdb1e35a4b4a4881b9e3f3859b928f782b66abe589bffa1490eda | อยากทราบว่า กฏตอนเเข่ง cs2 มีอะไรมั่ง ครับ | 0.650 | model_admission_denied | canonical_competition_scope, clause_semantics_needed, model_transport_failure, requested_need_not_source_verified, thai_vowel_composition |
| 5411eaf1f2b82fa81713cb1bf1c30b8364fae9410299a20f57ea7d914d4de88a | What is JSON? Answer in one sentence | 3.452 | model_admission_denied | bounded_compatibility_operation_not_independently_verified, independent_request_or_constraint_coverage_unresolved, meaning_transport_or_protocol_failure, model_admission, no_supported_task, r101_model_unavailable, required_relation_missing, store_or_snapshot_unavailable, unrecognised_factual_predicate |
| 41012f5c83e7677c556132b420329ddeeddecb5cc52392d26ffd96482d213616 | Driving Force Shifter อยู่ซนไหน | 0.914 | model_admission_denied | bounded_compatibility_requested_operation_unverified, independent_request_or_constraint_coverage_unresolved, meaning_transport_or_protocol_failure, model_transport_failure |
| 4b5d53ef91b969f655f353e5a2f4f9f81db102537e849ec70f6260f3aca69edf | Where can you play Monster Hunter Rise? | 0.777 | model_admission_denied | bounded_compatibility_requested_operation_unverified, independent_request_or_constraint_coverage_unresolved, meaning_transport_or_protocol_failure, model_transport_failure, unrecognised_factual_predicate |

## 10. การแก้ล่าสุดทำอะไรได้แล้ว และยังพิสูจน์อะไรไม่ได้

| กลุ่ม | หลักฐานก่อนแก้ | หลักฐานหลังแก้ | ขอบเขต |
|---|---|---|---|
| sharedboundary/context | plannerกับobserverแบ่งไม่ตรง;บางpositiveผ่านด้วยcorrectivetasksอยู่แล้ว | round01 105checks/14HTTP | ไม่อ้างbaselineผิดทุกข้อ |
| repeatedquote | 6checksล้ม3 | 6checksผ่าน | ประโยคเต็มซ้ำ/ taskfamilycountตรง;substringกำกวมยังblock |
| wrongnumericgameedition | matrix26/27;TEKKEN9ตอบ8;แก้typedอย่างเดียวcompatยังหลุด1/18 | numeric19checksและHTTPpositives/negativesผ่าน | source-derivednumericfamily C04/C05;ไม่ครอบคลุมRoman/DLCทุกแบบ |
| finalround02 | เก็บfailureเดิมครบ | 27matrix +149checksอื่น +21HTTP/52assertionsผ่าน | คนละตัวหารและซ้ำพฤติกรรม;ไม่ใช่accuracy |
| sourcequality | อาหรับปนในคำตอบ | ตรวจพบอยู่ในpayloadจริง | ยังไม่แก้ownerrecord;ไม่ใช่หลักฐานว่าโมเดลแต่งคำนี้ขึ้น |

โค้ดlatest commit99791918 ยังไม่มี full200/2111ใหม่ การใช้คะแนน196/255หรือ1946/2487แทนคะแนนlatestจึงไม่ถูกต้อง และผลscopeguardผ่านไม่พิสูจน์ความถูกต้องทางเกมของข้อความต้นทางทุกบรรทัด

## 11. แผนแก้จากสาเหตุร่วมและเกณฑ์ตรวจ

| ลำดับ | งาน | กรณีปกติที่ต้องรักษา | กรณีผิดที่ต้องกัน | เงื่อนไขจบรอบ |
|---|---|---|---|---|
| 1 | need completion / partial output reconciliation | ราคา+จอง+เกมครบ;usage/genreตอบตรง | ตอบแล้วกลับบอกส่วนเดิมไม่มีข้อมูล;หัวข้อซ้ำ | finaltext/needstate/claimsตรงกันและไม่ตัดsibling |
| 2 | audience+duration+service scope | PSU0;ต่างสถาบันถูกกลุ่ม;หนึ่งและหลายservice | คำผิดทำให้แสดงPSU0แทนต่างมหาลัย;forgedtotal/quantity | positive+ambiguity+wrongtarget+sourceedit/withdrawผ่าน |
| 3 | deadline+admission diagnostics | native/source-backedตอบได้แม้modelไม่พร้อม | runcallเกินงบ,timeoutfalse,admissionถูกเรียกว่าDBเสีย | จับactualstageและเวลา;จำลองslow/denied/errorโดยไม่หยุดmodel;verifiedpartialยังส่งได้ |
| 4 | source applicability/dataquality | ใช้webpinsเมื่อcontentตรง;ราคาowner0คงเดิม | stale/withdrawn/crossentity,foreigntext/literalescapes | แก้เฉพาะสำเนาพร้อมrevisionและไม่publishเอง |
| 5 | owner/editor lifecycle+attachments+หมวดเบาบาง | add/edit/withdrawผ่านHTTP/editorและแชต | cacheเก่า/recordถอน/ภาพยังอ่านไม่ได้แต่claimอ่านแล้ว | หลักฐานtransaction/snapshot/receiptsครบและข้อจำกัดชัด |
| 6 | รอบรวมหลังมีการแก้เชื่อมระบบจริง | ใช้manifestเดิมและworker1 | เปลี่ยนข้อสอบ/เอาholdoutฝึก/เรียกscoresemantic | รายงานrequesterrors/literal/source-reviewedsubsetแยกและเปรียบเทียบsamekeys |

ไม่เริ่มรอบรวมใหม่ในงานวิเคราะห์นี้ และไม่แก้runtimeตามรายการข้างบนโดยเงียบ ๆ งานรอบนี้เป็นรายงานจากlogเท่านั้น

## 12. ไฟล์ส่งมอบและข้อจำกัดการตรวจ

- `REPORT_TH.md`: รายงานนี้
- `SUMMARY.json`: machine summary ทั้ง5รอบและคะแนนเดิมที่อ่านมา
- `DEEP_FINDINGS.json`: same200 comparisons, eventcounts, deadline anomalies
- `INPUT_MANIFEST.json`: path/SHA256ของRESULTSทั้ง5ไฟล์และSQLiteที่อ่านแบบread-only
- `FOCUSED_RESULT_INDEX.json`: result summaries รอบ02รวมfailedattempts
- `QUALITATIVE_REVIEW.json`: ตัวอย่างที่อ่านเชิงคุณภาพและคำวิเคราะห์
- `.local-private/RESULTS_ANALYSIS_VIEW.html`: เปิดดู/ค้นคำถามคำตอบทั้งหมดและfocusedcasesที่เครื่อง โดยไม่มีAPIภายนอก
- `.local-private/QUESTION_AUDIT.jsonl`, `.csv`: รายการทุกแถวจาก5รอบ พร้อมreason/flagsที่สกัด
- `.local-private/FOCUSED_CASES.jsonl`: 48focuseddeliveries แยกจากตัวหารbenchmark

rawanswers/traces/DBอยู่เครื่อง ไม่ใส่Git มีเพียงรายงานสรุป/สคริปต์/manifestตามขอบเขตที่ผู้ใช้อนุญาต

ข้อจำกัด: สองรอบ5%อ่านresponseครบแต่ไม่ได้เปิดSQLitetraceทั้งหมดใหม่;3รอบหลังmatchtraceครบ2511คำขอ การนับreasonเป็นสิ่งที่ระบบรายงานและซ้อนกันได้ ไม่ใช่rootcauseproof ส่วนsourcefactตรวจเจาะจงเฉพาะที่ระบุ ไม่ได้เปิดเว็บใหม่ อ่านภาพแนบครบ หรือรับรองsemanticทุก4623แถว ไม่รวมผลfixture/กรณีปลอมเป็นproductionexamples การสร้างสคริปต์ครั้งแรกมีencodingnameผิดก่อนอ่านคะแนน แก้แล้วรันเฉพาะการวิเคราะห์ใหม่ ไม่ใช่Flowfailureและไม่มีการทดสอบโมเดลซ้ำ

เอกสาร100ปัญหา/143auditgaps/76requirementsเดิมอยู่ `../r135_bounded_response_20261111/ALL_KNOWN_ISSUES_TH.md` ใช้ประกอบประวัติ ไม่ลบหรือเปลี่ยนrequirementเป็นcompleteจากรายงานนี้
