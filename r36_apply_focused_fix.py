from pathlib import Path
import ast, hashlib, json, shutil, subprocess
from datetime import datetime

ROOT = Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
WORK = Path(__file__).parent
REPORT = WORK / ('r36_focused_conversation_' + datetime.now().strftime('%Y%m%d_%H%M%S'))
REPORT.mkdir()
(WORK / 'r36_report_path.txt').write_text(str(REPORT), encoding='utf-8')
paths = ['app/session/context_resolver.py', 'app/pipeline/competition_overview.py',
         'app/pipeline/retrieval.py', 'app/pipeline/engine.py',
         'app/web_api/pipeline_supervisor.py', 'app/web_api/server.py',
         'app/pipeline/competition_conversation_signals.py']
before = {}
for rel in paths:
    p = ROOT / rel
    if p.exists():
        before[rel] = p.read_bytes()
        dest = REPORT / 'before' / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, dest)
    else:
        before[rel] = None
status = subprocess.run(['git', '-c', 'safe.directory=C:/Users/Chokhun/Downloads/Learn-LLM', '-C', str(ROOT), 'status', '--short'], capture_output=True, text=True)
(REPORT / 'git_status_before.txt').write_text(status.stdout + status.stderr, encoding='utf-8')
protected_keys = json.loads((ROOT / 'reports/r35_conversation_context_20261003_155502_590b79/protected_manifest.json').read_text(encoding='utf-8-sig'))
protected = {rel: hashlib.sha256((ROOT/rel).read_bytes()).hexdigest() for rel in protected_keys}
(REPORT / 'protected_before.json').write_text(json.dumps(protected, indent=2), encoding='utf-8')
for name in ('r36_actual_web_conversation_20261003.txt', 'r36_actual_web_debug_20261003.txt'):
    shutil.copy2(WORK/name, REPORT/name)

changes = {}
changes['app/pipeline/competition_conversation_signals.py'] = '''"""Bounded request grammar for competition conversations; no factual inference."""
from __future__ import annotations

import re
import unicodedata


def _clean(query: str) -> str:
    q = unicodedata.normalize("NFC", str(query or "")).casefold().strip(" ?!.,")
    return re.sub(r"(?:รายการ)+(?=แข่ง)", "รายการ", q).replace("กฏ", "กฎ")


def is_rulebook_catalog_request(query: str) -> bool:
    q = re.sub(r"\\s+", "", _clean(query))
    thai = re.fullmatch(
        r"(?:ตอนนี้)?(?:มี)?(?:รายการแข่ง|รายการแข่งขัน|เกมแข่ง|เกมแข่งขัน)(?:มี)?(?:อะไรบ้าง|อะไรมั่ง|ไหนบ้าง)(?:ครับ|ค่ะ|คับ)?"
        r"|(?:ตอนนี้)?(?:มี)?เกม(?:อะไร|ไหน)(?:ให้|ที่)?(?:รายการ)?(?:แข่ง|แข่งขัน)(?:บ้าง|มั่ง)?(?:ครับ|ค่ะ|คับ)?", q,
    )
    english = re.fullmatch(
        r"(?:what|which) (?:tournaments|competitions|competition games)(?: are (?:there|available|recorded))?"
        r"|list (?:the )?(?:tournaments|competitions|competition games)"
        r"|(?:what|which) games (?:can (?:we|i) compete in|are (?:there|available) for competition)", _clean(query),
    )
    return bool(thai or english)


def _generic_rule_text(query: str) -> str:
    from app.pipeline.competition_targets import resolve_competition_targets, replace_competition_target_mentions
    from app.core.typo_similarity import osa_distance

    resolution = resolve_competition_targets(query)
    if resolution.status == "exact":
        query = replace_competition_target_mentions(query, resolution, "")
    elif resolution.status != "absent":
        return ""
    q = _clean(query)
    if re.search(r"กฎ|กติกา", q):
        # Correct only the courtesy tail after an explicit rule request.
        # Do not rewrite unknown topic words or infer a different game.
        q = re.sub(r"(?:ครับ|ค่ะ|คับ)\\s*$", "", q).rstrip()
        for size in (5, 4, 6):
            suffix = q[-size:]
            prefix = q[:-size].rstrip()
            complete_request = re.fullmatch(
                r"(?:ขอ|ดู|เอา|แล้ว|อยากรู้|อยากดู|บอก|สรุป|มี|ของ|เกมนี้|เกม|กฎ|กติกา|การ|ตอน|แข่งขัน|แข่ง|อะไร|บ้าง|มั่ง|อื่น|เพิ่มเติม|อีก|ทั้งหมด|ไหม|มั้ย|\\s)+", prefix,
            ) and re.search(r"กฎ|กติกา", prefix)
            if complete_request and suffix and osa_distance(suffix, "หน่อย") <= 1:
                q = q[:-size].rstrip()
                break
    return q.strip(" ?!.,")


def is_broad_rule_request(query: str) -> bool:
    q = _generic_rule_text(query)
    if not q or not re.search(r"กฎ|กติกา|\\brules?\\b|\\bregulations\\b", q):
        return False
    thai = re.fullmatch(
        r"(?:ขอ|ดู|เอา|แล้ว|อยากรู้|อยากดู|บอก|สรุป|มี|เรื่อง|ของ|เกมนี้|เกม|กฎ|กติกา|ระเบียบ|การ|ตอน|แข่งขัน|แข่ง|ทัวร์นาเมนต์|อะไร|บ้าง|มั่ง|อื่น|เพิ่มเติม|อีก|ทั้งหมด|ไหม|มั้ย|หน่อย|ครับ|ค่ะ|คับ|\\s|[?!.,])+", q,
    )
    english = re.fullmatch(
        r"(?:can|could|i|we|you|see|show|tell|give|me|please|what|which|are|is|the|a|an|and|any|about|it|its|this|game|of|for|tournament|competition|rules|rule|regulations|other|more|additional|all|overview|summarize|\\s|[?!.,])+", q,
    )
    return bool(thai or english)


def is_more_rule_request(query: str) -> bool:
    q = _generic_rule_text(query)
    return is_broad_rule_request(query) and bool(re.search(r"อื่น|เพิ่มเติม|อีก|\\b(?:more|other|additional)\\b", q))
'''

def read(rel):
    return before[rel].decode('utf-8-sig').replace('\r\n', '\n')

def replace_once(text, old, new):
    if text.count(old) != 1:
        raise RuntimeError(f'Expected one patch location, found {text.count(old)}: {old[:100]}')
    return text.replace(old, new, 1)

rel = 'app/session/context_resolver.py'
s = read(rel)
s = replace_once(s, '    items = _history_dict_items(recent_history)\n    if len(items) < 2:\n', '''    from app.pipeline.competition_conversation_signals import (
        is_broad_rule_request, is_more_rule_request, is_rulebook_catalog_request,
    )

    current_target = resolve_competition_targets(original)
    generic = is_broad_rule_request(original)
    more = is_more_rule_request(original)
    english = original.isascii()
    prefix = ("Additional competition rules for" if more else "Competition rules for") if english else ("กติกาการแข่งขันเพิ่มเติม" if more else "กติกาการแข่งขัน")
    if current_target.status == "exact" and generic:
        target = current_target.targets[0]
        return ResolvedQuestion(
            original, f"{prefix} {target.label}", False, target.label,
            context_domain="competition_rules", context_operation="rule_more" if more else "rule_lookup",
            context_topic=target.label, reason="canonicalized_explicit_generic_competition_rules",
        )

    items = _history_dict_items(recent_history)
    if len(items) < 2:
''')
s = replace_once(s, '        if catalog_choice and prior_target.status == "absent":', '        if (catalog_choice or is_rulebook_catalog_request(prior)) and prior_target.status == "absent":')
start = s.index('    current_target = resolve_competition_targets(original)\n    if current_target.status != "absent"')
end = s.index('\n\ndef resolve_question_with_context', start)
s = s[:start] + '''    if current_target.status != "absent" or detect_game(original) or not generic:
        return None
    # Generic rule follow-ups may survive an intervening failed rule reply.
    # A user change of topic ends the search, regardless of assistant output.
    for index in range(len(items) - 2, -1, -2):
        user, reply = items[index:index + 2]
        if user.get("role") != "user" or reply.get("role") != "assistant":
            break
        if any(item.get("contextEligible") is False or item.get("context_eligible") is False for item in (user, reply)):
            break
        user_text = str(user.get("text") or "")
        user_target = resolve_competition_targets(user_text)
        resolved_text = str(reply.get("resolved_text") or user_text)
        prior_target = resolve_competition_targets(resolved_text)
        if reply.get("route_category") == "competition_rules" and prior_target.status == "exact":
            # An explicit target or a resolved rule follow-up anchors context;
            # assistant example lists never provide a target.
            if user_target.status == "exact" or is_broad_rule_request(user_text):
                target = prior_target.targets[0]
                return ResolvedQuestion(
                    original, f"{prefix} {target.label}", True, target.label,
                    context_domain="competition_rules", context_operation="rule_more" if more else "rule_lookup",
                    context_topic=target.label, reason="inherited_active_competition_game_for_rule_followup",
                )
        if user_target.status != "absent" or not is_broad_rule_request(user_text):
            break
    return None
''' + s[end:]
changes[rel] = s

rel = 'app/pipeline/retrieval.py'
s = read(rel)
start = s.index('def looks_like_broad_competition_rules_query(')
end = s.index('\n\ndef _competition_answer_from_hits', start)
chunk = s[start:end]
chunk = replace_once(chunk, '    if detect_competition_facet(query) is not None:\n        return False\n', '''    if detect_competition_facet(query) is not None:
        return False
    from app.pipeline.competition_conversation_signals import is_broad_rule_request
    if is_broad_rule_request(query):
        return True
''')
changes[rel] = s[:start] + chunk + s[end:]

rel = 'app/pipeline/competition_overview.py'
s = read(rel)
s = replace_once(s, 'from app.pipeline.competition_targets import resolve_competition_targets', 'from app.pipeline.competition_targets import resolve_competition_targets\nfrom app.pipeline.competition_conversation_signals import is_more_rule_request, is_rulebook_catalog_request')
start = s.index("    q = unicodedata.normalize('NFC', query)")
end = s.index('    rows = load_curated_rows()', start)
s = s[:start] + '    if not is_rulebook_catalog_request(query):\n        return None\n' + s[end:]
s = replace_once(s, '    import unicodedata\n', '')
s = replace_once(s, 'def build_competition_overview(query: str, locale: str) -> CompetitionOverview | None:', 'def build_competition_overview(query: str, locale: str, *, recent_history=None) -> CompetitionOverview | None:')
s = replace_once(s, "    target = resolution.targets[0]\n    rows = [", '''    target = resolution.targets[0]
    more = is_more_rule_request(query)
    def comparison_text(text):
        import unicodedata
        return re.sub(r"\\s+", "", unicodedata.normalize("NFC", text).casefold())
    seen_answers = []
    if more and isinstance(recent_history, list):
        for item in recent_history[-10:]:
            if not isinstance(item, dict) or item.get('role') != 'assistant' or item.get('route_category') != 'competition_rules':
                continue
            if item.get('contextEligible') is False or item.get('context_eligible') is False:
                continue
            previous = resolve_competition_targets(str(item.get('resolved_text') or ''))
            if previous.status == 'exact' and previous.targets[0].game_id == target.game_id:
                # History only excludes already displayed clauses. It is not
                # a source of facts and cannot add a new policy or target.
                seen_answers.append(comparison_text(str(item.get('text') or '')))
    rows = [''')
s = replace_once(s, '            lines = substantive_lines(text)\n', '''            lines = substantive_lines(text)
            if more:
                lines = tuple(line for line in lines if not any(comparison_text(line) in answer for answer in seen_answers))
''')
s = replace_once(s, '    if len(selected) < 3:\n        return None\n', '''    if more:
        # Include remaining source sections that do not map to a broad facet.
        for row in rows:
            if len(selected) >= 8:
                break
            if row['id'] in clauses and row['id'] not in seen:
                selected.append(row)
                selected_facets[row['id']] = 'other'
                selected_clauses[row['id']] = clauses[row['id']]
                seen.add(row['id'])
        if not selected:
            english = locale == 'en'
            answer = (f"I could not find further {target.label} clauses to show from the source sections this summary can read. This does not mean the rulebook contains no other rules. Ask about a specific topic for details."
                      if english else f"ยังไม่พบข้อกติกา {target.label} เพิ่มเติมจากส่วนเอกสารที่สรุปนี้อ่านได้ครับ ไม่ได้หมายความว่าเอกสารไม่มีกฎอื่น หากต้องการรายละเอียด ระบุหัวข้อ เช่น บทลงโทษ อุปกรณ์ หรือการหยุดเกมได้ครับ")
            hits = [hit_from_curated(rows[0])] if rows else []
            return CompetitionOverview(answer, hits, ())
    elif len(selected) < 3:
        return None
''')
s = replace_once(s, "    lines = [title, f'Tournament:", "    if more:\n        title = f'Additional {target.label} competition rules from the recorded rulebook:' if english else f'กติกา {target.label} เพิ่มเติมจากเอกสารที่มี:'\n    lines = [title, f'Tournament:")
changes[rel] = s

rel = 'app/pipeline/engine.py'
s = read(rel)
start = s.index('    def answer(')
end = s.index('    def _answer_multi(', start)
chunk = s[start:end]
chunk = replace_once(chunk, '                            planned_task=planner.tasks[0],', '                            planned_task=planner.tasks[0],\n                            recent_history=recent_history,')
chunk = replace_once(chunk, '            return self._answer_single(\n                question,', '            return self._answer_single(\n                question,\n                recent_history=recent_history,')
s = s[:start] + chunk + s[end:]
start = s.index('    def _answer_single(')
end = s.index('    ) -> PipelineAnswer:', start)
chunk = s[start:end]
chunk = replace_once(chunk, '        planned_task: QueryPlanTask | None = None,', '        planned_task: QueryPlanTask | None = None,\n        recent_history=None,')
s = s[:start] + chunk + s[end:]
s = replace_once(s, 'overview = build_competition_overview(pre.clean_query, locale.effective if locale is not None else "th")', 'overview = build_competition_overview(pre.clean_query, locale.effective if locale is not None else "th", recent_history=recent_history)')
changes[rel] = s

rel = 'app/web_api/pipeline_supervisor.py'
s = read(rel)
s = replace_once(s, '                    locale_decision=task.get("locale_decision"),', '                    locale_decision=task.get("locale_decision"),\n                    recent_history=task.get("recent_history"),')
s = replace_once(s, '        locale_decision: dict[str, Any] | None = None,\n    ) -> SupervisedCall:', '        locale_decision: dict[str, Any] | None = None,\n        recent_history: list[dict[str, Any]] | None = None,\n    ) -> SupervisedCall:')
s = replace_once(s, '                    "locale_decision": locale_decision or {},', '                    "locale_decision": locale_decision or {},\n                    "recent_history": list(recent_history or [])[-10:],')
changes[rel] = s

rel = 'app/web_api/server.py'
s = read(rel)
start = s.index('                    supervised = PIPELINE_SUPERVISOR.answer(')
end = s.index('                    worker_id = supervised.worker_id', start)
chunk = s[start:end]
chunk = replace_once(chunk, '                        locale_decision=locale_decision.to_dict(),', '                        locale_decision=locale_decision.to_dict(),\n                        recent_history=recent_history,')
changes[rel] = s[:start] + chunk + s[end:]

# Parse source files without importing the chatbot or executing any question.
for rel, content in changes.items():
    ast.parse(content, filename=rel)
for rel in paths:
    p = ROOT/rel
    if (p.read_bytes() if p.exists() else None) != before[rel]:
        raise RuntimeError('File changed concurrently: ' + rel)
for rel, content in changes.items():
    if before[rel] and b'\r\n' in before[rel]:
        content = content.replace('\n', '\r\n')
    (ROOT/rel).write_text(content, encoding='utf-8', newline='')
after = {rel: hashlib.sha256((ROOT/rel).read_bytes()).hexdigest() for rel in protected_keys}
if after != protected:
    raise RuntimeError('Protected owner/Gold files changed')
(REPORT/'changes.json').write_text(json.dumps({
    'changed_files': list(changes), 'syntax_parse': 'valid', 'protected_files_count': len(protected),
    'protected_files_unchanged': after == protected, 'tests_run': False,
    'before_hashes': {rel: hashlib.sha256(raw).hexdigest() if raw else None for rel,raw in before.items()},
    'after_hashes': {rel: hashlib.sha256((ROOT/rel).read_bytes()).hexdigest() for rel in changes}
}, indent=2), encoding='utf-8')
print(json.dumps({'report':str(REPORT), 'changed_files':len(changes), 'syntax_parse':'valid', 'protected_files_unchanged':len(protected), 'tests_run':False}))
