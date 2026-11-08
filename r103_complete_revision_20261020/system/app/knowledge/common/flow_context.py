"""One request context for planning, corrective reads and live observations."""
from contextvars import ContextVar
from contextlib import contextmanager
from dataclasses import dataclass,field
from uuid import uuid4
import time

CURRENT=ContextVar('common_flow_context',default=None)
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
    def public(self):
        from app.pipeline.request_deadline import current_budget
        b=current_budget()
        return {'request_id':self.request_id,'semantic_attempts':self.semantic_attempts,
          'corrective_reads':self.corrective_reads,'snapshot':self.snapshot,
          'budget':b.metadata() if b else {'global_timeout_enabled':False},'audits':self.audits,'events':self.events,'input':self.input}
@contextmanager
def request_context():
    old=CURRENT.get()
    if old is not None:
        yield old
        return
    token=CURRENT.set(Context())
    try:yield CURRENT.get()
    finally:CURRENT.reset(token)
