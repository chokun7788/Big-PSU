"""One request context for planning, corrective reads and live observations."""
from contextvars import ContextVar
from contextlib import contextmanager
from dataclasses import dataclass,field
from uuid import uuid4
import time,copy,hashlib,json,os

CURRENT=ContextVar('common_flow_context',default=None)

class PinnedInput(dict):
    """Allow audit enrichment while preserving the original question."""
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        if 'raw_question' in self and not isinstance(self['raw_question'],str):raise ValueError('raw_question_must_be_text')
    def __setitem__(self,key,value):
        if key=='raw_question':
            if not isinstance(value,str):raise ValueError('raw_question_must_be_text')
            if key in self and value!=self[key]:raise ValueError('raw_question_is_immutable')
        super().__setitem__(key,value)
    def __delitem__(self,key):
        if key=='raw_question' and key in self:raise ValueError('raw_question_is_immutable')
        super().__delitem__(key)
    def update(self,*args,**kwargs):
        values=dict(*args,**kwargs)
        if 'raw_question' in values and 'raw_question' in self and values['raw_question']!=self['raw_question']:raise ValueError('raw_question_is_immutable')
        for key,value in values.items():self[key]=value
    def setdefault(self,key,default=None):
        if key not in self:self[key]=default
        return self[key]
    def pop(self,key,*default):
        if key=='raw_question' and key in self:raise ValueError('raw_question_is_immutable')
        return super().pop(key,*default)
    def clear(self):
        if 'raw_question' in self:raise ValueError('raw_question_is_immutable')
        return super().clear()
    def popitem(self):
        if self and next(reversed(self))=='raw_question':raise ValueError('raw_question_is_immutable')
        return super().popitem()
    def __ior__(self,other):self.update(other);return self

@dataclass
class Context:
    request_id:str=field(default_factory=lambda:uuid4().hex)
    started:float=field(default_factory=time.perf_counter)
    semantic_attempts:int=0
    corrective_reads:int=0
    live:dict=field(default_factory=dict)
    audits:list=field(default_factory=list)
    snapshot:dict=field(default_factory=dict)
    events:list=field(default_factory=list)
    input:dict=field(default_factory=dict)
    model_calls_reserved:int=0
    model_calls_attempted:int=0
    model_calls_transport_completed:int=0
    max_model_calls:int=2
    reference_time_value:object=None
    validated_derivations:dict=field(default_factory=dict)
    parent_execution_scopes:dict=field(default_factory=dict)
    def __setattr__(self,name,value):
        if name=='request_id' and name in self.__dict__ and value!=self.__dict__[name]:raise ValueError('request_id_is_immutable')
        if name=='reference_time_value' and self.__dict__.get(name) is not None and value!=self.__dict__[name]:raise ValueError('request_reference_time_is_immutable')
        if name=='input':
            previous=self.__dict__.get('input',{})
            if 'raw_question' in previous and (not isinstance(value,dict) or value.get('raw_question')!=previous['raw_question']):raise ValueError('raw_question_is_immutable')
            value=PinnedInput(value)
        object.__setattr__(self,name,value)
    def __delattr__(self,name):
        if name=='input' and 'raw_question' in self.input:raise ValueError('raw_question_is_immutable')
        object.__delattr__(self,name)
    def reserve_model(self,stage):
        accepted=self.model_calls_reserved<self.max_model_calls
        if accepted:self.model_calls_reserved+=1
        self.event('R129_budget_ledger',model_stage=stage,accepted=accepted,reserved_calls=self.model_calls_reserved,max_calls=self.max_model_calls,reason=None if accepted else 'budget_exhausted')
        return accepted
    def event(self,stage,**detail):
        if len(self.events)<400:self.events.append({'stage':stage,'elapsed_ms':round((time.perf_counter()-self.started)*1000,3),**detail})
    def reserve_semantic(self):
        if self.semantic_attempts:return False
        self.semantic_attempts+=1
        return True
    def reserve_corrective(self):
        if self.corrective_reads:return False
        self.corrective_reads+=1
        return True
    def pin_reference_time(self,value=None):
        from .domain_flow.scope import reference_time
        if self.reference_time_value is not None:
            if value is not None and reference_time(value)!=self.reference_time_value:raise ValueError('request_reference_time_mismatch')
            return self.reference_time_value
        if value is None:
            from app.calendar.service_calendar import now_bangkok
            value=now_bangkok()
        self.reference_time_value=reference_time(value)
        self.event('request_reference_time_pinned',reference_time=self.reference_time_value.isoformat(),timezone='Asia/Bangkok')
        return self.reference_time_value
    def bind_snapshot(self,snapshot):
        release=snapshot.get('release') or snapshot
        records=release.get('records',{});sources=release.get('sources',{})
        manifest={'release_id':snapshot.get('active',snapshot.get('release_id')),'epoch':snapshot.get('epoch'),
          'record_revisions':{rid:r.get('revision') for rid,r in records.items()},
          'source_revisions':{sid:s.get('sha256') for sid,s in sources.items()},'withdrawn_record_ids':sorted(snapshot.get('withdrawn',[]))}
        digest=hashlib.sha256(json.dumps(manifest,sort_keys=True,separators=(',',':')).encode()).hexdigest()
        manifest.update(manifest_sha256=digest,reference_time=self.pin_reference_time().isoformat())
        if self.snapshot.get('manifest_sha256')!=digest:
            self.event('request_snapshot_bound',release_id=manifest['release_id'],epoch=manifest['epoch'],manifest_sha256=digest,
              previous_snapshot=({k:self.snapshot.get(k) for k in ['release_id','epoch','manifest_sha256']} if self.snapshot else None),previous_claims_must_be_invalidated=bool(self.snapshot))
        self.snapshot=manifest
        return manifest
    def identity(self):
        from .build_info import LOADED_BUILD
        observations=[]
        for event in self.events:
            if event.get('stage')!='R129_model_gateway':continue
            requested=event.get('model',event.get('requested_model'));returned=event.get('returned_model')
            observations.append({'stage':event.get('model_stage'),'requested_model':requested,'returned_model':returned,
              'requested_profile':event.get('profile'),'transport_ok':event.get('transport_ok',False),
              'response_model_name_verified':bool(returned and returned==requested),'returned_provenance':copy.deepcopy(event.get('returned_provenance',{}))})
        return {'locale':{'requested':self.input.get('requested_locale',self.input.get('locale')),'effective':self.input.get('effective_locale',self.input.get('locale'))},
          'reference_time':{'value':self.reference_time_value.isoformat() if self.reference_time_value is not None else None,'timezone':'Asia/Bangkok','pinned':self.reference_time_value is not None},
          'runtime_identity':copy.deepcopy(LOADED_BUILD),
          'model_profile':{'state':'observed' if observations else 'attempted_without_receipt' if self.model_calls_attempted else 'not_called',
            'requested_context_profile':os.getenv('PSU_PLANNER_PROFILE','retained'),'non_context_profile':'base','observations':observations,'asset_identity_not_inferred_from_alias':True}}
    def public(self):
        from app.pipeline.request_deadline import current_budget
        b=current_budget()
        return {'request_id':self.request_id,'semantic_attempts':self.semantic_attempts,'model_calls_reserved':self.model_calls_reserved,'model_calls_attempted':self.model_calls_attempted,'model_calls_transport_completed':self.model_calls_transport_completed,'max_model_calls':self.max_model_calls,
          'corrective_reads':self.corrective_reads,'snapshot':self.snapshot,
          'budget':b.metadata() if b else {'global_timeout_enabled':False},'audits':self.audits,'events':self.events,'input':self.input,**self.identity()}
@contextmanager
def request_context():
    old=CURRENT.get()
    if old is not None:
        yield old
        return
    token=CURRENT.set(Context())
    try:yield CURRENT.get()
    finally:CURRENT.reset(token)

def request_reference_time(value=None):
    ctx=CURRENT.get()
    if ctx is not None:return ctx.pin_reference_time(value)
    from .domain_flow.scope import reference_time
    return reference_time(value)
