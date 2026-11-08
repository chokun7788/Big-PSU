"""Focused synthetic billing line selection; not a billing semantics proof."""
import json, sys, time
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
W=Path(__file__).resolve().parent
sys.path.insert(0,str(W/'system'))
from app.knowledge.common.domain_flow import financial
from app.knowledge.common.domain_flow.contracts import Plan
def rec(**kw): return {'fields':{k:{'status':'known','value':v} for k,v in kw.items()}}
records={'a':rec(), 'b':rec(), 'svc':rec(platform='Switch'),
         'r1':rec(service_id='svc',audience_id='a',persons_min=1,persons_max=2),
         'r2':rec(service_id='svc',audience_id='a',persons_min=3,persons_max=4),
         'r3':rec(service_id='svc',audience_id='b',persons_min=1,persons_max=1)}
facts=[{'id':i,'record_id':i,'facet':'amount','billing_unit':'per_person'} for i in ('r1','r2','r3')]
index=SimpleNamespace(records=records)
def go():
    with patch.object(financial,'audience_mentions',return_value=({'a','b'},None)), patch.object(financial,'person_counts',return_value={'a':2,'b':1}), patch.object(financial,'unit_calculation',return_value={'amount_thb':50}), patch.object(financial,'title',return_value='audience'):
        return financial.billing(index,'2 people and 1 person',facts)
x=go()
checks={'different_bounds_not_collapsed':isinstance(x,Plan) and x.reason=='per_audience_counts_or_service_required'}
records['r2']['fields']['persons_min']['value']=1
records['r2']['fields']['persons_max']['value']=2
x=go()
checks['same_bounds_preserve_existing_dedup']=isinstance(x,list) and len(x)==2
out=W/('billing_scope_signature_'+str(time.time_ns()));out.mkdir()
report={'checks':checks,'all_passed':all(checks.values()),'scope':'synthetic direct billing selector; no source authority or transaction proof'}
(out/'RESULT.json').write_text(json.dumps(report,indent=2),encoding='utf8')
print(json.dumps({'path':str(out),**report}))
assert report['all_passed']
