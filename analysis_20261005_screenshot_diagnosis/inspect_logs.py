import json
import subprocess
from pathlib import Path

ROOTS = [
    Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data'),
    Path(r'C:\Users\Chokhun\Documents\Codex\PSU Esports Chatbot Ready 20261003'),
    Path(r'C:\Users\Chokhun\Documents\Codex\PSU_Esports_Share_20261003'),
]
out = Path(__file__).resolve().parent
scan = subprocess.run(['rg', '--files', '--hidden', '--no-ignore', '-g', 'web_chat_*.jsonl', '-g', '!**/.git/**', '-g', '!**/.venv/**', '-g', '!**/runtime/**', '-g', '!**/models/**', *map(str, ROOTS)], capture_output=True, text=True, encoding='utf-8')
paths = list(dict.fromkeys(scan.stdout.splitlines()))
matches = []
errors = []
count = 0
for name in paths:
    try:
        records = []
        for no, line in enumerate(Path(name).read_text(encoding='utf-8-sig').splitlines(), 1):
            try:
                row = json.loads(line)
            except (ValueError, TypeError):
                continue
            count += 1
            records.append((no, row))
        sessions = set()
        for no, row in records:
            q = str(row.get('question', ''))
            if ('บุคคลภายนอก' in q and ('ราคา' in q or 'ค่าบริการ' in q)) or ('ไก่' in q and 'ไข่' in q):
                sessions.add(row.get('client_session_id'))
        for no, row in records:
            if sessions and row.get('client_session_id') in sessions:
                matches.append({'file': name, 'line': no, 'record': row})
    except (OSError, UnicodeError) as e:
        errors.append({'file': name, 'error': str(e)})
(out / 'matching_sessions.json').write_text(json.dumps(matches, ensure_ascii=False, indent=2), encoding='utf-8')
inventory = {'files_scanned': len(paths), 'records_scanned': count, 'matching_session_records': len(matches), 'read_errors': errors, 'rg_errors': scan.stderr, 'files': paths}
(out / 'scan_inventory.json').write_text(json.dumps(inventory, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({k: inventory[k] for k in ['files_scanned', 'records_scanned', 'matching_session_records', 'read_errors']}, ensure_ascii=False))
for match in matches:
    r = match['record']
    print(json.dumps({'file': match['file'], 'line': match['line'], 'timestamp': r.get('timestamp'), 'question': r.get('question'), 'mode': r.get('mode'), 'history_count': r.get('recent_history_count'), 'resolved': r.get('context_resolution'), 'answer': r.get('answer', '')[:280]}, ensure_ascii=False))
