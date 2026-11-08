"""Audited lossless serialization compatibility, never interpretation repairs.

An empty redundant root list carries no slots. Ordered numeric task labels are
renamed by a bijection, including their edges. Quotes, targets, operations,
constraints, ambiguity and binding directions are never changed here.
"""
import copy,hashlib,json

def digest(value):
 return hashlib.sha256(json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def normalize(value):
 if not isinstance(value,dict) or value.get('version')!='r129-plan-v2':return value,{}
 out=copy.deepcopy(value);actions=[]
 if 'constraints' in out:
  if out['constraints']!=[]:raise ValueError('unscoped_root_constraints_cannot_be_dropped')
  del out['constraints'];actions.append('removed_redundant_empty_root_list')
 tasks=out.get('tasks')
 if isinstance(tasks,list) and 1<=len(tasks)<=4 and all(isinstance(t,dict) for t in tasks):
  ids=[t.get('id') for t in tasks]
  if all(type(old) in {int,str} and str(old)==str(i+1) for i,old in enumerate(ids)):
   mapping={str(old):f't{i+1}' for i,old in enumerate(ids)}
   for t in tasks:t['id']=mapping[str(t['id'])]
   edges=out.get('shared_bindings')
   if isinstance(edges,list):
    for e in edges:
     if not isinstance(e,dict):continue
     for key in ['source_task_id','target_task_id']:
      old=e.get(key)
      if type(old) in {int,str} and str(old) in mapping:e[key]=mapping[str(old)]
   actions.append('bijective_ordered_task_label_renaming')
 if not actions:return out,{}
 return out,{'wire_surface_adapter':'r132-lossless-surface-v1','surface_actions':actions,
             'raw_graph_surface_conformant':False,'original_graph_sha256':digest(value),
             'effective_graph_sha256':digest(out),'semantic_fields_changed':False,
             'model_semantic_correctness_claimed':False}
