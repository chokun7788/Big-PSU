"""Read-only citation review of saved answers; not a rerun or new evaluation score."""
import collections
import html
import json
import re
import sqlite3
from pathlib import Path
from inventory_saved_claims import observed

P = Path(__file__).resolve().parent
ROOT = P.parent
EVAL = ROOT/'r135_bounded_eval200_20261111/evaluation'
registry = json.loads((ROOT/'r135_bounded_response_20261111/system/data/knowledge/verified_web_citations.json').read_text(encoding='utf-8'))['entries']
review = {(r['record_id'],r['field']):r for r in json.loads((P/'CLAIM_CITATION_REVIEW.json').read_text(encoding='utf-8'))}
rows = list(map(json.loads,(EVAL/'RESULTS.jsonl').open(encoding='utf-8')))
db = sqlite3.connect((EVAL/'runtime/logs/transcripts.sqlite').resolve().as_uri()+'?mode=ro',uri=True)
out=[]
for row in rows:
 message=db.execute('SELECT metadata_json FROM chat_messages WHERE session_id=? AND role=? ORDER BY id DESC LIMIT 1',(row['session_id'],'assistant')).fetchone()
 artifact=json.loads(message[0]).get('decision_artifact',{}) if message else {}
 claims=observed(artifact,row.get('locale','th'))
 items=[]
 for claim in claims:
  disposition=review[(claim['record_id'],claim['facet'])]
  links=[]
  if claim['value'] in disposition.get('corroborated_values',[]):
   links=[{'url':e['url'],'section':e['section'],'access':e['access']} for e in registry if e['record_id']==claim['record_id'] and e['field']==claim['facet']]
  items.append({'record_id':claim['record_id'],'field':claim['facet'],'claim':claim['value'],
                'status':'corroborated' if links else ('not_verified_variant' if disposition['citation_review']=='partially_corroborated_variants' else disposition['citation_review']),'reason':disposition['reason'],'links':links})
 out.append({'key':row['key'],'question':row['question'],'mode':row['response'].get('mode'),
             'saved_answer':row['response'].get('answer',''),'claim_review':items,
             'scope':'Saved typed claims and known native text fields; empty list is unassessed, not verified.'})
db.close()
(P/'QUESTION_CITATION_REVIEW.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
esc=lambda x:html.escape(str(x))
parts=['<!doctype html><meta charset="utf-8"><title>ตรวจอ้างอิง 200 คำถาม</title><style>body{font:16px sans-serif;margin:24px}table{width:100%;border-collapse:collapse}td,th{border:1px solid #ccc;padding:12px;vertical-align:top}pre{white-space:pre-wrap;overflow-wrap:anywhere}.ok{color:#086b38}.no{color:#835413}</style>',
 '<h1>ตรวจอ้างอิงจากคำตอบเดิม 200 ข้อ</h1><p>อ่านผลที่บันทึกไว้ ไม่ได้รันโมเดลใหม่ ไม่ใช่คะแนนความถูกต้อง คอลัมน์คำตอบเป็นฉบับเดิม (ซ่อนเครื่องหมายอ้างอิงภายในเดิม) ลิงก์ด้านขวารองรับเฉพาะข้อความที่ระบุ ไม่ใช่ทั้งคำตอบ การเปิดเผยแพร่และวันมีผลยังไม่รับรอง</p>',
 '<p>ไม่พบลิงก์ที่ตรวจผ่าน ≠ ข้อมูลนั้นเป็นเท็จ กรณีเว็บเข้าไม่ได้หรือภาพ/เอกสารแนบยังไม่ตรวจ แสดงสถานะค้าง ไม่อ้างว่าเว็บไม่มีข้อมูล</p>',
 '<table><tr><th>คำถาม</th><th>คำตอบที่วัดไว้เดิม</th><th>หลักฐานที่ตรวจได้ / ข้อจำกัด</th></tr>']
for i,row in enumerate(out,1):
 details=[]
 for claim in row['claim_review']:
  links=' '.join('<a href="'+esc(e['url'])+'">'+esc(e['section'])+'</a> ('+esc(e['access'])+')' for e in claim['links'])
  details.append('<p class="'+('ok' if links else 'no')+'"><b>'+esc(claim['status'])+'</b>: '+esc(claim['claim'])+'<br>'+links+'<br>'+esc(claim['reason'])+'</p>')
 if not details:details=['ยังไม่ได้ประเมินอ้างอิงราย claim: ไม่มี typed claim ใน trace ชุดนี้; ไม่ใช่ผลว่าเว็บไม่มีข้อมูล']
 parts.append('<tr><td>'+str(i)+'. '+esc(row['question'])+'<br>'+esc(row['mode'])+'</td><td><pre>'+esc(re.sub(r'\[S\d+\]','',row['saved_answer']))+'</pre></td><td>'+''.join(details)+'</td></tr>')
parts.append('</table>')
(P/'CITATION_REVIEW_200.html').write_text(''.join(parts),encoding='utf-8')
summary={'questions':len(out),'with_observed_claims':sum(bool(x['claim_review']) for x in out),
         'with_at_least_one_corroborated_claim':sum(any(c['links'] for c in x['claim_review']) for x in out),
         'without_observed_claims_unassessed':sum(not x['claim_review'] for x in out),
         'whole_answer_semantic_acceptance':False}
(P/'QUESTION_REVIEW_SUMMARY.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print(json.dumps(summary))
