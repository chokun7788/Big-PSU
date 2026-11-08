"""Explain retained answers without executing a chatbot or model."""
import json,sqlite3,sys
from pathlib import Path
B=Path(__file__).resolve().parent;N=B/'r88_full_common_llm_20261017';R=B/'r90_full_flow_analysis_20261018'
sys.path.insert(0,str(N))
from analyze import rows
specs=[
 ('K01','ชื่อเกมถูก แต่คำถามว่าเป็นเกมอะไรพิมพ์ผิด',lambda q:'คือกมอะๆร' in q and 'Zelda' in q),
 ('K03','ถามสิทธิ์คนนอกใช้ VR กลับได้เมนูเวลาเล่น',lambda q:q=='A question about the studio: Can an external visitor use the VR headset?'),
 ('K04','ถามนโยบาย Maintenance แต่แผนเลือกช่องคำถาม',lambda q:q=='What is the studio policy for friday maintenance'),
 ('K05','คำถามผสมราคาและวิธีจองที่พิมพ์ขาด',lambda q:q=='How much does it cost for a general visiror to play Cockpit for 30 minutes and how do I boo'),
 ('K06','กติกา Tekken อังกฤษ: เนื้อหากับสำนวนตัวตรวจ',lambda q:q=='Hello, could you help? What conduct and etiquette do Tekken 8 tournament players follow?'),
 ('K07','ถามโซนของเกม กลับได้รายการบริการ',lambda q:q=='Please answer from verified studio information: Which studio zone has The Legend of Zelda: Breath of the Wild'),
 ('K08','ราคาที่หมดอายุ: ไม่ตอบตัวเลขปัจจุบันอาจเป็นการป้องกันที่ถูกต้อง',lambda q:q=='General Student เล่น VR 30 นาที 3 ชั่วโมง เสียกี่บาท'),
 ('K09','อาหาร: หยุดที่ watchdog ก่อนมีคำตอบ',lambda q:q=='เอาอาหารเข้าได้ไหม'),
 ('K10','ปุ่มยิง: ถามเพิ่มเหมือนกัน แต่ไม่ตรงคำที่ตัวตรวจบังคับ',lambda q:q=='ปุ่มยิงกดอะไร'),
]
selected={}
for file,line,row in rows(N/'full01'):
 for ident,title,pred in specs:
  if ident not in selected and pred(row['question']):selected[ident]={'id':ident,'title':title,'raw_file':str(file),'raw_line':line,'new':row}
assert len(selected)==len(specs),(len(selected),[s[0] for s in specs if s[0] not in selected])
old=sqlite3.connect((B/'r65_detailed_failure_analysis_20261014/evidence.sqlite').resolve().as_uri()+'?mode=ro',uri=True)
for x in selected.values():
 key=x['new']['key'];r=old.execute("SELECT question,answer,exception,mode,category,intent,confidence,elapsed,source_file,source_line FROM results WHERE arm='legacy_llm' AND key=?",(key,)).fetchone()
 x['old']=dict(zip(['question','answer','exception','mode','category','intent','confidence','elapsed','source_file','source_line'],r)) if r else None
 x['old_failed_grades']=[json.loads(v) for v, in old.execute("SELECT grade_json FROM grades WHERE arm='legacy_llm' AND key=? AND passed=0",(key,))]
old.close()
sessions=[json.loads(l) for l in (N/'SESSION_TURNS.jsonl').read_text('utf8').splitlines() if l]
sf=[r for r in sessions if r['session_id'] in ['SF-006','SF006']];assert len(sf)==2,len(sf)
selected['K02']={'id':'K02','title':'ถาม PC แล้วตอบสั้น ๆ ว่าอุปกรณ์: state มาถึง แต่ task ยังถูกปฏิเสธ','session_turns':sf}
with (R/'CASE_EVIDENCE.json').open('x',encoding='utf8') as f:json.dump(selected,f,ensure_ascii=False,indent=2)
print(json.dumps({k:{'question':v.get('new',{}).get('question'),'key':v.get('new',{}).get('key'),'session_turns':len(v.get('session_turns',[]))} for k,v in selected.items()},ensure_ascii=False))
