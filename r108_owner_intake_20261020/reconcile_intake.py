"""Review owner statements and sources; refresh questions without mutating responses or runtime data."""
import hashlib,json,shutil,sqlite3,zipfile
from datetime import datetime
from pathlib import Path
import xml.etree.ElementTree as ET

R=Path(__file__).resolve().parent;B=R.parent;F=B/'r107_owner_questions_20261020'
def read(p):return json.loads(p.read_text('utf8'))
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2),'utf8')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
before=read(R/'BEFORE_simple_questions.json');old={q['id']:q for q in before['questions']}
responses=read(F/'responses/simple_answers.json');at=datetime.now().astimezone().isoformat()
write(R/'REPLIES_REVIEWED.json',{'read_at':at,'file_sha256':digest(F/'responses/simple_answers.json'),'responses':responses,'note':'Draft replies reviewed at the explicit request in chat. Original submitted_at values preserved; this is not a web submission.'})
for name in ['index.html','app.js','style.css','server.py']:
 dest=R/('BEFORE_'+name)
 if not dest.exists():shutil.copy2(F/name,dest)

# Deliberately narrow statements to the part the reply actually answers.
facts={
'Q001':('รอก่อนเวลา','รอที่โซนกลางห้องได้ แต่ยังเข้าเล่นก่อนถึงเวลาจองไม่ได้'),
'Q003':('ต่อเวลา','หากรอบถัดไปยังว่างและอยู่ในเวลาบริการปกติ สามารถจองต่อผ่านขั้นตอนปกติได้'),
'Q004':('เปลี่ยนบริการระหว่างรอบ','ไม่มีการคืนเงินของรายการเดิม; คำตอบก่อนหน้าระบุให้ยกเลิกแล้วจองใหม่'),
'Q005':('แก้รายการจองที่จ่ายแล้ว','แก้ข้อมูลหลังจองไม่ได้ ให้ยกเลิกผ่านอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่พร้อมแนบสลิปที่ชำระไว้เดิม'),
'Q008':('ไปไม่ทันรอบ','ต้องแจ้งศูนย์; ผู้ตอบไม่ได้ให้ข้อยกเว้นเพิ่มเติมเรื่องการเช็กอิน'),
'Q009':('เปลี่ยนรอบเพราะฝน','ติดต่อเพจ Facebook พร้อมสลิปโอนเงินและหลักฐานการจอง'),
'Q010':('ศูนย์ปิดหลังจอง','ศูนย์ติดต่อผ่านอีเมล Gmail ที่ใช้สมัคร; ยังไม่ใช่ข้อยืนยันวิธีคืนเงินหรือเปลี่ยนรอบ'),
'Q011':('แก้ชื่อในรายการจอง','ยกเลิกผ่านอีเมลก่อนใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ พร้อมสลิปเดิม'),
'Q014':('เงินโอนเกิน','ติดต่อเพจ Facebook พร้อมสลิปและหลักฐานการจอง; คำตอบก่อนหน้าระบุเก็บใช้ session อนาคต ไม่คืนเงิน'),
'Q015':('โอนเพิ่มเมื่อยอดขาด','ติดต่อเพจ Facebook พร้อมสลิปและหลักฐานการจอง'),
'Q016':('การชำระเงิน','ต้องจ่ายเต็มจำนวน'),
'Q017':('ตรวจยอดโอน','ใช้เวลาประมาณ 30 นาที หากสถานะยังไม่เปลี่ยนให้ติดต่อเพจ Facebook'),
'Q018':('ใบกำกับภาษี','ออกใบกำกับภาษีไม่ได้; คำตอบก่อนหน้าแยกระบุใบเสนอราคาและใบเสร็จออกไม่ได้เช่นกัน'),
'Q019':('ติดต่อเมื่อมีปัญหาเงิน','ติดต่อเพจ Facebook พร้อมสลิปและหลักฐานการจอง; ไม่อนุมานสิทธิได้เงินคืนหรือระยะเวลาคืนเงินจากคำตอบนี้'),
'Q020':('บัญชี Steam','ศูนย์มีบัญชี Steam ให้ใช้ที่ศูนย์ และใช้บัญชีส่วนตัวได้'),
'Q021':('ขอบเขตคำตอบบัญชีเกม','คำตอบนี้ยืนยันเฉพาะ Steam ซ้ำกับ Q020 ไม่ได้ยืนยันบัญชี PS5/Switch/VR หรือสมาชิกออนไลน์/DLC'),
'Q022':('ออกจากบัญชี','เจ้าของระบุว่าออกจากระบบและไม่เก็บข้อมูลไว้; ยังไม่ได้ตรวจทางเทคนิคว่าไม่มีข้อมูลหลงเหลือทุกชนิด'),
'Q025':('ชดเชยอัปเดตเกม','หากอัปเดตนานเกิน 5 นาทีจะต่อเวลาให้; ไม่ระบุจำนวนเวลาที่ต่อ'),
'Q026':('เกมใช้งานไม่ได้','กรณีเปิดเกมไม่ได้จากเหตุอื่นที่ไม่ใช่อัปเดต สามารถเปลี่ยนเครื่องได้; ไม่แทนที่คำตอบเดิมที่ห้ามเปลี่ยนเครื่องขณะอัปเดต'),
'Q027':('ยืนยันเวอร์ชันเกม','สอบถามผู้ดูแลได้'),
'Q028':('ปัญหาเน็ตหรือระบบ','ใช้หลักการเดียวกับเหตุเครื่องขัดข้องและแจ้งเจ้าหน้าที่ตรวจสอบ'),
'Q029':('ความเสียหายอุปกรณ์','หากเสียเองโดยไม่เกี่ยวกับผู้เล่นไม่ต้องชดใช้; ไม่กำหนดยอดเงินหรือเหมารวมเหตุที่ยังไม่ตรวจ'),
'Q030':('อุปกรณ์ต่อพ่วงเสีย','แจ้งพนักงานให้เปลี่ยนได้'),
'Q032':('ผู้ปกครอง','การมีผู้ปกครองดูแลเป็นคำแนะนำ เซ็นยินยอมอย่างเดียวได้ และใช้ชื่อผู้ปกครองยืนยัน; ไม่ตั้งอายุขั้นต่ำแทนเจ้าของ'),
'Q033':('บันทึกภาพในเกม','capture ภาพหรือวิดีโอในเกมได้ เมื่อเสร็จให้ลบ; ไม่ครอบคลุมการถ่ายบุคคลหรือสถานที่'),
'Q034':('สตรีมเกม','คำตอบเดิมอนุญาตสตรีม คำตอบล่าสุดระบุไม่มีจำกัดโซน; ข้อความเรื่อง Steam ไม่ใช่การให้สิทธิ์ซอฟต์แวร์สตรีมเพิ่ม'),
'Q037':('ผู้ใช้ภายนอก','บุคคลภายนอกใช้บริการทั่วไปได้ทั้งหมด; ไม่ขยายไปเป็นคุณสมบัติแข่ง CS2 ซึ่งเอกสารกำหนดนักศึกษา PSU ภูเก็ต'),
'Q040':('วันหยุดราชการ','รอประกาศศูนย์ผ่านเพจ Facebook'),
'Q041':('เช่านอกเวลา','รับพิจารณาเช่าหรือกิจกรรมนอกเวลา/วันปิด ให้ปรึกษาผ่านเพจ Facebook; ไม่รับรองราคาเดียวกันทุกเวลา'),
'Q043':('ผู้ติดตาม','นั่งดูเพื่อนเล่นได้; ไม่อนุมานจำนวนผู้ติดตามไม่จำกัด'),
'Q044':('อุปกรณ์ส่วนตัว','อุปกรณ์เสริมส่วนตัวนำมาใช้ได้; คีย์บอร์ด/เมาส์ตามคำตอบก่อนหน้าต้องแจ้ง'),
'Q045':('เวลาเริ่มเช่าเหมา','เลือกเวลาเริ่มเองได้; ยังไม่ทราบชั่วโมงของคำว่าครึ่งวัน/เต็มวัน'),
'Q047':('จองเหมา','ติดต่อผ่านเพจ Facebook'),
'Q048':('เงื่อนไขเช่าเหมา','ให้ติดต่อเพจ Facebook; ไม่อนุมานกฎยกเลิก/คืนเงิน/เกินเวลา'),
'Q049':('หน่วยคิดค่าบริการรายชั่วโมง','ผู้ตอบระบุทั้งหมดคิดต่อคน; ไม่ขยายไปเป็นการคูณราคาเหมาห้องต่อหัว เพราะ Excel ระบุราคาต่อวัน/ครึ่งวันของโซน'),
'Q050':('ภาษี','ราคาในตารางรวมภาษีแล้ว; ไม่ได้ยกเลิกหมายเหตุค่าเจ้าหน้าที่นอกเวลาใน Excel'),
'group_rates':('ราคาเดิม','เจ้าของยืนยันใช้อัตราเดิม ณ เวลาตอบ ไม่สร้างวันเริ่ม/สิ้นสุดย้อนหลัง'),
'group_packages':('ราคาเหมาเดิม','เจ้าของยืนยันราคาเดิม; ต้องผูกกับตารางโซนและหน่วยงาน ไม่ใช้ราคาต่อคนของรายชั่วโมง'),
'group_people':('รายชื่อบุคลากร','เจ้าของยืนยันรายชื่อและตำแหน่งเดิม; ไม่เพิ่มข้อมูลติดต่อส่วนตัวหรือเดาชื่ออังกฤษ'),
'group_inventory':('รายการบริการ','เจ้าของระบุยังไม่มีเปลี่ยนจากรายการเดิม ไม่ใช่ผลตรวจสถานะเครื่องว่างแบบสด'),
}
notes={
'Q009':'ยังไม่ได้ให้จำนวนชั่วโมงแจ้งล่วงหน้า; ใช้ช่องทางติดต่อที่ยืนยัน ไม่ตั้งตัวเลขเพิ่ม',
'Q010':'ผลจัดการรายการ/เงินยังไม่ระบุ ไม่ถามเหตุสมมติกว้างซ้ำ',
'Q014':'วันหมดอายุเครดิตไม่ระบุ ไม่สรุปว่าไม่มีวันหมดอายุ',
'Q015':'เส้นตายโอนเพิ่มยังไม่ระบุ',
'Q019':'คำถามเดิมตั้งสมมติฐานว่าได้คืนเงิน ซึ่งคำตอบไม่ได้ยืนยัน จึงตัดสมมติฐานทิ้ง',
'Q020':'launcher อื่นยังไม่ยืนยัน',
'Q021':'คำถามเดิมรวมหลายแพลตฟอร์มและเรื่องสมาชิก/DLC; เก็บเป็น unknown ตามแพลตฟอร์ม ไม่ใส่คำตอบ Steam ข้ามแพลตฟอร์ม',
'Q025':'จำนวนเวลาต่อและจุดเริ่มนับไม่ระบุ',
'Q033':'กติกาถ่ายสถานที่/บุคคลยังไม่ระบุ ตัดคำถามผสมที่ผู้ตอบตั้งใจตอบเฉพาะในเกม',
'Q034':'สิทธิ์ติดตั้งซอฟต์แวร์สตรีมไม่ระบุ และนโยบายห้ามติดตั้งเองยังอยู่',
'Q038':'ใช้ชื่อผู้ปกครองตาม Q032 ได้ ส่วนชนิดช่องกรอก passport/validation เป็นงานตรวจระบบจอง',
'Q043':'จำนวนผู้ติดตามสูงสุดไม่ระบุ',
'Q044':'ไม่ใช้กฎนี้แทนข้อจำกัดเฉพาะการแข่งขัน',
'Q048':'การเปลี่ยนวัน/คืนเงินของเหมาไม่ระบุ ให้ประสานศูนย์',
'Q049':'เศษเวลาปัดแบบใดไม่ระบุ ไม่สร้างสูตรใหม่',
'Q050':'ค่าเจ้าหน้าที่นอกเวลามีหมายเหตุในต้นทาง ต้องแสดงแยกจากภาษี',
'Q052':'คำถามการรับรอง/เผยแพร่ผสมหลายเรื่องและเป็นงานกระบวนการภายใน ย้ายออกจากแบบถามบริการทั่วไป',
'group_controls':'คำยืนยันว่าของเดิมตรง ไม่ใช้เลือกแทนเมื่อแหล่ง Overcooked สองชุดขัดกันหรือเมื่อยังไม่เคยมีปุ่มในข้อมูล',
}
statements=[]
for key,(topic,text) in facts.items():
 a=responses['answers'].get(key,{})
 statements.append({'id':'owner108:'+key,'kind':'scoped_owner_statement','topic':topic,'answer_th':text,'source_question_id':key,'source_question':old[key]['question'],'source_text':a.get('text'),'source_updated_at':a.get('updated_at'),'limits':notes.get(key),'production_applied':False})
write(R/'SERVICE_STATEMENTS.json',{'created_at':at,'statements':statements,'note':'ข้อความจำกัดขอบเขตตามคำตอบ ไม่ใช่การอนุมัติข้อมูลทั้งหมดในคำถามผสม','production_applied':False})

# Keep imported source units separate from owner facts, with per-topic holds.
holds={'tekken':{16:'pause_conflict',17:'pause_conflict_penalty_unit',34:'pause_conflict',35:'pause_conflict_penalty_scope'},'rov':{85:'malformed_original_sentence',86:'truncated_in_original_docx'}}
documents=[]
ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
for game in ['valorant','cs2','rov','tekken']:
 data=read(R/(game+'_EXTRACT.json'));units=[]
 for p in data['paragraphs']:
  units.append({**p,'source_id':'doc108:'+game,'locator':f"document.xml/paragraph[{p['paragraph']}]",'quality_hold':holds.get(game,{}).get(p['paragraph']),'event_scope_only':True,'language':'en' if game=='valorant' and p['paragraph']>=80 else 'th'})
 tables=[]
 with zipfile.ZipFile(R/'sources'/f'{game}.docx') as z:
  root=ET.fromstring(z.read('word/document.xml'))
  for t in root.findall('.//w:tbl',ns):tables.append([[''.join(c.itertext()) if False else '\n'.join(''.join(n.text or '' for n in p.iter('{'+ns['w']+'}t')) for p in c.findall('.//w:p',ns)) for c in row.findall('w:tc',ns)] for row in t.findall('w:tr',ns)])
 documents.append({'game':game,'source_path':data['original_path'],'sha256':data['sha256'],'units':units,'tables':tables,'is_current_general_studio_policy':False,'note':'เก็บข้อความต้นฉบับครบตามที่อยู่ในไฟล์ ไม่ได้ยืนยันว่าต้นฉบับไม่ขาดหรือกฎไม่มีข้อขัดแย้ง; ไม่เผยแพร่เป็นกฎทั่วไปหรืออ้างเปิดรับสมัครปัจจุบัน'})
write(R/'TOURNAMENT_SOURCE_UNITS.json',{'documents':documents,'production_applied':False})

wb=read(R/'RENTAL_WORKBOOK_EXTRACT.json');sheet=next(iter(wb));prices=[]
for row in wb[sheet][2:]:
 cells=dict(row['cells']);line=row['row']
 for audience,cols in [('external',[(2,'full_day'),(3,'half_day')]),('internal',[(4,'full_day'),(5,'half_day')])]:
  for col,period in cols:
   prices.append({'zone_name':cells[1],'audience':audience,'period_label':period,'amount_thb':int(cells[col]),'room_seats':int(cells[6]),'equipment_included':cells[7].strip(),'locator':f'{sheet}!{chr(64+col)}{line}','duration_minutes':None,'billing_unit':'zone_rental_per_named_period','note':'room_seats คือที่นั่งรองรับห้อง ไม่ใช่จำนวนคนเล่นพร้อมกัน; ห้ามคูณจำนวนคนซ้ำ'})
workbook=Path('D:/Download New/ค่าบริการครึ่งวันและเต็มวัน PSU Esports Studio - Phuket (1).xlsx')
write(R/'RENTAL_SOURCE_RECONCILIATION.json',{'source_path':str(workbook),'source_sha256':digest(workbook),'packages':prices,'overtime_staff_note':dict(wb[sheet][2]['cells'])[8],'duration_hours_missing_in_workbook':True,'owner_confirmation':{'question_id':'group_packages','text':responses['answers']['group_packages']['text']},'production_applied':False})

# One precise owner question per item. New IDs prevent old compound answers being
# mistaken for answers to these narrower questions.
remaining=[
('R108_OPEN_16_18','เวลาเปิดพื้นที่','วันจันทร์–ศุกร์ ช่วง 16:00–18:00 ศูนย์ยังเปิดให้เข้าพื้นที่หรือปิดแล้ว?',['Q039']),
('R108_RENT_HALF_HOURS','ชั่วโมงเหมาครึ่งวัน','ราคาเหมาครึ่งวันครอบคลุมกี่ชั่วโมง?',['Q045']),
('R108_RENT_FULL_HOURS','ชั่วโมงเหมาเต็มวัน','ราคาเหมาเต็มวันครอบคลุมกี่ชั่วโมง?',['Q045']),
('R108_PS5_CONTROLLERS','จอย PS5','PS5 หนึ่งเครื่องมีจอยให้ผู้ใช้กี่จอย?',['Q042']),
('R108_MIXED_RATE','ผู้เล่นต่างกลุ่มราคา','ถ้านักศึกษา PSU กับบุคคลภายนอกมาเล่นด้วยกัน แต่ละคนจ่ายตามกลุ่มราคาของตัวเองใช่ไหม?',['Q051']),
('R108_PAYER','ผู้โอนเงิน','ผู้เล่นร่วมที่มีชื่อในรายการจอง โอนเงินแทนผู้จองหลักได้หรือไม่?',['Q013']),
('R108_TEKKEN_PAUSE','กติกา Pause ของ Tekken','Tekken รายการ PSU Esports ปะทะมันส์ สนั่นจอ ให้ใช้กฎใด: ห้าม Pause ทุกกรณี หรือ Pause ได้เมื่อทุกคนยินยอมและมีเหตุเหมาะสม?',['special:1']),
('R108_TEKKEN_PENALTY','หน่วยโทษ Tekken','ข้อความ Tekken ว่า “กดหยุดเกมโดยเจตนา ปรับแพ้ 1 รอบ” หมายถึงแพ้ Round เดียว แพ้ Game หรือแพ้ Match?',['special:1']),
('R108_ROV_615','ข้อความ RoV 6.1.5','RoV Blueket Games 2025 ข้อ 6.1.5 ลงท้ายว่า “และอื่น ๆ ที่ต้องห้ามตามกฎหมายการแข่งขันทันที” ต้องการให้แก้ประโยคนี้เป็นข้อความใด?',['special:2']),
('R108_ROV_6151','ข้อความ RoV 6.1.5.1','RoV Blueket Games 2025 ข้อ 6.1.5.1 จบค้างที่ “ตัดสิทธิ์ทีมผู้เข้าแข่งขันดังกล่าวออกจาก” ข้อความต่อจากนี้คืออะไร?',['special:2']),
]
qnew=[{'id':key,'title':title,'question':text,'original_question_ids':refs,'known_answer':''} for key,title,text,refs in remaining]
write(F/'simple_questions.json',{'schema_version':'psu-simple-owner-form-2','review_id':'r108_owner_intake_20261020','created_at':at,'questions':qnew,'count':len(qnew),'note':'เฉพาะข้อชัดเจนที่ยังต้องให้เจ้าของตัดสิน คำตอบเดิมทุกข้อยังเก็บแยก; ไม่ใช่จำนวนช่อง unknown ของฐานข้อมูลทั้งหมด','production_applied':False})
removed={'Q023','Q031','Q035','Q036'};actions=[]
for n,q in enumerate(before['questions'],1):
 key=q['id'];answer=responses['answers'].get(key,{}).get('text','');follow=[v['id'] for v in qnew if key in v['original_question_ids'] or key.startswith('book:') and (('tekken' in key and 'TEKKEN' in v['id']) or ('rov_' in key and 'ROV_' in v['id']))]
 if key in removed:action='removed_as_user_requested';reason='ไม่ใช่คำตอบว่าอนุญาต/ห้าม และไม่ลบข้อเท็จจริงเดิมที่เกี่ยวข้อง'
 elif key.startswith('book:'):action='document_received';reason='อ่าน DOCX ที่ส่งมาแล้ว; ใช้เฉพาะรายการแข่งขันในชื่อเอกสาร; ข้อขัดแย้ง/ขาดจริงถามแยก'
 elif key=='Q046':action='existing_source_resolved';reason='ข้อความให้ไปดูข้อมูลเป็นคำสั่งงาน; อ่าน Excel แล้วมีอุปกรณ์และความจุครบ'
 elif key=='group_controls':action='assistant_research';reason='คำยืนยันของเดิมกับคำสั่งค้นของที่ไม่มีแยกกัน ไม่สร้างผังปุ่มเอง'
 elif follow:action='split_specific_remaining';reason='เก็บคำตอบที่ตอบได้แล้ว และถามใหม่ทีละประเด็นที่ยังต้องตัดสิน'
 elif key in ['Q038','Q052']:action='internal_task_or_broad_question_removed';reason=notes[key]
 else:action='received_scoped_answer';reason=notes.get(key,'เก็บคำตอบตามขอบเขตที่ตอบ ไม่ถามเงื่อนไขสมมติเพิ่ม')
 actions.append({'old_display_number':n,'id':key,'old_question':q['question'],'original_question_ids':q['original_question_ids'],'raw_answer':answer,'action':action,'reason':reason,'followup_ids':follow})
write(R/'QUESTION_REVIEW_ALL_56.json',actions)
write(R/'REMAINING_OWNER_QUESTIONS.json',qnew)
write(R/'UNKNOWN_FACETS_NOT_REASKED.json',{'note':'คงเป็น unknown/จำกัดคำตอบหรือส่งต่อผู้ดูแล ไม่ถือว่าครบจากการลดจำนวนคำถาม','facets':notes})
write(R/'ASSISTANT_ACTIONS.json',[
 {'id':'rental_source','status':'done','source':'RENTAL_SOURCE_RECONCILIATION.json','result':'24 ราคา 6 โซน 2 กลุ่มหน่วยงาน 2 ช่วง พร้อมอุปกรณ์/ที่นั่ง; ไม่พบชั่วโมง'},
 {'id':'rulebook_import','status':'done_with_source_holds','source':'TOURNAMENT_SOURCE_UNITS.json','result':'อ่านครบ 4 DOCX เก็บข้อความและตาราง; ไม่เติมท้าย RoV หรือเลือก Pause Tekken เอง'},
 {'id':'controls_missing','status':'researched_exact_layout_unverified','source':'CONTROL_RESEARCH_TH.md','result':'ข้อมูลหลักที่ตรวจยังไม่ยืนยันปุ่มทุกปุ่มของ preset ที่ศูนย์; ไม่ใช้ผัง PC แทน PS5'},
 {'id':'booking_identity_field','status':'requires_booking_form_inspection','source_question_id':'Q038','result':'แยกจากคำถามเด็ก/ผู้ปกครอง; ไม่ให้เจ้าของตอบชื่อตัวแปรระบบ'},
 {'id':'physical_filming','status':'unknown_scoped_out','source_question_id':'Q033','result':'คำตอบ capture เกมไม่ตอบนโยบายถ่ายบุคคล/สถานที่'},
 {'id':'accounts_other_than_steam','status':'unknown_scoped_out','source_question_id':'Q021','result':'ไม่ยืนยัน PS5/Switch/VR subscriptions หรือ DLC ด้วยคำตอบ Steam'},
])

lines=['# ตรวจคำตอบและเอกสาร R108','',f'ตรวจเมื่อ {at}','',
'## สรุป','',f'- ตรวจแบบเดิมครบ {len(actions)} ข้อ และเก็บข้อความตอบดิบทั้งหมดแยกไว้',
'- เอาข้อ 19 / 26 / 30 / 31 ออกจากแบบถาม: Q023 / Q031 / Q035 / Q036',
f'- แบบเว็บเหลือ {len(qnew)} ข้อเจาะจง หมายเลขใหม่เริ่ม 1; ข้อความเดิมและประวัติไม่ได้ถูกลบ',
'- ข้อที่ตอบไว้แล้วใช้ได้ตามเรื่องที่ตอบ ไม่ตีความว่าทุกเงื่อนไขในคำถามผสมได้รับคำตอบแล้ว',
'- รับเข้าเป็นชุดข้อมูลตรวจสอบ R108 ยังไม่ได้ติดตั้งทับแชท R78 หรือเปลี่ยน frozen R106 และไม่ได้รันคำถาม LLM/test ใหม่','',
'## เอกสารแข่งขัน','',
'อ่านครบ 4 ไฟล์และเก็บ SHA-256 สำเนาต้นฉบับ ข้อความแต่ละย่อหน้าและตาราง CS2 ไว้ที่ SOURCE_MANIFEST.json / TOURNAMENT_SOURCE_UNITS.json คำสั่งผู้จัดในกติกาเป็นเนื้อหากฎของงานนั้น ไม่ใช่คำสั่งให้โปรแกรมเปลี่ยนนโยบายศูนย์','',
'### Tekken','',
'- P0016 ห้ามหยุดเกมทุกเหตุผล; P0034 อนุญาตเมื่อทุกคนยินยอมและมีเหตุเหมาะสม เป็นความขัดแย้งในไฟล์เดียวกัน',
'- P0017 ปรับแพ้ 1 รอบทันที; P0035 โทษเช่นเดียวกับการออกจากเกมโดยไม่ได้รับอนุญาต (P0033) ยังต้องยืนยันหน่วยและเงื่อนไข ห้ามเลือกกฎใดเอง',
'- FT2 / Round 3 / Timer 60s / PS5 / เดี่ยว / ไม่ใช้ DLC และกฎอื่นที่ไม่ได้ขัดกันเก็บได้โดยแยกหัวข้อ ไม่ต้องกั้นทั้งเล่มเพราะปัญหา Pause จุดเดียว','',
'### RoV','',
'- P0085 ข้อ 6.1.5 มีถ้อยคำรวมผิดลักษณะ “ตามกฎหมายการแข่งขันทันที” และ P0086 ข้อ 6.1.5.1 ตัดค้างที่ “ออกจาก” จริงใน DOCX ต้นฉบับ ไม่ใช่แค่ migration ขาด',
'- รูปฝังมีเพียงโลโก้ Blueket Games 2025 ตรวจภาพแล้ว ไม่มีหน้ากฎต่อที่ซ่อนในรูป',
'- ส่วนอื่นคงข้อความ: BO3 ทุกรอบ / Global Ban-Pick / 18 ฮีโร่ขั้นต่ำ / Default skin / โทรศัพท์มือถือเท่านั้น ไม่อนุญาต Tablet/iPad',
'- กฎความปลอดภัย P0053 กับความเจ็บป่วย P0061 ต้องคงบริบทต่างกัน ไม่สรุปให้ฝืนเล่นเมื่อไม่ปลอดภัย',
'- งานลงวันที่ 11 กันยายน 2568 จึงต้องตอบโดยระบุรายการ/ปี ไม่บอกว่าวันสมัคร/วันแข่งยังเป็นปัจจุบัน','',
'### CS2 และ VALORANT','',
'- CS2 P0017 จำกัดผู้แข่งนักศึกษา PSU ภูเก็ต ไม่ใช้ขยายไปปฏิเสธผู้ใช้บริการทั่วไป; P0029 รายชื่อแผนที่เป็นของรายการ 2026 ตามเอกสาร ไม่ใช่ active pool ทั่วโลก',
'- CS2 เก็บ penalty table เป็นแถวคู่การละเมิด/บทลงโทษ ป้องกันจับบทลงโทษผิดรายการ',
'- VALORANT มีไทยและอังกฤษ (Update 17/02/2026) เก็บแยกภาษา มีเลือกฝั่งด้วยโยนเหรียญในไทย P0037 แต่ไม่พบข้อภาษาอังกฤษตรงกัน จึงไม่ถือว่าฉบับอังกฤษครอบคลุมทุกหัวข้อ',
'- ไม่อนุมานค่าสมัคร/อายุขั้นต่ำเป็น 0 หรือไม่มีข้อจำกัดเมื่อเอกสารไม่ได้ระบุ; ไม่ให้ข้อมูลนอกเอกสารเติมเป็นกฎผู้จัดโดยอัตโนมัติ','',
'## ราคาเหมาและความจุ','',
'อ่านไฟล์ค่าบริการครึ่งวันและเต็มวันเดิมครบแล้ว มี 24 ราคา จาก 6 โซน × 2 กลุ่มหน่วยงาน × 2 ระยะ มีความจุที่นั่งและอุปกรณ์ครบตามคอลัมน์ F/G แต่ไม่มีจำนวนชั่วโมงหรือเงื่อนไขยกเลิก จึงเหลือถามเฉพาะชั่วโมงครึ่งวัน/เต็มวัน ไม่ให้พิมพ์ตารางราคาใหม่','',
'- All Zones: ภายนอกเต็ม/ครึ่งวัน 12,000/6,000; ภายใน 6,000/3,000 บาท; รองรับ 50 ที่นั่ง; อุปกรณ์เกมทั้งหมด',
'- Cockpit: 2,000/1,000 และ 1,000/500; 35 ที่นั่ง; 2 เครื่อง',
'- VR: 6,000/3,000 และ 3,000/1,500; 34 ที่นั่ง; VR 1 เครื่อง',
'- Nintendo Switch: 2,000/1,000 และ 1,000/500; 37 ที่นั่ง; 1 เครื่อง',
'- PS5: 2,000/1,000 และ 1,000/500; 37 ที่นั่ง; 2 เครื่อง',
'- PC: 4,000/2,000 และ 2,000/1,000; 43 ที่นั่ง; 10 เครื่อง',
'- จำนวนที่นั่งห้องในไฟล์เหมาต้องไม่สลับกับจำนวนคนเล่นพร้อมกันของการจองเครื่อง',
'- หมายเหตุ H3: ค่าตอบแทนเจ้าหน้าที่นอกเวลาเบิกตามระเบียบมหาวิทยาลัย จึงไม่สรุปว่า “รวมภาษีแล้ว” แปลว่าไม่มีค่าเจ้าหน้าที่เพิ่ม',
'- คำยืนยัน “ราคาเดิม” เป็นหลักฐานเวลาตอบ ไม่เปลี่ยนช่วง validity เก่าย้อนหลังหรือกำหนดวันหมดอายุเอง','',
'## คำตอบที่ต้องคงขอบเขต','',
'- Q021 ตอบ Steam ซ้ำ แม้คำถามถาม console: เก็บ Steam อย่างเดียว ไม่ใส่ PS Plus/Nintendo online/DLC ว่ามีให้',
'- Q026 เปลี่ยนเครื่องเมื่อเปิดเกมไม่ได้จากเหตุอื่น แยกจากกรณีรออัปเดตที่คำตอบเดิมห้ามเปลี่ยน',
'- Q033 อนุญาต capture เกมแล้วลบ ไม่แปลว่าอนุญาตถ่ายคน/สถานที่',
'- Q013 ผู้โอนที่มีรายชื่อยังใช้คำกำกวม จึงถาม yes/no ให้ตัดสินตรง ๆ',
'- การลบข้ออาหาร/เด็ก/ขอเพิ่มเกมเป็นการลบคำถามกว้าง ไม่ใช่ลบหรือกลับข้อเท็จจริงเก่าที่ทราบแล้ว',
'- ทุก facet ที่คำตอบยังไม่ครอบคลุมอยู่ใน UNKNOWN_FACETS_NOT_REASKED.json ไม่ถูกนับว่าครบเพียงเพราะหน้าคำถามสั้นลง','',
'## คำถามค้างในเว็บ','']
for i,q in enumerate(qnew,1):lines.append(f"{i}. {q['question']}")
lines+=['','## บันทึกการจัดการครบ 56 ข้อ','', '| ข้อเดิม | ID | จัดการ | เหตุผล |','|---|---|---|---|']
for a in actions:lines.append(f"| {a['old_display_number']} | {a['id']} | {a['action']} | {a['reason']} |")
lines+=['','## หลักฐานและข้อจำกัด','',
'- REPLIES_REVIEWED.json เก็บข้อความร่างเดิมพร้อมบริบท ไม่แก้สถานะ submitted_at ให้ดูเหมือนเจ้าของกดส่ง',
'- SERVICE_STATEMENTS.json เป็นคำตอบจำกัดขอบเขต; TOURNAMENT_SOURCE_UNITS.json เป็นข้อมูลเอกสารอ้างอิง; ไม่ใช่การ mark complete ทุกกฎ 104 ข้อ',
'- ไม่รับรองว่าการย้ายเข้าระบบตอบจริงเสร็จในรอบนี้ งานนี้ตรวจข้อมูลและจัดหน้าคำถามให้ตรงคำตอบก่อน',
'- ตรวจ HTTP/API และความคงเดิมของไฟล์ข้อมูล/ประวัติ; browser automation ใช้งานไม่ได้ในสภาพแวดล้อมนี้ จึงยังไม่อ้างตรวจภาพหน้าเว็บจริง']
(R/'INTAKE_REVIEW_TH.md').write_text('\n'.join(lines),'utf8')
write(R/'SUMMARY.json',{'old_question_count':len(actions),'remaining_owner_questions':len(qnew),'explicitly_removed_old_numbers':[19,26,30,31],'scoped_statements':len(statements),'document_count':len(documents),'source_units':sum(len(d['units']) for d in documents),'rental_prices':len(prices),'production_applied':False,'llm_calls':0})
print(json.dumps(read(R/'SUMMARY.json'),ensure_ascii=False))
