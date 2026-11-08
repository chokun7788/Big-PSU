"""Preselect real API checks before the training outcomes are available."""
import json
from pathlib import Path
R=Path(__file__).resolve().parent
read=lambda n:list(map(json.loads,(R/n).open(encoding='utf8')))
test=read('test.jsonl');jobs={j['key']:j for j in read('ALL_RETAINED_JOBS.jsonl')}
indices=[1,4,9,10,13,14,21,29]
selected=[jobs[test[i]['key']] for i in indices]
(R/'API_SELECTED_JOBS.jsonl').write_text(''.join(json.dumps(j,ensure_ascii=False)+'\n' for j in selected),'utf8')
(R/'API_SELECTION_MANIFEST.json').write_text(json.dumps({'requests':len(selected),'selected_test_indices':indices,'selection_before_training_results':True,'new_questions':0,'reason':'existing difficult contexts: tournament, inventory, multiple needs, eligibility, bring-vs-consume, game-service mapping, booking and identification','model_payload_contains_no_keys_or_gold':True},ensure_ascii=False,indent=2),'utf8')
print(len(selected),'retained API questions selected')
