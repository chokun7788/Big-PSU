import json,collections,re
from pathlib import Path
B=Path(__file__).resolve().parent
result={};fixture_tests=[]
for mode in ('legacy','common'):
 p=json.loads((B/(mode+'_test_all.py_temp_fixed.json')).read_text(encoding='utf-8'))
 counts=collections.Counter();samples=[]
 for typ in ('errors','failures'):
  for name,trace in p[typ]:
   key='ownership_blocked NameError' if 'NameError' in trace and 'ownership_blocked' in trace else 'missing reference fixture' if 'FileNotFoundError' in trace else trace.strip().splitlines()[-1][:150]
   counts[key]+=1
   if key=='missing reference fixture':fixture_tests.append({'mode':mode,'test':name})
   if len(samples)<12:samples.append({'test':name,'type':typ,'cause':key})
 result[mode]={'test_functions':p['tests'],'failure_events':len(p['failures']),'error_events':len(p['errors']),'skipped':len(p['skipped']),'causes':counts,'samples':samples}
(B/'NATIVE_UNIT_ANALYSIS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
(B/'FIXTURE_TESTS_TO_RERUN.json').write_text(json.dumps(fixture_tests,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'summary':{m:{k:v for k,v in r.items() if k!='samples'} for m,r in result.items()},'fixture_tests':fixture_tests},ensure_ascii=False))
