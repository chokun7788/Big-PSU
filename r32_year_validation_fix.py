from pathlib import Path
import json
P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');R=Path(Path(__file__).with_name('r32_report_path.txt').read_text().strip())
for rel in ['app/pipeline/answer_contracts.py','app/pipeline/competition_source_gaps.py','tests/test_competition_recorded_year_r32.py']:
 with (R/('candidate8_before_'+rel.replace('/','_'))).open('xb') as f:f.write((P/rel).read_bytes())
path=P/'app/pipeline/answer_contracts.py';s=path.read_text(encoding='utf-8');anchor='    if "structured_service_game_availability_no_match" in mode_key:\n        types.add("no_answer")\n';assert anchor in s
s=s.replace(anchor,anchor+'    if mode_key == "competition_rule_detail_no_answer":\n        types.add("no_answer")\n');path.write_text(s,encoding='utf-8')
path=P/'app/pipeline/competition_source_gaps.py';s=path.read_text(encoding='utf-8');s=s.replace("('requested_rulebook_year_not_in_source',))","('requested_rulebook_year_not_in_source', 'event_year_not_covered'))");path.write_text(s,encoding='utf-8')
path=P/'tests/test_competition_recorded_year_r32.py';s=path.read_text(encoding='utf-8');s+='''
    def test_year_abstention_survives_answer_contract(self):
        from app.pipeline.answer_contracts import validate_answer_contract
        from app.pipeline.schemas import PipelineRoute
        for q,l in [('CS2 tournament 2027 eligibility and roster','en'),('กติกา RoV ปี 2026 จำนวนผู้เล่นต่อทีม','th')]:
            with self.subTest(q=q):
                a=lookup_competition_reply(q,l)
                route=PipelineRoute('competition_rules','competition_rules_lookup',0.97,'fact','medium','test')
                x=validate_answer_contract(q,a.answer,route,hits=[],mode='pipeline:competition_rule_detail_no_answer')
                self.assertTrue(x.ok,x.errors);self.assertIn('no_answer',x.answer_types)
'''
# Current function requires a QuestionFrame rather than the raw query.
import sys;sys.path.insert(0,str(P))
import inspect
from app.pipeline.answer_contracts import validate_answer_contract
print(inspect.signature(validate_answer_contract))
s=s.replace("x=validate_answer_contract(q,a.answer,route,hits=[],mode='pipeline:competition_rule_detail_no_answer')","from app.pipeline.question_frame import build_question_frame\n                x=validate_answer_contract(build_question_frame(q,route),a.answer,route,hits=[],mode='pipeline:competition_rule_detail_no_answer')")
path.write_text(s,encoding='utf-8')
