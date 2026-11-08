"""Describe delivered evidence coverage without claiming human intent accuracy."""

def build(plan,obligations,response,hits):
 needs=[]
 if plan.get('operation')=='compound':
  for index,child in enumerate(plan.get('clauses',[]),1):
   nested=child.get('need_ledger') or {}
   status=child.get('need_status','unknown')
   needs.append({'id':'clause_'+str(index),'source_span':child.get('clause',''),
    'status':status,'children':nested.get('needs',[]),'response_type':child.get('response_type')})
 else:
  fields=list(dict.fromkeys(plan.get('requested_fields',[])))
  for field in fields:
   rows=[o for o in obligations if o.get('field')==field]
   known=[o for o in rows if o.get('status')=='known' and o.get('evidence_refs')]
   unsupported=[o for o in rows if o.get('status')!='known' or not o.get('evidence_refs')]
   states={o.get('status') for o in unsupported}
   if known:status='partial' if unsupported else 'answered'
   elif 'conflicted' in states:status='conflicted'
   elif 'not_current' in states or any(o.get('field')=='validity' and o.get('status')=='not_current' for o in obligations):status='not_current'
   elif 'needs_clarification' in states:status='missing_slot'
   elif 'unsupported_scope' in states:status='unsupported'
   else:status='missing_fact'
   needs.append({'id':'field_'+field,'field':field,'status':status,
    'evidence_refs':[{'record_id':o.get('record_id'),'field':field,'sources':o.get('evidence_refs',[])} for o in known],
    'unanswered_records':[{'record_id':o.get('record_id'),'status':o.get('status')} for o in unsupported]})
  for i,span in enumerate(plan.get('unresolved_clauses',[]),1):
   needs.append({'id':'unresolved_'+str(i),'source_span':span,'status':'ambiguous'})
 limits=list(plan.get('scope_limits',[]))
 if any(o.get('field')=='validity' and o.get('status')=='unknown' for o in obligations):limits.append({'reason':'unconfirmed_effective_dates'})
 if response=='retry':
  for need in needs:need['status']='retry';need.pop('evidence_refs',None)
 return {'version':'common_need_ledger_v1','needs':needs,'total_needs':len(needs),
  'answered_needs':sum(n['status']=='answered' for n in needs),'scope_limits':limits,
  'snapshot_consistent':response!='retry','semantic_correctness_verified':False,
  'coverage_basis':'selected typed fields and explicit clauses; not all possible user intents',
  'evidence_hits':len(hits),'response_type':response}
