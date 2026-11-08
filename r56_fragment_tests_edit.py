from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r56_current_path.txt').read_text());ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
p=ROOT/'app/pipeline/conversation_rules.py';t=p.read_text(encoding='utf-8');t=t.replace("'source_policy_complete':not bool(source_gap_ids)","'known_source_fragment_gaps':bool(source_gap_ids), 'source_policy_complete':False if source_gap_ids else None",1);p.write_text(t,encoding='utf-8')
p=ROOT/'tests/test_remaining_repairs_r56.py';t=p.read_text(encoding='utf-8');needle='    def test_capacity_idempotency_and_no_ambiguous_replay(self):'
addition='''    def test_rov_fragment_source_hash_and_no_fake_policy_completion(self):
        import copy
        from app.pipeline.rulebook_source_fragments import fragment_translation,is_recorded_fragment
        from app.pipeline.conversation_rules import rulebook_manifest,build_full_rule_answer
        from app.pipeline.competition_targets import resolve_competition_targets
        rows,_=rulebook_manifest(resolve_competition_targets('rules RoV').targets[0])
        row=next(r for r in rows if is_recorded_fragment(r))
        text=fragment_translation(row);self.assertIn('source stops here',text)
        self.assertIn('6.1.3.1.',text);self.assertIn('both teams',text)
        changed=copy.deepcopy(row);changed['text']+='different source'
        self.assertIsNone(fragment_translation(changed))
        for locale in ('th','en'):
            history=[];seen=set()
            for page in range(5):
                q='Show all recorded competition rules for RoV.' if not page else 'RoV continue with the remaining rules.'
                r=build_full_rule_answer(q,locale,recent_history=history);cov=r['trace'][-1].metadata
                self.assertFalse(cov['source_policy_complete']);self.assertFalse(cov['owner_confirmed'])
                self.assertEqual(cov['outcome'],'answered_partial')
                self.assertNotIn('english_localization_incomplete',r['validation'].warnings)
                self.assertIn('rulebook_source_incomplete',r['validation'].warnings)
                self.assertFalse(seen & set(cov['returned_ids']));seen.update(cov['returned_ids'])
                history.append(dict(role='assistant',route_category='competition_rules',rule_coverage=cov,delivery_status='client_acknowledged'))
                if seen==set(cov['expected_ids']):break
            self.assertEqual(len(seen),12)
'''
assert needle in t;t=t.replace(needle,addition+needle,1);p.write_text(t,encoding='utf-8');print('fragment source-gap regression added')
