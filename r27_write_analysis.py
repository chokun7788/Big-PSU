import json,hashlib,re
from collections import Counter
from r27_fixture import PROJECT,REPORT

def read(name):return [json.loads(x) for x in (REPORT/name).read_text(encoding='utf-8').splitlines() if x.strip()]
fixture=json.loads((REPORT/'content_contract_fixture_v2.json').read_text(encoding='utf-8'))['cases'];contracts={c['id']:c for c in fixture}
baseline=read('baseline_r26_details.jsonl');final=read('final_G_details.jsonl')
new_before=read('new_A_details.jsonl');new_after=read('final_new_C_details.jsonl')
groups=Counter()
for r in baseline:
    if r['passed']:continue
    for failure in r['failures']:groups[failure.split(':',1)[0]]+=1
audit={'baseline_fixture_version':'v1 (preserved)','acceptance_fixture_version':'v2','changed_contracts':[],'equivalent_English_variants_not_semantic_failures':['valorant-checkin-en','valorant-new-content-en','valorant-emergency-en'],'note':'v1 literal assertions can reject another valid hash-approved English wording; raw 165/320 must not be presented as a measured universal semantic accuracy rate'}
v1=json.loads((REPORT/'content_contract_fixture.json').read_text(encoding='utf-8'))['cases']
for old,new in zip(v1,fixture):
    if old['required_clauses']!=new['required_clauses']:audit['changed_contracts'].append({'id':new['id'],'before':old['required_clauses'],'after':new['required_clauses'],'reason':'split numbered clauses whose final outline dot is optional; do not require a heading as part of the normative statement'})
with (REPORT/'oracle_revision_audit.json').open('x',encoding='utf-8') as f:json.dump(audit,f,ensure_ascii=False,indent=2)

causes=[
('P0','เลือกข้อกฎย่อยไม่ตรงคำถาม','devices, notes, own/provided equipment, hero/skin, roster change','facet กว้างกับคำว่า game/team/equipment มีคะแนน แต่ไม่ได้แยก proposition; guard จึงอาจยอมรับเรื่องข้างเคียงหรือปฏิเสธว่าไม่มีข้อมูล','เลือก clause จาก rulebook เดียวตามแนวคิดย่อย และตรวจ source hash สำหรับอังกฤษ'),
('P0','ตัดเงื่อนไขและรายการไม่ครบ','RoV rematch/overheating/long pause, VALORANT rollback, Tekken settings','window และจำนวน clause ที่แสดงมีขีดจำกัด; ข้อห้าม/เว้นแต่/Stage/Advantage ถูกตัดจากท้ายแม้เอกสารมี','รักษา clause เต็มและรับทุก clause ที่ผูกกับ proposition; test ต้องตรวจทุกเงื่อนไขและหน่วย'),
('P0','การแก้คำเปลี่ยนคำที่ถูกเป็นความหมายอื่น','score → scope','บริบท tournament ทำให้ scope เป็นผู้สมัครของ edit distance แต่ score ไม่อยู่ในรายการคำจริงที่ป้องกันไว้','ป้องกัน score/scores และทดสอบคำจริง scope, ชื่อเกม ตัวเลข และ negation'),
('P1','ประโยคแรกไม่ตรง แม้รายละเอียดมีคำตอบ','overtime timeout, source scope, notes, heroes','เรียงจาก chunk/heading หรือค่าแรกของ subtype ไม่ได้เรียงจาก proposition ที่ถาม','first-line contract แยกจากการมีเนื้อหาที่ส่วน Details'),
('P1','คำสำคัญพิมพ์ขาดแล้วไม่ได้เข้า facet','ประท้วง/โน้ต/โซเชียล/ฮีโร่, protest/notes/heroes/settings/score','ตัวกู้คำเดิมเน้น task vocabulary จึงกู้ tournament ได้แต่ไม่กู้ proposition word; fallback กลายเป็น overview หรือข้ออื่น','OSA edit distance 1 พร้อม registered game และ independent syntax/context anchor; จำกัด span/edit budget เดิม ไม่มี whole-question alias'),
('P1','worker เปลี่ยนทุก 250 คำถามทำให้ 503','HTTP candidate และ sequential จบไม่ครบ','Start-PSU-Esports-Chatbot.ps1 ตั้ง recycle=250, queue wait=3s; supervisor ฆ่าตัวเดิมและเริ่มตัวใหม่ทันที ก่อน ready จึงไม่มี worker รับงาน ไม่ใช่ข้อกฎผิด','เตรียม replacement ขณะตัวเดิมยังทำงาน สลับหลัง ready; cleanup spare เมื่อ failure/shutdown และไม่รับ stale slot'),
('P2','Grader เก่าปฏิเสธ clause อังกฤษสั้น','30 Tekken equipment +17 VALORANT penalty','กรองเฉพาะ modal/ตัวเลขและ window 7 tokens; 5-token PS5 clause กับ penalty definitions บางข้อไม่ผ่าน','atomic complete-clause presence; คงคะแนนดิบและ gates อื่น; completeness แยกใช้ fixture'),
('P2','คำถามไม่ระบุเกมเสียเวลาผ่านโมเดลก่อนถามกลับ','TH/EN tournament rules without target','การตรวจ target เดิมอยู่หลัง semantic/intent route; การถามกลับไม่ต้องเรียกโมเดลเหล่านี้','ย้าย guard มาไว้หลัง preprocess/explicit competition signal ก่อนโมเดล; ไม่เรียก RAG หรือ booking เพื่อเดาเกม'),
]
lines=['# วิเคราะห์ r27: สาเหตุ คำตอบที่ควรได้ และการแก้','',f'หลักฐานอยู่ใน `{REPORT}`','', '## ระดับของผล','', '- 2,000 ข้อ: route/status/evidence/source presence; ไม่ใช่ตรวจทุก proposition ทุกคำตอบ','- 320 ข้อ: 104 ประเด็นไทย/อังกฤษ ×3 รูปคำถาม +8 controls; literal clause completeness และ first line','- 128 ข้อ: 16 ประเด็น ×2 ภาษา ×4 รูปแบบใหม่/พิมพ์เบิ้ล/ผิดหลายส่วน/พิมพ์ขาด เป็น development cases หลังตรวจแล้ว ไม่ใช่ blind field data','- ข้อกำหนดที่ผู้จัดไม่ได้รับรองแยกจากผลอัตโนมัติ','', '## ลำดับแก้ตามความรุนแรง','', '| ระดับ | ปัญหา | ตัวอย่าง | สาเหตุ | วิธีแก้ |','| --- | --- | --- | --- | --- |']
lines.extend('| '+' | '.join(row)+' |' for row in causes)
lines += ['', '## คะแนนและเหตุที่เลือกคำตอบ','', '- ค่า confidence 0.97 ของเส้นทางใหม่หมายถึงการตัดสินเส้นทางแบบขอบเขตจำกัด ไม่ใช่โอกาส 97% ที่ทุกข้อกฎถูก','- เส้นทางใหม่ต้องเป็นเกมเดียวที่ลงทะเบียนและมี competition signal; คำถามไม่รู้จักยังผ่าน pipeline เดิม','- แนวคิดย่อยใช้คำทั่วไปของหัวข้อ (ไม่ใช้ ID คำถามหรือข้อความ Gold) จับ clause เต็มใน source; ถ้าหลาย chunk มีข้อความตรง เลือก chunk ที่รองรับ clause ในแนวคิดนั้นมากกว่า','- เนื้อหาคำตอบไม่ได้สร้างจากคะแนนหรือจาก LLM: ใช้ต้นฉบับหรือ English overlay ที่ hash ผ่าน พร้อม source ID ใน trace','- รูปแบบเดิมมี retrieval/facet score แต่ source heading และหัวข้อกว้างไม่ได้พิสูจน์ proposition เช่น time allowance กับ pause reason','- การรวม eligibility/roster/registration ต้องรวมทุกเรื่องที่ถาม; full run A จับ regression นี้และแก้ก่อน run B','', '## Oracle ที่ตรวจแก้เอง','', '- เก็บ fixture v1 กับผลดิบไว้; v2 แยก numbered clause ที่ไม่มีจุดท้ายออกจาก heading ให้ถูก','- EN check-in/new content/emergency มีคำแปลหลาย chunk ที่มีความหมายเทียบกันได้; การไม่ตรง literal ใน v1 ไม่ใช่หลักฐาน semantic wrong ทุกเคส','- ไม่แก้ Gold เดิมเพื่อเพิ่มคะแนน: กรณี 47 fails ใช้ source-presence grade อีกช่อง','', '## หลักฐานต่อประเด็นที่ baseline ไม่ผ่าน','']
seen=set()
for r in baseline:
    if r['passed'] or r['anchor'] in seen:continue
    seen.add(r['anchor']);c=contracts[r['id']]
    lines += ['### '+r['anchor'],'', '**คำถาม:** '+r['question'],'','**คำตอบเดิม:**','```text',r['response']['answer'],'```','', '**ข้อที่ตัวตรวจรายงาน:** '+', '.join(x.split(':',1)[0] for x in r['failures']),'', '**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**']
    lines.extend('- '+clause for clause in c['required_clauses'])
    lines += ['',f'อ้างอิง `{c.get("source_id")}`; source hash `{c.get("source_sha256")}`','']
    selected=[t for t in r['response'].get('trace',[]) if t['stage'] in ('competition_source_grounding','competition_overview','universal_intent','competition_target_guard','competition_evidence_coverage')]
    if selected:lines += ['**เหตุการณ์จาก trace:**','```json',json.dumps(selected,ensure_ascii=False,indent=2),'```','']
    after=next(x for x in final if x['id']==r['id']);lines += ['**หลังแก้:** '+('ผ่าน contract' if after['passed'] else 'ยังไม่ผ่าน')+'; mode '+after['response']['mode'],'']
lines += ['## ขอบเขตที่ยังรอ / ไม่อ้างว่าปิดปัญหาแล้ว','', '- Tekken s03 กับ s07 ขัดเรื่อง pause: ให้ผู้จัดยืนยันว่า s07 เป็นข้อยกเว้นหรือไม่ ต้องขอกรรมการก่อนอย่างไร และโทษเป็น Round/Game/FT2 Match','- V2 104 รายการยัง pending review; ไม่ publish และไม่เปลี่ยน owner schedule','- EN overlay ตรวจ source ได้ ไม่ใช่การรับรองอย่างเป็นทางการของผู้จัด','- คำถามรูปแบบใหม่และคำพิมพ์ผิดนอก vocab/budget ยังอาจต้อง clarification; ไม่มีผล field traffic ที่ยืนยันความครอบคลุม','- one local worker ยังมี bounded admission queue; การแก้ planned recycle ไม่ได้ยืนยัน SLA หลายผู้ใช้/งาน LLM พร้อมกัน','- r26 timeout 719s ไม่เกิดใน full r27 B; timing ใหม่วัด locale/cue/canonical/entry-to-split ได้ แต่ยังไม่ได้พิสูจน์ว่า timeout เก่าเกิดจาก worker recycle','']
with (REPORT/'CAUSE_ANALYSIS_TH.md').open('x',encoding='utf-8') as f:f.write('\n'.join(lines))
print(json.dumps({'baseline':len(baseline),'baseline_passed':sum(r['passed'] for r in baseline),'failures':dict(groups),'anchors_reviewed':len(seen),'new_before_passed':sum(r['passed'] for r in new_before),'new_after_passed':sum(r['passed'] for r in new_after),'oracle_changes':len(audit['changed_contracts'])},ensure_ascii=False))
