from pathlib import Path
import ast,shutil
W=Path(__file__).parent;R=Path((W/'r37_report_path.txt').read_text().strip());P=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
def patch(rel,old,new):
 p=P/rel;raw=p.read_bytes();s=raw.decode('utf-8-sig').replace('\r\n','\n')
 if s.count(old)!=1:raise RuntimeError('Patch differs '+rel+' '+old[:50])
 s=s.replace(old,new,1);ast.parse(s,filename=rel)
 snap=R/'before_C_review'/rel;snap.parent.mkdir(parents=True,exist_ok=True)
 if not snap.exists():shutil.copy2(p,snap)
 p.write_text(s.replace('\n','\r\n') if b'\r\n' in raw else s,encoding='utf-8',newline='')
patch('app/pipeline/competition_conversation_signals.py','|what|which|are|is|the|','|what|which|are|is|there|the|')
patch('app/pipeline/competition_conversation_signals.py',
 'def _generic_rule_text(query: str) -> str:',
 '''def competition_choice_text(query: str) -> str:
    q=_clean(query)
    q=re.sub(r'^(?:(?:แล้ว|ขอ|เลือก|เอา|เกม)\\s*)+|^(?:and|then|what about|for|the game)\\s+', '', q).strip()
    return re.sub(r'(?:ครับ+|ค่ะ+|คับ+|หน่อย+|ล่ะ|please|pls)\\s*$', '', q).strip(' ?!.,')

def _generic_rule_text(query: str) -> str:''')
patch('app/session/context_resolver.py',
 '        is_broad_rule_request, is_more_rule_request, is_rulebook_catalog_request,',
 '        is_broad_rule_request, is_more_rule_request, is_rulebook_catalog_request, competition_choice_text,')
patch('app/session/context_resolver.py',
 '    generic = is_broad_rule_request(original) or more',
 '''    generic = is_broad_rule_request(original) or more
    from app.pipeline.competition_taxonomy import detect_competition_facet
    specific_followup = (
        current_target.status == "absent"
        and bool(re.search(r"กฎ|กฏ|กติกา|\\brules?\\b", original, re.I))
        and detect_competition_facet(original) is not None
        and not re.search(r"ศูนย์|สตูดิโอ|\\b(?:studio|cent[er]{2})\\b|ไม่(?:เอา|ต้องการ)", original, re.I)
    )''')
patch('app/session/context_resolver.py',
 '''    choice = normalize_text(original).strip(" ?!.,؟")
    choice = re.sub(r"^(?:แล้ว|ขอ|เอา|เกม|and\\s+|what about\\s+|for\\s+|the game\\s+)", "", choice).strip()
    choice = re.sub(r"(?:ครับ|ค่ะ|คับ|หน่อย|please)$", "", choice).strip(" ?!.,")''',
 '    choice = competition_choice_text(normalize_text(original))')
patch('app/session/context_resolver.py',
 'or detect_game(original) or not generic:',
 'or detect_game(original) or not (generic or specific_followup):')
patch('app/session/context_resolver.py',
 '            recovered_choice = resolve_competition_targets("competition rules " + user_text)\n            if recovered_choice.status == "exact" and len(recovered_choice.explicit_mentions) == 1 and _alias_key(user_text) == _alias_key(recovered_choice.explicit_mentions[0]):',
 '            user_choice = competition_choice_text(normalize_text(user_text))\n            recovered_choice = resolve_competition_targets("competition rules " + user_choice)\n            if recovered_choice.status == "exact" and len(recovered_choice.explicit_mentions) == 1 and _alias_key(user_choice) == _alias_key(recovered_choice.explicit_mentions[0]):')
patch('app/session/context_resolver.py',
 '                    original, f"{prefix} {target.label}", True, target.label,',
 '                    original, f"{original if specific_followup else prefix} {target.label}", True, target.label,')
patch('app/pipeline/competition_overview.py',
 '            lines = substantive_lines(text)\n            section_title =',
 '''            lines = substantive_lines(text)
            identities = {comparison_text(str(value)) for value in (
                row.get('section_title'), row.get('tournament'),
                approved_localization(row, 'section_title') if locale == 'en' else '',
                approved_localization(row, 'tournament') if locale == 'en' else '',
            ) if value}
            lines = tuple(line for line in lines if comparison_text(line) not in identities)
            section_title =''')
print('Reviewed choice decorations, specific rule follow-ups and source headings.')
