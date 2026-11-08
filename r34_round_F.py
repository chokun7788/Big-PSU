from pathlib import Path
P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
def edit(rel,old,new):
 p=P/rel;s=p.read_text(encoding='utf-8');assert s.count(old)==1,(rel,s.count(old));p.write_text(s.replace(old,new),encoding='utf-8')
edit('app/pipeline/engine.py','    boundary_parts = _split_boundary_compound_question(clean)', '''    from app.pipeline.source_task_signals import fee_comparison_query
    if fee_comparison_query(clean) and not re.search(
        r'จอง|เช็กอิน|เช็คอิน|ยกเลิก|เปิดกี่|ปิดกี่|มีเกม|ปุ่ม|\\b(?:book|booking|reserve|reservation|check.in|cancel|games?|controls?|payment|open|close)\\b', clean, re.I,
    ):
        # Two services joined by "and/และ" are operands of one price operation.
        # A separate booking/control/schedule operation must still be split.
        return [clean]
    boundary_parts = _split_boundary_compound_question(clean)''')
edit('app/core/task_frame_recovery.py','    if re.search(r"จ่าย|ชำระ",text) and re.search(r"ยังไง|ยงไง|อย่างไร",text):','    if re.search(r"จ่าย|ชำระ",text):')
edit('app/core/task_frame_recovery.py','    if has_resource or has_game:\n', '    if "วิธี" in text and "เงิน" in text:\n        frames += [("วิธีชำระเงิน",1),("วิธีจ่ายเงิน",1)]\n    if has_resource or has_game:\n')
edit('app/pipeline/source_task_signals.py',r'mock\s+(?:other\s+)?people',r'mock(?:ing)?\s+(?:other\s+)?people')
edit('app/core/task_frame_recovery.py',"        if near('studio') and re.search(r'\\b(?:language|speech)\\b',low):targets.append('offensive')", "        if near('studio') and re.search(r'\\b(?:language|speech)\\b',low):targets.extend(('offensive','insulting'))\n        if near('studio') and re.search(r'\\b(?:allowed|permitted|prohibit)\\b',low):targets.append('insults')")
edit('app/core/intent_cue_recovery.py',"            ('protest', r'\\b(?:coach|captain|file|submit|submits|deadline|minutes)\\b'),", "            ('players', r'\\b(?:per\\s+team|team\\s+size)\\b'),\n            ('protest', r'\\b(?:coach|captain|file|submit|submits|deadline|minutes)\\b'),")
print('Round F fixes 8 new source-verified wording/mutation failures')
