from pathlib import Path
P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
p=P/'app/pipeline/engine.py';s=p.read_text(encoding='utf-8')
old='def _english_compound_intent(part: str) -> str:\n';assert s.count(old)==1
new='''def _english_compound_intent(part: str) -> str:
    from app.pipeline.source_task_signals import fee_comparison_query, payment_method_query
    if fee_comparison_query(part):
        return "price"
    if re.search(r"\\b(?:pay|payment)\\b", part or "", re.I) and re.search(
        r"\\b(?:how\\s+many\\s+minutes?|deadline|timeout|within\\s+\\d+)\\b", part, re.I,
    ):
        return "booking_payment_deadline"
    if payment_method_query(part or ""):
        return "booking_payment_method"
'''
p.write_text(s.replace(old,new),encoding='utf-8')
p=P/'tests/test_source_task_boundaries_r34_20261003.py';s=p.read_text(encoding='utf-8')
s+='''    def test_english_payment_method_and_deadline_are_distinct_operations(self):
        q='How do I pay for a booking and how many minutes do I have to pay after booking?'
        parts=_split_multi_question(q)
        self.assertEqual(len(parts),2)
        self.assertIn('how many minutes',parts[1])
    def test_english_fee_comparison_and_booking_are_distinct_operations(self):
        q='Which is cheaper, PC or VR, and how do I book a session?'
        parts=_split_multi_question(q)
        self.assertEqual(len(parts),2)
        self.assertIn('PC or VR',parts[0])
        self.assertIn('book',parts[1])
'''
p.write_text(s,encoding='utf-8');print('Round I: English comparison/payment composition; two regression gates added')
