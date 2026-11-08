"""Publish final human-readable evidence after the completed analysis gates."""
import hashlib,json,time
from pathlib import Path
R=Path(__file__).resolve().parent
def load(n):return json.loads((R/n).read_text('utf-8-sig'))
def link(n,label=None):return f'[{label or n}]({(R/n).resolve().as_posix()})'
assert load('REQUEST_COMPLETION.json')['requested_detailed_diagnosis_then_ten_percent_sample_complete']
scores=load('SCORES.json');audit=load('MODEL_AND_MECHANISM_AUDIT.json');rep=load('ALL_REVIEWED_CASE_REPRODUCTION.json');strict=load('STRICT_ONLY_CHANGES_REVIEW.json')
assert strict['changed_grade_identities']==9
assert all(x['answer_identical'] and set(x['before_failures']+x['after_failures'])=={'latency_ceiling'} for x in strict['changes'])
original=R/'SAMPLE10_SCORE_TABLES_INITIAL_TH.md'
if not original.exists():original.write_bytes((R/'SAMPLE10_FINAL_REPORT_TH.md').read_bytes())
out=['# ผลข้อ2ละเอียดและทดสอบ10%ทุกหมวด — R131','',
 'งานวินิจฉัยและชุดทดสอบที่ผู้ใช้สั่งเสร็จแล้ว **2,111 unique request keys / 5,584 grade identities** ครบทุกตัว ไม่มีขาดหรือซ้ำ ใช้คำถามเดิมจาก Full ทั้ง14หมวด ปัดขึ้น10%ราย stratum และเติมตามหมวดของ input โดยเลือกก่อนรันและไม่ใช้ผลคะแนนเลือกคำถาม','',
 '**คำตอบทั้ง2,111ข้อเหมือน saved R130 เดิมทุกข้อ** รอบนี้ไม่มีการแก้ runtime หรือฝึกโมเดลใหม่ จึงเป็นหลักฐานการเกิดซ้ำของปัญหา ไม่ใช่ผลคุณภาพดีขึ้นหลังแก้ Flow','',
 'วินิจฉัยก่อนเริ่มทดสอบ: อ่านกลไกจาก raw เดิมครบ20,554คำถาม/55,811เกณฑ์ และตรวจ source/trace รายกรณี72ข้อก่อนเปิด gate ระหว่างรอผลตรวจเพิ่มรวม167 unique keys ที่อ่าน source รายกรณีหรือทดลอง reader เฉพาะในหน่วยความจำ ยืนยันตัวอย่างผิดเรื่อง/ผิดขอบเขต/ตอบขาด117 keys ตัวอย่างนี้เลือกเพื่อวินิจฉัย จึงไม่ใช้คำนวณ accuracy หรือแทนจำนวนผิดทั้งหมด อีก20,387 keys ยังไม่ตัดสิน semantic รายข้อ','',
 f"ใน sample มี{rep['source_reviewed_keys_in_sample']}keys ตรงกับทะเบียนตรวจ source และคำตอบเกิดซ้ำครบ{rep['identical_answer_count']}keys รวมตัวอย่างปัญหาที่เคยยืนยัน{rep['confirmed_failure_examples_reproduced']}keys ดู"+link('ALL_REVIEWED_CASE_REPRODUCTION.json'),'',
 '## คะแนนตามภาษาที่ร้องขอ','',
 'Strict รวมข้อกำหนด route/intent/mode/source/ข้อความ/เวลา ตาม grader เดิม Positive literal ตรวจเพียงข้อกำหนดข้อความด้านบวกที่มีอยู่ ทั้งสองค่า **ไม่ใช่ semantic accuracy** ตารางใช้ denominator เดียวกันในแต่ละภาษา; unassessed ของ baseline เก็บอยู่ใน denominator ไม่ตัดทิ้ง','',
 '| ผลที่บันทึก/รันใหม่ | ภาษา | Strict ผ่าน/ทั้งหมด | Positive literal ผ่าน/eligible | Literal% | Unassessed |',
 '|---|---|---:|---:|---:|---:|']
for arm in ['R64_saved','R95_saved','R130_saved','R130_repeat_10pct']:
 for loc in ['th','en','auto']:
  c=scores['by_requested_locale'][arm][loc]
  out.append(f"| {arm} | {loc} | {c['strict_passed']}/{c['grades']} ({c['strict_percent']:.2f}%) | {c.get('literal_passed',0)}/{c['literal_eligible']} | {c['literal_percent_fixed_denominator']:.2f}% | {c.get('literal_unassessed',0)} |")
out+=['',
 'Strict ของ repeat ต่างจาก saved R130 จำนวน9 grade identities: 5เปลี่ยนเป็นผ่านและ4เปลี่ยนเป็นไม่ผ่าน ทุกข้อแตกต่างเพียง latency_ceiling และคำตอบเหมือนเดิม จึงไม่อ้าง semantic ดีขึ้น/แย่ลงจากความต่างคะแนนนี้ ดู'+link('STRICT_ONLY_CHANGES_REVIEW.json'),'',
 '## ทุกหมวดตาม input','',
 'หมวดเป็น metadata เพื่อเลือกและรายงาน coverage ไม่ใช่คำตัดสินว่า planner ตี intent ถูก คำถามเดียวอยู่หลายหมวดได้ จึงบวกจำนวนแต่ละแถวเป็น unique total ไม่ได้','',
 '| หมวด | ประชากรเดิม | เลือก/รันครบ | Strict% | Positive literal ผ่าน/eligible | Literal% |',
 '|---|---:|---:|---:|---:|---:|']
for a in load('SAMPLE_ALLOCATION.json')['categories']:
 c=scores['by_input_category_overlapping']['R130_repeat_10pct'][a['category']]
 pct=f"{c['literal_percent_fixed_denominator']:.2f}%" if c['literal_percent_fixed_denominator'] is not None else 'ไม่มีเกณฑ์ด้านบวก'
 out.append(f"| {a['category']} {a['name_th']} | {a.get('population',a.get('population_keys','ดู SAMPLE_ALLOCATION'))} | {c['requests']} | {c['strict_percent']:.2f}% | {c.get('literal_passed',0)}/{c['literal_eligible']} | {pct} |")
out+=['',
 '**ข้อจำกัดหมวด:** C07 มีประชากรเดิม6คำถาม เลือก1 ส่วนใหญ่เป็น offsite จึงยังไม่ครอบคลุม rental onsite ทุก operation; C14 ไม่มี source ข่าวจริง และผล literal100% ของหมวดเล็ก เช่น C09 ไม่ยืนยัน semantic ถูก100%','',
 '## การยืนยันการรันและกลไก','',
 '- ตรวจ frozen files2,371ไฟล์และ logical source digest ก่อน/หลังผ่าน รวม source/input/code/prompt/weights ข้อมูลต้นฉบับและ approvals ไม่เปลี่ยน',
 '- ตรวจ returned provenance ของ model calls ที่สำเร็จ30ครั้ง: retained24/base6 ไม่มี profile/adapter/base revision/messages/schema/stage/precision/model mismatch',
 '- Actual base: typhoon-ai/typhoon2.5-qwen3-4b; alias psu-r129:latest; HF NF4 double quant BF16; context ใช้ retained R121 adapter ส่วน selector/generic ใช้ base ไม่ promote new adapter ที่ไม่ผ่าน critical review',
 '- Model HTTP attempts54 / transport successes30 / ไม่สำเร็จ24 events จำนวน requests ไม่เท่าจำนวน events และ HTTPสำเร็จไม่ได้แปลว่าคำตอบถูก',
 '- พบ admission denial926 requests, schema/version rejection25 requests และ gateway transport failure22 requests เป็นจำนวนกลไกที่เกิดซ้ำ กลุ่มซ้อนทับและบางข้อถูก typed reader กู้ได้ จึงไม่รวมเป็น semantic failures',
 f"- Median{audit['latency']['median_sec']:.3f}s / P95{audit['latency']['p95_sec']:.3f}s / P99{audit['latency']['p99_sec']:.3f}s / max{audit['latency']['max_sec']:.3f}s; {audit['latency']['above_20_sec']}requests เกิน20s",'',
 'Live ใช้ controlled unavailable fixture จึงไม่ใช่คำยืนยันสถานะ provider จริง การเทียบ saved R64/R95 มี source/backend/precision/clock/deadline confounds ไม่มี baseline inference/regrading ใหม่ และไม่อ้าง causal Flow effect ระหว่าง sample มี offline forensic work ร่วมบางช่วง จึงไม่อ้าง performance effect แบบควบคุมจากเวลาต่างกัน','',
 '## สาเหตุและลำดับแก้','',
 'ต้นเหตุที่ยืนยันได้รวมการผูก entity ไทยผิด, event scope หาย, verifier ปฏิเสธ clause ที่มีสาระเพราะข้อความเท่ากับ heading, reader ตอบชื่อเอกสารแทนรูปแบบแข่งขัน และ need บางส่วนหาย ปัญหาเหล่านี้หลายข้อเกิดก่อนเรียกโมเดลหรือที่ reader/verifier จึงยังไม่มีเหตุผลให้ฝึก weights เพิ่มแทนการแก้จุดเหล่านี้','',
 '- '+link('ITEM02_FINAL_REGISTER_TH.md','ทะเบียน15ต้นเหตุ พร้อมผลกระทบและเกณฑ์แก้'),
 '- '+link('ITEM02_DETAILED_DIAGNOSIS_TH.md','รายงานข้อ2ละเอียดที่เสร็จก่อนเริ่มเทส'),
 '- '+link('CONSOLIDATED_SOURCE_REVIEW.json','หลักฐานรายกรณี167keys พร้อม source/trace/คำตัดสิน'),
 '- '+link('REPAIR_ACCEPTANCE_PLAN_TH.md','ลำดับแก้และเกณฑ์ตรวจรับ'),'',
 '## สิ่งที่ยังไม่ปิด','',
 'งานข้อ2และsampleเสร็จ แต่ยังไม่มี runtime fixes และยังไม่ปิด semantic acceptance ของ Flow ทั้ง76requirements/14หมวด คงข้อที่ยังตัดสินไม่ได้เป็น review_required ห้ามอ่านคะแนน literal เป็นความถูกต้องทางความหมาย Candidateยังไม่ติดตั้งทับR78','',
 '## หลักฐานการตรวจรับรอบนี้','']
out += ['- '+link(n) for n in ['DIAGNOSIS_PRETEST_COMPLETE.json','SELECTION_FREEZE.json','EXECUTION_COMPLETE.json','COVERAGE.json','SCORES.json','MODEL_AND_MECHANISM_AUDIT.json','CHANGED_ANSWER_REVIEW.json','REQUIREMENTS_SCOPE_PRESERVATION.json','REQUEST_COMPLETION.json']]
(R/'SAMPLE10_FINAL_REPORT_TH.md').write_text('\n'.join(out)+'\n','utf8')
registry=R/'ITEM02_FINAL_REGISTER_TH.md'
t=registry.read_text('utf8').replace('ไม่มีการแก้ Flow ระหว่างการทดสอบย่อยที่กำลังทำ','ไม่มีการแก้ Flow ระหว่างการทดสอบย่อยรอบนี้').replace('ต้องรอผลครบและตรวจคำตอบที่เปลี่ยนก่อนสรุป','ผลครบแล้ว2111keys/5584grades คำตอบเหมือนsavedR130ทุกข้อ; strictต่าง9grade identitiesเฉพาะlatency ดูSAMPLE10_FINAL_REPORT_TH.md และSTRICT_ONLY_CHANGES_REVIEW.json')
registry.write_text(t,'utf8')
handoff=['# R131 — งานข้อ2ละเอียดและsample10%เสร็จ','',
 'ผู้ใช้สั่งข้อ2แบบละเอียดก่อนแล้วเทส10%ทุกหมวด ไม่มีsubagents ไม่แก้frozenR130/source/approvals/prompt/weights/logเดิม','',
 'เสร็จแล้ว: diagnosisก่อนgate72sourcecases, เพิ่มระหว่างรอรวม167unique reviewed/probed keys/117confirmed content-scope-omission examples ไม่ใช่accuracy ทุก20554keysมีmechanismledger อีก20387keysยังไม่ตัดสินsemanticรายข้อ','',
 'Sample2111keys/5584grade identitiesครบ ไม่มีขาด/ซ้ำ ไม่มีexceptions ตรวจhash2371files/logicalsource/modelhealthก่อนหลังผ่าน gateway54attempts/30success provenanceverified24retained6base คำตอบทุก2111keysเหมือนsavedR130 strictต่าง9identitiesเพราะlatencyอย่างเดียว literalเหมือนเดิมทั้งหมด','',
 'Sourcecasesที่อยู่sample16keysเหมือนเดิมครบ มี13confirmed failure examplesเกิดซ้ำ งานวินิจฉัยและsampleเสร็จ แต่Flowqualityacceptanceยังไม่เสร็จ/ไม่มีruntimefix/ไม่มีpromoteadapter/ไม่ติดตั้งR78','',
 'อ่าน ITEM02_FINAL_REGISTER_TH.md / SAMPLE10_FINAL_REPORT_TH.md / REPAIR_ACCEPTANCE_PLAN_TH.md / REQUEST_COMPLETION.json / CONSOLIDATED_SOURCE_REVIEW.json','',
 'ไม่ต้องรันsampleซ้ำ ไม่สร้างheartbeat งานทดสอบตามคำสั่งนี้เสร็จแล้ว หากผู้ใช้สั่งแก้ให้ทำcandidateถัดไป ไม่แก้R130หรือผลR131เดิม ขอบเขต76requirements/14หมวดคงเดิมตามREQUIREMENTS_SCOPE_PRESERVATION.json','',
 'C07population6sample1ส่วนใหญ่offsite ไม่ครอบคลุมrentalonsiteทุกoperation; C14ไม่มีsourceข่าวจริง คะแนนstrict/literalไม่ใช่semanticaccuracy baselineใช้savedR64/R95/R130เท่านั้นมีconfounds ห้ามอ้างcausalFloweffect','',
 'Controller18956/child35784จบแล้วก่อนanalysis โมเดล42136port12921และAPI37576port13024เป็นprocessเดิม ตรวจPID/commandlineจริงก่อนเปลี่ยน การจบsampleไม่ใช่การหยุดmodeldaemon','',
 'finalize_review.pyเคยผิดที่ถือว่าทุกrequirementมีsha256 ทั้งที่14categoryentriesไม่มี แก้ให้เก็บNoneและแยกcopied_definition_text_sha256แล้ว finalizeสำเร็จ ไม่มีtest/modelrequestเพิ่ม ไม่แก้parenttraceability']
(R/'CURRENT_HANDOFF_TH.md').write_text('\n'.join(handoff)+'\n','utf8')
manifest={n:hashlib.sha256((R/n).read_bytes()).hexdigest() for n in ['ITEM02_FINAL_REGISTER_TH.md','ITEM02_DETAILED_DIAGNOSIS_TH.md','SAMPLE10_FINAL_REPORT_TH.md','CONSOLIDATED_SOURCE_REVIEW.json','REPAIR_ACCEPTANCE_PLAN_TH.md','REQUEST_COMPLETION.json','STRICT_ONLY_CHANGES_REVIEW.json']}
(R/'FINAL_DELIVERY_MANIFEST.json').write_text(json.dumps({'complete':True,'files':manifest,'published_at':time.time()},indent=2),'utf8')
print(json.dumps({'published':True,'strict_changes_all_latency_only':True,'reviewed_sample':16,'confirmed_examples_reproduced':13},ensure_ascii=False))
