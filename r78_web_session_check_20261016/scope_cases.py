CASES=[]
def add(group,locale,queries,need=(),forbid=(),mode=None,source=None,topic=None):
 for q in queries:CASES.append(dict(group=group,locale=locale,question=q,need=list(need),forbid=list(forbid),expected_mode=mode,expected_source=source,expected_topic=topic))
add('personal_permission','en',[
 'Can I bring my own keyboard?', 'Can I use my own mouse?',
 'May I use personal keyboards and mice?', 'Is my own keyboard allowed?',
 'Could you tell me whether I am allowed to use my personal mouse?',
],['not allowed'],[],source='migrated_owner_claim_personal_keyboard_mouse')
add('personal_permission','th',[
 'เอาคีย์บอร์ดตัวเองมาใช้ได้ไหม','เอาเมาส์ส่วนตัวมาได้มั้ย',
 'คีย์บอร์ดส่วนตัวอนุญาตไหม','ขอถามครับ ใช้เมาส์ของผมได้หรือเปล่า',
 'นำคีย์บอร์ดและเมาส์ส่วนตัวมาใช้ได้ไหม',
],['ไม่อนุญาต'],[],source='migrated_owner_claim_personal_keyboard_mouse')
add('wrong_slip','en',[
 'I uploaded the wrong slip. How do I fix it?',
 'How can I correct an incorrect payment slip image?',
 'My slip image is wrong, what should I do?',
 'I mistakenly attached a slip, how do I correct this?',
],['Facebook','https://www.facebook.com/psuesportsphuket'],[],source='procedure_wrong_slip')
add('wrong_slip','th',[
 'แนบสลิปผิดทำไง','อัปโหลดสลิปผิดรูปต้องแก้ยังไง',
 'ขอวิธีแก้ไขรูปสลิปที่ส่งผิดหน่อย','ส่งสลิปผิดไปแล้วต้องทำอย่างไร',
],['ส่งสลิป','https://www.facebook.com/psuesportsphuket'],[],source='procedure_wrong_slip')
add('wrong_amount','en',['What do I do when I paid the wrong amount for my booking?'],['does not confirm','above or below','Studio page:'],['10 minutes','The booking steps are:'],mode='pipeline:common_unconfirmed',topic='wrong_amount')
add('wrong_amount','th',['จ่ายยอดผิดต้องทำยังไง'],['ยังยืนยัน','เกินหรือขาด','เพจศูนย์'],['795-276244-1'],mode='pipeline:common_unconfirmed',topic='wrong_amount')
add('overpayment','en',['I overpaid for my booking. What should I do?','I paid too much. Can you help?'],['does not confirm','overpayments','Studio page:'],['refund guaranteed','within 10 minutes'],mode='pipeline:common_unconfirmed',topic='overpayment')
add('overpayment','th',['ค่าจองโอนเกินทำยังไง','ถ้าจ่ายเกินไปต้องทำอะไร'],['ยังยืนยัน','โอนเกิน','เพจศูนย์'],['คืนเงินเต็มจำนวน','795-276244-1'],mode='pipeline:common_unconfirmed',topic='overpayment')
add('underpayment','en',['I underpaid for my reservation. What now?'],['does not confirm','underpayments'],['new booking is required'],mode='pipeline:common_unconfirmed',topic='underpayment')
add('underpayment','th',['โอนขาดต้องทำยังไง'],['ยังยืนยัน','โอนขาด'],['ต้องจองใหม่'],mode='pipeline:common_unconfirmed',topic='underpayment')
add('installments','en',['Can I pay in installments?','Are installment payments allowed?'],['does not confirm','installment'],['10 minutes'],mode='pipeline:common_unconfirmed',topic='installments')
add('installments','th',['ผ่อนชำระค่าจองได้ไหม','จ่ายแบบผ่อนได้ไหม'],['ยังยืนยัน','ผ่อนชำระ'],['สามารถผ่อนได้'],mode='pipeline:common_unconfirmed',topic='installments')
add('processing','en',['How long does a bank transfer take to arrive?','How long is payment processing?'],['does not confirm','reach the account'],['10 minutes'],mode='pipeline:common_unconfirmed',topic='transfer_processing')
add('processing','th',['โอนเงินกี่วันถึงบัญชี','เงินโอนเข้าบัญชีใช้เวลากี่วัน'],['ยังยืนยัน','เงินโอนเข้าถึงบัญชี'],['10 นาที'],mode='pipeline:common_unconfirmed',topic='transfer_processing')
add('age','en',['Can an 8 years old child use the studio?','What are the minimum age and guardian requirements?'],['does not confirm','age and guardian'],['children are allowed'],mode='pipeline:common_unconfirmed',topic='age_guardian')
add('age','th',['กฎศูนย์อนุญาตให้เด็กอายุ 8 ปีเข้าไหม','ต้องมีผู้ปกครองไหม'],['ยังยืนยัน','อายุและผู้ปกครอง'],['เด็กเข้าได้ครับ'],mode='pipeline:common_unconfirmed',topic='age_guardian')
add('compound','en',['How do I pay and can I bring my own keyboard?'],['795-276244-1','not allowed'],[],mode='pipeline:common_answer')
add('compound','en',['How do I pay and can I pay in installments?'],['795-276244-1','does not confirm','installment'],[],mode='pipeline:common_partial_answer')
add('compound','th',['จ่ายค่าจองยังไงและแนบสลิปผิดต้องทำไง'],['795-276244-1','ส่งสลิป'],[],mode='pipeline:common_answer')
add('compound','th',['จ่ายค่าจองยังไงและผ่อนชำระได้ไหม'],['795-276244-1','ยังยืนยัน','ผ่อนชำระ'],[],mode='pipeline:common_partial_answer')
add('negative_scope','en',['What model keyboard does the studio provide?','Can I buy my own keyboard here?','Can I bring my own headset?','Can I use my own keyboard at the VALORANT tournament?'],[],[],source='!migrated_owner_claim_personal_keyboard_mouse')
add('negative_scope','th',['ศูนย์มีคีย์บอร์ดรุ่นไหน','เอาหูฟังส่วนตัวมาใช้ได้ไหม','กฎแข่ง valorant เอาคีย์บอร์ดส่วนตัวมาได้ไหม'],[],[],source='!migrated_owner_claim_personal_keyboard_mouse')
add('unknown_extra_object','en',['Can I bring my own keyboard and camera?'],['each item'],[],mode='pipeline:common_clarification')
