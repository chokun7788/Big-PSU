from pathlib import Path
import json,hashlib
p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');r=Path(Path('r30_report_path.txt').read_text().strip())
def edit(rel,old,new):
    f=p/rel;s=f.read_text(encoding='utf-8');assert s.count(old)==1,(rel,s.count(old));f.write_text(s.replace(old,new),encoding='utf-8')
files=['app/core/duration_alternatives.py','app/pipeline/service_fee_alternatives.py','app/pipeline/control_button_target.py','app/pipeline/closed_query_improvements.py']
for rel in files:
    dest=r/'before_D'/rel;dest.parent.mkdir(parents=True,exist_ok=True);assert not dest.exists();dest.write_bytes((p/rel).read_bytes())
edit(files[0],"_SHARED=re.compile(r'(?<![0-9A-Za-z:.])(?P<a>'+_NUM+r')\\s*(?:'+_JOIN+r')\\s*(?P<b>'+_NUM+r')\\s*(?P<u>'+_UNIT+r')',re.I)","_SHARED=re.compile(r'(?<![0-9A-Za-z:.])(?P<chain>(?:'+_NUM+r'\\s*(?:'+_UNIT+r')?\\s*(?:'+_JOIN+r')\\s*)+'+_NUM+r'\\s*'+_UNIT+r')',re.I)")
edit(files[0],"        values=tuple(dict.fromkeys(_minutes(shared[g],shared['u']) for g in ('a','b')))",'''        parts=re.split(r'\\s*(?:'+_JOIN+r')\\s*',shared['chain'],flags=re.I)
        values=[];carried_unit=None
        for part in reversed(parts):
            item=re.fullmatch(r'('+_NUM+r')\\s*('+_UNIT+r')?',part.strip(),re.I)
            if item is None:return None
            carried_unit=item.group(2) or carried_unit
            if carried_unit is None:return None
            values.append(_minutes(item.group(1),carried_unit))
        values=tuple(dict.fromkeys(reversed(values)))''')
edit(files[1],"    if english:\n        from app.pipeline.bilingual_english import _detect_group as detect_group,_GROUP_LABELS_EN,_people",'''    from app.core.customer_group import excludes_student_group
    if excludes_student_group(query):
        # A denied affiliation does not establish another price entitlement.
        # Clarify unless a separate positive customer group is explicit.
        positive_group=re.search(r'บุคคลทั่วไป|ผู้ใหญ่|ศิษย์เก่า|ต่างสถาบัน|ต่างมหาวิทยาลัย|\\b(?:general adult|general public|alumni|external student|other university|PSU staff)\\b',query,re.I)
        if not positive_group:
            answer=('Which current user group applies: PSU staff, PSU alumni or students from another institution, or general adults? Saying you are not a PSU student does not identify your fee group.' if english else
                    'ปัจจุบันอยู่กลุ่มใดครับ: บุคลากร PSU, ศิษย์เก่า PSU/นักศึกษาต่างสถาบัน หรือบุคคลทั่วไป การบอกว่าไม่ใช่นักศึกษา มอ ยังระบุกลุ่มราคาที่ใช้ไม่ได้')
            return StructuredToolResult(answer,[],'service_fee_customer_group_clarification',.98,{'reason':'negated_membership_does_not_establish_group'})
        # Remove only the denied affiliation before the existing group resolver.
        query=re.sub(r'ไม่ใช่\\s*(?:นักศึกษา|นักเรียน|นิสิต|เด็ก)\\s*(?:มอ|psu)?|\\bnot\\s+(?:a\\s+)?(?:psu\\s+)?student\\b', '',query,flags=re.I)
    if english:
        from app.pipeline.bilingual_english import _detect_group as detect_group,_GROUP_LABELS_EN,_people''')
edit(files[1],"capacity=fee['capacity'].replace('คน','people') if english else fee['capacity']","capacity=('1 person' if fee['capacity']=='1 คน' else fee['capacity'].replace('คน','people')) if english else fee['capacity']")
edit(files[2],"r'[rlf]\\d+|dpad(?:up|down|left|right)?'","r'[a-z]+\\d+|dpad(?:up|down|left|right)?'")
edit(files[3],"    if not resolution.is_exact or resolution.top_candidate is None:return None",'''    if not resolution.is_exact or resolution.top_candidate is None:
        answer=('Please specify the full game title and edition. I cannot select a booking service without a verified game-to-service match.' if english else
                'กรุณาระบุชื่อเกมและภาคให้ชัดเจนครับ ยังเลือกบริการให้ไม่ได้จนกว่าจะพบเกมที่ตรงกับรายการบริการที่ยืนยันได้')
        return StructuredToolResult(answer,[],'booking_game_target_clarification',.98,{'resolution':resolution.as_dict(),'no_inferred_booking_service':True})''')
edit(files[3],"    if not rows:return None",'''    if not rows:
        answer=(f'I could not find a recorded booking service for {game}. Please check with studio staff before booking for this game.' if english else
                f'ยังไม่พบบริการจองที่มี {game} ในรายการที่บันทึกไว้ครับ กรุณาตรวจสอบกับเจ้าหน้าที่ก่อนจองเพื่อเล่นเกมนี้')
        return StructuredToolResult(answer,[],'booking_game_service_no_answer',.98,{'game':game,'no_inferred_booking_service':True})''')
edit(files[3],"def answer_closed_query_improvement(query,locale):",'''def _fee_catalog(query,locale):
    from app.core.normalization import has_price_intent,SERVICE_ALIASES,contains_alias
    if not (has_price_intent(query) or re.search(r'\\b(?:prices?|fees?|costs?)\\b',query,re.I)):return None
    if not re.search(r'แต่ละ(?:เครื่อง|โซน|บริการ)|ตาราง.*ราคา|ค่าบริการ.*ทั้งหมด|ราคา.*ทั้งหมด|ค่าเล่น.*(?:เครื่อง|โซน).*บ้าง|\\b(?:each|all)\\s+(?:service|zone|device|station)s?\\b',query,re.I):return None
    if any(contains_alias(query,a,fuzzy=False)[0] for a in SERVICE_ALIASES.values()):return None
    from app.calculator.service_fee import SERVICE_FEES,GROUP_LABELS
    from app.pipeline.bilingual_english import _GROUP_LABELS_EN
    from app.core.source_registry import SERVICE_FEE_IMAGE_2026_ID,PC_SERVICE_FEE_LOCAL_UPDATE_20260727_ID,make_source_hits
    en=locale=='en';labels=_GROUP_LABELS_EN if en else GROUP_LABELS
    lines=['Service Fee table (recorded package rates):' if en else 'ตาราง Service Fee สำหรับทุกบริการ (ราคาต่อแพ็กเกจ):']
    for key,fee in SERVICE_FEES.items():
        capacity=('1 person' if fee['capacity']=='1 คน' else fee['capacity'].replace('คน','people')) if en else fee['capacity']
        lines.append(f"\\n{fee['label']} ({capacity}), {fee['minutes_per_session']} "+('minutes/session' if en else 'นาที/รอบ'))
        for group,price in fee['prices'].items():
            lines.append(f"•    {labels[group]}: {price:,} "+('THB' if en else 'บาท'))
    hits=make_source_hits([SERVICE_FEE_IMAGE_2026_ID,PC_SERVICE_FEE_LOCAL_UPDATE_20260727_ID])
    lines.append('PC rates include the local service fee update 2026-07-27.' if en else 'ราคา PC อ้างอิง local service fee update 2026-07-27')
    for url in dict.fromkeys(h.get('metadata',{}).get('source_url','') for h in hits):
        if url:lines.append(('Source: ' if en else 'แหล่งข้อมูล: ')+url)
    return StructuredToolResult('\\n'.join(lines),hits,'structured_service_fee_catalog',.98,{'catalog_only':True,'prices_unchanged':True})

def answer_closed_query_improvement(query,locale):''')
edit(files[3],"[('service_fee',answer_fee_alternatives),('reservation',_booking_resource),('no_answer',_media_policy_gap)]","[('service_fee',answer_fee_alternatives),('service_fee',_fee_catalog),('reservation',_booking_resource),('no_answer',_media_policy_gap)]")
with (r/'app_freeze_D.json').open('x',encoding='utf-8') as f:json.dump({str(v.relative_to(p)):hashlib.sha256(v.read_bytes()).hexdigest() for v in (p/'app').rglob('*.py')},f,indent=2)
print('Applied source-confirmed boundary and broad fee fixes; source/Gold untouched.')
