import json,hashlib,os,sys,time,urllib.request
from pathlib import Path
R=Path(__file__).resolve().parent;S=R/'system';sys.path.insert(0,str(S));os.environ.update(OLLAMA_URL='http://127.0.0.1:12421',PSU_CHATBOT_OLLAMA_MODEL='psu-r121-trained:latest')
with urllib.request.urlopen(os.environ['OLLAMA_URL']+'/health',timeout=4) as f:health=json.load(f)
assert health['training_complete_verified'] and health['serving_protocol']=='r128-bounded-context-v1'
question='Which keyboard key should I use for a heavy attack?'
payload={'model':'psu-r121-trained:latest','messages':[{'role':'user','content':json.dumps({'original_question':question})}],'options':{'num_predict':1},'context_protocol':'r128-resolved-question-v1','request_timeout_sec':30}
with urllib.request.urlopen(urllib.request.Request(os.environ['OLLAMA_URL']+'/api/chat',json.dumps(payload).encode(),{'Content-Type':'application/json'}),timeout=35) as f:one=json.load(f)
checks={'same_adapter_weights':health['adapter_sha256']=='e6a342902a0e469181094c05f412b355cef8cb1f57ce03aa78b6705b67f9b0d8','same_base_revision':health['base_revision']=='ce0a7416fe82d4404b2b4a253ce3ac095ab1252c','num_predict_honored':one['eval_count']<=1,'effective_input_hash_verified':one['provenance']['effective_input_sha256']==hashlib.sha256(question.encode()).hexdigest()}
from app.knowledge.common.domain_flow.understanding import interpret
from app.knowledge.common.domain_flow.contracts import RequestBudget
from app.knowledge.common.domain_flow.index import FactIndex
idx=FactIndex({'records':{},'facts':[]});budget=RequestBudget();first=interpret('How do I request assistance for a game that stops responding?',budget,index=idx);second_budget=RequestBudget();second=interpret('How do I request assistance for a game that stops responding?',second_budget,index=idx)
checks['actual_adapter_context_transport']=first.event.get('transport_ok') and first.event.get('effective_input_verified')
checks['actual_context_schema_checked']=first.accepted
checks['repeat_context_cached_without_generation']=second.accepted and second_budget.model_calls==0 and second.event.get('cache_hit') is True
out={'all_passed':all(checks.values()),'checks':checks,'health':health,'one_token_probe':one,'context':first.as_dict(),'cache':second.as_dict(),'weights_changed':False,'answer_accuracy_claimed':False}
(R/'MODEL_VERIFICATION.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),'utf8');print(json.dumps({'checks':checks,'all_passed':out['all_passed']},indent=2));assert out['all_passed']
