import json,hashlib,uuid,sys,os,subprocess
from pathlib import Path
from datetime import datetime
root=Path(__file__).parent;project=Path(r'C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data');sys.path.insert(0,str(project))
old=Path((root/'r28_report_path.txt').read_text(encoding='utf-8').strip())
report=project/'reports'/('r29_input_guard_context_'+datetime.now().strftime('%Y%m%d_%H%M%S')+'_'+uuid.uuid4().hex[:6]);report.mkdir()
(root/'r29_report_path.txt').write_text(str(report),encoding='utf-8')
files=['app/core/keyboard_input_anomaly.py','app/core/runtime_input_quality_guard.py','app/pipeline/engine.py','app/web_api/pipeline_supervisor.py']
protected=json.loads((old/'protected_manifest.json').read_text(encoding='utf-8'));protected.pop('docs/127_competition_contract_r27_flow_20261001.md')
protected['data/eval/master_gt_bilingual_multi_error_2000_20260929_r15.jsonl']=hashlib.sha256((project/'data/eval/master_gt_bilingual_multi_error_2000_20260929_r15.jsonl').read_bytes()).hexdigest()
manifest={}
for name in files:
    path=report/'before'/name;path.parent.mkdir(parents=True,exist_ok=True);path.open('xb').write((project/name).read_bytes());manifest[name]=hashlib.sha256((project/name).read_bytes()).hexdigest()
for name,data in [('before_manifest.json',manifest),('protected_manifest.json',protected)]:
    with (report/name).open('x',encoding='utf-8') as f:json.dump(data,f,ensure_ascii=False,indent=2)
source={r['id']:r for r in (json.loads(x) for x in (project/'data/eval/master_gt_bilingual_multi_error_2000_20260929_r15.jsonl').read_text(encoding='utf-8').splitlines() if x.strip())}
old_records=json.loads((old/'guard_prior_audit.json').read_text(encoding='utf-8'))['records'];cases=[]
for r in old_records:
    if r['after_blocked'] and r['corpus']!='layout_diagnostic':
        g=source[r['id']];true_layout='keyboard_layout' in g.get('metadata',{}).get('behavior_tags',[])
        cases.append({'id':r['id'],'question':r['question'],'clean_question':g['clean_question'],'locale':g['locale'],'domain':g['domain'],'kind':'true_layout' if true_layout else 'false_rejection','expected_blocked':true_layout,'source_gold':g,'before_guard':r['after']})
assert len(cases)==36 and sum(c['expected_blocked'] for c in cases)==5
from app.core.runtime_input_quality_guard import RuntimeInputQualityGuard
guard=RuntimeInputQualityGuard.from_environment();guard.mode='enforce';guard.repeat_policy='warn_and_continue'
for c in cases:c['before_full_features']=guard.inspect(c['question']).features.to_dict()
with (report/'blocked36_fixture.json').open('x',encoding='utf-8') as f:json.dump({'scope':'31 source-labelled ordinary noisy inputs and 5 deliberate layout controls; guard outcome only, not answer correctness','cases':cases},f,ensure_ascii=False,indent=2)
flow='''# Flow r29 — ตรวจ input guard จากบริบทและหลักฐานราย span

## เป้าหมายและข้อจำกัด

แก้ false rejection 31 ข้อ โดยรักษา true-layout controls 5 ข้อ ไม่ปิด guard ไม่เพิ่ม alias ทั้งประโยค ไม่แก้ Gold/ต้นฉบับ/นโยบาย. การผ่าน guard ไม่ใช่คำตอบถูก ต้องตรวจ route/คำตอบแยกหลังปลดการหยุด. เว็บใช้อยู่ r28 บน8090จนกว่ารุ่นใหม่จะผ่าน actual HTTP

## ขั้นตอน

1. Freeze 36 cases จากชุดเก่า พร้อม clean/noisy/metadata/expected outcome และ features/span/raw mapping/score ทั้งหมด. แยก keyboard_layout tags ก่อนถือว่าเป็น false rejection
2. วิเคราะห์ทุก source span: normalization ลบเลข/เครื่องหมายจาก mapped candidate จนเหลือ 1–2 ตัวอักษรหรือไม่, target_quality ดีกว่า source จริงหรือไม่, มี lexical neighbor ของคำอังกฤษในบริบทประโยคหรือไม่
3. ลดหลักฐาน layout ที่อ่อน: mapped English ต้องมีรูปแบบภาษาอังกฤษพอ, source ที่แข็งแรงกว่า mapping ไม่ใช่หลักฐานการแก้, Thai span ที่อ่านได้และ mapped target ไม่ใช่คำอังกฤษต้องไม่ตัดสินทั้งประโยคจาก ngram อย่างเดียว
4. ให้ alphabetic English typo ที่มี lexical neighbor 1 edit (รวม transpose) และมี English context หลายคำผ่านได้. ไม่แก้ input ที่ส่งเข้าระบบ; ไม่ให้ short fragments/ตัวเลข/ชื่อ/negation เปลี่ยนค่า. Diagnostic ต้องแสดงเหตุผล lexical context
5. ประกาศ controls เพิ่มจากข้อความใหม่และ projection แป้นสองทิศทาง, clean sentences, names, codes, dates/numbers. แยก development หลังดู failuresออกจาก untouched regressions; ไม่สร้าง expectationsจากผล runtime
6. รัน guard 36 + regression4,280 + controls; บันทึก false reject และ layout detection แยก. ตรวจ end-to-end กลุ่ม31กับ source/clean answersและ fixture booking; ข้อผิดที่ยังเหลือแยกguard/recovery/route/retrieval/contract
7. Unit/competition regression/APIจริง: pipeline direct ไม่ผ่านเว็บ guard. สร้าง package ใหม่หลัง freezecode, รันชุดทีละชุด, เปลี่ยน8090เมื่อผ่านและเก็บแพ็กเกจ/logsเดิม. ตรวจ Gold/source hashesสุดท้าย
8. รายงานอะไรแก้ได้ อะไรไม่แก้ สิ่งที่รอเจ้าของยังอ้างแบบเดิม; ไม่เอา guard-pass ไปนับเป็น booked/free ถูกต้องหรือ owner policy approval

## การรับผล

31 ordinary noisy inputs ไม่ถูก block, 5 deliberate layouts ยังตรวจพบ. ไม่มี newly blocked ใน competition regressionsและ valid heldout controls. ยอมรับว่า short/mixed ambiguous fragmentsอาจให้ downstreamถามกลับ; ไม่เพิ่มความมั่นใจจาก scorengramโดยเดา. การตัดสิน thresholdต้องรายงาน tradeoffกับ controls
'''
with (project/'docs/129_input_guard_context_r29_flow_20261002.md').open('x',encoding='utf-8') as f:f.write(flow)
with (report/'flow_initial.md').open('x',encoding='utf-8') as f:f.write(flow)
status=subprocess.run(['git','-c','safe.directory=C:/Users/Chokhun/Downloads/Learn-LLM','--no-optional-locks','status','--short'],cwd=project,capture_output=True,text=True,encoding='utf-8',check=True).stdout
with (report/'git_status_before.txt').open('x',encoding='utf-8') as f:f.write(status)
print(json.dumps({'report':str(report),'false_rejections':31,'true_layout_controls':5},ensure_ascii=False))
