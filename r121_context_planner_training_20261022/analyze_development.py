"""Posthoc integration evidence. These are development/regression results."""
import collections,hashlib,json,statistics
from pathlib import Path
R=Path(__file__).resolve().parent
def rows(p):return list(map(json.loads,p.open(encoding='utf8')))
def read(p):return json.loads(p.read_text('utf8'))
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
allsets={name:rows(R/name/'trained/RESULTS.jsonl') for name in ['api02','guard01','priority01','reader01']}
summary={};doc=['# R121 — ตรวจการเชื่อม Flow หลังวิเคราะห์ข้อผิดพลาด','', '**เป็น posthoc development/regression ไม่ใช่ fresh held-out accuracy** ใช้ adapter เดิมตลอด ไม่มีการฝึกเพิ่มหรือเพิ่มคำถามใหม่ การวัด 30 ข้อของโมเดลยังเก็บแยกตามเดิม','']
for name,rs in allsets.items():
 assert read(R/name/'TEST_COMPLETE.json')['complete']
 frozen=read(R/name/'RUN_FREEZE.json');assert all(sha(p)==h for p,h in frozen.items()),('frozen run changed',name)
 positive=[g for x in rs for g in x['grades'] if g['positive_literal']]
 summary[name]={'requests':len(rs),'http_200':sum(x['http_status']==200 for x in rs),'positive_literal_pass':sum(g['literal_passed'] for g in positive),'positive_literal_grades':len(positive),'positive_literal_requests':sum(any(g['positive_literal'] for g in x['grades']) for x in rs),'latency_median_sec':statistics.median(x['elapsed_sec'] for x in rs),'new_questions':0,'fresh_heldout':False,'frozen_source_unchanged':True}
 if name=='guard01':
  p8=[g for x in rs[:8] for g in x['grades'] if g['positive_literal']]
  summary[name]['same_original_8_questions']={'positive_pass':sum(g['literal_passed'] for g in p8),'positive_grades':len(p8)}
 doc+=['## '+name,'', '```json',json.dumps(summary[name],ensure_ascii=False,indent=2),'```','']
 for x in rs:
  artifact=x['response'].get('decision_artifact') or {};u=artifact.get('understanding') or {}
  needs=[{k:n.get(k) for k in ['category','status','reason_codes','execution_query']} for n in artifact.get('need_results',[])]
  event=u.get('event') or {}
  doc+=['### '+x['question'],'',x['response'].get('answer') or '(ไม่มีคำตอบ)','',f"key `{x['key']}`; HTTP {x['http_status']}; {x['elapsed_sec']:.3f} วินาที",'', '```json',json.dumps({'understanding_accepted':u.get('accepted'),'tasks':u.get('tasks'),'source_quote_repairs':event.get('source_quote_repairs'),'independent_subtask_reviews':event.get('independent_subtask_reviews'),'meaning_review':event.get('meaning_review'),'needs':needs,'literal_grades':[{'id':g['id'],'literal_passed':g['literal_passed'],'literal_errors':g.get('literal_errors')} for g in x['grades'] if g['positive_literal']]},ensure_ascii=False,indent=2),'```','']
(R/'DEVELOPMENT_COMPARISON.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),'utf8')
(R/'DEVELOPMENT_PER_REQUEST_TH.md').write_text('\n'.join(doc),'utf8')
print(json.dumps(summary,ensure_ascii=False,indent=2))
