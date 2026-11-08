"""Explicit human-agent review decisions over the 289 retained annotations.

Only language plans are targets. No business answer is copied into weights.
These questions have been exposed before and are never called a fresh holdout.
"""
import copy,hashlib,json,re,sys,collections
from pathlib import Path
BASE=Path(__file__).resolve().parent;R=BASE/'training_v2';R.mkdir(exist_ok=False);sys.path.insert(0,str(BASE/'system'))
from app.knowledge.common.domain_flow.graph_protocol import VERSION,messages,adapt
from app.knowledge.common.domain_flow.context_contract import validate
rows=json.loads((BASE/'LABELS_REVIEW_INPUT.json').read_text('utf8'))
quarantine={39:'Incomplete incident phrase does not identify a requested action.',65:'Fragment about drink/area has no clear requested permission/action.',71:'Unrelated lost-property/wet-equipment fragments; no defensible single intent.',90:'Two unrelated games in a corrupted controls request.',91:'Advance hours phrase lacks a complete requested action.',160:'Nonpayment, number 10 and late check-in are conflated without a relation.',185:'Policy for facebook is ambiguous between social contact and a policy.',206:'Fragment about drink/area with no clear requested action.'}
ambiguous={12,69,81,92,97,164,271}
targets={16:'PlayStation 5 #01-#02',43:'Ms. Kamlawan Nuansai',59:'Hades II',105:'PC #03-#10',166:'VR Zone',192:'อารีน่าออฟเวเลอร์',195:'PC Zone',251:'VR Zone',263:'Nintendo Switch Zone'}
compound={104:'PC',133:'Nintendo Switch',134:'Nintendo Switch',135:'VR',141:'PS5',142:'Cockpit',143:'VR',282:'Cockpit'}
reviews=[];accepted=[]
for i,row in enumerate(rows):
 p=copy.deepcopy(row['label']);changes=[];q=row['question']
 if i in ambiguous:p['tasks'][0]['ambiguous']=True;changes.append('Preserve missing/competing input rather than invent a resolution.')
 if i in targets:
  assert targets[i] in q
  p['tasks'][0]['target']=targets[i];changes.append('Preserve the complete exact named target, including station range/zone.')
 if i==111:
  p['tasks'][0]['ambiguous']=False;p['tasks'][0]['constraints']=[c for c in p['tasks'][0]['constraints'] if c['slot']!='duration']+[{'slot':'duration','quote':'1 ชั่วโมง 30 นาที','source_record_id':''}];changes.append('Conventional hours then minutes is one compound duration, not two alternatives.')
 if i==159:p['tasks'][0]['facet']='closing_time';changes.append('Closing time differs from opening time.')
 if i==249:p['tasks'][0]['constraints'].append({'slot':'audience','quote':'PSU studenr','source_record_id':''});changes.append('Retain the explicitly misspelled audience as quoted language.')
 if i==268:
  p['tasks'][0]['constraints']=[c for c in p['tasks'][0]['constraints'] if c['quote']!='PC']
  p['tasks'][1]['constraints']=[c for c in p['tasks'][1]['constraints'] if c['quote'] not in {'8 buttons','Tekken 8'}];changes.append('Button quantity/game belong to controls; PC belongs only to price.')
 if i==269:
  p['tasks'][0]['constraints']=[c for c in p['tasks'][0]['constraints'] if c['slot']!='audience'];changes.append('A negated PSU membership is not positive PSU audience evidence.')
 if 208<=i<=219:
  period='ครึ่งวัน' if 'ครึ่งวัน' in q else 'เต็มวัน';p['tasks'][0]['constraints'].append({'slot':'requested_scope','quote':period,'source_record_id':''});changes.append('Preserve rental half/full day separately from personal hourly play.')
 if 232<=i<=243:
  p['tasks'][0]['target']=re.search(r'กิจกรรมจำลองทดสอบ\s+\d+',q)[0];changes.append('Keep exact synthetic event identity; this is language supervision, not a real event claim.')
 if i==239:p['tasks'][0]['facet']='registration_url';changes.append('Requested output is a registration link.')
 graph={'version':VERSION,'focus':p['focus'],'context_quotes':p['context_quotes'],'tasks':[],'shared_bindings':[]}
 for j,t in enumerate(p['tasks']):
  t={**t,'id':f't{j+1}'}
  if j and i in compound:
   target=compound[i];t['target']=target;t['constraints']=[c for c in t['constraints'] if c['slot'] in {'platform','service'} and c['quote'] in target]
   if not any(c['slot']=='service' for c in t['constraints']):t['constraints'].append({'slot':'service','quote':target,'source_record_id':''})
   graph['shared_bindings'].append({'source_task_id':'t1','target_task_id':t['id'],'slot':'target','quote':target,'basis':'explicit_anaphor' if re.search(r'\bit\b',t['quote']) else 'source_related_ellipsis'})
   changes.append('Second task shares only the source-named service; no price-option duration or button scope.')
  for c in t['constraints']:c['scope']='local' if c['quote'] in t['quote'] else 'shared'
  graph['tasks'].append(t)
 legacy,_=adapt(graph,q);ok,reason=validate(legacy,q);assert ok,(i,reason)
 spans=[]
 for t in graph['tasks']:
  for role,s in [('task',t['quote']),('target',t['target']),*[(c['slot'],c['quote']) for c in t['constraints']]]:
   if s:
    pos=q.index(s);spans.append({'task_id':t['id'],'role':role,'start':pos,'end':pos+len(s),'quote':s,'exact_current_input':True})
 record={'row':i,'key':row['key'],'prior_split':row['split'],'decision':'quarantined' if i in quarantine else 'reviewed_corrected' if changes else 'reviewed_retained','rationale':quarantine.get(i) or changes or ['Requested action, target, source quote, domain, field and constraints reviewed against the current question.'],'source_spans':spans,'original_label_sha256':hashlib.sha256(json.dumps(row['label'],sort_keys=True).encode()).hexdigest(),'reviewed_label':graph,'business_answer_supervised':False,'review_basis':'explicit_question_semantics_and_original_plan_contract','teacher_answer_is_gold':False}
 reviews.append(record)
 if i not in quarantine:accepted.append({**{k:v for k,v in row.items() if k!='label'},'label':graph,'messages':messages(q)+[{'role':'assistant','content':json.dumps(graph,ensure_ascii=False,separators=(',',':'))}],'review_row':i})
# Group every same domain/action/target/constraint family together. Conservative
# grouping may over-group, which reduces claimed generalization rather than
# letting near-identical tasks cross the split. Fixed before optimization.
def family(x):
 p=x['label'];signature=[]
 for t in p['tasks']:
  signature.append((t['domain'],t['operation'],t['facet'],t['target'].casefold(),tuple(sorted((c['slot'],c['quote'].casefold()) for c in t['constraints'])),t['ambiguous']))
 return hashlib.sha256(json.dumps(signature,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
parent=list(range(len(accepted)))
def root(i):
 while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
 return i
seen={}
for i,x in enumerate(accepted):
 for kind,k in [('review_semantics',family(x)),('original_family',x['family'])]:
  tag=(kind,k)
  if tag in seen:parent[root(i)]=root(seen[tag])
  else:seen[tag]=i
groups={}
for i,x in enumerate(accepted):
 x['review_family']='union_'+str(root(i));groups.setdefault(x['review_family'],[]).append(x)
split={k:[] for k in ['train','validation','test']};covered=set();validation_cats=set()
# First retain evaluation families (never put their sister paraphrase in train).
ordered=sorted(groups,key=lambda k:hashlib.sha256(('r129-fixed-split:'+k).encode()).hexdigest())
for k in ordered:
 group=groups[k];cats={t['domain'] for x in group for t in x['label']['tasks'] if t['domain']!='general'}
 if cats-covered or any(x['split']=='test' for x in group):dest='test';covered|=cats
 elif cats-validation_cats and any(x['split']=='validation' for x in group):dest='validation';validation_cats|=cats
 else:dest='train'
 split[dest]+=group
# Ensure every category has validation support using a different whole family.
for domain in sorted(covered-validation_cats):
 eligible=[k for k in ordered if groups[k][0] in split['train'] and any(t['domain']==domain for x in groups[k] for t in x['label']['tasks'])]
 assert eligible,('missing_validation_family',domain)
 group=groups[eligible[0]]
 for x in group:split['train'].remove(x)
 split['validation']+=group;validation_cats|={t['domain'] for x in group for t in x['label']['tasks']}
for name,xs in split.items():(R/(name+'.jsonl')).write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in xs),'utf8')
(R/'ANNOTATION_REVIEW.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in reviews),'utf8')
report={'reviewed':len(reviews),'accepted':len(accepted),'quarantined':len(quarantine),'corrected':sum(x['decision']=='reviewed_corrected' for x in reviews),'split_counts':{k:len(v) for k,v in split.items()},'categories_test':sorted(covered),'categories_validation':sorted(validation_cats),'same_review_family_crosses_split':False,'original_labels_exposed_to_retained_adapter':True,'fresh_holdout':False,'new_questions':0,'semantic_answer_gold_claimed':False,'full_test_is_retained_workload_not_unseen_generalization':True}
fs=[{x['review_family'] for x in xs} for xs in split.values()];assert not any(fs[i]&fs[j] for i in range(3) for j in range(i))
original=[{x['family'] for x in xs} for xs in split.values()];assert not any(original[i]&original[j] for i in range(3) for j in range(i))
report['original_family_crosses_split']=False;report['grouping']='transitive union of reviewed semantic signature and known original multilingual/core families'
(R/'ANNOTATION_REVIEW_SUMMARY.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),'utf8');print(json.dumps(report,ensure_ascii=False))
