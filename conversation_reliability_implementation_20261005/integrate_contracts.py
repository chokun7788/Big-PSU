from pathlib import Path
import shutil
ROOT=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
HERE=Path(__file__).resolve().parent
def edit(rel,old,new):
    p=ROOT/rel; text=p.read_text(encoding='utf-8-sig')
    assert old in text,rel
    b=HERE/'before'/rel
    if not b.exists():
        b.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,b)
    p.write_text(text.replace(old,new,1),encoding='utf-8',newline='')

edit('app/pipeline/engine.py', '        if competition_signal and competition_target.status == "exact":\n            from app.pipeline.competition_source_gaps', '''        if competition_signal and competition_target.status == "exact":
            from app.pipeline.conversation_rules import build_full_rule_answer
            full = build_full_rule_answer(pre.clean_query, locale.effective if locale else 'th', recent_history=recent_history)
            if full:
                trace.extend(full['trace'])
                return self._build_result(full['answer'], full['hits'], started, full['mode'], .98,
                                          full['route'], entities, full['validation'], trace)
        if competition_signal and competition_target.status == "exact":
            from app.pipeline.competition_source_gaps''')
edit('app/web_api/server.py', "                actual_plan = contract.get('request_plan') or request_plan", "                actual_plan = contract.get('request_plan') or request_plan\n                response['rule_coverage'] = next((t.metadata for t in reversed(result.trace) if t.stage == 'competition_full_coverage'), None)")
edit('app/session/context_resolver.py', '    generic = is_broad_rule_request(original) or more', '''    from app.pipeline.conversation_rules import wants_full_rules
    full_scope = wants_full_rules(original) and not re.search(r'ราคา|จอง|เกมอะไร|อุปกรณ์|ปุ่ม|\\b(?:price|book|games?|equipment|controls?)\\b', original, re.I)
    generic = is_broad_rule_request(original) or more or full_scope''')
edit('app/session/context_resolver.py', '    prefix = ("Additional competition rules for" if more else "Competition rules for") if english else ("กติกาการแข่งขันเพิ่มเติม" if more else "กติกาการแข่งขัน")', '''    prefix = ("All detailed competition rules for" if full_scope else "Additional competition rules for" if more else "Competition rules for") if english else ("กติกาการแข่งขันทั้งหมด" if full_scope else "กติกาการแข่งขันเพิ่มเติม" if more else "กติกาการแข่งขัน")''')
edit('app/pipeline/competition_conversation_signals.py', '|ทั้งหมด|ไหม|', '|ทั้งหมด|ทุกหัวข้อ|ทุกข้อ|ทุกส่วน|รายละเอียด|ครบ|ไหม|')
edit('app/pipeline/competition_conversation_signals.py', '|all|overview|', '|all|full|complete|detailed|details|sections|topics|overview|')
edit('app/pipeline/competition_overview.py', "            if item.get('contextEligible') is False or item.get('context_eligible') is False:\n                continue", "            if item.get('contextEligible') is False or item.get('context_eligible') is False:\n                continue\n            if item.get('delivery_status') in {'prepared', 'server_written', 'uncertain'}:\n                continue")
edit('app/pipeline/engine.py', '            answer = format_no_answer(route.category, locale.effective)', '''            for item in trace:
                if item.stage in {'conversation_contract', 'competition_full_coverage'}:
                    item.metadata['outcome'] = 'schema_rejected'
                    item.metadata['rejected_errors'] = rejected_errors
                    item.metadata['returned_ids'] = []
                    item.metadata['covered_ids'] = []
            answer = format_no_answer(route.category, locale.effective)''')
print('Integrated coverage, safe continuation and semantic outcomes.')
