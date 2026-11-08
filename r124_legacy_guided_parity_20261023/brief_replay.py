import json,sys
from pathlib import Path
R=Path(__file__).resolve().parent
for line in (R/sys.argv[1]/'RESULTS.jsonl').read_text('utf8').splitlines():
 r=json.loads(line)
 if 'result' in r:r.update(artifact=r['result'].get('decision_artifact') or {},answer=r['result'].get('answer',''))
 a=r.get('artifact',{})
 needs=a.get('need_results',[])
 print(json.dumps({'key':r['key'][:8],'question':r['question'],'answer':r.get('answer','')[:380],
  'states':[n.get('execution_contract',{}).get('terminal_state',n.get('status')) for n in needs],
  'reason':[n.get('execution_contract',{}).get('reason_codes',n.get('reason_codes')) for n in needs],
  'skipped':r.get('skipped'),'error':r.get('error')},ensure_ascii=False))
