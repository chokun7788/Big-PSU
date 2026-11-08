"""Group recorded changed answers by actual source references and review risks; no semantic grading."""
import collections,hashlib,json,re,time
from pathlib import Path
base=Path(__file__).resolve().parent
src=base/'changed_answer_group_queue_1793166229784847000'/'ITEMS.jsonl'
items=[json.loads(s) for s in src.read_text(encoding='utf8').splitlines() if s.strip()]
assert len(items)==750 and len({x['key'] for x in items})==750
terms=re.compile(r'\b(?:price|cost|baht|rate|fine|penalty|forfeit|rule|round|event|tournament|match|date|booking|available|permission|id|membership)\b|ราคา|ค่าปรับ|กฎ|แข่ง|รอบ|วันที่|จอง|สมาชิก|บัตร|อนุญาต',re.I)
num=re.compile(r'(?<!\w)\d+(?:[.,:]\d+)?(?!\w)')
groups=collections.defaultdict(list)
for x in items:
 refs=x['original_result']['source_refs']; category=tuple(sorted(x['categories'])); risk=[]
 if 'C13' in category:risk.append('competition_scope_or_conditions')
 if terms.search(x['question']):risk.append('decision_sensitive_topic')
 if set(num.findall(x['old']))!=set(num.findall(x['new'])):risk.append('numeric_tokens_changed')
 if not refs:risk.append('no_source_receipt')
 if len(category)>1:risk.append('multiple_categories')
 sig=(x['candidate_group'],category,tuple(tuple(r) for r in refs),tuple(risk))
 groups[sig].append(x)
out=base/('changed_answer_source_batches_'+str(time.time_ns()));out.mkdir()
report=[]
for i,(sig,rows) in enumerate(sorted(groups.items(),key=lambda e:(-len(e[1]),str(e[0]))),1):
 kind,cats,refs,risk=sig; report.append({'batch_id':i,'candidate_group':kind,'categories':cats,'source_refs':refs,'risk_flags':risk,'count':len(rows),'keys':[x['key'] for x in rows],'representatives':[{'key':x['key'],'question':x['question'],'old':x['old'],'new':x['new']} for x in rows[:3]],'semantic_status':'review_required'})
(out/'BATCHES.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
summary={'input_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'total_items':len(items),'batch_count':len(report),'risk_flag_counts':dict(collections.Counter(flag for b in report for flag in b['risk_flags'] for _ in b['keys'])),'same_source_batches_of_two_or_more':sum(b['count'] for b in report if b['count']>=2),'all_items_review_required':True,'semantic_acceptance_or_source_authority_inferred':False,'new_inference_or_http':False}
(out/'REPORT.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf8');print(json.dumps({'path':str(out),**summary},ensure_ascii=False))
