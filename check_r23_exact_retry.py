from pathlib import Path
import json
import re
import time
import urllib.request
import uuid

report = Path(Path(__file__).with_name('r23_report_path.txt').read_text(encoding='utf-8'))
base = 'http://127.0.0.1:8090'
health = json.load(urllib.request.urlopen(base + '/health', timeout=3))
payload = {
    'question': 'ตอนบ่าย3มีอุปกรณ์อะไรว่างให้เล่นบ้าง',
    'locale': 'th',
    'client_session_id': 'r23-exact-retry-' + uuid.uuid4().hex,
    'recent_history': [],
    'experimental_allow_llm': True,
    'experimental_rag_fallback': True,
    'debug': True,
}
request = urllib.request.Request(
    base + '/api/chat',
    json.dumps(payload, ensure_ascii=False).encode('utf-8'),
    {'Content-Type': 'application/json; charset=utf-8'},
)
started = time.perf_counter()
response = json.load(urllib.request.urlopen(request, timeout=25))
elapsed = round(time.perf_counter() - started, 4)
answer = response.get('answer', '')
traces = [item for item in response.get('trace', []) if item['stage'] == 'live_booking_status']
metadata = traces[-1].get('metadata', {}) if traces else {}
names = [line.strip().removeprefix('•').strip() for line in answer.splitlines() if line.strip().startswith('•')]
count = re.search(r':\s*(\d+)\s*รายการ', answer)
checks = {
    'version_r23': health['runtime']['version'] == '2026.10.01-available-equipment-r23',
    'live_route': response.get('mode') == 'pipeline:live_booking_status_fast_path',
    'fresh_selected_source': metadata.get('transport') == health['runtime']['booking']['fetch_mode'] and metadata.get('source') == 'remote_csv_live' and metadata.get('cached') is False,
    'time_15_to_16': '15:00-16:00' in answer,
    'free_only_format': 'ถูกจอง' not in answer and 'Gaming Monitor' not in answer,
    'count_matches_list': bool(count and int(count.group(1)) == len(names)),
    'under_20_seconds': elapsed < 20,
}
record = {'health': health, 'payload': payload, 'http_wall_sec': elapsed, 'checks': checks, 'response': response}
output = report / ('http_exact_retry_' + uuid.uuid4().hex[:8] + '.json')
with output.open('x', encoding='utf-8') as handle:
    json.dump(record, handle, ensure_ascii=False, indent=2)
print(json.dumps({'path': str(output), 'http_wall_sec': elapsed, 'checks': checks, 'metadata': metadata, 'answer': answer}, ensure_ascii=False))
if not all(checks.values()):
    raise SystemExit(1)
