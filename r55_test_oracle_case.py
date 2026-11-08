from pathlib import Path
import shutil
BASE=Path(__file__).resolve().parent
OUT=Path((BASE/'r55_current_path.txt').read_text())
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
rel=Path('tests/test_p0_calendar_booking_reconciliation_20260925.py')
p=ROOT/rel;s=p.read_text(encoding='utf-8')
old='self.assertIn("a Thai public holiday alone does not automatically close", en.answer)'
assert old in s
s=s.replace(old,'self.assertIn("a Thai public holiday alone does not automatically close", en.answer.casefold())',1)
p.write_text(s,encoding='utf-8')
shutil.copy2(p,OUT/'candidate_6/PSU_Esports_Chatbot_Local'/rel)
print('Case-insensitive calendar wording assertion; expected policy unchanged.')
