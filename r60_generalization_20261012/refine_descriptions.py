from prepare import SYSTEM,B
import json,shutil
p=SYSTEM/'app/knowledge/common/schema_descriptions.json'
backup=B/'schema_descriptions_round1.json';assert not backup.exists();shutil.copy2(p,backup)
data=json.loads(p.read_text(encoding='utf-8'))
TH={
'how_to_play':'เป้าหมายของเกม วิธีเริ่มเล่น สิ่งที่ต้องทำระหว่างเล่นและลำดับการเล่นโดยสรุป ไม่ใช่วิธีชนะทุกด่าน',
'eligibility':'คุณสมบัติและบุคคลที่มีสิทธิ์อยู่ในกลุ่มนี้ ไม่ใช่เอกสารที่ใช้พิสูจน์สิทธิ์',
'required_proofs':'เอกสารหรือสิ่งที่ต้องยื่นแสดงเพื่อพิสูจน์ว่ามีสิทธิ์ในกลุ่มผู้ใช้นี้',
'state':'สถานะเปิดหรือปิด หรือปรับเวลาพิเศษของวันที่ประกาศ',
'freshness_policy':'ระยะเวลาที่ข้อมูลสดยังใช้ยืนยันได้ อายุข้อมูล การหมดอายุ และเวลาแคช',
'status_mapping':'ความหมายของรหัสสถานะจากระบบ หรือการแปลรหัสเหล่านั้นให้เป็นสถานะที่เข้าใจได้',
'body':'เนื้อหาข่าวหรือประกาศ ว่าแจ้งรายละเอียดเรื่องใด',
'offered':'ศูนย์มีเกมนี้ให้เล่นในบริการที่เลือกหรือยัง และยืนยันว่ามีหรือไม่มี',
'game_version':'รุ่นหรือเวอร์ชันของเกมที่ติดตั้ง',
'rulebook_release':'ฉบับ รุ่น หรือเวอร์ชันของกฎการแข่งขันที่รายการนี้ใช้อ้างอิง',
'competition_dates':'วันและวันที่จัดการแข่งขัน',
'role':'หน้าที่ ความรับผิดชอบ และสิ่งที่บุคคลนี้ดูแล',
'bindings':'การควบคุม คำสั่งแต่ละอย่างกับปุ่มที่ต้องกดและวิธีกด',
'session_minutes':'ระยะเวลาเล่นจริงที่ผู้ใช้ได้รับจากหนึ่งรอบบริการ เป็นนาที',
'occupancy_minutes':'ระยะเวลาที่ระบบจองกันหรือล็อกเครื่องเอาไว้ เป็นนาที อาจไม่เท่ากับเวลาเล่นจริง',
}
for key,text in TH.items():data['fields'][key]['description_th']=text
data['version']=2
p.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8');print('Refined developer semantics; no catalog/owner fact edits')
