"""Actual 4-bit LoRA optimization with a frozen base, context-first labels only."""
import argparse,contextlib,gc,hashlib,json,math,os,random,shutil,time,traceback
from pathlib import Path
R=Path(__file__).resolve().parent
os.environ.update(HF_HUB_OFFLINE='1',HF_HUB_DISABLE_TELEMETRY='1',TOKENIZERS_PARALLELISM='false',WANDB_DISABLED='true')
import torch
import torch.nn.functional as F
from transformers import AutoTokenizer,AutoModelForCausalLM,BitsAndBytesConfig
from peft import LoraConfig,get_peft_model,prepare_model_for_kbit_training,set_peft_model_state_dict
from safetensors.torch import load_file

from context_contract import messages
parser=argparse.ArgumentParser();parser.add_argument('--run',default='train01');args=parser.parse_args()
OUT=R/args.run;OUT.mkdir(exist_ok=False)
BASE=Path('D:/CodexTraining/psu-r121-20261022/model');START=time.monotonic()
CFG={'seed':121,'epochs':3,'batch_size':1,'gradient_accumulation':8,'learning_rate':.00015,'lora_rank':8,'lora_alpha':16,'lora_dropout':.05,
 'target_modules':['q_proj','k_proj','v_proj','o_proj'],'quant_type':'nf4','double_quant':True,'compute_dtype':'bfloat16','max_sequence_tokens':2048,
 'max_generation_tokens':850,'validation_selection':'lowest mean completion loss','base_repository':'typhoon-ai/typhoon2.5-qwen3-4b','base_revision':'ce0a7416fe82d4404b2b4a253ce3ac095ab1252c',
 'protocol':'r129-plan-v2','reviewed_labels':True,'business_answer_targets':False,'new_questions':0,'production_installed':False}
def write(name,v):(OUT/name).write_text(json.dumps(v,ensure_ascii=False,indent=2),'utf8')
def status(phase,**kw):
 v={'phase':phase,'elapsed_sec':round(time.monotonic()-START,2),'pid':os.getpid(),'updated_at':time.time(),**kw}
 tmp=OUT/('progress_'+str(time.time_ns())+'.json');tmp.write_text(json.dumps(v,ensure_ascii=False,indent=2),'utf8')
 # Status telemetry must never abort GPU work because Windows holds a reader.
 for attempt in range(8):
  try:os.replace(tmp,OUT/'PROGRESS.json');break
  except PermissionError:time.sleep(.05*(attempt+1))
 with (OUT/'STATUS_JOURNAL.jsonl').open('a',encoding='utf8') as journal:journal.write(json.dumps(v,ensure_ascii=False)+'\n')
 print(json.dumps(v,ensure_ascii=False),flush=True)
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def read(n):return json.loads((R/n).read_text('utf8'))
def rows(n):return list(map(json.loads,(R/n).open(encoding='utf8')))
def fingerprint(model,adapter):
 h=hashlib.sha256();count=0
 for n,p in model.named_parameters():
  if ('lora_' in n)!=adapter:continue
  h.update(n.encode());h.update(str(tuple(p.shape)).encode());h.update(str(p.dtype).encode())
  raw=p.detach().contiguous().view(torch.uint8).reshape(-1)
  for i in range(0,raw.numel(),8*1024*1024):h.update(raw[i:i+8*1024*1024].cpu().numpy().tobytes())
  count+=1
 return {'sha256':h.hexdigest(),'parameter_tensors':count}
def loss_for(model,x):
 ids=torch.tensor([x['input_ids']],dtype=torch.long,device='cuda');p=x['prompt_len'];length=ids.shape[-1]
 # Predict completion tokens only. Avoid allocating vocabulary logits for the
 # long prompt; every completion token still receives ordinary causal CE loss.
 positions=torch.arange(p-1,length-1,device='cuda')
 with torch.autocast('cuda',dtype=torch.bfloat16):out=model(input_ids=ids,attention_mask=torch.ones_like(ids),use_cache=False,logits_to_keep=positions)
 logits=out.logits.reshape(-1,out.logits.shape[-1]);target=ids[:,p:].reshape(-1)
 return F.cross_entropy(logits.float(),target)
def validation_loss(model,xs):
 model.eval();losses=[]
 with torch.no_grad():
  for x in xs:losses.append(float(loss_for(model,x)))
 return sum(losses)/len(losses)
try:
 write('TRAINING_CONFIG.json',CFG)
 freeze=read('DATASET_FREEZE.json')
 for p,h in freeze.items():assert sha(p)==h,('dataset_changed',p)
 freeze.update({str((R/n).resolve()):sha(R/n) for n in [Path(__file__).name,'context_contract.py','system/app/knowledge/common/domain_flow/graph_protocol.py','TOKENIZED_train.json','TOKENIZED_validation.json','TOKENIZED_test.json','ANNOTATION_REVIEW_SUMMARY.json','EVALUATION_PROTOCOL.json']})
 write('RUN_FREEZE.json',freeze)
 assert read('ANNOTATION_REVIEW_SUMMARY.json')['reviewed']==289
 train=read('TOKENIZED_train.json');val=read('TOKENIZED_validation.json');test=rows('test.jsonl')
 assert len(train)>100 and len(test)>30 and all(len(x['input_ids'])<=CFG['max_sequence_tokens'] for x in train+val)
 random.seed(CFG['seed']);torch.manual_seed(CFG['seed']);torch.cuda.manual_seed_all(CFG['seed'])
 status('loading_base',gpu=torch.cuda.get_device_name(0),free_total=torch.cuda.mem_get_info())
 tok=AutoTokenizer.from_pretrained(BASE,local_files_only=True,trust_remote_code=False)
 quant=BitsAndBytesConfig(load_in_4bit=True,bnb_4bit_quant_type='nf4',bnb_4bit_use_double_quant=True,bnb_4bit_compute_dtype=torch.bfloat16)
 base=AutoModelForCausalLM.from_pretrained(BASE,quantization_config=quant,device_map={'':0},torch_dtype=torch.bfloat16,low_cpu_mem_usage=True,local_files_only=True,trust_remote_code=False,attn_implementation='sdpa')
 base=prepare_model_for_kbit_training(base,use_gradient_checkpointing=True,gradient_checkpointing_kwargs={'use_reentrant':False})
 # Frozen embedding/head matrices need not stay fp32. Preserve layer norms in
 # fp32 and keep all trainable LoRA tensors under autocast for a 6 GB device.
 for mod in [base.get_input_embeddings(),base.get_output_embeddings()]:
  if mod is not None and not getattr(mod.weight,'quant_state',None):mod.weight.data=mod.weight.data.to(torch.bfloat16)
 model=get_peft_model(base,LoraConfig(r=CFG['lora_rank'],lora_alpha=CFG['lora_alpha'],lora_dropout=CFG['lora_dropout'],target_modules=CFG['target_modules'],bias='none',task_type='CAUSAL_LM'))
 trainable=[(n,p) for n,p in model.named_parameters() if p.requires_grad]
 assert trainable and all('lora_' in n for n,p in trainable)
 write('MODEL_PREFLIGHT.json',{'trainable_parameters':sum(p.numel() for n,p in trainable),'trainable_names':[n for n,p in trainable],
  'base_requires_grad_parameters':sum(p.numel() for n,p in model.named_parameters() if p.requires_grad and 'lora_' not in n),'allocated_bytes':torch.cuda.memory_allocated(),'reserved_bytes':torch.cuda.memory_reserved(),'free_total':torch.cuda.mem_get_info()})
 initial_adapter=fingerprint(model,True);write('INITIAL_ADAPTER_HASH.json',initial_adapter)
 # Test outputs are saved without feeding them to optimization or selecting
 # hyperparameters from them. Validation selection uses only the other split.
 before_base=fingerprint(model,False);write('BASE_PARAMETERS_BEFORE.json',before_base)
 optimizer=torch.optim.AdamW([p for n,p in trainable],lr=CFG['learning_rate'],weight_decay=.01)
 steps_per_epoch=math.ceil(len(train)/CFG['gradient_accumulation']);total_steps=CFG['epochs']*steps_per_epoch
 optimizer_step=0;micro=0;best_val=math.inf;best_path=None;losslog=[]
 for epoch in range(CFG['epochs']):
  order=list(range(len(train)));random.Random(CFG['seed']+epoch).shuffle(order)
  model.train();model.config.use_cache=False;model.gradient_checkpointing_enable(gradient_checkpointing_kwargs={'use_reentrant':False});optimizer.zero_grad(set_to_none=True)
  for pos,i in enumerate(order):
   before=time.monotonic();loss=loss_for(model,train[i]);assert torch.isfinite(loss),('nonfinite_loss',micro)
   group_start=(pos//CFG['gradient_accumulation'])*CFG['gradient_accumulation'];denom=min(CFG['gradient_accumulation'],len(order)-group_start)
   (loss/denom).backward();micro+=1
   rec={'epoch':epoch+1,'micro_step':micro,'sample_key':train[i]['key'],'completion_loss':float(loss.detach()),'elapsed_micro_sec':round(time.monotonic()-before,3),'peak_allocated_bytes':torch.cuda.max_memory_allocated()};losslog.append(rec)
   with (OUT/'TRAINING_LOSS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(rec)+'\n')
   del loss
   if (pos+1)%CFG['gradient_accumulation']==0 or pos+1==len(order):
    norm=torch.nn.utils.clip_grad_norm_([p for n,p in trainable],1.0);assert torch.isfinite(norm) and float(norm)>0,('gradient',float(norm))
    warmup=min(1.,(optimizer_step+1)/5);progress=optimizer_step/max(1,total_steps-1);lr=CFG['learning_rate']*warmup*.5*(1+math.cos(math.pi*progress))
    for group in optimizer.param_groups:group['lr']=lr
    optimizer.step();optimizer.zero_grad(set_to_none=True);optimizer_step+=1
    status('training',epoch=epoch+1,epochs=CFG['epochs'],micro_step=micro,total_micro_steps=len(train)*CFG['epochs'],optimizer_step=optimizer_step,total_optimizer_steps=total_steps,
     loss=rec['completion_loss'],gradient_norm=float(norm),learning_rate=lr,peak_allocated_bytes=torch.cuda.max_memory_allocated())
  mean_val=validation_loss(model,val);checkpoint=OUT/f'epoch_{epoch+1:02}';model.save_pretrained(checkpoint,safe_serialization=True)
  write(f'VALIDATION_EPOCH_{epoch+1:02}.json',{'epoch':epoch+1,'mean_completion_loss':mean_val,'questions':len(val),'used_for_gradient_updates':False})
  if mean_val<best_val:best_val=mean_val;best_path=checkpoint
  status('epoch_saved',epoch=epoch+1,validation_loss=mean_val,best_validation_loss=best_val,optimizer_step=optimizer_step)
 assert optimizer_step==total_steps and micro==len(train)*CFG['epochs']
 final=OUT/'adapter';shutil.copytree(best_path,final)
 set_peft_model_state_dict(model,load_file(str(final/'adapter_model.safetensors'),device='cuda'))
 after_base=fingerprint(model,False);write('BASE_PARAMETERS_AFTER.json',after_base);assert before_base==after_base,'Frozen base weights changed'
 final_adapter=fingerprint(model,True);write('FINAL_ADAPTER_HASH.json',final_adapter);assert initial_adapter['sha256']!=final_adapter['sha256'],'Adapter weights did not change'
 write('OPTIMIZATION_PROOF.json',{'actual_weight_updates':True,'optimizer_steps':optimizer_step,'micro_steps':micro,'base_parameter_hash_unchanged':True,'initial_adapter':initial_adapter,'final_adapter':final_adapter,'best_checkpoint':str(best_path),'best_validation_loss':best_val,'adapter':str(final),'peak_allocated_bytes':torch.cuda.max_memory_allocated()})
 # Held-out test generation is performed later by the identical three-arm server.
 assert all(sha(p)==h for p,h in freeze.items()),'Frozen training source/data changed'
 write('TRAINING_COMPLETE.json',{'complete':True,'actual_weight_updates':True,'optimizer_steps':optimizer_step,'train_questions':len(train),'validation_questions':len(val),'test_questions':len(test),'new_questions':0,'base_parameters_unchanged':True,'adapter_changed':True,'selected_checkpoint':str(best_path),'adapter':str(final),'dataset_code_unchanged':True,'production_installed':False,'elapsed_sec':round(time.monotonic()-START,2)})
 status('complete',actual_weight_updates=True,adapter=str(final),optimizer_steps=optimizer_step)
except BaseException as exc:
 write('FAILED.json',{'error':repr(exc),'traceback':traceback.format_exc(),'elapsed_sec':time.monotonic()-START});status('failed',error=repr(exc));raise
