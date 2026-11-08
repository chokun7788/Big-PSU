import json,sys
from pathlib import Path
B=Path(__file__).resolve().parent;T=B/'verification'/sys.argv[1];T.mkdir(parents=True,exist_ok=False)
sys.path.insert(0,str(B/'system'))
from app.knowledge.common.reply_repair import rejection
cases=[
 ('No, I mean how do I pay?','how do I pay?'),
 ('No I meant when must I pay?','when must I pay?'),
 ('Nope. Parking location','Parking location'),
 ('Not that; how many sessions can I book?','how many sessions can I book?'),
 ('None of these: Which games are on PC?','Which games are on PC?'),
 ("No, I'm asking about How do I pay?",'How do I pay?'),
 ('No, I am asking about when must I pay?','when must I pay?'),
 ('No, what I mean is do not show bank details; when must I pay?','do not show bank details; when must I pay?'),
 ('No, I mean PC #01 on 2026-10-16 at 15:00 for 30 minutes','PC #01 on 2026-10-16 at 15:00 for 30 minutes'),
 ('ไม่ใช่ครับ หมายถึงจ่ายค่าจองยังไง','จ่ายค่าจองยังไง'),
 ('ไม่ใช่ค่ะ—หมายถึงต้องจ่ายภายในกี่นาที','ต้องจ่ายภายในกี่นาที'),
 ('ไม่ใช่หมายถึงจองหนึ่งครั้งได้กี่รอบ','จองหนึ่งครั้งได้กี่รอบ'),
 ('ไม่ใช่อันนี้ครับ ขอถามที่จอดรถอยู่ไหน','ที่จอดรถอยู่ไหน'),
 ('ไม่มีในนี้ หมายถึงโอนเกินต้องทำอย่างไร','โอนเกินต้องทำอย่างไร'),
 ('ไม่ใช่ครับ ตอนจองต้องจ่ายภายในกี่นาที','ตอนจองต้องจ่ายภายในกี่นาที'),
 ('ไม่ใช่ครับ หมายถึงไม่เอาเลขบัญชี ขอแค่กำหนดจ่ายเงินภายในกี่นาที','ไม่เอาเลขบัญชี ขอแค่กำหนดจ่ายเงินภายในกี่นาที'),
 ('No, I mean','CANCEL'),('No!','CANCEL'),('ไม่ใช่ครับ','CANCEL'),('ไม่เอา','CANCEL'),
 ('No refund is needed. How do I pay?',None),('No payment has been made yet.',None),
 ('No problem, how do I pay?',None),('ไม่ใช่แค่ราคา อยากรู้เกมด้วย',None),
 ('ไม่เอา เลขบัญชี ขอแค่กำหนดจ่ายเงิน',None),('ไม่เอาเลขบัญชี ขอแค่กำหนดจ่ายเงิน',None),
 ('Yes, but can I pay in installments?',None),('ใช่แต่ถ้าโอนเกินล่ะ',None),
 ('I mean how do I pay?',None),('Notice the correct format.',None),
 ('No I meaningful text',None),('No, I meaningful text','I meaningful text'),
]
rows=[]
for q,expected in cases:
    parsed=rejection(q)
    actual=None if parsed is None else parsed['replacement'] or 'CANCEL'
    rows.append({'question':q,'expected':expected,'actual':actual,'passed':actual==expected})
result={'count':len(rows),'passed':sum(r['passed'] for r in rows),'scope':'raw substring parser, not full answer/model accuracy','cases':rows}
(T/'RESULTS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps({k:v for k,v in result.items() if k!='cases'}));raise SystemExit(any(not r['passed'] for r in rows))
