import json,time,urllib.request
from pathlib import Path
R=Path(__file__).resolve().parent
payload={'model':'psu-r121-base:latest','messages':[{'role':'system','content':'Return only the exact JSON object requested, no commentary.'},{'role':'user','content':'Return this JSON object exactly: {"ok":true,"items":[1,2,3]}'}],'stream':False,'think':False,'options':{'num_predict':1,'temperature':0,'num_ctx':1024}}
before=time.perf_counter();req=urllib.request.Request('http://127.0.0.1:12421/api/chat',json.dumps(payload).encode(),{'Content-Type':'application/json'})
with urllib.request.urlopen(req,timeout=60) as response:body=json.load(response)
out={'probe':'client_num_predict_1_contract_probe_not_customer_accuracy','request':payload,'response':body,'wall_sec':time.perf_counter()-before,'server_returned_more_than_requested_limit':body.get('eval_count',0)>1,'shared_model_queue_wait_not_separately_measured':True}
(R/'BACKEND_OPTIONS_PROBE.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'wall_sec':out['wall_sec'],'requested_limit':1,'actual_generated_tokens':body.get('eval_count'),'content':body.get('message',{}).get('content'),'limit_not_honored':out['server_returned_more_than_requested_limit']},ensure_ascii=False))
