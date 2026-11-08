from pathlib import Path
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
def edit(name,old,new):
    p=ROOT/name;s=p.read_text(encoding='utf-8');assert old in s,(name,old[:80]);p.write_text(s.replace(old,new,1),encoding='utf-8')
edit('app/session/conversation_plan.py',r'จอง(?:ยังไง|อย่างไร)',r'จอง(?:เครื่อง|อุปกรณ์)?(?:ยังไง|อย่างไร)')
edit('app/pipeline/service_query_completion.py',r'เปิด|ปิด|maintenance|opening hours',r'เปิด|ปิด|maintenance|opening hours|\b(?:open|close|opens|closes)\b')
edit('app/pipeline/service_query_completion.py',"    if not 2<=len(parts)<=3:return [question]", """    if len(parts)==1 and re.search(r'ชำระเงิน(?:ยังไง|อย่างไร).*จ่ายเงินสด',question):
        parts=[p.strip() for p in re.split(r'(?=จ่ายเงินสด)',question,maxsplit=1)]
    if not 2<=len(parts)<=3:return [question]""")
edit('app/pipeline/service_query_completion.py',"    if en and re.search(r'\\b(?:shoot|reload)\\b',q):", """    if en and re.search(r'\\b(?:when|what|which|opening|business|service)\\b.*\\b(?:open|opens|hours|schedule)\\b',q) and not re.search(r'\\b(?:today|tomorrow|now|available|free|price|cost)\\b|\\d{4}-\\d{2}-\\d{2}',q):
        from app.pipeline.bilingual_english import _answer_schedule
        value=_answer_schedule(q,EntityBundle())
        if value:return _result(value.answer,value.hits,'schedule','schedule_query',dict(basis='regular_service_calendar',not_live=True))
    if en and re.search(r'\\b(?:shoot|reload)\\b',q):""")
edit('tests/test_service_repairs_r55.py',"('ชำระเงินยังไง จ่ายเงินสดได้ไหม',1)","('ชำระเงินยังไง จ่ายเงินสดได้ไหม',2)")
edit('tests/test_service_repairs_r55.py',"resource_name='VR #1 Morning'","resource_name='VR Station #1 Morning'")
print('loop2 unit findings fixed')
