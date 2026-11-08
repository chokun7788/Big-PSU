import gzip,json
from pathlib import Path
R=Path(__file__).resolve().parent
def rows(p):
 with gzip.open(p,'rt',encoding='utf8') as f:
  for line in f:yield json.loads(line)
old={x['key']:x for x in rows(R/'SAVED_R130_SELECTED_RESULTS.jsonl.gz')}
changed=[]
for p in (R/'sample01').glob('RESULTS_*.jsonl.gz'):
 for new in rows(p):
  prior=old[new['key']];og={(g['file'],g['row'],g['variant']):g for g in prior['grades']}
  for g in new['grades']:
   identity=(g['file'],g['row'],g['variant']);before=og[identity]
   if before['passed']==g['passed']:continue
   changed.append({'key':new['key'],'question':new['question'],'grade_identity':identity,'before_passed':before['passed'],'after_passed':g['passed'],'before_failures':before['failures'],'after_failures':g['failures'],'before_elapsed_sec':prior['elapsed_sec'],'after_elapsed_sec':new['elapsed_sec'],'answer_identical':prior['result']['answer']==new['result']['answer']})
out={'changed_grade_identities':len(changed),'changes':changed,'no_regrading_or_new_queries':True}
(R/'STRICT_ONLY_CHANGES_REVIEW.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),'utf8')
print(json.dumps(out,ensure_ascii=False))
