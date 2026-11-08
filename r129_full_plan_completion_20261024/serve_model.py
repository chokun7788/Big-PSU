"""Identical NF4 base with three actual planner weight profiles.

Only context_understanding activates adapters. No labels/test keys or answers
are loaded by this server. Wire messages are never silently rewritten.
"""
import argparse,contextlib,hashlib,json,os,threading,time,traceback
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
R=Path(__file__).resolve().parent
os.environ.update(HF_HUB_OFFLINE='1',HF_HUB_DISABLE_TELEMETRY='1',TOKENIZERS_PARALLELISM='false')
import torch
from transformers import AutoTokenizer,AutoModelForCausalLM,BitsAndBytesConfig
from peft import PeftModel,prepare_model_for_kbit_training
parser=argparse.ArgumentParser();parser.add_argument('--port',type=int,default=12921);parser.add_argument('--output-name',default='model01');args=parser.parse_args()
BASE=Path('D:/CodexTraining/psu-r121-20261022/model');OLD=R.parent/'r121_context_planner_training_20261022/train02';NEW=R/'training_v2/train01';MODEL='psu-r129:latest'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def digest(value):return hashlib.sha256(json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
for run in [OLD,NEW]:
 assert json.loads((run/'TRAINING_COMPLETE.json').read_text('utf8'))['complete']
 proof=json.loads((run/'OPTIMIZATION_PROOF.json').read_text('utf8'));assert proof['actual_weight_updates'] and proof['base_parameter_hash_unchanged']
 assert proof['initial_adapter']['sha256']!=proof['final_adapter']['sha256']
adapters={'base':None,'retained':sha(OLD/'adapter/adapter_model.safetensors'),'new':sha(NEW/'adapter/adapter_model.safetensors')}
revision='ce0a7416fe82d4404b2b4a253ce3ac095ab1252c';digests={k:digest({'revision':revision,'adapter':v,'precision':'NF4 double quant BF16'}) for k,v in adapters.items()}
tok=AutoTokenizer.from_pretrained(BASE,local_files_only=True,trust_remote_code=False)
quant=BitsAndBytesConfig(load_in_4bit=True,bnb_4bit_quant_type='nf4',bnb_4bit_use_double_quant=True,bnb_4bit_compute_dtype=torch.bfloat16)
base=AutoModelForCausalLM.from_pretrained(BASE,local_files_only=True,trust_remote_code=False,quantization_config=quant,device_map={'':0},torch_dtype=torch.bfloat16,attn_implementation='sdpa',low_cpu_mem_usage=True)
base=prepare_model_for_kbit_training(base,use_gradient_checkpointing=False)
for mod in [base.get_input_embeddings(),base.get_output_embeddings()]:
 if mod is not None and not getattr(mod.weight,'quant_state',None):mod.weight.data=mod.weight.data.to(torch.bfloat16)
model=PeftModel.from_pretrained(base,OLD/'adapter',adapter_name='retained',is_trainable=False)
model.load_adapter(NEW/'adapter',adapter_name='new',is_trainable=False);model.eval();model.config.use_cache=True;model.gradient_checkpointing_disable();torch.cuda.empty_cache()
lock=threading.Lock();loglock=threading.Lock();OUT=R/args.output_name;OUT.mkdir(exist_ok=False)
manifest={'serving_protocol':'r129-multi-profile-v2','pid':os.getpid(),'model':MODEL,'profiles':adapters,'profile_digests':digests,'base_revision':revision,'quantization':'NF4 double quant BF16','url':f'http://127.0.0.1:{args.port}','other_stages':'base','actual_weight_updates_verified':True,'production_installed':False}
(OUT/'SERVER.json').write_text(json.dumps(manifest,indent=2),'utf8')
class Handler(BaseHTTPRequestHandler):
 def send(self,status,data):
  b=json.dumps(data,ensure_ascii=False).encode();self.send_response(status);self.send_header('Content-Type','application/json');self.send_header('Content-Length',str(len(b)));self.end_headers()
  try:self.wfile.write(b)
  except (BrokenPipeError,ConnectionResetError,ConnectionAbortedError):pass
 def do_GET(self):
  if self.path=='/health':return self.send(200,manifest)
  if self.path=='/api/tags':return self.send(200,{'models':[{'name':MODEL,'model':MODEL,'digest':digest(digests)}]})
  return self.send(404,{'error':'not_found'})
 def do_POST(self):
  if self.path!='/api/chat':return self.send(404,{'error':'not_found'})
  before=time.monotonic();rec={'started_at':time.time(),'transport_ok':False}
  try:
   data=json.loads(self.rfile.read(int(self.headers['Content-Length'])));assert data['model']==MODEL,'unsupported_model'
   stage=data.get('stage','generic');profile=data.get('planner_profile','retained') if stage=='context_understanding' else 'base';assert profile in adapters
   wire=data['messages'];assert isinstance(wire,list) and wire
   prompt=tok.apply_chat_template(wire,tokenize=False,add_generation_prompt=True,enable_thinking=False)
   options=data.get('options') or {};limit=max(1,min(int(options.get('num_predict',900)),900 if stage=='context_understanding' else 640));timeout=max(1,min(float(data.get('request_timeout_sec',90)),180))
   with lock:
    remaining=timeout-(time.monotonic()-before)
    if remaining<=0:raise TimeoutError('model_request_expired_in_queue')
    model.set_adapter('retained' if profile=='base' else profile)
    inputs=tok(prompt,add_special_tokens=False,return_tensors='pt').to('cuda');assert inputs['input_ids'].shape[-1]<=8192,'context_too_long'
    with (model.disable_adapter() if profile=='base' else contextlib.nullcontext()),torch.inference_mode(),torch.autocast('cuda',dtype=torch.bfloat16):
     ids=model.generate(**inputs,max_new_tokens=limit,max_time=remaining,do_sample=False,use_cache=True,pad_token_id=tok.pad_token_id or tok.eos_token_id,eos_token_id=tok.eos_token_id)
    count=int(ids.shape[-1]-inputs['input_ids'].shape[-1]);content=tok.decode(ids[0,inputs['input_ids'].shape[-1]:],skip_special_tokens=True).strip();del inputs,ids
   provenance={'serving_protocol':manifest['serving_protocol'],'effective_profile':profile,'adapter_active':profile!='base','adapter_sha256':adapters[profile],'base_revision':revision,'profile_digest':digests[profile],'effective_messages_sha256':digest(wire),'effective_schema_sha256':digest(data.get('format')),'quantization':'NF4 double quant BF16','stage':stage,'effective_max_new_tokens':limit,'hit_token_limit':count>=limit}
   rec.update(transport_ok=True,provenance=provenance,input_messages=wire,schema=data.get('format'),raw_output=content,eval_count=count)
   self.send(200,{'model':MODEL,'message':{'role':'assistant','content':content},'done':True,'eval_count':count,'provenance':provenance})
  except Exception as exc:
   rec.update(error=repr(exc),traceback=traceback.format_exc());self.send(500,{'error':repr(exc)})
  finally:
   rec['elapsed_sec']=time.monotonic()-before
   with loglock,(OUT/'REQUESTS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(rec,ensure_ascii=False)+'\n')
 def log_message(self,*args):pass
print(json.dumps(manifest),flush=True);ThreadingHTTPServer(('127.0.0.1',args.port),Handler).serve_forever()
