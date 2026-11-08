import json,hashlib
from pathlib import Path
p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');r=Path(Path('r30_report_path.txt').read_text().strip())
for rel in ['app/pipeline/protected_intents.py','app/pipeline/competition_targets.py']:
    dest=r/'before_G5b'/rel;dest.parent.mkdir(parents=True,exist_ok=True)
    with dest.open('xb') as out:out.write((p/rel).read_bytes())
f=p/'app/pipeline/protected_intents.py';s=f.read_text(encoding='utf-8');old='asks_booking and (asks_weekly_period or added_policy_period)';assert s.count(old)==1;f.write_text(s.replace(old,'asks_booking and (asks_weekly_period or added_policy_period or generic_periods)'),encoding='utf-8',newline='\n')
f=p/'app/pipeline/competition_targets.py';s=f.read_text(encoding='utf-8');old='"roster", "substitute", "forfeit",';assert s.count(old)==1;f.write_text(s.replace(old,'"protest", "roster", "substitute", "forfeit",'),encoding='utf-8',newline='\n')
with (r/'app_freeze_G5b.json').open('x',encoding='utf-8') as out:json.dump({str(f.relative_to(p)).replace('\\','/'):hashlib.sha256(f.read_bytes()).hexdigest() for f in (p/'app').rglob('*.py')},out,indent=2)
