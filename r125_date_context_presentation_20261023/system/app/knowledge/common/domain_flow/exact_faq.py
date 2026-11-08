"""Literal whole-question FAQ decisions from the current snapshot.

Owner-added stable Q&A must not require a new parser rule. Dynamic clocks,
occupancy, calculations and tournament dependencies retain their typed paths.
"""
import re,time
from dataclasses import replace
from .scope import norm,validity_allows
from .projection import value,bilingual

def key(text):return re.sub(r'[?!.。！？]+$','',norm(text)).strip()

def candidates(index,question,at):
    from .vocabulary import UNRECORDED_FIELDS,matches
    if matches(UNRECORDED_FIELDS,question):return []
    if re.search(r'ตอนนี้|วันนี้|พรุ่งนี้|มะรืน|เดือนนี้|ปีนี้|ปัจจุบัน|ล่าสุด|ครั้งหน้า|\b(?:now|today|tomorrow|currently|upcoming|latest|next|this (?:month|year))\b',question,re.I):return []
    out=[]
    for rid,r in index.records.items():
        if r.get('kind')!='faq' or value(r,'answer') is None:continue
        labels=bilingual(value(r,'question'))
        if not any(key(s)==key(question) for s in labels.values() if s):continue
        if not re.search(r'[?？]|ไหม|มั้ย|อะไร|ไหน|อย่างไร|ยังไง|\b(?:what|which|where|who|how|can|may|must|do|is|are)\b',' '.join(labels.values()),re.I):continue
        cats={f['category'] for f in index.byrecord[rid]}
        if not cats or cats&{'C06','C07','C11','C12','C13'}:continue
        # Structured descriptors/confirmations are inputs to other operators,
        # not user-facing FAQs to supersede their predicates/dependencies.
        raw=value(r,'source_variants') or value(r,'scope_note') or ''
        if 'r114_fact' in str(raw) or 'r114_confirmation' in str(raw):continue
        proxy={'validity':r.get('validity')}
        if validity_allows(proxy,at) is False:continue
        if not r['fields']['answer'].get('evidence_refs'):continue
        out.append((r,next(iter(cats)) if len(cats)==1 else None))
    return out

def answer(reader,snap,index,question,at,lang):
    rows=candidates(index,question,at)
    if not rows:return None
    from ..request_plan import Need,RequestPlan,VERSION,attach
    started=time.perf_counter();blocks=[];hits=[];receipts=[];variants={}
    for r,cat in rows:
        body=bilingual(value(r,'answer'))[lang] or bilingual(value(r,'answer'))['th']
        variants.setdefault(norm(body),body)
        refs=r['fields']['answer']['evidence_refs']
        if any(p['source_id'] not in snap['release']['sources'] for p in refs):return None
        receipts.append({'record_id':r['record_id'],'field':'answer','status':'known','evidence_refs':refs})
        for ref in refs:
            src=snap['release']['sources'][ref['source_id']]
            hits.append({'id':r['record_id']+':answer:'+str(len(hits)+1),'record_id':r['record_id'],'field':'answer','title':question,'text':body,
                'source_id':ref['source_id'],'snapshot_sha256':src['sha256'],'locator':ref['locator'],'citation_label':'S'+str(len(hits)+1),'source_url':src.get('public_url') or ''})
    conflict=len(variants)>1
    if conflict:blocks.append('พบคำตอบต่างฉบับสำหรับคำถามเดียวกัน จึงยังยืนยันเป็นนโยบายเดียวไม่ได้:' if lang=='th' else 'Recorded answers to this same question differ; one policy cannot be confirmed:')
    if rows[0][1]=='C02':blocks.append('ตามโปรไฟล์ต้นทางที่บันทึกไว้' if lang=='th' else 'According to the recorded source profile:')
    blocks.extend(variants.values())
    ids=[r['record_id'] for r,_ in rows]
    plan={'record_ids':ids,'requested_fields':['answer'],'method':'r124_exact_current_source_question',
        'question_identity_checked':True,'whole_question_match_only':True,'source_answer_confirmed':not conflict,'authority_conflict':conflict}
    result=reader.finish(snap,started,'\n\n'.join(blocks),hits,plan,receipts,response='partial_answer' if conflict else 'answer')
    result=attach(result,RequestPlan(VERSION,question,[Need('r124_faq','record_detail',question,question,ids,[],predicate='exact_source_question')],{'whole_question_identity':True}),snap)
    category=rows[0][1]
    art=result.decision_artifact
    art['need_results']=[{**row,'category':category} for row in art.get('need_results',[])]
    art['execution_contract']={'version':'r124','path':'exact_current_source_question','whole_question_semantics_verified':False,
        'question_identity_checked':True,'tasks':[{'task_id':'t1','terminal_state':'conflict' if conflict else 'supported','receipts':receipts,
            'obligations':[{'kind':'exact_whole_source_question','fulfilled':True}],'semantic_entailment_verified':False}]}
    return replace(result,decision_artifact=art)
