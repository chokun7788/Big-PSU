"""One domain execution path for snapshots, chat and source-contract evaluation."""
import re,time,threading
from collections import OrderedDict
from decimal import Decimal
from .contracts import Plan,RequestBudget
from .index import FactIndex
from .model import EvidenceSelector
from .scope import reference_time,norm,contains,years,requested_years,validity_allows,requested_minutes,in_year,event_years
from .routing import route,split_needs
from .readers import read,blocked
from .projection import compile_snapshot

_INDEX_CACHE=OrderedDict();_INDEX_LOCK=threading.Lock()

def language(question,locale):
    if locale in {'th','en'}:return locale
    return 'th' if re.search('[\u0e00-\u0e7f]',question) else 'en'

class Engine:
    def __init__(self,data,selector=None,provider=None,_index=None):
        self.index=_index or FactIndex(data);self.data=data;self.selector=selector or EvidenceSelector();self.provider=provider
        from .capabilities import catalog_for
        if not hasattr(self.index,'capability_catalog'):self.index.capability_catalog=catalog_for(self.index)
        self.capability_catalog={**self.index.capability_catalog,'snapshot':{'release_id':data.get('release_id'),'epoch':data.get('epoch')}}

    @classmethod
    def from_snapshot(cls,snapshot,cache_key=None,**kwargs):
        if cache_key is None:return cls(compile_snapshot(snapshot),**kwargs)
        key=(str(cache_key),snapshot.get('active'),snapshot.get('epoch'),bool(snapshot.get('evaluation_draft_only')),tuple(snapshot.get('withdrawn',[])))
        with _INDEX_LOCK:
            cached=_INDEX_CACHE.get(key)
            if cached is None:
                data=compile_snapshot(snapshot);cached=(data,FactIndex(data));_INDEX_CACHE[key]=cached
                while len(_INDEX_CACHE)>4:_INDEX_CACHE.popitem(last=False)
            else:_INDEX_CACHE.move_to_end(key)
        return cls(cached[0],_index=cached[1],**kwargs)

    def plan(self,category,question,at=None,meaning=None):
        from .hybrid_policy import plan
        return plan(self,category,question,at,meaning,self._r135_plan)

    def _r135_plan(self,category,question,at=None,meaning=None):
        if category=='C10' and meaning is not None and meaning.ambiguous:
            from .policy_scope import topic_clarification
            prompt=topic_clarification(question)
            if prompt:
                result=blocked(category,'policy_topic_missing_predicate','missing_input');result.metadata['context_clarification']=prompt;return result
        if category=='C11' and meaning is not None and meaning.facet=='service_periods':
            from .period_scope import plan as period_plan
            period=period_plan(self.index,question,reference_time(at))
            if period is not None:return period
            return blocked('C11','native_named_period_scope_not_identified','missing_input')
        from .duration_scope import guard as duration_guard
        duration=duration_guard(self.index,category,question,meaning)
        if duration is not None:return duration
        from .controller_catalog import plan as controller_plan
        controller=controller_plan(self.index,category,question,reference_time(at))
        if controller is not None:return controller
        from .source_decisions import plan as source_decision
        scoped=source_decision(self.index,question,reference_time(at),category)
        if scoped is not None:return scoped
        from .readers import guard
        safety=guard(self.index,category,norm(question),reference_time(at))
        if safety is not None:return safety
        if meaning is not None and meaning.ambiguous:
            from .meaning_reader import apply
            return apply(self.index,question,meaning,blocked(category,'meaning_requires_clarification','missing_input'),reference_time(at))
        from .comparison_executor import execute as compare
        comparison=compare(self.index,category,question,meaning,reference_time(at))
        if comparison is not None:return comparison
        if category=='C04':
            from .precision import ambiguous_game_variants
            ambiguity=ambiguous_game_variants(self.index,question)
            if ambiguity is not None:return ambiguity
        from .source_operations import native_operation
        native=native_operation(self.index,category,question,meaning)
        if native is not None:
            if meaning is not None and meaning.operation=='compare':
                native.metadata['operator']='compare'
                if category=='C06' and meaning.facet=='amount':native.metadata.setdefault('comparison_options',{fid:question for fid in native.ids})
            return native
        result=read(self.index,category,question,reference_time(at))
        if meaning is not None:
            from .meaning_reader import apply
            result=apply(self.index,question,meaning,result,reference_time(at))
            if meaning.operation=='compare':
                result.metadata['operator']='compare'
                if category=='C06' and meaning.facet=='amount':result.metadata.setdefault('comparison_options',{fid:question for fid in result.ids})
        return result

    def scoped_candidates(self,category,question,plan,at=None):
        if plan.reason in {'entity_not_bound','domain_not_bound'}:return []
        pool=[self.index.byid[k] for k in plan.candidates if k in self.index.byid]
        if category=='C13':
            asked=event_years(self.index,question)
            from .scope import rule_source_years
            if asked:pool=[f for f in pool if asked<=rule_source_years(self.index,f)]
            from .scope import rule_edition_events
            editions=rule_edition_events(self.index,question,pool)
            if editions is not None:pool=[f for f in pool if f.get('event_id') in editions]
        if plan.facets:
            strict=[f for f in pool if f['facet'] in plan.facets]
            pool=strict
        return [f for _,f in self.index.rank(category,question,pool=pool,limit=24)]

    def finish_plan(self,category,question,plan,at):
        # The model only sees a scoped pool, and selection must remain in that
        # pool. A cross-category/source ID can never enter the renderer.
        selected=[self.index.byid[k] for k in plan.ids if k in self.index.byid and self.index.byid[k]['category']==category]
        if len(selected)!=len(plan.ids):return blocked(category,'invalid_or_cross_category_fact','unavailable')
        if category=='C04':
            from .controller_catalog import selection,scope_identity,FACET
            controller=selection(self.index,question,at)
            if controller is not None:
                expected={f['id'] for f in controller['facts']}
                if set(plan.ids)!=expected or scope_identity(plan.metadata.get('controller_catalog_scope'))!=scope_identity(controller):return blocked(category,'controller_catalog_source_scope_not_verified')
            elif any(f['facet']==FACET for f in selected):return blocked(category,'controller_facts_require_input_device_scope')
        if category=='C13' and selected:
            from .rule_dependencies import proof
            dependencies=proof(self.index,question,plan.metadata.get('operator','rule_lookup'),at,plan.ids)
            if dependencies['errors'] or dependencies['missing_fact_ids']:return blocked(category,'rule_dependency_closure_not_confirmed')
            plan.metadata['rule_dependency_proof']=dependencies
            if dependencies['limits']:plan.status='partial'
        if category=='C10' and any(f.get('policy_complete') is False for f in selected):
            gaps=[f['id'] for f in selected if f.get('policy_complete') is False];selected=[f for f in selected if f['id'] not in gaps]
            if not selected:return blocked(category,'policy_conditions_or_exceptions_not_confirmed')
            plan.ids=[f['id'] for f in selected];plan.status='partial';plan.metadata['policy_source_gaps']=gaps
            if plan.metadata.get('recorded_source_collection'):plan.metadata.update(complete_set=False,member_ids=sorted({f['record_id'] for f in selected}),delivered_source_entries=len(selected))
        if category in {'C08','C09','C10'} and selected:
            from .policy_scope import applicability
            proofs={f['id']:applicability(self.index,f,question,at) for f in selected}
            if any(p['error'] for p in proofs.values()):
                result=blocked(category,next(p['error'] for p in proofs.values() if p['error']),'missing_input');result.metadata['context_clarification']={'th':'ต้องการตรวจนโยบายที่ใช้กับวันที่และเวลาใดครับ หากมีหลายกรณี กรุณาแยกวันและเวลาของแต่ละกรณี','en':'Which date and time should the policy apply to? Please separate dates and times belonging to different cases.'};return result
            allowed=[f for f in selected if proofs[f['id']]['allowed']]
            if not allowed:return blocked(category,'policy_not_effective_for_request','not_current')
            if len(allowed)!=len(selected) and plan.metadata.get('recorded_source_collection'):plan.metadata.update(complete_set=False,member_ids=sorted({f['record_id'] for f in allowed}),delivered_source_entries=len(allowed))
            if len(allowed)!=len(selected) or any(p['state']=='validity_interval_unconfirmed' for p in proofs.values()):plan.status='partial'
            selected=allowed;plan.ids=[f['id'] for f in selected];plan.metadata['policy_applicability']={f['id']:proofs[f['id']] for f in selected}
            from .policy_scope import procedure_limits
            limits={f['id']:procedure_limits(self.index.records[f['record_id']]) for f in selected if self.index.records[f['record_id']]['kind']=='procedure'}
            if any(limits.values()):plan.status='partial';plan.metadata['procedure_source_limits']=limits
        if category=='C04':
            from .game_scope import relation_projection
            from .player_scope import selection
            player=selection(self.index,question) if any(f['facet']=='players_max' for f in selected) else None
            for f in selected:
                if f['facet']=='players_max':
                    if f['id'] not in player['proofs']:return blocked(category,'requested_player_mode_not_recorded')
                    plan.metadata.setdefault('player_filter_proofs',{})[f['id']]=player['proofs'][f['id']]
                projection=relation_projection(self.index,f,question)
                if projection is not None:
                    if not projection['target_ids']:return blocked(category,'game_offering_not_confirmed_in_requested_platform')
                    plan.metadata.setdefault('game_relation_projections',{})[f['id']]=projection
        if category=='C05' and selected:
            from .control_scope import requested_button_count,physical_subset
            count=requested_button_count(self.index,question)
            if count is not None:
                if count<=0 or int(count)!=count:return blocked(category,'invalid_physical_button_count','missing_input')
                subset=physical_subset(self.index,question,selected);plan.metadata['physical_button_subset']=subset
                if not subset['verified']:
                    plan.status='partial';plan.reason='requested_control_subset_not_identified'
                    plan.metadata.update(requested_binding_count=int(count),recorded_binding_entries=len(selected),complete_set=False)
        if category=='C05':
            from .requested_output import allows as device_allows
            if any(not device_allows(self.index,question,f) for f in selected):
                p=blocked(category,'requested_input_device_not_source_verified')
                p.metadata['execution_notice']={'th':'ยังไม่มีผังควบคุมที่ยืนยันสำหรับอุปกรณ์ที่ถาม กรุณาระบุแพลตฟอร์มหรืออุปกรณ์ที่ใช้ครับ','en':'No verified control layout is recorded for the requested input device. Please specify the platform or device.'}
                return p
        if category=='C03':
            from .equipment_dimensions import allows
            if any(not allows(f,question) for f in selected):return blocked(category,'equipment_count_basis_not_confirmed')
        if category=='C14':
            from .news_scope import candidates,publication
            allowed={f['record_id'] for f in candidates(self.index,question)}
            if len(allowed)>1 and selected:return blocked(category,'news_event_edition_requires_clarification','missing_input')
            if selected and any(f['record_id'] not in allowed for f in selected):return blocked(category,'news_event_identity_not_confirmed')
            proofs={f['id']:publication(self.index,f,question,at) for f in selected}
            if any(not p['allowed'] for p in proofs.values()):return blocked(category,'news_publication_not_effective','not_current')
            plan.metadata['news_publication_scope']=proofs
            if any(p['state']=='publication_period_unconfirmed' for p in proofs.values()):plan.status='partial'
            for f in selected:
                if f['facet']!='status':continue
                from .news_scope import status_date_observed
                if not status_date_observed(question,at):return blocked(category,'registration_status_requested_date_not_observed','not_current')
                from ..registry import aware
                try:age=(at-aware(f['status_observed_at'])).total_seconds();fresh=0<=age<=f['freshness_max_age_seconds']
                except (KeyError,TypeError,ValueError):fresh=False;age=None
                if not fresh:return blocked(category,'registration_status_not_current','not_current')
                plan.metadata.setdefault('registration_status_freshness',[]).append({'fact_id':f['id'],'as_of':f['status_observed_at'],'age_seconds':age,'max_age_seconds':f['freshness_max_age_seconds'],'clock':at.isoformat(),'event_schedule_is_not_registration_status':True})
        if category=='C13' and selected:
            from .rule_semantics import select_topics
            coverage=select_topics(self.index,question,selected)
            if coverage:
                if not coverage['facts']:return blocked(category,'requested_operation_not_satisfied')
                plan.metadata.update(requested_rule_topics=coverage['requested'],covered_rule_topics=coverage['covered'],missing_rule_topics=coverage['missing'])
                if coverage['missing']:plan.status='partial';plan.reason='requested_rule_topics_not_recorded'
        if category=='C06':
            from .rate_bounds import source_scope
            proofs={f['id']:source_scope(self.index,f) for f in selected if f['facet']=='amount'}
            rejected={fid for fid,p in proofs.items() if not p['allowed']}
            if rejected:
                selected=[f for f in selected if f['id'] not in rejected];plan.ids=[f['id'] for f in selected]
                plan.status='partial' if selected else 'missing_source'
                plan.metadata['person_bounds_withheld']=sorted(rejected)
                plan.metadata['execution_notice']={'th':'ข้อมูลขอบเขตจำนวนคนของบางอัตรายังไม่ครบหรือแข่งขันกัน จึงยังยืนยันอัตราส่วนนั้นไม่ได้','en':'Some person-rate scopes are incomplete or competing; those rates are not confirmed.'}
            ranged={fid:p for fid,p in proofs.items() if p.get('ranged') and fid not in rejected}
            if ranged:
                plan.metadata['source_person_ranges']=ranged
                plan.metadata['arithmetic_unconfirmed']=sorted(set(plan.metadata.get('arithmetic_unconfirmed',[]))|set(ranged))
                plan.status='partial'
        from .precision import validate
        plan=validate(self.index,category,question,plan)
        if not plan.ids:return plan
        if category=='C02':
            from .person_scope import check as person_scope
            people={f['record_id'] for f in selected if self.index.records.get(f['record_id'],{}).get('kind')=='person'}
            scope={rid:person_scope(self.index.records[rid],question,at,period_only=all(f['facet']=='period' for f in selected if f['record_id']==rid)) for rid in people}
            excluded={rid for rid,p in scope.items() if not p['allowed']}
            if excluded:
                selected=[f for f in selected if f['record_id'] not in excluded];plan.ids=[f['id'] for f in selected]
                if not selected:return blocked(category,next(iter(scope.values()))['reason'],'not_current' if any('current' in p.get('reason','') or 'effective' in p.get('reason','') for p in scope.values()) else 'missing_source')
                plan.status='partial';plan.metadata['person_profile_subset']=True
            plan.metadata['person_scope_proofs']={rid:p for rid,p in scope.items() if p['allowed']}
            if any(p.get('state')=='effective_period_unknown' for p in scope.values() if p['allowed']):plan.status='partial';plan.metadata['person_period_unconfirmed']=True
            if any(p.get('requested_interval_fully_covered') is False for p in scope.values() if p['allowed']):plan.status='partial';plan.metadata['person_requested_period_partial']=True
        from app.pipeline.protected_intents import _food_facet
        if category=='C10' and _food_facet(question)=='food_bring_permission':
            # Consumption does not establish permission to bring an item.
            consumption=any(re.search(r'บริโภค|รับประทาน|กิน|\b(?:consum\w*|eat\w*)\b',' '.join(f['value'].values()),re.I) for f in selected)
            explicit_permission=all(f.get('service_policy_claim')=='food_bring' or _food_facet(' '.join((f.get('faq_question') or {}).values()))=='food_bring_permission' for f in selected)
            if consumption and not explicit_permission:
                plan.status='partial';plan.metadata['consumption_not_bring_permission']=True
        asked=event_years(self.index,question) if category=='C13' else requested_years(question)
        if category=='C13' and asked:
            options=set(plan.metadata.get('comparison_option_ids',[]))
            if options:
                from .scope import rule_source_years
                observed=set().union(*(rule_source_years(self.index,f) for f in selected))
                if not asked<=observed or any(f.get('event_id') not in options for f in selected):return blocked(category,'selected_rule_comparison_scope_mismatch')
            else:
                from .scope import rule_source_years
                if any(not asked<=rule_source_years(self.index,f) for f in selected):return blocked(category,'selected_rule_event_year_mismatch')
        if category in {'C06','C07'} and selected:
            if category=='C07':
                from .financial import rental_units
                units=rental_units(question)
                if any(u['quantity']!=1 for u in units):plan.status='partial';plan.metadata['package_quantity_unconfirmed']=units
            price=[f for f in selected if f['facet'] in {'amount','amount_thb'}]
            requested_at=in_year(at,next(iter(asked))) if len(asked)==1 else at
            if category=='C07':
                applicability={f['record_id']:{'record_revision':self.index.records[f['record_id']]['revision'],'reference_time':requested_at.isoformat(),'validity':f['validity'],'state':'unconfirmed_interval' if validity_allows(f,requested_at) is None else 'within_interval' if validity_allows(f,requested_at) else 'outside_interval'} for f in selected if self.index.records[f['record_id']]['kind']=='rental_package'}
                plan.metadata['rental_source_applicability']=applicability
                if any(p['state']=='unconfirmed_interval' for p in applicability.values()):plan.status='partial'
            expired=[f for f in price if validity_allows(f,requested_at) is False and not (f.get('confirmation_ref') and (not asked or asked=={at.year}))]
            if expired:return blocked(category,'rate_not_effective_for_request','not_current')
            acknowledgements=[f.get('confirmation_as_of') for f in price if f.get('confirmation_as_of')]
            if acknowledgements:
                confirmation=max(acknowledgements);plan.metadata['price_confirmation_as_of']=confirmation
                from datetime import date
                from .temporal import parse as parse_date
                target_day,_=parse_date(question,at.date())
                date_signal=bool(re.search(r'วันนี้|พรุ่งนี้|วันที่|\b(?:today|tomorrow|monday|tuesday|wednesday|thursday|friday|saturday|sunday)\b|20\d\d[-/]\d{1,2}[-/]\d{1,2}',question,re.I))
                if target_day is None and date_signal:
                    from app.calendar.service_calendar import resolve_date_from_text
                    resolution=resolve_date_from_text(question,today=at.date())
                    if resolution:target_day=resolution.target_date
                target_day=target_day or at.date()
                confirmed_day=date.fromisoformat(str(confirmation)[:10])
                dated=at.replace(year=target_day.year,month=target_day.month,day=target_day.day)
                effective=all(validity_allows(f,dated) is True for f in price)
                if not effective and (target_day<confirmed_day or target_day>at.date()):
                    plan.status='partial';plan.reason='rate_date_applicability_not_confirmed'
                    plan.metadata['rate_date_applicability_unconfirmed']={'requested_date':target_day.isoformat(),'confirmation_as_of':confirmed_day.isoformat()}
            if category=='C06':
                from .financial import quantity_text,unit_calculation
                quantity_q=quantity_text(self.index,question,selected)
                count_match=re.search(r'(\d+)\s*(?:คน|people|persons?|players?)',quantity_q)
                persons=int(count_match[1]) if count_match else 1
                billing_counts={line['fact_id']:line['persons'] for line in plan.metadata.get('billing_lines',[])}
                for f in price:
                    if f['id'] in plan.metadata.get('source_person_ranges',{}):continue  # display source ranges, never multiply them
                    scoped_persons=billing_counts.get(f['id'],persons)
                    calc=unit_calculation(self.index,f,plan.metadata.get('comparison_options',{}).get(f['id'],question))
                    if calc.get('error'):
                        if calc['error']=='duration_arithmetic_not_declared':
                            plan.status='partial';plan.reason=calc['error']
                            plan.metadata.setdefault('arithmetic_unconfirmed',[]).append(f['id']);continue
                        return blocked(category,calc['error'],calc['status'])
                    plan.metadata.setdefault('unit_calculations',{})[f['id']]=calc
                    per_person=f.get('confirmed_per_person') or f.get('billing_unit')=='per_person' or f.get('calculation')=='integer_sessions_per_person'
                    if scoped_persons>1 and not per_person and f.get('billing_unit')!='per_group':return blocked(category,'per_person_billing_basis_not_confirmed')
                    if f.get('billing_unit')=='per_group' and (f.get('persons_min') and scoped_persons<f['persons_min'] or f.get('persons_max') and scoped_persons>f['persons_max']):return blocked(category,'group_size_outside_confirmed_rate_scope','missing_input')
        return plan

    def _render_one(self,category,question,locale,plan,at):
        lang=language(question,locale);selected=[self.index.byid[k] for k in plan.ids]
        claims=[];blocks=[];computations=[];shown_subjects=set()
        from .financial import quantity_text
        quantity_q=quantity_text(self.index,question,selected)
        m=re.search(r'(\d+)\s*รอบ|\b(\d+)\s+sessions?\b',quantity_q);sessions=int(next(x for x in m.groups() if x)) if m else 1
        people=re.search(r'(\d+)\s*คน|\b(\d+)\s+(?:people|persons?|players?)\b',quantity_q);persons=int(next(x for x in people.groups() if x)) if people else 1
        billing={x['fact_id']:x for x in plan.metadata.get('billing_lines',[])}
        for f in selected:
            value=f['value'][lang];numeric=f.get('numeric')
            if f['id']==plan.metadata.get('calendar_service_fact_id'):value=plan.metadata['calendar_service_answer'][lang]
            if f['facet']=='specifications' and plan.metadata.get('specification_keys'):
                from .projection import value as field_value,bilingual
                keys=plan.metadata['specification_keys']
                entries=[x for x in field_value(self.index.records[f['record_id']],'specifications') or [] if isinstance(x,dict) and str(x.get('key','')).upper() in keys]
                value='; '.join(str(x['key'])+': '+bilingual(x['value'])[lang] for x in entries)
            if category=='C06' and f['facet']=='amount' and numeric is not None:
                calc=plan.metadata.get('unit_calculations',{}).get(f['id'])
                ranged=f['id'] in plan.metadata.get('source_person_ranges',{})
                numeric=f['numeric'] if ranged else calc['amount_thb'] if calc else float(Decimal(str(numeric))*sessions)
                per_person=f.get('confirmed_per_person') or f.get('billing_unit')=='per_person' or f.get('calculation')=='integer_sessions_per_person'
                if m and not ranged:
                    unit=('ต่อคน','per person') if per_person else ('ต่อกลุ่ม','per group') if f.get('billing_unit')=='per_group' else ('ตามหน่วยที่ระบุ','for the stated billing unit')
                    value=(f'{numeric:g} บาท{unit[0]} สำหรับ {sessions} รอบ' if lang=='th' else f'{numeric:g} THB {unit[1]} for {sessions} sessions')
                count=billing.get(f['id'],{}).get('persons',persons)
                if f.get('billing_unit')=='per_group':count=1
                total_requested=bool(re.search(r'(?:total|รวม).{0,35}(?:price|cost|fee|บาท|เงิน)|(?:price|cost|fee|ราคา|บาท).{0,35}(?:total|รวม)',question,re.I))
                if f['id'] not in plan.metadata.get('arithmetic_unconfirmed',[]) and (not total_requested or people or billing):
                    computations.append({'fact_id':f['id'],'unit_rate_thb':f['numeric'],'billing_unit':'per_person' if per_person else f.get('billing_unit'),'sessions':sessions,'billing_quantity':count,
                      'total_thb':float(Decimal(str(numeric))*count),'unit_calculation':calc,'assumption':'each line retains its own audience, service and declared arithmetic','evidence_refs':f['evidence_refs']})
                if calc and calc['requested_minutes'] is not None:value=(f'{numeric:g} บาท สำหรับ {calc["requested_minutes"]:g} นาที' if lang=='th' else f'{numeric:g} THB for {calc["requested_minutes"]:g} minutes')
            if f['id'] in plan.metadata.get('game_relation_projections',{}):value=plan.metadata['game_relation_projections'][f['id']]['value'][lang]
            state='unavailable' if f.get('provider_state') in {'unavailable','stale'} else 'answer'
            refs=f['evidence_refs']+f.get('confirmation_evidence_refs',[])
            projection=plan.metadata.get('game_relation_projections',{}).get(f['id'])
            if projection:refs=refs+[ref for ref in projection['evidence_refs'] if ref not in refs]
            controller=plan.metadata.get('controller_catalog_scope',{}).get('proofs',{}).get(f['id'])
            if controller:refs=refs+[ref for ref in controller['evidence_refs'] if ref not in refs]
            claims.append({'fact_id':f['id'],'record_id':f['record_id'],'facet':f['facet'],'value':value,'numeric':numeric,
              'evidence_refs':refs,'fixture':f.get('fixture',False),'status':state})
            shown=value
            if category=='C04' and f['facet']=='players_max':
                from .projection import bilingual
                proof=plan.metadata.get('player_filter_proofs',{}).get(f['id'],{})
                low,high=proof.get('players_min'),proof.get('players_max');mode=bilingual(proof.get('mode_name') or '')[lang]
                if low is not None:shown+=f' ({low}–{high} '+('คนตามโหมดที่บันทึก' if lang=='th' else 'players in the recorded mode')+')'
                else:shown+=(' (ยังไม่ยืนยันจำนวนผู้เล่นขั้นต่ำ)' if lang=='th' else ' (minimum player count unconfirmed)')
                if mode:shown+=' — '+mode
                if proof.get('platform'):shown+=' / '+proof['platform']
            # Source claims retain exact values for auditing; remove technical
            # None/internal field keys only from customer-facing presentation.
            if f['facet']=='specifications':shown=re.sub(r'(?:unit: None; ?|key: |value: )','',shown)
            if f['facet']=='official_description':
                captured=f.get('description_captured_at')
                scope=f.get('description_scope_note',{}).get(lang)
                if captured:shown+=(' (ข้อมูลที่บันทึกเมื่อ ' if lang=='th' else ' (Captured ')+captured[:10]+')'
                if scope:shown+='\n'+scope
            subject=f['subject'][lang]
            if f.get('legacy_search') and re.search(r'\.\*|\(\?:|\\[wsdb]|\|',subject):subject=''
            prefix=(subject+' — ') if subject else ''
            label=f['label'][lang]
            # Citations are claim indices, independent of presentation headings.
            citation=f' [S{len(claims)}]'
            if category in {'C02','C03','C04','C05','C06','C07','C11','C13'} and not plan.metadata.get('customer_calendar_answer'):
                if subject and subject not in shown_subjects:
                    blocks.append('**'+subject+'**');shown_subjects.add(subject)
                if f['facet']=='game_catalog' and ';' in shown:
                    blocks.extend('- '+name.strip() for name in shown.split(';') if name.strip())
                    blocks[-1]+=citation
                elif category=='C13':blocks.append(shown+citation)
                elif category=='C05':blocks.append('- **'+label+'**: '+shown+citation)
                elif '\n' in shown:
                    blocks.append('**'+label+'**')
                    blocks.extend('- '+line for line in shown.splitlines() if line.strip())
                    blocks[-1]+=citation
                else:blocks.append(('**'+label+'**: ' if norm(label)!=norm(shown) else '')+shown+citation)
                continue
            if f['facet']=='owner_policy':
                # Teacher-style fact first. Source conditions remain verbatim;
                # technical FAQ/intent identifiers are not customer headings.
                technical=not subject or self.index.records.get(f['record_id'],{}).get('kind')=='faq' or f.get('service_policy_claim') or re.fullmatch(r'[a-z][a-z0-9_.-]+',subject,re.I)
                blocks.append((subject+': ' if not technical else '')+shown+citation)
            elif norm(label)==norm(shown) or category=='C13' and norm(re.sub(r'^\s*\d+[.)]\s*','',label))==norm(re.sub(r'^\s*\d+[.)]\s*','',shown)):
                blocks.append(prefix+shown+citation)
            else:blocks.append(f'{prefix}{label}: {shown}'+citation)
        if category=='C05' and selected:
            from .projection import value as source_value
            for rid in dict.fromkeys(f['record_id'] for f in selected):
                record=self.index.records[rid];preset=source_value(record,'preset');version=source_value(record,'game_version')
                scope=[('พรีเซ็ต ' if lang=='th' else 'Preset ')+str(preset)] if preset else []
                if version:scope.append(('เวอร์ชันเกมที่บันทึกไว้ ' if lang=='th' else 'recorded game version ')+str(version))
                if scope:blocks.append('; '.join(scope))
        messages={
          'missing_source':('ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ','No confirmed source is available for the requested detail.'),
          'missing_input':('กรุณาระบุรายการและช่วงเวลาที่ต้องการตรวจสอบเพิ่มเติมครับ','Please specify the item and requested time.'),
          'not_current':('ยังไม่มีข้อมูลที่ยืนยันว่าใช้ได้กับวันที่หรือปีที่ถามครับ','No confirmed information applies to the requested date or year.'),
          'unavailable':('ระบบตรวจสอบส่วนนี้ไม่พร้อม จึงยังยืนยันคำตอบไม่ได้ครับ','The checking service is unavailable; this detail cannot be confirmed.'),
        }
        details={
          'player_mode_source_not_recorded':('ยังไม่มีข้อมูลจำนวนผู้เล่นพร้อมกันแยกตามเกมและโหมดที่ยืนยันได้ จึงยังระบุรายชื่อเกมตามจำนวนคนนี้ไม่ได้ครับ','Confirmed player counts by game and mode are not recorded, so games matching this player count cannot yet be listed.'),
          'requested_player_mode_not_recorded':('ยังไม่พบโหมดเกมที่ยืนยันว่ารองรับจำนวนผู้เล่นและเงื่อนไขที่ถามครับ','No recorded game mode confirms the requested player count and conditions.'),
          'entity_not_bound':('ยังระบุเกม เครื่อง หรือหัวข้อที่ต้องการอ่านไม่ชัดเจนครับ กรุณาระบุเป้าหมายเพิ่มเติม','The requested game, machine or topic is not identified. Please specify the target.'),
          'requested_operation_not_satisfied':('พบข้อมูลที่เกี่ยวข้อง แต่ยังไม่พบคำตอบตรงส่วนที่ถามครับ','Related records exist, but the requested detail is not established.'),
          'multiple_session_quantities_require_roles':('พบจำนวนรอบหลายค่าในคำถามเดียวกัน ต้องการใช้จำนวนใด หรือให้แยกเป็นตัวเลือกครับ?','There are several session counts. Which count applies, or should they be separate options?'),
        }
        if not blocks:blocks=[details.get(plan.reason,messages.get(plan.status,messages['missing_source']))[lang=='en']]
        if plan.metadata.get('controller_catalog_scope') is not None:
            from .controller_catalog import notice
            controller=plan.metadata['controller_catalog_scope']
            if selected and controller['request']['group_by']:
                from .projection import title as game_title
                blocks=[]
                for group,game_ids in sorted(controller['groups'].items()):
                    label=controller['group_labels'][group][lang]
                    if controller['request']['operation']=='group_count':blocks.append('**'+label+'**: '+str(len(game_ids))+(' เกมตามความสัมพันธ์ที่บันทึกไว้' if lang=='th' else ' games in the recorded relations'))
                    else:
                        blocks.append('**'+label+'**')
                        for gid in game_ids:
                            refs=[i+1 for i,c in enumerate(claims) if controller['proofs'][c['fact_id']]['game_id']==gid and group in controller['proofs'][c['fact_id']]['groups']]
                            blocks.append('- '+game_title(self.index.records[gid])[lang]+' '+''.join('[S'+str(i)+']' for i in refs))
            if not selected:blocks=[notice(lang)]
            error=plan.metadata['controller_catalog_scope']['request']['error']
            if not selected and error=='multiple_controller_models_require_explicit_relation':blocks=['ต้องการรายชื่อแยกสำหรับจอยแต่ละรุ่น หรือเกมที่รองรับจอยทุกรุ่นที่ระบุครับ?' if lang=='th' else 'Do you want a separate list for each controller, or games that support every stated model?']
            if not selected and error in {'multiple_controller_dates_require_separate_roles','invalid_controller_reference_date','controller_year_requires_specific_date'}:blocks=['กรุณาระบุวันที่ต้องการตรวจข้อมูลอุปกรณ์ควบคุม หากมีหลายวัน กรุณาแยกวันที่ของแต่ละกรณีครับ' if lang=='th' else 'Please give the date for the controller compatibility check. Separate dates belonging to different cases.']
            if not selected and error=='controller_grouping_field_missing':blocks=['ต้องการแยกรายชื่อเกมตามแพลตฟอร์มหรือโซนครับ?' if lang=='th' else 'Do you want the games grouped by platform or by studio zone?']
            if not selected and error=='controller_exclusion_scope_not_resolved':blocks=['ยังไม่มีหลักฐานยืนยันว่าเกมใดไม่รองรับจอยรุ่นที่ระบุ ข้อมูลว่ารองรับรุ่นอื่นไม่ได้ยืนยันว่าใช้รุ่นนี้ไม่ได้ครับ' if lang=='th' else 'The sources do not establish which games do not support this controller. Support for another model does not prove incompatibility.']
            elif selected and plan.metadata['controller_catalog_scope']['limits']:blocks.append(('ยังไม่ยืนยันอุปกรณ์ควบคุมหรือช่วงวันที่ใช้ของบางรายการ จึงแสดงได้เฉพาะเกมที่มีหลักฐานตรงกัน' if lang=='th' else 'Some device compatibility or effective dates remain unconfirmed; only games with matching recorded evidence are shown.'))
        if plan.reason=='person_public_scope_not_confirmed':
            blocks=['พบข้อมูลที่ตรงกับการค้นหา แต่ยังไม่มีสถานะยืนยันให้เผยแพร่ข้อมูลบุคคลส่วนนี้ครับ' if lang=='th' else 'Matching personnel records exist, but their public disclosure scope has not been confirmed.']
        if plan.reason=='control_platform_required':
            blocks=['ต้องการปุ่มของเกมนี้บนแพลตฟอร์มใดครับ?' if lang=='th' else 'Which platform do you want the controls for?']
        if plan.reason=='exact_button_not_recorded':
            blocks=['ยังไม่พบข้อมูลปุ่มหรือชุดปุ่มที่ระบุสำหรับเกมและแพลตฟอร์มนี้ครับ' if lang=='th' else 'The requested button or chord is not recorded for this game and platform.']
        if plan.reason=='requested_hardware_component_not_recorded':
            blocks=['พบรายการอุปกรณ์ แต่ยังไม่มีสเปกชิ้นส่วนที่ถามยืนยันไว้ครับ' if lang=='th' else 'The equipment is recorded, but the requested component specification is not confirmed.']
        if plan.reason=='offsite_rental_scope_not_recorded':
            blocks=['ยังไม่มีข้อมูลยืนยันบริการเช่าหรือยืมอุปกรณ์กลับบ้านครับ ข้อมูลราคาเหมาโซนภายในศูนย์ใช้ยืนยันบริการนี้ไม่ได้' if lang=='th' else 'Offsite equipment rental or borrowing is not confirmed by the recorded sources. Onsite zone-package prices do not establish this service.']
        if plan.reason=='requested_resource_offering_not_confirmed':
            blocks=['ยังไม่มีข้อมูลการติดตั้งที่ยืนยันเกมนี้บนเครื่องที่ระบุครับ ข้อมูลว่ามีในโซนไม่ได้ยืนยันทุกเครื่อง' if lang=='th' else 'The recorded installation relations do not confirm this game on the specified machine. A zone-level offering does not establish every machine.']
        if plan.metadata.get('resource_installation_source_verified'):
            shown=', '.join(plan.metadata['confirmed_resource_labels'][lang])
            blocks.insert(0,('ข้อมูลการติดตั้งที่บันทึกไว้ยืนยันเกมนี้บน: ' if lang=='th' else 'Recorded installation relations confirm this game on: ')+shown)
        if plan.metadata.get('missing_rule_topics'):
            from .rule_semantics import TOPIC_LABELS
            missing=', '.join(TOPIC_LABELS[t][lang=='en'] for t in plan.metadata['missing_rule_topics'])
            blocks.append(('ส่วนที่ยังไม่มีกติกาเฉพาะรายการยืนยัน: ' if lang=='th' else 'Event-specific rules still unconfirmed for: ')+missing)
        if plan.metadata.get('requested_binding_count') is not None:
            wanted=plan.metadata['requested_binding_count'];recorded=plan.metadata['recorded_binding_entries']
            blocks.insert(0,(f'แหล่งข้อมูลมี {recorded} รายการควบคุม แต่ยังไม่ระบุว่าชุด {wanted} ปุ่มที่ถามคือรายการใด ด้านล่างเป็นรายการที่ยืนยันได้ โปรดระบุกลุ่มปุ่มที่ต้องการ' if lang=='th' else f'The source records {recorded} control entries but does not identify the requested subset of {wanted} buttons. Known entries are listed below; please specify the button group.'))
        if plan.metadata.get('unanswered_buttons'):
            blocks.append(('ยังไม่พบข้อมูลปุ่ม: ' if lang=='th' else 'Unrecorded buttons: ')+', '.join(plan.metadata['unanswered_buttons']))
        if plan.metadata.get('unanswered_targets'):
            blocks.append(('ส่วนที่ยังไม่มีความสัมพันธ์โซนยืนยัน: ' if lang=='th' else 'Zone relations still unconfirmed for: ')+', '.join(t.get(lang) or t.get('en') or t.get('th') for t in plan.metadata['unanswered_targets']))
        if plan.metadata.get('operator') in {'count','group_count'} and 'catalog_member_ids' in plan.metadata:
            count=len(plan.metadata['catalog_member_ids'])
            intro=(f'นับได้ {count} เกมไม่ซ้ำ จากรายการความสัมพันธ์บริการที่บันทึกไว้' if lang=='th' else f'{count} distinct games in the recorded offered-service relations')
            if plan.metadata['operator']=='group_count':
                groups=plan.metadata['catalog_group_counts']
                details=[str(group)+': '+str(count) for group,count in groups.items()]
                intro+='\n'+'\n'.join(details)
            blocks.insert(0,intro)
        if not selected and plan.status=='missing_input' and category=='C13':
            blocks=['กรุณาระบุรายการแข่งขันหรือฉบับกติกาที่ต้องการ เพื่อให้จับคู่กติกาที่ถามได้ตรงครับ' if lang=='th' else 'Please specify the tournament or rulebook edition so I can match the rule you are asking about.']
        missing=plan.metadata.get('missing_slots',[])
        if not selected and missing:
            prompts={'audience':('ผู้เล่นอยู่ในกลุ่มผู้ใช้ใดครับ?','Which audience group applies to the players?'),
              'persons_per_audience':('แต่ละกลุ่มมีผู้เล่นกี่คน และเลือกบริการใดครับ?','How many players are in each audience group, and which service is requested?'),
              'service':('ต้องการทราบราคาของบริการใดครับ?','Which service do you want a price for?'),
              'rental_package':('ต้องการเหมาโซนใด สำหรับหน่วยงานภายในหรือภายนอก และครึ่งวันหรือเต็มวันครับ?','Which zone, organization audience and half/full-day package do you want?')}
            prompts['positive_quantity']=('กรุณาระบุจำนวนคนหรือรอบเป็นจำนวนเต็มมากกว่า 0 ครับ','Please give a positive whole number of people or sessions.')
            prompts['organization_group']=('ต้องการราคาเหมาในนามหน่วยงานภายในหรือภายนอกมหาวิทยาลัยครับ? กลุ่มบุคคลผู้เล่นกับกลุ่มหน่วยงานของแพ็กเกจใช้แทนกันไม่ได้','Is the package for an internal university unit or an external organization? Individual visitor status does not determine the package organization group.')
            prompts['event']=('ต้องการกติกาของรายการหรือฉบับใดครับ?','Which tournament or rulebook edition do you mean?')
            prompts['billing_period']=('บริการนี้มีหลายอัตราหรือหลายระยะเวลาต่อรอบ กรุณาระบุบริการและนาทีต่อรอบที่ต้องการครับ','There are multiple services or session lengths. Which service and minutes per session do you want?')
            blocks=[prompts.get(missing[0],messages['missing_input'])[lang=='en']]
            choices=plan.metadata.get('choices',[])
            if choices:blocks.append(('กลุ่มตามตารางราคา: ' if lang=='th' else 'Groups in the rate table: ')+', '.join(x.get(lang) or x.get('en') or x.get('th') for x in choices))
        if not selected and plan.metadata.get('execution_notice'):
            blocks=[plan.metadata['execution_notice'][lang]]
        if not selected and plan.metadata.get('context_clarification'):
            blocks=[plan.metadata['context_clarification'][lang]]
        if plan.metadata.get('comparison_options'):
            blocks.insert(0,'เปรียบเทียบเฉพาะระยะเวลาและอัตราที่บันทึกไว้ แต่ละบรรทัดเป็นทางเลือก ไม่ใช่ยอดรวมทุกทางเลือก' if lang=='th' else 'Comparison of recorded durations and rates only. Each line is an alternative, not a combined total.')
            if plan.metadata.get('unanswered_comparison_minutes'):
                blocks.append(('ยังไม่มีอัตราที่ตรงสำหรับนาที: ' if lang=='th' else 'No exact recorded rate for minutes: ')+', '.join(map(str,plan.metadata['unanswered_comparison_minutes'])))
        if plan.metadata.get('media_scope_unconfirmed'):
            blocks.insert(0,'ยังไม่ยืนยันสิทธิ์ถ่ายสถานที่หรือบุคคลจากนโยบายการบันทึกในเกม กรุณาตรวจขอบเขตข้อมูลด้านล่างครับ' if lang=='th' else 'An in-game capture policy does not establish permission to film the premises or people. The recorded source scope is shown below.')
        if plan.metadata.get('policy_source_variants'):
            blocks.insert(0,'พบข้อความขั้นตอนการจองหลายฉบับ ด้านล่างคงข้อความแต่ละฉบับไว้ ยังไม่ได้รวมเป็นนโยบายฉบับเดียว' if lang=='th' else 'Multiple recorded versions of the booking steps follow. They are retained separately rather than merged into a single policy.')
        if plan.metadata.get('policy_source_scope_variants'):
            blocks.insert(0,'มีข้อความนโยบายหลายฉบับที่ยังยืนยันไม่ได้ว่าใช้ขอบเขตหรือเงื่อนไขเดียวกัน จึงคงข้อมูลแต่ละฉบับไว้ กรุณาตรวจสอบกับศูนย์ก่อนใช้' if lang=='th' else 'Several recorded policy versions have unresolved scope or conditions. Each source is retained; confirm the applicable version with the studio.')
        if plan.metadata.get('recorded_source_collection'):
            blocks.insert(0,'รายการข้อความที่มีในแหล่งข้อมูล ไม่ยืนยันสิทธิ์ในทุกสถานการณ์ ต้องอ่านเงื่อนไขและข้อจำกัดของแต่ละรายการ' if lang=='th' else 'Recorded source entries only. They do not establish permission in every situation; each entry retains its conditions and limits.')
        if plan.metadata.get('collection_source_limits'):
            blocks.insert(0,'บางเงื่อนไขหรือความครบของรายการยังยืนยันไม่ได้ แสดงเฉพาะส่วนที่ตรวจหลักฐานแล้ว' if lang=='th' else 'Some conditions or collection coverage remain unconfirmed; only the source-checked subset is shown.')
        if plan.metadata.get('calendar_collection_basis'):
            play=plan.metadata.get('calendar_semantics')=='play_service_only_not_physical_building_hours_or_live_occupancy'
            blocks.insert(0,('ตารางบริการเล่นประจำที่บันทึกไว้ ไม่ใช่สถานะเครื่องว่างหรือเวลาเข้าอาคาร' if play else 'รายการช่วงเวลาประจำตามแหล่งข้อมูล ไม่ใช่สถานะเครื่องว่างแบบสด') if lang=='th' else ('Recorded regular play-service timetable, not live machine availability or building access hours.' if play else 'Recorded weekday periods, not live machine availability.'))
            limits=plan.metadata.get('calendar_source_limits',[])
            labels={'effective_period_unknown':('ช่วงวันที่มีผล','effective date interval'),'resource_applicability_unconfirmed':('ขอบเขตเครื่องหรือโซนที่ใช้','applicable resource or zone'),'timezone_unconfirmed':('เขตเวลาของตาราง','source timezone')}
            unknown=[labels[k][lang=='en'] for k in labels if k in limits]
            if unknown:blocks.append(('ยังยืนยันไม่ได้: ' if lang=='th' else 'Unconfirmed: ')+', '.join(unknown))
            daynames=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'] if lang=='en' else ['จันทร์','อังคาร','พุธ','พฤหัสบดี','ศุกร์','เสาร์','อาทิตย์']
            for key,prefix in [('weekly_missing_weekdays',('ยังไม่มีตารางที่ใช้ได้สำหรับ: ','No applicable record for: ')),('weekly_conflicting_weekdays',('ยังแยกฉบับหรือขอบเขตตารางไม่ได้สำหรับ: ','Unresolved source versions or scope for: '))]:
                if plan.metadata.get(key):blocks.append(prefix[lang=='en']+', '.join(daynames[d] for d in plan.metadata[key]))
            intervals=list(dict.fromkeys(str(p['validity'].get('effective_from') or '')+' – '+str(p['validity'].get('effective_until') or '') for p in plan.metadata.get('calendar_source_periods',[]) if p['validity'].get('state')=='known'))
            if intervals:blocks.append(('ช่วงที่ตารางมีผลตามต้นทาง: ' if lang=='th' else 'Recorded effective intervals: ')+ '; '.join(intervals))
        if plan.metadata.get('rule_dependency_proof',{}).get('limits'):blocks.append('ต้นทางยังไม่ยืนยันข้อกติกาที่อ้างถึงหรือความครบถ้วนของเนื้อหาบางส่วน ข้างต้นเป็นข้อความที่มีหลักฐานบันทึกไว้' if lang=='th' else 'The source has not confirmed all linked rule clauses or that the text is complete. The recorded text is shown above.')
        if plan.metadata.get('policy_source_gaps'):blocks.append('นโยบายบางฉบับยังไม่ยืนยันเงื่อนไขหรือข้อยกเว้น จึงแสดงเฉพาะข้อความที่มีข้อมูลประกอบครบ' if lang=='th' else 'Some recorded policies have unconfirmed conditions or exceptions. Only clauses with confirmed scope are shown.')
        if plan.metadata.get('procedure_source_limits'):
            captions={'preconditions':('เงื่อนไขก่อนเริ่ม','preconditions'),'required_documents':('เอกสารที่ต้องเตรียม','required documents'),'deadline_minutes':('กำหนดเวลา','deadline'),'outcome':('ผลลัพธ์หลังดำเนินการ','outcome')}
            fields=sorted({field for limits in plan.metadata['procedure_source_limits'].values() for field in limits})
            blocks.append(('ขั้นตอนที่ยังไม่ยืนยันข้อมูลประกอบ: ' if lang=='th' else 'Unconfirmed procedure information: ')+', '.join(captions[field][lang=='en'] for field in fields))
        if any(p['state']=='validity_interval_unconfirmed' for p in plan.metadata.get('policy_applicability',{}).values()):blocks.append('ช่วงที่นโยบายมีผลยังไม่ยืนยัน ข้างต้นเป็นข้อความที่บันทึกไว้ ไม่ยืนยันสิทธิ์ปัจจุบัน' if lang=='th' else 'The policy validity interval is unconfirmed. The recorded clause does not establish current permission.')
        if plan.metadata.get('news_publication_scope'):
            proofs=plan.metadata['news_publication_scope'].values()
            if any(p['state']=='historical_publication' for p in proofs):blocks.append('ประกาศเก่าที่บันทึกไว้ ไม่ยืนยันสถานะปัจจุบัน' if lang=='th' else 'Historical recorded announcement; this does not confirm current status.')
            if any(p['state']=='publication_period_unconfirmed' for p in plan.metadata['news_publication_scope'].values()):blocks.append('ยังไม่ยืนยันช่วงที่ประกาศนี้มีผล' if lang=='th' else 'The publication validity period is unconfirmed.')
        if plan.metadata.get('registration_status_freshness'):
            stamps=list(dict.fromkeys(r['as_of'] for r in plan.metadata['registration_status_freshness']))
            blocks.insert(0,('สถานะรับสมัครตามหลักฐานที่ตรวจไว้เมื่อ ' if lang=='th' else 'Registration status from the source observation at ')+', '.join(stamps))
        if plan.metadata.get('calendar_source_limits') and not plan.metadata.get('calendar_collection_basis'):
            if plan.metadata.get('calendar_semantics')=='play_service_only_not_physical_building_hours_or_live_occupancy':
                blocks.insert(0,'ตารางบริการเล่นประจำตามข้อมูลที่บันทึกไว้ ไม่ใช่สถานะเครื่องว่างแบบสดหรือเวลาเข้าอาคาร วันปิดพิเศษมีผลก่อนตารางนี้' if lang=='th' else 'Recorded regular play-service timetable, not live machine availability or building access hours. Special closures override this timetable.')
            else:
                limits=plan.metadata['calendar_source_limits']
                if 'opening_hours_conflicted' in limits:
                    blocks.insert(0,'เวลาเปิดพื้นที่ในแหล่งข้อมูลขัดแย้งกัน จึงยังยืนยันเวลาเข้าอาคารไม่ได้' if lang=='th' else 'Building access hours conflict across sources and remain unconfirmed.')
                elif 'zone_scope_unknown' in limits or 'effective_period_unknown' in limits:
                    blocks.insert(0,'ตามตารางที่บันทึกไว้ ข้อมูลนี้ไม่ยืนยันเครื่องว่างแบบสด' if lang=='th' else 'According to the recorded timetable; this does not establish live machine availability.')
        if plan.metadata.get('arithmetic_unconfirmed'):
            blocks.insert(0,'ทราบระยะเวลาที่ต้องการแล้ว แต่ยังไม่มีกฎคำนวณที่ยืนยันสำหรับระยะเวลานี้ อัตราด้านล่างเป็นราคาต่อหน่วยที่บันทึกไว้ ไม่ใช่ยอดรวมของคำขอนี้' if lang=='th' else 'The requested duration is known, but its billing arithmetic is not declared. The following are recorded unit rates, not a confirmed total for this request.')
        if plan.metadata.get('package_quantity_unconfirmed'):
            blocks.insert(0,'ราคาด้านล่างเป็นราคาต่อแพ็กเกจที่บันทึกไว้ ยังไม่มีกฎยืนยันยอดรวมสำหรับจำนวนวันหรือแพ็กเกจที่ขอครับ' if lang=='th' else 'The following are recorded per-package prices. No declared billing rule confirms a total for the requested number of days or packages.')
        if plan.metadata.get('zone_projection_missing'):
            blocks.insert(0,'ยังยืนยันโซนจากความสัมพันธ์ข้อมูลไม่ได้ แต่ยืนยันบริการที่มีเกมนี้ได้ดังนี้' if lang=='th' else 'The zone relation is not confirmed; the following studio services are confirmed to offer this game.')
        if plan.metadata.get('relation_completeness'):
            blocks.insert(0,'รายการที่ยืนยันได้จากความสัมพันธ์ที่มีอยู่ ยังไม่รับรองว่าครบทุกเกมหรือทุกโซน' if lang=='th' else 'Confirmed subset from recorded relations; completeness across all games and zones is not established.')
        if plan.metadata.get('consumption_not_bring_permission'):
            blocks.insert(0,'ข้อมูลด้านล่างยืนยันเฉพาะการบริโภคในบริเวณที่กำหนด ยังไม่ยืนยันสิทธิ์นำอาหารหรือเครื่องดื่มเข้าศูนย์แยกต่างหาก' if lang=='th' else 'The following source confirms consumption in designated areas. It does not separately confirm permission to bring food or drinks into the studio.')
        if plan.metadata.get('authority_conflict'):
            blocks.insert(0,'มีข้อความนโยบายหลายฉบับที่ยังไม่ยืนยันขอบเขตหรือฉบับที่ใช้แทนกัน กรุณาตรวจสอบกับศูนย์ก่อนใช้เงื่อนไขที่ต่างกัน' if lang=='th' else 'Policy sources have differing wording or scope without a confirmed superseding version. Please confirm the differing conditions with the studio.')
        if category=='C02' and selected:
            blocks.insert(0,'ตามโปรไฟล์ต้นทางที่บันทึกไว้' if lang=='th' else 'According to the recorded source profile:')
            if plan.metadata.get('person_period_unconfirmed'):blocks.append('ยังยืนยันช่วงดำรงตำแหน่งปัจจุบันไม่ได้ โปรไฟล์นี้เป็นข้อมูลที่บันทึกไว้ครับ' if lang=='th' else 'The current appointment period is unconfirmed; this is a recorded profile.')
            if plan.metadata.get('person_profile_subset'):blocks.append('แสดงเฉพาะรายชื่อที่ยืนยันขอบเขตเผยแพร่และช่วงเวลาที่ใช้ได้ ไม่รับรองว่าครบทุกคนครับ' if lang=='th' else 'Only profiles with applicable public and date scope are shown; this is not a complete personnel list.')
            if plan.metadata.get('person_requested_period_partial'):blocks.append('ข้อมูลตำแหน่งยืนยันเฉพาะช่วงที่แสดงด้านล่าง ไม่ครอบคลุมช่วงเวลาทั้งหมดที่ถามครับ' if lang=='th' else 'The role is confirmed only for the recorded interval below, which does not cover the entire requested period.')
            intervals=list(dict.fromkeys(str(p.get('validity',{}).get('effective_from') or '')+' – '+str(p.get('validity',{}).get('effective_until') or '') for p in plan.metadata.get('person_scope_proofs',{}).values() if p.get('state')=='recorded_effective_interval'))
            if intervals:blocks.append(('ช่วงที่ข้อมูลมีผล: ' if lang=='th' else 'Recorded effective interval: ')+ '; '.join(intervals))
        if category=='C05' and selected:
            if plan.metadata.get('control_layout_partial'):
                blocks.insert(0,'แหล่งข้อมูลระบุวิธีควบคุมเพียงบางส่วน ยังไม่มีผังปุ่มครบชุดที่ยืนยันได้' if lang=='th' else 'The source describes only part of the controls; a complete button layout is not confirmed.')
            if any(f.get('control_source_coverage')=='secondary_needs_manual_verify' for f in selected):
                blocks.append('ปุ่มชุดนี้มาจากแหล่งรอง ยังไม่ได้ตรวจยืนยันกับเวอร์ชันเกมและการตั้งค่าปุ่มของเครื่องที่ศูนย์ใช้อยู่จริง' if lang=='th' else 'These controls come from a secondary source and have not been verified against the studio installed game version and button preset.')
            notes={f['record_id']:f.get('control_verification_note',{}).get(lang,'') for f in selected}
            blocks.extend(('หมายเหตุ: ' if lang=='th' else 'Note: ')+note for note in notes.values() if note)
        if lang=='en' and any(f.get('english_translation_missing') for f in selected):
            blocks.insert(0,'A confirmed English translation is unavailable for some clauses; their Thai source text is retained below.')
        if not plan.metadata.get('comparison_options') and computations and (billing or people and len(computations)==1):
            total=sum(Decimal(str(c['total_thb'])) for c in computations)
            shown_total=format(total.normalize(),'f')
            if plan.metadata.get('rate_date_applicability_unconfirmed'):
                blocks.append(f'หากใช้อัตราที่แสดงนี้ รวม {shown_total} บาท โดยยังไม่ยืนยันการใช้กับวันที่ขอ' if lang=='th' else f'Using these recorded rates would total {shown_total} THB; applicability on the requested date remains unconfirmed.')
            else:blocks.append(f'รวม {shown_total} บาท ตามจำนวนคนและรอบที่ระบุ' if lang=='th' else f'Total: {shown_total} THB for the stated people and sessions.')
        status='unavailable' if claims and all(c['status']=='unavailable' for c in claims) else plan.status
        if plan.metadata.get('price_confirmation_as_of'):
            day=plan.metadata['price_confirmation_as_of'][:10]
            blocks.append(('อัตราที่เจ้าของยืนยันล่าสุด ณ '+day+' (ยังไม่ยืนยันวันเริ่ม–สิ้นสุดใหม่)' if lang=='th' else 'Rates last reaffirmed by the owner on '+day+'; no new effective interval was established.'))
        if any(p['state']=='unconfirmed_interval' for p in plan.metadata.get('rental_source_applicability',{}).values()):
            blocks.append('ข้อมูลแพ็กเกจตามแหล่งที่บันทึกไว้ ช่วงวันที่มีผลยังไม่ยืนยัน จึงยังยืนยันการใช้ข้อมูลนี้เป็นเงื่อนไขปัจจุบันไม่ได้' if lang=='th' else 'These are recorded package details. Their effective interval is unconfirmed, so current applicability is not established.')
        if plan.metadata.get('rate_date_applicability_unconfirmed'):
            day=plan.metadata['rate_date_applicability_unconfirmed']['requested_date']
            blocks.insert(0,('ยังยืนยันไม่ได้ว่าอัตราด้านล่างใช้กับวันที่ '+day+' ตัวเลขที่แสดงเป็นอัตราตามแหล่งข้อมูลที่มีครับ' if lang=='th' else 'The rates below are recorded source values; their applicability on '+day+' has not been confirmed.'))
        if category in {'C03','C04','C13'} and len(shown_subjects)==1 and blocks and blocks[0]=='**'+next(iter(shown_subjects))+'**':
            blocks.append(blocks.pop(0))
        if plan.metadata.get('named_period_answer'):
            blocks=[plan.metadata['named_period_answer'][lang]+' '+ ' '.join('[S'+str(i+1)+']' for i in range(len(claims)))]
            if plan.metadata.get('named_period_limits'):
                labels={'effective_period_unknown':('ช่วงวันที่มีผล','effective interval'),'timezone_unconfirmed':('เขตเวลา','timezone'),'resource_applicability_unconfirmed':('ขอบเขตโซน','applicable zone'),'named_period_identity_unconfirmed':('ชื่อรอบของช่วงเวลาที่บันทึกไว้','recorded interval period identity')}
                shown=[labels[k][lang=='en'] for k in plan.metadata['named_period_limits'] if k in labels]
                blocks.append(('ยังไม่ยืนยัน: ' if lang=='th' else 'Source limitations remain; not fully confirmed: ')+', '.join(shown))
        if plan.metadata.get('customer_calendar_answer'):
            blocks=[plan.metadata['customer_calendar_answer'][lang]+' '+ ' '.join('[S'+str(i+1)+']' for i in range(len(claims)))]
            if plan.metadata.get('calendar_source_limits'):
                limits=plan.metadata['calendar_source_limits']
                note='เป็นตารางบริการเล่นที่บันทึกไว้ ยังไม่ยืนยัน' if lang=='th' else 'Recorded play-service timetable only; unconfirmed: '
                labels={'effective_period_unknown':('ช่วงวันที่มีผล','effective date interval'),'resource_applicability_unconfirmed':('ขอบเขตเครื่องหรือโซนที่ใช้','applicable resource or zone'),'special_closure_applicability_unconfirmed':('ขอบเขตประกาศปิดพิเศษ','special closure applicability')}
                shown=[labels[k][lang=='en'] for k in labels if k in limits]
                blocks.append(note+(' / '.join(shown))+(' ไม่ใช่สถานะเครื่องว่างแบบสดครับ' if lang=='th' else '. This is not live machine availability.'))
        if plan.metadata.get('procedure_steps') and len(selected)==1:
            from .source_operations import procedure_rows
            steps=procedure_rows(selected[0]['value'][lang])
            if steps:blocks=[('ขั้นตอนการจอง' if lang=='th' else 'Booking steps')]+[str(i)+'. '+line for i,line in enumerate(steps,1)]+['[S1]']
        from .customer_render import render as render_customer
        blocks=render_customer(self.index,category,question,lang,selected,claims,computations,plan.metadata,blocks)
        if category=='C06' and plan.metadata.get('person_bounds_withheld'):
            blocks.insert(0,plan.metadata['execution_notice'][lang])
        if category=='C06' and plan.metadata.get('source_person_ranges'):
            ranges=plan.metadata['source_person_ranges']
            labels=[str(p['lower'])+'–'+str(p['upper']) for p in ranges.values()]
            blocks.insert(0,('อัตราตามช่วงจำนวนคนในแหล่งข้อมูล: ' if lang=='th' else 'Source person ranges: ')+', '.join(dict.fromkeys(labels))+(' คน; คำนวณยอดรวมไม่ได้จนกว่าจะยืนยันการจัดคนและหน่วยเรียกเก็บ' if lang=='th' else ' people; a total cannot be calculated until allocation and billing units are confirmed.'))
        wants_total=bool(re.search(r'(?:total|รวม).{0,35}(?:price|cost|fee|บาท|เงิน)|(?:price|cost|fee|ราคา|บาท).{0,35}(?:total|รวม)',question,re.I))
        if category=='C06' and wants_total and not computations:
            notice=('ยังยืนยันยอดรวมไม่ได้จากข้อมูลและเงื่อนไขที่ระบุ อัตราที่แสดงยังไม่ใช่ยอดรวมครับ' if lang=='th' else 'The total is not confirmed from the stated inputs and source scope. Any rates shown are not a confirmed total.')
            blocks.insert(0,notice)
            plan.metadata['missing_total_notice']=True
            if claims and status=='answer':status='partial'
        if category=='C01' and not selected and re.search(r'\be-?mail\b|อีเมล',question,re.I) and re.search(r'\b(?:policy|policies)\b|นโยบาย',question,re.I):
            # A question about email policy is not necessarily a request for
            # the contact address. Ask which aspect the user means without
            # inventing a policy or replacing it with an unrelated fact.
            blocks=['ต้องการทราบนโยบายเรื่องใดเกี่ยวกับอีเมล หรือกำลังขออีเมลติดต่อศูนย์ครับ?' if lang=='th' else 'Which email policy do you mean, or are you asking for the studio contact email?']
        if category=='C13' and selected and any(f.get('event_id') for f in selected):
            # A game match alone does not identify the user's tournament, and
            # a locally unique rulebook is not proof of event applicability.
            # Preserve the source clause and named event while stating that
            # the user must verify which rulebook governs their match.
            blocks.append('โปรดตรวจสอบว่ากติกาของรายการที่แสดงใช้กับแมตช์ของคุณหรือไม่' if lang=='th' else 'Please confirm that the displayed event rules apply to your match.')
        return {'answer':'\n'.join(blocks),'status':status,'claims':claims,'category':category,'reason':plan.reason,
          'fixture':any(f.get('fixture',False) for f in selected),'english_translation_missing':lang=='en' and any(f.get('english_translation_missing') for f in selected),
          'selection_basis':plan.reason,'computations':computations,'plan':{'facets':plan.facets,'locked':plan.locked,'metadata':plan.metadata}}

    def _legacy_answer(self,question,locale='auto',category=None,at=None,allow_llm=True,history=None,budget=None,understanding=None):
        started=time.monotonic();at=reference_time(at);budget=budget or RequestBudget()
        from .understanding import interpret,Understanding
        understanding=understanding if understanding is not None else (interpret(question,budget,allow_llm,index=self.index) if category is None else Understanding(reason='explicit_internal_category'))
        from .context_guard import apply as guard_context
        understanding=guard_context(question,self.index,understanding)
        needs=[t.quote for t in understanding.tasks] if understanding.accepted else split_needs(question,self.index)
        children=[];previous=''
        for need_index,part in enumerate(needs):
            meaning=understanding.tasks[need_index] if understanding.accepted else None
            cat=category or (meaning.category if meaning else route(self.index,part))
            scoped_q=part
            if meaning:
                # All inherited material is quoted from this user's request,
                # never from an answer or an untrusted model paraphrase.
                slots=[meaning.target,*[c['quote'] for c in meaning.constraints]]
                scoped_q+=' '+' '.join(s for s in slots if s and s not in part)
                from .meaning_reader import execution_query
                scoped_q=execution_query(self.index,scoped_q,meaning)
            if meaning is None and previous and cat in {'C04','C05','C06','C07'} and not self.index.bind(cat,part):
                # Inherit only a source-bound name from a prior need, never its
                # answer or an unverified model-generated factual statement.
                names={s for f in self.index.facts for s in f['subject'].values() if contains(previous,s)}
                if names:scoped_q=part+' '+max(names,key=len)
            if cat is None:
                p=blocked('','domain_not_bound');children.append(self._render_one('',part,locale,p,at));continue
            plan=self.plan(cat,scoped_q,at,meaning=meaning)
            if plan.ambiguous and allow_llm and not plan.locked:
                candidates=self.scoped_candidates(cat,scoped_q,plan,at)
                if candidates:
                    plans,event=self.selector.select([{'question':scoped_q,'language':language(part,locale),'facts':candidates}],budget)
                    plan=plans[0];plan.category=cat
            if plan.ambiguous and not allow_llm:
                plan.status='missing_source';plan.reason='typed_interpretation_unresolved';plan.ambiguous=False
                plan.metadata['compatibility_allowed']=bool(self.index.bind(cat,scoped_q))
            plan=self.finish_plan(cat,scoped_q,plan,at);result=self._render_one(cat,scoped_q,locale,plan,at)
            result['question']=part;result['execution_query']=scoped_q;children.append(result);previous=scoped_q
        def claim_key(c):return (c['fact_id'],c.get('numeric'),c['value'])
        claims=list({claim_key(c):c for r in children for c in r['claims']}.values())
        states=[r['status'] for r in children]
        state=states[0] if len(set(states))==1 else 'partial' if claims else ('unavailable' if 'unavailable' in states else 'missing_source')
        # Re-number citations across needs so displayed labels and evidence rows
        # refer to the same source claim even in a multi-domain response.
        labels={claim_key(c):i+1 for i,c in enumerate(claims)};blocks=[]
        for result in children:
            local={i+1:labels[claim_key(c)] for i,c in enumerate(result['claims'])}
            blocks.append(re.sub(r'\[S(\d+)\]',lambda m:'[S'+str(local[int(m[1])])+']',result['answer']))
        return {'answer':'\n\n'.join(blocks),'status':state,'claims':claims,'needs':children,'model_events':budget.events,'understanding':understanding.as_dict(),
          'elapsed_sec':time.monotonic()-started,'fixture':any(r['fixture'] for r in children),'english_translation_missing':any(r['english_translation_missing'] for r in children),
          'selection_basis':'r114_domain_flow','effective_locale':language(question,locale),'release_id':self.data.get('release_id'),'epoch':self.data.get('epoch')}

    def answer(self,question,locale='auto',category=None,at=None,allow_llm=True,history=None,budget=None,understanding=None):
        from .task_execution import execute
        return execute(self,question,locale,category,at,allow_llm,history,budget,understanding)
