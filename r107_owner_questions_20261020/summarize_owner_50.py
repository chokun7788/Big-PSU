"""Read saved questionnaire responses; list only remaining parts for follow-up."""
import collections,hashlib,json,urllib.request
from pathlib import Path
R=Path(__file__).resolve().parent;O=R/'owner_update_50'
url=json.loads((R/'session.json').read_text('utf8'))['url']
with urllib.request.urlopen(url+'api/state',timeout=10) as response:live=json.load(response)
questions=live['questions']['questions'];answers=live['answers']['answers'];ledger=json.loads((O/'SOURCE_OWNER_50.json').read_text('utf8'));payload=json.loads((O/'PREFILL_PAYLOAD.json').read_text('utf8'))
resolved={'answered','no_policy','not_applicable'};remaining=[];counts=collections.Counter();sections={}
for q in questions:
 a=answers.get(q['id'],{});status=a.get('status','unanswered');counts[status]+=1
 sec=sections.setdefault(q['section'],collections.Counter());sec['total']+=1;sec['resolved']+=status in resolved;sec['partial']+=status=='partial';sec['pending']+=status not in resolved
 if status not in resolved:remaining.append({'id':q['id'],'section':q['section'],'category':q['category'],'title':q['title'],'question':a.get('remaining_question') if status=='partial' else q['question'],'known_answer':a.get('text',''),'status':status,'source_items':a.get('source_items',[])})
assert len(questions)==302 and len(remaining)==297
assert counts['answered']==5 and counts['partial']==31 and counts['unanswered']==266
assert all(answers[id]['text']==a['text'] and answers[id]['remaining_question']==a['remaining_question'] for id,a in payload['answers'].items())
assert 'เอามาใช้ได้ แต่ต้องแจ้ง' in answers['Q044']['text']
assert answers['Q033']['status']=='partial' and 'สถานที่/บุคคล' in answers['Q033']['remaining_question']
assert answers['Q031']['status']=='partial' and not answers['Q031']['effective_from']
assert 'เกินกว่า 5 นาที' in answers['Q025']['text']
assert all(not a.get('effective_from') and not a.get('effective_until') for a in answers.values())
db=R.parent/'r106_complete_flow_20261020/system/data/knowledge/common.sqlite';unchanged=hashlib.sha256(db.read_bytes()).hexdigest()==live['questions']['source_database_sha256'];assert unchanged
summary={'source_items':50,'substantive_source_items':46,'source_items_without_substantive_answer':[8,11,20,47],'matched_questions':len(payload['answers']),'total_questions':len(questions),'fully_answered':counts['answered'],'partially_answered':counts['partial'],'untouched':counts['unanswered'],'remaining_questions_including_partial':len(remaining),'by_section':sections,'source_database_unchanged':unchanged,'production_applied':False,'questionnaire_url':url,'meaning':'remaining includes partially answered questions; it does not mean all these topics lack every fact'}
(O/'SUMMARY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),'utf8');(O/'REMAINING_QUESTIONS.json').write_text(json.dumps(remaining,ensure_ascii=False,indent=2),'utf8')
md=['# คำถามที่ยังต้องตอบหลังเติมชุด 50 ข้อ','',f'เดิม 302 ข้อ: ตอบครบ 5 ข้อ เติมบางส่วน 31 ข้อ ยังไม่มีคำตอบเฉพาะข้อ 266 ข้อ รวมเหลือ 297 ข้อที่ต้องเติม (รวม 31 ข้อที่มีคำตอบแล้วบางส่วน)','', 'จำนวนค้างยังมากเพราะรายการเดิมรวมการรับรองราคาทั้งตาราง/กติกาทีละข้อ/ข้อมูลเสริม คำตอบ 50 ข้อมีหลายเรื่องที่ยืนยันไว้แล้ว ไม่ได้ถูกละเลย','', 'ข้อที่ปิดได้: Q002 ไม่ให้สลับ 4 คนในบริการ 2 คน, Q006 แยกจองผิดวันกับเลื่อนแทนคืนเงิน, Q007 ใช้ขั้นตอนเปลี่ยนเวลาตามคำตอบล่าสุด, Q012 เบอร์ผิดไม่ต้องจองใหม่แต่อีเมลต้องถูก, Q024 ไม่ให้ผู้ใช้ติดตั้งเองแต่ขอพิจารณาเพิ่มเกมได้','', 'บันทึกการแก้ข้อมูลเดิม: คีย์บอร์ด/เมาส์ส่วนตัวใช้ได้แต่ต้องแจ้ง (คำตอบล่าสุด) เฉพาะการใช้ศูนย์ทั่วไป ไม่แทนกฎแข่งขัน','', 'Capture ภาพ/วิดีโอในเกมได้และให้ลบหลังเสร็จ ยังไม่ใช่อนุญาตถ่ายบุคคล/สถานที่; สตรีมได้แต่เงื่อนไขยังขาด; อัปเดตทุกจันทร์เช้าไม่ใช่การรับรองเวอร์ชันสด; เด็กยังไม่มีอายุขั้นต่ำที่ยืนยัน','']
for sec,v in sections.items():
 md+=['## '+sec,f"ค้าง {v['pending']} ข้อ (ตอบแล้วบางส่วน {v['partial']} ข้อ)",'']
 for q in remaining:
  if q['section']!=sec:continue
  md+=['### '+q['id']+' — '+q['title'],'']
  if q['known_answer']:md+=['**ตอบไว้แล้ว:** '+q['known_answer'],'','**ขอเฉพาะส่วนที่ยังขาด:**']
  md+=[q['question'],'','คำตอบเพิ่มเติม: __________','']
(R/'REMAINING_QUESTIONS_TH.md').write_text('\n'.join(md),'utf8')
mapping=['# การจับคู่คำตอบจากแชทเข้ากับ 302 ข้อ','', '| รหัส | หัวข้อ | ผล | ข้ออ้างอิงจากชุด 50 |','|---|---|---|---|']
for id,a in payload['answers'].items():mapping.append('| '+id+' | '+next(q['title'] for q in questions if q['id']==id)+' | '+('ครบ' if a['status']=='answered' else 'บางส่วน')+' | '+', '.join(map(str,a['source_items']))+' |')
(O/'MATCHING_REPORT_TH.md').write_text('\n'.join(mapping),'utf8')
print(json.dumps(summary,ensure_ascii=False,indent=2))
