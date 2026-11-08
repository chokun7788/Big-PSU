from pathlib import Path
import ast,shutil
W=Path(__file__).parent;R=Path((W/'r37_report_path.txt').read_text().strip());P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
rel='app/session/context_resolver.py';p=P/rel;raw=p.read_bytes();s=raw.decode('utf-8-sig').replace('\r\n','\n')
old='''    specific_followup = (
        current_target.status == "absent"
        and bool(re.search(r"กฎ|กฏ|กติกา|\\brules?\\b", original, re.I))
        and detect_competition_facet(original) is not None
        and not re.search(r"ศูนย์|สตูดิโอ|\\b(?:studio|cent[er]{2})\\b|ไม่(?:เอา|ต้องการ)", original, re.I)
    )'''
new='''    def specific_rule_request(text):
        return (
            bool(re.search(r"กฎ|กฏ|กติกา|\\brules?\\b", text, re.I))
            and detect_competition_facet(text) is not None
            and not re.search(r"ศูนย์|สตูดิโอ|\\b(?:studio|center|centre)\\b|ไม่(?:เอา|ต้องการ)", text, re.I)
        )
    specific_followup = current_target.status == "absent" and specific_rule_request(original)'''
if s.count(old)!=1:raise RuntimeError('Scope patch differs')
s=s.replace(old,new,1)
s=s.replace('if user_target.status == "exact" or is_broad_rule_request(user_text) or is_more_rule_request(user_text):','if user_target.status == "exact" or is_broad_rule_request(user_text) or is_more_rule_request(user_text) or specific_rule_request(user_text):',1)
s=s.replace('not (is_broad_rule_request(user_text) or is_more_rule_request(user_text)):','not (is_broad_rule_request(user_text) or is_more_rule_request(user_text) or specific_rule_request(user_text)):',1)
ast.parse(s);snap=R/'before_scope_review'/rel;snap.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,snap)
p.write_text(s.replace('\n','\r\n') if b'\r\n' in raw else s,encoding='utf-8',newline='')
print('Specific rule follow-ups preserve the active game for the next turn.')
