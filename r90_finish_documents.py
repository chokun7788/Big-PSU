"""Build reader-facing casebook/index from retained evidence only."""
import json,re
from pathlib import Path
B=Path(__file__).resolve().parent;R=B/'r90_full_flow_analysis_20261018';N=B/'r88_full_common_llm_20261017'
D=json.loads((R/'CASE_EVIDENCE.json').read_text('utf8'))
def local(name,label=None):return '['+(label or name)+']('+(R/name).as_posix()+')'
def write(name,s):
 with (R/name).open('x',encoding='utf8') as f:f.write(s.strip()+'\n')
def block(s):return '```text\n'+(s or '(ไม่มีคำตอบที่ส่งกลับในผลที่เก็บไว้)')+'\n```'
notes={
'K01':('เข้าใจว่าถาม “Zelda เป็นเกมอะไร” แม้คำว่า “เกมอะไร” พิมพ์ผิด ไม่ได้ถามชื่อทางการซ้ำ',
'''1. จับชื่อเกมตรงด้วย method `exact` และเลือก `game_detail_zelda_breath_of_the_wild` ถูกแล้ว
2. ส่วนที่เหลือ `คือกมอะๆร` ไม่ผ่านตัวระบุ task จึงไม่มี operation และไม่มี requested fields
3. ตัวค้นหัวข้อใน scope ไม่มี candidate ส่วนตัววางแผน LLM เสนอ field ถึง 12 ช่อง ตั้งแต่ title จนถึง source listing/zone IDs
4. JSON และ schema ผ่าน แต่ semantic guard ยังไม่ยอมรับว่ารู้เจตนาของคำผิดนี้ จึงปฏิเสธแผนด้วย `rejected_unverified_intent`
5. ทางออกจึงเป็นคำถามกลับเรื่องชื่อเกม ทั้งที่ชื่อถูกเลือกอยู่แล้ว และไม่อ่าน summary ที่มีอยู่''',
'''ฐานกลางมี summary, genre, how_to_play และ official_description เป็น known พร้อม evidence pointers อยู่แล้ว ดู DATA_INVENTORY.json/example_records จึงยืนยันได้ว่าเคสนี้ไม่ใช่ย้ายเนื้อหาเกมไม่มา สาเหตุประกอบกันคือ task recovery ไม่พอ + model เสนอเกินโจทย์ + guard ต้องการหลักฐานเจตนาที่ชั้นก่อนหน้ายังให้ไม่ได้''',
'''ควรตอบสรุปจาก summary ว่าเป็นเกมผจญภัยโลกเปิดที่สำรวจ ต่อสู้ แก้ปริศนา และทดลองวิธีผ่านสถานการณ์ได้ แล้วเสริมแนวเกมเมื่อเหมาะสม ไม่จำเป็นต้องคืนทุก field ที่โมเดลเสนอ แก้ที่การกู้ task cue และ contract ของ game overview โดยคงการป้องกันชื่อเกม/ตัวเลข/field ที่ไม่ได้ถาม''',
'''เป็น content regression ที่มีข้อมูลรองรับ ไม่ใช่ protocol mismatch อย่างเดียว ส่วนการเปิดรับทุก field ของโมเดลจะสร้างปัญหาใหม่ จึงไม่ใช่แนวแก้ที่เหมาะสม'''),
'K03':('ถามว่าบุคคลภายนอกเข้าใช้ VR ได้หรือไม่ เป็น eligibility/policy ไม่ใช่เวลาเล่นหรือช่องจองว่าง',
'''1. พบ VR Zone และบริการ VR 30/60 นาที แต่ยังไม่มี requested fields
2. ตัวค้นหัวข้อย่อยกลับได้ candidate เรื่องสลิปผิดและเปลี่ยนเวลา ไม่ใช่ eligibility; selector เลือกว่าง จึงไม่ได้ใช้ข้อเท็จจริงจากสองหัวข้อนั้น
3. field planner รอบถัดมามี transport TimeoutError ประมาณ 8 วินาที
4. ทางออกสุดท้ายเป็นเมนู field ของ VR เช่น Service/platform/Play time/Booking occupancy''',
'''มีทั้ง candidate recall/task mismatch และ transport timeout ใน request เดียว จึงไม่ควรอธิบายว่าเกิดจาก timeout อย่างเดียว หรือกล่าวว่า LLM ไม่ได้ถูกเรียกเลย คำตอบเดิมกล่าวถึงสิทธิ์บุคคลภายนอก แต่ต้องตรวจ source ของ policy ปัจจุบันก่อนนำรายละเอียดบัตร/ขั้นตอนทุกข้อกลับมาใช้''',
'''เลือก policy การเข้าใช้ของกลุ่มบุคคลภายนอกก่อน หาก source ยืนยันให้ตอบสิทธิ์นั้นโดยตรง หากไม่มี source ให้ระบุว่าเงื่อนไขการเข้าใช้ส่วนไหนยังยืนยันไม่ได้ การขอให้เลือกเวลาเล่นไม่ช่วยตอบคำถามนี้''',
'''ตัวตรวจบางแถวมีแต่ route/outcome ไม่มี positive content assertion แม้ผ่านแถวนั้นก็ไม่ได้ยืนยันว่าตอบ eligibility ถูก'''),
'K04':('ถามนโยบายช่วง Maintenance วันศุกร์ ซึ่งควรได้เนื้อหานโยบายของหัวข้อนั้น',
'''1. จับ FAQ `migrated_faq_rule_schedule_friday_maintenance` ด้วย bounded_fuzzy และระบุ operation=policy
2. field selection ยังว่างและข้อความทั้งประโยคอยู่ใน unresolved clauses
3. LLM เลือก field `question` แทน `answer`; schema ยอมรับว่าเป็นชื่อ field ที่มีจริง
4. semantic guard ปฏิเสธ intent ที่ยังไม่ยืนยัน จึงถามกลับให้เลือก question/Confirmed information/topic''',
'''เคสนี้แสดงว่า schema ถูกไม่เท่ากับเลือกสาระถูก และการรู้ชื่อ FAQ ไม่เท่ากับอ่านคำตอบ FAQ การตอบเดิมคืนทั้งสัปดาห์ซึ่งกว้างกว่าสิ่งที่ถาม ไม่ควรคัดลอกผลเดิมทั้งก้อนเป็นเป้าหมายใหม่''',
'''อ่าน answer ของ FAQ ที่ตรงวัน/นโยบาย หากต้องกล่าวช่วงเวลาให้ใช้ schedule ปัจจุบันที่ไม่ขัดแย้งกัน จำกัดคำตอบที่วันศุกร์ และแยก Maintenance ออกจากช่องจองหรือการเปิดให้เข้าอาคาร''',
'''grades ในตัวอย่างนี้ส่วนใหญ่ตรวจ route/outcome; trace ระบุปัญหา field ได้ละเอียดกว่าคะแนนเพียงอย่างเดียว'''),
'K05':('มีสองงาน: ราคาบุคคลทั่วไปเล่น Cockpit 30 นาที และวิธีจองที่พิมพ์ขาดท้าย',
'''1. field planner เสนอข้อมูล service/inventory หลายช่อง ซึ่งไม่ตอบราคาและวิธีจองตรง ๆ
2. semantic guard ลบ field เกินโจทย์ และรักษา strong needs `amount_minor`/`duration_minutes` ไว้ได้
3. แผนได้รับการรับแบบ `typed_partial_scope` แต่ clause `how do i boo` ยังไม่ชัด
4. outer validation/dispatcher คืนคำขอให้แยกคำถามทั้งก้อน แทนการแสดงสถานะของแต่ละงาน''',
'''การมี final_plan_accepted=True ไม่รับรองว่าจะมี output ที่ใช้ได้ เพราะ outer path ยัง veto ได้ ส่วนคำว่า visiror และ boo คือคนละจุดของความผิดในประโยค ราคาก็มีประเด็น validity ร่วมอยู่ด้วย คำตอบเดิมให้แพ็กเกจ 60 นาทีและเตือนตารางหมดอายุ ไม่ได้ตอบวิธีจองครบ''',
'''แยกสถานะต่อ need: ราคาเป็น current/historical/unknown ตาม source และวิธีจองเป็น answered/clarify เฉพาะข้อความท้ายที่ยังไม่ชัด หาก intent จองกู้ได้อย่างมั่นคงให้อ่าน procedure ปัจจุบัน ห้ามแปลง 30 นาทีเป็นราคาเฉลี่ยเอง''',
'''ไม่ใช่ตัวอย่างที่เดิมตอบครบแต่ใหม่ไม่ครบเพียงฝ่ายเดียว ต้องตรวจ completeness ทั้งสองคำตอบ และตัวตรวจในแถวนี้ไม่มี positive text assertion'''),
'K06':('ถามพฤติกรรมและมารยาทผู้เล่น Tekken 8 ต้องตอบกฎเกมนี้พร้อมเงื่อนไขและโทษที่เกี่ยวข้อง',
'''ระบบเลือกกติกา Tekken 8 และส่งเนื้อหาเกี่ยวกับการไม่เคารพคู่แข่ง การเยาะเย้ย/ดูหมิ่น และการเคารพกรรมการ แต่ตัวตรวจคาดวลีอังกฤษอีกสำนวนหนึ่ง เช่น “Unsportsmanlike behavior, such as mocking, taunting...”''',
'''การไม่พบวลีที่กำหนดไม่พอจะตัดสินว่าตอบผิดเกมหรือไม่มีสาระนั้น อย่างไรก็ตามยังต้องเทียบทุก proposition และข้อยกเว้น/โทษตาม source ไม่ให้คำว่า etiquette เพียงคำเดียวทำให้ถือว่าครบทั้งคำตอบ''',
'''รักษา game/edition lock และสรุป conduct/etiquette จาก clause ที่ตรงจริง ตรวจทั้งความหมายของข้อห้าม ผู้บังคับใช้ และผลของการละเมิด ประเมินแบบ fact/condition coverage ควบคู่กับ literal โดยไม่แก้ oracle เพื่อรับทุกข้อความ''',
'''เป็นกลุ่ม clause scope หรือ wording ที่ต้องตรวจตาม source; ยังไม่ประกาศว่า semantic pass สมบูรณ์หรือ English ได้รับ owner review จากตัวอย่างเดียว'''),
'K07':('ถามระดับโซนของเกม ไม่ใช่รายการแพ็กเกจหรือสถานะจองสด',
'''เลือก game presence และบริการ Nintendo Switch แบบ 1–2/1–4 คนถูกกลุ่มแล้ว แต่ renderer แสดงเฉพาะ confirmed source scope ของบริการ ไม่แสดงชื่อ Nintendo Switch Zone ที่โจทย์คาด''',
'''ไม่ได้เปลี่ยนเกมไป PS5 และยังกันความเข้าใจผิดเรื่อง live availability แต่ระดับคำตอบ service กับ zone ต่างกัน ต้องตรวจ relation หรือ source listing ก่อน map เป็นชื่อโซน ไม่สร้าง FK จากชื่อที่คล้ายกันโดยเดา''',
'''ตอบชื่อโซนจาก relation/source ที่ยืนยัน แล้วค่อยเสริมชื่อบริการถ้าจำเป็น แยก installed/offered ออกจาก available-now''',
'''มีทั้ง literal label mismatch และ projection ระดับคำตอบ จึงไม่ควรจัดเป็น model translation failure เพียงอย่างเดียว'''),
'K08':('ถามค่าบริการ VR ของ General Student แต่มีทั้ง 30 นาทีและ 3 ชั่วโมง ต้องรักษาบทบาทของแต่ละระยะเวลา',
'''1. ระบุกลุ่มศิษย์เก่า/นักศึกษาทั่วไปและเลือก rates ของ VR ได้
2. เวลาอ้างอิงของ full run อยู่เดือนตุลาคม แต่ rates ที่เกี่ยวข้องระบุ valid ตั้งแต่ 1 ก.พ. ถึงก่อน 1 เม.ย. 2026
3. ระบบไม่แสดงตัวเลขเป็นราคาปัจจุบัน และอธิบายช่วงมีผลที่บันทึก
4. oracle ที่มองหาคำว่า บาท/ฟรี จึงให้ literal fail แม้การงดรับรองราคาปัจจุบันมีเหตุผล''',
'''คำตอบเดิมระบุชัดว่าตัวเลขเป็น recorded rates และเตือนวันหมดอายุเช่นกัน จึงห้ามเขียนว่าเดิมอ้างราคาเก่าเป็นราคาปัจจุบันโดยไม่มีคำเตือน ส่วน duration 30 นาที/3 ชั่วโมงก็ไม่ได้แปลว่า parser เดิมเลือกถูกเสมอเพียงเพราะพบคำว่าบาท''',
'''คง validity guard ถ้าต้องการราคาปัจจุบันให้ขอ source รุ่นใหม่หรือการยืนยันต่ออายุที่ระบุช่วงเวลาให้ชัด ถ้าผู้ใช้ถามราคาอดีตจึงตอบ recorded rate พร้อมวันที่ อย่าต่ออายุหรือคำนวณ duration ที่ยังคลุมเครือเอง''',
'''เป็น protective behavior ปน evaluator mismatch และความเสี่ยงเรื่อง duration ไม่ควรปิด guard เพื่อเพิ่มคะแนน; VR กันเต็มชั่วโมงเป็น occupancy อีกชั้น ไม่เปลี่ยนราคาของแพ็กเกจ'''),
'K09':('คำถามนโยบายอาหารทั่วไป ต้องได้คำตอบจาก source หรือระบุสิ่งที่ไม่ทราบ',
'''parent harness หยุด request ด้วย `TimeoutError('request watchdog 28 seconds')` ก่อนมี result สุดท้าย เกณฑ์หลายแถวของ key เดียวจึง fail เป็น pipeline_exception ทั้งหมด''',
'''นี่เป็น execution failure ที่ยืนยันได้ ไม่ใช่หลักฐานว่าไม่มีนโยบายอาหารหรือเลือกคำตอบผิด เพราะไม่มี final query plan ให้ไล่ต่อ การไม่มี observed model calls ใน row นี้ก็ไม่รับรองว่า subprocess ไม่เคยเริ่ม model request''',
'''แยกเวลารอคิว การค้น การวางแผน และการ render ให้ชัด พร้อมบันทึก checkpoint ก่อนถูก kill ถ้าตอบ policy จาก source ได้ไม่ควรต้องรอ LLM หลายชั้น นโยบายรับประทานเฉพาะพื้นที่กำหนดห้ามขยายเป็นรายละเอียดอาหารภายนอกทุกเงื่อนไขโดยไม่มี source''',
'''ไม่อ้างวิเคราะห์ exact hanging function สำเร็จจาก exception อย่างเดียว และไม่ถือ failed grade หลายแถวเป็นหลายคำถามที่ timeout'''),
'K10':('ผู้ใช้ไม่ได้ระบุเกม จึงควรถามชื่อเกมสำหรับปุ่มยิง ไม่เดาปุ่มของเกมอื่น',
'''เดิมขอชื่อเกมโดยตรง ส่วนกลางขอเกม/อุปกรณ์/หัวข้อเพิ่มแบบกว้าง ทั้งคู่ยังไม่ดึงปุ่มเกมอื่นมาตอบ แต่ oracle ต้องการหนึ่งในวลี ยังไม่แน่ใจ/ยังไม่พบ/ขอ/ไม่มี ซึ่งคำตอบกลางไม่ได้ใช้ตามรูปที่ตรวจ''',
'''การไม่มี marker ทำให้ literal fail ได้แม้หลักการถามเพิ่มมีเหตุผล ขณะเดียวกันคำขอให้เลือกอุปกรณ์หรือหัวข้อยังไม่เจาะจงเท่าเดิม จึงมี UX ที่ปรับได้จริง''',
'''ถามสั้น ๆ ว่า “หมายถึงปุ่มยิงของเกมไหนครับ?” และเก็บ pending task=controls/action=shoot ไว้ พอผู้ใช้ตอบแค่ชื่อเกมให้ resolve task เดิมและ platform ตาม source ถ้าจำเป็น''',
'''แยก “ควรถามเพิ่ม” ออกจาก “ตัวตรวจบังคับถ้อยคำ” ไม่บังคับตอบปุ่มเพื่อให้ผ่าน answer_available และไม่อ้างว่า clarification ทุกข้อเป็น bug'''),
}
lines=['# ไล่คำตอบจริงทีละขั้น: เหตุใดจึงตอบแบบนี้','',
'อ่านควบคู่กับ '+local('03_PROBLEM_ANALYSIS_ALL_TH.md','บัญชีปัญหา 37 ประเภท')+' ตัวอย่างต่อไปนี้คัดจากผลที่บันทึกไว้แล้ว ไม่ได้ส่งคำถามทดสอบใหม่ คำตอบเดิมเป็นพฤติกรรมเปรียบเทียบ ไม่ใช่ gold truth โดยอัตโนมัติ','',
'แต่ละตัวอย่างแยก **เจตนาที่ตีความจากคำถาม → แผนที่ระบบเลือกจริง → field/source → guard → output → เกณฑ์ที่ให้ไม่ผ่าน → วิธีแก้** รายละเอียด raw ทุก field เก็บใน '+local('CASE_EVIDENCE.json')+' จึงตรวจย้อนโดย key ได้','']
for ident in sorted(D):
 x=D[ident];lines+=['## '+ident+' — '+x['title'],'']
 if ident=='K02':
  lines+=['**หลักฐาน:** SESSION_TURNS.jsonl, session SF-006 ของ R88 เป็น engine session fixture; ไม่อ้างว่าเป็นบทสนทนา HTTP ของผู้ใช้จริง','']
  for t in x['session_turns']:
   lines+=['### Turn '+str(t['turn']+1),'','**ผู้ใช้**',block(t['question']),'','**คำตอบที่ส่งจริง**',block(t['result']['answer']),'']
  lines+=['### สิ่งที่ trace ยืนยัน','',
  '1. Turn แรก `PC มีอะไรบ้าง` จับ PC scope ได้ และส่ง clarification พร้อม common state ที่มี zone/service IDs กลับไป',
  '2. Turn สอง `อุปกรณ์` ไม่ได้เริ่มจากศูนย์: rejected candidate ใช้ method `typed_common_state`, platform=PC, operation=equipment และ requested fields specifications/usage',
  '3. read contract มี equipment_model fields แล้ว และ relation_edges พบ PC/monitor/mouse/keyboard/headset/gaming chair ที่ผูกกับบริการ PC',
  '4. แต่ `อุปกรณ์` ยังเหลือใน unresolved clauses จึงไม่ผ่าน `unresolved_query_clause` และ dispatcher เปลี่ยนเป็น safe generic clarification',
  '5. equipment bridge รับ grammar ของรายการอุปกรณ์แบบประโยคเต็มบางรูป แต่ bare follow-up ยังไม่ถูกผูกเป็น task เดียวกันสำเร็จ','',
  '**ข้อสรุป:** เคสนี้ไม่ใช่ประวัติไม่ถูกส่งและไม่ใช่ไม่รู้จักอุปกรณ์ทั้งหมด รากปัญหาอยู่การรับ short task/context กับการตัดสิน coverage/guard หลังได้ scope แล้ว','',
  '**ควรทำแทน:** pending request ต้องระบุ task และ allowed selection slots ไว้ เมื่อผู้ใช้เลือก “อุปกรณ์” ให้ใช้ scope PC ที่ส่งจริง แล้วอ่าน related equipment ที่มีหลักฐาน ถ้าขาดเฉพาะเครื่องหรือระดับรายละเอียดค่อยถามเฉพาะส่วนนั้น ไม่ทิ้ง task กลับเป็นคำถามทั่วไป','',
  '**ข้อจำกัด:** session นี้ไม่ได้วัดการรับหลายผู้ใช้พร้อมกัน และผล 23/24 ของ suite ไม่ได้แปลว่าทุก turn มี positive fact assertion','']
  continue
 row=x['new'];r=row.get('result') or {};a=r.get('decision_artifact') or {};p=a.get('query_plan') or {};intent,chain,evidence,fix,grade=notes[ident]
 lines+=['**Request key:** `'+row['key']+'`','', '**เจตนา/สิ่งที่ต้องรักษา:** '+intent,'','### Input และคำตอบจริง','', '**คำถาม**',block(row['question']),'','**คำตอบเดิม R64 ON**',block((x.get('old') or {}).get('answer')),'','**คำตอบกลาง R88 ON**',block(r.get('answer')),'']
 if row.get('exception'):lines+=['**Exception:** `'+row['exception']+'`','']
 lines+=['### เส้นทางตัดสินที่พบจริง','',chain,'','### เหตุและหลักฐานประกอบ','',evidence,'','### ควรตอบ/ควรแก้อย่างไร','',fix,'','### อ่านคะแนนอย่างไร','',grade,'']
 failures=[]
 for g in row.get('grades') or []:
  for reason in g.get('failures') or []:
   if reason not in failures:failures.append(reason)
 lines+=['เหตุไม่ผ่านที่บันทึกไว้ (รวมซ้ำของ key เดียวกันแล้ว):','']+['- `'+s.replace('`',"'")+'`' for s in failures]+['']
 if p:lines+=['แผนสุดท้ายที่เปิดให้อ่านได้:','', '```json',json.dumps({k:p.get(k) for k in ['method','record_ids','operation','requested_fields','unresolved_clauses','semantic_review_needed','semantic_plan_accepted']},ensure_ascii=False,indent=2),'```','']
 audits=a.get('planner_audits') or []
 if audits:
  lines+=['Planner audit ต่อ call (ไม่ใช่คะแนนความถูกต้องของคำตอบ):','','| รอบ | Transport | Schema | Final plan | Semantic/Error |','|---|---|---|---|---|']
  for i,u in enumerate(audits):lines.append('| '+str(i+1)+' | '+str(u.get('transport_ok'))+' | '+str(u.get('schema_accepted'))+' | '+str(u.get('final_plan_accepted'))+' | '+str((u.get('semantic') or {}).get('semantic_status') or u.get('error_type') or u.get('gate_reason'))+' |')
  lines+=['']
 lines+=['**ตำแหน่ง raw:** `'+x['raw_file']+'`, logical JSONL line '+str(x['raw_line'])+'; ค้น key ใน CASE_EVIDENCE.json หรือฐาน evidence เพื่อดู full trace/expected contracts','']
lines+=['## K11 — เดิมมี runtime bug จริง: ownership_blocked','',
'Legacy ON มี execution exceptions 2,694 requests โดย 2,692 เป็น NameError ของ `ownership_blocked` และอีก 2 เป็น harness_timeout_30s จุดใช้ตัวแปรอยู่ใน `retrieve_curated` แต่ assignment ที่พบอยู่ในอีก function (`retrieve_competition_fact_cards`) จึงไม่อยู่ใน local scope เดียวกัน','',
'เป็นหลักฐานว่าไม่ควรยก retrieval เดิมมาทั้งชุด การนำ behavior กลับมาควรแยก pure task interpreter ออกจาก facts provider และไม่ดึง bug/facts เก่ากลับมาด้วย จำนวนนี้เป็น requests ไม่ใช่ grade events','',
'## K12 — สถานะจอง: ผลชุดนี้ไม่ได้เป็นการพิสูจน์ว่า API สดผิด','',
'R88 ตั้ง booking=controlled_unavailable ใน corpus หลัก จึงตั้งใจไม่อ้างสถานะเครื่องสดจาก WordPress การตอบว่าไม่สามารถยืนยันสถานะใน fixture นี้ต้องแยกจาก transport จริงและ occupancy correctness','',
'ผู้ใช้เคยตรวจสถานะจริงแล้วว่าถูกต้อง ข้อนี้คงไว้เป็นข้อมูลยืนยันจากผู้ใช้ ชุดทดสอบอัตโนมัติรอบนี้ไม่ได้ยกระดับเป็นการตรวจ live ground truth ใหม่ และไม่ได้หักล้างการยืนยันเดิม','',
'การแยกชั้นที่ถูกต้องคือ **เชื่อม endpoint ได้ → response parse ได้ → target/timezone ถูก → ช่วงเวลาทับกันตาม policy ถูก → ตรง known-result fixture/สถานะจริง** แต่ละชั้นต้องมีหลักฐานของตัวเอง','',
'## วิธีใช้ตัวอย่างเพื่อแก้โดยไม่ overfit','',
'1. กำหนด task/field/condition ที่ต้องตอบจาก source ก่อนเพิ่มคำถามกลายรูป',
'2. แก้ component ที่ทำความหมายหาย ไม่เพิ่ม alias ของคำถามเต็มทีละบรรทัด',
'3. คง hard negatives เช่น คนละเกม ตัวเลขเครื่องต่างกัน นโยบายชำระเงินคนละเงื่อนไข',
'4. ตรวจ partial answer/unknown/conflict/expiry ให้เป็นสถานะที่ถูกต้อง ไม่บังคับทุกข้อเป็น answer_available',
'5. แยกผลหลังแก้จากผลเก่าที่เก็บในชุดนี้ ไม่แก้ log เดิมเพื่อให้ดูเหมือนเคยผ่าน','']
write('05_CASEBOOK_TH.md','\n'.join(lines))

readme='''# เริ่มอ่าน: วิเคราะห์ Full Flow เดิมและ Format กลาง

วันที่จัดทำ: 18 ตุลาคม 2026 — รายงานจากโค้ดและผลทดสอบที่บันทึกไว้แล้ว

## สรุปภาษาง่าย

**ปัญหาหลักไม่ใช่แค่มีข้อมูลไม่ครบ:** การเปลี่ยนเป็น Format กลางเปลี่ยนตัวตีความและตัวเลือกคำตอบด้วย ข้อมูลบางเรื่องอยู่ในฐานแล้ว แต่ระบบยังไม่รู้ว่าคำถามต้องอ่านช่องไหน หรืออ่านแล้วถูกตัวตรวจขอบเขตปฏิเสธ จึงถามซ้ำ/ตอบไม่ตรงเรื่อง

ของเดิมสะสมตัวแก้คำผิด ตัวแยกเจตนา ตัวตอบแต่ละหมวด และตัวสืบต่อบทสนทนาไว้หลายชั้น ของกลางมีข้อดีด้านข้อมูลอ้างอิงและการแก้ไขข้อมูล แต่ยังไม่ได้รับพฤติกรรมเหล่านั้นมาครบ การย้ายข้อมูลอย่างเดียวจึงไม่ทำให้ตอบดีเท่าเดิมทันที

**แนวแก้ที่เสนอ:** ใช้ตัวตีความงานและตัวประกอบคำตอบที่เหมาะกับแต่ละหมวด โดยอ่านข้อเท็จจริงจากฐานกลางปัจจุบัน แล้วตรวจเงื่อนไข แหล่งที่มา และวันมีผล ไม่คัดลอกคำตอบราคา/นโยบายเก่ามาทับฐานใหม่

## อ่านตามลำดับนี้

{NAV}

## ผลเทียบที่ใช้เกณฑ์เดียวกัน

| ตัวชี้วัด | เดิม R64 + LLM ON | กลาง R88 + LLM ON |
|---|---:|---:|
| คำขอไม่ซ้ำ / เกณฑ์ประเมิน |20,554 /55,811|20,554 /55,811|
| Positive literal: มีข้อความที่เกณฑ์กำหนด |94.41%|72.10%|
| เกณฑ์เดิมทั้งหมด รวม route/intent/status |76.33%|9.02%|

**9.02% ไม่ใช่ความถูกต้องของเนื้อหา 9.02%** เพราะรวมสัญญา route/format เดิมซึ่งใหม่ใช้ต่างกัน ส่วน 72.10% ก็ไม่ใช่การรับรองความหมายทั้งคำตอบ: คำแปลต่างสำนวน การป้องกันราคาเก่าที่หมดอายุ หรือเกณฑ์ที่ตรวจแค่คำเดียว ยังต้องอ่านแยก

รายละเอียดไทย/อังกฤษ/auto และข้อจำกัดอยู่ในรายงาน 03 การเปรียบเทียบนี้ใช้คำตอบที่เก็บไว้แล้ว ไม่มีการเรียก chatbot หรือ LLM รอบใหม่

## อ่านคำศัพท์ในรายงาน

| คำ | ความหมายในระบบนี้ |
|---|---|
| entity / target | สิ่งที่ถามถึง เช่น PC, VR, เกม Tekken 8 |
| task / intent / operation | ต้องการทำอะไรกับสิ่งนั้น เช่น ถามราคา ปุ่ม กติกา สิทธิ์เข้าใช้ |
| field | ช่องข้อมูล เช่น summary, answer, amount_minor |
| relation / join | ความสัมพันธ์ เช่น เกมนี้มีบนบริการใด หรือโซนนี้มีอุปกรณ์ใด |
| clause / need | ส่วนย่อยของคำถาม หรือเนื้อหาหนึ่งข้อที่คำตอบต้องครอบคลุม |
| contract | เงื่อนไขที่ต้องรักษา เช่น เกมถูกตัว กลุ่มราคาถูก ระยะเวลาถูก ต้องไม่ตอบเกิน source |
| schema accepted | รูปแบบ/ชื่อช่องถูกกฎ ยังไม่แปลว่าความหมายถูก |
| semantic accepted | ยอมรับการตีความตาม guard ของระบบ ยังไม่เท่ากับมนุษย์รับรองคำตอบ |
| projection | เลือกว่าจะแสดง field หรือ related records ใดเพื่อให้ตรงคำถาม |
| guard / veto | ตัวตรวจที่หยุดหรือเปลี่ยนผลเมื่อไม่ผ่านเงื่อนไข |
| source / evidence | ข้อมูลต้นทางและจุดที่ตรวจย้อนยืนยันค่าได้ |
| validity | ช่วงวันที่ข้อมูลมีผล เช่น ราคาถึงก่อนวันที่กำหนด |
| protocol mismatch | ชื่อ route/intent/status/รูปแบบไม่ตรงเกณฑ์เดิม ต้องแยกจากสาระ |
| grade / request / call / audit event | หน่วยต่างกัน: เกณฑ์หนึ่งข้อ / คำขอไม่ซ้ำ / การเรียกโมเดล / เหตุการณ์ตรวจแผน |

## หลักฐานทุกกรณี ไม่ได้เลือกเฉพาะตัวอย่าง

{EVIDENCE}

ดัชนีเก็บทุก request ที่ไม่ผ่านอย่างน้อยหนึ่ง raw grade: กลาง 18,824 และเดิม 5,689 รายการ เหล่านี้ไม่ใช่จำนวนคำตอบผิดสาระที่มนุษย์ยืนยันแล้ว แต่ใช้ตาม key กลับไปตรวจคำถาม คำตอบ และเกณฑ์ได้ครบ

## ระดับข้อสรุปและขอบเขต

- **ยืนยันแล้ว:** เห็นเงื่อนไขในโค้ด ค่าในฐาน หรือแผน/คำตอบใน log ตรงกัน
- **สมมติฐานรายกลุ่ม:** อาการที่จัดอัตโนมัติ ยังต้องอ่าน source/trace ก่อนตัดสินรายคำถาม
- **การป้องกันที่อาจถูกต้อง:** ข้อมูลหมดอายุ ไม่ทราบ หรือ fixture ตั้งใจปิด live
- **ความเสี่ยงที่ยังไม่ตรวจ:** package/published deployment/ขอบเขตใหม่ที่ยังไม่มีผลรองรับ

Flow 01/02 อธิบาย **ระบบที่มีอยู่จริงใน snapshot** ส่วน Flow 04 เป็น **ข้อเสนอการซ่อม** ยังไม่ได้ติดตั้งจากงานเอกสารนี้ รายงานไม่อนุมัติ draft แทนเจ้าของ และไม่สร้างนโยบายที่ไม่มีแหล่งข้อมูล

งานนี้สร้างเอกสารและดัชนีใหม่ในโฟลเดอร์ R90 เท่านั้น ไม่รันชุดทดสอบใหม่ ไม่แก้ production code/data/approval และไม่เขียนทับ log เดิม Source hashes และการตรวจเอกสารดู DELIVERY_QA.json / DOCUMENT_REVIEW.md
'''
nav=[('01_FULL_FLOW_LEGACY_TH.md','1. Full Flow เดิม — input, session, คำผิด, routing, handlers, retrieval/LLM, output และการแก้ข้อมูล'),('02_FULL_FLOW_COMMON_TH.md','2. Full Flow กลาง — เจ้าของกรอก/แก้/เผยแพร่, preview, ข้อมูล 21 หมวด, interpretation, LLM/guard, joins และ output'),('03_PROBLEM_ANALYSIS_ALL_TH.md','3. ปัญหา 37 ประเภท — อาการ เหตุ หลักฐาน ผลที่ควรได้ แนวแก้ วิธีตรวจ และสิ่งที่ต้องใช้มนุษย์'),('04_FLOW_GAP_AND_REPAIR_TH.md','4. เทียบ Flow และแผนซ่อม — จุดต่างรายชั้น พร้อม target flow และลำดับทำงาน'),('05_CASEBOOK_TH.md','5. เจาะคำตอบจริง 12 กรณี — เหตุใดจึงเลือกแบบนี้ สิ่งที่ควรตอบ และข้อจำกัดของคะแนน'),('06_DATA_AND_OWNER_DECISIONS_TH.md','6. ความพร้อมข้อมูล — อะไรทำเองได้ อะไรต้องถามเจ้าของ และคำถามที่เจาะจง')]
ev=[('COMMON_FAILURE_INDEX_ALL.md','ดัชนี raw-failed requests กลางทั้งหมด'),('LEGACY_FAILURE_INDEX_ALL.md','ดัชนี raw-failed requests เดิมทั้งหมด'),('ALL_FAILURE_REASON_TYPES.md','เหตุไม่ผ่านทุกข้อความ: กลาง 620 ชนิด / เดิม 318 ชนิด'),('CASE_EVIDENCE.json','คำตอบเต็มและ trace ของตัวอย่าง'),('PROBLEM_CATALOG_REVIEWED.json','บัญชีปัญหารุ่นตรวจทาน'),('DATA_INVENTORY.json','รายการข้อมูล/ข้อขัดแย้ง/จุดภาษาอังกฤษที่ยังว่าง'),('DOCUMENT_REVIEW.md','ผลตรวจทานเอกสารและข้อจำกัด')]
readme=readme.replace('{NAV}','\n\n'.join('- '+local(p,l) for p,l in nav)).replace('{EVIDENCE}','\n\n'.join('- '+local(p,l) for p,l in ev))
write('README_TH.md',readme)
print('Wrote casebook and reading index; no chatbot or model calls')
