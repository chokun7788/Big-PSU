import json
from pathlib import Path
R=Path(Path(__file__).with_name('r34_report_path.txt').read_text().strip())
base={c['group']:c for c in json.loads((R/'R34_SOURCE_REVIEWED_FIXTURE.json').read_text(encoding='utf-8'))['cases']}
questions={
'price':[
('ช่วยเทียบค่าบริการ PC และ VR ให้หน่อย อันไหนถูกกว่า','ถูกกว่า','ถุกกว่า'),
('ขอข้อมูลหน่อยครับ PC เทียบกับ VR อันไหนแพงกว่า','แพงกว่า','แพงกว่่า'),
('อยากทราบว่า PC หรือ VR อันไหนถูกกว่า','อันไหนถูกกว่า','อันไหนถุกกว่า'),
('Which package is cheaper between PC and VR at the studio?','cheaper','cheeper'),
('Please tell me which is more expensive between VR and PC','expensive','expenssive'),
('Could you compare service fees for VR and PC?','fees','fees'),
('จอสอบถามนิดหนึ่ง PC กับ VR อันไหนแพงกว่า','แพงกว่า','พงกว่า'),
('Before visiting, which is more expensive, VR or PC?','expensive','expensve'),
],
'payment':[
('อยากทราบวิธีชำระเงินของศูนย์ครับ','ชำระ','ชำร'),
('ถ้าจะชำระเงิน ต้องจ่ายเงินยังไงครับ','จ่ายเงินยังไง','จ่ายเงืนยังไง'),
('ขอเลขบัญชีและวิธีจ่ายเงินหน่อยครับ','วิธีจ่าย','วิธีจ่าย'),
('Please explain the payment method for studio bookings','payment','paymnt'),
('Can you tell me how do I pay for my booking?','booking','bokking'),
('What payment method is used for booking at the studio?','payment','payemnt'),
('พอดีจะใช้บริการ ชำระเงินอย่างไรครับ','อย่างไร','อย่างไ'),
('How can we pay for the reservation at the studio?','reservation','reservatoin'),
],
'speech':[
('มีกฎเรื่องคำพูดไม่เหมาะสมตอนใช้ศูนย์ยังไงครับ','คำพูดไม่','คำพูไดม่'),
('ถ้าพูดจาดูหมิ่นคนอื่นในศูนย์ มีกฎอย่างไร','ดูหมิ่น','ดูหมื่น'),
('ขอข้อห้ามเรื่องคำพูดไม่เหมาะสมหน่อยครับ','คำพูดไม่','คำพูดไดม่'),
('Are insults permitted when using the studio?','insults','insullts'),
('Please explain the studio policy on offensive language','offensive','offenssive'),
('Is mocking other people allowed in the studio?','mocking','mocking'),
('คำพูดเหมาะสมเวลาอยู่ในศูนย์ต้องเป็นยังไงครับ','เหมาะสม','เหมาะสสม'),
('Does the studio prohibit insulting speech?','insulting','insultng'),
],
'competition':[
('ช่วยอ้างอิงกติกา อารีน่าออฟเวเลอร์ หัวข้อจำนวนผู้เล่นต่อทีมให้หน่อยครับ','กติกา','ติกา'),
('ขออ้างอิงกติกา RoV ในหัวข้อจำนวนผู้เล่นต่อทีมครับ','จำนวน','จำนวย'),
('ตามกติกา RoV จำนวนผู้เล่นต่อทีมเป็นเท่าไหร่','ต่อทีม','ต่อทืม'),
('Please cite RoV tournament rules for team size','tournament','tournamnet'),
('Could you explain team size under Arena of Valor rules?','team size','teem size'),
('อ้างอิงกติกา RoV เรื่องจำนวนผู้เล่นต่อทีมหน่อย','กติกา','ติกา'),
('For RoV, what is the number of players per team in the rules?','players','playres'),
('ขออ้างอิงกติกา อารีน่าออฟเวเลอร์ ในหัวข้อจำนวนผู้เล่นต่อทีมและรูปแบบการแข่งขัน','กติกา','ติกา'),
]}
cases=[]
for group,qs in questions.items():
 for i,(q,term,typo) in enumerate(qs,1):
  for variant,question in [('clean',q),('noisy',q.replace(term,typo,1))]:
   if variant=='noisy' and term==typo:continue
   c={**base[group], 'id':f'novel-{group}-{i:02}-{variant}', 'question':question,'locale':'th' if any('\u0e00'<=x<='\u0e7f' for x in question) else 'en','pair_variant':variant}
   cases.append(c)
with (R/'R34_NOVEL_SOURCE_FIXTURE.json').open('x',encoding='utf-8') as f:json.dump(dict(cases=cases,scope='New wording authored after rounds A-D; first E evaluation is a holdout. If used for fixes thereafter, it becomes regression evidence. Not owner approved.'),f,ensure_ascii=False,indent=2)
print({'novel_cases':len(cases)})
