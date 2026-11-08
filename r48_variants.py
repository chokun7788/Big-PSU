import sys,re
import r48_probe as p
VARIANTS={
 'university':('ศูนย์นี้เป็นของมหาลัยใช่ไหม','Who owns the studio?'),
 'membership':('ไม่ได้เป็นสมาชิกเข้าใช้ได้ไหม','Can a non-member use the studio?'),
 'spectators':('ไม่เล่นเอง แค่นั่งดูเพื่อน ได้หรือเปล่า','Can I just watch rather than play?'),
 'walk_in':('walk-in ยังต้องจองในระบบใช่ไหม','Do walk-in visitors need a reservation?'),
 'location':('ศูนย์อยู่ไหน ขอที่อยู่หน่อย','What is the address of the studio?'),
 'map':('ขอลิงก์แผนที่ไปศูนย์หน่อย','Please share a map to the studio.'),
 'parking':('รถยนต์กับมอเตอร์ไซค์มีที่จอดไหม','Where is the parking?'),
 'contact':('หาศูนย์ไม่เจอ ติดต่อทางไหน','How can I contact the studio?'),
 'four_people':('มากัน 4 คนแนะนำเครื่องอะไร','Which service would you recommend for four people?'),
 'player_identity':('ให้คนไม่มีรายชื่อในรายการจองใช้แทนได้ไหม','Can someone not listed in the reservation play instead?'),
 'checkin_documents':('เช็กอินต้องแสดงบัตรอะไร','Which ID card may I show at check-in?'),
 'change_machine':('จองผิดอุปกรณ์ ต้องทำไง','I reserved the wrong device. What should I do?'),
 'change_time':('อยากเปลี่ยนเวลาที่จองทำยังไง','Can I change my reservation time?'),
 'personal_keyboard_mouse':('นำเมาส์ส่วนตัวไปใช้ได้หรือเปล่า','Is my personal keyboard allowed for normal use?'),
 'wrong_slip':('อัปโหลดสลิปผิด ต้องส่งใหม่ที่ไหน','How do I replace an incorrect payment slip?'),
 'combined_transfer':('โอนรวมครั้งเดียวสำหรับหลายรายการจองได้ไหม','Is a single bank transfer allowed for several bookings?'),
 'group_checkin':('เช็คอินแทนเพื่อนทั้งกลุ่มได้ไหม','Can I check in for everyone in our group?'),
 'rest_seating':('มีที่ให้นั่งพักบ้างไหม','Is there a place to rest?'),
}
BOUNDARIES=[
 ('waiting','ไปถึงก่อนเวลาจองต้องรอตรงไหน?','Where should I wait before my booked slot?', ['rest_seating'],['designated_waiting_point']),
 ('parking-fee','ที่จอดรถฟรีไหม','Is parking free?', ['parking'],['parking_fee']),
 ('walk-immediate','walk in เล่นได้ทันทีไหม','Can I walk in and play immediately?', ['walk_in'],['immediate_walk_in_slot']),
 ('paid-date','จองผิดวัน แต่จ่ายแล้ว แก้ได้ไหม?','I booked the wrong date and already paid. Can I change the date?', [],['date_change_exception_and_channel']),
 ('refund-date','ขอเลื่อนเป็นวันอื่นแทนคืนเงินได้ไหม?','Can I reschedule to another day instead of a refund?', [],['date_change_exception_and_channel']),
 ('rotation','มา4คนสามารถเล่นเครื่อง2คนได้ไหมแล้วสลับกัน','Can four people take turns on a two-person service?', [],['capacity_rotation']),
 ('weather','ฝนตกหนักเดินทางไม่ได้ ขอเปลี่ยนรอบได้ไหม?','Can I change my time because rain prevents travel?', [],['weather_reschedule']),
 ('update-device','เกมกำลังอัปเดต เปลี่ยนไปใช้เครื่องอื่นได้ไหม?','Can I change machines while a game is updating?', [],['active_session_machine_change']),
 ('payer','จ่ายจากบัญชีของเพื่อนได้หรือเปล่า?','Can I pay from my friend\'s bank account?', [],['payer_identity']),
 ('id-name','ต้องใช้ชื่อจริงตรงกับบัตรไหม?','Does my real name need to match the ID card?', [],['name_matches_id']),
 ('friends-games','มีเกมไหนเล่นกับเพื่อนได้บ้าง?','Which games can I play with friends?', [],['multiplayer_game_modes']),
 ('two-people','มากันสองคน มีอะไรเล่นด้วยกันได้?','There are two of us. What can we play together?', [],['two_person_recommendation']),
 ('request-game','ถ้าอยากเล่นเกมที่ไม่มีในรายการ ขอให้ลงเพิ่มได้ไหม?','Can I request that you add a game that is not in the catalog?', [],['game_installation_permission']),
 ('late','ไปสายสิบห้านาทียังเล่นได้หรือเปล่า?','Can I still play if I arrive fifteen minutes late?', [],['late_grace_exception']),
 ('extend','เล่นอยู่แล้วอยากต่อเวลา ทำยังไง?','How can I extend my playing time?', [],['session_extension']),
 ('cross-zone','อยากเปลี่ยนจาก PC ไปเล่น PS5 ต้องจองใหม่ไหม?','If I change from PC to PS5, do I need a new booking?', [],['cross_zone_change']),
 ('steam','ต้องใช้บัญชี Steam ของตัวเองไหม?','Do I need to use my own Steam account?', [],['game_account_policy']),
 ('crash','เครื่องค้างหรือดับระหว่างเล่น เวลาที่เสียไปคิดยังไง?','How is lost time compensated if a machine crashes while playing?', [],['technical_fault_compensation']),
 ('logout','ลืมออกจากบัญชีหลังเล่น ต้องติดต่อใคร?','Who do I contact if I forgot to log out of my account?', ['contact'],['forgotten_logout_procedure']),
 ('photo','ถ่ายรูปหรืออัดวิดีโอได้ไหม?','Can I take photos or record video?', [],['photo_video_permission']),
 ('stream','สตรีมเกมจากเครื่องของศูนย์ได้ไหม?','Can I stream games from the studio PC?', [],['streaming_permission']),
 ('install','ติดตั้งเกม โปรแกรม หรือ mod เองได้ไหม?','Can I install games, programs, or mods myself?', [],['game_installation_permission']),
 ('minor','เด็กเข้าใช้บริการได้ไหม ต้องมีผู้ปกครองหรือเปล่า?','Can children use the studio, and do they need a guardian?', [],['minor_guardian_policy']),
 ('seats','ที่นั่งที่ระบุคือจำนวนคนเล่นพร้อมกันหรือจำนวนที่นั่งในห้อง?','Do the seats mean simultaneous players or seats in the room?', [],['seat_capacity_definition']),
 ('receipt','ขอใบเสนอราคาหรือใบเสร็จได้ไหม?','Can I request a quotation or receipt?', [],['quotation_receipt_procedure']),
 ('accounts','ศูนย์มีบัญชีเกมให้ยืมหรือเปล่า?','Does the studio loan game accounts?', [],['game_account_policy']),
 ('versions','เกมอัปเดตเวอร์ชันล่าสุดแล้วหรือยัง?','Are the games updated to the latest version?', [],['game_version_status']),
 ('update-time','ถ้าไปถึงแล้วเกมต้องอัปเดต เวลาจะเริ่มนับเลยไหม?','Does my service time start counting while the game updates?', [],['update_time_charging']),
 ('phone','กรอกเบอร์โทรผิด ต้องจองใหม่ไหม?','I entered the wrong phone number. Do I need a new booking?', [],['booking_phone_correction']),
 ('overpay','โอนเกินจำนวนที่ต้องจ่าย ทำยังไง?','I overpaid. What should I do?', [],['overpayment_resolution']),
 ('underpay','โอนขาดไปนิดหนึ่ง ต้องโอนเพิ่มหรือจองใหม่?','I underpaid. Should I transfer the difference or book again?', [],['underpayment_resolution']),
 ('closure','ถ้าศูนย์ปิดพิเศษหลังจองแล้ว จะจัดการรายการยังไง?','How is my booking handled if the studio closes unexpectedly?', [],['special_closure_booking_resolution']),
]
def cases():
 rows=p.cases()+[dict(id=f'{lang}-variant-{key}',locale=lang,turns=[q[lang=='en']],key=key) for lang in ('th','en') for key,q in VARIANTS.items()]
 rows += [dict(id=f'{lang}-boundary-{key}',locale=lang,turns=[qen if lang=='en' else qth],expected_claims=claims,expected_missing=missing) for lang in ('th','en') for key,qth,qen,claims,missing in BOUNDARIES]
 return rows
def grade(c,rs):
 if 'key' in c:return p.grade(c,rs)
 b=rs[-1]['response'];a=b.get('answer','');trace=b.get('trace',[])
 meta=next((t.get('metadata',{}) for t in trace if t.get('stage')=='user_service_facts'),{})
 checks=dict(transport=rs[-1]['status']==200 and b.get('ok') is True,expected_claims=set(meta.get('claim_ids',[]))==set(c['expected_claims']),explicit_missing=set(meta.get('missing_fields',[]))==set(c['expected_missing']),partial_not_complete=meta.get('outcome')!= 'answered_complete',english_no_thai=not re.search('[\u0e00-\u0e7f]',a) if c['locale']=='en' else True,no_timeout=not b.get('timed_out'))
 if c['id'].endswith(('-crash','-closure')):
  checks['known_refund_exception_preserved']='rule_refund_policy' in meta.get('recorded_rule_ids',[]) and ('refund' in a.casefold() if c['locale']=='en' else 'คืนเงิน' in a) and meta.get('outcome')=='answered_partial'
 return dict(id=c['id'],passed=all(checks.values()),checks=checks,answer=a,mode=b.get('mode'),records=rs)
if __name__=='__main__':
 p.p.cases=cases;p.p.grade=grade;p.p.run(sys.argv[1],sys.argv[2])
