import sys,json
from pathlib import Path
ROOT=Path(__file__).parent;P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');sys.path.insert(0,str(P))
R=Path((ROOT/'r33_report_path.txt').read_text().strip())
from app.pipeline.bilingual_english import _member_rows
from collections import Counter
print('member groups',Counter(r['group'] for r in _member_rows()))
for line in (R/'candidate_B_focus.jsonl').open(encoding='utf-8'):
    x=json.loads(line)
    if x['score']['v2']['noisy']['passed']:continue
    print(json.dumps({k:x[k] for k in ('id','question','positive','recovered')} | dict(failure=x['score']['v2']['noisy']['failures'],recoveries=[(i['observed'],i['intended']) for i in x['recoveries']]),ensure_ascii=False))
if len(sys.argv)>1:
    for line in (R/'candidate_B_focus.jsonl').open(encoding='utf-8'):
        x=json.loads(line)
        if x['id'].endswith(sys.argv[1]):
            print(json.dumps(dict(question=x['question'],result=x['result']),ensure_ascii=False,indent=2))
