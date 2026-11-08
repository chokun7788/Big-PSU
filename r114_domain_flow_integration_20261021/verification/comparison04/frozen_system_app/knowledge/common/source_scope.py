"""Preserve the difference between consumption location and food-origin permission."""
import re
from dataclasses import replace
from .registry import value

ORIGIN=r'ข้างนอก|ภายนอก|(?:อาหาร|เครื่องดื่ม).{0,12}(?:ตัวเอง|มาเอง)|\b(?:outside|own|personal)\b'

def qualify(result,question,records,lang):
    if not re.search(r'อาหาร|เครื่องดื่ม|\b(?:food|drinks?|beverages?)\b',question,re.I) or not re.search(ORIGIN,question,re.I):return result
    art=dict(result.decision_artifact or {})
    if not result.validation.ok or art.get('response_type') not in {'answer','list','partial_answer'}:return result
    ids={h.get('record_id') for h in result.hits}
    selected=[records[k] for k in ids if k in records and records[k]['kind'] in {'faq','policy'}]
    if not selected:return result
    texts=[]
    for record in selected:
        for key in ('answer','text'):
            content=value(record,key)
            if isinstance(content,dict):texts.extend(str(t) for t in content.values() if t)
            elif isinstance(content,str):texts.append(content)
    if not texts or any(re.search(ORIGIN,t,re.I) for t in texts):return result
    if not any(re.search(r'รับประทาน|บริเวณ|พื้นที่|\b(?:consum|designated|eating|area)',t,re.I) for t in texts):return result
    note=('แหล่งข้อมูลนี้ระบุพื้นที่รับประทานเท่านั้น ยังไม่ยืนยันว่าอนุญาตให้นำอาหารหรือเครื่องดื่มของตัวเองเข้ามาได้หรือไม่ครับ' if lang=='th' else 'This source specifies consumption areas only. Permission to bring your own food or drinks is not confirmed.')
    query=dict(art.get('query_plan') or {});limits=list(query.get('scope_limits',[]))
    limits.append({'requested':'food_origin_permission','status':'not_confirmed','reason':'source_only_covers_consumption_area'})
    query['scope_limits']=limits
    art.update(query_plan=query,response_type='partial_answer',source_scope_review={'requested':'food_origin_permission','confirmed':'consumption_area_only','permission_inferred':False})
    return replace(result,answer=note+'\n\n'+result.answer,mode='pipeline:common_partial_answer',route=replace(result.route,answer_type='partial_answer'),decision_artifact=art)
