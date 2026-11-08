"""Source/scope contracts for customer probes; not a universal accuracy grader."""
from pathlib import Path
import collections,json,statistics
R=Path(__file__).resolve().parent
def load(tag):return [json.loads(l) for l in (R/tag/'ANSWERS.jsonl').read_text('utf8').splitlines()]
def verdict(row):
 q=row['question'];r=row['result'];a=r.get('decision_artifact',{});p=a.get('query_plan',{});hits=r.get('hits',[]);answer=r.get('answer','');history=row['history']
 if not r['validation']['ok'] or not answer.strip():return False,'invalid_or_empty'
 if 'refund' in q:return any(h.get('field')=='answer' for h in hits) and 'except' in answer.lower(),'refund source and exception retained'
 if 'ตอนเย็น' in q:return any(h.get('field')=='answer' for h in hits) and '16:00' in answer and 'Maintenance' in answer,'sourced regular timetable, not live hours'
 if 'วันและเวลา' in q or 'Monday morning' in q or 'days can I book' in q:return p.get('operation')=='calendar' and '13:00' in answer and 'Maintenance' in answer,'booking time predicate read as schedule, not booking steps'
 if q.startswith('VALORANT'):return a.get('response_type')=='unconfirmed' and not hits,'missing game-mode data stated explicitly'
 if q.startswith('ROV'):return bool(p.get('r98_pending_context')) and a.get('response_type')=='clarification','normal/competition context asked'
 if q.startswith('ศูนย์อยู่'):return len(a.get('need_results',[]))==2 and any(h.get('field')=='address' for h in hits) and bool(p.get('price_scope_request')),'location answered, service selection retained'
 if 'New Horizons' in q:return len({h.get('record_id') for h in hits if h.get('field')=='summary'})==2,'both requested game summaries sourced'
 if 'อุปกรณ์' in q or 'equipment' in q:return len({h.get('record_id') for h in hits})>=6,'PC equipment list sources retained'
 if q=='วันนี้เปิดไหม':return '16 ตุลาคม 2569' in answer and len(answer)<100,'compact answer with test reference date'
 if 'ว่างไหม' in q:return [n['status'] for n in a.get('need_results',[])]==['live_unavailable','supported'] and bool(hits),'live unavailable separated from booking procedure'
 if 'own food' in q:return a.get('response_type')=='partial_answer' and a.get('source_scope_review',{}).get('permission_inferred') is False and bool(hits),'food origin permission not inferred from consumption area'
 if not history and ('ทั้งหมด' not in q and 'all the prices' not in q):return a.get('response_type')=='clarification' and bool(p.get('price_scope_request')),'service selection prompt'
 receipt=p.get('set_receipt',{});expected=2 if q=='PC' else 8
 return receipt.get('total_members')==expected and receipt.get('returned_members_count')==expected and p.get('audience_selection',{}).get('eligibility_assumed') is False,'complete declared-service set; unresolved eligibility not assumed'
summary={};detailed=[]
for tag in ['baseline01','final_off01','final_on01','final_off02','final_on02']:
 rows=load(tag);checks=[]
 for row in rows:
  ok,contract=verdict(row);checks.append(ok);detailed.append({'tag':tag,'question':row['question'],'locale':row['locale'],'has_history':bool(row['history']),'passed':ok,'contract':contract,'mode':row['result']['mode']})
 summary[tag]={'requests':len(rows),'contract_passed':sum(checks),'contract_failed':len(checks)-sum(checks),'median_seconds':statistics.median(r['elapsed'] for r in rows),'max_seconds':max(r['elapsed'] for r in rows)}
(R/'CUSTOMER_PROBE_ANALYSIS.json').write_text(json.dumps({'summary':summary,'checks':detailed,'limits':'Targeted source/scope checks. No full accuracy score; baseline was LLM OFF and new ON comparison is not a controlled model-effect study.'},ensure_ascii=False,indent=2),'utf8')
print(json.dumps(summary,ensure_ascii=False));print(json.dumps([r for r in detailed if not r['passed'] and r['tag']!='baseline01'],ensure_ascii=False))
