import urllib.request,json,time
from pathlib import Path
B=Path(__file__).resolve().parent;start=time.time()
payload={'model':'scb10x/typhoon2.5-qwen3-4b','stream':False,'think':False,'keep_alive':'10m','prompt':'Reply OK','options':{'num_ctx':4096,'num_predict':1,'temperature':0}}
try:
    req=urllib.request.Request('http://127.0.0.1:11434/api/generate',data=json.dumps(payload).encode(),headers={'Content-Type':'application/json'})
    with urllib.request.urlopen(req,timeout=60) as r:data=json.load(r)
    result={'warm_ready':True,'seconds':time.time()-start,'load_duration_ns':data.get('load_duration'),'total_duration_ns':data.get('total_duration'),'only_read_local_model':True}
except Exception as e:result={'warm_ready':False,'seconds':time.time()-start,'error_type':type(e).__name__,'error':str(e)}
(B/'LLM_WARM_PREFLIGHT.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(result)
