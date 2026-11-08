from pathlib import Path
import ast,shutil
W=Path(__file__).parent;R=Path((W/'r37_report_path.txt').read_text().strip());P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
p=P/'app/pipeline/competition_overview.py';raw=p.read_bytes();s=raw.decode('utf-8-sig').replace('\r\n','\n')
old='''    clauses = {}
    primary_pause_clauses = {}'''
new='''    # Bilingual documents may include a second set of English source sections
    # after the Thai rulebook. Use one primary set for both locales, translating
    # it through the existing localization registry for English. Parallel source
    # versions are not new rules when the user asks for additional clauses.
    primary_rows = [row for row in rows if any(re.search(r'[\\u0e00-\\u0e7f]', line)
                    for line in substantive_lines(str(row.get('text') or '')))]
    if primary_rows:
        rows = primary_rows
    clauses = {}
    primary_pause_clauses = {}'''
assert s.count(old)==1;s=s.replace(old,new,1)
old="            lines = substantive_lines(text)\n            identities ="
new="""            lines = substantive_lines(text)
            if locale != 'en' and primary_rows:
                lines = tuple(line for line in lines if re.search(r'[\\u0e00-\\u0e7f]', line))
            identities ="""
assert s.count(old)==1;s=s.replace(old,new,1);ast.parse(s)
snap=R/'before_parallel_source_review'/'app/pipeline/competition_overview.py';snap.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,snap)
p.write_text(s.replace('\n','\r\n') if b'\r\n' in raw else s,encoding='utf-8',newline='')
print('Excluded parallel language sections from additional-rule summaries.')
