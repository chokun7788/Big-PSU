from pathlib import Path
import ast, hashlib, json, shutil, difflib

work = Path(__file__).parent
root = Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
report = Path((work/'r36_report_path.txt').read_text(encoding='utf-8').strip())
def patch(rel, old, new):
    p = root/rel
    raw = p.read_bytes()
    text = raw.decode('utf-8-sig').replace('\r\n', '\n')
    if text.count(old) != 1:
        raise RuntimeError('Patch position count differs: '+rel)
    content = text.replace(old, new, 1)
    ast.parse(content, filename=rel)
    snapshot = report/'before_static_review'/rel
    snapshot.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(p, snapshot)
    if b'\r\n' in raw:
        content = content.replace('\n', '\r\n')
    p.write_text(content, encoding='utf-8', newline='')

patch('app/pipeline/competition_overview.py',
      '    section_ids: tuple[str, ...]\n',
      '    section_ids: tuple[str, ...]\n    history_answer_count: int = 0\n    excluded_clause_count: int = 0\n    no_further_clauses: bool = False\n')
patch('app/pipeline/competition_overview.py', '    clauses = {}\n', '    clauses = {}\n    excluded_count = 0\n')
patch('app/pipeline/competition_overview.py',
      '            if more:\n                lines = tuple(line for line in lines if not any(comparison_text(line) in answer for answer in seen_answers))\n',
      '            if more:\n                previous_count = len(lines)\n                lines = tuple(line for line in lines if not any(comparison_text(line) in answer for answer in seen_answers))\n                excluded_count += previous_count - len(lines)\n')
patch('app/pipeline/competition_overview.py',
      '            return CompetitionOverview(answer, hits, ())',
      '            return CompetitionOverview(answer, hits, (), len(seen_answers), excluded_count, True)')
patch('app/pipeline/competition_overview.py',
      "    return CompetitionOverview('\\n'.join(lines), [hit_from_curated(row) for row in used], tuple(row['id'] for row in used))",
      "    return CompetitionOverview('\\n'.join(lines), [hit_from_curated(row) for row in used], tuple(row['id'] for row in used), len(seen_answers), excluded_count)")
patch('app/pipeline/engine.py',
      '                overview_frame = build_question_frame(pre.clean_query, overview_route)\n                validation = validate_answer(pre.clean_query, overview.answer, overview_route, entities, hits=overview.hits, mode="pipeline:competition_rule_overview_source", frame=overview_frame)',
      '                overview_frame = build_question_frame(pre.clean_query, overview_route)\n                overview_mode = "pipeline:competition_rule_detail_no_answer" if overview.no_further_clauses else "pipeline:competition_rule_overview_source"\n                validation = validate_answer(pre.clean_query, overview.answer, overview_route, entities, hits=overview.hits, mode=overview_mode, frame=overview_frame)')
patch('app/pipeline/engine.py',
      '{"section_ids": list(overview.section_ids), "game_ids": [target.game_id for target in competition_target.targets], "validation_errors": list(validation.errors)}',
      '{"section_ids": list(overview.section_ids), "game_ids": [target.game_id for target in competition_target.targets], "validation_errors": list(validation.errors), "history_answer_count": overview.history_answer_count, "excluded_clause_count": overview.excluded_clause_count, "no_further_clauses": overview.no_further_clauses}')
patch('app/pipeline/engine.py',
      'return self._build_result(overview.answer, overview.hits, started, "pipeline:competition_rule_overview_source", 0.98, overview_route, entities, validation, trace)',
      'return self._build_result(overview.answer, overview.hits, started, overview_mode, 0.98, overview_route, entities, validation, trace)')
changes = json.loads((report/'changes.json').read_text(encoding='utf-8'))
for rel in changes['changed_files']:
    content = (root/rel).read_text(encoding='utf-8-sig')
    ast.parse(content, filename=rel)
    previous = report/'before'/rel
    old = previous.read_text(encoding='utf-8-sig') if previous.exists() else ''
    diff = ''.join(difflib.unified_diff(old.splitlines(True), content.splitlines(True), fromfile='before/'+rel, tofile='after/'+rel))
    dest = report/'diff'/Path(rel).with_suffix('.diff')
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(diff, encoding='utf-8')
    changes['after_hashes'][rel] = hashlib.sha256((root/rel).read_bytes()).hexdigest()
protected = json.loads((report/'protected_before.json').read_text(encoding='utf-8'))
assert all(hashlib.sha256((root/rel).read_bytes()).hexdigest() == sha for rel,sha in protected.items())
(report/'changes_final.json').write_text(json.dumps(changes, indent=2), encoding='utf-8')
print(json.dumps({'source_syntax':'valid', 'protected_unchanged':len(protected), 'tests_run':False, 'diff_files':len(changes['changed_files'])}))
