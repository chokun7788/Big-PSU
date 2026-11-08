import sys,json,re
from pathlib import Path
import r41_probe as p
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r48_current_path.txt').read_text());p.OUT=OUT
Q={
'university':('เป็นร้านเกมทั่วไปหรือเป็นของมหาวิทยาลัย?','Is this a university facility or a regular gaming cafe?'),
'membership':('ต้องเป็นสมาชิกก่อนไหม?','Do I need to be a member first?'),
'spectators':('ไปนั่งดูเพื่อนเล่นเฉย ๆ ได้ไหม?','Can I sit and watch my friends play?'),
'walk_in':('เดินเข้าไปใช้บริการเลยได้ไหม หรือต้องจอง?','Can I walk in or do I still need to book?'),
'location':('อยู่ตึกอะไร ชั้นไหน?','Which building and floor is the studio in?'),
'map':('มีลิงก์แผนที่ไหม?','Can I have the studio map link?'),
'parking':('มีที่จอดรถไหม?','Is there parking for cars and motorcycles?'),
'contact':('ถ้าหาศูนย์ไม่เจอ ติดต่อใครได้?','Who do I contact if I cannot find the studio?'),
'four_people':('มากันสี่คน ควรเลือกเครื่องไหน?','There are four of us. Which service should we choose?'),
'player_identity':('คนจองเป็นคนนึงแต่คนเล่นเป็นอีกคนสามารถทำได้ไหม','Can someone who is not listed in my booking play instead of me?'),
'checkin_documents':('ตอนมาถึงต้องแสดงหลักฐานอะไร?','What identification can I show when I arrive?'),
'change_machine':('จองผิดเครื่อง เปลี่ยนได้ไหม?','I booked the wrong machine. How can I change it?'),
'change_time':('เปลี่ยนเวลาจองได้ไหม?','How do I change my booking time?'),
'personal_keyboard_mouse':('เอาคีย์บอร์ดหรือเมาส์ตัวเองมาใช้ได้ไหม?','Can I bring my own keyboard or mouse for normal studio use?'),
'wrong_slip':('แนบสลิปผิดรูป เปลี่ยนได้ไหม?','I uploaded the wrong payment slip image. What should I do?'),
'combined_transfer':('จองหลายเครื่อง โอนครั้งเดียวได้ไหม?','Can I make one transfer for multiple machines?'),
'group_checkin':('มาก่อนหนึ่งคน เช็กอินแทนทั้งกลุ่มได้ไหม?','Can the first person to arrive check in for the whole group?'),
'rest_seating':('มีที่นั่งพักไหม','Is there somewhere to sit and rest?'),
}
CONTENT={
'university':(['มหาวิทยาลัย'],['university']),
'membership':(['ไม่ต้อง'],['not required']),
'spectators':(['ดู'],['watch']),
'walk_in':(['จอง','ระบบ'],['book','system']),
'location':(['อาคาร 5','ชั้น 1','83120'],['Building 5','Floor 1','83120']),
'map':(['https://maps.app.goo.gl/Ahst2vyFM4GDmC5s5'],['https://maps.app.goo.gl/Ahst2vyFM4GDmC5s5']),
'parking':(['รถยนต์','มอเตอร์ไซค์','5'],['cars','motorcycles','Building 5']),
'contact':(['https://www.facebook.com/psuesportsphuket'],['https://www.facebook.com/psuesportsphuket']),
'four_people':(['Nintendo Switch'],['Nintendo Switch']),
'player_identity':(['รายชื่อ','จอง'],['named','booking','cannot']),
'checkin_documents':(['บัตรประชาชน','บัตรนักศึกษา','บัตรนักเรียน','Passport'],['national ID','university student','school student','passport']),
'change_machine':(['ยกเลิก','อีเมล','ใหม่'],['cancel','email','new booking']),
'change_time':(['ยกเลิก','อีเมล','ใหม่'],['cancel','email','new booking']),
'personal_keyboard_mouse':(['ไม่อนุญาต','คีย์บอร์ด','เมาส์'],['not allowed','keyboards','mice']),
'wrong_slip':(['สลิป','https://www.facebook.com/psuesportsphuket'],['slip','https://www.facebook.com/psuesportsphuket']),
'combined_transfer':(['ครั้งเดียว','Note','ตรวจสอบ'],['one','note','verify']),
'group_checkin':(['ไม่ได้','รายคน','มาก่อน'],['cannot','individually','first']),
'rest_seating':(['กลางห้อง'],['central']),
}
def cases():
    return [dict(id=f'{lang}-{key}',locale=lang,turns=[Q[key][lang=='en']],key=key) for lang in ('th','en') for key in Q]
def grade(c,rs):
    b=rs[-1]['response'];answer=b.get('answer','');required=CONTENT[c['key']][c['locale']=='en']
    checks=dict(transport=rs[-1]['status']==200 and b.get('ok') is True,content=all(x.casefold() in answer.casefold() for x in required),not_no_answer='no_answer' not in b.get('mode',''),no_timeout=not b.get('timed_out'),english_no_thai=not re.search('[\u0e00-\u0e7f]',answer) if c['locale']=='en' else True)
    if c['key']=='player_identity' and c['locale']=='th':
        checks['unlisted_player_denied']=bool(re.search(r'ไม่ได้|ไม่สามารถ.+ได้',answer))
    if b.get('mode')=='pipeline:user_service_facts':
        meta=next((t.get('metadata',{}) for t in b.get('trace',[]) if t['stage']=='user_service_facts'),{})
        checks['correct_claim']=c['key'] in meta.get('claim_ids',[])
        checks['source_provenance']='local://service_policy/user_answers_20261008' in answer
    return dict(id=c['id'],passed=all(checks.values()),checks=checks,mode=b.get('mode'),answer=answer,records=rs)
p.cases=cases;p.grade=grade
if __name__=='__main__':p.run(sys.argv[1],sys.argv[2])
