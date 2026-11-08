from pathlib import Path
P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
p=P/'app/core/task_frame_recovery.py';s=p.read_text(encoding='utf-8')
old="อย่า(?!ง)|เกิน|กี่นาที";assert s.count(old)==1
p.write_text(s.replace(old,"อย่า(?!ง)|เกิน|ครับ|ค่ะ|คะ(?=\\s|$)|กี่นาที"),encoding='utf-8')
p=P/'app/pipeline/source_task_signals.py';s=p.read_text(encoding='utf-8')
old='def speech_rule_query(query: str) -> bool:\n';assert s.count(old)==1
new='''def speech_rule_query(query: str) -> bool:
    # Topic vocabulary inside a person's name is not a conduct question.
    if re.search(r'ตำแหน่ง|คือใคร|\\b(?:position|role|who|Mr|Ms|Mrs|Dr)\\b', query, re.I):
        return False
'''
p.write_text(s.replace(old,new),encoding='utf-8')
p=P/'tests/test_source_task_boundaries_r34_20261003.py';s=p.read_text(encoding='utf-8')
s+='''    def test_conduct_topic_in_a_person_name_does_not_steal_identity(self):
        from app.pipeline.source_task_signals import speech_rule_query
        self.assertFalse(speech_rule_query('What position does Mr. Insults hold at the studio?'))
        self.assertFalse(speech_rule_query('ตำแหน่งของนายเสียดสีในศูนย์คืออะไร'))
        self.assertTrue(speech_rule_query('Are insults permitted in the studio?'))
'''
p.write_text(s,encoding='utf-8');print('Round H: preserve polite suffix boundaries and personal-name intent')
