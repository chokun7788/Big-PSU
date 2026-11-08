import json,collections,statistics
from pathlib import Path
import r49_probe as r
def read(pattern):
 p=sorted(r.OUT.glob(pattern))[-1];return p,json.loads(p.read_text(encoding='utf-8'))
def link(p):return f'[{p.name}](<{p.resolve()}>)'
sets=[read(pattern) for pattern in ['R49_BASELINE_SOURCE*summary.json','R49_FIXED_SOURCE_V1*summary.json','R49_FIXED_SOURCE_V2*summary.json','R49_FOCUS_SOURCE_FINAL*summary.json','R49_NEW_WEB_FINAL*summary.json','R49_NODEBUG_WEB_FINAL*summary.json','R49_NODEBUG_WEB_R49_2*summary.json','R49_R48_REGRESSION_WEB_FINAL*summary.json','R49_NEW_WEB_R49_2*summary.json']]
rows=['| ชุด | รุ่น / วิธี | ผ่าน / เคส | คำขอ | หลักฐาน |','|---|---|---:|---:|---|']
labels=['ก่อนแก้','แก้รอบแรก','แก้ตัวจับคำ','ตรวจขอบเขตเพิ่มเติม','เว็บ debug เปิด รุ่น r49.1','เว็บ debug ปิด รุ่น r49.1 (พบข้อผิดพลาด)','เว็บ debug ปิด รุ่น r49.2','ชุดเดิม r48 บนเว็บ r49.2','ชุดใหม่บนเว็บ r49.2']
for label,(p,d) in zip(labels,sets):rows.append(f"| {label} | {'Source, ปิด LLM/semantic' if d['source'] else 'HTTP API จริง'} | {d['passed']}/{d['executed_cases']} | {d['requests']} | {link(p)} |")
baseline=sets[0][1];failed=[x for x in baseline['results'] if not x['passed']]
checks=collections.Counter(k for x in failed for k,v in x['checks'].items() if not v)
final=sets[-1][1];public=sets[-3][1];regression=sets[-2][1]
family=collections.Counter(x['family'] for x in final['results'])
language=collections.Counter(x['records'][0]['payload']['locale'] for x in final['results'])
elapsed=sorted(rec['elapsed_sec'] for d in [final,public,regression] for result in d['results'] for rec in result['records'])
percentile=lambda p:elapsed[min(len(elapsed)-1,int((len(elapsed)-1)*p))]
examples=[]
for suffix in ['parking-moto','own-controller','transfer-note','select-parking-fee','watch-free','topic-reset']:
 result=next(x for x in final['results'] if x['id']=='th-'+('follow-'+suffix if suffix in ['parking-moto','own-controller','transfer-note'] else suffix))
 examples.append('### '+result['id']+'\n\n'+ '\n'.join(f"{i+1}. {rec['payload']['question']}" for i,rec in enumerate(result['records']))+'\n\nคำตอบสุดท้ายจริง:\n\n```text\n'+result['answer']+'\n```\n')
flow='''# Flow การขยายคำถามบริการและความจำบทสนทนา r49

วันที่ 2026-10-09 — งานรอบนี้ดำเนินการแล้ว ดูผลจริงใน SERVICE_DIALOGUE_REPORT_R49.md

## 1. หลักฐานและขอบเขต

- ใช้คำตอบ 50 ข้อจากผู้ใช้ที่เก็บไว้เดิม แยก claim ที่ยืนยันแล้วออกจากช่องคำตอบว่าง
- เก็บ snapshot และ SHA-256 ก่อนแก้ app/tests/curated/rules/web ไม่ reset หรือ stash Git
- คำถามที่ไม่มีคำตอบชัดเจนต้องระบุ missing field การทดสอบผ่านไม่ทำให้ช่องนั้นกลายเป็นนโยบายที่เจ้าของยืนยัน
- เพิ่มเฉพาะเคสที่เกี่ยวข้อง ไม่เรียกชุดเต็มสองหมื่นกว่าเคส

## 2. Flow รับคำถาม

1. คงข้อความต้นฉบับไว้ใน log แล้ว normalize สำเนาสำหรับค้น
2. โหลดประวัติฝั่งเซิร์ฟเวอร์ของ session นี้ ประเมินคำถามต่อจาก assistant ล่าสุดเท่านั้น
3. ใช้หัวข้อจาก claim IDs/missing fields ที่เซิร์ฟเวอร์บันทึกและ client ACK แล้ว ไม่อนุมานหัวข้อจากข้อความคำตอบหรือ metadata ที่ client แต่งเอง
4. คำถามใหม่ระบุเรื่องชัดเจนให้ใช้เรื่องใหม่ คำถามสั้นที่ไม่มีฐานบริบทให้ขอรายละเอียด
5. หากคำถามสั้นจับ slot ของหัวข้อเดิมได้ ให้สร้างคำถามที่มีเรื่องครบ เช่น “แล้วเมาส์ล่ะ” ต่อจากอุปกรณ์ส่วนตัว ต้องคงคุณสมบัติ “ส่วนตัว”
6. หากหลายหัวข้อแล้วถาม “ฟรีไหม” ให้ถามว่าหมายถึงหัวข้อไหน เก็บ pending field เมื่อเลือกชื่อสั้น ๆ จึงตีความให้ครบ
7. ตัวจับคำบริการรับคำที่ต่างจากศัพท์กลางเล็กน้อย ใช้ OSA distance และ anchor คนละส่วนของประโยค ภาษาไทยเทียบสำเนาที่พับวรรณยุกต์/เครื่องหมายบางตัวร่วมด้วย
8. กันคำปฏิเสธ ตัวเลข วันที่ ID อุปกรณ์ และชื่อเฉพาะออกจาก correction targets จำกัดความยาว 256 ตัวอักษร และปฏิเสธ candidate ที่กำกวม
9. ตรวจขอบเขต: สมาชิกศูนย์ / Steam / ทีมแข่ง, เมาส์ส่วนตัว / ปุ่มเมาส์ในเกม / กติกาแข่ง, รูปสลิป / ใบเสร็จ / ถ่ายรูป ต้องแยกกัน
10. เลือกทุก claim ที่ตรงคำถาม พร้อม missing fields ของส่วนที่ยังตอบไม่ได้ คำถามหลายส่วนไม่ปล่อยให้มีเพียง claim แรกแล้วประกาศว่าตอบครบ
11. แสดงส่วนที่ยืนยันได้พร้อมแหล่งข้อมูล และส่วนที่ต้องยืนยันเพิ่มเติมอย่างชัดเจน ห้ามขยาย “ห้ามคีย์บอร์ด/เมาส์” เป็น “ห้ามจอย”
12. เก็บ state จาก result.trace ฉบับเต็มภายใน ไม่ใช้ query_debug.trace ซึ่งคัดเฉพาะ preprocessing และไม่ผูกความจำกับการเปิด debug
13. ส่งคำตอบ เก็บ delivery state รอ ACK ก่อนใช้เป็นฐานของคำถามต่อไป

## 3. Flow ตรวจและแก้

1. รัน baseline ด้วย oracle ที่กำหนด content, claim, missing และ context ไว้ก่อนแก้
2. จัดประเภทความผิด: วลีไม่ครอบคลุม / ตัวสะกด / lost context / scope รั่ว / สถานะไม่ถูกส่งถึงเว็บ / policy ยังว่าง
3. แก้เฉพาะประเภทที่ยืนยันได้ เก็บรอบเก่าครบ แล้วรัน source cases เดิมซ้ำ
4. เพิ่มการทดสอบสามรอบสนทนา เปลี่ยนหัวข้อ และค่าบริการที่ไม่ทราบ เพื่อจับการขยายความโดยเดา
5. รัน HTTP จาก candidate package จริงทั้ง debug=True และ debug=False โดยบันทึก payload ที่ส่งจริง ACK IDs, trace และเวลาครบ
6. หาก unit/source ผ่านแต่ HTTP ไม่ผ่าน ให้ตรวจเส้นทาง worker → server → state store → ACK → resolver ก่อนขยายศัพท์เพิ่มเติม
7. สร้าง candidate version ใหม่เมื่อแก้ source เพิ่ม เก็บ package/log รุ่นเก่า หยุดเฉพาะ PID ที่ยืนยันเป็น candidate ของงานนี้
8. รันชุดเดิมที่เกี่ยวข้อง 136 เคส พร้อมตรวจ hash ระหว่าง source และ package
9. หยุดการขยายทดสอบเมื่อ gate เหล่านี้ผ่าน รวบรวมขอบเขตที่ยังไม่ตรวจและคำถามสำหรับเจ้าของในรายงาน

## 4. ตรวจทาน Flow จากผลจริง

- รอบก่อน: เก็บ state จาก response.trace ทำให้ debug=False ไม่มีข้อมูล
- รอบแก้แรก: เปลี่ยนเป็น query_debug.trace แต่รายการนั้นถูกกรอง จึงยังไม่มี claim IDs การทดสอบ store แยกส่วนผ่านแต่ product ไม่ผ่าน
- รอบแก้สุดท้าย: เก็บจาก result.trace ภายใน และตรวจ HTTP ที่ debug=False จริง จึงครอบคลุมเส้นทางใช้งานจริง
- การรัน “Steam ต้องเป็นสมาชิกไหม” ผ่านในชุดนี้แปลว่าไม่เอานโยบายสมาชิกศูนย์ไปตอบ Steam ไม่ได้แปลว่ามีข้อมูลครบทุกนโยบายของ Steam
- การตอบ “ยังไม่ยืนยันค่าจอดรถ” ถูกต้องตามหลักฐาน แม้ยังไม่ใช่คำตอบราคาที่ผู้ใช้อยากรู้ ต้องเติมข้อมูลเจ้าของ ไม่ปรับคะแนนให้บังคับตอบฟรี
'''
flowpath=r.OUT/'SERVICE_DIALOGUE_FLOW_R49.md'
with flowpath.open('x',encoding='utf-8') as stream:stream.write(flow)
unitresults=[]
for name in ['test_service_fact_dialogue_r49','test_user_service_facts_r48','test_task_memory_r41','test_two_turn_choices_r39']:
 files=sorted(r.OUT.glob(name+'_*.txt'),key=lambda p:p.stat().st_mtime)
 p=files[-1];text=p.read_text(encoding='utf-8');unitresults.append(f'- {name}: '+text[text.rfind('Ran '):].strip().replace('\n',' ')+' — '+link(p))
report=f'''# รายงานขยายเคสบริการและบทสนทนา r49

วันที่ 2026-10-09, เวลาไทย — runtime สุดท้าย `{final['health']['runtime']['version']}`

## สรุปผลที่ทดสอบจริง

ชุดใหม่ {final['passed']}/{final['executed_cases']} เคส, เว็บปกติที่ debug=False {public['passed']}/{public['executed_cases']} เคส, ชุดเดิมที่เกี่ยวข้อง {regression['passed']}/{regression['executed_cases']} เคส ผ่านตามเงื่อนไขแต่ละชุด ไม่มี full test 20k ในรอบนี้ ตัวเลขสามชุดไม่ใช่เคสอิสระทั้งหมด: ชุด debug=False เป็นส่วนหนึ่งของชุดใหม่

{chr(10).join(rows)}

คำว่า “ผ่าน” รวมถึงตอบว่าไม่มีข้อมูลที่ยืนยันและขอรายละเอียดเมื่อควรทำ ไม่ได้หมายความว่าศูนย์ยืนยันทุกนโยบายแล้ว

## Coverage และ oracle

- ชุดใหม่ภาษา: {dict(language)}; ประเภท: {dict(family)}
- 14 หัวข้อบริการ มีวลีทั่วไปและ typo ทั้งไทย/อังกฤษ เช่น membrship, walkk, keyboarrd, คีย์บอด, โอนครังเดียว
- compound ตรวจครบทุก claim ที่คาดไว้และ missing fields ไม่ดูเพียง HTTP 200
- คำถาม 2–3 รอบ: motorcycles, map link, passport, own mouse/controller, note, slip channel, waiting point, date, ambiguous free และการเปลี่ยนไปถามรายชื่อเกม
- scope ตรวจว่าไม่ใช้ user_service_facts กับ Steam/team/ปุ่มยิง/กติกาแข่ง จุดนี้ไม่ได้ประเมินความครบถ้วนของคำตอบกติกาแข่งหรือ Steam
- แหล่ง oracle คือคำตอบผู้ใช้/claim IDs เดิมและ missing fields ไม่ใช้โมเดลตัดสินเองจากความคล้ายของประโยค ชื่อและข้อความภาษาอังกฤษแปลโดยระบบ ยังไม่มีการตรวจภาษาอังกฤษโดยเจ้าของเพิ่ม
- debug=False ตรวจข้อความที่จำเป็น, missing ที่ชัด, outcome ไม่ประกาศ complete เมื่อข้อมูลไม่ครบ, ไม่มี trace หลุด, ไม่ลากที่จอดรถกลับมาหลังเปลี่ยนเรื่อง
- ผลทั้งหมดเป็น automated checks ไม่มีหลักฐานใหม่จากการใช้บริการจริง ไม่มีการยืนยันสถานะจองสดในรอบนี้

## ทำไม baseline ถึงผิด

baseline ผ่าน 37/102 ไม่ควรแปลว่าอีก 65 คำตอบเป็นข้อเท็จจริงผิดทั้งหมด: {sum(not x['checks']['required_content'] for x in failed)} เคสไม่ผ่านข้อความที่ต้องมี และบางเคสเนื้อหาถูกแต่ไม่ผ่าน trace/context/scope contract เงื่อนไขที่ตกซ้ำซ้อนกันได้: `{dict(checks)}`

1. **คำและวลีไม่เข้าตัวจับ claim** — ข้อมูลมีอยู่ แต่ nonmembers, turn up, incorrect transfer receipt image หรือ motorcycle parking ไม่ตรงคำที่ handler รู้จัก จึงตกไป handler รายชื่อบุคลากร/ตารางเวลา/คำตอบไม่พบข้อมูล แก้ด้วยแนวคิดและ anchor ที่สัมพันธ์กับบริการ
2. **สะกดผิดทำให้ไม่เห็น noun หลัก** — อังกฤษใช้ token และ OSA หนึ่ง edit; ไทยไม่มีช่องว่างคั่นทุกคำและมีเครื่องหมายรวม จึงเทียบ span พร้อม diacritic fold กรณีโอนครังเดียวต้องเลือกระยะที่ใกล้ก่อนความยาว เพื่อไม่กินตัว น ของ “โอน”
3. **คำถามสั้นหายเงื่อนไขเดิม** — “แล้วเมาส์ล่ะ” ไม่มี own/personal, “ส่งที่ไหน” ไม่มี slip; เดิม reroute เป็นคำถามใหม่ แก้โดยบันทึก typed service state จากคำตอบที่ ACK แล้วและขยายเฉพาะ slot ที่สัมพันธ์กัน
4. **ขอบเขตข้อมูลรั่ว** — สมาชิกศูนย์ใช้ตอบสมาชิก Steam/team; นโยบายห้ามเมาส์ส่วนตัวมีโอกาสใช้ตอบปุ่มเมาส์ในเกม ต้องแยก service/account/game-control/tournament ก่อนเลือก claim
5. **ข้อมูลว่างแต่ขยายจากส่วนใกล้เคียง** — ดูเพื่อนได้ไม่เท่ากับฟรี มีที่จอดไม่เท่ากับฟรี ห้าม keyboard/mouse ไม่ยืนยันว่าห้าม controller แก้โดยแสดง missing field โดยตรงและไม่สร้างนโยบาย
6. **เส้นทางเว็บ debug=False ไม่ส่ง state** — รุ่น r49.1 ใช้ query_debug.trace ซึ่งมี preprocessing เท่านั้น จึงไม่เห็น user_service_facts การทดสอบ store แยกส่วนผ่านเพราะส่ง full trace ให้เอง แต่ HTTP ปิด debug ผ่านเพียง 6/28 รุ่น r49.2 ใช้ result.trace ภายในจึงผ่าน 28/28

ไม่ได้เกิดจากคะแนน retrieval เพียงอย่างเดียว หลายเคสหลุดก่อนถึงการค้นหรือเปลี่ยน operation เลย รายงานเคสที่พลาดทั้งหมดด้านล่างเก็บ mode/trace/normalized query และคำตอบจริง แยกสาเหตุระดับ route/context/oracle

## ตัวอย่างผลจริงหลังแก้

{chr(10).join(examples)}

## Unit checks ที่เกี่ยวข้อง

{chr(10).join(unitresults)}

## เวลาในการตอบบนเครื่องนี้

รวมคำขอจริงจาก 3 ชุดสุดท้าย {len(elapsed)} requests: median {statistics.median(elapsed):.3f}s, p95 {percentile(.95):.3f}s, max {max(elapsed):.3f}s นี่คือการส่งตามลำดับไปยังเครื่อง/โมเดลที่เปิดอยู่ จึงไม่ใช่ benchmark รองรับหลายคนพร้อมกันหรือ WordPress live booking และรวมกรณีขอรายละเอียด/ไม่พบคำตอบด้วย

## สิ่งที่เจ้าของยังต้องให้ข้อมูล

1. ที่จอดรถฟรีไหม ถ้ามีราคา เป็นของศูนย์หรือระบบอาคาร?
2. คนมานั่งดูเพื่อนต้องจ่ายเงินไหม มีเงื่อนไขจำนวนคนหรือพื้นที่ไหม?
3. จอยส่วนตัวอนุญาตไหม แยก PC/PS5/Switch/VR และกิจกรรมแข่งหรือบริการทั่วไปหรือไม่?
4. Note สำหรับโอนรวมต้องระบุอะไรบ้าง เช่น เลขรายการ ชื่อผู้จอง และยอดของแต่ละรายการ?
5. รอก่อนเวลาจองใช้โซนกลางได้หรือมีจุดอื่นที่กำหนด?
6. เปลี่ยนวันเมื่อจ่ายแล้วทำทางไหน และกรณี “เลื่อนแทนคืนเงินไม่ได้” ต่างจากเปลี่ยนวันผิดอย่างไร?
7. ข้อมูลเดิมที่ยังว่าง เช่น เด็ก/ผู้ปกครอง, ติดตั้งเกม, บัญชีผู้จ่าย, สตรีม/ถ่ายรูป, เวลาที่เสียจากอัปเดต/เครื่องเสีย ยังคงสถานะเดิม

## ขอบเขตและส่วนที่ยังพัฒนาได้

- ตัวแก้คำรอบนี้จำกัด noun บริการและ anchor ไม่ใช่ spell checker ทั่วภาษา; คำยาวเกิน 256 ตัวอักษรจะไม่ทำ fuzzy recovery
- ยังไม่รับประกันคำผิดหลายส่วนที่ไม่เหลือ anchor, สลับภาษาในประโยคทุกแบบ หรือคำถาม follow-up ทุกสำนวน
- ความจำใช้ latest acknowledged answer; restart server ทำให้ประวัติฝั่ง memory หาย ไม่ได้เพิ่ม persistence หรือระบบหลายเครื่องในงานนี้
- หลังเปลี่ยนหัวข้อแล้วถาม “แล้วมอเตอร์ไซค์ล่ะ” ระบบขอข้อมูล/ไม่พบคำตอบได้ เงื่อนไขผ่านคือไม่ยกคำตอบที่จอดเก่ามาปะปน ไม่ใช่สัญญาว่าจะสรุปความหมายได้ทุกกรณี
- คำถามสมาชิกทีม VALORANT และ Steam ผ่านการกัน scope; บางคำถามยังขอรายละเอียด/ไม่พบข้อมูล ไม่ถือว่ารู้จำนวนสมาชิกทีมแล้ว
- candidate ที่เปิดคือ r49.2; portable bundles รุ่นก่อนหน้ายังไม่ได้ rebuild ทั้งหมด
- เพิ่ม test case ใหม่เมื่อมีคำถามผู้ใช้จริงที่พลาด โดยคง oracle ตามข้อมูลจริงก่อนปรับ handler ไม่จำเป็นต้องขยาย alias ทุกคำผิด

## การเก็บไฟล์และตรวจรุ่น

แก้ 6 ไฟล์เดิม เพิ่ม 3 ไฟล์ code/test; ไฟล์เดิมอื่นที่ snapshot ไว้ 320 ไฟล์คง hash เดิม; curated/rules ไม่เปลี่ยน; source/package ตรงกัน 169/169 ไฟล์ ตรวจ Git diff --check exit 0

{link(r.OUT/'SOURCE_AND_RELEASE_AUDIT_R49_2.json')} · {link(r.OUT/'SOURCE_CHANGE_R49_2.diff')} · {link(r.OUT/'GIT_STATUS_R49_2.txt')} · {link(r.OUT/'GIT_DIFF_CHECK_R49_2.txt')}

snapshot ก่อนแก้และ log แต่ละรอบเก็บแยกไว้ในโฟลเดอร์นี้ รวมถึงผลรอบที่ไม่ผ่าน ไม่มีการลบ log หรือ reset/stash Git เดิม

Flow: {link(flowpath)}
'''
reportpath=r.OUT/'SERVICE_DIALOGUE_REPORT_R49.md'
with reportpath.open('x',encoding='utf-8') as stream:stream.write(report)
details=['# เคสที่เคยไม่ผ่านและหลักฐาน r49','\nอ่านร่วมกับ SERVICE_DIALOGUE_REPORT_R49.md; count ของ checks อาจซ้ำในเคสเดียว']
lookup={x['id']:x for x in final['results']}
for title,d in [('Baseline source',baseline),('HTTP debug=False r49.1',sets[5][1])]:
 details.append('\n## '+title+'\n')
 for x in d['results']:
  if x['passed']:continue
  details.append('\n### '+x['id']+'\n\nคำถาม: '+' → '.join(z['payload']['question'] for z in x['records'])+'\n\nไม่ผ่าน: '+', '.join(k for k,v in x['checks'].items() if not v)+'\n\nMode: `'+str(x.get('mode'))+'`\n\n```text\n'+x['answer']+'\n```')
  rec=x['records'][-1]['response'];meta=[t for t in rec.get('trace',[]) if t.get('stage') in ['user_service_facts','service_fact_scope_guard','preprocess']]
  details.append('\n\nContext / selection trace:\n\n```json\n'+json.dumps(dict(resolved_question=rec.get('resolved_question'),context_resolution=rec.get('context_resolution'),trace=meta),ensure_ascii=False,indent=2)+'\n```')
  if x['id'] in lookup:
   fixed=lookup[x['id']];details.append('\n\nคำตอบหลังแก้ r49.2 (ผ่าน='+str(fixed['passed'])+'):\n\n```text\n'+fixed['answer']+'\n```')
with (r.OUT/'FAILED_CASE_ANALYSIS_R49.md').open('x',encoding='utf-8') as stream:stream.write('\n'.join(details)+'\n')
print(reportpath)
