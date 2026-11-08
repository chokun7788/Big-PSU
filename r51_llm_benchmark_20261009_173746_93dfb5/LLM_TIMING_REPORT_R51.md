# LLM บนเครื่องผู้ใช้: เวลา คิว และปัญหาที่พบ r51

วันที่ 2026-10-09 Asia/Bangkok · แอป 2026.10.09-flow-r50.2 · model scb10x/typhoon2.5-qwen3-4b (4B, Q4_K_M) · NVIDIA RTX4050 Laptop GPU 6141MiB

## สรุปคำตอบ

- **ผ่านเว็บจริง คำถามที่ให้ LLM สร้างคำตอบ:** ชุด standard ที่ 1 คน p50 1.98s/p95 2.40s; 2คน p50 2.91s/p95 4.12s ผ่านครบทั้ง2waves ที่4คนเริ่ม503 (4/8คำขอ) ที่6คน503 (7/12)
- **โมเดลอย่างเดียว:** คำถามสั้นหลากหลายเมื่อโมเดลพร้อมประมาณ0.18–4.56s; สร้างยาวถึง128/256/512tokenใช้ประมาณ2.3/4.5/9.1s ตามลำดับ
- **512tokenพร้อมกัน:** 1/2/4/6คำขอ p95ประมาณ9/18/37/55s; คิวสะสมเห็นชัด ไม่ได้เร่งจำนวนคนแล้วทุกคนได้คำตอบใน9s
- โมเดลตอบstreamingมีtokenแรกเร็วเมื่อไม่รอคิว แต่เว็บปัจจุบันส่งoutputเมื่อpipelineจบ จึงไม่เท่ากับผู้ใช้เห็นคำตอบทันที
- ส่งคำขอขอ500คำบนเว็บ ไม่ได้หมายถึงได้500คำ: generation profileปัจจุบันจำกัด96–128token/สรุปสั้น บางข้อความถูกตัดออก/ปฏิเสธ
- รอบนี้ทดสอบและวิเคราะห์ ไม่เปลี่ยนโค้ดผลิตภัณฑ์ นโยบาย โมเดล หรือค่าserver; logเดิมคงอยู่

## 1. วิธีวัดและความหมาย

### A. ผ่านเว็บจริง

POST /api/chat ของ server8091, localeTH/EN, session/turnใหม่ทุกคำขอ, debug=trueเพื่อเก็บtraceเหมือนหน้าเว็บ, experimental_rag_fallback=trueเหมือน app.js ส่งจริง, allowLLMถูกควบคุมจากserver

เริ่ม16คำถาม 8หมวด: นิยาม เปรียบเทียบ เหตุผล ขั้นตอน แปล เขียนข้อความ คำนวณง่าย และอธิบายยาว ไทย8/อังกฤษ8 ตรวจว่า LLMใช้เพื่อ classify หรือ generate ไม่ถือLLMintentว่าเป็นgeneratedanswer

นำเฉพาะคำถามที่ส่งคำตอบLLMสำเร็จจริงมาทดสอบ concurrent standard และ long_request อย่างละ2waves ที่1,2,4,6คน หยุดเมื่อ2ระดับต่อกันไม่ผ่าน ไม่retry503 ไม่เพิ่มworkers ไม่ปิดhealthguard; appใช้worker1 queuewait3s activecap16 deadline20s PIDทุกระดับคงเดิม ไม่มี recycleปน

standardชุดที่เข้าgenerationได้เป็นคำถามTH5รูปแบบ; long_requestเป็นEN1รูปแบบที่ขอ500คำแต่ระบบตอบconcise การวัดนี้จึงไม่ใช่ balancedTH/ENทุกระดับและlong_requestไม่ใช่longoutputจริง

### B. โมเดลโดยตรง เพื่อสมมติให้ทุกคำขอเข้าสู่LLM

เรียกOllama /api/generate โมเดลเดียวกันบนเครื่องนี้ ไม่ผ่านrouting/validation/admissionของchatbot; stream=true, think=false, temperature0.15, top_p0.8, num_ctx3072, keep_alive30m

20single requests: 6รูปแบบTH/ENที่cap256, longTH/ENที่cap128/256/512, และเพิ่มsyntheticreferencecontext5000charsให้TH/ENที่cap128

Concurrent short cap128 และlong cap512 เริ่ม1,2,4,6คน อย่างละ2waves ทุกsessionแยก ไม่มีretryและไม่ยิงWordPress; harnessให้เวลา60sเพื่อเห็นคิวที่เกินproductdeadline20s ผลrawLLMจึงใช้แทนผลเว็บไม่ได้

ทุกworkloadทำตามลำดับ ไม่รันchatและdirectmodelbenchmarkทับกัน ไม่unloadโมเดลหรือ restartserverเพื่อทำcoldboot ตัวอย่างแรกมีproviderloadเวลาเพิ่มเป็นfirst-observedstartup effect ไม่ใช่controlledcold-startbenchmark

### สิ่งที่วัด

- End-to-end = ก่อนส่งHTTPถึงรับคำตอบครบ ส่วน direct = รวมเวลารอOllamaและstreamจนdone
- TTFT = firstnonemptyresponsefragment ไม่รวมthinking (thinkfalse) ไม่ใช่การตอบจบ
- p50=มัธยฐาน p95=nearest-rank (samplesน้อยบางระดับp95=max)
- generated_ok = transport200+โมเดลสร้างคำตอบที่ผ่านpipelineจนส่งออก ไม่ใช่factualcorrectnessทุกประโยค
- done=true = providerจบstreamได้; done_reason=length = ชนเพดานtoken ไม่รับรองว่าทำคำขอครบ
- ตารางsuccessful latencyไม่รวม503ที่ปฏิเสธเร็ว แต่ denominator/status countsรวมfailureเสมอ

## 2. ผ่านเว็บจริง: ผู้ใช้ถามพร้อมกัน

| ชุดผ่านเว็บ | พร้อมกัน | คำตอบ LLM ที่ส่งสำเร็จ/คำขอ | p50 (s) | p95 (s) | HTTP503 | PIDเปลี่ยน |
|---|---:|---:|---:|---:|---:|---|
| standard | 1 | 2/2 | 1.98 | 2.40 | 0 | ไม่ |
| standard | 2 | 4/4 | 2.91 | 4.12 | 0 | ไม่ |
| standard | 4 | 4/8 | 2.96 | 17.30 | 4 | ไม่ |
| standard | 6 | 5/12 | 3.25 | 5.28 | 7 | ไม่ |
| long_request | 1 | 2/2 | 2.67 | 2.90 | 0 | ไม่ |
| long_request | 2 | 4/4 | 3.69 | 5.25 | 0 | ไม่ |
| long_request | 4 | 4/8 | 4.39 | 5.97 | 4 | ไม่ |
| long_request | 6 | 4/12 | 4.02 | 6.03 | 8 | ไม่ |

Highest tested all-available level=2คำขอพร้อมกัน ยังไม่ได้วัด3คนจึงไม่อ้างmaximum2คนแบบตายตัว ระดับที่ผ่านคือavailabilityใน2waves ไม่ใช่capacityรับรองระยะยาว

ที่4standardมีคำตอบหนึ่งใช้17.30s (translationหลังRAGmiss) ส่วนคำขออื่นถูก503จากqueuewait คิว3sตัดคำขอได้ก่อนdeadline20s แม้modelยังตอบทีละคำขอได้ รายละเอียดเวลาLLMและpipelineอยู่rawtrace

หลักฐาน: [CHAT_LOAD_summary.json](<C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r51_llm_benchmark_20261009_173746_93dfb5\CHAT_LOAD_summary.json>) และ [CHAT_LOAD_raw.jsonl](<C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r51_llm_benchmark_20261009_173746_93dfb5\CHAT_LOAD_raw.jsonl>)

## 3. โมเดลโดยตรง: เวลาแต่ละประเภท/ความยาว

| แบบคำถาม | ภาษา | token cap | context เพิ่ม(chars) | เวลาจบ (s) | tokenแรก (s) | output tokens | tokens/s | เหตุจบ |
|---|---|---:|---:|---:|---:|---:|---:|---|
| definition | th | 256 | 0 | 2.41 | 0.49 | 114 | 59.45 | stop |
| definition | en | 256 | 0 | 1.00 | 0.08 | 55 | 59.76 | stop |
| comparison | th | 256 | 0 | 2.41 | 0.06 | 140 | 59.60 | stop |
| comparison | en | 256 | 0 | 0.81 | 0.09 | 43 | 59.95 | stop |
| steps | th | 256 | 0 | 4.56 | 0.06 | 256 | 56.88 | length |
| steps | en | 256 | 0 | 0.90 | 0.07 | 48 | 58.31 | stop |
| translation | th | 256 | 0 | 0.49 | 0.06 | 25 | 58.47 | stop |
| translation | en | 256 | 0 | 0.18 | 0.06 | 7 | 60.02 | stop |
| writing | th | 256 | 0 | 1.04 | 0.06 | 57 | 57.98 | stop |
| writing | en | 256 | 0 | 0.75 | 0.06 | 40 | 58.81 | stop |
| reasoning | th | 256 | 0 | 1.28 | 0.06 | 70 | 57.72 | stop |
| reasoning | en | 256 | 0 | 1.06 | 0.07 | 57 | 57.56 | stop |
| long | th | 128 | 0 | 2.28 | 0.06 | 128 | 57.76 | length |
| long | th | 256 | 0 | 4.50 | 0.06 | 256 | 57.72 | length |
| long | th | 512 | 0 | 9.06 | 0.07 | 512 | 57.01 | length |
| long | en | 128 | 0 | 2.32 | 0.10 | 128 | 57.82 | length |
| long | en | 256 | 0 | 4.50 | 0.06 | 256 | 57.73 | length |
| long | en | 512 | 0 | 9.05 | 0.07 | 512 | 57.01 | length |
| definition | th | 128 | 5000 | 2.41 | 0.39 | 111 | 55.23 | stop |
| definition | en | 128 | 5000 | 1.66 | 0.40 | 69 | 55.34 | stop |

Done reasons: {'stop': 13, 'length': 7}. คำขอ500คำทุกcapในการทดสอบนี้ชนlength แม้512tokenใช้9s ก็ไม่ได้ตอบ500คำครบ ไทยtokenไม่เท่ากับคำ จำนวนoutputtokensจริงและdone_reasonต้องอ่านร่วมกับเวลา

syntheticcontext5000charsไม่ได้เป็น5000tokens providerรายงานprompt_eval_countในraw เพิ่มcontextส่งผลต่อpromptprocessing/firsttokenและcache แต่2ตัวอย่างไม่พออ้างเส้นเวลาlinearทุกcontextlength

หลักฐาน: [MODEL_PROBE_summary.json](<C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r51_llm_benchmark_20261009_173746_93dfb5\MODEL_PROBE_summary.json>) และ [MODEL_PROBE_raw.jsonl](<C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r51_llm_benchmark_20261009_173746_93dfb5\MODEL_PROBE_raw.jsonl>)

## 4. ถ้าทุกคำขอเข้าที่โมเดลพร้อมกัน

| โมเดลโดยตรง | พร้อมกัน | มี done/คำขอ | p50 จบข้อความ (s) | p95 จบข้อความ (s) | p95 tokenแรก (s) | จบภายใน20s | ชน token limit |
|---|---:|---:|---:|---:|---:|---:|---:|
| short | 1 | 2/2 | 1.72 | 2.59 | 0.43 | 2/2 | 0 |
| short | 2 | 4/4 | 2.16 | 2.85 | 1.77 | 4/4 | 0 |
| short | 4 | 8/8 | 3.30 | 6.08 | 4.13 | 8/8 | 0 |
| short | 6 | 12/12 | 5.32 | 9.04 | 7.83 | 12/12 | 1 |
| long | 1 | 2/2 | 9.03 | 9.03 | 0.10 | 2/2 | 2 |
| long | 2 | 4/4 | 13.51 | 18.03 | 9.09 | 4/4 | 4 |
| long | 4 | 8/8 | 22.94 | 36.77 | 27.77 | 4/8 | 8 |
| long | 6 | 12/12 | 31.83 | 54.54 | 45.60 | 4/12 | 12 |

ทุกคำขอdirectจบstreamได้ 52/52 ภายในbudgetวัด60s แต่จำนวนที่ตรง20sต่างกัน และ {'stop': 25, 'length': 27}. จำนวนdoneไม่ใช่จำนวนคำตอบcompleteตามคำขอ

Long6คน: p50จบ31.83s/p95 54.54s, p95tokenแรก45.60s; เพียง4/12คำขอจบไม่เกิน20s ข้อจำกัดของwebจะเกิดก่อนรอถึง54sเพราะqueuewait3sและdeadline20s

Short6คนทุกคำขอจบไม่เกิน20sในdirecttestนี้ แต่ผ่านเว็บไม่ได้6ครบเพราะผ่านstageอื่น/queuepolicyด้วย ยังไม่ได้วัด8คนขึ้นไปในdirectbenchmark ไม่อ้างว่า6เป็นmaximumของOllama

หลักฐาน: [MODEL_LOAD_summary.json](<C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r51_llm_benchmark_20261009_173746_93dfb5\MODEL_LOAD_summary.json>) และ [MODEL_LOAD_raw.jsonl](<C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r51_llm_benchmark_20261009_173746_93dfb5\MODEL_LOAD_raw.jsonl>)

## 5. พบปัญหาอะไรจากคำถามจริง

16คำถาม validผ่านเว็บ ส่งgeneratedanswerออก6/16 อีก10คำถามเป็นclarification/noanswer ต้องแยกguard/renderer/outputvalidator/LLMtimeout; ไม่รายงาน16/16เพียงเพราะHTTP200

| ตัวอย่าง | พฤติกรรม/เหตุผลในlog | ควรเป็นอย่างไร |
|---|---|---|
| Explain network latency... | โมเดลสร้าง37tokensเสร็จ6.24s; providerload5.39s; generationcontractผ่าน แต่ downstreamvalidation expected fact/summary actual controls/how_to/list แล้วdiscard | อธิบายnetworklatencyจากmodelknowledgeโดยระบุขอบเขตทั่วไป ไม่ต้องมีsourceศูนย์ |
| Compare TCP and UDP ... each | conversation_scope_clarificationก่อนpipeline | เป็นcomparisonของTCP/UDP ไม่ใช่allบริการ; conversation_plan ALLจับ eachโดยไม่ต้องscopeบริการ |
| Why can high frame rate... | protected_price_missing_serviceก่อนLLM | อธิบายframepacing; price triggerจับ rate แม้เป็นframe rate |
| Box A/B ... each box | conversation_scope_clarificationก่อนLLM | A=5,B=3; eachหมายถึงแต่ละกล่อง ไม่ใช่บริการ; ไม่ใช่เพราะsubstringballตรงall (regexมีwordboundary) |
| Translate Thai sentence ... English | english_clarification/wronglayout | คำถามตั้งใจผสมสองภาษาเพื่องานแปล ไม่ควรเป็นlayouterrorเสมอ |
| Give three steps ... | english_no_answerก่อนgeneration | ขั้นตอนtouchtypingตามคำสั่ง; English directgeneral gateไม่ครอบคลุมสำนวนนี้ |
| Write invitation ... study session | english_no_answerหมวดreservation | creationโดนsemantic/sessionคำทั่วไปของreservation; ควรสร้างข้อความ2ประโยคโดยไม่แต่งข้อเท็จจริง |
| RAM vs SSD500คำ TH | generationprofile tradeoffs112token, done_reasonlength, outputcontractปฏิเสธ | ถ้ารองรับlonganswerต้องมีprofileตามความยาวจริง พร้อมrequiredcontentและbudget |
| network500words EN | general_concise128token ตัดเหลือ2ประโยค | ไม่ถือว่าทำคำขอ500คำครบ แม้modegeneralLLMผ่าน |
| touchtyping TH | acceptedแต่ตอบฝึกคลิกปุ่มตัวอักษร ไม่ได้ให้ขั้นตอนtouchtypingชัด | ฝึกตำแหน่งนิ้วแถวเหย้า พิมพ์โดยไม่มองแป้น ฝึกความแม่นแล้วเพิ่มความเร็ว; availabilityไม่ได้ตรวจsemanticนี้ |
| ping TH / ballsTH | generalfallbackมีTimeoutErrorจริงและllm_callว่างเมื่อexcept; finalHTTP200noanswer | แยกโมเดลหมดเวลาจากsourceไม่มีข้อมูล; exceptionควรคงtimingmetadataเพื่อวิเคราะห์ง่าย |

confidence0.58ของgeneralfallbackและ0.30ของvalidationfailedในtraceไม่ใช่probabilityความถูกต้อง ไม่ควรใช้แทนoracle สองชั้นอาจตัดสินต่างกัน จึงต้องดูfinalmode/source/answerและเหตุปฏิเสธร่วมกัน

Englishที่ผู้ใช้เคยยืนยันผ่านคือชุดข้อมูล/Flowบริการเดิม รอบนี้เป็นgeneral/creation/translationใหม่ พบข้อจำกัดเพิ่ม ไม่แก้approvedsourceเดิมหรือยกเลิกคำยืนยันเก่า

คำถาม คำตอบ และtraceที่อ่านได้: [QUESTIONS_ANSWERS_R51.md](<C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r51_llm_benchmark_20261009_173746_93dfb5\QUESTIONS_ANSWERS_R51.md>)

## 6. ที่มาของเวลาช้า

1. การสร้างoutputจำนวนมาก: longcap512ประมาณ9s; cap256ประมาณ4.5s; actualdecodeประมาณ50–60tokens/sส่วนใหญ่ตามprovider แต่ไม่ใช่อัตรารวมทุกrequestที่รอคิว
2. Queue: longNคำขอช่วงเดียวกันเวลาtailใกล้N×9s และTTFTของคนท้ายช้า ทั้งที่generateต่อrequestใกล้เดิม
3. Model admission/context/providerload: latencyENตัวหนึ่ง6.24sมีproviderload5.39s จึงไม่ใช่decodeทั้งหมด ไม่ยืนยันว่าphysicalreloadหรือcontextswitchโดยไม่มีrunnerlog
4. Pipelinecost: translationTH15.04sแต่generalgeneration0.69s เพราะRAGmiss/ขั้นตอนก่อนหน้า; แสดงว่าปรับmodelอย่างเดียวไม่ลดทุกtail
5. Routing/guard/outputcontract: หลายคำถามจบเร็วด้วยคำชี้แจงหรือnoanswer ไม่ใช่LLMตอบเร็วสำเร็จ
6. Healthข้อมูลgeneral_timeout_sec4.0ต่างจากtracegeneralcalltimeout15.0 ในรุ่นนี้ ต้องอ้างtraceคำขอจริง/อ่านcodeแทนการใช้healthfieldเดียว; ไม่เปลี่ยนruntimeในงานวัด

## 7. สภาพเครื่อง/ข้อจำกัด

RTX4050Laptop6GB; GPUmeasurementในartifact; RAMตอนเริ่มประมาณ87% เหลือ1.95GB (ก่อนหน้าr50เครื่องมีRAMว่างมากกว่า) model/embeddingโหลดอยู่ เหล่านี้เป็นmeasurementของเครื่องนี้ขณะนั้น ไม่เปรียบเทียบperfเป็นผลจากcodefixโดยตรง

ไม่ได้controlcoldstart/cache/thermalpower/backgroundappsทุกตัว ไม่ได้testCPU-onlyเครื่องอื่น ไม่ได้testWordPressพร้อมโหลด ไม่ได้testhumansemanticทุกคำตอบ p95samplesน้อย; ฟังก์ชันoutputcapและpromptต่างกันระหว่างchatกับdirectอย่างตั้งใจและมีoptionsบันทึก

## 8. งานแก้ถัดไปจากหลักฐาน ถ้าจะปรับผลิตภัณฑ์

1. P0 domain/scope: จำกัด all/each/rate ตามnoun/operation+บริบท ไม่ดักคำถามใหม่ที่ครบก่อนgeneralLLM; negativefixtureTCP/frame rate/eachbox
2. P0 validation: แยกgeneralmodelknowledgeจากsource-groundedstudioanswer ตรวจcontentcontractตามงานแทนcategoryคำผิวเผิน; อย่าปิดvalidatorทั้งหมด
3. P1 English/generaltranslation: clear-general gateและmixed-languageตามtranslationtask; fixtureอังกฤษที่ก่อนหน้าไม่ถึงgeneration
4. P1 requestedformat: generationprofileสั้น/กลาง/ยาวตามคำสั่งจริง จำกัดtokenอย่างมีเหตุผลพร้อมแจ้งผลpartial; บนGPUนี้long512ขีดเวลา9sเมื่อไม่รอ
5. P1 observability: คงllmmetadataเมื่อตั้งแต่except และใช้timeouthealthสอดคล้องtrace; แยกโมเดลล่มจากไม่มีsource
6. P2 performance: stageprofilingRAGmiss/intent/context reuse, queueSLA และstreamingสำหรับงานยาว; ถ้ารับคิว6longต้องรองรับเวลาtail~55sก่อนคิดปรับdeadline ไม่ใช่เพิ่มworkersโดยเดา

รอบนี้เก็บรายการเหล่านี้ไว้ ไม่แก้ระบบขณะวัดเพื่อรักษาการเปรียบเทียบ; state/logรุ่นก่อนคงอยู่

## 9. ปริมาณหลักฐานและการแก้เครื่องมือวัด

- Valid chatprobe16 + chatload52 + directprobe20 + directload52 = 140คำขอที่ใช้สรุป; chatloadaccepted29/52 HTTP {'200': 29, '503': 23}
- Firstinstrumentprobe16ไม่ได้ส่งexperimental_rag_fallback=trueซึ่งapp.jsส่งจริง จึงเก็บแยกเป็นdiagnostic ไม่ใช้สรุปgeneralgenerationcapacity ไม่ใช่ผลหน้าเว็บจริง
- Earlygenerated_answerfieldในV2นับmodeltextที่ถูกvalidatorปฏิเสธด้วย แก้classificationตามfinalmode/traceในไฟล์derived ไม่แก้rawnetworkrecords: [CHAT_PROBE_CORRECTED_CLASSIFICATION.json](<C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r51_llm_benchmark_20261009_173746_93dfb5\CHAT_PROBE_CORRECTED_CLASSIFICATION.json>)
- CPUCIMreadถูกsandboxปฏิเสธ จึงไม่แต่งCPUmodel; GPUข้อมูลจากnvidia-smiได้ ไม่จำเป็นต้องยกสิทธิ์เพื่อวัดคำขอ
- Performance/log/stateเกิดใหม่จากคำขอทดสอบตามปกติ ไม่มีreset/deleteของเก่าหรือปรับไฟล์เจ้าของ

Totals: [MEASUREMENT_TOTALS_R51.json](<C:\Users\Chokhun\Documents\Codex\2026-09-25\psu-esports-studio-phuket-chatbot-c-2\r51_llm_benchmark_20261009_173746_93dfb5\MEASUREMENT_TOTALS_R51.json>)
