# ผลพัฒนาและทดสอบตาม Flow r52

วันที่ 2026-10-09 · source และ candidate ล่าสุด r52.5 · ทดสอบบนเครื่องผู้ใช้

## 1. สิ่งที่ทำเสร็จ

แก้จุดที่พิสูจน์สาเหตุได้จาก routing, profile/coverage, streaming, log, browser request และคิวหลาย worker แล้วทดสอบเฉพาะส่วนที่เกี่ยวข้อง โดยไม่ได้รันชุดเต็ม 20,000 กว่าข้อ ใช้โมเดล Typhoon 4B เดิมและ shared model admission 1 งาน เพื่อไม่เพิ่มจำนวน generation บน GPU โดยไม่มีผลวัด

- frame rate/feel/each/across/study session ไม่กลายเป็นราคา/ทุกบริการ/ปุ่ม/จองเพียงเพราะส่วนหนึ่งของคำ
- `ว่าง` ที่อยู่ใน `ระหว่าง` ไม่เป็นคำถามสถานะว่าง ส่วน `PC ว่างไหมระหว่าง 10:00 กับ 11:00` ยังเป็นคำถามจอง
- งานแปล/ขั้นตอน/สองประโยค/ข้อดีข้อเสียแยกตาม entity/คำขอความยาว มี profile และ budget ตามคำขอ ไม่จำกัดทุกอย่างเหลือ 96–128 token
- stream ต้องได้รับ provider done ก่อนยอมรับ คำตอบบางส่วน/timeout มี metadata และเหตุผลเฉพาะ
- ผลไม่ครบบางรูปแบบแก้ได้หนึ่งครั้ง ภายใน budget เดิม; ถ้าไม่พอไม่ retry ไม่จำกัด
- หลาย worker ใช้ broker ที่ parent ร่วมกัน; model peak active ที่วัดเท่ากับ 1 ไม่ใช่ GPU generation พร้อมกัน 6 งาน
- Job API บันทึก SQLite ก่อน ACK, turn idempotency, payload conflict, ลำดับ session, capacity/TTL, polling และ queued cancellation
- งานที่ถูกปฏิเสธ admission ไม่ถูก commit เป็นคำตอบสุดท้าย; ทดลองใหม่ได้เมื่อมีเหตุผลว่าการเรียกโมเดลยังไม่ได้เกิด
- defer คืน dispatcher, first attempts มาก่อน retry, งาน retry อายุ 15 วินาทีได้สิทธิ์กลับ และพัก clear general requests เมื่อ broker แสดงว่าโมเดลไม่ว่าง

คำอธิบาย/เส้นทางครบ: [FLOW.md](FLOW.md) · คำตอบจริงรายข้อ: [QUESTIONS_ANSWERS_ANALYSIS.md](QUESTIONS_ANSWERS_ANALYSIS.md)

## 2. ผลแยกตามระดับหลักฐาน

| ชุด | ก่อน | หลัง | สิ่งที่ยืนยันได้ |
|---|---|---|---|
| Signal/profile/contract fixtures | 6/21 | 21/21 | เงื่อนไขเฉพาะที่มี oracle |
| Pipeline fixtures | 6/9 → 8/9 | 9/9 | routing/ส่งคำตอบ fixture; generation ถูก mock |
| เว็บจริง 11 general + 8 price turns | ส่ง LLM 9/11; transport 19/19 | ส่ง LLM 11/11; transport 19/19 | สร้าง/ส่งได้; เนื้อหามีข้อผิดพลาดตามหัวข้อ 5 |
| Tests ใหม่สำหรับงานนี้ | — | 11 methods ผ่าน | คิว/owner source/broker/repair/partial stream/contract |
| Browser request helper | — | ผ่าน | polling, one POST, fallback, bounded retry; fetch ถูก mock ไม่ใช่ visual browser QA |
| Regression ส่วนใกล้เคียง | 73 methods, 4 subfailures | 78 methods, 3 subfailures | แก้ selector ผิด 1 จุด; อีก 3 เกณฑ์เดิมล้าสมัย ต้องรายงานว่ายังแดง |

ผล suite ล่าสุดใน `loop_release_regression.txt`; tests ใหม่ใน `r52_5_unit.txt`; ไม่แก้ legacy tests เพื่อทำให้สีเขียว

### เกณฑ์ regression เดิมที่ยัง fail 3 subcases ใน 2 methods

1. ID ของบุคคลภายนอก: ต้องการ URL เว็บเก่า ทั้งที่คำตอบปัจจุบันอ้าง `local://service_policy/user_answers_20261008` จากเจ้าของและมี ID/student card/passport ครบ
2. membership: ต้องการข้อความ “do not need to be a PSU student” แทนคำตอบ owner source “Membership is not required…” จึงไม่ได้ตรวจ facet เดียวกัน
3. membership + ID: ตรวจ `National ID` แบบ case sensitive แต่ source เป็น `national ID`

รันบน snapshot ก่อนแก้แล้วพบ failures เหล่านี้อยู่ก่อนจริง (`baseline_neighbor_failures.txt`) เพิ่ม tests owner source ทั้งไทย/อังกฤษแทนการเปลี่ยนคำตอบให้เข้ากับเกณฑ์เก่า

## 3. เวลาคำขอ LLM พร้อมกัน

| ไฟล์ผล | จำนวนคำขอ | transport จบ | ส่งคำตอบ LLM | เวลาจบแต่ละคำขอ เรียงน้อย→มาก (วินาที) |
|---|---:|---:|---:|---|
| load_r52_5_one.json | 1 | 1 | 1 | 2.17 |
| load_r52_3_two.json | 2 | 2 | 2 | 2.61, 3.29 |
| load_before.json | 4 | 4 | 1 | 2.64, 3.96, 5.35, 9.88 |
| load_after.json | 4 | 4 | 4 | 3.04, 5.01, 6.74, 8.31 |
| load_r52_5_six.json | 6 | 6 | 6 | 3.40, 5.80, 7.47, 9.41, 10.95, 12.31 |

งานสั้นชุดเดียวกันใช้ตรวจคิวและการส่งครบ ไม่ใช้วัดความหลากหลายทางภาษา ไม่มี warm/cold randomization และจำนวนตัวอย่างน้อย จึงไม่รายงาน p95/SLO หรือจำนวนผู้ใช้สูงสุดที่รับรองได้ ตัวเลขนี้เป็น burst ที่ลองบนเครื่องจริง มี shared model limit 1

### โหลดผสม 6 คำขอ: งานยาว 500 คำ + LLM สั้น 3 ข้อ + ข้อมูลราคา/สมาชิก 2 ข้อ

| รุ่น | transport จบ | คำถามราคา | คำถามสมาชิก | เวลาจบสูงสุด |
|---|---|---|---|---|
| r52.3 | 6/6 | 17.01s | 17.69s | 19.23s |
| r52.4 | 6/6 | 9.03s | 9.71s | 19.51s |
| r52.5 | 6/6 | 5.52s | 6.31s | 20.70s |
| r52.5 รอบไม่มี regression รันคู่ | 6/6 | 1.67s | 2.17s | 18.81s |

ACK ของรอบ r52.5 อยู่ 0.022–0.248s เป็นเวลารับลงคิว ไม่ใช่เวลาที่ได้คำตอบ

รอบ quiet รับลงคิว 0.029–0.244s และงานยาวจบ 12.45s โดยราคา/สมาชิกจบก่อน การทดลองระหว่างพัฒนาบางรอบมี regression ใช้ CPU พร้อมกัน จึงใช้ตัวเลข 17→9→5.5s เป็นหลักฐานเชิงสำรวจประกอบ queue trace ไม่อ้างเป็นการวัด speedup แบบควบคุมปัจจัยครบ รอบ quiet บันทึกแยกใน `loop4_mixed_r52_5_quiet.json`

คำถามราคาของ r52.3 ใช้ pipeline จริงเพียง 0.0737s แต่รวมรอคิวประมาณ 17s: สาเหตุหลักคือคิวเลือก retry เก่าซ้ำ ไม่ใช่โมเดลไม่รู้ราคา การให้ first attempts เข้าก่อนและพักงานทั่วไปเมื่อโมเดลไม่ว่างช่วยลดเวลาราคาเป็น 5.52s; ยังมีค่า preprocessing/ช่อง worker และไม่ควรรับรองว่าราคาจะต่ำกว่า 1s ทุกโหลด

หนึ่งคำขอในรอบสุดท้ายใช้เวลารวมเกิน 20s เพราะรวมเวลาในคิวด้วย; deadline 20s เดิมครอบคลุมแต่ละ backend attempt ขณะที่ job TTL เท่ากับ 90s ขอบเขตนี้ต้องแสดงแยกกัน

การ duplicate turn เดิมคืน job เดิม (202); เปลี่ยน question ภายใต้ turn เดิมได้ 409 ไม่สร้าง inference ใหม่ (`idempotency` ในไฟล์ mixed)

## 4. ข้อสรุปจากงานวิจัยที่นำมาใช้จริง

ใช้ [CheckList](https://aclanthology.org/2020.acl-main.442/) สร้าง positive/negative/invariance fixtures, [IFEval](https://arxiv.org/abs/2311.07911) แยกเงื่อนไขรูปแบบที่ตรวจด้วยโปรแกรม, [Self-RAG](https://arxiv.org/abs/2310.11511) เป็นแนวคิดแยกการค้นกับความเพียงพอของหลักฐาน และ [VTC](https://arxiv.org/abs/2401.00588) เป็นแรงจูงใจตรวจ fairness/aging

เราไม่ได้ implement reflection training ของ Self-RAG, token fairness theorem ของ VTC, continuous batching ของ ORCA, PagedAttention ของ vLLM หรือย้าย engine งานที่ทำเป็น routing/validator/application queue/parent admission ซึ่งทดสอบได้บนระบบ Windows เดิม รายละเอียดงานวิจัย 19 งานและข้อจำกัดการค้นอยู่ใน [รายงานเดิม](../paper-search-results/20261009_181825_llm-serving-answers/report.md)

## 5. สิ่งที่ยังผิด/ยังไม่รับรอง

### P0 เนื้อหาของ general model หลังผ่านรูปแบบ

- Ping: โมเดลพูดว่าเป็นการทดสอบความเร็ว/เสถียรภาพ ไม่ชัดว่าตรวจ IP reachability และ round-trip time ด้วย ICMP ไม่ได้วัด bandwidth แบบ speed test; เทียบ [Microsoft ping](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/ping)
- แปล network connection เป็น internet connection ทำให้ความหมายแคบลง ถึงแม้ภาษาและจำนวนบรรทัดผ่าน ต้องใช้ translation fidelity rubric ไม่ใช่เพียง format
- บท 500 คำอังกฤษพูด HTTP/TLS เหนือ TCP แบบไม่จำกัดรุ่น; [RFC 9114](https://www.rfc-editor.org/rfc/rfc9114.html) ระบุ HTTP/3 บน QUIC จึงต้องมี version qualifier/exception ก่อนถือว่าอธิบายครบ
- RAM/SSD ไทยมีการเหมารวมเรื่องความร้อน/ความเสียหาย และยังไม่รับรองจำนวน 500 คำ เนื่องจาก runtime ไม่มี Thai tokenizer; metadata แจ้งการไม่ยืนยันจำนวนคำแล้ว
- งานชวนสองประโยคผ่าน 2 sentences แต่ใช้ประโยคแรกเป็นคำทักทาย จึงยังไม่ใช่สองประโยคที่มีเนื้อหาชวนเต็มทั้งคู่
- งานยาวในรอบ quiet มีข้อความท้าย “The term latency is preserved…” และถาม clarifying question เพิ่มแม้ตอบไปแล้ว เกิดจากโมเดลนำคำสั่งเก็บ term/ถามกลับเมื่อข้อมูลไม่พอมาแสดงใน output; validator ยังตรวจ word/entities แต่ไม่ตรวจส่วนท้ายชนิดนี้ ต้องเพิ่มข้อห้ามเผยคำสั่งและตรวจคำถามกลับที่ไม่จำเป็นก่อนนับว่าคำตอบพร้อมใช้งาน

แนวทางต่อ: curated general facts ที่มี primary sources เฉพาะหมวดที่ต้องการรองรับจริง → claim-level oracle/translation meaning checks → bounded repair เฉพาะกรณีมีหลักฐาน → rerun invariance sets ห้ามใช้ LLM ตรวจตัวเองแล้วรับรองทุกข้อความ หรือเติม template ตรงกับตัวอย่างเพียงอย่างเดียว

### P1 Serving และวัดผล

- ยังไม่ได้ทำ sustained load, hard-kill ระหว่าง actual generation หรือ freeze/restart recovery ของเว็บจริง; unit tests ใช้ DB reopen และ simulated revoke จึงไม่ใช่ crash certification ทั้งระบบ
- ยังไม่ได้วัดโมเดล parallel 2 เทียบ 1 แบบควบคุม memory/คุณภาพ ไม่เพิ่ม limit จากการคาดเดา; ก่อนลองต้องแยก runtime ทดลอง วัด VRAM/RAM/TTFT/stop/quality และคืนค่ารุ่นเดิมได้
- คิวรับได้ 32 ไม่แปลว่า 32 คนจะได้คำตอบภายใน 20s; job TTL/capacity และเวลาแต่ละ profile ต้องใช้ทดสอบโหลดเป้าหมาย
- job result มีอยู่ใน SQLite/API แต่ UI ยังไม่ recover job อัตโนมัติเมื่อ refresh; terminal results ยังไม่มี retention cleanup
- `llm_attempted` บาง trace เดิมยัง true แม้ health/admission ปฏิเสธ ต้องอ่าน `llm_concurrency_allowed`, skip reason, provider_done ประกอบ ไม่ใช้ flag เดียวเป็นหลักฐานว่าเรียกโมเดลสำเร็จ

### P2 ข้อมูลบริการที่ต้องยืนยันเฉพาะเรื่อง

ตารางราคาเดิมระบุถึง 2026-03-31: การแสดง recorded rates พร้อม caveat ถูกกว่าการยืนยันว่าเป็นราคาปัจจุบันโดยเดา ต้องถามเจ้าของว่า “อัตรา PS5/Switch/Cockpit/VR ในตารางเดิมยังใช้หลัง 31 มีนาคม 2026 หรือมีอัตรา/วันที่มีผลใหม่ใด?” PC มี local update 2026-07-27 แยกแล้ว งานนี้ไม่ได้เปลี่ยน policy

ผู้ใช้เคยยืนยันสถานะ booking สดและภาษาอังกฤษชุดบริการเดิมผ่านแล้ว คำยืนยันนั้นยังคงอยู่; งานทั่วไปที่เพิ่มในรอบนี้เป็นชุดใหม่ ไม่ใช้สรุปว่าผู้ใช้รับรองแล้ว

## 6. ไฟล์และระบบที่ใช้งาน

URL ทดลอง: http://127.0.0.1:8093/ · candidate: `candidate_r52_5/PSU_Esports_Chatbot_Local` · runtime `2026.10.09-research-flow-r52.5`

ใช้ Python/Ollama/models ที่มีบนเครื่องเดิม แพ็กเกจนี้เป็น candidate สำหรับเครื่องปัจจุบัน ไม่ใช่ชุด portable ใหม่พร้อมทุก dependency ต้นฉบับ ROOT แก้ source แล้ว; job feature default ปิดและเปิดใน launcher ของ candidate เท่านั้น อย่าใช้ launcher เก่าแล้วคาดว่ารัน source รุ่นใหม่นี้

ตรวจ hash 345 ไฟล์เดิม, owner data/Dashboard 38 ไฟล์ไม่เปลี่ยน, ไม่มีไฟล์ snapshot เดิมหาย, source candidate ตรง ROOT ข้อมูลเต็ม `preservation_audit.json` ไม่ได้เก็บ hash ของ old logs ก่อนเริ่ม จึงอ้างไม่ได้ว่าทุก old log ผ่าน hash audit แต่การรันใหม่เขียนเฉพาะผล/SQLite/log ของ candidate ใหม่และไม่ reset/revert

Git status ใช้ไม่ได้เพราะ worktree metadata ชี้ path ที่เข้าถึงไม่ได้ (`git_status_before.txt`); ไม่แก้ Git metadata และไม่ถือว่า working tree clean
