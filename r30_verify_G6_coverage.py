import json,collections
from pathlib import Path
r=Path(Path('r30_report_path.txt').read_text().strip());summary=json.loads((r/'final_G6_all_summary.json').read_text());keys=set();grades=0;provenance=collections.Counter();oldkeys=set()
for line in (r/'final_G5_all_results.jsonl').open(encoding='utf-8'):oldkeys.add(json.loads(line)['key'])
for line in (r/'final_G6_all_results.jsonl').open(encoding='utf-8'):
    x=json.loads(line);assert x['key'] not in keys;keys.add(x['key']);grades+=len(x['grades']);provenance[x.get('execution_provenance','missing')]+=1
assert keys==oldkeys and len(keys)==20327 and grades==55583
assert provenance['G6 affected competition replay']==summary['reexecuted_requests']
data={'unique_requests':len(keys),'case_grades':grades,'actual_G6_reexecutions':summary['reexecuted_requests'],'provenance_counts':provenance,'all_requests_reexecuted_in_G6':summary['reexecuted_requests']==len(keys),'identical_input_keys_to_G5':True,'actual_case_grade_counts_preserved':True,'scope_correction':'The conservative trace filter selected every input because competition capability metadata appears in all rows. Thus all 20327 requests were actually reexecuted. The not-a-new-20327-run phrase in the raw wrapper summary is a generic template; counts and per-row provenance establish actual coverage. Original raw summary retained.','static_profile':'LLM/semantic disabled; server locale binding, direct pipeline; runtime guard policy/API verified separately; controlled unavailable booking; no real occupancy oracle'}
with (r/'final_G6_verified_coverage.json').open('x',encoding='utf-8') as out:json.dump(data,out,ensure_ascii=False,indent=2)
print(json.dumps(data))
