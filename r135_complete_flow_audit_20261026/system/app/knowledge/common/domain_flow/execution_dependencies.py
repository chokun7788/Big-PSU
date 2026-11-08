"""Source-verified output conditions, separate from shared entity bindings.

Bounded predicates compare a THB unit rate or a source-recomputed total. Unsupported output
conditions remain unknown; no planner business value or audit flag is authority.
"""
import copy,json,re,hashlib
from contextlib import contextmanager
from dataclasses import asdict,is_dataclass
from decimal import Decimal
from .projection import value

VERSION='r135-execution-dependency-v1'
PREDICATES={'thb_unit_rate_comparison':{'source_kind':'rate','source_operation':'detail','source_field':'amount','unit':'THB','requires':'one completed scalar source unit-rate receipt','unlisted_predicates':'unsupported_dependency_predicate'},'thb_calculated_total_comparison':{'source_kind':'rate','source_operation':'price_calculate','source_field':'amount','unit':'THB','requires':'one complete source rate and independently recomputed people/session/duration calculation receipt','unlisted_predicates':'unsupported_dependency_predicate'}}
OPS={'below':'lt','under':'lt','less than':'lt','at most':'le','no more than':'le','above':'gt','over':'gt','more than':'gt','at least':'ge','equal to':'eq','เท่ากับ':'eq','ต่ำกว่า':'lt','น้อยกว่า':'lt','ไม่เกิน':'le','มากกว่า':'gt','เกิน':'gt','อย่างน้อย':'ge'}
GATE=re.compile(r'^\s*(?:(?P<introducer_en>if|unless|provided(?:\s+that)?)\s+(?P<label_en>it|(?:the\s+)?(?:(?:unit|total)\s+)?(?:price|cost))\s+(?:is\s+)?(?P<negated_en>not\s+)?|(?P<introducer_th>ถ้า|หาก|เว้นแต่)(?P<label_th>ราคา(?:ต่อหน่วย|รวม)?|ยอดรวม|มัน)\s*)(?P<operator>'+ '|'.join(re.escape(s) for s in sorted(OPS,key=len,reverse=True))+r')\s*(?P<value>\d+(?:\.\d+)?)\s*(?:THB|baht|บาท)\s*[,，]\s*',re.I)
SUFFIX_GATE=re.compile(GATE.pattern.removeprefix(r'^\s*').replace('if|unless|provided','only\\s+if|unless|provided',1).replace('ถ้า|หาก|เว้นแต่','เฉพาะเมื่อ|ต่อเมื่อ|เว้นแต่',1).removesuffix(r'\s*[,，]\s*')+r'\s*[?.!]*$',re.I)
BOTH_GATE=re.compile(r'^\s*(?:if\s+both\s+(?:(?P<kind_en>unit|total)\s+)?prices\s+(?:are\s+)?|(?:ถ้า|หาก)ราคา(?P<kind_th>ต่อหน่วย|รวม)?ทั้งสอง\s*)(?P<operator>'+ '|'.join(re.escape(s) for s in sorted(OPS,key=len,reverse=True))+r')\s*(?P<value>\d+(?:\.\d+)?)\s*(?:THB|baht|บาท)\s*[,，]\s*',re.I)
OUTPUT_CONDITION=re.compile(r'^\s*(?:(?:if|unless|provided(?:\s+that)?)\s+(?:both\s+(?:(?:unit|total)\s+)?prices\b|it\s+is|(?:the\s+)?(?:(?:unit|total)\s+)?(?:price|cost)\b)|(?:ถ้า|หาก|เว้นแต่)(?:ราคา|ยอดรวม))',re.I)
OUTPUT_SUFFIX=re.compile(r'\b(?:only\s+if|unless|provided(?:\s+that)?)\s+(?:(?:the\s+)?(?:(?:unit|total)\s+)?(?:price|cost)\b|it\s+is\b)|(?:เฉพาะเมื่อ|เว้นแต่|ต่อเมื่อ)(?:ราคา|ยอดรวม)',re.I)
AFFIRMATIVE_CONDITION=re.compile(r'^\s*(?:if\s+(?P<affirmative_en>yes|so|true|false|no)\s*[,，]|(?:ถ้า|หาก)(?P<affirmative_th>ไม่ใช่|ใช่)\s*[,，])',re.I)
STATE_CONDITION=re.compile(r'^\s*(?:if\s+(?:it|(?:the\s+)?(?:service|studio|resource|machine))\s+is\s+(?P<negative_en>not\s+)?(?P<state_en>available|free|open(?:\s+for\s+play)?)|(?:ถ้า|หาก)(?:(?:เครื่อง|บริการ|ศูนย์)\s*)?(?P<negative_th>ไม่)?(?P<state_th>ว่าง|เปิด(?:ให้เล่น)?))\s*[,，]\s*',re.I)
PREDICATES.update(recorded_service_window_boolean={'source_kind':'schedule','requires':'one boolean play-service question with an explicit point/range, independently recomputed calendar and source pointers'},live_resource_window_boolean={'source_kind':'live_binding','requires':'one boolean availability question and one current-request resource observation, independently checked binding, payload, freshness, calendar and requested window'})
PREDICATES['thb_calculated_total_comparison']['requires']='one purchase with a unique source rate per audience and independently recomputed people/session/duration arithmetic; alternatives are not summed'
def row(task):return asdict(task) if is_dataclass(task) else task

def referent_text(question):
 """A pronoun naming a computed price is not a service/game anaphor."""
 match=BOTH_GATE.match(question) or GATE.match(question) or STATE_CONDITION.match(question)
 if match:return ' '*match.end()+question[match.end():]
 if OUTPUT_CONDITION.match(question) or AFFIRMATIVE_CONDITION.match(question):
  comma=re.search(r'[,，]',question)
  if comma:return ' '*(comma.end())+question[comma.end():]
 suffix=OUTPUT_SUFFIX.search(question)
 if suffix:return question[:suffix.start()]+' '*(len(question)-suffix.start())
 return question

def edges(question,tasks):
 rows=[row(t) for t in tasks];result={}
 from ..flow_context import CURRENT
 ctx=CURRENT.get();parent=ctx.parent_execution_scopes.get(question) if ctx else None
 for n,task in enumerate(rows):
  text=task['source_span']['text'];both=BOTH_GATE.match(text);leading=GATE.match(text);trailing=SUFFIX_GATE.search(text) if not leading else None;match=leading or trailing;state=STATE_CONDITION.match(text);prefix=both or leading or AFFIRMATIVE_CONDITION.match(text) or state
  if parent:
   result[task['id']]=[{'version':VERSION,'basis':'parent_source_output_condition','target_task_id':task['id'],'source_task_id':None,'external_source_task_id':parent['task_id'],'execution_dependency':True,'binding_state':'parent_proof_required','parent_question_sha256':hashlib.sha256(parent['question'].encode()).hexdigest(),'source_span':copy.deepcopy(task['source_span']),'condition_span':{'start':task['source_span']['start'],'end':task['source_span']['start']+len(text[:prefix.end()].rstrip(' ,，')),'text':text[:prefix.end()].rstrip(' ,，')} if prefix else None}];continue
  if both:
   prior=[t for t in rows[:n] if t['category']=='C06' and t['facet']=='amount' and t['operation'] in {'detail','price_calculate'}]
   condition=text[:both.end()].rstrip(' ,，');label=(both['kind_en'] or both['kind_th'] or '').casefold();kind='calculated_total' if label in {'total','รวม'} else 'unit_rate' if label in {'unit','ต่อหน่วย'} else 'auto'
   state='bound' if len(prior)==2 else 'ambiguous_prerequisite' if len(prior)>2 else 'missing_prerequisite'
   if re.search(r'\b(?:if|unless|except|provided)\b|ถ้า|หาก|ยกเว้น',text[both.end():],re.I):state='unsupported_compound_condition'
   result[task['id']]=[{'version':VERSION,'basis':'source_output_condition','target_task_id':task['id'],'source_task_id':source['id'] if source else None,'prerequisite_candidates':[t['id'] for t in prior],'execution_dependency':True,'predicate':'thb_calculated_total_comparison' if kind=='calculated_total' or kind=='auto' and source and source['operation']=='price_calculate' else 'thb_unit_rate_comparison','source_span':copy.deepcopy(task['source_span']),'condition_span':{'start':task['source_span']['start'],'end':task['source_span']['start']+len(condition),'text':condition},'operator':OPS[both['operator'].casefold()],'threshold':both['value'],'unit':'THB','binding_state':state,'requested_amount_kind':kind,'combination':'all','quantifier':'both'} for source in (prior if len(prior)==2 else [None])]
   continue
  suffix=OUTPUT_SUFFIX.search(text) if not match and not prefix and not OUTPUT_CONDITION.match(text) else None
  if not match and not OUTPUT_CONDITION.match(text) and not AFFIRMATIVE_CONDITION.match(text) and not state and not suffix:continue
  prior=[t for t in rows[:n] if t['category']=='C06' and t['facet']=='amount' and t['operation'] in {'detail','price_calculate'}]
  edge={'version':VERSION,'basis':'source_output_condition','target_task_id':task['id'],'source_task_id':prior[0]['id'] if len(prior)==1 else None,'prerequisite_candidates':[t['id'] for t in prior],'execution_dependency':True,'predicate':'thb_unit_rate_comparison' if match else 'unsupported_output_condition','source_span':copy.deepcopy(task['source_span']),'condition_span':None,'operator':None,'threshold':None,'unit':'THB','binding_state':'bound' if match and len(prior)==1 else 'ambiguous_prerequisite' if len(prior)>1 else 'missing_prerequisite' if not prior else 'unsupported_condition'}
  if suffix:
   edge.update(binding_state='unsupported_dependency_predicate',unit=None,condition_span={'start':task['source_span']['start']+suffix.start(),'end':task['source_span']['end'],'text':text[suffix.start():]});result[task['id']]=[edge];continue
  if match:
   end=match.end();condition=text[match.start():end].rstrip(' ,，?!')
   label=(match['label_en'] or match['label_th']).casefold();kind='calculated_total' if re.search(r'total|รวม',label) else 'unit_rate' if re.search(r'unit|ต่อหน่วย',label) else 'auto'
   start=task['source_span']['start']+match.start();edge.update(condition_span={'start':start,'end':start+len(condition),'text':condition},operator=OPS[match['operator'].casefold()],threshold=match['value'],requested_amount_kind=kind)
   negated=((match['introducer_en'] or match['introducer_th']).casefold() in {'unless','เว้นแต่'}) != bool(match['negated_en'])
   if negated:edge.update(operator={'lt':'ge','le':'gt','gt':'le','ge':'lt','eq':'ne'}[edge['operator']],comparison_negated=True)
   if kind=='calculated_total' or kind=='auto' and len(prior)==1 and prior[0]['operation']=='price_calculate':edge['predicate']='thb_calculated_total_comparison'
   if re.search(r'\b(?:if|unless|except|provided)\b|ถ้า|หาก|ยกเว้น',text[end:],re.I):edge['binding_state']='unsupported_compound_condition'
   if trailing and re.search(r'\b(?:if|unless|except|provided)\b|ถ้า|หาก|ยกเว้น',text[:match.start()],re.I):edge['binding_state']='unsupported_compound_condition'
  affirmative=AFFIRMATIVE_CONDITION.match(text)
  if affirmative:
   prior=[t for t in rows[:n] if t['category'] in {'C11','C12'}]
   condition=text[:affirmative.end()].rstrip(' ,，')
   edge.update(source_task_id=prior[0]['id'] if len(prior)==1 else None,prerequisite_candidates=[t['id'] for t in prior],predicate='live_resource_window_boolean' if len(prior)==1 and prior[0]['category']=='C12' else 'recorded_service_window_boolean',binding_state='bound' if len(prior)==1 else 'ambiguous_prerequisite' if prior else 'unsupported_dependency_predicate',unit=None,expected_boolean=(affirmative['affirmative_en'] or affirmative['affirmative_th']).casefold() not in {'false','no','ไม่ใช่'},condition_span={'start':task['source_span']['start'],'end':task['source_span']['start']+len(condition),'text':condition})
   if re.search(r'\b(?:if|unless|except|provided)\b|ถ้า|หาก|ยกเว้น',text[affirmative.end():],re.I):edge['binding_state']='unsupported_compound_condition'
  if state:
   word=(state['state_en'] or state['state_th']).casefold();category='C11' if word.startswith('open') or word.startswith('เปิด') else 'C12'
   prior=[t for t in rows[:n] if t['category']==category];condition=text[:state.end()].rstrip(' ,，')
   edge.update(source_task_id=prior[0]['id'] if len(prior)==1 else None,prerequisite_candidates=[t['id'] for t in prior],predicate='recorded_service_window_boolean' if category=='C11' else 'live_resource_window_boolean',binding_state='bound' if len(prior)==1 else 'ambiguous_prerequisite' if prior else 'missing_prerequisite',unit=None,expected_boolean=not bool(state['negative_en'] or state['negative_th']),state_predicate_explicit=True,condition_span={'start':task['source_span']['start'],'end':task['source_span']['start']+len(condition),'text':condition})
   if re.search(r'\b(?:if|unless|except|provided)\b|ถ้า|หาก|ยกเว้น',text[state.end():],re.I):edge['binding_state']='unsupported_compound_condition'
  result[task['id']]=[edge]
 return result

def evaluate(index,question,tasks,task_id,executors,snapshot):
 expected=edges(question,tasks).get(task_id,[]);actual=next((row(t).get('execution_dependencies',[]) for t in tasks if row(t)['id']==task_id),[])
 base={'version':VERSION,'task_id':task_id,'outcome':'unknown','verified':False,'reason':'dependency_contract_not_recomputed','snapshot':copy.deepcopy(snapshot),'source_claim_refs':[]}
 if any(snapshot.get(k)!=index.snapshot_identity.get(k) for k in ['release_id','epoch']):return {**base,'reason':'dependency_source_snapshot_changed'}
 if any((s:=row(t)['source_span']).get('start',-1)<0 or question[s['start']:s['end']]!=s['text'] for t in tasks):return {**base,'reason':'dependency_source_span_not_current'}
 if not expected or actual!=expected:return base
 if len(expected)>1:
  parts=[_evaluate_edge(index,question,tasks,edge,executors,snapshot,base) for edge in expected]
  refs=[set(p['source_claim_refs']) for p in parts];distinct=all(not a&b for i,a in enumerate(refs) for b in refs[i+1:])
  verified=all(p['verified'] for p in parts) and distinct
  outcome=('true' if all(p['outcome']=='true' for p in parts) else 'false') if verified else 'unknown'
  edge={**copy.deepcopy(expected[0]),'source_task_id':None,'predicate':'all_source_conditions','source_task_ids':[p['source_task_id'] for p in expected]}
  return {**base,'edge':edge,'verified':verified,'outcome':outcome,'reason':'all_source_conditions_recomputed' if verified else 'prerequisites_not_distinct' if not distinct else 'one_or_more_prerequisites_unconfirmed','condition_results':parts,'source_claim_refs':sorted(set().union(*refs))}
 return _evaluate_edge(index,question,tasks,expected[0],executors,snapshot,base)

def _evaluate_edge(index,question,tasks,edge,executors,snapshot,base):
 base={**base,'edge':copy.deepcopy(edge)}
 if edge['binding_state']=='parent_proof_required':
  from ..flow_context import CURRENT
  ctx=CURRENT.get();parent=ctx.parent_execution_scopes.get(question) if ctx else None
  if not parent or parent['question']==question:return {**base,'reason':'parent_dependency_scope_missing'}
  proof=evaluate(index,parent['question'],parent['tasks'],parent['task_id'],parent['executors'],snapshot)
  return {**base,'verified':proof['verified'],'outcome':proof['outcome'],'reason':proof['reason'],'source_claim_refs':proof['source_claim_refs'],'parent_source_proof':proof}
 if edge['binding_state']!='bound':return {**base,'reason':edge['binding_state']}
 source=next((row(t) for t in tasks if row(t)['id']==edge['source_task_id']),None)
 executor=next((e for e in executors if e['task_id']==edge['source_task_id']),None)
 if not source or not executor or executor.get('status')!='supported' or executor.get('unresolved_obligations'):return {**base,'reason':'prerequisite_not_source_complete'}
 if edge['predicate'] in {'recorded_service_window_boolean','live_resource_window_boolean'}:
  from .boolean_dependencies import evaluate as boolean_evaluate
  return boolean_evaluate(index,source,executor,edge,snapshot,base)
 claims=[c for c in executor.get('claims',[]) if c.get('facet')=='amount']
 if len(claims)>1:
  from .mixed_price_dependencies import evaluate as mixed_evaluate
  return mixed_evaluate(index,source,executor,edge,snapshot,base)
 if len(claims)!=1:return {**base,'reason':'prerequisite_scalar_amount_not_unique'}
 claim=claims[0];fact=index.byid.get(claim.get('fact_id'));record=index.records.get(claim.get('record_id'),{})
 if not fact or fact['record_id']!=record.get('record_id') or record.get('kind')!='rate' or value(record,'currency')!='THB' or value(record,'amount_minor') is None:return {**base,'reason':'prerequisite_rate_source_not_confirmed'}
 scoped=source['source_span']['text']
 material=[(source.get('target_span') or {}).get('text',''),*[s['source_span']['text'] for s in source.get('slots',[])]]
 scoped+=' '+' '.join(s for s in material if s and s not in scoped)
 from .financial import rate_pool,unit_calculation,quantity_text,audience_mentions,resource_quantities
 from .request_verifier import observe
 if resource_quantities(index,scoped,(source.get('target_span') or {}).get('text') or None) or any(c['kind'] not in {'duration','persons','sessions'} for c in observe(index,scoped)['constraints']):return {**base,'reason':'prerequisite_quantity_or_condition_scope_unverified'}
 if fact['id'] not in {f['id'] for f in rate_pool(index,scoped)}:return {**base,'reason':'prerequisite_rate_scope_mismatch'}
 receipts=[r for r in executor.get('receipts',[]) if r.get('fact_id')==fact['id'] and r.get('record_revision')==record['revision'] and r.get('snapshot')==snapshot]
 if not receipts:return {**base,'reason':'prerequisite_snapshot_receipt_missing'}
 from ..registry import source_errors,pointer
 keys=['amount_minor','currency','service_id','audience_id','duration_minutes','unit']+[k for k in ['calculation_rule','persons_min','persons_max'] if record.get('fields',{}).get(k,{}).get('status')=='known']
 refs=[ref for key in keys for ref in record['fields'].get(key,{}).get('evidence_refs',[])]
 try:
  for key in keys:
   field=record['fields'][key]
   if field['status']!='known' or not field.get('evidence_refs'):raise ValueError('unconfirmed rate field')
   for ref in field['evidence_refs']:
    metadata,body=index.source_pairs[ref['source_id']]
    if source_errors(metadata,body,demo=False) or pointer(json.loads(body),ref['locator'])!=field['value']:raise ValueError('source pointer differs')
  base_amount=Decimal(value(record,'amount_minor'))/100
  if Decimal(str(fact.get('numeric')))!=base_amount:raise ValueError('projected rate differs from source')
  from .meaning_reader import execution_query
  from .understanding import MeaningTask
  meaning=MeaningTask(scoped,'service_fee','C06',source['operation'],'amount',(source.get('target_span') or {}).get('text',''),[{'slot':s['kind'],'quote':s['source_span']['text'],'source_record_id':s.get('source_record_id','')} for s in source.get('slots',[])])
  scoped=execution_query(index,scoped,meaning);calculation=unit_calculation(index,fact,scoped)
  if calculation.get('error'):raise ValueError('source arithmetic not confirmed')
  groups,_=audience_mentions(index,scoped)
  if groups and groups!={value(record,'audience_id')}:raise ValueError('total audience not unique')
  quantities=quantity_text(index,scoped,[fact]);people=list(re.finditer(r'(?<![\w.-])(-?\d+(?:\.\d+)?)\s*(?:people\b|persons?\b|players?\b|คน)',quantities,re.I))
  if len(people)>1:raise ValueError('person count roles not unique')
  persons=Decimal(people[0][1]) if people else Decimal(1)
  if persons<=0 or persons!=persons.to_integral_value():raise ValueError('invalid person count')
  unit=value(record,'unit');count=persons if unit=='per_person' else Decimal(1)
  if persons>1 and unit not in {'per_person','per_group'}:raise ValueError('per-person basis not declared')
  if unit=='per_group' and (value(record,'persons_min') and persons<value(record,'persons_min') or value(record,'persons_max') and persons>value(record,'persons_max')):raise ValueError('group bounds differ')
  unit_amount=Decimal(str(calculation['amount_thb']));total=unit_amount*count
  if Decimal(str(claim.get('numeric')))!=unit_amount:raise ValueError('rendered numeric claim differs from source arithmetic')
  calculations=[c for c in executor.get('calculation_receipts',[]) if c.get('fact_id')==fact['id']]
  requested_kind=edge.get('requested_amount_kind','auto');kind='calculated_total' if requested_kind=='calculated_total' or requested_kind=='auto' and source['operation']=='price_calculate' else 'unit_rate'
  if kind=='calculated_total' and source['operation']!='price_calculate':return {**base,'reason':'calculation_prerequisite_required'}
  if kind=='calculated_total' and len(calculations)!=1:raise ValueError('total calculation receipt required')
  sessions=re.search(r'(\d+)\s*รอบ|\b(\d+)\s+sessions?\b',quantities)
  expected_sessions=int(next(x for x in sessions.groups() if x)) if sessions else 1
  for calc in calculations:
   if calc.get('snapshot')!=snapshot or calc.get('unit_calculation')!=calculation or Decimal(str(calc.get('total_thb')))!=total or Decimal(str(calc.get('billing_quantity')))!=count or Decimal(str(calc.get('unit_rate_thb')))!=base_amount or calc.get('sessions')!=expected_sessions or calc.get('billing_unit')!=unit or calc.get('input_claim_refs')!=[fact['id']] or calc.get('evidence_refs')!=fact['evidence_refs'] or calc.get('transformation')!='decimal_source_declared_billing_v2':raise ValueError('calculation receipt differs from independent source recomputation')
  if kind=='unit_rate' and requested_kind=='auto' and (calculation['billed_units']!=1 or count!=1):return {**base,'reason':'prerequisite_amount_kind_ambiguous'}
  amount=total if kind=='calculated_total' else base_amount
  threshold=Decimal(edge['threshold']);op=edge['operator'];outcome={'lt':amount<threshold,'le':amount<=threshold,'gt':amount>threshold,'ge':amount>=threshold,'eq':amount==threshold,'ne':amount!=threshold}[op]
 except (KeyError,ValueError,TypeError,ArithmeticError):return {**base,'reason':'prerequisite_price_revalidation_failed'}
 return {**base,'outcome':'true' if outcome else 'false','verified':True,'reason':'source_price_comparison_recomputed','source_claim_refs':[fact['id']],'source_record_revision':record['revision'],'source_evidence_refs':copy.deepcopy(refs),'amount_kind':kind,'observed_amount_thb':str(amount),'observed_unit_amount_thb':str(base_amount),'independent_calculation':calculation,'billing_quantity':str(count),'threshold_thb':str(threshold),'operator':op}

@contextmanager
def parent_scope(index,question,tasks,task_id,executors,snapshot,child_question):
 from ..flow_context import CURRENT
 from .input_derivation import check
 ctx=CURRENT.get()
 if ctx is None or question==child_question or not check(child_question)['verified']:raise ValueError('parent_dependency_child_scope_not_verified')
 proof=evaluate(index,question,tasks,task_id,executors,snapshot)
 if not proof['verified'] or proof['outcome']!='true':raise ValueError('parent_dependency_not_satisfied')
 old=ctx.parent_execution_scopes.get(child_question)
 ctx.parent_execution_scopes[child_question]={'question':question,'tasks':[row(t) for t in tasks],'task_id':task_id,'executors':copy.deepcopy(executors),'snapshot':copy.deepcopy(snapshot)}
 try:yield proof
 finally:
  if old is None:ctx.parent_execution_scopes.pop(child_question,None)
  else:ctx.parent_execution_scopes[child_question]=old

def notice(proof,lang):
 if proof['outcome']=='false':return 'เงื่อนไขไม่ผ่าน จึงไม่แสดงงานที่ขอให้ทำเฉพาะเมื่อเงื่อนไขผ่านครับ' if lang=='th' else 'The condition is not met, so the conditional detail is not shown.'
 if proof['reason']=='ambiguous_prerequisite':
  monetary=proof.get('edge',{}).get('unit')=='THB'
  return ('เงื่อนไขนี้อ้างถึงราคาของตัวเลือกใดครับ?' if monetary else 'เงื่อนไขนี้อ้างถึงผลลัพธ์ของตัวเลือกใดครับ?') if lang=='th' else ('Which price option does this condition refer to?' if monetary else 'Which result does this condition refer to?')
 if proof['reason'] in {'calculation_prerequisite_required','prerequisite_amount_kind_ambiguous'}:return 'เงื่อนไขนี้ใช้ราคาต่อหน่วยหรือยอดรวมสำหรับจำนวนคนและรอบใดครับ?' if lang=='th' else 'Does this condition use a unit rate or a total for a particular number of people and sessions?'
 if proof['reason']=='unsupported_dependency_predicate':return 'ยังตรวจเงื่อนไขจากผลลัพธ์ประเภทนี้ด้วยวิธีที่รองรับไม่ได้ จึงยังไม่แสดงส่วนที่ขึ้นกับเงื่อนไขนี้ครับ' if lang=='th' else 'The requested output condition is not supported, so its dependent detail is withheld.'
 if proof['reason']=='unsupported_compound_condition':return 'ยังตรวจเงื่อนไขร่วมทั้งหมดนี้ไม่ได้ จึงยังไม่แสดงส่วนที่ขึ้นกับเงื่อนไขครับ' if lang=='th' else 'The combined conditions cannot all be verified, so their dependent detail is withheld.'
 if proof['reason']=='unsupported_condition':return 'กรุณาระบุเงื่อนไขราคาและว่าต้องการใช้ราคาต่อหน่วยหรือยอดรวมครับ' if lang=='th' else 'Please specify the price condition and whether it refers to a unit rate or a total.'
 return 'ยังประเมินเงื่อนไขจากผลก่อนหน้าไม่ได้ จึงยังไม่เปิดงานส่วนนี้ ส่วนที่ยืนยันได้ยังแสดงไว้ครับ' if lang=='th' else 'The prerequisite condition cannot be confirmed, so this conditional part is withheld. Independently supported parts are retained.'

def blocked_reason(proof):
 return 'execution_condition_not_met' if proof['outcome']=='false' else 'unsupported_operation' if proof['reason'] in {'unsupported_dependency_predicate','unsupported_compound_condition'} else 'execution_prerequisite_unconfirmed'

def attach_ledger(ledger,task,proof,result=None):
 ledger['dependency_receipts']=[copy.deepcopy(proof)]
 obligation={'id':task.id+':execution_dependency','kind':'execution_dependency','expected':task.execution_dependencies,'fulfilled':proof['verified'],'reason':None if proof['verified'] else proof['reason'],'claim_refs':proof['source_claim_refs'],'proof':copy.deepcopy(proof)}
 if proof['outcome']=='false' and proof.get('verified'):
  for o in ledger['obligations']:o.update(fulfilled=True,reason='conditional_task_not_applicable',claim_refs=[],proof=copy.deepcopy(proof))
  ledger.update(terminal_state='supported',reason_codes=['execution_condition_not_met'],all_obligations_fulfilled=True)
  if result is not None:result['status']='answer'
 ledger['obligations']=[o for o in ledger['obligations'] if o['kind']!='execution_dependency']+[obligation]
 ledger['all_obligations_fulfilled']=all(o['fulfilled'] for o in ledger['obligations'])
 return ledger
