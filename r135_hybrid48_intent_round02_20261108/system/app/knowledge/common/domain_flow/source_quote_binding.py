"""Repair casing only when it maps to one exact source substring."""
import copy,re
def rebind(value,question):
 value=copy.deepcopy(value);repairs=[]
 def bind(text,path):
  if not isinstance(text,str) or not text or text in question:return text
  matches=list(re.finditer(re.escape(text),question,re.I))
  if len(matches)!=1:return text
  source=matches[0].group()
  repairs.append({'path':path,'model_quote':text,'source_quote':source,'basis':'unique_case_insensitive_source_span'})
  return source
 if not isinstance(value,dict):return value,repairs
 if isinstance(value.get('context_quotes'),list):value['context_quotes']=[bind(s,'context_quotes') for s in value['context_quotes']]
 if isinstance(value.get('tasks'),list):
  for i,t in enumerate(value['tasks']):
   if not isinstance(t,dict):continue
   for name in ['quote','target']:
    if name in t:t[name]=bind(t[name],f'tasks[{i}].{name}')
   if isinstance(t.get('constraints'),list):
    for j,c in enumerate(t['constraints']):
     if isinstance(c,dict) and 'quote' in c:c['quote']=bind(c['quote'],f'tasks[{i}].constraints[{j}].quote')
 return value,repairs
