import hashlib
import json
import re
import sqlite3
import zlib
from pathlib import Path

base = Path(__file__).resolve().parent
out = base / 'r65_detailed_failure_analysis_20261014'
main = out / 'R65_DETAILED_FAILURE_ANALYSIS_TH.md'
text = main.read_text(encoding='utf-8')
anchor = 'จึงต้องตรวจoutcomeclassifierและการนำdiagnosticไปใช้ร่วมกัน ตัวเลขนี้ไม่ใช่จำนวนfalsepositiveเชิงความหมายที่ยืนยันแล้วทั้งหมด'
addition = '''

ตรวจแยกตาม expected vocabulary เพิ่มแล้ว: ใน legacy_offline 4,668 diagnostic ที่เป็น false แต่ strict ผ่าน แบ่งเป็น answer_available 2,295, localization_pending 1,298, route_only 757, live_lookup_required 314 และ clarification_required 4 ตัว `status_matches` รองรับ answer_available อยู่แล้ว จึงไม่ควรสรุปว่าเกิดจากการใช้คำว่า answer แทน answer_available; แต่ไม่รองรับ route_only และ classifier ยังผูกกับ mode whitelist ต้องตรวจ branch/outcome จริงทีละกลุ่มก่อนเปลี่ยนคะแนน รายละเอียดครบทั้งสี่รอบอยู่ใน [STORAGE_AND_OUTCOME_AUDIT.json](C:/Users/Chokhun/Documents/Codex/2026-09-25/psu-esports-studio-phuket-chatbot-c-2/r65_detailed_failure_analysis_20261014/STORAGE_AND_OUTCOME_AUDIT.json)
'''
assert text.count(anchor) == 1
text = text.replace(anchor, anchor + addition)
main.write_text(text, encoding='utf-8')
c = sqlite3.connect((out / 'evidence.sqlite').as_uri() + '?mode=ro', uri=True)
counts = {'results': c.execute('SELECT COUNT(*) FROM results').fetchone()[0],
          'grades': c.execute('SELECT COUNT(*) FROM grades').fetchone()[0]}
assert counts == {'results': 82216, 'grades': 223244}
raw_checks = []
for arm, raw in c.execute('SELECT arm,raw FROM results GROUP BY arm'):
    data = json.loads(zlib.decompress(raw))
    assert isinstance(data, dict) and data
    raw_checks.append(arm)
manifest = json.loads((out / 'INPUT_MANIFEST.json').read_text(encoding='utf-8'))
for item in manifest['files']:
    stat = Path(item['path']).stat()
    assert stat.st_size == item['bytes'] and stat.st_mtime_ns == item['mtime_ns']
broken = []
for link in re.findall(r'\]\((C:/[^)]+)\)', text):
    if not Path(re.sub(r':\d+$', '', link)).exists():
        broken.append(link)
assert not broken
verification = json.loads((out / 'REPORT_VERIFICATION.json').read_text(encoding='utf-8'))
verification['analysis_report_sha256'] = hashlib.sha256(main.read_bytes()).hexdigest()
verification['post_compaction_check'] = {'counts': counts, 'full_raw_samples_decoded_for_arms': raw_checks,
                                       'raw_files_unchanged': len(manifest['files']), 'broken_links': broken}
(out / 'REPORT_VERIFICATION.json').write_text(json.dumps(verification, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'verified': True, 'main_lines': len(text.splitlines()), 'main_bytes': main.stat().st_size,
                  'counts': counts, 'broken_links': broken}, ensure_ascii=False))
