from pathlib import Path
P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');p=P/'app/pipeline/competition_facet_recovery.py';s=p.read_text(encoding='utf-8');s=s.replace("('rulebook_identity',('event information',))", "('rulebook_identity',('event information','ใช้กับการแข่งขันไหน'))")
a='    for edit in edits:\n';assert a in s;s=s.replace(a,'''    for edit in edits:
        if re.search(r'[:;?!.,]',edit.original):continue
        # Preserve complete threshold words even when the candidate ends
        # before their last Thai letter. Otherwise หยุดเกิน becomes หยุดเกมน.
        if any(edit.start<m.end() and m.start()<edit.end for m in re.finditer(r'เกิน|การแข่งขันไหน',query)):continue
''',1);p.write_text(s,encoding='utf-8')
p=P/'tests/test_all_remaining_r32_20261002.py';s=p.read_text(encoding='utf-8');s+='''
    def test_recovery_preserves_valid_threshold_identity_and_punctuation(self):
        for q in ['กติกา RoV หยุดเกิน 10 นาทีกรรมการทำอย่างไร','กติกา Tekken 8 ใช้กับการแข่งขันไหน','Please check: I am preparing for a Counter Strike 2 match. What is the policy for the competition format? please.']:
            with self.subTest(q=q):self.assertEqual(recover_intent_cues(q),q)
''';p.write_text(s,encoding='utf-8');print('protected valid quantity terms, identity questions and punctuation boundaries')
