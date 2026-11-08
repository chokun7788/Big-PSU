"""Intersect material service scope with audience scope before reading rates."""
import re,time
from .registry import value
from .read_graph import linked

def resolve(reader,need,snap,records,ids,targets,lang):
    from .audience_scope import resolve as audiences
    from .answer import title
    groups,audit=audiences(need.query,records)
    material=[k for k in ids if records[k]['kind'] not in {'audience','rate'}]
    if material:
        scoped,_=linked(records,material,'price')
        services={value(records[k],'service_id') for k in scoped if records[k]['kind']=='rate'}
        targets=[k for k in targets if value(records[k],'service_id') in services]
    targets=[k for k in targets if value(records[k],'audience_id') not in audit.get('excluded_ids',[])]
    if groups:targets=[k for k in targets if value(records[k],'audience_id') in groups]
    if not targets:return [],groups,None
    if all(records[k]['validity']['state']=='unknown' for k in targets):
        body='ยังยืนยันราคาปัจจุบันไม่ได้ครับ ข้อมูลอัตราที่เกี่ยวข้องยังไม่มีวันที่มีผลที่ยืนยันแล้ว' if lang=='th' else 'The current price cannot be confirmed because the relevant rates have no confirmed effective dates.'
        result=reader.finish(snap,time.perf_counter(),body,[],{'record_ids':targets,'requested_fields':[],'method':'r102_price_effective_dates_missing','bridge_status':'owner_dates_missing'},[],response='unconfirmed')
        return targets,groups,result
    candidates=sorted({value(records[k],'audience_id') for k in targets if value(records[k],'audience_id') in records},key=lambda k:title(records[k],lang))
    all_groups=bool(re.search(r'ทั้งหมด|ทุกกลุ่ม|\b(?:all|every)\b',need.query,re.I))
    if not groups and not all_groups and (len(candidates)>1 or groups==[]):
        body=('ราคาขึ้นกับกลุ่มผู้ใช้ครับ ต้องการดูอัตราของกลุ่มใด: ' if lang=='th' else 'The price depends on the audience. Which audience rate should I check: ')+' / '.join(title(records[k],lang) for k in candidates)
        plan={'record_ids':[],'requested_fields':[],'method':'r102_required_audience_slot','audience_audit':audit,
          'pending_selection':{'candidate_ids':candidates,'subject_kind':'audience','scope_root_ids':material or ids,'allow_all':True}}
        return targets,groups,reader.finish(snap,time.perf_counter(),body,[],plan,[],response='clarification')
    return targets,groups,None
