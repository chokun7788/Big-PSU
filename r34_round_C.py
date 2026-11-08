from pathlib import Path
P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
def edit(rel,old,new):
 p=P/rel;s=p.read_text(encoding='utf-8');assert s.count(old)==1,(rel,s.count(old));p.write_text(s.replace(old,new),encoding='utf-8')
p=P/'app/pipeline/source_task_signals.py'
p.write_text(p.read_text(encoding='utf-8')+'''
def speech_rule_query(query: str) -> bool:
    thai = re.search(r'คำพูด(?:ไม่)?เหมาะสม|ดูหมิ่น|เสียดสี|เสียงดังเกิน', query)
    english = re.search(r'\\b(?:offensive\\s+language|inappropriate\\s+speech|insult(?:s|ing)?|mock\\s+(?:other\\s+)?people)\\b', query, re.I)
    context = re.search(r'ศูนย์|คำพูด|กฎ|ข้อห้าม|\\b(?:studio|rules?|allowed|may|can\\s+i)\\b', query, re.I)
    return bool((thai or english) and context)
''',encoding='utf-8')
edit('app/pipeline/protected_intents.py','    if _has(q, "คำพูดไม่เหมาะสม", "พูดจาดูหมิ่น", "เสียงดังเกิน") or bool(re.search(r"\\b(?:offensive\\s+language|insulting\\s+speech)\\b", q)):', '    from app.pipeline.source_task_signals import speech_rule_query\n    if speech_rule_query(q):')
edit('app/pipeline/question_frame.py','    # A zone/genre catalogue question asks for multiple games, even when the','    from app.pipeline.source_task_signals import speech_rule_query\n    if speech_rule_query(question):\n        return "studio_rule_lookup", "rules", 0.98\n    # A zone/genre catalogue question asks for multiple games, even when the')
# The corrupt fragment is one transposition. An intact affirmative fragment
# differs by three inserted negation characters, and is never a candidate.
edit('app/core/intent_cue_recovery.py','    from app.pipeline.competition_facet_recovery import recover_facet_cue', '''    from app.pipeline.competition_targets import looks_like_competition_rule_query
    if not looks_like_competition_rule_query(text) and 'คำพูดไม่' not in text:
        candidates = []
        for match in re.finditer(r'คำพู[\\u0e00-\\u0e7f]{3,6}(?=เหมาะสม)', text):
            observed = match.group()
            if osa_distance(observed, 'คำพูดไม่') == 1:
                candidates.append(match)
        if len(candidates) == 1:
            match = candidates[0]
            return CueRecovery(text, text[:match.start()]+'คำพูดไม่'+text[match.end():],
                               match.group(), 'คำพูดไม่', match.start(), 1,
                               'unique speech-fragment transposition before exact appropriateness topic')
    from app.pipeline.competition_facet_recovery import recover_facet_cue''')
edit('app/core/task_frame_recovery.py',"        if near('studio'):\n", "        if near('studio') and re.search(r'\\b(?:language|speech)\\b',low):targets.append('offensive')\n        if near('studio'):\n")
print('Round C source-backed speech topic and one-edit fragment recovery saved')
