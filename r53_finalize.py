import json,hashlib,datetime
from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r53_current_path.txt').read_text());ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');NEW=OUT/'candidate_r53_3/PSU_Esports_Chatbot_Local'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
before=json.loads((OUT/'before_hashes.json').read_text());changed=[];owner=[]
for relative,old in before.items():
 p=ROOT/relative;current=sha(p) if p.exists() else None
 if current!=old:changed.append(relative)
 if relative.startswith(('data/curated/','data/rules/','booking_dashboard/')):owner.append(dict(path=relative,unchanged=current==old))
parity=[]
for folder in ('app','web_chat','tests','data/general_evidence'):
 for p in (ROOT/folder).rglob('*'):
  if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc':
   q=NEW/p.relative_to(ROOT);parity.append(dict(path=p.relative_to(ROOT).as_posix(),same=q.exists() and sha(p)==sha(q)))
audit=dict(snapshot_files=len(before),changed_existing=changed,owner_files_checked=len(owner),owner_files_unchanged=all(r['unchanged'] for r in owner),owner=owner,candidate_source_parity=all(r['same'] for r in parity),parity=parity,git_status='metadata checkout path broken before edits; no reset/repair attempted',old_logs='existing logs were not overwritten or deleted; snapshot excluded logs; new results stored separately',runtime='2026.10.09-semantic-r53.3')
with (OUT/'PRESERVATION_AUDIT.json').open('x',encoding='utf-8') as s:json.dump(audit,s,ensure_ascii=False,indent=2)
allrows=[]
for label in ('web_before','web_after_r53_1','web_final_r53_2','web_repair_r53_3'):
 rows=json.loads((OUT/(label+'.json')).read_text());allrows.append((label,rows))
text='# คำถาม คำตอบ และเหตุผล r53\n\nข้อมูลนี้มาจากเว็บจริงบนเครื่องผู้ใช้ /api/chat/jobs และ trace ไม่ใช่คำตอบจำลอง ไม่นับ transport complete เป็น semantic correctness รายการ bounded clean เป็นเพียงไม่มีข้อผิดพลาดที่ตัวตรวจชุดนี้จับได้\n\n'
for label,rows in allrows:
 text+=f'## {label}\n\n'
 for n,r in enumerate(rows,1):
  result=r['job'].get('result') or {};calls=[t.get('metadata',{}).get('llm_call') for t in result.get('trace',[]) if t.get('metadata',{}).get('llm_call')];m=calls[-1] if calls else {}
  text+=f"### {n}. {r['question']}\n\n- input locale: {r['locale']}\n- mode: {result.get('mode')}\n- เวลา: {r['elapsed_sec']:.2f} วินาที; transport complete: {r['transport_completed']}; model answer: {r['model_answer_delivered']}\n\n**คำตอบจริง**\n\n{result.get('answer','')}\n\n"
  compact={k:m.get(k) for k in ('llm_provider_attempted','ollama_done','ollama_done_reason','llm_output_contract_ok','llm_output_rejected_reason','llm_failure_reason','llm_first_token_ms','llm_partial_response_chars','llm_output_word_count','llm_word_count_verified','llm_semantic_quality') if k in m}
  if 'llm_repair' in m:compact['repair']={k:m['llm_repair']['initial_call'].get(k) for k in ('llm_output_rejected_reason','llm_rejected_draft')};compact['repair']['attempts']=m['llm_repair']['attempts']
  text+='**เหตุผลจาก trace**\n\n```json\n'+json.dumps(compact,ensure_ascii=False,indent=2)+'\n```\n\n'
  if m.get('llm_rejected_draft'):text+='**ร่างที่ถูกปฏิเสธ**\n\n'+m['llm_rejected_draft']+'\n\n'
with (OUT/'QUESTIONS_ANSWERS_ANALYSIS.md').open('x',encoding='utf-8') as s:s.write(text)
summary='''# ผลการค้นและแก้ r53 — 2026-10-09

## สถานะ

ลงมือแก้ source และเปิด candidate r53.3 ที่ http://127.0.0.1:8093/ ไฟล์แพ็กเกจที่แจกคนอื่นก่อนหน้านี้ยังไม่ได้ sync เป็น r53 ใช้ candidate ของรอบนี้ทดลองได้ รายงานนี้ไม่รับรองว่าความรู้ทั่วไปหรือคำแปลทุกสำนวนถูกต้องทั้งหมด

## งานที่แก้และสาเหตุ

| ปัญหา | เหตุผลที่เคยเลือกตอบผิด | สิ่งที่แก้ |
|---|---|---|
| Translate ประโยค booking ถูกตอบกฎจอง | routing ตีความคำใน source เป็นคำถามศูนย์ก่อนระบุ translation task | route งานแปลที่มี source/target ชัดก่อน protected intent และใช้ปลายทางตามคำสั่ง |
| Wait 15 minutes ไป no_answer | การคัด general request ผ่าน guard เดิมไม่ครอบคลุม source แปล | ตรวจ task syntax ก่อน guard หมวดบริการ |
| network กลายเป็น internet | model เลือกคำใกล้เคียงและตัวตรวจเดิมดูรูปแบบอย่างเดียว | terminology/scope constraints พร้อม feedback |
| เลข/หน่วย/PC เปลี่ยน | ยังไม่มี source-output constraints | เปรียบเทียบตัวเลข หน่วย entities และ negation ที่ตรวจได้; ไม่รับ PC10 แทน PC1 |
| 15 กลายเป็นประมาณ 15 | รูปแบบและตัวเลขยังผ่าน แต่ระดับความแน่นอนเปลี่ยน | ตรวจ numeric approximation และบอกวิธีแก้ด้วยภาษาตรงไปตรงมา |
| คำเทคนิคขาดข้อยกเว้น | ไม่มี reference facts/ตรวจ contradiction ตามหมวด | context facts แยกจาก owner policy: ping, HTTP/TLS, TCP, RAM/SSD |
| meta Note/QUESTION กับคำถามกลับเกิน | prompt ชี้การคงศัพท์จน model บรรยาย prompt | ปรับ prompt และตรวจ instruction commentary/clarifying tail; literal Note ในคำแปลยังอนุญาต |
| งานคัดลอกมี note เกิน/คำชวนมีแต่คำทักทาย | provenance และ format validation ไม่รู้ชนิดงาน | ไม่เติม note ลงข้อความแปล/งานเขียนสั้น; แยก metadata; ตรวจ content sentence ของคำชวน |
| ทุก failure ถูกเข้าใจว่าโมเดลล่ม | mode legacy มี unavailable แม้ model done | เพิ่ม provider attempted/done และ failure_reason output_meaning_unverified; mode เดิมยังเก็บเพื่อ compatibility |

ไฟล์เปลี่ยน: app/pipeline/experimental_fallback.py, engine.py, query_signals.py เพิ่ม semantic_quality.py, tests/test_semantic_quality_r53.py และ data/general_evidence/technical_facts_20261009.json

## ผลแยกตามชั้น

- Fixtures bad/good เดิม: ก่อนแก้ 10/21 → หลังแก้ 21/21 → ตรวจสุดท้าย 21/21 นี่คือความถูกต้องตัวตรวจบนเคสที่กำหนด ไม่ใช่ accuracy ของผู้ใช้ทุกคำถาม
- Unit/pipeline/provider/jobs/conversation ที่เกี่ยวข้อง: ดู targeted_unit_r53_3.txt สำหรับผล source สุดท้าย; รอบก่อน 48/48 และเพิ่มหนึ่ง test อธิบาย feedback ในรอบสุดท้าย
- เว็บ baseline 6 เคส: transport 6/6, model answer 3/6; baseline เลือก subset จึงไม่เอาไปเทียบเปอร์เซ็นต์กับ 14 เคสโดยตรง
- เว็บ r53.1 14 เคส: transport 14/14, model answer 11/14; checker เดิมไม่มี error ใน 11 คำตอบ แต่ตรวจอ่านพบ addition “ประมาณ” ใน Wait 15 minutes จึงไม่นับ 11/11 เป็น semantic accurate
- เว็บ r53.2 11 เคส: transport 11/11, model answer 8/9 งาน LLM + 2/2 deterministic controls; คำแปล exact 15 ถูกปฏิเสธหลัง repair ยังเติมประมาณ เก็บ failure ไม่ยอมปล่อยเป็นคำแปลถูกต้อง
- เว็บ r53.3 5 เคสที่แก้เฉพาะ: transport/model 5/5, 0.54–1.46 วินาที; exact15/exact30/about15/คำสั่งไทย/exact PC10+negation ผ่านการอ่านตาม constraints
- ราคา PC บุคคลทั่วไปยังตอบ 70 บาท/60 นาทีจาก owner source; identification ภาษาอังกฤษยังตอบ national ID/student/school/passport จากคำตอบผู้ใช้

ผลเว็บทั้งหมด 36 requests คือ 6 baseline +14 r53.1 +11 r53.2 +5 r53.3 ไม่ใช่ 36 คำถามไม่ซ้ำและไม่ได้เป็น load test

## วิเคราะห์สิ่งที่ยังผิดหรือไม่ยืนยัน

### P1 — งานยาวภายใต้ deadline

คำถาม RAM/SSD ไทยประมาณ 500 คำได้ stream บางส่วน 1,222 characters แต่ไม่ done ภายใน 15 วินาที ระบบจึงไม่ปล่อยข้อความตัดกลางคำตอบ คำถาม DNS/TCP/TLS/HTTP อังกฤษ stream done ได้ 370 คำ ไม่ถึง minimum coverage ของคำขอ500 จึง reject ตาม requested_length_coverage_missing นี่คือสองเหตุผลต่างกัน: timeout กับ output coverage ต้องแก้ architecture long-job/deadline หรือ progressive delivery และวัด throughput ก่อน ไม่ลดเกณฑ์เพื่อให้ผลดูผ่าน ไม่ได้แก้ในรอบนี้

### P1 — การตรวจความหมายยังมีขอบเขต

negation เป็น presence check ยังแยกหลาย clause / not only / scope ไม่ได้; numbers ไม่รองรับคำเขียนเป็นตัวอักษรทุกแบบ; terminology มีเพียง concept/units ที่ระบุ; omission ของรายละเอียดอื่นยังหลุดได้ การมี keyword หรือ source URL ไม่รับรองความถูกต้องทุก claim ตัวตรวจ ping/HTTP/RAM เป็น pattern ตามข้อผิดจริง มีโอกาสทั้ง false positive และ false negative ต้องมี held-out paraphrase/contradiction set ก่อนใช้เป็นคะแนน accuracy

### P2 — source extraction และคำขอหลายงาน

รองรับ source-first และ target-first ที่มีภาษา/ขอบเขตชัด ไม่ครอบคลุมข้อความกำกวม/ไม่มี source; การแปลพร้อมถามราคาต่อในคำขอเดียวอาจมี ambiguity ยังไม่ได้ออกแบบ compositional task parser ไม่ควรอ้างว่ารองรับทุกสำนวน

### P2 — ภาษาไทยและรูปแบบคัดลอก

Thai word count ยังไม่มี tokenizer ที่ยืนยัน จึงห้ามนับ space/character แล้วอ้าง 500 คำ ภาษาไทยคำตอบ RAM สั้นบางสำนวนยังไม่ลื่น (“RAM ... สูญหาย”) ต้องปรับความชัดว่า “ข้อมูลใน RAM” แทนกล่าวตัวอุปกรณ์หาย การตัด note ใน task สำหรับ copy อยู่ใน metadata ผู้ใช้ควรเห็น provenance จาก UI แยก answer text ในงานถัดไป

### P2 — runtime และผลทดลอง

network translation อังกฤษหนึ่งครั้ง timeout ก่อน first token 15.6s; rerun r53.2 ได้คำตอบประมาณ1.44s จึงยังยืนยันสาเหตุระดับ GPU/queueไม่ได้จาก traceนี้ ไม่ตั้งชื่อว่าเป็น hallucination การทดสอบส่วนใหญ่ sequential ยังไม่วัดคุณภาพ r53 ภายใต้ concurrent workload

## การรักษาข้อมูล

snapshot before และ hashes อยู่แยกจาก source เดิม ตรวจ owner curated/rules/booking_dashboard ว่าไม่เปลี่ยนใน PRESERVATION_AUDIT.json ตรวจ source กับ candidate r53.3 ตรงกัน Git status ใช้ไม่ได้ตั้งแต่ก่อนแก้เพราะ metadata ชี้ checkout path เก่า จึงไม่อ้างว่า working tree clean ไม่ได้ reset Git ไม่ลบ log หรือแพ็กเกจเดิม

## Paper และ Flow

อ่าน 8 งานที่คัดจาก ACL/arXiv รายงานข้อจำกัดและ mapping อยู่ papers/report.md ใช้หลักการจากงานวิจัยร่วม constraints/context โดยไม่ได้ติดตั้ง xCOMET, FActScore หรือ CoVe เต็มระบบ Flow สมบูรณ์พร้อมการตรวจทานอยู่ FLOW.md ผลรายคำถามและเหตุผล trace อยู่ QUESTIONS_ANSWERS_ANALYSIS.md
'''
with (OUT/'RESULTS_ANALYSIS.md').open('x',encoding='utf-8') as s:s.write(summary)
flow_add='''

## ตรวจทานหลังลงมือจริง — Flow ฉบับใช้ต่อ

### ลำดับที่ปรับหลังพบปัญหา

raw input → detect explicit translation boundary ก่อน routing หมวดศูนย์ → แยก source กับ target language → profile budget → scoped evidence เฉพาะ factual request → generate → require provider done → shape check → meaning constraints → ถ้าพลาดและมี budget ส่งชื่อ error พร้อมคำอธิบายให้แก้เพียงครั้งเดียว → ตรวจซ้ำ → answer หรือ failure_reason ที่ระบุสาเหตุ → format provenance ตามชนิดงาน → job completed

job completed คือระบบส่งผลแล้ว อาจส่ง refusal/timeout ไม่ใช่คำตอบสำเร็จ; model done คือข้อความจาก provider จบ ไม่ใช่คำตอบถูกต้อง; semantic checks pass คือผ่านเฉพาะข้อกำหนดที่มี ไม่ใช่ทุก claim verified

### การทบทวนและผล 4 รอบ

1. Baseline: fixtures10/21 และเว็บ6เคส พบ source booking ถูกตีความเป็นนโยบายจอง รวมทั้ง no_answer ของ Wait15 เพิ่ม routing ก่อน protected intent ใน Flow
2. Implement r53.1: fixtures21/21; เว็บ14เคสมี11modelanswers; ตรวจอ่านพบ “ประมาณ” ที่ checker ยังไม่จับ และพบงานยาวไม่ครบ แยก semantic addition จาก timeout/coverage
3. Review r53.2: เพิ่ม target-first syntax, entity boundary PC1≠PC10, numeric certainty; unit48/48 และเว็บ11เคส ราคา/เอกสารยังผ่าน แต่ exact15ถูก reject หลัง repair พบชื่อรหัส error อย่างเดียวไม่ชี้วิธีแก้ชัดพอ
4. Refine r53.3: เพิ่ม feedback อธิบาย numeric certainty และ constraints อื่น; เว็บ5เคส exact15/exact30/about15/Thai command/PC10+negation ผ่าน; เพิ่ม unit แยก exact vs approximate ทั้งดี/ผิด ไม่ลด coverage criteria ของ500คำ

### งานลำดับถัดไปที่ทำเองได้

1. เส้นทาง long-job: กำหนด answer-length/deadline ตาม throughput ที่วัดจริง ใช้ queue/job polling และ explicit time limit ของงานยาว ทดสอบเฉพาะ100/300/500คำ ไทย–อังกฤษ ไม่เอาคำตอบสั้นแทนคำขอยาวแล้วบอกผ่าน
2. Expand meaning evaluation: held-out source/good/bad pairs ใส่ multiple negations, omission, numeric words, modifiers, bilingual identifiers กำหนด expected meaning ก่อนดู model answer แยก precision/coverage/false reject
3. Learnable evaluator feasibility: benchmark NLI/xCOMET offline แยก GPU generation วัดขนาด/เวลาและความน่าเชื่อถือไทย ใช้ abstain เมื่อ evaluator ไม่ชัด ไม่ใช่เพิ่มการเรียกโมเดลเองทุก request
4. Thai tokenizer: เลือก version/licence/dependency วัดหน่วยคำกับไทยผสมอังกฤษ เก็บ unknown ไว้จนวัดจริงได้
5. Clear provenance in UI: แสดง task/provider/verification status แยกจาก answer ที่ copy ได้; อย่าใช้ true accuracy badge จาก constraints_pass
6. Concurrent semantic test: เริ่ม2/4users แยก jobs capacity/admission wait/first token/answer quality และ session isolation ไม่เพิ่ม model parallelism จน memory/latency รองรับ

### เกณฑ์หยุดและคำถามเจ้าของ

รอบนี้หยุดเมื่อข้อผิดที่ยืนยันและอยู่ใน scope มี guard/repair พร้อมเทสเฉพาะและรายงานสิ่งค้าง งานยาว/semantic general ไม่ถือว่าปิดครบ ไม่มีคำถามนโยบายใหม่ที่ต้องเดาเพื่อทำ r53 ถ้าจะเปลี่ยนเงื่อนไขราคา/จองให้นอก source ต้องให้เจ้าของยืนยันตามรายการเดิม ห้ามใช้ general evidence ไปแทนนโยบายศูนย์

### เอกสารประกอบ

- papers/report.md: source links, selected papers, limits และ research→code mapping
- RESULTS_ANALYSIS.md: เหตุผลที่ยังตอบไม่ได้/ขอบเขตที่ไม่ได้แก้
- QUESTIONS_ANSWERS_ANALYSIS.md: คำถาม/คำตอบจริง/trace reasons/repair draft
- targeted_unit_r53_3.txt และ PRESERVATION_AUDIT.json: final verification / owner-data hashes / candidate parity
'''
with (OUT/'FLOW.md').open('a',encoding='utf-8') as s:s.write(flow_add)
print('owner unchanged',audit['owner_files_unchanged'],len(owner),'candidate parity',audit['candidate_source_parity'],'existing source changes',changed)
