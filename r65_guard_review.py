import collections,json
from pathlib import Path
BASE=Path(__file__).resolve().parent;B=BASE/'r64_full_comparison_20261013';O=BASE/'r65_detailed_failure_analysis_20261014'
lines=['# Input guard: mismatchที่ตรวจทานแล้ว','', 'แทนการเลือกkeyในappendixฉบับร่างที่ไม่ครอบคลุมsuffix _match; ไม่แก้gradeหรือlogR64',''];summary={};total=0
for mode in ('legacy','common'):
 rows=json.loads((B/(mode+'_GUARD_RESULTS.json')).read_text(encoding='utf-8'));bad=[r for r in rows if any(r.get(k) is False for k in ('layout_match','repeat_match','legacy_block_policy_match'))]
 counts=collections.Counter((r.get('expected') or {}).get('anomaly_family','unknown') for r in bad);summary[mode]={'cases':len(rows),'mismatch_cases':len(bad),'families':counts}
 for r in bad:total+=1;lines+= [f"## {total}. {mode} / {r['id']} / {r['input']}",'','```json',json.dumps(r,ensure_ascii=False,indent=2),'```','']
with (O/'INPUT_GUARD_CASES_REVIEWED.md').open('x',encoding='utf-8') as f:f.write('\n'.join(lines))
coverage=json.loads((O/'EXPORT_COVERAGE.json').read_text(encoding='utf-8'));coverage['guard_mismatches_exported_reviewed']=total;coverage['guard_review']=summary
(O/'GUARD_REVIEW_COVERAGE.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2),encoding='utf-8')
main=O/'R65_DETAILED_FAILURE_ANALYSIS_TH.md';text=main.read_text(encoding='utf-8').replace('INPUT_GUARD_CASES.md','INPUT_GUARD_CASES_REVIEWED.md')
main.write_text(text,encoding='utf-8');print(json.dumps(summary,ensure_ascii=False))
