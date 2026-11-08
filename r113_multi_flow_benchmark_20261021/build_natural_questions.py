"""Rephrase source-oracle tasks into natural and contrastive wording.

No strategy/model outputs are consulted. This remains a development corpus,
not a representative independent holdout or a claim of production accuracy.
"""
import hashlib,json,random,re
from pathlib import Path
R=Path(__file__).resolve().parent;model=json.loads((R/'COMMON_READ_MODEL.json').read_text('utf8'));facts={f['id']:f for f in model['facts']}
old=[json.loads(s) for s in (R/'pilot_field_contract/QUESTIONS_1400.jsonl').read_text('utf8').splitlines()]
patterns={
'address':(['เดินทางไปหา {s} ต้องไปที่ไหน','ขอพิกัดที่อยู่ของ {s}','{s} ตั้งอยู่ที่ใด'],['Where can I find {s}?','What is the address of {s}?']),
'building':(['{s} อยู่ตึกอะไร','จะไป {s} ต้องเข้าอาคารไหน','บอกเลขอาคารของ {s} ที'],['Which building houses {s}?','In what building is {s}?']),
'floor':(['{s} อยู่ชั้นไหน','ต้องขึ้นไปชั้นอะไรถึง {s}','ขอเลขชั้นที่ตั้ง {s}'],['On which floor is {s}?','What floor should I go to for {s}?']),
'map_url':(['ส่งลิงก์นำทางไป {s} ให้ที','มีแมพของ {s} ไหม','เปิดแผนที่ไป {s} จากลิงก์ไหน'],['Can you give me directions to {s} as a map link?','Send me a map for {s}.']),
'role':(['{s} ทำหน้าที่อะไร','ตำแหน่งของ {s} คืออะไร','ใครดูแลงานอะไรในกรณีของ {s}'],['What does {s} do at the studio?','Which role does {s} have?']),
'display_name':(['ขอชื่อที่แสดงในระบบของ {s}','{s} ใช้ชื่ออะไร','ชื่อเต็มของ {s} คืออะไร'],['How is {s} listed by name?','Give the full name recorded for {s}.']),
'team':(['{s} อยู่ทีมไหน','หน่วยงานของ {s} คือทีมใด','{s} สังกัดกลุ่มอะไร'],['Which team is {s} part of?','What group does {s} belong to?']),
'location':(['{s} อยู่โซนไหน','โซนไหนมี {s}','อยากหา {s} ต้องไปบริเวณใด'],['Where is {s} located?','Which zone has {s}?']),
'quantity':(['{s} มีทั้งหมดกี่เครื่อง','ของรุ่น {s} มีให้ใช้กี่ชุด','จำนวนเครื่องของ {s} เท่าไร'],['How many units of {s} are there?','How many {s} devices are provided?']),
'controllers':(['{s} เครื่องหนึ่งมีจอยให้กี่อัน','ใช้ {s} จะได้คอนโทรลเลอร์กี่ตัว','ขอจำนวนจอยต่อเครื่องของ {s}'],['How many controllers come with one {s}?','Are there two controllers for each {s}?']),
'specifications':(['สเปกของ {s} เป็นแบบไหน','อยากดูรายละเอียดฮาร์ดแวร์ {s}','{s} ใช้สเปกอะไร'],['What hardware specifications does {s} have?','Tell me the technical specs of {s}.']),
'capacity_persons':(['{s} ใช้พร้อมกันได้กี่คน','จำนวนคนที่เล่น {s} พร้อมกันได้มีเท่าไร','{s} รองรับผู้เล่นพร้อมกันเท่าไร'],['How many people can use {s} simultaneously?','What is the simultaneous player capacity of {s}?']),
'room_seats':(['ห้อง {s} มีที่นั่งกี่ที่','พื้นที่ {s} นั่งได้กี่คน','จำนวนที่นั่งในห้อง {s} มีเท่าไร'],['How many seats are in the {s} room?','What is the room seating capacity of {s}?']),
'summary':(['{s} เป็นเกมเกี่ยวกับอะไร','อธิบายว่า {s} คือเกมอะไร','เล่าเกี่ยวกับเกม {s} ให้ฟังที'],['What is {s} about?','Describe the game {s}.']),
'genre':(['{s} จัดเป็นเกมประเภทใด','แนวเกมของ {s} คืออะไร','{s} เป็นเกมแนวไหน'],['What genre is {s}?','Which game category does {s} belong to?']),
'how_to_play':(['{s} เล่นยังไง','เวลาเล่น {s} ผู้เล่นต้องทำอะไรบ้าง','ขอวิธีเริ่มเล่น {s}'],['How do you play {s}?','What do players do in {s}?']),
'supported_platforms':(['{s} รองรับแพลตฟอร์มไหนบ้าง','เกม {s} ออกให้เล่นบนระบบอะไร','{s} เล่นได้บนแพลตฟอร์มใด'],['What platforms does {s} support?','Which systems support {s}?']),
'studio_services':(['ที่ศูนย์จะเล่น {s} ต้องเลือกบริการไหน','{s} มีให้เล่นที่ไหนในศูนย์','จะเล่น {s} ต้องจองอะไร'],['Where can I play {s} in this studio?','Which studio service should I choose to play {s}?']),
'game_catalog':(['{s} มีเกมอะไรให้เลือกบ้าง','ขอดูรายชื่อเกมที่เล่นบน {s} ได้','ถ้าใช้บริการ {s} เลือกเล่นอะไรได้บ้าง'],['What games are available through {s}?','List all games offered on {s}.']),
'amount':(['เล่น {s} คิดกี่บาทต่อคนต่อรอบ','ขอราคาของ {s}','{s} มีค่าบริการเท่าไหร่'],['How much does {s} cost per person per session?','What is the price for {s}?']),
'amount_thb':(['ค่าเหมา {s} เท่าไร','ขอราคาแพ็กเกจ {s}','ถ้าเช่า {s} ต้องจ่ายกี่บาท'],['How much is the rental package {s}?','What does the {s} package cost?']),
'duration_minutes':(['{s} ให้ใช้นานกี่นาที','เวลาใช้งานของ {s} นับเป็นกี่นาที','{s} ใช้ได้ยาวนานเท่าไหร่ถ้าบอกเป็นนาที'],['How many minutes does {s} cover?','What is the duration of {s}, in minutes?']),
'equipment_included':(['เหมา {s} ได้อุปกรณ์อะไรรวมมาบ้าง','{s} รวมเครื่องอะไรให้ใช้','แพ็กเกจ {s} มีอุปกรณ์อะไรให้'],['What equipment is included with {s}?','Which devices come with the {s} package?']),
'bookable_periods':(['วัน{s}จองเล่นได้กี่โมงถึงกี่โมง','วัน{s}มีรอบไหนให้จอง','ถ้าไปวัน{s}เลือกช่วงเล่นอะไรได้บ้าง'],['When can I reserve a play session on {s}?','What are the bookable hours on {s}?']),
'maintenance_periods':(['วัน{s}มีช่วงซ่อมบำรุงเมื่อไหร่','วัน{s}งดเล่นเพื่อ maintenance กี่โมง','ช่วงบำรุงรักษาของวัน{s}คือเวลาใด'],['When is maintenance on {s}?','Which hours are reserved for maintenance on {s}?']),
'description':(['งาน {s} คือกิจกรรมอะไร','ขอรายละเอียดของงาน {s}','{s} จัดเกี่ยวกับอะไร'],['What is {s} about?','Describe the event {s}.']),
'date':(['{s} จัดวันไหน','วันจัดงาน {s} คือวันที่เท่าไร','อยากไป {s} ต้องไปวันไหน'],['When does {s} take place?','What is the date of {s}?']),
'registration':(['จะสมัคร {s} ได้จากลิงก์ไหน','ขอลิงก์สมัครงาน {s}','มีช่องทางลงทะเบียน {s} ไหม'],['Where can I register for {s}?','Give me the registration URL for {s}.']),
'status':(['งาน {s} ยังสมัครได้ไหม','{s} ปิดรับสมัครหรือยัง','สถานะการรับสมัคร {s} เป็นอย่างไร'],['Is registration for {s} still open?','Has registration closed for {s}?']),
'live_status':(['{s} ว่างอยู่ไหม','ช่วยเช็กว่าจอง {s} ได้หรือยัง','อยากรู้ว่า {s} ถูกจองหรือยัง'],['Is {s} available?','Can you check whether {s} is already booked?']),
}
policy={
'Q001':('ถ้าไปถึงก่อนเวลาที่จอง รอที่ไหนและเข้าเล่นก่อนได้ไหม','If I arrive early, where can I wait and may I start playing early?'),
'Q003':('กำลังเล่นอยู่แล้วอยากต่อเวลา ต้องทำยังไง','How can I extend my play session while I am already playing?'),
'Q004':('เปลี่ยนไปเล่นบริการอื่นระหว่างรอบแล้วเงินเดิมคืนไหม','If I change to another service during my session, is the original payment refunded?'),
'Q005':('จองผิดวันแต่จ่ายเงินแล้วต้องแก้ยังไง','I paid for a booking on the wrong date. How can I correct it?'),
'Q008':('ไปไม่ทันเวลาเริ่มเล่นต้องแจ้งไหม','Do I have to notify the studio if I cannot arrive by the start time?'),
'Q009':('ฝนตกหนักไปไม่ทัน ขอเปลี่ยนรอบต้องส่งอะไรให้ใคร','Heavy rain prevents me from arriving. Who do I contact and what evidence is needed to reschedule?'),
'Q010':('ถ้าศูนย์ปิดหลังจากจองแล้วทางศูนย์จะแจ้งอย่างไร','How will the studio contact me if it closes after I have booked?'),
'Q011':('กรอกชื่อผิดในรายการจองต้องแก้ยังไง','How do I correct a wrong name on my booking?'),
'Q014':('โอนเงินเกินยอดต้องทำอย่างไร','What should I do if I overpaid?'),
'Q015':('ยอดที่โอนขาดไป ต้องส่งหลักฐานเพิ่มอย่างไร','How do I send evidence for an additional payment after underpaying?'),
'Q016':('สามารถแบ่งจ่ายหรือวางมัดจำก่อนใช้บริการได้ไหม','May I pay in instalments or pay a deposit instead of the full amount?'),
'Q017':('โอนแล้วปกติกี่นาทีตรวจเสร็จ ถ้ายังไม่เปลี่ยนสถานะทำไง','How long does payment verification normally take, and what if my status does not change?'),
'Q018':('ขอใบเสร็จ ใบเสนอราคาหรือใบกำกับภาษีได้ไหม','Can you issue a receipt, quotation or tax invoice?'),
'Q019':('มีปัญหาเรื่องเงินที่จ่ายต้องติดต่อที่ไหนพร้อมหลักฐานอะไร','Where do I contact the studio about a payment problem and what evidence should I provide?'),
'Q020':('เล่นเกม Steam ต้องใช้บัญชีตัวเองไหม','Do I need my own Steam account to play?'),
'Q022':('เล่นเสร็จแล้วศูนย์เก็บข้อมูลล็อกอินผู้เล่นไว้ไหม','Does the studio keep players login data after logging them out?'),
'Q025':('ถ้าเกมต้องอัปเดตนานเกินห้านาทีจะชดเชยเวลาไหม','Is extra play time provided if an update takes more than five minutes?'),
'Q026':('เกมเปิดไม่ได้แต่ไม่ได้กำลังอัปเดต ย้ายเครื่องได้ไหม','May I change machines when a game cannot run for a reason other than updating?'),
'Q027':('จะเช็กเวอร์ชันเกมก่อนมาเล่นต้องถามใคร','Who can confirm the installed game version before I visit?'),
'Q028':('อินเทอร์เน็ตหรือระบบขัดข้องระหว่างเล่นต้องทำยังไง','What should I do about network or system faults during play?'),
'Q029':('ถ้าเครื่องเสียเองไม่ได้เกิดจากคนเล่นต้องชดใช้ไหม','Must I pay compensation if the equipment fails without me causing it?'),
'Q030':('เมาส์หรืออุปกรณ์ต่อพ่วงเสียระหว่างเล่นแจ้งใคร','Whom should I notify to replace a faulty peripheral?'),
'Q032':('ผู้ปกครองต้องอยู่ดูตลอดไหมหรือเซ็นยินยอมอย่างเดียวได้','Does a guardian have to stay, or is signed consent enough?'),
'Q033':('แคปภาพและอัดวิดีโอในเกมได้ไหมแล้วต้องลบไหม','May I capture in-game screenshots or video, and should I delete them afterwards?'),
'Q034':('สตรีมเกมได้ทุกโซนหรือมีจำกัด','Is game streaming restricted to any particular zone?'),
'Q037':('บุคคลภายนอกใช้บริการทั่วไปของศูนย์ได้ครบไหม','May external visitors use all general studio services?'),
'Q040':('วันหยุดราชการต้องรอประกาศเปิดปิดจากช่องทางใด','Where should I check public-holiday opening announcements?'),
'Q041':('อยากเช่าจัดงานนอกเวลาเปิดปกติติดต่อได้ไหม','Can I arrange an out-of-hours rental or event?'),
'Q043':('ไม่ได้เล่นเองแต่อยากนั่งดูเพื่อนเล่นได้ไหม','May I sit and watch my friend without playing?'),
'Q044':('เอาอุปกรณ์เสริมส่วนตัวมาใช้ได้หรือไม่','May I use my own gaming accessories?'),
'Q045':('ถ้าเช่าเหมาอยากเลือกเวลาเริ่มเองทำได้ไหม','Can I arrange my own rental start time?'),
'Q047':('ต้องการจองเหมาโซนติดต่อผ่านช่องทางไหน','How do I contact the studio to book a whole-zone rental?'),
'Q048':('เงื่อนไขยกเลิกหรือคืนเงินของราคาเหมาต้องคุยกับใคร','Whom should I contact about rental cancellation or refund terms?'),
'Q049':('คิดค่าบริการรายชั่วโมงเป็นต่อคนหรือต่อเครื่อง','Are hourly service fees charged per person or per machine?'),
'Q050':('ราคาที่แจ้งรวมภาษีหรือยัง','Do the quoted prices include tax?'),
'R108_PAYER':('ผู้โอนเงินต้องมีชื่อในรายการจองด้วยหรือไม่','Must the person paying be named on the booking?'),
'R108_MIXED_RATE':('นักศึกษา PSU กับคนนอกมาเล่นด้วยกันจ่ายตามกลุ่มของแต่ละคนใช่ไหม','Do a PSU student and an external visitor each pay their own audience rate?'),
'R108_OPEN_16_18':('วันธรรมดาช่วงสี่โมงถึงหกโมงเย็นศูนย์เปิดอยู่ไหม','Is the studio open on weekdays between 16:00 and 18:00?'),
}
gap={
'C01':['ศูนย์มีช่อง TikTok ทางการชื่ออะไร','ศูนย์มีเบอร์แฟกซ์อะไร','ศูนย์มีทางเข้าอาคารทางทิศเหนือหมายเลขอะไร'],
'C02':['{s} ได้เงินเดือนเท่าไร','ขอเบอร์มือถือส่วนตัวของ {s}','ที่อยู่บ้านของ {s} คืออะไร'],
'C03':['ประกันของ {s} หมดวันไหน','ขอ serial number ของ {s}','{s} ซื้อจากร้านใด'],
'C04':['แพตช์ที่ติดตั้งของ {s} เป็นเลขอะไร','{s} มี DLC ทุกตัวให้ใช้ไหม','บัญชีเกม {s} ซื้อเมื่อวันใด'],
'C05':['ใน {s} ปุ่มไหนเปิดโหมดเทเลพอร์ตอัตโนมัติ','ขอปุ่มเปิดระบบ Auto Win ของ {s}','ใน {s} กดปุ่มใดเพื่อสร้างด่านใหม่อัตโนมัติ'],
'C06':['ราคา {s} ในปี 2028 จะเท่าไร','ขอราคาของ {s} สำหรับปี 2029','ปี 2027 อัตราของ {s} ยืนยันแล้วเป็นเท่าไร'],
'C07':['มัดจำของแพ็กเกจ {s} เป็นกี่เปอร์เซ็นต์','ถ้าเหมา {s} เกินเวลาจะปรับกี่บาทต่อนาที','เจ้าหน้าที่แพ็กเกจ {s} ค่าโอทีตายตัวกี่บาท'],
'C08':['จอง {s} แล้วจะรับประกันเครื่องสำรองส่วนตัวให้ไหม','คนจองขอแก้ประวัติบัญชีทั้งหมดย้อนหลังได้กี่วัน','ถ้าจองเป็นชื่อบริษัทจะได้สิทธิ์พิเศษอะไรที่ประกาศไว้'],
'C09':['จ่ายด้วยคริปโตได้กี่สกุล','เครดิตเงินโอนเกินหมดอายุแน่นอนกี่วัน','คืนเงินเข้าบัตรเครดิตภายในกี่วันแน่นอน'],
'C10':['เด็กอายุขั้นต่ำตัวเลขแน่นอนกี่ขวบจึงเข้าได้','ถ่ายใบหน้าลูกค้าคนอื่นแล้วเผยแพร่ได้โดยไม่ขอไหม','ความเสียหายทุกชนิดมีค่าปรับตายตัวกี่บาท'],
'C11':['วันนี้เปิดพื้นที่ทั้งวันแน่นอนกี่โมงถึงกี่โมง','ปี 2029 ศูนย์ปิดวันหยุดพิเศษวันไหนบ้าง','วันหยุดราชการทุกวันในปี 2028 เปิดหรือปิดแน่นอน'],
'C12':['เครื่อง PhantomStation77 พรุ่งนี้เที่ยงว่างไหม','ช่วยยืนยันรายการจองหมายเลข SECRET-7788 ว่าจ่ายแล้วหรือยัง','เครื่อง PC99 มีคนใช้อยู่ตอนนี้ไหม'],
'C13':['หน่วยโทษ Pause Tekken ที่ยังไม่ยืนยันเป็น Round Game หรือ Match','รายการปี 2030 มีค่าลงทะเบียนเท่าไร','การแข่งขัน CS2 ปี 2028 ใช้แผนที่อะไรแน่นอน'],
'C14':['ขอข่าวจริงล่าสุดของศูนย์ที่ยืนยันจากระบบสดวันนี้','โปรโมชันลับปี 2030 ลดกี่เปอร์เซ็นต์','กิจกรรมจริงที่ไม่ได้อยู่ในข้อมูลเปิดรับกี่ทีม'],
}
out=[];seen=set();wrapth=['','ขอสอบถามหน่อยครับ ','ช่วยตอบสั้น ๆ ว่า ','อยากรู้ว่า ','กำลังวางแผนไปใช้บริการ เลยขอถามว่า ','รบกวนเช็กให้หน่อย ','ถามจากข้อมูลที่ศูนย์ให้ไว้ '];wrapen=['','Could you help me with this: ','Please answer briefly: ','I would like to know: ','Based on the studio sources, ']
def phrase(f,lang,v):
 s=f['subject'][lang];facet=f['facet'];rid=f['record_id']
 if rid in policy:return policy[rid][lang=='en']
 if facet.startswith('binding_'):return (f'ถ้าจะ{f["label"][lang]}ใน {s} ต้องกดอะไร' if lang=='th' else f'Which input performs {f["label"][lang]} in {s}?')
 if facet=='rule_clause':
  return (f'ตามกติกา {s} เรื่อง{f["label"][lang]}กำหนดไว้อย่างไร' if lang=='th' else f'Under {s}, what does the section {f["label"][lang]} specify?')
 pat=patterns.get(facet)
 if pat:return pat[lang=='en'][v%len(pat[lang=='en'])].format(s=s)
 return (f'{s} มีข้อมูลเรื่อง{f["label"][lang]}อย่างไร' if lang=='th' else f'For {s}, explain the {f["label"][lang]}.')
for j in old:
 j=json.loads(json.dumps(j));n=int(j['id'].split('-Q')[1])-1;cat=j['category'];lang='en' if j['locale']=='en' else 'th'
 exp=j['expected']['claims'];fs=[facts[x['fact_id']] for x in exp]
 if n>=80:
  sub=next(f for f in model['facts'] if f['category']==cat)['subject']['th'];q=gap[cat][n%len(gap[cat])].format(s=sub)
  q=wrapth[(n//len(gap[cat]))%len(wrapth)]+q
  j['expected']['status']='not_current' if cat=='C06' else 'missing_source'
 else:
  first=fs[0];q=phrase(first,lang,n)
  if j['stratum']=='multi_need':
   second=next((f for f in fs if f['subject'][lang]!=first['subject'][lang] or f['label'][lang]!=first['label'][lang]),None)
   if second:q+=(' and also ' if lang=='en' else ' แล้วขอ')+phrase(second,lang,n+1)
  if cat=='C06' and first['facet']=='amount' and j['stratum']=='single_need':q+=(f' รวม {j["expected"]["sessions"]} รอบ' if lang=='th' else f' for {j["expected"]["sessions"]} sessions')
  q=(wrapen[n%len(wrapen)] if lang=='en' else wrapth[n%len(wrapth)])+q
  # Typo channel changes only question vocabulary, never proper names/numbers.
  if n%7==0:q=q.replace('อย่างไร','อย่างไรร').replace('กี่เครื่อง','กี่เครือง').replace('Which input','Wihch input').replace('What is','Waht is')
 suffix=0;baseq=q
 follow_th=['ขอสรุปให้เข้าใจง่าย','ช่วยระบุเงื่อนไขที่เกี่ยวข้องด้วย','ขอใช้ข้อมูลที่ยืนยันได้','รบกวนตอบเฉพาะเรื่องนี้','ขอคำตอบสำหรับผู้เข้าใช้บริการ','ถ้ามีข้อจำกัดช่วยบอกด้วย','อยากทราบรายละเอียดตามข้อมูลศูนย์','ขอสรุปประเด็นสำคัญ','ช่วยอธิบายตรงคำถามนี้','ขออ้างอิงข้อมูลที่มี']
 follow_en=['Please explain clearly.','Include relevant conditions.','Use confirmed information.','Stay with this point.','Explain for a studio visitor.','Mention any limitations.','Use the studio sources.','Summarize the key point.','Please address this question.','Give the recorded information.']
 while (cat,q) in seen:
  q=baseq+' '+(follow_en if lang=='en' else follow_th)[suffix%10];suffix+=1
  if suffix>10:q=(wrapen if lang=='en' else wrapth)[suffix%len(wrapen if lang=='en' else wrapth)]+q
  assert suffix<30
 seen.add((cat,q));j['question']=q;j['question_origin']='source-grounded natural paraphrase/contrast development corpus; independently expected source claims; not representative user holdout';out.append(j)
assert len(out)==1400 and len(seen)==1400
p=R/'NATURAL_QUESTIONS_1400.jsonl';assert not p.exists();p.write_text('\n'.join(json.dumps(j,ensure_ascii=False) for j in out)+'\n','utf8')
manifest={'questions':1400,'per_category':100,'per_flow':100,'executions':4200,'question_set_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'read_model_sha256':hashlib.sha256((R/'COMMON_READ_MODEL.json').read_bytes()).hexdigest(),'strata_per_category':{'single_need':60,'multi_need':20,'missing_or_unconfirmed':20},'fixture_categories':['C12','C14'],'limits':['Source-grounded natural paraphrases remain a development set, not independent human semantic adjudication.','Expected identities were frozen from source tasks before strategy outputs; no answers were used to tune expected values.','Domain category is given to adapters; end-to-end category routing is not evaluated.','Provider/news are isolated fixtures; several rule excerpts lack English translation.','The earlier direct-field pilot was too easy and is preserved separately, not used as the headline result.']}
(R/'NATURAL_WORKLOAD_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),'utf8');print(json.dumps(manifest,ensure_ascii=False))
