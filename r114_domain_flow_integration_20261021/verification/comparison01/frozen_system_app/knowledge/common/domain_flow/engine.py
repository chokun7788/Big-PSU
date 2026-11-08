"""One domain execution path for snapshots, chat and source-contract evaluation."""
import re,time,threading
from collections import OrderedDict
from decimal import Decimal
from .contracts import Plan,RequestBudget
from .index import FactIndex
from .model import EvidenceSelector
from .scope import reference_time,norm,contains,years,requested_years,validity_allows,requested_minutes
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
        pool=[self.index.byid[k] for k in plan.candidates if k in self.index.byid]
        if category=='C13':
            asked=years(question)
            if asked:pool=[f for f in pool if asked<=years(' '.join(f['subject'].values()))]
        if plan.facets:
            strict=[f for f in pool if f['facet'] in plan.facets]
            if strict:pool=strict
        return [f for _,f in self.index.rank(category,question,pool=pool,limit=8)]

    def finish_plan(self,category,question,plan,at):
        # The model only sees a scoped pool, and selection must remain in that
        # pool. A cross-category/source ID can never enter the renderer.
        selected=[self.index.byid[k] for k in plan.ids if k in self.index.byid and self.index.byid[k]['category']==category]
        if len(selected)!=len(plan.ids):return blocked(category,'invalid_or_cross_category_fact','unavailable')
        asked=years(question) if category=='C13' else requested_years(question)
        if category=='C13' and asked and any(not asked<=years(' '.join(f['subject'].values())) for f in selected):
            return blocked(category,'selected_rule_event_year_mismatch')
        if category in {'C06','C07'} and selected:
            price=[f for f in selected if f['facet'] in {'amount','amount_thb'}]
            requested_at=at.replace(year=next(iter(asked))) if len(asked)==1 else at
            expired=[f for f in price if validity_allows(f,requested_at) is False and not (f.get('confirmation_ref') and (not asked or asked=={at.year}))]
            if expired:return blocked(category,'rate_not_effective_for_request','not_current')
            minutes=requested_minutes(question)
            if category=='C06' and minutes is not None:
                for f in price:
                    record=self.index.records.get(f['record_id'],{});duration=(record.get('fields',{}).get('duration_minutes') or {}).get('value')
                    if duration is not None and duration!=minutes:return blocked(category,'requested_duration_not_supported_by_selected_rate','missing_input')
        return plan

    def _render_one(self,category,question,locale,plan,at):
        lang=language(question,locale);selected=[self.index.byid[k] for k in plan.ids]
        claims=[];blocks=[];computations=[]
        quantity_q=norm(question)
        for s in sorted({norm(v) for f in selected for v in f['subject'].values()},key=len,reverse=True):quantity_q=quantity_q.replace(s,' ')
        m=re.search(r'(\d+)\s*รอบ|\b(\d+)\s+sessions?\b',quantity_q);sessions=int(next(x for x in m.groups() if x)) if m else 1
        people=re.search(r'(\d+)\s*คน|\b(\d+)\s+(?:people|persons?|players?)\b',quantity_q);persons=int(next(x for x in people.groups() if x)) if people else 1
        for f in selected:
            value=f['value'][lang];numeric=f.get('numeric')
            if category=='C06' and f['facet']=='amount' and numeric is not None:
                numeric=float(Decimal(str(numeric))*sessions)
                if m:value=(f'{numeric:g} บาทต่อคน สำหรับ {sessions} รอบ' if lang=='th' else f'{numeric:g} THB per person for {sessions} sessions')
                computations.append({'fact_id':f['id'],'rate_per_person_per_session':f['numeric'],'sessions':sessions,'persons':persons,
                  'total_thb':float(Decimal(str(f['numeric']))*sessions*persons),'assumption':'same audience and service; whole sessions only','evidence_refs':f['evidence_refs']})
            state='unavailable' if f.get('provider_state') in {'unavailable','stale'} else 'answer'
            claims.append({'fact_id':f['id'],'record_id':f['record_id'],'facet':f['facet'],'value':value,'numeric':numeric,
              'evidence_refs':f['evidence_refs'],'fixture':f.get('fixture',False),'status':state})
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
        status='unavailable' if claims and all(c['status']=='unavailable' for c in claims) else plan.status
        return {'answer':'\n'.join(blocks),'status':status,'claims':claims,'category':category,'reason':plan.reason,
          'fixture':any(f.get('fixture',False) for f in selected),'english_translation_missing':lang=='en' and any(f.get('english_translation_missing') for f in selected),
          'selection_basis':plan.reason,'computations':computations,'plan':{'facets':plan.facets,'locked':plan.locked,'metadata':plan.metadata}}

    def answer(self,question,locale='auto',category=None,at=None,allow_llm=True,history=None,budget=None):
        started=time.monotonic();at=reference_time(at);budget=budget or RequestBudget();needs=split_needs(question);children=[];previous=''
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
