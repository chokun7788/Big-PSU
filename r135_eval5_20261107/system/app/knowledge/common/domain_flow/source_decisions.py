"""Source-attested FAQ scopes, distinct from model predictions and game modes.

The content package owns aliases and bounded predicate matchers. A match cannot
authorize extra conditions, current occupancy, historical validity or a different
tournament. Corrections require the exact replaced field revision and digest.
"""
import hashlib,json,re
from .projection import value,bilingual
from .scope import validity_allows

def digest(x):
    return hashlib.sha256(json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def verified(index,record):
    profile=value(record,'legacy_search') or {}
    decision=profile.get('source_decision')
    if not isinstance(decision,dict) or decision.get('version')!=1:return None
    # Pin the entire mapping and answer to the same immutable source body.
    from ..registry import pointer,source_errors
    refs=record['fields']['legacy_search'].get('evidence_refs',[])
    if not refs:return None
    for ref in refs:
        pair=index.source_pairs.get(ref.get('source_id'))
        if not pair:return None
        src,body=pair
        try:
            if source_errors(src,body,demo=False) or src.get('trust') not in {'owner_confirmed','internal_verified'} or 'faq' not in src.get('authority_for',[]):return None
            mapped=pointer(json.loads(body),ref['locator'])
            if mapped!=profile:return None
        except (ValueError,TypeError,KeyError,IndexError):return None
    for field in ('question','answer'):
        f=record['fields'][field]
        if f.get('status')!='known' or not f.get('evidence_refs'):return None
        for ref in f['evidence_refs']:
            pair=index.source_pairs.get(ref.get('source_id'))
            try:
                if not pair or source_errors(*pair,demo=False) or pointer(json.loads(pair[1]),ref['locator'])!=f['value']:return None
            except (ValueError,TypeError,KeyError,IndexError):return None
    if decision.get('category') not in {'C01','C03','C04','C08','C09','C10'}:return None
    if decision.get('scope')!='general_studio':return None
    return decision

def entries(index):
    if hasattr(index,'_source_decisions'):return index._source_decisions
    index._source_decisions=[]
    for r in index.records.values():
        if r.get('kind')!='faq':continue
        d=verified(index,r)
        if d:index._source_decisions.append((r,d))
    return index._source_decisions

def canonical(text):
    from .exact_faq import key
    return key(text)

def match(index,question,at=None,category=None):
    # Independent questions must be split by the task graph before this reader.
    from .routing import split_needs
    if len(question)>600 or len(split_needs(question))>1:return []
    if re.search(r'แล้ว(?:ราคา|จอง|เปิด|ปิด)|และ(?:ราคา|วิธีจอง|เวลาเปิด)|\band(?: also)?\b.{0,20}(?:price|book|open)',question,re.I):return []
    q=canonical(question)
    if re.search(r'แข่งขัน|กติกา|ทัวร์นาเมนต์|tournament|competition|rulebook|\b20\d{2}\b|เมื่อก่อน|ปีที่แล้ว|เดือนที่แล้ว|วันที่\s*\d|last (?:year|month)|previously|as of',q,re.I):return []
    hits=[]
    for r,d in entries(index):
        if category and d['category']!=category:continue
        if at is not None and validity_allows({'validity':r.get('validity')},at) is False:continue
        source_exact=any(canonical(s)==q for s in bilingual(value(r,'question')).values() if s)
        alias_exact=any(canonical(s)==q for s in d.get('question_aliases',[]) if s)
        exact=source_exact or alias_exact
        if not exact:
            joined=re.sub(r'(?:คีย์บอร์ด\s*(?:และ|กับ)\s*เมาส์|keyboard\s+and\s+(?:mouse|mice))','device_pair',q,flags=re.I)
            joined=re.sub(r'แล้ว(?=หรือยัง|รึยัง|ไหม|มั้ย)','',joined)
            if re.search(r'และ|แล้ว|พร้อมกับ|อีกอย่าง|กับ(?:ขอ|มี|ถาม|อยาก|ราคา|เกม|จอง|เปิด)|\band\b|\balso\b',joined,re.I):continue
            markers=re.findall(r'ไหม|มั้ย|หรือยัง|หรือเปล่า|เท่าไหร่|ใคร|ที่ไหน|อะไร|ยังไง|\b(?:what|which|who|where|how|can|may)\b',joined,re.I)
            if len(markers)>1:continue
            rules=d.get('match',{})
            try:
                if not rules.get('all') or not all(re.search(p,q,re.I) for p in rules['all']):continue
                if any(re.search(p,q,re.I) for p in rules.get('none',[])):continue
                # Quantified/new requested details need their own typed source.
                if re.search(r'ราคา|กี่บาท|กี่นาที|กี่ชั่วโมง|กี่วัน|กี่คน|กี่ปี|ขั้นต่ำ|สูงสุด|ขั้นต่ำ|รับประกัน|คืนเงินภายใน|\b(?:price|cost|how much|how many|maximum|minimum|guarantee|expires?)\b',q,re.I):continue
                if re.search(r'\d',q) and not rules.get('numbers_allowed'):continue
            except (TypeError,re.error):continue
            if d.get('claim_class')=='group_recommendation':
                # A named game/platform narrows a generic recommendation into
                # another request. Do not return all owner options for it.
                from .dialogue_task import mentions,platforms
                if mentions(index,q,{'game'}) or platforms(index,q):continue
        # Literal identity does not expand the fact's scope. Some original
        # questions ask more than the owner actually established.
        hits.append((r,d,{'basis':'whole_source_question' if source_exact else 'source_declared_question_alias' if alias_exact else 'source_declared_predicate_with_qualifiers'}))
    return hits

def correction(index,record,decision):
    proofs=[]
    for rule in decision.get('corrections',[]):
        old=index.records.get(rule.get('record_id'),{})
        field=old.get('fields',{}).get(rule.get('field'),{})
        if old.get('revision')!=rule.get('revision') or digest(field)!=rule.get('field_sha256'):continue
        # The correction itself was source-attested in verified(). Explicit
        # human correction evidence is required; recency/trust alone is not.
        if not rule.get('owner_correction_quote') or not rule.get('owner_source_pointer'):continue
        evidence=decision.get('original_evidence',[])
        if not any(e.get('pointer')==rule['owner_source_pointer'] and rule['owner_correction_quote'] in json.dumps(e.get('value'),ensure_ascii=False) for e in evidence):continue
        proofs.append({**rule,'replacement_record_id':record['record_id'],'scope':decision['scope']})
    return proofs

def unique(index,question,at=None,category=None):
    hits=match(index,question,at,category)
    # Different applicable actions are not settled by a lexical priority score.
    if len(hits)!=1:return None
    return hits[0]

def current_corrections(index):
    if hasattr(index,'_current_corrections'):return index._current_corrections
    proofs=[p for r,d in entries(index) for p in correction(index,r,d)]
    # Withdrawal of a replacement policy does not make an explicitly attested
    # migration error true again. Keep the rejection receipt, while withholding
    # the withdrawn replacement itself. This is not a policy recency rule.
    from ..registry import source_errors
    for src,body in index.source_pairs.values():
        if src.get('trust') not in {'internal_verified','owner_confirmed'} or not {'faq','policy'}<=set(src.get('authority_for',[])):continue
        try:
            if source_errors(src,body,demo=False):continue
            d=json.loads(body)['mapped_fields']['legacy_search']['source_decision']
            if d.get('scope')!='general_studio':continue
            error_only={**d,'corrections':[c for c in d.get('corrections',[]) if c.get('correction_kind')=='migration_error']}
            proofs.extend(correction(index,{'record_id':None},error_only))
        except (KeyError,TypeError,ValueError):continue
    unique={}
    for p in proofs:
        k=(p['record_id'],p['field'],p['revision'],p['field_sha256'])
        if k not in unique or p['replacement_record_id'] is not None:unique[k]=p
    index._current_corrections=list(unique.values())
    return index._current_corrections

def guard_result(reader,result,snap,index,question,at,lang):
    """Prevent a compatibility reader from reviving a corrected old field."""
    art=result.decision_artifact or {}
    from .controller_catalog import request as controller_request,delivery_errors as controller_errors,notice as controller_notice
    controller=controller_request(index,question)
    delivered=(art.get('domain_flow') or {}).get('typed_claims',[])
    if controller and not delivered:
        delivered=[c for need in art.get('need_results',[]) for c in need.get('claim_packets',[])]
        if not delivered:delivered=[{'record_id':o.get('record_id'),'facet':o.get('field'),'value':None} for o in art.get('obligations',[]) if o.get('record_id')]
    if controller and delivered:
        if controller_errors(index,question,delivered,at,art.get('need_results',[])):
            import time
            from dataclasses import replace
            safe=reader.finish(snap,time.perf_counter(),controller_notice(lang),[],{'record_ids':[],'requested_fields':[],'method':'controller_scope_guard','controller_scope':controller},[],response='unconfirmed')
            return replace(safe,decision_artifact={**safe.decision_artifact,'controller_scope_rejection':{'reason':'console_catalog_does_not_establish_controller_support','rejected_record_ids':[c.get('record_id') for c in delivered],'source_scope_recomputed':True}})
    ids=set()
    def visit(x):
        if isinstance(x,dict):
            if isinstance(x.get('record_id'),str):ids.add(x['record_id'])
            if isinstance(x.get('record_ids'),list):ids.update(s for s in x['record_ids'] if isinstance(s,str))
            for v in x.values():visit(v)
        elif isinstance(x,list):
            for v in x:visit(v)
    # Inspect delivered reads, not rejected candidates or the correction audit
    # itself (which necessarily names the replaced record).
    visit(art.get('obligations',[]))
    visit({'record_ids':(art.get('query_plan') or {}).get('record_ids',[])})
    visit((art.get('domain_flow') or {}).get('typed_claims',[]))
    for need in art.get('need_results',[]):visit(need.get('claim_packets',[]))
    invalid=ids&getattr(index,'invalid_source_decisions',set())
    if invalid:
        import time
        return reader.finish(snap,time.perf_counter(),'แหล่งอ้างอิงของคำตอบฉบับนี้ตรวจยืนยันไม่ผ่าน จึงยังตอบยืนยันไม่ได้ครับ' if lang=='th' else 'The source mapping for this answer did not verify, so it cannot be confirmed.',[],{'record_ids':[],'requested_fields':[],'method':'invalid_source_decision_rejected','invalid_record_ids':sorted(invalid)},[],response='unconfirmed')
    affected=[p for p in current_corrections(index) if p['record_id'] in ids]
    if not affected:return result
    import time
    if re.search(r'แข่งขัน|กติกา|tournament|competition|rulebook|\b20\d{2}\b',question,re.I):
        return reader.finish(snap,time.perf_counter(),'ข้อมูลบริการทั่วไปใช้ยืนยันกฎรายการแข่งขันหรือฉบับย้อนหลังนี้ไม่ได้ครับ' if lang=='th' else 'General studio information does not establish this tournament or historical rule.',[],{'record_ids':[],'requested_fields':[],'method':'source_correction_scope_guard','superseded_read_rejected':affected},[],response='unconfirmed')
    replacements={p['replacement_record_id'] for p in affected}
    replacements={rid for rid in replacements if rid in index.records and any(r['record_id']==rid for r,d in entries(index))}
    if not replacements:
        return reader.finish(snap,time.perf_counter(),'คำตอบฉบับเดิมมีหลักฐานว่าถูกย้ายผิด และฉบับทดแทนไม่มีสถานะใช้งานแล้ว จึงยังยืนยันนโยบายนี้ไม่ได้ครับ' if lang=='th' else 'The earlier answer was an attested migration error, and no active replacement is available. This policy cannot be confirmed.',[],{'record_ids':[],'requested_fields':[],'method':'inactive_replacement_does_not_revive_migration_error','rejected_fields':affected},[],response='unconfirmed')
    rows=[(index.records[rid],next(d['category'] for r,d in entries(index) if r['record_id']==rid)) for rid in replacements]
    from .exact_faq import answer as render
    return render(reader,snap,index,question,at,lang,_rows=rows,_source_decision={'basis':'compatibility_read_of_explicitly_corrected_field','partial':True,'corrections':affected,'limits':['extra_requested_detail_not_established'],'semantic_entailment_verified':False})

def plan(index,question,at=None,category=None):
    row=unique(index,question,at,category)
    if not row:return None
    r,d,receipt=row
    fs=index.byrecord[r['record_id']]
    if not fs:return None
    from .readers import confirmed
    adjacent=d.get('partial') and d.get('claim_class') in {'group_recommendation','update_schedule_not_live_version','contact_not_admission_guarantee','notification_not_refund_or_reschedule'}
    result=confirmed(d['category'],fs,'source_declared_scoped_decision',source_decision={**receipt,'record_id':r['record_id'],'source_scope':d['scope'],'claim_class':d.get('claim_class','policy'),'limits':d.get('limits',[]),'corrections':correction(index,r,d)},adjacent_source_subset=bool(adjacent))
    result.locked=True
    if d.get('partial'):result.status='partial'
    return result

def answer(reader,snap,index,question,at,lang):
    row=unique(index,question,at)
    if not row:return None
    r,d,receipt=row
    from .exact_faq import answer as render
    return render(reader,snap,index,question,at,lang,_rows=[(r,d['category'])],_source_decision={**receipt,'record_id':r['record_id'],'partial':bool(d.get('partial')),'scope':d['scope'],'claim_class':d.get('claim_class','policy'),'limits':d.get('limits',[]),'corrections':correction(index,r,d),'semantic_entailment_verified':False})
