from pathlib import Path
import json, hashlib, shutil, datetime

OUT=Path(__file__).resolve().parent
PACK=OUT/'ready_package/PSU_Esports_Chatbot_Local'
CAND=OUT/'system/PSU_Esports_Chatbot_Local'
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
UI=PACK/'app/knowledge/common/ui'
RUN=OUT/('owner_help_'+datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))
RUN.mkdir()
catalog=json.loads((UI.parent/'catalog.json').read_text(encoding='utf-8'))

# These examples explain the form. They are never loaded into records or published.
rows=[
('center','ข้อมูลพื้นฐานศูนย์','ข้อมูลศูนย์และการเดินทาง','เมื่อเพิ่มชื่อศูนย์ หน่วยงานเจ้าของ ที่อยู่ หรือแผนที่','ศูนย์อยู่ที่ไหน อยู่ตึกอะไร','หนึ่งรายการต่อศูนย์ ไม่ใส่ราคาหรือสถานะจองในที่อยู่',[],{'name':'ศูนย์อีสปอร์ตตัวอย่าง','operator':'มหาวิทยาลัยตัวอย่าง','address':'อาคารตัวอย่าง ชั้น 1','building':'อาคารตัวอย่าง','floor':'1','description':'พื้นที่ฝึกทักษะเกมและอีสปอร์ต'}),
('contact','ช่องทางติดต่อ','ข้อมูลศูนย์และการเดินทาง','เมื่อเพิ่มเพจ อีเมล เบอร์โทร หรือช่องทางติดต่อที่เปิดเผยได้','หาศูนย์ไม่เจอติดต่อใคร','แยกหนึ่งรายการต่อช่องทาง พร้อมเรื่องที่ติดต่อได้',[],{'channel':'facebook','value':'https://www.facebook.com/example','purpose':'สอบถามเส้นทางและแจ้งปัญหา'}),
('facility','ที่จอดรถ / ที่นั่งพัก / สิ่งอำนวยความสะดวก','ข้อมูลศูนย์และการเดินทาง','เมื่อบอกว่ามีอะไรให้ใช้และอยู่บริเวณไหน','มีที่นั่งรอไหม ที่จอดรถอยู่ไหน','หนึ่งรายการต่อสิ่งอำนวยความสะดวก',[],{'name':'ที่นั่งพักตัวอย่าง','location':'กลางห้องตัวอย่าง','usage_conditions':'ใช้รอเพื่อนตามเงื่อนไขที่ศูนย์ยืนยัน'}),
('zone','โซน เช่น PC / PS5 / VR','อุปกรณ์และการจอง','เมื่อเพิ่มพื้นที่หรือหมวดอุปกรณ์ใหญ่','มีโซนอะไรบ้าง','โซนเป็นหมวดพื้นที่ ส่วน PC #01 ต้องอยู่หมวดเครื่องจริง',[],{'name':'โซน PC ตัวอย่าง','description':'พื้นที่เล่นเกมคอมพิวเตอร์','room_seats':10}),
('equipment_model','รุ่นอุปกรณ์และสเปก','อุปกรณ์และการจอง','เมื่อเพิ่มรุ่นคอมพิวเตอร์ จอ จอย หรือพวงมาลัย','ใช้การ์ดจออะไร จอยรุ่นไหน','หนึ่งรายการต่อรุ่น แล้วค่อยนำรุ่นไปเลือกให้เครื่องจริง',[],{'name':'คอมพิวเตอร์รุ่นตัวอย่าง','device_type':'pc','specifications':[{'key':'RAM','value':'16','unit':'GB'}]}),
('resource','เครื่องจริง เช่น PC #01','อุปกรณ์และการจอง','เมื่อเพิ่มเครื่องที่มีอยู่จริงในศูนย์','PC #01 อยู่โซนไหน เล่นได้กี่คน','พร้อมให้บริการ = เครื่องใช้ได้ทางกายภาพ ไม่ได้แปลว่ายังไม่ถูกจอง',['zone','equipment_model'],{'name':'PC #01 ตัวอย่าง','capacity_persons':1,'physical_pool_key':'pc_01','operational_status':'in_service'}),
('service','ตัวเลือกบริการบนหน้าจอง','อุปกรณ์และการจอง','เมื่อเพิ่มตัวเลือกที่ผู้ใช้กดจอง เช่น PC 1 ชั่วโมง หรือ VR 30 นาที','จอง VR 30 นาทีใช้เครื่องอะไร','หนึ่งรายการต่อรูปแบบบริการ เวลาเล่นกับเวลาที่กันเครื่องอาจต่างกัน',['resource'],{'name':'VR 30 นาที ตัวอย่าง','platform':'VR','session_minutes':30,'occupancy_minutes':60,'capacity_min':1,'capacity_max':1,'booking_product_key':'ใช้รหัสจริงจาก WordPress'}),
('game','เกม: ชื่อ / เนื้อหา / วิธีเล่นเบื้องต้น','เกมและวิธีเล่น','เมื่อเพิ่มข้อมูลว่าเกมคืออะไร เล่นแบบไหน รองรับแพลตฟอร์มอะไร','เกมนี้เกี่ยวกับอะไร เล่นยังไง','เกมรองรับ PC ไม่ได้แปลว่าศูนย์ติดตั้งไว้ ต้องเพิ่มหมวดเกมที่มีให้เล่นจริงด้วย',[],{'title':'เกมตัวอย่าง','edition':'ภาคตัวอย่าง','genre':'เกมผจญภัย','summary':'ช่วยตัวละครสำรวจเกาะและเก็บสิ่งของ','how_to_play':'เดินสำรวจ ทำภารกิจ และผ่านด่าน','supported_platforms':['PC']}),
('game_service','เกมที่มีให้เล่นจริงในศูนย์','เกมและวิธีเล่น','เมื่อยืนยันว่าเกมใดมีในบริการหรือเครื่องใดของศูนย์','ที่ศูนย์มีเกมนี้บน PC ไหม','เลือกเกมและบริการที่สร้างไว้ก่อน แยกจากข้อมูลทั่วไปของตัวเกม',['game','service','resource','policy'],{'offered':True,'game_version':'เวอร์ชันที่ตรวจจริง เช่น 1.2'}),
('game_mode','การเล่นกับเพื่อน / จำนวนผู้เล่น','เกมและวิธีเล่น','เมื่อเพิ่มโหมดเล่นคนเดียว เล่นร่วมเครื่อง หรือเล่นออนไลน์','เกมนี้เล่นสองคนได้ไหม','จำนวนผู้เล่นของเกมกับความจุเครื่องเป็นคนละค่า',['game'],{'mode_name':'เล่นร่วมเครื่องตัวอย่าง','platform':'PC','players_min':1,'players_max':2,'network_requirement':'ระบุว่าต้องใช้อินเทอร์เน็ตหรือบัญชีหรือไม่จากข้อมูลจริง','studio_supported':True}),
('control_set','ปุ่มควบคุมเกม','เกมและวิธีเล่น','เมื่อเพิ่มปุ่มของเกม แยกตามแพลตฟอร์ม อุปกรณ์ และชุดปุ่ม','เกมนี้กดอะไรเพื่อกระโดด','หนึ่งรายการต่อเกม + แพลตฟอร์ม + ชุดปุ่ม ห้ามยืมปุ่มของอีกแพลตฟอร์มมาใช้',['game'],{'platform':'PC','input_device':'keyboard_mouse','preset':'default','bindings':[{'buttons':['Space'],'gesture':'press','action':{'th':'กระโดดในเกมตัวอย่าง','en':None},'context':{'th':'ขณะควบคุมตัวละคร','en':None}}]}),
('audience','กลุ่มผู้ใช้ / กลุ่มราคา','ราคาและการเหมา','เมื่อแยกบุคคลทั่วไป นักศึกษา หรือหน่วยงานภายใน/ภายนอก','ใครได้ราคานี้ ต้องใช้หลักฐานอะไร','บุคคลทั่วไปกับหน่วยงานภายนอกอาจมีเงื่อนไขต่างกัน ห้ามรวมเอง',[],{'name':'กลุ่มผู้ใช้ตัวอย่าง','eligibility':'ผู้ที่ตรงตามนิยามที่เจ้าของยืนยัน','required_proofs':['เอกสารสิทธิ์ตามประกาศจริง']}),
('rate','ค่าบริการปกติ','ราคาและการเหมา','เมื่อเพิ่มราคาของบริการสำหรับกลุ่มผู้ใช้และช่วงจำนวนคน','บุคคลทั่วไปเล่น PC ชั่วโมงละเท่าไร','แยกราคาตามบริการและกลุ่ม ห้ามใช้ข้อความ FAQ แทนตารางราคา',['service','audience'],{'amount_minor':3500,'currency':'THB','unit':'per_hour','duration_minutes':60,'persons_min':1,'persons_max':1,'calculation_rule':'no_extrapolation'}),
('rental_package','ราคาเหมา / ครึ่งวัน / เต็มวัน','ราคาและการเหมา','เมื่อเพิ่มราคาแพ็กเกจเหมา พร้อมโซนและอุปกรณ์ที่รวม','เหมาเต็มวันได้อะไร ราคาเท่าไร','ชื่อครึ่งวันไม่ทำให้ระบบรู้ว่าเป็นกี่ชั่วโมง ต้องใช้ระยะเวลาที่เจ้าของยืนยัน',['zone','audience'],{'name':'แพ็กเกจเหมาครึ่งวันตัวอย่าง','period_label':'half_day','duration_minutes':240,'amount_minor':400000,'currency':'THB','equipment_included':'ระบุจำนวนและรายการอุปกรณ์จากเอกสารจริง','room_seats':20,'terms':'ระบุเงื่อนไขค่าเจ้าหน้าที่และสิ่งที่ไม่รวม'}),
('schedule','เวลาประจำสัปดาห์','เวลาเปิดและวันปิด','เมื่อเพิ่มเวลาเปิดพื้นที่ ช่วงที่จองได้ และช่วงบำรุงรักษา','วันจันทร์เปิดกี่โมง จองช่วงไหนได้','หนึ่งรายการต่อวันและขอบเขตโซน เวลาเปิดพื้นที่กับเวลาที่จองได้กรอกแยกกัน',['zone'],{'timezone':'Asia/Bangkok','weekday':0,'zone_ids':[],'open_periods':[{'start':'09:00','end':'17:00'}],'bookable_periods':[{'start':'09:00','end':'12:00'},{'start':'13:00','end':'17:00'}],'maintenance_periods':[{'start':'12:00','end':'13:00'}]}),
('closure','วันปิดพิเศษ / เปลี่ยนเวลาเฉพาะวัน','เวลาเปิดและวันปิด','เมื่อมีข้อยกเว้นจากเวลาประจำสัปดาห์ในวันที่แน่นอน','วันที่นี้ปิดพิเศษไหม','ระบุวันที่ ค.ศ. และเหตุผลตามประกาศ ไม่เพิ่มนโยบายคืนเงินเอง',['zone','policy'],{'local_date':'2026-12-31','zone_ids':[],'state':'closed','reason':'เหตุผลตามประกาศตัวอย่าง'}),
('policy','กฎศูนย์: อนุญาต / ห้าม / เงื่อนไข','กฎและขั้นตอนบริการ','เมื่อกำหนดว่าอะไรทำได้หรือไม่ได้ เช่น อุปกรณ์ส่วนตัวหรือการเปลี่ยนจอง','เอาเมาส์ตัวเองมาได้ไหม','หนึ่งรายการต่อประเด็น เก็บเงื่อนไขและข้อยกเว้นให้ครบ',['procedure'],{'topic':'example_personal_peripherals','subject':'อุปกรณ์ส่วนตัวในตัวอย่าง','decision':'prohibited','conditions_all':[],'details':'ข้อความตัวอย่าง: ไม่อนุญาตตามประกาศสมมุติ'}),
('procedure','ขั้นตอน: จอง / จ่าย / เช็กอิน / แก้ปัญหา','กฎและขั้นตอนบริการ','เมื่อบอกว่าลูกค้าต้องทำอะไรทีละขั้น','จองผิดเครื่องต้องทำยังไง','กฎบอกว่าทำได้ไหม ส่วนขั้นตอนบอกว่าต้องทำอย่างไร',['contact'],{'topic':'example_change_booking','preconditions':[],'steps':[{'order':1,'instruction':{'th':'ขั้นตอนแรกตามเอกสารตัวอย่าง','en':None},'contact_id':None}],'outcome':'ผลที่ยืนยันได้หลังทำครบขั้นตอน'}),
('competition','รายการแข่งขัน / ฉบับกติกา','การแข่งขัน','เมื่อเพิ่มการแข่งขัน ชื่อรายการ ปี เกม และฉบับเอกสาร','แข่งเกมอะไร ใช้กติกาฉบับไหน','เป็นข้อมูลหัวรายการ กติกาแต่ละข้อกรอกในหมวดข้อกติกา',['game','competition'],{'event_name':'รายการแข่งขันตัวอย่าง 2026','rulebook_release':'ฉบับ 1 วันที่ตามต้นทาง','coverage':'partial'}),
('competition_rule','ข้อกติกาการแข่งขัน','การแข่งขัน','เมื่อเพิ่มกติกาแต่ละข้อ เช่น คุณสมบัติ ทีม รูปแบบแข่ง หรือบทลงโทษ','ใช้ตัวสำรองได้ไหม กฎตอนแข่งมีอะไรบ้าง','หนึ่งรายการต่อข้อเดิม เชื่อมรายการแข่งขันที่ถูกเกม/ปี และเก็บเงื่อนไขท้ายข้อครบ',['competition','competition_rule'],{'section_number':'6.1.5','facet':'roster_composition','heading':'หัวข้อกติกาทีมตัวอย่าง','text':'ข้อความกติกาเต็มจากต้นทางตัวอย่าง รวมเงื่อนไขและข้อยกเว้น','completeness':'complete'}),
('news','ประกาศ / กิจกรรม / โปรโมชัน','ประกาศและข้อมูลเสริม','เมื่อเพิ่มประกาศที่มีช่วงเวลาและรายละเอียด','เดือนนี้มีกิจกรรมอะไร','ราคาโปรโมชันต้องมีค่าบริการที่อ้างอิงตรงกัน วันปิดควรกรอกหมวดวันปิดพิเศษด้วย',['audience','contact'],{'title':'กิจกรรมตัวอย่าง','body':'รายละเอียดกิจกรรมพร้อมเงื่อนไขตามประกาศ','event_start':'2026-12-01T09:00:00+07:00','event_end':'2026-12-01T17:00:00+07:00'}),
('person','ทีมงานที่เปิดเผยได้','ประกาศและข้อมูลเสริม','เมื่อเพิ่มชื่อและหน้าที่ทีมงานที่อนุญาตให้เผยแพร่','ใครดูแลเรื่องนี้','ใช้ชื่อและช่องทางงานที่เปิดเผยได้ ห้ามใส่ข้อมูลลูกค้าหรือเบอร์ส่วนตัวโดยไม่ได้รับอนุญาต',['contact'],{'display_name':'ทีมงานตัวอย่าง','role':'ผู้ประสานงาน','public_scope':'ติดต่อเฉพาะเรื่องบริการที่ระบุ'}),
('faq','คำถามทั่วไปเพิ่มเติม','ประกาศและข้อมูลเสริม','เมื่อคำตอบไม่เหมาะกับหมวดหลัก เช่น คำอธิบายประกอบบริการ','ศูนย์เป็นของมหาวิทยาลัยไหม','ใช้เสริมข้อมูล ห้ามสร้างคำตอบเรื่องราคา กฎ หรือสถานะสดที่ขัดกับหมวดหลัก',[],{'question':'คำถามเกี่ยวกับศูนย์ตัวอย่าง','answer':'คำตอบที่ศูนย์ยืนยันแล้วตามแหล่งจริง','topic':'example_center_background'}),
('live_binding','เชื่อมสถานะจอง WordPress (ผู้ดูแลระบบ)','สำหรับผู้ดูแลระบบ','เมื่อผู้ดูแลจับคู่บริการกับรหัส API และตรวจความหมายสถานะแล้ว','PC #01 ตอนนี้ว่างไหม','กรอกค่าจริงจากระบบ ไม่กรอกคำว่าว่างด้วยมือ การกรอกหมวดนี้ยังไม่เชื่อม API ใหม่ให้อัตโนมัติ',['service','resource'],{'provider':'wordpress_booking','external_resource_key':'รหัสจริงจาก API ห้ามเดา','physical_pool_key':'pc_01','status_mapping':[{'raw':'ค่าจริงที่ API ส่งกลับ','normalized':'unknown'}],'timezone':'Asia/Bangkok','freshness_policy':'นโยบายอายุข้อมูลที่ผู้ดูแลอนุมัติ'})
]
helpdata={r[0]:dict(label=r[1],group=r[2],when=r[3],question=r[4],tip=r[5],before=r[6],examples=r[7]) for r in rows}
labels={'th':'ภาษาไทย','en':'ภาษาอังกฤษ (ยังไม่มีคำแปลให้เว้นว่าง)','start':'เริ่มเวลา (ชั่วโมง:นาที)','end':'สิ้นสุดเวลา (ชั่วโมง:นาที)','key':'หัวข้อสเปก เช่น RAM','value':'ค่า','unit':'หน่วย เช่น GB (ไม่มีหน่วยให้เว้นว่าง)','buttons':'ปุ่มที่ใช้ เช่น Space','gesture':'วิธีกด','action':'สิ่งที่เกิดขึ้นเมื่อกด','context':'ใช้ในสถานการณ์ไหน','field':'เงื่อนไขเรื่องอะไร','operator':'วิธีเปรียบเทียบ','order':'ลำดับขั้นตอน','instruction':'สิ่งที่ผู้ใช้ต้องทำ','contact_id':'ช่องทางติดต่อ (เว้นว่างได้)','raw':'ค่าดิบที่ API ส่งกลับ','normalized':'ความหมายของสถานะ'}
enums=dict(facebook='เพจ Facebook',email='อีเมล',phone='เบอร์โทรศัพท์',website='เว็บไซต์',onsite='ติดต่อที่ศูนย์',pc='คอมพิวเตอร์',console='เครื่องคอนโซล',vr='เครื่อง VR',wheel='พวงมาลัย',display='จอภาพ',peripheral='อุปกรณ์ต่อพ่วง',furniture='เฟอร์นิเจอร์',in_service='เครื่องพร้อมใช้งาน (ยังไม่บอกสถานะจอง)',out_of_service='เครื่องหยุดให้บริการ',retired='เลิกใช้เครื่องนี้',keyboard_mouse='คีย์บอร์ดและเมาส์',gamepad='จอยเกม',racing_wheel='พวงมาลัย',vr_motion='อุปกรณ์ควบคุม VR',press='กดครั้งเดียว',hold='กดค้าง',release='ปล่อยปุ่ม',double_press='กดสองครั้ง',simultaneous='กดพร้อมกัน',sequence='กดตามลำดับ',move='ขยับอุปกรณ์',per_session='ต่อรอบ',per_hour='ต่อชั่วโมง',per_person='ต่อคน',per_group='ต่อกลุ่ม',fixed='ราคาตายตัวตามบริการ',linear='คูณตามเวลาได้ (ต้องมีประกาศยืนยัน)',no_extrapolation='ห้ามคำนวณต่อจากราคานี้เอง',half_day='ครึ่งวัน',full_day='เต็มวัน',custom='ช่วงเวลาที่กำหนดเอง',closed='ปิดบริการ',modified_hours='เปลี่ยนเวลาเฉพาะวัน',open_override='เปิดพิเศษ',allowed='อนุญาต',prohibited='ไม่อนุญาต',required='จำเป็นต้องทำ',conditional='อนุญาตเมื่อครบเงื่อนไข',eq='เท่ากับ',**{'in':'อยู่ในรายการ'},gte='มากกว่าหรือเท่ากับ',lte='น้อยกว่าหรือเท่ากับ',complete='ครบตามต้นทาง',partial='มีข้อมูลเพียงบางส่วน',conflicted='ข้อมูลขัดแย้ง ต้องตรวจเพิ่ม',truncated='ข้อความถูกตัด ยังไม่ครบ',free='ว่าง',occupied='ถูกจอง',unavailable='ไม่เปิดให้ใช้',unknown='ยังไม่ทราบ',wordpress_booking='ระบบจอง WordPress',**{'Asia/Bangkok':'เวลาไทย', 'THB':'บาทไทย'},identity='ข้อมูลรายการและเกม',eligibility_registration='คุณสมบัติและการสมัคร',roster_composition='รายชื่อทีมและตัวสำรอง',competition_format='รูปแบบการแข่งขัน',match_configuration='การตั้งค่าแมตช์',pre_match_on_site='ก่อนแข่งและการมาถึง',in_match_operations='ระหว่างการแข่งขัน',fair_play_conduct='มารยาทและความยุติธรรม',penalty_matrix='บทลงโทษ',protest_dispute='ประท้วงและข้อพิพาท',references_change_history='เอกสารอ้างอิงและประวัติการแก้ไข',game_specific='กฎเฉพาะเกม')

def typ(s):
    t=s.get('type','string');return next((x for x in t if x!='null'),'string') if isinstance(t,list) else t
def example(s,key,kind):
    # Examples are schema-shaped and leave nullable subfields blank where appropriate.
    t=typ(s)
    if key in helpdata[kind]['examples']:v=helpdata[kind]['examples'][key];return {'th':v,'en':None} if t=='object' and set(s.get('properties',{}))=={'th','en'} and isinstance(v,str) else v
    if s.get('enum'):return s['enum'][0]
    if s.get('format')=='date':return '2026-12-01'
    if s.get('format')=='date-time':return '2026-12-01T09:00:00+07:00'
    if t=='object':return {k:example(v,k,kind) for k,v in s.get('properties',{}).items()}
    if t=='array':return [example(s['items'],key.removesuffix('_ids'),kind)]
    if t=='integer':return max(s.get('minimum',1),1)
    if t=='boolean':return True
    if key=='en':return None
    if key.endswith('_id'):return 'example_'+key[:-3]
    if key.endswith('_url'):return 'https://example.com/info'
    if key in {'start','end'}:return '09:00' if key=='start' else '12:00'
    return 'ข้อความตัวอย่าง: '+labels.get(key,key)

fieldhelp={}
for c in catalog:
    fieldhelp[c['kind']]={}
    for f in c['fields']:
        e=example(f['value_schema'],f['key'],c['kind'])
        if f['reference_kind']:
            e=['example_'+f['reference_kind']] if typ(f['value_schema'])=='array' else 'example_'+f['reference_kind']
            if f['key']=='zone_ids' and c['kind'] in {'schedule','closure'}:e=[]
        hints=[]
        if f['publish_core']:hints.append('ต้องยืนยันช่องนี้ก่อนเผยแพร่ แต่บันทึกร่างที่ยังไม่ครบได้')
        if f['reference_kind']:hints.append('เลือกจากรายการที่สร้างไว้ ไม่ต้องพิมพ์รหัสเอง; รายการที่เชื่อมต้องเผยแพร่ก่อนรายการนี้')
        if f['key']=='amount_minor':hints.append('กรอกเป็นสตางค์: 35 บาท = 3500; 4,000 บาท = 400000; ใส่ 0 เฉพาะเมื่อยืนยันว่าฟรี')
        if f['key']=='weekday':hints.append('เลือกชื่อวัน ระบบเก็บเป็นเลข 0–6 ให้เอง')
        if f['key']=='zone_ids' and c['kind'] in {'schedule','closure'}:hints.append('เลือก “มีข้อมูลยืนยัน” และไม่เพิ่มแถว = ทุกโซนตามประกาศ; “ไม่ทราบ” = ยังไม่รู้ขอบเขต')
        if f['key'] in {'conditions_all','preconditions'}:hints.append('ไม่เพิ่มแถวได้เมื่อยืนยันว่าไม่มีเงื่อนไข; ถ้าไม่แน่ใจให้เลือก “ไม่ทราบ”')
        if typ(f['value_schema'])=='object' and set(f['value_schema'].get('properties',{}))=={'th','en'}:hints.append('ใส่ไทยก่อนก็ได้ อังกฤษยังไม่มีให้เว้นว่าง ไม่ต้องแปลเองโดยเดา')
        if typ(f['value_schema'])=='array':hints.append('กด “เพิ่มรายการ” แล้วกรอกทีละรายการ; ดูตัวอย่างด้านล่าง')
        fieldhelp[c['kind']][f['key']]={'hint':' • '.join(hints) or 'กรอกตามข้อมูลจริง ถ้าไม่มีหลักฐานให้คง “ไม่ทราบ”','example':e}

prefix='const OWNER_HELP='+json.dumps(helpdata,ensure_ascii=False)+';\nconst FIELD_HELP='+json.dumps(fieldhelp,ensure_ascii=False)+';\nconst SUB_LABELS='+json.dumps(labels,ensure_ascii=False)+';\nconst OPTION_LABELS='+json.dumps(enums,ensure_ascii=False)+';\n'
(RUN/'help_data.json').write_text(json.dumps({'categories':helpdata,'fields':fieldhelp},ensure_ascii=False,indent=2),encoding='utf-8')
backups={}
for base in (PACK,CAND,ROOT):
    for name in ('index.html','owner.js','owner.css'):
        p=base/'app/knowledge/common/ui'/name
        data=p.read_bytes();role='ready' if base==PACK else 'candidate' if base==CAND else 'source'
        b=RUN/'before'/role/name;b.parent.mkdir(parents=True,exist_ok=True);b.write_bytes(data)
        backups[str(p)]={'sha256':hashlib.sha256(data).hexdigest(),'backup':str(b)}
(RUN/'before_hashes.json').write_text(json.dumps(backups,ensure_ascii=False,indent=2),encoding='utf-8')

js=(UI/'owner.js').read_text(encoding='utf-8')
js=js.replace("let catalog={},record=null",prefix+"let catalog={},record=null",1)
js=js.replace("async function api(path,body)","function userError(s){let msg=s;for(let [a,b] of Object.entries({'Open this page using Open-Owner-Content.cmd':'กรุณาเปิดหน้านี้ผ่านไฟล์ Open-Owner-Content.cmd','Confirm that these values come from center information':'ติ๊กยืนยันแหล่งข้อมูลจริงก่อนบันทึก','Time-sensitive content requires confirmed validity':'หมวดนี้ต้องยืนยันวันเริ่มมีผลก่อนเผยแพร่','English translation needs review or explicit machine-translation status':'เลือกสถานะคำแปลอังกฤษให้ตรงกับการตรวจจริง','required before publication':'ต้องยืนยันข้อมูลช่องนี้ก่อนเผยแพร่','missing reference':'ไม่พบรายการที่เชื่อม','source needs factual review':'ต้องตรวจข้อมูลจากต้นทางก่อนเผยแพร่','Known validity requires effective_from':'เลือกวันที่เริ่มมีผลด้วย','Unknown validity cannot assert dates':'หากยังไม่ยืนยันช่วงวันที่ ให้ล้างวันที่เริ่มและสิ้นสุด','Stale English review':'ข้อความเปลี่ยนแล้ว ต้องตรวจคำแปลอังกฤษฉบับนี้ใหม่'}))msg=msg.split(a).join(b);if(record)for(let f of catalog[record.kind].fields)msg=msg.split(f.key+':').join(f.meaning_th+':');return msg;}\nasync function api(path,body)",1)
js=js.replace('message(e.message,true);','message(userError(e.message),true);')
js=js.replace('function valueEditor(schema,val,refKind=null){','function valueEditor(schema,val,refKind=null,key=""){')
js=js.replace("s.append(new Option('เลือกรายการ',''));","s.append(new Option('เลือกชื่อรายการที่สร้างไว้',''));s.setAttribute('aria-label',SUB_LABELS[key]||'เลือกรายการที่เชื่อม');")
js=js.replace("get=()=>s.value;}\r\n else if(schema.enum)","get=()=>s.value;}\r\n else if(schema.enum)") # source newline neutral
js=js.replace("root.append(s);get=()=>s.value;}\n else if(schema.enum)","root.append(s);if(s.options.length===1)root.append(node('p','ยังไม่มีรายการให้เลือก กรุณาสร้างหมวดที่เกี่ยวข้องก่อน (ดู “ต้องมีข้อมูลไหนก่อน” ด้านบน)'));get=()=>s.value;}\n else if(schema.enum)")
js=js.replace("for(let v of schema.enum)s.append(new Option(v,v));","for(let v of schema.enum)s.append(new Option(OPTION_LABELS[v]||v,v));")
js=js.replace("let l=node('label',k==='th'?'ข้อความไทย':k==='en'?'English':k);let ed=valueEditor(sub,val?.[k]);","let l=node('label',SUB_LABELS[k]||k);let ed=valueEditor(sub,val?.[k],k==='contact_id'?'contact':null,k);")
js=js.replace("node('button','+ เพิ่มแถว')","node('button','+ เพิ่มรายการ')")
js=js.replace("let ed=valueEditor(schema.items,x,refKind);","let ed=valueEditor(schema.items,x,refKind,key);")
js=js.replace("new Option('ใช่ / true','true'),new Option('ไม่ใช่ / false','false')","new Option('ใช่ / มี / รองรับ','true'),new Option('ไม่ใช่ / ไม่มี / ไม่รองรับ','false')")
js=js.replace("else if(t==='integer'){", "else if(key==='weekday'&&t==='integer'){let s=node('select');['จันทร์','อังคาร','พุธ','พฤหัสบดี','ศุกร์','เสาร์','อาทิตย์'].forEach((v,i)=>s.append(new Option(v,String(i))));s.value=String(val??0);root.append(s);get=()=>Number(s.value);}\n else if(t==='integer'){")
js=js.replace("i.rows=2;root.append(i);","i.rows=2;i.placeholder=key==='en'?'ยังไม่มีคำแปลให้เว้นว่าง':key==='start'?'เช่น 09:00':key==='end'?'เช่น 12:00':'';root.append(i);")
js=js.replace("let ed=valueEditor(f.value_schema,unit.value??defaults(f.value_schema),f.reference_kind);","let ed=valueEditor(f.value_schema,unit.value??defaults(f.value_schema),f.reference_kind,f.key);ed.root.setAttribute('aria-label',f.meaning_th);box.dataset.field=f.key;s.setAttribute('aria-label','สถานะ: '+f.meaning_th);let h=FIELD_HELP[r.kind][f.key];box.append(node('p',h.hint));let ex=node('details');ex.className='field-example';ex.append(node('summary','ดูตัวอย่างการกรอก: '+f.meaning_th),exampleView(h.example),node('small','ตัวอย่างสมมุติสำหรับอธิบายช่องกรอก ไม่ใช่ข้อมูลจริงของศูนย์ และไม่ถูกใส่ลงในช่องอัตโนมัติ'));box.append(ex);")
js=js.replace("box.append(node('h3',(f.publish_core?'★ ':'')+f.meaning_th),node('small',f.key+(f.reference_kind?' → '+f.reference_kind:'')));","box.append(node('h3',(f.publish_core?'★ ต้องมี: ':'')+f.meaning_th));")
js=js.replace("$('state').textContent=revision?", "showGuide(r.kind);updateReadiness();$('state').textContent=revision?")
js=js.replace("$('kind').onchange=drawList;", "$('kind').onchange=()=>task(async()=>{if(dirty&&!await confirmAction('มีข้อมูลที่ยังไม่บันทึก ต้องการเปลี่ยนหมวดและออกจากรายการนี้หรือไม่?')){$('kind').value=record.kind;return;}dirty=false;record=null;saved=null;$('editor').hidden=true;$('welcome').hidden=false;showGuide($('kind').value);drawList();});")
js=js.replace("for(let c of x.catalog)$('kind').append(new Option(c.owner_form,c.kind));", "let groups={};for(let c of x.catalog){let h=OWNER_HELP[c.kind];if(!groups[h.group]){let g=node('optgroup');g.label=h.group;$('kind').append(g);groups[h.group]=g;}groups[h.group].append(new Option(h.label,c.kind));}")
js=js.replace("await refresh();message('พร้อมกรอกข้อมูล", "await refresh();showGuide('game');message('พร้อมกรอกข้อมูล")
extra=r'''
function exampleView(v){let root=node('div');root.className='example-values';if(Array.isArray(v)){if(!v.length)root.append(node('p','ไม่เพิ่มรายการ (ใช้ได้เฉพาะเมื่อยืนยันว่าเป็นรายการว่างจริง)'));v.forEach((x,i)=>{let item=node('div');item.append(node('strong','รายการที่ '+(i+1)),exampleView(x));root.append(item);});}else if(v&&typeof v==='object'){for(let [k,x] of Object.entries(v)){let l=node('div');l.append(node('strong',(SUB_LABELS[k]||k)+': '),exampleView(x));root.append(l);}}else root.append(node('span',v===null?'เว้นว่าง':typeof v==='boolean'?(v?'ใช่ / มี / รองรับ':'ไม่ใช่ / ไม่มี / ไม่รองรับ'):OPTION_LABELS[v]||String(v)));return root;}
function showGuide(kind){let h=OWNER_HELP[kind],c=catalog[kind];$('guide').replaceChildren();$('guide').append(node('h2','เลือกหมวดนี้เมื่อไหร่?'),node('h3',h.label),node('p',h.when),node('p','ช่วยตอบคำถาม เช่น “'+h.question+'”'));let box=node('div');box.className='guide-tip';box.append(node('strong','จำง่าย ๆ: '),node('span',h.tip));$('guide').append(box);let before=h.before.filter(k=>k!==kind).map(k=>OWNER_HELP[k].label);$('guide').append(node('p','ต้องมีข้อมูลไหนก่อน: '+(before.length?before.join(' → ')+' (เฉพาะช่องที่ใช้เชื่อม)':'เริ่มกรอกหมวดนี้ได้เลย ไม่ต้องสร้างหมวดอื่นก่อน')));let core=node('ul');for(let f of c.fields.filter(f=>f.publish_core))core.append(node('li',f.meaning_th));let det=node('details');det.append(node('summary','ก่อนเผยแพร่ ต้องมีอะไรบ้าง ('+c.fields.filter(f=>f.publish_core).length+' ช่อง)'),core);$('guide').append(det);$('new').textContent='＋ เพิ่ม'+h.label;$('rid').placeholder=kind+'_example';$('form_intro').textContent='เริ่มจากช่อง ★ เลือก “มีข้อมูลยืนยัน” แล้วกรอกตามข้อมูลจริง ช่องที่ยังไม่ทราบเก็บเป็นร่างได้';}
function updateReadiness(){if(!record)return;let needed=catalog[record.kind].fields.filter(f=>f.publish_core);let missing=needed.filter(f=>editors[f.key]?.s.value!=='known');$('readiness').textContent=missing.length?'ยังต้องยืนยัน '+missing.length+' ช่องก่อนเผยแพร่: '+missing.map(f=>f.meaning_th).join(' / '):'เลือกยืนยันช่องหลักครบแล้ว กรุณาตรวจค่าที่กรอก แหล่งข้อมูล รายการที่เชื่อม และช่วงวันที่ก่อนอนุมัติ';}
$('fields').addEventListener('change',updateReadiness);
'''
# Function definitions/events must precede asynchronous startup completion; appended synchronously is safe.
js+='\n'+extra

html=(UI/'index.html').read_text(encoding='utf-8')
html=html.replace('<h1>PSU Esports • ข้อมูลกลาง</h1>','<h1>จัดการข้อมูลให้แชทบอท PSU Esports</h1>')
html=html.replace('<section><div id="welcome">','<section><nav class="steps" aria-label="ลำดับการใช้งาน"><span>1 เลือกหมวด</span><span>2 กรอกและบันทึกร่าง</span><span>3 ตรวจทาน</span><span>4 เผยแพร่ให้แชทบอท</span></nav><div id="guide" class="guide"></div><div id="welcome">')
html=html.replace('<h2>เริ่มจากหมวดเกม หรือหมวดที่ต้องการ</h2>','<h2>เริ่มใช้ได้ใน 4 ขั้นตอน</h2><ol><li>เลือกหมวดทางซ้าย แล้วอ่านคำอธิบายด้านบน</li><li>กด “เพิ่ม…” หรือเลือกข้อมูลเดิมเพื่อแก้ไข</li><li>เปิด “ดูตัวอย่างการกรอก” ใต้แต่ละช่อง แล้วใส่ข้อมูลจริง</li><li>บันทึกร่าง → ตรวจทานและอนุมัติ → เผยแพร่</li></ol><p>ไม่จำเป็นต้องกรอกครบทั้ง 24 หมวด เลือกเฉพาะเรื่องที่ต้องการให้แชทบอทรู้</p>')
html=html.replace('<label>รหัสถาวร ', '<p id="form_intro"></p><p id="readiness" class="readiness" role="status"></p><label>รหัสรายการ (ตั้งครั้งเดียว) ')
html=html.replace('ใช้ a-z, ตัวเลข, _ : - อย่างน้อย 3 ตัว เปลี่ยนชื่อได้โดยคงรหัสเดิม','ตัวอย่าง game_example ใช้ตัวอังกฤษเล็ก ตัวเลข หรือ _ : - อย่างน้อย 3 ตัว ไม่ใช่ชื่อที่ลูกค้าจะเห็น; เปลี่ยนชื่อในช่องข้อมูลได้ แต่คงรหัสนี้ไว้')
html=html.replace('ชื่อเรียกอื่น / Alias จริง (ไม่จำเป็นต้องใส่ทุกคำสะกดผิด)','ชื่อย่อหรือชื่อที่ลูกค้าเรียก (ไม่จำเป็นต้องกรอก)')
html=html.replace('ช่วงวันที่ข้อมูลมีผล','ข้อมูลนี้เริ่มใช้เมื่อไหร่?')
html=html.replace('ราคา ตารางเวลา วันปิด กติกา และข่าว ต้องยืนยันช่วงวันที่ก่อนเผยแพร่','ตัวอย่าง: เริ่มใช้ 1 ธันวาคม 2026 เวลา 09:00 ให้เลือกวันที่และเวลาในช่องด้านบน (ตัวอย่างสมมุติ) ราคา ตารางเวลา วันปิด กติกา และข่าว ต้องยืนยันช่วงวันที่ก่อนเผยแพร่; วันปิดพิเศษให้กรอกวันที่ปิดในช่องข้อมูลของหมวดนั้นด้วย')
html=html.replace('สถานะภาษา','จะให้ตอบภาษาอังกฤษด้วยไหม?')
html=html.replace('</select></label></details>\n<div id="fields">','</select></label><p>กรอกไทยอย่างเดียวได้ถ้ายังไม่มีคำแปล หากมีอังกฤษด้วยให้เลือกสถานะตามจริง: “แปลโดยระบบ” หรือ “เจ้าของตรวจความหมายแล้ว”; สถานะตรวจแล้วต้องติ๊กยืนยันการตรวจคำแปลด้านล่างด้วย</p></details>\n<div id="fields">')
html=html.replace('ดาวน์โหลดข้อมูล JSON','ดาวน์โหลดสำเนาข้อมูล (สำหรับผู้ดูแล)')
css=(UI/'owner.css').read_text(encoding='utf-8')+'''
[hidden]{display:none!important}.steps{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:18px}.steps span{padding:8px 10px;border-radius:20px;background:#e8eff7;font-size:14px}.guide{background:#f2f7fc;border:1px solid #c8d9ec;padding:18px;border-radius:10px;margin-bottom:24px}.guide h2{margin-top:0}.guide h3{font-size:20px;color:#123b6b}.guide-tip{border-left:4px solid #1f668c;padding:10px;background:#fff}.readiness{background:#fff7e6;border:1px solid #e8d6a6;padding:12px;border-radius:7px}.field>p{font-size:14px;color:#465c73;line-height:1.7}.field-example{background:#f8fafc}.example-values{line-height:1.8;padding:5px 10px}.example-values .example-values{border-left:2px solid #dce4ef;margin:4px 0}button:focus-visible,input:focus-visible,select:focus-visible,textarea:focus-visible,summary:focus-visible{outline:3px solid #5d94bf;outline-offset:2px}.guide li{margin:7px 0}section{min-width:0}#fields small{margin-top:8px}#readiness{overflow-wrap:anywhere}aside h2{margin-top:0}dialog{max-width:550px;border:1px solid #ccd9e9;border-radius:12px;padding:24px}dialog::backdrop{background:#18324f66}
'''
stage=RUN/'stage';stage.mkdir()
for name,data in {'owner.js':js,'index.html':html,'owner.css':css}.items():(stage/name).write_text(data,encoding='utf-8')
# Validate every help example against the existing field schema; no records are created.
import sys
sys.path.insert(0,str(PACK));sys.path.insert(0,str(UI.parent/'vendor'))
from jsonschema import Draft202012Validator,FormatChecker
errors=[]
for c in catalog:
    for f in c['fields']:
        for e in Draft202012Validator(f['value_schema'],format_checker=FormatChecker()).iter_errors(fieldhelp[c['kind']][f['key']]['example']):errors.append(c['kind']+'.'+f['key']+': '+e.message)
(RUN/'example_validation.json').write_text(json.dumps({'categories':len(helpdata),'fields':sum(len(c['fields']) for c in catalog),'errors':errors},ensure_ascii=False,indent=2),encoding='utf-8')
if errors:raise SystemExit('\n'.join(errors))
for base in (PACK,CAND):
    for name in ('index.html','owner.js','owner.css'):
        target=base/'app/knowledge/common/ui'/name
        if hashlib.sha256(target.read_bytes()).hexdigest()!=backups[str(target)]['sha256']:raise RuntimeError('Changed during editing: '+str(target))
        shutil.copy2(stage/name,target)

# All-category plain-language guide, same examples as the UI.
doc=['# กรอกข้อมูลให้แชทบอท: คู่มือพร้อมตัวอย่างทุกหมวด','',
'## เปิดใช้งาน','', 'ดับเบิลคลิก `Open-Owner-Content.cmd` ในโฟลเดอร์แพ็กเกจ แล้วเลือกหมวดทางซ้าย หน้ากรอกมีคำอธิบายและตัวอย่างให้ดูทันที','',
'## ทำแค่ 4 ขั้นตอน','', '1. เลือกหมวด → กดเพิ่ม หรือเลือกข้อมูลเดิม', '2. ช่องที่รู้จริงเลือก “มีข้อมูลยืนยัน” แล้วกรอก; ช่องที่ยังไม่รู้คง “ไม่ทราบ” เปิดดูตัวอย่างใต้ช่องได้', '3. ตรวจข้อมูลจริง ติ๊กยืนยันแหล่งข้อมูล แล้วบันทึกร่าง; ตรวจทานและอนุมัติเมื่อพร้อม', '4. เผยแพร่ให้แชทบอทอ่าน แล้วลองถามจากหน้าแชท คำถามใหม่จะอ่านฉบับใหม่','',
'ร่างที่ยังไม่ครบสามารถบันทึกได้ แต่ช่อง ★ ต้องมีข้อมูลก่อนอนุมัติ/เผยแพร่ การอนุมัติและเผยแพร่ยังตรวจค่าจริงและรายการที่เชื่อมด้วย ไม่ใช่แค่เลือกสถานะครบ','',
'ตัวอย่างทั้งหมดด้านล่างเป็นข้อมูลสมมุติเพื่ออธิบายการกรอก ไม่ใช่ประกาศ ราคา หรือกติกาจริงของ PSU ไม่ใส่ตัวอย่างลงฐานข้อมูลอัตโนมัติ','',
'## เลือกหมวดอย่างรวดเร็ว','', '| ต้องการเพิ่ม | เลือกหมวด |', '|---|---|', '| ชื่อเกม / เกมเกี่ยวกับอะไร | เกม |', '| ยืนยันว่าศูนย์มีเกมนี้บนเครื่องใด | เกมที่มีให้เล่นจริง |', '| ปุ่มกระโดด / ปุ่มยิง | ปุ่มควบคุมเกม |', '| เล่นกับเพื่อนได้กี่คน | การเล่นกับเพื่อน |', '| เพิ่ม PC #01 | เครื่องจริง |', '| เพิ่มตัวเลือก PC 1 ชั่วโมงบนหน้าจอง | ตัวเลือกบริการบนหน้าจอง |', '| ค่าบริการบุคคลทั่วไป | กลุ่มผู้ใช้ + ค่าบริการปกติ |', '| ราคาเหมาเต็มวัน | ราคาเหมา |', '| วันจันทร์เปิดกี่โมง | เวลาประจำสัปดาห์ |', '| ปิดเฉพาะวันที่กำหนด | วันปิดพิเศษ |', '| ทำได้หรือไม่ได้ | กฎศูนย์ |', '| ต้องทำอย่างไรทีละขั้น | ขั้นตอนบริการ |', '| แข่งเกมไหน ปีอะไร | รายการแข่งขัน |', '| กติกาทีม / ตัวสำรอง / บทลงโทษ | ข้อกติกาการแข่งขัน |', '',
'## ตัวอย่างงานที่ต้องใช้หลายหมวด','',
'### เพิ่มเกมใหม่ให้ตอบได้ครบ','', '1. **เกม**: ใส่ชื่อ เนื้อหา และวิธีเล่น → เผยแพร่', '2. **โซน → เครื่องจริง → ตัวเลือกบริการ**: สร้างเฉพาะรายการที่ยังไม่มี แล้วเผยแพร่ตามลำดับ', '3. **เกมที่มีให้เล่นจริง**: เลือกเกมและบริการนั้น ระบุมี/ไม่มี และเครื่องเฉพาะถ้าทราบ', '4. **ปุ่มควบคุมเกม**: เลือกเกม แพลตฟอร์ม อุปกรณ์ ชุดปุ่ม และเพิ่มปุ่มทีละรายการ', '5. **การเล่นกับเพื่อน**: กรอกโหมดและจำนวนผู้เล่นที่ตรวจแล้ว หากอยากให้ตอบเรื่องเล่นหลายคน', '',
'กรอกแค่หมวดเกมจะให้ข้อมูลทั่วไปของเกม แต่ยังไม่ยืนยันว่าศูนย์ติดตั้งเกมหรือมีปุ่มควบคุมเกมนั้น','',
'### เพิ่มราคาใหม่','', 'สร้างหรือเลือก **กลุ่มผู้ใช้** และ **ตัวเลือกบริการ** ที่ตรงกัน → เผยแพร่รายการที่เชื่อมก่อน → เพิ่ม **ค่าบริการปกติ** พร้อมวันเริ่มมีผล หน่วยราคา จำนวนคน และวิธีคิดตามเอกสาร','',
'ราคาในช่องนี้เป็นสตางค์: 35 บาท → 3500, 35.50 บาท → 3550, 4,000 บาท → 400000; ใส่ 0 เฉพาะเมื่อยืนยันว่าฟรี ระบบคำนวณราคาและปฏิทินบางเส้นทางยังใช้ตัวอ่านเดิมร่วมด้วย ต้องตรวจคำตอบจริงก่อนนำข้อมูลใหม่ไปใช้ทุกเส้นทาง','',
'### เพิ่มกติกาแข่งขัน','', 'เกม → รายการแข่งขัน (เกม/ชื่อ/ปี/ฉบับ) → ข้อกติกาทีละข้อ (เลขข้อ/หมวด/ข้อความเต็ม) หากมีข้อยกเว้นเชื่อมกันต้องเลือกข้อที่เกี่ยวข้องของรายการเดียวกัน','',
'### เพิ่มเวลาเปิดหรือวันปิด','', 'เวลาประจำสัปดาห์ = ตารางตามชื่อวัน; วันปิดพิเศษ = วันที่แน่นอน เวลาเปิดพื้นที่กับช่วงจองได้กรอกแยกกัน ตัวอย่าง 09:00–17:00 เปิดพื้นที่ แต่ช่วงจอง 09:00–12:00 และ 13:00–17:00 ไม่ได้ทำให้จองช่วง 12:00–13:00 ได้','',
'## ตัวอย่างแต่ละหมวด','']
for c in catalog:
    h=helpdata[c['kind']];doc += ['### '+h['label'],'', '**ใช้เมื่อ:** '+h['when'],'', '**ช่วยตอบ:** '+h['question'],'', '**จำง่าย ๆ:** '+h['tip'],'', '**ข้อมูลที่ต้องมีมาก่อน (เฉพาะช่องที่ใช้เชื่อม):** '+(' / '.join(helpdata[k]['label'] for k in h['before'] if k!=c['kind']) or 'ไม่ต้องมีหมวดอื่นก่อน'),'','| ช่อง | จำเป็นก่อนเผยแพร่ | วิธีกรอก / ตัวอย่างสมมุติ |','|---|---|---|']
    for f in c['fields']:
        fh=fieldhelp[c['kind']][f['key']];e=json.dumps(fh['example'],ensure_ascii=False)
        doc.append('| '+f['meaning_th'].replace('|','/')+' | '+('★ ต้องยืนยัน' if f['publish_core'] else 'ยังไม่ทราบได้')+' | '+fh['hint'].replace('|','/')+'<br>ตัวอย่าง: `'+e.replace('|','/')+'` |')
    doc.append('')
doc += ['## ข้อที่มักสับสน','', '- **ไม่ทราบ** = ยังไม่มีหลักฐาน; **ไม่เกี่ยวข้อง** = ยืนยันแล้วว่าช่องนี้ใช้ไม่ได้กับรายการนี้; **ไม่มี/ไม่รองรับ** = เลือกมีข้อมูลยืนยัน แล้วเลือก “ไม่ใช่ / ไม่มี / ไม่รองรับ”', '- **รายการว่าง** = เลือกมีข้อมูลยืนยันแล้วไม่เพิ่มแถว ใช้เฉพาะช่องที่ความหมายอนุญาต เช่น ทุกโซนหรือไม่มีเงื่อนไข; ไม่ใช่การแทนค่าที่ไม่ทราบ', '- **ชื่อเรียกอื่น** = ชื่อย่อที่ใช้จริง เช่น ชื่อย่อเกม ไม่ต้องสร้างรายการทุกคำพิมพ์ผิด', '- **อังกฤษ** = ยังไม่มีก็เว้นว่าง ถ้ามีคำแปลเลือกแปลโดยระบบหรือเจ้าของตรวจแล้วตามจริง หากเลือกตรวจแล้วต้องติ๊กยืนยันฉบับนี้ด้วย', '- **วันเริ่มมีผล** = ใช้วันที่ ค.ศ. และเวลาไทยตามประกาศจริง ไม่ใช้วันที่ตัวอย่างเป็นนโยบาย', '- **ไม่พบชื่อในช่องเชื่อม** = สร้างและบันทึกหมวดต้นทางก่อน แล้วกลับมาโหลดรายการล่าสุด/เปิดรายการนี้ใหม่ รายการต้นทางต้องเผยแพร่ก่อนรายการที่อ้างถึง', '- **บันทึกร่างแล้วแชทยังไม่เปลี่ยน** = ต้องอนุมัติและเผยแพร่ก่อน หน้า “ทดลองคำตอบ” อ่านเฉพาะฐานกลาง; สถานะจองสดและระบบรวมต้องลองหน้าแชท', '- **สถานะว่าง** = อ่านจาก WordPress ตามเวลา ไม่กรอกด้วยมือในเครื่องจริงหรือ FAQ', '', '## ก่อนใช้ข้อมูลจริง','', 'ตรวจชื่อ/จำนวน/ราคา/วันที่จากเจ้าของ ไม่เติมข้อห้ามหรือเงื่อนไขใหม่โดยเดา ร่างเดิม 41 รายการยังต้องตรวจตามจริง การแสดงตัวอย่างช่วยกรอก ไม่ใช่การยืนยันข้อมูลเดิมแทนเจ้าของ','']
(RUN/'OWNER_EASY_GUIDE_TH.md').write_text('\n'.join(doc),encoding='utf-8')
for base in (PACK,CAND):
    (base/'owner_content_docs/OWNER_EASY_GUIDE_TH.md').write_text('\n'.join(doc),encoding='utf-8')
plan={'run':str(RUN),'before':backups,'stage':str(stage),'targets':[str(ROOT/'app/knowledge/common/ui'/n) for n in ('index.html','owner.js','owner.css')], 'examples_are_display_only':True}
(OUT/'owner_help_latest.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'run':str(RUN),'categories':24,'fields':155,'example_errors':errors,'ready_and_candidate_updated':True},ensure_ascii=False))
