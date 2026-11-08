"""Request-local compiled IR from the validated legacy planner wire contract.

No business facts or benchmark keys enter compilation. Source spans refer to
the immutable current question; history remains owned by the native binder.
"""
import copy,re
from dataclasses import dataclass,field,asdict
from .capabilities import resolve
from .scope import requested_minutes

VERSION='r123-plan-ir-v1'
TERMINALS={'supported','partial','missing_input','missing_source','conflict','not_current','provider_unavailable','budget_exhausted','unsupported_operation','invalid_plan'}

@dataclass(frozen=True)
class Span:
    start:int
    end:int
    text:str
    def validate(self,question):return 0<=self.start<self.end<=len(question) and question[self.start:self.end]==self.text

def span(question,text,within=None):
    if not text:return None
    lo,hi=(within.start,within.end) if within else (0,len(question))
    pos=question.find(text,lo,hi)
    return Span(pos,pos+len(text),text) if pos>=0 else None

@dataclass
class Slot:
    id:str
    kind:str
    role:str
    source_span:Span
    owner_task_id:str
    normalized_value:object=None
    normalized_unit:str|None=None
    origin:str='current_user'
    scope:str='local'
    source_record_id:str=''

@dataclass
class Binding:
    id:str
    source_task_id:str
    target_task_id:str
    source_span:Span
    basis:str
    inherited_slots:list=field(default_factory=list)
    execution_dependency:bool=False

@dataclass
class Obligation:
    id:str
    kind:str
    task_id:str
    expected:object=None

@dataclass
class CompiledTask:
    id:str
    source_span:Span
    category:str|None
    operation:str
    facet:str
    capability:dict
    target_span:Span|None=None
    target_scope:str='none'
    bound_record_ids:list=field(default_factory=list)
    slots:list=field(default_factory=list)
    bindings:list=field(default_factory=list)
    obligations:list=field(default_factory=list)
    ambiguities:list=field(default_factory=list)
    errors:list=field(default_factory=list)
    canonical_operation:str=''
    source_provenance:list=field(default_factory=list)
    semantic_dependencies:list=field(default_factory=list)
    execution_dependencies:list=field(default_factory=list)

    def validate(self,question):
        if not self.source_span.validate(question):raise ValueError('invalid_task_span')
        if self.target_span and not self.target_span.validate(question):raise ValueError('invalid_target_span')
        for s in self.slots:
            if not s.source_span.validate(question):raise ValueError('invalid_slot_span')
            if s.scope=='local' and not (self.source_span.start<=s.source_span.start<s.source_span.end<=self.source_span.end):raise ValueError('slot_scope_leak')
        for b in self.bindings:
            if not b.source_span.validate(question):raise ValueError('invalid_binding_span')

@dataclass
class CompiledRequest:
    question:str
    snapshot:dict
    tasks:list
    compiler_events:list=field(default_factory=list)
    version:str=VERSION
    wire_version:str='r121-meaning-wire'
    wire_adapter:str='validated_meaning_task_adapter'
    whole_question_semantics_verified:bool=False
    input_basis:str='engine_question_after_native_normalization'
    raw_request_offset_mapping_implemented:bool=False
    shared_bindings:list=field(default_factory=list)
    superseded_slots:list=field(default_factory=list)
    request_context:dict=field(default_factory=dict)

    def as_dict(self):return asdict(self)
    def validate(self):
        if not 1<=len(self.tasks)<=4:raise ValueError('invalid_legacy_task_count')
        ids=[t.id for t in self.tasks]
        if len(ids)!=len(set(ids)):raise ValueError('duplicate_task_id')
        for task in self.tasks:
            task.validate(self.question)
            for b in task.bindings:
                if b.target_task_id!=task.id or b.source_task_id not in [*ids,'request']:raise ValueError('invalid_binding_task')
                if b.source_task_id!='request' and ids.index(b.source_task_id)>=ids.index(task.id):raise ValueError('cyclic_or_forward_reference')

def normalize_duration(index,text,meaning):
    from .meaning_reader import execution_query
    return requested_minutes(execution_query(index,text,meaning))

def compile_request(question,understanding,index,snapshot):
    if not understanding.accepted:return CompiledRequest(question,snapshot,[],[{'reason':'legacy_plan_unaccepted','coverage':'unverified'}])
    tasks=[];events=[]
    for i,meaning in enumerate(understanding.tasks):
        tid=f't{i+1}';quote_span=span(question,meaning.quote)
        if quote_span is None:raise ValueError('unbound_task_quote')
        task=CompiledTask(tid,quote_span,meaning.category,meaning.operation,meaning.facet,resolve(meaning.category,meaning.operation,meaning.facet))
        task.canonical_operation=meaning.canonical_operation or meaning.category+'.'+meaning.facet if meaning.category else 'unresolved'
        if meaning.ambiguous:task.ambiguities.append('legacy_meaning_requires_clarification')
        local=span(question,meaning.target,quote_span)
        if local:task.target_span=local;task.target_scope='local'
        elif meaning.target:
            antecedents=[t for t in tasks if span(question,meaning.target,t.source_span)]
            if antecedents:
                prior=antecedents[-1];target=span(question,meaning.target,prior.source_span)
                audit=understanding.event.get('context_scope_review',[])
                basis=next((a['action'] for a in audit if a.get('task_quote')==meaning.quote and a.get('source_quote')==meaning.target and a['action'] in {'unique_previous_source_named_referent','source_related_service_game_ellipsis','source_related_booking_ellipsis'}),None)
                edge=next((b for b in understanding.event.get('shared_bindings',[]) if b.get('validated') and b['target_task_id']==tid and b['slot_kind']=='target' and b['source_span']['text']==meaning.target),None)
                if edge:basis=edge['basis']
                if basis is None:
                    from .context_guard import named_targets,ANAPHOR
                    names=named_targets(index,prior.source_span.text)
                    if len(names)==1 and names[0]==meaning.target and re.search(ANAPHOR,meaning.quote,re.I):basis='compiler_validated_unique_anaphor'
                if basis:
                    task.target_span=target;task.target_scope='shared'
                    task.bindings.append(Binding(f'b{i+1}',prior.id,tid,target,basis))
                else:task.errors.append('unproven_cross_task_target')
            else:task.errors.append('target_outside_task_without_antecedent')
        if task.target_span:
            task.bound_record_ids=sorted({f['record_id'] for f in index.bind(meaning.category,task.target_span.text)}) if meaning.category else []
        for n,c in enumerate(meaning.constraints):
            source=span(question,c['quote'],quote_span);scope='local'
            if source is None and task.target_scope=='shared' and c['slot'] in {'service','platform'} and c['quote'] in task.target_span.text:
                source=span(question,c['quote'],task.target_span);scope='shared'
            shared=next((b for b in understanding.event.get('shared_bindings',[]) if b.get('validated') and b['target_task_id']==tid and b['slot_kind']==c['slot'] and b['source_span']['text']==c['quote']),None)
            if source is None and shared:
                source=Span(**shared['source_span']);scope='shared'
                bid='b_'+shared['id'];src=shared['source_task_id']
                if src==tid or not any(t.id==src and t.source_span.start<=source.start and source.end<=t.source_span.end for t in tasks):src='request'
                task.bindings.append(Binding(bid,src,tid,source,shared['basis'],[f'{tid}s{n+1}'],False))
                task.semantic_dependencies.append({'binding_id':bid,'source':src,'slot_kind':c['slot']})
            if source is None:
                task.errors.append('unresolved_external_constraint_scope');events.append({'task_id':tid,'quote':c['quote'],'kind':c['slot'],'reason':'external_slot_requires_explicit_scope'})
                continue
            role=c['slot'];value=None;unit=None
            if c['slot']=='duration':
                value=normalize_duration(index,c['quote'],meaning);unit='minute'
                near=question[max(quote_span.start,source.start-12):min(quote_span.end,source.end+16)]
                role='comparison_duration' if meaning.operation=='compare' else 'session_duration' if re.search(r'ต่อรอบ|รอบละ|per session|each session',near,re.I) else 'requested_duration'
            from ..flow_context import CURRENT
            from .scope import norm
            context=CURRENT.get();raw=(context.input.get('raw_question') or context.input.get('normalized_question') or '') if context else question
            origin='current_user' if norm(c['quote']) in norm(raw) else 'derived_execution_slot'
            task.slots.append(Slot(f'{tid}s{n+1}',c['slot'],role,source,tid,value,unit,origin=origin,scope=scope,source_record_id=c.get('source_record_id','')))
        task.obligations.append(Obligation(f'{tid}:answer','task_completion',tid,meaning.facet))
        if task.capability['operation']=='compare_durations':
            values=sorted({s.normalized_value for s in task.slots if s.role=='comparison_duration' and s.normalized_value is not None})
            if len(values)<2:task.ambiguities.append('comparison_requires_distinct_duration_options')
            task.obligations.extend(Obligation(f'{tid}:duration:{v}','duration_option',tid,v) for v in values)
        if task.capability['operation'] in {'list','count','group_count','group_list'}:
            task.obligations.append(Obligation(f'{tid}:set','collection_scope',tid,meaning.operation))
        tasks.append(task)
    result=CompiledRequest(question,snapshot,tasks,events)
    result.version='r129-plan-ir-v2';result.wire_version=understanding.event.get('wire_version','r121-meaning-wire')
    result.shared_bindings=copy.deepcopy(understanding.event.get('shared_bindings',[]));result.superseded_slots=copy.deepcopy(understanding.event.get('superseded_slots',[]))
    from .executor_registry import describe
    from .request_provenance import capture
    from .span_provenance import alignment,resolve_span
    context=capture(question);context['span_map']=alignment(context['raw_question'],question,context.get('derivation'),context.get('trusted_slot_provenance'))
    result.request_context=context;result.raw_request_offset_mapping_implemented=True
    for task in tasks:
        task.capability=describe(task,task.source_span.text)
        task.source_provenance=[{'role':'task','execution_span':asdict(task.source_span),'source':resolve_span(context['span_map'],task.source_span.start,task.source_span.end)}]
        if task.target_span:task.source_provenance.append({'role':'target','execution_span':asdict(task.target_span),'source':resolve_span(context['span_map'],task.target_span.start,task.target_span.end)})
        for binding in task.bindings:task.source_provenance.append({'role':'shared_binding','binding_id':binding.id,'execution_span':asdict(binding.source_span),'source':resolve_span(context['span_map'],binding.source_span.start,binding.source_span.end)})
        for slot in task.slots:task.source_provenance.append({'role':slot.role,'slot_id':slot.id,'execution_span':asdict(slot.source_span),'source':resolve_span(context['span_map'],slot.source_span.start,slot.source_span.end)})
    result.validate();return result

def prepared_meaning(meaning,compiled):
    """Do not mutate the original planner proposal during reader preparation."""
    result=copy.deepcopy(meaning)
    result.ambiguous=bool(meaning.ambiguous or compiled.ambiguities or compiled.errors)
    return result
