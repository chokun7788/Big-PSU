"""Small serializable contracts. Unknown is different from missing input/failure."""
from dataclasses import dataclass,field
from typing import Any

STATUSES=frozenset({'answer','partial','missing_source','missing_input','not_current','unavailable'})

@dataclass
class Plan:
    ids:list[str]=field(default_factory=list)
    status:str='missing_source'
    reason:str='no_confirmed_source'
    category:str=''
    facets:list[str]=field(default_factory=list)
    candidates:list[str]=field(default_factory=list)
    ambiguous:bool=False
    locked:bool=False
    metadata:dict[str,Any]=field(default_factory=dict)

    def __post_init__(self):
        if self.status not in STATUSES:raise ValueError('Unsupported plan status')
        self.ids=list(dict.fromkeys(self.ids))

@dataclass
class RequestBudget:
    max_model_calls:int=2
    model_calls:int=0
    events:list[dict]=field(default_factory=list)
    admission_denials:int=0

    def reserve(self):
        if self.model_calls>=self.max_model_calls:return False
        self.model_calls+=1
        return True

    def cancel_unattempted(self):
        """Return a reservation denied before inference, preserving the call cap."""
        if self.model_calls:self.model_calls-=1
        self.admission_denials+=1
