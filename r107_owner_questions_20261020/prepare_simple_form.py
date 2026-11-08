"""Group repeated owner confirmations; preserve detailed questions and answers."""
import json,shutil,urllib.request
from pathlib import Path
R=Path(__file__).resolve().parent
with urllib.request.urlopen('http://127.0.0.1:8120/api/state',timeout=5) as r:live=json.load(r)
qs=live['questions']['questions'];byid={q['id']:q for q in qs};answers=live['answers']['answers'];out=[]
backup=R/'before_simple_form';backup.mkdir(exist_ok=True)
for f in ['index.html','app.js','style.css','server.py']:
 if not (backup/f).exists():shutil.copy2(R/f,backup/f)
(backup/'STATE_SNAPSHOT.json').write_text(json.dumps(live['answers'],ensure_ascii=False,indent=2),'utf8')
for q in qs:
 a=answers.get(q['id'],{})
 if q['section']!='คำถามนโยบาย' or a.get('status') in ['answered','no_policy','not_applicable']:continue
 out.append({'id':q['id'],'title':q['title'],'question':a.get('remaining_question') or q['question'],'original_question_ids':[q['id']],'known_answer':a.get('text','')})
def group(id,title,question,ids):
 if ids:out.append({'id':id,'title':title,'question':question,'original_question_ids':ids,'known_answer':''})
group('group_rates','ตารางราคาปัจจุบัน','ราคา PC, PS5, Nintendo Switch, Cockpit และ VR ในตารางเดิมยังใช้อยู่หรือไม่? ขอวันเริ่มใช้และวันสิ้นสุด (ถ้าไม่กำหนดให้บอกว่าไม่กำหนด) ถ้ามีเฉพาะบางรายการเปลี่ยน ให้ระบุเฉพาะรายการและราคาใหม่', [q['id'] for q in qs if q['category']=='rates'])
group('group_packages','ราคาแพ็กเกจเหมา','ราคาเหมาครึ่งวัน/เต็มวันในตารางที่เคยส่งยังใช้อยู่หรือไม่ และเริ่มใช้/สิ้นสุดเมื่อไร? ถ้าราคาใดเปลี่ยนให้ระบุเฉพาะรายการนั้น เงื่อนไขชั่วโมง/สิ่งที่รวมในแพ็กเกจตอบในคำถามเหมาก่อนหน้าได้ ไม่ต้องพิมพ์ซ้ำ',[q['id'] for q in qs if q['category']=='packages'])
for q in qs:
 if not q['id'].startswith('book:') or q['id'].count(':')!=1:continue
 rid=q['record_ids'][0];ids=[q['id']]+[x['id'] for x in qs if x['id'].startswith(q['id']+':')]
 ids += [x['id'] for x in qs if x['category']=='rules' and any(e['field']=='competition_id' and e['value']==rid for e in x.get('evidence',[]))]
 # Rule cards carry only text/heading evidence: match their actual field from frozen records.
 import sqlite3
 db=R.parent/'r106_complete_flow_20261020/system/data/knowledge/common.sqlite'
 c=sqlite3.connect(db.resolve().as_uri()+'?mode=ro',uri=True)
 for key,payload in c.execute('select h.record_id,r.payload from cc_heads h join cc_revisions r on h.record_id=r.record_id and h.head=r.version where h.kind=? and h.withdrawn=0',('competition_rule',)):
  rec=json.loads(payload)
  if rec['fields']['competition_id'].get('value')==rid:ids.append('rule:'+key)
 c.close()
 question='ขอเอกสารกติกาฉบับเต็มที่ให้ใช้สำหรับ '+q['title']+' (ส่งลิงก์ หรือบอกชื่อไฟล์ที่จะส่งในแชทได้) ระบุฉบับ/วันที่/ขอบเขตที่ใช้ หรือบอกว่าเป็นข้อมูลประวัติแล้ว หากมีอายุขั้นต่ำ ค่าสมัคร หรือกฎพฤติกรรมเพิ่มเติม ขอข้อความหรือเลขข้อที่เกี่ยวข้อง ไม่ต้องตรวจยืนยันทีละข้อในเว็บนี้'
 if 'tekken' in rid:
  ids+=['special:1'];question+=' และช่วยระบุว่ากฎห้าม Pause กับกฎ Pause เมื่อยินยอมใช้ต่างกันอย่างไร โทษ “1 รอบ” หมายถึง Round, Game หรือ Match'
 if 'rov' in rid:
  ids+=['special:2'];question+=' โดยเฉพาะข้อ 6.1.5 และ 6.1.5.1 ที่ข้อความท้ายยังขาด ขอหน้าที่มีข้อความต่อครบ'
 group(q['id'],q['title'],question,list(dict.fromkeys(ids)))
group('group_people','ชื่อและตำแหน่งบุคลากร','ชื่อและตำแหน่งบุคลากรในชุดเดิมให้แชทแสดงได้ทั้งหมดหรือไม่? ถ้ามีคนที่ไม่ให้แสดงหรือข้อมูลเปลี่ยน ให้ระบุเฉพาะคนนั้น ชื่ออังกฤษถ้าไม่มี spelling ทางการให้ตอบว่าคงชื่อไทยได้',[q['id'] for q in qs if q['category']=='people'])
group('group_controls','ผังปุ่มที่ใช้จริง','ผังปุ่มเกมเดิมตรงกับเครื่องที่ศูนย์ใช้หรือมีเกมใดเปลี่ยน preset/ปุ่ม? ขอรูปหรือไฟล์เฉพาะเกมที่เปลี่ยน/ยังไม่มี โดยเฉพาะ Delta Force, Pokémon Champions และ Overcooked ที่ข้อมูลสองชุดไม่ตรงกัน ถ้ายังไม่ได้ตรวจสามารถตอบว่ายังไม่ทราบ ไม่ต้องยืนยันทุกเกมทีละรายการ',[q['id'] for q in qs if q['category']=='controls']+['special:3','special:6'])
group('group_inventory','รายการเกมและอุปกรณ์ที่เปลี่ยน','นอกจากรายชื่อเกมเล่นสองคนที่เพิ่งให้มา มีเกม/เครื่อง/อุปกรณ์ใดเพิ่ม ถอน หรือเปลี่ยนจากรายการเดิมไหม? ถ้ามีขอเฉพาะรายการที่เปลี่ยน พร้อมแหล่งรายการล่าสุดและวันที่ตรวจ ถ้ายังไม่ได้ตรวจให้บอกว่ายังไม่ได้ตรวจ',[q['id'] for q in qs if q['category']=='inventory'])
assert len({q['id'] for q in out})==len(out)
covered={id for q in out for id in q['original_question_ids']}
pending={q['id'] for q in qs if answers.get(q['id'],{}).get('status') not in ['answered','no_policy','not_applicable']}
assert pending-covered=={'special:4','special:5'}
result={'schema_version':'psu-simple-owner-form-1','questions':out,'count':len(out),'covers_original_pending_questions':len(covered),'technical_items_not_asked':['special:4','special:5'],'note':'รวมรายการตรวจซ้ำเป็นคำถามเดียว ช่องคำตอบว่างคือยังไม่ตอบ คำตอบเดิมเก็บไว้แยก'}
(R/'simple_questions.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),'utf8')
print(json.dumps({'simple_questions':len(out),'covered_old_questions':len(covered),'technical_alias_questions_omitted':2},ensure_ascii=False))
