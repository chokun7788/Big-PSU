import collections,json,math
from pathlib import Path
B=Path(__file__).resolve().parent
def partition(s):
 if s.startswith(('route:','route expected','outcome expected','intent:','legacy_mode_prefix:','status:','forbidden_category','route_mismatch','outcome_mismatch','wrong_category','wrong_intent','mode_mismatch')):return 'protocol_outcome'
 if any(x in s for x in ['source','document_id','chunk','evidence','rulebook target']):return 'source_alignment'
 if 'first_line' in s or 'heading' in s:return 'presentation'
 if 'latency' in s or 'timeout' in s:return 'performance'
 if 'english_thai_prose' in s:return 'locale_marker'
 if 'validation' in s:return 'validation'
 return 'content_contract'
def read(p):return [json.loads(s) for s in p.read_text('utf8').splitlines() if s.strip()]
def summarize(rows):
 counts=collections.Counter();locales=collections.defaultdict(collections.Counter);failed=[]
 for row in rows:
  counts['requests']+=1;counts['exceptions']+=bool(row.get('exception'));counts['validation_rejected_requests']+=(row.get('result') or {}).get('validation',{}).get('ok') is False
  for g in row['grades']:
   counts['grades']+=1;counts['strict_pass']+=g['passed'];locales[row['effective_locale']]['grades']+=1;locales[row['effective_locale']]['strict_pass']+=g['passed']
   ps=collections.defaultdict(list)
   for e in g['failures']:ps[partition(e)].append(e)
   if not g['passed']:
    counts['failed_grades']+=1
    for p in ps:counts[p+'_failed_grades']+=1
    if set(ps)=={'protocol_outcome'}:counts['protocol_only_failed']+=1
    failed.append({'question':row['question'],'key':row['key'],'grade':g,'partitions':dict(ps),'answer':row['result'].get('answer'),'plan':row['result'].get('decision_artifact')})
 times=sorted(r['elapsed_wall'] for r in rows)
 return {'counts':dict(counts),'locales':{k:dict(v) for k,v in locales.items()},'timing':{'mean':sum(times)/len(times),'p50':times[math.ceil(len(times)*.5)-1],'p95':times[math.ceil(len(times)*.95)-1],'max':max(times)}},failed
old=read(B.parent/'r66_common_repair_20261014/MATRIX_final20_off.jsonl');new=read(B/'MATRIX_final05_off.jsonl');a,_=summarize(old);b,failed=summarize(new)
old_by={r['key']:r for r in old};changes=[];newcontent=[]
for r in new:
 previous=old_by[r['key']]
 for og,ng in zip(previous['grades'],r['grades']):
  assert (og['file'],og['row'],og['variant'])==(ng['file'],ng['row'],ng['variant'])
  added=[e for e in ng['failures'] if e not in og['failures']]
  if og['passed']!=ng['passed'] or added:changes.append({'question':r['question'],'before_pass':og['passed'],'after_pass':ng['passed'],'new_failures':added,'before_answer':previous['result'].get('answer'),'after_answer':r['result'].get('answer')})
  if any(partition(e)=='content_contract' for e in added):newcontent.append(changes[-1])
report={'baseline':'R66 final20 common OFF, existing stored results','current':'R67 final05 common OFF','legacy_rerun':False,'same_questions':set(old_by)=={r['key'] for r in new},'before':a,'after':b,'strict_repairs':sum(not c['before_pass'] and c['after_pass'] for c in changes),'strict_regressions':sum(c['before_pass'] and not c['after_pass'] for c in changes),'new_content_contract_failures':newcontent,'changes':changes}
(B/'PAIRED_R66_R67.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
(B/'ALL_FAILED_GRADES_final05.json').write_text(json.dumps(failed,ensure_ascii=False,indent=2),encoding='utf8')
md=['# ผลที่ยังไม่ผ่าน — ชุดเดิม 223 คำถาม / 503 เกณฑ์ (ปิด LLM)','','จำนวนเกณฑ์ตกไม่ใช่จำนวนคำถามที่ตอบผิดเชิงความหมาย ต้องอ่าน source และ scope ประกอบ แบ่งกลุ่มซ้อนกันได้','']
for i,r in enumerate(failed,1):md += [f'## {i}. {r["question"]}','','```json',json.dumps(r['partitions'],ensure_ascii=False,indent=2),'```','','คำตอบจริง:','',r['answer'] or '', '']
(B/'ALL_FAILED_GRADES_final05.md').write_text('\n'.join(md),encoding='utf8')
print(json.dumps({k:v for k,v in report.items() if k not in ['changes','new_content_contract_failures']},ensure_ascii=False,indent=2));print('NEW CONTENT CONTRACT FAILURES',json.dumps(newcontent,ensure_ascii=False)[:8000])
