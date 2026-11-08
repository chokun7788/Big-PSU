"""Independent request observations and five-section delivery verification.

The observations are made from the user's text and source vocabulary BEFORE
looking at planner tasks. Recognised needs can challenge an omitted task.
Unrecognised or ambiguous language remains review_required; the detector never
certifies arbitrary natural-language semantic completeness.
"""
import copy,re
from .vocabulary import FACETS as PATTERNS,POLICY_INTENTS
from .understanding import FACETS,DOMAINS,MeaningTask
from .scope import norm,contains,requested_minutes
from .projection import title

VERSION='r135-request-verifier-v1'
DEFAULT={'C01':'description','C02':'role','C03':'name','C04':'summary','C05':'input_bindings','C06':'amount','C07':'amount_thb','C08':'owner_policy','C09':'owner_policy','C10':'owner_policy','C11':'open_periods','C12':'live_status','C13':'rule_clause','C14':'body'}
ALIASES={'date':'event_start','registration':'registration_url','closing_time':'open_periods'}

def clauses(question,index=None):
    # Only predicate-leading coordination, not an "and" within an entity name
    # or condition. Preserve original offsets and full surrounding qualifiers.
    from .routing import protected_source_spans
    protected=protected_source_spans(question,index)
    cuts=[m for m in re.finditer(r'[;\n]+|\s+and(?:\s+also)?\s+(?=(?:how|what|where|when|which|who|can|may|is|are)\b)|\s*แล้ว(?:ก็)?\s*(?=(?:ราคา|จอง|เปิด|ปิด|ขอ|ต้อง|ใช้|มีเกม|กี่))|\s*และ\s*(?=(?:ขอ|อยากรู้|ราคา|วิธีจอง|ขั้นตอน))',question,re.I) if not any(a<=m.start()<b for a,b in protected)]
    result=[];start=0
    for cut in [*cuts,None]:
        end=cut.start() if cut else len(question)
        a=start
        while a<end and question[a].isspace():a+=1
        b=end
        while b>a and question[b-1].isspace():b-=1
        if b>a:result.append({'start':a,'end':b,'text':question[a:b]})
        if cut:start=cut.end()
    return result

def observe(index,question):
    from .routing import route
    from .rule_semantics import requested_topics,explicit_competition
    from .named_spans import masked
    needs=[];uncertain=[];constraints=[]
    competition_context=explicit_competition(question,index)
    for part in clauses(question,index):
        from .execution_dependencies import referent_text
        text=part['text'];predicate_text=masked(index,referent_text(text));cat=route(index,predicate_text);found=[]
        from .payment_intent import predicate_text as payment_predicate_text
        predicate_text=payment_predicate_text(predicate_text)
        # Catalog "available/offered" and dated live occupancy are distinct
        # predicates. The word available alone cannot manufacture a live need.
        dated=bool(re.search(r'ตอนนี้|วันนี้|พรุ่งนี้|\b(?:now|today|tomorrow|occupied|already booked)\b|20\d\d-\d\d-\d\d|\d{1,2}:\d{2}',text,re.I))
        if re.search(PATTERNS['game_catalog'],text,re.I) and not dated:cat='C04'
        from .offering_intent import named_game_offering
        static_game_offering=named_game_offering(index,text)
        if static_game_offering:cat='C04'
        independent_business=bool(re.search(r'ราคา|กี่บาท|how much|\b(?:price|cost|fee|payment|refund|receipt)\b|วิธีจอง|ขั้นตอน.*จอง|how (?:do|to|can).{0,15}\b(?:book|reserve)\b',predicate_text,re.I))
        price_predicate=bool(re.search(r'ราคา|กี่บาท|how much(?!\s+(?:time|long|notice|waiting)\b)|\b(?:price|cost|fee)\b',predicate_text,re.I))
        if price_predicate and cat in {None,'C06','C07','C10'} and not re.search(r'คืนเงิน|refund|overpay|underpay|receipt|slip',text,re.I):
            cat='C07' if re.search(r'เหมา|แพ็กเกจ|\b(?:rental|packages?|full.day|half.day)\b',text,re.I) else 'C06'
        if competition_context and not independent_business:cat='C13'
        if cat=='C13':
            topics=requested_topics(text)
            found=[('C13','rule_clause','competition.'+topic) for topic in topics] or [('C13','rule_clause','')]
        else:
            policy=[]
            for intent,c,_,pattern in POLICY_INTENTS:
                if intent=='external_visitor' and price_predicate and not re.search(r'อนุญาต|เข้าได้|ใช้ได้ไหม|allowed|permitted|eligible|\b(?:can|may).{0,25}(?:use|enter|access)\b',text,re.I):continue
                if c in {'C08','C09','C10'}:
                    from .policy_scope import requested_actions
                    if intent not in requested_actions(predicate_text,c):continue
                if re.search(pattern,predicate_text,re.I):policy.append((c,'payer' if c=='C09' and intent=='payer' else 'owner_policy','policy.'+intent))
            # A policy mention inside a competition request belongs to that
            # competition. It is not a separate studio permission request.
            found.extend(policy)
            candidates=set([cat]) if cat else set()
            for c in ['C01','C02','C03','C04','C05','C06','C07','C14']:
                if index.bind(c,text):candidates.add(c)
            if re.search(PATTERNS['amount'],predicate_text,re.I) and cat not in {'C08','C09','C10'}:candidates.add('C07' if cat=='C07' else 'C06')
            # In this frame staff is the visitor's audience, not a request
            # for a staff directory. Explicit directory predicates stay separate.
            if (re.search(r'\b(?:staff|employees?)\b',predicate_text,re.I)
                and re.search(r'\b(?:access|enter|use|play)\b',predicate_text,re.I)
                and re.search(r'\b(?:non[- ]?students?|not\s+(?:a\s+)?student)\b',predicate_text,re.I)
                and not re.search(r'\b(?:list|directory|names?|personnel)\b|\bwho\s+(?:are|works?)\b',predicate_text,re.I)):
                candidates.discard('C02')
                if cat=='C02':cat=None
            for c in sorted(candidates-{None,'C08','C09','C10','C13'}):
                fields=[]
                for facet in FACETS.get(c,()):
                    pattern=PATTERNS.get(facet)
                    if pattern and re.search(pattern,predicate_text,re.I):fields.append(facet)
                if c=='C05' and re.search(r'ปุ่ม|กดอะไร|กดตรงไหน|\b(?:buttons?|controls?|bindings?)\b',predicate_text,re.I):fields=['input_bindings']
                if c=='C04' and 'game_catalog' in fields:
                    from .player_scope import requested_count
                    if 'players_max' in fields or requested_count(index,text) is not None:
                        fields.remove('game_catalog')
                        if 'players_max' not in fields:fields.append('players_max')
                if c=='C13':continue
                # Broad "what is" is framing when an explicit field is asked.
                if len(fields)>1:fields=[f for f in fields if f not in {'summary','description','display_name'}]
                # Cross-category source entity names are not extra needs. A
                # service label containing "PC" cannot turn its price into a
                # hardware/description question.
                if c!=cat:fields=[f for f in fields if f!='terms']
                if c!=cat and c not in {'C06','C07'}:fields=[f for f in fields if f not in {'summary','description','display_name','players_max','capacity_persons','location','value','operator'}]
                found.extend((c,ALIASES.get(f,f),'') for f in fields)
            # A category guess with no observed predicate is not an obligation
            # to invent/recover. The existing plan remains available, while the
            # residual text is explicitly left for semantic review.
        from .controller_catalog import request as controller_request
        if static_game_offering:found=[('C04','studio_services','')]
        controller=controller_request(index,text)
        if controller and not independent_business:
            found=[('C04','zone' if controller['group_by']=='zone' else 'game_catalog','')]
            span=controller['source_span'];constraints.append({'id':'rc'+str(len(constraints)+1),'kind':'input_device','source_span':{'start':part['start']+span['start'],'end':part['start']+span['end'],'text':span['text']},'owner_span':part,'semantic_application_verified':False})
        from .control_intent import request as control_request
        if control_request(index,text):found=[('C05','input_bindings','controls.requested_binding')]
        from .period_scope import request as period_request
        if period_request(index,text):found=[('C11','service_periods','calendar.named_play_period')]
        from .package_intent import request as package_request
        package=package_request(index,text)
        if package:
            cat='C07'
            found=[('C07',facet,'rental.named_package_field') for facet in package['facets']]
        from .policy_scope import topic_clarification
        if topic_clarification(text):
            found=[];uncertain.append({'source_span':part,'reason':'policy_topic_missing_predicate','status':'review_required'})
        # An equipment-use question about a "gaming PC" does not by itself
        # request a game definition. Keep explicit game nouns and source-bound
        # game titles, including separate coordinated questions.
        if any(c=='C03' and f=='usage' for c,f,_ in found) and re.search(r'\bgaming\s+(?:pc|computer)\b',text,re.I) and not re.search(r'\bgames?\b|เกม',text,re.I):
            bound_game=any(index.records.get(f['record_id'],{}).get('kind')=='game' for f in index.bind('C04',text))
            if not bound_game:found=[row for row in found if row[:2]!=('C04','summary')]
        unique=list(dict.fromkeys(found))
        if not unique and re.search(r'\?|\b(?:what|where|when|who|which|how|can|may)\b|อะไร|อย่างไร|ยังไง|กี่|ไหม|ที่ไหน',text,re.I):uncertain.append({'source_span':part,'reason':'unrecognised_factual_predicate','status':'review_required'})
        for c,facet,predicate in unique:
            needs.append({'id':'rn'+str(len(needs)+1),'category':c,'facet':facet,'predicate':predicate,'source_span':part,'basis':'independent_text_and_source_vocabulary_observation','semantic_accuracy_verified':False})
        constraint_text=masked(index,text)
        for kind,pattern in [('duration',r'\d+(?:\.\d+)?\s*(?:ชั่วโมง|นาที|hours?|hrs?|minutes?)'),('persons',r'\d+\s*(?:คน|people|persons?|players?)'),('sessions',r'\d+\s*(?:รอบ|sessions?)'),('date',r'20\d\d-\d\d-\d\d'),('time',r'(?<!\d)\d{1,2}:\d{2}(?!\d)'),('condition',r'(?:ถ้า|หาก|ยกเว้น|เว้นแต่|เฉพาะเมื่อ|ต่อเมื่อ|ไม่ใช่|ไม่ได้เป็น|\bonly\s+if\b|\bif\b|\bunless\b|\bprovided(?:\s+that)?\b|\bexcept\b|\bnot\b).+')]:
            for match in re.finditer(pattern,constraint_text,re.I):
                constraints.append({'id':'rc'+str(len(constraints)+1),'kind':kind,'source_span':{'start':part['start']+match.start(),'end':part['start']+match.end(),'text':text[match.start():match.end()]},'owner_span':part,'semantic_application_verified':False})
        if price_predicate:
            from .financial import resource_quantities
            for quantity in resource_quantities(index,text):constraints.append({'id':'rc'+str(len(constraints)+1),'kind':'resource_quantity','source_span':{'start':part['start']+quantity['start'],'end':part['start']+quantity['end'],'text':quantity['quote']},'owner_span':part,'semantic_application_verified':False})
        if cat=='C07':
            from .financial import rental_units
            for units in rental_units(text):constraints.append({'id':'rc'+str(len(constraints)+1),'kind':'package_quantity','source_span':{'start':part['start']+units['start'],'end':part['start']+units['end'],'text':units['quote']},'owner_span':part,'semantic_application_verified':False})
    return {'version':VERSION,'question':question,'needs':needs,'constraints':constraints,'uncertain':uncertain,'detector_completeness_claimed':False,'human_semantic_accuracy_claimed':False}

def matches(need,task):
    cat=task.category if hasattr(task,'category') else task.get('category')
    facet=task.facet if hasattr(task,'facet') else task.get('facet')
    predicate=task.canonical_operation if hasattr(task,'canonical_operation') else task.get('canonical_operation','')
    span=task.source_span if hasattr(task,'source_span') else task.get('source_span',{})
    a,b=(span.start,span.end) if hasattr(span,'start') else (span.get('start',0),span.get('end',0))
    source=need['source_span'];overlap=a<source['end'] and source['start']<b
    return bool(cat==need['category'] and ALIASES.get(facet,facet)==need['facet'] and overlap and (not need['predicate'].startswith('policy.') or predicate in {'',need['predicate']}))

def supplement(index,question,proposal):
    """Bounded typed correction only; no extra context/model inference.

    Policy/general tasks are not proof that every predicate is planned. Add
    distinct explicit fields only; ambiguous/unrecognised observations remain
    visible to the final verifier rather than fabricated tasks.
    """
    if not proposal.accepted:return proposal
    result=copy.deepcopy(proposal);observed=observe(index,question);added=[]
    for need in observed['needs']:
        def covered(task):
            start=question.find(task.quote)
            return matches(need,{'category':task.category,'facet':task.facet,'canonical_operation':task.canonical_operation,'source_span':{'start':start,'end':start+len(task.quote)}})
        if any(covered(t) for t in result.tasks):continue
        if len(result.tasks)>=32:continue
        cat=need['category'];facet=need['facet'];text=need['source_span']['text']
        domain=next(d for d,(c,_) in DOMAINS.items() if c==cat)
        operation='control' if cat=='C05' else 'rule_lookup' if cat=='C13' else 'availability' if cat=='C12' else 'price_calculate' if cat in {'C06','C07'} and facet in {'amount','amount_thb'} else 'detail'
        if re.search(r'\blist\b|ทั้งหมด|อะไรบ้าง',text,re.I) and facet in {'game_catalog','input_bindings'}:operation='list'
        result.tasks.append(MeaningTask(text,domain,cat,operation,facet,canonical_operation=need['predicate']))
        added.append({'need_id':need['id'],'task_index':len(result.tasks),'basis':'independent_explicit_predicate_typed_corrective_read','model_called':False})
    result.event={**result.event,'independent_request_observations':observed,'typed_corrective_tasks':added,'internal_task_limit':32}
    return result

def verify(index,question,contract,answer='',children=None):
    observed=observe(index,question);tasks=(contract.get('request_plan') or {}).get('tasks',[]);ledgers=contract.get('tasks',[]);executors=contract.get('executor_results',[])
    coverage=[];children=children or []
    from .execution_dependencies import evaluate as evaluate_dependency
    dependency_proofs={t['id']:evaluate_dependency(index,question,tasks,t['id'],executors,(contract.get('request_plan') or {}).get('snapshot',{})) for t in tasks if t.get('execution_dependencies')}
    for need in observed['needs']:
        matched=[t for t in tasks if matches(need,t)];task_ids={t['id'] for t in matched}
        receipts=[r for l in ledgers if l.get('task_id') in task_ids for r in l.get('receipts',[])]
        claims=[c for e in executors if e.get('task_id') in task_ids for c in e.get('claims',[])]
        compatible={need['facet']}
        if need['category']=='C04' and need['facet'] in {'game_catalog','zone'}:
            from .controller_catalog import request as controller_request,FACET
            if controller_request(index,need['source_span']['text']):compatible.add(FACET)
        if need['category']=='C11' and need['facet']=='open_periods':compatible.add('service_periods')
        if need['category']=='C12':supported=any(o.get('binding_mapping_and_clock_checked') and o.get('requested_date_and_window_verified') and o.get('terminal_state')=='supported' for e in executors if e.get('task_id') in task_ids for o in e.get('observation_receipts',[]))
        elif need['category']=='C05':supported=bool(claims or receipts)
        else:supported=any(c.get('facet') in compatible for c in claims) or any(r.get('field',r.get('facet')) in compatible for r in receipts)
        # A task about the whole rulebook is no evidence for an omitted topic.
        if need['predicate'].startswith('competition.'):
            from .rule_semantics import topic_matches,substantive
            topic=need['predicate'].split('.',1)[1]
            supported=any(topic_matches(topic,c.get('value','')) and substantive(c.get('value','')) for c in claims)
        if need['predicate'].startswith('policy.'):
            wanted=need['predicate'].split('.',1)[1]
            supported=supported and any(wanted in c.get('plan',{}).get('metadata',{}).get('policy_intents',[]) or c.get('plan',{}).get('metadata',{}).get('canonical_policy_intent')==wanted for c in children if c.get('execution_contract',{}).get('task_id') in task_ids)
            if not children:supported=False
        excluded=[dependency_proofs[t['id']] for t in matched if dependency_proofs.get(t['id'],{}).get('outcome')=='false' and dependency_proofs[t['id']].get('verified')]
        if excluded:supported=True
        fatal=any(l.get('fatal') for l in ledgers if l.get('task_id') in task_ids)
        complete=bool(matched and supported and not fatal)
        coverage.append({**need,'planned':bool(matched),'task_ids':sorted(task_ids),'source_receipts_present':bool(receipts),'delivered':complete,'status':'conditional_not_applicable' if complete and excluded else 'structurally_supported' if complete else 'review_required' if matched else 'uncovered','reason':'verified_prerequisite_condition_not_met' if complete and excluded else 'source_operation_projection_present' if complete else 'requested_need_not_source_verified' if matched else 'factual_need_omitted_from_plan','dependency_proofs':excluded})
    constraint_rows=[]
    for constraint in observed['constraints']:
        owner=constraint['owner_span'];related=[t for t in tasks if t['source_span']['start']<owner['end'] and owner['start']<t['source_span']['end']]
        ids={t['id'] for t in related};parts=[c for c in children if c.get('execution_contract',{}).get('task_id') in ids];verified=False;proof=[]
        if constraint['kind']=='input_device':
            from .controller_catalog import claim_errors,selection
            for child in parts:
                claims=child.get('claims',[]);q=owner['text'];declared=child.get('plan',{}).get('metadata',{}).get('controller_catalog_scope')
                if claims and not claim_errors(index,q,claims,contract['request_plan']['snapshot']['reference_time'],declared):
                    proof.append({'basis':'independently_recomputed_input_device_game_and_offering_relations','source_claim_refs':[c['fact_id'] for c in claims],'controller_scope':selection(index,q,contract['request_plan']['snapshot']['reference_time'])['proofs']})
            verified=bool(proof)
        if constraint['kind'] in {'duration','persons','sessions'}:
            text=constraint['source_span']['text'];number=float(re.search(r'\d+(?:\.\d+)?',text)[0]);expected=requested_minutes(text) if constraint['kind']=='duration' else number
            mixed_tasks=set()
            from .financial import audience_mentions
            from .mixed_price_dependencies import recompute as mixed_total
            for task in related:
                if task.get('category')!='C06' or task.get('operation')!='price_calculate':continue
                mixed_tasks.add(task['id']);executor=next((e for e in executors if e.get('task_id')==task['id']),None)
                try:
                    calculated=mixed_total(index,task,executor or {},(contract.get('request_plan') or {}).get('snapshot',{}))
                    if constraint['kind']=='persons':
                        for role in calculated['quantity_roles']:
                            span=role['source_span'];offset=task['source_span']['start']
                            if (span['start']+offset,span['end']+offset)==(constraint['source_span']['start'],constraint['source_span']['end']) and role['persons']==expected:proof.append({'basis':'source_audience_quantity_role_and_all_purchase_lines_recomputed','audience_id':role['audience_id'],'value':role['persons'],'source_claim_refs':calculated['source_claim_refs'],'source_quantity_role':role})
                    elif constraint['kind']=='sessions' and calculated['sessions']==expected:proof.append({'basis':'all_source_purchase_lines_share_recomputed_session_quantity','value':expected,'source_claim_refs':calculated['source_claim_refs']})
                    elif constraint['kind']=='duration' and all(line['unit_calculation']['requested_minutes']==expected for line in calculated['lines']):proof.append({'basis':'all_source_purchase_lines_share_recomputed_duration','value':expected,'source_claim_refs':calculated['source_claim_refs']})
                except (KeyError,ValueError,TypeError,ArithmeticError):pass
            for part in parts:
                if part.get('execution_contract',{}).get('task_id') in mixed_tasks:continue
                for calc in part.get('computations',[]):
                    actual=(calc.get('unit_calculation') or {}).get('requested_minutes') if constraint['kind']=='duration' else calc.get('billing_quantity') if constraint['kind']=='persons' else calc.get('sessions')
                    if actual==expected:proof.append({'fact_id':calc['fact_id'],'basis':'independently_observed_quantity_matches_calculation_receipt','value':actual})
            if constraint['kind']=='duration':
                # A single source rate for the exact requested period can prove
                # the period without inventing multi-period arithmetic.
                from .projection import value
                for task in related:
                    if task.get('category')!='C06':continue
                    query=task['source_span']['text']
                    spans=re.findall(r'\d+(?:\.\d+)?\s*(?:ชั่วโมง|นาที|hours?|hrs?|minutes?)',query,re.I)
                    if len(spans)!=1 or requested_minutes(spans[0])!=expected:continue
                    executor=next((e for e in executors if e.get('task_id')==task['id']),{})
                    ledger=next((l for l in ledgers if l.get('task_id')==task['id']),{})
                    for claim in executor.get('claims',[]):
                        fact=index.byid.get(claim.get('fact_id'),{});record=index.records.get(claim.get('record_id'),{})
                        if record.get('kind')!='rate' or claim.get('facet')!='amount' or fact.get('record_id')!=claim.get('record_id') or value(record,'duration_minutes')!=expected:continue
                        if fact.get('numeric') is None or fact.get('numeric')!=claim.get('numeric'):continue
                        receipts=[r for r in ledger.get('receipts',[]) if r.get('fact_id')==claim.get('fact_id') and r.get('record_revision')==record.get('revision') and r.get('value_validation')=='numeric_recomputed' and r.get('requested_scope',{}).get('verified')]
                        if any(any(e.get('locator','').endswith('/duration_minutes') for e in r.get('evidence_refs',[])) for r in receipts):
                            proof.append({'fact_id':claim['fact_id'],'basis':'exact_single_source_rate_duration_and_scoped_receipt_recomputed','value':expected})
            verified=bool(proof)
            if constraint['kind']=='persons':
                from .player_scope import selection
                for task in related:
                    if task.get('category')!='C04' or task.get('facet')!='players_max':continue
                    scoped=selection(index,task['source_span']['text']);executor=next((e for e in executors if e.get('task_id')==task['id']),{})
                    actual=[c for c in executor.get('claims',[]) if c.get('facet')=='players_max'];allowed={f['id'] for f in scoped['facts']}
                    if scoped['requested_count']==expected and actual and all(c['fact_id'] in allowed for c in actual):proof.append({'basis':'source_game_mode_minimum_and_maximum_recomputed','requested_count':expected,'mode_proofs':[scoped['proofs'][c['fact_id']] for c in actual]})
                verified=bool(proof)
        if constraint['kind']=='condition':
            from .package_intent import price_scenario
            scenario=price_scenario(index,owner['text'])
            if scenario and constraint['source_span']['text'].startswith(scenario['scenario_span']['text']):
                # Text, amount and revision are recomputed; a receipt flag or
                # the word package alone cannot establish this narrow scenario.
                for child in parts:
                    for claim in child.get('claims',[]):
                        fact=index.byid.get(claim.get('fact_id'),{});record=index.records.get(scenario['record_id'],{})
                        if not fact or fact.get('record_id')!=scenario['record_id'] or fact.get('facet')!='amount_thb' or fact.get('numeric') is None or claim.get('numeric')!=fact['numeric'] or claim.get('value') not in fact.get('value',{}).values():continue
                        receipts=child.get('execution_contract',{}).get('receipts',[])
                        if any(r.get('fact_id')==fact['id'] and r.get('record_revision')==record.get('revision') and r.get('snapshot')==contract['request_plan']['snapshot'] and r.get('requested_scope',{}).get('verified') and r.get('value_validation')=='numeric_recomputed' for r in receipts):
                            proof.append({'basis':'sole_hypothetical_named_package_unit_price_source_recomputed','record_id':scenario['record_id'],'fact_id':fact['id'],'scenario_span':scenario['scenario_span'],'unit_count':1,'permission_or_booking_confirmed':False})
            for tid in ids:
                dependency=dependency_proofs.get(tid,{})
                edge=dependency.get('edge',{})
                if dependency.get('verified') and edge.get('source_span')==owner and (edge.get('condition_span') or {}).get('text') and constraint['source_span']['text'].startswith(edge['condition_span']['text']):proof.append({'basis':'source_prerequisite_condition_recomputed','outcome':dependency['outcome'],'source_claim_refs':dependency['source_claim_refs'],'dependency':dependency})
            verified=bool(proof)
        if constraint['kind'] in {'date','time'}:
            text=constraint['source_span']['text']
            if constraint['kind'] in {'date','time'}:
                from .policy_scope import applicability
                for task in related:
                    if task.get('category') not in {'C08','C09','C10'}:continue
                    executor=next((e for e in executors if e.get('task_id')==task['id']),{})
                    for claim in executor.get('claims',[]):
                        fact=index.byid.get(claim.get('fact_id'))
                        if not fact or fact['category']!=task['category']:continue
                        current=applicability(index,fact,owner['text'],contract['request_plan']['snapshot']['reference_time'])
                        receipt=next((r for r in executor.get('receipts',[]) if r.get('fact_id')==claim.get('fact_id')),{})
                        matches_time=current['requested_reference_time'].startswith(text+'T') if constraint['kind']=='date' else current['requested_reference_time'][11:16]==text.zfill(5)
                        if current['state']=='within_recorded_interval' and matches_time and receipt.get('record_revision')==index.records[fact['record_id']]['revision'] and receipt.get('requested_scope',{}).get('policy_applicability')==current and all(ref in claim.get('evidence_refs',[]) for ref in fact['evidence_refs']):
                            proof.append({'fact_id':fact['id'],'basis':'raw_requested_policy_date_and_source_interval_recomputed','value':text,'policy_applicability':current})
            # A native compound retains source claims/receipts, while the
            # outer verifier may have no original typed child metadata.
            # Recompute the calendar from this exact task and pinned source.
            from .boolean_dependencies import calendar_projection
            for task in related:
                if task.get('category')!='C11':continue
                executor=next((e for e in executors if e.get('task_id')==task['id']),None)
                if executor is None:continue
                try:
                    calendar,_=calendar_projection(index,task,executor,(contract.get('request_plan') or {}).get('snapshot',{}))
                    meta=calendar.metadata;window=(meta.get('calendar_window_evaluation') or {}).get('requested_window') or {}
                    if meta.get('local_date')==text if constraint['kind']=='date' else text in {window.get('start'),window.get('end')}:proof.append({'fact_id':meta['calendar_service_fact_id'],'basis':'current_task_calendar_projection_recomputed_from_source_receipts','value':text})
                except (KeyError,ValueError,TypeError,AttributeError):pass
            for part in parts:
                meta=part.get('plan',{}).get('metadata',{})
                receipts=part.get('execution_contract',{}).get('receipts',[])
                if constraint['kind']=='date' and meta.get('named_period_receipt'):
                    from .period_scope import verify as verify_period
                    from types import SimpleNamespace
                    exact=part.get('execution_query',part.get('question',owner['text']))
                    source_clock=contract['request_plan']['snapshot']['reference_time']
                    scope=meta['named_period_receipt'].get('scope',{})
                    if scope.get('local_date')==text and verify_period(index,SimpleNamespace(facet='service_periods'),part.get('claims',[]),meta,exact,source_clock) and {r.get('fact_id') for r in receipts}=={c['fact_id'] for c in part.get('claims',[])}:
                        proof.append({'fact_id':part['claims'][0]['fact_id'],'basis':'named_service_period_date_weekday_and_source_receipts_recomputed','value':text})
                calendar_checked=any(r.get('value_validation')=='registered_calendar_projection_recomputed' for r in receipts)
                window=(meta.get('calendar_window_evaluation') or {}).get('requested_window') or {}
                if calendar_checked and (meta.get('local_date')==text if constraint['kind']=='date' else text in {window.get('start'),window.get('end')}):
                    proof.append({'fact_id':meta['calendar_service_fact_id'],'basis':'reconstructed_source_calendar_request_projection','value':text})
                if constraint['kind']=='date':
                    for receipt in receipts:
                        profile=receipt.get('requested_scope',{}).get('person_profile_scope',{})
                        if profile.get('requested_interval_fully_covered') and any(a.startswith(text+'T') for a,b in profile.get('requested_intervals',[])):
                            proof.append({'fact_id':receipt['fact_id'],'basis':'public_person_source_interval_covers_requested_date','value':text})
            for executor in executors:
                if executor.get('task_id') not in ids:continue
                for observation in executor.get('observation_receipts',[]):
                    if not observation.get('binding_mapping_and_clock_checked') or not observation.get('requested_date_and_window_verified'):continue
                    window=observation.get('requested_window') or {}
                    applies=observation.get('target_date')==text if constraint['kind']=='date' else text in {window.get('start'),window.get('end')}
                    if applies:
                        proof.append({'binding_id':observation['binding_id'],'basis':'independent_provider_snapshot_date_window_check','value':text})
            verified=bool(proof)
        if constraint['kind']=='package_quantity':
            from .financial import rental_units
            from .projection import value
            units=rental_units(constraint['source_span']['text'])
            if len(units)==1 and units[0]['quantity']==1:
                for part in parts:
                    for claim in part.get('claims',[]):
                        record=index.records.get(claim.get('record_id'),{})
                        day=units[0]['unit'] in {'วัน','day','days'}
                        if record.get('kind')=='rental_package' and claim.get('facet')=='amount_thb' and (not day or value(record,'period_label')=='full_day'):
                            proof.append({'fact_id':claim['fact_id'],'basis':'one_declared_source_package_unit_without_extrapolation','value':1})
            verified=bool(proof)
        # Other constraints require their native source/date/condition verifier;
        # mere presence inside a task quote is not evidence of application.
        if constraint['kind']=='date':
            from .controller_catalog import request as controller_request,claim_errors,selection
            if controller_request(index,owner['text']):
                for child in parts:
                    claims=child.get('claims',[]);ref=contract['request_plan']['snapshot']['reference_time']
                    if claims and not claim_errors(index,owner['text'],claims,ref,child.get('plan',{}).get('metadata',{}).get('controller_catalog_scope')):
                        current=selection(index,owner['text'],ref)['proofs']
                        if current and all(p['requested_reference_time'][:10]==constraint['source_span']['text'] and not p['validity_unconfirmed'] for p in current.values()):proof.append({'basis':'controller_game_offering_validity_intervals_recomputed','value':constraint['source_span']['text'],'source_claim_refs':[c['fact_id'] for c in claims]})
                verified=bool(proof)
        constraint_rows.append({**constraint,'planned_task_ids':sorted(ids),'status':'structurally_supported' if verified else 'review_required','proof':proof})
    unsupported=[r['id'] for r in coverage if not r['delivered']];unplanned=[r['id'] for r in coverage if not r['planned']]
    unresolved=[o for l in ledgers for o in l.get('obligations',[]) if o.get('fulfilled') is not True]
    unresolved.extend({'id':'request:'+c['id'],'kind':'request_constraint','expected':c['source_span']['text'],'task_ids':c['planned_task_ids'],'fulfilled':False,'reason':'request_constraint_application_unverified'} for c in constraint_rows if c['status']=='review_required')
    fatals=[f for l in ledgers for f in l.get('fatal',[])]
    return {'version':VERSION,'observations':observed,'plan_coverage':{'status':'uncovered' if unplanned else 'review_required' if observed['uncertain'] or not coverage else 'observed_needs_planned','needs':coverage,'uncovered_need_ids':unplanned,'complete_natural_language_detection_claimed':False},
      'constraint_coverage':{'status':'review_required' if any(c['status']=='review_required' for c in constraint_rows) else 'observed_constraints_verified','constraints':constraint_rows},
      'execution_coverage':{'status':'incomplete' if unresolved or unplanned else 'planned_operations_completed','unresolved_obligations':unresolved,'unplanned_need_ids':unplanned},
      'evidence_support':{'status':'rejected' if fatals else 'receipt_checks_passed' if any(l.get('receipts') for l in ledgers) else 'unconfirmed','fatal':fatals,'semantic_entailment_verified':False},
      'answer_coverage':{'status':'incomplete' if unsupported else 'review_required','undelivered_need_ids':unsupported,'rendered_nonempty':bool(answer.strip()),'semantic_review_required':True},
      'whole_question_semantics_verified':False,'requires_partial_delivery':bool(unplanned or any(c['status']=='review_required' for c in constraint_rows)),'human_semantic_accuracy_claimed':False}


def delivery_notice(verified,lang):
    missing=[n['source_span']['text'] for n in verified['plan_coverage']['needs'] if not n['planned']]
    constraints=[c['source_span']['text'] for c in verified['constraint_coverage']['constraints'] if c['status']=='review_required']
    parts=[]
    if missing:parts.append(('ส่วนที่ยังไม่มีแผนประมวลผลที่ยืนยันได้: ' if lang=='th' else 'Parts without a verified execution plan: ')+'; '.join(dict.fromkeys(missing)))
    if constraints:parts.append(('ยังยืนยันการใช้เงื่อนไขต่อไปนี้ในคำตอบไม่ได้: ' if lang=='th' else 'Application of these requested constraints remains unverified: ')+'; '.join(dict.fromkeys(constraints)))
    if any(c['kind']=='resource_quantity' and c['status']=='review_required' for c in verified['constraint_coverage']['constraints']):parts.append('ยังยืนยันวิธีคิดราคารวมตามจำนวนเครื่องที่ขอไม่ได้ ราคาแสดงเฉพาะหน่วยที่มีหลักฐาน' if lang=='th' else 'A total for the requested number of machines is not confirmed; shown prices cover only the recorded billing unit.')
    return '\n'.join(parts)


def attach_constraint_obligations(contract,verified):
    """Keep task status and ExecutorResult consistent with request constraints."""
    if verified.get('delivery_invalidated'):return
    from .terminal_states import PUBLIC
    for ledger in contract.get('tasks',[]):
        task_id=ledger['task_id'];rows=[c for c in verified.get('constraint_coverage',{}).get('constraints',[]) if task_id in c['planned_task_ids']]
        if not rows:continue
        new=[{'id':'request:'+c['id']+':'+task_id,'kind':'request_constraint','expected':c['source_span']['text'],'fulfilled':c['status']=='structurally_supported','reason':None if c['status']=='structurally_supported' else 'request_constraint_application_unverified','proof':c['proof']} for c in rows]
        ledger['obligations']=[o for o in ledger.get('obligations',[]) if o.get('kind')!='request_constraint']+new
        ledger['all_obligations_fulfilled']=all(o.get('fulfilled') is True for o in ledger['obligations'])
        if any(not o['fulfilled'] for o in new):
            ledger['reason_codes']=list(dict.fromkeys([*ledger.get('reason_codes',[]),'request_constraint_application_unverified']))
            if ledger['terminal_state']=='supported':ledger['terminal_state']='partial'
        for executor in contract.get('executor_results',[]):
            if executor.get('task_id')!=task_id:continue
            executor.update(status=ledger['terminal_state'],public_status=PUBLIC[ledger['terminal_state']])
            for key,wanted in [('resolved_obligations',True),('unresolved_obligations',False)]:
                executor[key]=[o for o in executor.get(key,[]) if o.get('kind')!='request_constraint']+[o for o in new if o['fulfilled'] is wanted]
