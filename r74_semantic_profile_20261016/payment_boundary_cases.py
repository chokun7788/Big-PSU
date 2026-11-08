"""Destination/method versus arrival time, same source and frozen test clock."""
CASES=[]
for lang,queries,word in [
 ('th',['โอนเงินเข้าบัญชีไหน','โอนเงินเข้าบัญชีอะไร','ต้องโอนเข้าธนาคารไหน','เลขบัญชีสำหรับโอนค่าจองคืออะไร'], 'สลิป'),
 ('en',['Which bank account do I use to pay?','Where do I transfer the booking payment?'], 'slip')]:
 for q in queries:CASES.append(dict(group='account_destination',locale=lang,question=q,need=['795-276244-1',word],forbid=['does not confirm','ระยะเวลาที่เงินโอนเข้าถึงบัญชี'],expected_sources_any=['migrated_faq_rule_payment_bank','migrated_faq_rule_en_payment_method_natural']))
for lang,queries in [
 ('th',['โอนเงินกี่วันถึงบัญชี','โอนแล้วเงินจะเข้าบัญชีเมื่อไหร่','โอนเงินแล้วแต่ยังไม่เข้าบัญชีทำไง','เงินโอนเข้าบัญชีนานไหม']),
 ('en',['How long does the payment transfer take to arrive?','How long is payment processing?'])]:
 for q in queries:CASES.append(dict(group='arrival_time',locale=lang,question=q,need=['ยังยืนยัน' if lang=='th' else 'does not confirm'],forbid=['795-276244-1'],expected_topic='transfer_processing'))
for lang,q in [('th','หลังจองต้องจ่ายภายในกี่นาที'),('en','When must I pay for my booking?')]:
 CASES.append(dict(group='payment_deadline',locale=lang,question=q,need=['10'],forbid=['795-276244-1','transfer takes'],expected_source='migrated_faq_rule_payment_10_minutes'))
