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

    def plan(self,category,question,at=None):
        return read(self.index,category,question,reference_time(at))

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
                    if calc.get('error'):return blocked(category,calc['error'],calc['status'])
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
            if category=='C06' and f['facet']=='amount' and numeric is not None:
                calc=plan.metadata.get('unit_calculations',{}).get(f['id'])
                numeric=calc['amount_thb'] if calc else float(Decimal(str(numeric))*sessions)
                per_person=f.get('confirmed_per_person') or f.get('billing_unit')=='per_person' or f.get('calculation')=='integer_sessions_per_person'
                if m:
                    unit=('ต่อคน','per person') if per_person else ('ต่อกลุ่ม','per group') if f.get('billing_unit')=='per_group' else ('ตามหน่วยที่ระบุ','for the stated billing unit')
                    value=(f'{numeric:g} บาท{unit[0]} สำหรับ {sessions} รอบ' if lang=='th' else f'{numeric:g} THB {unit[1]} for {sessions} sessions')
                count=billing.get(f['id'],{}).get('persons',persons)
                if f.get('billing_unit')=='per_group':count=1
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
        missing=plan.metadata.get('missing_slots',[])
        if not selected and missing:
            prompts={'audience':('ผู้เล่นอยู่ในกลุ่มผู้ใช้ใดครับ?','Which audience group applies to the players?'),
              'persons_per_audience':('แต่ละกลุ่มมีผู้เล่นกี่คน และเลือกบริการใดครับ?','How many players are in each audience group, and which service is requested?'),
              'service':('ต้องการทราบราคาของบริการใดครับ?','Which service do you want a price for?'),
              'rental_package':('ต้องการเหมาโซนใด สำหรับหน่วยงานภายในหรือภายนอก และครึ่งวันหรือเต็มวันครับ?','Which zone, organization audience and half/full-day package do you want?')}
            prompts['positive_quantity']=('กรุณาระบุจำนวนคนหรือรอบเป็นจำนวนเต็มมากกว่า 0 ครับ','Please give a positive whole number of people or sessions.')
            prompts['event']=('ต้องการกติกาของรายการหรือฉบับใดครับ?','Which tournament or rulebook edition do you mean?')
            blocks=[prompts.get(missing[0],messages['missing_input'])[lang=='en']]
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

    def answer(self,question,locale='auto',category=None,at=None,allow_llm=True,history=None,budget=None):
        started=time.monotonic();at=reference_time(at);budget=budget or RequestBudget();needs=split_needs(question,self.index);children=[];previous=''
        for part in needs:
            cat=category or route(self.index,part)
            scoped_q=part
            if previous and cat in {'C04','C05','C06','C07'} and not self.index.bind(cat,part):
                # Inherit only a source-bound name from a prior need, never its
                # answer or an unverified model-generated factual statement.
                names={s for f in self.index.facts for s in f['subject'].values() if contains(previous,s)}
                if names:scoped_q=part+' '+max(names,key=len)
            if cat is None:
                p=blocked('','domain_not_bound');children.append(self._render_one('',part,locale,p,at));continue
            plan=self.plan(cat,scoped_q,at)
            if plan.ambiguous and allow_llm and not plan.locked:
                candidates=self.scoped_candidates(cat,scoped_q,plan,at)
                if candidates:
                    plans,event=self.selector.select([{'question':scoped_q,'language':language(part,locale),'facts':candidates}],budget)
                    plan=plans[0];plan.category=cat
            if plan.ambiguous and not allow_llm:
                plan.status='missing_source';plan.reason='typed_interpretation_unresolved';plan.ambiguous=False
                plan.metadata['compatibility_allowed']=bool(self.index.bind(cat,scoped_q))
            plan=self.finish_plan(cat,scoped_q,plan,at);result=self._render_one(cat,scoped_q,locale,plan,at)
            result['question']=part;children.append(result);previous=scoped_q
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
        return {'answer':'\n\n'.join(blocks),'status':state,'claims':claims,'needs':children,'model_events':budget.events,
          'elapsed_sec':time.monotonic()-started,'fixture':any(r['fixture'] for r in children),'english_translation_missing':any(r['english_translation_missing'] for r in children),
          'selection_basis':'r114_domain_flow','effective_locale':language(question,locale),'release_id':self.data.get('release_id'),'epoch':self.data.get('epoch')}
