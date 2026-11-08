"""Language meanings and field contracts; no venue facts or per-question answers."""
import re

FACETS={
 'operator':r'มหาวิทยาลัย|ของใคร|ใคร(?:ดำเนิน|ดูแลศูนย์)|ผู้ดำเนิน|university|operat(?:or|ed)|owned by',
 'description':r'รายละเอียด(?:ของ)?งาน|รายละเอียดกิจกรรม|กิจกรรมอะไร|จัดเกี่ยวกับ|event details|describe (?:the )?event|what is .+ about',
 'address':r'ที่อยู่|อยู่ตรงไหน|อยู่ที่ไหน|ศูนย์อยู่|ตั้งอยู่ที่ใด|ต้องไปที่ไหน|address|where (?:is|can (?:i|we) find)|where .*(?:studio|cent(?:er|re))|located',
 'building':r'ตึก|อาคาร|building', 'floor':r'ชั้น(?:ไหน|อะไร|ที่)|\bfloor\b','map_url':r'แผนที่|แมพ|นำทาง|\bmap\b',
 'value':r'ติดต่อ|ช่องทาง|เพจ|contact|phone|facebook|เบอร์',
 'role':r'หน้าที่|ตำแหน่ง|ดูแลงาน|งานอะไร|รับผิดชอบ|role|responsib|position|duties|what does .+ do',
 'affiliation':r'สังกัด|คณะไหน|วิทยาลัยไหน|affiliation|affiliated|which (?:faculty|college|institution)',
 'period':r'ช่วงเวลา|ดำรงตำแหน่ง.*(?:ปี|เมื่อ)|รุ่นปี|วาระ|term of office|tenure|(?:profile|recorded|employment|appointment) period|which (?:year|cohort)',
 'team':r'\bteam\b|ทีม(?:ไหน|อะไร|ที่สังกัด)|อยู่กลุ่มไหน|สังกัดกลุ่ม|group.+belong','display_name':r'รายชื่อ|ใครบ้าง|ชื่ออะไร|แนะนำชื่อ|\bname\b|who (?:is|are)|listed.+directory',
 'location':r'ที่ตั้ง|อยู่โซนไหน|โซนไหน|อยู่ตรงไหน|อยู่ที่ไหน|ตั้งอยู่|บริเวณใด|location|which zone|where .*(?:located|find)',
 'quantity':r'จำนวนเครื่อง|กี่เครื?อง|กี่เครือง|กี่ชุด|มีทั้งหมดกี่|how many .*?(?:units|machines|consoles|devices)|\bquantity\b',
 'capacity_persons':r'กี่คน|จำนวนคน|เล่นพร้อมกัน|simultaneous|how many (?:people|players)|player capacity',
 'service_capacity':r'ช่วงจำนวนผู้ใช้|จำนวนผู้ใช้ตาม(?:รายการ)?บริการ|service participant range|listed service capacity',
 'controllers':r'กี่จอย|จอย(?:ต่อ|กี่|จำนวน|ให้กี่)|how many controllers|controllers? per',
 'specifications':r'สเปก|ฮาร์ดแวร์|spec(?:ification)?s?|hardware',
 'device_type':r'ชนิดอุปกรณ์|ประเภทอุปกรณ์|device type|kind of device',
 'usage':r'การใช้งาน|ใช้ทำอะไร|ใช้อย่างไร|usage|used for',
 'summary':r'คือ(?:เกม)?อะไร|เกี่ยวกับ(?:เกม|อะไร)|เล่าเกี่ยวกับเกม|คำอธิบายเกม|overview|what is|what.+about|tell me about|describe (?:the )?game',
 'official_description':r'คำบรรยายฉบับเต็ม|คำบรรยาย.*ต้นทาง|รายละเอียด(?:ฉบับ)?เต็ม.*เกม|official description|full (?:source )?description|detailed (?:game )?description',
 'genre':r'แนวเกม|เกมแนวไหน|ประเภทเกม|เกมประเภทใด|\bgenre\b|what kind of game|game category',
 'how_to_play':r'วิธี(?:เริ่ม)?เล่น|เล่นยังไง|เล่นอย่างไรร?|ผู้เล่นต้องทำ|how (?:do|can).+play|how to play|what do players do',
 'supported_platforms':r'รองรับแพลตฟอร์ม|ออกให้เล่นบนระบบ|แพลตฟอร์มใด|platforms?.*support|which systems|supported platforms',
 'studio_services':r'ต้องเลือกบริการ|ต้องจองอะไร|มีให้เล่นที่ไหน|where can i play|which studio service|บริการไหน',
 'game_catalog':r'มีเกมอะไร|รายชื่อเกม|เลือกเล่นอะไร|เกมไหนบ้าง|\b(?:what|which) games?\b|list all games|games .*(?:available|offered)',
 'players_max':r'กี่คน|เล่นด้วยกัน|สองคน|สี่คน|เพื่อน|multiplayer|players|together|two people|four people',
 'amount':r'กี่บาท|ราคา|ค่าบริการ|ค่าเล่น|เท่าไ[รหร่]|\bprice\b|\bcost\b|\brate\b|how much|\bfee\b',
 'amount_thb':r'กี่บาท|ราคา|ค่าเหมา|\bprice\b|\bcost\b|how much',
 'duration_minutes':r'กี่นาที|เป็นนาที|ยาวนาน|ระยะเวลา|ใช้ได้นาน|how many minutes|duration|how long',
 'equipment_included':r'รวม.*(?:อุปกรณ์|เครื่อง)|อุปกรณ์อะไร|อุปกรณ์ที่รวม|equipment.*included|devices.*come with|included equipment',
 'terms':r'เงื่อนไข|ข้อกำหนด|\b(?:terms?|conditions?)\b',
 'room_seats':r'ที่นั่ง(?:ใน)?ห้อง|ที่นั่ง(?:ทั้งหมด|กี่ที่)|นั่งได้กี่คน|room seats|room seating|how many seats.*room',
 'zone':r'แพ็กเกจ.*(?:โซนไหน|โซนใด)|(?:which|what) zones?.*(?:package|rental)|(?:package|rental).*(?:which|what) zones?',
 'audience':r'แพ็กเกจ.*(?:หน่วยงานใด|กลุ่มใด)|(?:which|what) (?:organizations?|audiences?).*(?:package|rental)|(?:package|rental).*(?:which|what) (?:organizations?|audiences?)',
 'bookable_periods':r'ช่วง(?:ไหน|เวลา).*จอง|จอง.*(?:กี่โมง|รอบไหน|ช่วง)|ช่วงเล่นอะไร|มีรอบไหนให้จอง|bookable|when can i reserve|hours.*book|book.*hours',
 'open_periods':r'เปิด|ปิด|opening|\bopen\b|\bclosed\b',
 'maintenance_periods':r'บำรุงรักษา|ซ่อมบำรุง|maintenance',
 'local_date':r'วันที่ปิดพิเศษ|exception date', 'reason':r'เหตุผล|\breason\b',
 'weekday_closing':r'(?:16|สี่โมง|4\s*(?:pm|p\.m)).*(?:18|หกโมง|6\s*(?:pm|p\.m))',
 'date':r'จัดวันไหน|วันที่เท่าไร|วันจัดงาน|ต้องไปวันไหน|when.+take place|date of|event date',
 'registration':r'ลิงก์สมัคร|ช่องทางลงทะเบียน|ช่องทางสมัคร|สมัคร.*ลิงก์|registration url|registration link|where can i register',
 'status':r'ยังสมัคร|ปิดรับสมัคร|สถานะการรับสมัคร|registration.*(?:open|closed)|has registration closed|registration status',
 'live_status':r'(?<!ระห)ว่าง|ถูกจอง|คนใช้อยู่|availability|available|already booked|occupied',
}

# The first pattern binds the source's semantic topic. The second binds a
# customer situation; values/decisions always come from the selected source.
POLICY_INTENTS=[
 ('booking_steps','C08',r'^how to book$|^booking_steps$|^booking steps$|^วิธีจอง$|^ขั้นตอนการจอง$',
  r'จอง.*(?:ทำยังไง|อย่างไร|ยังไง)|วิธีจอง|ขั้นตอน.*จอง|เข้าไปเล่น.*เริ่ม|how.*\b(?:start|begin)\b.*\b(?:play|visit|playing|visiting)\b|how (?:to|(?:can|do|should) (?:i|we)) (?:book|reserve)'),
 ('customer_cancel','C08',r'^cancel_advance_time$|^cancel.*in advance$|^cancel reservation$|^ยกเลิกการจอง$|^ยกเลิก.*ล่วงหน้า$',
  r'(?:(?:can|may|how|when).{0,30}(?:i|we).{0,20}cancel|cancel (?:my|our|a|the) (?:booking|reservation)|cancel after booking|(?:ยกเลิก.*การจอง|ยกเลิกจอง|ยกเลิก.*ล่วงหน้า|จอง.{0,25}ยกเลิก))'),
 ('studio_cancel','C08',r'booking_cancel_invalid_info|booking.*cancel.*no notice|reasons why.*cancel.*without prior notice|การจอง.*ยกเลิก.*ไม่แจ้ง|เหตุที่การจอง.*ยกเลิก',
  r'(?:\b(?:studio|system)\b\s+(?:(?:can|may|will|does|could)\s+)?cancel|(?:ศูนย์|ระบบ)\s*(?:จะ|สามารถ|มีสิทธิ์|เป็นผู้)?\s*ยกเลิก|(?:cancel|ยกเลิก).*(?:without.*notice|ไม่แจ้ง|ข้อมูล.*(?:ผิด|ไม่ถูก)|invalid.*info))'),
 ('booking_session_limit','C08',r'^booking_session_and_payment$|^book how many session pay$|^จอง.*กี่ session.*จ่าย$',
  r'จอง.*(?:ได้กี่รอบ|กี่รอบ|กี่\s*session)|(?:how many|maximum).{0,25}sessions?.{0,35}book|book.{0,25}(?:how many|maximum).{0,15}sessions?'),
 ('walk_in','C08',r'walk.in|เดินเข้าไปใช้บริการ',r'walk.in|เดินเข้า.*(?:จอง|บริการ)|ต้องจองก่อนไหม|ต้องจองไหม'),
 ('change_time','C08',r'booking time.*chang|เปลี่ยนเวลาจอง',r'เปลี่ยนเวลาจอง|เปลี่ยนรอบ|change.*booking time|booking time.*chang'),
 ('wrong_machine','C08',r'wrong machine|จองผิดเครื่อง',r'จองผิดเครื่อง|wrong machine'),
 ('membership_requirement','C10',r'membership|member first|สมาชิก',r'\b(?:membership|member(?:ship)? sign.?up)\b|(?:ต้อง|สมัคร|เป็น).{0,15}สมาชิก'),
 ('checkin_documents','C08',r'check.in document|เอกสารตอนเช็คอิน|แสดงหลักฐาน|present.*identification',r'เช็คอิน.*(?:เอกสาร|บัตร)|เช็กอิน.*(?:เอกสาร|บัตร)|แสดงหลักฐาน|check.in.*(?:document|card)|documents.*check.in|\b(?:what|which)\s+(?:id|identification|documents?)\b(?=.{0,120}\b(?:studio|visitor|check.in|arrival|service)\b)|\b(?:id|identification|passport|documents?).{0,35}(?:need|bring|show|present)\b(?=.{0,120}\b(?:studio|visitor|check.in|arrival|service)\b)'),
 ('checkin_advance','C08',r'check.in in advance|เช็คอินล่วงหน้า',r'เช็คอิน.*ล่วงหน้า|เช็กอิน.*ล่วงหน้า|check.in.*(?:early|advance)|how early.*check.in|check.in.*before.*(?:play|use|start)|เช็[คก]อิน.*ก่อน.*(?:เล่น|เริ่ม|ใช้)'),
 ('wrong_slip','C09',r'slip is wrong|สลิปผิดรูป',r'สลิปผิด|แนบ.*สลิป.*ผิด|wrong.*slip|slip.*wrong'),
 ('installation','C10',r'install.*(?:mod|program|game)|ติดตั้งเกม|ติดตั้งโปรแกรม',r'ติดตั้ง.*(?:เอง|ได้ไหม)|ลงเกมเอง|\binstall\b.*(?:myself|software|mod|game)'),
 ('arrival_waiting','C08',r'arrival waiting|รอก่อนเวลา',r'ก่อนเวลา|มาก่อน|ถึงก่อน|รอ(?:ที่ไหน|ตรงไหน)|arrive early|wait.*(?:where|before)|start.*early'),
 ('extend_session','C08',r'extend (?:play )?session|booking extension|ต่อเวลา',r'ต่อเวลา|จองต่อ|เล่นต่อ|extend.*(?:play|session)|session.*extend'),
 ('change_service','C08',r'change service|เปลี่ยนบริการระหว่าง',r'เปลี่ยน.{0,14}(?:เครื่อง|บริการ)|(?:pc|ps5).*(?:ไป|เป็น).*(?:pc|ps5)|change.*(?:service|machine)|switch.*(?:service|machine)'),
 ('correct_booking_name','C08',r'correct booking name|แก้ชื่อ',r'กรอกชื่อผิด|ชื่อผิด|แก้(?:ไข)?ชื่อ.*(?:รายการจอง|จอง)|wrong name|correct.{0,30}name.{0,30}(?:booking|reservation)'),
 ('change_paid_booking','C08',r'change paid booking|แก้รายการจองที่จ่ายแล้ว',r'จองผิดวัน|เปลี่ยนวัน|แก้.*(?:รายการจอง|หลังจอง)|wrong date|change.*(?:paid booking|date)|correct.*(?:paid booking|date)'),
 ('late_notice','C08',r'late arrival notice|ไปไม่ทันรอบ',r'ไปไม่ทัน|มาสาย|ไปสาย|แจ้ง.*ช้า|cannot arrive|late.*(?:arrival|session)|arrive.*(?:late|time)|notify.*studio'),
 ('rain_reschedule','C08',r'rain reschedule|เปลี่ยนรอบเพราะฝน',r'ฝน|heavy rain|rain.*(?:resched|arriv)'),
 ('closure_after_booking','C08',r'studio closes after booking|ศูนย์ปิดหลังจอง',r'ศูนย์ปิด.*จอง|ปิดหลัง.*จอง|studio.*clos.*(?:after|book)|contact me.*clos'),
 ('spectators','C08',r'spectators|นั่งดูเพื่อน',r'นั่งดู|ดูเพื่อน|ไม่เล่น.*ดู|watch.*friend|spectator'),
 ('overpayment','C09',r'overpayment|เงินโอนเกิน',r'โอนเกิน|จ่ายเกิน|เงินเกิน|overpa(?:id|y)|paid too much'),
 ('underpayment','C09',r'underpayment|โอนเพิ่มเมื่อยอดขาด|โอนขาด|ยอด.{0,30}ขาด|underpa(?:id|y)',r'โอนขาด|ยอด.*ขาด|โอนเพิ่ม|additional payment|underpa(?:id|y)|additional.*slip'),
 ('full_payment','C09',r'full payment|จ่ายเต็ม',r'แบ่งจ่าย|มัดจำก่อนใช้|ผ่อน|instalment|deposit instead|pay.*full'),
 ('payment_verification','C09',r'payment verification|ตรวจสลิป',r'ตรวจ.*(?:กี่นาที|สถานะ)|สถานะไม่เปลี่ยน|ตรวจเสร็จ|verification|payment checking|status.*(?:not|change)'),
 ('documents','C09',r'tax invoice and receipt|ใบกำกับภาษี',r'ใบเสร็จ|ใบเสนอราคา|ใบกำกับ|receipt|quotation|tax invoice'),
 ('payer','C09',r'payment sender|ผู้โอนเงิน',r'บัญชี.*เพื่อน|ผู้โอน|คนโอน|payment sender|person paying|named.*booking|payer'),
 ('payment_contact','C09',r'payment problem contact|ปัญหาชำระ',r'ปัญหา.*(?:เงิน|ชำระ)|payment problem|contact.*payment'),
 ('refund','C09',r'^refund$|refund (?:procedure|request|policy)|คืนเงิน',r'คืนเงิน|\brefund\b'),
 ('steam_account','C10',r'Steam account|บัญชี Steam',r'steam.*(?:บัญชี|account)|บัญชี.*steam|own steam|need.*steam'),
 ('logout_data','C10',r'logout and login data|ข้อมูลหลังออกระบบ',r'ออกจากบัญชี|ออกจากระบบ|เก็บ.*(?:ล็อกอิน|login|ข้อมูลผู้เล่น)|login data|keep.*(?:login|data)|logging.*out|logout'),
 ('update_compensation','C10',r'game update compensation|ชดเชยเกมอัปเดต',r'อัปเดต.*(?:เวลา|ห้านาที|5)|update.*(?:minutes|time)|extra.*time.*update'),
 ('game_failure_switch','C10',r'game fails to run change machine|เกมเปิดไม่ได้',r'เกม.*(?:เปิดไม่ได้|เล่นไม่ได้|ใช้งานไม่ได้)|game cannot run|game.*(?:fails|cannot).*run'),
 ('installed_version','C10',r'confirm installed version|ตรวจเวอร์ชัน',r'เช็กเวอร์ชัน|เช็คเวอร์ชัน|เวอร์ชัน.*ถาม|confirm.*version|installed game version'),
 ('network_fault','C10',r'network fault|ระบบเน็ตขัดข้อง',r'อินเทอร์เน็ต|เน็ต.*(?:ขัดข้อง|เสีย)|ระบบขัดข้อง|network|system fault'),
 ('equipment_compensation','C10',r'equipment damage compensation|damage[ _]+responsibility|ชดใช้เครื่องเสีย|รับผิดชอบ.*เสียหาย|เสียหาย.*รับผิดชอบ',r'ความเสียหายอุปกรณ์|เครื่องเสียเอง|ชดใช้|ชดเชย.*(?:พัง|เสียหาย)|(?:พัง|เสียหาย).*ชดเชย|damage.*compensation|(?:compensat|owe|pay|what if).{0,80}damag|damag.{0,80}(?:compensat|owe|pay)|pay compensation|equipment fails|(?:responsib(?:le|ility)|owe|pay).{0,100}(?:wheel|equipment|device).{0,40}(?:breaks?|fails?|damag)|(?:if|ถ้า).{0,50}(?:drop|ทำ.{0,50}ตก).{0,60}(?:fine|penalt|ค่าปรับ|ชดใช้)'),
 ('peripheral_fault','C10',r'faulty peripheral|เปลี่ยนอุปกรณ์เสีย',r'(?:เมาส์|อุปกรณ์ต่อพ่วง).*เสีย|faulty peripheral|replace.*peripheral'),
 ('guardian','C10',r'guardian consent|ผู้ปกครอง',r'ผู้ปกครอง|เซ็นยินยอม|guardian|parental|signed consent'),
 ('capture','C10',r'game capture|แคปภาพเกม',r'แคป|อัดวิดีโอในเกม|ถ่าย.*เกม|screenshots?|in.game.*video|capture'),
 ('streaming','C10',r'game streaming|โซนสตรีม',r'สตรีม|\bstream(?:ing)?\b'),
 ('external_visitor','C10',r'external visitors|บุคคลภายนอก',r'บุคคลภายนอก|คนนอก.*บริการ|external visitor|general studio services|(?:ไม่ใช่|ไม่ได้เป็น).{0,18}นักศึกษา.{0,8}(?:psu|มอ).{0,22}(?:เข้า|เล่น|บริการ)|(?:non[- ]psu|not (?:a |an )?psu student).{0,40}(?:use|play|enter|access)'),
 ('personal_accessories','C10',r'personal accessories|อุปกรณ์เสริมส่วนตัว',r'อุปกรณ์.*(?:ตัวเอง|ส่วนตัว)|(?:เมาส์|คีย์บอร์ด).*มา|own.*(?:accessor|keyboard|mouse)|personal.*accessor'),
 ('food_bring','C10',r'^food_bring$|bring.*food|นำอาหารเข้า',r'(?:นำ|เอา|ถือ).*(?:อาหาร|เครื่องดื่ม).*(?:เข้า|มา)|\bbring\b.{0,40}\b(?:food|drinks?)\b'),
 ('personal_power','C10',r'^personal_power$|personal.*power|ปลั๊กพ่วงส่วนตัว',r'ปลั๊กพ่วง|รางปลั๊ก|(?:own|personal).{0,20}(?:power strip|extension cord)'),
 ('public_holiday','C11',r'public holiday opening|วันหยุดราชการ',r'วันหยุดราชการ|public.holiday|holiday.*announcement'),
 ('out_of_hours_rental','C07',r'out of hours rental|เช่านอกเวลา',r'นอกเวลา|out.of.hours'),
 ('rental_start','C07',r'rental start time|เวลาเริ่มเหมา',r'เลือกเวลาเริ่ม|เริ่มเอง|rental start|own.*start time'),
 ('rental_contact','C07',r'rental contact|ติดต่อเหมา',r'จองเหมา.*(?:ติดต่อ|ช่องทาง)|เช่า.*ติดต่อ|contact.*(?:rental|whole.zone)|venue.*rental'),
 ('rental_terms','C07',r'rental cancellation terms|ยกเลิกเหมา',r'(?:เหมา|rental).*(?:ยกเลิก|คืนเงิน|cancell|refund)|(?:cancell|refund).*rental'),
 ('per_person','C06',r'per person billing|ต่อคนหรือต่อเครื่อง',r'ต่อคนหรือต่อเครื่อง|per person or per machine|hourly.*(?:person|machine)'),
 ('tax_included','C06',r'tax included|ราคารวมภาษี',r'รวมภาษี|include.*tax|prices?.*tax'),
 ('mixed_audience','C06',r'mixed audience players|ผู้เล่นต่างกลุ่ม',r'ต่างกลุ่ม|กลุ่ม.*ต่างกัน|นักศึกษา.*คนนอก|mixed audience|each.*audience|student.*external'),
]

UNRECORDED_FIELDS=r'รหัสผ่าน|รหัสลับ|serial number|เลขซีเรียล|ซื้อจากร้าน|ซื้อเมื่อวัน|เบอร์มือถือส่วนตัว|ที่อยู่บ้าน|เงินเดือน|private (?:phone|email)|personal password|salary|home address|แฟกซ์|fax|tiktok|ทางทิศเหนือ|auto win|เทเลพอร์ตอัตโนมัติ|สร้างด่านใหม่อัตโนมัติ|teleport mode|auto.win|secret.pin'

# The router and reader share these predicate frames. A generic word such as
# "announced" must not bypass a missing-predicate guard via another domain.
PREDICATE_GAPS={
 'C03':[(r'ประกัน|warranty',r'ประกัน|warranty')],
 'C07':[(r'โอที|overtime',r'โอที|overtime')],
 'C08':[(r'รับประกัน.*เครื่องสำรอง|เครื่องสำรอง.*รับประกัน|guarantee.*backup',r'เครื่องสำรอง|backup guarantee'),
        (r'ประวัติบัญชี.*ย้อนหลัง|account.*history.*days',r'ประวัติบัญชี|account history'),
        (r'ชื่อบริษัท.*สิทธิ์|company.*privilege|จองเป็นชื่อบริษัท',r'ชื่อบริษัท|company booking')],
 'C09':[(r'คริปโต|crypto',r'คริปโต|crypto'),(r'เครดิต.*หมดอายุ|credit.*expir',r'หมดอายุเครดิต|credit expiry'),
        (r'คืนเงิน.*ภายใน.*กี่วัน|refund.*within.*days|บัตรเครดิต.*กี่วัน',r'กำหนดเวลาคืนเงิน|refund deadline')],
 'C10':[(r'อายุขั้นต่ำ|ขั้นต่ำ.*(?:กี่ขวบ|กี่ปี)|minimum age',r'อายุขั้นต่ำ|minimum age'),
         (r'ถ่าย.*(?:ใบหน้า|คนอื่น|บุคคล)|film.*(?:people|other customers)',r'ถ่าย.*(?:บุคคล|คนอื่น)|film.*people'),
         (r'ค่าปรับ.*(?:ทุกชนิด|ตายตัว|กี่บาท)|ความเสียหายทุกชนิด',r'ค่าปรับตายตัว|fixed damage fine')],
 'C14':[(r'(?:ข่าว|news).*(?:ระบบสด|\blive\b|real.time)',r'แหล่งข่าวสด|live_news_feed|live news feed'),
        (r'(?:กิจกรรม|งาน|events?).*(?:เปิดรับกี่ทีม|how many teams)',r'รับ.*ทีม|จำนวนทีม|team.*(?:limit|capacity)|how many teams')],
}

def predicate_domain(q):
    # A backup guarantee is an operation policy, not equipment warranty.
    for cat in ['C08','C09','C10','C07','C03','C14']:
        if any(matches(pattern,q) for pattern,_ in PREDICATE_GAPS[cat]):return cat
    return None

def matches(pattern,text):return bool(re.search(pattern,text,re.I))

# Match a requested consumption action, never add a new business permission.
POLICY_INTENTS.append(('food_consumption','C10',r'อาหาร.*เครื่องดื่ม|food.*drinks?',r'(?:อาหาร|เครื่องดื่ม).{0,30}(?:กิน|รับประทาน|บริโภค)|(?:กิน|รับประทาน|บริโภค).{0,20}(?:อาหาร|เครื่องดื่ม)|\b(?:can|may|must)\b.{0,20}\b(?:eat|drink)\b|\b(?:eat|eating)\b.{0,25}\b(?:area|desk|designated)\b'))
