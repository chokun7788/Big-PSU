"""Read existing rule formats and current chat responses without publishing data."""
import hashlib
import json
import sys
import time
import urllib.request
import uuid
from collections import Counter
from datetime import datetime
from pathlib import Path

ROOT = Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
OUT = Path(__file__).parent / ('competition_format_audit_' + datetime.now().strftime('%Y%m%d_%H%M%S') + '_' + uuid.uuid4().hex[:6])
OUT.mkdir()
Path(__file__).with_name('competition_format_audit_path.txt').write_text(str(OUT), encoding='utf-8')
sys.path.insert(0, str(ROOT))
from tools.convert_competition_rules import clean_lines, split_sections, chunk_section
from app.knowledge.canonical_retrieval import active_canonical_competition_release_ids

def read(relative):
    return [json.loads(line) for line in (ROOT / relative).read_text(encoding='utf-8-sig').splitlines() if line.strip()]

docs = read('data/competition_rules/competition_rule_documents.jsonl')
chunks = read('data/competition_rules/competition_rule_chunks.jsonl')
curated = {row['id']: row for row in read('data/curated/curated_competition_rules.jsonl')}
queue = read('data/competition_rules/review/competition_rule_claim_v2_review_queue.jsonl')
records = read('data/competition_rules/canonical/competition_rule_records.jsonl')
releases = read('data/competition_rules/canonical/competition_rule_releases.jsonl')
template = json.loads((ROOT / 'data/competition_rules/canonical/competition_rule_submission_template.json').read_text(encoding='utf-8'))
source_checks = []
for doc in docs:
    raw = Path(doc['source_path']).read_text(encoding='utf-8-sig')
    normalized = clean_lines(raw)
    regenerated = [text for heading, lines in split_sections(normalized) for text in chunk_section(lines)]
    saved = [row for row in chunks if row['document_id'] == doc['id']]
    source_checks.append({'game': doc['game'], 'source_file': doc['source_file'], 'chars': len(raw), 'normalized_lines': len(normalized), 'chunks': len(saved), 'matches_current_source_import': regenerated == [row['text'] for row in saved], 'curated_text_matches_chunks': all(row['id'] in curated and row['text'] == curated[row['id']]['text'] for row in saved)})

summary = {
    'source_checks': source_checks,
    'common_sections': list(template['common_sections']),
    'canonical_game_modules': dict(Counter(row['module'] for row in records if row['module'] != 'common')),
    'canonical_release_states': [{'release_id': row['release_id'], 'runtime_eligible': row['runtime_eligible'], 'activation_status': row['activation_status'], 'review_status': row['review_status']} for row in releases],
    'active_canonical_release_ids': sorted(active_canonical_competition_release_ids()),
    'queue': {'records': len(queue), 'status': dict(Counter(row['status'] for row in queue)), 'atomicity': dict(Counter(row['quality']['atomicity'] for row in queue)), 'heading_relation': dict(Counter(row['quality']['heading_clause_relation'] for row in queue)), 'english_status': dict(Counter(row['claim']['answer_en_status'] for row in queue)), 'blank_answer_th': sum(not row['claim']['answer_th'].strip() for row in queue), 'source_hash_matches': sum(hashlib.sha256(row['source']['clause_th'].encode('utf-8')).hexdigest() == row['source']['clause_sha256'] for row in queue)},
    'raw_heading_equals_text': sum(row['section_title'].strip() == row['text'].strip() for row in chunks),
    'note': 'Equal heading/text may still be a complete numbered rule. This count does not mean 65 rules are empty or wrong.',
    'project_data_mutated': False,
}
with (OUT / 'data_format_audit.json').open('x', encoding='utf-8') as handle:
    json.dump(summary, handle, ensure_ascii=False, indent=2)
print(json.dumps({'output': str(OUT), 'data_summary': summary}, ensure_ascii=False), flush=True)

cases = [
    ('th-team', 'th', 'CS2 แข่งทีมละกี่คน'),
    ('en-team', 'en', 'How many starting players can a CS2 team have?'),
    ('th-settings', 'th', 'Tekken 8 การตั้งค่าเกมเป็นยังไง'),
    ('en-settings', 'en', 'What are the Tekken 8 in-game settings?'),
    ('th-device', 'th', 'RoV ใช้ Tablet หรือ iPad แข่งได้ไหม'),
    ('en-device', 'en', 'Can I use a tablet or iPad in the RoV competition?'),
    ('th-pause', 'th', 'VALORANT technical pause สื่อสารได้ไหม'),
    ('en-pause', 'en', 'Can players communicate during a VALORANT technical pause?'),
    ('th-table', 'th', 'CS2 ตารางบทลงโทษมีอะไรบ้าง'),
    ('en-table', 'en', 'What is the CS2 tournament penalty matrix?'),
    ('th-overview', 'th', 'กติกา CS2 มีอะไรบ้าง'),
    ('en-overview', 'en', 'What are the CS2 tournament rules?'),
]
answers = []
for id, locale, question in cases:
    payload = {'question': question, 'locale': locale, 'recent_history': [], 'client_session_id': 'format-audit-' + uuid.uuid4().hex, 'experimental_allow_llm': True, 'experimental_rag_fallback': True, 'debug': True}
    started = time.perf_counter()
    try:
        response = json.load(urllib.request.urlopen(urllib.request.Request('http://127.0.0.1:8090/api/chat', json.dumps(payload, ensure_ascii=False).encode('utf-8'), {'Content-Type': 'application/json'}), timeout=25))
        answer = response.get('answer', '')
        lines = [line for line in answer.splitlines() if line.strip()]
        record = {'id': id, 'locale': locale, 'question': question, 'first_line': lines[0] if lines else '', 'mode': response.get('mode'), 'route_category': response.get('route_category'), 'latency_sec': round(time.perf_counter() - started, 4), 'response': response}
    except Exception as exc:
        record = {'id': id, 'locale': locale, 'question': question, 'error': str(exc)}
    answers.append(record)
    print(json.dumps({key: value for key, value in record.items() if key != 'response'}, ensure_ascii=False), flush=True)
    with (OUT / 'current_http_answers.jsonl').open('a', encoding='utf-8') as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + '\n')
with (OUT / 'current_http_answers.json').open('x', encoding='utf-8') as handle:
    json.dump(answers, handle, ensure_ascii=False, indent=2)
print('Audit complete', flush=True)
