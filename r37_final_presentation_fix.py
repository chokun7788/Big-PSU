from pathlib import Path
import ast,shutil
W=Path(__file__).parent;R=Path((W/'r37_report_path.txt').read_text().strip());P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
p=P/'app/pipeline/competition_overview.py';raw=p.read_bytes();s=raw.decode('utf-8-sig').replace('\r\n','\n')
old="        body = re.sub(r'^\\d+(?:\\.\\d+)*[.)]?\\s+', '', line)"
new=old+"""
        if re.fullmatch(r'(?:การย้อนรอบ(?:\\s*\\(Round Rollback\\))?|Round Rollback)', body, re.I):
            continue"""
assert s.count(old)==1;s=s.replace(old,new,1);ast.parse(s)
snap=R/'before_short_heading_review'/'app/pipeline/competition_overview.py';snap.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,snap)
p.write_text(s.replace('\n','\r\n') if b'\r\n' in raw else s,encoding='utf-8',newline='')
print('Excluded standalone rollback headings; full rollback requirements retained.')
