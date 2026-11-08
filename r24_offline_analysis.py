"""Regrade stored answers only and preserve every original result."""
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data')
REPORT = Path(Path(__file__).with_name('r24_report_path.txt').read_text(encoding='utf-8').strip())
sys.path.insert(0, str(ROOT))
from app.knowledge.localization import approved_localization
from tools.competition_user_ground_truth_r24 import normalized

def read(path):
    return [json.loads(line) for line in path.read_text(encoding='utf-8-sig').splitlines() if line.strip()]

source = {row['id']: row for row in read(ROOT / 'data/competition_rules/competition_rule_chunks.jsonl')}
gold = {row['id']: row for row in read(ROOT / 'data/eval/competition_user_r24_2000_20261001.jsonl')}
original = read(REPORT / 'full_A_details.jsonl')
regraded = []
changed = []
for record in original:
    row = dict(record)
    row['failures'] = list(record['failures'])
    if 'answer_without_substantive_source_content' in row['failures']:
        ids = [id.removeprefix('canonical::') for id in row['source_ids'] if id.removeprefix('canonical::') in source]
        texts = [(approved_localization(source[id], 'text') if row['locale'] == 'en' else source[id]['text']) or '' for id in ids]
        short = [normalized(line.strip().lstrip('*-•· ')) for text in texts for line in text.splitlines() if 8 <= len(line.strip()) < 120 and (any(ch.isdigit() for ch in line) or re.search(r'\b(?:uses?|must|may|prohibited|allowed)\b', line, re.I))]
        if any(text in normalized(row['answer']) for text in short):
            row['failures'].remove('answer_without_substantive_source_content')
            changed.append({'id': row['id'], 'original_failures': record['failures'], 'regraded_failures': row['failures'], 'reason': 'Short complete literal source facts are valid; original answer was not rerun.'})
    row['passed'] = not row['failures']
    regraded.append(row)
stats = Counter('passed' if row['passed'] else 'failed' for row in regraded)
for row in regraded:
    stats.update(row['failures'])
summary = {'run': 'full_A_offline_regraded_with_B_short_fact_rubric', 'total': len(regraded), 'stats': dict(stats), 'regraded_cases': len(changed), 'pipeline_rerun': False, 'original_file_unchanged': True, 'note': 'Only short literal content gate changed. All original routes, answers, target and facet judgments retained. The one new identity translation is excluded from this short-content gate.'}
with (REPORT / 'full_A_offline_regraded_summary.json').open('x', encoding='utf-8') as handle:
    json.dump(summary, handle, ensure_ascii=False, indent=2)
with (REPORT / 'full_A_short_content_regrading.json').open('x', encoding='utf-8') as handle:
    json.dump(changed, handle, ensure_ascii=False, indent=2)

def diagnosis(row):
    if row['mode'] == 'pipeline:game_meta_clarification':
        return 'ตัวกรองคำถามเกมทั่วไปทำงานก่อนกติกา แม้มีชื่อเกมและหัวข้อการแข่งขันครบ; เพิ่มเงื่อนไข competition signal ก่อนตัวกรอง'
    if row['id'] == 'R24-TH-SAFE-013':
        return 'คำว่า กติกกา ไม่ฟื้นเป็น กติกา เมื่อไม่มีชื่อเกม; ฟื้น cue เฉพาะเมื่อมี timeout/การแข่งขัน แล้วถามให้ระบุเกม'
    if row['locale'] == 'en' and row['expected_facet'] == 'rulebook_identity' and row['game'] == 'tekken8':
        return 'ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม'
    failures = set(row['failures'])
    if 'foreign_game_evidence' in failures:
        return 'พบหลักฐานเกมอื่น; trace แสดงการขยายชื่อเกม/การเปรียบเทียบ ต้องยึด explicit target เดิมและใช้ query แยกแต่ละเกม'
    if 'route_mismatch' in failures:
        return 'เข้าหมวดอื่นก่อนการแข่งขัน; ตรวจ cue และ protected responder ที่แย่งตอบ เช่น rulebook มี book'
    if failures == {'answer_without_substantive_source_content'}:
        return 'ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก'
    if 'overview_without_multiple_rule_clauses' in failures:
        return 'คำถามรวมได้หลักฐานหลายหัวข้อแต่ไม่มีข้อความกติกาจริงครบ; ใช้ selected substantive overview ของเกมที่ระบุ'
    if 'wrong_facet_evidence' in failures:
        return 'เลือกหัวข้อไม่ตรงคำถามหรือไม่มี English เนื้อหาในแถวที่ตรง; จัด substantive candidates ก่อน headings'
    return 'ตรวจ outcome, source IDs และ trace รายกรณี; หมวดนี้เป็นการจัดกลุ่มอัตโนมัติ ไม่ใช่คำยืนยันสาเหตุจากมนุษย์'

lines = ['# รายละเอียดเคสที่ตกในการทดสอบ r24', '', 'เก็บคำตอบจริงจากการรันไว้ครบใน JSONL เดิม เอกสารนี้เพิ่มคำอธิบายโดยไม่แก้ผลเก่า', '', '## รอบ B: 37 เคสที่ตกและทดสอบซ้ำ C ผ่าน', '']
retake = {row['id']: row for row in read(REPORT / 'failed_C_details.jsonl')}
for row in read(REPORT / 'full_B_details.jsonl'):
    if row['passed']:
        continue
    case = gold[row['id']]
    lines.extend([f"### {row['id']}", '', f"- คำถาม: {row['question']}", f"- คาดหวัง: {row['expected_status']} / {case.get('expected_game_id')} / {row['expected_facet'] or 'ต้องระบุเกม'}", f"- ตอบจริงรอบ B: `{row['mode']}` — {row['answer'].replace(chr(10), ' ')[:750]}", f"- เงื่อนไขที่ตก: {', '.join(row['failures'])}", f"- วิเคราะห์: {diagnosis(row)}", f"- ทดสอบซ้ำ C: {'ผ่าน' if retake[row['id']]['passed'] else 'ไม่ผ่าน'} / `{retake[row['id']]['mode']}`", f"- คำตอบหลังแก้: {retake[row['id']]['answer'].replace(chr(10), ' ')[:1100]}", ''])
lines.extend(['## รอบ A: เคสที่ตกตาม rubric เดิม 180 เคส', '', 'หลายสาเหตุอาจเกิดร่วมกันในเคสเดียว; คอลัมน์วิเคราะห์เป็นการจัดกลุ่มเบื้องต้น ต้องอ่าน trace เพื่อยืนยันข้อสรุปรายเคส', '', '| ID | คำถาม | Mode | เหตุที่ตก | วิเคราะห์ |', '|---|---|---|---|---|'])
for row in original:
    if not row['passed']:
        values = [row['id'], row['question'], row['mode'], ', '.join(row['failures']), diagnosis(row)]
        lines.append('| ' + ' | '.join(value.replace('|', '\\|').replace('\n', ' ') for value in values) + ' |')
with (REPORT / 'failure_analysis_r24.md').open('x', encoding='utf-8') as handle:
    handle.write('\n'.join(lines) + '\n')

preservation = {
    'source_gold': {'expected_sha256': '51e94305ddc0e30190480698a217d09b16e00d0f9fe2612b4206e1e868cc36c1', 'actual_sha256': hashlib.sha256((ROOT / 'data/eval/competition_rules_rag_ground_truth_v1.jsonl').read_bytes()).hexdigest()},
    'source_chunks': {'expected_sha256': '36fa00666d129cb8e65d8828b841ced198ec10d4f87b0c7aa1cb1057443bd9b0', 'actual_sha256': hashlib.sha256((ROOT / 'data/competition_rules/competition_rule_chunks.jsonl').read_bytes()).hexdigest()},
    'app_package_matches_source': all((ROOT / path.relative_to(ROOT / 'owner_local_delivery_20261001_competition_r24_final/PSU_Esports_Chatbot_Local')).read_bytes() == path.read_bytes() for path in (ROOT / 'owner_local_delivery_20261001_competition_r24_final/PSU_Esports_Chatbot_Local/app').rglob('*.py') if '__pycache__' not in path.parts),
    'old_source_backups': [str(path.relative_to(REPORT)) for path in (REPORT / 'before').rglob('*.py')],
    'old_package_snapshot_backups': [str(path.relative_to(REPORT)) for path in (REPORT / 'package_final_before_sync').rglob('*') if path.is_file()],
}
assert all(preservation[key]['expected_sha256'] == preservation[key]['actual_sha256'] for key in ('source_gold', 'source_chunks'))
assert preservation['app_package_matches_source']
with (REPORT / 'final_preservation_check.json').open('x', encoding='utf-8') as handle:
    json.dump(preservation, handle, ensure_ascii=False, indent=2)
print(json.dumps(summary, ensure_ascii=False))
