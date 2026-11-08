"""Read retained results only. This script never imports the chatbot or a model."""
from pathlib import Path
from collections import Counter, defaultdict
import hashlib
import json

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(__file__).resolve().parent
R95 = ROOT / 'r95_merged_flow_implementation_20261018'
OLD = ROOT / 'r89_saved_full_comparison_20261018/SAME_CHECKER_COMPARISON.json'

def read(path):
    return json.loads(path.read_text(encoding='utf-8'))

def classify(row):
    mode = row.get('mode') or ''
    rejected = row.get('rejected_candidate') or {}
    errors = rejected.get('validation_errors') or []
    plan = row.get('query_plan') or {}
    selection = plan.get('entity_selection') or {}
    if mode == 'pipeline:common_not_current':
        return 'source_validity_not_current'
    if selection.get('availability_failure') in {'timeout', 'busy'}:
        return 'model_availability_' + selection['availability_failure']
    if 'unresolved_query_clause' in errors:
        return 'candidate_rejected_unresolved_clause'
    if any(x.startswith('missing_requested_field:') for x in errors):
        return 'candidate_rejected_missing_field'
    if rejected:
        return 'candidate_rejected_other'
    if 'clarification' in mode:
        return 'clarification_with_failed_text_contract'
    if 'answer' in mode:
        return 'answer_with_failed_text_contract_needs_semantic_review'
    return 'other_needs_review'

def main():
    old, new = read(OLD), read(R95/'full_analysis/ANALYSIS_FINAL.json')
    request_counts, grade_counts = Counter(), Counter()
    examples, domains = defaultdict(list), defaultdict(Counter)
    failure_requests = failure_grades = 0
    mode_counts = Counter()
    for line in (R95/'full_analysis/PER_REQUEST_ANALYSIS.jsonl').open(encoding='utf-8'):
        row = json.loads(line)
        failed = [x for x in row.get('failures', []) if x.get('positive') and not x.get('passed')]
        if not failed:
            continue
        category = classify(row)
        failure_requests += 1
        failure_grades += len(failed)
        request_counts[category] += 1
        grade_counts[category] += len(failed)
        domains[row.get('domain', '')][category] += 1
        mode_counts[row.get('mode', '')] += 1
        if len(examples[category]) < 3:
            examples[category].append({
                'key': row['key'], 'question': row['question'], 'locale': row.get('locale'),
                'domain': row.get('domain'), 'answer': row.get('answer'), 'mode': row.get('mode'),
                'path': row.get('path'), 'query_plan': row.get('query_plan'),
                'rejected_candidate': row.get('rejected_candidate'), 'failed_contracts': failed,
            })
    assert failure_grades == new['totals']['positive_checked'] - new['totals']['positive_passed']
    assert failure_requests == new['totals']['positive_requests'] - new['totals']['all_positive_pass_requests']
    comparison = {}
    for domain, row in new['by_domain'].items():
        if domain not in old['by_domain'] or not row.get('positive_checked'):
            continue
        legacy = old['by_domain'][domain]['old_positive_passed']
        comparison[domain] = {
            'denominator': row['positive_checked'], 'legacy_passed': legacy,
            'r88_passed': old['by_domain'][domain]['new_positive_passed'],
            'r95_passed': row['positive_passed'], 'net_grade_gap_vs_legacy': legacy-row['positive_passed'],
        }
    payload = {
        'scope': 'retained-output analysis only; no chatbot/model/test execution',
        'classification': 'mutually exclusive diagnostic buckets from existing logs, not verified semantic root causes',
        'precedence': ['validity', 'model availability', 'unresolved clause', 'missing field', 'other rejection', 'clarification', 'answer text mismatch', 'other'],
        'failed_positive_requests': failure_requests, 'failed_positive_grades': failure_grades,
        'request_counts': dict(request_counts), 'grade_counts': dict(grade_counts),
        'by_domain': {k:dict(v) for k,v in domains.items()},
        'mode_counts': dict(mode_counts), 'domain_comparison': comparison,
        'examples': dict(examples),
    }
    (OUT/'SAVED_EVIDENCE_ANALYSIS.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding='utf-8')
    paths = [OLD,R95/'full_analysis/ANALYSIS_FINAL.json',R95/'full_analysis/PER_REQUEST_ANALYSIS.jsonl',
             R95/'full_analysis/REGRESSIONS_VS_R88.json',R95/'FULL_TEST_COMPLETE.json']
    paths += list((R95/'system/app/knowledge/common').glob('task_*.py'))
    paths += [R95/'system/app/knowledge/common/answer.py',R95/'system/app/pipeline/migrated_chat.py']
    manifest = {str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    (OUT/'READ_ONLY_SOURCE_MANIFEST.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    print(json.dumps({'requests':failure_requests,'grades':failure_grades,'request_counts':dict(request_counts),'grade_counts':dict(grade_counts)},ensure_ascii=False))

if __name__ == '__main__':
    main()
