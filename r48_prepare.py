import json,uuid,hashlib,shutil
from pathlib import Path
BASE=Path(__file__).resolve().parent;ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
OUT=BASE/('r48_user_facts_20261008_'+uuid.uuid4().hex[:8]);OUT.mkdir();(BASE/'r48_current_path.txt').write_text(str(OUT))
before={}
for folder in ('app','tests','data/curated','data/rules','web_chat'):
    for p in (ROOT/folder).rglob('*'):
        if p.is_file() and '__pycache__' not in p.parts:
            rel=p.relative_to(ROOT);d=OUT/'before'/rel;d.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,d);before[rel.as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
(OUT/'before_manifest.json').write_text(json.dumps(before,indent=2))
questions='''เป็นร้านเกมทั่วไปหรือเป็นของมหาวิทยาลัย?
ต้องเป็นสมาชิกก่อนไหม?
ไปนั่งดูเพื่อนเล่นเฉย ๆ ได้ไหม?
เดินเข้าไปใช้บริการเลยได้ไหม หรือต้องจอง?
ศูนย์อยู่ตรงไหน?
อยู่ตึกอะไร ชั้นไหน?
มีลิงก์แผนที่ไหม?
ไปถึงก่อนเวลาจองต้องรอตรงไหน?
มีที่จอดรถไหม?
ถ้าหาศูนย์ไม่เจอ ติดต่อใครได้?
มีเกมไหนเล่นกับเพื่อนได้บ้าง?
มากันสองคน มีอะไรเล่นด้วยกันได้?
มากันสี่คน ควรเลือกเครื่องไหน?
มา4คนสามารถเล่นเครื่อง2คนได้ไหมแล้วสลับกัน
ถ้าอยากเล่นเกมที่ไม่มีในรายการ ขอให้ลงเพิ่มได้ไหม?
คนจองเป็นคนนึงแต่คนเล่นเป็นอีกคนสามารถทำได้ไหม
ตอนมาถึงต้องแสดงหลักฐานอะไร?
จองผิดเครื่อง เปลี่ยนได้ไหม?
เปลี่ยนเวลาจองได้ไหม?
ไปสายสิบห้านาทียังเล่นได้หรือเปล่า?
ถ้าไปไม่ทัน ต้องแจ้งใคร?
เล่นอยู่แล้วอยากต่อเวลา ทำยังไง?
อยากเปลี่ยนจาก PC ไปเล่น PS5 ต้องจองใหม่ไหม?
ต้องใช้บัญชี Steam ของตัวเองไหม?
เครื่องค้างหรือดับระหว่างเล่น เวลาที่เสียไปคิดยังไง?
ลืมออกจากบัญชีหลังเล่น ต้องติดต่อใคร?
เอาคีย์บอร์ดหรือเมาส์ตัวเองมาใช้ได้ไหม?
ถ่ายรูปหรืออัดวิดีโอได้ไหม?
สตรีมเกมจากเครื่องของศูนย์ได้ไหม?
ติดตั้งเกม โปรแกรม หรือ mod เองได้ไหม?
เด็กเข้าใช้บริการได้ไหม ต้องมีผู้ปกครองหรือเปล่า?
ที่นั่งที่ระบุคือจำนวนคนเล่นพร้อมกันหรือจำนวนที่นั่งในห้อง?
ขอใบเสนอราคาหรือใบเสร็จได้ไหม?
ศูนย์มีบัญชีเกมให้ยืมหรือเปล่า?
เกมอัปเดตเวอร์ชันล่าสุดแล้วหรือยัง?
ถ้าไปถึงแล้วเกมต้องอัปเดต เวลาจะเริ่มนับเลยไหม?
เกมกำลังอัปเดต เปลี่ยนไปใช้เครื่องอื่นได้ไหม?
ต้องใช้ชื่อจริงตรงกับบัตรไหม?
กรอกเบอร์โทรผิด ต้องจองใหม่ไหม?
จ่ายจากบัญชีของเพื่อนได้หรือเปล่า?
โอนเกินจำนวนที่ต้องจ่าย ทำยังไง?
โอนขาดไปนิดหนึ่ง ต้องโอนเพิ่มหรือจองใหม่?
แนบสลิปผิดรูป เปลี่ยนได้ไหม?
จองหลายเครื่อง โอนครั้งเดียวได้ไหม?
จองผิดวัน แต่จ่ายแล้ว แก้ได้ไหม?
ขอเลื่อนเป็นวันอื่นแทนคืนเงินได้ไหม?
ถ้าศูนย์ปิดพิเศษหลังจองแล้ว จะจัดการรายการยังไง?
ฝนตกหนักเดินทางไม่ได้ ขอเปลี่ยนรอบได้ไหม?
มาก่อนหนึ่งคน เช็กอินแทนทั้งกลุ่มได้ไหม?
มีที่นั่งพักไหม'''.splitlines()
answers={1:'เป็นของมหาวิทยาลัย',2:'ไม่ต้องเป็นสมาชิกก็สามารถใช้บริการได้',3:'ดูได้',4:'ในกรณี walk in ก็ต้องจองผ่านระบบ',5:'อาคาร 5 ชั้น 1 มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต 80 หมู่ 1 ถ.วิชิตสงคราม อ.กะทู้ จ.ภูเก็ต 83120',6:'อาคาร 5 ชั้น 1 มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต 80 หมู่ 1 ถ.วิชิตสงคราม อ.กะทู้ จ.ภูเก็ต 83120',7:'https://maps.app.goo.gl/Ahst2vyFM4GDmC5s5',9:'มีที่ตอดรถหน้าตึก 5 สำหรับรถยนต์และมอเตอร์ไซค์',10:'ติดต่อผ่านเพจศูนย์อีสปอร์ต https://www.facebook.com/psuesportsphuket',13:'Nintendo Swich',16:'ไม่ได้ คนเล่นต้องเป็นคนที่จองมาหรือมีรายชื่ออยู่ในรายการจอง',17:'บัตรประชาชน หรือบัตรนักศึกษา หรือบัตรนักเรียน หรือ passport',18:'ให้กดยกเลิกผ่านอีเมล และจองเข้ามาใหม่',19:'ให้กดยกเลิกผ่านอีเมล และจองเข้ามาใหม่',27:'อันนี้ไม่ได้',43:'ให้ส่งสลิปมาทางเพจศูนย์อีสปอร์ต',44:'ได้ แต่ต้องเขียน note ตอนจองเข้ามา เพื่อให้ทางศูนย์ตรวจสอบ',45:'ในกรณีที่มีการจ่ายเงินเรียบร้อย สามารถเปลี่ยนวันได้',46:'ไม่ได้',47:'ไม่เข้าใจคำถาม4',49:'ไม่ได้ จะเช็คเป็นรายคน แต่คนที่มาก่อนสามารถเล่นได้',50:'มี ตรงโซนกลางห้อง'}
raw=dict(schema_version=1,source_id='user_service_answers_20261008',received_date='2026-10-08',effective_date=None,basis='user_provided_in_this_chat',items=[dict(number=i,question=q,answer=answers.get(i),status='needs_question_clarification' if i==47 else 'scope_confirmation_pending' if i in (45,46) else 'user_confirmed' if i in answers else 'unanswered') for i,q in enumerate(questions,1)])
with (OUT/'USER_INPUT_50.json').open('x',encoding='utf-8') as f:json.dump(raw,f,ensure_ascii=False,indent=2)
claims={}
def claim(key,nums,th,en,category='reservation'):
    claims[key]=dict(source_items=nums,status='user_confirmed',category=category,answers=dict(th=th,en=en))
fb='https://www.facebook.com/psuesportsphuket';mp=answers[7]
claim('university',[1],'PSU Esports Studio - Phuket เป็นศูนย์ของมหาวิทยาลัยสงขลานครินทร์ครับ','PSU Esports Studio - Phuket is a university facility of Prince of Songkla University.','overview')
claim('membership',[2],'ไม่ต้องเป็นสมาชิกก็สามารถใช้บริการได้ครับ','Membership is not required to use the studio.')
claim('spectators',[3],'สามารถมานั่งดูเพื่อนเล่นได้ครับ','You may sit and watch your friends play.')
claim('walk_in',[4],'Walk-in ได้ แต่ยังต้องจองผ่านระบบก่อนใช้บริการครับ','Walk-in visitors must still book through the reservation system before using the service.')
claim('location',[5,6],'ศูนย์อยู่ที่'+answers[5]+'ครับ','The studio is in Building 5, Floor 1, Prince of Songkla University, Phuket Campus, 80 Moo 1 Vichitsongkram Road, Kathu, Phuket 83120.','contact')
claim('map',[7],'ลิงก์แผนที่ศูนย์: '+mp,'Studio map: '+mp,'contact')
claim('parking',[9],'มีที่จอดรถหน้าตึก 5 สำหรับรถยนต์และมอเตอร์ไซค์ครับ','Parking for cars and motorcycles is available in front of Building 5.','contact')
claim('contact',[10],'ติดต่อผ่านเพจศูนย์อีสปอร์ตได้ครับ: '+fb,'Contact the studio Facebook page: '+fb,'contact')
claim('four_people',[13],'มากัน 4 คน แนะนำ Nintendo Switch ครับ','For a group of four, the recommended service is Nintendo Switch.','equipment')
claim('player_identity',[16],'คนเล่นต้องเป็นคนที่จองหรือมีรายชื่ออยู่ในรายการจอง ไม่สามารถให้ผู้ที่ไม่มีรายชื่อมาใช้แทนได้ครับ','The player must be the person who booked or be named in the booking. Someone not listed cannot use the booking instead.')
claim('checkin_documents',[17],'เมื่อมาถึงให้แสดงบัตรประชาชน บัตรนักศึกษา บัตรนักเรียน หรือ Passport อย่างใดอย่างหนึ่งครับ','At arrival, present a national ID card, university student card, school student card, or passport.')
claim('change_machine',[18],'กรณีจองผิดเครื่อง ให้กดยกเลิกผ่านอีเมล แล้วจองเข้ามาใหม่ครับ','If you booked the wrong machine, cancel through the email and make a new booking.')
claim('change_time',[19],'หากต้องการเปลี่ยนเวลาจอง ให้กดยกเลิกผ่านอีเมล แล้วจองเข้ามาใหม่ครับ','To change the booking time, cancel through the email and make a new booking.')
claim('personal_keyboard_mouse',[27],'ไม่อนุญาตให้นำคีย์บอร์ดหรือเมาส์ส่วนตัวมาใช้ครับ','Personal keyboards and mice are not allowed for general studio use.','rules')
claim('wrong_slip',[43],'กรณีแนบสลิปผิดรูป ให้ส่งสลิปมาทางเพจศูนย์อีสปอร์ตครับ: '+fb,'If you uploaded the wrong payment slip image, send the slip to the studio Facebook page: '+fb)
claim('combined_transfer',[44],'จองหลายเครื่องสามารถโอนเงินครั้งเดียวได้ แต่ต้องเขียน Note ตอนจอง เพื่อให้ศูนย์ตรวจสอบครับ','You may make one bank transfer for multiple machines, but you must add a note when booking so the studio can verify it.')
claim('group_checkin',[49],'เช็กอินแทนทั้งกลุ่มไม่ได้ ศูนย์ตรวจเป็นรายคน แต่คนที่มาก่อนสามารถเล่นได้ครับ','You cannot check in for the whole group. Each person is checked individually, but those who arrive first may play.')
claim('rest_seating',[50],'มีที่นั่งพักตรงโซนกลางห้องครับ','Rest seating is available in the central area of the room.','equipment')
facts=dict(schema_version=1,source_id=raw['source_id'],source_url='local://service_policy/user_answers_20261008',received_date='2026-10-08',effective_date=None,basis=raw['basis'],raw_sha256=hashlib.sha256((OUT/'USER_INPUT_50.json').read_bytes()).hexdigest(),english_status='agent_translation_from_user_confirmed_thai',claims=claims,pending_boundary=dict(items=[45,46],answers_th={str(i):answers[i] for i in (45,46)},question='Scope/exception and processing channel for paid-date change versus rescheduling instead of refund'))
with (OUT/'FACTS_STAGED.json').open('x',encoding='utf-8') as f:json.dump(facts,f,ensure_ascii=False,indent=2)
print(json.dumps(dict(out=str(OUT),active_claims=len(claims),statuses={s:sum(x['status']==s for x in raw['items']) for s in set(x['status'] for x in raw['items'])}),ensure_ascii=False))
