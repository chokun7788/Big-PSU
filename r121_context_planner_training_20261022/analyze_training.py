"""Report saved measurements without rerunning any questions."""
import collections,hashlib,json,statistics
from pathlib import Path
from planner_metrics import aggregate
R=Path(__file__).resolve().parent;T=R/'train02'
def read(p):return json.loads(p.read_text('utf8'))
def rows(p):return list(map(json.loads,p.open(encoding='utf8')))
def write(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2),'utf8')
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
assert read(T/'TRAINING_COMPLETE.json')['complete']
gold=rows(R/'test.jsonl');base=rows(T/'baseline_test.jsonl');trained=rows(T/'trained_test.jsonl')
assert len(gold)==len(base)==len(trained)==30 and [x['key'] for x in gold]==[x['key'] for x in base]==[x['key'] for x in trained]
metrics=['source_contract_valid','focus_correct','domains_correct','domain_facet_correct','task_count_correct','tasks_exact']
summary={'baseline':aggregate(base),'trained':aggregate(trained),'by_locale':{},'paired':{},'test_size':30,'semantic_answer_accuracy':None}
for loc in sorted({r['locale'] for r in gold}):
 summary['by_locale'][loc]={name:aggregate([r for r in rs if r['locale']==loc]) for name,rs in [('baseline',base),('trained',trained)]}
for k in metrics:summary['paired'][k]={'improved':sum(not b['metrics'][k] and a['metrics'][k] for b,a in zip(base,trained)),'regressed':sum(b['metrics'][k] and not a['metrics'][k] for b,a in zip(base,trained))}
summary['latency']={n:{'median_sec':statistics.median(r['elapsed_sec'] for r in rs),'total_sec':sum(r['elapsed_sec'] for r in rs)} for n,rs in [('baseline',base),('trained',trained)]}
protected=read(R/'PROTECTED_INPUTS.json');changed=[p for p,h in protected.items() if not Path(p).is_file() or sha(Path(p))!=h]
assert not changed,changed
write(R/'SOURCE_VERIFICATION.json',{'protected_files':len(protected),'all_unchanged':True,'changed':changed})
write(R/'PLANNER_COMPARISON.json',summary)
body=['# R121 — เปรียบเทียบการตีโจทย์ก่อน/หลังฝึกจริง','', 'วัดคำถามเดิม 30 ข้อ แยก family จากชุดสอน คะแนนนี้เป็นการตีโจทย์เทียบ agent-authored labels ไม่ใช่ความถูกต้องของคำตอบปลายทาง','', '| ตัววัด | ก่อนฝึก | หลังฝึก | ดีขึ้น / ถอยลง |','|---|---:|---:|---:|']
for k in metrics:body.append(f"| {k} | {summary['baseline'][k]}/30 | {summary['trained'][k]}/30 | {summary['paired'][k]['improved']} / {summary['paired'][k]['regressed']} |")
body+=['', '`tasks_exact` หมายถึงชุด signature (domain, operation, facet, ambiguous) ที่ตรงกันและผ่าน contract ไม่ได้หมายถึง target/constraints ทุกตัวตรง gold ส่วน typed-constraint precision/recall เป็นการเทียบ slot และข้อความตรงตัว ข้อความที่ต่าง gold แต่อ้างจากคำถามถูกอาจยังยอมรับได้ และการไม่มี typed slot ไม่ได้แปลว่าบริบทหาย หากยังอยู่ใน task quote จึงต้อง review ความหมายแยก','', '## แยกภาษา/locale','']
for loc,s in summary['by_locale'].items():
 body+=['### '+loc,'',f"จำนวน {s['baseline']['requests']} ข้อ; focus {s['baseline']['focus_correct']} → {s['trained']['focus_correct']}; domain {s['baseline']['domains_correct']} → {s['trained']['domains_correct']}; exact task signature {s['baseline']['tasks_exact']} → {s['trained']['tasks_exact']}",'']
body+=['## รายข้อทั้งหมด','']
for i,(g,b,a) in enumerate(zip(gold,base,trained),1):
 body += [f"### {i}. {g['question']}",'',f"- key: `{g['key']}`; locale: {g['locale']}",f"- ก่อนฝึก focus/domain/facet/tasks: {b['metrics']['focus_correct']}/{b['metrics']['domains_correct']}/{b['metrics']['domain_facet_correct']}/{b['metrics']['tasks_exact']}",f"- หลังฝึก focus/domain/facet/tasks: {a['metrics']['focus_correct']}/{a['metrics']['domains_correct']}/{a['metrics']['domain_facet_correct']}/{a['metrics']['tasks_exact']}",f"- หลังฝึก contract: {a['metrics']['source_contract_reason']}; missing typed constraints: {a['metrics']['missing_constraints']}",'','Gold plan:','```json',json.dumps(g['label'],ensure_ascii=False,indent=2),'```','','ก่อนฝึก:','```',b['raw_output'],'```','','หลังฝึก:','```',a['raw_output'],'```','']
(R/'PLANNER_PER_REQUEST_TH.md').write_text('\n'.join(body),'utf8')
print(json.dumps(summary,ensure_ascii=False,indent=2))
