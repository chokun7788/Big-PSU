from pathlib import Path
import json,re,hashlib,ast,difflib,shutil
W=Path(__file__).parent;R=Path((W/'r37_report_path.txt').read_text().strip());P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');PACKAGE=P/'owner_local_delivery_20261003_competition_conversation_r37_final3/PSU_Esports_Chatbot_Local'
def read(name):return json.loads((R/name).read_text(encoding='utf-8-sig'))
main=read('final3_ready_SUMMARY.json');extra=read('final3_holdout_repeat_SUMMARY.json');content=read('SOURCE_CONTENT_final3_ready.json');unit=read('final3_regression.json')
assert main['passed']==main['requests'] and extra['passed']==extra['requests'] and content['passed']==content['answers_audited'] and unit['passed']
ui=json.loads((W/'r37_2_production_UI_8_turns.json').read_text(encoding='utf-8'))
assert len(ui)==8 and ui[0]['result']['mode']=='pipeline:competition_rulebook_catalog'
ui_errors=[]
seen=[]
for i,row in enumerate(ui[1:],1):
 if row['result']['route_category']!='competition_rules' or row['result']['context_resolution'].get('context_game')!='VALORANT':ui_errors.append((i,'wrong_rulebook_context'))
 if not row['clauses'] or any(not re.search(r'[\u0e00-\u0e7f]',line) for line in row['clauses']):ui_errors.append((i,'non_thai_rule_clause'))
 if i in (5,7):
  prior=[c for old in ui[max(1,i-5):i] for c in old['clauses']]
  if any(re.sub(r'\s+','',line) in [re.sub(r'\s+','',old) for old in prior] for line in row['clauses']):ui_errors.append((i,'repeated_clause'))
assert not ui_errors,ui_errors
protected=read('protected_before.json')
assert all(hashlib.sha256((P/rel).read_bytes()).hexdigest()==sha for rel,sha in protected.items())
rels=read('changes.json')['files'];manifest={}
for rel in rels:
 current=(P/rel).read_bytes();ast.parse(current.decode('utf-8-sig'))
 assert current==(PACKAGE/rel).read_bytes()
 manifest[rel]=hashlib.sha256(current).hexdigest()
 dst=R/'final_source'/rel;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(P/rel,dst)
 old=(R/'before'/rel).read_text(encoding='utf-8-sig');new=current.decode('utf-8-sig').replace('\r\n','\n')
 diff=R/'final_diff'/Path(rel).with_suffix('.diff');diff.parent.mkdir(parents=True,exist_ok=True)
 diff.write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='before/'+rel,tofile='final/'+rel)),encoding='utf-8')
for name in ('r37_2_production_UI_8_turns.json','r37_2_production_UI_transcript.txt','r37_2_web_proof.png'):
 shutil.copy2(W/name,R/name)
summary={'runtime_version':'2026.10.03-competition-conversation-r37.2','http_requests':main['requests']+extra['requests'],'http_passed':main['passed']+extra['passed'],'overview_answers_audited':content['answers_audited'],'source_clause_checks':content['clauses_audited'],'regression_methods':unit['tests'],'ui_turns':len(ui),'ui_errors':ui_errors,'protected_files_unchanged':len(protected),'package':str(PACKAGE),'source_hashes':manifest}
with (R/'FINAL_SUMMARY.json').open('x',encoding='utf-8') as f:json.dump(summary,f,ensure_ascii=False,indent=2)
text=f'''# ทดสอบคำถามแบบผู้ใช้และแก้บทสนทนากติกา — r37.2

3 ตุลาคม 2026 / เว็บหลัก http://127.0.0.1:8090/

## ผลล่าสุด

- ชุดคำถามเดิมและคำถามดัดแปลงหลัก: **{main['passed']}/{main['requests']}**
- คำถามใหม่และการขอกฎเพิ่มเติมหลายครั้ง: **{extra['passed']}/{extra['requests']}**
- รวม **{summary['http_passed']}/{summary['http_requests']} ข้อ** ผ่านเงื่อนไขที่ตรวจ
- ตรวจเนื้อหาของภาพรวม **{content['answers_audited']} คำตอบ / {content['clauses_audited']} ข้อความกฎ** พบข้อความตรงในแหล่งที่เลือกทั้งหมด ไม่มีชื่อรายการแข่งขันปนเป็นข้อกฎ ไม่มีบั๊กอยู่ใต้หัวข้อหยุดฉุกเฉิน และไม่มีส่วนอังกฤษคู่ขนานในสรุปไทย
- ทดสอบขอบเขตบริบท **{unit['tests']} ชุด** ผ่าน รวมการเปลี่ยนเรื่อง คำจริงภาษาอังกฤษ เกม/ปีที่ไม่รองรับ และประวัติที่ไม่ควรนำมาใช้
- ลองผ่านหน้าเว็บหลักจริงแบบ Auto **8 ข้อ** ต่อเนื่อง ผ่านรายชื่อเกม การเลือก VALORANT คำผิด และคำขอกฎเพิ่มเติมสองครั้ง
- ไฟล์ข้อมูล/คำตอบอ้างอิงเดิม **{len(protected)} ไฟล์** hash ก่อนและหลังตรงกัน

ผลนี้เป็นการตรวจงานกติกา/บทสนทนาชุดที่ระบุ ไม่ใช่ผล Ground Truth ทั้งโปรเจกต์ หรือการรับรองนโยบายและคำแปลจากเจ้าของ

## คำถามที่ลองจริง

ชุดเดิม: “มีเกมอะไรให้แข่งมั่ง” → “valorant” → “ขอกฏหนาอย” → “ขอกฏของเกมหน่อย” → “ขอกฏของเกม valo หน่อย” → “มีกฏอื่นไหม”

ตัวอย่างถ้อยคำดัดแปลง:

- มีเกมไรให้แข่งมั่ง / แข่งเกมไหนได้บ้าง / มีเกมไหนแข่งได้มั่ง
- valroant / valorantt / แล้ว valorantt ล่ะ / เอาวาโล / วาโลครับ
- ขอกฎหน่อยยย / ขอกฎเกมนี้หน่อยย / ขอกติกาของเกมนี้ครับบบ
- กติกาเกมนี้มีไรมั่ง / มีข้ออื่นอีกป่าว / แล้วข้ออื่นล่ะ / ต่ออีกหน่อย
- กฎเรื่องอุปกรณ์ของเกมนี้มีอะไรบ้าง
- Which games can we compete in? / Then CS2 please
- can i see the rulez for this game pls / can i see all ruless for this game pls
- Any additional rules? / anything else

กรณีป้องกันการตอบมั่ว: เปลี่ยนไปถามเวลาเปิด, ขอกฎศูนย์, ไม่เอากฎแล้วถามว่า VALORANT คืออะไร, เกม Minecraft, กติกาปี 2024 และ more please ที่ไม่มีเรื่องเดิม

## สาเหตุที่พบและวิธีแก้

| ประเภท | หลักฐานที่พบ | การแก้ |
|---|---|---|
| ถ้อยคำต่าง แต่เป้าหมายเดิม | คำถาม “มีเกมไร…” และ “แข่งเกมไหน…” หลุดจากตัวตรวจรายชื่อ | ใช้รูปแบบคำขอที่ประกอบจากคำถาม/เกม/การแข่งขันและคำลงท้าย ไม่เพิ่ม alias ทั้งประโยคทีละคำถาม |
| แก้ชื่อเกมหลังเสียบริบท | valroant ถูกแก้เป็น VALORANT ใน preprocessing แต่ถูกส่งไปข้อมูลเกม | ใช้ตัวกู้ชื่อแบบระยะตัวอักษรเดิมก่อนตัดสินคำตอบชื่อเกมสั้น โดยมีเรื่องการแข่งขันก่อนหน้าเป็นหลักฐาน |
| เป้าหมายที่กู้แล้วไม่ถูกส่งต่อ | ขอกฎหน่อยยย หลัง valroant ยังเสียเป้าหมาย | รับเป้าหมายที่ resolve แล้วของชื่อเกมพิมพ์ผิดเป็นบริบทต่อเนื่อง โดยตรวจว่าเป็นตัวเลือกชื่อเกมที่จำกัดขอบเขต |
| คำลงท้ายผิด/เบิ้ล | หนาอย, หน่อยยย, ครับบบ | แก้เฉพาะคำลงท้ายเมื่อส่วนคำขอกฎชัดเจน เก็บข้อความเดิมไว้สำหรับวิเคราะห์ |
| คำขอเพิ่มเติมไม่มีคำว่า “กฎ” | มีข้ออื่นอีกป่าว / ต่ออีกหน่อย | รับเป็นคำขอเพิ่มเฉพาะเมื่อมี rulebook ที่ใช้งานอยู่; ไม่มีเรื่องเดิมไม่เลือกเกมเอง |
| คำถามเฉพาะต่อจากภาพรวม | กฎเรื่องอุปกรณ์ของเกมนี้ | ใช้หัวข้อที่ตรวจได้เดิม พร้อมเป้าหมายเกมล่าสุด รักษาคำถามเฉพาะ ไม่เขียนเป็นภาพรวมทับหัวข้อ |
| คำอังกฤษมีคำผิด | rulez/ruless | ตรวจคำขอจากโครงสร้างประโยคร่วมกับระยะตัวอักษร และกันคำจริง เช่น roles/runes ไม่แก้เป็น rules |
| รายชื่ออังกฤษถูกปฏิเสธ | debug แสดง english_output_contains_thai_prose | ถ้าไม่มีชื่อรายการอังกฤษใน registry ใช้ชื่อเกมและปีที่อ่านได้จากแหล่ง ไม่สมมุติชื่อรายการหรือสร้างสถานะอนุมัติคำแปล |
| คำเปลี่ยนเรื่องยังมีคำว่า “กฎ” | ไม่เอากฎแล้ว VALORANT คืออะไร ไปกติกา | ตัดเฉพาะคำนำปฏิเสธงานเดิม เมื่อคำขอใหม่ครบและชัด เก็บ original question ไว้ |
| metadata ถูกคิดเป็นกฎ | ชื่อรายการมีปี หรือเลขใน CS2 | แยกชื่อรายการ/หัวข้อสั้นออกจากประโยคข้อกำหนด; เลขในชื่อเกมไม่ใช่จำนวนที่กำหนดในกฎ |
| title field เป็นข้อกฎเต็ม | กติกา CS2 บางข้อมี text เท่ากับ section_title | เก็บประโยคที่มีข้อกำหนดจริง ไม่ตัดทุกข้อความที่เท่ากับชื่อหัวข้อ |
| chunk รวมหลายหัวข้อ | ส่วนหยุดฉุกเฉินมี Bug Rules ตามมาภายใน chunk เดียว | หัวข้อหยุดฉุกเฉินใช้เฉพาะข้อก่อนหัวข้อย่อยถัดไป ข้อบั๊กที่เหลือไม่แสดงใต้หัวข้อหยุดฉุกเฉิน |
| เอกสารสองภาษาถูกนับเป็นข้อใหม่ | หน้าเว็บตอบกฎอังกฤษซ้ำความหมายกฎไทยในการขอเพิ่มครั้งที่สอง | เลือกชุดหัวข้อหลักจากข้อกฎภาษาไทย และใช้คำแปลเดิมของชุดนั้นเมื่อขออังกฤษ ส่วนอังกฤษคู่ขนานไม่ใช่ข้อใหม่ |
| หัวข้อสั้นปนเป็น bullet | การย้อนรอบ (Round Rollback) ไม่มีข้อกำหนดตามมา | ตัดชื่อหัวข้อเดี่ยว รักษาข้อความกฎการย้อนรอบเต็มไว้ |

## Flow ล่าสุด

1. อ่านคำถามและประวัติของคำขอนั้น
2. แยกคำขอรายชื่อ / ตัวเลือกเกม / ภาพรวมกฎ / หัวข้อเฉพาะ / ข้อเพิ่มเติม / การเปลี่ยนเรื่อง
3. กู้ชื่อเกมและคำงานเฉพาะเมื่อมีหลักฐานและรูปแบบที่รองรับ ไม่แก้ปี ตัวเลข หรือชื่อเกมใหม่โดยเดา
4. คำต่อเนื่องใช้เกมล่าสุดที่ยืนยันได้จากผู้ใช้และคำถามที่ resolve แล้ว; หยุดเมื่อเปลี่ยนหัวข้อ
5. เลือก rulebook ของเกมเดียวและชุดหัวข้อหลักของเอกสาร
6. ภาพรวมใช้ข้อกฎจริงหลายหมวด; หัวข้อเฉพาะใช้เส้นทางค้นเนื้อหาเฉพาะเดิม
7. เมื่อขอข้อเพิ่มเติม ตัดข้อที่แสดงแล้วในประวัติที่มี และใช้ข้อความจากเอกสารเดิมสำหรับข้อใหม่
8. รักษาขอบเขตหัวข้อภายใน chunk และแยก metadata ออกจากข้อกำหนด
9. ตรวจเกม/แหล่ง/รูปแบบ/ภาษาของคำตอบ พร้อมบันทึกเหตุผลใน trace
10. ถ้าข้อมูลหรือฉบับที่ถามยืนยันไม่ได้ ให้บอกข้อจำกัด ไม่มีการยืมกฎจากเกมหรือปีอื่น

## ลำดับผลและข้อผิดพลาดของการทดสอบ

- r36 ก่อนแก้: 27/41 ผ่าน
- รอบ A: 38/41 ผ่าน แต่ unit พบ roles ถูกแก้เป็น rules จึงแก้ตัวกันคำจริง
- รอบ B: มี ConnectionRefused ช่วงเริ่มเว็บ 7 ข้อ และพบการตัดข้อกฎ CS2 จริงออก ต้องแยกสองสาเหตุนี้ออกจากกัน
- รอบ C: ชุดหลัก 41/41; ชุดใหม่ 12/13 พบชื่อรายการ CS2 ปนเป็น bullet
- รุ่น r37: 54/54 และ literal source audit ผ่าน แต่หน้าเว็บเพิ่มเติมครั้งที่สองพบกฎสองภาษาซ้ำความหมาย แสดงว่าความตรงตัวเพียงอย่างเดียวยังไม่พอ
- รุ่น r37.1: 62/62; หน้าเว็บครบ 8 ข้อ แต่พบหัวข้อสั้นหนึ่งรายการ จึงเก็บการแก้รูปแบบเพิ่ม
- **รุ่นที่ใช้งาน r37.2: 62/62, source audit {content['clauses_audited']} ข้อ, unit {unit['tests']} ชุด, หน้าเว็บ 8 ข้อผ่าน**
- มีความผิดพลาดในตัวจัดชุดคำถามเพิ่มหนึ่งครั้ง (array รูปแบบผิด) เก็บ log ไว้ และใช้ชุดแก้รูปแบบใหม่สำหรับผลสุดท้าย ไม่ถือข้อผิดพลาดของตัวทดสอบนั้นเป็นผลตอบผิดของ chatbot

ไม่ได้ทับผลที่ผิดหรือผลรอบก่อน ไฟล์ JSONL เก็บคำถาม ประวัติที่ส่ง คำตอบ trace เวลา และเหตุผลที่ไม่ผ่าน แยกกันตามชื่อรอบ

## เปิดใช้งานและหลักฐาน

เว็บเดิม: http://127.0.0.1:8090/ — runtime `2026.10.03-competition-conversation-r37.2`

Package: `{PACKAGE}`

แก้ runtime 3 ไฟล์: competition_conversation_signals.py, context_resolver.py, competition_overview.py เส้นทางส่งประวัติ server/worker ที่แก้ใน r36 ใช้ต่อในรุ่นนี้

ไฟล์ก่อนแก้/หลังแก้/hash/diff และผลทุกช่วงอยู่ใน `{R}`

- final3_ready.jsonl / final3_ready_SUMMARY.json
- final3_holdout_repeat.jsonl / final3_holdout_repeat_SUMMARY.json
- SOURCE_CONTENT_final3_ready.json
- final3_regression.json และ log
- r37_2_production_UI_8_turns.json / r37_2_production_UI_transcript.txt
- r37_2_web_proof.png
- FINAL_SUMMARY.json / final_source / final_diff

## ขอบเขตที่ยังต้องเข้าใจ

- 62 ข้อเป็นชุดตรวจเฉพาะการคุยเรื่องกติกา ไม่ได้ครอบคลุมทุกประโยคหรือทุกความหมายที่อาจพิมพ์ผิด
- literal source audit ตรวจข้อความที่แสดงกับแหล่งที่เลือก รวมเงื่อนไขรูปแบบ/ภาษา ไม่ใช่การรับรองว่าเอกสารต้นฉบับมีนโยบายถูกต้องทุกข้อ
- ใช้ประวัติ 10 ข้อความล่าสุดที่เว็บส่งมา; ไม่ใช่ความจำทั้งแชทข้ามการ refresh หรือทุกข้อความย้อนหลัง
- การระบุเกม/ปีที่ไม่มีข้อมูลยังต้องชี้แจงหรือแจ้งว่าไม่ยืนยัน ไม่ตอบโดยเดา
- ไม่มีการแก้นโยบาย ไฟล์เจ้าของ คำแปลเดิม Gold หรือเก็บสถานะจองจริงใหม่
- แท็บประวัติของผู้ใช้ไม่ได้ถูก refresh/ล้าง การ reload เพื่อทดสอบทำในแท็บทดลองใหม่เท่านั้น
'''
with (W/'PSU_ESPORTS_R37_TEST_AND_FIX_REPORT_20261003.md').open('x',encoding='utf-8') as f:f.write(text)
with (R/'FINAL_REPORT_TH.md').open('x',encoding='utf-8') as f:f.write(text)
print(json.dumps(summary,ensure_ascii=False))
