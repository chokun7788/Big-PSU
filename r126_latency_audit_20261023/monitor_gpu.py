import json,subprocess,time
from pathlib import Path
R=Path(__file__).resolve().parent;c=json.loads((R/'PROCESS.json').read_text('utf8'));OUT=Path(c['output'])
for i in range(150):
 if (OUT/'COMPLETE.json').exists():break
 try:
  r=subprocess.run(['nvidia-smi','--query-gpu=pstate,power.draw,power.limit,clocks.current.sm,utilization.gpu,utilization.memory,memory.used,memory.free','--format=csv,noheader,nounits'],capture_output=True,text=True,timeout=3)
  with (OUT/'GPU_DURING.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps({'time':time.time(),'columns':['pstate','power_w','power_limit_w','sm_mhz','gpu_pct','memory_pct','used_mib','free_mib'],'sample':r.stdout.strip(),'error':r.stderr.strip()})+'\n')
 except Exception as e:
  with (OUT/'GPU_DURING.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps({'time':time.time(),'error':repr(e)})+'\n')
 time.sleep(2)
print('GPU sampling finished')
