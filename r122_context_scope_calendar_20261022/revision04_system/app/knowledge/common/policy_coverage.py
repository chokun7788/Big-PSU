"""Source-scoped coverage of coordinated policy facets; no invented penalties."""
import re,time,json
from .registry import value

FACETS={
 'food':r'อาหาร|เครื่องดื่ม|\b(?:food|drinks?|eating)\b',
 'noise':r'เสียงดัง|ส่งเสียง|\b(?:noise|loud|shouting)\b',
 'damage':r'เสียหาย|ชดเชย|ค่าปรับ|\b(?:damag\w*|compensation|penalt\w*)\b'}
def prose(record,field,lang):
    x=value(record,field)
    return str((x.get(lang) or '') if isinstance(x,dict) else x or '')

def answer(reader,need,snap,at,lang):
    if need.task not in {'policy','faq_content','unresolved'}:return None
    facets=[k for k,p in FACETS.items() if re.search(p,need.query,re.I)]
    if len(facets)<2:return None
    from .answer import effective
    records=snap['release']['records'];selected=[];coverage=[]
    for facet in facets:
        candidates=[]
        for rid,r in records.items():
            if r['kind'] not in {'faq','policy'} or rid in snap.get('withdrawn',[]) or not effective(r,at,records):continue
            heading=' '.join(prose(r,k,lang) for k in ('question','subject','topic'))
            body=' '.join(prose(r,k,lang) for k in ('answer','details','consequence'))
            if not re.search(FACETS[facet],heading,re.I) or not body:continue
            # A named severity may constrain selection; general questions may
            # use a complete source that explicitly preserves all severities.
            severity=[p for p in (r'เล็กน้อย|\bminor\b',r'ปานกลาง|\bmoderate\b',r'ร้ายแรง|\bsevere\b') if re.search(p,need.query,re.I)]
            if facet=='damage' and not severity and any(re.search(p,heading,re.I) for p in (r'เล็กน้อย|\bminor\b',r'ปานกลาง|\bmoderate\b',r'ร้ายแรง|\bsevere\b')):continue
            if severity and not any(re.search(p,heading+' '+body,re.I) for p in severity):continue
            other=sum(bool(re.search(p,heading,re.I)) for k,p in FACETS.items() if k!=facet)
            score=10-3*other
            if facet=='damage' and re.search(r'\d.{0,25}(?:บาท|THB|baht)',body,re.I):score+=2
            candidates.append((score,rid))
        candidates.sort(key=lambda x:(-x[0],x[1]))
        if candidates:selected.append(candidates[0][1]);coverage.append({'facet':facet,'record_id':candidates[0][1],'status':'source_selected'})
        else:coverage.append({'facet':facet,'status':'missing_source'})
    selected=list(dict.fromkeys(selected))
    if not selected:return None
    fields=[k for k in ('answer','decision','conditions_all','exceptions','details','consequence') if any(value(records[r],k) is not None for r in selected)]
    plan={'record_ids':selected,'scope_ids':selected,'requested_fields':fields,'operation':'policy','method':'r102_policy_facet_coverage','all_fields':False,
      'unresolved_clauses':[],'task_plan':{'task':'policy','predicate':'policy_applicability'},'policy_facet_coverage':coverage}
    result=reader.execute_task(need.query,snap=snap,at=at,lang=lang,plan=plan)
    if result and any(x['status']=='missing_source' for x in coverage):
        from dataclasses import replace
        missing=', '.join(x['facet'] for x in coverage if x['status']=='missing_source')
        note=('ยังไม่มีข้อมูลยืนยันครบสำหรับ: ' if lang=='th' else 'Confirmed details are still missing for: ')+missing
        result=replace(result,answer=result.answer+'\n\n'+note,decision_artifact={**result.decision_artifact,'response_type':'partial_answer','missing_policy_facets':missing})
    return result
