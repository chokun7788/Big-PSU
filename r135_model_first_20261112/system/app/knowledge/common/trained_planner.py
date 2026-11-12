"""Retained training wire, literal validation, one bounded plan review.

Independent observations challenge plans; they never create executor tasks.
No source answer, hidden native intent correction, training or live reset.
"""
import json,os,types
from .domain_flow.context_contract import messages,validate,FOCUS
from .domain_flow.understanding import _native_schema,_native_parse

def schema():
 value=_native_schema(())
 value['properties'].update(focus={'type':'string','enum':FOCUS},context_quotes={'type':'array','maxItems':12,'items':{'type':'string'}})
 value['required']=['focus','context_quotes','tasks']
 return value

def parse(content,question):
 def unique(pairs):
  result={}
  for key,value in pairs:
   if key in result:raise ValueError('duplicate_planner_json_key')
   result[key]=value
  return result
 if not isinstance(content,str) or len(content.encode())>131072:raise ValueError('planner_payload_limit')
 value=json.loads(content,object_pairs_hook=unique)
 valid,reason=validate(value,question)
 if not valid:raise ValueError('retained_wire_'+reason)
 result=_native_parse(json.dumps(value,ensure_ascii=False),question,())
 if not result.accepted:raise ValueError(result.reason)
 items=[]
 for task in result.tasks:
  start=question.find(task.quote)
  if question.find(task.quote,start+1)>=0:raise ValueError('ambiguous_quote_occurrence')
  span={'start':start,'end':start+len(task.quote),'text':task.quote}
  items.append({'quote':task.quote,'category':task.category,'domain':task.domain,'operation':task.operation,'facet':task.facet,'target':task.target,'constraints':task.constraints,'canonical_operation':'','ambiguity':'model_declared_ambiguity' if task.ambiguous else 'none','source_span':span,'predicate_span':dict(span),'predicate_span_separately_proposed':False,'context_origin':'retained_model_exact_quote'})
 return items

def inspect(index,question,items):
 from .domain_flow.request_verifier import observe,matches
 from .domain_flow.plan_contract import compile_request
 from .domain_flow.understanding import MeaningTask,Understanding
 problems=[];observed=observe(index,question)
 for item in items:
  if item['category']=='C05':
   from .domain_flow.control_intent import request as control_request
   from .domain_flow.dialogue_task import mentions
   if mentions(index,item['quote'],{'game'}) and control_request(index,item['quote']) is None:problems.append({'kind':'controls_task_without_control_predicate','quote':item['quote']})
  # A generic policy field is not a policy subtype. Bind only an independently
  # recognised unique action in this exact quote, without changing the category.
  local=observe(index,item['quote'])
  policies={n['predicate'] for n in local['needs'] if n['category']==item['category'] and n['facet']==item['facet'] and n['predicate'].startswith('policy.')}
  if len(policies)==1:item['canonical_operation']=next(iter(policies))
  if item['target'] and item['target'] not in item['quote'] or any(c['quote'] not in item['quote'] for c in item.get('constraints',[])):problems.append({'kind':'context_not_in_task_quote','quote':item['quote']})
  for other in items:
   a,b=item['source_span'],other['source_span']
   if item is not other and a['start']<b['end'] and b['start']<a['end']:problems.append({'kind':'overlapping_task_scope','quote':item['quote']})
 tasks=[{'category':i['category'],'facet':i['facet'],'canonical_operation':i['canonical_operation'],'source_span':i['source_span']} for i in items]
 for need in observed['needs']:
  if not any(matches(need,t) for t in tasks):problems.append({'kind':'independently_observed_need_unplanned','category':need['category'],'facet':need['facet'],'quote':need['source_span']['text']})
 return problems

def plan(question,index):
 from .domain_flow.model_gateway import call
 from .bounded_time import remaining
 model=os.getenv('PSU_CHATBOT_OLLAMA_MODEL','psu-r129:latest')
 audit={'version':4,'planner':'retained_training_wire_with_bounded_review','raw_question':question,'model':model,'legacy_splitter_used_before_model':False,'native_corrective_tasks_added':False,'free_form_model_rendering_enabled':False,'attempts':[],'review_limit':1,'schema':'retained_focus_context_tasks','coverage_completeness_claimed':False}
 wire=messages(question);initial=None;initial_issues=[]
 for attempt in range(2):
  left=remaining()
  if attempt and (left is None or left<12):audit['review_skipped']='insufficient_remaining_request_budget';break
  client=types.SimpleNamespace(model=model,timeout=35,http_attempted=False,admission={})
  payload={'model':model,'stage':'context_understanding','messages':wire,'format':schema(),'stream':False,'think':False,'keep_alive':'30m','options':{'temperature':0,'seed':121,'num_ctx':6144,'num_predict':640}}
  receipt={'attempt':attempt+1,'review':bool(attempt)};audit['attempts'].append(receipt)
  try:
   response=call(client,payload);content=response.get('message',{}).get('content','');receipt.update(raw_content=content,transport_completed=True,provenance=response.get('provenance',{}),http_attempted=client.http_attempted)
   items=parse(content,question);problems=inspect(index,question,items);receipt.update(validated_needs=items,plan_problems=problems)
   if not problems:
    audit.update(validated_needs=items,transport_completed=True,returned_provenance=receipt['provenance'],selected_attempt=attempt+1,remaining_plan_problems=[])
    return items,audit
   if attempt==0:initial=items;initial_issues=problems
  except (ValueError,TypeError,KeyError,RecursionError) as exc:
   receipt.update(failure=type(exc).__name__+': '+str(exc));content=receipt.get('raw_content','');problems=[{'kind':'invalid_plan','reason':str(exc)}]
   if content.lstrip().startswith('{') and not content.rstrip().endswith('}'):
    audit['review_skipped']='incomplete_protocol_output_not_retried';break
  except OSError as exc:
   receipt.update(failure=type(exc).__name__+': '+str(exc),http_attempted=client.http_attempted);audit['transport_failure']=True;break
  if not attempt:
   wire=wire+[{'role':'assistant','content':content[:12000]},{'role':'user','content':json.dumps({'review_instruction':'Review the task plan once. Fix the listed omissions or scope errors using exact original substrings. Keep every requested action. Return the same retained JSON schema only; never answer or invent facts.','original_question':question,'plan_problems':problems},ensure_ascii=False)}]
 if initial is not None:
  unsafe={p['quote'] for p in initial_issues if p['kind'] in {'context_not_in_task_quote','overlapping_task_scope'}}
  for item in initial:
   if item['quote'] in unsafe:item['ambiguity']='unverified_task_scope'
  audit.update(validated_needs=initial,transport_completed=True,returned_provenance=audit['attempts'][0].get('provenance',{}),selected_attempt=1,remaining_plan_problems=initial_issues,partial_plan_retained=True)
  return initial,audit
 audit.update(validated_needs=[],failure='no_valid_model_plan',transport_completed=any(a.get('transport_completed') for a in audit['attempts']))
 return [],audit
