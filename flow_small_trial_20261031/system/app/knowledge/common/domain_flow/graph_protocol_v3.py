"""Explicit future protocol: play-service periods have their own language facet.

This codec is not selected by the retained model gateway, training consumer or
cached v2 replay. No model is claimed to have learned or produced this wire.
"""
import copy,json
from . import graph_protocol as v2
from .context_contract import DOMAIN_FACETS,FOCUS,OPERATIONS,SLOTS,validate
from .understanding import DOMAINS,MeaningTask,Understanding

VERSION='r135-plan-v3'
FACETS=copy.deepcopy(DOMAIN_FACETS);FACETS['schedule']+=' service_periods'
FOCUS_CHOICES=[*FOCUS,'service_periods']
SYSTEM=(v2.SYSTEM.partition('Domains/facets: ')[0].replace(v2.VERSION,VERSION)+
 'service_periods means recorded named play-service sessions and their states. '
 'It is distinct from physical open_periods, bookable_periods, maintenance_periods and live occupancy. '
 'Ask for all relevant recorded days when no day is stated; do not invent a day, time or availability. '
 'Use schedule/list/service_periods for named play-session time requests. '
 'No venue times or business answers belong in this language plan. '
 'Domains/facets: '+json.dumps(FACETS,separators=(',',':'))+'. Operations: '+','.join(OPERATIONS)+'. Slots: '+','.join(SLOTS)+'. Focus: '+','.join(FOCUS_CHOICES))

def messages(question):return [{'role':'system','content':SYSTEM},{'role':'user','content':json.dumps({'question':question},ensure_ascii=False,separators=(',',':'))}]

def schema():
    from .understanding import schema as v2_schema
    value=copy.deepcopy(v2_schema())
    value['properties']['version']['const']=VERSION
    value['properties']['focus']['enum']=list(FOCUS_CHOICES)
    value['properties']['tasks']['items']['properties']['facet']['enum'].append('service_periods')
    return value

def adapt(value,question):
    if not isinstance(value,dict) or value.get('version')!=VERSION:raise ValueError('explicit_v3_wire_version_required')
    # The unchanged graph shape adapter checks IDs, direction and raw binding
    # spans. Only its version discriminator is bridged, never a semantic facet.
    shape=copy.deepcopy(value);shape['version']=v2.VERSION
    result,receipt=v2.adapt(shape,question)
    valid,reason=validate(result,question,domain_facets=FACETS,focus_choices=FOCUS_CHOICES)
    if not valid:raise ValueError('v3_'+reason)
    if len(result['tasks'])==1 and result['tasks'][0]['quote']!=question:raise ValueError('v3_single_task_must_retain_whole_request')
    receipt.update(wire_version=VERSION,adapter='explicit_v3_graph_shape_adapter',shape_adapter_version=v2.VERSION,
                   semantic_facet_rewritten=False,model_training_or_generation_proven=False)
    return result,receipt

def parse(content,question):
    from ..registry import Draft202012Validator
    if not isinstance(content,str):return Understanding(reason='invalid_v3_wire_json')
    try:
        if len(content)>131072 or len(content.encode('utf8'))>131072:raise ValueError('v3_payload_too_large')
        def unique(pairs):
            result={}
            for key,value in pairs:
                if key in result:raise ValueError('duplicate_v3_json_key')
                result[key]=value
            return result
        value=json.loads(content,object_pairs_hook=unique)
        if list(Draft202012Validator(schema()).iter_errors(value)):raise ValueError('invalid_v3_schema')
        result,receipt=adapt(value,question)
        tasks=[MeaningTask(t['quote'],t['domain'],DOMAINS[t['domain']][0],t['operation'],t['facet'],t['target'],t['constraints'],t['ambiguous']) for t in result['tasks']]
    except (ValueError,TypeError,KeyError,AttributeError,RecursionError,UnicodeError):return Understanding(reason='invalid_v3_wire_proposal')
    return Understanding(tasks,True,'validated_explicit_v3_proposal',{'http_attempted':False,'model_called':False,
                         'context_focus':result['focus'],'context_quotes':copy.deepcopy(result['context_quotes']),**receipt})
