from pathlib import Path
P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');R=Path(Path(__file__).with_name('r32_report_path.txt').read_text().strip());path=P/'app/pipeline/competition_facet_recovery.py'
with (R/'final12_facet_before_conjunction.py').open('xb') as f:f.write(path.read_bytes())
s=path.read_text(encoding='utf-8');anchor="        recovered=query[:edit.start]+edit.canonical+query[edit.end:]\n";assert anchor in s
block='''        connectors=[m for m in re.finditer(r'และ|กับ|\\band\\b',query,re.I) if edit.start<m.end() and m.start()<edit.end]
        if connectors:
            # A facet edit cannot consume the first letter of a conjunction.
            # Re-score the same facet with the conjunction as a hard boundary.
            boundary=connectors[0]
            if edit.start>=boundary.start():continue
            _,bounded=recover_names(query[:boundary.start()],registry,allow_same_target_overlap=True)
            same=[e for e in bounded if e.start==edit.start and e.game_id==edit.game_id and e.canonical==edit.canonical]
            if not same:continue
            edit=same[0]
'''
path.write_text(s.replace(anchor,block+anchor),encoding='utf-8')
path=P/'tests/test_partial_source_age_r32.py';s=path.read_text(encoding='utf-8');s+='''
    def test_typo_recovery_preserves_thai_conjunction(self):
        from app.core.intent_cue_recovery import recover_intent_cues
        from app.pipeline.competition_facet_recovery import recover_facet_cue
        for q in ['กติกา CS2 คุณสมบัตและอายุขั้นต่ำคืออะไร','กติกา CS2 คุณสมบัตกับอายุขั้นต่ำคืออะไร']:
            with self.subTest(q=q):
                x=recover_facet_cue(q);self.assertIsNotNone(x)
                recovered=x[0];self.assertIn('คุณสมบัติ',recovered)
                self.assertIn('และ' if 'และ' in q else 'กับ',recovered)
                self.assertEqual(lookup_competition_reply(recovered,'th').outcome,'partial')
''';s=s.replace('        from app.core.intent_cue_recovery import recover_intent_cues\n','');path.write_text(s,encoding='utf-8')
