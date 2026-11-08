"""Finite full-test job supervisor. No schedule, no production mutation."""
import ctypes,json,os,subprocess,sys,time,datetime
from pathlib import Path
import report
B=Path(__file__).resolve().parent
kernel=ctypes.WinDLL('kernel32',use_last_error=True)
kernel.OpenProcess.argtypes=[ctypes.c_ulong,ctypes.c_int,ctypes.c_ulong];kernel.OpenProcess.restype=ctypes.c_void_p
kernel.GetExitCodeProcess.argtypes=[ctypes.c_void_p,ctypes.POINTER(ctypes.c_ulong)]
kernel.CloseHandle.argtypes=[ctypes.c_void_p]
handles={};owned=[];logs=[];restarts={k:0 for k in ('legacy_offline','common_offline','model_matrix')}
for item in json.loads((B/'ACTIVE_RUNNERS.json').read_text(encoding='utf-8-sig')):
 cmd=item['CommandLine']
 if 'r64_full_comparison_20261013' not in cmd:raise RuntimeError('Not an R64 runner')
 key='legacy_offline' if 'full_run.py legacy offline' in cmd else 'common_offline' if 'bounded_offline.py common' in cmd else 'model_matrix' if 'model_matrix.py' in cmd else None
 if key is None:raise RuntimeError('Unexpected runner identity')
 handles[key]=kernel.OpenProcess(0x1000,False,item['ProcessId'])
 if not handles[key]:raise RuntimeError('Cannot inspect owned process; do not restart on access failure. Windows error '+str(ctypes.get_last_error()))
def alive(handle):
 if not handle:return False
 code=ctypes.c_ulong()
 if not kernel.GetExitCodeProcess(handle,ctypes.byref(code)):raise RuntimeError('Process query denied; refusing duplicate restart')
 return code.value==259
def restart(key):
 restarts[key]+=1
 if restarts[key]>3:raise RuntimeError('Recovery attempts exhausted: '+key)
 tag='recovery_'+datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
 args=[sys.executable,'-B',str(B/'model_matrix.py'),'--resume','--tag',tag] if key=='model_matrix' else [sys.executable,'-B',str(B/'bounded_offline.py'),key.split('_')[0],'--resume','--tag',tag]
 log=(B/(key+'_'+tag+'.log')).open('x',encoding='utf-8');logs.append(log)
 p=subprocess.Popen(args,cwd=B.parent,stdout=log,stderr=subprocess.STDOUT,creationflags=subprocess.CREATE_NO_WINDOW);owned.append(p)
 if handles.get(key):kernel.CloseHandle(handles[key])
 handles[key]=kernel.OpenProcess(0x1000,False,p.pid)
 print(json.dumps({'event':'restart_owned_test_runner','key':key,'pid':p.pid,'args':args}),flush=True)
try:
 while True:
  report.main();result=json.loads((B/'ANALYSIS_LATEST.json').read_text(encoding='utf-8'))
  state={'updated':datetime.datetime.now().isoformat(),'complete':all(v['complete'] for v in result.values()),'coverage':{k:v['counts']['requests'] for k,v in result.items()},'restarts':restarts,'production_changed':False}
  (B/'SUPERVISOR_STATUS.json').write_text(json.dumps(state,ensure_ascii=False,indent=2),encoding='utf-8')
  print(json.dumps(state),flush=True)
  if state['complete']:
   (B/'FULL_TEST_COMPLETE.json').write_text(json.dumps(state,indent=2),encoding='utf-8');break
  for key in handles:
   needs=not result[key]['complete'] if key!='model_matrix' else not (result['legacy_llm']['complete'] and result['common_llm']['complete'])
   if needs and not alive(handles[key]):restart(key)
  # Short sleeps allow a normal interrupt. This finite job stops on full coverage.
  for _ in range(20):time.sleep(30)
except BaseException as e:
 (B/'SUPERVISOR_ERROR.json').write_text(json.dumps({'error':repr(e),'restarts':restarts,'work_not_complete':True},indent=2),encoding='utf-8');raise
finally:
 for h in handles.values():
  if h:kernel.CloseHandle(h)
 for log in logs:log.close()
