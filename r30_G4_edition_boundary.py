from pathlib import Path
import json,hashlib
p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');r=Path(Path('r30_report_path.txt').read_text().strip())
def edit(rel,old,new):
    f=p/rel;d=r/'before_G4b'/rel;d.parent.mkdir(parents=True,exist_ok=True)
    with d.open('xb') as out:out.write(f.read_bytes())
    s=f.read_text(encoding='utf-8');assert s.count(old)==1;(f).write_text(s.replace(old,new),encoding='utf-8',newline='\n')
edit('app/pipeline/competition_targets.py',r"r'(?![a-z0-9])(?!\s*(?:ภาค|เวอร์ชัน|version)?\s*\d)(?!\s+[ivx]+\b)'",r"r'(?![a-z0-9])(?!\s*(?:ภาค|เวอร์ชัน|v(?:ersion)?)?\s*(?:\d+|[ivx]+\b))'")
f=p/'app/pipeline/competition_targets.py';s=f.read_text(encoding='utf-8')
old='        return CompetitionTargetResolution("exact", targets, mentions, "registered_competition_alias")'
assert s.count(old)==1
new='        direct = any(_contains_alias(query, alias) for alias in targets[0].aliases)\n        return CompetitionTargetResolution("exact", targets, mentions, "registered_competition_alias" if direct else "unique_registered_rulebook_edition")'
f.write_text(s.replace(old,new),encoding='utf-8',newline='\n')
edit('app/pipeline/competition_detail.py','    answer = render_rule_reply(selected[0], selected[1:], used[0], locale)', '''    first = selected[0]
    if target.reason == 'unique_registered_rulebook_edition':
        label = target.targets[0].label
        first = (f'In the recorded {label} rulebook: ' if locale == 'en' else f'ตามเอกสารกติกา {label} ที่มี: ') + first
    answer = render_rule_reply(first, selected[1:], used[0], locale)''')
f=p/'tests/test_r30_remaining_source_contracts.py';s=f.read_text(encoding='utf-8');s=s.replace("'Tekken VII tournament rules'","'Tekken VII tournament rules','Tekken v7 tournament rules','Tekken version VII tournament rules'")
s=s.replace("self.assertIn('จำนวนรอบต่อเกม (Round): 3',a)","self.assertIn('จำนวนรอบต่อเกม (Round): 3',a)\n        self.assertIn('Tekken 8',a.splitlines()[0])")
f.write_text(s,encoding='utf-8',newline='\n')
manifest={str(f.relative_to(p)).replace('\\','/'):hashlib.sha256(f.read_bytes()).hexdigest() for f in (p/'app').rglob('*.py')}
with (r/'app_freeze_G4b.json').open('x',encoding='utf-8') as out:json.dump(manifest,out,indent=2)
print(json.dumps({'freeze':'G4b','changes':'explicit edition boundaries and rulebook-qualified inferred edition reply'}))
