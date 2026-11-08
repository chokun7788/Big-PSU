import json,collections,statistics,math,re,urllib.request,hashlib
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r51_current_path.txt').read_text());OLD=Path((BASE/'r50_current_path.txt').read_text())
def read(name):return json.loads((OUT/name).read_text(encoding='utf-8'))
def write(name,obj):
 with (OUT/name).open('x',encoding='utf-8') as f:f.write(obj if isinstance(obj,str) else json.dumps(obj,ensure_ascii=False,indent=2))
def link(name):return f'[{name}](<{OUT/name}>)'
probe=read('CHAT_PROBE_V2_summary.json');chat=read('CHAT_LOAD_summary.json');mp=read('MODEL_PROBE_summary.json');ml=read('MODEL_LOAD_summary.json')
def accepted(x):return 'general_llm' in x['response'].get('mode','') and 'unavailable' not in x['response'].get('mode','')
accepted_rows=[x for x in probe['results'] if accepted(x)]
errors=[]
for x in probe['results']:
 traces=x['response'].get('trace',[])
 errors.append(dict(kind=x['kind'],locale=x['locale'],question=x['payload']['question'],accepted_generated=accepted(x),elapsed_sec=x['elapsed_sec'],mode=x['response'].get('mode'),llm_calls=x.get('llm_calls',[]),failure_events=[t for t in traces if t.get('decision') in ['failed','general_rag_miss_llm_unavailable','english_no_answer','english_clarification'] or 'clarification' in t.get('stage','')]))
write('CHAT_PROBE_CORRECTED_CLASSIFICATION.json',dict(total=len(probe['results']),accepted_generated=len(accepted_rows),note='Final mode determines accepted output. Early probe generated_answer also counted model text later rejected by validation; raw evidence remains unchanged.',results=errors))
def fmt(x):return f'{x:.2f}' if isinstance(x,(int,float)) else '—'
ct=['| ชุดผ่านเว็บ | พร้อมกัน | คำตอบ LLM ที่ส่งสำเร็จ/คำขอ | p50 (s) | p95 (s) | HTTP503 | PIDเปลี่ยน |','|---|---:|---:|---:|---:|---:|---|']
for x in chat['profiles']:ct.append(f"| {x['profile']} | {x['users']} | {x['generated_ok']}/{x['requests']} | {fmt(x['successful_latency']['p50'])} | {fmt(x['successful_latency']['p95'])} | {x['status_counts'].get('503',0)} | {'ใช่' if x['worker_pids_before']!=x['worker_pids_after'] else 'ไม่'} |")
mt=['| โมเดลโดยตรง | พร้อมกัน | มี done/คำขอ | p50 จบข้อความ (s) | p95 จบข้อความ (s) | p95 tokenแรก (s) | จบภายใน20s | ชน token limit |','|---|---:|---:|---:|---:|---:|---:|---:|']
for x in ml['profiles']:mt.append(f"| {x['profile']} | {x['users']} | {x['completed']}/{x['requests']} | {fmt(x['latency']['p50'])} | {fmt(x['latency']['p95'])} | {fmt(x['first_token']['p95'])} | {x['under_product_20sec']}/{x['requests']} | {x['truncated']} |")
pt=['| แบบคำถาม | ภาษา | token cap | context เพิ่ม(chars) | เวลาจบ (s) | tokenแรก (s) | output tokens | tokens/s | เหตุจบ |','|---|---|---:|---:|---:|---:|---:|---:|---|']
for x in mp['results']:pt.append(f"| {x['kind']} | {x['locale']} | {x['num_predict']} | {x['synthetic_context_chars']} | {fmt(x['elapsed_sec'])} | {fmt(x['first_token_sec'])} | {x['tokens']} | {fmt(x['tokens_per_sec'])} | {x['done_reason']} |")
details=['# คำถามและคำตอบจริงในการทดสอบ LLM r51','\n2026-10-09 Asia/Bangkok · ไม่ถือว่า HTTP200 หรือ done=true เป็น semantic correctness\n','## ผ่านเว็บแชท 16 คำถาม']
for x in probe['results']:
 details += [f"### {x['kind']} / {x['locale']}",f"\nคำถาม: {x['payload']['question']}\n",f"เวลา {x['elapsed_sec']:.2f}s · mode `{x['response'].get('mode')}` · accepted model output {accepted(x)}\n",'คำตอบ:\n\n'+x['response'].get('answer',''), '\nเหตุการณ์ที่เกี่ยวข้อง:\n']
 for t in x['response'].get('trace',[]):
  if t['stage'] in ['experimental_rag_fallback','validation','bilingual_route','tool_router']:
   details.append(f"- `{t['stage']}/{t['decision']}` confidence={t.get('confidence')} — {t.get('detail')}")
 details.append('')
details.append('## โมเดลโดยตรง 20 คำถาม/การตั้งค่า')
for x in mp['results']:
 details += [f"### {x['kind']} / {x['locale']} / cap {x['num_predict']} / context {x['synthetic_context_chars']} chars",f"\nคำถาม: {x['question']}\n",f"เวลา {x['elapsed_sec']:.2f}s · first token {fmt(x['first_token_sec'])}s · {x['tokens']} tokens · done_reason `{x['done_reason']}`\n",x['answer'],'']
write('QUESTIONS_ANSWERS_R51.md','\n'.join(details))
chatraw=[json.loads(l) for l in (OUT/'CHAT_LOAD_raw.jsonl').read_text(encoding='utf-8').splitlines()]
modelraw=[json.loads(l) for l in (OUT/'MODEL_LOAD_raw.jsonl').read_text(encoding='utf-8').splitlines()]
model_lengths=collections.Counter(x['done_reason'] for x in mp['results']);load_lengths=collections.Counter(x['done_reason'] for x in modelraw)
stats=dict(valid_chat_probe=16,chat_load_requests=len(chatraw),chat_load_accepted=sum(x['generated_answer'] and x['transport_ok'] for x in chatraw),chat_load_http=collections.Counter(str(x['status']) for x in chatraw),direct_probe_requests=len(mp['results']),direct_probe_done_reasons=dict(model_lengths),direct_load_requests=len(modelraw),direct_load_completed=sum(x['completed'] for x in modelraw),direct_load_done_reasons=dict(load_lengths),accepted_probe_elapsed=[x['elapsed_sec'] for x in accepted_rows],scope='Model completion/availability timing only; no exhaustive semantic pass count')
write('MEASUREMENT_TOTALS_R51.json',stats)
report=f'''# LLM บนเครื่องผู้ใช้: เวลา คิว และปัญหาที่พบ r51

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

{chr(10).join(ct)}

Highest tested all-available level=2คำขอพร้อมกัน ยังไม่ได้วัด3คนจึงไม่อ้างmaximum2คนแบบตายตัว ระดับที่ผ่านคือavailabilityใน2waves ไม่ใช่capacityรับรองระยะยาว

ที่4standardมีคำตอบหนึ่งใช้17.30s (translationหลังRAGmiss) ส่วนคำขออื่นถูก503จากqueuewait คิว3sตัดคำขอได้ก่อนdeadline20s แม้modelยังตอบทีละคำขอได้ รายละเอียดเวลาLLMและpipelineอยู่rawtrace

หลักฐาน: {link('CHAT_LOAD_summary.json')} และ {link('CHAT_LOAD_raw.jsonl')}

## 3. โมเดลโดยตรง: เวลาแต่ละประเภท/ความยาว

{chr(10).join(pt)}

Done reasons: {dict(model_lengths)}. คำขอ500คำทุกcapในการทดสอบนี้ชนlength แม้512tokenใช้9s ก็ไม่ได้ตอบ500คำครบ ไทยtokenไม่เท่ากับคำ จำนวนoutputtokensจริงและdone_reasonต้องอ่านร่วมกับเวลา

syntheticcontext5000charsไม่ได้เป็น5000tokens providerรายงานprompt_eval_countในraw เพิ่มcontextส่งผลต่อpromptprocessing/firsttokenและcache แต่2ตัวอย่างไม่พออ้างเส้นเวลาlinearทุกcontextlength

หลักฐาน: {link('MODEL_PROBE_summary.json')} และ {link('MODEL_PROBE_raw.jsonl')}

## 4. ถ้าทุกคำขอเข้าที่โมเดลพร้อมกัน

{chr(10).join(mt)}

ทุกคำขอdirectจบstreamได้ {stats['direct_load_completed']}/{stats['direct_load_requests']} ภายในbudgetวัด60s แต่จำนวนที่ตรง20sต่างกัน และ {dict(load_lengths)}. จำนวนdoneไม่ใช่จำนวนคำตอบcompleteตามคำขอ

Long6คน: p50จบ31.83s/p95 54.54s, p95tokenแรก45.60s; เพียง4/12คำขอจบไม่เกิน20s ข้อจำกัดของwebจะเกิดก่อนรอถึง54sเพราะqueuewait3sและdeadline20s

Short6คนทุกคำขอจบไม่เกิน20sในdirecttestนี้ แต่ผ่านเว็บไม่ได้6ครบเพราะผ่านstageอื่น/queuepolicyด้วย ยังไม่ได้วัด8คนขึ้นไปในdirectbenchmark ไม่อ้างว่า6เป็นmaximumของOllama

หลักฐาน: {link('MODEL_LOAD_summary.json')} และ {link('MODEL_LOAD_raw.jsonl')}

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

คำถาม คำตอบ และtraceที่อ่านได้: {link('QUESTIONS_ANSWERS_R51.md')}

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

- Valid chatprobe16 + chatload{len(chatraw)} + directprobe20 + directload{len(modelraw)} = {16+len(chatraw)+20+len(modelraw)}คำขอที่ใช้สรุป; chatloadaccepted{stats['chat_load_accepted']}/{len(chatraw)} HTTP {dict(stats['chat_load_http'])}
- Firstinstrumentprobe16ไม่ได้ส่งexperimental_rag_fallback=trueซึ่งapp.jsส่งจริง จึงเก็บแยกเป็นdiagnostic ไม่ใช้สรุปgeneralgenerationcapacity ไม่ใช่ผลหน้าเว็บจริง
- Earlygenerated_answerfieldในV2นับmodeltextที่ถูกvalidatorปฏิเสธด้วย แก้classificationตามfinalmode/traceในไฟล์derived ไม่แก้rawnetworkrecords: {link('CHAT_PROBE_CORRECTED_CLASSIFICATION.json')}
- CPUCIMreadถูกsandboxปฏิเสธ จึงไม่แต่งCPUmodel; GPUข้อมูลจากnvidia-smiได้ ไม่จำเป็นต้องยกสิทธิ์เพื่อวัดคำขอ
- Performance/log/stateเกิดใหม่จากคำขอทดสอบตามปกติ ไม่มีreset/deleteของเก่าหรือปรับไฟล์เจ้าของ

Totals: {link('MEASUREMENT_TOTALS_R51.json')}
'''
write('LLM_TIMING_REPORT_R51.md',report)
with urllib.request.urlopen('http://127.0.0.1:8091/health',timeout=10) as r:health=json.load(r)
release=Path((OLD/'release_r50_2_path.txt').read_text());frozen=read('ENVIRONMENT_BEFORE.json')['health']['runtime']['version'];original=json.loads((OLD/'SOURCE_RELEASE_AUDIT_R50.json').read_text());root=Path('C:/Users/Chokhun/Downloads/Learn-LLM/18_PSU_Esports_Update_Route_Data')
code_equal={rel:hashlib.sha256((root/rel).read_bytes()).hexdigest()==hashlib.sha256((release/rel).read_bytes()).hexdigest() for rel in original['checks']}
assert all(code_equal.values());assert health['runtime']['version']==frozen
write('FINAL_ENVIRONMENT_AND_AUDIT_R51.json',dict(health=health,source_release_unchanged=code_equal,source_files_checked=len(code_equal),runtime_version_unchanged=True,document_links_exist=all(Path(t).exists() for t in re.findall(r'\]\(<([^>]+)>\)',report))))
print(json.dumps(dict(valid_measurement_requests=16+len(chatraw)+20+len(modelraw),accepted_chat_probe=len(accepted_rows),chat_load=stats['chat_load_http'],direct_probe=model_lengths,direct_load=load_lengths,source_equal_files=len(code_equal)),ensure_ascii=False))
