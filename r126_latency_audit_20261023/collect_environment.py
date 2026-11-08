import json,subprocess,time
from pathlib import Path
R=Path(__file__).resolve().parent
queries={'power_scheme':['powercfg','/getactivescheme'],'gpu':['nvidia-smi','--query-gpu=name,pstate,power.draw,power.limit,clocks.current.sm,clocks.max.sm,memory.used,memory.total,memory.free','--format=csv,noheader'],'battery':['pwsh','-NoProfile','-Command','Get-CimInstance -Namespace root/wmi -ClassName BatteryStatus | Select-Object PowerOnline,Discharging,Charging | ConvertTo-Json']}
output={'captured_at':time.time(),'read_only':True,'settings_changed':False,'queries':{}}
for key,cmd in queries.items():
 result=subprocess.run(cmd,capture_output=True,text=True,timeout=15);output['queries'][key]={'command':cmd,'exit_code':result.returncode,'stdout':result.stdout.strip(),'stderr':result.stderr.strip()}
(R/'ENVIRONMENT.json').write_text(json.dumps(output,ensure_ascii=False,indent=2),'utf8');print(json.dumps(output,ensure_ascii=False,indent=2))
