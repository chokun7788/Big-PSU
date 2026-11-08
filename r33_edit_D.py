from pathlib import Path
P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
f=P/'app/core/task_frame_recovery.py';s=f.read_text(encoding='utf-8');needle='    has_game=game.is_exact';assert s.count(needle)==1
s=s.replace(needle,needle+'''
    if has_game and game.top_candidate is not None and re.search(r'ไหม|มั้ย',text):
        alias=game.top_candidate.matched_alias
        found=re.search(re.escape(alias),text,re.I) if alias else None
        if found:
            prefix=text[:found.start()]
            slot=re.search(r'(?:^|\\s)([\\u0e00-\\u0e7f]{1,3})\\s*$',prefix)
            if slot and slot.group(1) not in {'มี','มา','ไป','ไม่','ดู','ขอ'} and osa_distance(slot.group(1),'มี')==1:
                return slot.start(1),slot.group(1),'มี',1,'existence verb before exact catalog title and question particle'
''')
f.write_text(s,encoding='utf-8')
f=P/'app/pipeline/closed_query_improvements.py';s=f.read_text(encoding='utf-8');needle='def answer_closed_query_improvement(query,locale):';assert s.count(needle)==1
extra='''def _non_catalog_request(query,locale):
    en=locale=='en'
    if re.search(r'หน่วยงาน\\s*ดำเนินการ|หน่วยงานที่ดำเนินการ',query):
        # Use the existing recorded operator rule, rather than member names.
        from app.runtime.fast_answer import fast_answer_question
        result=fast_answer_question('ใครดำเนินการศูนย์',experimental_allow_llm=False)
        if result is not None and 'วิทยาลัยการคอมพิวเตอร์' in result.answer:
            return StructuredToolResult(result.answer,result.hits,'studio_operator_source',.98,{'operator_rule':True})
    personal=bool(re.search(r'คีย์บอร์ด.{0,6}(?:ตัวเอง|ดัวเอง|ส่วนตัว)|เมาส์.{0,6}(?:ตัวเอง|ส่วนตัว)|\\b(?:my|own|personal)\\s+(?:keyboard|mouse|controller)\\b',query,re.I))
    permission=bool(re.search(r'มาใช้|นำ|เอา|ได้ไหม|\\b(?:bring|use|allowed)\\b',query,re.I))
    if personal and permission:
        answer=('I could not find a verified general studio policy allowing replacement of the studio keyboard, mouse or controller with a personal peripheral. Please ask staff whether your device is allowed and how it must be connected.' if en else 'ยังไม่พบนโยบายการใช้บริการทั่วไปที่ยืนยันได้ว่านำคีย์บอร์ด เมาส์ หรือคอนโทรลเลอร์ส่วนตัวมาสลับกับชุดของศูนย์ได้ครับ กรุณาถามเจ้าหน้าที่ว่าอุปกรณ์ของคุณใช้ได้หรือไม่ และต้องเชื่อมต่ออย่างไร')
        return StructuredToolResult(answer,[],'personal_peripheral_policy_no_answer',.97,{'missing_general_policy':True,'competition_policy_not_reused':True})
    if re.search(r'ส่งเครื่อง.*ไปบ้าน|\\b(?:deliver|delivery|ship)\\b.*\\b(?:home|house)\\b',query,re.I):
        answer=('I could not find verified information that the studio delivers gaming equipment to users at home. Please ask the studio directly about this service.' if en else 'ยังไม่พบข้อมูลที่ยืนยันได้ว่าศูนย์มีบริการส่งเครื่องเกมไปที่บ้านครับ กรุณาสอบถามศูนย์โดยตรงเกี่ยวกับบริการนี้')
        return StructuredToolResult(answer,[],'equipment_home_delivery_no_answer',.98,{'missing_service':'home_equipment_delivery'})
    return None

'''
# Avoid a speculative signature/call for the operator; use the existing rule
# through the structured source catalog after checking its function below.
extra=extra[:extra.index("    if re.search(r'หน่วยงาน")]+extra[extra.index('    personal='):]
s=s.replace(needle,extra+needle).replace("[('service_fee',_fee_comparison)","[('no_answer',_non_catalog_request),('service_fee',_fee_comparison)")
f.write_text(s,encoding='utf-8')
f=Path(__file__).with_name('r33_unit_all.py');s=f.read_text(encoding='utf-8').replace('work/r30_test_dependencies','work/r33_test_dependencies');f.write_text(s,encoding='utf-8')
print('D: exact game existence frame, explicit service policy gaps; unit dependency path repaired')
