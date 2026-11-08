"""Describe retained API results; do not turn keyword checks into semantic accuracy."""
import collections,json,statistics
from pathlib import Path
R=Path(__file__).resolve().parent;A=R/'api02'
def rows(p):return list(map(json.loads,p.open(encoding='utf8')))
def events(value):
 found={}
 def walk(x):
  if isinstance(x,dict):
   if 'transport_ok' in x and 'schema_ok' in x and x.get('id'):found[x['id']]=x
   for v in x.values():walk(v)
  elif isinstance(x,list):
   for v in x:walk(v)
 walk(value);return list(found.values())
allrows={arm:rows(A/arm/'RESULTS.jsonl') for arm in ['base','trained']}
summary={};report=['# R121 — ผลแชท API ก่อน/หลัง adapter','', 'คำถามเดิม 8 ข้อต่อแขน ฐานข้อมูลและ candidate Flow เดียวกัน เปลี่ยนเฉพาะ context adapter ไม่ใช่ Full Test; positive literal checks ไม่ใช่ semantic accuracy และ strict protocol ของ benchmark เดิมต้องอ่านแยก','']
for arm,rs in allrows.items():
 c=collections.Counter();partitions=collections.Counter()
 for row in rs:
  positive=[g for g in row['grades'] if g['positive_literal']];ev=events(row['response'].get('decision_artifact',{}))
  c['requests']+=1;c['http_200']+=row['http_status']==200;c['validation_ok']+=row['response'].get('validation_ok') is True
  c['grades']+=len(row['grades']);c['strict_pass']+=sum(g['passed'] for g in row['grades']);c['positive_grades']+=len(positive);c['positive_pass']+=sum(g['literal_passed'] for g in positive);c['positive_requests']+=bool(positive)
  c['timed_out']+=bool(row['response'].get('timed_out'));c['model_events']+=len(ev);c['transport_ok']+=sum(e['transport_ok'] for e in ev);c['schema_ok']+=sum(e['schema_ok'] for e in ev)
  for e in ev:
   proof=e.get('model_provenance',{})
   if proof:
    c['provenance_verified_events']+=bool(proof.get('base_revision')=='ce0a7416fe82d4404b2b4a253ce3ac095ab1252c' and proof.get('adapter_sha256'))
    if proof.get('stage')=='context':
     c['context_events']+=1;c['adapter_profile_matches']+=proof['adapter_active']==(arm=='trained')
    elif proof.get('stage')=='evidence_selection':
     c['selector_events']+=1;c['selector_adapter_disabled']+=proof['adapter_active'] is False
  for g in row['grades']:
   for name,details in g.get('partitions',{}).items():partitions[name]+=len(details)
 summary[arm]={**dict(c),'failure_partition_occurrences':dict(partitions),'latency_median_sec':statistics.median(x['elapsed_sec'] for x in rs)}
report+=['## ตัวเลขที่วัดได้','', '```json',json.dumps(summary,ensure_ascii=False,indent=2),'```','', '## รายข้อ','']
for b,a in zip(allrows['base'],allrows['trained']):
 assert b['key']==a['key']
 report += ['### '+b['question'],'',f"key: `{b['key']}`; locale: {b['locale']}",'']
 for row in [b,a]:
  ev=events(row['response'].get('decision_artifact',{}));positive=[g for g in row['grades'] if g['positive_literal']]
  report += ['#### '+row['arm'],'',row['response'].get('answer') or '(ไม่มีคำตอบ)', '',f"HTTP {row['http_status']}; {row['elapsed_sec']:.2f} วินาที; positive literal {sum(g['literal_passed'] for g in positive)}/{len(positive)} grades",'', 'แผนและหลักฐาน model transport:', '```json',json.dumps([{'stage':e.get('stage'),'transport_ok':e['transport_ok'],'schema_ok':e['schema_ok'],'reason':e.get('reason'),'error':e.get('error'),'context_focus':e.get('context_focus'),'context_quotes':e.get('context_quotes'),'raw_content':e.get('raw_content'),'model_provenance':e.get('model_provenance')} for e in ev],ensure_ascii=False,indent=2),'```','', 'ผลตรวจ benchmark เดิม:', '```json',json.dumps([{'id':g.get('id'),'passed':g['passed'],'positive_literal':g['positive_literal'],'literal_passed':g['literal_passed'],'literal_errors':g.get('literal_errors'),'partitions':g.get('partitions')} for g in row['grades']],ensure_ascii=False,indent=2),'```','']
(R/'API_COMPARISON.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),'utf8')
(R/'API_PER_REQUEST_TH.md').write_text('\n'.join(report),'utf8')
print(json.dumps(summary,ensure_ascii=False,indent=2))
