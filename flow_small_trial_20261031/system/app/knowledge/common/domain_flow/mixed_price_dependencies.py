"""Recompute one purchase total with explicit, source-bound audience counts.

Comparison alternatives and partial audience sets never become a purchase sum.
"""
import copy,re
from decimal import Decimal
from .projection import value,title

def count_roles(index,text,groups):
 """Raw numeric spans adjacent to the actual source audience labels."""
 mentions=[]
 for gid in groups:
  record=index.records[gid]
  for label in {s for s in [*title(record).values(),*sum(record.get('aliases',{}).values(),[])] if s}:
   for m in re.finditer(re.escape(label),text,re.I):mentions.append((m.start(),m.end(),gid))
 mentions=[m for m in mentions if not any(a<=m[0] and m[1]<=b and b-a>m[1]-m[0] for a,b,g in mentions)]
 roles=[]
 quantity=r'(?P<quantity>(?<![\w.])-?\d+(?:\.\d+)?\s*(?:people\b|persons?\b|players?\b|คน))'
 for start,end,gid in sorted(set(mentions)):
  suffix=re.match(r'\s*(?::|=)?\s*'+quantity,text[end:],re.I)
  prefix=re.search(quantity+r'\s*(?:(?:from|in|for)\s+)?$',text[:start],re.I)
  matches=[(m,end if suffix is m else 0) for m in [suffix,prefix] if m]
  if len(matches)!=1:continue
  m,offset=matches[0];a,b=offset+m.start('quantity'),offset+m.end('quantity');count=Decimal(re.match(r'-?\d+(?:\.\d+)?',text[a:b])[0])
  if count<=0 or count!=count.to_integral_value():continue
  role={'audience_id':gid,'persons':int(count),'source_span':{'start':a,'end':b,'text':text[a:b]},'audience_span':{'start':start,'end':end,'text':text[start:end]}}
  if role not in roles:roles.append(role)
 if any(sum(r['audience_id']==gid for r in roles)!=1 for gid in groups):raise ValueError('audience_count_roles_not_unique_or_complete')
 if len({(r['source_span']['start'],r['source_span']['end']) for r in roles})!=len(roles):raise ValueError('same_count_assigned_to_multiple_audiences')
 return roles

def recompute(index,source,executor,snapshot):
 from .financial import audience_mentions,rate_pool,service_scope,unit_calculation,resource_quantities,quantity_text
 from .request_verifier import observe
 from .boolean_dependencies import source_fields
 from .scope import reference_time,validity_allows
 text=source['source_span']['text'];material=[(source.get('target_span') or {}).get('text',''),*[s['source_span']['text'] for s in source.get('slots',[])]]
 scoped=text+' '+' '.join(s for s in material if s and s not in text)
 if source['category']!='C06' or source['operation']!='price_calculate':raise ValueError('one_purchase_calculation_required')
 if re.search(r'\b(?:compare|versus|instead|either|or)\b|เปรียบ|เทียบ|หรือ',scoped,re.I):raise ValueError('comparison_alternatives_not_purchase_total')
 if executor.get('status')!='supported' or executor.get('unresolved_obligations') or executor.get('result_scope',{}).get('snapshot')!=snapshot:raise ValueError('prerequisite_not_source_complete')
 if index.snapshot_identity!={k:snapshot.get(k) for k in ['release_id','epoch']}:raise ValueError('source_snapshot_changed')
 observed=observe(index,text)
 if resource_quantities(index,scoped) or any(c['kind'] not in {'duration','persons','sessions'} for c in observed['constraints']):raise ValueError('quantity_or_condition_scope_unverified')
 groups,negative=audience_mentions(index,scoped);services=service_scope(index,scoped)
 if not groups or negative or len(services)!=1:raise ValueError('purchase_scope_not_unique')
 person_constraints=[c for c in observed['constraints'] if c['kind']=='persons']
 roles=count_roles(index,text,groups) if person_constraints else []
 if len(groups)>1 and not roles:raise ValueError('mixed_audience_person_quantities_required')
 counts={r['audience_id']:r['persons'] for r in roles} if roles else {gid:1 for gid in groups}
 person_spans={(r['source_span']['start'],r['source_span']['end']) for r in roles}
 if {(c['source_span']['start'],c['source_span']['end']) for c in observed['constraints'] if c['kind']=='persons'}!=person_spans:raise ValueError('unassigned_or_unverified_person_quantity')
 pool=[f for f in rate_pool(index,scoped) if f['facet']=='amount'];bygroup={gid:[f for f in pool if value(index.records[f['record_id']],'audience_id')==gid] for gid in groups}
 if any(len(fs)!=1 for fs in bygroup.values()):raise ValueError('audience_rate_source_not_unique_or_complete')
 expected={fs[0]['id'] for fs in bygroup.values()};claims=[c for c in executor.get('claims',[]) if c.get('facet')=='amount'];calculations=executor.get('calculation_receipts',[])
 if len(claims)!=len(expected) or {c.get('fact_id') for c in claims}!=expected or len(calculations)!=len(expected) or {c.get('fact_id') for c in calculations}!=expected:raise ValueError('mixed_purchase_not_all_source_lines')
 sessions=list(re.finditer(r'(\d+)\s*รอบ|\b(\d+)\s+sessions?\b',quantity_text(index,scoped,pool),re.I))
 if len(sessions)>1:raise ValueError('session_roles_not_unique')
 session_count=int(next(x for x in sessions[0].groups() if x)) if sessions else 1
 refs=source_fields(index,index.records[next(iter(services))],['name']);lines=[]
 for gid in sorted(groups):
  fact=bygroup[gid][0];record=index.records[fact['record_id']];unit=value(record,'unit');persons=counts[gid]
  if unit not in {'per_person','per_group','per_session'} or persons>1 and unit=='per_session' or value(record,'currency')!='THB' or value(record,'service_id') not in services or validity_allows(fact,reference_time(snapshot['reference_time'])) is not True:raise ValueError('rate_unit_currency_service_or_validity_unconfirmed')
  keys=['amount_minor','currency','service_id','audience_id','duration_minutes','unit']+[k for k in ['calculation_rule','persons_min','persons_max'] if record.get('fields',{}).get(k,{}).get('status')=='known']
  line_refs=source_fields(index,record,keys)+source_fields(index,index.records[gid],['name']);refs+=line_refs
  if unit=='per_group' and (value(record,'persons_min') and persons<value(record,'persons_min') or value(record,'persons_max') and persons>value(record,'persons_max')):raise ValueError('group_size_outside_rate_scope')
  base=Decimal(value(record,'amount_minor'))/100
  if base!=Decimal(str(fact['numeric'])):raise ValueError('projected_amount_not_source')
  calc=unit_calculation(index,fact,scoped)
  if calc.get('error'):raise ValueError('arithmetic_not_source_declared')
  claim=next(c for c in claims if c['fact_id']==fact['id']);receipt=next(c for c in calculations if c['fact_id']==fact['id']);count=Decimal(persons if unit=='per_person' else 1);total=Decimal(str(calc['amount_thb']))*count
  if claim.get('record_id')!=record['record_id'] or Decimal(str(claim.get('numeric')))!=Decimal(str(calc['amount_thb'])) or claim.get('evidence_refs')!=fact['evidence_refs']+fact.get('confirmation_evidence_refs',[]):raise ValueError('mixed_claim_source_or_numeric_mismatch')
  if not any(r.get('fact_id')==fact['id'] and r.get('record_revision')==record['revision'] and r.get('snapshot')==snapshot for r in executor.get('receipts',[])):raise ValueError('current_rate_receipt_missing')
  if receipt.get('snapshot')!=snapshot or receipt.get('unit_calculation')!=calc or Decimal(str(receipt.get('total_thb')))!=total or Decimal(str(receipt.get('billing_quantity')))!=count or Decimal(str(receipt.get('unit_rate_thb')))!=base or receipt.get('sessions')!=session_count or receipt.get('billing_unit')!=unit or receipt.get('input_claim_refs')!=[fact['id']] or receipt.get('evidence_refs')!=fact['evidence_refs'] or receipt.get('transformation')!='decimal_source_declared_billing_v2':raise ValueError('mixed_calculation_receipt_not_recomputed_source')
  lines.append({'fact_id':fact['id'],'record_revision':record['revision'],'audience_id':gid,'persons':persons,'billing_quantity':str(count),'unit_rate_thb':str(base),'total_thb':str(total),'unit_calculation':calc,'source_evidence_refs':line_refs,'quantity_role':next((r for r in roles if r['audience_id']==gid),None)})
 return {'total_thb':sum(Decimal(x['total_thb']) for x in lines),'source_claim_refs':sorted(expected),'source_evidence_refs':refs,'lines':copy.deepcopy(lines),'quantity_roles':roles,'sessions':session_count,'source_span':copy.deepcopy(source['source_span'])}

def evaluate(index,source,executor,edge,snapshot,base):
 try:
  if edge.get('requested_amount_kind')=='unit_rate':return {**base,'reason':'prerequisite_scalar_amount_not_unique'}
  proof=recompute(index,source,executor,snapshot);amount=proof.pop('total_thb');threshold=Decimal(edge['threshold']);op=edge['operator'];outcome={'lt':amount<threshold,'le':amount<=threshold,'gt':amount>threshold,'ge':amount>=threshold,'eq':amount==threshold,'ne':amount!=threshold}[op]
  return {**base,**proof,'verified':True,'outcome':'true' if outcome else 'false','reason':'source_mixed_purchase_total_recomputed','amount_kind':'calculated_total','observed_amount_thb':str(amount),'threshold_thb':str(threshold),'operator':op}
 except (KeyError,ValueError,TypeError,ArithmeticError) as error:return {**base,'reason':'mixed_purchase_prerequisite_unconfirmed','revalidation_reason':str(error)}
