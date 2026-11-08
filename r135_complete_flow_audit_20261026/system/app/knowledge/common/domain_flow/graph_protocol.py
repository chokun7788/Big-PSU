"""Versioned planner wire: language plans only, no source/business values."""
import copy,json
from .context_contract import FOCUS,DOMAIN_FACETS,OPERATIONS,SLOTS
VERSION='r129-plan-v2'
SYSTEM=('Interpret the customer request into a source-quoted task graph; do not answer. '
 'Return ONLY one JSON object, with no markdown, YAML, explanation or input echo. '
 'The version string MUST be exactly "r129-plan-v2". Root keys MUST be exactly version, focus, context_quotes, tasks, shared_bindings. '
 'tasks is a JSON array of one to four objects. shared_bindings and constraints are JSON arrays (use [] when empty). '
 'Task ids MUST be "t1", "t2", "t3", "t4" in order, never "1" or numeric 1. '
 'There MUST NOT be a root constraints key; constraints belongs inside each task only. '
 'target MUST be an exact question substring or empty string; never output a field name such as local_date as a target unless those characters were in the question. '
 'A single task quote must contain the whole question, including its requested action and conditions. '
 'Return version, focus, context_quotes, tasks, shared_bindings. Each task has id, quote, domain, operation, facet, target, constraints, ambiguous. '
 'Constraints have slot, quote, source_record_id (empty), scope (local/shared). All quotes are exact input substrings. '
 'Shared bindings have source_task_id,target_task_id,slot,quote,basis (shared_prefix/explicit_anaphor/source_related_ellipsis). '
 'Keep local overrides. Do not broadcast constraints to unrelated tasks. Preserve ambiguity and missing input. '
 'Split factual needs, never style requests. Game/device mentions may be context for booking, eligibility or price. '
 'Never invent IDs, answers, prices, dates not stated, permissions or source authority. '
 'Domains/facets: '+json.dumps(DOMAIN_FACETS,separators=(',',':'))+'. Operations: '+','.join(OPERATIONS)+'. Slots: '+','.join(SLOTS)+'. Focus: '+','.join(FOCUS))
def messages(question):return [{'role':'system','content':SYSTEM},{'role':'user','content':json.dumps({'question':question},ensure_ascii=False,separators=(',',':'))}]

def extend_schema(value):
 value=copy.deepcopy(value);string={'type':'string'}
 value['properties']['version']={'const':VERSION,'type':'string'}
 task=value['properties']['tasks']['items'];task['properties']['id']={'type':'string','enum':['t1','t2','t3','t4']};task['required'].append('id')
 slot=task['properties']['constraints']['items'];slot['properties']['scope']={'type':'string','enum':['local','shared']};slot['required'].append('scope')
 edge={'type':'object','properties':{'source_task_id':string,'target_task_id':string,'slot':{'type':'string','enum':SLOTS+['target']},'quote':string,'basis':{'type':'string','enum':['shared_prefix','explicit_anaphor','source_related_ellipsis']}},'required':['source_task_id','target_task_id','slot','quote','basis'],'additionalProperties':False}
 value['properties']['shared_bindings']={'type':'array','maxItems':24,'items':edge}
 value['required']=['version','focus','context_quotes','tasks','shared_bindings']
 return value
def adapt(value,question):
 if value.get('version')!=VERSION:return value,{'wire_version':'r121-meaning-wire','adapter':'explicit_legacy_wire_adapter'}
 if set(value)!={'version','focus','context_quotes','tasks','shared_bindings'}:raise ValueError('graph_root_fields')
 tasks=value['tasks'];ids=[t.get('id') for t in tasks]
 if not 1<=len(tasks)<=4 or len(set(ids))!=len(ids):raise ValueError('graph_task_ids')
 output=[]
 for i,t in enumerate(tasks):
  if t.get('id')!=f't{i+1}':raise ValueError('graph_task_order')
  expected={'id','quote','domain','operation','facet','target','constraints','ambiguous'}
  if set(t)!=expected:raise ValueError('graph_task_fields')
  t=copy.deepcopy(t);t.pop('id')
  for c in t['constraints']:
   if c.get('scope') not in {'local','shared'}:raise ValueError('graph_slot_scope')
   c.pop('scope')
  output.append(t)
 if not isinstance(value['shared_bindings'],list) or len(value['shared_bindings'])>24:raise ValueError('graph_binding_count')
 for edge in value['shared_bindings']:
  if set(edge)!={'source_task_id','target_task_id','slot','quote','basis'}:raise ValueError('graph_binding_fields')
  if edge['source_task_id'] not in ids or edge['target_task_id'] not in ids or ids.index(edge['source_task_id'])>=ids.index(edge['target_task_id']):raise ValueError('graph_binding_direction')
  if edge['quote'] not in question or not edge['quote'] or edge['slot'] not in set(SLOTS)|{'target'}:raise ValueError('graph_binding_quote')
  if edge['basis'] not in {'shared_prefix','explicit_anaphor','source_related_ellipsis'}:raise ValueError('graph_binding_basis')
 return {'focus':value['focus'],'context_quotes':value['context_quotes'],'tasks':output},{'wire_version':VERSION,'adapter':'validated_graph_wire','proposed_shared_bindings':copy.deepcopy(value['shared_bindings'])}
