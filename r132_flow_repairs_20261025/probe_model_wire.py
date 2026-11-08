"""Bounded actual inference on existing held-out inputs and the changed prompt."""
import hashlib,json,os,sys,time,urllib.request
from pathlib import Path
R=Path(__file__).resolve().parent
os.environ.update(OLLAMA_URL='http://127.0.0.1:12921',PSU_CHATBOT_OLLAMA_MODEL='psu-r129:latest',PSU_PLANNER_PROFILE='retained')
sys.path.insert(0,str(R/'system'))
from app.knowledge.common.domain_flow.graph_protocol import messages
from app.knowledge.common.domain_flow.understanding import schema,parse
from app.knowledge.common.domain_flow.model_gateway import digest
out=R/('wire_smoke_'+str(time.time_ns()));out.mkdir()
cases=[json.loads(s) for s in (R/'test.jsonl').read_text('utf8').splitlines()][:3]
rows=[]
for i,c in enumerate(cases):
 q=c['question'];wire=messages(q);shape=schema()
 payload={'model':'psu-r129:latest','stage':'context_understanding','planner_profile':'retained','messages':wire,'format':shape,'stream':False,'think':False,'request_timeout_sec':100,'options':{'temperature':0,'seed':117,'num_ctx':6144,'num_predict':900}}
 before=time.perf_counter();row={'case_index':i,'question':q,'input_sha256':hashlib.sha256(q.encode()).hexdigest(),'messages':wire,'schema':shape}
 try:
  req=urllib.request.Request('http://127.0.0.1:12921/api/chat',json.dumps(payload).encode(),{'Content-Type':'application/json'})
  with urllib.request.urlopen(req,timeout=110) as f:response=json.load(f)
  raw=response['message']['content'];parsed=parse(raw,q)
  prov=response.get('provenance',{})
  row.update(raw_output=raw,response=response,wire_accepted=parsed.accepted,reason=parsed.reason,parsed_tasks=[t.as_dict() for t in parsed.tasks],identity_verified=response.get('model')=='psu-r129:latest' and prov.get('effective_profile')=='retained' and prov.get('effective_messages_sha256')==digest(wire) and prov.get('effective_schema_sha256')==digest(shape),schema_constrained_decoding=prov.get('schema_constrained_decoding',False))
 except Exception as e:row.update(error=repr(e),wire_accepted=False)
 row['elapsed_sec']=time.perf_counter()-before;rows.append(row)
 with (out/'RESULTS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(row,ensure_ascii=False)+'\n')
 print(json.dumps({k:row.get(k) for k in ['case_index','wire_accepted','reason','identity_verified','schema_constrained_decoding','elapsed_sec','error']},ensure_ascii=False),flush=True)
(out/'SUMMARY.json').write_text(json.dumps({'cases':len(rows),'accepted':sum(r.get('wire_accepted',False) for r in rows),'all_model_identities_verified':all(r.get('identity_verified') for r in rows),'semantic_accuracy':None,'staged_decoder_active':False},indent=2),'utf8')
(R/'LATEST_WIRE_SMOKE.json').write_text(json.dumps({'output':str(out)},indent=2),'utf8')
