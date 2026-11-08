import json
from pathlib import Path
R=Path(__file__).resolve().parent;c=json.loads((R/'LIVE_API_PROCESS.json').read_text('utf8'));out=Path(c['output'])
for row in json.loads((out/'API_RESULTS.json').read_text('utf8')):
 if row['group']!='live_month':continue
 b=row['response'];a=b.get('decision_artifact',{})
 print(json.dumps({'q':row['question'],'answer':b['answer'],'resolved_question':b.get('resolved_question'),'state':b.get('common_read_state'),'understanding':a.get('understanding'),'context':b.get('context_resolution')},ensure_ascii=False))
