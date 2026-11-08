"""Consolidate authored source reviews; compare only to completed saved sample.

No assistant/model calls, grading or source mutations occur here.
"""
import collections
import gzip
import hashlib
import json
import time
from pathlib import Path

R = Path(__file__).resolve().parent


def load(name):
    return json.loads((R / name).read_text('utf-8-sig'))


def write(name, value):
    (R / name).write_text(json.dumps(value, ensure_ascii=False, indent=2), 'utf8')


assert load('EXECUTION_COMPLETE.json')['complete']
assert load('ANALYSIS_COMPLETE.json')['sample_coverage_verified']
assert not load('MODEL_AND_MECHANISM_AUDIT.json')['provenance_errors']
sources = [
    'INDIVIDUAL_SOURCE_REVIEW.json',
    'POST_GATE_GPU_CAUSAL_REFINEMENT.json',
    'POST_GATE_RELATED_SOURCE_REVIEW.json',
    'POST_GATE_TOURNAMENT_SCOPE_REVIEW.json',
]
reviews = collections.defaultdict(list)
for name in sources:
    for case in load(name)['cases']:
        reviews[case['key']].append({'review_file': name, 'case': case})

consolidated = []
for key, evidence in sorted(reviews.items()):
    questions = {x['case']['question'] for x in evidence}
    answers = {x['case'].get('answer', x['case'].get('saved_answer')) for x in evidence}
    assert len(questions) == len(answers) == 1, key
    flags = [x['case']['confirmed_actual_content_failure'] for x in evidence
             if 'confirmed_actual_content_failure' in x['case']]
    assert not flags or len(set(flags)) == 1, ('conflicting_manual_decisions', key)
    gpu_probe = any(x['review_file'] == 'POST_GATE_GPU_CAUSAL_REFINEMENT.json' for x in evidence)
    consolidated.append({
        'key': key, 'question': next(iter(questions)), 'saved_answer': next(iter(answers)),
        'confirmed_content_scope_omission_example': any(flags) or gpu_probe,
        'judgment_basis': 'authored_source_review_and_or_local_reader_probe',
        'evidence': evidence,
    })
assert len(consolidated) == 167
assert sum(x['confirmed_content_scope_omission_example'] for x in consolidated) == 117
write('CONSOLIDATED_SOURCE_REVIEW.json', {
    'unique_reviewed_or_probed_keys': len(consolidated),
    'confirmed_content_scope_omission_examples': 117,
    'semantic_unadjudicated_keys_in_full': 20554 - len(consolidated),
    'semantic_accuracy': None, 'not_exhaustive_error_count': True,
    'cases': consolidated,
})

fresh = {}
for path in sorted((R / 'sample01').glob('RESULTS_*.jsonl.gz')):
    with gzip.open(path, 'rt', encoding='utf8') as stream:
        for line in stream:
            row = json.loads(line)
            assert row['key'] not in fresh
            fresh[row['key']] = row
assert len(fresh) == 2111
reproductions = []
for case in consolidated:
    if case['key'] not in fresh:
        continue
    row = fresh[case['key']]
    answer = (row.get('result') or {}).get('answer')
    exact = answer == case['saved_answer']
    reproductions.append({
        'key': case['key'], 'question': case['question'],
        'saved_answer': case['saved_answer'], 'new_answer': answer,
        'exact_answer_reproduced': exact,
        'previous_confirmed_content_scope_omission_example': case['confirmed_content_scope_omission_example'],
        'semantic_disposition': 'previous_source_review_applies_to_identical_answer_input_and_source' if exact else 'changed_answer_review_required',
        'evidence_files': [x['review_file'] for x in case['evidence']],
    })
write('ALL_REVIEWED_CASE_REPRODUCTION.json', {
    'cases': reproductions,
    'source_reviewed_keys_in_sample': len(reproductions),
    'identical_answer_count': sum(x['exact_answer_reproduced'] for x in reproductions),
    'confirmed_failure_examples_reproduced': sum(x['exact_answer_reproduced'] and x['previous_confirmed_content_scope_omission_example'] for x in reproductions),
    'semantic_accuracy': None, 'not_random_semantic_adjudication_of_all_sample_keys': True,
})
changes = load('REPEAT_ANSWER_CHANGES.json')
# Changed answers require authored review. Zero changes closes this gate without
# pretending unchanged answers are correct or all sample semantics were reviewed.
if changes['changed_answer_count']:
    raise RuntimeError('Author source-backed CHANGED_ANSWER_REVIEW.json before closing this gate')
write('CHANGED_ANSWER_REVIEW.json', {
    'complete': True, 'changed_answer_count': 0,
    'all_2111_answer_strings_identical_to_saved_R130': True,
    'conclusion_th': 'คำตอบเหมือนเดิมทุกข้อ รวมทั้งตัวอย่างปัญหาที่ตรวจ source ไว้ ไม่ใช่ผลคุณภาพดีขึ้นหรือคำยืนยันว่าคำตอบทั้งหมดถูก',
    'semantic_accuracy': None, 'new_semantic_judgments_from_string_equality': 0,
})
analysis = load('ANALYSIS_COMPLETE.json')
analysis.update(changed_answer_semantic_review_pending=False,
                changed_answer_review_complete=True,
                all_reviewed_case_reproduction_complete=True)
write('ANALYSIS_COMPLETE.json', analysis)
parent_trace_path=R.parent/'r130_owner_context_completion_20261025/REQUIREMENTS_TRACEABILITY.json'
parent_trace=json.loads(parent_trace_path.read_text('utf-8-sig'))
assert len(parent_trace['requirements'])==76
write('REQUIREMENTS_SCOPE_PRESERVATION.json', {
    'authoritative_traceability_path': str(parent_trace_path),
    'authoritative_traceability_sha256': hashlib.sha256(parent_trace_path.read_bytes()).hexdigest(),
    'requirements': [{'id': x['id'], 'title': x['title'], 'source_sha256': x.get('sha256'),
                      'copied_definition_text_sha256': hashlib.sha256(x['text'].encode('utf8')).hexdigest(),
                      'inherited_acceptance_status': x['status']}
                     for x in parent_trace['requirements']],
    'requirements_removed': 0, 'acceptance_statuses_promoted_by_sample': 0,
    'scope_categories': 14, 'completion_percent': None,
    'semantic_acceptance_complete': False,
    'note_th': 'งานข้อ2และsampleเสร็จไม่เปลี่ยนstatusคุณภาพรายrequirement; ใช้ทะเบียนต้นเหตุและsourcecaseประกอบการแก้ถัดไป ไม่ใช้membershipทุกหมวดแทนoperationcoverage',
})
write('REQUEST_COMPLETION.json', {
    'requested_detailed_diagnosis_then_ten_percent_sample_complete': True,
    'diagnosis_preceded_new_execution': True,
    'sample_requests': 2111, 'sample_grade_identities': 5584,
    'reviewed_or_probed_source_keys': 167,
    'confirmed_content_scope_omission_examples': 117,
    'all_input_categories_sampled': True,
    'sparse_category_limitations': ['C07: population6/selected1, mainly offsite; onsite rental not comprehensively evaluated', 'C14: no real current-news source records'],
    'flow_quality_acceptance_complete': False,
    'requirements_scope': {'count': 76, 'categories': 14, 'scope_reduced': False},
    'semantic_accuracy': None,
    'runtime_fixes': 0, 'new_baseline_inferences': 0, 'baseline_regrading': 0,
    'production_installed': False,
    'completed_at': time.time(),
    'evidence_sha256': {name: hashlib.sha256((R / name).read_bytes()).hexdigest()
        for name in ['DIAGNOSIS_PRETEST_COMPLETE.json', 'EXECUTION_COMPLETE.json',
                     'COVERAGE.json', 'SCORES.json', 'MODEL_AND_MECHANISM_AUDIT.json',
                     'CONSOLIDATED_SOURCE_REVIEW.json', 'CHANGED_ANSWER_REVIEW.json']},
})
write('STATUS.json', {
    'phase': 'requested_diagnosis_and_sample_complete', 'complete': True,
    'diagnosis_complete': True, 'sample_complete': True,
    'sample_requests': 2111, 'sample_grades': 5584,
    'flow_quality_acceptance_complete': False, 'semantic_accuracy': None,
    'production_installed': False, 'updated_at': time.time(),
})
print(json.dumps({'reviewed_cases': len(consolidated),
                  'sample_reviewed_cases': len(reproductions),
                  'reproduced_confirmed_examples': sum(x['exact_answer_reproduced'] and x['previous_confirmed_content_scope_omission_example'] for x in reproductions),
                  'changed_answers': 0}, ensure_ascii=False))
