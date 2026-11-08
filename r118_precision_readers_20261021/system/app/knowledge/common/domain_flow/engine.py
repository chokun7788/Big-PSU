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
        result=read(self.index,category,question,reference_time(at))
        if meaning is not None:
            from .meaning_reader import apply
            result=apply(self.index,question,meaning,result,reference_time(at))
        return result

    def scoped_candidates(self,category,question,plan,at=None):
        if plan.reason in {'entity_not_bound','domain_not_bound'}:return []
        pool=[self.index.byid[k] for k in plan.candidates if k in self.index.byid]
        if category=='C13':
            asked=event_years(self.index,question)
            if asked:pool=[f for f in pool if asked<=event_years(self.index,' '.join(f['subject'].values()))]
        if plan.facets:
            strict=[f for f in pool if f['facet'] in plan.facets]
            pool=strict
        return [f for _,f in self.index.rank(category,question,pool=pool,limit=8)]

    def finish_plan(self,category,question,plan,at):
        # The model only sees a scoped pool, and selection must remain in that
        # pool. A cross-category/source ID can never enter the renderer.
        selected=[self.index.byid[k] for k in plan.ids if k in self.index.byid and self.index.byid[k]['category']==category]
        if len(selected)!=len(plan.ids):return blocked(category,'invalid_or_cross_category_fact','unavailable')
        from .precision import validate
        plan=validate(self.index,category,question,plan)
        if not plan.ids:return plan
        if category=='C02':
            from .projection import value
            unsafe=[f for f in selected if self.index.records.get(f['record_id'],{}).get('kind')=='person' and
                    (self.index.records[f['record_id']]['fields'].get('public_scope',{}).get('status')!='known' or
                     re.search(r'private|internal|not public|ภายใน|ห้ามเผยแพร่',str(value(self.index.records[f['record_id']],'public_scope') or ''),re.I))]
            if unsafe:
                result=blocked(category,'person_public_scope_not_confirmed')
                result.metadata['source_match_exists']=True
                result.metadata['lookup_operator']=plan.metadata.get('operator','person_to_role')
                return result
        asked=event_years(self.index,question) if category=='C13' else requested_years(question)
        if category=='C13' and asked and any(not asked<=event_years(self.index,' '.join(f['subject'].values())) for f in selected):
            return blocked(category,'selected_rule_event_year_mismatch')
        if category in {'C06','C07'} and selected:
            price=[f for f in selected if f['facet'] in {'amount','amount_thb'}]
            requested_at=in_year(at,next(iter(asked))) if len(asked)==1 else at
            expired=[f for f in price if validity_allows(f,requested_at) is False and not (f.get('confirmation_ref') and (not asked or asked=={at.year}))]
            if expired:return blocked(category,'rate_not_effective_for_request','not_current')
            acknowledgements=[f.get('confirmation_as_of') for f in price if f.get('confirmation_as_of')]
            if acknowledgements:plan.metadata['price_confirmation_as_of']=max(acknowledgements)
            if category=='C06':
                from .financial import quantity_text,unit_calculation
                quantity_q=quantity_text(self.index,question,selected)
                count_match=re.search(r'(\d+)\s*(?:คน|people|persons?|players?)',quantity_q)
                persons=int(count_match[1]) if count_match else 1
                for f in price:
                    calc=unit_calculation(self.index,f,question)
                    if calc.get('error'):
                        if calc['error']=='duration_arithmetic_not_declared':
                            plan.status='partial';plan.reason=calc['error']
                            plan.metadata.setdefault('arithmetic_unconfirmed',[]).append(f['id']);continue
                        return blocked(category,calc['error'],calc['status'])
                    plan.metadata.setdefault('unit_calculations',{})[f['id']]=calc
                    per_person=f.get('confirmed_per_person') or f.get('billing_unit')=='per_person' or f.get('calculation')=='integer_sessions_per_person'
                    if persons>1 and not per_person and f.get('billing_unit')!='per_group':return blocked(category,'per_person_billing_basis_not_confirmed')
                    if f.get('billing_unit')=='per_group' and (f.get('persons_min') and persons<f['persons_min'] or f.get('persons_max') and persons>f['persons_max']):return blocked(category,'group_size_outside_confirmed_rate_scope','missing_input')
        return plan

    def _render_one(self,category,question,locale,plan,at):
        lang=language(question,locale);selected=[self.index.byid[k] for k in plan.ids]
        claims=[];blocks=[];computations=[]
        from .financial import quantity_text
        quantity_q=quantity_text(self.index,question,selected)
        m=re.search(r'(\d+)\s*รอบ|\b(\d+)\s+sessions?\b',quantity_q);sessions=int(next(x for x in m.groups() if x)) if m else 1
        people=re.search(r'(\d+)\s*คน|\b(\d+)\s+(?:people|persons?|players?)\b',quantity_q);persons=int(next(x for x in people.groups() if x)) if people else 1
        billing={x['fact_id']:x for x in plan.metadata.get('billing_lines',[])}
        for f in selected:
            value=f['value'][lang];numeric=f.get('numeric')
            if f['facet']=='specifications' and plan.metadata.get('specification_keys'):
                from .projection import value as field_value,bilingual
                keys=plan.metadata['specification_keys']
                entries=[x for x in field_value(self.index.records[f['record_id']],'specifications') or [] if isinstance(x,dict) and str(x.get('key','')).upper() in keys]
                value='; '.join(str(x['key'])+': '+bilingual(x['value'])[lang] for x in entries)
            if category=='C06' and f['facet']=='amount' and numeric is not None:
                calc=plan.metadata.get('unit_calculations',{}).get(f['id'])
                numeric=calc['amount_thb'] if calc else float(Decimal(str(numeric))*sessions)
                per_person=f.get('confirmed_per_person') or f.get('billing_unit')=='per_person' or f.get('calculation')=='integer_sessions_per_person'
                if m:
                    unit=('ต่อคน','per person') if per_person else ('ต่อกลุ่ม','per group') if f.get('billing_unit')=='per_group' else ('ตามหน่วยที่ระบุ','for the stated billing unit')
                    value=(f'{numeric:g} บาท{unit[0]} สำหรับ {sessions} รอบ' if lang=='th' else f'{numeric:g} THB {unit[1]} for {sessions} sessions')
                count=billing.get(f['id'],{}).get('persons',persons)
                if f.get('billing_unit')=='per_group':count=1
                if f['id'] not in plan.metadata.get('arithmetic_unconfirmed',[]):
                    computations.append({'fact_id':f['id'],'unit_rate_thb':f['numeric'],'billing_unit':'per_person' if per_person else f.get('billing_unit'),'sessions':sessions,'billing_quantity':count,
                      'total_thb':float(Decimal(str(numeric))*count),'unit_calculation':calc,'assumption':'each line retains its own audience, service and declared arithmetic','evidence_refs':f['evidence_refs']})
                if calc and calc['requested_minutes'] is not None:value=(f'{numeric:g} บาท สำหรับ {calc["requested_minutes"]:g} นาที ตามกฎ {calc["rule"]}' if lang=='th' else f'{numeric:g} THB for {calc["requested_minutes"]:g} minutes under the declared {calc["rule"]} rule')
            state='unavailable' if f.get('provider_state') in {'unavailable','stale'} else 'answer'
            refs=f['evidence_refs']+f.get('confirmation_evidence_refs',[])
            claims.append({'fact_id':f['id'],'record_id':f['record_id'],'facet':f['facet'],'value':value,'numeric':numeric,
              'evidence_refs':refs,'fixture':f.get('fixture',False),'status':state})
            shown=value
            # Source claims retain exact values for auditing; remove technical
            # None/internal field keys only from customer-facing presentation.
            if f['facet']=='specifications':shown=re.sub(r'(?:unit: None; ?|key: |value: )','',shown)
            blocks.append(f"{f['subject'][lang]} — {f['label'][lang]}: {shown} [S{len(blocks)+1}]")
        messages={
          'missing_source':('ยังไม่มีข้อมูลยืนยันสำหรับส่วนที่ถามครับ','No confirmed source is available for the requested detail.'),
          'missing_input':('กรุณาระบุรายการและช่วงเวลาที่ต้องการตรวจสอบเพิ่มเติมครับ','Please specify the item and requested time.'),
          'not_current':('ยังไม่มีข้อมูลที่ยืนยันว่าใช้ได้กับวันที่หรือปีที่ถามครับ','No confirmed information applies to the requested date or year.'),
          'unavailable':('ระบบตรวจสอบส่วนนี้ไม่พร้อม จึงยังยืนยันคำตอบไม่ได้ครับ','The checking service is unavailable; this detail cannot be confirmed.'),
        }
        if not blocks:blocks=[messages.get(plan.status,messages['missing_source'])[lang=='en']]
        if plan.reason=='person_public_scope_not_confirmed':
            blocks=['พบข้อมูลที่ตรงกับการค้นหา แต่ยังไม่มีสถานะยืนยันให้เผยแพร่ข้อมูลบุคคลส่วนนี้ครับ' if lang=='th' else 'Matching personnel records exist, but their public disclosure scope has not been confirmed.']
        if plan.reason=='control_platform_required':
            blocks=['ต้องการปุ่มของเกมนี้บนแพลตฟอร์มใดครับ?' if lang=='th' else 'Which platform do you want the controls for?']
        if plan.reason=='exact_button_not_recorded':
            blocks=['ยังไม่พบข้อมูลปุ่มหรือชุดปุ่มที่ระบุสำหรับเกมและแพลตฟอร์มนี้ครับ' if lang=='th' else 'The requested button or chord is not recorded for this game and platform.']
        if plan.reason=='requested_hardware_component_not_recorded':
            blocks=['พบรายการอุปกรณ์ แต่ยังไม่มีสเปกชิ้นส่วนที่ถามยืนยันไว้ครับ' if lang=='th' else 'The equipment is recorded, but the requested component specification is not confirmed.']
        if plan.metadata.get('unanswered_buttons'):
            blocks.append(('ยังไม่พบข้อมูลปุ่ม: ' if lang=='th' else 'Unrecorded buttons: ')+', '.join(plan.metadata['unanswered_buttons']))
        if plan.metadata.get('unanswered_targets'):
            blocks.append(('ส่วนที่ยังไม่มีความสัมพันธ์โซนยืนยัน: ' if lang=='th' else 'Zone relations still unconfirmed for: ')+', '.join(t.get(lang) or t.get('en') or t.get('th') for t in plan.metadata['unanswered_targets']))
        if plan.metadata.get('operator') in {'count','group_count'} and 'catalog_member_ids' in plan.metadata:
            count=len(plan.metadata['catalog_member_ids'])
            intro=(f'นับได้ {count} เกมไม่ซ้ำ จากรายการความสัมพันธ์บริการที่บันทึกไว้' if lang=='th' else f'{count} distinct games in the recorded offered-service relations')
            if plan.metadata['operator']=='group_count':
                groups=plan.metadata['catalog_group_counts']
                details=[f"{self.index.byid[k]['subject'][lang]}: {groups[self.index.byid[k]['record_id']]}" for k in plan.ids]
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
            prompts['event']=('ต้องการกติกาของรายการหรือฉบับใดครับ?','Which tournament or rulebook edition do you mean?')
            prompts['billing_period']=('บริการนี้มีหลายอัตราหรือหลายระยะเวลาต่อรอบ กรุณาระบุบริการและนาทีต่อรอบที่ต้องการครับ','There are multiple services or session lengths. Which service and minutes per session do you want?')
            blocks=[prompts.get(missing[0],messages['missing_input'])[lang=='en']]
            choices=plan.metadata.get('choices',[])
            if choices:blocks.append(('กลุ่มตามตารางราคา: ' if lang=='th' else 'Groups in the rate table: ')+', '.join(x.get(lang) or x.get('en') or x.get('th') for x in choices))
        if plan.metadata.get('calendar_source_limits'):
            blocks.insert(0,('ตารางที่บันทึกไว้ (ยังไม่ยืนยันโซนและช่วงที่มีผล; เวลาเปิดบางรายการขัดแย้ง จึงไม่ใช่การยืนยันสถานะเปิดหรือสิทธิ์จองจริง)' if lang=='th' else 'Recorded schedule only: zone and effective dates are unconfirmed; some opening-hour sources conflict. This does not confirm current opening or actual booking eligibility.'))
        if plan.metadata.get('arithmetic_unconfirmed'):
            blocks.insert(0,'ทราบระยะเวลาที่ต้องการแล้ว แต่ยังไม่มีกฎคำนวณที่ยืนยันสำหรับระยะเวลานี้ อัตราด้านล่างเป็นราคาต่อหน่วยที่บันทึกไว้ ไม่ใช่ยอดรวมของคำขอนี้' if lang=='th' else 'The requested duration is known, but its billing arithmetic is not declared. The following are recorded unit rates, not a confirmed total for this request.')
        if plan.metadata.get('zone_projection_missing'):
            blocks.insert(0,'ยังยืนยันโซนจากความสัมพันธ์ข้อมูลไม่ได้ แต่ยืนยันบริการที่มีเกมนี้ได้ดังนี้' if lang=='th' else 'The zone relation is not confirmed; the following studio services are confirmed to offer this game.')
        if plan.metadata.get('relation_completeness'):
            blocks.insert(0,'รายการที่ยืนยันได้จากความสัมพันธ์ที่มีอยู่ ยังไม่รับรองว่าครบทุกเกมหรือทุกโซน' if lang=='th' else 'Confirmed subset from recorded relations; completeness across all games and zones is not established.')
        if lang=='en' and any(f.get('english_translation_missing') for f in selected):
            blocks.insert(0,'A confirmed English translation is unavailable for some clauses; their Thai source text is retained below.')
        if computations and (billing or people and len(computations)==1):
            total=sum(Decimal(str(c['total_thb'])) for c in computations)
            shown_total=format(total.normalize(),'f')
            blocks.append(f'รวม {shown_total} บาท ตามจำนวนคนและรอบที่ระบุ' if lang=='th' else f'Total: {shown_total} THB for the stated people and sessions.')
        status='unavailable' if claims and all(c['status']=='unavailable' for c in claims) else plan.status
        if plan.metadata.get('price_confirmation_as_of'):
            day=plan.metadata['price_confirmation_as_of'][:10]
            blocks.insert(0,('อัตราที่เจ้าของยืนยันล่าสุด ณ '+day+' (ยังไม่ยืนยันวันเริ่ม–สิ้นสุดใหม่)' if lang=='th' else 'Rates last reaffirmed by the owner on '+day+'; no new effective interval was established.'))
        return {'answer':'\n'.join(blocks),'status':status,'claims':claims,'category':category,'reason':plan.reason,
          'fixture':any(f.get('fixture',False) for f in selected),'english_translation_missing':lang=='en' and any(f.get('english_translation_missing') for f in selected),
          'selection_basis':plan.reason,'computations':computations,'plan':{'facets':plan.facets,'locked':plan.locked,'metadata':plan.metadata}}

    def answer(self,question,locale='auto',category=None,at=None,allow_llm=True,history=None,budget=None,understanding=None):
        started=time.monotonic();at=reference_time(at);budget=budget or RequestBudget()
        from .understanding import interpret,Understanding
        understanding=understanding if understanding is not None else (interpret(question,budget,allow_llm,index=self.index) if category is None else Understanding(reason='explicit_internal_category'))
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
            if previous and cat in {'C04','C05','C06','C07'} and not self.index.bind(cat,part):
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
