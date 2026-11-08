"""Offline analysis of actual saved HTTP output; never sends chat requests."""
import collections,hashlib,json,statistics,sys
from pathlib import Path
R=Path(__file__).resolve().parent
read=lambda p:json.loads(p.read_text('utf8'))
rows=lambda p:list(map(json.loads,p.open(encoding='utf8')))
def artifacts(x):
 a=x.get('response',{}).get('decision_artifact') or x.get('result',{}).get('decision_artifact') or {}
 if isinstance(a.get('domain_flow'),dict):
  d=a['domain_flow'];return {**d,'understanding':a.get('understanding',{}),'needs':a.get('need_results',[]),'claims':[c for n in a.get('need_results',[]) for c in n.get('claim_packets',[])]}
 out=[]
 def visit(v):
  if isinstance(v,dict):
   if 'needs' in v and 'understanding' in v:out.append(v)
   for c in v.values():visit(c)
  elif isinstance(v,list):
   for c in v:visit(c)
 visit(a)
 return max(out,key=lambda v:len(v.get('claims',[])),default={})
def summary(rs):
 c=collections.Counter();local=collections.defaultdict(collections.Counter);domains=collections.defaultdict(collections.Counter)
 for x in rs:
  gs=x['grades'];positive=[g for g in gs if g['positive_literal']]
  for d in [c,local[x.get('requested_locale',x.get('locale','unknown'))],domains[x.get('domain','unknown')]]:
   d.update(requests=1,grades=len(gs),positive_grades=len(positive),positive_pass=sum(g['literal_passed'] for g in positive),strict_pass=sum(g['passed'] for g in gs),positive_requests=bool(positive),positive_requests_pass=bool(positive) and all(g['literal_passed'] for g in positive))
  for g in gs:
   for k,vs in g.get('partitions',{}).items():c['failure_'+k]+=len(vs)
 times=[x.get('elapsed_sec') for x in rs if x.get('elapsed_sec') is not None]
 return {'counts':dict(c),'locales':{k:dict(v) for k,v in local.items()},'domains':{k:dict(v) for k,v in domains.items()},'latency_sec':{'median':statistics.median(times),'mean':statistics.mean(times),'max':max(times)} if times else None}
def main():
 revision='03' if '--revision03' in sys.argv else '02' if '--revision02' in sys.argv else '01'
 groups={'baseline':R/'baseline01/RESULTS.jsonl','student':R/f'student{revision}/RESULTS.jsonl','development_before':R.parent/'r119_complete_source_audit_20261021/http03/RESULTS.jsonl','development_after':R/f'regression{revision}/RESULTS.jsonl'}
 results={k:rows(p) for k,p in groups.items() if p.exists()}
 out={'revision':revision,'partial':any(not (R/d/'TEST_COMPLETE.json').exists() for d in ['student'+revision,'regression'+revision]),'evaluation_reused_for_development':revision!='01','summaries':{k:summary(v) for k,v in results.items()},'pairs':{}}
 evidence=[]
 for label,before,after in [('evaluation','baseline','student'),('development','development_before','development_after')]:
  if before not in results or after not in results:continue
  bs={x['key']:x for x in results[before]};pairs=[]
  for a in results[after]:
   b=bs[a['key']];assert a['question']==b['question']
   bp=[g for g in b['grades'] if g['positive_literal']];ap=[g for g in a['grades'] if g['positive_literal']]
   assert len(bp)==len(ap)
   pair={'key':a['key'],'question':a['question'],'domain':a.get('domain'),'locale':a.get('requested_locale'),
     'positive_grades':len(ap),'before_positive':sum(g['literal_passed'] for g in bp),'after_positive':sum(g['literal_passed'] for g in ap),
     'answer_changed':b['result']['answer']!=a['result']['answer']}
   pairs.append(pair)
   evidence.append({**pair,'cohort':label,'before_answer':b['result']['answer'],'after_answer':a['result']['answer'],
    'before_artifact':artifacts(b),'after_artifact':artifacts(a),'before_grades':b['grades'],'after_grades':a['grades'],
    'after_sources':a.get('response',{}).get('sources'),'after_error':a.get('error'),'after_http_status':a.get('http_status')})
  out['pairs'][label]={'compared':len(pairs),'positive_improved':[p['key'] for p in pairs if p['after_positive']>p['before_positive']],
    'positive_regressed':[p['key'] for p in pairs if p['after_positive']<p['before_positive']],'rows':pairs}
 (R/'SAVED_COMPARISON.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),'utf8')
 with (R/'PER_REQUEST_COMPARISON.jsonl').open('w',encoding='utf8') as f:
  for e in evidence:f.write(json.dumps(e,ensure_ascii=False)+'\n')
 md=['# คำตอบจริงก่อนและหลัง R120','', 'ผล literal checks เป็นเพียงการตรวจถ้อยคำ ต้องอ่านคำตอบและ source ประกอบ ไม่ใช่เปอร์เซ็นต์ semantic accuracy','']
 for n,e in enumerate(evidence,1):
  a=e['after_artifact'];u=a.get('understanding',{})
  md += [f'## {n}. {e["cohort"]} / {e["key"][:12]}', '',e['question'],'',f'Literal: {e["before_positive"]} → {e["after_positive"]} / {e["positive_grades"]}','','### ก่อน','',e['before_answer'],'','### หลัง','',e['after_answer'],'','### Source / execution evidence','','```json',json.dumps({'status':a.get('status'),'understanding':u,'needs':a.get('needs'),'claims':a.get('claims')},ensure_ascii=False,indent=2),'```','']
 (R/'PER_REQUEST_COMPARISON_TH.md').write_text('\n'.join(md),'utf8')
 print(json.dumps({k:v for k,v in out.items() if k!='pairs'},ensure_ascii=False))
if __name__=='__main__':main()
