import json,re,sys
from pathlib import Path
import r48_probe as old
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r49_current_path.txt').read_text());old.p.OUT=OUT

SINGLES={
 'membership':['คนทั่วไปไม่สมัครสมาชิกเข้าได้ปะ','ต้องสมัครสมาชิคก่อนเข้าเล่นไหม','Do nonmembers need to sign up first?','Do I need a membrship to play?'],
 'spectators':['ไปดูเพื่อนเฉยๆไม่ได้เล่นได้มั้ย','นั่งดููเพื่อนเล่นได้ไหม','Am I allowed to watch a friend without playing?','Can I just waatch my friend play?'],
 'walk_in':['ไปหน้าร้านเลย ยังต้องจองมั้ย','walkinn ต้องจองก่อนเล่นไหม','Can I turn up without reserving?','Can I walkk in without a booking?'],
 'parking':['ขับมอไซค์ไป จอดตรงไหน','มีที่จอดรดสำหรับรถยนต์ไหม','Can I park my motorcycle there?','Is there parkinng for a car?'],
 'location':['ขอพิกัดศูนย์ อยู่ตึกไหนชั้นอะไร','ศูนย์อยู่ตึกใหน ชั้นใหน','Which floor and building should I go to?','Which buillding is the studio in?'],
 'map':['ขอ Google Maps ไปศูนย์','ขอลิงค์แผนทีไปศูนย์','Could you send me the Google Maps link?','Can I get a maap link to the studio?'],
 'checkin_documents':['เช็กอินใช้พาสปอร์ตได้ปะ','ต้องเอาบัตรอะไรไปแสดงตอนเข้าศูนย์','Is a passport acceptable at check-in?','What ID do I need to show on arrival?'],
 'change_machine':['เผลอเลือกเครื่องผิดตอนจองแก้ยังไง','จองผืดเครื่อง เปลี่ยนได้มั้ย','I picked the wrong console in my reservation. How do I fix it?','I booked the wrong machne. How do I fix it?'],
 'change_time':['อยากย้ายเวลาที่จองไว้ทำไง','เปลี่ยนเวลาจอองได้ปะ','Can I move my reservation to a different time?','Can I change my boking time?'],
 'personal_keyboard_mouse':['เอาเม้าส์ของผมไปเสียบได้ปะ','เอาคีย์บอดส่วนตัวมาใช้ได้มั้ย','Are visitors permitted to plug in their own mouse?','Can I bring my own keyboarrd?'],
 'wrong_slip':['ส่งรูปหลักฐานโอนผิด แก้ตรงไหน','แนบสะลิปผิดรูปทำไง','I attached the incorrect transfer receipt image. How can I replace it?','Uploaded the wrong payment sllip, how do I fix it?'],
 'combined_transfer':['จองไว้ 3 เครื่องจ่ายรวมยอดเดียวได้ไหม','จองหลายเครื่องโอนครังเดียวได้ปะ','Can I pay for three machines with a single transfer?','Can I pay multiple bookings with one transferr?'],
 'group_checkin':['เพื่อนยังมาไม่ครบ ผมเช็คอินแทนทุกคนได้ไหม','เช็กอินแทนเพื่อนทังกลุ่มได้ปะ','Can I check everyone in before my friends arrive?','Can I check-in for the whoole group?'],
 'rest_seating':['มีโซนให้นั่งรอพักไหม','มีที่นังพักไหม','Is there a waiting area where I can rest?','Is there a reest area?'],
}
MULTI=[
 ('map-parking','ขอแผนที่ศูนย์ และมีที่จอดรถไหม','Can I get a map and is there parking?', ['map','parking'],[]),
 ('member-watch','ต้องเป็นสมาชิกไหม แล้วนั่งดูเพื่อนได้ไหม','Do I need membership, and can I watch my friends?', ['membership','spectators'],[]),
 ('slip-transfer','แนบสลิปผิดรูปแก้ยังไง และจองหลายเครื่องโอนครั้งเดียวได้ไหม','How do I replace a wrong slip, and can I make one transfer for multiple machines?', ['wrong_slip','combined_transfer'],[]),
 ('mouse-controller','เอาเมาส์ตัวเองไปใช้ได้ไหม แล้วจอยตัวเองล่ะ','Can I bring my own mouse, and what about my own controller?', ['personal_keyboard_mouse'],['personal_controller_permission']),
 ('parking-children','มีที่จอดรถไหม และเด็กต้องมีผู้ปกครองไหม','Is there parking, and do children need a guardian?', ['parking'],['minor_guardian_policy']),
]
FOLLOWUPS=[
 ('parking-moto',['มีที่จอดรถไหม','แล้วมอเตอร์ไซค์ล่ะ'],['Is there parking?','What about motorcycles?'],['parking'],[]),
 ('parking-free',['มีที่จอดรถไหม','ฟรีไหม'],['Is there parking?','Is it free?'],['parking'],['parking_fee']),
 ('map-after-location',['ศูนย์อยู่ตรงไหน','ขอลิงก์หน่อย'],['Where is the studio?','Can I get the link?'],['map'],[]),
 ('passport',['ตอนมาถึงต้องแสดงหลักฐานอะไร','passport ล่ะ'],['What identification do I show on arrival?','And a passport?'],['checkin_documents'],[]),
 ('own-mouse',['เอาคีย์บอร์ดส่วนตัวมาได้ไหม','แล้วเมาส์ล่ะ'],['Can I bring my own keyboard?','What about a mouse?'],['personal_keyboard_mouse'],[]),
 ('own-controller',['เอาคีย์บอร์ดส่วนตัวมาได้ไหม','แล้วจอยล่ะ'],['Can I bring my own keyboard?','What about a controller?'],[],['personal_controller_permission']),
 ('transfer-note',['จองหลายเครื่องโอนครั้งเดียวได้ไหม','ต้องเขียนอะไรใน note'],['Can I make one transfer for multiple machines?','What should I write in the note?'],['combined_transfer'],['combined_transfer_note_format']),
 ('slip-contact',['แนบสลิปผิดรูปแก้ยังไง','ส่งที่ไหน'],['How do I fix a wrong slip image?','Where should I send it?'],['wrong_slip'],[]),
 ('waiting-point',['มีที่นั่งพักไหม','ถ้าไปก่อนเวลาจองรอที่นั่นได้ไหม'],['Is there a rest area?','Can I wait there before my booking?'],['rest_seating'],['designated_waiting_point']),
 ('time-shift-date',['เปลี่ยนเวลาจองได้ไหม','แล้วเปลี่ยนวันล่ะ'],['Can I change my booking time?','What about changing the date?'],[],['date_change_exception_and_channel']),
]
SCOPES=[
 ('steam-member','Steam ต้องเป็นสมาชิกก่อนไหม','Does Steam require membership?',[],'not_user_facts'),
 ('team-member','สมาชิกทีม VALORANT ต้องมีกี่คน','How many members are in a VALORANT tournament team?',[],'not_user_facts'),
 ('fire-mouse','ปุ่มยิง CS2 ใช้เมาส์ปุ่มไหน','Which mouse button fires in CS2?',[],'not_user_facts'),
 ('tournament-mouse','กฎการแข่งขัน VALORANT ใช้เมาส์ส่วนตัวได้ไหม','Can I use my own mouse in the VALORANT tournament?',[],'not_user_facts'),
 ('dl-games','โหลดเกมเองลง PC ได้ไหม','Can I download and install a game myself on the PC?', ['game_installation_permission'],'missing'),
 ('other-payer','จ่ายเงินให้หลายเครื่องด้วยบัญชีเพื่อนได้ไหม','Can my friend pay for multiple machines using their account?', ['payer_identity'],'missing'),
 ('parking-photo','ถ่ายรูปที่จอดรถได้ไหม','Can I take photos in the parking area?', ['photo_video_permission'],'missing'),
 ('arrival-no-id','ไม่มีบัตรประชาชนใช้ passport แทนได้ไหม','I have no national ID. Can I use a passport instead?',[],'documents'),
]
def cases():
 rows=[]
 for key,qs in SINGLES.items():
  for i,q in enumerate(qs):rows.append(dict(id=f'{"th" if i<2 else "en"}-new-{key}-{i%2}',locale='th' if i<2 else 'en',turns=[q],key=key,family='paraphrase' if i%2==0 else 'typo'))
 for lang in ('th','en'):
  for key,th,en,claims,missing in MULTI:rows.append(dict(id=f'{lang}-multi-{key}',locale=lang,turns=[en if lang=='en' else th],claims=claims,missing=missing,family='compound'))
  for key,th,en,claims,missing in FOLLOWUPS:rows.append(dict(id=f'{lang}-follow-{key}',locale=lang,turns=en if lang=='en' else th,claims=claims,missing=missing,family='followup'))
  for key,th,en,fields,kind in SCOPES:rows.append(dict(id=f'{lang}-scope-{key}',locale=lang,turns=[en if lang=='en' else th],missing=fields,scope_kind=kind,family='scope'))
  initial='Is there parking and can I watch my friends?' if lang=='en' else 'มีที่จอดรถไหม และนั่งดูเพื่อนได้ไหม'
  free='Is it free?' if lang=='en' else 'ฟรีไหม'
  rows.append(dict(id=f'{lang}-ambiguity-free',locale=lang,turns=[initial,free],family='ambiguity',scope_kind='clarification'))
  rows.append(dict(id=f'{lang}-select-parking-fee',locale=lang,turns=[initial,free,'parking' if lang=='en' else 'ที่จอดรถ'],family='followup',claims=['parking'],missing=['parking_fee']))
  rows.append(dict(id=f'{lang}-watch-free',locale=lang,turns=['Can I watch my friends?' if lang=='en' else 'นั่งดูเพื่อนได้ไหม',free],family='followup',claims=['spectators'],missing=['spectator_fee']))
  rows.append(dict(id=f'{lang}-topic-reset',locale=lang,turns=['Is there parking?' if lang=='en' else 'มีที่จอดรถไหม','What games are available in PC?' if lang=='en' else 'PC มีเกมอะไรบ้าง','What about motorcycles?' if lang=='en' else 'แล้วมอเตอร์ไซค์ล่ะ'],family='scope',scope_kind='not_user_facts'))
 return rows
def fact_meta(b):
 return [t.get('metadata',{}) for t in b.get('trace',[]) if t.get('stage','').endswith('user_service_facts')]
def grade(c,rs):
 b=rs[-1]['response'];a=b.get('answer','');trace=fact_meta(b)
 claims={k for m in trace for k in m.get('claim_ids',[])};missing={k for m in trace for k in m.get('missing_fields',[])}
 checks=dict(transport=all(x['status']==200 and x['response'].get('ok') is True for x in rs),no_timeout=not any(x['response'].get('timed_out') for x in rs),english_no_thai=not re.search('[\u0e00-\u0e7f]',a) if c['locale']=='en' else True)
 expected=[c['key']] if 'key' in c else c.get('claims',[])
 required=[chunk for key in expected for chunk in old.CONTENT[key][c['locale']=='en']]
 checks['required_content']=all(x.casefold() in a.casefold() for x in required)
 if expected:checks['claims_traced']=set(expected)<=claims
 if c.get('missing'):checks['missing_fields']=set(c['missing'])<=missing
 if c.get('scope_kind')=='not_user_facts':checks['separate_scope']=not trace
 if c.get('scope_kind')=='clarification':checks['explicit_clarification']=b.get('route_category')=='clarification' and not trace
 if c.get('scope_kind')=='documents':checks['document_options']=all(x.casefold() in a.casefold() for x in old.CONTENT['checkin_documents'][c['locale']=='en'])
 if c['family']=='followup':checks['context_used']=bool((b.get('context_resolution') or {}).get('used_context')) or c['id'].endswith('time-shift-date')
 return dict(id=c['id'],passed=all(checks.values()),checks=checks,answer=a,mode=b.get('mode'),claims=sorted(claims),missing=sorted(missing),family=c['family'],records=rs)
if __name__=='__main__':old.p.cases=cases;old.p.grade=grade;old.p.run(sys.argv[1],sys.argv[2])
