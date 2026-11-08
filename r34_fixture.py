import json
from pathlib import Path
W=Path(__file__).parent;R=Path((W/'r34_report_path.txt').read_text().strip())
groups={
'price':[
'จอสอบถามหน่อยครับ กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า PC กับ VR อันไหนพงกว่า',
'PC กับ VR อันไหนแพงกว่า','ขอสอบถามว่า PC กับ VR อันไหนแพงก่วา','PC กับ VR อันไหนพงกว่า',
'ช่วยเทียบ PC กับ VR อันไหนถูกกว่า','PC กับ VR อันไหนถุกกว่า',
'ขอข้อมูลที่ยืนยันได้หน่อย PC และ VR อันไหนแพงกว่า','จอสอบถาม PC กับ VR อันไหนถูกกว่า',
'Which is more expensive, PC or VR?','Which is more expensve, PC or VR?',
'Which is cheaper, PC or VR?','Which is cheeper, PC or VR?',
'Please compare prices for PC and VR','Compare PC and VR service fees',
'ขอเทียบราคา PC กับ VR','ราคา PC กับ VR ต่างกันยังไง'],
'payment':[
'รบกวนเช็กข้อมูลของศนย์ให้หน่อยครับ จ่ายเงินยังไงตอนของ อะ','จ่ายเงินยังไงตอนจอง','จ่ายเงินยังไง',
'ขอทราบว่าชำระเงินอย่างไร','ชำระเงินยังไงตอนของ','ชำระเงินยงไงตอนจอง',
'วิธีจ่ายเงินของศูนย์คืออะไร','จ่ายเงืนยังไงตอนจอง','จ่ายเงินยงไงตอนของ',
'How do I pay for a booking?','How can I pay for the reservation?','What is the payment method?',
'How do I pay by bank transfer?','How do I make a bank transfer for a booking?',
'How do I pay for my reservatoin?','What is the paymnt method?'],
'speech':[
'ช่วยอธิบายให้เข้าใจง่ายหน่อยว่า ขอข้อมูลเรื่องคำพูไดม่เหมาะสม','ขอข้อมูลเรื่องคำพูดไม่เหมาะสม',
'ขอข้อมูลเรื่องคำพูดไดม่เหมาะสม','คำพูไดม่เหมาะสมในศูนย์มีกฎอะไร','คำพุดไม่เหมาะสมมีข้อห้ามอะไร',
'คำพูดไม่เหมาะสสมในศูนย์ทำได้ไหม','ในศูนย์ห้ามพูดจาดูหมิ่นใช่ไหม','ขอกฎเรื่องเสียดสีคนอื่น',
'คำพูดเหมาะสมในศูนย์ควรเป็นยังไง','ถ้าคำพูดไม่เหมาะสมควรทำอย่างไร',
'What are the studio rules about offensive language?','Are insults allowed in the studio?',
'What are the rules on loud noise and insulting speech?','Can I mock other people at the studio?',
'What are the studio rules for offenssive language?','What are the studio rules about inappropriate speech?'],
'competition':[
'ขอสอบถามหน่อยครับ ขออ้างอิงติกา อารีน่าออฟเวเลอร์ ในหัวข้อจำนวยผู้เล่นต่อทีม หน่อย',
'ขออ้างอิงกติกา อารีน่าออฟเวเลอร์ ในหัวข้อจำนวนผู้เล่นต่อทีม',
'อ้างอิงติกา RoV จำนวนผู้เล่นต่อทีม','ขอกติกา RoV จำนวยผู้เล่นต่อทีม',
'กติกา RoV จำนวนผู้เล่นต่อทืม','RoV กติาเรื่องจำนวนผู้เล่นต่อทีม',
'กติกกา RoV จำนววนผู้เล่นต่อทีม','อ้างอิงติกา Arena of Valor จำนวนผู้เล่นต่อทีม',
'อ้างอิงติกา RoV ในหัวข้อจำนวยผู้เล่นต่อทีมและรูปแบบการแข่งขัน',
'กติกา RoV จำนวนผู้เล่นต่อทีมตาม Blueket 2025',
'What do the RoV tournament rules say about team size?','What is the team size in Arena of Valor tournament rules?',
'What do the RoV tournamnet rules say about team size?','What do the RoV tournament rules say about teem size?',
'What do the RoV tournament rules say about team sze?','What do the RoV rules say about number of players per team?']}
cases=[]
for group,qs in groups.items():
 for n,q in enumerate(qs,1):
  locale='th' if any('\u0e00'<=c<='\u0e7f' for c in q) else 'en'
  if group=='price':required=[['PC'],['VR'],['25'],['70'],['190'],['525'],['380'],['1050','1,050']];source=['service_fee'];forbidden=[]
  elif group=='payment':required=[['795-276244-1'],['Siam Commercial Bank','ไทยพาณิชย์'],['สลิป','slip']];source=['payment_bank','rule_payment_bank'];forbidden=['cannot be transferred','ไม่สามารถโอนสิทธิ์']
  elif group=='speech':required=[['ห้าม','must not','Avoid','avoid','prohibited'],['ดูหมิ่น','เสียดสี','insult','mock','sarcastic']];source=['noise_language','noise_language_rule','noise_language'];forbidden=[]
  else:required=[['5v5','5 v 5','5 คน','5 players']];source=['competition_rules_rov_blueket_2025_men'];forbidden=['PSU Phuket CS2','VALORANT 2026','Tekken 8']
  cases.append(dict(id=f'{group}-{n:02}',group=group,question=q,locale=locale,required=required,source=source,forbidden=forbidden))
fixture=dict(cases=cases,oracle='Assistant source-content contract: original fee tables, payment rule, general noise/language rule, RoV Blueket mode 5v5. No claim of roster+substitutes size. Not owner approved.',provisional_cases=['price-13','price-14','price-16','speech-09','speech-10','speech-14','speech-16'])
with (R/'R34_FOUR_GROUP_SOURCE_FIXTURE.json').open('x',encoding='utf-8') as f:json.dump(fixture,f,ensure_ascii=False,indent=2)
print(dict(cases=len(cases),groups=list(groups)))
