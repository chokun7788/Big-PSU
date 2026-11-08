# PSU Esports Chatbot: วิเคราะห์ปัญหาและวิธีแก้จากงานวิจัย

วันที่ 9 ตุลาคม 2026 · รายงานภาษาไทย · ทบทวนแบบเจาะปัญหา 19 งาน · สถานะ: วิจัยและออกแบบ ยังไม่ได้เปลี่ยนโค้ดหรือรันทดสอบใหม่ในรอบนี้

## 1. คำตอบที่ได้จากการค้น

ต้องแก้ร่วมกัน 4 ชั้น: **เข้าใจคำถาม → สร้างคำตอบครบตามที่ขอ → จัดคิวและใช้โมเดล → ตรวจและส่งคำตอบ** การเพิ่มจำนวน worker แก้ได้เพียงบางส่วน และอาจเพิ่มการแย่ง GPU/RAM ถ้าแต่ละ worker ส่งงานเข้าโมเดลพร้อมกันโดยไม่มีตัวกลางควบคุม

ลำดับที่แนะนำ:

1. P0 แก้ routing และ answer contract ที่ทำให้คำถามชัดเจนถูกถามกลับหรือทิ้งคำตอบ
2. P0 เก็บเหตุผลและเวลาแต่ละขั้น โดยไม่ใช้ HTTP 200 เป็นเครื่องหมายว่าตอบถูก
3. P1 แยกงานตอบจากข้อมูลกับงานสร้างข้อความ จัดคิว LLM แบบมีขอบเขตและเห็นสถานะ
4. P1 กำหนดความยาวตามคำขอ ส่งความคืบหน้า และรักษาการตรวจคำตอบก่อนยืนยัน
5. P2 ทดลองโมเดลพร้อมกัน 1 เทียบ 2 งานบนเครื่องจริง เมื่อ 4 ข้อแรกทำงานถูกต้อง
6. P3 พิจารณา engine/เครื่องเซิร์ฟเวอร์เมื่อมีผลวัดว่าระบบปัจจุบันรองรับโหลดเป้าหมายไม่ได้

**วิธีนำไปทำ:** [FLOW_IMPLEMENTATION.md](FLOW_IMPLEMENTATION.md) มีลำดับแก้ ไฟล์ที่เกี่ยวข้อง ตัวอย่างคำถาม เกณฑ์ผ่าน และแผนทดลอง

## 2. ขอบเขตและความน่าเชื่อถือ

ใช้สกิล paper-search-pro ตามคำขอ ตรวจ Setup พบว่ายังไม่มี OpenAlex API key และ NCBI email จึงหยุด workflow ตัวช่วยค้นหลายฐาน แล้วใช้ web search และเปิดบทความต้นฉบับจาก arXiv, USENIX, ACL Anthology และ NeurIPS แทน ค้นเรื่อง concurrency/scheduling, memory, routing/RAG, evaluation, multilingual และ spelling รวมทั้งค้นงานใหม่ปี 2025–2026 เพิ่ม

นี่เป็น **targeted literature review** สำหรับตัดสินใจพัฒนา ไม่ใช่การค้น Standard 60–180 งานที่เสร็จครบขั้นของสกิล ไม่อ้าง PRISMA compliance หรือเปอร์เซ็นต์ครอบคลุมวรรณกรรม ไม่มี citation-count/rank lookup, citation-network expansion หรือการประเมิน saturation ตัวเลขความเกี่ยวข้องใน HTML เป็นการจัดลำดับของผู้เขียนรายงาน ไม่ใช่ผล classifier ตาม workflow ปกติ รายงานภาษาไทยและ Flow เป็นเอกสารหลัก

ตรวจชื่อ ผู้เขียน และวิธีที่เกี่ยวข้องจากหน้าแหล่งต้นฉบับ/ส่วนวิธีของบทความตาม reading ledger ใน papers.json ไม่ได้อ่านทุกหน้าของทุกงาน ผลวิจัยจากเครื่องขนาดใหญ่ใช้เป็นหลักการ ไม่ใช้คูณเวลาของเครื่องผู้ใช้ งาน preprint ระบุเป็น preprint เมื่อยังไม่ได้ตรวจการตีพิมพ์

หลักฐานระบบมาจาก r51 เดิมและการอ่านโค้ดปัจจุบัน จึงแยก:

- **ยืนยันจาก log/โค้ด:** การจับคำ each/rate, queue wait, token cap, คำตอบถูกทิ้ง, timeout
- **ข้อสันนิษฐาน:** คำ session ทำให้ study session เข้าหมวดจอง; provider load 5.39 วินาทีเกิดจากโหลดใหม่จริงหรือไม่
- **ยังไม่ได้ยืนยัน:** parallel 2 จะเร็วขึ้นเท่าไร, จำนวนผู้ใช้สูงสุดระยะยาว, คุณภาพหลังแก้, การเปลี่ยน engine บนแพ็กเกจ Windows
- **มนุษย์ยืนยันแล้วในบริบทเดิม:** ผู้ใช้ยืนยันสถานะจองจริงถูกต้องและอังกฤษของชุดบริการเดิมผ่าน การทดลองคำถามทั่วไปชุดใหม่ไม่ได้ยกเลิกคำยืนยันนั้น

## 3. หลักฐานบนเครื่องผู้ใช้

แอปที่วัด: r50.2 / 2026.10.09-flow-r50.2, Typhoon 2.5 Qwen3 4B Q4_K_M, RTX 4050 Laptop 6GB ใช้ GPU ประมาณ 5GB ขณะวัด RAM ประมาณ 87% ไม่ใช่ค่าปัจจุบันตลอดเวลา

| รายการ | ผล r51 | ความหมายที่ถูกต้อง |
|---|---|---|
| เว็บ actual chat probe | ส่งคำตอบ LLM ผ่าน pipeline 6/16 | อีก 10 เคสมี guard, renderer, validation หรือ timeout; ไม่ใช่โมเดลผิดทั้งหมด |
| เว็บ concurrent standard 1 คน | p95 2.40s, 2/2 ส่งคำตอบ | ตัวอย่างน้อย ไม่ใช่ SLO รับรอง |
| เว็บ concurrent standard 2 คน | p95 4.12s, 4/4 ส่งคำตอบ | ระดับสูงสุดที่ทดสอบแล้วผ่านครบ; ยังไม่ได้วัด 3 |
| เว็บ concurrent standard 4 คน | 4/8 ส่งคำตอบ, 4 HTTP 503 | ติด policy คิวและขั้น pipeline |
| โมเดลตรง output 512 token / 1 งาน | ประมาณ 9s | หลายเคสจบเพราะ length ไม่ได้ตอบครบ |
| โมเดลตรง 512 token / 6 งานพร้อมกัน | p95 จบ 54.54s, p95 token แรก 45.60s | คนท้ายรอคิวหนัก; การรับเข้าคิวไม่ได้แปลว่าจบเร็ว |
| โมเดลตรง concurrent ทั้งหมด | done 52/52, stop 25 / length 27 | done เป็นการจบ stream; ไม่ใช่ความครบ/ความถูกต้อง |
| เว็บถามให้ตอบ 500 คำ | profile 96–128 token; บางเคสเหลือ 2 ประโยค | เว็บชุด long_request ไม่ใช่ benchmark คำตอบยาวจริง |

หลักฐานเต็ม: [รายงาน r51](../../r51_llm_benchmark_20261009_173746_93dfb5/LLM_TIMING_REPORT_R51.md), [คำถาม คำตอบ และเหตุผล](../../r51_llm_benchmark_20261009_173746_93dfb5/QUESTIONS_ANSWERS_R51.md)

## 4. แยกปัญหา: ทำไมตอบแบบนี้ และควรตอบอะไร

| กลุ่ม | ตัวอย่าง / สิ่งที่ระบบตอบ | สาเหตุที่ยืนยันได้ | คำตอบหรือพฤติกรรมที่ควรได้ | วิธีแก้หลัก |
|---|---|---|---|---|
| คำทั่วไปชนศัพท์บริการ | Why can high frame rate still feel choppy? → ถามบริการเพื่อบอกราคา | protected_intents.py นับ rate ทั้งใน price signal และ usage signal จึงเป็นหลักฐานสองเงื่อนไขจากคำเดียว ส่วน conversation_plan.py ก็มี rates? เป็น price candidate | อธิบาย frame pacing, frame time, synchronization เป็นเหตุที่เป็นไปได้ ไม่วินิจฉัยเครื่องโดยไม่มีข้อมูล | semantic slots + contextual evidence ก่อนเปิด price guard |
| คำบอกขอบเขตจับกว้างเกิน | Compare TCP and UDP ... each → ถามว่าทั้งหมดของหมวดไหน | ALL regex ยอมให้ each/every/both เดี่ยว ๆ เป็น scope บริการ | เทียบ TCP/UDP ตามด้านที่ถาม | ต้องผูก quantifier กับ noun/topic หรือ pending clarification |
| คำโจทย์ทั่วไปชน scope | balls in each box → scope clarification | each box ชน ALL เหมือนข้างบน ไม่ใช่ ball มี substring all | A=5, B=3 ใน fixture นี้ | ชนิดงาน reasoning และ entities boxes ต้องชนะ scope บริการ |
| รูปแบบภาษาไม่ครอบคลุม | Give three steps ... → english_no_answer | English direct-general gate มีช่องว่างสำหรับสำนวนคำสั่งนี้ | 3 ขั้นตอนฝึก touch typing ตามลำดับ | ภาษาไทย/อังกฤษใช้ task schema เดียวกัน |
| ผสมภาษาถูกปฏิเสธ | Translate this Thai sentence to English → wrong layout | ทางออก renderer จัดเป็น wrong layout แทน translation | แปลข้อความที่ระบุโดยรักษาความหมาย | ตรวจเจตนาการแปลก่อน layout gate; ไม่แก้ quoted text แบบเดา |
| คำทั่วไปคล้ายการจอง | Write ... study session → reservation no_answer | final route ยืนยัน; ต้นเหตุคำ session ยังเป็น hypothesis | ข้อความเชิญ 2 ประโยค | trace competing candidates; แยก study session กับ booking slot |
| validator ไม่สอดคล้อง | Explain network latency → โมเดลตอบแล้วแต่ no_answer | generation contract ผ่าน; downstream expected fact/summary แต่ actual controls/how_to/list | อธิบาย latency โดยยอมให้มีคำแนะนำสั้นที่เกี่ยวข้อง | ใช้ AnswerPlan เดียวกันทั้ง generate/validate/render |
| คำตอบไม่ครบ | RAM vs SSD 500 คำ → ถูกตัดและปฏิเสธ / network 500 words → สั้น | cap ต่ำและ concise shaping | ตอบตามความยาวที่รองรับ หรือแจ้งขอบเขตที่ทำได้อย่างตรงไปตรงมา | adaptive output budget + required content + completion check |
| ระบบล่มกลายเป็นไม่มีข้อมูล | ping TH / balls TH → ข้อมูลยังไม่พบ | TimeoutError; llm_call ว่างเมื่อ exception | แจ้งโมเดลหมดเวลาและแนวทางลองใหม่ | reason code แยก model timeout / source missing / validation failed |
| ส่งสำเร็จแต่เนื้อหายังอ่อน | touch typing TH → ฝึกคลิกปุ่มตัวอักษร | คำตอบผ่าน pipeline แต่ไม่ให้วิธีฝึกที่ชัด | วางนิ้วแถวเหย้า ฝึกไม่มองแป้น เน้นแม่นแล้วเพิ่มความเร็ว | assertion เนื้อหา + semantic rubric |
| คิวเต็มเร็ว | 4/6 คนบางคำขอ 503 | pipeline worker 1, รอ worker 3s, active cap 16, deadline 20s | รับงานที่ยังมี capacity พร้อม job ID/สถานะ; ถ้าเต็มต้องแจ้งตรง | bounded job queue แยก queue deadline กับ execution budget |
| รอคำตอบเต็มก่อนแสดง | token แรก provider เร็ว แต่หน้าเว็บยังรอ | provider stream อยู่แล้ว แต่ web คืนเมื่อ pipeline จบ | ความคืบหน้าทันที; คำตอบ final หลังตรวจ | events สำหรับ queued/running/final; stream คำตอบตามนโยบาย validation |

**ข้อสรุป:** “ข้อมูลมีครบ” ยังไม่พอ ต้องเลือกหมวดและ section ถูก รักษาบริบทก่อนหน้า แล้วตรวจให้ครบตามคำขอ กฎหรือราคาหายจากคำตอบอาจเกิดจาก routing/rendering แม้แหล่งข้อมูลครบ จึงต้องดู trace ก่อนเพิ่มข้อมูลใหม่

**จุดที่ตรวจพบเพิ่มในรอบอ่านโค้ด:** [protected_intents.py](C:/Users/Chokhun/Downloads/Learn-LLM/18_PSU_Esports_Update_Route_Data/app/pipeline/protected_intents.py:173) ให้ rate/rates เป็น price signal และ [บรรทัด 274](C:/Users/Chokhun/Downloads/Learn-LLM/18_PSU_Esports_Update_Route_Data/app/pipeline/protected_intents.py:274) ให้คำเดียวกันเป็น usage ก่อนคืน price and usage เมื่อไม่มี service นี่อธิบาย positive สองเงื่อนไขที่ไม่เป็นอิสระได้ จึงต้องแก้ทุก price detector ที่ใช้จริง ไม่แก้ regex ใน conversation_plan.py จุดเดียวแล้วสรุปว่าครบ

## 5. งานวิจัยที่ตรงกับปัญหา

### 5.1 การรันพร้อมกัน คิว และ memory

- **P01 Orca (OSDI 2022):** จัด batch ใหม่ในแต่ละรอบสร้าง token ช่วยให้คำขอเข้า/ออก batch ได้ระหว่างงานกำลังรัน แนวคิด continuous batching ต้องอยู่ใน inference engine การเพิ่ม Python worker ไม่ได้สร้างกลไกนี้ให้เอง [ต้นฉบับ](https://www.usenix.org/system/files/osdi22-yu.pdf)
- **P02 PagedAttention / vLLM (SOSP 2023):** จัด KV cache เป็น block ลดพื้นที่เสียและแบ่งใช้เมื่อมี prefix ร่วม เหมาะกับการรองรับ batch มากขึ้น แต่ยังต้องมีหน่วยความจำพอสำหรับ model และ cache ที่ใช้จริง ไม่ได้ทำให้ VRAM ไม่จำกัด [ต้นฉบับ](https://arxiv.org/abs/2309.06180)
- **P03 Sarathi-Serve (OSDI 2024):** แบ่ง prefill เป็นช่วงและกำหนด token budget ต่อ iteration เพื่อลดการรบกวน decode งานยาว การตัดข้อความ input ของแอปแล้วส่งหลาย request ไม่เท่ากับ chunked prefill ใน engine [ต้นฉบับ](https://www.usenix.org/system/files/osdi24-agrawal.pdf)
- **P04 DistServe (OSDI 2024):** แยก prefill/decode ไปคนละ GPU และใช้ goodput ภายใต้ TTFT/TPOT SLO เป็นเป้าหมาย แนววัดผลนำมาใช้ได้ แต่สถาปัตยกรรมหลาย GPU ยังไม่เหมาะกับเครื่องนี้ [ต้นฉบับ](https://arxiv.org/abs/2401.09670)
- **P05 FastServe (preprint ฉบับที่ตรวจ):** token preemption และหลายระดับ priority ช่วยลด head of line blocking ต้องบริหาร KV cache ที่พักไว้ด้วย คิว short/long ของแอปเป็นการยืมแนวคิด ไม่ได้มี token preemption แบบบทความ [ต้นฉบับ](https://arxiv.org/abs/2305.05920)
- **P06 Fairness / VTC (2024 revision):** วัดภาระด้วย input/output token และจัดลำดับจากบริการที่แต่ละ client ได้รับ ไม่ใช้จำนวน request อย่างเดียว นำมาปรับเป็น fair admission + aging ในแอปก่อน ส่วนหลักประกันใน paper ต้องใช้กลไกที่เขาศึกษา [ต้นฉบับ](https://arxiv.org/abs/2401.00588)
- **P07 Fluid-Guided Scheduling (2025, revision v4 ปี 2026, preprint):** การรับงานต้องคิดถึง KV cache ที่โตระหว่าง decode มี WAIT/Nested WAIT; ทดลองหลักผ่าน Vidur และมี A100 80GB ใน appendix เหมาะเป็นเหตุผลให้ทำ memory-aware admission ยังไม่ควรยก policy ทั้งชุดมาใช้ทันที [ต้นฉบับ](https://arxiv.org/abs/2504.11320)
- **P08 SGLang (NeurIPS 2024):** RadixAttention ใช้ KV cache ของ prefix ร่วมซ้ำ และมี structured decoding ช่วยลดงานซ้ำ นำมาใช้เริ่มจากจัด system prompt ให้คงที่และวัด cache จริง การ cache คำตอบ booking สดเป็นอีกเรื่อง ต้องมี freshness/version [ต้นฉบับ](https://papers.nips.cc/paper_files/paper/2024/file/724be4472168f31ba1c9ac630f15dec8-Paper-Conference.pdf)

### 5.2 เลือกงานและหลักฐานให้ถูกก่อนสร้างคำตอบ

- **P09 RouteLLM (ICLR 2025):** เรียนรู้ router ระหว่างโมเดลแรงกับโมเดลเล็กจาก preference data จุดที่นำมาใช้คือวัด trade-off ของ routing ด้วยคุณภาพจริง แต่โจทย์ของเราตอนนี้เป็น task/domain routing ไม่ใช่เลือก strong/weak model; ไม่ใช่ติดตั้ง RouteLLM แล้ว regex ผิดจะหาย [ต้นฉบับ](https://arxiv.org/abs/2406.18665)
- **P10 Self-RAG (2023 / ICLR 2024):** แยกว่าจะ retrieve หรือไม่ และตรวจ relevance/support/usefulness บทความต้อง train reflection tokens การทำ gate/validator ในแอปเป็นแนวคิดประยุกต์ ไม่ใช่ Self-RAG เต็มระบบ [ต้นฉบับ](https://arxiv.org/abs/2310.11511)
- **P11 CRAG (2024 preprint):** ประเมินเอกสารเป็น correct/incorrect/ambiguous แล้วเลือกทางแก้ เหมาะกับการแยก “ค้นผิดหมวด” จาก “แหล่งไม่มีคำตอบ” ในแอปเราใช้แหล่งเจ้าของยืนยันก่อน; web search ทั่วไปไม่ใช้ทดแทนกฎ/ราคาศูนย์ [ต้นฉบับ](https://arxiv.org/abs/2401.15884)
- **P12 Lost in the Middle (2023 preprint):** ตำแหน่งหลักฐานและความยาว context มีผลในงานที่ทดสอบ ใช้เป็นเหตุผลให้คัด section ที่ตรงคำถามและทดลองตำแหน่งเอกสาร ไม่ใช่หลักฐานว่าความผิดพลาดใน r51 ทุกเคสเกิดจาก context ยาว [ต้นฉบับ](https://arxiv.org/abs/2307.03172)
- **P13 LLMLingua (2023):** จัดงบ prompt ต่างกันระหว่างคำสั่ง คำถาม และตัวอย่าง วิธี compression มีต้นทุนและอาจเสียข้อมูล เริ่มจากลบ context ที่ไม่เกี่ยวข้องก่อน; ตัวเลขราคา วัน เวลา และข้อยกเว้นต้องคงไว้ [ต้นฉบับ](https://arxiv.org/abs/2310.05736)

### 5.3 วัดคำตอบ ไม่วัดแค่รันจบ

- **P14 CheckList (ACL 2020):** ใช้ Minimum Functionality, Invariance และ Directional Expectation ตรวจความสามารถเฉพาะ ยืมเป็นชุดคำถามเดิม/เปลี่ยนสำนวน/เปลี่ยน slot พร้อม negative controls แทนการเพิ่ม typo แบบสุ่มจำนวนมากอย่างเดียว [ต้นฉบับ](https://aclanthology.org/2020.acl-main.442/)
- **P15 IFEval (2023):** ตรวจคำสั่งที่ตรวจได้ด้วยโปรแกรม เช่นจำนวน bullet/ประโยค/ความยาว แยก prompt-level กับ instruction-level ผล ผ่านรูปแบบไม่ได้รับรองเนื้อหาถูก และการนับคำภาษาไทยต้องกำหนด tokenizer ที่ชัดเจน [ต้นฉบับ](https://arxiv.org/abs/2311.07911)
- **P16 Ragas (2023, revision 2025):** แยก faithfulness, answer relevance และ context relevance ใช้ช่วยวิเคราะห์ชั้นที่ผิดได้ LLM judge ใช้ประกอบผล และต้องสอบเทียบกับ fixture/oracle ที่มีอยู่ ไม่ใช้ self-judge รับรองข้อเท็จจริงทุกอย่าง [ต้นฉบับ](https://arxiv.org/abs/2309.15217)
- **P17 AbstentionBench (2025):** แยกเหตุที่ควรไม่ตอบ เช่นขาดเงื่อนไข คำถามตั้งบนสมมติฐานผิด ข้อมูลล้าสมัย การเปลี่ยนเป็นโมเดลใหญ่/เพิ่ม reasoning ไม่รับรองว่าจะรู้ว่าเมื่อไรควรถามกลับ ใช้สร้าง positive และ negative answerability fixtures [ต้นฉบับ](https://arxiv.org/abs/2506.09038)

### 5.4 ภาษาไทย อังกฤษ และพิมพ์ผิด

- **P18 NeuSpell (EMNLP demos 2020):** ใช้บริบทของประโยคและ noise ที่คล้ายความผิดจริงช่วยแก้สะกด เป็นงานภาษาอังกฤษ จึงนำหลักการ contextual correction มาใช้กับไทยได้แต่ผลตัวเลขไม่โอนตรง หลีกเลี่ยงแก้ชื่อเกม/เลขเครื่อง/เวลาโดยอัตโนมัติเมื่อความหมายกำกวม [ต้นฉบับ](https://aclanthology.org/2020.emnlp-demos.21/)
- **P19 MASSIVE (ACL 2023):** แยก intent กับ slots ในข้อมูลหลายภาษา รวม th-TH และวัด exact match/intent accuracy/slot F1 เป็นแนวทางทำ schema ร่วมไทยอังกฤษ แต่ข้อมูลทั่วไปของเขาไม่ใช่ ground truth กฎหรือราคาศูนย์เรา [ต้นฉบับ](https://aclanthology.org/2023.acl-long.235/)

## 6. How to: สถาปัตยกรรมที่เหมาะกับระบบนี้

### A. เข้าใจคำถามด้วย AnswerPlan กลาง

ให้ผล interpretation มี domain, task, entities, time/date, user_group, scope, requested_sections, requested_length, pending_question, source_requirement และ provenance ของ slot แต่ละตัว เก็บข้อความดิบเสมอ

การจับ keyword ยังใช้เสนอ candidate ได้ แต่ price ต้องมีความสัมพันธ์ “ค่าบริการของอะไร/กลุ่มไหน” ขณะที่ frame rate มี technical entity จึงไม่ควรเปิด price guard ส่วน each ต้องขยาย noun ที่กำลังพูดถึง ไม่สร้าง service scope โดยอัตโนมัติ

กรณีถามราคา “บุคคลภายนอก” แล้วตอบ “PC” ให้เติม service ของ pending price plan และคง user_group เดิม “ทั้งหมด” เติม scope โดยคงหมวดราคา คำถามใหม่คนละเรื่องต้องยกเลิก pending ด้วยเหตุผลที่ตรวจได้

competition_rules ต้องคง game, tournament/version, section ที่ถาม; ไม่พบ CS2/ROV ใน corpus ที่ตรวจจริงต้องแจ้งขาดกติกาเกมนั้น ห้ามยืม VALORANT มาแทน หากถามทั้งหมดของเกมที่มีข้อมูลให้เลือก sections ของเกมนั้นให้ครบ

### B. เส้นทางตอบต่างกันตามหลักฐาน

1. ราคาหรือข้อมูลที่มีโครงสร้าง: อ่านข้อมูลยืนยันและ render โดยตรง; LLM ใช้ช่วยภาษาได้เมื่อจำเป็น
2. booking status: ดึงข้อมูลจริงตาม flow เดิม ตรวจวันที่ไทย/freshness แล้ว render; ค่า cache ไม่เปลี่ยนเป็นข้อมูลสดเอง
3. กฎการแข่งขัน: retrieval ที่ผูก game/version/sections แล้วตรวจ coverage; มีบางส่วนตอบส่วนที่มีพร้อมระบุสิ่งที่ขาด
4. งานทั่วไป/แปล/เขียน: ไม่พยายามหาเอกสารศูนย์ทุกครั้ง คำตอบทั่วไปไม่มี source ศูนย์ก็เป็นคำตอบที่ถูกประเภทได้
5. กำกวมจริง: ถามเฉพาะ slot ที่ขาด พร้อมเก็บ pending state; ห้ามวนกลับไปถามทุกหมวดเมื่อผู้ใช้ตอบ slot แล้ว

### C. รับหลายผู้ใช้โดยมีงานค้างที่ตรวจสถานะได้

ออกแบบ endpoint งานใหม่ที่เข้าคิวและตอบรับ job ID เร็ว สถานะ queued/running/validating/completed/failed/cancelled/expired เป็นคนละสถานะกับคำตอบ ส่ง progress ผ่าน SSE หรือ polling และเก็บ final หลัง validator ผ่าน

แยก queue budget ออกจาก execution budget ตั้ง queue cap, ต่อ-session cap และ total lifetime มี fairness กับ aging กันงานยาวอดคิว หากโหลดต่อเนื่องเกินกำลังประมวลผล ต้องจำกัดรับงานหรือเพิ่ม capacity คิวไม่ทำให้ทุกคำขอตอบได้ทันพร้อมกันแบบไม่จำกัด

### D. เพิ่ม parallel อย่างมีหลักฐาน

แอป worker ต้องผ่าน LLM broker กลางเพราะ semaphore เดิมอยู่ในแต่ละ process การเพิ่ม worker อย่างเดียวทำให้ limit เดิมไม่ได้ครอบคลุมทั้งระบบ

เริ่มโมเดล 1 lane ให้ถูกก่อน แล้ว A/B 2 lanes ด้วย runtime ที่ระบบเป็นเจ้าของบนพอร์ตแยก ตรวจ model runner ว่าใช้ parallel จริง และวัด GPU peak/RAM/OOM/CPU fallback/คุณภาพ อย่ากำหนดผลลัพธ์ว่าต้องเร็ว 2 เท่า

เอกสาร Ollama ระบุ OLLAMA_NUM_PARALLEL เพิ่มหน่วยความจำ context ตามจำนวน parallel และ OLLAMA_MAX_QUEUE เป็นเพดานคิว; setting ของ server ต้องกำหนดก่อนเริ่ม server การตั้ง env ใน client ไม่ได้ปรับ service ที่รันอยู่แล้ว [Ollama FAQ](https://docs.ollama.com/faq)

### E. ความยาวและ streaming ต้องไม่ทำให้ตอบไม่ครบ

คำถามสั้นใช้ budget สั้น คำถาม “3 ขั้นตอน” ต้องมีครบ 3 ขั้น คำถาม “ทั้งหมด” ต้องมี coverage ของรายการที่ยืนยันได้ คำตอบยาวต้องมี budget ตามงานและภาษา ไม่ใช้ 128 token กับทุกคำขอ

Provider ของระบบ stream อยู่แล้ว การเปิดหน้าเว็บ stream จึงต้องเปลี่ยน protocol ผ่าน supervisor และ renderer ด้วย สำหรับ facts ของศูนย์ส่ง progress ระหว่างรอ แล้วส่งคำตอบที่ตรวจครบ; หากแสดง generated preview ให้แยกจาก final และรองรับการปฏิเสธ/แทนที่อย่างชัดเจน [Ollama Streaming](https://docs.ollama.com/api/streaming)

## 7. แก้ข้อเสนอเดิมให้ตรงโค้ด

- การเพิ่ม queue wait เป็น 30s ด้วย env อย่างเดียวใช้ไม่ได้: worker_queue_wait_sec() จำกัดสูงสุด 5s ต้องแก้การออกแบบ/โค้ดและ deadline ถ้าต้องการคิวยาวกว่านั้น
- PSU_LLM_CONCURRENCY_WAIT_SEC จำกัดสูงสุด 1s และ semaphore เป็น threading object ใน process ต้องมี shared admission เมื่อใช้หลาย workers
- keep_alive 30m และ warmup มีอยู่แล้ว จึงตรวจค่า/runner log ก่อนเสนอเพิ่มสิ่งเดิม
- active cap 16 ไม่ได้หมายถึงโมเดลตอบพร้อมกัน 16 คน; queue cap ของแอปกับ Ollama เป็นคนละชั้น
- streaming ช่วยให้เห็นความคืบหน้าเร็วขึ้น แต่ไม่ลดจำนวน token ที่ต้องสร้างเอง
- คำตอบ final ที่ 200 แต่ no_answer / validation_failed / truncated ต้องนับแยก

## 8. การทดสอบที่ควรทำหลังลงมือ

ดูชุดละเอียดใน Flow: เริ่ม 12 failure families จาก r51 พร้อมไทยอังกฤษ/สำนวนใหม่/negative controls และ multi-turn price→PC/all จากผู้ใช้

วัด 3 แบบแยกกัน: router-only ไม่มี LLM, direct model, และ actual web with validation ใช้ภาษาไทยอังกฤษสมดุล งานสั้น/ยาวจริง/ผสม/long input/arrival burst และ sustained arrival

รายงานจำนวนที่รับเข้าคิว จำนวนที่ตอบครบถูกตาม fixture จำนวนที่จบทัน SLO และ latency ของ failure ด้วย เลี่ยง survivor bias ที่รายงานเฉพาะคำขอเร็วซึ่งรอด queue

สำหรับคำตอบไม่มี oracle ชัดเจน ใช้ rubric และ judge ประกอบ โดยระบุ provisional ไม่เปลี่ยนเป็น “คนยืนยันแล้ว” อัตโนมัติ

## 9. สิ่งที่ทำเองได้ และสิ่งที่ยังต้องตัดสินใจ

**ทำเองได้จากหลักฐาน:** scoped intent guard, schema/contract ร่วม, tracing, renderer error, output completion, targeted fixtures, job queue prototype, cancellation/idempotency, isolated parallel benchmark, paper-to-code comparison

**ยังต้องเจ้าของเมื่อเกิดช่องว่างข้อมูลจริง:** กฎเกม/รายการที่ corpus ไม่มี, roster/rules ที่ยังไม่ได้รับไฟล์, นโยบายคืนเงิน/เปลี่ยนวัน/เด็กเข้าใช้บริการที่ไม่ยืนยัน ห้าม LLM แต่ง

**ตัวเลือกผลิตภัณฑ์ที่ควรสรุปก่อนเปิดจริง:** ยอมรอคิวสูงสุดกี่วินาทีสำหรับงานยาว, ขอบเขตตอบคำถามทั่วไป, ถ้าเครื่องไม่พอจะใช้งาน local ต่อหรือให้ server กลาง ข้อเสนอทดลองใน Flow เดินหน้าได้โดยยังไม่ต้องใช้คำตอบเหล่านี้เป็นนโยบายจริง

## 10. ผลตรวจทานรายงาน

ตรวจแยกสาเหตุ routing กับ provider, ไม่เอา done/HTTP200 เป็น correct, ไม่ใช้ throughput multiplier จาก paper รับรองเครื่องนี้, ไม่เสนอใช้ Self-RAG/CRAG/RouteLLM เต็มระบบแบบข้ามเงื่อนไข, ไม่เอา cache booking เก่ามาเรียกสด และแยกข้อสันนิษฐาน provider load/study session ออกจากหลักฐานแล้ว

ไฟล์ประกอบ: papers.json, papers.csv, bibtex.bib, ris.ris, query_plan.json, execution_log.json และ raw/ อยู่ในโฟลเดอร์เดียวกัน HTML ใช้ renderer ของสกิลพร้อมข้อความระบุ fallback review; citation counts/coverage ไม่ได้วัด หาก UI ของ renderer แสดง 0 ในช่องที่ข้อมูลหาย ให้ถือว่าไม่ทราบ ไม่ใช่ผลค้นว่าเป็นศูนย์
