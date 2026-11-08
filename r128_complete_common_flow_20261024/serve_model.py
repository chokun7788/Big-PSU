"""Actual local NF4 inference, with a trained context adapter and base selector.

This is an experiment transport, not an Ollama model or production install.
No test keys, gold labels, venue answers, or replay results are loaded.
"""
import argparse,contextlib,hashlib,json,os,threading,time,traceback
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
R=Path(__file__).resolve().parent
os.environ.update(HF_HUB_OFFLINE='1',HF_HUB_DISABLE_TELEMETRY='1',TOKENIZERS_PARALLELISM='false')
import torch
from transformers import AutoTokenizer,AutoModelForCausalLM,BitsAndBytesConfig
from peft import PeftModel,prepare_model_for_kbit_training
from context_contract import messages
parser=argparse.ArgumentParser();parser.add_argument('--port',type=int,default=12121);parser.add_argument('--output-name',default='inference01');args=parser.parse_args()
assert Path(args.output_name).name==args.output_name and args.output_name not in {'.','..'},'Use a new child directory name'
RUN=R.parent/'r121_context_planner_training_20261022/train02';BASE=Path('D:/CodexTraining/psu-r121-20261022/model');ADAPTER=RUN/'adapter'
assert json.loads((RUN/'TRAINING_COMPLETE.json').read_text('utf8'))['complete']
proof=json.loads((RUN/'OPTIMIZATION_PROOF.json').read_text('utf8'))
assert proof['actual_weight_updates'] and proof['optimizer_steps']==93 and proof['base_parameter_hash_unchanged']
assert proof['initial_adapter']['sha256']!=proof['final_adapter']['sha256']
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
adapter_sha=sha(ADAPTER/'adapter_model.safetensors');revision='ce0a7416fe82d4404b2b4a253ce3ac095ab1252c'
profiles={'psu-r121-base:latest':False,'psu-r121-trained:latest':True}
digests={k:hashlib.sha256((revision+adapter_sha+k).encode()).hexdigest() for k in profiles}
tok=AutoTokenizer.from_pretrained(BASE,local_files_only=True,trust_remote_code=False)
quant=BitsAndBytesConfig(load_in_4bit=True,bnb_4bit_quant_type='nf4',bnb_4bit_use_double_quant=True,bnb_4bit_compute_dtype=torch.bfloat16)
base=AutoModelForCausalLM.from_pretrained(BASE,local_files_only=True,trust_remote_code=False,quantization_config=quant,device_map={'':0},torch_dtype=torch.bfloat16,attn_implementation='sdpa',low_cpu_mem_usage=True)
base=prepare_model_for_kbit_training(base,use_gradient_checkpointing=False)
for mod in [base.get_input_embeddings(),base.get_output_embeddings()]:
 if mod is not None and not getattr(mod.weight,'quant_state',None):mod.weight.data=mod.weight.data.to(torch.bfloat16)
model=PeftModel.from_pretrained(base,ADAPTER,is_trainable=False);model.eval();model.config.use_cache=True
model.gradient_checkpointing_disable();torch.cuda.empty_cache();lock=threading.Lock()
OUT=R/args.output_name;OUT.mkdir(exist_ok=False)
manifest={'serving_protocol':'r128-bounded-context-v1','pid':os.getpid(),'url':f'http://127.0.0.1:{args.port}','profiles':profiles,'digests':digests,'base_revision':revision,'adapter_sha256':adapter_sha,'quantization':'NF4 double quant, BF16 compute','training_complete_verified':True,'production_installed':False}
(OUT/'SERVER.json').write_text(json.dumps(manifest,indent=2),'utf8')
class Handler(BaseHTTPRequestHandler):
 def send(self,status,data):
  b=json.dumps(data,ensure_ascii=False).encode();self.send_response(status);self.send_header('Content-Type','application/json');self.send_header('Content-Length',str(len(b)));self.end_headers()
  try:self.wfile.write(b)
  except (BrokenPipeError,ConnectionResetError,ConnectionAbortedError):pass
 def do_GET(self):
  if self.path=='/health':return self.send(200,manifest)
  if self.path=='/api/tags':return self.send(200,{'models':[{'name':k,'model':k,'digest':digests[k]} for k in profiles]})
  self.send(404,{'error':'not_found'})
 def do_POST(self):
  if self.path not in {'/api/chat','/api/generate'}:return self.send(404,{'error':'not_found'})
  before=time.monotonic();record={'started_at':time.time(),'transport_ok':False}
  try:
   data=json.loads(self.rfile.read(int(self.headers['Content-Length'])));profile=data['model'];record['requested_profile']=profile
   if profile not in profiles:
    record['error']='unsupported_model_profile';self.send(400,{'error':'unsupported_model_profile','supported':list(profiles)});return
   wire=data.get('messages')
   if wire is None:
    wire=([{'role':'system','content':data['system']}] if data.get('system') else [])+[{'role':'user','content':data.get('prompt','')}]
   try:user=json.loads(wire[-1]['content'])
   except (ValueError,TypeError):user=None
   context=isinstance(user,dict) and 'original_question' in user
   active=context and profiles[profile];stage='context' if context else ('evidence_selection' if isinstance(user,list) else 'generic_base_inference')
   if context:wire=messages(user['original_question'])
   else:
    wire=[dict(m) for m in wire]
    if isinstance(data.get('format'),dict):
     wire.insert(0,{'role':'system','content':'Return only JSON matching this schema: '+json.dumps(data['format'],separators=(',',':'))})
   # R121 adapter accepts a resolved question. Session facts never live in the weights.
   input_question=user['original_question'] if context else ''
   input_sha=hashlib.sha256(input_question.encode()).hexdigest() if context else None
   options=data.get('options') or {}
   requested_tokens=int(options.get('num_predict',512 if context else 640))
   max_tokens=max(1,min(requested_tokens,512 if context else 640))
   request_timeout=max(1.,min(float(data.get('request_timeout_sec',90)),180.))
   record.update(requested_tokens=requested_tokens,effective_max_new_tokens=max_tokens,request_timeout_sec=request_timeout,effective_input_sha256=input_sha,context_protocol=data.get('context_protocol','legacy-r121-resolved-question'))
   prompt=tok.apply_chat_template(wire,tokenize=False,add_generation_prompt=True,enable_thinking=False)
   with lock:
    remaining=request_timeout-(time.monotonic()-before)
    if remaining<=0:raise TimeoutError('model_request_expired_in_queue')
    inputs=tok(prompt,add_special_tokens=False,return_tensors='pt').to('cuda')
    assert inputs['input_ids'].shape[-1]<=8192,'context_too_long'
    with (contextlib.nullcontext() if active else model.disable_adapter()),torch.inference_mode(),torch.autocast('cuda',dtype=torch.bfloat16):
     ids=model.generate(**inputs,max_new_tokens=max_tokens,max_time=remaining,do_sample=False,use_cache=True,pad_token_id=tok.pad_token_id or tok.eos_token_id,eos_token_id=tok.eos_token_id)
    content=tok.decode(ids[0,inputs['input_ids'].shape[-1]:],skip_special_tokens=True).strip()
    count=int(ids.shape[-1]-inputs['input_ids'].shape[-1]);del inputs,ids
   provenance={'base_repository':'typhoon-ai/typhoon2.5-qwen3-4b','base_revision':revision,'adapter_sha256':adapter_sha,'adapter_active':active,'stage':stage,'quantization':'NF4','profile_digest':digests[profile],'serving_protocol':'r128-bounded-context-v1','effective_input_sha256':input_sha,'effective_max_new_tokens':max_tokens}
   result={'model':profile,'message':{'role':'assistant','content':content},'response':content,'done':True,'eval_count':count,'provenance':provenance}
   record.update(transport_ok=True,profile=profile,stage=stage,provenance=provenance,input_messages=wire,raw_output=content,eval_count=count)
   self.send(200,result)
  except Exception as exc:
   record.update(error=repr(exc),traceback=traceback.format_exc());self.send(500,{'error':repr(exc)})
  finally:
   record['elapsed_sec']=round(time.monotonic()-before,4)
   with (OUT/'REQUESTS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(record,ensure_ascii=False)+'\n')
 def log_message(self,*args):pass
print(json.dumps(manifest),flush=True)
ThreadingHTTPServer(('127.0.0.1',args.port),Handler).serve_forever()
