"""Assemble the final report from completed, saved native HTTP runs only."""
import collections,hashlib,json,re,sqlite3
from pathlib import Path
from datetime import datetime
from regrade_saved import collect
R=Path(__file__).resolve().parent;B=R/'runs/http01';A=R/'runs/http03'
def read(p):return json.loads(p.read_text('utf8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rows(p):return {x['question_id']:x for x in map(json.loads,p.read_text('utf8').splitlines())}
def pct(n,d):return f'{n/d*100:.2f}%' if d else 'N/A'
bc=read(B/'TEST_COMPLETE.json');ac=read(A/'TEST_COMPLETE.json')
assert all(c['complete'] and c['unique_question_keys']==1400 and c['source_code_inputs_unchanged'] and c['model_identity_verified'] for c in [bc,ac])
b=rows(B/'RESULTS.jsonl');a=rows(A/'RESULTS.jsonl');assert b.keys()==a.keys() and len(a)==1400
bg={k:v['grade_v2'] for k,v in rows(B/'review_v2/ALL_REVIEWED.jsonl').items()};ag={k:v['grade_v2'] for k,v in rows(A/'review_v2/ALL_REVIEWED.jsonl').items()}
bs=read(B/'review_v2/SUMMARY.json')['groups'];as_=read(A/'review_v2/SUMMARY.json')['groups']
jobs={j['id']:j for j in map(json.loads,(R/'EXISTING_QUESTIONS_1400.jsonl').read_text('utf8').splitlines())}
expect={j['id']:j for j in read(R/'NATIVE_EXPECTATIONS.json')['questions']}
ref=read(R/'NATIVE_SOURCE_REFERENCE.json');facts={f['id']:f for f in ref['facts']}
originals=read(R/'REFERENCE_HASHES.json');original_changes=[p for p,h in originals.items() if sha(Path(p))!=h];assert not original_changes
assert sha(R/'EXISTING_QUESTIONS_1400.jsonl')==read(R/'QUESTION_MANIFEST.json')['sha256']
for k in a:assert a[k]['question']==b[k]['question']==jobs[k]['question'] and a[k]['locale']==b[k]['locale']==jobs[k]['locale']
db=R/'system/data/knowledge/common.sqlite'
with sqlite3.connect(db.as_uri()+'?mode=ro',uri=True) as c:
    state={'approvals':c.execute('select count(*) from cc_approvals').fetchone()[0],
       'draft_records':c.execute('select count(*) from cc_heads where withdrawn=0').fetchone()[0],
       'withdrawn_records':c.execute('select count(*) from cc_heads where withdrawn!=0').fetchone()[0],
       'active_release':c.execute("select value from cc_meta where key='active'").fetchone()[0],
       'published_releases':c.execute('select count(*) from cc_releases').fetchone()[0]}
assert state['approvals']==0 and not state['active_release'] and state['published_releases']==0
assert sha(db)==read(B/'RUN_FREEZE.json')['files'][str(db)]==read(A/'RUN_FREEZE.json')['files'][str(db)]
fixture={k for k in a if ag[k]['fixture_only_goal']};assert len(fixture)==160
fixture_claims_before=[k for k in fixture if collect(b[k]['response'])];fixture_claims_after=[k for k in fixture if collect(a[k]['response'])]
assert not fixture_claims_after,fixture_claims_after
negative={k for k in a if not expect[k]['goals']};positive=set(a)-fixture-negative
assert len(negative)==280 and len(positive)==960
negative_claims_after=[k for k in negative if collect(a[k]['response'])];assert not negative_claims_after,negative_claims_after
missing_positive=[k for k in positive if ag[k]['matched_claims']!=ag[k]['expected_claims']]
changes={'improved_strict':[k for k in a if ag[k]['passed'] and not bg[k]['passed']],
         'regressed_strict':[k for k in a if bg[k]['passed'] and not ag[k]['passed']],
         'positive_missing_goals_after':missing_positive,'fixture_factual_substitution_before':sorted(fixture_claims_before),
         'fixture_factual_substitution_after':fixture_claims_after,'negative_factual_substitution_after':negative_claims_after}
partial_regressions=[k for k in changes['regressed_strict'] if k.startswith('C11') and ag[k]['content_exact'] and ag[k]['actual_status']=='partial']
other_regressions=[k for k in changes['regressed_strict'] if k not in partial_regressions]
changes['calendar_answer_to_partial_with_complete_claims']=partial_regressions
changes['other_strict_regressions_requiring_review']=other_regressions
model={}
for name,run in [('before',B),('after',A)]:
    ev={e['id']:e for e in map(json.loads,(run/'MODEL_EVENTS.jsonl').read_text('utf8').splitlines())};c=collections.Counter()
    for e in ev.values():
        c['selector_events']+=1;c['http_attempted']+=bool(e.get('http_attempted'));c['transport_ok']+=e['transport_ok'];c['schema_ok']+=e['schema_ok'];c['identity_verified']+=bool(e.get('identity_verified'))
    model[name]=dict(c)
translation=[k for k,x in a.items() if (x['response'].get('language') or {}).get('effective')=='en' and 'A confirmed English translation is unavailable' in x['response'].get('answer','')]
tech={k for k,j in jobs.items() if re.search(r'(?<![a-z0-9])(?:migrated_rate_|rate_recovered_)',j['question'])}
integrity={'original_reference_files':len(originals),'original_files_unchanged':True,'source_database_unchanged':True,'questions_unchanged':True,
           'completed_runs':['http01','http03'],'aborted_run':read(R/'runs/http02/ABORTED.json'),'native_state':state,'model':model,'production_installed':False}
(R/'INTEGRITY_FINAL.json').write_text(json.dumps(integrity,ensure_ascii=False,indent=2),'utf8')
result={'complete':True,'new_questions':0,'unique_question_keys':1400,'before':bs['ALL'],'after':as_['ALL'],
        'positive_nonfixture':len(positive),'negative':len(negative),'fixture_goals':len(fixture),'changes':changes,'technical_questions':len(tech),
        'english_questions_retaining_untranslated_thai_clauses':len(translation),'model':model,'human_semantic_accuracy_claimed':False}
(R/'COMPARISON_FINAL.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),'utf8')

names={'C01':'ศูนย์/สถานที่/ติดต่อ','C02':'บุคลากร','C03':'อุปกรณ์','C04':'เกมและแค็ตตาล็อก','C05':'วิธีควบคุมเกม','C06':'ราคาปกติ','C07':'ราคาเหมา','C08':'การจองและขั้นตอน','C09':'ชำระเงิน/เอกสาร','C10':'กฎการใช้บริการ','C11':'ตารางเวลา','C12':'สถานะจองสด','C13':'กติกาการแข่งขัน','C14':'ข่าว/กิจกรรม'}
lines=['# R115 — ทำครบขั้น 1–3 และตรวจผ่านแชทจริง','','## สรุป','',
 'ตรวจ source เดิม → แก้โค้ดตามสาเหตุ → ตรวจคำถามเดิมผ่าน `/api/chat` จริง เปิด LLM และเลือกหมวดอัตโนมัติ ครบ 1,400 ข้อทั้งก่อนและหลังแก้ ไม่เพิ่มคำถาม ไม่รัน full 20,554 ไม่ติดตั้งทับ R78',
 '',f"- Positive ที่มี source จริงผ่าน strict: **{bs['ALL']['positive_nonfixture_pass']}/960 ({pct(bs['ALL']['positive_nonfixture_pass'],960)}) → {as_['ALL']['positive_nonfixture_pass']}/960 ({pct(as_['ALL']['positive_nonfixture_pass'],960)})**",
 f"- Positive ที่คืน goal claims ครบหลังแก้: {len(positive)-len(missing_positive)}/960 ข้อ เป็น source-claim coverage ไม่ใช่ human semantic accuracy",
 f"- Negative: {sum(ag[k]['passed'] for k in negative)}/280 ผ่าน strict; {sum(ag[k]['safe_abstention'] for k in negative)}/280 ไม่มี factual claim และตอบแบบไม่ยืนยัน",
 f"- Fixture positive 160 ข้อไม่มี fake live/news source ใน native: ยังตอบเนื้อหาเหล่านั้นไม่ได้ แต่คำตอบที่แทนด้วยข้อมูลผิดเรื่องลดจาก {len(fixture_claims_before)} ข้อเหลือ {len(fixture_claims_after)} ข้อ",
 f"- Strict ทั้ง corpus: {bs['ALL']['strict']}/1,400 ({pct(bs['ALL']['strict'],1400)}) → {as_['ALL']['strict']}/1,400 ({pct(as_['ALL']['strict'],1400)}) รวมข้อ fixture ที่ไม่มีข้อมูลไว้ ไม่ซ่อน coverage",
 f"- Strict เมื่อแยก 160 fixture goals ที่ไม่มี native source: {bs['ALL']['strict']}/1,240 ({pct(bs['ALL']['strict'],1240)}) → {as_['ALL']['strict']}/1,240 ({pct(as_['ALL']['strict'],1240)})",
 f"- Strict ดีขึ้น {len(changes['improved_strict'])} ข้อ; ถอยลง {len(changes['regressed_strict'])} ข้อ",
 f"- ในข้อที่ strict ลด มี {len(partial_regressions)} ข้อตารางเวลาที่คืน claims ครบแต่เปลี่ยนจาก answer เป็น partial ตามช่องว่างของ source; อีก {len(other_regressions)} ข้อต้อง review แยก ไม่ซ่อนการลดคะแนนไว้",
 '', 'ตัวเลขทั้งหมดเป็นการตรวจ source identity/value/state กับ expected ที่ freeze ก่อน HTTP ใช้ projection ร่วมในการจัด identity ไม่ใช่คะแนนความถูกต้องจากผู้ประเมินมนุษย์อิสระ และไม่ใช่หลักฐานว่าระบบพร้อม production ครบทุกเงื่อนไข',
 '', '## วิธีทดสอบและ lineage','',
 '- R113 เป็นแหล่งคำถามเดิมและ expected เดิม; R114 shared-engine เคยได้ 99.14% บน frozen read model จึงเทียบตรงกับ native API รอบนี้ไม่ได้ เพราะ source/fixture/adapter และเส้นทางการทำงานต่างกัน',
 '- Before = R114 candidate ที่คัดลอกแยกมาทดสอบใน R115, runs/http01; After = candidate R115, runs/http03 ใช้ DB เดิมที่ hash ตรงกัน',
 '- ไม่ใช้ category hint; ทุกข้อแยก session; เวลาอ้างอิงเดิม 2026-10-21T12:00:00+07:00; ไม่เรียก baseline เก่ามารันใหม่ด้วยข้อมูลคนละรุ่น',
 '- http02 หยุดโดยตั้งใจหลังวิเคราะห์ log พบช่องโหว่เพิ่ม ไม่ใช่ full run และไม่เอามาปนเป็นผลสำเร็จ เก็บ ABORTED.json, original raw log และสำเนาโค้ดที่ hash ตรงกับ RUN_FREEZE ครบ',
 '- 301 code checks ผ่าน โดยใช้ข้อความเดิม/ค่าคงที่เดิม และตรวจ source extension ใน memory ไม่มี HTTP/model เพิ่มในชุดนี้ ผลตรวจที่ไม่ผ่านระหว่างพัฒนาเก็บไว้ด้วย',
 '- review_v2 อ่านทั้ง domain fact_id packets และ compatibility record/field packets ตรวจ raw response เดิมทั้งสองรอบด้วยเกณฑ์เดียวกัน ไม่เขียนทับ original grades',
 '', '## ผลรายหมวด','', '| หมวด | Strict ก่อน /100 | Strict หลัง /100 | Positive มี source หลัง |','|---|---:|---:|---:|']
for cat in names:
    before=bs[cat];after=as_[cat];lines.append(f"| {cat} {names[cat]} | {before['strict']} | {after['strict']} | {after['positive_nonfixture_pass']}/{after['positive_nonfixture']} |")
lines+=['','C12/C14 มี positive fixture หมวดละ 80 ข้อและ negative หมวดละ 20 ข้อ การได้ strict เฉพาะ negative ไม่ใช่ความสามารถตอบ live/news positive ได้แล้ว',
 '', '## จุดที่แก้และความหมายของผล','',
 '1. **Identity แย่งคำถามชื่อบุคลากร**: จำกัดคำกว้างชื่ออะไรและแก้ regex ชื่อไทย ไม่ hardcode ชื่อคน',
 '2. **รหัส rate ถูกแยกเป็น staff/availability**: ผูก ID ทั้งรหัสกับ record ปัจจุบันก่อน route และจำกัด rate pool ตาม ID จริง แยก duration จาก money amount เมื่อถามเวลาเท่าไหร่',
 '3. **Predicate guard ถูกข้าม**: router และ reader ใช้ predicate frames ร่วมกัน ถามสิทธิ์บริษัท การถ่ายบุคคล คริปโต ประกัน ฯลฯ ต้องมี source ของ predicate นั้น ไม่ใช้ขั้นตอนจองหรือกฎใกล้เคียงแทน',
 '4. **FAQ ตารางกว้างกว่า field ที่ถาม**: อ่าน recorded period รายวันก่อน แสดงข้อจำกัดโซน/ช่วงมีผล/เวลาเปิดที่ขัดแย้ง ใช้ partial แทนการยืนยันสิทธิ์จองจริงเมื่อ source ยังไม่ครบ',
 '5. **Live request ถูกตอบด้วยข้อมูลเครื่อง**: ตรวจชื่อเครื่องพร้อมวันเวลาและการถามว่าจองได้หรือยังเป็น live task อ่าน resource binding จริงก่อน provider ไม่ใช้ static location/capacity แทนสถานะ',
 '6. **Unknown booking reference**: แยก missing source ของเลขจองจาก provider unavailable ไม่เลือกเครื่องหรือเลขจองข้างเคียง',
 '7. **Unknown event หลุดไปกติกาคนละงาน/เพจติดต่อ**: เมื่อ news reader ผูกกิจกรรมไม่ได้ ให้ปิดทาง fallback ข้ามเรื่อง พร้อม guard จำนวนทีมและข่าวสดที่ไม่มีหลักฐาน',
 '8. **คำแปลไม่ครบ**: แจ้งชัดก่อนแสดงย่อหน้าไทยในคำตอบอังกฤษ ไม่เรียกว่าคำแปลอังกฤษครบ',
 '9. **เครื่องมือตรวจมองไม่เห็น compatibility packets**: แก้ตัววิเคราะห์ offline แยก original grade จาก review_v2 และอ่านเนื้อหาจริงประกอบทุกกลุ่ม',
 '',f"มีคำถามรหัสเทคนิค {len(tech)} ข้อ: strict {sum(bg[k]['passed'] for k in tech)}/{len(tech)} → {sum(ag[k]['passed'] for k in tech)}/{len(tech)} ต้องแยกจากการตอบภาษาธรรมชาติ ไม่อ้างว่าเป็น generalization กับคำถามใหม่",
 '', '## สิ่งที่ยังไม่ถือว่าแก้ครบ','',
 '- **ตารางเวลา**: owner ยืนยันปิดวันธรรมดา 16:00–18:00 เท่านั้น; open_periods บางวัน conflicted, zone_ids และ effective dates ยัง unknown ไม่แก้ข้อมูลให้เป็นเปิดช่วงอื่นเอง คำตอบช่วงจองที่ partial จงใจคงความไม่แน่นอน แม้ oracle เก่าคาด answer',
 '- **VR**: คำยืนยันต่อคนถูกผูกกับ rates เดิมแล้ว แต่ไม่เพิ่มจำนวนคนที่ใช้ได้จริง ส่วนลด การปัดเศษ หรือเงื่อนไข eligibility โดยไม่มี source ไม่เปลี่ยนข้อมูลเพื่อให้เทสผ่าน',
 '- **C13 extra clauses 3 ข้อ**: มี summary และย่อหน้าหัวข้อเดียวกันจาก source ที่มีจริง คืน goal clauses ครบและมี source เพิ่ม เป็น granularity/overlap ของ oracle กับข้อมูล native ไม่ใช่หลักฐานว่าแต่งกฎ คง strict fail และตัวอย่างไว้',
 f'- **ภาษาอังกฤษ**: {len(translation)} คำถามอังกฤษยังมีบางย่อหน้าไทยที่ไม่มีคำแปลยืนยัน แม้ source claims ตรง expected จึงไม่ใช่คะแนนคุณภาพภาษาอังกฤษครบถ้วน',
 '- **สถานะจองจริง/ข่าวสด**: workload ไม่มี snapshot fixture เดิมใน native และ provider/binding ที่ใช้ได้จริงยังไม่ถูกยืนยัน ห้ามใช้ผล unavailable/missing_source มาสรุปว่ารู้สถานะว่างหรือข่าวล่าสุดจริง',
 '- **ข้อมูลเป็น draft**: ยังไม่มี approvals/release สำหรับ production; ใช้ migration preview เท่านั้น การเผยแพร่จริงต้องยืนยันข้อมูลและผ่านขั้นตอน owner ที่มีอยู่',
 '- **ความละเอียดของสเปก**: บาง equipment specifications มีเพียง zone/quantity; คืนค่าตาม source ได้ไม่ได้หมายความว่ามี CPU/RAM/ความละเอียดจอครบ ตัวอักษร boilerplate ในค่า structured ถูกย่อในการแสดงผล จึงมี literal-body flags ที่ต้องแยกจากข้อมูลผิด ทั้งหมดเก็บใน raw และรายละเอียดด้านล่าง',
 '', '## LLM และ transport','', '```json',json.dumps(model,ensure_ascii=False,indent=2),'```','',
 'ข้างบนเป็น domain evidence-selector events ที่มี id/transport/schema ใน log ไม่ใช่การอนุมานจำนวนเรียกโมเดลจากการเปิด toggle ทุกรอบเปิด LLM แต่ typed reader ตอบเองได้ก็ไม่จำเป็นต้องเรียก การส่ง HTTP สำเร็จ รูปแบบ model ถูก และคำตอบถูกต้องเป็นคนละเกณฑ์',
 f"- Actual chat HTTP หลังแก้: {sum(ag[k]['http_ok'] for k in ag)}/1,400; delivery validation {sum(ag[k]['validation_ok'] for k in ag)}/1,400",
 f"- Latency ก่อน: median {bc['latency_median_sec']:.3f}s, p95 {bc['latency_p95_sec']:.3f}s; หลัง: median {ac['latency_median_sec']:.3f}s, p95 {ac['latency_p95_sec']:.3f}s ไม่แยก causal effect จาก cache/สภาพเครื่องด้วย",
 '', '## ความครบถ้วนและไฟล์','',f"- Original references {len(originals)} ไฟล์ hash เดิมครบ; DB เดิม; input/expected ไม่เปลี่ยน; build/model identity ตรวจทั้งก่อนและหลัง", 
 '- source facts nonfixture 1,164 จับคู่ native ครบใน scope ที่ตรวจ ไม่ได้หมายความว่าครอบคลุมข้อมูลธุรกิจทุกหัวข้อที่อาจมีคนถาม',
 '```json',json.dumps(state,ensure_ascii=False,indent=2),'```','',
 '- [แผน Flow และเหตุผล](02_IMPLEMENTATION_FLOW_TH.md)',
 '- [ตรวจ source ก่อนรัน](01_SOURCE_REVIEW_TH.md)',
 '- [รายละเอียดข้อที่เคยไม่ผ่านและหลักฐานก่อน/หลัง](ROOT_CAUSE_REVIEW_TH.md)',
 '- [คะแนนเปรียบเทียบและรายชื่อเปลี่ยนแปลง](COMPARISON_FINAL.json)',
 '- [หลักฐานความครบถ้วน](INTEGRITY_FINAL.json)',
 '- [ผลตรวจหลังแก้ครบชุด](runs/http03/TEST_COMPLETE.json)',
 '- [Raw response หลังแก้](runs/http03/RESULTS.jsonl)',
 '', '## ขั้นถัดไปที่จำเป็นก่อนใช้จริง','',
 'ยืนยันขอบเขต/วันมีผลของตารางและเงื่อนไข VR จากเจ้าของ จัดคำแปลอังกฤษที่ขาด ตรวจ live bindings/provider ด้วยขั้นตอนที่เจ้าของอนุญาต แล้วเผยแพร่ draft ตามระบบ approvals ปัจจุบัน ผลรอบนี้เพียงพอสำหรับยืนยันการแก้ช่องโหว่ในชุดคำถามเดิม ไม่ใช่เหตุให้ประกาศว่าทุกหมวดพร้อมจริงหรือเปลี่ยน production อัตโนมัติ','']
(R/'FINAL_REPORT_TH.md').write_text('\n'.join(lines),'utf8')

# Detailed audit: every original strict failure plus any regression, including
# fixture misses. Preserve raw original grades and give source refs separately.
details=['# ตรวจสาเหตุและตัวอย่างทุกข้อที่ไม่ผ่านรอบก่อนแก้','',
 'อ่านคู่กับ FINAL_REPORT_TH.md ไม่ถือ extra claims ทั้งหมดเป็นเนื้อหาผิดและไม่ถือ missing fixture เป็นการตอบถูก รายการนี้อ่าน saved raw เท่านั้น ไม่ส่งคำถามใหม่','']
for k in a:
    if bg[k]['passed'] and ag[k]['passed'] and not (bg[k]['returned_claim_values_not_literal_in_body'] or ag[k]['returned_claim_values_not_literal_in_body']):continue
    x,y=b[k],a[k];g,h=bg[k],ag[k]
    if h['fixture_only_goal']:note='Source gap: goal fixture ไม่มีใน native; ตรวจเพิ่มว่าระบบไม่แทนด้วย source ผิดเรื่อง ไม่เอา safe abstention มานับ answered accuracy'
    elif k.startswith('C11') and h['actual_status']=='partial':note='Applicability gap: คืน recorded fields พร้อมข้อจำกัด source และ partial; ยังไม่ยืนยันสิทธิ์จอง/เวลาเปิดจริง'
    elif k.startswith('C13') and h['extra'] and not h['missing']:note='Granularity/overlap: goal clauses ครบ มี source summary เพิ่ม ต้องคง strict fail และไม่เรียก actual content failure อัตโนมัติ'
    elif h['passed']:note='ผ่าน source identity/value/state checks หลังแก้ ไม่ใช่ human semantic adjudication'
    else:note='ยังต้องตรวจรายละเอียดตาม source/สถานะ; ไม่อ้างว่าถูกทั้งหมด'
    details += [f'## {k} — {names[x["category"]]}','',x['question'],'',note,'',
       f"ก่อน: strict={g['passed']}, {g['classification']}, state={g['actual_status']}",'','```text',x['response'].get('answer',''),'```','',
       f"หลัง: strict={h['passed']}, {h['classification']}, state={h['actual_status']}",'','```text',y['response'].get('answer',''),'```','',
       '### Goal/source evidence','', '```json',json.dumps(expect[k]['goals'],ensure_ascii=False,indent=2),'```','',
       '### หลังแก้: additional/missing/pointer checks','', '```json',json.dumps({f:h[f] for f in ['missing','extra','wrong','evidence_mismatches','unknown_refs','reference_gaps','returned_claim_values_not_literal_in_body']},ensure_ascii=False,indent=2),'```','']
(R/'ROOT_CAUSE_REVIEW_TH.md').write_text('\n'.join(details),'utf8')
status=read(R/'STATUS.json');status.update(phase='complete',complete=True,completed_at=datetime.now().astimezone().isoformat(),final_report='FINAL_REPORT_TH.md',source_unchanged=True,model_verified=True)
(R/'STATUS.json').write_text(json.dumps(status,ensure_ascii=False,indent=2),'utf8')
print(json.dumps({'before':bs['ALL'],'after':as_['ALL'],'changes':{k:len(v) for k,v in changes.items()},'integrity':state,'report':str(R/'FINAL_REPORT_TH.md')},ensure_ascii=False))
