import json,collections
from pathlib import Path
r=Path(Path('r30_report_path.txt').read_text().strip());flags=collections.defaultdict(collections.Counter);exact=0;rows=[]
for line in (r/'final_G5_runtime_guard500_results.jsonl').open(encoding='utf-8'):
    x=json.loads(line);c=x['case'];pred=set(x['quality']['flags']);expected=set(c['expected_flags']);exact+=pred==expected
    for name in ['keyboard_layout_mismatch','repeated_character_typo']:
        e=name in expected;a=name in pred;flags[name]['tp' if e and a else 'fn' if e else 'fp' if a else 'tn']+=1
    if pred!=expected:rows.append({'id':c['id'],'question':c['observed_input'],'expected':list(expected),'predicted':list(pred),'quality':x['quality']})
with (r/'final_G5_runtime_guard500_interpretation.json').open('x',encoding='utf-8') as out:json.dump({'total':500,'exact_flags':exact,'by_flag':flags,'flag_mismatches':rows,'policy_action_result':json.loads((r/'final_G5_runtime_guard500_summary.json').read_text()),'scope':'flag accuracy and applied policy actions, no semantic answer oracle; not independent holdout','metadata_caution':'raw_gold_expects_repeat_to_block in the older runner summary is a static label, not a dataset-derived fact; use original_label_block_match and source cases'},out,ensure_ascii=False,indent=2)
print(json.dumps({'exact_flags':exact,'by_flag':flags,'flag_mismatch_ids':[x['id'] for x in rows]}))
