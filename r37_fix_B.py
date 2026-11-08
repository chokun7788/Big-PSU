from pathlib import Path
import ast,shutil,json
W=Path(__file__).parent;R=Path((W/'r37_report_path.txt').read_text().strip());P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
def patch(rel,old,new):
 p=P/rel;raw=p.read_bytes();s=raw.decode('utf-8-sig').replace('\r\n','\n')
 if s.count(old)!=1:raise RuntimeError('Patch location differs: '+rel+' '+old[:60])
 s=s.replace(old,new,1);ast.parse(s,filename=rel)
 snap=R/'before_B'/rel;snap.parent.mkdir(parents=True,exist_ok=True)
 if not snap.exists():shutil.copy2(p,snap)
 p.write_text(s.replace('\n','\r\n') if b'\r\n' in raw else s,encoding='utf-8',newline='')
patch('app/pipeline/competition_conversation_signals.py',"{'rules','rule','runes','rues','ruse'}","{'rules','rule','roles','runes','rues','ruse'}")
patch('app/session/context_resolver.py',
 '        prior_target = resolve_competition_targets(resolved_text)\n        if reply.get("route_category")',
 '''        prior_target = resolve_competition_targets(resolved_text)
        if user_target.status == "absent" and reply.get("route_category") == "competition_rules":
            recovered_choice = resolve_competition_targets("competition rules " + user_text)
            if recovered_choice.status == "exact" and len(recovered_choice.explicit_mentions) == 1 and _alias_key(user_text) == _alias_key(recovered_choice.explicit_mentions[0]):
                user_target = recovered_choice
        if reply.get("route_category")''')
patch('app/pipeline/competition_overview.py',
 "        if len(line) < 12 or not is_rule_clause(line):\n            continue",
 '''        if len(line) < 12 or not is_rule_clause(line):
            continue
        # A tournament year alone cannot turn an event title into a rule.
        if not is_rule_clause(re.sub(r'\\b20\\d{2}\\b', '', line)):
            continue''')
patch('app/pipeline/competition_overview.py',
 '    clauses = {}\n    excluded_count = 0',
 '    clauses = {}\n    primary_pause_clauses = {}\n    excluded_count = 0')
patch('app/pipeline/competition_overview.py',
 "            lines = substantive_lines(text)\n            if more:",
 '''            lines = substantive_lines(text)
            section_title = str(row.get('section_title') or '')
            if requested_pause_kind(section_title):
                # Chunks can contain a second heading after the pause rules.
                # Bind the primary pause label only to clauses before that
                # heading; remaining bug/rollback rules may appear as extras.
                scoped = []
                for line in source_clause_lines(text)[1:]:
                    if not is_rule_clause(line):
                        if scoped:
                            break
                        continue
                    scoped.append(line)
                primary_pause_clauses[str(row['id'])] = substantive_lines('\\n'.join(scoped))
            if more:''')
patch('app/pipeline/competition_overview.py',
 "                return clauses[row['id']]\n            return tuple(line",
 "                return tuple(line for line in clauses[row['id']] if line in primary_pause_clauses.get(row['id'], clauses[row['id']]))\n            return tuple(line")
print('Applied B: corrected-target history, real-word guard, metadata and pause-section boundary.')
