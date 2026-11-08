"""Check completion and preserve each analysis command's output once."""
import sys,json,subprocess
from pathlib import Path
B=Path(__file__).resolve().parent;tag=sys.argv[1]
state=json.loads((B/('FINAL_'+tag)/'STATUS.json').read_text(encoding='utf-8'));assert state.get('complete')
out=B/('POSTPROCESS_'+tag);out.mkdir(exist_ok=False)
for script in ['verify_completed_gates.py','audit_results.py','compare_baseline.py']:
 with (out/(script+'.log')).open('x',encoding='utf-8') as f:subprocess.run([sys.executable,'-B',str(B/script),tag],cwd=B,stdout=f,stderr=subprocess.STDOUT,check=True)
audit=json.loads((B/('AUDIT_'+tag)/'SUMMARY.json').read_text(encoding='utf-8'))
for flag in ('off','llm'):
 d=audit[flag];print(json.dumps({'mode':flag,'counts':d['counts'],'locales':d['locales'],'timing':d['timing'],'model_trace_observations':d['model_trace_observations']},ensure_ascii=False))
