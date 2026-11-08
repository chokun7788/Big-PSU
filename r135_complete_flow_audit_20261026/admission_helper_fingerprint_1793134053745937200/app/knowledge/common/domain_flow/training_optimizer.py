"""Admission-first, offline LoRA consumer. Importing this module loads no model.

Recorded reviews and frozen protocols are evidence to audit, not semantic truth.
The caller must finish individual adjudication and freeze the evaluation protocol
before this consumer can import a tokenizer, CUDA framework, or optimizer.
"""
import datetime,json,math,os,platform,random,shutil,sys,time
from pathlib import Path
from .training_contract import Artifacts,digest,file_sha,load_admitted_dataset,runtime_contract,source_identity

CONFIG={'seed':121,'epochs':3,'batch_size':1,'gradient_accumulation':8,'learning_rate':0.00015,
        'lora_rank':8,'lora_alpha':16,'lora_dropout':0.05,'target_modules':['q_proj','k_proj','v_proj','o_proj'],
        'quant_type':'nf4','double_quant':True,'compute_dtype':'bfloat16','max_sequence_tokens':2048,
        'max_generation_tokens':850,'selection':'lowest development completion loss',
        'base_repository':'typhoon-ai/typhoon2.5-qwen3-4b',
        'base_revision':'ce0a7416fe82d4404b2b4a253ce3ac095ab1252c','precision':'HF_NF4_doublequant_BF16'}
STRATA=('single_need','multi_domain','shared_context','negation_condition_exception',
        'comparison_list_count','ambiguity_missing_source','conflict_validity_provider','event_dependencies')
METRICS=('planner','executor_verifier','end_to_end_answer')
REQUIRED_METRIC_COMPONENTS={
 'planner':('task_boundary_count','semantic_domain_operation_field','entity_binding','slot_role_scope','shared_context_override','factual_need_condition_coverage','clarification_precision_overasking','structural_validity_separate'),
 'executor_verifier':('requested_options_members','source_entity_event_audience_time_alignment','arithmetic_units_proof','conflict_validity_provider_status','independent_work_budget_drops','unsupported_operation_disclosure'),
 'end_to_end_answer':('source_supported_claims','need_option_completeness','unsupported_facts_permissions_conditions','abstention_clarification_refusal','claim_citation_alignment','first_line_relevance_repetition','cold_warm_median_p95_timeout_calls','complete_supported_answer_answerable_unanswerable'),
}
class AdmissionBlocked(ValueError):pass

def _read(path):return json.loads(Path(path).read_text('utf8'))
def _write(directory,name,value):
    (directory/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n','utf8')
def _progress(directory,value):
    # A Windows reader can hold PROGRESS.json open; telemetry must not abort
    # already admitted GPU work. The append-only journal retains every update.
    with (directory/'STATUS_JOURNAL.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(value)+'\n')
    temporary=directory/('progress_'+str(time.time_ns())+'.json');_write(directory,temporary.name,value)
    for attempt in range(8):
        try:os.replace(temporary,directory/'PROGRESS.json');return
        except PermissionError:time.sleep(0.05*(attempt+1))
def _run_files(dataset,code_root):
    result={str(p):file_sha(p) for p in dataset.iterdir() if p.is_file()}
    result.update({str(p):file_sha(p) for p in sorted(code_root.rglob('*.py'))})
    return result
def _require(ok,reason):
    if not ok:raise ValueError(reason)
def _files(root):
    return {str(p.relative_to(root)).replace('\\','/'):file_sha(p) for p in sorted(root.rglob('*')) if p.is_file()}

def verify_base(base,manifest,runtime):
    """The declared revision and complete local file manifest must both match."""
    base=Path(base).resolve();profile=runtime['model_profile'];files=manifest.get('files',{})
    _require(manifest.get('model_profile')==profile,'base_manifest_profile_mismatch')
    _require(all(profile.get(k)==CONFIG[k] for k in ['base_repository','base_revision','precision']),'unsupported_training_base_profile')
    _require(bool(files) and all(isinstance(k,str) and isinstance(v,str) and len(v)==64 for k,v in files.items()),'base_manifest_files_required')
    _require('config.json' in files and 'tokenizer_config.json' in files and 'chat_template.jinja' in files and any(k.endswith('.safetensors') for k in files),'base_manifest_incomplete')
    for name,sha in files.items():
        p=(base/name).resolve()
        _require(base in p.parents and p.is_file(),'base_manifest_path_invalid')
        _require(file_sha(p)==sha,'base_asset_changed:'+name)
    _require(_files(base)==files,'base_asset_inventory_changed')
    actual=runtime_contract(_read(base/'tokenizer_config.json'),chat_template=(base/'chat_template.jinja').read_text('utf8'),model_profile=profile)
    _require(actual==runtime,'actual_training_tokenizer_runtime_mismatch')

def verify_semantic_families(review,examples,keys):
    """Bind reviewed semantic groups to existing identities and one split.

    V2 permits a conservatively reviewed semantic group to contain distinct
    original families; it never rewrites those original identities.
    """
    version=review.get('version')
    _require(version in {'r135-semantic-family-review-v1','r135-semantic-family-review-v2'} and review.get('inventory_sha256')==digest(sorted(keys)),'semantic_family_review_required')
    bykey={x['question_key']:x for x in examples};seen=[]
    _require(len(bykey)==len(examples) and set(bykey)==set(keys),'semantic_family_example_inventory_mismatch')
    for g in review.get('groups',[]):
        members=g.get('question_keys')
        _require(isinstance(g.get('reason'),str) and bool(g['reason'].strip()) and isinstance(members,list) and bool(members),'semantic_family_reason_required')
        _require(all(k in bykey for k in members),'semantic_family_unknown_key')
        if version=='r135-semantic-family-review-v1':
            identity_ok={bykey[k]['family'] for k in members}=={g.get('family')}
        else:
            original=g.get('original_family_by_key')
            identity_ok=isinstance(g.get('semantic_family'),str) and bool(g['semantic_family'].strip()) and isinstance(original,dict) and set(original)==set(members) and all(original[k]==bykey[k]['family'] for k in members)
        _require(len({bykey[k]['split'] for k in members})==1 and identity_ok,'semantic_family_split_or_identity_mismatch')
        seen+=members
    _require(sorted(seen)==sorted(keys),'semantic_family_inventory_incomplete_or_duplicate')

def verify_protocol(protocol,artifacts,dataset,runtime,manifest_sha,source_sha):
    """Consume separately recorded family/coverage/metric decisions, never infer them."""
    freeze=_read(Path(dataset)/'DATASET_FREEZE.json')
    _require(protocol.get('version')=='r135-optimization-protocol-v1','optimization_protocol_version')
    for name,value in {'dataset_freeze_sha256':file_sha(Path(dataset)/'DATASET_FREEZE.json'),
                       'runtime_contract_sha256':digest(runtime),'base_manifest_sha256':manifest_sha,
                       'optimization_config_sha256':digest(CONFIG),'source_identity_sha256':source_sha}.items():
        _require(protocol.get(name)==value,'optimization_protocol_changed:'+name)
    keys=sorted(freeze['expected_keys']);keys_sha=digest(keys)
    families=artifacts.read(protocol['family_review_ref'])
    examples=[json.loads(x) for x in (Path(dataset)/'EXAMPLES.jsonl').read_text('utf8').splitlines() if x.strip()]
    verify_semantic_families(families,examples,keys)
    coverage=artifacts.read(protocol['coverage_review_ref'])
    _require(coverage.get('version')=='r135-strata-review-v1' and coverage.get('inventory_sha256')==keys_sha,'strata_review_required')
    _require(set(coverage.get('strata',{}))==set(STRATA),'all_eight_strata_must_be_reported')
    for name,c in coverage['strata'].items():
        ks=c.get('question_keys',[])
        _require(isinstance(ks,list) and len(ks)==len(set(ks)) and set(ks)<=set(keys),'stratum_keys_invalid:'+name)
        _require(c.get('status') in {'assessed','insufficient'} and isinstance(c.get('reason'),str) and bool(c['reason'].strip()),'stratum_review_reason_required:'+name)
        _require(bool(ks) or c['status']=='insufficient','empty_stratum_cannot_be_assessed:'+name)
        _require(c['status']!='insufficient' or isinstance(c.get('interpretation_limit'),str) and bool(c['interpretation_limit'].strip()),'sparse_stratum_limit_required:'+name)
    evaluation=artifacts.read(protocol['evaluation_plan_ref'])
    _require(evaluation.get('version')=='r135-three-arm-evaluation-v2' and evaluation.get('arms')==['base','r121','candidate'],'frozen_three_arm_evaluation_required')
    _require(evaluation.get('runtime_contract_sha256')==digest(runtime) and evaluation.get('source_identity_sha256')==source_sha,'evaluation_runtime_source_mismatch')
    _require(evaluation.get('semantic_unknown_handling')=='review_required' and evaluation.get('structural_is_semantic') is False,'evaluation_must_separate_semantics')
    for name in METRICS:
        block=evaluation.get('metrics',{}).get(name,{})
        _require(all(isinstance(block.get(k),str) and block[k].strip() for k in ['definitions','promotion_criteria','review_method']),'frozen_metric_criteria_required:'+name)
        components=block.get('components')
        _require(isinstance(components,dict) and set(components)==set(REQUIRED_METRIC_COMPONENTS[name]),'metric_component_inventory_required:'+name)
        for component,value in components.items():
            _require(isinstance(value,dict) and all(isinstance(value.get(k),str) and value[k].strip() for k in ['definition','denominator','review_method']),'metric_component_definition_required:'+name+':'+component)
    refs={name:artifacts.read(evaluation[name]) for name in ['question_inventory_ref','locale_ref','reference_clock_ref','live_fixture_ref','budgets_ref','retained_adapter_ref','exposure_review_ref']}
    inventory=refs['question_inventory_ref'].get('question_keys',[])
    _require(isinstance(inventory,list) and bool(inventory) and len(inventory)==len(set(inventory)),'evaluation_question_inventory_invalid')
    locales=refs['locale_ref'].get('requested_locales',{})
    _require(set(locales)==set(inventory) and all(v in {'th','en','auto'} for v in locales.values()),'evaluation_locale_inventory_mismatch')
    clock=datetime.datetime.fromisoformat(refs['reference_clock_ref']['reference_clock_iso'])
    _require(clock.tzinfo is not None,'evaluation_clock_timezone_required')
    _require(refs['live_fixture_ref'].get('mode')=='frozen_fixture' and isinstance(refs['live_fixture_ref'].get('observations'),list),'evaluation_live_fixture_required')
    budgets=refs['budgets_ref'];_require(budgets.get('context_generation_cap')==CONFIG['max_generation_tokens'] and bool(budgets.get('stage_budgets')),'evaluation_budget_contract_required')
    adapter=refs['retained_adapter_ref']
    _require(adapter.get('base_revision')==CONFIG['base_revision'] and adapter.get('precision')==CONFIG['precision'] and adapter.get('stage')=='context_understanding','evaluation_retained_adapter_identity_required')
    adapter_ref=adapter.get('weights_ref',{});ap=Path(adapter_ref.get('path','')).resolve()
    _require(any(ap==root or root in ap.parents for root in artifacts.roots) and ap.is_file() and file_sha(ap)==adapter_ref.get('sha256'),'evaluation_retained_adapter_weights_changed')
    exposure=refs['exposure_review_ref']
    _require(set(exposure.get('question_exposures',{}))==set(inventory) and all(v in {'unseen','retained_development'} for v in exposure['question_exposures'].values()),'evaluation_exposure_inventory_required')
    known=set(freeze.get('known_exposed',[]))
    _require(all(exposure['question_exposures'][k]=='retained_development' for k in set(inventory)&known),'exposed_evaluation_key_cannot_be_fresh_holdout')
    return {'families':families,'coverage':coverage,'evaluation':evaluation}

def admit_run(dataset,artifacts,runtime,base,base_manifest_ref,protocol_ref):
    # This must stay first: no expensive framework imports or even base-file
    # scanning is needed to reject a partially reviewed real corpus.
    if artifacts._cache is None:artifacts._cache={}
    splits=load_admitted_dataset(dataset,artifacts,runtime)
    manifest=artifacts.read(base_manifest_ref);verify_base(base,manifest,runtime)
    freeze=_read(Path(dataset)/'DATASET_FREEZE.json');source_sha=digest(source_identity(artifacts.read(freeze['source_ref'])))
    protocol=artifacts.read(protocol_ref)
    reviews=verify_protocol(protocol,artifacts,dataset,runtime,base_manifest_ref['sha256'],source_sha)
    artifacts.verify_pinned_files()
    return {'splits':splits,'manifest':manifest,'protocol':protocol,'reviews':reviews,'source_identity_sha256':source_sha}

def pack_examples(tokenizer,examples,runtime):
    """Use the exact inference template; reject long samples without truncation."""
    packed=[]
    for x in examples:
        ms=x['messages'];_require(ms[-1]['role']=='assistant','completion_role_invalid')
        prompt=tokenizer.apply_chat_template(ms[:-1],**runtime['template_options'])
        full=tokenizer.apply_chat_template(ms,**runtime['completion_template_options'])
        _require(isinstance(prompt,str) and isinstance(full,str) and full.startswith(prompt),'completion_template_prefix_mismatch')
        p=tokenizer(prompt,add_special_tokens=False)['input_ids'];ids=tokenizer(full,add_special_tokens=False)['input_ids']
        _require(ids[:len(p)]==p and 0<len(p)<len(ids),'completion_token_prefix_mismatch')
        _require(len(ids)<=CONFIG['max_sequence_tokens'],'training_example_exceeds_sequence_limit:'+x['question_key'])
        _require(len(ids)-len(p)<=CONFIG['max_generation_tokens'],'training_target_exceeds_generation_cap:'+x['question_key'])
        packed.append({'key':x['question_key'],'input_ids':ids,'prompt_len':len(p),'completion_len':len(ids)-len(p)})
    _require(bool(packed),'empty_optimization_or_development_split')
    return packed

def run_optimizer(dataset,artifacts,runtime,base,base_manifest_ref,protocol_ref,output,*,check_only=False):
    try:admitted=admit_run(dataset,artifacts,runtime,base,base_manifest_ref,protocol_ref)
    except (ValueError,KeyError,FileNotFoundError) as exc:raise AdmissionBlocked(str(exc)) from exc
    if check_only:return {'admitted':True,'optimizer_started':False,'split_counts':{k:len(v) for k,v in admitted['splits'].items()},'semantic_truth_verified':False}
    output=Path(output).resolve();base=Path(base).resolve();dataset=Path(dataset).resolve()
    for protected in [base,dataset]:
        _require(output!=protected and output not in protected.parents and protected not in output.parents,'training_output_overlaps_input')
    output.mkdir(exist_ok=False)
    started=time.monotonic()
    code_root=Path(__file__).resolve().parents[4]
    frozen_files=_run_files(dataset,code_root)
    _write(output,'RUN_FREEZE.json',{'files':frozen_files,'base_manifest_ref':base_manifest_ref,'protocol_ref':protocol_ref,
                                    'runtime':runtime,'config':CONFIG,'source_identity_sha256':admitted['source_identity_sha256'],
                                    'split_counts':{k:len(v) for k,v in admitted['splits'].items()},'test_used_for_selection':False,'production_installed':False})
    _progress(output,{'phase':'admitted_before_model_import','optimizer_started':False,'pid':os.getpid()})
    try:
        os.environ.update(HF_HUB_OFFLINE='1',HF_HUB_DISABLE_TELEMETRY='1',TOKENIZERS_PARALLELISM='false',WANDB_DISABLED='true')
        # Lazy imports are deliberately below actual row/source/protocol admission.
        import torch
        import torch.nn.functional as F
        from transformers import AutoTokenizer,AutoModelForCausalLM,BitsAndBytesConfig
        from peft import LoraConfig,get_peft_model,prepare_model_for_kbit_training,set_peft_model_state_dict
        from safetensors.torch import load_file
        from importlib.metadata import version
        _require(torch.cuda.is_available() and torch.cuda.is_bf16_supported(),'required_cuda_bf16_unavailable')
        environment={'python':sys.version,'platform':platform.platform(),'packages':{n:version(n) for n in ['torch','transformers','peft','bitsandbytes','safetensors']},
                     'cuda':torch.version.cuda,'gpu':torch.cuda.get_device_name(0),'free_total_bytes':list(torch.cuda.mem_get_info()),'reference_configuration':CONFIG}
        _write(output,'ENVIRONMENT.json',environment)
        tok=AutoTokenizer.from_pretrained(base,local_files_only=True,trust_remote_code=False)
        _require(digest(tok.chat_template)==runtime['chat_template_sha256'],'loaded_tokenizer_chat_template_changed')
        train=pack_examples(tok,admitted['splits']['train'],runtime);dev=pack_examples(tok,admitted['splits']['development'],runtime)
        for name,xs in [('train',train),('development',dev)]:_write(output,'TOKENIZED_'+name+'.json',xs)
        _write(output,'TOKEN_STATS.json',{name:{'rows':len(xs),'sequence_max':max(len(x['input_ids']) for x in xs),'completion_max':max(x['completion_len'] for x in xs),'truncated':0} for name,xs in [('train',train),('development',dev)]})
        random.seed(CONFIG['seed']);torch.manual_seed(CONFIG['seed']);torch.cuda.manual_seed_all(CONFIG['seed'])
        # Recheck all actual source and artifact bytes just before GPU loading.
        admit_run(dataset,artifacts,runtime,base,base_manifest_ref,protocol_ref)
        _require(_run_files(dataset,code_root)==frozen_files,'training_inputs_changed_before_model_load')
        quant=BitsAndBytesConfig(load_in_4bit=True,bnb_4bit_quant_type='nf4',bnb_4bit_use_double_quant=True,bnb_4bit_compute_dtype=torch.bfloat16)
        model=AutoModelForCausalLM.from_pretrained(base,quantization_config=quant,device_map={'':0},torch_dtype=torch.bfloat16,low_cpu_mem_usage=True,local_files_only=True,trust_remote_code=False,attn_implementation='sdpa')
        model=prepare_model_for_kbit_training(model,use_gradient_checkpointing=True,gradient_checkpointing_kwargs={'use_reentrant':False})
        for mod in [model.get_input_embeddings(),model.get_output_embeddings()]:
            if mod is not None and not getattr(mod.weight,'quant_state',None):mod.weight.data=mod.weight.data.to(torch.bfloat16)
        model=get_peft_model(model,LoraConfig(r=CONFIG['lora_rank'],lora_alpha=CONFIG['lora_alpha'],lora_dropout=CONFIG['lora_dropout'],target_modules=CONFIG['target_modules'],bias='none',task_type='CAUSAL_LM'))
        trainable=[(n,p) for n,p in model.named_parameters() if p.requires_grad]
        _require(bool(trainable) and all('lora_' in n for n,p in trainable),'non_adapter_trainable_parameters')
        _require(getattr(model,'is_loaded_in_4bit',False) is True,'actual_model_not_4bit')
        _write(output,'MODEL_PREFLIGHT.json',{'actual_model_class':type(model).__name__,'actual_base_class':type(model.get_base_model()).__name__,
              'actual_config_model_type':model.config.model_type,'actual_name_or_path':model.config._name_or_path,'actual_loaded_in_4bit':model.is_loaded_in_4bit,
              'backend':'transformers/HF','compute_dtype':str(torch.bfloat16),'quantization_config':quant.to_dict(),
              'parameter_dtypes':sorted({str(p.dtype) for n,p in model.named_parameters()}),'base_manifest_ref':base_manifest_ref,
              'base_revision_proof':'complete local asset hashes checked against the frozen manifest; revision string alone is not proof',
              'actual_allocated_bytes':torch.cuda.memory_allocated(),'actual_reserved_bytes':torch.cuda.memory_reserved()})
        def fingerprint(adapter):
            import hashlib
            h=hashlib.sha256();count=0
            for n,p in model.named_parameters():
                if ('lora_' in n)!=adapter:continue
                h.update(n.encode());h.update(str(tuple(p.shape)).encode());h.update(str(p.dtype).encode());raw=p.detach().contiguous().view(torch.uint8).reshape(-1)
                for i in range(0,raw.numel(),8*1024*1024):h.update(raw[i:i+8*1024*1024].cpu().numpy().tobytes())
                count+=1
            return {'sha256':h.hexdigest(),'parameter_tensors':count}
        def loss_for(x):
            ids=torch.tensor([x['input_ids']],dtype=torch.long,device='cuda');p=x['prompt_len'];positions=torch.arange(p-1,ids.shape[-1]-1,device='cuda')
            with torch.autocast('cuda',dtype=torch.bfloat16):result=model(input_ids=ids,attention_mask=torch.ones_like(ids),use_cache=False,logits_to_keep=positions)
            return F.cross_entropy(result.logits.reshape(-1,result.logits.shape[-1]).float(),ids[:,p:].reshape(-1))
        base_before=fingerprint(False);adapter_before=fingerprint(True)
        _write(output,'PARAMETERS_BEFORE.json',{'base':base_before,'adapter':adapter_before,'trainable_names':[n for n,p in trainable],'trainable_parameters':sum(p.numel() for n,p in trainable)})
        optimizer=torch.optim.AdamW([p for n,p in trainable],lr=CONFIG['learning_rate'],weight_decay=0.01)
        total_steps=CONFIG['epochs']*math.ceil(len(train)/CONFIG['gradient_accumulation']);steps=0;step_attempts=0;micro=0;best=math.inf;best_path=None
        for epoch in range(CONFIG['epochs']):
            order=list(range(len(train)));random.Random(CONFIG['seed']+epoch).shuffle(order);model.train();model.config.use_cache=False;optimizer.zero_grad(set_to_none=True)
            for pos,i in enumerate(order):
                loss=loss_for(train[i]);_require(bool(torch.isfinite(loss)),'nonfinite_training_loss')
                group_start=pos//CONFIG['gradient_accumulation']*CONFIG['gradient_accumulation'];denom=min(CONFIG['gradient_accumulation'],len(order)-group_start)
                (loss/denom).backward();micro+=1;record={'epoch':epoch+1,'micro_step':micro,'question_key':train[i]['key'],'completion_loss':float(loss.detach())};del loss
                if (pos+1)%CONFIG['gradient_accumulation']==0 or pos+1==len(order):
                    norm=torch.nn.utils.clip_grad_norm_([p for n,p in trainable],1.0);_require(bool(torch.isfinite(norm)) and float(norm)>0,'nonfinite_or_zero_gradient')
                    lr=CONFIG['learning_rate']*min(1.,(steps+1)/5)*0.5*(1+math.cos(math.pi*steps/max(1,total_steps-1)))
                    for group in optimizer.param_groups:group['lr']=lr
                    step_attempts+=1;optimizer.step();steps+=1;optimizer.zero_grad(set_to_none=True);record.update(optimizer_step=steps,gradient_norm=float(norm),learning_rate=lr)
                with (output/'TRAINING_LOSS.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(record)+'\n')
                _progress(output,{'phase':'optimizing','pid':os.getpid(),'optimizer_steps':steps,'total_optimizer_steps':total_steps,'micro_steps':micro,'elapsed_sec':time.monotonic()-started})
            model.eval();losses=[]
            with torch.no_grad():
                for x in dev:
                    value=float(loss_for(x));_require(math.isfinite(value),'nonfinite_development_loss');losses.append(value)
            mean=sum(losses)/len(losses);checkpoint=output/('epoch_'+str(epoch+1).zfill(2));model.save_pretrained(checkpoint,safe_serialization=True)
            _write(output,'DEVELOPMENT_EPOCH_'+str(epoch+1).zfill(2)+'.json',{'mean_completion_loss':mean,'rows':len(dev),'used_for_gradient_updates':False,'semantic_accuracy':None})
            if mean<best:best=mean;best_path=checkpoint
        _require(steps==total_steps and micro==len(train)*CONFIG['epochs'],'optimization_step_count_mismatch')
        final=output/'adapter';shutil.copytree(best_path,final);set_peft_model_state_dict(model,load_file(str(final/'adapter_model.safetensors'),device='cuda'))
        base_after=fingerprint(False);adapter_after=fingerprint(True)
        _require(base_before==base_after and adapter_before!=adapter_after,'base_changed_or_adapter_not_updated')
        admit_run(dataset,artifacts,runtime,base,base_manifest_ref,protocol_ref)
        _require(_run_files(dataset,code_root)==frozen_files,'frozen_training_inputs_changed')
        proof={'actual_weight_updates':True,'optimizer_steps':steps,'micro_steps':micro,'base_before':base_before,'base_after':base_after,'adapter_before':adapter_before,'adapter_after':adapter_after,
               'best_development_loss':best,'selected_checkpoint':str(best_path),'adapter':str(final),'adapter_files':_files(final),'test_used_for_selection':False,'production_installed':False,
               'semantic_acceptance':False,'elapsed_sec':time.monotonic()-started,'peak_allocated_bytes':torch.cuda.max_memory_allocated()}
        _write(output,'OPTIMIZATION_PROOF.json',proof);_write(output,'TRAINING_COMPLETE.json',{'optimization_complete':True,**proof});return proof
    except BaseException as exc:
        import traceback
        completed=locals().get('steps',0);attempted=locals().get('step_attempts',0)
        _write(output,'FAILED.json',{'admitted':True,'error':repr(exc),'traceback':traceback.format_exc(),'optimizer_steps_completed':completed,
               'optimizer_step_attempts':attempted,'micro_steps':locals().get('micro',0),'model_loaded':'model' in locals(),
               'actual_weight_updates':True if completed else None if attempted else False,'production_installed':False,'elapsed_sec':time.monotonic()-started});raise
