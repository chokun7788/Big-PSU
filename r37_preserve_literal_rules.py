from pathlib import Path
import ast,shutil
W=Path(__file__).parent;R=Path((W/'r37_report_path.txt').read_text().strip());P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
p=P/'app/pipeline/competition_overview.py';raw=p.read_bytes();s=raw.decode('utf-8-sig').replace('\r\n','\n')
old="        if not is_rule_clause(re.sub(r'\\b20\\d{2}\\b', '', line)):\n            continue"
new="        body = re.sub(r'^\\d+(?:\\.\\d+)*[.)]?\\s+', '', line)\n        if not is_rule_clause(re.sub(r'\\b20\\d{2}\\b', '', body)):\n            continue"
assert s.count(old)==1;s=s.replace(old,new,1)
old="            lines = tuple(line for line in lines if comparison_text(line) not in identities)"
new="""            # Some source sections consist of a complete numbered rule in
            # their title field. Retain a title that contains an actual rule;
            # remove only heading labels without substantive policy evidence.
            lines = tuple(line for line in lines if comparison_text(line) not in identities
                          or is_rule_clause(re.sub(r'^\\d+(?:\\.\\d+)*[.)]?\\s+', '', line)))"""
assert s.count(old)==1;s=s.replace(old,new,1)
old="                for line in source_clause_lines(text)[1:]:"
new="""                raw_lines = source_clause_lines(text)
                # A one-line source section may itself be the complete rule.
                # Do not drop its first line merely because it has a title.
                first_is_heading = bool(raw_lines and comparison_text(raw_lines[0]) in identities
                                        and not is_rule_clause(re.sub(r'^\\d+(?:\\.\\d+)*[.)]?\\s+', '', raw_lines[0])))
                for line in raw_lines[1:] if first_is_heading else raw_lines:"""
assert s.count(old)==1;s=s.replace(old,new,1);ast.parse(s)
snap=R/'before_literal_rule_review'/'app/pipeline/competition_overview.py';snap.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,snap)
p.write_text(s.replace('\n','\r\n') if b'\r\n' in raw else s,encoding='utf-8',newline='')
print('Preserved complete rules stored as titles and one-line pause sections.')
