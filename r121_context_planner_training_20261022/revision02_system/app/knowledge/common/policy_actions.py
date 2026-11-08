"""Read a related consumption rule without turning it into bring permission."""
import re
from dataclasses import replace
from .registry import value
from .query_contract import normalize,matches

def answer(reader,question,snap,records,lang,at):
    from .intent_contracts import infer
    if infer(question)['predicate']!='bring_permission':return None
    from .answer import effective
    q=normalize(question)
    # Object cues are language meanings, never a venue permission decision.
    groups=[('alcohol',r'แอลกอฮอล์|เหล้า|เบียร์|\b(?:alcohol|alcoholic|beer|wine)\b'),('food',r'อาหาร|\bfood\b'),('drink',r'เครื่องดื่ม|\b(?:drinks?|beverages?)\b')]
    patterns=[pat for _,pat in groups if re.search(pat,q,re.I)]
    if not patterns:return None
    selected=[]
    for rid,r in records.items():
        if r['kind']!='faq' or not effective(r,at,records):continue
        metadata=str(value(r,'question') or {})+' '+str(value(r,'intent_key') or '')
        content=value(r,'answer') or {};texts=' '.join(str(v) for v in content.values()) if isinstance(content,dict) else str(content)
        if not any(re.search(pat,metadata,re.I) for pat in patterns):continue
        if not re.search(r'รับประทาน|กิน|ดื่ม|\b(?:consum\w*|eat\w*|drink\w*)\b',texts,re.I):continue
        # When an explicit bring condition exists, let the original policy
        # interpreter bind that condition; do not replace it by partial scope.
        if re.search(r'นำ.{0,20}(?:เข้า|มา)|\bbring\b',texts,re.I):return None
        selected.append(rid)
    if not selected:return None
    plan={'record_ids':selected,'scope_ids':selected,'requested_fields':['answer'],'all_fields':False,'platform':None,'operation':'policy','method':'policy_action_scope','unresolved_clauses':[],
          'scope_limits':[{'requested':'bring_permission','confirmed':'consumption_rule_only','reason':'different_action_not_inferred'}]}
    result=reader.execute_task(question,snap=snap,at=at,lang=lang,plan=plan)
    if not result.validation.ok or result.decision_artifact.get('response_type') in {'retry','not_current','unconfirmed'}:return result
    note=('ข้อมูลต่อไปนี้ยืนยันกฎการรับประทานหรือดื่มภายในศูนย์ แต่ยังไม่ยืนยันเงื่อนไขการนำสิ่งที่ถามเข้ามาครับ' if lang=='th' else 'The following sources confirm consumption rules inside the studio. They do not separately confirm permission to bring the item into the studio.')
    art=dict(result.decision_artifact);art.update(response_type='partial_answer',source_scope_review={'requested':'bring_permission','confirmed':'consumption_rule_only','permission_inferred':False})
    return replace(result,answer=note+'\n\n'+result.answer,mode='pipeline:common_partial_answer',route=replace(result.route,answer_type='partial_answer'),decision_artifact=art)
