"""Independent task contracts. Facts copied from existing source inspection."""
CASES=[]
def add(group,lang,queries,need=(),forbid=(),roles=()):
    for q in queries:CASES.append(dict(group=group,locale=lang,question=q,need=list(need),forbid=list(forbid),roles=list(roles)))
add('method','en',[
 'How do I pay for my booking?',
 'Please answer from verified studio information: How do I pay for my booking? Could you check this for me',
 'What payment method should I use?',
 'I am visiting the studio. Where do I transfer the booking payment?',
 'Which bank account do I use to pay?',
],['795-276244-1','slip'],['maximum of 3'],['payment_method'])
add('method','th',['จ่ายค่าจองยังไง','ขอสอบถามหน่อยครับ ต้องชำระเงินอย่างไร','โอนเงินเข้าบัญชีไหน','ใช้ช่องทางไหนในการจ่ายเงิน'],['795-276244-1','สลิป'],[],['payment_method'])
add('deadline','en',['When must I pay for my booking?','How soon after booking must payment be made?','What is the payment deadline?','If I do not pay within 10 minutes after booking, what happens?'],['10','cancel'],['795-276244-1'],['payment_deadline'])
add('deadline','th',['หลังจองต้องจ่ายภายในกี่นาที','กำหนดชำระเงินคือเมื่อไหร่','ถ้าไม่จ่ายภายใน 10 นาทีหลังจองจะเป็นยังไง'],['10','ยกเลิก'],['795-276244-1'],['payment_deadline'])
add('quota','en',['How many sessions can one booking include?','I need the official answer: How many sessions can one booking include?','What is the maximum number of sessions per booking?','How many slots can I reserve in one reservation?'],['3','booking'],['795-276244-1'],['booking_quota'])
add('quota','th',['จองหนึ่งครั้งได้กี่รอบ','ขอทราบจำนวน session สูงสุดต่อการจองหนึ่งครั้ง','1 การจองเลือกได้กี่ช่วงเวลา'],['3'],['795-276244-1'],['booking_quota'])
add('compound','en',['How do I pay and when is the payment deadline?','How many sessions can one booking include and how do I pay?','How many sessions can I book, how do I pay, and when must I pay?'],['795-276244-1','slip'],[],['payment_method'])
CASES[-3]['need']+=['10'];CASES[-3]['roles']+=['payment_deadline']
CASES[-2]['need']+=['3'];CASES[-2]['roles']+=['booking_quota']
CASES[-1]['need']+=['3','10'];CASES[-1]['roles']+=['booking_quota','payment_deadline']
add('compound','th',['จ่ายช่องทางไหนและต้องจ่ายเมื่อไหร่','จองได้กี่รอบและโอนบัญชีไหน','จองได้กี่รอบ จ่ายยังไง แล้วต้องจ่ายภายในกี่นาที'],['795-276244-1'],[],['payment_method'])
CASES[-3]['need']+=['10'];CASES[-3]['roles']+=['payment_deadline']
CASES[-2]['need']+=['3'];CASES[-2]['roles']+=['booking_quota']
CASES[-1]['need']+=['3','10'];CASES[-1]['roles']+=['booking_quota','payment_deadline']
add('studio_rules','en',['What are the studio rules?','I am planning a visit and would like to know: What are the studio rules? Could you check this for me','Could you explain the center regulations before I visit?'],['designated areas','equipment','noise'],['VALORANT'],['studio_rules'])
add('studio_rules','th',['กฎศูนย์มีอะไรบ้าง','ก่อนมาใช้บริการ ขอทราบกฎระเบียบของศูนย์หน่อยครับ','กฏของสตูดิโอมีอะไรมั่ง'],['พื้นที่','คืนอุปกรณ์','เสียงดัง'],['VALORANT'],['studio_rules'])
add('negative_intent','en',["I do not need bank details; when must I pay for my booking?","When must I pay? Do not show the bank account."],['10'],['795-276244-1'],['payment_deadline'])
add('negative_intent','th',['ไม่เอาเลขบัญชี ขอแค่กำหนดจ่ายเงินภายในกี่นาที'],['10'],['795-276244-1'],['payment_deadline'])
add('rules_scope','en',['What are the CS2 tournament rules?'],['Counter-Strike'],['VALORANT'],[])
add('rules_scope','th',['กฎตอนแข่ง tekken 8 มีอะไรบ้าง'],['TEKKEN'],['VALORANT'],[])
add('quota_scope','en',['How many sessions can I book per day?'],['3','daily limit has not been confirmed'],[],['booking_quota'])
add('unconfirmed','en',['How do I pay for my booking with cash?'],[],['cash is accepted','cash payment is allowed'],[])
add('unconfirmed','th',['จ่ายค่าจองด้วยบัตรเครดิตได้ไหม'],[],['รับบัตรเครดิต','บัตรเครดิตได้ครับ'],[])
# Held-out question families are evaluated after the first implementation.
HOLDOUT=[]
def held(group,lang,q,need,forbid=()):HOLDOUT.append(dict(group=group,locale=lang,question=q,need=need,forbid=list(forbid),roles=[]))
held('method_holdout','en','For my reservation, could you tell me how to make the payment?', ['795-276244-1','slip'])
held('method_holdout','th','รบกวนแจ้งวิธีการชำระค่าจองให้หน่อยได้ไหม', ['795-276244-1'])
held('quota_holdout','en','Is there a cap on the number of sessions in a single booking?', ['3'])
held('quota_holdout','th','การจองแต่ละครั้ง จำกัดจำนวนรอบเท่าไร', ['3'])
held('deadline_holdout','en','How long do I have to complete payment after I reserve?', ['10'])
held('deadline_holdout','th','จองเสร็จแล้วมีเวลาให้โอนเงินนานเท่าไหร่', ['10'])
held('rules_holdout','en','Before using the center, what regulations should visitors follow?', ['designated areas','equipment'])
held('rules_holdout','th','ผู้มาใช้ศูนย์ต้องปฏิบัติตามกฎอะไรบ้าง', ['คืนอุปกรณ์'])
held('compound_holdout','en','For a single reservation, tell me the session cap and the payment method and deadline.', ['3','795-276244-1','10'])
held('negative_scope_holdout','en','What are the payment rules for the VALORANT tournament?', [],['795-276244-1'])
held('other_topic_holdout','en','What does R2 do in eFootball on PS5?', ['Dash'])
held('other_topic_holdout','th','ที่จอดรถอยู่ไหน', ['อาคาร 5'])
