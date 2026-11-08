import json,sys,hashlib
from pathlib import Path
p=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');r=Path(Path('r30_report_path.txt').read_text().strip());sys.path.insert(0,str(p))
from app.pipeline.competition_detail import requested_detail_concepts
queries={'สถานที่จัด PSU Phuket CS2 2026 คือที่ไหน':'venue','CS2 timeout ตอน freeze time ได้กี่วิกี่ครั้ง':'timeout'}
rows={}
for line in (r/'FINAL_G6_EXTRA_CORPUS_RESULTS.jsonl').open(encoding='utf-8'):
    row=json.loads(line)
    if row['question'] in queries:rows[row['question']]=row
assert len(rows)==2
source=p/'data/content/competition/competition_rules_cs2_psu_phuket_2026.json'
doc=json.loads(source.read_text(encoding='utf-8'));sections=doc['locales']['th']['fields']['sections']
evidence={}
for q,kind in queries.items():
    clauses=[s for s in sections if ('การแข่งขันจะแข่งขันทั้งหมด 1 วัน' if kind=='venue' else 'การขอเวลานอก ทีมละ 4 ครั้ง') in s['text']]
    assert len(clauses)==1
    evidence[q]={'actual':rows[q],'recognized_concepts':[x.name for x in requested_detail_concepts(q,'cs2')],'source_path':str(source),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'literal_source':clauses[0], 'cause':'Venue vocabulary does not recognize สถานที่จัด before the event title; no recognized detail concept, so coverage safely refuses.' if kind=='venue' else 'Bare timeout is not tactical_timeout vocabulary; freeze time matches round_time, so the duration of the round is answered while the requested timeout quantity/duration is omitted.', 'expected_source_bound_answer':'ตามเอกสารกติกา CS2 ที่มี: แข่งขัน 1 วัน ณ PSU Esports Studio - Phuket มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต' if kind=='venue' else 'ตามเอกสารกติกา CS2 ที่มี: ขอเวลานอกได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time', 'policy_confirmation':'recorded source only; not confirmation of current event schedule','priority':'P1','next_flow':'Add bounded proposition vocabulary plus TH/EN, clean/noisy, negative controls; validate requested quantity, duration and condition; never substitute freeze-time duration for timeout.'}
with (r/'CONFIRMED_REMAINING_G6_CASES.json').open('x',encoding='utf-8') as out:json.dump(evidence,out,ensure_ascii=False,indent=2)
text=['# ข้อที่ยังผิดจริงหลัง G6 และ Flow รอบถัดไป','', 'ข้อเหล่านี้ตรวจจากคำตอบ/trace และต้นฉบับแล้ว แยกจาก keyword รูปแบบเก่า ยังไม่ได้แก้ใน G6 และไม่ต้องเดานโยบายใหม่','']
for q,e in evidence.items():
    text += ['## '+q,'','- คำตอบจริง: '+e['actual']['result']['answer'],'- Concept ที่ระบบรู้จัก: '+(', '.join(e['recognized_concepts']) or 'ไม่มี'),'- สาเหตุที่ยืนยัน: '+e['cause'],'- คำตอบที่ควรได้ตามเอกสารเดิม: '+e['expected_source_bound_answer'],'- ข้อ source: '+e['literal_source']['text'],'- งานต่อ: '+e['next_flow'],'']
text += ['## Gate รอบถัดไป','','1. เพิ่ม content contract ของ venue/timeout ก่อนแก้ รวมคำถามที่ถามเฉพาะสถานที่หรือเฉพาะจำนวน/เวลา และคำถามสองเรื่อง','2. ตรวจ negative: timeout ของ VALORANT, เวลา freeze time ปกติ, เวลานอกทางเทคนิค, ตำแหน่งปุ่ม, วันจัดรายการใหม่ที่ไม่มี source','3. แก้ matcher/coverage แบบ proposition ที่ผูกเกมและ source ไม่เพิ่ม whole-question alias','4. ตรวจ first line + quantities + condition + source + recorded-event qualifier; focused → unit → competition corpora → actual API','5. เปรียบเทียบ clean/noisy และทำ source/Gold preservation audit ก่อน release','', 'หลักฐาน JSON มี actual trace/grades, source hash และต้นฉบับครบ ไม่ใช้จำนวนเกณฑ์ไม่ผ่านแทนจำนวนคำตอบผิดทั้งหมด']
with (r/'REMAINING_G6_PRIORITY_AND_FLOW_TH.md').open('x',encoding='utf-8') as out:out.write('\n'.join(text)+'\n')
print(json.dumps({q:e['recognized_concepts'] for q,e in evidence.items()},ensure_ascii=False))
