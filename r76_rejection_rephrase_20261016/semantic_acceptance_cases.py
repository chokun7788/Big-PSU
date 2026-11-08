"""Pending REAL inference contrast set. Not executed/counted as passed in R74."""
CASES=[]
for lang,queries in [
 ('en',['I attached the incorrect proof of payment. How do I fix it?',
        'I uploaded an incorrect bank transfer image. How do I fix it?',
        'I uploaded the incorrect image of my bank transfer. How do I correct it?']),
 ('th',['แนบหลักฐานชำระเงินผิด ต้องแก้ยังไง',
        'แนบรูปยืนยันการโอนผิดไป ต้องทำอย่างไร',
        'หลักฐานจ่ายเงินที่แนบไปผิดรูป ต้องแก้แบบไหน'])]:
 for q in queries:CASES.append(dict(group='semantic_positive',locale=lang,question=q,need=['facebook.com/psuesportsphuket'],forbid=[],expected_source='procedure_wrong_slip'))
for lang,queries in [
 ('en',['I attached incorrect proof of identity. How do I fix it?',
        'The incorrect payment amount needs correction. What should I do?',
        'What is the correct file format for proof of payment?',
        'I attached incorrect proof of payment for tournament registration. How do I fix it?']),
 ('th',['แนบหลักฐานยืนยันตัวตนผิด ต้องแก้ยังไง',
        'โอนยอดผิดต้องแก้อย่างไร',
        'หลักฐานชำระเงินต้องใช้ไฟล์รูปแบบไหนถึงจะถูกต้อง',
        'แนบหลักฐานชำระเงินสมัครแข่งขันผิด ต้องแก้ยังไง'])]:
 for q in queries:CASES.append(dict(group='semantic_negative_scope_only',locale=lang,question=q,need=[],forbid=[],expected_source='!procedure_wrong_slip'))
