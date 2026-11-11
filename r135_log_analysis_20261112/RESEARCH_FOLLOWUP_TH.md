# งานวิจัยและแผนทดลองต่อจากปัญหาใน log — 12 พฤศจิกายน 2026

ฐานปัญหา: REPORT_TH.md, ADMISSION_AUDIT.json และ DEEP_FINDINGS.json ใช้ต่อจากชุดอ้างอิงเดิม 31 papers/11 official docs ใน parent ไม่เริ่มค้นปัญหาเดิมใหม่ทั้งหมด

## วิธีค้นและข้อจำกัด

ใช้แนวทาง agent-mode ของ skill paper-search-pro เพื่อเลือกวิธีสำหรับ implementation ไม่ใช่ systematic review ตรวจ config แล้วพบ MISSING_REQUIRED_CONFIG จึงหยุด API helpers ตาม SKILL.md ไม่ติดตั้งหรือสร้าง keys ข้าม multi-index federation, journal metrics, classifier subagents และ saturation estimate; ใช้ main agent ค้น primary webpages แยกแทนตามกฎห้าม subagents ของโครงการ จำนวนอ้างอิงข้างล่างเป็นชุดคัดเลือกเฉพาะปัญหา ไม่ใช่ผลรัน Standard/Quick pipeline สำเร็จ ไม่อ้าง PRISMA หรือความครอบคลุมวรรณกรรมทั้งหมด

คำค้น: Adaptive-RAG question complexity; FrugalGPT cost performance cascade; The Tail at Scale; Selective Question Answering under Domain Shift; PAL Program-aided Language Models; official circuit breaker half-open and deadline propagation

ตรวจ primary abstracts/metadata และ official documentation sections ที่เกี่ยวข้อง ไม่กล่าวว่าอ่าน full text ของทุกงานครบ ไม่มีงานใดพิสูจน์ผลบนระบบ PSU หรือเครื่องนี้ล่วงหน้า

## หลักฐานที่เลือกและวิธีใช้ร่วมกัน

| แหล่ง | หลักการจากงานนั้น | ข้อเสนอประยุกต์ PSU | สิ่งที่ไม่อ้างว่าทำแล้ว |
|---|---|---|---|
| [Adaptive-RAG, NAACL2024](https://aclanthology.org/2024.naacl-long.389/) | เลือกวิธี QA ตามความซับซ้อน แทนใช้เส้นทางแพงเท่ากันทุกคำถาม; ใช้ classifier ที่ฝึกมา | ใช้ native typed/source reads ที่ตรวจได้ก่อน เลือก model เฉพาะ need ที่ยังไม่รองรับและมีงบ | ไม่ฝึก classifier ใหม่ และไม่ถือว่า source-first routing เท่ากับทำ Adaptive-RAG ครบ |
| [FrugalGPT, 2023](https://arxiv.org/abs/2305.05176) | ศึกษา prompt adaptation, approximation และ model cascades ภายใต้งบ | มองค่าใช้จ่าย/เวลาเป็นงบต่อ need หยุด escalation เมื่อหลักฐานไม่เพิ่ม; ไม่ให้ขั้นเสริมทำลายคำตอบที่ตรวจได้แล้ว | ไม่ติดตั้งหลายโมเดล ไม่เอาตัวเลขลดต้นทุนของ paper มาเป็นผล PSU |
| [The Tail at Scale, CACM2013](https://research.google/pubs/the-tail-at-scale/) | ความหน่วงช่วงหางมีผลต่อประสบการณ์รวม ต้องออกแบบทั้งระบบให้ทนต่อส่วนที่ช้า | ดู p95/max/over-budget ไม่ใช้ median เพียงอย่างเดียว; ตรวจ outlier2859s แยกและส่ง verified partial | ไม่เปิด hedged/parallel requests บนโมเดลเดียวและไม่กล่าวว่าแก้ hard cancellation แล้ว |
| [Selective QA under Domain Shift, ACL2020](https://aclanthology.org/2020.acl-main.503/) | วัดการตอบได้ร่วมกับความถูกต้องภายใต้ abstention และ domain shift; softmax confidence อย่างเดียวไม่พอ | ติดตาม coverage/risk และ positive controls ควบคู่กับ negatives ห้ามทำให้ดูดีด้วยการระงับทุกข้อ | ไม่อ้าง calibrated confidence หรือ semantic accuracy จาก literal/HTTP |
| [PAL, ICML2023](https://proceedings.mlr.press/v202/gao23f.html) | แยกการแปลโจทย์กับการคำนวณ โดยใช้ runtime ทำขั้นคำนวณ | ใช้ Decimal และ typed source-rate/rule/quantity proofs ที่จำกัดและตรวจกลับได้; compose หลักฐานทุก alternative ที่ส่ง แทนให้โมเดลรับรองเอง | ไม่ให้รันโค้ดอิสระจากโมเดล และ arithmetic ไม่รับรองว่า source/หน่วย/ผู้ใช้ถูกต้อง |
| [Circuit Breaker, Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker) | แยก Closed/Open/Half-Open, จำกัด recovery probes และเก็บ observability ของสาเหตุ | ตรวจ cooldown receipt, kind isolation และ recovery โดยไม่ปิด health guard; แยก denied-before-HTTP จาก timeout หลังส่ง | ไม่ reset live circuit หรือหยุด protected model; parent มี half-open code อยู่แล้ว ต้องทดสอบก่อนอ้างว่าขาด |
| [Deadlines, gRPC](https://grpc.io/docs/guides/deadlines/) | deadline ต้อง propagate; แอปต้องหยุดงานที่เริ่มไว้เองเมื่อถูก cancel | request clock ร่วม, คงเวลา finalizer, cap แต่ละ call, แสดง over-budget ตามจริงและตรวจงานที่ยังทำต่อ | ระบบใช้ HTTP/custom gateway ไม่ได้ย้ายเป็น gRPC; cancel Future ไม่ใช่หลักฐานว่าหยุดโมเดลแล้ว |

วิธีใช้ร่วม: source-bound plan → deterministic verification ทุก claim → request coverage → optional model ภายใต้งบและ circuit → final text/state ที่ตรงกับสิ่งที่ตรวจได้ → แยก latency/coverage/source precision ในรายงาน

## จับคู่กับปัญหาใหญ่จากรายงาน

- LOG-01/02/17/18: Tail at Scale + deadline propagation + circuit observability + cost-aware escalation; ยังต้องแยกเวลาแอป/queue/โมเดล/เครื่องพัก และลดการเก็บ snapshot ซ้ำโดยไม่ทำหลักฐานหาย
- LOG-03/04/05/09/12: adaptive routing + shared task/slot contracts จากแผนเดิม; ใช้ source relations และ raw spans ไม่ใช้ชื่อคล้ายหรือ platform เดียวเป็น proof
- LOG-06/07/08: typed program arithmetic + audience/service/unit binding + all-delivered-lines proof; ราคา0/หลายบริการ/ช่วงคนต้องรักษาทั้ง positive และ negative
- LOG-10/11/13/15: ใช้ provenance/citation/data-quality methods ใน RESEARCH_METHODS_FOR_ALL_ISSUES_TH.md เดิม ไม่อ้างว่า paper routing แก้ source authority หรือวันที่มีผลได้
- LOG-14/16: selective QA + paired evaluation/holdout discipline เดิม; จัดการ stale literal criteria โดยรายงานแยก ไม่แก้คะแนนย้อนหลังเพื่อให้สูง

## วงรอบที่ได้รับอนุญาต

1. เลือก actual failure หนึ่งกลุ่มจาก log พร้อมผลคาดและขอบเขตที่ไม่ควรถูกกระทบ
2. สร้าง candidate แยก เก็บ before; ถ้าไม่เกิดแล้วใน parent ล่าสุดให้จัดเป็นประวัติ ไม่แก้ให้ซับซ้อนขึ้นโดยไม่จำเป็น
3. แก้สาเหตุร่วมหนึ่งชุด ไม่ลด source/target/quantity/withdraw guards
4. รัน positive + prior failure + ambiguity/forgery + affected regression ครั้งเดียวหลังแก้
5. ตรวจคำตอบจริง claims/receipts/terminal state และเก็บทุก attempt รวมที่ล้ม
6. แนวทางเดิมล้มสองรอบให้เปลี่ยน/ถอน/พัก ไม่วน negatives เพิ่มอย่างเดียว
7. รวมเฉพาะที่มีหลักฐาน แล้วเลือกกลุ่มถัดไป; broad trial ใช้ worker1 และ manifestเดิมเมื่อมี substantive integration change; ไม่รันทุกการแก้หนึ่งจุด

### รอบแรกที่เลือก

ตรวจ false duration notice ของ PC หลายบริการแต่ audience เดียว: log ตอบ0บาทสำหรับ30นาที แล้วแจ้งว่า30นาทียังไม่ยืนยัน โค้ด duration_proofs เดิมยอมรับเพียงหนึ่ง rate/หนึ่ง calculation จึงต้องพิสูจน์ก่อนว่าเกิดใน parent ล่าสุดจริง แล้วพิจารณา compositional proof ของ **ทุก alternative ที่ส่ง** โดยห้ามนำราคา alternatives มาบวกเป็นยอดซื้อ

รอบนี้ไม่อ้างว่าแก้ cooldown/latency ทั้งระบบแล้ว งาน admission/deadline เป็นลำดับถัดไปที่ต้องรักษา model health และไม่แตะ process ที่ป้องกันไว้
