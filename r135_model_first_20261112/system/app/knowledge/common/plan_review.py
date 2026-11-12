"""One bounded compact-plan review; retain verified subset if it fails."""
import copy,json

def review(question,index,items,audit,client,payload):
 from .trained_planner import inspect
 from .domain_flow.model_gateway import call
 from .bounded_time import remaining
 from .model_first import parse
 issues=inspect(index,question,items)
 audit.update(plan_review={'limit':1,'initial_problems':issues,'attempted':False},native_corrective_tasks_added=False)
 if not issues:return items,audit
 left=remaining()
 if __import__('os').getenv('PSU_MODEL_FIRST_REVIEW')=='guard':
  audit['plan_review']['skipped']='guard_only_no_second_model_call'
 elif left is None or left<12:
  audit['plan_review']['skipped']='insufficient_remaining_request_budget'
 else:
  review_payload=copy.deepcopy(payload)
  review_payload['messages'] += [{'role':'assistant','content':audit.get('raw_model_content','')[:12000]},{'role':'user','content':json.dumps({'instruction':'Review your plan once. Restore omitted customer needs or correct mismatched result types. Select exact whole-clause ranges retaining local service, audience and quantities. Return only the original compact JSON array, no facts. Do not add a task merely because an entity is mentioned.','original_question':question,'independent_plan_problems':issues},ensure_ascii=False)}]
  audit['plan_review']['attempted']=True
  try:
   response=call(client,review_payload);content=response.get('message',{}).get('content','')
   audit['plan_review'].update(raw_content=content,transport_completed=True,provenance=response.get('provenance',{}))
   revised=parse(content,question);problems=inspect(index,question,revised);audit['plan_review']['remaining_problems']=problems
   if not problems:
    audit.update(initial_validated_needs=items,validated_needs=revised,selected_attempt=2,remaining_plan_problems=[])
    return revised,audit
  except (OSError,ValueError,TypeError,KeyError,RecursionError) as exc:audit['plan_review']['failure']=type(exc).__name__+': '+str(exc)
 # Scope conflicts are not permission to execute one task's context in another.
 unsafe={p['quote'] for p in issues if p['kind'] in {'context_not_in_task_quote','overlapping_task_scope','controls_task_without_control_predicate'}}
 for item in items:
  if item['quote'] in unsafe:item['ambiguity']='model_plan_conflict'
 audit.update(validated_needs=items,selected_attempt=1,remaining_plan_problems=issues,partial_plan_retained=True)
 return items,audit
