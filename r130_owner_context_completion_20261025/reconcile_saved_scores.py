"""Fixed input-defined denominators across saved R64/R95 and R130 outputs.

This reads saved grades only. It does not run a baseline or alter reference
grades. Unassessable literal checks are explicit instead of disappearing.
"""
import collections,gzip,hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parent;OUT=R/'full_analysis'
assert json.loads((OUT/'COVERAGE.json').read_text('utf8'))['complete']
expected={}
with (R.parent/'r95_merged_flow_implementation_20261018/FULL_JOBS.jsonl').open(encoding='utf8') as f:
 for line in f:
  x=json.loads(line);entries={}
  for e in x['entries']:
   c=e['case'];contract=c.get('answer_contract') or c
   entries[(e['file'],e['row'],e['variant'])]=bool(c.get('required_clauses') or c.get('clauses') or any(contract.get(k) for k in ['must_contain','must_contain_any','must_contain_all_groups']))
  expected[x['key']]={'locale':x['locale'],'entries':entries}
def read(path):
 with gzip.open(path,'rt',encoding='utf8') as f:
  for line in f:yield json.loads(line)
arms={'R64_legacy_llm':[R.parent/'r129_full_plan_completion_20261024/SAVED_LEGACY_ROWS.jsonl.gz'],'R95_common_llm':sorted((R.parent/'r95_merged_flow_implementation_20261018/full01').glob('RESULTS_*.jsonl.gz')),'R130_common_llm':sorted((R/'full01').glob('RESULTS_*.jsonl.gz'))}
summary={};paired={};coverage={}
for arm,paths in arms.items():
 seen=set();scores=collections.defaultdict(collections.Counter);flags={};missing_grades=0;unexpected_grades=0
 for p in paths:
  for x in read(p):
   key=x['key'];assert key not in seen,(arm,'duplicate_key',key);seen.add(key)
   assert key in expected,(arm,'unexpected_key',key)
   metadata=expected[key];locale=metadata['locale'];c=scores[locale];c['requests']+=1;actual=set()
   for g in x.get('grades',[]):
    gid=g['file'],g['row'],g['variant'];assert gid not in actual;(actual.add(gid));c['grades']+=1;c['strict_passed']+=int(g['passed'])
    if gid not in metadata['entries']:unexpected_grades+=1;continue
    literal=None
    if metadata['entries'][gid]:
     c['positive_literal_eligible']+=1
     not_executable=bool(x.get('exception') or any('pipeline_exception' in str(s) or 'grader_exception' in str(s) for s in g.get('failures',[])))
     if not not_executable:
      if isinstance(g.get('content_checks_passed'),bool):literal=g['content_checks_passed']
      elif isinstance(g.get('partitions'),dict):literal=not g['partitions'].get('content',[])
     c['positive_literal_unassessed' if literal is None else 'positive_literal_passed' if literal else 'positive_literal_failed']+=1
    flags[(key,*gid)]={'strict':bool(g['passed']),'literal':literal,'eligible':metadata['entries'][gid]}
   missing_grades+=len(set(metadata['entries'])-actual)
 for c in scores.values():
  c['strict_percent']=100*c['strict_passed']/c['grades'];eligible=c['positive_literal_eligible'];assessed=c['positive_literal_passed']+c['positive_literal_failed']
  c['literal_passed_over_all_eligible_percent']=100*c['positive_literal_passed']/eligible if eligible else None
  c['literal_passed_among_assessed_percent']=100*c['positive_literal_passed']/assessed if assessed else None
  assert c['positive_literal_passed']+c['positive_literal_failed']+c['positive_literal_unassessed']==eligible
 missing_keys=set(expected)-seen;coverage[arm]={'requests':len(seen),'grades':len(flags),'missing_keys':len(missing_keys),'missing_grades':missing_grades,'unexpected_grades':unexpected_grades};assert not missing_keys and not missing_grades and not unexpected_grades and len(flags)==55811
 summary[arm]=dict(scores);paired[arm]=flags
comparisons={}
for baseline in ['R64_legacy_llm','R95_common_llm']:
 counter=collections.Counter()
 for identity,new in paired['R130_common_llm'].items():
  old=paired[baseline][identity];counter['same_grade_identities']+=1
  counter['strict_both_pass']+=old['strict'] and new['strict'];counter['strict_baseline_only']+=old['strict'] and not new['strict'];counter['strict_R130_only']+=not old['strict'] and new['strict']
  if new['eligible']:
   counter['literal_fixed_eligible']+=1
   if old['literal'] is None or new['literal'] is None:counter['literal_unassessed_in_either_arm']+=1
   else:
    counter['literal_assessed_in_both']+=1;counter['literal_baseline_only']+=old['literal'] and not new['literal'];counter['literal_R130_only']+=not old['literal'] and new['literal']
 comparisons[baseline]=dict(counter)
result={'scores_by_requested_locale':summary,'coverage':coverage,'paired_same_grade_identities':comparisons,'literal_eligibility_defined_by_frozen_input_not_runtime_success':True,'unassessable_checks_retained_in_denominator_and_reported':True,'semantic_answer_accuracy':None,'baseline_inferences':0,'source_data_clock_deadline_backend_versions_differ':True,'causal_flow_effect':False}
(OUT/'FIXED_DENOMINATOR_SCORES.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),'utf8')
lines=['# เทียบ saved Flow เดิม / R95 / R130 ด้วยตัวหารเดียวกัน','','ใช้ request keys และ grade identities เดียวกัน ไม่รันคำถาม baseline ใหม่ แบ่งภาษาโดย requested locale จาก frozen workload ทุกแขน ข้อมูล clock/backend/deadline ต่างรุ่น จึงไม่ใช่ causal effect ของ Flow อย่างเดียว','', '| แขน | ภาษา request | Strict ผ่าน/ทั้งหมด | Strict % | Literal ผ่าน/มีเกณฑ์ | ยังประเมิน literal ไม่ได้ |','|---|---|---:|---:|---:|---:|']
for arm,locales in summary.items():
 for locale,c in sorted(locales.items()):lines.append(f"| {arm} | {locale} | {c['strict_passed']}/{c['grades']} | {c['strict_percent']:.2f} | {c['positive_literal_passed']}/{c['positive_literal_eligible']} | {c['positive_literal_unassessed']} |")
lines+=['','Positive literal เป็นชุดเกณฑ์ข้อความที่กำหนดจาก input ก่อนดูผล ไม่ใช่ semantic accuracy กรณี execution/grader ไม่สามารถประเมินได้แสดงไว้ในคอลัมน์แยก ไม่ตัดออกจนทำให้คะแนนดูดีขึ้น รายงานคำตรงตัวที่ประเมินได้กับตัวหารทั้งหมดแยกอยู่ใน JSON','', 'การเปลี่ยน route/intent/source-ID หรือ first-line wording ต้องแยกจากความถูกต้องของข้อเท็จจริง กรณีตัดสิน semantic ไม่ได้คง review_required']
(OUT/'SAVED_FLOW_COMPARISON_TH.md').write_text('\n'.join(lines)+'\n','utf8');print(json.dumps({'coverage':coverage,'same_reference_grade_count':55811,'new_baseline_inferences':0}))
