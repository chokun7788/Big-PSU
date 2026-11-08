"""Twenty synthetic scenario sets. Only the new isolated database is writable."""
import os,sys,json,copy,hashlib,sqlite3,time,collections,csv,traceback,multiprocessing,unicodedata
from pathlib import Path
from datetime import datetime
B=Path(__file__).resolve().parent
OLD=B.parent/'r58_examples_240_20261012'
SYSTEM=B.parent/'r58_common_content_20261010/system/PSU_Esports_Chatbot_Local'
sys.path.insert(0,str(OLD))
import build_and_test as prior
from app.knowledge.common.registry import template,CATALOG,source_errors,canonical_json,schema_errors
from app.knowledge.common.store import CommonStore
from app.knowledge.common.answer import CommonAnswerer,title
from run_content_fast import OneReleaseStore
DB=B/'DEMO_720_ONLY.sqlite'
AT=datetime.fromisoformat('2026-10-12T15:00:00+07:00')
WARNING='ข้อมูลสมมุติแยกสำหรับทดสอบเท่านั้น ไม่ใช่บริการ ราคา กฎ หรือข้อมูลจริงของ PSU / SYNTHETIC DEMO ONLY — NOT PRODUCTION'
ACTOR='DEMO_AUTO_NOT_REAL_OWNER'
ORDER=prior.ORDER
def L(th,en):return {'th':th,'en':en}
def rid(k,i):return f'demo20_{k}_{i:02}'
def url(p):return 'https://example.invalid/demo20/'+p
def filejson(p,x):
    p=B/p;p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('x',encoding='utf-8') as f:json.dump(x,f,ensure_ascii=False,indent=2)
def digestdb(p):
    c=sqlite3.connect('file:'+p.as_posix()+'?mode=ro',uri=True)
    try:return hashlib.sha256('\n'.join(c.iterdump()).encode()).hexdigest()
    finally:c.close()
# All games and venues below are fictional; no current product/game claims.
# label TH/EN, game TH/EN, mechanics TH/EN, platform, min/max, session/occupancy,
# price minor, policy topic TH/EN, policy decision. Capacities are authored fixtures.
SCENARIOS=[
('ดาวเหนือ','Northstar','สวนเมฆ','Cloud Garden','ปลูกต้นไม้ร่วมกันและแบ่งหน้าที่เก็บเมล็ด','Plant together and split seed collecting tasks','Nintendo Switch',1,4,60,60,4500,'ดูเพื่อนเล่น','Watching friends','allowed'),
('ดาวเหนือ พลัส','Northstar Plus','วงโคจรคู่','Orbit Duo','ผู้เล่นสองคนประสานปุ่มเพื่อพายานผ่านวงแหวน','Two players coordinate buttons to fly through rings','PS5',2,2,90,90,12000,'เปลี่ยนผู้เล่น','Player substitution','prohibited'),
('ละอองฝน','Drizzle','ประภาคารเสมือน','Virtual Beacon','ใช้มือเสมือนจัดแสงนำทางเรือ','Use motion inputs to arrange lights guiding ships','VR',1,1,30,60,7500,'พักเมื่อเวียนหัว','Motion discomfort breaks','required'),
('สายหมอก','Mist','ทางโค้งสีเงิน','Silver Curve','ฝึกเบรกและเข้าโค้งด้วยพวงมาลัย','Practise braking and cornering with a wheel','Cockpit',1,1,45,60,9500,'ปรับเบาะ','Seat adjustment','conditional'),
('บัวสีคราม','Indigo Lotus','ก้อนบล็อกสี','Colour Blocks','จัดบล็อกตามตัวอย่างโดยไม่มีการแข่งขัน','Arrange blocks to match examples without competing','PC',1,1,60,60,0,'กิจกรรมเรียนรู้ฟรี','Free learning activity','allowed'),
('ปะการัง','Coral','สะพานเพื่อน','Friend Bridge','ร่วมกันวางสะพานให้ตัวละครข้ามแม่น้ำ','Place bridges together to cross a river','Nintendo Switch',2,4,120,120,18000,'อาหารในโซน','Food in the zone','prohibited'),
('ตะวันอ่อน','Gentle Sun','ทีมดาวตก','Meteor Team','ทีมสองฝั่งแข่งขันเก็บจุดพลังงาน','Two teams compete to collect energy points','PC',5,10,120,120,50000,'จำนวนสมาชิกทีม','Team roster','required'),
('ฟ้าหลังฝน','After Rain','ผู้ส่งจดหมาย','Letter Runner','ส่งจดหมายให้ครบโดยเลือกเส้นทางสั้น','Deliver letters by selecting short routes','PS5',1,2,30,30,3500,'บัญชีผู้เล่น','Player accounts','conditional'),
('ลมทะเล','Sea Breeze','ท่าเรือดิจิทัล','Digital Harbour','จัดคิวเรือโดยเล่นเป็นกลุ่มใหญ่','Arrange vessel queues as a large group','PC',3,12,180,180,90000,'การจองหมู่คณะ','Group reservations','required'),
('ห้องสมุดดาว','Star Library','บทเพลงลูกบาศก์','Cube Melody','กดปุ่มตามสีและจังหวะเพื่อสร้างเพลง','Press to match colours and rhythms and create music','PS5',1,4,60,60,6000,'ปรับระดับเสียง','Volume adjustment','conditional'),
('ต้นเฟิร์น','Fern','เขาวงกตเงา','Shadow Maze','หาทางออกโดยบอกเส้นทางให้เพื่อนฟัง','Find an exit by describing paths to teammates','PC',2,3,90,90,10000,'อุปกรณ์ส่วนตัว','Personal devices','allowed'),
('ทองทราย','Sand Gold','ห้องทดลองลอยฟ้า','Sky Laboratory','หยิบวัตถุเสมือนประกอบเครื่องจักร','Assemble virtual machines using motion inputs','VR',1,1,20,60,5000,'พื้นที่ปลอดภัย','Safety boundary','required'),
('จันทร์เสี้ยว','Crescent','ขบวนรถจิ๋ว','Tiny Convoy','ควบคุมรถหลายคันให้วิ่งถึงปลายทาง','Steer a convoy to its destination','Cockpit',1,1,60,60,11000,'ฝึกก่อนเริ่ม','Practice before starting','allowed'),
('แสงอรุณ','Dawn Light','ครัวสายรุ้ง','Rainbow Kitchen','แบ่งหน้าที่ทำอาหารสมมุติให้ทันเวลา','Split tasks to prepare fictional meals on time','Nintendo Switch',1,4,45,60,5500,'ถ่ายภาพ','Photography','conditional'),
('กิ่งไผ่','Bamboo','กล่องปริศนา','Puzzle Box','ผลัดกันแก้ปริศนาและบันทึกรหัส','Take turns solving puzzles and recording codes','PC',1,2,75,75,8000,'ติดตั้งโปรแกรม','Software installation','prohibited'),
('เมฆขาว','White Cloud','บันไดเสียง','Sound Ladder','ฟังสัญญาณเสียงและเลือกตำแหน่งบนบันได','Listen to audio cues and select ladder positions','PC',1,1,60,60,4000,'การช่วยเข้าถึง','Accessibility assistance','allowed'),
('มะลิ','Jasmine','เมืองกระดาษ','Paper Town','ต่อชิ้นส่วนเมืองแล้วแลกเปลี่ยนทรัพยากร','Build a town and trade resources','PS5',1,4,120,120,22000,'เลื่อนวัน','Changing dates','conditional'),
('กระเบน','Ray','ดาวเทียมหลงทาง','Lost Satellite','เลือกคำสั่งนำดาวเทียมกลับสถานี','Choose commands to guide a satellite back','PC',1,1,60,60,3000,'คืนเงิน','Refund requests','prohibited'),
('แปะก๊วย','Ginkgo','ลานนักสำรวจ','Explorer Yard','รวมกลุ่มเก็บเบาะแสและสรุปเส้นทาง','Collect clues as a group and agree on a route','Nintendo Switch',2,6,180,180,30000,'หลักฐานเช็กอิน','Check-in proof','required'),
('รุ่งเรือง','Radiance','เวทีฝึกฝน','Practice Arena','จับคู่ผู้เล่นฝึกกลยุทธ์โดยไม่จัดอันดับ','Pair players for unranked strategy practice','PC',2,8,240,240,72000,'การประท้วงผล','Result appeals','conditional')]
NAMES={
 'center':('ศูนย์ทดลอง','Demo venue'),'zone':('โซนทดลอง','Demo zone'),'equipment_model':('รุ่นอุปกรณ์','Demo model'),'resource':('เครื่องทดลอง','Demo station'),'service':('รอบทดลอง','Demo session'),'game':('เกมสมมุติ','Fictional game'),'audience':('กลุ่มผู้ใช้','Demo visitors'),'contact':('ช่องทางช่วยเหลือ','Demo help channel'),'procedure':('ขั้นตอนทดลอง','Demo procedure'),'policy':('ข้อกำหนดทดลอง','Demo policy'),'facility':('พื้นที่พัก','Demo amenity'),'game_service':('การติดตั้งทดลอง','Demo installation'),'game_mode':('โหมดทดลอง','Demo mode'),'control_set':('ชุดควบคุมทดลอง','Demo controls'),'rate':('อัตราทดลอง','Demo tariff'),'rental_package':('แพ็กเกจทดลอง','Demo package'),'schedule':('ตารางทดลอง','Demo timetable'),'closure':('ประกาศวันทดลอง','Demo date notice'),'competition':('รายการฝึก','Demo event'),'competition_rule':('ข้อการแข่งขันทดลอง','Demo rule'),'news':('ข่าวทดลอง','Demo bulletin'),'person':('ผู้ดูแลสมมุติ','Fictional host'),'faq':('คำถามตัวอย่าง','Demo enquiry'),'live_binding':('ตัวเชื่อมทดลอง','Demo binding')}
FAC=[('มุมดูเพื่อน','Spectator corner'),('จุดพักสายตา','Eye-rest corner'),('เก้าอี้พัก VR','VR rest chair'),('จุดปรับเบาะ','Seat adjustment point'),('โต๊ะเรียนรู้','Learning table'),('จุดฝากอาหาร','Food storage point'),('โต๊ะรวมทีม','Team table'),('เคาน์เตอร์บัญชี','Account help counter'),('พื้นที่รวมกลุ่ม','Group meeting area'),('จุดยืมหูฟัง','Headphone collection'),('ชั้นวางอุปกรณ์','Device shelf'),('จุดสวมอุปกรณ์','Headset fitting point'),('ป้ายฝึกขับ','Driving practice board'),('ฉากถ่ายภาพ','Photo backdrop'),('เคาน์เตอร์เทคนิค','Technical counter'),('ทางเข้าไร้ขั้น','Step-free entry'),('มุมรอรอบใหม่','Rescheduling waiting area'),('จุดสอบถามเงิน','Payment help point'),('โต๊ะตรวจเอกสาร','Document desk'),('โต๊ะกรรมการ','Official desk')]
def record(k,i):
    th,en,gth,gen,mth,men,p,mn,mx,dur,occ,price,tth,ten,decision=SCENARIOS[i-1]
    r=template(k);r['record_id']=rid(k,i);r['validity']={'state':'known','effective_from':'2026-01-01T00:00:00+07:00','effective_until':'2028-01-01T00:00:00+07:00'}
    r['localization']={'source_language':'mixed','en_status':'agent_translated','source_revision_hash':None}
    label=L(NAMES[k][0]+' '+th,NAMES[k][1]+' '+en)
    r['aliases']={'th':[label['th']],'en':[label['en']]}
    contact=['onsite','email','facebook','website','phone'][i%5]
    contactval={'onsite':f'DEMO desk {en}','email':f'fiction{i:02}@example.invalid','facebook':url(f'social/{i}'),'website':url(f'contact/{i}'),'phone':f'DEMO-NON-DIALABLE-{i:02}'}[contact]
    start=['08:00','09:00','10:00','11:00'][i%4];end=['17:00','18:00','19:00','20:00'][i%4]
    breaks=[] if i%4==0 else [{'start':'12:00','end':'13:00'}]
    books=[{'start':start,'end':end}] if not breaks else [{'start':start,'end':'12:00'},{'start':'13:00','end':end}]
    closure=['closed','modified_hours','open_override'][i%3]
    proof=[] if i%4==0 else [f'DEMO pass {en}']+( [f'DEMO group list {i}'] if mx>4 else [])
    steps=[{'order':1,'instruction':L('เลือกบริการสมมุติ '+th,'Select the fictional '+en+' service'),'contact_id':None},{'order':2,'instruction':L('ตรวจชื่อและเงื่อนไขก่อนยืนยัน','Check names and conditions before confirming'),'contact_id':rid('contact',i)}]
    if i%3==0:steps.append({'order':3,'instruction':L('แจ้งผู้ดูแลเพื่อขอความช่วยเหลือเฉพาะรอบทดลอง','Ask the demo operator for session-specific help'),'contact_id':rid('contact',i)})
    policydetail=L(f'กติกาสมมุติเรื่อง{tth}: {decision}; ถ้าเงื่อนไขไม่ครบให้ติดต่อผู้ดูแล ไม่ใช่กฎของ PSU',f'Fictional rule for {ten}: {decision}; contact the demo operator if requirements are not met. Not PSU policy.')
    conditions=[] if decision=='allowed' else [{'field':'demo_session','operator':'eq','value':True}]
    offered=i not in (8,18);dev={'PC':'pc','PS5':'console','Nintendo Switch':'console','VR':'vr','Cockpit':'wheel'}[p]
    inputdev={'PC':'keyboard_mouse','PS5':'gamepad','Nintendo Switch':'gamepad','VR':'vr_motion','Cockpit':'racing_wheel'}[p]
    vals={
 'center':{'name':label,'operator':L('ผู้ประกอบการสมมุติ '+th,'Fictional '+en+' operator'),'description':L(f'สถานการณ์ทดลอง {i}: {gth} ไม่ใช่สถานที่จริง',f'Synthetic scenario {i}: {gen}, not a real venue'),'address':L(f'เลขที่สมมุติ {i*7} ถนนตัวอย่าง แขวงทดลอง','Fictional address '+str(i*7)+', Example Road, Test District'),'building':f'DEMO Tower {chr(65+i%5)}','floor':str(i%5+1),'map_url':url(f'map/{i}'),'timezone':'Asia/Bangkok'},
 'zone':{'name':label,'description':L(f'โซนจำลอง {p} สำหรับ{gth}',f'Synthetic {p} zone for {gen}'),'location':L(f'อาคารทดสอบ ชั้น {i%5+1} ห้อง {100+i}',f'Test building, floor {i%5+1}, room {100+i}'),'room_seats':mx+2+i%3},
 'equipment_model':{'name':label,'device_type':dev,'specifications':[{'key':'DEMO screen','value':str(24+i%5*3),'unit':'inch'},{'key':'DEMO input','value':inputdev,'unit':''}],'usage':L(f'เครื่องสมมุติใช้กับ {p}; ห้ามอ้างเป็นสเปกศูนย์',f'Fictional equipment for {p}; not a PSU specification')},
 'resource':{'name':label,'zone_id':rid('zone',i),'equipment_model_ids':[rid('equipment_model',i)],'capacity_persons':mx,'physical_pool_key':f'demo20_pool_{i:02}','operational_status':['in_service','out_of_service','retired'][0 if i%5 else (1 if i%10 else 2)]},
 'service':{'name':label,'resource_ids':[rid('resource',i)],'platform':p,'session_minutes':dur,'occupancy_minutes':occ,'capacity_min':mn,'capacity_max':mx,'booking_product_key':f'DEMO20_BOOKING_{i:02}'},
 'game':{'title':L('เกมสมมุติ '+gth,'Fictional '+gen),'edition':f'DEMO fiction revision {i}','genre':L(['ร่วมมือ','ปริศนา','จำลอง','จังหวะ','กลยุทธ์'][i%5],['Cooperative','Puzzle','Simulation','Rhythm','Strategy'][i%5]),'summary':L('เกมแต่งขึ้นเพื่อทดสอบ: '+mth,'Fictional test game: '+men),'how_to_play':L(mth+'; ใช้คำสั่งตามชุดควบคุมทดลอง',men+'; follow the demonstration controls'),'supported_platforms':[p]+(['PC'] if p!='PC' and i%4==0 else []),'publisher_url':url(f'fictional-game/{i}'),'age_rating':L('เรตอายุสมมุติ DEMO '+str(3+i%4*3),'Synthetic DEMO rating '+str(3+i%4*3))},
 'audience':{'name':label,'eligibility':L(f'ผู้ใช้สมมุติกลุ่ม {i}: '+('เข้าร่วมกิจกรรมฟรี' if price==0 else 'ใช้บริการตามรอบทดลอง'),f'Fictional group {i}: '+('free learning activity' if price==0 else 'demo sessions only')),'required_proofs':proof},
 'contact':{'channel':contact,'value':contactval,'purpose':L('สอบถามสมมุติเรื่อง '+tth,'Fictional support for '+ten),'office_hours':L('ช่วงทดลอง '+start+'–'+end,'Demo hours '+start+'–'+end)},
 'procedure':{'topic':'DEMO '+ten,'preconditions':conditions,'steps':steps,'required_documents':proof,'deadline_minutes':[0,10,15,30,60][i%5],'outcome':L('ผลทดสอบ: ตรวจสอบ '+tth+' เสร็จ','Demo outcome: '+ten+' checked')},
 'policy':{'topic':'DEMO '+ten,'subject':label,'decision':decision,'conditions_all':conditions,'exceptions':L('ข้อยกเว้นสมมุติ: ต้องได้รับอนุญาตจากผู้ดูแลกิจกรรมเฉพาะครั้ง','Synthetic exception: permission from the demo event operator is required'),'consequence':L('ให้หยุดขั้นตอนและสอบถามผู้ดูแลสมมุติ','Pause and ask the fictional operator'),'details':policydetail,'procedure_id':rid('procedure',i)},
 'facility':{'name':label,'location':L(FAC[i-1][0]+f' อยู่ห้องทดสอบ {100+i}',FAC[i-1][1]+f' in demo room {100+i}'),'usage_conditions':L('ใช้ตามรอบทดลอง; '+('ต้องขอผู้ดูแลก่อน' if i%2 else 'ใช้ได้ระหว่างรอ'), 'Demo sessions only; '+('ask the operator first' if i%2 else 'may use while waiting')),'accessibility':L('ข้อมูลสมมุติ: '+('เข้าถึงได้ไม่มีขั้น' if i%2 else 'ต้องมีผู้ดูแลช่วย'), 'Synthetic accessibility: '+('step-free route' if i%2 else 'operator assistance needed'))},
 'game_service':{'game_id':rid('game',i),'service_id':rid('service',i),'offered':offered,'installed_resource_ids':[rid('resource',i)] if offered else [],'game_version':f'DEMO BUILD {i}','account_policy_id':rid('policy',i)},
 'game_mode':{'game_id':rid('game',i),'mode_name':label,'platform':p,'players_min':mn,'players_max':mx,'network_requirement':L('เครือข่ายจำลอง: '+('ออนไลน์' if i%2 else 'เล่นออฟไลน์'), 'Synthetic network: '+('online' if i%2 else 'offline')),'studio_supported':offered},
 'control_set':{'game_id':rid('game',i),'platform':p,'input_device':inputdev,'preset':f'DEMO_LAYOUT_{i}','game_version':f'DEMO BUILD {i}','bindings':[{'buttons':[f'DEMO_{inputdev}_{n}'],'gesture':'press','action':L(['ยืนยัน','เคลื่อนที่','ย้อนกลับ'][n-1],['Confirm','Move','Back'][n-1]),'context':L('คำสั่งสมมุติของ '+gth,'Fictional input for '+gen)} for n in range(1,2+i%3)],'limitations':L('ชุดควบคุมเกมแต่งขึ้น ใช้ทดสอบเท่านั้น','Controls for a fictional game; testing only')},
 'rate':{'service_id':rid('service',i),'audience_id':rid('audience',i),'amount_minor':price,'currency':'THB','unit':['per_session','per_hour','per_person','per_group'][i%4],'duration_minutes':dur,'persons_min':mn,'persons_max':mx,'calculation_rule':'fixed' if price==0 else 'no_extrapolation','tax_note':L('ราคาสมมุติ ไม่ใช้เรียกเก็บเงินจริง','Synthetic price; never collect actual payment')},
 'rental_package':{'name':label,'zone_ids':[rid('zone',i)],'audience_id':rid('audience',i),'period_label':['half_day','full_day','custom'][i%3],'duration_minutes':[180,360,240][i%3],'amount_minor':0 if price==0 else price*3+1250,'currency':'THB','equipment_included':L('เครื่องสมมุติ '+th+' พร้อมอุปกรณ์ '+p,'Fictional '+en+' station and '+p+' inputs'),'room_seats':mx+2+i%3,'terms':L(f'แพ็กเกจสมมุติไม่รวมค่าต่อเวลา; รอบละ {mn}–{mx} คน',f'Synthetic package excludes extensions; {mn}–{mx} people per session')},
 'schedule':{'timezone':'Asia/Bangkok','zone_ids':[rid('zone',i)],'weekday':i%7,'open_periods':[{'start':start,'end':end}],'bookable_periods':books,'maintenance_periods':breaks,'reason':L('ตารางสมมุติ '+th+(' มีพักบำรุงรักษา' if breaks else ' ไม่มีพักบำรุงรักษา'),'Synthetic '+en+' schedule'+(' with maintenance' if breaks else ' without maintenance'))},
 'closure':{'local_date':f'2026-12-{i:02}','zone_ids':[rid('zone',i)],'state':closure,'open_periods':[] if closure=='closed' else [{'start':'14:00','end':'18:00'}],'bookable_periods':[] if closure=='closed' else [{'start':'14:00','end':'18:00'}],'reason':L('ประกาศสมมุติ '+th+': '+closure,'Synthetic '+en+' date notice: '+closure),'resolution_policy_id':rid('policy',i)},
 'competition':{'game_id':rid('game',i),'event_name':label,'division':L('กลุ่มฝึก '+str(mn)+'–'+str(mx)+' คน','Practice group '+str(mn)+'–'+str(mx)+' players'),'rulebook_release':f'DEMO20_REV_{i}','competition_dates':[f'2026-12-{i:02}'],'coverage':'partial' if i%3==0 else 'complete'},
 'competition_rule':{'competition_id':rid('competition',i),'section_number':f'{i%5+1}.{i}','facet':['identity','eligibility_registration','roster_composition','competition_format','match_configuration','pre_match_on_site','in_match_operations','fair_play_conduct','penalty_matrix','protest_dispute'][i%10],'heading':label,'text':L(f'ข้อสมมุติ {i}: {tth} ให้ปฏิบัติตามคำตัดสิน {decision}; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง',f'Fictional clause {i}: for {ten}, follow decision {decision}; exception requires written demo operator approval; not actual rules'),'depends_on_ids':[],'completeness':'complete'},
 'news':{'title':label,'body':L(f'ข่าวสมมุติ: กิจกรรม{gth} สำหรับกลุ่ม {mn}–{mx} คน; ไม่มีรับเงินจริง',f'Synthetic bulletin: {gen} activity for {mn}–{mx} people; no actual payment'),'event_start':f'2026-12-{i:02}T10:00:00+07:00','event_end':f'2026-12-{i:02}T12:00:00+07:00','audience_ids':[rid('audience',i)],'contact_id':rid('contact',i),'registration_url':url(f'register/{i}')},
 'person':{'display_name':label,'role':L('ผู้ดูแลสมมุติเรื่อง '+tth,'Fictional host for '+ten),'team':L('ทีมทดสอบ '+th,'Demo '+en+' team'),'public_contact_id':rid('contact',i),'public_scope':L('บุคคลแต่งขึ้น ไม่มีข้อมูลส่วนตัวจริง','Fictional identity; no actual personal data')},
 'faq':{'question':label,'answer':L('คำตอบตัวอย่าง: '+policydetail['th'],'Example answer: '+policydetail['en']),'related_ids':[rid('policy',i),rid('procedure',i)],'topic':'DEMO '+ten,'scope_note':L('ใช้ได้เฉพาะสถานการณ์สมมุติ '+th,'Only applies to fictional '+en+' scenario')},
 'live_binding':{'service_id':rid('service',i),'provider':'wordpress_booking','external_resource_key':f'DEMO20_EXTERNAL_{i}','physical_pool_key':f'demo20_pool_{i:02}','status_mapping':[{'raw':'DEMO_EMPTY_'+str(i),'normalized':'free'},{'raw':'DEMO_BUSY_'+str(i),'normalized':'occupied'},{'raw':'DEMO_UNKNOWN_'+str(i),'normalized':'unknown'}],'timezone':'Asia/Bangkok','freshness_policy':L(f'ค่าจำลอง TTL {15+i*5} วินาที; ไม่เรียก API และไม่ยืนยันสถานะสด',f'Synthetic TTL {15+i*5} seconds; no API call or live status claim')}
    }[k]
    for key,v in vals.items():r['fields'][key].update(status='known',value=v,evidence_refs=[],note=WARNING)
    for key,f in r['fields'].items():
        if key not in vals:f.update(status='unknown',value=None,evidence_refs=[],note=WARNING+'; ไม่ได้กำหนดค่าในตัวอย่างนี้')
    if k=='competition':r['fields']['supersedes_id'].update(status='not_applicable',note=WARNING+'; ไม่มีฉบับก่อนหน้า')
    # Optional unknowns must remain unknown. Empty lists / zero / false stay known.
    unknown={'center':'map_url','game':'age_rating','equipment_model':'specifications','audience':'required_proofs','facility':'accessibility','game_service':'game_version','person':'public_contact_id','service':'booking_product_key'}
    if i%5==0 and k in unknown:r['fields'][unknown[k]].update(status='unknown',value=None,evidence_refs=[],note=WARNING+'; ยังไม่ได้กำหนด ไม่ใช่ไม่มี/ศูนย์')
    return r
def build():
    if DB.exists():raise RuntimeError('Preserve existing experiment database')
    baseline={'old_demo':digestdb(OLD/'DEMO_ONLY.sqlite'),'production_package':prior.production_digest()}
    src=sqlite3.connect('file:'+(OLD/'DEMO_ONLY.sqlite').as_posix()+'?mode=ro',uri=True);dst=sqlite3.connect(DB);src.backup(dst);dst.close();src.close()
    store=CommonStore(DB);snap=store.snapshot()
    if not snap['allow_demo'] or len(snap['release']['records'])!=240:raise RuntimeError('Expected unmodified DEMO 240 baseline')
    selected=[];status=collections.Counter();profiles=[]
    for i,s in enumerate(SCENARIOS,1):profiles.append({'set':i,'label_th':s[0],'label_en':s[1],'fictional_game':s[2:4],'platform':s[6],'players_min':s[7],'players_max':s[8],'session_minutes':s[9],'occupancy_minutes':s[10],'amount_minor':s[11],'fictional_policy_topic':s[12:14],'fictional_decision':s[14]})
    for k in ORDER:
        for i in range(1,21):
            r=record(k,i)
            snapshot=canonical_json({'warning':WARNING,'values':{key:f['value'] for key,f in r['fields'].items() if f['status']=='known'}})
            sid='fixture20_'+r['record_id'];source={'source_id':sid,'kind':'fixture','path':str(B/'records'/k/(r['record_id']+'.json')),'sha256':hashlib.sha256(snapshot.encode()).hexdigest(),'authority_for':[k],'observed_at':'2026-10-12T15:00:00+07:00','trust':'synthetic','public_url':None}
            store.add_source(source,snapshot,actor=ACTOR)
            for key,f in r['fields'].items():
                status[f['status']]+=1
                if f['status']=='known':f['evidence_refs']=[{'source_id':sid,'locator':'/values/'+key}]
            errors=schema_errors(r)
            if errors:raise ValueError(k+' '+str(i)+': '+str(errors))
            saved=store.save(r,actor=ACTOR,expected_version=0,change_note=WARNING)
            store.approve(saved['record_id'],saved['version'],saved['hash'],actor=ACTOR)
            selected.append(r['record_id']);filejson('records/'+k+'/'+r['record_id']+'.json',store.get(r['record_id'])['record'])
        print('new '+k+': 20',flush=True)
    release=store.publish(selected,actor=ACTOR,expected_active=snap['active'],request_key='demo-20-diverse-sets')
    final=store.snapshot()
    assert len(final['release']['records'])==720
    filejson('SCENARIOS.json',profiles)
    filejson('MANIFEST.json',{'warning':WARNING,'new_sets':20,'categories':24,'new_records':480,'retained_prior_records':240,'active_total_records':720,'new_per_kind':{k:20 for k in ORDER},'new_field_statuses':dict(status),'demo_database':str(DB),'release':release,'all_new_content':'fictional synthetic authored, no publisher or production claims','translation':'agent_translated; not human reviewed','baseline':baseline,'original_demo_unchanged':baseline['old_demo']==digestdb(OLD/'DEMO_ONLY.sqlite'),'production_package_unchanged':baseline['production_package']==prior.production_digest(),'fixture_rejected_in_production':source_errors(source,snapshot,demo=False)})
    print('IMPORT COMPLETE 480 new / 720 total',flush=True)

# Two distinct, authored customer question variants plus multi-part expectations.
# No router terms, aliases or production code are changed to force these tests.
PROMPTS={
 'center':(['address'],'อยู่ตรงไหน','Where is it located?','ไปที่ไหนถึงจะเจอที่นี่','What is the address?', ['building','floor'],'อยู่ตึกอะไร ชั้นไหน','Which building and floor is it on?'),
 'zone':(['room_seats'],'มีที่นั่งกี่ที่','How many seats are there?','รองรับคนนั่งทั้งหมดได้กี่คน','What is the seating capacity?', ['location','room_seats'],'โซนนี้อยู่ตรงไหนและมีที่นั่งกี่ที่','Where is this zone and how many seats does it have?'),
 'equipment_model':(['specifications'],'สเปกมีอะไรบ้าง','What are its specifications?','มีรายละเอียดสเปกเครื่องยังไง','Tell me the hardware specifications.', ['device_type','specifications'],'เป็นอุปกรณ์ประเภทอะไรและสเปกเป็นยังไง','What device type is it and what are its specifications?'),
 'resource':(['capacity_persons'],'เล่นพร้อมกันได้กี่คน','How many people can play at once?','เครื่องนี้ให้เล่นพร้อมกันสูงสุดกี่คน','What is the maximum number of users on this station?', ['operational_status','capacity_persons'],'เครื่องยังใช้งานได้ไหมและรองรับกี่คน','Is this station in service and how many people can use it?'),
 'service':(['session_minutes'],'หนึ่งรอบเล่นได้กี่นาที','How many minutes does one session last?','จองหนึ่งรอบได้เวลาเล่นเท่าไร','How long can I play in one session?', ['session_minutes','occupancy_minutes'],'เวลาเล่นกับเวลาที่กินช่องจองกี่นาที','What are the play duration and booking occupancy in minutes?'),
 'game':(['how_to_play'],'เล่นยังไง','How do I play it?','เกมนี้ต้องทำอะไรเพื่อเล่นให้สำเร็จ','What do I do to play this game?', ['summary','how_to_play'],'เกมเกี่ยวกับอะไรและเล่นยังไง','What is this game about and how do I play it?'),
 'audience':(['required_proofs'],'ต้องใช้หลักฐานอะไร','What proof is required?','ต้องเอาเอกสารอะไรมาแสดง','Which documents do I need to show?', ['eligibility','required_proofs'],'ใครใช้สิทธิ์กลุ่มนี้ได้และต้องแสดงหลักฐานอะไร','Who qualifies for this group and what proof is needed?'),
 'contact':(['value'],'ติดต่อทางไหน','How can I contact them?','จะติดต่อผู้ดูแลได้ยังไง','Where can I reach the operator?', ['value','office_hours'],'ติดต่อที่ไหนและติดต่อได้ช่วงไหน','What is the contact and what are the office hours?'),
 'procedure':(['steps'],'ต้องทำยังไงบ้าง','What steps should I follow?','ช่วยบอกขั้นตอนให้ทำตามหน่อย','Walk me through the procedure.', ['steps','required_documents'],'มีขั้นตอนอะไรและต้องใช้เอกสารอะไร','What are the steps and required documents?'),
 'policy':(['details'],'กฎเป็นยังไง','What are the rules?','มีเงื่อนไขต้องทำตามอะไรบ้าง','What requirements apply?', ['decision','exceptions'],'อนุญาตไหมและมีข้อยกเว้นอะไร','Is it allowed and are there exceptions?'),
 'facility':(['location'],'อยู่ตรงไหนในร้าน','Where in the venue is it?','ต้องเดินไปจุดไหน','Where should I go to find this amenity?', ['location','accessibility'],'อยู่ตรงไหนและคนที่ต้องการความช่วยเหลือเข้าใช้ยังไง','Where is it and what accessibility help is available?'),
 'game_service':(['offered'],'มีให้เล่นหรือยัง','Is this game offered?','ตอนนี้มีเกมนี้ให้เล่นในบริการนี้ไหม','Does this service offer this game?', ['offered','game_version'],'มีให้เล่นไหมและติดตั้งรุ่นไหน','Is it offered and what build is installed?'),
 'game_mode':(['players_max'],'เล่นพร้อมกันได้สูงสุดกี่คน','How many people can play together at most?','คนเล่นได้เยอะสุดเท่าไหร่','What is the maximum player count?', ['players_min','players_max'],'ต้องมีขั้นต่ำกี่คนและเล่นได้สูงสุดกี่คน','What are the minimum and maximum player counts?'),
 'control_set':(['bindings'],'ปุ่มอะไรบ้าง','What are the controls?','ต้องกดปุ่มไหนทำอะไรบ้าง','Which buttons perform which actions?', ['platform','bindings'],'ใช้กับเครื่องประเภทไหนและต้องกดปุ่มอะไร','Which platform are these controls for and what are the buttons?'),
 'rate':(['amount_minor'],'ราคาเท่าไหร่','How much does it cost?','ค่าบริการจำนวนกี่บาท','What is the fee?', ['amount_minor','duration_minutes'],'ราคาเท่าไหร่และได้กี่นาที','What is the price and how many minutes does it cover?'),
 'rental_package':(['amount_minor'],'เหมาเท่าไหร่','How much is the rental?','แพ็กเกจนี้คิดค่าบริการกี่บาท','How much does this package cost?', ['amount_minor','equipment_included'],'ราคาเหมาเท่าไหร่และรวมอุปกรณ์อะไร','What is the rental price and which equipment is included?'),
 'schedule':(['bookable_periods'],'จองช่วงไหนได้บ้าง','What are the booking hours?','มีช่วงเวลาไหนที่จองเล่นได้','Which time periods can I book?', ['open_periods','maintenance_periods'],'เปิดช่วงไหนและพักบำรุงรักษาตอนไหน','What are the opening and maintenance periods?'),
 'closure':(['state'],'วันนั้นปิดไหม','Is it closed on that date?','วันนี้ในประกาศเปิดหรือปิด','Does this date notice say open or closed?', ['state','reason'],'วันนั้นเปิดปิดยังไงและเพราะอะไร','What is the opening status on that date and why?'),
 'competition':(['rulebook_release'],'ใช้กติกาฉบับไหน','Which rulebook release applies?','รายการนี้อ้างอิงกฎเวอร์ชันอะไร','What version of the rules is used?', ['rulebook_release','competition_dates'],'ใช้กติกาฉบับไหนและแข่งวันที่เท่าไหร่','Which rulebook release and competition dates apply?'),
 'competition_rule':(['text'],'ข้อนี้กำหนดอะไร','What does this rule require?','อยากอ่านข้อความกติกาข้อนี้ให้ครบ','Please give the full text of this rule.', ['text','completeness'],'กติกาข้อนี้มีเนื้อหาอะไรและข้อมูลครบไหม','What does the rule say and is its content complete?'),
 'news':(['body'],'ประกาศว่าอะไร','What does the announcement say?','ข่าวนี้แจ้งรายละเอียดอะไร','What information is in this bulletin?', ['body','event_start','event_end'],'ประกาศอะไรและกิจกรรมเริ่มจบเมื่อไหร่','What is announced and when does the event start and end?'),
 'person':(['role'],'รับผิดชอบอะไร','What is their role?','ผู้ดูแลคนนี้ช่วยเรื่องไหน','What does this host handle?', ['role','public_contact_id'],'รับผิดชอบเรื่องอะไรและติดต่อทางไหน','What is their role and public contact?'),
 'faq':(['answer'],'คำตอบคืออะไร','What is the answer?','ช่วยตอบคำถามรายการนี้หน่อย','Please answer this enquiry.', ['answer','scope_note'],'คำตอบคืออะไรและใช้กับกรณีไหน','What is the answer and its scope?'),
 'live_binding':(['status_mapping'],'จับคู่สถานะยังไง','How are statuses mapped?','รหัสจากระบบจะแปลงเป็นสถานะแบบไหน','How are provider statuses translated?', ['status_mapping','freshness_policy'],'จับคู่สถานะแบบไหนและเก็บข้อมูลนานเท่าไหร่','What are the status mappings and freshness policy?')}
def cases(records):
    out=[]
    def add(r,lang,style,q,keys,history=None):out.append({'id':f'{len(out)+1:05}','rid':r['record_id'],'kind':r['kind'],'lang':lang,'style':style,'question':q,'expected_fields':keys,'history':history or []})
    for k in ORDER:
        for i in range(1,21):
            r=records[rid(k,i)];keys,th,en,th2,en2,mkeys,mth,men=PROMPTS[k]
            for lang in ('th','en'):
                name=r['aliases'][lang][0];question=th if lang=='th' else en
                add(r,lang,'all_fields',name+(' ขอข้อมูลทั้งหมดทุกส่วน' if lang=='th' else ' Show all information'),list(r['fields']))
                add(r,lang,'natural',name+' '+question,keys)
                add(r,lang,'paraphrase',name+' '+(th2 if lang=='th' else en2),keys)
                add(r,lang,'followup',('แล้ว' if lang=='th' else 'And ')+question,keys,[{'role':'user','content':name+(' ขอรายละเอียด' if lang=='th' else ' Tell me about it')}])
                add(r,lang,'multi_field',name+' '+(mth if lang=='th' else men),mkeys)
                if k in {'resource','game','audience','service'}:
                    pos=max(1,len(name)//2);typo=name[:pos]+name[pos]+name[pos:]
                    add(r,lang,'name_repeat',typo+' '+question,keys)
    # Existing cases control changes caused only by adding many new records.
    oldqs=json.loads((OLD/'content_final/QUESTIONS_EXPECTED.json').read_text(encoding='utf-8'))
    for old in oldqs:
        if old['rid'].endswith('_01') and old['style'] in {'all_fields','natural'}:
            r=records[old['rid']];add(r,old['lang'],'old_control_'+old['style'],old['question'],old['expected_fields'],old['history'])
    return out
def init_worker():
    global store,records,answerer
    store=OneReleaseStore(DB).freeze();records=store.frozen['release']['records'];answerer=CommonAnswerer(store)
    if not store.frozen['allow_demo']:raise RuntimeError('DEMO only')
def evaluate(c):
    started=time.perf_counter()
    try:
        ans=answerer.answer(c['question'],locale=c['lang'],history=c['history'],at=AT)
        ok,why=prior.score(ans,c,records)
        return {**c,'passed':ok,'reasons':why,'answer':ans.answer if ans else None,'mode':ans.mode if ans else None,'decision':ans.decision_artifact if ans else None,'evidence':ans.hits if ans else [],'elapsed_seconds':time.perf_counter()-started,'exception':None}
    except Exception:return {**c,'passed':False,'reasons':['exception'],'answer':None,'exception':traceback.format_exc(),'elapsed_seconds':time.perf_counter()-started}
def run_tests():
    snap=CommonStore(DB).snapshot();qs=cases(snap['release']['records']);filejson('QUESTIONS_EXPECTED.json',qs)
    filejson('EVALUATION_SCOPE.json',{'warning':WARNING,'workers':4,'immutable_validated_snapshot_reused':True,'epoch_checked_each_answer':True,'actual_common_answerer':True,'llm':False,'live_wordpress':False,'not_latency_benchmark':True,'queries':len(qs),'human_review':False,'expected_authored_independently_from_router':True})
    result=[];sums=collections.defaultdict(collections.Counter)
    with (B/'ANSWERS_AND_DECISIONS.jsonl').open('x',encoding='utf-8') as f:
        with multiprocessing.Pool(4,initializer=init_worker) as pool:
            for n,row in enumerate(pool.imap_unordered(evaluate,qs,chunksize=4),1):
                result.append(row);f.write(json.dumps(row,ensure_ascii=False)+'\n')
                for name in ['overall/all','style/'+row['style'],'kind/'+row['kind'],'language/'+row['lang']]:sums[name]['pass' if row['passed'] else 'fail']+=1
                if n%100==0:f.flush();print(f'completed {n}/{len(qs)}; pass={sums["overall/all"]["pass"]}; fail={sums["overall/all"]["fail"]}',flush=True)
    filejson('SUMMARY.json',{k:dict(v) for k,v in sums.items()});filejson('FAILURES.json',sorted([r for r in result if not r['passed']],key=lambda r:r['id']))
    assert CommonStore(DB).still_current(snap)
    print('TEST COMPLETE '+json.dumps(dict(sums['overall/all'])),flush=True)
if __name__=='__main__':
    multiprocessing.freeze_support()
    if sys.argv[1]=='build':build()
    elif sys.argv[1]=='test':run_tests()
    else:raise SystemExit('build or test')
