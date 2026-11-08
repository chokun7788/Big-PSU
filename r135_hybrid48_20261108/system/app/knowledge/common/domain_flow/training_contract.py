"""Artifact-bound training admission; recorded review is not semantic truth.

Only accepted, individually adjudicated language plans enter optimization.
Unreviewed rows stay visible and block readiness of the declared inventory.
No optimizer, model loading, network or business data mutation occurs here.
"""
import copy,hashlib,json,re,unicodedata
from pathlib import Path
from ..registry import Draft202012Validator
from .graph_protocol import VERSION as WIRE_VERSION,messages,adapt
from .understanding import schema
from .context_contract import validate
from .training_input import planner_question,IMPLEMENTATION_SHA256 as INPUT_IMPLEMENTATION_SHA256

VERSION='r135-training-v1'
# Split decisions delegate to this module; pin both implementations so a
# changed helper cannot silently reuse an older admitted dataset/runtime.
_IMPLEMENTATION_FILES=(Path(__file__),Path(__file__).with_name('semantic_family_plan.py'))
IMPLEMENTATION_SHA256=hashlib.sha256(b'\0'.join(p.name.encode('utf8')+b'\0'+hashlib.sha256(p.read_bytes()).digest() for p in _IMPLEMENTATION_FILES)).hexdigest()
CRITERIA=('needs_and_style','intent_operation_facet','entities_and_slot_roles','local_shared_history_scope','negation_and_ambiguity','source_version_alignment','no_business_answer_target')
EXAMPLE_FIELDS={'question_key','family','original_families','split','raw_question','allowed_context','contract_version','plan_label','annotation_provenance','messages','exposure'}
SPLITS={'train','development','holdout','retained_evaluation'}

def digest(value):return hashlib.sha256(json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode('utf8')).hexdigest()
def file_sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def example_sha(example):
    # Semantic review binds the label/input/family/origin. Packing, exposure and
    # split have independent gates plus an exact full-file freeze; repacking an
    # unchanged reviewed label does not invent another semantic adjudication.
    fields=['question_key','family','original_families','raw_question','allowed_context','contract_version','plan_label']
    value={key:example.get(key) for key in fields};origin=example.get('annotation_provenance',{})
    value['annotation_origin']={key:origin.get(key) for key in ['method','origin_ref']}
    return digest(value)

class ArtifactError(ValueError):pass

class Artifacts:
    def __init__(self,*roots):self.roots=[Path(p).resolve() for p in roots];self._cache=None;self._identities={}
    def read(self,ref):
        if not isinstance(ref,dict) or not {'path','sha256'}<=set(ref) or not re.fullmatch('[0-9a-f]{64}',str(ref.get('sha256',''))):raise ArtifactError('artifact_reference_required')
        p=Path(ref['path']);p=(self.roots[0]/p).resolve() if not p.is_absolute() else p.resolve()
        if not any(p==root or root in p.parents for root in self.roots):raise ArtifactError('artifact_outside_declared_roots')
        if not p.is_file():raise ArtifactError('artifact_missing')
        if self._cache is not None and p in self._cache:
            actual,data=self._cache[p]
        else:
            data=p.read_bytes();actual=hashlib.sha256(data).hexdigest()
            if self._cache is not None:self._cache[p]=(actual,data)
        if actual!=ref['sha256']:raise ArtifactError('artifact_hash_changed')
        try:
            if 'line' in ref:
                n=ref['line']
                if type(n) is not int or n<1:raise ArtifactError('artifact_line_invalid')
                value=json.loads(data.decode('utf8').splitlines()[n-1])
            else:value=json.loads(data.decode('utf8'))
            pointer=ref.get('pointer','')
            if pointer and (not isinstance(pointer,str) or not pointer.startswith('/')):raise ArtifactError('artifact_pointer_invalid')
            for token in pointer.split('/')[1:] if pointer else []:
                token=token.replace('~1','/').replace('~0','~');value=value[int(token)] if isinstance(value,list) else value[token]
            return value
        except (ValueError,IndexError,KeyError,TypeError,UnicodeError) as exc:raise ArtifactError('artifact_content_unreadable') from exc

    def source_digest(self,ref):
        key=digest(ref)
        if self._cache is not None and key in self._identities:return self._identities[key]
        value=digest(source_identity(self.read(ref)))
        if self._cache is not None:self._identities[key]=value
        return value

    def verify_pinned_files(self):
        for path,(expected,_) in (self._cache or {}).items():
            if not path.is_file() or file_sha(path)!=expected:raise ArtifactError('artifact_changed_during_admission')

def source_identity(snapshot):
    records=snapshot.get('release',{}).get('records');sources=snapshot.get('source_pairs')
    if not isinstance(records,dict) or not isinstance(sources,dict) or type(snapshot.get('epoch')) is not int:raise ArtifactError('pinned_source_snapshot_required')
    if any(r.get('record_id')!=rid or type(r.get('revision')) is not int for rid,r in records.items()):raise ArtifactError('source_record_identity_invalid')
    return {'release_id':snapshot.get('active'),'epoch':snapshot['epoch'],'records':{rid:{'revision':r['revision'],'sha256':digest(r)} for rid,r in records.items()},'sources':{sid:digest(pair) for sid,pair in sources.items()}}

def protocol(version):
    if version==WIRE_VERSION:return {'version':WIRE_VERSION,'schema':schema,'messages':messages,'adapt':adapt,'validate':validate}
    if version=='r135-plan-v3':
        from . import graph_protocol_v3 as v3
        return {'version':v3.VERSION,'schema':v3.schema,'messages':v3.messages,'adapt':v3.adapt,
                'validate':lambda value,question:validate(value,question,domain_facets=v3.FACETS,focus_choices=v3.FOCUS_CHOICES)}
    raise ArtifactError('explicit_supported_training_wire_version_required')

def protocol_implementation_sha(version):
    here=Path(__file__).parent
    names=['graph_protocol.py','context_contract.py','understanding.py']
    if version=='r135-plan-v3':names.append('graph_protocol_v3.py')
    return digest({name:file_sha(here/name) for name in names})

def runtime_contract(tokenizer_config,*,chat_template=None,template_options=None,model_profile=None,wire_version=WIRE_VERSION):
    if not isinstance(tokenizer_config,dict):raise ArtifactError('actual_tokenizer_configuration_required')
    template=chat_template if chat_template is not None else tokenizer_config.get('chat_template')
    if not template:raise ArtifactError('actual_chat_template_required')
    if not isinstance(model_profile,dict) or not {'base_repository','base_revision','precision','selector_profile','generic_profile'}<=set(model_profile):raise ArtifactError('declared_model_profile_required')
    options=template_options or {'tokenize':False,'add_generation_prompt':True,'enable_thinking':False}
    wire=protocol(wire_version)
    return {'version':VERSION,'wire_version':wire_version,'schema_sha256':digest(wire['schema']()),'system_prompt_sha256':digest(wire['messages']('')[0]),'planner_protocol_implementation_sha256':protocol_implementation_sha(wire_version),'tokenizer_config_sha256':digest(tokenizer_config),'chat_template_sha256':digest(template),'template_options':copy.deepcopy(options),'completion_template_options':{**options,'add_generation_prompt':False},'model_profile':copy.deepcopy(model_profile or {}),'admission_implementation_sha256':IMPLEMENTATION_SHA256,'training_input_implementation_sha256':INPUT_IMPLEMENTATION_SHA256}

def migrated_review_view(example,review,artifacts):
    """Reuse an existing semantic review only after a version-only replay.

    This is a packing/protocol bridge, not another individual adjudication.
    A changed facet, quote, role, context or provenance requires a new review.
    """
    ref=example.get('annotation_provenance',{}).get('wire_migration_ref')
    if ref is None:return example
    record=artifacts.read(ref)
    required={'kind','from_version','to_version','original_example_ref','original_review_ref','original_example_sha256','migrated_example_sha256'}
    if not isinstance(record,dict) or set(record)!=required or record['kind']!='structural_wire_version_migration':raise ArtifactError('wire_migration_record_invalid')
    if record['from_version']!=WIRE_VERSION or record['to_version']!='r135-plan-v3' or example.get('contract_version')!=record['to_version']:raise ArtifactError('wire_migration_version_invalid')
    original=artifacts.read(record['original_example_ref']);prior=artifacts.read(record['original_review_ref'])
    if prior!=review or prior.get('adjudication_status') not in {'accepted','corrected'}:raise ArtifactError('wire_migration_prior_review_not_accepted')
    if original.get('contract_version')!=WIRE_VERSION or original.get('plan_label',{}).get('version')!=WIRE_VERSION:raise ArtifactError('wire_migration_original_version_invalid')
    expected=copy.deepcopy(original);expected['contract_version']=record['to_version'];expected['plan_label']['version']=record['to_version']
    if record['original_example_sha256']!=example_sha(original) or record['migrated_example_sha256']!=example_sha(example) or example_sha(expected)!=example_sha(example):raise ArtifactError('wire_migration_semantic_change_requires_individual_review')
    ignored={'runtime_contract_sha256','wire_migration_ref','semantic_family_move_ref'}
    provenance=lambda row:{k:v for k,v in row.get('annotation_provenance',{}).items() if k not in ignored}
    if provenance(original)!=provenance(example):raise ArtifactError('wire_migration_origin_provenance_changed')
    saved=Path(original.get('annotation_provenance',{}).get('origin_ref',{}).get('path','')).stem
    expected_split='train' if saved=='train' else 'development'
    move_ref=example.get('annotation_provenance',{}).get('semantic_family_move_ref')
    if move_ref is not None:
        # Replay the complete pinned group against its original v3 rows. This
        # permits only reviewed train-to-development moves; semantic coverage
        # and the eventual protocol freeze remain separate mandatory gates.
        from .semantic_family_plan import apply_reviewed_family_moves
        group=artifacts.read(move_ref)
        group_examples=[artifacts.read(m['example_ref']) for m in group['members']]
        planned,moves=apply_reviewed_family_moves(group_examples,[move_ref],artifacts)
        matches=[x for x in planned if x['question_key']==example['question_key']]
        if len(matches)!=1 or not any(m['question_key']==example['question_key'] for m in moves) or example_sha(matches[0])!=example_sha(example) or matches[0]['annotation_provenance']['origin_ref']!=example['annotation_provenance']['origin_ref'] or matches[0]['exposure']!=example['exposure']:
            raise ArtifactError('wire_migration_family_move_mismatch')
        expected_split='development'
    if example.get('split')!=expected_split:raise ArtifactError('wire_migration_saved_file_split_mismatch')
    return original

def _review_binding(example,review,artifacts,expected_source,effective_question=None):
    try:example=migrated_review_view(example,review,artifacts)
    except (ArtifactError,KeyError,TypeError,ValueError) as exc:return [str(exc)],None
    issues=[];bound=example_sha(example);key=example.get('question_key')
    if not isinstance(review,dict):return ['individual_review_record_missing'],None
    if review.get('version')!=VERSION or review.get('question_key')!=key or review.get('example_sha256')!=bound:issues.append('review_not_bound_to_exact_example')
    reviewer=review.get('reviewer',{})
    if reviewer.get('kind') not in {'human','agent'} or not reviewer.get('id'):issues.append('individual_reviewer_identity_required')
    if review.get('review_method')!='individual_source_adjudication':issues.append('heuristic_or_generic_review_not_adjudication')
    state=review.get('adjudication_status')
    if state not in {'accepted','corrected','quarantined'}:issues.append('individual_adjudication_unresolved')
    try:
        source=artifacts.read(review.get('source_version'))
        if artifacts.source_digest(review.get('source_version'))!=expected_source:issues.append('review_source_version_not_expected_snapshot')
        evidence=artifacts.read(review.get('adjudication_ref'))
        if any(evidence.get(k)!=v for k,v in [('question_key',key),('example_sha256',bound),('adjudication_status',state),('reviewer',reviewer),('source_identity_sha256',expected_source)]):issues.append('adjudication_artifact_binding_mismatch')
        unresolved=review.get('unresolved_issues')
        if not isinstance(unresolved,list) or evidence.get('unresolved_issues')!=unresolved:issues.append('explicit_unresolved_issue_inventory_required')
        elif state in {'accepted','corrected'} and any(not isinstance(issue,dict) or issue.get('scope')!='answer_source' or not issue.get('reason') or not issue.get('handling') for issue in unresolved):issues.append('unresolved_label_issue_cannot_be_optimized')
        if state=='quarantined':
            if not evidence.get('quarantine_reason') or review.get('quarantine_reason')!=evidence['quarantine_reason']:issues.append('quarantine_reason_required')
        else:
            criteria=evidence.get('criteria',{});raw=example.get('raw_question','')
            if set(criteria)!=set(CRITERIA):issues.append('individual_review_criteria_incomplete')
            for criterion in CRITERIA:
                decision=criteria.get(criterion,{})
                if decision.get('status')!='passed' or not decision.get('reason'):issues.append('review_criterion_unresolved:'+criterion)
                quotes=decision.get('raw_quotes',[])
                if not quotes or any(not isinstance(q,str) or not q or q not in raw for q in quotes):issues.append('review_criterion_input_evidence_missing:'+criterion)
                for rid in decision.get('source_record_ids',[]):
                    if rid not in source['release']['records']:issues.append('review_criterion_source_record_missing:'+criterion)
        origin=example.get('annotation_provenance',{})
        traces=review.get('teacher_trace_refs')
        if origin.get('method')=='teacher_plan':
            if review.get('teacher_status')!='recorded' or not traces:issues.append('actual_teacher_trace_required')
            for ref in traces or []:
                trace=artifacts.read(ref)
                if trace.get('question_key')!=key or not isinstance(trace.get('plan'),dict) or not trace.get('source_version'):issues.append('teacher_trace_identity_or_source_missing')
                else:
                    receipt=artifacts.read(trace.get('inference_receipt_ref'))
                    identity=receipt.get('model_identity',{});request=receipt.get('request',{});response=receipt.get('response',{})
                    try:raw_request=json.loads(request['messages'][-1]['content']);raw_plan=json.loads(response['content'])
                    except (KeyError,ValueError,TypeError,IndexError):raw_request={};raw_plan=None
                    if receipt.get('status')!='success' or receipt.get('question_key')!=key or not receipt.get('request_id') or receipt.get('request_id')!=receipt.get('response_request_id') or raw_request.get('question')!=(effective_question if effective_question is not None else example.get('raw_question')) or raw_plan!=trace['plan']:issues.append('teacher_receipt_not_same_successful_question_and_plan')
                    if receipt.get('stage')!='context_understanding' or request.get('planner_profile')!=identity.get('profile'):issues.append('teacher_receipt_stage_or_profile_mismatch')
                    if not re.fullmatch(r'[0-9a-f]{40}|[0-9a-f]{64}',str(identity.get('base_revision',''))) or not identity.get('backend') or not identity.get('precision') or identity.get('profile')!='base' and not re.fullmatch('[0-9a-f]{64}',str(identity.get('adapter_sha256',''))):issues.append('actual_teacher_model_provenance_required')
                    teacher_source=artifacts.source_digest(trace['source_version'])
                    alignment=review.get('teacher_source_alignment')
                    if alignment not in {'same_source','adjudicated_source_change'} or alignment=='same_source' and teacher_source!=expected_source:issues.append('teacher_current_source_alignment_unresolved')
                    if alignment=='adjudicated_source_change' and evidence.get('teacher_source_identity_sha256')!=teacher_source:issues.append('changed_teacher_source_not_adjudicated')
        elif origin.get('method')=='manual_review_of_saved_question':
            if traces!=[] or review.get('teacher_status')!='not_applicable':issues.append('manual_origin_must_not_invent_teacher_trace')
        else:issues.append('label_origin_not_reviewed_manual_or_teacher')
    except ArtifactError as exc:issues.append(str(exc))
    return sorted(set(issues)),state

def admit(example,review,artifacts,source_ref,runtime):
    issues=[];state=None
    if not isinstance(example,dict):return {'eligible':False,'inventory_adjudicated':False,'issues':['training_example_object_required']}
    if not isinstance(review,dict):return {'eligible':False,'inventory_adjudicated':False,'issues':['individual_review_record_missing'],'semantic_truth_verified_by_gate':False}
    if set(example)!=EXAMPLE_FIELDS:issues.append('training_example_fields')
    raw=example.get('raw_question');label=example.get('plan_label');effective=raw
    try:
        source=artifacts.source_digest(source_ref)
        origin=artifacts.read(example.get('annotation_provenance',{}).get('origin_ref'))
        if origin.get('key',origin.get('question_key'))!=example.get('question_key') or origin.get('question',origin.get('raw_question'))!=raw:issues.append('origin_question_identity_mismatch')
        effective=planner_question(example,origin,artifacts,source_ref)
        binding,state=_review_binding(example,review,artifacts,source,effective);issues+=binding
        original={str(origin[k]) for k in ['family','review_family'] if origin.get(k)}
        if not original<=set(example.get('original_families',[])):issues.append('original_or_review_family_dropped')
    except (ArtifactError,ValueError,TypeError,KeyError,AttributeError) as exc:issues.append(str(exc))
    if issues:return {'eligible':False,'inventory_adjudicated':False,'issues':sorted(set(issues)),'adjudication_status':state,'semantic_truth_verified_by_gate':False}
    if state=='quarantined':return {'eligible':False,'inventory_adjudicated':True,'issues':['individually_quarantined'],'adjudication_status':state,'semantic_truth_verified_by_gate':False}
    if not isinstance(raw,str) or not raw.strip() or not example.get('question_key') or not example.get('family'):issues.append('question_key_family_and_raw_required')
    if not isinstance(example.get('original_families'),list) or not example['original_families']:issues.append('original_family_provenance_required')
    if example.get('split') not in SPLITS:issues.append('unknown_training_split')
    if example.get('exposure') not in {'unseen','retained','development'}:issues.append('exposure_history_required')
    if example.get('split')=='holdout' and example.get('exposure')!='unseen':issues.append('exposed_holdout_must_be_development_or_retained_evaluation')
    try:wire=protocol(runtime.get('wire_version'))
    except ArtifactError as exc:return {'eligible':False,'inventory_adjudicated':False,'issues':[str(exc)],'semantic_truth_verified_by_gate':False}
    if example.get('contract_version')!=wire['version'] or runtime.get('schema_sha256')!=digest(wire['schema']()) or runtime.get('system_prompt_sha256')!=digest(wire['messages']('')[0]):issues.append('current_wire_schema_prompt_mismatch')
    saved_split=Path(example.get('annotation_provenance',{}).get('origin_ref',{}).get('path','')).stem
    if wire['version']=='r135-plan-v3' and saved_split in {'validation','test'} and example.get('split')=='train':issues.append('historical_evaluation_file_cannot_be_v3_training')
    if runtime.get('planner_protocol_implementation_sha256')!=protocol_implementation_sha(wire['version']):issues.append('current_planner_protocol_implementation_mismatch')
    if runtime.get('admission_implementation_sha256')!=IMPLEMENTATION_SHA256:issues.append('current_admission_implementation_mismatch')
    if runtime.get('training_input_implementation_sha256')!=INPUT_IMPLEMENTATION_SHA256:issues.append('current_history_input_implementation_mismatch')
    if example.get('messages')!=wire['messages'](effective)+[{'role':'assistant','content':json.dumps(label,ensure_ascii=False,separators=(',',':'))}]:issues.append('exact_current_training_messages_required')
    if example.get('annotation_provenance',{}).get('runtime_contract_sha256')!=digest(runtime):issues.append('tokenizer_template_or_model_profile_contract_mismatch')
    try:
        errors=list(Draft202012Validator(wire['schema']()).iter_errors(label))
        if errors:issues.append('plan_label_outside_current_language_wire')
        adapted,_=wire['adapt'](label,effective);valid,reason=wire['validate'](adapted,effective)
        if not valid:issues.append('plan_label_'+reason)
        if len(label['tasks'])==1 and label['tasks'][0]['quote']!=effective:issues.append('single_task_must_preserve_entire_planner_input')
    except (ValueError,KeyError,TypeError,AttributeError):issues.append('invalid_plan_label')
    migrated=example.get('annotation_provenance',{}).get('wire_migration_ref') is not None
    return {'eligible':not issues,'inventory_adjudicated':True,'issues':sorted(set(issues)),'adjudication_status':state,'semantic_truth_verified_by_gate':False,'review_acceptance_basis':'pinned_prior_individual_adjudication_and_recomputed_version_only_migration' if migrated else 'pinned_artifacts_and_recorded_individual_adjudication','new_semantic_review_claimed_by_migration':False}

def _audit_dataset(examples,reviews,artifacts,source_ref,runtime,*,expected_keys,known_exposed=()):
    issues=[];keys=[x.get('question_key') for x in examples];review_keys=[x.get('question_key') for x in reviews];index={x.get('question_key'):x for x in reviews};exposed=set(known_exposed)
    if len(keys)!=len(set(keys)):issues.append('duplicate_question_keys')
    if len(review_keys)!=len(set(review_keys)):issues.append('duplicate_review_keys')
    if set(keys)!=set(expected_keys):issues.append('declared_corpus_inventory_mismatch')
    if set(review_keys)-set(keys):issues.append('orphan_review_records')
    decisions=[];groups={};counts={s:0 for s in SPLITS}
    for example in examples:
        decision=admit(example,index.get(example.get('question_key')),artifacts,source_ref,runtime)
        if example.get('question_key') in exposed and (example.get('exposure')=='unseen' or example.get('split')=='holdout'):
            decision['eligible']=False;decision['issues'].append('known_exposed_question_cannot_be_fresh_holdout')
        decisions.append({'question_key':example.get('question_key'),**decision})
        if decision['eligible']:
            counts[example['split']]+=1
            for group in [example['family'],*example['original_families']]:groups.setdefault(group,set()).add(example['split'])
            core=' '.join(unicodedata.normalize('NFKC',example['raw_question']).casefold().split())
            groups.setdefault('normalized_raw:'+digest(core),set()).add(example['split'])
    overlaps={k:sorted(v) for k,v in groups.items() if len(v)>1}
    if overlaps:issues.append('family_crosses_training_development_evaluation')
    inventory=all(d['inventory_adjudicated'] for d in decisions) and set(keys)==set(expected_keys) and not issues
    ready=inventory and counts['train']>0 and counts['development']>0 and not any(not d['eligible'] and d.get('adjudication_status')!='quarantined' for d in decisions)
    return {'version':VERSION,'ready_for_optimization':ready,'inventory_individually_adjudicated':inventory,'rows':decisions,'dataset_issues':issues,'family_overlaps':overlaps,'eligible_split_counts':counts,'source_identity_sha256':artifacts.source_digest(source_ref),'runtime_contract':runtime,'runtime_contract_sha256':digest(runtime),'declared_inventory_sha256':digest(sorted(expected_keys)),'fresh_holdout_claimed':counts['holdout']>0 and ready,'semantic_truth_verified_by_gate':False,'actual_model_inferences':0,'optimizer_started':False}

def audit_dataset(examples,reviews,artifacts,source_ref,runtime,*,expected_keys,known_exposed=()):
    pinned=Artifacts(*artifacts.roots);pinned._cache={}
    report=_audit_dataset(examples,reviews,pinned,source_ref,runtime,expected_keys=expected_keys,known_exposed=known_exposed)
    try:pinned.verify_pinned_files()
    except ArtifactError as exc:
        report['dataset_issues'].append(str(exc));report['ready_for_optimization']=False;report['inventory_individually_adjudicated']=False
    return report

def require_ready(report):
    if report.get('version')!=VERSION or report.get('ready_for_optimization') is not True or report.get('inventory_individually_adjudicated') is not True or report.get('dataset_issues')!=[] or not report.get('rows') or any(not r.get('inventory_adjudicated') or not r.get('eligible') and r.get('adjudication_status')!='quarantined' for r in report['rows']):raise ValueError('training_admission_not_ready')

def prepare_dataset(destination,examples,reviews,artifacts,source_ref,runtime,*,expected_keys,known_exposed=()):
    """Write a new immutable-at-admission bundle, including every rejected row."""
    report=audit_dataset(examples,reviews,artifacts,source_ref,runtime,expected_keys=expected_keys,known_exposed=known_exposed)
    destination=Path(destination);destination.mkdir(exist_ok=False)
    def write(name,value):
        text=''.join(json.dumps(row,ensure_ascii=False)+'\n' for row in value) if name.endswith('.jsonl') else json.dumps(value,ensure_ascii=False,indent=2)+'\n'
        (destination/name).write_text(text,'utf8')
    write('EXAMPLES.jsonl',examples);write('REVIEWS.jsonl',reviews);write('ADMISSION.json',report)
    allowed={r['question_key'] for r in report['rows'] if r['eligible']}
    for split in sorted(SPLITS):write(split+'.jsonl',[e for e in examples if e.get('question_key') in allowed and e.get('split')==split])
    write('QUARANTINE.jsonl',[{'example':e,'decision':d} for e,d in zip(examples,report['rows']) if not d['eligible']])
    files={p.name:file_sha(p) for p in destination.iterdir() if p.is_file()}
    freeze={'version':VERSION,'files':files,'source_ref':source_ref,'runtime_contract_sha256':digest(runtime),'expected_keys':sorted(expected_keys),'known_exposed':sorted(known_exposed),'ready_for_optimization':report['ready_for_optimization'],'historical_sources_modified':False}
    write('DATASET_FREEZE.json',freeze)
    if report['ready_for_optimization']:write('READY_FOR_OPTIMIZATION.json',{'version':VERSION,'freeze_sha256':file_sha(destination/'DATASET_FREEZE.json'),'admission_sha256':file_sha(destination/'ADMISSION.json'),'semantic_truth_verified_by_gate':False})
    return report

def load_admitted_dataset(directory,artifacts,runtime):
    """Consumer gate revalidates the actual rows/artifacts before model loading."""
    directory=Path(directory);freeze=json.loads((directory/'DATASET_FREEZE.json').read_text('utf8'));ready=json.loads((directory/'READY_FOR_OPTIMIZATION.json').read_text('utf8'))
    if freeze.get('version')!=VERSION or ready.get('freeze_sha256')!=file_sha(directory/'DATASET_FREEZE.json') or ready.get('admission_sha256')!=file_sha(directory/'ADMISSION.json') or freeze.get('runtime_contract_sha256')!=digest(runtime):raise ValueError('training_freeze_or_runtime_changed')
    for name,sha in freeze['files'].items():
        path=(directory/name).resolve()
        if path.parent!=directory.resolve() or file_sha(path)!=sha:raise ValueError('training_file_changed:'+name)
    def rows(name):return [json.loads(line) for line in (directory/name).read_text('utf8').splitlines() if line.strip()]
    examples=rows('EXAMPLES.jsonl');reviews=rows('REVIEWS.jsonl');report=audit_dataset(examples,reviews,artifacts,freeze['source_ref'],runtime,expected_keys=freeze['expected_keys'],known_exposed=freeze['known_exposed'])
    require_ready(report)
    if digest(report)!=digest(json.loads((directory/'ADMISSION.json').read_text('utf8'))):raise ValueError('training_admission_replay_changed')
    allowed={r['question_key'] for r in report['rows'] if r['eligible']}
    return {split:[e for e in examples if e['question_key'] in allowed and e['split']==split] for split in SPLITS}
