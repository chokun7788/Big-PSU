from pathlib import Path
BASE=Path(__file__).resolve().parent;OUT=Path((BASE/'r56_current_path.txt').read_text());ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
assert not (OUT/'EDIT2_DONE').exists()
p=ROOT/'app/pipeline/user_service_facts.py';t=p.read_text(encoding='utf-8');old='คนจอง.*คนเล่น|คนเล่น.*คนจอง|จองแทน'
assert old in t;t=t.replace(old,'คนจอง.*คนเล่น|คนเล่น.*(?:คนจอง|ไม่มีชื่อ)|จองชื่อ.*แต่.*คนเล่น|จองแทน',1);p.write_text(t,encoding='utf-8')
p=ROOT/'tests/test_remaining_repairs_r56.py';t=p.read_text(encoding='utf-8');needle='    def test_mixed_language_logout_unknown(self):'
t=t.replace(needle,"    def test_player_not_listed_natural_order(self):\n        r=answer_user_service_facts('ผมจองชื่อผมแต่คนเล่นไม่มีชื่อในรายการได้ไหม')\n        self.assertIn('player_identity',r['trace'][0].metadata['claim_ids'])\n"+needle,1);p.write_text(t,encoding='utf-8')
(OUT/'EDIT2_DONE').write_text('named player scope in natural word order',encoding='utf-8')
print('player scope refined; owner data unchanged')
